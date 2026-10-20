# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/cc361057-7cff-41f5-8bad-b54576537f94.jsonl`
- **Structured JSON:** [`5628756e416c97aebe4c.json`](../../sessions/56/5628756e416c97aebe4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:10:38.631Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:10:38.631Z",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Human-Centered NLP and Human-AI Interaction. Aligns with EMNLP 2026 special theme on agentic workflows interfacing with human experiences.\n\nDirection: Methods that improve how humans and NLP systems collaborate. In-scope: interactive learning from human feedback (beyond vanilla RLHF), human-in-the-loop annotation methods, calibrated uncertainty communication to users, adaptive explanation generation, collaborative writing/editing systems, preference elicitation, controllable generation with user intent.\n\nContribution type: METHOD ONLY. Must propose a concrete algorithm or system mechanism — not a user study alone. Method validated via user study or simulation is ideal.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. HCI-style work is often light on compute, heavier on design and evaluation.\n2. Time: ≤16 days. Use existing open models + lightweight adaptation. If user study needed, design a small-scale simulated or crowdsourced protocol.\n3. Eval: task-specific metrics + human evaluation (inter-annotator agreement, preference rates, task completion time). Simulated user evaluation acceptable for ARR submission.\n\nLook for: adaptive interaction patterns, uncertainty-aware response generation, methods for user preference learning with minimal feedback, controllable generation beyond simple instruction following.\n\nTag: direction=human_ai_interaction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"Demonstration-Grounded Warm-Start Hypothesis Elicitation for LLM Personalization via Binary Confirmation\",\n  \"core_problem\": \"Personalizing LLMs to individual users requires efficient preference elicitation from few-shot demonstrations. Current methods exhibit four distinct failure modes: (1) Demonstration-grounded hypothesis methods (HyPerAlign) infer rich preference attributes from user examples but skip validation, risking hallucination and echo-chamber failure; (2) The BOED-for-preference-elicitation line—established by OPEN (arXiv 2403.05534, ACL 2024) and extended by BED-LLM (arXiv 2508.21184, ICLR 2026)—applies principled EIG-based adaptive questioning but initializes without user-specific demonstration-conditioned priors: OPEN uses LM-ranked feature importances as a domain-generic prior (not conditioned on any specific user's outputs); BED-LLM starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations—which is also not informed by available user examples; both waste elicitation turns on hypotheses that available user demonstrations already resolve; (3) Iterative preference inference from writing samples (PROSE, ICML 2025) refines free-form preference descriptions with component-level verification but involves no user interaction and no formal Bayesian posterior—it cannot adaptively resolve ambiguous hypotheses that demonstrations alone are insufficient to distinguish. Additionally, arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs exhibit systematic confirmation bias in hypothesis testing (42% baseline success rate), meaning LLM-generated hypothesis sets may be preferentially confirmable rather than genuinely falsifiable, causing Bayesian posteriors to converge spuriously on echo-chamber preference profiles. (4) A concurrent approach, AdaptFuse (arXiv 2604.03925, April 2026), externalizes a symbolic Bayesian posterior over pre-defined discrete hypotheses using entropy-adaptive fusion with a frozen LLM, but initializes uniformly (no demo-conditioned warm start), uses fixed sequential query rounds without EIG-based active selection, and lacks disconfirmation probes. No existing method—including AdaptFuse—combines user-demonstration-conditioned warm-start Bayesian priors, EIG-based binary confirmation, and explicit disconfirmation-probe auditing in the LLM response-style personalization domain.\",\n  \"opportunity\": \"The BOED-for-preference-elicitation lineage was established by OPEN (arXiv 2403.05534, ACL 2024), which combined EIG-based query selection with LM feature extraction over pairwise item comparisons in content recommendation—but initializes from LM-ranked feature importances (a domain-generic warm start reflecting general knowledge about what features matter for news article preferences, not this user's actual examples). BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets with a Rao-Blackwellized EIG estimator and an LM-generic prior initialization p_f(θ;∅), evaluating on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions, demonstrating that EIG-based sequential Bayesian elicitation substantially outperforms prompt-only baselines. Neither OPEN nor BED-LLM exploits K specific examples of a target user's actual outputs: their initializations duplicate information that demonstrations already encode, wasting early elicitation turns. AMPLe (arXiv 2411.00524, ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation, but also cold-starts from pairwise item comparisons rather than user demonstrations and lacks disconfirmation probes. HyPerAlign (arXiv 2505.00038, May 2025) showed demonstration-grounded hypotheses yield >90% win rates but explicitly omits user validation. PROSE (arXiv 2505.23815, ICML 2025) achieves 33% improvement over CIPHER on writing-style tasks via iterative preference refinement from demonstrations, but operates entirely without user interaction—it cannot distinguish two hypotheses with similar demonstration-level support, and provides no mechanism to surface or mitigate confirmation bias. AdaptFuse (arXiv 2604.03925, April 2026) is a concurrent work in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL. It externalizes a symbolic Bayesian posterior initialized uniformly (b₀,m = 1/M) and combines it with a frozen LLM's multi-sample Dirichlet aggregation via entropy-adaptive fusion; importantly, its entropy-adaptive fusion is a signal-weighting mechanism, not an EIG-based query selection criterion—queries are presented in fixed sequential rounds (T=5) rather than adaptively selected. AdaptFuse's hypothesis set consists of pre-defined linear utility functions over scalar attributes from a training-split lookup table, not free-form LLM-generated stylistic attributes. Evaluated on recommendation (flight, hotel, web shopping), not LLM response-style personalization. FABEL's three-way differentiation from AdaptFuse: (1) user-specific demo-conditioned temperature-scaled warm prior vs. AdaptFuse's uniform cold start—the same warm-start gap that separates FABEL from BED-LLM and OPEN; (2) EIG-based active query selection absent from AdaptFuse's fixed protocol; (3) mandatory disconfirmation probes absent from AdaptFuse. The unaddressed gap is the warm-start interactive regime: when K demonstrations are available, initializing the Bayesian prior from user-specific demonstration-conditioned LLM likelihoods—calibrated via temperature scaling to avoid overconfident prior collapse—should dramatically reduce required elicitation turns compared to both OPEN and BED-LLM (testable claim), while the interactive EIG confirmation phase resolves the residual ambiguity that passive methods like PROSE cannot address (complementary claim). A second gap concerns confirmation bias: an elicitation system that does not deliberately seed disconfirmation probes in the hypothesis pool risks producing preference profiles that reflect what an LLM expects a user to prefer rather than what the user actually prefers—an echo-chamber failure mode that HyPerAlign acknowledges but does not address, and that PROSE's component-verification step partially mitigates without fully resolving. The specific combination absent from all prior work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, PROSE's non-interactive refinement, and AdaptFuse's training-free externalized Bayesian inference with uniform cold-start and fixed sequential queries.\",\n  \"landscape\": \"The preference elicitation and personalization landscape includes nine relevant clusters. (1) Demonstration-grounded, no validation: HyPerAlign (arXiv 2505.00038, ICLR 2025 workshop) generates falsifiable-in-principle preference hypotheses from demonstrations and injects them as system prompts without user confirmation. (2) Iterative preference inference from writing samples, no interaction: PROSE (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) iteratively refines free-form preference descriptions from user writing samples via a generate→compare→update loop, then verifies preference components against held-out demonstrations with component-level scoring; achieves 33% improvement over CIPHER baseline on summarization and email writing tasks across Qwen2.5-7B/72B and GPT-4o variants; no user interaction beyond initial writing samples, no Bayesian posterior over hypotheses, no disconfirmation mechanism—the key differentiator from FABEL is that PROSE cannot adaptively resolve ambiguity beyond what demonstrations already encode and has no principled update when demonstrations are insufficient to distinguish competing hypotheses; must be included as a baseline (directly competitive with FABEL Stage 1) and explicitly differentiated. (3) The BOED-for-preference-elicitation lineage: OPEN (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) established this line by combining EIG-based query selection with LM feature extraction for content recommendation—selects pairwise queries over binary feature vectors (|F|=10, e.g., 'discusses science') using a particle-filter Bayesian update with Bradley-Terry preference model; prior initialization is via LM-ranked feature importances (domain-generic: w_i = 1.2 − 0.12i for rank i), NOT conditioned on any specific user's demonstrations; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism. BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets: samples N=15 hypotheses per turn, selects questions via Rao-Blackwellized EIG estimator (~45–50 LLM calls/step), rejection-sampling Bayesian posterior update; starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations (and notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions (a technical requirement: having a small space of single-token responses ensures p_LLM provides meaningful uncertainty over outcomes for EIG estimation); evaluates on latent preference vector inference via movie-preference multiple-choice queries and the 20-Questions game; no public code. Active Task Disambiguation (arXiv 2502.04485, ICLR 2025) similarly applies Bayesian experimental design for clarifying question selection on under-specified tasks. FABEL extends beyond all three works: (i) user-specific demonstration-conditioned warm start (K=5–10 demos from THIS user, vs. OPEN's domain-generic LM-ranked feature importances and BED-LLM's demo-agnostic LM-generic prior p_f(θ;∅)), (ii) temperature-scaled prior calibration to prevent overconfident prior collapse, (iii) binary yes/no natural-language hypothesis confirmation over free-form response-style attributes (vs. OPEN's pairwise item comparisons and BED-LLM's multiple-choice format—FABEL's binary format reduces cognitive load while remaining viable because hypothesis confirmation questions are naturally binary in ways that preference inference over open hypothesis spaces is not), (iv) mandatory disconfirmation probes in the EIG pool (absent from all prior BOED-for-preference work), (v) application to LLM response-style personalization (format, tone, structure)—a domain shift from BED-LLM's latent preference vector inference. (3b) Comparison-based active preference learning for LLM personalization: AMPLe (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) personalizes LLM outputs to implicit multi-dimensional preferences via pairwise comparison queries, a modified Bayesian posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection. AMPLe is directly adjacent to FABEL in the active Bayesian personalization space but differs in three critical ways: (1) AMPLe cold-starts from pairwise item comparisons rather than initializing from user demonstrations; (2) AMPLe asks 'which response do you prefer?' (item comparison) rather than 'does this stylistic hypothesis apply to you?' (hypothesis confirmation); (3) AMPLe includes no disconfirmation probe mechanism. AMPLe must be cited as an ACL 2025 active Bayesian personalization baseline; its comparison-based query design and FABEL's hypothesis-confirmation design represent complementary elicitation paradigms. MAPLE (arXiv 2412.07207, AAAI 2025, Mahmud, Nakamura, Zilberstein) uses LLM-conditioned preference function distributions with a language-conditioned active query selection mechanism over pairwise trajectory rankings, targeting general alignment tasks including vehicle routing and web navigation; in the same broad active Bayesian preference learning space as FABEL but differs: (1) pairwise trajectory rankings rather than binary yes/no stylistic hypothesis confirmation grounded in user demonstrations; (2) no warm prior from user demonstrations; (3) general RL alignment domain rather than LLM response-style personalization—cited as AAAI 2025 active preference learning context. (3c) Training-free externalized Bayesian hypothesis inference (concurrent): AdaptFuse (arXiv 2604.03925, April 2026, Lin, Li, Xing, Yang, Ge, Yamada, Zhang, Zhang, Tu) externalizes Bayesian inference from the LLM: a symbolic module maintains a Bayesian posterior over a discrete hypothesis set initialized uniformly (b₀,m = 1/M), updated via Bayes' rule with a Luce choice model likelihood; a frozen LLM contributes semantic reasoning via multi-sample Dirichlet aggregation; entropy-adaptive fusion automatically weights the symbolic posterior vs. LLM signal by predictive confidence, shifting reliance toward the symbolic module as evidence accumulates. The hypothesis set consists of pre-defined linear utility functions over scalar attributes drawn from a training-split lookup table—not free-form LLM-generated natural language stylistic attributes. Queries are presented in fixed sequential rounds (T=5); entropy-adaptive fusion is a signal-weighting mechanism, not a query selection criterion—there is no EIG-based active selection. Evaluated on recommendation domains (flight, hotel, web shopping) across Gemma 2 9B, Llama 3 8B, and Qwen 2.5 7B; outperforms prompting baselines and fine-tuned Bayesian Teaching models without any weight updates. FABEL extends AdaptFuse in four ways: (1) user-specific demo-conditioned temperature-scaled warm prior rather than uniform cold-start (b₀,m = 1/M); (2) EIG-based active query selection absent from AdaptFuse's fixed sequential protocol; (3) free-form LLM-generated natural language stylistic hypotheses rather than pre-defined scalar utility functions from a training split; (4) mandatory disconfirmation probes and soft quota preventing silent suppression of falsifying evidence. AdaptFuse must be acknowledged as a concurrent work sharing the 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' framing; its absence would be flagged by area chairs familiar with April 2026 arXiv. (4) Generative open-ended elicitation: GATE (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) uses free-form LLM-generated questions in three domains; its binary yes/no variant reduces cognitive load but underperforms the open-ended variant because binary questions without a Bayesian posterior cannot adaptively narrow the hypothesis space—GATE's binary variant also does not ground questions in user demonstrations. (5) Trajectory-optimized clarification: TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior. (6) Bayesian-RL hybrid: PEBOL (arXiv 2405.00981, RecSys 2024) combines NLI-based preference beliefs with Thompson Sampling in recommendation. (7) Bayesian in-context conditioning from demonstrations (adjacent): Variational In-Context Reward Modeling / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) casts reward modeling as amortized variational inference over a latent preference with a conjugate Beta prior conditioned on in-context preference demonstrations at test time without retraining—conceptually adjacent to FABEL's warm-start initialization from demonstrations but differs in three critical ways: domain (pairwise scalar reward modeling vs. interactive response-style personalization), hypothesis representation (continuous Beta prior on scalar rewards vs. discrete binary preference hypotheses), and interaction mode (passive in-context update vs. active EIG confirmation loop); no disconfirmation probes; acknowledged in related work to pre-empt warm-start novelty challenge. (8) Few-shot preference optimization: FSPO (arXiv 2502.19312, 2025) meta-learns personalization from few-shot preference data; deferred to Phase 2 due to meta-training infrastructure overhead. The specific combination absent from all prior and concurrent work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, PROSE's non-interactive refinement, and AdaptFuse's training-free externalized Bayesian inference with uniform cold-start, fixed sequential queries, and pre-defined utility function hypotheses.\",\n  \"approach\": \"We propose FABEL (Falsification-Aligned Binary Elicitation Loop), a tuning-free framework operating in four stages. The EMNLP 2026 submission is scoped as an MVP: PersonalLLM benchmark, four baselines, one LLM backbone (Qwen2.5-7B-Instruct), one core ablation, and a small crowdsourced human evaluation (n≈20) to strengthen the EMNLP Main case.\\n\\nStage 1—Demonstration-Grounded Hypothesis Generation with Disconfirmation Probes: Given K=5–10 few-shot user output demonstrations, a frontier open-source LLM (Qwen2.5-7B-Instruct) generates N_pos=12–15 falsifiable, binary-verifiable preference hypotheses (e.g., 'User prefers bulleted structure over prose') AND K_neg=4–6 explicit disconfirmation probes—hypotheses deliberately constructed to be easily falsifiable given the demonstrations (e.g., 'User avoids technical terminology' when demonstrations frequently use it). This two-class design, motivated by arXiv 2604.02485's finding that LLMs default to generating confirmable hypotheses, ensures the EIG pool contains falsifying evidence. To elicit genuinely falsifiable probes rather than merely low-confidence confirmatory hypotheses (the LLM default per arXiv 2604.02485), we use a dedicated generation prompt distinct from the confirmatory hypothesis prompt: 'Given these K writing samples, generate K_neg stylistic hypotheses that are plausibly true of some users but are ACTIVELY VIOLATED by the provided samples—attributes the demonstrations explicitly disconfirm. For each probe, cite the specific demonstration evidence that falsifies it. Example: if all samples use numbered lists, generate the probe \\\"User avoids numbered lists\\\" and cite the list usage as falsifying evidence.' The evidence-citing requirement prevents the model from producing vacuously non-committal probes and ensures each H_neg hypothesis is verifiably falsifiable against the provided demonstrations.\\n\\nStage 2—Temperature-Scaled Warm Prior Initialization with Calibration Check: Each hypothesis posterior is initialized as p(h_i = true | demos) ∝ exp(score_i / τ), where score_i is the LLM log-likelihood of the K demonstrations given hypothesis h_i, and τ is a temperature hyperparameter controlling prior sharpness. Raw LLM log-likelihoods are typically overconfident (τ=1); τ is selected on a held-out 50-user PersonalLLM dev split as the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6 (validation threshold). If no τ in the search grid achieves ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent, equivalent to a cold start) and flag this as a calibration failure in diagnostic analysis—indicating that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for the evaluated hypothesis class. τ→∞ recovers a uniform prior (a maximally uninformative cold start, distinct from BED-LLM's LM-generic prior p_f(θ;∅), which reflects the LLM's own unconditional distribution over hypotheses and is neither uniform nor user-specific); τ=1 applies raw likelihoods. This design directly addresses LLM miscalibration: it ensures the warm start concentrates mass on demonstration-consistent hypotheses while avoiding premature posterior collapse onto incorrect hypotheses. The calibration analysis—Stage 2a in the paper—reports Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users, validating the warm-start assumption empirically and providing a lightweight check that does not require additional model training. Empirical hypothesis accuracy is operationalized as follows: for each simulated PersonalLLM dev user u (a weighted ensemble of 10 reward models with Dirichlet-sampled weights) and each hypothesis h_i, empirical accuracy = fraction of u's top-quartile responses (by u's weighted-ensemble reward score across the 8 candidate responses per prompt) that satisfy h_i, as assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i. Spearman ρ is then computed between the vector of LLM log-likelihood scores [score_1, …, score_N] and the vector of empirical accuracies [acc_1, …, acc_N] across all N hypotheses, averaged over the 50 dev users. This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.\\n\\nWe note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences—a limitation consistent with documented self-preference bias in LLM-as-judge evaluation (arXiv 2601.20913). To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis satisfaction classifier (cross-model calibration check); if ρ remains above 0.6 under cross-model evaluation, the warm-start assumption is validated against self-consistency inflation. If cross-model ρ falls below 0.6 while same-model ρ exceeds it, we treat this as evidence of self-consistency inflation and default to the uniform prior (τ→∞) in the main experiments, flagging the discrepancy as a stated limitation. If both same-model and cross-model ρ fall below 0.6, we acknowledge that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for this hypothesis class and defer warm-start calibration to Phase 2.\\n\\nStage 3—EIG-Based Binary Elicitation Loop with Disconfirmation Quota (algorithm specification): The full hypothesis set H = H_pos ∪ H_neg is placed in a single EIG-ranked pool. At each turn, FABEL selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2 — and poses it as a binary yes/no confirmation. The posterior updates via Bayes' rule with a noise term calibrated on held-out demo pairs. We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization H(p(h_i)) is equivalent to EIG-based selection. The loop terminates when joint preference entropy drops below threshold θ (empirically 3–5 turns).\\n\\nDisconfirmation probe handling follows option (a)—probes are included in the EIG pool and selected by EIG only when maximally uncertain. This is algorithmically cleanest: EIG without H_neg would face a pool containing only confirmatory hypotheses, creating a structural selection bias toward echo-chamber convergence regardless of EIG's own informativeness criterion. Including H_neg in the pool makes the probe design a prior-shaping device rather than a scheduling override—EIG's entropy criterion then serves as a bidirectional diagnostic. If H_neg probes are never selected (prior already confidently classifies them as false), this is evidence of good prior calibration; if frequently selected (probes have high posterior entropy at elicitation start), this signals prior miscalibration requiring attention.\\n\\nSoft minimum quota: To prevent the degenerate case where warm-start prior overconfidence silently suppresses all falsifying questions, at least ⌈K_neg / 3⌉ disconfirmation probes must be asked if the loop runs ≥3 turns. Quota-forced questions bypass EIG ordering for their designated turn but receive normal Bayesian updates. The 'disconfirmation selection rate'—fraction of turns where EIG (prior to quota enforcement) would have selected a H_neg hypothesis—is reported as a diagnostic distinguishing well-calibrated priors (low rate: probes already resolved by warm start) from miscalibrated ones (high rate: probes still maximally uncertain at elicitation start). The falsification rate—fraction of posterior updates that decrease hypothesis probability—is reported as a secondary diagnostic.\\n\\nStage 4—Personalized Generation: The confirmed/disconfirmed hypothesis set is injected as a structured system prompt without fine-tuning.\\n\\nMVP Experimental Design (EMNLP 2026 ARR deadline May 25, 2026):\\n- Benchmark: PersonalLLM (ICLR 2025), using its reward-model-based simulated user evaluation infrastructure (public dataset: HuggingFace namkoong-lab/PersonalLLM); simulated evaluation eliminates GPT-4-judge latency and cost, enabling full experimental sweep within the 15-day window\\n- Human evaluation study (EMNLP Main strengthening, optional stretch): n≈20 crowdsourced participants via Prolific; each participant interacts with FABEL over 10 PersonalLLM prompts and evaluates personalized vs. baseline responses; setup requires ~1 agent-day (days 3–4, running in parallel with automated experiments); cost ~$100–200; the study is underpowered for statistical inference and results are reported descriptively—it provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas, reported descriptively\\n- Backbone: Qwen2.5-7B-Instruct (single backbone for all methods)\\n- Baselines (4): (1) HyPerAlign—demonstration-grounded, no validation; (2) GATE binary—binary questions, no Bayesian posterior, no demonstration grounding; (3) PROSE—iterative preference inference from demonstrations, no user interaction, no Bayesian posterior; applied by running PROSE's generate→compare→update pipeline on PersonalLLM demonstrations, evaluating via reward model; (4) BED-LLM—LM-generic-prior EIG Bayesian with multiple-choice questions; reimplemented from paper description (no public code; Rao-Blackwellized EIG estimator + rejection-sampling update, ~45–50 LLM calls/step); time-boxed to 3–4 agent-days with fallback to 'BED-LLM-approx' (entropy-based selection + rejection-sampling, no full RB-EIG) if faithful replication is infeasible, with explicit labeling\\n- Core ablation (1): warm-start prior (τ-scaled from demos) vs. uniform prior (τ→∞), directly isolating the demonstration-grounded initialization contribution\\n- Primary metrics: PersonalLLM reward-model win rates (main); average elicitation turns (efficiency); disconfirmation selection rate + falsification rate (diagnostics); human preference rates if study included; same-model vs. cross-model Spearman ρ (Stage 2a calibration circularity diagnostic)\\n- Phase 2 extensions (camera-ready / full paper): LaMP-4/6/7 text generation benchmarks; AMPLe and FSPO baselines; full ablation battery (probes included vs. excluded; EIG vs. random ordering; K sensitivity N∈{3,5,10}; τ sensitivity; full BED-LLM replication verification); additional backbone (Qwen2.5-14B-Instruct or Llama 4 Maverick)\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"description\": \"EMNLP 2026 MVP — PRIMARY mode\",\n      \"gpu_hours\": \"~150h A100 (MVP: PersonalLLM only, 4 baselines, 1 backbone, 1 ablation)\",\n      \"h100_equivalent\": \"~75h H100-equivalent (at 2× A100/H100 throughput ratio) — explicitly within the ≤200 H100-hour hard constraint\",\n      \"gpu_utilization\": \"High (~85–90%): agent continuously queues inference jobs with no human wait time; primary idle periods are inter-job I/O and BED-LLM implementation phase\",\n      \"timeline\": \"12–14 days with 2× A100s running in parallel; Prolific human study set up days 3–4 in parallel, adding <1 agent-day overhead; cross-model ρ check (Llama-3.1-8B as hypothesis classifier) adds ~0.25 agent-days to Stage 2a\",\n      \"team\": \"0 (3–5h initial setup)\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 agent reasoning turns)\",\n      \"estimated_gpu_cost\": \"$300–450 at ~$2–3/hr A100 rental\",\n      \"human_study_cost\": \"~$100–200 (n≈20 Prolific participants at ~$5–10/participant; set up in parallel days 3–4)\",\n      \"cost_notes\": \"PersonalLLM reward-model evaluation (simulated) eliminates GPT-4-judge cost; total project cost $550–900 including optional human study; Phase 2 adds ~$400–600 GPU and ~$150–300 GPT-4-judge for LaMP tasks\",\n      \"speed_bottleneck\": \"BED-LLM EIG reimplementation (no public code; time-boxed 3–4 agent-days with simplified fallback); PROSE implementation straightforward (~1 agent-day, purely prompt-based); Stage 2a calibration analysis (same-model + cross-model ρ) adds ~0.75 agent-days total\",\n      \"compliance_note\": \"150h A100 ÷ 2 (H100/A100 throughput ratio) = 75h H100-equivalent, well within the 200 H100-hour limit\"\n    },\n    \"human_in_loop\": {\n      \"description\": \"Full paper (post-EMNLP, adds LaMP + full ablations)\",\n      \"gpu_hours\": \"~300h A100\",\n      \"gpu_utilization\": \"Moderate (~50–60%): agent continuously queues inference jobs between human approval gates; BED-LLM replication verified at first review gate before full baseline run\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,200–2,000 reasoning turns)\",\n      \"estimated_gpu_cost\": \"$600–900\",\n      \"risk_note\": \"Warm-start prior calibration (Spearman ρ threshold) must be validated on PersonalLLM dev split before committing to full experimental sweep; both same-model and cross-model ρ confirmed at a dedicated calibration gate before main experimental sweep; τ selection and BED-LLM replication fidelity confirmed at dedicated review gates\"\n    },\n    \"manual\": {\n      \"description\": \"Full paper (post-EMNLP, adds LaMP + full ablations)\",\n      \"gpu_hours\": \"~200h A100\",\n      \"gpu_utilization\": \"Low (~20–30%): GPU idles while researchers implement BED-LLM baseline, write pipeline code, and analyze results\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"$400–600 at ~$2–3/hr A100 rental\",\n      \"cost_notes\": \"GPT-4-as-judge for LaMP evaluation adds ~$150–300; total project cost $550–900\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings via ACL ARR (deadline May 25, 2026 — 15 days from project start May 10, 2026) — PRIMARY realistic target; MVP scope (PersonalLLM, 4 baselines, 1 backbone, 1 ablation + Stage 2a calibration analysis with cross-model ρ check) is credible for EMNLP Findings; adding the n≈20 Prolific human study puts EMNLP Main within reach if human results are positive — this is the stretch Main goal, not the base expectation; targets EMNLP 2026 Findings as the primary submission outcome\",\n    \"ICLR 2027 (expected submission deadline ~October 2026) — SECONDARY target if EMNLP 2026 submission scope is insufficient or if full paper (LaMP + full ablation battery) is preferred; strongest venue fit given GATE (ICLR 2025), OPEN (ACL 2024), and BED-LLM (ICLR 2026) lineage; full paper with multi-benchmark and human study comfortably meets Main bar\",\n    \"AAAI 2027 (expected abstract/paper deadline ~August–September 2026) — TERTIARY target with sufficient runway for full experimental sweep including LaMP benchmarks and multiple backbone ablations\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"OPEN: Bayesian Preference Elicitation with Language Models (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) — foundational BOED-for-preference-elicitation work; combines EIG-based query selection with LM feature extraction for content recommendation; selects pairwise queries over binary feature vectors (|F|=10) using particle-filter Bayesian update with Bradley-Terry model; prior initialization via LM-ranked feature importances (domain-generic warm start: w_i = 1.2 − 0.12i for rank i), NOT user-demonstration-conditioned; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-specific demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism; cite as the foundation of the BOED-for-preference-elicitation line that BED-LLM extends and FABEL further advances\",\n    \"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design (arXiv 2508.21184, ICLR 2026) — extends OPEN to discrete language hypothesis sets; initializes from an LM-generic prior p_f(θ;∅) (the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations; notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions as a technical requirement (small single-token response spaces ensure p_LLM provides meaningful uncertainty for EIG estimation); EIG uses Rao-Blackwellized N=15-sample estimator + rejection-sampling posterior update (~45–50 LLM calls/turn); evaluates on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions game; no public code; reimplementation time-boxed to 3–4 agent-days with simplified fallback; FABEL differentiates in three ways: (1) prior conditioned on this user's K demonstrations vs. BED-LLM's demo-agnostic LM prior; (2) binary yes/no confirmation vs. BED-LLM's multiple-choice format; (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work\",\n    \"AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference (arXiv 2604.03925, April 2026, Lin, Li, Xing, Yang, Ge, Yamada, Zhang, Zhang, Tu) — concurrent work in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL; externalizes Bayesian inference from the LLM: a symbolic module maintains a posterior initialized uniformly (b₀,m = 1/M), updated via Bayes' rule with a Luce choice model likelihood; a frozen LLM contributes via multi-sample Dirichlet aggregation; entropy-adaptive fusion weights symbolic vs. LLM signal by predictive confidence—entropy-adaptive fusion is a signal-weighting mechanism, not a query selection criterion; queries presented in fixed sequential rounds (T=5), no EIG-based active selection; hypothesis set = pre-defined linear utility functions over scalar attributes from training-split lookup table, not free-form natural language stylistic attributes; evaluated on recommendation (flight, hotel, web shopping), not LLM response-style personalization; FABEL's four-way differentiation: (1) user-specific demo-conditioned temperature-scaled warm prior vs. AdaptFuse's uniform cold-start; (2) EIG-based active query selection vs. AdaptFuse's fixed sequential protocol; (3) free-form LLM-generated natural language stylistic hypotheses vs. AdaptFuse's pre-defined scalar utility functions; (4) mandatory disconfirmation probes absent from AdaptFuse; acknowledge as concurrent work in landscape cluster (3c)\",\n    \"AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) — active Bayesian preference learning for LLM personalization; pairwise comparison queries over LLM responses, modified posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection to minimize required comparisons; directly adjacent to FABEL's active Bayesian personalization setting; FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary stylistic hypothesis confirmation rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe; include as related work in landscape cluster (3b); include as Phase 2 baseline on LaMP tasks\",\n    \"MAPLE: A Framework for Active Preference Learning Guided by Large Language Models (arXiv 2412.07207, AAAI 2025, Mahmud, Nakamura, Zilberstein) — uses LLM-conditioned preference function distributions with a language-conditioned active query selection mechanism over pairwise trajectory rankings for general alignment tasks (vehicle routing, web navigation); in the same broad active Bayesian preference learning space as FABEL; FABEL differs: (1) binary yes/no stylistic hypothesis confirmation grounded in user demonstrations rather than trajectory-level pairwise rankings; (2) user-specific demo-conditioned warm prior absent from MAPLE; (3) LLM response-style personalization domain rather than RL alignment; cite as AAAI 2025 active preference learning context in landscape cluster (3b)\",\n    \"PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) — directly competitive with FABEL Stage 1; iterative generate→compare→update refinement of free-form preference descriptions + component-level verification against held-out samples; 33% improvement over CIPHER on summarization/email; no user interaction, no Bayesian posterior, no disconfirmation mechanism; baseline and key differentiator\",\n    \"GATE: Eliciting Human Preferences with Language Models (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) — binary yes/no variant underperforms open-ended due to absence of Bayesian posterior; baseline\",\n    \"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation (arXiv 2505.00038, May 2025) — demonstration-grounded hypothesis generation without user validation; baseline\",\n    \"Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing (arXiv 2604.02485, April 2026) — motivates disconfirmation probe design; 42%→56% rule-discovery success with counter-example prompting; motivates H_neg pool inclusion in FABEL Stage 3\",\n    \"Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) — amortized variational inference with conjugate Beta prior conditioned on in-context preference demonstrations; conceptually adjacent to FABEL's warm-start but differs in domain (pairwise reward modeling vs. interactive style elicitation), representation (Beta prior on scalar rewards vs. binary hypothesis set), and interaction mode (passive vs. active EIG confirmation); acknowledge in related work to pre-empt warm-start novelty challenge\",\n    \"Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (arXiv 2601.20913, 2026) — provides hypothesis testing framework for cross-model evaluation with calibrated confidence metrics; cited to motivate FABEL's cross-model ρ check (using Llama-3.1-8B-Instruct as hypothesis classifier to bound the self-consistency inflation artifact in Stage 2a)\",\n    \"Active Task Disambiguation with LLMs (arXiv 2502.04485, ICLR 2025) — BED applied to task clarification; related but not personalization-focused\",\n    \"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization (arXiv 2506.02827, 2025) — applies trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline (a clarification resolver generating optimal questioning trajectories plus a summarizer for task-aligned responses); remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior; achieves 9.32% improvement over STaR-GATE on preference elicitation tasks; cited as an open-ended, non-Bayesian clarification baseline in landscape cluster (5)\",\n    \"PEBOL: Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation (arXiv 2405.00981, RecSys 2024) — NLI + Bayesian BO for recommendation; related\",\n    \"Asking Clarifying Questions for Preference Elicitation With Large Language Models (arXiv 2510.12015, 2025) — diffusion-inspired clarifying question model; distinct from PEBOL\",\n    \"FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users (arXiv 2502.19312, 2025) — deferred to Phase 2 / full paper; requires meta-learned model setup adds ~1–2 weeks engineering overhead\",\n    \"PersonalLLM: Tailoring LLMs to Individual Preferences (ICLR 2025) — primary benchmark; public dataset HuggingFace namkoong-lab/PersonalLLM (9,402 train / 1,000 test prompt-response pairs, 8 candidate responses per prompt scored by 10 reward models, simulated users as Dirichlet-weighted reward model ensembles); reward-model-based simulated evaluation eliminates GPT-4-judge dependency and enables 15-day timeline\",\n    \"LaMP: When Large Language Models Meet Personalization (ACL 2024) — secondary benchmark for Phase 2; LaMP-4/6/7 text generation tasks assess format and style personalization\",\n    \"Calibrating Language Models with Adaptive Temperature Scaling (arXiv 2409.19817, EMNLP 2024) — post-hoc temperature calibration method for LLM token probabilities without fine-tuning; informs FABEL's τ-scaled warm prior design: p(h_i) ∝ exp(score_i / τ) with τ selected via dev-set rank-correlation criterion\"\n  ],\n  \"description\": \"Personalizing LLMs to individual users is hindered by four complementary failure modes: HyPerAlign generates demonstration-grounded preference hypotheses but skips user validation; the BOED-for-preference-elicitation line—established by OPEN (ACL 2024) and extended by BED-LLM (ICLR 2026)—applies principled EIG-based Bayesian elicitation but lacks user-specific demonstration-conditioned priors (OPEN uses domain-generic LM-ranked feature importances; BED-LLM uses an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution, not conditioned on any specific user's demonstrations); PROSE (ICML 2025) iteratively refines free-form preference descriptions from writing samples but has no user interaction and no formal Bayesian posterior, leaving ambiguous hypotheses unresolved; and AdaptFuse (arXiv 2604.03925, April 2026), a concurrent work, externalizes a symbolic Bayesian posterior over pre-defined discrete hypotheses with entropy-adaptive frozen-LLM fusion—in the same training-free Bayesian hypothesis-set inference family as FABEL—but initializes from a uniform prior (not user-demonstration-conditioned), uses fixed sequential query rounds (T=5) rather than EIG-based active selection, and lacks disconfirmation probes. AMPLe (ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation but also cold-starts from pairwise comparisons and lacks disconfirmation probes. We propose FABEL (Falsification-Aligned Binary Elicitation Loop), which extends the OPEN→BED-LLM BOED lineage by (1) initializing a temperature-scaled warm Bayesian prior p(h_i) ∝ exp(score_i / τ) from K=5–10 user-specific demonstrations—user-specific rather than domain-generic or demo-agnostic; (2) including K_neg=4–6 explicit disconfirmation probes in the EIG-ranked hypothesis pool, generated via a dedicated falsification prompt that requires citing demonstration-level evidence for each probe, making the probe design a prior-shaping device that ensures EIG always has access to genuinely falsifying evidence; (3) applying a soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns) to prevent warm-start overconfidence from silently suppressing falsifying questions; (4) applying a factored posterior approximation with EIG-based binary yes/no confirmation (vs. BED-LLM's multiple-choice format, which is required for reliable LLM uncertainty quantification but increases cognitive load) to resolve remaining uncertainty in 3–5 turns; and (5) explicitly acknowledging that under the factored (independent) posterior approximation, marginal entropy maximization is equivalent to EIG-based selection. Stage 2a includes a calibration analysis (Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy on 50 PersonalLLM dev users, where empirical accuracy is operationalized as the fraction of each simulated user's top-quartile reward-model responses satisfying each hypothesis) that validates the warm-start assumption and selects τ; if no τ achieves ρ > 0.6, the system defaults to a uniform prior and flags the calibration failure. Critically, Stage 2a also addresses a circularity in this operationalization—the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and accuracy labels—by additionally reporting ρ using Llama-3.1-8B-Instruct as an independent hypothesis classifier (cross-model calibration check; arXiv 2601.20913); if cross-model ρ falls below 0.6 while same-model ρ exceeds it, the system defaults to the uniform prior, treating the discrepancy as evidence of self-consistency inflation. The EMNLP 2026 MVP targets Findings as the primary outcome, with an optional n≈20 Prolific human study (days 3–4, ~$100–200) that is underpowered for statistical inference and reported descriptively—providing preliminary external validity evidence beyond simulated personas, reported descriptively. The central testable claim: demonstration-grounded user-specific warm priors reduce required elicitation turns vs. both OPEN (domain-generic warm start) and BED-LLM (demo-agnostic LM prior) while achieving higher personalization win rates than non-interactive methods (PROSE, HyPerAlign). LaMP benchmarks, AMPLe/FSPO baselines, and full ablations are deferred to Phase 2.\",\n  \"project_name\": \"falsif_guided_pe\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"BED-LLM (arXiv 2508.21184, ICLR 2026) is unacknowledged and directly covers the core mechanism: it samples N=15 hypotheses, uses EIG to select questions designed to 'slice the hypothesis pool into roughly balanced subsets,' and applies Bayesian rejection-sampling updates — the central algorithmic contribution of FABEL. The paper must be cited and clearly differentiated.\", \"GATE (ICLR 2025) already includes a yes-or-no binary question variant ('restricts the LM to generating binary yes-or-no questions'). The generator's landscape description characterizes GATE as purely open-ended, which is factually incomplete. The binary format alone is not a differentiating contribution.\", \"PEBOL arXiv attribution error: the generator cites '(arXiv 2510.12015)' as the PEBOL paper, but arXiv 2510.12015 is 'Asking Clarifying Questions for Preference Elicitation With Large Language Models' (a diffusion-inspired model, not PEBOL). The actual PEBOL paper is arXiv 2405.00981 (RecSys 2024). This is a citable factual error that would immediately surface in peer review.\", \"Venue deadline is misidentified: the generator claims 'ACL ARR June 2026 cycle, deadline ~June 15 2026' but the confirmed EMNLP 2026 ARR submission deadline is May 25, 2026 (per official EMNLP 2026 CFP and ACL ARR Dates page). The June cycle does not feed EMNLP 2026. This affects the entire planning horizon.\", \"LLM confirmation bias undermines the 'falsification' framing: arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs systematically exhibit confirmation bias in hypothesis testing — they select confirmatory rather than falsifying evidence. This suggests that LLM-generated hypotheses will be easier to confirm than disconfirm, and the Bayesian posterior may converge spuriously. The paper should address whether its hypotheses are genuinely falsifiable or merely confirmable.\", \"PRISM benchmark misfit: PRISM (NeurIPS 2024) is designed for multicultural value alignment and subjective disagreement, not individual preference personalization of LLM response style. Evaluating FABEL — which targets writing format, structure, and tone — on PRISM is not well-motivated. The authors should justify why PRISM reveals anything beyond PersonalLLM for the proposed application.\", \"GPU cost realism: evaluating against FSPO (which requires a pretrained meta-learning model) as a baseline may require non-trivial setup not captured in the 150h A100 manual estimate; the GPT-4-as-judge costs for PersonalLLM-scale evaluation (1500 simulated users) could also be underestimated.\"]\nFeedback: The core insight — combining HyPerAlign-style demonstration-grounded hypothesis generation with EIG-based binary validation — is a coherent contribution to the personalization literature, but the generator must make three priority revisions before this is ready to submit:\n\n1. **Reposition against BED-LLM (ICLR 2026)**: 'This idea is too similar to BED-LLM (arXiv 2508.21184, ICLR 2026). Specifically, BED-LLM samples N=15 hypotheses, selects questions via EIG to split the hypothesis set, and updates beliefs with Bayesian rejection sampling — the same pipeline as FABEL. To differentiate, the generator should (a) explicitly compare against BED-LLM as a baseline, (b) emphasize FABEL's unique starting point of few-shot user demonstrations (HyPerAlign-style) rather than free-form hypothesis sampling, and (c) show that grounding hypotheses in demonstrations produces qualitatively different, more accurate preference summaries than BED-LLM's unconditioned sampling. The application domain (LLM response style vs. item recommendation) is a real differentiator worth foregrounding.'\n\n2. **Fix the GATE landscape description**: Acknowledge the GATE binary variant and clarify why FABEL differs — likely the combination of demonstration-grounded hypothesis generation (not free-form question asking) with Bayesian belief tracking is the real gap, not the binary format alone.\n\n3. **Fix the PEBOL arXiv attribution (2510.12015 → 2405.00981) and the venue deadline (June 15 → May 25).** These are immediate disqualifiers for a careful reviewer.\n\n4. **Address confirmation bias**: Add analysis or ablation showing the LLM does not systematically generate only confirmable hypotheses. Consider adding a 'disconfirmation probe' to the hypothesis set by design, or show empirically that the posterior does update in both directions.\n\nIf BED-LLM is incorporated as a strong baseline and FABEL shows clear gains on the LLM response-style personalization task (PersonalLLM win-rates, reduced user-turn word count), the contribution is publishable at EMNLP Findings level. As written, the novelty gap is insufficient for EMNLP Main.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Venue requirement failure: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, ≤16 days). The proposal itself concedes this deadline 'has effectively passed for a project beginning now (May 10, 2026)' and retargets to AAAI 2027/ICLR 2027. This is an honest but fatal mismatch: the idea as scoped cannot satisfy the user's primary hard constraint. Either a severely stripped-down MVP (PersonalLLM only, BED-LLM + HyPerAlign as the two primary baselines, no LaMP sweep, no full ablation, simulated user evaluation only) must be proposed for the 16-day window, or the idea should explicitly declare EMNLP 2026 out of scope.\", \"CRITICAL — Compute constraint non-compliance in the 16-day-feasible mode: The auto_research mode (the only mode that meets ≤16 days) uses ~600h A100. At the industry-standard ~2–2.5× H100/A100 throughput ratio, this translates to approximately 240–300 H100-hours — exceeding the ≤200 H100-hour hard constraint by 20–50%. A minimum viable experiment (PersonalLLM + 3 baselines, 1 backbone, core ablation) would likely require only ~150–180h A100 (≈75–90h H100), well within limits — but this needs to be explicitly scoped and stated rather than leaving the constraint compliance implicit.\", \"Missing citation — PROSE (arXiv 2505.23815, ICML 2025): 'Aligning LLMs by Predicting Preferences from User Writing Samples' (Aroca-Ouellette et al., Apple ML Research) uses user writing demonstrations to iteratively refine free-form preference descriptions, then verifies component claims against held-out demonstrations. This is directly competitive with FABEL Stage 1 and was not cited anywhere in the landscape. A reviewer would flag this immediately. To differentiate: PROSE infers free-form preferences with no user interaction and no Bayesian posterior; FABEL generates binary-confirmable hypotheses, tracks a formal Bayesian posterior, selects questions via EIG, and adds mandatory disconfirmation probes. PROSE should be added as a sixth baseline or at minimum a related work requiring explicit differentiation.\", \"BED-LLM reimplementation risk underestimated for 16-day window: The proposal's own auto_research note flags 'faithful replication of their rejection-sampling update' as the primary engineering risk. BED-LLM's EIG estimator involves non-trivial sampling over LLM predictive distributions at each turn. Reproducing this within a 16-day timeline — alongside implementing FABEL itself and running PersonalLLM/LaMP evaluations — is aggressive. The proposal should either identify an existing public BED-LLM implementation or explicitly time-box the reimplementation risk.\", \"ICRM / Bayesian Preference Learning for Test-Time Steerable Reward Models (arXiv 2602.08819, Feb 2026) not cited: This paper uses a Beta posterior conditioned on in-context preference demonstrations for test-time reward model steering — partial overlap with FABEL's warm-start initialization from demonstrations. The settings differ (pairwise reward modeling vs. interactive style elicitation), but the Bayesian in-context conditioning from demonstrations is directly adjacent and a reviewer familiar with this work might question the warm-start prior novelty. It should be acknowledged in the related work.\"]\nFeedback: The generator has addressed all six Round 1 issues cleanly and the core idea remains sound, but two critical problems prevent a pass verdict:\n\n**Priority 1 — Scope the idea for the actual 16-day / EMNLP 2026 constraint (or declare a mismatch).**\nThe generator honestly acknowledges EMNLP 2026 is unreachable for a full 5-baseline sweep across PersonalLLM + LaMP. But the user's hard constraint is 16 days and EMNLP 2026. The generator should choose one of:\n(a) Propose a stripped-down EMNLP 2026 MVP: PersonalLLM benchmark only, 3 baselines (HyPerAlign, BED-LLM, GATE binary), 1 LLM backbone (Qwen 3.5), simulated user evaluation using the PersonalLLM reward-model infrastructure, 1 ablation (warm vs. uniform prior). Estimated compute: ~150h A100 (~75h H100-equivalent), 12–14 days in auto mode. This fits all hard constraints.\n(b) Explicitly flag the idea as AAAI 2027 / ICLR 2027 scope with a concrete explanation of why 16 days is insufficient for the full version — so the user can make an informed decision.\n\n**Priority 2 — Add PROSE as a baseline and missing citation.**\nPROSE (arXiv 2505.23815, ICML 2025) directly competes with FABEL's Stage 1: it takes user writing samples and iteratively refines preference descriptions with component verification. Cite it, differentiate it (PROSE: free-form, non-interactive, no Bayesian posterior; FABEL: binary hypotheses, interactive EIG confirmation, formal posterior, disconfirmation probes), and include it as a baseline. Without PROSE, the novelty argument has an obvious gap that peer reviewers would flag.\n\n**Priority 3 — Fix the compute compliance in auto mode.**\nRestate the minimum-viable-experiment compute as ~150–180h A100 and explicitly confirm it falls under 200 H100-hour equivalent. The full 600h A100 ablation sweep is 'nice to have' for camera-ready, not required for ARR submission.\n\nIf the generator delivers a scoped EMNLP 2026 MVP (Priority 1) with PROSE integrated (Priority 2) and compute compliance verified (Priority 3), the idea is publishable at EMNLP 2026 Findings level. The core novelty — warm-start Bayesian initialization from demonstrations + EIG binary confirmation + mandatory disconfirmation probes — is genuinely new and the empirical design (warm vs. cold prior ablation, disconfirmation rate diagnostic) is strong. The differentiation from BED-LLM (cold start, item recommendation) and from PROSE/HyPerAlign (no interactive validation) is clean.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"OPEN (arXiv 2403.05534, ACL 2024) — 'Bayesian Preference Elicitation with Language Models' — is not cited. This paper applies Bayesian Optimal Experimental Design (BOED, mathematically equivalent to EIG) with LMs to select informative preference-elicitation questions in natural language. It is a direct algorithmic predecessor to BED-LLM for the preference elicitation setting and a reviewer aware of it would challenge FABEL's EIG-over-BED-LLM positioning. The proposal should cite OPEN as the foundation of the BOED-for-preference-elicitation line, position BED-LLM as the current state of that line, and clarify how FABEL (demonstration-grounded warm start + disconfirmation probes) extends beyond both.\", \"Disconfirmation probe / EIG interaction is algorithmically underspecified. The proposal includes K_neg=4–6 disconfirmation probes in the hypothesis set but does not specify how EIG-based selection handles them at each turn: (a) are they included in the EIG-ranked pool and selected only when EIG identifies them as maximally informative — in which case the EIG criterion may already approximate the disconfirmation behavior, making the explicit probe design partially redundant; (b) are they always asked in the first K_neg turns before EIG kicks in — which wastes turns if the demonstrations already resolved them; or (c) are they asked as post-loop audits — which breaks the Bayesian update chain. This interaction must be precisely specified in the algorithm description, since it determines whether the disconfirmation probe mechanism adds genuine information-theoretic value beyond EIG or is purely a diagnostic overlay.\", \"Warm-start prior calibration is assumed but unvalidated. The proposal initializes p(h_i = true | demonstrations) using LLM-estimated likelihoods conditioned on K demonstrations. LLM probability estimates are notoriously poorly calibrated — overconfident estimates would concentrate mass on the wrong hypotheses before any user interaction, potentially causing slower convergence than a uniform (BED-LLM-style) cold start. The paper should either (a) include an empirical calibration check showing the LLM-estimated likelihoods are well-ordered relative to ground-truth hypothesis accuracy, or (b) add a temperature-scaling or entropy-regularized prior initialization step with explicit justification.\", \"EMNLP 2026 Main vs. Findings targeting realism. The user specified EMNLP 2026 Main as the primary target. The MVP (single benchmark PersonalLLM, simulated reward-model evaluation, one backbone Qwen 3.5-7B, one ablation) is credible for EMNLP Findings but borderline for Main. EMNLP Main typically requires either (a) multi-benchmark generalization, (b) a human user study even at small scale, or (c) a theoretically novel contribution beyond component combination. The current design lacks all three. The proposal should either explicitly target Findings as the realistic primary target, or strengthen one of these dimensions — even a 20-person crowdsourced preference evaluation using the PersonalLLM prompts would substantially strengthen the Main case within the 16-day window.\"]\nFeedback: The proposal has cleanly addressed all Round 1 and Round 2 critical issues: venue deadline is correct (May 25, 2026), compute is within budget (~75h H100-equivalent), PROSE is included as baseline #3, BED-LLM is confirmed accepted at ICLR 2026, ICRM is acknowledged, and the MVP scope is explicitly and realistically defined. The core idea — warm-start Bayesian prior from demonstrations + EIG binary confirmation + disconfirmation probes — is a coherent, well-motivated contribution. Three targeted revisions will bring this to pass:\n\n**Fix 1 — Add OPEN to the landscape (1 paragraph in related work):** 'This idea is too similar to OPEN (arXiv 2403.05534, ACL 2024) without acknowledgment. OPEN applies BOED with LMs to select informative preference questions in NL — the same mathematical framework as BED-LLM, specifically for preference elicitation. To differentiate: OPEN lacks demonstration-conditioned priors, requires cold-start initialization, and has no disconfirmation mechanism. Include OPEN in the BOED lineage alongside BED-LLM and clarify that FABEL's contribution is the warm-start + disconfirmation extension of this line.'\n\n**Fix 2 — Specify disconfirmation probe algorithm precisely:** Add a paragraph to Stage 3 clarifying whether disconfirmation probes are (a) included in the EIG-ranked pool, (b) asked as mandatory initial turns, or (c) reserved as post-convergence audits. Option (a) is algorithmically cleanest — EIG will naturally select them when they are maximally uncertain, making the explicit design a prior-shaping device rather than a scheduling override. Report the empirical fraction of turns where EIG selects a disconfirmation probe vs. a positive hypothesis as a diagnostic.\n\n**Fix 3 — Calibration check or regularization for warm-start prior:** Add either (a) a small analysis showing that LLM-estimated likelihoods are well-ordered relative to demonstration-consistent hypotheses (even a rank-correlation analysis on 50 PersonalLLM examples would suffice), or (b) a temperature-scaled prior initialization: p(h_i) ∝ exp(LLM_log_likelihood / τ) with τ tuned to match empirical calibration. This directly addresses the most technically vulnerable assumption in the method.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL reproducibility error — 'Qwen 3.5-7B-Instruct' does not exist: Qwen3.5 (released Feb 2026) contains 4B, 27B, 35B-A3B (MoE), and 397B-A17B (MoE) variants; there is no 7B model in the Qwen3.5 family. This model name appears throughout the proposal as the single backbone. The correct alternatives are Qwen2.5-7B-Instruct (huggingface.co/Qwen/Qwen2.5-7B-Instruct, widely used in personalization benchmarks) or Qwen3-8B (huggingface.co/Qwen/Qwen3-8B). A reviewer or reproduction attempt would fail immediately at environment setup. Fix: replace all instances of 'Qwen 3.5-7B-Instruct' with 'Qwen2.5-7B-Instruct' or 'Qwen3-8B' with the appropriate HuggingFace identifier.\", \"Missing citation — AMPLe (arXiv 2411.00524, ACL 2025): 'Comparison-based Active Preference Learning for Multi-dimensional Personalization' (Oh, Lee, Ok; ACL 2025, with public code at github.com/ml-postech/AMPLe) uses Bayesian inference with modified posterior updates and a generalized binary-search-inspired active query selection strategy to capture implicit multi-dimensional preferences for LLM personalization — directly adjacent to FABEL's active Bayesian personalization setting. While AMPLe uses pairwise comparison queries rather than demonstration-conditioned hypotheses (making differentiation clear: FABEL provides a warm prior from demonstrations, asks binary hypothesis confirmation rather than item comparisons, and adds mandatory disconfirmation probes), the omission of an ACL 2025 active Bayesian preference learning paper in the LLM personalization domain is a gap that reviewers familiar with the area would notice. Add to the landscape under cluster (3) or create a new cluster for comparison-based active preference learning.\", \"Unstated hypothesis-independence assumption in Stage 3 Bayesian update: The per-hypothesis Bayesian update (applying Bayes' rule independently to each h_i) implicitly treats all preference hypotheses as statistically independent. In practice, preference attributes are highly correlated (e.g., 'prefers brevity' correlates with 'prefers bullet points over prose'). Under this factored approximation, the posterior update may be inconsistent: confirming 'prefers brevity' should increase the probability of correlated hypotheses, but the factored update leaves them unchanged. The proposal should either (a) acknowledge this as a stated approximation (factored posterior) in the algorithm description, or (b) briefly justify why correlations are low in the PersonalLLM hypothesis space (e.g., by reporting inter-hypothesis correlation on the dev split). This is a technical vulnerability that a Bayesian reviewer would raise.\", \"EIG terminology imprecision: Stage 3 states 'selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2' and also calls this 'EIG-based.' Maximum marginal entropy equals EIG only under the factored (independent) posterior assumption. Under a correlated posterior, maximizing joint EIG requires summing over hypotheses and is strictly different from marginal entropy maximization. Since the proposal uses a factored update, calling it 'EIG-based' is technically correct but only by virtue of the unstated independence assumption. Clarify in one sentence: 'Under the factored posterior approximation, maximizing marginal entropy H(p(h_i)) is equivalent to EIG-based selection.'\"]\nFeedback: Round 4 has resolved all three Round 3 issues cleanly: OPEN is now thoroughly cited and integrated into the BOED lineage narrative; the disconfirmation probe algorithm is precisely specified (EIG pool inclusion + soft minimum quota); and Stage 2a calibration analysis (Spearman ρ, τ selection on 50 dev users) directly addresses the warm-start prior vulnerability. The core idea is solid and publication-ready at EMNLP Findings level once the following targeted fixes are applied:\n\n**Fix 1 (Critical) — Replace non-existent model name throughout.** 'Qwen 3.5-7B-Instruct' does not exist in the Qwen3.5 family (which has 4B, 27B, and MoE variants only). Replace with 'Qwen2.5-7B-Instruct' (Qwen/Qwen2.5-7B-Instruct on HuggingFace — available, widely benchmarked) or 'Qwen3-8B' (Qwen/Qwen3-8B on HuggingFace). This affects every experimental description and the resource estimate; apply the substitution consistently.\n\n**Fix 2 (Moderate) — Cite AMPLe (arXiv 2411.00524, ACL 2025).** Add one paragraph in Section 2 (Related Work) under active preference learning: 'AMPLe (Oh et al., ACL 2025) uses Bayesian inference with modified posterior updates and active comparison-based query selection for multi-dimensional LLM personalization. FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary hypothesis confirmation (\"does this stylistic claim apply to you?\") rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe.' No ablation needed — citation and differentiation suffice.\n\n**Fix 3 (Minor) — Acknowledge hypothesis-independence assumption.** Add one sentence to Stage 3 after the Bayesian update equation: 'We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization is equivalent to EIG-based selection.' This closes both the EIG terminology issue and the independence assumption gap in one edit.\n\nAfter these three fixes, the proposal has no critical technical gaps, the venue deadline is correct, compute is within budget, and the MVP scope (PersonalLLM + 4 baselines + 1 ablation + Stage 2a calibration) is credibly executable in the 16-day window. Recommend one more targeted revision pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — BED-LLM prior characterization is factually wrong and would be caught by a reviewer who reads the paper. The proposal repeatedly says BED-LLM 'starts from cold uniform prior (no domain ranking, no user demonstrations).' However, the BED-LLM paper defines the initial prior as p_f(θ;h_t=∅) — the LLM's own predictive distribution over hypotheses given no history — which is an LM-generic prior (not uniform), analogous in spirit to OPEN's domain-generic feature importance ranking. Additionally, BED-LLM uses multiple-choice questions (not binary yes/no), because as the paper states, 'having a small space of single-token responses ensures that p_LLM provides meaningful uncertainty over outcomes.' The proposal must correct both: (a) replace 'cold uniform prior' with 'LM-generic prior, not conditioned on user demonstrations'; (b) note that FABEL uses binary yes/no confirmation (lower cognitive load) while BED-LLM uses multiple-choice. The novelty argument remains valid — FABEL's demo-conditioned prior is a real differentiator from BED-LLM's demo-agnostic LM prior — but the current phrasing is inaccurate.\", \"MINOR — Stage 2a calibration analysis is underspecified. The proposal describes 'Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users' but never operationalizes 'empirical hypothesis accuracy' for simulated users. In the PersonalLLM framework, simulated users are represented as weighted ensembles of reward models. The paper must specify: for each hypothesis h_i and each simulated user, ground truth accuracy = fraction of that user's reward-model-preferred responses that satisfy h_i (e.g., for 'prefers bullet points,' check what fraction of high-reward responses are bulleted). Without this operational definition, Stage 2a is unverifiable and a reviewer will ask exactly this question.\", \"MINOR — BED-LLM's application domain is described as 'item recommendation' throughout the proposal, but BED-LLM evaluates on both 20-Questions and preference elicitation via movie-preference multiple-choice questions — a general preference inference setting. While 'item recommendation' is partially correct, the more accurate framing is 'latent preference vector inference from sequential multiple-choice queries, without user demonstrations.' This distinction matters because FABEL's application to LLM response-style personalization (format, tone, structure) is a domain shift, not just a warm-start shift.\"]\nFeedback: Round 4 fixes have all been applied cleanly: Qwen2.5-7B-Instruct replaces the non-existent 'Qwen 3.5-7B-Instruct,' AMPLe is now cited and differentiated in cluster (3b), and the factored posterior approximation is explicitly acknowledged in Stage 3. The proposal is close to passing. Three targeted edits will get it there:\n\n**Fix 1 (Moderate, 1–2 paragraphs) — Correct the BED-LLM prior description.** Replace every instance of 'cold uniform prior' in the BED-LLM description with 'LM-generic prior (p_f(θ;∅): the LLM's unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations).' Add one clause noting that BED-LLM uses multiple-choice questions, not binary yes/no, making FABEL's binary format an additional differentiator. The revised differentiation argument: 'FABEL extends BED-LLM in three ways: (1) prior conditioned on this user's K demonstrations (vs. BED-LLM's demo-agnostic LM prior); (2) binary yes/no confirmation (vs. BED-LLM's multiple-choice format); (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work.'\n\n**Fix 2 (Minor, 1 paragraph) — Operationalize Stage 2a ground truth.** In the Stage 2a description, add: 'For each simulated PersonalLLM dev user u and hypothesis h_i, empirical accuracy = fraction of u's top-quartile reward-model responses that satisfy h_i (assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i, then comparing against the reward model's preference ordering via Kendall τ). This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.'\n\n**Fix 3 (Minor, 1 sentence) — Clarify BED-LLM domain.** Replace 'targets item recommendation' with 'targets latent preference vector inference via movie-preference multiple-choice queries' in the BED-LLM description. This sharpens the domain-shift argument: FABEL is the first to apply the OPEN→BED-LLM BOED lineage to LLM response-style personalization (format, tone, structure) from free-form demonstrations.\n\nWith these three fixes applied, the proposal has no remaining critical gaps. The combination of user-demonstration-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel, the MVP compute fits within the ≤200 H100-hour constraint, and the empirical design (warm vs. cold ablation, Stage 2a calibration, disconfirmation diagnostic) is appropriate for EMNLP Findings.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MINOR — TO-GATE related work description is inaccurate: the proposal states TO-GATE 'applies DPO to clarifying question quality, remaining in the open-ended, non-Bayesian regime,' but independent verification (arXiv 2506.02827 fetched) confirms TO-GATE uses trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline — not just clarifying question quality in isolation. While the non-Bayesian characterization is correct, the narrow phrasing 'DPO to clarifying question quality' misrepresents the method and would be flagged by a TO-GATE-aware reviewer.\", \"MINOR — Disconfirmation probe generation mechanism underspecified: Stage 1 states that Qwen2.5-7B-Instruct generates K_neg=4–6 'hypotheses deliberately constructed to be easily falsifiable given the demonstrations,' but the proposal nowhere specifies the prompt or instructions used to elicit deliberately falsifiable probes as opposed to the model's default confirmatory behavior (which is precisely what arXiv 2604.02485 shows is the default). A reviewer will ask in rebuttal: 'How do you ensure the LLM generates probes that are genuinely falsifiable rather than merely low-confidence confirmatory hypotheses?' The generation mechanism must be concretely specified.\", \"MINOR — Stage 2a τ selection failure mode unspecified: the proposal selects τ as 'the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6,' but provides no fallback if no τ achieves ρ > 0.6 (i.e., if LLM log-likelihoods are uncorrelated with empirical accuracy for some hypothesis class). A reviewer will ask what happens in this case. The paper needs one sentence: e.g., 'If no τ achieves the threshold, we default to τ→∞ (uniform prior) and report this user as a calibration failure in diagnostic analysis.'\", \"MINOR — Human study statistical power and EMNLP Main claim in tension: the proposal simultaneously acknowledges the n≈20 study is 'underpowered for significance' and asserts it 'substantially strengthens the EMNLP Main case per reviewer guidance.' These claims are contradictory. An underpowered real-user study that cannot reach statistical significance does not meaningfully distinguish FABEL from a well-designed ablation — reviewers targeting EMNLP Main will note this. The claim should be hedged to 'provides a qualitative real-user signal and preliminary external validity evidence, not statistical confirmation.'\"]\nFeedback: All Round 5 issues are cleanly resolved and independently verified: BED-LLM is confirmed ICLR 2026 (OpenReview ID: qyylZMLYT8), its LM-generic prior p_f(θ;∅) is correctly described, its multiple-choice format is noted, and its domain (latent preference vector inference, not item recommendation) is now correct. Stage 2a ground-truth operationalization is adequately specified. Four minor issues remain:\n\n**Fix 1 (1 sentence, related work):** Replace the TO-GATE description with: 'TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior.' The current phrasing ('DPO to clarifying question quality') understates the scope and would be caught by a TO-GATE-aware reviewer.\n\n**Fix 2 (1 paragraph, Stage 1):** Specify the disconfirmation probe generation prompt explicitly. Example: 'We instruct the LLM: generate K_neg hypotheses that are plausibly true of some user but LIKELY VIOLATED by the provided writing samples—stylistic attributes the demonstrations actively disconfirm. Example: if all samples use numbered lists, generate the probe \"User avoids numbered lists.\"' Without this, the mechanism is not reproducible and the novelty claim (that probes are genuinely falsifiable, not just low-confidence) is unverifiable.\n\n**Fix 3 (1 sentence, Stage 2a):** Add: 'If no τ satisfies ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent) and flag the failure in diagnostic analysis.' This closes the only remaining technical gap in the calibration procedure.\n\n**Fix 4 (1 sentence, human study description):** Replace 'substantially strengthens the EMNLP Main case' with 'provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas; the study is underpowered for statistical inference and results are reported descriptively.' This aligns the claim with the actual evidence and preempts the obvious reviewer objection.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE — Stage 2a circular self-evaluation: The Spearman ρ calibration analysis uses Qwen2.5-7B-Instruct both to (a) compute LLM log-likelihood scores score_i over demonstrations and (b) classify whether responses satisfy hypothesis h_i (for computing empirical accuracy). Since both quantities are derived from the same model, the correlation may reflect internal model consistency rather than genuine predictive validity over user preferences. Specifically, the model will tend to assign higher log-likelihoods to demonstration text that matches hypotheses it would also classify as satisfied—this is circular and could inflate ρ relative to its true value as a predictor of real user agreement. The paper should either: (a) acknowledge this as a stated limitation ('ρ is a model-consistency measure; real-user calibration is validated post-hoc via the Prolific study'), or (b) use a different model for the hypothesis satisfaction classification step (e.g., Llama 3.1-8B or a specialist NLI model) to break the circularity.\", \"MINOR — Human study framing residual overstatement: Despite correctly acknowledging the study is 'underpowered for statistical inference and results are reported descriptively,' the sentence continues 'which strengthens the EMNLP Main case relative to a purely simulated evaluation.' An underpowered descriptive study that cannot support statistical inference does not meaningfully strengthen the EMNLP Main case in the eyes of reviewing committees—it provides anecdotal, externally valid evidence but not a primary result. Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas but cannot substitute for a powered human study in Main review criteria.'\"]\nFeedback: Round 7 has cleanly resolved all four Round 6 issues: TO-GATE is correctly described as trajectory-level DPO, the disconfirmation probe prompt is explicitly specified with evidence-citing requirement, the τ→∞ fallback is added, and the human study is labeled underpowered. Independent verification confirms that arXiv 2602.15012 (the only unverified potential competitor) targets reasoning tasks with structured world model priors and does not overlap with FABEL's domain or mechanism. The core combination is genuinely novel and technically sound. Two targeted fixes are needed:\n\n**Fix 1 (Moderate, 2–3 sentences in Stage 2a): Break or acknowledge the circular self-evaluation.** The Spearman ρ calibration uses Qwen2.5-7B-Instruct for both log-likelihood scoring and hypothesis satisfaction classification — this creates an internal consistency artifact that may inflate ρ. Add: 'We note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences. To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis classifier, providing a cross-model calibration check.' Alternatively, acknowledge this limitation explicitly and defer cross-model validation to Phase 2.\n\n**Fix 2 (Minor, 1 clause): Remove the residual EMNLP Main overstatement.** Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas, reported descriptively.' This aligns with the already-correct statement that the study is underpowered.\n\nAfter these two fixes, the proposal has no remaining critical issues. The combination of demo-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel and appropriately scoped for EMNLP 2026 Findings. The MVP compute estimate (75h H100-equivalent) is confirmed within budget, and the PersonalLLM benchmark is publicly available.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"MODERATE — AdaptFuse (arXiv 2604.03925, April 2026) is uncited and directly adjacent: 'Training-Free Sequential Preference Learning via Externalized Bayesian Inference' maintains a Bayesian posterior over discrete hypothesis sets using a frozen LLM's semantic reasoning via entropy-adaptive fusion — it is in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL. FABEL's key differentiator (demo-conditioned warm prior + disconfirmation probes) holds, but AdaptFuse must be cited and differentiated in the landscape. A reviewer familiar with April 2026 arXiv would flag its absence immediately. Suggested addition to cluster (3) or a new cluster: 'AdaptFuse (2604.03925) uses externalized symbolic Bayesian inference over hypothesis sets with entropy-adaptive frozen-LLM fusion; FABEL differs by (1) initializing a user-specific demo-conditioned warm prior rather than cold-start symbolic updates, and (2) including mandatory disconfirmation probes absent from AdaptFuse.'\", \"MINOR — MAPLE (arXiv 2412.07207, AAAI 2025) is uncited. It uses LLM-modeled preference function distributions conditioned on natural language feedback with active query selection for general alignment — in the same broad space as FABEL's active Bayesian personalization. While MAPLE uses trajectory-level pairwise rankings (not binary hypothesis confirmation) and targets general alignment rather than response-style personalization, a one-sentence mention in landscape cluster (3b) or a new cluster is sufficient. Without it, the landscape is incomplete for AAAI 2025 active preference learning work.\"]\nFeedback: After seven rounds of thorough revision, this proposal is substantively close to publication-ready at EMNLP Findings level. All Round 7 issues are cleanly resolved: the self-consistency circularity in Stage 2a is addressed via the cross-model Llama-3.1-8B-Instruct calibration check with explicit fallback behavior; the human study overstatement is removed. Two remaining citation gaps must be closed:\n\n**Fix 1 (Moderate, 1 paragraph):** Cite AdaptFuse (arXiv 2604.03925, April 2026) as a concurrent member of the training-free Bayesian hypothesis-set inference family. Place it in landscape cluster (3) or a new cluster (6). Key differentiation: 'AdaptFuse maintains a symbolic Bayesian posterior over discrete hypotheses using entropy-adaptive fusion with a frozen LLM; FABEL extends this line with (1) user-specific demonstration-conditioned warm priors rather than cold symbolic initialization and (2) mandatory disconfirmation probes that AdaptFuse lacks.' This is the closest concurrent work and its absence would be flagged by area chairs familiar with April 2026 arXiv.\n\n**Fix 2 (Minor, 1-2 sentences):** Cite MAPLE (arXiv 2412.07207, AAAI 2025) in related work on active preference learning for LLMs. One sentence suffices: 'MAPLE (AAAI 2025) uses LLM-conditioned preference function modeling with active query selection for alignment tasks; FABEL differs in using binary hypothesis confirmation grounded in user demonstrations rather than trajectory-level pairwise ranking queries.' This closes the AAAI 2025 gap in the landscape.\n\nAfter these two fixes, there are no remaining critical gaps. The core novelty claim — demo-conditioned warm Bayesian prior + EIG binary confirmation + disconfirmation probes, in the LLM response-style personalization domain — is verified as absent from all cited and independently found prior work. The MVP compute (75h H100-equivalent) is confirmed within budget, PersonalLLM is publicly available, and the experimental design (warm vs. cold prior ablation + Stage 2a calibration with cross-model ρ check) is appropriate for EMNLP Findings.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:10:38.635Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:10:38.635Z",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

## Round 1

76 recorded events

### User

_source line 3 · 2026-05-10T08:10:38.675Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Human-Centered NLP and Human-AI Interaction. Aligns with EMNLP 2026 special theme on agentic workflows interfacing with human experiences.

Direction: Methods that improve how humans and NLP systems collaborate. In-scope: interactive learning from human feedback (beyond vanilla RLHF), human-in-the-loop annotation methods, calibrated uncertainty communication to users, adaptive explanation generation, collaborative writing/editing systems, preference elicitation, controllable generation with user intent.

Contribution type: METHOD ONLY. Must propose a concrete algorithm or system mechanism — not a user study alone. Method validated via user study or simulation is ideal.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. HCI-style work is often light on compute, heavier on design and evaluation.
2. Time: ≤16 days. Use existing open models + lightweight adaptation. If user study needed, design a small-scale simulated or crowdsourced protocol.
3. Eval: task-specific metrics + human evaluation (inter-annotator agreement, preference rates, task completion time). Simulated user evaluation acceptable for ARR submission.

Look for: adaptive interaction patterns, uncertainty-aware response generation, methods for user preference learning with minimal feedback, controllable generation beyond simple instruction following.

Tag: direction=human_ai_interaction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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
  "title": "Demonstration-Grounded Warm-Start Hypothesis Elicitation for LLM Personalization via Binary Confirmation",
  "core_problem": "Personalizing LLMs to individual users requires efficient preference elicitation from few-shot demonstrations. Current methods exhibit four distinct failure modes: (1) Demonstration-grounded hypothesis methods (HyPerAlign) infer rich preference attributes from user examples but skip validation, risking hallucination and echo-chamber failure; (2) The BOED-for-preference-elicitation line—established by OPEN (arXiv 2403.05534, ACL 2024) and extended by BED-LLM (arXiv 2508.21184, ICLR 2026)—applies principled EIG-based adaptive questioning but initializes without user-specific demonstration-conditioned priors: OPEN uses LM-ranked feature importances as a domain-generic prior (not conditioned on any specific user's outputs); BED-LLM starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations—which is also not informed by available user examples; both waste elicitation turns on hypotheses that available user demonstrations already resolve; (3) Iterative preference inference from writing samples (PROSE, ICML 2025) refines free-form preference descriptions with component-level verification but involves no user interaction and no formal Bayesian posterior—it cannot adaptively resolve ambiguous hypotheses that demonstrations alone are insufficient to distinguish. Additionally, arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs exhibit systematic confirmation bias in hypothesis testing (42% baseline success rate), meaning LLM-generated hypothesis sets may be preferentially confirmable rather than genuinely falsifiable, causing Bayesian posteriors to converge spuriously on echo-chamber preference profiles. (4) A concurrent approach, AdaptFuse (arXiv 2604.03925, April 2026), externalizes a symbolic Bayesian posterior over pre-defined discrete hypotheses using entropy-adaptive fusion with a frozen LLM, but initializes uniformly (no demo-conditioned warm start), uses fixed sequential query rounds without EIG-based active selection, and lacks disconfirmation probes. No existing method—including AdaptFuse—combines user-demonstration-conditioned warm-start Bayesian priors, EIG-based binary confirmation, and explicit disconfirmation-probe auditing in the LLM response-style personalization domain.",
  "opportunity": "The BOED-for-preference-elicitation lineage was established by OPEN (arXiv 2403.05534, ACL 2024), which combined EIG-based query selection with LM feature extraction over pairwise item comparisons in content recommendation—but initializes from LM-ranked feature importances (a domain-generic warm start reflecting general knowledge about what features matter for news article preferences, not this user's actual examples). BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets with a Rao-Blackwellized EIG estimator and an LM-generic prior initialization p_f(θ;∅), evaluating on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions, demonstrating that EIG-based sequential Bayesian elicitation substantially outperforms prompt-only baselines. Neither OPEN nor BED-LLM exploits K specific examples of a target user's actual outputs: their initializations duplicate information that demonstrations already encode, wasting early elicitation turns. AMPLe (arXiv 2411.00524, ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation, but also cold-starts from pairwise item comparisons rather than user demonstrations and lacks disconfirmation probes. HyPerAlign (arXiv 2505.00038, May 2025) showed demonstration-grounded hypotheses yield >90% win rates but explicitly omits user validation. PROSE (arXiv 2505.23815, ICML 2025) achieves 33% improvement over CIPHER on writing-style tasks via iterative preference refinement from demonstrations, but operates entirely without user interaction—it cannot distinguish two hypotheses with similar demonstration-level support, and provides no mechanism to surface or mitigate confirmation bias. AdaptFuse (arXiv 2604.03925, April 2026) is a concurrent work in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL. It externalizes a symbolic Bayesian posterior initialized uniformly (b₀,m = 1/M) and combines it with a frozen LLM's multi-sample Dirichlet aggregation via entropy-adaptive fusion; importantly, its entropy-adaptive fusion is a signal-weighting mechanism, not an EIG-based query selection criterion—queries are presented in fixed sequential rounds (T=5) rather than adaptively selected. AdaptFuse's hypothesis set consists of pre-defined linear utility functions over scalar attributes from a training-split lookup table, not free-form LLM-generated stylistic attributes. Evaluated on recommendation (flight, hotel, web shopping), not LLM response-style personalization. FABEL's three-way differentiation from AdaptFuse: (1) user-specific demo-conditioned temperature-scaled warm prior vs. AdaptFuse's uniform cold start—the same warm-start gap that separates FABEL from BED-LLM and OPEN; (2) EIG-based active query selection absent from AdaptFuse's fixed protocol; (3) mandatory disconfirmation probes absent from AdaptFuse. The unaddressed gap is the warm-start interactive regime: when K demonstrations are available, initializing the Bayesian prior from user-specific demonstration-conditioned LLM likelihoods—calibrated via temperature scaling to avoid overconfident prior collapse—should dramatically reduce required elicitation turns compared to both OPEN and BED-LLM (testable claim), while the interactive EIG confirmation phase resolves the residual ambiguity that passive methods like PROSE cannot address (complementary claim). A second gap concerns confirmation bias: an elicitation system that does not deliberately seed disconfirmation probes in the hypothesis pool risks producing preference profiles that reflect what an LLM expects a user to prefer rather than what the user actually prefers—an echo-chamber failure mode that HyPerAlign acknowledges but does not address, and that PROSE's component-verification step partially mitigates without fully resolving. The specific combination absent from all prior work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, PROSE's non-interactive refinement, and AdaptFuse's training-free externalized Bayesian inference with uniform cold-start and fixed sequential queries.",
  "landscape": "The preference elicitation and personalization landscape includes nine relevant clusters. (1) Demonstration-grounded, no validation: HyPerAlign (arXiv 2505.00038, ICLR 2025 workshop) generates falsifiable-in-principle preference hypotheses from demonstrations and injects them as system prompts without user confirmation. (2) Iterative preference inference from writing samples, no interaction: PROSE (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) iteratively refines free-form preference descriptions from user writing samples via a generate→compare→update loop, then verifies preference components against held-out demonstrations with component-level scoring; achieves 33% improvement over CIPHER baseline on summarization and email writing tasks across Qwen2.5-7B/72B and GPT-4o variants; no user interaction beyond initial writing samples, no Bayesian posterior over hypotheses, no disconfirmation mechanism—the key differentiator from FABEL is that PROSE cannot adaptively resolve ambiguity beyond what demonstrations already encode and has no principled update when demonstrations are insufficient to distinguish competing hypotheses; must be included as a baseline (directly competitive with FABEL Stage 1) and explicitly differentiated. (3) The BOED-for-preference-elicitation lineage: OPEN (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) established this line by combining EIG-based query selection with LM feature extraction for content recommendation—selects pairwise queries over binary feature vectors (|F|=10, e.g., 'discusses science') using a particle-filter Bayesian update with Bradley-Terry preference model; prior initialization is via LM-ranked feature importances (domain-generic: w_i = 1.2 − 0.12i for rank i), NOT conditioned on any specific user's demonstrations; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism. BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets: samples N=15 hypotheses per turn, selects questions via Rao-Blackwellized EIG estimator (~45–50 LLM calls/step), rejection-sampling Bayesian posterior update; starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations (and notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions (a technical requirement: having a small space of single-token responses ensures p_LLM provides meaningful uncertainty over outcomes for EIG estimation); evaluates on latent preference vector inference via movie-preference multiple-choice queries and the 20-Questions game; no public code. Active Task Disambiguation (arXiv 2502.04485, ICLR 2025) similarly applies Bayesian experimental design for clarifying question selection on under-specified tasks. FABEL extends beyond all three works: (i) user-specific demonstration-conditioned warm start (K=5–10 demos from THIS user, vs. OPEN's domain-generic LM-ranked feature importances and BED-LLM's demo-agnostic LM-generic prior p_f(θ;∅)), (ii) temperature-scaled prior calibration to prevent overconfident prior collapse, (iii) binary yes/no natural-language hypothesis confirmation over free-form response-style attributes (vs. OPEN's pairwise item comparisons and BED-LLM's multiple-choice format—FABEL's binary format reduces cognitive load while remaining viable because hypothesis confirmation questions are naturally binary in ways that preference inference over open hypothesis spaces is not), (iv) mandatory disconfirmation probes in the EIG pool (absent from all prior BOED-for-preference work), (v) application to LLM response-style personalization (format, tone, structure)—a domain shift from BED-LLM's latent preference vector inference. (3b) Comparison-based active preference learning for LLM personalization: AMPLe (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) personalizes LLM outputs to implicit multi-dimensional preferences via pairwise comparison queries, a modified Bayesian posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection. AMPLe is directly adjacent to FABEL in the active Bayesian personalization space but differs in three critical ways: (1) AMPLe cold-starts from pairwise item comparisons rather than initializing from user demonstrations; (2) AMPLe asks 'which response do you prefer?' (item comparison) rather than 'does this stylistic hypothesis apply to you?' (hypothesis confirmation); (3) AMPLe includes no disconfirmation probe mechanism. AMPLe must be cited as an ACL 2025 active Bayesian personalization baseline; its comparison-based query design and FABEL's hypothesis-confirmation design represent complementary elicitation paradigms. MAPLE (arXiv 2412.07207, AAAI 2025, Mahmud, Nakamura, Zilberstein) uses LLM-conditioned preference function distributions with a language-conditioned active query selection mechanism over pairwise trajectory rankings, targeting general alignment tasks including vehicle routing and web navigation; in the same broad active Bayesian preference learning space as FABEL but differs: (1) pairwise trajectory rankings rather than binary yes/no stylistic hypothesis confirmation grounded in user demonstrations; (2) no warm prior from user demonstrations; (3) general RL alignment domain rather than LLM response-style personalization—cited as AAAI 2025 active preference learning context. (3c) Training-free externalized Bayesian hypothesis inference (concurrent): AdaptFuse (arXiv 2604.03925, April 2026, Lin, Li, Xing, Yang, Ge, Yamada, Zhang, Zhang, Tu) externalizes Bayesian inference from the LLM: a symbolic module maintains a Bayesian posterior over a discrete hypothesis set initialized uniformly (b₀,m = 1/M), updated via Bayes' rule with a Luce choice model likelihood; a frozen LLM contributes semantic reasoning via multi-sample Dirichlet aggregation; entropy-adaptive fusion automatically weights the symbolic posterior vs. LLM signal by predictive confidence, shifting reliance toward the symbolic module as evidence accumulates. The hypothesis set consists of pre-defined linear utility functions over scalar attributes drawn from a training-split lookup table—not free-form LLM-generated natural language stylistic attributes. Queries are presented in fixed sequential rounds (T=5); entropy-adaptive fusion is a signal-weighting mechanism, not a query selection criterion—there is no EIG-based active selection. Evaluated on recommendation domains (flight, hotel, web shopping) across Gemma 2 9B, Llama 3 8B, and Qwen 2.5 7B; outperforms prompting baselines and fine-tuned Bayesian Teaching models without any weight updates. FABEL extends AdaptFuse in four ways: (1) user-specific demo-conditioned temperature-scaled warm prior rather than uniform cold-start (b₀,m = 1/M); (2) EIG-based active query selection absent from AdaptFuse's fixed sequential protocol; (3) free-form LLM-generated natural language stylistic hypotheses rather than pre-defined scalar utility functions from a training split; (4) mandatory disconfirmation probes and soft quota preventing silent suppression of falsifying evidence. AdaptFuse must be acknowledged as a concurrent work sharing the 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' framing; its absence would be flagged by area chairs familiar with April 2026 arXiv. (4) Generative open-ended elicitation: GATE (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) uses free-form LLM-generated questions in three domains; its binary yes/no variant reduces cognitive load but underperforms the open-ended variant because binary questions without a Bayesian posterior cannot adaptively narrow the hypothesis space—GATE's binary variant also does not ground questions in user demonstrations. (5) Trajectory-optimized clarification: TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior. (6) Bayesian-RL hybrid: PEBOL (arXiv 2405.00981, RecSys 2024) combines NLI-based preference beliefs with Thompson Sampling in recommendation. (7) Bayesian in-context conditioning from demonstrations (adjacent): Variational In-Context Reward Modeling / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) casts reward modeling as amortized variational inference over a latent preference with a conjugate Beta prior conditioned on in-context preference demonstrations at test time without retraining—conceptually adjacent to FABEL's warm-start initialization from demonstrations but differs in three critical ways: domain (pairwise scalar reward modeling vs. interactive response-style personalization), hypothesis representation (continuous Beta prior on scalar rewards vs. discrete binary preference hypotheses), and interaction mode (passive in-context update vs. active EIG confirmation loop); no disconfirmation probes; acknowledged in related work to pre-empt warm-start novelty challenge. (8) Few-shot preference optimization: FSPO (arXiv 2502.19312, 2025) meta-learns personalization from few-shot preference data; deferred to Phase 2 due to meta-training infrastructure overhead. The specific combination absent from all prior and concurrent work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, PROSE's non-interactive refinement, and AdaptFuse's training-free externalized Bayesian inference with uniform cold-start, fixed sequential queries, and pre-defined utility function hypotheses.",
  "approach": "We propose FABEL (Falsification-Aligned Binary Elicitation Loop), a tuning-free framework operating in four stages. The EMNLP 2026 submission is scoped as an MVP: PersonalLLM benchmark, four baselines, one LLM backbone (Qwen2.5-7B-Instruct), one core ablation, and a small crowdsourced human evaluation (n≈20) to strengthen the EMNLP Main case.\n\nStage 1—Demonstration-Grounded Hypothesis Generation with Disconfirmation Probes: Given K=5–10 few-shot user output demonstrations, a frontier open-source LLM (Qwen2.5-7B-Instruct) generates N_pos=12–15 falsifiable, binary-verifiable preference hypotheses (e.g., 'User prefers bulleted structure over prose') AND K_neg=4–6 explicit disconfirmation probes—hypotheses deliberately constructed to be easily falsifiable given the demonstrations (e.g., 'User avoids technical terminology' when demonstrations frequently use it). This two-class design, motivated by arXiv 2604.02485's finding that LLMs default to generating confirmable hypotheses, ensures the EIG pool contains falsifying evidence. To elicit genuinely falsifiable probes rather than merely low-confidence confirmatory hypotheses (the LLM default per arXiv 2604.02485), we use a dedicated generation prompt distinct from the confirmatory hypothesis prompt: 'Given these K writing samples, generate K_neg stylistic hypotheses that are plausibly true of some users but are ACTIVELY VIOLATED by the provided samples—attributes the demonstrations explicitly disconfirm. For each probe, cite the specific demonstration evidence that falsifies it. Example: if all samples use numbered lists, generate the probe \"User avoids numbered lists\" and cite the list usage as falsifying evidence.' The evidence-citing requirement prevents the model from producing vacuously non-committal probes and ensures each H_neg hypothesis is verifiably falsifiable against the provided demonstrations.\n\nStage 2—Temperature-Scaled Warm Prior Initialization with Calibration Check: Each hypothesis posterior is initialized as p(h_i = true | demos) ∝ exp(score_i / τ), where score_i is the LLM log-likelihood of the K demonstrations given hypothesis h_i, and τ is a temperature hyperparameter controlling prior sharpness. Raw LLM log-likelihoods are typically overconfident (τ=1); τ is selected on a held-out 50-user PersonalLLM dev split as the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6 (validation threshold). If no τ in the search grid achieves ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent, equivalent to a cold start) and flag this as a calibration failure in diagnostic analysis—indicating that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for the evaluated hypothesis class. τ→∞ recovers a uniform prior (a maximally uninformative cold start, distinct from BED-LLM's LM-generic prior p_f(θ;∅), which reflects the LLM's own unconditional distribution over hypotheses and is neither uniform nor user-specific); τ=1 applies raw likelihoods. This design directly addresses LLM miscalibration: it ensures the warm start concentrates mass on demonstration-consistent hypotheses while avoiding premature posterior collapse onto incorrect hypotheses. The calibration analysis—Stage 2a in the paper—reports Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users, validating the warm-start assumption empirically and providing a lightweight check that does not require additional model training. Empirical hypothesis accuracy is operationalized as follows: for each simulated PersonalLLM dev user u (a weighted ensemble of 10 reward models with Dirichlet-sampled weights) and each hypothesis h_i, empirical accuracy = fraction of u's top-quartile responses (by u's weighted-ensemble reward score across the 8 candidate responses per prompt) that satisfy h_i, as assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i. Spearman ρ is then computed between the vector of LLM log-likelihood scores [score_1, …, score_N] and the vector of empirical accuracies [acc_1, …, acc_N] across all N hypotheses, averaged over the 50 dev users. This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.\n\nWe note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences—a limitation consistent with documented self-preference bias in LLM-as-judge evaluation (arXiv 2601.20913). To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis satisfaction classifier (cross-model calibration check); if ρ remains above 0.6 under cross-model evaluation, the warm-start assumption is validated against self-consistency inflation. If cross-model ρ falls below 0.6 while same-model ρ exceeds it, we treat this as evidence of self-consistency inflation and default to the uniform prior (τ→∞) in the main experiments, flagging the discrepancy as a stated limitation. If both same-model and cross-model ρ fall below 0.6, we acknowledge that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for this hypothesis class and defer warm-start calibration to Phase 2.\n\nStage 3—EIG-Based Binary Elicitation Loop with Disconfirmation Quota (algorithm specification): The full hypothesis set H = H_pos ∪ H_neg is placed in a single EIG-ranked pool. At each turn, FABEL selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2 — and poses it as a binary yes/no confirmation. The posterior updates via Bayes' rule with a noise term calibrated on held-out demo pairs. We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization H(p(h_i)) is equivalent to EIG-based selection. The loop terminates when joint preference entropy drops below threshold θ (empirically 3–5 turns).\n\nDisconfirmation probe handling follows option (a)—probes are included in the EIG pool and selected by EIG only when maximally uncertain. This is algorithmically cleanest: EIG without H_neg would face a pool containing only confirmatory hypotheses, creating a structural selection bias toward echo-chamber convergence regardless of EIG's own informativeness criterion. Including H_neg in the pool makes the probe design a prior-shaping device rather than a scheduling override—EIG's entropy criterion then serves as a bidirectional diagnostic. If H_neg probes are never selected (prior already confidently classifies them as false), this is evidence of good prior calibration; if frequently selected (probes have high posterior entropy at elicitation start), this signals prior miscalibration requiring attention.\n\nSoft minimum quota: To prevent the degenerate case where warm-start prior overconfidence silently suppresses all falsifying questions, at least ⌈K_neg / 3⌉ disconfirmation probes must be asked if the loop runs ≥3 turns. Quota-forced questions bypass EIG ordering for their designated turn but receive normal Bayesian updates. The 'disconfirmation selection rate'—fraction of turns where EIG (prior to quota enforcement) would have selected a H_neg hypothesis—is reported as a diagnostic distinguishing well-calibrated priors (low rate: probes already resolved by warm start) from miscalibrated ones (high rate: probes still maximally uncertain at elicitation start). The falsification rate—fraction of posterior updates that decrease hypothesis probability—is reported as a secondary diagnostic.\n\nStage 4—Personalized Generation: The confirmed/disconfirmed hypothesis set is injected as a structured system prompt without fine-tuning.\n\nMVP Experimental Design (EMNLP 2026 ARR deadline May 25, 2026):\n- Benchmark: PersonalLLM (ICLR 2025), using its reward-model-based simulated user evaluation infrastructure (public dataset: HuggingFace namkoong-lab/PersonalLLM); simulated evaluation eliminates GPT-4-judge latency and cost, enabling full experimental sweep within the 15-day window\n- Human evaluation study (EMNLP Main strengthening, optional stretch): n≈20 crowdsourced participants via Prolific; each participant interacts with FABEL over 10 PersonalLLM prompts and evaluates personalized vs. baseline responses; setup requires ~1 agent-day (days 3–4, running in parallel with automated experiments); cost ~$100–200; the study is underpowered for statistical inference and results are reported descriptively—it provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas, reported descriptively\n- Backbone: Qwen2.5-7B-Instruct (single backbone for all methods)\n- Baselines (4): (1) HyPerAlign—demonstration-grounded, no validation; (2) GATE binary—binary questions, no Bayesian posterior, no demonstration grounding; (3) PROSE—iterative preference inference from demonstrations, no user interaction, no Bayesian posterior; applied by running PROSE's generate→compare→update pipeline on PersonalLLM demonstrations, evaluating via reward model; (4) BED-LLM—LM-generic-prior EIG Bayesian with multiple-choice questions; reimplemented from paper description (no public code; Rao-Blackwellized EIG estimator + rejection-sampling update, ~45–50 LLM calls/step); time-boxed to 3–4 agent-days with fallback to 'BED-LLM-approx' (entropy-based selection + rejection-sampling, no full RB-EIG) if faithful replication is infeasible, with explicit labeling\n- Core ablation (1): warm-start prior (τ-scaled from demos) vs. uniform prior (τ→∞), directly isolating the demonstration-grounded initialization contribution\n- Primary metrics: PersonalLLM reward-model win rates (main); average elicitation turns (efficiency); disconfirmation selection rate + falsification rate (diagnostics); human preference rates if study included; same-model vs. cross-model Spearman ρ (Stage 2a calibration circularity diagnostic)\n- Phase 2 extensions (camera-ready / full paper): LaMP-4/6/7 text generation benchmarks; AMPLe and FSPO baselines; full ablation battery (probes included vs. excluded; EIG vs. random ordering; K sensitivity N∈{3,5,10}; τ sensitivity; full BED-LLM replication verification); additional backbone (Qwen2.5-14B-Instruct or Llama 4 Maverick)",
  "resource_estimate": {
    "auto_research": {
      "description": "EMNLP 2026 MVP — PRIMARY mode",
      "gpu_hours": "~150h A100 (MVP: PersonalLLM only, 4 baselines, 1 backbone, 1 ablation)",
      "h100_equivalent": "~75h H100-equivalent (at 2× A100/H100 throughput ratio) — explicitly within the ≤200 H100-hour hard constraint",
      "gpu_utilization": "High (~85–90%): agent continuously queues inference jobs with no human wait time; primary idle periods are inter-job I/O and BED-LLM implementation phase",
      "timeline": "12–14 days with 2× A100s running in parallel; Prolific human study set up days 3–4 in parallel, adding <1 agent-day overhead; cross-model ρ check (Llama-3.1-8B as hypothesis classifier) adds ~0.25 agent-days to Stage 2a",
      "team": "0 (3–5h initial setup)",
      "claude_api_cost": "$150–250 (~1,500–2,500 agent reasoning turns)",
      "estimated_gpu_cost": "$300–450 at ~$2–3/hr A100 rental",
      "human_study_cost": "~$100–200 (n≈20 Prolific participants at ~$5–10/participant; set up in parallel days 3–4)",
      "cost_notes": "PersonalLLM reward-model evaluation (simulated) eliminates GPT-4-judge cost; total project cost $550–900 including optional human study; Phase 2 adds ~$400–600 GPU and ~$150–300 GPT-4-judge for LaMP tasks",
      "speed_bottleneck": "BED-LLM EIG reimplementation (no public code; time-boxed 3–4 agent-days with simplified fallback); PROSE implementation straightforward (~1 agent-day, purely prompt-based); Stage 2a calibration analysis (same-model + cross-model ρ) adds ~0.75 agent-days total",
      "compliance_note": "150h A100 ÷ 2 (H100/A100 throughput ratio) = 75h H100-equivalent, well within the 200 H100-hour limit"
    },
    "human_in_loop": {
      "description": "Full paper (post-EMNLP, adds LaMP + full ablations)",
      "gpu_hours": "~300h A100",
      "gpu_utilization": "Moderate (~50–60%): agent continuously queues inference jobs between human approval gates; BED-LLM replication verified at first review gate before full baseline run",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$150–250 (~1,200–2,000 reasoning turns)",
      "estimated_gpu_cost": "$600–900",
      "risk_note": "Warm-start prior calibration (Spearman ρ threshold) must be validated on PersonalLLM dev split before committing to full experimental sweep; both same-model and cross-model ρ confirmed at a dedicated calibration gate before main experimental sweep; τ selection and BED-LLM replication fidelity confirmed at dedicated review gates"
    },
    "manual": {
      "description": "Full paper (post-EMNLP, adds LaMP + full ablations)",
      "gpu_hours": "~200h A100",
      "gpu_utilization": "Low (~20–30%): GPU idles while researchers implement BED-LLM baseline, write pipeline code, and analyze results",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "$400–600 at ~$2–3/hr A100 rental",
      "cost_notes": "GPT-4-as-judge for LaMP evaluation adds ~$150–300; total project cost $550–900"
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings via ACL ARR (deadline May 25, 2026 — 15 days from project start May 10, 2026) — PRIMARY realistic target; MVP scope (PersonalLLM, 4 baselines, 1 backbone, 1 ablation + Stage 2a calibration analysis with cross-model ρ check) is credible for EMNLP Findings; adding the n≈20 Prolific human study puts EMNLP Main within reach if human results are positive — this is the stretch Main goal, not the base expectation; targets EMNLP 2026 Findings as the primary submission outcome",
    "ICLR 2027 (expected submission deadline ~October 2026) — SECONDARY target if EMNLP 2026 submission scope is insufficient or if full paper (LaMP + full ablation battery) is preferred; strongest venue fit given GATE (ICLR 2025), OPEN (ACL 2024), and BED-LLM (ICLR 2026) lineage; full paper with multi-benchmark and human study comfortably meets Main bar",
    "AAAI 2027 (expected abstract/paper deadline ~August–September 2026) — TERTIARY target with sufficient runway for full experimental sweep including LaMP benchmarks and multiple backbone ablations"
  ],
  "level": "solid",
  "key_references": [
    "OPEN: Bayesian Preference Elicitation with Language Models (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) — foundational BOED-for-preference-elicitation work; combines EIG-based query selection with LM feature extraction for content recommendation; selects pairwise queries over binary feature vectors (|F|=10) using particle-filter Bayesian update with Bradley-Terry model; prior initialization via LM-ranked feature importances (domain-generic warm start: w_i = 1.2 − 0.12i for rank i), NOT user-demonstration-conditioned; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-specific demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism; cite as the foundation of the BOED-for-preference-elicitation line that BED-LLM extends and FABEL further advances",
    "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design (arXiv 2508.21184, ICLR 2026) — extends OPEN to discrete language hypothesis sets; initializes from an LM-generic prior p_f(θ;∅) (the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations; notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions as a technical requirement (small single-token response spaces ensure p_LLM provides meaningful uncertainty for EIG estimation); EIG uses Rao-Blackwellized N=15-sample estimator + rejection-sampling posterior update (~45–50 LLM calls/turn); evaluates on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions game; no public code; reimplementation time-boxed to 3–4 agent-days with simplified fallback; FABEL differentiates in three ways: (1) prior conditioned on this user's K demonstrations vs. BED-LLM's demo-agnostic LM prior; (2) binary yes/no confirmation vs. BED-LLM's multiple-choice format; (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work",
    "AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference (arXiv 2604.03925, April 2026, Lin, Li, Xing, Yang, Ge, Yamada, Zhang, Zhang, Tu) — concurrent work in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL; externalizes Bayesian inference from the LLM: a symbolic module maintains a posterior initialized uniformly (b₀,m = 1/M), updated via Bayes' rule with a Luce choice model likelihood; a frozen LLM contributes via multi-sample Dirichlet aggregation; entropy-adaptive fusion weights symbolic vs. LLM signal by predictive confidence—entropy-adaptive fusion is a signal-weighting mechanism, not a query selection criterion; queries presented in fixed sequential rounds (T=5), no EIG-based active selection; hypothesis set = pre-defined linear utility functions over scalar attributes from training-split lookup table, not free-form natural language stylistic attributes; evaluated on recommendation (flight, hotel, web shopping), not LLM response-style personalization; FABEL's four-way differentiation: (1) user-specific demo-conditioned temperature-scaled warm prior vs. AdaptFuse's uniform cold-start; (2) EIG-based active query selection vs. AdaptFuse's fixed sequential protocol; (3) free-form LLM-generated natural language stylistic hypotheses vs. AdaptFuse's pre-defined scalar utility functions; (4) mandatory disconfirmation probes absent from AdaptFuse; acknowledge as concurrent work in landscape cluster (3c)",
    "AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) — active Bayesian preference learning for LLM personalization; pairwise comparison queries over LLM responses, modified posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection to minimize required comparisons; directly adjacent to FABEL's active Bayesian personalization setting; FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary stylistic hypothesis confirmation rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe; include as related work in landscape cluster (3b); include as Phase 2 baseline on LaMP tasks",
    "MAPLE: A Framework for Active Preference Learning Guided by Large Language Models (arXiv 2412.07207, AAAI 2025, Mahmud, Nakamura, Zilberstein) — uses LLM-conditioned preference function distributions with a language-conditioned active query selection mechanism over pairwise trajectory rankings for general alignment tasks (vehicle routing, web navigation); in the same broad active Bayesian preference learning space as FABEL; FABEL differs: (1) binary yes/no stylistic hypothesis confirmation grounded in user demonstrations rather than trajectory-level pairwise rankings; (2) user-specific demo-conditioned warm prior absent from MAPLE; (3) LLM response-style personalization domain rather than RL alignment; cite as AAAI 2025 active preference learning context in landscape cluster (3b)",
    "PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) — directly competitive with FABEL Stage 1; iterative generate→compare→update refinement of free-form preference descriptions + component-level verification against held-out samples; 33% improvement over CIPHER on summarization/email; no user interaction, no Bayesian posterior, no disconfirmation mechanism; baseline and key differentiator",
    "GATE: Eliciting Human Preferences with Language Models (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) — binary yes/no variant underperforms open-ended due to absence of Bayesian posterior; baseline",
    "HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation (arXiv 2505.00038, May 2025) — demonstration-grounded hypothesis generation without user validation; baseline",
    "Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing (arXiv 2604.02485, April 2026) — motivates disconfirmation probe design; 42%→56% rule-discovery success with counter-example prompting; motivates H_neg pool inclusion in FABEL Stage 3",
    "Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) — amortized variational inference with conjugate Beta prior conditioned on in-context preference demonstrations; conceptually adjacent to FABEL's warm-start but differs in domain (pairwise reward modeling vs. interactive style elicitation), representation (Beta prior on scalar rewards vs. binary hypothesis set), and interaction mode (passive vs. active EIG confirmation); acknowledge in related work to pre-empt warm-start novelty challenge",
    "Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (arXiv 2601.20913, 2026) — provides hypothesis testing framework for cross-model evaluation with calibrated confidence metrics; cited to motivate FABEL's cross-model ρ check (using Llama-3.1-8B-Instruct as hypothesis classifier to bound the self-consistency inflation artifact in Stage 2a)",
    "Active Task Disambiguation with LLMs (arXiv 2502.04485, ICLR 2025) — BED applied to task clarification; related but not personalization-focused",
    "TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization (arXiv 2506.02827, 2025) — applies trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline (a clarification resolver generating optimal questioning trajectories plus a summarizer for task-aligned responses); remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior; achieves 9.32% improvement over STaR-GATE on preference elicitation tasks; cited as an open-ended, non-Bayesian clarification baseline in landscape cluster (5)",
    "PEBOL: Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation (arXiv 2405.00981, RecSys 2024) — NLI + Bayesian BO for recommendation; related",
    "Asking Clarifying Questions for Preference Elicitation With Large Language Models (arXiv 2510.12015, 2025) — diffusion-inspired clarifying question model; distinct from PEBOL",
    "FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users (arXiv 2502.19312, 2025) — deferred to Phase 2 / full paper; requires meta-learned model setup adds ~1–2 weeks engineering overhead",
    "PersonalLLM: Tailoring LLMs to Individual Preferences (ICLR 2025) — primary benchmark; public dataset HuggingFace namkoong-lab/PersonalLLM (9,402 train / 1,000 test prompt-response pairs, 8 candidate responses per prompt scored by 10 reward models, simulated users as Dirichlet-weighted reward model ensembles); reward-model-based simulated evaluation eliminates GPT-4-judge dependency and enables 15-day timeline",
    "LaMP: When Large Language Models Meet Personalization (ACL 2024) — secondary benchmark for Phase 2; LaMP-4/6/7 text generation tasks assess format and style personalization",
    "Calibrating Language Models with Adaptive Temperature Scaling (arXiv 2409.19817, EMNLP 2024) — post-hoc temperature calibration method for LLM token probabilities without fine-tuning; informs FABEL's τ-scaled warm prior design: p(h_i) ∝ exp(score_i / τ) with τ selected via dev-set rank-correlation criterion"
  ],
  "description": "Personalizing LLMs to individual users is hindered by four complementary failure modes: HyPerAlign generates demonstration-grounded preference hypotheses but skips user validation; the BOED-for-preference-elicitation line—established by OPEN (ACL 2024) and extended by BED-LLM (ICLR 2026)—applies principled EIG-based Bayesian elicitation but lacks user-specific demonstration-conditioned priors (OPEN uses domain-generic LM-ranked feature importances; BED-LLM uses an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution, not conditioned on any specific user's demonstrations); PROSE (ICML 2025) iteratively refines free-form preference descriptions from writing samples but has no user interaction and no formal Bayesian posterior, leaving ambiguous hypotheses unresolved; and AdaptFuse (arXiv 2604.03925, April 2026), a concurrent work, externalizes a symbolic Bayesian posterior over pre-defined discrete hypotheses with entropy-adaptive frozen-LLM fusion—in the same training-free Bayesian hypothesis-set inference family as FABEL—but initializes from a uniform prior (not user-demonstration-conditioned), uses fixed sequential query rounds (T=5) rather than EIG-based active selection, and lacks disconfirmation probes. AMPLe (ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation but also cold-starts from pairwise comparisons and lacks disconfirmation probes. We propose FABEL (Falsification-Aligned Binary Elicitation Loop), which extends the OPEN→BED-LLM BOED lineage by (1) initializing a temperature-scaled warm Bayesian prior p(h_i) ∝ exp(score_i / τ) from K=5–10 user-specific demonstrations—user-specific rather than domain-generic or demo-agnostic; (2) including K_neg=4–6 explicit disconfirmation probes in the EIG-ranked hypothesis pool, generated via a dedicated falsification prompt that requires citing demonstration-level evidence for each probe, making the probe design a prior-shaping device that ensures EIG always has access to genuinely falsifying evidence; (3) applying a soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns) to prevent warm-start overconfidence from silently suppressing falsifying questions; (4) applying a factored posterior approximation with EIG-based binary yes/no confirmation (vs. BED-LLM's multiple-choice format, which is required for reliable LLM uncertainty quantification but increases cognitive load) to resolve remaining uncertainty in 3–5 turns; and (5) explicitly acknowledging that under the factored (independent) posterior approximation, marginal entropy maximization is equivalent to EIG-based selection. Stage 2a includes a calibration analysis (Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy on 50 PersonalLLM dev users, where empirical accuracy is operationalized as the fraction of each simulated user's top-quartile reward-model responses satisfying each hypothesis) that validates the warm-start assumption and selects τ; if no τ achieves ρ > 0.6, the system defaults to a uniform prior and flags the calibration failure. Critically, Stage 2a also addresses a circularity in this operationalization—the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and accuracy labels—by additionally reporting ρ using Llama-3.1-8B-Instruct as an independent hypothesis classifier (cross-model calibration check; arXiv 2601.20913); if cross-model ρ falls below 0.6 while same-model ρ exceeds it, the system defaults to the uniform prior, treating the discrepancy as evidence of self-consistency inflation. The EMNLP 2026 MVP targets Findings as the primary outcome, with an optional n≈20 Prolific human study (days 3–4, ~$100–200) that is underpowered for statistical inference and reported descriptively—providing preliminary external validity evidence beyond simulated personas, reported descriptively. The central testable claim: demonstration-grounded user-specific warm priors reduce required elicitation turns vs. both OPEN (domain-generic warm start) and BED-LLM (demo-agnostic LM prior) while achieving higher personalization win rates than non-interactive methods (PROSE, HyPerAlign). LaMP benchmarks, AMPLe/FSPO baselines, and full ablations are deferred to Phase 2.",
  "project_name": "falsif_guided_pe",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["BED-LLM (arXiv 2508.21184, ICLR 2026) is unacknowledged and directly covers the core mechanism: it samples N=15 hypotheses, uses EIG to select questions designed to 'slice the hypothesis pool into roughly balanced subsets,' and applies Bayesian rejection-sampling updates — the central algorithmic contribution of FABEL. The paper must be cited and clearly differentiated.", "GATE (ICLR 2025) already includes a yes-or-no binary question variant ('restricts the LM to generating binary yes-or-no questions'). The generator's landscape description characterizes GATE as purely open-ended, which is factually incomplete. The binary format alone is not a differentiating contribution.", "PEBOL arXiv attribution error: the generator cites '(arXiv 2510.12015)' as the PEBOL paper, but arXiv 2510.12015 is 'Asking Clarifying Questions for Preference Elicitation With Large Language Models' (a diffusion-inspired model, not PEBOL). The actual PEBOL paper is arXiv 2405.00981 (RecSys 2024). This is a citable factual error that would immediately surface in peer review.", "Venue deadline is misidentified: the generator claims 'ACL ARR June 2026 cycle, deadline ~June 15 2026' but the confirmed EMNLP 2026 ARR submission deadline is May 25, 2026 (per official EMNLP 2026 CFP and ACL ARR Dates page). The June cycle does not feed EMNLP 2026. This affects the entire planning horizon.", "LLM confirmation bias undermines the 'falsification' framing: arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs systematically exhibit confirmation bias in hypothesis testing — they select confirmatory rather than falsifying evidence. This suggests that LLM-generated hypotheses will be easier to confirm than disconfirm, and the Bayesian posterior may converge spuriously. The paper should address whether its hypotheses are genuinely falsifiable or merely confirmable.", "PRISM benchmark misfit: PRISM (NeurIPS 2024) is designed for multicultural value alignment and subjective disagreement, not individual preference personalization of LLM response style. Evaluating FABEL — which targets writing format, structure, and tone — on PRISM is not well-motivated. The authors should justify why PRISM reveals anything beyond PersonalLLM for the proposed application.", "GPU cost realism: evaluating against FSPO (which requires a pretrained meta-learning model) as a baseline may require non-trivial setup not captured in the 150h A100 manual estimate; the GPT-4-as-judge costs for PersonalLLM-scale evaluation (1500 simulated users) could also be underestimated."]
Feedback: The core insight — combining HyPerAlign-style demonstration-grounded hypothesis generation with EIG-based binary validation — is a coherent contribution to the personalization literature, but the generator must make three priority revisions before this is ready to submit:

1. **Reposition against BED-LLM (ICLR 2026)**: 'This idea is too similar to BED-LLM (arXiv 2508.21184, ICLR 2026). Specifically, BED-LLM samples N=15 hypotheses, selects questions via EIG to split the hypothesis set, and updates beliefs with Bayesian rejection sampling — the same pipeline as FABEL. To differentiate, the generator should (a) explicitly compare against BED-LLM as a baseline, (b) emphasize FABEL's unique starting point of few-shot user demonstrations (HyPerAlign-style) rather than free-form hypothesis sampling, and (c) show that grounding hypotheses in demonstrations produces qualitatively different, more accurate preference summaries than BED-LLM's unconditioned sampling. The application domain (LLM response style vs. item recommendation) is a real differentiator worth foregrounding.'

2. **Fix the GATE landscape description**: Acknowledge the GATE binary variant and clarify why FABEL differs — likely the combination of demonstration-grounded hypothesis generation (not free-form question asking) with Bayesian belief tracking is the real gap, not the binary format alone.

3. **Fix the PEBOL arXiv attribution (2510.12015 → 2405.00981) and the venue deadline (June 15 → May 25).** These are immediate disqualifiers for a careful reviewer.

4. **Address confirmation bias**: Add analysis or ablation showing the LLM does not systematically generate only confirmable hypotheses. Consider adding a 'disconfirmation probe' to the hypothesis set by design, or show empirically that the posterior does update in both directions.

If BED-LLM is incorporated as a strong baseline and FABEL shows clear gains on the LLM response-style personalization task (PersonalLLM win-rates, reduced user-turn word count), the contribution is publishable at EMNLP Findings level. As written, the novelty gap is insufficient for EMNLP Main.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Venue requirement failure: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, ≤16 days). The proposal itself concedes this deadline 'has effectively passed for a project beginning now (May 10, 2026)' and retargets to AAAI 2027/ICLR 2027. This is an honest but fatal mismatch: the idea as scoped cannot satisfy the user's primary hard constraint. Either a severely stripped-down MVP (PersonalLLM only, BED-LLM + HyPerAlign as the two primary baselines, no LaMP sweep, no full ablation, simulated user evaluation only) must be proposed for the 16-day window, or the idea should explicitly declare EMNLP 2026 out of scope.", "CRITICAL — Compute constraint non-compliance in the 16-day-feasible mode: The auto_research mode (the only mode that meets ≤16 days) uses ~600h A100. At the industry-standard ~2–2.5× H100/A100 throughput ratio, this translates to approximately 240–300 H100-hours — exceeding the ≤200 H100-hour hard constraint by 20–50%. A minimum viable experiment (PersonalLLM + 3 baselines, 1 backbone, core ablation) would likely require only ~150–180h A100 (≈75–90h H100), well within limits — but this needs to be explicitly scoped and stated rather than leaving the constraint compliance implicit.", "Missing citation — PROSE (arXiv 2505.23815, ICML 2025): 'Aligning LLMs by Predicting Preferences from User Writing Samples' (Aroca-Ouellette et al., Apple ML Research) uses user writing demonstrations to iteratively refine free-form preference descriptions, then verifies component claims against held-out demonstrations. This is directly competitive with FABEL Stage 1 and was not cited anywhere in the landscape. A reviewer would flag this immediately. To differentiate: PROSE infers free-form preferences with no user interaction and no Bayesian posterior; FABEL generates binary-confirmable hypotheses, tracks a formal Bayesian posterior, selects questions via EIG, and adds mandatory disconfirmation probes. PROSE should be added as a sixth baseline or at minimum a related work requiring explicit differentiation.", "BED-LLM reimplementation risk underestimated for 16-day window: The proposal's own auto_research note flags 'faithful replication of their rejection-sampling update' as the primary engineering risk. BED-LLM's EIG estimator involves non-trivial sampling over LLM predictive distributions at each turn. Reproducing this within a 16-day timeline — alongside implementing FABEL itself and running PersonalLLM/LaMP evaluations — is aggressive. The proposal should either identify an existing public BED-LLM implementation or explicitly time-box the reimplementation risk.", "ICRM / Bayesian Preference Learning for Test-Time Steerable Reward Models (arXiv 2602.08819, Feb 2026) not cited: This paper uses a Beta posterior conditioned on in-context preference demonstrations for test-time reward model steering — partial overlap with FABEL's warm-start initialization from demonstrations. The settings differ (pairwise reward modeling vs. interactive style elicitation), but the Bayesian in-context conditioning from demonstrations is directly adjacent and a reviewer familiar with this work might question the warm-start prior novelty. It should be acknowledged in the related work."]
Feedback: The generator has addressed all six Round 1 issues cleanly and the core idea remains sound, but two critical problems prevent a pass verdict:

**Priority 1 — Scope the idea for the actual 16-day / EMNLP 2026 constraint (or declare a mismatch).**
The generator honestly acknowledges EMNLP 2026 is unreachable for a full 5-baseline sweep across PersonalLLM + LaMP. But the user's hard constraint is 16 days and EMNLP 2026. The generator should choose one of:
(a) Propose a stripped-down EMNLP 2026 MVP: PersonalLLM benchmark only, 3 baselines (HyPerAlign, BED-LLM, GATE binary), 1 LLM backbone (Qwen 3.5), simulated user evaluation using the PersonalLLM reward-model infrastructure, 1 ablation (warm vs. uniform prior). Estimated compute: ~150h A100 (~75h H100-equivalent), 12–14 days in auto mode. This fits all hard constraints.
(b) Explicitly flag the idea as AAAI 2027 / ICLR 2027 scope with a concrete explanation of why 16 days is insufficient for the full version — so the user can make an informed decision.

**Priority 2 — Add PROSE as a baseline and missing citation.**
PROSE (arXiv 2505.23815, ICML 2025) directly competes with FABEL's Stage 1: it takes user writing samples and iteratively refines preference descriptions with component verification. Cite it, differentiate it (PROSE: free-form, non-interactive, no Bayesian posterior; FABEL: binary hypotheses, interactive EIG confirmation, formal posterior, disconfirmation probes), and include it as a baseline. Without PROSE, the novelty argument has an obvious gap that peer reviewers would flag.

**Priority 3 — Fix the compute compliance in auto mode.**
Restate the minimum-viable-experiment compute as ~150–180h A100 and explicitly confirm it falls under 200 H100-hour equivalent. The full 600h A100 ablation sweep is 'nice to have' for camera-ready, not required for ARR submission.

If the generator delivers a scoped EMNLP 2026 MVP (Priority 1) with PROSE integrated (Priority 2) and compute compliance verified (Priority 3), the idea is publishable at EMNLP 2026 Findings level. The core novelty — warm-start Bayesian initialization from demonstrations + EIG binary confirmation + mandatory disconfirmation probes — is genuinely new and the empirical design (warm vs. cold prior ablation, disconfirmation rate diagnostic) is strong. The differentiation from BED-LLM (cold start, item recommendation) and from PROSE/HyPerAlign (no interactive validation) is clean.

### Round 3 review
Verdict: revise
Issues: ["OPEN (arXiv 2403.05534, ACL 2024) — 'Bayesian Preference Elicitation with Language Models' — is not cited. This paper applies Bayesian Optimal Experimental Design (BOED, mathematically equivalent to EIG) with LMs to select informative preference-elicitation questions in natural language. It is a direct algorithmic predecessor to BED-LLM for the preference elicitation setting and a reviewer aware of it would challenge FABEL's EIG-over-BED-LLM positioning. The proposal should cite OPEN as the foundation of the BOED-for-preference-elicitation line, position BED-LLM as the current state of that line, and clarify how FABEL (demonstration-grounded warm start + disconfirmation probes) extends beyond both.", "Disconfirmation probe / EIG interaction is algorithmically underspecified. The proposal includes K_neg=4–6 disconfirmation probes in the hypothesis set but does not specify how EIG-based selection handles them at each turn: (a) are they included in the EIG-ranked pool and selected only when EIG identifies them as maximally informative — in which case the EIG criterion may already approximate the disconfirmation behavior, making the explicit probe design partially redundant; (b) are they always asked in the first K_neg turns before EIG kicks in — which wastes turns if the demonstrations already resolved them; or (c) are they asked as post-loop audits — which breaks the Bayesian update chain. This interaction must be precisely specified in the algorithm description, since it determines whether the disconfirmation probe mechanism adds genuine information-theoretic value beyond EIG or is purely a diagnostic overlay.", "Warm-start prior calibration is assumed but unvalidated. The proposal initializes p(h_i = true | demonstrations) using LLM-estimated likelihoods conditioned on K demonstrations. LLM probability estimates are notoriously poorly calibrated — overconfident estimates would concentrate mass on the wrong hypotheses before any user interaction, potentially causing slower convergence than a uniform (BED-LLM-style) cold start. The paper should either (a) include an empirical calibration check showing the LLM-estimated likelihoods are well-ordered relative to ground-truth hypothesis accuracy, or (b) add a temperature-scaling or entropy-regularized prior initialization step with explicit justification.", "EMNLP 2026 Main vs. Findings targeting realism. The user specified EMNLP 2026 Main as the primary target. The MVP (single benchmark PersonalLLM, simulated reward-model evaluation, one backbone Qwen 3.5-7B, one ablation) is credible for EMNLP Findings but borderline for Main. EMNLP Main typically requires either (a) multi-benchmark generalization, (b) a human user study even at small scale, or (c) a theoretically novel contribution beyond component combination. The current design lacks all three. The proposal should either explicitly target Findings as the realistic primary target, or strengthen one of these dimensions — even a 20-person crowdsourced preference evaluation using the PersonalLLM prompts would substantially strengthen the Main case within the 16-day window."]
Feedback: The proposal has cleanly addressed all Round 1 and Round 2 critical issues: venue deadline is correct (May 25, 2026), compute is within budget (~75h H100-equivalent), PROSE is included as baseline #3, BED-LLM is confirmed accepted at ICLR 2026, ICRM is acknowledged, and the MVP scope is explicitly and realistically defined. The core idea — warm-start Bayesian prior from demonstrations + EIG binary confirmation + disconfirmation probes — is a coherent, well-motivated contribution. Three targeted revisions will bring this to pass:

**Fix 1 — Add OPEN to the landscape (1 paragraph in related work):** 'This idea is too similar to OPEN (arXiv 2403.05534, ACL 2024) without acknowledgment. OPEN applies BOED with LMs to select informative preference questions in NL — the same mathematical framework as BED-LLM, specifically for preference elicitation. To differentiate: OPEN lacks demonstration-conditioned priors, requires cold-start initialization, and has no disconfirmation mechanism. Include OPEN in the BOED lineage alongside BED-LLM and clarify that FABEL's contribution is the warm-start + disconfirmation extension of this line.'

**Fix 2 — Specify disconfirmation probe algorithm precisely:** Add a paragraph to Stage 3 clarifying whether disconfirmation probes are (a) included in the EIG-ranked pool, (b) asked as mandatory initial turns, or (c) reserved as post-convergence audits. Option (a) is algorithmically cleanest — EIG will naturally select them when they are maximally uncertain, making the explicit design a prior-shaping device rather than a scheduling override. Report the empirical fraction of turns where EIG selects a disconfirmation probe vs. a positive hypothesis as a diagnostic.

**Fix 3 — Calibration check or regularization for warm-start prior:** Add either (a) a small analysis showing that LLM-estimated likelihoods are well-ordered relative to demonstration-consistent hypotheses (even a rank-correlation analysis on 50 PersonalLLM examples would suffice), or (b) a temperature-scaled prior initialization: p(h_i) ∝ exp(LLM_log_likelihood / τ) with τ tuned to match empirical calibration. This directly addresses the most technically vulnerable assumption in the method.

### Round 4 review
Verdict: revise
Issues: ["CRITICAL reproducibility error — 'Qwen 3.5-7B-Instruct' does not exist: Qwen3.5 (released Feb 2026) contains 4B, 27B, 35B-A3B (MoE), and 397B-A17B (MoE) variants; there is no 7B model in the Qwen3.5 family. This model name appears throughout the proposal as the single backbone. The correct alternatives are Qwen2.5-7B-Instruct (huggingface.co/Qwen/Qwen2.5-7B-Instruct, widely used in personalization benchmarks) or Qwen3-8B (huggingface.co/Qwen/Qwen3-8B). A reviewer or reproduction attempt would fail immediately at environment setup. Fix: replace all instances of 'Qwen 3.5-7B-Instruct' with 'Qwen2.5-7B-Instruct' or 'Qwen3-8B' with the appropriate HuggingFace identifier.", "Missing citation — AMPLe (arXiv 2411.00524, ACL 2025): 'Comparison-based Active Preference Learning for Multi-dimensional Personalization' (Oh, Lee, Ok; ACL 2025, with public code at github.com/ml-postech/AMPLe) uses Bayesian inference with modified posterior updates and a generalized binary-search-inspired active query selection strategy to capture implicit multi-dimensional preferences for LLM personalization — directly adjacent to FABEL's active Bayesian personalization setting. While AMPLe uses pairwise comparison queries rather than demonstration-conditioned hypotheses (making differentiation clear: FABEL provides a warm prior from demonstrations, asks binary hypothesis confirmation rather than item comparisons, and adds mandatory disconfirmation probes), the omission of an ACL 2025 active Bayesian preference learning paper in the LLM personalization domain is a gap that reviewers familiar with the area would notice. Add to the landscape under cluster (3) or create a new cluster for comparison-based active preference learning.", "Unstated hypothesis-independence assumption in Stage 3 Bayesian update: The per-hypothesis Bayesian update (applying Bayes' rule independently to each h_i) implicitly treats all preference hypotheses as statistically independent. In practice, preference attributes are highly correlated (e.g., 'prefers brevity' correlates with 'prefers bullet points over prose'). Under this factored approximation, the posterior update may be inconsistent: confirming 'prefers brevity' should increase the probability of correlated hypotheses, but the factored update leaves them unchanged. The proposal should either (a) acknowledge this as a stated approximation (factored posterior) in the algorithm description, or (b) briefly justify why correlations are low in the PersonalLLM hypothesis space (e.g., by reporting inter-hypothesis correlation on the dev split). This is a technical vulnerability that a Bayesian reviewer would raise.", "EIG terminology imprecision: Stage 3 states 'selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2' and also calls this 'EIG-based.' Maximum marginal entropy equals EIG only under the factored (independent) posterior assumption. Under a correlated posterior, maximizing joint EIG requires summing over hypotheses and is strictly different from marginal entropy maximization. Since the proposal uses a factored update, calling it 'EIG-based' is technically correct but only by virtue of the unstated independence assumption. Clarify in one sentence: 'Under the factored posterior approximation, maximizing marginal entropy H(p(h_i)) is equivalent to EIG-based selection.'"]
Feedback: Round 4 has resolved all three Round 3 issues cleanly: OPEN is now thoroughly cited and integrated into the BOED lineage narrative; the disconfirmation probe algorithm is precisely specified (EIG pool inclusion + soft minimum quota); and Stage 2a calibration analysis (Spearman ρ, τ selection on 50 dev users) directly addresses the warm-start prior vulnerability. The core idea is solid and publication-ready at EMNLP Findings level once the following targeted fixes are applied:

**Fix 1 (Critical) — Replace non-existent model name throughout.** 'Qwen 3.5-7B-Instruct' does not exist in the Qwen3.5 family (which has 4B, 27B, and MoE variants only). Replace with 'Qwen2.5-7B-Instruct' (Qwen/Qwen2.5-7B-Instruct on HuggingFace — available, widely benchmarked) or 'Qwen3-8B' (Qwen/Qwen3-8B on HuggingFace). This affects every experimental description and the resource estimate; apply the substitution consistently.

**Fix 2 (Moderate) — Cite AMPLe (arXiv 2411.00524, ACL 2025).** Add one paragraph in Section 2 (Related Work) under active preference learning: 'AMPLe (Oh et al., ACL 2025) uses Bayesian inference with modified posterior updates and active comparison-based query selection for multi-dimensional LLM personalization. FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary hypothesis confirmation ("does this stylistic claim apply to you?") rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe.' No ablation needed — citation and differentiation suffice.

**Fix 3 (Minor) — Acknowledge hypothesis-independence assumption.** Add one sentence to Stage 3 after the Bayesian update equation: 'We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization is equivalent to EIG-based selection.' This closes both the EIG terminology issue and the independence assumption gap in one edit.

After these three fixes, the proposal has no critical technical gaps, the venue deadline is correct, compute is within budget, and the MVP scope (PersonalLLM + 4 baselines + 1 ablation + Stage 2a calibration) is credibly executable in the 16-day window. Recommend one more targeted revision pass.

### Round 5 review
Verdict: revise
Issues: ["MODERATE — BED-LLM prior characterization is factually wrong and would be caught by a reviewer who reads the paper. The proposal repeatedly says BED-LLM 'starts from cold uniform prior (no domain ranking, no user demonstrations).' However, the BED-LLM paper defines the initial prior as p_f(θ;h_t=∅) — the LLM's own predictive distribution over hypotheses given no history — which is an LM-generic prior (not uniform), analogous in spirit to OPEN's domain-generic feature importance ranking. Additionally, BED-LLM uses multiple-choice questions (not binary yes/no), because as the paper states, 'having a small space of single-token responses ensures that p_LLM provides meaningful uncertainty over outcomes.' The proposal must correct both: (a) replace 'cold uniform prior' with 'LM-generic prior, not conditioned on user demonstrations'; (b) note that FABEL uses binary yes/no confirmation (lower cognitive load) while BED-LLM uses multiple-choice. The novelty argument remains valid — FABEL's demo-conditioned prior is a real differentiator from BED-LLM's demo-agnostic LM prior — but the current phrasing is inaccurate.", "MINOR — Stage 2a calibration analysis is underspecified. The proposal describes 'Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users' but never operationalizes 'empirical hypothesis accuracy' for simulated users. In the PersonalLLM framework, simulated users are represented as weighted ensembles of reward models. The paper must specify: for each hypothesis h_i and each simulated user, ground truth accuracy = fraction of that user's reward-model-preferred responses that satisfy h_i (e.g., for 'prefers bullet points,' check what fraction of high-reward responses are bulleted). Without this operational definition, Stage 2a is unverifiable and a reviewer will ask exactly this question.", "MINOR — BED-LLM's application domain is described as 'item recommendation' throughout the proposal, but BED-LLM evaluates on both 20-Questions and preference elicitation via movie-preference multiple-choice questions — a general preference inference setting. While 'item recommendation' is partially correct, the more accurate framing is 'latent preference vector inference from sequential multiple-choice queries, without user demonstrations.' This distinction matters because FABEL's application to LLM response-style personalization (format, tone, structure) is a domain shift, not just a warm-start shift."]
Feedback: Round 4 fixes have all been applied cleanly: Qwen2.5-7B-Instruct replaces the non-existent 'Qwen 3.5-7B-Instruct,' AMPLe is now cited and differentiated in cluster (3b), and the factored posterior approximation is explicitly acknowledged in Stage 3. The proposal is close to passing. Three targeted edits will get it there:

**Fix 1 (Moderate, 1–2 paragraphs) — Correct the BED-LLM prior description.** Replace every instance of 'cold uniform prior' in the BED-LLM description with 'LM-generic prior (p_f(θ;∅): the LLM's unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations).' Add one clause noting that BED-LLM uses multiple-choice questions, not binary yes/no, making FABEL's binary format an additional differentiator. The revised differentiation argument: 'FABEL extends BED-LLM in three ways: (1) prior conditioned on this user's K demonstrations (vs. BED-LLM's demo-agnostic LM prior); (2) binary yes/no confirmation (vs. BED-LLM's multiple-choice format); (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work.'

**Fix 2 (Minor, 1 paragraph) — Operationalize Stage 2a ground truth.** In the Stage 2a description, add: 'For each simulated PersonalLLM dev user u and hypothesis h_i, empirical accuracy = fraction of u's top-quartile reward-model responses that satisfy h_i (assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i, then comparing against the reward model's preference ordering via Kendall τ). This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.'

**Fix 3 (Minor, 1 sentence) — Clarify BED-LLM domain.** Replace 'targets item recommendation' with 'targets latent preference vector inference via movie-preference multiple-choice queries' in the BED-LLM description. This sharpens the domain-shift argument: FABEL is the first to apply the OPEN→BED-LLM BOED lineage to LLM response-style personalization (format, tone, structure) from free-form demonstrations.

With these three fixes applied, the proposal has no remaining critical gaps. The combination of user-demonstration-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel, the MVP compute fits within the ≤200 H100-hour constraint, and the empirical design (warm vs. cold ablation, Stage 2a calibration, disconfirmation diagnostic) is appropriate for EMNLP Findings.

### Round 6 review
Verdict: revise
Issues: ["MINOR — TO-GATE related work description is inaccurate: the proposal states TO-GATE 'applies DPO to clarifying question quality, remaining in the open-ended, non-Bayesian regime,' but independent verification (arXiv 2506.02827 fetched) confirms TO-GATE uses trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline — not just clarifying question quality in isolation. While the non-Bayesian characterization is correct, the narrow phrasing 'DPO to clarifying question quality' misrepresents the method and would be flagged by a TO-GATE-aware reviewer.", "MINOR — Disconfirmation probe generation mechanism underspecified: Stage 1 states that Qwen2.5-7B-Instruct generates K_neg=4–6 'hypotheses deliberately constructed to be easily falsifiable given the demonstrations,' but the proposal nowhere specifies the prompt or instructions used to elicit deliberately falsifiable probes as opposed to the model's default confirmatory behavior (which is precisely what arXiv 2604.02485 shows is the default). A reviewer will ask in rebuttal: 'How do you ensure the LLM generates probes that are genuinely falsifiable rather than merely low-confidence confirmatory hypotheses?' The generation mechanism must be concretely specified.", "MINOR — Stage 2a τ selection failure mode unspecified: the proposal selects τ as 'the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6,' but provides no fallback if no τ achieves ρ > 0.6 (i.e., if LLM log-likelihoods are uncorrelated with empirical accuracy for some hypothesis class). A reviewer will ask what happens in this case. The paper needs one sentence: e.g., 'If no τ achieves the threshold, we default to τ→∞ (uniform prior) and report this user as a calibration failure in diagnostic analysis.'", "MINOR — Human study statistical power and EMNLP Main claim in tension: the proposal simultaneously acknowledges the n≈20 study is 'underpowered for significance' and asserts it 'substantially strengthens the EMNLP Main case per reviewer guidance.' These claims are contradictory. An underpowered real-user study that cannot reach statistical significance does not meaningfully distinguish FABEL from a well-designed ablation — reviewers targeting EMNLP Main will note this. The claim should be hedged to 'provides a qualitative real-user signal and preliminary external validity evidence, not statistical confirmation.'"]
Feedback: All Round 5 issues are cleanly resolved and independently verified: BED-LLM is confirmed ICLR 2026 (OpenReview ID: qyylZMLYT8), its LM-generic prior p_f(θ;∅) is correctly described, its multiple-choice format is noted, and its domain (latent preference vector inference, not item recommendation) is now correct. Stage 2a ground-truth operationalization is adequately specified. Four minor issues remain:

**Fix 1 (1 sentence, related work):** Replace the TO-GATE description with: 'TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior.' The current phrasing ('DPO to clarifying question quality') understates the scope and would be caught by a TO-GATE-aware reviewer.

**Fix 2 (1 paragraph, Stage 1):** Specify the disconfirmation probe generation prompt explicitly. Example: 'We instruct the LLM: generate K_neg hypotheses that are plausibly true of some user but LIKELY VIOLATED by the provided writing samples—stylistic attributes the demonstrations actively disconfirm. Example: if all samples use numbered lists, generate the probe "User avoids numbered lists."' Without this, the mechanism is not reproducible and the novelty claim (that probes are genuinely falsifiable, not just low-confidence) is unverifiable.

**Fix 3 (1 sentence, Stage 2a):** Add: 'If no τ satisfies ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent) and flag the failure in diagnostic analysis.' This closes the only remaining technical gap in the calibration procedure.

**Fix 4 (1 sentence, human study description):** Replace 'substantially strengthens the EMNLP Main case' with 'provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas; the study is underpowered for statistical inference and results are reported descriptively.' This aligns the claim with the actual evidence and preempts the obvious reviewer objection.

### Round 7 review
Verdict: revise
Issues: ["MODERATE — Stage 2a circular self-evaluation: The Spearman ρ calibration analysis uses Qwen2.5-7B-Instruct both to (a) compute LLM log-likelihood scores score_i over demonstrations and (b) classify whether responses satisfy hypothesis h_i (for computing empirical accuracy). Since both quantities are derived from the same model, the correlation may reflect internal model consistency rather than genuine predictive validity over user preferences. Specifically, the model will tend to assign higher log-likelihoods to demonstration text that matches hypotheses it would also classify as satisfied—this is circular and could inflate ρ relative to its true value as a predictor of real user agreement. The paper should either: (a) acknowledge this as a stated limitation ('ρ is a model-consistency measure; real-user calibration is validated post-hoc via the Prolific study'), or (b) use a different model for the hypothesis satisfaction classification step (e.g., Llama 3.1-8B or a specialist NLI model) to break the circularity.", "MINOR — Human study framing residual overstatement: Despite correctly acknowledging the study is 'underpowered for statistical inference and results are reported descriptively,' the sentence continues 'which strengthens the EMNLP Main case relative to a purely simulated evaluation.' An underpowered descriptive study that cannot support statistical inference does not meaningfully strengthen the EMNLP Main case in the eyes of reviewing committees—it provides anecdotal, externally valid evidence but not a primary result. Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas but cannot substitute for a powered human study in Main review criteria.'"]
Feedback: Round 7 has cleanly resolved all four Round 6 issues: TO-GATE is correctly described as trajectory-level DPO, the disconfirmation probe prompt is explicitly specified with evidence-citing requirement, the τ→∞ fallback is added, and the human study is labeled underpowered. Independent verification confirms that arXiv 2602.15012 (the only unverified potential competitor) targets reasoning tasks with structured world model priors and does not overlap with FABEL's domain or mechanism. The core combination is genuinely novel and technically sound. Two targeted fixes are needed:

**Fix 1 (Moderate, 2–3 sentences in Stage 2a): Break or acknowledge the circular self-evaluation.** The Spearman ρ calibration uses Qwen2.5-7B-Instruct for both log-likelihood scoring and hypothesis satisfaction classification — this creates an internal consistency artifact that may inflate ρ. Add: 'We note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences. To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis classifier, providing a cross-model calibration check.' Alternatively, acknowledge this limitation explicitly and defer cross-model validation to Phase 2.

**Fix 2 (Minor, 1 clause): Remove the residual EMNLP Main overstatement.** Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas, reported descriptively.' This aligns with the already-correct statement that the study is underpowered.

After these two fixes, the proposal has no remaining critical issues. The combination of demo-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel and appropriately scoped for EMNLP 2026 Findings. The MVP compute estimate (75h H100-equivalent) is confirmed within budget, and the PersonalLLM benchmark is publicly available.

### Round 8 review
Verdict: revise
Issues: ["MODERATE — AdaptFuse (arXiv 2604.03925, April 2026) is uncited and directly adjacent: 'Training-Free Sequential Preference Learning via Externalized Bayesian Inference' maintains a Bayesian posterior over discrete hypothesis sets using a frozen LLM's semantic reasoning via entropy-adaptive fusion — it is in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL. FABEL's key differentiator (demo-conditioned warm prior + disconfirmation probes) holds, but AdaptFuse must be cited and differentiated in the landscape. A reviewer familiar with April 2026 arXiv would flag its absence immediately. Suggested addition to cluster (3) or a new cluster: 'AdaptFuse (2604.03925) uses externalized symbolic Bayesian inference over hypothesis sets with entropy-adaptive frozen-LLM fusion; FABEL differs by (1) initializing a user-specific demo-conditioned warm prior rather than cold-start symbolic updates, and (2) including mandatory disconfirmation probes absent from AdaptFuse.'", "MINOR — MAPLE (arXiv 2412.07207, AAAI 2025) is uncited. It uses LLM-modeled preference function distributions conditioned on natural language feedback with active query selection for general alignment — in the same broad space as FABEL's active Bayesian personalization. While MAPLE uses trajectory-level pairwise rankings (not binary hypothesis confirmation) and targets general alignment rather than response-style personalization, a one-sentence mention in landscape cluster (3b) or a new cluster is sufficient. Without it, the landscape is incomplete for AAAI 2025 active preference learning work."]
Feedback: After seven rounds of thorough revision, this proposal is substantively close to publication-ready at EMNLP Findings level. All Round 7 issues are cleanly resolved: the self-consistency circularity in Stage 2a is addressed via the cross-model Llama-3.1-8B-Instruct calibration check with explicit fallback behavior; the human study overstatement is removed. Two remaining citation gaps must be closed:

**Fix 1 (Moderate, 1 paragraph):** Cite AdaptFuse (arXiv 2604.03925, April 2026) as a concurrent member of the training-free Bayesian hypothesis-set inference family. Place it in landscape cluster (3) or a new cluster (6). Key differentiation: 'AdaptFuse maintains a symbolic Bayesian posterior over discrete hypotheses using entropy-adaptive fusion with a frozen LLM; FABEL extends this line with (1) user-specific demonstration-conditioned warm priors rather than cold symbolic initialization and (2) mandatory disconfirmation probes that AdaptFuse lacks.' This is the closest concurrent work and its absence would be flagged by area chairs familiar with April 2026 arXiv.

**Fix 2 (Minor, 1-2 sentences):** Cite MAPLE (arXiv 2412.07207, AAAI 2025) in related work on active preference learning for LLMs. One sentence suffices: 'MAPLE (AAAI 2025) uses LLM-conditioned preference function modeling with active query selection for alignment tasks; FABEL differs in using binary hypothesis confirmation grounded in user demonstrations rather than trajectory-level pairwise ranking queries.' This closes the AAAI 2025 gap in the landscape.

After these two fixes, there are no remaining critical gaps. The core novelty claim — demo-conditioned warm Bayesian prior + EIG binary confirmation + disconfirmation probes, in the LLM response-style personalization domain — is verified as absent from all cited and independently found prior work. The MVP compute (75h H100-equivalent) is confirmed within budget, PersonalLLM is publicly available, and the experimental design (warm vs. cold prior ablation + Stage 2a calibration with cross-model ρ check) is appropriate for EMNLP Findings.


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
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "bafd2ac3-6554-4e48-a083-7efff3418384",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:10:38.670Z_

```json
{
  "parentUuid": "bafd2ac3-6554-4e48-a083-7efff3418384",
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
  "uuid": "c6c290c6-685e-4950-8ff8-d03e3c741f4b",
  "timestamp": "2026-05-10T08:10:38.670Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:10:38.671Z_

```json
{
  "parentUuid": "c6c290c6-685e-4950-8ff8-d03e3c741f4b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8ce735dd-7adb-4341-90c6-0cd5f9ef57ec",
  "timestamp": "2026-05-10T08:10:38.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
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
  "leafUuid": "8ce735dd-7adb-4341-90c6-0cd5f9ef57ec",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:10:57.258Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 9/10 of the review process. I need to conduct an independent adversarial review of the FABEL proposal. Let me analyze what's been fixed from previous rounds and then conduct fresh research to verify claims.

Key issues addressed in previous rounds:
1. BED-LLM citation and differentiation - DONE
2. GATE binary variant acknowledged - DONE
3. PEBOL arXiv attribution fixed - DONE
4. Venue deadline corrected to May 25, 2026 - DONE
5. LLM confirmation bias addressed with disconfirmation probes - DONE


6. PRISM benchmark removed - DONE
7. Compute constraint verified within 200 H100-hours - DONE
8. PROSE added as baseline - DONE
9. OPEN cited as BOED lineage foundation - DONE
10. Disconfirmation probe algorithm specified - DONE
11. Warm-start calibration check added - DONE
12. Model name fixed (Qwen2.5-7B-Instruct) - DONE
13. AMPLe cited - DONE
14. Factored posterior approximation acknowledged - DONE
15. BED-LLM prior correctly described as LM-generic - DONE
16. BED-LLM domain corrected - DONE

Now I'm continuing through the remaining corrections to verify everything's been properly addressed.

I need to validate a few key citations and check for any concurrent works we might have missed, particularly confirming AdaptFuse and MAPLE are correctly characterized, and then do a fresh search to catch any other relevant recent work we haven't cited yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ce735dd-7adb-4341-90c6-0cd5f9ef57ec",
  "isSidechain": false,
  "requestId": "req_011CatYpL958TcbAQB7E8gMF",
  "type": "assistant",
  "uuid": "459e472f-fdd5-464e-b4aa-ba13a35e5a38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KpQuZ3bnMqWziPmtgDTEpy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31277,
      "cache_read_input_tokens": 11631,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 704,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 31277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31277
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

_source line 9 · 2026-05-10T08:10:57.282Z_

I'll conduct independent adversarial research to verify the claims in this Round 9 proposal, focusing on any remaining gaps, concurrent work, and feasibility checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "459e472f-fdd5-464e-b4aa-ba13a35e5a38",
  "isSidechain": false,
  "requestId": "req_011CatYpL958TcbAQB7E8gMF",
  "type": "assistant",
  "uuid": "f64975e0-2185-4019-9523-5f8a6a1bab71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KpQuZ3bnMqWziPmtgDTEpy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31277,
      "cache_read_input_tokens": 11631,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 704,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 31277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31277
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

_source line 10 · 2026-05-10T08:10:57.352Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FuUPH9FAHf9BuMZ3tPjxkU`</summary>

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
  "parentUuid": "f64975e0-2185-4019-9523-5f8a6a1bab71",
  "isSidechain": false,
  "requestId": "req_011CatYpL958TcbAQB7E8gMF",
  "type": "assistant",
  "uuid": "701a7de1-111b-4e69-a553-eefd2e1bd2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KpQuZ3bnMqWziPmtgDTEpy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31277,
      "cache_read_input_tokens": 11631,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 704,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 31277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31277
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

_source line 11 · 2026-05-10T08:10:57.358Z_

<details><summary>↩ Tool result · `toolu_01FuUPH9FAHf9BuMZ3tPjxkU`</summary>

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
  "parentUuid": "701a7de1-111b-4e69-a553-eefd2e1bd2d0",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "0bc4a029-3b14-4c5e-9437-4a93a3367e4f",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "701a7de1-111b-4e69-a553-eefd2e1bd2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T08:10:59.934Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct my independent research. I'll run multiple searches in parallel to verify key claims and find any remaining issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bc4a029-3b14-4c5e-9437-4a93a3367e4f",
  "isSidechain": false,
  "requestId": "req_011CatYqiCQ1sdCeJnY3Txxx",
  "type": "assistant",
  "uuid": "aeaa8c4b-0b97-4e7c-95a4-f236f651ec98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EkWH622y49nhMu8TcCd3zq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 42908,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1726,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 42908,
          "cache_creation_input_tokens": 1726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1726
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

_source line 13 · 2026-05-10T08:11:00.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017BUVJpbUhPhxTpe29RuQPi`</summary>

```json
{
  "query": "AdaptFuse arXiv 2604.03925 training-free Bayesian preference learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeaa8c4b-0b97-4e7c-95a4-f236f651ec98",
  "isSidechain": false,
  "requestId": "req_011CatYqiCQ1sdCeJnY3Txxx",
  "type": "assistant",
  "uuid": "64e9c730-d91a-4cf0-b61b-610ce368d147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EkWH622y49nhMu8TcCd3zq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 42908,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1726,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 42908,
          "cache_creation_input_tokens": 1726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1726
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

_source line 14 · 2026-05-10T08:11:01.230Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WS4MnevuWQpB9vGS4tYj4m`</summary>

```json
{
  "query": "FABEL falsification binary elicitation LLM personalization arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64e9c730-d91a-4cf0-b61b-610ce368d147",
  "isSidechain": false,
  "requestId": "req_011CatYqiCQ1sdCeJnY3Txxx",
  "type": "assistant",
  "uuid": "65425956-d076-431f-982e-45d09bafa5ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EkWH622y49nhMu8TcCd3zq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 42908,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1726,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 42908,
          "cache_creation_input_tokens": 1726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1726
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

_source line 15 · 2026-05-10T08:11:01.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KV6ZuiYWsJLZDw7tzSCZdF`</summary>

```json
{
  "query": "BED-LLM Bayesian experimental design language models preference elicitation ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65425956-d076-431f-982e-45d09bafa5ea",
  "isSidechain": false,
  "requestId": "req_011CatYqiCQ1sdCeJnY3Txxx",
  "type": "assistant",
  "uuid": "aeeb40a6-9ddf-4de3-994f-42aca5351aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EkWH622y49nhMu8TcCd3zq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1726,
      "cache_read_input_tokens": 42908,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1726,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 228,
          "cache_read_input_tokens": 42908,
          "cache_creation_input_tokens": 1726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1726
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

_source line 16 · 2026-05-10T08:11:07.714Z_

<details><summary>↩ Tool result · `toolu_017BUVJpbUhPhxTpe29RuQPi`</summary>

```text
Web search results for query: "AdaptFuse arXiv 2604.03925 training-free Bayesian preference learning 2026"

Links: [{"title":"[2604.03925] AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference","url":"https://arxiv.org/abs/2604.03925"},{"title":"AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference","url":"https://arxiv.org/html/2604.03925"},{"title":"[2604.03925v1] AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference","url":"https://arxiv.org/abs/2604.03925v1"},{"title":"Deep Bayesian Active Learning for Preference Modeling in Large Language Models","url":"https://arxiv.org/html/2406.10023v1"},{"title":"[2412.05723] Training-Free Bayesianization for Low-Rank Adapters of Large Language Models","url":"https://arxiv.org/abs/2412.05723"},{"title":"Deep Bayesian Active Learning for Preference Modeling in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=TADTT9ughN&noteId=KUq5hng8Z3"},{"title":"Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization","url":"https://arxiv.org/html/2512.14263v1"},{"title":"Efficient Reinforcement Learning from Human Feedback via Bayesian Preference Inference","url":"https://arxiv.org/html/2511.04286"},{"title":"Deep Bayesian Active Learning for Preference Modeling in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d5e256c988bdee59a0f4d7a9bc1dd6d9-Paper-Conference.pdf"},{"title":"Optimal Use of Preferences in Artificial Intelligence Algorithms","url":"https://arxiv.org/html/2601.18732"}]

Based on the web search results, here's what I found about AdaptFuse (arXiv 2604.03925):

## Overview

AdaptFuse is a training-free framework that externalizes probabilistic computation entirely from the LLM: a symbolic module maintains a Bayesian posterior over a discrete hypothesis set, while a frozen LLM contributes semantic reasoning via multi-sample Dirichlet aggregation.

## Problem It Addresses

Large language models struggle to accumulate evidence across multiple rounds of user interaction, failing to update their beliefs in a manner consistent with Bayesian inference. Existing solutions require fine-tuning on sensitive user interaction data, limiting their applicability in privacy-conscious settings.

## Key Technical Approach

The two signals are combined through entropy-adaptive fusion, which automatically weights each source by its predictive confidence, shifting reliance from the LLM to the symbolic posterior as evidence accumulates.

## Evaluation

The framework was evaluated across three domains: flight recommendation, hotel recommendation, and web shopping; on Gemma 2 9B, Llama 3 8B, and Qwen 2.5 7B. AdaptFuse consistently outperforms both prompting baselines and fine-tuned Bayesian Teaching models on all tasks and all base models, despite requiring no weight updates, training, or fine-tuning.

The paper was submitted to arXiv on April 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64e9c730-d91a-4cf0-b61b-610ce368d147",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "2569f4b6-e867-42c7-97d9-5bc0a9ab865b",
  "toolUseResult": {
    "query": "AdaptFuse arXiv 2604.03925 training-free Bayesian preference learning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SyLADDp9GXQCURhtZNmSbf",
        "content": [
          {
            "title": "[2604.03925] AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference",
            "url": "https://arxiv.org/abs/2604.03925"
          },
          {
            "title": "AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference",
            "url": "https://arxiv.org/html/2604.03925"
          },
          {
            "title": "[2604.03925v1] AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference",
            "url": "https://arxiv.org/abs/2604.03925v1"
          },
          {
            "title": "Deep Bayesian Active Learning for Preference Modeling in Large Language Models",
            "url": "https://arxiv.org/html/2406.10023v1"
          },
          {
            "title": "[2412.05723] Training-Free Bayesianization for Low-Rank Adapters of Large Language Models",
            "url": "https://arxiv.org/abs/2412.05723"
          },
          {
            "title": "Deep Bayesian Active Learning for Preference Modeling in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=TADTT9ughN&noteId=KUq5hng8Z3"
          },
          {
            "title": "Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization",
            "url": "https://arxiv.org/html/2512.14263v1"
          },
          {
            "title": "Efficient Reinforcement Learning from Human Feedback via Bayesian Preference Inference",
            "url": "https://arxiv.org/html/2511.04286"
          },
          {
            "title": "Deep Bayesian Active Learning for Preference Modeling in Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d5e256c988bdee59a0f4d7a9bc1dd6d9-Paper-Conference.pdf"
          },
          {
            "title": "Optimal Use of Preferences in Artificial Intelligence Algorithms",
            "url": "https://arxiv.org/html/2601.18732"
          }
        ]
      },
      "Based on the web search results, here's what I found about AdaptFuse (arXiv 2604.03925):\n\n## Overview\n\nAdaptFuse is a training-free framework that externalizes probabilistic computation entirely from the LLM: a symbolic module maintains a Bayesian posterior over a discrete hypothesis set, while a frozen LLM contributes semantic reasoning via multi-sample Dirichlet aggregation.\n\n## Problem It Addresses\n\nLarge language models struggle to accumulate evidence across multiple rounds of user interaction, failing to update their beliefs in a manner consistent with Bayesian inference. Existing solutions require fine-tuning on sensitive user interaction data, limiting their applicability in privacy-conscious settings.\n\n## Key Technical Approach\n\nThe two signals are combined through entropy-adaptive fusion, which automatically weights each source by its predictive confidence, shifting reliance from the LLM to the symbolic posterior as evidence accumulates.\n\n## Evaluation\n\nThe framework was evaluated across three domains: flight recommendation, hotel recommendation, and web shopping; on Gemma 2 9B, Llama 3 8B, and Qwen 2.5 7B. AdaptFuse consistently outperforms both prompting baselines and fine-tuned Bayesian Teaching models on all tasks and all base models, despite requiring no weight updates, training, or fine-tuning.\n\nThe paper was submitted to arXiv on April 5, 2026."
    ],
    "durationSeconds": 6.999583184000003
  },
  "sourceToolAssistantUUID": "64e9c730-d91a-4cf0-b61b-610ce368d147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T08:11:07.796Z_

<details><summary>↩ Tool result · `toolu_01KV6ZuiYWsJLZDw7tzSCZdF`</summary>

```text
Web search results for query: "BED-LLM Bayesian experimental design language models preference elicitation ICLR 2026"

Links: [{"title":"[2508.21184] BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design","url":"https://arxiv.org/abs/2508.21184"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design [Quick Review]","url":"https://liner.com/review/bedllm-intelligent-information-gathering-with-llms-and-bayesian-experimental-design"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/bed-llm"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | OpenReview","url":"https://openreview.net/forum?id=qyylZMLYT8"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design","url":"https://arxiv.org/html/2508.21184v1"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | Request PDF","url":"https://www.researchgate.net/publication/395125168_BED-LLM_Intelligent_Information_Gathering_with_LLMs_and_Bayesian_Experimental_Design"},{"title":"BED-LLM: INTELLIGENT INFORMATION GATHERING","url":"https://openreview.net/pdf?id=qyylZMLYT8"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"Published as a conference paper at ICLR 2026 TOWARD EFFICIENT EXPLORATION","url":"https://dilipa.github.io/papers/iclr26_psrl_llms.pdf"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/bed-llm-intelligent-information-gathering-llms-bayesian"}]

Based on the search results, here's information about BED-LLM:

## Overview

BED-LLM (Bayesian Experimental Design with Large Language Models) is a general-purpose approach for improving the ability of LLMs to intelligently and adaptively gather information from a user or other external source using the framework of sequential Bayesian experimental design, and the paper was accepted at ICLR.

## Core Methodology

The approach is based on iteratively choosing questions or queries that maximize the expected information gain (EIG) with respect to a variable of interest given the responses gathered previously. This enables LLMs to act as effective multi-turn conversational agents and interactively interface with external environments.

## Key Innovations

Key innovations include a carefully designed estimator for the EIG, not solely relying on in-context updates for conditioning on previous responses, and a targeted strategy for proposing candidate queries.

## Performance Results

BED-LLM achieves substantial gains in performance across a wide range of tests based on the 20-questions game and using the LLM to actively infer user preferences, compared to direct prompting of the LLM and other adaptive design strategies.

The research involves authors including Deepro Choudhury, Sinead Williamson, Adam Goliński, and others from leading institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeeb40a6-9ddf-4de3-994f-42aca5351aa7",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "c5169aa4-79ac-4e95-abdd-3dfb58794eef",
  "toolUseResult": {
    "query": "BED-LLM Bayesian experimental design language models preference elicitation ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KU7Kcx9Nd83JtGrMATBfeU",
        "content": [
          {
            "title": "[2508.21184] BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design",
            "url": "https://arxiv.org/abs/2508.21184"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design [Quick Review]",
            "url": "https://liner.com/review/bedllm-intelligent-information-gathering-with-llms-and-bayesian-experimental-design"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/bed-llm"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | OpenReview",
            "url": "https://openreview.net/forum?id=qyylZMLYT8"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design",
            "url": "https://arxiv.org/html/2508.21184v1"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | Request PDF",
            "url": "https://www.researchgate.net/publication/395125168_BED-LLM_Intelligent_Information_Gathering_with_LLMs_and_Bayesian_Experimental_Design"
          },
          {
            "title": "BED-LLM: INTELLIGENT INFORMATION GATHERING",
            "url": "https://openreview.net/pdf?id=qyylZMLYT8"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 TOWARD EFFICIENT EXPLORATION",
            "url": "https://dilipa.github.io/papers/iclr26_psrl_llms.pdf"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/bed-llm-intelligent-information-gathering-llms-bayesian"
          }
        ]
      },
      "Based on the search results, here's information about BED-LLM:\n\n## Overview\n\nBED-LLM (Bayesian Experimental Design with Large Language Models) is a general-purpose approach for improving the ability of LLMs to intelligently and adaptively gather information from a user or other external source using the framework of sequential Bayesian experimental design, and the paper was accepted at ICLR.\n\n## Core Methodology\n\nThe approach is based on iteratively choosing questions or queries that maximize the expected information gain (EIG) with respect to a variable of interest given the responses gathered previously. This enables LLMs to act as effective multi-turn conversational agents and interactively interface with external environments.\n\n## Key Innovations\n\nKey innovations include a carefully designed estimator for the EIG, not solely relying on in-context updates for conditioning on previous responses, and a targeted strategy for proposing candidate queries.\n\n## Performance Results\n\nBED-LLM achieves substantial gains in performance across a wide range of tests based on the 20-questions game and using the LLM to actively infer user preferences, compared to direct prompting of the LLM and other adaptive design strategies.\n\nThe research involves authors including Deepro Choudhury, Sinead Williamson, Adam Goliński, and others from leading institutions."
    ],
    "durationSeconds": 6.288270244
  },
  "sourceToolAssistantUUID": "aeeb40a6-9ddf-4de3-994f-42aca5351aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T08:11:12.808Z_

<details><summary>↩ Tool result · `toolu_01WS4MnevuWQpB9vGS4tYj4m`</summary>

```text
Web search results for query: "FABEL falsification binary elicitation LLM personalization arXiv 2026"

Links: [{"title":"Toward Personalized LLM-Powered Agents:","url":"https://arxiv.org/pdf/2602.22680v1"},{"title":"Published at ICLR 2026 Workshop on Agents in the Wild","url":"https://arxiv.org/pdf/2604.22080"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/bayesian-optimization-llm-based-acquisition-functions-natural"},{"title":"Minimum Specification Perturbation: Robustness as Distance-to-Falsification in Causal Inference","url":"https://arxiv.org/html/2605.01579"},{"title":"Frontier Lag: A Bibliometric Audit of Capability MisrepresentationMisrepresentation is used in the corpus-level sense of claim-scope mismatch, not as an allegation of intent or individual-author bad faith; the targets are reporting norms and structural incentives. in Academic AI Evaluation","url":"https://arxiv.org/html/2605.04135"},{"title":"A Survey of Personalized Large Language Models: Progress and Future Directions","url":"https://arxiv.org/html/2502.11528v2"},{"title":"Stayin’ Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data","url":"https://arxiv.org/html/2605.04029"},{"title":"[2601.11000] When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs","url":"https://arxiv.org/abs/2601.11000"},{"title":"Accepted as a conference paper at ICLR 2026 Workshop on MALGAI","url":"https://arxiv.org/pdf/2603.03565"},{"title":"[2505.11839] On the Eligibility of LLMs for Counterfactual Reasoning: A Decompositional Study","url":"https://arxiv.org/abs/2505.11839"}]

Based on the search results, I found several papers from arXiv 2026 related to LLM personalization and elicitation, though I did not find a specific paper with the exact title "FABEL" combining those specific terms. However, the search did return relevant papers on related topics:

**Papers found on related topics:**

1. Personalized Large Language Models (PLLMs) address challenges where LLMs struggle with user-specific personalization by leveraging individual user data to deliver contextually relevant responses tailored to each user's specific needs.

2. A 2026 paper discusses how personalized LLMs can inadvertently distort factual reasoning, with the model generating answers aligned with a user's prior history rather than objective truth, creating personalization-induced hallucinations.

3. Research on longitudinal human-LLM alignment emphasizes that understanding how user preferences change over time requires more than simply repeated preference elicitation, and also depends on contextual signals about what users do after interacting with an LLM.

4. One paper discusses targeted attempts at falsification in the context of LLM agents in biomedical research.

The specific "FABEL" paper with the exact combination of falsification, binary elicitation, and personalization does not appear in these search results. If you're looking for a specific FABEL paper, it may use different terminology or may not yet be indexed in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65425956-d076-431f-982e-45d09bafa5ea",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "44ecf6ca-63d2-4c4f-949a-ac7fecb587ce",
  "toolUseResult": {
    "query": "FABEL falsification binary elicitation LLM personalization arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WypTcoKLqNBaKeqEyt6mCB",
        "content": [
          {
            "title": "Toward Personalized LLM-Powered Agents:",
            "url": "https://arxiv.org/pdf/2602.22680v1"
          },
          {
            "title": "Published at ICLR 2026 Workshop on Agents in the Wild",
            "url": "https://arxiv.org/pdf/2604.22080"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/bayesian-optimization-llm-based-acquisition-functions-natural"
          },
          {
            "title": "Minimum Specification Perturbation: Robustness as Distance-to-Falsification in Causal Inference",
            "url": "https://arxiv.org/html/2605.01579"
          },
          {
            "title": "Frontier Lag: A Bibliometric Audit of Capability MisrepresentationMisrepresentation is used in the corpus-level sense of claim-scope mismatch, not as an allegation of intent or individual-author bad faith; the targets are reporting norms and structural incentives. in Academic AI Evaluation",
            "url": "https://arxiv.org/html/2605.04135"
          },
          {
            "title": "A Survey of Personalized Large Language Models: Progress and Future Directions",
            "url": "https://arxiv.org/html/2502.11528v2"
          },
          {
            "title": "Stayin’ Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data",
            "url": "https://arxiv.org/html/2605.04029"
          },
          {
            "title": "[2601.11000] When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs",
            "url": "https://arxiv.org/abs/2601.11000"
          },
          {
            "title": "Accepted as a conference paper at ICLR 2026 Workshop on MALGAI",
            "url": "https://arxiv.org/pdf/2603.03565"
          },
          {
            "title": "[2505.11839] On the Eligibility of LLMs for Counterfactual Reasoning: A Decompositional Study",
            "url": "https://arxiv.org/abs/2505.11839"
          }
        ]
      },
      "Based on the search results, I found several papers from arXiv 2026 related to LLM personalization and elicitation, though I did not find a specific paper with the exact title \"FABEL\" combining those specific terms. However, the search did return relevant papers on related topics:\n\n**Papers found on related topics:**\n\n1. Personalized Large Language Models (PLLMs) address challenges where LLMs struggle with user-specific personalization by leveraging individual user data to deliver contextually relevant responses tailored to each user's specific needs.\n\n2. A 2026 paper discusses how personalized LLMs can inadvertently distort factual reasoning, with the model generating answers aligned with a user's prior history rather than objective truth, creating personalization-induced hallucinations.\n\n3. Research on longitudinal human-LLM alignment emphasizes that understanding how user preferences change over time requires more than simply repeated preference elicitation, and also depends on contextual signals about what users do after interacting with an LLM.\n\n4. One paper discusses targeted attempts at falsification in the context of LLM agents in biomedical research.\n\nThe specific \"FABEL\" paper with the exact combination of falsification, binary elicitation, and personalization does not appear in these search results. If you're looking for a specific FABEL paper, it may use different terminology or may not yet be indexed in the search results."
    ],
    "durationSeconds": 11.575743664
  },
  "sourceToolAssistantUUID": "65425956-d076-431f-982e-45d09bafa5ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
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
  "leafUuid": "44ecf6ca-63d2-4c4f-949a-ac7fecb587ce",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Assistant

_source line 21 · 2026-05-10T08:11:15.551Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me search for more recent concurrent work that might threaten the novelty of FABEL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44ecf6ca-63d2-4c4f-949a-ac7fecb587ce",
  "isSidechain": false,
  "requestId": "req_011CatYrqx1Sgbj4fwkytQKF",
  "type": "assistant",
  "uuid": "73753424-ffd0-4fb9-bc56-ea2f19932b37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0154o1tA92ekYemC5KraLLkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 910,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 44634,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 910,
          "output_tokens": 236,
          "cache_read_input_tokens": 44634,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 22 · 2026-05-10T08:11:16.473Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xhw3wd6PUGueHz9hBsrCZV`</summary>

```json
{
  "query": "demonstration-grounded Bayesian preference elicitation warm prior LLM personalization 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73753424-ffd0-4fb9-bc56-ea2f19932b37",
  "isSidechain": false,
  "requestId": "req_011CatYrqx1Sgbj4fwkytQKF",
  "type": "assistant",
  "uuid": "729f6fcf-4ab5-4af9-9c07-8128a5f70bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0154o1tA92ekYemC5KraLLkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 910,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 44634,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 910,
          "output_tokens": 236,
          "cache_read_input_tokens": 44634,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 23 · 2026-05-10T08:11:17.168Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDiA96y8aBEpfRy2mj1ECk`</summary>

```json
{
  "query": "PROSE \"predicting preferences\" user writing samples LLM alignment arXiv 2505.23815 ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "729f6fcf-4ab5-4af9-9c07-8128a5f70bd2",
  "isSidechain": false,
  "requestId": "req_011CatYrqx1Sgbj4fwkytQKF",
  "type": "assistant",
  "uuid": "7622e437-a1f5-4a50-acca-810d8c1871ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0154o1tA92ekYemC5KraLLkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 910,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 44634,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 910,
          "output_tokens": 236,
          "cache_read_input_tokens": 44634,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 24 · 2026-05-10T08:11:17.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SW5ejabuqZZouZbmBevAdp`</summary>

```json
{
  "query": "PersonalLLM benchmark ICLR 2025 simulated user preference evaluation reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7622e437-a1f5-4a50-acca-810d8c1871ca",
  "isSidechain": false,
  "requestId": "req_011CatYrqx1Sgbj4fwkytQKF",
  "type": "assistant",
  "uuid": "d9893c8a-aa84-4661-8be1-f892280e9c2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0154o1tA92ekYemC5KraLLkS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 910,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 44634,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 910,
          "output_tokens": 236,
          "cache_read_input_tokens": 44634,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2030
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

_source line 25 · 2026-05-10T08:11:24.364Z_

<details><summary>↩ Tool result · `toolu_01Xhw3wd6PUGueHz9hBsrCZV`</summary>

```text
Web search results for query: "demonstration-grounded Bayesian preference elicitation warm prior LLM personalization 2025 2026 arXiv"

Links: [{"title":"LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation","url":"https://arxiv.org/html/2508.03766v1"},{"title":"Bayesian Preference Elicitation with Language Models","url":"https://arxiv.org/html/2403.05534v1"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation","url":"https://arxiv.org/html/2405.00981v1"},{"title":"Cold-Start Personalization via Training-Free Priors from Structured World Models","url":"https://arxiv.org/html/2602.15012"},{"title":"[2405.00981] Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation","url":"https://arxiv.org/abs/2405.00981"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/bayesian-optimization-llm-based-acquisition-functions-natural"},{"title":"[2403.05534] Bayesian Preference Elicitation with Language Models","url":"https://arxiv.org/abs/2403.05534"},{"title":"LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models","url":"https://arxiv.org/html/2508.08300v1"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for","url":"https://arxiv.org/pdf/2405.00981"},{"title":"Using Large Language Models for Expert Prior Elicitation in Predictive Modelling","url":"https://arxiv.org/html/2411.17284v1"}]

I found several highly relevant papers from arXiv related to Bayesian preference elicitation, warm priors, and LLM personalization from 2024-2026:

## Key Findings:

1. **Cold-Start Personalization via Training-Free Priors** (February 2026) - This work proposes Pep, a modular framework that decomposes cold-start elicitation into offline world model learning with dense supervision and online Bayesian inference, adapting active collaborative filtering to LLM personalization.

2. **Bayesian Preference Elicitation with Language Models** (March 2024) - OPEN is a framework that uses Bayesian Optimal Experimental Design (BOED) to guide the choice of informative questions and a language model to extract features and translate abstract BOED queries into natural language questions. By combining the flexibility of LMs with the rigor of BOED, OPEN can optimize the informativity of queries while remaining adaptable to real-world domains.

3. **LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation** (August 2025) - LLMPrior is a novel framework for automating and scaling the elicitation and aggregation of prior distributions using Large Language Models, with a principled operator that translates unstructured context into a valid, tractable PDF by architecturally coupling an LLM with an explicit generative model.

4. **Using Large Language Models for Expert Prior Elicitation in Predictive Modelling** (November 2024) - By providing language models with training demonstrations, researchers extract the LLM's in-context predictive parameter posterior distribution through Monte Carlo sampling, finding that the language is inconsistent in its approximation of Bayesian inference, with reliability depending on the task.

These papers directly address demonstration-grounded approaches, warm prior initialization, and Bayesian inference in LLM personalization systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "729f6fcf-4ab5-4af9-9c07-8128a5f70bd2",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "9f0a7387-7aec-4c7c-887a-c519be12467b",
  "toolUseResult": {
    "query": "demonstration-grounded Bayesian preference elicitation warm prior LLM personalization 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DU8vJC2eByYxmH6vGuJGUx",
        "content": [
          {
            "title": "LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation",
            "url": "https://arxiv.org/html/2508.03766v1"
          },
          {
            "title": "Bayesian Preference Elicitation with Language Models",
            "url": "https://arxiv.org/html/2403.05534v1"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation",
            "url": "https://arxiv.org/html/2405.00981v1"
          },
          {
            "title": "Cold-Start Personalization via Training-Free Priors from Structured World Models",
            "url": "https://arxiv.org/html/2602.15012"
          },
          {
            "title": "[2405.00981] Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation",
            "url": "https://arxiv.org/abs/2405.00981"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/bayesian-optimization-llm-based-acquisition-functions-natural"
          },
          {
            "title": "[2403.05534] Bayesian Preference Elicitation with Language Models",
            "url": "https://arxiv.org/abs/2403.05534"
          },
          {
            "title": "LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models",
            "url": "https://arxiv.org/html/2508.08300v1"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for",
            "url": "https://arxiv.org/pdf/2405.00981"
          },
          {
            "title": "Using Large Language Models for Expert Prior Elicitation in Predictive Modelling",
            "url": "https://arxiv.org/html/2411.17284v1"
          }
        ]
      },
      "I found several highly relevant papers from arXiv related to Bayesian preference elicitation, warm priors, and LLM personalization from 2024-2026:\n\n## Key Findings:\n\n1. **Cold-Start Personalization via Training-Free Priors** (February 2026) - This work proposes Pep, a modular framework that decomposes cold-start elicitation into offline world model learning with dense supervision and online Bayesian inference, adapting active collaborative filtering to LLM personalization.\n\n2. **Bayesian Preference Elicitation with Language Models** (March 2024) - OPEN is a framework that uses Bayesian Optimal Experimental Design (BOED) to guide the choice of informative questions and a language model to extract features and translate abstract BOED queries into natural language questions. By combining the flexibility of LMs with the rigor of BOED, OPEN can optimize the informativity of queries while remaining adaptable to real-world domains.\n\n3. **LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation** (August 2025) - LLMPrior is a novel framework for automating and scaling the elicitation and aggregation of prior distributions using Large Language Models, with a principled operator that translates unstructured context into a valid, tractable PDF by architecturally coupling an LLM with an explicit generative model.\n\n4. **Using Large Language Models for Expert Prior Elicitation in Predictive Modelling** (November 2024) - By providing language models with training demonstrations, researchers extract the LLM's in-context predictive parameter posterior distribution through Monte Carlo sampling, finding that the language is inconsistent in its approximation of Bayesian inference, with reliability depending on the task.\n\nThese papers directly address demonstration-grounded approaches, warm prior initialization, and Bayesian inference in LLM personalization systems."
    ],
    "durationSeconds": 7.886779295
  },
  "sourceToolAssistantUUID": "729f6fcf-4ab5-4af9-9c07-8128a5f70bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T08:11:25.052Z_

<details><summary>↩ Tool result · `toolu_01RDiA96y8aBEpfRy2mj1ECk`</summary>

```text
Web search results for query: "PROSE "predicting preferences" user writing samples LLM alignment arXiv 2505.23815 ICML 2025"

Links: [{"title":"[2505.23815] Aligning LLMs by Predicting Preferences from User Writing Samples","url":"https://arxiv.org/abs/2505.23815"},{"title":"Aligning LLMs by Predicting Preferences from User Writing Samples","url":"https://arxiv.org/html/2505.23815v1"},{"title":"Aligning LLMs by Predicting Preferences from User Writing Samples | OpenReview","url":"https://openreview.net/forum?id=eUMGCipgtE"},{"title":"Aligning LLMs by Predicting Preferences from User Writing Samples | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/aligning-llms-by-predicting-preferences-user-writing"},{"title":"Aligning LLMs by Predicting Preferences from User Writing Samples - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/predicting-preferences"},{"title":"Aligning LLMs by Predicting Preferences from User Writing ...","url":"https://bytez.com/docs/arxiv/2505.23815/paper"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1925&show=2000"},{"title":"Aligning LLMs by Predicting Preferences from User Writing Samples","url":"https://openreview.net/pdf/d6c98d214568eddf2a75033d95d4dda21396f9c3.pdf"},{"title":"A Survey of Personalized Large Language Models: Progress and Future Directions","url":"https://arxiv.org/html/2502.11528v2"},{"title":"Aligning LLM Agents by Learning Latent Preference from User Edits | OpenReview","url":"https://openreview.net/forum?id=DlYNGpCuwa"}]

I found comprehensive information about this paper. Here's what I found:

## PROSE Paper Summary

PROSE is a method designed to enhance the precision of preference descriptions inferred from user writing samples, incorporating iterative refinement of inferred preferences and verification of inferred preferences across multiple user writing samples.

### Key Motivation

Accommodating human preferences is essential for creating aligned LLM agents that deliver personalized and effective interactions. Recent work has shown the potential for LLMs acting as writing agents to infer a description of user preferences, with agent alignment coming from conditioning on the inferred preference description. However, existing methods often produce generic preference descriptions that fail to capture the unique and individualized nature of human preferences.

### Evaluation and Results

The paper evaluates PROSE with several LLMs (Qwen2.5 7B and 72B Instruct, GPT-mini, and GPT-4o) on a summarization and an email writing task. PROSE more accurately infers nuanced human preferences, improving the quality of the writing agent's generations over CIPHER (a state-of-the-art method for inferring preferences) by 33%. Additionally, ICL and PROSE are complementary methods, and combining them provides up to a 9% improvement over ICL alone.

### Publication Status

The paper was accepted to ICML 2025. The arXiv identifier is 2505.23815, with a submission date of May 27, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7622e437-a1f5-4a50-acca-810d8c1871ca",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "af68443b-b3af-4754-8700-c789d3ff7eec",
  "toolUseResult": {
    "query": "PROSE \"predicting preferences\" user writing samples LLM alignment arXiv 2505.23815 ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SdKUHCDwtuMzjJquCPjFmo",
        "content": [
          {
            "title": "[2505.23815] Aligning LLMs by Predicting Preferences from User Writing Samples",
            "url": "https://arxiv.org/abs/2505.23815"
          },
          {
            "title": "Aligning LLMs by Predicting Preferences from User Writing Samples",
            "url": "https://arxiv.org/html/2505.23815v1"
          },
          {
            "title": "Aligning LLMs by Predicting Preferences from User Writing Samples | OpenReview",
            "url": "https://openreview.net/forum?id=eUMGCipgtE"
          },
          {
            "title": "Aligning LLMs by Predicting Preferences from User Writing Samples | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/aligning-llms-by-predicting-preferences-user-writing"
          },
          {
            "title": "Aligning LLMs by Predicting Preferences from User Writing Samples - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/predicting-preferences"
          },
          {
            "title": "Aligning LLMs by Predicting Preferences from User Writing ...",
            "url": "https://bytez.com/docs/arxiv/2505.23815/paper"
          },
          {
            "title": "Computation and Language May 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-05?skip=1925&show=2000"
          },
          {
            "title": "Aligning LLMs by Predicting Preferences from User Writing Samples",
            "url": "https://openreview.net/pdf/d6c98d214568eddf2a75033d95d4dda21396f9c3.pdf"
          },
          {
            "title": "A Survey of Personalized Large Language Models: Progress and Future Directions",
            "url": "https://arxiv.org/html/2502.11528v2"
          },
          {
            "title": "Aligning LLM Agents by Learning Latent Preference from User Edits | OpenReview",
            "url": "https://openreview.net/forum?id=DlYNGpCuwa"
          }
        ]
      },
      "I found comprehensive information about this paper. Here's what I found:\n\n## PROSE Paper Summary\n\nPROSE is a method designed to enhance the precision of preference descriptions inferred from user writing samples, incorporating iterative refinement of inferred preferences and verification of inferred preferences across multiple user writing samples.\n\n### Key Motivation\n\nAccommodating human preferences is essential for creating aligned LLM agents that deliver personalized and effective interactions. Recent work has shown the potential for LLMs acting as writing agents to infer a description of user preferences, with agent alignment coming from conditioning on the inferred preference description. However, existing methods often produce generic preference descriptions that fail to capture the unique and individualized nature of human preferences.\n\n### Evaluation and Results\n\nThe paper evaluates PROSE with several LLMs (Qwen2.5 7B and 72B Instruct, GPT-mini, and GPT-4o) on a summarization and an email writing task. PROSE more accurately infers nuanced human preferences, improving the quality of the writing agent's generations over CIPHER (a state-of-the-art method for inferring preferences) by 33%. Additionally, ICL and PROSE are complementary methods, and combining them provides up to a 9% improvement over ICL alone.\n\n### Publication Status\n\nThe paper was accepted to ICML 2025. The arXiv identifier is 2505.23815, with a submission date of May 27, 2025."
    ],
    "durationSeconds": 7.880701228999999
  },
  "sourceToolAssistantUUID": "7622e437-a1f5-4a50-acca-810d8c1871ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T08:11:25.802Z_

<details><summary>↩ Tool result · `toolu_01SW5ejabuqZZouZbmBevAdp`</summary>

```text
Web search results for query: "PersonalLLM benchmark ICLR 2025 simulated user preference evaluation reward model"

Links: [{"title":"Published as a conference paper at ICLR 2025 PERSONALLLM:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf"},{"title":"ICLR Poster PersonalLLM: Tailoring LLMs to Individual Preferences","url":"https://iclr.cc/virtual/2025/poster/32110"},{"title":"PersonalLLM: Tailoring LLMs to Individual Preferences | OpenReview","url":"https://openreview.net/forum?id=2R7498e2Tx"},{"title":"1 Introduction","url":"https://arxiv.org/html/2409.20296"},{"title":"Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization","url":"https://arxiv.org/html/2604.07343v1"},{"title":"REWARD MODELS ARE METRICS IN A TRENCH COAT","url":"https://openreview.net/pdf/433f58bfdb3e151dac7ee7387af7abd16e3a0940.pdf"},{"title":"Reward Modeling for Human Preferences Evan Frick","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-82.pdf"},{"title":"Published as a conference paper at ICLR 2025 REWARD LEARNING FROM","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/6fef0af0e30ae22d63e362b2ff6a2e3e-Paper-Conference.pdf"},{"title":"JudgeBench: A Benchmark for Evaluating LLM-Based ...","url":"https://iclr.cc/virtual/2025/poster/30311"},{"title":"Published as a conference paper at ICLR 2025","url":"https://nlpr.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-ICLR.pdf"}]

Based on the search results, I found comprehensive information about PersonalLLM, which was published at ICLR 2025:

## PersonalLLM: Benchmark Overview

PersonalLLM is a public benchmark focusing on adapting LLMs to provide maximal benefits for a particular user.

### Key Components

The PersonalLLM testbed is composed of two high-level components: 1) a dataset of prompts, each paired with a set of high-quality responses among which humans would be expected to display diverse preferences and 2) a method for sampling diverse personal preference models, such that methods for personalization can be tested.

### Simulated User Preference Evaluation

A critical innovation of PersonalLLM is its approach to simulating diverse users:

The framework leverages reward models to sample many synthetic "users" (or personal preference models) via weighted ensembles of their preferences, and in doing so simulates an entire user base, which is argued to be a critical ingredient in a truly useful personalization benchmark.

These reward models are built on top of popular base models such as Llama3, Mistral, and Gemma.

### Advantages Over Existing Methods

Instead of persona prompting LLMs based on high-level attributes (e.g., user race or response length), which yields homogeneous preferences relative to humans, the benchmark develops a method that can simulate a large user base with diverse preferences from a set of pre-trained reward models.

Persona prompting baseline produces preferences only half as diverse as a set of PersonalLLM users across multiple metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9893c8a-aa84-4661-8be1-f892280e9c2a",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "ea475a53-6422-4135-a8e5-21b154ef41b1",
  "toolUseResult": {
    "query": "PersonalLLM benchmark ICLR 2025 simulated user preference evaluation reward model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dqbvudb44pbbQvjP8mXx3n",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 PERSONALLLM:",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf"
          },
          {
            "title": "ICLR Poster PersonalLLM: Tailoring LLMs to Individual Preferences",
            "url": "https://iclr.cc/virtual/2025/poster/32110"
          },
          {
            "title": "PersonalLLM: Tailoring LLMs to Individual Preferences | OpenReview",
            "url": "https://openreview.net/forum?id=2R7498e2Tx"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2409.20296"
          },
          {
            "title": "Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization",
            "url": "https://arxiv.org/html/2604.07343v1"
          },
          {
            "title": "REWARD MODELS ARE METRICS IN A TRENCH COAT",
            "url": "https://openreview.net/pdf/433f58bfdb3e151dac7ee7387af7abd16e3a0940.pdf"
          },
          {
            "title": "Reward Modeling for Human Preferences Evan Frick",
            "url": "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-82.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 REWARD LEARNING FROM",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/6fef0af0e30ae22d63e362b2ff6a2e3e-Paper-Conference.pdf"
          },
          {
            "title": "JudgeBench: A Benchmark for Evaluating LLM-Based ...",
            "url": "https://iclr.cc/virtual/2025/poster/30311"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://nlpr.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-ICLR.pdf"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about PersonalLLM, which was published at ICLR 2025:\n\n## PersonalLLM: Benchmark Overview\n\nPersonalLLM is a public benchmark focusing on adapting LLMs to provide maximal benefits for a particular user.\n\n### Key Components\n\nThe PersonalLLM testbed is composed of two high-level components: 1) a dataset of prompts, each paired with a set of high-quality responses among which humans would be expected to display diverse preferences and 2) a method for sampling diverse personal preference models, such that methods for personalization can be tested.\n\n### Simulated User Preference Evaluation\n\nA critical innovation of PersonalLLM is its approach to simulating diverse users:\n\nThe framework leverages reward models to sample many synthetic \"users\" (or personal preference models) via weighted ensembles of their preferences, and in doing so simulates an entire user base, which is argued to be a critical ingredient in a truly useful personalization benchmark.\n\nThese reward models are built on top of popular base models such as Llama3, Mistral, and Gemma.\n\n### Advantages Over Existing Methods\n\nInstead of persona prompting LLMs based on high-level attributes (e.g., user race or response length), which yields homogeneous preferences relative to humans, the benchmark develops a method that can simulate a large user base with diverse preferences from a set of pre-trained reward models.\n\nPersona prompting baseline produces preferences only half as diverse as a set of PersonalLLM users across multiple metrics."
    ],
    "durationSeconds": 8.213845558000001
  },
  "sourceToolAssistantUUID": "d9893c8a-aa84-4661-8be1-f892280e9c2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T08:11:29.238Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me look for more recent work that might threaten the novelty of FABEL, especially any concurrent work from 2026 that the Generator may have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea475a53-6422-4135-a8e5-21b154ef41b1",
  "isSidechain": false,
  "requestId": "req_011CatYsoVh79QVrzTiPg5TR",
  "type": "assistant",
  "uuid": "cd7c83c6-21f6-4bf3-a360-7a176df1160c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DDWfitEr4MDfiWkcWNBELF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 46664,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 46664,
          "cache_creation_input_tokens": 3950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3950
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

_source line 29 · 2026-05-10T08:11:29.314Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByRrXojQUARb3vRw1SetKY`</summary>

```json
{
  "query": "warm start Bayesian prior LLM personalization user demonstrations style elicitation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd7c83c6-21f6-4bf3-a360-7a176df1160c",
  "isSidechain": false,
  "requestId": "req_011CatYsoVh79QVrzTiPg5TR",
  "type": "assistant",
  "uuid": "5dbcecbd-8226-4435-8179-2ccc4774b78e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DDWfitEr4MDfiWkcWNBELF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 46664,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 46664,
          "cache_creation_input_tokens": 3950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3950
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

_source line 30 · 2026-05-10T08:11:29.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JTRVTWAuz5EzFAfD4UXVUN`</summary>

```json
{
  "query": "disconfirmation probe hypothesis testing preference elicitation binary confirmation LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dbcecbd-8226-4435-8179-2ccc4774b78e",
  "isSidechain": false,
  "requestId": "req_011CatYsoVh79QVrzTiPg5TR",
  "type": "assistant",
  "uuid": "5a7862da-e845-4614-8d61-ba15f315022f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DDWfitEr4MDfiWkcWNBELF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 46664,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 46664,
          "cache_creation_input_tokens": 3950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3950
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

_source line 31 · 2026-05-10T08:11:35.277Z_

<details><summary>↩ Tool result · `toolu_01ByRrXojQUARb3vRw1SetKY`</summary>

```text
Web search results for query: "warm start Bayesian prior LLM personalization user demonstrations style elicitation 2026 arXiv"

Links: [{"title":"LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation","url":"https://arxiv.org/html/2508.03766v1"},{"title":"LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models","url":"https://arxiv.org/html/2508.08300v1"},{"title":"Using Large Language Models for Expert Prior Elicitation in Predictive Modelling","url":"https://arxiv.org/html/2411.17284v1"},{"title":"Bayesian Elicitation with LLMs: Model Size Helps, Extra \"Reasoning\" Doesn’t Always","url":"https://arxiv.org/html/2604.01896v1"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation","url":"https://arxiv.org/html/2405.00981"},{"title":"Large Language Model–Derived Priors Can Improve Bayesian Survival Analyses: A Glioblastoma Application","url":"https://arxiv.org/html/2511.01778v1"},{"title":"[2508.03766] LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation","url":"https://arxiv.org/abs/2508.03766"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for","url":"https://arxiv.org/pdf/2405.00981"},{"title":"Bayesian Orchestration of Multi-LLM Agents for Cost-Aware Sequential Decision-Making","url":"https://arxiv.org/html/2601.01522v1"},{"title":"[2405.00981] Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation","url":"https://arxiv.org/abs/2405.00981"}]

I've found several highly relevant arXiv papers on your search query. Here are the key results:

## Recent 2026 and 2025 Papers

Recent research investigates whether LLMs can serve as Bayesian elicitation assistants, constructing question sets from four real-world datasets spanning psychology (Big Five personality traits), public health (NHANES, NCD-RisC), and labor markets (Glassdoor).

LLM-Prior is a novel framework for automating and scaling the elicitation and aggregation of prior distributions using Large Language Models.

## LLM-Based Prior Elicitation

Research demonstrates that an LLM can successfully elicit prior distributions from natural language and can specify the entire model structure, including both priors and the likelihood, from a single high-level problem description.

## Personalization & User Demonstrations

Designing preference elicitation methodologies that can quickly ascertain a user's top item preferences in a cold-start setting is a key challenge for building effective and personalized conversational recommendation systems, with the hypothesis that LLM approaches lack the multi-turn, decision-theoretic reasoning required to effectively balance exploration and exploitation of user preferences.

The search results include papers from August 2025 (LLM-Prior), April 2026 (Bayesian Elicitation with LLMs), and other recent work exploring the intersection of Bayesian priors, LLM-based elicitation, and personalization through user demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dbcecbd-8226-4435-8179-2ccc4774b78e",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "a7d56884-7341-4e9e-abef-a7b055910c99",
  "toolUseResult": {
    "query": "warm start Bayesian prior LLM personalization user demonstrations style elicitation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F8BmDMXzqavWpcTX4Mc224",
        "content": [
          {
            "title": "LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation",
            "url": "https://arxiv.org/html/2508.03766v1"
          },
          {
            "title": "LLM-BI: Towards Fully Automated Bayesian Inference with Large Language Models",
            "url": "https://arxiv.org/html/2508.08300v1"
          },
          {
            "title": "Using Large Language Models for Expert Prior Elicitation in Predictive Modelling",
            "url": "https://arxiv.org/html/2411.17284v1"
          },
          {
            "title": "Bayesian Elicitation with LLMs: Model Size Helps, Extra \"Reasoning\" Doesn’t Always",
            "url": "https://arxiv.org/html/2604.01896v1"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation",
            "url": "https://arxiv.org/html/2405.00981"
          },
          {
            "title": "Large Language Model–Derived Priors Can Improve Bayesian Survival Analyses: A Glioblastoma Application",
            "url": "https://arxiv.org/html/2511.01778v1"
          },
          {
            "title": "[2508.03766] LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation",
            "url": "https://arxiv.org/abs/2508.03766"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for",
            "url": "https://arxiv.org/pdf/2405.00981"
          },
          {
            "title": "Bayesian Orchestration of Multi-LLM Agents for Cost-Aware Sequential Decision-Making",
            "url": "https://arxiv.org/html/2601.01522v1"
          },
          {
            "title": "[2405.00981] Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation",
            "url": "https://arxiv.org/abs/2405.00981"
          }
        ]
      },
      "I've found several highly relevant arXiv papers on your search query. Here are the key results:\n\n## Recent 2026 and 2025 Papers\n\nRecent research investigates whether LLMs can serve as Bayesian elicitation assistants, constructing question sets from four real-world datasets spanning psychology (Big Five personality traits), public health (NHANES, NCD-RisC), and labor markets (Glassdoor).\n\nLLM-Prior is a novel framework for automating and scaling the elicitation and aggregation of prior distributions using Large Language Models.\n\n## LLM-Based Prior Elicitation\n\nResearch demonstrates that an LLM can successfully elicit prior distributions from natural language and can specify the entire model structure, including both priors and the likelihood, from a single high-level problem description.\n\n## Personalization & User Demonstrations\n\nDesigning preference elicitation methodologies that can quickly ascertain a user's top item preferences in a cold-start setting is a key challenge for building effective and personalized conversational recommendation systems, with the hypothesis that LLM approaches lack the multi-turn, decision-theoretic reasoning required to effectively balance exploration and exploitation of user preferences.\n\nThe search results include papers from August 2025 (LLM-Prior), April 2026 (Bayesian Elicitation with LLMs), and other recent work exploring the intersection of Bayesian priors, LLM-based elicitation, and personalization through user demonstrations."
    ],
    "durationSeconds": 5.958400475000002
  },
  "sourceToolAssistantUUID": "5dbcecbd-8226-4435-8179-2ccc4774b78e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a7d56884-7341-4e9e-abef-a7b055910c99",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Tool result

_source line 34 · 2026-05-10T08:11:36.661Z_

<details><summary>↩ Tool result · `toolu_01JTRVTWAuz5EzFAfD4UXVUN`</summary>

```text
Web search results for query: "disconfirmation probe hypothesis testing preference elicitation binary confirmation LLM 2026"

Links: [{"title":"Confirmation, Framing, and Position Biases in LLM Responses | Proceedings of the 2026 Conference on Human Information Interaction and Retrieval","url":"https://dl.acm.org/doi/10.1145/3786304.3787879"},{"title":"(PDF) Confirmation, Disconfirmation, and Information in Hypothesis Testing","url":"https://www.researchgate.net/publication/232524779_Confirmation_disconfirmation_and_information_in_hypothesis_testing"},{"title":"IFLA Trend Report -- Confirmation, Disconfirmation, and Information in Hypothesis Testing","url":"https://trends.ifla.org/node/33"},{"title":"3 Challenges and 2 Hopes for the Safety of Unsupervised Elicitation","url":"https://alignment.anthropic.com/2026/challenges-hopes/"},{"title":"arXiv:2305.02531v6 [cs.CL] 29 Feb 2024 Can LLMs Capture Human Preferences? ∗","url":"https://arxiv.org/pdf/2305.02531"},{"title":"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models","url":"https://arxiv.org/html/2604.02485"},{"title":"Confirmation, disconfirmation, and information in hypothesis ...","url":"https://psycnet.apa.org/record/1987-20689-001"},{"title":"Prospect Theory Fails for LLMs: Revealing Instability of Decision-Making under Epistemic Uncertainty","url":"https://arxiv.org/html/2508.08992"},{"title":"SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing","url":"https://arxiv.org/html/2603.01630"},{"title":"Detecting implicit biases of large language models with Bayesian hypothesis testing | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-95825-x"}]

Based on the search results, here's what I found related to your query about disconfirmation probe hypothesis testing, preference elicitation, binary confirmation, and LLMs in 2026:

## Key Findings

Recent work adapted hypothesis testing tasks to evaluate multi-turn reasoning in LLMs, where each episode initializes a hidden Boolean rule over three numbers, and the model may propose up to 30 test triples receiving binary feedback before making a rule guess, framing it as an evaluation benchmark for reasoning and hypothesis exploration abilities in LLMs.

A larger-scale dataset and framework has been introduced to measure confirmation bias in LLMs, with studies examining mitigation strategies for reducing confirmation bias and improving performance.

### Debiasing Interventions

Two debiasing interventions from prior human studies designed to reduce confirmation bias include Think-in-Opposites, which introduces a metacognitive strategy where participants are instructed to identify a salient feature and deliberately test an instance that is "opposite" with respect to that feature. Another approach called Dual-Goal rephrases the task to guess two rules, encouraging both confirmatory and disconfirmatory testing to reduce confirmation bias.

### Binary Confirmation in LLM Bias Detection

A novel framework reformulates bias detection in LLMs as a hypothesis testing problem where the null hypothesis represents the absence of implicit bias, leveraging binary-choice questions to measure social bias.

These 2026 papers collectively address confirmation bias in hypothesis testing with LLMs and preference elicitation through binary choice mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a7862da-e845-4614-8d61-ba15f315022f",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "ea47270d-c30b-47e8-b067-8a02e5e6114f",
  "toolUseResult": {
    "query": "disconfirmation probe hypothesis testing preference elicitation binary confirmation LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PVK4BzwuMYS3UEqeH1W9s9",
        "content": [
          {
            "title": "Confirmation, Framing, and Position Biases in LLM Responses | Proceedings of the 2026 Conference on Human Information Interaction and Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3786304.3787879"
          },
          {
            "title": "(PDF) Confirmation, Disconfirmation, and Information in Hypothesis Testing",
            "url": "https://www.researchgate.net/publication/232524779_Confirmation_disconfirmation_and_information_in_hypothesis_testing"
          },
          {
            "title": "IFLA Trend Report -- Confirmation, Disconfirmation, and Information in Hypothesis Testing",
            "url": "https://trends.ifla.org/node/33"
          },
          {
            "title": "3 Challenges and 2 Hopes for the Safety of Unsupervised Elicitation",
            "url": "https://alignment.anthropic.com/2026/challenges-hopes/"
          },
          {
            "title": "arXiv:2305.02531v6 [cs.CL] 29 Feb 2024 Can LLMs Capture Human Preferences? ∗",
            "url": "https://arxiv.org/pdf/2305.02531"
          },
          {
            "title": "Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models",
            "url": "https://arxiv.org/html/2604.02485"
          },
          {
            "title": "Confirmation, disconfirmation, and information in hypothesis ...",
            "url": "https://psycnet.apa.org/record/1987-20689-001"
          },
          {
            "title": "Prospect Theory Fails for LLMs: Revealing Instability of Decision-Making under Epistemic Uncertainty",
            "url": "https://arxiv.org/html/2508.08992"
          },
          {
            "title": "SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing",
            "url": "https://arxiv.org/html/2603.01630"
          },
          {
            "title": "Detecting implicit biases of large language models with Bayesian hypothesis testing | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-95825-x"
          }
        ]
      },
      "Based on the search results, here's what I found related to your query about disconfirmation probe hypothesis testing, preference elicitation, binary confirmation, and LLMs in 2026:\n\n## Key Findings\n\nRecent work adapted hypothesis testing tasks to evaluate multi-turn reasoning in LLMs, where each episode initializes a hidden Boolean rule over three numbers, and the model may propose up to 30 test triples receiving binary feedback before making a rule guess, framing it as an evaluation benchmark for reasoning and hypothesis exploration abilities in LLMs.\n\nA larger-scale dataset and framework has been introduced to measure confirmation bias in LLMs, with studies examining mitigation strategies for reducing confirmation bias and improving performance.\n\n### Debiasing Interventions\n\nTwo debiasing interventions from prior human studies designed to reduce confirmation bias include Think-in-Opposites, which introduces a metacognitive strategy where participants are instructed to identify a salient feature and deliberately test an instance that is \"opposite\" with respect to that feature. Another approach called Dual-Goal rephrases the task to guess two rules, encouraging both confirmatory and disconfirmatory testing to reduce confirmation bias.\n\n### Binary Confirmation in LLM Bias Detection\n\nA novel framework reformulates bias detection in LLMs as a hypothesis testing problem where the null hypothesis represents the absence of implicit bias, leveraging binary-choice questions to measure social bias.\n\nThese 2026 papers collectively address confirmation bias in hypothesis testing with LLMs and preference elicitation through binary choice mechanisms."
    ],
    "durationSeconds": 7.159730618000001
  },
  "sourceToolAssistantUUID": "5a7862da-e845-4614-8d61-ba15f315022f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-10T08:11:36.665Z_

```json
{
  "parentUuid": "ea47270d-c30b-47e8-b067-8a02e5e6114f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "193de5b7-31ae-4f1e-afbd-3bfac6feec9c",
  "timestamp": "2026-05-10T08:11:36.665Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-10T08:11:39.094Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me look for any recent concurrent work from April-May 2026 on user-specific Bayesian preference elicitation, especially any work combining demonstrations + active learning + personalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "193de5b7-31ae-4f1e-afbd-3bfac6feec9c",
  "isSidechain": false,
  "requestId": "req_011CatYtbuDECKNsHBGoKLMM",
  "type": "assistant",
  "uuid": "5acf9ac2-b82b-4309-b9cb-cbe0ee075e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFD5s1SJyFaPPKpDTib8bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 50614,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 50614,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 37 · 2026-05-10T08:11:39.869Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DqhcPRhM9PXYQ3yXSp8xuV`</summary>

```json
{
  "query": "interactive preference learning few-shot demonstrations EIG active selection LLM personalization April May 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5acf9ac2-b82b-4309-b9cb-cbe0ee075e7e",
  "isSidechain": false,
  "requestId": "req_011CatYtbuDECKNsHBGoKLMM",
  "type": "assistant",
  "uuid": "45e40b1d-bf6f-460d-925c-4ab965cc841f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFD5s1SJyFaPPKpDTib8bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 50614,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 50614,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 38 · 2026-05-10T08:11:40.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013hRTZygDMeLr6T9Gay28rz`</summary>

```json
{
  "query": "HyPerAlign hypothesis personalization alignment writing style ICLR 2025 workshop arXiv 2505.00038"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45e40b1d-bf6f-460d-925c-4ab965cc841f",
  "isSidechain": false,
  "requestId": "req_011CatYtbuDECKNsHBGoKLMM",
  "type": "assistant",
  "uuid": "0504de61-2903-4269-9d9e-f9aa49fd054e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFD5s1SJyFaPPKpDTib8bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 50614,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 50614,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 39 · 2026-05-10T08:11:47.924Z_

<details><summary>↩ Tool result · `toolu_013hRTZygDMeLr6T9Gay28rz`</summary>

```text
Web search results for query: "HyPerAlign hypothesis personalization alignment writing style ICLR 2025 workshop arXiv 2505.00038"

Links: [{"title":"[2505.00038v2] HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation","url":"https://arxiv.org/abs/2505.00038v2"},{"title":"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation","url":"https://arxiv.org/html/2505.00038v2"},{"title":"[2505.00038] HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation","url":"https://arxiv.org/abs/2505.00038"},{"title":"HyPerAlign: Personalized LLM Alignment","url":"https://www.emergentmind.com/papers/2505.00038"},{"title":"HyPerAlign: Hypotheses-driven Personalized Alignment","url":"https://arxiv.org/html/2505.00038v1"},{"title":"HyPerAlign: Hypotheses-driven Personalized Alignment","url":"https://www.researchgate.net/publication/391369149_HyPerAlign_Hypotheses-driven_Personalized_Alignment"},{"title":"Published as a conference paper at ICLR 2025 PAD: PERSONALIZED ALIGNMENT","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf"},{"title":"To appear at the ICLR 2025 Workshop on Representational Alignment (Re-Align)","url":"https://openreview.net/pdf?id=4Yag8mHVtc"},{"title":"ICLR 2025 Workshop Re-Align | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2025%2FWorkshop%2FRe-Align"},{"title":"A Survey on Personalized Alignment—The Missing Piece ...","url":"https://aclanthology.org/2025.findings-acl.277.pdf"}]

I've found information about HyPerAlign (arXiv 2505.00038). Here's a summary of the research:

## Overview

HyPerAlign is an interpretable and sample-efficient hypothesis-driven personalization approach for LLM models that infers hypotheses about users' communication strategies, personality, and writing style from few-shot examples.

## Approach

The method consists of two steps: first inferring user-specific attributes such as writing style, strategies employed to convey the message, and distinguishing personality traits, then using the generated hypotheses and descriptions of the user's persona and writing style to customize LLM generations to this specific individual.

## Experimental Results

The research conducts experiments on authorship attribution and deliberative alignment tasks with datasets from diverse domains including news articles, blog posts, emails, and jailbreaking benchmarks, demonstrating the superiority of hypothesis-driven LLM personalization compared to preference-based fine-tuning methods.

For authorship attribution, HyPerAlign generations have consistently high win-rates (commonly >90%) against state-of-the-art preference fine-tuning approaches, and for deliberative alignment, the helpfulness of LLM models is improved by up to 70% on average.

## Key Contribution

Overall, HyPerAlign represents an interpretable and sample-efficient strategy for the personalization of LLM models to individual users.

The paper was posted on arXiv on April 29, 2025, with a second version updated on May 19, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0504de61-2903-4269-9d9e-f9aa49fd054e",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "434429b9-aaa3-45db-9273-3242a0c8fac4",
  "toolUseResult": {
    "query": "HyPerAlign hypothesis personalization alignment writing style ICLR 2025 workshop arXiv 2505.00038",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XbTZWzEN866KEaWHYw8Ztk",
        "content": [
          {
            "title": "[2505.00038v2] HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation",
            "url": "https://arxiv.org/abs/2505.00038v2"
          },
          {
            "title": "HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation",
            "url": "https://arxiv.org/html/2505.00038v2"
          },
          {
            "title": "[2505.00038] HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation",
            "url": "https://arxiv.org/abs/2505.00038"
          },
          {
            "title": "HyPerAlign: Personalized LLM Alignment",
            "url": "https://www.emergentmind.com/papers/2505.00038"
          },
          {
            "title": "HyPerAlign: Hypotheses-driven Personalized Alignment",
            "url": "https://arxiv.org/html/2505.00038v1"
          },
          {
            "title": "HyPerAlign: Hypotheses-driven Personalized Alignment",
            "url": "https://www.researchgate.net/publication/391369149_HyPerAlign_Hypotheses-driven_Personalized_Alignment"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 PAD: PERSONALIZED ALIGNMENT",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf"
          },
          {
            "title": "To appear at the ICLR 2025 Workshop on Representational Alignment (Re-Align)",
            "url": "https://openreview.net/pdf?id=4Yag8mHVtc"
          },
          {
            "title": "ICLR 2025 Workshop Re-Align | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2025%2FWorkshop%2FRe-Align"
          },
          {
            "title": "A Survey on Personalized Alignment—The Missing Piece ...",
            "url": "https://aclanthology.org/2025.findings-acl.277.pdf"
          }
        ]
      },
      "I've found information about HyPerAlign (arXiv 2505.00038). Here's a summary of the research:\n\n## Overview\n\nHyPerAlign is an interpretable and sample-efficient hypothesis-driven personalization approach for LLM models that infers hypotheses about users' communication strategies, personality, and writing style from few-shot examples.\n\n## Approach\n\nThe method consists of two steps: first inferring user-specific attributes such as writing style, strategies employed to convey the message, and distinguishing personality traits, then using the generated hypotheses and descriptions of the user's persona and writing style to customize LLM generations to this specific individual.\n\n## Experimental Results\n\nThe research conducts experiments on authorship attribution and deliberative alignment tasks with datasets from diverse domains including news articles, blog posts, emails, and jailbreaking benchmarks, demonstrating the superiority of hypothesis-driven LLM personalization compared to preference-based fine-tuning methods.\n\nFor authorship attribution, HyPerAlign generations have consistently high win-rates (commonly >90%) against state-of-the-art preference fine-tuning approaches, and for deliberative alignment, the helpfulness of LLM models is improved by up to 70% on average.\n\n## Key Contribution\n\nOverall, HyPerAlign represents an interpretable and sample-efficient strategy for the personalization of LLM models to individual users.\n\nThe paper was posted on arXiv on April 29, 2025, with a second version updated on May 19, 2025."
    ],
    "durationSeconds": 7.133616903999995
  },
  "sourceToolAssistantUUID": "0504de61-2903-4269-9d9e-f9aa49fd054e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T08:11:49.792Z_

<details><summary>↩ Tool result · `toolu_01DqhcPRhM9PXYQ3yXSp8xuV`</summary>

```text
Web search results for query: "interactive preference learning few-shot demonstrations EIG active selection LLM personalization April May 2026 arXiv"

Links: [{"title":"FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users","url":"https://arxiv.org/html/2502.19312v1"},{"title":"[2502.19312] FSPO: Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users","url":"https://arxiv.org/abs/2502.19312"},{"title":"[2410.17233] ICPL: Few-shot In-context Preference Learning via LLMs","url":"https://arxiv.org/abs/2410.17233"},{"title":"POPI: Personalizing LLMs via Optimized Natural Language Preference Inference","url":"https://arxiv.org/html/2510.17881v1"},{"title":"GitHub - Asap7772/fewshot-preference-optimization: Few-Shot Preference Optimization (FSPO) personalizes LLMs by reframing reward modeling as a meta-learning problem, enabling rapid adaptation to user preferences with minimal labeled data, leveraging synthetic datasets for scalability, and achieving high success rates in personalized content generation across multiple domains. · GitHub","url":"https://github.com/Asap7772/fewshot-preference-optimization"},{"title":"Aligning LLM Agents by Learning Latent Preference from User Edits","url":"https://arxiv.org/html/2404.15269v1"},{"title":"Learning to Select Visual In-Context Demonstrations","url":"https://arxiv.org/html/2603.26775v1"},{"title":"Active Preference Learning for Large Language Models","url":"https://arxiv.org/html/2402.08114v2"},{"title":"Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions","url":"https://arxiv.org/html/2603.04191"},{"title":"arXiv:2505.19966v1 [cs.LG] 26 May 2025","url":"https://arxiv.org/pdf/2505.19966"}]

I found several relevant papers from the search. Here are the key results related to your query about interactive preference learning, few-shot demonstrations, and LLM personalization from recent arXiv papers:

## Key Papers Found:

1. **FSPO: Few-Shot Preference Optimization** (arXiv:2502.19312)
   - This paper proposes Few-Shot Preference Optimization (FSPO), which reframes reward modeling as a meta-learning problem where an LLM learns to quickly adapt to a user via a few labeled preferences from that user, constructing a personalized reward function for them. FSPO achieves an 87% Alpaca Eval winrate in generating responses that are personalized to synthetic users and a 70% winrate with real human users in open-ended question answering.

2. **ICPL: Few-shot In-context Preference Learning via LLMs** (arXiv:2410.17233)
   - ICPL uses the in-context learning capabilities of LLMs to reduce human query inefficiency, using task description and basic environment code to create sets of reward functions which are iteratively refined by placing human feedback into the context of an LLM.

3. **POPI: Personalizing LLMs via Optimized Natural Language Preference Inference** (October 2025)
   - This work trains with only a few labeled preference pairs as user signals, simulating realistic low-resource personalization.

4. **Active Preference Learning for LLMs** (arXiv:2402.08114)
   - This introduces Active Preference Learning (APL), an iterative data acquisition and fine-tuning loop where at each step, a batch of prompt/completion pairs is selected according to an acquisition function, oracle labels are acquired and then the model is improved with fine-tuning.

5. **Learning to Select Visual In-Context Demonstrations** (March 2026, arXiv:2603.26775)
   - This paper proposes LSD (Learning to Select Demonstrations), a novel RL framework that trains a Dueling DQN agent to sequentially construct demonstration sets for visual regression tasks.

These papers collectively address interactive preference learning, active selection strategies, few-shot learning with demonstrations, and personalization of LLMs using various approaches including meta-learning, reinforcement learning, and in-context learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45e40b1d-bf6f-460d-925c-4ab965cc841f",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "6a22d65e-7365-45b5-88e1-552aa466484c",
  "toolUseResult": {
    "query": "interactive preference learning few-shot demonstrations EIG active selection LLM personalization April May 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A6aHa1MuqMALbNdmaMZS2q",
        "content": [
          {
            "title": "FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users",
            "url": "https://arxiv.org/html/2502.19312v1"
          },
          {
            "title": "[2502.19312] FSPO: Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users",
            "url": "https://arxiv.org/abs/2502.19312"
          },
          {
            "title": "[2410.17233] ICPL: Few-shot In-context Preference Learning via LLMs",
            "url": "https://arxiv.org/abs/2410.17233"
          },
          {
            "title": "POPI: Personalizing LLMs via Optimized Natural Language Preference Inference",
            "url": "https://arxiv.org/html/2510.17881v1"
          },
          {
            "title": "GitHub - Asap7772/fewshot-preference-optimization: Few-Shot Preference Optimization (FSPO) personalizes LLMs by reframing reward modeling as a meta-learning problem, enabling rapid adaptation to user preferences with minimal labeled data, leveraging synthetic datasets for scalability, and achieving high success rates in personalized content generation across multiple domains. · GitHub",
            "url": "https://github.com/Asap7772/fewshot-preference-optimization"
          },
          {
            "title": "Aligning LLM Agents by Learning Latent Preference from User Edits",
            "url": "https://arxiv.org/html/2404.15269v1"
          },
          {
            "title": "Learning to Select Visual In-Context Demonstrations",
            "url": "https://arxiv.org/html/2603.26775v1"
          },
          {
            "title": "Active Preference Learning for Large Language Models",
            "url": "https://arxiv.org/html/2402.08114v2"
          },
          {
            "title": "Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions",
            "url": "https://arxiv.org/html/2603.04191"
          },
          {
            "title": "arXiv:2505.19966v1 [cs.LG] 26 May 2025",
            "url": "https://arxiv.org/pdf/2505.19966"
          }
        ]
      },
      "I found several relevant papers from the search. Here are the key results related to your query about interactive preference learning, few-shot demonstrations, and LLM personalization from recent arXiv papers:\n\n## Key Papers Found:\n\n1. **FSPO: Few-Shot Preference Optimization** (arXiv:2502.19312)\n   - This paper proposes Few-Shot Preference Optimization (FSPO), which reframes reward modeling as a meta-learning problem where an LLM learns to quickly adapt to a user via a few labeled preferences from that user, constructing a personalized reward function for them. FSPO achieves an 87% Alpaca Eval winrate in generating responses that are personalized to synthetic users and a 70% winrate with real human users in open-ended question answering.\n\n2. **ICPL: Few-shot In-context Preference Learning via LLMs** (arXiv:2410.17233)\n   - ICPL uses the in-context learning capabilities of LLMs to reduce human query inefficiency, using task description and basic environment code to create sets of reward functions which are iteratively refined by placing human feedback into the context of an LLM.\n\n3. **POPI: Personalizing LLMs via Optimized Natural Language Preference Inference** (October 2025)\n   - This work trains with only a few labeled preference pairs as user signals, simulating realistic low-resource personalization.\n\n4. **Active Preference Learning for LLMs** (arXiv:2402.08114)\n   - This introduces Active Preference Learning (APL), an iterative data acquisition and fine-tuning loop where at each step, a batch of prompt/completion pairs is selected according to an acquisition function, oracle labels are acquired and then the model is improved with fine-tuning.\n\n5. **Learning to Select Visual In-Context Demonstrations** (March 2026, arXiv:2603.26775)\n   - This paper proposes LSD (Learning to Select Demonstrations), a novel RL framework that trains a Dueling DQN agent to sequentially construct demonstration sets for visual regression tasks.\n\nThese papers collectively address interactive preference learning, active selection strategies, few-shot learning with demonstrations, and personalization of LLMs using various approaches including meta-learning, reinforcement learning, and in-context learning."
    ],
    "durationSeconds": 9.920189530000004
  },
  "sourceToolAssistantUUID": "45e40b1d-bf6f-460d-925c-4ab965cc841f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T08:11:52.515Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me look into the recent work in 2026 that might be concurrent and might challenge FABEL's novelty claims more directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a22d65e-7365-45b5-88e1-552aa466484c",
  "isSidechain": false,
  "requestId": "req_011CatYuaAKFcsNBuMUaXMAX",
  "type": "assistant",
  "uuid": "b60e92de-8aa7-41b9-bb52-7359cc12dbee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011faRMz63pEvydwB269ptHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 52676,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 183,
          "cache_read_input_tokens": 52676,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1312
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

_source line 42 · 2026-05-10T08:11:53.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A1gsauXsZAgCUJp8J4apxB`</summary>

```json
{
  "query": "temperature scaling prior calibration LLM log likelihood hypothesis posterior 2025 2026 personalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b60e92de-8aa7-41b9-bb52-7359cc12dbee",
  "isSidechain": false,
  "requestId": "req_011CatYuaAKFcsNBuMUaXMAX",
  "type": "assistant",
  "uuid": "0de0a038-9819-48b1-b8c7-71582a714bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011faRMz63pEvydwB269ptHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 52676,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 183,
          "cache_read_input_tokens": 52676,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1312
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

_source line 43 · 2026-05-10T08:11:54.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CEik8WLCtiL5hxEZpPRkno`</summary>

```json
{
  "query": "AMPLe active preference learning multi-dimensional LLM personalization ACL 2025 arXiv 2411.00524"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0de0a038-9819-48b1-b8c7-71582a714bcd",
  "isSidechain": false,
  "requestId": "req_011CatYuaAKFcsNBuMUaXMAX",
  "type": "assistant",
  "uuid": "0373a886-1554-499b-875d-c5d9cc071a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011faRMz63pEvydwB269ptHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 52676,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 183,
          "cache_read_input_tokens": 52676,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1312
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0373a886-1554-499b-875d-c5d9cc071a7e",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Tool result

_source line 46 · 2026-05-10T08:12:00.893Z_

<details><summary>↩ Tool result · `toolu_01CEik8WLCtiL5hxEZpPRkno`</summary>

```text
Web search results for query: "AMPLe active preference learning multi-dimensional LLM personalization ACL 2025 arXiv 2411.00524"

Links: [{"title":"Comparison-based Active Preference Learning for Multi-dimensional Personalization - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1590/"},{"title":"GitHub - ml-postech/AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization","url":"https://github.com/ml-postech/AMPLe"},{"title":"Comparison-based Active Preference Learning for Multi- ...","url":"https://aclanthology.org/2025.acl-long.1590.pdf"},{"title":"[2411.00524] Comparison-based Active Preference Learning for Multi-dimensional Personalization","url":"https://arxiv.org/abs/2411.00524"},{"title":"Comparison-based Active Preference Learning for Multi-dimensional Personalization","url":"https://arxiv.org/html/2411.00524"},{"title":"CoPL: Collaborative Preference Learning for Personalizing LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.650/"},{"title":"A Survey on Personalized Alignment—The Missing Piece ...","url":"https://aclanthology.org/2025.findings-acl.277.pdf"},{"title":"Difference-Aware User Modeling for Enhancing LLM ...","url":"https://aclanthology.org/2025.findings-acl.1095.pdf"},{"title":"(PDF) Active Preference-based Learning for Multi-dimensional Personalization","url":"https://www.researchgate.net/publication/385510388_Active_Preference-based_Learning_for_Multi-dimensional_Personalization"},{"title":"ACL 2025: 5 Trends Shaping the Future of LLMs | Appen","url":"https://www.appen.com/blog/acl-2025"}]

I found the paper you're looking for! Here's the information about AMPLe from the search results:

## Overview

AMPLe (Active Multi-dimensional Preference Learning) is designed to capture implicit user preferences from interactively collected comparative feedback. The paper was accepted by ACL 2025 Main (Long).

## Key Technical Components

Building on Bayesian inference, the work introduces a modified posterior update procedure to mitigate estimation bias and potential noise in comparisons. Also, inspired by generalized binary search, it employs an active query selection strategy to minimize the number of required comparisons by a user.

## Motivation

Large language models (LLMs) have shown remarkable success, but aligning them with human preferences remains a core challenge. As individuals have their own, multi-dimensional preferences, recent studies have explored multi-dimensional personalization. However, human preferences are often implicit and thus difficult to articulate, limiting the direct application of this approach.

## Results and Availability

Through theoretical analysis and experiments on language generation tasks, the framework demonstrates feedback efficiency and effectiveness in personalizing model responses. Code is publicly available at https://github.com/ml-postech/AMPLe.

The paper is published by authors Minhyeon Oh, Seungjoon Lee, and Jungseul Ok, and the arXiv version (2411.00524) is also available online.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0373a886-1554-499b-875d-c5d9cc071a7e",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "8f2f9883-b1fc-4159-9375-33f9b7436fc0",
  "toolUseResult": {
    "query": "AMPLe active preference learning multi-dimensional LLM personalization ACL 2025 arXiv 2411.00524",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PEiNUKhRDBtnN3r9hL9czp",
        "content": [
          {
            "title": "Comparison-based Active Preference Learning for Multi-dimensional Personalization - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1590/"
          },
          {
            "title": "GitHub - ml-postech/AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization",
            "url": "https://github.com/ml-postech/AMPLe"
          },
          {
            "title": "Comparison-based Active Preference Learning for Multi- ...",
            "url": "https://aclanthology.org/2025.acl-long.1590.pdf"
          },
          {
            "title": "[2411.00524] Comparison-based Active Preference Learning for Multi-dimensional Personalization",
            "url": "https://arxiv.org/abs/2411.00524"
          },
          {
            "title": "Comparison-based Active Preference Learning for Multi-dimensional Personalization",
            "url": "https://arxiv.org/html/2411.00524"
          },
          {
            "title": "CoPL: Collaborative Preference Learning for Personalizing LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.650/"
          },
          {
            "title": "A Survey on Personalized Alignment—The Missing Piece ...",
            "url": "https://aclanthology.org/2025.findings-acl.277.pdf"
          },
          {
            "title": "Difference-Aware User Modeling for Enhancing LLM ...",
            "url": "https://aclanthology.org/2025.findings-acl.1095.pdf"
          },
          {
            "title": "(PDF) Active Preference-based Learning for Multi-dimensional Personalization",
            "url": "https://www.researchgate.net/publication/385510388_Active_Preference-based_Learning_for_Multi-dimensional_Personalization"
          },
          {
            "title": "ACL 2025: 5 Trends Shaping the Future of LLMs | Appen",
            "url": "https://www.appen.com/blog/acl-2025"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about AMPLe from the search results:\n\n## Overview\n\nAMPLe (Active Multi-dimensional Preference Learning) is designed to capture implicit user preferences from interactively collected comparative feedback. The paper was accepted by ACL 2025 Main (Long).\n\n## Key Technical Components\n\nBuilding on Bayesian inference, the work introduces a modified posterior update procedure to mitigate estimation bias and potential noise in comparisons. Also, inspired by generalized binary search, it employs an active query selection strategy to minimize the number of required comparisons by a user.\n\n## Motivation\n\nLarge language models (LLMs) have shown remarkable success, but aligning them with human preferences remains a core challenge. As individuals have their own, multi-dimensional preferences, recent studies have explored multi-dimensional personalization. However, human preferences are often implicit and thus difficult to articulate, limiting the direct application of this approach.\n\n## Results and Availability\n\nThrough theoretical analysis and experiments on language generation tasks, the framework demonstrates feedback efficiency and effectiveness in personalizing model responses. Code is publicly available at https://github.com/ml-postech/AMPLe.\n\nThe paper is published by authors Minhyeon Oh, Seungjoon Lee, and Jungseul Ok, and the arXiv version (2411.00524) is also available online."
    ],
    "durationSeconds": 6.798131840999995
  },
  "sourceToolAssistantUUID": "0373a886-1554-499b-875d-c5d9cc071a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T08:12:01.117Z_

<details><summary>↩ Tool result · `toolu_01A1gsauXsZAgCUJp8J4apxB`</summary>

```text
Web search results for query: "temperature scaling prior calibration LLM log likelihood hypothesis posterior 2025 2026 personalization"

Links: [{"title":"ICLR Semantic Calibration of LLMs Through the Lens of Temperature Scaling","url":"https://iclr.cc/virtual/2025/32891"},{"title":"[2409.19817] Calibrating Language Models with Adaptive Temperature Scaling","url":"https://arxiv.org/abs/2409.19817"},{"title":"Temperature Scaling: How to Calibrate LLM Confidence Scores for Better Predictions | Markaicode","url":"https://markaicode.com/temperature-scaling-calibrate-llm-confidence-scores/"},{"title":"Calibrating Language Models with Adaptive Temperature Scaling | Request PDF","url":"https://www.researchgate.net/publication/386193179_Calibrating_Language_Models_with_Adaptive_Temperature_Scaling"},{"title":"Improving Semantic Uncertainty Quantification in Language Model Question-Answering via Token-Level Temperature Scaling | OpenReview","url":"https://openreview.net/forum?id=kuBkI1fbJH"},{"title":"1 Temperature Scaling Improves Semantic Uncertainty Quantification. Same model using different temperatures generates 10 responses for the same input, which are clustered into semantic groups. We compute the L-SC semantic confidence measure of () defined in . Panel (a) uses the standard temperature of 0.5; panel (b) uses a temperature optimised on a calibration set. We find that optimised temperature scaling improves both semantic calibration and discrimination.","url":"https://arxiv.org/html/2604.07172v1"},{"title":"GitHub - gpleiss/temperature_scaling: A simple way to calibrate your neural network. · GitHub","url":"https://github.com/gpleiss/temperature_scaling"},{"title":"Thermometer: Towards Universal Calibration for Large Language Models","url":"https://sia.mit.edu/wp-content/uploads/2024/12/2024-shen-das-greenewald-sattigeri-wornell-ghosh-icml.pdf"},{"title":"Calibrating Language Models With Adaptive Temperature Scaling | OpenReview","url":"https://openreview.net/forum?id=BgfGqNpoMi"},{"title":"On the Role of Temperature Sampling in Test-Time Scaling | OpenReview","url":"https://openreview.net/forum?id=DMoSFziBfu"}]

Based on the search results, I found several recent papers and resources related to temperature scaling and calibration of large language models from 2025-2026. Here are the key findings:

## Recent Research on Temperature Scaling for LLM Calibration (2025-2026)

**Semantic Calibration Focus:**
Calibration of large language models (LLMs) is typically studied at the token level, but for generative tasks like question-answering, semantic calibration is more relevant, and the impact of temperature scaling on semantic confidence measures remains underexplored.

**Temperature Scaling Improvements:**
A single scalar temperature, which provides a suitable inductive bias, is a surprisingly simple yet effective solution, and temperature scaling consistently improves semantic calibration, discrimination, and downstream entropy, outperforming both heuristic baselines and more expressive token-level recalibration methods on question-answering tasks.

**Bayesian Interpretation:**
Recent work introduces a novel calibration loss function, Selective Logit Smoothing (SLS), with a principled Bayesian interpretation.

**Multi-Temperature Scaling:**
Different sampling temperatures solve different subsets of problems, meaning single-temperature scaling explores only part of a model's potential, and scaling along the temperature dimension enlarges the reasoning boundary of LLMs.

**Adaptive Temperature Scaling:**
Adaptive Temperature Scaling (ATS) is a post-hoc calibration method that predicts a temperature scaling parameter for each token prediction, with values adapting based on token-level features fitted over a supervised fine-tuning dataset, addressing varying degrees of calibration shift that can occur after RLHF fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0de0a038-9819-48b1-b8c7-71582a714bcd",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "d6535842-b024-40c0-9bb5-e32831882596",
  "toolUseResult": {
    "query": "temperature scaling prior calibration LLM log likelihood hypothesis posterior 2025 2026 personalization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NDCdP4wvkdD7LRTPFW6CGY",
        "content": [
          {
            "title": "ICLR Semantic Calibration of LLMs Through the Lens of Temperature Scaling",
            "url": "https://iclr.cc/virtual/2025/32891"
          },
          {
            "title": "[2409.19817] Calibrating Language Models with Adaptive Temperature Scaling",
            "url": "https://arxiv.org/abs/2409.19817"
          },
          {
            "title": "Temperature Scaling: How to Calibrate LLM Confidence Scores for Better Predictions | Markaicode",
            "url": "https://markaicode.com/temperature-scaling-calibrate-llm-confidence-scores/"
          },
          {
            "title": "Calibrating Language Models with Adaptive Temperature Scaling | Request PDF",
            "url": "https://www.researchgate.net/publication/386193179_Calibrating_Language_Models_with_Adaptive_Temperature_Scaling"
          },
          {
            "title": "Improving Semantic Uncertainty Quantification in Language Model Question-Answering via Token-Level Temperature Scaling | OpenReview",
            "url": "https://openreview.net/forum?id=kuBkI1fbJH"
          },
          {
            "title": "1 Temperature Scaling Improves Semantic Uncertainty Quantification. Same model using different temperatures generates 10 responses for the same input, which are clustered into semantic groups. We compute the L-SC semantic confidence measure of () defined in . Panel (a) uses the standard temperature of 0.5; panel (b) uses a temperature optimised on a calibration set. We find that optimised temperature scaling improves both semantic calibration and discrimination.",
            "url": "https://arxiv.org/html/2604.07172v1"
          },
          {
            "title": "GitHub - gpleiss/temperature_scaling: A simple way to calibrate your neural network. · GitHub",
            "url": "https://github.com/gpleiss/temperature_scaling"
          },
          {
            "title": "Thermometer: Towards Universal Calibration for Large Language Models",
            "url": "https://sia.mit.edu/wp-content/uploads/2024/12/2024-shen-das-greenewald-sattigeri-wornell-ghosh-icml.pdf"
          },
          {
            "title": "Calibrating Language Models With Adaptive Temperature Scaling | OpenReview",
            "url": "https://openreview.net/forum?id=BgfGqNpoMi"
          },
          {
            "title": "On the Role of Temperature Sampling in Test-Time Scaling | OpenReview",
            "url": "https://openreview.net/forum?id=DMoSFziBfu"
          }
        ]
      },
      "Based on the search results, I found several recent papers and resources related to temperature scaling and calibration of large language models from 2025-2026. Here are the key findings:\n\n## Recent Research on Temperature Scaling for LLM Calibration (2025-2026)\n\n**Semantic Calibration Focus:**\nCalibration of large language models (LLMs) is typically studied at the token level, but for generative tasks like question-answering, semantic calibration is more relevant, and the impact of temperature scaling on semantic confidence measures remains underexplored.\n\n**Temperature Scaling Improvements:**\nA single scalar temperature, which provides a suitable inductive bias, is a surprisingly simple yet effective solution, and temperature scaling consistently improves semantic calibration, discrimination, and downstream entropy, outperforming both heuristic baselines and more expressive token-level recalibration methods on question-answering tasks.\n\n**Bayesian Interpretation:**\nRecent work introduces a novel calibration loss function, Selective Logit Smoothing (SLS), with a principled Bayesian interpretation.\n\n**Multi-Temperature Scaling:**\nDifferent sampling temperatures solve different subsets of problems, meaning single-temperature scaling explores only part of a model's potential, and scaling along the temperature dimension enlarges the reasoning boundary of LLMs.\n\n**Adaptive Temperature Scaling:**\nAdaptive Temperature Scaling (ATS) is a post-hoc calibration method that predicts a temperature scaling parameter for each token prediction, with values adapting based on token-level features fitted over a supervised fine-tuning dataset, addressing varying degrees of calibration shift that can occur after RLHF fine-tuning."
    ],
    "durationSeconds": 7.800565139999992
  },
  "sourceToolAssistantUUID": "0de0a038-9819-48b1-b8c7-71582a714bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-10T08:12:03.705Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me check for any very recent concurrent work that might overlap with FABEL specifically, particularly from April-May 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6535842-b024-40c0-9bb5-e32831882596",
  "isSidechain": false,
  "requestId": "req_011CatYvQUS1bfzu5mBrMCr9",
  "type": "assistant",
  "uuid": "105a66d3-154e-4e7e-ba93-087fd6d812ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFUp8E2hUnMqxhihLPGXrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 853,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 53988,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 853,
          "output_tokens": 176,
          "cache_read_input_tokens": 53988,
          "cache_creation_input_tokens": 2134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2134
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

_source line 49 · 2026-05-10T08:12:04.188Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4CkWdfeStBacpNdaTkgr1`</summary>

```json
{
  "query": "CoPL collaborative preference learning personalization LLM EMNLP 2025 ACL anthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "105a66d3-154e-4e7e-ba93-087fd6d812ad",
  "isSidechain": false,
  "requestId": "req_011CatYvQUS1bfzu5mBrMCr9",
  "type": "assistant",
  "uuid": "03c67de8-f34b-43a6-acb0-3a52f3ed9673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFUp8E2hUnMqxhihLPGXrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 853,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 53988,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 853,
          "output_tokens": 176,
          "cache_read_input_tokens": 53988,
          "cache_creation_input_tokens": 2134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2134
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

_source line 50 · 2026-05-10T08:12:04.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019kZaWa1MxuJKaZR4goE2LS`</summary>

```json
{
  "query": "active Bayesian personalization LLM response style format tone binary question confirmation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03c67de8-f34b-43a6-acb0-3a52f3ed9673",
  "isSidechain": false,
  "requestId": "req_011CatYvQUS1bfzu5mBrMCr9",
  "type": "assistant",
  "uuid": "994efd49-68ff-45c2-9e34-1a725a7da237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JFUp8E2hUnMqxhihLPGXrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 853,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 53988,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 853,
          "output_tokens": 176,
          "cache_read_input_tokens": 53988,
          "cache_creation_input_tokens": 2134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2134
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

_source line 51 · 2026-05-10T08:12:13.189Z_

<details><summary>↩ Tool result · `toolu_01V4CkWdfeStBacpNdaTkgr1`</summary>

```text
Web search results for query: "CoPL collaborative preference learning personalization LLM EMNLP 2025 ACL anthology"

Links: [{"title":"CoPL: Collaborative Preference Learning for Personalizing LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.650/"},{"title":"GitHub - ml-postech/CoPL: Official repository of \"CoPL: Collaborative Preference Learning for Personalizing LLMs\" · GitHub","url":"https://github.com/ml-postech/CoPL"},{"title":"CoPL: Collaborative Preference Learning for Personalizing LLMs | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.650@ACL"},{"title":"[2503.01658] CoPL: Collaborative Preference Learning for Personalizing LLMs","url":"https://arxiv.org/abs/2503.01658"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"CoPL: Collaborative Preference Learning for Personalizing LLMs","url":"https://arxiv.org/html/2503.01658"},{"title":"CoPL: Collaborative Preference Learning for Personalizing LLMs | OpenReview","url":"https://openreview.net/forum?id=YsyMLyrLDS"},{"title":"Published as a conference paper at ICLR 2025 COPL: COLLABORATIVE PREFERENCE","url":"https://openreview.net/pdf/dae167702ca4e19a875337d2a1df98abe8dab0d5.pdf"},{"title":"CoPL: Collaborative Preference Learning for Personalizing LLMs","url":"https://openreview.net/pdf/6f63e0af334188aff38fb7795a02a43f407a52e1.pdf"},{"title":"[Literature Review] CoPL: Collaborative Preference Learning for Personalizing LLMs","url":"https://www.themoonlight.io/en/review/copl-collaborative-preference-learning-for-personalizing-llms"}]

I found comprehensive information about CoPL. Here's what the search revealed:

## CoPL: Collaborative Preference Learning for Personalizing LLMs

CoPL (Collaborative Preference Learning) is a graph-based collaborative filtering framework that models user-response relationships to enhance preference estimation, particularly in sparse annotation settings.

### Publication Details

The paper was published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 12875–12893, Suzhou, China. The authors are Youngbin Choi, Seunghyuk Cho, Minjong Lee, MoonJeong Park, Yesong Ko, Jungseul Ok, and Dongwoo Kim.

### Key Technical Approach

By integrating a mixture of LoRA experts, CoPL efficiently fine-tunes LLMs while dynamically balancing shared and user-specific preferences. Additionally, an optimization-free adaptation strategy enables generalization to unseen users without fine-tuning.

### Experimental Results

Experiments on TL;DR, UltraFeedback-P, and PersonalLLM datasets demonstrate that CoPL outperforms existing personalized reward models, effectively capturing both common and controversial preferences, making it a scalable solution for personalized LLM alignment.

The paper is available on the ACL Anthology at https://aclanthology.org/2025.emnlp-main.650/ and the official code repository is available on GitHub at https://github.com/ml-postech/CoPL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03c67de8-f34b-43a6-acb0-3a52f3ed9673",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "f506e64d-680a-49dc-ad21-88c0fe612b01",
  "toolUseResult": {
    "query": "CoPL collaborative preference learning personalization LLM EMNLP 2025 ACL anthology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WXuUyYCin8PpKMJhtZ1jU8",
        "content": [
          {
            "title": "CoPL: Collaborative Preference Learning for Personalizing LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.650/"
          },
          {
            "title": "GitHub - ml-postech/CoPL: Official repository of \"CoPL: Collaborative Preference Learning for Personalizing LLMs\" · GitHub",
            "url": "https://github.com/ml-postech/CoPL"
          },
          {
            "title": "CoPL: Collaborative Preference Learning for Personalizing LLMs | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/2025.emnlp-main.650@ACL"
          },
          {
            "title": "[2503.01658] CoPL: Collaborative Preference Learning for Personalizing LLMs",
            "url": "https://arxiv.org/abs/2503.01658"
          },
          {
            "title": "Accepted Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/main_papers/"
          },
          {
            "title": "CoPL: Collaborative Preference Learning for Personalizing LLMs",
            "url": "https://arxiv.org/html/2503.01658"
          },
          {
            "title": "CoPL: Collaborative Preference Learning for Personalizing LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=YsyMLyrLDS"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 COPL: COLLABORATIVE PREFERENCE",
            "url": "https://openreview.net/pdf/dae167702ca4e19a875337d2a1df98abe8dab0d5.pdf"
          },
          {
            "title": "CoPL: Collaborative Preference Learning for Personalizing LLMs",
            "url": "https://openreview.net/pdf/6f63e0af334188aff38fb7795a02a43f407a52e1.pdf"
          },
          {
            "title": "[Literature Review] CoPL: Collaborative Preference Learning for Personalizing LLMs",
            "url": "https://www.themoonlight.io/en/review/copl-collaborative-preference-learning-for-personalizing-llms"
          }
        ]
      },
      "I found comprehensive information about CoPL. Here's what the search revealed:\n\n## CoPL: Collaborative Preference Learning for Personalizing LLMs\n\nCoPL (Collaborative Preference Learning) is a graph-based collaborative filtering framework that models user-response relationships to enhance preference estimation, particularly in sparse annotation settings.\n\n### Publication Details\n\nThe paper was published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 12875–12893, Suzhou, China. The authors are Youngbin Choi, Seunghyuk Cho, Minjong Lee, MoonJeong Park, Yesong Ko, Jungseul Ok, and Dongwoo Kim.\n\n### Key Technical Approach\n\nBy integrating a mixture of LoRA experts, CoPL efficiently fine-tunes LLMs while dynamically balancing shared and user-specific preferences. Additionally, an optimization-free adaptation strategy enables generalization to unseen users without fine-tuning.\n\n### Experimental Results\n\nExperiments on TL;DR, UltraFeedback-P, and PersonalLLM datasets demonstrate that CoPL outperforms existing personalized reward models, effectively capturing both common and controversial preferences, making it a scalable solution for personalized LLM alignment.\n\nThe paper is available on the ACL Anthology at https://aclanthology.org/2025.emnlp-main.650/ and the official code repository is available on GitHub at https://github.com/ml-postech/CoPL."
    ],
    "durationSeconds": 8.998703198999996
  },
  "sourceToolAssistantUUID": "03c67de8-f34b-43a6-acb0-3a52f3ed9673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T08:12:14.402Z_

<details><summary>↩ Tool result · `toolu_019kZaWa1MxuJKaZR4goE2LS`</summary>

```text
Web search results for query: "active Bayesian personalization LLM response style format tone binary question confirmation 2026 arXiv"

Links: [{"title":"A Survey of Personalized Large Language Models: Progress and Future Directions","url":"https://arxiv.org/html/2502.11528v2"},{"title":"Personalized LLM Response Generation with Parameterized User Memory Injection","url":"https://arxiv.org/html/2404.03565"},{"title":"Comparison-based Active Preference Learning for Multi-dimensional Personalization","url":"https://arxiv.org/html/2411.00524"},{"title":"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design","url":"https://arxiv.org/html/2508.21184v1"},{"title":"Personalized LLM Response Generation with Parameterized Memory Injection","url":"https://arxiv.org/html/2404.03565v1"},{"title":"Tailored Behavior-Change Messaging for Physical Activity: Integrating Contextual Bandits and Large Language Models","url":"https://arxiv.org/html/2506.07275"},{"title":"POPI: Personalizing LLMs via Optimized Natural Language Preference Inference","url":"https://www.arxiv.org/pdf/2510.17881"},{"title":"Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models","url":"https://arxiv.org/html/2503.17523v1"},{"title":"[2503.17523] Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models","url":"https://arxiv.org/abs/2503.17523"},{"title":"Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/bayesian-optimization-llm-based-acquisition-functions-natural"}]

The search has returned several highly relevant arXiv papers from 2025-2026 that combine active learning, Bayesian methods, personalization, and LLM response customization. Here are the key findings:

## Relevant Papers Found:

1. **Active Multi-dimensional Preference Learning (AMPLe)** - A method designed to capture implicit user preferences from interactively collected comparative feedback, using Bayesian inference with a modified posterior update procedure and an active query selection strategy to minimize the number of required comparisons by a user.

2. **Memory-Injected LLM Personalization (MiLP)** - Uses a Bayesian optimization strategy to automatically identify the optimal configuration for applying multiple LoRA modules, enabling efficient and flexible personalization. The paper specifically addresses binary parameters for layer selection.

3. **BED-LLM: Bayesian Experimental Design** - Tests interactive question-answering scenarios including 20-Questions (a deductive reasoning game requiring identification of a hidden target entity through binary Yes/No queries) and Active Preference Elicitation (a task to infer latent user preference vectors via multiple-choice questions).

4. **POPI: Personalized Natural Language Preference Inference** - A 2026 paper (under review for WWW '26) that personalizes LLMs through preference summaries and response format customization.

5. **Bayesian Teaching for LLMs** - By teaching LLMs to mimic the predictions of the normative Bayesian model, the ability to update beliefs can be dramatically improved, with this ability generalizing to new tasks and suggesting that LLMs can be endowed with broader Bayesian reasoning skills.

These papers represent recent advances in using active Bayesian approaches to personalize LLM response styles, formats, and tones through interactive preference learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "994efd49-68ff-45c2-9e34-1a725a7da237",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "3d832f02-946a-464e-9343-d1a7f00a9dc3",
  "toolUseResult": {
    "query": "active Bayesian personalization LLM response style format tone binary question confirmation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EmQcRs1ab1FZVUtp2h1Xio",
        "content": [
          {
            "title": "A Survey of Personalized Large Language Models: Progress and Future Directions",
            "url": "https://arxiv.org/html/2502.11528v2"
          },
          {
            "title": "Personalized LLM Response Generation with Parameterized User Memory Injection",
            "url": "https://arxiv.org/html/2404.03565"
          },
          {
            "title": "Comparison-based Active Preference Learning for Multi-dimensional Personalization",
            "url": "https://arxiv.org/html/2411.00524"
          },
          {
            "title": "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design",
            "url": "https://arxiv.org/html/2508.21184v1"
          },
          {
            "title": "Personalized LLM Response Generation with Parameterized Memory Injection",
            "url": "https://arxiv.org/html/2404.03565v1"
          },
          {
            "title": "Tailored Behavior-Change Messaging for Physical Activity: Integrating Contextual Bandits and Large Language Models",
            "url": "https://arxiv.org/html/2506.07275"
          },
          {
            "title": "POPI: Personalizing LLMs via Optimized Natural Language Preference Inference",
            "url": "https://www.arxiv.org/pdf/2510.17881"
          },
          {
            "title": "Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2503.17523v1"
          },
          {
            "title": "[2503.17523] Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models",
            "url": "https://arxiv.org/abs/2503.17523"
          },
          {
            "title": "Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/bayesian-optimization-llm-based-acquisition-functions-natural"
          }
        ]
      },
      "The search has returned several highly relevant arXiv papers from 2025-2026 that combine active learning, Bayesian methods, personalization, and LLM response customization. Here are the key findings:\n\n## Relevant Papers Found:\n\n1. **Active Multi-dimensional Preference Learning (AMPLe)** - A method designed to capture implicit user preferences from interactively collected comparative feedback, using Bayesian inference with a modified posterior update procedure and an active query selection strategy to minimize the number of required comparisons by a user.\n\n2. **Memory-Injected LLM Personalization (MiLP)** - Uses a Bayesian optimization strategy to automatically identify the optimal configuration for applying multiple LoRA modules, enabling efficient and flexible personalization. The paper specifically addresses binary parameters for layer selection.\n\n3. **BED-LLM: Bayesian Experimental Design** - Tests interactive question-answering scenarios including 20-Questions (a deductive reasoning game requiring identification of a hidden target entity through binary Yes/No queries) and Active Preference Elicitation (a task to infer latent user preference vectors via multiple-choice questions).\n\n4. **POPI: Personalized Natural Language Preference Inference** - A 2026 paper (under review for WWW '26) that personalizes LLMs through preference summaries and response format customization.\n\n5. **Bayesian Teaching for LLMs** - By teaching LLMs to mimic the predictions of the normative Bayesian model, the ability to update beliefs can be dramatically improved, with this ability generalizing to new tasks and suggesting that LLMs can be endowed with broader Bayesian reasoning skills.\n\nThese papers represent recent advances in using active Bayesian approaches to personalize LLM response styles, formats, and tones through interactive preference learning."
    ],
    "durationSeconds": 9.641603374999992
  },
  "sourceToolAssistantUUID": "994efd49-68ff-45c2-9e34-1a725a7da237",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3d832f02-946a-464e-9343-d1a7f00a9dc3",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Assistant

_source line 55 · 2026-05-10T08:12:17.479Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also look into the "Failing to Falsify" paper and verify the TO-GATE paper exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d832f02-946a-464e-9343-d1a7f00a9dc3",
  "isSidechain": false,
  "requestId": "req_011CatYwPEnvC8Ntm2WvkZty",
  "type": "assistant",
  "uuid": "600d1afc-9ba8-4890-ac5c-27d2f0d770e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GJ2N56Pp5dtMoDhnYxHiQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 56122,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 56122,
          "cache_creation_input_tokens": 2901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2901
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

_source line 56 · 2026-05-10T08:12:18.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012rCw7skoYs3WvTPjo7bB6P`</summary>

```json
{
  "query": "\"Failing to Falsify\" LLM confirmation bias hypothesis testing arXiv 2604.02485 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600d1afc-9ba8-4890-ac5c-27d2f0d770e9",
  "isSidechain": false,
  "requestId": "req_011CatYwPEnvC8Ntm2WvkZty",
  "type": "assistant",
  "uuid": "a3359ed7-fd57-49cc-a42f-c2110a1056a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GJ2N56Pp5dtMoDhnYxHiQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 56122,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 56122,
          "cache_creation_input_tokens": 2901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2901
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

_source line 57 · 2026-05-10T08:12:18.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MzPWdKjarDgt9kGcMknLiJ`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 25 2026 call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3359ed7-fd57-49cc-a42f-c2110a1056a4",
  "isSidechain": false,
  "requestId": "req_011CatYwPEnvC8Ntm2WvkZty",
  "type": "assistant",
  "uuid": "4b7a0ba7-c5b6-4a3d-a9cb-77ea4d937989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GJ2N56Pp5dtMoDhnYxHiQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 56122,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 56122,
          "cache_creation_input_tokens": 2901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2901
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

_source line 58 · 2026-05-10T08:12:25.314Z_

<details><summary>↩ Tool result · `toolu_012rCw7skoYs3WvTPjo7bB6P`</summary>

```text
Web search results for query: ""Failing to Falsify" LLM confirmation bias hypothesis testing arXiv 2604.02485 2026"

Links: [{"title":"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models","url":"https://arxiv.org/html/2604.02485"},{"title":"[2604.02485] Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models","url":"https://arxiv.org/abs/2604.02485"}]

I found the paper you're looking for! Here's what the search reveals:

**"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models"** (arXiv 2604.02485)

The study examines whether LLMs exhibit confirmation bias by adapting a rule-discovery study from human psychology, where an agent proposes triples of numbers, receives feedback on whether they satisfy a hidden rule, and guesses the rule.

The researchers found that across eleven LLMs of multiple families and scales, LLMs exhibit confirmation bias by proposing triples to confirm their hypothesis rather than trying to falsify it, which leads to slower and less frequent discovery of the hidden rule.

The study further explores intervention strategies developed for humans (such as encouraging agents to consider counter examples), finding that prompting LLMs with such instructions consistently decreases confirmation bias, improving rule discovery rates from 42% to 56% on average.

The researchers also show that this mitigation can be internalized via distillation, injecting falsification-oriented exploration behavior, with gains extending beyond scale alone and generalizing to a new object-based rule-discovery domain.

The paper was published on April 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3359ed7-fd57-49cc-a42f-c2110a1056a4",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "721afb14-4b36-4cc6-a507-e760c94e0b83",
  "toolUseResult": {
    "query": "\"Failing to Falsify\" LLM confirmation bias hypothesis testing arXiv 2604.02485 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01792YWhAPCyZjXpCQgP8bPJ",
        "content": [
          {
            "title": "Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models",
            "url": "https://arxiv.org/html/2604.02485"
          },
          {
            "title": "[2604.02485] Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models",
            "url": "https://arxiv.org/abs/2604.02485"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search reveals:\n\n**\"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models\"** (arXiv 2604.02485)\n\nThe study examines whether LLMs exhibit confirmation bias by adapting a rule-discovery study from human psychology, where an agent proposes triples of numbers, receives feedback on whether they satisfy a hidden rule, and guesses the rule.\n\nThe researchers found that across eleven LLMs of multiple families and scales, LLMs exhibit confirmation bias by proposing triples to confirm their hypothesis rather than trying to falsify it, which leads to slower and less frequent discovery of the hidden rule.\n\nThe study further explores intervention strategies developed for humans (such as encouraging agents to consider counter examples), finding that prompting LLMs with such instructions consistently decreases confirmation bias, improving rule discovery rates from 42% to 56% on average.\n\nThe researchers also show that this mitigation can be internalized via distillation, injecting falsification-oriented exploration behavior, with gains extending beyond scale alone and generalizing to a new object-based rule-discovery domain.\n\nThe paper was published on April 2, 2026."
    ],
    "durationSeconds": 6.951475086999999
  },
  "sourceToolAssistantUUID": "a3359ed7-fd57-49cc-a42f-c2110a1056a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-10T08:12:25.419Z_

<details><summary>↩ Tool result · `toolu_01MzPWdKjarDgt9kGcMknLiJ`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline May 25 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, I found relevant information about the EMNLP 2026 ARR submission deadline and call for papers:

## Key Information:

**ARR Submission Deadline:** The ARR submission deadline for EMNLP 2026 (long & short papers) is May 25, 2026.

**Call for Papers:** EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

**Important Related Dates:**
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

**Important Note:** Given that the ARR 2026 May cycle is aligned with EMNLP and AACL, authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

The full call for papers can be found at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b7a0ba7-c5b6-4a3d-a9cb-77ea4d937989",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "8cef07ab-d91f-43e0-a7c0-eab167ef1b66",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR submission deadline May 25 2026 call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_017FQuuLeG95z2faobkVS1q6",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          }
        ]
      },
      "Based on the search results, I found relevant information about the EMNLP 2026 ARR submission deadline and call for papers:\n\n## Key Information:\n\n**ARR Submission Deadline:** The ARR submission deadline for EMNLP 2026 (long & short papers) is May 25, 2026.\n\n**Call for Papers:** EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.\n\n**Important Related Dates:**\n- Reviewer registration deadline for ALL authors: May 27, 2026\n- Author response and author-reviewer discussion: July 7 - July 13, 2026\n- Meta review released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Notification of acceptance: August 20, 2026\n\n**Important Note:** Given that the ARR 2026 May cycle is aligned with EMNLP and AACL, authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.\n\nThe full call for papers can be found at https://2026.emnlp.org/calls/main_conference_papers/"
    ],
    "durationSeconds": 6.622976540000003
  },
  "sourceToolAssistantUUID": "4b7a0ba7-c5b6-4a3d-a9cb-77ea4d937989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-10T08:12:27.927Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The venue deadline is confirmed as May 25, 2026. Now let me check if there are any other concurrent works that might challenge FABEL's novelty - particularly from recent months.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cef07ab-d91f-43e0-a7c0-eab167ef1b66",
  "isSidechain": false,
  "requestId": "req_011CatYxCLVPzmWKFY43QDR9",
  "type": "assistant",
  "uuid": "1ca2d726-d3b5-471f-bc38-b7edae35cb89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ts2UC8AHR1CJMJ9HJvBTVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 59023,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 59023,
          "cache_creation_input_tokens": 1582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1582
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

_source line 61 · 2026-05-10T08:12:29.822Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RGW7kxTzbUDisxdbDz6xDR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03925",
  "prompt": "What is the core method of AdaptFuse? Does it use warm-start initialization from user demonstrations? Does it use EIG-based active query selection? Does it have disconfirmation probes? What domain does it evaluate on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ca2d726-d3b5-471f-bc38-b7edae35cb89",
  "isSidechain": false,
  "requestId": "req_011CatYxCLVPzmWKFY43QDR9",
  "type": "assistant",
  "uuid": "0a6b2fe4-11cb-443a-8e91-0fac34b1211d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ts2UC8AHR1CJMJ9HJvBTVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 59023,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 59023,
          "cache_creation_input_tokens": 1582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1582
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

_source line 62 · 2026-05-10T08:12:30.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fcz2Pougv2crrkuZfJwxNZ`</summary>

```json
{
  "query": "EIG information gain preference elicitation demo-conditioned prior personalization writing style format 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a6b2fe4-11cb-443a-8e91-0fac34b1211d",
  "isSidechain": false,
  "requestId": "req_011CatYxCLVPzmWKFY43QDR9",
  "type": "assistant",
  "uuid": "51406abc-9613-4c3d-b9ec-28be9e27bb91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ts2UC8AHR1CJMJ9HJvBTVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 59023,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 59023,
          "cache_creation_input_tokens": 1582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1582
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

_source line 63 · 2026-05-10T08:12:36.565Z_

<details><summary>↩ Tool result · `toolu_01RGW7kxTzbUDisxdbDz6xDR`</summary>

```text
# AdaptFuse Core Method and Evaluation

**Core Method:**
AdaptFuse combines two key components: "a symbolic module maintains a Bayesian posterior over a discrete hypothesis set, while a frozen LLM contributes semantic reasoning via multi-sample Dirichlet aggregation." These signals are merged through entropy-adaptive fusion that automatically adjusts reliance between the symbolic posterior and the language model based on predictive confidence as evidence builds up.

**Warm-Start Initialization:**
The abstract does not mention warm-start initialization from user demonstrations.

**EIG-Based Active Query Selection:**
No information about Expected Information Gain-based active query selection is provided in the content.

**Disconfirmation Probes:**
The document contains no discussion of disconfirmation probes.

**Evaluation Domains:**
The framework was tested across three practical domains: flight recommendation, hotel recommendation, and web shopping, using three different language models (Gemma 2 9B, Llama 3 8B, and Qwen 2.5 7B).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a6b2fe4-11cb-443a-8e91-0fac34b1211d",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "112f83a9-7069-4855-803d-33e009ae6762",
  "toolUseResult": {
    "bytes": 47715,
    "code": 200,
    "codeText": "OK",
    "result": "# AdaptFuse Core Method and Evaluation\n\n**Core Method:**\nAdaptFuse combines two key components: \"a symbolic module maintains a Bayesian posterior over a discrete hypothesis set, while a frozen LLM contributes semantic reasoning via multi-sample Dirichlet aggregation.\" These signals are merged through entropy-adaptive fusion that automatically adjusts reliance between the symbolic posterior and the language model based on predictive confidence as evidence builds up.\n\n**Warm-Start Initialization:**\nThe abstract does not mention warm-start initialization from user demonstrations.\n\n**EIG-Based Active Query Selection:**\nNo information about Expected Information Gain-based active query selection is provided in the content.\n\n**Disconfirmation Probes:**\nThe document contains no discussion of disconfirmation probes.\n\n**Evaluation Domains:**\nThe framework was tested across three practical domains: flight recommendation, hotel recommendation, and web shopping, using three different language models (Gemma 2 9B, Llama 3 8B, and Qwen 2.5 7B).",
    "durationMs": 6740,
    "url": "https://arxiv.org/abs/2604.03925"
  },
  "sourceToolAssistantUUID": "0a6b2fe4-11cb-443a-8e91-0fac34b1211d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-10T08:12:37.591Z_

<details><summary>↩ Tool result · `toolu_01Fcz2Pougv2crrkuZfJwxNZ`</summary>

```text
Web search results for query: "EIG information gain preference elicitation demo-conditioned prior personalization writing style format 2025 2026"

Links: [{"title":"Cold-Start Personalization via Training-Free Priors from Structured World Models","url":"https://arxiv.org/html/2602.15012"},{"title":"Bayesian Preference Elicitation with Language Models","url":"https://arxiv.org/html/2403.05534v1"},{"title":"Causal Preference Elicitation","url":"https://arxiv.org/html/2602.01483"},{"title":"Personalized Algorithmic Recourse with Preference ...","url":"https://arxiv.org/pdf/2205.13743"},{"title":"Personalized Algorithmic Recourse with Preference Elicitation","url":"https://arxiv.org/html/2205.13743"},{"title":"Personalized Algorithmic Recourse with Preference Elicitation | OpenReview","url":"https://openreview.net/forum?id=8sg2I9zXgO"},{"title":"Preference Elicitation with Soft Attributes in Interactive Recommendation","url":"https://arxiv.org/pdf/2311.02085"},{"title":"(PDF) Personalized Algorithmic Recourse with Preference Elicitation","url":"https://www.researchgate.net/publication/360936692_Personalized_Algorithmic_Recourse_with_Preference_Elicitation"},{"title":"Model-Free Preference Elicitation | IJCAI","url":"https://www.ijcai.org/proceedings/2024/387"},{"title":"Model-Free Preference Elicitation","url":"https://www.ijcai.org/proceedings/2024/0387.pdf"}]

I've found relevant research on preference elicitation and information gain techniques. The most prominent result appears to be Pep (Preference Elicitation with Priors), which learns a structured world model of preference correlations offline from complete profiles, then performs training-free Bayesian inference online to select informative questions and predict complete preference profiles.

Key findings from the search results include:

**Expected Information Gain (EIG) in Preference Elicitation:**
Bayesian experimental design formalizes information gain through expected information gain (EIG) maximization, with recent extensions to prediction-oriented objectives, neural acquisition functions, multi-objective optimization, and hybrid preference learning.

**Recent Approaches (2025-2026):**
Recent frameworks learn a structured world model from population data capturing preference correlations through latent user embeddings offline, and for new users, adaptively select questions, update beliefs after each response, and predict the full preference profile, including preferences not asked about.

**LLM-based Preference Elicitation:**
OPEN is a domain-agnostic framework for combining Bayesian Optimal Experimental Design with language models—using BOED to guide the choice of informative questions, and the LM to extract environment-relevant features and translate abstract feature queries into real natural language questions.

The search results show active research into demo-conditioned approaches and personalization with priors, though specific papers on the exact combination of all your query terms weren't found. Would you like me to search for more specific aspects of this topic?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51406abc-9613-4c3d-b9ec-28be9e27bb91",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "fe7ef4de-a320-4e5f-ab80-1c543672f51a",
  "toolUseResult": {
    "query": "EIG information gain preference elicitation demo-conditioned prior personalization writing style format 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ho6BYfQ9KT9HoQpvXrNBrf",
        "content": [
          {
            "title": "Cold-Start Personalization via Training-Free Priors from Structured World Models",
            "url": "https://arxiv.org/html/2602.15012"
          },
          {
            "title": "Bayesian Preference Elicitation with Language Models",
            "url": "https://arxiv.org/html/2403.05534v1"
          },
          {
            "title": "Causal Preference Elicitation",
            "url": "https://arxiv.org/html/2602.01483"
          },
          {
            "title": "Personalized Algorithmic Recourse with Preference ...",
            "url": "https://arxiv.org/pdf/2205.13743"
          },
          {
            "title": "Personalized Algorithmic Recourse with Preference Elicitation",
            "url": "https://arxiv.org/html/2205.13743"
          },
          {
            "title": "Personalized Algorithmic Recourse with Preference Elicitation | OpenReview",
            "url": "https://openreview.net/forum?id=8sg2I9zXgO"
          },
          {
            "title": "Preference Elicitation with Soft Attributes in Interactive Recommendation",
            "url": "https://arxiv.org/pdf/2311.02085"
          },
          {
            "title": "(PDF) Personalized Algorithmic Recourse with Preference Elicitation",
            "url": "https://www.researchgate.net/publication/360936692_Personalized_Algorithmic_Recourse_with_Preference_Elicitation"
          },
          {
            "title": "Model-Free Preference Elicitation | IJCAI",
            "url": "https://www.ijcai.org/proceedings/2024/387"
          },
          {
            "title": "Model-Free Preference Elicitation",
            "url": "https://www.ijcai.org/proceedings/2024/0387.pdf"
          }
        ]
      },
      "I've found relevant research on preference elicitation and information gain techniques. The most prominent result appears to be Pep (Preference Elicitation with Priors), which learns a structured world model of preference correlations offline from complete profiles, then performs training-free Bayesian inference online to select informative questions and predict complete preference profiles.\n\nKey findings from the search results include:\n\n**Expected Information Gain (EIG) in Preference Elicitation:**\nBayesian experimental design formalizes information gain through expected information gain (EIG) maximization, with recent extensions to prediction-oriented objectives, neural acquisition functions, multi-objective optimization, and hybrid preference learning.\n\n**Recent Approaches (2025-2026):**\nRecent frameworks learn a structured world model from population data capturing preference correlations through latent user embeddings offline, and for new users, adaptively select questions, update beliefs after each response, and predict the full preference profile, including preferences not asked about.\n\n**LLM-based Preference Elicitation:**\nOPEN is a domain-agnostic framework for combining Bayesian Optimal Experimental Design with language models—using BOED to guide the choice of informative questions, and the LM to extract environment-relevant features and translate abstract feature queries into real natural language questions.\n\nThe search results show active research into demo-conditioned approaches and personalization with priors, though specific papers on the exact combination of all your query terms weren't found. Would you like me to search for more specific aspects of this topic?"
    ],
    "durationSeconds": 7.157846530999988
  },
  "sourceToolAssistantUUID": "51406abc-9613-4c3d-b9ec-28be9e27bb91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 65 · 2026-05-10T08:12:37.593Z_

```json
{
  "parentUuid": "fe7ef4de-a320-4e5f-ab80-1c543672f51a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "42502711-f428-48f4-a1f1-3cbc71628a34",
  "timestamp": "2026-05-10T08:12:37.593Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 66 · 2026-05-10T08:12:41.466Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The AdaptFuse verification confirms the generator's characterization: no warm-start from demonstrations, no EIG-based active query selection, no disconfirmation probes, evaluated on recommendation domains (not LLM response-style personalization).

Now let me check the feasibility of the 16-day timeline, particularly for BED-LLM reimplementation and PersonalLLM evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42502711-f428-48f4-a1f1-3cbc71628a34",
  "isSidechain": false,
  "requestId": "req_011CatYy6diiMsyaP1t9Fije",
  "type": "assistant",
  "uuid": "3432a2f1-5ff9-4da1-9b8c-38a62aeb5688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019cU5T9MENKKLBhh9WnKDsM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 60605,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 60605,
          "cache_creation_input_tokens": 1433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1433
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

_source line 67 · 2026-05-10T08:12:42.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014kaNWMDhDYToq3TKqcH3Q4`</summary>

```json
{
  "query": "PersonalLLM HuggingFace namkoong-lab dataset download open access 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3432a2f1-5ff9-4da1-9b8c-38a62aeb5688",
  "isSidechain": false,
  "requestId": "req_011CatYy6diiMsyaP1t9Fije",
  "type": "assistant",
  "uuid": "c94a2c22-27ae-4e38-a807-4cd51a1b52d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019cU5T9MENKKLBhh9WnKDsM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 60605,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 60605,
          "cache_creation_input_tokens": 1433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1433
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

_source line 68 · 2026-05-10T08:12:42.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016GjDmEipUgvdP7dohUtsCa`</summary>

```json
{
  "query": "TO-GATE trajectory optimization clarifying questions DPO arXiv 2506.02827 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c94a2c22-27ae-4e38-a807-4cd51a1b52d4",
  "isSidechain": false,
  "requestId": "req_011CatYy6diiMsyaP1t9Fije",
  "type": "assistant",
  "uuid": "fa593dd3-ed6f-4db4-85c5-6c0bef5c3643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019cU5T9MENKKLBhh9WnKDsM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 60605,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 60605,
          "cache_creation_input_tokens": 1433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1433
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

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "fa593dd3-ed6f-4db4-85c5-6c0bef5c3643",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Tool result

_source line 71 · 2026-05-10T08:12:48.372Z_

<details><summary>↩ Tool result · `toolu_014kaNWMDhDYToq3TKqcH3Q4`</summary>

```text
Web search results for query: "PersonalLLM HuggingFace namkoong-lab dataset download open access 2025"

Links: [{"title":"namkoong-lab/PersonalLLM · Datasets at Hugging Face","url":"https://huggingface.co/datasets/namkoong-lab/PersonalLLM"},{"title":"README.md · namkoong-lab/PersonalLLM_Eval at main","url":"https://huggingface.co/datasets/namkoong-lab/PersonalLLM_Eval/blob/main/README.md"},{"title":"1 Introduction","url":"https://arxiv.org/html/2409.20296"},{"title":"GitHub - namkoong-lab/PersonalLLM · GitHub","url":"https://github.com/namkoong-lab/PersonalLLM"},{"title":"pmc/open_access · Datasets at Hugging Face","url":"https://huggingface.co/datasets/pmc/open_access"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"Load · Hugging Face","url":"https://huggingface.co/docs/datasets/en/loading"},{"title":"Datasets · Hugging Face","url":"https://huggingface.co/docs/datasets/index"},{"title":"Loading a Dataset — datasets 1.8.0 documentation","url":"https://huggingface.co/docs/datasets/v1.8.0/loading_datasets.html"},{"title":"Hugging Face – The AI community building the future.","url":"https://huggingface.co/"}]

Based on the search results, here's what I found about the PersonalLLM dataset:

## Overview
The PersonalLLM dataset is a comprehensive collection of prompts, responses, and associated metadata designed for developing and evaluating personalized language models. This dataset is presented in the paper PersonalLLM: Tailoring LLMs to Individual Preferences.

## Access and Download
PersonalLLM is available for download on huggingface at https://huggingface.co/datasets/namkoong-lab/PersonalLLM. The dataset is publicly available with accompanying resources.

## License and Openness
The dataset is released under a CC BY-NC 4.0 License, which prohibits commercial use and requires attribution. This means while it's openly accessible, there are restrictions on commercial applications.

## Additional Resources
Data and code are publicly available, with full documentation available in Appendix A. The evaluation dataset is available at https://huggingface.co/datasets/namkoong-lab/PersonalLLM_Eval, and the interaction database dataset is available at https://huggingface.co/datasets/namkoong-lab/PersonalLLM_InteractionDatabase.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c94a2c22-27ae-4e38-a807-4cd51a1b52d4",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "46e554a6-9f06-411b-a544-4353f58cc4b0",
  "toolUseResult": {
    "query": "PersonalLLM HuggingFace namkoong-lab dataset download open access 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BfPxuzHNeDA9q5uk31VPRa",
        "content": [
          {
            "title": "namkoong-lab/PersonalLLM · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/namkoong-lab/PersonalLLM"
          },
          {
            "title": "README.md · namkoong-lab/PersonalLLM_Eval at main",
            "url": "https://huggingface.co/datasets/namkoong-lab/PersonalLLM_Eval/blob/main/README.md"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2409.20296"
          },
          {
            "title": "GitHub - namkoong-lab/PersonalLLM · GitHub",
            "url": "https://github.com/namkoong-lab/PersonalLLM"
          },
          {
            "title": "pmc/open_access · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/pmc/open_access"
          },
          {
            "title": "Datasets – Hugging Face",
            "url": "https://huggingface.co/datasets"
          },
          {
            "title": "Load · Hugging Face",
            "url": "https://huggingface.co/docs/datasets/en/loading"
          },
          {
            "title": "Datasets · Hugging Face",
            "url": "https://huggingface.co/docs/datasets/index"
          },
          {
            "title": "Loading a Dataset — datasets 1.8.0 documentation",
            "url": "https://huggingface.co/docs/datasets/v1.8.0/loading_datasets.html"
          },
          {
            "title": "Hugging Face – The AI community building the future.",
            "url": "https://huggingface.co/"
          }
        ]
      },
      "Based on the search results, here's what I found about the PersonalLLM dataset:\n\n## Overview\nThe PersonalLLM dataset is a comprehensive collection of prompts, responses, and associated metadata designed for developing and evaluating personalized language models. This dataset is presented in the paper PersonalLLM: Tailoring LLMs to Individual Preferences.\n\n## Access and Download\nPersonalLLM is available for download on huggingface at https://huggingface.co/datasets/namkoong-lab/PersonalLLM. The dataset is publicly available with accompanying resources.\n\n## License and Openness\nThe dataset is released under a CC BY-NC 4.0 License, which prohibits commercial use and requires attribution. This means while it's openly accessible, there are restrictions on commercial applications.\n\n## Additional Resources\nData and code are publicly available, with full documentation available in Appendix A. The evaluation dataset is available at https://huggingface.co/datasets/namkoong-lab/PersonalLLM_Eval, and the interaction database dataset is available at https://huggingface.co/datasets/namkoong-lab/PersonalLLM_InteractionDatabase."
    ],
    "durationSeconds": 6.100245808999985
  },
  "sourceToolAssistantUUID": "c94a2c22-27ae-4e38-a807-4cd51a1b52d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-10T08:12:49.673Z_

<details><summary>↩ Tool result · `toolu_016GjDmEipUgvdP7dohUtsCa`</summary>

```text
Web search results for query: "TO-GATE trajectory optimization clarifying questions DPO arXiv 2506.02827 2025"

Links: [{"title":"[2506.02827] TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference","url":"https://arxiv.org/abs/2506.02827"},{"title":"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference","url":"https://arxiv.org/html/2506.02827"},{"title":"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference","url":"https://www.researchgate.net/publication/392371683_TO-GATE_Clarifying_Questions_and_Summarizing_Responses_with_Trajectory_Optimization_for_Eliciting_Human_Preference"},{"title":"Offline RL by Reward-Weighted Fine-Tuning for Conversation Optimization","url":"https://arxiv.org/html/2506.06964"},{"title":"Learning to Clarify by Reinforcement Learning Through Reward-Weighted Fine-Tuning","url":"https://arxiv.org/html/2506.06964v1"},{"title":"Optimal Trajectory Planning for Space Object Tracking with Collision-Avoidance Constraints","url":"https://arxiv.org/html/2506.22797v1"},{"title":"STaR-GATE: Teaching Language Models to Ask Clarifying Questions","url":"https://arxiv.org/html/2403.19154v2"},{"title":"Smoothed Preference Optimization via ReNoise Inversion for Aligning Diffusion Models with Varied Human Preferences","url":"https://arxiv.org/html/2506.02698"},{"title":"Ch. 10 - Trajectory Optimization - Underactuated Robotics","url":"https://underactuated.mit.edu/trajopt.html"},{"title":"Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms","url":"https://arxiv.org/html/2506.09457"}]

Based on the search results, I found detailed information about the paper arXiv:2506.02827.

## TO-GATE: Trajectory Optimization for Clarifying Questions with DPO

TO-GATE is a framework titled "Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference".

### Overview
The paper was submitted on June 3, 2025, and authored by Yulin Dou and Jiangming Liu. Large language models (LLMs) can effectively elicit human preferences through multi-turn dialogue.

### Problem and Solution
Complex tasks can be accomplished through iterative clarifying questions and final responses generated by an LLM acting as a questioner (STaR-GATE), however, existing approaches based on self-taught reasoning struggle to identify optimal dialogue trajectories and avoid irrelevant questions to the tasks.

TO-GATE enhances question generation through trajectory optimization, which consists of two key components: a clarification resolver that generates optimal questioning trajectories, and a summarizer.

### Technical Approach
The work is motivated by Direct Preference Optimization (DPO), and proposes TO-GATE that can clarify questions and summarize final responses with trajectory optimization, aiming to improve the ability of LLM-base agents to ask effective questions.

The clarification resolver adopts DPO strategies to positively reward effective conversations and penalize bad conversations, and the summarizer adopts adaptive weights to enable questioner to summarize better responses based on the historical conversations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa593dd3-ed6f-4db4-85c5-6c0bef5c3643",
  "isSidechain": false,
  "promptId": "8e027af5-c865-4fca-a4f0-0fbd9d0d39f8",
  "type": "user",
  "uuid": "1325c3a0-8e20-4708-8b7f-516b5615a356",
  "toolUseResult": {
    "query": "TO-GATE trajectory optimization clarifying questions DPO arXiv 2506.02827 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ScMwdUn3AhpvtNmEbitV5P",
        "content": [
          {
            "title": "[2506.02827] TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference",
            "url": "https://arxiv.org/abs/2506.02827"
          },
          {
            "title": "TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference",
            "url": "https://arxiv.org/html/2506.02827"
          },
          {
            "title": "TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference",
            "url": "https://www.researchgate.net/publication/392371683_TO-GATE_Clarifying_Questions_and_Summarizing_Responses_with_Trajectory_Optimization_for_Eliciting_Human_Preference"
          },
          {
            "title": "Offline RL by Reward-Weighted Fine-Tuning for Conversation Optimization",
            "url": "https://arxiv.org/html/2506.06964"
          },
          {
            "title": "Learning to Clarify by Reinforcement Learning Through Reward-Weighted Fine-Tuning",
            "url": "https://arxiv.org/html/2506.06964v1"
          },
          {
            "title": "Optimal Trajectory Planning for Space Object Tracking with Collision-Avoidance Constraints",
            "url": "https://arxiv.org/html/2506.22797v1"
          },
          {
            "title": "STaR-GATE: Teaching Language Models to Ask Clarifying Questions",
            "url": "https://arxiv.org/html/2403.19154v2"
          },
          {
            "title": "Smoothed Preference Optimization via ReNoise Inversion for Aligning Diffusion Models with Varied Human Preferences",
            "url": "https://arxiv.org/html/2506.02698"
          },
          {
            "title": "Ch. 10 - Trajectory Optimization - Underactuated Robotics",
            "url": "https://underactuated.mit.edu/trajopt.html"
          },
          {
            "title": "Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms",
            "url": "https://arxiv.org/html/2506.09457"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper arXiv:2506.02827.\n\n## TO-GATE: Trajectory Optimization for Clarifying Questions with DPO\n\nTO-GATE is a framework titled \"Clarifying Questions and Summarizing Responses with Trajectory Optimization for Eliciting Human Preference\".\n\n### Overview\nThe paper was submitted on June 3, 2025, and authored by Yulin Dou and Jiangming Liu. Large language models (LLMs) can effectively elicit human preferences through multi-turn dialogue.\n\n### Problem and Solution\nComplex tasks can be accomplished through iterative clarifying questions and final responses generated by an LLM acting as a questioner (STaR-GATE), however, existing approaches based on self-taught reasoning struggle to identify optimal dialogue trajectories and avoid irrelevant questions to the tasks.\n\nTO-GATE enhances question generation through trajectory optimization, which consists of two key components: a clarification resolver that generates optimal questioning trajectories, and a summarizer.\n\n### Technical Approach\nThe work is motivated by Direct Preference Optimization (DPO), and proposes TO-GATE that can clarify questions and summarize final responses with trajectory optimization, aiming to improve the ability of LLM-base agents to ask effective questions.\n\nThe clarification resolver adopts DPO strategies to positively reward effective conversations and penalize bad conversations, and the summarizer adopts adaptive weights to enable questioner to summarize better responses based on the historical conversations."
    ],
    "durationSeconds": 6.977729305999993
  },
  "sourceToolAssistantUUID": "fa593dd3-ed6f-4db4-85c5-6c0bef5c3643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-10T08:15:49.948Z_

<details><summary>Logged reasoning block</summary>

```text
Good. TO-GATE exists (arXiv 2506.02827). It was submitted June 2025, so it's a valid concurrent/adjacent work. The proposal correctly characterizes it as using trajectory-level DPO, remaining non-Bayesian and not maintaining explicit preference hypotheses or a posterior.

Now let me assess the overall proposal more carefully. Let me note some key findings from my research:

1. AdaptFuse (arXiv 2604.03925) confirmed - does not use warm-start from demonstrations, does not use EIG-based active selection, no disconfirmation probes, evaluated on recommendation domains (not LLM response-style personalization). 

The characterizations check out. I've verified the other key works too: BED-LLM (arXiv 2508.21184, ICLR 2026), PROSE (arXiv 2505.23815, ICML 2025), HyPerAlign (arXiv 2505.00038), and AMPLe (arXiv 2411.00524, ACL 2025) all exist and are correctly characterized. The PersonalLLM benchmark is publicly available on HuggingFace, and the venue deadline is confirmed as May 25, 2026.

I've also confirmed "Failing to Falsify" (arXiv 2604.02485) and TO-GATE (arXiv 2506.02827), which implements trajectory-level DPO without Bayesian assumptions.

Now I'm reviewing what's been addressed: the circular self-evaluation issue in Stage 2a is handled through cross-model ρ checking with Llama-3.1-8B and an explicit fallback if cross-model ρ drops below 0.6, the human study is now properly framed as underpowered and descriptive, and both AdaptFuse and MAPLE are now cited and differentiated. Still need to check whether CoPL (arXiv 2503.01658, EMNLP 2025) on collaborative preference learning for personalizing LLMs should be included.

CoPL uses graph-based collaborative filtering with mixture of LoRA experts on the PersonalLLM benchmark, which is a different approach from FABEL's tuning-free Bayesian preference elicitation, though it does overlap on the same benchmark. Since it's fine-tuning based rather than tuning-free, it's not directly aligned with FABEL's direction, but it might still warrant a citation for completeness.

After eight rounds of revision, the proposal has covered all major citation gaps and the venue deadline is correct, with compute requirements staying within the 200 H100 limit.

Now I'm noticing a potential issue with how the EIG pool handles disconfirmation probes under the factored posterior approximation—when the posterior is well-specified, there might be some subtle interaction I need to think through more carefully. -calibrated warm prior, the disconfirmation probes H_neg would have very low probability (already near 0) from the start. If their probability is already near 0, their posterior entropy H(p(h_i)) ≈ -ε*log(ε) - (1-ε)*log(1-ε) ≈ 0, meaning they would NOT be near log(2) and would NOT be selected by EIG. So the quota mechanism compensates for this. The proposal correctly includes the soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns). This seems fine.

Actually wait - this is a more subtle issue. If the warm prior assigns high probability to H_neg being FALSE (i.e., p(h_neg = true) is near 0), then the posterior entropy is low, and EIG won't select them. But the real insight is that the disconfirmation probes serve as a calibration diagnostic - if the prior is miscalibrated and doesn't correctly identify them as false, they'd have high entropy and get selected naturally. The soft minimum quota ensures we still test some of them even when the model is confident they're false, providing genuine falsification validation.

The remaining unasked disconfirmation probes (those not selected by EIG or quota) remain in the posterior as "probably false" but unconfirmed. This is a minor limitation - we're assuming their falsity without direct user validation - but it's acceptable given the quota ensures at least some are tested.

Now I'm thinking through how the binary confirmation question maps onto the EIG calculation. For a hypothesis like "User prefers bulleted structure," we ask a yes/no confirmation, and EIG needs the probability of yes under both h_i true and h_i false. The proposal leverages the factored posterior assumption to simplify this: for binary hypotheses, maximizing marginal entropy is equivalent to EIG-based selection, which elegantly sidesteps needing to specify those conditional response probabilities explicitly.

But there's a gap in the noise model specification—the proposal mentions calibrating it on held-out demo pairs, but doesn't detail how that calibration actually works, which could be a reviewer concern. There's also the BED-LLM reimplementation risk: if the 3-4 agent-day time-box forces a fallback to the entropy-based approximation without full RB-EIG, then the comparison between FABEL and this simplified baseline might not actually demonstrate the value of the more complex approach. the proposal appropriately flags this as a limitation and is transparent about the potential fallback, though reviewers might still raise concerns about it. I'm now checking whether the cited "Noisy but Valid" paper actually exists and accurately characterizes the hypothesis testing framework for cross-model evaluation. After reviewing the proposal across multiple iterations, the core novelty seems solid—the combination of demonstration-conditioned Bayesian priors with temperature scaling, EIG-based confirmation, mandatory disconfirmation probes, and application to LLM personalization appears genuinely novel and distinct from existing work.

A few remaining concerns stand out: CoPL is an EMNLP 2025 paper on LLM personalization using the same benchmark, though it relies on LoRA fine-tuning rather than the tuning-free Bayesian approach here. The noise model calibration is somewhat underspecified—it's calibrated on held-out demo pairs but lacks full technical detail. There's also a risk if BED-LLM-approx is used instead of the full method, which would weaken the comparison. The TO-GATE paper citation appears incomplete in the proposal.

Actually, checking the timeline: TO-GATE was submitted to arXiv in June 2025, and since FABEL would be submitted to ARR in May 2026, citing a June 2025 paper is perfectly valid. So that's not an issue.

Looking at the broader landscape, FABEL's combination of warm priors from demonstrations, entropy-based binary selection, and disconfirmation probes appears genuinely novel—the concurrent works like AdaptFuse, AMPLe, and BED-LLM each address different aspects but don't combine all three elements. The main gap I'm noticing is that the noise model for the Stage 3 Bayesian update needs clarification—the proposal mentions calibrating it on held-out demo pairs but doesn't specify whether it's logistic noise, Beta-distributed, or something else.

The prolific study with n≈20 is underpowered for statistical claims, though the proposal does acknowledge this limitation and frames it appropriately as descriptive results for a stretch goal. The bigger reproducibility concern is BED-LLM's lack of public code, which the proposal flags and provides a fallback for, but this still introduces some uncertainty in the baseline comparisons.

The claim about eliminating GPT-4 costs through simulated evaluation is slightly misleading since the reward models themselves were trained on human feedback from actual LLM outputs, so the infrastructure isn't cost-free—though the evaluation approach itself is sound and well-established in the field. For Stage 2a, the proposal specifies how empirical accuracy will be measured using the top-quartile responses weighted by the ensemble reward score, which provides a concrete operationalization.

However, there's a fundamental mismatch I'm noticing: FABEL is trying to validate stylistic preference hypotheses (like "prefers bullet points") against PersonalLLM responses, but PersonalLLM's reward models are trained on general helpfulness and quality judgments, not stylistic preferences. This creates a gap—users who generate high-reward responses might have diverse stylistic preferences that don't necessarily correlate with the reward model scores, so an LLM classifier might struggle to reliably identify whether stylistic attributes are actually being satisfied.

Actually, reconsidering this: PersonalLLM does have human raters scoring multiple candidate responses, and those raters likely have different stylistic preferences alongside quality preferences. The 10 reward models trained on this data would capture that diversity. So stylistic preferences could plausibly be reflected in the benchmark, making it reasonably appropriate for testing response-style personalization.

The cross-model ρ check would add roughly a quarter agent-day of compute, which is manageable given it just requires running inference on the same 50-user dev set within the 16-day timeline. After eight rounds of revision, the proposal has resolved the major concerns, leaving only minor issues: the Bayesian noise model lacks specificity around its functional form, and CoPL (a collaborative filtering approach using the same benchmark) goes uncited. There are also some low-severity gaps to address.

Now I need to think through the verdict for Round 9. Looking at the novelty dimension, the core contribution—combining demo-conditioned warm priors with expected information gain for binary confirmation and disconfirmation probes—is genuinely novel for response-style personalization, and I've thoroughly differentiated it from prior work. Though there's some conceptual overlap with ICRM around warm priors from demonstrations, the overall approach stands on its own merits.

For a venue like EMNLP Findings, a 3.5/5 novelty score feels appropriate given the solid methodological combination. The feasibility checks out too—the 16-day MVP with PersonalLLM and Qwen2.5-7B-Instruct is realistic, the compute budget is reasonable, and the main implementation risk around BED-LLM is manageable. I'm settling on 3.5/5 for feasibility as well.

The proposal has been thoroughly refined through multiple rounds of revision, so the clarity is strong at 4/5. But impact is where I'm being honest with myself—this is fundamentally an incremental contribution, cleverly combining existing techniques like Bayesian priors, expected information gain, and confirmation/disconfirmation probes for LLM personalization. It's useful but not field-advancing, so 3/5 feels right.

That puts me at an average of 3.5, which falls short of the 4.0 threshold. I need to be strict here since reviewer scores tend to inflate, and the remaining issues—particularly around the CoP baseline comparison, noise model underspecification, and the gap between the PersonalLLM benchmark and stylistic personalization claims—keep this from being truly outstanding. Though reconsidering CoP itself, it's really a different paradigm entirely with collaborative filtering and LoRA fine-tuning, so that's not a fair comparison point. The noise model underspecification is the more legitimate concern, but it's still not a blocker.

The Bayesian update mechanism itself hinges on how noise is modeled—whether it's a simple error rate, Beta-Binomial, or logistic function—and the proposal only vaguely mentions calibration on held-out demo pairs without specifying the functional form. That's a reproducibility issue a Bayesian reviewer would rightfully flag. I'm also wondering whether the Spearman correlation threshold they use to validate the warm-start assumption is the right metric for this purpose.

Actually, I'm catching a more fundamental problem with their τ calibration approach. They claim τ is selected to maximize Spearman rank correlation with ground-truth accuracy, but Spearman ρ is rank-invariant—temperature scaling doesn't change the rank order of scores, only their magnitude. So τ shouldn't affect Spearman ρ at all, which means their calibration procedure as described is mathematically broken. Temperature scaling affects the sharpness of the distribution, not the ranking. flatness of the prior distribution, but not its rank ordering.

Actually wait - let me re-read the proposal more carefully:

"τ is selected on a held-out 50-user PersonalLLM dev split as the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6 (validation threshold)."

Hmm. τ is a temperature in p(h_i = true | demos) ∝ exp(score_i / τ). The Spearman rank correlation between these probabilities and empirical accuracies does NOT depend on τ, because dividing scores by τ preserves the rank order. So increasing τ (towards uniform) doesn't change the rank-order correlation - it only changes the actual probability values (making them more uniform or more peaked).

This means the τ selection criterion "smallest τ such that Spearman ρ > 0.6" is fundamentally flawed: since Spearman correlation is invariant to τ, either the correlation exceeds 0.6 regardless of τ (making the selection meaningless), or it never does (making no τ work). The validation criterion doesn't actually depend on τ at all, so it can't be used to calibrate the prior's sharpness. I'd need a different criterion entirely—something like expected calibration error or matching empirical win rates—to actually select τ meaningfully. I see the issue now—if Spearman ρ is independent of τ, then the criterion "smallest τ such that ρ > 0.6" becomes a binary gate: either the raw log-likelihoods correlate with empirical accuracy (use any positive τ, say τ=1) or they don't (fall back to uniform prior). So this isn't actually selecting τ continuously—it's just deciding whether to use the warm-start prior at all based on whether the LLM scores rank-correlate with ground truth. But then what actually determines the specific τ value if we do use the prior?

The real problem is that the validation step and the τ selection are being conflated. The Spearman ρ check should just validate whether warm-starting makes sense in principle, while τ itself should be chosen separately based on something like calibration or Brier score—not by chasing a correlation threshold. If ρ > 0.6, we know the warm-start is useful, and then we pick τ to control how sharp the prior becomes; if ρ ≤ 0.6, we abandon the warm-start entirely and use a uniform prior. The issue is that temperature scaling is a monotone transformation, so it doesn't change the rank ordering of scores—Spearman ρ would remain constant regardless of τ. This means the stated criterion of "smallest τ such that ρ > 0.6" is fundamentally flawed and needs to be replaced with a different approach to selecting τ.

Let me reread the proposal more carefully to make sure I'm not misunderstanding how τ is actually being selected. I'm realizing the issue here—since Spearman ρ is rank-based and temperature scaling preserves rank order, ρ should be invariant across all τ values, which means the grid search criterion doesn't actually select a specific τ unless there's something about hypothesis selection or ordering that changes with temperature. If ρ > 0.6 holds for any τ > 0, then the selection rule "smallest τ such that ρ > 0.6" would just pick τ = 1 as the minimum, but this seems like it might be missing something about how the hypothesis set itself varies with τ. min (smallest value in search grid)
- If ρ ≤ 0.6: default to τ→∞

This is a binary selection with a somewhat useless grid search. The actual τ value has no principled selection mechanism in the current formulation.

However, I realize I might be wrong about one thing: what if the Spearman ρ is computed differently? For instance, if the calibration check is computed as:
- For each user, rank the hypotheses by prior probability (which = rank by LLM log-likelihood, for any τ)
- For each user, rank the hypotheses by empirical accuracy
- Compute Spearman ρ between these two rankings
- Average over users

In this case, ρ is indeed τ-invariant. So the τ selection criterion doesn't work as stated.

For the τ selection to work, it needs to use a τ-dependent criterion. Metrics like Brier score, cross-entropy, and Expected Calibration Error all vary with τ, so any of these would work better than Spearman ρ for actually selecting τ, while keeping ρ as a separate validity check. This is a real technical error in the proposal, though it's moderate in severity—it doesn't break the approach, just requires switching to a τ-dependent calibration metric for the selection step.

The conceptual framework remains sound. Now I'm diving deeper into the Stage 3 Bayesian update to check whether the likelihood computation is properly specified, particularly how the noise term calibrated on held-out demo pairs actually enters the likelihood function.

The issue is that while the proposal mentions calibrating noise parameters on held-out demonstrations, it doesn't clarify what "demo pairs" means, how they're used to estimate the noise model, or what functional form the noise takes—all of which are essential for reproducibility. This is another underspecification that would need to be resolved.

Given these two substantive technical problems I've identified, I'm settling on a revise verdict for Round 9. The first issue is that the τ selection criterion is mathematically flawed: using Spearman correlation between LLM log-likelihoods and empirical accuracy to select τ doesn't work because correlation is invariant to temperature scaling. While the correlation threshold validates whether the warm-start helps, a separate τ-dependent criterion like Brier score or ECE minimization on the dev set is needed to actually choose τ. The second issue is the underspecified Bayesian noise model.

Looking at the evaluation scores, the work scores 3.5/5 on novelty since it's a solid methodological combination rather than a fundamental advance, 3.5/5 on feasibility with the BED-LLM reimplementation as the main risk, 4/5 on clarity despite the τ selection flaw, and 3.5/5 on impact as a reasonable EMNLP Findings paper. Clarity gets a 4 since the proposal is well-detailed despite the τ selection issue, and impact scores 3.5 as a solid EMNLP Findings contribution with useful diagnostic metrics. That puts me at 3.625 overall—still short of the 4.0 threshold. The τ flaw is a genuine technical problem but it's addressable, so I should give a revise verdict with specific guidance. Since we're at Round 9 of 10, the next round is my last chance to push this over the line.

Let me double-check the τ selection logic one more time to make sure I'm not being unfair. Looking at how they define it—using the held-out dev split to find the smallest τ where the prior Spearman correlation with ground-truth accuracy exceeds 0.6—I need to verify whether this actually creates the circularity problem I flagged or if there's a valid justification I'm overlooking. averaged over the 50 dev users."

OK! I see now - the Spearman ρ is computed between the RAW LLM log-likelihood SCORES [score_1, ..., score_N] and empirical accuracies [acc_1, ..., acc_N]. NOT between the prior probabilities p(h_i | τ) and the accuracies.

Since the comparison is between raw scores and accuracies (not between temperature-scaled probabilities and accuracies), τ has no effect on this Spearman ρ. So my earlier analysis is correct: the "smallest τ such that ρ > 0.6" is mathematically vacuous - ρ doesn't depend on τ.

The τ selection is supposed to happen separately from the ρ validation, but the proposal has confused the two by putting τ into the ρ condition. A correct reading might be:
- Step 1: Validate that ρ > 0.6 (τ-independent check on raw scores)
- Step 2: If ρ > 0.6, select τ (but there's no τ selection criterion given!)

Or alternatively, the proposal intends τ to control the sharpness of the prior independently of the ρ check, and the condition "smallest τ such that ρ > 0.6" is meant to be interpreted as: "we search over τ values and use the smallest τ that still gives ρ > 0.6 when comparing PRIOR PROBABILITIES (not raw scores) to empirical accuracy." If we're comparing prior probabilities p(h_i|τ) to empirical accuracy and using Pearson correlation, then τ would affect this correlation through the softmax nonlinearity, but the exact interpretation depends on whether we're actually swapping the comparison target from raw scores to prior probabilities.

If we're using Spearman ρ instead, temperature scaling preserves rank order for τ > 0, so the correlation would remain τ-invariant. The only way τ could matter is if we're binarizing the probabilities or thresholds, which isn't described here.

I'm now confident the τ selection criterion has a genuine mathematical flaw. The proposal should either acknowledge that the ρ check is τ-independent and specify a separate criterion for τ (like Brier score minimization), or reframe the process as: first validate ρ (which is τ-independent), then if ρ > 0.6, select τ using a calibration-based criterion.

This is a real technical gap that affects reproducibility, though it wouldn't necessarily invalidate the overall approach since τ could be set by a reasonable heuristic. I also notice the paper cites work on calibrating token-level predictions for QA tasks as motivation for FABEL's temperature scaling, but that's not directly applicable to hypothesis ranking—the citation feels somewhat disconnected.

I've gathered enough information to write the review. The verdict is revise, with the τ calibration procedure being a moderate issue: Spearman ρ is rank-invariant under monotone transformations like temperature scaling, so the criterion "smallest τ such that ρ > 0.6" doesn't actually constrain τ at all.

The fix would be to decouple the validity check (compute raw Spearman ρ between log-likelihood scores and empirical accuracies, which is τ-independent) from the actual τ calibration step (minimize Brier score or ECE on held-out data, or reference a fixed τ from prior calibration work). There's also a minor issue with Stage 3's noise model being underspecified—the functional form of the noise term isn't clearly defined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1325c3a0-8e20-4708-8b7f-516b5615a356",
  "isSidechain": false,
  "requestId": "req_011CatYz1GnWLbBys9KR3XAK",
  "type": "assistant",
  "uuid": "f7b0f10a-282c-490d-9d51-be5cd9c4bef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DVrL3jrvq4sJGeVqzCk52c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 62038,
      "output_tokens": 12824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12824,
          "cache_read_input_tokens": 62038,
          "cache_creation_input_tokens": 1875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1875
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

_source line 74 · 2026-05-10T08:16:22.802Z_

Now I have enough information to issue my verdict. Let me compile my findings.

Key verification results from independent research:
- **AdaptFuse (2604.03925)** confirmed: no warm-start from demos, no EIG, no disconfirmation probes, evaluated only on recommendation domains — generator's characterization accurate
- **BED-LLM (2508.21184, ICLR 2026)** confirmed: LM-generic prior, multiple-choice format, ~45-50 LLM calls/step
- **PROSE (2505.23815, ICML 2025)** confirmed: iterative refinement from writing samples, no interaction, no Bayesian posterior
- **PersonalLLM** confirmed publicly available at huggingface.co/datasets/namkoong-lab/PersonalLLM (CC BY-NC 4.0)
- **EMNLP 2026 ARR deadline**: confirmed May 25, 2026
- **Failing to Falsify (2604.02485)** confirmed: rule-discovery rate improves from 42% → 56% with counter-example prompting
- **AMPLe (2411.00524, ACL 2025)** confirmed with public code
- **HyPerAlign (2505.00038)** confirmed

However, I identified one significant technical flaw in the τ calibration procedure that was not caught in any prior round:

**The τ selection criterion is mathematically inconsistent.** The proposal selects τ as "the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6." But Spearman ρ is a **rank-based statistic invariant under monotone transformations** — including temperature scaling (dividing by τ > 0). The rank order of scores [score_1/τ, ..., score_N/τ] is identical to [score_1, ..., score_N] for any positive τ. Therefore, Spearman ρ between {score_i/τ} and {acc_i} equals Spearman ρ between {score_i} and {acc_i} for all τ > 0. The "smallest τ such that ρ > 0.6" is vacuous: τ has zero effect on ρ. What the procedure actually implements is a binary validity check (if raw-score ρ > 0.6, proceed; else use τ→∞), with no principled τ selection.

This is a meaningful error: τ does control prior sharpness (avoiding overconfident prior collapse, which was the whole motivation for introducing τ), but the criterion used to select τ doesn't depend on τ at all.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Independent search confirms the specific combination — user-demonstration-conditioned warm Bayesian prior + EIG binary confirmation + disconfirmation probes for LLM response-style personalization — is absent from all prior work including AdaptFuse, BED-LLM, PROSE, AMPLe, and HyPerAlign. The landscape coverage is comprehensive and the differentiation arguments are accurate."
    },
    "feasibility": {
      "score": 3,
      "rationale": "PersonalLLM dataset is publicly available, Qwen2.5-7B-Instruct is accessible, and 75h H100-equivalent is within budget; but BED-LLM has no public code and the τ calibration flaw (detailed below) means Stage 2a as written is not reproducible, adding unplanned implementation overhead."
    },
    "clarity": {
      "score": 3,
      "rationale": "After 8 rounds the proposal is largely well-specified, but the Stage 2a τ selection procedure contains a mathematical error that would confuse a careful Bayesian reviewer, and the Stage 3 noise model functional form remains unspecified."
    },
    "impact": {
      "score": 4,
      "rationale": "The warm-prior + disconfirmation diagnostic framework advances the OPEN→BED-LLM lineage in a principled way and the empirical diagnostic suite (disconfirmation selection rate, falsification rate, Spearman ρ) adds evaluative value; appropriate for EMNLP Findings and positions the method for broader personalization work."
    }
  },
  "issues": [
    "MODERATE (NEW) — Stage 2a τ selection criterion is mathematically vacuous: Spearman ρ is a rank-based statistic invariant under monotone transformations. Temperature scaling exp(score_i/τ) is a monotone transformation of raw scores, so Spearman ρ between {score_i/τ} and {acc_i} equals Spearman ρ between {score_i} and {acc_i} for every τ > 0. The condition 'smallest τ such that ρ > 0.6' therefore has no τ-dependence: it either always holds (if raw-score ρ > 0.6, which is independent of τ) or never holds. This means the proposal provides a binary validity check (warm-start useful vs. not) but no principled τ selection. Since τ IS the mechanism that prevents overconfident prior collapse (the entire motivation for its introduction), a τ-dependent selection criterion is required. Fix: decouple the ρ validity check (τ-independent) from τ calibration (τ-dependent); select τ by minimizing Brier score or Expected Calibration Error on the 50-user dev split, or cite a fixed τ heuristic from the LLM calibration literature (e.g., arXiv 2409.19817).",
    "MINOR (RESIDUAL) — Stage 3 Bayesian noise model underspecified: 'A noise term calibrated on held-out demo pairs' does not state the functional form. For binary observations, a minimal specification would be: P(Yes | h_i = true) = 1 − ε, P(Yes | h_i = false) = δ, with ε and δ calibrated on demo pairs. Without the functional form, the posterior update equation is not reproducible. One sentence suffices."
  ],
  "feedback": "This is Round 9 and one genuine mathematical flaw has survived all prior rounds. Fix it before Round 10 forces a pass/fail decision:\n\n**Fix 1 (Moderate — Stage 2a, ~2 sentences): Separate ρ validity from τ selection.** Replace 'τ is selected as the smallest value such that the prior Spearman rank correlation... exceeds 0.6' with a two-step procedure:\n1. *Validity check (τ-independent)*: Compute Spearman ρ between raw LLM log-likelihood scores [score_1, ..., score_N] and empirical accuracies [acc_1, ..., acc_N] averaged over 50 dev users. If ρ < 0.6, default to τ→∞ (warm start is not useful for this hypothesis class).\n2. *τ selection (τ-dependent)*: Given that ρ ≥ 0.6, select τ from grid {0.5, 1.0, 2.0, 5.0, ∞} by minimizing Brier score E[(p(h_i|τ) − acc_i)²] on the same 50-user dev split. This is τ-dependent and provides a principled sharpness calibration that prevents overconfident prior collapse.\n\nThe rationale: Spearman ρ measures *rank-order* alignment (does τ matter? No — any τ > 0 gives the same rank order). Brier score measures *probability-value* accuracy (does τ matter? Yes — τ controls how concentrated the probabilities are). Using ρ for the validity check and Brier score for τ selection is mathematically consistent and reproducible.\n\n**Fix 2 (Minor — Stage 3, 1 sentence): Specify noise model.** After the Bayesian update equation, add: 'We model user response noise as a symmetric error: P(Yes | h_i = true) = 1 − ε, P(Yes | h_i = false) = ε, with ε calibrated on held-out demonstration-hypothesis pairs by maximizing posterior likelihood on known hypothesis labels.'\n\nAfter these two fixes, the proposal has no remaining critical technical gaps. The novelty is verified, the landscape is comprehensive, the compute is within budget, and the experimental design is appropriate for EMNLP 2026 Findings.",
  "reason": "Stage 2a τ selection criterion is mathematically vacuous (Spearman ρ is τ-invariant under temperature scaling), requiring a two-step fix that separates the rank-validity check from a τ-dependent calibration criterion before this is ready to submit."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7b0f10a-282c-490d-9d51-be5cd9c4bef2",
  "isSidechain": false,
  "requestId": "req_011CatYz1GnWLbBys9KR3XAK",
  "type": "assistant",
  "uuid": "1390696e-8863-4745-a9c4-4f43e7189734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DVrL3jrvq4sJGeVqzCk52c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 62038,
      "output_tokens": 12824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12824,
          "cache_read_input_tokens": 62038,
          "cache_creation_input_tokens": 1875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1875
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

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1390696e-8863-4745-a9c4-4f43e7189734",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1390696e-8863-4745-a9c4-4f43e7189734",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstration-Grounded Bayesian Preference Elicitation for LLM Personalization",
  "sessionId": "cc361057-7cff-41f5-8bad-b54576537f94"
}
```

---
