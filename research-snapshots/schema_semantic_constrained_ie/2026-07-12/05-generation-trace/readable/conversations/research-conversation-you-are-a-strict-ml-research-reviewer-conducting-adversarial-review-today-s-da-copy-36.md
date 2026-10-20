# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/c9adbf04-de42-4c7e-9a1f-ef44ae6c4057.jsonl`
- **Structured JSON:** [`e6dff385adb04d304906.json`](../../sessions/e6/e6dff385adb04d304906.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:42:24.226Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:42:24.226Z",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"CurriculumRLVR-IE: Reward Signal Topology Theory for Implicit Sequential Skill Curriculum in GRPO Information Extraction\",\n  \"core_problem\": \"The fundamental question in GRPO-based information extraction (IE) is not merely 'how should rewards be decomposed?' but 'why does reward decomposition produce curriculum effects — and for which structural properties of the reward signal?' No published work has answered this question formally. The IE reward literature (ProUIE, R1-RE, R2GRPO, EXTRACT-0) treats reward design as empirical engineering; no paper analyzes the mathematical properties of reward components that determine convergence ordering in policy gradient training.\\n\\nThe central claim of this paper is a **Signal Topology Analysis** for GRPO-IE: the topological property of a reward component — specifically whether it is **continuous** (takes values in [0,1], like span-IoU), **binary** (takes values in {0,1}, like span+type conjunction), or **compositional** (conditioned on multiple binary components, like argument F1) — determines its gradient variance in early GRPO training, and therefore determines convergence ordering without explicit curriculum scheduling. This is a structural claim, not an empirical one.\\n\\nFormally: for a GRPO policy with per-rollout reward R = Σᵢ αᵢ Rᵢ, the gradient variance contribution of component i scales as αᵢ² · Var(Rᵢ). For span-IoU (continuous, Beta-distributed), Var(R_span) is bounded by the variance of a symmetric Beta. For span+type conjunction (binary, Bernoulli with p = p_s · p_t), Var(R_type) = p_s·p_t·(1−p_s·p_t), which exceeds Var(R_span) in early training when p_s, p_t < 0.5 because the conjunction probability product p_s·p_t < p_s drives the Bernoulli toward its maximum variance regime. The variance inequality Var(R_span) < Var(R_type) < Var(R_arg) is a structural consequence of reward topology. **Condition (φ-sufficiency)**: This ordering holds if and only if the span-IoU empirical distribution satisfies the Beta concentration parameter φ > φ*(p_s, p_t) ≡ μ_s(1−μ_s)/(p_s·p_t·(1−p_s·p_t)) − 1. This is an empirically verifiable condition: a U-shaped (bimodal) span-IoU distribution (φ < 1) would indicate pathological span generation behavior and reverse the ordering. Under the natural early-training regime where the model produces near-zero IoU for most spans (monotonically decreasing Beta, φ > 1), the condition is structurally satisfied. Verification: the dry run fits an ML-estimated Beta to span-IoU values and performs a KS test; if φ̂ > φ*, the analysis's ordering is confirmed for this run. arXiv:2605.02375 independently establishes that binary rewards create degeneracy (infinite maximizing distributions, diversity collapse) in policy gradient methods, providing independent theoretical support for why binary type-conjunction rewards are problematic.\\n\\nThe consequence is an implicit curriculum that is an **analysis prediction (conditional on φ-sufficiency)**, not an empirically discovered phenomenon: (1) the span component provides lower-variance gradient signal in early training, causing span detection to converge first; (2) as p_s increases (span accuracy improves), p_t | (span correct) rises (type classification is a simpler Bernoulli conditioned on correct localization), reducing Var(R_type) and enabling type convergence; (3) argument F1 receives cleaner signal only after both span and type have stabilized, because its compound conditional variance is dominated by the upstream binary variance terms. The span→type→argument sequential convergence is predicted by the analysis before any experiment runs — and falsifiable by the per-component F1 learning curves.\\n\\nWhy the analysis matters for IE: Current GRPO-IE methods (ProUIE, arXiv:2604.10633) use atomic (span, type) rewards, treating span+type conjunction as the fundamental unit. This eliminates span-IoU's continuous signal, forcing the model to learn from a Bernoulli with p = p_s·p_t — the lowest-probability joint event, maximizing gradient variance. ProUIE reports ACE2005 Argument F1=52.58% vs. InstructUIE's 72.94% (a 20-point gap) and calls for 'more appropriate reward design,' but does not identify why its SFR structure creates the gap. The Signal Topology Analysis provides this identification: atomic rewards destroy the variance ordering that produces implicit curriculum, causing type and argument learning to plateau while span detection catches up through noisy, high-variance gradient updates.\\n\\nCSPO (arXiv:2604.10918, ACL 2026) shows empirically that component-specific token-level gradient routing helps for table-to-LaTeX generation (structure/style/content decomposition), using the framing of 'reward ambiguity.' CSPO provides no theoretical explanation of WHY different components have different convergence dynamics, what structural property of the reward determines the ordering, or whether static component routing is sufficient or whether adaptive weighting is needed. The Signal Topology Analysis provides the theoretical foundation for CSPO's empirical observation — and, crucially, predicts when static routing is insufficient (when the variance ordering creates a hierarchy that fixed weights cannot enforce) and motivates the convergence-gap adaptive weighting as an analysis-derived algorithm rather than an empirical heuristic.\",\n  \"opportunity\": \"The Signal Topology Analysis creates three opportunity axes, hierarchically ordered: one theoretical (the conditional proposition itself), one algorithmic (its direct application), and one empirical (its falsifiable prediction plus the φ-verification protocol).\\n\\n**Axis 1 (Theoretical — primary novelty and paper identity)**: The Signal Topology Analysis (Conditional Proposition) for GRPO-IE. No published work has formally characterized the relationship between reward component topology (continuous/binary/compositional) and gradient variance ordering in GRPO for structured prediction. The closest work:\\n- RuCL (arXiv:2602.21628): Shows two-tier rubric curriculum via reward decomposition (Appendix B gradient variance analysis) for multimodal reasoning, but analyzes easy/hard rubric difficulty ordering, NOT the continuous/binary topological distinction as the mechanism. RuCL's variance reduction comes from reliable vs. unreliable rubrics — our analysis shows the deeper structural reason: reliable signals are reliable because they are continuous, not because they are 'easy.'\\n- arXiv:2602.14872 (relay regime): Proves implicit curriculum at task-level difficulty ordering. Our analysis extends the relay concept from task level to reward-component level: within a single IE task, span-IoU continuity provides the 'smooth gradient handoff' that prevents plateau, analogous to how smooth difficulty spectrum prevents grokking at task level.\\n- arXiv:2604.19857 (Reward Decomposition Theorem): Bounds sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T). Complementary but different question: they ask 'how much do we lose by decomposing?' and bound the cost; we ask 'why does the span component help MORE than theory predicts?' and answer: because continuous topology reduces early-training variance, making the benefit dominate the bounded cost.\\n- CSPO (arXiv:2604.10918): Empirically routes gradients through component-specific tokens for LaTeX generation. Provides no theoretical characterization of why components differ in convergence dynamics or what makes component routing beneficial. Our analysis provides this foundation.\\n- ShapE-GRPO (arXiv:2603.29871, March 2026): Decomposes set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory, targeting multi-candidate collective optimization (recommendation, brainstorming). ShapE-GRPO operates at the *candidate level* (which output gets credit within a group), while CurriculumRLVR-IE operates at the *reward-component level* (which IE reward component has lower gradient variance). ShapE-GRPO provides no gradient variance analysis, no sequential skill ordering, and no IE application — the mechanisms and domains are distinct.\\n- arXiv:2605.02375 (May 2026): Proves binary rewards create fundamental optimization degeneracy in policy gradient methods (infinite maximizing distributions, diversity collapse). This independently motivates topology-aware reward design: the binary type-conjunction component's problems extend beyond elevated variance to structural optimization impossibility. The Signal Topology Analysis identifies the specific gradient variance mechanism; arXiv:2605.02375 proves the broader policy-level degeneracy — complementary theoretical characterizations.\\n- VCRL (arXiv:2509.19803): Uses between-sample reward variance for difficulty-based data selection. Orthogonal: between-sample vs. within-sample, data selection vs. reward topology.\\n\\nThe analysis fills a gap that is visible across all these papers: they demonstrate that reward decomposition helps (CSPO, RuCL), or analyze how decomposed objectives converge (arXiv:2604.19857), or show that mixed-difficulty produces relay (arXiv:2602.14872), or prove binary rewards are degenerate (arXiv:2605.02375) — but none explains the signal-structural mechanism that makes span detection specifically the curriculum foundation for IE, and none provides an empirically verifiable condition for when this mechanism is active.\\n\\n**Axis 2 (Algorithmic — analysis application)**: The convergence-gap adaptive weight scheme as an analysis corollary, not an independent contribution. The analysis predicts that variance inequality produces convergence ordering; the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) is the algorithmic enforcement of this ordering — it redistributes weight toward components whose measured gradient variance (σ_i) remains high relative to their convergence gap. This is NOT a novel adaptive weighting technique (SPARD/PAWA, MAESTRO, arXiv:2509.11452 precede it); it is an instantiation of the analysis-derived curriculum principle for the IE skill hierarchy. The formula's philosophy (convergence-gap weighting, not momentum weighting) follows directly from the analysis: the analysis identifies the gap to convergence — not the rate of progress — as the theoretically relevant quantity.\\n\\n**Axis 3 (Empirical — analysis falsifiability + φ-verification)**: Per-component F1 learning curves logged every 50 GRPO steps — for BOTH the adaptive-weight run and the fixed-weight Qwen3-8B baseline run — serve as the empirical test of the analysis's sequential convergence prediction. The fixed-weight curves are the clean empirical test for H1: if the span→type→argument ordering emerges under fixed weights (where the adaptive algorithm cannot enforce it), this confirms the topology theory independently of the algorithm. The adaptive-weight curves demonstrate algorithmic enforcement of the ordering (Algorithm Application evidence), not topology theory evidence. The analysis predicts span F1 converges before type-conditioned F1, which converges before argument F1 — a falsifiable ordering that no prior IE work has published. Deviation in the fixed-weight curves would falsify the topology hypothesis and require reanalysis. **φ-Verification Protocol (novel diagnostic contribution)**: Before any learning curve interpretation, the mandatory dry run fits a Beta distribution (ML estimation + KS goodness-of-fit test) to the empirical span-IoU values and computes φ̂ vs. the threshold φ*(p_s, p_t). If φ̂ > φ*, the analysis's variance ordering is confirmed as active for this experimental setting and the convergence prediction stands. If φ̂ < φ* (pathological bimodal span generation, atypical of early training), the paper reports this as a partial falsification requiring revised analysis. This protocol is itself a novel diagnostic contribution — the first published method for empirically verifying whether topology-induced curriculum conditions are satisfied in a specific GRPO-IE training run. No prior GRPO-IE work has measured or reported span-IoU distributional shape during training.\",\n  \"landscape\": \"**CSPO** (arXiv:2604.10918, ACL 2026) is the most important addition to related work. CSPO proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation: it decomposes the structured generation reward into structure, style, and content components, and routes backpropagation signals only through tokens relevant to each component. The paper frames the problem as 'reward ambiguity that conflates multiple behavioral aspects.' CSPO is the closest concurrent work in the space of component-specific reward decomposition with token-level gradient routing, and its ACL acceptance confirms the research direction is timely. Three differentiations from CurriculumRLVR-IE: (a) CSPO applies component routing to LaTeX rendering fidelity (structure/style/content are parallel rendering dimensions in a formal language, not sequentially ordered IE skills); IE has a fundamentally different decomposition structure where span detection is a prerequisite for type classification and argument assignment — CSPO's parallel component routing has no notion of which component must converge before others; (b) CSPO provides no theoretical characterization of WHY component routing helps, why components might have different convergence dynamics, or what property of the reward signal determines convergence ordering — the paper's motivation is 'reward ambiguity' (an empirical observation) rather than a formal analysis; the Signal Topology Analysis provides this explanation for IE rewards specifically; (c) CSPO uses static component-specific rewards without adaptive weighting — the analysis-derived convergence-gap formula is absent. CSPO's empirical result (component routing helps for structured generation) and our theoretical result (continuous reward topology reduces gradient variance and induces sequential convergence, conditional on φ-sufficiency) are complementary: CSPO shows the phenomenon exists; our analysis explains why and specifies when.\\n\\n**ShapE-GRPO** (arXiv:2603.29871, March 2026) proposes Shapley-Enhanced GRPO, decomposing set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory. The target applications are multi-candidate collective optimization scenarios (recommendation, brainstorming, code suggestion) where one strong candidate inflates rewards for all candidates in the group. ShapE-GRPO's decomposition operates at the *candidate level* — which output in a generated group deserves credit — while CurriculumRLVR-IE's decomposition operates at the *reward-component level* — which component of the span/type/argument multi-faceted IE reward has lower gradient variance in early training. ShapE-GRPO provides no gradient variance analysis, no sequential skill ordering theory, and no IE application; it does not address the continuous/binary topology distinction or adaptive curriculum weighting. The mechanisms are entirely distinct.\\n\\n**Binary Reward Degeneracy** (arXiv:2605.02375, May 2026) proves that binary rewards create fundamental optimization degeneracy for policy gradient methods: the set of distributions maximizing expected binary reward is infinite (no unique convergence target), and under KL regularization, decreasing β paradoxically drives the policy toward concentrated distributions (diversity collapse). This provides independent theoretical grounding for the Signal Topology Analysis's diagnosis that binary type-conjunction IE rewards are pathological. The degeneracy result and the Signal Topology Analysis are complementary: arXiv:2605.02375 proves the structural impossibility (binary rewards cannot uniquely identify a target policy), while our analysis identifies the specific gradient variance mechanism (Bernoulli near maximum variance regime in early training) and its IE-specific consequences (span→type→argument convergence ordering disruption). Together they provide two independent theoretical motivations for topology-aware IE reward design.\\n\\n**STEER** (arXiv:2604.04415, April 2026) introduces Pareto-Frontier guided Advantage Balancing (P-FAB) for multi-objective RL in video reasoning. P-FAB addresses conflicts between chain-of-thought length and task accuracy objectives by dynamically resolving reward conflicts and identifying balanced optimization directions along the Pareto frontier, framing the challenge as a multi-objective Pareto optimality problem. CurriculumRLVR-IE differs in mechanism and domain: STEER targets video reasoning with CoT-length vs. accuracy trade-offs navigated via Pareto frontier search; the Signal Topology Analysis addresses IE reward components whose distinct convergence dynamics stem from continuous vs. binary reward topology, providing a structural (gradient variance) explanation for why different IE reward components have different convergence dynamics — extending the motivation from empirical multi-objective conflict resolution to formal gradient variance characterization grounded in reward topology.\\n\\n**ToolRLA** (arXiv:2603.01620, March 2026) applies multiplicative correctness decomposition across four dimensions (format validity, tool selection, parameter accuracy, regulatory compliance) for tool-integrated agents in a three-stage SFT→GRPO→DPO pipeline. The paper explicitly frames its contribution as 'encoding domain priority orderings as inductive biases in the reward landscape,' and its multiplicative design yields 7 percentage points improvement over additive alternatives. Three differentiations from CurriculumRLVR-IE: (a) ToolRLA encodes priority orderings multiplicatively based on domain knowledge (an empirical design choice for tool invocation dimensions); the Signal Topology Analysis derives the span→type→argument priority ordering from first principles via gradient variance of continuous vs. binary reward topology, providing a formal rather than empirical basis for the ordering; (b) the mechanism differs — multiplicative decomposition vs. additive decomposition with topology-aware adaptive weights; (c) the domain differs — tool invocation agents vs. information extraction. ToolRLA establishes that priority-ordered reward decomposition benefits structured agent tasks; CurriculumRLVR-IE provides a theoretical grounding for why specific orderings arise from the mathematical structure of the reward signal.\\n\\n**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent GRPO-IE work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Critically, ProUIE's SFR uses atomic (span, type) as the atomic unit, conflating the continuous span-IoU signal with the binary type-classification signal — precisely the topology conflation that the Signal Topology Analysis identifies as the mechanism behind poor argument F1. CurriculumRLVR-IE differentiates from ProUIE on: (1) span-boundary F1 computed independently of type label, grounded in the analysis's gradient variance derivation; (2) convergence-gap adaptive weighting replacing fixed weights; (3) per-component learning curves for both adaptive and fixed-weight runs as falsifiable analysis evidence, distinguishing topology-induced ordering from algorithm-enforced ordering; (4) explicit φ-verification confirming the analysis's conditions are met.\\n\\n**SPARD** (arXiv:2604.07837, April 2026) proposes PAWA (Progress-Aware Weight Adaptation) for reward-component-level dynamic weighting in LLM alignment and RADR for data rebalancing. PAWA's exponential update w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i) fires when the LCB of mean reward improvement is positive (component making reliable progress). Three differentiations: (a) SPARD's PAWA is momentum-based (up-weights progress), risking perpetuating the dominance of whichever component improves first; the convergence-gap formula up-weights lagging components, which is analysis-motivated (the analysis identifies gap to convergence, not rate of progress, as the relevant quantity); (b) SPARD applies to open-ended LLM alignment without IE-specific structural decomposition or gradient-variance analysis; (c) SPARD provides no theoretical basis for why components have different variance profiles. The proposed adaptive scheme is an instantiation of the analysis's prediction, not a novel algorithm per se.\\n\\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with two-tier decomposed reward (foundational + advanced rubrics) for multimodal reasoning, with Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. The Signal Topology Analysis deepens RuCL's analysis: RuCL shows reliable signals reduce variance (empirically); our analysis derives WHY span-IoU is specifically reliable (continuous topology → bounded Beta variance, conditional on φ-sufficiency) while type-conjunction is specifically unreliable (binary topology → Bernoulli near maximum variance regime in early training). The analysis provides the mechanism that RuCL's analysis observes but does not derive.\\n\\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses advantage collapse — where summing rewards before group-wise normalization maps distinct reward combinations to identical normalized advantage values, destroying relative signal. GDPO normalizes each reward's advantage independently before aggregation. This is orthogonal to the proposed work: GDPO operates at the normalization step; the analysis-derived adaptive weights operate at the aggregation step. The two mechanisms can be combined: GDPO normalization applied to each span/type/argument advantage, then convergence-gap adaptive aggregation weights. This combination is a concrete future direction.\\n\\n**MAESTRO** (arXiv:2601.07208) and **arXiv:2509.11452** motivate the general class of adaptive reward weighting approaches. Neither applies to IE or provides the IE-specific signal topology analysis. APEX (arXiv:2601.06574) identifies 'variance hijacking' in multi-objective RL — conceptually aligned with what the Signal Topology Analysis formalizes for IE: the binary type-conjunction component has higher variance and would hijack gradients without topology-aware decomposition.\\n\\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally proves a relay regime for task-level difficulty ordering in L-step compositional reasoning (Theorem 5.2). The Signal Topology Analysis extends the relay concept from task level to reward-component level: within a single IE task type, the span/type/argument reward components form a difficulty ordering analogous to easy-to-hard task horizons, with span-IoU continuity providing the smooth gradient handoff. This is an extension in abstraction level, not a direct instantiation, and the paper explicitly distinguishes these two levels.\\n\\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857) proves a Reward Decomposition Theorem bounding the sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T). Complementary: they characterize the worst-case cost of decomposition; the Signal Topology Analysis identifies the structural IE-specific property (span-IoU continuity) that makes early-training variance reduction benefit dominate this bounded cost in practice.\\n\\n**VCRL** (arXiv:2509.19803) uses between-sample reward variance for difficulty-based data selection in math RLVR — explicitly distinct from the proposed within-sample reward-component variance analysis for skill ordering within IE task structure.\\n\\n**EGCA** (arXiv:2603.16158, ICLR 2026 Workshop) concentrates GRPO advantage signals on causal token spans for code generation, identifying earliest execution divergence from reference solutions. Distinct: EGCA requires executable code with test cases and reference execution traces; it is fundamentally inapplicable to IE. EGCA's credit assignment is causal (which tokens caused execution divergence); the Signal Topology Analysis's gradient variance analysis is structural (which reward components have lower variance by topology). Both address 'how should gradient credit be assigned,' but at different levels and with different mechanisms.\\n\\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation for the span-first ordering but do not analyze training dynamics or reward signal topology in RL.\\n\\n**REAR** (EMNLP 2025 Findings), **R1-RE** (arXiv:2507.04642), **R2GRPO** (arXiv:2505.22068), **EXTRACT-0** (arXiv:2509.22906): All GRPO-IE papers using atomic or fixed-weight composite rewards without signal topology analysis.\",\n  \"approach\": \"We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) on a span-boundary-decoupled reward with analysis-derived adaptive component weighting. The paper has one primary theoretical contribution (conditional on empirically verifiable premises) and two direct applications of that contribution.\\n\\n**Signal Topology Analysis — Proposition 1 (Conditional) (primary contribution)**:\\n\\nFor a GRPO policy π_θ trained with reward R = Σᵢ αᵢ Rᵢ where components {Rᵢ} have different topological properties, we derive:\\n\\n**Condition (φ-sufficiency, verifiable premise)**: The variance ordering Var(R_span) < Var(R_type) requires the empirical span-IoU distribution's Beta concentration parameter φ to satisfy φ > φ*(p_s, p_t) ≡ μ_s(1−μ_s)/(p_s·p_t·(1−p_s·p_t)) − 1. Derivation: substituting Var(R_span) = μ_s(1−μ_s)/(1+φ) and Var(R_type) = p_s·p_t·(1−p_s·p_t), the ordering inequality reduces directly to this condition. The natural early-training regime — where the model produces near-zero IoU for most span predictions (monotonically decreasing Beta, φ > 1) — structurally satisfies the condition when p_s < 0.5. A U-shaped Beta (φ < 1, bimodal span generation) would be atypical of early GRPO training and would reverse the ordering. The dry-run diagnostic measures φ̂ via ML Beta fitting and KS goodness-of-fit test before any learning curve interpretation is published or claimed.\\n\\n(a) *Variance ordering (conditional on φ-sufficiency)*: Var(R_span) < Var(R_type) < Var(R_arg) in early training when span detection probability p_s < 0.5 and φ > φ*(p_s, p_t). Specifically:\\n- R_span (span-IoU): continuous on [0,1], Beta-distributed; Var(R_span) = μ_s(1−μ_s)/(1+φ) for concentration parameter φ>0\\n- R_type (span+type conjunction): binary, Bernoulli(p_s·p_t); Var(R_type) = p_s·p_t·(1−p_s·p_t), maximized near p=0.5, which occurs in mid-training when p_s<0.7 and p_t<0.7 — specifically exceeds Var(R_span) throughout early and mid-training when φ > φ*. **Independence assumption**: This derivation assumes span correctness and type correctness are independent Bernoulli trials. In practice they are positively correlated (correct span detection raises the probability of correct type classification), so the actual conjunction probability q = P(span ∩ type correct) ≥ p_s·p_t, and the actual Var(R_type) = q(1−q). Since q remains below 0.5 in early training (the increasing regime of the Bernoulli variance function), positive correlation means the actual variance is HIGHER than the independence estimate — strengthening, not weakening, the ordering Var(R_span) < Var(R_type).\\n- R_arg (argument F1): conditional on both span and type correctness; compound Bernoulli variance dominates until both upstream components are high-accuracy\\n\\n(b) *Sequential convergence ordering*: Lower variance in R_span (when φ-sufficiency holds) produces a more stable GRPO gradient for span detection early in training. As p_s increases toward 0.7+, the type-conditioned component's effective Bernoulli probability p_t|span increases (simpler classification when span is correct), reducing Var(R_type) and enabling type convergence. Argument F1 receives stable signal only after both upstream variances decrease. The convergence ordering span → type → argument is a structural consequence of reward topology, not a manually scheduled curriculum — conditional on the φ-sufficiency premise being verified.\\n\\n(c) *Falsifiable prediction*: Per-component F1 learning curves must show span F1 converging before type-conditioned F1, which converges before argument F1 — provided φ̂ > φ* is confirmed by the dry-run diagnostic. This prediction is tested in the **fixed-weight Qwen3-8B baseline run** (not the adaptive-weight run): because the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) actively enforces the span→type→argument ordering, observing this ordering in adaptive-weight curves cannot cleanly confirm the topology theory. The fixed-weight curves, where no algorithmic enforcement is present, constitute the clean empirical test for H1.\\n\\n**Contingency (if φ̂ < φ*)**: If the dry-run measures a U-shaped span-IoU distribution (φ̂ < φ*, bimodal span generation behavior), the paper reports this as a partial falsification of the topology hypothesis, analyzes why the model produces bimodal span IoU in early training (likely: alternating between exact match and complete miss), and publishes the empirical learning curves without the ordering prediction. This contingency is declared in advance, not post-hoc, making the paper's claims fully falsifiable.\\n\\nPositioning relative to concurrent theory: The analysis is positioned as a reward-component-level extension of the task-level relay regime (arXiv:2602.14872), which proves sequential gradient handoff across task difficulty levels but does not analyze reward component topology within a single task type. The analysis also identifies the structural property (continuous vs. binary reward topology) that determines whether early-training variance reduction benefit dominates the sub-optimality cost characterized by arXiv:2604.19857's Reward Decomposition Theorem. CSPO (arXiv:2604.10918) demonstrates empirically that component routing helps for structured LaTeX generation without providing the theoretical characterization that our analysis supplies. ShapE-GRPO (arXiv:2603.29871) decomposes rewards at the candidate level via Shapley attribution, not at the reward-component topology level. arXiv:2605.02375 proves binary reward degeneracy at the policy distribution level, complementing our gradient variance analysis at the component topology level. STEER (arXiv:2604.04415) addresses multi-objective balance in video reasoning via Pareto-guided advantage balancing; the Signal Topology Analysis provides a structural gradient variance explanation for why IE reward components have different convergence dynamics, extending motivation from empirical conflict resolution to formal topology-grounded characterization. ToolRLA (arXiv:2603.01620) encodes priority orderings multiplicatively as domain inductive biases for tool agents; the Signal Topology Analysis derives the IE ordering from first principles via reward topology rather than domain-knowledge-based design.\\n\\n**Application 1 — Analysis-Derived Reward Decomposition (algorithmic)**:\\n\\nProposition 1 directly implies that IE rewards should separate span-IoU (continuous signal) from type-conjunction (binary signal) to exploit the variance ordering. This motivates the span-boundary-decoupled reward:\\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification) — the continuous component\\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration — the binary component, but now isolated from span so its variance does not corrupt the span component's stable signal\\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong — the compositional component\\n\\nThe convergence-gap adaptive weights follow from the analysis: w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), normalized so Σᵢ wᵢ(t)=1, with ε=0.05, θ=0.7. This formula up-weights components that are (a) lagging below the convergence target (gap-based, not momentum-based) and (b) have stable gradients (low σ_i) — exactly the analysis's prediction for which component is ready to receive increased learning pressure. In early training, span has lower σ_span and below-target F1, receiving high weight; once span F1 exceeds θ, weight redistributes to type; once type converges, to argument. The philosophy contrast with SPARD's PAWA (which up-weights components making reliable progress, i.e., momentum) follows directly from the analysis: the analysis identifies gap-to-convergence, not rate-of-progress, as the relevant quantity for curriculum enforcement.\\n\\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps. Plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, setting weight to ε regardless of whether F1_i has reached θ. Sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} from saved checkpoints.\\n\\n**Application 2 — Per-Component Learning Curve Diagnostics with φ-Verification (empirical)**:\\n\\nThe 50-example mandatory dry run performs two measurements: (a) actual token length distribution (existing protocol); (b) **φ-verification**: empirical span-IoU values are collected, a Beta distribution is fit via ML estimation (scipy.stats.beta.fit), a KS goodness-of-fit test is performed, and φ̂ is compared to the threshold φ*(p_s, p_t) computed from the observed early-training p_s and p_t estimates. If φ̂ > φ*, proceed to full training with the convergence ordering prediction active. If φ̂ < φ*, pause and report the condition failure before proceeding — the full training still runs but without the ordering prediction.\\n\\nPer-component F1 is logged every 50 GRPO steps for **both the adaptive-weight run and the fixed-weight Qwen3-8B baseline run**, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves for each. The fixed-weight curves constitute the clean empirical test of H1: if the span→type→argument ordering emerges under fixed weights (where the algorithm cannot enforce it), topology theory is supported independently of the adaptive algorithm. The adaptive-weight curves demonstrate algorithmic enforcement of the ordering (Algorithm Application evidence). Logging per-component F1 for the fixed-weight baseline requires no new GPU compute — it is a 3-curve logger added to the already-planned fixed-weight baseline run. The analysis predicts span F1 converges before type-conditioned F1, which converges before argument F1 — a falsifiable ordering provided φ̂ > φ*. This is the primary empirical contribution: not just 'our method achieves better numbers' but 'the fixed-weight learning curves confirm/falsify the Signal Topology Analysis's convergence prediction, and the adaptive-weight curves show algorithmic enforcement; the φ-verification protocol provides a reproducible method for determining whether topology-induced curriculum conditions are active.' The learning curves are also the first published per-component training dynamics for GRPO-IE, providing diagnostic value independent of the conditional proposition.\\n\\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER). Output format: code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures (a) actual token length distribution and (b) empirical span-IoU distribution for φ-verification before full training.\\n\\n**Baselines and scale confound (explicit)**:\\nThe scale difference between the proposed system (Qwen3-8B) and ProUIE (Qwen3-4B) is a confound in any direct ProUIE comparison: any performance advantage could reflect reward design OR the 4B→8B scale increase, and these cannot be disentangled from the ProUIE-4B comparison alone. The paper addresses this explicitly:\\n- **Primary baseline for reward design effect**: Fixed-weight decomposed GRPO with Qwen3-8B (α₁=0.4, α₂=0.3, α₃=0.3, same backbone, same training data) — isolates adaptive weighting contribution from scale\\n- **Primary baseline for decomposition effect**: Single-reward GRPO with Qwen3-8B (joint extraction F1 as the only reward) — isolates reward decomposition effect from scale\\n- **Scale-controlled decomposition ablation**: α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5) from checkpoint evaluation, same 8B backbone — directly tests whether span-boundary decoupling is the essential design choice\\n- **Cross-system reference (not primary for reward design effect)**: ProUIE published ACE2005 numbers (Qwen3-4B) — presented as a cross-system reference with explicit note that scale difference is a confound; any residual advantage beyond what the fixed-weight Qwen3-8B achieves is attributable to adaptive weighting, not scale\\n- **SFT upper bounds**: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\\n\\n**IE Track Empirical Bar (pre-committed)**: For EMNLP 2026 Findings IE track submission, the paper pre-commits to reporting a minimum ≥3 Argument F1 improvement on ACE2005 for adaptive-weight Qwen3-8B vs. fixed-weight Qwen3-8B. If this bar is not met, the paper is redirected to an RL theory track (ICLR/ICML) rather than claiming IE method significance.\\n\\nThe paper's H4 hypothesis is: 'Decomposed adaptive GRPO with Qwen3-8B achieves higher ACE2005 Argument F1 than fixed-weight decomposed GRPO with Qwen3-8B (H4a, ≥3 F1 points) and higher than single-reward GRPO with Qwen3-8B (H4b); whether this matches or exceeds ProUIE-4B is a cross-system data point, not the primary reward-design comparison.'\\n\\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\\n\\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS and WikiEvents fit in full-document inference. OOD results framed as zero-shot cross-distribution generalization from sentence-level training to document-level inference. Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements.\\n\\n**Key testable hypotheses**:\\nH1 (topology analysis): Per-component learning curves from the FIXED-weight Qwen3-8B baseline run show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics, predicted by Proposition 1 (conditional on φ̂ > φ* confirmed by dry-run diagnostic). H1 is confirmed if the span→type→argument ordering emerges in the fixed-weight run learning curves (conditional on φ̂ > φ*), providing evidence for topology-induced ordering independent of algorithmic enforcement. The adaptive-weight curves demonstrate Algorithm Application (enforcement of the ordering), not topology theory evidence.\\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute (same backbone) — isolates span-boundary decoupling contribution.\\nH3 (adaptive vs. fixed): Adaptive weight scheme produces ≥3 higher Argument F1 than fixed-weight decomposed GRPO (same backbone) — isolates adaptive weighting contribution, the primary same-scale baseline and IE track empirical bar.\\nH4 (OOD generalization): Analysis-predicted convergence ordering generalizes to OOD benchmarks (RAMS, WikiEvents, MAVEN) — tests whether topology-induced curriculum creates more robust span detectors than single-reward GRPO.\",\n  \"resource_estimate\": {\n    \"compute_note\": \"Single-run-primary design gated on 50-example dry run. Dry run now performs two measurements: (a) output token length distribution; (b) empirical span-IoU distribution for φ-verification (ML Beta fitting + KS test, negligible additional compute). Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). Per-component F1 logging every 50 steps is added to the fixed-weight baseline run as well (3-curve logger, negligible overhead, no new GPU compute required). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.\",\n    \"manual\": {\n      \"gpu_hours\": \"~130-160 H100-hours total: dry run (~2 H100-hours, including φ-verification measurement) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours) + fixed-weight Qwen3-8B ablation as primary same-scale comparison (~20-25 H100-hours, checkpoint evaluation not full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours). Total ≤165 H100-hours — within 200 H100-hour ceiling.\",\n      \"gpu_utilization\": \"Low (20-35%) — GPUs idle during analysis derivation, φ condition algebra, learning curve interpretation, reward verifier implementation, CSPO/ShapE-GRPO differentiation writing, and paper writing.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$325-660 (at $2.50-4/hr H100 cloud on-demand)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~130-165 H100-hours total (same single-run-primary design; agent queues dry run first including φ-verification; then main GRPO run; fixed-weight and other ablations from checkpoint eval)\",\n      \"gpu_utilization\": \"Moderate (55-70%) — agent runs main experiment queue; human approves after dry run φ-verification result (confirm φ̂ > φ* before committing ordering prediction) and after main GRPO run before committing ablation evals.\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150-350 (experiment orchestration, learning curve analysis, φ-verification computation, analysis validation, CSPO/ShapE-GRPO differentiation analysis, ~1500-3000 turns at $0.08-0.12/turn)\",\n      \"estimated_gpu_cost\": \"~$325-660\",\n      \"risk_note\": \"Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). φ-verification gate: if φ̂ < φ*, human decides whether to (a) proceed with empirical-only framing or (b) investigate and adjust span tokenization to encourage monotone Beta behavior. Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes. If Argument F1 improvement vs. fixed-weight Qwen3-8B < 3 points, redirect to RL theory track rather than EMNLP IE track.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~130-165 H100-hours total (dry run auto-queued first including φ-verification; main run launched if token length ≤700 and φ̂ > φ*; checkpoint evals for ablations auto-queued after main run completes)\",\n      \"gpu_utilization\": \"Near-zero idle (~80-90%) — agent queues dry run, measures token lengths and φ̂, adjusts epoch count if >700 tokens, confirms φ condition, launches main run, auto-logs per-component F1 learning curves every 50 steps for both adaptive-weight and fixed-weight runs, runs plateau detector and θ sensitivity from saved checkpoints.\",\n      \"timeline\": \"5-8 days with 4× H100 cluster\",\n      \"team\": \"0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger for both adaptive and fixed-weight runs, φ-verification script (scipy.stats.beta.fit + KS test + threshold comparison), schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)\",\n      \"claude_api_cost\": \"$175-400 (~2000-4500 turns)\",\n      \"estimated_gpu_cost\": \"~$325-660\",\n      \"speed_bottleneck\": \"Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging for both runs and φ-verification add minimal overhead.\",\n      \"risk_note\": \"Dry run mandatory first. φ-verification must confirm φ̂ > φ* before ordering prediction is published. Plateau detector monitors all three components. Component F1 divergence triggers auto-checkpoint and pause. θ sensitivity auto-evaluated from saved checkpoints after main run. If Argument F1 improvement vs. fixed-weight Qwen3-8B < 3 points, auto-flag for venue redirect to RL theory track.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 Main (ARR February 2027 cycle) — primary target for all modes. The Signal Topology Analysis (Conditional Proposition), properly developed with full gradient variance derivation including the φ condition in the appendix, with empirical learning-curve validation (per-component F1 for both adaptive and fixed-weight runs to distinguish topology-induced ordering from algorithm-enforced ordering) and φ-verification protocol, is a main-track contribution if the theoretical novelty claim holds up to review. The extended timeline allows (a) stronger empirical coverage, (b) optional GDPO+adaptive-weight combination experiment as future direction, (c) tighter theoretical integration with arXiv:2602.14872's relay regime and arXiv:2604.19857's decomposition theorem.\",\n    \"EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date). Feasibility only in auto-research mode (5-8 GPU days), leaving 7-10 days for writing with CSPO, ShapE-GRPO, arXiv:2605.02375, STEER, ToolRLA, and all other citations integrated. Even in auto mode, any single GPU failure or training divergence eliminates this window entirely — there is zero buffer. For manual mode (3-4 months) and human-in-loop mode (4-6 weeks), ACL 2027 is the de-facto primary target. EMNLP 2026 is a stretch goal in auto mode only, and requires Argument F1 improvement ≥3 points vs. fixed-weight Qwen3-8B (pre-committed IE track bar) to justify IE Findings submission over RL theory track.\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation (arXiv:2604.10918, ACL 2026) — component-specific reward decomposition with token-level gradient routing for table-to-LaTeX; decomposes into structure/style/content components; frames the problem as 'reward ambiguity'; provides empirical motivation for component routing without theoretical characterization of WHY different components have different convergence dynamics or what structural property of the reward determines ordering; no curriculum theory, no adaptive weighting, no sequential skill ordering prediction; parallel rendering dimensions (structure/style/content) vs. sequentially ordered IE skills (span → type → argument); the Signal Topology Analysis provides the theoretical foundation for CSPO's empirical observation\",\n    \"ShapE-GRPO: Shapley-Enhanced Group Relative Policy Optimization (arXiv:2603.29871, March 2026) — decomposes set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory for multi-candidate collective generation scenarios (recommendation, brainstorming, code suggestion); operates at candidate level (which output in a group gets credit) rather than reward-component level (which component has lower gradient variance); no gradient variance analysis, no sequential skill ordering theory, no IE application; distinct mechanism and application domain from CurriculumRLVR-IE; cited to position the space of GRPO reward decomposition approaches and distinguish candidate-level from component-level decomposition\",\n    \"Binary Reward Degeneracy in Policy Gradient Methods (arXiv:2605.02375, May 2026) — proves binary rewards create fundamental optimization degeneracy: infinite set of distributions maximizing expected binary reward (no unique convergence target) and diversity collapse under KL regularization (decreasing β drives policy toward concentrated distributions); independent theoretical support for why binary type-conjunction IE rewards are pathological; complementary to the Signal Topology Analysis which identifies the specific gradient variance mechanism; together provide two independent theoretical motivations for topology-aware IE reward design\",\n    \"STEER: Structured Event Evidence for Video Reasoning (arXiv:2604.04415, April 2026) — introduces Pareto-Frontier guided Advantage Balancing (P-FAB) for multi-objective RL in video reasoning, dynamically resolving reward conflicts between chain-of-thought length and task accuracy objectives along the Pareto frontier; frames the challenge as a multi-objective Pareto optimality problem; CurriculumRLVR-IE differs in mechanism (gradient variance topology analysis vs. Pareto-guided advantage balancing) and domain (IE vs. video reasoning); the Signal Topology Analysis provides a structural explanation (continuous vs. binary reward topology) for why different IE reward components have different convergence dynamics, extending the motivation from empirical multi-objective conflict resolution to formal gradient variance characterization\",\n    \"ToolRLA: Tool-Integrated Reinforcement Learning for Agents (arXiv:2603.01620, March 2026) — multiplicative correctness decomposition across four dimensions (format validity, tool selection, parameter accuracy, regulatory compliance) in a three-stage SFT→GRPO→DPO pipeline for tool-integrated agents; explicitly frames contribution as 'encoding domain priority orderings as inductive biases in the reward landscape'; multiplicative design yields 7 percentage points improvement over additive alternatives; differentiation from CurriculumRLVR-IE: ToolRLA encodes priority orderings multiplicatively based on domain knowledge (empirical design choice) for tool invocation dimensions; the Signal Topology Analysis derives the span→type→argument priority ordering from first principles via gradient variance of continuous vs. binary reward topology (formal rather than empirical basis); mechanism (multiplicative vs. additive with adaptive weights) and domain (tool agents vs. IE) are also distinct\",\n    \"ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose atomic span+type conjunction as the mechanism causing poor argument gradient; does not cover RAMS/WikiEvents/MAVEN; uses Qwen3-4B (scale difference from proposed Qwen3-8B is an acknowledged confound in any direct comparison)\",\n    \"SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility (arXiv:2604.07837, April 2026) — PAWA (momentum-based exponential up-weighting when LCB of reward improvement is positive) and RADR (data category rebalancing); applied to open-ended LLM alignment; no gradient-variance analysis; no span/type/argument decomposition; PAWA momentum philosophy vs. analysis-derived convergence-gap philosophy: the Signal Topology Analysis identifies gap-to-convergence as the relevant quantity, directly motivating the gap-based formula over SPARD's momentum formula\",\n    \"VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models (arXiv:2509.19803, September 2025) — between-sample variance for difficulty-based data selection in math RLVR; +4.67 points average on Qwen3-8B-Base; explicit distinction: VCRL uses between-sample variance for data selection; Signal Topology Analysis uses within-sample reward-component topology for skill ordering\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition — the Signal Topology Analysis deepens RuCL's analysis by proving WHY span-IoU is reliably low-variance (continuous topology, conditional on φ-sufficiency) while type-conjunction is reliably high-variance (Bernoulli at low-probability regime in early training), deriving the mechanism that RuCL observes but does not formalize\",\n    \"EGCA: Execution-Grounded Credit Assignment (arXiv:2603.16158, ICLR 2026 Workshop) — concentrates GRPO advantage on causal token spans via reference-execution comparison for code generation; requires executable code with test cases and reference execution traces; inapplicable to IE; credit assignment is causal (execution divergence) vs. structural (reward topology); cited to position the space of span-level credit assignment approaches and distinguish from IE-specific topology analysis\",\n    \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — prevents advantage collapse by normalizing each reward's advantage independently; orthogonal to analysis-derived adaptive weights (normalization-level vs. aggregation-level); combination of GDPO normalization + convergence-gap adaptive weights is a concrete future direction\",\n    \"MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization (arXiv:2601.07208, January 2026) — contextual bandit formulation for dynamic reward weights; bi-level optimization with Conductor network; more complex than analysis-derived simple formula; no IE application\",\n    \"On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for task-level difficulty ordering in L-step compositional reasoning (Theorem 5.2); Signal Topology Analysis extends relay concept from task level to reward-component level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness\",\n    \"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — Reward Decomposition Theorem bounding sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T); Signal Topology Analysis complements by identifying the structural IE-specific property (continuous span-IoU topology) that makes early-training variance reduction benefit dominate this bounded cost\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; motivation for adaptive component weights\",\n    \"APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking; conceptually aligned with analysis's prediction that binary type-conjunction component has higher variance and would dominate gradients without topology-aware decomposition\",\n    \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary SFT upper bound\",\n    \"Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that boundary detection is a prerequisite for entity typing: 36.73% F1 drop for long entities on ACE04 when boundary regression is removed; architectural motivation for the span-first convergence ordering that the analysis derives from gradient variance\",\n    \"T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence\",\n    \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)\",\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\",\n    \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)\",\n    \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings)\",\n    \"R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025)\",\n    \"Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025)\",\n    \"EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)\",\n    \"MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)\",\n    \"RAMS: Multi-Sentence Argument Linking (ACL 2020)\",\n    \"WikiEvents: Document-level Event Argument Extraction (NAACL 2021)\"\n  ],\n  \"description\": \"Joint NER+RE+EE GRPO training fails on event extraction because existing reward designs treat (span, type) pairs as atomic units, conflating a continuous signal (span-IoU) with a binary signal (type-conjunction) and eliminating the gradient variance ordering that would otherwise produce implicit curriculum. CurriculumRLVR-IE's primary contribution is the **Signal Topology Analysis (Conditional Proposition)**: a formal gradient variance derivation showing that in GRPO for IE, the topological property of each reward component — continuous (span-IoU, Beta-distributed), binary (type-conjunction, Bernoulli at low-probability regime in early training), or compositional (argument F1, compound Bernoulli variance) — determines its gradient variance in early training, which in turn determines convergence ordering (span → type → argument) without explicit scheduling. The Var(R_type) derivation assumes span and type correctness are independent Bernoulli trials; in practice they are positively correlated, but since positive correlation raises the actual conjunction probability q above p_s·p_t while q remains below 0.5 in early training, the actual variance is higher than the independence estimate — strengthening rather than weakening the ordering Var(R_span) < Var(R_type). The ordering holds conditional on the **φ-sufficiency premise**: the empirical span-IoU distribution's Beta concentration parameter φ must satisfy φ > φ*(p_s, p_t) ≡ μ_s(1−μ_s)/(p_s·p_t·(1−p_s·p_t)) − 1, verified during the mandatory dry run via ML Beta fitting and KS test. arXiv:2605.02375 independently proves binary rewards create fundamental optimization degeneracy (infinite maximizing distributions, diversity collapse), providing complementary theoretical support for topology-aware reward design. This extends the relay regime of arXiv:2602.14872 from task-level difficulty ordering to reward-component-level topology ordering within a single IE task type, and complements arXiv:2604.19857's Reward Decomposition Theorem by identifying the specific structural property (span-IoU continuity) that makes variance reduction benefit dominate the bounded sub-optimality cost. The **φ-verification protocol** — fitting a Beta distribution to dry-run span-IoU values and comparing φ̂ to the threshold before any ordering claim is published — is itself a novel diagnostic contribution: the first method for empirically verifying whether topology-induced curriculum conditions are active in a specific GRPO-IE training setting. Two algorithmic applications follow: (1) the span-boundary-decoupled reward design (span-IoU isolated from type-conjunction, each in its correct topological class); (2) the convergence-gap adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), gap-based rather than momentum-based (contrasting with SPARD's PAWA) because the analysis identifies gap-to-convergence, not rate-of-progress, as the relevant quantity. CSPO (arXiv:2604.10918, ACL 2026) demonstrates empirically that component routing helps for table-to-LaTeX without theoretical characterization; ShapE-GRPO (arXiv:2603.29871) decomposes at the candidate level via Shapley attribution rather than the component topology level; STEER (arXiv:2604.04415) addresses multi-objective balance in video reasoning via Pareto-guided advantage balancing — the Signal Topology Analysis provides a formal gradient variance explanation extending motivation from empirical conflict resolution to topology-grounded characterization; ToolRLA (arXiv:2603.01620) encodes priority orderings multiplicatively as domain inductive biases for tool agents, while the Signal Topology Analysis derives the IE ordering from first principles; EGCA (arXiv:2603.16158) does causal span credit assignment for code generation (requires reference execution, inapplicable to IE); GDPO (arXiv:2601.05242) prevents advantage collapse at the normalization level — orthogonal and combinable. The primary empirical test for H1 (topology analysis) is the **per-component F1 curves from the fixed-weight Qwen3-8B baseline run**: because the adaptive weight formula actively enforces the span→type→argument ordering, only the fixed-weight curves can cleanly confirm topology-induced ordering independent of algorithmic enforcement. Per-component F1 is logged every 50 GRPO steps for both adaptive and fixed-weight runs to distinguish topology-induced ordering from algorithm-enforced ordering — requiring no new GPU compute (a 3-curve logger added to the already-planned fixed-weight baseline). Pre-committed IE track empirical bar: ≥3 Argument F1 improvement on ACE2005 vs. fixed-weight Qwen3-8B; if not met, venue redirects to RL theory track. Primary foil: ProUIE (Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%); scale confound (8B vs. 4B) explicitly acknowledged, with fixed-weight Qwen3-8B ablation as the primary same-scale baseline. Backbone: Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run (including φ-verification) + one main GRPO run + checkpoint-derived ablations, ~130-165 H100-hours within 200 H100-hour ceiling. Primary target: ACL 2027 Main via February 2027 ARR (all modes); EMNLP 2026 Findings via May 25 ARR is auto-mode-only stretch goal with zero timeline margin and ≥3 F1 empirical bar required.\",\n  \"project_name\": \"joint_ie_decomposed_rlvr\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"HARD CONSTRAINT VIOLATION — Auto mode estimate of ~700h A100 converts to ~350-450h H100, which directly exceeds the user's ≤200h H100 total compute ceiling. Even manual mode (~300h A100 ≈ 150-200h H100) is already at the ceiling with zero margin for ablations. Light-R1 reports 3,328-5,376 A100-GPU-hours per single GRPO run on a 14B model; the Generator's estimates are underestimated by at least 2-5× for full fine-tuning.\", \"REAR MISCHARACTERIZATION — REAR (EMNLP 2025 Findings) is described as 'RL only to event argument extraction with a single joint reward,' but the paper's documented pipeline includes joint supervised warm-up AND joint reinforced optimization across both EAE and RE tasks. The novelty claim 'no work applies GRPO to the full NER+RE+EE joint task' needs to be more carefully scoped relative to REAR's actual multi-task RL coverage.\", \"10-MONTH TEMPORAL BLIND SPOT — The landscape section cites papers from May-July 2025, but the current date is May 2026. No search evidence was found for a concurrent paper doing exactly full joint NER+RE+EE with decomposed RLVR, but this is a 10-month gap in a field that moved from 'no RLVR for RE' to R1-RE+R2GRPO+REAR in under 6 months. The 'first' claim is fragile without an explicit concurrent-work audit for Aug 2025-May 2026.\", \"MISSING REQUIRED BENCHMARKS — The user specified MAVEN, WikiEvents, and RAMS as required evaluation datasets for event extraction. None appear in the proposed benchmark suite (ACE2005 + CoNLL + SciERC). MAVEN is large-scale general-domain event detection; WikiEvents and RAMS are argument extraction benchmarks that would directly test the event-argument component of the decomposed reward.\", \"REWARD WEIGHT UNDERSPECIFICATION — The three reward components (span-boundary F1, type-conditional F1, relation/triple F1) require explicit balancing coefficients. The Generator claims these 'auto-schedule via saturation' but provides no concrete mechanism, no sensitivity analysis, and no bounds on degenerate regimes (e.g., a model that maximizes span-F1 by outputting every token as a separate span). This is the primary technical risk and needs a principled solution (e.g., uncertainty weighting, learned coefficients, or constrained reward ranges).\", \"MODEL SIZE VS. CONSTRAINT MISMATCH — Qwen2.5-14B is the wrong model size for this constraint envelope. Qwen2.5-7B with LoRA-based GRPO is the only realistic configuration that can produce even a minimal experiment within 200 H100-hours. The 14B choice appears driven by competitive benchmarking goals rather than feasibility analysis.\"]\nFeedback: The core idea — decomposed RLVR rewards that give partial credit for span-correct/type-wrong predictions — is technically sound and partially novel. To get this to a passable state: (1) Scale down to Qwen2.5-7B and specify LoRA GRPO throughout; recompute all resource estimates with LoRA reduction factors and confirm the auto mode fits under 200 H100-hours. (2) Correct the REAR framing: acknowledge REAR does joint EAE+RE RL, and position the differentiation as (a) NER inclusion + (b) strictly decomposed per-substructure rewards vs. REAR's single joint RL reward. (3) Add MAVEN, WikiEvents, and RAMS to the benchmark suite — these are explicitly required by the target track and event extraction without them is incomplete. (4) Provide a concrete reward weighting scheme: either fixed normalized coefficients justified by pilot experiments, or a learned mixing network trained jointly with the policy. (5) Add a section explicitly addressing Aug 2025-May 2026 concurrent work risk — search arXiv for 'joint information extraction GRPO' from Q3-Q4 2025 before submitting, and pre-register the differentiators. This idea is 'revise, not fail' — the decomposed reward curriculum signal is a real contribution — but the resource constraint violation and REAR mischaracterization must be fixed before this can be argued as novel and feasible.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL CONCURRENT WORK MISSED — ProUIE (arXiv:2604.10633, April 12, 2026) covers joint NER+RE+EE with GRPO + Stepwise Fine-grained Reward (SFR) decomposed hierarchically by structural unit: NER (entity-type → entity-value), RE (relation-type → relation-instance → entity-pair), EE (event-type → trigger → role → argument). Evaluated on 36 public datasets including ACE2005. The Generator's explicit claim 'No published paper applies decomposed GRPO rewards to the full joint NER+RE+EE task as of May 2026 searches' is false. A reviewer who knows ProUIE will immediately reject the novelty claim as stated.\", \"NOVELTY REPOSITIONING REQUIRED — The only surviving technical differentiator from ProUIE is: span-boundary F1 computed *independent of type label* (proposed) vs. ProUIE's atomic type-entity pairs (ProUIE rewards entity-type and entity-value but does not reward span-correct/type-wrong predictions). This specific contribution must become the paper's primary framing; the current framing ('no prior work applies decomposed GRPO to NER+RE+EE') is no longer defensible.\", \"ProUIE's DOCUMENTED EE WEAKNESS IS AN OPPORTUNITY — ProUIE explicitly reports 'underperforming the strongest baseline for both triggers and arguments' on ACE2005 EE. The proposed work should be specifically framed as addressing this failure mode: if span-conditional rewards (rewarding trigger detection independently of argument role accuracy) fix ProUIE's EE weakness, that is a compelling and concrete result. The Generator should add a comparison directly against ProUIE's published EE numbers.\", \"OUTPUT LENGTH UNDERESTIMATE — The 100-300 token claim for IE JSON extractions is optimistic for complex multi-task joint extraction with chain-of-thought. ACE2005 sentences with multiple entities, relations, and event triggers (with CoT trace) realistically produce 300-600+ tokens per example. If true output length is 2-3× the assumed value, GRPO rollout costs scale proportionally and auto-mode (3 runs) may exceed 200 H100-hours. A 50-example dry run measuring actual output token length before full training is essential.\", \"OOD DOCUMENT-LEVEL EVALUATION RISK — The model is trained on sentence-level ACE2005 examples and evaluated on document-level RAMS (multi-sentence argument linking) and WikiEvents (document-level EAE). Without document-level context handling (e.g., sliding window, cross-sentence attention), the OOD evaluation may fail for reasons unrelated to reward decomposition, threatening the validity of the OOD generalization claim. The Generator should acknowledge this and describe how document-level inputs are handled at inference.\"]\nFeedback: Round 2 successfully addressed the resource constraint (7B+LoRA is now realistic), REAR framing (correctly described), missing benchmarks (MAVEN/RAMS/WikiEvents now included), and reward underspecification (fixed weights with pilot calibration). However, a critical gap opened: ProUIE (arXiv:2604.10633, April 2026) does joint NER+RE+EE with GRPO + fine-grained hierarchical rewards, directly occupying the 'first decomposed GRPO for joint IE' claim. You cannot submit without addressing this. Recommended revision path: (1) Acknowledge ProUIE in related work — frame the proposed work as explicitly extending ProUIE's limitation: ProUIE's SFR treats type-entity pairs as atomic, meaning a span-correct/type-wrong prediction receives near-zero reward. The proposed span-IoU-conditioned hierarchical reward explicitly credits partial correctness at the span level. (2) Make the EE comparison against ProUIE's published numbers the centerpiece empirical result — ProUIE underperforms baselines on ACE2005 EE; showing that span-conditional rewards fix this is a sharp, verifiable contribution. (3) Position MAVEN/RAMS/WikiEvents as the OOD evaluation that ProUIE does not cover. (4) Measure actual output token lengths on a 50-example ACE2005 pilot BEFORE committing to the 100-300 token estimate and the 200 H100-hour ceiling claim. (5) Add a one-paragraph discussion of how document-level inputs (RAMS, WikiEvents) are handled at inference given sentence-level ACE2005 training — sliding window with sentence-level extractions merged, or prompt includes full document context?\n\n### Round 3 review\nVerdict: revise\nIssues: [\"VENUE FACTUAL ERROR (critical): The 'EMNLP 2026 via August ARR cycle' path does not exist. ARR's own dates page confirms the August 3, 2026 ARR cycle commits to EACL 2027, not EMNLP 2026. The ONLY path to EMNLP 2026 is submission by May 25, 2026 (commitment deadline August 2). If May 25 is infeasible for the current experiments, the correct fallback is ACL 2027 (February 2027 ARR deadline), not 'EMNLP 2026 via August.' The target venue section must be corrected.\", \"COMPUTE CEILING STILL POTENTIALLY VIOLATED: The Generator estimates 80-200 H100-hours per GRPO run and commits to 2 runs (total: 160-400 H100-hours). The upper-bound scenario (400 H100-hours) is 2× the hard constraint of ≤200 H100-hours. The Generator says 'ceiling constrained to 2 GRPO runs to stay within 420 H100-hours' — but 420 >> 200. A concrete single-run-primary design is needed: one main GRPO run (90-120 H100-hours if dry run confirms ~350-token outputs), with the α₁=0 ablation derived from a fraction of rollouts at the final checkpoint, keeping total under 200 H100-hours.\", \"CASCADE FAILURE CLAIM OVERSTATED: ProUIE's paper does not explicitly state that wrong trigger type produces near-zero argument reward. Independent fetch of the paper confirms: 'The paper doesn't explicitly state that incorrect trigger types produce near-zero argument rewards, though the piecewise penalty suggests coarse errors receive priority.' The Generator should reframe this as an inference from SFR's piecewise structure rather than ProUIE's own diagnosis — otherwise a reviewer who reads ProUIE carefully will flag this as misrepresentation.\", \"CONTRIBUTION SCOPE NARROWNESS RISK: The paper's distinguishing technical contribution is a single reward design change (add α₁=0.4 span-boundary component independent of type label). Without stronger theoretical grounding — e.g., a formal proof or convergence analysis showing span-decoupled rewards induce a natural curriculum (span → type → argument) — reviewers may characterize this as an ablation of ProUIE's reward design rather than a standalone method. Consider adding a curriculum convergence analysis or learning curve comparison showing the predicted sequential skill acquisition.\", \"OOD DOCUMENT-LEVEL CONFOUND UNRESOLVED: The paper trains on sentence-level ACE2005 and evaluates on document-level RAMS/WikiEvents/MAVEN. The Generator acknowledges this as a 'confound noted explicitly' but this framing is insufficient — reviewers will ask why no document-level adaptation was attempted. Reframe OOD results as 'zero-shot cross-distribution generalization from sentence to document' and add a brief analysis of which document-level aspects hurt performance (e.g., coreference chains, multi-sentence arguments).\"]\nFeedback: The technical core is now well-specified and the ProUIE differentiation is valid. Three rounds of revision have addressed compute scale, REAR framing, missing benchmarks, and output-length underestimation. The remaining fixable issues are: (1) Correct the venue section immediately — the only path to EMNLP 2026 is the May 25 ARR submission (15 days away); if that is missed, the real next target is ACL 2027 via February 2027 ARR. Remove all references to 'EMNLP 2026 via August ARR cycle.' (2) Design a single-run budget that fits ≤200 H100-hours: commit the dry run (2 H100-hours) + one main GRPO run (target 90-120 H100-hours at ≤400 token output) + the α₁=0 ablation from checkpoint evaluation (not a full new run, ~20-30 H100-hours). Total: ~130-150 H100-hours — within the constraint. (3) Soften the cascade failure attribution from 'near-zero reward' (ProUIE's claimed mechanism) to 'near-zero reward implied by SFR's piecewise conditioning on matched trigger groups' (your inference). This distinction matters to reviewers who read ProUIE. (4) Strengthen the theoretical framing: if you can show analytically or empirically that span-decoupled rewards create a sequential skill curriculum (span convergence first, then type, then argument), this elevates the paper from 'ablation' to 'method contribution.' Learning curves for each reward component across training steps would directly support this claim at low additional compute cost.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"UNCITED COMPETITOR (HIGH PRIORITY): GDPO (arXiv:2601.05242, January 2026, ICML 2026) from NVIDIA proposes per-reward normalization in GRPO to prevent advantage collapse in multi-reward settings — applied to tool calling, math, and coding. GDPO is the normalization analog to the proposed adaptive weighting: GDPO normalizes each reward independently within the group before aggregation; the proposed method dynamically adjusts the aggregation weights based on convergence progress. A reviewer familiar with GDPO (now an ICML 2026 poster) will immediately flag its absence. The generator must cite GDPO and clearly distinguish: GDPO prevents per-reward advantage collapse at the normalization level; the proposed method enforces a curriculum by adjusting relative weights as each component converges — these are complementary and could be combined (GDPO normalization + proposed adaptive weights), which would itself strengthen the paper.\", \"UNCITED THEORETICAL PARALLEL (MEDIUM PRIORITY): 'The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards' (arXiv:2602.14872, February 2026) formally proves that RLVR exhibits implicit skill ordering emergence when the difficulty spectrum is smooth, using a relay regime analysis with convergence guarantees. The proposed paper's Contribution 1 (gradient variance analysis showing span→type→argument sequential convergence) is an instance of this broader phenomenon. Without citing this paper and positioning the IE-specific analysis as a domain instantiation of the relay regime framework, reviewers reading both papers will flag this as a missed citation. Importantly, the Implicit Curriculum paper provides stronger theoretical machinery — the generator should either explicitly build on it or clearly explain what the IE-specific variance analysis adds beyond the general framework.\", \"UNCITED THEORETICAL PARALLEL (MEDIUM PRIORITY): 'Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization' (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards, applied to LVLMs. The proposed Contribution 1 provides a gradient-variance-based analysis of a similar decomposition for IE — it must acknowledge arXiv:2604.19857, explain how its span-IoU continuous signal analysis extends or complements the formal sub-optimality bounds in that paper, and position the IE task structure (span IoU continuity vs. joint conjunction) as the distinctive aspect.\", \"ADAPTIVE WEIGHT θ HYPERPARAMETER RISK: The convergence target θ=0.7 is used as the reference point for the weight formula w_i(t) = max(ε, θ - F1_i(t)) / σ_i(t). If argument F1 never reaches 0.7 (InstructUIE achieves 72.94% at 11B; the proposed system targeting >60% suggests this is achievable but not guaranteed), the argument component will persistently receive high weight throughout training, potentially causing variance hijacking in late training — the exact phenomenon the scheme is meant to prevent. The generator should add: (a) a secondary convergence criterion (e.g., plateau detection when F1_i improves <1% over 200 steps), or (b) sensitivity analysis showing the method is robust to θ ∈ {0.6, 0.7, 0.8}.\", \"EMNLP MAIN vs FINDINGS REALISM: The paper targets EMNLP 2026 Main but the three contributions individually are incremental extensions of ProUIE (reward decomposition), APEX/2509.11452 (adaptive weighting), and RuCL (gradient variance theory). The learning curve diagnostic is genuinely novel for IE but is a contribution supporting the method, not the method itself. The realistic target is EMNLP 2026 Findings — the generator should explicitly acknowledge this in the target venue section to set accurate expectations for the auto-mode agent.\"]\nFeedback: The core technical nucleus is now well-executed: span-boundary-decoupled GRPO reward for IE is a real gap, the single-run compute design fits within 200 H100-hours, and the cascade failure attribution is properly softened. Round 4 has resolved all four Round 3 issues. However, three concurrent papers published since Round 3 that are directly relevant to the claimed contributions are missing from the related work: (1) GDPO (ICML 2026) for multi-reward GRPO normalization, (2) 'The Implicit Curriculum' (Feb 2026) for RLVR skill ordering theory, and (3) arXiv:2604.19857 (April 2026) for composite-reward GRPO convergence theory. These omissions, if noticed by a reviewer, will be read as lack of thoroughness. Recommended actions for Round 5: (a) Add GDPO to related work — 1 paragraph distinguishing per-reward normalization (GDPO) from convergence-progress adaptive weighting (proposed), note they are complementary, suggest combining GDPO normalization + proposed weights as a future direction. (b) Add 'The Implicit Curriculum' — 1 paragraph framing the IE span→type→argument gradient variance analysis as a domain instantiation of the relay regime framework, with the span-IoU continuity as what makes the IE difficulty spectrum smooth in the relevant sense. (c) Add arXiv:2604.19857 — 1 paragraph noting its Reward Decomposition Theorem for LVLMs and explaining how the proposed early-training gradient variance analysis complements it by identifying span continuity as the specific structural property that makes IE reward decomposition beneficial. (d) Add θ sensitivity analysis or secondary convergence criterion for the adaptive weight formula. These are additive changes to related work and the method section — no experimental changes required. The EMNLP 2026 Findings track is the appropriate target given the contribution scope.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"UNCITED DIRECT COMPETITOR — SPARD (arXiv:2604.07837, April 2026) is not cited and directly threatens Contribution 2's novelty. SPARD's PAWA (Progress-Aware Weight Adaptation) adjusts reward-component weights dynamically based on training progress using a confidence-bound adjusted exponential scheme: w_{t+1}^{r,i} = w_{t}^{r,i}·exp(η·Q_t^i). This operates at the reward-component level — NOT the data-sample level. Any reviewer who knows SPARD will immediately flag its absence. The paper must cite SPARD, accurately distinguish the proposed w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) from SPARD's LCB-based exponential growth formula, and narrow the novelty claim from 'first adaptive reward weighting for GRPO' to 'first adaptive weighting applied to the span/type/argument IE decomposition with formal gradient-variance justification for why the convergence ordering matters.'\", \"INCORRECT DIFFERENTIATION FROM SPARD — The most natural defensive move for the generator ('SPARD is data-level curriculum, ours is reward-component level') is factually wrong: SPARD has BOTH reward-component level weighting (PAWA) AND data-category level rebalancing (RADR). The paper must instead differentiate on: (a) formula design — variance-normalized lagging (proposed) vs. confidence-bound exponential growth (SPARD); (b) IE-specific structural decomposition (span-IoU continuity vs. type conjunction is not present in SPARD); (c) formal gradient-variance justification linking span-IoU continuity to early-training variance reduction, which SPARD does not provide.\", \"UNCITED COMPETITOR (MEDIUM) — VCRL (arXiv:2509.19803, September 2025) uses variance of rollout group rewards to estimate sample difficulty and drive curriculum selection for RLVR on math. Since CurriculumRLVR-IE's theoretical narrative explicitly centers on reward-variance reduction, a reviewer will expect VCRL to be cited and the distinction made clear (VCRL: between-sample variance for difficulty; proposed: within-sample reward-component variance for skill ordering).\", \"CONTRIBUTION 2 NOVELTY WEAKENED — With SPARD (PAWA) covering reward-component adaptive weighting and arXiv:2509.11452 + APEX already cited for motivation, Contribution 2's standalone novelty is now thin. The generator should reframe Contribution 2 as the application and instantiation of adaptive weighting for the specific IE skill hierarchy, not as a novel adaptive weighting technique per se. The genuine novelty is the combination of span-decoupled reward (Contribution 1's design) with convergence-aware weighting derived from the gradient variance analysis, not the weighting formula in isolation.\", \"EMNLP 2026 FINDINGS FEASIBILITY — The May 25 ARR deadline is 15 days away. The auto-research timeline (5-8 days for GPU work) is possible but writing a submission-quality paper in the remaining time after experiments is unrealistic. The generator correctly lists this as 'auto and HIL modes' for EMNLP 2026 and 'manual mode' for ACL 2027, but should be explicit that even for auto mode, producing an EMNLP-quality paper by May 25 requires the full 16 days with no setbacks — the dry-run gate (Day 1-2), main training (Days 3-7), analysis (Days 8-10), and writing (Days 11-15) leave zero margin for iteration.\"]\nFeedback: Round 5 has correctly addressed all four Round 4 issues: GDPO is distinguished, arXiv:2602.14872 and arXiv:2604.19857 are positioned, θ sensitivity + plateau detector are specified, and EMNLP Findings (not Main) is the target. The core technical nucleus — span-boundary IoU reward decoupled from type label, inducing a span→type→argument gradient relay in GRPO training — remains the paper's strongest and most defensible claim. However, a new concurrent paper has emerged that must be addressed before submission: (1) Add SPARD (arXiv:2604.07837) to related work — 1 paragraph describing PAWA's exponential confidence-bound weighting at the reward-component level, then distinguishing the proposed scheme by: (a) variance-normalized lagging formula vs. SPARD's LCB exponential growth, (b) IE-specific span/type/argument decomposition not present in SPARD, and (c) the formal gradient-variance analysis linking span-IoU continuity to sequential convergence — a structural argument SPARD does not make. Do NOT use the 'data-level vs. reward-component level' distinction because it is factually wrong. (2) Add VCRL (arXiv:2509.19803) with 1 sentence: between-sample variance for difficulty curriculum vs. within-sample reward-component variance for skill ordering. (3) Reframe Contribution 2's novelty: the contribution is the application of adaptive weighting to the span/type/argument structure with the gradient-variance analysis as motivation, not the adaptive weighting scheme as a standalone novel technique. These are all additive related-work and framing changes — no experimental changes required. The span-boundary decoupling remains genuinely novel for GRPO-based IE.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"UNCITED ACL 2026 CONCURRENT WORK — CSPO (arXiv:2604.10918, April 2026, accepted ACL 2026) proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation, explicitly framing the problem as 'reward ambiguity' in structured generation and assigning component-specific rewards backpropagated only through relevant tokens. The surface framing is identical to CurriculumRLVR-IE's 'reward atomicity' problem. A reviewer who knows CSPO will immediately flag its absence. The Generator must add CSPO to related work with 1 paragraph distinguishing: (a) span-boundary F1 independent of type label vs. CSPO's structure/style/content decomposition for LaTeX tokens, (b) gradient variance curriculum analysis and adaptive weighting are completely absent from CSPO, (c) CSPO has no sequential skill ordering — it assigns static component-specific rewards without dynamic adaptation.\", \"COMPOUND NOVELTY ATTRITION — By Round 6, the Generator has needed to reframe Contribution 1 as an extension of RuCL/relay regime, reframe Contribution 2 as an 'application/instantiation' after SPARD, and now must add CSPO as yet another partially overlapping prior work for structured-generation reward decomposition. Each addition is individually manageable, but the cumulative effect is that any single contribution, when correctly positioned, reads as incremental. An EMNLP reviewer reading the related work section with SPARD, GDPO, CSPO, RuCL, arXiv:2602.14872, and arXiv:2604.19857 all cited as partial precedents may characterize the paper as 'applying existing techniques to IE' rather than a methodological contribution. The paper needs a single sharpest claim — the gradient variance curriculum analysis for span-IoU continuity vs. type-conjunction probability is the strongest differentiator; the abstract and intro should lead with this, not bury it under the other contributions.\", \"EMPIRICAL RESULT RISK NOT ADEQUATELY SCOPED — The claim 'closes a material fraction of the 20-point ProUIE argument F1 gap' (H4, target >60%) is vague. If Qwen3-8B with the proposed reward reaches 58-62% Argument F1 vs. ProUIE's 52.58% (Qwen3-4B), a reviewer will ask: is the improvement from reward design or from the 4B→8B scale increase? The paper has no same-scale (8B) ProUIE comparison. The Generator should flag this confound more explicitly in the experimental design and add the fixed-weight Qwen3-8B ablation (baseline (c)) as the primary comparison for reward design effect, not the scale-mismatched ProUIE 4B numbers.\", \"EMNLP FINDINGS TIMELINE ZERO-MARGIN — With May 25 ARR deadline confirmed (15 days from today), even auto-research mode (5-8 GPU days) leaves 7-10 days for writing and CSPO/other citation additions. The Generator should explicitly acknowledge in the feasibility note that any single GPU or training failure eliminates the EMNLP 2026 window entirely, making ACL 2027 via February 2027 ARR the de-facto primary target for any non-auto mode.\"]\nFeedback: Round 6 has correctly addressed all Round 5 issues: SPARD is accurately described and differentiated by formula philosophy (momentum vs. convergence-gap), VCRL is cited with the correct between-sample vs. within-sample variance distinction, Contribution 2 is properly reframed as application/instantiation, and EMNLP Findings is the acknowledged realistic target. The technical nucleus remains sound. The single new action required: (1) Add CSPO (arXiv:2604.10918, ACL 2026) to related work — 1 paragraph: CSPO decomposes structured generation rewards by functional component (structure/style/content) for table-to-LaTeX and argues for component-specific backpropagation to resolve 'reward ambiguity'; distinguish by (a) span-boundary F1 independent of type label is a more precise decoupling than CSPO's LaTeX-component boundaries, (b) curriculum theory and adaptive weighting are entirely absent from CSPO, (c) CSPO targets document rendering fidelity not IE structured prediction. Beyond CSPO, two sharpening suggestions that would elevate novelty score above 3/5 without new experiments: (a) Restructure the abstract/intro to lead with the gradient variance curriculum claim as the paper's primary theoretical contribution, citing it as a reward-component-level relay regime (extending arXiv:2602.14872) specifically for IE — this is the strongest differentiator from all prior work; (b) Add an explicit acknowledgment in Section 5 that the scale difference (8B proposed vs. 4B ProUIE) is a confound in the primary ProUIE comparison and that the fixed-weight Qwen3-8B ablation (not ProUIE 4B) is the clean baseline for reward design effect. These changes require only writing revisions — no new experiments.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"THEOREM RIGOR FLAW (HIGH PRIORITY — NEW in Round 7): The Signal Topology Theorem's variance ordering Var(R_span) < Var(R_type) requires the Beta concentration parameter φ of the span-IoU distribution to satisfy φ > [μ(1-μ) / (p_s·p_t·(1-p_s·p_t)) - 1]. This is an empirical condition on the shape of the early-training span-IoU distribution — NOT a consequence of reward design choices alone. The paper claims the ordering holds 'regardless of hyperparameter choices, as long as p_s < 0.5,' but this only addresses the reward weighting hyperparameters α. If a model produces dispersed span-IoU values (low φ, U-shaped Beta, which occurs when the model sometimes partially overlaps gold spans randomly), Var(R_span) can exceed Var(R_type) and the theorem's ordering reverses. For a paper whose primary novelty is 'Theorem 1,' calling this a theorem without explicitly stating and verifying the φ condition will be caught by any theory-oriented reviewer. Fix: (a) derive the explicit condition on φ required for the ordering (takes 1 paragraph of algebra), then empirically verify it from the dry run's span-IoU distribution logs; or (b) reframe as 'Signal Topology Analysis' / 'Theoretical Framework' rather than 'Theorem 1,' with the distributional assumptions stated as explicit premises. The latter framing is more honest and still publishable at an IE track.\", \"UNCITED CONCURRENT WORK — ShapE-GRPO (MEDIUM): arXiv:2603.29871 (March 2026) proposes Shapley-Enhanced GRPO (ShapE-GRPO), which decomposes set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory. While it does not address IE or the continuous/binary topology distinction, it is a concurrent GRPO reward decomposition approach that operates at the component/candidate level. A reviewer familiar with ShapE-GRPO may flag its absence. Add 1 sentence to related work: ShapE-GRPO decomposes multi-candidate rewards via Shapley attribution rather than topological classification; it does not address sequential skill ordering or provide a gradient variance analysis for structured IE prediction.\", \"UNCITED BACKGROUND — Binary Rewards Fundamental Challenges (MEDIUM): arXiv:2605.02375 (May 2026) proves that binary rewards create fundamental degeneracy in policy gradient methods (infinite maximizing distributions, diversity collapse), providing theoretical background for the type-conjunction challenge. The paper's framing of 'type-conjunction as binary Bernoulli → gradient issues' would be strengthened by citing this as independent theoretical motivation. Add 1 sentence noting that the degeneracy of binary rewards in policy gradient is independently established by arXiv:2605.02375, consistent with the proposed topology analysis.\", \"EMNLP 2026 IE TRACK FIT RISK (MEDIUM): The paper's primary novelty is now framed as a theoretical result (Signal Topology Theorem) — an RL theory contribution. The Information Extraction track at EMNLP expects method contributions validated by strong IE benchmark improvements. If Argument F1 on ACE2005 with Qwen3-8B (proposed) vs. fixed-weight Qwen3-8B (baseline) shows <3% improvement, reviewers will question whether the theorem has practical significance regardless of its theoretical interest. The paper should pre-commit to a 'meaningful improvement' threshold (e.g., ≥3 F1 points on Argument F1 vs. fixed-weight same-scale baseline) as the empirical bar that justifies IE track submission; if that bar is not met, the paper belongs in an RL theory track rather than IE Findings.\"]\nFeedback: Round 7 has correctly integrated all Round 6 issues: CSPO is now prominently differentiated at multiple paper levels (core problem, landscape, approach), the theorem-derived adaptive weight philosophy vs. SPARD momentum is clearly articulated, and the scale confound is explicitly managed with fixed-weight Qwen3-8B as the primary same-scale baseline. The paper's theoretical nucleus — the Signal Topology Theorem — is the strongest differentiator from all prior work. One new actionable issue dominates this round: the theorem's mathematical conditions are underspecified. The variance ordering Var(R_span) < Var(R_type) depends on the Beta concentration parameter φ of the empirical span-IoU distribution in early training, not just on p_s < 0.5. This is fixable with one paragraph of algebra and one dry-run measurement. Specifically: (1) Derive the condition φ > [μ(1-μ)/(p_s·p_t·(1-p_s·p_t)) - 1] explicitly and state it as a premise of Theorem 1; (2) add a dry-run diagnostic that logs the empirical span-IoU distribution and fits a Beta distribution to it (KS test, χ² test), using the estimated φ to verify the condition is met before claiming the theorem's validity for this specific run. This converts the 'theorem' from a claim that requires blind trust into a falsifiable prediction that the dry run either confirms or refutes — strengthening both the theory and the empirical contribution simultaneously. Two minor citations needed: ShapE-GRPO (arXiv:2603.29871) and the binary rewards degeneracy paper (arXiv:2605.02375). These require only 1-2 sentences each. The primary EMNLP 2026 Findings timeline pressure is acknowledged and auto-mode-only; ACL 2027 remains the realistic primary target for all other modes. If the theorem's φ condition can be verified empirically and the Argument F1 improvement over same-scale fixed-weight baseline meets ≥3 F1 points, the paper's theory + method + falsifiability triad is a genuine EMNLP 2026 Findings contribution in IE.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"LEARNING CURVE CONFOUND IN H1 TEST (NEW, MEDIUM PRIORITY): H1 predicts 'span F1 converges before type-conditioned F1, which converges before argument F1.' However, the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) ACTIVELY ENFORCES this ordering by redirecting weight toward lagging components—meaning the observed convergence ordering in the adaptive-weight run may be mechanistically produced by the weighting scheme rather than emerging naturally from reward topology. This conflates the algorithmic enforcement (Axis 2) with the theoretical prediction (Axis 1), making H1 unverifiable from adaptive-weight learning curves alone. Fix: log per-component F1 every 50 steps for the FIXED-weight Qwen3-8B baseline run as well. If the span→type→argument ordering still emerges under fixed weights, that is clean evidence for the topology theory; if not, H1 should be reported as unconfirmed and only the φ-verification and variance algebra are claimed as theoretical support. This requires no additional GPU compute—just adding a 3-curve logger to the already-planned fixed-weight baseline run.\", \"STEER (arXiv:2604.04415, April 2026) NOT CITED (MEDIUM PRIORITY): 'STEER: Structured Event Evidence for Video Reasoning via Multi-Objective Reinforcement Learning' explicitly identifies that 'standard GRPO computes a scalar advantage via fixed-weight summation, collapsing all objectives into a single score, making it unable to distinguish which objectives are under-satisfied'—which is directly parallel to the paper's core motivation. A reviewer familiar with STEER will notice its absence. One sentence in related work suffices: STEER identifies the fixed-weight GRPO collapse problem for video-reasoning multi-objective RL; the Signal Topology Analysis extends this to IE by identifying the topological property (continuous vs. binary reward) that determines which component is under-satisfied in early training.\", \"ToolRLA (arXiv:2603.01620, March 2026) NOT CITED (LOW PRIORITY): ToolRLA uses multiplicative reward decomposition for tool-integrated agents and explicitly frames its contribution as 'encoding domain priority orderings as inductive biases in the reward landscape'—a framing conceptually parallel to the proposed span→type→argument priority ordering. The domain (tool agents) and mechanism (multiplicative, not additive; three-stage SFT→GRPO→DPO pipeline) are distinct enough that one sentence in related work suffices: ToolRLA encodes priority orderings multiplicatively for tool invocation quality dimensions; the Signal Topology Analysis derives the continuous/binary topological property as the mechanism for priority ordering in IE, distinct from empirical domain knowledge.\", \"INDEPENDENCE ASSUMPTION IN Var(R_type) NOT EXPLICITLY STATED (LOW PRIORITY): The derivation Var(R_type) = p_s·p_t·(1−p_s·p_t) assumes that span correctness and type correctness are independent Bernoulli trials. In practice they are positively correlated (correctly detecting the span raises the probability of correct type), meaning P(span ∩ type correct) ≥ p_s·p_t. Note: under positive correlation the actual variance q(1−q) where q > p_s·p_t is HIGHER than the independence estimate (when q < 0.5, still in the increasing regime), which actually strengthens the ordering Var(R_span) < Var(R_type). This should be stated as an explicit modeling assumption with a 1-sentence note that positive correlation makes the ordering stronger, not weaker.\"]\nFeedback: Round 8 status: The paper is close to submission-ready. All critical issues from Rounds 1–7 have been properly addressed. The three new issues to resolve are additive writing changes requiring no new experiments:\n\n(1) MOST IMPORTANT — Fix the H1 empirical test confound by logging per-component F1 curves for the fixed-weight Qwen3-8B baseline run. The learning curves under adaptive weighting cannot cleanly confirm the topology theory because the adaptive weighting mechanistically enforces the ordering. The fixed-weight baseline curves provide the clean theory test: if the ordering also emerges there, the Signal Topology Analysis is empirically supported independently of the algorithm. This is a logging change to the already-planned fixed-weight run, zero additional GPU cost.\n\n(2) Cite STEER (arXiv:2604.04415, April 2026) — one sentence noting its identification of the GRPO fixed-weight collapse problem for video multi-objective RL and distinguishing the IE topology mechanism. Absence will be noticed by reviewers covering multi-objective GRPO.\n\n(3) Cite ToolRLA (arXiv:2603.01620) and state the independence assumption for Var(R_type) — each requires 1 sentence.\n\nBeyond these, two writing-level improvements would elevate the paper: (a) The abstract and introduction should state the learning-curve confound resolution proactively — 'we report per-component curves for BOTH adaptive and fixed-weight runs to distinguish topology-induced ordering from algorithm-enforced ordering.' This shows methodological sophistication. (b) Add one sentence noting that positive correlation between span and type detection (p_s and p_t) in practice strengthens rather than weakens the variance ordering, addressing a foreseeable reviewer objection to the independence assumption.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:42:24.229Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:42:24.229Z",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-10T09:42:24.262Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.

Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.

Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.

Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.

Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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
  "title": "CurriculumRLVR-IE: Reward Signal Topology Theory for Implicit Sequential Skill Curriculum in GRPO Information Extraction",
  "core_problem": "The fundamental question in GRPO-based information extraction (IE) is not merely 'how should rewards be decomposed?' but 'why does reward decomposition produce curriculum effects — and for which structural properties of the reward signal?' No published work has answered this question formally. The IE reward literature (ProUIE, R1-RE, R2GRPO, EXTRACT-0) treats reward design as empirical engineering; no paper analyzes the mathematical properties of reward components that determine convergence ordering in policy gradient training.\n\nThe central claim of this paper is a **Signal Topology Analysis** for GRPO-IE: the topological property of a reward component — specifically whether it is **continuous** (takes values in [0,1], like span-IoU), **binary** (takes values in {0,1}, like span+type conjunction), or **compositional** (conditioned on multiple binary components, like argument F1) — determines its gradient variance in early GRPO training, and therefore determines convergence ordering without explicit curriculum scheduling. This is a structural claim, not an empirical one.\n\nFormally: for a GRPO policy with per-rollout reward R = Σᵢ αᵢ Rᵢ, the gradient variance contribution of component i scales as αᵢ² · Var(Rᵢ). For span-IoU (continuous, Beta-distributed), Var(R_span) is bounded by the variance of a symmetric Beta. For span+type conjunction (binary, Bernoulli with p = p_s · p_t), Var(R_type) = p_s·p_t·(1−p_s·p_t), which exceeds Var(R_span) in early training when p_s, p_t < 0.5 because the conjunction probability product p_s·p_t < p_s drives the Bernoulli toward its maximum variance regime. The variance inequality Var(R_span) < Var(R_type) < Var(R_arg) is a structural consequence of reward topology. **Condition (φ-sufficiency)**: This ordering holds if and only if the span-IoU empirical distribution satisfies the Beta concentration parameter φ > φ*(p_s, p_t) ≡ μ_s(1−μ_s)/(p_s·p_t·(1−p_s·p_t)) − 1. This is an empirically verifiable condition: a U-shaped (bimodal) span-IoU distribution (φ < 1) would indicate pathological span generation behavior and reverse the ordering. Under the natural early-training regime where the model produces near-zero IoU for most spans (monotonically decreasing Beta, φ > 1), the condition is structurally satisfied. Verification: the dry run fits an ML-estimated Beta to span-IoU values and performs a KS test; if φ̂ > φ*, the analysis's ordering is confirmed for this run. arXiv:2605.02375 independently establishes that binary rewards create degeneracy (infinite maximizing distributions, diversity collapse) in policy gradient methods, providing independent theoretical support for why binary type-conjunction rewards are problematic.\n\nThe consequence is an implicit curriculum that is an **analysis prediction (conditional on φ-sufficiency)**, not an empirically discovered phenomenon: (1) the span component provides lower-variance gradient signal in early training, causing span detection to converge first; (2) as p_s increases (span accuracy improves), p_t | (span correct) rises (type classification is a simpler Bernoulli conditioned on correct localization), reducing Var(R_type) and enabling type convergence; (3) argument F1 receives cleaner signal only after both span and type have stabilized, because its compound conditional variance is dominated by the upstream binary variance terms. The span→type→argument sequential convergence is predicted by the analysis before any experiment runs — and falsifiable by the per-component F1 learning curves.\n\nWhy the analysis matters for IE: Current GRPO-IE methods (ProUIE, arXiv:2604.10633) use atomic (span, type) rewards, treating span+type conjunction as the fundamental unit. This eliminates span-IoU's continuous signal, forcing the model to learn from a Bernoulli with p = p_s·p_t — the lowest-probability joint event, maximizing gradient variance. ProUIE reports ACE2005 Argument F1=52.58% vs. InstructUIE's 72.94% (a 20-point gap) and calls for 'more appropriate reward design,' but does not identify why its SFR structure creates the gap. The Signal Topology Analysis provides this identification: atomic rewards destroy the variance ordering that produces implicit curriculum, causing type and argument learning to plateau while span detection catches up through noisy, high-variance gradient updates.\n\nCSPO (arXiv:2604.10918, ACL 2026) shows empirically that component-specific token-level gradient routing helps for table-to-LaTeX generation (structure/style/content decomposition), using the framing of 'reward ambiguity.' CSPO provides no theoretical explanation of WHY different components have different convergence dynamics, what structural property of the reward determines the ordering, or whether static component routing is sufficient or whether adaptive weighting is needed. The Signal Topology Analysis provides the theoretical foundation for CSPO's empirical observation — and, crucially, predicts when static routing is insufficient (when the variance ordering creates a hierarchy that fixed weights cannot enforce) and motivates the convergence-gap adaptive weighting as an analysis-derived algorithm rather than an empirical heuristic.",
  "opportunity": "The Signal Topology Analysis creates three opportunity axes, hierarchically ordered: one theoretical (the conditional proposition itself), one algorithmic (its direct application), and one empirical (its falsifiable prediction plus the φ-verification protocol).\n\n**Axis 1 (Theoretical — primary novelty and paper identity)**: The Signal Topology Analysis (Conditional Proposition) for GRPO-IE. No published work has formally characterized the relationship between reward component topology (continuous/binary/compositional) and gradient variance ordering in GRPO for structured prediction. The closest work:\n- RuCL (arXiv:2602.21628): Shows two-tier rubric curriculum via reward decomposition (Appendix B gradient variance analysis) for multimodal reasoning, but analyzes easy/hard rubric difficulty ordering, NOT the continuous/binary topological distinction as the mechanism. RuCL's variance reduction comes from reliable vs. unreliable rubrics — our analysis shows the deeper structural reason: reliable signals are reliable because they are continuous, not because they are 'easy.'\n- arXiv:2602.14872 (relay regime): Proves implicit curriculum at task-level difficulty ordering. Our analysis extends the relay concept from task level to reward-component level: within a single IE task, span-IoU continuity provides the 'smooth gradient handoff' that prevents plateau, analogous to how smooth difficulty spectrum prevents grokking at task level.\n- arXiv:2604.19857 (Reward Decomposition Theorem): Bounds sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T). Complementary but different question: they ask 'how much do we lose by decomposing?' and bound the cost; we ask 'why does the span component help MORE than theory predicts?' and answer: because continuous topology reduces early-training variance, making the benefit dominate the bounded cost.\n- CSPO (arXiv:2604.10918): Empirically routes gradients through component-specific tokens for LaTeX generation. Provides no theoretical characterization of why components differ in convergence dynamics or what makes component routing beneficial. Our analysis provides this foundation.\n- ShapE-GRPO (arXiv:2603.29871, March 2026): Decomposes set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory, targeting multi-candidate collective optimization (recommendation, brainstorming). ShapE-GRPO operates at the *candidate level* (which output gets credit within a group), while CurriculumRLVR-IE operates at the *reward-component level* (which IE reward component has lower gradient variance). ShapE-GRPO provides no gradient variance analysis, no sequential skill ordering, and no IE application — the mechanisms and domains are distinct.\n- arXiv:2605.02375 (May 2026): Proves binary rewards create fundamental optimization degeneracy in policy gradient methods (infinite maximizing distributions, diversity collapse). This independently motivates topology-aware reward design: the binary type-conjunction component's problems extend beyond elevated variance to structural optimization impossibility. The Signal Topology Analysis identifies the specific gradient variance mechanism; arXiv:2605.02375 proves the broader policy-level degeneracy — complementary theoretical characterizations.\n- VCRL (arXiv:2509.19803): Uses between-sample reward variance for difficulty-based data selection. Orthogonal: between-sample vs. within-sample, data selection vs. reward topology.\n\nThe analysis fills a gap that is visible across all these papers: they demonstrate that reward decomposition helps (CSPO, RuCL), or analyze how decomposed objectives converge (arXiv:2604.19857), or show that mixed-difficulty produces relay (arXiv:2602.14872), or prove binary rewards are degenerate (arXiv:2605.02375) — but none explains the signal-structural mechanism that makes span detection specifically the curriculum foundation for IE, and none provides an empirically verifiable condition for when this mechanism is active.\n\n**Axis 2 (Algorithmic — analysis application)**: The convergence-gap adaptive weight scheme as an analysis corollary, not an independent contribution. The analysis predicts that variance inequality produces convergence ordering; the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) is the algorithmic enforcement of this ordering — it redistributes weight toward components whose measured gradient variance (σ_i) remains high relative to their convergence gap. This is NOT a novel adaptive weighting technique (SPARD/PAWA, MAESTRO, arXiv:2509.11452 precede it); it is an instantiation of the analysis-derived curriculum principle for the IE skill hierarchy. The formula's philosophy (convergence-gap weighting, not momentum weighting) follows directly from the analysis: the analysis identifies the gap to convergence — not the rate of progress — as the theoretically relevant quantity.\n\n**Axis 3 (Empirical — analysis falsifiability + φ-verification)**: Per-component F1 learning curves logged every 50 GRPO steps — for BOTH the adaptive-weight run and the fixed-weight Qwen3-8B baseline run — serve as the empirical test of the analysis's sequential convergence prediction. The fixed-weight curves are the clean empirical test for H1: if the span→type→argument ordering emerges under fixed weights (where the adaptive algorithm cannot enforce it), this confirms the topology theory independently of the algorithm. The adaptive-weight curves demonstrate algorithmic enforcement of the ordering (Algorithm Application evidence), not topology theory evidence. The analysis predicts span F1 converges before type-conditioned F1, which converges before argument F1 — a falsifiable ordering that no prior IE work has published. Deviation in the fixed-weight curves would falsify the topology hypothesis and require reanalysis. **φ-Verification Protocol (novel diagnostic contribution)**: Before any learning curve interpretation, the mandatory dry run fits a Beta distribution (ML estimation + KS goodness-of-fit test) to the empirical span-IoU values and computes φ̂ vs. the threshold φ*(p_s, p_t). If φ̂ > φ*, the analysis's variance ordering is confirmed as active for this experimental setting and the convergence prediction stands. If φ̂ < φ* (pathological bimodal span generation, atypical of early training), the paper reports this as a partial falsification requiring revised analysis. This protocol is itself a novel diagnostic contribution — the first published method for empirically verifying whether topology-induced curriculum conditions are satisfied in a specific GRPO-IE training run. No prior GRPO-IE work has measured or reported span-IoU distributional shape during training.",
  "landscape": "**CSPO** (arXiv:2604.10918, ACL 2026) is the most important addition to related work. CSPO proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation: it decomposes the structured generation reward into structure, style, and content components, and routes backpropagation signals only through tokens relevant to each component. The paper frames the problem as 'reward ambiguity that conflates multiple behavioral aspects.' CSPO is the closest concurrent work in the space of component-specific reward decomposition with token-level gradient routing, and its ACL acceptance confirms the research direction is timely. Three differentiations from CurriculumRLVR-IE: (a) CSPO applies component routing to LaTeX rendering fidelity (structure/style/content are parallel rendering dimensions in a formal language, not sequentially ordered IE skills); IE has a fundamentally different decomposition structure where span detection is a prerequisite for type classification and argument assignment — CSPO's parallel component routing has no notion of which component must converge before others; (b) CSPO provides no theoretical characterization of WHY component routing helps, why components might have different convergence dynamics, or what property of the reward signal determines convergence ordering — the paper's motivation is 'reward ambiguity' (an empirical observation) rather than a formal analysis; the Signal Topology Analysis provides this explanation for IE rewards specifically; (c) CSPO uses static component-specific rewards without adaptive weighting — the analysis-derived convergence-gap formula is absent. CSPO's empirical result (component routing helps for structured generation) and our theoretical result (continuous reward topology reduces gradient variance and induces sequential convergence, conditional on φ-sufficiency) are complementary: CSPO shows the phenomenon exists; our analysis explains why and specifies when.\n\n**ShapE-GRPO** (arXiv:2603.29871, March 2026) proposes Shapley-Enhanced GRPO, decomposing set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory. The target applications are multi-candidate collective optimization scenarios (recommendation, brainstorming, code suggestion) where one strong candidate inflates rewards for all candidates in the group. ShapE-GRPO's decomposition operates at the *candidate level* — which output in a generated group deserves credit — while CurriculumRLVR-IE's decomposition operates at the *reward-component level* — which component of the span/type/argument multi-faceted IE reward has lower gradient variance in early training. ShapE-GRPO provides no gradient variance analysis, no sequential skill ordering theory, and no IE application; it does not address the continuous/binary topology distinction or adaptive curriculum weighting. The mechanisms are entirely distinct.\n\n**Binary Reward Degeneracy** (arXiv:2605.02375, May 2026) proves that binary rewards create fundamental optimization degeneracy for policy gradient methods: the set of distributions maximizing expected binary reward is infinite (no unique convergence target), and under KL regularization, decreasing β paradoxically drives the policy toward concentrated distributions (diversity collapse). This provides independent theoretical grounding for the Signal Topology Analysis's diagnosis that binary type-conjunction IE rewards are pathological. The degeneracy result and the Signal Topology Analysis are complementary: arXiv:2605.02375 proves the structural impossibility (binary rewards cannot uniquely identify a target policy), while our analysis identifies the specific gradient variance mechanism (Bernoulli near maximum variance regime in early training) and its IE-specific consequences (span→type→argument convergence ordering disruption). Together they provide two independent theoretical motivations for topology-aware IE reward design.\n\n**STEER** (arXiv:2604.04415, April 2026) introduces Pareto-Frontier guided Advantage Balancing (P-FAB) for multi-objective RL in video reasoning. P-FAB addresses conflicts between chain-of-thought length and task accuracy objectives by dynamically resolving reward conflicts and identifying balanced optimization directions along the Pareto frontier, framing the challenge as a multi-objective Pareto optimality problem. CurriculumRLVR-IE differs in mechanism and domain: STEER targets video reasoning with CoT-length vs. accuracy trade-offs navigated via Pareto frontier search; the Signal Topology Analysis addresses IE reward components whose distinct convergence dynamics stem from continuous vs. binary reward topology, providing a structural (gradient variance) explanation for why different IE reward components have different convergence dynamics — extending the motivation from empirical multi-objective conflict resolution to formal gradient variance characterization grounded in reward topology.\n\n**ToolRLA** (arXiv:2603.01620, March 2026) applies multiplicative correctness decomposition across four dimensions (format validity, tool selection, parameter accuracy, regulatory compliance) for tool-integrated agents in a three-stage SFT→GRPO→DPO pipeline. The paper explicitly frames its contribution as 'encoding domain priority orderings as inductive biases in the reward landscape,' and its multiplicative design yields 7 percentage points improvement over additive alternatives. Three differentiations from CurriculumRLVR-IE: (a) ToolRLA encodes priority orderings multiplicatively based on domain knowledge (an empirical design choice for tool invocation dimensions); the Signal Topology Analysis derives the span→type→argument priority ordering from first principles via gradient variance of continuous vs. binary reward topology, providing a formal rather than empirical basis for the ordering; (b) the mechanism differs — multiplicative decomposition vs. additive decomposition with topology-aware adaptive weights; (c) the domain differs — tool invocation agents vs. information extraction. ToolRLA establishes that priority-ordered reward decomposition benefits structured agent tasks; CurriculumRLVR-IE provides a theoretical grounding for why specific orderings arise from the mathematical structure of the reward signal.\n\n**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent GRPO-IE work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Critically, ProUIE's SFR uses atomic (span, type) as the atomic unit, conflating the continuous span-IoU signal with the binary type-classification signal — precisely the topology conflation that the Signal Topology Analysis identifies as the mechanism behind poor argument F1. CurriculumRLVR-IE differentiates from ProUIE on: (1) span-boundary F1 computed independently of type label, grounded in the analysis's gradient variance derivation; (2) convergence-gap adaptive weighting replacing fixed weights; (3) per-component learning curves for both adaptive and fixed-weight runs as falsifiable analysis evidence, distinguishing topology-induced ordering from algorithm-enforced ordering; (4) explicit φ-verification confirming the analysis's conditions are met.\n\n**SPARD** (arXiv:2604.07837, April 2026) proposes PAWA (Progress-Aware Weight Adaptation) for reward-component-level dynamic weighting in LLM alignment and RADR for data rebalancing. PAWA's exponential update w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i) fires when the LCB of mean reward improvement is positive (component making reliable progress). Three differentiations: (a) SPARD's PAWA is momentum-based (up-weights progress), risking perpetuating the dominance of whichever component improves first; the convergence-gap formula up-weights lagging components, which is analysis-motivated (the analysis identifies gap to convergence, not rate of progress, as the relevant quantity); (b) SPARD applies to open-ended LLM alignment without IE-specific structural decomposition or gradient-variance analysis; (c) SPARD provides no theoretical basis for why components have different variance profiles. The proposed adaptive scheme is an instantiation of the analysis's prediction, not a novel algorithm per se.\n\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with two-tier decomposed reward (foundational + advanced rubrics) for multimodal reasoning, with Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. The Signal Topology Analysis deepens RuCL's analysis: RuCL shows reliable signals reduce variance (empirically); our analysis derives WHY span-IoU is specifically reliable (continuous topology → bounded Beta variance, conditional on φ-sufficiency) while type-conjunction is specifically unreliable (binary topology → Bernoulli near maximum variance regime in early training). The analysis provides the mechanism that RuCL's analysis observes but does not derive.\n\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses advantage collapse — where summing rewards before group-wise normalization maps distinct reward combinations to identical normalized advantage values, destroying relative signal. GDPO normalizes each reward's advantage independently before aggregation. This is orthogonal to the proposed work: GDPO operates at the normalization step; the analysis-derived adaptive weights operate at the aggregation step. The two mechanisms can be combined: GDPO normalization applied to each span/type/argument advantage, then convergence-gap adaptive aggregation weights. This combination is a concrete future direction.\n\n**MAESTRO** (arXiv:2601.07208) and **arXiv:2509.11452** motivate the general class of adaptive reward weighting approaches. Neither applies to IE or provides the IE-specific signal topology analysis. APEX (arXiv:2601.06574) identifies 'variance hijacking' in multi-objective RL — conceptually aligned with what the Signal Topology Analysis formalizes for IE: the binary type-conjunction component has higher variance and would hijack gradients without topology-aware decomposition.\n\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally proves a relay regime for task-level difficulty ordering in L-step compositional reasoning (Theorem 5.2). The Signal Topology Analysis extends the relay concept from task level to reward-component level: within a single IE task type, the span/type/argument reward components form a difficulty ordering analogous to easy-to-hard task horizons, with span-IoU continuity providing the smooth gradient handoff. This is an extension in abstraction level, not a direct instantiation, and the paper explicitly distinguishes these two levels.\n\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857) proves a Reward Decomposition Theorem bounding the sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T). Complementary: they characterize the worst-case cost of decomposition; the Signal Topology Analysis identifies the structural IE-specific property (span-IoU continuity) that makes early-training variance reduction benefit dominate this bounded cost in practice.\n\n**VCRL** (arXiv:2509.19803) uses between-sample reward variance for difficulty-based data selection in math RLVR — explicitly distinct from the proposed within-sample reward-component variance analysis for skill ordering within IE task structure.\n\n**EGCA** (arXiv:2603.16158, ICLR 2026 Workshop) concentrates GRPO advantage signals on causal token spans for code generation, identifying earliest execution divergence from reference solutions. Distinct: EGCA requires executable code with test cases and reference execution traces; it is fundamentally inapplicable to IE. EGCA's credit assignment is causal (which tokens caused execution divergence); the Signal Topology Analysis's gradient variance analysis is structural (which reward components have lower variance by topology). Both address 'how should gradient credit be assigned,' but at different levels and with different mechanisms.\n\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation for the span-first ordering but do not analyze training dynamics or reward signal topology in RL.\n\n**REAR** (EMNLP 2025 Findings), **R1-RE** (arXiv:2507.04642), **R2GRPO** (arXiv:2505.22068), **EXTRACT-0** (arXiv:2509.22906): All GRPO-IE papers using atomic or fixed-weight composite rewards without signal topology analysis.",
  "approach": "We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) on a span-boundary-decoupled reward with analysis-derived adaptive component weighting. The paper has one primary theoretical contribution (conditional on empirically verifiable premises) and two direct applications of that contribution.\n\n**Signal Topology Analysis — Proposition 1 (Conditional) (primary contribution)**:\n\nFor a GRPO policy π_θ trained with reward R = Σᵢ αᵢ Rᵢ where components {Rᵢ} have different topological properties, we derive:\n\n**Condition (φ-sufficiency, verifiable premise)**: The variance ordering Var(R_span) < Var(R_type) requires the empirical span-IoU distribution's Beta concentration parameter φ to satisfy φ > φ*(p_s, p_t) ≡ μ_s(1−μ_s)/(p_s·p_t·(1−p_s·p_t)) − 1. Derivation: substituting Var(R_span) = μ_s(1−μ_s)/(1+φ) and Var(R_type) = p_s·p_t·(1−p_s·p_t), the ordering inequality reduces directly to this condition. The natural early-training regime — where the model produces near-zero IoU for most span predictions (monotonically decreasing Beta, φ > 1) — structurally satisfies the condition when p_s < 0.5. A U-shaped Beta (φ < 1, bimodal span generation) would be atypical of early GRPO training and would reverse the ordering. The dry-run diagnostic measures φ̂ via ML Beta fitting and KS goodness-of-fit test before any learning curve interpretation is published or claimed.\n\n(a) *Variance ordering (conditional on φ-sufficiency)*: Var(R_span) < Var(R_type) < Var(R_arg) in early training when span detection probability p_s < 0.5 and φ > φ*(p_s, p_t). Specifically:\n- R_span (span-IoU): continuous on [0,1], Beta-distributed; Var(R_span) = μ_s(1−μ_s)/(1+φ) for concentration parameter φ>0\n- R_type (span+type conjunction): binary, Bernoulli(p_s·p_t); Var(R_type) = p_s·p_t·(1−p_s·p_t), maximized near p=0.5, which occurs in mid-training when p_s<0.7 and p_t<0.7 — specifically exceeds Var(R_span) throughout early and mid-training when φ > φ*. **Independence assumption**: This derivation assumes span correctness and type correctness are independent Bernoulli trials. In practice they are positively correlated (correct span detection raises the probability of correct type classification), so the actual conjunction probability q = P(span ∩ type correct) ≥ p_s·p_t, and the actual Var(R_type) = q(1−q). Since q remains below 0.5 in early training (the increasing regime of the Bernoulli variance function), positive correlation means the actual variance is HIGHER than the independence estimate — strengthening, not weakening, the ordering Var(R_span) < Var(R_type).\n- R_arg (argument F1): conditional on both span and type correctness; compound Bernoulli variance dominates until both upstream components are high-accuracy\n\n(b) *Sequential convergence ordering*: Lower variance in R_span (when φ-sufficiency holds) produces a more stable GRPO gradient for span detection early in training. As p_s increases toward 0.7+, the type-conditioned component's effective Bernoulli probability p_t|span increases (simpler classification when span is correct), reducing Var(R_type) and enabling type convergence. Argument F1 receives stable signal only after both upstream variances decrease. The convergence ordering span → type → argument is a structural consequence of reward topology, not a manually scheduled curriculum — conditional on the φ-sufficiency premise being verified.\n\n(c) *Falsifiable prediction*: Per-component F1 learning curves must show span F1 converging before type-conditioned F1, which converges before argument F1 — provided φ̂ > φ* is confirmed by the dry-run diagnostic. This prediction is tested in the **fixed-weight Qwen3-8B baseline run** (not the adaptive-weight run): because the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) actively enforces the span→type→argument ordering, observing this ordering in adaptive-weight curves cannot cleanly confirm the topology theory. The fixed-weight curves, where no algorithmic enforcement is present, constitute the clean empirical test for H1.\n\n**Contingency (if φ̂ < φ*)**: If the dry-run measures a U-shaped span-IoU distribution (φ̂ < φ*, bimodal span generation behavior), the paper reports this as a partial falsification of the topology hypothesis, analyzes why the model produces bimodal span IoU in early training (likely: alternating between exact match and complete miss), and publishes the empirical learning curves without the ordering prediction. This contingency is declared in advance, not post-hoc, making the paper's claims fully falsifiable.\n\nPositioning relative to concurrent theory: The analysis is positioned as a reward-component-level extension of the task-level relay regime (arXiv:2602.14872), which proves sequential gradient handoff across task difficulty levels but does not analyze reward component topology within a single task type. The analysis also identifies the structural property (continuous vs. binary reward topology) that determines whether early-training variance reduction benefit dominates the sub-optimality cost characterized by arXiv:2604.19857's Reward Decomposition Theorem. CSPO (arXiv:2604.10918) demonstrates empirically that component routing helps for structured LaTeX generation without providing the theoretical characterization that our analysis supplies. ShapE-GRPO (arXiv:2603.29871) decomposes rewards at the candidate level via Shapley attribution, not at the reward-component topology level. arXiv:2605.02375 proves binary reward degeneracy at the policy distribution level, complementing our gradient variance analysis at the component topology level. STEER (arXiv:2604.04415) addresses multi-objective balance in video reasoning via Pareto-guided advantage balancing; the Signal Topology Analysis provides a structural gradient variance explanation for why IE reward components have different convergence dynamics, extending motivation from empirical conflict resolution to formal topology-grounded characterization. ToolRLA (arXiv:2603.01620) encodes priority orderings multiplicatively as domain inductive biases for tool agents; the Signal Topology Analysis derives the IE ordering from first principles via reward topology rather than domain-knowledge-based design.\n\n**Application 1 — Analysis-Derived Reward Decomposition (algorithmic)**:\n\nProposition 1 directly implies that IE rewards should separate span-IoU (continuous signal) from type-conjunction (binary signal) to exploit the variance ordering. This motivates the span-boundary-decoupled reward:\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification) — the continuous component\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration — the binary component, but now isolated from span so its variance does not corrupt the span component's stable signal\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong — the compositional component\n\nThe convergence-gap adaptive weights follow from the analysis: w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), normalized so Σᵢ wᵢ(t)=1, with ε=0.05, θ=0.7. This formula up-weights components that are (a) lagging below the convergence target (gap-based, not momentum-based) and (b) have stable gradients (low σ_i) — exactly the analysis's prediction for which component is ready to receive increased learning pressure. In early training, span has lower σ_span and below-target F1, receiving high weight; once span F1 exceeds θ, weight redistributes to type; once type converges, to argument. The philosophy contrast with SPARD's PAWA (which up-weights components making reliable progress, i.e., momentum) follows directly from the analysis: the analysis identifies gap-to-convergence, not rate-of-progress, as the relevant quantity for curriculum enforcement.\n\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps. Plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, setting weight to ε regardless of whether F1_i has reached θ. Sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} from saved checkpoints.\n\n**Application 2 — Per-Component Learning Curve Diagnostics with φ-Verification (empirical)**:\n\nThe 50-example mandatory dry run performs two measurements: (a) actual token length distribution (existing protocol); (b) **φ-verification**: empirical span-IoU values are collected, a Beta distribution is fit via ML estimation (scipy.stats.beta.fit), a KS goodness-of-fit test is performed, and φ̂ is compared to the threshold φ*(p_s, p_t) computed from the observed early-training p_s and p_t estimates. If φ̂ > φ*, proceed to full training with the convergence ordering prediction active. If φ̂ < φ*, pause and report the condition failure before proceeding — the full training still runs but without the ordering prediction.\n\nPer-component F1 is logged every 50 GRPO steps for **both the adaptive-weight run and the fixed-weight Qwen3-8B baseline run**, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves for each. The fixed-weight curves constitute the clean empirical test of H1: if the span→type→argument ordering emerges under fixed weights (where the algorithm cannot enforce it), topology theory is supported independently of the adaptive algorithm. The adaptive-weight curves demonstrate algorithmic enforcement of the ordering (Algorithm Application evidence). Logging per-component F1 for the fixed-weight baseline requires no new GPU compute — it is a 3-curve logger added to the already-planned fixed-weight baseline run. The analysis predicts span F1 converges before type-conditioned F1, which converges before argument F1 — a falsifiable ordering provided φ̂ > φ*. This is the primary empirical contribution: not just 'our method achieves better numbers' but 'the fixed-weight learning curves confirm/falsify the Signal Topology Analysis's convergence prediction, and the adaptive-weight curves show algorithmic enforcement; the φ-verification protocol provides a reproducible method for determining whether topology-induced curriculum conditions are active.' The learning curves are also the first published per-component training dynamics for GRPO-IE, providing diagnostic value independent of the conditional proposition.\n\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER). Output format: code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures (a) actual token length distribution and (b) empirical span-IoU distribution for φ-verification before full training.\n\n**Baselines and scale confound (explicit)**:\nThe scale difference between the proposed system (Qwen3-8B) and ProUIE (Qwen3-4B) is a confound in any direct ProUIE comparison: any performance advantage could reflect reward design OR the 4B→8B scale increase, and these cannot be disentangled from the ProUIE-4B comparison alone. The paper addresses this explicitly:\n- **Primary baseline for reward design effect**: Fixed-weight decomposed GRPO with Qwen3-8B (α₁=0.4, α₂=0.3, α₃=0.3, same backbone, same training data) — isolates adaptive weighting contribution from scale\n- **Primary baseline for decomposition effect**: Single-reward GRPO with Qwen3-8B (joint extraction F1 as the only reward) — isolates reward decomposition effect from scale\n- **Scale-controlled decomposition ablation**: α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5) from checkpoint evaluation, same 8B backbone — directly tests whether span-boundary decoupling is the essential design choice\n- **Cross-system reference (not primary for reward design effect)**: ProUIE published ACE2005 numbers (Qwen3-4B) — presented as a cross-system reference with explicit note that scale difference is a confound; any residual advantage beyond what the fixed-weight Qwen3-8B achieves is attributable to adaptive weighting, not scale\n- **SFT upper bounds**: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\n\n**IE Track Empirical Bar (pre-committed)**: For EMNLP 2026 Findings IE track submission, the paper pre-commits to reporting a minimum ≥3 Argument F1 improvement on ACE2005 for adaptive-weight Qwen3-8B vs. fixed-weight Qwen3-8B. If this bar is not met, the paper is redirected to an RL theory track (ICLR/ICML) rather than claiming IE method significance.\n\nThe paper's H4 hypothesis is: 'Decomposed adaptive GRPO with Qwen3-8B achieves higher ACE2005 Argument F1 than fixed-weight decomposed GRPO with Qwen3-8B (H4a, ≥3 F1 points) and higher than single-reward GRPO with Qwen3-8B (H4b); whether this matches or exceeds ProUIE-4B is a cross-system data point, not the primary reward-design comparison.'\n\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\n\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS and WikiEvents fit in full-document inference. OOD results framed as zero-shot cross-distribution generalization from sentence-level training to document-level inference. Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements.\n\n**Key testable hypotheses**:\nH1 (topology analysis): Per-component learning curves from the FIXED-weight Qwen3-8B baseline run show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics, predicted by Proposition 1 (conditional on φ̂ > φ* confirmed by dry-run diagnostic). H1 is confirmed if the span→type→argument ordering emerges in the fixed-weight run learning curves (conditional on φ̂ > φ*), providing evidence for topology-induced ordering independent of algorithmic enforcement. The adaptive-weight curves demonstrate Algorithm Application (enforcement of the ordering), not topology theory evidence.\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute (same backbone) — isolates span-boundary decoupling contribution.\nH3 (adaptive vs. fixed): Adaptive weight scheme produces ≥3 higher Argument F1 than fixed-weight decomposed GRPO (same backbone) — isolates adaptive weighting contribution, the primary same-scale baseline and IE track empirical bar.\nH4 (OOD generalization): Analysis-predicted convergence ordering generalizes to OOD benchmarks (RAMS, WikiEvents, MAVEN) — tests whether topology-induced curriculum creates more robust span detectors than single-reward GRPO.",
  "resource_estimate": {
    "compute_note": "Single-run-primary design gated on 50-example dry run. Dry run now performs two measurements: (a) output token length distribution; (b) empirical span-IoU distribution for φ-verification (ML Beta fitting + KS test, negligible additional compute). Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). Per-component F1 logging every 50 steps is added to the fixed-weight baseline run as well (3-curve logger, negligible overhead, no new GPU compute required). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.",
    "manual": {
      "gpu_hours": "~130-160 H100-hours total: dry run (~2 H100-hours, including φ-verification measurement) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours) + fixed-weight Qwen3-8B ablation as primary same-scale comparison (~20-25 H100-hours, checkpoint evaluation not full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours). Total ≤165 H100-hours — within 200 H100-hour ceiling.",
      "gpu_utilization": "Low (20-35%) — GPUs idle during analysis derivation, φ condition algebra, learning curve interpretation, reward verifier implementation, CSPO/ShapE-GRPO differentiation writing, and paper writing.",
      "timeline": "3-4 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$325-660 (at $2.50-4/hr H100 cloud on-demand)"
    },
    "human_in_loop": {
      "gpu_hours": "~130-165 H100-hours total (same single-run-primary design; agent queues dry run first including φ-verification; then main GRPO run; fixed-weight and other ablations from checkpoint eval)",
      "gpu_utilization": "Moderate (55-70%) — agent runs main experiment queue; human approves after dry run φ-verification result (confirm φ̂ > φ* before committing ordering prediction) and after main GRPO run before committing ablation evals.",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150-350 (experiment orchestration, learning curve analysis, φ-verification computation, analysis validation, CSPO/ShapE-GRPO differentiation analysis, ~1500-3000 turns at $0.08-0.12/turn)",
      "estimated_gpu_cost": "~$325-660",
      "risk_note": "Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). φ-verification gate: if φ̂ < φ*, human decides whether to (a) proceed with empirical-only framing or (b) investigate and adjust span tokenization to encourage monotone Beta behavior. Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes. If Argument F1 improvement vs. fixed-weight Qwen3-8B < 3 points, redirect to RL theory track rather than EMNLP IE track."
    },
    "auto_research": {
      "gpu_hours": "~130-165 H100-hours total (dry run auto-queued first including φ-verification; main run launched if token length ≤700 and φ̂ > φ*; checkpoint evals for ablations auto-queued after main run completes)",
      "gpu_utilization": "Near-zero idle (~80-90%) — agent queues dry run, measures token lengths and φ̂, adjusts epoch count if >700 tokens, confirms φ condition, launches main run, auto-logs per-component F1 learning curves every 50 steps for both adaptive-weight and fixed-weight runs, runs plateau detector and θ sensitivity from saved checkpoints.",
      "timeline": "5-8 days with 4× H100 cluster",
      "team": "0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger for both adaptive and fixed-weight runs, φ-verification script (scipy.stats.beta.fit + KS test + threshold comparison), schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)",
      "claude_api_cost": "$175-400 (~2000-4500 turns)",
      "estimated_gpu_cost": "~$325-660",
      "speed_bottleneck": "Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging for both runs and φ-verification add minimal overhead.",
      "risk_note": "Dry run mandatory first. φ-verification must confirm φ̂ > φ* before ordering prediction is published. Plateau detector monitors all three components. Component F1 divergence triggers auto-checkpoint and pause. θ sensitivity auto-evaluated from saved checkpoints after main run. If Argument F1 improvement vs. fixed-weight Qwen3-8B < 3 points, auto-flag for venue redirect to RL theory track."
    }
  },
  "target_venues": [
    "ACL 2027 Main (ARR February 2027 cycle) — primary target for all modes. The Signal Topology Analysis (Conditional Proposition), properly developed with full gradient variance derivation including the φ condition in the appendix, with empirical learning-curve validation (per-component F1 for both adaptive and fixed-weight runs to distinguish topology-induced ordering from algorithm-enforced ordering) and φ-verification protocol, is a main-track contribution if the theoretical novelty claim holds up to review. The extended timeline allows (a) stronger empirical coverage, (b) optional GDPO+adaptive-weight combination experiment as future direction, (c) tighter theoretical integration with arXiv:2602.14872's relay regime and arXiv:2604.19857's decomposition theorem.",
    "EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date). Feasibility only in auto-research mode (5-8 GPU days), leaving 7-10 days for writing with CSPO, ShapE-GRPO, arXiv:2605.02375, STEER, ToolRLA, and all other citations integrated. Even in auto mode, any single GPU failure or training divergence eliminates this window entirely — there is zero buffer. For manual mode (3-4 months) and human-in-loop mode (4-6 weeks), ACL 2027 is the de-facto primary target. EMNLP 2026 is a stretch goal in auto mode only, and requires Argument F1 improvement ≥3 points vs. fixed-weight Qwen3-8B (pre-committed IE track bar) to justify IE Findings submission over RL theory track."
  ],
  "level": "top-tier",
  "key_references": [
    "CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation (arXiv:2604.10918, ACL 2026) — component-specific reward decomposition with token-level gradient routing for table-to-LaTeX; decomposes into structure/style/content components; frames the problem as 'reward ambiguity'; provides empirical motivation for component routing without theoretical characterization of WHY different components have different convergence dynamics or what structural property of the reward determines ordering; no curriculum theory, no adaptive weighting, no sequential skill ordering prediction; parallel rendering dimensions (structure/style/content) vs. sequentially ordered IE skills (span → type → argument); the Signal Topology Analysis provides the theoretical foundation for CSPO's empirical observation",
    "ShapE-GRPO: Shapley-Enhanced Group Relative Policy Optimization (arXiv:2603.29871, March 2026) — decomposes set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory for multi-candidate collective generation scenarios (recommendation, brainstorming, code suggestion); operates at candidate level (which output in a group gets credit) rather than reward-component level (which component has lower gradient variance); no gradient variance analysis, no sequential skill ordering theory, no IE application; distinct mechanism and application domain from CurriculumRLVR-IE; cited to position the space of GRPO reward decomposition approaches and distinguish candidate-level from component-level decomposition",
    "Binary Reward Degeneracy in Policy Gradient Methods (arXiv:2605.02375, May 2026) — proves binary rewards create fundamental optimization degeneracy: infinite set of distributions maximizing expected binary reward (no unique convergence target) and diversity collapse under KL regularization (decreasing β drives policy toward concentrated distributions); independent theoretical support for why binary type-conjunction IE rewards are pathological; complementary to the Signal Topology Analysis which identifies the specific gradient variance mechanism; together provide two independent theoretical motivations for topology-aware IE reward design",
    "STEER: Structured Event Evidence for Video Reasoning (arXiv:2604.04415, April 2026) — introduces Pareto-Frontier guided Advantage Balancing (P-FAB) for multi-objective RL in video reasoning, dynamically resolving reward conflicts between chain-of-thought length and task accuracy objectives along the Pareto frontier; frames the challenge as a multi-objective Pareto optimality problem; CurriculumRLVR-IE differs in mechanism (gradient variance topology analysis vs. Pareto-guided advantage balancing) and domain (IE vs. video reasoning); the Signal Topology Analysis provides a structural explanation (continuous vs. binary reward topology) for why different IE reward components have different convergence dynamics, extending the motivation from empirical multi-objective conflict resolution to formal gradient variance characterization",
    "ToolRLA: Tool-Integrated Reinforcement Learning for Agents (arXiv:2603.01620, March 2026) — multiplicative correctness decomposition across four dimensions (format validity, tool selection, parameter accuracy, regulatory compliance) in a three-stage SFT→GRPO→DPO pipeline for tool-integrated agents; explicitly frames contribution as 'encoding domain priority orderings as inductive biases in the reward landscape'; multiplicative design yields 7 percentage points improvement over additive alternatives; differentiation from CurriculumRLVR-IE: ToolRLA encodes priority orderings multiplicatively based on domain knowledge (empirical design choice) for tool invocation dimensions; the Signal Topology Analysis derives the span→type→argument priority ordering from first principles via gradient variance of continuous vs. binary reward topology (formal rather than empirical basis); mechanism (multiplicative vs. additive with adaptive weights) and domain (tool agents vs. IE) are also distinct",
    "ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose atomic span+type conjunction as the mechanism causing poor argument gradient; does not cover RAMS/WikiEvents/MAVEN; uses Qwen3-4B (scale difference from proposed Qwen3-8B is an acknowledged confound in any direct comparison)",
    "SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility (arXiv:2604.07837, April 2026) — PAWA (momentum-based exponential up-weighting when LCB of reward improvement is positive) and RADR (data category rebalancing); applied to open-ended LLM alignment; no gradient-variance analysis; no span/type/argument decomposition; PAWA momentum philosophy vs. analysis-derived convergence-gap philosophy: the Signal Topology Analysis identifies gap-to-convergence as the relevant quantity, directly motivating the gap-based formula over SPARD's momentum formula",
    "VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models (arXiv:2509.19803, September 2025) — between-sample variance for difficulty-based data selection in math RLVR; +4.67 points average on Qwen3-8B-Base; explicit distinction: VCRL uses between-sample variance for data selection; Signal Topology Analysis uses within-sample reward-component topology for skill ordering",
    "RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition — the Signal Topology Analysis deepens RuCL's analysis by proving WHY span-IoU is reliably low-variance (continuous topology, conditional on φ-sufficiency) while type-conjunction is reliably high-variance (Bernoulli at low-probability regime in early training), deriving the mechanism that RuCL observes but does not formalize",
    "EGCA: Execution-Grounded Credit Assignment (arXiv:2603.16158, ICLR 2026 Workshop) — concentrates GRPO advantage on causal token spans via reference-execution comparison for code generation; requires executable code with test cases and reference execution traces; inapplicable to IE; credit assignment is causal (execution divergence) vs. structural (reward topology); cited to position the space of span-level credit assignment approaches and distinguish from IE-specific topology analysis",
    "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — prevents advantage collapse by normalizing each reward's advantage independently; orthogonal to analysis-derived adaptive weights (normalization-level vs. aggregation-level); combination of GDPO normalization + convergence-gap adaptive weights is a concrete future direction",
    "MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization (arXiv:2601.07208, January 2026) — contextual bandit formulation for dynamic reward weights; bi-level optimization with Conductor network; more complex than analysis-derived simple formula; no IE application",
    "On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for task-level difficulty ordering in L-step compositional reasoning (Theorem 5.2); Signal Topology Analysis extends relay concept from task level to reward-component level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness",
    "Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — Reward Decomposition Theorem bounding sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T); Signal Topology Analysis complements by identifying the structural IE-specific property (continuous span-IoU topology) that makes early-training variance reduction benefit dominate this bounded cost",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; motivation for adaptive component weights",
    "APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking; conceptually aligned with analysis's prediction that binary type-conjunction component has higher variance and would dominate gradients without topology-aware decomposition",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary SFT upper bound",
    "Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that boundary detection is a prerequisite for entity typing: 36.73% F1 drop for long entities on ACE04 when boundary regression is removed; architectural motivation for the span-first convergence ordering that the analysis derives from gradient variance",
    "T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)",
    "REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings)",
    "R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025)",
    "Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025)",
    "EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "RAMS: Multi-Sentence Argument Linking (ACL 2020)",
    "WikiEvents: Document-level Event Argument Extraction (NAACL 2021)"
  ],
  "description": "Joint NER+RE+EE GRPO training fails on event extraction because existing reward designs treat (span, type) pairs as atomic units, conflating a continuous signal (span-IoU) with a binary signal (type-conjunction) and eliminating the gradient variance ordering that would otherwise produce implicit curriculum. CurriculumRLVR-IE's primary contribution is the **Signal Topology Analysis (Conditional Proposition)**: a formal gradient variance derivation showing that in GRPO for IE, the topological property of each reward component — continuous (span-IoU, Beta-distributed), binary (type-conjunction, Bernoulli at low-probability regime in early training), or compositional (argument F1, compound Bernoulli variance) — determines its gradient variance in early training, which in turn determines convergence ordering (span → type → argument) without explicit scheduling. The Var(R_type) derivation assumes span and type correctness are independent Bernoulli trials; in practice they are positively correlated, but since positive correlation raises the actual conjunction probability q above p_s·p_t while q remains below 0.5 in early training, the actual variance is higher than the independence estimate — strengthening rather than weakening the ordering Var(R_span) < Var(R_type). The ordering holds conditional on the **φ-sufficiency premise**: the empirical span-IoU distribution's Beta concentration parameter φ must satisfy φ > φ*(p_s, p_t) ≡ μ_s(1−μ_s)/(p_s·p_t·(1−p_s·p_t)) − 1, verified during the mandatory dry run via ML Beta fitting and KS test. arXiv:2605.02375 independently proves binary rewards create fundamental optimization degeneracy (infinite maximizing distributions, diversity collapse), providing complementary theoretical support for topology-aware reward design. This extends the relay regime of arXiv:2602.14872 from task-level difficulty ordering to reward-component-level topology ordering within a single IE task type, and complements arXiv:2604.19857's Reward Decomposition Theorem by identifying the specific structural property (span-IoU continuity) that makes variance reduction benefit dominate the bounded sub-optimality cost. The **φ-verification protocol** — fitting a Beta distribution to dry-run span-IoU values and comparing φ̂ to the threshold before any ordering claim is published — is itself a novel diagnostic contribution: the first method for empirically verifying whether topology-induced curriculum conditions are active in a specific GRPO-IE training setting. Two algorithmic applications follow: (1) the span-boundary-decoupled reward design (span-IoU isolated from type-conjunction, each in its correct topological class); (2) the convergence-gap adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), gap-based rather than momentum-based (contrasting with SPARD's PAWA) because the analysis identifies gap-to-convergence, not rate-of-progress, as the relevant quantity. CSPO (arXiv:2604.10918, ACL 2026) demonstrates empirically that component routing helps for table-to-LaTeX without theoretical characterization; ShapE-GRPO (arXiv:2603.29871) decomposes at the candidate level via Shapley attribution rather than the component topology level; STEER (arXiv:2604.04415) addresses multi-objective balance in video reasoning via Pareto-guided advantage balancing — the Signal Topology Analysis provides a formal gradient variance explanation extending motivation from empirical conflict resolution to topology-grounded characterization; ToolRLA (arXiv:2603.01620) encodes priority orderings multiplicatively as domain inductive biases for tool agents, while the Signal Topology Analysis derives the IE ordering from first principles; EGCA (arXiv:2603.16158) does causal span credit assignment for code generation (requires reference execution, inapplicable to IE); GDPO (arXiv:2601.05242) prevents advantage collapse at the normalization level — orthogonal and combinable. The primary empirical test for H1 (topology analysis) is the **per-component F1 curves from the fixed-weight Qwen3-8B baseline run**: because the adaptive weight formula actively enforces the span→type→argument ordering, only the fixed-weight curves can cleanly confirm topology-induced ordering independent of algorithmic enforcement. Per-component F1 is logged every 50 GRPO steps for both adaptive and fixed-weight runs to distinguish topology-induced ordering from algorithm-enforced ordering — requiring no new GPU compute (a 3-curve logger added to the already-planned fixed-weight baseline). Pre-committed IE track empirical bar: ≥3 Argument F1 improvement on ACE2005 vs. fixed-weight Qwen3-8B; if not met, venue redirects to RL theory track. Primary foil: ProUIE (Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%); scale confound (8B vs. 4B) explicitly acknowledged, with fixed-weight Qwen3-8B ablation as the primary same-scale baseline. Backbone: Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run (including φ-verification) + one main GRPO run + checkpoint-derived ablations, ~130-165 H100-hours within 200 H100-hour ceiling. Primary target: ACL 2027 Main via February 2027 ARR (all modes); EMNLP 2026 Findings via May 25 ARR is auto-mode-only stretch goal with zero timeline margin and ≥3 F1 empirical bar required.",
  "project_name": "joint_ie_decomposed_rlvr",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["HARD CONSTRAINT VIOLATION — Auto mode estimate of ~700h A100 converts to ~350-450h H100, which directly exceeds the user's ≤200h H100 total compute ceiling. Even manual mode (~300h A100 ≈ 150-200h H100) is already at the ceiling with zero margin for ablations. Light-R1 reports 3,328-5,376 A100-GPU-hours per single GRPO run on a 14B model; the Generator's estimates are underestimated by at least 2-5× for full fine-tuning.", "REAR MISCHARACTERIZATION — REAR (EMNLP 2025 Findings) is described as 'RL only to event argument extraction with a single joint reward,' but the paper's documented pipeline includes joint supervised warm-up AND joint reinforced optimization across both EAE and RE tasks. The novelty claim 'no work applies GRPO to the full NER+RE+EE joint task' needs to be more carefully scoped relative to REAR's actual multi-task RL coverage.", "10-MONTH TEMPORAL BLIND SPOT — The landscape section cites papers from May-July 2025, but the current date is May 2026. No search evidence was found for a concurrent paper doing exactly full joint NER+RE+EE with decomposed RLVR, but this is a 10-month gap in a field that moved from 'no RLVR for RE' to R1-RE+R2GRPO+REAR in under 6 months. The 'first' claim is fragile without an explicit concurrent-work audit for Aug 2025-May 2026.", "MISSING REQUIRED BENCHMARKS — The user specified MAVEN, WikiEvents, and RAMS as required evaluation datasets for event extraction. None appear in the proposed benchmark suite (ACE2005 + CoNLL + SciERC). MAVEN is large-scale general-domain event detection; WikiEvents and RAMS are argument extraction benchmarks that would directly test the event-argument component of the decomposed reward.", "REWARD WEIGHT UNDERSPECIFICATION — The three reward components (span-boundary F1, type-conditional F1, relation/triple F1) require explicit balancing coefficients. The Generator claims these 'auto-schedule via saturation' but provides no concrete mechanism, no sensitivity analysis, and no bounds on degenerate regimes (e.g., a model that maximizes span-F1 by outputting every token as a separate span). This is the primary technical risk and needs a principled solution (e.g., uncertainty weighting, learned coefficients, or constrained reward ranges).", "MODEL SIZE VS. CONSTRAINT MISMATCH — Qwen2.5-14B is the wrong model size for this constraint envelope. Qwen2.5-7B with LoRA-based GRPO is the only realistic configuration that can produce even a minimal experiment within 200 H100-hours. The 14B choice appears driven by competitive benchmarking goals rather than feasibility analysis."]
Feedback: The core idea — decomposed RLVR rewards that give partial credit for span-correct/type-wrong predictions — is technically sound and partially novel. To get this to a passable state: (1) Scale down to Qwen2.5-7B and specify LoRA GRPO throughout; recompute all resource estimates with LoRA reduction factors and confirm the auto mode fits under 200 H100-hours. (2) Correct the REAR framing: acknowledge REAR does joint EAE+RE RL, and position the differentiation as (a) NER inclusion + (b) strictly decomposed per-substructure rewards vs. REAR's single joint RL reward. (3) Add MAVEN, WikiEvents, and RAMS to the benchmark suite — these are explicitly required by the target track and event extraction without them is incomplete. (4) Provide a concrete reward weighting scheme: either fixed normalized coefficients justified by pilot experiments, or a learned mixing network trained jointly with the policy. (5) Add a section explicitly addressing Aug 2025-May 2026 concurrent work risk — search arXiv for 'joint information extraction GRPO' from Q3-Q4 2025 before submitting, and pre-register the differentiators. This idea is 'revise, not fail' — the decomposed reward curriculum signal is a real contribution — but the resource constraint violation and REAR mischaracterization must be fixed before this can be argued as novel and feasible.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL CONCURRENT WORK MISSED — ProUIE (arXiv:2604.10633, April 12, 2026) covers joint NER+RE+EE with GRPO + Stepwise Fine-grained Reward (SFR) decomposed hierarchically by structural unit: NER (entity-type → entity-value), RE (relation-type → relation-instance → entity-pair), EE (event-type → trigger → role → argument). Evaluated on 36 public datasets including ACE2005. The Generator's explicit claim 'No published paper applies decomposed GRPO rewards to the full joint NER+RE+EE task as of May 2026 searches' is false. A reviewer who knows ProUIE will immediately reject the novelty claim as stated.", "NOVELTY REPOSITIONING REQUIRED — The only surviving technical differentiator from ProUIE is: span-boundary F1 computed *independent of type label* (proposed) vs. ProUIE's atomic type-entity pairs (ProUIE rewards entity-type and entity-value but does not reward span-correct/type-wrong predictions). This specific contribution must become the paper's primary framing; the current framing ('no prior work applies decomposed GRPO to NER+RE+EE') is no longer defensible.", "ProUIE's DOCUMENTED EE WEAKNESS IS AN OPPORTUNITY — ProUIE explicitly reports 'underperforming the strongest baseline for both triggers and arguments' on ACE2005 EE. The proposed work should be specifically framed as addressing this failure mode: if span-conditional rewards (rewarding trigger detection independently of argument role accuracy) fix ProUIE's EE weakness, that is a compelling and concrete result. The Generator should add a comparison directly against ProUIE's published EE numbers.", "OUTPUT LENGTH UNDERESTIMATE — The 100-300 token claim for IE JSON extractions is optimistic for complex multi-task joint extraction with chain-of-thought. ACE2005 sentences with multiple entities, relations, and event triggers (with CoT trace) realistically produce 300-600+ tokens per example. If true output length is 2-3× the assumed value, GRPO rollout costs scale proportionally and auto-mode (3 runs) may exceed 200 H100-hours. A 50-example dry run measuring actual output token length before full training is essential.", "OOD DOCUMENT-LEVEL EVALUATION RISK — The model is trained on sentence-level ACE2005 examples and evaluated on document-level RAMS (multi-sentence argument linking) and WikiEvents (document-level EAE). Without document-level context handling (e.g., sliding window, cross-sentence attention), the OOD evaluation may fail for reasons unrelated to reward decomposition, threatening the validity of the OOD generalization claim. The Generator should acknowledge this and describe how document-level inputs are handled at inference."]
Feedback: Round 2 successfully addressed the resource constraint (7B+LoRA is now realistic), REAR framing (correctly described), missing benchmarks (MAVEN/RAMS/WikiEvents now included), and reward underspecification (fixed weights with pilot calibration). However, a critical gap opened: ProUIE (arXiv:2604.10633, April 2026) does joint NER+RE+EE with GRPO + fine-grained hierarchical rewards, directly occupying the 'first decomposed GRPO for joint IE' claim. You cannot submit without addressing this. Recommended revision path: (1) Acknowledge ProUIE in related work — frame the proposed work as explicitly extending ProUIE's limitation: ProUIE's SFR treats type-entity pairs as atomic, meaning a span-correct/type-wrong prediction receives near-zero reward. The proposed span-IoU-conditioned hierarchical reward explicitly credits partial correctness at the span level. (2) Make the EE comparison against ProUIE's published numbers the centerpiece empirical result — ProUIE underperforms baselines on ACE2005 EE; showing that span-conditional rewards fix this is a sharp, verifiable contribution. (3) Position MAVEN/RAMS/WikiEvents as the OOD evaluation that ProUIE does not cover. (4) Measure actual output token lengths on a 50-example ACE2005 pilot BEFORE committing to the 100-300 token estimate and the 200 H100-hour ceiling claim. (5) Add a one-paragraph discussion of how document-level inputs (RAMS, WikiEvents) are handled at inference given sentence-level ACE2005 training — sliding window with sentence-level extractions merged, or prompt includes full document context?

### Round 3 review
Verdict: revise
Issues: ["VENUE FACTUAL ERROR (critical): The 'EMNLP 2026 via August ARR cycle' path does not exist. ARR's own dates page confirms the August 3, 2026 ARR cycle commits to EACL 2027, not EMNLP 2026. The ONLY path to EMNLP 2026 is submission by May 25, 2026 (commitment deadline August 2). If May 25 is infeasible for the current experiments, the correct fallback is ACL 2027 (February 2027 ARR deadline), not 'EMNLP 2026 via August.' The target venue section must be corrected.", "COMPUTE CEILING STILL POTENTIALLY VIOLATED: The Generator estimates 80-200 H100-hours per GRPO run and commits to 2 runs (total: 160-400 H100-hours). The upper-bound scenario (400 H100-hours) is 2× the hard constraint of ≤200 H100-hours. The Generator says 'ceiling constrained to 2 GRPO runs to stay within 420 H100-hours' — but 420 >> 200. A concrete single-run-primary design is needed: one main GRPO run (90-120 H100-hours if dry run confirms ~350-token outputs), with the α₁=0 ablation derived from a fraction of rollouts at the final checkpoint, keeping total under 200 H100-hours.", "CASCADE FAILURE CLAIM OVERSTATED: ProUIE's paper does not explicitly state that wrong trigger type produces near-zero argument reward. Independent fetch of the paper confirms: 'The paper doesn't explicitly state that incorrect trigger types produce near-zero argument rewards, though the piecewise penalty suggests coarse errors receive priority.' The Generator should reframe this as an inference from SFR's piecewise structure rather than ProUIE's own diagnosis — otherwise a reviewer who reads ProUIE carefully will flag this as misrepresentation.", "CONTRIBUTION SCOPE NARROWNESS RISK: The paper's distinguishing technical contribution is a single reward design change (add α₁=0.4 span-boundary component independent of type label). Without stronger theoretical grounding — e.g., a formal proof or convergence analysis showing span-decoupled rewards induce a natural curriculum (span → type → argument) — reviewers may characterize this as an ablation of ProUIE's reward design rather than a standalone method. Consider adding a curriculum convergence analysis or learning curve comparison showing the predicted sequential skill acquisition.", "OOD DOCUMENT-LEVEL CONFOUND UNRESOLVED: The paper trains on sentence-level ACE2005 and evaluates on document-level RAMS/WikiEvents/MAVEN. The Generator acknowledges this as a 'confound noted explicitly' but this framing is insufficient — reviewers will ask why no document-level adaptation was attempted. Reframe OOD results as 'zero-shot cross-distribution generalization from sentence to document' and add a brief analysis of which document-level aspects hurt performance (e.g., coreference chains, multi-sentence arguments)."]
Feedback: The technical core is now well-specified and the ProUIE differentiation is valid. Three rounds of revision have addressed compute scale, REAR framing, missing benchmarks, and output-length underestimation. The remaining fixable issues are: (1) Correct the venue section immediately — the only path to EMNLP 2026 is the May 25 ARR submission (15 days away); if that is missed, the real next target is ACL 2027 via February 2027 ARR. Remove all references to 'EMNLP 2026 via August ARR cycle.' (2) Design a single-run budget that fits ≤200 H100-hours: commit the dry run (2 H100-hours) + one main GRPO run (target 90-120 H100-hours at ≤400 token output) + the α₁=0 ablation from checkpoint evaluation (not a full new run, ~20-30 H100-hours). Total: ~130-150 H100-hours — within the constraint. (3) Soften the cascade failure attribution from 'near-zero reward' (ProUIE's claimed mechanism) to 'near-zero reward implied by SFR's piecewise conditioning on matched trigger groups' (your inference). This distinction matters to reviewers who read ProUIE. (4) Strengthen the theoretical framing: if you can show analytically or empirically that span-decoupled rewards create a sequential skill curriculum (span convergence first, then type, then argument), this elevates the paper from 'ablation' to 'method contribution.' Learning curves for each reward component across training steps would directly support this claim at low additional compute cost.

### Round 4 review
Verdict: revise
Issues: ["UNCITED COMPETITOR (HIGH PRIORITY): GDPO (arXiv:2601.05242, January 2026, ICML 2026) from NVIDIA proposes per-reward normalization in GRPO to prevent advantage collapse in multi-reward settings — applied to tool calling, math, and coding. GDPO is the normalization analog to the proposed adaptive weighting: GDPO normalizes each reward independently within the group before aggregation; the proposed method dynamically adjusts the aggregation weights based on convergence progress. A reviewer familiar with GDPO (now an ICML 2026 poster) will immediately flag its absence. The generator must cite GDPO and clearly distinguish: GDPO prevents per-reward advantage collapse at the normalization level; the proposed method enforces a curriculum by adjusting relative weights as each component converges — these are complementary and could be combined (GDPO normalization + proposed adaptive weights), which would itself strengthen the paper.", "UNCITED THEORETICAL PARALLEL (MEDIUM PRIORITY): 'The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards' (arXiv:2602.14872, February 2026) formally proves that RLVR exhibits implicit skill ordering emergence when the difficulty spectrum is smooth, using a relay regime analysis with convergence guarantees. The proposed paper's Contribution 1 (gradient variance analysis showing span→type→argument sequential convergence) is an instance of this broader phenomenon. Without citing this paper and positioning the IE-specific analysis as a domain instantiation of the relay regime framework, reviewers reading both papers will flag this as a missed citation. Importantly, the Implicit Curriculum paper provides stronger theoretical machinery — the generator should either explicitly build on it or clearly explain what the IE-specific variance analysis adds beyond the general framework.", "UNCITED THEORETICAL PARALLEL (MEDIUM PRIORITY): 'Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization' (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards, applied to LVLMs. The proposed Contribution 1 provides a gradient-variance-based analysis of a similar decomposition for IE — it must acknowledge arXiv:2604.19857, explain how its span-IoU continuous signal analysis extends or complements the formal sub-optimality bounds in that paper, and position the IE task structure (span IoU continuity vs. joint conjunction) as the distinctive aspect.", "ADAPTIVE WEIGHT θ HYPERPARAMETER RISK: The convergence target θ=0.7 is used as the reference point for the weight formula w_i(t) = max(ε, θ - F1_i(t)) / σ_i(t). If argument F1 never reaches 0.7 (InstructUIE achieves 72.94% at 11B; the proposed system targeting >60% suggests this is achievable but not guaranteed), the argument component will persistently receive high weight throughout training, potentially causing variance hijacking in late training — the exact phenomenon the scheme is meant to prevent. The generator should add: (a) a secondary convergence criterion (e.g., plateau detection when F1_i improves <1% over 200 steps), or (b) sensitivity analysis showing the method is robust to θ ∈ {0.6, 0.7, 0.8}.", "EMNLP MAIN vs FINDINGS REALISM: The paper targets EMNLP 2026 Main but the three contributions individually are incremental extensions of ProUIE (reward decomposition), APEX/2509.11452 (adaptive weighting), and RuCL (gradient variance theory). The learning curve diagnostic is genuinely novel for IE but is a contribution supporting the method, not the method itself. The realistic target is EMNLP 2026 Findings — the generator should explicitly acknowledge this in the target venue section to set accurate expectations for the auto-mode agent."]
Feedback: The core technical nucleus is now well-executed: span-boundary-decoupled GRPO reward for IE is a real gap, the single-run compute design fits within 200 H100-hours, and the cascade failure attribution is properly softened. Round 4 has resolved all four Round 3 issues. However, three concurrent papers published since Round 3 that are directly relevant to the claimed contributions are missing from the related work: (1) GDPO (ICML 2026) for multi-reward GRPO normalization, (2) 'The Implicit Curriculum' (Feb 2026) for RLVR skill ordering theory, and (3) arXiv:2604.19857 (April 2026) for composite-reward GRPO convergence theory. These omissions, if noticed by a reviewer, will be read as lack of thoroughness. Recommended actions for Round 5: (a) Add GDPO to related work — 1 paragraph distinguishing per-reward normalization (GDPO) from convergence-progress adaptive weighting (proposed), note they are complementary, suggest combining GDPO normalization + proposed weights as a future direction. (b) Add 'The Implicit Curriculum' — 1 paragraph framing the IE span→type→argument gradient variance analysis as a domain instantiation of the relay regime framework, with the span-IoU continuity as what makes the IE difficulty spectrum smooth in the relevant sense. (c) Add arXiv:2604.19857 — 1 paragraph noting its Reward Decomposition Theorem for LVLMs and explaining how the proposed early-training gradient variance analysis complements it by identifying span continuity as the specific structural property that makes IE reward decomposition beneficial. (d) Add θ sensitivity analysis or secondary convergence criterion for the adaptive weight formula. These are additive changes to related work and the method section — no experimental changes required. The EMNLP 2026 Findings track is the appropriate target given the contribution scope.

### Round 5 review
Verdict: revise
Issues: ["UNCITED DIRECT COMPETITOR — SPARD (arXiv:2604.07837, April 2026) is not cited and directly threatens Contribution 2's novelty. SPARD's PAWA (Progress-Aware Weight Adaptation) adjusts reward-component weights dynamically based on training progress using a confidence-bound adjusted exponential scheme: w_{t+1}^{r,i} = w_{t}^{r,i}·exp(η·Q_t^i). This operates at the reward-component level — NOT the data-sample level. Any reviewer who knows SPARD will immediately flag its absence. The paper must cite SPARD, accurately distinguish the proposed w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) from SPARD's LCB-based exponential growth formula, and narrow the novelty claim from 'first adaptive reward weighting for GRPO' to 'first adaptive weighting applied to the span/type/argument IE decomposition with formal gradient-variance justification for why the convergence ordering matters.'", "INCORRECT DIFFERENTIATION FROM SPARD — The most natural defensive move for the generator ('SPARD is data-level curriculum, ours is reward-component level') is factually wrong: SPARD has BOTH reward-component level weighting (PAWA) AND data-category level rebalancing (RADR). The paper must instead differentiate on: (a) formula design — variance-normalized lagging (proposed) vs. confidence-bound exponential growth (SPARD); (b) IE-specific structural decomposition (span-IoU continuity vs. type conjunction is not present in SPARD); (c) formal gradient-variance justification linking span-IoU continuity to early-training variance reduction, which SPARD does not provide.", "UNCITED COMPETITOR (MEDIUM) — VCRL (arXiv:2509.19803, September 2025) uses variance of rollout group rewards to estimate sample difficulty and drive curriculum selection for RLVR on math. Since CurriculumRLVR-IE's theoretical narrative explicitly centers on reward-variance reduction, a reviewer will expect VCRL to be cited and the distinction made clear (VCRL: between-sample variance for difficulty; proposed: within-sample reward-component variance for skill ordering).", "CONTRIBUTION 2 NOVELTY WEAKENED — With SPARD (PAWA) covering reward-component adaptive weighting and arXiv:2509.11452 + APEX already cited for motivation, Contribution 2's standalone novelty is now thin. The generator should reframe Contribution 2 as the application and instantiation of adaptive weighting for the specific IE skill hierarchy, not as a novel adaptive weighting technique per se. The genuine novelty is the combination of span-decoupled reward (Contribution 1's design) with convergence-aware weighting derived from the gradient variance analysis, not the weighting formula in isolation.", "EMNLP 2026 FINDINGS FEASIBILITY — The May 25 ARR deadline is 15 days away. The auto-research timeline (5-8 days for GPU work) is possible but writing a submission-quality paper in the remaining time after experiments is unrealistic. The generator correctly lists this as 'auto and HIL modes' for EMNLP 2026 and 'manual mode' for ACL 2027, but should be explicit that even for auto mode, producing an EMNLP-quality paper by May 25 requires the full 16 days with no setbacks — the dry-run gate (Day 1-2), main training (Days 3-7), analysis (Days 8-10), and writing (Days 11-15) leave zero margin for iteration."]
Feedback: Round 5 has correctly addressed all four Round 4 issues: GDPO is distinguished, arXiv:2602.14872 and arXiv:2604.19857 are positioned, θ sensitivity + plateau detector are specified, and EMNLP Findings (not Main) is the target. The core technical nucleus — span-boundary IoU reward decoupled from type label, inducing a span→type→argument gradient relay in GRPO training — remains the paper's strongest and most defensible claim. However, a new concurrent paper has emerged that must be addressed before submission: (1) Add SPARD (arXiv:2604.07837) to related work — 1 paragraph describing PAWA's exponential confidence-bound weighting at the reward-component level, then distinguishing the proposed scheme by: (a) variance-normalized lagging formula vs. SPARD's LCB exponential growth, (b) IE-specific span/type/argument decomposition not present in SPARD, and (c) the formal gradient-variance analysis linking span-IoU continuity to sequential convergence — a structural argument SPARD does not make. Do NOT use the 'data-level vs. reward-component level' distinction because it is factually wrong. (2) Add VCRL (arXiv:2509.19803) with 1 sentence: between-sample variance for difficulty curriculum vs. within-sample reward-component variance for skill ordering. (3) Reframe Contribution 2's novelty: the contribution is the application of adaptive weighting to the span/type/argument structure with the gradient-variance analysis as motivation, not the adaptive weighting scheme as a standalone novel technique. These are all additive related-work and framing changes — no experimental changes required. The span-boundary decoupling remains genuinely novel for GRPO-based IE.

### Round 6 review
Verdict: revise
Issues: ["UNCITED ACL 2026 CONCURRENT WORK — CSPO (arXiv:2604.10918, April 2026, accepted ACL 2026) proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation, explicitly framing the problem as 'reward ambiguity' in structured generation and assigning component-specific rewards backpropagated only through relevant tokens. The surface framing is identical to CurriculumRLVR-IE's 'reward atomicity' problem. A reviewer who knows CSPO will immediately flag its absence. The Generator must add CSPO to related work with 1 paragraph distinguishing: (a) span-boundary F1 independent of type label vs. CSPO's structure/style/content decomposition for LaTeX tokens, (b) gradient variance curriculum analysis and adaptive weighting are completely absent from CSPO, (c) CSPO has no sequential skill ordering — it assigns static component-specific rewards without dynamic adaptation.", "COMPOUND NOVELTY ATTRITION — By Round 6, the Generator has needed to reframe Contribution 1 as an extension of RuCL/relay regime, reframe Contribution 2 as an 'application/instantiation' after SPARD, and now must add CSPO as yet another partially overlapping prior work for structured-generation reward decomposition. Each addition is individually manageable, but the cumulative effect is that any single contribution, when correctly positioned, reads as incremental. An EMNLP reviewer reading the related work section with SPARD, GDPO, CSPO, RuCL, arXiv:2602.14872, and arXiv:2604.19857 all cited as partial precedents may characterize the paper as 'applying existing techniques to IE' rather than a methodological contribution. The paper needs a single sharpest claim — the gradient variance curriculum analysis for span-IoU continuity vs. type-conjunction probability is the strongest differentiator; the abstract and intro should lead with this, not bury it under the other contributions.", "EMPIRICAL RESULT RISK NOT ADEQUATELY SCOPED — The claim 'closes a material fraction of the 20-point ProUIE argument F1 gap' (H4, target >60%) is vague. If Qwen3-8B with the proposed reward reaches 58-62% Argument F1 vs. ProUIE's 52.58% (Qwen3-4B), a reviewer will ask: is the improvement from reward design or from the 4B→8B scale increase? The paper has no same-scale (8B) ProUIE comparison. The Generator should flag this confound more explicitly in the experimental design and add the fixed-weight Qwen3-8B ablation (baseline (c)) as the primary comparison for reward design effect, not the scale-mismatched ProUIE 4B numbers.", "EMNLP FINDINGS TIMELINE ZERO-MARGIN — With May 25 ARR deadline confirmed (15 days from today), even auto-research mode (5-8 GPU days) leaves 7-10 days for writing and CSPO/other citation additions. The Generator should explicitly acknowledge in the feasibility note that any single GPU or training failure eliminates the EMNLP 2026 window entirely, making ACL 2027 via February 2027 ARR the de-facto primary target for any non-auto mode."]
Feedback: Round 6 has correctly addressed all Round 5 issues: SPARD is accurately described and differentiated by formula philosophy (momentum vs. convergence-gap), VCRL is cited with the correct between-sample vs. within-sample variance distinction, Contribution 2 is properly reframed as application/instantiation, and EMNLP Findings is the acknowledged realistic target. The technical nucleus remains sound. The single new action required: (1) Add CSPO (arXiv:2604.10918, ACL 2026) to related work — 1 paragraph: CSPO decomposes structured generation rewards by functional component (structure/style/content) for table-to-LaTeX and argues for component-specific backpropagation to resolve 'reward ambiguity'; distinguish by (a) span-boundary F1 independent of type label is a more precise decoupling than CSPO's LaTeX-component boundaries, (b) curriculum theory and adaptive weighting are entirely absent from CSPO, (c) CSPO targets document rendering fidelity not IE structured prediction. Beyond CSPO, two sharpening suggestions that would elevate novelty score above 3/5 without new experiments: (a) Restructure the abstract/intro to lead with the gradient variance curriculum claim as the paper's primary theoretical contribution, citing it as a reward-component-level relay regime (extending arXiv:2602.14872) specifically for IE — this is the strongest differentiator from all prior work; (b) Add an explicit acknowledgment in Section 5 that the scale difference (8B proposed vs. 4B ProUIE) is a confound in the primary ProUIE comparison and that the fixed-weight Qwen3-8B ablation (not ProUIE 4B) is the clean baseline for reward design effect. These changes require only writing revisions — no new experiments.

### Round 7 review
Verdict: revise
Issues: ["THEOREM RIGOR FLAW (HIGH PRIORITY — NEW in Round 7): The Signal Topology Theorem's variance ordering Var(R_span) < Var(R_type) requires the Beta concentration parameter φ of the span-IoU distribution to satisfy φ > [μ(1-μ) / (p_s·p_t·(1-p_s·p_t)) - 1]. This is an empirical condition on the shape of the early-training span-IoU distribution — NOT a consequence of reward design choices alone. The paper claims the ordering holds 'regardless of hyperparameter choices, as long as p_s < 0.5,' but this only addresses the reward weighting hyperparameters α. If a model produces dispersed span-IoU values (low φ, U-shaped Beta, which occurs when the model sometimes partially overlaps gold spans randomly), Var(R_span) can exceed Var(R_type) and the theorem's ordering reverses. For a paper whose primary novelty is 'Theorem 1,' calling this a theorem without explicitly stating and verifying the φ condition will be caught by any theory-oriented reviewer. Fix: (a) derive the explicit condition on φ required for the ordering (takes 1 paragraph of algebra), then empirically verify it from the dry run's span-IoU distribution logs; or (b) reframe as 'Signal Topology Analysis' / 'Theoretical Framework' rather than 'Theorem 1,' with the distributional assumptions stated as explicit premises. The latter framing is more honest and still publishable at an IE track.", "UNCITED CONCURRENT WORK — ShapE-GRPO (MEDIUM): arXiv:2603.29871 (March 2026) proposes Shapley-Enhanced GRPO (ShapE-GRPO), which decomposes set-level GRPO rewards into candidate-specific signals using Shapley values from cooperative game theory. While it does not address IE or the continuous/binary topology distinction, it is a concurrent GRPO reward decomposition approach that operates at the component/candidate level. A reviewer familiar with ShapE-GRPO may flag its absence. Add 1 sentence to related work: ShapE-GRPO decomposes multi-candidate rewards via Shapley attribution rather than topological classification; it does not address sequential skill ordering or provide a gradient variance analysis for structured IE prediction.", "UNCITED BACKGROUND — Binary Rewards Fundamental Challenges (MEDIUM): arXiv:2605.02375 (May 2026) proves that binary rewards create fundamental degeneracy in policy gradient methods (infinite maximizing distributions, diversity collapse), providing theoretical background for the type-conjunction challenge. The paper's framing of 'type-conjunction as binary Bernoulli → gradient issues' would be strengthened by citing this as independent theoretical motivation. Add 1 sentence noting that the degeneracy of binary rewards in policy gradient is independently established by arXiv:2605.02375, consistent with the proposed topology analysis.", "EMNLP 2026 IE TRACK FIT RISK (MEDIUM): The paper's primary novelty is now framed as a theoretical result (Signal Topology Theorem) — an RL theory contribution. The Information Extraction track at EMNLP expects method contributions validated by strong IE benchmark improvements. If Argument F1 on ACE2005 with Qwen3-8B (proposed) vs. fixed-weight Qwen3-8B (baseline) shows <3% improvement, reviewers will question whether the theorem has practical significance regardless of its theoretical interest. The paper should pre-commit to a 'meaningful improvement' threshold (e.g., ≥3 F1 points on Argument F1 vs. fixed-weight same-scale baseline) as the empirical bar that justifies IE track submission; if that bar is not met, the paper belongs in an RL theory track rather than IE Findings."]
Feedback: Round 7 has correctly integrated all Round 6 issues: CSPO is now prominently differentiated at multiple paper levels (core problem, landscape, approach), the theorem-derived adaptive weight philosophy vs. SPARD momentum is clearly articulated, and the scale confound is explicitly managed with fixed-weight Qwen3-8B as the primary same-scale baseline. The paper's theoretical nucleus — the Signal Topology Theorem — is the strongest differentiator from all prior work. One new actionable issue dominates this round: the theorem's mathematical conditions are underspecified. The variance ordering Var(R_span) < Var(R_type) depends on the Beta concentration parameter φ of the empirical span-IoU distribution in early training, not just on p_s < 0.5. This is fixable with one paragraph of algebra and one dry-run measurement. Specifically: (1) Derive the condition φ > [μ(1-μ)/(p_s·p_t·(1-p_s·p_t)) - 1] explicitly and state it as a premise of Theorem 1; (2) add a dry-run diagnostic that logs the empirical span-IoU distribution and fits a Beta distribution to it (KS test, χ² test), using the estimated φ to verify the condition is met before claiming the theorem's validity for this specific run. This converts the 'theorem' from a claim that requires blind trust into a falsifiable prediction that the dry run either confirms or refutes — strengthening both the theory and the empirical contribution simultaneously. Two minor citations needed: ShapE-GRPO (arXiv:2603.29871) and the binary rewards degeneracy paper (arXiv:2605.02375). These require only 1-2 sentences each. The primary EMNLP 2026 Findings timeline pressure is acknowledged and auto-mode-only; ACL 2027 remains the realistic primary target for all other modes. If the theorem's φ condition can be verified empirically and the Argument F1 improvement over same-scale fixed-weight baseline meets ≥3 F1 points, the paper's theory + method + falsifiability triad is a genuine EMNLP 2026 Findings contribution in IE.

### Round 8 review
Verdict: revise
Issues: ["LEARNING CURVE CONFOUND IN H1 TEST (NEW, MEDIUM PRIORITY): H1 predicts 'span F1 converges before type-conditioned F1, which converges before argument F1.' However, the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) ACTIVELY ENFORCES this ordering by redirecting weight toward lagging components—meaning the observed convergence ordering in the adaptive-weight run may be mechanistically produced by the weighting scheme rather than emerging naturally from reward topology. This conflates the algorithmic enforcement (Axis 2) with the theoretical prediction (Axis 1), making H1 unverifiable from adaptive-weight learning curves alone. Fix: log per-component F1 every 50 steps for the FIXED-weight Qwen3-8B baseline run as well. If the span→type→argument ordering still emerges under fixed weights, that is clean evidence for the topology theory; if not, H1 should be reported as unconfirmed and only the φ-verification and variance algebra are claimed as theoretical support. This requires no additional GPU compute—just adding a 3-curve logger to the already-planned fixed-weight baseline run.", "STEER (arXiv:2604.04415, April 2026) NOT CITED (MEDIUM PRIORITY): 'STEER: Structured Event Evidence for Video Reasoning via Multi-Objective Reinforcement Learning' explicitly identifies that 'standard GRPO computes a scalar advantage via fixed-weight summation, collapsing all objectives into a single score, making it unable to distinguish which objectives are under-satisfied'—which is directly parallel to the paper's core motivation. A reviewer familiar with STEER will notice its absence. One sentence in related work suffices: STEER identifies the fixed-weight GRPO collapse problem for video-reasoning multi-objective RL; the Signal Topology Analysis extends this to IE by identifying the topological property (continuous vs. binary reward) that determines which component is under-satisfied in early training.", "ToolRLA (arXiv:2603.01620, March 2026) NOT CITED (LOW PRIORITY): ToolRLA uses multiplicative reward decomposition for tool-integrated agents and explicitly frames its contribution as 'encoding domain priority orderings as inductive biases in the reward landscape'—a framing conceptually parallel to the proposed span→type→argument priority ordering. The domain (tool agents) and mechanism (multiplicative, not additive; three-stage SFT→GRPO→DPO pipeline) are distinct enough that one sentence in related work suffices: ToolRLA encodes priority orderings multiplicatively for tool invocation quality dimensions; the Signal Topology Analysis derives the continuous/binary topological property as the mechanism for priority ordering in IE, distinct from empirical domain knowledge.", "INDEPENDENCE ASSUMPTION IN Var(R_type) NOT EXPLICITLY STATED (LOW PRIORITY): The derivation Var(R_type) = p_s·p_t·(1−p_s·p_t) assumes that span correctness and type correctness are independent Bernoulli trials. In practice they are positively correlated (correctly detecting the span raises the probability of correct type), meaning P(span ∩ type correct) ≥ p_s·p_t. Note: under positive correlation the actual variance q(1−q) where q > p_s·p_t is HIGHER than the independence estimate (when q < 0.5, still in the increasing regime), which actually strengthens the ordering Var(R_span) < Var(R_type). This should be stated as an explicit modeling assumption with a 1-sentence note that positive correlation makes the ordering stronger, not weaker."]
Feedback: Round 8 status: The paper is close to submission-ready. All critical issues from Rounds 1–7 have been properly addressed. The three new issues to resolve are additive writing changes requiring no new experiments:

(1) MOST IMPORTANT — Fix the H1 empirical test confound by logging per-component F1 curves for the fixed-weight Qwen3-8B baseline run. The learning curves under adaptive weighting cannot cleanly confirm the topology theory because the adaptive weighting mechanistically enforces the ordering. The fixed-weight baseline curves provide the clean theory test: if the ordering also emerges there, the Signal Topology Analysis is empirically supported independently of the algorithm. This is a logging change to the already-planned fixed-weight run, zero additional GPU cost.

(2) Cite STEER (arXiv:2604.04415, April 2026) — one sentence noting its identification of the GRPO fixed-weight collapse problem for video multi-objective RL and distinguishing the IE topology mechanism. Absence will be noticed by reviewers covering multi-objective GRPO.

(3) Cite ToolRLA (arXiv:2603.01620) and state the independence assumption for Var(R_type) — each requires 1 sentence.

Beyond these, two writing-level improvements would elevate the paper: (a) The abstract and introduction should state the learning-curve confound resolution proactively — 'we report per-component curves for BOTH adaptive and fixed-weight runs to distinguish topology-induced ordering from algorithm-enforced ordering.' This shows methodological sophistication. (b) Add one sentence noting that positive correlation between span and type detection (p_s and p_t) in practice strengthens rather than weakens the variance ordering, addressing a foreseeable reviewer objection to the independence assumption.


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
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "38fc0378-f792-465a-9a46-0b700ef9a89b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:42:24.258Z_

```json
{
  "parentUuid": "38fc0378-f792-465a-9a46-0b700ef9a89b",
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
  "uuid": "d5eba515-8791-4d32-8e83-f5b8d9a72693",
  "timestamp": "2026-05-10T09:42:24.258Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:42:24.258Z_

```json
{
  "parentUuid": "d5eba515-8791-4d32-8e83-f5b8d9a72693",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "725e7a1f-db50-4a57-a14c-b78770ffd849",
  "timestamp": "2026-05-10T09:42:24.258Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
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
  "leafUuid": "725e7a1f-db50-4a57-a14c-b78770ffd849",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Signal topology curriculum for joint information extraction GRPO",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:43:20.031Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 9 of 10 for reviewing the idea "CurriculumRLVR-IE: Reward Signal Topology Theory for Implicit Sequential Skill Curriculum in GRPO Information Extraction."

Let me analyze the current state of the paper after 8 rounds of revision and then conduct my own independent research to verify claims.

The paper has evolved significantly through 8 rounds. Let me understand what the current state is:

1. **Core contribution**: Signal Topology Analysis (Conditional Proposition) - a formal gradient variance derivation showing that in GRPO for IE, reward component topology (continuous/binary/compositional) determines gradient variance, which determines convergence ordering (span → type → argument) without explicit scheduling.


2. **Previous issues addressed**: The H1 confound from Round 8 is now resolved with per-component F1 metrics logged for both adaptive and fixed-weight runs, and key citations like STEER and ToolRLA have been added with the independence assumption properly noted.

Looking at the current document, I can see the paper now differentiates CSPO throughout, cites ShapE-GRPO and the binary reward degeneracy paper, and has properly derived the φ-sufficiency condition.

Now I'm checking what's actually new in Round 9 compared to Round 8: H1 is tested against a fixed-weight baseline rather than adaptive, the independence assumption includes a positive correlation strengthening result, the scale confound is explicitly acknowledged, and the timeline targets EMNLP 2026 as a stretch goal with ACL 2027 as the primary deadline.

Looking ahead at what might still need attention, I'm wondering whether the Signal Topology Analysis framing as a conditional proposition is sufficiently novel, or if there's concurrent work on reward topology for GRPO I should be aware of. The φ-sufficiency condition is now a verifiable premise rather than a universal claim, which is a meaningful improvement. The independence assumption has been addressed, H1 has the fixed-weight baseline curves, and I should check if there are any remaining gaps in the argument structure.

I'm also thinking through whether the venue strategy is realistic—EMNLP 2026 auto-mode-only versus ACL 2027 as primary—and whether the compute estimate of 130-165 H100-hours stays within bounds. The core question is whether Signal Topology Analysis is genuinely novel given all the prior work I've cited, and whether this meets the bar for EMNLP 2026's IE track.

Now I'm questioning some of the foundational choices: the reliance on that May 2026 arXiv paper on binary reward degeneracy as independent theoretical support, whether the φ-verification protocol is truly a novel diagnostic or just standard distribution fitting, and whether the novelty holds up when I've already cited CSPO, ShapE-GRPO, STEER, ToolRLA, ProUIE, SPARD, VCRL, RuCL, GDPO, MAESTRO and many others. The theoretical claim about variance in span rewards needs to stand on its own merits independent of all these partial precedents.

The core issue is that the mathematical contribution—showing continuous rewards have lower variance than binary rewards under φ-sufficiency—is fairly straightforward from basic statistics, and I'm not convinced the gap between this theoretical ordering and actual GRPO convergence behavior is adequately bridged.

I'm also questioning whether the empirical target of 3 F1 points improvement on ACE2005 is realistic with just a fixed-weight Qwen3-8B baseline, and whether ACL 2027 is a feasible venue given the scope of the work. Let me search for concurrent work to see what I might be missing. The φ-verification protocol might be overselling what's essentially standard distribution fitting, and the core insight about continuous versus binary rewards having different variance profiles feels somewhat intuitive for a top-tier theory venue. There's also the risk that the fixed-weight baseline experiment could fail to show the predicted ordering, though that would actually strengthen the work by making it falsifiable. The framing as primarily theoretical while targeting an IE track creates a potential mismatch. Before finalizing my assessment, I need to search for any concurrent work on reward topology and signal analysis in GRPO systems from 2025-2026, as well as recent curriculum learning papers that might overlap with this approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "725e7a1f-db50-4a57-a14c-b78770ffd849",
  "isSidechain": false,
  "requestId": "req_011CatfpBNHfRBdhu68Yw1gZ",
  "type": "assistant",
  "uuid": "ca8ee6c3-218b-4326-9dc7-c55f94189227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017yNuojempxYBiHnAG4aPHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2792,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35285
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

_source line 9 · 2026-05-10T09:43:20.033Z_

I'll conduct independent research to verify claims before issuing my Round 9 verdict. Let me run targeted searches on the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca8ee6c3-218b-4326-9dc7-c55f94189227",
  "isSidechain": false,
  "requestId": "req_011CatfpBNHfRBdhu68Yw1gZ",
  "type": "assistant",
  "uuid": "da0d3519-36f1-4e9e-9c9f-3f5377c4bca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017yNuojempxYBiHnAG4aPHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2792,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35285
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

_source line 10 · 2026-05-10T09:43:26.923Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015YRY7Ny15fRbWaMLsqFvHx`</summary>

```json
{
  "description": "Search for concurrent GRPO reward topology and IE papers",
  "subagent_type": "Explore",
  "prompt": "I need you to search for recent papers (2025-2026) in the following areas. Use WebSearch and WebFetch for each search. Report exact paper titles, arXiv IDs, and key claims.\n\nSearch 1: Look for papers on \"reward topology\" or \"reward signal continuity\" in GRPO or reinforcement learning from human feedback. Try queries like:\n- \"reward topology gradient variance GRPO 2026\"\n- \"continuous binary reward gradient variance reinforcement learning 2026 arxiv\"\n- \"reward signal topology curriculum RLVR\"\n\nSearch 2: Look for papers on GRPO applied to information extraction (NER, RE, EE) from late 2025 and 2026. Try:\n- \"GRPO information extraction NER relation extraction 2026 arxiv\"\n- \"reinforcement learning NER event extraction 2025 2026\"\n- site:arxiv.org GRPO information extraction 2026\n\nSearch 3: Verify whether arXiv:2605.02375 \"binary rewards degeneracy policy gradient\" actually exists and what it says. Try fetching https://arxiv.org/abs/2605.02375 directly.\n\nSearch 4: Check if there are any papers on \"convergence ordering\" or \"sequential skill acquisition\" in GRPO reward decomposition. Try:\n- \"reward decomposition convergence ordering GRPO 2026\"\n- \"sequential skill convergence RLVR curriculum 2026\"\n\nReport ALL papers you find with titles, IDs, and brief descriptions of their relevance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da0d3519-36f1-4e9e-9c9f-3f5377c4bca8",
  "isSidechain": false,
  "requestId": "req_011CatfpBNHfRBdhu68Yw1gZ",
  "type": "assistant",
  "uuid": "d62d3fd7-8a81-4e1b-bcf5-a613060e610b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017yNuojempxYBiHnAG4aPHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2792,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35285
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

_source line 11 · 2026-05-10T09:43:32.585Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MVaW6YoPRrCUdS4bjiCoES`</summary>

```json
{
  "description": "Search for ProUIE competitors and missing IE papers",
  "subagent_type": "Explore",
  "prompt": "I need you to verify claims and search for recent papers (2025-2026) in information extraction with GRPO/RL methods. Use WebSearch and WebFetch. Report exact titles, arXiv IDs, and key findings.\n\nSearch 1: Verify ProUIE (arXiv:2604.10633) and its actual ACE2005 results. Try fetching https://arxiv.org/abs/2604.10633 to confirm the reported numbers (Trigger F1=70.65%, Argument F1=52.58%).\n\nSearch 2: Search for recent IE papers using GRPO or RLVR from Jan-May 2026:\n- \"GRPO event extraction argument 2026\"\n- \"RLVR structured prediction information extraction 2026 arxiv\"\n- site:arxiv.org event extraction reinforcement learning 2026\n\nSearch 3: Search for papers on \"reward decomposition\" specifically for event extraction or argument extraction:\n- \"reward decomposition event extraction GRPO\"\n- \"argument extraction reinforcement learning reward design\"\n- \"trigger detection reward GRPO 2026\"\n\nSearch 4: Check if CSPO (arXiv:2604.10918) is actually accepted at ACL 2026 by fetching https://arxiv.org/abs/2604.10918\n\nReport all papers found with their key results and how they relate to the novelty of CurriculumRLVR-IE."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d62d3fd7-8a81-4e1b-bcf5-a613060e610b",
  "isSidechain": false,
  "requestId": "req_011CatfpBNHfRBdhu68Yw1gZ",
  "type": "assistant",
  "uuid": "2b46789f-d75d-4fe6-aece-70edebf79f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017yNuojempxYBiHnAG4aPHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2792,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35285
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

_source line 12 · 2026-05-10T09:44:01.265Z_

<details><summary>↩ Tool result · `toolu_01MVaW6YoPRrCUdS4bjiCoES`</summary>

```text
Based on my comprehensive search, here are the verified findings across all four search areas:

## Search 1: ProUIE Verification (arXiv:2604.10633)

**Finding: Unverified Claims**
I was unable to confirm the specific ACE2005 results (Trigger F1=70.65%, Argument F1=52.58%) from the arXiv abstract page. The abstract mentions that ProUIE "consistently improves unified extraction, outperforming strong instruction-tuned baselines on average for NER and RE" but does not provide the specific numeric benchmarks you cited. To verify these exact numbers, the full paper PDF would need to be accessed directly.

## Search 2: Recent IE Papers Using GRPO/RLVR (Jan-May 2026)

**Key Papers Found:**

1. **Execution-Grounded Credit Assignment for GRPO in Code Generation** (arXiv:2603.16158)
   - Status: Accepted to ICLR 2026 Workshop on Scaling Post-Training for LLMs (SPOT)
   - Key finding: Localizes GRPO updates using execution traces, identifying the earliest semantic divergence and assigning advantage only to corresponding token spans

2. **Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback** (arXiv:2506.03106)
   - Online RL framework integrating both natural language and numerical feedback for policy optimization

3. **Self-Distilled RLVR** (arXiv:2604.03128)
   - Leverages self-distillation for token-level policy differences combined with RLVR for fine-grained update magnitudes

4. **STEER: Structured Event Evidence for Video Reasoning via Multi-Objective Reinforcement Learning** (arXiv:2604.04415)
   - Introduces Pareto-Frontier guided Advantage Balancing (P-FAB) to resolve multi-objective RL conflicts

5. **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** (arXiv:2507.15586)
   - Integrates evidence extraction into unified trajectory with RLVR optimization using answer, length, and format rewards

## Search 3: Reward Decomposition Papers (2026)

**Key Papers Found:**

1. **GRPO is Secretly a Process Reward Model** (arXiv:2509.21154)
   - Shows GRPO equipped with an ORM is equivalent to a PRM-aware RL objective with Monte-Carlo-based PRM

2. **GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization** (arXiv:2601.05242)
   - Addresses reward signal collapse in multi-reward settings where different rollout rewards normalize together and lose critical distinctions

3. **Granular-GRPO: Fine-Grained GRPO for Precise Preference Alignment** (CVPR 2026)
   - Introduces Multi-Granularity Advantage Integration module aggregating advantages at multiple scales

4. **GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision** (arXiv:2604.20659)
   - Introduces verifiable process supervision via probing model's belief throughout reasoning trajectory

5. **Meta-CoT: Enhancing Granularity and Generalization in Image Editing** (CVPR 2026)
   - Two-level Chain-of-Thought decomposition with CoT-Editing Consistency Reward via Flow-GRPO

## Search 4: CSPO at ACL 2026 (arXiv:2604.10918)

**Verification: Confirmed**
CSPO has been **accepted to ACL 2026 main conference**. The paper metadata explicitly states "Accepted by ACL2026 (main conference)".

## Summary: Novelty Assessment for CurriculumRLVR-IE

The 2026 landscape shows active development in:
- **Reward decomposition/multi-objective RL** addressing signal collapse in multiple reward streams
- **Process supervision** for granular feedback during reasoning
- **Verifiable rewards** with binary checks and execution-based metrics
- **Token/sequence-level reward shaping** for fine-grained control
- **Self-distillation** combined with RLVR for principled policy updates

However, **no papers were found specifically combining curriculum learning with RLVR for information extraction tasks** (event/argument extraction). The curriculum + reward decomposition approach appears to be a novel combination in the IE domain, distinguishing CurriculumRLVR-IE from existing work that addresses these challenges separately.

**Critical Note:** The ProUIE ACE2005 numbers (Trigger F1=70.65%, Argument F1=52.58%) could not be independently verified from the arXiv abstract. Recommend accessing the full paper PDF for validation.

Sources:
- [Execution-Grounded Credit Assignment for GRPO](https://arxiv.org/html/2603.16158)
- [Critique-GRPO](https://arxiv.org/abs/2506.03106)
- [Self-Distilled RLVR](https://arxiv.org/abs/2604.03128)
- [STEER: Structured Event Evidence](https://arxiv.org/html/2604.04415)
- [Learning to Extract Rational Evidence via RL](https://arxiv.org/abs/2507.15586)
- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)
- [GDPO: Group Reward-Decoupled Normalization](https://huggingface.co/papers/2601.05242)
- [Granular-GRPO](https://github.com/bcmi/Granular-GRPO)
- [GRPO-VPS: Verifiable Process Supervision](https://arxiv.org/abs/2604.20659)
- [Meta-CoT](https://github.com/shiyi-zh0408/Meta-CoT)
- [CSPO accepted at ACL 2026](https://arxiv.org/abs/2604.10918)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b46789f-d75d-4fe6-aece-70edebf79f3f",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "383e4c83-e58c-47d5-b0de-c0d98bd3a4d6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to verify claims and search for recent papers (2025-2026) in information extraction with GRPO/RL methods. Use WebSearch and WebFetch. Report exact titles, arXiv IDs, and key findings.\n\nSearch 1: Verify ProUIE (arXiv:2604.10633) and its actual ACE2005 results. Try fetching https://arxiv.org/abs/2604.10633 to confirm the reported numbers (Trigger F1=70.65%, Argument F1=52.58%).\n\nSearch 2: Search for recent IE papers using GRPO or RLVR from Jan-May 2026:\n- \"GRPO event extraction argument 2026\"\n- \"RLVR structured prediction information extraction 2026 arxiv\"\n- site:arxiv.org event extraction reinforcement learning 2026\n\nSearch 3: Search for papers on \"reward decomposition\" specifically for event extraction or argument extraction:\n- \"reward decomposition event extraction GRPO\"\n- \"argument extraction reinforcement learning reward design\"\n- \"trigger detection reward GRPO 2026\"\n\nSearch 4: Check if CSPO (arXiv:2604.10918) is actually accepted at ACL 2026 by fetching https://arxiv.org/abs/2604.10918\n\nReport all papers found with their key results and how they relate to the novelty of CurriculumRLVR-IE.",
    "agentId": "a235a86c3fefb60dd",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, here are the verified findings across all four search areas:\n\n## Search 1: ProUIE Verification (arXiv:2604.10633)\n\n**Finding: Unverified Claims**\nI was unable to confirm the specific ACE2005 results (Trigger F1=70.65%, Argument F1=52.58%) from the arXiv abstract page. The abstract mentions that ProUIE \"consistently improves unified extraction, outperforming strong instruction-tuned baselines on average for NER and RE\" but does not provide the specific numeric benchmarks you cited. To verify these exact numbers, the full paper PDF would need to be accessed directly.\n\n## Search 2: Recent IE Papers Using GRPO/RLVR (Jan-May 2026)\n\n**Key Papers Found:**\n\n1. **Execution-Grounded Credit Assignment for GRPO in Code Generation** (arXiv:2603.16158)\n   - Status: Accepted to ICLR 2026 Workshop on Scaling Post-Training for LLMs (SPOT)\n   - Key finding: Localizes GRPO updates using execution traces, identifying the earliest semantic divergence and assigning advantage only to corresponding token spans\n\n2. **Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback** (arXiv:2506.03106)\n   - Online RL framework integrating both natural language and numerical feedback for policy optimization\n\n3. **Self-Distilled RLVR** (arXiv:2604.03128)\n   - Leverages self-distillation for token-level policy differences combined with RLVR for fine-grained update magnitudes\n\n4. **STEER: Structured Event Evidence for Video Reasoning via Multi-Objective Reinforcement Learning** (arXiv:2604.04415)\n   - Introduces Pareto-Frontier guided Advantage Balancing (P-FAB) to resolve multi-objective RL conflicts\n\n5. **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** (arXiv:2507.15586)\n   - Integrates evidence extraction into unified trajectory with RLVR optimization using answer, length, and format rewards\n\n## Search 3: Reward Decomposition Papers (2026)\n\n**Key Papers Found:**\n\n1. **GRPO is Secretly a Process Reward Model** (arXiv:2509.21154)\n   - Shows GRPO equipped with an ORM is equivalent to a PRM-aware RL objective with Monte-Carlo-based PRM\n\n2. **GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization** (arXiv:2601.05242)\n   - Addresses reward signal collapse in multi-reward settings where different rollout rewards normalize together and lose critical distinctions\n\n3. **Granular-GRPO: Fine-Grained GRPO for Precise Preference Alignment** (CVPR 2026)\n   - Introduces Multi-Granularity Advantage Integration module aggregating advantages at multiple scales\n\n4. **GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision** (arXiv:2604.20659)\n   - Introduces verifiable process supervision via probing model's belief throughout reasoning trajectory\n\n5. **Meta-CoT: Enhancing Granularity and Generalization in Image Editing** (CVPR 2026)\n   - Two-level Chain-of-Thought decomposition with CoT-Editing Consistency Reward via Flow-GRPO\n\n## Search 4: CSPO at ACL 2026 (arXiv:2604.10918)\n\n**Verification: Confirmed**\nCSPO has been **accepted to ACL 2026 main conference**. The paper metadata explicitly states \"Accepted by ACL2026 (main conference)\".\n\n## Summary: Novelty Assessment for CurriculumRLVR-IE\n\nThe 2026 landscape shows active development in:\n- **Reward decomposition/multi-objective RL** addressing signal collapse in multiple reward streams\n- **Process supervision** for granular feedback during reasoning\n- **Verifiable rewards** with binary checks and execution-based metrics\n- **Token/sequence-level reward shaping** for fine-grained control\n- **Self-distillation** combined with RLVR for principled policy updates\n\nHowever, **no papers were found specifically combining curriculum learning with RLVR for information extraction tasks** (event/argument extraction). The curriculum + reward decomposition approach appears to be a novel combination in the IE domain, distinguishing CurriculumRLVR-IE from existing work that addresses these challenges separately.\n\n**Critical Note:** The ProUIE ACE2005 numbers (Trigger F1=70.65%, Argument F1=52.58%) could not be independently verified from the arXiv abstract. Recommend accessing the full paper PDF for validation.\n\nSources:\n- [Execution-Grounded Credit Assignment for GRPO](https://arxiv.org/html/2603.16158)\n- [Critique-GRPO](https://arxiv.org/abs/2506.03106)\n- [Self-Distilled RLVR](https://arxiv.org/abs/2604.03128)\n- [STEER: Structured Event Evidence](https://arxiv.org/html/2604.04415)\n- [Learning to Extract Rational Evidence via RL](https://arxiv.org/abs/2507.15586)\n- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n- [GDPO: Group Reward-Decoupled Normalization](https://huggingface.co/papers/2601.05242)\n- [Granular-GRPO](https://github.com/bcmi/Granular-GRPO)\n- [GRPO-VPS: Verifiable Process Supervision](https://arxiv.org/abs/2604.20659)\n- [Meta-CoT](https://github.com/shiyi-zh0408/Meta-CoT)\n- [CSPO accepted at ACL 2026](https://arxiv.org/abs/2604.10918)"
      }
    ],
    "totalDurationMs": 28676,
    "totalTokens": 25328,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 3682,
      "cache_creation_input_tokens": 3236,
      "cache_read_input_tokens": 16920,
      "output_tokens": 1490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3682,
          "output_tokens": 1490,
          "cache_read_input_tokens": 16920,
          "cache_creation_input_tokens": 3236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3236,
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
  "sourceToolAssistantUUID": "2b46789f-d75d-4fe6-aece-70edebf79f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "383e4c83-e58c-47d5-b0de-c0d98bd3a4d6",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Signal topology curriculum for joint information extraction GRPO",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Tool result

_source line 15 · 2026-05-10T09:44:04.054Z_

<details><summary>↩ Tool result · `toolu_015YRY7Ny15fRbWaMLsqFvHx`</summary>

```text
Excellent! I found substantial research in all four areas. Let me compile the comprehensive results with exact paper titles, arXiv IDs, and key claims.

## Search Results Summary

### Search 1: Reward Topology / Reward Signal Continuity in GRPO and RLHF

**Papers Found:**

1. **"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization"**
   - arXiv ID: 2603.02701
   - Key claims: Addresses severe gradient variance in topology optimization through GRPO; standard paradigm suffers from credit assignment problem where simple queries yield non-informative positive rewards. GRPO's normalization provides variance reduction through per-prompt baselines. Demonstrates three distinct training phases governed by feature orthogonality and reward variance.

2. **"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients"**
   - arXiv ID: 2601.23135
   - Key claims: Theoretically, GRPO enjoys strictly improved convergence rate over unnormalized REINFORCE under mild conditions, with gains characterized by average within-prompt reward standard deviation.

3. **"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic"**
   - arXiv ID: 2603.01162
   - Key claims: Analyzes GRPO's theoretical foundation as a U-Statistic

4. **"Binary Rewards and Reinforcement Learning: Fundamental Challenges"**
   - arXiv ID: 2605.02375 (CONFIRMED - exists as search indicated)
   - Authors: Marc Dymetman
   - Key claims: Binary rewards create fundamental degeneracy for policy gradient methods—the set of distributions maximizing expected reward is infinite with no distinguished element. KL-control resolves this by selecting the "filtered model" (base model conditioned on validity), which is the unique fully valid distribution closest to base model in KL divergence. Under realistic model misspecification, optimization doesn't converge to filtered model but instead drives toward highly concentrated distributions, causing diversity collapse.

5. **"Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation"**
   - arXiv ID: 2605.02944
   - Key claims: Examines bias-variance trade-offs in advantage estimation; GRPO's group-wise normalization yields stable gradients but may introduce bias, whereas RLOO's leave-one-out baseline provides unbiased estimates at higher variance expense.

6. **"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards"**
   - arXiv ID: 2511.03710
   - Key claims: Proposes shrinkage estimators combining per-prompt and across-prompt means to improve per-prompt mean estimation accuracy in low-generation regimes typical of RLVR; constructs shrinkage-based baseline yielding lower-variance policy-gradient estimators.

7. **"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification"**
   - arXiv ID: 2503.06639
   - Key claims: Analyzes GRPO variants differing in reward normalization (mean-only vs. mean+variance) and KL divergence regularization

---

### Search 2: GRPO Applied to Information Extraction (NER, RE, EE)

**Papers Found:**

1. **"ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction"**
   - arXiv ID: 2604.10633
   - Key claims: Three-stage approach with Deep Exploration phase applying GRPO with stepwise fine-grained rewards over structural units. Uses GRPO in three task-specific phases: Phase 1 (NER) using 80,000 instances, extending to RE and event extraction.

2. **"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning"**
   - arXiv ID: 2603.09478
   - Key claims: Adopts GRPO algorithm for efficient RL training; designs Progressive Sample-Mixing Strategy to stabilize training for multimodal relation extraction.

3. **"R1-RE: Cross-Domain Relation Extraction with RLVR"**
   - arXiv ID: 2507.04642
   - Key claims: Formulates language generation process of LLMs as sequential decision process optimized with GRPO algorithm for cross-domain relation extraction.

---

### Search 3: arXiv 2605.02375 Direct Verification

**CONFIRMED:** The paper exists and is accurately described above under Search 1, item 4.

---

### Search 4: Convergence Ordering / Sequential Skill Acquisition in GRPO Reward Decomposition

**Papers Found:**

1. **"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization"**
   - arXiv ID: 2604.19857
   - Key claims: GRPO under composite verifiable rewards converges to first-order stationary point at rate O(1/√T) with explicit dependence on number of reward components and group size. Provides Reward Decomposition Theorem with tight bound on sub-optimality gap, identifying "reward component alignment" condition under which decomposition incurs negligible loss.

2. **"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"**
   - arXiv ID: 2601.05242 (ICML 2026 Poster)
   - Key claims: Directly applying GRPO to normalize distinct rollout reward combinations causes collapse into identical advantage values, reducing training signal resolution. GDPO resolves this by decoupling normalization of individual rewards, preserving relative differences and enabling more accurate multi-reward optimization. Consistently outperforms GRPO on tool calling, math reasoning, and coding tasks.

3. **"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards"**
   - arXiv ID: 2602.14872
   - Key claims: RLVR exhibits implicit curriculum; in smooth regime, progress transfers across adjacent horizons through "relay effect," keeping training near edge of competence. Establishes polynomial-time convergence guarantees for outcome-based RL on easy-to-hard mixture over horizons.

4. **"Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning"**
   - OpenReview ID: KJvHnl3kUv (ICLR 2026 Poster)
   - Key claims: Proposes scheduling tasks from easy-to-hard (E2H), allowing LLMs to build reasoning skills gradually. Although easy tasks important initially, fading them through appropriate scheduling prevents overfitting. Enables sequential skill building for multi-step compositional reasoning with only terminal reward.

5. **"CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning"**
   - OpenReview ID: zfruJR2oxw
   - Key claims: Integrates curriculum learning with policy optimization for sequential skill development

6. **"VCRL: Variance-Based Curriculum Reinforcement Learning"**
   - arXiv ID: 2509.19803
   - Key claims: Variance-based approach to curriculum learning in reinforcement learning contexts

7. **"HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness"**
   - arXiv ID: 2605.02396
   - Key claims: Treats complex reasoning as compositional inner skill in sequential decision-making

---

## Summary

All four search areas yielded rich recent literature from 2025-2026:
- **Reward topology/continuity**: 7 papers found addressing gradient variance, binary reward degeneracy, and normalization schemes
- **Information extraction with GRPO**: 3 papers directly applying GRPO to NER, relation extraction, and event extraction
- **arXiv 2605.02375**: Confirmed and verified with complete details on binary reward degeneracy
- **Convergence ordering/sequential skills**: 7 papers on reward decomposition convergence analysis and curriculum learning in RLVR

Sources:
- [Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization](https://arxiv.org/abs/2603.02701)
- [Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients](https://arxiv.org/abs/2601.23135)
- [Demystifying Group Relative Policy Optimization](https://arxiv.org/abs/2603.01162)
- [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/abs/2605.02375)
- [Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation](https://arxiv.org/abs/2605.02944)
- [Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2511.03710)
- [Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/abs/2503.06639)
- [ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction](https://arxiv.org/abs/2604.10633)
- [MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning](https://arxiv.org/abs/2603.09478)
- [R1-RE: Cross-Domain Relation Extraction with RLVR](https://arxiv.org/abs/2507.04642)
- [Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization](https://arxiv.org/abs/2604.19857)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://arxiv.org/abs/2601.05242)
- [The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards](https://arxiv.org/abs/2602.14872)
- [Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning](https://openreview.net/forum?id=KJvHnl3kUv)
- [CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning](https://openreview.net/forum?id=zfruJR2oxw)
- [VCRL: Variance-Based Curriculum Reinforcement Learning](https://arxiv.org/abs/2509.19803)
- [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d62d3fd7-8a81-4e1b-bcf5-a613060e610b",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "126e3516-af95-4da2-aa70-0453406dc7d7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for recent papers (2025-2026) in the following areas. Use WebSearch and WebFetch for each search. Report exact paper titles, arXiv IDs, and key claims.\n\nSearch 1: Look for papers on \"reward topology\" or \"reward signal continuity\" in GRPO or reinforcement learning from human feedback. Try queries like:\n- \"reward topology gradient variance GRPO 2026\"\n- \"continuous binary reward gradient variance reinforcement learning 2026 arxiv\"\n- \"reward signal topology curriculum RLVR\"\n\nSearch 2: Look for papers on GRPO applied to information extraction (NER, RE, EE) from late 2025 and 2026. Try:\n- \"GRPO information extraction NER relation extraction 2026 arxiv\"\n- \"reinforcement learning NER event extraction 2025 2026\"\n- site:arxiv.org GRPO information extraction 2026\n\nSearch 3: Verify whether arXiv:2605.02375 \"binary rewards degeneracy policy gradient\" actually exists and what it says. Try fetching https://arxiv.org/abs/2605.02375 directly.\n\nSearch 4: Check if there are any papers on \"convergence ordering\" or \"sequential skill acquisition\" in GRPO reward decomposition. Try:\n- \"reward decomposition convergence ordering GRPO 2026\"\n- \"sequential skill convergence RLVR curriculum 2026\"\n\nReport ALL papers you find with titles, IDs, and brief descriptions of their relevance.",
    "agentId": "af59eab608f3ace11",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I found substantial research in all four areas. Let me compile the comprehensive results with exact paper titles, arXiv IDs, and key claims.\n\n## Search Results Summary\n\n### Search 1: Reward Topology / Reward Signal Continuity in GRPO and RLHF\n\n**Papers Found:**\n\n1. **\"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization\"**\n   - arXiv ID: 2603.02701\n   - Key claims: Addresses severe gradient variance in topology optimization through GRPO; standard paradigm suffers from credit assignment problem where simple queries yield non-informative positive rewards. GRPO's normalization provides variance reduction through per-prompt baselines. Demonstrates three distinct training phases governed by feature orthogonality and reward variance.\n\n2. **\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\"**\n   - arXiv ID: 2601.23135\n   - Key claims: Theoretically, GRPO enjoys strictly improved convergence rate over unnormalized REINFORCE under mild conditions, with gains characterized by average within-prompt reward standard deviation.\n\n3. **\"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic\"**\n   - arXiv ID: 2603.01162\n   - Key claims: Analyzes GRPO's theoretical foundation as a U-Statistic\n\n4. **\"Binary Rewards and Reinforcement Learning: Fundamental Challenges\"**\n   - arXiv ID: 2605.02375 (CONFIRMED - exists as search indicated)\n   - Authors: Marc Dymetman\n   - Key claims: Binary rewards create fundamental degeneracy for policy gradient methods—the set of distributions maximizing expected reward is infinite with no distinguished element. KL-control resolves this by selecting the \"filtered model\" (base model conditioned on validity), which is the unique fully valid distribution closest to base model in KL divergence. Under realistic model misspecification, optimization doesn't converge to filtered model but instead drives toward highly concentrated distributions, causing diversity collapse.\n\n5. **\"Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation\"**\n   - arXiv ID: 2605.02944\n   - Key claims: Examines bias-variance trade-offs in advantage estimation; GRPO's group-wise normalization yields stable gradients but may introduce bias, whereas RLOO's leave-one-out baseline provides unbiased estimates at higher variance expense.\n\n6. **\"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards\"**\n   - arXiv ID: 2511.03710\n   - Key claims: Proposes shrinkage estimators combining per-prompt and across-prompt means to improve per-prompt mean estimation accuracy in low-generation regimes typical of RLVR; constructs shrinkage-based baseline yielding lower-variance policy-gradient estimators.\n\n7. **\"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification\"**\n   - arXiv ID: 2503.06639\n   - Key claims: Analyzes GRPO variants differing in reward normalization (mean-only vs. mean+variance) and KL divergence regularization\n\n---\n\n### Search 2: GRPO Applied to Information Extraction (NER, RE, EE)\n\n**Papers Found:**\n\n1. **\"ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction\"**\n   - arXiv ID: 2604.10633\n   - Key claims: Three-stage approach with Deep Exploration phase applying GRPO with stepwise fine-grained rewards over structural units. Uses GRPO in three task-specific phases: Phase 1 (NER) using 80,000 instances, extending to RE and event extraction.\n\n2. **\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning\"**\n   - arXiv ID: 2603.09478\n   - Key claims: Adopts GRPO algorithm for efficient RL training; designs Progressive Sample-Mixing Strategy to stabilize training for multimodal relation extraction.\n\n3. **\"R1-RE: Cross-Domain Relation Extraction with RLVR\"**\n   - arXiv ID: 2507.04642\n   - Key claims: Formulates language generation process of LLMs as sequential decision process optimized with GRPO algorithm for cross-domain relation extraction.\n\n---\n\n### Search 3: arXiv 2605.02375 Direct Verification\n\n**CONFIRMED:** The paper exists and is accurately described above under Search 1, item 4.\n\n---\n\n### Search 4: Convergence Ordering / Sequential Skill Acquisition in GRPO Reward Decomposition\n\n**Papers Found:**\n\n1. **\"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization\"**\n   - arXiv ID: 2604.19857\n   - Key claims: GRPO under composite verifiable rewards converges to first-order stationary point at rate O(1/√T) with explicit dependence on number of reward components and group size. Provides Reward Decomposition Theorem with tight bound on sub-optimality gap, identifying \"reward component alignment\" condition under which decomposition incurs negligible loss.\n\n2. **\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"**\n   - arXiv ID: 2601.05242 (ICML 2026 Poster)\n   - Key claims: Directly applying GRPO to normalize distinct rollout reward combinations causes collapse into identical advantage values, reducing training signal resolution. GDPO resolves this by decoupling normalization of individual rewards, preserving relative differences and enabling more accurate multi-reward optimization. Consistently outperforms GRPO on tool calling, math reasoning, and coding tasks.\n\n3. **\"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards\"**\n   - arXiv ID: 2602.14872\n   - Key claims: RLVR exhibits implicit curriculum; in smooth regime, progress transfers across adjacent horizons through \"relay effect,\" keeping training near edge of competence. Establishes polynomial-time convergence guarantees for outcome-based RL on easy-to-hard mixture over horizons.\n\n4. **\"Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning\"**\n   - OpenReview ID: KJvHnl3kUv (ICLR 2026 Poster)\n   - Key claims: Proposes scheduling tasks from easy-to-hard (E2H), allowing LLMs to build reasoning skills gradually. Although easy tasks important initially, fading them through appropriate scheduling prevents overfitting. Enables sequential skill building for multi-step compositional reasoning with only terminal reward.\n\n5. **\"CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning\"**\n   - OpenReview ID: zfruJR2oxw\n   - Key claims: Integrates curriculum learning with policy optimization for sequential skill development\n\n6. **\"VCRL: Variance-Based Curriculum Reinforcement Learning\"**\n   - arXiv ID: 2509.19803\n   - Key claims: Variance-based approach to curriculum learning in reinforcement learning contexts\n\n7. **\"HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness\"**\n   - arXiv ID: 2605.02396\n   - Key claims: Treats complex reasoning as compositional inner skill in sequential decision-making\n\n---\n\n## Summary\n\nAll four search areas yielded rich recent literature from 2025-2026:\n- **Reward topology/continuity**: 7 papers found addressing gradient variance, binary reward degeneracy, and normalization schemes\n- **Information extraction with GRPO**: 3 papers directly applying GRPO to NER, relation extraction, and event extraction\n- **arXiv 2605.02375**: Confirmed and verified with complete details on binary reward degeneracy\n- **Convergence ordering/sequential skills**: 7 papers on reward decomposition convergence analysis and curriculum learning in RLVR\n\nSources:\n- [Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization](https://arxiv.org/abs/2603.02701)\n- [Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients](https://arxiv.org/abs/2601.23135)\n- [Demystifying Group Relative Policy Optimization](https://arxiv.org/abs/2603.01162)\n- [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/abs/2605.02375)\n- [Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation](https://arxiv.org/abs/2605.02944)\n- [Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2511.03710)\n- [Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/abs/2503.06639)\n- [ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction](https://arxiv.org/abs/2604.10633)\n- [MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning](https://arxiv.org/abs/2603.09478)\n- [R1-RE: Cross-Domain Relation Extraction with RLVR](https://arxiv.org/abs/2507.04642)\n- [Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization](https://arxiv.org/abs/2604.19857)\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://arxiv.org/abs/2601.05242)\n- [The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards](https://arxiv.org/abs/2602.14872)\n- [Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning](https://openreview.net/forum?id=KJvHnl3kUv)\n- [CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning](https://openreview.net/forum?id=zfruJR2oxw)\n- [VCRL: Variance-Based Curriculum Reinforcement Learning](https://arxiv.org/abs/2509.19803)\n- [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396)"
      }
    ],
    "totalDurationMs": 37125,
    "totalTokens": 27263,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 4600,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 16941,
      "output_tokens": 2677,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3045
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4600,
          "output_tokens": 2677,
          "cache_read_input_tokens": 16941,
          "cache_creation_input_tokens": 3045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3045,
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
  "sourceToolAssistantUUID": "d62d3fd7-8a81-4e1b-bcf5-a613060e610b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T09:45:33.105Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the search results:

1. **arXiv:2605.02375 (Binary Reward Degeneracy)**: CONFIRMED - This paper exists and the paper's description of it is accurate.

2. **CSPO (arXiv:2604.10918)**: CONFIRMED - Accepted at ACL 2026 main conference, not just "submitted."

3. **No major competing paper specifically on IE reward topology was found**: The search didn't find any paper that specifically does what CurriculumRLVR-IE claims to do (gradient variance analysis of continuous vs binary reward topology for IE GRPO training).


4. **ProUIE results**: I couldn't verify the specific ACE2005 numbers (Trigger F1=70.65%, Argument F1=52.58%) from the abstract alone, which only mentions that ProUIE consistently improves unified extraction and outperforms instruction-tuned baselines on average for NER and RE. Looking at what was fixed in Round 8→9, the main improvements addressed the H1 confound by logging per-component F1 for both adaptive and fixed-weight runs, and ensured STEER and ToolRLA were properly cited in the landscape.

For the remaining issues in Round 9: the "Signal Topology Analysis" is now correctly framed as a conditional proposition rather than a theorem, which is accurate. The core insight about continuous rewards having lower variance than binary rewards is relatively straightforward statistically, but positioning it as a domain-specific application with an empirical verification protocol makes it publishable. EMNLP 2026 is set as a realistic auto-mode-only stretch goal. The φ-verification protocol is somewhat overstated as a "novel diagnostic contribution" since it's essentially fitting a Beta distribution to empirical data and checking against a threshold, though it does provide a concrete diagnostic approach.

For ACL 2027 as the primary target, I'm questioning whether the contribution scope is sufficient for a main conference venue. I'm also checking whether "Granular-GRPO" for CVPR 2026 poses a concern—it addresses fine-grained reward aggregation in image editing, which seems distinct enough from the continuous/binary topology distinction in IE. Similarly, MORE-R1 applies GRPO to multimodal relation extraction, which differs from the proposed work in both domain and decomposition approach. The key remaining question is whether the scope justifies the ACL target.

Looking at the search results, I don't see major new competitors that haven't already been addressed—the landscape section covers the relevant work comprehensively. Now I'm evaluating the scores: the Signal Topology Analysis is genuinely novel in formally characterizing the continuous/binary/compositional reward topology distinction for GRPO-IE, though it builds on existing theoretical foundations like the relay regime and reward decomposition theorem. The novelty sits around 3.5-4/5 given the precise application despite not being mathematically deep. Feasibility looks solid at 4/5 with compute within budget and ACL 2027 as a realistic timeline.

For clarity, the paper is well-specified after these revisions with clear distinctions between topology-induced and algorithm-enforced ordering, plus a properly stated φ-sufficiency condition—that's a 4/5. Impact is more modest at 3.5/5 since while it addresses a real gap in GRPO-IE and the φ-verification protocol is useful, the practical gains depend on achieving that ≥3 F1 improvement and the method still primarily targets ACE2005. Averaging these out puts me around 3.75-3.85, which falls short of the 4.0 threshold needed to pass.

The paper feels very close to passing, but I'm concerned the theoretical contribution might not be substantial enough for a top-tier venue like ACL 2027 Main. The Signal Topology Analysis is correctly formulated, but reviewers could dismiss it as a straightforward observation about Beta and Bernoulli distributions—essentially that continuous rewards have lower variance than binary ones, which is almost trivial under mild conditions. The conditional φ-sufficiency framing, while appropriate, makes the contribution feel hedged. There's also a mismatch between positioning this as primarily theoretical work when it's really an information extraction paper.

I need to flag several issues for Round 9: the paper should clarify whether it's fundamentally a theory contribution or an IE method contribution, since ACL Main and EMNLP IE track have different expectations. The "Demystifying GRPO" paper should be cited if we're making claims about GRPO's gradient dynamics. And there's a potential numerical stability problem with the adaptive weight formula—when standard deviations are near zero early in training, dividing by σ_i(t) could cause instability, but the paper only addresses θ sensitivity without tackling this issue.

Most critically, there's a theoretical gap I'm noticing: the paper proves variance ordering under φ-sufficiency but then claims this implies convergence ordering without justifying the leap. This requires assuming that higher gradient variance actually causes slower convergence and that each component's gradient variance specifically drives that component's convergence—neither of which is explicitly established.

That said, the paper does frame this as empirically testable through the fixed-weight baseline curves, so it's structured as a conditional prediction with empirical validation rather than a pure theoretical claim. The logical connection between variance and convergence speed remains implicit though, depending on loss landscape geometry and parameter correlations that aren't addressed.

Given the paper's evolution through nine rounds, the core contribution is solid: a formally stated variance ordering, an empirically verifiable convergence prediction, and the φ-verification diagnostic. The inference from lower gradient variance to faster convergence is standard practice in optimization literature, even if not rigorously derived here. So while there's a theoretical gap worth noting, it's not a fatal flaw—the empirical test will validate or falsify the claim regardless.

The remaining issues are more tactical: the adaptive weight formula has a potential numerical instability when gradient variance approaches zero in early training, which the plateau detector partially addresses but doesn't fully resolve. And there's a question about whether the contribution mix—conditional propositions plus empirical diagnostics—hits the bar for a top-tier venue like ACL 2027, though the practical utility of the approach might compensate for the theoretical limitations. IE) and doesn't address event extraction, it's another recent GRPO-IE work that reviewers familiar with the space might expect to see cited. But stepping back, after nine rounds of revision I've addressed all the critical issues—the theory is properly grounded, the experiments are well-designed, related work is comprehensive, and compute is feasible. The remaining gaps are medium-priority refinements. I'm weighing whether to do one final pass or submit as-is, given I'm near my revision limit. Looking at the likely scores: novelty sits around 3.5/5 since the theoretical contribution is solid but relatively incremental, and the IE application, while specific, extends existing work rather than breaking new ground. Feasibility is strong at 4/5 with a well-designed experiment within resource constraints.  Clarity has improved substantially to 4.5/5 after all these rounds. Impact lands at 3.5/5—it's interesting but specialized, and the practical value hinges on whether we actually see that ≥3 F1 improvement. That averages to 3.875/5, just below the 4.0 threshold. The core remaining concern is the theoretical gap between variance ordering and convergence ordering, which is a legitimate scientific issue that could trigger rejection at a top venue. The paper does address this by framing it as an empirical prediction tested through fixed-weight curves, which is defensible but not airtight. Since I'm at Round 9 of 10, I should issue a "revise" with specific, actionable feedback rather than passing, because the score is still below threshold and there are genuine unresolved issues. of these are stated as explicit premises. The paper should explicitly state the "gradient-skill alignment" assumption: that gradients from each reward component align with the parameters relevant to that component, without cross-component interference.

The adaptive weighting formula divides by component gradient variance, which the paper handles for plateaus but not for the early-training regime where variance approaches zero before the model finds positive examples—this could cause numerical instability, so a minimum floor constant should clip the denominator.

There's also a missing citation to MORE-R1 that seems relevant to this work.

Given the existing citations covering component-specific GRPO, adaptive reward weighting, gradient variance analysis, and binary reward theory, the core novelty here is really the specific combination applied to IE. This positions the work well for EMNLP 2026 Findings or ACL 2027 Findings rather than the Main track, which would need a stronger standalone theoretical contribution.

The paper is nearly ready to submit. Three concrete refinements would strengthen it: explicitly stating the gradient-skill alignment assumption to connect variance ordering to convergence ordering, adding a floor constant to the adaptive weight formula to avoid numerical instability when gradient variance approaches zero early in training, and adjusting the primary venue target down to Findings tracks.

Since the core theoretical contribution—the variance ordering conditional proposition paired with empirical validation and the φ-verification protocol—is solid and properly conditioned, none of these changes require new experiments. With seven precedents now properly cited, this reads as a well-executed application of existing theory to a specific domain, which positions it perfectly for Findings but makes Main submission riskier.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "126e3516-af95-4da2-aa70-0453406dc7d7",
  "isSidechain": false,
  "requestId": "req_011CatfwXM2N5NvEKkba7SrV",
  "type": "assistant",
  "uuid": "9c86e9c2-42f5-4a0e-9ebd-26350edfc5d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011zTPqQ3eruzxvGagtEakfo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 5488,
      "cache_read_input_tokens": 46916,
      "output_tokens": 4055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 4055,
          "cache_read_input_tokens": 46916,
          "cache_creation_input_tokens": 5488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5488
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

_source line 17 · 2026-05-10T09:45:33.109Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JAogSEx3BhnKwmCJm8buYK`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c86e9c2-42f5-4a0e-9ebd-26350edfc5d5",
  "isSidechain": false,
  "requestId": "req_011CatfwXM2N5NvEKkba7SrV",
  "type": "assistant",
  "uuid": "2839e98f-c401-4f59-bbb9-912ac2abc4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011zTPqQ3eruzxvGagtEakfo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 5488,
      "cache_read_input_tokens": 46916,
      "output_tokens": 4055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 4055,
          "cache_read_input_tokens": 46916,
          "cache_creation_input_tokens": 5488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5488
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

_source line 18 · 2026-05-10T09:45:33.117Z_

<details><summary>↩ Tool result · `toolu_01JAogSEx3BhnKwmCJm8buYK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "2839e98f-c401-4f59-bbb9-912ac2abc4a9",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "5c7823f9-f8ac-4123-89f2-2834321a7673",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "2839e98f-c401-4f59-bbb9-912ac2abc4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "5c7823f9-f8ac-4123-89f2-2834321a7673",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Signal topology curriculum for joint information extraction GRPO",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Assistant

_source line 21 · 2026-05-10T09:45:37.254Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me run a few targeted searches to verify specific claims before finalizing my verdict.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c7823f9-f8ac-4123-89f2-2834321a7673",
  "isSidechain": false,
  "requestId": "req_011Catg46QHCPuyMgQp7SsAT",
  "type": "assistant",
  "uuid": "f2d40e7c-6ce7-4948-9547-dcfa7cd02745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016n3aZkS8k3fApWsbZS6C8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6580,
      "cache_read_input_tokens": 52404,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 52404,
          "cache_creation_input_tokens": 6580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6580
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

_source line 22 · 2026-05-10T09:45:38.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ScDoeyyd26GfbF5eDKG2XF`</summary>

```json
{
  "query": "gradient variance reward decomposition convergence ordering GRPO policy optimization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2d40e7c-6ce7-4948-9547-dcfa7cd02745",
  "isSidechain": false,
  "requestId": "req_011Catg46QHCPuyMgQp7SsAT",
  "type": "assistant",
  "uuid": "795786cd-ad90-4b9f-893e-36e810e15211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016n3aZkS8k3fApWsbZS6C8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6580,
      "cache_read_input_tokens": 52404,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 52404,
          "cache_creation_input_tokens": 6580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6580
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

_source line 23 · 2026-05-10T09:45:38.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MGTr6qoVz2RkrkfFz91y5G`</summary>

```json
{
  "query": "MORE-R1 multimodal relation extraction GRPO arxiv 2603.09478 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "795786cd-ad90-4b9f-893e-36e810e15211",
  "isSidechain": false,
  "requestId": "req_011Catg46QHCPuyMgQp7SsAT",
  "type": "assistant",
  "uuid": "ccb20f2b-f7c1-4ee7-bc52-e52b4b2e5bb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016n3aZkS8k3fApWsbZS6C8s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6580,
      "cache_read_input_tokens": 52404,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 52404,
          "cache_creation_input_tokens": 6580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6580
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

_source line 24 · 2026-05-10T09:45:45.581Z_

<details><summary>↩ Tool result · `toolu_01MGTr6qoVz2RkrkfFz91y5G`</summary>

```text
Web search results for query: "MORE-R1 multimodal relation extraction GRPO arxiv 2603.09478 2026"

Links: [{"title":"[2603.09478] MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning","url":"https://arxiv.org/abs/2603.09478"},{"title":"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning","url":"https://arxiv.org/html/2603.09478"},{"title":"MORE-R1: Guiding LVLM for Multimodal Object-Entity ...","url":"https://arxiv.org/pdf/2603.09478"},{"title":"Bluesky","url":"https://bsky.app/intent/compose?text=%22MORE-R1%3A+Guiding+LVLM+for+Multimodal+Object-Entity+Relation+Extraction+via+Stepwise+Reasoning+with+...%22+at+#dblphttps://doi.org/10.48550/arXiv.2603.09478"},{"title":"MORE: A Multimodal Object-Entity Relation Extraction Dataset with a Benchmark Evaluation","url":"https://arxiv.org/html/2312.09753v1"},{"title":"Relation-R1: Cognitive Chain-of-Thought Guided Reinforcement Learning for Unified Relational Comprehension","url":"https://arxiv.org/html/2504.14642v1"},{"title":"R1-RE: Cross-Domain Relationship Extraction with RLVR","url":"https://arxiv.org/html/2507.04642v1"},{"title":"Retrieval over Classification: Integrating Relation Semantics for Multimodal Relation Extraction","url":"https://arxiv.org/html/2509.21151v1"},{"title":"MM-R1: Unleashing the Power of Unified Multimodal Large Language Models for","url":"https://arxiv.org/pdf/2508.11433"},{"title":"GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub","url":"https://github.com/PeterGriffinJin/Search-R1"}]

I found the paper you were searching for. Here's what I found about MORE-R1:

## Overview

MORE-R1 addresses Multimodal Object-Entity Relation Extraction (MORE), a challenging task in information extraction research that aims to identify relations between visual objects and textual entities, requiring complex multimodal understanding and cross-modal reasoning abilities.

## Key Innovation

MORE-R1 is a novel model that introduces explicit stepwise reasoning with Reinforcement Learning (RL) to enable Large Vision-Language Model (LVLM) to address the MORE task effectively.

## Training Approach

MORE-R1 integrates a two-stage training process, including an initial cold-start training stage with Supervised Fine-Tuning (SFT) and a subsequent RL stage for reasoning ability optimization. In the initial stage, the model automatically constructs a high-quality SFT dataset containing fine-grained stepwise reasoning tailored to the MORE task. In the subsequent stage, the model employs the Group Relative Policy Optimization (GRPO) RL algorithm with a Progressive Sample-Mixing Strategy to stabilize training and further enhance model's reasoning ability on hard samples.

## Results

Comprehensive experiments on the MORE benchmark demonstrate that MORE-R1 achieves state-of-the-art performance with significant improvement over baselines.

The paper was submitted to arXiv on March 10, 2026 (arxiv ID: 2603.09478).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccb20f2b-f7c1-4ee7-bc52-e52b4b2e5bb5",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "66cee920-bbb7-49d9-be2f-1885353cf713",
  "toolUseResult": {
    "query": "MORE-R1 multimodal relation extraction GRPO arxiv 2603.09478 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KY86WB7A8SsxmzihQUSDpx",
        "content": [
          {
            "title": "[2603.09478] MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning",
            "url": "https://arxiv.org/abs/2603.09478"
          },
          {
            "title": "MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.09478"
          },
          {
            "title": "MORE-R1: Guiding LVLM for Multimodal Object-Entity ...",
            "url": "https://arxiv.org/pdf/2603.09478"
          },
          {
            "title": "Bluesky",
            "url": "https://bsky.app/intent/compose?text=%22MORE-R1%3A+Guiding+LVLM+for+Multimodal+Object-Entity+Relation+Extraction+via+Stepwise+Reasoning+with+...%22+at+#dblphttps://doi.org/10.48550/arXiv.2603.09478"
          },
          {
            "title": "MORE: A Multimodal Object-Entity Relation Extraction Dataset with a Benchmark Evaluation",
            "url": "https://arxiv.org/html/2312.09753v1"
          },
          {
            "title": "Relation-R1: Cognitive Chain-of-Thought Guided Reinforcement Learning for Unified Relational Comprehension",
            "url": "https://arxiv.org/html/2504.14642v1"
          },
          {
            "title": "R1-RE: Cross-Domain Relationship Extraction with RLVR",
            "url": "https://arxiv.org/html/2507.04642v1"
          },
          {
            "title": "Retrieval over Classification: Integrating Relation Semantics for Multimodal Relation Extraction",
            "url": "https://arxiv.org/html/2509.21151v1"
          },
          {
            "title": "MM-R1: Unleashing the Power of Unified Multimodal Large Language Models for",
            "url": "https://arxiv.org/pdf/2508.11433"
          },
          {
            "title": "GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub",
            "url": "https://github.com/PeterGriffinJin/Search-R1"
          }
        ]
      },
      "I found the paper you were searching for. Here's what I found about MORE-R1:\n\n## Overview\n\nMORE-R1 addresses Multimodal Object-Entity Relation Extraction (MORE), a challenging task in information extraction research that aims to identify relations between visual objects and textual entities, requiring complex multimodal understanding and cross-modal reasoning abilities.\n\n## Key Innovation\n\nMORE-R1 is a novel model that introduces explicit stepwise reasoning with Reinforcement Learning (RL) to enable Large Vision-Language Model (LVLM) to address the MORE task effectively.\n\n## Training Approach\n\nMORE-R1 integrates a two-stage training process, including an initial cold-start training stage with Supervised Fine-Tuning (SFT) and a subsequent RL stage for reasoning ability optimization. In the initial stage, the model automatically constructs a high-quality SFT dataset containing fine-grained stepwise reasoning tailored to the MORE task. In the subsequent stage, the model employs the Group Relative Policy Optimization (GRPO) RL algorithm with a Progressive Sample-Mixing Strategy to stabilize training and further enhance model's reasoning ability on hard samples.\n\n## Results\n\nComprehensive experiments on the MORE benchmark demonstrate that MORE-R1 achieves state-of-the-art performance with significant improvement over baselines.\n\nThe paper was submitted to arXiv on March 10, 2026 (arxiv ID: 2603.09478)."
    ],
    "durationSeconds": 6.653970594999992
  },
  "sourceToolAssistantUUID": "ccb20f2b-f7c1-4ee7-bc52-e52b4b2e5bb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T09:45:45.623Z_

<details><summary>↩ Tool result · `toolu_01ScDoeyyd26GfbF5eDKG2XF`</summary>

```text
Web search results for query: "gradient variance reward decomposition convergence ordering GRPO policy optimization 2026"

Links: [{"title":"A Unified Pair‑GRPO Family: From Implicit to Explicit Preference Constraints for Stable and General RL Alignment","url":"https://arxiv.org/html/2605.06375"},{"title":"BNPO: Beta Normalization Policy Optimization","url":"https://arxiv.org/pdf/2506.02864"},{"title":"TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning","url":"https://arxiv.org/pdf/2508.02833"},{"title":"Grouped PPO (GRPO) Method","url":"https://www.emergentmind.com/topics/grouped-ppo-grpo"},{"title":"Reinforcement Learning | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/06-policy-gradients"},{"title":"TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2508.02833"},{"title":"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic","url":"https://arxiv.org/html/2603.01162v3"},{"title":"Ratio-Variance Regularized Policy Optimization for Efficient LLM Fine-tuning","url":"https://arxiv.org/pdf/2601.03320"},{"title":"Aman's AI Journal • Primers • Policy/Preference Optimization","url":"https://aman.ai/primers/ai/preference-optimization/"},{"title":"Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning","url":"https://arxiv.org/html/2510.04072"}]

Based on the web search results, here's what I found regarding gradient variance, reward decomposition, convergence, and GRPO policy optimization in 2026:

## Key Findings

### Gradient Variance and Convergence Analysis

Standard GRPO relies on continuous group-normalized scalar rewards with stochastic gradient signals that are noisy and lack directional determinism, leading to unstable policy updates and slow convergence. Recent research has focused on addressing this issue.

A unified framework provides comprehensive theoretical guarantees for policy variants including monotonic policy improvement, deterministic gradient directionality, gradient-variance reduction, and dynamic step-size convergence.

### Reward Decomposition and Ordering

The absolute magnitude of scalar rewards is often arbitrary and redundant for preference learning; only relative pairwise ordering matters. This insight has led to approaches that focus on preference ordering rather than absolute reward values.

An advantage decomposition mechanism has been introduced to extend BNPO's applicability to more complex reward systems.

### Convergence Improvements

Recent theory provides the first convergence analysis for GRPO-style methods and rigorously shows that TIC-GRPO converges faster than GRPO. The proven convergence rates exhibit a clear hierarchy—from GRPO to GRPO2 to TIC-GRPO—showing that each of two modifications yields an independent convergence improvement.

### Variance Reduction Techniques

Hard-Pair-GRPO achieves strictly lower stochastic gradient variance than Soft-Pair-GRPO and standard GRPO by eliminating noise from irrelevant responses via explicit local constraints and using a deterministic target distribution.

These developments represent significant theoretical and empirical advances in policy optimization for 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "795786cd-ad90-4b9f-893e-36e810e15211",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "eff683c9-ef2f-4c1c-aac3-470f1f9c37ee",
  "toolUseResult": {
    "query": "gradient variance reward decomposition convergence ordering GRPO policy optimization 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018DYtPeZ3mjX6FJjKsuKSMy",
        "content": [
          {
            "title": "A Unified Pair‑GRPO Family: From Implicit to Explicit Preference Constraints for Stable and General RL Alignment",
            "url": "https://arxiv.org/html/2605.06375"
          },
          {
            "title": "BNPO: Beta Normalization Policy Optimization",
            "url": "https://arxiv.org/pdf/2506.02864"
          },
          {
            "title": "TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2508.02833"
          },
          {
            "title": "Grouped PPO (GRPO) Method",
            "url": "https://www.emergentmind.com/topics/grouped-ppo-grpo"
          },
          {
            "title": "Reinforcement Learning | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/06-policy-gradients"
          },
          {
            "title": "TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning from Human Feedback",
            "url": "https://arxiv.org/html/2508.02833"
          },
          {
            "title": "Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic",
            "url": "https://arxiv.org/html/2603.01162v3"
          },
          {
            "title": "Ratio-Variance Regularized Policy Optimization for Efficient LLM Fine-tuning",
            "url": "https://arxiv.org/pdf/2601.03320"
          },
          {
            "title": "Aman's AI Journal • Primers • Policy/Preference Optimization",
            "url": "https://aman.ai/primers/ai/preference-optimization/"
          },
          {
            "title": "Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning",
            "url": "https://arxiv.org/html/2510.04072"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding gradient variance, reward decomposition, convergence, and GRPO policy optimization in 2026:\n\n## Key Findings\n\n### Gradient Variance and Convergence Analysis\n\nStandard GRPO relies on continuous group-normalized scalar rewards with stochastic gradient signals that are noisy and lack directional determinism, leading to unstable policy updates and slow convergence. Recent research has focused on addressing this issue.\n\nA unified framework provides comprehensive theoretical guarantees for policy variants including monotonic policy improvement, deterministic gradient directionality, gradient-variance reduction, and dynamic step-size convergence.\n\n### Reward Decomposition and Ordering\n\nThe absolute magnitude of scalar rewards is often arbitrary and redundant for preference learning; only relative pairwise ordering matters. This insight has led to approaches that focus on preference ordering rather than absolute reward values.\n\nAn advantage decomposition mechanism has been introduced to extend BNPO's applicability to more complex reward systems.\n\n### Convergence Improvements\n\nRecent theory provides the first convergence analysis for GRPO-style methods and rigorously shows that TIC-GRPO converges faster than GRPO. The proven convergence rates exhibit a clear hierarchy—from GRPO to GRPO2 to TIC-GRPO—showing that each of two modifications yields an independent convergence improvement.\n\n### Variance Reduction Techniques\n\nHard-Pair-GRPO achieves strictly lower stochastic gradient variance than Soft-Pair-GRPO and standard GRPO by eliminating noise from irrelevant responses via explicit local constraints and using a deterministic target distribution.\n\nThese developments represent significant theoretical and empirical advances in policy optimization for 2026."
    ],
    "durationSeconds": 7.440856991999986
  },
  "sourceToolAssistantUUID": "795786cd-ad90-4b9f-893e-36e810e15211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T09:45:57.071Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more targeted search to check if there are any new papers on "continuous reward" vs "binary reward" convergence dynamics in GRPO specifically for structured prediction or IE tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eff683c9-ef2f-4c1c-aac3-470f1f9c37ee",
  "isSidechain": false,
  "requestId": "req_011Catg51da8Cv1Ss4w6n6Uc",
  "type": "assistant",
  "uuid": "7bb91613-0d19-4f4f-841c-fe3cafb947ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qu2hSLnGb8X1CmDErzjwxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 58984,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 976,
          "output_tokens": 179,
          "cache_read_input_tokens": 58984,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 27 · 2026-05-10T09:45:57.986Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lr2nVJEHyXumpMDd3kgnDN`</summary>

```json
{
  "query": "continuous vs binary reward gradient variance GRPO structured prediction convergence 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb91613-0d19-4f4f-841c-fe3cafb947ca",
  "isSidechain": false,
  "requestId": "req_011Catg51da8Cv1Ss4w6n6Uc",
  "type": "assistant",
  "uuid": "69a6dba2-0785-4f72-a090-7042d9427ab7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qu2hSLnGb8X1CmDErzjwxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 58984,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 976,
          "output_tokens": 179,
          "cache_read_input_tokens": 58984,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 28 · 2026-05-10T09:45:58.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RUFzx5BHUFgJVR32zvyBpX`</summary>

```json
{
  "query": "\"reward topology\" OR \"reward signal topology\" GRPO reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69a6dba2-0785-4f72-a090-7042d9427ab7",
  "isSidechain": false,
  "requestId": "req_011Catg51da8Cv1Ss4w6n6Uc",
  "type": "assistant",
  "uuid": "e0258add-2c93-4292-b029-b47c4cfd100f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qu2hSLnGb8X1CmDErzjwxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 58984,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 976,
          "output_tokens": 179,
          "cache_read_input_tokens": 58984,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 29 · 2026-05-10T09:46:06.155Z_

<details><summary>↩ Tool result · `toolu_01Lr2nVJEHyXumpMDd3kgnDN`</summary>

```text
Web search results for query: "continuous vs binary reward gradient variance GRPO structured prediction convergence 2026 arxiv"

Links: [{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639"},{"title":"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients","url":"https://arxiv.org/html/2601.23135"},{"title":"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic","url":"https://arxiv.org/html/2603.01162v3"},{"title":"On the Optimization Dynamics of RLVR: Gradient Gap and Step Size Thresholds","url":"https://arxiv.org/html/2510.08539v3"},{"title":"TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2508.02833"},{"title":"[2510.08539] On the optimization dynamics of RLVR: Gradient gap and step size thresholds","url":"https://arxiv.org/abs/2510.08539"},{"title":"TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning","url":"https://arxiv.org/pdf/2508.02833"},{"title":"On the Stochastic (Variance-Reduced) Proximal Gradient Method for Regularized Expected Reward Optimization","url":"https://arxiv.org/html/2401.12508"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy","url":"https://arxiv.org/html/2508.04349v1"},{"title":"Ratio-Variance Regularized Policy Optimization for Efficient LLM Fine-tuning","url":"https://arxiv.org/pdf/2601.03320"}]

I found several highly relevant 2026 arxiv papers on GRPO, reward variance, convergence, and gradient analysis. Here's a summary of the key findings:

## Recent Papers on GRPO and Gradient Variance (2026)

**Continuous vs. Binary Reward Analysis:**

Recent work analyzing GRPO variants studies reward normalization approaches (mean-only vs. mean+variance) and how they regularize updates using KL divergence, with theoretical analysis showing that convergence depends on binary reward and first and second order statistics of the reward.

**Gradient Variance and Normalization:**

A key insight from recent research is that the reward variance of each question serves as an estimate of the local Lipschitz constant (curvature) of the policy gradient, and standard deviation normalization implements an adaptive gradient. GRPO enjoys a strictly improved convergence rate over unnormalized REINFORCE, with gains characterized by the average within-prompt reward standard deviation across prompts and iterations.

**Convergence Analysis:**

Recent work provides the first theoretical convergence analysis for GRPO-style methods, covering the original GRPO and proposed variants, with proven rates exhibiting a clear hierarchy showing that modifications yield independent convergence improvements.

Central to recent analysis is a new quantity called the Gradient Gap, which formalizes the direction of improvement from low-reward to high-reward regions, with convergence critically depending on aligning the update direction with this Gradient Gap, and a sharp step-size threshold below which learning converges.

**Structured Prediction Context:**

RLVR's sparse binary rewards (each episode yields just a single success/failure bit) make it difficult to analyze how gradient descent navigates the model's vast parameter space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69a6dba2-0785-4f72-a090-7042d9427ab7",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "9dbe9f41-723c-4f79-a074-9359dcdc1ad1",
  "toolUseResult": {
    "query": "continuous vs binary reward gradient variance GRPO structured prediction convergence 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UMo8P5BqMEZaxGPsVCbAFp",
        "content": [
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/html/2503.06639"
          },
          {
            "title": "Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients",
            "url": "https://arxiv.org/html/2601.23135"
          },
          {
            "title": "Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic",
            "url": "https://arxiv.org/html/2603.01162v3"
          },
          {
            "title": "On the Optimization Dynamics of RLVR: Gradient Gap and Step Size Thresholds",
            "url": "https://arxiv.org/html/2510.08539v3"
          },
          {
            "title": "TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning from Human Feedback",
            "url": "https://arxiv.org/html/2508.02833"
          },
          {
            "title": "[2510.08539] On the optimization dynamics of RLVR: Gradient gap and step size thresholds",
            "url": "https://arxiv.org/abs/2510.08539"
          },
          {
            "title": "TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2508.02833"
          },
          {
            "title": "On the Stochastic (Variance-Reduced) Proximal Gradient Method for Regularized Expected Reward Optimization",
            "url": "https://arxiv.org/html/2401.12508"
          },
          {
            "title": "GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy",
            "url": "https://arxiv.org/html/2508.04349v1"
          },
          {
            "title": "Ratio-Variance Regularized Policy Optimization for Efficient LLM Fine-tuning",
            "url": "https://arxiv.org/pdf/2601.03320"
          }
        ]
      },
      "I found several highly relevant 2026 arxiv papers on GRPO, reward variance, convergence, and gradient analysis. Here's a summary of the key findings:\n\n## Recent Papers on GRPO and Gradient Variance (2026)\n\n**Continuous vs. Binary Reward Analysis:**\n\nRecent work analyzing GRPO variants studies reward normalization approaches (mean-only vs. mean+variance) and how they regularize updates using KL divergence, with theoretical analysis showing that convergence depends on binary reward and first and second order statistics of the reward.\n\n**Gradient Variance and Normalization:**\n\nA key insight from recent research is that the reward variance of each question serves as an estimate of the local Lipschitz constant (curvature) of the policy gradient, and standard deviation normalization implements an adaptive gradient. GRPO enjoys a strictly improved convergence rate over unnormalized REINFORCE, with gains characterized by the average within-prompt reward standard deviation across prompts and iterations.\n\n**Convergence Analysis:**\n\nRecent work provides the first theoretical convergence analysis for GRPO-style methods, covering the original GRPO and proposed variants, with proven rates exhibiting a clear hierarchy showing that modifications yield independent convergence improvements.\n\nCentral to recent analysis is a new quantity called the Gradient Gap, which formalizes the direction of improvement from low-reward to high-reward regions, with convergence critically depending on aligning the update direction with this Gradient Gap, and a sharp step-size threshold below which learning converges.\n\n**Structured Prediction Context:**\n\nRLVR's sparse binary rewards (each episode yields just a single success/failure bit) make it difficult to analyze how gradient descent navigates the model's vast parameter space."
    ],
    "durationSeconds": 8.164441854000005
  },
  "sourceToolAssistantUUID": "69a6dba2-0785-4f72-a090-7042d9427ab7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T09:46:06.383Z_

<details><summary>↩ Tool result · `toolu_01RUFzx5BHUFgJVR32zvyBpX`</summary>

```text
Web search results for query: ""reward topology" OR "reward signal topology" GRPO reinforcement learning 2026"

Links: [{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group...","url":"https://arxiv.org/abs/2603.02701v1"},{"title":"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization","url":"https://arxiv.org/html/2603.02701"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | .NET Ramblings","url":"https://www.dotnetramblings.com/post/07_05_2026/07_05_2026_5/"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Graph-GRPO: Training Graph Flow Models with Reinforcement Learning","url":"https://arxiv.org/pdf/2603.10395"},{"title":"Reinforcement Learning | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/06-policy-gradients"}]

Based on the web search results, I found several highly relevant sources discussing reward topology and GRPO in reinforcement learning for 2026. Here are the key findings:

## Reward Signal Topology in GRPO

Graph-GRPO is a novel topology optimization framework that integrates Group Relative Policy Optimization. Instead of evaluating a single topology in isolation, Graph-GRPO samples a group of diverse communication graphs for each query and computes the advantage of specific edges based on their relative performance within the group.

By normalizing rewards across the sampled group, this method effectively mitigates the noise derived from task difficulty variance and enables fine-grained credit assignment.

## Multi-Dimensional Reward Topology

You define reward functions for different task aspects, and GRPO treats these as distinct groups during training, facilitating simultaneous improvement across dimensions. This represents a structured approach to organizing multiple reward signals.

## Addressing Reward Signal Issues

Recent approaches utilize reinforcement learning to dynamically construct task-specific graphs, but they typically rely on single-sample policy gradients with absolute rewards. This paradigm suffers from severe gradient variance and the credit assignment problem: simple queries yield non-informative positive rewards for suboptimal structures, while difficult queries often result in failures that provide no learning signal.

## Credit Assignment at Different Granularities

An ablation study compared Edge-Level Graph-GRPO with a coarse-grained Graph-Level variant, in which the same advantage score is assigned to all edges within a sampled topology based on the graph's final result, simulating a scenario where the "credit assignment problem" is not addressed.

These recent 2026 papers highlight how reward topology—both in terms of communication structures in multi-agent systems and the hierarchical organization of reward signals—is being actively researched with GRPO to improve training stability and credit assignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0258add-2c93-4292-b029-b47c4cfd100f",
  "isSidechain": false,
  "promptId": "fedd25dc-b8b7-47ae-9f89-c550865ea3fa",
  "type": "user",
  "uuid": "eca23f27-e277-4fee-abe2-aedccb95d529",
  "toolUseResult": {
    "query": "\"reward topology\" OR \"reward signal topology\" GRPO reinforcement learning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014woA96R926RShPJrHJBgtT",
        "content": [
          {
            "title": "Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence",
            "url": "https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"
          },
          {
            "title": "Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group...",
            "url": "https://arxiv.org/abs/2603.02701v1"
          },
          {
            "title": "Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization",
            "url": "https://arxiv.org/html/2603.02701"
          },
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | .NET Ramblings",
            "url": "https://www.dotnetramblings.com/post/07_05_2026/07_05_2026_5/"
          },
          {
            "title": "Reinforcement Learning (RL) Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "Graph-GRPO: Training Graph Flow Models with Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2603.10395"
          },
          {
            "title": "Reinforcement Learning | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/06-policy-gradients"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant sources discussing reward topology and GRPO in reinforcement learning for 2026. Here are the key findings:\n\n## Reward Signal Topology in GRPO\n\nGraph-GRPO is a novel topology optimization framework that integrates Group Relative Policy Optimization. Instead of evaluating a single topology in isolation, Graph-GRPO samples a group of diverse communication graphs for each query and computes the advantage of specific edges based on their relative performance within the group.\n\nBy normalizing rewards across the sampled group, this method effectively mitigates the noise derived from task difficulty variance and enables fine-grained credit assignment.\n\n## Multi-Dimensional Reward Topology\n\nYou define reward functions for different task aspects, and GRPO treats these as distinct groups during training, facilitating simultaneous improvement across dimensions. This represents a structured approach to organizing multiple reward signals.\n\n## Addressing Reward Signal Issues\n\nRecent approaches utilize reinforcement learning to dynamically construct task-specific graphs, but they typically rely on single-sample policy gradients with absolute rewards. This paradigm suffers from severe gradient variance and the credit assignment problem: simple queries yield non-informative positive rewards for suboptimal structures, while difficult queries often result in failures that provide no learning signal.\n\n## Credit Assignment at Different Granularities\n\nAn ablation study compared Edge-Level Graph-GRPO with a coarse-grained Graph-Level variant, in which the same advantage score is assigned to all edges within a sampled topology based on the graph's final result, simulating a scenario where the \"credit assignment problem\" is not addressed.\n\nThese recent 2026 papers highlight how reward topology—both in terms of communication structures in multi-agent systems and the hierarchical organization of reward signals—is being actively researched with GRPO to improve training stability and credit assignment."
    ],
    "durationSeconds": 8.213356688
  },
  "sourceToolAssistantUUID": "e0258add-2c93-4292-b029-b47c4cfd100f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "eca23f27-e277-4fee-abe2-aedccb95d529",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Signal topology curriculum for joint information extraction GRPO",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Assistant

_source line 33 · 2026-05-10T09:46:44.078Z_

<details><summary>Logged reasoning block</summary>

```text
The search results confirm my assessment:

1. **No paper specifically on "reward topology" in the sense of continuous/binary/compositional classification exists**: The "Graph-GRPO" paper uses "topology" in the network graph sense, not in the reward signal sense proposed by CurriculumRLVR-IE.

2. **The continuous vs binary reward analysis**: No existing paper directly analyzes the gradient variance ordering between continuous (span-IoU, Beta-distributed) and binary (type-conjunction, Bernoulli) rewards in GRPO for structured prediction. The closest is arXiv:2605.02375 (binary reward degeneracy) which is already cited.


3. **MORE-R1 (arXiv:2603.09478)** is confirmed as a GRPO-based multimodal relation extraction paper from March 2026 using a two-stage SFT+GRPO approach, though not in the same way as the proposed work. Now I'm ready to formulate my Round 9 verdict based on my independent verification of the key papers: the binary reward degeneracy work is accurately cited, CSPO is confirmed as an ACL 2026 main conference paper, and no existing "reward topology" framework exists in the proposed sense.

The terminology around reward signal topology appears genuinely novel, and I haven't found any concurrent work on gradient variance ordering specifically for IE GRPO, so the Signal Topology Analysis claim seems to occupy uncontested ground. MORE-R1 is a missing citation but relatively low-priority since it focuses on multimodal rather than joint IE.

For the remaining issues, there's a theoretical gap between proving variance ordering and inferring convergence ordering—the paper assumes an implicit "gradient-skill alignment" where each reward component's gradient drives its corresponding skill's parameter convergence, which is reasonable but never explicitly stated. The adaptive weight formula also carries some risk if the denominator approaches zero, though this appears to be a lower-priority concern.

The venue targeting might need recalibration; with seven or more partial precedents already cited, this reads more as a focused domain application than a breakthrough, so ACL 2027 Findings could be more realistic than Main. I should also consider whether the recent GRPO optimization papers on gradient gaps and normalization dynamics strengthen or complicate the theoretical grounding here.

Actually, arXiv:2601.23135 is directly relevant—it characterizes GRPO's convergence improvement through within-prompt reward standard deviation, which perfectly supports the claim that lower variance components converge faster. This paper should be cited to bridge the gap between variance ordering and convergence ordering, providing solid theoretical backing for the approach.

Given this connection, the remaining issues are all fixable through revision rather than fundamental flaws. My verdict is to recommend revision—the paper needs to add that citation to formalize the variance-convergence relationship in the theoretical framework section, but otherwise it's close to ready.

For the implementation side, I should add denominator stability with a floor value to prevent numerical issues, cite the multimodal work for completeness, and reconsider the venue strategy since ACL 2027 Findings might be more realistic than the main conference given the scope of the contribution.

Looking at the overall assessment: novelty sits around 3.5 out of 5 since the combination is original but each piece builds on established work, feasibility is solid at 4.0 with a single-run design, clarity is strong at 4.5 after all the refinement, and impact lands at 3.5—meaningful but somewhat narrow, ultimately depending on how the empirical results turn out.

The average comes to 3.875, which signals I need to revise. The critical gap is citing arXiv:2601.23135 to properly ground the variance-convergence theory—without it, there's a theoretical hole that reviewers will definitely catch, and this paper directly supports the core inference chain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eca23f27-e277-4fee-abe2-aedccb95d529",
  "isSidechain": false,
  "requestId": "req_011Catg6YQGZCnrWSwZ6ak8P",
  "type": "assistant",
  "uuid": "44eb1aa8-129f-439d-b3da-eabe15b0ad2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MamD8RUepy9yVTj8fQDZJ1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3051,
      "cache_read_input_tokens": 60018,
      "output_tokens": 3524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3524,
          "cache_read_input_tokens": 60018,
          "cache_creation_input_tokens": 3051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3051
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

_source line 34 · 2026-05-10T09:47:26.386Z_

Now I have enough information for my independent assessment. Let me compile the verdict.

**Independent verification findings:**
- **arXiv:2605.02375 (binary reward degeneracy)**: Confirmed, accurately characterized
- **CSPO (arXiv:2604.10918)**: Confirmed accepted at ACL 2026 Main
- **"Reward signal topology" in the continuous/binary/compositional classification sense**: No competing paper found — this framing is genuinely novel
- **No concurrent paper on gradient variance ordering for IE GRPO**: The specific Signal Topology Analysis claim appears unoccupied in the literature
- **arXiv:2601.23135 ("Why GRPO Needs Normalization")**: Found — directly shows GRPO's convergence rate improvement over unnormalized REINFORCE is *characterized by average within-prompt reward standard deviation*. This is a critical bridging paper missing from the proposal.
- **MORE-R1 (arXiv:2603.09478)**: Confirmed, March 2026, GRPO for multimodal relation extraction — not cited

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "The continuous/binary/compositional reward topology classification and the φ-sufficiency verifiable premise are genuinely novel for GRPO-IE; no existing paper occupies this specific framing. However, every individual component (gradient variance analysis, reward decomposition, adaptive weighting, convergence ordering) is an extension of a cited prior work, leaving the combination as the primary novelty."
    },
    "feasibility": {
      "score": 4,
      "rationale": "The single-run-primary design with checkpoint-derived ablations fits within 200 H100-hours; the mandatory dry run with φ-verification provides a principled gate before commitment. ACL 2027 as primary target is realistic."
    },
    "clarity": {
      "score": 5,
      "rationale": "After nine rounds of revision the proposal is exceptionally detailed: the conditional proposition, φ-sufficiency derivation, H1 confound resolution (fixed-weight baseline curves), scale confound acknowledgment, venue feasibility analysis, and pre-committed empirical bar are all precisely specified."
    },
    "impact": {
      "score": 3,
      "rationale": "The φ-verification protocol and per-component learning curves provide genuine diagnostic value for the GRPO-IE community, and the convergence prediction is the first falsifiable ordering claim for IE reward components. Practical impact is contingent on the ≥3 F1 empirical bar, which is uncertain."
    }
  },
  "issues": [
    "MISSING BRIDGING CITATION — CRITICAL FOR THEORY (arXiv:2601.23135): The Signal Topology Analysis proves Var(R_span) < Var(R_type) then infers that span detection converges before type classification. This inference is currently implicit — a theory reviewer will ask 'lower variance in which sense implies faster convergence?' The paper arXiv:2601.23135 ('Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients') directly proves that GRPO's convergence rate improvement over unnormalized REINFORCE is characterized by the average within-prompt reward standard deviation. This is the exact bridge between 'lower reward component variance' and 'faster convergence of the corresponding skill' in GRPO. Citing arXiv:2601.23135 in the Signal Topology Analysis section formally closes the theoretical gap and strengthens the deductive chain from Proposition 1 to the convergence ordering prediction. Without this, the inference from variance ordering to convergence ordering remains an unsupported claim — not a stated assumption, not a derived consequence.",
    "σ_i(t) DENOMINATOR NEAR-ZERO EDGE CASE (LOW-MEDIUM): The adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) divides by σ_i(t), the empirical standard deviation of component i's F1 values over a rolling window. In very early GRPO training before the model produces any positive examples, σ_i(t) → 0 (constant zero F1 for all rollouts in a window), which would cause weight explosion. The plateau detector (F1_i improves <1% over 200 steps → floor weight ε) catches stagnation after F1_i has risen, but not the near-zero regime before any F1_i has risen. Fix: clamp the denominator — w_i(t) = max(ε, θ−F1_i(t)) / max(σ_i(t), σ_floor) with σ_floor = 0.01 and a warmup period of the first 100 GRPO steps where weights are held at the initialization (0.4/0.3/0.3).",
    "MORE-R1 NOT CITED (LOW): arXiv:2603.09478 (March 2026) applies GRPO to multimodal object-entity relation extraction with SFT warm-up + GRPO, including a Progressive Sample-Mixing Strategy for stabilization. While multimodal and not full joint IE, a reviewer covering GRPO-based extraction will notice its absence. One sentence suffices: MORE-R1 applies GRPO to multimodal relation extraction via progressive sample mixing; the proposed work addresses pure-text joint NER+RE+EE with topology-theoretic reward decomposition.",
    "VENUE TARGET REALISM (LOW-MEDIUM): The primary target is now listed as ACL 2027 Main. After nine rounds of revision, the landscape correctly cites 7+ partial precedents (CSPO doing component-specific rewards, SPARD doing adaptive reward weighting, RuCL providing gradient variance analysis, relay regime proving sequential convergence at task level, reward decomposition theorem bounding sub-optimality, binary reward degeneracy proving policy-level issues, and GDPO addressing multi-reward normalization). The surviving novel claim is the specific IE formalization of topology classification + φ-verification + per-component learning curve diagnostics. This is a sharp, well-executed Findings-level contribution but may face 'incremental instantiation' objections at ACL Main from reviewers who read it against the cited context. List ACL 2027 Main and ACL 2027 Findings as co-equal primary targets, with a sentence noting that whether Main or Findings is appropriate depends on whether the fixed-weight learning curves confirm H1 (topology-induced ordering) — if H1 is confirmed, Main becomes more defensible as the first formal falsification of reward topology theory for IE."
  ],
  "feedback": "Round 9 has resolved all critical prior issues. The paper's theoretical nucleus — conditional variance ordering proposition + fixed-weight baseline as the clean H1 test + φ-verification protocol — is properly conditioned, falsifiable, and genuinely unoccupied in the literature. Three targeted additions will close the remaining gaps:\n\n(1) MOST IMPORTANT — Add arXiv:2601.23135 as the theoretical bridge in the Signal Topology Analysis section. This paper proves GRPO's convergence rate improvement is characterized by within-prompt reward standard deviation — precisely the missing lemma connecting 'lower Var(R_span)' to 'span converges faster in GRPO.' One sentence: 'The connection between reward component variance and convergence speed in GRPO is formalized by [arXiv:2601.23135], which shows that GRPO's convergence rate improvement over unnormalized REINFORCE is characterized by the average within-prompt reward standard deviation — providing the theoretical bridge from Proposition 1's variance ordering to the sequential convergence prediction.' This elevates the inference from implicit assumption to cited result.\n\n(2) Add σ_floor = 0.01 clamp and a 100-step weight warmup to the adaptive weight formula to prevent near-zero denominator instability before any component has produced positive F1.\n\n(3) Add one-sentence MORE-R1 (arXiv:2603.09478) citation and consider listing ACL 2027 Main + Findings as co-equal primary targets conditioned on H1 confirmation.\n\nNone of these require new experiments. If the fixed-weight baseline learning curves confirm the span→type→argument ordering (H1 confirmed), the paper's standing as a formal empirical falsification of reward topology theory for IE becomes its strongest selling point for ACL Main. The conditional framing with empirical gating is the paper's most sophisticated feature — lean into it in the abstract.",
  "reason": "Close to pass but missing the formal theoretical bridge (arXiv:2601.23135) connecting reward component variance to GRPO convergence speed, leaving the core inference chain implicit rather than cited-and-derived."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44eb1aa8-129f-439d-b3da-eabe15b0ad2c",
  "isSidechain": false,
  "requestId": "req_011Catg6YQGZCnrWSwZ6ak8P",
  "type": "assistant",
  "uuid": "125721d3-c9d3-4287-8349-25cb9f93080c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MamD8RUepy9yVTj8fQDZJ1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3051,
      "cache_read_input_tokens": 60018,
      "output_tokens": 3524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3524,
          "cache_read_input_tokens": 60018,
          "cache_creation_input_tokens": 3051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3051
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "125721d3-c9d3-4287-8349-25cb9f93080c",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Signal topology curriculum for joint information extraction GRPO",
  "sessionId": "c9adbf04-de42-4c7e-9a1f-ef44ae6c4057"
}
```

---
