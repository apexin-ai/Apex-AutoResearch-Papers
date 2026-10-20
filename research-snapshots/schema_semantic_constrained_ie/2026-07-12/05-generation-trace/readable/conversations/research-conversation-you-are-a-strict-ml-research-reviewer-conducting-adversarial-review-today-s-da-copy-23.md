# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/df7bbab5-7d2b-4484-832d-90837932efdc.jsonl`
- **Structured JSON:** [`ed18a8ebcd1225a74dda.json`](../../sessions/ed/ed18a8ebcd1225a74dda.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:03:05.201Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:03:05.201Z",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weighting Induces Sequential Skill Curriculum for Joint NER+RE+EE\",\n  \"core_problem\": \"GRPO-based information extraction (IE) rewards universally treat (span, type) pairs as atomic structural units: a prediction with the correct span but wrong type label receives the same near-zero reward as a completely missed mention. This atomicity assumption has a precise gradient-theoretic consequence. In early GRPO training when both span detection and type classification are unreliable, atomic rewards produce high-variance gradients: the expected non-zero signal requires simultaneously correct span AND correct type, a low-probability joint event whose probability product makes the reward sparse and noisy. Span-decoupled rewards break this bottleneck — span-boundary F1 is continuous, lower-variance, and receives non-zero gradient even when type is wrong, stabilizing the GRPO objective in early training and allowing span detection to converge first. As span accuracy increases, the type-conditioned component's gradient variance drops (conditioned on correct spans, type prediction becomes a simpler classification problem), creating a span→type→argument sequential convergence structure — an implicit curriculum emerging from reward decomposition rather than explicit scheduling.\\n\\nProUIE (arXiv:2604.10633, April 2026) provides the clearest empirical evidence for the cost of atomic rewards. Its Stepwise Fine-grained Reward (SFR) for event extraction computes argument-level F1 (F_full) by first matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap. When trigger type or span is wrong, fewer argument pairs match, reducing F_full — and the piecewise penalty (Eq. 9) simultaneously shifts gradient emphasis toward trigger correction rather than argument assignment. The result, as we infer from SFR's structure (ProUIE does not explicitly diagnose the mechanism), is that argument role learning receives weakened gradient signal whenever trigger detection fails. ProUIE reports ACE2005 Trigger F1=70.65% and Argument F1=52.58% versus InstructUIE (Flan-T5-XXL, 11B) at 77.13%/72.94% — a 20-point argument F1 deficit. ProUIE's authors attribute this to 'unified generation setting and reward configuration' and call for 'more appropriate reward design,' but do not identify which structural feature of SFR causes the gap.\\n\\nThe core missing ingredient is a principled span-boundary reward that is decoupled from type label, accompanied by a formal justification showing why this decomposition creates stable sequential skill acquisition during GRPO training. No published GRPO-IE work provides either: ProUIE's SFR, R1-RE, R2GRPO, and EXTRACT-0 all use atomic (span, type) rewards; and no GRPO-IE paper has analyzed reward decomposition through the lens of gradient variance or curriculum induction.\",\n  \"opportunity\": \"ProUIE's acknowledged performance gap ('more appropriate reward design') and its documented 20-point argument F1 deficit on ACE2005 create a precisely bounded opportunity with three distinct axes — two empirical and one theoretical — none of which existing work covers.\\n\\n**Axis 1 (Theoretical — primary novelty)**: No published work has formally analyzed how decomposing IE rewards by skill type (span detection vs. type classification vs. relational assignment) induces sequential skill convergence in GRPO training. The closest parallel is RuCL (arXiv:2602.21628), which uses tiered rubric rewards in GRPO for multimodal reasoning and provides a gradient variance decomposition in Appendix B showing that reliable foundational reward components reduce early-training gradient variance. For IE, the analogous argument requires showing that span-boundary F1 has systematically lower reward variance than joint (span, type) F1 in early training — because span IoU is a continuous signal while joint correctness is a low-probability conjunction — and that this variance gap induces a span→type→argument convergence ordering. Making this argument formally for IE, supported by per-component learning curves, is a genuine theoretical contribution gap. The recent 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) formally proves a relay regime for task-level difficulty ordering but does not analyze reward-component-level difficulty ordering within a single task type — the proposed analysis applies the relay regime concept at a different level of abstraction. The Reward Decomposition Theorem of arXiv:2604.19857 bounds the sub-optimality gap between decomposed and joint GRPO optimization but does not identify which structural properties of the reward signal (continuous span-IoU vs. joint conjunction) determine whether decomposition is beneficial — our variance analysis fills that gap.\\n\\n**Axis 2 (Algorithmic — secondary novelty)**: Existing GRPO-IE work uses fixed reward weights. The multi-objective RL literature (arXiv:2509.11452) has proven that fixed-weight scalarization is provably suboptimal for non-convex Pareto fronts, and APEX (arXiv:2601.06574) has identified 'variance hijacking' — high-variance reward components dominating gradients — as the mechanism behind fixed-weight failures. GDPO (arXiv:2601.05242, ICML 2026) addresses the related problem of advantage collapse via per-reward normalization but uses fixed aggregation weights; the proposed adaptive scheme adjusts weights based on convergence progress and is orthogonal to GDPO normalization. Both problems are directly relevant to IE: span F1 and type F1 have different variances at different training stages, making fixed weights suboptimal. Dynamic weight adaptation — tracking each component's convergence progress and up-weighting lagging components — provides a principled curriculum enforcement that ProUIE's SFR and all other GRPO-IE designs lack.\\n\\n**Axis 3 (Empirical — benchmark coverage)**: ProUIE evaluates EE on only ACE2005, CASIE, and PHEE; no RLVR-IE paper has assessed OOD event argument generalization on RAMS (139 event types, 65 argument roles, document-level), WikiEvents (50 event types, document-level), or MAVEN (168 event types, general-domain trigger detection). The proposed span-decoupled curriculum reward addresses ProUIE's diagnosed failure mode and directly fills all three gaps.\",\n  \"landscape\": \"**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. When trigger detection fails, F_full shrinks (fewer argument pairs match) and the gradient emphasis shifts to trigger correction rather than argument assignment — producing, as we infer from the structural piecewise design, weakened argument-learning signal during trigger training. ProUIE does not explicitly state this mechanism; the authors attribute weak EE to 'unified generation setting and reward configuration' and call for 'stronger event-specific modeling and more appropriate reward design' in limitations. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Our work differentiates from ProUIE on three axes: (1) span-boundary F1 computed independently of type label with formal gradient-variance justification; (2) dynamic weight adaptation replacing fixed weights; (3) per-component learning curve analysis.\\n\\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with a two-tier decomposed reward (foundational rubrics + advanced rubrics) for multimodal reasoning, with a curriculum coefficient progressively shifting weight from easy to hard rubrics. Appendix B provides gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. RuCL achieves +7.83% average improvement across seven benchmarks. It is the methodological parallel most relevant to our curriculum-induction claim — but for multimodal reasoning, not IE, and without the span-boundary decoupling insight or IE-specific convergence analysis.\\n\\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses a different failure mode of multi-reward GRPO: advantage collapse. In standard GRPO, rewards are summed before group-wise normalization (r_sum = r₁+...+rₙ; A = (r_sum − mean)/std), causing distinct reward combinations — e.g., (span=0, type=1), (span=0, type=2), and (span=1, type=2) — to map to identical normalized advantage values, destroying the relative signal between reward types. GDPO decouples normalization: each reward's advantage is normalized independently (A_i = (r_i − mean_i)/std_i) before summation and batch-wise renormalization. This preserves the relative differences between reward combinations at the normalization level. The proposed adaptive weight scheme is orthogonal: it operates after per-reward advantages are computed, adjusting the relative aggregation weights w_i(t) based on convergence progress rather than modifying the normalization step. The two mechanisms can be combined directly — GDPO normalization applied to each span/type/argument advantage, followed by convergence-progress adaptive aggregation weights — and this combination is a natural future direction. GDPO was tested on tool calling (Berkeley BFCL-v3: +4.73% live accuracy over GRPO), math, and coding, using DeepSeek-R1-1.5B and Qwen3-4B; it has not been applied to IE.\\n\\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally analyzes RLVR training dynamics on L-step compositional reasoning tasks, proving that mixed-difficulty training enters a relay regime when the difficulty ratio R = O(1) (smooth spectrum): persistent gradient signals on easier horizons make slightly harder horizons tractable, producing an implicit curriculum without explicit scheduling (Theorem 5.2 bounds inter-horizon plateau at Õ(L_max/η) vs. exponentially longer in the grokking regime). Crucially, the relay regime is analyzed at the task level — different training instances of different horizon lengths L₁ < L₂ < L_max — and the framework does not address reward decomposition. The proposed Contribution 1 applies the relay regime concept at a different level of analysis: within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, and the continuous span-IoU signal provides the 'smooth gradient handoff' that prevents prolonged plateaus during type and argument learning. This reward-component-level relay is a conceptual extension of the task-level relay regime, not a direct instantiation, and constitutes the novel contribution of Contribution 1 beyond the original framework.\\n\\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards in LVLMs, establishing convergence to a first-order stationary point at rate O(1/√T). Their result characterizes when sequential or parallel per-component optimization loses performance relative to joint training. The proposed Contribution 1 is complementary: rather than bounding the worst-case sub-optimality cost of decomposition in general, it identifies the specific structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that determines whether the decomposed reward yields lower early-training gradient variance. Together, the two analyses bracket the expected behavior: arXiv:2604.19857 establishes that decomposed GRPO is guaranteed to converge (sub-optimality is bounded), and the proposed variance analysis identifies why for IE rewards specifically the early-training variance reduction from span continuity is expected to dominate the sub-optimality cost.\\n\\n**Dynamic reward weighting** (arXiv:2509.11452, 2025) proves that fixed-weight scalarization fails on non-convex multi-objective RL Pareto fronts and proposes hypervolume-guided adaptive weight adjustment compatible with GRPO. **APEX** (arXiv:2601.06574, 2026) identifies 'variance hijacking' in multi-objective RL and proposes per-objective priority based on Learning Potential × Conflict Penalty × Progress Need. Neither paper applies adaptive weighting to IE or analyzes the span-type variance differential.\\n\\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation but do not analyze training dynamics or reward signal ordering in RL.\\n\\n**REAR** (EMNLP 2025 Findings) applies DeepSeek-R1-style RL to joint EAE+RE via supervised warm-up + joint RL, single joint reward; excludes NER and trigger detection. **R1-RE** (arXiv:2507.04642, July 2025) is RLVR for RE only, single reward, strong OOD robustness. **R2GRPO** (arXiv:2505.22068, May 2025) applies GRPO to scientific NER+RE with a composite reward, no EE and no substructure decomposition. **EXTRACT-0** (arXiv:2509.22906, September 2025) uses 7B LoRA+GRPO with semantic similarity reward for document extraction. **KnowCoder** (ACL 2024) achieves state-of-the-art IE via code-style schema SFT. **GoLLIE** (ICLR 2024) improves zero-shot IE via annotation guideline following.\\n\\nNo published paper provides span-boundary reward independent of type label, formal gradient-variance curriculum justification for IE reward decomposition, or dynamic weight adaptation for span/type reward components in GRPO-IE training, as of May 2026.\",\n  \"approach\": \"We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) and a span-boundary-decoupled reward with adaptive component weighting. The paper has three contributions: a theoretical contribution (gradient variance analysis), an algorithmic contribution (adaptive weights replacing fixed weights), and an empirical contribution (per-component learning curves as diagnostic evidence for curriculum induction).\\n\\n**Contribution 1 — Gradient Variance Analysis (theoretical)**:\\nWe formalize the curriculum-induction property of span-decoupled rewards. In early GRPO training, let p_s = P(span correct) and p_t = P(type correct | span) be the model's per-token span detection rate and type accuracy given correct span. For standard atomic rewards (joint span+type), the non-zero reward probability is p_s · p_t — low in early training because it requires a conjunction. For span-decoupled rewards, the span component alone has non-zero probability p_s > p_s · p_t. The gradient variance of the span-decoupled reward is:\\n\\nVar(∇R_decomposed) = α₁²·Var(∇F1_span) + α₂²·Var(∇F1_type|span) + α₃²·Var(∇F1_arg) + cross terms\\n\\nWe show that when p_s < 0.5 (early training), Var(∇R_decomposed) < Var(∇R_atomic) because α₁·∇F1_span provides a stable non-zero signal that reduces total gradient variance, following the same framework as RuCL's Appendix B but derived for continuous span-IoU rewards rather than binary rubrics. As span detection improves (p_s → 0.7+), the type-conditioned component's gradient variance decreases (conditioning on correct spans reduces label ambiguity), and argument F1 receives cleaner signal. This creates a span→type→argument sequential convergence ordering that is a direct consequence of reward decomposition — not an explicitly scheduled curriculum.\\n\\nWe position this analysis in relation to two concurrent theoretical frameworks. First, 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) proves a relay regime for task-level difficulty ordering: when the training set contains tasks of smoothly graduated horizons L₁ < L₂ < L_max, gradient dominance is handed off from easy to hard tasks, producing implicit curriculum emergence. Our analysis applies the relay concept at a different level — within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, with span-IoU continuity providing the smooth gradient handoff. This is a reward-component-level relay, not a task-level relay, and the paper explicitly distinguishes these two levels. Second, arXiv:2604.19857 proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed and joint GRPO optimization at O(1/√T). Our variance analysis complements this bound: arXiv:2604.19857 characterizes the worst-case cost of decomposition (sub-optimality); our analysis identifies the structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that makes the early-training variance reduction benefit dominate this cost in practice. The testable prediction is per-component learning curves that show span F1 converging before type-conditioned F1, which converges before argument F1.\\n\\n**Contribution 2 — Adaptive Component Weights (algorithmic)**:\\nReplacing fixed weights (0.4/0.3/0.3) with a dynamic scheme motivated by arXiv:2509.11452's finding that fixed scalarization is suboptimal and APEX's identification of variance hijacking. At each evaluation checkpoint t, let F1_i(t) be the current F1 for component i ∈ {span, type, arg} and σ_i(t) be its rolling standard deviation over the last 50 steps. The adaptive weight:\\n\\nw_i(t) = max(ε, θ − F1_i(t)) / σ_i(t)\\nnormalized so Σᵢ wᵢ(t) = 1, with ε=0.05 preventing zero weights, θ=0.7 as the convergence target.\\n\\nThis rule assigns higher weight to components that are lagging convergence (below θ=0.7) and lower variance (reliable gradient signal), preventing variance hijacking from the highest-variance component. Early in training, span typically has lower variance and below-target F1, so it receives high weight; once span F1 exceeds 0.7, weight shifts to type; once type converges, weight shifts to argument.\\n\\n**Relationship to GDPO**: GDPO (arXiv:2601.05242, ICML 2026) addresses a complementary but distinct normalization-level failure: advantage collapse, where summing rewards before group-wise normalization maps distinct reward combinations (e.g., span=0,type=1 vs. span=1,type=0) to identical normalized advantage values. GDPO's fix — normalizing each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation — operates at the normalization step. The proposed adaptive weights operate after per-reward advantages are computed, adjusting relative aggregation weights based on convergence progress. The two mechanisms are orthogonal and can be combined: applying GDPO normalization to each span/type/argument advantage before applying the convergence-progress adaptive weights would simultaneously prevent advantage collapse and enforce the curriculum. This combination is identified as a concrete future direction.\\n\\n**Secondary convergence criterion (θ sensitivity)**: The convergence target θ=0.7 assumes argument F1 will approach 70%+ during training (InstructUIE achieves 72.94% at 11B; the proposed system targets >60% at 8B, making this uncertain). If argument F1 plateaus below θ, the argument component would persistently receive high weight, risking the variance hijacking the scheme is designed to prevent. To address this: (a) a plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, regardless of whether F1_i has reached θ — converged-by-plateau components have their weight set to ε; (b) sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} is conducted via checkpoint evaluation on the saved main-run checkpoints, requiring no additional full training runs. If plateau detection triggers for argument before θ, weight redistribution favors whichever remaining component has the largest convergence gap and lowest variance.\\n\\n**Reward formula with adaptive weights**:\\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification)\\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration\\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong\\n\\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps.\\n\\n**Contribution 3 — Learning Curve Diagnostics (empirical)**:\\nPer-component F1 is logged every 50 GRPO steps throughout training, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves. The predicted pattern (span converges first, then type, then argument) is treated as an empirically testable consequence of the gradient variance analysis. Deviation from this pattern would falsify the curriculum-induction hypothesis and require reanalysis. This is a diagnostic contribution: even if final numbers are modest, the learning curves themselves constitute evidence about GRPO training dynamics for IE that no prior work has published.\\n\\n**Cascade failure reframing (addressing reviewer concern)**:\\nWe do not attribute to ProUIE the claim that wrong trigger type produces near-zero argument reward — ProUIE makes no such explicit statement. Our paper presents this as an inference: ProUIE's SFR structure (Eq. 9-10) implies that trigger group mismatch reduces F_full by limiting argument pair matching coverage, and the piecewise penalty shifts gradient emphasis toward trigger correction rather than argument assignment. The specific mechanism is our analysis, not ProUIE's diagnosis. ProUIE's authors observe the symptom (weak EE, especially argument F1) and call for 'more appropriate reward design'; our paper provides the mechanism and the fix.\\n\\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER).\\n\\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\\n\\n**Output format**: Code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures actual token length distribution before full training; all compute commitments gated on this measurement. Expected 300-600 tokens per example.\\n\\n**Baselines and comparison structure**:\\n(a) SFT baselines: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\\n(b) Single-reward GRPO: joint extraction F1 as the only reward, same Qwen3-8B — isolates reward decomposition effect\\n(c) Fixed-weight decomposed GRPO (α₁=0.4, α₂=0.3, α₃=0.3 throughout): ablation isolating adaptive weight contribution from span decoupling contribution\\n(d) α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5): derived from checkpoint evaluation, not a full new run — directly tests whether span-boundary decoupling is the essential design choice\\n(e) ProUIE published ACE2005 numbers (Qwen3-4B, scale difference noted explicitly)\\n(f) OOD: RAMS, WikiEvents, MAVEN (zero-shot cross-distribution generalization, sentence→document shift explicitly noted as confound; analysis identifies which document-level aspects hurt: coreference resolution for cross-sentence arguments, multi-sentence span detection)\\n\\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS (300-600 tokens) and WikiEvents (400-800 tokens) fit in full-document inference. OOD results are framed as 'zero-shot cross-distribution generalization from sentence-level training to document-level inference.' Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements. This converts the confound from a limitation to an analytical contribution.\\n\\n**Key testable hypotheses**:\\nH1 (curriculum): Per-component learning curves show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics.\\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute — isolates span-boundary decoupling contribution.\\nH3 (adaptive vs. fixed): Adaptive weight scheme produces higher Argument F1 than fixed-weight decomposed GRPO — isolates adaptive weighting contribution.\\nH4 (ProUIE gap): Decomposed GRPO closes a material fraction of the 20-point argument F1 gap vs. InstructUIE (target: Argument F1 >60% at 8B scale).\",\n  \"resource_estimate\": {\n    \"compute_note\": \"Single-run-primary design gated on 50-example dry run. Output token length: 300-600 tokens per example for joint NER+RE+EE with CoT (corrected from earlier 100-300 estimate). Dry run measures actual distribution before full training. Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.\",\n    \"manual\": {\n      \"gpu_hours\": \"~130-160 H100-hours total: dry run (~2 H100-hours) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours at ≤400 token output measured by dry run) + fixed-weight ablation from checkpoint evaluation (~20-25 H100-hours, not a full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours, draws on saved checkpoints). Total ≤165 H100-hours — within 200 H100-hour ceiling.\",\n      \"gpu_utilization\": \"Low (20-35%) — GPUs idle during gradient variance analysis derivation, learning curve interpretation, reward verifier implementation, and writing.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$325-660 (at $2.50-4/hr H100 cloud on-demand)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~130-165 H100-hours total (same single-run-primary design; agent queues dry run first, then main GRPO run; α₁=0, fixed-weight, and θ sensitivity ablations derived from checkpoint eval, not new runs)\",\n      \"gpu_utilization\": \"Moderate (55-70%) — agent runs main experiment queue; human approves after dry run token measurement and after main GRPO run before committing ablation evals.\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150-350 (experiment orchestration, learning curve analysis, reward weight logging, ProUIE comparison analysis, gradient variance derivation review, GDPO integration evaluation, ~1500-3000 turns at $0.08-0.12/turn)\",\n      \"estimated_gpu_cost\": \"~$325-660\",\n      \"risk_note\": \"Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~130-165 H100-hours total (dry run auto-queued first; main run launched if token length ≤700; checkpoint evals for ablations auto-queued after main run completes)\",\n      \"gpu_utilization\": \"Near-zero idle (~80-90%) — agent queues dry run, measures token lengths, adjusts epoch count if >700 tokens, launches main run, auto-logs per-component F1 learning curves every 50 steps, runs plateau detector and θ sensitivity from saved checkpoints.\",\n      \"timeline\": \"5-8 days with 4× H100 cluster\",\n      \"team\": \"0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger, schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)\",\n      \"claude_api_cost\": \"$175-400 (orchestration, learning curve analysis, gradient variance analysis review, ProUIE comparison, hypothesis evaluation, GDPO complementarity analysis, ~2000-4500 turns)\",\n      \"estimated_gpu_cost\": \"~$325-660\",\n      \"speed_bottleneck\": \"Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging adds minimal overhead. Learning curve generation and θ sensitivity eval are automated and gated on the main run completing.\",\n      \"risk_note\": \"Dry run mandatory first: agent auto-measures token lengths on 50 ACE2005 examples. If >700 tokens, reduces epoch count 30% before full training. Plateau detector monitors all three components (F1_i improvement <1% over 200 steps triggers weight floor activation at ε=0.1). If adaptive weight update produces weight collapse (one component reaches w>0.8 for >100 consecutive steps), agent logs alert and applies weight floor ε=0.1 on all components. Component F1 divergence (any component leads joint F1 by >20 points for 3 consecutive checkpoints) triggers auto-checkpoint and pause. θ sensitivity (θ ∈ {0.6, 0.7, 0.8}) auto-evaluated from saved checkpoints after main run.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date; commitment deadline August 2, 2026; acceptance notification August 20, 2026. The three contributions — reward decomposition extending ProUIE, adaptive weighting extending APEX/arXiv:2509.11452, and gradient variance theory as IE-domain analysis — are individually incremental extensions of prior work; the learning curve diagnostic is novel for IE but supports the method rather than constituting the core method. The Findings track is the realistic target given this contribution scope. Main track targeting requires stronger standalone theoretical novelty or substantially larger empirical improvement over the Findings threshold.)\",\n    \"ACL 2027 (ARR February 2027 cycle — comfortable fallback for all modes, and primary target for manual mode with 3-4 month timeline. The extended timeline allows: (a) stronger empirical coverage (additional datasets, further ablation), (b) optional GDPO+adaptive-weight combination experiment as a concrete future-direction follow-up, (c) tighter theoretical integration with arXiv:2602.14872's relay regime framework. Note: the August 2026 ARR cycle commits to EACL 2027, not EMNLP 2026 — this is verified from aclrollingreview.org/dates.)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose piecewise conditioning as the mechanism; does not cover RAMS/WikiEvents/MAVEN\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), curriculum coefficient shifting weight over training, Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition, but for multimodal reasoning not IE\",\n    \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — normalizes each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation to prevent advantage collapse where distinct reward combinations map to identical normalized values; GRPO sums rewards before normalization, losing relative signal; GDPO applied to tool calling (+4.73% BFCL live accuracy), math (+6.3% AIME for DeepSeek-R1-1.5B), coding; NOT applied to IE; orthogonal to proposed adaptive weights (normalization-level fix vs. weighting-level curriculum); combination of GDPO normalization + proposed adaptive weights is a concrete future direction\",\n    \"On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for mixed-difficulty RLVR on L-step compositional tasks: when difficulty ratio R = O(1), gradient signals on easier horizons make harder horizons tractable (Theorem 5.2: inter-horizon plateau exponentially shorter than grokking regime); implicit curriculum emerges at task level; does NOT analyze reward decomposition; proposed Contribution 1 extends relay concept from task-level to reward-component-level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness\",\n    \"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — proves Reward Decomposition Theorem bounding sub-optimality gap between decomposed per-component and joint GRPO optimization; convergence to first-order stationary point at O(1/√T); applied to LVLMs with multiple reward signals (visual reasoning, instruction following, factual accuracy); proposed Contribution 1 complements this by identifying the structural IE-specific property (continuous span-IoU vs. joint span+type conjunction) that makes early-training variance reduction benefit dominate the sub-optimality cost characterized in this theorem\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; proposes hypervolume-guided and gradient-based adaptive weight optimization compatible with GRPO; motivation for adaptive component weights\",\n    \"APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking (high-variance reward components dominating gradients) in multi-objective RL; per-objective priority based on Learning Potential × Conflict Penalty × Progress Need; 10.9× hypervolume vs. static weighting; motivation for variance-aware weight adaptation\",\n    \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary EE baseline that ProUIE fails to beat and the performance target for this work\",\n    \"Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that span boundary detection is prerequisite for entity typing: removing boundary regression causes 36.73% F1 drop for long entities on ACE04; motivation for span-first curriculum\",\n    \"T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence for span-before-type ordering\",\n    \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)\",\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\",\n    \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)\",\n    \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings) — joint EAE+RE via supervised warm-up + joint RL, single joint reward, excludes NER\",\n    \"R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025) — RE only, single reward\",\n    \"Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025) — scientific NER+RE, single composite reward, no EE\",\n    \"EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)\",\n    \"MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)\",\n    \"RAMS: Multi-Sentence Argument Linking (ACL 2020)\",\n    \"WikiEvents: Document-level Event Argument Extraction (NAACL 2021)\"\n  ],\n  \"description\": \"Joint NER+RE+EE GRPO training fails on event extraction because all existing reward designs treat (span, type) pairs as atomic — providing near-zero gradient when span localization is correct but type classification fails. CurriculumRLVR-IE addresses this with three contributions: (1) a formal gradient variance analysis showing that span-boundary rewards, being continuous span-IoU signals rather than low-probability span-AND-type conjunctions, have systematically lower variance in early training, inducing a span→type→argument sequential convergence (curriculum) as a consequence of reward decomposition rather than explicit scheduling — positioned as a reward-component-level instantiation of the relay regime framework from arXiv:2602.14872 and complementing the Reward Decomposition Theorem of arXiv:2604.19857; (2) an adaptive component weight scheme replacing fixed weights, motivated by arXiv:2509.11452's proof that fixed-weight scalarization is suboptimal and APEX's variance hijacking analysis, which up-weights lagging components with low variance and shifts weight as each component converges — explicitly distinguished from GDPO (arXiv:2601.05242, ICML 2026), which prevents advantage collapse at the normalization level and is orthogonal/combinable with adaptive aggregation weights; the scheme includes a plateau detector (F1_i improvement <1% over 200 steps triggers convergence regardless of θ) and a θ ∈ {0.6, 0.7, 0.8} sensitivity analysis from saved checkpoints; (3) per-component F1 learning curves logged every 50 GRPO steps as a falsifiable empirical test of the curriculum-induction hypothesis. The primary foil is ProUIE (arXiv:2604.10633, Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%), whose SFR piecewise structure (as we infer from Eq. 9-10) weakens argument gradient when trigger matching fails. The backbone is Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run + one main GRPO run + checkpoint-derived ablations, total ~130-165 H100-hours within 200 H100-hour ceiling. Target: EMNLP 2026 Findings via May 25 ARR submission (human-in-loop and auto modes); ACL 2027 Main via February 2027 ARR (manual mode and fallback).\",\n  \"project_name\": \"joint_ie_decomposed_rlvr\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"HARD CONSTRAINT VIOLATION — Auto mode estimate of ~700h A100 converts to ~350-450h H100, which directly exceeds the user's ≤200h H100 total compute ceiling. Even manual mode (~300h A100 ≈ 150-200h H100) is already at the ceiling with zero margin for ablations. Light-R1 reports 3,328-5,376 A100-GPU-hours per single GRPO run on a 14B model; the Generator's estimates are underestimated by at least 2-5× for full fine-tuning.\", \"REAR MISCHARACTERIZATION — REAR (EMNLP 2025 Findings) is described as 'RL only to event argument extraction with a single joint reward,' but the paper's documented pipeline includes joint supervised warm-up AND joint reinforced optimization across both EAE and RE tasks. The novelty claim 'no work applies GRPO to the full NER+RE+EE joint task' needs to be more carefully scoped relative to REAR's actual multi-task RL coverage.\", \"10-MONTH TEMPORAL BLIND SPOT — The landscape section cites papers from May-July 2025, but the current date is May 2026. No search evidence was found for a concurrent paper doing exactly full joint NER+RE+EE with decomposed RLVR, but this is a 10-month gap in a field that moved from 'no RLVR for RE' to R1-RE+R2GRPO+REAR in under 6 months. The 'first' claim is fragile without an explicit concurrent-work audit for Aug 2025-May 2026.\", \"MISSING REQUIRED BENCHMARKS — The user specified MAVEN, WikiEvents, and RAMS as required evaluation datasets for event extraction. None appear in the proposed benchmark suite (ACE2005 + CoNLL + SciERC). MAVEN is large-scale general-domain event detection; WikiEvents and RAMS are argument extraction benchmarks that would directly test the event-argument component of the decomposed reward.\", \"REWARD WEIGHT UNDERSPECIFICATION — The three reward components (span-boundary F1, type-conditional F1, relation/triple F1) require explicit balancing coefficients. The Generator claims these 'auto-schedule via saturation' but provides no concrete mechanism, no sensitivity analysis, and no bounds on degenerate regimes (e.g., a model that maximizes span-F1 by outputting every token as a separate span). This is the primary technical risk and needs a principled solution (e.g., uncertainty weighting, learned coefficients, or constrained reward ranges).\", \"MODEL SIZE VS. CONSTRAINT MISMATCH — Qwen2.5-14B is the wrong model size for this constraint envelope. Qwen2.5-7B with LoRA-based GRPO is the only realistic configuration that can produce even a minimal experiment within 200 H100-hours. The 14B choice appears driven by competitive benchmarking goals rather than feasibility analysis.\"]\nFeedback: The core idea — decomposed RLVR rewards that give partial credit for span-correct/type-wrong predictions — is technically sound and partially novel. To get this to a passable state: (1) Scale down to Qwen2.5-7B and specify LoRA GRPO throughout; recompute all resource estimates with LoRA reduction factors and confirm the auto mode fits under 200 H100-hours. (2) Correct the REAR framing: acknowledge REAR does joint EAE+RE RL, and position the differentiation as (a) NER inclusion + (b) strictly decomposed per-substructure rewards vs. REAR's single joint RL reward. (3) Add MAVEN, WikiEvents, and RAMS to the benchmark suite — these are explicitly required by the target track and event extraction without them is incomplete. (4) Provide a concrete reward weighting scheme: either fixed normalized coefficients justified by pilot experiments, or a learned mixing network trained jointly with the policy. (5) Add a section explicitly addressing Aug 2025-May 2026 concurrent work risk — search arXiv for 'joint information extraction GRPO' from Q3-Q4 2025 before submitting, and pre-register the differentiators. This idea is 'revise, not fail' — the decomposed reward curriculum signal is a real contribution — but the resource constraint violation and REAR mischaracterization must be fixed before this can be argued as novel and feasible.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL CONCURRENT WORK MISSED — ProUIE (arXiv:2604.10633, April 12, 2026) covers joint NER+RE+EE with GRPO + Stepwise Fine-grained Reward (SFR) decomposed hierarchically by structural unit: NER (entity-type → entity-value), RE (relation-type → relation-instance → entity-pair), EE (event-type → trigger → role → argument). Evaluated on 36 public datasets including ACE2005. The Generator's explicit claim 'No published paper applies decomposed GRPO rewards to the full joint NER+RE+EE task as of May 2026 searches' is false. A reviewer who knows ProUIE will immediately reject the novelty claim as stated.\", \"NOVELTY REPOSITIONING REQUIRED — The only surviving technical differentiator from ProUIE is: span-boundary F1 computed *independent of type label* (proposed) vs. ProUIE's atomic type-entity pairs (ProUIE rewards entity-type and entity-value but does not reward span-correct/type-wrong predictions). This specific contribution must become the paper's primary framing; the current framing ('no prior work applies decomposed GRPO to NER+RE+EE') is no longer defensible.\", \"ProUIE's DOCUMENTED EE WEAKNESS IS AN OPPORTUNITY — ProUIE explicitly reports 'underperforming the strongest baseline for both triggers and arguments' on ACE2005 EE. The proposed work should be specifically framed as addressing this failure mode: if span-conditional rewards (rewarding trigger detection independently of argument role accuracy) fix ProUIE's EE weakness, that is a compelling and concrete result. The Generator should add a comparison directly against ProUIE's published EE numbers.\", \"OUTPUT LENGTH UNDERESTIMATE — The 100-300 token claim for IE JSON extractions is optimistic for complex multi-task joint extraction with chain-of-thought. ACE2005 sentences with multiple entities, relations, and event triggers (with CoT trace) realistically produce 300-600+ tokens per example. If true output length is 2-3× the assumed value, GRPO rollout costs scale proportionally and auto-mode (3 runs) may exceed 200 H100-hours. A 50-example dry run measuring actual output token length before full training is essential.\", \"OOD DOCUMENT-LEVEL EVALUATION RISK — The model is trained on sentence-level ACE2005 examples and evaluated on document-level RAMS (multi-sentence argument linking) and WikiEvents (document-level EAE). Without document-level context handling (e.g., sliding window, cross-sentence attention), the OOD evaluation may fail for reasons unrelated to reward decomposition, threatening the validity of the OOD generalization claim. The Generator should acknowledge this and describe how document-level inputs are handled at inference.\"]\nFeedback: Round 2 successfully addressed the resource constraint (7B+LoRA is now realistic), REAR framing (correctly described), missing benchmarks (MAVEN/RAMS/WikiEvents now included), and reward underspecification (fixed weights with pilot calibration). However, a critical gap opened: ProUIE (arXiv:2604.10633, April 2026) does joint NER+RE+EE with GRPO + fine-grained hierarchical rewards, directly occupying the 'first decomposed GRPO for joint IE' claim. You cannot submit without addressing this. Recommended revision path: (1) Acknowledge ProUIE in related work — frame the proposed work as explicitly extending ProUIE's limitation: ProUIE's SFR treats type-entity pairs as atomic, meaning a span-correct/type-wrong prediction receives near-zero reward. The proposed span-IoU-conditioned hierarchical reward explicitly credits partial correctness at the span level. (2) Make the EE comparison against ProUIE's published numbers the centerpiece empirical result — ProUIE underperforms baselines on ACE2005 EE; showing that span-conditional rewards fix this is a sharp, verifiable contribution. (3) Position MAVEN/RAMS/WikiEvents as the OOD evaluation that ProUIE does not cover. (4) Measure actual output token lengths on a 50-example ACE2005 pilot BEFORE committing to the 100-300 token estimate and the 200 H100-hour ceiling claim. (5) Add a one-paragraph discussion of how document-level inputs (RAMS, WikiEvents) are handled at inference given sentence-level ACE2005 training — sliding window with sentence-level extractions merged, or prompt includes full document context?\n\n### Round 3 review\nVerdict: revise\nIssues: [\"VENUE FACTUAL ERROR (critical): The 'EMNLP 2026 via August ARR cycle' path does not exist. ARR's own dates page confirms the August 3, 2026 ARR cycle commits to EACL 2027, not EMNLP 2026. The ONLY path to EMNLP 2026 is submission by May 25, 2026 (commitment deadline August 2). If May 25 is infeasible for the current experiments, the correct fallback is ACL 2027 (February 2027 ARR deadline), not 'EMNLP 2026 via August.' The target venue section must be corrected.\", \"COMPUTE CEILING STILL POTENTIALLY VIOLATED: The Generator estimates 80-200 H100-hours per GRPO run and commits to 2 runs (total: 160-400 H100-hours). The upper-bound scenario (400 H100-hours) is 2× the hard constraint of ≤200 H100-hours. The Generator says 'ceiling constrained to 2 GRPO runs to stay within 420 H100-hours' — but 420 >> 200. A concrete single-run-primary design is needed: one main GRPO run (90-120 H100-hours if dry run confirms ~350-token outputs), with the α₁=0 ablation derived from a fraction of rollouts at the final checkpoint, keeping total under 200 H100-hours.\", \"CASCADE FAILURE CLAIM OVERSTATED: ProUIE's paper does not explicitly state that wrong trigger type produces near-zero argument reward. Independent fetch of the paper confirms: 'The paper doesn't explicitly state that incorrect trigger types produce near-zero argument rewards, though the piecewise penalty suggests coarse errors receive priority.' The Generator should reframe this as an inference from SFR's piecewise structure rather than ProUIE's own diagnosis — otherwise a reviewer who reads ProUIE carefully will flag this as misrepresentation.\", \"CONTRIBUTION SCOPE NARROWNESS RISK: The paper's distinguishing technical contribution is a single reward design change (add α₁=0.4 span-boundary component independent of type label). Without stronger theoretical grounding — e.g., a formal proof or convergence analysis showing span-decoupled rewards induce a natural curriculum (span → type → argument) — reviewers may characterize this as an ablation of ProUIE's reward design rather than a standalone method. Consider adding a curriculum convergence analysis or learning curve comparison showing the predicted sequential skill acquisition.\", \"OOD DOCUMENT-LEVEL CONFOUND UNRESOLVED: The paper trains on sentence-level ACE2005 and evaluates on document-level RAMS/WikiEvents/MAVEN. The Generator acknowledges this as a 'confound noted explicitly' but this framing is insufficient — reviewers will ask why no document-level adaptation was attempted. Reframe OOD results as 'zero-shot cross-distribution generalization from sentence to document' and add a brief analysis of which document-level aspects hurt performance (e.g., coreference chains, multi-sentence arguments).\"]\nFeedback: The technical core is now well-specified and the ProUIE differentiation is valid. Three rounds of revision have addressed compute scale, REAR framing, missing benchmarks, and output-length underestimation. The remaining fixable issues are: (1) Correct the venue section immediately — the only path to EMNLP 2026 is the May 25 ARR submission (15 days away); if that is missed, the real next target is ACL 2027 via February 2027 ARR. Remove all references to 'EMNLP 2026 via August ARR cycle.' (2) Design a single-run budget that fits ≤200 H100-hours: commit the dry run (2 H100-hours) + one main GRPO run (target 90-120 H100-hours at ≤400 token output) + the α₁=0 ablation from checkpoint evaluation (not a full new run, ~20-30 H100-hours). Total: ~130-150 H100-hours — within the constraint. (3) Soften the cascade failure attribution from 'near-zero reward' (ProUIE's claimed mechanism) to 'near-zero reward implied by SFR's piecewise conditioning on matched trigger groups' (your inference). This distinction matters to reviewers who read ProUIE. (4) Strengthen the theoretical framing: if you can show analytically or empirically that span-decoupled rewards create a sequential skill curriculum (span convergence first, then type, then argument), this elevates the paper from 'ablation' to 'method contribution.' Learning curves for each reward component across training steps would directly support this claim at low additional compute cost.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"UNCITED COMPETITOR (HIGH PRIORITY): GDPO (arXiv:2601.05242, January 2026, ICML 2026) from NVIDIA proposes per-reward normalization in GRPO to prevent advantage collapse in multi-reward settings — applied to tool calling, math, and coding. GDPO is the normalization analog to the proposed adaptive weighting: GDPO normalizes each reward independently within the group before aggregation; the proposed method dynamically adjusts the aggregation weights based on convergence progress. A reviewer familiar with GDPO (now an ICML 2026 poster) will immediately flag its absence. The generator must cite GDPO and clearly distinguish: GDPO prevents per-reward advantage collapse at the normalization level; the proposed method enforces a curriculum by adjusting relative weights as each component converges — these are complementary and could be combined (GDPO normalization + proposed adaptive weights), which would itself strengthen the paper.\", \"UNCITED THEORETICAL PARALLEL (MEDIUM PRIORITY): 'The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards' (arXiv:2602.14872, February 2026) formally proves that RLVR exhibits implicit skill ordering emergence when the difficulty spectrum is smooth, using a relay regime analysis with convergence guarantees. The proposed paper's Contribution 1 (gradient variance analysis showing span→type→argument sequential convergence) is an instance of this broader phenomenon. Without citing this paper and positioning the IE-specific analysis as a domain instantiation of the relay regime framework, reviewers reading both papers will flag this as a missed citation. Importantly, the Implicit Curriculum paper provides stronger theoretical machinery — the generator should either explicitly build on it or clearly explain what the IE-specific variance analysis adds beyond the general framework.\", \"UNCITED THEORETICAL PARALLEL (MEDIUM PRIORITY): 'Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization' (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards, applied to LVLMs. The proposed Contribution 1 provides a gradient-variance-based analysis of a similar decomposition for IE — it must acknowledge arXiv:2604.19857, explain how its span-IoU continuous signal analysis extends or complements the formal sub-optimality bounds in that paper, and position the IE task structure (span IoU continuity vs. joint conjunction) as the distinctive aspect.\", \"ADAPTIVE WEIGHT θ HYPERPARAMETER RISK: The convergence target θ=0.7 is used as the reference point for the weight formula w_i(t) = max(ε, θ - F1_i(t)) / σ_i(t). If argument F1 never reaches 0.7 (InstructUIE achieves 72.94% at 11B; the proposed system targeting >60% suggests this is achievable but not guaranteed), the argument component will persistently receive high weight throughout training, potentially causing variance hijacking in late training — the exact phenomenon the scheme is meant to prevent. The generator should add: (a) a secondary convergence criterion (e.g., plateau detection when F1_i improves <1% over 200 steps), or (b) sensitivity analysis showing the method is robust to θ ∈ {0.6, 0.7, 0.8}.\", \"EMNLP MAIN vs FINDINGS REALISM: The paper targets EMNLP 2026 Main but the three contributions individually are incremental extensions of ProUIE (reward decomposition), APEX/2509.11452 (adaptive weighting), and RuCL (gradient variance theory). The learning curve diagnostic is genuinely novel for IE but is a contribution supporting the method, not the method itself. The realistic target is EMNLP 2026 Findings — the generator should explicitly acknowledge this in the target venue section to set accurate expectations for the auto-mode agent.\"]\nFeedback: The core technical nucleus is now well-executed: span-boundary-decoupled GRPO reward for IE is a real gap, the single-run compute design fits within 200 H100-hours, and the cascade failure attribution is properly softened. Round 4 has resolved all four Round 3 issues. However, three concurrent papers published since Round 3 that are directly relevant to the claimed contributions are missing from the related work: (1) GDPO (ICML 2026) for multi-reward GRPO normalization, (2) 'The Implicit Curriculum' (Feb 2026) for RLVR skill ordering theory, and (3) arXiv:2604.19857 (April 2026) for composite-reward GRPO convergence theory. These omissions, if noticed by a reviewer, will be read as lack of thoroughness. Recommended actions for Round 5: (a) Add GDPO to related work — 1 paragraph distinguishing per-reward normalization (GDPO) from convergence-progress adaptive weighting (proposed), note they are complementary, suggest combining GDPO normalization + proposed weights as a future direction. (b) Add 'The Implicit Curriculum' — 1 paragraph framing the IE span→type→argument gradient variance analysis as a domain instantiation of the relay regime framework, with the span-IoU continuity as what makes the IE difficulty spectrum smooth in the relevant sense. (c) Add arXiv:2604.19857 — 1 paragraph noting its Reward Decomposition Theorem for LVLMs and explaining how the proposed early-training gradient variance analysis complements it by identifying span continuity as the specific structural property that makes IE reward decomposition beneficial. (d) Add θ sensitivity analysis or secondary convergence criterion for the adaptive weight formula. These are additive changes to related work and the method section — no experimental changes required. The EMNLP 2026 Findings track is the appropriate target given the contribution scope.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:03:05.204Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:03:05.204Z",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-10T08:03:05.231Z_

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

## Idea under review (round 5/10)
{
  "title": "CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weighting Induces Sequential Skill Curriculum for Joint NER+RE+EE",
  "core_problem": "GRPO-based information extraction (IE) rewards universally treat (span, type) pairs as atomic structural units: a prediction with the correct span but wrong type label receives the same near-zero reward as a completely missed mention. This atomicity assumption has a precise gradient-theoretic consequence. In early GRPO training when both span detection and type classification are unreliable, atomic rewards produce high-variance gradients: the expected non-zero signal requires simultaneously correct span AND correct type, a low-probability joint event whose probability product makes the reward sparse and noisy. Span-decoupled rewards break this bottleneck — span-boundary F1 is continuous, lower-variance, and receives non-zero gradient even when type is wrong, stabilizing the GRPO objective in early training and allowing span detection to converge first. As span accuracy increases, the type-conditioned component's gradient variance drops (conditioned on correct spans, type prediction becomes a simpler classification problem), creating a span→type→argument sequential convergence structure — an implicit curriculum emerging from reward decomposition rather than explicit scheduling.\n\nProUIE (arXiv:2604.10633, April 2026) provides the clearest empirical evidence for the cost of atomic rewards. Its Stepwise Fine-grained Reward (SFR) for event extraction computes argument-level F1 (F_full) by first matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap. When trigger type or span is wrong, fewer argument pairs match, reducing F_full — and the piecewise penalty (Eq. 9) simultaneously shifts gradient emphasis toward trigger correction rather than argument assignment. The result, as we infer from SFR's structure (ProUIE does not explicitly diagnose the mechanism), is that argument role learning receives weakened gradient signal whenever trigger detection fails. ProUIE reports ACE2005 Trigger F1=70.65% and Argument F1=52.58% versus InstructUIE (Flan-T5-XXL, 11B) at 77.13%/72.94% — a 20-point argument F1 deficit. ProUIE's authors attribute this to 'unified generation setting and reward configuration' and call for 'more appropriate reward design,' but do not identify which structural feature of SFR causes the gap.\n\nThe core missing ingredient is a principled span-boundary reward that is decoupled from type label, accompanied by a formal justification showing why this decomposition creates stable sequential skill acquisition during GRPO training. No published GRPO-IE work provides either: ProUIE's SFR, R1-RE, R2GRPO, and EXTRACT-0 all use atomic (span, type) rewards; and no GRPO-IE paper has analyzed reward decomposition through the lens of gradient variance or curriculum induction.",
  "opportunity": "ProUIE's acknowledged performance gap ('more appropriate reward design') and its documented 20-point argument F1 deficit on ACE2005 create a precisely bounded opportunity with three distinct axes — two empirical and one theoretical — none of which existing work covers.\n\n**Axis 1 (Theoretical — primary novelty)**: No published work has formally analyzed how decomposing IE rewards by skill type (span detection vs. type classification vs. relational assignment) induces sequential skill convergence in GRPO training. The closest parallel is RuCL (arXiv:2602.21628), which uses tiered rubric rewards in GRPO for multimodal reasoning and provides a gradient variance decomposition in Appendix B showing that reliable foundational reward components reduce early-training gradient variance. For IE, the analogous argument requires showing that span-boundary F1 has systematically lower reward variance than joint (span, type) F1 in early training — because span IoU is a continuous signal while joint correctness is a low-probability conjunction — and that this variance gap induces a span→type→argument convergence ordering. Making this argument formally for IE, supported by per-component learning curves, is a genuine theoretical contribution gap. The recent 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) formally proves a relay regime for task-level difficulty ordering but does not analyze reward-component-level difficulty ordering within a single task type — the proposed analysis applies the relay regime concept at a different level of abstraction. The Reward Decomposition Theorem of arXiv:2604.19857 bounds the sub-optimality gap between decomposed and joint GRPO optimization but does not identify which structural properties of the reward signal (continuous span-IoU vs. joint conjunction) determine whether decomposition is beneficial — our variance analysis fills that gap.\n\n**Axis 2 (Algorithmic — secondary novelty)**: Existing GRPO-IE work uses fixed reward weights. The multi-objective RL literature (arXiv:2509.11452) has proven that fixed-weight scalarization is provably suboptimal for non-convex Pareto fronts, and APEX (arXiv:2601.06574) has identified 'variance hijacking' — high-variance reward components dominating gradients — as the mechanism behind fixed-weight failures. GDPO (arXiv:2601.05242, ICML 2026) addresses the related problem of advantage collapse via per-reward normalization but uses fixed aggregation weights; the proposed adaptive scheme adjusts weights based on convergence progress and is orthogonal to GDPO normalization. Both problems are directly relevant to IE: span F1 and type F1 have different variances at different training stages, making fixed weights suboptimal. Dynamic weight adaptation — tracking each component's convergence progress and up-weighting lagging components — provides a principled curriculum enforcement that ProUIE's SFR and all other GRPO-IE designs lack.\n\n**Axis 3 (Empirical — benchmark coverage)**: ProUIE evaluates EE on only ACE2005, CASIE, and PHEE; no RLVR-IE paper has assessed OOD event argument generalization on RAMS (139 event types, 65 argument roles, document-level), WikiEvents (50 event types, document-level), or MAVEN (168 event types, general-domain trigger detection). The proposed span-decoupled curriculum reward addresses ProUIE's diagnosed failure mode and directly fills all three gaps.",
  "landscape": "**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. When trigger detection fails, F_full shrinks (fewer argument pairs match) and the gradient emphasis shifts to trigger correction rather than argument assignment — producing, as we infer from the structural piecewise design, weakened argument-learning signal during trigger training. ProUIE does not explicitly state this mechanism; the authors attribute weak EE to 'unified generation setting and reward configuration' and call for 'stronger event-specific modeling and more appropriate reward design' in limitations. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Our work differentiates from ProUIE on three axes: (1) span-boundary F1 computed independently of type label with formal gradient-variance justification; (2) dynamic weight adaptation replacing fixed weights; (3) per-component learning curve analysis.\n\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with a two-tier decomposed reward (foundational rubrics + advanced rubrics) for multimodal reasoning, with a curriculum coefficient progressively shifting weight from easy to hard rubrics. Appendix B provides gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. RuCL achieves +7.83% average improvement across seven benchmarks. It is the methodological parallel most relevant to our curriculum-induction claim — but for multimodal reasoning, not IE, and without the span-boundary decoupling insight or IE-specific convergence analysis.\n\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses a different failure mode of multi-reward GRPO: advantage collapse. In standard GRPO, rewards are summed before group-wise normalization (r_sum = r₁+...+rₙ; A = (r_sum − mean)/std), causing distinct reward combinations — e.g., (span=0, type=1), (span=0, type=2), and (span=1, type=2) — to map to identical normalized advantage values, destroying the relative signal between reward types. GDPO decouples normalization: each reward's advantage is normalized independently (A_i = (r_i − mean_i)/std_i) before summation and batch-wise renormalization. This preserves the relative differences between reward combinations at the normalization level. The proposed adaptive weight scheme is orthogonal: it operates after per-reward advantages are computed, adjusting the relative aggregation weights w_i(t) based on convergence progress rather than modifying the normalization step. The two mechanisms can be combined directly — GDPO normalization applied to each span/type/argument advantage, followed by convergence-progress adaptive aggregation weights — and this combination is a natural future direction. GDPO was tested on tool calling (Berkeley BFCL-v3: +4.73% live accuracy over GRPO), math, and coding, using DeepSeek-R1-1.5B and Qwen3-4B; it has not been applied to IE.\n\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally analyzes RLVR training dynamics on L-step compositional reasoning tasks, proving that mixed-difficulty training enters a relay regime when the difficulty ratio R = O(1) (smooth spectrum): persistent gradient signals on easier horizons make slightly harder horizons tractable, producing an implicit curriculum without explicit scheduling (Theorem 5.2 bounds inter-horizon plateau at Õ(L_max/η) vs. exponentially longer in the grokking regime). Crucially, the relay regime is analyzed at the task level — different training instances of different horizon lengths L₁ < L₂ < L_max — and the framework does not address reward decomposition. The proposed Contribution 1 applies the relay regime concept at a different level of analysis: within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, and the continuous span-IoU signal provides the 'smooth gradient handoff' that prevents prolonged plateaus during type and argument learning. This reward-component-level relay is a conceptual extension of the task-level relay regime, not a direct instantiation, and constitutes the novel contribution of Contribution 1 beyond the original framework.\n\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards in LVLMs, establishing convergence to a first-order stationary point at rate O(1/√T). Their result characterizes when sequential or parallel per-component optimization loses performance relative to joint training. The proposed Contribution 1 is complementary: rather than bounding the worst-case sub-optimality cost of decomposition in general, it identifies the specific structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that determines whether the decomposed reward yields lower early-training gradient variance. Together, the two analyses bracket the expected behavior: arXiv:2604.19857 establishes that decomposed GRPO is guaranteed to converge (sub-optimality is bounded), and the proposed variance analysis identifies why for IE rewards specifically the early-training variance reduction from span continuity is expected to dominate the sub-optimality cost.\n\n**Dynamic reward weighting** (arXiv:2509.11452, 2025) proves that fixed-weight scalarization fails on non-convex multi-objective RL Pareto fronts and proposes hypervolume-guided adaptive weight adjustment compatible with GRPO. **APEX** (arXiv:2601.06574, 2026) identifies 'variance hijacking' in multi-objective RL and proposes per-objective priority based on Learning Potential × Conflict Penalty × Progress Need. Neither paper applies adaptive weighting to IE or analyzes the span-type variance differential.\n\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation but do not analyze training dynamics or reward signal ordering in RL.\n\n**REAR** (EMNLP 2025 Findings) applies DeepSeek-R1-style RL to joint EAE+RE via supervised warm-up + joint RL, single joint reward; excludes NER and trigger detection. **R1-RE** (arXiv:2507.04642, July 2025) is RLVR for RE only, single reward, strong OOD robustness. **R2GRPO** (arXiv:2505.22068, May 2025) applies GRPO to scientific NER+RE with a composite reward, no EE and no substructure decomposition. **EXTRACT-0** (arXiv:2509.22906, September 2025) uses 7B LoRA+GRPO with semantic similarity reward for document extraction. **KnowCoder** (ACL 2024) achieves state-of-the-art IE via code-style schema SFT. **GoLLIE** (ICLR 2024) improves zero-shot IE via annotation guideline following.\n\nNo published paper provides span-boundary reward independent of type label, formal gradient-variance curriculum justification for IE reward decomposition, or dynamic weight adaptation for span/type reward components in GRPO-IE training, as of May 2026.",
  "approach": "We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) and a span-boundary-decoupled reward with adaptive component weighting. The paper has three contributions: a theoretical contribution (gradient variance analysis), an algorithmic contribution (adaptive weights replacing fixed weights), and an empirical contribution (per-component learning curves as diagnostic evidence for curriculum induction).\n\n**Contribution 1 — Gradient Variance Analysis (theoretical)**:\nWe formalize the curriculum-induction property of span-decoupled rewards. In early GRPO training, let p_s = P(span correct) and p_t = P(type correct | span) be the model's per-token span detection rate and type accuracy given correct span. For standard atomic rewards (joint span+type), the non-zero reward probability is p_s · p_t — low in early training because it requires a conjunction. For span-decoupled rewards, the span component alone has non-zero probability p_s > p_s · p_t. The gradient variance of the span-decoupled reward is:\n\nVar(∇R_decomposed) = α₁²·Var(∇F1_span) + α₂²·Var(∇F1_type|span) + α₃²·Var(∇F1_arg) + cross terms\n\nWe show that when p_s < 0.5 (early training), Var(∇R_decomposed) < Var(∇R_atomic) because α₁·∇F1_span provides a stable non-zero signal that reduces total gradient variance, following the same framework as RuCL's Appendix B but derived for continuous span-IoU rewards rather than binary rubrics. As span detection improves (p_s → 0.7+), the type-conditioned component's gradient variance decreases (conditioning on correct spans reduces label ambiguity), and argument F1 receives cleaner signal. This creates a span→type→argument sequential convergence ordering that is a direct consequence of reward decomposition — not an explicitly scheduled curriculum.\n\nWe position this analysis in relation to two concurrent theoretical frameworks. First, 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) proves a relay regime for task-level difficulty ordering: when the training set contains tasks of smoothly graduated horizons L₁ < L₂ < L_max, gradient dominance is handed off from easy to hard tasks, producing implicit curriculum emergence. Our analysis applies the relay concept at a different level — within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, with span-IoU continuity providing the smooth gradient handoff. This is a reward-component-level relay, not a task-level relay, and the paper explicitly distinguishes these two levels. Second, arXiv:2604.19857 proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed and joint GRPO optimization at O(1/√T). Our variance analysis complements this bound: arXiv:2604.19857 characterizes the worst-case cost of decomposition (sub-optimality); our analysis identifies the structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that makes the early-training variance reduction benefit dominate this cost in practice. The testable prediction is per-component learning curves that show span F1 converging before type-conditioned F1, which converges before argument F1.\n\n**Contribution 2 — Adaptive Component Weights (algorithmic)**:\nReplacing fixed weights (0.4/0.3/0.3) with a dynamic scheme motivated by arXiv:2509.11452's finding that fixed scalarization is suboptimal and APEX's identification of variance hijacking. At each evaluation checkpoint t, let F1_i(t) be the current F1 for component i ∈ {span, type, arg} and σ_i(t) be its rolling standard deviation over the last 50 steps. The adaptive weight:\n\nw_i(t) = max(ε, θ − F1_i(t)) / σ_i(t)\nnormalized so Σᵢ wᵢ(t) = 1, with ε=0.05 preventing zero weights, θ=0.7 as the convergence target.\n\nThis rule assigns higher weight to components that are lagging convergence (below θ=0.7) and lower variance (reliable gradient signal), preventing variance hijacking from the highest-variance component. Early in training, span typically has lower variance and below-target F1, so it receives high weight; once span F1 exceeds 0.7, weight shifts to type; once type converges, weight shifts to argument.\n\n**Relationship to GDPO**: GDPO (arXiv:2601.05242, ICML 2026) addresses a complementary but distinct normalization-level failure: advantage collapse, where summing rewards before group-wise normalization maps distinct reward combinations (e.g., span=0,type=1 vs. span=1,type=0) to identical normalized advantage values. GDPO's fix — normalizing each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation — operates at the normalization step. The proposed adaptive weights operate after per-reward advantages are computed, adjusting relative aggregation weights based on convergence progress. The two mechanisms are orthogonal and can be combined: applying GDPO normalization to each span/type/argument advantage before applying the convergence-progress adaptive weights would simultaneously prevent advantage collapse and enforce the curriculum. This combination is identified as a concrete future direction.\n\n**Secondary convergence criterion (θ sensitivity)**: The convergence target θ=0.7 assumes argument F1 will approach 70%+ during training (InstructUIE achieves 72.94% at 11B; the proposed system targets >60% at 8B, making this uncertain). If argument F1 plateaus below θ, the argument component would persistently receive high weight, risking the variance hijacking the scheme is designed to prevent. To address this: (a) a plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, regardless of whether F1_i has reached θ — converged-by-plateau components have their weight set to ε; (b) sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} is conducted via checkpoint evaluation on the saved main-run checkpoints, requiring no additional full training runs. If plateau detection triggers for argument before θ, weight redistribution favors whichever remaining component has the largest convergence gap and lowest variance.\n\n**Reward formula with adaptive weights**:\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification)\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong\n\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps.\n\n**Contribution 3 — Learning Curve Diagnostics (empirical)**:\nPer-component F1 is logged every 50 GRPO steps throughout training, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves. The predicted pattern (span converges first, then type, then argument) is treated as an empirically testable consequence of the gradient variance analysis. Deviation from this pattern would falsify the curriculum-induction hypothesis and require reanalysis. This is a diagnostic contribution: even if final numbers are modest, the learning curves themselves constitute evidence about GRPO training dynamics for IE that no prior work has published.\n\n**Cascade failure reframing (addressing reviewer concern)**:\nWe do not attribute to ProUIE the claim that wrong trigger type produces near-zero argument reward — ProUIE makes no such explicit statement. Our paper presents this as an inference: ProUIE's SFR structure (Eq. 9-10) implies that trigger group mismatch reduces F_full by limiting argument pair matching coverage, and the piecewise penalty shifts gradient emphasis toward trigger correction rather than argument assignment. The specific mechanism is our analysis, not ProUIE's diagnosis. ProUIE's authors observe the symptom (weak EE, especially argument F1) and call for 'more appropriate reward design'; our paper provides the mechanism and the fix.\n\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER).\n\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\n\n**Output format**: Code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures actual token length distribution before full training; all compute commitments gated on this measurement. Expected 300-600 tokens per example.\n\n**Baselines and comparison structure**:\n(a) SFT baselines: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\n(b) Single-reward GRPO: joint extraction F1 as the only reward, same Qwen3-8B — isolates reward decomposition effect\n(c) Fixed-weight decomposed GRPO (α₁=0.4, α₂=0.3, α₃=0.3 throughout): ablation isolating adaptive weight contribution from span decoupling contribution\n(d) α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5): derived from checkpoint evaluation, not a full new run — directly tests whether span-boundary decoupling is the essential design choice\n(e) ProUIE published ACE2005 numbers (Qwen3-4B, scale difference noted explicitly)\n(f) OOD: RAMS, WikiEvents, MAVEN (zero-shot cross-distribution generalization, sentence→document shift explicitly noted as confound; analysis identifies which document-level aspects hurt: coreference resolution for cross-sentence arguments, multi-sentence span detection)\n\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS (300-600 tokens) and WikiEvents (400-800 tokens) fit in full-document inference. OOD results are framed as 'zero-shot cross-distribution generalization from sentence-level training to document-level inference.' Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements. This converts the confound from a limitation to an analytical contribution.\n\n**Key testable hypotheses**:\nH1 (curriculum): Per-component learning curves show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics.\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute — isolates span-boundary decoupling contribution.\nH3 (adaptive vs. fixed): Adaptive weight scheme produces higher Argument F1 than fixed-weight decomposed GRPO — isolates adaptive weighting contribution.\nH4 (ProUIE gap): Decomposed GRPO closes a material fraction of the 20-point argument F1 gap vs. InstructUIE (target: Argument F1 >60% at 8B scale).",
  "resource_estimate": {
    "compute_note": "Single-run-primary design gated on 50-example dry run. Output token length: 300-600 tokens per example for joint NER+RE+EE with CoT (corrected from earlier 100-300 estimate). Dry run measures actual distribution before full training. Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.",
    "manual": {
      "gpu_hours": "~130-160 H100-hours total: dry run (~2 H100-hours) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours at ≤400 token output measured by dry run) + fixed-weight ablation from checkpoint evaluation (~20-25 H100-hours, not a full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours, draws on saved checkpoints). Total ≤165 H100-hours — within 200 H100-hour ceiling.",
      "gpu_utilization": "Low (20-35%) — GPUs idle during gradient variance analysis derivation, learning curve interpretation, reward verifier implementation, and writing.",
      "timeline": "3-4 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$325-660 (at $2.50-4/hr H100 cloud on-demand)"
    },
    "human_in_loop": {
      "gpu_hours": "~130-165 H100-hours total (same single-run-primary design; agent queues dry run first, then main GRPO run; α₁=0, fixed-weight, and θ sensitivity ablations derived from checkpoint eval, not new runs)",
      "gpu_utilization": "Moderate (55-70%) — agent runs main experiment queue; human approves after dry run token measurement and after main GRPO run before committing ablation evals.",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150-350 (experiment orchestration, learning curve analysis, reward weight logging, ProUIE comparison analysis, gradient variance derivation review, GDPO integration evaluation, ~1500-3000 turns at $0.08-0.12/turn)",
      "estimated_gpu_cost": "~$325-660",
      "risk_note": "Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes."
    },
    "auto_research": {
      "gpu_hours": "~130-165 H100-hours total (dry run auto-queued first; main run launched if token length ≤700; checkpoint evals for ablations auto-queued after main run completes)",
      "gpu_utilization": "Near-zero idle (~80-90%) — agent queues dry run, measures token lengths, adjusts epoch count if >700 tokens, launches main run, auto-logs per-component F1 learning curves every 50 steps, runs plateau detector and θ sensitivity from saved checkpoints.",
      "timeline": "5-8 days with 4× H100 cluster",
      "team": "0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger, schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)",
      "claude_api_cost": "$175-400 (orchestration, learning curve analysis, gradient variance analysis review, ProUIE comparison, hypothesis evaluation, GDPO complementarity analysis, ~2000-4500 turns)",
      "estimated_gpu_cost": "~$325-660",
      "speed_bottleneck": "Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging adds minimal overhead. Learning curve generation and θ sensitivity eval are automated and gated on the main run completing.",
      "risk_note": "Dry run mandatory first: agent auto-measures token lengths on 50 ACE2005 examples. If >700 tokens, reduces epoch count 30% before full training. Plateau detector monitors all three components (F1_i improvement <1% over 200 steps triggers weight floor activation at ε=0.1). If adaptive weight update produces weight collapse (one component reaches w>0.8 for >100 consecutive steps), agent logs alert and applies weight floor ε=0.1 on all components. Component F1 divergence (any component leads joint F1 by >20 points for 3 consecutive checkpoints) triggers auto-checkpoint and pause. θ sensitivity (θ ∈ {0.6, 0.7, 0.8}) auto-evaluated from saved checkpoints after main run."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date; commitment deadline August 2, 2026; acceptance notification August 20, 2026. The three contributions — reward decomposition extending ProUIE, adaptive weighting extending APEX/arXiv:2509.11452, and gradient variance theory as IE-domain analysis — are individually incremental extensions of prior work; the learning curve diagnostic is novel for IE but supports the method rather than constituting the core method. The Findings track is the realistic target given this contribution scope. Main track targeting requires stronger standalone theoretical novelty or substantially larger empirical improvement over the Findings threshold.)",
    "ACL 2027 (ARR February 2027 cycle — comfortable fallback for all modes, and primary target for manual mode with 3-4 month timeline. The extended timeline allows: (a) stronger empirical coverage (additional datasets, further ablation), (b) optional GDPO+adaptive-weight combination experiment as a concrete future-direction follow-up, (c) tighter theoretical integration with arXiv:2602.14872's relay regime framework. Note: the August 2026 ARR cycle commits to EACL 2027, not EMNLP 2026 — this is verified from aclrollingreview.org/dates.)"
  ],
  "level": "top-tier",
  "key_references": [
    "ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose piecewise conditioning as the mechanism; does not cover RAMS/WikiEvents/MAVEN",
    "RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), curriculum coefficient shifting weight over training, Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition, but for multimodal reasoning not IE",
    "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — normalizes each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation to prevent advantage collapse where distinct reward combinations map to identical normalized values; GRPO sums rewards before normalization, losing relative signal; GDPO applied to tool calling (+4.73% BFCL live accuracy), math (+6.3% AIME for DeepSeek-R1-1.5B), coding; NOT applied to IE; orthogonal to proposed adaptive weights (normalization-level fix vs. weighting-level curriculum); combination of GDPO normalization + proposed adaptive weights is a concrete future direction",
    "On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for mixed-difficulty RLVR on L-step compositional tasks: when difficulty ratio R = O(1), gradient signals on easier horizons make harder horizons tractable (Theorem 5.2: inter-horizon plateau exponentially shorter than grokking regime); implicit curriculum emerges at task level; does NOT analyze reward decomposition; proposed Contribution 1 extends relay concept from task-level to reward-component-level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness",
    "Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — proves Reward Decomposition Theorem bounding sub-optimality gap between decomposed per-component and joint GRPO optimization; convergence to first-order stationary point at O(1/√T); applied to LVLMs with multiple reward signals (visual reasoning, instruction following, factual accuracy); proposed Contribution 1 complements this by identifying the structural IE-specific property (continuous span-IoU vs. joint span+type conjunction) that makes early-training variance reduction benefit dominate the sub-optimality cost characterized in this theorem",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; proposes hypervolume-guided and gradient-based adaptive weight optimization compatible with GRPO; motivation for adaptive component weights",
    "APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking (high-variance reward components dominating gradients) in multi-objective RL; per-objective priority based on Learning Potential × Conflict Penalty × Progress Need; 10.9× hypervolume vs. static weighting; motivation for variance-aware weight adaptation",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary EE baseline that ProUIE fails to beat and the performance target for this work",
    "Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that span boundary detection is prerequisite for entity typing: removing boundary regression causes 36.73% F1 drop for long entities on ACE04; motivation for span-first curriculum",
    "T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence for span-before-type ordering",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)",
    "REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings) — joint EAE+RE via supervised warm-up + joint RL, single joint reward, excludes NER",
    "R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025) — RE only, single reward",
    "Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025) — scientific NER+RE, single composite reward, no EE",
    "EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "RAMS: Multi-Sentence Argument Linking (ACL 2020)",
    "WikiEvents: Document-level Event Argument Extraction (NAACL 2021)"
  ],
  "description": "Joint NER+RE+EE GRPO training fails on event extraction because all existing reward designs treat (span, type) pairs as atomic — providing near-zero gradient when span localization is correct but type classification fails. CurriculumRLVR-IE addresses this with three contributions: (1) a formal gradient variance analysis showing that span-boundary rewards, being continuous span-IoU signals rather than low-probability span-AND-type conjunctions, have systematically lower variance in early training, inducing a span→type→argument sequential convergence (curriculum) as a consequence of reward decomposition rather than explicit scheduling — positioned as a reward-component-level instantiation of the relay regime framework from arXiv:2602.14872 and complementing the Reward Decomposition Theorem of arXiv:2604.19857; (2) an adaptive component weight scheme replacing fixed weights, motivated by arXiv:2509.11452's proof that fixed-weight scalarization is suboptimal and APEX's variance hijacking analysis, which up-weights lagging components with low variance and shifts weight as each component converges — explicitly distinguished from GDPO (arXiv:2601.05242, ICML 2026), which prevents advantage collapse at the normalization level and is orthogonal/combinable with adaptive aggregation weights; the scheme includes a plateau detector (F1_i improvement <1% over 200 steps triggers convergence regardless of θ) and a θ ∈ {0.6, 0.7, 0.8} sensitivity analysis from saved checkpoints; (3) per-component F1 learning curves logged every 50 GRPO steps as a falsifiable empirical test of the curriculum-induction hypothesis. The primary foil is ProUIE (arXiv:2604.10633, Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%), whose SFR piecewise structure (as we infer from Eq. 9-10) weakens argument gradient when trigger matching fails. The backbone is Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run + one main GRPO run + checkpoint-derived ablations, total ~130-165 H100-hours within 200 H100-hour ceiling. Target: EMNLP 2026 Findings via May 25 ARR submission (human-in-loop and auto modes); ACL 2027 Main via February 2027 ARR (manual mode and fallback).",
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
  "promptId": "d917b6f7-9f45-46d8-a588-62c8ab0f7bb8",
  "type": "user",
  "uuid": "7a799e09-427a-49f8-bb01-aace14fd41ec",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:03:05.228Z_

```json
{
  "parentUuid": "7a799e09-427a-49f8-bb01-aace14fd41ec",
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
  "uuid": "f6d05954-a672-4a24-97db-81f171740759",
  "timestamp": "2026-05-10T08:03:05.228Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:03:05.228Z_

```json
{
  "parentUuid": "f6d05954-a672-4a24-97db-81f171740759",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5bedba63-84b9-4a11-97c0-b84bf6f2742d",
  "timestamp": "2026-05-10T08:03:05.228Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
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
  "leafUuid": "5bedba63-84b9-4a11-97c0-b84bf6f2742d",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled GRPO for joint NER+RE+EE with adaptive weights",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:08:50.640Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea that has gone through 4 rounds of revision. The core idea is CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weighting for Joint NER+RE+EE.

This is Round 5 of review. Let me assess what has been addressed from Round 4 issues:

Round 4 issues were:
1. GDPO (arXiv:2601.05242) - uncited competitor
2. 'The Implicit Curriculum' (arXiv:2602.14872) - uncited theoretical parallel


3. arXiv:2604.19857 - uncited theoretical parallel (Reward Decomposition)
4. Adaptive weight θ hyperparameter risk
5. EMNLP Main vs Findings realism

Looking at the current Round 5 submission, GDPO is now properly cited and positioned as using fixed aggregation weights while the proposed approach adaptively adjusts them based on convergence progress. I need to check whether the other three uncited papers have been addressed and whether the hyperparameter sensitivity and venue positioning concerns have been resolved.

Now I'm verifying the existence and claims of the key papers referenced: ProUIE, GDPO, the learning dynamics paper, and the reward decomposition work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bedba63-84b9-4a11-97c0-b84bf6f2742d",
  "isSidechain": false,
  "requestId": "req_011CatYEueFNSj9vsrRU4z9R",
  "type": "assistant",
  "uuid": "48429c78-93cc-4778-a2fd-912a3bf7a8e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012xXvYiCfvPSrwa6oa71vDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24368,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1775,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24368
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

_source line 9 · 2026-05-10T08:08:50.642Z_

I'll conduct independent research to verify this idea's claims before issuing a verdict on Round 5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48429c78-93cc-4778-a2fd-912a3bf7a8e6",
  "isSidechain": false,
  "requestId": "req_011CatYEueFNSj9vsrRU4z9R",
  "type": "assistant",
  "uuid": "538e0fcd-d091-461d-b98e-7ae092b42534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012xXvYiCfvPSrwa6oa71vDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24368,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1775,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24368
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

_source line 10 · 2026-05-10T08:08:50.721Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FG6S8jPE53YyCeQihD75vj`</summary>

```json
{
  "description": "Verify key papers and search for concurrent work in GRPO-based IE",
  "subagent_type": "Explore",
  "prompt": "I need you to search for and verify several papers related to GRPO-based information extraction, and find any concurrent work. Please use WebSearch and WebFetch tools to do real research. This is for adversarial review of a research idea.\n\n**Papers to verify existence and claims:**\n\n1. ProUIE (arXiv:2604.10633) - \"A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction\" - claimed April 2026, GRPO with Stepwise Fine-grained Reward for joint NER+RE+EE, ACE2005 Trigger F1=70.65%, Argument F1=52.58%\n\n2. GDPO (arXiv:2601.05242) - claimed ICML 2026, per-reward normalization in GRPO to prevent advantage collapse, tested on tool calling/math/coding\n\n3. \"On the Learning Dynamics of RLVR at the Edge of Competence\" (arXiv:2602.14872) - claimed February 2026, relay regime formal analysis for RLVR\n\n4. \"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization\" (arXiv:2604.19857) - claimed April 2026, Reward Decomposition Theorem for GRPO\n\n5. RuCL (arXiv:2602.21628) - claimed 2026, GRPO with rubric-based curriculum for multimodal reasoning\n\n**Concurrent work search:**\nSearch for any papers from Jan-May 2026 on these topics:\n- \"GRPO information extraction\" 2026\n- \"span boundary reward GRPO\" 2026\n- \"decomposed reward information extraction\" 2026\n- \"curriculum RLVR NER relation extraction\" 2026\n- \"adaptive reward weighting GRPO\" 2026\n\n**Resource estimate check:**\nSearch for realistic estimates of GRPO training costs for 8B parameter models with LoRA on IE datasets (ACE2005 ~25K examples). What are actual GPU hours reported in similar papers?\n\nPlease do at least 8-10 searches and fetch the abstracts of the key papers to verify claims. Report what you find for each paper and any concurrent work discovered."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "538e0fcd-d091-461d-b98e-7ae092b42534",
  "isSidechain": false,
  "requestId": "req_011CatYEueFNSj9vsrRU4z9R",
  "type": "assistant",
  "uuid": "c1c6507f-a122-4570-a2b9-fde92b03d7c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012xXvYiCfvPSrwa6oa71vDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24368,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1775,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24368
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

_source line 11 · 2026-05-10T08:08:50.764Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PaA5HhCfdmg6RbhV5gAcVH`</summary>

```json
{
  "description": "Search for SOTA on ACE2005 IE benchmarks and recent RLVR IE work",
  "subagent_type": "Explore",
  "prompt": "I need you to independently verify the current state-of-the-art for information extraction benchmarks and find recent relevant work. This is for adversarial peer review of a research paper on GRPO-based joint IE. Use WebSearch and WebFetch tools.\n\n**Search tasks:**\n\n1. Find current SOTA on ACE2005 event extraction (trigger and argument F1). What are the best published numbers as of early 2026? Search \"ACE2005 event extraction state of the art 2026\" and \"ACE2005 argument extraction best results\".\n\n2. Find current SOTA on ACE2005 NER and relation extraction. \n\n3. Search Papers With Code for ACE2005 event extraction leaderboard: try fetching https://paperswithcode.com/sota/event-extraction-on-ace-2005\n\n4. Search for any papers combining span-boundary detection with RLVR/GRPO training. Try \"span boundary reinforcement learning NER\" and \"span detection GRPO training\".\n\n5. Search for recent (2025-2026) papers on joint IE with large language models: \"joint information extraction LLM 2026\" and \"unified IE GRPO 2025 2026\".\n\n6. Search for RAMS benchmark evaluation: what recent methods have evaluated on RAMS? Are there strong baselines?\n\n7. Search for \"R2GRPO scientific information extraction\" to verify this paper exists.\n\n8. Check if EXTRACT-0 (arXiv:2509.22906) is a real paper.\n\n9. Search for \"dynamic reward weighting GRPO\" 2025-2026 to find any competitors to the adaptive weighting claim.\n\n10. Search for \"APEX multi-objective alignment\" arXiv:2601.06574 to verify this paper.\n\nReport all findings with paper titles, venues, and key numbers. Flag any papers that seem to be strong competitors to the proposed CurriculumRLVR-IE idea."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1c6507f-a122-4570-a2b9-fde92b03d7c1",
  "isSidechain": false,
  "requestId": "req_011CatYEueFNSj9vsrRU4z9R",
  "type": "assistant",
  "uuid": "0ca07f0d-0090-4d50-8286-c3968e0ea772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012xXvYiCfvPSrwa6oa71vDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24368,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1775,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 24368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24368
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

_source line 12 · 2026-05-10T08:10:47.791Z_

<details><summary>↩ Tool result · `toolu_01FG6S8jPE53YyCeQihD75vj`</summary>

```text
Excellent! I now have comprehensive information. Let me compile my findings into a detailed report.

## Comprehensive Research Verification Report: GRPO-Based Information Extraction Papers and Concurrent Work

Based on 15+ targeted searches and paper fetches, here are my findings for your adversarial review:

---

### **VERIFIED PAPERS**

#### 1. **ProUIE (arXiv:2604.10633)** ✓ VERIFIED
- **Title**: "A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction"
- **Submission**: April 2026 (claimed correctly)
- **Status**: Paper exists and is indexed on arXiv
- **Key Claims Verified**:
  - Uses GRPO with **Stepwise Fine-grained Reward (SFR)** decomposing structural correctness into progressively finer units ✓
  - Covers joint NER+RE+EE tasks ✓
  - Tested on 36 public datasets ✓
  - Three-stage approach: Complete Modeling (CM) → Streamlined Alignment (SA) → Deep Exploration (DE) ✓
- **Specific Metrics Status**: The abstract confirms the paper exists but the exact ACE2005 Trigger F1=70.65%, Argument F1=52.58% claims **could not be verified from abstract/summary**. Would need full PDF access to validate exact numbers.
- **Source**: [ProUIE arXiv:2604.10633](https://arxiv.org/abs/2604.10633)

#### 2. **GDPO (arXiv:2601.05242)** ✓ VERIFIED
- **Title**: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
- **Venue Claim**: ICML 2026 ✓ CONFIRMED (ICML Poster 63333)
- **Submission**: January 2026 (claimed correctly)
- **Status**: Paper exists, has official implementation [GitHub: NVlabs/GDPO](https://github.com/NVlabs/GDPO)
- **Key Claims Verified**:
  - Per-reward normalization prevents advantage collapse ✓
  - Tests on tool calling, math, and coding tasks ✓
  - Outperforms GRPO on all three domains ✓
- **Technical Detail Verified**: GDPO applies group-wise normalization on individual rewards independently before aggregation, addressing GRPO's issue of collapsing distinct reward combinations into identical advantage values ✓

#### 3. **"On the Learning Dynamics of RLVR at the Edge of Competence" (arXiv:2602.14872)** ✓ VERIFIED
- **Title**: "On the Learning Dynamics of RLVR at the Edge of Competence"
- **Submission**: February 16, 2026 (claimed correctly)
- **Status**: Paper exists and is indexed
- **Key Claims Verified**:
  - Relay regime formal analysis for RLVR ✓
  - Explains how smooth difficulty spectrum enables continuous learning ✓
  - Adaptive Fourier analysis techniques on finite groups ✓
  - Shows grokking-type phase transitions with discontinuous spectra ✓
- **Critical Detail**: Introduces "implicit curriculum" concept where RLVR naturally learns easier problems first, shaping the frontier for harder ones

#### 4. **"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization" (arXiv:2604.19857)** ✓ VERIFIED
- **Submission**: April 2026 (claimed correctly)
- **Status**: Paper exists and is indexed
- **Key Claims Verified**:
  - **Reward Decomposition Theorem** derives bounds on per-component vs. joint optimization ✓
  - GRPO convergence rate proven as **O(1/√T)** with explicit dependence on reward components and group size ✓
  - PAC-Bayes generalization bound for tool-augmented policies ✓
  - Introduces Tool-Augmented MDP (TA-MDP) framework ✓
- **Source**: [arXiv:2604.19857](https://arxiv.org/abs/2604.19857)

#### 5. **RuCL (arXiv:2602.21628)** ✓ VERIFIED
- **Title**: "RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning"
- **Submission**: February 25, 2026 (revised March 3, 2026)
- **Status**: Paper exists and is indexed
- **Key Claims Verified**:
  - Rubric-based curriculum learning for multimodal reasoning ✓
  - Integration with GRPO ✓ (per search results: "Integrated with GRPO")
  - Stratifies evaluation rubrics into foundational and advanced categories ✓
  - Reports state-of-the-art on 7B-scale reasoning models ✓
  - Mitigates reward hacking and training instability ✓
- **Metrics**: Paper reports achieving "state-of-the-art accuracy of 60.06%" with Qwen2.5-VL-7B (+7.83% improvement)
- **Source**: [RuCL arXiv:2602.21628](https://arxiv.org/abs/2602.21628)

---

### **CONCURRENT WORK DISCOVERED**

#### 1. **R1-RE (arXiv:2507.04642)** - Cross-Domain Relation Extraction with RLVR
- **Contribution**: First RLVR framework for RE tasks, reframing RE as guided reasoning
- **Performance**: R1-RE-7B achieves ~70% OOD accuracy (on par with GPT-4o)
- **Key Innovation**: Reasoning-guided annotation approach improves OOD robustness by up to 30pp over supervised baselines
- **Datasets**: SemEval-2010 and proprietary MDKG dataset
- **Source**: [R1-RE arXiv:2507.04642](https://arxiv.org/abs/2507.04642)

#### 2. **R2GRPO** - Relevance and Rule-Induced GRPO for Scientific IE
- **Contribution**: Composite reward function combining relevance and rule-induction signals
- **Method**: Two-stage approach with MimicSFT (structured reasoning templates) + R2GRPO
- **Results**: Outperforms supervised baselines on SciER dataset for both NER and RE, especially on RE tasks
- **Framework**: Applied to scientific information extraction with Qwen2.5-7B-Instruct
- **Source**: [Beyond path selection paper](https://arxiv.org/html/2505.22068)

#### 3. **MAESTRO** - Meta-learning Adaptive Estimation of Scalarization Trade-offs
- **Contribution**: Dynamically adapts reward weights based on prompt-response semantics
- **Innovation**: Conductor meta-policy selects reward scalarization strategy per prompt-response pair
- **Context**: Uses terminal hidden states as context for reward weighting decisions
- **Status**: 2026 publication

#### 4. **DW-GRPO** - Dynamic Weighting GRPO
- **Contribution**: Monitors rate of change for each reward component, dynamically adjusts weights via softmax
- **Innovation**: Assigns higher weights to objectives showing slower progress, preventing policy collapse
- **Mechanism**: Temperature-based softmax weighting with lagging component detection
- **Status**: 2026 publication

#### 5. **HA-DW** - History-Aware Adaptive Difficulty Weighting
- **Contribution**: Adaptive reweighting based on evolving difficulty anchor
- **Innovation**: Compensates for bias in group-relative advantage estimation
- **Integration**: Works with GRPO to adjust advantages dynamically based on training history
- **Status**: 2026 publication

#### 6. **DIVA-GRPO** - Difficulty-Adaptive Variant Advantage
- **Contribution**: Batch z-score normalization + difficulty-weighted scaling
- **Innovation**: Reward-range-based rescaling prevents inflated advantages from minor reward differences
- **Application**: Multimodal reasoning tasks
- **Status**: 2026 publication

#### 7. **S-GRPO** (arXiv:2604.16557) - Unified Post-Training for Vision-Language Models
- **Contribution**: Extends GRPO to unified VLM post-training
- **Status**: April 2026 submission

#### 8. **EVPO** (arXiv:2604.19485) - Explained Variance Policy Optimization
- **Contribution**: Adaptive critic utilization in LLM post-training with GRPO
- **Status**: April 2026 submission

---

### **RESOURCE ESTIMATES FOR ACE2005-SCALE IE TRAINING**

#### GPU Requirements for 8B + LoRA on ACE2005:
- **ACE2005 size**: ~25K examples (you specified correctly), 599 documents
- **A100 80GB with LoRA (r=64)**: ✓ Can fit comfortably
- **H200 with LoRA (r=64)**: ✓ Recommended for stability
- **Memory overhead**: GRPO requires 2-3x VRAM of SFT
- **Batch configuration examples**:
  - Single A100: Tested example was DeepSeek-R1-Distill-Qwen-7B with ~$30.97 total spend
  - H200: 141GB memory allows disaggregated training at scale

#### Training Duration Data Points:
- **DeepSeek R1 (large-scale)**: 2.79 million GPU hours on H800s = 198 hours for preliminary R1-Zero
- **Single A100 example**: ~$30.97 for smart contract task (full cost estimate)
- **H200 disaggregated GRPO**: $152.16 for 24-hour run (cheaper than PPO at $190.08)
- **Batch size**: 32 unique questions typical = 512 batch size per step

#### Cost Estimation for ACE2005 (8B + LoRA):
- **Ballpark**: 50-200 GPU hours on A100 (based on task complexity and available metrics)
- **At typical cloud pricing**: $150-600 range
- **Note**: No exact papers found reporting ACE2005-specific GRPO training hours; estimates extrapolated from similar-scale tasks

---

### **CRITICAL ASSESSMENT FOR ADVERSARIAL REVIEW**

#### Strengths of Verified Work:
1. ✓ All five target papers **exist and are indexed on arXiv**
2. ✓ GDPO confirmed accepted to ICML 2026
3. ✓ Theoretical contributions well-documented (convergence proofs, decomposition theorems)
4. ✓ Concurrent work shows active research area with multiple reward-weighting approaches
5. ✓ ProUIE's three-stage approach (CM→SA→DE) is novel for unified IE

#### Gaps and Cautions:
1. **ProUIE exact metrics**: ACE2005 F1 scores (70.65% Trigger, 52.58% Argument) **could not be verified from abstracts** - need full paper PDF
2. **No papers found specifically on "span boundary reward GRPO"** - this phrase appears in discussions of GRPO's implicit process rewards but not as named method
3. **ACE2005 GRPO training cost**: No published papers found reporting exact GPU hours for this specific dataset+model combo
4. **Resource estimates are extrapolated**, not direct from ACE2005-specific experiments
5. **R1-RE is from July 2025 submission** (not within Jan-May 2026 window, though published in 2026)
6. **Reward decomposition approaches proliferating**: 6+ variants found (MAESTRO, DW-GRPO, HA-DW, DIVA-GRPO, etc.), suggesting the space is competitive

#### Verification Status Summary:
| Paper | Exists | Metrics Verified | Venue Confirmed | Concurrent Work |
|-------|--------|------------------|-----------------|-----------------|
| ProUIE | ✓ | Partial | No venue claim | Yes (R2GRPO, others) |
| GDPO | ✓ | Partial | ✓ ICML 2026 | Yes (multiple variants) |
| Edge of Competence | ✓ | Yes | No venue claim | Yes (implicit curriculum papers) |
| Reward Decomposition | ✓ | Partial | No venue claim | Yes (MAESTRO, DW-GRPO, HA-DW) |
| RuCL | ✓ | Partial | No venue claim | Yes (multiple curriculum methods) |

---

### **Sources Referenced**

Key papers verified:
- [ProUIE arXiv:2604.10633](https://arxiv.org/abs/2604.10633)
- [GDPO arXiv:2601.05242](https://arxiv.org/abs/2601.05242) - [GitHub](https://github.com/NVlabs/GDPO)
- [Edge of Competence arXiv:2602.14872](https://arxiv.org/abs/2602.14872)
- [Reward Decomposition arXiv:2604.19857](https://arxiv.org/abs/2604.19857)
- [RuCL arXiv:2602.21628](https://arxiv.org/abs/2602.21628)
- [R1-RE arXiv:2507.04642](https://arxiv.org/abs/2507.04642)
- [R2GRPO paper](https://arxiv.org/html/2505.22068)
- [GDPO ICML Poster](https://icml.cc/virtual/2026/poster/63333)
- [DeepSeek R1 Training Analysis](https://www.fluence.network/blog/deepseek-r1-training/)
- [Spheron GRPO Guide 2026](https://www.spheron.network/blog/grpo-fine-tuning-gpu-cloud/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1c6507f-a122-4570-a2b9-fde92b03d7c1",
  "isSidechain": false,
  "promptId": "d917b6f7-9f45-46d8-a588-62c8ab0f7bb8",
  "type": "user",
  "uuid": "9ba22183-023a-4985-9518-ebf7852c81b2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for and verify several papers related to GRPO-based information extraction, and find any concurrent work. Please use WebSearch and WebFetch tools to do real research. This is for adversarial review of a research idea.\n\n**Papers to verify existence and claims:**\n\n1. ProUIE (arXiv:2604.10633) - \"A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction\" - claimed April 2026, GRPO with Stepwise Fine-grained Reward for joint NER+RE+EE, ACE2005 Trigger F1=70.65%, Argument F1=52.58%\n\n2. GDPO (arXiv:2601.05242) - claimed ICML 2026, per-reward normalization in GRPO to prevent advantage collapse, tested on tool calling/math/coding\n\n3. \"On the Learning Dynamics of RLVR at the Edge of Competence\" (arXiv:2602.14872) - claimed February 2026, relay regime formal analysis for RLVR\n\n4. \"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization\" (arXiv:2604.19857) - claimed April 2026, Reward Decomposition Theorem for GRPO\n\n5. RuCL (arXiv:2602.21628) - claimed 2026, GRPO with rubric-based curriculum for multimodal reasoning\n\n**Concurrent work search:**\nSearch for any papers from Jan-May 2026 on these topics:\n- \"GRPO information extraction\" 2026\n- \"span boundary reward GRPO\" 2026\n- \"decomposed reward information extraction\" 2026\n- \"curriculum RLVR NER relation extraction\" 2026\n- \"adaptive reward weighting GRPO\" 2026\n\n**Resource estimate check:**\nSearch for realistic estimates of GRPO training costs for 8B parameter models with LoRA on IE datasets (ACE2005 ~25K examples). What are actual GPU hours reported in similar papers?\n\nPlease do at least 8-10 searches and fetch the abstracts of the key papers to verify claims. Report what you find for each paper and any concurrent work discovered.",
    "agentId": "af409eaa543c222e5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I now have comprehensive information. Let me compile my findings into a detailed report.\n\n## Comprehensive Research Verification Report: GRPO-Based Information Extraction Papers and Concurrent Work\n\nBased on 15+ targeted searches and paper fetches, here are my findings for your adversarial review:\n\n---\n\n### **VERIFIED PAPERS**\n\n#### 1. **ProUIE (arXiv:2604.10633)** ✓ VERIFIED\n- **Title**: \"A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction\"\n- **Submission**: April 2026 (claimed correctly)\n- **Status**: Paper exists and is indexed on arXiv\n- **Key Claims Verified**:\n  - Uses GRPO with **Stepwise Fine-grained Reward (SFR)** decomposing structural correctness into progressively finer units ✓\n  - Covers joint NER+RE+EE tasks ✓\n  - Tested on 36 public datasets ✓\n  - Three-stage approach: Complete Modeling (CM) → Streamlined Alignment (SA) → Deep Exploration (DE) ✓\n- **Specific Metrics Status**: The abstract confirms the paper exists but the exact ACE2005 Trigger F1=70.65%, Argument F1=52.58% claims **could not be verified from abstract/summary**. Would need full PDF access to validate exact numbers.\n- **Source**: [ProUIE arXiv:2604.10633](https://arxiv.org/abs/2604.10633)\n\n#### 2. **GDPO (arXiv:2601.05242)** ✓ VERIFIED\n- **Title**: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n- **Venue Claim**: ICML 2026 ✓ CONFIRMED (ICML Poster 63333)\n- **Submission**: January 2026 (claimed correctly)\n- **Status**: Paper exists, has official implementation [GitHub: NVlabs/GDPO](https://github.com/NVlabs/GDPO)\n- **Key Claims Verified**:\n  - Per-reward normalization prevents advantage collapse ✓\n  - Tests on tool calling, math, and coding tasks ✓\n  - Outperforms GRPO on all three domains ✓\n- **Technical Detail Verified**: GDPO applies group-wise normalization on individual rewards independently before aggregation, addressing GRPO's issue of collapsing distinct reward combinations into identical advantage values ✓\n\n#### 3. **\"On the Learning Dynamics of RLVR at the Edge of Competence\" (arXiv:2602.14872)** ✓ VERIFIED\n- **Title**: \"On the Learning Dynamics of RLVR at the Edge of Competence\"\n- **Submission**: February 16, 2026 (claimed correctly)\n- **Status**: Paper exists and is indexed\n- **Key Claims Verified**:\n  - Relay regime formal analysis for RLVR ✓\n  - Explains how smooth difficulty spectrum enables continuous learning ✓\n  - Adaptive Fourier analysis techniques on finite groups ✓\n  - Shows grokking-type phase transitions with discontinuous spectra ✓\n- **Critical Detail**: Introduces \"implicit curriculum\" concept where RLVR naturally learns easier problems first, shaping the frontier for harder ones\n\n#### 4. **\"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization\" (arXiv:2604.19857)** ✓ VERIFIED\n- **Submission**: April 2026 (claimed correctly)\n- **Status**: Paper exists and is indexed\n- **Key Claims Verified**:\n  - **Reward Decomposition Theorem** derives bounds on per-component vs. joint optimization ✓\n  - GRPO convergence rate proven as **O(1/√T)** with explicit dependence on reward components and group size ✓\n  - PAC-Bayes generalization bound for tool-augmented policies ✓\n  - Introduces Tool-Augmented MDP (TA-MDP) framework ✓\n- **Source**: [arXiv:2604.19857](https://arxiv.org/abs/2604.19857)\n\n#### 5. **RuCL (arXiv:2602.21628)** ✓ VERIFIED\n- **Title**: \"RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning\"\n- **Submission**: February 25, 2026 (revised March 3, 2026)\n- **Status**: Paper exists and is indexed\n- **Key Claims Verified**:\n  - Rubric-based curriculum learning for multimodal reasoning ✓\n  - Integration with GRPO ✓ (per search results: \"Integrated with GRPO\")\n  - Stratifies evaluation rubrics into foundational and advanced categories ✓\n  - Reports state-of-the-art on 7B-scale reasoning models ✓\n  - Mitigates reward hacking and training instability ✓\n- **Metrics**: Paper reports achieving \"state-of-the-art accuracy of 60.06%\" with Qwen2.5-VL-7B (+7.83% improvement)\n- **Source**: [RuCL arXiv:2602.21628](https://arxiv.org/abs/2602.21628)\n\n---\n\n### **CONCURRENT WORK DISCOVERED**\n\n#### 1. **R1-RE (arXiv:2507.04642)** - Cross-Domain Relation Extraction with RLVR\n- **Contribution**: First RLVR framework for RE tasks, reframing RE as guided reasoning\n- **Performance**: R1-RE-7B achieves ~70% OOD accuracy (on par with GPT-4o)\n- **Key Innovation**: Reasoning-guided annotation approach improves OOD robustness by up to 30pp over supervised baselines\n- **Datasets**: SemEval-2010 and proprietary MDKG dataset\n- **Source**: [R1-RE arXiv:2507.04642](https://arxiv.org/abs/2507.04642)\n\n#### 2. **R2GRPO** - Relevance and Rule-Induced GRPO for Scientific IE\n- **Contribution**: Composite reward function combining relevance and rule-induction signals\n- **Method**: Two-stage approach with MimicSFT (structured reasoning templates) + R2GRPO\n- **Results**: Outperforms supervised baselines on SciER dataset for both NER and RE, especially on RE tasks\n- **Framework**: Applied to scientific information extraction with Qwen2.5-7B-Instruct\n- **Source**: [Beyond path selection paper](https://arxiv.org/html/2505.22068)\n\n#### 3. **MAESTRO** - Meta-learning Adaptive Estimation of Scalarization Trade-offs\n- **Contribution**: Dynamically adapts reward weights based on prompt-response semantics\n- **Innovation**: Conductor meta-policy selects reward scalarization strategy per prompt-response pair\n- **Context**: Uses terminal hidden states as context for reward weighting decisions\n- **Status**: 2026 publication\n\n#### 4. **DW-GRPO** - Dynamic Weighting GRPO\n- **Contribution**: Monitors rate of change for each reward component, dynamically adjusts weights via softmax\n- **Innovation**: Assigns higher weights to objectives showing slower progress, preventing policy collapse\n- **Mechanism**: Temperature-based softmax weighting with lagging component detection\n- **Status**: 2026 publication\n\n#### 5. **HA-DW** - History-Aware Adaptive Difficulty Weighting\n- **Contribution**: Adaptive reweighting based on evolving difficulty anchor\n- **Innovation**: Compensates for bias in group-relative advantage estimation\n- **Integration**: Works with GRPO to adjust advantages dynamically based on training history\n- **Status**: 2026 publication\n\n#### 6. **DIVA-GRPO** - Difficulty-Adaptive Variant Advantage\n- **Contribution**: Batch z-score normalization + difficulty-weighted scaling\n- **Innovation**: Reward-range-based rescaling prevents inflated advantages from minor reward differences\n- **Application**: Multimodal reasoning tasks\n- **Status**: 2026 publication\n\n#### 7. **S-GRPO** (arXiv:2604.16557) - Unified Post-Training for Vision-Language Models\n- **Contribution**: Extends GRPO to unified VLM post-training\n- **Status**: April 2026 submission\n\n#### 8. **EVPO** (arXiv:2604.19485) - Explained Variance Policy Optimization\n- **Contribution**: Adaptive critic utilization in LLM post-training with GRPO\n- **Status**: April 2026 submission\n\n---\n\n### **RESOURCE ESTIMATES FOR ACE2005-SCALE IE TRAINING**\n\n#### GPU Requirements for 8B + LoRA on ACE2005:\n- **ACE2005 size**: ~25K examples (you specified correctly), 599 documents\n- **A100 80GB with LoRA (r=64)**: ✓ Can fit comfortably\n- **H200 with LoRA (r=64)**: ✓ Recommended for stability\n- **Memory overhead**: GRPO requires 2-3x VRAM of SFT\n- **Batch configuration examples**:\n  - Single A100: Tested example was DeepSeek-R1-Distill-Qwen-7B with ~$30.97 total spend\n  - H200: 141GB memory allows disaggregated training at scale\n\n#### Training Duration Data Points:\n- **DeepSeek R1 (large-scale)**: 2.79 million GPU hours on H800s = 198 hours for preliminary R1-Zero\n- **Single A100 example**: ~$30.97 for smart contract task (full cost estimate)\n- **H200 disaggregated GRPO**: $152.16 for 24-hour run (cheaper than PPO at $190.08)\n- **Batch size**: 32 unique questions typical = 512 batch size per step\n\n#### Cost Estimation for ACE2005 (8B + LoRA):\n- **Ballpark**: 50-200 GPU hours on A100 (based on task complexity and available metrics)\n- **At typical cloud pricing**: $150-600 range\n- **Note**: No exact papers found reporting ACE2005-specific GRPO training hours; estimates extrapolated from similar-scale tasks\n\n---\n\n### **CRITICAL ASSESSMENT FOR ADVERSARIAL REVIEW**\n\n#### Strengths of Verified Work:\n1. ✓ All five target papers **exist and are indexed on arXiv**\n2. ✓ GDPO confirmed accepted to ICML 2026\n3. ✓ Theoretical contributions well-documented (convergence proofs, decomposition theorems)\n4. ✓ Concurrent work shows active research area with multiple reward-weighting approaches\n5. ✓ ProUIE's three-stage approach (CM→SA→DE) is novel for unified IE\n\n#### Gaps and Cautions:\n1. **ProUIE exact metrics**: ACE2005 F1 scores (70.65% Trigger, 52.58% Argument) **could not be verified from abstracts** - need full paper PDF\n2. **No papers found specifically on \"span boundary reward GRPO\"** - this phrase appears in discussions of GRPO's implicit process rewards but not as named method\n3. **ACE2005 GRPO training cost**: No published papers found reporting exact GPU hours for this specific dataset+model combo\n4. **Resource estimates are extrapolated**, not direct from ACE2005-specific experiments\n5. **R1-RE is from July 2025 submission** (not within Jan-May 2026 window, though published in 2026)\n6. **Reward decomposition approaches proliferating**: 6+ variants found (MAESTRO, DW-GRPO, HA-DW, DIVA-GRPO, etc.), suggesting the space is competitive\n\n#### Verification Status Summary:\n| Paper | Exists | Metrics Verified | Venue Confirmed | Concurrent Work |\n|-------|--------|------------------|-----------------|-----------------|\n| ProUIE | ✓ | Partial | No venue claim | Yes (R2GRPO, others) |\n| GDPO | ✓ | Partial | ✓ ICML 2026 | Yes (multiple variants) |\n| Edge of Competence | ✓ | Yes | No venue claim | Yes (implicit curriculum papers) |\n| Reward Decomposition | ✓ | Partial | No venue claim | Yes (MAESTRO, DW-GRPO, HA-DW) |\n| RuCL | ✓ | Partial | No venue claim | Yes (multiple curriculum methods) |\n\n---\n\n### **Sources Referenced**\n\nKey papers verified:\n- [ProUIE arXiv:2604.10633](https://arxiv.org/abs/2604.10633)\n- [GDPO arXiv:2601.05242](https://arxiv.org/abs/2601.05242) - [GitHub](https://github.com/NVlabs/GDPO)\n- [Edge of Competence arXiv:2602.14872](https://arxiv.org/abs/2602.14872)\n- [Reward Decomposition arXiv:2604.19857](https://arxiv.org/abs/2604.19857)\n- [RuCL arXiv:2602.21628](https://arxiv.org/abs/2602.21628)\n- [R1-RE arXiv:2507.04642](https://arxiv.org/abs/2507.04642)\n- [R2GRPO paper](https://arxiv.org/html/2505.22068)\n- [GDPO ICML Poster](https://icml.cc/virtual/2026/poster/63333)\n- [DeepSeek R1 Training Analysis](https://www.fluence.network/blog/deepseek-r1-training/)\n- [Spheron GRPO Guide 2026](https://www.spheron.network/blog/grpo-fine-tuning-gpu-cloud/)"
      }
    ],
    "totalDurationMs": 117062,
    "totalTokens": 43491,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2837,
      "cache_read_input_tokens": 37167,
      "output_tokens": 3480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3480,
          "cache_read_input_tokens": 37167,
          "cache_creation_input_tokens": 2837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2837,
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
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "c1c6507f-a122-4570-a2b9-fde92b03d7c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
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
  "leafUuid": "9ba22183-023a-4985-9518-ebf7852c81b2",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled GRPO for joint NER+RE+EE with adaptive weights",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Tool result

_source line 15 · 2026-05-10T08:11:28.992Z_

<details><summary>↩ Tool result · `toolu_01PaA5HhCfdmg6RbhV5gAcVH`</summary>

```text
Now let me compile a comprehensive final report based on all the research I've conducted:

## COMPREHENSIVE STATE-OF-THE-ART VERIFICATION REPORT

Based on systematic searching across multiple sources, here are my findings for your adversarial peer review of the GRPO-based joint IE paper:

---

### 1. **ACE2005 EVENT EXTRACTION BENCHMARKS**

**Current SOTA Rankings (Early 2026):**
- Event Extraction SOTA: **DeepStruct multi-task** (ACL 2022)
- Event Argument Extraction SOTA: **NLI+** 
- These are listed as top models on Papers with Code leaderboard

**Recent High-Performance Models (2024-2025):**
- MTCM (Multiple Template Choice Model) - achieves SOTA on ACE2005-EN
- ECPEAE (Event Co-occurrences Prefix Event Argument Extraction) - shows >10% improvements in low-resource settings
- Joint models using dynamic attention matching and graph attention networks

**Key Benchmark Metrics Found:**
- One recent model achieved: 73.3% trigger identification F1, 72.6% trigger classification F1, 55.7% argument identification F1, 54.7% argument classification F1
- Seq2EG reports improvements of 3.4% F1 for event detection and 4.7% F1 for argument classification over baselines on ACE2005

⚠️ **Note:** Specific numeric scores for DeepStruct and NLI+ were not directly accessible in search results, but these remain the cited SOTA models.

---

### 2. **ACE2005 NER AND RELATION EXTRACTION SOTA**

**NER Performance:**
- SOTA F1 score: **89.04%** on ACE2005
- Zhong and Chen (2020) achieved F1 of 90.9 on ACE2005-Ent

**Relation Extraction Performance:**
- REKnow method: **68.3 F1** on ACE2005
- Marker collaborating models achieve SOTA on ACE2005

**Papers with Code Leaderboards:**
- [ACE2005 Benchmark (NER)](https://paperswithcode.com/sota/named-entity-recognition-on-ace-2005)
- [ACE2005 Benchmark (Relation Extraction)](https://paperswithcode.com/sota/relation-extraction-on-ace-2005)

---

### 3. **PAPERS WITH CODE LEADERBOARDS**

Papers with Code shows benchmarks redirecting through Hugging Face for:
- Event Extraction on ACE2005
- Event Argument Extraction on ACE2005
- NER on ACE2005
- Relation Extraction on ACE2005

The leaderboards confirm DeepStruct multi-task and NLI+ as current leaders.

---

### 4. **SPAN-BOUNDARY DETECTION WITH RL/GRPO**

**Key Papers Found:**

a) **SKD-NER (ACL EMNLP 2023)** - Continual NER via Span-based Knowledge Distillation with Reinforcement Learning
   - Uses span-based approach with RL strategies
   - Addresses catastrophic forgetting in continual learning

b) **GPRL (Gaussian Prior Reinforcement Learning)**
   - Formulates nested NER as entity triplet sequence generation
   - Uses Gaussian Prior Adjustment (GPA) for boundary recognition
   - Incorporates Entity Order Reinforcement Learning (EORL)

c) **BGNER (Boundary Guidance Framework, 2025)**
   - Recent boundary-enhanced NER framework

d) **T2-NER (Two-Stage Span-Based Framework)**
   - Unified NER with templates

⚠️ **Competitor Alert:** These papers show that span-based RL approaches for NER are already established, particularly SKD-NER combining knowledge distillation with RL.

---

### 5. **JOINT IE WITH LLMs (2025-2026)**

**Recent Papers:**

a) **Reamend** - Novel LLM augmented joint learning framework for entity-relation extraction
   - Simultaneously recognizes entities and relations
   - Eliminates redundant triplets
   - Published 2025

b) **LLM + ASP Workflow for Joint Entity-Relation Extraction** (2508.12611)
   - Shows 10% training data needed for comparable performance to SOTA JERE systems

c) **AEVS Framework** - Grounds extraction elements to source text to address hallucination
   - Addresses the critical hallucination problem in LLM-based IE

d) **Multi-Document Event Extraction (EMNLP 2025)**
   - Recent work on document-level event extraction

e) **SciEx Framework** - Prompt-driven and RAG-based scientific IE
   - Transforms unstructured research PDFs into structured knowledge

⚠️ **Competitor Alert:** LLM-based joint IE is an active area with multiple recent approaches, particularly addressing hallucination control.

---

### 6. **RAMS BENCHMARK EVALUATION**

**Dataset Specs:**
- 3,993 documents from news articles
- 139 event types, 65 role types
- Derived from real-world news

**Recent SOTA Methods (2025-2026):**

a) **DPFS (Dual-Paradigm Fusion Strategy)** - Integrates classification-based and generative approaches
   - 3.0% improvement over second-best baseline on Argument Classification

b) **SALE (Structure-Aware Large Language Models)** - Two-stage training paradigm
   - Structure-aware fine-tuning + event extraction alignment

c) **SPARE (Semantic-aware Prompt-based Argument Extractor)**
   - Uses document-sentence-entity heterogeneous graph with GCNs
   - Position-aware semantic role attention

**Challenge:** F1 scores drop significantly with increasing distance between triggers and arguments.

---

### 7. **R2GRPO SCIENTIFIC IE VERIFICATION**

⚠️ **FINDING: R2GRPO NOT FOUND** - Search for "R2GRPO scientific information extraction" returned no results. This appears to NOT be a published paper or widely-known framework as of early 2026.

**Related Papers on Scientific IE Found:**
- Structured information extraction from scientific text with LLMs (Nature Commun. 2024)
- SciEx Framework for scientific IE
- Grounded Knowledge Graph Extraction via LLMs with Anchor-Constrained Framework

---

### 8. **EXTRACT-0 (arXiv:2509.22906) VERIFICATION**

✓ **VERIFIED - REAL PAPER**

**Key Details:**
- **Title:** Extract-0: A Specialized Language Model for Document Information Extraction
- **Author:** Henrique Godoy
- **Published:** September 26, 2025
- **Model Size:** 7 billion parameters
- **Venue:** arXiv preprint

**Methodology:**
- Synthetic data generation: 280,128 training examples
- Supervised fine-tuning with LoRA (0.53% weight modification)
- **Reinforcement Learning via GRPO**
- Novel semantic similarity-based reward function

**Performance:**
- Mean reward: **0.573** on 1,000 diverse document extraction tasks
- Outperforms GPT-4.1 (0.457), o3 (0.464), GPT-4.1-2025 (0.459)

**Reward Function Design:**
- MiniLM-L6-v2 embedding similarity for text fields
- Relative difference for numbers
- Temporal distance for dates
- Bipartite matching for lists

**Code/Dataset Available:**
- GitHub: [herniqeu/extract0](https://github.com/herniqeu/extract0)
- HuggingFace Dataset: [HenriqueGodoy/extract-0](https://huggingface.co/datasets/HenriqueGodoy/extract-0)

⚠️ **Competitor Alert: CRITICAL** - Extract-0 directly applies GRPO to information extraction with a semantic similarity-based reward function. This is highly relevant to your work and represents a strong baseline using GRPO for IE.

---

### 9. **DYNAMIC REWARD WEIGHTING & ADAPTIVE WEIGHTING COMPETITORS**

**Three Major Competitors Found:**

#### a) **Dynamic Reward Weighting (arXiv:2509.11452)**
- **Title:** Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting
- **Authors:** Yining Lu et al.
- **Submitted:** September 14, 2025
- **Venue:** TACL'26
- **Status:** Published as conference paper

**Key Innovation:**
- Proposes dynamic reward weighting that adaptively adjusts weights during online RL
- Addresses limitations of fixed-weight linear scalarization
- Two approaches: hypervolume-guided weight adaptation and gradient-based weight optimization
- Outperforms fixed-weight baselines on Pareto optimal solutions

⚠️ **Direct Competitor Alert:** This paper directly addresses adaptive weighting for multi-objective RL, which is a key claim in your CurriculumRLVR-IE work.

#### b) **MAESTRO (arXiv:2601.07208)**
- **Title:** MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization
- **Submitted:** January 2026
- **Key Feature:** Dynamically adapts reward weights according to prompt-response semantics
- **Difference:** Prompt-dependent (not fixed) reward weights

#### c) **SPARD (arXiv:2604.07837)**
- **Title:** SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility
- **Authors:** 13 authors including Xuyang Zhi, Xiaohongshu Inc.
- **Submitted:** April 9, 2026
- **Status:** Very recent work

**Key Innovation:**
- Self-paced curriculum by perceiving learning progress
- Dynamically adjusts multi-objective reward weights
- Integrates Reward Dynamics with Data utility
- Shows improvements across multiple benchmarks

⚠️ **Direct Competitor Alert: CRITICAL** - SPARD combines curriculum learning with dynamic reward weighting for RLVR. This directly overlaps with claimed contributions of CurriculumRLVR-IE.

---

### 10. **APEX MULTI-OBJECTIVE ALIGNMENT (arXiv:2601.06574) VERIFICATION**

✓ **VERIFIED - REAL PAPER**

**Key Details:**
- **Title:** APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation
- **Published:** January 10, 2026
- **Authors:** Dongliang Chen et al. (11 authors)

**Problem Addressed:**
- Fixed weights in multi-objective optimization fail under heterogeneous rewards
- Two mechanistic causes identified:
  1. **Variance hijacking** - reward dispersion causes implicit reweighting
  2. **Gradient conflicts** - competing objectives produce opposing updates

**Solution:**
- Dual-Stage Adaptive Normalization
- P³ Adaptive Priorities combining:
  - Learning potential
  - Conflict penalty
  - Other factors

**Results (Stable Diffusion 3.5):**
- +1.31 PickScore
- +0.35 DeQA
- +0.53 Aesthetics
- Maintains competitive OCR accuracy

⚠️ **Note:** APEX focuses on vision-language generation, not information extraction, but the adaptive weighting methodology is highly relevant.

---

### 11. **CURRICULUM REINFORCEMENT LEARNING FOR RLVR**

**Key Papers:**

#### a) **VCRL (arXiv:2509.19803)**
- **Title:** VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models
- **Submitted:** September 24, 2025
- **Key Innovation:** Uses variance of rollout group rewards to determine sample difficulty
- **Results:** 4.67 point average improvement over GSPO baseline on Qwen3-8B-Base

**Mechanism:**
- Variance-based Dynamic Sampling
- Replay Learning with Memory Bank
- Targets moderate-difficulty samples (higher variance)

#### b) **Implicit Curriculum (arXiv:2602.14872)**
- **Title:** The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards
- **Key Finding:** Mixed-difficulty training naturally creates implicit curriculum without explicit scheduling

#### c) **E2H Reasoner (arXiv:2506.06632)**
- **Title:** Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning
- **Inspiration:** Curriculum learning for RLVR
- **Approach:** Schedule tasks from easy to hard

⚠️ **Competitor Alert: CRITICAL** - VCRL applies curriculum learning specifically to RLVR with variance-based difficulty estimation. This is very close to your CurriculumRLVR-IE concept but applied to mathematical reasoning.

---

### 12. **GRPO FOR INFORMATION EXTRACTION**

**General GRPO Applications Found:**
- Training-Free Group Relative Policy Optimization (2510.08191)
- GRPO for visual information extraction (over 83% on simple, 95.8% on complex questions)
- Retrieval-GRPO - multi-objective framework for dense retrieval
- Code quality improvement with GRPO

**GRPO Overview (2025):**
- Eliminates value model from PPO
- Group-sampling-based baseline estimation
- Significantly reduces computational overhead
- Standard technique for reasoning and structured output tasks

⚠️ **Key Finding:** No specific papers on GRPO applied to joint information extraction (NER+RE+EE) were found, suggesting this is a novel application area.

---

### 13. **OTHER RECENT SPAN DETECTION & EVENT EXTRACTION WORK**

**Hallucination Span Detection with GRPO:**
- Models trained with span-F1 metric rewards
- Issue discovered: reward hacking (defaulting to no hallucinations)
- Solution: class-aware policy optimization with scaling factors

**Recent Event Extraction Generative Approaches (2024-2025):**

a) **GEMS** - Generation-based Event Argument Extraction
   - Permutes event elements for multiple prompts
   - Encodes with concatenated context and ontology
   - Captures diverse structural interactions

b) **KC-GEE** - Knowledge-based Conditioning for Generative Event Extraction
   - Uses knowledge to condition generation

c) **Diffusion Model Approaches** - Context-aware prompt for generation-based EAE

---

### SUMMARY OF COMPETITIVE THREATS

**Direct Competitors to CurriculumRLVR-IE:**

1. **SPARD (arXiv:2604.07837)** ⚠️ HIGHEST RISK
   - Self-paced curriculum + dynamic reward weighting for RLVR
   - General framework across benchmarks
   - April 2026 (very recent)

2. **VCRL (arXiv:2509.19803)** ⚠️ HIGH RISK
   - Variance-based curriculum for RLVR
   - September 2025
   - Applied to math reasoning but methodology is general

3. **Dynamic Reward Weighting (arXiv:2509.11452)** ⚠️ MEDIUM-HIGH RISK
   - Adaptive multi-objective reward weighting
   - TACL'26 acceptance
   - September 2025

4. **Extract-0 (arXiv:2509.22906)** ⚠️ MEDIUM RISK
   - GRPO applied to document IE
   - Semantic similarity-based reward function
   - September 2025

5. **MAESTRO (arXiv:2601.07208)** ⚠️ MEDIUM RISK
   - Adaptive reward weighting conditioned on semantics
   - January 2026

---

### NOVELTY ASSESSMENT

**Potentially Novel About Your Work (if addressing these gaps):**
- Combination of curriculum learning + RLVR + adaptive weighting specifically for **joint IE** (NER+RE+EE)
- Span-boundary specific curriculum strategies
- Specific benchmark results on ACE2005, RAMS, and scientific IE datasets

**Already Covered by Existing Work:**
- Curriculum learning for RLVR ✓ (VCRL, E2H, Implicit Curriculum)
- Dynamic/adaptive reward weighting ✓ (arXiv:2509.11452, MAESTRO, SPARD)
- GRPO for structured extraction ✓ (Extract-0, hallucination detection, visual IE)
- RL for NER/event extraction ✓ (SKD-NER, GPRL, etc.)

---

### KEY RECOMMENDATIONS FOR YOUR REVIEW

1. **Demand specific comparisons** with SPARD and VCRL on IE tasks
2. **Request results on standard benchmarks** (ACE2005 trigger/argument F1, RAMS, scientific IE)
3. **Challenge the novelty claims** about adaptive weighting and curriculum learning
4. **Verify the reward function design** is actually superior to semantic similarity-based rewards (Extract-0)
5. **Check if span-boundary detection improvements** are significant vs. existing boundary-aware approaches
6. **Evaluate against recent prompt/template-based baselines** (MTCM, ECPEAE, GEMS)

Sources:
- [Papers with Code - ACE2005 Event Extraction](https://paperswithcode.com/sota/event-extraction-on-ace-2005)
- [Papers with Code - ACE2005 Event Argument Extraction](https://paperswithcode.com/sota/event-argument-extraction-on-ace-2005)
- [MAVEN: A Massive General Domain Event Detection Dataset](https://arxiv.org/pdf/2004.13590)
- [Prompt for extraction: Multiple templates choice model](https://www.sciencedirect.com/science/article/pii/S0950705124001795)
- [Joint event extraction model with dynamic attention](https://www.nature.com/articles/s41598-025-91501-2)
- [SKD-NER: Continual Named Entity Recognition via Span-based Knowledge Distillation with Reinforcement Learning](https://aclanthology.org/2023.emnlp-main.413/)
- [Gaussian Prior Reinforcement Learning for Nested NER](https://arxiv.org/abs/2305.07266)
- [Large language model augmented joint learning for entity-relation extraction](https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073)
- [Closed-Domain Event Extraction Literature Review January 2025](https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf)
- [Extract-0: A Specialized Language Model for Document Information Extraction](https://arxiv.org/abs/2509.22906)
- [VCRL: Variance-based Curriculum Reinforcement Learning for LLMs](https://arxiv.org/abs/2509.19803)
- [Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting](https://arxiv.org/abs/2509.11452)
- [SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility](https://arxiv.org/abs/2604.07837)
- [APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation](https://arxiv.org/abs/2601.06574)
- [DeepStruct: Pretraining of Language Models for Structure Prediction](https://aclanthology.org/2022.findings-acl.67/)
- [Event co-occurrences for prompt-based generative event argument extraction](https://www.nature.com/articles/s41598-024-82883-w)
- [Structured information extraction from scientific text with LLMs](https://www.nature.com/articles/s41467-024-45563-x)
- [An LLM + ASP Workflow for Joint Entity-Relation Extraction](https://arxiv.org/abs/2508.12611)
- [RLVR: Verifiable Rewards for Reliable Enterprise LLMs](https://www.appen.com/blog/rlvr)
- [The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards](https://arxiv.org/html/2602.14872)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ca07f0d-0090-4d50-8286-c3968e0ea772",
  "isSidechain": false,
  "promptId": "d917b6f7-9f45-46d8-a588-62c8ab0f7bb8",
  "type": "user",
  "uuid": "28d66e77-fd8b-4e68-9b56-c3d0a77827c8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to independently verify the current state-of-the-art for information extraction benchmarks and find recent relevant work. This is for adversarial peer review of a research paper on GRPO-based joint IE. Use WebSearch and WebFetch tools.\n\n**Search tasks:**\n\n1. Find current SOTA on ACE2005 event extraction (trigger and argument F1). What are the best published numbers as of early 2026? Search \"ACE2005 event extraction state of the art 2026\" and \"ACE2005 argument extraction best results\".\n\n2. Find current SOTA on ACE2005 NER and relation extraction. \n\n3. Search Papers With Code for ACE2005 event extraction leaderboard: try fetching https://paperswithcode.com/sota/event-extraction-on-ace-2005\n\n4. Search for any papers combining span-boundary detection with RLVR/GRPO training. Try \"span boundary reinforcement learning NER\" and \"span detection GRPO training\".\n\n5. Search for recent (2025-2026) papers on joint IE with large language models: \"joint information extraction LLM 2026\" and \"unified IE GRPO 2025 2026\".\n\n6. Search for RAMS benchmark evaluation: what recent methods have evaluated on RAMS? Are there strong baselines?\n\n7. Search for \"R2GRPO scientific information extraction\" to verify this paper exists.\n\n8. Check if EXTRACT-0 (arXiv:2509.22906) is a real paper.\n\n9. Search for \"dynamic reward weighting GRPO\" 2025-2026 to find any competitors to the adaptive weighting claim.\n\n10. Search for \"APEX multi-objective alignment\" arXiv:2601.06574 to verify this paper.\n\nReport all findings with paper titles, venues, and key numbers. Flag any papers that seem to be strong competitors to the proposed CurriculumRLVR-IE idea.",
    "agentId": "a1250a6cd7ee333a6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me compile a comprehensive final report based on all the research I've conducted:\n\n## COMPREHENSIVE STATE-OF-THE-ART VERIFICATION REPORT\n\nBased on systematic searching across multiple sources, here are my findings for your adversarial peer review of the GRPO-based joint IE paper:\n\n---\n\n### 1. **ACE2005 EVENT EXTRACTION BENCHMARKS**\n\n**Current SOTA Rankings (Early 2026):**\n- Event Extraction SOTA: **DeepStruct multi-task** (ACL 2022)\n- Event Argument Extraction SOTA: **NLI+** \n- These are listed as top models on Papers with Code leaderboard\n\n**Recent High-Performance Models (2024-2025):**\n- MTCM (Multiple Template Choice Model) - achieves SOTA on ACE2005-EN\n- ECPEAE (Event Co-occurrences Prefix Event Argument Extraction) - shows >10% improvements in low-resource settings\n- Joint models using dynamic attention matching and graph attention networks\n\n**Key Benchmark Metrics Found:**\n- One recent model achieved: 73.3% trigger identification F1, 72.6% trigger classification F1, 55.7% argument identification F1, 54.7% argument classification F1\n- Seq2EG reports improvements of 3.4% F1 for event detection and 4.7% F1 for argument classification over baselines on ACE2005\n\n⚠️ **Note:** Specific numeric scores for DeepStruct and NLI+ were not directly accessible in search results, but these remain the cited SOTA models.\n\n---\n\n### 2. **ACE2005 NER AND RELATION EXTRACTION SOTA**\n\n**NER Performance:**\n- SOTA F1 score: **89.04%** on ACE2005\n- Zhong and Chen (2020) achieved F1 of 90.9 on ACE2005-Ent\n\n**Relation Extraction Performance:**\n- REKnow method: **68.3 F1** on ACE2005\n- Marker collaborating models achieve SOTA on ACE2005\n\n**Papers with Code Leaderboards:**\n- [ACE2005 Benchmark (NER)](https://paperswithcode.com/sota/named-entity-recognition-on-ace-2005)\n- [ACE2005 Benchmark (Relation Extraction)](https://paperswithcode.com/sota/relation-extraction-on-ace-2005)\n\n---\n\n### 3. **PAPERS WITH CODE LEADERBOARDS**\n\nPapers with Code shows benchmarks redirecting through Hugging Face for:\n- Event Extraction on ACE2005\n- Event Argument Extraction on ACE2005\n- NER on ACE2005\n- Relation Extraction on ACE2005\n\nThe leaderboards confirm DeepStruct multi-task and NLI+ as current leaders.\n\n---\n\n### 4. **SPAN-BOUNDARY DETECTION WITH RL/GRPO**\n\n**Key Papers Found:**\n\na) **SKD-NER (ACL EMNLP 2023)** - Continual NER via Span-based Knowledge Distillation with Reinforcement Learning\n   - Uses span-based approach with RL strategies\n   - Addresses catastrophic forgetting in continual learning\n\nb) **GPRL (Gaussian Prior Reinforcement Learning)**\n   - Formulates nested NER as entity triplet sequence generation\n   - Uses Gaussian Prior Adjustment (GPA) for boundary recognition\n   - Incorporates Entity Order Reinforcement Learning (EORL)\n\nc) **BGNER (Boundary Guidance Framework, 2025)**\n   - Recent boundary-enhanced NER framework\n\nd) **T2-NER (Two-Stage Span-Based Framework)**\n   - Unified NER with templates\n\n⚠️ **Competitor Alert:** These papers show that span-based RL approaches for NER are already established, particularly SKD-NER combining knowledge distillation with RL.\n\n---\n\n### 5. **JOINT IE WITH LLMs (2025-2026)**\n\n**Recent Papers:**\n\na) **Reamend** - Novel LLM augmented joint learning framework for entity-relation extraction\n   - Simultaneously recognizes entities and relations\n   - Eliminates redundant triplets\n   - Published 2025\n\nb) **LLM + ASP Workflow for Joint Entity-Relation Extraction** (2508.12611)\n   - Shows 10% training data needed for comparable performance to SOTA JERE systems\n\nc) **AEVS Framework** - Grounds extraction elements to source text to address hallucination\n   - Addresses the critical hallucination problem in LLM-based IE\n\nd) **Multi-Document Event Extraction (EMNLP 2025)**\n   - Recent work on document-level event extraction\n\ne) **SciEx Framework** - Prompt-driven and RAG-based scientific IE\n   - Transforms unstructured research PDFs into structured knowledge\n\n⚠️ **Competitor Alert:** LLM-based joint IE is an active area with multiple recent approaches, particularly addressing hallucination control.\n\n---\n\n### 6. **RAMS BENCHMARK EVALUATION**\n\n**Dataset Specs:**\n- 3,993 documents from news articles\n- 139 event types, 65 role types\n- Derived from real-world news\n\n**Recent SOTA Methods (2025-2026):**\n\na) **DPFS (Dual-Paradigm Fusion Strategy)** - Integrates classification-based and generative approaches\n   - 3.0% improvement over second-best baseline on Argument Classification\n\nb) **SALE (Structure-Aware Large Language Models)** - Two-stage training paradigm\n   - Structure-aware fine-tuning + event extraction alignment\n\nc) **SPARE (Semantic-aware Prompt-based Argument Extractor)**\n   - Uses document-sentence-entity heterogeneous graph with GCNs\n   - Position-aware semantic role attention\n\n**Challenge:** F1 scores drop significantly with increasing distance between triggers and arguments.\n\n---\n\n### 7. **R2GRPO SCIENTIFIC IE VERIFICATION**\n\n⚠️ **FINDING: R2GRPO NOT FOUND** - Search for \"R2GRPO scientific information extraction\" returned no results. This appears to NOT be a published paper or widely-known framework as of early 2026.\n\n**Related Papers on Scientific IE Found:**\n- Structured information extraction from scientific text with LLMs (Nature Commun. 2024)\n- SciEx Framework for scientific IE\n- Grounded Knowledge Graph Extraction via LLMs with Anchor-Constrained Framework\n\n---\n\n### 8. **EXTRACT-0 (arXiv:2509.22906) VERIFICATION**\n\n✓ **VERIFIED - REAL PAPER**\n\n**Key Details:**\n- **Title:** Extract-0: A Specialized Language Model for Document Information Extraction\n- **Author:** Henrique Godoy\n- **Published:** September 26, 2025\n- **Model Size:** 7 billion parameters\n- **Venue:** arXiv preprint\n\n**Methodology:**\n- Synthetic data generation: 280,128 training examples\n- Supervised fine-tuning with LoRA (0.53% weight modification)\n- **Reinforcement Learning via GRPO**\n- Novel semantic similarity-based reward function\n\n**Performance:**\n- Mean reward: **0.573** on 1,000 diverse document extraction tasks\n- Outperforms GPT-4.1 (0.457), o3 (0.464), GPT-4.1-2025 (0.459)\n\n**Reward Function Design:**\n- MiniLM-L6-v2 embedding similarity for text fields\n- Relative difference for numbers\n- Temporal distance for dates\n- Bipartite matching for lists\n\n**Code/Dataset Available:**\n- GitHub: [herniqeu/extract0](https://github.com/herniqeu/extract0)\n- HuggingFace Dataset: [HenriqueGodoy/extract-0](https://huggingface.co/datasets/HenriqueGodoy/extract-0)\n\n⚠️ **Competitor Alert: CRITICAL** - Extract-0 directly applies GRPO to information extraction with a semantic similarity-based reward function. This is highly relevant to your work and represents a strong baseline using GRPO for IE.\n\n---\n\n### 9. **DYNAMIC REWARD WEIGHTING & ADAPTIVE WEIGHTING COMPETITORS**\n\n**Three Major Competitors Found:**\n\n#### a) **Dynamic Reward Weighting (arXiv:2509.11452)**\n- **Title:** Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting\n- **Authors:** Yining Lu et al.\n- **Submitted:** September 14, 2025\n- **Venue:** TACL'26\n- **Status:** Published as conference paper\n\n**Key Innovation:**\n- Proposes dynamic reward weighting that adaptively adjusts weights during online RL\n- Addresses limitations of fixed-weight linear scalarization\n- Two approaches: hypervolume-guided weight adaptation and gradient-based weight optimization\n- Outperforms fixed-weight baselines on Pareto optimal solutions\n\n⚠️ **Direct Competitor Alert:** This paper directly addresses adaptive weighting for multi-objective RL, which is a key claim in your CurriculumRLVR-IE work.\n\n#### b) **MAESTRO (arXiv:2601.07208)**\n- **Title:** MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization\n- **Submitted:** January 2026\n- **Key Feature:** Dynamically adapts reward weights according to prompt-response semantics\n- **Difference:** Prompt-dependent (not fixed) reward weights\n\n#### c) **SPARD (arXiv:2604.07837)**\n- **Title:** SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility\n- **Authors:** 13 authors including Xuyang Zhi, Xiaohongshu Inc.\n- **Submitted:** April 9, 2026\n- **Status:** Very recent work\n\n**Key Innovation:**\n- Self-paced curriculum by perceiving learning progress\n- Dynamically adjusts multi-objective reward weights\n- Integrates Reward Dynamics with Data utility\n- Shows improvements across multiple benchmarks\n\n⚠️ **Direct Competitor Alert: CRITICAL** - SPARD combines curriculum learning with dynamic reward weighting for RLVR. This directly overlaps with claimed contributions of CurriculumRLVR-IE.\n\n---\n\n### 10. **APEX MULTI-OBJECTIVE ALIGNMENT (arXiv:2601.06574) VERIFICATION**\n\n✓ **VERIFIED - REAL PAPER**\n\n**Key Details:**\n- **Title:** APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation\n- **Published:** January 10, 2026\n- **Authors:** Dongliang Chen et al. (11 authors)\n\n**Problem Addressed:**\n- Fixed weights in multi-objective optimization fail under heterogeneous rewards\n- Two mechanistic causes identified:\n  1. **Variance hijacking** - reward dispersion causes implicit reweighting\n  2. **Gradient conflicts** - competing objectives produce opposing updates\n\n**Solution:**\n- Dual-Stage Adaptive Normalization\n- P³ Adaptive Priorities combining:\n  - Learning potential\n  - Conflict penalty\n  - Other factors\n\n**Results (Stable Diffusion 3.5):**\n- +1.31 PickScore\n- +0.35 DeQA\n- +0.53 Aesthetics\n- Maintains competitive OCR accuracy\n\n⚠️ **Note:** APEX focuses on vision-language generation, not information extraction, but the adaptive weighting methodology is highly relevant.\n\n---\n\n### 11. **CURRICULUM REINFORCEMENT LEARNING FOR RLVR**\n\n**Key Papers:**\n\n#### a) **VCRL (arXiv:2509.19803)**\n- **Title:** VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models\n- **Submitted:** September 24, 2025\n- **Key Innovation:** Uses variance of rollout group rewards to determine sample difficulty\n- **Results:** 4.67 point average improvement over GSPO baseline on Qwen3-8B-Base\n\n**Mechanism:**\n- Variance-based Dynamic Sampling\n- Replay Learning with Memory Bank\n- Targets moderate-difficulty samples (higher variance)\n\n#### b) **Implicit Curriculum (arXiv:2602.14872)**\n- **Title:** The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards\n- **Key Finding:** Mixed-difficulty training naturally creates implicit curriculum without explicit scheduling\n\n#### c) **E2H Reasoner (arXiv:2506.06632)**\n- **Title:** Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning\n- **Inspiration:** Curriculum learning for RLVR\n- **Approach:** Schedule tasks from easy to hard\n\n⚠️ **Competitor Alert: CRITICAL** - VCRL applies curriculum learning specifically to RLVR with variance-based difficulty estimation. This is very close to your CurriculumRLVR-IE concept but applied to mathematical reasoning.\n\n---\n\n### 12. **GRPO FOR INFORMATION EXTRACTION**\n\n**General GRPO Applications Found:**\n- Training-Free Group Relative Policy Optimization (2510.08191)\n- GRPO for visual information extraction (over 83% on simple, 95.8% on complex questions)\n- Retrieval-GRPO - multi-objective framework for dense retrieval\n- Code quality improvement with GRPO\n\n**GRPO Overview (2025):**\n- Eliminates value model from PPO\n- Group-sampling-based baseline estimation\n- Significantly reduces computational overhead\n- Standard technique for reasoning and structured output tasks\n\n⚠️ **Key Finding:** No specific papers on GRPO applied to joint information extraction (NER+RE+EE) were found, suggesting this is a novel application area.\n\n---\n\n### 13. **OTHER RECENT SPAN DETECTION & EVENT EXTRACTION WORK**\n\n**Hallucination Span Detection with GRPO:**\n- Models trained with span-F1 metric rewards\n- Issue discovered: reward hacking (defaulting to no hallucinations)\n- Solution: class-aware policy optimization with scaling factors\n\n**Recent Event Extraction Generative Approaches (2024-2025):**\n\na) **GEMS** - Generation-based Event Argument Extraction\n   - Permutes event elements for multiple prompts\n   - Encodes with concatenated context and ontology\n   - Captures diverse structural interactions\n\nb) **KC-GEE** - Knowledge-based Conditioning for Generative Event Extraction\n   - Uses knowledge to condition generation\n\nc) **Diffusion Model Approaches** - Context-aware prompt for generation-based EAE\n\n---\n\n### SUMMARY OF COMPETITIVE THREATS\n\n**Direct Competitors to CurriculumRLVR-IE:**\n\n1. **SPARD (arXiv:2604.07837)** ⚠️ HIGHEST RISK\n   - Self-paced curriculum + dynamic reward weighting for RLVR\n   - General framework across benchmarks\n   - April 2026 (very recent)\n\n2. **VCRL (arXiv:2509.19803)** ⚠️ HIGH RISK\n   - Variance-based curriculum for RLVR\n   - September 2025\n   - Applied to math reasoning but methodology is general\n\n3. **Dynamic Reward Weighting (arXiv:2509.11452)** ⚠️ MEDIUM-HIGH RISK\n   - Adaptive multi-objective reward weighting\n   - TACL'26 acceptance\n   - September 2025\n\n4. **Extract-0 (arXiv:2509.22906)** ⚠️ MEDIUM RISK\n   - GRPO applied to document IE\n   - Semantic similarity-based reward function\n   - September 2025\n\n5. **MAESTRO (arXiv:2601.07208)** ⚠️ MEDIUM RISK\n   - Adaptive reward weighting conditioned on semantics\n   - January 2026\n\n---\n\n### NOVELTY ASSESSMENT\n\n**Potentially Novel About Your Work (if addressing these gaps):**\n- Combination of curriculum learning + RLVR + adaptive weighting specifically for **joint IE** (NER+RE+EE)\n- Span-boundary specific curriculum strategies\n- Specific benchmark results on ACE2005, RAMS, and scientific IE datasets\n\n**Already Covered by Existing Work:**\n- Curriculum learning for RLVR ✓ (VCRL, E2H, Implicit Curriculum)\n- Dynamic/adaptive reward weighting ✓ (arXiv:2509.11452, MAESTRO, SPARD)\n- GRPO for structured extraction ✓ (Extract-0, hallucination detection, visual IE)\n- RL for NER/event extraction ✓ (SKD-NER, GPRL, etc.)\n\n---\n\n### KEY RECOMMENDATIONS FOR YOUR REVIEW\n\n1. **Demand specific comparisons** with SPARD and VCRL on IE tasks\n2. **Request results on standard benchmarks** (ACE2005 trigger/argument F1, RAMS, scientific IE)\n3. **Challenge the novelty claims** about adaptive weighting and curriculum learning\n4. **Verify the reward function design** is actually superior to semantic similarity-based rewards (Extract-0)\n5. **Check if span-boundary detection improvements** are significant vs. existing boundary-aware approaches\n6. **Evaluate against recent prompt/template-based baselines** (MTCM, ECPEAE, GEMS)\n\nSources:\n- [Papers with Code - ACE2005 Event Extraction](https://paperswithcode.com/sota/event-extraction-on-ace-2005)\n- [Papers with Code - ACE2005 Event Argument Extraction](https://paperswithcode.com/sota/event-argument-extraction-on-ace-2005)\n- [MAVEN: A Massive General Domain Event Detection Dataset](https://arxiv.org/pdf/2004.13590)\n- [Prompt for extraction: Multiple templates choice model](https://www.sciencedirect.com/science/article/pii/S0950705124001795)\n- [Joint event extraction model with dynamic attention](https://www.nature.com/articles/s41598-025-91501-2)\n- [SKD-NER: Continual Named Entity Recognition via Span-based Knowledge Distillation with Reinforcement Learning](https://aclanthology.org/2023.emnlp-main.413/)\n- [Gaussian Prior Reinforcement Learning for Nested NER](https://arxiv.org/abs/2305.07266)\n- [Large language model augmented joint learning for entity-relation extraction](https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073)\n- [Closed-Domain Event Extraction Literature Review January 2025](https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf)\n- [Extract-0: A Specialized Language Model for Document Information Extraction](https://arxiv.org/abs/2509.22906)\n- [VCRL: Variance-based Curriculum Reinforcement Learning for LLMs](https://arxiv.org/abs/2509.19803)\n- [Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting](https://arxiv.org/abs/2509.11452)\n- [SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility](https://arxiv.org/abs/2604.07837)\n- [APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation](https://arxiv.org/abs/2601.06574)\n- [DeepStruct: Pretraining of Language Models for Structure Prediction](https://aclanthology.org/2022.findings-acl.67/)\n- [Event co-occurrences for prompt-based generative event argument extraction](https://www.nature.com/articles/s41598-024-82883-w)\n- [Structured information extraction from scientific text with LLMs](https://www.nature.com/articles/s41467-024-45563-x)\n- [An LLM + ASP Workflow for Joint Entity-Relation Extraction](https://arxiv.org/abs/2508.12611)\n- [RLVR: Verifiable Rewards for Reliable Enterprise LLMs](https://www.appen.com/blog/rlvr)\n- [The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards](https://arxiv.org/html/2602.14872)"
      }
    ],
    "totalDurationMs": 158225,
    "totalTokens": 58846,
    "totalToolUseCount": 41,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4595,
      "cache_read_input_tokens": 49237,
      "output_tokens": 5007,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5007,
          "cache_read_input_tokens": 49237,
          "cache_creation_input_tokens": 4595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4595,
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
      "otherToolCount": 41
    }
  },
  "sourceToolAssistantUUID": "0ca07f0d-0090-4d50-8286-c3968e0ea772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
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
  "leafUuid": "28d66e77-fd8b-4e68-9b56-c3d0a77827c8",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled GRPO for joint NER+RE+EE with adaptive weights",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Assistant

_source line 18 · 2026-05-10T08:12:41.387Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have comprehensive research findings. Let me analyze what I found:

**Key papers - all verified:**
- ProUIE (arXiv:2604.10633) ✓ - Joint NER+RE+EE with GRPO+SFR
- GDPO (arXiv:2601.05242) ✓ - ICML 2026 confirmed
- arXiv:2602.14872 ✓ - "On the Learning Dynamics of RLVR at the Edge of Competence"


- arXiv:2604.19857 ✓ - Reward Decomposition Theorem
- RuCL (arXiv:2602.21628) ✓
- EXTRACT-0 (arXiv:2509.22906) ✓
- APEX (arXiv:2601.06574) ✓

I'm also finding some critical new work here - SPARD from April 2026 looks particularly interesting as it's combining self-paced curriculum learning with dynamic reward mechanisms for RL alignment.  That's directly overlapping with the adaptive weighting and curriculum components of the proposed approach, and it wasn't cited. VCRL uses variance of rollout rewards to assess sample difficulty, which connects to the curriculum induction claims. MAESTRO does adaptive reward weighting based on prompt-response semantics from January 2026, also not cited. There's an inconsistency I'm noting about R2GRPO - one source says it exists as "Beyond Path Selection" but another says it wasn't found.

Looking at what Round 5 actually addressed from the previous feedback, I can see GDPO is now cited and positioned as orthogonal to the normalization approach, the relay regime framework and Reward Decomposition Theorem papers are both included, the θ sensitivity analysis with checkpoint values and plateau detection is there, and the submission correctly targets EMNLP 2026 Findings. But there's a critical gap: SPARD from April 2026 combines self-paced curriculum with dynamic reward weighting for RLVR and isn't cited anywhere.

SPARD's approach to dynamically adjusting multi-objective reward weights and integrating reward dynamics with data utility directly overlaps with Contribution 2's adaptive weighting mechanism and the curriculum induction claims, which a reviewer would almost certainly catch as concurrent work. There's also VCRL from September 2025 on variance-based curriculum RL that uses rollout group reward variance to determine sample difficulty and shows strong improvements over GSPO, which relates to the variance-based curriculum framing here.

That said, SPARD operates on general RLVR without the span-boundary decomposition specific to information extraction, so the novelty of CurriculumRLVR-IE isn't entirely threatened, but the omission still needs addressing.

The real differentiator is the structural decomposition of IE rewards into span, type, and argument components with the theoretical gradient variance analysis tailored to IE-specific reward structures. SPARD's self-paced curriculum is fundamentally about data difficulty scheduling rather than reward component decomposition, and VCRL estimates difficulty at the sample level without decomposing within reward components. However, the adaptive weighting formula itself—using the ratio of margin to variance—bears enough conceptual similarity to SPARD's dynamic weighting that I need to be more explicit about what makes the IE-specific application distinct.

For the resource estimate, the 130-165 H100-hours for an 8B model with LoRA on ACE2005 seems plausible given the small parameter footprint and dataset size, though the corrected output budget of 300-600 tokens per example across multiple epochs tightens the calculation considerably.

Let me work through the math more carefully: with GRPO requiring 8-16 rollouts per prompt and those token outputs, the generation pass alone across 4-8 epochs could demand 200-800 H100-hours on 4 GPUs, before accounting for backward passes. But LoRA's efficiency during backprop should help offset some of that cost, and the batch throughput at 8B scale is more favorable than my initial estimate suggested. , 8 rollouts per prompt
- 25K examples: 25K × 8 × 450 tokens avg = 90M tokens total generation for one epoch
- At 2000 tokens/s with 4×H100 = 8000 tokens/s: 90M / 8000 / 3600 ≈ 3.1 H100-hours per epoch total

For 20 epochs: ~62 H100-hours for generation
Add backward passes: maybe 2× = ~124 H100-hours total

So the 130-165 H100-hours estimate is actually plausible for the main run. This is within the constraint.

Actually, I need to reconsider. GRPO training is typically more expensive than pure SFT because of the group rollout generation. Let me think more carefully:

The Light-R1 paper reported 3,328-5,376 A100-GPU-hours for a single GRPO run on a 14B model, which is much larger and trained on more data. With an 8B model using LoRA, I have some advantages—LoRA reduces memory and allows bigger batches, the model is half the size, and ACE2005 is relatively small. The 300-600 token length is longer than typical math problems though, which could push costs up. So 130-165 H100-hours feels optimistic but not unreasonable, especially since the proposal emphasizes a single primary run with most ablations coming from checkpoint evaluation rather than separate full training runs. That's a smart way to stay within budget constraints.

Now looking at the Round 5 assessment, the submission has fixed all the Round 4 issues—GDPO is cited and distinguished, the recent papers are referenced, and the θ sensitivity with plateau detection is included. But there are still two uncited papers that directly overlap: SPARD handles curriculum plus adaptive weighting, and VCRL covers variance-based curriculum learning. The novelty is getting squeezed—after five rounds of revision, the core contributions are the gradient variance analysis for IE reward decomposition, the adaptive weighting scheme, and the per-component learning curves, but that adaptive weighting piece is now under threat from these existing methods.

The key distinction is that SPARD applies data-level curriculum while this work focuses on reward-component-level curriculum, and the IE-specific span-boundary decomposition remains the novel core. The contribution scope is still narrow for EMNLP Main, so targeting the Findings track is the right call. On novelty, I'm scoring this 3/5—the span-boundary-decoupled GRPO for IE is valid and not directly covered elsewhere, but SPARD and VCRL do diminish the distinctiveness of the adaptive weighting framing, the weighting formula itself is relatively straightforward, and while the gradient variance analysis is a theoretical contribution, it's built on existing foundations.

The feasibility looks solid at 4/5—running 8B with LoRA on ACE2005 is definitely doable, the 130-165 H100-hours estimate is plausible if optimistic, all datasets are available, and while 16 days to the ARR deadline is tight for manual submission, human-in-loop or automated modes make it more realistic.

On clarity, I'm rating this 4/5 because the proposal is now quite detailed and well-specified—the connections to prior work are clear, the adaptive weighting formula is precisely defined, and the three contributions stand out distinctly. For impact though, I'm settling on 3/5: EMNLP Findings is the right venue for this kind of incremental work, and there's definitely a real gap to address with ProUIE's 52.58% versus InstructUIE's 72.94% on ACE2005, but the core solution of decomposed rewards is conceptually straightforward, and it's unclear how much this generalizes beyond joint IE tasks.

That puts me at 3.5/5 overall, which falls short of the 4.0 threshold needed to pass. The verdict is to revise. The main issues are missing citations—SPARD and VCRL are directly relevant concurrent work that overlap with the curriculum and adaptive weighting contributions—and I need to sharpen the differentiation between this approach and SPARD's self-paced curriculum. These are fixable problems though. After four rounds of revision, the core idea is solid, so it's really about addressing the citation gaps and clarifying what makes the adaptive weighting distinct from SPARD's approach.

The key differentiation is that SPARD and VCRL operate at the sample level—deciding which examples to train on harder—while this work decomposes the reward signal within each example across span boundaries, types, and arguments, creating an internal curriculum. That's a meaningful and valid distinction. Given the May 25 deadline for EMNLP 2026 Findings via ARR, and the fact that auto-research mode takes 5-8 days, the timeline is tight but theoretically feasible. auto and HIL modes)
- Fallback: ACL 2027 via February 2027 ARR (manual mode)

But the auto-research mode timeline is "5-8 days with 4× H100 cluster" - so theoretically feasible for the May 25 deadline. However, writing a paper in 5-8 days is extremely aggressive even for auto research.

**Final verdict: REVISE**

Issues:
1. SPARD (arXiv:2604.07837, April 2026) not cited - directly combines self-paced curriculum + dynamic reward weighting for RLVR, needs explicit differentiation
2. VCRL (arXiv:2509.19803) not cited - variance-based curriculum for RLVR that overlaps with the variance-framing of the gradient analysis

These are fixable but important. The idea remains sound at its core. The span-boundary-decoupled reward is genuinely novel among IE methods, and the adaptive weighting can be clearly distinguished from SPARD since it operates at the reward-component level rather than the data level. After five rounds of revision, all previous feedback has been addressed, though the average scores—novelty 3, feasibility 4, clarity 4, impact 3—still fall short of the 4.0 threshold needed for acceptance. I'd need to see stronger novelty and impact ratings to move this to a pass, as it currently reads more like a collection of incremental improvements rather than a cohesive breakthrough. ProUIE's weakness:
1. Span-boundary decoupled reward (novel for IE GRPO)
2. Adaptive weight scheme (multiple concurrent papers doing similar things)
3. Gradient variance analysis (theoretical extension of existing frameworks)

The span-boundary decoupling is genuinely novel and the most compelling contribution. The adaptive weighting is less novel given SPARD, VCRL, arXiv:2509.11452. The gradient variance analysis is a theoretical contribution but not a strong standalone theory paper.

For EMNLP Findings, this is probably borderline acceptable. For Main, it's clearly insufficient. The paper correctly targets Findings now.

**Revised scoring:**
- Novelty: 3 (span-decoupling is novel but adaptive weighting is crowded; multiple concurrent papers)
- Feasibility: 4 (single-run design within constraints, datasets available)
- Clarity: 4 (well-specified, relationships to other work clearly articulated)
- Impact: 3 (moderate impact, EMNLP Findings-level contribution)

Average: 3.5 → REVISE. The paper needs to address the novelty crowding around adaptive weighting and strengthen the theoretical contributions before resubmission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28d66e77-fd8b-4e68-9b56-c3d0a77827c8",
  "isSidechain": false,
  "requestId": "req_011CatYt38ji1jbGLmxSPAV3",
  "type": "assistant",
  "uuid": "91595a72-67e9-4096-afc6-d3cb45abcbac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UCpvvEu8dPh5vwhdTz59P7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10314,
      "cache_read_input_tokens": 35999,
      "output_tokens": 4483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4483,
          "cache_read_input_tokens": 35999,
          "cache_creation_input_tokens": 10314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10314
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

_source line 19 · 2026-05-10T08:12:45.949Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JcLYfHsZauVx4jHK76tjbp`</summary>

```json
{
  "description": "Verify SPARD paper and assess overlap with CurriculumRLVR-IE",
  "subagent_type": "Explore",
  "prompt": "Please fetch and read the abstract and key sections of this paper:\n\n1. SPARD (arXiv:2604.07837) - \"Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility\" - April 2026\n\nFetch: https://arxiv.org/abs/2604.07837\n\nKey questions to answer:\n- Does this paper combine self-paced curriculum learning with dynamic reward weighting for RLVR?\n- Does it dynamically adjust multi-objective reward component weights based on training progress?\n- Is it applied to structured tasks like information extraction, or general RLVR?\n- What is the specific mechanism for weight adaptation?\n\nAlso search for:\n- \"SPARD self-paced curriculum reward dynamics\" 2026\n- \"arXiv 2604.07837 RLVR\"\n\nCompare its approach to: \"CurriculumRLVR-IE uses adaptive weight w_i(t) = max(ε, θ − F1_i(t)) / σ_i(t) that assigns higher weight to reward components (span, type, argument) lagging convergence with lower variance\"\n\nReport exactly what SPARD does and whether it directly overlaps with the adaptive weighting + curriculum learning claims of the proposed CurriculumRLVR-IE paper. Also assess whether the differentiation \"SPARD operates at data-sample level while CurriculumRLVR-IE operates at reward-component level within each sample\" is a valid and clear distinction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91595a72-67e9-4096-afc6-d3cb45abcbac",
  "isSidechain": false,
  "requestId": "req_011CatYt38ji1jbGLmxSPAV3",
  "type": "assistant",
  "uuid": "09af1c65-eef4-4445-a061-3e72493c5dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UCpvvEu8dPh5vwhdTz59P7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10314,
      "cache_read_input_tokens": 35999,
      "output_tokens": 4483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4483,
          "cache_read_input_tokens": 35999,
          "cache_creation_input_tokens": 10314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10314
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "09af1c65-eef4-4445-a061-3e72493c5dbb",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled GRPO for joint NER+RE+EE with adaptive weights",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Tool result

_source line 22 · 2026-05-10T08:13:14.236Z_

<details><summary>↩ Tool result · `toolu_01JcLYfHsZauVx4jHK76tjbp`</summary>

```text
Based on my research, here is the detailed comparison and analysis:

## SPARD's Approach (arXiv:2604.07837)

**Does combine self-paced curriculum learning with dynamic reward weighting:** YES. SPARD explicitly integrates Progress-Aware Weight Adaptation (PAWA) for dynamic reward adjustment with curriculum learning principles.

**Dynamic reward component weight adjustment:** YES. PAWA adjusts multi-objective reward component weights during training based on learning progress using:
- **Formula:** w_{t+1}^{r,i} = w_{t}^{r,i} exp(η·Q_t^i) / Σ_j w_{t}^{r,j} exp(η·Q_t^j)
- **Progress metric:** Q_t^i = (μ_t^i - β·σ_t^i) - (μ_{t-1}^i - β·σ_{t-1}^i) (Lower Confidence Bound principle)
- **Mechanism:** Amplifies focus on fast-improving reward dimensions while maintaining smooth optimization

**Application scope:** General RLVR framework (not task-specific). SPARD is designed for broad LLM post-training across "comprehensive spectrum of model capabilities and application contexts."

**Weight adaptation mechanism specifics:**
1. **PAWA** operates at the **reward-component level**, tracking exponential moving averages of means and standard deviations across N scoring criteria
2. **RADR** (Reward-Attributed Data Rebalancing) operates at the **data-category level**, computing attribution matrices F_ij to assign data importance weights based on how effectively each category provides supervision signals for different reward dimensions

## Comparison to CurriculumRLVR-IE

**Direct overlap:** YES, there is significant overlap in **core concepts**:
- Both use dynamic weight adaptation based on training progress
- Both operate on multi-objective reward systems
- Both adjust weights to address lagging convergence

**Critical differences in **mechanism**:**
- **SPARD/PAWA:** Uses confidence-bound adjusted means with exponential growth regularization: w_{t+1}^{r,i} = w_{t}^{r,i} exp(η·Q_t^i)
- **CurriculumRLVR-IE:** Uses variance-normalized lagging: w_i(t) = max(ε, θ − F1_i(t)) / σ_i(t)

These are fundamentally different adaptation schemes - SPARD's relies on reliable performance gain detection, while CurriculumRLVR-IE's explicitly penalizes lagging metrics and normalizes by their variance.

## Validity of Differentiation Claim

**"SPARD operates at data-sample level while CurriculumRLVR-IE operates at reward-component level"**

This differentiation as stated is **INCORRECT and misleading**:
- SPARD's PAWA actually operates at the **reward-component level** (not data-sample level)
- SPARD's RADR is the data-level mechanism (data-category level, not sample-level)
- The actual distinction is more nuanced: SPARD has a **two-tier approach** (reward weights + data category rebalancing), while CurriculumRLVR-IE appears to be a **single-tier approach** (reward component weights only)

A more accurate differentiation would be: "SPARD integrates both reward-component and data-category reweighting, while CurriculumRLVR-IE focuses on reward-component level weight adaptation without explicit data rebalancing."

Sources:
- [SPARD arXiv abstract](https://arxiv.org/abs/2604.07837)
- [SPARD HTML version](https://arxiv.org/html/2604.07837)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09af1c65-eef4-4445-a061-3e72493c5dbb",
  "isSidechain": false,
  "promptId": "d917b6f7-9f45-46d8-a588-62c8ab0f7bb8",
  "type": "user",
  "uuid": "99b7c7a7-1349-43a5-864f-2715aea3155b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please fetch and read the abstract and key sections of this paper:\n\n1. SPARD (arXiv:2604.07837) - \"Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility\" - April 2026\n\nFetch: https://arxiv.org/abs/2604.07837\n\nKey questions to answer:\n- Does this paper combine self-paced curriculum learning with dynamic reward weighting for RLVR?\n- Does it dynamically adjust multi-objective reward component weights based on training progress?\n- Is it applied to structured tasks like information extraction, or general RLVR?\n- What is the specific mechanism for weight adaptation?\n\nAlso search for:\n- \"SPARD self-paced curriculum reward dynamics\" 2026\n- \"arXiv 2604.07837 RLVR\"\n\nCompare its approach to: \"CurriculumRLVR-IE uses adaptive weight w_i(t) = max(ε, θ − F1_i(t)) / σ_i(t) that assigns higher weight to reward components (span, type, argument) lagging convergence with lower variance\"\n\nReport exactly what SPARD does and whether it directly overlaps with the adaptive weighting + curriculum learning claims of the proposed CurriculumRLVR-IE paper. Also assess whether the differentiation \"SPARD operates at data-sample level while CurriculumRLVR-IE operates at reward-component level within each sample\" is a valid and clear distinction.",
    "agentId": "a40871fc8f1b76ac4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my research, here is the detailed comparison and analysis:\n\n## SPARD's Approach (arXiv:2604.07837)\n\n**Does combine self-paced curriculum learning with dynamic reward weighting:** YES. SPARD explicitly integrates Progress-Aware Weight Adaptation (PAWA) for dynamic reward adjustment with curriculum learning principles.\n\n**Dynamic reward component weight adjustment:** YES. PAWA adjusts multi-objective reward component weights during training based on learning progress using:\n- **Formula:** w_{t+1}^{r,i} = w_{t}^{r,i} exp(η·Q_t^i) / Σ_j w_{t}^{r,j} exp(η·Q_t^j)\n- **Progress metric:** Q_t^i = (μ_t^i - β·σ_t^i) - (μ_{t-1}^i - β·σ_{t-1}^i) (Lower Confidence Bound principle)\n- **Mechanism:** Amplifies focus on fast-improving reward dimensions while maintaining smooth optimization\n\n**Application scope:** General RLVR framework (not task-specific). SPARD is designed for broad LLM post-training across \"comprehensive spectrum of model capabilities and application contexts.\"\n\n**Weight adaptation mechanism specifics:**\n1. **PAWA** operates at the **reward-component level**, tracking exponential moving averages of means and standard deviations across N scoring criteria\n2. **RADR** (Reward-Attributed Data Rebalancing) operates at the **data-category level**, computing attribution matrices F_ij to assign data importance weights based on how effectively each category provides supervision signals for different reward dimensions\n\n## Comparison to CurriculumRLVR-IE\n\n**Direct overlap:** YES, there is significant overlap in **core concepts**:\n- Both use dynamic weight adaptation based on training progress\n- Both operate on multi-objective reward systems\n- Both adjust weights to address lagging convergence\n\n**Critical differences in **mechanism**:**\n- **SPARD/PAWA:** Uses confidence-bound adjusted means with exponential growth regularization: w_{t+1}^{r,i} = w_{t}^{r,i} exp(η·Q_t^i)\n- **CurriculumRLVR-IE:** Uses variance-normalized lagging: w_i(t) = max(ε, θ − F1_i(t)) / σ_i(t)\n\nThese are fundamentally different adaptation schemes - SPARD's relies on reliable performance gain detection, while CurriculumRLVR-IE's explicitly penalizes lagging metrics and normalizes by their variance.\n\n## Validity of Differentiation Claim\n\n**\"SPARD operates at data-sample level while CurriculumRLVR-IE operates at reward-component level\"**\n\nThis differentiation as stated is **INCORRECT and misleading**:\n- SPARD's PAWA actually operates at the **reward-component level** (not data-sample level)\n- SPARD's RADR is the data-level mechanism (data-category level, not sample-level)\n- The actual distinction is more nuanced: SPARD has a **two-tier approach** (reward weights + data category rebalancing), while CurriculumRLVR-IE appears to be a **single-tier approach** (reward component weights only)\n\nA more accurate differentiation would be: \"SPARD integrates both reward-component and data-category reweighting, while CurriculumRLVR-IE focuses on reward-component level weight adaptation without explicit data rebalancing.\"\n\nSources:\n- [SPARD arXiv abstract](https://arxiv.org/abs/2604.07837)\n- [SPARD HTML version](https://arxiv.org/html/2604.07837)"
      }
    ],
    "totalDurationMs": 28282,
    "totalTokens": 21599,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 19127,
      "output_tokens": 891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 891,
          "cache_read_input_tokens": 19127,
          "cache_creation_input_tokens": 1576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1576,
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
  "sourceToolAssistantUUID": "09af1c65-eef4-4445-a061-3e72493c5dbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T08:13:39.853Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! SPARD (arXiv:2604.07837, April 2026) actually:
1. Operates at the reward-component level with PAWA (Progress-Aware Weight Adaptation)
2. Uses dynamic weight adaptation based on training progress
3. Adjusts weights to address lagging convergence

This directly overlaps with CurriculumRLVR-IE's Contribution 2 (adaptive component weights).

The differentiation I thought was valid ("data-sample level vs. reward-component level") is actually INCORRECT - SPARD's PAWA operates at the reward-component level too.


So the real distinctions come down to the specific weighting formulas—SPARD employs an LCB-based exponential growth approach with confidence bounds, whereas CurriculumRLVR-IE uses variance-normalized lagging that directly targets the lagging component. Beyond the technical differences, SPARD is a general framework while CurriculumRLVR-IE is tailored specifically for IE, and only the latter provides the span-boundary decomposition insight and theoretical justification grounded in IE's reward structure. The critical issue is that SPARD isn't cited in the Round 5 submission, which means a reviewer familiar with it would see the adaptive weighting claim as substantially weakened since SPARD already does something similar. I need to revise the differentiation claim from "no prior work uses adaptive weights" to something more precise—that no prior work applies this specific adaptive weighting to IE's span/type/argument decomposition or provides the formal gradient-variance justification for why this decomposition creates a sequential curriculum. This is a significant gap that has to be addressed before Round 5.

Looking at my verified papers, I've now confirmed ProUIE, GDPO, and several others are properly cited and distinguished. But I've identified a critical uncited concurrent work: SPARD directly overlaps with Contribution 2 since PAWA operates at the reward-component level with dynamic weight adaptation based on training progress. The claim that my approach differs at the "data-sample level" is actually incorrect, so I need to cite SPARD and provide an accurate differentiation based on formula differences and IE-specific application instead. The adaptive weighting's novelty is really just a convergence-lagging variant of SPARD's approach, but applied specifically to the IE reward structure with variance normalization instead of confidence bounds and a plateau detector. The theoretical contribution around gradient variance and span-boundary IoU continuity creating a relay effect at the reward-component level is actually the strongest and most original part. The single-run design within 200 H100-hours is reasonable, though the overall novelty scores around 3/5 given how directly SPARD competes with the adaptive weighting component.

Looking at the full assessment, this lands at 3.5 average, which means it needs revision. The core issues are straightforward to fix: properly cite SPARD, clarify that Contribution 2 is a convergence-lagging variant with variance normalization rather than claiming it's the first adaptive weighting for GRPO, and keep the span-boundary IoU decomposition as the main novel contribution. The work is feasible and well-specified enough for EMNLP Findings with these corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b7c7a7-1349-43a5-864f-2715aea3155b",
  "isSidechain": false,
  "requestId": "req_011CatZ1o6cCWdATFFmyN3Ln",
  "type": "assistant",
  "uuid": "84adeb7c-d43f-412a-9b2b-d4789dd24934",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01P22936v76x6C12XMsKys2o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 46313,
      "output_tokens": 3721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3721,
          "cache_read_input_tokens": 46313,
          "cache_creation_input_tokens": 5374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5374
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

_source line 24 · 2026-05-10T08:14:18.353Z_

Now I have sufficient information to render my verdict. Let me compile the final assessment.

**Summary of findings from independent research:**

**Verified papers (all exist):**
- ProUIE ✓, GDPO (ICML 2026) ✓, arXiv:2602.14872 ✓, arXiv:2604.19857 ✓, RuCL ✓, EXTRACT-0 ✓, APEX ✓

**Critical new finding — SPARD (arXiv:2604.07837, April 2026) NOT cited:**
- "Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility"
- SPARD's PAWA (Progress-Aware Weight Adaptation) operates **at the reward-component level**, not data-sample level, using: `w_{t+1}^{r,i} = w_{t}^{r,i} · exp(η·Q_t^i)` where Q is a confidence-bound adjusted progress metric
- This directly overlaps with CurriculumRLVR-IE's Contribution 2 (adaptive weights)
- SPARD also has RADR for data-category rebalancing
- The differentiation the paper might use ("data-level vs. reward-component level") is factually incorrect — SPARD's PAWA IS reward-component level

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The span-boundary IoU reward decoupled from type label is genuinely novel for GRPO-based IE and remains the core contribution. However, Contribution 2 (adaptive component weights) is directly challenged by SPARD (arXiv:2604.07837, April 2026), whose PAWA mechanism operates at the reward-component level and adjusts weights based on training progress — the same concept as the proposed w_i(t) = max(ε, θ−F1_i(t))/σ_i(t). Additionally, VCRL (arXiv:2509.19803) applies variance-based curriculum to RLVR. The gradient variance analysis (Contribution 1) is the strongest distinguishing theoretical element, but it is built atop three existing frameworks (RuCL Appendix B, arXiv:2602.14872, arXiv:2604.19857)."
    },
    "feasibility": {
      "score": 4,
      "rationale": "The single-run-primary design with checkpoint-derived ablations is a credible approach to stay within 200 H100-hours; Qwen3-8B+LoRA on ACE2005 (~25K examples) at 300-600 tokens output is plausible at ~130-165 H100-hours. The plateau detector (F1_i improvement <1% over 200 steps) and θ sensitivity via saved checkpoints add robustness without extra training cost. The May 25 ARR deadline is achievable only for auto-research mode (5-8 days claimed), which is extremely tight for paper writing even with automation."
    },
    "clarity": {
      "score": 4,
      "rationale": "The three contributions are now precisely delineated, the relationship to GDPO/arXiv:2602.14872/arXiv:2604.19857 is carefully articulated, the θ sensitivity and plateau detector add methodological rigor, and the single-run compute design is clearly specified. The SPARD omission is the only major clarity gap that would confuse a reviewer who reads related work carefully."
    },
    "impact": {
      "score": 3,
      "rationale": "ProUIE's documented 20-point Argument F1 gap on ACE2005 is a real and concrete target, and span-boundary-decoupled rewards address it at a principled level. However, the contribution scope — a reward design modification on one joint IE model — is narrow, the adaptive weighting is now shared with SPARD, and the OOD evaluation (sentence-trained → document-level RAMS/WikiEvents) frames a confound as a contribution, limiting the generalization claim."
    }
  },
  "issues": [
    "UNCITED DIRECT COMPETITOR — SPARD (arXiv:2604.07837, April 2026) is not cited and directly threatens Contribution 2's novelty. SPARD's PAWA (Progress-Aware Weight Adaptation) adjusts reward-component weights dynamically based on training progress using a confidence-bound adjusted exponential scheme: w_{t+1}^{r,i} = w_{t}^{r,i}·exp(η·Q_t^i). This operates at the reward-component level — NOT the data-sample level. Any reviewer who knows SPARD will immediately flag its absence. The paper must cite SPARD, accurately distinguish the proposed w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) from SPARD's LCB-based exponential growth formula, and narrow the novelty claim from 'first adaptive reward weighting for GRPO' to 'first adaptive weighting applied to the span/type/argument IE decomposition with formal gradient-variance justification for why the convergence ordering matters.'",
    "INCORRECT DIFFERENTIATION FROM SPARD — The most natural defensive move for the generator ('SPARD is data-level curriculum, ours is reward-component level') is factually wrong: SPARD has BOTH reward-component level weighting (PAWA) AND data-category level rebalancing (RADR). The paper must instead differentiate on: (a) formula design — variance-normalized lagging (proposed) vs. confidence-bound exponential growth (SPARD); (b) IE-specific structural decomposition (span-IoU continuity vs. type conjunction is not present in SPARD); (c) formal gradient-variance justification linking span-IoU continuity to early-training variance reduction, which SPARD does not provide.",
    "UNCITED COMPETITOR (MEDIUM) — VCRL (arXiv:2509.19803, September 2025) uses variance of rollout group rewards to estimate sample difficulty and drive curriculum selection for RLVR on math. Since CurriculumRLVR-IE's theoretical narrative explicitly centers on reward-variance reduction, a reviewer will expect VCRL to be cited and the distinction made clear (VCRL: between-sample variance for difficulty; proposed: within-sample reward-component variance for skill ordering).",
    "CONTRIBUTION 2 NOVELTY WEAKENED — With SPARD (PAWA) covering reward-component adaptive weighting and arXiv:2509.11452 + APEX already cited for motivation, Contribution 2's standalone novelty is now thin. The generator should reframe Contribution 2 as the application and instantiation of adaptive weighting for the specific IE skill hierarchy, not as a novel adaptive weighting technique per se. The genuine novelty is the combination of span-decoupled reward (Contribution 1's design) with convergence-aware weighting derived from the gradient variance analysis, not the weighting formula in isolation.",
    "EMNLP 2026 FINDINGS FEASIBILITY — The May 25 ARR deadline is 15 days away. The auto-research timeline (5-8 days for GPU work) is possible but writing a submission-quality paper in the remaining time after experiments is unrealistic. The generator correctly lists this as 'auto and HIL modes' for EMNLP 2026 and 'manual mode' for ACL 2027, but should be explicit that even for auto mode, producing an EMNLP-quality paper by May 25 requires the full 16 days with no setbacks — the dry-run gate (Day 1-2), main training (Days 3-7), analysis (Days 8-10), and writing (Days 11-15) leave zero margin for iteration."
  ],
  "feedback": "Round 5 has correctly addressed all four Round 4 issues: GDPO is distinguished, arXiv:2602.14872 and arXiv:2604.19857 are positioned, θ sensitivity + plateau detector are specified, and EMNLP Findings (not Main) is the target. The core technical nucleus — span-boundary IoU reward decoupled from type label, inducing a span→type→argument gradient relay in GRPO training — remains the paper's strongest and most defensible claim. However, a new concurrent paper has emerged that must be addressed before submission: (1) Add SPARD (arXiv:2604.07837) to related work — 1 paragraph describing PAWA's exponential confidence-bound weighting at the reward-component level, then distinguishing the proposed scheme by: (a) variance-normalized lagging formula vs. SPARD's LCB exponential growth, (b) IE-specific span/type/argument decomposition not present in SPARD, and (c) the formal gradient-variance analysis linking span-IoU continuity to sequential convergence — a structural argument SPARD does not make. Do NOT use the 'data-level vs. reward-component level' distinction because it is factually wrong. (2) Add VCRL (arXiv:2509.19803) with 1 sentence: between-sample variance for difficulty curriculum vs. within-sample reward-component variance for skill ordering. (3) Reframe Contribution 2's novelty: the contribution is the application of adaptive weighting to the span/type/argument structure with the gradient-variance analysis as motivation, not the adaptive weighting scheme as a standalone novel technique. These are all additive related-work and framing changes — no experimental changes required. The span-boundary decoupling remains genuinely novel for GRPO-based IE.",
  "reason": "SPARD (arXiv:2604.07837, April 2026) directly overlaps with Contribution 2 at the reward-component level and is uncited; this must be addressed before any submission."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84adeb7c-d43f-412a-9b2b-d4789dd24934",
  "isSidechain": false,
  "requestId": "req_011CatZ1o6cCWdATFFmyN3Ln",
  "type": "assistant",
  "uuid": "b6190273-20a2-41dd-87fd-86758efabbc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01P22936v76x6C12XMsKys2o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 46313,
      "output_tokens": 3721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3721,
          "cache_read_input_tokens": 46313,
          "cache_creation_input_tokens": 5374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5374
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b6190273-20a2-41dd-87fd-86758efabbc9",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled GRPO for joint NER+RE+EE with adaptive weights",
  "sessionId": "df7bbab5-7d2b-4484-832d-90837932efdc"
}
```

---
