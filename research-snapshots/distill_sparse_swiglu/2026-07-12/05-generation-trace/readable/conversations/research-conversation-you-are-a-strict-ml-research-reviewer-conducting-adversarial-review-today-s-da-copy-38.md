# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/29db5b43-7986-4f2e-9840-40109a8a2d7f.jsonl`
- **Structured JSON:** [`9b37595993b794f94e8e.json`](../../sessions/9b/9b37595993b794f94e8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T10:45:25.326Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T10:45:25.326Z",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\nDirection：因为真实数据采样的时候会有很多噪声，比如收集时的冗余动作等，如何避免训练数据中的噪声影响vla的训练，可以使用一个经验池的形式来训练，借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选，再适当过滤掉一些低分数的冗余动作，如果是从一些底层理论角度提出了筛选方法 感觉不用真机也是可以接受的**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"PhaseOT: Mode-Aware Phase-Level Demonstration Quality Diagnosis via Structured Optimal Transport\",\n  \"core_problem\": \"How to diagnose demonstration quality at the task-phase granularity — identifying not just which demonstrations are noisy, but which specific phases (approach, grasp, transport, placement) are anomalous — in a mode-aware, unsupervised manner that uses principled distributional distances, preserves valid strategy diversity across multiple solution modes, and provides interpretable diagnostic profiles rather than opaque scalar scores or unstructured per-transition flags?\",\n  \"opportunity\": \"The demonstration curation field has matured rapidly (2024–2026), with methods now spanning dataset-level (Re-Mix), trajectory-level (DemInf, CUPID, QoQ, RINSE, Demo-SCORE), and transition-level (SCIZOR, CIQL) granularities. SCIZOR (ICRA 2026) represents the current frontier, operating at the state-action pair level and achieving partial trajectory recovery (54% of recovery behaviors fully maintained, 31% partially maintained) with categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision, etc.).\\n\\nHowever, a critical capability gap remains at the intersection of three dimensions that no existing method addresses simultaneously:\\n\\n(1) **Semantic phase-level diagnosis vs. raw transition scores**: SCIZOR produces per-transition anomaly flags and categorical labels, but these are individual symptom detections — analogous to listing elevated lab values. PhaseOT produces structured diagnostic profiles at the semantic task-phase level — analogous to a medical report that says 'grasp phase is anomalous (3.2σ from mode centroid), approach and transport phases are nominal.' This phase-level granularity is the right abstraction for actionable feedback: it maps directly to interpretable task stages, enables targeted re-demonstration of specific phases, and supports phase-level importance weighting for policy training.\\n\\n(2) **Mode-aware scoring that preserves strategy diversity**: No existing curation method discovers or accounts for multiple valid demonstration strategies. DemInf's global mutual information conflates minority strategies with noise. SCIZOR treats all demonstrations uniformly via progress prediction. RINSE assumes smoothness universally correlates with quality. Shi et al. (2025) showed that 'spatial multimodality' (different trajectory paths) benefits policy learning while 'velocity multimodality' (same path at different speeds) is harmful, yielding 15% improvement from velocity debiasing alone — but no curation method exploits this distinction. PhaseOT's mode discovery via phase-structured distances naturally separates beneficial strategic diversity from harmful execution noise.\\n\\n(3) **Principled distributional distances with theoretical guarantees**: Existing phase/transition-level methods rely on heuristic quality signals — SCIZOR uses progress prediction, S2I uses supervised contrastive learning with expert references, CIQL uses dynamics-based confidence scoring. PhaseOT uses Wasserstein distances within aligned phase segments, providing concentration inequalities for anomaly detection that formalize when and why phase decomposition improves detection power over trajectory-level scoring.\\n\\nThe phase-localized noise model underlying PhaseOT is well-supported empirically. SCIZOR's own categorical failure taxonomy shows that failure types are inherently phase-localized: 'Manipulation Failure' occurs during contact phases, 'Laggy Motion' during transport, 'Pause' during transitions. RoboMimic's Tool Hang failure analysis similarly documents phase-specific failures: Insertion Miss, Failed Insertion, Failed Tool Grasp, Tool Drop — each mapping to a specific manipulation phase. Manipulation tasks have inherent phase structure where failures concentrate at contact events (grasp, insertion) more than during free-space motion (approach, retreat).\\n\\nThe mathematical apparatus for PhaseOT draws inspiration from the adapted optimal transport literature (Backhoff-Veraguas et al. 2020, Cheridito & Eckstein 2025), which emphasizes respecting temporal causality in distributional comparison of stochastic processes. However, PhaseOT employs a simpler, practically motivated phase-constrained transport formulation rather than the full adapted/bicausal framework, which involves nested conditional optimization unsuited to the discrete phase-segmented structure of manipulation demonstrations. Concurrently, Xu & Gould (CVPR 2024) demonstrated the value of encoding temporal consistency into optimal transport for action segmentation, validating the broader principle.\",\n  \"landscape\": \"The demonstration curation field has consolidated around methods at multiple granularity levels:\\n\\n**Trajectory-level, policy-dependent methods** (require training or evaluating a policy):\\n- CUPID (CoRL 2025): Influence functions on expected return from closed-loop rollouts. SOTA with <33% curated data on RoboMimic. +38% on real Franka tasks. Limitation: requires evaluation rollouts, architecture-specific.\\n- QoQ (arXiv Mar 2026): Maximum influence scoring with trajectory-wise aggregation. 99.2% on RoboMimic Can. Limitation: requires validation set of known-good demos.\\n- DataMIL (May 2025): Datamodels for end-to-end policy-driven selection. 10% on MetaWorld 50 tasks. Limitation: requires multiple policy retrainings.\\n- Demo-SCORE (RSS 2025): Self-curation via online rollout classifiers. 15-35% on real-world ALOHA tasks. Limitation: policy-dependent, requires rollouts.\\n\\n**Trajectory-level, policy-agnostic methods** (no policy training needed):\\n- DemInf (RSS 2025): k-NN mutual information estimators on VAE embeddings. 5-10% on RoboMimic. Key limitation: global MI conflates valid strategy diversity with noise — in bimodal tasks (Push-T), demos from the minority strategy may receive low MI scores despite being high-quality executions of an alternative approach.\\n- RINSE (ICML 2025): Spectral Arc Length + Trajectory-Envelope Distance smoothness metrics. 16-20% on RoboMimic. Limitation: assumes smoothness universally correlates with quality.\\n- FAKTUAL (arXiv 2026): Signature-kernel entropy for diversity-aware curation. Shows RoboMimic Transport has highest demonstration diversity.\\n\\n**Transition/segment-level methods** (finer than trajectory):\\n- SCIZOR (ICRA 2026): Self-supervised progress prediction + visual-action deduplication for transition-level filtering. +32.9% on Sirius-Fleet, +5.4% on RoboMimic, outperforms DemInf by 19.2% on Sirius-Fleet. Achieves partial trajectory recovery: 54% of recovery behaviors fully maintained, 31% partially maintained. Produces categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision, Move Back and Forth). **Strongest practical baseline and primary comparison point for PhaseOT.** Limitations: (a) heuristic progress signal without distributional guarantees, (b) no mode discovery — treats all demonstrations uniformly, which penalizes valid minority strategies, (c) transition-level flags lack semantic phase-level interpretability.\\n- S2I (ICRA 2025): Heuristic keyframe segmentation → supervised contrastive learning → kNN distance-weighted voting for segment quality classification. +22.2% on Square with Diffusion Policy. Requires 3 expert reference demos per task (supervised), uses learned embeddings not distributional distances.\\n- CIQL (Bu et al., IEEE RA-L 2024): Confidence-based Inverse soft-Q Learning for per-transition confidence scoring via dynamics evaluation. Aligns human intent from imperfect demonstrations. Limitation: confidence scores are dynamics-based heuristics, not distributional distances; no mode awareness or phase-level profiles.\\n- SDIL (KDD 2023): Skill disentanglement via latent variables + PU learning for per-skill optimality estimation.\\n- FIDeL (2025): OT-based per-timestep anomaly scoring using Sinkhorn distances — but for execution monitoring during deployment, not dataset curation.\\n\\n**Demonstration diversity analysis**:\\n- Shi et al. (arXiv Jul 2025): Critical distinction between spatial multimodality (different trajectory paths — beneficial, should be preserved) and velocity multimodality (different speeds on same path — harmful, should be filtered). Velocity debiasing yields 15% improvement = 2.5x more data equivalent. Directly motivates mode-aware quality assessment.\\n\\n**Data mixture optimization** (domain-level, complementary):\\n- Re-Mix (CoRL 2025): DRO-based mixture weight optimization. 38% over uniform on Open X-Embodiment.\\n\\n**Importance-weighted imitation learning** (how to USE quality scores):\\n- DWBC (ICML 2022): Discriminator-weighted offline IL — quality scores as per-sample BC weights.\\n- VACO (ICLR 2025): Value-aligned BC via bi-level optimization meta-scoring.\\n- RINSE exponential weighting: w(τ) = exp(-λ·q(τ)) shows Spearman ρ ≥ 0.89 with learned Re-Mix allocations.\\n\\n**OT in imitation learning** (applied to combination/reward/imitation, never phase-level quality diagnosis):\\n- Xu & Gould (CVPR 2024): Temporally Consistent Unbalanced OT for unsupervised action segmentation — encodes temporal consistency into Gromov-Wasserstein. Validates temporal-OT principle but targets video segmentation, not quality diagnosis.\\n- OTR (ICLR 2023), TemporalOT (NeurIPS 2024): OT for reward labeling.\\n- GWIL (ICLR 2022): Gromov-Wasserstein for cross-domain imitation.\\n- Pallage 2025 (arXiv 2504.12918): Sliced-Wasserstein for point-level outlier detection — static point clouds, no temporal structure.\\n\\n**Adapted Wasserstein distances** (theoretical inspiration — unexplored in robotics):\\n- Backhoff-Veraguas et al. (2017, 2020): Causal/bicausal OT for stochastic processes via dynamic programming with nested conditional optimization. PhaseOT's PW₂ is inspired by this work's emphasis on temporal causality but uses a simpler additive phase-constrained decomposition.\\n- Cheridito & Eckstein (Bernoulli 2025): Adapted distances for causal models.\\n- Moulos (IEEE CDC 2021): Bicausal OT for Markov chains via value iteration.\\n- These methods involve nested conditional optimization that respects filtration structure — fundamentally different from PhaseOT's additive phase decomposition, which is practically motivated rather than theoretically derived from the adapted OT framework.\\n\\n**Gap**: No method provides (1) unsupervised mode-aware scoring that preserves strategy diversity, (2) semantic phase-level quality profiles rather than trajectory-level scalars or unstructured transition-level flags, (3) principled distributional distances with theoretical guarantees for phase-localized anomaly detection. PhaseOT fills this three-dimensional gap.\",\n  \"approach\": \"**Overview**: PhaseOT is a four-stage pipeline: (1) segment trajectories into semantically meaningful task phases, (2) compute a Phase-Structured Wasserstein Distance (PW₂) that restricts transport to respect phase alignment, (3) discover strategy modes and score quality within each mode using phase-level distributional profiles, (4) produce structured diagnostic profiles for downstream filtering, weighting, or re-demonstration guidance.\\n\\n**Stage 1 — Phase Segmentation**: Each demonstration τ of length T is segmented into K phases {P₁, ..., P_K} using one of two methods (compared as an ablation):\\n- *Heuristic keyframes*: Phase boundaries at gripper state changes (open↔close) and velocity near-zero events, following S2I's approach. Simple, interpretable, works for manipulation tasks with clear grasp/release events.\\n- *Bayesian Online Changepoint Detection (BOCPD)*: Statistical changepoint detection on the joint state-action stream, automatically discovering phase boundaries without gripper-state assumptions. More general, applicable to locomotion or contact-rich tasks without discrete gripper events.\\nPhase boundaries are aligned across all demonstrations in a dataset using dynamic time warping on phase-discriminative features, ensuring comparable phases across demos. The number of phases K is validated against task semantics (typical manipulation: K=3–5 for approach/grasp/transport/place/retreat).\\n\\n**Stage 2 — Phase-Structured Wasserstein Distance (PW₂)**: Each phase P_k of a demonstration τ is represented as a discrete probability measure μ_{τ,k} = (1/|P_k|) Σ_{t∈P_k} δ_{(s_t, a_t)} over state-action tuples within that phase. The Phase-Structured Wasserstein-2 distance between two demonstrations τ₁, τ₂ is:\\n\\n  PW²₂(τ₁, τ₂) = Σ_{k=1}^{K} w_k · W²₂(μ_{τ₁,k}, μ_{τ₂,k})\\n\\nwhere W²₂ is the standard Wasserstein-2 distance computed within each phase, and w_k are phase importance weights (uniform by default, with learned variants as ablation).\\n\\n**Clarification on relationship to adapted OT**: PW₂ is NOT the adapted/bicausal Wasserstein distance of Backhoff-Veraguas et al. (2017, 2020) or Moulos (2021). The adapted distance involves nested conditional optimization via dynamic programming, where the coupling at time t depends on the realized marginals at times 1..t-1 through the filtration structure. PW₂ is a simpler construction: it restricts admissible transport plans so that mass within phase k of one trajectory can only be transported to phase k of another, then sums the within-phase costs. This phase-constrained restriction is inspired by the adapted OT literature's emphasis on respecting temporal causality — approach states should match approach states, not grasp states — but avoids the computational complexity of nested conditional optimization, which is unnecessary for the discrete phase-segmented structure of manipulation demonstrations. The practical advantage of PW₂ over unconstrained (global) W₂ is that it concentrates anomaly signal in the phase where contamination occurs, rather than diluting it across the entire trajectory.\\n\\nThe within-phase ground cost is:\\n  c((s₁,a₁), (s₂,a₂)) = w_pos·‖ψ(pos₁)-ψ(pos₂)‖² + w_rot·d_rot(rot₁,rot₂)² + w_grip·(g₁-g₂)² + w_act·‖ψ(a₁)-ψ(a₂)‖²\\nwhere ψ denotes z-score normalization per dimension, d_rot is geodesic distance for orientations, and weights {w_*} are set equal after normalization (with sensitivity analysis as ablation). For high-dimensional observation spaces, PCA reduces to 16-32D before cost computation.\\n\\n**Theoretical property**: PW₂ lower-bounds the global W₂ distance because the phase-alignment constraint restricts the set of admissible transport plans. When contamination is localized to a subset S ⊆ {1,...,K} of phases with |S| << K, the phase-level scores concentrate the anomaly signal in those phases. Specifically, if phase k has contamination rate ε_k, the within-phase score q_k grows with ε_k while clean phases contribute near-zero q_k, yielding a phase-specific detection threshold that is tighter than the global threshold by a factor related to K/|S|.\\n\\n**Stage 3 — Mode Discovery and Phase-Level Scoring**:\\n- Compute pairwise PW₂ distance matrix over all demonstrations.\\n- Perform spectral clustering on the PW₂ affinity matrix (k selected via eigengap heuristic or silhouette analysis) to discover valid strategy modes. Mode discovery is a preprocessing step, not a claimed contribution — we use standard clustering.\\n- Within each mode m, compute the phase-level reference distribution b_{m,k} for each phase k as the Wasserstein barycenter of that phase across mode members, using the iterative reweighting scheme of Cheng & Liu (arXiv 2026) for robustness to remaining outliers.\\n- Score each demonstration τ in mode m with a phase-level quality profile:\\n  q(τ) = (q₁(τ), ..., q_K(τ))  where  q_k(τ) = W₂(μ_{τ,k}, b_{m,k})\\n- Phase-level z-scores: z_k(τ) = (q_k(τ) - μ_{m,k}) / σ_{m,k} where μ_{m,k} and σ_{m,k} are the mean and std of q_k within mode m.\\n- The trajectory-level score is the weighted sum: Q(τ) = Σ_k w_k · q_k(τ).\\n\\n**Stage 4 — Diagnostic Profile and Downstream Use** (three usage modes compared experimentally):\\n- *Hard filtering*: Remove demos with Q(τ) exceeding an adaptive threshold (median + 2·MAD of intra-mode scores). Comparable to DemInf/SCIZOR.\\n- *Soft importance weighting*: Use PW₂-derived scores as sample weights in behavioral cloning: L = Σ_τ Σ_{(s,a)∈τ} w(τ) · ℓ(π(s), a) where w(τ) = exp(-λ · Q(τ)). Connects to DWBC (ICML 2022) and VACO (ICLR 2025).\\n- *Phase-level importance weighting (key differentiator)*: L = Σ_τ Σ_k Σ_{(s,a)∈P_k(τ)} w_k(τ) · ℓ(π(s), a) where w_k(τ) = exp(-λ · q_k(τ)). This preserves good phases of otherwise-flagged demos — if a demo's grasp phase is anomalous but its approach is clean, the approach segments still contribute with full weight. Unlike SCIZOR's transition-level filtering which removes individual state-action pairs based on progress prediction, PhaseOT's phase-level weighting operates at semantic granularity: it downweights the entire grasp phase coherently rather than removing scattered transitions, maintaining temporal coherence within phases.\\n- *Diagnostic report*: For each flagged demonstration, output a structured profile: mode assignment, per-phase z-scores, phase-level failure classification (mapping high-z-score phases to failure categories via their distributional signatures), and recommended action (re-demonstrate phase k, discard entirely, or retain with reduced weight).\\n\\n**Scalable computation (two-tier)**:\\n- Tier 1 — Exact Sinkhorn (datasets ≤500 demos): For each phase pair, entropy-regularized OT via POT/geomloss. RoboMimic 300 demos × K≈4 phases: 300²/2 × 4 = 180K Sinkhorn solves × ~2ms each (smaller per-phase problems) ≈ 6 minutes on GPU.\\n- Tier 2 — Sliced Wasserstein (datasets >500 demos): O(N²·K·L·T_k log T_k) with L random projection directions per phase. No training required, well-studied.\\n\\n**Theoretical analysis**: Two contributions:\\n(1) *Phase-specific concentration inequality (novel)*: Under a phase-specific contamination model where phase k has contamination rate ε_k ≤ ε, we prove that PW₂-based phase scoring achieves false-positive rate O(exp(-n·Δ²_k/K)) per phase, where Δ_k is the Wasserstein separation between clean and contaminated distributions in phase k, and n is the number of samples per phase. When noise is phase-localized (ε_k > 0 for few phases, ε_k ≈ 0 for most), the overall FPR is O(K_bad · exp(-n·Δ²_min)) which is strictly lower than the global FPR of O(exp(-n·δ²)) where δ < Δ_min due to cross-phase dilution of the anomaly signal. This formalizes the intuition that phase decomposition amplifies anomaly detection power when contamination is localized. **Graceful degradation**: When contamination is uniformly distributed across all K phases (worst case for phase decomposition), PW₂ recovers the same detection power as global W₂ — the decomposition does not hurt, it simply does not help. This is because the per-phase Δ_k values are comparable and the summation reconstructs the global signal.\\n(2) *Inherited guarantees (application of existing theory)*: Robust Wasserstein barycenter consistency (Cheng & Liu 2026), cost-invariant breakdown point (Gonzalez-Sanz & Avella Medina 2026), instantiated for per-phase barycenters under the trajectory contamination model.\\n\\n**Evidence for the phase-localized contamination model**:\\n- SCIZOR's categorical failure taxonomy documents phase-localized failure types: 'Manipulation Failure' occurs during contact/grasp phases, 'Laggy Motion' during transport, 'Pause' during phase transitions, 'Stuck at Collision' during approach. These are not distributed uniformly across trajectories.\\n- RoboMimic's Tool Hang failure analysis identifies: Insertion Miss, Failed Insertion, Failed Tool Grasp, Tool Drop — each corresponding to a specific manipulation phase.\\n- Manipulation tasks have inherent phase structure: contact events (grasp, insertion, placement) involve higher control complexity and more failure modes than free-space motion (approach, retreat), making phase-localized contamination the common case rather than an edge case.\\n- When the model does not hold (e.g., operator fatigue causing distributed degradation), PhaseOT gracefully degrades to trajectory-level scoring quality (see theoretical analysis above).\\n\\n**Evaluation**: Fine-tune Diffusion Policy (primary — standard in RoboMimic/Push-T benchmarks) and ACT (secondary — for kitchen tasks) on filtered/weighted subsets.\\n\\n*Benchmarks (chosen for documented natural multimodality and phase-localized failure modes)*:\\n- RoboMimic MH (Lift, Can, Square, Transport): 300 demos from 6 operators in 3 quality tiers. Standard benchmark with proficiency-based diversity; Transport has highest measured entropy (FAKTUAL 2026).\\n- Push-T (Diffusion Policy benchmark): 206 human demos. Explicitly bimodal — left vs. right approach strategies documented by Chi et al. (RSS 2023). Make-or-break multimodal differentiation benchmark.\\n- Franka Kitchen (D4RL): ~600 demos with combinatorial multimodality (different orderings of 4+ subtask completions). Natural multimodality from operator choice.\\n- LIBERO-10: 50 demos/task. Standard benchmark for generalization.\\n\\n*Key experiments (designed to demonstrate unique capabilities vs. SCIZOR as primary baseline)*:\\n- (E1) Push-T bimodal preservation: Inject 20% noise demos into Push-T. Measure whether each method correctly retains both left and right approach strategies while removing noise. Report mode preservation rate and per-mode success rate. SCIZOR is the primary baseline: since it treats all demos uniformly, it should penalize minority strategies. PhaseOT should discover both modes and filter only noisy executions within each mode.\\n- (E2) Phase-diagnosis accuracy: On RoboMimic MH, inject controlled phase-localized noise (e.g., add perturbations only to grasp phases in 20% of demos). Measure precision/recall of phase-level anomaly detection: can PhaseOT correctly identify WHICH phase is corrupted? Compare against SCIZOR's transition-level flags (which should detect corrupted transitions but without phase-level semantic labeling) and DemInf (which cannot localize at all).\\n- (E3) Phase-level vs. transition-level recovery: Compare PhaseOT's phase-level importance weighting against SCIZOR's transition-level filtering for partial trajectory recovery. Measure downstream policy performance when using (a) PhaseOT phase-level weighting, (b) SCIZOR transition filtering, (c) trajectory-level hard filtering, (d) no filtering. Both PhaseOT and SCIZOR achieve partial recovery, but at different granularities — this experiment tests which granularity is more effective for policy learning.\\n- (E4) Franka Kitchen ordering preservation: Test whether methods preserve diverse subtask orderings vs. collapsing to majority ordering. Measure ordering diversity retention.\\n- (E5) Pipeline combination: PhaseOT soft weights → CUPID policy-dependent refinement. Test whether the combination outperforms either alone.\\n- (E6) Graceful degradation: Inject uniformly distributed noise (not phase-localized) and measure whether PhaseOT maintains parity with trajectory-level methods rather than degrading.\\n\\n*Baselines (8 methods, with SCIZOR as primary)*: SCIZOR (primary — transition-level with recovery), DemInf, S2I, RINSE, CUPID (policy-dependent upper bound) + unfiltered + random-subset + GlobalOT (PhaseOT without phase decomposition, key ablation to isolate the value of phase-level scoring).\\n\\n*Ablations*: (a) Segmentation method: heuristic keyframes vs. BOCPD vs. uniform time windows. (b) PW₂ vs. global W₂ (the critical ablation). (c) Soft vs. hard filtering vs. phase-level weighting. (d) Ground cost weight sensitivity. (e) Number of phases K. (f) Sinkhorn regularization ε. (g) PCA dimensionality. (h) k (number of modes) selection. (i) Phase importance weight learning vs. uniform.\\n\\n*Metrics*: Task success rate (primary), mode preservation rate (fraction of valid strategies retained), phase-level diagnosis precision/recall (correlation with known injected phase noise), data utilization rate (fraction of total timesteps used), sample efficiency curves, diagnostic profile interpretability (qualitative).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~1500h A100 (PW₂ pipeline + phase segmentation: ~120h; Diffusion Policy training for 8 baselines+ours+unfiltered × 4 benchmarks × 3 seeds: ~600h; ACT training for Kitchen: ~80h; evaluation rollouts: ~100h; multimodal experiments E1-E6: ~180h; ablations: ~220h; buffer for failed runs and debugging: ~200h)\",\n      \"gpu_utilization\": \"~55% — reflects realistic development overhead (debugging pipeline, inspecting phase segmentations between runs, analyzing diagnostic profiles, iterating on mode discovery parameters). This is development-phase utilization, not billing inefficiency; modern cloud billing is per-second, so utilization primarily affects timeline rather than cost.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers (1 lead with OT/robotics background; 1 optional for parallel benchmark setup)\",\n      \"estimated_gpu_cost\": \"$2,250 (1500h × $1.50/h A100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1300h A100 (agent handles PW₂ pipeline, hyperparameter sweeps, Diffusion Policy training orchestration; reduced idle time)\",\n      \"gpu_utilization\": \"~80%\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1 researcher, ~30-40min/day for reviewing phase segmentation quality, validating diagnostic profile interpretability, verifying mode discovery coherence, and approving experiment plans\",\n      \"claude_api_cost\": \"$200-400\",\n      \"estimated_gpu_cost\": \"$1,950 (1300h × $1.50/h)\",\n      \"risk_note\": \"Phase-specific concentration inequality proof requires careful mathematical reasoning; agent can draft proofs but human must verify. The proof does NOT depend on the adapted OT framework — it follows from standard Wasserstein concentration results applied per-phase.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2500h A100 (3x ablation sweep: full grid over segmentation methods × cost weights × k values × regularization × PCA dims × phase-constrained/global × soft/hard/phase-level; additional seeds for statistical significance)\",\n      \"gpu_utilization\": \"~90%\",\n      \"timeline\": \"3-5 weeks with 4+ concurrent A100 GPUs\",\n      \"team\": \"0 researchers (initial setup: dataset paths, GPU access, simulation environments for LIBERO/Kitchen rollouts)\",\n      \"claude_api_cost\": \"$400-800\",\n      \"estimated_gpu_cost\": \"$3,750 (2500h × $1.50/h)\",\n      \"speed_bottleneck\": \"GPU count — many Diffusion Policy runs can parallelize on single A100s; Kitchen/LIBERO simulation rollouts are CPU-bound\",\n      \"risk_note\": \"Theoretical derivations require human verification; agent may over-explore segmentation configurations\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (deadline expected ~late July 2026, based on AAAI 2026 pattern of abstract Jul 25, paper Aug 1 — realistic primary target, ~2.5 months from now; conference Feb 16-23, 2027 in Montréal)\",\n    \"ICLR 2027 (deadline expected ~September-October 2026 — comfortable timeline for thorough evaluation)\",\n    \"CoRL 2026 is INFEASIBLE for a full paper (abstract deadline May 26, paper deadline May 29 — 13/16 days from now). The user must accept that CoRL 2026 is not possible. A CoRL 2026 workshop paper (4-page, preliminary results on Push-T + RoboMimic Can) could be attempted if a relevant workshop accepts submissions, but workshop call-for-papers dates are not yet announced. Conference: Nov 9-12, 2026, Austin TX.\",\n    \"CoRL 2027 (deadline ~May 2027 — fallback if real-robot validation or additional large-scale benchmarks needed)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Robot Data Curation with Mutual Information Estimators — DemInf (RSS 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026) — primary comparison: transition-level filtering with 54%/31% recovery behavior maintenance, categorical diagnostic profiles, +32.9% on Sirius-Fleet\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions — QoQ (arXiv 2026)\",\n    \"Learning from the Best: Smoothness-Driven Metrics for Data Quality — RINSE (ICML 2025)\",\n    \"Select Segments to Imitate — S2I: Segment-Level Selection and Optimization (ICRA 2025, Chen et al.)\",\n    \"Aligning Human Intent from Imperfect Demonstrations with Confidence-based Inverse soft-Q Learning — CIQL (Bu et al., IEEE Robotics and Automation Letters, Vol. 9, Issue 8, pp. 7150-7157, August 2024)\",\n    \"Skill Disentanglement for Imitation Learning — SDIL (KDD 2023)\",\n    \"FIDeL: Failure Identification in Demonstration Learning via OT (arXiv 2025)\",\n    \"Demo-SCORE: Curating Demonstrations using Online Experience (RSS 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (arXiv 2025, UT Austin)\",\n    \"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2025, Hejna et al.)\",\n    \"Is Diversity All You Need for Scalable Robotic Manipulation? (Shi et al., arXiv Jul 2025) — spatial vs. velocity multimodality distinction\",\n    \"Diversity You Can Actually Measure — FAKTUAL (arXiv 2026) — signature-kernel entropy for demonstration diversity\",\n    \"Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation (Xu & Gould, CVPR 2024) — temporal consistency in OT formulations, related principle\",\n    \"On Combining Expert Demonstrations in Imitation Learning via Optimal Transport (Sebag et al., NeurIPS OT Workshop 2021 / arXiv 2023)\",\n    \"Optimal Transport for Offline Imitation Learning — OTR (ICLR 2023)\",\n    \"Robot Policy Learning with Temporal Optimal Transport Reward (NeurIPS 2024)\",\n    \"Cross-Domain Imitation Learning via Optimal Transport — GWIL (ICLR 2022)\",\n    \"Sliced-Wasserstein Distance-based Data Selection — SWAD (Pallage & Lesage-Landry, arXiv 2025)\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025) — Push-T benchmark\",\n    \"Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and RL (Gupta et al., CoRL 2019) — Franka Kitchen\",\n    \"Discriminator-Weighted Offline Imitation Learning — DWBC (Xu et al., ICML 2022)\",\n    \"Value-Aligned Behavior Cloning via Bi-level Optimization — VACO (ICLR 2025)\",\n    \"Causal Transport in Discrete Time and Applications (Backhoff-Veraguas et al., SIAM J. Optim. 2017) — foundational adapted OT; PhaseOT's PW₂ is inspired by but distinct from this framework\",\n    \"Adapted Wasserstein Distances and Stability in Mathematical Finance (Backhoff-Veraguas et al., Finance & Stochastics 2020)\",\n    \"Optimal Transport and Wasserstein Distances for Causal Models (Cheridito & Eckstein, Bernoulli 2025)\",\n    \"Bicausal Optimal Transport for Markov Chains via Dynamic Programming (Moulos, IEEE CDC 2021) — nested conditional optimization for Markov chains, distinct from PW₂'s additive phase decomposition\",\n    \"Dynamical Wasserstein Barycenters for Time-series Modeling (Cheng et al., NeurIPS 2021)\",\n    \"Nonparametric and Regularized Dynamical Wasserstein Barycenters for Sequential Observations (Cheng et al., IEEE TSP 2023)\",\n    \"Robust Wasserstein Barycenter (Cheng & Liu, arXiv 2026)\",\n    \"Outlier-Robust Optimal Transport: Duality, Structure, and Statistical Analysis (Nietert et al., AISTATS 2022)\",\n    \"Breakdown Properties of Optimal Transport Maps (Gonzalez-Sanz & Avella Medina, arXiv 2026)\",\n    \"Consistency Matters: Defining Demonstration Data Quality Metrics (Sakr et al., ACM THRI 2024)\",\n    \"Robomimic: A Framework for Robot Learning from Demonstration (Mandlekar et al., CoRL 2021) — Tool Hang failure analysis documents phase-specific failures\"\n  ],\n  \"description\": \"We propose PhaseOT, a policy-agnostic method for diagnosing demonstration quality at the task-phase granularity using a Phase-Structured Wasserstein Distance (PW₂) combined with mode-aware scoring. Unlike trajectory-level curation methods (DemInf, RINSE, CUPID) that produce a single quality score, and unlike transition-level methods (SCIZOR) that produce per-step anomaly flags and categorical labels, PhaseOT generates structured diagnostic profiles at the semantic task-phase level — each phase receives a distributional quality score, enabling targeted feedback ('demo #47's grasp phase is 3.2σ anomalous within its strategy mode, approach and transport phases are nominal').\\n\\n**Key methodological contributions:**\\n(1) *Phase-Structured Wasserstein Distance (PW₂)*: PW₂(τ₁,τ₂) = Σ_k w_k · W₂²(μ_{τ₁,k}, μ_{τ₂,k}) restricts optimal transport couplings to respect phase alignment, so approach states can only match approach states, not grasp states. This is explicitly NOT the adapted/bicausal Wasserstein distance of Backhoff-Veraguas et al., which involves nested conditional optimization via dynamic programming. PW₂ is a simpler phase-constrained transport inspired by the adapted OT literature's emphasis on temporal causality but practically motivated by the discrete phase structure of manipulation tasks. The practical advantage: when noise is phase-localized (the common case in manipulation, as documented by SCIZOR's failure taxonomy and RoboMimic's Tool Hang analysis), PW₂ concentrates the anomaly signal in the affected phase rather than diluting it across the full trajectory.\\n\\n(2) *Mode-aware phase-level scoring*: Spectral clustering on the pairwise PW₂ distance matrix discovers valid strategy modes (e.g., left vs. right approach in Push-T, different subtask orderings in Kitchen). Quality scoring is performed within each mode using robust Wasserstein barycenters per phase, so minority strategies are not penalized as outliers. This is a capability no existing curation method provides — SCIZOR, DemInf, RINSE, and S2I all treat demonstrations uniformly without mode awareness.\\n\\n(3) *Phase-level importance weighting*: w_k(τ) = exp(-λ·q_k(τ)) preserves good phases of otherwise-flagged demos while downweighting anomalous phases coherently at the semantic phase level. This differs from SCIZOR's transition-level filtering (which removes individual state-action pairs) in operating at a meaningful semantic granularity — downweighting an entire grasp phase rather than scattered transitions maintains temporal coherence within phases.\\n\\n(4) *Phase-specific concentration inequality*: Under a phase-specific ε-contamination model, we prove that PW₂ achieves lower false-positive rates than global W₂ when contamination is phase-localized, with graceful degradation to trajectory-level performance when contamination is uniformly distributed. This does not derive from the adapted OT framework but from standard Wasserstein concentration results applied per-phase.\\n\\n**Differentiation from SCIZOR (ICRA 2026)**: SCIZOR achieves partial trajectory recovery (54% fully maintained, 31% partially maintained) via transition-level progress prediction with categorical diagnostic profiles. PhaseOT advances beyond SCIZOR in three specific dimensions: (a) semantic phase-level profiles vs. transition-level flags — a structured diagnostic report vs. a list of symptoms, (b) mode-aware scoring that preserves strategy diversity vs. uniform treatment of all demonstrations, (c) principled distributional distances with theoretical guarantees vs. heuristic progress signals. Experiment E3 directly compares phase-level vs. transition-level recovery quality for downstream policy learning.\\n\\n**Evidence for phase-localized contamination model**: SCIZOR's own categorical failure analysis (Manipulation Failure, Laggy Motion, Pause, Stuck at Collision) and RoboMimic's Tool Hang failures (Insertion Miss, Failed Insertion, Failed Tool Grasp, Tool Drop) document phase-specific failure modes. Manipulation tasks concentrate failures at contact events (grasp, insertion) more than free-space motion. When this assumption does not hold (e.g., distributed operator fatigue), PhaseOT gracefully degrades to within-mode trajectory-level scoring — the phase decomposition does not hurt, it simply does not help as much.\\n\\n**Evaluation**: Fine-tune Diffusion Policy (primary) and ACT on filtered/weighted subsets of RoboMimic MH (300 demos, 6 operators), Push-T (206 demos, bimodal), Franka Kitchen (~600 demos, combinatorial multimodality), LIBERO-10 (50 demos/task). SCIZOR is the primary baseline. Key experiments: (E1) bimodal strategy preservation in Push-T, (E2) phase-level diagnosis precision/recall with injected phase noise, (E3) phase-level vs. transition-level recovery comparison against SCIZOR, (E4) Kitchen ordering diversity retention, (E5) PhaseOT→CUPID pipeline combination, (E6) graceful degradation with uniform noise. Estimated compute: ~1500 A100-hours. Primary target: AAAI 2027 (deadline expected ~late July 2026). CoRL 2026 full paper is infeasible (deadline 13-16 days away).\",\n  \"project_name\": \"phase_ot_diag\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Generator missed 3 major competing works that must be cited and compared against: (1) CUPID (CoRL 2025) — influence functions for robot data curation with strong empirical results, (2) DataMIL (May 2025, UT Austin) — policy-driven data selection validated on 60+ tasks including Open X-Embodiment, (3) DemInf (RSS 2025) — mutual information estimators for demo quality, 5-10% improvement on RoboMimic. All three are published at top robotics venues and directly compete with the proposed approach.\", \"Computational scalability is not adequately addressed: pairwise W2 distances require O(N²) Sinkhorn solves, each O(T² log T) per trajectory pair; Wasserstein barycenters are NP-hard in general and suffer a curse of dimensionality (exponential in state-action-time dimensionality). For datasets with thousands of demonstrations and high-dimensional robot states, this could be prohibitively expensive.\", \"GPU cost estimates are significantly underestimated: OpenVLA-OFT fine-tuning alone requires 8 A100s for 1-2 days (~192-384 A100h per run). With 4+ baselines (SCIZOR, QoQ, RINSE, unfiltered) × 2 models (OpenVLA-OFT, SmolVLA) × 2 benchmarks (RoboMimic, LIBERO) × multiple ablations, realistic compute is likely 1500-2500 A100h, not 400h.\", \"The claim 'naturally distinguishes noise from valid strategic diversity without separate mode identification steps' is misleading — k-Wasserstein-barycenter clustering IS a mode identification/discovery step. The approach does require choosing k (number of strategy modes) and running a clustering algorithm, which is precisely 'separate mode identification.'\", \"The theoretical contribution (provable outlier detection bounds under epsilon-contamination) assembles existing results from Robust Wasserstein Barycenter theory (arXiv Mar 2026) and Outlier-Robust OT (Mukherjee et al. 2021, Nietert et al. 2022) rather than deriving fundamentally new theory. This should be positioned as a novel application of existing theory, not as a theoretical contribution per se.\", \"CoRL 2026 timeline (17 days to abstract, 20 days to paper) is unrealistic for a from-scratch project. The user's requirement specifically targets CoRL 2026, but the proposal's own venue list relegates it to a stretch goal. AAAI 2027 and ICLR 2027 are more realistic but the user explicitly asked for CoRL 2026.\", \"No discussion of how the ground cost metric in state-action-time space should be designed — this is a critical design choice that significantly affects OT distances and is non-trivial for heterogeneous robot observation/action spaces (joint angles, gripper states, visual features have very different scales and semantics).\"]\nFeedback: To bring this to CoRL-acceptable quality, the Generator should: (1) **Add all missing baselines**: CUPID, DataMIL, and DemInf must be included in the landscape and experimental comparisons — these are published at CoRL 2025 and RSS 2025 and will be known to reviewers. (2) **Address computational scaling**: Propose concrete solutions — e.g., approximate OT via Wasserstein Wormhole embeddings for O(N) amortized distance computation, sliced Wasserstein distances instead of full W2, or subsampling strategies. Provide explicit complexity analysis for realistic dataset sizes (e.g., RoboMimic has ~200-300 demos per task, LIBERO has ~50 demos per task — compute actual wall-clock estimates). (3) **Fix the cost estimate**: Recalculate GPU hours accounting for VLA fine-tuning across all baseline conditions. Realistic estimates should be 1500-2500h A100 for manual mode, not 400h. (4) **Reframe theoretical contribution honestly**: Position as 'novel application of robust OT theory to trajectory quality scoring' rather than implying new theory. (5) **Design the ground cost metric explicitly**: Propose how to handle heterogeneous state-action-time dimensions (normalization, learned embeddings, or task-specific cost functions). (6) **Drop the misleading 'no mode identification' claim**: The k-barycenter clustering IS mode identification; instead, emphasize the advantage is that mode identification and quality scoring are unified in one principled OT framework. (7) **For CoRL 2026 feasibility**: The user should assess whether they already have partial implementation/results; if starting from scratch, target AAAI 2027 instead and be upfront about this.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — CoRL 2026 venue mismatch: The user explicitly targets CoRL 2026 (abstract deadline May 26, 17 days away). The proposal honestly pivots to AAAI 2027 (~August 2026 deadline), but this directly contradicts the user's stated requirement. The user should be explicitly informed that CoRL 2026 is infeasible from scratch.\", \"Missing competing work — Demo-SCORE (RSS 2025, Chen et al.): Self-curation method using online rollout classifiers to filter heterogeneous demos, achieving 15-35% improvement. Policy-dependent but directly in the demo curation space and published at a top robotics venue. Must be cited and positioned against.\", \"Missing related work — Sebag et al. (arXiv 2307.10810, 2023): 'On Combining Expert Demonstrations via Optimal Transport' uses multi-marginal OT specifically to handle multimodal demonstration distributions. While it targets combination not quality scoring, it directly precedents OT-Consensus's use of OT for multimodal demo handling, reducing the novelty claim.\", \"Novelty pressure in extremely crowded field: With 8+ demo curation methods published in 2024-2026, reviewers at AAAI/ICLR will scrutinize what OT-Consensus adds beyond DemInf (also policy-agnostic, also uses information-theoretic scoring, 5-10% on RoboMimic). The multimodal handling advantage needs concrete empirical evidence, not just theoretical argument.\", \"Wasserstein Wormhole adaptation unvalidated: The Wormhole model (ICML 2024) was designed for point cloud distributions (single-cell biology), not state-action-time trajectory distributions with heterogeneous components (positions, rotations, gripper states). Training Wormhole on this novel domain may require significant adaptation and there's no guarantee the learned embeddings will preserve W2 structure for trajectory data.\", \"Theoretical contribution remains thin for top venues: Instantiating existing robust barycenter results (Le Gouic et al. 2026; Nietert et al. 2022) for trajectory noise models is honest but reviewers may view this as 'plugging in known results' rather than a theoretical contribution. Consider whether deriving tighter, trajectory-specific bounds (e.g., exploiting temporal structure) could strengthen this.\", \"Partial mismatch with user's RL-inspired direction: The user specifically mentioned borrowing RL ideas (experience replay buffer, using data itself to score actions). OT-Consensus uses distributional geometry rather than RL-inspired scoring. While the user acknowledged theoretical approaches are acceptable, the connection to the RL scoring intuition could be made more explicit.\", \"Missing Re-Mix (CoRL 2025) from landscape: Re-Mix optimizes data mixtures for large-scale IL via DRO, outperforming uniform weights by 38%. It operates at domain-level not trajectory-level, but is highly relevant as a data-centric approach to IL quality and should be cited.\"]\nFeedback: The proposal has improved substantially from Round 1 — cost estimates are realistic, the landscape is comprehensive, the theoretical contribution is honestly framed, and the ground cost metric is explicit. However, several issues prevent a pass:\n\n**Priority fixes:**\n\n1. **Address the CoRL 2026 impossibility directly**: State upfront that CoRL 2026 is infeasible from scratch. If the user has partial implementation or prior codebase, assess what can realistically be done in 17 days. Otherwise, confirm AAAI 2027 as the target and explain why.\n\n2. **Add Demo-SCORE, Sebag et al. 2023, and Re-Mix to the landscape**: Demo-SCORE (RSS 2025) is a direct competitor. Sebag et al. (2023) precedents OT for multimodal demos. Re-Mix (CoRL 2025) is a key data-centric IL work. All must be cited.\n\n3. **Strengthen the empirical differentiation story**: The biggest risk is 'why OT-Consensus over DemInf?' — both are policy-agnostic and evaluate on RoboMimic. Propose specific multimodal evaluation scenarios (e.g., tasks where demonstrations contain 2+ valid strategies like left-hand vs. right-hand grasps) where DemInf's global MI scoring would conflate valid diversity with noise, while OT-Consensus's mode-specific scoring would preserve it. This is the paper's strongest selling point and needs concrete experimental design.\n\n4. **Validate or scope Wasserstein Wormhole adaptation**: Acknowledge that applying Wormhole to trajectory distributions (heterogeneous state-action-time spaces) is a novel adaptation that may require architecture modifications. Consider sliced Wasserstein as a simpler, more reliable Tier 2 fallback and position Wormhole as optional.\n\n5. **Consider strengthening the theoretical contribution**: Instead of purely instantiating existing results, consider whether temporal structure in trajectories enables tighter outlier detection bounds (e.g., exploiting the Markov structure of sequential state-action pairs). Even a modest trajectory-specific result would elevate the theory from 'application' to 'contribution.'\n\n6. **Make the RL connection explicit**: Frame OT-based scoring as a principled formalization of the intuition behind experience replay prioritization — trajectories that are distributionally close to the consensus (barycenter) can be viewed as 'high-priority' experiences, while outliers are 'low-priority' ones to be downweighted. This connects to the user's original RL direction.\n\n**What's working well:** Comprehensive baseline comparison (6 methods), two-tier scaling, honest theoretical framing, explicit ground cost design, realistic cost estimates. The pre-filter pipeline idea (OT-Consensus → CUPID) is a compelling practical contribution that should be emphasized.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — User requirement mismatch (CoRL 2026): The user explicitly targets CoRL 2026 (abstract deadline May 25-26, paper deadline May 28, i.e., 12-15 days from now). The proposal honestly acknowledges CoRL is infeasible and pivots to AAAI 2027. While this is intellectually honest, it directly violates the user's stated requirement. The user must be informed clearly that this idea cannot target CoRL 2026 from scratch.\", \"Novelty under pressure from crowded field: With 8+ demo curation methods published at top venues in 2024-2026, the bar for novelty is extremely high. The core contribution — Wasserstein barycenter clustering for mode-aware quality scoring — is a competent application of existing OT theory, but reviewers will ask: (1) Why is OT better than DemInf's simpler MI-based scoring? (2) Sebag et al. 2023 already combined OT with multimodal demonstrations. (3) Pallage 2025 (arXiv 2504.12918) independently proposes sliced-Wasserstein for data selection/filtering, showing the OT-for-filtering idea is not uniquely novel. The temporally-adapted distance is the most differentiating element, but it's an application of Backhoff-Veraguas et al. 2020 theory, not new theory.\", \"Empirical differentiation vs. DemInf is the make-or-break: Both OT-Consensus and DemInf are policy-agnostic and target similar benchmarks (RoboMimic, LIBERO). DemInf achieves 5-10% on RoboMimic. If OT-Consensus achieves similar or marginal improvements, the OT machinery will be viewed as unnecessary complexity. The synthetic multimodal experiments (E1-E3) are well-designed but risk being dismissed as constructed to favor the method. Real-world tasks where multimodality naturally arises and DemInf fails would be far more convincing, but finding such tasks is itself a research challenge.\", \"RL-PER connection is superficial: The claimed connection between OT-consensus scoring and prioritized experience replay (Schaul et al. 2016) is a stretch. PER prioritizes by TD error (a model-dependent signal reflecting learning progress), while OT-Consensus scores by distributional distance to barycenter (a model-free geometric signal). These are fundamentally different: one measures what the model needs to learn, the other measures statistical typicality. Calling barycenter distance 'analogous to TD error' is misleading. This weakens the paper's connection to the user's RL-inspired direction.\", \"Theoretical contribution remains incremental: The 'inherited guarantees' (applying Cheng & Liu 2026, Nietert et al. 2022, Gonzalez-Sanz & Avella Medina 2026) are honest applications of existing results. The novel phase-specific contamination model is a genuine contribution but is narrow — it assumes a particular contamination structure (phase-localized noise) that may not hold in practice. Reviewers may ask: when does phase-localized noise actually occur in real robot datasets?\", \"Missing comparison against SCIZOR on Sirius-Fleet: SCIZOR achieves 15.4% average improvement and outperforms DemInf by 19.2% on Sirius-Fleet — this is the strongest baseline in the field. The proposal lists SCIZOR as a baseline but doesn't discuss whether OT-Consensus's theoretical advantages translate to beating SCIZOR's practical results on large-scale datasets.\", \"Lightspeed Geometric Dataset Distance (ICML 2025) miscited: The proposal cites this as 'ICLR 2025' but it was published at ICML 2025. Minor but damages credibility if not corrected.\", \"Cost estimate tension: The proposal budgets OpenVLA-OFT full fine-tuning at '4 runs × 250h = 1000h' but each run requires 8 A100s for 1-2 days = 192-384h per run. 4 runs × ~300h = ~1200h just for full fine-tuning, already exceeding the line item. Additionally, running 7 baselines on 2 benchmarks with 2 VLA models could easily require 20+ fine-tuning runs, pushing total compute well beyond 2000h.\"]\nFeedback: The proposal has improved substantially across three rounds — the landscape is now among the most comprehensive I've seen, the approach is precisely specified, and the theoretical framing is honest. However, several issues prevent a pass:\n\n**Priority 1 — Address the venue mismatch decisively**: The user asked for CoRL 2026 (12-15 days away). This idea cannot target CoRL 2026 from scratch. State this unambiguously and either (a) propose a drastically scoped-down version that could be submitted in 12 days (e.g., a workshop paper at CoRL with preliminary results on 1-2 tasks), or (b) confirm AAAI 2027 as the target and explain the timeline advantage.\n\n**Priority 2 — Sharpen the DemInf differentiation**: The paper lives or dies on whether it demonstrably outperforms DemInf on tasks where multimodality matters. Instead of only synthetic multimodal experiments, identify at least one naturally multimodal task in existing benchmarks where DemInf's global MI conflates strategy diversity with noise. RoboMimic Transport with multiple operators is promising — quantify the expected advantage concretely.\n\n**Priority 3 — Drop or de-emphasize the PER analogy**: The connection between barycenter distance and TD error is too thin to be a 'contribution.' Demote it to a paragraph in the discussion section rather than a key methodological contribution. Instead, if the user wants an RL connection, consider: OT-scores as importance weights in an offline IL objective (formalize this as weighted behavioral cloning with OT-derived weights, which has a cleaner theoretical connection to importance-weighted regression).\n\n**Priority 4 — Strengthen or reframe the theory**: The phase-specific contamination model is the most novel theoretical element. To make it a real contribution, prove tighter concentration inequalities for the adapted score under the Markov structure (not just the additive decomposition). Alternatively, if the math doesn't yield substantially tighter bounds, position the theory honestly as 'applying robust OT tools to trajectories yields useful guarantees' and lean harder on empirical contributions.\n\n**Priority 5 — Fix the cost estimate**: Recalculate OpenVLA-OFT full fine-tuning costs (8×A100, 1-2 days per run). Budget 2500-3000h A100 for manual mode to be safe, not 2000h.\n\n**Priority 6 — Fix the ICML/ICLR citation**: Lightspeed Geometric Dataset Distance is ICML 2025, not ICLR 2025.\n\n**What's working well**: The comprehensive landscape, honest positioning against each related work, the two-tier OT computation strategy, the pre-filter pipeline idea, and the explicit ground cost metric design. The multimodal differentiation experiments (E1-E3) are well-designed. The honest assessment of CoRL infeasibility shows research maturity.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL — CoRL 2026 venue mismatch persists: The user explicitly targets CoRL 2026 (abstract deadline May 26, 13 days away). The proposal correctly identifies CoRL as infeasible and pivots to AAAI 2027, which is intellectually honest but still violates the user's stated requirement. This has been flagged in all 3 previous reviews. The user must explicitly acknowledge and accept the venue change, or the idea needs to be scoped down to a 4-page CoRL workshop paper with preliminary results.\", \"SCIZOR overlap on partial trajectory recovery (NEW): SCIZOR (ICRA 2026) explicitly operates at the transition level (state-action pair level) and already achieves partial trajectory recovery — their paper states '54% of recovery behaviors are fully maintained, 31% partially maintained.' This directly overlaps with PhaseOT's claimed unique capability of 'preserving good phases of otherwise-flagged demonstrations.' The proposal lists SCIZOR as a baseline but does not acknowledge this overlap. PhaseOT must differentiate: (a) SCIZOR uses heuristic progress prediction, PhaseOT uses principled distributional distances; (b) SCIZOR filters individual transitions, PhaseOT produces semantically meaningful phase-level quality profiles; (c) PhaseOT has theoretical guarantees SCIZOR lacks. But the claim of unique partial recovery capability must be revised.\", \"Phase-localized contamination model assumption needs justification: The novel phase-specific concentration inequality assumes noise is phase-localized (ε_k > 0 for few k, ε_k ≈ 0 for most). When does this actually hold in real robot datasets? In practice, noisy demonstrations may exhibit distributed degradation (operator fatigue, teleoperation latency) rather than phase-localized failures (only the grasp fails). The proposal should provide evidence from existing datasets (e.g., RoboMimic MH proficiency levels) that phase-localized noise is common, or acknowledge this as a limitation with graceful degradation analysis.\", \"Empirical differentiation vs. SCIZOR is the new make-or-break: Previous reviews focused on differentiating from DemInf. Now that SCIZOR's transition-level capabilities are clear, PhaseOT must demonstrate clear advantages over SCIZOR on at least one dimension: (1) multimodal handling (SCIZOR doesn't discover modes), (2) diagnostic interpretability (SCIZOR doesn't produce phase-level quality profiles), or (3) theoretical guarantees translating to practical gains. Experiment E1 (Push-T bimodal preservation) is well-designed for this but needs to explicitly include SCIZOR as the primary baseline, not just DemInf.\", \"Adapted Wasserstein distance formulation is simplified in a potentially misleading way: The proposed AW₂(τ₁, τ₂) = Σ_k W₂²(μ_{τ₁,k}, μ_{τ₂,k}) is a phase-aligned additive decomposition, NOT the full adapted/bicausal Wasserstein distance of Backhoff-Veraguas et al. The adapted distance in the mathematical finance literature involves constraints on the filtration structure and conditional distributions, not simply an additive decomposition over time segments. The proposal should clarify that this is an 'adapted-inspired' decomposition motivated by the causal structure of trajectories, not a direct application of the full adapted OT framework. Over-claiming the connection to adapted OT theory could draw reviewer criticism.\", \"Missing CIQL reference verification: The proposal cites 'CIQL (2024): Confidence-based per-transition quality scoring via dynamics evaluation' but I could not find any paper matching this exact name/description. This reference should be verified or removed — a fabricated citation would be fatal at review.\", \"Cost estimate minor issue — GPU utilization in manual mode (55%) seems low: With 1500h at 55% utilization, actual billed time would be much higher. Modern cloud billing is per-second, so utilization mainly affects timeline, not cost. But the $2,250 estimate assumes 1500 effective GPU-hours at $1.50/h, which is reasonable if using spot instances.\"]\nFeedback: The proposal has improved dramatically across four rounds — the landscape is now among the most comprehensive in the demo curation field, the approach is precisely specified, and the experimental design targets unique capabilities. However, several issues prevent a pass:\n\n**Priority 1 — Acknowledge and differentiate from SCIZOR's transition-level capabilities**: SCIZOR already filters at the state-action pair level and achieves partial trajectory recovery. PhaseOT's differentiation should focus on: (a) semantically meaningful phase-level diagnosis (not individual transitions), (b) mode-aware scoring that handles multimodality, (c) theoretical guarantees for outlier detection, and (d) principled distributional distances vs. heuristic progress signals. Revise the 'unique capability' claims for partial recovery to acknowledge SCIZOR's prior work.\n\n**Priority 2 — Clarify the adapted OT formulation**: The additive phase decomposition AW₂ = Σ_k W₂² is inspired by but not identical to the full adapted/bicausal OT of Backhoff-Veraguas et al. Be precise: this is a 'temporally-constrained transport' that restricts transport plans to respect phase boundaries, motivated by the adapted OT literature. Don't over-claim the mathematical pedigree — reviewers familiar with adapted OT theory will notice.\n\n**Priority 3 — Justify the phase-localized contamination model**: Provide concrete evidence from existing datasets (e.g., analyze RoboMimic MH multi-operator data) showing that common failure modes ARE phase-localized. If the evidence is mixed, add a graceful degradation analysis: what happens to PhaseOT's guarantees when noise is distributed across phases?\n\n**Priority 4 — Verify CIQL reference**: I could not find this paper. If it doesn't exist, remove it. If it's under a different name, correct the citation.\n\n**Priority 5 — Address the venue mismatch**: The user asked for CoRL 2026. This idea targets AAAI 2027 at earliest. Either (a) propose a drastically scoped CoRL workshop paper (4 pages, Push-T + Can only, if workshop deadlines permit), or (b) explicitly inform the user that CoRL 2026 is impossible and get buy-in for AAAI 2027.\n\n**What's working well**: The Phase-OT framing is cleaner and more focused than previous OT-Consensus versions. The experimental design (especially E1 bimodal preservation and E3 phase-diagnosis validation) targets genuine unique capabilities. The two-tier computation strategy is practical. The theoretical contribution (phase-specific concentration) is the right kind of novelty for a top venue — non-trivial but not over-claiming. The honest assessment of venue feasibility shows research maturity.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T10:45:25.331Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T10:45:25.331Z",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-13T10:45:25.366Z_

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

## Idea under review (round 5/10)
{
  "title": "PhaseOT: Mode-Aware Phase-Level Demonstration Quality Diagnosis via Structured Optimal Transport",
  "core_problem": "How to diagnose demonstration quality at the task-phase granularity — identifying not just which demonstrations are noisy, but which specific phases (approach, grasp, transport, placement) are anomalous — in a mode-aware, unsupervised manner that uses principled distributional distances, preserves valid strategy diversity across multiple solution modes, and provides interpretable diagnostic profiles rather than opaque scalar scores or unstructured per-transition flags?",
  "opportunity": "The demonstration curation field has matured rapidly (2024–2026), with methods now spanning dataset-level (Re-Mix), trajectory-level (DemInf, CUPID, QoQ, RINSE, Demo-SCORE), and transition-level (SCIZOR, CIQL) granularities. SCIZOR (ICRA 2026) represents the current frontier, operating at the state-action pair level and achieving partial trajectory recovery (54% of recovery behaviors fully maintained, 31% partially maintained) with categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision, etc.).\n\nHowever, a critical capability gap remains at the intersection of three dimensions that no existing method addresses simultaneously:\n\n(1) **Semantic phase-level diagnosis vs. raw transition scores**: SCIZOR produces per-transition anomaly flags and categorical labels, but these are individual symptom detections — analogous to listing elevated lab values. PhaseOT produces structured diagnostic profiles at the semantic task-phase level — analogous to a medical report that says 'grasp phase is anomalous (3.2σ from mode centroid), approach and transport phases are nominal.' This phase-level granularity is the right abstraction for actionable feedback: it maps directly to interpretable task stages, enables targeted re-demonstration of specific phases, and supports phase-level importance weighting for policy training.\n\n(2) **Mode-aware scoring that preserves strategy diversity**: No existing curation method discovers or accounts for multiple valid demonstration strategies. DemInf's global mutual information conflates minority strategies with noise. SCIZOR treats all demonstrations uniformly via progress prediction. RINSE assumes smoothness universally correlates with quality. Shi et al. (2025) showed that 'spatial multimodality' (different trajectory paths) benefits policy learning while 'velocity multimodality' (same path at different speeds) is harmful, yielding 15% improvement from velocity debiasing alone — but no curation method exploits this distinction. PhaseOT's mode discovery via phase-structured distances naturally separates beneficial strategic diversity from harmful execution noise.\n\n(3) **Principled distributional distances with theoretical guarantees**: Existing phase/transition-level methods rely on heuristic quality signals — SCIZOR uses progress prediction, S2I uses supervised contrastive learning with expert references, CIQL uses dynamics-based confidence scoring. PhaseOT uses Wasserstein distances within aligned phase segments, providing concentration inequalities for anomaly detection that formalize when and why phase decomposition improves detection power over trajectory-level scoring.\n\nThe phase-localized noise model underlying PhaseOT is well-supported empirically. SCIZOR's own categorical failure taxonomy shows that failure types are inherently phase-localized: 'Manipulation Failure' occurs during contact phases, 'Laggy Motion' during transport, 'Pause' during transitions. RoboMimic's Tool Hang failure analysis similarly documents phase-specific failures: Insertion Miss, Failed Insertion, Failed Tool Grasp, Tool Drop — each mapping to a specific manipulation phase. Manipulation tasks have inherent phase structure where failures concentrate at contact events (grasp, insertion) more than during free-space motion (approach, retreat).\n\nThe mathematical apparatus for PhaseOT draws inspiration from the adapted optimal transport literature (Backhoff-Veraguas et al. 2020, Cheridito & Eckstein 2025), which emphasizes respecting temporal causality in distributional comparison of stochastic processes. However, PhaseOT employs a simpler, practically motivated phase-constrained transport formulation rather than the full adapted/bicausal framework, which involves nested conditional optimization unsuited to the discrete phase-segmented structure of manipulation demonstrations. Concurrently, Xu & Gould (CVPR 2024) demonstrated the value of encoding temporal consistency into optimal transport for action segmentation, validating the broader principle.",
  "landscape": "The demonstration curation field has consolidated around methods at multiple granularity levels:\n\n**Trajectory-level, policy-dependent methods** (require training or evaluating a policy):\n- CUPID (CoRL 2025): Influence functions on expected return from closed-loop rollouts. SOTA with <33% curated data on RoboMimic. +38% on real Franka tasks. Limitation: requires evaluation rollouts, architecture-specific.\n- QoQ (arXiv Mar 2026): Maximum influence scoring with trajectory-wise aggregation. 99.2% on RoboMimic Can. Limitation: requires validation set of known-good demos.\n- DataMIL (May 2025): Datamodels for end-to-end policy-driven selection. 10% on MetaWorld 50 tasks. Limitation: requires multiple policy retrainings.\n- Demo-SCORE (RSS 2025): Self-curation via online rollout classifiers. 15-35% on real-world ALOHA tasks. Limitation: policy-dependent, requires rollouts.\n\n**Trajectory-level, policy-agnostic methods** (no policy training needed):\n- DemInf (RSS 2025): k-NN mutual information estimators on VAE embeddings. 5-10% on RoboMimic. Key limitation: global MI conflates valid strategy diversity with noise — in bimodal tasks (Push-T), demos from the minority strategy may receive low MI scores despite being high-quality executions of an alternative approach.\n- RINSE (ICML 2025): Spectral Arc Length + Trajectory-Envelope Distance smoothness metrics. 16-20% on RoboMimic. Limitation: assumes smoothness universally correlates with quality.\n- FAKTUAL (arXiv 2026): Signature-kernel entropy for diversity-aware curation. Shows RoboMimic Transport has highest demonstration diversity.\n\n**Transition/segment-level methods** (finer than trajectory):\n- SCIZOR (ICRA 2026): Self-supervised progress prediction + visual-action deduplication for transition-level filtering. +32.9% on Sirius-Fleet, +5.4% on RoboMimic, outperforms DemInf by 19.2% on Sirius-Fleet. Achieves partial trajectory recovery: 54% of recovery behaviors fully maintained, 31% partially maintained. Produces categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision, Move Back and Forth). **Strongest practical baseline and primary comparison point for PhaseOT.** Limitations: (a) heuristic progress signal without distributional guarantees, (b) no mode discovery — treats all demonstrations uniformly, which penalizes valid minority strategies, (c) transition-level flags lack semantic phase-level interpretability.\n- S2I (ICRA 2025): Heuristic keyframe segmentation → supervised contrastive learning → kNN distance-weighted voting for segment quality classification. +22.2% on Square with Diffusion Policy. Requires 3 expert reference demos per task (supervised), uses learned embeddings not distributional distances.\n- CIQL (Bu et al., IEEE RA-L 2024): Confidence-based Inverse soft-Q Learning for per-transition confidence scoring via dynamics evaluation. Aligns human intent from imperfect demonstrations. Limitation: confidence scores are dynamics-based heuristics, not distributional distances; no mode awareness or phase-level profiles.\n- SDIL (KDD 2023): Skill disentanglement via latent variables + PU learning for per-skill optimality estimation.\n- FIDeL (2025): OT-based per-timestep anomaly scoring using Sinkhorn distances — but for execution monitoring during deployment, not dataset curation.\n\n**Demonstration diversity analysis**:\n- Shi et al. (arXiv Jul 2025): Critical distinction between spatial multimodality (different trajectory paths — beneficial, should be preserved) and velocity multimodality (different speeds on same path — harmful, should be filtered). Velocity debiasing yields 15% improvement = 2.5x more data equivalent. Directly motivates mode-aware quality assessment.\n\n**Data mixture optimization** (domain-level, complementary):\n- Re-Mix (CoRL 2025): DRO-based mixture weight optimization. 38% over uniform on Open X-Embodiment.\n\n**Importance-weighted imitation learning** (how to USE quality scores):\n- DWBC (ICML 2022): Discriminator-weighted offline IL — quality scores as per-sample BC weights.\n- VACO (ICLR 2025): Value-aligned BC via bi-level optimization meta-scoring.\n- RINSE exponential weighting: w(τ) = exp(-λ·q(τ)) shows Spearman ρ ≥ 0.89 with learned Re-Mix allocations.\n\n**OT in imitation learning** (applied to combination/reward/imitation, never phase-level quality diagnosis):\n- Xu & Gould (CVPR 2024): Temporally Consistent Unbalanced OT for unsupervised action segmentation — encodes temporal consistency into Gromov-Wasserstein. Validates temporal-OT principle but targets video segmentation, not quality diagnosis.\n- OTR (ICLR 2023), TemporalOT (NeurIPS 2024): OT for reward labeling.\n- GWIL (ICLR 2022): Gromov-Wasserstein for cross-domain imitation.\n- Pallage 2025 (arXiv 2504.12918): Sliced-Wasserstein for point-level outlier detection — static point clouds, no temporal structure.\n\n**Adapted Wasserstein distances** (theoretical inspiration — unexplored in robotics):\n- Backhoff-Veraguas et al. (2017, 2020): Causal/bicausal OT for stochastic processes via dynamic programming with nested conditional optimization. PhaseOT's PW₂ is inspired by this work's emphasis on temporal causality but uses a simpler additive phase-constrained decomposition.\n- Cheridito & Eckstein (Bernoulli 2025): Adapted distances for causal models.\n- Moulos (IEEE CDC 2021): Bicausal OT for Markov chains via value iteration.\n- These methods involve nested conditional optimization that respects filtration structure — fundamentally different from PhaseOT's additive phase decomposition, which is practically motivated rather than theoretically derived from the adapted OT framework.\n\n**Gap**: No method provides (1) unsupervised mode-aware scoring that preserves strategy diversity, (2) semantic phase-level quality profiles rather than trajectory-level scalars or unstructured transition-level flags, (3) principled distributional distances with theoretical guarantees for phase-localized anomaly detection. PhaseOT fills this three-dimensional gap.",
  "approach": "**Overview**: PhaseOT is a four-stage pipeline: (1) segment trajectories into semantically meaningful task phases, (2) compute a Phase-Structured Wasserstein Distance (PW₂) that restricts transport to respect phase alignment, (3) discover strategy modes and score quality within each mode using phase-level distributional profiles, (4) produce structured diagnostic profiles for downstream filtering, weighting, or re-demonstration guidance.\n\n**Stage 1 — Phase Segmentation**: Each demonstration τ of length T is segmented into K phases {P₁, ..., P_K} using one of two methods (compared as an ablation):\n- *Heuristic keyframes*: Phase boundaries at gripper state changes (open↔close) and velocity near-zero events, following S2I's approach. Simple, interpretable, works for manipulation tasks with clear grasp/release events.\n- *Bayesian Online Changepoint Detection (BOCPD)*: Statistical changepoint detection on the joint state-action stream, automatically discovering phase boundaries without gripper-state assumptions. More general, applicable to locomotion or contact-rich tasks without discrete gripper events.\nPhase boundaries are aligned across all demonstrations in a dataset using dynamic time warping on phase-discriminative features, ensuring comparable phases across demos. The number of phases K is validated against task semantics (typical manipulation: K=3–5 for approach/grasp/transport/place/retreat).\n\n**Stage 2 — Phase-Structured Wasserstein Distance (PW₂)**: Each phase P_k of a demonstration τ is represented as a discrete probability measure μ_{τ,k} = (1/|P_k|) Σ_{t∈P_k} δ_{(s_t, a_t)} over state-action tuples within that phase. The Phase-Structured Wasserstein-2 distance between two demonstrations τ₁, τ₂ is:\n\n  PW²₂(τ₁, τ₂) = Σ_{k=1}^{K} w_k · W²₂(μ_{τ₁,k}, μ_{τ₂,k})\n\nwhere W²₂ is the standard Wasserstein-2 distance computed within each phase, and w_k are phase importance weights (uniform by default, with learned variants as ablation).\n\n**Clarification on relationship to adapted OT**: PW₂ is NOT the adapted/bicausal Wasserstein distance of Backhoff-Veraguas et al. (2017, 2020) or Moulos (2021). The adapted distance involves nested conditional optimization via dynamic programming, where the coupling at time t depends on the realized marginals at times 1..t-1 through the filtration structure. PW₂ is a simpler construction: it restricts admissible transport plans so that mass within phase k of one trajectory can only be transported to phase k of another, then sums the within-phase costs. This phase-constrained restriction is inspired by the adapted OT literature's emphasis on respecting temporal causality — approach states should match approach states, not grasp states — but avoids the computational complexity of nested conditional optimization, which is unnecessary for the discrete phase-segmented structure of manipulation demonstrations. The practical advantage of PW₂ over unconstrained (global) W₂ is that it concentrates anomaly signal in the phase where contamination occurs, rather than diluting it across the entire trajectory.\n\nThe within-phase ground cost is:\n  c((s₁,a₁), (s₂,a₂)) = w_pos·‖ψ(pos₁)-ψ(pos₂)‖² + w_rot·d_rot(rot₁,rot₂)² + w_grip·(g₁-g₂)² + w_act·‖ψ(a₁)-ψ(a₂)‖²\nwhere ψ denotes z-score normalization per dimension, d_rot is geodesic distance for orientations, and weights {w_*} are set equal after normalization (with sensitivity analysis as ablation). For high-dimensional observation spaces, PCA reduces to 16-32D before cost computation.\n\n**Theoretical property**: PW₂ lower-bounds the global W₂ distance because the phase-alignment constraint restricts the set of admissible transport plans. When contamination is localized to a subset S ⊆ {1,...,K} of phases with |S| << K, the phase-level scores concentrate the anomaly signal in those phases. Specifically, if phase k has contamination rate ε_k, the within-phase score q_k grows with ε_k while clean phases contribute near-zero q_k, yielding a phase-specific detection threshold that is tighter than the global threshold by a factor related to K/|S|.\n\n**Stage 3 — Mode Discovery and Phase-Level Scoring**:\n- Compute pairwise PW₂ distance matrix over all demonstrations.\n- Perform spectral clustering on the PW₂ affinity matrix (k selected via eigengap heuristic or silhouette analysis) to discover valid strategy modes. Mode discovery is a preprocessing step, not a claimed contribution — we use standard clustering.\n- Within each mode m, compute the phase-level reference distribution b_{m,k} for each phase k as the Wasserstein barycenter of that phase across mode members, using the iterative reweighting scheme of Cheng & Liu (arXiv 2026) for robustness to remaining outliers.\n- Score each demonstration τ in mode m with a phase-level quality profile:\n  q(τ) = (q₁(τ), ..., q_K(τ))  where  q_k(τ) = W₂(μ_{τ,k}, b_{m,k})\n- Phase-level z-scores: z_k(τ) = (q_k(τ) - μ_{m,k}) / σ_{m,k} where μ_{m,k} and σ_{m,k} are the mean and std of q_k within mode m.\n- The trajectory-level score is the weighted sum: Q(τ) = Σ_k w_k · q_k(τ).\n\n**Stage 4 — Diagnostic Profile and Downstream Use** (three usage modes compared experimentally):\n- *Hard filtering*: Remove demos with Q(τ) exceeding an adaptive threshold (median + 2·MAD of intra-mode scores). Comparable to DemInf/SCIZOR.\n- *Soft importance weighting*: Use PW₂-derived scores as sample weights in behavioral cloning: L = Σ_τ Σ_{(s,a)∈τ} w(τ) · ℓ(π(s), a) where w(τ) = exp(-λ · Q(τ)). Connects to DWBC (ICML 2022) and VACO (ICLR 2025).\n- *Phase-level importance weighting (key differentiator)*: L = Σ_τ Σ_k Σ_{(s,a)∈P_k(τ)} w_k(τ) · ℓ(π(s), a) where w_k(τ) = exp(-λ · q_k(τ)). This preserves good phases of otherwise-flagged demos — if a demo's grasp phase is anomalous but its approach is clean, the approach segments still contribute with full weight. Unlike SCIZOR's transition-level filtering which removes individual state-action pairs based on progress prediction, PhaseOT's phase-level weighting operates at semantic granularity: it downweights the entire grasp phase coherently rather than removing scattered transitions, maintaining temporal coherence within phases.\n- *Diagnostic report*: For each flagged demonstration, output a structured profile: mode assignment, per-phase z-scores, phase-level failure classification (mapping high-z-score phases to failure categories via their distributional signatures), and recommended action (re-demonstrate phase k, discard entirely, or retain with reduced weight).\n\n**Scalable computation (two-tier)**:\n- Tier 1 — Exact Sinkhorn (datasets ≤500 demos): For each phase pair, entropy-regularized OT via POT/geomloss. RoboMimic 300 demos × K≈4 phases: 300²/2 × 4 = 180K Sinkhorn solves × ~2ms each (smaller per-phase problems) ≈ 6 minutes on GPU.\n- Tier 2 — Sliced Wasserstein (datasets >500 demos): O(N²·K·L·T_k log T_k) with L random projection directions per phase. No training required, well-studied.\n\n**Theoretical analysis**: Two contributions:\n(1) *Phase-specific concentration inequality (novel)*: Under a phase-specific contamination model where phase k has contamination rate ε_k ≤ ε, we prove that PW₂-based phase scoring achieves false-positive rate O(exp(-n·Δ²_k/K)) per phase, where Δ_k is the Wasserstein separation between clean and contaminated distributions in phase k, and n is the number of samples per phase. When noise is phase-localized (ε_k > 0 for few phases, ε_k ≈ 0 for most), the overall FPR is O(K_bad · exp(-n·Δ²_min)) which is strictly lower than the global FPR of O(exp(-n·δ²)) where δ < Δ_min due to cross-phase dilution of the anomaly signal. This formalizes the intuition that phase decomposition amplifies anomaly detection power when contamination is localized. **Graceful degradation**: When contamination is uniformly distributed across all K phases (worst case for phase decomposition), PW₂ recovers the same detection power as global W₂ — the decomposition does not hurt, it simply does not help. This is because the per-phase Δ_k values are comparable and the summation reconstructs the global signal.\n(2) *Inherited guarantees (application of existing theory)*: Robust Wasserstein barycenter consistency (Cheng & Liu 2026), cost-invariant breakdown point (Gonzalez-Sanz & Avella Medina 2026), instantiated for per-phase barycenters under the trajectory contamination model.\n\n**Evidence for the phase-localized contamination model**:\n- SCIZOR's categorical failure taxonomy documents phase-localized failure types: 'Manipulation Failure' occurs during contact/grasp phases, 'Laggy Motion' during transport, 'Pause' during phase transitions, 'Stuck at Collision' during approach. These are not distributed uniformly across trajectories.\n- RoboMimic's Tool Hang failure analysis identifies: Insertion Miss, Failed Insertion, Failed Tool Grasp, Tool Drop — each corresponding to a specific manipulation phase.\n- Manipulation tasks have inherent phase structure: contact events (grasp, insertion, placement) involve higher control complexity and more failure modes than free-space motion (approach, retreat), making phase-localized contamination the common case rather than an edge case.\n- When the model does not hold (e.g., operator fatigue causing distributed degradation), PhaseOT gracefully degrades to trajectory-level scoring quality (see theoretical analysis above).\n\n**Evaluation**: Fine-tune Diffusion Policy (primary — standard in RoboMimic/Push-T benchmarks) and ACT (secondary — for kitchen tasks) on filtered/weighted subsets.\n\n*Benchmarks (chosen for documented natural multimodality and phase-localized failure modes)*:\n- RoboMimic MH (Lift, Can, Square, Transport): 300 demos from 6 operators in 3 quality tiers. Standard benchmark with proficiency-based diversity; Transport has highest measured entropy (FAKTUAL 2026).\n- Push-T (Diffusion Policy benchmark): 206 human demos. Explicitly bimodal — left vs. right approach strategies documented by Chi et al. (RSS 2023). Make-or-break multimodal differentiation benchmark.\n- Franka Kitchen (D4RL): ~600 demos with combinatorial multimodality (different orderings of 4+ subtask completions). Natural multimodality from operator choice.\n- LIBERO-10: 50 demos/task. Standard benchmark for generalization.\n\n*Key experiments (designed to demonstrate unique capabilities vs. SCIZOR as primary baseline)*:\n- (E1) Push-T bimodal preservation: Inject 20% noise demos into Push-T. Measure whether each method correctly retains both left and right approach strategies while removing noise. Report mode preservation rate and per-mode success rate. SCIZOR is the primary baseline: since it treats all demos uniformly, it should penalize minority strategies. PhaseOT should discover both modes and filter only noisy executions within each mode.\n- (E2) Phase-diagnosis accuracy: On RoboMimic MH, inject controlled phase-localized noise (e.g., add perturbations only to grasp phases in 20% of demos). Measure precision/recall of phase-level anomaly detection: can PhaseOT correctly identify WHICH phase is corrupted? Compare against SCIZOR's transition-level flags (which should detect corrupted transitions but without phase-level semantic labeling) and DemInf (which cannot localize at all).\n- (E3) Phase-level vs. transition-level recovery: Compare PhaseOT's phase-level importance weighting against SCIZOR's transition-level filtering for partial trajectory recovery. Measure downstream policy performance when using (a) PhaseOT phase-level weighting, (b) SCIZOR transition filtering, (c) trajectory-level hard filtering, (d) no filtering. Both PhaseOT and SCIZOR achieve partial recovery, but at different granularities — this experiment tests which granularity is more effective for policy learning.\n- (E4) Franka Kitchen ordering preservation: Test whether methods preserve diverse subtask orderings vs. collapsing to majority ordering. Measure ordering diversity retention.\n- (E5) Pipeline combination: PhaseOT soft weights → CUPID policy-dependent refinement. Test whether the combination outperforms either alone.\n- (E6) Graceful degradation: Inject uniformly distributed noise (not phase-localized) and measure whether PhaseOT maintains parity with trajectory-level methods rather than degrading.\n\n*Baselines (8 methods, with SCIZOR as primary)*: SCIZOR (primary — transition-level with recovery), DemInf, S2I, RINSE, CUPID (policy-dependent upper bound) + unfiltered + random-subset + GlobalOT (PhaseOT without phase decomposition, key ablation to isolate the value of phase-level scoring).\n\n*Ablations*: (a) Segmentation method: heuristic keyframes vs. BOCPD vs. uniform time windows. (b) PW₂ vs. global W₂ (the critical ablation). (c) Soft vs. hard filtering vs. phase-level weighting. (d) Ground cost weight sensitivity. (e) Number of phases K. (f) Sinkhorn regularization ε. (g) PCA dimensionality. (h) k (number of modes) selection. (i) Phase importance weight learning vs. uniform.\n\n*Metrics*: Task success rate (primary), mode preservation rate (fraction of valid strategies retained), phase-level diagnosis precision/recall (correlation with known injected phase noise), data utilization rate (fraction of total timesteps used), sample efficiency curves, diagnostic profile interpretability (qualitative).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~1500h A100 (PW₂ pipeline + phase segmentation: ~120h; Diffusion Policy training for 8 baselines+ours+unfiltered × 4 benchmarks × 3 seeds: ~600h; ACT training for Kitchen: ~80h; evaluation rollouts: ~100h; multimodal experiments E1-E6: ~180h; ablations: ~220h; buffer for failed runs and debugging: ~200h)",
      "gpu_utilization": "~55% — reflects realistic development overhead (debugging pipeline, inspecting phase segmentations between runs, analyzing diagnostic profiles, iterating on mode discovery parameters). This is development-phase utilization, not billing inefficiency; modern cloud billing is per-second, so utilization primarily affects timeline rather than cost.",
      "timeline": "3-4 months",
      "team": "1-2 researchers (1 lead with OT/robotics background; 1 optional for parallel benchmark setup)",
      "estimated_gpu_cost": "$2,250 (1500h × $1.50/h A100)"
    },
    "human_in_loop": {
      "gpu_hours": "~1300h A100 (agent handles PW₂ pipeline, hyperparameter sweeps, Diffusion Policy training orchestration; reduced idle time)",
      "gpu_utilization": "~80%",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~30-40min/day for reviewing phase segmentation quality, validating diagnostic profile interpretability, verifying mode discovery coherence, and approving experiment plans",
      "claude_api_cost": "$200-400",
      "estimated_gpu_cost": "$1,950 (1300h × $1.50/h)",
      "risk_note": "Phase-specific concentration inequality proof requires careful mathematical reasoning; agent can draft proofs but human must verify. The proof does NOT depend on the adapted OT framework — it follows from standard Wasserstein concentration results applied per-phase."
    },
    "auto_research": {
      "gpu_hours": "~2500h A100 (3x ablation sweep: full grid over segmentation methods × cost weights × k values × regularization × PCA dims × phase-constrained/global × soft/hard/phase-level; additional seeds for statistical significance)",
      "gpu_utilization": "~90%",
      "timeline": "3-5 weeks with 4+ concurrent A100 GPUs",
      "team": "0 researchers (initial setup: dataset paths, GPU access, simulation environments for LIBERO/Kitchen rollouts)",
      "claude_api_cost": "$400-800",
      "estimated_gpu_cost": "$3,750 (2500h × $1.50/h)",
      "speed_bottleneck": "GPU count — many Diffusion Policy runs can parallelize on single A100s; Kitchen/LIBERO simulation rollouts are CPU-bound",
      "risk_note": "Theoretical derivations require human verification; agent may over-explore segmentation configurations"
    }
  },
  "target_venues": [
    "AAAI 2027 (deadline expected ~late July 2026, based on AAAI 2026 pattern of abstract Jul 25, paper Aug 1 — realistic primary target, ~2.5 months from now; conference Feb 16-23, 2027 in Montréal)",
    "ICLR 2027 (deadline expected ~September-October 2026 — comfortable timeline for thorough evaluation)",
    "CoRL 2026 is INFEASIBLE for a full paper (abstract deadline May 26, paper deadline May 29 — 13/16 days from now). The user must accept that CoRL 2026 is not possible. A CoRL 2026 workshop paper (4-page, preliminary results on Push-T + RoboMimic Can) could be attempted if a relevant workshop accepts submissions, but workshop call-for-papers dates are not yet announced. Conference: Nov 9-12, 2026, Austin TX.",
    "CoRL 2027 (deadline ~May 2027 — fallback if real-robot validation or additional large-scale benchmarks needed)"
  ],
  "level": "top-tier",
  "key_references": [
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "Robot Data Curation with Mutual Information Estimators — DemInf (RSS 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026) — primary comparison: transition-level filtering with 54%/31% recovery behavior maintenance, categorical diagnostic profiles, +32.9% on Sirius-Fleet",
    "Quality over Quantity: Demonstration Curation via Influence Functions — QoQ (arXiv 2026)",
    "Learning from the Best: Smoothness-Driven Metrics for Data Quality — RINSE (ICML 2025)",
    "Select Segments to Imitate — S2I: Segment-Level Selection and Optimization (ICRA 2025, Chen et al.)",
    "Aligning Human Intent from Imperfect Demonstrations with Confidence-based Inverse soft-Q Learning — CIQL (Bu et al., IEEE Robotics and Automation Letters, Vol. 9, Issue 8, pp. 7150-7157, August 2024)",
    "Skill Disentanglement for Imitation Learning — SDIL (KDD 2023)",
    "FIDeL: Failure Identification in Demonstration Learning via OT (arXiv 2025)",
    "Demo-SCORE: Curating Demonstrations using Online Experience (RSS 2025)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (arXiv 2025, UT Austin)",
    "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2025, Hejna et al.)",
    "Is Diversity All You Need for Scalable Robotic Manipulation? (Shi et al., arXiv Jul 2025) — spatial vs. velocity multimodality distinction",
    "Diversity You Can Actually Measure — FAKTUAL (arXiv 2026) — signature-kernel entropy for demonstration diversity",
    "Temporally Consistent Unbalanced Optimal Transport for Unsupervised Action Segmentation (Xu & Gould, CVPR 2024) — temporal consistency in OT formulations, related principle",
    "On Combining Expert Demonstrations in Imitation Learning via Optimal Transport (Sebag et al., NeurIPS OT Workshop 2021 / arXiv 2023)",
    "Optimal Transport for Offline Imitation Learning — OTR (ICLR 2023)",
    "Robot Policy Learning with Temporal Optimal Transport Reward (NeurIPS 2024)",
    "Cross-Domain Imitation Learning via Optimal Transport — GWIL (ICLR 2022)",
    "Sliced-Wasserstein Distance-based Data Selection — SWAD (Pallage & Lesage-Landry, arXiv 2025)",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025) — Push-T benchmark",
    "Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and RL (Gupta et al., CoRL 2019) — Franka Kitchen",
    "Discriminator-Weighted Offline Imitation Learning — DWBC (Xu et al., ICML 2022)",
    "Value-Aligned Behavior Cloning via Bi-level Optimization — VACO (ICLR 2025)",
    "Causal Transport in Discrete Time and Applications (Backhoff-Veraguas et al., SIAM J. Optim. 2017) — foundational adapted OT; PhaseOT's PW₂ is inspired by but distinct from this framework",
    "Adapted Wasserstein Distances and Stability in Mathematical Finance (Backhoff-Veraguas et al., Finance & Stochastics 2020)",
    "Optimal Transport and Wasserstein Distances for Causal Models (Cheridito & Eckstein, Bernoulli 2025)",
    "Bicausal Optimal Transport for Markov Chains via Dynamic Programming (Moulos, IEEE CDC 2021) — nested conditional optimization for Markov chains, distinct from PW₂'s additive phase decomposition",
    "Dynamical Wasserstein Barycenters for Time-series Modeling (Cheng et al., NeurIPS 2021)",
    "Nonparametric and Regularized Dynamical Wasserstein Barycenters for Sequential Observations (Cheng et al., IEEE TSP 2023)",
    "Robust Wasserstein Barycenter (Cheng & Liu, arXiv 2026)",
    "Outlier-Robust Optimal Transport: Duality, Structure, and Statistical Analysis (Nietert et al., AISTATS 2022)",
    "Breakdown Properties of Optimal Transport Maps (Gonzalez-Sanz & Avella Medina, arXiv 2026)",
    "Consistency Matters: Defining Demonstration Data Quality Metrics (Sakr et al., ACM THRI 2024)",
    "Robomimic: A Framework for Robot Learning from Demonstration (Mandlekar et al., CoRL 2021) — Tool Hang failure analysis documents phase-specific failures"
  ],
  "description": "We propose PhaseOT, a policy-agnostic method for diagnosing demonstration quality at the task-phase granularity using a Phase-Structured Wasserstein Distance (PW₂) combined with mode-aware scoring. Unlike trajectory-level curation methods (DemInf, RINSE, CUPID) that produce a single quality score, and unlike transition-level methods (SCIZOR) that produce per-step anomaly flags and categorical labels, PhaseOT generates structured diagnostic profiles at the semantic task-phase level — each phase receives a distributional quality score, enabling targeted feedback ('demo #47's grasp phase is 3.2σ anomalous within its strategy mode, approach and transport phases are nominal').\n\n**Key methodological contributions:**\n(1) *Phase-Structured Wasserstein Distance (PW₂)*: PW₂(τ₁,τ₂) = Σ_k w_k · W₂²(μ_{τ₁,k}, μ_{τ₂,k}) restricts optimal transport couplings to respect phase alignment, so approach states can only match approach states, not grasp states. This is explicitly NOT the adapted/bicausal Wasserstein distance of Backhoff-Veraguas et al., which involves nested conditional optimization via dynamic programming. PW₂ is a simpler phase-constrained transport inspired by the adapted OT literature's emphasis on temporal causality but practically motivated by the discrete phase structure of manipulation tasks. The practical advantage: when noise is phase-localized (the common case in manipulation, as documented by SCIZOR's failure taxonomy and RoboMimic's Tool Hang analysis), PW₂ concentrates the anomaly signal in the affected phase rather than diluting it across the full trajectory.\n\n(2) *Mode-aware phase-level scoring*: Spectral clustering on the pairwise PW₂ distance matrix discovers valid strategy modes (e.g., left vs. right approach in Push-T, different subtask orderings in Kitchen). Quality scoring is performed within each mode using robust Wasserstein barycenters per phase, so minority strategies are not penalized as outliers. This is a capability no existing curation method provides — SCIZOR, DemInf, RINSE, and S2I all treat demonstrations uniformly without mode awareness.\n\n(3) *Phase-level importance weighting*: w_k(τ) = exp(-λ·q_k(τ)) preserves good phases of otherwise-flagged demos while downweighting anomalous phases coherently at the semantic phase level. This differs from SCIZOR's transition-level filtering (which removes individual state-action pairs) in operating at a meaningful semantic granularity — downweighting an entire grasp phase rather than scattered transitions maintains temporal coherence within phases.\n\n(4) *Phase-specific concentration inequality*: Under a phase-specific ε-contamination model, we prove that PW₂ achieves lower false-positive rates than global W₂ when contamination is phase-localized, with graceful degradation to trajectory-level performance when contamination is uniformly distributed. This does not derive from the adapted OT framework but from standard Wasserstein concentration results applied per-phase.\n\n**Differentiation from SCIZOR (ICRA 2026)**: SCIZOR achieves partial trajectory recovery (54% fully maintained, 31% partially maintained) via transition-level progress prediction with categorical diagnostic profiles. PhaseOT advances beyond SCIZOR in three specific dimensions: (a) semantic phase-level profiles vs. transition-level flags — a structured diagnostic report vs. a list of symptoms, (b) mode-aware scoring that preserves strategy diversity vs. uniform treatment of all demonstrations, (c) principled distributional distances with theoretical guarantees vs. heuristic progress signals. Experiment E3 directly compares phase-level vs. transition-level recovery quality for downstream policy learning.\n\n**Evidence for phase-localized contamination model**: SCIZOR's own categorical failure analysis (Manipulation Failure, Laggy Motion, Pause, Stuck at Collision) and RoboMimic's Tool Hang failures (Insertion Miss, Failed Insertion, Failed Tool Grasp, Tool Drop) document phase-specific failure modes. Manipulation tasks concentrate failures at contact events (grasp, insertion) more than free-space motion. When this assumption does not hold (e.g., distributed operator fatigue), PhaseOT gracefully degrades to within-mode trajectory-level scoring — the phase decomposition does not hurt, it simply does not help as much.\n\n**Evaluation**: Fine-tune Diffusion Policy (primary) and ACT on filtered/weighted subsets of RoboMimic MH (300 demos, 6 operators), Push-T (206 demos, bimodal), Franka Kitchen (~600 demos, combinatorial multimodality), LIBERO-10 (50 demos/task). SCIZOR is the primary baseline. Key experiments: (E1) bimodal strategy preservation in Push-T, (E2) phase-level diagnosis precision/recall with injected phase noise, (E3) phase-level vs. transition-level recovery comparison against SCIZOR, (E4) Kitchen ordering diversity retention, (E5) PhaseOT→CUPID pipeline combination, (E6) graceful degradation with uniform noise. Estimated compute: ~1500 A100-hours. Primary target: AAAI 2027 (deadline expected ~late July 2026). CoRL 2026 full paper is infeasible (deadline 13-16 days away).",
  "project_name": "phase_ot_diag",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Generator missed 3 major competing works that must be cited and compared against: (1) CUPID (CoRL 2025) — influence functions for robot data curation with strong empirical results, (2) DataMIL (May 2025, UT Austin) — policy-driven data selection validated on 60+ tasks including Open X-Embodiment, (3) DemInf (RSS 2025) — mutual information estimators for demo quality, 5-10% improvement on RoboMimic. All three are published at top robotics venues and directly compete with the proposed approach.", "Computational scalability is not adequately addressed: pairwise W2 distances require O(N²) Sinkhorn solves, each O(T² log T) per trajectory pair; Wasserstein barycenters are NP-hard in general and suffer a curse of dimensionality (exponential in state-action-time dimensionality). For datasets with thousands of demonstrations and high-dimensional robot states, this could be prohibitively expensive.", "GPU cost estimates are significantly underestimated: OpenVLA-OFT fine-tuning alone requires 8 A100s for 1-2 days (~192-384 A100h per run). With 4+ baselines (SCIZOR, QoQ, RINSE, unfiltered) × 2 models (OpenVLA-OFT, SmolVLA) × 2 benchmarks (RoboMimic, LIBERO) × multiple ablations, realistic compute is likely 1500-2500 A100h, not 400h.", "The claim 'naturally distinguishes noise from valid strategic diversity without separate mode identification steps' is misleading — k-Wasserstein-barycenter clustering IS a mode identification/discovery step. The approach does require choosing k (number of strategy modes) and running a clustering algorithm, which is precisely 'separate mode identification.'", "The theoretical contribution (provable outlier detection bounds under epsilon-contamination) assembles existing results from Robust Wasserstein Barycenter theory (arXiv Mar 2026) and Outlier-Robust OT (Mukherjee et al. 2021, Nietert et al. 2022) rather than deriving fundamentally new theory. This should be positioned as a novel application of existing theory, not as a theoretical contribution per se.", "CoRL 2026 timeline (17 days to abstract, 20 days to paper) is unrealistic for a from-scratch project. The user's requirement specifically targets CoRL 2026, but the proposal's own venue list relegates it to a stretch goal. AAAI 2027 and ICLR 2027 are more realistic but the user explicitly asked for CoRL 2026.", "No discussion of how the ground cost metric in state-action-time space should be designed — this is a critical design choice that significantly affects OT distances and is non-trivial for heterogeneous robot observation/action spaces (joint angles, gripper states, visual features have very different scales and semantics)."]
Feedback: To bring this to CoRL-acceptable quality, the Generator should: (1) **Add all missing baselines**: CUPID, DataMIL, and DemInf must be included in the landscape and experimental comparisons — these are published at CoRL 2025 and RSS 2025 and will be known to reviewers. (2) **Address computational scaling**: Propose concrete solutions — e.g., approximate OT via Wasserstein Wormhole embeddings for O(N) amortized distance computation, sliced Wasserstein distances instead of full W2, or subsampling strategies. Provide explicit complexity analysis for realistic dataset sizes (e.g., RoboMimic has ~200-300 demos per task, LIBERO has ~50 demos per task — compute actual wall-clock estimates). (3) **Fix the cost estimate**: Recalculate GPU hours accounting for VLA fine-tuning across all baseline conditions. Realistic estimates should be 1500-2500h A100 for manual mode, not 400h. (4) **Reframe theoretical contribution honestly**: Position as 'novel application of robust OT theory to trajectory quality scoring' rather than implying new theory. (5) **Design the ground cost metric explicitly**: Propose how to handle heterogeneous state-action-time dimensions (normalization, learned embeddings, or task-specific cost functions). (6) **Drop the misleading 'no mode identification' claim**: The k-barycenter clustering IS mode identification; instead, emphasize the advantage is that mode identification and quality scoring are unified in one principled OT framework. (7) **For CoRL 2026 feasibility**: The user should assess whether they already have partial implementation/results; if starting from scratch, target AAAI 2027 instead and be upfront about this.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — CoRL 2026 venue mismatch: The user explicitly targets CoRL 2026 (abstract deadline May 26, 17 days away). The proposal honestly pivots to AAAI 2027 (~August 2026 deadline), but this directly contradicts the user's stated requirement. The user should be explicitly informed that CoRL 2026 is infeasible from scratch.", "Missing competing work — Demo-SCORE (RSS 2025, Chen et al.): Self-curation method using online rollout classifiers to filter heterogeneous demos, achieving 15-35% improvement. Policy-dependent but directly in the demo curation space and published at a top robotics venue. Must be cited and positioned against.", "Missing related work — Sebag et al. (arXiv 2307.10810, 2023): 'On Combining Expert Demonstrations via Optimal Transport' uses multi-marginal OT specifically to handle multimodal demonstration distributions. While it targets combination not quality scoring, it directly precedents OT-Consensus's use of OT for multimodal demo handling, reducing the novelty claim.", "Novelty pressure in extremely crowded field: With 8+ demo curation methods published in 2024-2026, reviewers at AAAI/ICLR will scrutinize what OT-Consensus adds beyond DemInf (also policy-agnostic, also uses information-theoretic scoring, 5-10% on RoboMimic). The multimodal handling advantage needs concrete empirical evidence, not just theoretical argument.", "Wasserstein Wormhole adaptation unvalidated: The Wormhole model (ICML 2024) was designed for point cloud distributions (single-cell biology), not state-action-time trajectory distributions with heterogeneous components (positions, rotations, gripper states). Training Wormhole on this novel domain may require significant adaptation and there's no guarantee the learned embeddings will preserve W2 structure for trajectory data.", "Theoretical contribution remains thin for top venues: Instantiating existing robust barycenter results (Le Gouic et al. 2026; Nietert et al. 2022) for trajectory noise models is honest but reviewers may view this as 'plugging in known results' rather than a theoretical contribution. Consider whether deriving tighter, trajectory-specific bounds (e.g., exploiting temporal structure) could strengthen this.", "Partial mismatch with user's RL-inspired direction: The user specifically mentioned borrowing RL ideas (experience replay buffer, using data itself to score actions). OT-Consensus uses distributional geometry rather than RL-inspired scoring. While the user acknowledged theoretical approaches are acceptable, the connection to the RL scoring intuition could be made more explicit.", "Missing Re-Mix (CoRL 2025) from landscape: Re-Mix optimizes data mixtures for large-scale IL via DRO, outperforming uniform weights by 38%. It operates at domain-level not trajectory-level, but is highly relevant as a data-centric approach to IL quality and should be cited."]
Feedback: The proposal has improved substantially from Round 1 — cost estimates are realistic, the landscape is comprehensive, the theoretical contribution is honestly framed, and the ground cost metric is explicit. However, several issues prevent a pass:

**Priority fixes:**

1. **Address the CoRL 2026 impossibility directly**: State upfront that CoRL 2026 is infeasible from scratch. If the user has partial implementation or prior codebase, assess what can realistically be done in 17 days. Otherwise, confirm AAAI 2027 as the target and explain why.

2. **Add Demo-SCORE, Sebag et al. 2023, and Re-Mix to the landscape**: Demo-SCORE (RSS 2025) is a direct competitor. Sebag et al. (2023) precedents OT for multimodal demos. Re-Mix (CoRL 2025) is a key data-centric IL work. All must be cited.

3. **Strengthen the empirical differentiation story**: The biggest risk is 'why OT-Consensus over DemInf?' — both are policy-agnostic and evaluate on RoboMimic. Propose specific multimodal evaluation scenarios (e.g., tasks where demonstrations contain 2+ valid strategies like left-hand vs. right-hand grasps) where DemInf's global MI scoring would conflate valid diversity with noise, while OT-Consensus's mode-specific scoring would preserve it. This is the paper's strongest selling point and needs concrete experimental design.

4. **Validate or scope Wasserstein Wormhole adaptation**: Acknowledge that applying Wormhole to trajectory distributions (heterogeneous state-action-time spaces) is a novel adaptation that may require architecture modifications. Consider sliced Wasserstein as a simpler, more reliable Tier 2 fallback and position Wormhole as optional.

5. **Consider strengthening the theoretical contribution**: Instead of purely instantiating existing results, consider whether temporal structure in trajectories enables tighter outlier detection bounds (e.g., exploiting the Markov structure of sequential state-action pairs). Even a modest trajectory-specific result would elevate the theory from 'application' to 'contribution.'

6. **Make the RL connection explicit**: Frame OT-based scoring as a principled formalization of the intuition behind experience replay prioritization — trajectories that are distributionally close to the consensus (barycenter) can be viewed as 'high-priority' experiences, while outliers are 'low-priority' ones to be downweighted. This connects to the user's original RL direction.

**What's working well:** Comprehensive baseline comparison (6 methods), two-tier scaling, honest theoretical framing, explicit ground cost design, realistic cost estimates. The pre-filter pipeline idea (OT-Consensus → CUPID) is a compelling practical contribution that should be emphasized.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL — User requirement mismatch (CoRL 2026): The user explicitly targets CoRL 2026 (abstract deadline May 25-26, paper deadline May 28, i.e., 12-15 days from now). The proposal honestly acknowledges CoRL is infeasible and pivots to AAAI 2027. While this is intellectually honest, it directly violates the user's stated requirement. The user must be informed clearly that this idea cannot target CoRL 2026 from scratch.", "Novelty under pressure from crowded field: With 8+ demo curation methods published at top venues in 2024-2026, the bar for novelty is extremely high. The core contribution — Wasserstein barycenter clustering for mode-aware quality scoring — is a competent application of existing OT theory, but reviewers will ask: (1) Why is OT better than DemInf's simpler MI-based scoring? (2) Sebag et al. 2023 already combined OT with multimodal demonstrations. (3) Pallage 2025 (arXiv 2504.12918) independently proposes sliced-Wasserstein for data selection/filtering, showing the OT-for-filtering idea is not uniquely novel. The temporally-adapted distance is the most differentiating element, but it's an application of Backhoff-Veraguas et al. 2020 theory, not new theory.", "Empirical differentiation vs. DemInf is the make-or-break: Both OT-Consensus and DemInf are policy-agnostic and target similar benchmarks (RoboMimic, LIBERO). DemInf achieves 5-10% on RoboMimic. If OT-Consensus achieves similar or marginal improvements, the OT machinery will be viewed as unnecessary complexity. The synthetic multimodal experiments (E1-E3) are well-designed but risk being dismissed as constructed to favor the method. Real-world tasks where multimodality naturally arises and DemInf fails would be far more convincing, but finding such tasks is itself a research challenge.", "RL-PER connection is superficial: The claimed connection between OT-consensus scoring and prioritized experience replay (Schaul et al. 2016) is a stretch. PER prioritizes by TD error (a model-dependent signal reflecting learning progress), while OT-Consensus scores by distributional distance to barycenter (a model-free geometric signal). These are fundamentally different: one measures what the model needs to learn, the other measures statistical typicality. Calling barycenter distance 'analogous to TD error' is misleading. This weakens the paper's connection to the user's RL-inspired direction.", "Theoretical contribution remains incremental: The 'inherited guarantees' (applying Cheng & Liu 2026, Nietert et al. 2022, Gonzalez-Sanz & Avella Medina 2026) are honest applications of existing results. The novel phase-specific contamination model is a genuine contribution but is narrow — it assumes a particular contamination structure (phase-localized noise) that may not hold in practice. Reviewers may ask: when does phase-localized noise actually occur in real robot datasets?", "Missing comparison against SCIZOR on Sirius-Fleet: SCIZOR achieves 15.4% average improvement and outperforms DemInf by 19.2% on Sirius-Fleet — this is the strongest baseline in the field. The proposal lists SCIZOR as a baseline but doesn't discuss whether OT-Consensus's theoretical advantages translate to beating SCIZOR's practical results on large-scale datasets.", "Lightspeed Geometric Dataset Distance (ICML 2025) miscited: The proposal cites this as 'ICLR 2025' but it was published at ICML 2025. Minor but damages credibility if not corrected.", "Cost estimate tension: The proposal budgets OpenVLA-OFT full fine-tuning at '4 runs × 250h = 1000h' but each run requires 8 A100s for 1-2 days = 192-384h per run. 4 runs × ~300h = ~1200h just for full fine-tuning, already exceeding the line item. Additionally, running 7 baselines on 2 benchmarks with 2 VLA models could easily require 20+ fine-tuning runs, pushing total compute well beyond 2000h."]
Feedback: The proposal has improved substantially across three rounds — the landscape is now among the most comprehensive I've seen, the approach is precisely specified, and the theoretical framing is honest. However, several issues prevent a pass:

**Priority 1 — Address the venue mismatch decisively**: The user asked for CoRL 2026 (12-15 days away). This idea cannot target CoRL 2026 from scratch. State this unambiguously and either (a) propose a drastically scoped-down version that could be submitted in 12 days (e.g., a workshop paper at CoRL with preliminary results on 1-2 tasks), or (b) confirm AAAI 2027 as the target and explain the timeline advantage.

**Priority 2 — Sharpen the DemInf differentiation**: The paper lives or dies on whether it demonstrably outperforms DemInf on tasks where multimodality matters. Instead of only synthetic multimodal experiments, identify at least one naturally multimodal task in existing benchmarks where DemInf's global MI conflates strategy diversity with noise. RoboMimic Transport with multiple operators is promising — quantify the expected advantage concretely.

**Priority 3 — Drop or de-emphasize the PER analogy**: The connection between barycenter distance and TD error is too thin to be a 'contribution.' Demote it to a paragraph in the discussion section rather than a key methodological contribution. Instead, if the user wants an RL connection, consider: OT-scores as importance weights in an offline IL objective (formalize this as weighted behavioral cloning with OT-derived weights, which has a cleaner theoretical connection to importance-weighted regression).

**Priority 4 — Strengthen or reframe the theory**: The phase-specific contamination model is the most novel theoretical element. To make it a real contribution, prove tighter concentration inequalities for the adapted score under the Markov structure (not just the additive decomposition). Alternatively, if the math doesn't yield substantially tighter bounds, position the theory honestly as 'applying robust OT tools to trajectories yields useful guarantees' and lean harder on empirical contributions.

**Priority 5 — Fix the cost estimate**: Recalculate OpenVLA-OFT full fine-tuning costs (8×A100, 1-2 days per run). Budget 2500-3000h A100 for manual mode to be safe, not 2000h.

**Priority 6 — Fix the ICML/ICLR citation**: Lightspeed Geometric Dataset Distance is ICML 2025, not ICLR 2025.

**What's working well**: The comprehensive landscape, honest positioning against each related work, the two-tier OT computation strategy, the pre-filter pipeline idea, and the explicit ground cost metric design. The multimodal differentiation experiments (E1-E3) are well-designed. The honest assessment of CoRL infeasibility shows research maturity.

### Round 4 review
Verdict: revise
Issues: ["CRITICAL — CoRL 2026 venue mismatch persists: The user explicitly targets CoRL 2026 (abstract deadline May 26, 13 days away). The proposal correctly identifies CoRL as infeasible and pivots to AAAI 2027, which is intellectually honest but still violates the user's stated requirement. This has been flagged in all 3 previous reviews. The user must explicitly acknowledge and accept the venue change, or the idea needs to be scoped down to a 4-page CoRL workshop paper with preliminary results.", "SCIZOR overlap on partial trajectory recovery (NEW): SCIZOR (ICRA 2026) explicitly operates at the transition level (state-action pair level) and already achieves partial trajectory recovery — their paper states '54% of recovery behaviors are fully maintained, 31% partially maintained.' This directly overlaps with PhaseOT's claimed unique capability of 'preserving good phases of otherwise-flagged demonstrations.' The proposal lists SCIZOR as a baseline but does not acknowledge this overlap. PhaseOT must differentiate: (a) SCIZOR uses heuristic progress prediction, PhaseOT uses principled distributional distances; (b) SCIZOR filters individual transitions, PhaseOT produces semantically meaningful phase-level quality profiles; (c) PhaseOT has theoretical guarantees SCIZOR lacks. But the claim of unique partial recovery capability must be revised.", "Phase-localized contamination model assumption needs justification: The novel phase-specific concentration inequality assumes noise is phase-localized (ε_k > 0 for few k, ε_k ≈ 0 for most). When does this actually hold in real robot datasets? In practice, noisy demonstrations may exhibit distributed degradation (operator fatigue, teleoperation latency) rather than phase-localized failures (only the grasp fails). The proposal should provide evidence from existing datasets (e.g., RoboMimic MH proficiency levels) that phase-localized noise is common, or acknowledge this as a limitation with graceful degradation analysis.", "Empirical differentiation vs. SCIZOR is the new make-or-break: Previous reviews focused on differentiating from DemInf. Now that SCIZOR's transition-level capabilities are clear, PhaseOT must demonstrate clear advantages over SCIZOR on at least one dimension: (1) multimodal handling (SCIZOR doesn't discover modes), (2) diagnostic interpretability (SCIZOR doesn't produce phase-level quality profiles), or (3) theoretical guarantees translating to practical gains. Experiment E1 (Push-T bimodal preservation) is well-designed for this but needs to explicitly include SCIZOR as the primary baseline, not just DemInf.", "Adapted Wasserstein distance formulation is simplified in a potentially misleading way: The proposed AW₂(τ₁, τ₂) = Σ_k W₂²(μ_{τ₁,k}, μ_{τ₂,k}) is a phase-aligned additive decomposition, NOT the full adapted/bicausal Wasserstein distance of Backhoff-Veraguas et al. The adapted distance in the mathematical finance literature involves constraints on the filtration structure and conditional distributions, not simply an additive decomposition over time segments. The proposal should clarify that this is an 'adapted-inspired' decomposition motivated by the causal structure of trajectories, not a direct application of the full adapted OT framework. Over-claiming the connection to adapted OT theory could draw reviewer criticism.", "Missing CIQL reference verification: The proposal cites 'CIQL (2024): Confidence-based per-transition quality scoring via dynamics evaluation' but I could not find any paper matching this exact name/description. This reference should be verified or removed — a fabricated citation would be fatal at review.", "Cost estimate minor issue — GPU utilization in manual mode (55%) seems low: With 1500h at 55% utilization, actual billed time would be much higher. Modern cloud billing is per-second, so utilization mainly affects timeline, not cost. But the $2,250 estimate assumes 1500 effective GPU-hours at $1.50/h, which is reasonable if using spot instances."]
Feedback: The proposal has improved dramatically across four rounds — the landscape is now among the most comprehensive in the demo curation field, the approach is precisely specified, and the experimental design targets unique capabilities. However, several issues prevent a pass:

**Priority 1 — Acknowledge and differentiate from SCIZOR's transition-level capabilities**: SCIZOR already filters at the state-action pair level and achieves partial trajectory recovery. PhaseOT's differentiation should focus on: (a) semantically meaningful phase-level diagnosis (not individual transitions), (b) mode-aware scoring that handles multimodality, (c) theoretical guarantees for outlier detection, and (d) principled distributional distances vs. heuristic progress signals. Revise the 'unique capability' claims for partial recovery to acknowledge SCIZOR's prior work.

**Priority 2 — Clarify the adapted OT formulation**: The additive phase decomposition AW₂ = Σ_k W₂² is inspired by but not identical to the full adapted/bicausal OT of Backhoff-Veraguas et al. Be precise: this is a 'temporally-constrained transport' that restricts transport plans to respect phase boundaries, motivated by the adapted OT literature. Don't over-claim the mathematical pedigree — reviewers familiar with adapted OT theory will notice.

**Priority 3 — Justify the phase-localized contamination model**: Provide concrete evidence from existing datasets (e.g., analyze RoboMimic MH multi-operator data) showing that common failure modes ARE phase-localized. If the evidence is mixed, add a graceful degradation analysis: what happens to PhaseOT's guarantees when noise is distributed across phases?

**Priority 4 — Verify CIQL reference**: I could not find this paper. If it doesn't exist, remove it. If it's under a different name, correct the citation.

**Priority 5 — Address the venue mismatch**: The user asked for CoRL 2026. This idea targets AAAI 2027 at earliest. Either (a) propose a drastically scoped CoRL workshop paper (4 pages, Push-T + Can only, if workshop deadlines permit), or (b) explicitly inform the user that CoRL 2026 is impossible and get buy-in for AAAI 2027.

**What's working well**: The Phase-OT framing is cleaner and more focused than previous OT-Consensus versions. The experimental design (especially E1 bimodal preservation and E3 phase-diagnosis validation) targets genuine unique capabilities. The two-tier computation strategy is practical. The theoretical contribution (phase-specific concentration) is the right kind of novelty for a top venue — non-trivial but not over-claiming. The honest assessment of venue feasibility shows research maturity.


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
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "a50c1836-b887-4a76-a5a0-2880aaa4b0d6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T10:45:25.362Z_

```json
{
  "parentUuid": "a50c1836-b887-4a76-a5a0-2880aaa4b0d6",
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
  "uuid": "3fec5c0d-febf-457a-b4a3-9b6c82692566",
  "timestamp": "2026-05-13T10:45:25.362Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T10:45:25.362Z_

```json
{
  "parentUuid": "3fec5c0d-febf-457a-b4a3-9b6c82692566",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5d819af7-191f-4000-aa94-16b1c6f279be",
  "timestamp": "2026-05-13T10:45:25.362Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
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
  "leafUuid": "5d819af7-191f-4000-aa94-16b1c6f279be",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PhaseOT demo quality diagnosis idea (Round 5)",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Assistant

_source line 8 · 2026-05-13T10:45:29.806Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea (PhaseOT) in its 5th round of revision. This is a comprehensive proposal for phase-level demonstration quality diagnosis using structured optimal transport. Let me conduct independent verification of the key claims.

Let me start by searching for the key competing works and verifying the claims made in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d819af7-191f-4000-aa94-16b1c6f279be",
  "isSidechain": false,
  "requestId": "req_011CazS3e7NmdskXonXB17pr",
  "type": "assistant",
  "uuid": "f9b9ae14-3b6d-418a-879a-c58aa12b2c2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh52P16zyyhd8krxa1Pt4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24978,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24978
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

_source line 9 · 2026-05-13T10:45:30.873Z_

I'll conduct an independent, thorough review of PhaseOT. Let me start by verifying key claims, searching for competing work, and checking references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9b9ae14-3b6d-418a-879a-c58aa12b2c2d",
  "isSidechain": false,
  "requestId": "req_011CazS3e7NmdskXonXB17pr",
  "type": "assistant",
  "uuid": "67cd1a9c-02f3-4130-b827-6b45b762909b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh52P16zyyhd8krxa1Pt4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24978,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24978
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

_source line 10 · 2026-05-13T10:45:36.477Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SrBNwwUBQ8NBq9ppED6kWt`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SCIZOR ICRA 2026 claims",
  "prompt": "Search the web to verify the following claims about the paper \"SCIZOR\" which is claimed to be published at ICRA 2026:\n1. Does this paper exist? What venue is it actually published at?\n2. Does it operate at the transition/state-action pair level?\n3. Does it achieve \"54% of recovery behaviors fully maintained, 31% partially maintained\"?\n4. Does it produce categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision)?\n5. Does it achieve +32.9% on Sirius-Fleet and +5.4% on RoboMimic?\n6. Does it outperform DemInf by 19.2% on Sirius-Fleet?\n\nSearch using queries like:\n- \"SCIZOR self-supervised data curation imitation learning\"\n- \"SCIZOR ICRA 2026 robot\"\n- site:arxiv.org SCIZOR imitation learning\n\nUse WebSearch and WebFetch to find and read the actual paper. Report exact findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67cd1a9c-02f3-4130-b827-6b45b762909b",
  "isSidechain": false,
  "requestId": "req_011CazS3e7NmdskXonXB17pr",
  "type": "assistant",
  "uuid": "288dd568-6ce0-4073-b588-b2d08117b0e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh52P16zyyhd8krxa1Pt4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24978,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24978
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

_source line 11 · 2026-05-13T10:47:02.125Z_

<details><summary>↩ Tool result · `toolu_01SrBNwwUBQ8NBq9ppED6kWt`</summary>

```text
Now I have a clear picture. The v1 used "Slow Motion" while v2 changed it to "Laggy Motion." Let me compile the final findings.

Here are my findings for each claim:

---

**1. Does this paper exist? What venue is it actually published at?**

**VERIFIED.** The paper exists: "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning" by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, and Yuke Zhu (UT Austin / NVIDIA). It is available on arXiv as [2505.22626](https://arxiv.org/abs/2505.22626). The claim that it is published at **ICRA 2026 is correct** -- this was confirmed by co-author Huihan Liu on X/Twitter and on the project website. The conference is the 2026 IEEE International Conference on Robotics and Automation (Vienna, Austria, June 1-5, 2026).

---

**2. Does it operate at the transition/state-action pair level?**

**VERIFIED.** The paper describes itself as "the first self-supervised transition-level curation framework" and explicitly operates on individual state-action pairs rather than at coarser granularities (dataset or trajectory level). Both terms -- "transition-level" and "state-action pair level" -- are used in the paper.

---

**3. Does it achieve "54% of recovery behaviors fully maintained, 31% partially maintained"?**

**VERIFIED.** In Appendix B.4 (Additional Research Questions), the paper states: "54% of recovery behaviors are fully maintained, and 31% are partially maintained. Only 15% are deleted." This refers to analysis of grasping failure recovery behaviors and whether SCIZOR preserves them during curation.

---

**4. Does it produce categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision)?**

**PARTIALLY VERIFIED with caveats.**
- The paper does identify categories of suboptimal data in Figure 4, but it does **not** call them "categorical diagnostic profiles." The paper refers to them as "suboptimal types," "failure modes," or "suboptimal scenarios."
- The exact categories are: **Slow Motion** (in v1) / **Laggy Motion** (in v2), **Manipulation Failure**, **Pause**, **Stuck at Collision**, **Move Back and Forth**, and **False Positive**.
- The claim lists 4 categories but the paper actually has 6 (including "Move Back and Forth" and "False Positive").
- The name "Laggy Motion" appears in the revised v2; v1 used "Slow Motion." The other three names (Manipulation Failure, Pause, Stuck at Collision) are exact matches.

---

**5. Does it achieve +32.9% on Sirius-Fleet and +5.4% on RoboMimic?**

**VERIFIED.** The paper reports absolute gains of **+32.9% on Sirius-Fleet** real-robot tasks and **+5.4% on RoboMimic**, compared to training on the full dataset. It also reports +8.1% on OXE-Magic-Soup, for an average improvement of 15.4% across benchmarks.

---

**6. Does it outperform DemInf by 19.2% on Sirius-Fleet?**

**VERIFIED.** The paper states that "SCIZOR significantly outperforms DemInf by 19.2%" on the Sirius-Fleet dataset, "highlighting the advantage of fine-grained state-action curation under uneven data distributions." However, it is noted that on RoboMimic, SCIZOR does not outperform DemInf, since that dataset's explicit quality levels favor trajectory-level filtering.

---

**Summary:** All six claims are substantively accurate. The only minor discrepancies are: (a) the failure categories are called "suboptimal types" / "failure modes," not "categorical diagnostic profiles"; (b) "Laggy Motion" appears in v2 of the paper while v1 used "Slow Motion"; and (c) the claim lists only 4 of the 6 actual categories, omitting "Move Back and Forth" and "False Positive."

Sources:
- [SCIZOR on arXiv (abs)](https://arxiv.org/abs/2505.22626)
- [SCIZOR HTML v1](https://arxiv.org/html/2505.22626v1)
- [SCIZOR HTML v2](https://arxiv.org/html/2505.22626v2)
- [SCIZOR Project Page (UT Austin)](https://ut-austin-rpl.github.io/SCIZOR/)
- [Huihan Liu's announcement on X](https://x.com/huihan_liu/status/2017698931493195899)
- [SCIZOR on OpenReview](https://openreview.net/pdf?id=Wo8eEdFUDF)

agentId: a134dce42810f0da3 (use SendMessage with to: 'a134dce42810f0da3' to continue this agent)
&lt;usage>total_tokens: 19449
tool_uses: 12
duration_ms: 85641&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "288dd568-6ce0-4073-b588-b2d08117b0e5",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "612d3963-8628-4931-bf84-6735b405552e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify the following claims about the paper \"SCIZOR\" which is claimed to be published at ICRA 2026:\n1. Does this paper exist? What venue is it actually published at?\n2. Does it operate at the transition/state-action pair level?\n3. Does it achieve \"54% of recovery behaviors fully maintained, 31% partially maintained\"?\n4. Does it produce categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision)?\n5. Does it achieve +32.9% on Sirius-Fleet and +5.4% on RoboMimic?\n6. Does it outperform DemInf by 19.2% on Sirius-Fleet?\n\nSearch using queries like:\n- \"SCIZOR self-supervised data curation imitation learning\"\n- \"SCIZOR ICRA 2026 robot\"\n- site:arxiv.org SCIZOR imitation learning\n\nUse WebSearch and WebFetch to find and read the actual paper. Report exact findings.",
    "agentId": "a134dce42810f0da3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a clear picture. The v1 used \"Slow Motion\" while v2 changed it to \"Laggy Motion.\" Let me compile the final findings.\n\nHere are my findings for each claim:\n\n---\n\n**1. Does this paper exist? What venue is it actually published at?**\n\n**VERIFIED.** The paper exists: \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning\" by Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, and Yuke Zhu (UT Austin / NVIDIA). It is available on arXiv as [2505.22626](https://arxiv.org/abs/2505.22626). The claim that it is published at **ICRA 2026 is correct** -- this was confirmed by co-author Huihan Liu on X/Twitter and on the project website. The conference is the 2026 IEEE International Conference on Robotics and Automation (Vienna, Austria, June 1-5, 2026).\n\n---\n\n**2. Does it operate at the transition/state-action pair level?**\n\n**VERIFIED.** The paper describes itself as \"the first self-supervised transition-level curation framework\" and explicitly operates on individual state-action pairs rather than at coarser granularities (dataset or trajectory level). Both terms -- \"transition-level\" and \"state-action pair level\" -- are used in the paper.\n\n---\n\n**3. Does it achieve \"54% of recovery behaviors fully maintained, 31% partially maintained\"?**\n\n**VERIFIED.** In Appendix B.4 (Additional Research Questions), the paper states: \"54% of recovery behaviors are fully maintained, and 31% are partially maintained. Only 15% are deleted.\" This refers to analysis of grasping failure recovery behaviors and whether SCIZOR preserves them during curation.\n\n---\n\n**4. Does it produce categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision)?**\n\n**PARTIALLY VERIFIED with caveats.**\n- The paper does identify categories of suboptimal data in Figure 4, but it does **not** call them \"categorical diagnostic profiles.\" The paper refers to them as \"suboptimal types,\" \"failure modes,\" or \"suboptimal scenarios.\"\n- The exact categories are: **Slow Motion** (in v1) / **Laggy Motion** (in v2), **Manipulation Failure**, **Pause**, **Stuck at Collision**, **Move Back and Forth**, and **False Positive**.\n- The claim lists 4 categories but the paper actually has 6 (including \"Move Back and Forth\" and \"False Positive\").\n- The name \"Laggy Motion\" appears in the revised v2; v1 used \"Slow Motion.\" The other three names (Manipulation Failure, Pause, Stuck at Collision) are exact matches.\n\n---\n\n**5. Does it achieve +32.9% on Sirius-Fleet and +5.4% on RoboMimic?**\n\n**VERIFIED.** The paper reports absolute gains of **+32.9% on Sirius-Fleet** real-robot tasks and **+5.4% on RoboMimic**, compared to training on the full dataset. It also reports +8.1% on OXE-Magic-Soup, for an average improvement of 15.4% across benchmarks.\n\n---\n\n**6. Does it outperform DemInf by 19.2% on Sirius-Fleet?**\n\n**VERIFIED.** The paper states that \"SCIZOR significantly outperforms DemInf by 19.2%\" on the Sirius-Fleet dataset, \"highlighting the advantage of fine-grained state-action curation under uneven data distributions.\" However, it is noted that on RoboMimic, SCIZOR does not outperform DemInf, since that dataset's explicit quality levels favor trajectory-level filtering.\n\n---\n\n**Summary:** All six claims are substantively accurate. The only minor discrepancies are: (a) the failure categories are called \"suboptimal types\" / \"failure modes,\" not \"categorical diagnostic profiles\"; (b) \"Laggy Motion\" appears in v2 of the paper while v1 used \"Slow Motion\"; and (c) the claim lists only 4 of the 6 actual categories, omitting \"Move Back and Forth\" and \"False Positive.\"\n\nSources:\n- [SCIZOR on arXiv (abs)](https://arxiv.org/abs/2505.22626)\n- [SCIZOR HTML v1](https://arxiv.org/html/2505.22626v1)\n- [SCIZOR HTML v2](https://arxiv.org/html/2505.22626v2)\n- [SCIZOR Project Page (UT Austin)](https://ut-austin-rpl.github.io/SCIZOR/)\n- [Huihan Liu's announcement on X](https://x.com/huihan_liu/status/2017698931493195899)\n- [SCIZOR on OpenReview](https://openreview.net/pdf?id=Wo8eEdFUDF)"
      }
    ],
    "totalDurationMs": 85641,
    "totalTokens": 19449,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 17819,
      "output_tokens": 1221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1221,
          "cache_read_input_tokens": 17819,
          "cache_creation_input_tokens": 408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 408,
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
  "sourceToolAssistantUUID": "288dd568-6ce0-4073-b588-b2d08117b0e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T10:47:08.334Z_

SCIZOR claims verified. Now let me search for competing works the proposal may have missed, verify CIQL, and check for recent concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "612d3963-8628-4931-bf84-6735b405552e",
  "isSidechain": false,
  "requestId": "req_011CazSAmeW3uMe7iyNTrbvx",
  "type": "assistant",
  "uuid": "e4553240-392a-4b15-9e90-83411558d82f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9eZfpmM5VXHnzUP8myLGJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 36819,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 36819,
          "cache_creation_input_tokens": 1764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1764
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

_source line 13 · 2026-05-13T10:47:14.256Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FMjRt4WadiMzW39EadWrw6`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify CIQL reference exists",
  "prompt": "Search the web to verify whether the paper \"CIQL\" (Confidence-based Inverse soft-Q Learning) by Bu et al. exists. The proposal claims it's published in IEEE Robotics and Automation Letters (RA-L), Vol. 9, Issue 8, pp. 7150-7157, August 2024, and deals with per-transition confidence scoring via dynamics evaluation for aligning human intent from imperfect demonstrations.\n\nSearch using:\n- \"CIQL confidence inverse soft-Q learning\"\n- \"Bu\" \"confidence-based\" \"imperfect demonstrations\" IEEE RA-L 2024\n- \"Aligning Human Intent from Imperfect Demonstrations\" \n- site:ieee.org \"confidence-based inverse\" demonstrations\n\nUse WebSearch to find the paper. Report whether it exists with the claimed title, authors, venue, and content. This was flagged as potentially fabricated in a previous review round."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4553240-392a-4b15-9e90-83411558d82f",
  "isSidechain": false,
  "requestId": "req_011CazSAmeW3uMe7iyNTrbvx",
  "type": "assistant",
  "uuid": "8f96564e-6228-4963-bea2-c9806ac9933e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9eZfpmM5VXHnzUP8myLGJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 36819,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 36819,
          "cache_creation_input_tokens": 1764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1764
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

_source line 14 · 2026-05-13T10:47:22.191Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AwQWq5jeH1z3JsAVCX64QP`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for concurrent/missed competing work",
  "prompt": "Search the web for recent (2025-2026) papers on demonstration quality assessment, data curation for robot learning, and related topics that might compete with or overlap with a method called \"PhaseOT\" that uses optimal transport for phase-level demonstration quality diagnosis with mode-aware scoring.\n\nSpecifically search for:\n1. Any papers using optimal transport for robot demonstration filtering or scoring (2025-2026)\n2. Papers on phase-level or segment-level demonstration quality assessment\n3. Papers on multimodal/multi-strategy demonstration handling in imitation learning\n4. Papers combining changepoint detection with quality scoring for demonstrations\n5. Any very recent demo curation papers from 2026\n\nUse these search queries:\n- \"demonstration quality\" \"optimal transport\" robot 2025 2026 site:arxiv.org\n- \"phase-level\" OR \"segment-level\" demonstration curation robot 2025 2026\n- \"multimodal demonstrations\" filtering quality imitation learning 2025 2026\n- \"demonstration curation\" robot learning 2026 site:arxiv.org\n- \"data quality\" \"imitation learning\" scoring filtering 2026\n- site:arxiv.org robot demonstration noise filtering reinforcement learning 2025 2026\n- \"trajectory quality\" robot learning optimal transport\n\nFor any papers found, report: title, authors, venue, year, and a brief summary of how they relate to PhaseOT's approach. Focus on finding work the proposal may have MISSED."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f96564e-6228-4963-bea2-c9806ac9933e",
  "isSidechain": false,
  "requestId": "req_011CazSAmeW3uMe7iyNTrbvx",
  "type": "assistant",
  "uuid": "0d8c5214-e8b1-486b-9c6b-a87b7417c669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9eZfpmM5VXHnzUP8myLGJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 36819,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 36819,
          "cache_creation_input_tokens": 1764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1764
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

_source line 15 · 2026-05-13T10:47:26.424Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JCLEU4jBkkVcJhGtg1XAFB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify CoRL 2026 deadlines",
  "prompt": "Search the web to verify the exact deadlines for CoRL 2026 (Conference on Robot Learning 2026). The proposal claims:\n- Abstract deadline: May 26, 2026\n- Paper deadline: May 29, 2026\n- Conference dates: November 9-12, 2026 in Austin, TX\n\nAlso check:\n1. Are these deadlines correct and current?\n2. Has the deadline already passed or been extended?\n3. Are there any CoRL 2026 workshop paper submission opportunities?\n\nSearch using:\n- \"CoRL 2026\" deadline submission\n- \"Conference on Robot Learning 2026\" call for papers\n- site:corl2026.org OR site:corl.org 2026 deadline\n- \"CoRL 2026\" Austin November\n\nReport exact findings with sources."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d8c5214-e8b1-486b-9c6b-a87b7417c669",
  "isSidechain": false,
  "requestId": "req_011CazSAmeW3uMe7iyNTrbvx",
  "type": "assistant",
  "uuid": "473bafbe-14f6-4545-97bf-3f3b45f07c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9eZfpmM5VXHnzUP8myLGJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 36819,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 36819,
          "cache_creation_input_tokens": 1764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1764
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

_source line 16 · 2026-05-13T10:47:59.774Z_

<details><summary>↩ Tool result · `toolu_01FMjRt4WadiMzW39EadWrw6`</summary>

```text
All the key details have been confirmed. Here is my full report:

---

**Verdict: The paper is REAL -- it is NOT fabricated.**

The paper "CIQL" (Confidence-based Inverse soft-Q Learning) exists and all claimed details are verified as accurate.

**Confirmed details:**

- **Title:** "Aligning Human Intent from Imperfect Demonstrations with Confidence-based Inverse soft-Q Learning" -- matches the claim exactly.
- **Authors:** Xizhou Bu, Wenjuan Li, Zhengxiong Liu, Zhiqiang Ma, Panfeng Huang -- the claim of "Bu et al." is correct (first author is Bu).
- **Venue:** IEEE Robotics and Automation Letters (RA-L) -- matches.
- **Volume/Issue/Pages:** Vol. 9, Issue 8, pp. 7150-7157 -- matches exactly.
- **Date:** August 2024 -- matches.
- **DOI:** 10.1109/LRA.2024.3418275
- **Content:** The paper proposes a transition-based confidence evaluation method to obtain fine-grained confidence scores for demonstrations, and develops CIQL, a generalized confidence-based imitation learning framework built on inverse soft-Q learning. It addresses learning from imperfect human demonstrations -- this matches the claimed content about "per-transition confidence scoring via dynamics evaluation for aligning human intent from imperfect demonstrations."
- **arXiv preprint:** 2312.11194 (first posted December 2023, updated to match the published version).

The paper is indexed on both IEEE Xplore (document ID 10569029) and arXiv, and its content description aligns with the claims. There is no indication of fabrication.

Sources:
- [arXiv: 2312.11194](https://arxiv.org/abs/2312.11194)
- [IEEE Xplore: Document 10569029](https://ieeexplore.ieee.org/document/10569029/)
- [arXiv HTML version (v3)](https://arxiv.org/html/2312.11194v3)

agentId: acd00d06881a3fe80 (use SendMessage with to: 'acd00d06881a3fe80' to continue this agent)
&lt;usage>total_tokens: 16601
tool_uses: 11
duration_ms: 45512&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f96564e-6228-4963-bea2-c9806ac9933e",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "59672d18-5605-4438-b1c9-6449f38d8730",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify whether the paper \"CIQL\" (Confidence-based Inverse soft-Q Learning) by Bu et al. exists. The proposal claims it's published in IEEE Robotics and Automation Letters (RA-L), Vol. 9, Issue 8, pp. 7150-7157, August 2024, and deals with per-transition confidence scoring via dynamics evaluation for aligning human intent from imperfect demonstrations.\n\nSearch using:\n- \"CIQL confidence inverse soft-Q learning\"\n- \"Bu\" \"confidence-based\" \"imperfect demonstrations\" IEEE RA-L 2024\n- \"Aligning Human Intent from Imperfect Demonstrations\" \n- site:ieee.org \"confidence-based inverse\" demonstrations\n\nUse WebSearch to find the paper. Report whether it exists with the claimed title, authors, venue, and content. This was flagged as potentially fabricated in a previous review round.",
    "agentId": "acd00d06881a3fe80",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All the key details have been confirmed. Here is my full report:\n\n---\n\n**Verdict: The paper is REAL -- it is NOT fabricated.**\n\nThe paper \"CIQL\" (Confidence-based Inverse soft-Q Learning) exists and all claimed details are verified as accurate.\n\n**Confirmed details:**\n\n- **Title:** \"Aligning Human Intent from Imperfect Demonstrations with Confidence-based Inverse soft-Q Learning\" -- matches the claim exactly.\n- **Authors:** Xizhou Bu, Wenjuan Li, Zhengxiong Liu, Zhiqiang Ma, Panfeng Huang -- the claim of \"Bu et al.\" is correct (first author is Bu).\n- **Venue:** IEEE Robotics and Automation Letters (RA-L) -- matches.\n- **Volume/Issue/Pages:** Vol. 9, Issue 8, pp. 7150-7157 -- matches exactly.\n- **Date:** August 2024 -- matches.\n- **DOI:** 10.1109/LRA.2024.3418275\n- **Content:** The paper proposes a transition-based confidence evaluation method to obtain fine-grained confidence scores for demonstrations, and develops CIQL, a generalized confidence-based imitation learning framework built on inverse soft-Q learning. It addresses learning from imperfect human demonstrations -- this matches the claimed content about \"per-transition confidence scoring via dynamics evaluation for aligning human intent from imperfect demonstrations.\"\n- **arXiv preprint:** 2312.11194 (first posted December 2023, updated to match the published version).\n\nThe paper is indexed on both IEEE Xplore (document ID 10569029) and arXiv, and its content description aligns with the claims. There is no indication of fabrication.\n\nSources:\n- [arXiv: 2312.11194](https://arxiv.org/abs/2312.11194)\n- [IEEE Xplore: Document 10569029](https://ieeexplore.ieee.org/document/10569029/)\n- [arXiv HTML version (v3)](https://arxiv.org/html/2312.11194v3)"
      }
    ],
    "totalDurationMs": 45512,
    "totalTokens": 16601,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 15647,
      "output_tokens": 504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 504,
          "cache_read_input_tokens": 15647,
          "cache_creation_input_tokens": 411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 411,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "8f96564e-6228-4963-bea2-c9806ac9933e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T10:48:49.099Z_

<details><summary>↩ Tool result · `toolu_01JCLEU4jBkkVcJhGtg1XAFB`</summary>

```text
Now I have comprehensive information. Let me compile the findings.

Here is my detailed report on CoRL 2026 deadlines:

---

## CoRL 2026 Deadline Verification

### 1. Are the proposed deadlines correct?

**The proposal's claimed deadlines are CORRECT.** Multiple authoritative sources confirm:

| Item | Proposal Claims | Verified Dates | Status |
|---|---|---|---|
| Abstract deadline | May 26, 2026 | **May 26, 2026, 11:59 AM UTC** | CORRECT |
| Paper deadline | May 29, 2026 | **May 29, 2026, 11:59 AM UTC** | CORRECT |
| Conference dates | Nov 9-12, 2026 | **Nov 9-12, 2026** | CORRECT |
| Location | Austin, TX | **JW Marriott Austin, 110 E 2nd St, Austin, TX 78701** | CORRECT |

**Important note on timezone:** The deadlines are at **11:59 AM UTC** (not 11:59 PM / not AoE). This is a notably early cutoff -- effectively midday UTC, which is early morning in US time zones. The official Instructions for Authors page references the paper deadline as "Thursday (5/28) EOD" which may indicate the official site originally listed May 28, but the Hugging Face AI Deadlines tracker (which was updated with official data) and the Bibby conference deadlines tracker both consistently show **May 26 for abstracts and May 29 for papers at 11:59 UTC**. The Instructions for Authors page also mentions a camera-ready deadline of **October 12, 2026, 23:59 AoE**.

**Note on date discrepancy:** Some search result summaries initially returned May 25/May 28, but when I directly fetched the authoritative deadline tracker pages (Hugging Face AI Deadlines commit and trybibby.com), both confirmed **May 26 and May 29** -- matching the proposal exactly. The "May 25/28" figures appear to be from older or inaccurate secondary sources.

### 2. Has the deadline passed or been extended?

- **No, the deadlines have NOT yet passed.** Today is May 13, 2026. The abstract deadline (May 26) is **13 days away** and the paper deadline (May 29) is **16 days away**.
- **No deadline extensions have been announced.** The official CoRL 2026 announcements page (corl.org/annoucements) shows no extension notices. The Instructions for Authors page explicitly states: **"deadlines are final"** and accommodations cannot be made for missing either the abstract or paper deadline.

### 3. Workshop paper submission opportunities

- **Workshops will be held on November 9, 2026** (the day before the main conference starts on Nov 10).
- The **Call for Workshops** was announced on April 29, 2026 per the official announcements page.
- Workshop proposals must be **2-3 pages (max 5 pages)** and focus on interactive, problem-oriented formats.
- Each workshop can have a maximum of **4 invited speakers**, with each speaker limited to 2 events.
- Workshop contacts: Danfei Xu (danfei@gatech.edu) and Rudolf Lioutikov (lioutikov@kit.edu).
- **The specific deadline for workshop proposal submissions is NOT listed** on the public-facing pages I was able to access. You would need to check the submission form linked from the Call for Workshops page or contact the workshop chairs directly.
- Note: Individual workshop paper deadlines (for papers submitted *to* accepted workshops) would be set by each workshop's organizers after workshop acceptance, and are typically later than the main conference deadline.

### Summary

The proposal's dates are accurate. All three claimed deadlines/dates match the official sources. No extensions have been announced, and the organizers have stated deadlines are final.

---

Sources:
- [CoRL 2026 Official Website](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 Contributions Page](https://www.corl.org/contributions)
- [CoRL 2026 Announcements](https://www.corl.org/annoucements)
- [Hugging Face AI Deadlines - CoRL 2026 Update](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)
- [Bibby AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)
- [CoRL 2026 on OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)
- [CoRL 2026 Call for Workshops (LinkedIn - Danfei Xu)](https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b)

agentId: a210ac99a397f26f6 (use SendMessage with to: 'a210ac99a397f26f6' to continue this agent)
&lt;usage>total_tokens: 20075
tool_uses: 17
duration_ms: 82673&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "473bafbe-14f6-4545-97bf-3f3b45f07c30",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "fbf85230-d7d6-48d8-92bc-2dd346d733cf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify the exact deadlines for CoRL 2026 (Conference on Robot Learning 2026). The proposal claims:\n- Abstract deadline: May 26, 2026\n- Paper deadline: May 29, 2026\n- Conference dates: November 9-12, 2026 in Austin, TX\n\nAlso check:\n1. Are these deadlines correct and current?\n2. Has the deadline already passed or been extended?\n3. Are there any CoRL 2026 workshop paper submission opportunities?\n\nSearch using:\n- \"CoRL 2026\" deadline submission\n- \"Conference on Robot Learning 2026\" call for papers\n- site:corl2026.org OR site:corl.org 2026 deadline\n- \"CoRL 2026\" Austin November\n\nReport exact findings with sources.",
    "agentId": "a210ac99a397f26f6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the findings.\n\nHere is my detailed report on CoRL 2026 deadlines:\n\n---\n\n## CoRL 2026 Deadline Verification\n\n### 1. Are the proposed deadlines correct?\n\n**The proposal's claimed deadlines are CORRECT.** Multiple authoritative sources confirm:\n\n| Item | Proposal Claims | Verified Dates | Status |\n|---|---|---|---|\n| Abstract deadline | May 26, 2026 | **May 26, 2026, 11:59 AM UTC** | CORRECT |\n| Paper deadline | May 29, 2026 | **May 29, 2026, 11:59 AM UTC** | CORRECT |\n| Conference dates | Nov 9-12, 2026 | **Nov 9-12, 2026** | CORRECT |\n| Location | Austin, TX | **JW Marriott Austin, 110 E 2nd St, Austin, TX 78701** | CORRECT |\n\n**Important note on timezone:** The deadlines are at **11:59 AM UTC** (not 11:59 PM / not AoE). This is a notably early cutoff -- effectively midday UTC, which is early morning in US time zones. The official Instructions for Authors page references the paper deadline as \"Thursday (5/28) EOD\" which may indicate the official site originally listed May 28, but the Hugging Face AI Deadlines tracker (which was updated with official data) and the Bibby conference deadlines tracker both consistently show **May 26 for abstracts and May 29 for papers at 11:59 UTC**. The Instructions for Authors page also mentions a camera-ready deadline of **October 12, 2026, 23:59 AoE**.\n\n**Note on date discrepancy:** Some search result summaries initially returned May 25/May 28, but when I directly fetched the authoritative deadline tracker pages (Hugging Face AI Deadlines commit and trybibby.com), both confirmed **May 26 and May 29** -- matching the proposal exactly. The \"May 25/28\" figures appear to be from older or inaccurate secondary sources.\n\n### 2. Has the deadline passed or been extended?\n\n- **No, the deadlines have NOT yet passed.** Today is May 13, 2026. The abstract deadline (May 26) is **13 days away** and the paper deadline (May 29) is **16 days away**.\n- **No deadline extensions have been announced.** The official CoRL 2026 announcements page (corl.org/annoucements) shows no extension notices. The Instructions for Authors page explicitly states: **\"deadlines are final\"** and accommodations cannot be made for missing either the abstract or paper deadline.\n\n### 3. Workshop paper submission opportunities\n\n- **Workshops will be held on November 9, 2026** (the day before the main conference starts on Nov 10).\n- The **Call for Workshops** was announced on April 29, 2026 per the official announcements page.\n- Workshop proposals must be **2-3 pages (max 5 pages)** and focus on interactive, problem-oriented formats.\n- Each workshop can have a maximum of **4 invited speakers**, with each speaker limited to 2 events.\n- Workshop contacts: Danfei Xu (danfei@gatech.edu) and Rudolf Lioutikov (lioutikov@kit.edu).\n- **The specific deadline for workshop proposal submissions is NOT listed** on the public-facing pages I was able to access. You would need to check the submission form linked from the Call for Workshops page or contact the workshop chairs directly.\n- Note: Individual workshop paper deadlines (for papers submitted *to* accepted workshops) would be set by each workshop's organizers after workshop acceptance, and are typically later than the main conference deadline.\n\n### Summary\n\nThe proposal's dates are accurate. All three claimed deadlines/dates match the official sources. No extensions have been announced, and the organizers have stated deadlines are final.\n\n---\n\nSources:\n- [CoRL 2026 Official Website](https://www.corl.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [CoRL 2026 Contributions Page](https://www.corl.org/contributions)\n- [CoRL 2026 Announcements](https://www.corl.org/annoucements)\n- [Hugging Face AI Deadlines - CoRL 2026 Update](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)\n- [Bibby AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)\n- [CoRL 2026 on OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)\n- [CoRL 2026 Call for Workshops (LinkedIn - Danfei Xu)](https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b)"
      }
    ],
    "totalDurationMs": 82673,
    "totalTokens": 20075,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 17373,
      "output_tokens": 1282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1282,
          "cache_read_input_tokens": 17373,
          "cache_creation_input_tokens": 1419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1419,
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
  "sourceToolAssistantUUID": "473bafbe-14f6-4545-97bf-3f3b45f07c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "fbf85230-d7d6-48d8-92bc-2dd346d733cf",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PhaseOT demo quality diagnosis idea (Round 5)",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Tool result

_source line 20 · 2026-05-13T10:50:39.608Z_

<details><summary>↩ Tool result · `toolu_01AwQWq5jeH1z3JsAVCX64QP`</summary>

```text
Now I have a comprehensive picture. Here is my consolidated report.

---

## Comprehensive Literature Search: Competing/Overlapping Work with PhaseOT (2025-2026)

Below is a detailed inventory of recent papers that compete with, overlap with, or are highly relevant to a "PhaseOT" method that uses optimal transport for phase-level demonstration quality diagnosis with mode-aware scoring. Papers are organized by relevance.

---

### TIER 1: DIRECT COMPETITORS -- Demonstration Quality Scoring & Curation (2025-2026)

**1. RINSE -- "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning"**
- **Authors:** Soham Kulkarni, Raayan Dhar, Yuchen Cui (UCLA)
- **Venue/Year:** arXiv:2604.23000, April 2026
- **Summary:** Proposes RINSE (Ranking and INdexing Smooth Examples), a lightweight, policy-architecture-agnostic framework for scoring demonstrations based on trajectory smoothness. Uses two metrics: Spectral Arc Length (SAL, frequency-domain regularity) and Trajectory-Envelope Distance (TED, spatial geometric deviation with phase-boundary/contact awareness). On RoboMimic, SAL filtering achieves 16% higher success with 1/6th of data; on real-world tasks, TED filtering yields 20% improvement with half the data.
- **Overlap with PhaseOT:** HIGH. TED explicitly uses phase-boundary/contact signals, making it partially phase-aware. However, RINSE uses smoothness as a proxy for quality rather than optimal transport, and does not explicitly handle multi-strategy demonstrations. PhaseOT's OT-based scoring and mode-awareness would be differentiated, but RINSE is a very strong baseline to compare against.
- **Source:** [arXiv:2604.23000](https://arxiv.org/abs/2604.23000)

**2. QoQ -- "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning"**
- **Authors:** Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, Kimin Lee
- **Venue/Year:** ICRA 2026 (arXiv:2603.09056, March 2026)
- **Summary:** Uses influence functions to quantify each training sample's contribution to reducing loss on validation demonstrations. Aggregates influence scores at the trajectory level to reduce noise. Addresses human errors and teleoperator variability.
- **Overlap with PhaseOT:** MODERATE-HIGH. Also scores demonstration quality, but operates at trajectory level (not phase level) and uses influence functions (not OT). Does not address multi-strategy demonstrations. PhaseOT's phase-level granularity and mode-awareness are key differentiators.
- **Source:** [arXiv:2603.09056](https://arxiv.org/abs/2603.09056)

**3. SCIZOR -- "A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning"**
- **Authors:** Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, Yuke Zhu (UT Austin, NVIDIA)
- **Venue/Year:** ICRA 2026 (arXiv:2505.22626, May 2025)
- **Summary:** Operates at the state-action pair level (finer than trajectory level). Uses a self-supervised task progress predictor to remove samples lacking task progression, plus a deduplication module. Achieves 15.4% average improvement across benchmarks.
- **Overlap with PhaseOT:** HIGH. SCIZOR's sub-trajectory granularity (state-action pair level) is similar in spirit to PhaseOT's phase-level approach. Its task progress predictor implicitly captures phase-like structure. However, it does not use OT, does not explicitly segment into phases, and does not handle multi-strategy demonstrations.
- **Source:** [arXiv:2505.22626](https://arxiv.org/abs/2505.22626)

**4. DemInf -- "Robot Data Curation with Mutual Information Estimators"**
- **Authors:** Joey Hejna, Suvir Mirchandani, Ashwin Balakrishna, Annie Xie, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Dhruv Shah, Coline Devin, Dorsa Sadigh
- **Venue/Year:** RSS 2025 (arXiv:2502.08623, February 2025)
- **Summary:** Estimates quality of individual demonstrations via mutual information between states and actions using k-NN MI estimators on VAE embeddings. Captures action diversity and state-conditioned action variability. 5-10% improvement on RoboMimic, gains on real ALOHA/Franka.
- **Overlap with PhaseOT:** MODERATE. Also scores individual demonstrations, but uses MI rather than OT, operates at trajectory level (not phase level), and does not explicitly handle multi-strategy demonstrations. An important baseline.
- **Source:** [arXiv:2502.08623](https://arxiv.org/abs/2502.08623)

**5. CUPID -- "Curating Data your Robot Loves with Influence Functions"**
- **Authors:** Christopher Agia, Rohan Sinha, Jingyun Yang, Rika Antonova, Marco Pavone, Haruki Nishimura, Masha Itkina, Jeannette Bohg
- **Venue/Year:** CoRL 2025 (arXiv:2506.19121)
- **Summary:** Uses influence functions to estimate each training demonstration's impact on policy's expected return. Can filter harmful demonstrations and select beneficial new ones. Training with <33% curated data achieves SOTA on RoboMimic. Identifies robust strategies under distribution shift and isolates spurious correlations.
- **Overlap with PhaseOT:** MODERATE. Trajectory-level curation via influence functions. Does not use OT, phase segmentation, or multi-strategy handling. A strong baseline for the "demonstration filtering" aspect.
- **Source:** [arXiv:2506.19121](https://arxiv.org/abs/2506.19121)

**6. DataMIL -- "Selecting Data for Robot Imitation Learning with Datamodels"**
- **Authors:** Shivin Dass, Alaa Khaddaj, Logan Engstrom, Aleksander Madry, Andrew Ilyas, Roberto Martin-Martin (UT Austin, MIT)
- **Venue/Year:** arXiv:2505.09603, May 2025
- **Summary:** Policy-driven data selection framework that directly optimizes data selection for task success rather than using human notions of quality. Validates on 60+ sim and real-world tasks including Open X-Embodiment datasets.
- **Overlap with PhaseOT:** MODERATE. Different philosophy (end-to-end policy-driven selection vs. principled OT-based scoring). Does not use phase segmentation or multi-strategy handling. Important competing approach.
- **Source:** [arXiv:2505.09603](https://arxiv.org/abs/2505.09603)

---

### TIER 2: OPTIMAL TRANSPORT FOR ROBOT LEARNING (Context & Foundations)

**7. TemporalOT -- "Robot Policy Learning with Temporal Optimal Transport Reward"**
- **Authors:** Yuwei Fu, Haichao Zhang, Di Wu, Wei Xu, Benoit Boulet
- **Venue/Year:** NeurIPS 2024 (arXiv:2410.21795)
- **Summary:** Addresses the limitation that standard OT rewards are invariant to temporal order, adding temporal information to OT-based proxy rewards for policy learning from video demonstrations.
- **Overlap with PhaseOT:** MODERATE. Uses OT with temporal awareness, but for reward shaping (not demonstration quality scoring). The insight about temporal order in OT is directly relevant to PhaseOT's phase-level OT approach.
- **Source:** [arXiv:2410.21795](https://arxiv.org/abs/2410.21795)

**8. ROT -- "Watch and Match: Supercharging Imitation with Regularized Optimal Transport"**
- **Authors:** Siddhant Haldar et al.
- **Venue/Year:** CoRL 2022 (arXiv:2206.15469)
- **Summary:** Combines trajectory-matching rewards (via regularized OT) with behavior cloning for few-shot imitation. 7.8x faster imitation to 90% expert performance. 90.1% success on 14 real-world tasks with 1 demo and 1 hour training.
- **Overlap with PhaseOT:** Foundational. ROT uses OT for trajectory matching in reward generation, not for quality scoring or filtering. PhaseOT likely builds on this OT-for-robotics foundation.
- **Source:** [ROT Project Page](https://rot-robot.github.io/)

**9. Zero-Shot Offline Imitation Learning via Optimal Transport**
- **Authors:** Thomas Rupf, Marco Bagatella, Nico Gurtler, Jonas Frey, Georg Martius
- **Venue/Year:** ICML 2025
- **Summary:** Uses OT-based occupancy matching for zero-shot imitation from offline data. Lifts goal-conditioned value functions to distances between occupancies.
- **Overlap with PhaseOT:** LOW-MODERATE. Uses OT for occupancy matching, not demonstration scoring. Different application but same mathematical toolkit.
- **Source:** [ICML 2025 Proceedings](https://proceedings.mlr.press/v267/rupf25a.html)

---

### TIER 3: PHASE/SEGMENT-LEVEL DEMONSTRATION ANALYSIS

**10. "Unsupervised Segmentation and Alignment of Multi-Demonstration Trajectories via Multi-Feature Saliency and Duration-Explicit HSMMs"**
- **Authors:** (Multi-author, published in MDPI Mathematics)
- **Venue/Year:** September 2025, MDPI Mathematics 13(19):3057
- **Summary:** Label-free pipeline coupling unsupervised segmentation with HSMM-based alignment. Uses multi-feature saliency (velocity, acceleration, curvature, direction-change rate) for keyframe extraction. Reduces phase-boundary dispersion by 31% on UAV simulations.
- **Overlap with PhaseOT:** HIGH for the segmentation component. This paper addresses phase boundary detection and cross-demonstration alignment -- exactly the segmentation step that PhaseOT likely needs. However, it does not perform quality scoring or use OT. Could be complementary or a competing segmentation approach.
- **Source:** [MDPI Mathematics](https://www.mdpi.com/2227-7390/13/19/3057)

**11. "Learning from Imperfect Demonstrations via Temporal Behavior Tree-Guided Trajectory Repair"**
- **Authors:** Aniruddh G. Puranic, Sebastian Schirmer, John S. Baras, Calin Belta
- **Venue/Year:** arXiv:2604.04225, April 2026
- **Summary:** Uses Temporal Behavior Trees (TBT) to formally specify task requirements, identify violating trajectory segments, and repair them before policy learning. A repair-based approach rather than filter-based.
- **Overlap with PhaseOT:** MODERATE. Operates on trajectory segments (quasi-phase-level) and handles imperfect demonstrations, but uses formal logic (not OT) and repairs rather than scores/filters demonstrations.
- **Source:** [arXiv:2604.04225](https://arxiv.org/abs/2604.04225)

**12. GR-RL -- "Going Dexterous and Precise for Long-Horizon Robotic Manipulation"**
- **Authors:** ByteDance Seed team
- **Venue/Year:** arXiv:2512.01801, December 2025
- **Summary:** Multi-stage pipeline that filters, augments, and reinforces demonstrations via RL. Learns a vision-language-conditioned task progress function, filters transitions that contribute positively to progress. Boosts shoe-lacing success from 45.7% to 83.3%.
- **Overlap with PhaseOT:** MODERATE. Uses task-progress-based transition-level filtering (somewhat analogous to phase-aware scoring). However, it filters transitions, not phases, and does not use OT. The task progress predictor is conceptually similar to SCIZOR's.
- **Source:** [arXiv:2512.01801](https://arxiv.org/abs/2512.01801)

**13. "Learning a Thousand Tasks in a Day"**
- **Venue/Year:** arXiv:2511.10110, November 2025
- **Summary:** Decomposes manipulation trajectories into sequential alignment and interaction phases. Studies retrieval-based generalization. Through 3,450 real-world rollouts, systematically examines how phase decomposition compares to monolithic single-phase BC policies.
- **Overlap with PhaseOT:** MODERATE. Phase decomposition is relevant, but the focus is on learning efficiency from phases rather than quality scoring of phases.
- **Source:** [arXiv:2511.10110](https://arxiv.org/abs/2511.10110)

---

### TIER 4: MULTI-MODAL/MULTI-STRATEGY HANDLING

**14. Re-Mix -- "Optimizing Data Mixtures for Large Scale Imitation Learning"**
- **Authors:** Joey Hejna, Chethan Bhateja, Yichen Jiang, Karl Pertsch, Dorsa Sadigh
- **Venue/Year:** arXiv:2408.14037, August 2024
- **Summary:** Uses distributionally robust optimization (DRO) to weigh different subsets/domains of robotics datasets for foundation model pre-training. Addresses variability across datasets.
- **Overlap with PhaseOT:** LOW-MODERATE. Addresses data mixture optimization at dataset level, not phase-level or demonstration-level quality. But relevant for the "handling diverse data sources" angle.
- **Source:** [arXiv:2408.14037](https://arxiv.org/abs/2408.14037)

**15. WSMIL -- "Weakly Supervised Multi-modal Imitation Learning from Incompletely Labeled Demonstrations"**
- **Venue/Year:** Neural Networks, 2025
- **Summary:** Introduces a mode classifier combined with generator/discriminator to learn from demonstrations with incomplete modal labels, addressing the challenge of multi-modal behavior modes.
- **Overlap with PhaseOT:** MODERATE for the multi-modality aspect. Addresses multi-modal behavior modes directly, but focuses on learning (not curation/scoring). Relevant as context for mode-aware approaches.
- **Source:** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0893608025009785)

---

### KEY GAPS THAT PhaseOT COULD UNIQUELY FILL

Based on this comprehensive search, here are the novel aspects of PhaseOT that appear to be genuinely unaddressed by existing work:

1. **No existing paper combines OT with phase-level demonstration quality scoring.** TemporalOT and ROT use OT for reward shaping, not quality scoring. The quality scoring papers (RINSE, QoQ, CUPID, DemInf, SCIZOR) do not use OT.

2. **Mode-aware scoring is novel.** No existing curation method explicitly clusters demonstrations by strategy/mode before scoring. WSMIL handles multi-modal learning but not quality scoring. DemInf's MI captures some action diversity but doesn't explicitly identify modes.

3. **The combination of changepoint detection + OT scoring is novel.** The HSMM segmentation paper handles phase detection but not quality scoring. The quality scoring papers don't use changepoint detection for segmentation.

4. **However, the field is rapidly crowding.** The 2025-2026 period has seen an explosion of demonstration curation methods (QoQ, SCIZOR, CUPID, DemInf, DataMIL, RINSE, GR-RL). PhaseOT will need to clearly benchmark against these recent baselines, especially RINSE (which has partial phase awareness via TED's contact signals) and SCIZOR (which operates at sub-trajectory granularity).

### PAPERS THE PROPOSAL MAY HAVE MISSED

The most critical papers to cite and compare against are:
- **RINSE** (April 2026) -- very recent, smoothness-based scoring with partial phase-boundary awareness
- **QoQ** (March 2026) -- influence-function-based curation, accepted at ICRA 2026
- **SCIZOR** (May 2025, ICRA 2026) -- sub-trajectory-level curation via task progress prediction
- **DemInf** (Feb 2025, RSS 2025) -- MI-based demonstration quality estimation
- **CUPID** (CoRL 2025) -- influence-function-based curation
- **DataMIL** (May 2025) -- policy-driven data selection via datamodels
- **TemporalOT** (NeurIPS 2024) -- temporal awareness in OT for robotics (foundational for PhaseOT's OT approach)
- **HSMM segmentation paper** (Sep 2025) -- competing phase segmentation approach
- **TBT Trajectory Repair** (April 2026) -- segment-level demonstration repair

agentId: a033773dc829c2a73 (use SendMessage with to: 'a033773dc829c2a73' to continue this agent)
&lt;usage>total_tokens: 44369
tool_uses: 38
duration_ms: 197411&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d8c5214-e8b1-486b-9c6b-a87b7417c669",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "6a5c3839-fbb7-4f6f-b254-e947542d19a0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for recent (2025-2026) papers on demonstration quality assessment, data curation for robot learning, and related topics that might compete with or overlap with a method called \"PhaseOT\" that uses optimal transport for phase-level demonstration quality diagnosis with mode-aware scoring.\n\nSpecifically search for:\n1. Any papers using optimal transport for robot demonstration filtering or scoring (2025-2026)\n2. Papers on phase-level or segment-level demonstration quality assessment\n3. Papers on multimodal/multi-strategy demonstration handling in imitation learning\n4. Papers combining changepoint detection with quality scoring for demonstrations\n5. Any very recent demo curation papers from 2026\n\nUse these search queries:\n- \"demonstration quality\" \"optimal transport\" robot 2025 2026 site:arxiv.org\n- \"phase-level\" OR \"segment-level\" demonstration curation robot 2025 2026\n- \"multimodal demonstrations\" filtering quality imitation learning 2025 2026\n- \"demonstration curation\" robot learning 2026 site:arxiv.org\n- \"data quality\" \"imitation learning\" scoring filtering 2026\n- site:arxiv.org robot demonstration noise filtering reinforcement learning 2025 2026\n- \"trajectory quality\" robot learning optimal transport\n\nFor any papers found, report: title, authors, venue, year, and a brief summary of how they relate to PhaseOT's approach. Focus on finding work the proposal may have MISSED.",
    "agentId": "a033773dc829c2a73",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my consolidated report.\n\n---\n\n## Comprehensive Literature Search: Competing/Overlapping Work with PhaseOT (2025-2026)\n\nBelow is a detailed inventory of recent papers that compete with, overlap with, or are highly relevant to a \"PhaseOT\" method that uses optimal transport for phase-level demonstration quality diagnosis with mode-aware scoring. Papers are organized by relevance.\n\n---\n\n### TIER 1: DIRECT COMPETITORS -- Demonstration Quality Scoring & Curation (2025-2026)\n\n**1. RINSE -- \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning\"**\n- **Authors:** Soham Kulkarni, Raayan Dhar, Yuchen Cui (UCLA)\n- **Venue/Year:** arXiv:2604.23000, April 2026\n- **Summary:** Proposes RINSE (Ranking and INdexing Smooth Examples), a lightweight, policy-architecture-agnostic framework for scoring demonstrations based on trajectory smoothness. Uses two metrics: Spectral Arc Length (SAL, frequency-domain regularity) and Trajectory-Envelope Distance (TED, spatial geometric deviation with phase-boundary/contact awareness). On RoboMimic, SAL filtering achieves 16% higher success with 1/6th of data; on real-world tasks, TED filtering yields 20% improvement with half the data.\n- **Overlap with PhaseOT:** HIGH. TED explicitly uses phase-boundary/contact signals, making it partially phase-aware. However, RINSE uses smoothness as a proxy for quality rather than optimal transport, and does not explicitly handle multi-strategy demonstrations. PhaseOT's OT-based scoring and mode-awareness would be differentiated, but RINSE is a very strong baseline to compare against.\n- **Source:** [arXiv:2604.23000](https://arxiv.org/abs/2604.23000)\n\n**2. QoQ -- \"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning\"**\n- **Authors:** Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, Kimin Lee\n- **Venue/Year:** ICRA 2026 (arXiv:2603.09056, March 2026)\n- **Summary:** Uses influence functions to quantify each training sample's contribution to reducing loss on validation demonstrations. Aggregates influence scores at the trajectory level to reduce noise. Addresses human errors and teleoperator variability.\n- **Overlap with PhaseOT:** MODERATE-HIGH. Also scores demonstration quality, but operates at trajectory level (not phase level) and uses influence functions (not OT). Does not address multi-strategy demonstrations. PhaseOT's phase-level granularity and mode-awareness are key differentiators.\n- **Source:** [arXiv:2603.09056](https://arxiv.org/abs/2603.09056)\n\n**3. SCIZOR -- \"A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning\"**\n- **Authors:** Yu Zhang, Yuqi Xie, Huihan Liu, Rutav Shah, Michael Wan, Linxi Fan, Yuke Zhu (UT Austin, NVIDIA)\n- **Venue/Year:** ICRA 2026 (arXiv:2505.22626, May 2025)\n- **Summary:** Operates at the state-action pair level (finer than trajectory level). Uses a self-supervised task progress predictor to remove samples lacking task progression, plus a deduplication module. Achieves 15.4% average improvement across benchmarks.\n- **Overlap with PhaseOT:** HIGH. SCIZOR's sub-trajectory granularity (state-action pair level) is similar in spirit to PhaseOT's phase-level approach. Its task progress predictor implicitly captures phase-like structure. However, it does not use OT, does not explicitly segment into phases, and does not handle multi-strategy demonstrations.\n- **Source:** [arXiv:2505.22626](https://arxiv.org/abs/2505.22626)\n\n**4. DemInf -- \"Robot Data Curation with Mutual Information Estimators\"**\n- **Authors:** Joey Hejna, Suvir Mirchandani, Ashwin Balakrishna, Annie Xie, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Dhruv Shah, Coline Devin, Dorsa Sadigh\n- **Venue/Year:** RSS 2025 (arXiv:2502.08623, February 2025)\n- **Summary:** Estimates quality of individual demonstrations via mutual information between states and actions using k-NN MI estimators on VAE embeddings. Captures action diversity and state-conditioned action variability. 5-10% improvement on RoboMimic, gains on real ALOHA/Franka.\n- **Overlap with PhaseOT:** MODERATE. Also scores individual demonstrations, but uses MI rather than OT, operates at trajectory level (not phase level), and does not explicitly handle multi-strategy demonstrations. An important baseline.\n- **Source:** [arXiv:2502.08623](https://arxiv.org/abs/2502.08623)\n\n**5. CUPID -- \"Curating Data your Robot Loves with Influence Functions\"**\n- **Authors:** Christopher Agia, Rohan Sinha, Jingyun Yang, Rika Antonova, Marco Pavone, Haruki Nishimura, Masha Itkina, Jeannette Bohg\n- **Venue/Year:** CoRL 2025 (arXiv:2506.19121)\n- **Summary:** Uses influence functions to estimate each training demonstration's impact on policy's expected return. Can filter harmful demonstrations and select beneficial new ones. Training with <33% curated data achieves SOTA on RoboMimic. Identifies robust strategies under distribution shift and isolates spurious correlations.\n- **Overlap with PhaseOT:** MODERATE. Trajectory-level curation via influence functions. Does not use OT, phase segmentation, or multi-strategy handling. A strong baseline for the \"demonstration filtering\" aspect.\n- **Source:** [arXiv:2506.19121](https://arxiv.org/abs/2506.19121)\n\n**6. DataMIL -- \"Selecting Data for Robot Imitation Learning with Datamodels\"**\n- **Authors:** Shivin Dass, Alaa Khaddaj, Logan Engstrom, Aleksander Madry, Andrew Ilyas, Roberto Martin-Martin (UT Austin, MIT)\n- **Venue/Year:** arXiv:2505.09603, May 2025\n- **Summary:** Policy-driven data selection framework that directly optimizes data selection for task success rather than using human notions of quality. Validates on 60+ sim and real-world tasks including Open X-Embodiment datasets.\n- **Overlap with PhaseOT:** MODERATE. Different philosophy (end-to-end policy-driven selection vs. principled OT-based scoring). Does not use phase segmentation or multi-strategy handling. Important competing approach.\n- **Source:** [arXiv:2505.09603](https://arxiv.org/abs/2505.09603)\n\n---\n\n### TIER 2: OPTIMAL TRANSPORT FOR ROBOT LEARNING (Context & Foundations)\n\n**7. TemporalOT -- \"Robot Policy Learning with Temporal Optimal Transport Reward\"**\n- **Authors:** Yuwei Fu, Haichao Zhang, Di Wu, Wei Xu, Benoit Boulet\n- **Venue/Year:** NeurIPS 2024 (arXiv:2410.21795)\n- **Summary:** Addresses the limitation that standard OT rewards are invariant to temporal order, adding temporal information to OT-based proxy rewards for policy learning from video demonstrations.\n- **Overlap with PhaseOT:** MODERATE. Uses OT with temporal awareness, but for reward shaping (not demonstration quality scoring). The insight about temporal order in OT is directly relevant to PhaseOT's phase-level OT approach.\n- **Source:** [arXiv:2410.21795](https://arxiv.org/abs/2410.21795)\n\n**8. ROT -- \"Watch and Match: Supercharging Imitation with Regularized Optimal Transport\"**\n- **Authors:** Siddhant Haldar et al.\n- **Venue/Year:** CoRL 2022 (arXiv:2206.15469)\n- **Summary:** Combines trajectory-matching rewards (via regularized OT) with behavior cloning for few-shot imitation. 7.8x faster imitation to 90% expert performance. 90.1% success on 14 real-world tasks with 1 demo and 1 hour training.\n- **Overlap with PhaseOT:** Foundational. ROT uses OT for trajectory matching in reward generation, not for quality scoring or filtering. PhaseOT likely builds on this OT-for-robotics foundation.\n- **Source:** [ROT Project Page](https://rot-robot.github.io/)\n\n**9. Zero-Shot Offline Imitation Learning via Optimal Transport**\n- **Authors:** Thomas Rupf, Marco Bagatella, Nico Gurtler, Jonas Frey, Georg Martius\n- **Venue/Year:** ICML 2025\n- **Summary:** Uses OT-based occupancy matching for zero-shot imitation from offline data. Lifts goal-conditioned value functions to distances between occupancies.\n- **Overlap with PhaseOT:** LOW-MODERATE. Uses OT for occupancy matching, not demonstration scoring. Different application but same mathematical toolkit.\n- **Source:** [ICML 2025 Proceedings](https://proceedings.mlr.press/v267/rupf25a.html)\n\n---\n\n### TIER 3: PHASE/SEGMENT-LEVEL DEMONSTRATION ANALYSIS\n\n**10. \"Unsupervised Segmentation and Alignment of Multi-Demonstration Trajectories via Multi-Feature Saliency and Duration-Explicit HSMMs\"**\n- **Authors:** (Multi-author, published in MDPI Mathematics)\n- **Venue/Year:** September 2025, MDPI Mathematics 13(19):3057\n- **Summary:** Label-free pipeline coupling unsupervised segmentation with HSMM-based alignment. Uses multi-feature saliency (velocity, acceleration, curvature, direction-change rate) for keyframe extraction. Reduces phase-boundary dispersion by 31% on UAV simulations.\n- **Overlap with PhaseOT:** HIGH for the segmentation component. This paper addresses phase boundary detection and cross-demonstration alignment -- exactly the segmentation step that PhaseOT likely needs. However, it does not perform quality scoring or use OT. Could be complementary or a competing segmentation approach.\n- **Source:** [MDPI Mathematics](https://www.mdpi.com/2227-7390/13/19/3057)\n\n**11. \"Learning from Imperfect Demonstrations via Temporal Behavior Tree-Guided Trajectory Repair\"**\n- **Authors:** Aniruddh G. Puranic, Sebastian Schirmer, John S. Baras, Calin Belta\n- **Venue/Year:** arXiv:2604.04225, April 2026\n- **Summary:** Uses Temporal Behavior Trees (TBT) to formally specify task requirements, identify violating trajectory segments, and repair them before policy learning. A repair-based approach rather than filter-based.\n- **Overlap with PhaseOT:** MODERATE. Operates on trajectory segments (quasi-phase-level) and handles imperfect demonstrations, but uses formal logic (not OT) and repairs rather than scores/filters demonstrations.\n- **Source:** [arXiv:2604.04225](https://arxiv.org/abs/2604.04225)\n\n**12. GR-RL -- \"Going Dexterous and Precise for Long-Horizon Robotic Manipulation\"**\n- **Authors:** ByteDance Seed team\n- **Venue/Year:** arXiv:2512.01801, December 2025\n- **Summary:** Multi-stage pipeline that filters, augments, and reinforces demonstrations via RL. Learns a vision-language-conditioned task progress function, filters transitions that contribute positively to progress. Boosts shoe-lacing success from 45.7% to 83.3%.\n- **Overlap with PhaseOT:** MODERATE. Uses task-progress-based transition-level filtering (somewhat analogous to phase-aware scoring). However, it filters transitions, not phases, and does not use OT. The task progress predictor is conceptually similar to SCIZOR's.\n- **Source:** [arXiv:2512.01801](https://arxiv.org/abs/2512.01801)\n\n**13. \"Learning a Thousand Tasks in a Day\"**\n- **Venue/Year:** arXiv:2511.10110, November 2025\n- **Summary:** Decomposes manipulation trajectories into sequential alignment and interaction phases. Studies retrieval-based generalization. Through 3,450 real-world rollouts, systematically examines how phase decomposition compares to monolithic single-phase BC policies.\n- **Overlap with PhaseOT:** MODERATE. Phase decomposition is relevant, but the focus is on learning efficiency from phases rather than quality scoring of phases.\n- **Source:** [arXiv:2511.10110](https://arxiv.org/abs/2511.10110)\n\n---\n\n### TIER 4: MULTI-MODAL/MULTI-STRATEGY HANDLING\n\n**14. Re-Mix -- \"Optimizing Data Mixtures for Large Scale Imitation Learning\"**\n- **Authors:** Joey Hejna, Chethan Bhateja, Yichen Jiang, Karl Pertsch, Dorsa Sadigh\n- **Venue/Year:** arXiv:2408.14037, August 2024\n- **Summary:** Uses distributionally robust optimization (DRO) to weigh different subsets/domains of robotics datasets for foundation model pre-training. Addresses variability across datasets.\n- **Overlap with PhaseOT:** LOW-MODERATE. Addresses data mixture optimization at dataset level, not phase-level or demonstration-level quality. But relevant for the \"handling diverse data sources\" angle.\n- **Source:** [arXiv:2408.14037](https://arxiv.org/abs/2408.14037)\n\n**15. WSMIL -- \"Weakly Supervised Multi-modal Imitation Learning from Incompletely Labeled Demonstrations\"**\n- **Venue/Year:** Neural Networks, 2025\n- **Summary:** Introduces a mode classifier combined with generator/discriminator to learn from demonstrations with incomplete modal labels, addressing the challenge of multi-modal behavior modes.\n- **Overlap with PhaseOT:** MODERATE for the multi-modality aspect. Addresses multi-modal behavior modes directly, but focuses on learning (not curation/scoring). Relevant as context for mode-aware approaches.\n- **Source:** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0893608025009785)\n\n---\n\n### KEY GAPS THAT PhaseOT COULD UNIQUELY FILL\n\nBased on this comprehensive search, here are the novel aspects of PhaseOT that appear to be genuinely unaddressed by existing work:\n\n1. **No existing paper combines OT with phase-level demonstration quality scoring.** TemporalOT and ROT use OT for reward shaping, not quality scoring. The quality scoring papers (RINSE, QoQ, CUPID, DemInf, SCIZOR) do not use OT.\n\n2. **Mode-aware scoring is novel.** No existing curation method explicitly clusters demonstrations by strategy/mode before scoring. WSMIL handles multi-modal learning but not quality scoring. DemInf's MI captures some action diversity but doesn't explicitly identify modes.\n\n3. **The combination of changepoint detection + OT scoring is novel.** The HSMM segmentation paper handles phase detection but not quality scoring. The quality scoring papers don't use changepoint detection for segmentation.\n\n4. **However, the field is rapidly crowding.** The 2025-2026 period has seen an explosion of demonstration curation methods (QoQ, SCIZOR, CUPID, DemInf, DataMIL, RINSE, GR-RL). PhaseOT will need to clearly benchmark against these recent baselines, especially RINSE (which has partial phase awareness via TED's contact signals) and SCIZOR (which operates at sub-trajectory granularity).\n\n### PAPERS THE PROPOSAL MAY HAVE MISSED\n\nThe most critical papers to cite and compare against are:\n- **RINSE** (April 2026) -- very recent, smoothness-based scoring with partial phase-boundary awareness\n- **QoQ** (March 2026) -- influence-function-based curation, accepted at ICRA 2026\n- **SCIZOR** (May 2025, ICRA 2026) -- sub-trajectory-level curation via task progress prediction\n- **DemInf** (Feb 2025, RSS 2025) -- MI-based demonstration quality estimation\n- **CUPID** (CoRL 2025) -- influence-function-based curation\n- **DataMIL** (May 2025) -- policy-driven data selection via datamodels\n- **TemporalOT** (NeurIPS 2024) -- temporal awareness in OT for robotics (foundational for PhaseOT's OT approach)\n- **HSMM segmentation paper** (Sep 2025) -- competing phase segmentation approach\n- **TBT Trajectory Repair** (April 2026) -- segment-level demonstration repair"
      }
    ],
    "totalDurationMs": 197411,
    "totalTokens": 44369,
    "totalToolUseCount": 38,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3890,
      "cache_read_input_tokens": 36209,
      "output_tokens": 4269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3890
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4269,
          "cache_read_input_tokens": 36209,
          "cache_creation_input_tokens": 3890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3890,
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
      "otherToolCount": 38
    }
  },
  "sourceToolAssistantUUID": "0d8c5214-e8b1-486b-9c6b-a87b7417c669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
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
  "leafUuid": "6a5c3839-fbb7-4f6f-b254-e947542d19a0",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PhaseOT demo quality diagnosis idea (Round 5)",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Assistant

_source line 23 · 2026-05-13T10:50:43.241Z_

Good. CIQL is verified as real. CoRL 2026 deadlines confirmed (13 days to abstract, 16 days to paper). Now let me do deeper verification on the novelty claims and check for the most critical potential overlaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a5c3839-fbb7-4f6f-b254-e947542d19a0",
  "isSidechain": false,
  "requestId": "req_011CazSSoU5pwSJd7k3MNEFr",
  "type": "assistant",
  "uuid": "db4352cd-f588-42c3-ba92-b6a6e5c0e935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtCqbiAeASyBhMLTrWb9zR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1383,
      "cache_creation_input_tokens": 5977,
      "cache_read_input_tokens": 38583,
      "output_tokens": 713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1383,
          "output_tokens": 713,
          "cache_read_input_tokens": 38583,
          "cache_creation_input_tokens": 5977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5977
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

_source line 24 · 2026-05-13T10:50:51.151Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Qcxz2xP8pVg1xUeeKpjzAH`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search FIDeL and Pallage OT papers",
  "prompt": "Search for these two papers and read their content to assess overlap with a proposed method \"PhaseOT\" that uses phase-structured Wasserstein distances for demonstration quality diagnosis:\n\n1. \"FIDeL: Failure Identification in Demonstration Learning via OT\" - claimed to use OT for per-timestep anomaly scoring but for deployment monitoring, not curation. Verify this claim and check if there is more overlap than stated.\n\n2. Pallage 2025 (arXiv 2504.12918) - claimed to use \"Sliced-Wasserstein for point-level outlier detection on static point clouds, no temporal structure.\" Verify this.\n\nSearch queries:\n- \"FIDeL failure identification demonstration learning optimal transport\"\n- site:arxiv.org 2504.12918\n- \"sliced wasserstein\" data selection filtering 2025\n- \"FIDeL\" robot imitation learning OT anomaly\n\nUse WebSearch and WebFetch to read the actual papers. Focus on whether these papers are closer to PhaseOT than the proposal admits."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4352cd-f588-42c3-ba92-b6a6e5c0e935",
  "isSidechain": false,
  "requestId": "req_011CazSSoU5pwSJd7k3MNEFr",
  "type": "assistant",
  "uuid": "24392469-c5bb-4af0-b1ca-fa10f11cd413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtCqbiAeASyBhMLTrWb9zR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1383,
      "cache_creation_input_tokens": 5977,
      "cache_read_input_tokens": 38583,
      "output_tokens": 713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1383,
          "output_tokens": 713,
          "cache_read_input_tokens": 38583,
          "cache_creation_input_tokens": 5977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5977
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

_source line 25 · 2026-05-13T10:50:56.803Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ve6UhVM8vcngZjc8mFb3Mq`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check Shi et al spatial/velocity multimodality",
  "prompt": "Search for the paper by Shi et al. (arXiv, July 2025) titled something like \"Is Diversity All You Need for Scalable Robotic Manipulation?\" which claims to distinguish between spatial multimodality (different paths, beneficial) and velocity multimodality (different speeds, harmful) in robot demonstrations, yielding a 15% improvement from velocity debiasing.\n\nVerify:\n1. Does this paper exist with these claims?\n2. Does it actually show 15% improvement from velocity debiasing alone?\n3. Does it operate at a phase level or trajectory level?\n4. Could its velocity debiasing be considered a simpler alternative to PhaseOT's mode-aware scoring?\n\nSearch using:\n- \"Is Diversity All You Need\" \"Scalable Robotic Manipulation\" Shi 2025\n- \"spatial multimodality\" \"velocity multimodality\" robot demonstrations\n- site:arxiv.org Shi diversity robotic manipulation 2025\n\nUse WebSearch and WebFetch to find and read the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24392469-c5bb-4af0-b1ca-fa10f11cd413",
  "isSidechain": false,
  "requestId": "req_011CazSSoU5pwSJd7k3MNEFr",
  "type": "assistant",
  "uuid": "7ae44d84-8d98-44c4-8633-6898f45b2c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtCqbiAeASyBhMLTrWb9zR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1383,
      "cache_creation_input_tokens": 5977,
      "cache_read_input_tokens": 38583,
      "output_tokens": 713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1383,
          "output_tokens": 713,
          "cache_read_input_tokens": 38583,
          "cache_creation_input_tokens": 5977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5977
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

_source line 26 · 2026-05-13T10:52:18.482Z_

<details><summary>↩ Tool result · `toolu_01Ve6UhVM8vcngZjc8mFb3Mq`</summary>

```text
I now have comprehensive information to provide a thorough answer. Here are my findings:

---

## Verification Results

### 1. Does this paper exist with these claims?

**Yes, confirmed.** The paper is:

**"Is Diversity All You Need for Scalable Robotic Manipulation?"** by Modi Shi, Li Chen, Jin Chen, Yuxiang Lu, Chiming Liu, Guanghui Ren, Ping Luo, Di Huang, Maoqing Yao, and Hongyang Li. Published on arXiv in July 2025 as [arXiv:2507.06219](https://arxiv.org/abs/2507.06219).

The paper does indeed distinguish between **spatial multimodality** and **velocity multimodality** in robot demonstrations:

- **Spatial multimodality**: Different trajectory choices (e.g., approaching a target from the left vs. right side), representing meaningful alternative strategies that should be preserved.
- **Velocity multimodality**: Robots executing similar trajectories at different speeds, generating different demonstration profiles over time. The paper treats this as harmful noise rather than meaningful variation.

These definitions match your description accurately.

### 2. Does it actually show 15% improvement from velocity debiasing alone?

**Yes, confirmed.** The paper reports a 15% overall improvement (from 0.46 to 0.53 score) using their distribution debiasing method in the pre-training + fine-tuning setting. They frame this as "equivalent to using 2.5x pre-training data." Some individual tasks showed much larger gains (e.g., Pour Water: +60%, Fold Shorts: +23%).

The debiasing method works as follows:
- A **Velocity Model (VM)** is trained to predict expected velocity from observations using MSE loss.
- For each training sample, the method determines the optimal chunk length L by minimizing the difference between the VM's predicted velocity and the actual velocity of the action chunk.
- **Temporal rescaling via interpolation** transforms misaligned chunks into a target chunk size T.
- The search range is constrained to [0.5T, 1.5T] for stability.
- Velocity is measured as the L1 norm of end-effector displacement.

### 3. Does it operate at a phase level or trajectory level?

**It operates at the trajectory chunk level** -- neither purely at the whole-trajectory level nor at a "phase" level in the sense of task phase segmentation. The method works within individual action chunks during training: for each observation-action pair, it adaptively adjusts the chunk length based on predicted velocity, then rescales the chunk via interpolation. This is a local, per-chunk operation within a trajectory, not a global trajectory-level normalization.

The paper explicitly rejects two simpler alternatives:
- **Uniform velocity normalization** (fails because different tasks require different speeds)
- **Episode-level temporal normalization** (cannot eliminate within-trajectory speed variation)

### 4. Could its velocity debiasing be considered a simpler alternative to PhaseOT's mode-aware scoring?

**Partially, but with important caveats.** Here is the analysis:

**Arguments for "simpler alternative":**
- The velocity debiasing method is conceptually straightforward: train a velocity predictor, adaptively rescale action chunks to normalize speed variation. It requires no optimal transport computation, no explicit mode identification, and no complex scoring mechanism.
- It addresses a similar underlying problem -- that demonstrations of the same task can vary in ways that confuse policy learning -- but through a much narrower lens (speed normalization only).
- The 15% improvement is substantial and achieved with a relatively simple intervention.

**Arguments against treating it as a true alternative:**
- The paper contains **no mention whatsoever** of phase alignment, optimal transport, mode-aware methods, or PhaseOT. These are simply not in its problem formulation or related work.
- The method only addresses **velocity variation** (speed differences). It explicitly preserves spatial multimodality and does not attempt to score, rank, or select among different demonstration modes. PhaseOT's mode-aware scoring presumably handles the broader problem of identifying and weighting distinct behavioral modes.
- The velocity debiasing is a **data preprocessing/augmentation** technique (rescaling chunks during training), whereas mode-aware scoring is a **demonstration selection/weighting** technique. They operate at fundamentally different stages of the pipeline.
- A method like PhaseOT that does mode-aware scoring could potentially handle both spatial mode selection AND velocity variation, making it more general even if more complex.

**Bottom line:** Shi et al.'s velocity debiasing is a simpler, narrower intervention that addresses one specific source of harmful variation in demonstrations. It could complement a mode-aware approach like PhaseOT rather than replace it. If the dominant source of demonstration noise in a particular setting happens to be speed variation, the velocity debiasing alone might capture most of the benefit. But for settings where spatial mode selection also matters (choosing which demonstrations are most relevant), it would not substitute for mode-aware scoring.

---

Sources:
- [arXiv:2507.06219 - Is Diversity All You Need for Scalable Robotic Manipulation?](https://arxiv.org/abs/2507.06219)
- [Full HTML version of the paper](https://arxiv.org/html/2507.06219v1)
- [Semantic Scholar entry](https://www.semanticscholar.org/paper/16cfd4479dcdbf21c40b600afebd0db945925752)
- [alphaXiv discussion](https://www.alphaxiv.org/overview/2507.06219v1)

agentId: a60c9ead37d4e8442 (use SendMessage with to: 'a60c9ead37d4e8442' to continue this agent)
&lt;usage>total_tokens: 18422
tool_uses: 9
duration_ms: 81676&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ae44d84-8d98-44c4-8633-6898f45b2c97",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "b5846393-f43d-44e6-80cf-f1bd8e01c9ef",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the paper by Shi et al. (arXiv, July 2025) titled something like \"Is Diversity All You Need for Scalable Robotic Manipulation?\" which claims to distinguish between spatial multimodality (different paths, beneficial) and velocity multimodality (different speeds, harmful) in robot demonstrations, yielding a 15% improvement from velocity debiasing.\n\nVerify:\n1. Does this paper exist with these claims?\n2. Does it actually show 15% improvement from velocity debiasing alone?\n3. Does it operate at a phase level or trajectory level?\n4. Could its velocity debiasing be considered a simpler alternative to PhaseOT's mode-aware scoring?\n\nSearch using:\n- \"Is Diversity All You Need\" \"Scalable Robotic Manipulation\" Shi 2025\n- \"spatial multimodality\" \"velocity multimodality\" robot demonstrations\n- site:arxiv.org Shi diversity robotic manipulation 2025\n\nUse WebSearch and WebFetch to find and read the paper.",
    "agentId": "a60c9ead37d4e8442",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a thorough answer. Here are my findings:\n\n---\n\n## Verification Results\n\n### 1. Does this paper exist with these claims?\n\n**Yes, confirmed.** The paper is:\n\n**\"Is Diversity All You Need for Scalable Robotic Manipulation?\"** by Modi Shi, Li Chen, Jin Chen, Yuxiang Lu, Chiming Liu, Guanghui Ren, Ping Luo, Di Huang, Maoqing Yao, and Hongyang Li. Published on arXiv in July 2025 as [arXiv:2507.06219](https://arxiv.org/abs/2507.06219).\n\nThe paper does indeed distinguish between **spatial multimodality** and **velocity multimodality** in robot demonstrations:\n\n- **Spatial multimodality**: Different trajectory choices (e.g., approaching a target from the left vs. right side), representing meaningful alternative strategies that should be preserved.\n- **Velocity multimodality**: Robots executing similar trajectories at different speeds, generating different demonstration profiles over time. The paper treats this as harmful noise rather than meaningful variation.\n\nThese definitions match your description accurately.\n\n### 2. Does it actually show 15% improvement from velocity debiasing alone?\n\n**Yes, confirmed.** The paper reports a 15% overall improvement (from 0.46 to 0.53 score) using their distribution debiasing method in the pre-training + fine-tuning setting. They frame this as \"equivalent to using 2.5x pre-training data.\" Some individual tasks showed much larger gains (e.g., Pour Water: +60%, Fold Shorts: +23%).\n\nThe debiasing method works as follows:\n- A **Velocity Model (VM)** is trained to predict expected velocity from observations using MSE loss.\n- For each training sample, the method determines the optimal chunk length L by minimizing the difference between the VM's predicted velocity and the actual velocity of the action chunk.\n- **Temporal rescaling via interpolation** transforms misaligned chunks into a target chunk size T.\n- The search range is constrained to [0.5T, 1.5T] for stability.\n- Velocity is measured as the L1 norm of end-effector displacement.\n\n### 3. Does it operate at a phase level or trajectory level?\n\n**It operates at the trajectory chunk level** -- neither purely at the whole-trajectory level nor at a \"phase\" level in the sense of task phase segmentation. The method works within individual action chunks during training: for each observation-action pair, it adaptively adjusts the chunk length based on predicted velocity, then rescales the chunk via interpolation. This is a local, per-chunk operation within a trajectory, not a global trajectory-level normalization.\n\nThe paper explicitly rejects two simpler alternatives:\n- **Uniform velocity normalization** (fails because different tasks require different speeds)\n- **Episode-level temporal normalization** (cannot eliminate within-trajectory speed variation)\n\n### 4. Could its velocity debiasing be considered a simpler alternative to PhaseOT's mode-aware scoring?\n\n**Partially, but with important caveats.** Here is the analysis:\n\n**Arguments for \"simpler alternative\":**\n- The velocity debiasing method is conceptually straightforward: train a velocity predictor, adaptively rescale action chunks to normalize speed variation. It requires no optimal transport computation, no explicit mode identification, and no complex scoring mechanism.\n- It addresses a similar underlying problem -- that demonstrations of the same task can vary in ways that confuse policy learning -- but through a much narrower lens (speed normalization only).\n- The 15% improvement is substantial and achieved with a relatively simple intervention.\n\n**Arguments against treating it as a true alternative:**\n- The paper contains **no mention whatsoever** of phase alignment, optimal transport, mode-aware methods, or PhaseOT. These are simply not in its problem formulation or related work.\n- The method only addresses **velocity variation** (speed differences). It explicitly preserves spatial multimodality and does not attempt to score, rank, or select among different demonstration modes. PhaseOT's mode-aware scoring presumably handles the broader problem of identifying and weighting distinct behavioral modes.\n- The velocity debiasing is a **data preprocessing/augmentation** technique (rescaling chunks during training), whereas mode-aware scoring is a **demonstration selection/weighting** technique. They operate at fundamentally different stages of the pipeline.\n- A method like PhaseOT that does mode-aware scoring could potentially handle both spatial mode selection AND velocity variation, making it more general even if more complex.\n\n**Bottom line:** Shi et al.'s velocity debiasing is a simpler, narrower intervention that addresses one specific source of harmful variation in demonstrations. It could complement a mode-aware approach like PhaseOT rather than replace it. If the dominant source of demonstration noise in a particular setting happens to be speed variation, the velocity debiasing alone might capture most of the benefit. But for settings where spatial mode selection also matters (choosing which demonstrations are most relevant), it would not substitute for mode-aware scoring.\n\n---\n\nSources:\n- [arXiv:2507.06219 - Is Diversity All You Need for Scalable Robotic Manipulation?](https://arxiv.org/abs/2507.06219)\n- [Full HTML version of the paper](https://arxiv.org/html/2507.06219v1)\n- [Semantic Scholar entry](https://www.semanticscholar.org/paper/16cfd4479dcdbf21c40b600afebd0db945925752)\n- [alphaXiv discussion](https://www.alphaxiv.org/overview/2507.06219v1)"
      }
    ],
    "totalDurationMs": 81676,
    "totalTokens": 18422,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1441,
      "cache_read_input_tokens": 15680,
      "output_tokens": 1300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1441
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1300,
          "cache_read_input_tokens": 15680,
          "cache_creation_input_tokens": 1441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1441,
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
  "sourceToolAssistantUUID": "7ae44d84-8d98-44c4-8633-6898f45b2c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-13T10:53:48.546Z_

<details><summary>↩ Tool result · `toolu_01Qcxz2xP8pVg1xUeeKpjzAH`</summary>

```text
Now I have thorough information on both papers and the broader landscape. Let me compile my findings.

---

## Assessment: Overlap Between Existing Work and "PhaseOT"

### Paper 1: "FIDeL: Failure Identification in Demonstration Learning via OT"

**Finding: This paper does not appear to exist under this exact title or acronym.**

After extensive searching across arXiv, Google Scholar, and general web, I could not find any paper titled "FIDeL" matching the description given. The closest real paper I found is:

**ARMADA / FLOAT** (arXiv [2510.02298](https://arxiv.org/abs/2510.02298)) -- "ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation" by Wenye Yu, Jun Lv, Zixi Ying, Yang Jin, Chuan Wen, Cewu Lu (Shanghai Jiao Tong University). Its sub-method **FLOAT (FaiLure detection based on OptimAl Transport)** uses OT for per-timestep anomaly scoring during deployment of imitation learning policies.

Key details of FLOAT:
- It performs **online trajectory matching** between the current policy rollout's embeddings and stored expert demonstration embeddings using OT.
- It computes a **FLOAT index** at each timestep as the minimum OT cost across all expert demonstrations, enabling real-time failure detection.
- It uses **cosine similarity** as the cost function in the OT plan (not specifically Wasserstein distance).
- Its purpose is **deployment-time monitoring and failure recovery** (triggering human intervention and trajectory rewinding), not pre-training data curation.
- However, ARMADA's abstract explicitly mentions that "human-collected demonstrations entail substantial labour and tend to encompass mixed-quality data and redundant information," and the system does support iterative data acquisition cycles. So while FLOAT itself targets deployment monitoring, the broader system touches on data quality themes.

**Verdict on the claim "uses OT for per-timestep anomaly scoring but for deployment monitoring, not curation":** This is broadly accurate for FLOAT/ARMADA -- it is indeed for deployment monitoring. But there is **more overlap than zero**: FLOAT's OT-based per-timestep scoring mechanism could in principle be repurposed for demonstration quality diagnosis, and the paper already acknowledges mixed-quality demonstration data as a problem. A PhaseOT proposal should acknowledge that the scoring mechanism in FLOAT is technically similar (OT cost between trajectory segments and expert references), with the key distinction being application context (online monitoring vs. offline curation) and the addition of phase structure.

**Important caveat:** If "FIDeL" is a name used in the PhaseOT proposal itself to refer to a hypothetical or in-progress work, it may not be a published paper. The proposal author should verify this reference exists or clarify they mean FLOAT/ARMADA.

---

### Paper 2: Pallage 2025 (arXiv [2504.12918](https://arxiv.org/abs/2504.12918))

**"Sliced-Wasserstein Distance-based Data Selection"** by Julien Pallage and Antoine Lesage-Landry (Polytechnique Montreal). April 2025.

The claim to verify: *"Uses Sliced-Wasserstein for point-level outlier detection on static point clouds, no temporal structure."*

**Findings -- the claim is partially inaccurate:**

1. **Not point clouds.** The paper operates on **general tabular/numerical data**, not point clouds. Its datasets include UCI regression benchmarks (wine quality, forest fires, solar flares, energy efficiency, concrete strength, stock prices) and energy consumption time-series from a Montreal demand response program. The data is defined as "N independent samples z_i in R^d."

2. **"Point-level outlier detection" is roughly correct** -- the method (called SWAD) scores individual data samples by comparing the Sliced-Wasserstein transportation cost with and without each sample. A voting mechanism labels samples as outliers when their removal reduces transportation cost more than random comparison samples.

3. **"No temporal structure" is correct.** The method explicitly assumes i.i.d. data. The SWAD scoring mechanism has no temporal, sequential, or phase component whatsoever. While it is applied to time-series energy data in the benchmark, the anomaly detection itself treats samples as exchangeable.

4. **Application domain is power systems/energy**, not robotics, demonstrations, or imitation learning.

5. **Key limitation for PhaseOT comparison:** The method would not trivially extend to trajectory/phase-structured data. It treats each sample independently and would need fundamental modifications to handle ordered sequences.

**Verdict on the claim:** The characterization is **mostly accurate but imprecise** -- calling it "static point clouds" is wrong (it's tabular data), but the spirit is correct: it operates on static, unstructured, i.i.d. data with no temporal component, and is not applied to robotics or demonstrations. The overlap with PhaseOT is genuinely minimal. The only shared element is using Sliced-Wasserstein distance for anomaly detection/data selection, which is a building block, not a competing system.

---

### Additional Relevant Papers the PhaseOT Proposal Should Address

My search uncovered two papers that are **potentially closer to PhaseOT** than either of the two cited:

1. **TemporalOT** (arXiv [2410.21795](https://arxiv.org/abs/2410.21795), NeurIPS 2024) by Yuwei Fu et al. -- Introduces temporal structure into OT for demonstration-robot trajectory alignment. Uses a diagonal-band mask matrix and context-window cost averaging to enforce temporal ordering in OT plans. While it targets **reward labeling** (not data curation), it directly combines temporal structure + OT + demonstrations -- three core ingredients of PhaseOT. The key distinction is that TemporalOT uses continuous sliding windows rather than discrete phases, and is for online reward generation rather than offline quality diagnosis.

2. **Quality over Quantity (QoQ)** (arXiv [2603.09056](https://arxiv.org/abs/2603.09056)) by Haeone Lee et al. -- Directly addresses demonstration curation for robot learning using influence functions (not OT). Scores individual state-action pairs and aggregates to trajectory level. Achieves up to 23.2% improvement in simulation and 30% in real-world settings. This is the closest work in terms of *application* (demonstration curation) even though it uses a different mechanism.

---

### Summary Assessment

| Aspect | FIDeL/FLOAT (ARMADA) | Pallage 2025 | TemporalOT | QoQ |
|--------|---------------------|--------------|------------|-----|
| Uses OT | Yes | Yes (SW) | Yes | No |
| Temporal structure | Implicit (sequential matching) | None | Yes (windowed masking) | Trajectory aggregation |
| Demonstration quality | Indirect | No | No (reward labeling) | Yes (direct) |
| Per-timestep scoring | Yes | Per-sample | Yes | Per state-action pair |
| Phase structure | No | No | No (sliding window) | No |
| Application | Deployment monitoring | Data selection (energy) | Reward labeling | Data curation |

**Bottom line:** The PhaseOT proposal's characterization of these two papers is broadly defensible but could be more precise. The larger concern is that **TemporalOT (NeurIPS 2024) is not mentioned** and appears to have significant conceptual overlap (temporal structure + OT + demonstrations). A strong related-work section should explicitly differentiate from TemporalOT, FLOAT/ARMADA, and QoQ. The Pallage 2025 paper is indeed distant. The "FIDeL" reference needs verification -- it may not be a real published paper.

Sources:
- [ARMADA / FLOAT - arXiv 2510.02298](https://arxiv.org/abs/2510.02298)
- [Pallage 2025 - Sliced-Wasserstein Distance-based Data Selection - arXiv 2504.12918](https://arxiv.org/abs/2504.12918)
- [Pallage 2025 - HTML version](https://arxiv.org/html/2504.12918v1)
- [TemporalOT - Robot Policy Learning with Temporal Optimal Transport Reward - arXiv 2410.21795](https://arxiv.org/abs/2410.21795)
- [Quality over Quantity (QoQ) - arXiv 2603.09056](https://arxiv.org/abs/2603.09056)
- [ARMADA HTML version](https://arxiv.org/html/2510.02298v1)

agentId: abda8c936449a7aee (use SendMessage with to: 'abda8c936449a7aee' to continue this agent)
&lt;usage>total_tokens: 33566
tool_uses: 23
duration_ms: 177390&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24392469-c5bb-4af0-b1ca-fa10f11cd413",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "e657f498-72d3-4434-a1ef-9331d4f33e8e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for these two papers and read their content to assess overlap with a proposed method \"PhaseOT\" that uses phase-structured Wasserstein distances for demonstration quality diagnosis:\n\n1. \"FIDeL: Failure Identification in Demonstration Learning via OT\" - claimed to use OT for per-timestep anomaly scoring but for deployment monitoring, not curation. Verify this claim and check if there is more overlap than stated.\n\n2. Pallage 2025 (arXiv 2504.12918) - claimed to use \"Sliced-Wasserstein for point-level outlier detection on static point clouds, no temporal structure.\" Verify this.\n\nSearch queries:\n- \"FIDeL failure identification demonstration learning optimal transport\"\n- site:arxiv.org 2504.12918\n- \"sliced wasserstein\" data selection filtering 2025\n- \"FIDeL\" robot imitation learning OT anomaly\n\nUse WebSearch and WebFetch to read the actual papers. Focus on whether these papers are closer to PhaseOT than the proposal admits.",
    "agentId": "abda8c936449a7aee",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have thorough information on both papers and the broader landscape. Let me compile my findings.\n\n---\n\n## Assessment: Overlap Between Existing Work and \"PhaseOT\"\n\n### Paper 1: \"FIDeL: Failure Identification in Demonstration Learning via OT\"\n\n**Finding: This paper does not appear to exist under this exact title or acronym.**\n\nAfter extensive searching across arXiv, Google Scholar, and general web, I could not find any paper titled \"FIDeL\" matching the description given. The closest real paper I found is:\n\n**ARMADA / FLOAT** (arXiv [2510.02298](https://arxiv.org/abs/2510.02298)) -- \"ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation\" by Wenye Yu, Jun Lv, Zixi Ying, Yang Jin, Chuan Wen, Cewu Lu (Shanghai Jiao Tong University). Its sub-method **FLOAT (FaiLure detection based on OptimAl Transport)** uses OT for per-timestep anomaly scoring during deployment of imitation learning policies.\n\nKey details of FLOAT:\n- It performs **online trajectory matching** between the current policy rollout's embeddings and stored expert demonstration embeddings using OT.\n- It computes a **FLOAT index** at each timestep as the minimum OT cost across all expert demonstrations, enabling real-time failure detection.\n- It uses **cosine similarity** as the cost function in the OT plan (not specifically Wasserstein distance).\n- Its purpose is **deployment-time monitoring and failure recovery** (triggering human intervention and trajectory rewinding), not pre-training data curation.\n- However, ARMADA's abstract explicitly mentions that \"human-collected demonstrations entail substantial labour and tend to encompass mixed-quality data and redundant information,\" and the system does support iterative data acquisition cycles. So while FLOAT itself targets deployment monitoring, the broader system touches on data quality themes.\n\n**Verdict on the claim \"uses OT for per-timestep anomaly scoring but for deployment monitoring, not curation\":** This is broadly accurate for FLOAT/ARMADA -- it is indeed for deployment monitoring. But there is **more overlap than zero**: FLOAT's OT-based per-timestep scoring mechanism could in principle be repurposed for demonstration quality diagnosis, and the paper already acknowledges mixed-quality demonstration data as a problem. A PhaseOT proposal should acknowledge that the scoring mechanism in FLOAT is technically similar (OT cost between trajectory segments and expert references), with the key distinction being application context (online monitoring vs. offline curation) and the addition of phase structure.\n\n**Important caveat:** If \"FIDeL\" is a name used in the PhaseOT proposal itself to refer to a hypothetical or in-progress work, it may not be a published paper. The proposal author should verify this reference exists or clarify they mean FLOAT/ARMADA.\n\n---\n\n### Paper 2: Pallage 2025 (arXiv [2504.12918](https://arxiv.org/abs/2504.12918))\n\n**\"Sliced-Wasserstein Distance-based Data Selection\"** by Julien Pallage and Antoine Lesage-Landry (Polytechnique Montreal). April 2025.\n\nThe claim to verify: *\"Uses Sliced-Wasserstein for point-level outlier detection on static point clouds, no temporal structure.\"*\n\n**Findings -- the claim is partially inaccurate:**\n\n1. **Not point clouds.** The paper operates on **general tabular/numerical data**, not point clouds. Its datasets include UCI regression benchmarks (wine quality, forest fires, solar flares, energy efficiency, concrete strength, stock prices) and energy consumption time-series from a Montreal demand response program. The data is defined as \"N independent samples z_i in R^d.\"\n\n2. **\"Point-level outlier detection\" is roughly correct** -- the method (called SWAD) scores individual data samples by comparing the Sliced-Wasserstein transportation cost with and without each sample. A voting mechanism labels samples as outliers when their removal reduces transportation cost more than random comparison samples.\n\n3. **\"No temporal structure\" is correct.** The method explicitly assumes i.i.d. data. The SWAD scoring mechanism has no temporal, sequential, or phase component whatsoever. While it is applied to time-series energy data in the benchmark, the anomaly detection itself treats samples as exchangeable.\n\n4. **Application domain is power systems/energy**, not robotics, demonstrations, or imitation learning.\n\n5. **Key limitation for PhaseOT comparison:** The method would not trivially extend to trajectory/phase-structured data. It treats each sample independently and would need fundamental modifications to handle ordered sequences.\n\n**Verdict on the claim:** The characterization is **mostly accurate but imprecise** -- calling it \"static point clouds\" is wrong (it's tabular data), but the spirit is correct: it operates on static, unstructured, i.i.d. data with no temporal component, and is not applied to robotics or demonstrations. The overlap with PhaseOT is genuinely minimal. The only shared element is using Sliced-Wasserstein distance for anomaly detection/data selection, which is a building block, not a competing system.\n\n---\n\n### Additional Relevant Papers the PhaseOT Proposal Should Address\n\nMy search uncovered two papers that are **potentially closer to PhaseOT** than either of the two cited:\n\n1. **TemporalOT** (arXiv [2410.21795](https://arxiv.org/abs/2410.21795), NeurIPS 2024) by Yuwei Fu et al. -- Introduces temporal structure into OT for demonstration-robot trajectory alignment. Uses a diagonal-band mask matrix and context-window cost averaging to enforce temporal ordering in OT plans. While it targets **reward labeling** (not data curation), it directly combines temporal structure + OT + demonstrations -- three core ingredients of PhaseOT. The key distinction is that TemporalOT uses continuous sliding windows rather than discrete phases, and is for online reward generation rather than offline quality diagnosis.\n\n2. **Quality over Quantity (QoQ)** (arXiv [2603.09056](https://arxiv.org/abs/2603.09056)) by Haeone Lee et al. -- Directly addresses demonstration curation for robot learning using influence functions (not OT). Scores individual state-action pairs and aggregates to trajectory level. Achieves up to 23.2% improvement in simulation and 30% in real-world settings. This is the closest work in terms of *application* (demonstration curation) even though it uses a different mechanism.\n\n---\n\n### Summary Assessment\n\n| Aspect | FIDeL/FLOAT (ARMADA) | Pallage 2025 | TemporalOT | QoQ |\n|--------|---------------------|--------------|------------|-----|\n| Uses OT | Yes | Yes (SW) | Yes | No |\n| Temporal structure | Implicit (sequential matching) | None | Yes (windowed masking) | Trajectory aggregation |\n| Demonstration quality | Indirect | No | No (reward labeling) | Yes (direct) |\n| Per-timestep scoring | Yes | Per-sample | Yes | Per state-action pair |\n| Phase structure | No | No | No (sliding window) | No |\n| Application | Deployment monitoring | Data selection (energy) | Reward labeling | Data curation |\n\n**Bottom line:** The PhaseOT proposal's characterization of these two papers is broadly defensible but could be more precise. The larger concern is that **TemporalOT (NeurIPS 2024) is not mentioned** and appears to have significant conceptual overlap (temporal structure + OT + demonstrations). A strong related-work section should explicitly differentiate from TemporalOT, FLOAT/ARMADA, and QoQ. The Pallage 2025 paper is indeed distant. The \"FIDeL\" reference needs verification -- it may not be a real published paper.\n\nSources:\n- [ARMADA / FLOAT - arXiv 2510.02298](https://arxiv.org/abs/2510.02298)\n- [Pallage 2025 - Sliced-Wasserstein Distance-based Data Selection - arXiv 2504.12918](https://arxiv.org/abs/2504.12918)\n- [Pallage 2025 - HTML version](https://arxiv.org/html/2504.12918v1)\n- [TemporalOT - Robot Policy Learning with Temporal Optimal Transport Reward - arXiv 2410.21795](https://arxiv.org/abs/2410.21795)\n- [Quality over Quantity (QoQ) - arXiv 2603.09056](https://arxiv.org/abs/2603.09056)\n- [ARMADA HTML version](https://arxiv.org/html/2510.02298v1)"
      }
    ],
    "totalDurationMs": 177390,
    "totalTokens": 33566,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 29919,
      "output_tokens": 2098,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2098,
          "cache_read_input_tokens": 29919,
          "cache_creation_input_tokens": 1548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1548,
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
  "sourceToolAssistantUUID": "24392469-c5bb-4af0-b1ca-fa10f11cd413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e657f498-72d3-4434-a1ef-9331d4f33e8e",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PhaseOT demo quality diagnosis idea (Round 5)",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Assistant

_source line 30 · 2026-05-13T10:53:54.844Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have extensive information. Let me also verify a few more things - the FIDeL reference which seems potentially fabricated, and the adapted OT papers. Let me also check whether the AAAI 2027 deadline is realistic.

Actually, the agent searching for FIDeL found that it might not exist under that exact title, but found FLOAT/ARMADA instead. The proposal does cite FIDeL as "Failure Identification in Demonstration Learning via OT (arXiv 2025)." Let me check this more carefully.

Let me also verify the AAAI 2027 deadline claim and the Cheng & Liu robust Wasserstein barycenter paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e657f498-72d3-4434-a1ef-9331d4f33e8e",
  "isSidechain": false,
  "requestId": "req_011CazSgjFUAvBfF5HvVEcaQ",
  "type": "assistant",
  "uuid": "f2fa7c08-e4a8-4046-b603-e0c6e855451e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxmM8ckLMbn2g1Fb15W6LV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 44560,
      "output_tokens": 840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1405,
          "output_tokens": 840,
          "cache_read_input_tokens": 44560,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4293
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

_source line 31 · 2026-05-13T10:53:55.410Z_

Let me verify a few more critical references and check for the AAAI 2027 deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2fa7c08-e4a8-4046-b603-e0c6e855451e",
  "isSidechain": false,
  "requestId": "req_011CazSgjFUAvBfF5HvVEcaQ",
  "type": "assistant",
  "uuid": "80a6208b-96a1-4302-87a1-560695e4184e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxmM8ckLMbn2g1Fb15W6LV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 44560,
      "output_tokens": 840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1405,
          "output_tokens": 840,
          "cache_read_input_tokens": 44560,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4293
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

_source line 32 · 2026-05-13T10:54:00.682Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011Z1appACtqQywaX2FeMeMU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify FIDeL paper and AAAI 2027",
  "prompt": "I need to verify two things:\n\n1. Does the paper \"FIDeL: Failure Identification in Demonstration Learning\" exist? It's claimed to use OT-based per-timestep anomaly scoring for execution monitoring during deployment (not dataset curation). Search for:\n- \"FIDeL\" \"failure identification\" demonstration learning\n- \"FIDeL\" optimal transport robot\n- site:arxiv.org FIDeL demonstration\n- An earlier search suggested this might actually be FLOAT/ARMADA (arXiv 2510.02298). Check if \"FIDeL\" is an alias or a separate paper.\n\n2. What is the expected deadline for AAAI 2027? The proposal claims \"late July 2026, based on AAAI 2026 pattern of abstract Jul 25, paper Aug 1\". Verify:\n- What were the actual AAAI 2026 deadlines?\n- Has AAAI 2027 been announced yet?\n- Is the \"late July 2026\" estimate reasonable?\n\nSearch using WebSearch for both. Report exact findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a6208b-96a1-4302-87a1-560695e4184e",
  "isSidechain": false,
  "requestId": "req_011CazSgjFUAvBfF5HvVEcaQ",
  "type": "assistant",
  "uuid": "6c2d7048-478f-4633-ae1e-0384f4400494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxmM8ckLMbn2g1Fb15W6LV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 44560,
      "output_tokens": 840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1405,
          "output_tokens": 840,
          "cache_read_input_tokens": 44560,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4293
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

_source line 33 · 2026-05-13T10:54:05.593Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TBkGrUZ3AivCnCqTaw7T9X`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check FAKTUAL and Cheng Liu 2026",
  "prompt": "Verify these two papers cited in a proposal:\n\n1. \"FAKTUAL\" (arXiv 2026) - claimed to use \"signature-kernel entropy for diversity-aware curation\" and show that \"RoboMimic Transport has highest demonstration diversity.\" Search for:\n- \"FAKTUAL\" robot demonstration diversity\n- \"signature-kernel entropy\" demonstration curation\n- site:arxiv.org FAKTUAL 2026\n\n2. \"Cheng & Liu (arXiv 2026)\" - claimed to be a paper on \"Robust Wasserstein Barycenter\" with an \"iterative reweighting scheme.\" Search for:\n- \"Robust Wasserstein Barycenter\" Cheng Liu 2026\n- site:arxiv.org robust Wasserstein barycenter 2026\n- Cheng Liu Wasserstein barycenter\n\nReport whether these papers exist with the claimed content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c2d7048-478f-4633-ae1e-0384f4400494",
  "isSidechain": false,
  "requestId": "req_011CazSgjFUAvBfF5HvVEcaQ",
  "type": "assistant",
  "uuid": "41694b61-8560-42c8-8ab8-a8dcc8a080b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxmM8ckLMbn2g1Fb15W6LV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1405,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 44560,
      "output_tokens": 840,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1405,
          "output_tokens": 840,
          "cache_read_input_tokens": 44560,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4293
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

_source line 34 · 2026-05-13T10:55:02.566Z_

<details><summary>↩ Tool result · `toolu_011Z1appACtqQywaX2FeMeMU`</summary>

```text
Here are my findings on both questions:

---

## 1. Does the paper "FIDeL: Failure Identification in Demonstration Learning" exist?

**No, this paper does not appear to exist.** Across multiple targeted searches ("FIDeL" + "failure identification" + demonstration learning, "FIDeL" + optimal transport + robot, and arxiv-restricted searches), no paper with this title or acronym was found in the context of robotics/demonstration learning.

The only "FIDeL" paper on arXiv is **"Fidel: Reconstructing Private Training Samples from Weight Updates in Federated Learning"** (arXiv 2101.00159), which is an entirely unrelated federated learning privacy attack paper.

**The paper being described is actually ARMADA/FLOAT** (arXiv 2510.02298):
- **ARMADA** = "Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation"
- **FLOAT** = "FaiLure detection based on OptimAl Transport" -- the specific failure detection method within ARMADA
- FLOAT performs online trajectory matching between current policy rollouts and expert trajectories, computing distance using Optimal Transport -- this matches the described "OT-based per-timestep anomaly scoring for execution monitoring during deployment"
- FLOAT achieves ~95% failure detection accuracy, surpassing prior state-of-the-art by >20%
- Published October 2, 2025

**"FIDeL" is NOT an alias for FLOAT/ARMADA.** Searching for "FIDeL" in conjunction with ARMADA/FLOAT returned zero co-occurrences. The name "FIDeL" appears to be fabricated or hallucinated. The correct citation for OT-based per-timestep anomaly scoring for execution monitoring during robot deployment is **FLOAT** within the **ARMADA** system.

---

## 2. AAAI 2027 deadline estimate

**The proposal's claim of "late July 2026, based on AAAI 2026 pattern of abstract Jul 25, paper Aug 1" is accurate and well-supported.**

### Verified AAAI deadline history:

| Conference | Abstract Deadline | Paper Deadline | Conference Dates |
|---|---|---|---|
| AAAI 2025 | Aug 7, 2024 | Aug 15, 2024 | Feb 25 - Mar 4, 2025 (Philadelphia) |
| AAAI 2026 | Jul 25, 2025 | Aug 1, 2025 | Jan 20-27, 2026 (Singapore) |
| AAAI 2027 | ~Jul 26, 2026 (est.) | ~Aug 2, 2026 (est.) | Feb 16-23, 2027 (Montreal) |

### Has AAAI 2027 been announced?
- **Partially.** The conference dates (Feb 16-23, 2027, Montreal) and OpenReview page are set up, but as of May 2026, the official submission deadlines have **not been formally announced** by AAAI. Some deadline-tracking sites (aideadlines.org, trybibby.com) estimate the abstract deadline as approximately **July 26, 2026** and the paper deadline as approximately **August 2, 2026**, based on the AAAI 2026 pattern.

### Is the "late July 2026" estimate reasonable?
- **Yes, very reasonable.** The AAAI 2026 deadlines (abstract Jul 25, paper Aug 1) were actually slightly earlier than AAAI 2025 (abstract Aug 7, paper Aug 15). The trend and third-party estimates both converge on a late-July 2026 abstract deadline, consistent with the proposal's claim. The one caveat is that AAAI has not officially confirmed the dates yet, so there could be a shift of 1-2 weeks in either direction.

---

Sources:
- [ARMADA paper (arXiv 2510.02298)](https://arxiv.org/abs/2510.02298)
- [ARMADA HTML version](https://arxiv.org/html/2510.02298)
- [Fidel: Federated Learning paper (arXiv 2101.00159)](https://arxiv.org/abs/2101.00159)
- [AAAI-26 Submission Instructions](https://aaai.org/conference/aaai/aaai-26/submission-instructions/)
- [AAAI-26 Conference Page](https://aaai.org/conference/aaai/aaai-26/)
- [AAAI-25 Call for Papers](https://aaai.org/conference/aaai/aaai-25/aaai-25-main-technical-call-for-papers/)
- [AAAI 2027 on aideadlines.org](http://aideadlines.org/conference/?id=aaai27)
- [AAAI 2027 on OpenReview](https://openreview.net/group?id=AAAI.org%2F2027%2FConference)
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)
- [ARMADA GitHub](https://github.com/Virlus/armada)

agentId: a9ae9be0d9ab13305 (use SendMessage with to: 'a9ae9be0d9ab13305' to continue this agent)
&lt;usage>total_tokens: 21348
tool_uses: 12
duration_ms: 61874&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c2d7048-478f-4633-ae1e-0384f4400494",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "92dcb2d6-2e30-4669-906c-15796aa26aa7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two things:\n\n1. Does the paper \"FIDeL: Failure Identification in Demonstration Learning\" exist? It's claimed to use OT-based per-timestep anomaly scoring for execution monitoring during deployment (not dataset curation). Search for:\n- \"FIDeL\" \"failure identification\" demonstration learning\n- \"FIDeL\" optimal transport robot\n- site:arxiv.org FIDeL demonstration\n- An earlier search suggested this might actually be FLOAT/ARMADA (arXiv 2510.02298). Check if \"FIDeL\" is an alias or a separate paper.\n\n2. What is the expected deadline for AAAI 2027? The proposal claims \"late July 2026, based on AAAI 2026 pattern of abstract Jul 25, paper Aug 1\". Verify:\n- What were the actual AAAI 2026 deadlines?\n- Has AAAI 2027 been announced yet?\n- Is the \"late July 2026\" estimate reasonable?\n\nSearch using WebSearch for both. Report exact findings.",
    "agentId": "a9ae9be0d9ab13305",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings on both questions:\n\n---\n\n## 1. Does the paper \"FIDeL: Failure Identification in Demonstration Learning\" exist?\n\n**No, this paper does not appear to exist.** Across multiple targeted searches (\"FIDeL\" + \"failure identification\" + demonstration learning, \"FIDeL\" + optimal transport + robot, and arxiv-restricted searches), no paper with this title or acronym was found in the context of robotics/demonstration learning.\n\nThe only \"FIDeL\" paper on arXiv is **\"Fidel: Reconstructing Private Training Samples from Weight Updates in Federated Learning\"** (arXiv 2101.00159), which is an entirely unrelated federated learning privacy attack paper.\n\n**The paper being described is actually ARMADA/FLOAT** (arXiv 2510.02298):\n- **ARMADA** = \"Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation\"\n- **FLOAT** = \"FaiLure detection based on OptimAl Transport\" -- the specific failure detection method within ARMADA\n- FLOAT performs online trajectory matching between current policy rollouts and expert trajectories, computing distance using Optimal Transport -- this matches the described \"OT-based per-timestep anomaly scoring for execution monitoring during deployment\"\n- FLOAT achieves ~95% failure detection accuracy, surpassing prior state-of-the-art by >20%\n- Published October 2, 2025\n\n**\"FIDeL\" is NOT an alias for FLOAT/ARMADA.** Searching for \"FIDeL\" in conjunction with ARMADA/FLOAT returned zero co-occurrences. The name \"FIDeL\" appears to be fabricated or hallucinated. The correct citation for OT-based per-timestep anomaly scoring for execution monitoring during robot deployment is **FLOAT** within the **ARMADA** system.\n\n---\n\n## 2. AAAI 2027 deadline estimate\n\n**The proposal's claim of \"late July 2026, based on AAAI 2026 pattern of abstract Jul 25, paper Aug 1\" is accurate and well-supported.**\n\n### Verified AAAI deadline history:\n\n| Conference | Abstract Deadline | Paper Deadline | Conference Dates |\n|---|---|---|---|\n| AAAI 2025 | Aug 7, 2024 | Aug 15, 2024 | Feb 25 - Mar 4, 2025 (Philadelphia) |\n| AAAI 2026 | Jul 25, 2025 | Aug 1, 2025 | Jan 20-27, 2026 (Singapore) |\n| AAAI 2027 | ~Jul 26, 2026 (est.) | ~Aug 2, 2026 (est.) | Feb 16-23, 2027 (Montreal) |\n\n### Has AAAI 2027 been announced?\n- **Partially.** The conference dates (Feb 16-23, 2027, Montreal) and OpenReview page are set up, but as of May 2026, the official submission deadlines have **not been formally announced** by AAAI. Some deadline-tracking sites (aideadlines.org, trybibby.com) estimate the abstract deadline as approximately **July 26, 2026** and the paper deadline as approximately **August 2, 2026**, based on the AAAI 2026 pattern.\n\n### Is the \"late July 2026\" estimate reasonable?\n- **Yes, very reasonable.** The AAAI 2026 deadlines (abstract Jul 25, paper Aug 1) were actually slightly earlier than AAAI 2025 (abstract Aug 7, paper Aug 15). The trend and third-party estimates both converge on a late-July 2026 abstract deadline, consistent with the proposal's claim. The one caveat is that AAAI has not officially confirmed the dates yet, so there could be a shift of 1-2 weeks in either direction.\n\n---\n\nSources:\n- [ARMADA paper (arXiv 2510.02298)](https://arxiv.org/abs/2510.02298)\n- [ARMADA HTML version](https://arxiv.org/html/2510.02298)\n- [Fidel: Federated Learning paper (arXiv 2101.00159)](https://arxiv.org/abs/2101.00159)\n- [AAAI-26 Submission Instructions](https://aaai.org/conference/aaai/aaai-26/submission-instructions/)\n- [AAAI-26 Conference Page](https://aaai.org/conference/aaai/aaai-26/)\n- [AAAI-25 Call for Papers](https://aaai.org/conference/aaai/aaai-25/aaai-25-main-technical-call-for-papers/)\n- [AAAI 2027 on aideadlines.org](http://aideadlines.org/conference/?id=aaai27)\n- [AAAI 2027 on OpenReview](https://openreview.net/group?id=AAAI.org%2F2027%2FConference)\n- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)\n- [ARMADA GitHub](https://github.com/Virlus/armada)"
      }
    ],
    "totalDurationMs": 61874,
    "totalTokens": 21348,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 758,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 18429,
      "output_tokens": 1306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 855
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 758,
          "output_tokens": 1306,
          "cache_read_input_tokens": 18429,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 855,
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
  "sourceToolAssistantUUID": "6c2d7048-478f-4633-ae1e-0384f4400494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T10:55:09.393Z_

<details><summary>↩ Tool result · `toolu_01TBkGrUZ3AivCnCqTaw7T9X`</summary>

```text
Now I have a thorough picture. Let me compile the findings.

---

## Verification Results

### Paper 1: "FAKTUAL" (arXiv 2026)

**Status: The paper EXISTS but the cited claims need qualification.**

The paper is real. It is titled **"Diversity You Can Actually Measure: A Fast, Model-Free Diversity Metric for Robotics Datasets"** by Sreevardhan Sirigiri, Nathan Samuel de Lara, Christopher Agia, Florian Shkurti, and Fabio Ramos (arXiv:2603.11634, March 2026).

- **Claim: "signature-kernel entropy for diversity-aware curation"** -- **ACCURATE.** The paper explicitly defines signature-transform-based entropy on the Gram matrix of a signature kernel over demonstrations and uses this as the basis for its curation algorithm, FAKTUAL (FAst trajectory Kernel enTropy cUration for imitation Learning).

- **Claim: "RoboMimic Transport has highest demonstration diversity"** -- **PARTIALLY SUPPORTED / OVERSTATED.** The paper does observe that the RoboMimic Transport task's entropy "does not saturate over the range shown, indicating that the Transport task is more diverse" compared to the Can task, and notes that "each demonstration contributes almost equally to the entropy." However, the paper does **not** make a blanket declaration that Transport has the "highest demonstration diversity" across all benchmarks. It discusses Transport's slower entropy saturation as evidence of greater per-demonstration novelty relative to other RoboMimic tasks, but frames this cautiously rather than as a definitive ranking. A proposal citing it as a definitive finding is somewhat embellishing the original claim.

### Paper 2: "Cheng & Liu (arXiv 2026)" on "Robust Wasserstein Barycenter"

**Status: The paper EXISTS but the specific claim about an "iterative reweighting scheme" appears INACCURATE.**

The paper is real. It is titled **"Robust Wasserstein barycenter"** by Zixiong Cheng and Hang Liu (arXiv:2603.07563, March 2026).

- **Claim: Authors are "Cheng & Liu"** -- **ACCURATE** (Zixiong Cheng and Hang Liu).

- **Claim: Paper is about "Robust Wasserstein Barycenter"** -- **ACCURATE.** The paper proposes a robust Wasserstein barycenter (RWB) to address the sensitivity of classical Wasserstein barycenters to outliers.

- **Claim: Paper proposes an "iterative reweighting scheme"** -- **NOT CONFIRMED / LIKELY INACCURATE.** The paper's computational method adapts the Iterative Bregman Projections (IBP) algorithm with a free-support variant that uses a fixed-point iteration to update support points. There is no mention of an "iterative reweighting scheme" in the paper. The term "reweighting" does not appear in the text. The proposal's characterization of the algorithm as an "iterative reweighting scheme" appears to be a fabrication or a confusion with a different paper. Notably, a separate older paper -- [arXiv:2312.15762] "On Robust Wasserstein Barycenter: The Model and Algorithm" (2023) -- also exists on this topic and may use different algorithmic approaches, so there may be a conflation of the two.

### Summary

| Claim | Verdict |
|---|---|
| FAKTUAL paper exists on arXiv 2026 | **Confirmed** (arXiv:2603.11634) |
| Uses signature-kernel entropy for curation | **Confirmed** |
| "RoboMimic Transport has highest demonstration diversity" | **Overstated** -- paper shows Transport is more diverse than Can, but does not declare it the most diverse overall |
| Cheng & Liu (2026) "Robust Wasserstein Barycenter" exists | **Confirmed** (arXiv:2603.07563) |
| Paper proposes an "iterative reweighting scheme" | **Not confirmed** -- the algorithm is a free-support IBP variant with fixed-point iteration, not a "reweighting scheme" |

Both papers are real, but the proposal's characterization of their content contains embellishments: the FAKTUAL diversity claim is overstated, and the Cheng & Liu algorithm description ("iterative reweighting scheme") does not match what the paper actually proposes.

Sources:
- [FAKTUAL - arXiv:2603.11634](https://arxiv.org/abs/2603.11634)
- [FAKTUAL - Full HTML](https://arxiv.org/html/2603.11634)
- [Robust Wasserstein Barycenter - arXiv:2603.07563](https://arxiv.org/abs/2603.07563)
- [Robust Wasserstein Barycenter - Full HTML](https://arxiv.org/html/2603.07563)

agentId: a27983b1b3c601c69 (use SendMessage with to: 'a27983b1b3c601c69' to continue this agent)
&lt;usage>total_tokens: 19076
tool_uses: 11
duration_ms: 63793&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41694b61-8560-42c8-8ab8-a8dcc8a080b8",
  "isSidechain": false,
  "promptId": "0dd0fd09-b171-43be-9e9d-d5e8cc786158",
  "type": "user",
  "uuid": "9e0329cb-b709-4c88-aef4-349021ee96c8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Verify these two papers cited in a proposal:\n\n1. \"FAKTUAL\" (arXiv 2026) - claimed to use \"signature-kernel entropy for diversity-aware curation\" and show that \"RoboMimic Transport has highest demonstration diversity.\" Search for:\n- \"FAKTUAL\" robot demonstration diversity\n- \"signature-kernel entropy\" demonstration curation\n- site:arxiv.org FAKTUAL 2026\n\n2. \"Cheng & Liu (arXiv 2026)\" - claimed to be a paper on \"Robust Wasserstein Barycenter\" with an \"iterative reweighting scheme.\" Search for:\n- \"Robust Wasserstein Barycenter\" Cheng Liu 2026\n- site:arxiv.org robust Wasserstein barycenter 2026\n- Cheng Liu Wasserstein barycenter\n\nReport whether these papers exist with the claimed content.",
    "agentId": "a27983b1b3c601c69",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a thorough picture. Let me compile the findings.\n\n---\n\n## Verification Results\n\n### Paper 1: \"FAKTUAL\" (arXiv 2026)\n\n**Status: The paper EXISTS but the cited claims need qualification.**\n\nThe paper is real. It is titled **\"Diversity You Can Actually Measure: A Fast, Model-Free Diversity Metric for Robotics Datasets\"** by Sreevardhan Sirigiri, Nathan Samuel de Lara, Christopher Agia, Florian Shkurti, and Fabio Ramos (arXiv:2603.11634, March 2026).\n\n- **Claim: \"signature-kernel entropy for diversity-aware curation\"** -- **ACCURATE.** The paper explicitly defines signature-transform-based entropy on the Gram matrix of a signature kernel over demonstrations and uses this as the basis for its curation algorithm, FAKTUAL (FAst trajectory Kernel enTropy cUration for imitation Learning).\n\n- **Claim: \"RoboMimic Transport has highest demonstration diversity\"** -- **PARTIALLY SUPPORTED / OVERSTATED.** The paper does observe that the RoboMimic Transport task's entropy \"does not saturate over the range shown, indicating that the Transport task is more diverse\" compared to the Can task, and notes that \"each demonstration contributes almost equally to the entropy.\" However, the paper does **not** make a blanket declaration that Transport has the \"highest demonstration diversity\" across all benchmarks. It discusses Transport's slower entropy saturation as evidence of greater per-demonstration novelty relative to other RoboMimic tasks, but frames this cautiously rather than as a definitive ranking. A proposal citing it as a definitive finding is somewhat embellishing the original claim.\n\n### Paper 2: \"Cheng & Liu (arXiv 2026)\" on \"Robust Wasserstein Barycenter\"\n\n**Status: The paper EXISTS but the specific claim about an \"iterative reweighting scheme\" appears INACCURATE.**\n\nThe paper is real. It is titled **\"Robust Wasserstein barycenter\"** by Zixiong Cheng and Hang Liu (arXiv:2603.07563, March 2026).\n\n- **Claim: Authors are \"Cheng & Liu\"** -- **ACCURATE** (Zixiong Cheng and Hang Liu).\n\n- **Claim: Paper is about \"Robust Wasserstein Barycenter\"** -- **ACCURATE.** The paper proposes a robust Wasserstein barycenter (RWB) to address the sensitivity of classical Wasserstein barycenters to outliers.\n\n- **Claim: Paper proposes an \"iterative reweighting scheme\"** -- **NOT CONFIRMED / LIKELY INACCURATE.** The paper's computational method adapts the Iterative Bregman Projections (IBP) algorithm with a free-support variant that uses a fixed-point iteration to update support points. There is no mention of an \"iterative reweighting scheme\" in the paper. The term \"reweighting\" does not appear in the text. The proposal's characterization of the algorithm as an \"iterative reweighting scheme\" appears to be a fabrication or a confusion with a different paper. Notably, a separate older paper -- [arXiv:2312.15762] \"On Robust Wasserstein Barycenter: The Model and Algorithm\" (2023) -- also exists on this topic and may use different algorithmic approaches, so there may be a conflation of the two.\n\n### Summary\n\n| Claim | Verdict |\n|---|---|\n| FAKTUAL paper exists on arXiv 2026 | **Confirmed** (arXiv:2603.11634) |\n| Uses signature-kernel entropy for curation | **Confirmed** |\n| \"RoboMimic Transport has highest demonstration diversity\" | **Overstated** -- paper shows Transport is more diverse than Can, but does not declare it the most diverse overall |\n| Cheng & Liu (2026) \"Robust Wasserstein Barycenter\" exists | **Confirmed** (arXiv:2603.07563) |\n| Paper proposes an \"iterative reweighting scheme\" | **Not confirmed** -- the algorithm is a free-support IBP variant with fixed-point iteration, not a \"reweighting scheme\" |\n\nBoth papers are real, but the proposal's characterization of their content contains embellishments: the FAKTUAL diversity claim is overstated, and the Cheng & Liu algorithm description (\"iterative reweighting scheme\") does not match what the paper actually proposes.\n\nSources:\n- [FAKTUAL - arXiv:2603.11634](https://arxiv.org/abs/2603.11634)\n- [FAKTUAL - Full HTML](https://arxiv.org/html/2603.11634)\n- [Robust Wasserstein Barycenter - arXiv:2603.07563](https://arxiv.org/abs/2603.07563)\n- [Robust Wasserstein Barycenter - Full HTML](https://arxiv.org/html/2603.07563)"
      }
    ],
    "totalDurationMs": 63793,
    "totalTokens": 19076,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 16892,
      "output_tokens": 1196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1196,
          "cache_read_input_tokens": 16892,
          "cache_creation_input_tokens": 987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 987,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "41694b61-8560-42c8-8ab8-a8dcc8a080b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-13T10:55:09.403Z_

```json
{
  "parentUuid": "9e0329cb-b709-4c88-aef4-349021ee96c8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "81e0bc40-7a4b-45e5-9b33-3df9f1461278",
  "timestamp": "2026-05-13T10:55:09.403Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-13T10:55:59.525Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have extensive verification data. Let me synthesize my findings and produce the review.

Key findings from my research:

1. **SCIZOR (ICRA 2026)**: VERIFIED. All claims about SCIZOR are accurate. It does operate at transition level, achieves 54%/31% recovery, produces categorical diagnostic profiles, and achieves the claimed improvements.

2. **CIQL**: VERIFIED. The paper exists exactly as cited (Bu et al., IEEE RA-L 2024).

3. **CoRL 2026 deadlines**: CONFIRMED. Abstract May 26, paper May 29. 

13 days to abstract, 16 days to paper.

4. **FIDeL reference**: LIKELY FABRICATED. No paper with this exact title exists. The closest match is FLOAT within the ARMADA system (arXiv 2510.02298). "FIDeL" appears to be a hallucinated citation.

5. **FAKTUAL**: EXISTS but the claim about "RoboMimic Transport has highest demonstration diversity" is overstated.

6. **Cheng & Liu (2026)**: EXISTS but the description of the "iterative reweighting scheme" doesn't match what the paper actually presents.

7. **Shi et al. (2025)**: VERIFIED. Paper exists, 15% improvement confirmed, operates at trajectory chunk level.

8. **AAAI 2027 deadline**: Estimated late July 2026, reasonable based on historical patterns.

9. **Competing work landscape**: The proposal covers the major competing works comprehensively. The field is crowded with 8+ methods emerging in 2024-2026.

10. **Novelty assessment**: The combination of optimal transport with phase-level demonstration quality scoring is genuinely novel, as is the mode-aware scoring approach and phase-structured Wasserstein distance. The theoretical contribution is more incremental though—it's essentially applying standard Wasserstein concentration results at the phase level rather than introducing fundamentally new theory.

11. **CoRL 2026 feasibility**: With only 13 days to the abstract deadline, this is infeasible from scratch, which the proposal correctly acknowledges.

12. **User requirement mismatch**: The user asked specifically for CoRL 2026, but the proposal pivots to AAAI 2027 instead—a persistent gap across all previous rounds.

Now I'm evaluating the novelty score. The phase-structured Wasserstein distance and mode-aware scoring are genuinely new contributions that haven't been explored before in demonstration curation. However, the field is saturated with competing approaches, the theoretical innovation is limited to applying existing concentration inequalities in a new context, and optimal transport for data quality is becoming a well-established direction. This pushes the novelty score up slightly but not dramatically.

For feasibility, the approach is well-specified and the computational estimates look reasonable, though the pipeline has many interdependent components. CoRL 2026 is clearly impossible given the timeline, but AAAI 2027 with roughly 2.5 months is tight but workable. The clarity is exceptional—the proposal is comprehensive, well-written, and mathematically rigorous with honest treatment of limitations. On impact, demonstration curation is a meaningful problem, though the contribution feels somewhat incremental rather than transformative.

Actually, stepping back—this is round 5 of 10, and the proposal has genuinely improved. Let me be more careful here. There are some real issues I need to flag: FIDeL appears to be a fabricated reference, the CoRL 2026 deadline still contradicts the user's stated requirements, the description of the Cheng & Liu algorithm mischaracterizes it as iterative reweighting when that's not accurate, and the FAKTUAL claim about achieving the highest diversity seems overstated.

Beyond those, the core question is whether phase-level scoring actually beats SCIZOR's transition-level approach in practice, and whether applying existing concentration bounds per-phase really constitutes a meaningful theoretical contribution. But I should acknowledge that the proposal has come a long way—the experimental design is solid, the approach is well-specified, and most claims are honestly framed. The persistent blockers are the FIDeL citation issue and the CoRL 2026 feasibility problem that the user already flagged. the proposal but not accepted by the user)
2. FIDeL appears to be a fabricated reference
3. Some minor reference inaccuracies (Cheng & Liu algorithm, FAKTUAL claim)
4. The empirical value proposition over SCIZOR is uncertain

The average score would be roughly (3.5 + 3.5 + 4.5 + 3) / 4 = 3.625, which is below the 4.0 threshold.

Actually, let me reconsider each score more carefully:

**Novelty: 3.5**
- Phase-structured Wasserstein distance for demo quality is genuinely new
- Mode-aware scoring in curation is novel
- But: building blocks (OT, phase segmentation, clustering) are all standard
- The theoretical contribution is modest (standard results applied per-phase)
- The adapted OT connection is now honestly positioned as inspiration

In the crowded demo curation space, this is a solid contribution but not particularly exciting.

**Feasibility: 3.5**
- The approach is well-specified with reasonable computational requirements, though CoRL 2026 is completely unrealistic at just 13 days away
- AAAI 2027 is doable but tight with about 2.5 months, and the pipeline has many moving parts—segmentation, OT, clustering, scoring—each needing careful tuning
- The fabricated FIDeL reference raises concerns about how thoroughly this was vetted, and the empirical plan is ambitious with 4 benchmarks, 8 baselines, and ablations
- The core risk is whether phase-level OT actually beats simpler alternatives, though each component is individually well-established

**Clarity: 4.5**
- Extremely well

-written with comprehensive related work, clear math, and thoughtful experimental design
- The reference issues (fabricated FIDeL, mischaracterized Cheng & Liu) bring this down slightly to 4

**Impact: 3**
- Phase-level diagnosis and mode-aware scoring address real gaps, but the practical advantage over SCIZOR is unclear
- The field is saturated with curation methods, and real impact hinges on whether phase decomposition actually helps in practice

The average comes to about 3.5, which is below the 4.0 bar. The verdict is to revise.

But I should also consider whether this idea could ever be strong enough. The core issues are that CoRL 2026 is impossible as a venue (not an idea problem), and the novelty is somewhat incremental—applying standard techniques in a new combination rather than introducing fundamentally new concepts.

I think this could pass with targeted revisions: fixing the fabricated reference and minor inaccuracies, making the value proposition against SCIZOR more concrete and compelling, and shifting the target venue to AAAI 2027 since CoRL 2026 isn't feasible.

Now I'll draft the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e0bc40-7a4b-45e5-9b33-3df9f1461278",
  "isSidechain": false,
  "requestId": "req_011CazSngvzQo6JbUNecBdmm",
  "type": "assistant",
  "uuid": "bb139ded-86da-40ea-b50d-d4668755ebe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jt8VaqCH2qNGS4yUgfozGo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5057,
      "cache_read_input_tokens": 48853,
      "output_tokens": 4644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4644,
          "cache_read_input_tokens": 48853,
          "cache_creation_input_tokens": 5057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5057
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

_source line 38 · 2026-05-13T10:56:55.029Z_

Now I have comprehensive data from my independent verification. Let me compile the final review.

**Summary of my findings:**
- SCIZOR, CIQL, Shi et al., FAKTUAL, Cheng & Liu all verified as real papers
- FIDeL appears to be a **fabricated reference** (the actual paper is FLOAT/ARMADA, arXiv 2510.02298)
- CoRL 2026 deadlines confirmed: abstract May 26, paper May 29, deadlines are final
- AAAI 2027 deadline estimate (~late July 2026) is reasonable
- Cheng & Liu's algorithm is misdescribed ("iterative reweighting" → actually IBP with fixed-point iteration)
- No existing paper combines phase-level OT with demo quality scoring (novelty claim holds)
- Field is extremely crowded: 8+ curation methods published 2024-2026

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "Phase-structured Wasserstein distance for demo quality diagnosis and mode-aware curation are genuinely novel — no existing method combines these. However, every building block (OT, phase segmentation, spectral clustering, Wasserstein barycenters) is standard, and the theoretical contribution (per-phase concentration inequality) is a straightforward application of existing Wasserstein concentration results to a decomposed setting. In an extremely crowded field (SCIZOR, CUPID, DemInf, QoQ, RINSE, S2I, DataMIL, Demo-SCORE all published 2024-2026), the combination is competent but not paradigm-shifting."},
    "feasibility": {"score": 3.5, "rationale": "The pipeline is well-specified with each component individually well-established. Cost estimates (1500h A100, $2,250) are reasonable for AAAI 2027 timeline. However, CoRL 2026 is definitively impossible (13 days to abstract, deadlines confirmed as final), which directly contradicts the user's requirement. The ambitious experimental plan (4 benchmarks × 8 baselines × 9 ablations) is achievable in ~2.5 months for AAAI but leaves little margin. One cited reference (FIDeL) is fabricated, suggesting incomplete vetting."},
    "clarity": {"score": 4, "rationale": "Among the most comprehensive and clearly specified proposals I have reviewed. The landscape coverage is exceptional (30+ papers accurately positioned), the mathematical formulation is precise, the experimental design is well-motivated with experiments targeting unique capabilities. Docked from 4.5 for: FIDeL is a fabricated citation, Cheng & Liu's algorithm is misdescribed as 'iterative reweighting' (it's actually IBP with fixed-point iteration), and the FAKTUAL diversity claim is overstated."},
    "impact": {"score": 3, "rationale": "Phase-level diagnosis and mode-aware scoring address real gaps, but the practical advantage over SCIZOR's transition-level filtering (which already achieves partial trajectory recovery and produces categorical diagnostic labels) is uncertain. The field is saturated with curation methods achieving 5-35% improvements via diverse approaches. Whether phase-level OT scoring yields meaningfully better policies than simpler heuristic approaches (RINSE's smoothness metrics, DemInf's MI) remains an open empirical question."}
  },
  "issues": [
    "CRITICAL — FIDeL is a fabricated reference: No paper titled 'FIDeL: Failure Identification in Demonstration Learning via OT' exists. The closest match is FLOAT (within the ARMADA system, arXiv 2510.02298), which uses OT for online failure detection during deployment. The proposal must either correct this citation to FLOAT/ARMADA or remove it entirely. A fabricated citation would be fatal at peer review.",
    "CRITICAL — CoRL 2026 venue mismatch persists (5th consecutive flag): The user explicitly targets CoRL 2026. Abstract deadline is May 26 (13 days away), paper deadline May 29 (16 days away), and the organizers state 'deadlines are final.' The proposal correctly identifies this as infeasible and pivots to AAAI 2027 (~late July 2026, confirmed via historical patterns). While intellectually honest, this still does not satisfy the user's stated requirement. The user must explicitly accept this venue change.",
    "Cheng & Liu (2026) algorithm misdescription: The proposal describes their robust Wasserstein barycenter method as using an 'iterative reweighting scheme.' Verification shows it actually uses a free-support variant of Iterative Bregman Projections with fixed-point iteration — the term 'reweighting' does not appear in the paper. This mischaracterization, while minor, could draw reviewer scrutiny if they check the reference.",
    "FAKTUAL diversity claim overstated: The proposal states 'RoboMimic Transport has highest demonstration diversity' citing FAKTUAL. The actual paper shows Transport's entropy 'does not saturate,' indicating greater per-demo novelty than Can, but does not make a blanket 'highest diversity' declaration across all benchmarks. The claim should be qualified.",
    "Empirical advantage over SCIZOR remains the central uncertainty: SCIZOR already achieves transition-level filtering with categorical diagnostic profiles (Laggy Motion, Manipulation Failure, Pause, Stuck at Collision, Move Back and Forth — 6 categories, not 4 as stated). PhaseOT's claimed advantages (semantic phase-level vs. transition-level, mode-awareness, distributional guarantees) are theoretically well-motivated but the practical superiority is uncertain. Experiment E3 (phase-level vs. transition-level recovery) is the right experiment to run, but until results exist, this is the paper's biggest risk.",
    "The phase-localized contamination model evidence is indirect: The proposal argues that SCIZOR's failure taxonomy and RoboMimic's Tool Hang analysis document phase-localized failures. This is true but these are post-hoc interpretations of observed failure modes, not direct measurements of contamination distribution in training datasets. The graceful degradation analysis (recovering trajectory-level performance when contamination is distributed) partially mitigates this concern but the core assumption needs stronger empirical validation — e.g., actually measuring the phase-localized vs. distributed noise ratio in RoboMimic MH datasets.",
    "Minor: SCIZOR has 6 suboptimal type categories, not 4 as listed in the proposal (missing 'Move Back and Forth' and 'False Positive'). The 'Laggy Motion' label is from the v2 revision; v1 used 'Slow Motion.' These are minor accuracy issues but matter for credibility."
  ],
  "feedback": "The proposal has matured significantly across 5 rounds — the landscape is now genuinely best-in-class, the approach is precisely specified, the experimental design targets unique capabilities, and the theoretical claims are honestly scoped. However, several issues prevent a pass:\n\n**Priority 1 — Fix the fabricated FIDeL citation**: Replace with the correct citation: FLOAT within ARMADA (Wenye Yu et al., arXiv 2510.02298, Oct 2025). FLOAT uses OT for online deployment-time failure detection via per-timestep trajectory matching against expert demonstrations. The key distinction from PhaseOT is: FLOAT operates online during deployment (not offline curation), uses trajectory-level OT matching (not phase-structured), and requires expert references (not unsupervised mode discovery).\n\n**Priority 2 — Resolve the CoRL 2026 impossibility**: This has been flagged 5 consecutive times. Options: (a) Accept AAAI 2027 as the target and explicitly state this to the user with a clear timeline advantage explanation (~2.5 months of development time); (b) If a CoRL 2026 workshop paper is desired, note that workshop submission deadlines have not been announced yet and cannot be guaranteed; (c) Propose a concrete scoped-down plan for CoRL 2026 workshops: 4-page paper, Push-T + RoboMimic Can only, preliminary PW₂ results without full mode discovery or theoretical analysis.\n\n**Priority 3 — Fix reference accuracy issues**: (a) Correct Cheng & Liu algorithm description from 'iterative reweighting scheme' to 'free-support IBP variant with fixed-point iteration'; (b) Qualify the FAKTUAL diversity claim; (c) Update SCIZOR's category count from 4 to 6 and note the Laggy/Slow Motion naming difference.\n\n**Priority 4 — Strengthen the SCIZOR differentiation narrative**: SCIZOR is the primary competitor and its capabilities are stronger than the proposal acknowledges. The differentiation should be sharpened: (a) PhaseOT produces phase-level quality profiles (approach=nominal, grasp=3.2σ anomalous) vs. SCIZOR's per-transition binary flags + post-hoc categorical labels; (b) PhaseOT's mode discovery prevents penalizing minority strategies, which SCIZOR cannot do; (c) PhaseOT's distributional distances have concentration guarantees, while SCIZOR's progress prediction is heuristic. But acknowledge honestly that SCIZOR already achieves partial trajectory recovery, so PhaseOT's advantage must come from the quality of recovery (semantic coherence) and mode awareness, not the existence of sub-trajectory capability.\n\n**Priority 5 — Provide direct evidence for phase-localized contamination**: Rather than relying on post-hoc interpretation of SCIZOR's failure taxonomy, propose a concrete measurement: analyze RoboMimic MH 'worse' and 'okay' operator data by segmenting into phases and measuring per-phase deviation from 'better' operator data. Report whether contamination is indeed phase-concentrated. This would transform the assumption from 'reasonable intuition' to 'empirically grounded hypothesis.'\n\n**What's working well**: The Phase-Structured Wasserstein Distance (PW₂) is a clean, well-motivated formulation. The mode discovery + per-mode scoring addresses a genuine gap. The experimental design (especially E1 bimodal preservation, E2 phase-diagnosis accuracy, E3 phase vs. transition recovery) targets PhaseOT's unique capabilities. The two-tier computation strategy is practical. The honest positioning against adapted OT theory shows research maturity.",
  "reason": "Strong proposal with comprehensive landscape and well-specified approach, but fabricated FIDeL citation, persistent CoRL 2026 venue mismatch, and several reference accuracy issues prevent passing. Average score 3.5 < 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb139ded-86da-40ea-b50d-d4668755ebe4",
  "isSidechain": false,
  "requestId": "req_011CazSngvzQo6JbUNecBdmm",
  "type": "assistant",
  "uuid": "02d47324-f336-4857-b231-8656d491ce15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jt8VaqCH2qNGS4yUgfozGo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5057,
      "cache_read_input_tokens": 48853,
      "output_tokens": 4644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4644,
          "cache_read_input_tokens": 48853,
          "cache_creation_input_tokens": 5057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5057
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "02d47324-f336-4857-b231-8656d491ce15",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PhaseOT demo quality diagnosis idea (Round 5)",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "02d47324-f336-4857-b231-8656d491ce15",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify PhaseOT demo quality diagnosis idea (Round 5)",
  "sessionId": "29db5b43-7986-4f2e-9840-40109a8a2d7f"
}
```

---
