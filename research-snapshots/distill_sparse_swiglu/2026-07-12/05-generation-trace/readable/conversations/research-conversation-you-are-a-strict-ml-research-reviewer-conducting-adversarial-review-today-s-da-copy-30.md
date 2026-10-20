# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/79b7d0a3-cb81-4607-9e85-3b5600200248.jsonl`
- **Structured JSON:** [`f0255efb4e60285467fb.json`](../../sessions/f0/f0255efb4e60285467fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T17:37:30.914Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T17:37:30.914Z",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\nDirection：因为真实数据采样的时候会有很多噪声，比如收集时的冗余动作等，如何避免训练数据中的噪声影响vla的训练，可以使用一个经验池的形式来训练，借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选，再适当过滤掉一些低分数的冗余动作，如果是从一些底层理论角度提出了筛选方法 感觉不用真机也是可以接受的**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Chunk-Decomposed Adaptive Prioritization for VLA Supervised Fine-Tuning\",\n  \"core_problem\": \"Can we exploit the temporal structure of action-chunk prediction losses — which reveals *why* each demonstration transition is hard, not just *how* hard it is — to design a VLA-specific adaptive prioritization mechanism for SFT that outperforms both generic loss-based sampling and existing adaptive scalar-MSE reweighting (AdaMix)?\",\n  \"opportunity\": \"Every existing demonstration curation method (SCIZOR, CUPID, DataMIL, DemInf, RINSE) operates as a static filter-then-train preprocessing step, while every existing online prioritization method treats the training loss as a scalar priority signal — even when applied to sequential predictions. This includes AdaMix (EMMA, 2025), the most relevant prior work, which adaptively reweights VLA training samples based on aggregated MSE over action chunks, trajectory smoothness, and joint angle constraints — but reduces the chunk prediction loss to a single scalar before reweighting. VLA models with action chunking produce a uniquely structured loss signal: for each transition, the model predicts K future actions [a_1, ..., a_K], yielding a per-position loss vector [l_1, ..., l_K] that encodes *temporal prediction quality*. This vector is discarded when aggregated into a scalar mean loss. Yet it carries critical information: a transition where the first actions are correct but the chunk diverges mid-way (high temporal divergence) represents a temporal coherence challenge — the model has learned the local dynamics but fails to propagate them forward. A transition where all K actions are uniformly wrong (low temporal divergence, high aggregate) represents a fundamental perception or grounding failure. These require fundamentally different amounts of training focus, and the optimal treatment shifts during training: early on, most chunks are uniformly wrong; as training progresses, the model learns initial actions first and temporal coherence becomes the dominant bottleneck. This structured evolution has no analogue in LLM token prediction and cannot be captured by scalar prioritization.\\n\\nThe second VLA-specific opportunity is task phase structure: robot manipulation has identifiable critical phases (approach → grasp → transport → place) marked by gripper state transitions. Contact-phase transitions are brief but disproportionately important for task success, as shown empirically by DAM-VLA's asymmetric Gaussian weighting. However, both DAM-VLA (fixed Gaussian) and AdaMix (uniform across phases) apply the same weighting scheme to all transitions regardless of task phase. An adaptive mechanism that identifies which specific contact-phase transitions the current policy still struggles with would be more sample-efficient.\\n\\nThe parallel to recent work in LLM SFT is instructive: Token Cleaning (ICML 2025) showed that sub-sample-level (token-level) quality varies significantly within samples for LLM SFT, and that filtering at the token level outperforms sample-level filtering. CDAP applies the analogous insight to VLA SFT: position-level difficulty varies within action chunks, and prioritizing at the chunk-decomposed level outperforms sample-level scalar reweighting.\\n\\nNo existing work exploits the *intra-chunk temporal loss profile* as an adaptive priority signal for VLA training data selection. AdaMix reweights samples adaptively but uses scalar-aggregated MSE; DAM-VLA uses intra-chunk structure but applies fixed weights; Token Cleaning uses sub-sample structure but in discrete LLM token spaces. CDAP fills this specific intersection: adaptive online prioritization that decomposes the continuous action-chunk loss into temporal components capturing *why* transitions are hard.\",\n  \"landscape\": \"**Static demonstration curation (the dominant paradigm):** SCIZOR (ICRA 2026) uses self-supervised progress prediction to filter suboptimal/redundant transitions, achieving 32.9% gains on Sirius-Fleet and 5.4% on RoboMimic. CUPID (CoRL 2025) and QoQ (arXiv 2026) use influence functions to score demonstrations. DataMIL (ICLR 2026) trains datamodels to predict which data subsets improve success. DemInf (RSS 2025) estimates mutual information for quality scoring. RINSE (ICML 2025, arXiv:2604.23000) proposes smoothness-based metrics (Spectral Arc Length + Trajectory-Envelope Distance), achieving 16% higher success with 1/6 data on RoboMimic and 20% improvement with half data on real-world manipulation. Re-Mix (CoRL 2024) optimizes domain-level data mixtures via DRO. All operate as filter-then-train pipelines: the curation is fixed before training begins.\\n\\n**Adaptive sample reweighting for VLA SFT (most direct competitor):** EMMA/AdaMix (arXiv:2509.22407, Sep 2025, revised Mar 2026) introduces a hard-sample-aware training strategy for VLA models that adaptively reweights samples during SFT based on three metrics: (1) Action Prediction Error — MSE aggregated over the full action chunk: r_i^MSE = -(1/L) Σ ||â_{i+t} - a_{i+t}||²₂, (2) Trajectory Smoothness — second-order joint angle differences penalizing abrupt actions, and (3) Joint Angle Limitation — binary safety constraint. These are min-max normalized and combined via arithmetic mean into a composite score s_i, with sampling probability p(i) ∝ γ + λ·(1 − s_i). Built on the π₀ backbone, AdaMix achieves 13% improvement over uniform sampling on real-world tasks. The paper was submitted to ICLR 2026 but withdrawn; it remains an arXiv preprint. **Critical differentiation from CDAP:** AdaMix computes MSE *aggregated over the full action chunk* (scalar), then reweights — it does not decompose per-position losses within the chunk. Its trajectory smoothness metric operates on ground-truth joint angles, not on the model's prediction quality at each temporal position. CDAP's temporal divergence δ_i captures a fundamentally different signal: how the *model's prediction quality degrades* over the chunk horizon, which is invisible to aggregated MSE. A chunk where positions 1-4 are correct and positions 5-8 diverge has the same aggregated MSE as a chunk where all positions have moderate error, but represents a qualitatively different learning challenge.\\n\\n**Online Hard Example Mining (the 10-year-old precursor):** OHEM (Shrivastava et al., CVPR 2016) selects the highest-loss examples in each mini-batch for gradient updates in object detection. Focal Loss (Lin et al., ICCV 2017) down-weights easy examples via a modulating factor. Both use scalar loss magnitude as the difficulty signal and operate within-batch without cross-batch priority tracking. CDAP differs in three ways: (1) uses chunk-decomposed loss structure, not scalar magnitude; (2) maintains a persistent priority buffer with IS correction for across-batch prioritization; (3) adapts priorities online as the policy evolves.\\n\\n**Prioritized Experience Replay (PER) and its descendants:** Schaul et al. (ICLR 2016) introduced sum-tree priority buffers with IS correction for RL. OPER (TNNLS 2024) applies PER to offline RL including BC on D4RL — but computes priorities statically via a decoupled two-stage procedure requiring reward signals. AFBC (arXiv 2021) uses advantage estimates for BC prioritization — also reward-dependent and static. Freshness-Aware PER (arXiv April 2026) successfully extends PER to billion-parameter LLM/VLM RL training with exponential age decay addressing priority staleness — but exclusively targets reward-dependent RL post-training. None of these decompose the loss signal by temporal structure within action chunks.\\n\\n**Adaptive importance weighting for SFT (iw-SFT):** iw-SFT (arXiv 2507.12856) establishes that SFT on curated data maximizes a lower bound on the RL objective and introduces adaptive importance weights via policy ratios with EMA-tracked reference parameters (θ_q = αθ_q + (1−α)θ). Evaluates on D4RL locomotion, Ant-maze, and Franka Kitchen. **Critical differentiation:** iw-SFT's importance weights are *policy ratios* — they measure how far the current policy has drifted from the reference distribution. In continuous VLA action spaces (7-DoF or higher), policy ratios via Gaussian likelihoods are numerically unstable and dominated by minor mean shifts in low-variance dimensions. CDAP's chunk-decomposed loss directly measures *where and why* the policy fails, providing a more informative and stable signal in high-dimensional continuous action spaces.\\n\\n**Sub-sample-level data selection for LLM SFT:** Token Cleaning (ICML 2025 Spotlight, arXiv:2502.01968) investigates token quality from a noisy-label perspective and proposes token-level data selection for LLM SFT by examining the influence of model updates on each token, then applying threshold-based separation. This is the closest *conceptual* parallel to CDAP in the LLM domain: both move beyond sample-level to sub-sample-level quality assessment during SFT. The key difference is domain: Token Cleaning operates on discrete tokens in language sequences where quality is about informativeness vs. noise, while CDAP operates on continuous action predictions where quality has temporal structure (prediction quality degrades systematically with temporal distance from the current observation). ProFit (arXiv:2601.09195) selectively masks low-probability tokens during LLM SFT. PEAR (arXiv:2602.01058) uses IS reweighting at token/block/sequence level. PBS (arXiv:2602.17066) predicts per-sample loss from static token features. SuRe (arXiv:2511.22367) uses sequence-level NLL surprise for prioritized replay. All target discrete token prediction in LLMs and have no mechanism for handling continuous action chunks or temporal prediction quality degradation.\\n\\n**VLA-specific loss weighting:** DAM-VLA (arXiv March 2026) introduces dual-scale action weighting: trajectory-level asymmetric Gaussian weights centered on gripper state transitions (σ_l=6, σ_r=2) and chunk-level exponential decay. This is the closest work to CDAP's contact-phase awareness, but DAM-VLA applies *fixed, universal* loss weights to all transitions equally — it does not adaptively select which transitions to prioritize based on current policy performance. CDAP uses contact-phase proximity as one component of an *adaptive* priority that evolves with the policy.\\n\\n**VLA action chunk analysis at inference time:** 'VLA Knows Its Limits' (arXiv Feb 2026) reveals that intra-chunk actions attend invariantly to vision-language tokens and prediction quality degrades systematically with temporal distance, with 'action sinks' at initial and terminal positions. AutoHorizon dynamically estimates execution horizons from attention patterns. VGAS (arXiv:2602.07399, Feb 2026) introduces Q-Chunk-Former, a geometrically grounded Transformer critic, for value-guided action-chunk selection at inference time via best-of-N selection, resolving geometric ambiguities among candidate chunks. Both support CDAP's premise that intra-chunk temporal structure is informative, but address inference-time execution (AutoHorizon: execution horizons; VGAS: chunk selection), not training-time data prioritization.\\n\\n**Gap:** No existing work exploits the *intra-chunk temporal loss profile* as an adaptive priority signal for VLA SFT. Static curation methods (SCIZOR, RINSE) ignore training dynamics. Scalar-loss adaptive methods (AdaMix, OHEM, PER, iw-SFT) discard the temporal structure within chunks — AdaMix is the closest, performing adaptive reweighting during VLA SFT, but aggregates chunk MSE into a scalar before reweighting. Fixed-weighting methods (DAM-VLA) don't adapt to individual transition difficulty. LLM sub-sample methods (Token Cleaning, ProFit, PEAR, PBS) don't handle continuous action chunks. Inference-time chunk analysis methods (VGAS, AutoHorizon) don't address training-time prioritization. CDAP fills this intersection.\",\n  \"approach\": \"We propose CDAP (Chunk-Decomposed Adaptive Prioritization), replacing scalar loss-based sampling with a VLA-specific priority signal that exploits the temporal structure of action-chunk prediction losses during SFT. CDAP requires no auxiliary model, no reward annotations, and adds <3% compute overhead.\\n\\n**1. Chunk Temporal Profile (CTP) — the VLA-specific priority signal:**\\nDuring VLA SFT with action chunking (chunk size K), each transition i produces per-position L1 losses [l_{i,1}, ..., l_{i,K}] from the predicted vs. ground-truth action chunk. Instead of discarding this structure into a scalar mean (as AdaMix does with MSE), CDAP computes a two-component priority:\\n\\n(a) *Aggregate difficulty*: μ_i = (1/K) Σ_k l_{i,k} — overall prediction quality, analogous to AdaMix's aggregated MSE and standard loss-based priority.\\n\\n(b) *Temporal divergence*: δ_i = (1/(K−1)) Σ_{k=1}^{K−1} ReLU(l_{i,k+1} − l_{i,k}) — average positive slope of per-position losses, measuring how much prediction quality degrades over the chunk horizon. High δ_i indicates a temporal coherence challenge (initial actions correct, chunk diverges mid-way); low δ_i with high μ_i indicates a fundamental perception/grounding failure.\\n\\nWe also study alternative temporal metrics: loss variance within chunk (Var(l_{i,1}, ..., l_{i,K})), loss range (max − min), and Spearman correlation between position index and loss. The ablation identifies which temporal metric best captures learning-relevant structure.\\n\\n**2. Contact-Phase Aware Weighting:**\\nGripper state transitions (open→close, close→open) are identified directly from demonstration data (no model needed). Transitions within a window w of a gripper state change receive a multiplicative contact-phase boost: c_i = 1 + η if transition i is within w steps of a gripper transition, else c_i = 1. This is grounded in DAM-VLA's empirical finding that contact phases are critical for manipulation success, but unlike DAM-VLA's fixed Gaussian or AdaMix's phase-agnostic reweighting, CDAP combines this with adaptive difficulty-based selection: among all contact-phase transitions, CDAP prioritizes those the current policy still finds hard.\\n\\n**3. Priority Function and Sampling:**\\nThe composite priority for transition i is:\\n  p(i) = (μ_i + ε)^{α_μ} · (1 + γ · δ_i)^{α_δ} · c_i\\n\\nwhere α_μ controls aggregate-loss prioritization strength, α_δ controls temporal-divergence prioritization strength, and γ scales the divergence contribution. Setting α_δ = 0 recovers scalar-loss PER (OHEM+IS), enabling clean ablation against AdaMix's scalar approach. Transitions are sampled from a sum-tree buffer with probability proportional to p(i).\\n\\n**4. Importance-Sampling Correction:**\\nFollowing Schaul et al. and iw-SFT's theoretical framework, apply capped IS weights w_i = (N · p(i)/Σp)^{−β} with β annealed from β_0 to 1.0 over training. This ensures unbiased gradient estimates while maintaining the theoretical link to RL objective bounds established by iw-SFT. The key distinction: iw-SFT's weights correct for the ratio between behavior and current policy distributions (policy-ratio-based), while CDAP's weights correct for the ratio between the adaptive chunk-decomposed priority distribution and the uniform distribution (loss-structure-based). Both are valid IS schemes with different inductive biases.\\n\\n**5. Freshness-Aware Age Decay:**\\nAdopt Freshness-Aware PER's exponential age decay: p_eff(i) = p(i) · exp(−λ · age_i), where age_i counts steps since transition i was last sampled. This addresses priority staleness at VLA scale.\\n\\n**6. Lazy Updates with Coverage-Guaranteed Mixing:**\\nPriorities are updated lazily when sampled (loss is computed anyway for gradient updates, and the per-position losses [l_{i,1}, ..., l_{i,K}] are available at zero additional cost from the chunk prediction). With probability ε_mix, sample uniformly to ensure buffer coverage. We set ε_mix adaptively: ε_mix = max(ε_min, 1 − coverage_t) where coverage_t is the current fraction of transitions sampled at least once.\\n\\n**7. Empirical Hypotheses and Analysis (replacing overstated theoretical claims):**\\nInstead of claiming formal theorems, we formulate testable hypotheses motivated by the structure of action-chunk prediction, and provide the first systematic empirical investigation:\\n\\n(a) *Hypothesis 1 — Temporal profile evolution*: Under VLA SFT with action chunking of size K, the per-position loss profile [l_1(θ), ..., l_K(θ)] evolves from approximately flat (all positions equally hard early in training) to monotonically increasing (initial positions learned first, later positions remain hard). The rate of this transition depends on the temporal correlation structure of the demonstration data. We test this hypothesis by tracking per-position loss profiles across training for different transition types (contact vs. free-space, smooth vs. non-smooth demonstrations).\\n\\n(b) *Hypothesis 2 — Temporal divergence informativeness*: Transitions with similar aggregate difficulty μ but different temporal divergence δ have different downstream impact on task success, i.e., δ carries learning-relevant information beyond what μ captures. We test this by partitioning transitions into (μ, δ) bins and measuring per-bin gradient utility (cosine similarity with the full-data gradient).\\n\\n(c) *Variance reduction analysis*: For transitions exhibiting high temporal divergence (δ_i >> 0), we empirically measure whether gradient variance under chunk-decomposed prioritization is lower than under scalar-loss prioritization, and by how much. The intuition: when a chunk has heterogeneous per-position losses, scalar-loss PER may over- or under-prioritize depending on the aggregation, while chunk-decomposed prioritization places the transition at the appropriate priority for its *bottleneck* (the diverging later positions) rather than its *average*.\\n\\n(d) *Contact-phase sample complexity*: We empirically measure whether contact-phase boosted sampling reduces the number of gradient steps to reach a given contact-phase loss threshold compared to uniform and scalar-adaptive sampling.\\n\\n**8. Implementation on OpenVLA-OFT:**\\nIntegrate CDAP into the OpenVLA-OFT fine-tuning pipeline. The per-position losses are already computed during the L1 regression forward pass for each action chunk — CDAP's CTP computation (mean + temporal divergence) adds only K floating-point operations per transition, truly negligible overhead. The sum-tree priority buffer replaces the uniform DataLoader sampler. Implementation is ~150 lines of code.\\n\\n**9. Evaluation — Benchmarks:**\\n(a) Sirius-Fleet: real-world mixed-quality fleet data where data quality is the established bottleneck (SCIZOR showed 32.9% absolute gains). (b) RoboMimic multi-human (MH): explicit mixed-quality operators. (c) OXE subsets (Bridge, RT-1, DROID): cross-site quality heterogeneity. (d) SimplerEnv: VLA-specific evaluation.\\n\\n**10. Evaluation — Baselines:**\\n(a) Uniform sampling (OpenVLA-OFT default). (b) SCIZOR (static progress-based filtering, ICRA 2026). (c) RINSE (static smoothness-based filtering, ICML 2025). (d) CUPID (static influence-based, CoRL 2025). (e) AdaMix (adaptive scalar-MSE + smoothness + joint limits reweighting during VLA SFT, EMMA arXiv 2025 — most direct competitor). (f) Scalar-loss PER (α_δ=0 ablation of CDAP — equivalent to OHEM + IS correction + age decay, isolating temporal decomposition's value vs. scalar-loss adaptive methods including AdaMix). (g) SCIZOR→CDAP and RINSE→CDAP (adaptive on top of static, demonstrating complementary benefit).\\n\\nThe ablation path cleanly isolates CDAP's contribution: Uniform → AdaMix (scalar adaptive, external baseline) → Scalar PER+IS (α_δ=0, our framework without temporal component) → Full CDAP (with temporal decomposition). If scalar PER+IS ≈ AdaMix, the frameworks are equivalent modulo IS correction and age decay. If full CDAP > scalar PER+IS, temporal decomposition adds value. This is the paper's make-or-break comparison.\\n\\n**11. Evaluation — Key Analyses (VLA-specific empirical contributions):**\\n(a) *Temporal loss profile evolution*: Visualize how the intra-chunk loss profile [l_1, ..., l_K] evolves during training across different types of transitions (contact vs. free-space, successful vs. failed demonstrations). This is the first systematic study of how per-position action chunk losses evolve during VLA SFT — the empirical investigation itself is a contribution regardless of whether CDAP outperforms all baselines.\\n(b) *Loss rank decorrelation*: Measure Spearman correlation between initial and final per-transition loss rankings, and separately for aggregate difficulty μ and temporal divergence δ, to quantify how much the optimal data distribution shifts and whether the shift is captured by scalar vs. decomposed priorities.\\n(c) *Buffer coverage analysis*: Track the fraction of transitions sampled at least once during training under different prioritization schemes, directly addressing the staleness concern.\\n(d) *Temporal divergence vs. aggregate difficulty decomposition*: Show that transitions with similar μ but different δ have different downstream impact on task success, validating the information content of the temporal profile.\\n(e) *Ablation over α_μ, α_δ, γ, η, w, λ, ε_mix, β schedule*.\\n(f) *Compute overhead profiling* at VLA scale (expected: <3% wall-clock, <1% GPU).\\n(g) *Pre-pilot on RoboMimic-MH*: Before committing to the full experimental pipeline, run a small-scale pilot comparing uniform vs. AdaMix vs. scalar PER (α_δ=0) vs. full CDAP on RoboMimic-MH to validate that δ carries learning-relevant signal. This de-risks the main experimental investment.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~500h A100-80GB (~8 baselines × 20h + ~8 method runs × 25h + ~10 ablations × 12h + ~30h analysis/visualization + ~20h AdaMix reimplementation)\",\n      \"gpu_utilization\": \"~30-40% effective utilization; GPUs idle during implementation, debugging, and analysis\",\n      \"timeline\": \"2-4 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$750 at ~$1.50/hr\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~650h A100-80GB (agent explores more hyperparameter configurations and temporal metric variants; human gates benchmark selection and analysis framing; includes AdaMix reimplementation and pilot study)\",\n      \"gpu_utilization\": \"~65-75% utilization; agent queues experiments overnight, human reviews results and approves next batch\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$120-250 (800-1500 turns: code generation, experiment orchestration, result analysis)\",\n      \"estimated_gpu_cost\": \"~$975 at ~$1.50/hr\",\n      \"risk_note\": \"Primary risk is that α_δ ablation shows temporal decomposition adds minimal value over scalar-adaptive methods. Pilot on RoboMimic-MH (included in estimate) de-risks this before full benchmark commitment.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~1000-1200h A100-80GB (comprehensive exploration of temporal metrics, hyperparameters, cross-benchmark analysis, and AdaMix reimplementation/comparison)\",\n      \"gpu_utilization\": \"~90-95% utilization; agent runs 24/7\",\n      \"timeline\": \"10-16 days with 8× A100 cluster\",\n      \"team\": \"0 (initial setup and final review only)\",\n      \"claude_api_cost\": \"$250-500 (1500-3000 turns for code, orchestration, ablation design, paper drafting)\",\n      \"estimated_gpu_cost\": \"~$1,650 at ~$1.50/hr\",\n      \"speed_bottleneck\": \"GPU cluster availability for 7B model fine-tuning; Sirius-Fleet simulation throughput for evaluation rollouts\",\n      \"risk_note\": \"Agent may over-explore temporal metric variants; risk of ~10% wasted compute. Timeline tight for CoRL 2026 (abstract May 26, paper May 28 EOD / May 29 11:59 UTC) but feasible given that core implementation is ~150 lines. Pilot study should be prioritized in first 2 days.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline: May 26, 2026 11:59 UTC; paper deadline: May 28, 2026 EOD Thursday per Instruction for Authors, or May 29, 2026 11:59 UTC per OpenReview — use conservative May 28 EOD for planning)\",\n    \"AAAI 2027 (deadline: expected ~Aug 2026)\",\n    \"ICRA 2027 (deadline: expected ~Sep 2026)\",\n    \"ICLR 2027 (deadline: expected ~Sep-Oct 2026)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Online Hard Example Mining (Shrivastava et al., CVPR 2016)\",\n    \"Focal Loss for Dense Object Detection (Lin et al., ICCV 2017)\",\n    \"Prioritized Experience Replay (Schaul et al., ICLR 2016)\",\n    \"OPER: Decoupled Prioritized Resampling for Offline RL (Yue et al., TNNLS 2024, arXiv:2306.05412)\",\n    \"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (arXiv:2110.04698, 2021)\",\n    \"Supervised Fine Tuning on Curated Data is Reinforcement Learning (iw-SFT, arXiv:2507.12856, 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)\",\n    \"DemInf: Robot Data Curation with Mutual Information Estimators (RSS 2025)\",\n    \"RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025, arXiv:2604.23000)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions (QoQ, arXiv 2026)\",\n    \"EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (arXiv:2509.22407, Sep 2025, revised Mar 2026) — introduces AdaMix adaptive sample reweighting for VLA SFT\",\n    \"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning (ICML 2025 Spotlight, arXiv:2502.01968)\",\n    \"SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv:2511.22367, 2025)\",\n    \"ProFit: Probability-Guided Token Selection for SFT (arXiv:2601.09195, Jan 2026)\",\n    \"PEAR: Good SFT Optimizes for SFT, Better SFT Prepares for RL (arXiv:2602.01058, Feb 2026)\",\n    \"PBS: Predictive Batch Scheduling for LLM Training (arXiv:2602.17066, Feb 2026)\",\n    \"Freshness-Aware Prioritized Experience Replay for LLM/VLM RL (arXiv:2604.16918, April 2026)\",\n    \"Prioritized Replay for RL Post-training (arXiv:2601.02648, Jan 2026)\",\n    \"DAM-VLA: Dynamic Action Model-Based VLA Framework (arXiv March 2026)\",\n    \"VLA Knows Its Limits (arXiv:2602.21445, Feb 2026)\",\n    \"VGAS: Value-Guided Action-Chunk Selection for Few-Shot VLA Adaptation (arXiv:2602.07399, Feb 2026)\",\n    \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks (arXiv:2509.23224, 2025)\",\n    \"CAPS: Context-Aware Priority Sampling for Enhanced Imitation Learning (ICRA 2025, arXiv:2503.01650)\",\n    \"OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models (arXiv 2025)\",\n    \"PLD: Self-Improving VLA Models via Residual RL (ICLR 2026)\",\n    \"ExpReS-VLA: Specializing VLA Models Through Experience Replay (arXiv:2511.06202, 2025)\",\n    \"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)\",\n    \"GREATS: Online Selection of High-Quality Data for LLM Training (NeurIPS 2024)\",\n    \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models (arXiv 2023)\"\n  ],\n  \"description\": \"We propose CDAP (Chunk-Decomposed Adaptive Prioritization) for VLA model SFT, exploiting a VLA-specific signal that existing adaptive methods discard: the temporal structure of per-position losses within action chunks. VLA models with action chunking predict K future actions per transition, producing a loss vector [l_1, ..., l_K] that encodes temporal prediction quality — high temporal divergence (early actions correct, chunk diverges mid-way) indicates temporal coherence challenges, while uniformly high loss indicates perception/grounding failure. CDAP uses a two-component priority: aggregate difficulty (standard) and temporal divergence (VLA-specific), combined with contact-phase-aware weighting that boosts transitions near gripper state changes. This provides a richer priority signal than scalar loss aggregation (OHEM, standard PER), scalar-MSE adaptive reweighting (AdaMix/EMMA), policy ratios (iw-SFT), or fixed weighting (DAM-VLA), while requiring zero additional compute — per-position losses are already available from the chunk prediction forward pass. Just as Token Cleaning (ICML 2025) revealed that token-level quality varies within samples for LLM SFT, we show that position-level difficulty varies within action chunks for VLA SFT — but in a continuous action space with temporal structure rather than discrete tokens. We formulate testable hypotheses about temporal loss profile evolution (from flat to monotonically increasing during training) and temporal divergence informativeness, providing the first systematic empirical characterization of how intra-chunk loss profiles evolve during VLA SFT. Evaluated on Sirius-Fleet, RoboMimic-MH, OXE subsets, and SimplerEnv against eight baselines including SCIZOR, RINSE, AdaMix, and scalar-loss PER (our own α_δ=0 ablation), the ablation path Uniform → AdaMix → Scalar PER+IS → Full CDAP cleanly isolates the contribution of temporal decomposition. CDAP is designed as a complementary add-on: SCIZOR→CDAP and RINSE→CDAP demonstrate gains on top of static filtering. A small-scale RoboMimic-MH pilot is recommended before full benchmark commitment to validate that δ carries learning-relevant signal beyond μ.\",\n  \"project_name\": \"chunk_decomposed_priority_vla\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING RELATED WORK: OPER (Decoupled Prioritized Resampling for Offline RL, arXiv:2306.05412, TNNLS) directly applies TD-error-based prioritized resampling to behavioral cloning — this is the closest prior work and is completely unacknowledged. AFBC (arXiv:2110.04698) repurposes PER for BC in noisy datasets. Goal-Conditioned BC with Prioritized Sampling (IEEE 2021) applies prioritized sampling to goal-conditioned BC. ExpReS-VLA (arXiv:2511.06202) uses prioritized replay buffer for VLA fine-tuning.\", \"CRITICAL FEASIBILITY: Goal-conditioned value function training via hindsight relabeling in offline settings is known to be unstable. GoFAR (NeurIPS 2022) explicitly showed that 'hindsight relabeling involves sensitive hyperparameter tuning that cannot be easily performed offline' and proposed avoiding value function estimation entirely. GCSL (ICLR 2022) similarly avoids value estimation for stability. The proposal assumes a stable V(s,g) can be trained on demonstrations — this is an untested and potentially unsound assumption.\", \"LIBERO SATURATION: OpenVLA-OFT achieves 97.1% average on LIBERO-4. Pi0.5 achieves 97.5%. There is virtually no headroom for improvement. LIBERO-Plus (arXiv:2510.13626) shows VLAs drop from 95% to <30% under perturbations, but this tests robustness to environmental variations, not data quality. The paper needs benchmarks where data quality is the actual bottleneck.\", \"MISSING RELATED WORK (non-critical): DemInf (RSS 2025, MI-based curation), Re-Mix (CoRL 2024, data mixture optimization via DRO), DMDR (TNNLS 2025, diffusion-based noisy demo restoration). Also, iw-SFT (arXiv:2507.12856) establishes that SFT on curated data optimizes an RL objective bound — this theoretical insight partially subsumes APER's claimed theoretical contribution.\", \"VENUE DEADLINE ERROR: CoRL 2026 paper deadline is May 28, 2026 AoE (Thursday), not May 29 as stated. The official CoRL site explicitly emphasizes 'the paper submission deadline is Thursday (5/28) EOD rather than Friday.'\", \"COMPUTE OVERHEAD UNDERESTIMATED: Maintaining a goal-conditioned value function, periodically retraining it, and recomputing TD errors over the full demonstration buffer during VLA-scale fine-tuning is significantly more than ~5% overhead. A 7B VLA model's forward pass is already expensive; adding value function training + full-buffer TD recomputation every K steps could easily be 15-30%.\", \"DataMIL venue is ICLR 2026 Poster (not arXiv 2025 as cited). QoQ appears to be ICRA 2026 (not arXiv 2026). OpenVLA-OFT may no longer be SOTA — Pi0.5 and SimpleVLA-RL have matched or exceeded it.\", \"TIMELINE RISK: 15 days to abstract deadline and 18 days to paper deadline. Implementing a stable goal-conditioned value function, integrating it with OpenVLA-OFT training, running 5+ baselines + ablations on LIBERO/RoboMimic/OXE, and writing the paper is extremely ambitious even for auto-research mode.\"]\nFeedback: The core direction (adaptive vs. static data curation during VLA training) addresses a real gap, but the specific instantiation via TD-error PER has serious problems. To make this viable for CoRL 2026:\n\n1. **Acknowledge and differentiate from OPER, AFBC, and ExpReS-VLA.** OPER is the most direct threat — it already uses TD-error-based prioritized resampling for BC. You must clearly articulate what APER adds beyond OPER applied to VLA-scale training. The novelty claim needs complete rewriting.\n\n2. **Replace the goal-conditioned value function with a more stable priority signal.** The V(s,g) + hindsight relabeling approach has documented instability in offline settings. Consider alternatives: (a) SCIZOR-style progress prediction as a priority signal (but updated periodically), (b) policy loss/gradient magnitude as priority (no auxiliary model needed), (c) embedding-space surprise via the VLA's own representations. These avoid the known instability of offline value function estimation.\n\n3. **Choose benchmarks where data quality is the bottleneck.** Drop LIBERO (saturated at 97%). Use: RoboMimic multi-human (explicitly has mixed-quality operators), OXE subsets with known quality variation, or Sirius-Fleet (where SCIZOR showed 32.9% gains). The evaluation must demonstrate improvement ON TOP of static filtering (SCIZOR → APER), not just vs. uniform sampling.\n\n4. **Quantify the adaptive advantage formally.** When does adaptive prioritization provably outperform static filtering? A theoretical analysis showing conditions under which adaptive > static (e.g., when the optimal data distribution is non-stationary w.r.t. policy parameters) would significantly strengthen the contribution and address the 'why not just filter once' concern.\n\n5. **Be honest about compute overhead.** Profile the actual cost of priority recomputation at VLA scale. If it's 15-30%, the value proposition weakens substantially — why not just run SCIZOR and train 15% longer?\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — UNDERSTATED OVERLAP WITH iw-SFT: The iw-SFT paper (arXiv:2507.12856) already implements adaptive importance weights with time-lagged EMA (θ_q = αθ_q + (1−α)θ) that track the evolving policy during SFT training, with IS correction and per-step clipping. It also evaluates on D4RL and Franka Kitchen manipulation tasks. APER's claimed theoretical contribution — that adaptive IS weights yield tighter bounds than static — is already the core result of iw-SFT ('As q(τ) → p(τ;θ) we have J_iw-SFT(θ) → J(θ)'). The differentiation from iw-SFT needs to be much clearer: what exactly does APER's loss-driven priority add beyond iw-SFT's policy-ratio-driven adaptive weights?\", \"MISSING COMPETING WORKS — SuRe (arXiv:2511.22367): Surprise-Driven Prioritised Replay for Continual LLM Learning uses NLL/loss-based priority scoring for replay buffer management in LLM training. This is conceptually very close to APER — both use the model's own prediction loss as a priority signal for data selection during training. Must be discussed.\", \"MISSING COMPETING WORKS — ProFit (arXiv:2601.09195, Jan 2026): Probability-Guided Token Selection for SFT selectively masks low-probability tokens during SFT training, achieving 3-10% gains. PEAR (arXiv:2602.01058, Feb 2026): Importance sampling reweighting at token/block/sequence level for SFT. PBS (arXiv:2602.17066, Feb 2026): Online loss prediction for batch scheduling in LLM training. All three perform online, loss/probability-based data prioritization during SFT — overlapping with APER's core contribution.\", \"WEAK THEORETICAL NOVELTY: The formal analysis described (gap bounded by cumulative KL divergence, Lipschitz continuity implies adaptive reduces KL, adaptive outperforms static when loss rankings change) consists of straightforward applications of known results. The condition 'adaptive strictly outperforms static when per-transition loss rankings change during training' is near-tautological — of course static is suboptimal when the optimal distribution changes. This does not constitute a novel theoretical contribution for a top venue.\", \"OHEM PRIOR ART: Online Hard Example Mining (Shrivastava et al., CVPR 2016) is the 10-year-old technique of sampling based on current loss magnitude during training. APER is essentially OHEM applied to VLA SFT with PER's sum-tree data structure and IS correction. This connection should be explicitly discussed and differentiated from.\", \"MISSING RECENT WORK — RINSE (arXiv:2604.23000, April 2026): 'Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning' proposes smoothness-based quality metrics for IL demonstration curation, achieving 16% higher success with 1/6 of data on RoboMimic. This is a very recent static curation baseline that should be included.\", \"VENUE DEADLINE CLARIFICATION: CoRL 2026 official Instruction for Authors explicitly states 'the paper submission deadline is Thursday (5/28) EOD rather than Friday.' The HuggingFace tracker shows May 29 at 11:59 UTC, which is effectively May 28 EOD US time. The idea correctly notes May 28 but inconsistently also says May 29 in some places.\", \"LAZY PRIORITY STALENESS RISK: With lazy updates (only recomputing priorities when sampled), most transitions' priorities become stale. The ε_mix=0.05 uniform mixing only refreshes 5% of samples per step. With large demonstration datasets (100K+ transitions), most transitions will never be resampled during training, keeping permanently stale priorities. The freshness decay helps but only penalizes, never refreshes actual loss values. This needs analysis — what fraction of the buffer actually gets resampled during typical VLA fine-tuning?\"]\nFeedback: The Round 2 revision addressed Round 1's most critical issue (unstable value function) by switching to loss-driven priorities, which is a much cleaner approach. However, the novelty bar remains unmet for CoRL 2026. The core problem: APER combines known components (OHEM-style loss sampling + PER sum-tree + IS correction from Schaul et al. + freshness decay from FreshPER + theoretical framing from iw-SFT) without adding a genuinely new idea. To reach CoRL quality:\n\n1. **Differentiate sharply from iw-SFT.** iw-SFT already has adaptive IS weights tracking the policy during SFT. APER uses loss magnitude as priority while iw-SFT uses policy ratio — argue why loss-magnitude priorities are better (e.g., loss captures multi-modal difficulty that policy ratios miss in VLA action spaces). Ideally prove this formally.\n\n2. **Add VLA-specific novelty.** Generic PER applied to VLA is engineering. What about VLA-specific signals? E.g., action chunk consistency (some transitions have high loss because the chunk prediction diverges mid-chunk), visual attention entropy (high-attention transitions may be more informative), or multi-modal loss decomposition (separate vision/language/action loss components and prioritize by the bottleneck modality). These would make the contribution VLA-specific rather than a generic application.\n\n3. **Acknowledge and position against LLM SFT data selection work.** SuRe, ProFit, PEAR, PBS all perform online/loss-based data prioritization during LLM training. APER must explain why the VLA setting is different enough to warrant a separate contribution (e.g., continuous action spaces, multi-modal inputs, demonstration quality heterogeneity).\n\n4. **Strengthen the theoretical contribution.** The current analysis (KL divergence bounds, Lipschitz conditions) is textbook. Consider: (a) proving convergence rate improvements specific to multi-modal action distributions, (b) analyzing how action chunking interacts with per-transition priorities, or (c) providing sample complexity bounds showing adaptive PER needs fewer demonstrations to reach a given success rate.\n\n5. **Add RINSE (April 2026) as a baseline.** It's the most recent static curation method and directly competes on RoboMimic.\n\n6. **Quantify the staleness problem.** Run a simple analysis: during VLA fine-tuning with N transitions, what fraction of transitions are sampled at least once? How quickly do loss rankings decorrelate? This empirical characterization would strengthen the motivation.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING RELATED WORK — EMMA/AdaMix (arXiv:2509.22407, Sep 2025, revised Mar 2026): EMMA introduces AdaMix, a hard-sample-aware training strategy for VLA models that adaptively reweights samples during training based on three metrics: Action Prediction Error (MSE over action chunks), Trajectory Smoothness, and Joint Angle Limitation. AdaMix achieves 17% improvement over fixed-ratio mixing during VLA SFT. This is the closest existing work to CDAP in the VLA training space — it already performs online adaptive sample reweighting during VLA SFT using action prediction loss. The key difference is that AdaMix uses aggregated MSE over the full chunk while CDAP decomposes per-position losses, but this differentiation MUST be explicitly discussed. AdaMix should also be added as a baseline.\", \"MISSING RELATED WORK — Token Cleaning (arXiv:2502.01968, ICML 2025): Fine-grained token-level data selection for LLM SFT using influence of model updates on each token. Conceptually parallel to CDAP's per-position loss analysis — both move beyond sample-level to sub-sample-level quality assessment during SFT. Should be discussed in the LLM SFT landscape section.\", \"MISSING RELATED WORK — VGAS (arXiv:2602.07399, Feb 2026): Value-Guided Action-Chunk Selection for Few-Shot VLA Adaptation. Uses Q-Chunk-Former to evaluate and select action chunks at inference time. While inference-time (not training-time), it represents another work that analyzes action chunk quality at a fine-grained level.\", \"VENUE DEADLINE INACCURACY: The idea states 'abstract deadline: May 25, 2026' in the target_venues field — the actual CoRL 2026 abstract deadline is May 26, 2026 at 11:59 UTC. The paper deadline ambiguity (May 28 EOD Thursday vs. May 29 at 11:59 UTC) persists across sources; the idea should cite the conservative date (May 28 EOD).\", \"THEORETICAL CLAIMS OVERSTATED: The 'temporal profile evolution theorem' claims that per-position loss profiles evolve from flat to monotonically increasing 'under standard smoothness assumptions.' This is plausible but unproven — it's an empirical hypothesis, not a theorem. Calling it a theorem without proof or stating the exact assumptions risks reviewer pushback. The variance reduction result (chunk-decomposed prioritization reduces variance for heterogeneous chunks) is straightforward and adds limited theoretical novelty. The contact-phase sample complexity bound is a simple calculation, not a deep result.\", \"EMPIRICAL VALIDATION RISK: The entire contribution rests on the hypothesis that temporal divergence δ captures learning-relevant structure that scalar loss μ misses. If α_δ=0 (scalar PER ablation) performs comparably to full CDAP, the VLA-specific novelty collapses to engineering. This is the paper's make-or-break experiment and is currently untested.\", \"RINSE VENUE: The idea cites RINSE as 'arXiv April 2026' but it appears to be accepted at ICML 2025 (confirmed at icml.cc/virtual/2025/48703). This should be corrected.\", \"CAPS VENUE: CAPS (arXiv:2503.01650) is listed as a reference but was accepted at ICRA 2025 (not 2026). While not discussed in the landscape, if cited it should have the correct venue.\"]\nFeedback: Round 3 represents substantial improvement — the pivot from TD-error value functions (Round 1) through scalar loss prioritization (Round 2) to chunk-decomposed temporal profiles is the right direction. The CTP signal is genuinely novel. To reach CoRL quality:\n\n1. **CRITICAL: Add EMMA/AdaMix as related work AND baseline.** EMMA (arXiv:2509.22407) already performs online adaptive sample reweighting during VLA SFT using action prediction MSE. This is your most direct competitor. Differentiation: AdaMix uses aggregated MSE (scalar), CDAP decomposes per-position losses to capture *why* a transition is hard (temporal coherence vs. perception failure). Add AdaMix as baseline (e) between RINSE and scalar-loss PER: 'AdaMix (adaptive scalar-MSE reweighting during VLA SFT, EMMA 2025).' The ablation path becomes: Uniform → AdaMix (scalar adaptive) → Scalar-PER+IS (your α_δ=0 ablation) → full CDAP (temporal decomposition). This progression cleanly isolates CDAP's contribution.\n\n2. **Downgrade theoretical claims to hypotheses.** Present the temporal profile evolution as 'Hypothesis 1' to be validated empirically, not 'Theorem 1.' This is more honest and actually makes the empirical analysis contribution stronger — you're the first to systematically test this hypothesis. CoRL reviewers will appreciate intellectual honesty over inflated theory.\n\n3. **Strengthen the empirical contribution framing.** The first systematic analysis of how intra-chunk temporal loss profiles evolve during VLA SFT is genuinely valuable regardless of whether CDAP outperforms baselines. Frame it as: 'We provide the first empirical characterization of temporal loss profile evolution during VLA SFT, revealing [finding]. CDAP is a practical method motivated by this analysis.' This makes the paper valuable even if gains are modest.\n\n4. **Add Token Cleaning (ICML 2025) to LLM SFT landscape.** It's the closest LLM analogue — moving from sample-level to sub-sample-level (token-level) quality assessment during SFT. The parallel strengthens your positioning: 'Just as Token Cleaning reveals that token-level quality varies within samples for LLM SFT, we show that position-level difficulty varies within action chunks for VLA SFT.'\n\n5. **Fix venue citations.** RINSE → ICML 2025 (not just arXiv). CAPS → ICRA 2025. CoRL abstract deadline → May 26 (not May 25).\n\n6. **Design the α_δ ablation carefully.** The scalar PER (α_δ=0) vs. full CDAP comparison is the single most important experiment. If δ doesn't help, the paper doesn't work. Consider pre-running a small-scale pilot on RoboMimic-MH before committing to the full experimental pipeline.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T17:37:30.919Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T17:37:30.919Z",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-13T17:37:30.960Z_

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

## Idea under review (round 4/10)
{
  "title": "Chunk-Decomposed Adaptive Prioritization for VLA Supervised Fine-Tuning",
  "core_problem": "Can we exploit the temporal structure of action-chunk prediction losses — which reveals *why* each demonstration transition is hard, not just *how* hard it is — to design a VLA-specific adaptive prioritization mechanism for SFT that outperforms both generic loss-based sampling and existing adaptive scalar-MSE reweighting (AdaMix)?",
  "opportunity": "Every existing demonstration curation method (SCIZOR, CUPID, DataMIL, DemInf, RINSE) operates as a static filter-then-train preprocessing step, while every existing online prioritization method treats the training loss as a scalar priority signal — even when applied to sequential predictions. This includes AdaMix (EMMA, 2025), the most relevant prior work, which adaptively reweights VLA training samples based on aggregated MSE over action chunks, trajectory smoothness, and joint angle constraints — but reduces the chunk prediction loss to a single scalar before reweighting. VLA models with action chunking produce a uniquely structured loss signal: for each transition, the model predicts K future actions [a_1, ..., a_K], yielding a per-position loss vector [l_1, ..., l_K] that encodes *temporal prediction quality*. This vector is discarded when aggregated into a scalar mean loss. Yet it carries critical information: a transition where the first actions are correct but the chunk diverges mid-way (high temporal divergence) represents a temporal coherence challenge — the model has learned the local dynamics but fails to propagate them forward. A transition where all K actions are uniformly wrong (low temporal divergence, high aggregate) represents a fundamental perception or grounding failure. These require fundamentally different amounts of training focus, and the optimal treatment shifts during training: early on, most chunks are uniformly wrong; as training progresses, the model learns initial actions first and temporal coherence becomes the dominant bottleneck. This structured evolution has no analogue in LLM token prediction and cannot be captured by scalar prioritization.\n\nThe second VLA-specific opportunity is task phase structure: robot manipulation has identifiable critical phases (approach → grasp → transport → place) marked by gripper state transitions. Contact-phase transitions are brief but disproportionately important for task success, as shown empirically by DAM-VLA's asymmetric Gaussian weighting. However, both DAM-VLA (fixed Gaussian) and AdaMix (uniform across phases) apply the same weighting scheme to all transitions regardless of task phase. An adaptive mechanism that identifies which specific contact-phase transitions the current policy still struggles with would be more sample-efficient.\n\nThe parallel to recent work in LLM SFT is instructive: Token Cleaning (ICML 2025) showed that sub-sample-level (token-level) quality varies significantly within samples for LLM SFT, and that filtering at the token level outperforms sample-level filtering. CDAP applies the analogous insight to VLA SFT: position-level difficulty varies within action chunks, and prioritizing at the chunk-decomposed level outperforms sample-level scalar reweighting.\n\nNo existing work exploits the *intra-chunk temporal loss profile* as an adaptive priority signal for VLA training data selection. AdaMix reweights samples adaptively but uses scalar-aggregated MSE; DAM-VLA uses intra-chunk structure but applies fixed weights; Token Cleaning uses sub-sample structure but in discrete LLM token spaces. CDAP fills this specific intersection: adaptive online prioritization that decomposes the continuous action-chunk loss into temporal components capturing *why* transitions are hard.",
  "landscape": "**Static demonstration curation (the dominant paradigm):** SCIZOR (ICRA 2026) uses self-supervised progress prediction to filter suboptimal/redundant transitions, achieving 32.9% gains on Sirius-Fleet and 5.4% on RoboMimic. CUPID (CoRL 2025) and QoQ (arXiv 2026) use influence functions to score demonstrations. DataMIL (ICLR 2026) trains datamodels to predict which data subsets improve success. DemInf (RSS 2025) estimates mutual information for quality scoring. RINSE (ICML 2025, arXiv:2604.23000) proposes smoothness-based metrics (Spectral Arc Length + Trajectory-Envelope Distance), achieving 16% higher success with 1/6 data on RoboMimic and 20% improvement with half data on real-world manipulation. Re-Mix (CoRL 2024) optimizes domain-level data mixtures via DRO. All operate as filter-then-train pipelines: the curation is fixed before training begins.\n\n**Adaptive sample reweighting for VLA SFT (most direct competitor):** EMMA/AdaMix (arXiv:2509.22407, Sep 2025, revised Mar 2026) introduces a hard-sample-aware training strategy for VLA models that adaptively reweights samples during SFT based on three metrics: (1) Action Prediction Error — MSE aggregated over the full action chunk: r_i^MSE = -(1/L) Σ ||â_{i+t} - a_{i+t}||²₂, (2) Trajectory Smoothness — second-order joint angle differences penalizing abrupt actions, and (3) Joint Angle Limitation — binary safety constraint. These are min-max normalized and combined via arithmetic mean into a composite score s_i, with sampling probability p(i) ∝ γ + λ·(1 − s_i). Built on the π₀ backbone, AdaMix achieves 13% improvement over uniform sampling on real-world tasks. The paper was submitted to ICLR 2026 but withdrawn; it remains an arXiv preprint. **Critical differentiation from CDAP:** AdaMix computes MSE *aggregated over the full action chunk* (scalar), then reweights — it does not decompose per-position losses within the chunk. Its trajectory smoothness metric operates on ground-truth joint angles, not on the model's prediction quality at each temporal position. CDAP's temporal divergence δ_i captures a fundamentally different signal: how the *model's prediction quality degrades* over the chunk horizon, which is invisible to aggregated MSE. A chunk where positions 1-4 are correct and positions 5-8 diverge has the same aggregated MSE as a chunk where all positions have moderate error, but represents a qualitatively different learning challenge.\n\n**Online Hard Example Mining (the 10-year-old precursor):** OHEM (Shrivastava et al., CVPR 2016) selects the highest-loss examples in each mini-batch for gradient updates in object detection. Focal Loss (Lin et al., ICCV 2017) down-weights easy examples via a modulating factor. Both use scalar loss magnitude as the difficulty signal and operate within-batch without cross-batch priority tracking. CDAP differs in three ways: (1) uses chunk-decomposed loss structure, not scalar magnitude; (2) maintains a persistent priority buffer with IS correction for across-batch prioritization; (3) adapts priorities online as the policy evolves.\n\n**Prioritized Experience Replay (PER) and its descendants:** Schaul et al. (ICLR 2016) introduced sum-tree priority buffers with IS correction for RL. OPER (TNNLS 2024) applies PER to offline RL including BC on D4RL — but computes priorities statically via a decoupled two-stage procedure requiring reward signals. AFBC (arXiv 2021) uses advantage estimates for BC prioritization — also reward-dependent and static. Freshness-Aware PER (arXiv April 2026) successfully extends PER to billion-parameter LLM/VLM RL training with exponential age decay addressing priority staleness — but exclusively targets reward-dependent RL post-training. None of these decompose the loss signal by temporal structure within action chunks.\n\n**Adaptive importance weighting for SFT (iw-SFT):** iw-SFT (arXiv 2507.12856) establishes that SFT on curated data maximizes a lower bound on the RL objective and introduces adaptive importance weights via policy ratios with EMA-tracked reference parameters (θ_q = αθ_q + (1−α)θ). Evaluates on D4RL locomotion, Ant-maze, and Franka Kitchen. **Critical differentiation:** iw-SFT's importance weights are *policy ratios* — they measure how far the current policy has drifted from the reference distribution. In continuous VLA action spaces (7-DoF or higher), policy ratios via Gaussian likelihoods are numerically unstable and dominated by minor mean shifts in low-variance dimensions. CDAP's chunk-decomposed loss directly measures *where and why* the policy fails, providing a more informative and stable signal in high-dimensional continuous action spaces.\n\n**Sub-sample-level data selection for LLM SFT:** Token Cleaning (ICML 2025 Spotlight, arXiv:2502.01968) investigates token quality from a noisy-label perspective and proposes token-level data selection for LLM SFT by examining the influence of model updates on each token, then applying threshold-based separation. This is the closest *conceptual* parallel to CDAP in the LLM domain: both move beyond sample-level to sub-sample-level quality assessment during SFT. The key difference is domain: Token Cleaning operates on discrete tokens in language sequences where quality is about informativeness vs. noise, while CDAP operates on continuous action predictions where quality has temporal structure (prediction quality degrades systematically with temporal distance from the current observation). ProFit (arXiv:2601.09195) selectively masks low-probability tokens during LLM SFT. PEAR (arXiv:2602.01058) uses IS reweighting at token/block/sequence level. PBS (arXiv:2602.17066) predicts per-sample loss from static token features. SuRe (arXiv:2511.22367) uses sequence-level NLL surprise for prioritized replay. All target discrete token prediction in LLMs and have no mechanism for handling continuous action chunks or temporal prediction quality degradation.\n\n**VLA-specific loss weighting:** DAM-VLA (arXiv March 2026) introduces dual-scale action weighting: trajectory-level asymmetric Gaussian weights centered on gripper state transitions (σ_l=6, σ_r=2) and chunk-level exponential decay. This is the closest work to CDAP's contact-phase awareness, but DAM-VLA applies *fixed, universal* loss weights to all transitions equally — it does not adaptively select which transitions to prioritize based on current policy performance. CDAP uses contact-phase proximity as one component of an *adaptive* priority that evolves with the policy.\n\n**VLA action chunk analysis at inference time:** 'VLA Knows Its Limits' (arXiv Feb 2026) reveals that intra-chunk actions attend invariantly to vision-language tokens and prediction quality degrades systematically with temporal distance, with 'action sinks' at initial and terminal positions. AutoHorizon dynamically estimates execution horizons from attention patterns. VGAS (arXiv:2602.07399, Feb 2026) introduces Q-Chunk-Former, a geometrically grounded Transformer critic, for value-guided action-chunk selection at inference time via best-of-N selection, resolving geometric ambiguities among candidate chunks. Both support CDAP's premise that intra-chunk temporal structure is informative, but address inference-time execution (AutoHorizon: execution horizons; VGAS: chunk selection), not training-time data prioritization.\n\n**Gap:** No existing work exploits the *intra-chunk temporal loss profile* as an adaptive priority signal for VLA SFT. Static curation methods (SCIZOR, RINSE) ignore training dynamics. Scalar-loss adaptive methods (AdaMix, OHEM, PER, iw-SFT) discard the temporal structure within chunks — AdaMix is the closest, performing adaptive reweighting during VLA SFT, but aggregates chunk MSE into a scalar before reweighting. Fixed-weighting methods (DAM-VLA) don't adapt to individual transition difficulty. LLM sub-sample methods (Token Cleaning, ProFit, PEAR, PBS) don't handle continuous action chunks. Inference-time chunk analysis methods (VGAS, AutoHorizon) don't address training-time prioritization. CDAP fills this intersection.",
  "approach": "We propose CDAP (Chunk-Decomposed Adaptive Prioritization), replacing scalar loss-based sampling with a VLA-specific priority signal that exploits the temporal structure of action-chunk prediction losses during SFT. CDAP requires no auxiliary model, no reward annotations, and adds <3% compute overhead.\n\n**1. Chunk Temporal Profile (CTP) — the VLA-specific priority signal:**\nDuring VLA SFT with action chunking (chunk size K), each transition i produces per-position L1 losses [l_{i,1}, ..., l_{i,K}] from the predicted vs. ground-truth action chunk. Instead of discarding this structure into a scalar mean (as AdaMix does with MSE), CDAP computes a two-component priority:\n\n(a) *Aggregate difficulty*: μ_i = (1/K) Σ_k l_{i,k} — overall prediction quality, analogous to AdaMix's aggregated MSE and standard loss-based priority.\n\n(b) *Temporal divergence*: δ_i = (1/(K−1)) Σ_{k=1}^{K−1} ReLU(l_{i,k+1} − l_{i,k}) — average positive slope of per-position losses, measuring how much prediction quality degrades over the chunk horizon. High δ_i indicates a temporal coherence challenge (initial actions correct, chunk diverges mid-way); low δ_i with high μ_i indicates a fundamental perception/grounding failure.\n\nWe also study alternative temporal metrics: loss variance within chunk (Var(l_{i,1}, ..., l_{i,K})), loss range (max − min), and Spearman correlation between position index and loss. The ablation identifies which temporal metric best captures learning-relevant structure.\n\n**2. Contact-Phase Aware Weighting:**\nGripper state transitions (open→close, close→open) are identified directly from demonstration data (no model needed). Transitions within a window w of a gripper state change receive a multiplicative contact-phase boost: c_i = 1 + η if transition i is within w steps of a gripper transition, else c_i = 1. This is grounded in DAM-VLA's empirical finding that contact phases are critical for manipulation success, but unlike DAM-VLA's fixed Gaussian or AdaMix's phase-agnostic reweighting, CDAP combines this with adaptive difficulty-based selection: among all contact-phase transitions, CDAP prioritizes those the current policy still finds hard.\n\n**3. Priority Function and Sampling:**\nThe composite priority for transition i is:\n  p(i) = (μ_i + ε)^{α_μ} · (1 + γ · δ_i)^{α_δ} · c_i\n\nwhere α_μ controls aggregate-loss prioritization strength, α_δ controls temporal-divergence prioritization strength, and γ scales the divergence contribution. Setting α_δ = 0 recovers scalar-loss PER (OHEM+IS), enabling clean ablation against AdaMix's scalar approach. Transitions are sampled from a sum-tree buffer with probability proportional to p(i).\n\n**4. Importance-Sampling Correction:**\nFollowing Schaul et al. and iw-SFT's theoretical framework, apply capped IS weights w_i = (N · p(i)/Σp)^{−β} with β annealed from β_0 to 1.0 over training. This ensures unbiased gradient estimates while maintaining the theoretical link to RL objective bounds established by iw-SFT. The key distinction: iw-SFT's weights correct for the ratio between behavior and current policy distributions (policy-ratio-based), while CDAP's weights correct for the ratio between the adaptive chunk-decomposed priority distribution and the uniform distribution (loss-structure-based). Both are valid IS schemes with different inductive biases.\n\n**5. Freshness-Aware Age Decay:**\nAdopt Freshness-Aware PER's exponential age decay: p_eff(i) = p(i) · exp(−λ · age_i), where age_i counts steps since transition i was last sampled. This addresses priority staleness at VLA scale.\n\n**6. Lazy Updates with Coverage-Guaranteed Mixing:**\nPriorities are updated lazily when sampled (loss is computed anyway for gradient updates, and the per-position losses [l_{i,1}, ..., l_{i,K}] are available at zero additional cost from the chunk prediction). With probability ε_mix, sample uniformly to ensure buffer coverage. We set ε_mix adaptively: ε_mix = max(ε_min, 1 − coverage_t) where coverage_t is the current fraction of transitions sampled at least once.\n\n**7. Empirical Hypotheses and Analysis (replacing overstated theoretical claims):**\nInstead of claiming formal theorems, we formulate testable hypotheses motivated by the structure of action-chunk prediction, and provide the first systematic empirical investigation:\n\n(a) *Hypothesis 1 — Temporal profile evolution*: Under VLA SFT with action chunking of size K, the per-position loss profile [l_1(θ), ..., l_K(θ)] evolves from approximately flat (all positions equally hard early in training) to monotonically increasing (initial positions learned first, later positions remain hard). The rate of this transition depends on the temporal correlation structure of the demonstration data. We test this hypothesis by tracking per-position loss profiles across training for different transition types (contact vs. free-space, smooth vs. non-smooth demonstrations).\n\n(b) *Hypothesis 2 — Temporal divergence informativeness*: Transitions with similar aggregate difficulty μ but different temporal divergence δ have different downstream impact on task success, i.e., δ carries learning-relevant information beyond what μ captures. We test this by partitioning transitions into (μ, δ) bins and measuring per-bin gradient utility (cosine similarity with the full-data gradient).\n\n(c) *Variance reduction analysis*: For transitions exhibiting high temporal divergence (δ_i >> 0), we empirically measure whether gradient variance under chunk-decomposed prioritization is lower than under scalar-loss prioritization, and by how much. The intuition: when a chunk has heterogeneous per-position losses, scalar-loss PER may over- or under-prioritize depending on the aggregation, while chunk-decomposed prioritization places the transition at the appropriate priority for its *bottleneck* (the diverging later positions) rather than its *average*.\n\n(d) *Contact-phase sample complexity*: We empirically measure whether contact-phase boosted sampling reduces the number of gradient steps to reach a given contact-phase loss threshold compared to uniform and scalar-adaptive sampling.\n\n**8. Implementation on OpenVLA-OFT:**\nIntegrate CDAP into the OpenVLA-OFT fine-tuning pipeline. The per-position losses are already computed during the L1 regression forward pass for each action chunk — CDAP's CTP computation (mean + temporal divergence) adds only K floating-point operations per transition, truly negligible overhead. The sum-tree priority buffer replaces the uniform DataLoader sampler. Implementation is ~150 lines of code.\n\n**9. Evaluation — Benchmarks:**\n(a) Sirius-Fleet: real-world mixed-quality fleet data where data quality is the established bottleneck (SCIZOR showed 32.9% absolute gains). (b) RoboMimic multi-human (MH): explicit mixed-quality operators. (c) OXE subsets (Bridge, RT-1, DROID): cross-site quality heterogeneity. (d) SimplerEnv: VLA-specific evaluation.\n\n**10. Evaluation — Baselines:**\n(a) Uniform sampling (OpenVLA-OFT default). (b) SCIZOR (static progress-based filtering, ICRA 2026). (c) RINSE (static smoothness-based filtering, ICML 2025). (d) CUPID (static influence-based, CoRL 2025). (e) AdaMix (adaptive scalar-MSE + smoothness + joint limits reweighting during VLA SFT, EMMA arXiv 2025 — most direct competitor). (f) Scalar-loss PER (α_δ=0 ablation of CDAP — equivalent to OHEM + IS correction + age decay, isolating temporal decomposition's value vs. scalar-loss adaptive methods including AdaMix). (g) SCIZOR→CDAP and RINSE→CDAP (adaptive on top of static, demonstrating complementary benefit).\n\nThe ablation path cleanly isolates CDAP's contribution: Uniform → AdaMix (scalar adaptive, external baseline) → Scalar PER+IS (α_δ=0, our framework without temporal component) → Full CDAP (with temporal decomposition). If scalar PER+IS ≈ AdaMix, the frameworks are equivalent modulo IS correction and age decay. If full CDAP > scalar PER+IS, temporal decomposition adds value. This is the paper's make-or-break comparison.\n\n**11. Evaluation — Key Analyses (VLA-specific empirical contributions):**\n(a) *Temporal loss profile evolution*: Visualize how the intra-chunk loss profile [l_1, ..., l_K] evolves during training across different types of transitions (contact vs. free-space, successful vs. failed demonstrations). This is the first systematic study of how per-position action chunk losses evolve during VLA SFT — the empirical investigation itself is a contribution regardless of whether CDAP outperforms all baselines.\n(b) *Loss rank decorrelation*: Measure Spearman correlation between initial and final per-transition loss rankings, and separately for aggregate difficulty μ and temporal divergence δ, to quantify how much the optimal data distribution shifts and whether the shift is captured by scalar vs. decomposed priorities.\n(c) *Buffer coverage analysis*: Track the fraction of transitions sampled at least once during training under different prioritization schemes, directly addressing the staleness concern.\n(d) *Temporal divergence vs. aggregate difficulty decomposition*: Show that transitions with similar μ but different δ have different downstream impact on task success, validating the information content of the temporal profile.\n(e) *Ablation over α_μ, α_δ, γ, η, w, λ, ε_mix, β schedule*.\n(f) *Compute overhead profiling* at VLA scale (expected: <3% wall-clock, <1% GPU).\n(g) *Pre-pilot on RoboMimic-MH*: Before committing to the full experimental pipeline, run a small-scale pilot comparing uniform vs. AdaMix vs. scalar PER (α_δ=0) vs. full CDAP on RoboMimic-MH to validate that δ carries learning-relevant signal. This de-risks the main experimental investment.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~500h A100-80GB (~8 baselines × 20h + ~8 method runs × 25h + ~10 ablations × 12h + ~30h analysis/visualization + ~20h AdaMix reimplementation)",
      "gpu_utilization": "~30-40% effective utilization; GPUs idle during implementation, debugging, and analysis",
      "timeline": "2-4 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$750 at ~$1.50/hr"
    },
    "human_in_loop": {
      "gpu_hours": "~650h A100-80GB (agent explores more hyperparameter configurations and temporal metric variants; human gates benchmark selection and analysis framing; includes AdaMix reimplementation and pilot study)",
      "gpu_utilization": "~65-75% utilization; agent queues experiments overnight, human reviews results and approves next batch",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$120-250 (800-1500 turns: code generation, experiment orchestration, result analysis)",
      "estimated_gpu_cost": "~$975 at ~$1.50/hr",
      "risk_note": "Primary risk is that α_δ ablation shows temporal decomposition adds minimal value over scalar-adaptive methods. Pilot on RoboMimic-MH (included in estimate) de-risks this before full benchmark commitment."
    },
    "auto_research": {
      "gpu_hours": "~1000-1200h A100-80GB (comprehensive exploration of temporal metrics, hyperparameters, cross-benchmark analysis, and AdaMix reimplementation/comparison)",
      "gpu_utilization": "~90-95% utilization; agent runs 24/7",
      "timeline": "10-16 days with 8× A100 cluster",
      "team": "0 (initial setup and final review only)",
      "claude_api_cost": "$250-500 (1500-3000 turns for code, orchestration, ablation design, paper drafting)",
      "estimated_gpu_cost": "~$1,650 at ~$1.50/hr",
      "speed_bottleneck": "GPU cluster availability for 7B model fine-tuning; Sirius-Fleet simulation throughput for evaluation rollouts",
      "risk_note": "Agent may over-explore temporal metric variants; risk of ~10% wasted compute. Timeline tight for CoRL 2026 (abstract May 26, paper May 28 EOD / May 29 11:59 UTC) but feasible given that core implementation is ~150 lines. Pilot study should be prioritized in first 2 days."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline: May 26, 2026 11:59 UTC; paper deadline: May 28, 2026 EOD Thursday per Instruction for Authors, or May 29, 2026 11:59 UTC per OpenReview — use conservative May 28 EOD for planning)",
    "AAAI 2027 (deadline: expected ~Aug 2026)",
    "ICRA 2027 (deadline: expected ~Sep 2026)",
    "ICLR 2027 (deadline: expected ~Sep-Oct 2026)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Online Hard Example Mining (Shrivastava et al., CVPR 2016)",
    "Focal Loss for Dense Object Detection (Lin et al., ICCV 2017)",
    "Prioritized Experience Replay (Schaul et al., ICLR 2016)",
    "OPER: Decoupled Prioritized Resampling for Offline RL (Yue et al., TNNLS 2024, arXiv:2306.05412)",
    "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (arXiv:2110.04698, 2021)",
    "Supervised Fine Tuning on Curated Data is Reinforcement Learning (iw-SFT, arXiv:2507.12856, 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)",
    "DemInf: Robot Data Curation with Mutual Information Estimators (RSS 2025)",
    "RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025, arXiv:2604.23000)",
    "Quality over Quantity: Demonstration Curation via Influence Functions (QoQ, arXiv 2026)",
    "EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (arXiv:2509.22407, Sep 2025, revised Mar 2026) — introduces AdaMix adaptive sample reweighting for VLA SFT",
    "Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning (ICML 2025 Spotlight, arXiv:2502.01968)",
    "SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv:2511.22367, 2025)",
    "ProFit: Probability-Guided Token Selection for SFT (arXiv:2601.09195, Jan 2026)",
    "PEAR: Good SFT Optimizes for SFT, Better SFT Prepares for RL (arXiv:2602.01058, Feb 2026)",
    "PBS: Predictive Batch Scheduling for LLM Training (arXiv:2602.17066, Feb 2026)",
    "Freshness-Aware Prioritized Experience Replay for LLM/VLM RL (arXiv:2604.16918, April 2026)",
    "Prioritized Replay for RL Post-training (arXiv:2601.02648, Jan 2026)",
    "DAM-VLA: Dynamic Action Model-Based VLA Framework (arXiv March 2026)",
    "VLA Knows Its Limits (arXiv:2602.21445, Feb 2026)",
    "VGAS: Value-Guided Action-Chunk Selection for Few-Shot VLA Adaptation (arXiv:2602.07399, Feb 2026)",
    "Leave No Observation Behind: Real-time Correction for VLA Action Chunks (arXiv:2509.23224, 2025)",
    "CAPS: Context-Aware Priority Sampling for Enhanced Imitation Learning (ICRA 2025, arXiv:2503.01650)",
    "OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models (arXiv 2025)",
    "PLD: Self-Improving VLA Models via Residual RL (ICLR 2026)",
    "ExpReS-VLA: Specializing VLA Models Through Experience Replay (arXiv:2511.06202, 2025)",
    "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)",
    "GREATS: Online Selection of High-Quality Data for LLM Training (NeurIPS 2024)",
    "Open X-Embodiment: Robotic Learning Datasets and RT-X Models (arXiv 2023)"
  ],
  "description": "We propose CDAP (Chunk-Decomposed Adaptive Prioritization) for VLA model SFT, exploiting a VLA-specific signal that existing adaptive methods discard: the temporal structure of per-position losses within action chunks. VLA models with action chunking predict K future actions per transition, producing a loss vector [l_1, ..., l_K] that encodes temporal prediction quality — high temporal divergence (early actions correct, chunk diverges mid-way) indicates temporal coherence challenges, while uniformly high loss indicates perception/grounding failure. CDAP uses a two-component priority: aggregate difficulty (standard) and temporal divergence (VLA-specific), combined with contact-phase-aware weighting that boosts transitions near gripper state changes. This provides a richer priority signal than scalar loss aggregation (OHEM, standard PER), scalar-MSE adaptive reweighting (AdaMix/EMMA), policy ratios (iw-SFT), or fixed weighting (DAM-VLA), while requiring zero additional compute — per-position losses are already available from the chunk prediction forward pass. Just as Token Cleaning (ICML 2025) revealed that token-level quality varies within samples for LLM SFT, we show that position-level difficulty varies within action chunks for VLA SFT — but in a continuous action space with temporal structure rather than discrete tokens. We formulate testable hypotheses about temporal loss profile evolution (from flat to monotonically increasing during training) and temporal divergence informativeness, providing the first systematic empirical characterization of how intra-chunk loss profiles evolve during VLA SFT. Evaluated on Sirius-Fleet, RoboMimic-MH, OXE subsets, and SimplerEnv against eight baselines including SCIZOR, RINSE, AdaMix, and scalar-loss PER (our own α_δ=0 ablation), the ablation path Uniform → AdaMix → Scalar PER+IS → Full CDAP cleanly isolates the contribution of temporal decomposition. CDAP is designed as a complementary add-on: SCIZOR→CDAP and RINSE→CDAP demonstrate gains on top of static filtering. A small-scale RoboMimic-MH pilot is recommended before full benchmark commitment to validate that δ carries learning-relevant signal beyond μ.",
  "project_name": "chunk_decomposed_priority_vla",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL MISSING RELATED WORK: OPER (Decoupled Prioritized Resampling for Offline RL, arXiv:2306.05412, TNNLS) directly applies TD-error-based prioritized resampling to behavioral cloning — this is the closest prior work and is completely unacknowledged. AFBC (arXiv:2110.04698) repurposes PER for BC in noisy datasets. Goal-Conditioned BC with Prioritized Sampling (IEEE 2021) applies prioritized sampling to goal-conditioned BC. ExpReS-VLA (arXiv:2511.06202) uses prioritized replay buffer for VLA fine-tuning.", "CRITICAL FEASIBILITY: Goal-conditioned value function training via hindsight relabeling in offline settings is known to be unstable. GoFAR (NeurIPS 2022) explicitly showed that 'hindsight relabeling involves sensitive hyperparameter tuning that cannot be easily performed offline' and proposed avoiding value function estimation entirely. GCSL (ICLR 2022) similarly avoids value estimation for stability. The proposal assumes a stable V(s,g) can be trained on demonstrations — this is an untested and potentially unsound assumption.", "LIBERO SATURATION: OpenVLA-OFT achieves 97.1% average on LIBERO-4. Pi0.5 achieves 97.5%. There is virtually no headroom for improvement. LIBERO-Plus (arXiv:2510.13626) shows VLAs drop from 95% to <30% under perturbations, but this tests robustness to environmental variations, not data quality. The paper needs benchmarks where data quality is the actual bottleneck.", "MISSING RELATED WORK (non-critical): DemInf (RSS 2025, MI-based curation), Re-Mix (CoRL 2024, data mixture optimization via DRO), DMDR (TNNLS 2025, diffusion-based noisy demo restoration). Also, iw-SFT (arXiv:2507.12856) establishes that SFT on curated data optimizes an RL objective bound — this theoretical insight partially subsumes APER's claimed theoretical contribution.", "VENUE DEADLINE ERROR: CoRL 2026 paper deadline is May 28, 2026 AoE (Thursday), not May 29 as stated. The official CoRL site explicitly emphasizes 'the paper submission deadline is Thursday (5/28) EOD rather than Friday.'", "COMPUTE OVERHEAD UNDERESTIMATED: Maintaining a goal-conditioned value function, periodically retraining it, and recomputing TD errors over the full demonstration buffer during VLA-scale fine-tuning is significantly more than ~5% overhead. A 7B VLA model's forward pass is already expensive; adding value function training + full-buffer TD recomputation every K steps could easily be 15-30%.", "DataMIL venue is ICLR 2026 Poster (not arXiv 2025 as cited). QoQ appears to be ICRA 2026 (not arXiv 2026). OpenVLA-OFT may no longer be SOTA — Pi0.5 and SimpleVLA-RL have matched or exceeded it.", "TIMELINE RISK: 15 days to abstract deadline and 18 days to paper deadline. Implementing a stable goal-conditioned value function, integrating it with OpenVLA-OFT training, running 5+ baselines + ablations on LIBERO/RoboMimic/OXE, and writing the paper is extremely ambitious even for auto-research mode."]
Feedback: The core direction (adaptive vs. static data curation during VLA training) addresses a real gap, but the specific instantiation via TD-error PER has serious problems. To make this viable for CoRL 2026:

1. **Acknowledge and differentiate from OPER, AFBC, and ExpReS-VLA.** OPER is the most direct threat — it already uses TD-error-based prioritized resampling for BC. You must clearly articulate what APER adds beyond OPER applied to VLA-scale training. The novelty claim needs complete rewriting.

2. **Replace the goal-conditioned value function with a more stable priority signal.** The V(s,g) + hindsight relabeling approach has documented instability in offline settings. Consider alternatives: (a) SCIZOR-style progress prediction as a priority signal (but updated periodically), (b) policy loss/gradient magnitude as priority (no auxiliary model needed), (c) embedding-space surprise via the VLA's own representations. These avoid the known instability of offline value function estimation.

3. **Choose benchmarks where data quality is the bottleneck.** Drop LIBERO (saturated at 97%). Use: RoboMimic multi-human (explicitly has mixed-quality operators), OXE subsets with known quality variation, or Sirius-Fleet (where SCIZOR showed 32.9% gains). The evaluation must demonstrate improvement ON TOP of static filtering (SCIZOR → APER), not just vs. uniform sampling.

4. **Quantify the adaptive advantage formally.** When does adaptive prioritization provably outperform static filtering? A theoretical analysis showing conditions under which adaptive > static (e.g., when the optimal data distribution is non-stationary w.r.t. policy parameters) would significantly strengthen the contribution and address the 'why not just filter once' concern.

5. **Be honest about compute overhead.** Profile the actual cost of priority recomputation at VLA scale. If it's 15-30%, the value proposition weakens substantially — why not just run SCIZOR and train 15% longer?

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — UNDERSTATED OVERLAP WITH iw-SFT: The iw-SFT paper (arXiv:2507.12856) already implements adaptive importance weights with time-lagged EMA (θ_q = αθ_q + (1−α)θ) that track the evolving policy during SFT training, with IS correction and per-step clipping. It also evaluates on D4RL and Franka Kitchen manipulation tasks. APER's claimed theoretical contribution — that adaptive IS weights yield tighter bounds than static — is already the core result of iw-SFT ('As q(τ) → p(τ;θ) we have J_iw-SFT(θ) → J(θ)'). The differentiation from iw-SFT needs to be much clearer: what exactly does APER's loss-driven priority add beyond iw-SFT's policy-ratio-driven adaptive weights?", "MISSING COMPETING WORKS — SuRe (arXiv:2511.22367): Surprise-Driven Prioritised Replay for Continual LLM Learning uses NLL/loss-based priority scoring for replay buffer management in LLM training. This is conceptually very close to APER — both use the model's own prediction loss as a priority signal for data selection during training. Must be discussed.", "MISSING COMPETING WORKS — ProFit (arXiv:2601.09195, Jan 2026): Probability-Guided Token Selection for SFT selectively masks low-probability tokens during SFT training, achieving 3-10% gains. PEAR (arXiv:2602.01058, Feb 2026): Importance sampling reweighting at token/block/sequence level for SFT. PBS (arXiv:2602.17066, Feb 2026): Online loss prediction for batch scheduling in LLM training. All three perform online, loss/probability-based data prioritization during SFT — overlapping with APER's core contribution.", "WEAK THEORETICAL NOVELTY: The formal analysis described (gap bounded by cumulative KL divergence, Lipschitz continuity implies adaptive reduces KL, adaptive outperforms static when loss rankings change) consists of straightforward applications of known results. The condition 'adaptive strictly outperforms static when per-transition loss rankings change during training' is near-tautological — of course static is suboptimal when the optimal distribution changes. This does not constitute a novel theoretical contribution for a top venue.", "OHEM PRIOR ART: Online Hard Example Mining (Shrivastava et al., CVPR 2016) is the 10-year-old technique of sampling based on current loss magnitude during training. APER is essentially OHEM applied to VLA SFT with PER's sum-tree data structure and IS correction. This connection should be explicitly discussed and differentiated from.", "MISSING RECENT WORK — RINSE (arXiv:2604.23000, April 2026): 'Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning' proposes smoothness-based quality metrics for IL demonstration curation, achieving 16% higher success with 1/6 of data on RoboMimic. This is a very recent static curation baseline that should be included.", "VENUE DEADLINE CLARIFICATION: CoRL 2026 official Instruction for Authors explicitly states 'the paper submission deadline is Thursday (5/28) EOD rather than Friday.' The HuggingFace tracker shows May 29 at 11:59 UTC, which is effectively May 28 EOD US time. The idea correctly notes May 28 but inconsistently also says May 29 in some places.", "LAZY PRIORITY STALENESS RISK: With lazy updates (only recomputing priorities when sampled), most transitions' priorities become stale. The ε_mix=0.05 uniform mixing only refreshes 5% of samples per step. With large demonstration datasets (100K+ transitions), most transitions will never be resampled during training, keeping permanently stale priorities. The freshness decay helps but only penalizes, never refreshes actual loss values. This needs analysis — what fraction of the buffer actually gets resampled during typical VLA fine-tuning?"]
Feedback: The Round 2 revision addressed Round 1's most critical issue (unstable value function) by switching to loss-driven priorities, which is a much cleaner approach. However, the novelty bar remains unmet for CoRL 2026. The core problem: APER combines known components (OHEM-style loss sampling + PER sum-tree + IS correction from Schaul et al. + freshness decay from FreshPER + theoretical framing from iw-SFT) without adding a genuinely new idea. To reach CoRL quality:

1. **Differentiate sharply from iw-SFT.** iw-SFT already has adaptive IS weights tracking the policy during SFT. APER uses loss magnitude as priority while iw-SFT uses policy ratio — argue why loss-magnitude priorities are better (e.g., loss captures multi-modal difficulty that policy ratios miss in VLA action spaces). Ideally prove this formally.

2. **Add VLA-specific novelty.** Generic PER applied to VLA is engineering. What about VLA-specific signals? E.g., action chunk consistency (some transitions have high loss because the chunk prediction diverges mid-chunk), visual attention entropy (high-attention transitions may be more informative), or multi-modal loss decomposition (separate vision/language/action loss components and prioritize by the bottleneck modality). These would make the contribution VLA-specific rather than a generic application.

3. **Acknowledge and position against LLM SFT data selection work.** SuRe, ProFit, PEAR, PBS all perform online/loss-based data prioritization during LLM training. APER must explain why the VLA setting is different enough to warrant a separate contribution (e.g., continuous action spaces, multi-modal inputs, demonstration quality heterogeneity).

4. **Strengthen the theoretical contribution.** The current analysis (KL divergence bounds, Lipschitz conditions) is textbook. Consider: (a) proving convergence rate improvements specific to multi-modal action distributions, (b) analyzing how action chunking interacts with per-transition priorities, or (c) providing sample complexity bounds showing adaptive PER needs fewer demonstrations to reach a given success rate.

5. **Add RINSE (April 2026) as a baseline.** It's the most recent static curation method and directly competes on RoboMimic.

6. **Quantify the staleness problem.** Run a simple analysis: during VLA fine-tuning with N transitions, what fraction of transitions are sampled at least once? How quickly do loss rankings decorrelate? This empirical characterization would strengthen the motivation.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL MISSING RELATED WORK — EMMA/AdaMix (arXiv:2509.22407, Sep 2025, revised Mar 2026): EMMA introduces AdaMix, a hard-sample-aware training strategy for VLA models that adaptively reweights samples during training based on three metrics: Action Prediction Error (MSE over action chunks), Trajectory Smoothness, and Joint Angle Limitation. AdaMix achieves 17% improvement over fixed-ratio mixing during VLA SFT. This is the closest existing work to CDAP in the VLA training space — it already performs online adaptive sample reweighting during VLA SFT using action prediction loss. The key difference is that AdaMix uses aggregated MSE over the full chunk while CDAP decomposes per-position losses, but this differentiation MUST be explicitly discussed. AdaMix should also be added as a baseline.", "MISSING RELATED WORK — Token Cleaning (arXiv:2502.01968, ICML 2025): Fine-grained token-level data selection for LLM SFT using influence of model updates on each token. Conceptually parallel to CDAP's per-position loss analysis — both move beyond sample-level to sub-sample-level quality assessment during SFT. Should be discussed in the LLM SFT landscape section.", "MISSING RELATED WORK — VGAS (arXiv:2602.07399, Feb 2026): Value-Guided Action-Chunk Selection for Few-Shot VLA Adaptation. Uses Q-Chunk-Former to evaluate and select action chunks at inference time. While inference-time (not training-time), it represents another work that analyzes action chunk quality at a fine-grained level.", "VENUE DEADLINE INACCURACY: The idea states 'abstract deadline: May 25, 2026' in the target_venues field — the actual CoRL 2026 abstract deadline is May 26, 2026 at 11:59 UTC. The paper deadline ambiguity (May 28 EOD Thursday vs. May 29 at 11:59 UTC) persists across sources; the idea should cite the conservative date (May 28 EOD).", "THEORETICAL CLAIMS OVERSTATED: The 'temporal profile evolution theorem' claims that per-position loss profiles evolve from flat to monotonically increasing 'under standard smoothness assumptions.' This is plausible but unproven — it's an empirical hypothesis, not a theorem. Calling it a theorem without proof or stating the exact assumptions risks reviewer pushback. The variance reduction result (chunk-decomposed prioritization reduces variance for heterogeneous chunks) is straightforward and adds limited theoretical novelty. The contact-phase sample complexity bound is a simple calculation, not a deep result.", "EMPIRICAL VALIDATION RISK: The entire contribution rests on the hypothesis that temporal divergence δ captures learning-relevant structure that scalar loss μ misses. If α_δ=0 (scalar PER ablation) performs comparably to full CDAP, the VLA-specific novelty collapses to engineering. This is the paper's make-or-break experiment and is currently untested.", "RINSE VENUE: The idea cites RINSE as 'arXiv April 2026' but it appears to be accepted at ICML 2025 (confirmed at icml.cc/virtual/2025/48703). This should be corrected.", "CAPS VENUE: CAPS (arXiv:2503.01650) is listed as a reference but was accepted at ICRA 2025 (not 2026). While not discussed in the landscape, if cited it should have the correct venue."]
Feedback: Round 3 represents substantial improvement — the pivot from TD-error value functions (Round 1) through scalar loss prioritization (Round 2) to chunk-decomposed temporal profiles is the right direction. The CTP signal is genuinely novel. To reach CoRL quality:

1. **CRITICAL: Add EMMA/AdaMix as related work AND baseline.** EMMA (arXiv:2509.22407) already performs online adaptive sample reweighting during VLA SFT using action prediction MSE. This is your most direct competitor. Differentiation: AdaMix uses aggregated MSE (scalar), CDAP decomposes per-position losses to capture *why* a transition is hard (temporal coherence vs. perception failure). Add AdaMix as baseline (e) between RINSE and scalar-loss PER: 'AdaMix (adaptive scalar-MSE reweighting during VLA SFT, EMMA 2025).' The ablation path becomes: Uniform → AdaMix (scalar adaptive) → Scalar-PER+IS (your α_δ=0 ablation) → full CDAP (temporal decomposition). This progression cleanly isolates CDAP's contribution.

2. **Downgrade theoretical claims to hypotheses.** Present the temporal profile evolution as 'Hypothesis 1' to be validated empirically, not 'Theorem 1.' This is more honest and actually makes the empirical analysis contribution stronger — you're the first to systematically test this hypothesis. CoRL reviewers will appreciate intellectual honesty over inflated theory.

3. **Strengthen the empirical contribution framing.** The first systematic analysis of how intra-chunk temporal loss profiles evolve during VLA SFT is genuinely valuable regardless of whether CDAP outperforms baselines. Frame it as: 'We provide the first empirical characterization of temporal loss profile evolution during VLA SFT, revealing [finding]. CDAP is a practical method motivated by this analysis.' This makes the paper valuable even if gains are modest.

4. **Add Token Cleaning (ICML 2025) to LLM SFT landscape.** It's the closest LLM analogue — moving from sample-level to sub-sample-level (token-level) quality assessment during SFT. The parallel strengthens your positioning: 'Just as Token Cleaning reveals that token-level quality varies within samples for LLM SFT, we show that position-level difficulty varies within action chunks for VLA SFT.'

5. **Fix venue citations.** RINSE → ICML 2025 (not just arXiv). CAPS → ICRA 2025. CoRL abstract deadline → May 26 (not May 25).

6. **Design the α_δ ablation carefully.** The scalar PER (α_δ=0) vs. full CDAP comparison is the single most important experiment. If δ doesn't help, the paper doesn't work. Consider pre-running a small-scale pilot on RoboMimic-MH before committing to the full experimental pipeline.


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
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "type": "user",
  "uuid": "8460eca9-4b2c-4491-b8fb-4e0bba752eb1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T17:37:30.956Z_

```json
{
  "parentUuid": "8460eca9-4b2c-4491-b8fb-4e0bba752eb1",
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
  "uuid": "af852921-ecbd-4d7c-951d-32a5ac8a5d67",
  "timestamp": "2026-05-13T17:37:30.956Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T17:37:30.956Z_

```json
{
  "parentUuid": "af852921-ecbd-4d7c-951d-32a5ac8a5d67",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eda3b09c-913b-4e32-9592-d00dd94802b6",
  "timestamp": "2026-05-13T17:37:30.956Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
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
  "leafUuid": "eda3b09c-913b-4e32-9592-d00dd94802b6",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDAP novelty against AdaMix and temporal decomposition claims",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Assistant

_source line 8 · 2026-05-13T17:37:40.182Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea for CoRL 2026. This is round 4 of 10, so I need to be thorough in my independent verification. The idea has evolved significantly through 3 rounds of revision - from TD-error PER (Round 1) to scalar loss prioritization (Round 2) to chunk-decomposed temporal profiles (Round 3/4).

Let me systematically verify the key claims and search for competing work.

Key things to verify:
1. EMMA/AdaMix - is it properly acknowledged now? Does the differentiation hold?
2. Token Cleaning - properly cited?


3. Whether the temporal divergence signal is genuinely novel or if there's prior work I'm missing
4. Any other competing approaches in this space
5. CoRL 2026 submission timeline and requirements
6. Whether this approach is actually feasible to implement and validate
7. If I've been overstating the theoretical contributions and need to dial back those claims

Let me start searching through the literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda3b09c-913b-4e32-9592-d00dd94802b6",
  "isSidechain": false,
  "requestId": "req_011CazyUHGJnb6Gabc6DHmNy",
  "type": "assistant",
  "uuid": "b3bb8dfe-c98c-44c6-8cf6-307f245e7f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMm3hEDRibYm9wybkEe4gn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21594,
      "cache_read_input_tokens": 11841,
      "output_tokens": 625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21594
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

_source line 9 · 2026-05-13T17:37:40.184Z_

I'll conduct an independent, thorough review of this idea. Let me start by verifying key claims, searching for competing work, and checking deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3bb8dfe-c98c-44c6-8cf6-307f245e7f8b",
  "isSidechain": false,
  "requestId": "req_011CazyUHGJnb6Gabc6DHmNy",
  "type": "assistant",
  "uuid": "81767cc6-0aae-4615-a7c5-5b5a87dc4382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMm3hEDRibYm9wybkEe4gn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21594,
      "cache_read_input_tokens": 11841,
      "output_tokens": 625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21594
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

_source line 10 · 2026-05-13T17:37:45.676Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ER8xGve7t1Eh4aqmgNDTmT`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify EMMA/AdaMix and CoRL deadline",
  "prompt": "I need you to do web research for an ML paper review. Search for and verify:\n\n1. **EMMA/AdaMix paper**: Search for \"EMMA AdaMix VLA adaptive sample reweighting arXiv:2509.22407\". I need to confirm:\n   - Does this paper exist?\n   - What exactly does AdaMix do? Does it aggregate MSE over action chunks into a scalar, or does it decompose per-position losses?\n   - Was it submitted to ICLR 2026? Was it withdrawn?\n   - Try to fetch the actual paper abstract from arxiv.org/abs/2509.22407\n\n2. **CoRL 2026 deadlines**: Search for \"CoRL 2026 deadline submission\" and \"CoRL 2026 Austin\". Verify:\n   - Abstract deadline\n   - Paper deadline\n   - Conference dates (Nov 9-12, 2026?)\n\n3. **RINSE paper venue**: Search for \"RINSE smoothness-driven metrics imitation learning ICML 2025\" to verify it's at ICML 2025 (not just arXiv).\n\nPlease use WebSearch and WebFetch to get authoritative information. Report your findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81767cc6-0aae-4615-a7c5-5b5a87dc4382",
  "isSidechain": false,
  "requestId": "req_011CazyUHGJnb6Gabc6DHmNy",
  "type": "assistant",
  "uuid": "5e1c7e7c-48f5-46fa-bc3c-a7e81ede8db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMm3hEDRibYm9wybkEe4gn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21594,
      "cache_read_input_tokens": 11841,
      "output_tokens": 625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21594
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

_source line 11 · 2026-05-13T17:39:37.716Z_

<details><summary>↩ Tool result · `toolu_01ER8xGve7t1Eh4aqmgNDTmT`</summary>

```text
Now I have enough information for a comprehensive report. Here are my detailed findings:

---

## 1. EMMA / AdaMix Paper (arXiv:2509.22407)

**Paper exists: YES**

- **Title:** "EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer"
- **Authors:** Zhehao Dong, Xiaofeng Wang, Zheng Zhu, et al. (15 authors)
- **arXiv:** [2509.22407](https://arxiv.org/abs/2509.22407) -- v1 submitted Sep 26, 2025; v2 updated Mar 16, 2026
- **OpenReview:** [forum?id=4eKEAeY6Tz](https://openreview.net/forum?id=4eKEAeY6Tz)

**What AdaMix does technically:**

AdaMix **aggregates MSE over action chunks into a scalar** -- it does NOT decompose per-position losses. Specifically, it computes three metrics per sample and combines them:

1. **Action Prediction Error:** MSE between predicted action chunk and ground-truth sequence over a window of at most L frames, aggregated into a **single scalar per sample**: `r^MSE_i = -1/L * sum(||predicted - actual||^2)`
2. **Trajectory Smoothness:** Penalizes abrupt joint movements via second-order differences: `r^Smooth_i = -sum_j |acceleration_j|`
3. **Joint Angle Limitation:** Binary safety indicator for angle thresholds

These three normalized scores (each in [0,1]) are combined into a unified performance score: `s_i = (r^MSE + r^Smooth + r^Limit) / 3`. Sampling weights are then set as: `p(i) proportional to gamma + lambda * (1 - s_i)`, where lower-performing (harder) samples get higher weights.

**ICLR 2026 submission status: WITHDRAWN**

The paper was submitted to ICLR 2026 Conference as submission #9594 on September 17, 2025, modified November 12, 2025, and is listed as a **"Withdrawn Submission"** on OpenReview. No review scores are visible. No withdrawal reason is publicly stated.

---

## 2. CoRL 2026 Deadlines

There is a minor discrepancy between sources, but the authoritative information from the official CoRL website and the HuggingFace AI-deadlines tracker is:

- **Abstract deadline:** May 26, 2026, 11:59 UTC (per HuggingFace tracker; some sources list May 25 AoE which is roughly equivalent)
- **Paper deadline:** The official CoRL contributions page states **May 28, 2026 (AoE)**, with an explicit note: "Please note that the paper submission deadline is Thursday (5/28) EOD rather than Friday!" The HuggingFace tracker lists May 29, 2026 at 11:59 UTC, which is consistent with May 28 AoE (Anywhere on Earth = UTC-12, so May 28 23:59 AoE = May 29 11:59 UTC).
- **Camera-ready deadline:** October 12, 2026 (23:59 AoE)
- **Conference dates:** November 9-12, 2026 (workshops Nov 9, main conference Nov 10-12) -- **your Nov 9-12 date is confirmed**
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701

---

## 3. RINSE Paper Venue

**RINSE is a workshop paper at ICML 2025, NOT a main conference paper.**

- **Title:** "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning"
- **Authors:** Soham Kulkarni, Raayan Dhar, Yuchen Cui
- **Venue:** Poster at the **"DataWorld: Unifying Data Curation Frameworks Across Domains" workshop** at ICML 2025 (Saturday, July 19, Meeting Room 208-209)
- **ICML virtual site listing:** [icml.cc/virtual/2025/48703](https://icml.cc/virtual/2025/48703)
- **arXiv preprint:** [2604.23000](https://arxiv.org/abs/2604.23000) (submitted April 24, 2026 -- notably after the workshop, suggesting the arXiv version may be a revised/extended version)

The arXiv preprint itself does not claim main-conference acceptance. The ICML virtual site confirms it as a workshop poster presentation only. So if someone claims "RINSE is at ICML 2025," that is technically true but potentially misleading -- it is at an **ICML 2025 workshop**, not in the main conference proceedings.

---

Sources:
- [EMMA on arXiv](https://arxiv.org/abs/2509.22407)
- [EMMA on OpenReview (withdrawn)](https://openreview.net/forum?id=4eKEAeY6Tz)
- [EMMA HTML version with AdaMix details](https://arxiv.org/html/2509.22407v1)
- [CoRL 2026 official site](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 on HuggingFace AI-Deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)
- [RINSE at ICML 2025 virtual site](https://icml.cc/virtual/2025/48703)
- [RINSE arXiv preprint](https://arxiv.org/abs/2604.23000)
- [DataWorld workshop at ICML 2025](https://dataworldicml2025.github.io/)

agentId: a7ae09b19969377d6 (use SendMessage with to: 'a7ae09b19969377d6' to continue this agent)
&lt;usage>total_tokens: 23035
tool_uses: 20
duration_ms: 112033&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e1c7e7c-48f5-46fa-bc3c-a7e81ede8db3",
  "isSidechain": false,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "type": "user",
  "uuid": "c47bd307-7a80-438e-856a-b3b5dafa71bf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to do web research for an ML paper review. Search for and verify:\n\n1. **EMMA/AdaMix paper**: Search for \"EMMA AdaMix VLA adaptive sample reweighting arXiv:2509.22407\". I need to confirm:\n   - Does this paper exist?\n   - What exactly does AdaMix do? Does it aggregate MSE over action chunks into a scalar, or does it decompose per-position losses?\n   - Was it submitted to ICLR 2026? Was it withdrawn?\n   - Try to fetch the actual paper abstract from arxiv.org/abs/2509.22407\n\n2. **CoRL 2026 deadlines**: Search for \"CoRL 2026 deadline submission\" and \"CoRL 2026 Austin\". Verify:\n   - Abstract deadline\n   - Paper deadline\n   - Conference dates (Nov 9-12, 2026?)\n\n3. **RINSE paper venue**: Search for \"RINSE smoothness-driven metrics imitation learning ICML 2025\" to verify it's at ICML 2025 (not just arXiv).\n\nPlease use WebSearch and WebFetch to get authoritative information. Report your findings in detail.",
    "agentId": "a7ae09b19969377d6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information for a comprehensive report. Here are my detailed findings:\n\n---\n\n## 1. EMMA / AdaMix Paper (arXiv:2509.22407)\n\n**Paper exists: YES**\n\n- **Title:** \"EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer\"\n- **Authors:** Zhehao Dong, Xiaofeng Wang, Zheng Zhu, et al. (15 authors)\n- **arXiv:** [2509.22407](https://arxiv.org/abs/2509.22407) -- v1 submitted Sep 26, 2025; v2 updated Mar 16, 2026\n- **OpenReview:** [forum?id=4eKEAeY6Tz](https://openreview.net/forum?id=4eKEAeY6Tz)\n\n**What AdaMix does technically:**\n\nAdaMix **aggregates MSE over action chunks into a scalar** -- it does NOT decompose per-position losses. Specifically, it computes three metrics per sample and combines them:\n\n1. **Action Prediction Error:** MSE between predicted action chunk and ground-truth sequence over a window of at most L frames, aggregated into a **single scalar per sample**: `r^MSE_i = -1/L * sum(||predicted - actual||^2)`\n2. **Trajectory Smoothness:** Penalizes abrupt joint movements via second-order differences: `r^Smooth_i = -sum_j |acceleration_j|`\n3. **Joint Angle Limitation:** Binary safety indicator for angle thresholds\n\nThese three normalized scores (each in [0,1]) are combined into a unified performance score: `s_i = (r^MSE + r^Smooth + r^Limit) / 3`. Sampling weights are then set as: `p(i) proportional to gamma + lambda * (1 - s_i)`, where lower-performing (harder) samples get higher weights.\n\n**ICLR 2026 submission status: WITHDRAWN**\n\nThe paper was submitted to ICLR 2026 Conference as submission #9594 on September 17, 2025, modified November 12, 2025, and is listed as a **\"Withdrawn Submission\"** on OpenReview. No review scores are visible. No withdrawal reason is publicly stated.\n\n---\n\n## 2. CoRL 2026 Deadlines\n\nThere is a minor discrepancy between sources, but the authoritative information from the official CoRL website and the HuggingFace AI-deadlines tracker is:\n\n- **Abstract deadline:** May 26, 2026, 11:59 UTC (per HuggingFace tracker; some sources list May 25 AoE which is roughly equivalent)\n- **Paper deadline:** The official CoRL contributions page states **May 28, 2026 (AoE)**, with an explicit note: \"Please note that the paper submission deadline is Thursday (5/28) EOD rather than Friday!\" The HuggingFace tracker lists May 29, 2026 at 11:59 UTC, which is consistent with May 28 AoE (Anywhere on Earth = UTC-12, so May 28 23:59 AoE = May 29 11:59 UTC).\n- **Camera-ready deadline:** October 12, 2026 (23:59 AoE)\n- **Conference dates:** November 9-12, 2026 (workshops Nov 9, main conference Nov 10-12) -- **your Nov 9-12 date is confirmed**\n- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701\n\n---\n\n## 3. RINSE Paper Venue\n\n**RINSE is a workshop paper at ICML 2025, NOT a main conference paper.**\n\n- **Title:** \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning\"\n- **Authors:** Soham Kulkarni, Raayan Dhar, Yuchen Cui\n- **Venue:** Poster at the **\"DataWorld: Unifying Data Curation Frameworks Across Domains\" workshop** at ICML 2025 (Saturday, July 19, Meeting Room 208-209)\n- **ICML virtual site listing:** [icml.cc/virtual/2025/48703](https://icml.cc/virtual/2025/48703)\n- **arXiv preprint:** [2604.23000](https://arxiv.org/abs/2604.23000) (submitted April 24, 2026 -- notably after the workshop, suggesting the arXiv version may be a revised/extended version)\n\nThe arXiv preprint itself does not claim main-conference acceptance. The ICML virtual site confirms it as a workshop poster presentation only. So if someone claims \"RINSE is at ICML 2025,\" that is technically true but potentially misleading -- it is at an **ICML 2025 workshop**, not in the main conference proceedings.\n\n---\n\nSources:\n- [EMMA on arXiv](https://arxiv.org/abs/2509.22407)\n- [EMMA on OpenReview (withdrawn)](https://openreview.net/forum?id=4eKEAeY6Tz)\n- [EMMA HTML version with AdaMix details](https://arxiv.org/html/2509.22407v1)\n- [CoRL 2026 official site](https://www.corl.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [CoRL 2026 on HuggingFace AI-Deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)\n- [RINSE at ICML 2025 virtual site](https://icml.cc/virtual/2025/48703)\n- [RINSE arXiv preprint](https://arxiv.org/abs/2604.23000)\n- [DataWorld workshop at ICML 2025](https://dataworldicml2025.github.io/)"
      }
    ],
    "totalDurationMs": 112033,
    "totalTokens": 23035,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 21270,
      "output_tokens": 1527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1527,
          "cache_read_input_tokens": 21270,
          "cache_creation_input_tokens": 237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 237,
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
  "sourceToolAssistantUUID": "5e1c7e7c-48f5-46fa-bc3c-a7e81ede8db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T17:39:48.241Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017vpQbVwTDHQHUbeh8HLm81`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing work on action chunk loss decomposition",
  "prompt": "I'm reviewing an ML paper idea called \"CDAP\" that proposes decomposing per-position losses within action chunks during VLA (Vision-Language-Action) model training. The key claim is that no prior work exploits the *intra-chunk temporal loss profile* as a priority signal for VLA training.\n\nSearch for competing/related work that might invalidate this novelty claim. Use WebSearch for each of these queries:\n\n1. \"action chunk loss decomposition VLA training 2025 2026\" \n2. \"per-position loss action chunking robot learning\"\n3. \"temporal loss profile robot imitation learning\"\n4. \"action chunk prediction quality degradation VLA\"\n5. \"sub-chunk loss analysis robot manipulation\"\n6. \"intra-chunk loss weighting VLA fine-tuning\"\n7. Search for \"DAM-VLA dual action model\" to verify what exactly DAM-VLA does with chunk-level weighting\n8. Search for \"VLA Knows Its Limits action sinks arXiv:2602.21445\" to verify the claim about temporal prediction quality degradation within chunks\n\nFor each search, report what you find — especially any paper that decomposes action chunk losses at a per-position level during training (not inference). I need to know if the novelty claim holds up."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c47bd307-7a80-438e-856a-b3b5dafa71bf",
  "isSidechain": false,
  "requestId": "req_011Cazydd4vgwtHRwe7KJCXe",
  "type": "assistant",
  "uuid": "fb918ca3-293d-4cae-8a83-5c898a5742d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EFV8D6zubtPauHp3x2Lhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 33435,
      "output_tokens": 1190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1190,
          "cache_read_input_tokens": 33435,
          "cache_creation_input_tokens": 2230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2230
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

_source line 13 · 2026-05-13T17:39:56.425Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011qVthJS73rUCHeFWKrf6BY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for LLM SFT data selection and PER work",
  "prompt": "I'm reviewing an ML paper idea that applies prioritized experience replay with chunk-decomposed loss to VLA (Vision-Language-Action) model SFT. I need to verify several related works and find any missing ones.\n\nSearch for:\n\n1. \"Token Cleaning ICML 2025 arXiv:2502.01968\" — verify this exists and is ICML 2025 Spotlight\n2. \"iw-SFT supervised fine tuning reinforcement learning arXiv:2507.12856\" — verify this exists\n3. \"Freshness-Aware Prioritized Experience Replay LLM VLM arXiv:2604.16918\" — verify this exists\n4. \"SCIZOR self-supervised data curation imitation learning ICRA 2026\" — verify venue\n5. \"CUPID curating data influence functions CoRL 2025\" — verify venue\n6. \"DataMIL datamodels imitation learning ICLR 2026\" — verify venue\n7. \"adaptive sample weighting robot learning 2026\" — find any new competing work\n8. \"prioritized replay supervised fine-tuning continuous action 2025 2026\" — find concurrent work\n\nFor each, use WebSearch to find the paper and report: does it exist? What venue? What does it actually do? Is there any work I might be missing that decomposes losses at sub-sample level for robot learning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb918ca3-293d-4cae-8a83-5c898a5742d9",
  "isSidechain": false,
  "requestId": "req_011Cazydd4vgwtHRwe7KJCXe",
  "type": "assistant",
  "uuid": "866f6b76-5ee1-497f-a125-7b55d5e6d37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EFV8D6zubtPauHp3x2Lhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 33435,
      "output_tokens": 1190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1190,
          "cache_read_input_tokens": 33435,
          "cache_creation_input_tokens": 2230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2230
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

_source line 14 · 2026-05-13T17:40:05.330Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019ezpb7VmAR3D5tSN62AUc2`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for anti-evidence and feasibility concerns",
  "prompt": "I'm reviewing an ML paper idea called \"CDAP\" for VLA training. I need to find evidence AGAINST its core assumptions and check feasibility. Search for:\n\n1. \"action chunk prediction loss uniform across positions\" — does loss actually vary meaningfully across chunk positions, or is it roughly uniform?\n2. \"VLA action chunking loss analysis\" — any existing analysis of how losses distribute within action chunks\n3. \"OpenVLA-OFT fine-tuning cost GPU hours\" — what's the actual compute cost for fine-tuning OpenVLA?\n4. \"Sirius-Fleet dataset availability\" — is this dataset publicly available?\n5. \"prioritized experience replay doesn't help\" OR \"prioritized replay negative results\" — any evidence PER-style methods fail\n6. \"RoboMimic multi-human benchmark results 2025 2026\" — what are current SOTA results?\n7. \"SimplerEnv VLA evaluation benchmark\" — verify this exists and is standard\n8. \"CAPS context-aware priority sampling ICRA 2025 arXiv:2503.01650\" — verify this exists and what it does (the idea cites it but doesn't discuss it much)\n\nReport findings in detail. I'm especially interested in whether there's evidence that per-position loss variation within action chunks is negligible (which would undermine the entire idea)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866f6b76-5ee1-497f-a125-7b55d5e6d37b",
  "isSidechain": false,
  "requestId": "req_011Cazydd4vgwtHRwe7KJCXe",
  "type": "assistant",
  "uuid": "9f3f513c-49dd-40cb-9d97-3bce017419a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EFV8D6zubtPauHp3x2Lhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 33435,
      "output_tokens": 1190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1190,
          "cache_read_input_tokens": 33435,
          "cache_creation_input_tokens": 2230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2230
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

_source line 15 · 2026-05-13T17:42:30.792Z_

<details><summary>↩ Tool result · `toolu_011qVthJS73rUCHeFWKrf6BY`</summary>

```text
Now I have a thorough picture. Let me compile the full report.

Here is my comprehensive verification report for each paper, plus additional related work findings:

---

## 1. Token Cleaning (arXiv:2502.01968)

**Exists:** Yes. "Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning" by Jinlong Pang et al., UC Santa Cruz.

**Venue:** ICML 2025, but the claim that it is a **Spotlight** appears to be **incorrect or unverifiable**. The ICML virtual site lists it under `icml.cc/virtual/2025/poster/43777` -- i.e., as a **Poster**, not a Spotlight. The GitHub repo (`UCSC-REAL/TokenCleaning`) labels it as `[ICML 2025]` without the Spotlight tag, and it does not appear in ICML 2025 spotlight lists on papers.cool. You should double-check, but available evidence points to **Poster**, not Spotlight.

**What it does:** Investigates token quality from a noisy-label perspective. Proposes a pipeline that scores individual token quality by examining the influence of model updates on each token, then applies threshold-based separation to filter uninformative tokens. Two modes: Fixed-Model Cleaning (one-shot) and Self-Evolving Cleaning (iterative). This is directly relevant to your paper as it decomposes loss at the sub-sample (token) level for SFT.

---

## 2. iw-SFT (arXiv:2507.12856)

**Exists:** Yes. "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)" by Chongli Qin and Jost Tobias Springenberg.

**Venue:** As of my search, the paper is marked as **"Preprint. Under review."** No confirmed venue acceptance found. It has **not** been confirmed at any major conference (NeurIPS, ICML, ICLR) based on available evidence.

**What it does:** Shows SFT on curated data can be understood as maximizing a lower bound on the RL objective in a sparse reward setting. Proposes importance weighted SFT (iw-SFT), which re-weights the MLE objective to optimize a tighter bound. Generalizes to quality-scored data. Results competitive with advanced RL algorithms both for LLMs (66.7% on AIME 2024) and continuous control tasks. Highly relevant -- it provides per-sample importance weighting for SFT.

---

## 3. Freshness-Aware PER (arXiv:2604.16918)

**Exists:** Yes. "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning" by Weiyu Ma et al. (KAUST, CAS, UCL).

**Venue:** Posted to arXiv on April 18, 2026. **No confirmed venue** -- appears to be a preprint, likely under review. Could not find acceptance at ICML 2026, NeurIPS 2026, or elsewhere.

**What it does:** Addresses the failure of standard PER when applied to LLM/VLM RL. The core problem is priority staleness: rapid policy evolution of billion-parameter models makes stored priorities stale. Solution: augments PER priority with multiplicative exponential age decay grounded in effective sample size analysis. Achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs. on-policy baselines. Directly relevant as it adapts prioritized replay to large model training, though for RL not SFT.

---

## 4. SCIZOR (arXiv:2505.22626)

**Exists:** Yes. "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning" by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, Yuke Zhu (UT Austin RPL).

**Venue:** **ICRA 2026 -- confirmed.** Author Huihan Liu posted confirmation on X (Twitter), and the paper appears on OpenReview for ICRA 2026.

**What it does:** Targets two sources of low-quality data: suboptimal data (wrong actions) and redundant data (repetitive patterns). Uses a progress-prediction model to flag frames that fail to make task progress (no reward signals needed), plus joint visual-action embeddings clustered to detect and discard look-alike segments. Averages 15.4% improvement across large-scale imitation learning benchmarks. Relevant as a sample-level curation method (not sub-sample/token-level).

---

## 5. CUPID (arXiv:2506.19121)

**Exists:** Yes. "CUPID: Curating Data your Robot Loves with Influence Functions" by Christopher Agia et al.

**Venue:** **CoRL 2025 -- confirmed.** Published in Proceedings of Machine Learning Research (PMLR), Vol. 305 (`proceedings.mlr.press/v305/agia25a.html`). Also on OpenReview.

**What it does:** Uses influence functions to estimate how each training demonstration affects the policy's expected return, enabling ranking/selection of demonstrations by their impact on closed-loop performance. Can filter harmful demonstrations and subselect helpful new trajectories. Training with <33% of curated data achieves SOTA on RoboMimic. Works at the demonstration (sample) level, not sub-sample level.

---

## 6. DataMIL (arXiv:2505.09603)

**Exists:** Yes. "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels" (UT Austin RobIn Lab).

**Venue:** **ICLR 2026 -- confirmed** (appears on OpenReview as ICLR 2026 conference paper). Specific presentation tier (oral/spotlight/poster) could not be confirmed from search results, but it is accepted.

**What it does:** Policy-driven data selection framework using the datamodels paradigm. Instead of filtering based on human notions of quality, it directly optimizes data selection for task success using a novel surrogate loss on task-specific data. Validated on 60+ simulation and real-world manipulation tasks including Open X-Embodiment datasets. Shows ~10% performance boost on MetaWorld 50 tasks. Operates at sample level.

---

## 7-8. Additional/Competing/Concurrent Work Found

### PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)
- **arXiv:2511.00091** -- "Probe, Learn, Distill" framework
- Accepted at **ICLR 2026**
- Three-stage framework: (1) freeze VLA, train residual actors via off-policy RL; (2) distribution-aware data collection biasing interventions toward states the base policy visits; (3) distill curated trajectories back via SFT
- Achieves 99% on LIBERO, 50%+ gains on SimplerEnv
- Relevant because it uses distribution-aware replay and data quality filtering before SFT distillation

### "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority" (arXiv:2602.01227)
- Posted February 2026, no confirmed venue
- Formalizes SFT as distribution reshaping via token-level priority
- Categorizes approaches into Positive Priority (noise filtration) and Signed Priority (toxic mode unlearning)
- Directly relevant as a framework paper analyzing per-token loss weighting for SFT

### "Gradients Must Earn Their Influence: Unifying SFT with Generalized Entropic Objectives" (arXiv:2602.11424)
- February 2026 preprint
- Proposes generalized entropic objectives for SFT that modulate gradient influence
- Related to per-token importance weighting

### Entropy-Adaptive Fine-Tuning (EAFT) (arXiv:2601.02151)
- January 2026 preprint
- Uses soft gating mechanism that dynamically modulates training loss based on token-level entropy
- Directly relevant as a token-level dynamic loss reweighting method

### Action Preference Optimization with Adaptive Reweighting for VLA (arXiv:2506.07127)
- Adaptive sample-wise weighting for VLA preference optimization
- Increases weight of samples with high action prediction errors for desirable data
- Relevant as it does sample-level adaptive weighting specifically for VLA models with continuous actions

### Q-Chunking / Chunking the Critic (ICLR 2026)
- Published as ICLR 2026 conference paper
- Recipe for improving RL with action chunking in long-horizon sparse-reward tasks
- Relevant if your chunk-decomposed loss relates to action chunking

---

## Summary: Key Findings and Gaps

**Verification results:**
| Paper | Exists? | Claimed Venue | Actual Venue |
|-------|---------|---------------|--------------|
| Token Cleaning | Yes | ICML 2025 Spotlight | ICML 2025 **Poster** (Spotlight unverified) |
| iw-SFT | Yes | (not specified) | **Preprint, under review** |
| Freshness-Aware PER | Yes | (not specified) | **Preprint** (April 2026) |
| SCIZOR | Yes | ICRA 2026 | **ICRA 2026 -- confirmed** |
| CUPID | Yes | CoRL 2025 | **CoRL 2025 -- confirmed** |
| DataMIL | Yes | ICLR 2026 | **ICLR 2026 -- confirmed** |

**Potentially missing related work for sub-sample level loss decomposition in robot learning:**
1. **Token Priority paper** (arXiv:2602.01227) -- formalizes per-token priority weighting for SFT
2. **EAFT** (arXiv:2601.02151) -- token-level entropy-based dynamic loss modulation
3. **PLD** (ICLR 2026) -- distribution-aware replay + SFT distillation for VLA self-improvement
4. **Action Preference Optimization** (arXiv:2506.07127) -- adaptive sample-wise reweighting for VLA with continuous actions

The existing landscape shows: CUPID, SCIZOR, and DataMIL operate at the **sample/demonstration level**; Token Cleaning and the Token Priority paper operate at the **token level for LLM SFT**; but there appears to be a gap in work that specifically decomposes losses at a **chunk level** (sub-sample but not individual token) for **VLA/robot policy SFT with continuous actions** -- which is the niche your paper idea targets.

Sources:
- [Token Cleaning (arXiv:2502.01968)](https://arxiv.org/abs/2502.01968)
- [Token Cleaning ICML Poster Page](https://icml.cc/virtual/2025/poster/43777)
- [Token Cleaning GitHub](https://github.com/UCSC-REAL/TokenCleaning)
- [iw-SFT (arXiv:2507.12856)](https://arxiv.org/abs/2507.12856)
- [Freshness-Aware PER (arXiv:2604.16918)](https://arxiv.org/abs/2604.16918)
- [SCIZOR (arXiv:2505.22626)](https://arxiv.org/abs/2505.22626)
- [SCIZOR ICRA 2026 confirmation](https://x.com/huihan_liu/status/2017698931493195899)
- [CUPID (arXiv:2506.19121)](https://arxiv.org/abs/2506.19121)
- [CUPID CoRL 2025 proceedings](https://proceedings.mlr.press/v305/agia25a.html)
- [DataMIL (arXiv:2505.09603)](https://arxiv.org/abs/2505.09603)
- [DataMIL OpenReview](https://openreview.net/forum?id=AcTsKglDdh)
- [PLD: Self-Improving VLA (ICLR 2026)](https://wenlixiao.com/self-improve-VLA-PLD)
- [Token Priority (arXiv:2602.01227)](https://arxiv.org/abs/2602.01227)
- [EAFT (arXiv:2601.02151)](https://arxiv.org/html/2601.02151v1)
- [Action Preference Optimization (arXiv:2506.07127)](https://arxiv.org/html/2506.07127v1)
- [ICML 2025 Spotlight List (papers.cool)](https://papers.cool/venue/ICML.2025?group=Spotlight)

agentId: aa8e627ca68bfa3d5 (use SendMessage with to: 'aa8e627ca68bfa3d5' to continue this agent)
&lt;usage>total_tokens: 33038
tool_uses: 22
duration_ms: 154364&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "866f6b76-5ee1-497f-a125-7b55d5e6d37b",
  "isSidechain": false,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "type": "user",
  "uuid": "174d4153-1736-4c82-93f1-df725b5b7c46",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML paper idea that applies prioritized experience replay with chunk-decomposed loss to VLA (Vision-Language-Action) model SFT. I need to verify several related works and find any missing ones.\n\nSearch for:\n\n1. \"Token Cleaning ICML 2025 arXiv:2502.01968\" — verify this exists and is ICML 2025 Spotlight\n2. \"iw-SFT supervised fine tuning reinforcement learning arXiv:2507.12856\" — verify this exists\n3. \"Freshness-Aware Prioritized Experience Replay LLM VLM arXiv:2604.16918\" — verify this exists\n4. \"SCIZOR self-supervised data curation imitation learning ICRA 2026\" — verify venue\n5. \"CUPID curating data influence functions CoRL 2025\" — verify venue\n6. \"DataMIL datamodels imitation learning ICLR 2026\" — verify venue\n7. \"adaptive sample weighting robot learning 2026\" — find any new competing work\n8. \"prioritized replay supervised fine-tuning continuous action 2025 2026\" — find concurrent work\n\nFor each, use WebSearch to find the paper and report: does it exist? What venue? What does it actually do? Is there any work I might be missing that decomposes losses at sub-sample level for robot learning?",
    "agentId": "aa8e627ca68bfa3d5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a thorough picture. Let me compile the full report.\n\nHere is my comprehensive verification report for each paper, plus additional related work findings:\n\n---\n\n## 1. Token Cleaning (arXiv:2502.01968)\n\n**Exists:** Yes. \"Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning\" by Jinlong Pang et al., UC Santa Cruz.\n\n**Venue:** ICML 2025, but the claim that it is a **Spotlight** appears to be **incorrect or unverifiable**. The ICML virtual site lists it under `icml.cc/virtual/2025/poster/43777` -- i.e., as a **Poster**, not a Spotlight. The GitHub repo (`UCSC-REAL/TokenCleaning`) labels it as `[ICML 2025]` without the Spotlight tag, and it does not appear in ICML 2025 spotlight lists on papers.cool. You should double-check, but available evidence points to **Poster**, not Spotlight.\n\n**What it does:** Investigates token quality from a noisy-label perspective. Proposes a pipeline that scores individual token quality by examining the influence of model updates on each token, then applies threshold-based separation to filter uninformative tokens. Two modes: Fixed-Model Cleaning (one-shot) and Self-Evolving Cleaning (iterative). This is directly relevant to your paper as it decomposes loss at the sub-sample (token) level for SFT.\n\n---\n\n## 2. iw-SFT (arXiv:2507.12856)\n\n**Exists:** Yes. \"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)\" by Chongli Qin and Jost Tobias Springenberg.\n\n**Venue:** As of my search, the paper is marked as **\"Preprint. Under review.\"** No confirmed venue acceptance found. It has **not** been confirmed at any major conference (NeurIPS, ICML, ICLR) based on available evidence.\n\n**What it does:** Shows SFT on curated data can be understood as maximizing a lower bound on the RL objective in a sparse reward setting. Proposes importance weighted SFT (iw-SFT), which re-weights the MLE objective to optimize a tighter bound. Generalizes to quality-scored data. Results competitive with advanced RL algorithms both for LLMs (66.7% on AIME 2024) and continuous control tasks. Highly relevant -- it provides per-sample importance weighting for SFT.\n\n---\n\n## 3. Freshness-Aware PER (arXiv:2604.16918)\n\n**Exists:** Yes. \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning\" by Weiyu Ma et al. (KAUST, CAS, UCL).\n\n**Venue:** Posted to arXiv on April 18, 2026. **No confirmed venue** -- appears to be a preprint, likely under review. Could not find acceptance at ICML 2026, NeurIPS 2026, or elsewhere.\n\n**What it does:** Addresses the failure of standard PER when applied to LLM/VLM RL. The core problem is priority staleness: rapid policy evolution of billion-parameter models makes stored priorities stale. Solution: augments PER priority with multiplicative exponential age decay grounded in effective sample size analysis. Achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs. on-policy baselines. Directly relevant as it adapts prioritized replay to large model training, though for RL not SFT.\n\n---\n\n## 4. SCIZOR (arXiv:2505.22626)\n\n**Exists:** Yes. \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning\" by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, Yuke Zhu (UT Austin RPL).\n\n**Venue:** **ICRA 2026 -- confirmed.** Author Huihan Liu posted confirmation on X (Twitter), and the paper appears on OpenReview for ICRA 2026.\n\n**What it does:** Targets two sources of low-quality data: suboptimal data (wrong actions) and redundant data (repetitive patterns). Uses a progress-prediction model to flag frames that fail to make task progress (no reward signals needed), plus joint visual-action embeddings clustered to detect and discard look-alike segments. Averages 15.4% improvement across large-scale imitation learning benchmarks. Relevant as a sample-level curation method (not sub-sample/token-level).\n\n---\n\n## 5. CUPID (arXiv:2506.19121)\n\n**Exists:** Yes. \"CUPID: Curating Data your Robot Loves with Influence Functions\" by Christopher Agia et al.\n\n**Venue:** **CoRL 2025 -- confirmed.** Published in Proceedings of Machine Learning Research (PMLR), Vol. 305 (`proceedings.mlr.press/v305/agia25a.html`). Also on OpenReview.\n\n**What it does:** Uses influence functions to estimate how each training demonstration affects the policy's expected return, enabling ranking/selection of demonstrations by their impact on closed-loop performance. Can filter harmful demonstrations and subselect helpful new trajectories. Training with <33% of curated data achieves SOTA on RoboMimic. Works at the demonstration (sample) level, not sub-sample level.\n\n---\n\n## 6. DataMIL (arXiv:2505.09603)\n\n**Exists:** Yes. \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels\" (UT Austin RobIn Lab).\n\n**Venue:** **ICLR 2026 -- confirmed** (appears on OpenReview as ICLR 2026 conference paper). Specific presentation tier (oral/spotlight/poster) could not be confirmed from search results, but it is accepted.\n\n**What it does:** Policy-driven data selection framework using the datamodels paradigm. Instead of filtering based on human notions of quality, it directly optimizes data selection for task success using a novel surrogate loss on task-specific data. Validated on 60+ simulation and real-world manipulation tasks including Open X-Embodiment datasets. Shows ~10% performance boost on MetaWorld 50 tasks. Operates at sample level.\n\n---\n\n## 7-8. Additional/Competing/Concurrent Work Found\n\n### PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)\n- **arXiv:2511.00091** -- \"Probe, Learn, Distill\" framework\n- Accepted at **ICLR 2026**\n- Three-stage framework: (1) freeze VLA, train residual actors via off-policy RL; (2) distribution-aware data collection biasing interventions toward states the base policy visits; (3) distill curated trajectories back via SFT\n- Achieves 99% on LIBERO, 50%+ gains on SimplerEnv\n- Relevant because it uses distribution-aware replay and data quality filtering before SFT distillation\n\n### \"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority\" (arXiv:2602.01227)\n- Posted February 2026, no confirmed venue\n- Formalizes SFT as distribution reshaping via token-level priority\n- Categorizes approaches into Positive Priority (noise filtration) and Signed Priority (toxic mode unlearning)\n- Directly relevant as a framework paper analyzing per-token loss weighting for SFT\n\n### \"Gradients Must Earn Their Influence: Unifying SFT with Generalized Entropic Objectives\" (arXiv:2602.11424)\n- February 2026 preprint\n- Proposes generalized entropic objectives for SFT that modulate gradient influence\n- Related to per-token importance weighting\n\n### Entropy-Adaptive Fine-Tuning (EAFT) (arXiv:2601.02151)\n- January 2026 preprint\n- Uses soft gating mechanism that dynamically modulates training loss based on token-level entropy\n- Directly relevant as a token-level dynamic loss reweighting method\n\n### Action Preference Optimization with Adaptive Reweighting for VLA (arXiv:2506.07127)\n- Adaptive sample-wise weighting for VLA preference optimization\n- Increases weight of samples with high action prediction errors for desirable data\n- Relevant as it does sample-level adaptive weighting specifically for VLA models with continuous actions\n\n### Q-Chunking / Chunking the Critic (ICLR 2026)\n- Published as ICLR 2026 conference paper\n- Recipe for improving RL with action chunking in long-horizon sparse-reward tasks\n- Relevant if your chunk-decomposed loss relates to action chunking\n\n---\n\n## Summary: Key Findings and Gaps\n\n**Verification results:**\n| Paper | Exists? | Claimed Venue | Actual Venue |\n|-------|---------|---------------|--------------|\n| Token Cleaning | Yes | ICML 2025 Spotlight | ICML 2025 **Poster** (Spotlight unverified) |\n| iw-SFT | Yes | (not specified) | **Preprint, under review** |\n| Freshness-Aware PER | Yes | (not specified) | **Preprint** (April 2026) |\n| SCIZOR | Yes | ICRA 2026 | **ICRA 2026 -- confirmed** |\n| CUPID | Yes | CoRL 2025 | **CoRL 2025 -- confirmed** |\n| DataMIL | Yes | ICLR 2026 | **ICLR 2026 -- confirmed** |\n\n**Potentially missing related work for sub-sample level loss decomposition in robot learning:**\n1. **Token Priority paper** (arXiv:2602.01227) -- formalizes per-token priority weighting for SFT\n2. **EAFT** (arXiv:2601.02151) -- token-level entropy-based dynamic loss modulation\n3. **PLD** (ICLR 2026) -- distribution-aware replay + SFT distillation for VLA self-improvement\n4. **Action Preference Optimization** (arXiv:2506.07127) -- adaptive sample-wise reweighting for VLA with continuous actions\n\nThe existing landscape shows: CUPID, SCIZOR, and DataMIL operate at the **sample/demonstration level**; Token Cleaning and the Token Priority paper operate at the **token level for LLM SFT**; but there appears to be a gap in work that specifically decomposes losses at a **chunk level** (sub-sample but not individual token) for **VLA/robot policy SFT with continuous actions** -- which is the niche your paper idea targets.\n\nSources:\n- [Token Cleaning (arXiv:2502.01968)](https://arxiv.org/abs/2502.01968)\n- [Token Cleaning ICML Poster Page](https://icml.cc/virtual/2025/poster/43777)\n- [Token Cleaning GitHub](https://github.com/UCSC-REAL/TokenCleaning)\n- [iw-SFT (arXiv:2507.12856)](https://arxiv.org/abs/2507.12856)\n- [Freshness-Aware PER (arXiv:2604.16918)](https://arxiv.org/abs/2604.16918)\n- [SCIZOR (arXiv:2505.22626)](https://arxiv.org/abs/2505.22626)\n- [SCIZOR ICRA 2026 confirmation](https://x.com/huihan_liu/status/2017698931493195899)\n- [CUPID (arXiv:2506.19121)](https://arxiv.org/abs/2506.19121)\n- [CUPID CoRL 2025 proceedings](https://proceedings.mlr.press/v305/agia25a.html)\n- [DataMIL (arXiv:2505.09603)](https://arxiv.org/abs/2505.09603)\n- [DataMIL OpenReview](https://openreview.net/forum?id=AcTsKglDdh)\n- [PLD: Self-Improving VLA (ICLR 2026)](https://wenlixiao.com/self-improve-VLA-PLD)\n- [Token Priority (arXiv:2602.01227)](https://arxiv.org/abs/2602.01227)\n- [EAFT (arXiv:2601.02151)](https://arxiv.org/html/2601.02151v1)\n- [Action Preference Optimization (arXiv:2506.07127)](https://arxiv.org/html/2506.07127v1)\n- [ICML 2025 Spotlight List (papers.cool)](https://papers.cool/venue/ICML.2025?group=Spotlight)"
      }
    ],
    "totalDurationMs": 154364,
    "totalTokens": 33038,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 27811,
      "output_tokens": 3173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3173,
          "cache_read_input_tokens": 27811,
          "cache_creation_input_tokens": 2053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2053,
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
  "sourceToolAssistantUUID": "866f6b76-5ee1-497f-a125-7b55d5e6d37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "174d4153-1736-4c82-93f1-df725b5b7c46",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDAP novelty against AdaMix and temporal decomposition claims",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Tool result

_source line 18 · 2026-05-13T17:43:18.663Z_

<details><summary>↩ Tool result · `toolu_019ezpb7VmAR3D5tSN62AUc2`</summary>

```text
Now I have sufficient evidence to compile a comprehensive report. Here is my detailed analysis:

---

## Detailed Findings: Evidence Against CDAP Core Assumptions

### 1. Per-Position Loss Variation Within Action Chunks

**This is the most critical question, and the evidence is nuanced -- it partially supports and partially undermines CDAP.**

**Evidence that loss DOES vary across chunk positions (supports CDAP's premise):**
- **WorldVLA (arXiv:2506.21539)** provides the strongest empirical evidence. They show grasping success rate drops 10-50% with naive autoregressive action chunking. Their ablation (Table 3): without chunking, average success rate is 62.8%; with naive chunking, it drops to 54.0%. Their fix (attention masking) recovers to 76.6%. This confirms that later positions in autoregressive chunks accumulate error.
- The "Leave No Observation Behind" paper (arXiv:2509.23224) introduces a per-step correction module with positional sinusoidal embeddings encoding the index within the chunk, implicitly acknowledging that different positions have different error characteristics.

**However, critical caveats that may undermine CDAP:**
- **No paper I found reports actual per-position training loss curves.** The WorldVLA result is about *inference-time error propagation* in autoregressive generation, not about whether the *training loss* varies across positions. These are fundamentally different things. During training with teacher forcing, each position sees the ground-truth previous actions, so the autoregressive error compounding that happens at inference does not manifest in training loss.
- **FAST (Physical Intelligence, arXiv:2501.09747)** highlights a different problem: with naive binning tokenization, "low token prediction loss can often be achieved with mappings as trivial as simply copying the most recent action token." This suggests that per-position training loss may actually be *low and uniform* precisely because the model learns a trivial copying shortcut, not because prediction is genuinely easy. This is a significant concern for CDAP -- if loss is already low everywhere due to trivial solutions, re-weighting by loss won't help.
- **The ACT paper** uses exponential decay weighting at *inference time* (w(t) = exp(-t/temperature)), weighting recent chunk predictions more. But this is temporal ensembling of overlapping chunks at deployment, not a training loss weighting scheme.

**Bottom line:** The training loss may not vary as dramatically across positions as CDAP assumes, because teacher forcing masks the inference-time error compounding. The real problem (error propagation) manifests at deployment, not in the training loss.

### 2. Existing Analysis of Loss Distribution Within Action Chunks

**No published work directly analyzes how training losses distribute within action chunks.** I searched extensively and found:
- Papers analyze *inference* accuracy degradation (WorldVLA, Leave No Observation Behind)
- Papers analyze *deployment* smoothness via temporal ensembling (ACT)
- Papers analyze tokenization effects on loss (FAST)
- But **zero papers** report a simple "training loss by chunk position" plot

This is a gap in the literature that CDAP could fill -- but it also means there's no existing evidence confirming the assumption that training loss variation is large enough to exploit.

### 3. OpenVLA-OFT Fine-Tuning Compute Cost

Concrete numbers from multiple sources:
- **Original OpenVLA pretraining**: ~21,500 A100-hours (64 A100s x 14 days)
- **OpenVLA-OFT fine-tuning**: 8 A100/H100-80GB GPUs for 1-2 days = **192-384 GPU-hours** for 50K-150K gradient steps
- **LoRA fine-tuning**: 10-15 hours on a single A100 (for ~200 demonstrations)
- **Full fine-tuning**: 5-15 hours on 8 A100s = 40-120 GPU-hours

This is relevant for CDAP feasibility: if CDAP adds overhead to the loss computation or sampling, the baseline cost is 192-384 GPU-hours. Even a 2x overhead would be tolerable given modern compute budgets.

### 4. Sirius-Fleet Dataset Availability

**Yes, the datasets are publicly available.** The Sirius-Fleet GitHub repo (UT-Austin-RPL/sirius-fleet) provides:
- Simulation data (RoboCasa): available on HuggingFace at `huihanl/sirius-fleet-robocasa`
- Real robot data (MUTEX): available on HuggingFace at `huihanl/sirius-fleet-mutex`

Both are downloadable. The code is also open-source.

### 5. Evidence That PER-Style Methods Fail

**There is significant evidence of PER failure modes, which is directly relevant to CDAP:**

- **Pan et al. (UAI 2022, arXiv:2007.09569)** identify two core limitations: (1) outdated priorities and (2) insufficient coverage of the sample space. They prove that error-based prioritized sampling for MSE loss is mathematically equivalent to uniform sampling for cubic power loss.
- **Interplay of Prioritized Replay and Generalization (arXiv:2407.09702)**: In control tasks (MountainCar, Acrobot, CartPole), **none of the prioritized variants consistently outperform uniform replay**. Over-sampling high-priority transitions causes the network to "spend capacity minimizing error on those transitions at the cost of worse prediction in other states." The authors found that even basic Q-learning with uniform replay outperformed all three prioritized variants.
- **Supervised learning specifically**: One finding states "ER outperforms PrioritizedER in supervised learning tasks." Since VLA training is fundamentally supervised (behavior cloning), this is directly concerning for CDAP.
- The bias introduced by prioritization requires importance sampling correction, adding complexity and potential instability.

**This is arguably the strongest evidence against CDAP.** VLA fine-tuning is supervised learning, and PER-style methods have shown negative results specifically in supervised settings.

### 6. RoboMimic Multi-Human Benchmark Results

RoboMimic v0.5.0 was released June 2025, adding Diffusion Policy support, multi-dataset training, and language-conditioned policies. The benchmark includes:
- 5 tasks with proficient human (PH) datasets
- 4 tasks with mixed proficient/non-proficient human (MH) datasets
- Diffusion Policy is the current leading approach, with a reported "average improvement of 46.9%" over prior SOTA across 12 tasks/4 benchmarks

No specific 2025-2026 leaderboard numbers for multi-human were found in my search, but Diffusion Policy and its transformer variants remain the dominant approaches.

### 7. SimplerEnv Verification

**SimplerEnv is real and increasingly standard.** Key facts:
- Full name: SIMPLER (SIMulated Policies for Large-scale Evaluation of Robots)
- Provides simulated environments for Google Robot and WidowX manipulation
- Demonstrates **strong correlation with real-world performance** via low Mean Maximum Rank Violation (MMRV) scores and high Pearson correlation, validated on ~1,500 paired evaluation episodes
- Evaluated policies include RT-1, RT-1-X, RT-2-X, Octo variants
- Now integrated into broader evaluation frameworks alongside LIBERO, RoboTwin 2.0, RoboCasa-GR1, and BEHAVIOR-1K via the Allen AI VLA Evaluation Harness (`allenai/vla-evaluation-harness`)

It is a legitimate and increasingly adopted benchmark for VLA evaluation.

### 8. CAPS (Context-Aware Priority Sampling) Verification

**Confirmed: CAPS exists and was accepted to ICRA 2025 (arXiv:2503.01650).**

Critical detail: **CAPS operates at the whole-trajectory/sample level, NOT at the per-token or per-position level.** It uses:
1. A VQ-VAE to encode ego-vehicle trajectories + scene context into discrete cluster IDs
2. Inverse cluster frequency to re-weight how often *entire samples* appear during training (importance sampling)

CAPS is designed for autonomous driving, not robotics manipulation. It re-samples entire training examples (trajectory-level), not individual loss terms within a sequence. If CDAP cites CAPS as a predecessor, the distinction is important: CAPS does not do within-sequence priority weighting, which is what CDAP presumably proposes.

---

## Summary of Key Risks for CDAP

1. **Strongest risk**: The training loss may NOT vary meaningfully across chunk positions under teacher forcing. The error compounding that motivates CDAP occurs at inference time, not training time. No published work has confirmed that training-time per-position loss shows the variation CDAP assumes.

2. **PER methods fail in supervised learning**: Multiple papers show prioritized sampling underperforms uniform sampling in supervised settings. VLA fine-tuning is supervised learning.

3. **FAST's insight is damaging**: If action tokens are so correlated that models achieve low loss via trivial copying, then loss-based prioritization will assign similar (low) priorities everywhere -- defeating the purpose.

4. **CAPS is trajectory-level, not token-level**: If CDAP claims lineage from CAPS, the granularity difference is fundamental and needs justification.

5. **Compute feasibility is fine**: OpenVLA-OFT fine-tuning costs 192-384 GPU-hours, so moderate overhead from CDAP is acceptable.

6. **Sirius-Fleet data is available** and **SimplerEnv is a standard benchmark** -- these are not risks.

Sources:
- [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539)
- [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](https://arxiv.org/abs/2509.23224)
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)
- [Understanding and Mitigating the Limitations of Prioritized Experience Replay](https://arxiv.org/abs/2007.09569)
- [Investigating the Interplay of Prioritized Replay and Generalization](https://arxiv.org/html/2407.09702v2)
- [CAPS: Context-Aware Priority Sampling](https://arxiv.org/abs/2503.01650)
- [OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models](https://arxiv.org/html/2502.19645v1)
- [SimplerEnv: Evaluating Real-World Robot Manipulation Policies in Simulation](https://simpler-env.github.io/)
- [Sirius-Fleet GitHub Repository](https://github.com/UT-Austin-RPL/sirius-fleet)
- [Action Chunking for Robotics and AV](https://www.maximilianigl.com/blog/action-chunking)
- [Allen AI VLA Evaluation Harness](https://github.com/allenai/vla-evaluation-harness)
- [RoboMimic Framework](https://robomimic.github.io/)
- [Action Chunking and Exploratory Data Collection](https://arxiv.org/abs/2507.09061)
- [PD-VLA: Accelerating VLA with Parallel Decoding](https://arxiv.org/abs/2503.02310)

agentId: ae9e8b1ee50e20b7c (use SendMessage with to: 'ae9e8b1ee50e20b7c' to continue this agent)
&lt;usage>total_tokens: 37806
tool_uses: 34
duration_ms: 193330&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f3f513c-49dd-40cb-9d97-3bce017419a4",
  "isSidechain": false,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "type": "user",
  "uuid": "ae06bc9a-1e2f-436d-be4b-8e78dbe2e17e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML paper idea called \"CDAP\" for VLA training. I need to find evidence AGAINST its core assumptions and check feasibility. Search for:\n\n1. \"action chunk prediction loss uniform across positions\" — does loss actually vary meaningfully across chunk positions, or is it roughly uniform?\n2. \"VLA action chunking loss analysis\" — any existing analysis of how losses distribute within action chunks\n3. \"OpenVLA-OFT fine-tuning cost GPU hours\" — what's the actual compute cost for fine-tuning OpenVLA?\n4. \"Sirius-Fleet dataset availability\" — is this dataset publicly available?\n5. \"prioritized experience replay doesn't help\" OR \"prioritized replay negative results\" — any evidence PER-style methods fail\n6. \"RoboMimic multi-human benchmark results 2025 2026\" — what are current SOTA results?\n7. \"SimplerEnv VLA evaluation benchmark\" — verify this exists and is standard\n8. \"CAPS context-aware priority sampling ICRA 2025 arXiv:2503.01650\" — verify this exists and what it does (the idea cites it but doesn't discuss it much)\n\nReport findings in detail. I'm especially interested in whether there's evidence that per-position loss variation within action chunks is negligible (which would undermine the entire idea).",
    "agentId": "ae9e8b1ee50e20b7c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have sufficient evidence to compile a comprehensive report. Here is my detailed analysis:\n\n---\n\n## Detailed Findings: Evidence Against CDAP Core Assumptions\n\n### 1. Per-Position Loss Variation Within Action Chunks\n\n**This is the most critical question, and the evidence is nuanced -- it partially supports and partially undermines CDAP.**\n\n**Evidence that loss DOES vary across chunk positions (supports CDAP's premise):**\n- **WorldVLA (arXiv:2506.21539)** provides the strongest empirical evidence. They show grasping success rate drops 10-50% with naive autoregressive action chunking. Their ablation (Table 3): without chunking, average success rate is 62.8%; with naive chunking, it drops to 54.0%. Their fix (attention masking) recovers to 76.6%. This confirms that later positions in autoregressive chunks accumulate error.\n- The \"Leave No Observation Behind\" paper (arXiv:2509.23224) introduces a per-step correction module with positional sinusoidal embeddings encoding the index within the chunk, implicitly acknowledging that different positions have different error characteristics.\n\n**However, critical caveats that may undermine CDAP:**\n- **No paper I found reports actual per-position training loss curves.** The WorldVLA result is about *inference-time error propagation* in autoregressive generation, not about whether the *training loss* varies across positions. These are fundamentally different things. During training with teacher forcing, each position sees the ground-truth previous actions, so the autoregressive error compounding that happens at inference does not manifest in training loss.\n- **FAST (Physical Intelligence, arXiv:2501.09747)** highlights a different problem: with naive binning tokenization, \"low token prediction loss can often be achieved with mappings as trivial as simply copying the most recent action token.\" This suggests that per-position training loss may actually be *low and uniform* precisely because the model learns a trivial copying shortcut, not because prediction is genuinely easy. This is a significant concern for CDAP -- if loss is already low everywhere due to trivial solutions, re-weighting by loss won't help.\n- **The ACT paper** uses exponential decay weighting at *inference time* (w(t) = exp(-t/temperature)), weighting recent chunk predictions more. But this is temporal ensembling of overlapping chunks at deployment, not a training loss weighting scheme.\n\n**Bottom line:** The training loss may not vary as dramatically across positions as CDAP assumes, because teacher forcing masks the inference-time error compounding. The real problem (error propagation) manifests at deployment, not in the training loss.\n\n### 2. Existing Analysis of Loss Distribution Within Action Chunks\n\n**No published work directly analyzes how training losses distribute within action chunks.** I searched extensively and found:\n- Papers analyze *inference* accuracy degradation (WorldVLA, Leave No Observation Behind)\n- Papers analyze *deployment* smoothness via temporal ensembling (ACT)\n- Papers analyze tokenization effects on loss (FAST)\n- But **zero papers** report a simple \"training loss by chunk position\" plot\n\nThis is a gap in the literature that CDAP could fill -- but it also means there's no existing evidence confirming the assumption that training loss variation is large enough to exploit.\n\n### 3. OpenVLA-OFT Fine-Tuning Compute Cost\n\nConcrete numbers from multiple sources:\n- **Original OpenVLA pretraining**: ~21,500 A100-hours (64 A100s x 14 days)\n- **OpenVLA-OFT fine-tuning**: 8 A100/H100-80GB GPUs for 1-2 days = **192-384 GPU-hours** for 50K-150K gradient steps\n- **LoRA fine-tuning**: 10-15 hours on a single A100 (for ~200 demonstrations)\n- **Full fine-tuning**: 5-15 hours on 8 A100s = 40-120 GPU-hours\n\nThis is relevant for CDAP feasibility: if CDAP adds overhead to the loss computation or sampling, the baseline cost is 192-384 GPU-hours. Even a 2x overhead would be tolerable given modern compute budgets.\n\n### 4. Sirius-Fleet Dataset Availability\n\n**Yes, the datasets are publicly available.** The Sirius-Fleet GitHub repo (UT-Austin-RPL/sirius-fleet) provides:\n- Simulation data (RoboCasa): available on HuggingFace at `huihanl/sirius-fleet-robocasa`\n- Real robot data (MUTEX): available on HuggingFace at `huihanl/sirius-fleet-mutex`\n\nBoth are downloadable. The code is also open-source.\n\n### 5. Evidence That PER-Style Methods Fail\n\n**There is significant evidence of PER failure modes, which is directly relevant to CDAP:**\n\n- **Pan et al. (UAI 2022, arXiv:2007.09569)** identify two core limitations: (1) outdated priorities and (2) insufficient coverage of the sample space. They prove that error-based prioritized sampling for MSE loss is mathematically equivalent to uniform sampling for cubic power loss.\n- **Interplay of Prioritized Replay and Generalization (arXiv:2407.09702)**: In control tasks (MountainCar, Acrobot, CartPole), **none of the prioritized variants consistently outperform uniform replay**. Over-sampling high-priority transitions causes the network to \"spend capacity minimizing error on those transitions at the cost of worse prediction in other states.\" The authors found that even basic Q-learning with uniform replay outperformed all three prioritized variants.\n- **Supervised learning specifically**: One finding states \"ER outperforms PrioritizedER in supervised learning tasks.\" Since VLA training is fundamentally supervised (behavior cloning), this is directly concerning for CDAP.\n- The bias introduced by prioritization requires importance sampling correction, adding complexity and potential instability.\n\n**This is arguably the strongest evidence against CDAP.** VLA fine-tuning is supervised learning, and PER-style methods have shown negative results specifically in supervised settings.\n\n### 6. RoboMimic Multi-Human Benchmark Results\n\nRoboMimic v0.5.0 was released June 2025, adding Diffusion Policy support, multi-dataset training, and language-conditioned policies. The benchmark includes:\n- 5 tasks with proficient human (PH) datasets\n- 4 tasks with mixed proficient/non-proficient human (MH) datasets\n- Diffusion Policy is the current leading approach, with a reported \"average improvement of 46.9%\" over prior SOTA across 12 tasks/4 benchmarks\n\nNo specific 2025-2026 leaderboard numbers for multi-human were found in my search, but Diffusion Policy and its transformer variants remain the dominant approaches.\n\n### 7. SimplerEnv Verification\n\n**SimplerEnv is real and increasingly standard.** Key facts:\n- Full name: SIMPLER (SIMulated Policies for Large-scale Evaluation of Robots)\n- Provides simulated environments for Google Robot and WidowX manipulation\n- Demonstrates **strong correlation with real-world performance** via low Mean Maximum Rank Violation (MMRV) scores and high Pearson correlation, validated on ~1,500 paired evaluation episodes\n- Evaluated policies include RT-1, RT-1-X, RT-2-X, Octo variants\n- Now integrated into broader evaluation frameworks alongside LIBERO, RoboTwin 2.0, RoboCasa-GR1, and BEHAVIOR-1K via the Allen AI VLA Evaluation Harness (`allenai/vla-evaluation-harness`)\n\nIt is a legitimate and increasingly adopted benchmark for VLA evaluation.\n\n### 8. CAPS (Context-Aware Priority Sampling) Verification\n\n**Confirmed: CAPS exists and was accepted to ICRA 2025 (arXiv:2503.01650).**\n\nCritical detail: **CAPS operates at the whole-trajectory/sample level, NOT at the per-token or per-position level.** It uses:\n1. A VQ-VAE to encode ego-vehicle trajectories + scene context into discrete cluster IDs\n2. Inverse cluster frequency to re-weight how often *entire samples* appear during training (importance sampling)\n\nCAPS is designed for autonomous driving, not robotics manipulation. It re-samples entire training examples (trajectory-level), not individual loss terms within a sequence. If CDAP cites CAPS as a predecessor, the distinction is important: CAPS does not do within-sequence priority weighting, which is what CDAP presumably proposes.\n\n---\n\n## Summary of Key Risks for CDAP\n\n1. **Strongest risk**: The training loss may NOT vary meaningfully across chunk positions under teacher forcing. The error compounding that motivates CDAP occurs at inference time, not training time. No published work has confirmed that training-time per-position loss shows the variation CDAP assumes.\n\n2. **PER methods fail in supervised learning**: Multiple papers show prioritized sampling underperforms uniform sampling in supervised settings. VLA fine-tuning is supervised learning.\n\n3. **FAST's insight is damaging**: If action tokens are so correlated that models achieve low loss via trivial copying, then loss-based prioritization will assign similar (low) priorities everywhere -- defeating the purpose.\n\n4. **CAPS is trajectory-level, not token-level**: If CDAP claims lineage from CAPS, the granularity difference is fundamental and needs justification.\n\n5. **Compute feasibility is fine**: OpenVLA-OFT fine-tuning costs 192-384 GPU-hours, so moderate overhead from CDAP is acceptable.\n\n6. **Sirius-Fleet data is available** and **SimplerEnv is a standard benchmark** -- these are not risks.\n\nSources:\n- [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539)\n- [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](https://arxiv.org/abs/2509.23224)\n- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)\n- [Understanding and Mitigating the Limitations of Prioritized Experience Replay](https://arxiv.org/abs/2007.09569)\n- [Investigating the Interplay of Prioritized Replay and Generalization](https://arxiv.org/html/2407.09702v2)\n- [CAPS: Context-Aware Priority Sampling](https://arxiv.org/abs/2503.01650)\n- [OpenVLA-OFT: Fine-Tuning Vision-Language-Action Models](https://arxiv.org/html/2502.19645v1)\n- [SimplerEnv: Evaluating Real-World Robot Manipulation Policies in Simulation](https://simpler-env.github.io/)\n- [Sirius-Fleet GitHub Repository](https://github.com/UT-Austin-RPL/sirius-fleet)\n- [Action Chunking for Robotics and AV](https://www.maximilianigl.com/blog/action-chunking)\n- [Allen AI VLA Evaluation Harness](https://github.com/allenai/vla-evaluation-harness)\n- [RoboMimic Framework](https://robomimic.github.io/)\n- [Action Chunking and Exploratory Data Collection](https://arxiv.org/abs/2507.09061)\n- [PD-VLA: Accelerating VLA with Parallel Decoding](https://arxiv.org/abs/2503.02310)"
      }
    ],
    "totalDurationMs": 193330,
    "totalTokens": 37806,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 34177,
      "output_tokens": 2763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 865
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2763,
          "cache_read_input_tokens": 34177,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 865,
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
      "otherToolCount": 34
    }
  },
  "sourceToolAssistantUUID": "9f3f513c-49dd-40cb-9d97-3bce017419a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T17:43:27.693Z_

<details><summary>↩ Tool result · `toolu_017vpQbVwTDHQHUbeh8HLm81`</summary>

```text
Here is my comprehensive analysis of the novelty claim for "CDAP" -- the idea of decomposing per-position losses within action chunks as a priority signal during VLA training.

---

## Summary of Findings

### The Core Novelty Claim

CDAP proposes using the **intra-chunk temporal loss profile** (i.e., how prediction loss varies across positions within an action chunk) as a **priority signal for training** (e.g., data curriculum, sample weighting, etc.). The question is whether any prior work already does this.

### Most Threatening Prior Work

**1. DAM-VLA (arXiv:2603.00926, March 2026)** -- This is the closest competitor and partially overlaps.

DAM-VLA introduces a **dual-scale action weighting mechanism** that operates at both trajectory-level and action-chunk-level. The chunk-level component applies **exponential decay** within each predicted chunk to **prioritize immediate temporal accuracy** during training supervision. This means DAM-VLA **does** decompose the training loss at a per-position level within chunks and applies position-dependent weights. However, the key distinction is:

- DAM-VLA uses a **fixed, predetermined exponential decay** scheme. The weighting is a design choice (a prior), not derived from observed loss profiles.
- CDAP (as described) proposes **observing the actual per-position loss profile** and using that empirical signal to drive training priorities -- a data-driven approach rather than a fixed heuristic.

This is a meaningful but **narrow** distinction. A reviewer could argue DAM-VLA's exponential decay is an instance of intra-chunk loss weighting, even if not data-driven.

**2. VLA Knows Its Limits / AutoHorizon (arXiv:2602.21445, February 2026)** -- This paper provides strong **analysis** of temporal prediction quality degradation within chunks, identifying "radial action sinks" (attention concentrates on initial and terminal tokens, with rapid decay in between). It proposes **AutoHorizon**, which dynamically adjusts the execution horizon at **inference time** based on attention-weight confidence signals. Crucially:

- This paper **does not** decompose per-position losses during **training** -- it operates at inference time only.
- However, it does establish and characterize the very phenomenon (intra-chunk temporal quality degradation) that CDAP claims to exploit. If CDAP cites this as motivation, that is fine, but the analysis of the phenomenon itself is not novel.

**3. Mixture of Horizons / MoH (arXiv:2511.19433, November 2025)** -- MoH rearranges action chunks into segments with different horizons and processes them with a shared transformer. It includes a **balance loss** to prevent the gating mechanism from biasing toward longer horizons. This is about multi-horizon fusion rather than per-position loss decomposition, so it is less directly competing, but it does address the symptom (later positions in chunks are less accurate) from a structural angle.

**4. ACT / Action Chunking with Transformers (Zhao et al., 2023)** -- The foundational work uses L1 reconstruction loss across the entire chunk uniformly. It does **not** decompose or weight per-position losses differently. Standard practice in the field is uniform loss across chunk positions.

**5. Leave No Observation Behind / A2C2 (arXiv:2509.23224)** -- Addresses chunk degradation via a lightweight correction head at inference time. Does not modify training loss decomposition.

**6. Chain-of-Action (arXiv:2506.09990)** -- Uses MTP (multi-token prediction) regularization and masks out predictions beyond trajectory horizon, but does not weight per-position losses within chunks differently.

### Papers That Do NOT Threaten the Claim

- **LangForce/BayesianVLA** -- Bayesian decomposition of the VLA architecture, not the action chunk loss.
- **OpenVLA-OFT** -- Uses L1 regression for continuous actions with action chunking but uniform loss.
- **pi0** -- Flow matching on parallel action tokens, no per-position loss differentiation reported.
- **VLA-RL, ConRFT, etc.** -- RL-based fine-tuning methods that don't address intra-chunk loss structure.

---

## Verdict on Novelty

The novelty claim **partially holds but needs careful positioning**:

1. **DAM-VLA is a direct threat.** It applies position-dependent weighting (exponential decay) within action chunks during training. CDAP must clearly differentiate itself by emphasizing that it uses the **empirical loss profile** as a signal (data-driven) rather than a fixed decay prior. If CDAP does not use the loss profile in a data-driven way and instead just proposes fixed weighting, the novelty over DAM-VLA becomes very thin.

2. **The phenomenon is not novel.** "VLA Knows Its Limits" already characterizes the temporal quality degradation within chunks. CDAP cannot claim discovery of the phenomenon, only a novel exploitation of it for training.

3. **Using loss decomposition as a training priority signal** (e.g., for curriculum learning or sample weighting) appears to be genuinely novel if it means: "compute per-position losses, observe which positions/samples have unusual loss profiles, and use that to prioritize which training examples get more weight or are revisited." No paper I found does exactly this.

4. **The claim that "no prior work exploits the intra-chunk temporal loss profile as a priority signal"** is **too strong** given DAM-VLA. A more defensible claim would be: "no prior work uses the *observed/empirical* intra-chunk loss profile as a *data-driven* priority signal for training sample selection or curriculum design."

---

Sources:
- [DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework](https://arxiv.org/html/2603.00926)
- [DAM-VLA (Samsung Research Blog)](https://research.samsung.com/blog/DAM-VLA-A-Dynamic-Action-Model-Based-Vision-Language-Action-Framework-for-Robot-Manipulation)
- [VLA Knows Its Limits (arXiv:2602.21445)](https://arxiv.org/html/2602.21445)
- [Mixture of Horizons in Action Chunking (arXiv:2511.19433)](https://arxiv.org/html/2511.19433v1)
- [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](https://arxiv.org/html/2509.23224v1)
- [VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning](https://arxiv.org/html/2509.25718)
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/html/2502.19645v2)
- [Chain-of-Action: Trajectory Autoregressive Modeling](https://arxiv.org/html/2506.09990v1)
- [LangForce: Bayesian Decomposition of VLA Models](https://arxiv.org/html/2601.15197)
- [ACT Policy Explained](https://www.roboticscenter.ai/blog/act-policy-explained)
- [Reinforcement Learning with Action Chunking](https://arxiv.org/html/2507.07969v1)
- [Real-Time Robot Execution with Masked Action Chunking](https://arxiv.org/html/2601.20130)
- [pi0: A Vision-Language-Action Flow Model](https://www.pi.website/download/pi0.pdf)

agentId: ac55b26a2269eeafd (use SendMessage with to: 'ac55b26a2269eeafd' to continue this agent)
&lt;usage>total_tokens: 26871
tool_uses: 17
duration_ms: 219448&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb918ca3-293d-4cae-8a83-5c898a5742d9",
  "isSidechain": false,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "type": "user",
  "uuid": "b908a1e4-587e-4ea2-8ea1-dcd89e42c33d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML paper idea called \"CDAP\" that proposes decomposing per-position losses within action chunks during VLA (Vision-Language-Action) model training. The key claim is that no prior work exploits the *intra-chunk temporal loss profile* as a priority signal for VLA training.\n\nSearch for competing/related work that might invalidate this novelty claim. Use WebSearch for each of these queries:\n\n1. \"action chunk loss decomposition VLA training 2025 2026\" \n2. \"per-position loss action chunking robot learning\"\n3. \"temporal loss profile robot imitation learning\"\n4. \"action chunk prediction quality degradation VLA\"\n5. \"sub-chunk loss analysis robot manipulation\"\n6. \"intra-chunk loss weighting VLA fine-tuning\"\n7. Search for \"DAM-VLA dual action model\" to verify what exactly DAM-VLA does with chunk-level weighting\n8. Search for \"VLA Knows Its Limits action sinks arXiv:2602.21445\" to verify the claim about temporal prediction quality degradation within chunks\n\nFor each search, report what you find — especially any paper that decomposes action chunk losses at a per-position level during training (not inference). I need to know if the novelty claim holds up.",
    "agentId": "ac55b26a2269eeafd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive analysis of the novelty claim for \"CDAP\" -- the idea of decomposing per-position losses within action chunks as a priority signal during VLA training.\n\n---\n\n## Summary of Findings\n\n### The Core Novelty Claim\n\nCDAP proposes using the **intra-chunk temporal loss profile** (i.e., how prediction loss varies across positions within an action chunk) as a **priority signal for training** (e.g., data curriculum, sample weighting, etc.). The question is whether any prior work already does this.\n\n### Most Threatening Prior Work\n\n**1. DAM-VLA (arXiv:2603.00926, March 2026)** -- This is the closest competitor and partially overlaps.\n\nDAM-VLA introduces a **dual-scale action weighting mechanism** that operates at both trajectory-level and action-chunk-level. The chunk-level component applies **exponential decay** within each predicted chunk to **prioritize immediate temporal accuracy** during training supervision. This means DAM-VLA **does** decompose the training loss at a per-position level within chunks and applies position-dependent weights. However, the key distinction is:\n\n- DAM-VLA uses a **fixed, predetermined exponential decay** scheme. The weighting is a design choice (a prior), not derived from observed loss profiles.\n- CDAP (as described) proposes **observing the actual per-position loss profile** and using that empirical signal to drive training priorities -- a data-driven approach rather than a fixed heuristic.\n\nThis is a meaningful but **narrow** distinction. A reviewer could argue DAM-VLA's exponential decay is an instance of intra-chunk loss weighting, even if not data-driven.\n\n**2. VLA Knows Its Limits / AutoHorizon (arXiv:2602.21445, February 2026)** -- This paper provides strong **analysis** of temporal prediction quality degradation within chunks, identifying \"radial action sinks\" (attention concentrates on initial and terminal tokens, with rapid decay in between). It proposes **AutoHorizon**, which dynamically adjusts the execution horizon at **inference time** based on attention-weight confidence signals. Crucially:\n\n- This paper **does not** decompose per-position losses during **training** -- it operates at inference time only.\n- However, it does establish and characterize the very phenomenon (intra-chunk temporal quality degradation) that CDAP claims to exploit. If CDAP cites this as motivation, that is fine, but the analysis of the phenomenon itself is not novel.\n\n**3. Mixture of Horizons / MoH (arXiv:2511.19433, November 2025)** -- MoH rearranges action chunks into segments with different horizons and processes them with a shared transformer. It includes a **balance loss** to prevent the gating mechanism from biasing toward longer horizons. This is about multi-horizon fusion rather than per-position loss decomposition, so it is less directly competing, but it does address the symptom (later positions in chunks are less accurate) from a structural angle.\n\n**4. ACT / Action Chunking with Transformers (Zhao et al., 2023)** -- The foundational work uses L1 reconstruction loss across the entire chunk uniformly. It does **not** decompose or weight per-position losses differently. Standard practice in the field is uniform loss across chunk positions.\n\n**5. Leave No Observation Behind / A2C2 (arXiv:2509.23224)** -- Addresses chunk degradation via a lightweight correction head at inference time. Does not modify training loss decomposition.\n\n**6. Chain-of-Action (arXiv:2506.09990)** -- Uses MTP (multi-token prediction) regularization and masks out predictions beyond trajectory horizon, but does not weight per-position losses within chunks differently.\n\n### Papers That Do NOT Threaten the Claim\n\n- **LangForce/BayesianVLA** -- Bayesian decomposition of the VLA architecture, not the action chunk loss.\n- **OpenVLA-OFT** -- Uses L1 regression for continuous actions with action chunking but uniform loss.\n- **pi0** -- Flow matching on parallel action tokens, no per-position loss differentiation reported.\n- **VLA-RL, ConRFT, etc.** -- RL-based fine-tuning methods that don't address intra-chunk loss structure.\n\n---\n\n## Verdict on Novelty\n\nThe novelty claim **partially holds but needs careful positioning**:\n\n1. **DAM-VLA is a direct threat.** It applies position-dependent weighting (exponential decay) within action chunks during training. CDAP must clearly differentiate itself by emphasizing that it uses the **empirical loss profile** as a signal (data-driven) rather than a fixed decay prior. If CDAP does not use the loss profile in a data-driven way and instead just proposes fixed weighting, the novelty over DAM-VLA becomes very thin.\n\n2. **The phenomenon is not novel.** \"VLA Knows Its Limits\" already characterizes the temporal quality degradation within chunks. CDAP cannot claim discovery of the phenomenon, only a novel exploitation of it for training.\n\n3. **Using loss decomposition as a training priority signal** (e.g., for curriculum learning or sample weighting) appears to be genuinely novel if it means: \"compute per-position losses, observe which positions/samples have unusual loss profiles, and use that to prioritize which training examples get more weight or are revisited.\" No paper I found does exactly this.\n\n4. **The claim that \"no prior work exploits the intra-chunk temporal loss profile as a priority signal\"** is **too strong** given DAM-VLA. A more defensible claim would be: \"no prior work uses the *observed/empirical* intra-chunk loss profile as a *data-driven* priority signal for training sample selection or curriculum design.\"\n\n---\n\nSources:\n- [DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework](https://arxiv.org/html/2603.00926)\n- [DAM-VLA (Samsung Research Blog)](https://research.samsung.com/blog/DAM-VLA-A-Dynamic-Action-Model-Based-Vision-Language-Action-Framework-for-Robot-Manipulation)\n- [VLA Knows Its Limits (arXiv:2602.21445)](https://arxiv.org/html/2602.21445)\n- [Mixture of Horizons in Action Chunking (arXiv:2511.19433)](https://arxiv.org/html/2511.19433v1)\n- [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](https://arxiv.org/html/2509.23224v1)\n- [VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning](https://arxiv.org/html/2509.25718)\n- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/html/2502.19645v2)\n- [Chain-of-Action: Trajectory Autoregressive Modeling](https://arxiv.org/html/2506.09990v1)\n- [LangForce: Bayesian Decomposition of VLA Models](https://arxiv.org/html/2601.15197)\n- [ACT Policy Explained](https://www.roboticscenter.ai/blog/act-policy-explained)\n- [Reinforcement Learning with Action Chunking](https://arxiv.org/html/2507.07969v1)\n- [Real-Time Robot Execution with Masked Action Chunking](https://arxiv.org/html/2601.20130)\n- [pi0: A Vision-Language-Action Flow Model](https://www.pi.website/download/pi0.pdf)"
      }
    ],
    "totalDurationMs": 219448,
    "totalTokens": 26871,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 24090,
      "output_tokens": 1830,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1830,
          "cache_read_input_tokens": 24090,
          "cache_creation_input_tokens": 950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 950,
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
  "sourceToolAssistantUUID": "fb918ca3-293d-4cae-8a83-5c898a5742d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b908a1e4-587e-4ea2-8ea1-dcd89e42c33d",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDAP novelty against AdaMix and temporal decomposition claims",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Assistant

_source line 22 · 2026-05-13T17:44:51.519Z_

<details><summary>Logged reasoning block</summary>

```text
This is excellent research. Let me now synthesize all findings and form my independent judgment.

## Key Findings Summary

### 1. EMMA/AdaMix Verification
- **Confirmed**: AdaMix aggregates MSE over action chunks into a scalar, does NOT decompose per-position losses
- Was submitted to ICLR 2026 but **withdrawn**
- The idea correctly identifies this as the closest competitor and correctly differentiates

### 2. CoRL 2026 Deadlines
- Abstract: May 26, 2026 11:59 UTC ✓ (idea says May 26)


- Paper: May 28 EOD / May 29 11:59 UTC ✓ (idea correctly notes both)
- Venue: Austin, Nov 9-12 ✓

### 3. RINSE Venue
- **ICML 2025 Workshop** (DataWorld), NOT main conference. The idea cites "ICML 2025" which is technically misleading.

### 4. DAM-VLA
- Uses fixed exponential decay weighting within chunks - but this is a FIXED scheme, not data-driven
- CDAP's key differentiation: uses *empirical* loss profile, not fixed decay

### 5. Remaining Claims
Now I'm checking the final set of claims about other methods and their technical approaches.

The core issue I'm seeing is that CDAP assumes per-position training loss varies meaningfully across chunk positions, but under teacher forcing during training, this variation may not actually occur—the error compounding that motivates the approach happens at inference time, not during supervised training. I haven't found published evidence that training-time per-position loss shows the kind of meaningful variation CDAP relies on.

Priority-based experience replay also underperforms uniform sampling in supervised settings, and VLA fine-tuning is essentially behavior cloning. Token Cleaning appears as a poster at ICML 2025, not a spotlight presentation as mentioned.

There are several related works I should account for: papers on supervised fine-tuning with token priority, entropy-based dynamic loss modulation at the token level, and adaptive reweighting approaches for VLAs. SCIZOR, CUPID, and DataMIL are all confirmed at their stated venues.

Looking at novelty, the core contribution—decomposing action chunk losses per-position and using that temporal profile as a priority signal—is genuinely novel and distinct from prior work like AdaMix, which uses scalar aggregated MSE, and DAM-VLA, which applies fixed exponential decay rather than learning the weighting pattern.

That said, the framework itself combines established techniques: prioritized experience replay, importance sampling correction, freshness decay, and loss-based prioritization. The VLA-specific addition is the temporal divergence metric, and the contact-phase weighting borrows inspiration from DAM-VLA's asymmetric Gaussian. So novelty lands around 3.5—the specific signal is novel but the overall approach is engineering-focused.

On feasibility, there's a critical untested assumption: whether training loss actually varies meaningfully across chunk positions under teacher forcing. Since each position receives ground-truth context during training, error compounding doesn't occur the way it would at inference, which could flatten the temporal loss profile significantly. The pilot study on RoboMimic-MH is the right priority, but this experiment is essentially make-or-break for the whole approach.

Implementation-wise, the work is straightforward to execute with low compute overhead and available datasets, though the timeline is tight for CoRL 2026. That pushes feasibility to around 3.5—doable technically, but the core hypothesis is the real risk. The writing is clear and well-structured with a comprehensive landscape section and explicit differentiation from AdaMix, so clarity scores a 4. Impact is more modest at 3: if the temporal divergence signal works, it could be useful for VLA training, but the gains might be marginal over AdaMix, and as a training trick rather than a fundamental advance, its scope is limited to robotics-specific applications.

Averaging these scores gives 3.5, which falls short of the 4.0 threshold. The critical problem is that the entire approach hinges on an untested assumption—whether the temporal loss profile actually varies meaningfully across chunk positions under teacher forcing. Beyond that, there are several other concerns: priority experience replay has shown mixed results in supervised settings, some cited venues appear to be workshops or posters rather than main conference papers, and there are gaps in the related work section covering recent papers on token prioritization and preference optimization methods.

The verdict leans toward revision. The concept has evolved substantially over multiple rounds, but I need to directly confront the teacher-forcing assumption. Most VLA implementations with action chunking predict the entire action sequence simultaneously from a single observation rather than autoregressively within the chunk, which changes how I should think about whether loss variation across positions would actually emerge during training.

Since the model must predict all K actions from the same observation o_t, later positions naturally become harder to predict as they correspond to increasingly distant future states. This temporal distance effect should create the loss gradient I'm proposing, independent of autoregressive error compounding. But I need to verify this holds across different architectures—OpenVLA uses L1 regression, pi0 uses flow matching, and some use diffusion—so the mechanism might vary by implementation.

The real insight is that temporal divergence δ would only be informative if different chunks show *different* loss profiles. If every chunk exhibits monotonically increasing loss with position, then δ becomes a constant signal across the dataset and loses discriminative power. The value comes from chunks that diverge more than others—like contact transitions versus free-space motions—which would show higher variance in their loss curves.

Reconsidering my assessment: novelty is around 3.5 since the temporal divergence signal itself is original, though the overall framework combines existing techniques like contact-phase weighting from DAM-VLA. Feasibility is also 3.5—the implementation is straightforward and the core assumption about parallel chunk prediction avoiding teacher forcing issues is more sound than I initially thought, but the pilot study remains critical and the timeline is tight. The writing is clear and comprehensive at a 4, though it cuts off mid-sentence.

For impact, I'm settling on 3 since the potential gains could be marginal and the approach is VLA-specific, which narrows scope though it's appropriate for CoRL. That puts the average at 3.5, still below the 4.0 threshold.

Looking back at the previous feedback, the idea has addressed all the Round 3 issues—EMMA and AdaMix are now included as related work and baselines, theoretical claims have been reframed as hypotheses, Token Cleaning and VGAS are acknowledged, the venue deadline is corrected, and the α_δ ablation is designed with a pilot study. The main remaining concerns are whether the teacher-forcing and parallel prediction issue gets explicit treatment, and there's something else that got cut off.

Actually, I need to correct a couple of venue citations in the paper. Token Cleaning is listed as an ICML Spotlight, but it should be marked as a Poster instead. And RINSE should be clarified as an ICML Workshop under DataWorld, not just the main conference. There's also some missing related work to address.

The idea has genuinely matured—the core insight is novel and the landscape is comprehensive with solid experimental design—but I'm still weighing whether these remaining issues push it toward a revision or if it's ready to move forward.

The average score sits at 3.5, which is below the 4.0 threshold. The untested core assumption about temporal divergence is a real risk, and there are those citation errors to fix. But looking at impact specifically for CoRL: this is the premier venue for robot learning, VLA training efficiency is a hot topic right now, and even if CDAP's gains are modest, the empirical analysis of temporal loss profiles would be valuable on its own. That might justify bumping impact to 3.5, which would bring the overall average to around 3.625—still below threshold, but closer.

For novelty, the specific combination of ideas and the temporal divergence signal feels like a solid 3.5. It's clever, though not groundbreaking. I think I should go with a revise recommendation and give specific, actionable feedback.

The real empirical questions here are whether the δ signal adds much beyond μ, whether PER actually helps in supervised settings, and whether the temporal loss variation will be as pronounced as expected. The pilot study should answer these. I also notice the paper explicitly addresses the numerical instability issue with policy ratios in high-dimensional continuous spaces—that's a valid differentiation from iw-SFT. I should verify there's no concurrent work I'm missing on this adaptive approach. The temporal divergence signal is genuinely novel for VLA training and meaningfully different from AdaMix, though the framework itself combines established techniques like PER, importance sampling, and age decay—with contact-phase weighting directly borrowed from DAM-VLA. Implementation is straightforward with available datasets, but the key risk is whether per-position training loss varies enough under parallel chunk prediction to make the signal useful, which the pilot study addresses. The work is exceptionally well-presented with a comprehensive landscape and clean formulation, but the contribution feels incremental—a useful training-time tool rather than a fundamental advance, though the first systematic analysis of temporal loss profiles does have independent value.

The score comes in below the 4.0 threshold, and there are several concerns I need to address: the gap between teacher-forcing during training and parallel prediction at inference, PER's known failures in supervised learning settings, some venue citations that need fixing, and a few missing related works. The pilot study becomes absolutely critical for validating whether the temporal divergence signal actually captures meaningful variation in loss across positions, and I should explicitly argue why CDAP's VLA-specific signal overcomes the typical PER failure modes in supervised learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b908a1e4-587e-4ea2-8ea1-dcd89e42c33d",
  "isSidechain": false,
  "requestId": "req_011CazyvZeGkSdWhXDViZ2ki",
  "type": "assistant",
  "uuid": "0712724b-5eed-4eb4-8401-15fcfbfda363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY8m2b9beLkZsta1PgbXny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6138,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 35665,
      "output_tokens": 4062,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6138,
          "output_tokens": 4062,
          "cache_read_input_tokens": 35665,
          "cache_creation_input_tokens": 3122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3122
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

_source line 23 · 2026-05-13T17:44:51.521Z_

Now let me do one more focused search on the critical assumption — whether per-position training loss actually varies within action chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0712724b-5eed-4eb4-8401-15fcfbfda363",
  "isSidechain": false,
  "requestId": "req_011CazyvZeGkSdWhXDViZ2ki",
  "type": "assistant",
  "uuid": "733a6c19-f05e-4947-8acb-a141f9049a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY8m2b9beLkZsta1PgbXny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6138,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 35665,
      "output_tokens": 4062,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6138,
          "output_tokens": 4062,
          "cache_read_input_tokens": 35665,
          "cache_creation_input_tokens": 3122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3122
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

_source line 24 · 2026-05-13T17:44:59.153Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TmfS6eGAeMDSvhUKRGuTkt`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for chunk prediction training loss variation evidence",
  "prompt": "This is a critical question for an ML paper review. I need to understand how VLA models with action chunking predict their action chunks, because it determines whether per-position training loss varies across chunk positions.\n\nSearch for:\n\n1. \"OpenVLA-OFT action chunking implementation\" — How does OpenVLA-OFT predict action chunks? Is it autoregressive within the chunk (each action conditions on previous), or does it predict all K actions in parallel from the observation?\n\n2. \"action chunking teacher forcing VLA training\" — Is there teacher forcing within action chunks during VLA training?\n\n3. \"pi0 action prediction mechanism\" — How does pi0 predict action chunks (flow matching, parallel)?\n\n4. \"ACT action chunking transformer prediction mechanism\" — The original ACT paper — does it predict chunks in parallel via CVAE or autoregressively?\n\n5. \"action chunk loss per position training\" — Any evidence of per-position loss variation during training\n\n6. \"prioritized experience replay supervised learning failure\" OR \"PER doesn't work supervised learning\" — Evidence that PER-style methods fail in supervised settings\n\nThe key question: In standard VLA action-chunked training (e.g., OpenVLA-OFT), does the model predict all K actions from a single observation (making later positions harder because they're temporally distant from the observation), or does it use teacher forcing within the chunk (making all positions approximately equally difficult)?\n\nThis distinction is critical because the paper under review assumes per-position loss varies significantly within chunks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "733a6c19-f05e-4947-8acb-a141f9049a20",
  "isSidechain": false,
  "requestId": "req_011CazyvZeGkSdWhXDViZ2ki",
  "type": "assistant",
  "uuid": "d63a3798-4c1b-43fa-a23c-a875f6eb2d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY8m2b9beLkZsta1PgbXny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6138,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 35665,
      "output_tokens": 4062,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6138,
          "output_tokens": 4062,
          "cache_read_input_tokens": 35665,
          "cache_creation_input_tokens": 3122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3122
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d63a3798-4c1b-43fa-a23c-a875f6eb2d47",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDAP novelty against AdaMix and temporal decomposition claims",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Tool result

_source line 27 · 2026-05-13T17:49:31.495Z_

<details><summary>↩ Tool result · `toolu_01TmfS6eGAeMDSvhUKRGuTkt`</summary>

```text
Now I have comprehensive information to provide a thorough answer. Let me compile the findings.

---

Here is a detailed synthesis of my findings across all six topics:

## 1. OpenVLA-OFT: Parallel Prediction, NOT Autoregressive Within Chunks

OpenVLA-OFT predicts **all K actions in parallel from the observation in a single forward pass**. It does NOT use autoregressive decoding within the action chunk. The key architectural changes from the original OpenVLA:

- **Empty action embeddings** replace teacher-forced ground-truth inputs. These embeddings differ only in positional encoding values -- they carry no information about the ground-truth actions.
- **Bidirectional attention mask** replaces the causal attention mask, so each action position can attend to all other positions and all observation tokens simultaneously.
- An **MLP action head** maps decoder hidden states to continuous action values, trained with **mean L1 loss** between predicted and ground-truth actions.

This is a critical distinction: **there is no teacher forcing within the action chunk during training**. Each action position must predict its value solely from the observation tokens (image, language, robot state) and the positional encoding indicating which timestep it corresponds to. The model cannot "cheat" by looking at ground-truth actions at earlier positions within the chunk.

The original base OpenVLA (without OFT) **did** use autoregressive teacher forcing -- ground-truth action tokens shifted right by one position with causal masking, standard next-token prediction with cross-entropy loss. But OpenVLA-OFT fundamentally changed this to parallel decoding.

Paper: "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" (arXiv:2502.19645)

## 2. Teacher Forcing Within Chunks: Generally NO for Modern VLA Models

For models using **parallel decoding** (OpenVLA-OFT), **flow matching** (pi0), **diffusion** (Diffusion Policy), or **CVAE** (ACT), there is **no teacher forcing within the action chunk**. All positions are predicted simultaneously from the observation:

- **OpenVLA-OFT**: Empty action embeddings + bidirectional attention; no ground-truth actions provided during training's forward pass through the action head.
- **pi0**: Flow matching denoises the entire chunk simultaneously; the model predicts a vector field for all H=50 action positions at once.
- **Diffusion Policy**: Denoises all 16-32 action positions in parallel, conditioned on the observation.
- **ACT**: Decoder uses learnable positional queries (not ground-truth actions) + cross-attention to observation tokens; explicitly noted that "no ground truth information is passed into the decoder" so there is "no need for causal masking."

The only VLA paradigm that uses teacher forcing within a chunk is the **original autoregressive token-prediction** approach (e.g., base OpenVLA, RT-2), where each action token is predicted conditioned on previous ground-truth tokens during training. But these models typically predict a single timestep's action (e.g., 7 tokens for one action), not a multi-step chunk.

## 3. pi0: Flow Matching, All Positions Simultaneously

pi0 uses **conditional flow matching** to predict action chunks of H=50 timesteps in parallel:

- During training, given observation o_t, the model learns to denoise a noisy action chunk A_t^tau back to the clean chunk A_t, where tau controls noise level. The training loss is MSE between the predicted vector field and the true denoising direction.
- The **action expert** uses **full bidirectional attention** across action tokens, meaning all 50 positions are processed together, not sequentially.
- At inference, the model performs ~10 iterative denoising steps (each processing all 50 positions simultaneously), which is faster than 50 autoregressive steps.
- The noise schedule uses a shifted beta distribution emphasizing lower timesteps (noisier actions), but this is about the *denoising* timestep tau, not about position within the chunk.

Paper: "pi0: A Vision-Language-Action Flow Model for General Robot Control" (arXiv:2410.24164)

## 4. ACT: CVAE, Parallel Prediction via Learnable Queries

ACT predicts entire action chunks in a **single forward pass** using a **non-autoregressive** design:

- The decoder takes **k learnable positional queries** (one per action in the chunk), the latent z from the CVAE, and observation tokens.
- Critically: "No ground truth information is passed into the decoder (just the learnable query embeddings) and thus no need for causal masking! For the generation of each action, the decoder can consider both the earlier and subsequent actions it is predicting."
- This is inspired by DETR (object detection), which similarly uses a set of queries to predict outputs in parallel.
- Training loss: L1 reconstruction loss + KL-divergence regularization (CVAE objective).

The CVAE is a training aid to handle multimodality in demonstrations -- without it, the model averages across demonstration styles. But the prediction mechanism is fundamentally parallel.

Paper: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" (Tony Zhao et al.)

## 5. Per-Position Loss Variation: Indirect Evidence That Later Positions ARE Harder

While I did not find papers that explicitly plot per-position training loss curves across chunk positions, there is strong indirect evidence that **later positions within a chunk are harder to predict**, and multiple papers build on this assumption:

**"Leave No Observation Behind" (A2C2)**: Introduces a correction module that explicitly encodes "the index of the base action within the chunk" as a positional feature, implying that different positions need different corrections. The paper shows +23% improvement on dynamic tasks.

**"Bidirectional Decoding"**: Documents that "recent states are often more important to decision making" and that prediction quality degrades for later positions because the initial observation becomes "outdated" -- errors compound in open-loop execution.

**"Mixture of Horizons"**: Explicitly addresses the trade-off where "longer horizons facilitate structural foresight but shorter horizons ensure precise control," and uses per-position gating to weight predictions from different horizon lengths.

**"VLA Knows Its Limits"**: Research showing VLA models' attention patterns reveal that "later actions fail to adaptively adjust to environmental changes" -- they "repeatedly rely on static visual-linguistic features that are informative for early actions but increasingly outdated or misleading for later ones."

**The key theoretical reason**: In parallel prediction models (OpenVLA-OFT, ACT, Diffusion Policy, pi0), all actions are predicted from the **same single observation**. Later actions in the chunk correspond to timesteps that are temporally further from the observation. Since the environment evolves, predicting actions further into the future from a single snapshot is inherently harder -- the mapping from observation to action becomes more uncertain as temporal distance increases. This should manifest as higher per-position loss for later chunk positions during training.

## 6. PER in Supervised Learning: Evidence It Can Be Harmful

The paper "Understanding and Mitigating the Limitations of Prioritized Experience Replay" (Pan et al., 2022, published at UAI) provides both theoretical and empirical evidence:

- **Theoretical finding**: Error-based prioritized sampling for MSE minimization is mathematically equivalent to uniform sampling with a cubic power loss. This means PER implicitly changes the loss function rather than truly improving optimization.
- **Empirical finding**: In supervised learning (regression) settings, PER performed **worse** than uniform sampling.
- **Two core limitations**: (1) outdated priorities -- the loss landscape changes during training but priorities lag, and (2) insufficient coverage of the sample space -- high-loss samples are oversampled at the expense of others.

In an offline/supervised setting (which is what VLA training is -- behavior cloning from demonstrations), there is no evolving replay buffer or non-stationarity that PER was designed to address. The fixed dataset means priorities become a static reweighting that biases the loss function without the exploration benefit PER provides in online RL.

---

## Answer to Your Critical Question

**In standard VLA action-chunked training (OpenVLA-OFT, ACT, Diffusion Policy, pi0), the model predicts all K actions from a single observation WITHOUT teacher forcing within the chunk.** This is true for all the major paradigms:

- OpenVLA-OFT: empty embeddings + bidirectional attention
- ACT: learnable queries + CVAE, no ground-truth in decoder
- pi0: flow matching denoises all positions simultaneously
- Diffusion Policy: denoises all positions simultaneously

**This means the paper's assumption that per-position loss varies significantly within chunks is architecturally well-founded.** Later positions ARE harder because they must predict actions for timesteps that are temporally more distant from the conditioning observation. Multiple papers implicitly or explicitly build on this observation (A2C2's positional correction, Mixture of Horizons' per-position gating, Bidirectional Decoding's analysis).

The one exception would be if someone were using a purely autoregressive VLA with teacher forcing and multi-step action chunks -- in that case, during *training*, all positions would be approximately equally easy (since each token sees the ground truth for all previous tokens). But at *inference* time, the autoregressive model would still suffer from compounding errors at later positions. This autoregressive-with-teacher-forcing setup is uncommon for action-chunked VLAs; the dominant approaches are all parallel.

Sources:
- [OpenVLA-OFT Paper (arXiv:2502.19645)](https://arxiv.org/html/2502.19645v1)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [pi0 Paper (arXiv:2410.24164)](https://arxiv.org/html/2410.24164v1)
- [pi0 PDF](https://www.pi.website/download/pi0.pdf)
- [ACT / ALOHA Paper](https://tonyzhaozh.github.io/aloha/)
- [ACT Policy Explained](https://www.roboticscenter.ai/blog/act-policy-explained)
- [ACT Hugging Face Documentation](https://huggingface.co/docs/lerobot/act)
- [Leave No Observation Behind (A2C2) (arXiv:2509.23224)](https://arxiv.org/html/2509.23224v1)
- [Bidirectional Decoding (arXiv:2408.17355)](https://arxiv.org/html/2408.17355v1)
- [Mixture of Horizons](https://timsty1.github.io/moh/)
- [VLA Knows Its Limits (arXiv:2602.21445)](https://arxiv.org/html/2602.21445)
- [Understanding and Mitigating PER Limitations](https://arxiv.org/abs/2007.09569)
- [PER Limitations (UAI 2022 proceedings)](https://proceedings.mlr.press/v180/pan22a/pan22a.pdf)
- [PD-VLA Parallel Decoding (arXiv:2503.02310)](https://arxiv.org/html/2503.02310v1)
- [Action Chunking Blog Post](https://www.maximilianigl.com/blog/action-chunking)
- [Legato: Learning Native Continuation (arXiv:2602.12978)](https://arxiv.org/html/2602.12978)
- [Training-Time Action Conditioning (arXiv:2512.05964)](https://arxiv.org/html/2512.05964)
- [AR-VLA: True Autoregressive Action Expert](https://arxiv.org/html/2603.10126)

agentId: afb599c2ddc537543 (use SendMessage with to: 'afb599c2ddc537543' to continue this agent)
&lt;usage>total_tokens: 31978
tool_uses: 20
duration_ms: 272337&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d63a3798-4c1b-43fa-a23c-a875f6eb2d47",
  "isSidechain": false,
  "promptId": "8f591815-615c-4239-a161-f479c58f1dd2",
  "type": "user",
  "uuid": "59548276-7bd0-4ec2-a6b1-9a30291e019d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "This is a critical question for an ML paper review. I need to understand how VLA models with action chunking predict their action chunks, because it determines whether per-position training loss varies across chunk positions.\n\nSearch for:\n\n1. \"OpenVLA-OFT action chunking implementation\" — How does OpenVLA-OFT predict action chunks? Is it autoregressive within the chunk (each action conditions on previous), or does it predict all K actions in parallel from the observation?\n\n2. \"action chunking teacher forcing VLA training\" — Is there teacher forcing within action chunks during VLA training?\n\n3. \"pi0 action prediction mechanism\" — How does pi0 predict action chunks (flow matching, parallel)?\n\n4. \"ACT action chunking transformer prediction mechanism\" — The original ACT paper — does it predict chunks in parallel via CVAE or autoregressively?\n\n5. \"action chunk loss per position training\" — Any evidence of per-position loss variation during training\n\n6. \"prioritized experience replay supervised learning failure\" OR \"PER doesn't work supervised learning\" — Evidence that PER-style methods fail in supervised settings\n\nThe key question: In standard VLA action-chunked training (e.g., OpenVLA-OFT), does the model predict all K actions from a single observation (making later positions harder because they're temporally distant from the observation), or does it use teacher forcing within the chunk (making all positions approximately equally difficult)?\n\nThis distinction is critical because the paper under review assumes per-position loss varies significantly within chunks.",
    "agentId": "afb599c2ddc537543",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information to provide a thorough answer. Let me compile the findings.\n\n---\n\nHere is a detailed synthesis of my findings across all six topics:\n\n## 1. OpenVLA-OFT: Parallel Prediction, NOT Autoregressive Within Chunks\n\nOpenVLA-OFT predicts **all K actions in parallel from the observation in a single forward pass**. It does NOT use autoregressive decoding within the action chunk. The key architectural changes from the original OpenVLA:\n\n- **Empty action embeddings** replace teacher-forced ground-truth inputs. These embeddings differ only in positional encoding values -- they carry no information about the ground-truth actions.\n- **Bidirectional attention mask** replaces the causal attention mask, so each action position can attend to all other positions and all observation tokens simultaneously.\n- An **MLP action head** maps decoder hidden states to continuous action values, trained with **mean L1 loss** between predicted and ground-truth actions.\n\nThis is a critical distinction: **there is no teacher forcing within the action chunk during training**. Each action position must predict its value solely from the observation tokens (image, language, robot state) and the positional encoding indicating which timestep it corresponds to. The model cannot \"cheat\" by looking at ground-truth actions at earlier positions within the chunk.\n\nThe original base OpenVLA (without OFT) **did** use autoregressive teacher forcing -- ground-truth action tokens shifted right by one position with causal masking, standard next-token prediction with cross-entropy loss. But OpenVLA-OFT fundamentally changed this to parallel decoding.\n\nPaper: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" (arXiv:2502.19645)\n\n## 2. Teacher Forcing Within Chunks: Generally NO for Modern VLA Models\n\nFor models using **parallel decoding** (OpenVLA-OFT), **flow matching** (pi0), **diffusion** (Diffusion Policy), or **CVAE** (ACT), there is **no teacher forcing within the action chunk**. All positions are predicted simultaneously from the observation:\n\n- **OpenVLA-OFT**: Empty action embeddings + bidirectional attention; no ground-truth actions provided during training's forward pass through the action head.\n- **pi0**: Flow matching denoises the entire chunk simultaneously; the model predicts a vector field for all H=50 action positions at once.\n- **Diffusion Policy**: Denoises all 16-32 action positions in parallel, conditioned on the observation.\n- **ACT**: Decoder uses learnable positional queries (not ground-truth actions) + cross-attention to observation tokens; explicitly noted that \"no ground truth information is passed into the decoder\" so there is \"no need for causal masking.\"\n\nThe only VLA paradigm that uses teacher forcing within a chunk is the **original autoregressive token-prediction** approach (e.g., base OpenVLA, RT-2), where each action token is predicted conditioned on previous ground-truth tokens during training. But these models typically predict a single timestep's action (e.g., 7 tokens for one action), not a multi-step chunk.\n\n## 3. pi0: Flow Matching, All Positions Simultaneously\n\npi0 uses **conditional flow matching** to predict action chunks of H=50 timesteps in parallel:\n\n- During training, given observation o_t, the model learns to denoise a noisy action chunk A_t^tau back to the clean chunk A_t, where tau controls noise level. The training loss is MSE between the predicted vector field and the true denoising direction.\n- The **action expert** uses **full bidirectional attention** across action tokens, meaning all 50 positions are processed together, not sequentially.\n- At inference, the model performs ~10 iterative denoising steps (each processing all 50 positions simultaneously), which is faster than 50 autoregressive steps.\n- The noise schedule uses a shifted beta distribution emphasizing lower timesteps (noisier actions), but this is about the *denoising* timestep tau, not about position within the chunk.\n\nPaper: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\" (arXiv:2410.24164)\n\n## 4. ACT: CVAE, Parallel Prediction via Learnable Queries\n\nACT predicts entire action chunks in a **single forward pass** using a **non-autoregressive** design:\n\n- The decoder takes **k learnable positional queries** (one per action in the chunk), the latent z from the CVAE, and observation tokens.\n- Critically: \"No ground truth information is passed into the decoder (just the learnable query embeddings) and thus no need for causal masking! For the generation of each action, the decoder can consider both the earlier and subsequent actions it is predicting.\"\n- This is inspired by DETR (object detection), which similarly uses a set of queries to predict outputs in parallel.\n- Training loss: L1 reconstruction loss + KL-divergence regularization (CVAE objective).\n\nThe CVAE is a training aid to handle multimodality in demonstrations -- without it, the model averages across demonstration styles. But the prediction mechanism is fundamentally parallel.\n\nPaper: \"Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware\" (Tony Zhao et al.)\n\n## 5. Per-Position Loss Variation: Indirect Evidence That Later Positions ARE Harder\n\nWhile I did not find papers that explicitly plot per-position training loss curves across chunk positions, there is strong indirect evidence that **later positions within a chunk are harder to predict**, and multiple papers build on this assumption:\n\n**\"Leave No Observation Behind\" (A2C2)**: Introduces a correction module that explicitly encodes \"the index of the base action within the chunk\" as a positional feature, implying that different positions need different corrections. The paper shows +23% improvement on dynamic tasks.\n\n**\"Bidirectional Decoding\"**: Documents that \"recent states are often more important to decision making\" and that prediction quality degrades for later positions because the initial observation becomes \"outdated\" -- errors compound in open-loop execution.\n\n**\"Mixture of Horizons\"**: Explicitly addresses the trade-off where \"longer horizons facilitate structural foresight but shorter horizons ensure precise control,\" and uses per-position gating to weight predictions from different horizon lengths.\n\n**\"VLA Knows Its Limits\"**: Research showing VLA models' attention patterns reveal that \"later actions fail to adaptively adjust to environmental changes\" -- they \"repeatedly rely on static visual-linguistic features that are informative for early actions but increasingly outdated or misleading for later ones.\"\n\n**The key theoretical reason**: In parallel prediction models (OpenVLA-OFT, ACT, Diffusion Policy, pi0), all actions are predicted from the **same single observation**. Later actions in the chunk correspond to timesteps that are temporally further from the observation. Since the environment evolves, predicting actions further into the future from a single snapshot is inherently harder -- the mapping from observation to action becomes more uncertain as temporal distance increases. This should manifest as higher per-position loss for later chunk positions during training.\n\n## 6. PER in Supervised Learning: Evidence It Can Be Harmful\n\nThe paper \"Understanding and Mitigating the Limitations of Prioritized Experience Replay\" (Pan et al., 2022, published at UAI) provides both theoretical and empirical evidence:\n\n- **Theoretical finding**: Error-based prioritized sampling for MSE minimization is mathematically equivalent to uniform sampling with a cubic power loss. This means PER implicitly changes the loss function rather than truly improving optimization.\n- **Empirical finding**: In supervised learning (regression) settings, PER performed **worse** than uniform sampling.\n- **Two core limitations**: (1) outdated priorities -- the loss landscape changes during training but priorities lag, and (2) insufficient coverage of the sample space -- high-loss samples are oversampled at the expense of others.\n\nIn an offline/supervised setting (which is what VLA training is -- behavior cloning from demonstrations), there is no evolving replay buffer or non-stationarity that PER was designed to address. The fixed dataset means priorities become a static reweighting that biases the loss function without the exploration benefit PER provides in online RL.\n\n---\n\n## Answer to Your Critical Question\n\n**In standard VLA action-chunked training (OpenVLA-OFT, ACT, Diffusion Policy, pi0), the model predicts all K actions from a single observation WITHOUT teacher forcing within the chunk.** This is true for all the major paradigms:\n\n- OpenVLA-OFT: empty embeddings + bidirectional attention\n- ACT: learnable queries + CVAE, no ground-truth in decoder\n- pi0: flow matching denoises all positions simultaneously\n- Diffusion Policy: denoises all positions simultaneously\n\n**This means the paper's assumption that per-position loss varies significantly within chunks is architecturally well-founded.** Later positions ARE harder because they must predict actions for timesteps that are temporally more distant from the conditioning observation. Multiple papers implicitly or explicitly build on this observation (A2C2's positional correction, Mixture of Horizons' per-position gating, Bidirectional Decoding's analysis).\n\nThe one exception would be if someone were using a purely autoregressive VLA with teacher forcing and multi-step action chunks -- in that case, during *training*, all positions would be approximately equally easy (since each token sees the ground truth for all previous tokens). But at *inference* time, the autoregressive model would still suffer from compounding errors at later positions. This autoregressive-with-teacher-forcing setup is uncommon for action-chunked VLAs; the dominant approaches are all parallel.\n\nSources:\n- [OpenVLA-OFT Paper (arXiv:2502.19645)](https://arxiv.org/html/2502.19645v1)\n- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)\n- [pi0 Paper (arXiv:2410.24164)](https://arxiv.org/html/2410.24164v1)\n- [pi0 PDF](https://www.pi.website/download/pi0.pdf)\n- [ACT / ALOHA Paper](https://tonyzhaozh.github.io/aloha/)\n- [ACT Policy Explained](https://www.roboticscenter.ai/blog/act-policy-explained)\n- [ACT Hugging Face Documentation](https://huggingface.co/docs/lerobot/act)\n- [Leave No Observation Behind (A2C2) (arXiv:2509.23224)](https://arxiv.org/html/2509.23224v1)\n- [Bidirectional Decoding (arXiv:2408.17355)](https://arxiv.org/html/2408.17355v1)\n- [Mixture of Horizons](https://timsty1.github.io/moh/)\n- [VLA Knows Its Limits (arXiv:2602.21445)](https://arxiv.org/html/2602.21445)\n- [Understanding and Mitigating PER Limitations](https://arxiv.org/abs/2007.09569)\n- [PER Limitations (UAI 2022 proceedings)](https://proceedings.mlr.press/v180/pan22a/pan22a.pdf)\n- [PD-VLA Parallel Decoding (arXiv:2503.02310)](https://arxiv.org/html/2503.02310v1)\n- [Action Chunking Blog Post](https://www.maximilianigl.com/blog/action-chunking)\n- [Legato: Learning Native Continuation (arXiv:2602.12978)](https://arxiv.org/html/2602.12978)\n- [Training-Time Action Conditioning (arXiv:2512.05964)](https://arxiv.org/html/2512.05964)\n- [AR-VLA: True Autoregressive Action Expert](https://arxiv.org/html/2603.10126)"
      }
    ],
    "totalDurationMs": 272337,
    "totalTokens": 31978,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 28349,
      "output_tokens": 2815,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2815,
          "cache_read_input_tokens": 28349,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 813,
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
  "sourceToolAssistantUUID": "d63a3798-4c1b-43fa-a23c-a875f6eb2d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T17:50:03.499Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have a very comprehensive picture. Let me synthesize all my findings and form my final judgment.

## Complete Assessment

### Novelty Analysis

**What's genuinely novel:**
1. The temporal divergence δ as a priority signal — no existing work decomposes per-position training losses within action chunks as a priority signal for training data selection
2. The differentiation from AdaMix is clear and valid — AdaMix aggregates to scalar, CDAP decomposes

**What's NOT novel:**
1. PER + IS correction + sum-tree — Schaul et al. 2016


2. Freshness/age decay — FreshPER 2026
3. Contact-phase weighting — inspired by DAM-VLA
4. The observation that later chunk positions are harder — well-established across multiple VLA papers

I also need to correct some citation details: RINSE is a workshop paper at ICML 2025, not a main conference contribution, and Token Cleaning was accepted as a poster rather than a spotlight. There's also some missing work I should track down, including a token priority paper and EAFT.

Now looking at feasibility — the architecture actually supports this well since OpenVLA-OFT does parallel chunk prediction without teacher forcing, so per-position loss weighting should have real effects. Implementation is manageable and the datasets are all publicly available. But there's a real concern here: PER has documented failure modes in supervised learning. Pan et al. showed it's mathematically equivalent to loss reweighting and underperforms uniform sampling in supervised regression, which is exactly what VLA fine-tuning is. I'd need to argue that the temporal structure in VLAs makes this fundamentally different from generic supervised settings. There's also the staleness problem with lazy priority updates that needs addressing.

The timeline is brutal though — 13 days to abstract deadline, and fitting in CDAP implementation, pilot experiments, re-implementing AdaMix, running 8 baselines with ablations, and writing everything is extremely ambitious even with auto-research mode.

On impact: if the temporal divergence signal actually works, this becomes a useful training tool for the VLA community and the empirical characterization of temporal loss profiles has independent value. But realistically, this is a training efficiency trick rather than a fundamental contribution, and the gains over AdaMix might be modest since AdaMix already gets 13% improvement.

The framing is solid though — the idea is well-articulated with proper differentiation from related work, clean math, explicit ablations isolating each component, and honest hypothesis framing rather than overstated claims. The temporal divergence signal itself is genuinely novel for VLA training, though it's really a specific metric applied within a standard framework of PER, importance sampling, and age decay. The core assumption about per-position loss variation is architecturally sound given parallel prediction without teacher forcing, and implementation should be straightforward.

The real concerns are that PER has documented failures in supervised learning that aren't addressed, the timeline is extremely tight for CoRL 2026, and the overall contribution feels incremental — a training trick for a specific model class rather than a fundamental insight. Even if the temporal loss profiling works, gains over AdaMix might be modest. The scoring comes out to 3.5 overall, which falls short of the 4.0 threshold, so I need to revise by addressing the PER failure literature and clarifying what the key empirical observations actually are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59548276-7bd0-4ec2-a6b1-9a30291e019d",
  "isSidechain": false,
  "requestId": "req_011CazzPP4HhkxZv5yWiXswW",
  "type": "assistant",
  "uuid": "9dd0a395-4e21-4c63-ba8b-fe1601e34b9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPBBXheAvT8RZ5RebfMrKD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13081,
      "cache_read_input_tokens": 38787,
      "output_tokens": 3617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3617,
          "cache_read_input_tokens": 38787,
          "cache_creation_input_tokens": 13081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13081
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

_source line 29 · 2026-05-13T17:50:50.787Z_

I now have comprehensive findings from my independent research. Let me synthesize everything into my review.

## Key Independent Findings

**Critical architectural verification:** OpenVLA-OFT (the target platform) uses **parallel chunk prediction** with empty action embeddings + bidirectional attention — there is NO teacher forcing within action chunks during training. This means later positions are genuinely harder (predicting from a temporally distant observation), validating CDAP's core assumption about per-position loss variation. This is a significant positive for the idea.

**However, several important concerns remain:**

1. **PER failure in supervised learning** (Pan et al., UAI 2022) — mathematically showed PER for MSE is equivalent to uniform sampling with cubic power loss, and empirically showed PER performs *worse* than uniform in supervised regression. VLA fine-tuning IS supervised regression.

2. **Venue citation errors** — RINSE is an ICML 2025 *Workshop* (DataWorld) paper, not main conference. Token Cleaning is ICML 2025 *Poster*, not Spotlight.

3. **AdaMix status** — confirmed: was submitted to ICLR 2026 and *withdrawn*. Confirmed it uses aggregated scalar MSE, not per-position decomposition.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The temporal divergence signal δ as a VLA-specific priority is genuinely novel — no prior work decomposes per-position training losses within action chunks for data prioritization. The differentiation from AdaMix (scalar aggregation) is clear. However, the surrounding framework is a well-known combination (PER + IS correction + age decay + contact-phase heuristic), and the observation that later chunk positions are inherently harder is already established by VLA Knows Its Limits, A2C2, and Mixture of Horizons — CDAP's novelty is applying this known phenomenon as a training priority signal, not discovering it."},
    "feasibility": {"score": 3.5, "rationale": "Core assumption is architecturally sound — OpenVLA-OFT uses parallel chunk prediction without teacher forcing, so per-position loss SHOULD vary. Implementation is lightweight (~150 lines), datasets are public, compute is reasonable. Two serious concerns: (1) Pan et al. (UAI 2022) proved PER is equivalent to implicit loss reweighting in supervised settings and showed it underperforms uniform sampling in regression — this directly threatens CDAP since VLA SFT is supervised regression; (2) Timeline is extremely tight (13 days to abstract) even for auto-research mode."},
    "clarity": {"score": 4, "rationale": "Exceptionally well-structured: comprehensive landscape with proper differentiation from AdaMix/DAM-VLA/iw-SFT, clean mathematical formulation, honest hypothesis framing (not overstated theorems), and an explicit ablation path (Uniform → AdaMix → Scalar PER → Full CDAP) that isolates the temporal decomposition contribution. Minor venue citation errors."},
    "impact": {"score": 3, "rationale": "If δ proves informative, CDAP would be a useful training efficiency tool for action-chunked VLA models, and the first systematic empirical analysis of temporal loss profile evolution is independently valuable. But the contribution is incremental — a training-time sampling trick for a specific model class. The potential gains over AdaMix (which already achieves 13% improvement) may be modest, and the method is limited to VLA models with explicit action chunking."}
  },
  "issues": [
    "CRITICAL — PER FAILURE IN SUPERVISED LEARNING UNADDRESSED: Pan et al. (UAI 2022, 'Understanding and Mitigating the Limitations of Prioritized Replay') proved that error-based prioritized sampling for MSE minimization is mathematically equivalent to uniform sampling with a cubic power loss, and empirically showed PER performs WORSE than uniform in supervised regression. VLA fine-tuning is supervised L1/L2 regression. CDAP must directly address this foundational concern — why would chunk-decomposed PER succeed where standard PER demonstrably fails in supervised settings? The temporal decomposition may break this equivalence (because δ captures structure beyond loss magnitude), but this argument is not made.",
    "VENUE CITATION ERRORS: (1) RINSE (arXiv:2604.23000) was presented at the 'DataWorld: Unifying Data Curation Frameworks Across Domains' WORKSHOP at ICML 2025, NOT the main conference. Citing it as 'ICML 2025' without 'Workshop' is misleading. (2) Token Cleaning (arXiv:2502.01968) appears in ICML 2025 virtual site as a Poster (icml.cc/virtual/2025/poster/43777), not a Spotlight as claimed.",
    "MISSING DISCUSSION OF DAM-VLA AS PARTIAL PRIOR: DAM-VLA applies position-dependent exponential decay weighting within action chunks during training — this IS a form of intra-chunk loss decomposition, albeit with fixed (not data-driven) weights. The landscape discusses DAM-VLA but the novelty claim 'no existing work exploits the intra-chunk temporal loss profile' is too strong. A more defensible claim: 'no existing work uses the EMPIRICAL intra-chunk loss profile as a DATA-DRIVEN priority signal.'",
    "INSUFFICIENT DIFFERENTIATION FROM IMPLICIT LOSS REWEIGHTING: Pan et al. showed PER implicitly changes the effective loss function rather than improving optimization. CDAP's IS correction addresses the bias but doesn't address the coverage problem — high-priority transitions are oversampled, leaving low-priority transitions undertrained. The ε_mix uniform mixing partially addresses this, but with large datasets (100K+ transitions) and short VLA fine-tuning runs (50K-150K steps per OpenVLA-OFT), most transitions may never be resampled even once. The coverage analysis promised in the evaluation section should quantify this.",
    "TIMELINE RISK ELEVATED: 13 days to abstract deadline, 15 days to paper deadline. The pipeline requires: (1) implement CDAP (~2 days), (2) reimplement AdaMix (~2-3 days, no public code), (3) run RoboMimic-MH pilot (~1-2 days), (4) run 8 baselines + ablations on 4 benchmarks (~5-7 days), (5) analysis + writing (~3-5 days). Even with 8× A100 cluster running 24/7, this is extremely tight. Recommend scoping down to 2 benchmarks (RoboMimic-MH + SimplerEnv) for CoRL submission with remaining benchmarks for camera-ready.",
    "MISSING RELATED WORK (minor): 'Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority' (arXiv:2602.01227, Feb 2026) formalizes SFT as distribution reshaping via token-level priority, directly relevant to CDAP's framing. Should be discussed alongside Token Cleaning, ProFit, PEAR."
  ],
  "feedback": "The idea has matured well through 4 rounds — the temporal divergence signal δ is the right VLA-specific contribution, and the landscape/experimental design are strong. Three things will elevate this to CoRL quality:\n\n1. **ADDRESS PER-IN-SUPERVISED-LEARNING FAILURE HEAD-ON.** This is the most important remaining gap. Pan et al. (UAI 2022) showed PER ≡ implicit loss reweighting and fails in supervised regression. You must argue why CDAP is different. The key argument: Pan's equivalence holds for scalar-loss PER, but CDAP's temporal decomposition captures *structural* information (why a transition is hard, not just how hard) that scalar reweighting cannot express. Specifically, two transitions with identical aggregate loss μ but different δ receive different priorities under CDAP but identical priorities under scalar PER — this breaks the cubic-power-loss equivalence. Make this argument explicit and test it empirically: if CDAP with δ outperforms scalar PER (α_δ=0), it validates that the structural signal overcomes PER's supervised-learning limitations.\n\n2. **TIGHTEN THE NOVELTY CLAIM.** Change 'no existing work exploits the intra-chunk temporal loss profile' to 'no existing work uses the empirical intra-chunk loss profile as a data-driven adaptive priority signal.' This honestly acknowledges DAM-VLA's fixed positional weighting while maintaining CDAP's clear differentiation.\n\n3. **SCOPE DOWN FOR CoRL.** With 13 days to abstract, prioritize: (a) RoboMimic-MH pilot first (validates δ signal in 1-2 days), (b) if positive, run full comparison on RoboMimic-MH + SimplerEnv only, (c) add Sirius-Fleet and OXE for camera-ready. Four benchmarks × 8 baselines in 15 days is unrealistic.\n\n4. **Fix venue citations.** RINSE → 'ICML 2025 Workshop (DataWorld)'. Token Cleaning → 'ICML 2025'. Drop the 'Spotlight' claim unless verified independently.\n\n5. **Add Pan et al. (UAI 2022) to the landscape** under 'Online Hard Example Mining' or as a new subsection on PER limitations. Position CDAP as addressing PER's known failure modes in supervised settings through temporal decomposition.",
  "reason": "Strong VLA-specific insight (temporal divergence δ) with clean experimental design, but must address the documented failure of PER in supervised learning settings and tighten the novelty claim relative to DAM-VLA's fixed intra-chunk weighting."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dd0a395-4e21-4c63-ba8b-fe1601e34b9d",
  "isSidechain": false,
  "requestId": "req_011CazzPP4HhkxZv5yWiXswW",
  "type": "assistant",
  "uuid": "f9b3acbc-d6ec-4770-8204-e692db40e668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPBBXheAvT8RZ5RebfMrKD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13081,
      "cache_read_input_tokens": 38787,
      "output_tokens": 3617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3617,
          "cache_read_input_tokens": 38787,
          "cache_creation_input_tokens": 13081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13081
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f9b3acbc-d6ec-4770-8204-e692db40e668",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDAP novelty against AdaMix and temporal decomposition claims",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f9b3acbc-d6ec-4770-8204-e692db40e668",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDAP novelty against AdaMix and temporal decomposition claims",
  "sessionId": "79b7d0a3-cb81-4607-9e85-3b5600200248"
}
```

---
