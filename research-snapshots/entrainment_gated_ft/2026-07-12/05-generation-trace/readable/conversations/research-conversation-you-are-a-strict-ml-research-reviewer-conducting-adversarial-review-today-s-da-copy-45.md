# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/0aa39802-5b33-414f-b371-b5311ac03ff3.jsonl`
- **Structured JSON:** [`cc0e674a83c426ee88ab.json`](../../sessions/cc/cc0e674a83c426ee88ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:55:36.494Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:55:36.494Z",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Human-Centered NLP and Human-AI Interaction. Aligns with EMNLP 2026 special theme on agentic workflows interfacing with human experiences.\n\nDirection: Methods that improve how humans and NLP systems collaborate. In-scope: interactive learning from human feedback (beyond vanilla RLHF), human-in-the-loop annotation methods, calibrated uncertainty communication to users, adaptive explanation generation, collaborative writing/editing systems, preference elicitation, controllable generation with user intent.\n\nContribution type: METHOD ONLY. Must propose a concrete algorithm or system mechanism — not a user study alone. Method validated via user study or simulation is ideal.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. HCI-style work is often light on compute, heavier on design and evaluation.\n2. Time: ≤16 days. Use existing open models + lightweight adaptation. If user study needed, design a small-scale simulated or crowdsourced protocol.\n3. Eval: task-specific metrics + human evaluation (inter-annotator agreement, preference rates, task completion time). Simulated user evaluation acceptable for ARR submission.\n\nLook for: adaptive interaction patterns, uncertainty-aware response generation, methods for user preference learning with minimal feedback, controllable generation beyond simple instruction following.\n\nTag: direction=human_ai_interaction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Demonstration-Grounded Warm-Start Hypothesis Elicitation for LLM Personalization via Binary Confirmation\",\n  \"core_problem\": \"Personalizing LLMs to individual users requires efficient preference elicitation from few-shot demonstrations. Current methods exhibit three distinct failure modes: (1) Demonstration-grounded hypothesis methods (HyPerAlign) infer rich preference attributes from user examples but skip validation, risking hallucination and echo-chamber failure; (2) The BOED-for-preference-elicitation line—established by OPEN (arXiv 2403.05534, ACL 2024) and extended by BED-LLM (arXiv 2508.21184, ICLR 2026)—applies principled EIG-based adaptive questioning but initializes without user-specific demonstration-conditioned priors: OPEN uses LM-ranked feature importances as a domain-generic prior (not conditioned on any specific user's outputs); BED-LLM starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations—which is also not informed by available user examples; both waste elicitation turns on hypotheses that available user demonstrations already resolve; (3) Iterative preference inference from writing samples (PROSE, ICML 2025) refines free-form preference descriptions with component-level verification but involves no user interaction and no formal Bayesian posterior—it cannot adaptively resolve ambiguous hypotheses that demonstrations alone are insufficient to distinguish. Additionally, arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs exhibit systematic confirmation bias in hypothesis testing (42% baseline success rate), meaning LLM-generated hypothesis sets may be preferentially confirmable rather than genuinely falsifiable, causing Bayesian posteriors to converge spuriously on echo-chamber preference profiles. No existing method combines user-demonstration-conditioned warm-start Bayesian priors, EIG-based binary confirmation, and explicit disconfirmation-probe auditing in the LLM response-style personalization domain.\",\n  \"opportunity\": \"The BOED-for-preference-elicitation lineage was established by OPEN (arXiv 2403.05534, ACL 2024), which combined EIG-based query selection with LM feature extraction over pairwise item comparisons in content recommendation—but initializes from LM-ranked feature importances (a domain-generic warm start reflecting general knowledge about what features matter for news article preferences, not this user's actual examples). BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets with a Rao-Blackwellized EIG estimator and an LM-generic prior initialization p_f(θ;∅), evaluating on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions, demonstrating that EIG-based sequential Bayesian elicitation substantially outperforms prompt-only baselines. Neither OPEN nor BED-LLM exploits K specific examples of a target user's actual outputs: their initializations duplicate information that demonstrations already encode, wasting early elicitation turns. AMPLe (arXiv 2411.00524, ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation, but also cold-starts from pairwise item comparisons rather than user demonstrations and lacks disconfirmation probes. HyPerAlign (arXiv 2505.00038, May 2025) showed demonstration-grounded hypotheses yield >90% win rates but explicitly omits user validation. PROSE (arXiv 2505.23815, ICML 2025) achieves 33% improvement over CIPHER on writing-style tasks via iterative preference refinement from demonstrations, but operates entirely without user interaction—it cannot distinguish two hypotheses with similar demonstration-level support, and provides no mechanism to surface or mitigate confirmation bias. The unaddressed gap is the warm-start interactive regime: when K demonstrations are available, initializing the Bayesian prior from user-specific demonstration-conditioned LLM likelihoods—calibrated via temperature scaling to avoid overconfident prior collapse—should dramatically reduce required elicitation turns compared to both OPEN and BED-LLM (testable claim), while the interactive EIG confirmation phase resolves the residual ambiguity that passive methods like PROSE cannot address (complementary claim). A second gap concerns confirmation bias: an elicitation system that does not deliberately seed disconfirmation probes in the hypothesis pool risks producing preference profiles that reflect what an LLM expects a user to prefer rather than what the user actually prefers—an echo-chamber failure mode that HyPerAlign acknowledges but does not address, and that PROSE's component-verification step partially mitigates without fully resolving.\",\n  \"landscape\": \"The preference elicitation and personalization landscape includes eight relevant clusters. (1) Demonstration-grounded, no validation: HyPerAlign (arXiv 2505.00038, ICLR 2025 workshop) generates falsifiable-in-principle preference hypotheses from demonstrations and injects them as system prompts without user confirmation. (2) Iterative preference inference from writing samples, no interaction: PROSE (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) iteratively refines free-form preference descriptions from user writing samples via a generate→compare→update loop, then verifies preference components against held-out demonstrations with component-level scoring; achieves 33% improvement over CIPHER baseline on summarization and email writing tasks across Qwen2.5-7B/72B and GPT-4o variants; no user interaction beyond initial writing samples, no Bayesian posterior over hypotheses, no disconfirmation mechanism—the key differentiator from FABEL is that PROSE cannot adaptively resolve ambiguity beyond what demonstrations already encode and has no principled update when demonstrations are insufficient to distinguish competing hypotheses; must be included as a baseline (directly competitive with FABEL Stage 1) and explicitly differentiated. (3) The BOED-for-preference-elicitation lineage: OPEN (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) established this line by combining EIG-based query selection with LM feature extraction for content recommendation—selects pairwise queries over binary feature vectors (|F|=10, e.g., 'discusses science') using a particle-filter Bayesian update with Bradley-Terry preference model; prior initialization is via LM-ranked feature importances (domain-generic: w_i = 1.2 − 0.12i for rank i), NOT conditioned on any specific user's demonstrations; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism. BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets: samples N=15 hypotheses per turn, selects questions via Rao-Blackwellized EIG estimator (~45–50 LLM calls/step), rejection-sampling Bayesian posterior update; starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations (and notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions (a technical requirement: having a small space of single-token responses ensures p_LLM provides meaningful uncertainty over outcomes for EIG estimation); evaluates on latent preference vector inference via movie-preference multiple-choice queries and the 20-Questions game; no public code. Active Task Disambiguation (arXiv 2502.04485, ICLR 2025) similarly applies Bayesian experimental design for clarifying question selection on under-specified tasks. FABEL extends beyond all three works: (i) user-specific demonstration-conditioned warm start (K=5–10 demos from THIS user, vs. OPEN's domain-generic LM-ranked feature importances and BED-LLM's demo-agnostic LM-generic prior p_f(θ;∅)), (ii) temperature-scaled prior calibration to prevent overconfident prior collapse, (iii) binary yes/no natural-language hypothesis confirmation over free-form response-style attributes (vs. OPEN's pairwise item comparisons and BED-LLM's multiple-choice format—FABEL's binary format reduces cognitive load while remaining viable because hypothesis confirmation questions are naturally binary in ways that preference inference over open hypothesis spaces is not), (iv) mandatory disconfirmation probes in the EIG pool (absent from all prior BOED-for-preference work), (v) application to LLM response-style personalization (format, tone, structure)—a domain shift from BED-LLM's latent preference vector inference. (3b) Comparison-based active preference learning for LLM personalization: AMPLe (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) personalizes LLM outputs to implicit multi-dimensional preferences via pairwise comparison queries, a modified Bayesian posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection. AMPLe is directly adjacent to FABEL in the active Bayesian personalization space but differs in three critical ways: (1) AMPLe cold-starts from pairwise item comparisons rather than initializing from user demonstrations; (2) AMPLe asks 'which response do you prefer?' (item comparison) rather than 'does this stylistic hypothesis apply to you?' (hypothesis confirmation); (3) AMPLe includes no disconfirmation probe mechanism. AMPLe must be cited as an ACL 2025 active Bayesian personalization baseline; its comparison-based query design and FABEL's hypothesis-confirmation design represent complementary elicitation paradigms. (4) Generative open-ended elicitation: GATE (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) uses free-form LLM-generated questions in three domains; its binary yes/no variant reduces cognitive load but underperforms the open-ended variant because binary questions without a Bayesian posterior cannot adaptively narrow the hypothesis space—GATE's binary variant also does not ground questions in user demonstrations. (5) Trajectory-optimized clarification: TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior. (6) Bayesian-RL hybrid: PEBOL (arXiv 2405.00981, RecSys 2024) combines NLI-based preference beliefs with Thompson Sampling in recommendation. (7) Bayesian in-context conditioning from demonstrations (adjacent): Variational In-Context Reward Modeling / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) casts reward modeling as amortized variational inference over a latent preference with a conjugate Beta prior conditioned on in-context preference demonstrations at test time without retraining—conceptually adjacent to FABEL's warm-start initialization from demonstrations but differs in three critical ways: domain (pairwise scalar reward modeling vs. interactive response-style personalization), hypothesis representation (continuous Beta prior on scalar rewards vs. discrete binary preference hypotheses), and interaction mode (passive in-context update vs. active EIG confirmation loop); no disconfirmation probes; acknowledged in related work to pre-empt warm-start novelty challenge. (8) Few-shot preference optimization: FSPO (arXiv 2502.19312, 2025) meta-learns personalization from few-shot preference data; deferred to Phase 2 due to meta-training infrastructure overhead. The specific combination absent from all prior work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, and PROSE's non-interactive refinement.\",\n  \"approach\": \"We propose FABEL (Falsification-Aligned Binary Elicitation Loop), a tuning-free framework operating in four stages. The EMNLP 2026 submission is scoped as an MVP: PersonalLLM benchmark, four baselines, one LLM backbone (Qwen2.5-7B-Instruct), one core ablation, and a small crowdsourced human evaluation (n≈20) to strengthen the EMNLP Main case.\\n\\nStage 1—Demonstration-Grounded Hypothesis Generation with Disconfirmation Probes: Given K=5–10 few-shot user output demonstrations, a frontier open-source LLM (Qwen2.5-7B-Instruct) generates N_pos=12–15 falsifiable, binary-verifiable preference hypotheses (e.g., 'User prefers bulleted structure over prose') AND K_neg=4–6 explicit disconfirmation probes—hypotheses deliberately constructed to be easily falsifiable given the demonstrations (e.g., 'User avoids technical terminology' when demonstrations frequently use it). This two-class design, motivated by arXiv 2604.02485's finding that LLMs default to generating confirmable hypotheses, ensures the EIG pool contains falsifying evidence. To elicit genuinely falsifiable probes rather than merely low-confidence confirmatory hypotheses (the LLM default per arXiv 2604.02485), we use a dedicated generation prompt distinct from the confirmatory hypothesis prompt: 'Given these K writing samples, generate K_neg stylistic hypotheses that are plausibly true of some users but are ACTIVELY VIOLATED by the provided samples—attributes the demonstrations explicitly disconfirm. For each probe, cite the specific demonstration evidence that falsifies it. Example: if all samples use numbered lists, generate the probe \\\"User avoids numbered lists\\\" and cite the list usage as falsifying evidence.' The evidence-citing requirement prevents the model from producing vacuously non-committal probes and ensures each H_neg hypothesis is verifiably falsifiable against the provided demonstrations.\\n\\nStage 2—Temperature-Scaled Warm Prior Initialization with Calibration Check: Each hypothesis posterior is initialized as p(h_i = true | demos) ∝ exp(score_i / τ), where score_i is the LLM log-likelihood of the K demonstrations given hypothesis h_i, and τ is a temperature hyperparameter controlling prior sharpness. Raw LLM log-likelihoods are typically overconfident (τ=1); τ is selected on a held-out 50-user PersonalLLM dev split as the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6 (validation threshold). If no τ in the search grid achieves ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent, equivalent to a cold start) and flag this as a calibration failure in diagnostic analysis—indicating that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for the evaluated hypothesis class. τ→∞ recovers a uniform prior (a maximally uninformative cold start, distinct from BED-LLM's LM-generic prior p_f(θ;∅), which reflects the LLM's own unconditional distribution over hypotheses and is neither uniform nor user-specific); τ=1 applies raw likelihoods. This design directly addresses LLM miscalibration: it ensures the warm start concentrates mass on demonstration-consistent hypotheses while avoiding premature posterior collapse onto incorrect hypotheses. The calibration analysis—Stage 2a in the paper—reports Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users, validating the warm-start assumption empirically and providing a lightweight check that does not require additional model training. Empirical hypothesis accuracy is operationalized as follows: for each simulated PersonalLLM dev user u (a weighted ensemble of 10 reward models with Dirichlet-sampled weights) and each hypothesis h_i, empirical accuracy = fraction of u's top-quartile responses (by u's weighted-ensemble reward score across the 8 candidate responses per prompt) that satisfy h_i, as assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i. Spearman ρ is then computed between the vector of LLM log-likelihood scores [score_1, …, score_N] and the vector of empirical accuracies [acc_1, …, acc_N] across all N hypotheses, averaged over the 50 dev users. This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.\\n\\nWe note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences—a limitation consistent with documented self-preference bias in LLM-as-judge evaluation (arXiv 2601.20913). To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis satisfaction classifier (cross-model calibration check); if ρ remains above 0.6 under cross-model evaluation, the warm-start assumption is validated against self-consistency inflation. If cross-model ρ falls below 0.6 while same-model ρ exceeds it, we treat this as evidence of self-consistency inflation and default to the uniform prior (τ→∞) in the main experiments, flagging the discrepancy as a stated limitation. If both same-model and cross-model ρ fall below 0.6, we acknowledge that LLM log-likelihoods are not predictive of empirical hypothesis accuracy for this hypothesis class and defer warm-start calibration to Phase 2.\\n\\nStage 3—EIG-Based Binary Elicitation Loop with Disconfirmation Quota (algorithm specification): The full hypothesis set H = H_pos ∪ H_neg is placed in a single EIG-ranked pool. At each turn, FABEL selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2 — and poses it as a binary yes/no confirmation. The posterior updates via Bayes' rule with a noise term calibrated on held-out demo pairs. We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization H(p(h_i)) is equivalent to EIG-based selection. The loop terminates when joint preference entropy drops below threshold θ (empirically 3–5 turns).\\n\\nDisconfirmation probe handling follows option (a)—probes are included in the EIG pool and selected by EIG only when maximally uncertain. This is algorithmically cleanest: EIG without H_neg would face a pool containing only confirmatory hypotheses, creating a structural selection bias toward echo-chamber convergence regardless of EIG's own informativeness criterion. Including H_neg in the pool makes the probe design a prior-shaping device rather than a scheduling override—EIG's entropy criterion then serves as a bidirectional diagnostic. If H_neg probes are never selected (prior already confidently classifies them as false), this is evidence of good prior calibration; if frequently selected (probes have high posterior entropy at elicitation start), this signals prior miscalibration requiring attention.\\n\\nSoft minimum quota: To prevent the degenerate case where warm-start prior overconfidence silently suppresses all falsifying questions, at least ⌈K_neg / 3⌉ disconfirmation probes must be asked if the loop runs ≥3 turns. Quota-forced questions bypass EIG ordering for their designated turn but receive normal Bayesian updates. The 'disconfirmation selection rate'—fraction of turns where EIG (prior to quota enforcement) would have selected a H_neg hypothesis—is reported as a diagnostic distinguishing well-calibrated priors (low rate: probes already resolved by warm start) from miscalibrated ones (high rate: probes still maximally uncertain at elicitation start). The falsification rate—fraction of posterior updates that decrease hypothesis probability—is reported as a secondary diagnostic.\\n\\nStage 4—Personalized Generation: The confirmed/disconfirmed hypothesis set is injected as a structured system prompt without fine-tuning.\\n\\nMVP Experimental Design (EMNLP 2026 ARR deadline May 25, 2026):\\n- Benchmark: PersonalLLM (ICLR 2025), using its reward-model-based simulated user evaluation infrastructure (public dataset: HuggingFace namkoong-lab/PersonalLLM); simulated evaluation eliminates GPT-4-judge latency and cost, enabling full experimental sweep within the 15-day window\\n- Human evaluation study (EMNLP Main strengthening, optional stretch): n≈20 crowdsourced participants via Prolific; each participant interacts with FABEL over 10 PersonalLLM prompts and evaluates personalized vs. baseline responses; setup requires ~1 agent-day (days 3–4, running in parallel with automated experiments); cost ~$100–200; the study is underpowered for statistical inference and results are reported descriptively—it provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas, reported descriptively\\n- Backbone: Qwen2.5-7B-Instruct (single backbone for all methods)\\n- Baselines (4): (1) HyPerAlign—demonstration-grounded, no validation; (2) GATE binary—binary questions, no Bayesian posterior, no demonstration grounding; (3) PROSE—iterative preference inference from demonstrations, no user interaction, no Bayesian posterior; applied by running PROSE's generate→compare→update pipeline on PersonalLLM demonstrations, evaluating via reward model; (4) BED-LLM—LM-generic-prior EIG Bayesian with multiple-choice questions; reimplemented from paper description (no public code; Rao-Blackwellized EIG estimator + rejection-sampling update, ~45–50 LLM calls/step); time-boxed to 3–4 agent-days with fallback to 'BED-LLM-approx' (entropy-based selection + rejection-sampling, no full RB-EIG) if faithful replication is infeasible, with explicit labeling\\n- Core ablation (1): warm-start prior (τ-scaled from demos) vs. uniform prior (τ→∞), directly isolating the demonstration-grounded initialization contribution\\n- Primary metrics: PersonalLLM reward-model win rates (main); average elicitation turns (efficiency); disconfirmation selection rate + falsification rate (diagnostics); human preference rates if study included; same-model vs. cross-model Spearman ρ (Stage 2a calibration circularity diagnostic)\\n- Phase 2 extensions (camera-ready / full paper): LaMP-4/6/7 text generation benchmarks; AMPLe and FSPO baselines; full ablation battery (probes included vs. excluded; EIG vs. random ordering; K sensitivity N∈{3,5,10}; τ sensitivity; full BED-LLM replication verification); additional backbone (Qwen2.5-14B-Instruct or Llama 4 Maverick)\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"description\": \"EMNLP 2026 MVP — PRIMARY mode\",\n      \"gpu_hours\": \"~150h A100 (MVP: PersonalLLM only, 4 baselines, 1 backbone, 1 ablation)\",\n      \"h100_equivalent\": \"~75h H100-equivalent (at 2× A100/H100 throughput ratio) — explicitly within the ≤200 H100-hour hard constraint\",\n      \"gpu_utilization\": \"High (~85–90%): agent continuously queues inference jobs with no human wait time; primary idle periods are inter-job I/O and BED-LLM implementation phase\",\n      \"timeline\": \"12–14 days with 2× A100s running in parallel; Prolific human study set up days 3–4 in parallel, adding <1 agent-day overhead; cross-model ρ check (Llama-3.1-8B as hypothesis classifier) adds ~0.25 agent-days to Stage 2a\",\n      \"team\": \"0 (3–5h initial setup)\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 agent reasoning turns)\",\n      \"estimated_gpu_cost\": \"$300–450 at ~$2–3/hr A100 rental\",\n      \"human_study_cost\": \"~$100–200 (n≈20 Prolific participants at ~$5–10/participant; set up in parallel days 3–4)\",\n      \"cost_notes\": \"PersonalLLM reward-model evaluation (simulated) eliminates GPT-4-judge cost; total project cost $550–900 including optional human study; Phase 2 adds ~$400–600 GPU and ~$150–300 GPT-4-judge for LaMP tasks\",\n      \"speed_bottleneck\": \"BED-LLM EIG reimplementation (no public code; time-boxed 3–4 agent-days with simplified fallback); PROSE implementation straightforward (~1 agent-day, purely prompt-based); Stage 2a calibration analysis (same-model + cross-model ρ) adds ~0.75 agent-days total\",\n      \"compliance_note\": \"150h A100 ÷ 2 (H100/A100 throughput ratio) = 75h H100-equivalent, well within the 200 H100-hour limit\"\n    },\n    \"human_in_loop\": {\n      \"description\": \"Full paper (post-EMNLP, adds LaMP + full ablations)\",\n      \"gpu_hours\": \"~300h A100\",\n      \"gpu_utilization\": \"Moderate (~50–60%): agent continuously queues inference jobs between human approval gates; BED-LLM replication verified at first review gate before full baseline run\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,200–2,000 reasoning turns)\",\n      \"estimated_gpu_cost\": \"$600–900\",\n      \"risk_note\": \"Warm-start prior calibration (Spearman ρ threshold) must be validated on PersonalLLM dev split before committing to full experimental sweep; both same-model and cross-model ρ confirmed at a dedicated calibration gate before main experimental sweep; τ selection and BED-LLM replication fidelity confirmed at dedicated review gates\"\n    },\n    \"manual\": {\n      \"description\": \"Full paper (post-EMNLP, adds LaMP + full ablations)\",\n      \"gpu_hours\": \"~200h A100\",\n      \"gpu_utilization\": \"Low (~20–30%): GPU idles while researchers implement BED-LLM baseline, write pipeline code, and analyze results\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"$400–600 at ~$2–3/hr A100 rental\",\n      \"cost_notes\": \"GPT-4-as-judge for LaMP evaluation adds ~$150–300; total project cost $550–900\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings via ACL ARR (deadline May 25, 2026 — 15 days from project start May 10, 2026) — PRIMARY realistic target; MVP scope (PersonalLLM, 4 baselines, 1 backbone, 1 ablation + Stage 2a calibration analysis with cross-model ρ check) is credible for EMNLP Findings; adding the n≈20 Prolific human study puts EMNLP Main within reach if human results are positive — this is the stretch Main goal, not the base expectation; targets EMNLP 2026 Findings as the primary submission outcome\",\n    \"ICLR 2027 (expected submission deadline ~October 2026) — SECONDARY target if EMNLP 2026 submission scope is insufficient or if full paper (LaMP + full ablation battery) is preferred; strongest venue fit given GATE (ICLR 2025), OPEN (ACL 2024), and BED-LLM (ICLR 2026) lineage; full paper with multi-benchmark and human study comfortably meets Main bar\",\n    \"AAAI 2027 (expected abstract/paper deadline ~August–September 2026) — TERTIARY target with sufficient runway for full experimental sweep including LaMP benchmarks and multiple backbone ablations\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"OPEN: Bayesian Preference Elicitation with Language Models (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) — foundational BOED-for-preference-elicitation work; combines EIG-based query selection with LM feature extraction for content recommendation; selects pairwise queries over binary feature vectors (|F|=10) using particle-filter Bayesian update with Bradley-Terry model; prior initialization via LM-ranked feature importances (domain-generic warm start: w_i = 1.2 − 0.12i for rank i), NOT user-demonstration-conditioned; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-specific demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism; cite as the foundation of the BOED-for-preference-elicitation line that BED-LLM extends and FABEL further advances\",\n    \"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design (arXiv 2508.21184, ICLR 2026) — extends OPEN to discrete language hypothesis sets; initializes from an LM-generic prior p_f(θ;∅) (the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations; notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions as a technical requirement (small single-token response spaces ensure p_LLM provides meaningful uncertainty for EIG estimation); EIG uses Rao-Blackwellized N=15-sample estimator + rejection-sampling posterior update (~45–50 LLM calls/turn); evaluates on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions game; no public code; reimplementation time-boxed to 3–4 agent-days with simplified fallback; FABEL differentiates in three ways: (1) prior conditioned on this user's K demonstrations vs. BED-LLM's demo-agnostic LM prior; (2) binary yes/no confirmation vs. BED-LLM's multiple-choice format; (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work\",\n    \"AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) — active Bayesian preference learning for LLM personalization; pairwise comparison queries over LLM responses, modified posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection to minimize required comparisons; directly adjacent to FABEL's active Bayesian personalization setting; FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary stylistic hypothesis confirmation rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe; include as related work in landscape cluster (3b); include as Phase 2 baseline on LaMP tasks\",\n    \"PROSE: Aligning LLMs by Predicting Preferences from User Writing Samples (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) — directly competitive with FABEL Stage 1; iterative generate→compare→update refinement of free-form preference descriptions + component-level verification against held-out samples; 33% improvement over CIPHER on summarization/email; no user interaction, no Bayesian posterior, no disconfirmation mechanism; baseline and key differentiator\",\n    \"GATE: Eliciting Human Preferences with Language Models (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) — binary yes/no variant underperforms open-ended due to absence of Bayesian posterior; baseline\",\n    \"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation (arXiv 2505.00038, May 2025) — demonstration-grounded hypothesis generation without user validation; baseline\",\n    \"Failing to Falsify: LLM Confirmation Bias in Hypothesis Testing (arXiv 2604.02485, April 2026) — motivates disconfirmation probe design; 42%→56% rule-discovery success with counter-example prompting; motivates H_neg pool inclusion in FABEL Stage 3\",\n    \"Bayesian Preference Learning for Test-Time Steerable Reward Models / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) — amortized variational inference with conjugate Beta prior conditioned on in-context preference demonstrations; conceptually adjacent to FABEL's warm-start but differs in domain (pairwise reward modeling vs. interactive style elicitation), representation (Beta prior on scalar rewards vs. binary hypothesis set), and interaction mode (passive vs. active EIG confirmation); acknowledge in related work to pre-empt warm-start novelty challenge\",\n    \"Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (arXiv 2601.20913, 2026) — provides hypothesis testing framework for cross-model evaluation with calibrated confidence metrics; cited to motivate FABEL's cross-model ρ check (using Llama-3.1-8B-Instruct as hypothesis classifier to bound the self-consistency inflation artifact in Stage 2a)\",\n    \"Active Task Disambiguation with LLMs (arXiv 2502.04485, ICLR 2025) — BED applied to task clarification; related but not personalization-focused\",\n    \"TO-GATE: Clarifying Questions and Summarizing Responses with Trajectory Optimization (arXiv 2506.02827, 2025) — applies trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline (a clarification resolver generating optimal questioning trajectories plus a summarizer for task-aligned responses); remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior; achieves 9.32% improvement over STaR-GATE on preference elicitation tasks; cited as an open-ended, non-Bayesian clarification baseline in landscape cluster (5)\",\n    \"PEBOL: Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation (arXiv 2405.00981, RecSys 2024) — NLI + Bayesian BO for recommendation; related\",\n    \"Asking Clarifying Questions for Preference Elicitation With Large Language Models (arXiv 2510.12015, 2025) — diffusion-inspired clarifying question model; distinct from PEBOL\",\n    \"FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users (arXiv 2502.19312, 2025) — deferred to Phase 2 / full paper; requires meta-learned model setup adds ~1–2 weeks engineering overhead\",\n    \"PersonalLLM: Tailoring LLMs to Individual Preferences (ICLR 2025) — primary benchmark; public dataset HuggingFace namkoong-lab/PersonalLLM (9,402 train / 1,000 test prompt-response pairs, 8 candidate responses per prompt scored by 10 reward models, simulated users as Dirichlet-weighted reward model ensembles); reward-model-based simulated evaluation eliminates GPT-4-judge dependency and enables 15-day timeline\",\n    \"LaMP: When Large Language Models Meet Personalization (ACL 2024) — secondary benchmark for Phase 2; LaMP-4/6/7 text generation tasks assess format and style personalization\",\n    \"Calibrating Language Models with Adaptive Temperature Scaling (arXiv 2409.19817, EMNLP 2024) — post-hoc temperature calibration method for LLM token probabilities without fine-tuning; informs FABEL's τ-scaled warm prior design: p(h_i) ∝ exp(score_i / τ) with τ selected via dev-set rank-correlation criterion\"\n  ],\n  \"description\": \"Personalizing LLMs to individual users is hindered by three complementary failure modes: HyPerAlign generates demonstration-grounded preference hypotheses but skips user validation; the BOED-for-preference-elicitation line—established by OPEN (ACL 2024) and extended by BED-LLM (ICLR 2026)—applies principled EIG-based Bayesian elicitation but lacks user-specific demonstration-conditioned priors (OPEN uses domain-generic LM-ranked feature importances; BED-LLM uses an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution, not conditioned on any specific user's demonstrations); and PROSE (ICML 2025) iteratively refines free-form preference descriptions from writing samples but has no user interaction and no formal Bayesian posterior, leaving ambiguous hypotheses unresolved. AMPLe (ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation but also cold-starts from pairwise comparisons and lacks disconfirmation probes. We propose FABEL (Falsification-Aligned Binary Elicitation Loop), which extends the OPEN→BED-LLM BOED lineage by (1) initializing a temperature-scaled warm Bayesian prior p(h_i) ∝ exp(score_i / τ) from K=5–10 user-specific demonstrations—user-specific rather than domain-generic or demo-agnostic; (2) including K_neg=4–6 explicit disconfirmation probes in the EIG-ranked hypothesis pool, generated via a dedicated falsification prompt that requires citing demonstration-level evidence for each probe, making the probe design a prior-shaping device that ensures EIG always has access to genuinely falsifying evidence; (3) applying a soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns) to prevent warm-start overconfidence from silently suppressing falsifying questions; (4) applying a factored posterior approximation with EIG-based binary yes/no confirmation (vs. BED-LLM's multiple-choice format, which is required for reliable LLM uncertainty quantification but increases cognitive load) to resolve remaining uncertainty in 3–5 turns; and (5) explicitly acknowledging that under the factored (independent) posterior approximation, marginal entropy maximization is equivalent to EIG-based selection. Stage 2a includes a calibration analysis (Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy on 50 PersonalLLM dev users, where empirical accuracy is operationalized as the fraction of each simulated user's top-quartile reward-model responses satisfying each hypothesis) that validates the warm-start assumption and selects τ; if no τ achieves ρ > 0.6, the system defaults to a uniform prior and flags the calibration failure. Critically, Stage 2a also addresses a circularity in this operationalization—the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and accuracy labels—by additionally reporting ρ using Llama-3.1-8B-Instruct as an independent hypothesis classifier (cross-model calibration check; arXiv 2601.20913); if cross-model ρ falls below 0.6 while same-model ρ exceeds it, the system defaults to the uniform prior, treating the discrepancy as evidence of self-consistency inflation. The EMNLP 2026 MVP targets Findings as the primary outcome, with an optional n≈20 Prolific human study (days 3–4, ~$100–200) that is underpowered for statistical inference and reported descriptively—providing preliminary external validity evidence beyond simulated personas, reported descriptively. The central testable claim: demonstration-grounded user-specific warm priors reduce required elicitation turns vs. both OPEN (domain-generic warm start) and BED-LLM (demo-agnostic LM prior) while achieving higher personalization win rates than non-interactive methods (PROSE, HyPerAlign). LaMP benchmarks, AMPLe/FSPO baselines, and full ablations are deferred to Phase 2.\",\n  \"project_name\": \"falsif_guided_pe\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"BED-LLM (arXiv 2508.21184, ICLR 2026) is unacknowledged and directly covers the core mechanism: it samples N=15 hypotheses, uses EIG to select questions designed to 'slice the hypothesis pool into roughly balanced subsets,' and applies Bayesian rejection-sampling updates — the central algorithmic contribution of FABEL. The paper must be cited and clearly differentiated.\", \"GATE (ICLR 2025) already includes a yes-or-no binary question variant ('restricts the LM to generating binary yes-or-no questions'). The generator's landscape description characterizes GATE as purely open-ended, which is factually incomplete. The binary format alone is not a differentiating contribution.\", \"PEBOL arXiv attribution error: the generator cites '(arXiv 2510.12015)' as the PEBOL paper, but arXiv 2510.12015 is 'Asking Clarifying Questions for Preference Elicitation With Large Language Models' (a diffusion-inspired model, not PEBOL). The actual PEBOL paper is arXiv 2405.00981 (RecSys 2024). This is a citable factual error that would immediately surface in peer review.\", \"Venue deadline is misidentified: the generator claims 'ACL ARR June 2026 cycle, deadline ~June 15 2026' but the confirmed EMNLP 2026 ARR submission deadline is May 25, 2026 (per official EMNLP 2026 CFP and ACL ARR Dates page). The June cycle does not feed EMNLP 2026. This affects the entire planning horizon.\", \"LLM confirmation bias undermines the 'falsification' framing: arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs systematically exhibit confirmation bias in hypothesis testing — they select confirmatory rather than falsifying evidence. This suggests that LLM-generated hypotheses will be easier to confirm than disconfirm, and the Bayesian posterior may converge spuriously. The paper should address whether its hypotheses are genuinely falsifiable or merely confirmable.\", \"PRISM benchmark misfit: PRISM (NeurIPS 2024) is designed for multicultural value alignment and subjective disagreement, not individual preference personalization of LLM response style. Evaluating FABEL — which targets writing format, structure, and tone — on PRISM is not well-motivated. The authors should justify why PRISM reveals anything beyond PersonalLLM for the proposed application.\", \"GPU cost realism: evaluating against FSPO (which requires a pretrained meta-learning model) as a baseline may require non-trivial setup not captured in the 150h A100 manual estimate; the GPT-4-as-judge costs for PersonalLLM-scale evaluation (1500 simulated users) could also be underestimated.\"]\nFeedback: The core insight — combining HyPerAlign-style demonstration-grounded hypothesis generation with EIG-based binary validation — is a coherent contribution to the personalization literature, but the generator must make three priority revisions before this is ready to submit:\n\n1. **Reposition against BED-LLM (ICLR 2026)**: 'This idea is too similar to BED-LLM (arXiv 2508.21184, ICLR 2026). Specifically, BED-LLM samples N=15 hypotheses, selects questions via EIG to split the hypothesis set, and updates beliefs with Bayesian rejection sampling — the same pipeline as FABEL. To differentiate, the generator should (a) explicitly compare against BED-LLM as a baseline, (b) emphasize FABEL's unique starting point of few-shot user demonstrations (HyPerAlign-style) rather than free-form hypothesis sampling, and (c) show that grounding hypotheses in demonstrations produces qualitatively different, more accurate preference summaries than BED-LLM's unconditioned sampling. The application domain (LLM response style vs. item recommendation) is a real differentiator worth foregrounding.'\n\n2. **Fix the GATE landscape description**: Acknowledge the GATE binary variant and clarify why FABEL differs — likely the combination of demonstration-grounded hypothesis generation (not free-form question asking) with Bayesian belief tracking is the real gap, not the binary format alone.\n\n3. **Fix the PEBOL arXiv attribution (2510.12015 → 2405.00981) and the venue deadline (June 15 → May 25).** These are immediate disqualifiers for a careful reviewer.\n\n4. **Address confirmation bias**: Add analysis or ablation showing the LLM does not systematically generate only confirmable hypotheses. Consider adding a 'disconfirmation probe' to the hypothesis set by design, or show empirically that the posterior does update in both directions.\n\nIf BED-LLM is incorporated as a strong baseline and FABEL shows clear gains on the LLM response-style personalization task (PersonalLLM win-rates, reduced user-turn word count), the contribution is publishable at EMNLP Findings level. As written, the novelty gap is insufficient for EMNLP Main.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Venue requirement failure: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, ≤16 days). The proposal itself concedes this deadline 'has effectively passed for a project beginning now (May 10, 2026)' and retargets to AAAI 2027/ICLR 2027. This is an honest but fatal mismatch: the idea as scoped cannot satisfy the user's primary hard constraint. Either a severely stripped-down MVP (PersonalLLM only, BED-LLM + HyPerAlign as the two primary baselines, no LaMP sweep, no full ablation, simulated user evaluation only) must be proposed for the 16-day window, or the idea should explicitly declare EMNLP 2026 out of scope.\", \"CRITICAL — Compute constraint non-compliance in the 16-day-feasible mode: The auto_research mode (the only mode that meets ≤16 days) uses ~600h A100. At the industry-standard ~2–2.5× H100/A100 throughput ratio, this translates to approximately 240–300 H100-hours — exceeding the ≤200 H100-hour hard constraint by 20–50%. A minimum viable experiment (PersonalLLM + 3 baselines, 1 backbone, core ablation) would likely require only ~150–180h A100 (≈75–90h H100), well within limits — but this needs to be explicitly scoped and stated rather than leaving the constraint compliance implicit.\", \"Missing citation — PROSE (arXiv 2505.23815, ICML 2025): 'Aligning LLMs by Predicting Preferences from User Writing Samples' (Aroca-Ouellette et al., Apple ML Research) uses user writing demonstrations to iteratively refine free-form preference descriptions, then verifies component claims against held-out demonstrations. This is directly competitive with FABEL Stage 1 and was not cited anywhere in the landscape. A reviewer would flag this immediately. To differentiate: PROSE infers free-form preferences with no user interaction and no Bayesian posterior; FABEL generates binary-confirmable hypotheses, tracks a formal Bayesian posterior, selects questions via EIG, and adds mandatory disconfirmation probes. PROSE should be added as a sixth baseline or at minimum a related work requiring explicit differentiation.\", \"BED-LLM reimplementation risk underestimated for 16-day window: The proposal's own auto_research note flags 'faithful replication of their rejection-sampling update' as the primary engineering risk. BED-LLM's EIG estimator involves non-trivial sampling over LLM predictive distributions at each turn. Reproducing this within a 16-day timeline — alongside implementing FABEL itself and running PersonalLLM/LaMP evaluations — is aggressive. The proposal should either identify an existing public BED-LLM implementation or explicitly time-box the reimplementation risk.\", \"ICRM / Bayesian Preference Learning for Test-Time Steerable Reward Models (arXiv 2602.08819, Feb 2026) not cited: This paper uses a Beta posterior conditioned on in-context preference demonstrations for test-time reward model steering — partial overlap with FABEL's warm-start initialization from demonstrations. The settings differ (pairwise reward modeling vs. interactive style elicitation), but the Bayesian in-context conditioning from demonstrations is directly adjacent and a reviewer familiar with this work might question the warm-start prior novelty. It should be acknowledged in the related work.\"]\nFeedback: The generator has addressed all six Round 1 issues cleanly and the core idea remains sound, but two critical problems prevent a pass verdict:\n\n**Priority 1 — Scope the idea for the actual 16-day / EMNLP 2026 constraint (or declare a mismatch).**\nThe generator honestly acknowledges EMNLP 2026 is unreachable for a full 5-baseline sweep across PersonalLLM + LaMP. But the user's hard constraint is 16 days and EMNLP 2026. The generator should choose one of:\n(a) Propose a stripped-down EMNLP 2026 MVP: PersonalLLM benchmark only, 3 baselines (HyPerAlign, BED-LLM, GATE binary), 1 LLM backbone (Qwen 3.5), simulated user evaluation using the PersonalLLM reward-model infrastructure, 1 ablation (warm vs. uniform prior). Estimated compute: ~150h A100 (~75h H100-equivalent), 12–14 days in auto mode. This fits all hard constraints.\n(b) Explicitly flag the idea as AAAI 2027 / ICLR 2027 scope with a concrete explanation of why 16 days is insufficient for the full version — so the user can make an informed decision.\n\n**Priority 2 — Add PROSE as a baseline and missing citation.**\nPROSE (arXiv 2505.23815, ICML 2025) directly competes with FABEL's Stage 1: it takes user writing samples and iteratively refines preference descriptions with component verification. Cite it, differentiate it (PROSE: free-form, non-interactive, no Bayesian posterior; FABEL: binary hypotheses, interactive EIG confirmation, formal posterior, disconfirmation probes), and include it as a baseline. Without PROSE, the novelty argument has an obvious gap that peer reviewers would flag.\n\n**Priority 3 — Fix the compute compliance in auto mode.**\nRestate the minimum-viable-experiment compute as ~150–180h A100 and explicitly confirm it falls under 200 H100-hour equivalent. The full 600h A100 ablation sweep is 'nice to have' for camera-ready, not required for ARR submission.\n\nIf the generator delivers a scoped EMNLP 2026 MVP (Priority 1) with PROSE integrated (Priority 2) and compute compliance verified (Priority 3), the idea is publishable at EMNLP 2026 Findings level. The core novelty — warm-start Bayesian initialization from demonstrations + EIG binary confirmation + mandatory disconfirmation probes — is genuinely new and the empirical design (warm vs. cold prior ablation, disconfirmation rate diagnostic) is strong. The differentiation from BED-LLM (cold start, item recommendation) and from PROSE/HyPerAlign (no interactive validation) is clean.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"OPEN (arXiv 2403.05534, ACL 2024) — 'Bayesian Preference Elicitation with Language Models' — is not cited. This paper applies Bayesian Optimal Experimental Design (BOED, mathematically equivalent to EIG) with LMs to select informative preference-elicitation questions in natural language. It is a direct algorithmic predecessor to BED-LLM for the preference elicitation setting and a reviewer aware of it would challenge FABEL's EIG-over-BED-LLM positioning. The proposal should cite OPEN as the foundation of the BOED-for-preference-elicitation line, position BED-LLM as the current state of that line, and clarify how FABEL (demonstration-grounded warm start + disconfirmation probes) extends beyond both.\", \"Disconfirmation probe / EIG interaction is algorithmically underspecified. The proposal includes K_neg=4–6 disconfirmation probes in the hypothesis set but does not specify how EIG-based selection handles them at each turn: (a) are they included in the EIG-ranked pool and selected only when EIG identifies them as maximally informative — in which case the EIG criterion may already approximate the disconfirmation behavior, making the explicit probe design partially redundant; (b) are they always asked in the first K_neg turns before EIG kicks in — which wastes turns if the demonstrations already resolved them; or (c) are they asked as post-loop audits — which breaks the Bayesian update chain. This interaction must be precisely specified in the algorithm description, since it determines whether the disconfirmation probe mechanism adds genuine information-theoretic value beyond EIG or is purely a diagnostic overlay.\", \"Warm-start prior calibration is assumed but unvalidated. The proposal initializes p(h_i = true | demonstrations) using LLM-estimated likelihoods conditioned on K demonstrations. LLM probability estimates are notoriously poorly calibrated — overconfident estimates would concentrate mass on the wrong hypotheses before any user interaction, potentially causing slower convergence than a uniform (BED-LLM-style) cold start. The paper should either (a) include an empirical calibration check showing the LLM-estimated likelihoods are well-ordered relative to ground-truth hypothesis accuracy, or (b) add a temperature-scaling or entropy-regularized prior initialization step with explicit justification.\", \"EMNLP 2026 Main vs. Findings targeting realism. The user specified EMNLP 2026 Main as the primary target. The MVP (single benchmark PersonalLLM, simulated reward-model evaluation, one backbone Qwen 3.5-7B, one ablation) is credible for EMNLP Findings but borderline for Main. EMNLP Main typically requires either (a) multi-benchmark generalization, (b) a human user study even at small scale, or (c) a theoretically novel contribution beyond component combination. The current design lacks all three. The proposal should either explicitly target Findings as the realistic primary target, or strengthen one of these dimensions — even a 20-person crowdsourced preference evaluation using the PersonalLLM prompts would substantially strengthen the Main case within the 16-day window.\"]\nFeedback: The proposal has cleanly addressed all Round 1 and Round 2 critical issues: venue deadline is correct (May 25, 2026), compute is within budget (~75h H100-equivalent), PROSE is included as baseline #3, BED-LLM is confirmed accepted at ICLR 2026, ICRM is acknowledged, and the MVP scope is explicitly and realistically defined. The core idea — warm-start Bayesian prior from demonstrations + EIG binary confirmation + disconfirmation probes — is a coherent, well-motivated contribution. Three targeted revisions will bring this to pass:\n\n**Fix 1 — Add OPEN to the landscape (1 paragraph in related work):** 'This idea is too similar to OPEN (arXiv 2403.05534, ACL 2024) without acknowledgment. OPEN applies BOED with LMs to select informative preference questions in NL — the same mathematical framework as BED-LLM, specifically for preference elicitation. To differentiate: OPEN lacks demonstration-conditioned priors, requires cold-start initialization, and has no disconfirmation mechanism. Include OPEN in the BOED lineage alongside BED-LLM and clarify that FABEL's contribution is the warm-start + disconfirmation extension of this line.'\n\n**Fix 2 — Specify disconfirmation probe algorithm precisely:** Add a paragraph to Stage 3 clarifying whether disconfirmation probes are (a) included in the EIG-ranked pool, (b) asked as mandatory initial turns, or (c) reserved as post-convergence audits. Option (a) is algorithmically cleanest — EIG will naturally select them when they are maximally uncertain, making the explicit design a prior-shaping device rather than a scheduling override. Report the empirical fraction of turns where EIG selects a disconfirmation probe vs. a positive hypothesis as a diagnostic.\n\n**Fix 3 — Calibration check or regularization for warm-start prior:** Add either (a) a small analysis showing that LLM-estimated likelihoods are well-ordered relative to demonstration-consistent hypotheses (even a rank-correlation analysis on 50 PersonalLLM examples would suffice), or (b) a temperature-scaled prior initialization: p(h_i) ∝ exp(LLM_log_likelihood / τ) with τ tuned to match empirical calibration. This directly addresses the most technically vulnerable assumption in the method.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL reproducibility error — 'Qwen 3.5-7B-Instruct' does not exist: Qwen3.5 (released Feb 2026) contains 4B, 27B, 35B-A3B (MoE), and 397B-A17B (MoE) variants; there is no 7B model in the Qwen3.5 family. This model name appears throughout the proposal as the single backbone. The correct alternatives are Qwen2.5-7B-Instruct (huggingface.co/Qwen/Qwen2.5-7B-Instruct, widely used in personalization benchmarks) or Qwen3-8B (huggingface.co/Qwen/Qwen3-8B). A reviewer or reproduction attempt would fail immediately at environment setup. Fix: replace all instances of 'Qwen 3.5-7B-Instruct' with 'Qwen2.5-7B-Instruct' or 'Qwen3-8B' with the appropriate HuggingFace identifier.\", \"Missing citation — AMPLe (arXiv 2411.00524, ACL 2025): 'Comparison-based Active Preference Learning for Multi-dimensional Personalization' (Oh, Lee, Ok; ACL 2025, with public code at github.com/ml-postech/AMPLe) uses Bayesian inference with modified posterior updates and a generalized binary-search-inspired active query selection strategy to capture implicit multi-dimensional preferences for LLM personalization — directly adjacent to FABEL's active Bayesian personalization setting. While AMPLe uses pairwise comparison queries rather than demonstration-conditioned hypotheses (making differentiation clear: FABEL provides a warm prior from demonstrations, asks binary hypothesis confirmation rather than item comparisons, and adds mandatory disconfirmation probes), the omission of an ACL 2025 active Bayesian preference learning paper in the LLM personalization domain is a gap that reviewers familiar with the area would notice. Add to the landscape under cluster (3) or create a new cluster for comparison-based active preference learning.\", \"Unstated hypothesis-independence assumption in Stage 3 Bayesian update: The per-hypothesis Bayesian update (applying Bayes' rule independently to each h_i) implicitly treats all preference hypotheses as statistically independent. In practice, preference attributes are highly correlated (e.g., 'prefers brevity' correlates with 'prefers bullet points over prose'). Under this factored approximation, the posterior update may be inconsistent: confirming 'prefers brevity' should increase the probability of correlated hypotheses, but the factored update leaves them unchanged. The proposal should either (a) acknowledge this as a stated approximation (factored posterior) in the algorithm description, or (b) briefly justify why correlations are low in the PersonalLLM hypothesis space (e.g., by reporting inter-hypothesis correlation on the dev split). This is a technical vulnerability that a Bayesian reviewer would raise.\", \"EIG terminology imprecision: Stage 3 states 'selects the hypothesis with maximum posterior entropy H(p(h_i)) — nearest to log 2' and also calls this 'EIG-based.' Maximum marginal entropy equals EIG only under the factored (independent) posterior assumption. Under a correlated posterior, maximizing joint EIG requires summing over hypotheses and is strictly different from marginal entropy maximization. Since the proposal uses a factored update, calling it 'EIG-based' is technically correct but only by virtue of the unstated independence assumption. Clarify in one sentence: 'Under the factored posterior approximation, maximizing marginal entropy H(p(h_i)) is equivalent to EIG-based selection.'\"]\nFeedback: Round 4 has resolved all three Round 3 issues cleanly: OPEN is now thoroughly cited and integrated into the BOED lineage narrative; the disconfirmation probe algorithm is precisely specified (EIG pool inclusion + soft minimum quota); and Stage 2a calibration analysis (Spearman ρ, τ selection on 50 dev users) directly addresses the warm-start prior vulnerability. The core idea is solid and publication-ready at EMNLP Findings level once the following targeted fixes are applied:\n\n**Fix 1 (Critical) — Replace non-existent model name throughout.** 'Qwen 3.5-7B-Instruct' does not exist in the Qwen3.5 family (which has 4B, 27B, and MoE variants only). Replace with 'Qwen2.5-7B-Instruct' (Qwen/Qwen2.5-7B-Instruct on HuggingFace — available, widely benchmarked) or 'Qwen3-8B' (Qwen/Qwen3-8B on HuggingFace). This affects every experimental description and the resource estimate; apply the substitution consistently.\n\n**Fix 2 (Moderate) — Cite AMPLe (arXiv 2411.00524, ACL 2025).** Add one paragraph in Section 2 (Related Work) under active preference learning: 'AMPLe (Oh et al., ACL 2025) uses Bayesian inference with modified posterior updates and active comparison-based query selection for multi-dimensional LLM personalization. FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary hypothesis confirmation (\"does this stylistic claim apply to you?\") rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe.' No ablation needed — citation and differentiation suffice.\n\n**Fix 3 (Minor) — Acknowledge hypothesis-independence assumption.** Add one sentence to Stage 3 after the Bayesian update equation: 'We apply a factored (independent) posterior approximation, updating each hypothesis probability independently; under this approximation, marginal entropy maximization is equivalent to EIG-based selection.' This closes both the EIG terminology issue and the independence assumption gap in one edit.\n\nAfter these three fixes, the proposal has no critical technical gaps, the venue deadline is correct, compute is within budget, and the MVP scope (PersonalLLM + 4 baselines + 1 ablation + Stage 2a calibration) is credibly executable in the 16-day window. Recommend one more targeted revision pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — BED-LLM prior characterization is factually wrong and would be caught by a reviewer who reads the paper. The proposal repeatedly says BED-LLM 'starts from cold uniform prior (no domain ranking, no user demonstrations).' However, the BED-LLM paper defines the initial prior as p_f(θ;h_t=∅) — the LLM's own predictive distribution over hypotheses given no history — which is an LM-generic prior (not uniform), analogous in spirit to OPEN's domain-generic feature importance ranking. Additionally, BED-LLM uses multiple-choice questions (not binary yes/no), because as the paper states, 'having a small space of single-token responses ensures that p_LLM provides meaningful uncertainty over outcomes.' The proposal must correct both: (a) replace 'cold uniform prior' with 'LM-generic prior, not conditioned on user demonstrations'; (b) note that FABEL uses binary yes/no confirmation (lower cognitive load) while BED-LLM uses multiple-choice. The novelty argument remains valid — FABEL's demo-conditioned prior is a real differentiator from BED-LLM's demo-agnostic LM prior — but the current phrasing is inaccurate.\", \"MINOR — Stage 2a calibration analysis is underspecified. The proposal describes 'Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy across 50 PersonalLLM dev users' but never operationalizes 'empirical hypothesis accuracy' for simulated users. In the PersonalLLM framework, simulated users are represented as weighted ensembles of reward models. The paper must specify: for each hypothesis h_i and each simulated user, ground truth accuracy = fraction of that user's reward-model-preferred responses that satisfy h_i (e.g., for 'prefers bullet points,' check what fraction of high-reward responses are bulleted). Without this operational definition, Stage 2a is unverifiable and a reviewer will ask exactly this question.\", \"MINOR — BED-LLM's application domain is described as 'item recommendation' throughout the proposal, but BED-LLM evaluates on both 20-Questions and preference elicitation via movie-preference multiple-choice questions — a general preference inference setting. While 'item recommendation' is partially correct, the more accurate framing is 'latent preference vector inference from sequential multiple-choice queries, without user demonstrations.' This distinction matters because FABEL's application to LLM response-style personalization (format, tone, structure) is a domain shift, not just a warm-start shift.\"]\nFeedback: Round 4 fixes have all been applied cleanly: Qwen2.5-7B-Instruct replaces the non-existent 'Qwen 3.5-7B-Instruct,' AMPLe is now cited and differentiated in cluster (3b), and the factored posterior approximation is explicitly acknowledged in Stage 3. The proposal is close to passing. Three targeted edits will get it there:\n\n**Fix 1 (Moderate, 1–2 paragraphs) — Correct the BED-LLM prior description.** Replace every instance of 'cold uniform prior' in the BED-LLM description with 'LM-generic prior (p_f(θ;∅): the LLM's unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations).' Add one clause noting that BED-LLM uses multiple-choice questions, not binary yes/no, making FABEL's binary format an additional differentiator. The revised differentiation argument: 'FABEL extends BED-LLM in three ways: (1) prior conditioned on this user's K demonstrations (vs. BED-LLM's demo-agnostic LM prior); (2) binary yes/no confirmation (vs. BED-LLM's multiple-choice format); (3) mandatory disconfirmation probes absent from all prior BOED-for-preference work.'\n\n**Fix 2 (Minor, 1 paragraph) — Operationalize Stage 2a ground truth.** In the Stage 2a description, add: 'For each simulated PersonalLLM dev user u and hypothesis h_i, empirical accuracy = fraction of u's top-quartile reward-model responses that satisfy h_i (assessed by prompting Qwen2.5-7B-Instruct to classify each response as satisfying or violating h_i, then comparing against the reward model's preference ordering via Kendall τ). This operationalization is fully automated using PersonalLLM's existing reward-model infrastructure without additional human labels.'\n\n**Fix 3 (Minor, 1 sentence) — Clarify BED-LLM domain.** Replace 'targets item recommendation' with 'targets latent preference vector inference via movie-preference multiple-choice queries' in the BED-LLM description. This sharpens the domain-shift argument: FABEL is the first to apply the OPEN→BED-LLM BOED lineage to LLM response-style personalization (format, tone, structure) from free-form demonstrations.\n\nWith these three fixes applied, the proposal has no remaining critical gaps. The combination of user-demonstration-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel, the MVP compute fits within the ≤200 H100-hour constraint, and the empirical design (warm vs. cold ablation, Stage 2a calibration, disconfirmation diagnostic) is appropriate for EMNLP Findings.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MINOR — TO-GATE related work description is inaccurate: the proposal states TO-GATE 'applies DPO to clarifying question quality, remaining in the open-ended, non-Bayesian regime,' but independent verification (arXiv 2506.02827 fetched) confirms TO-GATE uses trajectory-level DPO across the full multi-turn clarification dialogue generation pipeline — not just clarifying question quality in isolation. While the non-Bayesian characterization is correct, the narrow phrasing 'DPO to clarifying question quality' misrepresents the method and would be flagged by a TO-GATE-aware reviewer.\", \"MINOR — Disconfirmation probe generation mechanism underspecified: Stage 1 states that Qwen2.5-7B-Instruct generates K_neg=4–6 'hypotheses deliberately constructed to be easily falsifiable given the demonstrations,' but the proposal nowhere specifies the prompt or instructions used to elicit deliberately falsifiable probes as opposed to the model's default confirmatory behavior (which is precisely what arXiv 2604.02485 shows is the default). A reviewer will ask in rebuttal: 'How do you ensure the LLM generates probes that are genuinely falsifiable rather than merely low-confidence confirmatory hypotheses?' The generation mechanism must be concretely specified.\", \"MINOR — Stage 2a τ selection failure mode unspecified: the proposal selects τ as 'the smallest value such that the prior Spearman rank correlation with ground-truth held-out-demo accuracy exceeds 0.6,' but provides no fallback if no τ achieves ρ > 0.6 (i.e., if LLM log-likelihoods are uncorrelated with empirical accuracy for some hypothesis class). A reviewer will ask what happens in this case. The paper needs one sentence: e.g., 'If no τ achieves the threshold, we default to τ→∞ (uniform prior) and report this user as a calibration failure in diagnostic analysis.'\", \"MINOR — Human study statistical power and EMNLP Main claim in tension: the proposal simultaneously acknowledges the n≈20 study is 'underpowered for significance' and asserts it 'substantially strengthens the EMNLP Main case per reviewer guidance.' These claims are contradictory. An underpowered real-user study that cannot reach statistical significance does not meaningfully distinguish FABEL from a well-designed ablation — reviewers targeting EMNLP Main will note this. The claim should be hedged to 'provides a qualitative real-user signal and preliminary external validity evidence, not statistical confirmation.'\"]\nFeedback: All Round 5 issues are cleanly resolved and independently verified: BED-LLM is confirmed ICLR 2026 (OpenReview ID: qyylZMLYT8), its LM-generic prior p_f(θ;∅) is correctly described, its multiple-choice format is noted, and its domain (latent preference vector inference, not item recommendation) is now correct. Stage 2a ground-truth operationalization is adequately specified. Four minor issues remain:\n\n**Fix 1 (1 sentence, related work):** Replace the TO-GATE description with: 'TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior.' The current phrasing ('DPO to clarifying question quality') understates the scope and would be caught by a TO-GATE-aware reviewer.\n\n**Fix 2 (1 paragraph, Stage 1):** Specify the disconfirmation probe generation prompt explicitly. Example: 'We instruct the LLM: generate K_neg hypotheses that are plausibly true of some user but LIKELY VIOLATED by the provided writing samples—stylistic attributes the demonstrations actively disconfirm. Example: if all samples use numbered lists, generate the probe \"User avoids numbered lists.\"' Without this, the mechanism is not reproducible and the novelty claim (that probes are genuinely falsifiable, not just low-confidence) is unverifiable.\n\n**Fix 3 (1 sentence, Stage 2a):** Add: 'If no τ satisfies ρ > 0.6 on the dev split, we default to τ→∞ (uniform prior equivalent) and flag the failure in diagnostic analysis.' This closes the only remaining technical gap in the calibration procedure.\n\n**Fix 4 (1 sentence, human study description):** Replace 'substantially strengthens the EMNLP Main case' with 'provides a qualitative real-user signal and preliminary external validity evidence beyond simulated personas; the study is underpowered for statistical inference and results are reported descriptively.' This aligns the claim with the actual evidence and preempts the obvious reviewer objection.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE — Stage 2a circular self-evaluation: The Spearman ρ calibration analysis uses Qwen2.5-7B-Instruct both to (a) compute LLM log-likelihood scores score_i over demonstrations and (b) classify whether responses satisfy hypothesis h_i (for computing empirical accuracy). Since both quantities are derived from the same model, the correlation may reflect internal model consistency rather than genuine predictive validity over user preferences. Specifically, the model will tend to assign higher log-likelihoods to demonstration text that matches hypotheses it would also classify as satisfied—this is circular and could inflate ρ relative to its true value as a predictor of real user agreement. The paper should either: (a) acknowledge this as a stated limitation ('ρ is a model-consistency measure; real-user calibration is validated post-hoc via the Prolific study'), or (b) use a different model for the hypothesis satisfaction classification step (e.g., Llama 3.1-8B or a specialist NLI model) to break the circularity.\", \"MINOR — Human study framing residual overstatement: Despite correctly acknowledging the study is 'underpowered for statistical inference and results are reported descriptively,' the sentence continues 'which strengthens the EMNLP Main case relative to a purely simulated evaluation.' An underpowered descriptive study that cannot support statistical inference does not meaningfully strengthen the EMNLP Main case in the eyes of reviewing committees—it provides anecdotal, externally valid evidence but not a primary result. Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas but cannot substitute for a powered human study in Main review criteria.'\"]\nFeedback: Round 7 has cleanly resolved all four Round 6 issues: TO-GATE is correctly described as trajectory-level DPO, the disconfirmation probe prompt is explicitly specified with evidence-citing requirement, the τ→∞ fallback is added, and the human study is labeled underpowered. Independent verification confirms that arXiv 2602.15012 (the only unverified potential competitor) targets reasoning tasks with structured world model priors and does not overlap with FABEL's domain or mechanism. The core combination is genuinely novel and technically sound. Two targeted fixes are needed:\n\n**Fix 1 (Moderate, 2–3 sentences in Stage 2a): Break or acknowledge the circular self-evaluation.** The Spearman ρ calibration uses Qwen2.5-7B-Instruct for both log-likelihood scoring and hypothesis satisfaction classification — this creates an internal consistency artifact that may inflate ρ. Add: 'We note a circularity in this operationalization: the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and empirical accuracy labels, so ρ partly reflects model self-consistency rather than purely predictive validity over real user preferences. To bound this effect, we additionally report ρ using Llama-3.1-8B-Instruct as the hypothesis classifier, providing a cross-model calibration check.' Alternatively, acknowledge this limitation explicitly and defer cross-model validation to Phase 2.\n\n**Fix 2 (Minor, 1 clause): Remove the residual EMNLP Main overstatement.** Replace 'which strengthens the EMNLP Main case relative to a purely simulated evaluation' with 'which provides preliminary external validity evidence beyond simulated personas, reported descriptively.' This aligns with the already-correct statement that the study is underpowered.\n\nAfter these two fixes, the proposal has no remaining critical issues. The combination of demo-conditioned warm prior + EIG binary confirmation + disconfirmation probes is genuinely novel and appropriately scoped for EMNLP 2026 Findings. The MVP compute estimate (75h H100-equivalent) is confirmed within budget, and the PersonalLLM benchmark is publicly available.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:55:36.499Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:55:36.499Z",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-10T07:55:36.528Z_

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

## Idea under review (round 8/10)
{
  "title": "Demonstration-Grounded Warm-Start Hypothesis Elicitation for LLM Personalization via Binary Confirmation",
  "core_problem": "Personalizing LLMs to individual users requires efficient preference elicitation from few-shot demonstrations. Current methods exhibit three distinct failure modes: (1) Demonstration-grounded hypothesis methods (HyPerAlign) infer rich preference attributes from user examples but skip validation, risking hallucination and echo-chamber failure; (2) The BOED-for-preference-elicitation line—established by OPEN (arXiv 2403.05534, ACL 2024) and extended by BED-LLM (arXiv 2508.21184, ICLR 2026)—applies principled EIG-based adaptive questioning but initializes without user-specific demonstration-conditioned priors: OPEN uses LM-ranked feature importances as a domain-generic prior (not conditioned on any specific user's outputs); BED-LLM starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution over hypotheses, not conditioned on any specific user's demonstrations—which is also not informed by available user examples; both waste elicitation turns on hypotheses that available user demonstrations already resolve; (3) Iterative preference inference from writing samples (PROSE, ICML 2025) refines free-form preference descriptions with component-level verification but involves no user interaction and no formal Bayesian posterior—it cannot adaptively resolve ambiguous hypotheses that demonstrations alone are insufficient to distinguish. Additionally, arXiv 2604.02485 ('Failing to Falsify', April 2026) shows LLMs exhibit systematic confirmation bias in hypothesis testing (42% baseline success rate), meaning LLM-generated hypothesis sets may be preferentially confirmable rather than genuinely falsifiable, causing Bayesian posteriors to converge spuriously on echo-chamber preference profiles. No existing method combines user-demonstration-conditioned warm-start Bayesian priors, EIG-based binary confirmation, and explicit disconfirmation-probe auditing in the LLM response-style personalization domain.",
  "opportunity": "The BOED-for-preference-elicitation lineage was established by OPEN (arXiv 2403.05534, ACL 2024), which combined EIG-based query selection with LM feature extraction over pairwise item comparisons in content recommendation—but initializes from LM-ranked feature importances (a domain-generic warm start reflecting general knowledge about what features matter for news article preferences, not this user's actual examples). BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets with a Rao-Blackwellized EIG estimator and an LM-generic prior initialization p_f(θ;∅), evaluating on latent preference vector inference via movie-preference multiple-choice queries and 20-Questions, demonstrating that EIG-based sequential Bayesian elicitation substantially outperforms prompt-only baselines. Neither OPEN nor BED-LLM exploits K specific examples of a target user's actual outputs: their initializations duplicate information that demonstrations already encode, wasting early elicitation turns. AMPLe (arXiv 2411.00524, ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation, but also cold-starts from pairwise item comparisons rather than user demonstrations and lacks disconfirmation probes. HyPerAlign (arXiv 2505.00038, May 2025) showed demonstration-grounded hypotheses yield >90% win rates but explicitly omits user validation. PROSE (arXiv 2505.23815, ICML 2025) achieves 33% improvement over CIPHER on writing-style tasks via iterative preference refinement from demonstrations, but operates entirely without user interaction—it cannot distinguish two hypotheses with similar demonstration-level support, and provides no mechanism to surface or mitigate confirmation bias. The unaddressed gap is the warm-start interactive regime: when K demonstrations are available, initializing the Bayesian prior from user-specific demonstration-conditioned LLM likelihoods—calibrated via temperature scaling to avoid overconfident prior collapse—should dramatically reduce required elicitation turns compared to both OPEN and BED-LLM (testable claim), while the interactive EIG confirmation phase resolves the residual ambiguity that passive methods like PROSE cannot address (complementary claim). A second gap concerns confirmation bias: an elicitation system that does not deliberately seed disconfirmation probes in the hypothesis pool risks producing preference profiles that reflect what an LLM expects a user to prefer rather than what the user actually prefers—an echo-chamber failure mode that HyPerAlign acknowledges but does not address, and that PROSE's component-verification step partially mitigates without fully resolving.",
  "landscape": "The preference elicitation and personalization landscape includes eight relevant clusters. (1) Demonstration-grounded, no validation: HyPerAlign (arXiv 2505.00038, ICLR 2025 workshop) generates falsifiable-in-principle preference hypotheses from demonstrations and injects them as system prompts without user confirmation. (2) Iterative preference inference from writing samples, no interaction: PROSE (arXiv 2505.23815, ICML 2025, Aroca-Ouellette, Mackraz, Theobald, Metcalf; Apple ML Research) iteratively refines free-form preference descriptions from user writing samples via a generate→compare→update loop, then verifies preference components against held-out demonstrations with component-level scoring; achieves 33% improvement over CIPHER baseline on summarization and email writing tasks across Qwen2.5-7B/72B and GPT-4o variants; no user interaction beyond initial writing samples, no Bayesian posterior over hypotheses, no disconfirmation mechanism—the key differentiator from FABEL is that PROSE cannot adaptively resolve ambiguity beyond what demonstrations already encode and has no principled update when demonstrations are insufficient to distinguish competing hypotheses; must be included as a baseline (directly competitive with FABEL Stage 1) and explicitly differentiated. (3) The BOED-for-preference-elicitation lineage: OPEN (arXiv 2403.05534, ACL 2024, Handa, Gal, Pavlick, Goodman, Andreas, Tamkin, Li) established this line by combining EIG-based query selection with LM feature extraction for content recommendation—selects pairwise queries over binary feature vectors (|F|=10, e.g., 'discusses science') using a particle-filter Bayesian update with Bradley-Terry preference model; prior initialization is via LM-ranked feature importances (domain-generic: w_i = 1.2 − 0.12i for rank i), NOT conditioned on any specific user's demonstrations; evaluates NYT article recommendation (n=30 articles, ~40 Prolific users); outperforms LM-only and BOED-only baselines in user studies; no user-demonstration-conditioned warm start, no response-style personalization domain, no disconfirmation mechanism. BED-LLM (arXiv 2508.21184, ICLR 2026) extends OPEN to discrete language hypothesis sets: samples N=15 hypotheses per turn, selects questions via Rao-Blackwellized EIG estimator (~45–50 LLM calls/step), rejection-sampling Bayesian posterior update; starts from an LM-generic prior p_f(θ;∅)—the LLM's own unconditional distribution over hypotheses, not conditioned on any specific user's demonstrations (and notably over-collapsed toward a small number of hypothesis types per the paper); uses multiple-choice questions (a technical requirement: having a small space of single-token responses ensures p_LLM provides meaningful uncertainty over outcomes for EIG estimation); evaluates on latent preference vector inference via movie-preference multiple-choice queries and the 20-Questions game; no public code. Active Task Disambiguation (arXiv 2502.04485, ICLR 2025) similarly applies Bayesian experimental design for clarifying question selection on under-specified tasks. FABEL extends beyond all three works: (i) user-specific demonstration-conditioned warm start (K=5–10 demos from THIS user, vs. OPEN's domain-generic LM-ranked feature importances and BED-LLM's demo-agnostic LM-generic prior p_f(θ;∅)), (ii) temperature-scaled prior calibration to prevent overconfident prior collapse, (iii) binary yes/no natural-language hypothesis confirmation over free-form response-style attributes (vs. OPEN's pairwise item comparisons and BED-LLM's multiple-choice format—FABEL's binary format reduces cognitive load while remaining viable because hypothesis confirmation questions are naturally binary in ways that preference inference over open hypothesis spaces is not), (iv) mandatory disconfirmation probes in the EIG pool (absent from all prior BOED-for-preference work), (v) application to LLM response-style personalization (format, tone, structure)—a domain shift from BED-LLM's latent preference vector inference. (3b) Comparison-based active preference learning for LLM personalization: AMPLe (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) personalizes LLM outputs to implicit multi-dimensional preferences via pairwise comparison queries, a modified Bayesian posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection. AMPLe is directly adjacent to FABEL in the active Bayesian personalization space but differs in three critical ways: (1) AMPLe cold-starts from pairwise item comparisons rather than initializing from user demonstrations; (2) AMPLe asks 'which response do you prefer?' (item comparison) rather than 'does this stylistic hypothesis apply to you?' (hypothesis confirmation); (3) AMPLe includes no disconfirmation probe mechanism. AMPLe must be cited as an ACL 2025 active Bayesian personalization baseline; its comparison-based query design and FABEL's hypothesis-confirmation design represent complementary elicitation paradigms. (4) Generative open-ended elicitation: GATE (arXiv 2310.11589, ICLR 2025, Li, Tamkin, Goodman, Andreas) uses free-form LLM-generated questions in three domains; its binary yes/no variant reduces cognitive load but underperforms the open-ended variant because binary questions without a Bayesian posterior cannot adaptively narrow the hypothesis space—GATE's binary variant also does not ground questions in user demonstrations. (5) Trajectory-optimized clarification: TO-GATE (arXiv 2506.02827) applies trajectory-level DPO across the full multi-turn clarification dialogue, optimizing response quality conditioned on clarification history; it remains non-Bayesian and does not maintain explicit preference hypotheses or a posterior. (6) Bayesian-RL hybrid: PEBOL (arXiv 2405.00981, RecSys 2024) combines NLI-based preference beliefs with Thompson Sampling in recommendation. (7) Bayesian in-context conditioning from demonstrations (adjacent): Variational In-Context Reward Modeling / ICRM (arXiv 2602.08819, Feb 2026, Hong, Tang, Wang) casts reward modeling as amortized variational inference over a latent preference with a conjugate Beta prior conditioned on in-context preference demonstrations at test time without retraining—conceptually adjacent to FABEL's warm-start initialization from demonstrations but differs in three critical ways: domain (pairwise scalar reward modeling vs. interactive response-style personalization), hypothesis representation (continuous Beta prior on scalar rewards vs. discrete binary preference hypotheses), and interaction mode (passive in-context update vs. active EIG confirmation loop); no disconfirmation probes; acknowledged in related work to pre-empt warm-start novelty challenge. (8) Few-shot preference optimization: FSPO (arXiv 2502.19312, 2025) meta-learns personalization from few-shot preference data; deferred to Phase 2 due to meta-training infrastructure overhead. The specific combination absent from all prior work: user-specific demonstration-conditioned Bayesian prior initialization + temperature-scaled calibration + EIG-based binary yes/no confirmation + mandatory disconfirmation probes + application to LLM response-style personalization (format, tone, structure)—distinct from AMPLe's comparison-based cold-start design, OPEN's domain-generic warm start, BED-LLM's demo-agnostic LM-generic prior with multiple-choice format, and PROSE's non-interactive refinement.",
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
    "AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization (arXiv 2411.00524, ACL 2025, Oh, Lee, Ok; POSTECH; public code: github.com/ml-postech/AMPLe) — active Bayesian preference learning for LLM personalization; pairwise comparison queries over LLM responses, modified posterior update robust to noisy feedback, and generalized binary-search-inspired active query selection to minimize required comparisons; directly adjacent to FABEL's active Bayesian personalization setting; FABEL differs in three ways: (1) FABEL initializes a warm prior from user demonstrations rather than cold-starting from comparisons; (2) FABEL asks binary stylistic hypothesis confirmation rather than item pairwise comparisons; (3) FABEL includes mandatory disconfirmation probes absent from AMPLe; include as related work in landscape cluster (3b); include as Phase 2 baseline on LaMP tasks",
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
  "description": "Personalizing LLMs to individual users is hindered by three complementary failure modes: HyPerAlign generates demonstration-grounded preference hypotheses but skips user validation; the BOED-for-preference-elicitation line—established by OPEN (ACL 2024) and extended by BED-LLM (ICLR 2026)—applies principled EIG-based Bayesian elicitation but lacks user-specific demonstration-conditioned priors (OPEN uses domain-generic LM-ranked feature importances; BED-LLM uses an LM-generic prior p_f(θ;∅)—the LLM's own unconditional predictive distribution, not conditioned on any specific user's demonstrations); and PROSE (ICML 2025) iteratively refines free-form preference descriptions from writing samples but has no user interaction and no formal Bayesian posterior, leaving ambiguous hypotheses unresolved. AMPLe (ACL 2025) addresses multi-dimensional LLM personalization via comparison-based active Bayesian elicitation but also cold-starts from pairwise comparisons and lacks disconfirmation probes. We propose FABEL (Falsification-Aligned Binary Elicitation Loop), which extends the OPEN→BED-LLM BOED lineage by (1) initializing a temperature-scaled warm Bayesian prior p(h_i) ∝ exp(score_i / τ) from K=5–10 user-specific demonstrations—user-specific rather than domain-generic or demo-agnostic; (2) including K_neg=4–6 explicit disconfirmation probes in the EIG-ranked hypothesis pool, generated via a dedicated falsification prompt that requires citing demonstration-level evidence for each probe, making the probe design a prior-shaping device that ensures EIG always has access to genuinely falsifying evidence; (3) applying a soft minimum quota (⌈K_neg/3⌉ probes if ≥3 turns) to prevent warm-start overconfidence from silently suppressing falsifying questions; (4) applying a factored posterior approximation with EIG-based binary yes/no confirmation (vs. BED-LLM's multiple-choice format, which is required for reliable LLM uncertainty quantification but increases cognitive load) to resolve remaining uncertainty in 3–5 turns; and (5) explicitly acknowledging that under the factored (independent) posterior approximation, marginal entropy maximization is equivalent to EIG-based selection. Stage 2a includes a calibration analysis (Spearman ρ between LLM log-likelihoods and empirical hypothesis accuracy on 50 PersonalLLM dev users, where empirical accuracy is operationalized as the fraction of each simulated user's top-quartile reward-model responses satisfying each hypothesis) that validates the warm-start assumption and selects τ; if no τ achieves ρ > 0.6, the system defaults to a uniform prior and flags the calibration failure. Critically, Stage 2a also addresses a circularity in this operationalization—the same model (Qwen2.5-7B-Instruct) computes both log-likelihood scores and accuracy labels—by additionally reporting ρ using Llama-3.1-8B-Instruct as an independent hypothesis classifier (cross-model calibration check; arXiv 2601.20913); if cross-model ρ falls below 0.6 while same-model ρ exceeds it, the system defaults to the uniform prior, treating the discrepancy as evidence of self-consistency inflation. The EMNLP 2026 MVP targets Findings as the primary outcome, with an optional n≈20 Prolific human study (days 3–4, ~$100–200) that is underpowered for statistical inference and reported descriptively—providing preliminary external validity evidence beyond simulated personas, reported descriptively. The central testable claim: demonstration-grounded user-specific warm priors reduce required elicitation turns vs. both OPEN (domain-generic warm start) and BED-LLM (demo-agnostic LM prior) while achieving higher personalization win rates than non-interactive methods (PROSE, HyPerAlign). LaMP benchmarks, AMPLe/FSPO baselines, and full ablations are deferred to Phase 2.",
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
  "promptId": "3326bc49-bb7f-42d2-bc00-b73c1ab5eb55",
  "type": "user",
  "uuid": "ff39b1ed-204c-4418-ab5a-86c3da652056",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:55:36.524Z_

```json
{
  "parentUuid": "ff39b1ed-204c-4418-ab5a-86c3da652056",
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
  "uuid": "88daf2eb-cac8-4039-8609-8d5a6a68b3d3",
  "timestamp": "2026-05-10T07:55:36.524Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:55:36.524Z_

```json
{
  "parentUuid": "88daf2eb-cac8-4039-8609-8d5a6a68b3d3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fa1b516c-cff7-4b7f-966b-54a960a03c4b",
  "timestamp": "2026-05-10T07:55:36.524Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
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
  "leafUuid": "fa1b516c-cff7-4b7f-966b-54a960a03c4b",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstrate warm-start Bayesian preference elicitation for LLM personalization",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:56:28.873Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. This is Round 8 of 10 reviewing the FABEL (Falsification-Aligned Binary Elicitation Loop) paper idea. I need to independently verify claims and assess the current state of the proposal after 7 rounds of revisions.

Looking at Round 7's feedback, the reviewer identified two issues:
1. MODERATE — Stage 2a circular self-evaluation (using same model for both log-likelihood scoring and hypothesis classification)
2. MINOR — Human study framing residual overstatement

Looking at the Round 8 submission, let me check if these have been addressed:


The authors have directly acknowledged the circularity issue, noting that the same model computes both log-likelihood scores and accuracy labels, which means the correlation partly reflects model self-consistency rather than genuine predictive validity. They've cited relevant literature on LLM-as-judge bias and added a cross-model calibration check using a different model as a robustness measure to bound this effect.

For the human study, they're being transparent that the sample size limits statistical inference, so they're presenting results descriptively as qualitative evidence of real-user preferences and preliminary external validity beyond simulated evaluations.

Now I need to independently verify the key claims in this work through web search—checking whether the cited papers and benchmarks actually exist and are described accurately, including BED-LLM's acceptance at ICLR 2026, PROSE at ICML 2025, HyPerAlign, the "Failing to Falsify" paper, the PersonalLLM benchmark, and AMPLe.

I should also look for concurrent work in demo-conditioned Bayesian preference elicitation, warm-start priors for preference learning, and disconfirmation-based hypothesis validation to see if there's overlapping research.

On the technical side, the core contribution—combining demonstration-grounded hypothesis generation with expected information gain-based binary confirmation and mandatory disconfirmation probes—seems like a reasonable extension of Bayesian optimal experimental design for preference learning, with the main novelty being how it grounds the prior in demonstrations rather than using domain-generic or language-model-generic approaches.

Now I'm checking what issues might still exist after seven rounds of review. The BED-LLM paper's arXiv timestamp (2508.21184 for August 2025) is plausible for an ICLR 2026 acceptance, though I should verify this independently since the Round 3 reviewer already confirmed it was accepted.

The proposal also cites TO-GATE (arXiv 2506.02827 from June 2025) and "Failing to Falsify" (arXiv 2604.02485 from April 2026) as motivation for the disconfirmation probes approach.

Looking at the specifics, I'm noticing a couple of concerns. The BED-LLM reimplementation is time-boxed to 3-4 agent-days, but given that there's no public code and the Rao-Blackwellized EIG estimator requires roughly 45-50 LLM calls per step, this timeline feels tight—though the proposal does acknowledge this risk. I'm also wondering about the novelty of the warm-start demonstration component.

The core claim is that FABEL's innovation lies in using demo-conditioned Bayesian warm starts, but HyPerAlign already generates hypotheses from demonstrations. What FABEL adds is treating those demo-derived hypotheses as a warm prior rather than just a fixed prompt, then layering on EIG-based interactive confirmation. The temperature scaling to prevent prior collapse is a practical touch, but I'm questioning whether this distinction is substantial enough.

For EMNLP Findings, the MVP scope looks reasonable—PersonalLLM with 4 baselines, 1 backbone, 1 ablation, and a ~20-person Prolific study. The real question is whether the contribution feels significant enough for that venue.

The factored posterior approximation is bothering me though. If I'm treating each hypothesis independently, then the "EIG" is really just marginal entropy maximization—which is a major simplification compared to BED-LLM's approach. A reviewer will likely push back on this: if the posterior factors, why not just run independent binary hypothesis tests on each one? The connection to proper EIG gets shaky.

And there's the practical concern about reimplementing BED-LLM from scratch. The Rao-Blackwellized EIG estimator needs roughly 45-50 LLM calls per turn, which is complex to get right in just 3-4 agent-days.

Now I need to verify some key references—particularly whether arXiv 2508.21184 is actually accepted at ICLR 2026, check for any recent 2025-2026 work on demo-conditioned preference elicitation I might have missed, and confirm the PersonalLLM benchmark is publicly available. After seven rounds of revision, the proposal has tackled the venue issues, recharacterized BED-LLM properly, added PROSE, AMPLe, and OPEN to related work, incorporated disconfirmation probes with explicit prompting, and started Stage 2a calibration analysis.

The core question for Round 8 is whether the combination of techniques—demo-grounded hypothesis generation from HyPerAlign, EIG-based sequential confirmation from BED-LLM, disconfirmation probes motivated by recent work, and temperature-scaled priors from calibration literature—constitutes sufficient novelty for EMNLP Findings, or if it's just recombining existing methods with one novel element. I also need to assess whether the PersonalLLM benchmark actually validates the claimed benefits adequately.

There's a fundamental mismatch between what PersonalLLM measures and what FABEL needs to demonstrate: the benchmark evaluates win rates across candidate responses using reward model ensembles, but it doesn't capture sequential elicitation turns or the efficiency gains from warm-starting the prior. PersonalLLM's simulated users respond to written prompts via reward scores, not to hypothesis confirmation questions, so there's a gap between the evaluation framework and the core claim about reducing elicitation turns through Bayesian sequential design.

Actually, looking at the proposal more carefully, FABEL does address this by simulating hypothesis confirmation: it takes hypotheses like "User prefers bullet points," generates yes/no questions, then checks whether the simulated user's top-ranked responses (according to reward models) actually satisfy those hypotheses using a language model classifier. This creates an implicit ground truth for what the simulated user would answer to preference questions, bridging the gap between reward model scoring and interactive elicitation.

The methodology seems sound for demonstrating the concept, especially since PersonalLLM is purpose-built for simulating diverse user preferences through reward model ensembles. Now I need to identify what to focus on for Round 8 feedback—given seven prior revisions, I should look for remaining technical gaps, missing related work, feasibility issues, or novelty concerns. Let me search for recent papers on demonstration-conditioned Bayesian preference learning and verify whether BED-LLM was actually accepted to ICLR 2026.

I should also check what other warm-start approaches exist for preference elicitation and make sure PROSE is accurately characterized in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa1b516c-cff7-4b7f-966b-54a960a03c4b",
  "isSidechain": false,
  "requestId": "req_011CatXfqVJVmvSi6ERj6Fjk",
  "type": "assistant",
  "uuid": "b77f7d54-4295-4679-8f13-ce998c356ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JpUBHtLES4nVDoY1qeuH3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28371,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3876,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28371
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

_source line 9 · 2026-05-10T07:56:28.875Z_

I'll conduct independent verification of the key claims before issuing a verdict. Let me search for recent concurrent works and verify the references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b77f7d54-4295-4679-8f13-ce998c356ee5",
  "isSidechain": false,
  "requestId": "req_011CatXfqVJVmvSi6ERj6Fjk",
  "type": "assistant",
  "uuid": "71eab50c-76b5-4399-9527-d4829e5969e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JpUBHtLES4nVDoY1qeuH3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28371,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3876,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28371
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

_source line 10 · 2026-05-10T07:56:35.521Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019Mw9z3Ymhrdh2rwPowu9Z5`</summary>

```json
{
  "description": "Verify key FABEL paper references and search for concurrent works",
  "subagent_type": "Explore",
  "prompt": "I need you to verify several academic paper references and search for concurrent works for a paper review. Please do the following searches and report what you find:\n\n1. Search for \"BED-LLM ICLR 2026 Bayesian Experimental Design language hypotheses\" on arXiv and via web to confirm it exists and was accepted at ICLR 2026. The claimed arXiv ID is 2508.21184.\n\n2. Search for \"PROSE aligning LLMs predicting preferences user writing samples ICML 2025\" to verify this paper exists. Claimed arXiv: 2505.23815.\n\n3. Search for \"HyPerAlign interpretable personalized LLM alignment hypothesis generation 2025\" to verify arXiv 2505.00038.\n\n4. Search for \"Failing to Falsify LLM confirmation bias hypothesis testing 2026\" to verify arXiv 2604.02485 and its claim about 42% baseline success rate.\n\n5. Search for recent (2025-2026) works on \"demonstration-conditioned Bayesian preference elicitation\" or \"warm-start preference learning from demonstrations\" that might overlap with FABEL's core contribution.\n\n6. Search for \"AMPLe comparison active preference learning personalization ACL 2025 POSTECH\" to confirm arXiv 2411.00524.\n\n7. Search for any recent (late 2025 - early 2026) papers combining \"Bayesian elicitation\" with \"few-shot demonstrations\" or \"writing samples\" for LLM personalization.\n\nFor each search, try at least 2 different query formulations. Report what you find including paper titles, venues, and whether the characterizations in the proposal are accurate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71eab50c-76b5-4399-9527-d4829e5969e5",
  "isSidechain": false,
  "requestId": "req_011CatXfqVJVmvSi6ERj6Fjk",
  "type": "assistant",
  "uuid": "22b3f028-6185-44d8-b0d6-66087733e81f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JpUBHtLES4nVDoY1qeuH3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28371,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3876,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28371
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

_source line 11 · 2026-05-10T07:56:44.217Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017DC8Px1w91vuZ1Zj66Komp`</summary>

```json
{
  "description": "Search for competing methods and simulation evaluation gaps",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a paper (FABEL) about LLM personalization via Bayesian preference elicitation. I need you to search for potential issues and concurrent works. Please do:\n\n1. Search \"PersonalLLM benchmark ICLR 2025 namkoong simulated users reward models\" to verify this benchmark is publicly available and check how simulated users work in it.\n\n2. Search \"OPEN Bayesian preference elicitation language models ACL 2024 Handa\" to verify arXiv 2403.05534 and its domain (news article recommendation, not LLM response style).\n\n3. Search \"AMPLe active multi-dimensional preference learning LLM personalization\" on arXiv and Papers with Code to check if public code exists at github.com/ml-postech/AMPLe.\n\n4. Search for \"disconfirmation probe hypothesis testing LLM 2025 2026\" for any concurrent methods using explicit disconfirmation in preference learning.\n\n5. Search \"EIG binary hypothesis confirmation personalization 2025\" and \"Bayesian personalization demonstration warm start 2026\" to find any concurrent works that might undermine novelty.\n\n6. Search \"GATE eliciting human preferences language models ICLR 2025\" to verify arXiv 2310.11589 and confirm it has a binary question variant.\n\n7. Check \"ICRM variational in-context reward modeling 2026 Hong Tang Wang\" for arXiv 2602.08819 and whether it's accurately described as using Beta prior conditioned on preference demonstrations.\n\nFor each, use 2+ query variations and report findings concisely. Flag any discrepancies between the paper's claims and what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b3f028-6185-44d8-b0d6-66087733e81f",
  "isSidechain": false,
  "requestId": "req_011CatXfqVJVmvSi6ERj6Fjk",
  "type": "assistant",
  "uuid": "e4a3b2f0-cc32-4ebc-ae49-05e5365171c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JpUBHtLES4nVDoY1qeuH3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28371,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3876,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3876,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 28371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28371
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

_source line 12 · 2026-05-10T07:57:09.825Z_

<details><summary>↩ Tool result · `toolu_019Mw9z3Ymhrdh2rwPowu9Z5`</summary>

```text
## Summary of Academic Paper Reference Verification

I've conducted comprehensive searches for all the papers you requested. Here are my findings:

### 1. **BED-LLM (arXiv 2508.21184)**
**Status: CONFIRMED - ICLR 2026 acceptance**
- **Full Title**: "BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design"
- **Venue**: Published at ICLR 2026
- **arXiv ID**: 2508.21184 (posted August 28, 2025)
- **Description Accuracy**: The characterization is accurate but incomplete. While BED-LLM does use Bayesian Experimental Design, it's not specifically about "language hypotheses" but rather about general hypothesis testing and information gathering through iterative question selection maximizing expected information gain (EIG).
- **Key Contribution**: Sequential Bayesian experimental design for interactive information gathering with LLMs, with applications to user preference inference and the 20 Questions game.

### 2. **PROSE (arXiv 2505.23815)**
**Status: CONFIRMED - ICML 2025 acceptance**
- **Full Title**: "Aligning LLMs by Predicting Preferences from User Writing Samples"
- **Venue**: ICML 2025 (poster presentation)
- **arXiv ID**: 2505.23815
- **Description Accuracy**: Accurate. The paper does align LLMs by predicting preferences from writing samples through iterative refinement and verification.
- **Key Results**: 33% improvement over CIPHER baseline; works with multiple LLMs (Qwen2.5, GPT-mini, GPT-4o); evaluated on summarization and email writing tasks.

### 3. **HyPerAlign (arXiv 2505.00038)**
**Status: CONFIRMED - May 2025**
- **Full Title**: "HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation"
- **arXiv ID**: 2505.00038 (v2 submitted May 19, 2025)
- **Authors**: Cristina Garbacea and Chenhao Tan
- **Description Accuracy**: Accurate. The paper infers hypotheses about user communication strategies, personality, and writing style from few-shot examples, then uses these hypotheses for personalization.
- **Key Results**: Win rates >90% on authorship attribution; up to 70% improvement on deliberative alignment tasks.

### 4. **"Failing to Falsify" (arXiv 2604.02485)**
**Status: CONFIRMED - 2026 publication**
- **Full Title**: "Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models"
- **arXiv ID**: 2604.02485
- **Description Accuracy**: ACCURATE regarding the 42% baseline success rate. The paper states: "prompting LLMs with such instruction consistently decreases confirmation bias in LLMs, improving rule discovery rates from 42% to 56% on average."
- **Key Finding**: Confirmation bias in rule-discovery tasks; mitigation improves success from 42% to 56%.
- **Methods**: Psychologically-grounded interventions (Dual-Goal, Think-in-Opposites); distillation for internalization.

### 5. **Bayesian Elicitation + Few-Shot Demonstrations + Writing Samples**
**Status: MULTIPLE RELEVANT WORKS FOUND**
- **FSPO (arXiv 2502.19312)**: "Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users" - Frames reward modeling as meta-learning; 2-5 writing samples suffice for strong style imitation.
- **PEBOL (arXiv 2405.00981)**: "Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation" - Uses Thompson Sampling with NLI for preference beliefs.
- **BAL-PM (arXiv 2406.10023)**: "Deep Bayesian Active Learning for Preference Modeling in Large Language Models" - Published at NeurIPS 2024.
- **MAPLE (arXiv 2412.07207)**: Combines Bayesian active learning with LLM-guided preference learning.

### 6. **AMPLe (arXiv 2411.00524)**
**Status: CONFIRMED - ACL 2025 Main Conference**
- **Full Title**: "Comparison-based Active Preference Learning for Multi-dimensional Personalization"
- **Venue**: ACL 2025 (Main conference, long paper)
- **arXiv ID**: 2411.00524
- **Authors**: From POSTECH (Pohang University of Science and Technology) - Minhyeon Oh, Seungjoon Lee, Jungseul Ok
- **Description Accuracy**: Accurate. Uses comparison-based feedback with Bayesian inference and active query selection (generalized binary search).
- **Code**: Publicly available at https://github.com/ml-postech/AMPLe

### 7. **Recent Combined Works (2025-2026)**
**Multiple relevant papers found:**
- **Bayesian Elicitation with LLMs (2026)**: arXiv 2604.01896 - Focuses on model size vs. reasoning capability tradeoffs
- **APRICOT**: Active preference learning with constraint-aware LLM task planning
- **The Alignment Auditor (arXiv 2510.06096)**: Bayesian framework for verifying LLM objectives
- **Stayin' Aligned Over Time (arXiv 2605.04029)**: Longitudinal human-LLM alignment with behavioral data

All seven referenced papers exist and are accurately characterized. The field shows strong momentum in 2025-2026 on combining Bayesian active learning with few-shot demonstrations for LLM personalization, validating FABEL's positioning as a competitive contribution to this space.

Sources:
- [BED-LLM on arXiv](https://arxiv.org/abs/2508.21184)
- [BED-LLM on OpenReview](https://openreview.net/forum?id=qyylZMLYT8)
- [PROSE on OpenReview](https://openreview.net/forum?id=eUMGCipgtE)
- [PROSE on ICML](https://icml.cc/virtual/2025/poster/44582)
- [HyPerAlign on arXiv](https://arxiv.org/abs/2505.00038)
- [Failing to Falsify on arXiv](https://arxiv.org/abs/2604.02485)
- [AMPLe on ACL Anthology](https://aclanthology.org/2025.acl-long.1590/)
- [AMPLe on arXiv](https://arxiv.org/abs/2411.00524)
- [FSPO on arXiv](https://arxiv.org/abs/2502.19312)
- [PEBOL on arXiv](https://arxiv.org/abs/2405.00981)
- [BAL-PM on arXiv](https://arxiv.org/abs/2406.10023)
- [MAPLE Framework](https://arxiv.org/html/2412.07207)
- [The Alignment Auditor on arXiv](https://arxiv.org/html/2510.06096v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22b3f028-6185-44d8-b0d6-66087733e81f",
  "isSidechain": false,
  "promptId": "3326bc49-bb7f-42d2-bc00-b73c1ab5eb55",
  "type": "user",
  "uuid": "87ba1978-ce04-43c7-80a2-702f519e4adf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to verify several academic paper references and search for concurrent works for a paper review. Please do the following searches and report what you find:\n\n1. Search for \"BED-LLM ICLR 2026 Bayesian Experimental Design language hypotheses\" on arXiv and via web to confirm it exists and was accepted at ICLR 2026. The claimed arXiv ID is 2508.21184.\n\n2. Search for \"PROSE aligning LLMs predicting preferences user writing samples ICML 2025\" to verify this paper exists. Claimed arXiv: 2505.23815.\n\n3. Search for \"HyPerAlign interpretable personalized LLM alignment hypothesis generation 2025\" to verify arXiv 2505.00038.\n\n4. Search for \"Failing to Falsify LLM confirmation bias hypothesis testing 2026\" to verify arXiv 2604.02485 and its claim about 42% baseline success rate.\n\n5. Search for recent (2025-2026) works on \"demonstration-conditioned Bayesian preference elicitation\" or \"warm-start preference learning from demonstrations\" that might overlap with FABEL's core contribution.\n\n6. Search for \"AMPLe comparison active preference learning personalization ACL 2025 POSTECH\" to confirm arXiv 2411.00524.\n\n7. Search for any recent (late 2025 - early 2026) papers combining \"Bayesian elicitation\" with \"few-shot demonstrations\" or \"writing samples\" for LLM personalization.\n\nFor each search, try at least 2 different query formulations. Report what you find including paper titles, venues, and whether the characterizations in the proposal are accurate.",
    "agentId": "a2348000853898b09",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Academic Paper Reference Verification\n\nI've conducted comprehensive searches for all the papers you requested. Here are my findings:\n\n### 1. **BED-LLM (arXiv 2508.21184)**\n**Status: CONFIRMED - ICLR 2026 acceptance**\n- **Full Title**: \"BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design\"\n- **Venue**: Published at ICLR 2026\n- **arXiv ID**: 2508.21184 (posted August 28, 2025)\n- **Description Accuracy**: The characterization is accurate but incomplete. While BED-LLM does use Bayesian Experimental Design, it's not specifically about \"language hypotheses\" but rather about general hypothesis testing and information gathering through iterative question selection maximizing expected information gain (EIG).\n- **Key Contribution**: Sequential Bayesian experimental design for interactive information gathering with LLMs, with applications to user preference inference and the 20 Questions game.\n\n### 2. **PROSE (arXiv 2505.23815)**\n**Status: CONFIRMED - ICML 2025 acceptance**\n- **Full Title**: \"Aligning LLMs by Predicting Preferences from User Writing Samples\"\n- **Venue**: ICML 2025 (poster presentation)\n- **arXiv ID**: 2505.23815\n- **Description Accuracy**: Accurate. The paper does align LLMs by predicting preferences from writing samples through iterative refinement and verification.\n- **Key Results**: 33% improvement over CIPHER baseline; works with multiple LLMs (Qwen2.5, GPT-mini, GPT-4o); evaluated on summarization and email writing tasks.\n\n### 3. **HyPerAlign (arXiv 2505.00038)**\n**Status: CONFIRMED - May 2025**\n- **Full Title**: \"HyPerAlign: Interpretable Personalized LLM Alignment via Hypothesis Generation\"\n- **arXiv ID**: 2505.00038 (v2 submitted May 19, 2025)\n- **Authors**: Cristina Garbacea and Chenhao Tan\n- **Description Accuracy**: Accurate. The paper infers hypotheses about user communication strategies, personality, and writing style from few-shot examples, then uses these hypotheses for personalization.\n- **Key Results**: Win rates >90% on authorship attribution; up to 70% improvement on deliberative alignment tasks.\n\n### 4. **\"Failing to Falsify\" (arXiv 2604.02485)**\n**Status: CONFIRMED - 2026 publication**\n- **Full Title**: \"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models\"\n- **arXiv ID**: 2604.02485\n- **Description Accuracy**: ACCURATE regarding the 42% baseline success rate. The paper states: \"prompting LLMs with such instruction consistently decreases confirmation bias in LLMs, improving rule discovery rates from 42% to 56% on average.\"\n- **Key Finding**: Confirmation bias in rule-discovery tasks; mitigation improves success from 42% to 56%.\n- **Methods**: Psychologically-grounded interventions (Dual-Goal, Think-in-Opposites); distillation for internalization.\n\n### 5. **Bayesian Elicitation + Few-Shot Demonstrations + Writing Samples**\n**Status: MULTIPLE RELEVANT WORKS FOUND**\n- **FSPO (arXiv 2502.19312)**: \"Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users\" - Frames reward modeling as meta-learning; 2-5 writing samples suffice for strong style imitation.\n- **PEBOL (arXiv 2405.00981)**: \"Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation\" - Uses Thompson Sampling with NLI for preference beliefs.\n- **BAL-PM (arXiv 2406.10023)**: \"Deep Bayesian Active Learning for Preference Modeling in Large Language Models\" - Published at NeurIPS 2024.\n- **MAPLE (arXiv 2412.07207)**: Combines Bayesian active learning with LLM-guided preference learning.\n\n### 6. **AMPLe (arXiv 2411.00524)**\n**Status: CONFIRMED - ACL 2025 Main Conference**\n- **Full Title**: \"Comparison-based Active Preference Learning for Multi-dimensional Personalization\"\n- **Venue**: ACL 2025 (Main conference, long paper)\n- **arXiv ID**: 2411.00524\n- **Authors**: From POSTECH (Pohang University of Science and Technology) - Minhyeon Oh, Seungjoon Lee, Jungseul Ok\n- **Description Accuracy**: Accurate. Uses comparison-based feedback with Bayesian inference and active query selection (generalized binary search).\n- **Code**: Publicly available at https://github.com/ml-postech/AMPLe\n\n### 7. **Recent Combined Works (2025-2026)**\n**Multiple relevant papers found:**\n- **Bayesian Elicitation with LLMs (2026)**: arXiv 2604.01896 - Focuses on model size vs. reasoning capability tradeoffs\n- **APRICOT**: Active preference learning with constraint-aware LLM task planning\n- **The Alignment Auditor (arXiv 2510.06096)**: Bayesian framework for verifying LLM objectives\n- **Stayin' Aligned Over Time (arXiv 2605.04029)**: Longitudinal human-LLM alignment with behavioral data\n\nAll seven referenced papers exist and are accurately characterized. The field shows strong momentum in 2025-2026 on combining Bayesian active learning with few-shot demonstrations for LLM personalization, validating FABEL's positioning as a competitive contribution to this space.\n\nSources:\n- [BED-LLM on arXiv](https://arxiv.org/abs/2508.21184)\n- [BED-LLM on OpenReview](https://openreview.net/forum?id=qyylZMLYT8)\n- [PROSE on OpenReview](https://openreview.net/forum?id=eUMGCipgtE)\n- [PROSE on ICML](https://icml.cc/virtual/2025/poster/44582)\n- [HyPerAlign on arXiv](https://arxiv.org/abs/2505.00038)\n- [Failing to Falsify on arXiv](https://arxiv.org/abs/2604.02485)\n- [AMPLe on ACL Anthology](https://aclanthology.org/2025.acl-long.1590/)\n- [AMPLe on arXiv](https://arxiv.org/abs/2411.00524)\n- [FSPO on arXiv](https://arxiv.org/abs/2502.19312)\n- [PEBOL on arXiv](https://arxiv.org/abs/2405.00981)\n- [BAL-PM on arXiv](https://arxiv.org/abs/2406.10023)\n- [MAPLE Framework](https://arxiv.org/html/2412.07207)\n- [The Alignment Auditor on arXiv](https://arxiv.org/html/2510.06096v1)"
      }
    ],
    "totalDurationMs": 34299,
    "totalTokens": 32828,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 14873,
      "cache_read_input_tokens": 16155,
      "output_tokens": 1793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1793,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 14873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14873,
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
  "sourceToolAssistantUUID": "22b3f028-6185-44d8-b0d6-66087733e81f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
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
  "leafUuid": "87ba1978-ce04-43c7-80a2-702f519e4adf",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstrate warm-start Bayesian preference elicitation for LLM personalization",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Tool result

_source line 15 · 2026-05-10T07:57:44.952Z_

<details><summary>↩ Tool result · `toolu_017DC8Px1w91vuZ1Zj66Komp`</summary>

```text
Based on my comprehensive search, here are my findings organized by search query:

## Summary of Findings

### 1. **PersonalLLM Benchmark (ICLR 2025, Namkoong)**
**Status: VERIFIED - Publicly Available**
- The benchmark is published and publicly available at ICLR 2025
- **Simulated Users Approach**: The paper uses **Dirichlet-weighted mixtures of 10 pre-trained reward models** to simulate a large user base with diverse preferences, NOT just generating simulated personas. The dataset includes 10,402 prompts with 8 LLM responses each.
- Public dataset available on Hugging Face (namkoong-lab/PersonalLLM)
- Paper: [Published at ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf)

### 2. **OPEN - Bayesian Preference Elicitation (arXiv 2403.05534, Handa et al.)**
**Status: VERIFIED - Correct Paper, BUT Domain Claim Needs Clarification**
- **Discrepancy Found**: The paper is titled "Bayesian Preference Elicitation with Language Models," NOT focused on news article recommendation
- **Actual Domain**: The paper addresses **general preference learning and alignment of AI systems to user interests**. While the search results mention a separate paper on "Generative News Recommendation" (2403.03424), OPEN (2403.05534) is fundamentally about using Bayesian Optimal Experimental Design (BOED) to elicit preferences via LMs
- Uses pairwise comparison queries translated to natural language by LMs
- Authors: Kunal Handa, Yarin Gal, Ellie Pavlick, Noah Goodman, Jacob Andreas, Alex Tamkin, Belinda Z. Li
- Paper: [arXiv 2403.05534](https://arxiv.org/abs/2403.05534)

### 3. **AMPLe - Active Multi-dimensional Preference Learning**
**Status: VERIFIED - Public Code Available**
- GitHub repository confirmed at [github.com/ml-postech/AMPLe](https://github.com/ml-postech/AMPLe)
- Published at ACL 2025 Main (Long papers)
- Uses modified Bayesian posterior updates and generalized binary search for active query selection
- Authors: Minhyeon Oh, Seungjoon Lee, Jungseul Ok
- Paper: [arXiv 2411.00524](https://arxiv.org/abs/2411.00524), [ACL Anthology](https://aclanthology.org/2025.acl-long.1590/)

### 4. **Disconfirmation Probe / Hypothesis Testing (2025-2026)**
**Status: NO DIRECT CONCURRENT WORK FOUND**
- No papers explicitly using "disconfirmation probe" in preference learning context were found in web search
- Found general work on hypothesis testing for LLM behavior, but not specifically disconfirmation-based preference elicitation
- Active learning with LLMs in 2026 exists, but no disconfirmation-specific method identified

### 5. **EIG + Binary Hypothesis Confirmation + Warm Start Personalization**
**Status: PARTIALLY FOUND - Limited Concurrent Work**
- EIG (Expected Information Gain) has been studied in hypothesis testing contexts, but no specific 2025-2026 paper explicitly combining EIG + binary hypothesis confirmation for personalization was found
- Warm-start personalization research exists (e.g., Pep framework reaching 77-87% oracle performance with 3-5x fewer interactions), but not specifically framed as "Bayesian personalization with demonstrations"
- General finding: Warm-start architectures separate cold-start (Bayesian priors) from warm personalization (fine-tuned models)

### 6. **GATE (Generative Active Task Elicitation) - ICLR 2025**
**Status: VERIFIED - GATE Confirmed**
- Published at ICLR 2025
- arXiv: [2310.11589](https://arxiv.org/abs/2310.11589)
- **Important Finding**: GATE uses **free-form, open-ended questions**, NOT binary questions
- The paper is authored by Belinda Z. Li (MIT CSAIL) and others
- In three domains (email validation, content recommendation, moral reasoning), GATE outperforms persona prompting and example-based elicitation
- **Discrepancy**: The paper does not mention a "binary question variant" in search results; GATE focuses on generative, open-ended interactions

### 7. **ICRM - In-Context Reward Modeling (arXiv 2602.08819)**
**Status: VERIFIED - Accurate Description**
- **Correctly Described**: Uses variational inference with a **conjugate Beta prior on Bradley-Terry model**, conditioned on preference demonstrations
- Two-headed regressor decouples preference mean (μ) from confidence factor (τ)
- Strong results: 63.7% → 95.6% accuracy on Focus subset with more demonstrations (1 to 8)
- Paper: [arXiv 2602.08819](https://arxiv.org/abs/2602.08819)
- **Status Note**: Currently available on arXiv; submission status to ICLR 2026 was unclear from search results

## Key Discrepancies Flagged

1. **OPEN (2403.05534)**: Paper description in FABEL claims focus on "news article recommendation" but the paper is actually about general preference learning via BOED—not domain-specific to news
2. **GATE (2310.11589)**: Claims about "binary question variant" not confirmed; GATE features free-form, open-ended questioning rather than binary choices
3. **Disconfirmation Methods**: No concurrent work found using explicit disconfirmation probing for preference learning (this may be a novelty of FABEL)
4. **EIG + Warm Start Personalization**: No specific 2025-2026 concurrent work found combining these approaches for LLM personalization

## Sources
- [PersonalLLM ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf)
- [PersonalLLM Dataset HuggingFace](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)
- [OPEN arXiv 2403.05534](https://arxiv.org/abs/2403.05534)
- [AMPLe GitHub](https://github.com/ml-postech/AMPLe)
- [AMPLe arXiv 2411.00524](https://arxiv.org/abs/2411.00524)
- [GATE ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf)
- [GATE arXiv 2310.11589](https://arxiv.org/abs/2310.11589)
- [ICRM arXiv 2602.08819](https://arxiv.org/abs/2602.08819)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4a3b2f0-cc32-4ebc-ae49-05e5365171c8",
  "isSidechain": false,
  "promptId": "3326bc49-bb7f-42d2-bc00-b73c1ab5eb55",
  "type": "user",
  "uuid": "57833035-84a2-4a07-b957-0a372e7fece1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper (FABEL) about LLM personalization via Bayesian preference elicitation. I need you to search for potential issues and concurrent works. Please do:\n\n1. Search \"PersonalLLM benchmark ICLR 2025 namkoong simulated users reward models\" to verify this benchmark is publicly available and check how simulated users work in it.\n\n2. Search \"OPEN Bayesian preference elicitation language models ACL 2024 Handa\" to verify arXiv 2403.05534 and its domain (news article recommendation, not LLM response style).\n\n3. Search \"AMPLe active multi-dimensional preference learning LLM personalization\" on arXiv and Papers with Code to check if public code exists at github.com/ml-postech/AMPLe.\n\n4. Search for \"disconfirmation probe hypothesis testing LLM 2025 2026\" for any concurrent methods using explicit disconfirmation in preference learning.\n\n5. Search \"EIG binary hypothesis confirmation personalization 2025\" and \"Bayesian personalization demonstration warm start 2026\" to find any concurrent works that might undermine novelty.\n\n6. Search \"GATE eliciting human preferences language models ICLR 2025\" to verify arXiv 2310.11589 and confirm it has a binary question variant.\n\n7. Check \"ICRM variational in-context reward modeling 2026 Hong Tang Wang\" for arXiv 2602.08819 and whether it's accurately described as using Beta prior conditioned on preference demonstrations.\n\nFor each, use 2+ query variations and report findings concisely. Flag any discrepancies between the paper's claims and what you find.",
    "agentId": "ae33b5f6112b5d3d6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, here are my findings organized by search query:\n\n## Summary of Findings\n\n### 1. **PersonalLLM Benchmark (ICLR 2025, Namkoong)**\n**Status: VERIFIED - Publicly Available**\n- The benchmark is published and publicly available at ICLR 2025\n- **Simulated Users Approach**: The paper uses **Dirichlet-weighted mixtures of 10 pre-trained reward models** to simulate a large user base with diverse preferences, NOT just generating simulated personas. The dataset includes 10,402 prompts with 8 LLM responses each.\n- Public dataset available on Hugging Face (namkoong-lab/PersonalLLM)\n- Paper: [Published at ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf)\n\n### 2. **OPEN - Bayesian Preference Elicitation (arXiv 2403.05534, Handa et al.)**\n**Status: VERIFIED - Correct Paper, BUT Domain Claim Needs Clarification**\n- **Discrepancy Found**: The paper is titled \"Bayesian Preference Elicitation with Language Models,\" NOT focused on news article recommendation\n- **Actual Domain**: The paper addresses **general preference learning and alignment of AI systems to user interests**. While the search results mention a separate paper on \"Generative News Recommendation\" (2403.03424), OPEN (2403.05534) is fundamentally about using Bayesian Optimal Experimental Design (BOED) to elicit preferences via LMs\n- Uses pairwise comparison queries translated to natural language by LMs\n- Authors: Kunal Handa, Yarin Gal, Ellie Pavlick, Noah Goodman, Jacob Andreas, Alex Tamkin, Belinda Z. Li\n- Paper: [arXiv 2403.05534](https://arxiv.org/abs/2403.05534)\n\n### 3. **AMPLe - Active Multi-dimensional Preference Learning**\n**Status: VERIFIED - Public Code Available**\n- GitHub repository confirmed at [github.com/ml-postech/AMPLe](https://github.com/ml-postech/AMPLe)\n- Published at ACL 2025 Main (Long papers)\n- Uses modified Bayesian posterior updates and generalized binary search for active query selection\n- Authors: Minhyeon Oh, Seungjoon Lee, Jungseul Ok\n- Paper: [arXiv 2411.00524](https://arxiv.org/abs/2411.00524), [ACL Anthology](https://aclanthology.org/2025.acl-long.1590/)\n\n### 4. **Disconfirmation Probe / Hypothesis Testing (2025-2026)**\n**Status: NO DIRECT CONCURRENT WORK FOUND**\n- No papers explicitly using \"disconfirmation probe\" in preference learning context were found in web search\n- Found general work on hypothesis testing for LLM behavior, but not specifically disconfirmation-based preference elicitation\n- Active learning with LLMs in 2026 exists, but no disconfirmation-specific method identified\n\n### 5. **EIG + Binary Hypothesis Confirmation + Warm Start Personalization**\n**Status: PARTIALLY FOUND - Limited Concurrent Work**\n- EIG (Expected Information Gain) has been studied in hypothesis testing contexts, but no specific 2025-2026 paper explicitly combining EIG + binary hypothesis confirmation for personalization was found\n- Warm-start personalization research exists (e.g., Pep framework reaching 77-87% oracle performance with 3-5x fewer interactions), but not specifically framed as \"Bayesian personalization with demonstrations\"\n- General finding: Warm-start architectures separate cold-start (Bayesian priors) from warm personalization (fine-tuned models)\n\n### 6. **GATE (Generative Active Task Elicitation) - ICLR 2025**\n**Status: VERIFIED - GATE Confirmed**\n- Published at ICLR 2025\n- arXiv: [2310.11589](https://arxiv.org/abs/2310.11589)\n- **Important Finding**: GATE uses **free-form, open-ended questions**, NOT binary questions\n- The paper is authored by Belinda Z. Li (MIT CSAIL) and others\n- In three domains (email validation, content recommendation, moral reasoning), GATE outperforms persona prompting and example-based elicitation\n- **Discrepancy**: The paper does not mention a \"binary question variant\" in search results; GATE focuses on generative, open-ended interactions\n\n### 7. **ICRM - In-Context Reward Modeling (arXiv 2602.08819)**\n**Status: VERIFIED - Accurate Description**\n- **Correctly Described**: Uses variational inference with a **conjugate Beta prior on Bradley-Terry model**, conditioned on preference demonstrations\n- Two-headed regressor decouples preference mean (μ) from confidence factor (τ)\n- Strong results: 63.7% → 95.6% accuracy on Focus subset with more demonstrations (1 to 8)\n- Paper: [arXiv 2602.08819](https://arxiv.org/abs/2602.08819)\n- **Status Note**: Currently available on arXiv; submission status to ICLR 2026 was unclear from search results\n\n## Key Discrepancies Flagged\n\n1. **OPEN (2403.05534)**: Paper description in FABEL claims focus on \"news article recommendation\" but the paper is actually about general preference learning via BOED—not domain-specific to news\n2. **GATE (2310.11589)**: Claims about \"binary question variant\" not confirmed; GATE features free-form, open-ended questioning rather than binary choices\n3. **Disconfirmation Methods**: No concurrent work found using explicit disconfirmation probing for preference learning (this may be a novelty of FABEL)\n4. **EIG + Warm Start Personalization**: No specific 2025-2026 concurrent work found combining these approaches for LLM personalization\n\n## Sources\n- [PersonalLLM ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/a730abbcd6cf4a371ca9545db5922442-Paper-Conference.pdf)\n- [PersonalLLM Dataset HuggingFace](https://huggingface.co/datasets/namkoong-lab/PersonalLLM)\n- [OPEN arXiv 2403.05534](https://arxiv.org/abs/2403.05534)\n- [AMPLe GitHub](https://github.com/ml-postech/AMPLe)\n- [AMPLe arXiv 2411.00524](https://arxiv.org/abs/2411.00524)\n- [GATE ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9867d5a22653ce98b02595061e40f12-Paper-Conference.pdf)\n- [GATE arXiv 2310.11589](https://arxiv.org/abs/2310.11589)\n- [ICRM arXiv 2602.08819](https://arxiv.org/abs/2602.08819)"
      }
    ],
    "totalDurationMs": 60731,
    "totalTokens": 35174,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1653,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 29782,
      "output_tokens": 1794,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1653,
          "output_tokens": 1794,
          "cache_read_input_tokens": 29782,
          "cache_creation_input_tokens": 1945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1945,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "e4a3b2f0-cc32-4ebc-ae49-05e5365171c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T08:00:41.115Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the findings from my searches and formulate a careful assessment.

**Key findings:**

1. **BED-LLM (arXiv 2508.21184, ICLR 2026)**: CONFIRMED. The paper exists and is accurately characterized. ✓

2. **PROSE (arXiv 2505.23815, ICML 2025)**: CONFIRMED. Accurate description. ✓

3. **HyPerAlign (arXiv 2505.00038)**: CONFIRMED. Win rates >90% confirmed. ✓


4. **"Failing to Falsify" (arXiv 2604.02485)**: CONFIRMED. The baseline and mitigation performance metrics check out. ✓

5. **AMPLe (arXiv 2411.00524, ACL 2025)**: CONFIRMED. Public code is available. ✓

6. **PersonalLLM (ICLR 2025)**: CONFIRMED. The model is accessible on HuggingFace. ✓

7. **OPEN (arXiv 2403.05534)**: I'm finding a discrepancy here—one source indicates the paper isn't actually about news article recommendation, which contradicts what I initially stated.

Looking back at the search results more carefully, OPEN does include a news recommendation evaluation on NYT articles, so that's not the issue. The real problem is that FABEL claims OPEN has domain-generic feature importance rankings specific to the NYT domain, which seems contradictory if OPEN is meant to be general-purpose. I need to figure out whether those feature rankings are actually domain-specific or if they're being mischaracterized.

Now I'm noticing another inconsistency with GATE—the FABEL proposal references a "GATE binary" variant with specific characteristics, but the search results don't show this variant being mentioned. I should check whether this is actually described in the GATE paper or if it's a variant FABEL created themselves. The agent likely just skimmed the paper without catching that detail. Now I need to focus on the substantive technical gaps that have persisted through seven rounds of revision. BAL-PM from NeurIPS 2024 is a significant omission—it directly addresses Bayesian active learning for preference modeling in LLMs, which overlaps substantially with FABEL's approach, and the proposal should cite it as related work. I'm also seeing MAPLE mentioned but the reference appears cut off, so I need to examine what that work contributes and whether it's another gap in the literature review.

The characterization of OPEN's domain scope is worth clarifying too—if OPEN actually uses general language model features rather than news-specific ones, then calling it a "news article recommendation" system might be oversimplifying its applicability. On the novelty front, the warm start from user demonstrations and the disconfirmation probe mechanism do represent genuine contributions beyond prior work like BED-LLM, though I should assess how substantial these advances really are relative to the overall contribution.

The factored posterior approximation is a significant limitation though—it essentially reduces the Bayesian experimental design down to selecting the most uncertain hypothesis, which is a fairly straightforward uncertainty-based selection strategy rather than true expected information gain. The EIG framing is technically sound but masks a considerable simplification of the Bayesian machinery.

For feasibility, the core components check out: PersonalLLM and Qwen2.5-7B-Instruct are both accessible, the computational budget of 75h H100-equivalent is reasonable, and while reimplementing BED-LLM carries some risk, it's manageable within the timeline constraints.

The proposal is well-articulated at this point and the algorithm is clearly specified with concrete baselines, though EMNLP Findings is probably the realistic venue given the incremental nature of the contribution. I should flag a couple of potentially relevant papers that aren't cited—BAL-PM from NeurIPS 2024 on Bayesian active learning for LLM preference modeling seems directly related, and there's also MAPLE that got cut off, both of which could represent gaps in the related work.

For the Round 8 verdict, the core question is whether there are unfixed critical issues or just minor ones that don't undermine the contribution. The BAL-PM omission is worth investigating more carefully since it's a recent NeurIPS paper in the same space, though the factored posterior's reduction to uncertainty sampling and the cross-model calibration overhead both seem manageable as-is. PS 2024, arXiv 2406.10023). If this paper applies Bayesian active learning to preference modeling in LLMs, it could be directly competitive. However:
- Does it use user demonstrations? Unclear.
- Does it use EIG-based query selection? Unclear.
- Is it in the response-style personalization domain? Unclear.

Without reading the paper, I can't be sure how closely it overlaps with FABEL. It might be more focused on preference data collection/annotation rather than user-facing personalization.

Similarly, MAPLE (arXiv 2412.07207) - without reading it, I can't be sure of the overlap.

Given that these are potential uncited relevant works that could affect the novelty claim, I should flag them as issues for the generator to investigate and address.

Now I'm examining some technical concerns. The PersonalLLM simulation uses response frequency as a proxy for preference confirmation, but this might not accurately capture how users would explicitly answer questions about subtle style preferences. The factored posterior approximation could also be problematic since preference attributes are often correlated, potentially leading to redundant questions about related attributes. And there's the question of whether binary yes/no questions truly offer lower cognitive load compared to BED-LLM's multiple-choice approach.

After reviewing everything, the core approach is sound and novel, all cited papers check out, and the proposal addresses the Round 7 feedback. The compute budget is reasonable at 75 hours of H100-equivalent time. But I need to flag those potentially uncited papers as a concern for novelty verification.

The most pressing question is whether BAL-PM from NeurIPS 2024 is actually competitive work here. It sounds like it could be about active learning for preference modeling in LLMs, which might overlap with FABEL's approach, but without seeing the full paper I can't determine if it's about RLHF/reward model training versus user-facing personalization. That's the key distinction that would determine if it's a critical gap in the related work.

MAPLE also looks potentially relevant given its focus on Bayesian active learning combined with LLM-guided preference learning from December 2024, so both of these could be meaningful omissions depending on their actual scope.

Overall, I'm settling on a novelty score of 3.5 out of 5 since the core contribution feels incremental—the factored posterior simplifies EIG to basic uncertainty sampling—though the demo-conditioned warm start does add something meaningful. Feasibility is solid at 4 out of 5 with the main risk being the BED-LLM reimplementation. The paper's clarity has improved significantly through these rounds to a 4 out of 5, and impact-wise this feels like EMNLP Findings material at 3.5 out of 5.

That puts me at roughly 3.75 overall, which falls short of the 4.0 threshold, so my verdict is to request revisions. The key issues I need to flag are the two potentially uncited papers, and more importantly, the risk that reviewers familiar with Bayesian experimental design will push back on how much the EIG framing is doing here when the factored posterior essentially reduces it to uncertainty-based selection. Let me reconsider whether that characterization is actually fair though—the factored posterior plus entropy maximization does equal EIG under the independence assumption, which is mathematically sound, but I should think through what BED-LLM is actually doing differently.

BED-LLM uses a Blackwellized EIG estimator that computes the full joint EIG rather than relying on the factored approximation, which means FABEL's approach is theoretically weaker from an information-theoretic standpoint. That said, the proposal already acknowledges this trade-off explicitly, framing it as a practical choice: the factored approximation drops the computational cost from O(N²) down to O(N) for N hypotheses. A reviewer might still ask why not just use the proper joint estimator, but the efficiency argument is legitimate and worth emphasizing. I should also verify that the core EMNLP Findings requirements are actually satisfied—the method novelty comes from combining demo-conditioned warm priors with disconfirmation probes, which does feel like a novel combination, and I need to check whether the empirical validation is solid.

Looking at my scoring breakdown, I'm settling on a novelty score around 3.5 because while the warm-start from demonstrations is genuinely novel in this context and the disconfirmation probe design is creative, the factored EIG approach is simpler than initially claimed. Feasibility looks solid at 4.0, and the main risk I see is whether BAL-PM and MAPLE turn out to be directly competitive works that should have been cited—if they're not, the proposal probably clears the bar.

My average across all dimensions lands at 3.875, just shy of the 4.0 threshold, which points toward a revise verdict. But I'm realizing this is Round 8 of 10, so the paper needs to be nearly there already, and the core issue really hinges on whether those two papers actually overlap with this work or not.

BAL-PM from NeurIPS 2024 could be about Bayesian active learning for preference modeling in LLMs, but without seeing it, I can't tell if it's addressing the same interactive preference discovery problem or if it's focused on traditional reward model training instead. MAPLE is similarly opaque without the full details. I should flag BAL-PM as potentially relevant work that needs investigation, but I can't definitively say it's a gap without more information.

On the EIG-based framing concern—actually, the proposal already addresses this by noting that under the factored posterior approximation, maximizing marginal entropy reduces to uncertainty sampling. So that's not a new issue to raise.

The more substantive question for this round is whether the "disconfirmation probe" mechanism is sufficiently specified. The proposal describes generating K_neg hypotheses that are plausibly true for some users but actively violated by the samples, but I'm wondering if the prompt engineering here is robust enough or if there are edge cases where the model might struggle to generate genuinely disconfirming attributes. , cite the specific demonstration evidence that falsifies it.'

This prompt asks the LLM to generate hypotheses that are VIOLATED by the demonstrations - but wait, this means these are negative examples. If a user provides 10 writing samples and the LLM generates "User avoids numbered lists" as a disconfirmation probe (because the samples use numbered lists), then:
1. When this probe is presented to the user: "Do you prefer to avoid numbered lists?" 
2. The user would say "no" (they use numbered lists, so they don't avoid them)
3. This would update the posterior for this probe to "false"

This is correct behavior. But here's a subtlety: the probe is "easily falsifiable given the demonstrations" - meaning the demonstrations already tell us this probe is false. Why waste an elicitation turn asking about it?

The proposal's answer is: "if H_neg probes are never selected (prior already confidently classifies them as false), this is evidence of good prior calibration." But if the demonstrations clearly falsify these probes, the warm-start prior should already assign low probability to them, meaning they'll rarely be selected by EIG since they have low entropy. So the disconfirmation probes would rarely or never be asked, making the "soft minimum quota" necessary to ensure at least some are asked.

The tension here is that if the warm start already handles these falsified probes, what's the actual value of including them? The proposal suggests that even when they're not selected, their presence in the hypothesis pool shapes how we understand the prior structure itself. But this raises a fair question: if the mandatory disconfirmation mechanism almost never triggers because EIG already avoids these low-entropy probes, then the whole mechanism might be solving a problem that doesn't really exist.

I'm noticing I keep going back and forth on this. Let me look at what the proposal actually says about how disconfirmation probes are handled...

The key insight is that including H_neg in the EIG pool prevents a structural bias toward confirmatory hypotheses—without it, the algorithm would naturally converge toward echo-chamber behavior. The soft quota acts as a safeguard against warm-start overconfidence silently suppressing falsifying questions. The "disconfirmation selection rate" diagnostic would show when this happens.

But there's still a tension: the EIG criterion selects based on entropy, which might not align with selecting disconfirmation probes when the warm-start prior is already confident.

If the prior assigns H_neg low probability (0.05-0.10), their entropy is only ~0.29 bits compared to the maximum of 1 bit, so EIG won't pick them. But if the prior is miscalibrated and assigns them higher probability (0.3-0.5), their entropy increases and EIG might select them—which would then reveal the miscalibration. So the probes function primarily as calibration diagnostics rather than a guaranteed falsification mechanism, which is a useful reframing but slightly softer than the "falsification-aligned" framing suggests.

After seven rounds of revision, the proposal feels solid. The main lingering concerns are whether BAL-PM from NeurIPS 2024 should be cited (moderate concern), whether the disconfirmation probes truly add value beyond the warm-start prior (they mostly help when the prior is miscalibrated, which is a subtle design tension but not fatal), and whether EMNLP Findings is the right venue (the human study with ~20 participants is underpowered for Main Track but reasonable for Findings). All the Round 7 issues have been resolved cleanly, the key papers check out, and there don't appear to be any critical blockers remaining.

I'm leaning toward "revise" rather than "pass" because the average score sits around 3.8, below the 4.0 threshold, and there's still the possibility of uncited relevant work like BAL-PM. The novelty is genuine but feels incremental—the demo-conditioned warm prior and disconfirmation probes are each novel, but their combination doesn't quite reach the bar for acceptance without revision. My scores settle at 3.5 for novelty, 4 for feasibility, 4.5 for clarity, and 3.5 for impact, averaging to 3.875.

Actually, reconsidering the novelty—the system does combine four distinct elements that no single paper has brought together: the demo-conditioned warm Bayesian prior, EIG-based binary confirmation, disconfirmation probes in the EIG pool, and temperature-scaled calibration. That's genuinely novel as a complete system. But the factored posterior essentially reduces EIG to uncertainty sampling, which feels like a significant simplification, and the demo-conditioned prior, while novel here, is a fairly natural extension that other teams might independently arrive at. I'll stick with 3.5 for novelty—it's solid work, but the incremental nature is appropriate for conference-level contribution.

Now looking at the verdict: there are three main issues to address. First, I need to investigate whether BAL-PM from NeurIPS 2024 and MAPLE are properly cited—those are recent papers that could be directly relevant. Second, there's a real tension in the disconfirmation probe mechanism: when the warm start works well, the H_neg probes end up with low entropy and won't get selected by EIG, which means the "falsification-aligned" framing becomes more of a fallback mechanism than a core feature. Though actually, the proposal does acknowledge this—it notes that if H_neg probes are never selected, that's evidence of good calibration. So the mechanism is already addressed, but the naming might be misleading since these probes function more as a calibration diagnostic than a guaranteed falsification strategy.

I've been iterating on this for seven rounds though, so re-litigating the framing at this point probably isn't productive. The genuinely new issues for this round are the two potentially uncited papers—BAL-PM and MAPLE. They're moderate severity since they might not directly overlap with FABEL's approach. Let me focus on those and verify whether BAL-PM is actually competitive work by looking more closely at what it does.

BAL-PM appears to be about efficient annotation of preference pairs for reward model training in the RLHF pipeline, which is different from FABEL's user-facing preference elicitation during deployment. That said, without reading the full paper I can't be completely certain about the overlap, so I should flag it as a potential gap that needs checking. For MAPLE, I'll do the same. My final verdict will be "revise" with these two papers as the primary remaining issues—if they don't actually compete with FABEL, the proposal should be in good shape.

Actually, I need to step back and be more decisive here. This is round 8 of 10, and the proposal has already been thoroughly revised through 7 previous rounds. The core contributions are solid—clear method, adequate baselines, empirical validation, correct venue targeting, and within compute budget. The only real concerns are these two potentially uncited papers, which may or may not actually overlap with the work. Given that BAL-PM and MAPLE represent a moderate concern at best, and everything else checks out, I should probably issue a pass rather than another revise cycle.

Looking at the scoring: if novelty lands at 4.0 with feasibility at 4, clarity at 4.5, and impact at 3.5, that averages to exactly 4.0—right at the threshold. The disconfirmation probe design is genuinely creative, and the factored posterior simplification of EIG, while somewhat incremental, still represents a meaningful contribution. I'm going to score novelty at 4 and move forward with a pass. With Clarity at 4.5 and Impact at 3.5, that brings the average down to 3.875, which falls below the 4.0 threshold—so this warrants a revise decision. The core issues are the potentially uncited BAL-PM and MAPLE papers, which represent genuine novelty gaps I need to flag. I'm also noticing the self-consistency check they added in Round 8 for Stage 2a—using a cross-model calibration with Llama-3.1-8B-Instruct to validate the warm-start assumption if ρ stays above 0.6—which is a reasonable safeguard but doesn't resolve the citation concerns.

The human study framing is now properly positioned as qualitative evidence rather than a rigorous validation, and the evaluation methodology raises a question about whether PersonalLLM's reward model ensemble can reliably simulate actual user binary responses.

I'm realizing the simulation treats contextual preferences as binary classifications, which might oversimplify how real users would respond to nuanced questions. But this is a limitation of the benchmark itself, not something FABEL introduces—PersonalLLM is an established benchmark, so all methods face this constraint.

My final assessment: **revise** with two specific concerns about potentially uncited competitive works (BAL-PM and MAPLE). The core proposal is sound and nearly ready.

Scoring this at 3.875 overall—novelty and impact around 3.5, feasibility at 4.0, clarity at 4.5.

Now I need to flag those two uncited papers and double-check whether OPEN's evaluation scope actually aligns with how FABEL frames it. The OPEN paper describes general preference learning via Bayesian optimization, but FABEL references it as evaluating NYT article recommendations specifically—I should verify if that's an accurate characterization or if there's a mismatch in how the prior work is being represented. The features do sound like news article features, so if OPEN evaluates on NYT recommendation, that aligns with what FABEL describes. I'm not entirely certain whether OPEN's primary evaluation is news-specific or more general—the second agent suggested it's broader—but given that Round 3 reviewers flagged OPEN as a key missing citation and Round 4 now includes it with detailed characterization, earlier reviewers probably would've caught any major factual errors. I'll treat this as a minor concern rather than something critical.

So my verdict is to revise, with two potentially uncited papers (BAL-PM from NeurIPS 2024 and MAPLE from 2412.07207) as the main issues, plus a minor note about the OPEN domain description accuracy.

Now I'm reconsidering whether BAL-PM and MAPLE are truly competitive works or just adjacent ones. BAL-PM focuses on preference data annotation efficiency through active learning for reward model training, which is more about the data collection pipeline than user-facing preference discovery like FABEL does. That distinction matters for whether it's a direct competitor.

MAPLE combines Bayesian active learning with LLM-guided preference learning, but without seeing the full paper, it's hard to assess if it's another annotation efficiency tool or something more directly comparable. I should flag both for the generator to investigate and either cite with clear differentiation or explain why they fall outside the scope.

I'm also thinking through whether the "disconfirmation probe as calibration diagnostic" concern I raised earlier is actually a real issue or a design feature. When the warm start works correctly, the negative probes have low entropy and won't get selected by the EIG mechanism anyway—so the falsification-aligned behavior is really just a fallback that only activates when something goes wrong. The proposal actually acknowledges this explicitly.

That said, it does mean the "F" in FABEL is somewhat of a misnomer. The method is fundamentally about calibration diagnostics rather than true falsification, which is worth noting as a minor framing issue.

For the second issue, I should clarify that the disconfirmation probes work as a calibration check—when the prior is well-calibrated, H_neg probes rarely get selected because they have low entropy. The actual falsification mechanism is the soft quota enforcing a minimum number of negative probes, not the EIG selection itself. The "Falsification-Aligned" label should be more precise about this distinction.

On the OPEN paper, I need to verify whether it's actually a narrow news recommendation study or if it's framed more broadly, and whether the domain characterization in FABEL accurately captures what OPEN does.

For the feedback, I'm looking at three concrete next steps: checking whether BAL-PM and MAPLE apply Bayesian active learning to LLM personalization rather than just annotation efficiency, adding a sentence to Stage 3 that explains how disconfirmation probes serve as a calibration diagnostic when the prior is well-calibrated, and clarifying that the soft quota is what guarantees the falsification mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57833035-84a2-4a07-b957-0a372e7fece1",
  "isSidechain": false,
  "requestId": "req_011CatXqHz16ikpZsqjDZ92f",
  "type": "assistant",
  "uuid": "7b3ca080-e847-4657-94a1-782abbb6aae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012ph8qkR55ixV7CVWEZcLfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 40002,
      "output_tokens": 10469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10469,
          "cache_read_input_tokens": 40002,
          "cache_creation_input_tokens": 7513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7513
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

_source line 17 · 2026-05-10T08:00:46.903Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RSvdjU3zLu7N2oesZeb3BL`</summary>

```json
{
  "description": "Check BAL-PM and MAPLE papers for FABEL overlap assessment",
  "subagent_type": "Explore",
  "prompt": "I need to check two specific papers to see if they compete with a paper about demo-conditioned Bayesian preference elicitation for LLM personalization (FABEL). FABEL combines: (1) user demonstration-conditioned Bayesian warm priors, (2) EIG-based binary hypothesis confirmation, (3) explicit disconfirmation probes, for LLM response-style personalization.\n\n1. Look up \"BAL-PM arXiv 2406.10023 NeurIPS 2024 deep Bayesian active learning preference modeling LLM\" and read the abstract carefully. Does it:\n   - Focus on user-facing interactive preference discovery? OR\n   - Focus on efficient annotation/data collection for reward model training?\n   Report the paper's title, abstract, and key contribution accurately.\n\n2. Look up \"MAPLE arXiv 2412.07207 Bayesian active learning LLM preference 2024\" and read the abstract. What problem does it solve and does it overlap with user-facing LLM personalization via hypothesis confirmation?\n\n3. Also check \"Bayesian preference learning warm start demonstration LLM 2025 2026\" for any other papers combining warm-start Bayesian priors with user demonstrations for preference elicitation.\n\n4. Fetch https://arxiv.org/abs/2406.10023 to read the abstract directly.\n\nReport what you find - specifically whether either paper applies to user-facing personalization (competing with FABEL) vs. RLHF/annotation efficiency (not competing)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3ca080-e847-4657-94a1-782abbb6aae2",
  "isSidechain": false,
  "requestId": "req_011CatXqHz16ikpZsqjDZ92f",
  "type": "assistant",
  "uuid": "c3f40db9-7d3f-4c48-9dca-df146acc52a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012ph8qkR55ixV7CVWEZcLfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 40002,
      "output_tokens": 10469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10469,
          "cache_read_input_tokens": 40002,
          "cache_creation_input_tokens": 7513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7513
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
  "leafUuid": "c3f40db9-7d3f-4c48-9dca-df146acc52a8",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstrate warm-start Bayesian preference elicitation for LLM personalization",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Tool result

_source line 20 · 2026-05-10T08:02:36.666Z_

<details><summary>↩ Tool result · `toolu_01RSvdjU3zLu7N2oesZeb3BL`</summary>

```text
Perfect. Now let me compile my findings. Based on all the research I've gathered, here's my comprehensive report:

## Summary: Competitive Analysis for FABEL

I've conducted a thorough search of the recent literature on Bayesian preference learning for LLMs. Here are my findings:

---

### **1. BAL-PM (arXiv 2406.10023) - "Deep Bayesian Active Learning for Preference Modeling in Large Language Models"**

**Status: NOT a direct competitor to FABEL**

**Key Details:**
- **Title:** Deep Bayesian Active Learning for Preference Modeling in Large Language Models
- **Published:** NeurIPS 2024 (arXiv June 2024)
- **Focus:** REWARD MODEL TRAINING EFFICIENCY, not user-facing personalization
- **Main Problem:** Reducing annotation costs for preference labeling in reward model training
- **Key Innovation:** BAL-PM targets points of high epistemic uncertainty while maximizing prompt distribution entropy, achieving 33-68% fewer required preference labels
- **Core Use Case:** Training data collection efficiency for RLHF pipelines

**Does NOT compete with FABEL because:** BAL-PM focuses on efficient annotation for backend reward model training, not interactive user-facing preference elicitation for LLM response personalization. It has no user demonstration conditioning or response-style customization component.

---

### **2. MAPLE (arXiv 2412.07207) - "MAPLE: A Framework for Active Preference Learning Guided by Large Language Models"**

**Status: PARTIAL overlap - touches user-facing preference learning but different scope**

**Key Details:**
- **Title:** MAPLE: A Framework for Active Preference Learning Guided by Large Language Models
- **Published:** AAAI 2025 AI Alignment Track (arXiv December 2024)
- **Focus:** USER-FACING interactive preference learning (makes queries more interpretable and answerable)
- **Main Problem:** High computational burden, excessive human annotation demands, lack of interpretability
- **Key Innovation:** Uses LLM to model preference function distributions conditioned on natural language feedback + pairwise trajectory rankings; language-conditioned active query selection
- **Core Use Case:** General preference learning for alignment, with human interpretability

**Competitive Overlap with FABEL:**
- MAPLE does address user-facing interactive preference discovery through hypothesis-space exploration
- However, MAPLE is broader (trajectory ranking, NL feedback) rather than focused on LLM response-style personalization via demonstration-conditioned warm priors
- MAPLE doesn't emphasize user demonstrations as Bayesian warm priors specifically for personalization

**Different enough that:** MAPLE's focus on general alignment and trajectory-based preferences doesn't directly target the FABEL niche of response-style personalization via demo-conditioned warm starts.

---

### **3. APRICOT (arXiv 2410.19656) - "APRICOT: Active Preference Learning and Constraint-Aware Task Planning with LLMs"**

**Status: Tangentially related - different domain (robotics)**

**Key Details:**
- **Title:** APRICOT: Active Preference Learning and Constraint-Aware Task Planning with LLMs
- **Published:** NeurIPS 2024 (arXiv October 2024)
- **Focus:** Interactive preference learning FROM USER DEMONSTRATIONS for constrained robotic tasks (e.g., refrigerator organization)
- **Key Innovation:** Combines LLM-based Bayesian active preference learning with task planning; resolves ambiguity in interpreting user actions
- **Core Use Case:** Robot task organization with geometric constraints

**Does NOT directly compete with FABEL because:** While APRICOT uses user demonstrations + Bayesian active learning, its domain is robotic task planning, not LLM response-style personalization.

---

### **4. AMPLe (arXiv 2411.00524) - "Comparison-based Active Preference Learning for Multi-dimensional Personalization"**

**Status: User-facing personalization, but different query mechanism**

**Key Details:**
- **Title:** Comparison-based Active Preference Learning for Multi-dimensional Personalization
- **Published:** ACL 2025 Main (arXiv November 2024)
- **Focus:** USER-FACING multi-dimensional LLM response personalization
- **Main Problem:** Learning implicit user preferences efficiently with robust posterior updates
- **Key Innovation:** Modified Bayesian posterior update to mitigate estimation bias; active query selection via generalized binary search to minimize required comparisons
- **Core Use Case:** Personalizing LLM response styles across multiple dimensions

**Competitive Overlap with FABEL:**
- AMPLe also targets interactive LLM personalization to user preferences
- Uses Bayesian inference for preference learning
- Employs active query selection to minimize user burden

**Key Difference:** AMPLe uses pairwise comparisons as queries; doesn't explicitly use user demonstrations as warm priors or EIG-based hypothesis confirmation probes.

---

### **5. AdaptFuse (arXiv 2604.03925) - "AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference"**

**Status: Sequential preference learning, not demonstration-conditioned**

**Key Details:**
- **Focus:** Training-free sequential preference learning via externalized Bayesian inference
- **Key Innovation:** Symbolic module maintains Bayesian posterior over discrete hypothesis set; frozen LLM provides semantic reasoning via entropy-adaptive fusion
- **Approach:** Maintains hypothesis confirmations through symbolic Bayesian updates (not via demonstrations)
- **Core Use Case:** Recommendation/personalization without fine-tuning

**Does NOT directly compete with FABEL because:** Doesn't use user demonstrations as warm priors; focuses on symbolic hypothesis confirmation rather than demo-conditioned Bayesian initialization.

---

### **6. In-Context Bayesian Reward Modeling (arXiv 2602.08819) - "Bayesian Preference Learning for Test-Time Steerable Reward Models"**

**Status: Test-time reward model adaptation, not user-facing personalization**

**Key Details:**
- **Title:** Bayesian Preference Learning for Test-Time Steerable Reward Models
- **Innovation:** Variational In-Context Reward Modeling (ICRM) uses in-context preference demonstrations with Beta priors for test-time reward model adaptation
- **Uses:** In-context demonstrations to condition warm priors (technically similar to FABEL's approach!)
- **Core Use Case:** Making reward models flexible at inference time for multi-objective alignment

**Does NOT compete with FABEL because:** Focuses on reward model inference-time flexibility, not on interactive user-facing response-style personalization via preference elicitation.

---

### **Conclusion:**

**Direct Competitors to FABEL:**
- **MAPLE** - Partial overlap (user-facing preference learning via active queries, but broader scope)
- **AMPLe** - Closest competitor (interactive LLM personalization with Bayesian active learning, but uses pairwise comparisons not demo-conditioned warm priors)

**Not Competitors (Different Focus Areas):**
- **BAL-PM** → RLHF/reward model training efficiency (backend, not user-facing)
- **APRICOT** → Robotic task planning with preference learning (different domain)
- **AdaptFuse** → Sequential symbolic hypothesis confirmation (no demonstrations)
- **In-Context Reward Models** → Test-time reward model flexibility (not user personalization)

**Unique Aspects of FABEL:**
FABEL appears to be novel in its specific combination of: (1) user demonstrations as Bayesian warm priors, (2) EIG-based binary hypothesis confirmation, (3) explicit disconfirmation probes, applied specifically to LLM response-style personalization. While other papers address pieces of this puzzle, the particular integration for demo-conditioned interactive personalization is not clearly replicated in the literature I searched.

---

Sources:
- [BAL-PM: Deep Bayesian Active Learning for Preference Modeling in Large Language Models](https://arxiv.org/abs/2406.10023)
- [MAPLE: A Framework for Active Preference Learning Guided by Large Language Models](https://arxiv.org/abs/2412.07207)
- [APRICOT: Active Preference Learning and Constraint-Aware Task Planning with LLMs](https://arxiv.org/abs/2410.19656)
- [AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization](https://arxiv.org/abs/2411.00524)
- [AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference](https://arxiv.org/abs/2604.03925)
- [Bayesian Preference Learning for Test-Time Steerable Reward Models](https://arxiv.org/abs/2602.08819)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3f40db9-7d3f-4c48-9dca-df146acc52a8",
  "isSidechain": false,
  "promptId": "3326bc49-bb7f-42d2-bc00-b73c1ab5eb55",
  "type": "user",
  "uuid": "3d28a61e-8591-4f31-9aa2-869df75e7a77",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to check two specific papers to see if they compete with a paper about demo-conditioned Bayesian preference elicitation for LLM personalization (FABEL). FABEL combines: (1) user demonstration-conditioned Bayesian warm priors, (2) EIG-based binary hypothesis confirmation, (3) explicit disconfirmation probes, for LLM response-style personalization.\n\n1. Look up \"BAL-PM arXiv 2406.10023 NeurIPS 2024 deep Bayesian active learning preference modeling LLM\" and read the abstract carefully. Does it:\n   - Focus on user-facing interactive preference discovery? OR\n   - Focus on efficient annotation/data collection for reward model training?\n   Report the paper's title, abstract, and key contribution accurately.\n\n2. Look up \"MAPLE arXiv 2412.07207 Bayesian active learning LLM preference 2024\" and read the abstract. What problem does it solve and does it overlap with user-facing LLM personalization via hypothesis confirmation?\n\n3. Also check \"Bayesian preference learning warm start demonstration LLM 2025 2026\" for any other papers combining warm-start Bayesian priors with user demonstrations for preference elicitation.\n\n4. Fetch https://arxiv.org/abs/2406.10023 to read the abstract directly.\n\nReport what you find - specifically whether either paper applies to user-facing personalization (competing with FABEL) vs. RLHF/annotation efficiency (not competing).",
    "agentId": "a3b38a82d53ef12ed",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now let me compile my findings. Based on all the research I've gathered, here's my comprehensive report:\n\n## Summary: Competitive Analysis for FABEL\n\nI've conducted a thorough search of the recent literature on Bayesian preference learning for LLMs. Here are my findings:\n\n---\n\n### **1. BAL-PM (arXiv 2406.10023) - \"Deep Bayesian Active Learning for Preference Modeling in Large Language Models\"**\n\n**Status: NOT a direct competitor to FABEL**\n\n**Key Details:**\n- **Title:** Deep Bayesian Active Learning for Preference Modeling in Large Language Models\n- **Published:** NeurIPS 2024 (arXiv June 2024)\n- **Focus:** REWARD MODEL TRAINING EFFICIENCY, not user-facing personalization\n- **Main Problem:** Reducing annotation costs for preference labeling in reward model training\n- **Key Innovation:** BAL-PM targets points of high epistemic uncertainty while maximizing prompt distribution entropy, achieving 33-68% fewer required preference labels\n- **Core Use Case:** Training data collection efficiency for RLHF pipelines\n\n**Does NOT compete with FABEL because:** BAL-PM focuses on efficient annotation for backend reward model training, not interactive user-facing preference elicitation for LLM response personalization. It has no user demonstration conditioning or response-style customization component.\n\n---\n\n### **2. MAPLE (arXiv 2412.07207) - \"MAPLE: A Framework for Active Preference Learning Guided by Large Language Models\"**\n\n**Status: PARTIAL overlap - touches user-facing preference learning but different scope**\n\n**Key Details:**\n- **Title:** MAPLE: A Framework for Active Preference Learning Guided by Large Language Models\n- **Published:** AAAI 2025 AI Alignment Track (arXiv December 2024)\n- **Focus:** USER-FACING interactive preference learning (makes queries more interpretable and answerable)\n- **Main Problem:** High computational burden, excessive human annotation demands, lack of interpretability\n- **Key Innovation:** Uses LLM to model preference function distributions conditioned on natural language feedback + pairwise trajectory rankings; language-conditioned active query selection\n- **Core Use Case:** General preference learning for alignment, with human interpretability\n\n**Competitive Overlap with FABEL:**\n- MAPLE does address user-facing interactive preference discovery through hypothesis-space exploration\n- However, MAPLE is broader (trajectory ranking, NL feedback) rather than focused on LLM response-style personalization via demonstration-conditioned warm priors\n- MAPLE doesn't emphasize user demonstrations as Bayesian warm priors specifically for personalization\n\n**Different enough that:** MAPLE's focus on general alignment and trajectory-based preferences doesn't directly target the FABEL niche of response-style personalization via demo-conditioned warm starts.\n\n---\n\n### **3. APRICOT (arXiv 2410.19656) - \"APRICOT: Active Preference Learning and Constraint-Aware Task Planning with LLMs\"**\n\n**Status: Tangentially related - different domain (robotics)**\n\n**Key Details:**\n- **Title:** APRICOT: Active Preference Learning and Constraint-Aware Task Planning with LLMs\n- **Published:** NeurIPS 2024 (arXiv October 2024)\n- **Focus:** Interactive preference learning FROM USER DEMONSTRATIONS for constrained robotic tasks (e.g., refrigerator organization)\n- **Key Innovation:** Combines LLM-based Bayesian active preference learning with task planning; resolves ambiguity in interpreting user actions\n- **Core Use Case:** Robot task organization with geometric constraints\n\n**Does NOT directly compete with FABEL because:** While APRICOT uses user demonstrations + Bayesian active learning, its domain is robotic task planning, not LLM response-style personalization.\n\n---\n\n### **4. AMPLe (arXiv 2411.00524) - \"Comparison-based Active Preference Learning for Multi-dimensional Personalization\"**\n\n**Status: User-facing personalization, but different query mechanism**\n\n**Key Details:**\n- **Title:** Comparison-based Active Preference Learning for Multi-dimensional Personalization\n- **Published:** ACL 2025 Main (arXiv November 2024)\n- **Focus:** USER-FACING multi-dimensional LLM response personalization\n- **Main Problem:** Learning implicit user preferences efficiently with robust posterior updates\n- **Key Innovation:** Modified Bayesian posterior update to mitigate estimation bias; active query selection via generalized binary search to minimize required comparisons\n- **Core Use Case:** Personalizing LLM response styles across multiple dimensions\n\n**Competitive Overlap with FABEL:**\n- AMPLe also targets interactive LLM personalization to user preferences\n- Uses Bayesian inference for preference learning\n- Employs active query selection to minimize user burden\n\n**Key Difference:** AMPLe uses pairwise comparisons as queries; doesn't explicitly use user demonstrations as warm priors or EIG-based hypothesis confirmation probes.\n\n---\n\n### **5. AdaptFuse (arXiv 2604.03925) - \"AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference\"**\n\n**Status: Sequential preference learning, not demonstration-conditioned**\n\n**Key Details:**\n- **Focus:** Training-free sequential preference learning via externalized Bayesian inference\n- **Key Innovation:** Symbolic module maintains Bayesian posterior over discrete hypothesis set; frozen LLM provides semantic reasoning via entropy-adaptive fusion\n- **Approach:** Maintains hypothesis confirmations through symbolic Bayesian updates (not via demonstrations)\n- **Core Use Case:** Recommendation/personalization without fine-tuning\n\n**Does NOT directly compete with FABEL because:** Doesn't use user demonstrations as warm priors; focuses on symbolic hypothesis confirmation rather than demo-conditioned Bayesian initialization.\n\n---\n\n### **6. In-Context Bayesian Reward Modeling (arXiv 2602.08819) - \"Bayesian Preference Learning for Test-Time Steerable Reward Models\"**\n\n**Status: Test-time reward model adaptation, not user-facing personalization**\n\n**Key Details:**\n- **Title:** Bayesian Preference Learning for Test-Time Steerable Reward Models\n- **Innovation:** Variational In-Context Reward Modeling (ICRM) uses in-context preference demonstrations with Beta priors for test-time reward model adaptation\n- **Uses:** In-context demonstrations to condition warm priors (technically similar to FABEL's approach!)\n- **Core Use Case:** Making reward models flexible at inference time for multi-objective alignment\n\n**Does NOT compete with FABEL because:** Focuses on reward model inference-time flexibility, not on interactive user-facing response-style personalization via preference elicitation.\n\n---\n\n### **Conclusion:**\n\n**Direct Competitors to FABEL:**\n- **MAPLE** - Partial overlap (user-facing preference learning via active queries, but broader scope)\n- **AMPLe** - Closest competitor (interactive LLM personalization with Bayesian active learning, but uses pairwise comparisons not demo-conditioned warm priors)\n\n**Not Competitors (Different Focus Areas):**\n- **BAL-PM** → RLHF/reward model training efficiency (backend, not user-facing)\n- **APRICOT** → Robotic task planning with preference learning (different domain)\n- **AdaptFuse** → Sequential symbolic hypothesis confirmation (no demonstrations)\n- **In-Context Reward Models** → Test-time reward model flexibility (not user personalization)\n\n**Unique Aspects of FABEL:**\nFABEL appears to be novel in its specific combination of: (1) user demonstrations as Bayesian warm priors, (2) EIG-based binary hypothesis confirmation, (3) explicit disconfirmation probes, applied specifically to LLM response-style personalization. While other papers address pieces of this puzzle, the particular integration for demo-conditioned interactive personalization is not clearly replicated in the literature I searched.\n\n---\n\nSources:\n- [BAL-PM: Deep Bayesian Active Learning for Preference Modeling in Large Language Models](https://arxiv.org/abs/2406.10023)\n- [MAPLE: A Framework for Active Preference Learning Guided by Large Language Models](https://arxiv.org/abs/2412.07207)\n- [APRICOT: Active Preference Learning and Constraint-Aware Task Planning with LLMs](https://arxiv.org/abs/2410.19656)\n- [AMPLe: Comparison-based Active Preference Learning for Multi-dimensional Personalization](https://arxiv.org/abs/2411.00524)\n- [AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference](https://arxiv.org/abs/2604.03925)\n- [Bayesian Preference Learning for Test-Time Steerable Reward Models](https://arxiv.org/abs/2602.08819)"
      }
    ],
    "totalDurationMs": 109758,
    "totalTokens": 32407,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 29943,
      "output_tokens": 2074,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 2074,
          "cache_read_input_tokens": 29943,
          "cache_creation_input_tokens": 390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 390,
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
  "sourceToolAssistantUUID": "c3f40db9-7d3f-4c48-9dca-df146acc52a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T08:03:25.317Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have more complete information. Let me analyze the findings:

1. **BAL-PM (NeurIPS 2024)**: NOT a competitor - focuses on RLHF annotation efficiency, not user-facing personalization. ✓
2. **MAPLE (AAAI 2025)**: Partial overlap but different scope (general alignment, trajectory ranking). Should probably be cited.
3. **AdaptFuse (arXiv 2604.03925)**: This is NEW and interesting - "Training-Free Sequential Preference Learning via Externalized Bayesian Inference" - it maintains a Bayesian posterior over discrete hypothesis set + frozen LLM provides semantic reasoning via entropy-adaptive fusion. 

AdaptFuse does sound potentially competitive, but the key distinction is that it doesn't leverage user demonstrations as warm priors for Bayesian initialization—it focuses on symbolic hypothesis confirmation instead. So while both are training-free Bayesian approaches, FABEL's demo-conditioned initialization is a meaningful differentiator. Given the timing (AdaptFuse in April 2026 vs. FABEL targeting EMNLP 2026), I should monitor this closely.

Now I'm looking more carefully at MAPLE from AAAI 2025 to understand how it fits into this landscape.

MAPLE seems to be more of a general alignment and RLHF paper that uses language-conditioned active query selection and models preference distributions from natural language feedback and trajectory rankings, rather than a direct competitor to FABEL's user-facing LLM personalization approach. The real concern is AdaptFuse from April 2026, which uses Bayesian inference over discrete hypotheses with a frozen LLM in a training-free setup—that's much closer to FABEL's core mechanism and needs to be cited and clearly differentiated through FABEL's use of demo-conditioned warm priors and disconfirmation probes. The disconfirmation probe mechanism's role is primarily diagnostic—it signals good prior calibration when probes aren't selected—but the "Falsification-Aligned" framing might oversell this since the soft quota is what actually guarantees falsification coverage. I initially thought this was a weakness, but the proposal does address it by positioning probes as prior-shaping devices whose selection rate indicates calibration quality. Still, a reviewer might push back: if these probes are genuinely false given the demos, why include them at all rather than just relying on the quota?

The answer is that the model's assessment of falsity could be wrong—the prior might be miscalibrated—so occasionally asking these probes catches that error. This rationale is already in the proposal, so I won't flag it further.

My remaining concerns are the potential uncited concurrent work in AdaptFuse and a minor MAPLE citation gap. For my final assessment, novelty sits around 3.5/5 since the demo-conditioned warm prior with disconfirmation probes is genuinely novel, though AdaptFuse could narrow that space depending on what it covers.

Feasibility is solid at 4.0/5—the scope is reasonable, the dataset is public, and compute is budgeted, with BED-LLM reimplementation as the main time-boxed risk. Clarity improved significantly to 4.5/5 after seven rounds of refinement. Impact lands at 3.5/5, which feels like EMNLP Findings level work.

That averages to 3.875/5, suggesting a revision is needed. But reconsidering novelty with AdaptFuse in mind: if it uses a Bayesian posterior over discrete hypotheses with a frozen LLM like BED-LLM or FABEL, then the key differentiator here is the demo-conditioned warm start rather than cold initialization.

Actually, wait—looking back at what the agent said about AdaptFuse, it maintains hypothesis confirmations through symbolic Bayesian updates without demonstrations, focusing on symbolic confirmation rather than demo-conditioned initialization. So AdaptFuse doesn't actually use user demonstrations at all, which means it's not as directly comparable as I thought. The novelty score of 3.5/5 still holds.

The verdict is to revise. I need to check and cite AdaptFuse as concurrent work while highlighting the demo-conditioned warm prior as the differentiator, and consider adding MAPLE from AAAI 2025 to related work. I need to cite AdaptFuse as concurrent work in the same Bayesian framework, noting the key difference that FABEL uses demo-conditioned warm starts while AdaptFuse performs cold symbolic updates. Beyond that, MAPLE deserves a brief mention for active preference learning with user interaction. The main implementation risk remains the BED-LLM baseline—without public code, I'll need to either commit to the full Rao-Blackwellized approach or clearly specify the approximation method (entropy-based selection with rejection sampling) if that's what gets used.

Actually, I realize the timeline concern was already addressed in previous feedback with the 3-4 agent-day time-box and labeled fallback, so I shouldn't keep flagging it. The real remaining issues are just those two citation gaps—both moderate-to-minor. I don't see any critical blockers left. The scores look reasonable: novelty and impact around 3.5, feasibility at 4.0, clarity at 4.5, averaging to 3.875, which suggests a revise recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d28a61e-8591-4f31-9aa2-869df75e7a77",
  "isSidechain": false,
  "requestId": "req_011CatYCoEjUoJAxer3Gj8zb",
  "type": "assistant",
  "uuid": "cbc9d757-2197-4d47-bda3-8134ff0309e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WHaLUxtDLVRyUYjetxuAh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12535,
      "cache_read_input_tokens": 47515,
      "output_tokens": 4327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4327,
          "cache_read_input_tokens": 47515,
          "cache_creation_input_tokens": 12535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12535
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

_source line 22 · 2026-05-10T08:03:47.959Z_

Based on my independent research, I now have sufficient information to issue the Round 8 verdict.

**Key findings from verification:**
- BED-LLM (ICLR 2026), PROSE (ICML 2025), HyPerAlign, OPEN (ACL 2024), AMPLe (ACL 2025), "Failing to Falsify" — all confirmed, accurately described ✓
- BAL-PM (NeurIPS 2024) = annotation efficiency for RLHF pipelines, NOT user-facing personalization — not a competitor ✓
- MAPLE (AAAI 2025) = user-facing active preference learning, but broader scope (trajectory ranking, general alignment) — should be cited
- **AdaptFuse (arXiv 2604.03925, April 2026)** = "Training-Free Sequential Preference Learning via Externalized Bayesian Inference" — maintains Bayesian posterior over discrete hypothesis sets with frozen LLM, training-free; directly adjacent to FABEL's mechanism, UNCITED
- PersonalLLM (ICLR 2025) on HuggingFace confirmed ✓
- All Round 7 fixes (self-consistency circularity → cross-model ρ check, human study overstatement removed) verified as applied ✓

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "Demo-conditioned warm Bayesian prior + disconfirmation probes is genuinely absent from OPEN, BED-LLM, AMPLe, and PROSE. However, AdaptFuse (April 2026, arXiv 2604.03925) represents an uncited concurrent work in the same 'training-free Bayesian posterior over discrete hypothesis sets' family, potentially narrowing the novelty gap. Under the factored posterior approximation, EIG reduces to simple uncertainty-based selection, which modestly weakens the Bayesian framing."
    },
    "feasibility": {
      "score": 4.0,
      "rationale": "PersonalLLM is public, Qwen2.5-7B-Instruct is available, compute (75h H100-equivalent) is within budget, and 16-day auto-research timeline is plausible. BED-LLM reimplementation (no public code, ~45-50 LLM calls/step) remains the primary timeline risk but is time-boxed with a labeled fallback."
    },
    "clarity": {
      "score": 4.5,
      "rationale": "After seven rounds, the algorithm is fully specified including disconfirmation probe prompt, τ-selection criterion with fallback, soft quota mechanism, factored posterior acknowledgment, and cross-model calibration check. No ambiguity remains in the core pipeline."
    },
    "impact": {
      "score": 3.5,
      "rationale": "Solid contribution to the interactive LLM personalization subfield. Demo-conditioned warm start genuinely reduces elicitation burden vs. BED-LLM/OPEN; disconfirmation probes address a real failure mode. EMNLP Findings is the realistic target; Main requires the human study to yield positive results."
    }
  },
  "issues": [
    "MODERATE — AdaptFuse (arXiv 2604.03925, April 2026) is uncited and directly adjacent: 'Training-Free Sequential Preference Learning via Externalized Bayesian Inference' maintains a Bayesian posterior over discrete hypothesis sets using a frozen LLM's semantic reasoning via entropy-adaptive fusion — it is in the same 'Bayesian posterior over discrete hypotheses + frozen LLM + no fine-tuning' family as BED-LLM and FABEL. FABEL's key differentiator (demo-conditioned warm prior + disconfirmation probes) holds, but AdaptFuse must be cited and differentiated in the landscape. A reviewer familiar with April 2026 arXiv would flag its absence immediately. Suggested addition to cluster (3) or a new cluster: 'AdaptFuse (2604.03925) uses externalized symbolic Bayesian inference over hypothesis sets with entropy-adaptive frozen-LLM fusion; FABEL differs by (1) initializing a user-specific demo-conditioned warm prior rather than cold-start symbolic updates, and (2) including mandatory disconfirmation probes absent from AdaptFuse.'",
    "MINOR — MAPLE (arXiv 2412.07207, AAAI 2025) is uncited. It uses LLM-modeled preference function distributions conditioned on natural language feedback with active query selection for general alignment — in the same broad space as FABEL's active Bayesian personalization. While MAPLE uses trajectory-level pairwise rankings (not binary hypothesis confirmation) and targets general alignment rather than response-style personalization, a one-sentence mention in landscape cluster (3b) or a new cluster is sufficient. Without it, the landscape is incomplete for AAAI 2025 active preference learning work."
  ],
  "feedback": "After seven rounds of thorough revision, this proposal is substantively close to publication-ready at EMNLP Findings level. All Round 7 issues are cleanly resolved: the self-consistency circularity in Stage 2a is addressed via the cross-model Llama-3.1-8B-Instruct calibration check with explicit fallback behavior; the human study overstatement is removed. Two remaining citation gaps must be closed:\n\n**Fix 1 (Moderate, 1 paragraph):** Cite AdaptFuse (arXiv 2604.03925, April 2026) as a concurrent member of the training-free Bayesian hypothesis-set inference family. Place it in landscape cluster (3) or a new cluster (6). Key differentiation: 'AdaptFuse maintains a symbolic Bayesian posterior over discrete hypotheses using entropy-adaptive fusion with a frozen LLM; FABEL extends this line with (1) user-specific demonstration-conditioned warm priors rather than cold symbolic initialization and (2) mandatory disconfirmation probes that AdaptFuse lacks.' This is the closest concurrent work and its absence would be flagged by area chairs familiar with April 2026 arXiv.\n\n**Fix 2 (Minor, 1-2 sentences):** Cite MAPLE (arXiv 2412.07207, AAAI 2025) in related work on active preference learning for LLMs. One sentence suffices: 'MAPLE (AAAI 2025) uses LLM-conditioned preference function modeling with active query selection for alignment tasks; FABEL differs in using binary hypothesis confirmation grounded in user demonstrations rather than trajectory-level pairwise ranking queries.' This closes the AAAI 2025 gap in the landscape.\n\nAfter these two fixes, there are no remaining critical gaps. The core novelty claim — demo-conditioned warm Bayesian prior + EIG binary confirmation + disconfirmation probes, in the LLM response-style personalization domain — is verified as absent from all cited and independently found prior work. The MVP compute (75h H100-equivalent) is confirmed within budget, PersonalLLM is publicly available, and the experimental design (warm vs. cold prior ablation + Stage 2a calibration with cross-model ρ check) is appropriate for EMNLP Findings.",
  "reason": "Two citation gaps remain (AdaptFuse April 2026 as uncited concurrent work, MAPLE AAAI 2025 as uncited related work); all Round 7 technical issues are cleanly resolved; proposal is otherwise publication-ready at EMNLP Findings level."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbc9d757-2197-4d47-bda3-8134ff0309e0",
  "isSidechain": false,
  "requestId": "req_011CatYCoEjUoJAxer3Gj8zb",
  "type": "assistant",
  "uuid": "8ba6c717-b928-449d-9a31-d4e2f0150029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WHaLUxtDLVRyUYjetxuAh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12535,
      "cache_read_input_tokens": 47515,
      "output_tokens": 4327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4327,
          "cache_read_input_tokens": 47515,
          "cache_creation_input_tokens": 12535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12535
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
  "leafUuid": "8ba6c717-b928-449d-9a31-d4e2f0150029",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstrate warm-start Bayesian preference elicitation for LLM personalization",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8ba6c717-b928-449d-9a31-d4e2f0150029",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Demonstrate warm-start Bayesian preference elicitation for LLM personalization",
  "sessionId": "0aa39802-5b33-414f-b371-b5311ac03ff3"
}
```

---
