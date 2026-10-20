# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/5395c75c-e1d8-4025-9db6-f1877f6d9018.jsonl`
- **Structured JSON:** [`816b8167ba969d2f5a72.json`](../../sessions/81/816b8167ba969d2f5a72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:45:07.573Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:45:07.573Z",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Human-Centered NLP and Human-AI Interaction. Aligns with EMNLP 2026 special theme on agentic workflows interfacing with human experiences.\n\nDirection: Methods that improve how humans and NLP systems collaborate. In-scope: interactive learning from human feedback (beyond vanilla RLHF), human-in-the-loop annotation methods, calibrated uncertainty communication to users, adaptive explanation generation, collaborative writing/editing systems, preference elicitation, controllable generation with user intent.\n\nContribution type: METHOD ONLY. Must propose a concrete algorithm or system mechanism — not a user study alone. Method validated via user study or simulation is ideal.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. HCI-style work is often light on compute, heavier on design and evaluation.\n2. Time: ≤16 days. Use existing open models + lightweight adaptation. If user study needed, design a small-scale simulated or crowdsourced protocol.\n3. Eval: task-specific metrics + human evaluation (inter-annotator agreement, preference rates, task completion time). Simulated user evaluation acceptable for ARR submission.\n\nLook for: adaptive interaction patterns, uncertainty-aware response generation, methods for user preference learning with minimal feedback, controllable generation beyond simple instruction following.\n\nTag: direction=human_ai_interaction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"Demonstration-Grounded Warm-Start Hypothesis Elicitation for LLM Personalization via Binary Confirmation\",\n  \"core_problem\": \"Personalizing LLMs to individual users requires efficient preference elicitation from few-shot demonstrations. Current methods exhibit three distinct failure modes: (1) Demonstration-grounded hypothesis methods (HyPerAlign) infer rich preference attributes from user examples but skip validation, risking hallucination and echo-chamber failure; (2) The BOED-for-preference-elicitation line—established by OPEN (arXiv 2403.05534, ACL 2024) and extended by BED-LLM (arXiv 2508.21184, ICLR 2026)—applies principled EIG-based adaptive questioning but initializes without user-specific demonstration-conditioned priors: OPEN uses LM-ranked feature importances as a domain-generic prior (not conditioned on any specific user's outputs); BED-LLM starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations—which is also not informed by available user examples; both waste elicitation turns on hypotheses that available user demonstrations already resolve; (3) Iterative preference inference from writing samples (PROSE, ICML 2025) refines free-form preference descriptions with component-level verification but involves no user interaction and no formal Bayesian posterior—it cannot adaptively resolve ambiguous hypotheses that demonstrations alone are insufficient to distinguish. Additionally, arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs exhibit systematic confirmation bias in hypothesis testing (42% baseline success rate), meaning LLM-generated hypothesis sets may be preferentially confirmable rather than genuinely falsifiable, causing Bayesian posteriors to converge spuriously on echo-chamber preference profiles. No existing method combines user-demonstration-conditioned warm-start Bayesian priors, EIG-based binary confirmation, and explicit disconfirmation-probe auditing in the LLM response-style personalization domain.\",\n  \"opportunity\": \"The BOED-for-preference-elicitation lineage was established by OPEN (arXiv 2403.05534, ACL 2024), which combined EIG-based query selection with LM feature extraction over pairwise item comparisons in content recommendation—but initializes from LM-ranked feature importances (a domain-generic warm start reflecting general knowledge about what features matter for news article preferences, not this user's actual examples). BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets with a Rao-Blackwellized EIG estimator and an LM-generic prior initialization p_f(θ;∅), evaluating on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions, demonstrating that EIG-based sequential Bayesian elicitation substantially outperforms prompt-only baselines. Neither OPEN nor BED-LLM exploits K specific examples of a target user's actual outputs: their initializations duplicate information that demonstrations already encode, wasting early elicitation turns. AMPLe (arXiv 2411.00524, ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation, but also cold-starts from pairwise item comparisons rather than user demonstrations and lacks disconfirmation probes. HyPerAlign (arXiv 2505.00038, May 2025) showed demonstration-grounded hypotheses yield >90% win rates but explicitly omits user validation. PROSE (arXiv 2505.23815, ICML 2025) achieves 33% improvement over CIPHER on writing-style tasks via iterative preference refinement from demonstrations, but operates entirely without user interaction—it cannot distinguish two hypotheses with similar demonstration-level support, and provides no mechanism to surface or mitigate confirmation bias. The unaddressed gap is the warm-start interactive regime: when K demonstrations are available, initializing the Bayesian prior from user-specific demonstration-conditioned LLM likelihoods—calibrated via temperature scaling to avoid overconfident prior collapse—should dramatically reduce required elicitation turns compared to both OPEN and BED-LLM (testable claim), while the interactive EIG confirmation phase resolves the residual ambiguity that passive methods like PROSE cannot address (complementary claim). A second gap concerns confirmation bias: an elicitation system that does not deliberately seed disconfirmation probes in the hypothesis pool risks producing preference profiles that reflect what an LLM expects a user to prefer rather than what the user actually prefers—an echo-chamber failure mode that HyPerAlign acknowledges but does not address, and that PROSE's component-verification step partially mitigates without fully resolving.\",\n  \"landscape\": \"The preference elicitation and personalization landscape includes eight relevant clusters. (1) Demonstration-grounded, no validation: HyPerAlign (arXiv 2505.00038, ICLR 2025 workshop) generates falsifiable-in-principle preference hypotheses from demonstrations and injects them as system prompts without user confirmation. (2) Iterative preference inference from writing samples, no interaction: PROSE (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) iteratively refines free-form preference descriptions from user writing samples via a generate→compare→update loop, then verifies preference components against held-out demonstrations with component-level scoring; achieves 33% improvement over CIPHER baseline on summarization and email writing tasks across Qwen2.5-7B/72B and GPT-4o variants; no user interaction beyond initial writing samples, no Bayesian posterior over hypotheses, no disconfirmation mechanism—the key differentiator from FABEL is that PROSE cannot adaptively resolve ambiguity beyond what demonstrations already encode and has no principled update when demonstrations are insufficient to distinguish competing hypotheses; must be included as a baseline (directly competitive with FABEL Stage 1) and explicitly differentiated. (3) The BOED-for-preference-elicitation lineage: OPEN (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) established this line by combining EIG-based query selection with LM feature extraction for content recommendation—selects pairwise queries over binary feature vectors (|F|=10, e.g., 'discusses science') using a particle-filter Bayesian update with Bradley-Terry preference model; prior initialization is via LM-ranked feature importances (domain-generic: w_i = 1.2 − 0.12i for rank i), NOT conditioned on any specific user's demonstrations; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism. BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets: samples N=15 hypotheses per turn, selects questions via Rao-Blackwellized EIG estimator (~45–50 LLM calls/step), rejection-sampling Bayesian posterior update; starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations (and notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions (a technical requirement: having a small space of single-token responses ensures p_LLM provides meaningful uncertainty over outcomes for EIG estimation); evaluates on latent preference vector inference via movie-preference multiple-choice queries and the 20-Questions game; no public code. Active Task Disambiguation (arXiv 2502.04485, ICLR 2025) similarly applies Bayesian experimental design for clarifying question selection on under-specified tasks. FABEL extends beyond all three works: (i) user-specific demonstration-conditioned warm start (K=5–10 demos from THIS user, vs. OPEN's domain-generic LM-ranked feature importances and BED-LLM's demo-agnostic LM-generic prior p_f(θ;∅)), (ii) temperature-scaled prior calibration to prevent overconfident prior collapse, (iii) binary yes/no natural-language hypothesis confirmation over free-form response-style attributes (vs. OPEN's pairwise item comparisons and BED-LLM's multiple-choice format—FABEL's binary format reduces cognitive load while remaining viable because hypothesis confirmation questions are naturally binary in ways that preference inference over open hypothesis spaces is not), (iv) mandatory disconfirmation probes in the EIG pool (absent from all prior BOED-for-preference work), (v) application to LLM response-style personalization (format, tone, structure)—a domain shift from BED-LLM's latent preference vector inference. (3b) Comparison-based active preference learning for LLM personalization: AMPLe (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) personalizes LLM outputs to implicit multi-dimensional preferences via pairwise comparison queries, a modified Bayesian posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection. AMPLe is directly adjacent to FABEL in the active Bayesian personalization space but differs in three critical ways: (1) AMPLe cold-starts from pairwise item comparisons rather than initializing from user demonstrations; (2) AMPLe asks 'which response do you prefer?' (item comparison) rather than 'does this stylistic hypothesis apply to you?' (hypothesis confirmation); (3) AMPLe includes no disconfirmation probe mechanism. AMPLe must be cited as an ACL 2025 active Bayesian personalization baseline; its comparison-based query design and FABEL's hypothesis-confirmation design represent complementary elicitation paradigms. (4) Generative open-ended elicitation: GATE (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) uses free-form LLM-generated questions in three domains; its binary yes/no variant reduces cognitive load but underperforms the open-ended variant because binary questions without a Bayesian posterior cannot adaptively narrow the hypothesis space—GATE's binary variant also does not ground questions in user demonstrations. (5) Trajectory-optimized clarification: TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior. (6) Bayesian-RL hybrid: PEBOL (arXiv 2405.00981, RecSys 2024) combines NLI-based preference beliefs with Thompson Sampling in recommendation. (7) Bayesian in-context conditioning from demonstrations (adjacent): Variational In-Context Reward Modeling / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) casts reward modeling as amortized variational inference over a latent preference with a conjugate Beta prior conditioned on in-context preference demonstrations at test time without retraining—conceptually adjacent to FABEL's warm-start initialization from demonstrations but differs in three critical ways: domain (pairwise scalar reward modeling vs. interactive response-style personalization), hypothesis representation (continuous Beta prior on scalar rewards vs. discrete binary preference hypotheses), and interaction mode (passive in-context update vs. active EIG confirmation loop); no disconfirmation probes; acknowledged in related work to pre-empt warm-start novelty challenge. (8) Few-shot preference optimization: FSPO (arXiv 2502.19312, 2025) meta-learns personalization from few-shot preference data; deferred to Phase 2 due to meta-training infrastructure overhead. The specific combination absent from all prior work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, and PROSE's non-interactive refinement.\",\n  \"approach\": \"We propose FABEL (Falsification-Aligned Binary Elicitation Loop), a tuning-free framework operating in four stages. The EMNLP 2026 submission is scoped as an MVP: PersonalLLM benchmark, four baselines, one LLM backbone (Qwen2.5-7B-Instruct), one core ablation, and a small crowdsourced human evaluation (n≈20) to strengthen the EMNLP Main case.\\n\\nStage 1—Demonstration-Grounded Hypothesis Generation with Disconfirmation Probes: Given K=5–10 few-shot user output demonstrations, a frontier open-source LLM (Qwen2.5-7B-Instruct) generates N_pos=12–15 falsifiable, binary-verifiable preference hypotheses (e.g., 'User prefers bulleted structure over prose') AND K_neg=4–6 explicit disconfirmation probes—hypotheses deliberately constructed to be easily falsifiable given the demonstrations (e.g., 'User avoids technical terminology' when demonstrations frequently use it). This two-class design, motivated by arXiv 2604.02485's finding that LLMs default to generating confirmable hypotheses, ensures the EIG pool contains falsifying evidence. To elicit genuinely falsifiable probes rather than merely low-confidence confirmatory hypotheses (the LLM default per arXiv 2604.02485), we use a dedicated generation prompt distinct from the confirmatory hypothesis prompt: 'Given these K writing samples, generate K_neg stylistic hypotheses that are plausibly true of some users but are ACTIVELY VIOLATED by the provided samples—attributes the demonstrations explicitly disconfirm. For each probe, cite the specific demonstration evidence that falsifies it. Example: if all samples use numbered lists, generate the probe \\\"User avoids numbered lists\\\" and cite the list usage as falsifying evidence.' The evidence-citing requirement prevents the model from producing vacuously non-committal probes and ensures each H_neg hypothesis is verifiably falsifiable against the provided demonstrations.\\n\\nStage 2—Temperature-Scaled Warm Prior Initialization with Calibration Check: Each hypothesis posterior is initialized as p(h_i = true | demos) ∝ exp(score_i / τ), where score_i is the LLM log-likelihood of the K demonstrations given hypothesis h_i, and τ is a temperature hyperparameter controlling prior sharpness. Raw LLM log-likelihoods are typically overconfident (τ=1); τ is selected on a held-out 50-user PersonalLLM dev split as the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6 (validation threshold). If no τ in the search grid achieves ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent, equivalent to a cold start) and flag this as a calibration failure in diagnostic analysis—indicating that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for the evaluated hypothesis class. τ→∞ recovers a uniform prior (a maximally uninformative cold start, distinct from BED-LLM's LM-generic prior p_f(θ;∅), which reflects the LLM's own unconditional distribution over hypotheses and is neither uniform nor user-specific); τ=1 applies raw likelihoods. This design directly addresses LLM miscalibration: it ensures the warm start concentrates mass on demonstration-consistent hypotheses while avoiding premature posterior collapse onto incorrect hypotheses. The calibration analysis—Stage 2a in the paper—reports Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users, validating the warm-start assumption empirically and providing a lightweight check that does not require additional model training. Empirical hypothesis accuracy is operationalized as follows: for each simulated PersonalLLM dev user u (a weighted ensemble of 10 reward models with Dirichlet-sampled weights) and each hypothesis h_i, empirical accuracy = fraction of u's top-quartile responses (by u's weighted-ensemble reward score across the 8 candidate responses per prompt) that satisfy h_i, as assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i. Spearman ρ is then computed between the vector of LLM log-likelihood scores [score_1, …, score_N] and the vector of empirical accuracies [acc_1, …, acc_N] across all N hypotheses, averaged over the 50 dev users. This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.\\n\\nStage 3—EIG-Based Binary Elicitation Loop with Disconfirmation Quota (algorithm specification): The full hypothesis set H = H_pos ∪ H_neg is placed in a single EIG-ranked pool. At each turn, FABEL selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2 — and poses it as a binary yes/no confirmation. The posterior updates via Bayes' rule with a noise term calibrated on held-out demo pairs. We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization H(p(h_i)) is equivalent to EIG-based selection. The loop terminates when joint preference entropy drops below threshold θ (empirically 3–5 turns).\\n\\nDisconfirmation probe handling follows option (a)—probes are included in the EIG pool and selected by EIG only when maximally uncertain. This is algorithmically cleanest: EIG without H_neg would face a pool containing only confirmatory hypotheses, creating a structural selection bias toward echo-chamber convergence regardless of EIG's own informativeness criterion. Including H_neg in the pool makes the probe design a prior-shaping device rather than a scheduling override—EIG's entropy criterion then serves as a bidirectional diagnostic. If H_neg probes are never selected (prior already confidently classifies them as false), this is evidence of good prior calibration; if frequently selected (probes have high posterior entropy at elicitation start), this signals prior miscalibration requiring attention.\\n\\nSoft minimum quota: To prevent the degenerate case where warm-start prior overconfidence silently suppresses all falsifying questions, at least ⌈K_neg / 3⌉ disconfirmation probes must be asked if the loop runs ≥3 turns. Quota-forced questions bypass EIG ordering for their designated turn but receive normal Bayesian updates. The 'disconfirmation selection rate'—fraction of turns where EIG (prior to quota enforcement) would have selected a H_neg hypothesis—is reported as a diagnostic distinguishing well-calibrated priors (low rate: probes already resolved by warm start) from miscalibrated ones (high rate: probes still maximally uncertain at elicitation start). The falsification rate—fraction of posterior updates that decrease hypothesis probability—is reported as a secondary diagnostic.\\n\\nStage 4—Personalized Generation: The confirmed/disconfirmed hypothesis set is injected as a structured system prompt without fine-tuning.\\n\\nMVP Experimental Design (EMNLP 2026 ARR deadline May 25, 2026):\\n- Benchmark: PersonalLLM (ICLR 2025), using its reward-model-based simulated user evaluation infrastructure (public dataset: HuggingFace namkoong-lab/PersonalLLM); simulated evaluation eliminates GPT-4-judge latency and cost, enabling full experimental sweep within the 15-day window\\n- Human evaluation study (EMNLP Main strengthening, optional stretch): n≈20 crowdsourced participants via Prolific; each participant interacts with FABEL over 10 PersonalLLM prompts and evaluates personalized vs. baseline responses; setup requires ~1 agent-day (days 3–4, running in parallel with automated experiments); cost ~$100–200; the study is underpowered for statistical inference and results are reported descriptively—it provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas, which strengthens the EMNLP Main case relative to a purely simulated evaluation\\n- Backbone: Qwen2.5-7B-Instruct (single backbone for all methods)\\n- Baselines (4): (1) HyPerAlign—demonstration-grounded, no validation; (2) GATE binary—binary questions, no Bayesian posterior, no demonstration grounding; (3) PROSE—iterative preference inference from demonstrations, no user interaction, no Bayesian posterior; applied by running PROSE's generate→compare→update pipeline on PersonalLLM demonstrations, evaluating via reward model; (4) BED-LLM—LM-generic-prior EIG Bayesian with multiple-choice questions; reimplemented from paper description (no public code; Rao-Blackwellized EIG estimator + rejection-sampling update, ~45–50 LLM calls/step); time-boxed to 3–4 agent-days with fallback to 'BED-LLM-approx' (entropy-based selection + rejection-sampling, no full RB-EIG) if faithful replication is infeasible, with explicit labeling\\n- Core ablation (1): warm-start prior (τ-scaled from demos) vs. uniform prior (τ→∞), directly isolating the demonstration-grounded initialization contribution\\n- Primary metrics: PersonalLLM reward-model win rates (main); average elicitation turns (efficiency); disconfirmation selection rate + falsification rate (diagnostics); human preference rates if study included\\n- Phase 2 extensions (camera-ready / full paper): LaMP-4/6/7 text generation benchmarks; AMPLe and FSPO baselines; full ablation battery (probes included vs. excluded; EIG vs. random ordering; K sensitivity N∈{3,5,10}; τ sensitivity; full BED-LLM replication verification); additional backbone (Qwen2.5-14B-Instruct or Llama 4 Maverick)\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"description\": \"EMNLP 2026 MVP — PRIMARY mode\",\n      \"gpu_hours\": \"~150h A100 (MVP: PersonalLLM only, 4 baselines, 1 backbone, 1 ablation)\",\n      \"h100_equivalent\": \"~75h H100-equivalent (at 2× A100/H100 throughput ratio) — explicitly within the ≤200 H100-hour hard constraint\",\n      \"gpu_utilization\": \"High (~85–90%): agent continuously queues inference jobs with no human wait time; primary idle periods are inter-job I/O and BED-LLM implementation phase\",\n      \"timeline\": \"12–14 days with 2× A100s running in parallel; Prolific human study set up days 3–4 in parallel, adding <1 agent-day overhead\",\n      \"team\": \"0 (3–5h initial setup)\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 agent reasoning turns)\",\n      \"estimated_gpu_cost\": \"$300–450 at ~$2–3/hr A100 rental\",\n      \"human_study_cost\": \"~$100–200 (n≈20 Prolific participants at ~$5–10/participant; set up in parallel days 3–4)\",\n      \"cost_notes\": \"PersonalLLM reward-model evaluation (simulated) eliminates GPT-4-judge cost; total project cost $550–900 including optional human study; Phase 2 adds ~$400–600 GPU and ~$150–300 GPT-4-judge for LaMP tasks\",\n      \"speed_bottleneck\": \"BED-LLM EIG reimplementation (no public code; time-boxed 3–4 agent-days with simplified fallback); PROSE implementation straightforward (~1 agent-day, purely prompt-based); Stage 2a calibration analysis adds ~0.5 agent-days\",\n      \"compliance_note\": \"150h A100 ÷ 2 (H100/A100 throughput ratio) = 75h H100-equivalent, well within the 200 H100-hour limit\"\n    },\n    \"human_in_loop\": {\n      \"description\": \"Full paper (post-EMNLP, adds LaMP + full ablations)\",\n      \"gpu_hours\": \"~300h A100\",\n      \"gpu_utilization\": \"Moderate (~50–60%): agent continuously queues inference jobs between human approval gates; BED-LLM replication verified at first review gate before full baseline run\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,200–2,000 reasoning turns)\",\n      \"estimated_gpu_cost\": \"$600–900\",\n      \"risk_note\": \"Warm-start prior calibration (Spearman ρ threshold) must be validated on PersonalLLM dev split before committing to full experimental sweep; τ selection and BED-LLM replication fidelity confirmed at dedicated review gates\"\n    },\n    \"manual\": {\n      \"description\": \"Full paper (post-EMNLP, adds LaMP + full ablations)\",\n      \"gpu_hours\": \"~200h A100\",\n      \"gpu_utilization\": \"Low (~20–30%): GPU idles while researchers implement BED-LLM baseline, write pipeline code, and analyze results\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"$400–600 at ~$2–3/hr A100 rental\",\n      \"cost_notes\": \"GPT-4-as-judge for LaMP evaluation adds ~$150–300; total project cost $550–900\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings via ACL ARR (deadline May 25, 2026 — 15 days from project start May 10, 2026) — PRIMARY realistic target; MVP scope (PersonalLLM, 4 baselines, 1 backbone, 1 ablation + Stage 2a calibration analysis) is credible for EMNLP Findings; adding the n≈20 Prolific human study puts EMNLP Main within reach if human results are positive — this is the stretch Main goal, not the base expectation; targets EMNLP 2026 Findings as the primary submission outcome\",\n    \"ICLR 2027 (expected submission deadline ~October 2026) — SECONDARY target if EMNLP 2026 submission scope is insufficient or if full paper (LaMP + full ablation battery) is preferred; strongest venue fit given GATE (ICLR 2025), OPEN (ACL 2024), and BED-LLM (ICLR 2026) lineage; full paper with multi-benchmark and human study comfortably meets Main bar\",\n    \"AAAI 2027 (expected abstract/paper deadline ~August–September 2026) — TERTIARY target with sufficient runway for full experimental sweep including LaMP benchmarks and multiple backbone ablations\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"OPEN: Bayesian Preference Elicitation with Language Models (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) — foundational BOED-for-preference-elicitation work; combines EIG-based query selection with LM feature extraction for content recommendation; selects pairwise queries over binary feature vectors (|F|=10) using particle-filter Bayesian update with Bradley-Terry model; prior initialization via LM-ranked feature importances (domain-generic warm start: w_i = 1.2 − 0.12i for rank i), NOT user-demonstration-conditioned; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-specific demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism; cite as the foundation of the BOED-for-preference-elicitation line that BED-LLM extends and FABEL further advances\",\n    \"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design (arXiv 2508.21184, ICLR 2026) — extends OPEN to discrete language hypothesis sets; initializes from an LM-generic prior p_f(θ;∅) (the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations; notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions as a technical requirement (small single-token response spaces ensure p_LLM provides meaningful uncertainty for EIG estimation); EIG uses Rao-Blackwellized N=15-sample estimator + rejection-sampling posterior update (~45–50 LLM calls/turn); evaluates on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions game; no public code; reimplementation time-boxed to 3–4 agent-days with simplified fallback; FABEL differentiates in three ways: (1) prior conditioned on this user's K demonstrations vs. BED-LLM's demo-agnostic LM prior; (2) binary yes/no confirmation vs. BED-LLM's multiple-choice format; (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work\",\n    \"AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) — active Bayesian preference learning for LLM personalization; pairwise comparison queries over LLM responses, modified posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection to minimize required comparisons; directly adjacent to FABEL's active Bayesian personalization setting; FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary stylistic hypothesis confirmation rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe; include as related work in landscape cluster (3b); include as Phase 2 baseline on LaMP tasks\",\n    \"PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) — directly competitive with FABEL Stage 1; iterative generate→compare→update refinement of free-form preference descriptions + component-level verification against held-out samples; 33% improvement over CIPHER on summarization/email; no user interaction, no Bayesian posterior, no disconfirmation mechanism; baseline and key differentiator\",\n    \"GATE: Eliciting Human Preferences with Language Models (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) — binary yes/no variant underperforms open-ended due to absence of Bayesian posterior; baseline\",\n    \"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation (arXiv 2505.00038, May 2025) — demonstration-grounded hypothesis generation without user validation; baseline\",\n    \"Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing (arXiv 2604.02485, April 2026) — motivates disconfirmation probe design; 42%→56% rule-discovery success with counter-example prompting; motivates H_neg pool inclusion in FABEL Stage 3\",\n    \"Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) — amortized variational inference with conjugate Beta prior conditioned on in-context preference demonstrations; conceptually adjacent to FABEL's warm-start but differs in domain (pairwise reward modeling vs. interactive style elicitation), representation (Beta prior on scalar rewards vs. binary hypothesis set), and interaction mode (passive vs. active EIG confirmation); acknowledge in related work to pre-empt warm-start novelty challenge\",\n    \"Active Task Disambiguation with LLMs (arXiv 2502.04485, ICLR 2025) — BED applied to task clarification; related but not personalization-focused\",\n    \"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization (arXiv 2506.02827, 2025) — applies trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline (a clarification resolver generating optimal questioning trajectories plus a summarizer for task-aligned responses); remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior; achieves 9.32% improvement over STaR-GATE on preference elicitation tasks; cited as an open-ended, non-Bayesian clarification baseline in landscape cluster (5)\",\n    \"PEBOL: Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation (arXiv 2405.00981, RecSys 2024) — NLI + Bayesian BO for recommendation; related\",\n    \"Asking Clarifying Questions for Preference Elicitation With Large Language Models (arXiv 2510.12015, 2025) — diffusion-inspired clarifying question model; distinct from PEBOL\",\n    \"FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users (arXiv 2502.19312, 2025) — deferred to Phase 2 / full paper; requires meta-learned model setup adds ~1–2 weeks engineering overhead\",\n    \"PersonalLLM: Tailoring LLMs to Individual Preferences (ICLR 2025) — primary benchmark; public dataset HuggingFace namkoong-lab/PersonalLLM (9,402 train / 1,000 test prompt-response pairs, 8 candidate responses per prompt scored by 10 reward models, simulated users as Dirichlet-weighted reward model ensembles); reward-model-based simulated evaluation eliminates GPT-4-judge dependency and enables 15-day timeline\",\n    \"LaMP: When Large Language Models Meet Personalization (ACL 2024) — secondary benchmark for Phase 2; LaMP-4/6/7 text generation tasks assess format and style personalization\",\n    \"Calibrating Language Models with Adaptive Temperature Scaling (arXiv 2409.19817, EMNLP 2024) — post-hoc temperature calibration method for LLM token probabilities without fine-tuning; informs FABEL's τ-scaled warm prior design: p(h_i) ∝ exp(score_i / τ) with τ selected via dev-set rank-correlation criterion\"\n  ],\n  \"description\": \"Personalizing LLMs to individual users is hindered by three complementary failure modes: HyPerAlign generates demonstration-grounded preference hypotheses but skips user validation; the BOED-for-preference-elicitation line—established by OPEN (ACL 2024) and extended by BED-LLM (ICLR 2026)—applies principled EIG-based Bayesian elicitation but lacks user-specific demonstration-conditioned priors (OPEN uses domain-generic LM-ranked feature importances; BED-LLM uses an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution, not conditioned on any specific user's demonstrations); and PROSE (ICML 2025) iteratively refines free-form preference descriptions from writing samples but has no user interaction and no formal Bayesian posterior, leaving ambiguous hypotheses unresolved. AMPLe (ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation but also cold-starts from pairwise comparisons and lacks disconfirmation probes. We propose FABEL (Falsification-Aligned Binary Elicitation Loop), which extends the OPEN→BED-LLM BOED lineage by (1) initializing a temperature-scaled warm Bayesian prior p(h_i) ∝ exp(score_i / τ) from K=5–10 user-specific demonstrations—user-specific rather than domain-generic or demo-agnostic; (2) including K_neg=4–6 explicit disconfirmation probes in the EIG-ranked hypothesis pool, generated via a dedicated falsification prompt that requires citing demonstration-level evidence for each probe, making the probe design a prior-shaping device that ensures EIG always has access to genuinely falsifying evidence; (3) applying a soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns) to prevent warm-start overconfidence from silently suppressing falsifying questions; (4) applying a factored posterior approximation with EIG-based binary yes/no confirmation (vs. BED-LLM's multiple-choice format, which is required for reliable LLM uncertainty quantification but increases cognitive load) to resolve remaining uncertainty in 3–5 turns; and (5) explicitly acknowledging that under the factored (independent) posterior approximation, marginal entropy maximization is equivalent to EIG-based selection. Stage 2a includes a calibration analysis (Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy on 50 PersonalLLM dev users, where empirical accuracy is operationalized as the fraction of each simulated user's top-quartile reward-model responses satisfying each hypothesis) that validates the warm-start assumption and selects τ; if no τ achieves ρ > 0.6, the system defaults to a uniform prior and flags the calibration failure. The EMNLP 2026 MVP targets Findings as the primary outcome, with an optional n≈20 Prolific human study (days 3–4, ~$100–200) that is underpowered for statistical inference and reported descriptively—providing a qualitative real-user signal and preliminary external validity evidence beyond simulated personas. The central testable claim: demonstration-grounded user-specific warm priors reduce required elicitation turns vs. both OPEN (domain-generic warm start) and BED-LLM (demo-agnostic LM prior) while achieving higher personalization win rates than non-interactive methods (PROSE, HyPerAlign). LaMP benchmarks, AMPLe/FSPO baselines, and full ablations are deferred to Phase 2.\",\n  \"project_name\": \"falsif_guided_pe\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"BED-LLM (arXiv 2508.21184, ICLR 2026) is unacknowledged and directly covers the core mechanism: it samples N=15 hypotheses, uses EIG to select questions designed to 'slice the hypothesis pool into roughly balanced subsets,' and applies Bayesian rejection-sampling updates — the central algorithmic contribution of FABEL. The paper must be cited and clearly differentiated.\", \"GATE (ICLR 2025) already includes a yes-or-no binary question variant ('restricts the LM to generating binary yes-or-no questions'). The generator's landscape description characterizes GATE as purely open-ended, which is factually incomplete. The binary format alone is not a differentiating contribution.\", \"PEBOL arXiv attribution error: the generator cites '(arXiv 2510.12015)' as the PEBOL paper, but arXiv 2510.12015 is 'Asking Clarifying Questions for Preference Elicitation With Large Language Models' (a diffusion-inspired model, not PEBOL). The actual PEBOL paper is arXiv 2405.00981 (RecSys 2024). This is a citable factual error that would immediately surface in peer review.\", \"Venue deadline is misidentified: the generator claims 'ACL ARR June 2026 cycle, deadline ~June 15 2026' but the confirmed EMNLP 2026 ARR submission deadline is May 25, 2026 (per official EMNLP 2026 CFP and ACL ARR Dates page). The June cycle does not feed EMNLP 2026. This affects the entire planning horizon.\", \"LLM confirmation bias undermines the 'falsification' framing: arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs systematically exhibit confirmation bias in hypothesis testing — they select confirmatory rather than falsifying evidence. This suggests that LLM-generated hypotheses will be easier to confirm than disconfirm, and the Bayesian posterior may converge spuriously. The paper should address whether its hypotheses are genuinely falsifiable or merely confirmable.\", \"PRISM benchmark misfit: PRISM (NeurIPS 2024) is designed for multicultural value alignment and subjective disagreement, not individual preference personalization of LLM response style. Evaluating FABEL — which targets writing format, structure, and tone — on PRISM is not well-motivated. The authors should justify why PRISM reveals anything beyond PersonalLLM for the proposed application.\", \"GPU cost realism: evaluating against FSPO (which requires a pretrained meta-learning model) as a baseline may require non-trivial setup not captured in the 150h A100 manual estimate; the GPT-4-as-judge costs for PersonalLLM-scale evaluation (1500 simulated users) could also be underestimated.\"]\nFeedback: The core insight — combining HyPerAlign-style demonstration-grounded hypothesis generation with EIG-based binary validation — is a coherent contribution to the personalization literature, but the generator must make three priority revisions before this is ready to submit:\n\n1. **Reposition against BED-LLM (ICLR 2026)**: 'This idea is too similar to BED-LLM (arXiv 2508.21184, ICLR 2026). Specifically, BED-LLM samples N=15 hypotheses, selects questions via EIG to split the hypothesis set, and updates beliefs with Bayesian rejection sampling — the same pipeline as FABEL. To differentiate, the generator should (a) explicitly compare against BED-LLM as a baseline, (b) emphasize FABEL's unique starting point of few-shot user demonstrations (HyPerAlign-style) rather than free-form hypothesis sampling, and (c) show that grounding hypotheses in demonstrations produces qualitatively different, more accurate preference summaries than BED-LLM's unconditioned sampling. The application domain (LLM response style vs. item recommendation) is a real differentiator worth foregrounding.'\n\n2. **Fix the GATE landscape description**: Acknowledge the GATE binary variant and clarify why FABEL differs — likely the combination of demonstration-grounded hypothesis generation (not free-form question asking) with Bayesian belief tracking is the real gap, not the binary format alone.\n\n3. **Fix the PEBOL arXiv attribution (2510.12015 → 2405.00981) and the venue deadline (June 15 → May 25).** These are immediate disqualifiers for a careful reviewer.\n\n4. **Address confirmation bias**: Add analysis or ablation showing the LLM does not systematically generate only confirmable hypotheses. Consider adding a 'disconfirmation probe' to the hypothesis set by design, or show empirically that the posterior does update in both directions.\n\nIf BED-LLM is incorporated as a strong baseline and FABEL shows clear gains on the LLM response-style personalization task (PersonalLLM win-rates, reduced user-turn word count), the contribution is publishable at EMNLP Findings level. As written, the novelty gap is insufficient for EMNLP Main.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Venue requirement failure: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, ≤16 days). The proposal itself concedes this deadline 'has effectively passed for a project beginning now (May 10, 2026)' and retargets to AAAI 2027/ICLR 2027. This is an honest but fatal mismatch: the idea as scoped cannot satisfy the user's primary hard constraint. Either a severely stripped-down MVP (PersonalLLM only, BED-LLM + HyPerAlign as the two primary baselines, no LaMP sweep, no full ablation, simulated user evaluation only) must be proposed for the 16-day window, or the idea should explicitly declare EMNLP 2026 out of scope.\", \"CRITICAL — Compute constraint non-compliance in the 16-day-feasible mode: The auto_research mode (the only mode that meets ≤16 days) uses ~600h A100. At the industry-standard ~2–2.5× H100/A100 throughput ratio, this translates to approximately 240–300 H100-hours — exceeding the ≤200 H100-hour hard constraint by 20–50%. A minimum viable experiment (PersonalLLM + 3 baselines, 1 backbone, core ablation) would likely require only ~150–180h A100 (≈75–90h H100), well within limits — but this needs to be explicitly scoped and stated rather than leaving the constraint compliance implicit.\", \"Missing citation — PROSE (arXiv 2505.23815, ICML 2025): 'Aligning LLMs by Predicting Preferences from User Writing Samples' (Aroca-Ouellette et al., Apple ML Research) uses user writing demonstrations to iteratively refine free-form preference descriptions, then verifies component claims against held-out demonstrations. This is directly competitive with FABEL Stage 1 and was not cited anywhere in the landscape. A reviewer would flag this immediately. To differentiate: PROSE infers free-form preferences with no user interaction and no Bayesian posterior; FABEL generates binary-confirmable hypotheses, tracks a formal Bayesian posterior, selects questions via EIG, and adds mandatory disconfirmation probes. PROSE should be added as a sixth baseline or at minimum a related work requiring explicit differentiation.\", \"BED-LLM reimplementation risk underestimated for 16-day window: The proposal's own auto_research note flags 'faithful replication of their rejection-sampling update' as the primary engineering risk. BED-LLM's EIG estimator involves non-trivial sampling over LLM predictive distributions at each turn. Reproducing this within a 16-day timeline — alongside implementing FABEL itself and running PersonalLLM/LaMP evaluations — is aggressive. The proposal should either identify an existing public BED-LLM implementation or explicitly time-box the reimplementation risk.\", \"ICRM / Bayesian Preference Learning for Test-Time Steerable Reward Models (arXiv 2602.08819, Feb 2026) not cited: This paper uses a Beta posterior conditioned on in-context preference demonstrations for test-time reward model steering — partial overlap with FABEL's warm-start initialization from demonstrations. The settings differ (pairwise reward modeling vs. interactive style elicitation), but the Bayesian in-context conditioning from demonstrations is directly adjacent and a reviewer familiar with this work might question the warm-start prior novelty. It should be acknowledged in the related work.\"]\nFeedback: The generator has addressed all six Round 1 issues cleanly and the core idea remains sound, but two critical problems prevent a pass verdict:\n\n**Priority 1 — Scope the idea for the actual 16-day / EMNLP 2026 constraint (or declare a mismatch).**\nThe generator honestly acknowledges EMNLP 2026 is unreachable for a full 5-baseline sweep across PersonalLLM + LaMP. But the user's hard constraint is 16 days and EMNLP 2026. The generator should choose one of:\n(a) Propose a stripped-down EMNLP 2026 MVP: PersonalLLM benchmark only, 3 baselines (HyPerAlign, BED-LLM, GATE binary), 1 LLM backbone (Qwen 3.5), simulated user evaluation using the PersonalLLM reward-model infrastructure, 1 ablation (warm vs. uniform prior). Estimated compute: ~150h A100 (~75h H100-equivalent), 12–14 days in auto mode. This fits all hard constraints.\n(b) Explicitly flag the idea as AAAI 2027 / ICLR 2027 scope with a concrete explanation of why 16 days is insufficient for the full version — so the user can make an informed decision.\n\n**Priority 2 — Add PROSE as a baseline and missing citation.**\nPROSE (arXiv 2505.23815, ICML 2025) directly competes with FABEL's Stage 1: it takes user writing samples and iteratively refines preference descriptions with component verification. Cite it, differentiate it (PROSE: free-form, non-interactive, no Bayesian posterior; FABEL: binary hypotheses, interactive EIG confirmation, formal posterior, disconfirmation probes), and include it as a baseline. Without PROSE, the novelty argument has an obvious gap that peer reviewers would flag.\n\n**Priority 3 — Fix the compute compliance in auto mode.**\nRestate the minimum-viable-experiment compute as ~150–180h A100 and explicitly confirm it falls under 200 H100-hour equivalent. The full 600h A100 ablation sweep is 'nice to have' for camera-ready, not required for ARR submission.\n\nIf the generator delivers a scoped EMNLP 2026 MVP (Priority 1) with PROSE integrated (Priority 2) and compute compliance verified (Priority 3), the idea is publishable at EMNLP 2026 Findings level. The core novelty — warm-start Bayesian initialization from demonstrations + EIG binary confirmation + mandatory disconfirmation probes — is genuinely new and the empirical design (warm vs. cold prior ablation, disconfirmation rate diagnostic) is strong. The differentiation from BED-LLM (cold start, item recommendation) and from PROSE/HyPerAlign (no interactive validation) is clean.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"OPEN (arXiv 2403.05534, ACL 2024) — 'Bayesian Preference Elicitation with Language Models' — is not cited. This paper applies Bayesian Optimal Experimental Design (BOED, mathematically equivalent to EIG) with LMs to select informative preference-elicitation questions in natural language. It is a direct algorithmic predecessor to BED-LLM for the preference elicitation setting and a reviewer aware of it would challenge FABEL's EIG-over-BED-LLM positioning. The proposal should cite OPEN as the foundation of the BOED-for-preference-elicitation line, position BED-LLM as the current state of that line, and clarify how FABEL (demonstration-grounded warm start + disconfirmation probes) extends beyond both.\", \"Disconfirmation probe / EIG interaction is algorithmically underspecified. The proposal includes K_neg=4–6 disconfirmation probes in the hypothesis set but does not specify how EIG-based selection handles them at each turn: (a) are they included in the EIG-ranked pool and selected only when EIG identifies them as maximally informative — in which case the EIG criterion may already approximate the disconfirmation behavior, making the explicit probe design partially redundant; (b) are they always asked in the first K_neg turns before EIG kicks in — which wastes turns if the demonstrations already resolved them; or (c) are they asked as post-loop audits — which breaks the Bayesian update chain. This interaction must be precisely specified in the algorithm description, since it determines whether the disconfirmation probe mechanism adds genuine information-theoretic value beyond EIG or is purely a diagnostic overlay.\", \"Warm-start prior calibration is assumed but unvalidated. The proposal initializes p(h_i = true | demonstrations) using LLM-estimated likelihoods conditioned on K demonstrations. LLM probability estimates are notoriously poorly calibrated — overconfident estimates would concentrate mass on the wrong hypotheses before any user interaction, potentially causing slower convergence than a uniform (BED-LLM-style) cold start. The paper should either (a) include an empirical calibration check showing the LLM-estimated likelihoods are well-ordered relative to ground-truth hypothesis accuracy, or (b) add a temperature-scaling or entropy-regularized prior initialization step with explicit justification.\", \"EMNLP 2026 Main vs. Findings targeting realism. The user specified EMNLP 2026 Main as the primary target. The MVP (single benchmark PersonalLLM, simulated reward-model evaluation, one backbone Qwen 3.5-7B, one ablation) is credible for EMNLP Findings but borderline for Main. EMNLP Main typically requires either (a) multi-benchmark generalization, (b) a human user study even at small scale, or (c) a theoretically novel contribution beyond component combination. The current design lacks all three. The proposal should either explicitly target Findings as the realistic primary target, or strengthen one of these dimensions — even a 20-person crowdsourced preference evaluation using the PersonalLLM prompts would substantially strengthen the Main case within the 16-day window.\"]\nFeedback: The proposal has cleanly addressed all Round 1 and Round 2 critical issues: venue deadline is correct (May 25, 2026), compute is within budget (~75h H100-equivalent), PROSE is included as baseline #3, BED-LLM is confirmed accepted at ICLR 2026, ICRM is acknowledged, and the MVP scope is explicitly and realistically defined. The core idea — warm-start Bayesian prior from demonstrations + EIG binary confirmation + disconfirmation probes — is a coherent, well-motivated contribution. Three targeted revisions will bring this to pass:\n\n**Fix 1 — Add OPEN to the landscape (1 paragraph in related work):** 'This idea is too similar to OPEN (arXiv 2403.05534, ACL 2024) without acknowledgment. OPEN applies BOED with LMs to select informative preference questions in NL — the same mathematical framework as BED-LLM, specifically for preference elicitation. To differentiate: OPEN lacks demonstration-conditioned priors, requires cold-start initialization, and has no disconfirmation mechanism. Include OPEN in the BOED lineage alongside BED-LLM and clarify that FABEL's contribution is the warm-start + disconfirmation extension of this line.'\n\n**Fix 2 — Specify disconfirmation probe algorithm precisely:** Add a paragraph to Stage 3 clarifying whether disconfirmation probes are (a) included in the EIG-ranked pool, (b) asked as mandatory initial turns, or (c) reserved as post-convergence audits. Option (a) is algorithmically cleanest — EIG will naturally select them when they are maximally uncertain, making the explicit design a prior-shaping device rather than a scheduling override. Report the empirical fraction of turns where EIG selects a disconfirmation probe vs. a positive hypothesis as a diagnostic.\n\n**Fix 3 — Calibration check or regularization for warm-start prior:** Add either (a) a small analysis showing that LLM-estimated likelihoods are well-ordered relative to demonstration-consistent hypotheses (even a rank-correlation analysis on 50 PersonalLLM examples would suffice), or (b) a temperature-scaled prior initialization: p(h_i) ∝ exp(LLM_log_likelihood / τ) with τ tuned to match empirical calibration. This directly addresses the most technically vulnerable assumption in the method.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL reproducibility error — 'Qwen 3.5-7B-Instruct' does not exist: Qwen3.5 (released Feb 2026) contains 4B, 27B, 35B-A3B (MoE), and 397B-A17B (MoE) variants; there is no 7B model in the Qwen3.5 family. This model name appears throughout the proposal as the single backbone. The correct alternatives are Qwen2.5-7B-Instruct (huggingface.co/Qwen/Qwen2.5-7B-Instruct, widely used in personalization benchmarks) or Qwen3-8B (huggingface.co/Qwen/Qwen3-8B). A reviewer or reproduction attempt would fail immediately at environment setup. Fix: replace all instances of 'Qwen 3.5-7B-Instruct' with 'Qwen2.5-7B-Instruct' or 'Qwen3-8B' with the appropriate HuggingFace identifier.\", \"Missing citation — AMPLe (arXiv 2411.00524, ACL 2025): 'Comparison-based Active Preference Learning for Multi-dimensional Personalization' (Oh, Lee, Ok; ACL 2025, with public code at github.com/ml-postech/AMPLe) uses Bayesian inference with modified posterior updates and a generalized binary-search-inspired active query selection strategy to capture implicit multi-dimensional preferences for LLM personalization — directly adjacent to FABEL's active Bayesian personalization setting. While AMPLe uses pairwise comparison queries rather than demonstration-conditioned hypotheses (making differentiation clear: FABEL provides a warm prior from demonstrations, asks binary hypothesis confirmation rather than item comparisons, and adds mandatory disconfirmation probes), the omission of an ACL 2025 active Bayesian preference learning paper in the LLM personalization domain is a gap that reviewers familiar with the area would notice. Add to the landscape under cluster (3) or create a new cluster for comparison-based active preference learning.\", \"Unstated hypothesis-independence assumption in Stage 3 Bayesian update: The per-hypothesis Bayesian update (applying Bayes' rule independently to each h_i) implicitly treats all preference hypotheses as statistically independent. In practice, preference attributes are highly correlated (e.g., 'prefers brevity' correlates with 'prefers bullet points over prose'). Under this factored approximation, the posterior update may be inconsistent: confirming 'prefers brevity' should increase the probability of correlated hypotheses, but the factored update leaves them unchanged. The proposal should either (a) acknowledge this as a stated approximation (factored posterior) in the algorithm description, or (b) briefly justify why correlations are low in the PersonalLLM hypothesis space (e.g., by reporting inter-hypothesis correlation on the dev split). This is a technical vulnerability that a Bayesian reviewer would raise.\", \"EIG terminology imprecision: Stage 3 states 'selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2' and also calls this 'EIG-based.' Maximum marginal entropy equals EIG only under the factored (independent) posterior assumption. Under a correlated posterior, maximizing joint EIG requires summing over hypotheses and is strictly different from marginal entropy maximization. Since the proposal uses a factored update, calling it 'EIG-based' is technically correct but only by virtue of the unstated independence assumption. Clarify in one sentence: 'Under the factored posterior approximation, maximizing marginal entropy H(p(h_i)) is equivalent to EIG-based selection.'\"]\nFeedback: Round 4 has resolved all three Round 3 issues cleanly: OPEN is now thoroughly cited and integrated into the BOED lineage narrative; the disconfirmation probe algorithm is precisely specified (EIG pool inclusion + soft minimum quota); and Stage 2a calibration analysis (Spearman ρ, τ selection on 50 dev users) directly addresses the warm-start prior vulnerability. The core idea is solid and publication-ready at EMNLP Findings level once the following targeted fixes are applied:\n\n**Fix 1 (Critical) — Replace non-existent model name throughout.** 'Qwen 3.5-7B-Instruct' does not exist in the Qwen3.5 family (which has 4B, 27B, and MoE variants only). Replace with 'Qwen2.5-7B-Instruct' (Qwen/Qwen2.5-7B-Instruct on HuggingFace — available, widely benchmarked) or 'Qwen3-8B' (Qwen/Qwen3-8B on HuggingFace). This affects every experimental description and the resource estimate; apply the substitution consistently.\n\n**Fix 2 (Moderate) — Cite AMPLe (arXiv 2411.00524, ACL 2025).** Add one paragraph in Section 2 (Related Work) under active preference learning: 'AMPLe (Oh et al., ACL 2025) uses Bayesian inference with modified posterior updates and active comparison-based query selection for multi-dimensional LLM personalization. FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary hypothesis confirmation (\"does this stylistic claim apply to you?\") rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe.' No ablation needed — citation and differentiation suffice.\n\n**Fix 3 (Minor) — Acknowledge hypothesis-independence assumption.** Add one sentence to Stage 3 after the Bayesian update equation: 'We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization is equivalent to EIG-based selection.' This closes both the EIG terminology issue and the independence assumption gap in one edit.\n\nAfter these three fixes, the proposal has no critical technical gaps, the venue deadline is correct, compute is within budget, and the MVP scope (PersonalLLM + 4 baselines + 1 ablation + Stage 2a calibration) is credibly executable in the 16-day window. Recommend one more targeted revision pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — BED-LLM prior characterization is factually wrong and would be caught by a reviewer who reads the paper. The proposal repeatedly says BED-LLM 'starts from cold uniform prior (no domain ranking, no user demonstrations).' However, the BED-LLM paper defines the initial prior as p_f(θ;h_t=∅) — the LLM's own predictive distribution over hypotheses given no history — which is an LM-generic prior (not uniform), analogous in spirit to OPEN's domain-generic feature importance ranking. Additionally, BED-LLM uses multiple-choice questions (not binary yes/no), because as the paper states, 'having a small space of single-token responses ensures that p_LLM provides meaningful uncertainty over outcomes.' The proposal must correct both: (a) replace 'cold uniform prior' with 'LM-generic prior, not conditioned on user demonstrations'; (b) note that FABEL uses binary yes/no confirmation (lower cognitive load) while BED-LLM uses multiple-choice. The novelty argument remains valid — FABEL's demo-conditioned prior is a real differentiator from BED-LLM's demo-agnostic LM prior — but the current phrasing is inaccurate.\", \"MINOR — Stage 2a calibration analysis is underspecified. The proposal describes 'Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users' but never operationalizes 'empirical hypothesis accuracy' for simulated users. In the PersonalLLM framework, simulated users are represented as weighted ensembles of reward models. The paper must specify: for each hypothesis h_i and each simulated user, ground truth accuracy = fraction of that user's reward-model-preferred responses that satisfy h_i (e.g., for 'prefers bullet points,' check what fraction of high-reward responses are bulleted). Without this operational definition, Stage 2a is unverifiable and a reviewer will ask exactly this question.\", \"MINOR — BED-LLM's application domain is described as 'item recommendation' throughout the proposal, but BED-LLM evaluates on both 20-Questions and preference elicitation via movie-preference multiple-choice questions — a general preference inference setting. While 'item recommendation' is partially correct, the more accurate framing is 'latent preference vector inference from sequential multiple-choice queries, without user demonstrations.' This distinction matters because FABEL's application to LLM response-style personalization (format, tone, structure) is a domain shift, not just a warm-start shift.\"]\nFeedback: Round 4 fixes have all been applied cleanly: Qwen2.5-7B-Instruct replaces the non-existent 'Qwen 3.5-7B-Instruct,' AMPLe is now cited and differentiated in cluster (3b), and the factored posterior approximation is explicitly acknowledged in Stage 3. The proposal is close to passing. Three targeted edits will get it there:\n\n**Fix 1 (Moderate, 1–2 paragraphs) — Correct the BED-LLM prior description.** Replace every instance of 'cold uniform prior' in the BED-LLM description with 'LM-generic prior (p_f(θ;∅): the LLM's unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations).' Add one clause noting that BED-LLM uses multiple-choice questions, not binary yes/no, making FABEL's binary format an additional differentiator. The revised differentiation argument: 'FABEL extends BED-LLM in three ways: (1) prior conditioned on this user's K demonstrations (vs. BED-LLM's demo-agnostic LM prior); (2) binary yes/no confirmation (vs. BED-LLM's multiple-choice format); (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work.'\n\n**Fix 2 (Minor, 1 paragraph) — Operationalize Stage 2a ground truth.** In the Stage 2a description, add: 'For each simulated PersonalLLM dev user u and hypothesis h_i, empirical accuracy = fraction of u's top-quartile reward-model responses that satisfy h_i (assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i, then comparing against the reward model's preference ordering via Kendall τ). This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.'\n\n**Fix 3 (Minor, 1 sentence) — Clarify BED-LLM domain.** Replace 'targets item recommendation' with 'targets latent preference vector inference via movie-preference multiple-choice queries' in the BED-LLM description. This sharpens the domain-shift argument: FABEL is the first to apply the OPEN→BED-LLM BOED lineage to LLM response-style personalization (format, tone, structure) from free-form demonstrations.\n\nWith these three fixes applied, the proposal has no remaining critical gaps. The combination of user-demonstration-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel, the MVP compute fits within the ≤200 H100-hour constraint, and the empirical design (warm vs. cold ablation, Stage 2a calibration, disconfirmation diagnostic) is appropriate for EMNLP Findings.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MINOR — TO-GATE related work description is inaccurate: the proposal states TO-GATE 'applies DPO to clarifying question quality, remaining in the open-ended, non-Bayesian regime,' but independent verification (arXiv 2506.02827 fetched) confirms TO-GATE uses trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline — not just clarifying question quality in isolation. While the non-Bayesian characterization is correct, the narrow phrasing 'DPO to clarifying question quality' misrepresents the method and would be flagged by a TO-GATE-aware reviewer.\", \"MINOR — Disconfirmation probe generation mechanism underspecified: Stage 1 states that Qwen2.5-7B-Instruct generates K_neg=4–6 'hypotheses deliberately constructed to be easily falsifiable given the demonstrations,' but the proposal nowhere specifies the prompt or instructions used to elicit deliberately falsifiable probes as opposed to the model's default confirmatory behavior (which is precisely what arXiv 2604.02485 shows is the default). A reviewer will ask in rebuttal: 'How do you ensure the LLM generates probes that are genuinely falsifiable rather than merely low-confidence confirmatory hypotheses?' The generation mechanism must be concretely specified.\", \"MINOR — Stage 2a τ selection failure mode unspecified: the proposal selects τ as 'the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6,' but provides no fallback if no τ achieves ρ > 0.6 (i.e., if LLM log-likelihoods are uncorrelated with empirical accuracy for some hypothesis class). A reviewer will ask what happens in this case. The paper needs one sentence: e.g., 'If no τ achieves the threshold, we default to τ→∞ (uniform prior) and report this user as a calibration failure in diagnostic analysis.'\", \"MINOR — Human study statistical power and EMNLP Main claim in tension: the proposal simultaneously acknowledges the n≈20 study is 'underpowered for significance' and asserts it 'substantially strengthens the EMNLP Main case per reviewer guidance.' These claims are contradictory. An underpowered real-user study that cannot reach statistical significance does not meaningfully distinguish FABEL from a well-designed ablation — reviewers targeting EMNLP Main will note this. The claim should be hedged to 'provides a qualitative real-user signal and preliminary external validity evidence, not statistical confirmation.'\"]\nFeedback: All Round 5 issues are cleanly resolved and independently verified: BED-LLM is confirmed ICLR 2026 (OpenReview ID: qyylZMLYT8), its LM-generic prior p_f(θ;∅) is correctly described, its multiple-choice format is noted, and its domain (latent preference vector inference, not item recommendation) is now correct. Stage 2a ground-truth operationalization is adequately specified. Four minor issues remain:\n\n**Fix 1 (1 sentence, related work):** Replace the TO-GATE description with: 'TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior.' The current phrasing ('DPO to clarifying question quality') understates the scope and would be caught by a TO-GATE-aware reviewer.\n\n**Fix 2 (1 paragraph, Stage 1):** Specify the disconfirmation probe generation prompt explicitly. Example: 'We instruct the LLM: generate K_neg hypotheses that are plausibly true of some user but LIKELY VIOLATED by the provided writing samples—stylistic attributes the demonstrations actively disconfirm. Example: if all samples use numbered lists, generate the probe \"User avoids numbered lists.\"' Without this, the mechanism is not reproducible and the novelty claim (that probes are genuinely falsifiable, not just low-confidence) is unverifiable.\n\n**Fix 3 (1 sentence, Stage 2a):** Add: 'If no τ satisfies ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent) and flag the failure in diagnostic analysis.' This closes the only remaining technical gap in the calibration procedure.\n\n**Fix 4 (1 sentence, human study description):** Replace 'substantially strengthens the EMNLP Main case' with 'provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas; the study is underpowered for statistical inference and results are reported descriptively.' This aligns the claim with the actual evidence and preempts the obvious reviewer objection.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:45:07.578Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:45:07.578Z",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-10T07:45:07.627Z_

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

## Idea under review (round 7/10)
{
  "title": "Demonstration-Grounded Warm-Start Hypothesis Elicitation for LLM Personalization via Binary Confirmation",
  "core_problem": "Personalizing LLMs to individual users requires efficient preference elicitation from few-shot demonstrations. Current methods exhibit three distinct failure modes: (1) Demonstration-grounded hypothesis methods (HyPerAlign) infer rich preference attributes from user examples but skip validation, risking hallucination and echo-chamber failure; (2) The BOED-for-preference-elicitation line—established by OPEN (arXiv 2403.05534, ACL 2024) and extended by BED-LLM (arXiv 2508.21184, ICLR 2026)—applies principled EIG-based adaptive questioning but initializes without user-specific demonstration-conditioned priors: OPEN uses LM-ranked feature importances as a domain-generic prior (not conditioned on any specific user's outputs); BED-LLM starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations—which is also not informed by available user examples; both waste elicitation turns on hypotheses that available user demonstrations already resolve; (3) Iterative preference inference from writing samples (PROSE, ICML 2025) refines free-form preference descriptions with component-level verification but involves no user interaction and no formal Bayesian posterior—it cannot adaptively resolve ambiguous hypotheses that demonstrations alone are insufficient to distinguish. Additionally, arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs exhibit systematic confirmation bias in hypothesis testing (42% baseline success rate), meaning LLM-generated hypothesis sets may be preferentially confirmable rather than genuinely falsifiable, causing Bayesian posteriors to converge spuriously on echo-chamber preference profiles. No existing method combines user-demonstration-conditioned warm-start Bayesian priors, EIG-based binary confirmation, and explicit disconfirmation-probe auditing in the LLM response-style personalization domain.",
  "opportunity": "The BOED-for-preference-elicitation lineage was established by OPEN (arXiv 2403.05534, ACL 2024), which combined EIG-based query selection with LM feature extraction over pairwise item comparisons in content recommendation—but initializes from LM-ranked feature importances (a domain-generic warm start reflecting general knowledge about what features matter for news article preferences, not this user's actual examples). BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets with a Rao-Blackwellized EIG estimator and an LM-generic prior initialization p_f(θ;∅), evaluating on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions, demonstrating that EIG-based sequential Bayesian elicitation substantially outperforms prompt-only baselines. Neither OPEN nor BED-LLM exploits K specific examples of a target user's actual outputs: their initializations duplicate information that demonstrations already encode, wasting early elicitation turns. AMPLe (arXiv 2411.00524, ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation, but also cold-starts from pairwise item comparisons rather than user demonstrations and lacks disconfirmation probes. HyPerAlign (arXiv 2505.00038, May 2025) showed demonstration-grounded hypotheses yield >90% win rates but explicitly omits user validation. PROSE (arXiv 2505.23815, ICML 2025) achieves 33% improvement over CIPHER on writing-style tasks via iterative preference refinement from demonstrations, but operates entirely without user interaction—it cannot distinguish two hypotheses with similar demonstration-level support, and provides no mechanism to surface or mitigate confirmation bias. The unaddressed gap is the warm-start interactive regime: when K demonstrations are available, initializing the Bayesian prior from user-specific demonstration-conditioned LLM likelihoods—calibrated via temperature scaling to avoid overconfident prior collapse—should dramatically reduce required elicitation turns compared to both OPEN and BED-LLM (testable claim), while the interactive EIG confirmation phase resolves the residual ambiguity that passive methods like PROSE cannot address (complementary claim). A second gap concerns confirmation bias: an elicitation system that does not deliberately seed disconfirmation probes in the hypothesis pool risks producing preference profiles that reflect what an LLM expects a user to prefer rather than what the user actually prefers—an echo-chamber failure mode that HyPerAlign acknowledges but does not address, and that PROSE's component-verification step partially mitigates without fully resolving.",
  "landscape": "The preference elicitation and personalization landscape includes eight relevant clusters. (1) Demonstration-grounded, no validation: HyPerAlign (arXiv 2505.00038, ICLR 2025 workshop) generates falsifiable-in-principle preference hypotheses from demonstrations and injects them as system prompts without user confirmation. (2) Iterative preference inference from writing samples, no interaction: PROSE (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) iteratively refines free-form preference descriptions from user writing samples via a generate→compare→update loop, then verifies preference components against held-out demonstrations with component-level scoring; achieves 33% improvement over CIPHER baseline on summarization and email writing tasks across Qwen2.5-7B/72B and GPT-4o variants; no user interaction beyond initial writing samples, no Bayesian posterior over hypotheses, no disconfirmation mechanism—the key differentiator from FABEL is that PROSE cannot adaptively resolve ambiguity beyond what demonstrations already encode and has no principled update when demonstrations are insufficient to distinguish competing hypotheses; must be included as a baseline (directly competitive with FABEL Stage 1) and explicitly differentiated. (3) The BOED-for-preference-elicitation lineage: OPEN (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) established this line by combining EIG-based query selection with LM feature extraction for content recommendation—selects pairwise queries over binary feature vectors (|F|=10, e.g., 'discusses science') using a particle-filter Bayesian update with Bradley-Terry preference model; prior initialization is via LM-ranked feature importances (domain-generic: w_i = 1.2 − 0.12i for rank i), NOT conditioned on any specific user's demonstrations; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism. BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets: samples N=15 hypotheses per turn, selects questions via Rao-Blackwellized EIG estimator (~45–50 LLM calls/step), rejection-sampling Bayesian posterior update; starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations (and notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions (a technical requirement: having a small space of single-token responses ensures p_LLM provides meaningful uncertainty over outcomes for EIG estimation); evaluates on latent preference vector inference via movie-preference multiple-choice queries and the 20-Questions game; no public code. Active Task Disambiguation (arXiv 2502.04485, ICLR 2025) similarly applies Bayesian experimental design for clarifying question selection on under-specified tasks. FABEL extends beyond all three works: (i) user-specific demonstration-conditioned warm start (K=5–10 demos from THIS user, vs. OPEN's domain-generic LM-ranked feature importances and BED-LLM's demo-agnostic LM-generic prior p_f(θ;∅)), (ii) temperature-scaled prior calibration to prevent overconfident prior collapse, (iii) binary yes/no natural-language hypothesis confirmation over free-form response-style attributes (vs. OPEN's pairwise item comparisons and BED-LLM's multiple-choice format—FABEL's binary format reduces cognitive load while remaining viable because hypothesis confirmation questions are naturally binary in ways that preference inference over open hypothesis spaces is not), (iv) mandatory disconfirmation probes in the EIG pool (absent from all prior BOED-for-preference work), (v) application to LLM response-style personalization (format, tone, structure)—a domain shift from BED-LLM's latent preference vector inference. (3b) Comparison-based active preference learning for LLM personalization: AMPLe (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) personalizes LLM outputs to implicit multi-dimensional preferences via pairwise comparison queries, a modified Bayesian posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection. AMPLe is directly adjacent to FABEL in the active Bayesian personalization space but differs in three critical ways: (1) AMPLe cold-starts from pairwise item comparisons rather than initializing from user demonstrations; (2) AMPLe asks 'which response do you prefer?' (item comparison) rather than 'does this stylistic hypothesis apply to you?' (hypothesis confirmation); (3) AMPLe includes no disconfirmation probe mechanism. AMPLe must be cited as an ACL 2025 active Bayesian personalization baseline; its comparison-based query design and FABEL's hypothesis-confirmation design represent complementary elicitation paradigms. (4) Generative open-ended elicitation: GATE (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) uses free-form LLM-generated questions in three domains; its binary yes/no variant reduces cognitive load but underperforms the open-ended variant because binary questions without a Bayesian posterior cannot adaptively narrow the hypothesis space—GATE's binary variant also does not ground questions in user demonstrations. (5) Trajectory-optimized clarification: TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior. (6) Bayesian-RL hybrid: PEBOL (arXiv 2405.00981, RecSys 2024) combines NLI-based preference beliefs with Thompson Sampling in recommendation. (7) Bayesian in-context conditioning from demonstrations (adjacent): Variational In-Context Reward Modeling / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) casts reward modeling as amortized variational inference over a latent preference with a conjugate Beta prior conditioned on in-context preference demonstrations at test time without retraining—conceptually adjacent to FABEL's warm-start initialization from demonstrations but differs in three critical ways: domain (pairwise scalar reward modeling vs. interactive response-style personalization), hypothesis representation (continuous Beta prior on scalar rewards vs. discrete binary preference hypotheses), and interaction mode (passive in-context update vs. active EIG confirmation loop); no disconfirmation probes; acknowledged in related work to pre-empt warm-start novelty challenge. (8) Few-shot preference optimization: FSPO (arXiv 2502.19312, 2025) meta-learns personalization from few-shot preference data; deferred to Phase 2 due to meta-training infrastructure overhead. The specific combination absent from all prior work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, and PROSE's non-interactive refinement.",
  "approach": "We propose FABEL (Falsification-Aligned Binary Elicitation Loop), a tuning-free framework operating in four stages. The EMNLP 2026 submission is scoped as an MVP: PersonalLLM benchmark, four baselines, one LLM backbone (Qwen2.5-7B-Instruct), one core ablation, and a small crowdsourced human evaluation (n≈20) to strengthen the EMNLP Main case.\n\nStage 1—Demonstration-Grounded Hypothesis Generation with Disconfirmation Probes: Given K=5–10 few-shot user output demonstrations, a frontier open-source LLM (Qwen2.5-7B-Instruct) generates N_pos=12–15 falsifiable, binary-verifiable preference hypotheses (e.g., 'User prefers bulleted structure over prose') AND K_neg=4–6 explicit disconfirmation probes—hypotheses deliberately constructed to be easily falsifiable given the demonstrations (e.g., 'User avoids technical terminology' when demonstrations frequently use it). This two-class design, motivated by arXiv 2604.02485's finding that LLMs default to generating confirmable hypotheses, ensures the EIG pool contains falsifying evidence. To elicit genuinely falsifiable probes rather than merely low-confidence confirmatory hypotheses (the LLM default per arXiv 2604.02485), we use a dedicated generation prompt distinct from the confirmatory hypothesis prompt: 'Given these K writing samples, generate K_neg stylistic hypotheses that are plausibly true of some users but are ACTIVELY VIOLATED by the provided samples—attributes the demonstrations explicitly disconfirm. For each probe, cite the specific demonstration evidence that falsifies it. Example: if all samples use numbered lists, generate the probe \"User avoids numbered lists\" and cite the list usage as falsifying evidence.' The evidence-citing requirement prevents the model from producing vacuously non-committal probes and ensures each H_neg hypothesis is verifiably falsifiable against the provided demonstrations.\n\nStage 2—Temperature-Scaled Warm Prior Initialization with Calibration Check: Each hypothesis posterior is initialized as p(h_i = true | demos) ∝ exp(score_i / τ), where score_i is the LLM log-likelihood of the K demonstrations given hypothesis h_i, and τ is a temperature hyperparameter controlling prior sharpness. Raw LLM log-likelihoods are typically overconfident (τ=1); τ is selected on a held-out 50-user PersonalLLM dev split as the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6 (validation threshold). If no τ in the search grid achieves ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent, equivalent to a cold start) and flag this as a calibration failure in diagnostic analysis—indicating that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for the evaluated hypothesis class. τ→∞ recovers a uniform prior (a maximally uninformative cold start, distinct from BED-LLM's LM-generic prior p_f(θ;∅), which reflects the LLM's own unconditional distribution over hypotheses and is neither uniform nor user-specific); τ=1 applies raw likelihoods. This design directly addresses LLM miscalibration: it ensures the warm start concentrates mass on demonstration-consistent hypotheses while avoiding premature posterior collapse onto incorrect hypotheses. The calibration analysis—Stage 2a in the paper—reports Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users, validating the warm-start assumption empirically and providing a lightweight check that does not require additional model training. Empirical hypothesis accuracy is operationalized as follows: for each simulated PersonalLLM dev user u (a weighted ensemble of 10 reward models with Dirichlet-sampled weights) and each hypothesis h_i, empirical accuracy = fraction of u's top-quartile responses (by u's weighted-ensemble reward score across the 8 candidate responses per prompt) that satisfy h_i, as assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i. Spearman ρ is then computed between the vector of LLM log-likelihood scores [score_1, …, score_N] and the vector of empirical accuracies [acc_1, …, acc_N] across all N hypotheses, averaged over the 50 dev users. This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.\n\nStage 3—EIG-Based Binary Elicitation Loop with Disconfirmation Quota (algorithm specification): The full hypothesis set H = H_pos ∪ H_neg is placed in a single EIG-ranked pool. At each turn, FABEL selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2 — and poses it as a binary yes/no confirmation. The posterior updates via Bayes' rule with a noise term calibrated on held-out demo pairs. We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization H(p(h_i)) is equivalent to EIG-based selection. The loop terminates when joint preference entropy drops below threshold θ (empirically 3–5 turns).\n\nDisconfirmation probe handling follows option (a)—probes are included in the EIG pool and selected by EIG only when maximally uncertain. This is algorithmically cleanest: EIG without H_neg would face a pool containing only confirmatory hypotheses, creating a structural selection bias toward echo-chamber convergence regardless of EIG's own informativeness criterion. Including H_neg in the pool makes the probe design a prior-shaping device rather than a scheduling override—EIG's entropy criterion then serves as a bidirectional diagnostic. If H_neg probes are never selected (prior already confidently classifies them as false), this is evidence of good prior calibration; if frequently selected (probes have high posterior entropy at elicitation start), this signals prior miscalibration requiring attention.\n\nSoft minimum quota: To prevent the degenerate case where warm-start prior overconfidence silently suppresses all falsifying questions, at least ⌈K_neg / 3⌉ disconfirmation probes must be asked if the loop runs ≥3 turns. Quota-forced questions bypass EIG ordering for their designated turn but receive normal Bayesian updates. The 'disconfirmation selection rate'—fraction of turns where EIG (prior to quota enforcement) would have selected a H_neg hypothesis—is reported as a diagnostic distinguishing well-calibrated priors (low rate: probes already resolved by warm start) from miscalibrated ones (high rate: probes still maximally uncertain at elicitation start). The falsification rate—fraction of posterior updates that decrease hypothesis probability—is reported as a secondary diagnostic.\n\nStage 4—Personalized Generation: The confirmed/disconfirmed hypothesis set is injected as a structured system prompt without fine-tuning.\n\nMVP Experimental Design (EMNLP 2026 ARR deadline May 25, 2026):\n- Benchmark: PersonalLLM (ICLR 2025), using its reward-model-based simulated user evaluation infrastructure (public dataset: HuggingFace namkoong-lab/PersonalLLM); simulated evaluation eliminates GPT-4-judge latency and cost, enabling full experimental sweep within the 15-day window\n- Human evaluation study (EMNLP Main strengthening, optional stretch): n≈20 crowdsourced participants via Prolific; each participant interacts with FABEL over 10 PersonalLLM prompts and evaluates personalized vs. baseline responses; setup requires ~1 agent-day (days 3–4, running in parallel with automated experiments); cost ~$100–200; the study is underpowered for statistical inference and results are reported descriptively—it provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas, which strengthens the EMNLP Main case relative to a purely simulated evaluation\n- Backbone: Qwen2.5-7B-Instruct (single backbone for all methods)\n- Baselines (4): (1) HyPerAlign—demonstration-grounded, no validation; (2) GATE binary—binary questions, no Bayesian posterior, no demonstration grounding; (3) PROSE—iterative preference inference from demonstrations, no user interaction, no Bayesian posterior; applied by running PROSE's generate→compare→update pipeline on PersonalLLM demonstrations, evaluating via reward model; (4) BED-LLM—LM-generic-prior EIG Bayesian with multiple-choice questions; reimplemented from paper description (no public code; Rao-Blackwellized EIG estimator + rejection-sampling update, ~45–50 LLM calls/step); time-boxed to 3–4 agent-days with fallback to 'BED-LLM-approx' (entropy-based selection + rejection-sampling, no full RB-EIG) if faithful replication is infeasible, with explicit labeling\n- Core ablation (1): warm-start prior (τ-scaled from demos) vs. uniform prior (τ→∞), directly isolating the demonstration-grounded initialization contribution\n- Primary metrics: PersonalLLM reward-model win rates (main); average elicitation turns (efficiency); disconfirmation selection rate + falsification rate (diagnostics); human preference rates if study included\n- Phase 2 extensions (camera-ready / full paper): LaMP-4/6/7 text generation benchmarks; AMPLe and FSPO baselines; full ablation battery (probes included vs. excluded; EIG vs. random ordering; K sensitivity N∈{3,5,10}; τ sensitivity; full BED-LLM replication verification); additional backbone (Qwen2.5-14B-Instruct or Llama 4 Maverick)",
  "resource_estimate": {
    "auto_research": {
      "description": "EMNLP 2026 MVP — PRIMARY mode",
      "gpu_hours": "~150h A100 (MVP: PersonalLLM only, 4 baselines, 1 backbone, 1 ablation)",
      "h100_equivalent": "~75h H100-equivalent (at 2× A100/H100 throughput ratio) — explicitly within the ≤200 H100-hour hard constraint",
      "gpu_utilization": "High (~85–90%): agent continuously queues inference jobs with no human wait time; primary idle periods are inter-job I/O and BED-LLM implementation phase",
      "timeline": "12–14 days with 2× A100s running in parallel; Prolific human study set up days 3–4 in parallel, adding <1 agent-day overhead",
      "team": "0 (3–5h initial setup)",
      "claude_api_cost": "$150–250 (~1,500–2,500 agent reasoning turns)",
      "estimated_gpu_cost": "$300–450 at ~$2–3/hr A100 rental",
      "human_study_cost": "~$100–200 (n≈20 Prolific participants at ~$5–10/participant; set up in parallel days 3–4)",
      "cost_notes": "PersonalLLM reward-model evaluation (simulated) eliminates GPT-4-judge cost; total project cost $550–900 including optional human study; Phase 2 adds ~$400–600 GPU and ~$150–300 GPT-4-judge for LaMP tasks",
      "speed_bottleneck": "BED-LLM EIG reimplementation (no public code; time-boxed 3–4 agent-days with simplified fallback); PROSE implementation straightforward (~1 agent-day, purely prompt-based); Stage 2a calibration analysis adds ~0.5 agent-days",
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
      "risk_note": "Warm-start prior calibration (Spearman ρ threshold) must be validated on PersonalLLM dev split before committing to full experimental sweep; τ selection and BED-LLM replication fidelity confirmed at dedicated review gates"
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
    "EMNLP 2026 Findings via ACL ARR (deadline May 25, 2026 — 15 days from project start May 10, 2026) — PRIMARY realistic target; MVP scope (PersonalLLM, 4 baselines, 1 backbone, 1 ablation + Stage 2a calibration analysis) is credible for EMNLP Findings; adding the n≈20 Prolific human study puts EMNLP Main within reach if human results are positive — this is the stretch Main goal, not the base expectation; targets EMNLP 2026 Findings as the primary submission outcome",
    "ICLR 2027 (expected submission deadline ~October 2026) — SECONDARY target if EMNLP 2026 submission scope is insufficient or if full paper (LaMP + full ablation battery) is preferred; strongest venue fit given GATE (ICLR 2025), OPEN (ACL 2024), and BED-LLM (ICLR 2026) lineage; full paper with multi-benchmark and human study comfortably meets Main bar",
    "AAAI 2027 (expected abstract/paper deadline ~August–September 2026) — TERTIARY target with sufficient runway for full experimental sweep including LaMP benchmarks and multiple backbone ablations"
  ],
  "level": "solid",
  "key_references": [
    "OPEN: Bayesian Preference Elicitation with Language Models (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) — foundational BOED-for-preference-elicitation work; combines EIG-based query selection with LM feature extraction for content recommendation; selects pairwise queries over binary feature vectors (|F|=10) using particle-filter Bayesian update with Bradley-Terry model; prior initialization via LM-ranked feature importances (domain-generic warm start: w_i = 1.2 − 0.12i for rank i), NOT user-demonstration-conditioned; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-specific demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism; cite as the foundation of the BOED-for-preference-elicitation line that BED-LLM extends and FABEL further advances",
    "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design (arXiv 2508.21184, ICLR 2026) — extends OPEN to discrete language hypothesis sets; initializes from an LM-generic prior p_f(θ;∅) (the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations; notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions as a technical requirement (small single-token response spaces ensure p_LLM provides meaningful uncertainty for EIG estimation); EIG uses Rao-Blackwellized N=15-sample estimator + rejection-sampling posterior update (~45–50 LLM calls/turn); evaluates on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions game; no public code; reimplementation time-boxed to 3–4 agent-days with simplified fallback; FABEL differentiates in three ways: (1) prior conditioned on this user's K demonstrations vs. BED-LLM's demo-agnostic LM prior; (2) binary yes/no confirmation vs. BED-LLM's multiple-choice format; (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work",
    "AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) — active Bayesian preference learning for LLM personalization; pairwise comparison queries over LLM responses, modified posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection to minimize required comparisons; directly adjacent to FABEL's active Bayesian personalization setting; FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary stylistic hypothesis confirmation rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe; include as related work in landscape cluster (3b); include as Phase 2 baseline on LaMP tasks",
    "PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) — directly competitive with FABEL Stage 1; iterative generate→compare→update refinement of free-form preference descriptions + component-level verification against held-out samples; 33% improvement over CIPHER on summarization/email; no user interaction, no Bayesian posterior, no disconfirmation mechanism; baseline and key differentiator",
    "GATE: Eliciting Human Preferences with Language Models (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) — binary yes/no variant underperforms open-ended due to absence of Bayesian posterior; baseline",
    "HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation (arXiv 2505.00038, May 2025) — demonstration-grounded hypothesis generation without user validation; baseline",
    "Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing (arXiv 2604.02485, April 2026) — motivates disconfirmation probe design; 42%→56% rule-discovery success with counter-example prompting; motivates H_neg pool inclusion in FABEL Stage 3",
    "Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) — amortized variational inference with conjugate Beta prior conditioned on in-context preference demonstrations; conceptually adjacent to FABEL's warm-start but differs in domain (pairwise reward modeling vs. interactive style elicitation), representation (Beta prior on scalar rewards vs. binary hypothesis set), and interaction mode (passive vs. active EIG confirmation); acknowledge in related work to pre-empt warm-start novelty challenge",
    "Active Task Disambiguation with LLMs (arXiv 2502.04485, ICLR 2025) — BED applied to task clarification; related but not personalization-focused",
    "TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization (arXiv 2506.02827, 2025) — applies trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline (a clarification resolver generating optimal questioning trajectories plus a summarizer for task-aligned responses); remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior; achieves 9.32% improvement over STaR-GATE on preference elicitation tasks; cited as an open-ended, non-Bayesian clarification baseline in landscape cluster (5)",
    "PEBOL: Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation (arXiv 2405.00981, RecSys 2024) — NLI + Bayesian BO for recommendation; related",
    "Asking Clarifying Questions for Preference Elicitation With Large Language Models (arXiv 2510.12015, 2025) — diffusion-inspired clarifying question model; distinct from PEBOL",
    "FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users (arXiv 2502.19312, 2025) — deferred to Phase 2 / full paper; requires meta-learned model setup adds ~1–2 weeks engineering overhead",
    "PersonalLLM: Tailoring LLMs to Individual Preferences (ICLR 2025) — primary benchmark; public dataset HuggingFace namkoong-lab/PersonalLLM (9,402 train / 1,000 test prompt-response pairs, 8 candidate responses per prompt scored by 10 reward models, simulated users as Dirichlet-weighted reward model ensembles); reward-model-based simulated evaluation eliminates GPT-4-judge dependency and enables 15-day timeline",
    "LaMP: When Large Language Models Meet Personalization (ACL 2024) — secondary benchmark for Phase 2; LaMP-4/6/7 text generation tasks assess format and style personalization",
    "Calibrating Language Models with Adaptive Temperature Scaling (arXiv 2409.19817, EMNLP 2024) — post-hoc temperature calibration method for LLM token probabilities without fine-tuning; informs FABEL's τ-scaled warm prior design: p(h_i) ∝ exp(score_i / τ) with τ selected via dev-set rank-correlation criterion"
  ],
  "description": "Personalizing LLMs to individual users is hindered by three complementary failure modes: HyPerAlign generates demonstration-grounded preference hypotheses but skips user validation; the BOED-for-preference-elicitation line—established by OPEN (ACL 2024) and extended by BED-LLM (ICLR 2026)—applies principled EIG-based Bayesian elicitation but lacks user-specific demonstration-conditioned priors (OPEN uses domain-generic LM-ranked feature importances; BED-LLM uses an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution, not conditioned on any specific user's demonstrations); and PROSE (ICML 2025) iteratively refines free-form preference descriptions from writing samples but has no user interaction and no formal Bayesian posterior, leaving ambiguous hypotheses unresolved. AMPLe (ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation but also cold-starts from pairwise comparisons and lacks disconfirmation probes. We propose FABEL (Falsification-Aligned Binary Elicitation Loop), which extends the OPEN→BED-LLM BOED lineage by (1) initializing a temperature-scaled warm Bayesian prior p(h_i) ∝ exp(score_i / τ) from K=5–10 user-specific demonstrations—user-specific rather than domain-generic or demo-agnostic; (2) including K_neg=4–6 explicit disconfirmation probes in the EIG-ranked hypothesis pool, generated via a dedicated falsification prompt that requires citing demonstration-level evidence for each probe, making the probe design a prior-shaping device that ensures EIG always has access to genuinely falsifying evidence; (3) applying a soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns) to prevent warm-start overconfidence from silently suppressing falsifying questions; (4) applying a factored posterior approximation with EIG-based binary yes/no confirmation (vs. BED-LLM's multiple-choice format, which is required for reliable LLM uncertainty quantification but increases cognitive load) to resolve remaining uncertainty in 3–5 turns; and (5) explicitly acknowledging that under the factored (independent) posterior approximation, marginal entropy maximization is equivalent to EIG-based selection. Stage 2a includes a calibration analysis (Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy on 50 PersonalLLM dev users, where empirical accuracy is operationalized as the fraction of each simulated user's top-quartile reward-model responses satisfying each hypothesis) that validates the warm-start assumption and selects τ; if no τ achieves ρ > 0.6, the system defaults to a uniform prior and flags the calibration failure. The EMNLP 2026 MVP targets Findings as the primary outcome, with an optional n≈20 Prolific human study (days 3–4, ~$100–200) that is underpowered for statistical inference and reported descriptively—providing a qualitative real-user signal and preliminary external validity evidence beyond simulated personas. The central testable claim: demonstration-grounded user-specific warm priors reduce required elicitation turns vs. both OPEN (domain-generic warm start) and BED-LLM (demo-agnostic LM prior) while achieving higher personalization win rates than non-interactive methods (PROSE, HyPerAlign). LaMP benchmarks, AMPLe/FSPO baselines, and full ablations are deferred to Phase 2.",
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
  "promptId": "8fb37705-38e8-4df4-9bc3-f241fc3162f5",
  "type": "user",
  "uuid": "745f7fe4-4de2-42be-895f-1de13fc4dbb3",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:45:07.621Z_

```json
{
  "parentUuid": "745f7fe4-4de2-42be-895f-1de13fc4dbb3",
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
  "uuid": "1d300271-ea68-41d1-baeb-0e061a4e5c73",
  "timestamp": "2026-05-10T07:45:07.621Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:45:07.621Z_

```json
{
  "parentUuid": "1d300271-ea68-41d1-baeb-0e061a4e5c73",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "737a4a6a-d030-4d4c-8e04-b66548a2d03e",
  "timestamp": "2026-05-10T07:45:07.621Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
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
  "leafUuid": "737a4a6a-d030-4d4c-8e04-b66548a2d03e",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM response-style personalization via demonstration-grounded Bayesian elicitation",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:45:25.352Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. This is Round 7 of 10 for reviewing a paper idea called FABEL (Falsification-Aligned Binary Elicitation Loop). Let me look at what was fixed in previous rounds and conduct fresh independent research to verify the current state of the idea.

From the Round 6 review, there were 4 minor issues:
1. TO-GATE description inaccuracy
2. Disconfirmation probe generation mechanism underspecified
3. Stage 2a τ selection failure mode unspecified
4. Human study statistical power vs. EMNLP Main claim tension

Looking at the current Round 7 proposal, let me check if these have been addressed:


The TO-GATE description has been corrected to properly characterize it as trajectory-level DPO with the specific performance metrics, and the disconfirmation probe generation mechanism is now being specified with details about how the system elicits falsifiable probes rather than defaulting to low-confidence confirmatory hypotheses.

For Stage 2a, I'm clarifying the τ failure mode: when the search grid doesn't yield a threshold above 0.6 on the dev split, we fall back to a uniform prior and mark it as a calibration failure, which signals that the LLM's log-likelihoods aren't actually predictive for that hypothesis class.

The human study claim is being revised to acknowledge that the study lacks statistical power, so findings are presented descriptively rather than as inferential results.

Now I'm checking the independent research to verify the key claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "737a4a6a-d030-4d4c-8e04-b66548a2d03e",
  "isSidechain": false,
  "requestId": "req_011CatWsUsXsw7SNfPotpW11",
  "type": "assistant",
  "uuid": "411fedd2-dc78-4c65-a270-75c904e20202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KNbrhrv3tECRxhjoE9CR2N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26822,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1920,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26822
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

_source line 9 · 2026-05-10T07:45:25.368Z_

I'll conduct independent verification searches on the key claims in this Round 7 proposal before issuing a verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "411fedd2-dc78-4c65-a270-75c904e20202",
  "isSidechain": false,
  "requestId": "req_011CatWsUsXsw7SNfPotpW11",
  "type": "assistant",
  "uuid": "5ab4662e-f2d9-4430-8123-bf707188c002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KNbrhrv3tECRxhjoE9CR2N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26822,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1920,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26822
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

_source line 10 · 2026-05-10T07:45:33.800Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0162n31e1g4UsHLpvtLLxsvY`</summary>

```json
{
  "description": "Search for competing work on LLM personalization via Bayesian preference elicitation",
  "subagent_type": "Explore",
  "prompt": "Search for recent papers (2025-2026) on these topics to help me independently verify novelty claims in a paper review. I need to find any work that combines: (1) user demonstration-conditioned priors with (2) EIG/Bayesian experimental design for (3) LLM personalization/preference elicitation. Also look for papers that might compete with FABEL.\n\nSearch queries to run:\n1. arxiv \"Bayesian preference elicitation\" LLM personalization 2025 2026\n2. arxiv \"active preference learning\" LLM personalization demonstration 2025\n3. arxiv \"EIG\" OR \"experimental information gain\" preference elicitation language model 2026\n4. site:openreview.net \"preference elicitation\" personalization demonstration 2026\n5. arxiv \"user preference\" \"few-shot\" \"Bayesian\" LLM interaction 2026\n6. arxiv \"FABEL\" OR \"falsification\" hypothesis elicitation personalization 2026\n7. Search for \"PersonalLLM\" benchmark availability on HuggingFace\n8. arxiv \"warm start\" Bayesian preference LLM 2025 2026\n\nFor each result, capture the title, authors, venue/year, and abstract summary. I'm looking especially for work that uses demonstrations to initialize Bayesian priors for preference elicitation, or work on EIG-based binary confirmation for LLM personalization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ab4662e-f2d9-4430-8123-bf707188c002",
  "isSidechain": false,
  "requestId": "req_011CatWsUsXsw7SNfPotpW11",
  "type": "assistant",
  "uuid": "d2ea7c8c-b390-4cfa-9a8a-32dddf721d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KNbrhrv3tECRxhjoE9CR2N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26822,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1920,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26822
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

_source line 11 · 2026-05-10T07:45:41.935Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RdcGvhH6FwnQGZFpVHE7Lo`</summary>

```json
{
  "description": "Verify key paper references and search for concurrent competing work",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a research paper proposal and need to independently verify several reference claims. Please:\n\n1. Search for and verify these specific papers exist with the claimed venues/years:\n   - \"OPEN: Bayesian Preference Elicitation with Language Models\" (arXiv 2403.05534, ACL 2024)\n   - \"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design\" (arXiv 2508.21184, ICLR 2026) \n   - \"AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization\" (arXiv 2411.00524, ACL 2025)\n   - \"PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples\" (arXiv 2505.23815, ICML 2025)\n   - \"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation\" (arXiv 2505.00038, May 2025)\n   - \"Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing\" (arXiv 2604.02485, April 2026)\n   - \"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization\" (arXiv 2506.02827, 2025)\n   - \"Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM\" (arXiv 2602.08819, Feb 2026)\n\n2. For each paper, fetch the arxiv page to verify: title, authors, year, venue (if stated), and abstract content matches the description given.\n\n3. Also search for: arxiv site:arxiv.org \"personalization\" \"preference\" \"Bayesian\" \"demonstration\" 2026 - to find any concurrent work that might compete\n\nPlease use WebFetch to actually read the arxiv abstract pages for at least 3-4 of the most critical papers (BED-LLM, OPEN, PROSE, HyPerAlign)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ea7c8c-b390-4cfa-9a8a-32dddf721d21",
  "isSidechain": false,
  "requestId": "req_011CatWsUsXsw7SNfPotpW11",
  "type": "assistant",
  "uuid": "2ff0fc9b-db49-4568-bdf3-b748327ef886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KNbrhrv3tECRxhjoE9CR2N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26822,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1920,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26822
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

_source line 12 · 2026-05-10T07:46:07.720Z_

<details><summary>↩ Tool result · `toolu_01RdcGvhH6FwnQGZFpVHE7Lo`</summary>

```text
Excellent! I've successfully verified all eight papers you listed. Here's a comprehensive summary of my findings:

## Verification Results

All eight papers have been **successfully verified** as existing with accurate titles and venues:

### 1. OPEN: Bayesian Preference Elicitation with Language Models
- **arXiv:** 2403.05534 ✓
- **Venue:** ACL 2024 (though listed on arXiv in cs.CL category)
- **Authors:** Kunal Handa, Yarin Gal, Ellie Pavlick, Noah Goodman, Jacob Andreas, Alex Tamkin, Belinda Z. Li
- **Status:** Verified - Framework combines BOED with LMs to optimize query informativity

### 2. BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design
- **arXiv:** 2508.21184 ✓
- **Venue:** ICLR 2026 ✓
- **Authors:** Deepro Choudhury, Sinead Williamson, Adam Goliński, Ning Miao, Freddie Bickford Smith, Michael Kirchhof, Yizhe Zhang, Tom Rainforth
- **Status:** Verified - Proposes sequential Bayesian experimental design for LLM information gathering

### 3. AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization
- **arXiv:** 2411.00524 ✓
- **Venue:** ACL 2025 (submitted Nov 2024, revised June 2025)
- **Authors:** Minhyeon Oh, Seungjoon Lee, Jungseul Ok
- **Status:** Verified - Active preference learning using Bayesian inference and binary search

### 4. PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples
- **arXiv:** 2505.23815 ✓
- **Venue:** ICML 2025 ✓
- **Authors:** Stéphane Aroca-Ouellette, Natalie Mackraz, Barry-John Theobald, Katherine Metcalf
- **Status:** Verified - Uses iterative refinement and verification of inferred preferences; 33% improvement over CIPHER

### 5. HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation
- **arXiv:** 2505.00038 ✓
- **Venue:** May 2025 ✓
- **Authors:** Cristina Garbacea, Chenhao Tan
- **Status:** Verified - Generates customized responses via hypothesis inference from limited examples

### 6. Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing
- **arXiv:** 2604.02485 ✓
- **Venue:** April 2026 ✓
- **Authors:** Ayush Rajesh Jhaveri, Anthony GX-Chen, Ilia Sucholutsky, Eunsol Choi
- **Status:** Verified - Demonstrates LLM confirmation bias; proposes interventions based on human psychology

### 7. TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization
- **arXiv:** 2506.02827 ✓
- **Venue:** 2025 ✓
- **Authors:** Yulin Dou, Jiangming Liu
- **Status:** Verified - Achieves 9.32% improvement on preference elicitation tasks

### 8. Bayesian Preference Learning for Test-Time Steerable Reward Models (ICRM)
- **arXiv:** 2602.08819 ✓
- **Venue:** Feb 2026 ✓
- **Authors:** Jiwoo Hong, Shao Tang, Zhipeng Wang
- **Status:** Verified - Variational In-Context Reward Modeling using Beta priors; 34% accuracy gains on SafeRLHF

## Concurrent Work in the Field

My search for related papers on arxiv.org revealed several competing/concurrent works worth noting:

1. **Cold-Start Personalization via Training-Free Priors from Structured World Models** (2602.15012, Feb 2026) - Offline structure learning + online Bayesian inference for cold-start preference elicitation

2. **Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models** (2503.17523, Jan 2026) - Teaching LLMs Bayesian belief updating

3. **HorizonBench: Long-Horizon Personalization with Evolving Preferences** (2604.17283, April 2026) - Tracking evolving user preferences over time

4. **Many Preferences, Few Policies: Towards Scalable Language Model Personalization** (2604.04144, April 2026) - PALM algorithm for portfolio of personalized LLMs

## Conclusion

All eight papers in your proposal have been **verified as legitimate, existing publications** with accurate titles, authors, years, and venues. The papers represent a coherent research narrative on Bayesian preference learning and personalization with LLMs. The concurrent works identified show this is indeed an active research area in 2026, particularly around preference elicitation, Bayesian methods, and personalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ff0fc9b-db49-4568-bdf3-b748327ef886",
  "isSidechain": false,
  "promptId": "8fb37705-38e8-4df4-9bc3-f241fc3162f5",
  "type": "user",
  "uuid": "1964a91b-bfb7-4b75-805f-61d5af18f5d2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research paper proposal and need to independently verify several reference claims. Please:\n\n1. Search for and verify these specific papers exist with the claimed venues/years:\n   - \"OPEN: Bayesian Preference Elicitation with Language Models\" (arXiv 2403.05534, ACL 2024)\n   - \"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design\" (arXiv 2508.21184, ICLR 2026) \n   - \"AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization\" (arXiv 2411.00524, ACL 2025)\n   - \"PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples\" (arXiv 2505.23815, ICML 2025)\n   - \"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation\" (arXiv 2505.00038, May 2025)\n   - \"Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing\" (arXiv 2604.02485, April 2026)\n   - \"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization\" (arXiv 2506.02827, 2025)\n   - \"Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM\" (arXiv 2602.08819, Feb 2026)\n\n2. For each paper, fetch the arxiv page to verify: title, authors, year, venue (if stated), and abstract content matches the description given.\n\n3. Also search for: arxiv site:arxiv.org \"personalization\" \"preference\" \"Bayesian\" \"demonstration\" 2026 - to find any concurrent work that might compete\n\nPlease use WebFetch to actually read the arxiv abstract pages for at least 3-4 of the most critical papers (BED-LLM, OPEN, PROSE, HyPerAlign).",
    "agentId": "ae33627191ac670f7",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I've successfully verified all eight papers you listed. Here's a comprehensive summary of my findings:\n\n## Verification Results\n\nAll eight papers have been **successfully verified** as existing with accurate titles and venues:\n\n### 1. OPEN: Bayesian Preference Elicitation with Language Models\n- **arXiv:** 2403.05534 ✓\n- **Venue:** ACL 2024 (though listed on arXiv in cs.CL category)\n- **Authors:** Kunal Handa, Yarin Gal, Ellie Pavlick, Noah Goodman, Jacob Andreas, Alex Tamkin, Belinda Z. Li\n- **Status:** Verified - Framework combines BOED with LMs to optimize query informativity\n\n### 2. BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design\n- **arXiv:** 2508.21184 ✓\n- **Venue:** ICLR 2026 ✓\n- **Authors:** Deepro Choudhury, Sinead Williamson, Adam Goliński, Ning Miao, Freddie Bickford Smith, Michael Kirchhof, Yizhe Zhang, Tom Rainforth\n- **Status:** Verified - Proposes sequential Bayesian experimental design for LLM information gathering\n\n### 3. AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization\n- **arXiv:** 2411.00524 ✓\n- **Venue:** ACL 2025 (submitted Nov 2024, revised June 2025)\n- **Authors:** Minhyeon Oh, Seungjoon Lee, Jungseul Ok\n- **Status:** Verified - Active preference learning using Bayesian inference and binary search\n\n### 4. PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples\n- **arXiv:** 2505.23815 ✓\n- **Venue:** ICML 2025 ✓\n- **Authors:** Stéphane Aroca-Ouellette, Natalie Mackraz, Barry-John Theobald, Katherine Metcalf\n- **Status:** Verified - Uses iterative refinement and verification of inferred preferences; 33% improvement over CIPHER\n\n### 5. HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation\n- **arXiv:** 2505.00038 ✓\n- **Venue:** May 2025 ✓\n- **Authors:** Cristina Garbacea, Chenhao Tan\n- **Status:** Verified - Generates customized responses via hypothesis inference from limited examples\n\n### 6. Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing\n- **arXiv:** 2604.02485 ✓\n- **Venue:** April 2026 ✓\n- **Authors:** Ayush Rajesh Jhaveri, Anthony GX-Chen, Ilia Sucholutsky, Eunsol Choi\n- **Status:** Verified - Demonstrates LLM confirmation bias; proposes interventions based on human psychology\n\n### 7. TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization\n- **arXiv:** 2506.02827 ✓\n- **Venue:** 2025 ✓\n- **Authors:** Yulin Dou, Jiangming Liu\n- **Status:** Verified - Achieves 9.32% improvement on preference elicitation tasks\n\n### 8. Bayesian Preference Learning for Test-Time Steerable Reward Models (ICRM)\n- **arXiv:** 2602.08819 ✓\n- **Venue:** Feb 2026 ✓\n- **Authors:** Jiwoo Hong, Shao Tang, Zhipeng Wang\n- **Status:** Verified - Variational In-Context Reward Modeling using Beta priors; 34% accuracy gains on SafeRLHF\n\n## Concurrent Work in the Field\n\nMy search for related papers on arxiv.org revealed several competing/concurrent works worth noting:\n\n1. **Cold-Start Personalization via Training-Free Priors from Structured World Models** (2602.15012, Feb 2026) - Offline structure learning + online Bayesian inference for cold-start preference elicitation\n\n2. **Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models** (2503.17523, Jan 2026) - Teaching LLMs Bayesian belief updating\n\n3. **HorizonBench: Long-Horizon Personalization with Evolving Preferences** (2604.17283, April 2026) - Tracking evolving user preferences over time\n\n4. **Many Preferences, Few Policies: Towards Scalable Language Model Personalization** (2604.04144, April 2026) - PALM algorithm for portfolio of personalized LLMs\n\n## Conclusion\n\nAll eight papers in your proposal have been **verified as legitimate, existing publications** with accurate titles, authors, years, and venues. The papers represent a coherent research narrative on Bayesian preference learning and personalization with LLMs. The concurrent works identified show this is indeed an active research area in 2026, particularly around preference elicitation, Bayesian methods, and personalization."
      }
    ],
    "totalDurationMs": 25781,
    "totalTokens": 23130,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4773,
      "cache_read_input_tokens": 17071,
      "output_tokens": 1279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1279,
          "cache_read_input_tokens": 17071,
          "cache_creation_input_tokens": 4773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4773,
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
  "sourceToolAssistantUUID": "2ff0fc9b-db49-4568-bdf3-b748327ef886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T07:46:30.655Z_

<details><summary>↩ Tool result · `toolu_0162n31e1g4UsHLpvtLLxsvY`</summary>

```text
## Summary: Recent Papers on Preference Elicitation, EIG-Based Learning, and LLM Personalization (2025-2026)

I've completed a comprehensive search across your specified topics. Here's what I found organized by key theme:

### Core Papers Combining Bayesian EIG + Preference Elicitation + LLMs

**Most directly relevant to your novelty verification:**

1. **BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design** (August 2025)
   - [arxiv.org/html/2508.21184](https://arxiv.org/html/2508.21184)
   - Proposes EIG-based adaptive information gathering for LLMs; iteratively selects questions/queries maximizing EIG
   - Demonstrates gains on 20-questions game and user preference inference tasks

2. **Bayesian Preference Elicitation with Language Models (OPEN)** (March 2024)
   - [arxiv.org/html/2403.05534](https://arxiv.org/html/2403.05534)
   - Uses Bayesian Optimal Experimental Design (BOED) to select informative questions
   - LM translates abstract BOED queries into natural language, maximizing EIG for preference elicitation

3. **Learning to Ask Informative Questions: Enhancing LLMs with Preference Optimization and Expected Information Gain** (October 2024)
   - [arxiv.org/html/2406.17453](https://arxiv.org/html/2406.17453)
   - Addresses how LLMs can generate questions that maximize EIG
   - Uses preference pairs (low-EIG vs high-EIG questions) with DPO

### Papers on Active/Adaptive Preference Learning with Demonstrations

4. **Comparison-based Active Preference Learning for Multi-dimensional Personalization (AMPLe)** (November 2024)
   - [arxiv.org/abs/2411.00524](https://arxiv.org/abs/2411.00524)
   - Active preference learning for multi-dimensional user preferences with fewer comparisons
   - Generates personalized LLM responses tailored to individual hidden preferences

5. **Active Preference Learning for Large Language Models** (February 2024)
   - [arxiv.org/abs/2402.08114](https://arxiv.org/abs/2402.08114)
   - Iterative data acquisition and fine-tuning loop with acquisition functions for DPO

### Demonstration-Conditioned Prior Initialization

6. **LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation** (August 2025)
   - [arxiv.org/abs/2508.03766](https://arxiv.org/abs/2508.03766)
   - Automates prior elicitation using LLMs
   - Translates unstructured contexts (descriptions, data, figures) into probability distributions
   - **Highly relevant: demonstrates using external knowledge to initialize Bayesian priors**

7. **Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models** (March 2026)
   - [arxiv.org/abs/2503.17523](https://arxiv.org/abs/2503.17523)
   - Shows LLMs can learn Bayesian reasoning through demonstrations/teaching
   - Generalizes to new tasks after demonstration-based training

### Binary/Efficient Preference Elicitation

8. **Asking Clarifying Questions for Preference Elicitation With Large Language Models** (July 2025)
   - [arxiv.org/abs/2510.12015](https://arxiv.org/abs/2510.12015)
   - Two-stage process for generating sequential clarifying questions
   - Inspired by diffusion models for preference disambiguation

9. **Accelerated Preference Elicitation with LLM-Based Proxies** (January 2025)
   - [arxiv.org/abs/2501.14625](https://arxiv.org/abs/2501.14625)
   - Achieves efficient outcomes with 5x fewer queries than classical methods
   - Combines LLM pipelines with proper-learning techniques

### Personalization Frameworks & Benchmarks

10. **PersonalLLM Benchmark** (Available on HuggingFace)
    - [huggingface.co/datasets/namkoong-lab/PersonalLLM](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)
    - Benchmark for adapting LLMs to individual user preferences
    - Uses simulated user base with diverse preferences from pre-trained reward models
    - Explores in-context learning and meta-learning baselines

11. **A Survey of Personalized Large Language Models: Progress and Future Directions** (February 2026)
    - [arxiv.org/abs/2502.11528](https://arxiv.org/abs/2502.11528)
    - Comprehensive survey covering profile modeling, memory, planning, execution
    - Reviews approaches like ONCE (interest summarization) and DPL (inter-user comparison)

12. **Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions** (February 2026)
    - [arxiv.org/abs/2602.22680](https://arxiv.org/abs/2602.22680)
    - Capability-oriented review of personalized LLM agents
    - Addresses when to infer, elicit, and commit to preferences

13. **PREMIUM: LLM Personalization with Individual-level Preference Feedback** (OpenReview)
    - [openreview.net/forum?id=N1pya6kv3g](https://openreview.net/forum?id=N1pya6kv3g)
    - Locally deployable framework for individual-level preference feedback
    - Continuous self-iteration during user-LLM interaction

### FABEL-Related Work (Hypothesis Falsification)

14. **Automated Hypothesis Validation with Agentic Sequential Falsifications (Popper)** (February 2025)
    - [arxiv.org/abs/2502.09858](https://arxiv.org/abs/2502.09858)
    - Framework for automated hypothesis validation using LLM agents
    - Sequential testing with strict Type-I error control
    - Uses e-values for statistically valid evidence aggregation

### Efficient Data Selection for Preference Learning

15. **Less is More: Improving LLM Alignment via Preference Data Selection (BeeS)** (June 2025)
    - [arxiv.org/abs/2502.14560](https://arxiv.org/abs/2502.14560)
    - Bayesian aggregation for preference selection
    - Achieves 3-8% improvements using only 10% of data

16. **Towards Understanding Valuable Preference Data for Large Language Model Alignment** (October 2025, updated March 2026)
    - [arxiv.org/abs/2510.13212](https://arxiv.org/abs/2510.13212)
    - Scoring functions for individual preference data quality
    - Demonstrates better alignment with less data

### Key Findings for Novelty Verification

**Combination that appears novel:**
- The specific combination of (1) demonstration-conditioned priors + (2) EIG-based binary confirmation + (3) LLM personalization is not explicitly found in a single paper
- **OPEN** (2024) does EIG + preference elicitation, but doesn't emphasize demonstration initialization
- **LLM-Prior** (2025) does demonstration-based prior initialization, but focuses on general Bayesian inference, not preference elicitation
- **BED-LLM** (2025) does EIG-based information gathering, but no mention of demonstration priors
- **AMPLe** (2024) does active preference learning for personalization but doesn't emphasize information-theoretic optimization

**Related but distinct approaches:**
- FABEL-like falsification work exists (Popper, 2025) but targets hypothesis validation, not preference elicitation
- PersonalLLM benchmark exists but doesn't combine EIG-based active learning with demonstration priors
- No papers explicitly combine all three: demonstration-initialized Bayesian priors + EIG optimization + preference-elicitation-for-personalization

This suggests your work has potential novelty in the specific combination, though the individual components are covered in recent literature. The gap appears to be integrating demonstration-based warm-starting with information-theoretic optimization for user preference learning.

Sources:
- [arxiv.org/html/2508.21184](https://arxiv.org/html/2508.21184)
- [arxiv.org/html/2403.05534](https://arxiv.org/html/2403.05534)
- [arxiv.org/html/2406.17453](https://arxiv.org/html/2406.17453)
- [arxiv.org/abs/2411.00524](https://arxiv.org/abs/2411.00524)
- [arxiv.org/abs/2402.08114](https://arxiv.org/abs/2402.08114)
- [arxiv.org/abs/2508.03766](https://arxiv.org/abs/2508.03766)
- [arxiv.org/abs/2503.17523](https://arxiv.org/abs/2503.17523)
- [arxiv.org/abs/2510.12015](https://arxiv.org/abs/2510.12015)
- [arxiv.org/abs/2501.14625](https://arxiv.org/abs/2501.14625)
- [huggingface.co/datasets/namkoong-lab/PersonalLLM](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)
- [arxiv.org/abs/2502.11528](https://arxiv.org/abs/2502.11528)
- [arxiv.org/abs/2602.22680](https://arxiv.org/abs/2602.22680)
- [openreview.net/forum?id=N1pya6kv3g](https://openreview.net/forum?id=N1pya6kv3g)
- [arxiv.org/abs/2502.09858](https://arxiv.org/abs/2502.09858)
- [arxiv.org/abs/2502.14560](https://arxiv.org/abs/2502.14560)
- [arxiv.org/abs/2510.13212](https://arxiv.org/abs/2510.13212)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2ea7c8c-b390-4cfa-9a8a-32dddf721d21",
  "isSidechain": false,
  "promptId": "8fb37705-38e8-4df4-9bc3-f241fc3162f5",
  "type": "user",
  "uuid": "7410c22f-d9cb-4c6d-813c-9ed0da1e77dd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) on these topics to help me independently verify novelty claims in a paper review. I need to find any work that combines: (1) user demonstration-conditioned priors with (2) EIG/Bayesian experimental design for (3) LLM personalization/preference elicitation. Also look for papers that might compete with FABEL.\n\nSearch queries to run:\n1. arxiv \"Bayesian preference elicitation\" LLM personalization 2025 2026\n2. arxiv \"active preference learning\" LLM personalization demonstration 2025\n3. arxiv \"EIG\" OR \"experimental information gain\" preference elicitation language model 2026\n4. site:openreview.net \"preference elicitation\" personalization demonstration 2026\n5. arxiv \"user preference\" \"few-shot\" \"Bayesian\" LLM interaction 2026\n6. arxiv \"FABEL\" OR \"falsification\" hypothesis elicitation personalization 2026\n7. Search for \"PersonalLLM\" benchmark availability on HuggingFace\n8. arxiv \"warm start\" Bayesian preference LLM 2025 2026\n\nFor each result, capture the title, authors, venue/year, and abstract summary. I'm looking especially for work that uses demonstrations to initialize Bayesian priors for preference elicitation, or work on EIG-based binary confirmation for LLM personalization.",
    "agentId": "aee1f3813162aaac6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary: Recent Papers on Preference Elicitation, EIG-Based Learning, and LLM Personalization (2025-2026)\n\nI've completed a comprehensive search across your specified topics. Here's what I found organized by key theme:\n\n### Core Papers Combining Bayesian EIG + Preference Elicitation + LLMs\n\n**Most directly relevant to your novelty verification:**\n\n1. **BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design** (August 2025)\n   - [arxiv.org/html/2508.21184](https://arxiv.org/html/2508.21184)\n   - Proposes EIG-based adaptive information gathering for LLMs; iteratively selects questions/queries maximizing EIG\n   - Demonstrates gains on 20-questions game and user preference inference tasks\n\n2. **Bayesian Preference Elicitation with Language Models (OPEN)** (March 2024)\n   - [arxiv.org/html/2403.05534](https://arxiv.org/html/2403.05534)\n   - Uses Bayesian Optimal Experimental Design (BOED) to select informative questions\n   - LM translates abstract BOED queries into natural language, maximizing EIG for preference elicitation\n\n3. **Learning to Ask Informative Questions: Enhancing LLMs with Preference Optimization and Expected Information Gain** (October 2024)\n   - [arxiv.org/html/2406.17453](https://arxiv.org/html/2406.17453)\n   - Addresses how LLMs can generate questions that maximize EIG\n   - Uses preference pairs (low-EIG vs high-EIG questions) with DPO\n\n### Papers on Active/Adaptive Preference Learning with Demonstrations\n\n4. **Comparison-based Active Preference Learning for Multi-dimensional Personalization (AMPLe)** (November 2024)\n   - [arxiv.org/abs/2411.00524](https://arxiv.org/abs/2411.00524)\n   - Active preference learning for multi-dimensional user preferences with fewer comparisons\n   - Generates personalized LLM responses tailored to individual hidden preferences\n\n5. **Active Preference Learning for Large Language Models** (February 2024)\n   - [arxiv.org/abs/2402.08114](https://arxiv.org/abs/2402.08114)\n   - Iterative data acquisition and fine-tuning loop with acquisition functions for DPO\n\n### Demonstration-Conditioned Prior Initialization\n\n6. **LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation** (August 2025)\n   - [arxiv.org/abs/2508.03766](https://arxiv.org/abs/2508.03766)\n   - Automates prior elicitation using LLMs\n   - Translates unstructured contexts (descriptions, data, figures) into probability distributions\n   - **Highly relevant: demonstrates using external knowledge to initialize Bayesian priors**\n\n7. **Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models** (March 2026)\n   - [arxiv.org/abs/2503.17523](https://arxiv.org/abs/2503.17523)\n   - Shows LLMs can learn Bayesian reasoning through demonstrations/teaching\n   - Generalizes to new tasks after demonstration-based training\n\n### Binary/Efficient Preference Elicitation\n\n8. **Asking Clarifying Questions for Preference Elicitation With Large Language Models** (July 2025)\n   - [arxiv.org/abs/2510.12015](https://arxiv.org/abs/2510.12015)\n   - Two-stage process for generating sequential clarifying questions\n   - Inspired by diffusion models for preference disambiguation\n\n9. **Accelerated Preference Elicitation with LLM-Based Proxies** (January 2025)\n   - [arxiv.org/abs/2501.14625](https://arxiv.org/abs/2501.14625)\n   - Achieves efficient outcomes with 5x fewer queries than classical methods\n   - Combines LLM pipelines with proper-learning techniques\n\n### Personalization Frameworks & Benchmarks\n\n10. **PersonalLLM Benchmark** (Available on HuggingFace)\n    - [huggingface.co/datasets/namkoong-lab/PersonalLLM](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)\n    - Benchmark for adapting LLMs to individual user preferences\n    - Uses simulated user base with diverse preferences from pre-trained reward models\n    - Explores in-context learning and meta-learning baselines\n\n11. **A Survey of Personalized Large Language Models: Progress and Future Directions** (February 2026)\n    - [arxiv.org/abs/2502.11528](https://arxiv.org/abs/2502.11528)\n    - Comprehensive survey covering profile modeling, memory, planning, execution\n    - Reviews approaches like ONCE (interest summarization) and DPL (inter-user comparison)\n\n12. **Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions** (February 2026)\n    - [arxiv.org/abs/2602.22680](https://arxiv.org/abs/2602.22680)\n    - Capability-oriented review of personalized LLM agents\n    - Addresses when to infer, elicit, and commit to preferences\n\n13. **PREMIUM: LLM Personalization with Individual-level Preference Feedback** (OpenReview)\n    - [openreview.net/forum?id=N1pya6kv3g](https://openreview.net/forum?id=N1pya6kv3g)\n    - Locally deployable framework for individual-level preference feedback\n    - Continuous self-iteration during user-LLM interaction\n\n### FABEL-Related Work (Hypothesis Falsification)\n\n14. **Automated Hypothesis Validation with Agentic Sequential Falsifications (Popper)** (February 2025)\n    - [arxiv.org/abs/2502.09858](https://arxiv.org/abs/2502.09858)\n    - Framework for automated hypothesis validation using LLM agents\n    - Sequential testing with strict Type-I error control\n    - Uses e-values for statistically valid evidence aggregation\n\n### Efficient Data Selection for Preference Learning\n\n15. **Less is More: Improving LLM Alignment via Preference Data Selection (BeeS)** (June 2025)\n    - [arxiv.org/abs/2502.14560](https://arxiv.org/abs/2502.14560)\n    - Bayesian aggregation for preference selection\n    - Achieves 3-8% improvements using only 10% of data\n\n16. **Towards Understanding Valuable Preference Data for Large Language Model Alignment** (October 2025, updated March 2026)\n    - [arxiv.org/abs/2510.13212](https://arxiv.org/abs/2510.13212)\n    - Scoring functions for individual preference data quality\n    - Demonstrates better alignment with less data\n\n### Key Findings for Novelty Verification\n\n**Combination that appears novel:**\n- The specific combination of (1) demonstration-conditioned priors + (2) EIG-based binary confirmation + (3) LLM personalization is not explicitly found in a single paper\n- **OPEN** (2024) does EIG + preference elicitation, but doesn't emphasize demonstration initialization\n- **LLM-Prior** (2025) does demonstration-based prior initialization, but focuses on general Bayesian inference, not preference elicitation\n- **BED-LLM** (2025) does EIG-based information gathering, but no mention of demonstration priors\n- **AMPLe** (2024) does active preference learning for personalization but doesn't emphasize information-theoretic optimization\n\n**Related but distinct approaches:**\n- FABEL-like falsification work exists (Popper, 2025) but targets hypothesis validation, not preference elicitation\n- PersonalLLM benchmark exists but doesn't combine EIG-based active learning with demonstration priors\n- No papers explicitly combine all three: demonstration-initialized Bayesian priors + EIG optimization + preference-elicitation-for-personalization\n\nThis suggests your work has potential novelty in the specific combination, though the individual components are covered in recent literature. The gap appears to be integrating demonstration-based warm-starting with information-theoretic optimization for user preference learning.\n\nSources:\n- [arxiv.org/html/2508.21184](https://arxiv.org/html/2508.21184)\n- [arxiv.org/html/2403.05534](https://arxiv.org/html/2403.05534)\n- [arxiv.org/html/2406.17453](https://arxiv.org/html/2406.17453)\n- [arxiv.org/abs/2411.00524](https://arxiv.org/abs/2411.00524)\n- [arxiv.org/abs/2402.08114](https://arxiv.org/abs/2402.08114)\n- [arxiv.org/abs/2508.03766](https://arxiv.org/abs/2508.03766)\n- [arxiv.org/abs/2503.17523](https://arxiv.org/abs/2503.17523)\n- [arxiv.org/abs/2510.12015](https://arxiv.org/abs/2510.12015)\n- [arxiv.org/abs/2501.14625](https://arxiv.org/abs/2501.14625)\n- [huggingface.co/datasets/namkoong-lab/PersonalLLM](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)\n- [arxiv.org/abs/2502.11528](https://arxiv.org/abs/2502.11528)\n- [arxiv.org/abs/2602.22680](https://arxiv.org/abs/2602.22680)\n- [openreview.net/forum?id=N1pya6kv3g](https://openreview.net/forum?id=N1pya6kv3g)\n- [arxiv.org/abs/2502.09858](https://arxiv.org/abs/2502.09858)\n- [arxiv.org/abs/2502.14560](https://arxiv.org/abs/2502.14560)\n- [arxiv.org/abs/2510.13212](https://arxiv.org/abs/2510.13212)"
      }
    ],
    "totalDurationMs": 56848,
    "totalTokens": 31939,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1795,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 25577,
      "output_tokens": 2584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1983
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1795,
          "output_tokens": 2584,
          "cache_read_input_tokens": 25577,
          "cache_creation_input_tokens": 1983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1983,
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
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "d2ea7c8c-b390-4cfa-9a8a-32dddf721d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
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
  "leafUuid": "7410c22f-d9cb-4c6d-813c-9ed0da1e77dd",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM response-style personalization via demonstration-grounded Bayesian elicitation",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Assistant

_source line 16 · 2026-05-10T07:48:08.077Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have information from both agents. Let me synthesize:

1. All key papers are verified as real and correctly attributed.
2. The concurrent work identified includes:
   - "Cold-Start Personalization via Training-Free Priors from Structured World Models" (2602.15012, Feb 2026) - This is interesting! "Offline structure learning + online Bayesian inference for cold-start preference elicitation" - this seems potentially highly relevant to FABEL's warm-start prior initialization approach.

Let me look more carefully at this potential concurrent work and whether it's been addressed.

Let me also consider what issues remain in the Round 7 proposal:


I've addressed most of the Round 6 issues: the TO-GATE description now properly specifies trajectory-level DPO across the full multi-turn dialogue, the disconfirmation probe generation includes explicit evidence-citing requirements, the Stage 2a τ failure mode has an explicit fallback, and the human study claim is hedged appropriately though still somewhat underpowered. Now I need to examine whether this concurrent work on cold-start personalization with structured world models poses a novelty concern for FABEL's approach. quite relevant - "Offline structure learning + online Bayesian inference for cold-start preference elicitation." This seems like it could overlap with FABEL's warm-start initialization. I should fetch this paper to understand it better.

**Potential Issue 2: "Many Preferences, Few Policies: Towards Scalable Language Model Personalization" (arXiv 2604.04144, April 2026)**
"PALM algorithm for portfolio of personalized LLMs" - active research in LLM personalization space.

**Overall assessment:**
Looking at Round 7, the main fix issues from Round 6 have been addressed. The core novelty - warm-start Bayesian prior from demonstrations + EIG binary confirmation + disconfirmation probes - appears still valid. The proposal is quite sophisticated and comprehensive.

Let me think about potential new issues:

1. **The "Cold-Start Personalization via Training-Free Priors from Structured World Models" paper** - If it uses demonstration-based priors for cold-start personalization, there's potential overlap with FABEL's warm-start approach that I need to examine more closely.

2. **PROSE baseline concerns**: PROSE requires user writing samples to run its generate→compare→update pipeline, but PersonalLLM may not have data in the right format for this, which could affect the baseline comparison.

3. **BED-LLM reimplementation risk**: Still a concern, though the proposal mitigates it with a time-boxed fallback approach.

4. **PersonalLLM dataset size for calibration**: The Stage 2a plan mentions using 50 dev users for τ calibration, but I'm noticing the full PersonalLLM dataset has thousands of users, so I need to verify this split is appropriate.

5. **PREMIUM and other concurrent work**: Found several potentially relevant papers on LLM personalization that weren't clearly addressed as concurrent work.

6. **Accelerated Preference Elicitation methods**: There's a paper achieving 5x query efficiency using LLM-based proxies that could be a competing approach.

Now I'm reviewing the current proposal state to see what else might need attention.

I'm noticing a couple of potential issues. First, there's a recent paper from February 2026 on cold-start personalization using Bayesian inference with structured world model priors—if it also uses demonstration-based warm priors, that could challenge FABEL's novelty. Second, there's an inconsistency in how Stage 2a describes the Kendall τ operationalization for the simulated PersonalLLM dev users, particularly around how empirical accuracy is being measured. I'm noticing some inconsistencies in how I've described the methodology—the description section mentions Kendall τ for comparing against the reward model's preference ordering, but the approach section only discusses Spearman ρ. Let me check if these are actually measuring different things or if one is extraneous. The core claim about top-quartile responses satisfying hypotheses seems consistent across sections though.

Looking at the related work, this accelerated preference elicitation paper achieves significant query efficiency through LLM-based proxies, which is conceptually similar to FABEL's warm-start approach but uses a different mechanism entirely. The human study framing is still a bit optimistic given the small sample size, though I've already hedged appropriately by noting it's underpowered for statistical inference. I should double-check the BED-LLM description to make sure I'm characterizing it accurately relative to what FABEL is doing. I should dig deeper into arXiv 2602.15012 since it seems directly relevant to FABEL's warm-start approach—using offline structure learning combined with online Bayesian inference for cold-start preference elicitation sounds like it could overlap significantly with what we're proposing. Looking at the overall proposal state now, the novelty score hinges on whether the combination of warm-start priors from demonstrations, EIG-based binary confirmation and disconfirmation probes, is genuinely distinct from existing work. The application to LLM response-style personalization represents a meaningful domain shift, and while each component builds on established techniques, their specific combination—particularly the mandatory disconfirmation probes—hasn't been addressed together before. I'd rate novelty at 3.5/5 given the solid but somewhat incremental nature of the work. The feasibility looks strong with a well-scoped MVP and compute requirements well under budget, though the 16-day timeline with BED-LLM reimplementation as a risk factor keeps it at 4/5. The proposal is exceptionally clear with well-justified choices, but the impact is moderate since improving preference elicitation efficiency through demonstration-based initialization, while useful, is fairly incremental.

Averaging these scores gives 3.75, which falls short of the 4.0 threshold. For Round 7, I'm leaning toward a revise verdict, especially given the unverified arXiv paper 2602.15012 on cold-start personalization with training-free priors that isn't cited—this could be a direct competitor that needs addressing.

There are a few remaining concerns worth flagging: the arXiv 2501.14625 paper claiming 5x fewer queries might overlap with FABEL's efficiency gains, PREMIUM's venue and timeline are unclear, the human study framing still reads as slightly overstated despite hedging, and there's an inconsistency in how Stage 2a is operationalized between the approach and empirical sections.

The most pressing issue is arXiv 2602.15012 on cold-start personalization with structured world model priors—if it uses demonstrations to initialize Bayesian priors for preference learning, that's a direct overlap with FABEL's Stage 2 that needs to be addressed through citation or differentiation. I should investigate this paper more carefully to determine whether it's a genuine conflict or just superficially similar.

Beyond that, the core technical claims hold up: using LLM log-likelihoods to condition the prior is sound, the EIG calculation correctly accounts for the factored posterior, and the disconfirmation probe design appears well-motivated.

The main gaps I'm flagging are whether arXiv 2602.15012 is actually a competing approach that deserves citation, and whether the human study framing overstates the strength of the evidence given the hedging language used. I'm recalibrating my scoring across the key dimensions. Novelty sits around 3.5 out of 5—the individual pieces exist elsewhere, but this specific combination of demo-conditioned priors, EIG-based confirmation, disconfirmation probes, and response personalization hasn't appeared together before, though I need to verify the arXiv 2602.15012 overlap. Feasibility looks solid at 4.0 given the clear MVP scope, reasonable compute budget, and tight but achievable 16-day timeline, with acknowledged fallbacks for the BED-LLM reimplementation and confirmed access to PersonalLLM. The proposal is exceptionally detailed and well-structured, landing at 4.0 for clarity.

Impact comes in at 3.5—appropriate for EMNLP Findings with practical personalization gains and a real solution to a failure mode, but methodologically incremental. That averages to 3.75, which falls short of the 4.0 threshold for acceptance, so I'm leaning toward a revise decision. The critical blocker is verifying whether arXiv 2602.15012 represents a genuine competitor that would undermine the novelty claim.

I've confirmed that BED-LLM's use of multiple-choice questions is correctly characterized in the proposal—the single-token response constraint does enable meaningful uncertainty estimates for EIG calculations. The Stage 2a accuracy metric is also well-specified: measuring the fraction of the user's top-quartile responses that satisfy each hypothesis, validated through a classifier. There's a potential concern emerging here that I need to think through.

The circularity issue is worth flagging: FABEL relies on Qwen2.5-7B-Instruct for both hypothesis generation and hypothesis satisfaction assessment, which could bias the warm-start calibration toward the model's own interpretation of what counts as satisfying a hypothesis. Additionally, computing Spearman correlation between the model's own log-likelihood scores and empirical accuracies introduces a confounding factor—the same model is being used to score responses and assess their quality, which could artificially inflate the correlation.

Now I'm compiling the key issues to report in my review. The main concerns are a potentially unverified competitor paper from February 2026 that overlaps with FABEL's Stage 2 approach, and the circular self-evaluation problem in the Stage 2a calibration analysis that could mask whether the warm start actually generalizes to real users. The Stage 2a calibration uses Qwen2.5-7B-Instruct both to (a) compute LLM log-likelihood scores and (b) classify whether responses satisfy hypotheses. This creates a circularity: the Spearman ρ might be inflated because the same model is self-consistent, not because the warm-start prior actually correlates with empirical user preferences. The paper should acknowledge this limitation or use a different model for the classification step.

On the human study framing, I initially thought the n≈20 Prolific study couldn't meaningfully strengthen the main case given its underpowered nature, but the revision to "provides a qualitative real-user signal and preliminary external validity evidence" is more defensible—it's now framed as strengthening relative to purely simulated evaluation rather than making an absolute claim. I'll treat this as borderline acceptable and keep it as a minor issue.

So I'm left deciding between pass and revise. The substantive concerns are the potentially uncited competitor paper and the circular self-evaluation in Stage 2a, with the latter being minor.

Since the arXiv paper represents a moderate novelty risk that could affect the core contribution, I'm issuing revise. Looking at the scores across novelty, feasibility, clarity, and impact, the average comes to 3.75—just below the 4.0 threshold anyway.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7410c22f-d9cb-4c6d-813c-9ed0da1e77dd",
  "isSidechain": false,
  "requestId": "req_011CatWyb8VDdXL4dQHeGTC6",
  "type": "assistant",
  "uuid": "24b9faac-07ed-4aa3-9624-a5525b826de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011y3RnsgguddkMwcg5yw2Mc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1305,
      "cache_creation_input_tokens": 4531,
      "cache_read_input_tokens": 38453,
      "output_tokens": 5807,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1305,
          "output_tokens": 5807,
          "cache_read_input_tokens": 38453,
          "cache_creation_input_tokens": 4531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4531
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

_source line 17 · 2026-05-10T07:48:11.280Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0196sMrmLVs7PUj7pLH3hhc9`</summary>

```json
{
  "description": "Fetch arXiv 2602.15012 and check for potential competition with FABEL's warm-start prior",
  "subagent_type": "Explore",
  "prompt": "Please fetch the abstract and key sections of arXiv paper 2602.15012 (\"Cold-Start Personalization via Training-Free Priors from Structured World Models\", Feb 2026) from https://arxiv.org/abs/2602.15012. I need to know:\n1. What exactly is the paper's approach - does it use user writing demonstrations to initialize Bayesian priors for preference elicitation?\n2. What domain does it target - recommendation? LLM response-style personalization?\n3. Does it use EIG or information-theoretic selection for queries?\n4. How does it differ from using LLM log-likelihoods over demonstrations to seed a Bayesian prior?\n\nAlso fetch the abstract of arXiv 2501.14625 (\"Accelerated Preference Elicitation with LLM-Based Proxies\") from https://arxiv.org/abs/2501.14625 to understand if it's competitive with warm-start Bayesian preference elicitation.\n\nUse WebFetch to read these pages directly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24b9faac-07ed-4aa3-9624-a5525b826de1",
  "isSidechain": false,
  "requestId": "req_011CatWyb8VDdXL4dQHeGTC6",
  "type": "assistant",
  "uuid": "801cb603-19da-424d-af25-5d753a1dd670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011y3RnsgguddkMwcg5yw2Mc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1305,
      "cache_creation_input_tokens": 4531,
      "cache_read_input_tokens": 38453,
      "output_tokens": 5807,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1305,
          "output_tokens": 5807,
          "cache_read_input_tokens": 38453,
          "cache_creation_input_tokens": 4531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4531
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
  "leafUuid": "801cb603-19da-424d-af25-5d753a1dd670",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM response-style personalization via demonstration-grounded Bayesian elicitation",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Tool result

_source line 20 · 2026-05-10T07:48:25.902Z_

<details><summary>↩ Tool result · `toolu_0196sMrmLVs7PUj7pLH3hhc9`</summary>

```text
Based on the fetched abstracts, here are the answers to your questions:

## Paper 2602.15012 ("Cold-Start Personalization via Training-Free Priors from Structured World Models")

**1. Approach - User writing demonstrations & Bayesian priors:**
The paper does **NOT** use user writing demonstrations to initialize Bayesian priors. Instead, it takes a different approach: it learns a **structured world model of preference correlations offline from complete profiles**, then performs **training-free Bayesian inference online** to select informative questions. There's no mention of using writing examples or demonstrations as initialization.

**2. Domain:**
The paper targets **multiple reasoning domains**: medical, mathematical, social, and commonsense reasoning—not recommendation systems or LLM response-style personalization specifically. It focuses on preference elicitation across diverse reasoning tasks.

**3. EIG or information-theoretic selection:**
While not explicitly labeled as Expected Information Gain (EIG), the approach performs "training-free Bayesian inference online to select informative questions," which implies information-theoretic principles guide query selection.

**4. Difference from LLM log-likelihood approach:**
The paper makes **no mention** of using LLM log-likelihoods over demonstrations to seed a Bayesian prior. The key distinction is that **Pep** exploits the factored structure of preference data with parameter efficiency (~10K parameters), whereas an LLM log-likelihood approach would rely on large language models (8B+ parameters). The paper emphasizes structure learning from complete profiles rather than LLM-based likelihood scoring.

**Performance**: Achieves 80.8% alignment with user preferences vs. 68.5% for RL baselines, requiring 3-5x fewer interactions.

---

## Paper 2501.14625 ("Accelerated Preference Elicitation with LLM-Based Proxies")

**Relation to warm-start Bayesian preference elicitation:**
This paper does **not explicitly discuss Bayesian preference elicitation**. Instead, it focuses on **combinatorial auctions** and uses LLM-based proxies with DNF-proper-learning techniques to accelerate preference elicitation through natural language communication. While it achieves 5x fewer queries than classical learning-based mechanisms, it's operating in a different problem space (auction bidding preferences) and methodology (LLM+DNF-learning) rather than Bayesian inference—so it may be somewhat orthogonal rather than directly competitive with warm-start Bayesian approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "801cb603-19da-424d-af25-5d753a1dd670",
  "isSidechain": false,
  "promptId": "8fb37705-38e8-4df4-9bc3-f241fc3162f5",
  "type": "user",
  "uuid": "5eafd8b3-66ab-49e7-844e-44722b90d8df",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please fetch the abstract and key sections of arXiv paper 2602.15012 (\"Cold-Start Personalization via Training-Free Priors from Structured World Models\", Feb 2026) from https://arxiv.org/abs/2602.15012. I need to know:\n1. What exactly is the paper's approach - does it use user writing demonstrations to initialize Bayesian priors for preference elicitation?\n2. What domain does it target - recommendation? LLM response-style personalization?\n3. Does it use EIG or information-theoretic selection for queries?\n4. How does it differ from using LLM log-likelihoods over demonstrations to seed a Bayesian prior?\n\nAlso fetch the abstract of arXiv 2501.14625 (\"Accelerated Preference Elicitation with LLM-Based Proxies\") from https://arxiv.org/abs/2501.14625 to understand if it's competitive with warm-start Bayesian preference elicitation.\n\nUse WebFetch to read these pages directly.",
    "agentId": "a6a3a6c2f4601c0a4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on the fetched abstracts, here are the answers to your questions:\n\n## Paper 2602.15012 (\"Cold-Start Personalization via Training-Free Priors from Structured World Models\")\n\n**1. Approach - User writing demonstrations & Bayesian priors:**\nThe paper does **NOT** use user writing demonstrations to initialize Bayesian priors. Instead, it takes a different approach: it learns a **structured world model of preference correlations offline from complete profiles**, then performs **training-free Bayesian inference online** to select informative questions. There's no mention of using writing examples or demonstrations as initialization.\n\n**2. Domain:**\nThe paper targets **multiple reasoning domains**: medical, mathematical, social, and commonsense reasoning—not recommendation systems or LLM response-style personalization specifically. It focuses on preference elicitation across diverse reasoning tasks.\n\n**3. EIG or information-theoretic selection:**\nWhile not explicitly labeled as Expected Information Gain (EIG), the approach performs \"training-free Bayesian inference online to select informative questions,\" which implies information-theoretic principles guide query selection.\n\n**4. Difference from LLM log-likelihood approach:**\nThe paper makes **no mention** of using LLM log-likelihoods over demonstrations to seed a Bayesian prior. The key distinction is that **Pep** exploits the factored structure of preference data with parameter efficiency (~10K parameters), whereas an LLM log-likelihood approach would rely on large language models (8B+ parameters). The paper emphasizes structure learning from complete profiles rather than LLM-based likelihood scoring.\n\n**Performance**: Achieves 80.8% alignment with user preferences vs. 68.5% for RL baselines, requiring 3-5x fewer interactions.\n\n---\n\n## Paper 2501.14625 (\"Accelerated Preference Elicitation with LLM-Based Proxies\")\n\n**Relation to warm-start Bayesian preference elicitation:**\nThis paper does **not explicitly discuss Bayesian preference elicitation**. Instead, it focuses on **combinatorial auctions** and uses LLM-based proxies with DNF-proper-learning techniques to accelerate preference elicitation through natural language communication. While it achieves 5x fewer queries than classical learning-based mechanisms, it's operating in a different problem space (auction bidding preferences) and methodology (LLM+DNF-learning) rather than Bayesian inference—so it may be somewhat orthogonal rather than directly competitive with warm-start Bayesian approaches."
      }
    ],
    "totalDurationMs": 14617,
    "totalTokens": 19109,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 291,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 16821,
      "output_tokens": 573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1424
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 291,
          "output_tokens": 573,
          "cache_read_input_tokens": 16821,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1424,
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
  "sourceToolAssistantUUID": "801cb603-19da-424d-af25-5d753a1dd670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T07:48:58.254Z_

<details><summary>Logged reasoning block</summary>

```text
OK, so arXiv 2602.15012 is about cold-start personalization for reasoning tasks (medical, mathematical, social), not LLM response-style personalization. And it doesn't use user writing demonstrations. So it's not a direct competitor to FABEL.

Now let me make my final assessment.

The remaining issues in Round 7 are:
1. arXiv 2602.15012 - NOT a direct competitor; different domain and approach. This is no longer an issue.
2. Stage 2a circular self-evaluation - MINOR technical concern
3. Human study framing - MINOR, mostly fixed


4. The main lingering concerns are the circular evaluation in Stage 2a where the same model computes log-likelihoods and classifies hypothesis satisfaction, which could artificially boost the correlation, plus the human study still oversells its contribution despite being underpowered.

5. BED-LLM lacks public code, though the proposal mitigates this with BED-LLM-approx as a fallback.

Looking back at what Round 6 flagged, the TO-GATE description is now fixed with specifics about trajectory-level DPO and the 9.32% improvement, and the disconfirmation probe generation now includes the explicit prompt for generating stylistic hypotheses.

The τ failure mode is handled—defaulting to τ→∞ when no grid value achieves ρ > 0.6 and flagging it as a calibration failure. The human study claim has been toned down from "substantially strengthens" to "which strengthens the EMNLP Main case relative to a purely simulated evaluation," though it still leans slightly optimistic.

Two minor concerns remain: Stage 2a uses the same model (Qwen2.5-7B) for both generating and validating the probes, creating a potential circularity in the Spearman ρ metric.  A reviewer could argue the correlation reflects model consistency rather than genuine predictive validity. The human study claim also oversells—with n≈20 and underpowered results, it's anecdotal evidence at best, not a meaningful strengthening of the main case.

Given these issues and my 3.75 score, I should recommend revision. On novelty, the combination of demonstration-conditioned warm priors, binary EIG confirmation, disconfirmation probes, and LLM personalization is genuinely novel but incremental—each component adapts existing work rather than introducing fundamentally new ideas. I'd rate that around 3.5-4.0. After seven rounds of revision addressing major problems, what remains are increasingly minor issues, so the paper is in reasonable shape overall. The warm prior approach builds naturally on existing BOED work, and together with the disconfirmation probes, it fills a real gap in the literature. For EMNLP Findings, a novelty score of 3.5 feels appropriate—there's genuine combination value and the disconfirmation mechanism is truly novel, even if the individual pieces are adaptations. Looking at the full picture: novelty at 3.5, feasibility at 4.0 given the well-scoped MVP and fallbacks, clarity at 4.0 with the algorithm tightly specified, and impact at 3.5 for practical personalization work. That puts the average at 3.75, which falls short of the 4.0 threshold, so this warrants a revision request. The main remaining issue is the circular self-evaluation concern in Stage 2a.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eafd8b3-66ab-49e7-844e-44722b90d8df",
  "isSidechain": false,
  "requestId": "req_011CatX85ndwXygVNEfh7nck",
  "type": "assistant",
  "uuid": "9fc0d059-29bd-42b5-bd8d-84946d8765b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015w3DDCfcapnnFfU8VUN3D8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7685,
      "cache_read_input_tokens": 42984,
      "output_tokens": 3783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3783,
          "cache_read_input_tokens": 42984,
          "cache_creation_input_tokens": 7685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7685
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

_source line 22 · 2026-05-10T07:49:30.226Z_

Now I have enough information to synthesize a final verdict. Let me assess all issues systematically.

**Round 6 fixes - verification:**
- ✅ TO-GATE: correctly described as "trajectory-level DPO across the full multi-turn clarification dialogue"
- ✅ Disconfirmation probe prompt: now includes explicit evidence-citing generation prompt
- ✅ τ failure fallback: τ→∞ default with calibration failure flag added
- ✅ Human study framing: "underpowered for statistical inference and results are reported descriptively" added — though still says "which strengthens the EMNLP Main case relative to a purely simulated evaluation" (residual mild overstatement)

**arXiv 2602.15012 verification:** Does NOT compete with FABEL — it targets reasoning tasks (medical/math/social), uses structured world model priors learned from complete profiles offline, not user writing demonstrations. Different domain and mechanism. Not a gap.

**New technical vulnerability identified — Stage 2a circular self-evaluation:**

The proposal uses Qwen2.5-7B-Instruct for (a) computing LLM log-likelihood scores over demonstrations and (b) classifying whether responses satisfy hypotheses. The Spearman ρ in Stage 2a is computed between these two quantities — both derived from the same model. This creates an internal consistency artifact: the model will tend to assign higher log-likelihoods to demonstrations that match hypotheses it would also classify as satisfied, inflating ρ in ways that may not reflect genuine predictive validity over real user preferences. This is a real technical concern that a Bayesian reviewer would raise.

**Scoring assessment:**

| Dimension | Score | Rationale |
|---|---|---|
| Novelty | 3.5 | Combination is genuine; demo-conditioned warm prior + disconfirmation probes in EIG pool is not found in any single prior paper. But each component is adapted from existing work, making this solidly incremental rather than transformative. |
| Feasibility | 4.0 | MVP scope well-defined, 75h H100-equivalent within budget, BED-LLM fallback (approx variant) in place, PersonalLLM confirmed on HuggingFace. |
| Clarity | 4.0 | Algorithm stages well-specified with explicit prompts, operationalized calibration procedure, disconfirmation diagnostic metrics. |
| Impact | 3.5 | Practical contribution to LLM personalization efficiency; disconfirmation mechanism addresses real failure mode; appropriate scope for EMNLP Findings. |

**Average: 3.75 — below 4.0 pass threshold.**

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "The combination of demo-conditioned warm prior + EIG binary confirmation + disconfirmation probes in the EIG pool is genuinely absent from all cited prior work; independent verification confirms no single paper (including arXiv 2602.15012, which targets reasoning tasks with structured world model priors) covers this combination. However, each individual component is a well-understood adaptation — the novelty is combinatorial and incremental rather than methodologically transformative, limiting the score."
    },
    "feasibility": {
      "score": 4.0,
      "rationale": "MVP scope is well-defined: PersonalLLM (confirmed public on HuggingFace), 4 baselines, 1 backbone (Qwen2.5-7B-Instruct), 1 ablation, ~75h H100-equivalent (well within 200h). BED-LLM reimplementation risk is acknowledged and time-boxed with a BED-LLM-approx fallback. The 16-day timeline is tight but plausible."
    },
    "clarity": {
      "score": 4.0,
      "rationale": "All four algorithmic stages are precisely specified with explicit prompts, operationalized calibration criteria, diagnostic metrics (disconfirmation selection rate, falsification rate, Spearman ρ), and fallback conditions. This is among the most precisely specified proposals across the review history."
    },
    "impact": {
      "score": 3.5,
      "rationale": "Addresses a practical and well-motivated problem; the disconfirmation probe mechanism targets a real failure mode (echo-chamber convergence) identified by independent empirical work (arXiv 2604.02485). Impact is appropriate for EMNLP Findings but the method is not sufficiently novel or general to be transformative."
    }
  },
  "issues": [
    "MODERATE — Stage 2a circular self-evaluation: The Spearman ρ calibration analysis uses Qwen2.5-7B-Instruct both to (a) compute LLM log-likelihood scores score_i over demonstrations and (b) classify whether responses satisfy hypothesis h_i (for computing empirical accuracy). Since both quantities are derived from the same model, the correlation may reflect internal model consistency rather than genuine predictive validity over user preferences. Specifically, the model will tend to assign higher log-likelihoods to demonstration text that matches hypotheses it would also classify as satisfied—this is circular and could inflate ρ relative to its true value as a predictor of real user agreement. The paper should either: (a) acknowledge this as a stated limitation ('ρ is a model-consistency measure; real-user calibration is validated post-hoc via the Prolific study'), or (b) use a different model for the hypothesis satisfaction classification step (e.g., Llama 3.1-8B or a specialist NLI model) to break the circularity.",
    "MINOR — Human study framing residual overstatement: Despite correctly acknowledging the study is 'underpowered for statistical inference and results are reported descriptively,' the sentence continues 'which strengthens the EMNLP Main case relative to a purely simulated evaluation.' An underpowered descriptive study that cannot support statistical inference does not meaningfully strengthen the EMNLP Main case in the eyes of reviewing committees—it provides anecdotal, externally valid evidence but not a primary result. Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas but cannot substitute for a powered human study in Main review criteria.'"
  ],
  "feedback": "Round 7 has cleanly resolved all four Round 6 issues: TO-GATE is correctly described as trajectory-level DPO, the disconfirmation probe prompt is explicitly specified with evidence-citing requirement, the τ→∞ fallback is added, and the human study is labeled underpowered. Independent verification confirms that arXiv 2602.15012 (the only unverified potential competitor) targets reasoning tasks with structured world model priors and does not overlap with FABEL's domain or mechanism. The core combination is genuinely novel and technically sound. Two targeted fixes are needed:\n\n**Fix 1 (Moderate, 2–3 sentences in Stage 2a): Break or acknowledge the circular self-evaluation.** The Spearman ρ calibration uses Qwen2.5-7B-Instruct for both log-likelihood scoring and hypothesis satisfaction classification — this creates an internal consistency artifact that may inflate ρ. Add: 'We note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences. To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis classifier, providing a cross-model calibration check.' Alternatively, acknowledge this limitation explicitly and defer cross-model validation to Phase 2.\n\n**Fix 2 (Minor, 1 clause): Remove the residual EMNLP Main overstatement.** Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas, reported descriptively.' This aligns with the already-correct statement that the study is underpowered.\n\nAfter these two fixes, the proposal has no remaining critical issues. The combination of demo-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel and appropriately scoped for EMNLP 2026 Findings. The MVP compute estimate (75h H100-equivalent) is confirmed within budget, and the PersonalLLM benchmark is publicly available.",
  "reason": "Average score 3.75 (below 4.0 pass threshold) due to incremental-combination novelty ceiling; one new moderate technical issue (Stage 2a circular self-evaluation) and one minor residual framing issue require targeted revision before this reaches pass quality."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc0d059-29bd-42b5-bd8d-84946d8765b3",
  "isSidechain": false,
  "requestId": "req_011CatX85ndwXygVNEfh7nck",
  "type": "assistant",
  "uuid": "6b40e0fe-45eb-428d-8b5c-3bfdbbfa5f21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015w3DDCfcapnnFfU8VUN3D8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7685,
      "cache_read_input_tokens": 42984,
      "output_tokens": 3783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3783,
          "cache_read_input_tokens": 42984,
          "cache_creation_input_tokens": 7685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7685
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
  "leafUuid": "6b40e0fe-45eb-428d-8b5c-3bfdbbfa5f21",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM response-style personalization via demonstration-grounded Bayesian elicitation",
  "sessionId": "5395c75c-e1d8-4025-9db6-f1877f6d9018"
}
```

---
