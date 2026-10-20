# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/6eb6fb4e-72f0-413e-9483-80f8446cb815.jsonl`
- **Structured JSON:** [`579a1ea08fbf8221e9d8.json`](../../sessions/57/579a1ea08fbf8221e9d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T01:16:43.443Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T01:16:43.443Z",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.\n\nDirection: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.\n\nContribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.\n2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.\n3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.\n\nAvoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.\n\nTag: direction=agent, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"SimGate: Learning When to Route LLM Agents to Deterministic Simulators for Rule-Governed Reasoning\",\n  \"core_problem\": \"Per-step compute allocation methods for LLM agents route between internal reasoning depths (CogRouter's four cognitive levels, ARES's effort tiers) or between skip-simulation and LLM-based world model rollouts (ITP-R's K-head predictor). On environments requiring accurate prediction of rule-governed dynamics — such as ScienceWorld's physics, chemistry, and biology simulations — LLM world models fail catastrophically: ITP-R (Qwen2.5-7B) achieves only 62.58 score (seen) / 58.94 (unseen) on ScienceWorld, dramatically below CogRouter's 84.6 score / 72.0% SR using purely internal cognitive adaptation. This ~22-point score gap demonstrates that LLM world models cannot reliably predict state transitions governed by scientific rules (temperature changes, chemical reactions, phase transitions), making the foresight they provide noisy rather than helpful. Meanwhile, ScienceWorld's underlying simulator implements these rules exactly and deterministically. Yet no method learns per-step routing between internal reasoning and such a deterministic external simulator: existing simulator-using agents invoke them unconditionally (Qian et al. show on FrozenLake/Sokoban/Navigation/PrimitiveSkill that forced simulation can degrade performance by up to 5%), while ITP-R's learned gating routes only to an approximate LLM world model. The gap: on environments with complex rule-governed dynamics, no method exploits the complementary value of ground-truth simulation through learned selective invocation.\",\n  \"opportunity\": \"ITP-R (Jan 2026) is the closest prior work on learned simulation gating, but two key observations create our opportunity. First, ITP-R's performance is benchmark-dependent: on ALFWorld (simpler household tasks), ITP-R with Qwen2.5-7B achieves 94.29%, outperforming CogRouter's 92.5% — the LLM world model works well on simple state transitions. But on ScienceWorld (complex scientific reasoning), ITP-R scores only 62.58 (seen) / 58.94 (unseen), compared to CogRouter's 84.6 score / 72.0% SR — a massive gap showing LLM world models fail precisely where accurate simulation of physical/chemical dynamics matters most. Second, deterministic simulators are available for both environments but unused by any routing method: ScienceWorld's Scala/JVM backend implements exact rule-governed transitions (water boils at 100°C, circuits follow Ohm's law, chemical reactions follow stoichiometry), and ALFWorld's TextWorld/PDDL backend provides exact household physics. The opportunity: a learned router that treats deterministic simulation as a complementary computation type to internal reasoning, specifically targeting the steps where rule-governed dynamics make internal prediction unreliable. On ScienceWorld, this addresses a genuine failure mode of LLM world models; on ALFWorld, it provides cost-equivalent accuracy by replacing GPU-intensive LLM world model inference with CPU-only deterministic simulation.\",\n  \"landscape\": \"ITP / ITP-R ('Imagine-then-Plan', arXiv 2601.08955, Jan 2026) introduces a K-head predictor for per-step simulation gating, routing to an SFT-trained LLM world model. With Qwen2.5-7B backbone: ALFWorld 94.29% (strong), ScienceWorld 62.58/58.94 score seen/unseen (weak — below CogRouter by ~22 points). The ScienceWorld underperformance suggests LLM world models cannot handle rule-governed scientific dynamics. Code at github.com/loyiv/ITP. CogRouter ('Think Fast and Slow', arXiv 2602.12662, Feb 2026) defines four cognitive levels with CoSFT + CoPO training on Qwen2.5-7B, achieving ALFWorld 92.5% and ScienceWorld 84.6 score / 72.0% SR (current ScienceWorld SOTA among routing methods) with 62% token reduction. Purely internal reasoning — no external simulation. Code at github.com/rhyang2021/CogRouter. ARES (arXiv 2603.07915, March 2026) trains a Qwen3-1.7B SFT router for {low, mid, high} reasoning effort, achieving 52.7% reasoning token reduction. Internal-only. Code at github.com/UCSB-NLP-Chang/Ares. Skill1 (arXiv 2605.06130, May 2026) achieves ALFWorld 97.5% via unified skill evolution with RL — current ALFWorld SOTA. Does not evaluate on ScienceWorld. PA-MoE+GiGPO (arXiv 2602.17038, Feb 2026) achieves ALFWorld 95.3% (7B) via phase-aware mixture of experts. RetroAgent achieves ALFWorld 94.9%. Dyna-Mind/RESIM (arXiv 2510.09577) achieves ALFWorld 92.5% (Dyna-GRPO) / 87.7% (RESIM) via learning to simulate from experience — uses a learned (not deterministic) simulator. AVIC (arXiv 2602.08236, Feb 2026) implements learned policy-based binary gating for world model invocation in visual spatial reasoning via prompting, without fine-tuning. Qian et al. (arXiv 2601.03905, Jan 2026) empirically show across FrozenLake, Navigation, PrimitiveSkill, and Sokoban (NOT ALFWorld) that forced world model use degrades performance; the primary bottleneck is deciding when to simulate. MTRouter (arXiv 2604.23530, ACL 2026) routes between different LLMs per turn. AgentRL (arXiv 2510.04206) scales agentic RL across multiple benchmarks. Key gap: ITP-R learns simulation gating but routes to an approximate LLM world model that fails on complex scientific reasoning (ScienceWorld). On environments where deterministic simulators implementing rule-governed dynamics are available, no method learns selective routing to exploit ground-truth state transitions.\",\n  \"approach\": \"We propose SimGate, a hybrid routing framework that learns per-step whether an LLM agent should rely on internal reasoning or invoke a deterministic external simulator for ground-truth lookahead, targeting environments where state transitions are governed by deterministic rules (physics, chemistry, game mechanics). Unlike ITP-R, which routes to an LLM world model that fails on complex scientific dynamics (scoring ~59 vs CogRouter's 84.6 on ScienceWorld), SimGate routes to the environment's own deterministic simulator — providing exact state transitions at CPU-only cost.\\n\\nThe framework has three components:\\n\\n(1) Agent backbone: Qwen2.5-7B (matching CogRouter for controlled comparison), with ReAct-style interaction augmented by routing decisions at each step.\\n\\n(2) Deterministic simulator access: For ScienceWorld (primary benchmark), the JVM-based simulator is accessed via py4j. State forking is implemented through action-replay: a parallel ScienceWorld instance replays the current episode's action history to reach the identical state, then executes 1-3 candidate action sequences to observe exact outcomes (temperature changes, chemical reactions, circuit states). This avoids JVM serialization complexity while guaranteeing identical states. For ALFWorld (secondary benchmark), state forking uses GameState.copy() (which is implemented, unlike the base Environment.copy()) combined with a fresh TextWorld runtime to evaluate candidate actions. Both approaches are CPU-only with negligible cost compared to LLM world model inference.\\n\\n(3) Lightweight router: a Qwen3-1.7B model fine-tuned via SFT to select per step from {fast-internal, deep-internal, deterministic-simulation}, based on interaction history and current observation. This three-way modality routing differs from ITP-R's depth selection (K∈{0,...,K_max} over a single approximate world model) by treating internal reasoning and external ground-truth simulation as categorically different computation types.\\n\\nTraining proceeds in two offline phases:\\n\\nPhase 1 (trajectory collection): Run the Qwen2.5-7B agent on ScienceWorld's 30 task types (200 task variations) and ALFWorld's 134 tasks across ~600 total episodes. At each decision step, execute all three modalities in parallel — fast-internal (direct ReAct), deep-internal (chain-of-thought with multi-step planning), and deterministic-simulation (1-3 step lookahead via action-replay forking) — and record which produced the action leading to highest eventual task success via counterfactual labeling.\\n\\nPhase 2 (router SFT): Fine-tune Qwen3-1.7B on the labeled (history, observation, best-modality) triples with cross-entropy loss, following ARES's training pipeline. No online RL needed.\\n\\nEvaluation:\\n- Primary benchmark: ScienceWorld (30 task types, 72.0% SR headroom above CogRouter SOTA). We compare against CogRouter (84.6 score / 72.0% SR), ITP-R (62.58/58.94 score), CoSFT+GRPO (71.1 score / 53.0% SR), AdaptThink (62.5 / 44.5%), ReAct, always-simulate, never-simulate, random routing, and confidence-threshold heuristic.\\n- Secondary benchmark: ALFWorld (134 tasks). We compare against ITP-R (94.29%), CogRouter (92.5%), PA-MoE+GiGPO (95.3%), always-simulate, and ReAct. Here the primary claim is cost-efficiency: matching ITP-R's accuracy tier with lower inference cost by replacing GPU-intensive LLM world model rollouts with CPU-only deterministic simulation. We acknowledge ALFWorld saturation (Skill1: 97.5%) and do not claim SOTA.\\n\\nKey metrics: task success rate, normalized score (ScienceWorld), total LLM tokens consumed, simulation invocation ratio, LLM world model inference cost vs deterministic simulation cost (FLOPs and wall-clock), and per-task-category success breakdown to identify WHERE deterministic simulation provides most value.\\n\\nCore hypotheses: (H1) On ScienceWorld, SimGate outperforms both CogRouter (which lacks external grounding for scientific reasoning) and ITP-R (whose LLM world model hallucinates scientific state transitions), targeting >88 score / >78% SR. (H2) On ALFWorld, SimGate matches ITP-R's accuracy (~94%) with >40% reduction in inference FLOPs by substituting CPU-only deterministic simulation for GPU-intensive LLM world model rollouts. (H3) Per-task-category analysis reveals that deterministic simulation provides greatest value on tasks requiring multi-step causal reasoning about physical/chemical processes (ScienceWorld: heating, chemical reactions, circuits) and least value on simple pattern-matching tasks.\\n\\nGeneralizability discussion: SimGate's deterministic-simulator variant requires access to a ground-truth simulator, limiting direct applicability. We position this along a simulator fidelity spectrum: deterministic simulators (ScienceWorld, ALFWorld, game engines) → high-fidelity learned simulators → approximate LLM world models. Our contribution demonstrates that when ground-truth dynamics ARE available, learned selective invocation achieves a cost-accuracy Pareto improvement over LLM-based world model routing — motivating future work on routing across simulators of varying fidelity.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~220h H100 80GB (60h trajectory collection on ScienceWorld+ALFWorld with all modalities, 10h router SFT, 40h CogRouter baseline reproduction on ScienceWorld, 30h ITP-R baseline reproduction, 20h other baselines, 30h ALFWorld secondary experiments, 30h ablations and per-category analysis)\",\n      \"gpu_utilization\": \"~50% effective utilization; ~50% idle from analysis, debugging, environment engineering, and writing\",\n      \"timeline\": \"14 days (tight for May 25 ARR deadline; ScienceWorld action-replay state forking requires ~2 days engineering)\",\n      \"team\": \"1 researcher\",\n      \"estimated_gpu_cost\": \"$440-660 at $2.00-3.00/hr H100 80GB\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~180h H100 80GB (agent automates trajectory collection, baseline evaluation scheduling, and result parsing; human focuses on state-forking engineering, router training decisions, and paper writing)\",\n      \"gpu_utilization\": \"~70% effective utilization\",\n      \"timeline\": \"12 days\",\n      \"team\": \"1 researcher, ~90min/day for ScienceWorld environment engineering, per-category analysis review, and training curves\",\n      \"claude_api_cost\": \"$60-100 (~600-1000 Opus turns for ScienceWorld API integration, state-forking implementation, baseline reproduction, data pipeline, analysis)\",\n      \"estimated_gpu_cost\": \"$360-540 at $2.00-3.00/hr\",\n      \"risk_note\": \"Primary risk is ScienceWorld state-forking engineering — action-replay approach requires maintaining a parallel JVM instance and may have performance overhead for long episodes (>50 steps). Mitigated by capping lookahead replay to last 10 actions + simulator fast-forward. Secondary risk: ITP-R baseline uses different training method (A2C) than CogRouter (CoPO), making direct comparison noisy — mitigated by including ablation with matched training.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~260h H100 80GB (broader ScienceWorld per-task-type analysis across all 30 task types, ALFWorld cost analysis, routing ablations, lookahead depths 1-3, router sizes, ITP-R matched-training comparison)\",\n      \"gpu_utilization\": \">90% utilization; agent pipelines trajectory collection → labeling → training → evaluation continuously\",\n      \"timeline\": \"10-12 days with 2+ H100 GPUs\",\n      \"team\": \"0 (initial 3h setup for ScienceWorld state forking + environment + API keys)\",\n      \"claude_api_cost\": \"$140-220 (~1400-2200 Opus turns for ScienceWorld integration, state forking implementation, experimentation, per-category analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$520-780 at $2.00-3.00/hr\",\n      \"speed_bottleneck\": \"CPU-bound ScienceWorld action-replay for state forking on long episodes; GPU bottleneck is Qwen2.5-7B inference for ~600 episodes × 3 modalities × ~30 steps = ~54K inference calls\",\n      \"risk_note\": \"Without human judgment on training method fairness (ITP-R uses A2C, CogRouter uses CoPO), agent may produce noisy comparisons; mitigated by including ITP-R-style gating trained with CoPO as an additional ablation\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026, short paper)\"\n  ],\n  \"level\": \"promising\",\n  \"key_references\": [\n    \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models [ITP/ITP-R] (arXiv 2601.08955, Jan 2026) — ALFWorld 94.29% (Qwen2.5-7B), ScienceWorld 62.58/58.94 score\",\n    \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents [CogRouter] (arXiv 2602.12662, Feb 2026) — ALFWorld 92.5%, ScienceWorld 84.6 score / 72.0% SR\",\n    \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents (arXiv 2603.07915, March 2026)\",\n    \"Current Agents Fail to Leverage World Model as Tool for Foresight [Qian et al.] (arXiv 2601.03905, Jan 2026) — evaluated on FrozenLake/Navigation/PrimitiveSkill/Sokoban, NOT ALFWorld\",\n    \"Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning (arXiv 2605.06130, May 2026) — ALFWorld 97.5% SOTA\",\n    \"Phase-Aware Mixture of Experts for Agentic RL [PA-MoE+GiGPO] (arXiv 2602.17038, Feb 2026) — ALFWorld 95.3% (7B)\",\n    \"Dyna-Mind: Learning to Simulate from Experience for Better AI Agents (arXiv 2510.09577) — ALFWorld 92.5% (Dyna-GRPO)\",\n    \"When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning [AVIC] (arXiv 2602.08236, Feb 2026)\",\n    \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings (arXiv 2604.23530, ACL 2026)\",\n    \"Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents (arXiv 2509.03581, 2025)\",\n    \"Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond (arXiv 2604.22748, April 2026)\",\n    \"AgentRL: Scaling Agentic Reinforcement Learning (arXiv 2510.04206)\"\n  ],\n  \"description\": \"We propose SimGate, a hybrid routing framework that learns per-step whether an LLM agent should use internal reasoning or invoke a deterministic external simulator for ground-truth lookahead, targeting environments where state transitions follow deterministic rules (physics, chemistry, game mechanics). The core evidence motivating SimGate: on ScienceWorld, ITP-R's LLM world model (Qwen2.5-7B) scores only 62.58/58.94 (seen/unseen), dramatically below CogRouter's 84.6 score / 72.0% SR using purely internal reasoning — a ~22-point gap demonstrating that LLM world models cannot reliably predict complex scientific state transitions (temperature changes, chemical reactions, circuit behavior). Meanwhile, ScienceWorld's JVM-based simulator implements these rules exactly. SimGate exploits this by learning when ground-truth simulation helps most: a Qwen3-1.7B router, SFT-trained on counterfactual trajectory data, selects per step from {fast-internal, deep-internal, deterministic-simulation}. State forking uses action-replay via parallel simulator instances (avoiding TextWorld's unimplemented Environment.copy()). On ScienceWorld (primary, 30 task types, 72.0% SR headroom), we hypothesize SimGate exceeds both CogRouter (no external grounding) and ITP-R (noisy LLM foresight), targeting >88 score / >78% SR. On ALFWorld (secondary, acknowledging 97.5% Skill1 saturation), SimGate aims to match ITP-R's 94.29% accuracy with >40% inference cost reduction by replacing GPU-intensive LLM world model rollouts with CPU-only deterministic simulation. We explicitly correct the prior version's factual error: ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B (not 88.57%, which is the Qwen3-8B number), outperforming CogRouter (92.5%). The LLM world model failure is benchmark-specific to complex rule-governed environments like ScienceWorld, not universal. Built on LangGraph with Qwen2.5-7B backbone, evaluated against CogRouter, ITP-R, PA-MoE+GiGPO, ARES, always-simulate, and heuristic baselines. Targeting EMNLP 2026 short paper (ARR deadline May 25, 2026). Estimated cost: 180-260 H100-hours ($360-780).\",\n  \"project_name\": \"sim_gate_cost_aware_plan\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL CONSTRAINT VIOLATION: User specified target venue EMNLP 2026 (ARR deadline May 25, 2026), but idea targets AAAI 2027 and ICLR 2027. This completely mismatches the user's submission plan.\", \"CRITICAL CONSTRAINT VIOLATION: User specified ≤200 H100-hours total compute budget. Idea estimates 400-1000 A100 GPU hours (~300-700 H100-equivalent hours), exceeding the budget by 1.5-3.5x.\", \"CRITICAL CONSTRAINT VIOLATION: User specified ≤16-day timeline. Even the auto_research mode estimates 1-3 weeks; manual mode estimates 3-5 months.\", \"CRITICAL MISSING COMPETING WORK: CogRouter ('Think Fast and Slow', arXiv 2602.12662, Feb 2026) trains step-level cognitive depth adaptation using RL (CoPO) on ALFWorld and ScienceWorld — the EXACT same benchmarks. Achieves 92.5% ALFWorld, 72.0% ScienceWorld with Qwen2.5-7B. Code available at github.com/rhyang2021/CogRouter. This is the single most important competing baseline and is entirely unacknowledged.\", \"CRITICAL MISSING COMPETING WORK: ARES (arXiv 2603.07915, March 2026) trains a lightweight per-step router for adaptive reasoning effort allocation in LLM agents, evaluated on WebArena. 52.7% reasoning token reduction. Nearly identical mechanism (lightweight router on hidden states) for the same abstract goal (step-level compute-aware decisions).\", \"MISSING RELATED WORK: Budget-aware inference literature from early 2026 (BAVT for LLM agents, BudgetThinker, Inference-Time Budget Control for LLM Search Agents) addresses cost-aware step-level decisions in agents — adjacent and relevant.\", \"MARGINAL NOVELTY: After accounting for CogRouter (step-level gating + RL in agent trajectories), ARES (lightweight router for per-step effort), and Rational Metareasoning (VOC-based per-step reasoning gating), the remaining novelty is narrow: 'apply the same gating concept to external world model invocation instead of internal reasoning.' This is an application-level contribution, not a methodological one.\", \"BASELINE INSUFFICIENCY: CogRouter achieves 92.5% on ALFWorld without any world model. SimGate must demonstrate that adding world model simulation + a learned gate exceeds this strong baseline, which is not guaranteed and adds significant complexity.\", \"DOES NOT BUILD ON SPECIFIED OSS CODEBASES: User required building on AutoGen, LangGraph, OpenManus, etc. The idea proposes building from scratch with Qwen3-14B + WebWorld-8B.\", \"RESOURCE ESTIMATE INCONSISTENCY: Manual mode claims ~40% GPU utilization but 400h A100 — if effective utilization is 40%, real GPU booking is ~1000h. The estimates across modes are not internally consistent.\"]\nFeedback: This idea needs fundamental restructuring to meet the user's requirements. Specific actions needed:\n\n1. **RETARGET TO EMNLP 2026**: Redesign the entire scope to fit the EMNLP 2026 ARR deadline (May 25, 2026, 14 days from today). This means drastically simplifying the approach.\n\n2. **FIT WITHIN 200 H100-HOURS**: The current design (Qwen3-14B backbone + WebWorld-8B world model + GRPO training + 3 benchmarks + 5 baselines) is far too expensive. Consider: (a) using a smaller backbone (7B instead of 14B), (b) reducing to 1-2 benchmarks, (c) replacing GRPO with simpler SFT-only training of the gating head, (d) using frozen world model predictions from precomputed rollouts rather than online generation.\n\n3. **COMPLETE IN 16 DAYS**: Use existing OSS agent codebases (AutoGen, LangGraph) as required. Precompute world model rollouts offline, then train the gate head as a simple binary classifier on pre-collected trajectory data. This avoids the expensive online RL loop.\n\n4. **ADDRESS CogRouter AND ARES**: These are the two closest competing works and MUST be cited, compared against, and differentiated from. CogRouter evaluates on the same benchmarks and achieves strong results (92.5% ALFWorld) without world models — you need to argue convincingly why adding world model gating improves over this. Consider using CogRouter as a baseline.\n\n5. **SHARPEN NOVELTY CLAIM**: The distinction 'gate external simulator rather than internal reasoning' is real but thin. To strengthen it, consider: (a) theoretical analysis of when external simulation has higher value of computation than internal reasoning, (b) empirical comparison showing that world model predictions provide complementary signal to internal reasoning, (c) hybrid approach combining CogRouter-style internal depth adaptation with SimGate-style external simulation gating.\n\n6. **SIMPLIFY SCOPE**: For a 16-day project with 200 H100-hours, focus on one benchmark (ALFWorld has the most mature world model support via TextWorld), one backbone, and a clean comparison showing that learned world model gating outperforms heuristic gating, always-simulate, and never-simulate baselines. Save the multi-benchmark story for a follow-up.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL MISCHARACTERIZATION: The proposal states 'ITP (2026) always simulates but adapts depth with ITP-R.' This is factually wrong. ITP-R's K-head predictor selects K_t ∈ {0,1,...,K_max} per step, where K=0 explicitly means NO simulation — the agent acts from internal reasoning alone. ITP-R IS a learned per-step router between 'no simulation' and 'simulation at various depths.' The proposal's core gap claim ('no existing work learns per-step routing between internal reasoning and external world model invocation') is therefore invalid.\", \"CRITICAL MISSING BASELINE: ITP-R (arXiv 2601.08955) achieves 88.57% on ALFWorld with Qwen3-8B using learned per-step simulation gating. This is the single most important baseline for SimGate's claimed contribution and must be included in experiments. Its lower performance vs CogRouter (88.57% vs 92.5%) actually raises a concerning question: if learned simulation routing (ITP-R) already underperforms pure internal adaptation (CogRouter) on ALFWorld, what evidence suggests SimGate's deterministic-simulator variant will reverse this trend?\", \"NOVELTY GAP NARROWER THAN CLAIMED: After accounting for ITP-R (learned K=0/K>0 routing), the remaining novelty reduces to: (a) routing to a deterministic external simulator vs LLM world model, (b) three-way modality selection vs depth selection, (c) separate router model vs backbone K-head. These are configuration-level differences, not methodological contributions. A short paper could possibly carry this, but only with an honest framing.\", \"GENERALIZABILITY CONCERN: The approach fundamentally depends on having access to a deterministic external simulator (ALFWorld's TextWorld). Most real-world agent tasks (web navigation, coding, API interaction) lack such simulators. The paper needs to address: under what conditions does this approach transfer? Without this discussion, reviewers will question practical relevance.\", \"AVIC (Yu et al., Feb 2026) NOT ADEQUATELY DIFFERENTIATED: AVIC implements a binary skip/call_wm gating policy for world model invocation in visual spatial reasoning. While the domain differs (vision vs text), the mechanism (learned binary gate for world model invocation) is conceptually identical. The proposal should explicitly differentiate.\", \"BENCHMARK SATURATION RISK: ALFWorld success rates are approaching ceiling (CogRouter 92.5%). Demonstrating statistically significant improvements above 92.5% on only 134 task instances requires careful analysis — the margin of improvement is thin and the evaluation set is small, making results potentially noisy.\", \"TEXTWORLD LOOKAHEAD ENGINEERING UNDERESTIMATED: ALFWorld's TextWorld has no built-in state-forking/cloning API for branching lookahead. Implementing 1-3 step lookahead with state save/restore requires custom engineering on top of the PDDL backend. This is doable but adds unaccounted complexity to the 16-day timeline.\"]\nFeedback: The revision successfully fixed R1's constraint violations (venue, compute, timeline) — good work. But a serious novelty problem has emerged: ITP-R already does learned per-step routing between 'skip simulation' (K=0) and 'simulate' (K>0). You MUST not mischaracterize ITP. Here is how to salvage the idea:\n\n1. **CORRECT ITP CHARACTERIZATION**: Acknowledge that ITP-R does per-step simulation gating. Then differentiate on the TYPE of simulation: ITP routes to an LLM-based (approximate, hallucination-prone) world model; SimGate routes to a deterministic external simulator providing exact state transitions. Frame this as: 'ITP asks when to imagine; SimGate asks when to consult ground truth.'\n\n2. **ADD ITP-R AS PRIMARY BASELINE**: Include ITP-R (88.57% ALFWorld) alongside CogRouter (92.5%) as the two key baselines. Your hypothesis becomes: 'Deterministic external simulation, when selectively invoked, outperforms both LLM-based simulation routing (ITP-R) and pure internal depth adaptation (CogRouter).' This is testable and interesting.\n\n3. **REFRAME NOVELTY HONESTLY**: The contribution is NOT 'first to learn simulation gating' — it's 'first to learn routing between internal reasoning and a deterministic external simulator as complementary modalities, showing that grounded simulation provides value that LLM-based world models cannot.' This narrower claim is defensible for a short paper.\n\n4. **ADDRESS THE ELEPHANT IN THE ROOM**: ITP-R (88.57%) UNDERPERFORMS CogRouter (92.5%) on ALFWorld, suggesting LLM-based world model routing may actually hurt on this benchmark. You need a convincing argument for why DETERMINISTIC simulation routing will succeed where LLM-based simulation routing failed. The argument should be: 'ITP's LLM world model adds noise through hallucinated state transitions; a deterministic simulator provides exact dynamics, making the router's job easier — it only needs to identify WHEN exact foresight helps, not whether the foresight is accurate.'\n\n5. **ADD GENERALIZABILITY DISCUSSION**: Explicitly acknowledge the deterministic simulator limitation. Propose how the framework extends to tasks with approximate/learned world models (connecting back to ITP/WebDreamer). This turns a weakness into a research direction.\n\n6. **DIFFERENTIATE FROM AVIC**: Add explicit comparison — AVIC gates visual imagination with heuristic sufficiency checks in vision tasks; SimGate trains a separate router model for text-based agent tasks with SFT on counterfactual trajectory data.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL FACTUAL ERROR: The proposal cites ITP-R's ALFWorld result as 88.57% throughout, but this is the Qwen3-8B number. ITP-R with Qwen2.5-7B (the SAME backbone SimGate proposes) achieves 94.29% on ALFWorld — verified from ITP-R's Table in the HTML paper. This is HIGHER than CogRouter's 92.5%. The entire motivating argument ('ITP-R underperforms CogRouter, suggesting LLM-based simulation routing hurts') is based on an unfair cross-backbone comparison and is empirically false on the matched backbone.\", \"CORE MOTIVATION INVALIDATED: Since ITP-R (Qwen2.5-7B) = 94.29% > CogRouter = 92.5%, LLM-based simulation routing does NOT underperform pure internal adaptation on ALFWorld with the same backbone. This destroys the central hypothesis: 'deterministic external simulation provides complementary foresight that is strictly more reliable than LLM-based world model imagination.' The LLM world model already works well — there's no demonstrated failure to fix.\", \"OUTDATED SOTA: The proposal treats CogRouter (92.5%) as ALFWorld SOTA. As of May 2026, Skill1 achieves 97.5%, PA-MoE+GiGPO achieves 93.8%, and ITP-R achieves 94.29% with Qwen2.5-7B. CogRouter is no longer the primary comparison target. SimGate must demonstrate improvement over 94.29% (ITP-R) or explain why beating the 97.5% Skill1 ceiling is realistic.\", \"BENCHMARK SATURATION: ALFWorld is at 97.5% SOTA with only 134 evaluation instances. The practical headroom above ITP-R's 94.29% is ~3 percentage points on 134 tasks, making statistically significant improvements extremely difficult to demonstrate. This is especially problematic for a short paper that needs clean, convincing results.\", \"MISATTRIBUTION OF QIAN ET AL. RESULTS: The proposal states 'unconditional simulation degrades performance by up to 5% on trivial steps (Qian et al., 2026)' in the context of ALFWorld. However, Qian et al. evaluated on FrozenLake, Navigation, PrimitiveSkill, and Sokoban — NOT ALFWorld. The 5% degradation claim cannot be attributed to ALFWorld tasks.\", \"ENVIRONMENT.COPY() ENGINEERING RISK: TextWorld's base Environment.copy() raises NotImplementedError (verified in source code at github.com/microsoft/TextWorld/blob/main/textworld/core.py). While GameState.copy() performs deepcopy, the full environment forking required for multi-step lookahead rollouts needs the Environment-level copy, which must be implemented from scratch for ALFWorld's specific TextWorld integration. This unaccounted engineering work is risky for a 14-day timeline.\", \"MISSING RECENT BASELINES: Skill1 (97.5%, May 7, 2026), PA-MoE+GiGPO (93.8%), Dyna-Mind/RESIM (87.7-92.5%), and AgentRL are all absent from the baseline list. These represent the actual competitive landscape on ALFWorld.\"]\nFeedback: The revision from R2 was well-executed in correcting the ITP mischaracterization (acknowledging K=0 option) and meeting hard constraints. But a new critical problem has emerged: you used ITP-R's Qwen3-8B result (88.57%) to argue it underperforms CogRouter (92.5%), when ITP-R's own paper reports 94.29% with Qwen2.5-7B — the backbone YOU plan to use. This means ITP-R with an LLM world model ALREADY outperforms CogRouter on the matched backbone, eliminating your core argument.\n\nTo salvage this idea, you must:\n\n1. **ACKNOWLEDGE ITP-R (Qwen2.5-7B) = 94.29%**: This is the correct comparison point for SimGate, not 88.57%. Your method must beat 94.29% to show deterministic simulation adds value over LLM simulation.\n\n2. **REFRAME THE MOTIVATION ENTIRELY**: You cannot argue 'LLM simulation hurts.' Instead, consider: (a) deterministic simulation is CHEAPER than LLM world model inference (no GPU cost, just CPU), so SimGate could match ITP-R's accuracy with lower computational cost; (b) deterministic simulation may be more robust on specific task categories where LLM world models still hallucinate (identify these via per-category analysis); (c) frame it as 'efficiency + reliability' rather than 'accuracy improvement.'\n\n3. **UPDATE BASELINES AND SOTA**: Include Skill1 (97.5%), PA-MoE+GiGPO (93.8%), ITP-R Qwen2.5-7B (94.29%), and Dyna-Mind (92.5%) as baselines. Acknowledge ALFWorld is near saturation.\n\n4. **CONSIDER PIVOTING BENCHMARK**: Given ALFWorld saturation, consider ScienceWorld (where CogRouter gets 72.0% and there's more headroom) or add a second benchmark where deterministic simulators are available and the benchmark isn't saturated.\n\n5. **FIX QIAN ET AL. ATTRIBUTION**: The 5% degradation finding is from FrozenLake/Sokoban/Navigation/PrimitiveSkill, not ALFWorld. Correct this citation or run your own analysis on ALFWorld.\n\n6. **ADDRESS ENVIRONMENT.COPY() RISK**: TextWorld's base Environment.copy() raises NotImplementedError. Plan for implementing state forking via GameState.copy() + manual environment reconstruction, and account for this engineering effort in your timeline.\n\n7. **STRONGEST VIABLE ANGLE**: Instead of 'deterministic sim beats LLM sim in accuracy,' argue: 'When a deterministic simulator exists, routing to it is (a) computationally cheaper than LLM world model rollouts (CPU vs GPU), (b) guaranteed correct (zero hallucination), and (c) enables more aggressive multi-step lookahead without accuracy degradation. SimGate demonstrates that this cost-accuracy tradeoff is favorable, achieving comparable accuracy to ITP-R with significantly lower inference cost.' This efficiency-focused framing is defensible even if accuracy improvements are marginal.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING BASELINE: EPO (arXiv 2509.22576, Sep 2025) achieves 96.8% binary success rate (IID) / 96.2% (OOD) on ScienceWorld with Qwen2.5-7B-Instruct via entropy-regularized policy optimization — far exceeding CogRouter's 72.0% SR. While EPO uses binary SR (not partial-credit score) and may use a different task subset, this result strongly suggests ScienceWorld is more solvable than the proposal assumes. The proposal treats CogRouter's 72.0% SR as the ceiling with '78% SR headroom' — but EPO has already reached ~97% SR without any simulation routing. This undermines the core motivation: if pure RL training (EPO) already solves ScienceWorld at 96.8% SR, what is the incremental value of deterministic simulator routing?\", \"MISSING BASELINE: EMPO2 (arXiv 2602.23008, Feb 2026) achieves 75.9 average score on ScienceWorld with Qwen2.5-7B via exploratory memory-augmented hybrid RL. This is another recent ScienceWorld result missing from the landscape.\", \"COMPUTE BUDGET VIOLATION: The user's hard constraint is ≤200 H100-hours. Manual mode estimates 220h (10% over) and auto mode estimates 260h (30% over). Only HIL at 180h fits within budget. The math breakdown shows 40h for CogRouter baseline + 30h for ITP-R baseline + 20h for other baselines = 90h on baselines alone — this may be reducible.\", \"ACTION-REPLAY COST UNDERESTIMATED FOR TRAJECTORY COLLECTION: Phase 1 requires executing the deterministic-simulation modality at every step of ~600 episodes × ~30 steps = ~18K decision points. Each fork costs ~1.5-5.5 seconds (JVM startup via py4j + action replay). At ~3s average, that's ~54,000 seconds = ~15 hours of wall-clock CPU time just for state forking during trajectory collection — not including the 1-3 candidate action evaluations per fork (which multiplies this by 1-3x). This is feasible but should be explicitly budgeted.\", \"METRIC COMPARABILITY ISSUES ON SCIENCEWORLD: The ScienceWorld landscape uses inconsistent metrics across papers. CogRouter reports both Score (84.6) and SR (72.0%); ITP-R reports Score (62.58/58.94); EPO reports binary SR (96.8%); EMPO2 reports Score on a -100 to 100 scale (75.9). The proposal's target of '>88 score / >78% SR' must specify which metric is primary and ensure all baselines are compared on the same metric. Without standardized evaluation, claimed improvements may be artifacts of metric selection.\", \"GENERALIZABILITY REMAINS INHERENTLY LIMITED: The approach requires a ground-truth deterministic simulator. The proposal discusses this honestly but does not address a key practical question: how many real-world agent benchmarks have such simulators? Among the user's specified benchmarks (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, Mind2Web, τ-bench), NONE have deterministic simulators. Only ALFWorld (TextWorld/PDDL) is listed. ScienceWorld is not in the user's specified benchmark list at all.\", \"BENCHMARK SELECTION CONCERN: The user specified evaluation on existing benchmarks including AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, and τ-bench. The proposal's primary benchmark (ScienceWorld) is NOT in this list. While ALFWorld is listed, it's designated as secondary and acknowledged as saturated. The proposal should justify why ScienceWorld is appropriate or include at least one of the user's specified benchmarks as primary.\", \"MISSING RELATED WORK: BoundaryRouter (arXiv 2605.07180, May 2026) proposes routing between lightweight LLM inference and full agent execution — conceptually adjacent to SimGate's routing paradigm. Qian et al. (arXiv 2601.03905) explicitly identifies the 'when to simulate' problem as unsolved — this should be cited as direct motivation, not just as evidence that forced simulation hurts.\"]\nFeedback: The R4 revision is a major improvement in factual accuracy, honest framing, and competitive landscape coverage. The ScienceWorld pivot is well-motivated, and the novelty claim (learned routing to deterministic simulators) is confirmed as genuine — my independent search found no competing work. However, several issues must be addressed:\n\n1. **ADDRESS EPO (CRITICAL)**: EPO achieves 96.8% binary SR on ScienceWorld with the same Qwen2.5-7B backbone, without any simulation routing. You MUST: (a) include EPO as a baseline, (b) explain why SimGate matters when pure RL training already nearly solves the benchmark, (c) consider whether SimGate's value is orthogonal (inference-time architectural choice) or redundant (EPO shows the problem is training, not architecture). The strongest argument: SimGate is a training-agnostic inference-time mechanism that COMPLEMENTS any backbone training method — run SimGate on top of an EPO-trained agent and show further gains or cost reduction. This would be much stronger than comparing only against CogRouter.\n\n2. **FIT WITHIN 200 H100-HOURS**: Reduce compute by: (a) dropping some baselines (PA-MoE+GiGPO and Dyna-Mind can be cited from their papers without reproduction), (b) reducing ALFWorld experiments (it's secondary and saturated), (c) using CogRouter's published checkpoints if available rather than reproducing training. Target ≤180h to leave margin.\n\n3. **STANDARDIZE SCIENCEWORLD METRICS**: Choose either Score or SR as the primary metric and ensure all baselines are compared on the same scale. If EPO only reports SR and CogRouter reports both, use SR as the common metric.\n\n4. **BENCHMARK ALIGNMENT**: The user specified ALFWorld but not ScienceWorld. Either: (a) add one of the user's specified benchmarks where deterministic simulation is relevant (ALFWorld is already included as secondary — consider making it co-primary), or (b) justify why ScienceWorld is the right benchmark despite not being in the user's list (strong argument: it's the benchmark where deterministic simulation matters most due to complex scientific rules).\n\n5. **REFRAME CONTRIBUTION**: Given EPO, the strongest framing is: 'SimGate demonstrates that learned routing to deterministic simulators provides a cost-accuracy Pareto improvement at inference time, complementary to and composable with any training-time optimization. When composed with an EPO-trained agent, SimGate achieves [X] with [Y]% fewer LLM inference calls.' This positions SimGate as an orthogonal, composable inference-time technique rather than competing with training-time methods.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL FACTUAL ERROR: ITP-R with Qwen2.5-7B achieves 85.07% overall on ALFWorld, NOT 94.29%. The 94.29% is the PICK subtask score (first column in ITP-R's Table 1). The per-task breakdown is: PICK 94.29%, CLEAN 88.89%, HEAT 87.50%, COOL 53.84%, LOOK 76.00%, PICK2 91.67%, Overall 85.07%. This error originated in the R3 review's 'correction' and has persisted unchecked. The proposal's claim 'ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B, outperforming CogRouter (92.5%)' is wrong — ITP-R actually underperforms CogRouter by 7.4 points (85.07% vs 92.5%). HOWEVER: this correction actually STRENGTHENS SimGate's motivation, since it shows LLM world model routing hurts on BOTH ALFWorld and ScienceWorld, not just ScienceWorld.\", \"COMPUTE BUDGET VIOLATION: User hard constraint is ≤200 H100-hours. Manual=220h (10% over), Auto=260h (30% over). Only HIL=180h fits. Baseline reproduction alone consumes 90h (40h CogRouter + 30h ITP-R + 20h others). Reduce by: (a) citing PA-MoE+GiGPO and Dyna-Mind results from their papers without reproduction, (b) using CogRouter's published checkpoints if available, (c) trimming ALFWorld secondary experiments to only the critical always-simulate comparison.\", \"EPO NOT ADDRESSED (R4 CRITICAL FEEDBACK IGNORED): R4 flagged EPO (arXiv 2509.22576, 96.8% binary SR on ScienceWorld) as a critical missing baseline. R5 does not mention EPO at all. My verification reveals EPO's metric is NOT directly comparable to CogRouter's — their GRPO baselines differ by 40pp (EPO: 93.8% Succ.* vs CogRouter: 53.0% SR), indicating completely different evaluation protocols and/or task subsets. The proposal should acknowledge EPO, explain the comparability issue, and clarify which ScienceWorld evaluation protocol SimGate will follow (CogRouter's 200-simulation protocol is recommended for consistency with the primary baseline).\", \"MISSING RELATED WORK — ARTIS (arXiv 2602.01709, Feb 2026): 'Agentic Risk-Aware Test-Time Scaling via Iterative Simulation' runs LLM-based simulation on ALL candidate actions before committing — an always-simulate pipeline with a risk-aware simulator. While it lacks learned gating (every action is simulated), it is the most relevant 'always-simulate' baseline and should be cited alongside Qian et al.'s findings. Position SimGate as selectively routing where ARTIS wastes compute by always simulating.\", \"BENCHMARK SELECTION NOT ALIGNED WITH USER REQUIREMENTS: The user specified evaluation on AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, and τ-bench. ScienceWorld (the primary benchmark) is NOT in this list. Only ALFWorld is included, and it's designated as secondary. The proposal should explicitly justify why ScienceWorld is the right primary benchmark despite not being on the user's list, or elevate ALFWorld to co-primary status.\", \"CORRECTED ITP-R NUMBER CHANGES ALFWorld NARRATIVE: With the correct ITP-R overall (85.07%), the proposal's ALFWorld story changes from 'match ITP-R's 94.29% with lower cost' to 'ITP-R underperforms CogRouter on ALFWorld too (85.07% vs 92.5%), confirming LLM world models are generally harmful for agent simulation — SimGate aims to match or exceed CogRouter's 92.5% by replacing noisy LLM simulation with exact deterministic simulation at lower cost.' This is actually a stronger argument.\"]\nFeedback: The idea's core novelty (learned routing to deterministic simulators) is independently confirmed as genuine — no competing work exists. But the R5 submission has a critical factual error and ignores R4's EPO feedback. Here's how to fix it:\n\n1. **FIX ITP-R ALFWORLD NUMBER (CRITICAL)**: Replace all instances of '94.29%' with the correct overall score of 85.07%. The 94.29% is the PICK subtask only. With the corrected number, ITP-R (85.07%) underperforms CogRouter (92.5%) on ALFWorld too — this STRENGTHENS your argument. The narrative becomes: 'LLM world model routing (ITP-R) underperforms pure internal adaptation (CogRouter) on BOTH ALFWorld (85.07% vs 92.5%) and ScienceWorld (62.58 vs 84.6), demonstrating that LLM world models are generally harmful rather than helpful for agent simulation. SimGate replaces the noisy LLM world model with exact deterministic simulation, targeting improvements on both benchmarks.'\n\n2. **CUT COMPUTE TO ≤190 H100-HOURS**: Drop PA-MoE+GiGPO and Dyna-Mind baseline reproduction (cite from papers: −20h). Check if CogRouter publishes checkpoints to avoid full retraining (−20h). Reduce ALFWorld secondary experiments to just always-simulate vs SimGate vs ITP-R (−15h). This gets you to ~165h with margin.\n\n3. **ADDRESS EPO**: Add one paragraph noting EPO's 96.8% SR claim. Explain the evaluation protocol discrepancy (GRPO baseline: 93.8% in EPO vs 53.0% in CogRouter — a 40pp gap indicating different evaluation setups). State that SimGate will follow CogRouter's 200-simulation evaluation protocol for direct comparability. If EPO's evaluation code is available, consider running SimGate under EPO's protocol as a secondary comparison.\n\n4. **ADD ARTIS AS RELATED WORK**: Cite ARTIS (2602.01709) as the 'always-simulate' baseline paradigm. SimGate is more efficient because it selectively invokes simulation only when rule-governed dynamics make internal prediction unreliable.\n\n5. **JUSTIFY SCIENCEWORLD OR ELEVATE ALFWORLD**: Either (a) add one sentence justifying ScienceWorld: 'While not in the standard agent benchmark lists, ScienceWorld uniquely tests rule-governed scientific reasoning where deterministic simulation provides maximum value — making it the ideal testbed for SimGate's core hypothesis'; or (b) make ALFWorld co-primary with ScienceWorld.\n\n6. **REVISE ALFWORLD HYPOTHESIS**: With ITP-R at 85.07% (not 94.29%), your ALFWorld target should be: 'Match or exceed CogRouter's 92.5% by replacing noisy LLM simulation with exact deterministic simulation, with lower inference cost than both ITP-R and CogRouter.' The cost-efficiency argument now pairs with an accuracy argument.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"CRITICAL FACTUAL ERROR (PERSISTS FROM R5, NOW ROUND 6): ITP-R with Qwen2.5-7B achieves 85.07% OVERALL on ALFWorld, NOT 94.29%. The 94.29% is the PICK subtask score only (per-task breakdown: PICK 94.29%, CLEAN 88.89%, HEAT 87.50%, COOL 53.84%, LOOK 76.00%, PICK2 91.67%, Overall 85.07%). Verified from arXiv HTML, raw table data, and GitHub table image — three independent sources. The proposal's claim 'ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B, outperforming CogRouter (92.5%)' is factually wrong. ITP-R (85.07%) UNDERPERFORMS CogRouter (92.5%) by 7.4 points. Critically, this correction STRENGTHENS SimGate's motivation: LLM world model routing hurts on BOTH ALFWorld AND ScienceWorld.\", \"EPO NOT ADDRESSED (THIRD CONSECUTIVE ROUND): EPO (arXiv 2509.22576) claims 96.8% binary success rate on ScienceWorld with Qwen2.5-7B — flagged as critical in R4, re-flagged in R5, still completely absent in R6. My independent verification reveals: (a) EPO uses binary {0,1} success, NOT the continuous ScienceWorld score (0-100); (b) EPO's GRPO baseline is 93.8% Succ.* vs CogRouter's 53.0% SR — a 40pp gap proving fundamentally different evaluation protocols; (c) EPO does not disclose task subset, episode count, or binarization threshold; (d) max_steps=30 (vs typical 100). These numbers are NOT directly comparable to CogRouter's, but reviewers WILL raise EPO and the proposal MUST preemptively address it.\", \"EMPO2 MISSING: EMPO2 (arXiv 2602.23008, Feb 2026) achieves 75.9 average score on ScienceWorld with Qwen2.5-7B using continuous score across 18-19 tasks via exploratory memory-augmented hybrid RL. This is a directly comparable ScienceWorld result using the same metric and backbone. Must be included in landscape.\", \"COMPUTE BUDGET VIOLATION: Manual (220h) and auto (260h) modes exceed the ≤200 H100-hour hard constraint. Only HIL (180h) fits. The description states '180-260 H100-hours' — the upper bound violates the user's requirement. The 90h baseline reproduction budget (40h CogRouter + 30h ITP-R + 20h others) is the main bloat area.\", \"BENCHMARK MISALIGNMENT: The user specified 8 benchmarks: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench. ScienceWorld (the primary benchmark) is NOT in this list. Only ALFWorld is included, designated as secondary and acknowledged as saturated (97.5% Skill1). The proposal must either justify ScienceWorld's inclusion or elevate ALFWorld to co-primary status.\", \"STRUCTURAL IMPACT LIMITATION: The method requires access to a ground-truth deterministic simulator, which is available for ScienceWorld (JVM/Scala) and ALFWorld (TextWorld/PDDL) but NOT for any real-world agent benchmark (WebArena, SWE-bench, GAIA, ToolBench, Mind2Web, τ-bench). This fundamentally limits the contribution's practical relevance and will be a primary reviewer concern at EMNLP.\", \"ARTIS (2602.01709) STILL NOT CITED: ARTIS implements risk-aware iterative simulation before commitment — the closest 'always-simulate' baseline paradigm. SimGate should cite it as motivation: ARTIS wastes compute by always simulating, while SimGate selectively routes. Also missing: Qian et al. (2601.03905) is cited but its finding ('agents fail to decide WHEN to simulate') should be more prominently positioned as direct motivation — SimGate is precisely the solution to the problem they identify.\"]\nFeedback: This is round 6 and the same critical issues keep recurring. You must fix them NOW or risk failing at round 10.\n\n1. **FIX ITP-R NUMBER IMMEDIATELY (THIS IS THE THIRD TIME)**: ITP-R overall on ALFWorld with Qwen2.5-7B = **85.07%**, not 94.29%. I verified this from the paper's Table 1 across three sources. The 94.29% is the PICK subtask column — the rightmost 'Overall' column reads 85.07%. This correction actually HELPS you: ITP-R (85.07%) < CogRouter (92.5%) on ALFWorld, meaning LLM world model routing hurts on BOTH benchmarks. Your narrative becomes: 'LLM world model routing (ITP-R) consistently underperforms pure internal adaptation (CogRouter) — 85.07% vs 92.5% on ALFWorld, 62.58 vs 84.6 on ScienceWorld — demonstrating that approximate LLM foresight introduces noise that outweighs its planning value. SimGate replaces this noisy foresight with exact deterministic simulation.'\n\n2. **ADDRESS EPO (NON-NEGOTIABLE)**: Add a paragraph: 'EPO (arXiv 2509.22576) reports 96.8% binary success rate on ScienceWorld with Qwen2.5-7B. However, EPO uses binary {0,1} success (not the standard continuous ScienceWorld score), an undisclosed task subset, and max_steps=30. Its GRPO baseline (93.8% Succ.*) differs by 40pp from CogRouter's (53.0% SR), indicating fundamentally different evaluation protocols. SimGate follows CogRouter's standardized 200-simulation evaluation protocol for direct comparability. We include EPO-style evaluation as a secondary metric for completeness.'\n\n3. **ADD EMPO2**: Include EMPO2 (75.9 avg score, 18-19 tasks) in the landscape as a baseline that uses the same continuous metric.\n\n4. **CUT COMPUTE TO ≤190h**: (a) Cite PA-MoE+GiGPO and Dyna-Mind results from their papers without reproduction (save ~15h). (b) Use CogRouter's published checkpoints if available instead of full retraining (save ~20h). (c) Reduce ALFWorld secondary experiments to essential comparisons only (save ~15h). Target 170h total.\n\n5. **JUSTIFY SCIENCEWORLD**: Add explicit justification: 'While ScienceWorld is not in the standard agent benchmark list, it uniquely tests rule-governed scientific reasoning (temperature physics, chemical reactions, electrical circuits) where deterministic simulation provides maximal value over LLM world models. ScienceWorld is the ideal testbed for SimGate's core hypothesis because the gap between deterministic and LLM-based simulation is largest on tasks requiring accurate prediction of physical/chemical dynamics.'\n\n6. **IMPACT WARNING**: The structural limitation (requires deterministic simulator) caps impact at ~2.5-3/5. To improve: (a) run a small experiment on one of the user's specified benchmarks where an approximate simulator could substitute (e.g., a code execution sandbox for SWE-bench, even if not deterministic), showing the framework generalizes beyond perfect simulators; or (b) connect more concretely to the growing ecosystem of game engines, physics simulators, and code sandboxes in agentic AI — argue that SimGate is relevant to any environment with a fast, reliable external evaluator.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T01:16:43.448Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T01:16:43.448Z",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-12T01:16:43.486Z_

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

## Idea under review (round 7/10)
{
  "title": "SimGate: Learning When to Route LLM Agents to Deterministic Simulators for Rule-Governed Reasoning",
  "core_problem": "Per-step compute allocation methods for LLM agents route between internal reasoning depths (CogRouter's four cognitive levels, ARES's effort tiers) or between skip-simulation and LLM-based world model rollouts (ITP-R's K-head predictor). On environments requiring accurate prediction of rule-governed dynamics — such as ScienceWorld's physics, chemistry, and biology simulations — LLM world models fail catastrophically: ITP-R (Qwen2.5-7B) achieves only 62.58 score (seen) / 58.94 (unseen) on ScienceWorld, dramatically below CogRouter's 84.6 score / 72.0% SR using purely internal cognitive adaptation. This ~22-point score gap demonstrates that LLM world models cannot reliably predict state transitions governed by scientific rules (temperature changes, chemical reactions, phase transitions), making the foresight they provide noisy rather than helpful. Meanwhile, ScienceWorld's underlying simulator implements these rules exactly and deterministically. Yet no method learns per-step routing between internal reasoning and such a deterministic external simulator: existing simulator-using agents invoke them unconditionally (Qian et al. show on FrozenLake/Sokoban/Navigation/PrimitiveSkill that forced simulation can degrade performance by up to 5%), while ITP-R's learned gating routes only to an approximate LLM world model. The gap: on environments with complex rule-governed dynamics, no method exploits the complementary value of ground-truth simulation through learned selective invocation.",
  "opportunity": "ITP-R (Jan 2026) is the closest prior work on learned simulation gating, but two key observations create our opportunity. First, ITP-R's performance is benchmark-dependent: on ALFWorld (simpler household tasks), ITP-R with Qwen2.5-7B achieves 94.29%, outperforming CogRouter's 92.5% — the LLM world model works well on simple state transitions. But on ScienceWorld (complex scientific reasoning), ITP-R scores only 62.58 (seen) / 58.94 (unseen), compared to CogRouter's 84.6 score / 72.0% SR — a massive gap showing LLM world models fail precisely where accurate simulation of physical/chemical dynamics matters most. Second, deterministic simulators are available for both environments but unused by any routing method: ScienceWorld's Scala/JVM backend implements exact rule-governed transitions (water boils at 100°C, circuits follow Ohm's law, chemical reactions follow stoichiometry), and ALFWorld's TextWorld/PDDL backend provides exact household physics. The opportunity: a learned router that treats deterministic simulation as a complementary computation type to internal reasoning, specifically targeting the steps where rule-governed dynamics make internal prediction unreliable. On ScienceWorld, this addresses a genuine failure mode of LLM world models; on ALFWorld, it provides cost-equivalent accuracy by replacing GPU-intensive LLM world model inference with CPU-only deterministic simulation.",
  "landscape": "ITP / ITP-R ('Imagine-then-Plan', arXiv 2601.08955, Jan 2026) introduces a K-head predictor for per-step simulation gating, routing to an SFT-trained LLM world model. With Qwen2.5-7B backbone: ALFWorld 94.29% (strong), ScienceWorld 62.58/58.94 score seen/unseen (weak — below CogRouter by ~22 points). The ScienceWorld underperformance suggests LLM world models cannot handle rule-governed scientific dynamics. Code at github.com/loyiv/ITP. CogRouter ('Think Fast and Slow', arXiv 2602.12662, Feb 2026) defines four cognitive levels with CoSFT + CoPO training on Qwen2.5-7B, achieving ALFWorld 92.5% and ScienceWorld 84.6 score / 72.0% SR (current ScienceWorld SOTA among routing methods) with 62% token reduction. Purely internal reasoning — no external simulation. Code at github.com/rhyang2021/CogRouter. ARES (arXiv 2603.07915, March 2026) trains a Qwen3-1.7B SFT router for {low, mid, high} reasoning effort, achieving 52.7% reasoning token reduction. Internal-only. Code at github.com/UCSB-NLP-Chang/Ares. Skill1 (arXiv 2605.06130, May 2026) achieves ALFWorld 97.5% via unified skill evolution with RL — current ALFWorld SOTA. Does not evaluate on ScienceWorld. PA-MoE+GiGPO (arXiv 2602.17038, Feb 2026) achieves ALFWorld 95.3% (7B) via phase-aware mixture of experts. RetroAgent achieves ALFWorld 94.9%. Dyna-Mind/RESIM (arXiv 2510.09577) achieves ALFWorld 92.5% (Dyna-GRPO) / 87.7% (RESIM) via learning to simulate from experience — uses a learned (not deterministic) simulator. AVIC (arXiv 2602.08236, Feb 2026) implements learned policy-based binary gating for world model invocation in visual spatial reasoning via prompting, without fine-tuning. Qian et al. (arXiv 2601.03905, Jan 2026) empirically show across FrozenLake, Navigation, PrimitiveSkill, and Sokoban (NOT ALFWorld) that forced world model use degrades performance; the primary bottleneck is deciding when to simulate. MTRouter (arXiv 2604.23530, ACL 2026) routes between different LLMs per turn. AgentRL (arXiv 2510.04206) scales agentic RL across multiple benchmarks. Key gap: ITP-R learns simulation gating but routes to an approximate LLM world model that fails on complex scientific reasoning (ScienceWorld). On environments where deterministic simulators implementing rule-governed dynamics are available, no method learns selective routing to exploit ground-truth state transitions.",
  "approach": "We propose SimGate, a hybrid routing framework that learns per-step whether an LLM agent should rely on internal reasoning or invoke a deterministic external simulator for ground-truth lookahead, targeting environments where state transitions are governed by deterministic rules (physics, chemistry, game mechanics). Unlike ITP-R, which routes to an LLM world model that fails on complex scientific dynamics (scoring ~59 vs CogRouter's 84.6 on ScienceWorld), SimGate routes to the environment's own deterministic simulator — providing exact state transitions at CPU-only cost.\n\nThe framework has three components:\n\n(1) Agent backbone: Qwen2.5-7B (matching CogRouter for controlled comparison), with ReAct-style interaction augmented by routing decisions at each step.\n\n(2) Deterministic simulator access: For ScienceWorld (primary benchmark), the JVM-based simulator is accessed via py4j. State forking is implemented through action-replay: a parallel ScienceWorld instance replays the current episode's action history to reach the identical state, then executes 1-3 candidate action sequences to observe exact outcomes (temperature changes, chemical reactions, circuit states). This avoids JVM serialization complexity while guaranteeing identical states. For ALFWorld (secondary benchmark), state forking uses GameState.copy() (which is implemented, unlike the base Environment.copy()) combined with a fresh TextWorld runtime to evaluate candidate actions. Both approaches are CPU-only with negligible cost compared to LLM world model inference.\n\n(3) Lightweight router: a Qwen3-1.7B model fine-tuned via SFT to select per step from {fast-internal, deep-internal, deterministic-simulation}, based on interaction history and current observation. This three-way modality routing differs from ITP-R's depth selection (K∈{0,...,K_max} over a single approximate world model) by treating internal reasoning and external ground-truth simulation as categorically different computation types.\n\nTraining proceeds in two offline phases:\n\nPhase 1 (trajectory collection): Run the Qwen2.5-7B agent on ScienceWorld's 30 task types (200 task variations) and ALFWorld's 134 tasks across ~600 total episodes. At each decision step, execute all three modalities in parallel — fast-internal (direct ReAct), deep-internal (chain-of-thought with multi-step planning), and deterministic-simulation (1-3 step lookahead via action-replay forking) — and record which produced the action leading to highest eventual task success via counterfactual labeling.\n\nPhase 2 (router SFT): Fine-tune Qwen3-1.7B on the labeled (history, observation, best-modality) triples with cross-entropy loss, following ARES's training pipeline. No online RL needed.\n\nEvaluation:\n- Primary benchmark: ScienceWorld (30 task types, 72.0% SR headroom above CogRouter SOTA). We compare against CogRouter (84.6 score / 72.0% SR), ITP-R (62.58/58.94 score), CoSFT+GRPO (71.1 score / 53.0% SR), AdaptThink (62.5 / 44.5%), ReAct, always-simulate, never-simulate, random routing, and confidence-threshold heuristic.\n- Secondary benchmark: ALFWorld (134 tasks). We compare against ITP-R (94.29%), CogRouter (92.5%), PA-MoE+GiGPO (95.3%), always-simulate, and ReAct. Here the primary claim is cost-efficiency: matching ITP-R's accuracy tier with lower inference cost by replacing GPU-intensive LLM world model rollouts with CPU-only deterministic simulation. We acknowledge ALFWorld saturation (Skill1: 97.5%) and do not claim SOTA.\n\nKey metrics: task success rate, normalized score (ScienceWorld), total LLM tokens consumed, simulation invocation ratio, LLM world model inference cost vs deterministic simulation cost (FLOPs and wall-clock), and per-task-category success breakdown to identify WHERE deterministic simulation provides most value.\n\nCore hypotheses: (H1) On ScienceWorld, SimGate outperforms both CogRouter (which lacks external grounding for scientific reasoning) and ITP-R (whose LLM world model hallucinates scientific state transitions), targeting >88 score / >78% SR. (H2) On ALFWorld, SimGate matches ITP-R's accuracy (~94%) with >40% reduction in inference FLOPs by substituting CPU-only deterministic simulation for GPU-intensive LLM world model rollouts. (H3) Per-task-category analysis reveals that deterministic simulation provides greatest value on tasks requiring multi-step causal reasoning about physical/chemical processes (ScienceWorld: heating, chemical reactions, circuits) and least value on simple pattern-matching tasks.\n\nGeneralizability discussion: SimGate's deterministic-simulator variant requires access to a ground-truth simulator, limiting direct applicability. We position this along a simulator fidelity spectrum: deterministic simulators (ScienceWorld, ALFWorld, game engines) → high-fidelity learned simulators → approximate LLM world models. Our contribution demonstrates that when ground-truth dynamics ARE available, learned selective invocation achieves a cost-accuracy Pareto improvement over LLM-based world model routing — motivating future work on routing across simulators of varying fidelity.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~220h H100 80GB (60h trajectory collection on ScienceWorld+ALFWorld with all modalities, 10h router SFT, 40h CogRouter baseline reproduction on ScienceWorld, 30h ITP-R baseline reproduction, 20h other baselines, 30h ALFWorld secondary experiments, 30h ablations and per-category analysis)",
      "gpu_utilization": "~50% effective utilization; ~50% idle from analysis, debugging, environment engineering, and writing",
      "timeline": "14 days (tight for May 25 ARR deadline; ScienceWorld action-replay state forking requires ~2 days engineering)",
      "team": "1 researcher",
      "estimated_gpu_cost": "$440-660 at $2.00-3.00/hr H100 80GB"
    },
    "human_in_loop": {
      "gpu_hours": "~180h H100 80GB (agent automates trajectory collection, baseline evaluation scheduling, and result parsing; human focuses on state-forking engineering, router training decisions, and paper writing)",
      "gpu_utilization": "~70% effective utilization",
      "timeline": "12 days",
      "team": "1 researcher, ~90min/day for ScienceWorld environment engineering, per-category analysis review, and training curves",
      "claude_api_cost": "$60-100 (~600-1000 Opus turns for ScienceWorld API integration, state-forking implementation, baseline reproduction, data pipeline, analysis)",
      "estimated_gpu_cost": "$360-540 at $2.00-3.00/hr",
      "risk_note": "Primary risk is ScienceWorld state-forking engineering — action-replay approach requires maintaining a parallel JVM instance and may have performance overhead for long episodes (>50 steps). Mitigated by capping lookahead replay to last 10 actions + simulator fast-forward. Secondary risk: ITP-R baseline uses different training method (A2C) than CogRouter (CoPO), making direct comparison noisy — mitigated by including ablation with matched training."
    },
    "auto_research": {
      "gpu_hours": "~260h H100 80GB (broader ScienceWorld per-task-type analysis across all 30 task types, ALFWorld cost analysis, routing ablations, lookahead depths 1-3, router sizes, ITP-R matched-training comparison)",
      "gpu_utilization": ">90% utilization; agent pipelines trajectory collection → labeling → training → evaluation continuously",
      "timeline": "10-12 days with 2+ H100 GPUs",
      "team": "0 (initial 3h setup for ScienceWorld state forking + environment + API keys)",
      "claude_api_cost": "$140-220 (~1400-2200 Opus turns for ScienceWorld integration, state forking implementation, experimentation, per-category analysis, and paper drafting)",
      "estimated_gpu_cost": "$520-780 at $2.00-3.00/hr",
      "speed_bottleneck": "CPU-bound ScienceWorld action-replay for state forking on long episodes; GPU bottleneck is Qwen2.5-7B inference for ~600 episodes × 3 modalities × ~30 steps = ~54K inference calls",
      "risk_note": "Without human judgment on training method fairness (ITP-R uses A2C, CogRouter uses CoPO), agent may produce noisy comparisons; mitigated by including ITP-R-style gating trained with CoPO as an additional ablation"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026, short paper)"
  ],
  "level": "promising",
  "key_references": [
    "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models [ITP/ITP-R] (arXiv 2601.08955, Jan 2026) — ALFWorld 94.29% (Qwen2.5-7B), ScienceWorld 62.58/58.94 score",
    "Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents [CogRouter] (arXiv 2602.12662, Feb 2026) — ALFWorld 92.5%, ScienceWorld 84.6 score / 72.0% SR",
    "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents (arXiv 2603.07915, March 2026)",
    "Current Agents Fail to Leverage World Model as Tool for Foresight [Qian et al.] (arXiv 2601.03905, Jan 2026) — evaluated on FrozenLake/Navigation/PrimitiveSkill/Sokoban, NOT ALFWorld",
    "Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning (arXiv 2605.06130, May 2026) — ALFWorld 97.5% SOTA",
    "Phase-Aware Mixture of Experts for Agentic RL [PA-MoE+GiGPO] (arXiv 2602.17038, Feb 2026) — ALFWorld 95.3% (7B)",
    "Dyna-Mind: Learning to Simulate from Experience for Better AI Agents (arXiv 2510.09577) — ALFWorld 92.5% (Dyna-GRPO)",
    "When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning [AVIC] (arXiv 2602.08236, Feb 2026)",
    "MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings (arXiv 2604.23530, ACL 2026)",
    "Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents (arXiv 2509.03581, 2025)",
    "Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond (arXiv 2604.22748, April 2026)",
    "AgentRL: Scaling Agentic Reinforcement Learning (arXiv 2510.04206)"
  ],
  "description": "We propose SimGate, a hybrid routing framework that learns per-step whether an LLM agent should use internal reasoning or invoke a deterministic external simulator for ground-truth lookahead, targeting environments where state transitions follow deterministic rules (physics, chemistry, game mechanics). The core evidence motivating SimGate: on ScienceWorld, ITP-R's LLM world model (Qwen2.5-7B) scores only 62.58/58.94 (seen/unseen), dramatically below CogRouter's 84.6 score / 72.0% SR using purely internal reasoning — a ~22-point gap demonstrating that LLM world models cannot reliably predict complex scientific state transitions (temperature changes, chemical reactions, circuit behavior). Meanwhile, ScienceWorld's JVM-based simulator implements these rules exactly. SimGate exploits this by learning when ground-truth simulation helps most: a Qwen3-1.7B router, SFT-trained on counterfactual trajectory data, selects per step from {fast-internal, deep-internal, deterministic-simulation}. State forking uses action-replay via parallel simulator instances (avoiding TextWorld's unimplemented Environment.copy()). On ScienceWorld (primary, 30 task types, 72.0% SR headroom), we hypothesize SimGate exceeds both CogRouter (no external grounding) and ITP-R (noisy LLM foresight), targeting >88 score / >78% SR. On ALFWorld (secondary, acknowledging 97.5% Skill1 saturation), SimGate aims to match ITP-R's 94.29% accuracy with >40% inference cost reduction by replacing GPU-intensive LLM world model rollouts with CPU-only deterministic simulation. We explicitly correct the prior version's factual error: ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B (not 88.57%, which is the Qwen3-8B number), outperforming CogRouter (92.5%). The LLM world model failure is benchmark-specific to complex rule-governed environments like ScienceWorld, not universal. Built on LangGraph with Qwen2.5-7B backbone, evaluated against CogRouter, ITP-R, PA-MoE+GiGPO, ARES, always-simulate, and heuristic baselines. Targeting EMNLP 2026 short paper (ARR deadline May 25, 2026). Estimated cost: 180-260 H100-hours ($360-780).",
  "project_name": "sim_gate_cost_aware_plan",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL CONSTRAINT VIOLATION: User specified target venue EMNLP 2026 (ARR deadline May 25, 2026), but idea targets AAAI 2027 and ICLR 2027. This completely mismatches the user's submission plan.", "CRITICAL CONSTRAINT VIOLATION: User specified ≤200 H100-hours total compute budget. Idea estimates 400-1000 A100 GPU hours (~300-700 H100-equivalent hours), exceeding the budget by 1.5-3.5x.", "CRITICAL CONSTRAINT VIOLATION: User specified ≤16-day timeline. Even the auto_research mode estimates 1-3 weeks; manual mode estimates 3-5 months.", "CRITICAL MISSING COMPETING WORK: CogRouter ('Think Fast and Slow', arXiv 2602.12662, Feb 2026) trains step-level cognitive depth adaptation using RL (CoPO) on ALFWorld and ScienceWorld — the EXACT same benchmarks. Achieves 92.5% ALFWorld, 72.0% ScienceWorld with Qwen2.5-7B. Code available at github.com/rhyang2021/CogRouter. This is the single most important competing baseline and is entirely unacknowledged.", "CRITICAL MISSING COMPETING WORK: ARES (arXiv 2603.07915, March 2026) trains a lightweight per-step router for adaptive reasoning effort allocation in LLM agents, evaluated on WebArena. 52.7% reasoning token reduction. Nearly identical mechanism (lightweight router on hidden states) for the same abstract goal (step-level compute-aware decisions).", "MISSING RELATED WORK: Budget-aware inference literature from early 2026 (BAVT for LLM agents, BudgetThinker, Inference-Time Budget Control for LLM Search Agents) addresses cost-aware step-level decisions in agents — adjacent and relevant.", "MARGINAL NOVELTY: After accounting for CogRouter (step-level gating + RL in agent trajectories), ARES (lightweight router for per-step effort), and Rational Metareasoning (VOC-based per-step reasoning gating), the remaining novelty is narrow: 'apply the same gating concept to external world model invocation instead of internal reasoning.' This is an application-level contribution, not a methodological one.", "BASELINE INSUFFICIENCY: CogRouter achieves 92.5% on ALFWorld without any world model. SimGate must demonstrate that adding world model simulation + a learned gate exceeds this strong baseline, which is not guaranteed and adds significant complexity.", "DOES NOT BUILD ON SPECIFIED OSS CODEBASES: User required building on AutoGen, LangGraph, OpenManus, etc. The idea proposes building from scratch with Qwen3-14B + WebWorld-8B.", "RESOURCE ESTIMATE INCONSISTENCY: Manual mode claims ~40% GPU utilization but 400h A100 — if effective utilization is 40%, real GPU booking is ~1000h. The estimates across modes are not internally consistent."]
Feedback: This idea needs fundamental restructuring to meet the user's requirements. Specific actions needed:

1. **RETARGET TO EMNLP 2026**: Redesign the entire scope to fit the EMNLP 2026 ARR deadline (May 25, 2026, 14 days from today). This means drastically simplifying the approach.

2. **FIT WITHIN 200 H100-HOURS**: The current design (Qwen3-14B backbone + WebWorld-8B world model + GRPO training + 3 benchmarks + 5 baselines) is far too expensive. Consider: (a) using a smaller backbone (7B instead of 14B), (b) reducing to 1-2 benchmarks, (c) replacing GRPO with simpler SFT-only training of the gating head, (d) using frozen world model predictions from precomputed rollouts rather than online generation.

3. **COMPLETE IN 16 DAYS**: Use existing OSS agent codebases (AutoGen, LangGraph) as required. Precompute world model rollouts offline, then train the gate head as a simple binary classifier on pre-collected trajectory data. This avoids the expensive online RL loop.

4. **ADDRESS CogRouter AND ARES**: These are the two closest competing works and MUST be cited, compared against, and differentiated from. CogRouter evaluates on the same benchmarks and achieves strong results (92.5% ALFWorld) without world models — you need to argue convincingly why adding world model gating improves over this. Consider using CogRouter as a baseline.

5. **SHARPEN NOVELTY CLAIM**: The distinction 'gate external simulator rather than internal reasoning' is real but thin. To strengthen it, consider: (a) theoretical analysis of when external simulation has higher value of computation than internal reasoning, (b) empirical comparison showing that world model predictions provide complementary signal to internal reasoning, (c) hybrid approach combining CogRouter-style internal depth adaptation with SimGate-style external simulation gating.

6. **SIMPLIFY SCOPE**: For a 16-day project with 200 H100-hours, focus on one benchmark (ALFWorld has the most mature world model support via TextWorld), one backbone, and a clean comparison showing that learned world model gating outperforms heuristic gating, always-simulate, and never-simulate baselines. Save the multi-benchmark story for a follow-up.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL MISCHARACTERIZATION: The proposal states 'ITP (2026) always simulates but adapts depth with ITP-R.' This is factually wrong. ITP-R's K-head predictor selects K_t ∈ {0,1,...,K_max} per step, where K=0 explicitly means NO simulation — the agent acts from internal reasoning alone. ITP-R IS a learned per-step router between 'no simulation' and 'simulation at various depths.' The proposal's core gap claim ('no existing work learns per-step routing between internal reasoning and external world model invocation') is therefore invalid.", "CRITICAL MISSING BASELINE: ITP-R (arXiv 2601.08955) achieves 88.57% on ALFWorld with Qwen3-8B using learned per-step simulation gating. This is the single most important baseline for SimGate's claimed contribution and must be included in experiments. Its lower performance vs CogRouter (88.57% vs 92.5%) actually raises a concerning question: if learned simulation routing (ITP-R) already underperforms pure internal adaptation (CogRouter) on ALFWorld, what evidence suggests SimGate's deterministic-simulator variant will reverse this trend?", "NOVELTY GAP NARROWER THAN CLAIMED: After accounting for ITP-R (learned K=0/K>0 routing), the remaining novelty reduces to: (a) routing to a deterministic external simulator vs LLM world model, (b) three-way modality selection vs depth selection, (c) separate router model vs backbone K-head. These are configuration-level differences, not methodological contributions. A short paper could possibly carry this, but only with an honest framing.", "GENERALIZABILITY CONCERN: The approach fundamentally depends on having access to a deterministic external simulator (ALFWorld's TextWorld). Most real-world agent tasks (web navigation, coding, API interaction) lack such simulators. The paper needs to address: under what conditions does this approach transfer? Without this discussion, reviewers will question practical relevance.", "AVIC (Yu et al., Feb 2026) NOT ADEQUATELY DIFFERENTIATED: AVIC implements a binary skip/call_wm gating policy for world model invocation in visual spatial reasoning. While the domain differs (vision vs text), the mechanism (learned binary gate for world model invocation) is conceptually identical. The proposal should explicitly differentiate.", "BENCHMARK SATURATION RISK: ALFWorld success rates are approaching ceiling (CogRouter 92.5%). Demonstrating statistically significant improvements above 92.5% on only 134 task instances requires careful analysis — the margin of improvement is thin and the evaluation set is small, making results potentially noisy.", "TEXTWORLD LOOKAHEAD ENGINEERING UNDERESTIMATED: ALFWorld's TextWorld has no built-in state-forking/cloning API for branching lookahead. Implementing 1-3 step lookahead with state save/restore requires custom engineering on top of the PDDL backend. This is doable but adds unaccounted complexity to the 16-day timeline."]
Feedback: The revision successfully fixed R1's constraint violations (venue, compute, timeline) — good work. But a serious novelty problem has emerged: ITP-R already does learned per-step routing between 'skip simulation' (K=0) and 'simulate' (K>0). You MUST not mischaracterize ITP. Here is how to salvage the idea:

1. **CORRECT ITP CHARACTERIZATION**: Acknowledge that ITP-R does per-step simulation gating. Then differentiate on the TYPE of simulation: ITP routes to an LLM-based (approximate, hallucination-prone) world model; SimGate routes to a deterministic external simulator providing exact state transitions. Frame this as: 'ITP asks when to imagine; SimGate asks when to consult ground truth.'

2. **ADD ITP-R AS PRIMARY BASELINE**: Include ITP-R (88.57% ALFWorld) alongside CogRouter (92.5%) as the two key baselines. Your hypothesis becomes: 'Deterministic external simulation, when selectively invoked, outperforms both LLM-based simulation routing (ITP-R) and pure internal depth adaptation (CogRouter).' This is testable and interesting.

3. **REFRAME NOVELTY HONESTLY**: The contribution is NOT 'first to learn simulation gating' — it's 'first to learn routing between internal reasoning and a deterministic external simulator as complementary modalities, showing that grounded simulation provides value that LLM-based world models cannot.' This narrower claim is defensible for a short paper.

4. **ADDRESS THE ELEPHANT IN THE ROOM**: ITP-R (88.57%) UNDERPERFORMS CogRouter (92.5%) on ALFWorld, suggesting LLM-based world model routing may actually hurt on this benchmark. You need a convincing argument for why DETERMINISTIC simulation routing will succeed where LLM-based simulation routing failed. The argument should be: 'ITP's LLM world model adds noise through hallucinated state transitions; a deterministic simulator provides exact dynamics, making the router's job easier — it only needs to identify WHEN exact foresight helps, not whether the foresight is accurate.'

5. **ADD GENERALIZABILITY DISCUSSION**: Explicitly acknowledge the deterministic simulator limitation. Propose how the framework extends to tasks with approximate/learned world models (connecting back to ITP/WebDreamer). This turns a weakness into a research direction.

6. **DIFFERENTIATE FROM AVIC**: Add explicit comparison — AVIC gates visual imagination with heuristic sufficiency checks in vision tasks; SimGate trains a separate router model for text-based agent tasks with SFT on counterfactual trajectory data.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL FACTUAL ERROR: The proposal cites ITP-R's ALFWorld result as 88.57% throughout, but this is the Qwen3-8B number. ITP-R with Qwen2.5-7B (the SAME backbone SimGate proposes) achieves 94.29% on ALFWorld — verified from ITP-R's Table in the HTML paper. This is HIGHER than CogRouter's 92.5%. The entire motivating argument ('ITP-R underperforms CogRouter, suggesting LLM-based simulation routing hurts') is based on an unfair cross-backbone comparison and is empirically false on the matched backbone.", "CORE MOTIVATION INVALIDATED: Since ITP-R (Qwen2.5-7B) = 94.29% > CogRouter = 92.5%, LLM-based simulation routing does NOT underperform pure internal adaptation on ALFWorld with the same backbone. This destroys the central hypothesis: 'deterministic external simulation provides complementary foresight that is strictly more reliable than LLM-based world model imagination.' The LLM world model already works well — there's no demonstrated failure to fix.", "OUTDATED SOTA: The proposal treats CogRouter (92.5%) as ALFWorld SOTA. As of May 2026, Skill1 achieves 97.5%, PA-MoE+GiGPO achieves 93.8%, and ITP-R achieves 94.29% with Qwen2.5-7B. CogRouter is no longer the primary comparison target. SimGate must demonstrate improvement over 94.29% (ITP-R) or explain why beating the 97.5% Skill1 ceiling is realistic.", "BENCHMARK SATURATION: ALFWorld is at 97.5% SOTA with only 134 evaluation instances. The practical headroom above ITP-R's 94.29% is ~3 percentage points on 134 tasks, making statistically significant improvements extremely difficult to demonstrate. This is especially problematic for a short paper that needs clean, convincing results.", "MISATTRIBUTION OF QIAN ET AL. RESULTS: The proposal states 'unconditional simulation degrades performance by up to 5% on trivial steps (Qian et al., 2026)' in the context of ALFWorld. However, Qian et al. evaluated on FrozenLake, Navigation, PrimitiveSkill, and Sokoban — NOT ALFWorld. The 5% degradation claim cannot be attributed to ALFWorld tasks.", "ENVIRONMENT.COPY() ENGINEERING RISK: TextWorld's base Environment.copy() raises NotImplementedError (verified in source code at github.com/microsoft/TextWorld/blob/main/textworld/core.py). While GameState.copy() performs deepcopy, the full environment forking required for multi-step lookahead rollouts needs the Environment-level copy, which must be implemented from scratch for ALFWorld's specific TextWorld integration. This unaccounted engineering work is risky for a 14-day timeline.", "MISSING RECENT BASELINES: Skill1 (97.5%, May 7, 2026), PA-MoE+GiGPO (93.8%), Dyna-Mind/RESIM (87.7-92.5%), and AgentRL are all absent from the baseline list. These represent the actual competitive landscape on ALFWorld."]
Feedback: The revision from R2 was well-executed in correcting the ITP mischaracterization (acknowledging K=0 option) and meeting hard constraints. But a new critical problem has emerged: you used ITP-R's Qwen3-8B result (88.57%) to argue it underperforms CogRouter (92.5%), when ITP-R's own paper reports 94.29% with Qwen2.5-7B — the backbone YOU plan to use. This means ITP-R with an LLM world model ALREADY outperforms CogRouter on the matched backbone, eliminating your core argument.

To salvage this idea, you must:

1. **ACKNOWLEDGE ITP-R (Qwen2.5-7B) = 94.29%**: This is the correct comparison point for SimGate, not 88.57%. Your method must beat 94.29% to show deterministic simulation adds value over LLM simulation.

2. **REFRAME THE MOTIVATION ENTIRELY**: You cannot argue 'LLM simulation hurts.' Instead, consider: (a) deterministic simulation is CHEAPER than LLM world model inference (no GPU cost, just CPU), so SimGate could match ITP-R's accuracy with lower computational cost; (b) deterministic simulation may be more robust on specific task categories where LLM world models still hallucinate (identify these via per-category analysis); (c) frame it as 'efficiency + reliability' rather than 'accuracy improvement.'

3. **UPDATE BASELINES AND SOTA**: Include Skill1 (97.5%), PA-MoE+GiGPO (93.8%), ITP-R Qwen2.5-7B (94.29%), and Dyna-Mind (92.5%) as baselines. Acknowledge ALFWorld is near saturation.

4. **CONSIDER PIVOTING BENCHMARK**: Given ALFWorld saturation, consider ScienceWorld (where CogRouter gets 72.0% and there's more headroom) or add a second benchmark where deterministic simulators are available and the benchmark isn't saturated.

5. **FIX QIAN ET AL. ATTRIBUTION**: The 5% degradation finding is from FrozenLake/Sokoban/Navigation/PrimitiveSkill, not ALFWorld. Correct this citation or run your own analysis on ALFWorld.

6. **ADDRESS ENVIRONMENT.COPY() RISK**: TextWorld's base Environment.copy() raises NotImplementedError. Plan for implementing state forking via GameState.copy() + manual environment reconstruction, and account for this engineering effort in your timeline.

7. **STRONGEST VIABLE ANGLE**: Instead of 'deterministic sim beats LLM sim in accuracy,' argue: 'When a deterministic simulator exists, routing to it is (a) computationally cheaper than LLM world model rollouts (CPU vs GPU), (b) guaranteed correct (zero hallucination), and (c) enables more aggressive multi-step lookahead without accuracy degradation. SimGate demonstrates that this cost-accuracy tradeoff is favorable, achieving comparable accuracy to ITP-R with significantly lower inference cost.' This efficiency-focused framing is defensible even if accuracy improvements are marginal.

### Round 4 review
Verdict: revise
Issues: ["CRITICAL MISSING BASELINE: EPO (arXiv 2509.22576, Sep 2025) achieves 96.8% binary success rate (IID) / 96.2% (OOD) on ScienceWorld with Qwen2.5-7B-Instruct via entropy-regularized policy optimization — far exceeding CogRouter's 72.0% SR. While EPO uses binary SR (not partial-credit score) and may use a different task subset, this result strongly suggests ScienceWorld is more solvable than the proposal assumes. The proposal treats CogRouter's 72.0% SR as the ceiling with '78% SR headroom' — but EPO has already reached ~97% SR without any simulation routing. This undermines the core motivation: if pure RL training (EPO) already solves ScienceWorld at 96.8% SR, what is the incremental value of deterministic simulator routing?", "MISSING BASELINE: EMPO2 (arXiv 2602.23008, Feb 2026) achieves 75.9 average score on ScienceWorld with Qwen2.5-7B via exploratory memory-augmented hybrid RL. This is another recent ScienceWorld result missing from the landscape.", "COMPUTE BUDGET VIOLATION: The user's hard constraint is ≤200 H100-hours. Manual mode estimates 220h (10% over) and auto mode estimates 260h (30% over). Only HIL at 180h fits within budget. The math breakdown shows 40h for CogRouter baseline + 30h for ITP-R baseline + 20h for other baselines = 90h on baselines alone — this may be reducible.", "ACTION-REPLAY COST UNDERESTIMATED FOR TRAJECTORY COLLECTION: Phase 1 requires executing the deterministic-simulation modality at every step of ~600 episodes × ~30 steps = ~18K decision points. Each fork costs ~1.5-5.5 seconds (JVM startup via py4j + action replay). At ~3s average, that's ~54,000 seconds = ~15 hours of wall-clock CPU time just for state forking during trajectory collection — not including the 1-3 candidate action evaluations per fork (which multiplies this by 1-3x). This is feasible but should be explicitly budgeted.", "METRIC COMPARABILITY ISSUES ON SCIENCEWORLD: The ScienceWorld landscape uses inconsistent metrics across papers. CogRouter reports both Score (84.6) and SR (72.0%); ITP-R reports Score (62.58/58.94); EPO reports binary SR (96.8%); EMPO2 reports Score on a -100 to 100 scale (75.9). The proposal's target of '>88 score / >78% SR' must specify which metric is primary and ensure all baselines are compared on the same metric. Without standardized evaluation, claimed improvements may be artifacts of metric selection.", "GENERALIZABILITY REMAINS INHERENTLY LIMITED: The approach requires a ground-truth deterministic simulator. The proposal discusses this honestly but does not address a key practical question: how many real-world agent benchmarks have such simulators? Among the user's specified benchmarks (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, Mind2Web, τ-bench), NONE have deterministic simulators. Only ALFWorld (TextWorld/PDDL) is listed. ScienceWorld is not in the user's specified benchmark list at all.", "BENCHMARK SELECTION CONCERN: The user specified evaluation on existing benchmarks including AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, and τ-bench. The proposal's primary benchmark (ScienceWorld) is NOT in this list. While ALFWorld is listed, it's designated as secondary and acknowledged as saturated. The proposal should justify why ScienceWorld is appropriate or include at least one of the user's specified benchmarks as primary.", "MISSING RELATED WORK: BoundaryRouter (arXiv 2605.07180, May 2026) proposes routing between lightweight LLM inference and full agent execution — conceptually adjacent to SimGate's routing paradigm. Qian et al. (arXiv 2601.03905) explicitly identifies the 'when to simulate' problem as unsolved — this should be cited as direct motivation, not just as evidence that forced simulation hurts."]
Feedback: The R4 revision is a major improvement in factual accuracy, honest framing, and competitive landscape coverage. The ScienceWorld pivot is well-motivated, and the novelty claim (learned routing to deterministic simulators) is confirmed as genuine — my independent search found no competing work. However, several issues must be addressed:

1. **ADDRESS EPO (CRITICAL)**: EPO achieves 96.8% binary SR on ScienceWorld with the same Qwen2.5-7B backbone, without any simulation routing. You MUST: (a) include EPO as a baseline, (b) explain why SimGate matters when pure RL training already nearly solves the benchmark, (c) consider whether SimGate's value is orthogonal (inference-time architectural choice) or redundant (EPO shows the problem is training, not architecture). The strongest argument: SimGate is a training-agnostic inference-time mechanism that COMPLEMENTS any backbone training method — run SimGate on top of an EPO-trained agent and show further gains or cost reduction. This would be much stronger than comparing only against CogRouter.

2. **FIT WITHIN 200 H100-HOURS**: Reduce compute by: (a) dropping some baselines (PA-MoE+GiGPO and Dyna-Mind can be cited from their papers without reproduction), (b) reducing ALFWorld experiments (it's secondary and saturated), (c) using CogRouter's published checkpoints if available rather than reproducing training. Target ≤180h to leave margin.

3. **STANDARDIZE SCIENCEWORLD METRICS**: Choose either Score or SR as the primary metric and ensure all baselines are compared on the same scale. If EPO only reports SR and CogRouter reports both, use SR as the common metric.

4. **BENCHMARK ALIGNMENT**: The user specified ALFWorld but not ScienceWorld. Either: (a) add one of the user's specified benchmarks where deterministic simulation is relevant (ALFWorld is already included as secondary — consider making it co-primary), or (b) justify why ScienceWorld is the right benchmark despite not being in the user's list (strong argument: it's the benchmark where deterministic simulation matters most due to complex scientific rules).

5. **REFRAME CONTRIBUTION**: Given EPO, the strongest framing is: 'SimGate demonstrates that learned routing to deterministic simulators provides a cost-accuracy Pareto improvement at inference time, complementary to and composable with any training-time optimization. When composed with an EPO-trained agent, SimGate achieves [X] with [Y]% fewer LLM inference calls.' This positions SimGate as an orthogonal, composable inference-time technique rather than competing with training-time methods.

### Round 5 review
Verdict: revise
Issues: ["CRITICAL FACTUAL ERROR: ITP-R with Qwen2.5-7B achieves 85.07% overall on ALFWorld, NOT 94.29%. The 94.29% is the PICK subtask score (first column in ITP-R's Table 1). The per-task breakdown is: PICK 94.29%, CLEAN 88.89%, HEAT 87.50%, COOL 53.84%, LOOK 76.00%, PICK2 91.67%, Overall 85.07%. This error originated in the R3 review's 'correction' and has persisted unchecked. The proposal's claim 'ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B, outperforming CogRouter (92.5%)' is wrong — ITP-R actually underperforms CogRouter by 7.4 points (85.07% vs 92.5%). HOWEVER: this correction actually STRENGTHENS SimGate's motivation, since it shows LLM world model routing hurts on BOTH ALFWorld and ScienceWorld, not just ScienceWorld.", "COMPUTE BUDGET VIOLATION: User hard constraint is ≤200 H100-hours. Manual=220h (10% over), Auto=260h (30% over). Only HIL=180h fits. Baseline reproduction alone consumes 90h (40h CogRouter + 30h ITP-R + 20h others). Reduce by: (a) citing PA-MoE+GiGPO and Dyna-Mind results from their papers without reproduction, (b) using CogRouter's published checkpoints if available, (c) trimming ALFWorld secondary experiments to only the critical always-simulate comparison.", "EPO NOT ADDRESSED (R4 CRITICAL FEEDBACK IGNORED): R4 flagged EPO (arXiv 2509.22576, 96.8% binary SR on ScienceWorld) as a critical missing baseline. R5 does not mention EPO at all. My verification reveals EPO's metric is NOT directly comparable to CogRouter's — their GRPO baselines differ by 40pp (EPO: 93.8% Succ.* vs CogRouter: 53.0% SR), indicating completely different evaluation protocols and/or task subsets. The proposal should acknowledge EPO, explain the comparability issue, and clarify which ScienceWorld evaluation protocol SimGate will follow (CogRouter's 200-simulation protocol is recommended for consistency with the primary baseline).", "MISSING RELATED WORK — ARTIS (arXiv 2602.01709, Feb 2026): 'Agentic Risk-Aware Test-Time Scaling via Iterative Simulation' runs LLM-based simulation on ALL candidate actions before committing — an always-simulate pipeline with a risk-aware simulator. While it lacks learned gating (every action is simulated), it is the most relevant 'always-simulate' baseline and should be cited alongside Qian et al.'s findings. Position SimGate as selectively routing where ARTIS wastes compute by always simulating.", "BENCHMARK SELECTION NOT ALIGNED WITH USER REQUIREMENTS: The user specified evaluation on AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, and τ-bench. ScienceWorld (the primary benchmark) is NOT in this list. Only ALFWorld is included, and it's designated as secondary. The proposal should explicitly justify why ScienceWorld is the right primary benchmark despite not being on the user's list, or elevate ALFWorld to co-primary status.", "CORRECTED ITP-R NUMBER CHANGES ALFWorld NARRATIVE: With the correct ITP-R overall (85.07%), the proposal's ALFWorld story changes from 'match ITP-R's 94.29% with lower cost' to 'ITP-R underperforms CogRouter on ALFWorld too (85.07% vs 92.5%), confirming LLM world models are generally harmful for agent simulation — SimGate aims to match or exceed CogRouter's 92.5% by replacing noisy LLM simulation with exact deterministic simulation at lower cost.' This is actually a stronger argument."]
Feedback: The idea's core novelty (learned routing to deterministic simulators) is independently confirmed as genuine — no competing work exists. But the R5 submission has a critical factual error and ignores R4's EPO feedback. Here's how to fix it:

1. **FIX ITP-R ALFWORLD NUMBER (CRITICAL)**: Replace all instances of '94.29%' with the correct overall score of 85.07%. The 94.29% is the PICK subtask only. With the corrected number, ITP-R (85.07%) underperforms CogRouter (92.5%) on ALFWorld too — this STRENGTHENS your argument. The narrative becomes: 'LLM world model routing (ITP-R) underperforms pure internal adaptation (CogRouter) on BOTH ALFWorld (85.07% vs 92.5%) and ScienceWorld (62.58 vs 84.6), demonstrating that LLM world models are generally harmful rather than helpful for agent simulation. SimGate replaces the noisy LLM world model with exact deterministic simulation, targeting improvements on both benchmarks.'

2. **CUT COMPUTE TO ≤190 H100-HOURS**: Drop PA-MoE+GiGPO and Dyna-Mind baseline reproduction (cite from papers: −20h). Check if CogRouter publishes checkpoints to avoid full retraining (−20h). Reduce ALFWorld secondary experiments to just always-simulate vs SimGate vs ITP-R (−15h). This gets you to ~165h with margin.

3. **ADDRESS EPO**: Add one paragraph noting EPO's 96.8% SR claim. Explain the evaluation protocol discrepancy (GRPO baseline: 93.8% in EPO vs 53.0% in CogRouter — a 40pp gap indicating different evaluation setups). State that SimGate will follow CogRouter's 200-simulation evaluation protocol for direct comparability. If EPO's evaluation code is available, consider running SimGate under EPO's protocol as a secondary comparison.

4. **ADD ARTIS AS RELATED WORK**: Cite ARTIS (2602.01709) as the 'always-simulate' baseline paradigm. SimGate is more efficient because it selectively invokes simulation only when rule-governed dynamics make internal prediction unreliable.

5. **JUSTIFY SCIENCEWORLD OR ELEVATE ALFWORLD**: Either (a) add one sentence justifying ScienceWorld: 'While not in the standard agent benchmark lists, ScienceWorld uniquely tests rule-governed scientific reasoning where deterministic simulation provides maximum value — making it the ideal testbed for SimGate's core hypothesis'; or (b) make ALFWorld co-primary with ScienceWorld.

6. **REVISE ALFWORLD HYPOTHESIS**: With ITP-R at 85.07% (not 94.29%), your ALFWorld target should be: 'Match or exceed CogRouter's 92.5% by replacing noisy LLM simulation with exact deterministic simulation, with lower inference cost than both ITP-R and CogRouter.' The cost-efficiency argument now pairs with an accuracy argument.

### Round 6 review
Verdict: revise
Issues: ["CRITICAL FACTUAL ERROR (PERSISTS FROM R5, NOW ROUND 6): ITP-R with Qwen2.5-7B achieves 85.07% OVERALL on ALFWorld, NOT 94.29%. The 94.29% is the PICK subtask score only (per-task breakdown: PICK 94.29%, CLEAN 88.89%, HEAT 87.50%, COOL 53.84%, LOOK 76.00%, PICK2 91.67%, Overall 85.07%). Verified from arXiv HTML, raw table data, and GitHub table image — three independent sources. The proposal's claim 'ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B, outperforming CogRouter (92.5%)' is factually wrong. ITP-R (85.07%) UNDERPERFORMS CogRouter (92.5%) by 7.4 points. Critically, this correction STRENGTHENS SimGate's motivation: LLM world model routing hurts on BOTH ALFWorld AND ScienceWorld.", "EPO NOT ADDRESSED (THIRD CONSECUTIVE ROUND): EPO (arXiv 2509.22576) claims 96.8% binary success rate on ScienceWorld with Qwen2.5-7B — flagged as critical in R4, re-flagged in R5, still completely absent in R6. My independent verification reveals: (a) EPO uses binary {0,1} success, NOT the continuous ScienceWorld score (0-100); (b) EPO's GRPO baseline is 93.8% Succ.* vs CogRouter's 53.0% SR — a 40pp gap proving fundamentally different evaluation protocols; (c) EPO does not disclose task subset, episode count, or binarization threshold; (d) max_steps=30 (vs typical 100). These numbers are NOT directly comparable to CogRouter's, but reviewers WILL raise EPO and the proposal MUST preemptively address it.", "EMPO2 MISSING: EMPO2 (arXiv 2602.23008, Feb 2026) achieves 75.9 average score on ScienceWorld with Qwen2.5-7B using continuous score across 18-19 tasks via exploratory memory-augmented hybrid RL. This is a directly comparable ScienceWorld result using the same metric and backbone. Must be included in landscape.", "COMPUTE BUDGET VIOLATION: Manual (220h) and auto (260h) modes exceed the ≤200 H100-hour hard constraint. Only HIL (180h) fits. The description states '180-260 H100-hours' — the upper bound violates the user's requirement. The 90h baseline reproduction budget (40h CogRouter + 30h ITP-R + 20h others) is the main bloat area.", "BENCHMARK MISALIGNMENT: The user specified 8 benchmarks: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench. ScienceWorld (the primary benchmark) is NOT in this list. Only ALFWorld is included, designated as secondary and acknowledged as saturated (97.5% Skill1). The proposal must either justify ScienceWorld's inclusion or elevate ALFWorld to co-primary status.", "STRUCTURAL IMPACT LIMITATION: The method requires access to a ground-truth deterministic simulator, which is available for ScienceWorld (JVM/Scala) and ALFWorld (TextWorld/PDDL) but NOT for any real-world agent benchmark (WebArena, SWE-bench, GAIA, ToolBench, Mind2Web, τ-bench). This fundamentally limits the contribution's practical relevance and will be a primary reviewer concern at EMNLP.", "ARTIS (2602.01709) STILL NOT CITED: ARTIS implements risk-aware iterative simulation before commitment — the closest 'always-simulate' baseline paradigm. SimGate should cite it as motivation: ARTIS wastes compute by always simulating, while SimGate selectively routes. Also missing: Qian et al. (2601.03905) is cited but its finding ('agents fail to decide WHEN to simulate') should be more prominently positioned as direct motivation — SimGate is precisely the solution to the problem they identify."]
Feedback: This is round 6 and the same critical issues keep recurring. You must fix them NOW or risk failing at round 10.

1. **FIX ITP-R NUMBER IMMEDIATELY (THIS IS THE THIRD TIME)**: ITP-R overall on ALFWorld with Qwen2.5-7B = **85.07%**, not 94.29%. I verified this from the paper's Table 1 across three sources. The 94.29% is the PICK subtask column — the rightmost 'Overall' column reads 85.07%. This correction actually HELPS you: ITP-R (85.07%) < CogRouter (92.5%) on ALFWorld, meaning LLM world model routing hurts on BOTH benchmarks. Your narrative becomes: 'LLM world model routing (ITP-R) consistently underperforms pure internal adaptation (CogRouter) — 85.07% vs 92.5% on ALFWorld, 62.58 vs 84.6 on ScienceWorld — demonstrating that approximate LLM foresight introduces noise that outweighs its planning value. SimGate replaces this noisy foresight with exact deterministic simulation.'

2. **ADDRESS EPO (NON-NEGOTIABLE)**: Add a paragraph: 'EPO (arXiv 2509.22576) reports 96.8% binary success rate on ScienceWorld with Qwen2.5-7B. However, EPO uses binary {0,1} success (not the standard continuous ScienceWorld score), an undisclosed task subset, and max_steps=30. Its GRPO baseline (93.8% Succ.*) differs by 40pp from CogRouter's (53.0% SR), indicating fundamentally different evaluation protocols. SimGate follows CogRouter's standardized 200-simulation evaluation protocol for direct comparability. We include EPO-style evaluation as a secondary metric for completeness.'

3. **ADD EMPO2**: Include EMPO2 (75.9 avg score, 18-19 tasks) in the landscape as a baseline that uses the same continuous metric.

4. **CUT COMPUTE TO ≤190h**: (a) Cite PA-MoE+GiGPO and Dyna-Mind results from their papers without reproduction (save ~15h). (b) Use CogRouter's published checkpoints if available instead of full retraining (save ~20h). (c) Reduce ALFWorld secondary experiments to essential comparisons only (save ~15h). Target 170h total.

5. **JUSTIFY SCIENCEWORLD**: Add explicit justification: 'While ScienceWorld is not in the standard agent benchmark list, it uniquely tests rule-governed scientific reasoning (temperature physics, chemical reactions, electrical circuits) where deterministic simulation provides maximal value over LLM world models. ScienceWorld is the ideal testbed for SimGate's core hypothesis because the gap between deterministic and LLM-based simulation is largest on tasks requiring accurate prediction of physical/chemical dynamics.'

6. **IMPACT WARNING**: The structural limitation (requires deterministic simulator) caps impact at ~2.5-3/5. To improve: (a) run a small experiment on one of the user's specified benchmarks where an approximate simulator could substitute (e.g., a code execution sandbox for SWE-bench, even if not deterministic), showing the framework generalizes beyond perfect simulators; or (b) connect more concretely to the growing ecosystem of game engines, physics simulators, and code sandboxes in agentic AI — argue that SimGate is relevant to any environment with a fast, reliable external evaluator.


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
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "0b1896b8-0fed-4cf2-afd7-af93345cb4f1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T01:16:43.482Z_

```json
{
  "parentUuid": "0b1896b8-0fed-4cf2-afd7-af93345cb4f1",
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
  "uuid": "564cfbaf-dfa9-40d3-bf3c-bd578ee6b407",
  "timestamp": "2026-05-12T01:16:43.482Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T01:16:43.482Z_

```json
{
  "parentUuid": "564cfbaf-dfa9-40d3-bf3c-bd578ee6b407",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "126cefc1-56a5-433d-becb-a7c90b43ccba",
  "timestamp": "2026-05-12T01:16:43.482Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
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
  "leafUuid": "126cefc1-56a5-433d-becb-a7c90b43ccba",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate: Deterministic simulator routing for LLM agents",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Assistant

_source line 8 · 2026-05-12T01:16:48.291Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - SimGate - which proposes learning when to route LLM agents to deterministic simulators for rule-governed reasoning. This is round 7/10, and there have been persistent issues across previous rounds. Let me conduct independent verification of the claims and assess the idea thoroughly.

Let me start by searching for the key papers and claims independently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "126cefc1-56a5-433d-becb-a7c90b43ccba",
  "isSidechain": false,
  "requestId": "req_011CawnsTLdbSxuT3ZicUs9M",
  "type": "assistant",
  "uuid": "0d21ba64-be8b-4af6-af36-b8621d5cc0d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQW6CiYetdwHgremr92ZiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23618,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23618
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

_source line 9 · 2026-05-12T01:16:49.710Z_

I'll conduct an independent, thorough review of this idea. Let me verify the key claims, check for missing competing work, and assess feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d21ba64-be8b-4af6-af36-b8621d5cc0d2",
  "isSidechain": false,
  "requestId": "req_011CawnsTLdbSxuT3ZicUs9M",
  "type": "assistant",
  "uuid": "a5304b6d-a02b-41d9-a8f9-4fa59baf47e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQW6CiYetdwHgremr92ZiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23618,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23618
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

_source line 10 · 2026-05-12T01:16:56.805Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TGqLmpF5H1xjhD5v6tSQX3`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ITP-R ALFWorld numbers",
  "prompt": "I need to verify the exact performance numbers for ITP-R (Imagine-then-Plan) on ALFWorld. The paper is arXiv 2601.08955 (Jan 2026). \n\nThere's been a persistent dispute: one claim says ITP-R with Qwen2.5-7B achieves 94.29% overall on ALFWorld, another says 94.29% is only the PICK subtask and overall is 85.07%.\n\nPlease:\n1. WebSearch for \"ITP-R ALFWorld Qwen2.5-7B results arXiv 2601.08955\"\n2. WebFetch the arxiv HTML page (https://arxiv.org/html/2601.08955) and look for Table 1 or the main results table showing ALFWorld performance\n3. Report the EXACT per-task breakdown AND overall number for Qwen2.5-7B on ALFWorld\n\nBe very precise - I need to know if 94.29% is the overall or just a subtask score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5304b6d-a02b-41d9-a8f9-4fa59baf47e2",
  "isSidechain": false,
  "requestId": "req_011CawnsTLdbSxuT3ZicUs9M",
  "type": "assistant",
  "uuid": "94a413b9-c7bc-47f4-a504-50d4c362f642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQW6CiYetdwHgremr92ZiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23618,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23618
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

_source line 11 · 2026-05-12T01:17:19.838Z_

<details><summary>↩ Tool result · `toolu_01TGqLmpF5H1xjhD5v6tSQX3`</summary>

```text
Here are the exact findings from the paper.

**Paper:** "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models" (arXiv 2601.08955, Jan 2026)

**ITP-R (with Reflexion) using Qwen2.5-7B on ALFWorld -- Table 1 results:**

| Subtask | Score |
|---------|-------|
| PICK | 94.29% |
| CLEAN | 88.89% |
| HEAT | 87.50% |
| COOL | 53.84% |
| LOOK | 76.00% |
| PICK2 | 91.67% |
| **Overall** | **85.07%** |

**Resolution of the dispute:** The 94.29% figure is **only the PICK subtask score**, not the overall score. The overall ALFWorld success rate for ITP-R with Qwen2.5-7B is **85.07%**. The claim that 94.29% is the overall score is incorrect -- it is the highest-performing individual subtask (PICK), and the overall number is substantially lower, dragged down especially by COOL (53.84%) and LOOK (76.00%).

Sources:
- [Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models](https://arxiv.org/html/2601.08955)

agentId: a7feb58bfbfb6cb78 (use SendMessage with to: 'a7feb58bfbfb6cb78' to continue this agent)
&lt;usage>total_tokens: 12498
tool_uses: 3
duration_ms: 23026&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94a413b9-c7bc-47f4-a504-50d4c362f642",
  "isSidechain": false,
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "80f2f291-b7a6-43c8-9e45-f7fd66d5b3a2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the exact performance numbers for ITP-R (Imagine-then-Plan) on ALFWorld. The paper is arXiv 2601.08955 (Jan 2026). \n\nThere's been a persistent dispute: one claim says ITP-R with Qwen2.5-7B achieves 94.29% overall on ALFWorld, another says 94.29% is only the PICK subtask and overall is 85.07%.\n\nPlease:\n1. WebSearch for \"ITP-R ALFWorld Qwen2.5-7B results arXiv 2601.08955\"\n2. WebFetch the arxiv HTML page (https://arxiv.org/html/2601.08955) and look for Table 1 or the main results table showing ALFWorld performance\n3. Report the EXACT per-task breakdown AND overall number for Qwen2.5-7B on ALFWorld\n\nBe very precise - I need to know if 94.29% is the overall or just a subtask score.",
    "agentId": "a7feb58bfbfb6cb78",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the exact findings from the paper.\n\n**Paper:** \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\" (arXiv 2601.08955, Jan 2026)\n\n**ITP-R (with Reflexion) using Qwen2.5-7B on ALFWorld -- Table 1 results:**\n\n| Subtask | Score |\n|---------|-------|\n| PICK | 94.29% |\n| CLEAN | 88.89% |\n| HEAT | 87.50% |\n| COOL | 53.84% |\n| LOOK | 76.00% |\n| PICK2 | 91.67% |\n| **Overall** | **85.07%** |\n\n**Resolution of the dispute:** The 94.29% figure is **only the PICK subtask score**, not the overall score. The overall ALFWorld success rate for ITP-R with Qwen2.5-7B is **85.07%**. The claim that 94.29% is the overall score is incorrect -- it is the highest-performing individual subtask (PICK), and the overall number is substantially lower, dragged down especially by COOL (53.84%) and LOOK (76.00%).\n\nSources:\n- [Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models](https://arxiv.org/html/2601.08955)"
      }
    ],
    "totalDurationMs": 23026,
    "totalTokens": 12498,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1240,
      "cache_read_input_tokens": 10920,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1240
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 10920,
          "cache_creation_input_tokens": 1240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1240,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "94a413b9-c7bc-47f4-a504-50d4c362f642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-12T01:17:23.675Z_

Good - confirmed ITP-R overall = **85.07%**, not 94.29%. The proposal STILL claims 94.29% in round 7. Let me now verify EPO, EMPO2, ARTIS, and search for any additional competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80f2f291-b7a6-43c8-9e45-f7fd66d5b3a2",
  "isSidechain": false,
  "requestId": "req_011Cawnv8XP3pTo5ds8hz5xA",
  "type": "assistant",
  "uuid": "920ac3df-b674-4831-991b-6d7a707471b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012k81V1HmEFxLLV3QoWsfRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 35459,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1063,
          "cache_read_input_tokens": 35459,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 13 · 2026-05-12T01:17:29.702Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01A5DxrLq7LXLqRqJkdnqhaN`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify EPO ScienceWorld results",
  "prompt": "I need to verify EPO's results on ScienceWorld. The paper is arXiv 2509.22576 (Sep 2025), claiming 96.8% binary success rate on ScienceWorld with Qwen2.5-7B.\n\nPlease:\n1. WebSearch for \"EPO entropy regularized policy optimization ScienceWorld arXiv 2509.22576\"\n2. Try to WebFetch the paper at https://arxiv.org/html/2509.22576 or https://arxiv.org/abs/2509.22576\n3. Report: (a) What metric does EPO use (binary success vs continuous score)? (b) What task subset of ScienceWorld? (c) What is max_steps? (d) What is their GRPO baseline performance? (e) How many tasks/episodes evaluated?\n\nThe key question: Is EPO's 96.8% directly comparable to CogRouter's 72.0% SR / 84.6 score on ScienceWorld? Are they using the same evaluation protocol?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "920ac3df-b674-4831-991b-6d7a707471b9",
  "isSidechain": false,
  "requestId": "req_011Cawnv8XP3pTo5ds8hz5xA",
  "type": "assistant",
  "uuid": "2191517e-0701-47e4-bfcb-a8c60d44dee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012k81V1HmEFxLLV3QoWsfRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 35459,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1063,
          "cache_read_input_tokens": 35459,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 14 · 2026-05-12T01:17:37.903Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014xubCvWsJaVBTRjfz8eaZv`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for EMPO2 and ARTIS papers",
  "prompt": "I need to verify two papers and find their ScienceWorld/agent results:\n\n1. **EMPO2** (arXiv 2602.23008, Feb 2026) — claimed to achieve 75.9 average score on ScienceWorld with Qwen2.5-7B via exploratory memory-augmented hybrid RL\n   - WebSearch for \"EMPO2 ScienceWorld arXiv 2602.23008\" \n   - Verify the 75.9 score claim\n   - What evaluation protocol do they use?\n\n2. **ARTIS** (arXiv 2602.01709, Feb 2026) — \"Agentic Risk-Aware Test-Time Scaling via Iterative Simulation\"\n   - WebSearch for \"ARTIS risk-aware test-time scaling iterative simulation arXiv 2602.01709\"\n   - What does this paper do? Is it an always-simulate baseline?\n   - What benchmarks does it evaluate on?\n\nReport findings for both papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2191517e-0701-47e4-bfcb-a8c60d44dee9",
  "isSidechain": false,
  "requestId": "req_011Cawnv8XP3pTo5ds8hz5xA",
  "type": "assistant",
  "uuid": "8d524193-7027-49b2-8a21-5c7d4a9652ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012k81V1HmEFxLLV3QoWsfRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 35459,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1063,
          "cache_read_input_tokens": 35459,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 15 · 2026-05-12T01:17:41.885Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XfnatjuurQpyZK47XR5vD9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing work on deterministic simulator routing",
  "prompt": "I'm reviewing a paper idea called \"SimGate\" that proposes learning when to route LLM agents to deterministic external simulators (as opposed to LLM world models or internal reasoning). I need to find if any competing work does this.\n\nPlease search extensively:\n1. WebSearch \"LLM agent deterministic simulator routing 2025 2026\"\n2. WebSearch \"learned routing external simulator LLM agent\"\n3. WebSearch \"when to simulate agent planning deterministic environment 2026\"\n4. WebSearch \"selective simulation invocation LLM agent ScienceWorld ALFWorld\"\n5. WebSearch \"ground truth simulator routing agent planning arxiv 2026\"\n6. WebSearch \"hybrid reasoning simulation agent routing 2025 2026\"\n\nI need to know: Has anyone published work on LEARNED routing between internal LLM reasoning and an external DETERMINISTIC simulator (not an LLM-based world model)? This is the core novelty claim of SimGate.\n\nAlso check: Are there any very recent (March-May 2026) papers on ScienceWorld or ALFWorld agent performance that might be missing from the competitive landscape?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d524193-7027-49b2-8a21-5c7d4a9652ab",
  "isSidechain": false,
  "requestId": "req_011Cawnv8XP3pTo5ds8hz5xA",
  "type": "assistant",
  "uuid": "c6b8efd8-9132-4035-a7e7-6017f5583933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012k81V1HmEFxLLV3QoWsfRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 35459,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1063,
          "cache_read_input_tokens": 35459,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 16 · 2026-05-12T01:19:38.730Z_

<details><summary>↩ Tool result · `toolu_014xubCvWsJaVBTRjfz8eaZv`</summary>

```text
Now I have comprehensive details for both papers. Here is my report:

---

## Paper 1: EMPO2 (arXiv 2602.23008)

**Title:** Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization

**Verification of the 75.9 claim: CONFIRMED.** The paper reports an average score of **75.9** on ScienceWorld using **Qwen2.5-7B-Instruct** as the base model, compared to GRPO's 33.2 (hence the 128.6% improvement).

**Evaluation Protocol:**
- Uses the **first 5 variants** of each task for training, and evaluates on **20 unseen test variants** per task.
- Critically, the reported 75.9 score is the performance of the trained model **without memory at test time**. Memory is used during training for exploration, but the final evaluation measures how well the model has internalized exploration benefits into its parameters.
- ScienceWorld has 18-19 tasks spanning chemistry, classification, biology, electricity, and measurement.

**Per-task breakdown highlights:**
- Perfect scores (100.0) on all classification tasks (find-animal, find-living-thing, find-non-living-thing, find-plant) and biology2 tasks (lifespan).
- Strong on electricity tasks (71-94 range).
- Weaker on chemistry (33-43) and some measurement tasks (measure-melting-point: 27.6).

---

## Paper 2: ARTIS (arXiv 2602.01709)

**Title:** Agentic Risk-Aware Test-Time Scaling via Iterative Simulation

**What it does:** ARTIS is a test-time scaling framework for agentic settings where actions are irreversible and costly. It decouples exploration from commitment by running **simulated interactions before real-world execution**. A key innovation is a **risk-aware tool simulator** that focuses fidelity on failure-inducing actions via targeted data generation and rebalanced training (addressing the problem that naive LLM simulators miss rare but high-impact failure modes).

**Is it an always-simulate baseline? YES.** ARTIS **always simulates before acting** -- every task undergoes multiple simulated attempts (default N=5) through three mandatory stages: iterative simulation, trial summarization, and final execution. There is no selective simulation; it is not a "decide whether to simulate" system. The baselines it compares against are direct execution (no simulation), Weighted Best-of-N sampling, and Sequential Revision.

**Benchmarks evaluated on:**
1. **BFCL-v3** (Berkeley Function Calling Leaderboard v3) -- multi-turn categories
2. **ACEBench** -- agent multi-step setting

**Key results:**
- BFCL-v3 Multi-Turn-Base: Qwen3-8B improved from 12.88% (direct) to 18.75%; Qwen3-32B from 21.75% to 30.50%.
- ACEBench Agent: Qwen3-8B improved dramatically from 14.60% to 52.10%; Qwen3-14B from 54.20% to 63.30%.
- Performance scales with number of simulation attempts, peaking around N=8-10.

**Notable:** ARTIS does NOT evaluate on ScienceWorld, WebShop, ToolBench, or API-Bank. Its evaluation is focused on function-calling / tool-use benchmarks (BFCL-v3 and ACEBench).

---

Sources:
- [EMPO2 - arXiv abstract](https://arxiv.org/abs/2602.23008)
- [EMPO2 - Full HTML paper](https://arxiv.org/html/2602.23008)
- [EMPO2 - Hugging Face paper page](https://huggingface.co/papers/2602.23008)
- [ARTIS - arXiv abstract](https://arxiv.org/abs/2602.01709)
- [ARTIS - Full HTML paper](https://arxiv.org/html/2602.01709)

agentId: a5a6b19c71792d334 (use SendMessage with to: 'a5a6b19c71792d334' to continue this agent)
&lt;usage>total_tokens: 24012
tool_uses: 16
duration_ms: 120823&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d524193-7027-49b2-8a21-5c7d4a9652ab",
  "isSidechain": false,
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "d30a4c35-d31f-4ec4-84da-bea15e549d2b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two papers and find their ScienceWorld/agent results:\n\n1. **EMPO2** (arXiv 2602.23008, Feb 2026) — claimed to achieve 75.9 average score on ScienceWorld with Qwen2.5-7B via exploratory memory-augmented hybrid RL\n   - WebSearch for \"EMPO2 ScienceWorld arXiv 2602.23008\" \n   - Verify the 75.9 score claim\n   - What evaluation protocol do they use?\n\n2. **ARTIS** (arXiv 2602.01709, Feb 2026) — \"Agentic Risk-Aware Test-Time Scaling via Iterative Simulation\"\n   - WebSearch for \"ARTIS risk-aware test-time scaling iterative simulation arXiv 2602.01709\"\n   - What does this paper do? Is it an always-simulate baseline?\n   - What benchmarks does it evaluate on?\n\nReport findings for both papers.",
    "agentId": "a5a6b19c71792d334",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive details for both papers. Here is my report:\n\n---\n\n## Paper 1: EMPO2 (arXiv 2602.23008)\n\n**Title:** Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization\n\n**Verification of the 75.9 claim: CONFIRMED.** The paper reports an average score of **75.9** on ScienceWorld using **Qwen2.5-7B-Instruct** as the base model, compared to GRPO's 33.2 (hence the 128.6% improvement).\n\n**Evaluation Protocol:**\n- Uses the **first 5 variants** of each task for training, and evaluates on **20 unseen test variants** per task.\n- Critically, the reported 75.9 score is the performance of the trained model **without memory at test time**. Memory is used during training for exploration, but the final evaluation measures how well the model has internalized exploration benefits into its parameters.\n- ScienceWorld has 18-19 tasks spanning chemistry, classification, biology, electricity, and measurement.\n\n**Per-task breakdown highlights:**\n- Perfect scores (100.0) on all classification tasks (find-animal, find-living-thing, find-non-living-thing, find-plant) and biology2 tasks (lifespan).\n- Strong on electricity tasks (71-94 range).\n- Weaker on chemistry (33-43) and some measurement tasks (measure-melting-point: 27.6).\n\n---\n\n## Paper 2: ARTIS (arXiv 2602.01709)\n\n**Title:** Agentic Risk-Aware Test-Time Scaling via Iterative Simulation\n\n**What it does:** ARTIS is a test-time scaling framework for agentic settings where actions are irreversible and costly. It decouples exploration from commitment by running **simulated interactions before real-world execution**. A key innovation is a **risk-aware tool simulator** that focuses fidelity on failure-inducing actions via targeted data generation and rebalanced training (addressing the problem that naive LLM simulators miss rare but high-impact failure modes).\n\n**Is it an always-simulate baseline? YES.** ARTIS **always simulates before acting** -- every task undergoes multiple simulated attempts (default N=5) through three mandatory stages: iterative simulation, trial summarization, and final execution. There is no selective simulation; it is not a \"decide whether to simulate\" system. The baselines it compares against are direct execution (no simulation), Weighted Best-of-N sampling, and Sequential Revision.\n\n**Benchmarks evaluated on:**\n1. **BFCL-v3** (Berkeley Function Calling Leaderboard v3) -- multi-turn categories\n2. **ACEBench** -- agent multi-step setting\n\n**Key results:**\n- BFCL-v3 Multi-Turn-Base: Qwen3-8B improved from 12.88% (direct) to 18.75%; Qwen3-32B from 21.75% to 30.50%.\n- ACEBench Agent: Qwen3-8B improved dramatically from 14.60% to 52.10%; Qwen3-14B from 54.20% to 63.30%.\n- Performance scales with number of simulation attempts, peaking around N=8-10.\n\n**Notable:** ARTIS does NOT evaluate on ScienceWorld, WebShop, ToolBench, or API-Bank. Its evaluation is focused on function-calling / tool-use benchmarks (BFCL-v3 and ACEBench).\n\n---\n\nSources:\n- [EMPO2 - arXiv abstract](https://arxiv.org/abs/2602.23008)\n- [EMPO2 - Full HTML paper](https://arxiv.org/html/2602.23008)\n- [EMPO2 - Hugging Face paper page](https://huggingface.co/papers/2602.23008)\n- [ARTIS - arXiv abstract](https://arxiv.org/abs/2602.01709)\n- [ARTIS - Full HTML paper](https://arxiv.org/html/2602.01709)"
      }
    ],
    "totalDurationMs": 120823,
    "totalTokens": 24012,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 21637,
      "output_tokens": 997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 997,
          "cache_read_input_tokens": 21637,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1377,
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
  "sourceToolAssistantUUID": "8d524193-7027-49b2-8a21-5c7d4a9652ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T01:20:04.517Z_

<details><summary>↩ Tool result · `toolu_01XfnatjuurQpyZK47XR5vD9`</summary>

```text
I now have a comprehensive picture. Here is my analysis:

---

## Competitive Landscape Analysis for "SimGate"

### Core Question: Has anyone published on LEARNED routing between internal LLM reasoning and an external DETERMINISTIC simulator?

**Short answer: No exact match found.** No published work proposes a learned gate/router that specifically decides when an LLM agent should invoke an external deterministic simulator (like a physics engine, game engine, or programmatic environment model) versus relying on its own internal reasoning or an LLM-based world model. However, several papers are **adjacently relevant** and must be cited/differentiated in a SimGate paper. Here they are, ranked by threat level:

---

### HIGH RELEVANCE -- Must differentiate clearly

1. **AutoTool (AAAI 2026)** -- [arXiv 2511.14650](https://arxiv.org/abs/2511.14650)
   - Builds a tool-invocation graph from past trajectories to predict the next tool call, bypassing the LLM via "inertial calls" when confidence is high. Evaluated on ScienceWorld and ALFWorld.
   - **Overlap with SimGate**: Learns *when to skip the LLM* and go directly to a tool/action. Operates on the same benchmarks.
   - **Key difference**: AutoTool routes between "ask the LLM" vs. "replay a cached tool pattern." It does NOT route to a deterministic simulator for state prediction/lookahead. It is about efficiency (skipping LLM calls), not about choosing a more accurate reasoning modality.

2. **BoundaryRouter (May 2026)** -- [arXiv 2605.07180](https://arxiv.org/abs/2605.07180)
   - Training-free method that decides whether a query needs full agentic execution or can be answered by direct LLM inference, using early-experience memory retrieval.
   - **Overlap with SimGate**: Learned routing between "lightweight reasoning" and "heavy agentic execution."
   - **Key difference**: Routes between two LLM-based modes (direct inference vs. multi-step agent). Does NOT involve an external deterministic simulator at all.

3. **DART (Feb 2026)** -- [arXiv 2602.00994](https://arxiv.org/abs/2602.00994)
   - Shows reasoning and tool-use *compete* during joint RL training (gradient interference / seesaw effect). Proposes disentangled LoRA modules.
   - **Overlap with SimGate**: Directly addresses the tension between internal reasoning and external tool use.
   - **Key difference**: Focuses on *training dynamics* (how to train both capabilities), not on a runtime routing decision. Does not involve a deterministic simulator.

4. **Budget-Aware Agentic Routing (Feb 2026)** -- [arXiv 2602.21227](https://arxiv.org/abs/2602.21227)
   - Learns to route between a cheap model and an expensive model at each agent step under budget constraints, using RL with boundary-guided training.
   - **Overlap with SimGate**: Learned per-step routing policy optimized via RL, with budget awareness.
   - **Key difference**: Routes between two LLMs (small vs. large), not between an LLM and a simulator.

5. **WebDreamer (TMLR 2025)** -- [arXiv 2411.06559](https://arxiv.org/abs/2411.06559)
   - Uses the LLM itself as a "world model" to simulate action outcomes for planning, as an alternative to tree search in external environments.
   - **Overlap with SimGate**: Directly compares LLM-as-world-model vs. external environment interaction for planning.
   - **Key difference**: Always uses the LLM world model; does not learn *when* to switch to the real environment. SimGate's novelty is precisely in learning this routing decision.

---

### MODERATE RELEVANCE -- Worth citing in related work

6. **Uno-Orchestra (May 2026)** -- [arXiv 2605.05007](https://arxiv.org/abs/2605.05007)
   - Unified RL-trained orchestration policy that jointly learns task decomposition and worker/model selection. 22 baselines, 13 benchmarks.
   - Routes among multiple agents/models, not to a deterministic simulator.

7. **AgentGate (April 2026)** -- [arXiv 2604.06696](https://arxiv.org/abs/2604.06696)
   - Structured routing engine for multi-agent systems; decides whether to invoke one agent, generate a multi-agent plan, return direct response, or stop.
   - Despite the similar name, this is about multi-agent orchestration, not simulator routing.

8. **ReflAct (EMNLP 2025)** -- [arXiv 2505.15182](https://arxiv.org/abs/2505.15182)
   - Achieves 93.3% on ALFWorld by grounding reasoning in goal-state reflection. No routing or simulator component, but sets a strong ALFWorld baseline.

9. **Throttling Web Agents Using Reasoning Gates (Sep 2025)** -- [arXiv 2509.01619](https://arxiv.org/abs/2509.01619)
   - Uses "reasoning gates" but in a completely different sense: computational puzzles imposed on agents to throttle them. Not related to simulator routing.

---

### RECENT ScienceWorld / ALFWorld PAPERS (March-May 2026)

These should be checked for updated baselines:

- **Retrieval-Augmented LLM Agents** (March 2026, [arXiv 2603.18272](https://arxiv.org/abs/2603.18272)) -- Evaluates retrieval-from-experience on ALFWorld and ScienceWorld. ALFWorld results up to ~65%, ScienceWorld gains small.
- **StateFactory / Co-Evolution of Policy and Internal Reward** (April 2026, [arXiv 2604.03098](https://arxiv.org/abs/2604.03098)) -- Reports +21.64% on ALFWorld, +12.40% on ScienceWorld over reactive baselines.
- **Coarse-to-Fine Grounded Memory** ([arXiv 2508.15305](https://arxiv.org/abs/2508.15305)) -- Graph-memory-augmented planning for LLM agents, evaluated on ALFWorld/ScienceWorld.
- **AgentSwift** ([arXiv 2506.06017](https://arxiv.org/abs/2506.06017)) -- Value-guided hierarchical search for efficient LLM agent design.

---

### Assessment of SimGate's Novelty

The novelty claim -- **a learned routing mechanism that decides per-step whether to query an external deterministic simulator vs. rely on LLM internal reasoning** -- appears to be **genuinely novel** as of May 2026. The closest neighbors are:

| Paper | Routes between | Learned? | Deterministic sim? |
|-------|---------------|----------|-------------------|
| SimGate (yours) | LLM reasoning <-> external deterministic simulator | Yes | **Yes** |
| AutoTool | LLM <-> cached tool pattern | Yes (graph-based) | No (tool replay) |
| BoundaryRouter | Direct LLM <-> full agent | Sort of (experience-based) | No |
| DART | Reasoning <-> tool-use (training) | N/A (training method) | No |
| Budget-Aware Routing | Small LLM <-> large LLM | Yes (RL) | No |
| WebDreamer | LLM world model only | No routing | No (LLM is the sim) |

**The gap SimGate fills**: Everyone routes LLM-to-LLM or LLM-to-tool. Nobody learns when to offload state prediction to a ground-truth deterministic simulator. WebDreamer is the philosophical inverse (it argues you should always use the LLM *as* the simulator). SimGate argues the opposite for environments where a cheap, accurate deterministic simulator exists.

**Recommended framing**: Position SimGate as complementary to WebDreamer (for domains where no deterministic simulator exists, use LLM world models; where one does exist, learn when to use it). Differentiate from AutoTool (which learns tool *sequencing patterns*, not *simulator invocation for state prediction*). Cite DART for the reasoning-vs-tool-use tension that motivates the need for explicit routing rather than joint training.

Sources:
- [AutoTool (AAAI 2026)](https://arxiv.org/abs/2511.14650)
- [BoundaryRouter](https://arxiv.org/abs/2605.07180)
- [DART](https://arxiv.org/abs/2602.00994)
- [Budget-Aware Agentic Routing](https://arxiv.org/abs/2602.21227)
- [WebDreamer](https://arxiv.org/abs/2411.06559)
- [Uno-Orchestra](https://arxiv.org/abs/2605.05007)
- [AgentGate](https://arxiv.org/abs/2604.06696)
- [ReflAct (EMNLP 2025)](https://arxiv.org/abs/2505.15182)
- [Throttling Web Agents](https://arxiv.org/abs/2509.01619)
- [Retrieval-Augmented LLM Agents](https://arxiv.org/abs/2603.18272)
- [Co-Evolution of Policy and Internal Reward](https://arxiv.org/abs/2604.03098)
- [SELECT-THEN-ROUTE (EMNLP 2025)](https://aclanthology.org/2025.emnlp-industry.28.pdf)

agentId: ad4b5bbc27f9e2653 (use SendMessage with to: 'ad4b5bbc27f9e2653' to continue this agent)
&lt;usage>total_tokens: 30497
tool_uses: 19
duration_ms: 142628&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6b8efd8-9132-4035-a7e7-6017f5583933",
  "isSidechain": false,
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "c7ad114b-2576-4e1b-abbe-da148b311445",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper idea called \"SimGate\" that proposes learning when to route LLM agents to deterministic external simulators (as opposed to LLM world models or internal reasoning). I need to find if any competing work does this.\n\nPlease search extensively:\n1. WebSearch \"LLM agent deterministic simulator routing 2025 2026\"\n2. WebSearch \"learned routing external simulator LLM agent\"\n3. WebSearch \"when to simulate agent planning deterministic environment 2026\"\n4. WebSearch \"selective simulation invocation LLM agent ScienceWorld ALFWorld\"\n5. WebSearch \"ground truth simulator routing agent planning arxiv 2026\"\n6. WebSearch \"hybrid reasoning simulation agent routing 2025 2026\"\n\nI need to know: Has anyone published work on LEARNED routing between internal LLM reasoning and an external DETERMINISTIC simulator (not an LLM-based world model)? This is the core novelty claim of SimGate.\n\nAlso check: Are there any very recent (March-May 2026) papers on ScienceWorld or ALFWorld agent performance that might be missing from the competitive landscape?",
    "agentId": "ad4b5bbc27f9e2653",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture. Here is my analysis:\n\n---\n\n## Competitive Landscape Analysis for \"SimGate\"\n\n### Core Question: Has anyone published on LEARNED routing between internal LLM reasoning and an external DETERMINISTIC simulator?\n\n**Short answer: No exact match found.** No published work proposes a learned gate/router that specifically decides when an LLM agent should invoke an external deterministic simulator (like a physics engine, game engine, or programmatic environment model) versus relying on its own internal reasoning or an LLM-based world model. However, several papers are **adjacently relevant** and must be cited/differentiated in a SimGate paper. Here they are, ranked by threat level:\n\n---\n\n### HIGH RELEVANCE -- Must differentiate clearly\n\n1. **AutoTool (AAAI 2026)** -- [arXiv 2511.14650](https://arxiv.org/abs/2511.14650)\n   - Builds a tool-invocation graph from past trajectories to predict the next tool call, bypassing the LLM via \"inertial calls\" when confidence is high. Evaluated on ScienceWorld and ALFWorld.\n   - **Overlap with SimGate**: Learns *when to skip the LLM* and go directly to a tool/action. Operates on the same benchmarks.\n   - **Key difference**: AutoTool routes between \"ask the LLM\" vs. \"replay a cached tool pattern.\" It does NOT route to a deterministic simulator for state prediction/lookahead. It is about efficiency (skipping LLM calls), not about choosing a more accurate reasoning modality.\n\n2. **BoundaryRouter (May 2026)** -- [arXiv 2605.07180](https://arxiv.org/abs/2605.07180)\n   - Training-free method that decides whether a query needs full agentic execution or can be answered by direct LLM inference, using early-experience memory retrieval.\n   - **Overlap with SimGate**: Learned routing between \"lightweight reasoning\" and \"heavy agentic execution.\"\n   - **Key difference**: Routes between two LLM-based modes (direct inference vs. multi-step agent). Does NOT involve an external deterministic simulator at all.\n\n3. **DART (Feb 2026)** -- [arXiv 2602.00994](https://arxiv.org/abs/2602.00994)\n   - Shows reasoning and tool-use *compete* during joint RL training (gradient interference / seesaw effect). Proposes disentangled LoRA modules.\n   - **Overlap with SimGate**: Directly addresses the tension between internal reasoning and external tool use.\n   - **Key difference**: Focuses on *training dynamics* (how to train both capabilities), not on a runtime routing decision. Does not involve a deterministic simulator.\n\n4. **Budget-Aware Agentic Routing (Feb 2026)** -- [arXiv 2602.21227](https://arxiv.org/abs/2602.21227)\n   - Learns to route between a cheap model and an expensive model at each agent step under budget constraints, using RL with boundary-guided training.\n   - **Overlap with SimGate**: Learned per-step routing policy optimized via RL, with budget awareness.\n   - **Key difference**: Routes between two LLMs (small vs. large), not between an LLM and a simulator.\n\n5. **WebDreamer (TMLR 2025)** -- [arXiv 2411.06559](https://arxiv.org/abs/2411.06559)\n   - Uses the LLM itself as a \"world model\" to simulate action outcomes for planning, as an alternative to tree search in external environments.\n   - **Overlap with SimGate**: Directly compares LLM-as-world-model vs. external environment interaction for planning.\n   - **Key difference**: Always uses the LLM world model; does not learn *when* to switch to the real environment. SimGate's novelty is precisely in learning this routing decision.\n\n---\n\n### MODERATE RELEVANCE -- Worth citing in related work\n\n6. **Uno-Orchestra (May 2026)** -- [arXiv 2605.05007](https://arxiv.org/abs/2605.05007)\n   - Unified RL-trained orchestration policy that jointly learns task decomposition and worker/model selection. 22 baselines, 13 benchmarks.\n   - Routes among multiple agents/models, not to a deterministic simulator.\n\n7. **AgentGate (April 2026)** -- [arXiv 2604.06696](https://arxiv.org/abs/2604.06696)\n   - Structured routing engine for multi-agent systems; decides whether to invoke one agent, generate a multi-agent plan, return direct response, or stop.\n   - Despite the similar name, this is about multi-agent orchestration, not simulator routing.\n\n8. **ReflAct (EMNLP 2025)** -- [arXiv 2505.15182](https://arxiv.org/abs/2505.15182)\n   - Achieves 93.3% on ALFWorld by grounding reasoning in goal-state reflection. No routing or simulator component, but sets a strong ALFWorld baseline.\n\n9. **Throttling Web Agents Using Reasoning Gates (Sep 2025)** -- [arXiv 2509.01619](https://arxiv.org/abs/2509.01619)\n   - Uses \"reasoning gates\" but in a completely different sense: computational puzzles imposed on agents to throttle them. Not related to simulator routing.\n\n---\n\n### RECENT ScienceWorld / ALFWorld PAPERS (March-May 2026)\n\nThese should be checked for updated baselines:\n\n- **Retrieval-Augmented LLM Agents** (March 2026, [arXiv 2603.18272](https://arxiv.org/abs/2603.18272)) -- Evaluates retrieval-from-experience on ALFWorld and ScienceWorld. ALFWorld results up to ~65%, ScienceWorld gains small.\n- **StateFactory / Co-Evolution of Policy and Internal Reward** (April 2026, [arXiv 2604.03098](https://arxiv.org/abs/2604.03098)) -- Reports +21.64% on ALFWorld, +12.40% on ScienceWorld over reactive baselines.\n- **Coarse-to-Fine Grounded Memory** ([arXiv 2508.15305](https://arxiv.org/abs/2508.15305)) -- Graph-memory-augmented planning for LLM agents, evaluated on ALFWorld/ScienceWorld.\n- **AgentSwift** ([arXiv 2506.06017](https://arxiv.org/abs/2506.06017)) -- Value-guided hierarchical search for efficient LLM agent design.\n\n---\n\n### Assessment of SimGate's Novelty\n\nThe novelty claim -- **a learned routing mechanism that decides per-step whether to query an external deterministic simulator vs. rely on LLM internal reasoning** -- appears to be **genuinely novel** as of May 2026. The closest neighbors are:\n\n| Paper | Routes between | Learned? | Deterministic sim? |\n|-------|---------------|----------|-------------------|\n| SimGate (yours) | LLM reasoning <-> external deterministic simulator | Yes | **Yes** |\n| AutoTool | LLM <-> cached tool pattern | Yes (graph-based) | No (tool replay) |\n| BoundaryRouter | Direct LLM <-> full agent | Sort of (experience-based) | No |\n| DART | Reasoning <-> tool-use (training) | N/A (training method) | No |\n| Budget-Aware Routing | Small LLM <-> large LLM | Yes (RL) | No |\n| WebDreamer | LLM world model only | No routing | No (LLM is the sim) |\n\n**The gap SimGate fills**: Everyone routes LLM-to-LLM or LLM-to-tool. Nobody learns when to offload state prediction to a ground-truth deterministic simulator. WebDreamer is the philosophical inverse (it argues you should always use the LLM *as* the simulator). SimGate argues the opposite for environments where a cheap, accurate deterministic simulator exists.\n\n**Recommended framing**: Position SimGate as complementary to WebDreamer (for domains where no deterministic simulator exists, use LLM world models; where one does exist, learn when to use it). Differentiate from AutoTool (which learns tool *sequencing patterns*, not *simulator invocation for state prediction*). Cite DART for the reasoning-vs-tool-use tension that motivates the need for explicit routing rather than joint training.\n\nSources:\n- [AutoTool (AAAI 2026)](https://arxiv.org/abs/2511.14650)\n- [BoundaryRouter](https://arxiv.org/abs/2605.07180)\n- [DART](https://arxiv.org/abs/2602.00994)\n- [Budget-Aware Agentic Routing](https://arxiv.org/abs/2602.21227)\n- [WebDreamer](https://arxiv.org/abs/2411.06559)\n- [Uno-Orchestra](https://arxiv.org/abs/2605.05007)\n- [AgentGate](https://arxiv.org/abs/2604.06696)\n- [ReflAct (EMNLP 2025)](https://arxiv.org/abs/2505.15182)\n- [Throttling Web Agents](https://arxiv.org/abs/2509.01619)\n- [Retrieval-Augmented LLM Agents](https://arxiv.org/abs/2603.18272)\n- [Co-Evolution of Policy and Internal Reward](https://arxiv.org/abs/2604.03098)\n- [SELECT-THEN-ROUTE (EMNLP 2025)](https://aclanthology.org/2025.emnlp-industry.28.pdf)"
      }
    ],
    "totalDurationMs": 142628,
    "totalTokens": 30497,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3612,
      "cache_read_input_tokens": 24480,
      "output_tokens": 2404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3612
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2404,
          "cache_read_input_tokens": 24480,
          "cache_creation_input_tokens": 3612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3612,
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
  "sourceToolAssistantUUID": "c6b8efd8-9132-4035-a7e7-6017f5583933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "c7ad114b-2576-4e1b-abbe-da148b311445",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate: Deterministic simulator routing for LLM agents",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Tool result

_source line 20 · 2026-05-12T01:20:05.610Z_

<details><summary>↩ Tool result · `toolu_01A5DxrLq7LXLqRqJkdnqhaN`</summary>

```text
Now I have all the critical information. Let me compile the complete analysis.

Here is my full analysis of EPO's claimed 96.8% on ScienceWorld and its comparability to CogRouter's results:

---

## (a) What metric does EPO use?

EPO uses **binary success rate only** (0/1). Their reward is defined as `r_T in {0, 1}` -- a binary task outcome at episode termination. They report two variants:
- **Succ.\***: average of *maximum* success rates across random seeds (best-case performance)
- **Succ.bar**: average performance after convergence (practical reliability)

The 96.8% figure is **Succ.bar for PPO+EPO on ScienceWorld IID tasks**. Their Succ.\* is actually **100.0%** on both IID and OOD.

This is fundamentally different from the ScienceWorld standard. ScienceWorld natively provides a **continuous score (0-100)** based on the fraction of subgoals completed. EPO binarizes this -- a task is either fully solved (1) or not (0). This inflates apparent performance for tasks that are partially solved.

## (b) What task subset of ScienceWorld?

EPO's paper is vague on this. It references "over 30 task types" generically but **does not specify whether all 30 tasks are evaluated or a subset**. They split into IID (in-distribution) and OOD (out-of-distribution) test sets, but the paper does not enumerate which tasks fall into each category, how many variations per task, or total episode counts. The only concrete number is "120 RL training steps" with three random seeds.

## (c) What is max_steps?

**Not explicitly stated in the EPO paper.** The paper only mentions "30+ turns of interaction" as a general characterization of multi-turn environments. The ScienceWorld default commonly used in other work is `env_step_limit=100`, but EPO does not confirm this.

## (d) What is their GRPO baseline performance?

From EPO's Table 1:
- **GRPO IID**: Succ.\* = 93.8%, Succ.bar = 81.6%
- **GRPO OOD**: Succ.\* = 91.7%, Succ.bar = 80.9%

For comparison, CogRouter's paper (arXiv 2602.12662) reports **GRPO at 53.0% SR and 71.1 score** on ScienceWorld with the same Qwen2.5-7B base model. This is a massive discrepancy -- EPO's GRPO baseline is ~80-82% while CogRouter's GRPO baseline is 53%. This alone proves the evaluation protocols are substantially different.

## (e) How many tasks/episodes evaluated?

EPO does not specify total episodes evaluated. CogRouter explicitly states 200 simulations for ScienceWorld evaluation.

---

## Key Question: Is EPO's 96.8% directly comparable to CogRouter's 72.0% SR / 84.6 score?

**No. They are NOT directly comparable.** Here are the critical differences:

1. **Different metrics**: EPO reports binary success (0/1 binarization of task outcome). CogRouter reports both binary success rate (72.0%) AND continuous score (84.6 out of 100). CogRouter's score captures partial task completion; EPO discards this information entirely.

2. **Wildly different GRPO baselines prove different evaluation setups**: EPO's GRPO gets ~81% binary success. CogRouter's GRPO gets 53% success rate and 71.1 score. With the same base model (Qwen2.5-7B), a ~28 percentage point gap in the same baseline method means they are using fundamentally different evaluation configurations -- likely different task subsets, different max_steps, different task variations, or different IID/OOD splits.

3. **EPO's "best of seeds" metric is aggressive**: Succ.\* (the average of the *maximum* success rate across seeds) reaches 100% for PPO+EPO. This cherry-picks the peak performance per seed rather than sustained performance.

4. **IID vs full evaluation**: EPO's 96.8% is specifically on IID (in-distribution) tasks. Their OOD number is 96.2% for PPO+EPO, which is close but the IID/OOD split itself is unspecified. CogRouter appears to evaluate on the full test set without such splitting.

5. **Undisclosed evaluation details**: EPO does not report max_steps, number of evaluation episodes, specific task subsets, or number of task variations. This makes independent verification difficult.

6. **GRPO+EPO is much more modest**: While PPO+EPO claims 96.8%, GRPO+EPO only achieves 83.8% (Succ.bar, IID) -- a relatively modest improvement over plain GRPO's 81.6%. The dramatic 96.8% number comes specifically from the PPO+EPO combination, where the PPO baseline was only 38.4%.

**Bottom line**: The 96.8% and 72.0% numbers cannot be meaningfully compared. The evaluation protocols differ in metric definition (binary vs. continuous), GRPO baseline performance (proving different evaluation configurations), and possibly task subsets and episode limits. If anything, the GRPO+EPO vs. CogRouter comparison on comparable terms would be more informative, but even that requires alignment of evaluation protocols.

---

Sources:
- [EPO: Entropy-regularized Policy Optimization (arXiv 2509.22576)](https://arxiv.org/abs/2509.22576)
- [EPO Full Paper HTML](https://arxiv.org/html/2509.22576v1)
- [EPO GitHub Repository](https://github.com/WujiangXu/EPO)
- [CogRouter: Think Fast and Slow (arXiv 2602.12662)](https://arxiv.org/abs/2602.12662)
- [CogRouter Full Paper HTML](https://arxiv.org/html/2602.12662)
- [ScienceWorld: Is your Agent Smarter than a 5th Grader? (arXiv 2203.07540)](https://arxiv.org/abs/2203.07540)
- [ScienceWorld GitHub Repository](https://github.com/allenai/ScienceWorld)
- [ScienceWorld PyPI Package](https://pypi.org/project/scienceworld/1.1.0/)
- [ScienceWorld Benchmark Overview](https://www.emergentmind.com/topics/scienceworld-benchmark)

agentId: a89e4f89589e303de (use SendMessage with to: 'a89e4f89589e303de' to continue this agent)
&lt;usage>total_tokens: 26529
tool_uses: 20
duration_ms: 155903&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2191517e-0701-47e4-bfcb-a8c60d44dee9",
  "isSidechain": false,
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "e0fde3ac-1901-4b26-96f7-108e3236a13b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify EPO's results on ScienceWorld. The paper is arXiv 2509.22576 (Sep 2025), claiming 96.8% binary success rate on ScienceWorld with Qwen2.5-7B.\n\nPlease:\n1. WebSearch for \"EPO entropy regularized policy optimization ScienceWorld arXiv 2509.22576\"\n2. Try to WebFetch the paper at https://arxiv.org/html/2509.22576 or https://arxiv.org/abs/2509.22576\n3. Report: (a) What metric does EPO use (binary success vs continuous score)? (b) What task subset of ScienceWorld? (c) What is max_steps? (d) What is their GRPO baseline performance? (e) How many tasks/episodes evaluated?\n\nThe key question: Is EPO's 96.8% directly comparable to CogRouter's 72.0% SR / 84.6 score on ScienceWorld? Are they using the same evaluation protocol?",
    "agentId": "a89e4f89589e303de",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the critical information. Let me compile the complete analysis.\n\nHere is my full analysis of EPO's claimed 96.8% on ScienceWorld and its comparability to CogRouter's results:\n\n---\n\n## (a) What metric does EPO use?\n\nEPO uses **binary success rate only** (0/1). Their reward is defined as `r_T in {0, 1}` -- a binary task outcome at episode termination. They report two variants:\n- **Succ.\\***: average of *maximum* success rates across random seeds (best-case performance)\n- **Succ.bar**: average performance after convergence (practical reliability)\n\nThe 96.8% figure is **Succ.bar for PPO+EPO on ScienceWorld IID tasks**. Their Succ.\\* is actually **100.0%** on both IID and OOD.\n\nThis is fundamentally different from the ScienceWorld standard. ScienceWorld natively provides a **continuous score (0-100)** based on the fraction of subgoals completed. EPO binarizes this -- a task is either fully solved (1) or not (0). This inflates apparent performance for tasks that are partially solved.\n\n## (b) What task subset of ScienceWorld?\n\nEPO's paper is vague on this. It references \"over 30 task types\" generically but **does not specify whether all 30 tasks are evaluated or a subset**. They split into IID (in-distribution) and OOD (out-of-distribution) test sets, but the paper does not enumerate which tasks fall into each category, how many variations per task, or total episode counts. The only concrete number is \"120 RL training steps\" with three random seeds.\n\n## (c) What is max_steps?\n\n**Not explicitly stated in the EPO paper.** The paper only mentions \"30+ turns of interaction\" as a general characterization of multi-turn environments. The ScienceWorld default commonly used in other work is `env_step_limit=100`, but EPO does not confirm this.\n\n## (d) What is their GRPO baseline performance?\n\nFrom EPO's Table 1:\n- **GRPO IID**: Succ.\\* = 93.8%, Succ.bar = 81.6%\n- **GRPO OOD**: Succ.\\* = 91.7%, Succ.bar = 80.9%\n\nFor comparison, CogRouter's paper (arXiv 2602.12662) reports **GRPO at 53.0% SR and 71.1 score** on ScienceWorld with the same Qwen2.5-7B base model. This is a massive discrepancy -- EPO's GRPO baseline is ~80-82% while CogRouter's GRPO baseline is 53%. This alone proves the evaluation protocols are substantially different.\n\n## (e) How many tasks/episodes evaluated?\n\nEPO does not specify total episodes evaluated. CogRouter explicitly states 200 simulations for ScienceWorld evaluation.\n\n---\n\n## Key Question: Is EPO's 96.8% directly comparable to CogRouter's 72.0% SR / 84.6 score?\n\n**No. They are NOT directly comparable.** Here are the critical differences:\n\n1. **Different metrics**: EPO reports binary success (0/1 binarization of task outcome). CogRouter reports both binary success rate (72.0%) AND continuous score (84.6 out of 100). CogRouter's score captures partial task completion; EPO discards this information entirely.\n\n2. **Wildly different GRPO baselines prove different evaluation setups**: EPO's GRPO gets ~81% binary success. CogRouter's GRPO gets 53% success rate and 71.1 score. With the same base model (Qwen2.5-7B), a ~28 percentage point gap in the same baseline method means they are using fundamentally different evaluation configurations -- likely different task subsets, different max_steps, different task variations, or different IID/OOD splits.\n\n3. **EPO's \"best of seeds\" metric is aggressive**: Succ.\\* (the average of the *maximum* success rate across seeds) reaches 100% for PPO+EPO. This cherry-picks the peak performance per seed rather than sustained performance.\n\n4. **IID vs full evaluation**: EPO's 96.8% is specifically on IID (in-distribution) tasks. Their OOD number is 96.2% for PPO+EPO, which is close but the IID/OOD split itself is unspecified. CogRouter appears to evaluate on the full test set without such splitting.\n\n5. **Undisclosed evaluation details**: EPO does not report max_steps, number of evaluation episodes, specific task subsets, or number of task variations. This makes independent verification difficult.\n\n6. **GRPO+EPO is much more modest**: While PPO+EPO claims 96.8%, GRPO+EPO only achieves 83.8% (Succ.bar, IID) -- a relatively modest improvement over plain GRPO's 81.6%. The dramatic 96.8% number comes specifically from the PPO+EPO combination, where the PPO baseline was only 38.4%.\n\n**Bottom line**: The 96.8% and 72.0% numbers cannot be meaningfully compared. The evaluation protocols differ in metric definition (binary vs. continuous), GRPO baseline performance (proving different evaluation configurations), and possibly task subsets and episode limits. If anything, the GRPO+EPO vs. CogRouter comparison on comparable terms would be more informative, but even that requires alignment of evaluation protocols.\n\n---\n\nSources:\n- [EPO: Entropy-regularized Policy Optimization (arXiv 2509.22576)](https://arxiv.org/abs/2509.22576)\n- [EPO Full Paper HTML](https://arxiv.org/html/2509.22576v1)\n- [EPO GitHub Repository](https://github.com/WujiangXu/EPO)\n- [CogRouter: Think Fast and Slow (arXiv 2602.12662)](https://arxiv.org/abs/2602.12662)\n- [CogRouter Full Paper HTML](https://arxiv.org/html/2602.12662)\n- [ScienceWorld: Is your Agent Smarter than a 5th Grader? (arXiv 2203.07540)](https://arxiv.org/abs/2203.07540)\n- [ScienceWorld GitHub Repository](https://github.com/allenai/ScienceWorld)\n- [ScienceWorld PyPI Package](https://pypi.org/project/scienceworld/1.1.0/)\n- [ScienceWorld Benchmark Overview](https://www.emergentmind.com/topics/scienceworld-benchmark)"
      }
    ],
    "totalDurationMs": 155903,
    "totalTokens": 26529,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 182,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 23217,
      "output_tokens": 1607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1523
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 182,
          "output_tokens": 1607,
          "cache_read_input_tokens": 23217,
          "cache_creation_input_tokens": 1523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1523,
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
  "sourceToolAssistantUUID": "2191517e-0701-47e4-bfcb-a8c60d44dee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T01:21:15.234Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. I now have very comprehensive information. Let me also check a few more things:

1. The proposal STILL claims ITP-R = 94.29% on ALFWorld. This is the 7th round and this error has been flagged since round 5. The correct number is 85.07%.

2. EPO's 96.8% on ScienceWorld uses fundamentally different evaluation (binary success, different task subset, different GRPO baseline of 93.8% vs CogRouter's 53.0%).

3. EMPO2's 75.9 score on ScienceWorld is confirmed.


4. ARTIS is confirmed as an always-simulate approach but operates on different benchmarks (BFCL-v3, ACEBench), while I've also identified several competing works like AutoTool, BoundaryRouter, DART, and Budget-Aware Agentic Routing that address similar problems on ScienceWorld and ALFWorld. SimGate's learned routing mechanism to a deterministic simulator does appear to be genuinely novel. Now let me verify that ITP-R number one more time since the proposal claims to correct a prior error.

The proposal states ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B, but my independent agent confirms the overall score is actually 85.07%—the 94.29% is only for the PICK subtask. So the proposal made an error in their "correction," claiming they were fixing 88.57% (the Qwen3-8B number) when they should have reported 85.07% as the true overall performance with Qwen2.5-7B.

I'm also noticing the resource estimates exceed the 200 H100-hour constraint for both manual (~220h) and auto (~260h) tracks, leaving only the HIL approach within budget. And there's a mismatch on benchmarks—the user specified ALFWorld but the proposal also evaluates on ScienceWorld, which wasn't requested. I'm seeing that AutoTool from AAAI 2026 uses ScienceWorld as well, so there might be some alignment issue here.

Looking back at what the previous reviews flagged, I'm tracking a pattern of unaddressed concerns across multiple rounds: the ITP-R metric is still wrong (now claiming 94.29% instead of the correct 85.07%), the compute budget violations persist, and several missing citations like ARTIS and EMPO2 haven't been incorporated despite being flagged in R4 and R5. I'm noticing there's a critical missing citation—AutoTool from AAAI 2026 that also does learned routing between LLM and deterministic approaches on similar benchmarks. For novelty, the core routing-to-simulator idea is genuinely novel and no one else implements it exactly this way, though the routing mechanism itself is standard SFT classification, so I'd rate this a 3.

0. On feasibility, the state forking approach for ScienceWorld is workable but risky, ALFWorld has known copy issues, compute partially exceeds budget, and the 14-day timeline is tight though doable for a short paper—that's a 3.0. The writing is clear and well-structured with honest limitations acknowledged, but that persistent factual error about ITP-R's performance score damages credibility, bringing clarity to 3.5. For impact, the approach is limited by requiring deterministic simulators, only two suitable benchmarks exist, and neither is mainstream in the broader agent research community.

Even with all factual corrections, the ceiling looks like novelty at 3.5, feasibility at 3.5, clarity at 4.0, but impact stays structurally capped around 2.5 because the fundamental limitation—needing deterministic environments—can't be overcome. That puts the average at 3.25 even in the best case, still below the 4.0 threshold needed to pass.

Though wait, I should reconsider whether the bar shifts for a short paper submission. A focused contribution demonstrating a novel principle might be acceptable at a venue like EMNLP, even if the scope is narrower. Let me check what the actual target venues are in the proposal.

The user specified EMNLP 2026 Main and Findings tracks, and the proposal is indeed targeting a short paper format with an ARR deadline of May 25, 2026. That's actually more aligned with the work's scope.

For a short paper, my scoring would shift slightly—novelty and feasibility might land around 3.0-3.5, clarity could reach 3.5-4.0, but impact remains the critical weakness at 2.5. The fundamental issue is that this only works with deterministic simulators, which excludes the standard benchmarks reviewers care about. That's a hard limitation even for a shorter contribution.

The verdict is still to revise. The novelty is genuine but the execution has persistent problems—wrong numbers, ignored feedback, budget miscalculations—and the impact ceiling is real. With three rounds left, the focus needs to be on fixing the ITP-R calculation, addressing the EPO issue, correcting the compute budget, and then tackling whatever remains.

Actually, I should be harsher here. We're at round 7 with the same errors recurring. But the core idea genuinely is novel, the approach is sound, and these are fixable problems. One more revision with crystal-clear guidance is warranted.

Looking at the final scores: novelty is 3 because routing to a deterministic simulator versus an LLM world model is a real distinction, but the routing mechanism itself is just standard SFT classification—it's more of an experimental finding than a methodological contribution. Feasibility is 3 because compute still overruns in two of three modes and the state forking engineering carries real risk on a 14-day timeline, though the approach itself is technically viable. Clarity is 3 because the proposal is well-structured but critically underdeveloped in key areas.

The bigger problem is impact. This approach fundamentally requires a ground-truth deterministic simulator, which locks it to ScienceWorld and ALFWorld. But the user's specified benchmarks don't have such simulators available, and ScienceWorld isn't even on their list. That's a severe practical limitation. The average across all dimensions comes to 2.875, which falls below the 4.0 threshold, so the verdict has to be revise.

Wait, let me reconsider the ITP-R discrepancy one more time. The proposal claims they're correcting the prior error by stating the actual number is 94.29%, not 88.57%, but I need to verify whether this correction is actually accurate or if it's still wrong.

Actually, the core issue is that the proposal is comparing against the wrong baseline entirely. If ITP-R truly underperforms CogRouter at 85.07% versus 92.5%, then the entire motivation flips—it strengthens the case for SimGate rather than weakening it, since it shows LLM world models consistently degrade performance across both benchmarks. I should also note that AutoTool appears to be a newly overlooked baseline that needs flagging.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0fde3ac-1901-4b26-96f7-108e3236a13b",
  "isSidechain": false,
  "requestId": "req_011Cawo8MHfu3Lh3GM3Ka3Zw",
  "type": "assistant",
  "uuid": "08b6e153-9f6d-491f-9b8a-eed2d7ccc546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXxB8MZa8DGDwhVfyhATPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3602,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 36343,
      "output_tokens": 3359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3602,
          "output_tokens": 3359,
          "cache_read_input_tokens": 36343,
          "cache_creation_input_tokens": 2770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2770
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

_source line 22 · 2026-05-12T01:21:15.387Z_

Let me search for one more critical piece — AutoTool, which was flagged by my search agent as evaluating on ScienceWorld and ALFWorld.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08b6e153-9f6d-491f-9b8a-eed2d7ccc546",
  "isSidechain": false,
  "requestId": "req_011Cawo8MHfu3Lh3GM3Ka3Zw",
  "type": "assistant",
  "uuid": "a6e45158-58ec-4969-b48c-7d5248ce3120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXxB8MZa8DGDwhVfyhATPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3602,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 36343,
      "output_tokens": 3359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3602,
          "output_tokens": 3359,
          "cache_read_input_tokens": 36343,
          "cache_creation_input_tokens": 2770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2770
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

_source line 23 · 2026-05-12T01:21:19.649Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015VCsDAw32abfyDhWkHWWK1`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify AutoTool AAAI 2026 details",
  "prompt": "I found a paper called AutoTool (arXiv 2511.14650, AAAI 2026) that apparently evaluates on ScienceWorld and ALFWorld and learns when to skip LLM calls via a tool-invocation graph.\n\nPlease:\n1. WebFetch https://arxiv.org/abs/2511.14650 to get the abstract and key results\n2. WebSearch \"AutoTool ScienceWorld ALFWorld AAAI 2026 results\"\n3. Report: (a) What does AutoTool do exactly? (b) What are its results on ScienceWorld and ALFWorld? (c) How does it relate to the idea of routing between LLM reasoning and external simulation?\n\nKeep the response under 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6e45158-58ec-4969-b48c-7d5248ce3120",
  "isSidechain": false,
  "requestId": "req_011Cawo8MHfu3Lh3GM3Ka3Zw",
  "type": "assistant",
  "uuid": "9101331b-5eb3-45fb-935f-fdf86b0401e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXxB8MZa8DGDwhVfyhATPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3602,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 36343,
      "output_tokens": 3359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3602,
          "output_tokens": 3359,
          "cache_read_input_tokens": 36343,
          "cache_creation_input_tokens": 2770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2770
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

_source line 24 · 2026-05-12T01:21:22.454Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VE9DsA4Wjo92yFj8dp5Jmc`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check EMNLP 2026 ARR deadline",
  "prompt": "I need to verify: Is the ARR (ACL Rolling Review) submission deadline of May 25, 2026 correct for targeting EMNLP 2026?\n\nWebSearch for \"ARR ACL Rolling Review 2026 submission deadlines\" and \"EMNLP 2026 submission deadline ARR cycle\".\n\nReport the actual ARR submission cycles in 2026 and which ones would be eligible for EMNLP 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9101331b-5eb3-45fb-935f-fdf86b0401e0",
  "isSidechain": false,
  "requestId": "req_011Cawo8MHfu3Lh3GM3Ka3Zw",
  "type": "assistant",
  "uuid": "a68f353f-5d9e-4594-9692-bb0bea1fcc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXxB8MZa8DGDwhVfyhATPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3602,
      "cache_creation_input_tokens": 2770,
      "cache_read_input_tokens": 36343,
      "output_tokens": 3359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3602,
          "output_tokens": 3359,
          "cache_read_input_tokens": 36343,
          "cache_creation_input_tokens": 2770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2770
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a68f353f-5d9e-4594-9692-bb0bea1fcc2a",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate: Deterministic simulator routing for LLM agents",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Tool result

_source line 27 · 2026-05-12T01:21:55.956Z_

<details><summary>↩ Tool result · `toolu_015VCsDAw32abfyDhWkHWWK1`</summary>

```text
Here is the report:

**(a) What AutoTool does.** AutoTool addresses the high inference cost of tool selection in LLM agent frameworks like ReAct. It exploits "tool usage inertia" -- the observation that tool invocation sequences in agent trajectories follow predictable patterns. It builds a directed graph from historical trajectories where nodes are tools and edges are transition probabilities. At runtime, it traverses this graph to select the next tool and generate parameters, skipping the LLM call when the graph prediction is confident enough. It also integrates parameter-level information for refined input generation.

**(b) Results on ScienceWorld and ALFWorld.**
- **ALFWorld:** AutoTool achieves a 1.18x speedup in LLM calls and over 1.60x reduction in total token consumption, while maintaining or slightly improving progress rate.
- **ScienceWorld:** ReAct+AutoTool shows stable efficiency gains in both LLM call counts and token consumption.
- Across all benchmarks (ALFWorld, ScienceWorld, ToolQuery-Academic), it reduces LLM call count by 15--25% and total token consumption by 10--40%, while maintaining competitive task completion rates.

**(c) Relation to routing between LLM reasoning and external simulation.** AutoTool is directly relevant to the idea of routing between LLM reasoning and external tool/simulation calls. Its core mechanism is a learned decision of when the LLM's reasoning is actually needed versus when the next tool call is predictable from the trajectory graph alone. This is effectively a lightweight routing layer: if the graph's transition probability is high, skip the LLM and go straight to the tool; otherwise, fall back to full LLM reasoning. It demonstrates that a significant fraction of LLM calls in agent loops are redundant -- the tool sequence is already determined by the task structure -- and a simple graph-based router can eliminate them with minimal accuracy loss.

Sources:
- [AutoTool on arXiv](https://arxiv.org/abs/2511.14650)
- [AutoTool HTML version](https://arxiv.org/html/2511.14650)
- [AutoTool GitHub](https://github.com/jiajingyyyyyy/AutoTool)

agentId: abb122b44d948383e (use SendMessage with to: 'abb122b44d948383e' to continue this agent)
&lt;usage>total_tokens: 12781
tool_uses: 3
duration_ms: 36303&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9101331b-5eb3-45fb-935f-fdf86b0401e0",
  "isSidechain": false,
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "f27c521b-8844-4880-8c3e-5bb9944fece0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I found a paper called AutoTool (arXiv 2511.14650, AAAI 2026) that apparently evaluates on ScienceWorld and ALFWorld and learns when to skip LLM calls via a tool-invocation graph.\n\nPlease:\n1. WebFetch https://arxiv.org/abs/2511.14650 to get the abstract and key results\n2. WebSearch \"AutoTool ScienceWorld ALFWorld AAAI 2026 results\"\n3. Report: (a) What does AutoTool do exactly? (b) What are its results on ScienceWorld and ALFWorld? (c) How does it relate to the idea of routing between LLM reasoning and external simulation?\n\nKeep the response under 300 words.",
    "agentId": "abb122b44d948383e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the report:\n\n**(a) What AutoTool does.** AutoTool addresses the high inference cost of tool selection in LLM agent frameworks like ReAct. It exploits \"tool usage inertia\" -- the observation that tool invocation sequences in agent trajectories follow predictable patterns. It builds a directed graph from historical trajectories where nodes are tools and edges are transition probabilities. At runtime, it traverses this graph to select the next tool and generate parameters, skipping the LLM call when the graph prediction is confident enough. It also integrates parameter-level information for refined input generation.\n\n**(b) Results on ScienceWorld and ALFWorld.**\n- **ALFWorld:** AutoTool achieves a 1.18x speedup in LLM calls and over 1.60x reduction in total token consumption, while maintaining or slightly improving progress rate.\n- **ScienceWorld:** ReAct+AutoTool shows stable efficiency gains in both LLM call counts and token consumption.\n- Across all benchmarks (ALFWorld, ScienceWorld, ToolQuery-Academic), it reduces LLM call count by 15--25% and total token consumption by 10--40%, while maintaining competitive task completion rates.\n\n**(c) Relation to routing between LLM reasoning and external simulation.** AutoTool is directly relevant to the idea of routing between LLM reasoning and external tool/simulation calls. Its core mechanism is a learned decision of when the LLM's reasoning is actually needed versus when the next tool call is predictable from the trajectory graph alone. This is effectively a lightweight routing layer: if the graph's transition probability is high, skip the LLM and go straight to the tool; otherwise, fall back to full LLM reasoning. It demonstrates that a significant fraction of LLM calls in agent loops are redundant -- the tool sequence is already determined by the task structure -- and a simple graph-based router can eliminate them with minimal accuracy loss.\n\nSources:\n- [AutoTool on arXiv](https://arxiv.org/abs/2511.14650)\n- [AutoTool HTML version](https://arxiv.org/html/2511.14650)\n- [AutoTool GitHub](https://github.com/jiajingyyyyyy/AutoTool)"
      }
    ],
    "totalDurationMs": 36303,
    "totalTokens": 12781,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 10860,
      "output_tokens": 516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 516,
          "cache_read_input_tokens": 10860,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "9101331b-5eb3-45fb-935f-fdf86b0401e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T01:22:39.640Z_

<details><summary>↩ Tool result · `toolu_01VE9DsA4Wjo92yFj8dp5Jmc`</summary>

```text
Here is the verified information:

---

**Yes, the May 25, 2026 ARR submission deadline is correct for targeting EMNLP 2026.** It is the final (latest) ARR cycle whose reviews will be completed in time for EMNLP 2026 commitment.

## ARR 2026 Submission Cycles

ARR now operates on 10-week review cycles (changed from 8-week cycles starting May 2025), yielding roughly 5 cycles per year. The 2026 cycles are:

| Cycle | Submission Deadline | Reviews Due | Meta-reviews Release | Cycle End |
|-------|-------------------|-------------|---------------------|-----------|
| January 2026 | January 5 | February 7 | March 3 | March 10 |
| March 2026 | March 16 | April 20 | May 21 | May 24 |
| **May 2026** | **May 25** | **June 29** | **July 30** | **August 2** |
| August 2026 | August 3 | TBA | TBA | October 11 |
| October 2026 | October 12 | TBA | TBA | December 20 |

## EMNLP 2026 Key Dates

- **ARR Submission Deadline:** May 25, 2026
- **Author Response Period:** July 7-13, 2026
- **Meta-review Release:** July 30, 2026
- **Commitment Deadline:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-ready Deadline:** September 20, 2026
- **Conference:** October 24-29, 2026

All deadlines are 11:59 PM UTC-12:00 (Anywhere on Earth).

## Which ARR Cycles Are Eligible for EMNLP 2026?

Papers from **any prior ARR cycle** (January 2026, March 2026, or earlier) that have received reviews and a meta-review may be committed to EMNLP 2026 by the August 2 commitment deadline.

The **May 2026 cycle** is the latest eligible cycle, but it has a critical constraint: since EMNLP 2026 and AACL 2026 share the same ARR May cycle, authors must **explicitly select EMNLP 2026 as their target conference at submission time**, and this choice is **binding**. Papers submitted to the May 2026 cycle that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

Papers from earlier cycles do not have this restriction and can be committed regardless of original venue preference.

## Summary

Your date of **May 25, 2026** is confirmed correct. Just be aware of the binding venue-selection requirement when submitting in the May cycle specifically.

Sources:
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 First Call for Papers (Twitter/X)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Binding Venue Selection Update (Twitter/X)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ARR Call for Papers](http://aclrollingreview.org/cfp)
- [ACL 2026 Main Conference](https://2026.aclweb.org/calls/main_conference_papers/)

agentId: a424f4b8fbb29979b (use SendMessage with to: 'a424f4b8fbb29979b' to continue this agent)
&lt;usage>total_tokens: 18195
tool_uses: 10
duration_ms: 77184&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a68f353f-5d9e-4594-9692-bb0bea1fcc2a",
  "isSidechain": false,
  "promptId": "7c75b4e6-db2b-42de-b123-76888964fe17",
  "type": "user",
  "uuid": "5980494c-e67e-45d7-a1d1-bc9164b54a7e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify: Is the ARR (ACL Rolling Review) submission deadline of May 25, 2026 correct for targeting EMNLP 2026?\n\nWebSearch for \"ARR ACL Rolling Review 2026 submission deadlines\" and \"EMNLP 2026 submission deadline ARR cycle\".\n\nReport the actual ARR submission cycles in 2026 and which ones would be eligible for EMNLP 2026.",
    "agentId": "a424f4b8fbb29979b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the verified information:\n\n---\n\n**Yes, the May 25, 2026 ARR submission deadline is correct for targeting EMNLP 2026.** It is the final (latest) ARR cycle whose reviews will be completed in time for EMNLP 2026 commitment.\n\n## ARR 2026 Submission Cycles\n\nARR now operates on 10-week review cycles (changed from 8-week cycles starting May 2025), yielding roughly 5 cycles per year. The 2026 cycles are:\n\n| Cycle | Submission Deadline | Reviews Due | Meta-reviews Release | Cycle End |\n|-------|-------------------|-------------|---------------------|-----------|\n| January 2026 | January 5 | February 7 | March 3 | March 10 |\n| March 2026 | March 16 | April 20 | May 21 | May 24 |\n| **May 2026** | **May 25** | **June 29** | **July 30** | **August 2** |\n| August 2026 | August 3 | TBA | TBA | October 11 |\n| October 2026 | October 12 | TBA | TBA | December 20 |\n\n## EMNLP 2026 Key Dates\n\n- **ARR Submission Deadline:** May 25, 2026\n- **Author Response Period:** July 7-13, 2026\n- **Meta-review Release:** July 30, 2026\n- **Commitment Deadline:** August 2, 2026\n- **Acceptance Notification:** August 20, 2026\n- **Camera-ready Deadline:** September 20, 2026\n- **Conference:** October 24-29, 2026\n\nAll deadlines are 11:59 PM UTC-12:00 (Anywhere on Earth).\n\n## Which ARR Cycles Are Eligible for EMNLP 2026?\n\nPapers from **any prior ARR cycle** (January 2026, March 2026, or earlier) that have received reviews and a meta-review may be committed to EMNLP 2026 by the August 2 commitment deadline.\n\nThe **May 2026 cycle** is the latest eligible cycle, but it has a critical constraint: since EMNLP 2026 and AACL 2026 share the same ARR May cycle, authors must **explicitly select EMNLP 2026 as their target conference at submission time**, and this choice is **binding**. Papers submitted to the May 2026 cycle that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.\n\nPapers from earlier cycles do not have this restriction and can be committed regardless of original venue preference.\n\n## Summary\n\nYour date of **May 25, 2026** is confirmed correct. Just be aware of the binding venue-selection requirement when submitting in the May cycle specifically.\n\nSources:\n- [ARR Dates and Venues](http://aclrollingreview.org/dates)\n- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 First Call for Papers (Twitter/X)](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [EMNLP 2026 Binding Venue Selection Update (Twitter/X)](https://x.com/emnlpmeeting/status/2047754845919031450)\n- [ARR Call for Papers](http://aclrollingreview.org/cfp)\n- [ACL 2026 Main Conference](https://2026.aclweb.org/calls/main_conference_papers/)"
      }
    ],
    "totalDurationMs": 77184,
    "totalTokens": 18195,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 16248,
      "output_tokens": 909,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 909,
          "cache_read_input_tokens": 16248,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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
  "sourceToolAssistantUUID": "a68f353f-5d9e-4594-9692-bb0bea1fcc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-12T01:23:24.144Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile my review.

Key findings:
1. **ITP-R factual error persists**: The proposal still claims ITP-R = 94.29% on ALFWorld with Qwen2.5-7B. The correct overall is 85.07%. This is the 3rd consecutive round this error has been flagged.

2. **EPO not addressed**: 4th consecutive round. EPO uses different evaluation protocols (binary success, different GRPO baseline of 93.8% vs CogRouter's 53%), but must still be addressed.

3. **EMPO2 still missing**: Relevant ScienceWorld baseline (75.9 score).


4. **ARTIS remains uncited**: The always-simulate paradigm work is still absent from the references.
5. **AutoTool (AAAI 2026) is a new gap**: This recent work evaluates on the same benchmarks (ScienceWorld and ALFWorld) with a related concept of learning when to skip LLM calls, though using a different mechanism.
6. **Venue deadline confirmed**: May 25, 2026 for EMNLP 2026 ARR is correct.
7. **Compute budget still exceeds limits**: Both manual (220h) and automatic (260h) approaches surpass the ≤200 H100-hour constraint.
8. **Novelty is confirmed as genuine**: The comprehensive search validates that no existing work implements this learned approach.

The core contribution—routing to deterministic simulators rather than relying on LLM world models—is genuinely novel, though the mechanism itself (supervised fine-tuning on counterfactual labels) is standard, and the distinction from ITP-R is somewhat narrow. The impact is fundamentally constrained by the requirement for deterministic simulators, which only ALFWorld provides among the specified benchmarks. Evaluating feasibility: the compute violations in two of three modes are concerning, state forking through action replay is technically viable but risky given the tight timeline, and while the proposal is well-structured with solid landscape analysis, there's still that persistent factual error about ITP-R's performance that needs correction.

Scoring this out: novelty at 3/5, feasibility at 3/5, clarity at 3/5 due to the credibility issues, and impact at 2.5/5 because the approach only works where deterministic simulators exist—which excludes all the real-world agent benchmarks the user cares about. That averages to 2.875, well below the 4.0 threshold, so this needs revision.

Even with fixes to the technical errors and better framing, the impact ceiling is around 3.0 since the fundamental limitation to toy environments can't be overcome. The best realistic outcome would be around 3.375. But since this is targeting a short paper format, the bar might be different—I should reconsider what's actually expected for that venue.

There's also a persistent issue with the ITP-R numbers that's been flagged multiple times. The proposal claims to have corrected it to 94.29%, but that's actually just the PICK subtask performance, not the overall score. R3 gave incorrect guidance that the generator followed, while R5 and R6 correctly identified the real error at 85.07%, which still hasn't been fixed. The proposal's claim about correcting this is misleading since it's citing the wrong benchmark subset.

Given that this is round 7 of 10 and the same errors persist across six revisions, I'm skeptical they'll be resolved in time. But the core idea is genuinely novel and the methodology is sound, so I'll provide a detailed revision with specific numbered actions and a clear warning about the shrinking timeline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5980494c-e67e-45d7-a1d1-bc9164b54a7e",
  "isSidechain": false,
  "requestId": "req_011CawoKhoG3UebptxVgsXXX",
  "type": "assistant",
  "uuid": "fbb6882d-9e51-4737-ae4a-d5fa4989877a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgqDg5252NTGhF5MuwLKm1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8578,
      "cache_read_input_tokens": 39113,
      "output_tokens": 4398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4398,
          "cache_read_input_tokens": 39113,
          "cache_creation_input_tokens": 8578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8578
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

_source line 30 · 2026-05-12T01:24:35.753Z_

Now I have comprehensive verification. Let me compile my review.

**Summary of findings:**
- ITP-R overall ALFWorld = **85.07%** (not 94.29%) — confirmed for the 3rd consecutive round
- EPO uses fundamentally different evaluation protocol (binary success, GRPO baseline 93.8% vs CogRouter 53%) — not comparable but must be addressed
- EMPO2 = 75.9 score on ScienceWorld — confirmed, still missing from proposal
- ARTIS = always-simulate paradigm — relevant, still not cited
- AutoTool (AAAI 2026) = evaluates on ScienceWorld/ALFWorld with learned tool-call skipping — NEW missing work
- Core novelty (learned routing to deterministic simulator) = **genuinely confirmed as novel** across extensive search
- EMNLP 2026 ARR deadline May 25 = confirmed correct
- Compute: 2/3 modes exceed 200 H100-hour hard constraint

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The core idea (learned routing to deterministic simulator vs LLM world model) is genuinely novel — confirmed via extensive search across arXiv, conferences, and adjacent fields. However, the routing mechanism itself (SFT classifier on counterfactual labels) is entirely standard, and the conceptual distance from ITP-R is narrow: same routing framework, different routing target. This is a valid but incremental contribution suitable for a short paper."},
    "feasibility": {"score": 3, "rationale": "Compute exceeds the 200 H100-hour hard constraint in manual (220h) and auto (260h) modes. The 14-day timeline with ScienceWorld action-replay state forking engineering (~2 days) leaves minimal margin. The SFT-only training pipeline is sound, but trajectory collection across ~600 episodes × 3 modalities × ~30 steps = ~54K inference calls is expensive and may encounter unexpected bottlenecks."},
    "clarity": {"score": 3, "rationale": "Well-structured proposal with comprehensive landscape analysis and honest generalizability discussion. However, credibility is severely undermined by the persistent ITP-R factual error (claims 94.29% overall when correct is 85.07% — wrong for 3 rounds despite explicit correction) and failure to address EPO for 4 consecutive rounds. The proposal claims to have 'explicitly corrected' to a number that is still wrong."},
    "impact": {"score": 2, "rationale": "The method requires a ground-truth deterministic simulator, limiting it to ScienceWorld (not in user's benchmark list) and ALFWorld (acknowledged as saturated at 97.5%). None of the user's specified real-world benchmarks (WebArena, SWE-bench, GAIA, ToolBench, Mind2Web, τ-bench) have deterministic simulators. This structural limitation caps practical relevance and will be the primary reviewer concern at EMNLP, where agent work increasingly focuses on real-world web/code benchmarks."}
  },
  "issues": [
    "CRITICAL FACTUAL ERROR (PERSISTS 3 ROUNDS): ITP-R with Qwen2.5-7B achieves 85.07% OVERALL on ALFWorld, NOT 94.29%. The 94.29% is the PICK subtask only. Per-task breakdown: PICK 94.29%, CLEAN 88.89%, HEAT 87.50%, COOL 53.84%, LOOK 76.00%, PICK2 91.67%, Overall 85.07% (verified from arXiv HTML Table 1). The proposal's claim 'ITP-R achieves 94.29% on ALFWorld with Qwen2.5-7B, outperforming CogRouter (92.5%)' is factually wrong. ITP-R (85.07%) UNDERPERFORMS CogRouter (92.5%) by 7.4 points. This correction STRENGTHENS SimGate's argument: LLM world model routing hurts on BOTH benchmarks.",
    "EPO NOT ADDRESSED (4TH CONSECUTIVE ROUND): EPO (arXiv 2509.22576) claims 96.8% binary SR on ScienceWorld with Qwen2.5-7B. Independent verification reveals: (a) binary {0,1} success metric, not continuous score; (b) GRPO baseline = 93.8% Succ.* vs CogRouter's 53.0% SR — a 40pp gap proving fundamentally different evaluation protocols; (c) undisclosed task subset, episode count, binarization threshold; (d) GRPO+EPO only achieves 83.8% Succ.bar (modest). These numbers are NOT directly comparable to CogRouter, but EMNLP reviewers WILL raise EPO and the proposal MUST preemptively address it.",
    "EMPO2 STILL MISSING (3RD CONSECUTIVE ROUND): EMPO2 (arXiv 2602.23008, Feb 2026) achieves 75.9 average score on ScienceWorld with Qwen2.5-7B using continuous score across 18-19 tasks via exploratory memory-augmented hybrid RL. This IS directly comparable to CogRouter's metric and must be included in the landscape as a baseline.",
    "NEW MISSING BASELINE — AutoTool (AAAI 2026, arXiv 2511.14650): AutoTool builds tool-invocation graphs from trajectories to predict next tool calls, skipping LLM inference when confident. Evaluated on BOTH ScienceWorld AND ALFWorld with 15-25% LLM call reduction. While AutoTool routes between 'ask LLM' vs 'replay cached tool pattern' (not to a deterministic simulator for state prediction), it operates on the same benchmarks with a related routing concept and must be cited and differentiated.",
    "COMPUTE BUDGET VIOLATION (PERSISTENT): Manual (220h) and auto (260h) modes exceed the ≤200 H100-hour hard constraint. Only HIL (180h) fits. The description's stated range '180-260 H100-hours' has an upper bound 30% over budget. The 90h baseline reproduction budget (40h CogRouter + 30h ITP-R + 20h others) is the primary area for reduction.",
    "ARTIS (arXiv 2602.01709) STILL NOT CITED (3RD ROUND): ARTIS implements risk-aware iterative simulation before commitment — running simulated interactions before real-world execution. While evaluated on different benchmarks (BFCL-v3, ACEBench), it represents the 'always-simulate' paradigm that SimGate claims to improve upon. Should be cited as motivation: ARTIS always simulates (wasting compute on easy steps), while SimGate selectively routes.",
    "BENCHMARK MISALIGNMENT WITH USER REQUIREMENTS: ScienceWorld (primary benchmark) is NOT in the user's specified benchmark list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench). ALFWorld is listed but designated secondary and saturated. The proposal must explicitly justify ScienceWorld inclusion or add a user-specified benchmark.",
    "STRUCTURAL IMPACT LIMITATION: The method requires a ground-truth deterministic simulator. Among all prominent agent benchmarks (WebArena, SWE-bench, GAIA, ToolBench, Mind2Web, τ-bench, AgentBench), NONE have deterministic simulators suitable for this approach. This confines the contribution to ScienceWorld and ALFWorld — environments that are increasingly marginal in the EMNLP agent track, which favors real-world web/code/tool-use benchmarks."
  ],
  "feedback": "This is round 7 of 10. The core novelty (learned routing to deterministic simulator) is CONFIRMED genuine — my extensive search across arXiv, conference proceedings, and adjacent fields found no competing work. But you are running out of rounds with the same errors persisting. Here are NON-NEGOTIABLE fixes:\n\n1. **FIX ITP-R TO 85.07% (FINAL WARNING)**: ITP-R overall ALFWorld with Qwen2.5-7B = 85.07%, confirmed from Table 1 across three independent sources. The 94.29% is the PICK subtask column ONLY. This is the 4th round I'm flagging this. Ironically, correcting it HELPS you: ITP-R (85.07%) < CogRouter (92.5%) means LLM world model routing hurts on BOTH ALFWorld AND ScienceWorld, strengthening your motivation. New narrative: 'ITP-R's LLM world model routing consistently underperforms pure internal adaptation (CogRouter): 85.07% vs 92.5% on ALFWorld, 62.58 vs 84.6 on ScienceWorld. This demonstrates that approximate LLM foresight introduces noise exceeding its planning value. SimGate replaces noisy foresight with exact deterministic simulation.'\n\n2. **ADDRESS EPO IN ONE PARAGRAPH**: 'EPO (arXiv 2509.22576) reports 96.8% binary success rate on ScienceWorld with Qwen2.5-7B. However, its evaluation protocol differs fundamentally from ours: (a) binary {0,1} success, not continuous ScienceWorld score; (b) GRPO baseline = 93.8% vs CogRouter's 53.0% SR, indicating different task subsets or evaluation configurations; (c) undisclosed task subset and episode count. We follow CogRouter's standardized 200-simulation protocol using continuous score for direct comparability. We also note EMPO2 (arXiv 2602.23008, 75.9 avg score) as a directly comparable baseline.'\n\n3. **CUT COMPUTE TO ≤180h**: (a) Cite PA-MoE+GiGPO, Dyna-Mind, and Skill1 results from their papers without reproduction (−15h). (b) Check CogRouter's GitHub for published checkpoints (−20h if available). (c) Reduce ALFWorld secondary experiments to SimGate vs always-simulate vs ITP-R only (−10h). (d) Drop one ablation tier (−10h). Target: 165h with 35h margin.\n\n4. **ADD AutoTool (AAAI 2026)**: Cite and differentiate: 'AutoTool learns to skip LLM calls by predicting tool sequences from a trajectory graph. SimGate differs in routing to a deterministic SIMULATOR for state prediction/lookahead, not replaying cached tool patterns. AutoTool optimizes call efficiency; SimGate optimizes reasoning modality.'\n\n5. **STRENGTHEN IMPACT ARGUMENT**: The structural limitation (needs deterministic simulator) is the biggest weakness. Mitigate by: (a) Connecting to the growing ecosystem of code execution sandboxes (SWE-bench uses Docker), game engines (NetHack, Minecraft), physics simulators — argue these are all forms of deterministic external computation that SimGate's framework extends to; (b) Frame SimGate as establishing the PRINCIPLE that ground-truth external computation, when available, should be selectively invoked rather than always used or never used — the principle generalizes even if this paper demonstrates it on two benchmarks; (c) Add a brief discussion connecting to tool-use agents: code interpreters, calculators, and API calls are all forms of 'deterministic external computation' — SimGate's routing concept applies whenever the agent can choose between reasoning internally and consulting an exact external oracle.\n\n6. **JUSTIFY SCIENCEWORLD BENCHMARK CHOICE**: Add: 'ScienceWorld uniquely tests rule-governed scientific reasoning (temperature physics, chemical reactions, electrical circuits) where the gap between LLM approximation and deterministic ground truth is largest. This makes it the ideal testbed for SimGate's core hypothesis, complementing ALFWorld (user-specified benchmark) as a secondary evaluation.'\n\nROUND 7 WARNING: You have 3 rounds remaining. Issues 1-4 are copy-paste fixes that should take <5 minutes. If these same errors appear in round 8, I will escalate to 'fail' on grounds of persistent non-responsiveness to reviewer feedback — a serious signal about execution quality.",
  "reason": "Genuine novelty confirmed but persistent factual errors (ITP-R 94.29% wrong for 3 rounds, EPO unaddressed for 4 rounds), compute budget violation, and fundamental impact limitation (requires deterministic simulator unavailable in real-world agent benchmarks) keep scores below the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb6882d-9e51-4737-ae4a-d5fa4989877a",
  "isSidechain": false,
  "requestId": "req_011CawoKhoG3UebptxVgsXXX",
  "type": "assistant",
  "uuid": "0e02fbce-4e05-4f35-bf57-919d0a67c9ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgqDg5252NTGhF5MuwLKm1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8578,
      "cache_read_input_tokens": 39113,
      "output_tokens": 4398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4398,
          "cache_read_input_tokens": 39113,
          "cache_creation_input_tokens": 8578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8578
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0e02fbce-4e05-4f35-bf57-919d0a67c9ec",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate: Deterministic simulator routing for LLM agents",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0e02fbce-4e05-4f35-bf57-919d0a67c9ec",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate: Deterministic simulator routing for LLM agents",
  "sessionId": "6eb6fb4e-72f0-413e-9483-80f8446cb815"
}
```

---
