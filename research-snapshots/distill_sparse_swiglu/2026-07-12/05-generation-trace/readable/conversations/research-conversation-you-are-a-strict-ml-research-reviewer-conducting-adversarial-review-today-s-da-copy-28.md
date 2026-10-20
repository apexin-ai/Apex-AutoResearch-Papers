# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 178
- **Recorded user turns:** 1
- **Tool calls:** 59
- **Original source:** `logs/chats/exported-trajectories/account-2/c910c13d-bae5-469c-bad4-44d932f7b20c.jsonl`
- **Structured JSON:** [`5056391d340d9eefc742.json`](../../sessions/50/5056391d340d9eefc742.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T11:39:05.927Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T11:39:05.927Z",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\nDirection：因为真实数据采样的时候会有很多噪声，比如收集时的冗余动作等，如何避免训练数据中的噪声影响vla的训练，可以使用一个经验池的形式来训练，借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选，再适当过滤掉一些低分数的冗余动作，如果是从一些底层理论角度提出了筛选方法 感觉不用真机也是可以接受的**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Learning\",\n  \"core_problem\": \"Does SFT data quality — which demonstrations are prioritized during training — affect downstream RL outcomes for vision-language-action models? The VLA training paradigm is shifting from SFT-only to SFT→RL pipelines, where SFT quality is the critical determinant of RL success. SimpleVLA-RL shows SFT data *quantity* gates RL (0 demos → 0% RL success), but no work has isolated how SFT data *quality* affects RL convergence and final performance. Multiple recent works study how SFT *technique* affects RL (gradient clipping, trust regions, distribution alignment), but none address the orthogonal question of data-level filtering. RAPID provides the mechanism to test this: by decomposing per-sample loss into reducible (learnable) and irreducible (noise) components via an EMA reference model, it prioritizes high-signal demonstrations during SFT, producing cleaner checkpoints for downstream RL. The core hypothesis is that noise-filtered SFT → faster RL convergence and better sample efficiency, particularly in realistic settings where demonstration quality varies.\",\n  \"opportunity\": \"Three converging trends create this opening:\\n\\n**1. SFT→RL pipelines are standard but SFT data quality's RL effect is unstudied.** SimpleVLA-RL (ICLR 2026) shows SFT accounts for 74pp of 82pp total improvement and SFT quantity gates RL success. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows warm-start SFT yields ~50% faster RL convergence. A growing body of work now demonstrates that SFT *technique* matters for downstream RL: the ICML 2026 'Off-Policy Token Clipped SFT' (Tian-Shuo Liu et al.) shows token-level gradient clipping during SFT yields 7.09% RL improvement and 11.54% reduced forgetting on LLM agentic benchmarks; PSFT (arXiv 2508.17784) applies PPO-style clipped surrogates to SFT; DFT (ICLR 2026, 2508.05629) dynamically rescales the SFT objective; 'Tailored Primitive Initialization' (arXiv 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning; PRISM (arXiv 2604.28123) aligns SFT and RL distributions via on-policy distillation. Yet none study how *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs. RAPID fills this gap with data-level noise filtering rather than token/objective-level modifications.\\n\\n**2. Reducible loss decomposition is proven but unexploited in VLA SFT.** RHO-LOSS (ICML 2022) showed excess loss identifies learnable-not-yet-learnt data, achieving 18x speedup on noisy datasets. ReLo (NeurIPS 2023) adapted this to RL using SAC's pre-existing target network. Rho-1 (NeurIPS 2024) brought it to LLM pretraining with a fixed reference. iw-SFT (arXiv 2507.12856) uses an EMA reference for importance-weighted SFT in continuous control — but for trajectory-level importance weights approximating on-policy gradients, not for reducible loss decomposition. RAPID uses the EMA for a different purpose: computing R(x) = max(0, L_θ(x) − L_EMA(x)) to decompose loss into reducible and irreducible components. The max(0,·) clamp provides explicit noise suppression that importance weighting lacks. DS2 (ICLR 2025) performs dynamic instance-level reweighting but uses raw loss without reducible decomposition, inheriting noise overfitting risk. No existing work applies sample-level, continuously-adaptive reducible-loss *prioritized sampling* to VLA SFT.\\n\\n**3. VLA demonstration quality varies in practice.** The 'When Do Curricula Work?' finding (ICLR 2021) that curricula provide marginal benefits on clean benchmarks implies RAPID's value is in noisy/mixed-quality settings and the SFT→RL pipeline — not clean-data benchmarks where VLAs already achieve 97%+. LIBERO-Plus (CVPR 2026) exposed that high success rates on standard LIBERO mask fragility (OpenVLA-OFT: 97.1% → 70.0%). Real-world datasets (OXE, DROID) contain heterogeneous demonstration quality from varied operators. RAPID targets these realistic conditions.\\n\\n**The specific gap (honestly stated):** iw-SFT already uses EMA for continuous control importance weighting. RAPID's novelty over iw-SFT is threefold: (a) reducible loss decomposition (not trajectory probabilities for importance weights), providing noise-robust prioritization via the max(0,·) clamp; (b) PER-style sampling (controlling which samples are seen, not multiplicative loss reweighting); (c) training-horizon-aware τ calibration with finite-T theory. Furthermore, no work — including all SFT-technique-for-RL papers — has tested whether SFT *data quality via noise filtering* affects downstream RL for VLAs.\",\n  \"landscape\": \"**Reducible/excess loss foundations:** RHO-LOSS (ICML 2022) selects points by excess loss over a fixed holdout-trained reference — 18x faster on noisy Clothing-1M. ReLo (NeurIPS 2023) computes reducible TD error using SAC's Polyak-averaged target network (double duty: TD stability + data scoring). Rho-1 (NeurIPS 2024) brings excess loss to LLM pretraining with a fixed reference for selective token training. All supervised applications use *static* reference models.\\n\\n**Dynamic instance-level reweighting:** DS2 (ICLR 2025) normalizes per-sample losses and applies transformation functions for dynamic reweighting during LLM pretraining, with formal convergence guarantees. Uses raw loss without reducible decomposition. LEAD (arXiv May 2025) uses EMA over *loss values* (not model parameters) for online data selection during LLM SFT. UDS (arXiv Oct 2025) uses nuclear norm of logits for utility-diversity batch selection without a reference model.\\n\\n**Importance-weighted SFT:** iw-SFT (arXiv Jul 2025, 2507.12856) proves SFT on curated data optimizes a lower bound on the RL objective. For continuous control (D4RL), it uses an EMA reference (θ_q = α·θ_q + (1-α)·θ) for trajectory-level importance weights. For LLMs, it uses discrete time-lagged updates. Critical distinction from RAPID: iw-SFT uses EMA for importance weighting (multiplicative loss scaling approximating on-policy gradients); RAPID uses EMA for reducible loss decomposition (R = max(0, L_θ − L_EMA)) with PER-style sampling priorities, providing noise robustness absent in importance weighting.\\n\\n**Domain-level data mixing:** DoReMi (NeurIPS 2023) uses excess loss with Group DRO for LLM domain mixing. Re-Mix (CoRL 2024) extends this to robot IL with domain-level weights over OXE datasets using a fixed reference. Both operate at domain level, not sample level.\\n\\n**Static demonstration curation:** SCIZOR (ICRA 2026) uses self-supervised progress prediction. CUPID (CoRL 2025) uses influence functions. RINSE (ICML 2025) uses smoothness metrics. DataMIL (ICLR 2026) uses datamodels. DemInf (RSS 2025) uses k-NN mutual information. All score data once before training — static preprocessing that cannot adapt to the policy's evolving learning needs.\\n\\n**SFT technique → RL quality (NEW — critical related work):** Off-Policy Token Clipped SFT (Tian-Shuo Liu et al., ICML 2026 poster) clips gradient updates from low-probability tokens during SFT, acting as a trust region that reduces forgetting (11.54%) and improves downstream RL (7.09%) on ALFWorld/ScienceWorld. PSFT (arXiv Aug 2025, 2508.17784) applies PPO-style clipped surrogates to SFT for generalization. DFT (ICLR 2026, 2508.05629) dynamically rescales SFT gradients based on token probability. Tailored Primitive Initialization (arXiv Nov 2025, 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning. PRISM (arXiv Apr 2026, 2604.28123) inserts on-policy distillation between SFT and RL to repair distributional drift. All operate on *techniques* (gradient clipping, objective modification, distribution alignment) rather than *data quality* (which demonstrations to prioritize).\\n\\n**RL post-training for VLAs:** SimpleVLA-RL (ICLR 2026) achieves 99.1% on LIBERO via GRPO post-training. SFT accounts for 74pp of 82pp improvement; Section 6.2 ablates quantity (not quality). VLA-OPD (arXiv Mar 2026) bridges offline SFT and online RL via on-policy distillation. VLA-RFT uses a learned world model for RL.\\n\\n**Curricula effectiveness:** 'When Do Curricula Work?' (ICLR 2021 Oral) shows curriculum benefits are marginal on clean data — gains come only under limited budget or noisy data. Critical calibration for RAPID's claims.\\n\\n**EMA dynamics and memorization:** EMA models show improved robustness to noisy labels (arXiv 2411.18704) but are not independent of the training model. Self-distillation feedback loops can amplify errors (arXiv 2603.24472). Zhang et al. (ICLR 2017) and Kajitsuka & Sato (ICLR 2025) show high-capacity models can memorize noise, so noise suppression cannot assume persistently high loss on noisy samples.\\n\\n**The gap:** Multiple works study SFT *technique* for RL (gradient clipping, trust regions, objective rescaling, distribution alignment). iw-SFT uses EMA for importance weighting in continuous control. No existing work applies sample-level reducible-loss prioritized sampling to VLA SFT, and no work tests whether SFT data quality via noise-filtering prioritization affects downstream RL for VLAs.\",\n  \"approach\": \"**Method overview.** RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations) replaces uniform sampling during VLA SFT with online, noise-robust prioritized sampling based on reducible loss. Beyond improving SFT in isolation, RAPID targets the SFT stage that initializes downstream RL — the paper's primary contribution is the empirical finding that SFT data quality cascades to RL outcomes.\\n\\n**Contribution 1: EMA-based reducible loss for VLA SFT.** RAPID computes reducible loss R(x) = max(0, L_θ(x) − L_EMA(x)), where L is action-prediction loss and θ_EMA ← τ·θ_EMA + (1−τ)·θ is updated every gradient step. *Honest positioning:* iw-SFT (2507.12856) proposed EMA for importance weighting in continuous control; RAPID uses EMA for a different purpose — reducible loss decomposition that provides noise-robust prioritization. The key mechanism is the max(0,·) clamp: noisy samples that the model cannot fit have L_θ ≈ L_EMA → R ≈ 0; noisy samples the model gradually memorizes have L_θ ≤ L_EMA → R = 0. Both regimes suppress noise. This decomposition cannot be replicated by raw-loss methods (DS2, SuRe) which assign high weight to noisy samples. Compared to LEAD's EMA over loss values, RAPID's EMA over model parameters captures richer structural information.\\n\\nSampling: transitions drawn proportionally to R(x)^α with importance-sampling correction β-annealed from 0→1 (Schaul et al. 2016). Priorities refreshed every K=500 steps (~8-12% compute overhead). Two-level sampling: trajectory priority = mean reducible loss (inter-demonstration), transition priority = per-step reducible loss (intra-demonstration).\\n\\n**Contribution 2: Training-horizon-aware τ calibration (theoretical support).** We analyze the bias-variance tradeoff in τ: tracking error scales as O(ε·τ/(1-τ)), signal quality scales similarly. The product is maximized at τ* = 1 − Θ(√ε). For VLA SFT (ε ≈ 5×10⁻⁴), τ* ≈ 0.978. Within the iw-SFT framework, the adaptive EMA reference achieves O(T) cumulative bound gap vs Ω(T²) for static references. *Testability caveat:* the constants in these bounds depend on loss landscape properties (Lipschitz constant, gradient bound) that are hard to estimate a priori. We frame the empirical bound-gap measurement as testing the theory's *qualitative* prediction (linear vs quadratic growth) rather than the *quantitative* crossover point T₀. The noise suppression guarantee is reformulated to handle high-capacity VLM memorization: relative suppression ratio O(1−τ) ≈ 0.022 for τ* = 0.978. Ablation over τ ∈ {0.97, 0.99, 0.995, 0.999, 0.9999} validates the theory and identifies failure modes at both extremes.\\n\\n**Contribution 3 (PRIMARY): RAPID+RL pipeline — SFT data quality → RL outcomes for VLAs.** The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL convergence for VLAs. *Differentiation from ICML 2026 clipping paper:* that work shows token-level gradient clipping during SFT improves downstream RL for LLMs on text-based agentic tasks; we show data-level noise filtering during SFT improves downstream RL for VLAs on robotic manipulation — complementary findings across domains and mechanisms. Protocol: (a) Vanilla SFT → GRPO (SimpleVLA-RL), (b) RAPID SFT → GRPO, on LIBERO-Long with 25% noise injection. Also test fixed-reference SFT → GRPO to validate that RAPID's *adaptive* filtering provides the RL benefit. Metrics: RL convergence speed (steps to 90% success), final success rate, total environment interactions. Even a modest improvement (e.g., 30-50% fewer RL steps) is practically significant given expensive RL environment interactions.\\n\\n**Experimental plan.** Built on OpenVLA-OFT (open-source).\\n\\n*Experiment 1 (Primary — Noise injection SFT):* Corrupt LIBERO-Long demonstrations at 10%, 25%, 50% with three corruption types: Gaussian action noise, random frame dropping, trajectory truncation. Pre-pilot to ensure baseline degrades to 60-80%. Baselines: uniform, raw-loss priority, DS2-adapted, fixed-reference reducible loss. *Limitation acknowledged:* synthetic corruption is a controlled test of the mechanism, not a claim about real-world robustness. Real-world noise (hesitation, suboptimal strategies, operator fatigue) is coherent and structurally different. The OXE experiment (Experiment 4) addresses this.\\n\\n*Experiment 2 (Primary — RAPID+RL pipeline):* 2-3 LIBERO-Long tasks with 25% noise. Four conditions: {Vanilla SFT, RAPID SFT, Fixed-reference SFT} × GRPO. RL stage uses SimpleVLA-RL (open-source, ~400 gradient steps, computationally cheap).\\n\\n*Experiment 3 (Sanity — Standard LIBERO-Long):* Clean data, expecting minimal gains per 'When Do Curricula Work?' analysis. Demonstrates RAPID does no harm.\\n\\n*Experiment 4 (AAAI — OXE mixed-quality):* Real-world heterogeneous quality, following SCIZOR/Re-Mix setup. Addresses the synthetic noise limitation.\\n\\n*Experiment 5 (AAAI — LIBERO-Plus robustness):* Tests whether noise filtering extracts more robust representations.\\n\\n**CoRL 2026 minimum viable plan (abstract May 26, paper May 29).** GO/NO-GO BY MAY 22: if first noise-injection + RL results are not available, fall back to AAAI 2027 only. CoRL scope: Experiments 1-3 (15 SFT runs + 4 RL runs ≈ 950 GPU-hours). Lead with RAPID+RL finding as headline. Risk: SimpleVLA-RL integration with RAPID checkpoints is untested.\\n\\n**AAAI 2027 (primary target, deadline ~Aug 2026).** Full version: all 5 experiments, complete ablation suite (τ, K, α, β), all baselines including CUPID and SCIZOR, comprehensive theory validation (qualitative bound gap growth, noise suppression ratios). This is the definitive version.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~3500h A100-80GB (noise injection: 3 types × 3 ratios × ~80h = ~720h + RAPID+RL: 6 RL runs × ~50h = 300h + LIBERO-Plus: ~200h eval + standard LIBERO-Long: 4 methods × 80h = 320h + OXE: ~400h + baselines ~600h + ablations ~500h + theory validation ~100h)\",\n      \"gpu_utilization\": \"~25-35% effective utilization\",\n      \"timeline\": \"10-14 weeks (full AAAI version); 14 days (CoRL sprint with go/no-go by May 22)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$5,250 at ~$1.50/hr (full version); ~$1,425 for CoRL sprint (950h)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~5000h A100-80GB\",\n      \"gpu_utilization\": \"~60-70% utilization\",\n      \"timeline\": \"6-8 weeks (full version); 10-12 days (CoRL sprint)\",\n      \"team\": \"1 researcher, ~30-45min/day\",\n      \"claude_api_cost\": \"$300-500\",\n      \"estimated_gpu_cost\": \"~$7,500 (full); ~$2,000 (CoRL sprint)\",\n      \"risk_note\": \"SimpleVLA-RL integration with RAPID SFT checkpoints is untested. May 22 go/no-go decision critical.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~6500-7500h A100-80GB\",\n      \"gpu_utilization\": \"~90-95%\",\n      \"timeline\": \"16-24 days with 8×A100\",\n      \"team\": \"0 (initial setup and final review only)\",\n      \"claude_api_cost\": \"$600-1000\",\n      \"estimated_gpu_cost\": \"~$11,000\",\n      \"speed_bottleneck\": \"GPU cluster availability; SimpleVLA-RL environment rollouts\",\n      \"risk_note\": \"Agent may over-explore τ-K interaction space; ~15-20% wasted compute risk without human calibration\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 26, paper May 29 — GO/NO-GO BY MAY 22: fall back to AAAI-only if first noise-injection + RL results unavailable; empirical focus with RAPID+RL headline, 15 SFT + 4 RL runs ≈ 950h)\",\n    \"AAAI 2027 (deadline ~Aug 2026 — primary target for full version with all experiments, theory, OXE, LIBERO-Plus)\",\n    \"ICRA 2027 (deadline ~Sep 2026 — fallback if CoRL infeasible, strong robot learning venue fit)\",\n    \"ICLR 2027 (deadline ~Sep-Oct 2026 — only if finite-T theory validates empirically and RAPID+RL finding is compelling)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt [RHO-LOSS] (ICML 2022)\",\n    \"Prioritized Experience Replay (ICLR 2016)\",\n    \"Prioritizing Samples in Reinforcement Learning with Reducible Loss [ReLo] (NeurIPS 2023)\",\n    \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)\",\n    \"Not All Tokens Are What You Need [Rho-1] (NeurIPS 2024)\",\n    \"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)\",\n    \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining [DS2] (ICLR 2025)\",\n    \"Supervised Fine Tuning on Curated Data is Reinforcement Learning [iw-SFT] (arXiv Jul 2025, 2507.12856)\",\n    \"LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning (arXiv May 2025)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)\",\n    \"RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025)\",\n    \"DemInf: Robot Data Curation with Mutual Information Estimators (RSS 2025)\",\n    \"When Do Curricula Work? (ICLR 2021)\",\n    \"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (ICML 2026 poster)\",\n    \"Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025, 2508.17784)\",\n    \"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026, 2508.05629)\",\n    \"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025, 2511.12429)\",\n    \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026, 2604.28123)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\",\n    \"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)\",\n    \"What Can RL Bring to VLA Generalization? (NeurIPS 2025)\",\n    \"VLA-OPD: Bridging Offline SFT and Online RL for VLAs via On-Policy Distillation (arXiv Mar 2026)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)\",\n    \"Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits (arXiv Nov 2024)\",\n    \"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv Mar 2026)\",\n    \"Understanding Deep Learning Requires Rethinking Generalization (Zhang et al., ICLR 2017)\",\n    \"On the Optimal Memorization Capacity of Transformers (Kajitsuka & Sato, ICLR 2025)\",\n    \"SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv Nov 2025)\",\n    \"Density-Ratio Weighted Behavioral Cloning (arXiv Oct 2025)\",\n    \"Token Priority SFT (arXiv Feb 2026)\",\n    \"UDS: Utility-Diversity Aware Online Batch Selection for LLM SFT (arXiv Oct 2025)\"\n  ],\n  \"description\": \"We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which replaces uniform sampling during VLA supervised fine-tuning with online, noise-robust prioritized sampling based on reducible loss — and provides the first empirical test of whether SFT data quality cascades to downstream RL outcomes for VLAs.\\n\\nRAPID makes three contributions:\\n\\n(1) **EMA-based reducible loss for VLA SFT**: Computes R(x) = max(0, L_θ(x) − L_EMA(x)) to decompose loss into learnable and irreducible components. Honest positioning: iw-SFT (2507.12856) uses EMA for importance weighting in continuous control; RAPID uses EMA for reducible loss decomposition with PER-style sampling, providing noise robustness via the max(0,·) clamp that importance weighting lacks. Training-horizon-aware τ calibration (τ* = 1 − Θ(√ε) ≈ 0.978) connects EMA decay to learning rate, with finite-T bounds predicting O(T) vs Ω(T²) cumulative gap over static references — framed as a qualitative prediction validated empirically.\\n\\n(2) **Noise-robust SFT on mixed-quality demonstrations**: Controlled noise injection experiments (Gaussian action noise, frame dropping, trajectory truncation) on LIBERO-Long validate that reducible loss decomposition outperforms raw-loss methods and static curation on noisy data. Acknowledges synthetic corruption as a controlled mechanism test; OXE experiments (AAAI version) address real-world heterogeneity.\\n\\n(3) **RAPID+RL pipeline validation (primary contribution)**: The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL for VLAs. Differentiation from the ICML 2026 'Off-Policy Token Clipped SFT' paper: that work shows token-level gradient clipping during SFT improves RL for LLMs; we show data-level noise filtering during SFT improves RL for VLAs — complementary findings across domains and mechanisms. Tests RAPID SFT → SimpleVLA-RL GRPO vs vanilla SFT → GRPO, measuring RL convergence speed and sample efficiency.\\n\\nCoRL 2026 is a stretch goal (go/no-go by May 22); AAAI 2027 is the primary target with full experiments including LIBERO-Plus robustness and OXE mixed-quality.\",\n  \"project_name\": \"adaptive_replay_vla\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: VACO (Value-Aligned Behavior Cloning, ICLR 2025) uses a meta-scoring network + value function to adaptively weight BC demonstrations during training via bi-level optimization. This is the closest existing work and is not cited or discussed. The generator must explicitly differentiate APER from VACO and justify why TD-error-based PER sampling is superior to learned meta-weights.\", \"CRITICAL: ReLo (NeurIPS 2023) demonstrated that TD-error-based prioritization frequently samples noisy/unlearnable data points with persistently high loss, hindering learning. The proposed approach uses raw TD error magnitude as the priority signal, which is known to be a flawed proxy. The paper must address how APER avoids this well-documented failure mode—reducible loss or similar corrections should be considered.\", \"CRITICAL: Hindsight goal relabeling is designed for goal-conditioned settings where goals are states (e.g., images). VLA models operate with natural language instructions as goals. How does one perform hindsight relabeling of language goals? This is a non-trivial technical challenge (requires captioning achieved states as language goals) that is completely unspecified.\", \"MISSING RELATED WORK: SuRe (Surprise-Driven Prioritised Replay, NeurIPS-submitted 2025) applies NLL-based prioritized replay to LLM continual learning. Token Priority SFT (arXiv Feb 2026) formalizes SFT as granular importance sampling. iw-SFT (arXiv Jul 2025) shows SFT on curated data is RL. These concurrent works significantly narrow the novelty claim.\", \"FEASIBILITY: The experimental plan requires reproducing 5 baselines across 3 benchmarks with ablations in under 20 days. Demo-SCORE requires training a policy, generating online rollouts, training a classifier, and filtering—this alone could take days to reproduce. The scope should be reduced to ensure quality over quantity.\", \"THEORETICAL WEAKNESS: For a sim-only CoRL paper, the theoretical contribution is thin. The paper should provide formal analysis (e.g., convergence guarantees, sample complexity bounds, or formal connection between TD error and demonstration quality under specific assumptions) to compensate for the lack of real-robot experiments.\", \"COST REALISM: The manual mode estimates ~500h A100 GPU hours, but with 5 baselines × 24h each on 8 GPUs, that alone is 960 GPU-hours. The estimate appears to undercount baseline reproduction costs significantly.\"]\nFeedback: The core intuition (adaptive > static data curation for VLA SFT) is reasonable, but the execution plan has critical gaps. Here's how to strengthen the idea:\n\n1. **Address VACO directly**: Read VACO (ICLR 2025) carefully and position APER as an improvement. Potential differentiators: VACO requires bi-level optimization (expensive), APER uses simpler PER sampling; VACO targets offline RL, APER targets imitation learning SFT. But you must demonstrate empirically or theoretically why your approach is better.\n\n2. **Fix the TD error proxy problem**: Replace raw TD error with reducible loss (ReLo, NeurIPS 2023) or a learned quality score. Alternatively, combine TD error with a noise detector (e.g., consistency across recomputation) to filter out irreducibly-noisy transitions. This would actually strengthen the novelty.\n\n3. **Solve language-conditioned hindsight relabeling**: Either (a) use a VLM to caption achieved goal states as language instructions for relabeling, (b) operate in embedding space rather than language space, or (c) use action-prediction loss as the priority signal instead of TD error, removing the need for a separate value function entirely. Option (c) would simplify the method considerably—high-loss transitions are 'surprising' to the current policy, similar to TD error but without the auxiliary value function.\n\n4. **Reduce scope for CoRL deadline**: Drop Demo-SCORE and DataMIL baselines (keep SCIZOR and CUPID as strongest competitors + uniform). Focus on LIBERO only (4 suites are sufficient). Add 1-2 targeted ablations rather than 10. This makes the timeline realistic.\n\n5. **Strengthen theory**: Prove a formal connection between TD-error-based priority and the expected improvement in policy performance per gradient step (sample efficiency bound). Even a simplified analysis under assumptions would strengthen a sim-only paper.\n\n6. **Consider the simpler alternative**: Using the policy's own prediction loss as the priority signal (high-loss = surprising = prioritize) would be simpler, avoid the need for a separate value function, and directly address the 'policy-aware' motivation. This might actually be a cleaner contribution.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: LIBERO benchmark saturation. OpenVLA-OFT achieves 96.2/98.3/96.2/90.7% per suite. Only LIBERO-Long has meaningful headroom at 90.7%. PLD achieves 99% (with RL). Showing statistically significant improvement from ~97% → 98% requires many evaluation seeds and the gains are not compelling. The generator must either: (a) add experiments on noisier/more diverse datasets where data quality matters more (e.g., OXE subsets, mixed-quality demonstrations), (b) design controlled noise injection experiments to demonstrate RAPID's noise-robustness advantage, or (c) adopt LIBERO-Plus/LIBERO-PRO which test robustness under perturbation and have more headroom.\", \"CRITICAL: Motivation-experiment mismatch. The core motivation is filtering noise from real-world demonstrations ('真实数据采样的时候会有很多噪声，比如收集时的冗余动作'), but LIBERO uses 50 high-quality human-teleoperated demos per task. These are relatively clean — the noise/redundancy that RAPID targets may be insufficient to demonstrate meaningful gains. The experimental design must include a scenario with genuinely noisy or heterogeneous demonstrations to validate the core hypothesis.\", \"MISSING RELATED WORK: 'Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning' (arXiv 2510.16882, Oct 2025) directly performs online scoring and selection of training samples during SFT using model output logits. This is conceptually very close to RAPID's online prioritization during SFT, though in the LLM domain. Must be cited and differentiated.\", \"NOVELTY CONCERN: SuRe (arXiv Nov 2025) combines NLL-based surprise + EMA (fast/slow LoRA merged via EMA) + prioritized replay. RAPID combines reducible loss (current_loss - EMA_loss) + EMA reference + prioritized replay. The key distinction — using reducible loss instead of raw NLL to avoid over-sampling noisy data — is actually ReLo's contribution (NeurIPS 2023), not RAPID's. RAPID's novel contribution is the domain transfer to VLA SFT + multi-granularity sampling. This should be stated more honestly rather than claiming the reducible loss mechanism as novel.\", \"TECHNICAL NOTE: ReLo uses a target network (periodic hard copy from online network) as its reference, NOT an EMA. RAPID proposes EMA instead. This is a meaningful design choice that should be explicitly justified — why EMA rather than periodic hard copy? What are the tradeoffs? This is actually a contribution that should be highlighted and ablated.\", \"THEORETICAL DEPTH: The convergence rate claim O(1/√(nη)) vs O(1/√n) is a standard importance sampling variance reduction result. The per-step improvement bound under Lipschitz smoothness is likely straightforward. The most interesting theoretical contribution — connecting reducible-loss prioritization to iw-SFT's importance-weighted framework as an adaptive quality score — should be the centerpiece of the theory section, not just one of three results.\", \"COST NOTE: CoRL deadline dates are off by 1 day (abstract May 25 not 26, paper May 28 not 29). Minor but indicates imprecision.\"]\nFeedback: The revision thoroughly addressed Round 1 issues (VACO positioning, ReLo failure mode, hindsight relabeling removal, scope reduction), showing strong engagement. The proposal is well-structured and the method is sound. However, two critical issues remain that prevent a pass:\n\n**1. Fix the experimental design for LIBERO saturation.** Your primary benchmark is near-saturated (97% avg). Three concrete options:\n- (a) **Add an OXE-based experiment**: Curate a mixed-quality subset of Open X-Embodiment with known quality variation (e.g., mix Bridge, RT-1, and lower-quality datasets). This directly tests the noisy-data motivation.\n- (b) **Controlled noise injection on LIBERO**: Systematically corrupt demonstrations (random action noise, frame dropping, trajectory truncation) at varying corruption ratios (10-50%) and show RAPID degrades gracefully while uniform sampling and static curation do not. This is the cleanest experimental design for the core claim.\n- (c) **Use LIBERO-Long exclusively or LIBERO-Plus**: LIBERO-Long (90.7% baseline) has more headroom. LIBERO-Plus tests robustness under perturbation and reveals that current high success rates are fragile.\n\n**2. Sharpen the novelty claim.** Currently the proposal presents reducible loss as its key contribution, but this is ReLo's idea. RAPID's actual novel contributions are: (i) adapting reducible loss from RL (with target network) to imitation SFT (with EMA reference) — justify and ablate EMA vs hard copy; (ii) multi-granularity trajectory+transition sampling; (iii) theoretical connection to iw-SFT showing reducible loss as an adaptive importance weight. Lead with these three points explicitly.\n\n**3. Minor additions needed:**\n- Cite and differentiate from 'Utility-Diversity Aware Online Batch Selection for LLM SFT' (arXiv 2510.16882)\n- Make the iw-SFT connection the centerpiece theoretical result\n- Add an ablation: EMA reference vs periodic hard-copy reference (à la ReLo's target network)\n- Consider reporting data efficiency curves (how quickly RAPID matches full-data performance) rather than just final success rate, since the headroom at convergence is small\n\n**Timeline recommendation:** CoRL 2026 (12 days) is infeasible for addressing these issues. Target AAAI 2027 (Aug deadline) as primary, with CoRL as a stretch only if implementation is complete and you can run the noise-injection experiment rapidly.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING REFERENCE: Re-Mix (Hejna et al., CoRL 2024) uses excess behavior cloning loss relative to a fixed reference model for domain-level data weighting in large-scale imitation learning — the same core concept (excess/reducible loss relative to a reference model to identify learnable vs. irreducibly hard data in IL) applied in the same domain (robot imitation learning). Published at CoRL, the user's target venue. Must be cited and explicitly differentiated. Key differences to articulate: Re-Mix operates at domain level with fixed reference and DRO optimization; RAPID operates at sample/transition level with adaptive EMA reference and PER-style sampling.\", \"CRITICAL MISSING REFERENCE: RHO-LOSS (Mindermann et al., ICML 2022) is the true foundational work on 'reducible holdout loss selection' for supervised learning — selecting training points that most reduce generalization loss by separating learnable from irreducibly noisy data using a reference model. The proposal credits ReLo (NeurIPS 2023) as foundational, but ReLo itself builds on RHO-LOSS. Since RAPID targets supervised fine-tuning (not RL), RHO-LOSS is a more direct ancestor than ReLo and must be cited.\", \"MISSING REFERENCE: DoReMi (Xie et al., NeurIPS 2023) uses excess loss relative to a pretrained reference model for domain mixing weights in LLM pretraining. Conceptually parallel to Re-Mix and RAPID. Should be cited to show the broader lineage of excess-loss-based data selection.\", \"MISSING REFERENCE: LEAD (arXiv May 2025, 2505.07437) introduces Instance-Level Dynamic Uncertainty combining instantaneous loss with exponential smoothing of historical loss signals for online data selection during LLM SFT. Very close mechanistically — uses EMA-smoothed loss signals (not an EMA model, but similar intuition) for online SFT selection. Must be cited and differentiated.\", \"MISSING REFERENCE: DataMIL (arXiv May 2025, 2505.09603) is a policy-driven data selection framework for robot imitation learning using the datamodels paradigm. Validated on 60+ tasks including Open X-Embodiment. While static, it's an important concurrent work in robot demonstration curation that should appear in the landscape.\", \"MISSING REFERENCE: DemInf / Robot Data Curation with Mutual Information Estimators (RSS 2025, 2502.08623) uses k-NN mutual information estimation for offline robot demonstration quality scoring. Another concurrent robot data curation method missing from the landscape.\", \"VENUE CORRECTION: RINSE is listed as 'arXiv April 2026' but was accepted at ICML 2025. Should be cited as 'RINSE (ICML 2025)' — this is a peer-reviewed publication, not just an arXiv preprint.\", \"NOVELTY REPOSITIONING NEEDED: The proposal's gap statement ('No existing work applies reducible-loss-based adaptive prioritized sampling to VLA imitation learning SFT') is technically accurate but misleadingly narrow. Re-Mix applies excess loss to imitation learning (domain level). RHO-LOSS applies reducible loss to supervised learning. Rho-1 applies excess loss to LLM pretraining. The real gap is narrower: 'No existing work applies sample-level, adaptive (EMA) reducible-loss prioritized sampling to VLA SFT.' This should be stated honestly.\", \"IMPACT CONCERN: SimpleVLA-RL (ICLR 2026) achieves 99% on standard LIBERO via RL post-training. The RL approach may increasingly marginalize SFT data curation as the bottleneck for VLA performance. The paper should discuss why SFT data quality still matters even when RL post-training is available — e.g., RL requires reward engineering, SFT is the warm-start for RL, or RAPID could complement RL post-training.\", \"MINOR: CoRL 2026 official deadlines are May 25/28 AoE (not May 26/29 as stated). The proposal's dates are UTC conversions of the AoE deadlines — technically the same instant but the official citation should use AoE.\"]\nFeedback: The proposal has improved substantially from Rounds 1-2, addressing LIBERO saturation (LIBERO-Plus + noise injection), motivation-experiment mismatch, UDS citation, and novelty positioning. The method is technically sound and the experimental plan is comprehensive. However, **the landscape analysis has a critical blind spot**: at least 6 important works are uncited, and two of them (Re-Mix, RHO-LOSS) directly impact the novelty claim.\n\n**Priority 1 — Cite and differentiate from Re-Mix (CoRL 2024).** This is the most urgent fix. Re-Mix demonstrates that excess BC loss relative to a reference model effectively curates imitation learning data at the domain level. RAPID's differentiation is clear: (a) sample/transition-level granularity vs. domain-level, (b) adaptive EMA reference vs. fixed reference, (c) PER-style online sampling vs. DRO optimization. Frame RAPID as extending Re-Mix's domain-level insight to fine-grained, adaptive sample-level prioritization. This is actually a strong narrative — 'Re-Mix showed excess loss works for domain weighting; we show it works even better at sample granularity with an adaptive reference.'\n\n**Priority 2 — Cite RHO-LOSS (ICML 2022) as the true foundational concept.** The reducible loss concept for supervised learning originates here, not in ReLo. Since RAPID is a supervised (SFT) method, RHO-LOSS is the direct ancestor. ReLo adapted it to RL; RAPID adapts it back to supervised learning but with key differences (EMA reference, multi-granularity, iw-SFT connection).\n\n**Priority 3 — Cite LEAD, DoReMi, DataMIL, DemInf.** These are important for landscape completeness. LEAD is particularly relevant — differentiate by noting LEAD uses exponential smoothing of loss *values* while RAPID uses an EMA *model* to compute reducible loss, which captures more information about what is genuinely learnable vs. noisy.\n\n**Priority 4 — Honestly reposition the novelty.** The gap is not 'no one has used reducible loss for imitation learning' (Re-Mix's excess loss is conceptually identical). The gap is: (a) no sample-level adaptive reducible loss for VLA SFT, (b) no EMA model as adaptive reference (vs. fixed or periodic hard-copy), (c) no multi-granularity trajectory+transition prioritization, (d) no theoretical connection to iw-SFT. Lead with these specific contributions.\n\n**Priority 5 — Address the RL paradigm shift.** SimpleVLA-RL achieves 99% on LIBERO via RL. Discuss why SFT data quality still matters: (a) SFT provides the warm-start for RL, (b) better SFT initialization could make RL more sample-efficient, (c) not all settings allow online interaction for RL, (d) RAPID could potentially be combined with RL post-training. This strengthens the impact argument.\n\n**Estimated effort:** These are all writing/framing changes, not experimental changes. The experimental plan is solid. With these fixes, the paper could target AAAI 2027 or ICRA 2027 competitively.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"FACTUAL: ReLo's target network in SAC uses Polyak averaging (EMA), not periodic hard copy as the proposal claims. The proposal states 'ReLo uses a *periodically hard-copied* target network' — this is inaccurate for SAC-based experiments. Since ReLo already implements EMA-based reducible loss for prioritized sampling (in RL), RAPID's Contribution 1 novelty is narrower than presented. The actual novel contribution is introducing an EMA reference in *supervised/imitation learning* where no target network naturally exists — this should be stated precisely.\", \"MISSING REFERENCE: DS2 — 'Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining' (ICLR 2025, arXiv 2502.06733). This peer-reviewed work at a top venue performs dynamic, instance-level, loss-based sample reweighting during training with a theoretical convergence framework. It is conceptually very close to RAPID's online prioritization mechanism (though it uses raw loss, not reducible loss, and targets LLM pretraining). Should be cited and differentiated — RAPID's reducible loss avoids the noise overfitting issue that DS2's raw-loss approach would face.\", \"ADVERSARIAL EVIDENCE NOT ADDRESSED: 'When Do Curricula Work?' (Wu et al., ICLR 2021) demonstrates that curriculum/prioritized sampling provides only marginal benefits on standard benchmarks with clean data — the apparent benefit is entirely explained by dynamic training set size, not the ordering itself. Benefits emerge only under (1) limited training budget or (2) noisy data. Standard LIBERO uses 50 clean human-teleoperated demos per task — RAPID may show null results there. The noise injection experiment addresses condition (2), but the proposal should acknowledge that gains on clean LIBERO may be minimal and position the noise experiments as the primary validation.\", \"EMA FEEDBACK LOOP: The EMA reference model is derived from the training model itself, creating a potential confirmation bias where the model's systematic errors propagate through the priority signal. Research on EMA teachers in self-distillation (arXiv 2411.18704) shows that even slow EMA updates can amplify epistemic suppression via feedback loops. This risk should be discussed as a limitation and the EMA decay sensitivity ablation (τ ∈ {0.999–0.99999}) should explicitly check for this failure mode.\", \"VENUE MISMATCH: The user explicitly requested CoRL 2026 (abstract May 26, paper May 28 — 13-15 days away). The proposal withdraws from CoRL without offering a minimal viable plan. A focused CoRL submission is tight but potentially feasible: theory (iw-SFT connection) + implementation on OpenVLA-OFT + LIBERO noise injection (primary experiment) + standard LIBERO + 2-3 baselines (uniform, raw-loss priority, fixed-reference ablation). If the researcher has GPU access and OpenVLA-OFT familiarity, this is a 14-day sprint. The user indicated a theory-focused paper without real robot experiments is acceptable — the proposal should at least sketch this option.\", \"THEORETICAL DEPTH: The O(1/√(nη)) vs O(1/√n) convergence rate improvement is a standard importance sampling variance reduction result. The per-step improvement bound under Lipschitz smoothness is straightforward. For ICLR 2027, the iw-SFT connection needs to go beyond standard IS analysis — e.g., prove that the adaptive quality score from EMA-based reducible loss provably tightens the iw-SFT bound more than any static score in a formal PAC-learning or regret-minimization framework, not just claim it intuitively.\"]\nFeedback: The proposal has improved dramatically across 4 rounds — the landscape is now comprehensive, the method is well-motivated, and the experimental plan is thorough. The remaining gap to 'pass' is not about missing references or experimental design, but about the inherent novelty ceiling and impact uncertainty. Here is how to close that gap:\n\n**1. Fix the ReLo characterization (easy, high priority).** ReLo's target network in SAC IS Polyak-averaged (EMA). Claiming 'periodic hard copy' misrepresents the prior art and overstates your novelty. Reframe Contribution 1 as: 'We introduce an EMA reference model for reducible loss computation in supervised/imitation learning, where no target network naturally exists. Unlike RL (ReLo), where the target network serves double duty for TD learning stability and reducible loss, RAPID's EMA reference is purpose-built for data quality scoring.' This is still a valid contribution — just be precise.\n\n**2. Offer a CoRL 2026 minimal plan (important for user requirements).** Even if risky, sketch a focused 14-day plan: (a) formalize iw-SFT theory (3 days), (b) implement EMA reference + reducible loss on OpenVLA-OFT (3 days), (c) run LIBERO noise injection (3 corruption types × 2 ratios, 3 baselines — 4 days), (d) standard LIBERO as secondary (2 days), (e) write paper (4 days, overlapping). Drop OXE, LIBERO-Plus, UDS baseline, and extensive ablations — save those for AAAI 2027 if CoRL is rejected. The user said a theory-focused paper is acceptable.\n\n**3. Acknowledge the clean-data limitation explicitly.** On standard LIBERO (97% baseline, clean data), RAPID may show minimal gains based on the 'When Do Curricula Work?' finding. Position the noise injection and LIBERO-Plus experiments as primary evidence, with standard LIBERO as a 'does no harm' sanity check. This honest framing is stronger than over-claiming.\n\n**4. Deepen the iw-SFT theory (for ICLR consideration).** The convergence rate claim is standard IS. To make the theory the genuine centerpiece: (a) prove a formal regret bound showing that adaptive reference strictly dominates static reference under mild assumptions on loss landscape dynamics, (b) connect the EMA decay rate τ to the optimal IS proposal distribution tracking rate, (c) derive the conditions under which RAPID's adaptive quality score achieves the minimax optimal convergence rate for the class of smooth loss functions.\n\n**5. Cite DS2 (ICLR 2025).** One sentence: 'DS2 demonstrates that dynamic instance-level loss-based reweighting improves LLM pretraining convergence with theoretical guarantees; however, DS2 uses raw loss and does not decompose reducible vs. irreducible components, inheriting the noise overfitting risk identified by RHO-LOSS.' This strengthens your positioning.\n\n**6. Discuss EMA feedback risk as a limitation.** Acknowledge that the EMA reference is not independent of the training model. The τ ablation partially addresses this — extreme values of τ (very high = near-copy, very low = near-identity) should reveal the failure mode if present.\n\n**Bottom line:** The proposal is competitive for ICRA 2027 and likely AAAI 2027 as-is. For CoRL 2026, a focused sprint is feasible if the user prioritizes it. For ICLR 2027, the theory needs genuine depth beyond standard IS analysis. The main bottleneck to 'pass' is that novelty and impact are both at 3/5 — fixing the ReLo characterization, adding DS2, and offering a CoRL plan would not change these scores, but deepening the theory or adding a surprising experimental finding (e.g., RAPID-initialized policies converge 2x faster with SimpleVLA-RL) would.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"THEORETICAL CONCERN: Theorem 1's O(T) vs Ω(T²) asymptotic advantage assumes 'non-trivial policy drift during training,' but VLA SFT typically runs for 1-3 epochs over ~500 demonstrations with small learning rates. The cumulative drift may be insufficient for the asymptotic separation to manifest in practice. The proposal should either (a) derive finite-T bounds showing the advantage at realistic training horizons, or (b) empirically demonstrate the bound gap grows across training for their actual experimental setup.\", \"IMPACT GAP: The RAPID+RL complementarity is the strongest impact argument ('SFT accounts for 74pp of 82pp total improvement in SimpleVLA-RL') but is left as future work. Even a small experiment showing RAPID-initialized SFT → SimpleVLA-RL outperforms vanilla SFT → SimpleVLA-RL would dramatically strengthen the paper's impact argument and address the 'RL makes SFT quality irrelevant' concern.\", \"FEASIBILITY RISK: The CoRL sprint plan lists 18 noise-injection runs + 12 standard LIBERO runs = 30 runs. At ~120h per OpenVLA-OFT training run (even with speedups), this requires substantial parallel GPU capacity within 9 experiment days (Days 4-9). With 8×A100, that's ~450 GPU-hours/day sustained, which is feasible only with near-perfect pipeline automation and zero debugging time. The plan should identify a minimum viable experiment set (~12-15 runs) that validates the core claim.\", \"MINOR MISSING REFERENCES: (a) Green-VLA's DataQA pipeline (arXiv Feb 2026, 2602.00919) — a VLA-specific static data curation pipeline using quality metrics, relevant as a concurrent VLA data curation method. (b) VLA-OPD (arXiv March 2026, 2603.26666) — bridges offline SFT and online RL for VLAs via on-policy distillation, relevant to the SFT+RL complementarity discussion.\", \"THEOREM 3 PRACTICAL ASSUMPTION: The noise filtering guarantee assumes irreducibly noisy transitions maintain high loss for all θ (L_θ(i) ≥ σ²). For VLA action prediction with L1 loss, moderate action noise (σ ∈ {0.05, 0.1}) may not produce persistently high loss — high-capacity VLMs can partially fit noise, especially in low-dimensional action spaces. The guarantee should specify assumptions on noise magnitude relative to the model's fitting capacity.\", \"VENUE FIT: CoRL historically favors papers with strong empirical contributions, often including real-robot experiments or compelling simulation results. A theory-focused paper with limited simulation experiments (the fallback plan) may face a venue mismatch. The proposal should consider whether the CoRL sprint can reliably produce sufficient empirical evidence, or whether targeting AAAI 2027 as the primary venue with CoRL as a stretch goal is more honest.\"]\nFeedback: The proposal has improved dramatically across 5 rounds and the landscape analysis is now world-class — I found no significant missing competitive work that isn't already cited. The method is sound, the positioning is honest, and the theoretical framing is well-motivated. However, the average score (3.5) remains below the 4.0 threshold due to inherent novelty and impact ceilings. Here's how to close the gap:\n\n**1. Add a RAPID+RL experiment (highest priority for impact).** This is the single most impactful addition. SimpleVLA-RL's SFT stage accounts for 74pp of 82pp total improvement. Run: (a) vanilla SFT → RL, (b) RAPID SFT → RL, on 2-3 LIBERO-Long tasks. Even a small improvement in RL convergence speed or final performance would transform the paper's impact narrative from 'another data curation method' to 'better SFT initialization for the entire VLA training pipeline.' This directly addresses the RL post-training trend concern.\n\n**2. Derive finite-T bounds for Theorem 1.** The O(T) vs Ω(T²) asymptotic result is elegant but may not manifest in short VLA SFT runs. Derive a bound like: 'For T ≥ T₀(ε, τ), the adaptive reference achieves at least X% tighter bound than the best static reference.' This makes the theory practically relevant and directly testable.\n\n**3. Reduce the CoRL experiment scope to minimum viable.** Cut to: (a) noise injection on LIBERO-Long only (3 corruption types × 1 ratio = 3 configs × 3 methods = 9 runs), (b) standard LIBERO-Long as sanity check (3 runs), (c) 1 key ablation: EMA vs fixed reference (3 runs). Total: ~15 runs, feasible with 4×A100 in 7 days. This validates the core claim (reducible > raw loss on noisy data) and Theorem 1 (adaptive > static reference).\n\n**4. Cite Green-VLA DataQA and VLA-OPD.** Minor additions to an already comprehensive landscape.\n\n**5. For the full AAAI version:** Add LIBERO-Plus robustness evaluation, OXE mixed-quality experiments, and the RAPID+RL experiment. This is where the paper can become genuinely compelling.\n\n**Bottom line:** The proposal is at its structural ceiling — further revision of positioning or landscape won't change scores. What's needed is experimental evidence (especially RAPID+RL) and finite-T theoretical results to push novelty and impact from 3 to 4.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MISSING REFERENCE: 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' (ICML 2026, poster). This paper directly studies how SFT technique quality affects downstream RL performance — showing 7.09% RL improvement and 11.54% reduced forgetting via token-level clipping. While it operates on LLMs (ALFWorld, ScienceWorld) at the token level rather than VLA data level, it establishes the same principle as RAPID's Contribution 4 ('SFT quality cascades to RL'). Must be cited. RAPID's differentiation: (a) data/demonstration-level filtering vs. token-level clipping, (b) VLA domain with action-prediction loss vs. LLM domain with language loss, (c) noise filtering mechanism vs. trust-region mechanism. This weakens the claim of 'first to study SFT quality → RL' — reframe as 'first to study SFT *data quality* → RL for *VLAs*.'\", \"NOVELTY NARROWING: iw-SFT (arXiv 2507.12856) already implements EMA update θ_q = α·θ_q + (1-α)·θ for continuous control (D4RL) experiments. The proposal's Contribution 1 claims 'RAPID introduces a purpose-built EMA reference specifically designed for data quality scoring' as if no EMA reference exists in supervised/IL settings — but iw-SFT uses exactly this mechanism for updating the auxiliary distribution q in continuous control SFT/BC. The critical distinction: iw-SFT uses EMA for trajectory-level importance weights (multiplicative loss reweighting), while RAPID uses EMA for *reducible loss computation* + *PER-style sampling priorities*. This distinction is real but must be articulated precisely. Reframe: 'iw-SFT proposed EMA for importance weighting; we use EMA for reducible loss decomposition, revealing that the EMA reference enables noise-robust prioritization beyond what importance weighting alone provides.'\", \"CoRL TIMELINE: 13 days to abstract deadline (May 26), 16 days to paper deadline (May 29). The proposal should include an explicit go/no-go decision point: if the first noise-injection experiment results are not available by ~May 22-23, fall back to AAAI 2027 only. The abstract deadline requires at least preliminary results to write a credible abstract.\", \"FINITE-T TESTABILITY: Corollary 1.1 predicts T₀ = C₁/(C₂·Δ₀·ε) falls within 'thousands of steps' for τ* = 0.978. However, the constants C₁, C₂ depend on loss landscape properties (Lipschitz constant M, gradient bound ε) that are difficult to estimate a priori for VLA models. The empirical crossover point may differ by an order of magnitude from the theoretical prediction. The proposal should acknowledge this uncertainty and frame the empirical bound-gap measurement as a test of the theory's qualitative prediction (linear vs quadratic growth) rather than its quantitative prediction (exact T₀).\", \"NOISE INJECTION VS REAL-WORLD NOISE: The primary experiment uses synthetic corruption (Gaussian noise, frame dropping, truncation). Real-world demonstration noise (hesitation, redundant motions, suboptimal strategies, operator fatigue) has fundamentally different structure — it's *coherent* noise that may be harder for reducible loss to detect. The OXE experiment (deferred to AAAI) would address this. For CoRL, acknowledge this limitation explicitly and frame noise injection as a controlled test of the mechanism, not a claim about real-world robustness.\"]\nFeedback: The proposal has reached an exceptionally high level of polish and the landscape analysis is now world-class. The remaining gap to 'pass' (avg 3.5 vs 4.0 threshold) reflects inherent novelty and impact ceilings rather than fixable oversights. Here is how to close the gap:\n\n**1. Cite and differentiate from ICML 2026 clipping paper (easy, high priority).** 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' establishes that SFT technique → RL performance in LLMs. RAPID's differentiation is clear: (a) data-level noise filtering vs. token-level trust region, (b) VLA domain vs. LLM domain, (c) prioritized sampling vs. gradient clipping. Frame RAPID as: 'The ICML 2026 work shows SFT technique affects RL for LLMs; we show SFT *data quality* affects RL for VLAs — a complementary finding in a different domain with a different mechanism.'\n\n**2. Sharpen iw-SFT differentiation (important).** iw-SFT already uses EMA for continuous control. RAPID's actual novelty over iw-SFT is threefold: (a) reducible loss decomposition (iw-SFT uses trajectory probabilities for importance weights, RAPID uses loss difference for noise-robust prioritization), (b) PER-style sampling (iw-SFT reweights loss multiplicatively, RAPID controls which samples are seen), (c) theoretical analysis of optimal τ and finite-T crossover. State this explicitly rather than claiming EMA reference as wholly novel.\n\n**3. The path to pushing impact from 3→4.** The single most impactful result would be a compelling RAPID+RL experiment showing e.g. 30-50% fewer RL steps to reach 90% success. If this materializes, lead the paper with it. The narrative becomes: 'SFT data quality is the hidden bottleneck of VLA RL pipelines; RAPID provides a drop-in fix.' This is more impactful than 'another data curation method for noisy demonstrations.'\n\n**4. Consider whether CoRL is the right target.** With 13 days to abstract, the risk of a rushed submission is high. The AAAI 2027 timeline (3+ months) allows comprehensive experiments including LIBERO-Plus and OXE, which would strengthen impact significantly. A well-executed AAAI paper with the RAPID+RL finding as headline result + robustness on LIBERO-Plus + OXE mixed-quality is stronger than a rushed CoRL submission. If you attempt CoRL, treat it as a stretch with explicit go/no-go by May 22.\n\n**5. For the next revision, focus on sharpening rather than expanding.** The proposal is comprehensive but very long. The landscape analysis is thorough but could be tightened. Every additional reference and caveat adds length but diminishing returns on clarity. The core story is: 'EMA-based reducible loss enables noise-robust, adaptive data prioritization for VLA SFT, and this cascades to faster RL convergence.' Everything should serve this narrative.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T11:39:05.932Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T11:39:05.932Z",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

## Round 1

176 recorded events

### User

_source line 3 · 2026-05-13T11:39:05.977Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-13 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).
Direction：因为真实数据采样的时候会有很多噪声，比如收集时的冗余动作等，如何避免训练数据中的噪声影响vla的训练，可以使用一个经验池的形式来训练，借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选，再适当过滤掉一些低分数的冗余动作，如果是从一些底层理论角度提出了筛选方法 感觉不用真机也是可以接受的**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?
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
  "title": "RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Learning",
  "core_problem": "Does SFT data quality — which demonstrations are prioritized during training — affect downstream RL outcomes for vision-language-action models? The VLA training paradigm is shifting from SFT-only to SFT→RL pipelines, where SFT quality is the critical determinant of RL success. SimpleVLA-RL shows SFT data *quantity* gates RL (0 demos → 0% RL success), but no work has isolated how SFT data *quality* affects RL convergence and final performance. Multiple recent works study how SFT *technique* affects RL (gradient clipping, trust regions, distribution alignment), but none address the orthogonal question of data-level filtering. RAPID provides the mechanism to test this: by decomposing per-sample loss into reducible (learnable) and irreducible (noise) components via an EMA reference model, it prioritizes high-signal demonstrations during SFT, producing cleaner checkpoints for downstream RL. The core hypothesis is that noise-filtered SFT → faster RL convergence and better sample efficiency, particularly in realistic settings where demonstration quality varies.",
  "opportunity": "Three converging trends create this opening:\n\n**1. SFT→RL pipelines are standard but SFT data quality's RL effect is unstudied.** SimpleVLA-RL (ICLR 2026) shows SFT accounts for 74pp of 82pp total improvement and SFT quantity gates RL success. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows warm-start SFT yields ~50% faster RL convergence. A growing body of work now demonstrates that SFT *technique* matters for downstream RL: the ICML 2026 'Off-Policy Token Clipped SFT' (Tian-Shuo Liu et al.) shows token-level gradient clipping during SFT yields 7.09% RL improvement and 11.54% reduced forgetting on LLM agentic benchmarks; PSFT (arXiv 2508.17784) applies PPO-style clipped surrogates to SFT; DFT (ICLR 2026, 2508.05629) dynamically rescales the SFT objective; 'Tailored Primitive Initialization' (arXiv 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning; PRISM (arXiv 2604.28123) aligns SFT and RL distributions via on-policy distillation. Yet none study how *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs. RAPID fills this gap with data-level noise filtering rather than token/objective-level modifications.\n\n**2. Reducible loss decomposition is proven but unexploited in VLA SFT.** RHO-LOSS (ICML 2022) showed excess loss identifies learnable-not-yet-learnt data, achieving 18x speedup on noisy datasets. ReLo (NeurIPS 2023) adapted this to RL using SAC's pre-existing target network. Rho-1 (NeurIPS 2024) brought it to LLM pretraining with a fixed reference. iw-SFT (arXiv 2507.12856) uses an EMA reference for importance-weighted SFT in continuous control — but for trajectory-level importance weights approximating on-policy gradients, not for reducible loss decomposition. RAPID uses the EMA for a different purpose: computing R(x) = max(0, L_θ(x) − L_EMA(x)) to decompose loss into reducible and irreducible components. The max(0,·) clamp provides explicit noise suppression that importance weighting lacks. DS2 (ICLR 2025) performs dynamic instance-level reweighting but uses raw loss without reducible decomposition, inheriting noise overfitting risk. No existing work applies sample-level, continuously-adaptive reducible-loss *prioritized sampling* to VLA SFT.\n\n**3. VLA demonstration quality varies in practice.** The 'When Do Curricula Work?' finding (ICLR 2021) that curricula provide marginal benefits on clean benchmarks implies RAPID's value is in noisy/mixed-quality settings and the SFT→RL pipeline — not clean-data benchmarks where VLAs already achieve 97%+. LIBERO-Plus (CVPR 2026) exposed that high success rates on standard LIBERO mask fragility (OpenVLA-OFT: 97.1% → 70.0%). Real-world datasets (OXE, DROID) contain heterogeneous demonstration quality from varied operators. RAPID targets these realistic conditions.\n\n**The specific gap (honestly stated):** iw-SFT already uses EMA for continuous control importance weighting. RAPID's novelty over iw-SFT is threefold: (a) reducible loss decomposition (not trajectory probabilities for importance weights), providing noise-robust prioritization via the max(0,·) clamp; (b) PER-style sampling (controlling which samples are seen, not multiplicative loss reweighting); (c) training-horizon-aware τ calibration with finite-T theory. Furthermore, no work — including all SFT-technique-for-RL papers — has tested whether SFT *data quality via noise filtering* affects downstream RL for VLAs.",
  "landscape": "**Reducible/excess loss foundations:** RHO-LOSS (ICML 2022) selects points by excess loss over a fixed holdout-trained reference — 18x faster on noisy Clothing-1M. ReLo (NeurIPS 2023) computes reducible TD error using SAC's Polyak-averaged target network (double duty: TD stability + data scoring). Rho-1 (NeurIPS 2024) brings excess loss to LLM pretraining with a fixed reference for selective token training. All supervised applications use *static* reference models.\n\n**Dynamic instance-level reweighting:** DS2 (ICLR 2025) normalizes per-sample losses and applies transformation functions for dynamic reweighting during LLM pretraining, with formal convergence guarantees. Uses raw loss without reducible decomposition. LEAD (arXiv May 2025) uses EMA over *loss values* (not model parameters) for online data selection during LLM SFT. UDS (arXiv Oct 2025) uses nuclear norm of logits for utility-diversity batch selection without a reference model.\n\n**Importance-weighted SFT:** iw-SFT (arXiv Jul 2025, 2507.12856) proves SFT on curated data optimizes a lower bound on the RL objective. For continuous control (D4RL), it uses an EMA reference (θ_q = α·θ_q + (1-α)·θ) for trajectory-level importance weights. For LLMs, it uses discrete time-lagged updates. Critical distinction from RAPID: iw-SFT uses EMA for importance weighting (multiplicative loss scaling approximating on-policy gradients); RAPID uses EMA for reducible loss decomposition (R = max(0, L_θ − L_EMA)) with PER-style sampling priorities, providing noise robustness absent in importance weighting.\n\n**Domain-level data mixing:** DoReMi (NeurIPS 2023) uses excess loss with Group DRO for LLM domain mixing. Re-Mix (CoRL 2024) extends this to robot IL with domain-level weights over OXE datasets using a fixed reference. Both operate at domain level, not sample level.\n\n**Static demonstration curation:** SCIZOR (ICRA 2026) uses self-supervised progress prediction. CUPID (CoRL 2025) uses influence functions. RINSE (ICML 2025) uses smoothness metrics. DataMIL (ICLR 2026) uses datamodels. DemInf (RSS 2025) uses k-NN mutual information. All score data once before training — static preprocessing that cannot adapt to the policy's evolving learning needs.\n\n**SFT technique → RL quality (NEW — critical related work):** Off-Policy Token Clipped SFT (Tian-Shuo Liu et al., ICML 2026 poster) clips gradient updates from low-probability tokens during SFT, acting as a trust region that reduces forgetting (11.54%) and improves downstream RL (7.09%) on ALFWorld/ScienceWorld. PSFT (arXiv Aug 2025, 2508.17784) applies PPO-style clipped surrogates to SFT for generalization. DFT (ICLR 2026, 2508.05629) dynamically rescales SFT gradients based on token probability. Tailored Primitive Initialization (arXiv Nov 2025, 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning. PRISM (arXiv Apr 2026, 2604.28123) inserts on-policy distillation between SFT and RL to repair distributional drift. All operate on *techniques* (gradient clipping, objective modification, distribution alignment) rather than *data quality* (which demonstrations to prioritize).\n\n**RL post-training for VLAs:** SimpleVLA-RL (ICLR 2026) achieves 99.1% on LIBERO via GRPO post-training. SFT accounts for 74pp of 82pp improvement; Section 6.2 ablates quantity (not quality). VLA-OPD (arXiv Mar 2026) bridges offline SFT and online RL via on-policy distillation. VLA-RFT uses a learned world model for RL.\n\n**Curricula effectiveness:** 'When Do Curricula Work?' (ICLR 2021 Oral) shows curriculum benefits are marginal on clean data — gains come only under limited budget or noisy data. Critical calibration for RAPID's claims.\n\n**EMA dynamics and memorization:** EMA models show improved robustness to noisy labels (arXiv 2411.18704) but are not independent of the training model. Self-distillation feedback loops can amplify errors (arXiv 2603.24472). Zhang et al. (ICLR 2017) and Kajitsuka & Sato (ICLR 2025) show high-capacity models can memorize noise, so noise suppression cannot assume persistently high loss on noisy samples.\n\n**The gap:** Multiple works study SFT *technique* for RL (gradient clipping, trust regions, objective rescaling, distribution alignment). iw-SFT uses EMA for importance weighting in continuous control. No existing work applies sample-level reducible-loss prioritized sampling to VLA SFT, and no work tests whether SFT data quality via noise-filtering prioritization affects downstream RL for VLAs.",
  "approach": "**Method overview.** RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations) replaces uniform sampling during VLA SFT with online, noise-robust prioritized sampling based on reducible loss. Beyond improving SFT in isolation, RAPID targets the SFT stage that initializes downstream RL — the paper's primary contribution is the empirical finding that SFT data quality cascades to RL outcomes.\n\n**Contribution 1: EMA-based reducible loss for VLA SFT.** RAPID computes reducible loss R(x) = max(0, L_θ(x) − L_EMA(x)), where L is action-prediction loss and θ_EMA ← τ·θ_EMA + (1−τ)·θ is updated every gradient step. *Honest positioning:* iw-SFT (2507.12856) proposed EMA for importance weighting in continuous control; RAPID uses EMA for a different purpose — reducible loss decomposition that provides noise-robust prioritization. The key mechanism is the max(0,·) clamp: noisy samples that the model cannot fit have L_θ ≈ L_EMA → R ≈ 0; noisy samples the model gradually memorizes have L_θ ≤ L_EMA → R = 0. Both regimes suppress noise. This decomposition cannot be replicated by raw-loss methods (DS2, SuRe) which assign high weight to noisy samples. Compared to LEAD's EMA over loss values, RAPID's EMA over model parameters captures richer structural information.\n\nSampling: transitions drawn proportionally to R(x)^α with importance-sampling correction β-annealed from 0→1 (Schaul et al. 2016). Priorities refreshed every K=500 steps (~8-12% compute overhead). Two-level sampling: trajectory priority = mean reducible loss (inter-demonstration), transition priority = per-step reducible loss (intra-demonstration).\n\n**Contribution 2: Training-horizon-aware τ calibration (theoretical support).** We analyze the bias-variance tradeoff in τ: tracking error scales as O(ε·τ/(1-τ)), signal quality scales similarly. The product is maximized at τ* = 1 − Θ(√ε). For VLA SFT (ε ≈ 5×10⁻⁴), τ* ≈ 0.978. Within the iw-SFT framework, the adaptive EMA reference achieves O(T) cumulative bound gap vs Ω(T²) for static references. *Testability caveat:* the constants in these bounds depend on loss landscape properties (Lipschitz constant, gradient bound) that are hard to estimate a priori. We frame the empirical bound-gap measurement as testing the theory's *qualitative* prediction (linear vs quadratic growth) rather than the *quantitative* crossover point T₀. The noise suppression guarantee is reformulated to handle high-capacity VLM memorization: relative suppression ratio O(1−τ) ≈ 0.022 for τ* = 0.978. Ablation over τ ∈ {0.97, 0.99, 0.995, 0.999, 0.9999} validates the theory and identifies failure modes at both extremes.\n\n**Contribution 3 (PRIMARY): RAPID+RL pipeline — SFT data quality → RL outcomes for VLAs.** The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL convergence for VLAs. *Differentiation from ICML 2026 clipping paper:* that work shows token-level gradient clipping during SFT improves downstream RL for LLMs on text-based agentic tasks; we show data-level noise filtering during SFT improves downstream RL for VLAs on robotic manipulation — complementary findings across domains and mechanisms. Protocol: (a) Vanilla SFT → GRPO (SimpleVLA-RL), (b) RAPID SFT → GRPO, on LIBERO-Long with 25% noise injection. Also test fixed-reference SFT → GRPO to validate that RAPID's *adaptive* filtering provides the RL benefit. Metrics: RL convergence speed (steps to 90% success), final success rate, total environment interactions. Even a modest improvement (e.g., 30-50% fewer RL steps) is practically significant given expensive RL environment interactions.\n\n**Experimental plan.** Built on OpenVLA-OFT (open-source).\n\n*Experiment 1 (Primary — Noise injection SFT):* Corrupt LIBERO-Long demonstrations at 10%, 25%, 50% with three corruption types: Gaussian action noise, random frame dropping, trajectory truncation. Pre-pilot to ensure baseline degrades to 60-80%. Baselines: uniform, raw-loss priority, DS2-adapted, fixed-reference reducible loss. *Limitation acknowledged:* synthetic corruption is a controlled test of the mechanism, not a claim about real-world robustness. Real-world noise (hesitation, suboptimal strategies, operator fatigue) is coherent and structurally different. The OXE experiment (Experiment 4) addresses this.\n\n*Experiment 2 (Primary — RAPID+RL pipeline):* 2-3 LIBERO-Long tasks with 25% noise. Four conditions: {Vanilla SFT, RAPID SFT, Fixed-reference SFT} × GRPO. RL stage uses SimpleVLA-RL (open-source, ~400 gradient steps, computationally cheap).\n\n*Experiment 3 (Sanity — Standard LIBERO-Long):* Clean data, expecting minimal gains per 'When Do Curricula Work?' analysis. Demonstrates RAPID does no harm.\n\n*Experiment 4 (AAAI — OXE mixed-quality):* Real-world heterogeneous quality, following SCIZOR/Re-Mix setup. Addresses the synthetic noise limitation.\n\n*Experiment 5 (AAAI — LIBERO-Plus robustness):* Tests whether noise filtering extracts more robust representations.\n\n**CoRL 2026 minimum viable plan (abstract May 26, paper May 29).** GO/NO-GO BY MAY 22: if first noise-injection + RL results are not available, fall back to AAAI 2027 only. CoRL scope: Experiments 1-3 (15 SFT runs + 4 RL runs ≈ 950 GPU-hours). Lead with RAPID+RL finding as headline. Risk: SimpleVLA-RL integration with RAPID checkpoints is untested.\n\n**AAAI 2027 (primary target, deadline ~Aug 2026).** Full version: all 5 experiments, complete ablation suite (τ, K, α, β), all baselines including CUPID and SCIZOR, comprehensive theory validation (qualitative bound gap growth, noise suppression ratios). This is the definitive version.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~3500h A100-80GB (noise injection: 3 types × 3 ratios × ~80h = ~720h + RAPID+RL: 6 RL runs × ~50h = 300h + LIBERO-Plus: ~200h eval + standard LIBERO-Long: 4 methods × 80h = 320h + OXE: ~400h + baselines ~600h + ablations ~500h + theory validation ~100h)",
      "gpu_utilization": "~25-35% effective utilization",
      "timeline": "10-14 weeks (full AAAI version); 14 days (CoRL sprint with go/no-go by May 22)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$5,250 at ~$1.50/hr (full version); ~$1,425 for CoRL sprint (950h)"
    },
    "human_in_loop": {
      "gpu_hours": "~5000h A100-80GB",
      "gpu_utilization": "~60-70% utilization",
      "timeline": "6-8 weeks (full version); 10-12 days (CoRL sprint)",
      "team": "1 researcher, ~30-45min/day",
      "claude_api_cost": "$300-500",
      "estimated_gpu_cost": "~$7,500 (full); ~$2,000 (CoRL sprint)",
      "risk_note": "SimpleVLA-RL integration with RAPID SFT checkpoints is untested. May 22 go/no-go decision critical."
    },
    "auto_research": {
      "gpu_hours": "~6500-7500h A100-80GB",
      "gpu_utilization": "~90-95%",
      "timeline": "16-24 days with 8×A100",
      "team": "0 (initial setup and final review only)",
      "claude_api_cost": "$600-1000",
      "estimated_gpu_cost": "~$11,000",
      "speed_bottleneck": "GPU cluster availability; SimpleVLA-RL environment rollouts",
      "risk_note": "Agent may over-explore τ-K interaction space; ~15-20% wasted compute risk without human calibration"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26, paper May 29 — GO/NO-GO BY MAY 22: fall back to AAAI-only if first noise-injection + RL results unavailable; empirical focus with RAPID+RL headline, 15 SFT + 4 RL runs ≈ 950h)",
    "AAAI 2027 (deadline ~Aug 2026 — primary target for full version with all experiments, theory, OXE, LIBERO-Plus)",
    "ICRA 2027 (deadline ~Sep 2026 — fallback if CoRL infeasible, strong robot learning venue fit)",
    "ICLR 2027 (deadline ~Sep-Oct 2026 — only if finite-T theory validates empirically and RAPID+RL finding is compelling)"
  ],
  "level": "solid",
  "key_references": [
    "Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt [RHO-LOSS] (ICML 2022)",
    "Prioritized Experience Replay (ICLR 2016)",
    "Prioritizing Samples in Reinforcement Learning with Reducible Loss [ReLo] (NeurIPS 2023)",
    "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)",
    "Not All Tokens Are What You Need [Rho-1] (NeurIPS 2024)",
    "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)",
    "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining [DS2] (ICLR 2025)",
    "Supervised Fine Tuning on Curated Data is Reinforcement Learning [iw-SFT] (arXiv Jul 2025, 2507.12856)",
    "LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning (arXiv May 2025)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)",
    "RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025)",
    "DemInf: Robot Data Curation with Mutual Information Estimators (RSS 2025)",
    "When Do Curricula Work? (ICLR 2021)",
    "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (ICML 2026 poster)",
    "Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025, 2508.17784)",
    "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026, 2508.05629)",
    "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025, 2511.12429)",
    "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026, 2604.28123)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)",
    "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)",
    "What Can RL Bring to VLA Generalization? (NeurIPS 2025)",
    "VLA-OPD: Bridging Offline SFT and Online RL for VLAs via On-Policy Distillation (arXiv Mar 2026)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)",
    "Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits (arXiv Nov 2024)",
    "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv Mar 2026)",
    "Understanding Deep Learning Requires Rethinking Generalization (Zhang et al., ICLR 2017)",
    "On the Optimal Memorization Capacity of Transformers (Kajitsuka & Sato, ICLR 2025)",
    "SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv Nov 2025)",
    "Density-Ratio Weighted Behavioral Cloning (arXiv Oct 2025)",
    "Token Priority SFT (arXiv Feb 2026)",
    "UDS: Utility-Diversity Aware Online Batch Selection for LLM SFT (arXiv Oct 2025)"
  ],
  "description": "We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which replaces uniform sampling during VLA supervised fine-tuning with online, noise-robust prioritized sampling based on reducible loss — and provides the first empirical test of whether SFT data quality cascades to downstream RL outcomes for VLAs.\n\nRAPID makes three contributions:\n\n(1) **EMA-based reducible loss for VLA SFT**: Computes R(x) = max(0, L_θ(x) − L_EMA(x)) to decompose loss into learnable and irreducible components. Honest positioning: iw-SFT (2507.12856) uses EMA for importance weighting in continuous control; RAPID uses EMA for reducible loss decomposition with PER-style sampling, providing noise robustness via the max(0,·) clamp that importance weighting lacks. Training-horizon-aware τ calibration (τ* = 1 − Θ(√ε) ≈ 0.978) connects EMA decay to learning rate, with finite-T bounds predicting O(T) vs Ω(T²) cumulative gap over static references — framed as a qualitative prediction validated empirically.\n\n(2) **Noise-robust SFT on mixed-quality demonstrations**: Controlled noise injection experiments (Gaussian action noise, frame dropping, trajectory truncation) on LIBERO-Long validate that reducible loss decomposition outperforms raw-loss methods and static curation on noisy data. Acknowledges synthetic corruption as a controlled mechanism test; OXE experiments (AAAI version) address real-world heterogeneity.\n\n(3) **RAPID+RL pipeline validation (primary contribution)**: The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL for VLAs. Differentiation from the ICML 2026 'Off-Policy Token Clipped SFT' paper: that work shows token-level gradient clipping during SFT improves RL for LLMs; we show data-level noise filtering during SFT improves RL for VLAs — complementary findings across domains and mechanisms. Tests RAPID SFT → SimpleVLA-RL GRPO vs vanilla SFT → GRPO, measuring RL convergence speed and sample efficiency.\n\nCoRL 2026 is a stretch goal (go/no-go by May 22); AAAI 2027 is the primary target with full experiments including LIBERO-Plus robustness and OXE mixed-quality.",
  "project_name": "adaptive_replay_vla",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: VACO (Value-Aligned Behavior Cloning, ICLR 2025) uses a meta-scoring network + value function to adaptively weight BC demonstrations during training via bi-level optimization. This is the closest existing work and is not cited or discussed. The generator must explicitly differentiate APER from VACO and justify why TD-error-based PER sampling is superior to learned meta-weights.", "CRITICAL: ReLo (NeurIPS 2023) demonstrated that TD-error-based prioritization frequently samples noisy/unlearnable data points with persistently high loss, hindering learning. The proposed approach uses raw TD error magnitude as the priority signal, which is known to be a flawed proxy. The paper must address how APER avoids this well-documented failure mode—reducible loss or similar corrections should be considered.", "CRITICAL: Hindsight goal relabeling is designed for goal-conditioned settings where goals are states (e.g., images). VLA models operate with natural language instructions as goals. How does one perform hindsight relabeling of language goals? This is a non-trivial technical challenge (requires captioning achieved states as language goals) that is completely unspecified.", "MISSING RELATED WORK: SuRe (Surprise-Driven Prioritised Replay, NeurIPS-submitted 2025) applies NLL-based prioritized replay to LLM continual learning. Token Priority SFT (arXiv Feb 2026) formalizes SFT as granular importance sampling. iw-SFT (arXiv Jul 2025) shows SFT on curated data is RL. These concurrent works significantly narrow the novelty claim.", "FEASIBILITY: The experimental plan requires reproducing 5 baselines across 3 benchmarks with ablations in under 20 days. Demo-SCORE requires training a policy, generating online rollouts, training a classifier, and filtering—this alone could take days to reproduce. The scope should be reduced to ensure quality over quantity.", "THEORETICAL WEAKNESS: For a sim-only CoRL paper, the theoretical contribution is thin. The paper should provide formal analysis (e.g., convergence guarantees, sample complexity bounds, or formal connection between TD error and demonstration quality under specific assumptions) to compensate for the lack of real-robot experiments.", "COST REALISM: The manual mode estimates ~500h A100 GPU hours, but with 5 baselines × 24h each on 8 GPUs, that alone is 960 GPU-hours. The estimate appears to undercount baseline reproduction costs significantly."]
Feedback: The core intuition (adaptive > static data curation for VLA SFT) is reasonable, but the execution plan has critical gaps. Here's how to strengthen the idea:

1. **Address VACO directly**: Read VACO (ICLR 2025) carefully and position APER as an improvement. Potential differentiators: VACO requires bi-level optimization (expensive), APER uses simpler PER sampling; VACO targets offline RL, APER targets imitation learning SFT. But you must demonstrate empirically or theoretically why your approach is better.

2. **Fix the TD error proxy problem**: Replace raw TD error with reducible loss (ReLo, NeurIPS 2023) or a learned quality score. Alternatively, combine TD error with a noise detector (e.g., consistency across recomputation) to filter out irreducibly-noisy transitions. This would actually strengthen the novelty.

3. **Solve language-conditioned hindsight relabeling**: Either (a) use a VLM to caption achieved goal states as language instructions for relabeling, (b) operate in embedding space rather than language space, or (c) use action-prediction loss as the priority signal instead of TD error, removing the need for a separate value function entirely. Option (c) would simplify the method considerably—high-loss transitions are 'surprising' to the current policy, similar to TD error but without the auxiliary value function.

4. **Reduce scope for CoRL deadline**: Drop Demo-SCORE and DataMIL baselines (keep SCIZOR and CUPID as strongest competitors + uniform). Focus on LIBERO only (4 suites are sufficient). Add 1-2 targeted ablations rather than 10. This makes the timeline realistic.

5. **Strengthen theory**: Prove a formal connection between TD-error-based priority and the expected improvement in policy performance per gradient step (sample efficiency bound). Even a simplified analysis under assumptions would strengthen a sim-only paper.

6. **Consider the simpler alternative**: Using the policy's own prediction loss as the priority signal (high-loss = surprising = prioritize) would be simpler, avoid the need for a separate value function, and directly address the 'policy-aware' motivation. This might actually be a cleaner contribution.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: LIBERO benchmark saturation. OpenVLA-OFT achieves 96.2/98.3/96.2/90.7% per suite. Only LIBERO-Long has meaningful headroom at 90.7%. PLD achieves 99% (with RL). Showing statistically significant improvement from ~97% → 98% requires many evaluation seeds and the gains are not compelling. The generator must either: (a) add experiments on noisier/more diverse datasets where data quality matters more (e.g., OXE subsets, mixed-quality demonstrations), (b) design controlled noise injection experiments to demonstrate RAPID's noise-robustness advantage, or (c) adopt LIBERO-Plus/LIBERO-PRO which test robustness under perturbation and have more headroom.", "CRITICAL: Motivation-experiment mismatch. The core motivation is filtering noise from real-world demonstrations ('真实数据采样的时候会有很多噪声，比如收集时的冗余动作'), but LIBERO uses 50 high-quality human-teleoperated demos per task. These are relatively clean — the noise/redundancy that RAPID targets may be insufficient to demonstrate meaningful gains. The experimental design must include a scenario with genuinely noisy or heterogeneous demonstrations to validate the core hypothesis.", "MISSING RELATED WORK: 'Utility-Diversity Aware Online Batch Selection for LLM Supervised Fine-tuning' (arXiv 2510.16882, Oct 2025) directly performs online scoring and selection of training samples during SFT using model output logits. This is conceptually very close to RAPID's online prioritization during SFT, though in the LLM domain. Must be cited and differentiated.", "NOVELTY CONCERN: SuRe (arXiv Nov 2025) combines NLL-based surprise + EMA (fast/slow LoRA merged via EMA) + prioritized replay. RAPID combines reducible loss (current_loss - EMA_loss) + EMA reference + prioritized replay. The key distinction — using reducible loss instead of raw NLL to avoid over-sampling noisy data — is actually ReLo's contribution (NeurIPS 2023), not RAPID's. RAPID's novel contribution is the domain transfer to VLA SFT + multi-granularity sampling. This should be stated more honestly rather than claiming the reducible loss mechanism as novel.", "TECHNICAL NOTE: ReLo uses a target network (periodic hard copy from online network) as its reference, NOT an EMA. RAPID proposes EMA instead. This is a meaningful design choice that should be explicitly justified — why EMA rather than periodic hard copy? What are the tradeoffs? This is actually a contribution that should be highlighted and ablated.", "THEORETICAL DEPTH: The convergence rate claim O(1/√(nη)) vs O(1/√n) is a standard importance sampling variance reduction result. The per-step improvement bound under Lipschitz smoothness is likely straightforward. The most interesting theoretical contribution — connecting reducible-loss prioritization to iw-SFT's importance-weighted framework as an adaptive quality score — should be the centerpiece of the theory section, not just one of three results.", "COST NOTE: CoRL deadline dates are off by 1 day (abstract May 25 not 26, paper May 28 not 29). Minor but indicates imprecision."]
Feedback: The revision thoroughly addressed Round 1 issues (VACO positioning, ReLo failure mode, hindsight relabeling removal, scope reduction), showing strong engagement. The proposal is well-structured and the method is sound. However, two critical issues remain that prevent a pass:

**1. Fix the experimental design for LIBERO saturation.** Your primary benchmark is near-saturated (97% avg). Three concrete options:
- (a) **Add an OXE-based experiment**: Curate a mixed-quality subset of Open X-Embodiment with known quality variation (e.g., mix Bridge, RT-1, and lower-quality datasets). This directly tests the noisy-data motivation.
- (b) **Controlled noise injection on LIBERO**: Systematically corrupt demonstrations (random action noise, frame dropping, trajectory truncation) at varying corruption ratios (10-50%) and show RAPID degrades gracefully while uniform sampling and static curation do not. This is the cleanest experimental design for the core claim.
- (c) **Use LIBERO-Long exclusively or LIBERO-Plus**: LIBERO-Long (90.7% baseline) has more headroom. LIBERO-Plus tests robustness under perturbation and reveals that current high success rates are fragile.

**2. Sharpen the novelty claim.** Currently the proposal presents reducible loss as its key contribution, but this is ReLo's idea. RAPID's actual novel contributions are: (i) adapting reducible loss from RL (with target network) to imitation SFT (with EMA reference) — justify and ablate EMA vs hard copy; (ii) multi-granularity trajectory+transition sampling; (iii) theoretical connection to iw-SFT showing reducible loss as an adaptive importance weight. Lead with these three points explicitly.

**3. Minor additions needed:**
- Cite and differentiate from 'Utility-Diversity Aware Online Batch Selection for LLM SFT' (arXiv 2510.16882)
- Make the iw-SFT connection the centerpiece theoretical result
- Add an ablation: EMA reference vs periodic hard-copy reference (à la ReLo's target network)
- Consider reporting data efficiency curves (how quickly RAPID matches full-data performance) rather than just final success rate, since the headroom at convergence is small

**Timeline recommendation:** CoRL 2026 (12 days) is infeasible for addressing these issues. Target AAAI 2027 (Aug deadline) as primary, with CoRL as a stretch only if implementation is complete and you can run the noise-injection experiment rapidly.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL MISSING REFERENCE: Re-Mix (Hejna et al., CoRL 2024) uses excess behavior cloning loss relative to a fixed reference model for domain-level data weighting in large-scale imitation learning — the same core concept (excess/reducible loss relative to a reference model to identify learnable vs. irreducibly hard data in IL) applied in the same domain (robot imitation learning). Published at CoRL, the user's target venue. Must be cited and explicitly differentiated. Key differences to articulate: Re-Mix operates at domain level with fixed reference and DRO optimization; RAPID operates at sample/transition level with adaptive EMA reference and PER-style sampling.", "CRITICAL MISSING REFERENCE: RHO-LOSS (Mindermann et al., ICML 2022) is the true foundational work on 'reducible holdout loss selection' for supervised learning — selecting training points that most reduce generalization loss by separating learnable from irreducibly noisy data using a reference model. The proposal credits ReLo (NeurIPS 2023) as foundational, but ReLo itself builds on RHO-LOSS. Since RAPID targets supervised fine-tuning (not RL), RHO-LOSS is a more direct ancestor than ReLo and must be cited.", "MISSING REFERENCE: DoReMi (Xie et al., NeurIPS 2023) uses excess loss relative to a pretrained reference model for domain mixing weights in LLM pretraining. Conceptually parallel to Re-Mix and RAPID. Should be cited to show the broader lineage of excess-loss-based data selection.", "MISSING REFERENCE: LEAD (arXiv May 2025, 2505.07437) introduces Instance-Level Dynamic Uncertainty combining instantaneous loss with exponential smoothing of historical loss signals for online data selection during LLM SFT. Very close mechanistically — uses EMA-smoothed loss signals (not an EMA model, but similar intuition) for online SFT selection. Must be cited and differentiated.", "MISSING REFERENCE: DataMIL (arXiv May 2025, 2505.09603) is a policy-driven data selection framework for robot imitation learning using the datamodels paradigm. Validated on 60+ tasks including Open X-Embodiment. While static, it's an important concurrent work in robot demonstration curation that should appear in the landscape.", "MISSING REFERENCE: DemInf / Robot Data Curation with Mutual Information Estimators (RSS 2025, 2502.08623) uses k-NN mutual information estimation for offline robot demonstration quality scoring. Another concurrent robot data curation method missing from the landscape.", "VENUE CORRECTION: RINSE is listed as 'arXiv April 2026' but was accepted at ICML 2025. Should be cited as 'RINSE (ICML 2025)' — this is a peer-reviewed publication, not just an arXiv preprint.", "NOVELTY REPOSITIONING NEEDED: The proposal's gap statement ('No existing work applies reducible-loss-based adaptive prioritized sampling to VLA imitation learning SFT') is technically accurate but misleadingly narrow. Re-Mix applies excess loss to imitation learning (domain level). RHO-LOSS applies reducible loss to supervised learning. Rho-1 applies excess loss to LLM pretraining. The real gap is narrower: 'No existing work applies sample-level, adaptive (EMA) reducible-loss prioritized sampling to VLA SFT.' This should be stated honestly.", "IMPACT CONCERN: SimpleVLA-RL (ICLR 2026) achieves 99% on standard LIBERO via RL post-training. The RL approach may increasingly marginalize SFT data curation as the bottleneck for VLA performance. The paper should discuss why SFT data quality still matters even when RL post-training is available — e.g., RL requires reward engineering, SFT is the warm-start for RL, or RAPID could complement RL post-training.", "MINOR: CoRL 2026 official deadlines are May 25/28 AoE (not May 26/29 as stated). The proposal's dates are UTC conversions of the AoE deadlines — technically the same instant but the official citation should use AoE."]
Feedback: The proposal has improved substantially from Rounds 1-2, addressing LIBERO saturation (LIBERO-Plus + noise injection), motivation-experiment mismatch, UDS citation, and novelty positioning. The method is technically sound and the experimental plan is comprehensive. However, **the landscape analysis has a critical blind spot**: at least 6 important works are uncited, and two of them (Re-Mix, RHO-LOSS) directly impact the novelty claim.

**Priority 1 — Cite and differentiate from Re-Mix (CoRL 2024).** This is the most urgent fix. Re-Mix demonstrates that excess BC loss relative to a reference model effectively curates imitation learning data at the domain level. RAPID's differentiation is clear: (a) sample/transition-level granularity vs. domain-level, (b) adaptive EMA reference vs. fixed reference, (c) PER-style online sampling vs. DRO optimization. Frame RAPID as extending Re-Mix's domain-level insight to fine-grained, adaptive sample-level prioritization. This is actually a strong narrative — 'Re-Mix showed excess loss works for domain weighting; we show it works even better at sample granularity with an adaptive reference.'

**Priority 2 — Cite RHO-LOSS (ICML 2022) as the true foundational concept.** The reducible loss concept for supervised learning originates here, not in ReLo. Since RAPID is a supervised (SFT) method, RHO-LOSS is the direct ancestor. ReLo adapted it to RL; RAPID adapts it back to supervised learning but with key differences (EMA reference, multi-granularity, iw-SFT connection).

**Priority 3 — Cite LEAD, DoReMi, DataMIL, DemInf.** These are important for landscape completeness. LEAD is particularly relevant — differentiate by noting LEAD uses exponential smoothing of loss *values* while RAPID uses an EMA *model* to compute reducible loss, which captures more information about what is genuinely learnable vs. noisy.

**Priority 4 — Honestly reposition the novelty.** The gap is not 'no one has used reducible loss for imitation learning' (Re-Mix's excess loss is conceptually identical). The gap is: (a) no sample-level adaptive reducible loss for VLA SFT, (b) no EMA model as adaptive reference (vs. fixed or periodic hard-copy), (c) no multi-granularity trajectory+transition prioritization, (d) no theoretical connection to iw-SFT. Lead with these specific contributions.

**Priority 5 — Address the RL paradigm shift.** SimpleVLA-RL achieves 99% on LIBERO via RL. Discuss why SFT data quality still matters: (a) SFT provides the warm-start for RL, (b) better SFT initialization could make RL more sample-efficient, (c) not all settings allow online interaction for RL, (d) RAPID could potentially be combined with RL post-training. This strengthens the impact argument.

**Estimated effort:** These are all writing/framing changes, not experimental changes. The experimental plan is solid. With these fixes, the paper could target AAAI 2027 or ICRA 2027 competitively.

### Round 4 review
Verdict: revise
Issues: ["FACTUAL: ReLo's target network in SAC uses Polyak averaging (EMA), not periodic hard copy as the proposal claims. The proposal states 'ReLo uses a *periodically hard-copied* target network' — this is inaccurate for SAC-based experiments. Since ReLo already implements EMA-based reducible loss for prioritized sampling (in RL), RAPID's Contribution 1 novelty is narrower than presented. The actual novel contribution is introducing an EMA reference in *supervised/imitation learning* where no target network naturally exists — this should be stated precisely.", "MISSING REFERENCE: DS2 — 'Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining' (ICLR 2025, arXiv 2502.06733). This peer-reviewed work at a top venue performs dynamic, instance-level, loss-based sample reweighting during training with a theoretical convergence framework. It is conceptually very close to RAPID's online prioritization mechanism (though it uses raw loss, not reducible loss, and targets LLM pretraining). Should be cited and differentiated — RAPID's reducible loss avoids the noise overfitting issue that DS2's raw-loss approach would face.", "ADVERSARIAL EVIDENCE NOT ADDRESSED: 'When Do Curricula Work?' (Wu et al., ICLR 2021) demonstrates that curriculum/prioritized sampling provides only marginal benefits on standard benchmarks with clean data — the apparent benefit is entirely explained by dynamic training set size, not the ordering itself. Benefits emerge only under (1) limited training budget or (2) noisy data. Standard LIBERO uses 50 clean human-teleoperated demos per task — RAPID may show null results there. The noise injection experiment addresses condition (2), but the proposal should acknowledge that gains on clean LIBERO may be minimal and position the noise experiments as the primary validation.", "EMA FEEDBACK LOOP: The EMA reference model is derived from the training model itself, creating a potential confirmation bias where the model's systematic errors propagate through the priority signal. Research on EMA teachers in self-distillation (arXiv 2411.18704) shows that even slow EMA updates can amplify epistemic suppression via feedback loops. This risk should be discussed as a limitation and the EMA decay sensitivity ablation (τ ∈ {0.999–0.99999}) should explicitly check for this failure mode.", "VENUE MISMATCH: The user explicitly requested CoRL 2026 (abstract May 26, paper May 28 — 13-15 days away). The proposal withdraws from CoRL without offering a minimal viable plan. A focused CoRL submission is tight but potentially feasible: theory (iw-SFT connection) + implementation on OpenVLA-OFT + LIBERO noise injection (primary experiment) + standard LIBERO + 2-3 baselines (uniform, raw-loss priority, fixed-reference ablation). If the researcher has GPU access and OpenVLA-OFT familiarity, this is a 14-day sprint. The user indicated a theory-focused paper without real robot experiments is acceptable — the proposal should at least sketch this option.", "THEORETICAL DEPTH: The O(1/√(nη)) vs O(1/√n) convergence rate improvement is a standard importance sampling variance reduction result. The per-step improvement bound under Lipschitz smoothness is straightforward. For ICLR 2027, the iw-SFT connection needs to go beyond standard IS analysis — e.g., prove that the adaptive quality score from EMA-based reducible loss provably tightens the iw-SFT bound more than any static score in a formal PAC-learning or regret-minimization framework, not just claim it intuitively."]
Feedback: The proposal has improved dramatically across 4 rounds — the landscape is now comprehensive, the method is well-motivated, and the experimental plan is thorough. The remaining gap to 'pass' is not about missing references or experimental design, but about the inherent novelty ceiling and impact uncertainty. Here is how to close that gap:

**1. Fix the ReLo characterization (easy, high priority).** ReLo's target network in SAC IS Polyak-averaged (EMA). Claiming 'periodic hard copy' misrepresents the prior art and overstates your novelty. Reframe Contribution 1 as: 'We introduce an EMA reference model for reducible loss computation in supervised/imitation learning, where no target network naturally exists. Unlike RL (ReLo), where the target network serves double duty for TD learning stability and reducible loss, RAPID's EMA reference is purpose-built for data quality scoring.' This is still a valid contribution — just be precise.

**2. Offer a CoRL 2026 minimal plan (important for user requirements).** Even if risky, sketch a focused 14-day plan: (a) formalize iw-SFT theory (3 days), (b) implement EMA reference + reducible loss on OpenVLA-OFT (3 days), (c) run LIBERO noise injection (3 corruption types × 2 ratios, 3 baselines — 4 days), (d) standard LIBERO as secondary (2 days), (e) write paper (4 days, overlapping). Drop OXE, LIBERO-Plus, UDS baseline, and extensive ablations — save those for AAAI 2027 if CoRL is rejected. The user said a theory-focused paper is acceptable.

**3. Acknowledge the clean-data limitation explicitly.** On standard LIBERO (97% baseline, clean data), RAPID may show minimal gains based on the 'When Do Curricula Work?' finding. Position the noise injection and LIBERO-Plus experiments as primary evidence, with standard LIBERO as a 'does no harm' sanity check. This honest framing is stronger than over-claiming.

**4. Deepen the iw-SFT theory (for ICLR consideration).** The convergence rate claim is standard IS. To make the theory the genuine centerpiece: (a) prove a formal regret bound showing that adaptive reference strictly dominates static reference under mild assumptions on loss landscape dynamics, (b) connect the EMA decay rate τ to the optimal IS proposal distribution tracking rate, (c) derive the conditions under which RAPID's adaptive quality score achieves the minimax optimal convergence rate for the class of smooth loss functions.

**5. Cite DS2 (ICLR 2025).** One sentence: 'DS2 demonstrates that dynamic instance-level loss-based reweighting improves LLM pretraining convergence with theoretical guarantees; however, DS2 uses raw loss and does not decompose reducible vs. irreducible components, inheriting the noise overfitting risk identified by RHO-LOSS.' This strengthens your positioning.

**6. Discuss EMA feedback risk as a limitation.** Acknowledge that the EMA reference is not independent of the training model. The τ ablation partially addresses this — extreme values of τ (very high = near-copy, very low = near-identity) should reveal the failure mode if present.

**Bottom line:** The proposal is competitive for ICRA 2027 and likely AAAI 2027 as-is. For CoRL 2026, a focused sprint is feasible if the user prioritizes it. For ICLR 2027, the theory needs genuine depth beyond standard IS analysis. The main bottleneck to 'pass' is that novelty and impact are both at 3/5 — fixing the ReLo characterization, adding DS2, and offering a CoRL plan would not change these scores, but deepening the theory or adding a surprising experimental finding (e.g., RAPID-initialized policies converge 2x faster with SimpleVLA-RL) would.

### Round 5 review
Verdict: revise
Issues: ["THEORETICAL CONCERN: Theorem 1's O(T) vs Ω(T²) asymptotic advantage assumes 'non-trivial policy drift during training,' but VLA SFT typically runs for 1-3 epochs over ~500 demonstrations with small learning rates. The cumulative drift may be insufficient for the asymptotic separation to manifest in practice. The proposal should either (a) derive finite-T bounds showing the advantage at realistic training horizons, or (b) empirically demonstrate the bound gap grows across training for their actual experimental setup.", "IMPACT GAP: The RAPID+RL complementarity is the strongest impact argument ('SFT accounts for 74pp of 82pp total improvement in SimpleVLA-RL') but is left as future work. Even a small experiment showing RAPID-initialized SFT → SimpleVLA-RL outperforms vanilla SFT → SimpleVLA-RL would dramatically strengthen the paper's impact argument and address the 'RL makes SFT quality irrelevant' concern.", "FEASIBILITY RISK: The CoRL sprint plan lists 18 noise-injection runs + 12 standard LIBERO runs = 30 runs. At ~120h per OpenVLA-OFT training run (even with speedups), this requires substantial parallel GPU capacity within 9 experiment days (Days 4-9). With 8×A100, that's ~450 GPU-hours/day sustained, which is feasible only with near-perfect pipeline automation and zero debugging time. The plan should identify a minimum viable experiment set (~12-15 runs) that validates the core claim.", "MINOR MISSING REFERENCES: (a) Green-VLA's DataQA pipeline (arXiv Feb 2026, 2602.00919) — a VLA-specific static data curation pipeline using quality metrics, relevant as a concurrent VLA data curation method. (b) VLA-OPD (arXiv March 2026, 2603.26666) — bridges offline SFT and online RL for VLAs via on-policy distillation, relevant to the SFT+RL complementarity discussion.", "THEOREM 3 PRACTICAL ASSUMPTION: The noise filtering guarantee assumes irreducibly noisy transitions maintain high loss for all θ (L_θ(i) ≥ σ²). For VLA action prediction with L1 loss, moderate action noise (σ ∈ {0.05, 0.1}) may not produce persistently high loss — high-capacity VLMs can partially fit noise, especially in low-dimensional action spaces. The guarantee should specify assumptions on noise magnitude relative to the model's fitting capacity.", "VENUE FIT: CoRL historically favors papers with strong empirical contributions, often including real-robot experiments or compelling simulation results. A theory-focused paper with limited simulation experiments (the fallback plan) may face a venue mismatch. The proposal should consider whether the CoRL sprint can reliably produce sufficient empirical evidence, or whether targeting AAAI 2027 as the primary venue with CoRL as a stretch goal is more honest."]
Feedback: The proposal has improved dramatically across 5 rounds and the landscape analysis is now world-class — I found no significant missing competitive work that isn't already cited. The method is sound, the positioning is honest, and the theoretical framing is well-motivated. However, the average score (3.5) remains below the 4.0 threshold due to inherent novelty and impact ceilings. Here's how to close the gap:

**1. Add a RAPID+RL experiment (highest priority for impact).** This is the single most impactful addition. SimpleVLA-RL's SFT stage accounts for 74pp of 82pp total improvement. Run: (a) vanilla SFT → RL, (b) RAPID SFT → RL, on 2-3 LIBERO-Long tasks. Even a small improvement in RL convergence speed or final performance would transform the paper's impact narrative from 'another data curation method' to 'better SFT initialization for the entire VLA training pipeline.' This directly addresses the RL post-training trend concern.

**2. Derive finite-T bounds for Theorem 1.** The O(T) vs Ω(T²) asymptotic result is elegant but may not manifest in short VLA SFT runs. Derive a bound like: 'For T ≥ T₀(ε, τ), the adaptive reference achieves at least X% tighter bound than the best static reference.' This makes the theory practically relevant and directly testable.

**3. Reduce the CoRL experiment scope to minimum viable.** Cut to: (a) noise injection on LIBERO-Long only (3 corruption types × 1 ratio = 3 configs × 3 methods = 9 runs), (b) standard LIBERO-Long as sanity check (3 runs), (c) 1 key ablation: EMA vs fixed reference (3 runs). Total: ~15 runs, feasible with 4×A100 in 7 days. This validates the core claim (reducible > raw loss on noisy data) and Theorem 1 (adaptive > static reference).

**4. Cite Green-VLA DataQA and VLA-OPD.** Minor additions to an already comprehensive landscape.

**5. For the full AAAI version:** Add LIBERO-Plus robustness evaluation, OXE mixed-quality experiments, and the RAPID+RL experiment. This is where the paper can become genuinely compelling.

**Bottom line:** The proposal is at its structural ceiling — further revision of positioning or landscape won't change scores. What's needed is experimental evidence (especially RAPID+RL) and finite-T theoretical results to push novelty and impact from 3 to 4.

### Round 6 review
Verdict: revise
Issues: ["MISSING REFERENCE: 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' (ICML 2026, poster). This paper directly studies how SFT technique quality affects downstream RL performance — showing 7.09% RL improvement and 11.54% reduced forgetting via token-level clipping. While it operates on LLMs (ALFWorld, ScienceWorld) at the token level rather than VLA data level, it establishes the same principle as RAPID's Contribution 4 ('SFT quality cascades to RL'). Must be cited. RAPID's differentiation: (a) data/demonstration-level filtering vs. token-level clipping, (b) VLA domain with action-prediction loss vs. LLM domain with language loss, (c) noise filtering mechanism vs. trust-region mechanism. This weakens the claim of 'first to study SFT quality → RL' — reframe as 'first to study SFT *data quality* → RL for *VLAs*.'", "NOVELTY NARROWING: iw-SFT (arXiv 2507.12856) already implements EMA update θ_q = α·θ_q + (1-α)·θ for continuous control (D4RL) experiments. The proposal's Contribution 1 claims 'RAPID introduces a purpose-built EMA reference specifically designed for data quality scoring' as if no EMA reference exists in supervised/IL settings — but iw-SFT uses exactly this mechanism for updating the auxiliary distribution q in continuous control SFT/BC. The critical distinction: iw-SFT uses EMA for trajectory-level importance weights (multiplicative loss reweighting), while RAPID uses EMA for *reducible loss computation* + *PER-style sampling priorities*. This distinction is real but must be articulated precisely. Reframe: 'iw-SFT proposed EMA for importance weighting; we use EMA for reducible loss decomposition, revealing that the EMA reference enables noise-robust prioritization beyond what importance weighting alone provides.'", "CoRL TIMELINE: 13 days to abstract deadline (May 26), 16 days to paper deadline (May 29). The proposal should include an explicit go/no-go decision point: if the first noise-injection experiment results are not available by ~May 22-23, fall back to AAAI 2027 only. The abstract deadline requires at least preliminary results to write a credible abstract.", "FINITE-T TESTABILITY: Corollary 1.1 predicts T₀ = C₁/(C₂·Δ₀·ε) falls within 'thousands of steps' for τ* = 0.978. However, the constants C₁, C₂ depend on loss landscape properties (Lipschitz constant M, gradient bound ε) that are difficult to estimate a priori for VLA models. The empirical crossover point may differ by an order of magnitude from the theoretical prediction. The proposal should acknowledge this uncertainty and frame the empirical bound-gap measurement as a test of the theory's qualitative prediction (linear vs quadratic growth) rather than its quantitative prediction (exact T₀).", "NOISE INJECTION VS REAL-WORLD NOISE: The primary experiment uses synthetic corruption (Gaussian noise, frame dropping, truncation). Real-world demonstration noise (hesitation, redundant motions, suboptimal strategies, operator fatigue) has fundamentally different structure — it's *coherent* noise that may be harder for reducible loss to detect. The OXE experiment (deferred to AAAI) would address this. For CoRL, acknowledge this limitation explicitly and frame noise injection as a controlled test of the mechanism, not a claim about real-world robustness."]
Feedback: The proposal has reached an exceptionally high level of polish and the landscape analysis is now world-class. The remaining gap to 'pass' (avg 3.5 vs 4.0 threshold) reflects inherent novelty and impact ceilings rather than fixable oversights. Here is how to close the gap:

**1. Cite and differentiate from ICML 2026 clipping paper (easy, high priority).** 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' establishes that SFT technique → RL performance in LLMs. RAPID's differentiation is clear: (a) data-level noise filtering vs. token-level trust region, (b) VLA domain vs. LLM domain, (c) prioritized sampling vs. gradient clipping. Frame RAPID as: 'The ICML 2026 work shows SFT technique affects RL for LLMs; we show SFT *data quality* affects RL for VLAs — a complementary finding in a different domain with a different mechanism.'

**2. Sharpen iw-SFT differentiation (important).** iw-SFT already uses EMA for continuous control. RAPID's actual novelty over iw-SFT is threefold: (a) reducible loss decomposition (iw-SFT uses trajectory probabilities for importance weights, RAPID uses loss difference for noise-robust prioritization), (b) PER-style sampling (iw-SFT reweights loss multiplicatively, RAPID controls which samples are seen), (c) theoretical analysis of optimal τ and finite-T crossover. State this explicitly rather than claiming EMA reference as wholly novel.

**3. The path to pushing impact from 3→4.** The single most impactful result would be a compelling RAPID+RL experiment showing e.g. 30-50% fewer RL steps to reach 90% success. If this materializes, lead the paper with it. The narrative becomes: 'SFT data quality is the hidden bottleneck of VLA RL pipelines; RAPID provides a drop-in fix.' This is more impactful than 'another data curation method for noisy demonstrations.'

**4. Consider whether CoRL is the right target.** With 13 days to abstract, the risk of a rushed submission is high. The AAAI 2027 timeline (3+ months) allows comprehensive experiments including LIBERO-Plus and OXE, which would strengthen impact significantly. A well-executed AAAI paper with the RAPID+RL finding as headline result + robustness on LIBERO-Plus + OXE mixed-quality is stronger than a rushed CoRL submission. If you attempt CoRL, treat it as a stretch with explicit go/no-go by May 22.

**5. For the next revision, focus on sharpening rather than expanding.** The proposal is comprehensive but very long. The landscape analysis is thorough but could be tightened. Every additional reference and caveat adds length but diminishing returns on clarity. The core story is: 'EMA-based reducible loss enables noise-robust, adaptive data prioritization for VLA SFT, and this cascades to faster RL convergence.' Everything should serve this narrative.


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
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "4896c68b-f15b-4a94-bc55-d5b64d277811",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T11:39:05.972Z_

```json
{
  "parentUuid": "4896c68b-f15b-4a94-bc55-d5b64d277811",
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
  "uuid": "9970614f-1c45-4038-bbed-806127fabd10",
  "timestamp": "2026-05-13T11:39:05.972Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T11:39:05.973Z_

```json
{
  "parentUuid": "9970614f-1c45-4038-bbed-806127fabd10",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "602f2728-dac8-4a75-8f5a-0b9a914d00a5",
  "timestamp": "2026-05-13T11:39:05.973Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "602f2728-dac8-4a75-8f5a-0b9a914d00a5",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Assistant

_source line 8 · 2026-05-13T11:39:10.786Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 7 of 10 for reviewing the RAPID paper idea. Let me conduct a thorough independent review. I need to:

1. Verify the claims made in the proposal
2. Search for missing competitive work
3. Check if the issues from previous rounds have been addressed
4. Assess novelty, feasibility, clarity, and impact

Let me start by searching for the key claims and references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "602f2728-dac8-4a75-8f5a-0b9a914d00a5",
  "isSidechain": false,
  "requestId": "req_011CazW93hJqyQpLxF2cPdEa",
  "type": "assistant",
  "uuid": "261dbc84-1b1d-4021-9c64-d39b3adc61cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wEqNHYA5HkZxhH5Pht4D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24965,
      "cache_read_input_tokens": 11841,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 231,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24965
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-13T11:39:11.800Z_

I'll conduct an independent review of this proposal, focusing on verifying claims, finding missing competitive work, and assessing whether the Round 6 issues have been adequately addressed. Let me start with parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "261dbc84-1b1d-4021-9c64-d39b3adc61cb",
  "isSidechain": false,
  "requestId": "req_011CazW93hJqyQpLxF2cPdEa",
  "type": "assistant",
  "uuid": "6bbd89a4-fbe2-4276-92b2-ddf92f5121ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wEqNHYA5HkZxhH5Pht4D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24965,
      "cache_read_input_tokens": 11841,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 231,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24965
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T11:39:12.087Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016PWMFw6wzvwjiFEZQstBzj`</summary>

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
  "parentUuid": "6bbd89a4-fbe2-4276-92b2-ddf92f5121ce",
  "isSidechain": false,
  "requestId": "req_011CazW93hJqyQpLxF2cPdEa",
  "type": "assistant",
  "uuid": "f7a9fbb6-6f4e-4958-abbd-16dff94412dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wEqNHYA5HkZxhH5Pht4D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24965,
      "cache_read_input_tokens": 11841,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 231,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24965
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T11:39:12.094Z_

<details><summary>↩ Tool result · `toolu_016PWMFw6wzvwjiFEZQstBzj`</summary>

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
  "parentUuid": "f7a9fbb6-6f4e-4958-abbd-16dff94412dc",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "fc36954c-ffae-4f61-b66a-43fe6341f33a",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "f7a9fbb6-6f4e-4958-abbd-16dff94412dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T11:39:15.046Z_

Let me now conduct thorough independent searches across multiple dimensions. I'll start with verifying key claims and searching for competitive work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc36954c-ffae-4f61-b66a-43fe6341f33a",
  "isSidechain": false,
  "requestId": "req_011CazW9VqRzv2hkEmWsJMXJ",
  "type": "assistant",
  "uuid": "530bd741-3b34-4cfa-b912-1c2b745e64d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBw5tEqx2c43wLzR63eYZH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 36806,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 36806,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T11:39:15.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TaeXaMSZ1VkUUc5R9NiP9d`</summary>

```json
{
  "query": "CoRL 2026 conference submission deadline dates Austin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "530bd741-3b34-4cfa-b912-1c2b745e64d5",
  "isSidechain": false,
  "requestId": "req_011CazW9VqRzv2hkEmWsJMXJ",
  "type": "assistant",
  "uuid": "7c0e13b4-e8c2-4f15-a0ea-6859f67a09f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBw5tEqx2c43wLzR63eYZH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 36806,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 36806,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T11:39:19.507Z_

<details><summary>↩ Tool result · `toolu_01TaeXaMSZ1VkUUc5R9NiP9d`</summary>

```text
Web search results for query: "CoRL 2026 conference submission deadline dates Austin"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"}]

Based on the search results, here are the CoRL 2026 conference submission deadline dates for the Austin event:

**Submission Deadlines:**
- Abstract submission deadline: May 26, 2026 11:59 UTC
- Paper submission deadline: Thursday (5/28) EOD

**Conference Details:**
- Conference dates: November 9-12, 2026
- Venue: JW Marriott Austin, 110 E 2nd St, Austin, TX 78701

Additionally, the camera-ready version of accepted papers is due by Oct 12, 2026 (23:59 Anywhere on Earth).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c0e13b4-e8c2-4f15-a0ea-6859f67a09f6",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "0f85d330-055c-4e2b-861c-771af770435f",
  "toolUseResult": {
    "query": "CoRL 2026 conference submission deadline dates Austin",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XnUDCAd9g5e8ZhLZxVbhY9",
        "content": [
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz",
            "url": "https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          }
        ]
      },
      "Based on the search results, here are the CoRL 2026 conference submission deadline dates for the Austin event:\n\n**Submission Deadlines:**\n- Abstract submission deadline: May 26, 2026 11:59 UTC\n- Paper submission deadline: Thursday (5/28) EOD\n\n**Conference Details:**\n- Conference dates: November 9-12, 2026\n- Venue: JW Marriott Austin, 110 E 2nd St, Austin, TX 78701\n\nAdditionally, the camera-ready version of accepted papers is due by Oct 12, 2026 (23:59 Anywhere on Earth)."
    ],
    "durationSeconds": 3.6670023109999983
  },
  "sourceToolAssistantUUID": "7c0e13b4-e8c2-4f15-a0ea-6859f67a09f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T11:39:22.429Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T9574HG3hQpLxXwgbyaMuD`</summary>

```json
{
  "query": "iw-SFT \"supervised fine tuning on curated data is reinforcement learning\" 2507.12856 EMA continuous control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f85d330-055c-4e2b-861c-771af770435f",
  "isSidechain": false,
  "requestId": "req_011CazWA3EoSgPrca98SiWm1",
  "type": "assistant",
  "uuid": "55d7e3ee-2df6-4226-a012-159c82c14b06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ekia6b8RS39xcZTDAnya8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 38057,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 38057,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 661
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T11:39:33.083Z_

<details><summary>↩ Tool result · `toolu_01T9574HG3hQpLxXwgbyaMuD`</summary>

```text
Web search results for query: "iw-SFT "supervised fine tuning on curated data is reinforcement learning" 2507.12856 EMA continuous control"

Links: [{"title":"[2507.12856] Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/abs/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://arxiv.org/pdf/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/html/2507.12856"},{"title":"Paper page - Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://huggingface.co/papers/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://www.alphaxiv.org/overview/2507.12856v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v1"},{"title":"Proximal Supervised Fine-Tuning","url":"https://arxiv.org/html/2508.17784v1"},{"title":"(PDF) Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://www.researchgate.net/publication/393784242_Supervised_Fine_Tuning_on_Curated_Data_is_Reinforcement_Learning_and_can_be_improved"},{"title":"Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning","url":"https://arxiv.org/html/2509.15157v1"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved) | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/supervised-fine-tuning-curated-data-is-reinforcement"}]

Based on the search results, I found the paper you're looking for. Here's a summary of the key information:

## Paper Overview

Behavior Cloning (BC) on curated (or filtered) data is the predominant paradigm for supervised fine-tuning (SFT) of large language models; as well as for imitation learning of control policies.

## Main Contribution: iw-SFT

The paper's central insight is that SFT can be understood as maximizing a lower bound on the RL objective in a sparse reward setting. Building on this observation, a small modification to SFT leads to an importance weighted variant that behaves closer to training with RL as it: i) optimizes a tighter bound to the RL objective and, ii) can improve performance compared to SFT on curated data. This variant is referred to as importance weighted supervised fine-tuning (iw-SFT).

## Key Results

The method is easy to implement and can be further generalized to training with quality scored data. The resulting SFT variants are competitive with more advanced RL algorithms for large language models and for training policies in continuous control tasks.

## Practical Improvements

Training with iw-SFT on the curated dataset S1.1K surpasses training with SFT only by up to 7% depending on the AIME benchmark.

The paper (arXiv:2507.12856) was authored by Chongli Qin and Jost Tobias Springenberg from Independent Research, and additional code and information is available at https://independentresearch.ai/posts/iwsft.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55d7e3ee-2df6-4226-a012-159c82c14b06",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "bb33a753-a838-468b-a428-c11b623b9949",
  "toolUseResult": {
    "query": "iw-SFT \"supervised fine tuning on curated data is reinforcement learning\" 2507.12856 EMA continuous control",
    "results": [
      {
        "tool_use_id": "srvtoolu_019oXb29SWRXLW6CvNFKbvTx",
        "content": [
          {
            "title": "[2507.12856] Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://arxiv.org/abs/2507.12856"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement ...",
            "url": "https://arxiv.org/pdf/2507.12856"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://arxiv.org/html/2507.12856"
          },
          {
            "title": "Paper page - Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://huggingface.co/papers/2507.12856"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement ...",
            "url": "https://www.alphaxiv.org/overview/2507.12856v1"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification",
            "url": "https://arxiv.org/html/2508.05629v1"
          },
          {
            "title": "Proximal Supervised Fine-Tuning",
            "url": "https://arxiv.org/html/2508.17784v1"
          },
          {
            "title": "(PDF) Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://www.researchgate.net/publication/393784242_Supervised_Fine_Tuning_on_Curated_Data_is_Reinforcement_Learning_and_can_be_improved"
          },
          {
            "title": "Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning",
            "url": "https://arxiv.org/html/2509.15157v1"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved) | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/supervised-fine-tuning-curated-data-is-reinforcement"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's a summary of the key information:\n\n## Paper Overview\n\nBehavior Cloning (BC) on curated (or filtered) data is the predominant paradigm for supervised fine-tuning (SFT) of large language models; as well as for imitation learning of control policies.\n\n## Main Contribution: iw-SFT\n\nThe paper's central insight is that SFT can be understood as maximizing a lower bound on the RL objective in a sparse reward setting. Building on this observation, a small modification to SFT leads to an importance weighted variant that behaves closer to training with RL as it: i) optimizes a tighter bound to the RL objective and, ii) can improve performance compared to SFT on curated data. This variant is referred to as importance weighted supervised fine-tuning (iw-SFT).\n\n## Key Results\n\nThe method is easy to implement and can be further generalized to training with quality scored data. The resulting SFT variants are competitive with more advanced RL algorithms for large language models and for training policies in continuous control tasks.\n\n## Practical Improvements\n\nTraining with iw-SFT on the curated dataset S1.1K surpasses training with SFT only by up to 7% depending on the AIME benchmark.\n\nThe paper (arXiv:2507.12856) was authored by Chongli Qin and Jost Tobias Springenberg from Independent Research, and additional code and information is available at https://independentresearch.ai/posts/iwsft."
    ],
    "durationSeconds": 10.649705077000002
  },
  "sourceToolAssistantUUID": "55d7e3ee-2df6-4226-a012-159c82c14b06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T11:39:36.298Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZBdqevAm2aBFSHbYnKCuK`</summary>

```json
{
  "query": "\"off-policy token clipped\" SFT RL initialization ICML 2026 \"Tian-Shuo Liu\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb33a753-a838-468b-a428-c11b623b9949",
  "isSidechain": false,
  "requestId": "req_011CazWB3WTDMLNzYe7tZafi",
  "type": "assistant",
  "uuid": "677bdb42-f33c-4883-a218-58a69d0ee4d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvQFTvME4HHWabPN8k62kz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 38718,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 38718,
          "cache_creation_input_tokens": 1011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1011
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T11:39:42.481Z_

<details><summary>↩ Tool result · `toolu_01TZBdqevAm2aBFSHbYnKCuK`</summary>

```text
Web search results for query: ""off-policy token clipped" SFT RL initialization ICML 2026 "Tian-Shuo Liu""

Links: [{"title":"ICML Poster Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL","url":"https://icml.cc/virtual/2026/poster/61171"},{"title":"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview","url":"https://openreview.net/forum?id=qJLKOryYeR"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2508.11408"},{"title":"GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub","url":"https://github.com/Gen-Verse/Open-AgentRL"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"Clipping-Free Policy Optimization for Large Language Models","url":"https://arxiv.org/html/2601.22801v1"},{"title":"Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE","url":"https://openreview.net/pdf?id=FhTAG591Ve"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"group-relative reinforce is secretly an off-policy algorithm","url":"https://openreview.net/pdf?id=7CFlXvCoN6"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"}]

Based on the search results, I found information about the work you're looking for:

Tian-Shuo Liu and colleagues have a paper on Supervised Fine-Tuning (SFT) as a critical step for adapting Large Language Models (LLMs) to specialized domains, often serving as an initialization for subsequent reinforcement learning (RL). The paper frames tokens with low probability in expert data as 'off-policy' tokens, as they represent a significant deviation from the model's current prior knowledge.

The authors adopt a well-established clipping strategy to constrain per-token updates within a trust region, applying this strategy to SFT to moderate the learning process by constraining gradient updates from off-policy tokens, creating a more on-policy-like training dynamic.

Through extensive experiments on the agentic benchmarks ALFWorld and ScienceWorld, this clipped approach reduces forgetting on out-of-distribution tasks by 11.54% and boosts final RL performance by 7.09% compared to standard SFT. The paper appears at ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "677bdb42-f33c-4883-a218-58a69d0ee4d3",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "2924480d-195f-45d3-8f77-0abac2b1cf7b",
  "toolUseResult": {
    "query": "\"off-policy token clipped\" SFT RL initialization ICML 2026 \"Tian-Shuo Liu\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Taiicw1gR9CvLk6AsCa9iv",
        "content": [
          {
            "title": "ICML Poster Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL",
            "url": "https://icml.cc/virtual/2026/poster/61171"
          },
          {
            "title": "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview",
            "url": "https://openreview.net/forum?id=qJLKOryYeR"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2508.11408"
          },
          {
            "title": "GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub",
            "url": "https://github.com/Gen-Verse/Open-AgentRL"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          },
          {
            "title": "Clipping-Free Policy Optimization for Large Language Models",
            "url": "https://arxiv.org/html/2601.22801v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE",
            "url": "https://openreview.net/pdf?id=FhTAG591Ve"
          },
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "group-relative reinforce is secretly an off-policy algorithm",
            "url": "https://openreview.net/pdf?id=7CFlXvCoN6"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2508.05629"
          }
        ]
      },
      "Based on the search results, I found information about the work you're looking for:\n\nTian-Shuo Liu and colleagues have a paper on Supervised Fine-Tuning (SFT) as a critical step for adapting Large Language Models (LLMs) to specialized domains, often serving as an initialization for subsequent reinforcement learning (RL). The paper frames tokens with low probability in expert data as 'off-policy' tokens, as they represent a significant deviation from the model's current prior knowledge.\n\nThe authors adopt a well-established clipping strategy to constrain per-token updates within a trust region, applying this strategy to SFT to moderate the learning process by constraining gradient updates from off-policy tokens, creating a more on-policy-like training dynamic.\n\nThrough extensive experiments on the agentic benchmarks ALFWorld and ScienceWorld, this clipped approach reduces forgetting on out-of-distribution tasks by 11.54% and boosts final RL performance by 7.09% compared to standard SFT. The paper appears at ICML 2026."
    ],
    "durationSeconds": 6.177740094999997
  },
  "sourceToolAssistantUUID": "677bdb42-f33c-4883-a218-58a69d0ee4d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T11:39:45.507Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JumLGMPPKuuNwbwZb3BBgG`</summary>

```json
{
  "query": "SimpleVLA-RL GRPO reinforcement learning VLA ICLR 2026 SFT contribution percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2924480d-195f-45d3-8f77-0abac2b1cf7b",
  "isSidechain": false,
  "requestId": "req_011CazWBjTn9RT2oJaBrbJEC",
  "type": "assistant",
  "uuid": "1cfed930-6c7b-4299-8fd2-aa726313bf55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTmcgWgQxhpL64JSwjmA9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 39729,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 39729,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T11:39:51.101Z_

<details><summary>↩ Tool result · `toolu_01JumLGMPPKuuNwbwZb3BBgG`</summary>

```text
Web search results for query: "SimpleVLA-RL GRPO reinforcement learning VLA ICLR 2026 SFT contribution percentage"

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"ICLR Poster SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://iclr.cc/virtual/2026/poster/10009314"},{"title":"SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE","url":"https://openreview.net/pdf/ec4796d06d4fb6583b2800d1782e89edf90d594e.pdf"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"SimpleVLA-RL: Scalable RL for VLA Models","url":"https://www.emergentmind.com/papers/2509.09674"},{"title":"Activity · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/activity"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://rlvla.github.io/"},{"title":"PRIME-RL · GitHub","url":"https://github.com/PRIME-RL"}]

Based on the search results, I found information about SimpleVLA-RL, which is an ICLR 2026 paper on scaling VLA training via reinforcement learning. The framework uses GRPO loss to update the policy model.

However, the search results do not contain specific information about the **SFT contribution percentage** that you asked about. While the results show that SimpleVLA-RL achieves an average success rate increase from 91% (SFT) to 99.1% on LIBERO, and using only one trajectory per task for cold-start SFT, SimpleVLA-RL raises the performance from 17.3 to 91.7, yielding an improvement of 74.4 points (430.1%), these figures represent performance improvements rather than the specific contribution percentage of SFT within the model.

If you're looking for more technical details about the SFT contribution percentage or other specific metrics from the paper, you may need to access the full paper directly through the ICLR website or arXiv at https://arxiv.org/abs/2509.09674.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cfed930-6c7b-4299-8fd2-aa726313bf55",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "2195cd2d-0991-4c91-88ab-4690048cdfbb",
  "toolUseResult": {
    "query": "SimpleVLA-RL GRPO reinforcement learning VLA ICLR 2026 SFT contribution percentage",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UE7RCwkTq6Fgwew9HXXSDX",
        "content": [
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=TQhSodCM4r"
          },
          {
            "title": "ICLR Poster SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://iclr.cc/virtual/2026/poster/10009314"
          },
          {
            "title": "SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE",
            "url": "https://openreview.net/pdf/ec4796d06d4fb6583b2800d1782e89edf90d594e.pdf"
          },
          {
            "title": "[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.09674"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          },
          {
            "title": "SimpleVLA-RL: Scalable RL for VLA Models",
            "url": "https://www.emergentmind.com/papers/2509.09674"
          },
          {
            "title": "Activity · PRIME-RL/SimpleVLA-RL",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL/activity"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://rlvla.github.io/"
          },
          {
            "title": "PRIME-RL · GitHub",
            "url": "https://github.com/PRIME-RL"
          }
        ]
      },
      "Based on the search results, I found information about SimpleVLA-RL, which is an ICLR 2026 paper on scaling VLA training via reinforcement learning. The framework uses GRPO loss to update the policy model.\n\nHowever, the search results do not contain specific information about the **SFT contribution percentage** that you asked about. While the results show that SimpleVLA-RL achieves an average success rate increase from 91% (SFT) to 99.1% on LIBERO, and using only one trajectory per task for cold-start SFT, SimpleVLA-RL raises the performance from 17.3 to 91.7, yielding an improvement of 74.4 points (430.1%), these figures represent performance improvements rather than the specific contribution percentage of SFT within the model.\n\nIf you're looking for more technical details about the SFT contribution percentage or other specific metrics from the paper, you may need to access the full paper directly through the ICLR website or arXiv at https://arxiv.org/abs/2509.09674."
    ],
    "durationSeconds": 5.590998100999998
  },
  "sourceToolAssistantUUID": "1cfed930-6c7b-4299-8fd2-aa726313bf55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2195cd2d-0991-4c91-88ab-4690048cdfbb",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool call

_source line 23 · 2026-05-13T11:39:54.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RhffNfinVyoSCbH3bpGrMC`</summary>

```json
{
  "query": "VLA data curation demonstration quality filtering 2026 arxiv robot imitation learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2195cd2d-0991-4c91-88ab-4690048cdfbb",
  "isSidechain": false,
  "requestId": "req_011CazWCNVVKbi5YtV5ajVwS",
  "type": "assistant",
  "uuid": "85f63cae-4c06-406d-b859-dcf88e77150c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJ1Ao6p45c1faym4bvwDxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 40601,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 40601,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 851
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T11:40:01.464Z_

<details><summary>↩ Tool result · `toolu_01RhffNfinVyoSCbH3bpGrMC`</summary>

```text
Web search results for query: "VLA data curation demonstration quality filtering 2026 arxiv robot imitation learning"

Links: [{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v2"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623"},{"title":"[2306.02437] Data Quality in Imitation Learning","url":"https://arxiv.org/abs/2306.02437"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning","url":"https://arxiv.org/html/2408.14037v1"}]

Based on the search results, I found several highly relevant papers on VLA data curation and demonstration quality filtering from 2026 and recent years on arXiv:

## Key Papers Found:

**1. Quality over Quantity (2026)**
Quality over Quantity (QoQ) is a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. QoQ is particularly well-suited for scaling to modern VLAs, which involve billions of parameters.

**2. CUPID: Curating Data your Robot Loves with Influence Functions (2025)**
CUPID is a novel data curation method that uses influence functions to measure the causal impact of a demonstration on the policy's closed-loop performance, highlighting the general utility of performance-based curation for filtering existing training demonstrations and subselecting new demonstrations.

**3. Scizor: A Self-Supervised Approach to Data Curation (2025)**
Scizor is the first self-supervised, transition-level data curation method that scales to the Open-X Embodiment Dataset with more than one million trajectories for large-scale models such as the Octo vision-language-action (VLA) model, reducing dataset size by filtering out suboptimal and redundant state-action pairs.

**4. Demonstration Information Estimation (DemInf) (2025)**
DemInf is a method for data curation in robot imitation learning that uses mutual information as a basis for measuring the quality of individual demonstrations and instantiates mutual information estimators as a way to rank and select demonstrations.

These papers all address the core challenge of filtering and curating high-quality demonstration data for robot imitation learning and VLA models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85f63cae-4c06-406d-b859-dcf88e77150c",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "d1cda93f-c4bd-47b7-b786-7b05d0406aa2",
  "toolUseResult": {
    "query": "VLA data curation demonstration quality filtering 2026 arxiv robot imitation learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HzyVSCHNUxLc8eFvSZoSDs",
        "content": [
          {
            "title": "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/html/2603.09056"
          },
          {
            "title": "CUPID: Curating Data your Robot Loves with Influence Functions",
            "url": "https://arxiv.org/html/2506.19121v1"
          },
          {
            "title": "Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning",
            "url": "https://arxiv.org/html/2505.22626v2"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2602.00919v1"
          },
          {
            "title": "Robot Data Curation with Mutual Information Estimators",
            "url": "https://arxiv.org/html/2502.08623"
          },
          {
            "title": "[2306.02437] Data Quality in Imitation Learning",
            "url": "https://arxiv.org/abs/2306.02437"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/abs/2603.09056"
          },
          {
            "title": "[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning",
            "url": "https://arxiv.org/abs/2505.22626"
          },
          {
            "title": "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning",
            "url": "https://arxiv.org/html/2408.14037v1"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on VLA data curation and demonstration quality filtering from 2026 and recent years on arXiv:\n\n## Key Papers Found:\n\n**1. Quality over Quantity (2026)**\nQuality over Quantity (QoQ) is a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. QoQ is particularly well-suited for scaling to modern VLAs, which involve billions of parameters.\n\n**2. CUPID: Curating Data your Robot Loves with Influence Functions (2025)**\nCUPID is a novel data curation method that uses influence functions to measure the causal impact of a demonstration on the policy's closed-loop performance, highlighting the general utility of performance-based curation for filtering existing training demonstrations and subselecting new demonstrations.\n\n**3. Scizor: A Self-Supervised Approach to Data Curation (2025)**\nScizor is the first self-supervised, transition-level data curation method that scales to the Open-X Embodiment Dataset with more than one million trajectories for large-scale models such as the Octo vision-language-action (VLA) model, reducing dataset size by filtering out suboptimal and redundant state-action pairs.\n\n**4. Demonstration Information Estimation (DemInf) (2025)**\nDemInf is a method for data curation in robot imitation learning that uses mutual information as a basis for measuring the quality of individual demonstrations and instantiates mutual information estimators as a way to rank and select demonstrations.\n\nThese papers all address the core challenge of filtering and curating high-quality demonstration data for robot imitation learning and VLA models."
    ],
    "durationSeconds": 7.4528361589999985
  },
  "sourceToolAssistantUUID": "85f63cae-4c06-406d-b859-dcf88e77150c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T11:40:06.783Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MNZBfiNqEQ9fT3UKkaDnhL`</summary>

```json
{
  "query": "\"Quality over Quantity\" demonstration curation influence functions VLA 2603.09056 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1cda93f-c4bd-47b7-b786-7b05d0406aa2",
  "isSidechain": false,
  "requestId": "req_011CazWD8nG1pzVYhhpvMXXt",
  "type": "assistant",
  "uuid": "216bc73c-41df-4015-ad1a-ae3001337779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwAJSoanrXkrjaf3Bw2RHu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 41452,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 41452,
          "cache_creation_input_tokens": 930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 930
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T11:40:12.499Z_

<details><summary>↩ Tool result · `toolu_01MNZBfiNqEQ9fT3UKkaDnhL`</summary>

```text
Web search results for query: ""Quality over Quantity" demonstration curation influence functions VLA 2603.09056 2026"

Links: [{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[2502.08211] Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation","url":"https://arxiv.org/abs/2502.08211"},{"title":"Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio–Video Foundation Model","url":"https://arxiv.org/html/2503.09205v1"},{"title":"Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/quality-over-quantity-llm-based-curation-data"},{"title":"Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250208211X/abstract"},{"title":"From Quantity to Quality: Boosting LLM Performance with Self-Guided Data Selection for Instruction Tuning","url":"https://arxiv.org/html/2308.12032v4"},{"title":"[2503.09205] Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model","url":"https://arxiv.org/abs/2503.09205"},{"title":"IF-CPS: Influence Functions for Cyber-Physical Systems— A Unified Framework for Diagnosis, Curation, and Safety Attribution","url":"https://arxiv.org/html/2603.21543"},{"title":"[2308.12032] From Quantity to Quality: Boosting LLM Performance with Self-Guided Data Selection for Instruction Tuning","url":"https://arxiv.org/abs/2308.12032"}]

Based on the search results, I found the paper you're looking for:

"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning" is the paper with identifier arXiv:2603.09056. 

The paper was authored by Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, and Kimin Lee from KAIST, UC Berkeley, and New York University, and was submitted on March 10, 2026.

The paper proposes Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. The work addresses the critical bottleneck of demonstration data quality in robot learning, where human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors.

The approach is particularly well-suited for scaling to modern VLAs (Vision Language Actions models), which involve billions of parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "216bc73c-41df-4015-ad1a-ae3001337779",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "b76b5916-1073-48ff-87a2-da0b9b8c75d8",
  "toolUseResult": {
    "query": "\"Quality over Quantity\" demonstration curation influence functions VLA 2603.09056 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ry6vVzELBpUeMG6faaGCcA",
        "content": [
          {
            "title": "[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/abs/2603.09056"
          },
          {
            "title": "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/html/2603.09056"
          },
          {
            "title": "[2502.08211] Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation",
            "url": "https://arxiv.org/abs/2502.08211"
          },
          {
            "title": "Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio–Video Foundation Model",
            "url": "https://arxiv.org/html/2503.09205v1"
          },
          {
            "title": "Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/quality-over-quantity-llm-based-curation-data"
          },
          {
            "title": "Quality over Quantity: Boosting Data Efficiency Through Ensembled Multimodal Data Curation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250208211X/abstract"
          },
          {
            "title": "From Quantity to Quality: Boosting LLM Performance with Self-Guided Data Selection for Instruction Tuning",
            "url": "https://arxiv.org/html/2308.12032v4"
          },
          {
            "title": "[2503.09205] Quality Over Quantity? LLM-Based Curation for a Data-Efficient Audio-Video Foundation Model",
            "url": "https://arxiv.org/abs/2503.09205"
          },
          {
            "title": "IF-CPS: Influence Functions for Cyber-Physical Systems— A Unified Framework for Diagnosis, Curation, and Safety Attribution",
            "url": "https://arxiv.org/html/2603.21543"
          },
          {
            "title": "[2308.12032] From Quantity to Quality: Boosting LLM Performance with Self-Guided Data Selection for Instruction Tuning",
            "url": "https://arxiv.org/abs/2308.12032"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning\" is the paper with identifier arXiv:2603.09056. \n\nThe paper was authored by Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, and Kimin Lee from KAIST, UC Berkeley, and New York University, and was submitted on March 10, 2026.\n\nThe paper proposes Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. The work addresses the critical bottleneck of demonstration data quality in robot learning, where human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors.\n\nThe approach is particularly well-suited for scaling to modern VLAs (Vision Language Actions models), which involve billions of parameters."
    ],
    "durationSeconds": 5.711251801000006
  },
  "sourceToolAssistantUUID": "216bc73c-41df-4015-ad1a-ae3001337779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-13T11:40:15.681Z_

This is an important find — a new paper from March 2026 that the proposal doesn't cite. Let me search more deeply for competitive work and verify other claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b76b5916-1073-48ff-87a2-da0b9b8c75d8",
  "isSidechain": false,
  "requestId": "req_011CazWDwpj8KUWP62jkwe42",
  "type": "assistant",
  "uuid": "583af3cd-ff03-4085-8b8c-f8f18b237099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HL3LdtpYcdJ6z7kDZRcX4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 42382,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 42382,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T11:40:16.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XSWuv4kP6wtpipYdPTq8e7`</summary>

```json
{
  "query": "reducible loss prioritized sampling SFT VLA imitation learning noise filtering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "583af3cd-ff03-4085-8b8c-f8f18b237099",
  "isSidechain": false,
  "requestId": "req_011CazWDwpj8KUWP62jkwe42",
  "type": "assistant",
  "uuid": "bdf4227b-a420-40c9-94af-570911d4c5ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HL3LdtpYcdJ6z7kDZRcX4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 42382,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 42382,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T11:40:24.892Z_

<details><summary>↩ Tool result · `toolu_01XSWuv4kP6wtpipYdPTq8e7`</summary>

```text
Web search results for query: "reducible loss prioritized sampling SFT VLA imitation learning noise filtering 2026"

Links: [{"title":"[2208.10483] Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://arxiv.org/abs/2208.10483"},{"title":"PRIORITIZED TRAINING ON POINTS THAT ARE LEARN","url":"https://openreview.net/pdf?id=Y0cGpgUhSvp"},{"title":"Prioritizing samples in reinforcement learning with reducible loss | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667130"},{"title":"ReLo: Reducible Loss for RL","url":"https://shivakanthsujit.github.io/reducible-loss/"},{"title":"(PDF) Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://www.researchgate.net/publication/362859466_Prioritizing_Samples_in_Reinforcement_Learning_with_Reducible_Loss"},{"title":"Provably Mitigating Overoptimization in RLHF: Your SFT ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/fa69e968b7319fd42524febd41475fb3-Paper-Conference.pdf"},{"title":"ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy","url":"https://arxiv.org/html/2502.05450"},{"title":"[2206.07137] Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt","url":"https://ar5iv.labs.arxiv.org/html/2206.07137"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"[2405.16436] Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer","url":"https://arxiv.org/abs/2405.16436"}]

I found relevant research related to your query. Here are the key findings:

## Reducible Loss and Prioritized Sampling

The research develops an algorithm to prioritize samples with high learn-ability, while assigning lower priority to those that are hard-to-learn, typically caused by noise or stochasticity. Learn-ability of a sample is defined as the steady decrease of the training loss associated with this sample over time.

Vanilla PER focuses on data points with high TD loss, but such points could have high loss because they are noisy or not learnable by the model. Instead of prioritization based on the TD error, researchers propose that the agent should focus on samples that have higher reducible TD error, using a measure of how much the TD error can be potentially decreased.

## Noise Filtering in Training

Research on this topic addresses a critical problem: in real-world noisy datasets, high loss examples may be mislabelled or ambiguous. In controlled experiments, points selected by high loss or gradient norm are overwhelmingly those with noise-corrupted labels, and this failure mode degrades performance severely.

## VLA and Imitation Learning (SFT)

Recent advancements in training generalist robotic policies using Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in understanding and executing various manipulation tasks, primarily attributed to large-scale imitation-style pre-training and grounding with robot actions.

The search results contain several relevant papers from 2022-2025, though I did not find a specific paper specifically combining all these terms (reducible loss, prioritized sampling, SFT, VLA, imitation learning, and noise filtering) in a single work from 2026. The results show this is an active research area with work on individual components of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdf4227b-a420-40c9-94af-570911d4c5ec",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "58a45971-8d5e-4945-b456-79ab1e4ce97c",
  "toolUseResult": {
    "query": "reducible loss prioritized sampling SFT VLA imitation learning noise filtering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016yRYt8hhR2vZk9gxjFKERw",
        "content": [
          {
            "title": "[2208.10483] Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://arxiv.org/abs/2208.10483"
          },
          {
            "title": "PRIORITIZED TRAINING ON POINTS THAT ARE LEARN",
            "url": "https://openreview.net/pdf?id=Y0cGpgUhSvp"
          },
          {
            "title": "Prioritizing samples in reinforcement learning with reducible loss | Proceedings of the 37th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3666122.3667130"
          },
          {
            "title": "ReLo: Reducible Loss for RL",
            "url": "https://shivakanthsujit.github.io/reducible-loss/"
          },
          {
            "title": "(PDF) Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://www.researchgate.net/publication/362859466_Prioritizing_Samples_in_Reinforcement_Learning_with_Reducible_Loss"
          },
          {
            "title": "Provably Mitigating Overoptimization in RLHF: Your SFT ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/fa69e968b7319fd42524febd41475fb3-Paper-Conference.pdf"
          },
          {
            "title": "ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy",
            "url": "https://arxiv.org/html/2502.05450"
          },
          {
            "title": "[2206.07137] Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt",
            "url": "https://ar5iv.labs.arxiv.org/html/2206.07137"
          },
          {
            "title": "SimpleVLA-RL: Scalable VLA Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/simplevla-rl"
          },
          {
            "title": "[2405.16436] Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer",
            "url": "https://arxiv.org/abs/2405.16436"
          }
        ]
      },
      "I found relevant research related to your query. Here are the key findings:\n\n## Reducible Loss and Prioritized Sampling\n\nThe research develops an algorithm to prioritize samples with high learn-ability, while assigning lower priority to those that are hard-to-learn, typically caused by noise or stochasticity. Learn-ability of a sample is defined as the steady decrease of the training loss associated with this sample over time.\n\nVanilla PER focuses on data points with high TD loss, but such points could have high loss because they are noisy or not learnable by the model. Instead of prioritization based on the TD error, researchers propose that the agent should focus on samples that have higher reducible TD error, using a measure of how much the TD error can be potentially decreased.\n\n## Noise Filtering in Training\n\nResearch on this topic addresses a critical problem: in real-world noisy datasets, high loss examples may be mislabelled or ambiguous. In controlled experiments, points selected by high loss or gradient norm are overwhelmingly those with noise-corrupted labels, and this failure mode degrades performance severely.\n\n## VLA and Imitation Learning (SFT)\n\nRecent advancements in training generalist robotic policies using Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in understanding and executing various manipulation tasks, primarily attributed to large-scale imitation-style pre-training and grounding with robot actions.\n\nThe search results contain several relevant papers from 2022-2025, though I did not find a specific paper specifically combining all these terms (reducible loss, prioritized sampling, SFT, VLA, imitation learning, and noise filtering) in a single work from 2026. The results show this is an active research area with work on individual components of your query."
    ],
    "durationSeconds": 8.379105341999995
  },
  "sourceToolAssistantUUID": "bdf4227b-a420-40c9-94af-570911d4c5ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-13T11:40:24.934Z_

```json
{
  "parentUuid": "58a45971-8d5e-4945-b456-79ab1e4ce97c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9cc28660-89b3-495c-91e3-dd11ed293f7a",
  "timestamp": "2026-05-13T11:40:24.934Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-13T11:40:27.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WTKWzqusi8eYGu6dTenhst`</summary>

```json
{
  "query": "SFT data quality affects downstream RL performance VLA robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc28660-89b3-495c-91e3-dd11ed293f7a",
  "isSidechain": false,
  "requestId": "req_011CazWEsQ73fqUGmvq2S4S4",
  "type": "assistant",
  "uuid": "7be0f7ba-fd62-45df-a18d-f3491f0c536a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYj1ekvzmKHU1BzHquJqMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 43285,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 43285,
          "cache_creation_input_tokens": 1183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1183
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T11:40:37.361Z_

<details><summary>↩ Tool result · `toolu_01WTKWzqusi8eYGu6dTenhst`</summary>

```text
Web search results for query: "SFT data quality affects downstream RL performance VLA robot 2025 2026"

Links: [{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091v1"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2602.10503"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"}]

Based on the search results, I found several recent papers (2025-2026) that discuss how SFT (Supervised Fine-Tuning) data quality affects downstream RL (Reinforcement Learning) performance in VLA (Vision-Language-Action) robot models. Here are the key findings:

## Key Issues with SFT Data Quality

Standard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting of pre-trained capabilities, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency.

Collecting high-quality robot demonstrations is both costly and labor-intensive, making large-scale datasets much harder to obtain. Even when such data are available, they are often collected through teleoperation pipelines that are decoupled from the deployed VLA policy, leaving critical coverage gaps: human operators must manually anticipate and correct failure modes, but their demonstrations rarely reflect the actual distribution of states the policy will encounter at deployment.

## Data Quality Impact on Downstream Performance

SFT methods require extensive manual collection of robot-human paired trajectories, leading to overfitting and poor resilience to unseen scene configurations or object variations.

Offline SFT exhibits severe forgetting: as seen-task success improves, unseen performance collapses—approaching zero for Object tasks and dropping substantially for Spatial tasks—confirming that optimizing solely on offline trajectories quickly erodes pre-trained skills due to distribution shifts.

## Solutions Through RL-Generated Data

Research analyzes the key components of automatic data collection most beneficial for SFT, and conducts extensive experiments in simulation and on real robot hardware to examine how RL-generated data influences generalization to unseen tasks. Results show that residual policy probing and distribution-aware replay are key to collecting deployment-aligned data that improves VLAs' capabilities on both seen and unseen tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7be0f7ba-fd62-45df-a18d-f3491f0c536a",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "f403f3f7-53f1-4227-b652-cd4305e80950",
  "toolUseResult": {
    "query": "SFT data quality affects downstream RL performance VLA robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015oStXSakvqwvPuPd8FwpkV",
        "content": [
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for...",
            "url": "https://arxiv.org/abs/2603.26666"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL",
            "url": "https://arxiv.org/html/2511.00091v1"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.18719v1"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          },
          {
            "title": "SimpleVLA-RL: Scalable VLA Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/simplevla-rl"
          },
          {
            "title": "Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning",
            "url": "https://arxiv.org/html/2602.10503"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "2025-9-18 ThinkAct: Vision-Language-Action Reasoning via",
            "url": "https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          }
        ]
      },
      "Based on the search results, I found several recent papers (2025-2026) that discuss how SFT (Supervised Fine-Tuning) data quality affects downstream RL (Reinforcement Learning) performance in VLA (Vision-Language-Action) robot models. Here are the key findings:\n\n## Key Issues with SFT Data Quality\n\nStandard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting of pre-trained capabilities, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency.\n\nCollecting high-quality robot demonstrations is both costly and labor-intensive, making large-scale datasets much harder to obtain. Even when such data are available, they are often collected through teleoperation pipelines that are decoupled from the deployed VLA policy, leaving critical coverage gaps: human operators must manually anticipate and correct failure modes, but their demonstrations rarely reflect the actual distribution of states the policy will encounter at deployment.\n\n## Data Quality Impact on Downstream Performance\n\nSFT methods require extensive manual collection of robot-human paired trajectories, leading to overfitting and poor resilience to unseen scene configurations or object variations.\n\nOffline SFT exhibits severe forgetting: as seen-task success improves, unseen performance collapses—approaching zero for Object tasks and dropping substantially for Spatial tasks—confirming that optimizing solely on offline trajectories quickly erodes pre-trained skills due to distribution shifts.\n\n## Solutions Through RL-Generated Data\n\nResearch analyzes the key components of automatic data collection most beneficial for SFT, and conducts extensive experiments in simulation and on real robot hardware to examine how RL-generated data influences generalization to unseen tasks. Results show that residual policy probing and distribution-aware replay are key to collecting deployment-aligned data that improves VLAs' capabilities on both seen and unseen tasks."
    ],
    "durationSeconds": 9.393491593999991
  },
  "sourceToolAssistantUUID": "7be0f7ba-fd62-45df-a18d-f3491f0c536a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f403f3f7-53f1-4227-b652-cd4305e80950",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool call

_source line 35 · 2026-05-13T11:40:40.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016iXbiwjTZ7tNUhiWf8iU5q`</summary>

```json
{
  "query": "VLA-RL \"VLA-RL\" 2505.18719 scalable reinforcement learning robotic manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f403f3f7-53f1-4227-b652-cd4305e80950",
  "isSidechain": false,
  "requestId": "req_011CazWFn9cyGVAUuccTLR8G",
  "type": "assistant",
  "uuid": "96306199-3516-4b37-9ccd-82d8256eee28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZDcEUVyVXbFKbuNdnaWHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 44468,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 44468,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T11:40:47.986Z_

<details><summary>↩ Tool result · `toolu_016iXbiwjTZ7tNUhiWf8iU5q`</summary>

```text
Web search results for query: "VLA-RL "VLA-RL" 2505.18719 scalable reinforcement learning robotic manipulation 2026"

Links: [{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518719L/abstract"},{"title":"GitHub - GuanxingLu/vlarl: Single-file implementation to advance vision-language-action (VLA) models with reinforcement learning. · GitHub","url":"https://github.com/GuanxingLu/vlarl"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.18719"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/392104761_VLA-RL_Towards_Masterful_and_General_Robotic_Manipulation_with_Scalable_Reinforcement_Learning"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"[2509.09674v1] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674v1"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"}]

Based on the search results, here's what I found about VLA-RL (arxiv 2505.18719):

## Overview

VLA-RL is an algorithmic and systematic framework that leverages online reinforcement learning (RL) to improve pretrained auto-regressive VLAs in downstream tasks.

## Problem It Addresses

Recent high-capacity vision-language-action (VLA) models have demonstrated impressive performance on a range of robotic manipulation tasks by imitating human demonstrations. However, exploiting offline data with limited visited states will cause execution failure in out-of-distribution scenarios.

## Key Technical Contributions

VLA-RL introduces a trajectory-level RL formulation for auto-regressive VLA training, which models general robotic manipulation trajectory as multi-modal multi-turn conversation. To address the challenge of sparse rewards, it fine-tunes a pretrained vision-language model as a robotic process reward model, which is trained on pseudo reward labels annotated on automatically extracted task segments.

To scale up, several implementation findings improve the stability and efficiency including curriculum selection strategy, GPU-balanced vectorized environments, batch decoding, and critic warmup.

## Performance Results

VLA-RL enables OpenVLA-7B to surpass the strongest finetuned baseline by 4.5% on 40 challenging robotic manipulation tasks in LIBERO, and even matches the performance of advanced commercial models such as π₀-FAST.

The observation that performance scales with test-time optimization suggests an emerging principle analogous to inference scaling laws in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96306199-3516-4b37-9ccd-82d8256eee28",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "4ace7317-a640-4b39-bdc3-4af4c1ae70e9",
  "toolUseResult": {
    "query": "VLA-RL \"VLA-RL\" 2505.18719 scalable reinforcement learning robotic manipulation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HbjxisMPZhesFFZyHTbmFv",
        "content": [
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.18719v1"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=TQhSodCM4r"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250518719L/abstract"
          },
          {
            "title": "GitHub - GuanxingLu/vlarl: Single-file implementation to advance vision-language-action (VLA) models with reinforcement learning. · GitHub",
            "url": "https://github.com/GuanxingLu/vlarl"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2505.18719"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/392104761_VLA-RL_Towards_Masterful_and_General_Robotic_Manipulation_with_Scalable_Reinforcement_Learning"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          },
          {
            "title": "[2509.09674v1] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.09674v1"
          },
          {
            "title": "[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.09674"
          }
        ]
      },
      "Based on the search results, here's what I found about VLA-RL (arxiv 2505.18719):\n\n## Overview\n\nVLA-RL is an algorithmic and systematic framework that leverages online reinforcement learning (RL) to improve pretrained auto-regressive VLAs in downstream tasks.\n\n## Problem It Addresses\n\nRecent high-capacity vision-language-action (VLA) models have demonstrated impressive performance on a range of robotic manipulation tasks by imitating human demonstrations. However, exploiting offline data with limited visited states will cause execution failure in out-of-distribution scenarios.\n\n## Key Technical Contributions\n\nVLA-RL introduces a trajectory-level RL formulation for auto-regressive VLA training, which models general robotic manipulation trajectory as multi-modal multi-turn conversation. To address the challenge of sparse rewards, it fine-tunes a pretrained vision-language model as a robotic process reward model, which is trained on pseudo reward labels annotated on automatically extracted task segments.\n\nTo scale up, several implementation findings improve the stability and efficiency including curriculum selection strategy, GPU-balanced vectorized environments, batch decoding, and critic warmup.\n\n## Performance Results\n\nVLA-RL enables OpenVLA-7B to surpass the strongest finetuned baseline by 4.5% on 40 challenging robotic manipulation tasks in LIBERO, and even matches the performance of advanced commercial models such as π₀-FAST.\n\nThe observation that performance scales with test-time optimization suggests an emerging principle analogous to inference scaling laws in language models."
    ],
    "durationSeconds": 7.733238981999995
  },
  "sourceToolAssistantUUID": "96306199-3516-4b37-9ccd-82d8256eee28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T11:40:50.497Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UA6kZm5MgEcaN9NjuohSCq`</summary>

```json
{
  "query": "online data selection training prioritization noisy demonstrations behavior cloning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ace7317-a640-4b39-bdc3-4af4c1ae70e9",
  "isSidechain": false,
  "requestId": "req_011CazWGZYsJwUrxxMPPa519",
  "type": "assistant",
  "uuid": "cda7e0a7-08da-4b97-be95-39473457c03a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173xPuqfqyDrkKyjWJx7dL3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 45488,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 45488,
          "cache_creation_input_tokens": 1048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1048
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T11:40:58.133Z_

<details><summary>↩ Tool result · `toolu_01UA6kZm5MgEcaN9NjuohSCq`</summary>

```text
Web search results for query: "online data selection training prioritization noisy demonstrations behavior cloning 2025 2026"

Links: [{"title":"Behavior Cloning from Suboptimal Demonstrations with Robust World Models | OpenReview","url":"https://openreview.net/forum?id=PZwpFrNNYn"},{"title":"Behavioral Cloning from Noisy Demonstrations | OpenReview","url":"https://openreview.net/forum?id=zrT3HcsWSAt"},{"title":"BEHAVIORAL CLONING FROM NOISY DEMONSTRA","url":"https://openreview.net/pdf?id=zrT3HcsWSAt"},{"title":"Counterfactual Behavior Cloning: Offline Imitation Learning","url":"https://collab.me.vt.edu/pdfs/losey_thri2025.pdf"},{"title":"Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks: Journal of the Chinese Institute of Engineers: Vol 48 , No 6 - Get Access","url":"https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354"},{"title":"Better-than-Demonstrator Imitation Learning via Automatically ...","url":"http://proceedings.mlr.press/v100/brown20a/brown20a.pdf"},{"title":"ICLR 2021 Behavioral Cloning from Noisy Demonstrations Spotlight","url":"https://iclr.cc/virtual/2021/spotlight/3447"},{"title":"Discriminator-Weighted Offline Imitation Learning from ...","url":"https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"},{"title":"Behavioral Cloning in Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning-bc"},{"title":"Constrained Behavior Cloning for Robotic Learning","url":"https://arxiv.org/html/2408.10568v1"}]

I've performed a web search on your query about online data selection training prioritization, noisy demonstrations, and behavior cloning for 2025-2026. Here are the relevant research findings:

## Recent Research on Behavior Cloning with Noisy Data

Recent work on behavior cloning addresses the challenge of learning from low-quality data, with existing methods often requiring filtering or reweighting of failed or noisy demonstrations. 

One approach, Robust Imitation with a Critic (RIC), utilizes a critic-regularized imitation learning objective to incorporate both successful and failed demonstrations, steering imitation learning towards better trajectories via a conservative critic.

## Data Selection and Prioritization Approaches

A recent discriminator-weighted approach introduces an additional discriminator to the behavioral cloning method, which analytically weighs all data to distinguish between optimal and suboptimal instances, with this discriminative weighting influencing policy learning and preventing suboptimal behavior.

Research finds that extrapolating what the human teacher meant — as opposed to rigorously following what the human actually demonstrated — leads to more proficient learning from humans.

## Automatic Ranking Methods

One technique injects noise into a policy learned through behavioral cloning to automatically generate ranked policies of varying performance, and by progressively adding more noise, researchers can automatically synthesize a preference ranking that is used to learn a reward function optimized using reinforcement learning.

The research shows significant progress in 2025-2026 on handling noisy demonstrations through discriminative weighting, critic guidance, and automatic ranking mechanisms, rather than requiring manual data filtering or annotation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda7e0a7-08da-4b97-be95-39473457c03a",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "7426a064-5108-482f-8b61-b93826804684",
  "toolUseResult": {
    "query": "online data selection training prioritization noisy demonstrations behavior cloning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FyHpZUhGP4jw5vLH9SyvUs",
        "content": [
          {
            "title": "Behavior Cloning from Suboptimal Demonstrations with Robust World Models | OpenReview",
            "url": "https://openreview.net/forum?id=PZwpFrNNYn"
          },
          {
            "title": "Behavioral Cloning from Noisy Demonstrations | OpenReview",
            "url": "https://openreview.net/forum?id=zrT3HcsWSAt"
          },
          {
            "title": "BEHAVIORAL CLONING FROM NOISY DEMONSTRA",
            "url": "https://openreview.net/pdf?id=zrT3HcsWSAt"
          },
          {
            "title": "Counterfactual Behavior Cloning: Offline Imitation Learning",
            "url": "https://collab.me.vt.edu/pdfs/losey_thri2025.pdf"
          },
          {
            "title": "Discriminator-weighted offline imitation learning with unlabeled demonstrations for robotic tasks: Journal of the Chinese Institute of Engineers: Vol 48 , No 6 - Get Access",
            "url": "https://www.tandfonline.com/doi/full/10.1080/02533839.2025.2517354"
          },
          {
            "title": "Better-than-Demonstrator Imitation Learning via Automatically ...",
            "url": "http://proceedings.mlr.press/v100/brown20a/brown20a.pdf"
          },
          {
            "title": "ICLR 2021 Behavioral Cloning from Noisy Demonstrations Spotlight",
            "url": "https://iclr.cc/virtual/2021/spotlight/3447"
          },
          {
            "title": "Discriminator-Weighted Offline Imitation Learning from ...",
            "url": "https://proceedings.mlr.press/v162/xu22l/xu22l.pdf"
          },
          {
            "title": "Behavioral Cloning in Imitation Learning",
            "url": "https://www.emergentmind.com/topics/behavioral-cloning-bc"
          },
          {
            "title": "Constrained Behavior Cloning for Robotic Learning",
            "url": "https://arxiv.org/html/2408.10568v1"
          }
        ]
      },
      "I've performed a web search on your query about online data selection training prioritization, noisy demonstrations, and behavior cloning for 2025-2026. Here are the relevant research findings:\n\n## Recent Research on Behavior Cloning with Noisy Data\n\nRecent work on behavior cloning addresses the challenge of learning from low-quality data, with existing methods often requiring filtering or reweighting of failed or noisy demonstrations. \n\nOne approach, Robust Imitation with a Critic (RIC), utilizes a critic-regularized imitation learning objective to incorporate both successful and failed demonstrations, steering imitation learning towards better trajectories via a conservative critic.\n\n## Data Selection and Prioritization Approaches\n\nA recent discriminator-weighted approach introduces an additional discriminator to the behavioral cloning method, which analytically weighs all data to distinguish between optimal and suboptimal instances, with this discriminative weighting influencing policy learning and preventing suboptimal behavior.\n\nResearch finds that extrapolating what the human teacher meant — as opposed to rigorously following what the human actually demonstrated — leads to more proficient learning from humans.\n\n## Automatic Ranking Methods\n\nOne technique injects noise into a policy learned through behavioral cloning to automatically generate ranked policies of varying performance, and by progressively adding more noise, researchers can automatically synthesize a preference ranking that is used to learn a reward function optimized using reinforcement learning.\n\nThe research shows significant progress in 2025-2026 on handling noisy demonstrations through discriminative weighting, critic guidance, and automatic ranking mechanisms, rather than requiring manual data filtering or annotation."
    ],
    "durationSeconds": 7.632079522999993
  },
  "sourceToolAssistantUUID": "cda7e0a7-08da-4b97-be95-39473457c03a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T11:41:01.245Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAVDBgceNXT8sbLDXtHdnP`</summary>

```json
{
  "query": "PRISM \"pre-alignment\" \"on-policy distillation\" multimodal reinforcement learning 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7426a064-5108-482f-8b61-b93826804684",
  "isSidechain": false,
  "requestId": "req_011CazWHK12hLw8P1D13yeBf",
  "type": "assistant",
  "uuid": "bfeadb2d-eda1-4c59-bc7b-d558b2f8d687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVe1nfEkFCv6LJnJa5DrKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 46536,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 46536,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 932
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T11:41:08.040Z_

<details><summary>↩ Tool result · `toolu_01QAVDBgceNXT8sbLDXtHdnP`</summary>

```text
Web search results for query: "PRISM "pre-alignment" "on-policy distillation" multimodal reinforcement learning 2604"

Links: [{"title":"[2604.28123] PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning","url":"https://arxiv.org/abs/2604.28123"},{"title":"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning","url":"https://arxiv.org/html/2604.28123"},{"title":"GitHub - XIAO4579/PRISM: Beyond SFT-to-RL: Pre-alignment via Black-BoxOn-Policy Distillation for Multimodal RL · GitHub","url":"https://github.com/XIAO4579/PRISM"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"}]

I found the research paper on your query. Here's what I found:

PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning is a paper (arXiv:2604.28123) that addresses challenges in post-training large multimodal models.

**Problem it addresses:** The standard post-training recipe for large multimodal models applies supervised fine-tuning (SFT) on curated demonstrations followed by reinforcement learning with verifiable rewards (RLVR). However, SFT introduces distributional drift that neither preserves the model's original capabilities nor faithfully matches the supervision distribution.

**The solution:** PRISM is a three-stage pipeline that mitigates this drift by inserting an explicit distribution-alignment stage between SFT and RLVR. Building on the principle of on-policy distillation (OPD), PRISM casts alignment as a black-box, response-level adversarial game between the policy and a Mixture-of-Experts (MoE) discriminator with dedicated perception and reasoning experts, providing disentangled corrective signals that steer the policy toward the supervision distribution.

Experiments on Qwen3-VL show that PRISM consistently improves downstream RLVR performance across multiple RL algorithms (GRPO, DAPO, GSPO) and diverse multimodal benchmarks.

The paper was published in April 2026, and the code, data, and model checkpoints of PRISM have been released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfeadb2d-eda1-4c59-bc7b-d558b2f8d687",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "d2f3b157-9cb1-4e14-b35c-48bd25d4b6c5",
  "toolUseResult": {
    "query": "PRISM \"pre-alignment\" \"on-policy distillation\" multimodal reinforcement learning 2604",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DpNCHPqKFUXVRVH97hgmEw",
        "content": [
          {
            "title": "[2604.28123] PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2604.28123"
          },
          {
            "title": "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/html/2604.28123"
          },
          {
            "title": "GitHub - XIAO4579/PRISM: Beyond SFT-to-RL: Pre-alignment via Black-BoxOn-Policy Distillation for Multimodal RL · GitHub",
            "url": "https://github.com/XIAO4579/PRISM"
          },
          {
            "title": "GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR"
          }
        ]
      },
      "I found the research paper on your query. Here's what I found:\n\nPRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning is a paper (arXiv:2604.28123) that addresses challenges in post-training large multimodal models.\n\n**Problem it addresses:** The standard post-training recipe for large multimodal models applies supervised fine-tuning (SFT) on curated demonstrations followed by reinforcement learning with verifiable rewards (RLVR). However, SFT introduces distributional drift that neither preserves the model's original capabilities nor faithfully matches the supervision distribution.\n\n**The solution:** PRISM is a three-stage pipeline that mitigates this drift by inserting an explicit distribution-alignment stage between SFT and RLVR. Building on the principle of on-policy distillation (OPD), PRISM casts alignment as a black-box, response-level adversarial game between the policy and a Mixture-of-Experts (MoE) discriminator with dedicated perception and reasoning experts, providing disentangled corrective signals that steer the policy toward the supervision distribution.\n\nExperiments on Qwen3-VL show that PRISM consistently improves downstream RLVR performance across multiple RL algorithms (GRPO, DAPO, GSPO) and diverse multimodal benchmarks.\n\nThe paper was published in April 2026, and the code, data, and model checkpoints of PRISM have been released."
    ],
    "durationSeconds": 6.790220018000007
  },
  "sourceToolAssistantUUID": "bfeadb2d-eda1-4c59-bc7b-d558b2f8d687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T11:41:11.126Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PF9PxqYkFmyMxv4TU8QJHo`</summary>

```json
{
  "query": "\"Quality over Quantity\" 2603.09056 CUPID influence functions VLA demonstration curation 2026 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2f3b157-9cb1-4e14-b35c-48bd25d4b6c5",
  "isSidechain": false,
  "requestId": "req_011CazWJ3Fmffrk36SjEFwFv",
  "type": "assistant",
  "uuid": "572aa878-8fc5-485d-9254-f368a66cb22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxBHTdphQYgB7Ufhqfxx7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 47468,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 47468,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T11:41:16.784Z_

<details><summary>↩ Tool result · `toolu_01PF9PxqYkFmyMxv4TU8QJHo`</summary>

```text
Web search results for query: ""Quality over Quantity" 2603.09056 CUPID influence functions VLA demonstration curation 2026 venue"

Links: [{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"IF-CPS: Influence Functions for Cyber-Physical Systems— A Unified Framework for Diagnosis, Curation, and Safety Attribution","url":"https://arxiv.org/html/2603.21543"},{"title":"Why do people say quality over quantity? - Quora","url":"https://www.quora.com/Why-do-people-say-quality-over-quantity"}]

I found the paper you're looking for! Here's what the search revealed:

"Quality over Quantity" (QoQ) is a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. The paper was submitted to arXiv on March 10, 2026.

The authors are Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, and Kimin Lee, affiliated with KAIST, UC Berkeley, and New York University.

Regarding the connection to VLAs and demonstration curation: QoQ is particularly well-suited for scaling to modern Vision-Language-Action models (VLAs), which involve billions of parameters. The paper relates this to CUPID, which uses returns estimated from policy rollouts to curate robot data.

The paper (arxiv.org/abs/2603.09056) focuses on data curation for robot learning using influence functions to identify and select high-quality demonstration data, which is essential for effective data-driven robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "572aa878-8fc5-485d-9254-f368a66cb22c",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "84dd551f-951c-43fe-a498-22ee665faa29",
  "toolUseResult": {
    "query": "\"Quality over Quantity\" 2603.09056 CUPID influence functions VLA demonstration curation 2026 venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ACbFDdjPZQ4XKtTj2RVrML",
        "content": [
          {
            "title": "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/html/2603.09056"
          },
          {
            "title": "[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/abs/2603.09056"
          },
          {
            "title": "CUPID: Curating Data your Robot Loves with Influence Functions",
            "url": "https://arxiv.org/html/2506.19121v1"
          },
          {
            "title": "CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview",
            "url": "https://openreview.net/forum?id=TqevdDMqrK"
          },
          {
            "title": "CUPID: Robot Data Curation via Influence Functions",
            "url": "https://www.emergentmind.com/papers/2506.19121"
          },
          {
            "title": "[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions",
            "url": "https://arxiv.org/abs/2506.19121"
          },
          {
            "title": "[PDF] CUPID: Curating Data your Robot Loves with Influence Functions | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CUPID:-Curating-Data-your-Robot-Loves-with-Agia-Sinha/666481cd9e72de8e90e3dd12fb826338f5ce17f0"
          },
          {
            "title": "CUPID: Curating Data your Robot Loves with Influence Functions",
            "url": "https://proceedings.mlr.press/v305/agia25a.html"
          },
          {
            "title": "IF-CPS: Influence Functions for Cyber-Physical Systems— A Unified Framework for Diagnosis, Curation, and Safety Attribution",
            "url": "https://arxiv.org/html/2603.21543"
          },
          {
            "title": "Why do people say quality over quantity? - Quora",
            "url": "https://www.quora.com/Why-do-people-say-quality-over-quantity"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\n\"Quality over Quantity\" (QoQ) is a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. The paper was submitted to arXiv on March 10, 2026.\n\nThe authors are Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, and Kimin Lee, affiliated with KAIST, UC Berkeley, and New York University.\n\nRegarding the connection to VLAs and demonstration curation: QoQ is particularly well-suited for scaling to modern Vision-Language-Action models (VLAs), which involve billions of parameters. The paper relates this to CUPID, which uses returns estimated from policy rollouts to curate robot data.\n\nThe paper (arxiv.org/abs/2603.09056) focuses on data curation for robot learning using influence functions to identify and select high-quality demonstration data, which is essential for effective data-driven robot learning."
    ],
    "durationSeconds": 5.654332114999997
  },
  "sourceToolAssistantUUID": "572aa878-8fc5-485d-9254-f368a66cb22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T11:41:21.439Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015hPsD9G5W5XQ26sYNdQQ5g`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.09056",
  "prompt": "Extract the full abstract, authors, submission date, and any information about whether this is accepted at a venue. What method does QoQ use for data curation? Is it static or online/dynamic? How does it compare to influence function based methods? Does it involve reducible loss or EMA?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84dd551f-951c-43fe-a498-22ee665faa29",
  "isSidechain": false,
  "requestId": "req_011CazWJggJ1VMACHKNNHd65",
  "type": "assistant",
  "uuid": "b126a8ae-4b74-40ad-9fc0-791ce4b69e07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cgFffCyHWWxevJqEZ4jyi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 48197,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 48197,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b126a8ae-4b74-40ad-9fc0-791ce4b69e07",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool result

_source line 46 · 2026-05-13T11:41:28.310Z_

<details><summary>↩ Tool result · `toolu_015hPsD9G5W5XQ26sYNdQQ5g`</summary>

```text
# Paper Summary: Quality over Quantity

**Full Abstract:**
"Learning from demonstrations has emerged as a promising paradigm for end-to-end robot control, particularly when scaled to diverse and large datasets. However, the quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning. Human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors, making data curation essential yet largely manual and heuristic-driven. In this work, we propose Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. To efficiently estimate this contribution, we leverage influence functions, which quantify the impact of individual training samples on model performance. We further introduce two key techniques to adapt influence functions for robot demonstrations: (i) using maximum influence across validation samples to capture the most relevant state-action pairs, and (ii) aggregating influence scores of state-action pairs within the same trajectory to reduce noise and improve data coverage. Experiments in both simulated and real-world settings show that QoQ consistently improves policy performances over prior data selection methods."

**Authors:** Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, Kimin Lee

**Submission Date:** March 10, 2026

**Venue Status:** Accepted to ICRA 2026

---

## Method Details

**QoQ's Data Curation Approach:**
QoQ uses influence functions to select high-quality demonstrations. It defines quality as "the contribution of each training sample to reducing loss on validation demonstrations."

**Static vs. Dynamic:** The paper provides no indication this is an online/dynamic method—it appears to be a static curation approach applied to collected datasets.

**Comparison to Influence Function Methods:** QoQ *is* an influence function-based method. Rather than comparing against other influence function approaches, the abstract notes it improves over "prior data selection methods."

**Reducible Loss/EMA:** Neither reducible loss nor exponential moving average (EMA) mechanisms are mentioned in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b126a8ae-4b74-40ad-9fc0-791ce4b69e07",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "f4f333b6-ad38-472a-873f-de9d3f6721bb",
  "toolUseResult": {
    "bytes": 46273,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Quality over Quantity\n\n**Full Abstract:**\n\"Learning from demonstrations has emerged as a promising paradigm for end-to-end robot control, particularly when scaled to diverse and large datasets. However, the quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning. Human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors, making data curation essential yet largely manual and heuristic-driven. In this work, we propose Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. To efficiently estimate this contribution, we leverage influence functions, which quantify the impact of individual training samples on model performance. We further introduce two key techniques to adapt influence functions for robot demonstrations: (i) using maximum influence across validation samples to capture the most relevant state-action pairs, and (ii) aggregating influence scores of state-action pairs within the same trajectory to reduce noise and improve data coverage. Experiments in both simulated and real-world settings show that QoQ consistently improves policy performances over prior data selection methods.\"\n\n**Authors:** Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, Kimin Lee\n\n**Submission Date:** March 10, 2026\n\n**Venue Status:** Accepted to ICRA 2026\n\n---\n\n## Method Details\n\n**QoQ's Data Curation Approach:**\nQoQ uses influence functions to select high-quality demonstrations. It defines quality as \"the contribution of each training sample to reducing loss on validation demonstrations.\"\n\n**Static vs. Dynamic:** The paper provides no indication this is an online/dynamic method—it appears to be a static curation approach applied to collected datasets.\n\n**Comparison to Influence Function Methods:** QoQ *is* an influence function-based method. Rather than comparing against other influence function approaches, the abstract notes it improves over \"prior data selection methods.\"\n\n**Reducible Loss/EMA:** Neither reducible loss nor exponential moving average (EMA) mechanisms are mentioned in the provided content.",
    "durationMs": 6867,
    "url": "https://arxiv.org/abs/2603.09056"
  },
  "sourceToolAssistantUUID": "b126a8ae-4b74-40ad-9fc0-791ce4b69e07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T11:41:31.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RvExmc9bPyAkVcecghJiuN`</summary>

```json
{
  "query": "EMA reference model noise filtering self-distillation feedback loop limitations 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4f333b6-ad38-472a-873f-de9d3f6721bb",
  "isSidechain": false,
  "requestId": "req_011CazWKXvy7XN3oR1BRvuBk",
  "type": "assistant",
  "uuid": "c4cc44fe-5f94-4ddd-922a-c53189e9848c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gdpj8yKcWqXG7fuMvMX11n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 49091,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 49091,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 651
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T11:41:39.750Z_

<details><summary>↩ Tool result · `toolu_01RvExmc9bPyAkVcecghJiuN`</summary>

```text
Web search results for query: "EMA reference model noise filtering self-distillation feedback loop limitations 2025 2026"

Links: [{"title":"REINFORCEMENT LEARNING VIA SELF-DISTILLATION","url":"https://openreview.net/pdf?id=k8DcHShsrJ"},{"title":"Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits","url":"https://arxiv.org/html/2411.18704v1"},{"title":"Self-knowledge distillation through ensemble model averaging: a novel approach for image classification | The Visual Computer | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00371-025-04032-2"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/pdf/2601.20802"},{"title":"GitHub - lasgroup/SDPO: Reinforcement Learning via Self-Distillation (SDPO) · GitHub","url":"https://github.com/lasgroup/SDPO"},{"title":"Techniques for Training Stability (Gradient Clipping, EMA)","url":"https://apxml.com/courses/advanced-diffusion-architectures/chapter-4-advanced-diffusion-training/training-stability-techniques"},{"title":"Understanding Self-Distillation and Privileged Information Distillation","url":"https://emilianopp.github.io/Privileged-Information-Distillation-and-Self-Distillation/"},{"title":"Distributed Self-Distillation | Speechmatics","url":"https://blog.speechmatics.com/distirbuted-self-distillation"},{"title":"SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1","url":"https://arxiv.org/pdf/2601.19897"},{"title":"How to Scale Your EMA Dan Busbridge∗ Jason Ramapuram∗ Pierre Ablin∗","url":"https://arxiv.org/pdf/2307.13813"}]

I found several relevant research papers and resources about EMA (Exponential Moving Average) reference models, noise filtering, self-distillation, feedback loops, and their limitations in 2025-2026. Here's what the search results reveal:

## Key Findings:

### EMA in Self-Distillation Framework
The EMA teacher is updated via exponential moving average of the student parameters, acting as an implicit ensemble of past student models, making it more stable and less noisy than the current student. This provides richer, higher-quality targets, enabling the student to keep improving in an iterative bootstrapping loop.

### Noise Filtering Properties
The noise reduction of weight averaging improves generalization throughout training, with EMA models being very effective early in training, with remarkable performance after just a few epochs. The EMA model can achieve notable performances while keeping a large learning rate for fast progress through noise reduction from averaging.

### Key Limitations Identified

**Feedback Quality Dependency:** SDPO performance depends on the quality of environment feedback—if the environment provides uninformative or misleading feedback, a model may not be able to learn from it.

**Mode Bias Problem:** The main problem with pure self-distillation is its bias towards easier-to-fit modes, which may inherently be suboptimal.

**In-Context Learning Requirement:** SDPO performance depends on a model's in-context learning ability, suggesting that SDPO is primarily applicable for RL-training stronger base models, while it can underperform on weaker models.

**Bootstrapping Limitations:** After bootstrapping with EMA parameters, noisy SGD updates quickly take over and deteriorate model performance.

The search results indicate active 2025-2026 research examining self-distillation frameworks with EMA teachers and their effectiveness constraints in feedback-based learning scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4cc44fe-5f94-4ddd-922a-c53189e9848c",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "ab8b89f0-8011-4392-8706-806245c3f3bc",
  "toolUseResult": {
    "query": "EMA reference model noise filtering self-distillation feedback loop limitations 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013GLw6H1wgp6LcB7Q6zxqnM",
        "content": [
          {
            "title": "REINFORCEMENT LEARNING VIA SELF-DISTILLATION",
            "url": "https://openreview.net/pdf?id=k8DcHShsrJ"
          },
          {
            "title": "Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits",
            "url": "https://arxiv.org/html/2411.18704v1"
          },
          {
            "title": "Self-knowledge distillation through ensemble model averaging: a novel approach for image classification | The Visual Computer | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00371-025-04032-2"
          },
          {
            "title": "Reinforcement Learning via Self-Distillation",
            "url": "https://arxiv.org/pdf/2601.20802"
          },
          {
            "title": "GitHub - lasgroup/SDPO: Reinforcement Learning via Self-Distillation (SDPO) · GitHub",
            "url": "https://github.com/lasgroup/SDPO"
          },
          {
            "title": "Techniques for Training Stability (Gradient Clipping, EMA)",
            "url": "https://apxml.com/courses/advanced-diffusion-architectures/chapter-4-advanced-diffusion-training/training-stability-techniques"
          },
          {
            "title": "Understanding Self-Distillation and Privileged Information Distillation",
            "url": "https://emilianopp.github.io/Privileged-Information-Distillation-and-Self-Distillation/"
          },
          {
            "title": "Distributed Self-Distillation | Speechmatics",
            "url": "https://blog.speechmatics.com/distirbuted-self-distillation"
          },
          {
            "title": "SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1",
            "url": "https://arxiv.org/pdf/2601.19897"
          },
          {
            "title": "How to Scale Your EMA Dan Busbridge∗ Jason Ramapuram∗ Pierre Ablin∗",
            "url": "https://arxiv.org/pdf/2307.13813"
          }
        ]
      },
      "I found several relevant research papers and resources about EMA (Exponential Moving Average) reference models, noise filtering, self-distillation, feedback loops, and their limitations in 2025-2026. Here's what the search results reveal:\n\n## Key Findings:\n\n### EMA in Self-Distillation Framework\nThe EMA teacher is updated via exponential moving average of the student parameters, acting as an implicit ensemble of past student models, making it more stable and less noisy than the current student. This provides richer, higher-quality targets, enabling the student to keep improving in an iterative bootstrapping loop.\n\n### Noise Filtering Properties\nThe noise reduction of weight averaging improves generalization throughout training, with EMA models being very effective early in training, with remarkable performance after just a few epochs. The EMA model can achieve notable performances while keeping a large learning rate for fast progress through noise reduction from averaging.\n\n### Key Limitations Identified\n\n**Feedback Quality Dependency:** SDPO performance depends on the quality of environment feedback—if the environment provides uninformative or misleading feedback, a model may not be able to learn from it.\n\n**Mode Bias Problem:** The main problem with pure self-distillation is its bias towards easier-to-fit modes, which may inherently be suboptimal.\n\n**In-Context Learning Requirement:** SDPO performance depends on a model's in-context learning ability, suggesting that SDPO is primarily applicable for RL-training stronger base models, while it can underperform on weaker models.\n\n**Bootstrapping Limitations:** After bootstrapping with EMA parameters, noisy SGD updates quickly take over and deteriorate model performance.\n\nThe search results indicate active 2025-2026 research examining self-distillation frameworks with EMA teachers and their effectiveness constraints in feedback-based learning scenarios."
    ],
    "durationSeconds": 8.571580486999999
  },
  "sourceToolAssistantUUID": "c4cc44fe-5f94-4ddd-922a-c53189e9848c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-13T11:41:42.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BPoic3p7uWjESyAAbqM3Z3`</summary>

```json
{
  "query": "adaptive data selection curriculum learning VLA robot manipulation SFT RL pipeline 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab8b89f0-8011-4392-8706-806245c3f3bc",
  "isSidechain": false,
  "requestId": "req_011CazWLNxFMWbscFJyixnwU",
  "type": "assistant",
  "uuid": "b58572c9-a8fe-4d69-a698-182d07296857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M99ij9jPKQMJ5CsyEX7QFv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 49742,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 49742,
          "cache_creation_input_tokens": 1011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1011
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-13T11:41:51.805Z_

<details><summary>↩ Tool result · `toolu_01BPoic3p7uWjESyAAbqM3Z3`</summary>

```text
Web search results for query: "adaptive data selection curriculum learning VLA robot manipulation SFT RL pipeline 2026"

Links: [{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=xqRD4LLY5M"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518719L/abstract"},{"title":"TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation","url":"https://arxiv.org/html/2602.09023"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"Test-Time RL for VLAs","url":"https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"}]

I found several highly relevant papers on this topic from 2026 and recent months. Here are the key findings:

## VLA-RL Framework (May 2025)

VLA-RL is an algorithmic and systematic framework that leverages online reinforcement learning (RL) to improve pretrained auto-regressive VLAs in downstream tasks. A key component of this framework is an adaptive curriculum that selects tasks based on the agent's current capabilities. Implementation findings that improve stability and efficiency include curriculum selection strategy, GPU-balanced vectorized environments, batch decoding, and critic warmup.

## VLA-OPD: Bridging SFT and RL (March 2026)

VLA-OPD is a framework bridging the efficiency of SFT with the robustness of RL, leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories, enabling active error correction on policy-induced states while preserving pre-trained general capabilities through gentle alignment.

## PLD: Self-Improving VLAs with Data Generation (2026)

Probe, Learn, Distill (PLD) is a plug-and-play framework that improves VLAs through residual reinforcement learning and distribution-aware data collection, where in Stage 1 the VLA backbone is frozen and lightweight residual actors are trained via off-policy RL. RL-generated, policy-aligned data can surpass teleoperation-only demonstrations, offering a scalable path toward self-improving VLA models.

## TwinRL-VLA: Digital Twin-Driven RL (March 2026)

TwinRL constructs a high-fidelity digital twin as an exploration amplifier and guide for real-world online RL, combining exploration-space expansion warm-up that synthesizes diverse trajectories and sim-to-real guided exploration that uses parallel twin RL rollouts.

These papers collectively demonstrate the trend toward combining adaptive curriculum learning, data selection strategies, and hybrid SFT-RL pipelines for improving VLA models in robot manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b58572c9-a8fe-4d69-a698-182d07296857",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "be78ba76-ecdc-4538-98e2-aff5b15d0057",
  "toolUseResult": {
    "query": "adaptive data selection curriculum learning VLA robot manipulation SFT RL pipeline 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NUGYafxndNK8Bz985UFfmt",
        "content": [
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.18719v1"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for...",
            "url": "https://arxiv.org/abs/2603.26666"
          },
          {
            "title": "SimpleVLA-RL: Scalable VLA Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/simplevla-rl"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=xqRD4LLY5M"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250518719L/abstract"
          },
          {
            "title": "TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation",
            "url": "https://arxiv.org/html/2602.09023"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          },
          {
            "title": "Test-Time RL for VLAs",
            "url": "https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"
          }
        ]
      },
      "I found several highly relevant papers on this topic from 2026 and recent months. Here are the key findings:\n\n## VLA-RL Framework (May 2025)\n\nVLA-RL is an algorithmic and systematic framework that leverages online reinforcement learning (RL) to improve pretrained auto-regressive VLAs in downstream tasks. A key component of this framework is an adaptive curriculum that selects tasks based on the agent's current capabilities. Implementation findings that improve stability and efficiency include curriculum selection strategy, GPU-balanced vectorized environments, batch decoding, and critic warmup.\n\n## VLA-OPD: Bridging SFT and RL (March 2026)\n\nVLA-OPD is a framework bridging the efficiency of SFT with the robustness of RL, leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories, enabling active error correction on policy-induced states while preserving pre-trained general capabilities through gentle alignment.\n\n## PLD: Self-Improving VLAs with Data Generation (2026)\n\nProbe, Learn, Distill (PLD) is a plug-and-play framework that improves VLAs through residual reinforcement learning and distribution-aware data collection, where in Stage 1 the VLA backbone is frozen and lightweight residual actors are trained via off-policy RL. RL-generated, policy-aligned data can surpass teleoperation-only demonstrations, offering a scalable path toward self-improving VLA models.\n\n## TwinRL-VLA: Digital Twin-Driven RL (March 2026)\n\nTwinRL constructs a high-fidelity digital twin as an exploration amplifier and guide for real-world online RL, combining exploration-space expansion warm-up that synthesizes diverse trajectories and sim-to-real guided exploration that uses parallel twin RL rollouts.\n\nThese papers collectively demonstrate the trend toward combining adaptive curriculum learning, data selection strategies, and hybrid SFT-RL pipelines for improving VLA models in robot manipulation tasks."
    ],
    "durationSeconds": 9.1833995
  },
  "sourceToolAssistantUUID": "b58572c9-a8fe-4d69-a698-182d07296857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-13T11:41:55.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Adx5b827TC8PGj9FaYK7bC`</summary>

```json
{
  "query": "PSFT \"proximal supervised fine-tuning\" 2508.17784 PPO clipped surrogate SFT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be78ba76-ecdc-4538-98e2-aff5b15d0057",
  "isSidechain": false,
  "requestId": "req_011CazWMGSrf6VCEJqKwAWaR",
  "type": "assistant",
  "uuid": "58cb8d6e-6dd9-4602-9e09-5a289de70c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqrFa6UUxp5zYnjyyr1Z8V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1093,
      "cache_read_input_tokens": 50753,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 50753,
          "cache_creation_input_tokens": 1093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1093
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-13T11:41:59.961Z_

<details><summary>↩ Tool result · `toolu_01Adx5b827TC8PGj9FaYK7bC`</summary>

```text
Web search results for query: "PSFT "proximal supervised fine-tuning" 2508.17784 PPO clipped surrogate SFT"

Links: [{"title":"Proximal Supervised Fine-Tuning PROXIMAL SUPERVISED FINE-TUNING","url":"https://arxiv.org/pdf/2508.17784"},{"title":"[2508.17784] Proximal Supervised Fine-Tuning","url":"https://arxiv.org/abs/2508.17784"},{"title":"(PDF) Proximal Supervised Fine-Tuning","url":"https://www.researchgate.net/publication/394941431_Proximal_Supervised_Fine-Tuning"},{"title":"[Literature Review] Proximal Supervised Fine-Tuning","url":"https://www.themoonlight.io/en/review/proximal-supervised-fine-tuning"},{"title":"Proximal Supervised Fine-Tuning | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.17784v1"},{"title":"[2508.17784v1] Proximal Supervised Fine-Tuning","url":"https://arxiv.org/abs/2508.17784v1"},{"title":"Proximal SFT (PSFT)","url":"https://www.emergentmind.com/topics/proximal-sft-psft"},{"title":"Proximal Supervised Fine-Tuning (2508.17784v1)","url":"https://www.emergentmind.com/papers/2508.17784"},{"title":"Proximal Supervised Fine-Tuning | OpenReview","url":"https://openreview.net/forum?id=hQtwQqYikp"},{"title":"support Proximal Supervised Fine-Tuning · Issue #9157 · hiyouga/LlamaFactory","url":"https://github.com/hiyouga/LlamaFactory/issues/9157"}]

Based on the search results, I found comprehensive information about the paper you're looking for. Here's what the search revealed:

## Overview

The paper proposes Proximal SFT (PSFT), inspired by trust-region policy optimization (TRPO) and proximal policy optimization (PPO) in reinforcement learning (RL).

## Key Concepts

The approach introduces a novel objective based on a clipped surrogate objective that leverages the benefits of trust regions to constrain policy updates. By viewing SFT as a special case of policy gradient methods with constant positive advantages, PSFT stabilizes optimization and leads to generalization.

## Methodology

Drawing from PPO, which uses a clipped surrogate objective to prevent excessive policy updates, PSFT introduces a similar mechanism. The approach addresses the issue that supervised fine-tuning (SFT) of foundation models often leads to poor generalization, where prior capabilities deteriorate after tuning on new tasks or domains.

## Results

Experiments across mathematical, human-value, and multimodal domains show that PSFT matches standard SFT in-domain, outperforms it in out-of-domain generalization, remains stable under prolonged training without causing entropy collapse, and provides a stronger foundation for the subsequent optimization.

The paper (arXiv:2508.17784) was published in August 2025, and code is available at https://github.com/zwhong714/PSFT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58cb8d6e-6dd9-4602-9e09-5a289de70c3d",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "4bd1a604-bbe6-493c-8023-839de43f0123",
  "toolUseResult": {
    "query": "PSFT \"proximal supervised fine-tuning\" 2508.17784 PPO clipped surrogate SFT",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MYkByrxxRrdFk45xB5Sygz",
        "content": [
          {
            "title": "Proximal Supervised Fine-Tuning PROXIMAL SUPERVISED FINE-TUNING",
            "url": "https://arxiv.org/pdf/2508.17784"
          },
          {
            "title": "[2508.17784] Proximal Supervised Fine-Tuning",
            "url": "https://arxiv.org/abs/2508.17784"
          },
          {
            "title": "(PDF) Proximal Supervised Fine-Tuning",
            "url": "https://www.researchgate.net/publication/394941431_Proximal_Supervised_Fine-Tuning"
          },
          {
            "title": "[Literature Review] Proximal Supervised Fine-Tuning",
            "url": "https://www.themoonlight.io/en/review/proximal-supervised-fine-tuning"
          },
          {
            "title": "Proximal Supervised Fine-Tuning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2508.17784v1"
          },
          {
            "title": "[2508.17784v1] Proximal Supervised Fine-Tuning",
            "url": "https://arxiv.org/abs/2508.17784v1"
          },
          {
            "title": "Proximal SFT (PSFT)",
            "url": "https://www.emergentmind.com/topics/proximal-sft-psft"
          },
          {
            "title": "Proximal Supervised Fine-Tuning (2508.17784v1)",
            "url": "https://www.emergentmind.com/papers/2508.17784"
          },
          {
            "title": "Proximal Supervised Fine-Tuning | OpenReview",
            "url": "https://openreview.net/forum?id=hQtwQqYikp"
          },
          {
            "title": "support Proximal Supervised Fine-Tuning · Issue #9157 · hiyouga/LlamaFactory",
            "url": "https://github.com/hiyouga/LlamaFactory/issues/9157"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for. Here's what the search revealed:\n\n## Overview\n\nThe paper proposes Proximal SFT (PSFT), inspired by trust-region policy optimization (TRPO) and proximal policy optimization (PPO) in reinforcement learning (RL).\n\n## Key Concepts\n\nThe approach introduces a novel objective based on a clipped surrogate objective that leverages the benefits of trust regions to constrain policy updates. By viewing SFT as a special case of policy gradient methods with constant positive advantages, PSFT stabilizes optimization and leads to generalization.\n\n## Methodology\n\nDrawing from PPO, which uses a clipped surrogate objective to prevent excessive policy updates, PSFT introduces a similar mechanism. The approach addresses the issue that supervised fine-tuning (SFT) of foundation models often leads to poor generalization, where prior capabilities deteriorate after tuning on new tasks or domains.\n\n## Results\n\nExperiments across mathematical, human-value, and multimodal domains show that PSFT matches standard SFT in-domain, outperforms it in out-of-domain generalization, remains stable under prolonged training without causing entropy collapse, and provides a stronger foundation for the subsequent optimization.\n\nThe paper (arXiv:2508.17784) was published in August 2025, and code is available at https://github.com/zwhong714/PSFT."
    ],
    "durationSeconds": 4.858409834999999
  },
  "sourceToolAssistantUUID": "58cb8d6e-6dd9-4602-9e09-5a289de70c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-13T11:42:02.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019gEodf1cp1MevvFkDkRVLJ`</summary>

```json
{
  "query": "experience replay data scoring action filtering VLA vision language action model training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bd1a604-bbe6-493c-8023-839de43f0123",
  "isSidechain": false,
  "requestId": "req_011CazWMsEdHyn9MjTyxzVgc",
  "type": "assistant",
  "uuid": "9f09552b-4f6e-4527-a763-d440fd577d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StRA2Q3YvXDtqpfRGYp9n1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 51846,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 51846,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 904
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9f09552b-4f6e-4527-a763-d440fd577d22",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool result

_source line 56 · 2026-05-13T11:42:11.166Z_

<details><summary>↩ Tool result · `toolu_019gEodf1cp1MevvFkDkRVLJ`</summary>

```text
Web search results for query: "experience replay data scoring action filtering VLA vision language action model training 2025 2026"

Links: [{"title":"[2511.06202] ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/abs/2511.06202"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/html/2603.03818"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/html/2509.15937v1"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"}]

Based on the web search results, I found several highly relevant papers and research on experience replay, data scoring, action filtering, and VLA (Vision-Language-Action) model training from 2025-2026:

## Key Research Findings:

### ExpReS-VLA: Experience Replay for VLA Specialization
ExpReS-VLA is a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. The approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs, and retrieves the k most similar past experiences using cosine similarity to augment training batches while a prioritized experience replay buffer preserves recently successful trajectories.

### VLA Continual Learning with Experience Replay
Recent research investigates how large-scale pretraining in VLAs interacts with experience replay across different replay sizes, revealing that large-scale pretraining is a key factor affecting both forward and backward transfer behavior, and specifically reduces forgetting especially in low-data regimes while preserving knowledge of past tasks.

### Action Scoring and Filtering Approaches
Research on VLAC (Vision-Language-Action-Critic) addresses the bottleneck of sparse, handcrafted rewards in robotic RL by introducing a general process reward model that outputs dense progress delta and done signal, eliminating task-specific reward engineering.

### Chain-of-Thought VLA Training
CoT-VLA frameworks can leverage action-less datasets like EPIC-KITCHEN-100 to enhance subgoal image generation ability, unlocking the potential of using abundant unlabeled video data to improve VLA's visual reasoning capability.

These represent cutting-edge approaches in 2025-2026 for improving VLA training efficiency through experience replay mechanisms, data quality scoring, and action-aware filtering strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f09552b-4f6e-4527-a763-d440fd577d22",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "fbc01d9e-30f4-4eb8-b5c4-a1ebebb5020d",
  "toolUseResult": {
    "query": "experience replay data scoring action filtering VLA vision language action model training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ty1eECYevxAQjoJbHVmB4x",
        "content": [
          {
            "title": "[2511.06202] ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval",
            "url": "https://arxiv.org/abs/2511.06202"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/html/2603.03818"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2406.09246"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "2025-9-18 ThinkAct: Vision-Language-Action Reasoning via",
            "url": "https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"
          },
          {
            "title": "A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.15937v1"
          },
          {
            "title": "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers and research on experience replay, data scoring, action filtering, and VLA (Vision-Language-Action) model training from 2025-2026:\n\n## Key Research Findings:\n\n### ExpReS-VLA: Experience Replay for VLA Specialization\nExpReS-VLA is a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. The approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs, and retrieves the k most similar past experiences using cosine similarity to augment training batches while a prioritized experience replay buffer preserves recently successful trajectories.\n\n### VLA Continual Learning with Experience Replay\nRecent research investigates how large-scale pretraining in VLAs interacts with experience replay across different replay sizes, revealing that large-scale pretraining is a key factor affecting both forward and backward transfer behavior, and specifically reduces forgetting especially in low-data regimes while preserving knowledge of past tasks.\n\n### Action Scoring and Filtering Approaches\nResearch on VLAC (Vision-Language-Action-Critic) addresses the bottleneck of sparse, handcrafted rewards in robotic RL by introducing a general process reward model that outputs dense progress delta and done signal, eliminating task-specific reward engineering.\n\n### Chain-of-Thought VLA Training\nCoT-VLA frameworks can leverage action-less datasets like EPIC-KITCHEN-100 to enhance subgoal image generation ability, unlocking the potential of using abundant unlabeled video data to improve VLA's visual reasoning capability.\n\nThese represent cutting-edge approaches in 2025-2026 for improving VLA training efficiency through experience replay mechanisms, data quality scoring, and action-aware filtering strategies."
    ],
    "durationSeconds": 8.343887134000019
  },
  "sourceToolAssistantUUID": "9f09552b-4f6e-4527-a763-d440fd577d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 57 · 2026-05-13T11:42:11.169Z_

```json
{
  "parentUuid": "fbc01d9e-30f4-4eb8-b5c4-a1ebebb5020d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "22d23cd8-ffa6-4023-92a3-c87b1a0db305",
  "timestamp": "2026-05-13T11:42:11.169Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 58 · 2026-05-13T11:42:14.596Z_

Important find — ExpReS-VLA uses prioritized experience replay for VLA training. Let me investigate this and continue searching for other missing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22d23cd8-ffa6-4023-92a3-c87b1a0db305",
  "isSidechain": false,
  "requestId": "req_011CazWNh9w4MjG1NBRMdXMc",
  "type": "assistant",
  "uuid": "2c3b663e-0d38-4003-aafc-4c3cc8e79ca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APejVt3ETM685SNhZP6Ky5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 52750,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 52750,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-13T11:42:16.841Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RhVXHsSW6xBujPp7tr26ff`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.06202",
  "prompt": "Extract the full abstract, authors, submission date, and venue/status. Does ExpReS-VLA use prioritized experience replay? Is it related to SFT data quality or noise filtering? Does it use reducible loss or any form of data quality scoring during training? What exactly is the experience replay mechanism?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3b663e-0d38-4003-aafc-4c3cc8e79ca5",
  "isSidechain": false,
  "requestId": "req_011CazWNh9w4MjG1NBRMdXMc",
  "type": "assistant",
  "uuid": "2915589a-e444-4bba-8d7a-2dcc732f9ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APejVt3ETM685SNhZP6Ky5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 52750,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 52750,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-13T11:42:23.675Z_

<details><summary>↩ Tool result · `toolu_01RhVXHsSW6xBujPp7tr26ff`</summary>

```text
# ExpReS-VLA Analysis

## Metadata

**Authors:** Shahram Najam Syed, Yatharth Ahuja, Arthur Jakobsson, Jeff Ichnowski

**Submission Date:** November 9, 2025 (v1); March 6, 2026 (v2)

**Venue/Status:** Accepted to International Conference on Robotics and Automation (ICRA) 2026

## Full Abstract

"Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the k most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations."

## Key Findings

**Prioritized Experience Replay:** Yes—the method uses "a prioritized experience replay buffer [that] preserves recently successful trajectories."

**SFT Data Quality/Noise Filtering:** Not directly related. The work focuses on task-specific adaptation rather than foundational model pre-training quality.

**Data Quality Scoring Mechanism:** The Thresholded Hybrid Contrastive Loss (THCL) distinguishes between successful and unsuccessful demonstrations but doesn't employ reducible loss or explicit quality scoring metrics.

**Experience Replay Mechanism:** Stores compressed embeddings (97% reduction), retrieves k-nearest neighbors via cosine similarity for batch augmentation, and prioritizes recent successful trajectories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2915589a-e444-4bba-8d7a-2dcc732f9ffc",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "4b49b538-90b1-470e-b6ca-ecbd8495d093",
  "toolUseResult": {
    "bytes": 48508,
    "code": 200,
    "codeText": "OK",
    "result": "# ExpReS-VLA Analysis\n\n## Metadata\n\n**Authors:** Shahram Najam Syed, Yatharth Ahuja, Arthur Jakobsson, Jeff Ichnowski\n\n**Submission Date:** November 9, 2025 (v1); March 6, 2026 (v2)\n\n**Venue/Status:** Accepted to International Conference on Robotics and Automation (ICRA) 2026\n\n## Full Abstract\n\n\"Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the k most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations.\"\n\n## Key Findings\n\n**Prioritized Experience Replay:** Yes—the method uses \"a prioritized experience replay buffer [that] preserves recently successful trajectories.\"\n\n**SFT Data Quality/Noise Filtering:** Not directly related. The work focuses on task-specific adaptation rather than foundational model pre-training quality.\n\n**Data Quality Scoring Mechanism:** The Thresholded Hybrid Contrastive Loss (THCL) distinguishes between successful and unsuccessful demonstrations but doesn't employ reducible loss or explicit quality scoring metrics.\n\n**Experience Replay Mechanism:** Stores compressed embeddings (97% reduction), retrieves k-nearest neighbors via cosine similarity for batch augmentation, and prioritizes recent successful trajectories.",
    "durationMs": 6830,
    "url": "https://arxiv.org/abs/2511.06202"
  },
  "sourceToolAssistantUUID": "2915589a-e444-4bba-8d7a-2dcc732f9ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-13T11:42:28.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A8wfbn3HG9t58tg7ERJcjq`</summary>

```json
{
  "query": "LIBERO-Plus robustness analysis VLA CVPR 2026 OpenVLA-OFT fragility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b49b538-90b1-470e-b6ca-ecbd8495d093",
  "isSidechain": false,
  "requestId": "req_011CazWPcf5pe9fSSZVSRKwb",
  "type": "assistant",
  "uuid": "798ab7bd-bf1f-40ef-9dcf-6a55ef69b28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oZ87XCkxmBjoKVN2UkqTH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 53901,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 53901,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-13T11:42:36.484Z_

<details><summary>↩ Tool result · `toolu_01A8wfbn3HG9t58tg7ERJcjq`</summary>

```text
Web search results for query: "LIBERO-Plus robustness analysis VLA CVPR 2026 OpenVLA-OFT fragility"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"}]

I found comprehensive information about LIBERO-Plus, a robustness analysis study of Vision-Language-Action (VLA) models. Here are the key findings:

## Overview

LIBERO-Plus reveals that across all perturbation factors, current VLAs exhibit brittle generalization, with performance degrading significantly under various input perturbations, particularly with changes in camera viewpoint and robot initial state.

## Key Fragility Findings

The analysis exposes critical weaknesses, with models exhibiting extreme sensitivity to perturbation factors including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## Findings on OpenVLA-OFT

Surprisingly, even without any valid language input, OpenVLA-OFT's performance on the object suite remained largely unchanged, with significant degradation observed only on the long suite. This is attributed to greater reliance on instruction guidance in long-horizon tasks, revealing that although the model is nominally designed as a Vision-Language-Action framework, in practice it degenerates into a form that disregards language, behaving more like a Vision-Action model.

## Language Insensitivity

Language perturbations result in the second smallest average performance drop (-25.3) across most models, which is counter-intuitive and merits deeper investigation.

## The LIBERO-Plus Benchmark

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities, with benchmark construction following a systematic two-stage process of expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "798ab7bd-bf1f-40ef-9dcf-6a55ef69b28d",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "24b02e99-6a5d-4b64-8467-0172d666074d",
  "toolUseResult": {
    "query": "LIBERO-Plus robustness analysis VLA CVPR 2026 OpenVLA-OFT fragility",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E8YECkWb9o5E7PJK43CcGq",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=6mEfYoMRpF"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"
          }
        ]
      },
      "I found comprehensive information about LIBERO-Plus, a robustness analysis study of Vision-Language-Action (VLA) models. Here are the key findings:\n\n## Overview\n\nLIBERO-Plus reveals that across all perturbation factors, current VLAs exhibit brittle generalization, with performance degrading significantly under various input perturbations, particularly with changes in camera viewpoint and robot initial state.\n\n## Key Fragility Findings\n\nThe analysis exposes critical weaknesses, with models exhibiting extreme sensitivity to perturbation factors including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n## Findings on OpenVLA-OFT\n\nSurprisingly, even without any valid language input, OpenVLA-OFT's performance on the object suite remained largely unchanged, with significant degradation observed only on the long suite. This is attributed to greater reliance on instruction guidance in long-horizon tasks, revealing that although the model is nominally designed as a Vision-Language-Action framework, in practice it degenerates into a form that disregards language, behaving more like a Vision-Action model.\n\n## Language Insensitivity\n\nLanguage perturbations result in the second smallest average performance drop (-25.3) across most models, which is counter-intuitive and merits deeper investigation.\n\n## The LIBERO-Plus Benchmark\n\nLIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities, with benchmark construction following a systematic two-stage process of expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing."
    ],
    "durationSeconds": 7.654236249999987
  },
  "sourceToolAssistantUUID": "798ab7bd-bf1f-40ef-9dcf-6a55ef69b28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-13T11:42:41.478Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PFvVvZUPSLSRBWRELqVxRs`</summary>

```json
{
  "query": "iw-SFT continuous control D4RL EMA update trajectory importance weights implementation details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24b02e99-6a5d-4b64-8467-0172d666074d",
  "isSidechain": false,
  "requestId": "req_011CazWQZQQjPJPSuJAreQWf",
  "type": "assistant",
  "uuid": "67dc383a-743a-4761-b61a-3376098bb355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D1yqhypxzndDPN2t7wL8j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 54593,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 54593,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1037
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T11:42:49.637Z_

<details><summary>↩ Tool result · `toolu_01PFvVvZUPSLSRBWRELqVxRs`</summary>

```text
Web search results for query: "iw-SFT continuous control D4RL EMA update trajectory importance weights implementation details"

Links: [{"title":"Importance-Weighted SFT (iw-SFT)","url":"https://www.emergentmind.com/topics/importance-weighted-sft-iw-sft"},{"title":"Sequence-level iw-SFT for Fine-Tuning","url":"https://www.emergentmind.com/topics/sequence-level-iw-sft"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/html/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://arxiv.org/pdf/2507.12856"},{"title":"Muninn: Your Trajectory Diffusion Model But Faster","url":"https://arxiv.org/html/2605.09999"},{"title":"Latent Weight Diffusion: Generating policies from trajectories","url":"https://arxiv.org/html/2410.14040v1"},{"title":"1 Decoupled Prioritized Resampling for Offline RL","url":"https://arxiv.org/pdf/2306.05412"},{"title":"Fusian: Multi-LoRA Fusion for Fine-Grained Continuous MBTI Personality Control in Large Language Models","url":"https://arxiv.org/html/2603.15405"},{"title":"Boosting Continuous Control with Consistency Policy | Yuhui Chen - 陈宇辉","url":"https://cccedric.github.io/cpql/"},{"title":"Diffusion Model Predictive Control","url":"https://arxiv.org/html/2410.05364v2"}]

Based on the search results, I found relevant information about iw-SFT (Importance-Weighted Supervised Fine-Tuning) with continuous control on D4RL benchmarks. Here's what I found:

## iw-SFT Overview

The central insight underpinning iw-SFT is that standard SFT, when performed on curated demonstration data, can be viewed as maximizing a lower bound on the expected RL return in a sparse reward regime.

## Continuous Control on D4RL

In continuous control (D4RL), SFT(Q) on top-10% trajectories already outperforms BC and matches RL methods such as AWAC, TD3+BC, CQL, and IQL; iw-SFT(Q) further improves (e.g., Walker2D Medium-Replay: 66→75).

## Trajectory Importance Weights Implementation

For D4RL experiments, they use a batch size of 256 where each element consists of a full trajectory, thus enabling normalized importance weights to be computed on the fly.

## Importance Reweighting Scheme

An adaptive (importance) reweighting scheme (iw-SFT) can be introduced that asymptotically maximizes the RL objective as the bound tightens over the course of training, and this simple change from SFT to iw-SFT not only theoretically narrows the gap between SFT and RL but also practically can achieve better results in the same settings that SFT excels in.

The search results reference the paper by Qin et al. (2025) which provides implementation details for iw-SFT on D4RL continuous control tasks. For more specific implementation details about EMA updates and trajectory importance weight computation, you may want to refer to the original arxiv paper: https://arxiv.org/html/2507.12856 or https://arxiv.org/pdf/2507.12856


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67dc383a-743a-4761-b61a-3376098bb355",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "39991eac-7389-40ec-9e91-6472b2c4ca8d",
  "toolUseResult": {
    "query": "iw-SFT continuous control D4RL EMA update trajectory importance weights implementation details",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RcNB3RrsNz6gH6ejsq31S1",
        "content": [
          {
            "title": "Importance-Weighted SFT (iw-SFT)",
            "url": "https://www.emergentmind.com/topics/importance-weighted-sft-iw-sft"
          },
          {
            "title": "Sequence-level iw-SFT for Fine-Tuning",
            "url": "https://www.emergentmind.com/topics/sequence-level-iw-sft"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://arxiv.org/html/2507.12856"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement ...",
            "url": "https://arxiv.org/pdf/2507.12856"
          },
          {
            "title": "Muninn: Your Trajectory Diffusion Model But Faster",
            "url": "https://arxiv.org/html/2605.09999"
          },
          {
            "title": "Latent Weight Diffusion: Generating policies from trajectories",
            "url": "https://arxiv.org/html/2410.14040v1"
          },
          {
            "title": "1 Decoupled Prioritized Resampling for Offline RL",
            "url": "https://arxiv.org/pdf/2306.05412"
          },
          {
            "title": "Fusian: Multi-LoRA Fusion for Fine-Grained Continuous MBTI Personality Control in Large Language Models",
            "url": "https://arxiv.org/html/2603.15405"
          },
          {
            "title": "Boosting Continuous Control with Consistency Policy | Yuhui Chen - 陈宇辉",
            "url": "https://cccedric.github.io/cpql/"
          },
          {
            "title": "Diffusion Model Predictive Control",
            "url": "https://arxiv.org/html/2410.05364v2"
          }
        ]
      },
      "Based on the search results, I found relevant information about iw-SFT (Importance-Weighted Supervised Fine-Tuning) with continuous control on D4RL benchmarks. Here's what I found:\n\n## iw-SFT Overview\n\nThe central insight underpinning iw-SFT is that standard SFT, when performed on curated demonstration data, can be viewed as maximizing a lower bound on the expected RL return in a sparse reward regime.\n\n## Continuous Control on D4RL\n\nIn continuous control (D4RL), SFT(Q) on top-10% trajectories already outperforms BC and matches RL methods such as AWAC, TD3+BC, CQL, and IQL; iw-SFT(Q) further improves (e.g., Walker2D Medium-Replay: 66→75).\n\n## Trajectory Importance Weights Implementation\n\nFor D4RL experiments, they use a batch size of 256 where each element consists of a full trajectory, thus enabling normalized importance weights to be computed on the fly.\n\n## Importance Reweighting Scheme\n\nAn adaptive (importance) reweighting scheme (iw-SFT) can be introduced that asymptotically maximizes the RL objective as the bound tightens over the course of training, and this simple change from SFT to iw-SFT not only theoretically narrows the gap between SFT and RL but also practically can achieve better results in the same settings that SFT excels in.\n\nThe search results reference the paper by Qin et al. (2025) which provides implementation details for iw-SFT on D4RL continuous control tasks. For more specific implementation details about EMA updates and trajectory importance weight computation, you may want to refer to the original arxiv paper: https://arxiv.org/html/2507.12856 or https://arxiv.org/pdf/2507.12856"
    ],
    "durationSeconds": 8.153636436000001
  },
  "sourceToolAssistantUUID": "67dc383a-743a-4761-b61a-3376098bb355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "39991eac-7389-40ec-9e91-6472b2c4ca8d",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool call

_source line 67 · 2026-05-13T11:42:55.307Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P97UtyT39zDmfQax5LnZrK`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.12856",
  "prompt": "I need to understand the exact mechanism of iw-SFT in continuous control: 1) Does it use an EMA model (exponential moving average of model parameters)? 2) What exactly does the EMA compute - trajectory-level importance weights or something else? 3) How is the EMA reference used - for loss reweighting (multiplicative) or for computing reducible loss? 4) Is there any noise-filtering or data prioritization mechanism? 5) What is the exact equation for the importance weights? Focus on Sections 3-4 and any D4RL implementation details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39991eac-7389-40ec-9e91-6472b2c4ca8d",
  "isSidechain": false,
  "requestId": "req_011CazWRXgVrCthVimE4i3F5",
  "type": "assistant",
  "uuid": "a9efa092-f12b-4c3f-963a-d26b956e2f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HW6tWVH4QGY2w5DcbQ3S5J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 55630,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 991,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 55630,
          "cache_creation_input_tokens": 991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 991
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-13T11:43:01.196Z_

<details><summary>↩ Tool result · `toolu_01P97UtyT39zDmfQax5LnZrK`</summary>

```text
# iw-SFT Mechanism in Continuous Control

## 1. EMA Model Usage
Yes, iw-SFT uses exponential moving average. The paper states: "instead of updating the importance weighting distribution q at discrete time-points we use exponential weight averaging θq=αθq+(1−α)θ during each step."

## 2. EMA Computation
The EMA computes a lagged version of model parameters that represents the reference distribution q(τ). This isn't trajectory-specific; rather, it maintains a running average of the policy parameters to define importance weights.

## 3. Reference Application
The EMA reference operates multiplicatively through reweighting. The method calculates: "wj←exp(∑ig(ρij))" where importance weight ratios ρ are derived from log-probability differences between the EMA policy and reference policy, then applies these weights directly to the loss.

## 4. Noise-Filtering Mechanisms
The approach includes data prioritization through quality binning. Algorithm 2 shows datasets are curated by "percentile cutoffs=[90, 95, 98]," creating overlapping quality bins that effectively filter and prioritize higher-quality trajectories before training begins.

## 5. Exact Importance Weight Equation
The trajectory-level importance weight follows: "exp(∑ig(ρij))" where ρij represents per-token log-probability differences. The smoothing function g(x)=kx provides control over weight scaling, preventing extreme variance in importance weighting during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9efa092-f12b-4c3f-963a-d26b956e2f71",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "5b946b29-588d-4e12-9ef0-f08c3e78cb36",
  "toolUseResult": {
    "bytes": 296212,
    "code": 200,
    "codeText": "OK",
    "result": "# iw-SFT Mechanism in Continuous Control\n\n## 1. EMA Model Usage\nYes, iw-SFT uses exponential moving average. The paper states: \"instead of updating the importance weighting distribution q at discrete time-points we use exponential weight averaging θq=αθq+(1−α)θ during each step.\"\n\n## 2. EMA Computation\nThe EMA computes a lagged version of model parameters that represents the reference distribution q(τ). This isn't trajectory-specific; rather, it maintains a running average of the policy parameters to define importance weights.\n\n## 3. Reference Application\nThe EMA reference operates multiplicatively through reweighting. The method calculates: \"wj←exp(∑ig(ρij))\" where importance weight ratios ρ are derived from log-probability differences between the EMA policy and reference policy, then applies these weights directly to the loss.\n\n## 4. Noise-Filtering Mechanisms\nThe approach includes data prioritization through quality binning. Algorithm 2 shows datasets are curated by \"percentile cutoffs=[90, 95, 98],\" creating overlapping quality bins that effectively filter and prioritize higher-quality trajectories before training begins.\n\n## 5. Exact Importance Weight Equation\nThe trajectory-level importance weight follows: \"exp(∑ig(ρij))\" where ρij represents per-token log-probability differences. The smoothing function g(x)=kx provides control over weight scaling, preventing extreme variance in importance weighting during training.",
    "durationMs": 5885,
    "url": "https://arxiv.org/html/2507.12856"
  },
  "sourceToolAssistantUUID": "a9efa092-f12b-4c3f-963a-d26b956e2f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-13T11:43:11.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PAn6HUbLn9XGLATJMXTfky`</summary>

```json
{
  "query": "ReLo reducible loss reinforcement learning target network Polyak averaging EMA periodic hard copy NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b946b29-588d-4e12-9ef0-f08c3e78cb36",
  "isSidechain": false,
  "requestId": "req_011CazWSP9KcPdssfW7K5mSB",
  "type": "assistant",
  "uuid": "fd0921f4-2e76-4033-ab64-3ce8f56f6df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3yH9b4Ag6QeUUy1oVdVkp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 56621,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 571,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 56621,
          "cache_creation_input_tokens": 571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 571
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-13T11:43:16.790Z_

<details><summary>↩ Tool result · `toolu_01PAn6HUbLn9XGLATJMXTfky`</summary>

```text
Web search results for query: "ReLo reducible loss reinforcement learning target network Polyak averaging EMA periodic hard copy NeurIPS 2023"

Links: [{"title":"ReLo: Reducible Loss for RL","url":"https://shivakanthsujit.github.io/reducible-loss/"},{"title":"Basic TRFL Usage: Target Network Updating | by AurelianTactics | aureliantactics | Medium","url":"https://medium.com/aureliantactics/basic-trfl-usage-target-network-updating-3660d77a08fd"},{"title":"Deep Deterministic Policy Gradient — Spinning Up documentation","url":"https://spinningup.openai.com/en/latest/algorithms/ddpg.html"},{"title":"Learning the Target Network in Function Space","url":"https://arxiv.org/html/2406.01838v2"},{"title":"Target Networks for Training Stability","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-2-deep-q-networks/target-networks"},{"title":"GitHub - NotNANtoN/Deep-RL-Torch: Modular Deep Reinforcement Learning libary based on PyTorch","url":"https://github.com/NotNANtoN/Deep-RL-Torch"},{"title":"Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/48726631f87322012c6be38e00c72a47-Paper-Conference.pdf"},{"title":"Marin Vlastelica","url":"https://jimimvp.github.io/rl-roundup"},{"title":"(PDF) Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://www.researchgate.net/publication/362859466_Prioritizing_Samples_in_Reinforcement_Learning_with_Reducible_Loss"},{"title":"[Quick Review] Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://liner.com/review/prioritizing-samples-in-reinforcement-learning-with-reducible-loss"}]

Based on the search results, I found relevant information about ReLo and its relation to target network updating mechanisms:

## ReLo: Reducible Loss in Reinforcement Learning

ReLo is a novel prioritization scheme that quantifies sample learn-ability, presented as a NeurIPS 2022 paper. (Note: The search results indicate NeurIPS 2022, though you mentioned NeurIPS 2023 in your query.)

### Core Concept

Instead of prioritization based on the TD error, ReLo proposes that the agent should focus on samples that have higher reducible TD error, using a measure of how much the TD error can be potentially decreased.

### Target Network Compatibility

An important finding from the research is that ReLo is robust to the target network update mechanism, whether it is a hard copy of online parameters at a fixed frequency (as in DQN and Rainbow) or if the target network is an exponential moving average of the online parameters (as in Soft Actor Critic). This means ReLo works effectively with both:
- **Periodic hard copy**: Hard frequency-based updates where the entire target network is replaced
- **Polyak averaging/EMA**: Soft exponential moving average updates where the target network changes gradually

### Computational Efficiency

ReLo is computationally efficient, requiring only one additional forward pass through the target network, making it easily integrable into existing off-policy Q-learning algorithms without significant overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd0921f4-2e76-4033-ab64-3ce8f56f6df1",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "0ccc86d6-d7fa-47a0-8e20-c415820fb17e",
  "toolUseResult": {
    "query": "ReLo reducible loss reinforcement learning target network Polyak averaging EMA periodic hard copy NeurIPS 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KjMhaNdZqm1FRprEwjYzgn",
        "content": [
          {
            "title": "ReLo: Reducible Loss for RL",
            "url": "https://shivakanthsujit.github.io/reducible-loss/"
          },
          {
            "title": "Basic TRFL Usage: Target Network Updating | by AurelianTactics | aureliantactics | Medium",
            "url": "https://medium.com/aureliantactics/basic-trfl-usage-target-network-updating-3660d77a08fd"
          },
          {
            "title": "Deep Deterministic Policy Gradient — Spinning Up documentation",
            "url": "https://spinningup.openai.com/en/latest/algorithms/ddpg.html"
          },
          {
            "title": "Learning the Target Network in Function Space",
            "url": "https://arxiv.org/html/2406.01838v2"
          },
          {
            "title": "Target Networks for Training Stability",
            "url": "https://apxml.com/courses/advanced-reinforcement-learning/chapter-2-deep-q-networks/target-networks"
          },
          {
            "title": "GitHub - NotNANtoN/Deep-RL-Torch: Modular Deep Reinforcement Learning libary based on PyTorch",
            "url": "https://github.com/NotNANtoN/Deep-RL-Torch"
          },
          {
            "title": "Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/48726631f87322012c6be38e00c72a47-Paper-Conference.pdf"
          },
          {
            "title": "Marin Vlastelica",
            "url": "https://jimimvp.github.io/rl-roundup"
          },
          {
            "title": "(PDF) Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://www.researchgate.net/publication/362859466_Prioritizing_Samples_in_Reinforcement_Learning_with_Reducible_Loss"
          },
          {
            "title": "[Quick Review] Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://liner.com/review/prioritizing-samples-in-reinforcement-learning-with-reducible-loss"
          }
        ]
      },
      "Based on the search results, I found relevant information about ReLo and its relation to target network updating mechanisms:\n\n## ReLo: Reducible Loss in Reinforcement Learning\n\nReLo is a novel prioritization scheme that quantifies sample learn-ability, presented as a NeurIPS 2022 paper. (Note: The search results indicate NeurIPS 2022, though you mentioned NeurIPS 2023 in your query.)\n\n### Core Concept\n\nInstead of prioritization based on the TD error, ReLo proposes that the agent should focus on samples that have higher reducible TD error, using a measure of how much the TD error can be potentially decreased.\n\n### Target Network Compatibility\n\nAn important finding from the research is that ReLo is robust to the target network update mechanism, whether it is a hard copy of online parameters at a fixed frequency (as in DQN and Rainbow) or if the target network is an exponential moving average of the online parameters (as in Soft Actor Critic). This means ReLo works effectively with both:\n- **Periodic hard copy**: Hard frequency-based updates where the entire target network is replaced\n- **Polyak averaging/EMA**: Soft exponential moving average updates where the target network changes gradually\n\n### Computational Efficiency\n\nReLo is computationally efficient, requiring only one additional forward pass through the target network, making it easily integrable into existing off-policy Q-learning algorithms without significant overhead."
    ],
    "durationSeconds": 5.726335531999998
  },
  "sourceToolAssistantUUID": "fd0921f4-2e76-4033-ab64-3ce8f56f6df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-13T11:43:20.609Z_

This is a critical finding — ReLo works with BOTH periodic hard copy AND EMA (Polyak averaging). The proposal correctly identified this in Round 6. Let me now fetch the actual ReLo paper to verify details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ccc86d6-d7fa-47a0-8e20-c415820fb17e",
  "isSidechain": false,
  "requestId": "req_011CazWTXkXS6Bhw59uzGZ6D",
  "type": "assistant",
  "uuid": "ea7ae1ee-dacd-4217-8f18-cc4ed3bf4954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJ2G6PXydSqo9eCFQP3oHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 57192,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 57192,
          "cache_creation_input_tokens": 958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 958
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-13T11:43:22.461Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VK8RdWpzhWNV2nT9Ycz7Tm`</summary>

```json
{
  "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/48726631f87322012c6be38e00c72a47-Paper-Conference.pdf",
  "prompt": "Extract key details: 1) Does ReLo use Polyak averaging (EMA) or periodic hard copy for its target network? 2) Is the target network an EMA of the online network? 3) What is the exact formula for reducible loss? 4) What environments does ReLo work on? 5) Does ReLo address supervised learning or just RL?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea7ae1ee-dacd-4217-8f18-cc4ed3bf4954",
  "isSidechain": false,
  "requestId": "req_011CazWTXkXS6Bhw59uzGZ6D",
  "type": "assistant",
  "uuid": "1a0029d9-b46f-465a-833e-6621876444e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJ2G6PXydSqo9eCFQP3oHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 57192,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 57192,
          "cache_creation_input_tokens": 958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 958
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-13T11:43:28.699Z_

<details><summary>↩ Tool result · `toolu_01VK8RdWpzhWNV2nT9Ycz7Tm`</summary>

```text
I appreciate your request, but I need to be direct: the content provided appears to be a PDF file encoded in binary format (PDF stream objects with compression), not readable text. The raw PDF structure shows font definitions, page objects, and compressed content streams that cannot be meaningfully interpreted without proper PDF parsing.

To answer your specific questions about ReLo's methodology, I would need:
- A text-extracted version of the document
- The actual paper content in readable format
- Or a direct link to the paper

**From what I can observe about the document structure:**
The PDF contains 1228+ objects with embedded fonts and compressed streams, suggesting it's a technical paper, but the actual content discussing ReLo's target network approach, loss formulas, and experimental setup is not accessible in the format provided.

**To proceed, I can:**
1. Accept a plain-text version of the relevant sections
2. Work from a proper document excerpt
3. Help you extract and convert the PDF to readable text first

Would you like to provide the content in a more accessible format?

[Binary content (application/pdf, 1.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/c910c13d-bae5-469c-bad4-44d932f7b20c/tool-results/webfetch-1778672603913-jwbb2u.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a0029d9-b46f-465a-833e-6621876444e6",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "88eb6b8d-27a0-4bf5-8a5d-414431d6a408",
  "toolUseResult": {
    "bytes": 1415774,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to be direct: the content provided appears to be a PDF file encoded in binary format (PDF stream objects with compression), not readable text. The raw PDF structure shows font definitions, page objects, and compressed content streams that cannot be meaningfully interpreted without proper PDF parsing.\n\nTo answer your specific questions about ReLo's methodology, I would need:\n- A text-extracted version of the document\n- The actual paper content in readable format\n- Or a direct link to the paper\n\n**From what I can observe about the document structure:**\nThe PDF contains 1228+ objects with embedded fonts and compressed streams, suggesting it's a technical paper, but the actual content discussing ReLo's target network approach, loss formulas, and experimental setup is not accessible in the format provided.\n\n**To proceed, I can:**\n1. Accept a plain-text version of the relevant sections\n2. Work from a proper document excerpt\n3. Help you extract and convert the PDF to readable text first\n\nWould you like to provide the content in a more accessible format?\n\n[Binary content (application/pdf, 1.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/c910c13d-bae5-469c-bad4-44d932f7b20c/tool-results/webfetch-1778672603913-jwbb2u.pdf]",
    "durationMs": 6231,
    "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/48726631f87322012c6be38e00c72a47-Paper-Conference.pdf"
  },
  "sourceToolAssistantUUID": "1a0029d9-b46f-465a-833e-6621876444e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-13T11:43:32.985Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012ZEqZWxtbunnXL4DLuuzFA`</summary>

```json
{
  "url": "https://shivakanthsujit.github.io/reducible-loss/",
  "prompt": "Extract key details about ReLo: 1) Does ReLo use Polyak averaging (EMA) or periodic hard copy for its target network? 2) What is the exact formula for reducible loss in ReLo? 3) Does ReLo address supervised learning or only RL? 4) What is the relationship between the target network and the reducible loss computation? 5) Any mentions of SAC and its target network mechanism?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88eb6b8d-27a0-4bf5-8a5d-414431d6a408",
  "isSidechain": false,
  "requestId": "req_011CazWUQhdtgq3E48ddESMQ",
  "type": "assistant",
  "uuid": "3a0ae1d7-116a-4535-9445-7289a435d8e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBzTQgntS3nPcDnM4vkdt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 58150,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 58150,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-13T11:43:37.429Z_

<details><summary>↩ Tool result · `toolu_012ZEqZWxtbunnXL4DLuuzFA`</summary>

```text
# ReLo Key Details Analysis

**1) Target Network Update Mechanism:**
The document specifies that the target network is "periodically updated" but does not explicitly state whether Polyak averaging (EMA) or hard copies are used. It only notes the target network "is only periodically updated with the online model parameters."

**2) Reducible Loss Formula:**
The exact formula provided is: "ReLo = L_θ + L_θ_tgt" where L_θ represents loss with online network parameters and L_θ_tgt represents loss with target network parameters.

**3) Application Domain:**
ReLo is specifically designed for reinforcement learning. The method is "tailored to the RL problem" and "can be applied to any off policy Q learning method." The authors acknowledge inspiration from supervised learning (RHO Loss), but ReLo itself addresses RL exclusively.

**4) Target Network Role:**
The target network serves as a proxy for estimating learnable versus noisy samples. The document explains: "a good proxy for the hold-out model is the target network as it is only periodically updated with the online model parameters. It retains the performance of the agent on older data."

**5) SAC Mentions:**
SAC (Soft Actor-Critic) is mentioned as a baseline in continuous control experiments where "ReLo improves performance of the baseline SAC and vanilla PER with SAC," but the document contains no details about SAC's specific target network mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a0ae1d7-116a-4535-9445-7289a435d8e3",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "8a121f36-a4d4-419c-9053-3a9f434addb5",
  "toolUseResult": {
    "bytes": 16367,
    "code": 200,
    "codeText": "OK",
    "result": "# ReLo Key Details Analysis\n\n**1) Target Network Update Mechanism:**\nThe document specifies that the target network is \"periodically updated\" but does not explicitly state whether Polyak averaging (EMA) or hard copies are used. It only notes the target network \"is only periodically updated with the online model parameters.\"\n\n**2) Reducible Loss Formula:**\nThe exact formula provided is: \"ReLo = L_θ + L_θ_tgt\" where L_θ represents loss with online network parameters and L_θ_tgt represents loss with target network parameters.\n\n**3) Application Domain:**\nReLo is specifically designed for reinforcement learning. The method is \"tailored to the RL problem\" and \"can be applied to any off policy Q learning method.\" The authors acknowledge inspiration from supervised learning (RHO Loss), but ReLo itself addresses RL exclusively.\n\n**4) Target Network Role:**\nThe target network serves as a proxy for estimating learnable versus noisy samples. The document explains: \"a good proxy for the hold-out model is the target network as it is only periodically updated with the online model parameters. It retains the performance of the agent on older data.\"\n\n**5) SAC Mentions:**\nSAC (Soft Actor-Critic) is mentioned as a baseline in continuous control experiments where \"ReLo improves performance of the baseline SAC and vanilla PER with SAC,\" but the document contains no details about SAC's specific target network mechanism.",
    "durationMs": 4441,
    "url": "https://shivakanthsujit.github.io/reducible-loss/"
  },
  "sourceToolAssistantUUID": "3a0ae1d7-116a-4535-9445-7289a435d8e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-13T11:43:40.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RbNHVR4sB7jkCV8r9graTz`</summary>

```json
{
  "query": "ReLo reducible loss SAC Polyak averaging target network soft update mechanism NeurIPS paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a121f36-a4d4-419c-9053-3a9f434addb5",
  "isSidechain": false,
  "requestId": "req_011CazWV44CJvSE5PV4DLftB",
  "type": "assistant",
  "uuid": "876cebac-7236-4feb-9c7e-0f03c4618d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRWNqSNnn6rR95P9SiN8ce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 58713,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 526,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 58713,
          "cache_creation_input_tokens": 526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 526
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-13T11:43:46.418Z_

<details><summary>↩ Tool result · `toolu_01RbNHVR4sB7jkCV8r9graTz`</summary>

```text
Web search results for query: "ReLo reducible loss SAC Polyak averaging target network soft update mechanism NeurIPS paper"

Links: [{"title":"Soft Actor-Critic (SAC)","url":"https://www.tedstaley.com/posts/sac/sac.html"},{"title":"Deep Policy Gradient Methods Without Batch Updates, ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/019ef89617d539b15ed610ce8d1b76e1-Paper-Conference.pdf"},{"title":"6 Established RL Models — 1 Minute Each | by James Koh, PhD | MITB For All | Medium","url":"https://medium.com/mitb-for-all/6-established-rl-models-1-min-each-f5a6438f26bb"},{"title":"ReLo: Reducible Loss for RL","url":"https://shivakanthsujit.github.io/reducible-loss/"},{"title":"Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/48726631f87322012c6be38e00c72a47-Paper-Conference.pdf"},{"title":"Target Networks for Training Stability","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-2-deep-q-networks/target-networks"},{"title":"Basic TRFL Usage: Target Network Updating | by AurelianTactics | aureliantactics | Medium","url":"https://medium.com/aureliantactics/basic-trfl-usage-target-network-updating-3660d77a08fd"},{"title":"NeurIPS Poster A General-Purpose Theorem for High-Probability Bounds of Stochastic Approximation with Polyak Averaging","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119445"},{"title":"Soft Actor-Critic — Spinning Up documentation - OpenAI","url":"https://spinningup.openai.com/en/latest/algorithms/sac.html"},{"title":"[Quick Review] Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://liner.com/review/prioritizing-samples-in-reinforcement-learning-with-reducible-loss"}]

Based on the search results, I found relevant information about the ReLo (Reducible Loss) paper and its relationship to SAC, Polyak averaging, and target network mechanisms.

## Key Findings:

**ReLo (Reducible Loss) Overview:**
ReLo is a novel prioritization scheme that quantifies the learn-ability of a sample by measuring the potential reduction in its training loss. This is a NeurIPS 2022 paper that proposes an alternative to traditional prioritized experience replay (PER).

**ReLo with SAC and Soft Update Mechanisms:**
ReLo is robust to the target network update mechanism, whether it is a hard copy of online parameters at a fixed frequency (as in DQN and Rainbow) or if the target network is an exponential moving average of the online parameters (as in Soft Actor Critic). SAC has an online and an exponential moving average target Q network which is used to generate the ReLo priority term.

**Performance with SAC:**
In continuous control tasks, ReLo improves performance of the baseline SAC and vanilla PER with SAC. On 6 of the 9 environments, ReLo outperforms the baseline SAC as well as SAC with PER.

**Computational Efficiency:**
ReLo is computationally efficient, requiring only one additional forward pass through the target network, making it easily integrable into existing off-policy Q-learning algorithms without significant overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "876cebac-7236-4feb-9c7e-0f03c4618d84",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "45248e1d-b231-4dd7-a891-92018e93041e",
  "toolUseResult": {
    "query": "ReLo reducible loss SAC Polyak averaging target network soft update mechanism NeurIPS paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BLANbMW2kycaAHF4wfR9ht",
        "content": [
          {
            "title": "Soft Actor-Critic (SAC)",
            "url": "https://www.tedstaley.com/posts/sac/sac.html"
          },
          {
            "title": "Deep Policy Gradient Methods Without Batch Updates, ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/019ef89617d539b15ed610ce8d1b76e1-Paper-Conference.pdf"
          },
          {
            "title": "6 Established RL Models — 1 Minute Each | by James Koh, PhD | MITB For All | Medium",
            "url": "https://medium.com/mitb-for-all/6-established-rl-models-1-min-each-f5a6438f26bb"
          },
          {
            "title": "ReLo: Reducible Loss for RL",
            "url": "https://shivakanthsujit.github.io/reducible-loss/"
          },
          {
            "title": "Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/48726631f87322012c6be38e00c72a47-Paper-Conference.pdf"
          },
          {
            "title": "Target Networks for Training Stability",
            "url": "https://apxml.com/courses/advanced-reinforcement-learning/chapter-2-deep-q-networks/target-networks"
          },
          {
            "title": "Basic TRFL Usage: Target Network Updating | by AurelianTactics | aureliantactics | Medium",
            "url": "https://medium.com/aureliantactics/basic-trfl-usage-target-network-updating-3660d77a08fd"
          },
          {
            "title": "NeurIPS Poster A General-Purpose Theorem for High-Probability Bounds of Stochastic Approximation with Polyak Averaging",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/119445"
          },
          {
            "title": "Soft Actor-Critic — Spinning Up documentation - OpenAI",
            "url": "https://spinningup.openai.com/en/latest/algorithms/sac.html"
          },
          {
            "title": "[Quick Review] Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://liner.com/review/prioritizing-samples-in-reinforcement-learning-with-reducible-loss"
          }
        ]
      },
      "Based on the search results, I found relevant information about the ReLo (Reducible Loss) paper and its relationship to SAC, Polyak averaging, and target network mechanisms.\n\n## Key Findings:\n\n**ReLo (Reducible Loss) Overview:**\nReLo is a novel prioritization scheme that quantifies the learn-ability of a sample by measuring the potential reduction in its training loss. This is a NeurIPS 2022 paper that proposes an alternative to traditional prioritized experience replay (PER).\n\n**ReLo with SAC and Soft Update Mechanisms:**\nReLo is robust to the target network update mechanism, whether it is a hard copy of online parameters at a fixed frequency (as in DQN and Rainbow) or if the target network is an exponential moving average of the online parameters (as in Soft Actor Critic). SAC has an online and an exponential moving average target Q network which is used to generate the ReLo priority term.\n\n**Performance with SAC:**\nIn continuous control tasks, ReLo improves performance of the baseline SAC and vanilla PER with SAC. On 6 of the 9 environments, ReLo outperforms the baseline SAC as well as SAC with PER.\n\n**Computational Efficiency:**\nReLo is computationally efficient, requiring only one additional forward pass through the target network, making it easily integrable into existing off-policy Q-learning algorithms without significant overhead."
    ],
    "durationSeconds": 5.688527699000027
  },
  "sourceToolAssistantUUID": "876cebac-7236-4feb-9c7e-0f03c4618d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 78 · 2026-05-13T11:43:46.421Z_

```json
{
  "parentUuid": "45248e1d-b231-4dd7-a891-92018e93041e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d103a651-6090-4723-b9a2-119a32eafd60",
  "timestamp": "2026-05-13T11:43:46.421Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d103a651-6090-4723-b9a2-119a32eafd60",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Assistant

_source line 81 · 2026-05-13T11:43:49.828Z_

Good — confirmed that ReLo uses EMA (Polyak averaging) in SAC. The Round 6 proposal correctly identifies this. Now let me search for more potential competitive work and verify remaining claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d103a651-6090-4723-b9a2-119a32eafd60",
  "isSidechain": false,
  "requestId": "req_011CazWViQHPsW3KM5HcyUVy",
  "type": "assistant",
  "uuid": "1a263cff-259c-40c4-a4ee-a2e5f5408e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iRxU71scrCyWaGE7cLZjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 59239,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1107,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 59239,
          "cache_creation_input_tokens": 1107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1107
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-13T11:43:50.639Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RnK8xw3hnmqvggaVagDihC`</summary>

```json
{
  "query": "\"data quality\" \"SFT\" \"reinforcement learning\" \"warm start\" \"initialization\" downstream effect 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a263cff-259c-40c4-a4ee-a2e5f5408e22",
  "isSidechain": false,
  "requestId": "req_011CazWViQHPsW3KM5HcyUVy",
  "type": "assistant",
  "uuid": "0bb56855-92ff-4375-9b6b-a0a5f0d3abc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iRxU71scrCyWaGE7cLZjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 59239,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1107,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 59239,
          "cache_creation_input_tokens": 1107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1107
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-13T11:43:59.737Z_

<details><summary>↩ Tool result · `toolu_01RnK8xw3hnmqvggaVagDihC`</summary>

```text
Web search results for query: ""data quality" "SFT" "reinforcement learning" "warm start" "initialization" downstream effect 2025 2026"

Links: [{"title":"The Best Instruction-Tuning Data are Those That Fit | OpenReview","url":"https://openreview.net/forum?id=4jFSekBaDT"},{"title":"TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...","url":"https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"},{"title":"TAILORED PRIMITIVE INITIALIZATION IS THE SECRET KEY TO ...","url":"https://openreview.net/pdf?id=1tWqSvoeBd"},{"title":"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview","url":"https://openreview.net/forum?id=qJLKOryYeR"},{"title":"Synthetic Data | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/12-synthetic-data"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2026 DATA RECIPES FOR REASONING MODELS","url":"https://openreview.net/pdf?id=7xjoTuaNmN"},{"title":"Curating High-Quality SFT Datasets","url":"https://apxml.com/courses/rlhf-reinforcement-learning-human-feedback/chapter-2-sft-phase-rlhf/sft-dataset-curation"},{"title":"Reinforcement Learning on Pre-Training Data","url":"https://arxiv.org/html/2509.19249v1"},{"title":"AI 101: The State of Reinforcement Learning in 2025","url":"https://turingpost.substack.com/p/ai-101-the-state-of-reinforcement"}]

Based on the search results, I found several highly relevant papers and discussions on the intersection of data quality, SFT, reinforcement learning, warm start, and initialization with downstream effects in 2025-2026. Here are the key findings:

## Key Research Findings

### SFT Data Quality and Downstream RL Performance

Studies show that the distribution of thinking tokens in the SFT dataset strongly influences downstream reasoning performance: when warm-starting from two SFT datasets with different reasoning chain patterns, the resulting RL performance can diverge dramatically, even though both patterns are valid and interpretable to humans.

### Data-Centric Approaches for RL Preparation

Research falls within the data-centric category, focusing specifically on curating the SFT dataset to better prepare LLMs for downstream RL training. One approach proposes the Tailor (Task-AdaptIve, Learning-Primitive-Oriented Reinforcement) finetuning pipeline, which automatically discovers diverse reasoning primitives.

### Quality-Distribution Alignment

SFT is most effective when the data is aligned with the model's pretrained distribution, and aligning supervision with the pretrained distribution provides a simple yet powerful strategy to improve both the efficiency and effectiveness of SFT.

### SFT as Foundation for RL

As the initial post-training stage, SFT teaches LLMs to follow instructions, and once these models can produce responses that are clear, interpretable, and verifiable for annotators, they become well-suited for leveraging human feedback in downstream tasks via techniques like reinforcement learning. SFT's primary objective is to align the output space of pre-trained LLMs with the preferred formats of downstream tasks.

### Preventing Catastrophic Forgetting

SFT's tendency to memorize a small set of expert data for a downstream task can impair generalization and lead to catastrophic forgetting of prior knowledge, but applying clipped strategies can reduce forgetting on out-of-distribution tasks by 11.54% and boost final RL performance by 7.09%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bb56855-92ff-4375-9b6b-a0a5f0d3abc8",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "c2227415-f48a-451d-936a-1afb2a2b033b",
  "toolUseResult": {
    "query": "\"data quality\" \"SFT\" \"reinforcement learning\" \"warm start\" \"initialization\" downstream effect 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LcPS4Ra37BVdEzqJK7y6xP",
        "content": [
          {
            "title": "The Best Instruction-Tuning Data are Those That Fit | OpenReview",
            "url": "https://openreview.net/forum?id=4jFSekBaDT"
          },
          {
            "title": "TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...",
            "url": "https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"
          },
          {
            "title": "TAILORED PRIMITIVE INITIALIZATION IS THE SECRET KEY TO ...",
            "url": "https://openreview.net/pdf?id=1tWqSvoeBd"
          },
          {
            "title": "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview",
            "url": "https://openreview.net/forum?id=qJLKOryYeR"
          },
          {
            "title": "Synthetic Data | RLHF Book by Nathan Lambert",
            "url": "https://rlhfbook.com/c/12-synthetic-data"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 DATA RECIPES FOR REASONING MODELS",
            "url": "https://openreview.net/pdf?id=7xjoTuaNmN"
          },
          {
            "title": "Curating High-Quality SFT Datasets",
            "url": "https://apxml.com/courses/rlhf-reinforcement-learning-human-feedback/chapter-2-sft-phase-rlhf/sft-dataset-curation"
          },
          {
            "title": "Reinforcement Learning on Pre-Training Data",
            "url": "https://arxiv.org/html/2509.19249v1"
          },
          {
            "title": "AI 101: The State of Reinforcement Learning in 2025",
            "url": "https://turingpost.substack.com/p/ai-101-the-state-of-reinforcement"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and discussions on the intersection of data quality, SFT, reinforcement learning, warm start, and initialization with downstream effects in 2025-2026. Here are the key findings:\n\n## Key Research Findings\n\n### SFT Data Quality and Downstream RL Performance\n\nStudies show that the distribution of thinking tokens in the SFT dataset strongly influences downstream reasoning performance: when warm-starting from two SFT datasets with different reasoning chain patterns, the resulting RL performance can diverge dramatically, even though both patterns are valid and interpretable to humans.\n\n### Data-Centric Approaches for RL Preparation\n\nResearch falls within the data-centric category, focusing specifically on curating the SFT dataset to better prepare LLMs for downstream RL training. One approach proposes the Tailor (Task-AdaptIve, Learning-Primitive-Oriented Reinforcement) finetuning pipeline, which automatically discovers diverse reasoning primitives.\n\n### Quality-Distribution Alignment\n\nSFT is most effective when the data is aligned with the model's pretrained distribution, and aligning supervision with the pretrained distribution provides a simple yet powerful strategy to improve both the efficiency and effectiveness of SFT.\n\n### SFT as Foundation for RL\n\nAs the initial post-training stage, SFT teaches LLMs to follow instructions, and once these models can produce responses that are clear, interpretable, and verifiable for annotators, they become well-suited for leveraging human feedback in downstream tasks via techniques like reinforcement learning. SFT's primary objective is to align the output space of pre-trained LLMs with the preferred formats of downstream tasks.\n\n### Preventing Catastrophic Forgetting\n\nSFT's tendency to memorize a small set of expert data for a downstream task can impair generalization and lead to catastrophic forgetting of prior knowledge, but applying clipped strategies can reduce forgetting on out-of-distribution tasks by 11.54% and boost final RL performance by 7.09%."
    ],
    "durationSeconds": 9.093849056000007
  },
  "sourceToolAssistantUUID": "0bb56855-92ff-4375-9b6b-a0a5f0d3abc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-13T11:44:03.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGdumWJjKJmQ5c9qKGbNxm`</summary>

```json
{
  "query": "\"Tailored Primitive Initialization\" 2511.12429 SFT demonstration diversity RL reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2227415-f48a-451d-936a-1afb2a2b033b",
  "isSidechain": false,
  "requestId": "req_011CazWWhYiJdQTaFpDPPnjq",
  "type": "assistant",
  "uuid": "6b0e5dd6-9dbe-4882-aa50-e9334c98da6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJg6W2jZHT3oN6UUp1uL4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 60346,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 60346,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-13T11:44:10.488Z_

<details><summary>↩ Tool result · `toolu_01KGdumWJjKJmQ5c9qKGbNxm`</summary>

```text
Web search results for query: ""Tailored Primitive Initialization" 2511.12429 SFT demonstration diversity RL reasoning"

Links: [{"title":"[2511.12429] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/abs/2511.12429"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/html/2511.12429v1"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2511.12429v1"},{"title":"[Literature Review] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://www.themoonlight.io/en/review/tailored-primitive-initialization-is-the-secret-key-to-reinforcement-learning"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=1tWqSvoeBd"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/397700530_Tailored_Primitive_Initialization_is_the_Secret_Key_to_Reinforcement_Learning"},{"title":"TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...","url":"https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"},{"title":"[2511.17852] Transformers with RL or SFT Provably Learn Sparse Boolean Functions, But Differently","url":"https://arxiv.org/abs/2511.17852"},{"title":"[2511.11113v1] VIDEOP2R: Video Understanding from Perception to Reasoning","url":"https://arxiv.org/abs/2511.11113v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Summary

The paper "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning" (arXiv 2511.12429) addresses challenges in applying reinforcement learning to large language models for reasoning tasks.

**Key Problem:** RL faces challenges including low sampling efficiency and strong dependence on model initialization, where some models achieve rapid improvements with minimal RL steps while others require significant training data to make progress.

**Main Approach:** The paper proposes Tailor, a finetuning pipeline that automatically discovers and curates novel reasoning primitives, thereby expanding the coverage of reasoning-state distributions before RL.

**Core Insight:** Most existing warm-start pipelines, where supervised fine-tuning (SFT) precedes the RL stage, include only a limited set of primitive patterns, such as rule-based traces or distilled target behaviors from the SFT dataset. However, these often exhibit low coverage of the reasoning token distribution, leading to inefficient exploration and slower RL improvement.

**Demonstration Diversity:** Diversity analysis using NV-Embed-v2 showed that Tailor significantly increased the diversity of high-level reasoning primitives in the SFT dataset, as indicated by lower pairwise cosine similarity scores of thinking token embeddings.

**Results:** Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that Tailor generates more diverse and higher-quality warm-start data, resulting in higher downstream RL performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b0e5dd6-9dbe-4882-aa50-e9334c98da6b",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "0448fe40-05cc-4eee-9f9d-2c7fc91e585f",
  "toolUseResult": {
    "query": "\"Tailored Primitive Initialization\" 2511.12429 SFT demonstration diversity RL reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bd4Nb94Ff6TKrCzCPhGnrV",
        "content": [
          {
            "title": "[2511.12429] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://arxiv.org/abs/2511.12429"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://arxiv.org/html/2511.12429v1"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2511.12429v1"
          },
          {
            "title": "[Literature Review] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/tailored-primitive-initialization-is-the-secret-key-to-reinforcement-learning"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=1tWqSvoeBd"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/397700530_Tailored_Primitive_Initialization_is_the_Secret_Key_to_Reinforcement_Learning"
          },
          {
            "title": "TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...",
            "url": "https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"
          },
          {
            "title": "[2511.17852] Transformers with RL or SFT Provably Learn Sparse Boolean Functions, But Differently",
            "url": "https://arxiv.org/abs/2511.17852"
          },
          {
            "title": "[2511.11113v1] VIDEOP2R: Video Understanding from Perception to Reasoning",
            "url": "https://arxiv.org/abs/2511.11113v1"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2508.05629"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for:\n\n## Summary\n\nThe paper \"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning\" (arXiv 2511.12429) addresses challenges in applying reinforcement learning to large language models for reasoning tasks.\n\n**Key Problem:** RL faces challenges including low sampling efficiency and strong dependence on model initialization, where some models achieve rapid improvements with minimal RL steps while others require significant training data to make progress.\n\n**Main Approach:** The paper proposes Tailor, a finetuning pipeline that automatically discovers and curates novel reasoning primitives, thereby expanding the coverage of reasoning-state distributions before RL.\n\n**Core Insight:** Most existing warm-start pipelines, where supervised fine-tuning (SFT) precedes the RL stage, include only a limited set of primitive patterns, such as rule-based traces or distilled target behaviors from the SFT dataset. However, these often exhibit low coverage of the reasoning token distribution, leading to inefficient exploration and slower RL improvement.\n\n**Demonstration Diversity:** Diversity analysis using NV-Embed-v2 showed that Tailor significantly increased the diversity of high-level reasoning primitives in the SFT dataset, as indicated by lower pairwise cosine similarity scores of thinking token embeddings.\n\n**Results:** Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that Tailor generates more diverse and higher-quality warm-start data, resulting in higher downstream RL performance."
    ],
    "durationSeconds": 7.430006139000005
  },
  "sourceToolAssistantUUID": "6b0e5dd6-9dbe-4882-aa50-e9334c98da6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-13T11:44:13.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QvLqptE5Utyv1j11zayaoB`</summary>

```json
{
  "query": "demonstration noise filtering robot learning EMA model loss decomposition online data weighting 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0448fe40-05cc-4eee-9f9d-2c7fc91e585f",
  "isSidechain": false,
  "requestId": "req_011CazWXVZRHAePzrHkYjLiS",
  "type": "assistant",
  "uuid": "cebd5a51-f749-4060-b094-59b494d817e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015svD3jCuGFiQ6FnbJVSbpS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 61478,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 61478,
          "cache_creation_input_tokens": 974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 974
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-13T11:44:21.384Z_

<details><summary>↩ Tool result · `toolu_01QvLqptE5Utyv1j11zayaoB`</summary>

```text
Web search results for query: "demonstration noise filtering robot learning EMA model loss decomposition online data weighting 2025 2026 arxiv"

Links: [{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=1900&show=2000"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=25&show=2000"},{"title":"[2302.06548] Automatic Noise Filtering with Dynamic Sparse Training in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2302.06548"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=2425&show=2000"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=1975&show=2000"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=6875&show=2000"},{"title":"Robotics Mar 2025","url":"https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"}]

Based on the web search results, I found several relevant papers related to robot learning and related techniques, though I didn't locate a single paper that exactly matches all the specific terms in your query. Here are the most relevant findings:

## Key Related Papers and Topics Found:

1. **Noise Filtering in Robot Learning**: The search returned "Automatic Noise Filtering" (ANF), which uses the principles of dynamic sparse training in synergy with various deep reinforcement learning algorithms, published in 2023.

2. **Robot Learning from Demonstrations**: Imitation Learning (IL), also known as Learning from Demonstration (LfD) or Robot programming by Demonstration (PbD), relies on an autonomous agent learning to execute tasks or acquiring new skills by observing/emulating demonstrations provided by an expert.

3. **Recent Robot Learning Advances (2025-2026)**: The search results show numerous recent papers on robot learning from March through July 2025, with several accepted to major conferences like ICLR 2026, including work on fine-tuning that allows generalist foundation models to efficiently adapt to specific tasks, environments, and robotic platforms.

4. **World Models for Robot Learning**: Recent work includes actionable world models providing foresight (anticipating future states or action consequences before execution), imagination-driven planning, and data amplification (synthesizing additional demonstrations or interaction trajectories to improve learning).

The search results show active research in these areas during 2025-2026 on arXiv, though I did not find a single paper matching all your specific technical terms (EMA model loss decomposition, online data weighting) in the snippets returned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cebd5a51-f749-4060-b094-59b494d817e3",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "9d11ba1e-7880-4d65-80d7-b7f3f57a7482",
  "toolUseResult": {
    "query": "demonstration noise filtering robot learning EMA model loss decomposition online data weighting 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_012q4fqZiJP7cPyn8qM9qoTp",
        "content": [
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"
          },
          {
            "title": "Machine Learning Mar 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-03?skip=1900&show=2000"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-07?skip=25&show=2000"
          },
          {
            "title": "[2302.06548] Automatic Noise Filtering with Dynamic Sparse Training in Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2302.06548"
          },
          {
            "title": "Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions",
            "url": "https://arxiv.org/html/2604.15395v1"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2605.00080v1"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-06?skip=2425&show=2000"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://arxiv.org/list/cs/2025-05?skip=1975&show=2000"
          },
          {
            "title": "Computer Science Jun 2025",
            "url": "https://arxiv.org/list/cs/2025-06?skip=6875&show=2000"
          },
          {
            "title": "Robotics Mar 2025",
            "url": "https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers related to robot learning and related techniques, though I didn't locate a single paper that exactly matches all the specific terms in your query. Here are the most relevant findings:\n\n## Key Related Papers and Topics Found:\n\n1. **Noise Filtering in Robot Learning**: The search returned \"Automatic Noise Filtering\" (ANF), which uses the principles of dynamic sparse training in synergy with various deep reinforcement learning algorithms, published in 2023.\n\n2. **Robot Learning from Demonstrations**: Imitation Learning (IL), also known as Learning from Demonstration (LfD) or Robot programming by Demonstration (PbD), relies on an autonomous agent learning to execute tasks or acquiring new skills by observing/emulating demonstrations provided by an expert.\n\n3. **Recent Robot Learning Advances (2025-2026)**: The search results show numerous recent papers on robot learning from March through July 2025, with several accepted to major conferences like ICLR 2026, including work on fine-tuning that allows generalist foundation models to efficiently adapt to specific tasks, environments, and robotic platforms.\n\n4. **World Models for Robot Learning**: Recent work includes actionable world models providing foresight (anticipating future states or action consequences before execution), imagination-driven planning, and data amplification (synthesizing additional demonstrations or interaction trajectories to improve learning).\n\nThe search results show active research in these areas during 2025-2026 on arXiv, though I did not find a single paper matching all your specific technical terms (EMA model loss decomposition, online data weighting) in the snippets returned."
    ],
    "durationSeconds": 7.628126871000044
  },
  "sourceToolAssistantUUID": "cebd5a51-f749-4060-b094-59b494d817e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-13T11:44:24.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GkKHi7epaJ2NEVDwuUVcS3`</summary>

```json
{
  "query": "DS2 dynamic loss sample reweighting LLM pretraining ICLR 2025 2502.06733"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d11ba1e-7880-4d65-80d7-b7f3f57a7482",
  "isSidechain": false,
  "requestId": "req_011CazWYHtEXFGsoUWCr57DV",
  "type": "assistant",
  "uuid": "4081493f-ca90-4fd8-90ca-a69295e37d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1FPP6Us6rFDekH8hqZLR6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 62452,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 62452,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-13T11:44:30.999Z_

<details><summary>↩ Tool result · `toolu_01GkKHi7epaJ2NEVDwuUVcS3`</summary>

```text
Web search results for query: "DS2 dynamic loss sample reweighting LLM pretraining ICLR 2025 2502.06733"

Links: [{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/html/2502.06733v1"},{"title":"[2502.06733] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://arxiv.org/abs/2502.06733"},{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=gU4ZgQNsOC"},{"title":"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/dynamic-loss-based-sample-reweighting-for-improved-large-language-model-pretraining"},{"title":"DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...","url":"https://shiqiang.wang/papers/DS_ICLR2025.pdf"},{"title":"A View on Language Model Pre-training and Inference: Data curation, sample reweighting, and energy-optimal inference for higher user satisfaction | HKUST CSE","url":"https://cse.hkust.edu.hk/pg/seminars/S25/woisetschlager.html"},{"title":"ICLR Poster Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://iclr.cc/virtual/2025/poster/28818"},{"title":"[Quick Review] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining","url":"https://liner.com/review/dynamic-lossbased-sample-reweighting-for-improved-large-language-model-pretraining"},{"title":"GitHub - F-JISOO/ICLR-2025-Submitted · GitHub","url":"https://github.com/F-JISOO/ICLR-2025-Submitted"},{"title":"Sampling and Loss Weights in Multi-Domain Training","url":"https://arxiv.org/html/2511.06913v1"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining

This is a paper accepted at ICLR 2025 by Daouda Sow and colleagues, with the arXiv ID 2502.06733.

**Core Contribution:**

The paper introduces novel algorithms for dynamic, instance-level data reweighting aimed at improving both the efficiency and effectiveness of LLM pretraining. The methods adjust the weight of each training sample based on its loss value in an online fashion, allowing the model to dynamically focus on more informative or important samples at the current training stage.

**Key Features:**

- The framework allows for devising reweighting strategies deprioritizing redundant or uninformative data, which work best
- The research introduces novel dynamic instance-level loss-based reweighting strategies, such as LinUpper, Quadratic, and Extremes, to optimize learning dynamics

**Theoretical and Empirical Results:**

The paper develops a new theoretical framework for analyzing the impact of loss-based reweighting on the convergence of gradient-based optimization, providing the first formal characterization of how these strategies affect convergence bounds. The approach is empirically validated across a spectrum of tasks, from pretraining 7B and 1.4B parameter LLMs to smaller-scale language models, demonstrating faster convergence and significantly improved performance.

A ready-to-use implementation is available on GitHub for the GPT2 experiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4081493f-ca90-4fd8-90ca-a69295e37d82",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "10c5f4fd-c55e-43d6-a846-b687c3b665a6",
  "toolUseResult": {
    "query": "DS2 dynamic loss sample reweighting LLM pretraining ICLR 2025 2502.06733",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jrgt3SpPhaDhFawHwwtmcJ",
        "content": [
          {
            "title": "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining",
            "url": "https://arxiv.org/html/2502.06733v1"
          },
          {
            "title": "[2502.06733] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining",
            "url": "https://arxiv.org/abs/2502.06733"
          },
          {
            "title": "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining | OpenReview",
            "url": "https://openreview.net/forum?id=gU4ZgQNsOC"
          },
          {
            "title": "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining for ICLR 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/dynamic-loss-based-sample-reweighting-for-improved-large-language-model-pretraining"
          },
          {
            "title": "DYNAMIC LOSS-BASED SAMPLE REWEIGHTING FOR ...",
            "url": "https://shiqiang.wang/papers/DS_ICLR2025.pdf"
          },
          {
            "title": "A View on Language Model Pre-training and Inference: Data curation, sample reweighting, and energy-optimal inference for higher user satisfaction | HKUST CSE",
            "url": "https://cse.hkust.edu.hk/pg/seminars/S25/woisetschlager.html"
          },
          {
            "title": "ICLR Poster Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining",
            "url": "https://iclr.cc/virtual/2025/poster/28818"
          },
          {
            "title": "[Quick Review] Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining",
            "url": "https://liner.com/review/dynamic-lossbased-sample-reweighting-for-improved-large-language-model-pretraining"
          },
          {
            "title": "GitHub - F-JISOO/ICLR-2025-Submitted · GitHub",
            "url": "https://github.com/F-JISOO/ICLR-2025-Submitted"
          },
          {
            "title": "Sampling and Loss Weights in Multi-Domain Training",
            "url": "https://arxiv.org/html/2511.06913v1"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for:\n\n## Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining\n\nThis is a paper accepted at ICLR 2025 by Daouda Sow and colleagues, with the arXiv ID 2502.06733.\n\n**Core Contribution:**\n\nThe paper introduces novel algorithms for dynamic, instance-level data reweighting aimed at improving both the efficiency and effectiveness of LLM pretraining. The methods adjust the weight of each training sample based on its loss value in an online fashion, allowing the model to dynamically focus on more informative or important samples at the current training stage.\n\n**Key Features:**\n\n- The framework allows for devising reweighting strategies deprioritizing redundant or uninformative data, which work best\n- The research introduces novel dynamic instance-level loss-based reweighting strategies, such as LinUpper, Quadratic, and Extremes, to optimize learning dynamics\n\n**Theoretical and Empirical Results:**\n\nThe paper develops a new theoretical framework for analyzing the impact of loss-based reweighting on the convergence of gradient-based optimization, providing the first formal characterization of how these strategies affect convergence bounds. The approach is empirically validated across a spectrum of tasks, from pretraining 7B and 1.4B parameter LLMs to smaller-scale language models, demonstrating faster convergence and significantly improved performance.\n\nA ready-to-use implementation is available on GitHub for the GPT2 experiments."
    ],
    "durationSeconds": 6.754584396999969
  },
  "sourceToolAssistantUUID": "4081493f-ca90-4fd8-90ca-a69295e37d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 90_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "10c5f4fd-c55e-43d6-a846-b687c3b665a6",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 91_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool call

_source line 92 · 2026-05-13T11:44:34.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HmqHwuir5GRhgv8e1LCxht`</summary>

```json
{
  "query": "LIBERO-Long benchmark success rate state of the art 2026 VLA OpenVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c5f4fd-c55e-43d6-a846-b687c3b665a6",
  "isSidechain": false,
  "requestId": "req_011CazWZ1GNtvP1ZCaLKfkG3",
  "type": "assistant",
  "uuid": "9f89ebf2-bcbd-494c-917d-837429b1b8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Txg38izAbKisb6eoh5johW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 63363,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 63363,
          "cache_creation_input_tokens": 1026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1026
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-13T11:44:42.398Z_

<details><summary>↩ Tool result · `toolu_01HmqHwuir5GRhgv8e1LCxht`</summary>

```text
Web search results for query: "LIBERO-Long benchmark success rate state of the art 2026 VLA OpenVLA"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"}]

Based on the search results, here's what I found regarding LIBERO-Long benchmark success rates and state-of-the-art VLA performance in 2026:

## LIBERO-Long Benchmark Performance

On LIBERO, strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal, and 30-60 percent on LIBERO-100 depending on training recipe. Note that LIBERO-100 appears to refer to the longer-horizon tasks in the LIBERO benchmark suite.

## State-of-the-Art Results

The current state-of-the-art on standard LIBERO is held by OpenVLA-OFT (Optimized Fine-Tuning variant):

OpenVLA-OFT, a policy created with a fine-tuning recipe, achieves SOTA results in LIBERO: 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy. More recent variants have pushed this even higher: VLA-IAP achieves a state-of-the-art average success rate of 97.8%, and a self-improving method achieves near-saturated 99% success rates on the LIBERO benchmark.

## Important Context

However, it's crucial to note that despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components. This suggests that high benchmark scores mask limitations in true robustness and generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f89ebf2-bcbd-494c-917d-837429b1b8c3",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "6199882a-3dd3-49f3-a170-e536bab180b8",
  "toolUseResult": {
    "query": "LIBERO-Long benchmark success rate state of the art 2026 VLA OpenVLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_0122szADavZWqojzrAZvz2jQ",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found regarding LIBERO-Long benchmark success rates and state-of-the-art VLA performance in 2026:\n\n## LIBERO-Long Benchmark Performance\n\nOn LIBERO, strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal, and 30-60 percent on LIBERO-100 depending on training recipe. Note that LIBERO-100 appears to refer to the longer-horizon tasks in the LIBERO benchmark suite.\n\n## State-of-the-Art Results\n\nThe current state-of-the-art on standard LIBERO is held by OpenVLA-OFT (Optimized Fine-Tuning variant):\n\nOpenVLA-OFT, a policy created with a fine-tuning recipe, achieves SOTA results in LIBERO: 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy. More recent variants have pushed this even higher: VLA-IAP achieves a state-of-the-art average success rate of 97.8%, and a self-improving method achieves near-saturated 99% success rates on the LIBERO benchmark.\n\n## Important Context\n\nHowever, it's crucial to note that despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components. This suggests that high benchmark scores mask limitations in true robustness and generalization."
    ],
    "durationSeconds": 7.910389223000035
  },
  "sourceToolAssistantUUID": "9f89ebf2-bcbd-494c-917d-837429b1b8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-13T11:44:45.511Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbLZYTYv5XF8GYUfWaLRoG`</summary>

```json
{
  "query": "Green-VLA DataQA pipeline data quality VLA 2602.00919 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6199882a-3dd3-49f3-a170-e536bab180b8",
  "isSidechain": false,
  "requestId": "req_011CazWZqmewWsvPxeJefYsA",
  "type": "assistant",
  "uuid": "7e1b360a-3b84-4fed-8ae7-1ac0a9a60d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXKNza945AoSux3b7Doucf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 64389,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 64389,
          "cache_creation_input_tokens": 1031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1031
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-13T11:44:53.369Z_

<details><summary>↩ Tool result · `toolu_01MbLZYTYv5XF8GYUfWaLRoG`</summary>

```text
Web search results for query: "Green-VLA DataQA pipeline data quality VLA 2602.00919 2026"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919"},{"title":"Paper page - Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://huggingface.co/papers/2602.00919"},{"title":"[2602.00919] Green-VLA: Staged Vision-Language-Action Model for Generalist Robots","url":"https://arxiv.org/abs/2602.00919"},{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://greenvla.github.io/"},{"title":"Green-VLA: Staged Vision–Language–Action Model for Generalist Robots","url":"https://arxiv.org/pdf/2602.00919"},{"title":"VLA Calibration Pipeline 2025.1.0.32; CASA version 6.6.6-17 and Pipeline 2025.1.036; CASA version 6.6.6-18 — NRAO Science Site","url":"https://science.nrao.edu/facilities/vla/data-processing/pipeline"},{"title":"6. The Data Reduction and Analysis Pipeline","url":"http://sundog.stsci.edu/first/apj/sectionstar3_7.html"},{"title":"The Very Large Array Data Processing Pipeline - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018AAS...23134214K/abstract"},{"title":"Interpreting QA2 Scores — NRAO Science Site","url":"https://science.nrao.edu/facilities/vla/data-processing/pipeline/interpreting-qa2-scores"},{"title":"NRAO Science Ready Data Products in the Era of ngVLA - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021AAS...23753510T/abstract"}]

Based on the search results, I found information about the Green-VLA DataQA pipeline. The query returned results primarily about Green-VLA, a robotics framework (arxiv paper 2602.00919), rather than the Very Large Array (VLA) astronomical facility.

## Green-VLA DataQA Pipeline

The DataQA pipeline was employed for robotic dataset curation and quality assessment, enabling the model training to focus on high-quality demonstrations and improving both sample efficiency and final policy performance.

The DataQA Pipeline uses quality filtering with jitter (J), sharpness (S), diversity (D), and variance (σ²) metrics, enabling superior sample efficiency—achieving better results with 3,000 hours than competitors with 10,000+ hours.

At the data level, the DataQA pipeline filters and smooths heterogeneous demonstrations and aligns temporal dynamics via optical flow–based resampling.

The pipeline auto-filters 3,000+ hours using jitter, sharpness, diversity, and state variance metrics plus optical-flow alignment, enabling stable multi-embodiment training with improved data efficiency.

This DataQA pipeline is part of the Green-VLA framework, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e1b360a-3b84-4fed-8ae7-1ac0a9a60d2b",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "7f111610-fc14-4368-bdb3-ad577827d87b",
  "toolUseResult": {
    "query": "Green-VLA DataQA pipeline data quality VLA 2602.00919 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QCyMtgtG3bK3GVj1rpLMR7",
        "content": [
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2602.00919"
          },
          {
            "title": "Paper page - Green-VLA: Staged Vision-Language-Action Model for Generalist Robots",
            "url": "https://huggingface.co/papers/2602.00919"
          },
          {
            "title": "[2602.00919] Green-VLA: Staged Vision-Language-Action Model for Generalist Robots",
            "url": "https://arxiv.org/abs/2602.00919"
          },
          {
            "title": "Green-VLA: Staged Vision–Language–Action Model for Generalist Robots",
            "url": "https://greenvla.github.io/"
          },
          {
            "title": "Green-VLA: Staged Vision–Language–Action Model for Generalist Robots",
            "url": "https://arxiv.org/pdf/2602.00919"
          },
          {
            "title": "VLA Calibration Pipeline 2025.1.0.32; CASA version 6.6.6-17 and Pipeline 2025.1.036; CASA version 6.6.6-18 — NRAO Science Site",
            "url": "https://science.nrao.edu/facilities/vla/data-processing/pipeline"
          },
          {
            "title": "6. The Data Reduction and Analysis Pipeline",
            "url": "http://sundog.stsci.edu/first/apj/sectionstar3_7.html"
          },
          {
            "title": "The Very Large Array Data Processing Pipeline - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2018AAS...23134214K/abstract"
          },
          {
            "title": "Interpreting QA2 Scores — NRAO Science Site",
            "url": "https://science.nrao.edu/facilities/vla/data-processing/pipeline/interpreting-qa2-scores"
          },
          {
            "title": "NRAO Science Ready Data Products in the Era of ngVLA - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021AAS...23753510T/abstract"
          }
        ]
      },
      "Based on the search results, I found information about the Green-VLA DataQA pipeline. The query returned results primarily about Green-VLA, a robotics framework (arxiv paper 2602.00919), rather than the Very Large Array (VLA) astronomical facility.\n\n## Green-VLA DataQA Pipeline\n\nThe DataQA pipeline was employed for robotic dataset curation and quality assessment, enabling the model training to focus on high-quality demonstrations and improving both sample efficiency and final policy performance.\n\nThe DataQA Pipeline uses quality filtering with jitter (J), sharpness (S), diversity (D), and variance (σ²) metrics, enabling superior sample efficiency—achieving better results with 3,000 hours than competitors with 10,000+ hours.\n\nAt the data level, the DataQA pipeline filters and smooths heterogeneous demonstrations and aligns temporal dynamics via optical flow–based resampling.\n\nThe pipeline auto-filters 3,000+ hours using jitter, sharpness, diversity, and state variance metrics plus optical-flow alignment, enabling stable multi-embodiment training with improved data efficiency.\n\nThis DataQA pipeline is part of the Green-VLA framework, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments."
    ],
    "durationSeconds": 7.851944162000029
  },
  "sourceToolAssistantUUID": "7e1b360a-3b84-4fed-8ae7-1ac0a9a60d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-13T11:44:56.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WQNZEoeG9i7xyEU9u8XPiU`</summary>

```json
{
  "query": "sample-level online adaptive data selection during SFT training noise-robust 2025 2026 robot imitation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f111610-fc14-4368-bdb3-ad577827d87b",
  "isSidechain": false,
  "requestId": "req_011CazWaefh9HLo4VvkfNDN7",
  "type": "assistant",
  "uuid": "536873c9-2dd1-48a6-bac2-344083cb3bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGm5okiALSsX2pEiQtfQez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 65420,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 65420,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 886
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-13T11:45:03.993Z_

<details><summary>↩ Tool result · `toolu_01WQNZEoeG9i7xyEU9u8XPiU`</summary>

```text
Web search results for query: "sample-level online adaptive data selection during SFT training noise-robust 2025 2026 robot imitation"

Links: [{"title":"RESample: A Robust Data Augmentation Framework via Exploratory Sampling for Robotic Manipulation","url":"https://arxiv.org/html/2510.17640"},{"title":"Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"},{"title":"[2510.17640] RESample: A Robust Data Augmentation Framework via Exploratory Sampling for Robotic Manipulation","url":"https://arxiv.org/abs/2510.17640"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v2"},{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"IntervenGen","url":"https://sites.google.com/view/intervengen2024"},{"title":"[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/abs/2505.09603"},{"title":"A Survey on Reinforcement Learning of Vision-Language-Action Models for Robotic Manipulation | TechRxiv","url":"https://www.techrxiv.org/users/934012/articles/1366553/master/file/data/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf?inline=true"},{"title":"Robot See, Robot Do: On the Development of Robust and Adaptive Imitation Learning for Robots","url":"https://vtechworks.lib.vt.edu/items/d885e933-b35c-4279-8820-f0fb32db4c54"},{"title":"[1703.09327] DART: Noise Injection for Robust Imitation Learning","url":"https://arxiv.org/abs/1703.09327"}]

I found several relevant research papers related to your search query. Here are the key results:

## Recent Papers on Noise-Robust Robot Imitation Learning (2025-2026)

### RESample: Robust Data Augmentation for Robotic Manipulation
RESample is an automated OOD data augmentation framework through exploratory sampling that designs an exploratory sampling mechanism that adaptively incorporates action proxies into the training dataset to ensure efficiency. The framework explicitly encourages VLAs to recover from OOD states and enhances their robustness against distributional shifts.

### DataMIL: Data Selection for Robot Imitation Learning
DataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance.

### RoboTwin 2.0: Domain Randomization for Bimanual Manipulation
Domain randomization approaches including noise injection in expert demonstrations enable robust visuomotor policies, and RoboTwin 2.0 integrates interactive simulation feedback with systematic domain randomization to generate higher-fidelity imitation data.

### Interactive Imitation Learning Advances
Recent work proposes using agent-generated data that lead to errors as examples of "what not to do," using this data in an ergodic imitation learning framework, leading to more robust policies.

These papers collectively address sample-level adaptive data selection, noise robustness, and supervised fine-tuning (SFT) strategies for robot imitation learning in the 2025-2026 timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "536873c9-2dd1-48a6-bac2-344083cb3bb1",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "291f2b78-d962-4bdf-b6f8-a11192fe0628",
  "toolUseResult": {
    "query": "sample-level online adaptive data selection during SFT training noise-robust 2025 2026 robot imitation",
    "results": [
      {
        "tool_use_id": "srvtoolu_016GJd6VeuGJ5ywQCbvHQHBR",
        "content": [
          {
            "title": "RESample: A Robust Data Augmentation Framework via Exploratory Sampling for Robotic Manipulation",
            "url": "https://arxiv.org/html/2510.17640"
          },
          {
            "title": "Imitation learning for legged robot locomotion: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"
          },
          {
            "title": "[2510.17640] RESample: A Robust Data Augmentation Framework via Exploratory Sampling for Robotic Manipulation",
            "url": "https://arxiv.org/abs/2510.17640"
          },
          {
            "title": "RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation",
            "url": "https://arxiv.org/html/2506.18088v2"
          },
          {
            "title": "Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"
          },
          {
            "title": "IntervenGen",
            "url": "https://sites.google.com/view/intervengen2024"
          },
          {
            "title": "[2505.09603] DataMIL: Selecting Data for Robot Imitation Learning with Datamodels",
            "url": "https://arxiv.org/abs/2505.09603"
          },
          {
            "title": "A Survey on Reinforcement Learning of Vision-Language-Action Models for Robotic Manipulation | TechRxiv",
            "url": "https://www.techrxiv.org/users/934012/articles/1366553/master/file/data/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf?inline=true"
          },
          {
            "title": "Robot See, Robot Do: On the Development of Robust and Adaptive Imitation Learning for Robots",
            "url": "https://vtechworks.lib.vt.edu/items/d885e933-b35c-4279-8820-f0fb32db4c54"
          },
          {
            "title": "[1703.09327] DART: Noise Injection for Robust Imitation Learning",
            "url": "https://arxiv.org/abs/1703.09327"
          }
        ]
      },
      "I found several relevant research papers related to your search query. Here are the key results:\n\n## Recent Papers on Noise-Robust Robot Imitation Learning (2025-2026)\n\n### RESample: Robust Data Augmentation for Robotic Manipulation\nRESample is an automated OOD data augmentation framework through exploratory sampling that designs an exploratory sampling mechanism that adaptively incorporates action proxies into the training dataset to ensure efficiency. The framework explicitly encourages VLAs to recover from OOD states and enhances their robustness against distributional shifts.\n\n### DataMIL: Data Selection for Robot Imitation Learning\nDataMIL is a policy-driven data selection framework built on the datamodels paradigm that reasons about data selection in an end-to-end manner, using the policy itself to identify which data points will most improve performance.\n\n### RoboTwin 2.0: Domain Randomization for Bimanual Manipulation\nDomain randomization approaches including noise injection in expert demonstrations enable robust visuomotor policies, and RoboTwin 2.0 integrates interactive simulation feedback with systematic domain randomization to generate higher-fidelity imitation data.\n\n### Interactive Imitation Learning Advances\nRecent work proposes using agent-generated data that lead to errors as examples of \"what not to do,\" using this data in an ergodic imitation learning framework, leading to more robust policies.\n\nThese papers collectively address sample-level adaptive data selection, noise robustness, and supervised fine-tuning (SFT) strategies for robot imitation learning in the 2025-2026 timeframe."
    ],
    "durationSeconds": 7.174648721000005
  },
  "sourceToolAssistantUUID": "536873c9-2dd1-48a6-bac2-344083cb3bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-13T11:45:06.828Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KDy6WwcB9RfNfLN34kGmf2`</summary>

```json
{
  "query": "\"density ratio\" weighted behavioral cloning VLA demonstration curation arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291f2b78-d962-4bdf-b6f8-a11192fe0628",
  "isSidechain": false,
  "requestId": "req_011CazWbS4wCAdJG6CPEGcsc",
  "type": "assistant",
  "uuid": "61e07e6c-1fb9-4788-939c-fcb6563b8890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUorMfpQh57D4eywiSyCYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 66306,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 66306,
          "cache_creation_input_tokens": 1108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1108
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-13T11:45:12.261Z_

<details><summary>↩ Tool result · `toolu_01KDy6WwcB9RfNfLN34kGmf2`</summary>

```text
Web search results for query: ""density ratio" weighted behavioral cloning VLA demonstration curation arxiv 2025"

Links: [{"title":"[2510.01479] Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets","url":"https://arxiv.org/abs/2510.01479"},{"title":"Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets","url":"https://arxiv.org/html/2510.01479v1"},{"title":"Density-Ratio Weighted Behavioral Cloning:","url":"https://arxiv.org/pdf/2510.01479"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/html/2509.25718"},{"title":"ADR-BC: Adversarial Density Weighted Regression Behavior Cloning","url":"https://arxiv.org/html/2405.20351v1"},{"title":"Behavioral Cloning via Search in Embedded Demonstration Dataset","url":"https://arxiv.org/html/2306.09082"},{"title":"[2604.23000] Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://arxiv.org/abs/2604.23000"},{"title":"Understanding Behavior Cloning with Action Quantization","url":"https://arxiv.org/pdf/2603.20538"},{"title":"VALUE-ALIGNED BEHAVIOR CLONING FOR OFFLINE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/17ab5964d90f38b174a068646c958789-Paper-Conference.pdf"},{"title":"Fine-tuning Behavioral Cloning Policies with Preference- ...","url":"https://arxiv.org/pdf/2509.26605"}]

Based on the search results, I found a directly relevant paper:

The paper "Density-Ratio Weighted Behavioral Cloning" introduces a robust imitation learning approach that uses a small, verified clean reference set to estimate trajectory-level density ratios via a binary discriminator. These ratios are clipped and used as weights in the BC approach.

The paper was posted on arXiv on October 1, 2025 (arxiv ID: 2510.01479) and focuses on learning control policies from corrupted datasets through weighted behavioral cloning.

However, I should note that while the search results contain papers on density-ratio weighted behavioral cloning and VLA model post-training, I didn't find a single paper that explicitly combines all the elements you mentioned (density ratio, weighted behavioral cloning, VLA, demonstration curation) in 2025. The paper 2510.01479 is about density-ratio weighted BC for learning from corrupted data, while other results discuss VLA models and demonstration curation separately.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61e07e6c-1fb9-4788-939c-fcb6563b8890",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "79a26a71-d757-4ebb-b382-acdbeafdba90",
  "toolUseResult": {
    "query": "\"density ratio\" weighted behavioral cloning VLA demonstration curation arxiv 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A8Ho5REMousEifg7TN3CSs",
        "content": [
          {
            "title": "[2510.01479] Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets",
            "url": "https://arxiv.org/abs/2510.01479"
          },
          {
            "title": "Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets",
            "url": "https://arxiv.org/html/2510.01479v1"
          },
          {
            "title": "Density-Ratio Weighted Behavioral Cloning:",
            "url": "https://arxiv.org/pdf/2510.01479"
          },
          {
            "title": "VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning",
            "url": "https://arxiv.org/html/2509.25718"
          },
          {
            "title": "ADR-BC: Adversarial Density Weighted Regression Behavior Cloning",
            "url": "https://arxiv.org/html/2405.20351v1"
          },
          {
            "title": "Behavioral Cloning via Search in Embedded Demonstration Dataset",
            "url": "https://arxiv.org/html/2306.09082"
          },
          {
            "title": "[2604.23000] Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning",
            "url": "https://arxiv.org/abs/2604.23000"
          },
          {
            "title": "Understanding Behavior Cloning with Action Quantization",
            "url": "https://arxiv.org/pdf/2603.20538"
          },
          {
            "title": "VALUE-ALIGNED BEHAVIOR CLONING FOR OFFLINE ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/17ab5964d90f38b174a068646c958789-Paper-Conference.pdf"
          },
          {
            "title": "Fine-tuning Behavioral Cloning Policies with Preference- ...",
            "url": "https://arxiv.org/pdf/2509.26605"
          }
        ]
      },
      "Based on the search results, I found a directly relevant paper:\n\nThe paper \"Density-Ratio Weighted Behavioral Cloning\" introduces a robust imitation learning approach that uses a small, verified clean reference set to estimate trajectory-level density ratios via a binary discriminator. These ratios are clipped and used as weights in the BC approach.\n\nThe paper was posted on arXiv on October 1, 2025 (arxiv ID: 2510.01479) and focuses on learning control policies from corrupted datasets through weighted behavioral cloning.\n\nHowever, I should note that while the search results contain papers on density-ratio weighted behavioral cloning and VLA model post-training, I didn't find a single paper that explicitly combines all the elements you mentioned (density ratio, weighted behavioral cloning, VLA, demonstration curation) in 2025. The paper 2510.01479 is about density-ratio weighted BC for learning from corrupted data, while other results discuss VLA models and demonstration curation separately."
    ],
    "durationSeconds": 5.424609813999966
  },
  "sourceToolAssistantUUID": "61e07e6c-1fb9-4788-939c-fcb6563b8890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-13T11:45:15.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HiFEJB4suoxNH3QXjVC5X8`</summary>

```json
{
  "query": "RINSE smoothness metrics data quality imitation learning ICML 2025 2604.23000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79a26a71-d757-4ebb-b382-acdbeafdba90",
  "isSidechain": false,
  "requestId": "req_011CazWc3SgMHLjacSzXL5JC",
  "type": "assistant",
  "uuid": "b12cd474-1194-437c-be06-2cdcfb6945a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JsvGcTKBRPLkPbBHDisLY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 67414,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 67414,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 101_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b12cd474-1194-437c-be06-2cdcfb6945a2",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 102_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool result

_source line 103 · 2026-05-13T11:45:24.310Z_

<details><summary>↩ Tool result · `toolu_01HiFEJB4suoxNH3QXjVC5X8`</summary>

```text
Web search results for query: "RINSE smoothness metrics data quality imitation learning ICML 2025 2604.23000"

Links: [{"title":"ICML Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://icml.cc/virtual/2025/48703"},{"title":"[2604.23000] Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://arxiv.org/abs/2604.23000"},{"title":"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning","url":"https://arxiv.org/html/2604.23000"},{"title":"GitHub - TobyLeelsz/iqmpc: Official code implementation of ICML 2025 paper: Reward-free World Models for Online Imitation Learning · GitHub","url":"https://github.com/TobyLeelsz/iqmpc"},{"title":"Data Quality in Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=FwmvbuDiMk&noteId=yRiDkOIoZK"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"ICML.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICML.2025"},{"title":"ICML 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/icml-statistics/icml-2025-statistics/"},{"title":"Submitted by Fabian Paischer Submitted at Institute for Machine Learning","url":"https://epub.jku.at/download/pdf/11285421.pdf"},{"title":"ICML Poster Reward-free World Models for Online Imitation Learning","url":"https://icml.cc/virtual/2025/poster/44035"}]

I found relevant information about your query. Here are the results:

## RINSE: Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning

RINSE (Ranking and INdexing Smooth Examples) is a lightweight framework for scoring demonstrations based on trajectory smoothness that is policy-architecture-agnostic and operates on trajectory data alone, with TED additionally using a phase-boundary/contact signal.

Grounded in motor control theory—which establishes smoothness as a hallmark of skilled movement—RINSE uses two complementary metrics: Spectral Arc Length (SAL), a spectral measure of frequency-domain regularity, and Trajectory-Envelope Distance (TED), a spatial measure of contact-aware geometric deviation.

### Key Results

RINSE enables more efficient and reliable policy learning from imperfect data by filtering demonstration data based on trajectory smoothness, unlike existing techniques that typically require extensive manual annotation or substantial computational cost. RINSE assigns dataset quality scores that correlate strongly with downstream performance and can be used to monitor the data collection process.

The empirical results are impressive:
- On RoboMimic benchmarks, SAL filtering achieves 16% higher success using one-sixth of the data.
- On real-world manipulation, TED filtering achieves 20% improvement with half the data.
- These results support smoothness as a useful quality signal across filtering, retrieval, and reweighting settings, especially in noisy or heterogeneous data regimes.

The paper (arXiv 2604.23000) appears to be accepted at ICML 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b12cd474-1194-437c-be06-2cdcfb6945a2",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "52006630-8ffd-4876-929d-44950813224f",
  "toolUseResult": {
    "query": "RINSE smoothness metrics data quality imitation learning ICML 2025 2604.23000",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Z2eL8oQMtLkydrihhAc5i",
        "content": [
          {
            "title": "ICML Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning",
            "url": "https://icml.cc/virtual/2025/48703"
          },
          {
            "title": "[2604.23000] Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning",
            "url": "https://arxiv.org/abs/2604.23000"
          },
          {
            "title": "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning",
            "url": "https://arxiv.org/html/2604.23000"
          },
          {
            "title": "GitHub - TobyLeelsz/iqmpc: Official code implementation of ICML 2025 paper: Reward-free World Models for Online Imitation Learning · GitHub",
            "url": "https://github.com/TobyLeelsz/iqmpc"
          },
          {
            "title": "Data Quality in Imitation Learning | OpenReview",
            "url": "https://openreview.net/forum?id=FwmvbuDiMk&noteId=yRiDkOIoZK"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "ICML.2025 | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/ICML.2025"
          },
          {
            "title": "ICML 2025 Statistics - Paper Copilot",
            "url": "https://papercopilot.com/statistics/icml-statistics/icml-2025-statistics/"
          },
          {
            "title": "Submitted by Fabian Paischer Submitted at Institute for Machine Learning",
            "url": "https://epub.jku.at/download/pdf/11285421.pdf"
          },
          {
            "title": "ICML Poster Reward-free World Models for Online Imitation Learning",
            "url": "https://icml.cc/virtual/2025/poster/44035"
          }
        ]
      },
      "I found relevant information about your query. Here are the results:\n\n## RINSE: Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning\n\nRINSE (Ranking and INdexing Smooth Examples) is a lightweight framework for scoring demonstrations based on trajectory smoothness that is policy-architecture-agnostic and operates on trajectory data alone, with TED additionally using a phase-boundary/contact signal.\n\nGrounded in motor control theory—which establishes smoothness as a hallmark of skilled movement—RINSE uses two complementary metrics: Spectral Arc Length (SAL), a spectral measure of frequency-domain regularity, and Trajectory-Envelope Distance (TED), a spatial measure of contact-aware geometric deviation.\n\n### Key Results\n\nRINSE enables more efficient and reliable policy learning from imperfect data by filtering demonstration data based on trajectory smoothness, unlike existing techniques that typically require extensive manual annotation or substantial computational cost. RINSE assigns dataset quality scores that correlate strongly with downstream performance and can be used to monitor the data collection process.\n\nThe empirical results are impressive:\n- On RoboMimic benchmarks, SAL filtering achieves 16% higher success using one-sixth of the data.\n- On real-world manipulation, TED filtering achieves 20% improvement with half the data.\n- These results support smoothness as a useful quality signal across filtering, retrieval, and reweighting settings, especially in noisy or heterogeneous data regimes.\n\nThe paper (arXiv 2604.23000) appears to be accepted at ICML 2025."
    ],
    "durationSeconds": 8.562719663999975
  },
  "sourceToolAssistantUUID": "b12cd474-1194-437c-be06-2cdcfb6945a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 104 · 2026-05-13T11:45:24.314Z_

```json
{
  "parentUuid": "52006630-8ffd-4876-929d-44950813224f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "95d1eb19-9756-4005-b5e7-c7ceb0c04912",
  "timestamp": "2026-05-13T11:45:24.314Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 105 · 2026-05-13T11:45:27.957Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C78yk8SFhx5MNySE9RPB5X`</summary>

```json
{
  "query": "CoRL 2026 abstract deadline May 25 or May 26 AoE UTC official"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95d1eb19-9756-4005-b5e7-c7ceb0c04912",
  "isSidechain": false,
  "requestId": "req_011CazWcvwnYMW1msqWasyNC",
  "type": "assistant",
  "uuid": "a2f7a02e-bc23-493e-b1c5-8aada8ab0ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xho74SMLajfEyKJ3QJQmGr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1056,
      "cache_read_input_tokens": 68200,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 68200,
          "cache_creation_input_tokens": 1056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1056
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-13T11:45:31.650Z_

<details><summary>↩ Tool result · `toolu_01C78yk8SFhx5MNySE9RPB5X`</summary>

```text
Web search results for query: "CoRL 2026 abstract deadline May 25 or May 26 AoE UTC official"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"}]

Based on the search results, I found information about the CoRL 2026 abstract deadline:

The abstract submission deadline for CoRL 2026 is May 26, 2026 at 11:59 UTC.

However, there's a discrepancy in one source: The CoRL 2026 official announcement lists May 25 as the abstract submission deadline.

The most recent and detailed source (from February 26, 2026) indicates May 26, 2026 11:59 UTC, which appears to be the official deadline. Both dates fall "Anywhere on Earth" (AoE) in UTC timezone as specified in the query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2f7a02e-bc23-493e-b1c5-8aada8ab0ba2",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "148e3b96-76ac-44af-a9c0-a6fe5619b78d",
  "toolUseResult": {
    "query": "CoRL 2026 abstract deadline May 25 or May 26 AoE UTC official",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XmhGESnz5KphYPPUTuFDBK",
        "content": [
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "Refactor conference data · huggingface/ai-deadlines at f3cc2d7",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "Vincent Vanhoucke's Post",
            "url": "https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"
          }
        ]
      },
      "Based on the search results, I found information about the CoRL 2026 abstract deadline:\n\nThe abstract submission deadline for CoRL 2026 is May 26, 2026 at 11:59 UTC.\n\nHowever, there's a discrepancy in one source: The CoRL 2026 official announcement lists May 25 as the abstract submission deadline.\n\nThe most recent and detailed source (from February 26, 2026) indicates May 26, 2026 11:59 UTC, which appears to be the official deadline. Both dates fall \"Anywhere on Earth\" (AoE) in UTC timezone as specified in the query."
    ],
    "durationSeconds": 3.687980350000027
  },
  "sourceToolAssistantUUID": "a2f7a02e-bc23-493e-b1c5-8aada8ab0ba2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-13T11:45:35.474Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011uUa5WyoYSPAGm1d35qHdy`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract the exact submission deadlines for CoRL 2026. What are the abstract deadline and paper deadline? Are dates in AoE or UTC? What timezone is specified?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "148e3b96-76ac-44af-a9c0-a6fe5619b78d",
  "isSidechain": false,
  "requestId": "req_011CazWdUP9RHcznSyAcf2wF",
  "type": "assistant",
  "uuid": "65f72f2c-8bc8-486e-a098-434fbb3473c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ng2ryN51cLjzUSnHDBEViM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 69256,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 69256,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 731
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-13T11:45:38.009Z_

<details><summary>↩ Tool result · `toolu_011uUa5WyoYSPAGm1d35qHdy`</summary>

```text
Based on the provided web page content, **I cannot extract the submission deadlines for CoRL 2026**. 

The page shown is the "Call for Papers" overview, which describes the conference scope and welcome topics. However, it does not contain specific deadline dates. The page only references: "For paper submission format and timeline, see: [Instruction for Authors](/contributions/instruction-for-authors)"

To find the abstract and paper deadlines, you would need to visit the "Instruction for Authors" page linked in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65f72f2c-8bc8-486e-a098-434fbb3473c8",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "ae3608fd-7360-4215-b29c-8927f8f0192d",
  "toolUseResult": {
    "bytes": 134133,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided web page content, **I cannot extract the submission deadlines for CoRL 2026**. \n\nThe page shown is the \"Call for Papers\" overview, which describes the conference scope and welcome topics. However, it does not contain specific deadline dates. The page only references: \"For paper submission format and timeline, see: [Instruction for Authors](/contributions/instruction-for-authors)\"\n\nTo find the abstract and paper deadlines, you would need to visit the \"Instruction for Authors\" page linked in the document.",
    "durationMs": 2531,
    "url": "https://www.corl.org/contributions/call-for-papers"
  },
  "sourceToolAssistantUUID": "65f72f2c-8bc8-486e-a098-434fbb3473c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-13T11:45:40.795Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E7WWMfDZhB8yGFETnkRFYe`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract the exact submission deadlines for CoRL 2026 including abstract deadline and paper deadline. What timezone is specified (AoE or UTC)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae3608fd-7360-4215-b29c-8927f8f0192d",
  "isSidechain": false,
  "requestId": "req_011CazWdwXYE3ZtxX7sZJNvJ",
  "type": "assistant",
  "uuid": "4a64f494-f9eb-4612-b7a8-b426259f1427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9wChYaA8tXTWz9tVAGGrm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 69987,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 69987,
          "cache_creation_input_tokens": 245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 245
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-13T11:45:43.984Z_

<details><summary>↩ Tool result · `toolu_01E7WWMfDZhB8yGFETnkRFYe`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the provided content, I cannot extract the exact submission deadlines for abstract and paper submissions. The page includes a "Key Dates" section header, but **the actual deadline dates are not displayed in the provided text**.

However, regarding timezone specification:

The document mentions **Anywhere on Earth (AoE)** timezone specifically for the camera-ready submission deadline: "The camera-ready version of your paper is due by Oct 12, 2026 (23:59 [Anywhere on Earth](https://www.timeanddate.com/time/zones/aoe))."

There is one reference to a paper deadline being "Thursday (5/28) EOD" but without the year or full context, and no abstract deadline date is visible in the extracted content.

To obtain the complete submission deadlines, you would need to access the full webpage or contact the organizers directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a64f494-f9eb-4612-b7a8-b426259f1427",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "56787108-1759-445d-ba2d-ba99593afd4c",
  "toolUseResult": {
    "bytes": 176667,
    "code": 200,
    "codeText": "OK",
    "result": "# CoRL 2026 Submission Deadlines\n\nBased on the provided content, I cannot extract the exact submission deadlines for abstract and paper submissions. The page includes a \"Key Dates\" section header, but **the actual deadline dates are not displayed in the provided text**.\n\nHowever, regarding timezone specification:\n\nThe document mentions **Anywhere on Earth (AoE)** timezone specifically for the camera-ready submission deadline: \"The camera-ready version of your paper is due by Oct 12, 2026 (23:59 [Anywhere on Earth](https://www.timeanddate.com/time/zones/aoe)).\"\n\nThere is one reference to a paper deadline being \"Thursday (5/28) EOD\" but without the year or full context, and no abstract deadline date is visible in the extracted content.\n\nTo obtain the complete submission deadlines, you would need to access the full webpage or contact the organizers directly.",
    "durationMs": 3185,
    "url": "https://www.corl.org/contributions/instruction-for-authors"
  },
  "sourceToolAssistantUUID": "4a64f494-f9eb-4612-b7a8-b426259f1427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-13T11:45:46.785Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Q4N36CtERsi7orFj4pxTf`</summary>

```json
{
  "query": "site:openreview.net CoRL 2026 abstract deadline submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56787108-1759-445d-ba2d-ba99593afd4c",
  "isSidechain": false,
  "requestId": "req_011CazWeP3CjE1Eg1HGLU9X7",
  "type": "assistant",
  "uuid": "b2163d9a-7391-47d1-aaff-0d78e5c62f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbkjapXVzWEQpPcavqCSis",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 329,
      "cache_read_input_tokens": 70232,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 70232,
          "cache_creation_input_tokens": 329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 329
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-13T11:45:51.373Z_

<details><summary>↩ Tool result · `toolu_013Q4N36CtERsi7orFj4pxTf`</summary>

```text
Web search results for query: "site:openreview.net CoRL 2026 abstract deadline submission deadline"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

Papers may be submitted through OpenReview via the link: https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference.

It's important to note that the deadlines are final, and no accommodations can be made for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2163d9a-7391-47d1-aaff-0d78e5c62f49",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "0195e476-aa9c-4572-8949-8f36c1ca5352",
  "toolUseResult": {
    "query": "site:openreview.net CoRL 2026 abstract deadline submission deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_015oApivw5pnoRLz4qyN71KL",
        "content": [
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "Refactor conference data · huggingface/ai-deadlines at f3cc2d7",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          }
        ]
      },
      "Based on the search results, here are the CoRL 2026 submission deadlines:\n\nThe abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.\n\nPapers may be submitted through OpenReview via the link: https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference.\n\nIt's important to note that the deadlines are final, and no accommodations can be made for missing the abstract deadline or paper deadline."
    ],
    "durationSeconds": 4.584006172999972
  },
  "sourceToolAssistantUUID": "b2163d9a-7391-47d1-aaff-0d78e5c62f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-13T11:45:54.564Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013oJuMUuB2cVg1FVUcz9evP`</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
  "prompt": "Extract the exact submission deadlines for CoRL 2026. What is the abstract deadline and paper deadline? What timezone (AoE or UTC)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0195e476-aa9c-4572-8949-8f36c1ca5352",
  "isSidechain": false,
  "requestId": "req_011CazWevczjsBfugALmvmfc",
  "type": "assistant",
  "uuid": "cc30158c-f8dc-4a6a-98cb-1c92164e00b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMwCfZJiYUeWFdp8my4qh3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 70561,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 70561,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-13T11:45:56.683Z_

<details><summary>↩ Tool result · `toolu_013oJuMUuB2cVg1FVUcz9evP`</summary>

```text
I cannot extract the submission deadlines for CoRL 2026 from the provided content. The web page excerpt contains only navigation elements, footer information, and general OpenReview platform details—it does not include any specific deadline dates, abstract submission times, paper submission times, or timezone information for the CoRL 2026 conference.

To find this information, you would need to visit the full CoRL 2026 conference page on OpenReview or check the conference's official website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc30158c-f8dc-4a6a-98cb-1c92164e00b7",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "8c91cb81-1a9e-40cd-bd3a-17f2eb202c12",
  "toolUseResult": {
    "bytes": 57999,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot extract the submission deadlines for CoRL 2026 from the provided content. The web page excerpt contains only navigation elements, footer information, and general OpenReview platform details—it does not include any specific deadline dates, abstract submission times, paper submission times, or timezone information for the CoRL 2026 conference.\n\nTo find this information, you would need to visit the full CoRL 2026 conference page on OpenReview or check the conference's official website.",
    "durationMs": 2114,
    "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
  },
  "sourceToolAssistantUUID": "cc30158c-f8dc-4a6a-98cb-1c92164e00b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 115 · 2026-05-13T11:46:00.441Z_

Let me verify the deadline from a reliable aggregator.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c91cb81-1a9e-40cd-bd3a-17f2eb202c12",
  "isSidechain": false,
  "requestId": "req_011CazWfKZsnMWmpXEUzQA6q",
  "type": "assistant",
  "uuid": "a4debb67-35f3-44ef-a300-7b4bd49d0e05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsnnnwVov7gtJveVdqjiAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 71233,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 71233,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-13T11:46:00.976Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U6tj7yk2P2DwTJNnT1fmKR`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "Extract the exact CoRL 2026 conference deadline dates. What are the abstract and paper submission deadlines? What timezone?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4debb67-35f3-44ef-a300-7b4bd49d0e05",
  "isSidechain": false,
  "requestId": "req_011CazWfKZsnMWmpXEUzQA6q",
  "type": "assistant",
  "uuid": "c333bc97-3e2a-4b10-961f-510728cd86d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsnnnwVov7gtJveVdqjiAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 71233,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 71233,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-13T11:46:03.248Z_

<details><summary>↩ Tool result · `toolu_01U6tj7yk2P2DwTJNnT1fmKR`</summary>

```text
# CoRL 2026 Conference Deadlines

Based on the update to the conference details, here are the exact submission deadlines for CoRL 2026:

## Submission Deadlines

| Deadline Type | Date | Time | Timezone |
|---|---|---|---|
| **Abstract Submission** | May 26, 2026 | 11:59 | UTC |
| **Paper Submission** | May 29, 2026 | 11:59 | UTC |

## Additional Conference Details

- **Conference Dates:** November 9-12, 2026
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701
- **Schedule:** 
  - Workshops: November 9
  - Main Conference: November 10-12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c333bc97-3e2a-4b10-961f-510728cd86d0",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "2f4d97e4-27d8-4595-be6f-1bb887651ec3",
  "toolUseResult": {
    "bytes": 60013,
    "code": 200,
    "codeText": "OK",
    "result": "# CoRL 2026 Conference Deadlines\n\nBased on the update to the conference details, here are the exact submission deadlines for CoRL 2026:\n\n## Submission Deadlines\n\n| Deadline Type | Date | Time | Timezone |\n|---|---|---|---|\n| **Abstract Submission** | May 26, 2026 | 11:59 | UTC |\n| **Paper Submission** | May 29, 2026 | 11:59 | UTC |\n\n## Additional Conference Details\n\n- **Conference Dates:** November 9-12, 2026\n- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701\n- **Schedule:** \n  - Workshops: November 9\n  - Main Conference: November 10-12",
    "durationMs": 2270,
    "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
  },
  "sourceToolAssistantUUID": "c333bc97-3e2a-4b10-961f-510728cd86d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 118_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2f4d97e4-27d8-4595-be6f-1bb887651ec3",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 119_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Assistant

_source line 120 · 2026-05-13T11:46:06.799Z_

Good — the proposal's dates (abstract May 26, paper May 29) are correct according to the latest data showing UTC timezone. Let me now search for a few more critical dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f4d97e4-27d8-4595-be6f-1bb887651ec3",
  "isSidechain": false,
  "requestId": "req_011CazWfoRRxnUGvJjkq6Rpd",
  "type": "assistant",
  "uuid": "02cf31f5-5eb3-4dc7-a01e-d32dd522fa43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbQrkMGz9uKzeRh56vNxdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 71477,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 71477,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 350
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-13T11:46:07.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WoZWCattDgnE9j6YKxh4oT`</summary>

```json
{
  "query": "\"when do curricula work\" ICLR 2021 curriculum learning marginal benefits clean data noise"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02cf31f5-5eb3-4dc7-a01e-d32dd522fa43",
  "isSidechain": false,
  "requestId": "req_011CazWfoRRxnUGvJjkq6Rpd",
  "type": "assistant",
  "uuid": "12edeb54-2fd6-4f7a-8020-5fc7cd91c1f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbQrkMGz9uKzeRh56vNxdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 71477,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 71477,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 350
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-13T11:46:13.136Z_

<details><summary>↩ Tool result · `toolu_01WoZWCattDgnE9j6YKxh4oT`</summary>

```text
Web search results for query: ""when do curricula work" ICLR 2021 curriculum learning marginal benefits clean data noise"

Links: [{"title":"Published as a conference paper at ICLR 2021 WHEN DO CURRICULA WORK?","url":"https://openreview.net/pdf?id=tW4QEInpni"},{"title":"When Do Curricula Work? | OpenReview","url":"https://openreview.net/forum?id=tW4QEInpni"},{"title":"[2012.03107] When Do Curricula Work?","url":"https://arxiv.org/abs/2012.03107"},{"title":"Iclr","url":"https://iclr.cc/virtual/2021/oral/3401"},{"title":"dblp: When Do Curricula Work?","url":"https://dblp.org/rec/conf/iclr/WuDN21.html"},{"title":"When Do Curricula Work? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201203107W/abstract"},{"title":"GitHub - google-research/understanding-curricula · GitHub","url":"https://github.com/google-research/understanding-curricula"},{"title":"When Do Curricula Work? · Papers I Read","url":"https://shagunsodhani.com/papers-I-read/When-Do-Curricula-Work"},{"title":"[2012.03107v3] When Do Curricula Work?","url":"https://arxiv.org/abs/2012.03107v3"},{"title":"When Do Curricula Work? - Papertalk","url":"https://papertalk.org/papertalks/29107"}]

I found the ICLR 2021 paper "When Do Curricula Work?" Here are the key findings:

## Overview

The paper, authored by Xiaoxia Wu, Ethan Dyer, and Behnam Neyshabur, investigates when curriculum learning—the practice of ordering training examples by difficulty—actually provides benefits.

## Key Findings

For standard benchmark datasets, curricula have only marginal benefits, and randomly ordered samples perform as well or better than curricula and anti-curricula, suggesting that any benefit is entirely due to the dynamic training set size.

## When Curricula Help

The paper identifies specific conditions where curriculum learning does provide benefits:

Curriculum, but not anti-curriculum or random ordering can indeed improve the performance either with limited training time budget or in the existence of noisy data.

More specifically, for training with a limited time budget (center) or with noisy data (right) curriculum learning can be beneficial.

## Methodology

The researchers conducted extensive experiments over thousands of orderings spanning three kinds of learning: curriculum, anti-curriculum, and random-curriculum—in which the size of the training dataset is dynamically increased over time, but the examples are randomly ordered.

The paper provides a nuanced view of curriculum learning, showing that while it doesn't help under standard training conditions with clean data and sufficient time, it becomes valuable under resource constraints or when dealing with noisy datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12edeb54-2fd6-4f7a-8020-5fc7cd91c1f9",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "be949cf5-b5b7-4a64-b0d2-df7104f50bc6",
  "toolUseResult": {
    "query": "\"when do curricula work\" ICLR 2021 curriculum learning marginal benefits clean data noise",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WzBCNLTXxibsq3voNF7NEm",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2021 WHEN DO CURRICULA WORK?",
            "url": "https://openreview.net/pdf?id=tW4QEInpni"
          },
          {
            "title": "When Do Curricula Work? | OpenReview",
            "url": "https://openreview.net/forum?id=tW4QEInpni"
          },
          {
            "title": "[2012.03107] When Do Curricula Work?",
            "url": "https://arxiv.org/abs/2012.03107"
          },
          {
            "title": "Iclr",
            "url": "https://iclr.cc/virtual/2021/oral/3401"
          },
          {
            "title": "dblp: When Do Curricula Work?",
            "url": "https://dblp.org/rec/conf/iclr/WuDN21.html"
          },
          {
            "title": "When Do Curricula Work? - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv201203107W/abstract"
          },
          {
            "title": "GitHub - google-research/understanding-curricula · GitHub",
            "url": "https://github.com/google-research/understanding-curricula"
          },
          {
            "title": "When Do Curricula Work? · Papers I Read",
            "url": "https://shagunsodhani.com/papers-I-read/When-Do-Curricula-Work"
          },
          {
            "title": "[2012.03107v3] When Do Curricula Work?",
            "url": "https://arxiv.org/abs/2012.03107v3"
          },
          {
            "title": "When Do Curricula Work? - Papertalk",
            "url": "https://papertalk.org/papertalks/29107"
          }
        ]
      },
      "I found the ICLR 2021 paper \"When Do Curricula Work?\" Here are the key findings:\n\n## Overview\n\nThe paper, authored by Xiaoxia Wu, Ethan Dyer, and Behnam Neyshabur, investigates when curriculum learning—the practice of ordering training examples by difficulty—actually provides benefits.\n\n## Key Findings\n\nFor standard benchmark datasets, curricula have only marginal benefits, and randomly ordered samples perform as well or better than curricula and anti-curricula, suggesting that any benefit is entirely due to the dynamic training set size.\n\n## When Curricula Help\n\nThe paper identifies specific conditions where curriculum learning does provide benefits:\n\nCurriculum, but not anti-curriculum or random ordering can indeed improve the performance either with limited training time budget or in the existence of noisy data.\n\nMore specifically, for training with a limited time budget (center) or with noisy data (right) curriculum learning can be beneficial.\n\n## Methodology\n\nThe researchers conducted extensive experiments over thousands of orderings spanning three kinds of learning: curriculum, anti-curriculum, and random-curriculum—in which the size of the training dataset is dynamically increased over time, but the examples are randomly ordered.\n\nThe paper provides a nuanced view of curriculum learning, showing that while it doesn't help under standard training conditions with clean data and sufficient time, it becomes valuable under resource constraints or when dealing with noisy datasets."
    ],
    "durationSeconds": 5.474786609000002
  },
  "sourceToolAssistantUUID": "12edeb54-2fd6-4f7a-8020-5fc7cd91c1f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-13T11:46:16.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BTqU4DTDVM3q5AxcwVfoLc`</summary>

```json
{
  "query": "prioritized experience replay imitation learning behavior cloning demonstration weighting online adaptive 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be949cf5-b5b7-4a64-b0d2-df7104f50bc6",
  "isSidechain": false,
  "requestId": "req_011CazWgXhucG1hfAT3u3hva",
  "type": "assistant",
  "uuid": "a764cf12-6e79-47b0-94d8-52095c53a42f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLZrwXeahz9N2utfYETfeH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 71827,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 71827,
          "cache_creation_input_tokens": 871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-13T11:46:24.672Z_

<details><summary>↩ Tool result · `toolu_01BTqU4DTDVM3q5AxcwVfoLc`</summary>

```text
Web search results for query: "prioritized experience replay imitation learning behavior cloning demonstration weighting online adaptive 2025 2026"

Links: [{"title":"(PDF) Integrating Behavior Cloning and Reinforcement Learning for Improved Performance in Dense and Sparse Reward Environments","url":"https://www.researchgate.net/publication/340492801_Integrating_Behavior_Cloning_and_Reinforcement_Learning_for_Improved_Performance_in_Dense_and_Sparse_Reward_Environments"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"},{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"(PDF) Prioritized Experience Replay","url":"https://www.researchgate.net/publication/284219262_Prioritized_Experience_Replay"},{"title":"Prioritized Experience Replay","url":"https://arxiv.org/pdf/1511.05952"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"Behavioral Cloning in Imitation Learning","url":"https://www.emergentmind.com/topics/behavioral-cloning-bc"},{"title":"Improved exploration–exploitation trade-off through adaptive prioritized experience replay - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231224016072"},{"title":"Uncertainty Prioritized Experience Replay","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_45.pdf"},{"title":"Reliability-Adjusted Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=hmQk2Iwdh0"}]

Based on the search results, I found several relevant papers and research addressing the intersection of prioritized experience replay, imitation learning, behavior cloning, and adaptive online learning from 2025-2026:

## Recent Developments (2025-2026)

**Behavior Cloning with Adaptive Methods:**
Conditioning policies on desired outcomes (return-to-go, goals) enables generalist agents and controlled extrapolation but requires careful trajectory weighting and regularization to avoid OOD collapse (2025).

**Advanced Experience Replay Techniques:**

A novel prioritizing technique called Bellman Error and TD trade-off Q-network (BETDQNet) adjusts sampling probabilities using an adaptively weighted score function that simultaneously augments two criteria: the Bellman error (BE) and TD error (2024-2025).

Reliability-adjusted Prioritized Experience Replay (ReaPER) extends PER by introducing a novel measure of temporal difference error reliability and theoretically enables more efficient learning than PER (2025).

**Outcome-Weighted Demonstration Replay:**

BReA-VLA pairs lightweight low-rank adapters with an Outcome-Conditioned Replay (OCR) procedure that samples replay batches with outcome-asymmetric weighting, treating failed demonstrations as repulsive anchors and successful demonstrations as attractive anchors.

ChronoBank-VLA is a time-indexed embedding archive that supports outcome-weighted retrieval whose weighting kernel is itself a function of trajectory age and recent failure density.

**Uncertainty-Based Prioritization:**
Epistemic uncertainty, the uncertainty reducible through learning, is the key quantity of interest and can be appropriately calibrated by dividing the epistemic uncertainty estimate by an aleatoric uncertainty estimate (information gain) (2025).

These approaches collectively address online adaptive learning with demonstration weighting and prioritized sampling across imitation learning and reinforcement learning domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a764cf12-6e79-47b0-94d8-52095c53a42f",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "ce2cae4f-aeb9-4194-bdb1-387ca5ef29c5",
  "toolUseResult": {
    "query": "prioritized experience replay imitation learning behavior cloning demonstration weighting online adaptive 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GKcqfxrVoH2yh1SwpqhZ2f",
        "content": [
          {
            "title": "(PDF) Integrating Behavior Cloning and Reinforcement Learning for Improved Performance in Dense and Sparse Reward Environments",
            "url": "https://www.researchgate.net/publication/340492801_Integrating_Behavior_Cloning_and_Reinforcement_Learning_for_Improved_Performance_in_Dense_and_Sparse_Reward_Environments"
          },
          {
            "title": "Prioritized Experience Replay | Request PDF",
            "url": "https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"
          },
          {
            "title": "[1511.05952] Prioritized Experience Replay",
            "url": "https://arxiv.org/abs/1511.05952"
          },
          {
            "title": "(PDF) Prioritized Experience Replay",
            "url": "https://www.researchgate.net/publication/284219262_Prioritized_Experience_Replay"
          },
          {
            "title": "Prioritized Experience Replay",
            "url": "https://arxiv.org/pdf/1511.05952"
          },
          {
            "title": "GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub",
            "url": "https://github.com/yingchengyang/Reinforcement-Learning-Papers"
          },
          {
            "title": "Behavioral Cloning in Imitation Learning",
            "url": "https://www.emergentmind.com/topics/behavioral-cloning-bc"
          },
          {
            "title": "Improved exploration–exploitation trade-off through adaptive prioritized experience replay - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0925231224016072"
          },
          {
            "title": "Uncertainty Prioritized Experience Replay",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_45.pdf"
          },
          {
            "title": "Reliability-Adjusted Prioritized Experience Replay | OpenReview",
            "url": "https://openreview.net/forum?id=hmQk2Iwdh0"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and research addressing the intersection of prioritized experience replay, imitation learning, behavior cloning, and adaptive online learning from 2025-2026:\n\n## Recent Developments (2025-2026)\n\n**Behavior Cloning with Adaptive Methods:**\nConditioning policies on desired outcomes (return-to-go, goals) enables generalist agents and controlled extrapolation but requires careful trajectory weighting and regularization to avoid OOD collapse (2025).\n\n**Advanced Experience Replay Techniques:**\n\nA novel prioritizing technique called Bellman Error and TD trade-off Q-network (BETDQNet) adjusts sampling probabilities using an adaptively weighted score function that simultaneously augments two criteria: the Bellman error (BE) and TD error (2024-2025).\n\nReliability-adjusted Prioritized Experience Replay (ReaPER) extends PER by introducing a novel measure of temporal difference error reliability and theoretically enables more efficient learning than PER (2025).\n\n**Outcome-Weighted Demonstration Replay:**\n\nBReA-VLA pairs lightweight low-rank adapters with an Outcome-Conditioned Replay (OCR) procedure that samples replay batches with outcome-asymmetric weighting, treating failed demonstrations as repulsive anchors and successful demonstrations as attractive anchors.\n\nChronoBank-VLA is a time-indexed embedding archive that supports outcome-weighted retrieval whose weighting kernel is itself a function of trajectory age and recent failure density.\n\n**Uncertainty-Based Prioritization:**\nEpistemic uncertainty, the uncertainty reducible through learning, is the key quantity of interest and can be appropriately calibrated by dividing the epistemic uncertainty estimate by an aleatoric uncertainty estimate (information gain) (2025).\n\nThese approaches collectively address online adaptive learning with demonstration weighting and prioritized sampling across imitation learning and reinforcement learning domains."
    ],
    "durationSeconds": 7.981020740000007
  },
  "sourceToolAssistantUUID": "a764cf12-6e79-47b0-94d8-52095c53a42f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 125 · 2026-05-13T11:46:24.674Z_

```json
{
  "parentUuid": "ce2cae4f-aeb9-4194-bdb1-387ca5ef29c5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "97236bc5-7e25-4e7a-9f46-896dba05e194",
  "timestamp": "2026-05-13T11:46:24.674Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 126 · 2026-05-13T11:46:27.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jsc7gZYFeTykrygysU1uQQ`</summary>

```json
{
  "query": "VACO \"value-aligned behavior cloning\" ICLR 2025 demonstration weighting meta-scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97236bc5-7e25-4e7a-9f46-896dba05e194",
  "isSidechain": false,
  "requestId": "req_011CazWhP1Z9UmnbmCzeY7G1",
  "type": "assistant",
  "uuid": "c17928b8-7c05-4b75-bb9d-1d8526e5ba82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121JWqATRHDNm7gwqWBfj7m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 72698,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 72698,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1134
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-13T11:46:35.070Z_

<details><summary>↩ Tool result · `toolu_01Jsc7gZYFeTykrygysU1uQQ`</summary>

```text
Web search results for query: "VACO "value-aligned behavior cloning" ICLR 2025 demonstration weighting meta-scoring"

Links: [{"title":"Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/17ab5964d90f38b174a068646c958789-Abstract-Conference.html"},{"title":"Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization | OpenReview","url":"https://openreview.net/forum?id=elTJBP7Fbv"},{"title":"ICLR Poster Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization","url":"https://iclr.cc/virtual/2025/poster/28908"},{"title":"Value-aligned Behavior Cloning for Offline Reinforcement ...","url":"https://iclr.cc/media/iclr-2025/Slides/28908.pdf"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.12638"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/130333a7b4a79fe39fe5a69106eba20f113c93df.pdf"}]

Based on the search results, I found comprehensive information about VACO. Here's what the research describes:

## Overview

VACO (Value-aligned Behavior Cloning via Bi-level Optimization) is a novel bi-level framework that integrates an inner loop for weighted supervised behavior cloning with an outer loop dedicated to value alignment. The paper was part of the International Conference on Representation Learning 2025 (ICLR 2025).

## Key Components

In this framework, the inner loop employs a meta-scoring network to evaluate and appropriately weight each training sample, while the outer loop maximizes value estimation for alignment with controlled noise to facilitate limited exploration.

## How It Works

The bi-level structure allows VACO to identify the optimal weighted BC policy, ultimately maximizing the expected estimated return conditioned on the learned value function. The learned meta-weights effectively reflect the quality of the data: higher meta-weights are associated with state-action pairs more likely generated by "expert" (good) policies, while lower meta-weights correspond to those generated by "random" (bad) policies.

## Problem Addressed

Although BC inherently avoids out-of-distribution deviations, it lacks the ability to discern between high and low-quality data, potentially leading to sub-optimal performance when facing with poor-quality data. Current offline RL algorithms attempt to enhance BC by incorporating value estimation, yet often struggle to effectively balance these two critical components.

## Performance

VACO achieves superior performance compared to existing state-of-the-art methods when evaluated across a variety of continuous control benchmarks in offline RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c17928b8-7c05-4b75-bb9d-1d8526e5ba82",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "61babe26-0008-4ac0-a0dc-544a6122be5d",
  "toolUseResult": {
    "query": "VACO \"value-aligned behavior cloning\" ICLR 2025 demonstration weighting meta-scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C8b4bAf2sQ6X19oJDMYjZP",
        "content": [
          {
            "title": "Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/17ab5964d90f38b174a068646c958789-Abstract-Conference.html"
          },
          {
            "title": "Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=elTJBP7Fbv"
          },
          {
            "title": "ICLR Poster Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization",
            "url": "https://iclr.cc/virtual/2025/poster/28908"
          },
          {
            "title": "Value-aligned Behavior Cloning for Offline Reinforcement ...",
            "url": "https://iclr.cc/media/iclr-2025/Slides/28908.pdf"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Publications | Chenjia Bai",
            "url": "http://baichenjia.cn/publication/"
          },
          {
            "title": "ICLR 2025 Schedule",
            "url": "https://iclr.cc/virtual/2025/calendar"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2510.12638"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/130333a7b4a79fe39fe5a69106eba20f113c93df.pdf"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about VACO. Here's what the research describes:\n\n## Overview\n\nVACO (Value-aligned Behavior Cloning via Bi-level Optimization) is a novel bi-level framework that integrates an inner loop for weighted supervised behavior cloning with an outer loop dedicated to value alignment. The paper was part of the International Conference on Representation Learning 2025 (ICLR 2025).\n\n## Key Components\n\nIn this framework, the inner loop employs a meta-scoring network to evaluate and appropriately weight each training sample, while the outer loop maximizes value estimation for alignment with controlled noise to facilitate limited exploration.\n\n## How It Works\n\nThe bi-level structure allows VACO to identify the optimal weighted BC policy, ultimately maximizing the expected estimated return conditioned on the learned value function. The learned meta-weights effectively reflect the quality of the data: higher meta-weights are associated with state-action pairs more likely generated by \"expert\" (good) policies, while lower meta-weights correspond to those generated by \"random\" (bad) policies.\n\n## Problem Addressed\n\nAlthough BC inherently avoids out-of-distribution deviations, it lacks the ability to discern between high and low-quality data, potentially leading to sub-optimal performance when facing with poor-quality data. Current offline RL algorithms attempt to enhance BC by incorporating value estimation, yet often struggle to effectively balance these two critical components.\n\n## Performance\n\nVACO achieves superior performance compared to existing state-of-the-art methods when evaluated across a variety of continuous control benchmarks in offline RL."
    ],
    "durationSeconds": 7.424925701999979
  },
  "sourceToolAssistantUUID": "c17928b8-7c05-4b75-bb9d-1d8526e5ba82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 128 · 2026-05-13T11:46:41.717Z_

Now let me look for one more critical angle — whether the SFT→RL cascade finding has been studied recently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61babe26-0008-4ac0-a0dc-544a6122be5d",
  "isSidechain": false,
  "requestId": "req_011CazWi9VjFB9o5pYJtwC37",
  "type": "assistant",
  "uuid": "406d544d-a93b-4536-9cd7-9b9665172c7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gR6njsgCKieq4n4mgV7ns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 73832,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 73832,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 924
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-13T11:46:42.039Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NdwPBnLd6d6xG2XD2bVZnA`</summary>

```json
{
  "query": "\"SFT quality\" cascades \"RL\" downstream convergence \"data filtering\" \"warm start\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "406d544d-a93b-4536-9cd7-9b9665172c7e",
  "isSidechain": false,
  "requestId": "req_011CazWi9VjFB9o5pYJtwC37",
  "type": "assistant",
  "uuid": "764d7e6d-c1e8-48a3-a8be-88a3a86b8cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gR6njsgCKieq4n4mgV7ns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 73832,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 73832,
          "cache_creation_input_tokens": 924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 924
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-13T11:46:50.639Z_

<details><summary>↩ Tool result · `toolu_01NdwPBnLd6d6xG2XD2bVZnA`</summary>

```text
Web search results for query: ""SFT quality" cascades "RL" downstream convergence "data filtering" "warm start" 2026"

Links: [{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=SFT"},{"title":"Curating High-Quality SFT Datasets","url":"https://apxml.com/courses/rlhf-reinforcement-learning-human-feedback/chapter-2-sft-phase-rlhf/sft-dataset-curation"},{"title":"A Data Story of the GLM Model Family: From GLM (2021) to GLM-5 (2026)","url":"https://kili-technology.com/blog/data-story-glm-model-family"},{"title":"SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models","url":"https://arxiv.org/html/2504.11468"},{"title":"How to Train Your LLM Web Agent: A Statistical Diagnosis","url":"https://openreview.net/pdf?id=6v4fYh1m1c"},{"title":"Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training","url":"https://arxiv.org/html/2602.10815v1"},{"title":"[2601.07224] Consolidation or Adaptation? PRISM: Disentangling SFT and RL Data via Gradient Concentration","url":"https://arxiv.org/abs/2601.07224"},{"title":"Sequential SFT-then-RL Pipeline","url":"https://www.emergentmind.com/topics/sequential-sft-then-rl-pipeline"},{"title":"Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning","url":"https://arxiv.org/html/2509.06948v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2508.11408"}]

I found relevant research on the interconnected topics of SFT quality, RL training, convergence, data filtering, and warm-start initialization. Here are the key findings:

## SFT Quality Cascading to RL Performance

Research shows that SFT-stage methods that better prepare models for RL represent an effective step toward more holistic LLM post-training by designing and evaluating SFT with downstream RL in mind rather than in isolation. The effort invested in curating a high-quality SFT dataset pays dividends throughout the RLHF process, with a well-initialized model providing a stronger foundation for reward modeling and requiring less drastic policy updates during RL fine-tuning.

## Data Filtering and Quality Dimensions

Contemporary approaches treat alignment as a sequence of dataset factories—SFT datasets, verifiable RL environments, and filtering rules—running inside an asynchronous RL system. SFT corpora are categorized into General Chat, Reasoning, and Coding & Agent components, with reasoning data emphasizing verifiability through rejection sampling from verifiable problems and difficulty filtering around tasks earlier models fail on.

## Convergence Dynamics and Warm Start

While SFT provides effective initialization and rapid early convergence for cold-start training, it contributes little to final convergence performance, with SFT facilitating rapid initial learning while RL enables better asymptotic performance. Hybrid runs that branch off from SFT checkpoints to continue training with RL push the Pareto frontier, achieving higher success rates for the same compute.

## Recent 2026 Frameworks

The sequential SFT-then-RL pipeline has solidified as the community's default post-training protocol, with empirical studies such as the "Plasticity-Ceiling Framework" providing explicit scaling law guidance and checkpointing rules to maximize task ceiling while preserving update plasticity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "764d7e6d-c1e8-48a3-a8be-88a3a86b8cbb",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "0be58827-e06a-4bb9-b63b-31cb6d182101",
  "toolUseResult": {
    "query": "\"SFT quality\" cascades \"RL\" downstream convergence \"data filtering\" \"warm start\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WbHSonSPS57BaTfPijWGVx",
        "content": [
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=SFT"
          },
          {
            "title": "Curating High-Quality SFT Datasets",
            "url": "https://apxml.com/courses/rlhf-reinforcement-learning-human-feedback/chapter-2-sft-phase-rlhf/sft-dataset-curation"
          },
          {
            "title": "A Data Story of the GLM Model Family: From GLM (2021) to GLM-5 (2026)",
            "url": "https://kili-technology.com/blog/data-story-glm-model-family"
          },
          {
            "title": "SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models",
            "url": "https://arxiv.org/html/2504.11468"
          },
          {
            "title": "How to Train Your LLM Web Agent: A Statistical Diagnosis",
            "url": "https://openreview.net/pdf?id=6v4fYh1m1c"
          },
          {
            "title": "Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training",
            "url": "https://arxiv.org/html/2602.10815v1"
          },
          {
            "title": "[2601.07224] Consolidation or Adaptation? PRISM: Disentangling SFT and RL Data via Gradient Concentration",
            "url": "https://arxiv.org/abs/2601.07224"
          },
          {
            "title": "Sequential SFT-then-RL Pipeline",
            "url": "https://www.emergentmind.com/topics/sequential-sft-then-rl-pipeline"
          },
          {
            "title": "Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning",
            "url": "https://arxiv.org/html/2509.06948v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2508.11408"
          }
        ]
      },
      "I found relevant research on the interconnected topics of SFT quality, RL training, convergence, data filtering, and warm-start initialization. Here are the key findings:\n\n## SFT Quality Cascading to RL Performance\n\nResearch shows that SFT-stage methods that better prepare models for RL represent an effective step toward more holistic LLM post-training by designing and evaluating SFT with downstream RL in mind rather than in isolation. The effort invested in curating a high-quality SFT dataset pays dividends throughout the RLHF process, with a well-initialized model providing a stronger foundation for reward modeling and requiring less drastic policy updates during RL fine-tuning.\n\n## Data Filtering and Quality Dimensions\n\nContemporary approaches treat alignment as a sequence of dataset factories—SFT datasets, verifiable RL environments, and filtering rules—running inside an asynchronous RL system. SFT corpora are categorized into General Chat, Reasoning, and Coding & Agent components, with reasoning data emphasizing verifiability through rejection sampling from verifiable problems and difficulty filtering around tasks earlier models fail on.\n\n## Convergence Dynamics and Warm Start\n\nWhile SFT provides effective initialization and rapid early convergence for cold-start training, it contributes little to final convergence performance, with SFT facilitating rapid initial learning while RL enables better asymptotic performance. Hybrid runs that branch off from SFT checkpoints to continue training with RL push the Pareto frontier, achieving higher success rates for the same compute.\n\n## Recent 2026 Frameworks\n\nThe sequential SFT-then-RL pipeline has solidified as the community's default post-training protocol, with empirical studies such as the \"Plasticity-Ceiling Framework\" providing explicit scaling law guidance and checkpointing rules to maximize task ceiling while preserving update plasticity."
    ],
    "durationSeconds": 8.594419642000052
  },
  "sourceToolAssistantUUID": "764d7e6d-c1e8-48a3-a8be-88a3a86b8cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 131_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0be58827-e06a-4bb9-b63b-31cb6d182101",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 132_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool call

_source line 133 · 2026-05-13T11:46:53.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RWW34V6iWhVm9AFUWgMgoD`</summary>

```json
{
  "query": "\"Why Does RL Generalize Better Than SFT\" data-centric VLM post-training 2602.10815"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be58827-e06a-4bb9-b63b-31cb6d182101",
  "isSidechain": false,
  "requestId": "req_011CazWjJ8RB42fFn57VfUgJ",
  "type": "assistant",
  "uuid": "f0b44e96-4510-4ce8-acf4-0a8230cd87b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hEjtN6VpZKsp9ZsUkarWi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 74756,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 74756,
          "cache_creation_input_tokens": 1045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1045
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-13T11:46:59.311Z_

<details><summary>↩ Tool result · `toolu_01RWW34V6iWhVm9AFUWgMgoD`</summary>

```text
Web search results for query: ""Why Does RL Generalize Better Than SFT" data-centric VLM post-training 2602.10815"

Links: [{"title":"[2602.10815] Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training","url":"https://arxiv.org/abs/2602.10815"},{"title":"Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training","url":"https://arxiv.org/html/2602.10815v1"},{"title":"Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training - Takara TLDR | Takara TLDR","url":"https://tldr.takara.ai/p/2602.10815"},{"title":"Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on","url":"https://arxiv.org/pdf/2602.10815"},{"title":"[Literature Review] Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training","url":"https://www.themoonlight.io/en/review/why-does-rl-generalize-better-than-sft-a-data-centric-perspective-on-vlm-post-training"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://arxiv.org/html/2501.17161v1"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training | OpenReview","url":"https://openreview.net/forum?id=dYur3yabMj"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundationa Model Post-training","url":"https://arxiv.org/html/2501.17161"},{"title":"GitHub - byyx666/DC-SFT: This is official code implementation of the &lt;Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training>","url":"https://github.com/byyx666/DC-SFT"},{"title":"[2501.17161] SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://arxiv.org/abs/2501.17161"}]

I found the research paper you were looking for. Here's a summary of the key findings from arXiv paper 2602.10815:

## Paper Overview

The adaptation of large-scale Vision-Language Models (VLMs) through post-training reveals a pronounced generalization gap: models fine-tuned with Reinforcement Learning (RL) consistently achieve superior out-of-distribution (OOD) performance compared to those trained with Supervised Fine-Tuning (SFT).

## Main Explanation

The paper posits a data-centric explanation for this phenomenon, contending that RL's generalization advantage arises from an implicit data filtering mechanism that inherently prioritizes medium-difficulty training samples.

## Key Findings

Training on hard samples significantly degrades OOD performance. To test this hypothesis, the authors introduce Difficulty-Curated SFT (DC-SFT), a straightforward method that explicitly filters the training set based on sample difficulty.

## Results

Experiments show that DC-SFT not only substantially enhances OOD generalization over standard SFT, but also surpasses the performance of RL-based training, all while providing greater stability and computational efficiency.

The paper provides both theoretical insight and a practical method for improving VLM generalization by focusing on the difficulty distribution of training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0b44e96-4510-4ce8-acf4-0a8230cd87b0",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "93ba23ff-70bc-4aef-9377-413b1a452610",
  "toolUseResult": {
    "query": "\"Why Does RL Generalize Better Than SFT\" data-centric VLM post-training 2602.10815",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EBJSHejofQSUdacw3VCn4C",
        "content": [
          {
            "title": "[2602.10815] Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training",
            "url": "https://arxiv.org/abs/2602.10815"
          },
          {
            "title": "Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training",
            "url": "https://arxiv.org/html/2602.10815v1"
          },
          {
            "title": "Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training - Takara TLDR | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2602.10815"
          },
          {
            "title": "Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on",
            "url": "https://arxiv.org/pdf/2602.10815"
          },
          {
            "title": "[Literature Review] Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training",
            "url": "https://www.themoonlight.io/en/review/why-does-rl-generalize-better-than-sft-a-data-centric-perspective-on-vlm-post-training"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://arxiv.org/html/2501.17161v1"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training | OpenReview",
            "url": "https://openreview.net/forum?id=dYur3yabMj"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundationa Model Post-training",
            "url": "https://arxiv.org/html/2501.17161"
          },
          {
            "title": "GitHub - byyx666/DC-SFT: This is official code implementation of the &lt;Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training>",
            "url": "https://github.com/byyx666/DC-SFT"
          },
          {
            "title": "[2501.17161] SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://arxiv.org/abs/2501.17161"
          }
        ]
      },
      "I found the research paper you were looking for. Here's a summary of the key findings from arXiv paper 2602.10815:\n\n## Paper Overview\n\nThe adaptation of large-scale Vision-Language Models (VLMs) through post-training reveals a pronounced generalization gap: models fine-tuned with Reinforcement Learning (RL) consistently achieve superior out-of-distribution (OOD) performance compared to those trained with Supervised Fine-Tuning (SFT).\n\n## Main Explanation\n\nThe paper posits a data-centric explanation for this phenomenon, contending that RL's generalization advantage arises from an implicit data filtering mechanism that inherently prioritizes medium-difficulty training samples.\n\n## Key Findings\n\nTraining on hard samples significantly degrades OOD performance. To test this hypothesis, the authors introduce Difficulty-Curated SFT (DC-SFT), a straightforward method that explicitly filters the training set based on sample difficulty.\n\n## Results\n\nExperiments show that DC-SFT not only substantially enhances OOD generalization over standard SFT, but also surpasses the performance of RL-based training, all while providing greater stability and computational efficiency.\n\nThe paper provides both theoretical insight and a practical method for improving VLM generalization by focusing on the difficulty distribution of training data."
    ],
    "durationSeconds": 5.833558238000027
  },
  "sourceToolAssistantUUID": "f0b44e96-4510-4ce8-acf4-0a8230cd87b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 135 · 2026-05-13T11:47:03.985Z_

This is a very important find — "Why Does RL Generalize Better Than SFT?" (2602.10815) directly argues that **RL's advantage comes from implicit data filtering of medium-difficulty samples**, and DC-SFT explicitly filters by difficulty to surpass RL. This is extremely close to RAPID's premise. Let me investigate more deeply.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93ba23ff-70bc-4aef-9377-413b1a452610",
  "isSidechain": false,
  "requestId": "req_011CazWjwBcofr4UnnDU6EaK",
  "type": "assistant",
  "uuid": "549d6c36-3d99-4c10-aab0-f2eaf762d07a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HW2d9LKmprFC36ALoTNGPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 75801,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 75801,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-13T11:47:07.081Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0145cG2T16y3uf5Vu1b4JtEm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.10815",
  "prompt": "Extract: 1) Full abstract 2) Authors and affiliations 3) Submission date and venue status 4) How exactly does DC-SFT work? What is the data filtering mechanism? 5) Does it use loss-based filtering, difficulty scoring, or something else? 6) Is it applied to VLA/robot tasks or just VLM reasoning? 7) How does it relate to reducible loss or EMA-based methods? 8) What are the key baselines and results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "549d6c36-3d99-4c10-aab0-f2eaf762d07a",
  "isSidechain": false,
  "requestId": "req_011CazWjwBcofr4UnnDU6EaK",
  "type": "assistant",
  "uuid": "74815833-b720-4fba-81f4-99fe5d64335d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HW2d9LKmprFC36ALoTNGPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 75801,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 75801,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-13T11:47:12.874Z_

<details><summary>↩ Tool result · `toolu_0145cG2T16y3uf5Vu1b4JtEm`</summary>

```text
# Analysis of arXiv:2602.10815

## 1) Full Abstract
The paper examines why Reinforcement Learning outperforms Supervised Fine-Tuning in Vision-Language Models. It proposes that RL's advantage stems from implicit data filtering favoring medium-difficulty samples. The authors introduce Difficulty-Curated SFT (DC-SFT), which explicitly filters training data by difficulty, achieving superior out-of-distribution performance compared to standard SFT and RL approaches.

## 2) Authors and Affiliations
The paper lists four authors: Aojun Lu, Tao Feng, Hangjie Yuan, Wei Li, and Yanan Sun. However, specific institutional affiliations are not provided in the accessible webpage content.

## 3) Submission Date and Venue Status
Submitted February 11, 2026 to arXiv as a Computer Science paper (categories: Computer Vision and Pattern Recognition and Machine Learning). This is a preprint with no journal publication status indicated.

## 4-5) DC-SFT Mechanism and Filtering Approach
The webpage provides only high-level description: the method "explicitly filters the training set based on sample difficulty." The specific technical implementation details—whether loss-based, difficulty scoring algorithms, or other mechanisms—are not detailed in this abstract or metadata.

## 6) Application Scope
The research focuses on Vision-Language Models (VLMs) specifically, not VLA/robot tasks or general reasoning domains.

## 7) Related Methods
No mention of reducible loss or EMA-based methods appears in the available content.

## 8) Key Results
DC-SFT reportedly "substantially enhances OOD generalization over standard SFT" while "surpass[ing] the performance of RL-based training" with "greater stability and computational efficiency."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74815833-b720-4fba-81f4-99fe5d64335d",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "e2421b86-103d-473f-aac2-dfb8fe400d9b",
  "toolUseResult": {
    "bytes": 47109,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2602.10815\n\n## 1) Full Abstract\nThe paper examines why Reinforcement Learning outperforms Supervised Fine-Tuning in Vision-Language Models. It proposes that RL's advantage stems from implicit data filtering favoring medium-difficulty samples. The authors introduce Difficulty-Curated SFT (DC-SFT), which explicitly filters training data by difficulty, achieving superior out-of-distribution performance compared to standard SFT and RL approaches.\n\n## 2) Authors and Affiliations\nThe paper lists four authors: Aojun Lu, Tao Feng, Hangjie Yuan, Wei Li, and Yanan Sun. However, specific institutional affiliations are not provided in the accessible webpage content.\n\n## 3) Submission Date and Venue Status\nSubmitted February 11, 2026 to arXiv as a Computer Science paper (categories: Computer Vision and Pattern Recognition and Machine Learning). This is a preprint with no journal publication status indicated.\n\n## 4-5) DC-SFT Mechanism and Filtering Approach\nThe webpage provides only high-level description: the method \"explicitly filters the training set based on sample difficulty.\" The specific technical implementation details—whether loss-based, difficulty scoring algorithms, or other mechanisms—are not detailed in this abstract or metadata.\n\n## 6) Application Scope\nThe research focuses on Vision-Language Models (VLMs) specifically, not VLA/robot tasks or general reasoning domains.\n\n## 7) Related Methods\nNo mention of reducible loss or EMA-based methods appears in the available content.\n\n## 8) Key Results\nDC-SFT reportedly \"substantially enhances OOD generalization over standard SFT\" while \"surpass[ing] the performance of RL-based training\" with \"greater stability and computational efficiency.\"",
    "durationMs": 5789,
    "url": "https://arxiv.org/abs/2602.10815"
  },
  "sourceToolAssistantUUID": "74815833-b720-4fba-81f4-99fe5d64335d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-13T11:47:18.614Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Urbx3i9DXoC6s8HooATTZU`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.10815v1",
  "prompt": "I need to understand the technical details of DC-SFT: 1) How exactly is sample difficulty defined/measured? Is it based on model loss, a reference model, or something else? 2) What is the filtering mechanism - threshold-based, top-k, or percentile? 3) Is it a static one-time filter or dynamic/online during training? 4) Does it use any EMA or reducible loss concept? 5) What VLM tasks are tested (reasoning, visual QA, etc.)? 6) What are the key quantitative results? 7) How does it relate to the RAPID-like idea of filtering noisy/hard samples during SFT?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2421b86-103d-473f-aac2-dfb8fe400d9b",
  "isSidechain": false,
  "requestId": "req_011CazWkw6SYWnxPZqABNX9i",
  "type": "assistant",
  "uuid": "6ea3e8e1-c2f0-4260-8b1d-0c63d3719fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4x2SRvUStN5ZZM6wjkfvK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 76821,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 76821,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 693
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-13T11:47:26.128Z_

<details><summary>↩ Tool result · `toolu_01Urbx3i9DXoC6s8HooATTZU`</summary>

```text
# DC-SFT Technical Analysis

## 1) Sample Difficulty Definition
Difficulty is determined by model response correctness across multiple generations. The paper categorizes samples as:
- **Easy**: "all G responses are correct" (G=8 samples generated)
- **Hard**: "all G responses are incorrect"
- **Medium-difficulty**: "responses contain a mixture of correct and incorrect answers"

## 2) Filtering Mechanism
The approach uses **categorical filtering** rather than threshold-based or top-k methods. Samples are partitioned into discrete difficulty subsets, then the hard subset is excluded entirely. The paper notes: "we conduct SFT separately on each subset" and uses "batch sizes of 16 for SFT and 128 for GRPO."

## 3) Static vs. Dynamic
The filtering is **static and one-time**. Data partitioning occurs before training using "eight distinct responses...generated...using a temperature of 0.9." All subsequent training uses the pre-filtered dataset.

## 4) Loss-Based Concepts
The paper does not employ EMA or reducible loss metrics. Instead, it relies on binary correctness judgments from generated responses.

## 5) VLM Tasks Tested
- Image classification (ImageNet subsets)
- Visual grounding (RefCOCO, Ref-L4, Lisa)
- Mathematical reasoning (MMK12, MMMU, WeMath, MathVerse, MathVista, MathVision)

## 6) Key Results
SFT-EM (easy + medium data) outperforms GRPO by up to **4.48%** on OOD tasks while being **4.9× faster** on ImageNet training. For reasoning: SFT-EM achieves "55.32%" average on Qwen2.5-VL-7B versus "53.12%" for GRPO.

## 7) Relation to RAPID-Like Approaches
Both filter noisy/difficult samples during SFT, but DC-SFT's approach is simpler: it removes hard samples entirely rather than using online weighting or confidence-based mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ea3e8e1-c2f0-4260-8b1d-0c63d3719fe8",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "7e836e9b-6eef-4963-9b43-f7d7d437305a",
  "toolUseResult": {
    "bytes": 224976,
    "code": 200,
    "codeText": "OK",
    "result": "# DC-SFT Technical Analysis\n\n## 1) Sample Difficulty Definition\nDifficulty is determined by model response correctness across multiple generations. The paper categorizes samples as:\n- **Easy**: \"all G responses are correct\" (G=8 samples generated)\n- **Hard**: \"all G responses are incorrect\"\n- **Medium-difficulty**: \"responses contain a mixture of correct and incorrect answers\"\n\n## 2) Filtering Mechanism\nThe approach uses **categorical filtering** rather than threshold-based or top-k methods. Samples are partitioned into discrete difficulty subsets, then the hard subset is excluded entirely. The paper notes: \"we conduct SFT separately on each subset\" and uses \"batch sizes of 16 for SFT and 128 for GRPO.\"\n\n## 3) Static vs. Dynamic\nThe filtering is **static and one-time**. Data partitioning occurs before training using \"eight distinct responses...generated...using a temperature of 0.9.\" All subsequent training uses the pre-filtered dataset.\n\n## 4) Loss-Based Concepts\nThe paper does not employ EMA or reducible loss metrics. Instead, it relies on binary correctness judgments from generated responses.\n\n## 5) VLM Tasks Tested\n- Image classification (ImageNet subsets)\n- Visual grounding (RefCOCO, Ref-L4, Lisa)\n- Mathematical reasoning (MMK12, MMMU, WeMath, MathVerse, MathVista, MathVision)\n\n## 6) Key Results\nSFT-EM (easy + medium data) outperforms GRPO by up to **4.48%** on OOD tasks while being **4.9× faster** on ImageNet training. For reasoning: SFT-EM achieves \"55.32%\" average on Qwen2.5-VL-7B versus \"53.12%\" for GRPO.\n\n## 7) Relation to RAPID-Like Approaches\nBoth filter noisy/difficult samples during SFT, but DC-SFT's approach is simpler: it removes hard samples entirely rather than using online weighting or confidence-based mechanisms.",
    "durationMs": 7506,
    "url": "https://arxiv.org/html/2602.10815v1"
  },
  "sourceToolAssistantUUID": "6ea3e8e1-c2f0-4260-8b1d-0c63d3719fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 140 · 2026-05-13T11:47:31.290Z_

This is extremely relevant — DC-SFT is a static, correctness-based filter for VLM reasoning tasks, while RAPID is an online, loss-based adaptive filter for VLA action prediction. Significant overlap in motivation but different domains and mechanisms. The proposal doesn't cite this paper. Let me do a few more critical searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e836e9b-6eef-4963-9b43-f7d7d437305a",
  "isSidechain": false,
  "requestId": "req_011CazWmuo5tNo8KdLSGhosg",
  "type": "assistant",
  "uuid": "2cee5c9d-18e0-415d-aa5e-83d874f48981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcM5KMjp1zZsMJjCUMa52j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 77514,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 77514,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-13T11:47:31.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AbfCofTx593p2VGFUAn6kr`</summary>

```json
{
  "query": "\"SFT memorizes RL generalizes\" 2501.17161 foundation model post-training data filtering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cee5c9d-18e0-415d-aa5e-83d874f48981",
  "isSidechain": false,
  "requestId": "req_011CazWmuo5tNo8KdLSGhosg",
  "type": "assistant",
  "uuid": "5e700be3-9bbf-4b0e-bff7-d22bbe7eafc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcM5KMjp1zZsMJjCUMa52j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 77514,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 735,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 77514,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 735
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-13T11:47:35.875Z_

<details><summary>↩ Tool result · `toolu_01AbfCofTx593p2VGFUAn6kr`</summary>

```text
Web search results for query: ""SFT memorizes RL generalizes" 2501.17161 foundation model post-training data filtering"

Links: [{"title":"[2501.17161] SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://arxiv.org/abs/2501.17161"},{"title":"GitHub - LeslieTrue/SFTvsRL: Official implementation of paper: SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training · GitHub","url":"https://github.com/LeslieTrue/SFTvsRL"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training | OpenReview","url":"https://openreview.net/forum?id=dYur3yabMj"},{"title":"Paper page - SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://huggingface.co/papers/2501.17161"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://arxiv.org/html/2501.17161v1"},{"title":"SFT Memorizes, RL Generalizes","url":"https://tianzhechu.com/SFTvsRL/"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundationa Model Post-training","url":"https://arxiv.org/html/2501.17161"},{"title":"ICML Poster SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://icml.cc/virtual/2025/poster/44633"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://proceedings.mlr.press/v267/chu25c.html"},{"title":"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training, Tianzhe Chu+, ICML'25 · Issue #1740 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1740"}]

Based on the search results, here's what I found about paper 2501.17161:

## Overview

The paper "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training" (arXiv 2501.17161) was authored by Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V. Le, Sergey Levine, and Yi Ma.

## Key Findings

The paper studies the difference between SFT and RL on generalization and memorization, focusing on text-based rule variants and visual variants.

The main results show a clear distinction:
- RL, especially when trained with an outcome-based reward, generalizes across both rule-based textual and visual variants, while SFT tends to memorize training data and struggles to generalize out-of-distribution scenarios.

## Methodology

The researchers introduce GeneralPoints, an arithmetic reasoning card game, and adopt V-IRL, a real-world navigation environment, to assess how models trained with SFT and RL generalize to unseen variants in both textual and visual domains.

Further analysis reveals that RL improves the model's underlying visual recognition capabilities, contributing to its enhanced generalization in the visual domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e700be3-9bbf-4b0e-bff7-d22bbe7eafc7",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "b72c6de4-3e96-45b7-b0e3-4a678de011ef",
  "toolUseResult": {
    "query": "\"SFT memorizes RL generalizes\" 2501.17161 foundation model post-training data filtering",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VWJyhoTqJNAxV3hrUxRFmX",
        "content": [
          {
            "title": "[2501.17161] SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://arxiv.org/abs/2501.17161"
          },
          {
            "title": "GitHub - LeslieTrue/SFTvsRL: Official implementation of paper: SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training · GitHub",
            "url": "https://github.com/LeslieTrue/SFTvsRL"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training | OpenReview",
            "url": "https://openreview.net/forum?id=dYur3yabMj"
          },
          {
            "title": "Paper page - SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://huggingface.co/papers/2501.17161"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://arxiv.org/html/2501.17161v1"
          },
          {
            "title": "SFT Memorizes, RL Generalizes",
            "url": "https://tianzhechu.com/SFTvsRL/"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundationa Model Post-training",
            "url": "https://arxiv.org/html/2501.17161"
          },
          {
            "title": "ICML Poster SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://icml.cc/virtual/2025/poster/44633"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://proceedings.mlr.press/v267/chu25c.html"
          },
          {
            "title": "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training, Tianzhe Chu+, ICML'25 · Issue #1740 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/1740"
          }
        ]
      },
      "Based on the search results, here's what I found about paper 2501.17161:\n\n## Overview\n\nThe paper \"SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training\" (arXiv 2501.17161) was authored by Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V. Le, Sergey Levine, and Yi Ma.\n\n## Key Findings\n\nThe paper studies the difference between SFT and RL on generalization and memorization, focusing on text-based rule variants and visual variants.\n\nThe main results show a clear distinction:\n- RL, especially when trained with an outcome-based reward, generalizes across both rule-based textual and visual variants, while SFT tends to memorize training data and struggles to generalize out-of-distribution scenarios.\n\n## Methodology\n\nThe researchers introduce GeneralPoints, an arithmetic reasoning card game, and adopt V-IRL, a real-world navigation environment, to assess how models trained with SFT and RL generalize to unseen variants in both textual and visual domains.\n\nFurther analysis reveals that RL improves the model's underlying visual recognition capabilities, contributing to its enhanced generalization in the visual domain."
    ],
    "durationSeconds": 4.389528969999985
  },
  "sourceToolAssistantUUID": "5e700be3-9bbf-4b0e-bff7-d22bbe7eafc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-13T11:47:39.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017eoKHt2vSHZgoW6VEbtMGq`</summary>

```json
{
  "query": "OpenVLA-OFT training GPU hours time cost A100 fine-tuning LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b72c6de4-3e96-45b7-b0e3-4a678de011ef",
  "isSidechain": false,
  "requestId": "req_011CazWndV66t79s4W89T2wV",
  "type": "assistant",
  "uuid": "d54509c3-fe21-46a0-9381-9cd3122eb1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PERZBRAH27snAN4NxMmGrR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 78249,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 78249,
          "cache_creation_input_tokens": 1061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1061
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 144_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d54509c3-fe21-46a0-9381-9cd3122eb1ee",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 145_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool result

_source line 146 · 2026-05-13T11:47:45.956Z_

<details><summary>↩ Tool result · `toolu_017eoKHt2vSHZgoW6VEbtMGq`</summary>

```text
Web search results for query: "OpenVLA-OFT training GPU hours time cost A100 fine-tuning LIBERO"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"}]

Based on the search results, here's the information about OpenVLA-OFT training costs and GPU hours for fine-tuning on LIBERO:

## Training Configuration and Time Cost

OpenVLA-OFT training jobs were run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.

## Gradient Steps by Dataset

The number of training steps varies by LIBERO task suite:
- For LIBERO experiments, 50K gradient steps were used with a batch size of 128 (8 GPUs x 16 samples each)
- For LIBERO-10 (LIBERO-Long), 80K gradient steps were used with the same batch size configuration

## Comparison to Standard OpenVLA Fine-tuning

For context, standard OpenVLA fine-tuning with LoRA takes 10-15 hours on a single A100 GPU, while the OFT approach uses more GPUs but achieves faster wall-clock training time of 1-2 days.

## Hardware Requirements

The recommended GPU memory for OpenVLA-OFT training on LIBERO with 1 input image is 44.1 GB, and with 2 input images plus proprioceptive state is 62.5 GB, both fitting within the 80GB A100/H100 GPUs used.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d54509c3-fe21-46a0-9381-9cd3122eb1ee",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "156fa303-f4a7-4420-9287-9187afa87059",
  "toolUseResult": {
    "query": "OpenVLA-OFT training GPU hours time cost A100 fine-tuning LIBERO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xxn1eptpBjh1BuRBAih7b4",
        "content": [
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub",
            "url": "https://github.com/moojink/openvla-oft"
          },
          {
            "title": "openvla/openvla-7b-finetuned-libero-spatial · Hugging Face",
            "url": "https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"
          },
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "openvla/openvla-7b-finetuned-libero-10 · Hugging Face",
            "url": "https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://openvla.github.io/"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2406.09246v3"
          }
        ]
      },
      "Based on the search results, here's the information about OpenVLA-OFT training costs and GPU hours for fine-tuning on LIBERO:\n\n## Training Configuration and Time Cost\n\nOpenVLA-OFT training jobs were run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.\n\n## Gradient Steps by Dataset\n\nThe number of training steps varies by LIBERO task suite:\n- For LIBERO experiments, 50K gradient steps were used with a batch size of 128 (8 GPUs x 16 samples each)\n- For LIBERO-10 (LIBERO-Long), 80K gradient steps were used with the same batch size configuration\n\n## Comparison to Standard OpenVLA Fine-tuning\n\nFor context, standard OpenVLA fine-tuning with LoRA takes 10-15 hours on a single A100 GPU, while the OFT approach uses more GPUs but achieves faster wall-clock training time of 1-2 days.\n\n## Hardware Requirements\n\nThe recommended GPU memory for OpenVLA-OFT training on LIBERO with 1 input image is 44.1 GB, and with 2 input images plus proprioceptive state is 62.5 GB, both fitting within the 80GB A100/H100 GPUs used."
    ],
    "durationSeconds": 6.788485157000017
  },
  "sourceToolAssistantUUID": "d54509c3-fe21-46a0-9381-9cd3122eb1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 147 · 2026-05-13T11:47:45.958Z_

```json
{
  "parentUuid": "156fa303-f4a7-4420-9287-9187afa87059",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "365693a4-1f03-4bdf-a86d-d9643cedbc41",
  "timestamp": "2026-05-13T11:47:45.958Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 148 · 2026-05-13T11:47:48.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgASu9k9ik8ENrqRzRNy4p`</summary>

```json
{
  "query": "SimpleVLA-RL GRPO training cost GPU hours environment interactions RL stage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "365693a4-1f03-4bdf-a86d-d9643cedbc41",
  "isSidechain": false,
  "requestId": "req_011CazWoNZBpHjcZbxoShjv4",
  "type": "assistant",
  "uuid": "820da84a-5db3-4ffb-8039-6e2157028548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNa2y1VC3BVJvSjhkYrXxr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 79310,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 79310,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-13T11:48:01.239Z_

<details><summary>↩ Tool result · `toolu_01FgASu9k9ik8ENrqRzRNy4p`</summary>

```text
Web search results for query: "SimpleVLA-RL GRPO training cost GPU hours environment interactions RL stage"

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"Paper page - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://huggingface.co/papers/2509.09674"},{"title":"[Literature Review] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/simplevla-rl-scaling-vla-training-via-reinforcement-learning"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.09674v1"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"RL/docs/guides/grpo.md at 1c371a9b34a703ac66fdc2d80b536f5fad99e616 · NVIDIA-NeMo/RL","url":"https://github.com/NVIDIA-NeMo/RL/blob/1c371a9b34a703ac66fdc2d80b536f5fad99e616/docs/guides/grpo.md"}]

I found search results about SimpleVLA-RL. However, the specific information about GPU hours training cost and exact environment interaction numbers doesn't appear to be in these results. Let me search more specifically for the computational requirements.

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"GitHub - thegovind/simplevla-rl: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://github.com/thegovind/simplevla-rl"},{"title":"SimpleVLA-RL/README.md at main · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/blob/main/README.md"},{"title":"Paper page - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://huggingface.co/papers/2509.09674"},{"title":"SRL: Scaling Distributed Reinforcement Learning to Over Ten Thousand Cores","url":"https://arxiv.org/html/2306.16688v3"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"How Much Do GPU Clusters Really Cost?","url":"https://newsletter.semianalysis.com/p/how-much-do-gpu-clusters-really-cost"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"A Comprehensive Guide to Selecting and Estimating GPUs for Serving ML Models. | by Samuel Taiwo | Medium","url":"https://medium.com/@samuel-taiwo/a-comprehensive-guide-to-selecting-and-estimating-gpus-for-serving-ml-models-23d2874dcbd8"},{"title":"Activity · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/activity"}]

Let me search for the actual paper with specific training metrics and numbers.

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement ...","url":"https://arxiv.org/pdf/2509.09674"},{"title":"Paper page - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://huggingface.co/papers/2509.09674"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"SimpleVLA-RL: Scalable RL for VLA Models","url":"https://www.emergentmind.com/papers/2509.09674"},{"title":"SimpleVLA-RL/README.md at main · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/blob/main/README.md"},{"title":"GitHub - thegovind/simplevla-rl: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://github.com/thegovind/simplevla-rl"},{"title":"(PDF) SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://www.researchgate.net/publication/395418649_SimpleVLA-RL_Scaling_VLA_Training_via_Reinforcement_Learning"}]

Based on my web search results, I've found comprehensive information about SimpleVLA-RL. Here's a summary of the key findings:

## SimpleVLA-RL: GRPO Training Overview

SimpleVLA-RL extends a rule-based online RL framework to VLA models for embodied manipulation tasks. The framework computes the GRPO loss to update the policy model.

### Training Configuration and Environment Interactions

The maximum environment interaction step is set to 512 in the LIBERO and 200, 400, or 800 in the RoboTwin1.0&2.0, depending on different tasks. For the four task suites of LIBERO, SFT is performed using all 500 demonstrations per task suite, then RL is performed on 500 corresponding simulation scenarios.

### GPU Resources and Hardware

Training is performed on 8×NVIDIA A800 80GB GPUs, with extensive domain randomization and parallel environment rollout. A single-node setup uses NUM_NODES=1, NUM_GPUS=8 (1 node with 8 NVIDIA A800 GPUs, each having 80GB memory).

### RL Stage Performance

On LIBERO, average success rate increases from 91% (SFT) to 99.1% (SimpleVLA-RL), with a 12% absolute gain on long-horizon tasks. With only a single demonstration per task (One-Trajectory SFT), RL boosts LIBERO-Long success rates from 17.3% to 91.7%, surpassing even the full-trajectory SFT baseline.

However, I was unable to find specific GPU-hour training cost figures or total number of environment interactions during the RL stage in the available search results. The paper appears to focus on performance metrics and task success rates rather than detailed computational cost reporting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "820da84a-5db3-4ffb-8039-6e2157028548",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "4bfbaa7e-6d2f-466e-9280-f4f25bcfd8b3",
  "toolUseResult": {
    "query": "SimpleVLA-RL GRPO training cost GPU hours environment interactions RL stage",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LykrXNC5MaPifshqZKwakA",
        "content": [
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=TQhSodCM4r"
          },
          {
            "title": "[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.09674"
          },
          {
            "title": "SimpleVLA-RL: Scalable VLA Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/simplevla-rl"
          },
          {
            "title": "Paper page - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://huggingface.co/papers/2509.09674"
          },
          {
            "title": "[Literature Review] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/simplevla-rl-scaling-vla-training-via-reinforcement-learning"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2509.09674v1"
          },
          {
            "title": "GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub",
            "url": "https://github.com/verl-project/verl"
          },
          {
            "title": "RL/docs/guides/grpo.md at 1c371a9b34a703ac66fdc2d80b536f5fad99e616 · NVIDIA-NeMo/RL",
            "url": "https://github.com/NVIDIA-NeMo/RL/blob/1c371a9b34a703ac66fdc2d80b536f5fad99e616/docs/guides/grpo.md"
          }
        ]
      },
      "I found search results about SimpleVLA-RL. However, the specific information about GPU hours training cost and exact environment interaction numbers doesn't appear to be in these results. Let me search more specifically for the computational requirements.",
      {
        "tool_use_id": "srvtoolu_01FnNgH1pxLQKbod4qbEG6P9",
        "content": [
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "GitHub - thegovind/simplevla-rl: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://github.com/thegovind/simplevla-rl"
          },
          {
            "title": "SimpleVLA-RL/README.md at main · PRIME-RL/SimpleVLA-RL",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL/blob/main/README.md"
          },
          {
            "title": "Paper page - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://huggingface.co/papers/2509.09674"
          },
          {
            "title": "SRL: Scaling Distributed Reinforcement Learning to Over Ten Thousand Cores",
            "url": "https://arxiv.org/html/2306.16688v3"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=TQhSodCM4r"
          },
          {
            "title": "How Much Do GPU Clusters Really Cost?",
            "url": "https://newsletter.semianalysis.com/p/how-much-do-gpu-clusters-really-cost"
          },
          {
            "title": "SimpleVLA-RL: Scalable VLA Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/simplevla-rl"
          },
          {
            "title": "A Comprehensive Guide to Selecting and Estimating GPUs for Serving ML Models. | by Samuel Taiwo | Medium",
            "url": "https://medium.com/@samuel-taiwo/a-comprehensive-guide-to-selecting-and-estimating-gpus-for-serving-ml-models-23d2874dcbd8"
          },
          {
            "title": "Activity · PRIME-RL/SimpleVLA-RL",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL/activity"
          }
        ]
      },
      "Let me search for the actual paper with specific training metrics and numbers.",
      {
        "tool_use_id": "srvtoolu_01BWAEX9BHQkKMqSd2QStGgo",
        "content": [
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          },
          {
            "title": "[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2509.09674"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement ...",
            "url": "https://arxiv.org/pdf/2509.09674"
          },
          {
            "title": "Paper page - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://huggingface.co/papers/2509.09674"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=TQhSodCM4r"
          },
          {
            "title": "SimpleVLA-RL: Scalable RL for VLA Models",
            "url": "https://www.emergentmind.com/papers/2509.09674"
          },
          {
            "title": "SimpleVLA-RL/README.md at main · PRIME-RL/SimpleVLA-RL",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL/blob/main/README.md"
          },
          {
            "title": "GitHub - thegovind/simplevla-rl: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://github.com/thegovind/simplevla-rl"
          },
          {
            "title": "(PDF) SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/395418649_SimpleVLA-RL_Scaling_VLA_Training_via_Reinforcement_Learning"
          }
        ]
      },
      "Based on my web search results, I've found comprehensive information about SimpleVLA-RL. Here's a summary of the key findings:\n\n## SimpleVLA-RL: GRPO Training Overview\n\nSimpleVLA-RL extends a rule-based online RL framework to VLA models for embodied manipulation tasks. The framework computes the GRPO loss to update the policy model.\n\n### Training Configuration and Environment Interactions\n\nThe maximum environment interaction step is set to 512 in the LIBERO and 200, 400, or 800 in the RoboTwin1.0&2.0, depending on different tasks. For the four task suites of LIBERO, SFT is performed using all 500 demonstrations per task suite, then RL is performed on 500 corresponding simulation scenarios.\n\n### GPU Resources and Hardware\n\nTraining is performed on 8×NVIDIA A800 80GB GPUs, with extensive domain randomization and parallel environment rollout. A single-node setup uses NUM_NODES=1, NUM_GPUS=8 (1 node with 8 NVIDIA A800 GPUs, each having 80GB memory).\n\n### RL Stage Performance\n\nOn LIBERO, average success rate increases from 91% (SFT) to 99.1% (SimpleVLA-RL), with a 12% absolute gain on long-horizon tasks. With only a single demonstration per task (One-Trajectory SFT), RL boosts LIBERO-Long success rates from 17.3% to 91.7%, surpassing even the full-trajectory SFT baseline.\n\nHowever, I was unable to find specific GPU-hour training cost figures or total number of environment interactions during the RL stage in the available search results. The paper appears to focus on performance metrics and task success rates rather than detailed computational cost reporting."
    ],
    "durationSeconds": 12.512942679999979
  },
  "sourceToolAssistantUUID": "820da84a-5db3-4ffb-8039-6e2157028548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 150 · 2026-05-13T11:48:04.393Z_

Now let me do one final critical search to look for any very recent work that might have been missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bfbaa7e-6d2f-466e-9280-f4f25bcfd8b3",
  "isSidechain": false,
  "requestId": "req_011CazWpVvisRfocEDm2Qayc",
  "type": "assistant",
  "uuid": "c97cb45e-f692-4bc1-930d-88ef9ef8e913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPTQD3MPeqw2UHe696GG5Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 80333,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 80333,
          "cache_creation_input_tokens": 2191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2191
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-13T11:48:05.198Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ziwiEA4msetMGJ8HJUZ8P`</summary>

```json
{
  "query": "arxiv 2026 robot demonstration curation online training-time data selection noise reduction VLA SFT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c97cb45e-f692-4bc1-930d-88ef9ef8e913",
  "isSidechain": false,
  "requestId": "req_011CazWpVvisRfocEDm2Qayc",
  "type": "assistant",
  "uuid": "8de7df59-5023-438f-988a-c67ef0d2bad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPTQD3MPeqw2UHe696GG5Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 80333,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 80333,
          "cache_creation_input_tokens": 2191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2191
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-13T11:48:13.426Z_

<details><summary>↩ Tool result · `toolu_012ziwiEA4msetMGJ8HJUZ8P`</summary>

```text
Web search results for query: "arxiv 2026 robot demonstration curation online training-time data selection noise reduction VLA SFT"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs","url":"https://arxiv.org/html/2603.11426v1"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"A Pragmatic VLA Foundation Model","url":"https://arxiv.org/html/2601.18692v1"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"}]

I found several highly relevant arxiv papers from 2026 related to your search query. Here are the key findings:

## Primary Results:

**Quality over Quantity (QoQ)**: Learning from demonstrations has emerged as a promising paradigm for end-to-end robot control, particularly when scaled to diverse and large datasets. However, the quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning. Human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors, making data curation essential yet largely manual and heuristic-driven. QoQ proposes a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations, using influence functions to quantify the impact of individual training samples on model performance.

**Demo-SCORE**: A method for robots to self-curate based on online robot experience, training and cross-validating a classifier to discern successful policy roll-outs from unsuccessful ones and using the classifier to filter heterogeneous demonstration datasets. Demo-SCORE can effectively identify suboptimal demonstrations without manual curation.

**Green-VLA**: Demonstrates a three-stage approach using the same architecture: (i) R0 pretraining on the unfiltered BRIDGE mixture, (ii) R1-style SFT on a filtered BRIDGE subset, and (iii) R2 RL fine-tuning starting from the filtered R1 checkpoint, showing how dataset curation plus RL alignment builds on the unified pretrain to progressively improve performance.

These papers address online training-time data selection, noise reduction through demonstration curation, and VLA supervised fine-tuning (SFT) that your query specifically targeted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8de7df59-5023-438f-988a-c67ef0d2bad1",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "d5954963-85ac-49d7-b9f6-a672818d9ef1",
  "toolUseResult": {
    "query": "arxiv 2026 robot demonstration curation online training-time data selection noise reduction VLA SFT",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GBVC3JH8khABGrW5ZLKazr",
        "content": [
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2602.00919v1"
          },
          {
            "title": "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/html/2603.09056"
          },
          {
            "title": "[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning",
            "url": "https://arxiv.org/abs/2603.09056"
          },
          {
            "title": "Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs",
            "url": "https://arxiv.org/html/2603.11426v1"
          },
          {
            "title": "From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop",
            "url": "https://icra2026vlapipeline.github.io/"
          },
          {
            "title": "A Pragmatic VLA Foundation Model",
            "url": "https://arxiv.org/html/2601.18692v1"
          },
          {
            "title": "Curating Demonstrations using Online Experience",
            "url": "https://arxiv.org/html/2503.03707"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "DataMIL : Selecting Data for Robot Imitation Learning with Datamodels",
            "url": "https://arxiv.org/html/2505.09603"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.16391"
          }
        ]
      },
      "I found several highly relevant arxiv papers from 2026 related to your search query. Here are the key findings:\n\n## Primary Results:\n\n**Quality over Quantity (QoQ)**: Learning from demonstrations has emerged as a promising paradigm for end-to-end robot control, particularly when scaled to diverse and large datasets. However, the quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning. Human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors, making data curation essential yet largely manual and heuristic-driven. QoQ proposes a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations, using influence functions to quantify the impact of individual training samples on model performance.\n\n**Demo-SCORE**: A method for robots to self-curate based on online robot experience, training and cross-validating a classifier to discern successful policy roll-outs from unsuccessful ones and using the classifier to filter heterogeneous demonstration datasets. Demo-SCORE can effectively identify suboptimal demonstrations without manual curation.\n\n**Green-VLA**: Demonstrates a three-stage approach using the same architecture: (i) R0 pretraining on the unfiltered BRIDGE mixture, (ii) R1-style SFT on a filtered BRIDGE subset, and (iii) R2 RL fine-tuning starting from the filtered R1 checkpoint, showing how dataset curation plus RL alignment builds on the unified pretrain to progressively improve performance.\n\nThese papers address online training-time data selection, noise reduction through demonstration curation, and VLA supervised fine-tuning (SFT) that your query specifically targeted."
    ],
    "durationSeconds": 8.224588655999979
  },
  "sourceToolAssistantUUID": "8de7df59-5023-438f-988a-c67ef0d2bad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-13T11:48:18.327Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013xR9kzasgqrypwaBxXmFfH`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.03707",
  "prompt": "I need to understand this paper on 'Curating Demonstrations using Online Experience': 1) What is Demo-SCORE? 2) Is it static or online/dynamic during training? 3) Does it use loss-based signals, EMA models, or reducible loss? 4) When was it submitted and to what venue? 5) How does it differ from online data weighting approaches like RAPID? 6) What tasks does it apply to?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5954963-85ac-49d7-b9f6-a672818d9ef1",
  "isSidechain": false,
  "requestId": "req_011CazWqQ2nyyGL19MMACsVG",
  "type": "assistant",
  "uuid": "93852c7f-0df2-4d11-8c5a-b5017abbffa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZiJdA6L3GdrP3t9gRGyQU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 82524,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 82524,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 154_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "93852c7f-0df2-4d11-8c5a-b5017abbffa0",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 155_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Tool result

_source line 156 · 2026-05-13T11:48:25.180Z_

<details><summary>↩ Tool result · `toolu_013xR9kzasgqrypwaBxXmFfH`</summary>

```text
# Demo-SCORE: Curating Demonstrations Using Online Experience

## 1) What is Demo-SCORE?

Demo-SCORE is an automated method for filtering heterogeneous demonstration datasets by identifying and removing unreliable strategies. The approach trains a binary classifier on policy rollouts to distinguish successful from failed trajectories, then applies this classifier to curate the original demonstration set.

## 2) Static or Dynamic During Training?

Demo-SCORE operates **statically post-training**. It trains an initial policy on all demonstrations, generates rollouts during evaluation, trains the classifier, and then filters demonstrations for a final retraining phase. It is not dynamically applied during the initial policy training.

## 3) Loss-Based Signals, EMA Models, or Reducible Loss?

Demo-SCORE uses **binary success/failure labels** from rollouts rather than loss-based signals. The classifier learns from "sparse binary success/failure annotations" without computing reducible loss or using EMA models. It relies on cross-validation across multiple policy checkpoints for generalization.

## 4) Submission Timeline and Venue

The paper shows a version number (2503.03707v2) indicating an **arXiv submission in March 2025**. No specific conference venue is explicitly stated in the provided content.

## 5) Comparison to RAPID and Online Data Weighting

The paper does not mention RAPID. It compares to Training Loss weighting (inverse loss), Autonomous Imitation Learning, and Return-Conditioned Policies. Unlike online weighting approaches, Demo-SCORE performs **binary filtering** (keep/discard) rather than continuous reweighting.

## 6) Task Applications

Demo-SCORE evaluates on robotic manipulation tasks: Robosuite square peg insertion, ALOHA peg insertion (simulated and real), and five real-world ALOHA tasks (spoon placement, chocolate transfer, sharpie pickup, strawberry pickup, jellybean assembly).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93852c7f-0df2-4d11-8c5a-b5017abbffa0",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "62f38c7e-756b-4ce3-be73-17fa2995f6a9",
  "toolUseResult": {
    "bytes": 417931,
    "code": 200,
    "codeText": "OK",
    "result": "# Demo-SCORE: Curating Demonstrations Using Online Experience\n\n## 1) What is Demo-SCORE?\n\nDemo-SCORE is an automated method for filtering heterogeneous demonstration datasets by identifying and removing unreliable strategies. The approach trains a binary classifier on policy rollouts to distinguish successful from failed trajectories, then applies this classifier to curate the original demonstration set.\n\n## 2) Static or Dynamic During Training?\n\nDemo-SCORE operates **statically post-training**. It trains an initial policy on all demonstrations, generates rollouts during evaluation, trains the classifier, and then filters demonstrations for a final retraining phase. It is not dynamically applied during the initial policy training.\n\n## 3) Loss-Based Signals, EMA Models, or Reducible Loss?\n\nDemo-SCORE uses **binary success/failure labels** from rollouts rather than loss-based signals. The classifier learns from \"sparse binary success/failure annotations\" without computing reducible loss or using EMA models. It relies on cross-validation across multiple policy checkpoints for generalization.\n\n## 4) Submission Timeline and Venue\n\nThe paper shows a version number (2503.03707v2) indicating an **arXiv submission in March 2025**. No specific conference venue is explicitly stated in the provided content.\n\n## 5) Comparison to RAPID and Online Data Weighting\n\nThe paper does not mention RAPID. It compares to Training Loss weighting (inverse loss), Autonomous Imitation Learning, and Return-Conditioned Policies. Unlike online weighting approaches, Demo-SCORE performs **binary filtering** (keep/discard) rather than continuous reweighting.\n\n## 6) Task Applications\n\nDemo-SCORE evaluates on robotic manipulation tasks: Robosuite square peg insertion, ALOHA peg insertion (simulated and real), and five real-world ALOHA tasks (spoon placement, chocolate transfer, sharpie pickup, strawberry pickup, jellybean assembly).",
    "durationMs": 6847,
    "url": "https://arxiv.org/html/2503.03707"
  },
  "sourceToolAssistantUUID": "93852c7f-0df2-4d11-8c5a-b5017abbffa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-13T11:48:28.084Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014SHkuYWP6v2m48PWKZt6oV`</summary>

```json
{
  "query": "\"token priority SFT\" arxiv 2026 importance sampling SFT granular training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62f38c7e-756b-4ce3-be73-17fa2995f6a9",
  "isSidechain": false,
  "requestId": "req_011CazWrGFkdoNx6rAfYpZKz",
  "type": "assistant",
  "uuid": "1cf25f7f-ea1d-49cc-b084-03152f07183f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eozc1pPxLUCapEgbRwcsU9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 83461,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 83461,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-13T11:48:36.297Z_

<details><summary>↩ Tool result · `toolu_014SHkuYWP6v2m48PWKZt6oV`</summary>

```text
Web search results for query: ""token priority SFT" arxiv 2026 importance sampling SFT granular training"

Links: [{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://arxiv.org/html/2602.01227"},{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://www.arxiv.org/pdf/2602.01227"},{"title":"[2601.09195] ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection","url":"https://arxiv.org/abs/2601.09195"},{"title":"[2602.01227] Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://arxiv.org/abs/2602.01227"},{"title":"Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://www.arxiv.org/pdf/2602.01058"},{"title":"Leveraging Importance Sampling to Detach Alignment Modules from Large Language Models","url":"https://arxiv.org/html/2505.19700"},{"title":"ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection","url":"https://arxiv.org/html/2601.09195"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2508.11408"},{"title":"Mitigating Reward Over-optimization in Direct Alignment Algorithms with Importance Sampling","url":"https://arxiv.org/html/2506.08681"},{"title":"Token-Importance Guided Direct Preference Optimization","url":"https://arxiv.org/html/2505.19653v1"}]

Based on the web search results, I found several highly relevant papers from 2026 and recent work on token priority in supervised fine-tuning with importance sampling approaches:

## Key Findings:

**Main Paper - "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority"**

This position paper advocates Token Priority as the essential bridge, formalizing Supervised Fine-Tuning (SFT) not as simple optimization but as a precise distribution reshaping process that aligns raw data with the ideal alignment manifold.

By viewing token priority Φ(x) as a Granular Importance Sampling estimator (approximating the density ratio πθ(x)/πdata(x)), SFT can dynamically modulate gradients, allowing the model to "clip" updates on tokens where the policy divergence is excessive while accelerating learning on tokens within the trust region.

**Granular Training Approaches:**

Token Priority filters noise in SFT by identifying and masking easy, surface-level patterns, preventing the model from overfitting to the static training distribution and forcing it to focus on the "long-tail" logic tokens that dictate generalization.

A fine-grained priority function can reward locally optimal actions via selective backpropagation, ensuring that models learn robust logical operators rather than just memorizing successful paths.

**Related Methods:**

ProFit selectively masks low-probability tokens to prevent surface-level overfitting, consistently outperforming traditional SFT baselines on general reasoning and mathematical benchmarks.

PEAR (Policy Evaluation–inspired Algorithm for Offline Learning Loss Reweighting) is an OPE-inspired loss reweighting scheme that down-weights logged continuations that are implausible under the current policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cf25f7f-ea1d-49cc-b084-03152f07183f",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "3840bf58-c904-4b49-ae0d-460cd068e40c",
  "toolUseResult": {
    "query": "\"token priority SFT\" arxiv 2026 importance sampling SFT granular training",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CvhWJPHcbKeH2PerMMpoxZ",
        "content": [
          {
            "title": "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority",
            "url": "https://arxiv.org/html/2602.01227"
          },
          {
            "title": "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority",
            "url": "https://www.arxiv.org/pdf/2602.01227"
          },
          {
            "title": "[2601.09195] ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection",
            "url": "https://arxiv.org/abs/2601.09195"
          },
          {
            "title": "[2602.01227] Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority",
            "url": "https://arxiv.org/abs/2602.01227"
          },
          {
            "title": "Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning",
            "url": "https://www.arxiv.org/pdf/2602.01058"
          },
          {
            "title": "Leveraging Importance Sampling to Detach Alignment Modules from Large Language Models",
            "url": "https://arxiv.org/html/2505.19700"
          },
          {
            "title": "ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection",
            "url": "https://arxiv.org/html/2601.09195"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2508.11408"
          },
          {
            "title": "Mitigating Reward Over-optimization in Direct Alignment Algorithms with Importance Sampling",
            "url": "https://arxiv.org/html/2506.08681"
          },
          {
            "title": "Token-Importance Guided Direct Preference Optimization",
            "url": "https://arxiv.org/html/2505.19653v1"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers from 2026 and recent work on token priority in supervised fine-tuning with importance sampling approaches:\n\n## Key Findings:\n\n**Main Paper - \"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority\"**\n\nThis position paper advocates Token Priority as the essential bridge, formalizing Supervised Fine-Tuning (SFT) not as simple optimization but as a precise distribution reshaping process that aligns raw data with the ideal alignment manifold.\n\nBy viewing token priority Φ(x) as a Granular Importance Sampling estimator (approximating the density ratio πθ(x)/πdata(x)), SFT can dynamically modulate gradients, allowing the model to \"clip\" updates on tokens where the policy divergence is excessive while accelerating learning on tokens within the trust region.\n\n**Granular Training Approaches:**\n\nToken Priority filters noise in SFT by identifying and masking easy, surface-level patterns, preventing the model from overfitting to the static training distribution and forcing it to focus on the \"long-tail\" logic tokens that dictate generalization.\n\nA fine-grained priority function can reward locally optimal actions via selective backpropagation, ensuring that models learn robust logical operators rather than just memorizing successful paths.\n\n**Related Methods:**\n\nProFit selectively masks low-probability tokens to prevent surface-level overfitting, consistently outperforming traditional SFT baselines on general reasoning and mathematical benchmarks.\n\nPEAR (Policy Evaluation–inspired Algorithm for Offline Learning Loss Reweighting) is an OPE-inspired loss reweighting scheme that down-weights logged continuations that are implausible under the current policy."
    ],
    "durationSeconds": 8.21014482200006
  },
  "sourceToolAssistantUUID": "1cf25f7f-ea1d-49cc-b084-03152f07183f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-13T11:48:39.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NxE1J6GgLggyXrBv6Rr2iJ`</summary>

```json
{
  "query": "\"Good SFT Optimizes\" \"Better SFT Prepares for Reinforcement Learning\" 2602.01058"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3840bf58-c904-4b49-ae0d-460cd068e40c",
  "isSidechain": false,
  "requestId": "req_011CazWs5tScGUHVM4W38LeZ",
  "type": "assistant",
  "uuid": "168a0a95-434d-4a60-9910-4f68c6c9e510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Anf6Nwg8azATD2vLSCgEGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 84093,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 946,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 84093,
          "cache_creation_input_tokens": 946,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 946
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-13T11:48:45.009Z_

<details><summary>↩ Tool result · `toolu_01NxE1J6GgLggyXrBv6Rr2iJ`</summary>

```text
Web search results for query: ""Good SFT Optimizes" "Better SFT Prepares for Reinforcement Learning" 2602.01058"

Links: [{"title":"[2602.01058] Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://arxiv.org/abs/2602.01058"},{"title":"Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://arxiv.org/html/2602.01058"},{"title":"Paper page - Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://huggingface.co/papers/2602.01058"},{"title":"Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://www.arxiv.org/pdf/2602.01058"},{"title":"(PDF) Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning","url":"https://www.researchgate.net/publication/400369783_Good_SFT_Optimizes_for_SFT_Better_SFT_Prepares_for_Reinforcement_Learning"}]

I found the research paper you were looking for! Here are the key details:

**Paper Title:** Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning

**Authors & Date:** The paper was submitted on February 1, 2026 by Dylan Zhang, Yufeng Xu, Haojin Wang, Qingzhi Chen, and Hao Peng

**Key Finding:** After identical RL training, models initialized from stronger SFT checkpoints can significantly underperform those initialized from weaker ones

**Main Contribution:** The researchers propose PEAR (Policy Evaluation-inspired Algorithm for Offline Learning Loss Re-weighting), an SFT-stage method that corrects this mismatch and better prepares the model for RL

The paper addresses an important issue in LLM post-training: the distribution that generates the offline SFT data can differ substantially from the policy optimized during online RL, which learns from its own rollouts

The paper is available on arXiv at https://arxiv.org/abs/2602.01058


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "168a0a95-434d-4a60-9910-4f68c6c9e510",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "97cdc653-8997-49d0-91b2-1c2cbe696f1f",
  "toolUseResult": {
    "query": "\"Good SFT Optimizes\" \"Better SFT Prepares for Reinforcement Learning\" 2602.01058",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DWeGyjrjY8CjYvqk6bpTdz",
        "content": [
          {
            "title": "[2602.01058] Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.01058"
          },
          {
            "title": "Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning",
            "url": "https://arxiv.org/html/2602.01058"
          },
          {
            "title": "Paper page - Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning",
            "url": "https://huggingface.co/papers/2602.01058"
          },
          {
            "title": "Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning",
            "url": "https://www.arxiv.org/pdf/2602.01058"
          },
          {
            "title": "(PDF) Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/400369783_Good_SFT_Optimizes_for_SFT_Better_SFT_Prepares_for_Reinforcement_Learning"
          }
        ]
      },
      "I found the research paper you were looking for! Here are the key details:\n\n**Paper Title:** Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning\n\n**Authors & Date:** The paper was submitted on February 1, 2026 by Dylan Zhang, Yufeng Xu, Haojin Wang, Qingzhi Chen, and Hao Peng\n\n**Key Finding:** After identical RL training, models initialized from stronger SFT checkpoints can significantly underperform those initialized from weaker ones\n\n**Main Contribution:** The researchers propose PEAR (Policy Evaluation-inspired Algorithm for Offline Learning Loss Re-weighting), an SFT-stage method that corrects this mismatch and better prepares the model for RL\n\nThe paper addresses an important issue in LLM post-training: the distribution that generates the offline SFT data can differ substantially from the policy optimized during online RL, which learns from its own rollouts\n\nThe paper is available on arXiv at https://arxiv.org/abs/2602.01058"
    ],
    "durationSeconds": 5.297245464000036
  },
  "sourceToolAssistantUUID": "168a0a95-434d-4a60-9910-4f68c6c9e510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 161 · 2026-05-13T11:48:49.307Z_

This is another very important find — "Good SFT Optimizes for SFT, Better SFT Prepares for RL" (2602.01058) directly studies how SFT technique/data affects downstream RL and proposes PEAR, an SFT-stage loss reweighting method to better prepare for RL. This is highly relevant and not cited in the proposal. Let me fetch more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97cdc653-8997-49d0-91b2-1c2cbe696f1f",
  "isSidechain": false,
  "requestId": "req_011CazWsj2rMjtFdtXGMWq7f",
  "type": "assistant",
  "uuid": "f4cdf0da-d834-438e-8470-54ce22331cea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPUWZE3DZQKAx1Ku4BDwvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 85039,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 85039,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-13T11:48:51.974Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HdjgdVwgNG7mrLEvAnfHxN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.01058",
  "prompt": "Extract: 1) Full abstract 2) What is PEAR exactly? How does it work? 3) Does it use loss reweighting, data filtering, or something else? 4) Is it for LLMs or robots? 5) What is the key insight about SFT quality and downstream RL? 6) Venue status (accepted where?) 7) How does it relate to the idea that SFT data quality affects RL outcomes?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4cdf0da-d834-438e-8470-54ce22331cea",
  "isSidechain": false,
  "requestId": "req_011CazWsj2rMjtFdtXGMWq7f",
  "type": "assistant",
  "uuid": "05cd0e7d-e576-428c-96c1-1d89fcb5c6cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPUWZE3DZQKAx1Ku4BDwvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 85039,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 85039,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-13T11:48:57.580Z_

<details><summary>↩ Tool result · `toolu_01HdjgdVwgNG7mrLEvAnfHxN`</summary>

```text
# Analysis of arXiv:2602.01058

**1) Full Abstract:**
Post-training reasoning LLMs involves SFT followed by RL. The paper shows that stronger SFT checkpoints can underperform weaker ones after identical RL training due to distribution mismatch. PEAR is proposed to reweight SFT loss using importance sampling at token, block, and sequence levels. Experiments on mathematical reasoning tasks show improvements up to 14.6% on AIME2025.

**2) What is PEAR?**
PEAR stands for "Policy Evaluation-inspired Algorithm for Offline Learning Loss Re-weighting." It's "an SFT-stage method that corrects this mismatch and better prepares the model for RL."

**3) Loss Reweighting vs. Filtering:**
PEAR uses **loss reweighting**. It "uses importance sampling to reweight the SFT loss, with three variants operating at the token, block, and sequence levels."

**4) LLMs or Robots:**
This applies to **Large Language Models (LLMs)**. The work focuses on "post-training of reasoning LLMs."

**5) Key Insight on SFT Quality and RL:**
The critical finding: "the distribution that generates the offline SFT data can differ substantially from the policy optimized during online RL, which learns from its own rollouts." Superior SFT performance doesn't guarantee better RL outcomes—alignment between SFT and RL distributions matters.

**6) Venue Status:**
The paper was submitted February 1, 2026. No acceptance venue is mentioned on this abstract page.

**7) Relation to SFT Data Quality:**
PEAR embodies the principle that SFT should be "designed and evaluated with downstream RL in mind rather than in isolation," treating data quality through distributional alignment rather than raw performance optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05cd0e7d-e576-428c-96c1-1d89fcb5c6cd",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "399bf5ab-bb2e-4f3d-b9f1-57bf141b54ef",
  "toolUseResult": {
    "bytes": 48146,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2602.01058\n\n**1) Full Abstract:**\nPost-training reasoning LLMs involves SFT followed by RL. The paper shows that stronger SFT checkpoints can underperform weaker ones after identical RL training due to distribution mismatch. PEAR is proposed to reweight SFT loss using importance sampling at token, block, and sequence levels. Experiments on mathematical reasoning tasks show improvements up to 14.6% on AIME2025.\n\n**2) What is PEAR?**\nPEAR stands for \"Policy Evaluation-inspired Algorithm for Offline Learning Loss Re-weighting.\" It's \"an SFT-stage method that corrects this mismatch and better prepares the model for RL.\"\n\n**3) Loss Reweighting vs. Filtering:**\nPEAR uses **loss reweighting**. It \"uses importance sampling to reweight the SFT loss, with three variants operating at the token, block, and sequence levels.\"\n\n**4) LLMs or Robots:**\nThis applies to **Large Language Models (LLMs)**. The work focuses on \"post-training of reasoning LLMs.\"\n\n**5) Key Insight on SFT Quality and RL:**\nThe critical finding: \"the distribution that generates the offline SFT data can differ substantially from the policy optimized during online RL, which learns from its own rollouts.\" Superior SFT performance doesn't guarantee better RL outcomes—alignment between SFT and RL distributions matters.\n\n**6) Venue Status:**\nThe paper was submitted February 1, 2026. No acceptance venue is mentioned on this abstract page.\n\n**7) Relation to SFT Data Quality:**\nPEAR embodies the principle that SFT should be \"designed and evaluated with downstream RL in mind rather than in isolation,\" treating data quality through distributional alignment rather than raw performance optimization.",
    "durationMs": 5601,
    "url": "https://arxiv.org/abs/2602.01058"
  },
  "sourceToolAssistantUUID": "05cd0e7d-e576-428c-96c1-1d89fcb5c6cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 164 · 2026-05-13T11:49:01.082Z_

This is critical. PEAR (Feb 2026) directly studies how SFT loss reweighting affects downstream RL for LLMs — closely related to RAPID's Contribution 3. Let me check one more dimension.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "399bf5ab-bb2e-4f3d-b9f1-57bf141b54ef",
  "isSidechain": false,
  "requestId": "req_011CazWtep8PwYYoozKyWa8r",
  "type": "assistant",
  "uuid": "11382b33-4ff8-456b-b459-db299b99c667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxoYCPcKjY7DZpn73kmD3i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 85718,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 85718,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-13T11:49:01.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FJ7NKAwfnaAc1Zqepb47iC`</summary>

```json
{
  "query": "data curation VLA SFT RL pipeline robot 2026 arxiv noise filtering quality scoring training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11382b33-4ff8-456b-b459-db299b99c667",
  "isSidechain": false,
  "requestId": "req_011CazWtep8PwYYoozKyWa8r",
  "type": "assistant",
  "uuid": "ee674722-bebf-4dde-9f5a-abe3b42dda51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxoYCPcKjY7DZpn73kmD3i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 85718,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 85718,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-13T11:49:10.193Z_

<details><summary>↩ Tool result · `toolu_01FJ7NKAwfnaAc1Zqepb47iC`</summary>

```text
Web search results for query: "data curation VLA SFT RL pipeline robot 2026 arxiv noise filtering quality scoring training"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"From SFT to RL: Demystifying the Post-Training Pipeline for LLM-based Vulnerability Detection","url":"https://arxiv.org/html/2602.14012"},{"title":"𝜋_\"RL\": Online RL Fine-tuning for Flow-based Vision-Language-Action Models","url":"https://arxiv.org/html/2510.25889v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for...","url":"https://arxiv.org/abs/2603.26666"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091v1"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2510.01623v1"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"}]

Based on the search results, I found several highly relevant papers from arXiv 2026 discussing data curation, VLA (Vision-Language-Action) models, SFT (Supervised Fine-Tuning), RL (Reinforcement Learning) pipelines, and robot training:

## Key Findings:

**Green-VLA (January 2026)**: This work performs a three-stage comparison including R0 pretraining on unfiltered data, R1-style SFT on filtered subsets, and R2 RL fine-tuning, demonstrating how dataset curation plus RL alignment progressively improves performance on target embodiments.

**VLA-OPD (March 2026)**: This framework bridges the efficiency of SFT with the robustness of RL by leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories, enabling active error correction on policy-induced states while preserving pre-trained capabilities.

**Data Curation and Noise Filtering**: Most VLA pipelines lack rigorous data curation, principled training regimes, and standardized evaluation, leading to inconsistent performance and safety concerns on physical robots. For data curation in post-training pipelines, rejection sampling proves more effective than rationalization-based supervision, as rationalization can introduce hallucinations; in RL training, difficulty-aware data filtering can reduce data coverage, causing performance loss.

**Quality Scoring and Training**: Training often uses two stages: SFT with CoT supervision to learn reasoning over images and instructions, followed by refinement via RL with verifiable rewards (GRPO).

These papers represent recent advances in creating more robust VLA training pipelines with improved data handling and quality control mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee674722-bebf-4dde-9f5a-abe3b42dda51",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "37e37ae3-d162-4a64-833e-149ebc340c60",
  "toolUseResult": {
    "query": "data curation VLA SFT RL pipeline robot 2026 arxiv noise filtering quality scoring training",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nvzo68DFG4ZXVCZsJYuj7n",
        "content": [
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2602.00919v1"
          },
          {
            "title": "From SFT to RL: Demystifying the Post-Training Pipeline for LLM-based Vulnerability Detection",
            "url": "https://arxiv.org/html/2602.14012"
          },
          {
            "title": "𝜋_\"RL\": Online RL Fine-tuning for Flow-based Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.25889v1"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666"
          },
          {
            "title": "From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop",
            "url": "https://icra2026vlapipeline.github.io/"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for...",
            "url": "https://arxiv.org/abs/2603.26666"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL",
            "url": "https://arxiv.org/html/2511.00091v1"
          },
          {
            "title": "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.01623v1"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers from arXiv 2026 discussing data curation, VLA (Vision-Language-Action) models, SFT (Supervised Fine-Tuning), RL (Reinforcement Learning) pipelines, and robot training:\n\n## Key Findings:\n\n**Green-VLA (January 2026)**: This work performs a three-stage comparison including R0 pretraining on unfiltered data, R1-style SFT on filtered subsets, and R2 RL fine-tuning, demonstrating how dataset curation plus RL alignment progressively improves performance on target embodiments.\n\n**VLA-OPD (March 2026)**: This framework bridges the efficiency of SFT with the robustness of RL by leveraging an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories, enabling active error correction on policy-induced states while preserving pre-trained capabilities.\n\n**Data Curation and Noise Filtering**: Most VLA pipelines lack rigorous data curation, principled training regimes, and standardized evaluation, leading to inconsistent performance and safety concerns on physical robots. For data curation in post-training pipelines, rejection sampling proves more effective than rationalization-based supervision, as rationalization can introduce hallucinations; in RL training, difficulty-aware data filtering can reduce data coverage, causing performance loss.\n\n**Quality Scoring and Training**: Training often uses two stages: SFT with CoT supervision to learn reasoning over images and instructions, followed by refinement via RL with verifiable rewards (GRPO).\n\nThese papers represent recent advances in creating more robust VLA training pipelines with improved data handling and quality control mechanisms."
    ],
    "durationSeconds": 8.327464090000023
  },
  "sourceToolAssistantUUID": "ee674722-bebf-4dde-9f5a-abe3b42dda51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 167 · 2026-05-13T11:49:10.196Z_

```json
{
  "parentUuid": "37e37ae3-d162-4a64-833e-149ebc340c60",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "04304a59-de09-454b-806d-76eb18bef8e1",
  "timestamp": "2026-05-13T11:49:10.196Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 168_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "04304a59-de09-454b-806d-76eb18bef8e1",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 169_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Assistant

_source line 170 · 2026-05-13T11:49:13.058Z_

I've now conducted extensive research. Let me synthesize my findings and produce the review verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04304a59-de09-454b-806d-76eb18bef8e1",
  "isSidechain": false,
  "requestId": "req_011CazWuap3jhFFC42pSiEL2",
  "type": "assistant",
  "uuid": "8f245c1d-6d80-40fc-8105-1fcd91704a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS3ScB8y5xLuoVFGUEw3H7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 86433,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 86433,
          "cache_creation_input_tokens": 1112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1112
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-13T11:49:13.861Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UvRYZkhRztHxNyf4Ys8a3k`</summary>

```json
{
  "query": "\"self-distillation\" \"sometimes degrade\" reasoning LLM 2603 arxiv feedback loop EMA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f245c1d-6d80-40fc-8105-1fcd91704a86",
  "isSidechain": false,
  "requestId": "req_011CazWuap3jhFFC42pSiEL2",
  "type": "assistant",
  "uuid": "56cfc7f8-8926-430b-b341-1d8f8e1a022a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS3ScB8y5xLuoVFGUEw3H7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 86433,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 86433,
          "cache_creation_input_tokens": 1112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1112
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-13T11:49:18.960Z_

<details><summary>↩ Tool result · `toolu_01UvRYZkhRztHxNyf4Ys8a3k`</summary>

```text
Web search results for query: ""self-distillation" "sometimes degrade" reasoning LLM 2603 arxiv feedback loop EMA"

Links: [{"title":"[2603.24472] Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?","url":"https://arxiv.org/abs/2603.24472"},{"title":"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?","url":"https://arxiv.org/html/2603.24472v1"},{"title":"[2603.24472v1] Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?","url":"https://arxiv.org/abs/2603.24472v1"},{"title":"Paper page - Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?","url":"https://huggingface.co/papers/2603.24472"},{"title":"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.24472"},{"title":"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? [Quick Review]","url":"https://liner.com/review/why-does-selfdistillation-sometimes-degrade-reasoning-capability-llms"},{"title":"1 Introduction","url":"https://arxiv.org/html/2605.06597"},{"title":"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.24472"},{"title":"[2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models","url":"https://arxiv.org/abs/2601.18734"},{"title":"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?","url":"https://www.researchgate.net/publication/403153841_Why_Does_Self-Distillation_Sometimes_Degrade_the_Reasoning_Capability_of_LLMs"}]

I found the paper you're looking for! Here's what the search results show:

The arXiv paper 2603.24472 titled "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?" addresses how self-distillation can reduce response length while degrading performance in mathematical reasoning, tracing this degradation to the suppression of epistemic verbalization - the model's expression of uncertainty during reasoning.

The research shows that conditioning the teacher on rich information suppresses uncertainty expression, enabling rapid in-domain optimization with limited task coverage but harming out-of-distribution performance, where unseen problems benefit from expressing uncertainty and adjusting accordingly.

Notably regarding the feedback loop you asked about: A moving target teacher, even with slow EMA (exponential moving average) updates, amplifies epistemic suppression through a feedback loop, where the student learns from an increasingly confident teacher, leading to greater performance degradation. Fixing the teacher to the initial policy yields better performance.

The researchers observe performance drops of up to 40% across Qwen3-8B, DeepSeek-Distill-Qwen-7B, and Olmo3-7B-Instruct.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56cfc7f8-8926-430b-b341-1d8f8e1a022a",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "747aea40-bcbc-4e31-99ab-648fc8a5e74f",
  "toolUseResult": {
    "query": "\"self-distillation\" \"sometimes degrade\" reasoning LLM 2603 arxiv feedback loop EMA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DVAi7zNnF37PFcGgKHa19D",
        "content": [
          {
            "title": "[2603.24472] Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?",
            "url": "https://arxiv.org/abs/2603.24472"
          },
          {
            "title": "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?",
            "url": "https://arxiv.org/html/2603.24472v1"
          },
          {
            "title": "[2603.24472v1] Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?",
            "url": "https://arxiv.org/abs/2603.24472v1"
          },
          {
            "title": "Paper page - Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?",
            "url": "https://huggingface.co/papers/2603.24472"
          },
          {
            "title": "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.24472"
          },
          {
            "title": "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? [Quick Review]",
            "url": "https://liner.com/review/why-does-selfdistillation-sometimes-degrade-reasoning-capability-llms"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2605.06597"
          },
          {
            "title": "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.24472"
          },
          {
            "title": "[2601.18734] Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models",
            "url": "https://arxiv.org/abs/2601.18734"
          },
          {
            "title": "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?",
            "url": "https://www.researchgate.net/publication/403153841_Why_Does_Self-Distillation_Sometimes_Degrade_the_Reasoning_Capability_of_LLMs"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search results show:\n\nThe arXiv paper 2603.24472 titled \"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?\" addresses how self-distillation can reduce response length while degrading performance in mathematical reasoning, tracing this degradation to the suppression of epistemic verbalization - the model's expression of uncertainty during reasoning.\n\nThe research shows that conditioning the teacher on rich information suppresses uncertainty expression, enabling rapid in-domain optimization with limited task coverage but harming out-of-distribution performance, where unseen problems benefit from expressing uncertainty and adjusting accordingly.\n\nNotably regarding the feedback loop you asked about: A moving target teacher, even with slow EMA (exponential moving average) updates, amplifies epistemic suppression through a feedback loop, where the student learns from an increasingly confident teacher, leading to greater performance degradation. Fixing the teacher to the initial policy yields better performance.\n\nThe researchers observe performance drops of up to 40% across Qwen3-8B, DeepSeek-Distill-Qwen-7B, and Olmo3-7B-Instruct."
    ],
    "durationSeconds": 5.093437007999979
  },
  "sourceToolAssistantUUID": "56cfc7f8-8926-430b-b341-1d8f8e1a022a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 173 · 2026-05-13T11:49:22.219Z_

This confirms a key risk the proposal acknowledges — EMA feedback loops. Now let me consolidate all findings into the final review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "747aea40-bcbc-4e31-99ab-648fc8a5e74f",
  "isSidechain": false,
  "requestId": "req_011CazWvECLYwN3LvkMWBWrR",
  "type": "assistant",
  "uuid": "129c5982-cd6b-422e-bc75-0c2a5bf1b2b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S81kWKtEPhA66R1Jy6V14m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 87545,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 87545,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-13T11:49:22.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eg8RCxyUQmDTSX4CEFs8EK`</summary>

```json
{
  "query": "CoRL 2026 paper acceptance rate real robot experiments simulation-only policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "129c5982-cd6b-422e-bc75-0c2a5bf1b2b7",
  "isSidechain": false,
  "requestId": "req_011CazWvECLYwN3LvkMWBWrR",
  "type": "assistant",
  "uuid": "ba48e683-93ba-4c86-b8b5-4c5c26709d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S81kWKtEPhA66R1Jy6V14m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 87545,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 87545,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-13T11:49:27.825Z_

<details><summary>↩ Tool result · `toolu_01Eg8RCxyUQmDTSX4CEFs8EK`</summary>

```text
Web search results for query: "CoRL 2026 paper acceptance rate real robot experiments simulation-only policy"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2025 - Call for Papers","url":"https://2025.corl.org/contributions/call-for-papers"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2026 - Awards","url":"https://www.corl.org/program/awards"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"Call for Papers – CORL 2022","url":"https://corl2022.org/call-for-papers/"}]

Based on the search results, I can provide you with information about CoRL 2026's policies regarding robot experiments and simulation:

## Real Robot Experiments and Simulation Policies

Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. This reflects CoRL's emphasis on practical robotics research and the importance of demonstrating real-world applicability.

The conference guidelines clarify that simulation-only work is acceptable if it convincingly demonstrates transferability to real robots. For example, in guidance from previous years, papers are noted as satisfying requirements if they show sim-to-real transfer capabilities (such as autonomous driving in simulation environments like CARLA).

## Paper Acceptance Rate

Unfortunately, the search results do not contain information about CoRL 2026's paper acceptance rate. The results reference acceptance rates from other years (such as CoRL 2024), but specific statistics for CoRL 2026 are not yet available in the search results. If you need this information, you may want to check the OpenReview portal directly at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference once decisions have been announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba48e683-93ba-4c86-b8b5-4c5c26709d24",
  "isSidechain": false,
  "promptId": "42ca653a-3bab-4928-ac0b-fe8cc5d4e06f",
  "type": "user",
  "uuid": "dadf66b6-d5ca-44c4-a3ff-5a3c8f30a64a",
  "toolUseResult": {
    "query": "CoRL 2026 paper acceptance rate real robot experiments simulation-only policy",
    "results": [
      {
        "tool_use_id": "srvtoolu_011MJcUYgrE39dbwfuEENUTU",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more",
            "url": "https://github.com/smallfryy/corl-2025-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2025 - Call for Papers",
            "url": "https://2025.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2024 - Instruction for Reviews",
            "url": "https://2024.corl.org/contributions/instruction-for-reviews"
          },
          {
            "title": "CoRL 2026 - Awards",
            "url": "https://www.corl.org/program/awards"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2024 Accepted Paper List - Paper Copilot",
            "url": "https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"
          },
          {
            "title": "Call for Papers – CORL 2022",
            "url": "https://corl2022.org/call-for-papers/"
          }
        ]
      },
      "Based on the search results, I can provide you with information about CoRL 2026's policies regarding robot experiments and simulation:\n\n## Real Robot Experiments and Simulation Policies\n\nAuthors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. This reflects CoRL's emphasis on practical robotics research and the importance of demonstrating real-world applicability.\n\nThe conference guidelines clarify that simulation-only work is acceptable if it convincingly demonstrates transferability to real robots. For example, in guidance from previous years, papers are noted as satisfying requirements if they show sim-to-real transfer capabilities (such as autonomous driving in simulation environments like CARLA).\n\n## Paper Acceptance Rate\n\nUnfortunately, the search results do not contain information about CoRL 2026's paper acceptance rate. The results reference acceptance rates from other years (such as CoRL 2024), but specific statistics for CoRL 2026 are not yet available in the search results. If you need this information, you may want to check the OpenReview portal directly at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference once decisions have been announced."
    ],
    "durationSeconds": 4.888314223000081
  },
  "sourceToolAssistantUUID": "ba48e683-93ba-4c86-b8b5-4c5c26709d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 176 · 2026-05-13T11:50:35.925Z_

Now I have enough information to produce a thorough review. Let me synthesize all findings.

Based on my extensive independent research — 20+ searches, multiple deep reads — here is my review:

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The gap is real but narrower than presented. iw-SFT already uses EMA for continuous control SFT; RAPID's novelty is the specific combination of reducible loss decomposition (from RHO-LOSS/ReLo) + PER-style sampling + application to VLA SFT. Each component exists; the integration and domain transfer is the contribution. The 'first to test SFT data quality → RL for VLAs' claim is weakened by PEAR (2602.01058) and DC-SFT (2602.10815) studying exactly SFT→RL cascading for LLMs/VLMs, plus the ICML 2026 clipping paper for LLM agents."},
    "feasibility": {"score": 3, "rationale": "The CoRL sprint (950 GPU-hours in ~14 days) is extremely tight but technically possible with existing infrastructure (OpenVLA-OFT trains in 1-2 days on 8×A100). The go/no-go by May 22 is honest. However, the RAPID+RL experiment (Contribution 3, the headline) requires untested SimpleVLA-RL integration with custom SFT checkpoints — debugging this alone could consume the entire timeline. AAAI 2027 timeline is realistic."},
    "clarity": {"score": 4, "rationale": "The proposal is exceptionally well-structured after 6 rounds of revision. The landscape analysis is comprehensive, positioning is mostly honest, and the experimental plan is detailed with explicit risk management (go/no-go dates, CoRL vs AAAI fallback). The three contributions are clearly delineated."},
    "impact": {"score": 3, "rationale": "The SFT→RL cascade finding would be impactful IF it materializes with compelling numbers, but it's the untested headline contribution. On clean LIBERO (97%+ baseline), gains will be marginal per 'When Do Curricula Work?' finding. The noise-injection setting is a controlled mechanism test, not a real-world demonstration. The practical impact depends on whether real-world VLA datasets are noisy enough for RAPID to matter — currently undemonstrated."}
  },
  "issues": [
    "MISSING REFERENCE (HIGH PRIORITY): 'Good SFT Optimizes for SFT, Better SFT Prepares for Reinforcement Learning' (arXiv 2602.01058, Feb 2026) proposes PEAR — an SFT-stage importance-sampling loss reweighting method that explicitly optimizes SFT for downstream RL outcomes. This paper directly studies how SFT technique (loss reweighting) affects downstream RL for LLMs, closely overlapping with RAPID's Contribution 3 ('SFT data quality → RL outcomes'). PEAR operates at token/block/sequence level with importance weights; RAPID operates at demonstration level with reducible loss priorities. Must be cited and differentiated. RAPID's claim of 'first to study SFT data quality → RL' is now further weakened — reframe as 'first to study noise-filtering prioritized sampling during VLA SFT for downstream RL.'",
    "MISSING REFERENCE (HIGH PRIORITY): 'Why Does RL Generalize Better Than SFT? A Data-Centric Perspective on VLM Post-Training' (arXiv 2602.10815, Feb 2026) proposes DC-SFT — static difficulty-based data filtering during SFT that *surpasses RL* performance on OOD tasks. The core insight is identical to RAPID's: filtering hard/noisy samples from SFT training improves outcomes. DC-SFT uses correctness-based difficulty categorization (static, pre-training); RAPID uses reducible loss (online, during training). DC-SFT targets VLM reasoning; RAPID targets VLA manipulation. This paper strengthens RAPID's motivation (data filtering during SFT matters) but narrows its novelty (the principle is already demonstrated). Must be cited.",
    "MISSING REFERENCE: QoQ — 'Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning' (arXiv 2603.09056, ICRA 2026). Static influence-function-based demonstration curation specifically for VLA/robot learning with billion-parameter models. Directly relevant to the static curation baseline landscape. The proposal cites CUPID but not QoQ, which is the more recent and VLA-specific influence function work.",
    "NOVELTY CEILING: The proposal's three contributions are each partially anticipated: (1) EMA-based reducible loss — iw-SFT uses EMA for continuous control, ReLo uses Polyak-averaged target for reducible loss in RL, RHO-LOSS/Rho-1 use reducible loss in supervised learning; (2) noise-robust SFT — DC-SFT filters noisy/hard samples from SFT, RINSE uses smoothness metrics, Green-VLA's DataQA pipeline filters demonstrations; (3) SFT quality → RL cascade — PEAR, the ICML 2026 clipping paper, 'Tailored Primitive Initialization', and PRISM all study how SFT technique/quality affects downstream RL. RAPID's unique combination (online reducible-loss PER for VLA SFT + downstream RL testing) is valid but the contribution per component is incremental.",
    "THEORETICAL TESTABILITY REMAINS WEAK: The finite-T bounds (Corollary 1.1) depend on constants C₁, C₂ tied to loss landscape properties (Lipschitz constant, gradient bound) that cannot be estimated a priori for VLA models. The proposal acknowledges this but the 'qualitative prediction' framing (linear vs quadratic growth) may not be testable in short VLA SFT runs (1-3 epochs, ~500 demos). If the bound gap doesn't manifest empirically, the theory section loses its anchor.",
    "CoRL FEASIBILITY RISK: The RAPID+RL experiment (Contribution 3, the headline) requires integrating RAPID SFT checkpoints with SimpleVLA-RL's GRPO pipeline — a nontrivial engineering task on an untested code path. If this integration fails or produces inconclusive results by May 22, the CoRL submission falls back to Contributions 1-2 only, which are weaker without the RL cascade story."
  ],
  "feedback": "The proposal has reached a high level of polish and landscape comprehensiveness after 6 rounds. The remaining path to 'pass' requires addressing two newly discovered missing references and honestly confronting the narrowing novelty:\n\n**1. Cite PEAR (2602.01058) and DC-SFT (2602.10815) — these are the most critical additions.** Both papers from Feb 2026 directly study how SFT data quality/filtering affects downstream outcomes. PEAR uses importance-sampling loss reweighting during SFT to prepare for RL (LLM domain). DC-SFT filters hard samples from SFT to surpass RL performance (VLM domain). Together with the ICML 2026 clipping paper (already cited), these form a clear trend: 'SFT quality for RL' is an active research direction, not a gap. Reframe RAPID as: 'We bring this principle to VLA manipulation with a noise-robust, online mechanism (reducible loss PER) rather than static correctness-based filtering (DC-SFT) or token-level reweighting (PEAR).' This is still a valid contribution — online adaptivity and noise robustness via reducible loss decomposition differentiate RAPID from all of these.\n\n**2. Cite QoQ (2603.09056, ICRA 2026).** This is a 2026 VLA-specific influence-function curation method. Add it alongside CUPID and DataMIL in the static curation baseline section.\n\n**3. Reframe Contribution 3 more narrowly.** Instead of 'first empirical test of whether SFT data quality affects downstream RL for VLAs,' state: 'first empirical test of whether *noise-filtering prioritized sampling* during VLA SFT improves downstream RL convergence — complementing concurrent findings in LLMs (PEAR, ICML 2026 clipping) and VLMs (DC-SFT) by demonstrating the principle extends to continuous action prediction with a different mechanism.'\n\n**4. Strengthen the DC-SFT comparison.** DC-SFT's static filtering already surpasses RL for VLM reasoning. RAPID's key advantages over DC-SFT: (a) online adaptation to the policy's evolving learning state (DC-SFT filters once before training), (b) noise robustness via reducible loss (DC-SFT uses correctness labels, unavailable for continuous action prediction), (c) applicability to VLA where binary correctness is undefined. This is actually a strong differentiator — make it explicit.\n\n**5. For the CoRL sprint, prioritize the RAPID+RL experiment.** If you can show even a modest improvement (e.g., 20-30% fewer RL steps to 90% success), it transforms the narrative. Without it, the paper is 'another data curation method' competing with QoQ, SCIZOR, CUPID, RINSE, DataMIL, and Green-VLA's DataQA — a crowded space.\n\n**Bottom line:** The proposal needs to acknowledge that 'SFT quality for RL' is now a recognized research direction (PEAR, DC-SFT, ICML 2026 clipping, Tailored Primitive Initialization), not an untouched gap. RAPID's contribution is the specific mechanism (online reducible-loss PER) and domain (VLA continuous control) — which is valid but must be positioned honestly against this landscape. With these 2-3 additional citations and reframing, the average score could reach 3.5, but reaching 4.0 requires compelling empirical results (especially the RAPID+RL finding) that don't yet exist.",
  "reason": "Novelty narrowed by uncited PEAR (2602.01058) and DC-SFT (2602.10815) studying SFT filtering→RL for LLMs/VLMs; the 'SFT quality for RL' gap is no longer untouched. Core mechanism is sound but incremental — each component (reducible loss, EMA reference, PER sampling, SFT→RL cascade) exists in prior work. Impact hinges on untested RAPID+RL experiment."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dadf66b6-d5ca-44c4-a3ff-5a3c8f30a64a",
  "isSidechain": false,
  "requestId": "req_011CazWvtCLg46KCs5hYkoow",
  "type": "assistant",
  "uuid": "dc8591b1-ed1a-4835-9ac5-3eb1b42d39bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4WMpN22KeEyS2PUn4Fc1w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 88509,
      "output_tokens": 2598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2598,
          "cache_read_input_tokens": 88509,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 177_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "dc8591b1-ed1a-4835-9ac5-3eb1b42d39bb",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---

### Runtime record

_source line 178_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA data quality filtering for SFT→RL pipelines",
  "sessionId": "c910c13d-bae5-469c-bad4-44d932f7b20c"
}
```

---
