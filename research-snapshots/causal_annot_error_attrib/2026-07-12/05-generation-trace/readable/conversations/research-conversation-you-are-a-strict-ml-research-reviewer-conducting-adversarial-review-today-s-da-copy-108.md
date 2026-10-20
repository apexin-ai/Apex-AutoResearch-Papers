# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-14 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 119
- **Recorded user turns:** 1
- **Tool calls:** 36
- **Original source:** `logs/chats/exported-trajectories/account-1/d191e023-538e-4ee0-ba64-e2dc7a3a305e.jsonl`
- **Structured JSON:** [`13c3a129801d7902c497.json`](../../sessions/13/13c3a129801d7902c497.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T06:56:22.849Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T06:56:22.849Z",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-14 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **按照以下方向，生成1-2个优质idea，保质不求量：Token-Level Representation Surgery for VLA Robustness\nTarget: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).\nDirection: Token pruning and augmentation in VLA visual representations — methods that surgically manipulate visual tokens in latent space to improve VLA generalization under realistic perturbations. The core theoretical insight is that VLA visual encoders produce highly redundant token sequences where task-irrelevant tokens (background clutter, static scene regions, occluded areas) dominate attention budgets and create brittle feature correlations. By pruning uninformative tokens and augmenting critical ones in representation space (not pixel space), we compress the effective visual input to a task-relevant manifold that is inherently more robust to distribution shift. Theoretical grounding includes: (1) Information Bottleneck — pruning enforces a tighter bottleneck that retains only task-sufficient statistics, provably improving generalization bounds; (2) Attention Entropy Reduction — concentrating attention mass on fewer, more informative tokens reduces sensitivity to perturbations in pruned regions; (3) Manifold Regularization — augmenting retained tokens along the tangent space of the learned representation manifold provides robustness without leaving the data support. In-scope: adaptive token pruning based on action-relevance scoring, latent-space token augmentation via interpolation/extrapolation on task-critical tokens, attention-guided token selection with theoretical guarantees on information retention, combined prune-and-augment pipelines that maintain action prediction quality while improving robustness to visual distractors, lighting changes, viewpoint shifts, and occlusion.\nRecent landscape (do not duplicate): Helix-style self-correction, CacheVLA,LightVLA,TraceVLA, RoboPro, retry/reflection wrappers around VLAs, FastVLA token merging (efficiency-only, no robustness analysis), TokenLearner fixed-count compression. Robustness as benchmark-only is saturated — must propose a method with theoretical motivation.\nContribution type: METHOD ONLY. New training algorithm combining action-conditioned token pruning with latent manifold augmentation: (1) a differentiable token relevance scorer trained with auxiliary action-prediction loss to identify which visual tokens carry task-critical information, (2) a prune-then-augment pipeline that removes low-relevance tokens and performs controlled perturbation of high-relevance tokens in latent space, (3) theoretical analysis showing the pruning step tightens the information bottleneck bound while augmentation smooths the action-prediction landscape, yielding provable robustness margins.\nEVAL PROTOCOL — IMPORTANT:\nTRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90).\nEVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.\nReport robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).\nAdditionally report token reduction ratio vs. robustness improvement curve, and ablate pruning-only vs. augmentation-only vs. combined.\nExperiments can be extended to other benchmark series (e.g., CALVIN with perturbation variants) to verify cross-benchmark robustness.\nSIM-ONLY MITIGATION: Robustness eval in sim is well-accepted at CoRL — established LIBERO-PLUS / LIBERO-PRO style suites are a recognized sim-only pattern.\nHARD CONSTRAINTS:\nCompute: ≤200 H100-hours total. Fine-tune from open VLA checkpoints (OpenVLA, SmolVLA, OpenPi, π0) — no pretraining. Token pruning/augmentation adds negligible overhead. Show the math.\nTime: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers.\nEval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.\nLook for: action-conditioned token relevance scoring that adapts per-timestep, latent-space augmentation that exploits the geometry of VLA's representation manifold, information-theoretic pruning criteria with provable bounds, attention entropy as a proxy for robustness, connections between token sparsity and flat minima in action space. Avoid: vanilla pixel-space data augmentation without latent-space method, static/fixed pruning ratios without adaptivity, pure efficiency-motivated token reduction rebranded as robustness, just-add-noise training.\nTag: direction=robust_vla, contribution_type=method, sub_direction=token_surgery, target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-14?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Action-Conditioned Information Bottleneck Token Surgery for Robust VLAs\",\n  \"core_problem\": \"VLA visual encoders produce redundant token sequences where task-irrelevant tokens carry spurious correlations with environment-specific factors — correlations that collapse under visual perturbations. Existing token pruning methods (VLA-IAP, LightVLA, GridS, DTP, Compressor-VLA, SP-VLA, VLA-Pruner, ETA-VLA, EcoVLA, FocusVLA) optimize exclusively for inference efficiency or clean-condition accuracy, while existing robustness methods operate at other levels: policy-level regularization (RobustVLA), input restoration (CRT), or lightweight affine token modulation (FTM, which uses input-independent global parameters). Critically, post-hoc token compression has been shown to actively HURT adversarial robustness by concentrating adversarial signal on high-importance retained tokens (arXiv 2601.21531, 2601.12042). The position paper 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues exactly this thesis but provides no concrete VLA instantiation. TCA (ICCV 2025) provides preliminary evidence that token condensation can improve distribution shift robustness in classification (+21.4% on CIFAR-100-C), but operates training-free at test time without action conditioning. SimPrune (ICLR 2025) enforces cross-branch augmentation consistency during token pruning in self-supervised pretraining, but targets training efficiency rather than deployment robustness. FocusVLA (arXiv 2603.28740) dynamically selects task-relevant visual tokens via cross-attention-based top-K selection, achieving 98.7% on LIBERO — but targets clean-condition accuracy using attention magnitude scores without IB objectives, augmentation consistency, or robustness evaluation under visual perturbations. We show that token-level intervention CAN improve VLA robustness — when the token scorer is jointly trained with an information bottleneck objective using multi-view augmentation consistency that implicitly decorrelates from nuisance variables, producing perturbation-invariant relevance scores fundamentally different from both attention-based importance used in post-hoc methods and FocusVLA, input-independent affine modulation used in FTM, and cross-branch similarity matching used in SimPrune.\",\n  \"opportunity\": \"LIBERO-Plus (CVPR 2026) reveals catastrophic robustness gaps (95% → <30% under camera/state perturbations), with current SOTA at SRPO 82.1% avg. FTM (arXiv 2512.02902) shows that even a simple global affine transformation on visual tokens recovers viewpoint robustness (48.5% → 87.1% on π0.5 with 4K params), demonstrating that token-level intervention is a promising robustness lever — but FTM's input-independent, fixed-parameter design cannot adapt to scene content, varies in effectiveness across perturbation types, and lacks information-theoretic grounding. BC-IB (ICML 2025) demonstrates that IB at the representation level improves clean accuracy on LIBERO but explicitly acknowledges robustness to domain shifts as an open problem. TCA (ICCV 2025) demonstrates that token condensation improves distribution shift robustness in ViT classification by up to 21.4%, providing direct supporting evidence that the token-reduction-for-robustness direction is viable — but TCA is training-free, task-agnostic, and untested on embodied action prediction. SimPrune (ICLR 2025) shows cross-branch consistency can guide token pruning in SSL, but targets pretraining efficiency without an IB objective or robustness evaluation. FocusVLA (arXiv 2603.28740) demonstrates that cross-attention-based top-K token selection achieves excellent clean accuracy (98.7% on LIBERO with 256 of 512 tokens retained) — but operates on architectures with large token budgets (512 tokens) without IB grounding or perturbation robustness evaluation, leaving the question of whether attention-based selection degrades gracefully under visual perturbations entirely open. The unexploited gap is: applying IB at the TOKEN level with ADAPTIVE, INPUT-DEPENDENT selection, conditioned on ACTION prediction, using MULTI-VIEW augmentation consistency to achieve perturbation invariance — a combination that provides principled, per-timestep token selection with information-theoretic motivation, going beyond FTM's fixed modulation, BC-IB's coarse-grained bottleneck, TCA's training-free approach, SimPrune's efficiency-focused consistency, and FocusVLA's accuracy-driven attention selection.\",\n  \"landscape\": \"The VLA token intervention literature spans efficiency, accuracy-driven selection, modulation, and robustness approaches. EFFICIENCY-FOCUSED PRUNING: VLA-IAP (Mar 2026) achieves 97.8% on LIBERO with 1.54x speedup via training-free interaction-aligned pruning; LightVLA (ICRA 2026) uses differentiable Gumbel softmax selection reducing FLOPs by 59.1%; GridS (ICML 2026) performs differentiable grid resampling; Compressor-VLA uses instruction-guided dual compression; DTP prunes distracting tokens for accuracy not perturbation robustness; SP-VLA (ICLR 2026, arXiv 2506.12723) jointly schedules models and prunes tokens via spatio-semantic dual-aware importance; VLA-Pruner (arXiv 2511.16449) uses dual-level importance combining prefill attention and temporal-smoothed action decode attention; ETA-VLA (arXiv 2603.25766) performs temporal fusion with intra-LLM sparsification; EcoVLA (arXiv 2602.00780) applies environment-aware adaptive pruning as a training-free plug-and-play framework; OneWM-VLA (arXiv 2605.07931) compresses each view to one token via adaptive attention pooling. ACCURACY-DRIVEN TOKEN SELECTION: FocusVLA (arXiv 2603.28740, March 2026) dynamically selects task-relevant visual tokens via cross-attention-based top-K selection between action queries and vision keys, achieving 98.7% on LIBERO (multi-weight) with a 0.5B model (Qwen2.5-0.5B + DINOv2/SigLIP, 342.7M trainable params). FocusVLA retains 256 of 512 raw tokens (50% retention), demonstrating that attention-guided selection improves clean accuracy — but it does NOT use IB objectives, augmentation consistency, or robustness evaluation under visual perturbations. Its cross-attention scores reflect task relevance under nominal conditions but may not remain stable under domain shift, since attention-based importance is itself perturbed under visual corruption (the same vulnerability documented for post-hoc pruning in arXiv 2601.21531). ACIBS differs from FocusVLA in three fundamental ways: (1) IB-grounded scoring vs. attention-magnitude selection, (2) multi-view consistency training for perturbation invariance vs. clean-condition-only training, (3) robustness as the primary objective vs. accuracy. TOKEN-LEVEL MODULATION: FTM (arXiv 2512.02902) applies an input-independent global affine transformation F̂=(1+γ)⊙F+β to visual tokens from π0.5's ViT encoder, achieving camera 87.1%, lighting 96.0%, texture 96.0%, noise 93.6% on LIBERO-V with only 4K params — remarkably effective but limited by: (a) input-independence (same γ,β regardless of scene content), (b) tested only on π0.5 (3B+ params), not compact models like SmolVLA, (c) no token selection/pruning (all tokens retained), (d) no information-theoretic grounding. FLA extends FTM with low-rank ViT updates (4.7M params, 90.8%) but requires encoder modification. AUGMENTATION-CONSISTENT TOKEN METHODS: SimPrune (ICLR 2025) enforces cross-branch cosine similarity matching for token-pair pruning during self-supervised pretraining — conceptually related to ACIBS's consistency loss but differs in three key ways: (1) SimPrune targets training efficiency in SSL dual-branch architectures, not deployment robustness in VLAs; (2) SimPrune uses pairwise cosine similarity for token matching, not an IB-grounded scoring head; (3) SimPrune prunes matched token pairs to reduce compute, not to select perturbation-invariant tokens for action prediction. TCA (ICCV 2025, arXiv 2410.14729) demonstrates that training-free token condensation improves distribution shift robustness by up to 21.4% on CIFAR-100-C via reservoir-based domain anchor tokens — directly supporting the token-reduction-for-robustness thesis but operating training-free, at test time, without action conditioning or IB objectives. IB FOR ROBOTICS: BC-IB (ICML 2025, arXiv 2502.02853) applies IB at the REPRESENTATION level in behavior cloning, minimizing I(X;Z) on the full latent vector — improves clean accuracy by +5.6% on LIBERO but does not operate at token granularity and explicitly notes domain-shift robustness as unstudied. IBTM (OpenReview) combines IB with learnable token merging for ViT efficiency but targets FLOPs reduction on classification without action conditioning or robustness evaluation. MULTI-VIEW IB: DRIBO (ICML 2022) uses augmentation-generated paired views with a contrastive MIB objective to learn robust RL representations — directly inspiring our nuisance-invariant token selection approach but operating at representation level, not token selection level. MIB (Federici et al., ICLR 2020) provides the theoretical foundation for multi-view IB without nuisance labels. VLA ROBUSTNESS: RobustVLA (arXiv 2511.01331) applies Jacobian + smoothness regularization during online RL post-training (~82.5% on observation perturbations). CRT (arXiv 2602.01158) uses a corruption restoration transformer as preprocessing. SRPO achieves 82.1 on LIBERO-Plus via self-referential RL policy optimization (current LIBERO-Plus SOTA). AVA-VLA (arXiv 2511.18960) introduces active visual attention that dynamically reweights visual tokens based on instruction and execution history, achieving 74.7% avg on LIBERO-Plus — relevant as it also performs dynamic token reweighting, but uses POMDP-motivated attention reweighting for clean generalization rather than IB-grounded selection for perturbation invariance. COUNTER-EVIDENCE: arXiv 2601.21531 and 2601.12042 demonstrate that POST-HOC token compression hurts adversarial robustness via the 'distortion concentrator' effect — but these exclusively evaluate training-free compression with attention-based importance scores that are themselves perturbed. Fischer et al. (2021, arXiv 2107.05712) show that VIB's apparent adversarial robustness in classification is partly attributable to gradient obfuscation rather than provable guarantees — motivating our empirical rather than certified robustness framing. POSITION PAPER: 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues the thesis that token reduction should target robustness/quality, not just efficiency — ACIBS is the first concrete VLA instantiation of this vision.\",\n  \"approach\": \"We train a lightweight differentiable token scoring head atop SmolVLA's visual encoder (SmolVLM-2: SigLIP vision encoder + SmolLM2 language decoder, 450M total params with ~100M action expert, 64 visual tokens per frame) that is jointly optimized with action prediction and a multi-view augmentation-consistent Information Bottleneck (IB) objective. COMPACT TOKEN SPACE ANALYSIS: SmolVLA's 64 visual tokens per frame — produced via 3×3 pixel shuffle (9× spatial reduction) — represent an already-aggressive compression. We explicitly study how further IB-guided pruning interacts with this compact space via a retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9}, corresponding to 32, 38, 45, 51, and 58 tokens retained. Key observations: (a) Even k=0.8 prunes 13 tokens — sufficient to remove background-dominated tokens while preserving manipulation-critical spatial information, since SmolVLA's pixel-shuffle tokens are spatially localized and many correspond to static background regions. (b) The IB objective's KL term provides per-sample ADAPTIVE retention: the prior p_0(m) sets a SOFT target retention rate, not a hard cutoff. In practice, this means the effective retention varies per-timestep — scenes with cluttered backgrounds may retain fewer tokens (e.g., k_eff ≈ 0.6), while visually sparse manipulation scenes retain more (k_eff ≈ 0.9). This adaptive behavior is a key advantage over fixed-rate pruning methods. (c) Unlike FocusVLA which prunes from 512 to 256 tokens (50% retention with substantial redundancy), pruning from 64 tokens operates in a regime where each token carries high information density. This motivates our IB formulation: the VIB term ensures that pruning decisions maximize retained action-relevant information per token, while the consistency term ensures these decisions are perturbation-invariant. We report both nominal and perturbed accuracy at each k to characterize the robustness-efficiency Pareto frontier in this compact token space. The key methodological advance is the REFORMULATED IB OBJECTIVE that eliminates the need for explicit nuisance variable labels or conditional MI estimation. Instead of minimizing I(V_selected; N | A) — which requires access to nuisance factor samples N — we adopt a multi-view consistency approach inspired by DRIBO (ICML 2022) and MIB (Federici et al., ICLR 2020): during training, each observation X is paired with an augmented view X' generated via domain randomization (camera jitter ±15°, color/lighting perturbation, background texture swap using LIBERO's built-in randomization). Both views pass through SmolVLA's frozen SigLIP encoder to produce token sequences V and V'. The combined training loss is: L = L_action(f(V_m), A) + α·D_KL(q(m|V) || p_0(m)) + β·||S(V) - S(V')||². The first term maximizes action-prediction accuracy from selected tokens. The second term is a VIB-style token-level bottleneck: q(m|V) is the per-token Bernoulli selection distribution parameterized by the scorer MLP via Gumbel-softmax relaxation (architecturally following LightVLA's differentiable selection), and p_0(m) is a Bernoulli prior with target retention rate k — this forces compression of redundant information. The third term is the CROSS-VIEW SELECTION CONSISTENCY loss: it penalizes differences in the scorer's output logits S(·) across augmented views, forcing the scorer to be INVARIANT to augmentation-defined nuisance factors. This formulation uses only standard KL divergence and MSE — no neural MI estimation required, sidestepping the bias/variance issues of variational MI bounds (Poole et al., ICML 2019). The augmentation pipeline implicitly defines nuisance variables: any information that varies across views (background, lighting, viewpoint) is nuisance, and the consistency loss forces the scorer to ignore it. We note the conceptual connection to SimPrune (ICLR 2025), which also uses cross-branch consistency for token pruning — but SimPrune operates in SSL pretraining using cosine similarity for efficiency-driven token-pair matching, while ACIBS operates in VLA fine-tuning using an IB-grounded scorer for robustness-driven token selection, representing a fundamentally different objective and mechanism. The scorer is implemented as a 2-layer MLP (~50K params) predicting per-token logits, with Gumbel-softmax producing differentiable soft masks during training and hard top-k selection during inference. DIFFERENTIATION FROM FocusVLA: FocusVLA uses cross-attention scores between action queries and vision keys for top-K selection in a 512-token space, optimizing clean-condition accuracy without IB or consistency objectives. ACIBS differs in: (1) IB-grounded scoring that compresses information-theoretically vs. attention-magnitude selection, (2) multi-view consistency for perturbation-invariant scores vs. nominal-only training, (3) operation in SmolVLA's compact 64-token space where each pruning decision carries higher impact, (4) robustness as primary objective vs. accuracy. FocusVLA's attention-based scores are themselves susceptible to perturbation-induced drift (the same failure mode documented for post-hoc pruning), while ACIBS's consistency-trained scorer is explicitly trained to be invariant to such perturbations. THEORETICAL FRAMING: We frame ACIBS with information-theoretic motivation rather than provable robustness certificates. The VIB term upper-bounds the mutual information I(X;M) between input tokens and selected mask, encouraging compression; the consistency term empirically enforces invariance to augmentation-defined nuisance factors. We do NOT claim certified robustness margins — Fischer et al. (2021) demonstrated that VIB's apparent adversarial robustness in classification is partly attributable to gradient obfuscation, and certified bounds would require additional assumptions (Lipschitz continuity, bounded perturbation sets) beyond what VIB alone provides. Instead, our contribution is an empirically grounded method that achieves perturbation invariance through the joint training of IB compression and augmentation consistency, validated on LIBERO-Plus. FTM BASELINE CONTINGENCY: If FTM adapted to SmolVLA recovers most of the robustness gap (e.g., >75% avg on LIBERO-Plus), our contribution shifts to demonstrating that adaptive, input-dependent, per-token selection with IB grounding provides COMPLEMENTARY gains — we evaluate FTM+ACIBS (global affine modulation followed by IB-guided selective pruning) and show the combination exceeds either alone by leveraging both feature recalibration and information-theoretic token filtering. This compositional result would be novel regardless of FTM's standalone strength. PROGRESSIVE SUBMISSION STRATEGY: Given the 15-day timeline (abstract May 26, paper May 29), we define a minimal viable submission (MVS) and ideal submission. MVS (non-negotiable): ACIBS standalone with retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9}, ablations isolating VIB and consistency terms, 4 perturbation dimensions (camera, lighting, texture, noise), comparison against SmolVLA baseline and FTM-SmolVLA. Ideal submission (if time permits): adds FTM+ACIBS combination experiment, additional baselines (VLA-IAP, BC-IB), and per-dimension analysis. The FTM+ACIBS combination experiment is deferred to camera-ready if time runs short. This strategy requires prior familiarity with SmolVLA/LeRobot codebase and LIBERO evaluation infrastructure — the timeline is feasible for a researcher who has already worked with these tools but would not be achievable starting from scratch. Key differentiation from prior work: (a) vs. FTM — adaptive, input-dependent, per-token selection with IB motivation vs. input-independent global affine modulation; FTM retains all tokens with shifted features, ACIBS selects informative tokens and discards nuisance-carrying ones; composable as FTM+ACIBS; (b) vs. BC-IB — token-level vs. representation-level IB, robustness-targeted via multi-view consistency vs. accuracy-targeted; (c) vs. DRIBO — token selection level vs. representation level, action-conditioned for manipulation; (d) vs. post-hoc pruning — trained perturbation-invariant scorer vs. unstable attention-based importance; (e) vs. SimPrune — IB-grounded action-conditioned robustness scorer vs. cosine-similarity efficiency matcher in SSL; (f) vs. TCA — trained, action-conditioned IB selection vs. training-free, task-agnostic condensation; (g) vs. IBTM — action-conditioned and robustness-evaluated vs. task-agnostic efficiency; (h) vs. FocusVLA — IB-grounded perturbation-invariant scoring in compact 64-token space vs. attention-based accuracy-driven selection in 512-token space without robustness evaluation or information-theoretic grounding. We evaluate on LIBERO-Plus across 4 key perturbation dimensions (camera, lighting, texture, noise) for the primary CoRL submission, with full 7-dimension evaluation deferred to extended version. Baselines include efficiency-focused pruning (VLA-IAP, DTP), accuracy-driven selection (FocusVLA), token modulation (FTM adapted to SmolVLA backbone), robustness methods (RobustVLA, CRT, SRPO), and the representation-level IB approach (BC-IB), plus ablations isolating the VIB term and consistency term, retention rate sweep, and the FTM+ACIBS combination (time permitting, else camera-ready).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~155-185h H100 (SmolVLA base: ~4h/run; with IB scorer + dual-view forward pass: ~12h/run; 5 retention rate configs × 12h = 60h training; LIBERO-Plus eval on 4 perturbation dims ~5h per model × 5 models (ACIBS-best-k, FTM-SmolVLA, 2 ablations, baseline) = 25h; retention rate sweep eval ~15h; baseline reproductions ~25h; debugging/iteration ~30-40h; total ~155-165h within 200h budget with ~35h margin)\",\n      \"gpu_utilization\": \"Moderate idle (35-45%) — researcher iterates on α/β trade-off and analyzes per-dimension robustness curves between runs\",\n      \"timeline\": \"12-15 days (abstract by May 26, paper by May 29 CoRL 2026). Requires prior familiarity with SmolVLA/LeRobot and LIBERO infrastructure. Progressive submission: MVS (ACIBS + ablations + retention sweep) guaranteed; FTM+ACIBS combination deferred to camera-ready if needed\",\n      \"team\": \"1-2 researchers with existing SmolVLA/LIBERO experience\",\n      \"estimated_gpu_cost\": \"$390-$465 (at ~$2.50/hr H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~145-175h H100 (agent systematically sweeps α/β/k retention rate; human approves VIB/consistency/action-loss trade-off at each checkpoint; dual-view augmentation adds ~40% overhead per training run vs. standard SmolVLA fine-tuning; retention rate sweep adds ~20h)\",\n      \"gpu_utilization\": \"20-30% lower idle vs manual — agent queues next run while human reviews robustness vs. clean accuracy trade-offs\",\n      \"timeline\": \"10-12 days\",\n      \"team\": \"1 researcher with SmolVLA/LIBERO experience, ~1.5hr/day reviewing trade-off curves and selecting augmentation strategies\",\n      \"claude_api_cost\": \"$80-150 (estimated ~800-1500 turns for experiment design, augmentation pipeline setup, result analysis)\",\n      \"estimated_gpu_cost\": \"$365-$440\",\n      \"risk_note\": \"α/β/k tuning is the critical human decision loop — α too high destroys action-relevant signal in SmolVLA's compact 64-token space, β too high forces trivially constant selection that ignores scene content, k too low (e.g., 0.5) may lose spatial coverage needed for precise manipulation. The dual-view augmentation pipeline must be carefully calibrated: augmentations too weak fail to define meaningful nuisance, too strong create views where task-relevant information also differs\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~175-195h H100 (more exploration of α/β/k hyperparameter space including full retention rate sweep; includes failed runs; fits within 200h budget with scoped 4-dimension eval and MVS scope)\",\n      \"gpu_utilization\": \"Near-zero idle — agent continuously pipelines training → evaluation → next experiment\",\n      \"timeline\": \"8-12 days with 2 H100 GPUs\",\n      \"team\": \"0 (initial setup only, assumes pre-configured SmolVLA/LIBERO environment)\",\n      \"claude_api_cost\": \"$200-350\",\n      \"estimated_gpu_cost\": \"$440-$490\",\n      \"speed_bottleneck\": \"LIBERO-Plus evaluation throughput — ~5h per 4-dimension evaluation pass per model on single GPU; retention rate sweep multiplies eval cost by 5×\",\n      \"risk_note\": \"Agent may over-explore hyperparameter space without convergence intuition; multi-view augmentation magnitude is sensitive and agent may not distinguish meaningful augmentation failures from hyperparameter failures. The 200h budget is tight with 5-point retention sweep — agent should use early stopping on clearly failing k values\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract: May 26 11:59 UTC, paper: May 29 11:59 UTC — PRIMARY TARGET, progressive submission: MVS = ACIBS + retention rate sweep + ablations on 4 perturbation dims; ideal = + FTM+ACIBS combination + extended baselines; 15-day timeline from today May 14, requires prior SmolVLA/LIBERO familiarity)\",\n    \"AAAI 2027 (deadlines TBD, likely ~August 2026 — extended version with full 7-dimension LIBERO-Plus evaluation, FTM+ACIBS combination if deferred, tangent-space augmentation ablation, multi-backbone experiments on π0.5)\",\n    \"ICLR 2027 (deadline ~October 2026 — most comprehensive version with compositional perturbations and theoretical analysis)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\",\n    \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025, 2506.01844)\",\n    \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation [BC-IB] (ICML 2025, arXiv 2502.02853)\",\n    \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2025, 2512.02902)\",\n    \"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2026, 2603.28740)\",\n    \"Token Reduction Should Go Beyond Efficiency in Generative Models — From Vision, Language to Multimodality (arXiv 2025, 2505.18227)\",\n    \"Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning [SimPrune] (ICLR 2025)\",\n    \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation [TCA] (ICCV 2025, arXiv 2410.14729)\",\n    \"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck (ICML 2022)\",\n    \"Learning Robust Representations via Multi-View Information Bottleneck [MIB] (ICLR 2020, arXiv 2002.07017)\",\n    \"A Closer Look at the Adversarial Robustness of Information Bottleneck Models (Fischer et al., 2021, arXiv 2107.05712)\",\n    \"CLUB: A Contrastive Log-ratio Upper Bound of Mutual Information (ICML 2020)\",\n    \"On Variational Bounds of Mutual Information (Poole et al., ICML 2019)\",\n    \"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging [IBTM] (OpenReview 2024)\",\n    \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models (arXiv 2025, 2511.01331)\",\n    \"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs [CRT] (arXiv 2026, 2602.01158)\",\n    \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2025, 2511.15605)\",\n    \"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (arXiv 2025, 2511.18960)\",\n    \"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression (arXiv 2026, 2601.21531)\",\n    \"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models (arXiv 2026, 2601.12042)\",\n    \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models (arXiv 2026, 2603.22991)\",\n    \"The Better You Learn, The Smarter You Prune: Towards Efficient VLAs via Differentiable Token Pruning [LightVLA] (ICRA 2026)\",\n    \"See What Matters: Differentiable Grid Sample Pruning for Generalizable VLA [GridS] (ICML 2026)\",\n    \"DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2026, 2601.16065)\",\n    \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2025, 2511.18950)\",\n    \"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2025, 2511.16449)\",\n    \"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification (arXiv 2026, 2603.25766)\",\n    \"EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration (arXiv 2026, 2602.00780)\",\n    \"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy [OneWM-VLA] (arXiv 2026, 2605.07931)\",\n    \"Deep Variational Information Bottleneck (Alemi et al., ICLR 2017, arXiv 1612.00410)\",\n    \"Token Bottleneck: One Token to Remember Dynamics [ToBo] (NeurIPS 2025, arXiv 2507.06543)\",\n    \"First-Order Manifold Data Augmentation for Regression Learning [FOMA] (ICML 2024)\"\n  ],\n  \"description\": \"We propose Action-Conditioned Information Bottleneck Token Surgery (ACIBS), a method that reconceptualizes VLA visual token selection from an efficiency optimization into a robustness mechanism. Current VLA models achieve >95% success on standard benchmarks but collapse to <30% under visual perturbations (LIBERO-Plus, CVPR 2026), with the current SOTA (SRPO) at 82.1% average. Existing token pruning methods (VLA-IAP, LightVLA, GridS, DTP, SP-VLA, VLA-Pruner, ETA-VLA, EcoVLA) target inference speed; accuracy-driven selection methods like FocusVLA (arXiv 2603.28740) achieve excellent clean accuracy (98.7% via cross-attention top-K) but lack IB grounding and robustness evaluation; post-hoc compression actively hurts adversarial robustness via the 'distortion concentrator' effect (arXiv 2601.21531, 2601.12042); and FTM (arXiv 2512.02902) achieves strong viewpoint robustness (87.1% on π0.5) via a simple input-independent global affine transformation on visual tokens — but its fixed parameters cannot adapt to scene content. Meanwhile, BC-IB (ICML 2025) applies IB at the representation level for clean accuracy without addressing token-level robustness; TCA (ICCV 2025) demonstrates that token condensation improves distribution shift robustness by up to 21.4% in classification but is training-free and task-agnostic; SimPrune (ICLR 2025) enforces cross-branch augmentation consistency for token pruning in SSL pretraining but targets efficiency; and 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues this thesis without a concrete VLA method. ACIBS bridges these gaps with a fundamentally different formulation: a differentiable token scorer jointly trained with action prediction and a MULTI-VIEW AUGMENTATION-CONSISTENT IB objective. Built on SmolVLA (SmolVLM-2: SigLIP vision encoder + SmolLM2 language decoder, 450M params, 64 visual tokens per frame), the combined loss is L = L_action + α·D_KL(q(m|V) || p_0(m)) + β·||S(V) - S(V')||², where the VIB term compresses token information and the consistency term forces the scorer to be INVARIANT to augmentation-defined nuisance factors. A critical design consideration is that SmolVLA's 64 tokens (via 3×3 pixel shuffle, 9× reduction) already represent aggressive compression. We address this via a retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9} (32-58 tokens retained), with the IB objective's KL term providing per-sample ADAPTIVE retention — the prior p_0 sets a soft target, allowing the effective retention to vary per-timestep based on scene content. Even k=0.8 prunes 13 tokens, sufficient to remove background-dominated spatial regions while preserving manipulation-critical information. Unlike FocusVLA which prunes from 512 to 256 tokens with substantial redundancy, ACIBS operates in a compact regime where each pruning decision carries high impact, making IB-guided selection especially valuable. We frame this with information-theoretic motivation rather than certified robustness guarantees — Fischer et al. (2021) showed VIB's apparent adversarial robustness is partly gradient obfuscation, so we target empirical perturbation invariance through joint IB compression and augmentation consistency, not provable bounds. The approach extends DRIBO's multi-view IB principle from representation-level RL to token-level VLA selection. We explicitly plan for a strong FTM baseline: if FTM adapted to SmolVLA achieves >75% avg on LIBERO-Plus, we demonstrate FTM+ACIBS (global modulation + IB-guided selection) exceeds either alone, showing the approaches are complementary. Primary target is CoRL 2026 (abstract May 26, paper May 29) with a progressive submission strategy: minimal viable submission (ACIBS + retention rate sweep + ablations, 4 perturbation dimensions) guaranteed by deadline; FTM+ACIBS combination deferred to camera-ready if needed. Timeline requires prior SmolVLA/LeRobot and LIBERO familiarity. Strict 200h H100 compute budget (~155h estimated). Baselines include FTM (adapted to SmolVLA), accuracy-driven selection (FocusVLA), efficiency-focused pruning (VLA-IAP, DTP), robustness methods (RobustVLA, CRT, SRPO), and the representation-level IB approach (BC-IB), plus ablations isolating the VIB term and consistency term, retention rate sweep, and the FTM+ACIBS combination.\",\n  \"project_name\": \"ib_token_surgery_vla\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"FATAL COMPUTE MISMATCH: The idea proposes OpenVLA-OFT (7B params, 8×A100 for 24-48h per run = 192-384 GPU-hours per run) but user's hard constraint is ≤200 H100-hours total. A single training run exhausts the entire budget with zero room for ablations, hyperparameter tuning, or evaluation. The idea's own resource estimate (2000-3000h) confirms this is 10-15x over budget.\", \"MISSED CRITICAL PRIOR WORK: BC-IB (ICML 2025, arXiv 2502.02853) already applies Information Bottleneck to behavior cloning for robot manipulation on LIBERO, reducing MI to 1/4 and improving LIBERO-Goal by +7.7%. The claim of being 'first to use IB for VLA robustness' is significantly weakened.\", \"MISSED CRITICAL PRIOR WORK: IBTM (under review, OpenReview) directly combines IB principle with learnable token merging in vision transformers — exactly the IB + token selection combination claimed as novel.\", \"MISSED COMPETITOR: RobustVLA (arXiv 2511.01331, ICLR 2026 submission) achieves +12.6% robustness on pi0 and +10.4% on OpenVLA across 17 perturbations via Jacobian + smoothness regularization — a direct robustness method for VLAs that must be compared against.\", \"MISSED COMPETITOR: Token Bottleneck / ToBo (NeurIPS 2025, arXiv 2507.06543) uses a bottleneck token concept for robot manipulation with demonstrated physical-robot robustness.\", \"UNADDRESSED COUNTER-EVIDENCE: arXiv 2601.21531 and 2601.12042 demonstrate token compression HURTS adversarial robustness. The idea must explicitly explain why trained IB pruning avoids this failure mode — the distinction (trained vs. post-hoc) is valid but never articulated.\", \"LIBERO-Plus evaluation cost underestimated: 10,030 tasks with a 7B model requires ~300+ GPU-hours per evaluation pass, further blowing the compute budget.\", \"Timeline risk: 20 days with ≤200 H100-hours leaves essentially no room for iteration. Even with SmolVLA, implementing IB scorer + tangent-space augmentation + running ablations across 7 perturbation dimensions in 20 days is extremely aggressive.\"]\nFeedback: Three critical fixes needed:\n\n1. **COMPUTE FIX (mandatory)**: Replace OpenVLA-OFT (7B) with SmolVLA (450M params, ~20 GPU-hours per LIBERO suite). SmolVLA achieves 87.3% on LIBERO — lower than OFT's 97.1% but fits the 200 H100-hour budget. Alternatively, use LoRA fine-tuning of a 3B model (OpenPi) at ~8-12h per run. Recalculate: with SmolVLA, you get ~80h for 4 LIBERO suites training + ~50h for ablations + ~70h for LIBERO-Plus evaluation = feasible within 200h.\n\n2. **NOVELTY POSITIONING (mandatory)**: Must explicitly differentiate from (a) BC-IB (ICML 2025) — which applies IB at the representation level, not token level, and doesn't target perturbation robustness; (b) IBTM — which is for efficiency not robustness, and is domain-general without action-conditioning; (c) RobustVLA — which uses regularization without token manipulation. The key differentiator should be: 'IB-guided token-level surgery that simultaneously prunes nuisance-correlated tokens AND augments retained tokens in latent space, specifically targeting distribution-shift robustness rather than efficiency or clean-condition accuracy.'\n\n3. **ADDRESS COUNTER-EVIDENCE (mandatory)**: Explicitly discuss why trained IB pruning differs from post-hoc compression that hurts robustness (per arXiv 2601.21531). The argument: post-hoc methods have unstable token rankings under perturbation, while IB-trained scorers learn perturbation-invariant relevance because the IB objective explicitly decorrelates from nuisance variables. This distinction should appear in the theoretical analysis.\n\nAdditional: Add RobustVLA and CRT as experimental baselines. Consider whether the 'tangent-space augmentation' component (extending FOMA) adds enough over the IB pruning alone to justify its complexity — if ablations show pruning-only captures 80%+ of the gain, the augmentation may be unnecessary weight for a tight timeline.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL BASELINE: 'VLA Models Are More Generalizable Than You Think' (arXiv 2512.02902) demonstrates Feature Token Modulation (FTM), which improves LIBERO viewpoint robustness from 48.5% to 87.1% using a simple affine transformation on visual tokens with only 4K parameters. This is a token-level robustness method that achieves strong results with drastically less complexity than ACIBS. It must be cited, discussed, and included as an experimental baseline.\", \"NUISANCE VARIABLE ACCESS UNDER-SPECIFIED: The IB regularizer minimizes I(V_selected; N | A) where N = {background texture, lighting, camera pose}. But LIBERO training data is clean/nominal — how does the method access nuisance variable samples during training? The claim that 'a variational upper bound makes training tractable WITHOUT requiring explicit nuisance factor labels' needs concrete specification. BC-IB uses a standard VIB formulation on I(X;Z) which doesn't require nuisance labels; but conditional MI I(V;N|A) inherently references N. Is N inferred? Augmented? This is a critical gap between the theoretical formulation and practical implementation.\", \"VARIATIONAL MI ESTIMATION RISK: Upper bounds on conditional MI are notoriously loose and sensitive to architecture/optimizer choices (Poole et al., ICML 2019). The claim of tractable optimization via variational bounds glosses over substantial practical challenges: neural MI estimators are biased, high-variance, and batch-size-dependent. For token-level conditional MI in a compact 450M-param model, this could easily fail to provide meaningful gradients.\", \"TIMELINE CONTRADICTION: The generator's manual estimate is '3-4 weeks' but CoRL abstract deadline is May 26 (12 days from today). The human-in-loop estimate of '10-14 days' barely fits. This timeline tension is not adequately addressed — the idea should either (a) explicitly scope to a CoRL-feasible subset (e.g., IB pruning only, no augmentation, 2-3 perturbation dimensions) or (b) target AAAI 2027 as primary venue.\", \"MISSING SURVEY CONTEXT: 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227, May 2025) is a position paper arguing exactly the thesis that token reduction should target robustness/quality not just efficiency. While not a methods paper, it provides important framing that ACIBS should cite and position against — claiming to be the first to instantiate this vision for VLAs.\", \"CoRL DEADLINE DATES SLIGHTLY WRONG: The idea states 'abstract: May 25, paper: May 28 AoE' but the official CoRL 2026 site lists abstract deadline as May 26 11:59 UTC and paper deadline as May 28-29 (sources vary). Minor but should be corrected.\", \"COST ESTIMATE INCONSISTENCY: Manual mode estimates '40-50% idle' GPU utilization but claims only 150-200h total. With SmolVLA at ~8-12h/run for training + 20-25h per model evaluation × 4-5 models = 80-125h eval alone + 32-60h training = 112-185h. This barely fits 200h with zero margin for failed runs, debugging, or hyperparameter exploration of the IB λ parameter — which the generator identifies as the critical tuning decision.\"]\nFeedback: The revision from Round 1 substantially improved compute feasibility and landscape coverage. Three focused fixes for Round 3:\n\n1. **ADD FTM BASELINE + CLARIFY ADVANTAGE (mandatory)**: Cite arXiv 2512.02902 and explain why ACIBS's IB-based approach is preferable to FTM's simple affine transformation, which achieves 87.1% viewpoint robustness with 4K params. The argument should be: FTM is a fixed transformation that doesn't adapt per-timestep or per-token, doesn't generalize across perturbation types (viewpoint-specific), and has no information-theoretic guarantee. ACIBS provides adaptive, per-timestep token selection with provable information retention. Include FTM as experimental baseline.\n\n2. **SPECIFY NUISANCE VARIABLE HANDLING (mandatory)**: Concretely describe how I(V_selected; N | A) is optimized without nuisance labels. Options: (a) use domain-randomized LIBERO variants as implicit nuisance samples during training (but this becomes data augmentation, undermining the 'no pixel-space augmentation' claim); (b) use a CLUB-style upper bound (Cheng et al., ICML 2020) that only requires paired clean observations; (c) use a variational decoder q(n|v) trained jointly to predict nuisance factors, following DRIBO's multi-view approach. Pick one and specify the training pipeline concretely.\n\n3. **RESOLVE TIMELINE (mandatory)**: Either (a) explicitly scope the CoRL submission to a minimal viable paper: IB pruning only (no tangent-space augmentation), SmolVLA backbone only, 3-4 key perturbation dimensions from LIBERO-Plus, with full ablation deferred to camera-ready; or (b) designate AAAI 2027 as the primary target with CoRL as a stretch goal. The current '3-4 week' manual estimate is incompatible with the 12-day CoRL deadline.\n\nMinor: cite arXiv 2505.18227 ('Token Reduction Should Go Beyond Efficiency') as supporting motivation, and correct CoRL deadline dates to official May 26/May 28-29.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"VENUE TARGET MISMATCH: User explicitly requires 'Target: CoRL 2026' but the idea designates AAAI 2027 as primary target with CoRL as 'stretch goal.' The idea must be primarily scoped for CoRL 2026 with the 12-day timeline and 200h compute as hard constraints, not soft guidelines.\", \"SMOLVLA FACTUAL ERRORS: The idea states 'SmolVLM-256M vision backbone + Qwen2.5-0.5B LLM' but SmolVLA actually uses SmolVLM2-500M (SigLIP encoder) and SmolLM2 (HuggingFace's own LLM with layer skipping), not Qwen2.5-0.5B. These errors undermine credibility.\", \"MISSING COMPETITOR — SimPrune (ICLR 2025): 'Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning' explicitly enforces cross-branch augmentation consistency during token pruning — the same core mechanism as ACIBS's consistency loss ||S(V)-S(V')||². SimPrune targets training efficiency rather than robustness, but the conceptual overlap is substantial and must be cited and differentiated.\", \"MISSING COMPETITOR — TCA (ICCV 2025, arXiv 2410.14729): 'Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation' demonstrates that token condensation improves distribution shift robustness by up to 21.4% on CIFAR-100-C and cross-dataset benchmarks. This directly supports the 'token reduction helps robustness' thesis and provides prior evidence that the approach direction works, but also reduces novelty of the core claim.\", \"COMPUTE STILL EXCEEDS HARD CONSTRAINT: Manual estimate of 200-250h exceeds the user's hard ≤200h budget. The idea acknowledges 'may slightly exceed' but the user specified this as a HARD CONSTRAINT. The mitigation (evaluate 4 dimensions first, defer full 7 to camera-ready) is reasonable but should be the primary plan, not a fallback.\", \"PROVABLE ROBUSTNESS MARGINS CLAIM IS VAGUE: The description repeatedly claims 'provable robustness margins' and 'information-theoretic compression guarantees' but never specifies what theorem is proved. A VIB KL term provides an upper bound on I(X;Z) but converting this to a robustness margin (e.g., Lipschitz bound on action error under perturbation) requires additional assumptions that are not stated.\", \"FTM BASELINE RISK UNDER-DISCUSSED: FTM achieves 87.1% viewpoint / 90.5% avg on LIBERO-V with 4K params and trivial training. If FTM adapted to SmolVLA recovers most of the robustness gap, ACIBS's added complexity (50K scorer, dual-view training, IB tuning of α/β/k) may yield marginal improvement insufficient for a top-venue contribution. The idea should explicitly discuss what happens if FTM-on-SmolVLA is a strong baseline.\", \"SEVERAL RECENT VLA PRUNING METHODS UNCITED: VLA-Pruner (arXiv 2511.16449), SP-VLA (ICLR 2026, arXiv 2506.12723), ETA-VLA (arXiv 2603.25766), EcoVLA (arXiv 2602.00780), and OneWM-VLA (arXiv 2605.07931) are recent VLA-specific token pruning methods. While efficiency-focused, they represent the broader competitive landscape and key ones should be cited in the landscape section.\"]\nFeedback: The Round 3 revision is substantially improved — the multi-view consistency reformulation elegantly solves the nuisance variable access problem from Round 2, the landscape coverage is now comprehensive (20+ papers), and the FTM/BC-IB/post-hoc differentiation is well-articulated. Four targeted fixes for Round 4:\n\n1. **SCOPE FOR CoRL PRIMARY (mandatory)**: Restructure the entire submission plan around CoRL 2026 as the primary target. The scoped version you already describe (IB pruning + consistency loss, no tangent-space augmentation, SmolVLA only, 4 key perturbation dimensions) should be the MAIN plan, not a stretch fallback. Compute should be re-estimated to fit strictly within 200h: ~4 training configs × 12h = 48h + 4 models × 5h eval = 20h + 30h debugging = 98h, leaving margin. AAAI 2027 can be mentioned as the extended version.\n\n2. **FIX SMOLVLA DETAILS + ADD SimPrune/TCA (mandatory)**: Correct the architecture to SmolVLM2-500M (SigLIP) + SmolLM2. Cite SimPrune (ICLR 2025) and differentiate: 'SimPrune enforces augmentation consistency for token pruning during self-supervised pretraining to maintain semantic alignment, targeting efficiency; ACIBS enforces consistency during VLA fine-tuning with an IB objective, targeting perturbation invariance for robustness.' Cite TCA (ICCV 2025) as supporting evidence that token reduction improves distribution shift robustness.\n\n3. **SHARPEN THEORETICAL CLAIMS (mandatory)**: Either (a) state a concrete theorem: 'Under Assumptions X (Lipschitz action decoder, bounded perturbation ε), the VIB-trained scorer with retention rate k achieves action prediction error bounded by [expression]' — even if the proof is standard VIB theory applied to this setting; or (b) downgrade the claim from 'provable robustness margins' to 'information-theoretic motivation with empirical robustness improvement,' which is honest and still publishable at CoRL.\n\n4. **EXPLICITLY PLAN FOR FTM BASELINE OUTCOME (recommended)**: Add a contingency analysis: 'If FTM adapted to SmolVLA achieves >X% on LIBERO-Plus, our contribution shifts to demonstrating that adaptive, per-token selection with IB grounding provides complementary gains — we can combine FTM's global modulation with ACIBS's selective pruning (FTM+ACIBS) and show the combination exceeds either alone.' This makes the paper robust to a strong FTM baseline result.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MISSING COMPETITOR — FocusVLA (arXiv 2603.28740, March 2026): FocusVLA dynamically selects task-relevant visual tokens via cross-attention-based top-K selection, achieving 98.7% on LIBERO with a 0.5B model. While it does NOT use IB objectives, augmentation consistency, or robustness evaluation, it IS a concurrent method targeting task-relevant visual token selection in VLAs and must be cited. Differentiation is clear: FocusVLA uses attention magnitude for accuracy-driven selection without robustness evaluation, while ACIBS uses IB-grounded scoring with multi-view consistency for perturbation invariance.\", \"COMPACT TOKEN SPACE RISK UNDER-ANALYZED: SmolVLA already aggressively compresses to 64 visual tokens per frame (via 3×3 pixel shuffle, 9× reduction). Further pruning to e.g. 32 tokens means each token carries enormous information density. The idea acknowledges α sensitivity but does not explicitly discuss what retention rates k are viable in this compact space or how this interacts with the IB objective. If the retention rate must be >80% (retaining >51 of 64 tokens) to preserve action accuracy, the actual 'pruning' may be minimal and the robustness benefit correspondingly small. The ablation plan should include a retention rate sweep (k ∈ {0.5, 0.6, 0.7, 0.8, 0.9}) with both nominal and perturbed accuracy reported.\", \"TIMELINE REMAINS EXTREMELY TIGHT: 15 days for implementation + training + evaluation + paper writing with zero margin for setbacks. The scoping (4 perturbation dimensions, no tangent-space augmentation) is appropriate, but even this scoped version requires: (a) implementing dual-view augmentation pipeline with LIBERO's randomization, (b) implementing Gumbel-softmax scorer integrated into SmolVLA's architecture, (c) adapting FTM to SmolVLA as baseline, (d) setting up LIBERO-Plus evaluation infrastructure, (e) running 4+ training configs and 5+ evaluation passes, (f) writing the paper. Any single component hitting an unexpected issue could derail the submission.\", \"MINOR: The auto_research GPU cost estimate ($450-$500) exceeds the manual estimate ($375-$450) despite using more GPU hours — this is internally consistent, but the auto mode at ~180-200h H100 is right at the hard constraint boundary with no margin for failed runs in autonomous mode.\"]\nFeedback: This is a substantially mature idea after 4 rounds of revision — the core novelty holds, the formulation is clean, and all major prior concerns have been addressed. Two targeted fixes to push toward passing:\n\n1. **ADD FocusVLA + ANALYZE RETENTION RATES (mandatory)**: Cite FocusVLA (arXiv 2603.28740) in the landscape as a concurrent attention-based token selection method (no IB, no robustness eval). More importantly, add explicit analysis of the retention rate k in SmolVLA's 64-token space: 'We plan a retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9} (32-58 tokens retained). The compact 64-token input means even k=0.8 prunes 13 tokens — enough to remove background-dominated tokens while preserving manipulation-critical spatial information. The IB objective's KL term adapts the effective retention per-sample, so the prior p_0 sets a soft target rather than a hard cutoff.' This addresses the concern that pruning on top of already-compressed tokens may yield minimal effect.\n\n2. **SHARPEN TIMELINE MITIGATION (recommended)**: Acknowledge that a single researcher executing the full pipeline in 15 days requires prior familiarity with SmolVLA/LeRobot and LIBERO infrastructure. Consider a progressive submission strategy: abstract by May 26 scoping the contribution, with the paper by May 29 potentially deferring FTM+ACIBS combination experiment to camera-ready if time runs short. This creates a minimal viable submission (ACIBS standalone + ablations) vs. ideal submission (+ FTM combination + more baselines).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-14T06:56:22.855Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T06:56:22.855Z",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

## Round 1

117 recorded events

### User

_source line 3 · 2026-05-14T06:56:22.887Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-14 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **按照以下方向，生成1-2个优质idea，保质不求量：Token-Level Representation Surgery for VLA Robustness
Target: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).
Direction: Token pruning and augmentation in VLA visual representations — methods that surgically manipulate visual tokens in latent space to improve VLA generalization under realistic perturbations. The core theoretical insight is that VLA visual encoders produce highly redundant token sequences where task-irrelevant tokens (background clutter, static scene regions, occluded areas) dominate attention budgets and create brittle feature correlations. By pruning uninformative tokens and augmenting critical ones in representation space (not pixel space), we compress the effective visual input to a task-relevant manifold that is inherently more robust to distribution shift. Theoretical grounding includes: (1) Information Bottleneck — pruning enforces a tighter bottleneck that retains only task-sufficient statistics, provably improving generalization bounds; (2) Attention Entropy Reduction — concentrating attention mass on fewer, more informative tokens reduces sensitivity to perturbations in pruned regions; (3) Manifold Regularization — augmenting retained tokens along the tangent space of the learned representation manifold provides robustness without leaving the data support. In-scope: adaptive token pruning based on action-relevance scoring, latent-space token augmentation via interpolation/extrapolation on task-critical tokens, attention-guided token selection with theoretical guarantees on information retention, combined prune-and-augment pipelines that maintain action prediction quality while improving robustness to visual distractors, lighting changes, viewpoint shifts, and occlusion.
Recent landscape (do not duplicate): Helix-style self-correction, CacheVLA,LightVLA,TraceVLA, RoboPro, retry/reflection wrappers around VLAs, FastVLA token merging (efficiency-only, no robustness analysis), TokenLearner fixed-count compression. Robustness as benchmark-only is saturated — must propose a method with theoretical motivation.
Contribution type: METHOD ONLY. New training algorithm combining action-conditioned token pruning with latent manifold augmentation: (1) a differentiable token relevance scorer trained with auxiliary action-prediction loss to identify which visual tokens carry task-critical information, (2) a prune-then-augment pipeline that removes low-relevance tokens and performs controlled perturbation of high-relevance tokens in latent space, (3) theoretical analysis showing the pruning step tightens the information bottleneck bound while augmentation smooths the action-prediction landscape, yielding provable robustness margins.
EVAL PROTOCOL — IMPORTANT:
TRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90).
EVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.
Report robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).
Additionally report token reduction ratio vs. robustness improvement curve, and ablate pruning-only vs. augmentation-only vs. combined.
Experiments can be extended to other benchmark series (e.g., CALVIN with perturbation variants) to verify cross-benchmark robustness.
SIM-ONLY MITIGATION: Robustness eval in sim is well-accepted at CoRL — established LIBERO-PLUS / LIBERO-PRO style suites are a recognized sim-only pattern.
HARD CONSTRAINTS:
Compute: ≤200 H100-hours total. Fine-tune from open VLA checkpoints (OpenVLA, SmolVLA, OpenPi, π0) — no pretraining. Token pruning/augmentation adds negligible overhead. Show the math.
Time: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers.
Eval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.
Look for: action-conditioned token relevance scoring that adapts per-timestep, latent-space augmentation that exploits the geometry of VLA's representation manifold, information-theoretic pruning criteria with provable bounds, attention entropy as a proxy for robustness, connections between token sparsity and flat minima in action space. Avoid: vanilla pixel-space data augmentation without latent-space method, static/fixed pruning ratios without adaptivity, pure efficiency-motivated token reduction rebranded as robustness, just-add-noise training.
Tag: direction=robust_vla, contribution_type=method, sub_direction=token_surgery, target_venues=["CoRL 2026"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-14?
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
  "title": "Action-Conditioned Information Bottleneck Token Surgery for Robust VLAs",
  "core_problem": "VLA visual encoders produce redundant token sequences where task-irrelevant tokens carry spurious correlations with environment-specific factors — correlations that collapse under visual perturbations. Existing token pruning methods (VLA-IAP, LightVLA, GridS, DTP, Compressor-VLA, SP-VLA, VLA-Pruner, ETA-VLA, EcoVLA, FocusVLA) optimize exclusively for inference efficiency or clean-condition accuracy, while existing robustness methods operate at other levels: policy-level regularization (RobustVLA), input restoration (CRT), or lightweight affine token modulation (FTM, which uses input-independent global parameters). Critically, post-hoc token compression has been shown to actively HURT adversarial robustness by concentrating adversarial signal on high-importance retained tokens (arXiv 2601.21531, 2601.12042). The position paper 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues exactly this thesis but provides no concrete VLA instantiation. TCA (ICCV 2025) provides preliminary evidence that token condensation can improve distribution shift robustness in classification (+21.4% on CIFAR-100-C), but operates training-free at test time without action conditioning. SimPrune (ICLR 2025) enforces cross-branch augmentation consistency during token pruning in self-supervised pretraining, but targets training efficiency rather than deployment robustness. FocusVLA (arXiv 2603.28740) dynamically selects task-relevant visual tokens via cross-attention-based top-K selection, achieving 98.7% on LIBERO — but targets clean-condition accuracy using attention magnitude scores without IB objectives, augmentation consistency, or robustness evaluation under visual perturbations. We show that token-level intervention CAN improve VLA robustness — when the token scorer is jointly trained with an information bottleneck objective using multi-view augmentation consistency that implicitly decorrelates from nuisance variables, producing perturbation-invariant relevance scores fundamentally different from both attention-based importance used in post-hoc methods and FocusVLA, input-independent affine modulation used in FTM, and cross-branch similarity matching used in SimPrune.",
  "opportunity": "LIBERO-Plus (CVPR 2026) reveals catastrophic robustness gaps (95% → <30% under camera/state perturbations), with current SOTA at SRPO 82.1% avg. FTM (arXiv 2512.02902) shows that even a simple global affine transformation on visual tokens recovers viewpoint robustness (48.5% → 87.1% on π0.5 with 4K params), demonstrating that token-level intervention is a promising robustness lever — but FTM's input-independent, fixed-parameter design cannot adapt to scene content, varies in effectiveness across perturbation types, and lacks information-theoretic grounding. BC-IB (ICML 2025) demonstrates that IB at the representation level improves clean accuracy on LIBERO but explicitly acknowledges robustness to domain shifts as an open problem. TCA (ICCV 2025) demonstrates that token condensation improves distribution shift robustness in ViT classification by up to 21.4%, providing direct supporting evidence that the token-reduction-for-robustness direction is viable — but TCA is training-free, task-agnostic, and untested on embodied action prediction. SimPrune (ICLR 2025) shows cross-branch consistency can guide token pruning in SSL, but targets pretraining efficiency without an IB objective or robustness evaluation. FocusVLA (arXiv 2603.28740) demonstrates that cross-attention-based top-K token selection achieves excellent clean accuracy (98.7% on LIBERO with 256 of 512 tokens retained) — but operates on architectures with large token budgets (512 tokens) without IB grounding or perturbation robustness evaluation, leaving the question of whether attention-based selection degrades gracefully under visual perturbations entirely open. The unexploited gap is: applying IB at the TOKEN level with ADAPTIVE, INPUT-DEPENDENT selection, conditioned on ACTION prediction, using MULTI-VIEW augmentation consistency to achieve perturbation invariance — a combination that provides principled, per-timestep token selection with information-theoretic motivation, going beyond FTM's fixed modulation, BC-IB's coarse-grained bottleneck, TCA's training-free approach, SimPrune's efficiency-focused consistency, and FocusVLA's accuracy-driven attention selection.",
  "landscape": "The VLA token intervention literature spans efficiency, accuracy-driven selection, modulation, and robustness approaches. EFFICIENCY-FOCUSED PRUNING: VLA-IAP (Mar 2026) achieves 97.8% on LIBERO with 1.54x speedup via training-free interaction-aligned pruning; LightVLA (ICRA 2026) uses differentiable Gumbel softmax selection reducing FLOPs by 59.1%; GridS (ICML 2026) performs differentiable grid resampling; Compressor-VLA uses instruction-guided dual compression; DTP prunes distracting tokens for accuracy not perturbation robustness; SP-VLA (ICLR 2026, arXiv 2506.12723) jointly schedules models and prunes tokens via spatio-semantic dual-aware importance; VLA-Pruner (arXiv 2511.16449) uses dual-level importance combining prefill attention and temporal-smoothed action decode attention; ETA-VLA (arXiv 2603.25766) performs temporal fusion with intra-LLM sparsification; EcoVLA (arXiv 2602.00780) applies environment-aware adaptive pruning as a training-free plug-and-play framework; OneWM-VLA (arXiv 2605.07931) compresses each view to one token via adaptive attention pooling. ACCURACY-DRIVEN TOKEN SELECTION: FocusVLA (arXiv 2603.28740, March 2026) dynamically selects task-relevant visual tokens via cross-attention-based top-K selection between action queries and vision keys, achieving 98.7% on LIBERO (multi-weight) with a 0.5B model (Qwen2.5-0.5B + DINOv2/SigLIP, 342.7M trainable params). FocusVLA retains 256 of 512 raw tokens (50% retention), demonstrating that attention-guided selection improves clean accuracy — but it does NOT use IB objectives, augmentation consistency, or robustness evaluation under visual perturbations. Its cross-attention scores reflect task relevance under nominal conditions but may not remain stable under domain shift, since attention-based importance is itself perturbed under visual corruption (the same vulnerability documented for post-hoc pruning in arXiv 2601.21531). ACIBS differs from FocusVLA in three fundamental ways: (1) IB-grounded scoring vs. attention-magnitude selection, (2) multi-view consistency training for perturbation invariance vs. clean-condition-only training, (3) robustness as the primary objective vs. accuracy. TOKEN-LEVEL MODULATION: FTM (arXiv 2512.02902) applies an input-independent global affine transformation F̂=(1+γ)⊙F+β to visual tokens from π0.5's ViT encoder, achieving camera 87.1%, lighting 96.0%, texture 96.0%, noise 93.6% on LIBERO-V with only 4K params — remarkably effective but limited by: (a) input-independence (same γ,β regardless of scene content), (b) tested only on π0.5 (3B+ params), not compact models like SmolVLA, (c) no token selection/pruning (all tokens retained), (d) no information-theoretic grounding. FLA extends FTM with low-rank ViT updates (4.7M params, 90.8%) but requires encoder modification. AUGMENTATION-CONSISTENT TOKEN METHODS: SimPrune (ICLR 2025) enforces cross-branch cosine similarity matching for token-pair pruning during self-supervised pretraining — conceptually related to ACIBS's consistency loss but differs in three key ways: (1) SimPrune targets training efficiency in SSL dual-branch architectures, not deployment robustness in VLAs; (2) SimPrune uses pairwise cosine similarity for token matching, not an IB-grounded scoring head; (3) SimPrune prunes matched token pairs to reduce compute, not to select perturbation-invariant tokens for action prediction. TCA (ICCV 2025, arXiv 2410.14729) demonstrates that training-free token condensation improves distribution shift robustness by up to 21.4% on CIFAR-100-C via reservoir-based domain anchor tokens — directly supporting the token-reduction-for-robustness thesis but operating training-free, at test time, without action conditioning or IB objectives. IB FOR ROBOTICS: BC-IB (ICML 2025, arXiv 2502.02853) applies IB at the REPRESENTATION level in behavior cloning, minimizing I(X;Z) on the full latent vector — improves clean accuracy by +5.6% on LIBERO but does not operate at token granularity and explicitly notes domain-shift robustness as unstudied. IBTM (OpenReview) combines IB with learnable token merging for ViT efficiency but targets FLOPs reduction on classification without action conditioning or robustness evaluation. MULTI-VIEW IB: DRIBO (ICML 2022) uses augmentation-generated paired views with a contrastive MIB objective to learn robust RL representations — directly inspiring our nuisance-invariant token selection approach but operating at representation level, not token selection level. MIB (Federici et al., ICLR 2020) provides the theoretical foundation for multi-view IB without nuisance labels. VLA ROBUSTNESS: RobustVLA (arXiv 2511.01331) applies Jacobian + smoothness regularization during online RL post-training (~82.5% on observation perturbations). CRT (arXiv 2602.01158) uses a corruption restoration transformer as preprocessing. SRPO achieves 82.1 on LIBERO-Plus via self-referential RL policy optimization (current LIBERO-Plus SOTA). AVA-VLA (arXiv 2511.18960) introduces active visual attention that dynamically reweights visual tokens based on instruction and execution history, achieving 74.7% avg on LIBERO-Plus — relevant as it also performs dynamic token reweighting, but uses POMDP-motivated attention reweighting for clean generalization rather than IB-grounded selection for perturbation invariance. COUNTER-EVIDENCE: arXiv 2601.21531 and 2601.12042 demonstrate that POST-HOC token compression hurts adversarial robustness via the 'distortion concentrator' effect — but these exclusively evaluate training-free compression with attention-based importance scores that are themselves perturbed. Fischer et al. (2021, arXiv 2107.05712) show that VIB's apparent adversarial robustness in classification is partly attributable to gradient obfuscation rather than provable guarantees — motivating our empirical rather than certified robustness framing. POSITION PAPER: 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues the thesis that token reduction should target robustness/quality, not just efficiency — ACIBS is the first concrete VLA instantiation of this vision.",
  "approach": "We train a lightweight differentiable token scoring head atop SmolVLA's visual encoder (SmolVLM-2: SigLIP vision encoder + SmolLM2 language decoder, 450M total params with ~100M action expert, 64 visual tokens per frame) that is jointly optimized with action prediction and a multi-view augmentation-consistent Information Bottleneck (IB) objective. COMPACT TOKEN SPACE ANALYSIS: SmolVLA's 64 visual tokens per frame — produced via 3×3 pixel shuffle (9× spatial reduction) — represent an already-aggressive compression. We explicitly study how further IB-guided pruning interacts with this compact space via a retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9}, corresponding to 32, 38, 45, 51, and 58 tokens retained. Key observations: (a) Even k=0.8 prunes 13 tokens — sufficient to remove background-dominated tokens while preserving manipulation-critical spatial information, since SmolVLA's pixel-shuffle tokens are spatially localized and many correspond to static background regions. (b) The IB objective's KL term provides per-sample ADAPTIVE retention: the prior p_0(m) sets a SOFT target retention rate, not a hard cutoff. In practice, this means the effective retention varies per-timestep — scenes with cluttered backgrounds may retain fewer tokens (e.g., k_eff ≈ 0.6), while visually sparse manipulation scenes retain more (k_eff ≈ 0.9). This adaptive behavior is a key advantage over fixed-rate pruning methods. (c) Unlike FocusVLA which prunes from 512 to 256 tokens (50% retention with substantial redundancy), pruning from 64 tokens operates in a regime where each token carries high information density. This motivates our IB formulation: the VIB term ensures that pruning decisions maximize retained action-relevant information per token, while the consistency term ensures these decisions are perturbation-invariant. We report both nominal and perturbed accuracy at each k to characterize the robustness-efficiency Pareto frontier in this compact token space. The key methodological advance is the REFORMULATED IB OBJECTIVE that eliminates the need for explicit nuisance variable labels or conditional MI estimation. Instead of minimizing I(V_selected; N | A) — which requires access to nuisance factor samples N — we adopt a multi-view consistency approach inspired by DRIBO (ICML 2022) and MIB (Federici et al., ICLR 2020): during training, each observation X is paired with an augmented view X' generated via domain randomization (camera jitter ±15°, color/lighting perturbation, background texture swap using LIBERO's built-in randomization). Both views pass through SmolVLA's frozen SigLIP encoder to produce token sequences V and V'. The combined training loss is: L = L_action(f(V_m), A) + α·D_KL(q(m|V) || p_0(m)) + β·||S(V) - S(V')||². The first term maximizes action-prediction accuracy from selected tokens. The second term is a VIB-style token-level bottleneck: q(m|V) is the per-token Bernoulli selection distribution parameterized by the scorer MLP via Gumbel-softmax relaxation (architecturally following LightVLA's differentiable selection), and p_0(m) is a Bernoulli prior with target retention rate k — this forces compression of redundant information. The third term is the CROSS-VIEW SELECTION CONSISTENCY loss: it penalizes differences in the scorer's output logits S(·) across augmented views, forcing the scorer to be INVARIANT to augmentation-defined nuisance factors. This formulation uses only standard KL divergence and MSE — no neural MI estimation required, sidestepping the bias/variance issues of variational MI bounds (Poole et al., ICML 2019). The augmentation pipeline implicitly defines nuisance variables: any information that varies across views (background, lighting, viewpoint) is nuisance, and the consistency loss forces the scorer to ignore it. We note the conceptual connection to SimPrune (ICLR 2025), which also uses cross-branch consistency for token pruning — but SimPrune operates in SSL pretraining using cosine similarity for efficiency-driven token-pair matching, while ACIBS operates in VLA fine-tuning using an IB-grounded scorer for robustness-driven token selection, representing a fundamentally different objective and mechanism. The scorer is implemented as a 2-layer MLP (~50K params) predicting per-token logits, with Gumbel-softmax producing differentiable soft masks during training and hard top-k selection during inference. DIFFERENTIATION FROM FocusVLA: FocusVLA uses cross-attention scores between action queries and vision keys for top-K selection in a 512-token space, optimizing clean-condition accuracy without IB or consistency objectives. ACIBS differs in: (1) IB-grounded scoring that compresses information-theoretically vs. attention-magnitude selection, (2) multi-view consistency for perturbation-invariant scores vs. nominal-only training, (3) operation in SmolVLA's compact 64-token space where each pruning decision carries higher impact, (4) robustness as primary objective vs. accuracy. FocusVLA's attention-based scores are themselves susceptible to perturbation-induced drift (the same failure mode documented for post-hoc pruning), while ACIBS's consistency-trained scorer is explicitly trained to be invariant to such perturbations. THEORETICAL FRAMING: We frame ACIBS with information-theoretic motivation rather than provable robustness certificates. The VIB term upper-bounds the mutual information I(X;M) between input tokens and selected mask, encouraging compression; the consistency term empirically enforces invariance to augmentation-defined nuisance factors. We do NOT claim certified robustness margins — Fischer et al. (2021) demonstrated that VIB's apparent adversarial robustness in classification is partly attributable to gradient obfuscation, and certified bounds would require additional assumptions (Lipschitz continuity, bounded perturbation sets) beyond what VIB alone provides. Instead, our contribution is an empirically grounded method that achieves perturbation invariance through the joint training of IB compression and augmentation consistency, validated on LIBERO-Plus. FTM BASELINE CONTINGENCY: If FTM adapted to SmolVLA recovers most of the robustness gap (e.g., >75% avg on LIBERO-Plus), our contribution shifts to demonstrating that adaptive, input-dependent, per-token selection with IB grounding provides COMPLEMENTARY gains — we evaluate FTM+ACIBS (global affine modulation followed by IB-guided selective pruning) and show the combination exceeds either alone by leveraging both feature recalibration and information-theoretic token filtering. This compositional result would be novel regardless of FTM's standalone strength. PROGRESSIVE SUBMISSION STRATEGY: Given the 15-day timeline (abstract May 26, paper May 29), we define a minimal viable submission (MVS) and ideal submission. MVS (non-negotiable): ACIBS standalone with retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9}, ablations isolating VIB and consistency terms, 4 perturbation dimensions (camera, lighting, texture, noise), comparison against SmolVLA baseline and FTM-SmolVLA. Ideal submission (if time permits): adds FTM+ACIBS combination experiment, additional baselines (VLA-IAP, BC-IB), and per-dimension analysis. The FTM+ACIBS combination experiment is deferred to camera-ready if time runs short. This strategy requires prior familiarity with SmolVLA/LeRobot codebase and LIBERO evaluation infrastructure — the timeline is feasible for a researcher who has already worked with these tools but would not be achievable starting from scratch. Key differentiation from prior work: (a) vs. FTM — adaptive, input-dependent, per-token selection with IB motivation vs. input-independent global affine modulation; FTM retains all tokens with shifted features, ACIBS selects informative tokens and discards nuisance-carrying ones; composable as FTM+ACIBS; (b) vs. BC-IB — token-level vs. representation-level IB, robustness-targeted via multi-view consistency vs. accuracy-targeted; (c) vs. DRIBO — token selection level vs. representation level, action-conditioned for manipulation; (d) vs. post-hoc pruning — trained perturbation-invariant scorer vs. unstable attention-based importance; (e) vs. SimPrune — IB-grounded action-conditioned robustness scorer vs. cosine-similarity efficiency matcher in SSL; (f) vs. TCA — trained, action-conditioned IB selection vs. training-free, task-agnostic condensation; (g) vs. IBTM — action-conditioned and robustness-evaluated vs. task-agnostic efficiency; (h) vs. FocusVLA — IB-grounded perturbation-invariant scoring in compact 64-token space vs. attention-based accuracy-driven selection in 512-token space without robustness evaluation or information-theoretic grounding. We evaluate on LIBERO-Plus across 4 key perturbation dimensions (camera, lighting, texture, noise) for the primary CoRL submission, with full 7-dimension evaluation deferred to extended version. Baselines include efficiency-focused pruning (VLA-IAP, DTP), accuracy-driven selection (FocusVLA), token modulation (FTM adapted to SmolVLA backbone), robustness methods (RobustVLA, CRT, SRPO), and the representation-level IB approach (BC-IB), plus ablations isolating the VIB term and consistency term, retention rate sweep, and the FTM+ACIBS combination (time permitting, else camera-ready).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~155-185h H100 (SmolVLA base: ~4h/run; with IB scorer + dual-view forward pass: ~12h/run; 5 retention rate configs × 12h = 60h training; LIBERO-Plus eval on 4 perturbation dims ~5h per model × 5 models (ACIBS-best-k, FTM-SmolVLA, 2 ablations, baseline) = 25h; retention rate sweep eval ~15h; baseline reproductions ~25h; debugging/iteration ~30-40h; total ~155-165h within 200h budget with ~35h margin)",
      "gpu_utilization": "Moderate idle (35-45%) — researcher iterates on α/β trade-off and analyzes per-dimension robustness curves between runs",
      "timeline": "12-15 days (abstract by May 26, paper by May 29 CoRL 2026). Requires prior familiarity with SmolVLA/LeRobot and LIBERO infrastructure. Progressive submission: MVS (ACIBS + ablations + retention sweep) guaranteed; FTM+ACIBS combination deferred to camera-ready if needed",
      "team": "1-2 researchers with existing SmolVLA/LIBERO experience",
      "estimated_gpu_cost": "$390-$465 (at ~$2.50/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~145-175h H100 (agent systematically sweeps α/β/k retention rate; human approves VIB/consistency/action-loss trade-off at each checkpoint; dual-view augmentation adds ~40% overhead per training run vs. standard SmolVLA fine-tuning; retention rate sweep adds ~20h)",
      "gpu_utilization": "20-30% lower idle vs manual — agent queues next run while human reviews robustness vs. clean accuracy trade-offs",
      "timeline": "10-12 days",
      "team": "1 researcher with SmolVLA/LIBERO experience, ~1.5hr/day reviewing trade-off curves and selecting augmentation strategies",
      "claude_api_cost": "$80-150 (estimated ~800-1500 turns for experiment design, augmentation pipeline setup, result analysis)",
      "estimated_gpu_cost": "$365-$440",
      "risk_note": "α/β/k tuning is the critical human decision loop — α too high destroys action-relevant signal in SmolVLA's compact 64-token space, β too high forces trivially constant selection that ignores scene content, k too low (e.g., 0.5) may lose spatial coverage needed for precise manipulation. The dual-view augmentation pipeline must be carefully calibrated: augmentations too weak fail to define meaningful nuisance, too strong create views where task-relevant information also differs"
    },
    "auto_research": {
      "gpu_hours": "~175-195h H100 (more exploration of α/β/k hyperparameter space including full retention rate sweep; includes failed runs; fits within 200h budget with scoped 4-dimension eval and MVS scope)",
      "gpu_utilization": "Near-zero idle — agent continuously pipelines training → evaluation → next experiment",
      "timeline": "8-12 days with 2 H100 GPUs",
      "team": "0 (initial setup only, assumes pre-configured SmolVLA/LIBERO environment)",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$440-$490",
      "speed_bottleneck": "LIBERO-Plus evaluation throughput — ~5h per 4-dimension evaluation pass per model on single GPU; retention rate sweep multiplies eval cost by 5×",
      "risk_note": "Agent may over-explore hyperparameter space without convergence intuition; multi-view augmentation magnitude is sensitive and agent may not distinguish meaningful augmentation failures from hyperparameter failures. The 200h budget is tight with 5-point retention sweep — agent should use early stopping on clearly failing k values"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract: May 26 11:59 UTC, paper: May 29 11:59 UTC — PRIMARY TARGET, progressive submission: MVS = ACIBS + retention rate sweep + ablations on 4 perturbation dims; ideal = + FTM+ACIBS combination + extended baselines; 15-day timeline from today May 14, requires prior SmolVLA/LIBERO familiarity)",
    "AAAI 2027 (deadlines TBD, likely ~August 2026 — extended version with full 7-dimension LIBERO-Plus evaluation, FTM+ACIBS combination if deferred, tangent-space augmentation ablation, multi-backbone experiments on π0.5)",
    "ICLR 2027 (deadline ~October 2026 — most comprehensive version with compositional perturbations and theoretical analysis)"
  ],
  "level": "top-tier",
  "key_references": [
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)",
    "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv 2025, 2506.01844)",
    "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation [BC-IB] (ICML 2025, arXiv 2502.02853)",
    "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2025, 2512.02902)",
    "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2026, 2603.28740)",
    "Token Reduction Should Go Beyond Efficiency in Generative Models — From Vision, Language to Multimodality (arXiv 2025, 2505.18227)",
    "Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning [SimPrune] (ICLR 2025)",
    "Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation [TCA] (ICCV 2025, arXiv 2410.14729)",
    "DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck (ICML 2022)",
    "Learning Robust Representations via Multi-View Information Bottleneck [MIB] (ICLR 2020, arXiv 2002.07017)",
    "A Closer Look at the Adversarial Robustness of Information Bottleneck Models (Fischer et al., 2021, arXiv 2107.05712)",
    "CLUB: A Contrastive Log-ratio Upper Bound of Mutual Information (ICML 2020)",
    "On Variational Bounds of Mutual Information (Poole et al., ICML 2019)",
    "Efficient Visual Transformer by Information Bottleneck Inspired Token Merging [IBTM] (OpenReview 2024)",
    "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models (arXiv 2025, 2511.01331)",
    "Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs [CRT] (arXiv 2026, 2602.01158)",
    "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2025, 2511.15605)",
    "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (arXiv 2025, 2511.18960)",
    "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression (arXiv 2026, 2601.21531)",
    "Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models (arXiv 2026, 2601.12042)",
    "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models (arXiv 2026, 2603.22991)",
    "The Better You Learn, The Smarter You Prune: Towards Efficient VLAs via Differentiable Token Pruning [LightVLA] (ICRA 2026)",
    "See What Matters: Differentiable Grid Sample Pruning for Generalizable VLA [GridS] (ICML 2026)",
    "DTP: A Simple yet Effective Distracting Token Pruning Framework for VLA Models (arXiv 2026, 2601.16065)",
    "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2025, 2511.18950)",
    "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (ICLR 2026, arXiv 2506.12723)",
    "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2025, 2511.16449)",
    "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification (arXiv 2026, 2603.25766)",
    "EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration (arXiv 2026, 2602.00780)",
    "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy [OneWM-VLA] (arXiv 2026, 2605.07931)",
    "Deep Variational Information Bottleneck (Alemi et al., ICLR 2017, arXiv 1612.00410)",
    "Token Bottleneck: One Token to Remember Dynamics [ToBo] (NeurIPS 2025, arXiv 2507.06543)",
    "First-Order Manifold Data Augmentation for Regression Learning [FOMA] (ICML 2024)"
  ],
  "description": "We propose Action-Conditioned Information Bottleneck Token Surgery (ACIBS), a method that reconceptualizes VLA visual token selection from an efficiency optimization into a robustness mechanism. Current VLA models achieve >95% success on standard benchmarks but collapse to <30% under visual perturbations (LIBERO-Plus, CVPR 2026), with the current SOTA (SRPO) at 82.1% average. Existing token pruning methods (VLA-IAP, LightVLA, GridS, DTP, SP-VLA, VLA-Pruner, ETA-VLA, EcoVLA) target inference speed; accuracy-driven selection methods like FocusVLA (arXiv 2603.28740) achieve excellent clean accuracy (98.7% via cross-attention top-K) but lack IB grounding and robustness evaluation; post-hoc compression actively hurts adversarial robustness via the 'distortion concentrator' effect (arXiv 2601.21531, 2601.12042); and FTM (arXiv 2512.02902) achieves strong viewpoint robustness (87.1% on π0.5) via a simple input-independent global affine transformation on visual tokens — but its fixed parameters cannot adapt to scene content. Meanwhile, BC-IB (ICML 2025) applies IB at the representation level for clean accuracy without addressing token-level robustness; TCA (ICCV 2025) demonstrates that token condensation improves distribution shift robustness by up to 21.4% in classification but is training-free and task-agnostic; SimPrune (ICLR 2025) enforces cross-branch augmentation consistency for token pruning in SSL pretraining but targets efficiency; and 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues this thesis without a concrete VLA method. ACIBS bridges these gaps with a fundamentally different formulation: a differentiable token scorer jointly trained with action prediction and a MULTI-VIEW AUGMENTATION-CONSISTENT IB objective. Built on SmolVLA (SmolVLM-2: SigLIP vision encoder + SmolLM2 language decoder, 450M params, 64 visual tokens per frame), the combined loss is L = L_action + α·D_KL(q(m|V) || p_0(m)) + β·||S(V) - S(V')||², where the VIB term compresses token information and the consistency term forces the scorer to be INVARIANT to augmentation-defined nuisance factors. A critical design consideration is that SmolVLA's 64 tokens (via 3×3 pixel shuffle, 9× reduction) already represent aggressive compression. We address this via a retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9} (32-58 tokens retained), with the IB objective's KL term providing per-sample ADAPTIVE retention — the prior p_0 sets a soft target, allowing the effective retention to vary per-timestep based on scene content. Even k=0.8 prunes 13 tokens, sufficient to remove background-dominated spatial regions while preserving manipulation-critical information. Unlike FocusVLA which prunes from 512 to 256 tokens with substantial redundancy, ACIBS operates in a compact regime where each pruning decision carries high impact, making IB-guided selection especially valuable. We frame this with information-theoretic motivation rather than certified robustness guarantees — Fischer et al. (2021) showed VIB's apparent adversarial robustness is partly gradient obfuscation, so we target empirical perturbation invariance through joint IB compression and augmentation consistency, not provable bounds. The approach extends DRIBO's multi-view IB principle from representation-level RL to token-level VLA selection. We explicitly plan for a strong FTM baseline: if FTM adapted to SmolVLA achieves >75% avg on LIBERO-Plus, we demonstrate FTM+ACIBS (global modulation + IB-guided selection) exceeds either alone, showing the approaches are complementary. Primary target is CoRL 2026 (abstract May 26, paper May 29) with a progressive submission strategy: minimal viable submission (ACIBS + retention rate sweep + ablations, 4 perturbation dimensions) guaranteed by deadline; FTM+ACIBS combination deferred to camera-ready if needed. Timeline requires prior SmolVLA/LeRobot and LIBERO familiarity. Strict 200h H100 compute budget (~155h estimated). Baselines include FTM (adapted to SmolVLA), accuracy-driven selection (FocusVLA), efficiency-focused pruning (VLA-IAP, DTP), robustness methods (RobustVLA, CRT, SRPO), and the representation-level IB approach (BC-IB), plus ablations isolating the VIB term and consistency term, retention rate sweep, and the FTM+ACIBS combination.",
  "project_name": "ib_token_surgery_vla",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["FATAL COMPUTE MISMATCH: The idea proposes OpenVLA-OFT (7B params, 8×A100 for 24-48h per run = 192-384 GPU-hours per run) but user's hard constraint is ≤200 H100-hours total. A single training run exhausts the entire budget with zero room for ablations, hyperparameter tuning, or evaluation. The idea's own resource estimate (2000-3000h) confirms this is 10-15x over budget.", "MISSED CRITICAL PRIOR WORK: BC-IB (ICML 2025, arXiv 2502.02853) already applies Information Bottleneck to behavior cloning for robot manipulation on LIBERO, reducing MI to 1/4 and improving LIBERO-Goal by +7.7%. The claim of being 'first to use IB for VLA robustness' is significantly weakened.", "MISSED CRITICAL PRIOR WORK: IBTM (under review, OpenReview) directly combines IB principle with learnable token merging in vision transformers — exactly the IB + token selection combination claimed as novel.", "MISSED COMPETITOR: RobustVLA (arXiv 2511.01331, ICLR 2026 submission) achieves +12.6% robustness on pi0 and +10.4% on OpenVLA across 17 perturbations via Jacobian + smoothness regularization — a direct robustness method for VLAs that must be compared against.", "MISSED COMPETITOR: Token Bottleneck / ToBo (NeurIPS 2025, arXiv 2507.06543) uses a bottleneck token concept for robot manipulation with demonstrated physical-robot robustness.", "UNADDRESSED COUNTER-EVIDENCE: arXiv 2601.21531 and 2601.12042 demonstrate token compression HURTS adversarial robustness. The idea must explicitly explain why trained IB pruning avoids this failure mode — the distinction (trained vs. post-hoc) is valid but never articulated.", "LIBERO-Plus evaluation cost underestimated: 10,030 tasks with a 7B model requires ~300+ GPU-hours per evaluation pass, further blowing the compute budget.", "Timeline risk: 20 days with ≤200 H100-hours leaves essentially no room for iteration. Even with SmolVLA, implementing IB scorer + tangent-space augmentation + running ablations across 7 perturbation dimensions in 20 days is extremely aggressive."]
Feedback: Three critical fixes needed:

1. **COMPUTE FIX (mandatory)**: Replace OpenVLA-OFT (7B) with SmolVLA (450M params, ~20 GPU-hours per LIBERO suite). SmolVLA achieves 87.3% on LIBERO — lower than OFT's 97.1% but fits the 200 H100-hour budget. Alternatively, use LoRA fine-tuning of a 3B model (OpenPi) at ~8-12h per run. Recalculate: with SmolVLA, you get ~80h for 4 LIBERO suites training + ~50h for ablations + ~70h for LIBERO-Plus evaluation = feasible within 200h.

2. **NOVELTY POSITIONING (mandatory)**: Must explicitly differentiate from (a) BC-IB (ICML 2025) — which applies IB at the representation level, not token level, and doesn't target perturbation robustness; (b) IBTM — which is for efficiency not robustness, and is domain-general without action-conditioning; (c) RobustVLA — which uses regularization without token manipulation. The key differentiator should be: 'IB-guided token-level surgery that simultaneously prunes nuisance-correlated tokens AND augments retained tokens in latent space, specifically targeting distribution-shift robustness rather than efficiency or clean-condition accuracy.'

3. **ADDRESS COUNTER-EVIDENCE (mandatory)**: Explicitly discuss why trained IB pruning differs from post-hoc compression that hurts robustness (per arXiv 2601.21531). The argument: post-hoc methods have unstable token rankings under perturbation, while IB-trained scorers learn perturbation-invariant relevance because the IB objective explicitly decorrelates from nuisance variables. This distinction should appear in the theoretical analysis.

Additional: Add RobustVLA and CRT as experimental baselines. Consider whether the 'tangent-space augmentation' component (extending FOMA) adds enough over the IB pruning alone to justify its complexity — if ablations show pruning-only captures 80%+ of the gain, the augmentation may be unnecessary weight for a tight timeline.

### Round 2 review
Verdict: revise
Issues: ["MISSING CRITICAL BASELINE: 'VLA Models Are More Generalizable Than You Think' (arXiv 2512.02902) demonstrates Feature Token Modulation (FTM), which improves LIBERO viewpoint robustness from 48.5% to 87.1% using a simple affine transformation on visual tokens with only 4K parameters. This is a token-level robustness method that achieves strong results with drastically less complexity than ACIBS. It must be cited, discussed, and included as an experimental baseline.", "NUISANCE VARIABLE ACCESS UNDER-SPECIFIED: The IB regularizer minimizes I(V_selected; N | A) where N = {background texture, lighting, camera pose}. But LIBERO training data is clean/nominal — how does the method access nuisance variable samples during training? The claim that 'a variational upper bound makes training tractable WITHOUT requiring explicit nuisance factor labels' needs concrete specification. BC-IB uses a standard VIB formulation on I(X;Z) which doesn't require nuisance labels; but conditional MI I(V;N|A) inherently references N. Is N inferred? Augmented? This is a critical gap between the theoretical formulation and practical implementation.", "VARIATIONAL MI ESTIMATION RISK: Upper bounds on conditional MI are notoriously loose and sensitive to architecture/optimizer choices (Poole et al., ICML 2019). The claim of tractable optimization via variational bounds glosses over substantial practical challenges: neural MI estimators are biased, high-variance, and batch-size-dependent. For token-level conditional MI in a compact 450M-param model, this could easily fail to provide meaningful gradients.", "TIMELINE CONTRADICTION: The generator's manual estimate is '3-4 weeks' but CoRL abstract deadline is May 26 (12 days from today). The human-in-loop estimate of '10-14 days' barely fits. This timeline tension is not adequately addressed — the idea should either (a) explicitly scope to a CoRL-feasible subset (e.g., IB pruning only, no augmentation, 2-3 perturbation dimensions) or (b) target AAAI 2027 as primary venue.", "MISSING SURVEY CONTEXT: 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227, May 2025) is a position paper arguing exactly the thesis that token reduction should target robustness/quality not just efficiency. While not a methods paper, it provides important framing that ACIBS should cite and position against — claiming to be the first to instantiate this vision for VLAs.", "CoRL DEADLINE DATES SLIGHTLY WRONG: The idea states 'abstract: May 25, paper: May 28 AoE' but the official CoRL 2026 site lists abstract deadline as May 26 11:59 UTC and paper deadline as May 28-29 (sources vary). Minor but should be corrected.", "COST ESTIMATE INCONSISTENCY: Manual mode estimates '40-50% idle' GPU utilization but claims only 150-200h total. With SmolVLA at ~8-12h/run for training + 20-25h per model evaluation × 4-5 models = 80-125h eval alone + 32-60h training = 112-185h. This barely fits 200h with zero margin for failed runs, debugging, or hyperparameter exploration of the IB λ parameter — which the generator identifies as the critical tuning decision."]
Feedback: The revision from Round 1 substantially improved compute feasibility and landscape coverage. Three focused fixes for Round 3:

1. **ADD FTM BASELINE + CLARIFY ADVANTAGE (mandatory)**: Cite arXiv 2512.02902 and explain why ACIBS's IB-based approach is preferable to FTM's simple affine transformation, which achieves 87.1% viewpoint robustness with 4K params. The argument should be: FTM is a fixed transformation that doesn't adapt per-timestep or per-token, doesn't generalize across perturbation types (viewpoint-specific), and has no information-theoretic guarantee. ACIBS provides adaptive, per-timestep token selection with provable information retention. Include FTM as experimental baseline.

2. **SPECIFY NUISANCE VARIABLE HANDLING (mandatory)**: Concretely describe how I(V_selected; N | A) is optimized without nuisance labels. Options: (a) use domain-randomized LIBERO variants as implicit nuisance samples during training (but this becomes data augmentation, undermining the 'no pixel-space augmentation' claim); (b) use a CLUB-style upper bound (Cheng et al., ICML 2020) that only requires paired clean observations; (c) use a variational decoder q(n|v) trained jointly to predict nuisance factors, following DRIBO's multi-view approach. Pick one and specify the training pipeline concretely.

3. **RESOLVE TIMELINE (mandatory)**: Either (a) explicitly scope the CoRL submission to a minimal viable paper: IB pruning only (no tangent-space augmentation), SmolVLA backbone only, 3-4 key perturbation dimensions from LIBERO-Plus, with full ablation deferred to camera-ready; or (b) designate AAAI 2027 as the primary target with CoRL as a stretch goal. The current '3-4 week' manual estimate is incompatible with the 12-day CoRL deadline.

Minor: cite arXiv 2505.18227 ('Token Reduction Should Go Beyond Efficiency') as supporting motivation, and correct CoRL deadline dates to official May 26/May 28-29.

### Round 3 review
Verdict: revise
Issues: ["VENUE TARGET MISMATCH: User explicitly requires 'Target: CoRL 2026' but the idea designates AAAI 2027 as primary target with CoRL as 'stretch goal.' The idea must be primarily scoped for CoRL 2026 with the 12-day timeline and 200h compute as hard constraints, not soft guidelines.", "SMOLVLA FACTUAL ERRORS: The idea states 'SmolVLM-256M vision backbone + Qwen2.5-0.5B LLM' but SmolVLA actually uses SmolVLM2-500M (SigLIP encoder) and SmolLM2 (HuggingFace's own LLM with layer skipping), not Qwen2.5-0.5B. These errors undermine credibility.", "MISSING COMPETITOR — SimPrune (ICLR 2025): 'Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning' explicitly enforces cross-branch augmentation consistency during token pruning — the same core mechanism as ACIBS's consistency loss ||S(V)-S(V')||². SimPrune targets training efficiency rather than robustness, but the conceptual overlap is substantial and must be cited and differentiated.", "MISSING COMPETITOR — TCA (ICCV 2025, arXiv 2410.14729): 'Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation' demonstrates that token condensation improves distribution shift robustness by up to 21.4% on CIFAR-100-C and cross-dataset benchmarks. This directly supports the 'token reduction helps robustness' thesis and provides prior evidence that the approach direction works, but also reduces novelty of the core claim.", "COMPUTE STILL EXCEEDS HARD CONSTRAINT: Manual estimate of 200-250h exceeds the user's hard ≤200h budget. The idea acknowledges 'may slightly exceed' but the user specified this as a HARD CONSTRAINT. The mitigation (evaluate 4 dimensions first, defer full 7 to camera-ready) is reasonable but should be the primary plan, not a fallback.", "PROVABLE ROBUSTNESS MARGINS CLAIM IS VAGUE: The description repeatedly claims 'provable robustness margins' and 'information-theoretic compression guarantees' but never specifies what theorem is proved. A VIB KL term provides an upper bound on I(X;Z) but converting this to a robustness margin (e.g., Lipschitz bound on action error under perturbation) requires additional assumptions that are not stated.", "FTM BASELINE RISK UNDER-DISCUSSED: FTM achieves 87.1% viewpoint / 90.5% avg on LIBERO-V with 4K params and trivial training. If FTM adapted to SmolVLA recovers most of the robustness gap, ACIBS's added complexity (50K scorer, dual-view training, IB tuning of α/β/k) may yield marginal improvement insufficient for a top-venue contribution. The idea should explicitly discuss what happens if FTM-on-SmolVLA is a strong baseline.", "SEVERAL RECENT VLA PRUNING METHODS UNCITED: VLA-Pruner (arXiv 2511.16449), SP-VLA (ICLR 2026, arXiv 2506.12723), ETA-VLA (arXiv 2603.25766), EcoVLA (arXiv 2602.00780), and OneWM-VLA (arXiv 2605.07931) are recent VLA-specific token pruning methods. While efficiency-focused, they represent the broader competitive landscape and key ones should be cited in the landscape section."]
Feedback: The Round 3 revision is substantially improved — the multi-view consistency reformulation elegantly solves the nuisance variable access problem from Round 2, the landscape coverage is now comprehensive (20+ papers), and the FTM/BC-IB/post-hoc differentiation is well-articulated. Four targeted fixes for Round 4:

1. **SCOPE FOR CoRL PRIMARY (mandatory)**: Restructure the entire submission plan around CoRL 2026 as the primary target. The scoped version you already describe (IB pruning + consistency loss, no tangent-space augmentation, SmolVLA only, 4 key perturbation dimensions) should be the MAIN plan, not a stretch fallback. Compute should be re-estimated to fit strictly within 200h: ~4 training configs × 12h = 48h + 4 models × 5h eval = 20h + 30h debugging = 98h, leaving margin. AAAI 2027 can be mentioned as the extended version.

2. **FIX SMOLVLA DETAILS + ADD SimPrune/TCA (mandatory)**: Correct the architecture to SmolVLM2-500M (SigLIP) + SmolLM2. Cite SimPrune (ICLR 2025) and differentiate: 'SimPrune enforces augmentation consistency for token pruning during self-supervised pretraining to maintain semantic alignment, targeting efficiency; ACIBS enforces consistency during VLA fine-tuning with an IB objective, targeting perturbation invariance for robustness.' Cite TCA (ICCV 2025) as supporting evidence that token reduction improves distribution shift robustness.

3. **SHARPEN THEORETICAL CLAIMS (mandatory)**: Either (a) state a concrete theorem: 'Under Assumptions X (Lipschitz action decoder, bounded perturbation ε), the VIB-trained scorer with retention rate k achieves action prediction error bounded by [expression]' — even if the proof is standard VIB theory applied to this setting; or (b) downgrade the claim from 'provable robustness margins' to 'information-theoretic motivation with empirical robustness improvement,' which is honest and still publishable at CoRL.

4. **EXPLICITLY PLAN FOR FTM BASELINE OUTCOME (recommended)**: Add a contingency analysis: 'If FTM adapted to SmolVLA achieves >X% on LIBERO-Plus, our contribution shifts to demonstrating that adaptive, per-token selection with IB grounding provides complementary gains — we can combine FTM's global modulation with ACIBS's selective pruning (FTM+ACIBS) and show the combination exceeds either alone.' This makes the paper robust to a strong FTM baseline result.

### Round 4 review
Verdict: revise
Issues: ["MISSING COMPETITOR — FocusVLA (arXiv 2603.28740, March 2026): FocusVLA dynamically selects task-relevant visual tokens via cross-attention-based top-K selection, achieving 98.7% on LIBERO with a 0.5B model. While it does NOT use IB objectives, augmentation consistency, or robustness evaluation, it IS a concurrent method targeting task-relevant visual token selection in VLAs and must be cited. Differentiation is clear: FocusVLA uses attention magnitude for accuracy-driven selection without robustness evaluation, while ACIBS uses IB-grounded scoring with multi-view consistency for perturbation invariance.", "COMPACT TOKEN SPACE RISK UNDER-ANALYZED: SmolVLA already aggressively compresses to 64 visual tokens per frame (via 3×3 pixel shuffle, 9× reduction). Further pruning to e.g. 32 tokens means each token carries enormous information density. The idea acknowledges α sensitivity but does not explicitly discuss what retention rates k are viable in this compact space or how this interacts with the IB objective. If the retention rate must be >80% (retaining >51 of 64 tokens) to preserve action accuracy, the actual 'pruning' may be minimal and the robustness benefit correspondingly small. The ablation plan should include a retention rate sweep (k ∈ {0.5, 0.6, 0.7, 0.8, 0.9}) with both nominal and perturbed accuracy reported.", "TIMELINE REMAINS EXTREMELY TIGHT: 15 days for implementation + training + evaluation + paper writing with zero margin for setbacks. The scoping (4 perturbation dimensions, no tangent-space augmentation) is appropriate, but even this scoped version requires: (a) implementing dual-view augmentation pipeline with LIBERO's randomization, (b) implementing Gumbel-softmax scorer integrated into SmolVLA's architecture, (c) adapting FTM to SmolVLA as baseline, (d) setting up LIBERO-Plus evaluation infrastructure, (e) running 4+ training configs and 5+ evaluation passes, (f) writing the paper. Any single component hitting an unexpected issue could derail the submission.", "MINOR: The auto_research GPU cost estimate ($450-$500) exceeds the manual estimate ($375-$450) despite using more GPU hours — this is internally consistent, but the auto mode at ~180-200h H100 is right at the hard constraint boundary with no margin for failed runs in autonomous mode."]
Feedback: This is a substantially mature idea after 4 rounds of revision — the core novelty holds, the formulation is clean, and all major prior concerns have been addressed. Two targeted fixes to push toward passing:

1. **ADD FocusVLA + ANALYZE RETENTION RATES (mandatory)**: Cite FocusVLA (arXiv 2603.28740) in the landscape as a concurrent attention-based token selection method (no IB, no robustness eval). More importantly, add explicit analysis of the retention rate k in SmolVLA's 64-token space: 'We plan a retention rate sweep k ∈ {0.5, 0.6, 0.7, 0.8, 0.9} (32-58 tokens retained). The compact 64-token input means even k=0.8 prunes 13 tokens — enough to remove background-dominated tokens while preserving manipulation-critical spatial information. The IB objective's KL term adapts the effective retention per-sample, so the prior p_0 sets a soft target rather than a hard cutoff.' This addresses the concern that pruning on top of already-compressed tokens may yield minimal effect.

2. **SHARPEN TIMELINE MITIGATION (recommended)**: Acknowledge that a single researcher executing the full pipeline in 15 days requires prior familiarity with SmolVLA/LeRobot and LIBERO infrastructure. Consider a progressive submission strategy: abstract by May 26 scoping the contribution, with the paper by May 29 potentially deferring FTM+ACIBS combination experiment to camera-ready if time runs short. This creates a minimal viable submission (ACIBS standalone + ablations) vs. ideal submission (+ FTM combination + more baselines).


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
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "6ae66a34-4867-47c2-8d3a-9d9313ecec64",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T06:56:22.884Z_

```json
{
  "parentUuid": "6ae66a34-4867-47c2-8d3a-9d9313ecec64",
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
  "uuid": "7cb7d247-85b9-4689-93e6-59995f7b0f50",
  "timestamp": "2026-05-14T06:56:22.884Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T06:56:22.884Z_

```json
{
  "parentUuid": "7cb7d247-85b9-4689-93e6-59995f7b0f50",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0d966331-5b5c-476f-97b5-6cb846a0ddb0",
  "timestamp": "2026-05-14T06:56:22.884Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0d966331-5b5c-476f-97b5-6cb846a0ddb0",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Assistant

_source line 8 · 2026-05-14T06:56:31.619Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed review request for a research idea that has gone through 4 rounds of revision. I'm now at round 5/10 and need to conduct an independent, rigorous review. Let me systematically verify the claims and assess the idea.

Let me start by searching for the key papers and competitors mentioned, and look for any missing work.

Key things to verify:
1. FocusVLA (arXiv 2603.28740) - was it added?
2. SmolVLA architecture details
3. LIBERO-Plus benchmarks and current SOTA
4. FTM paper details
5. SimPrune and TCA citations


6. Whether any new competitors have emerged since the last round
7. Whether the compute requirements are actually feasible
8. Whether the proposed timeline is realistic

Let me search systematically through these areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d966331-5b5c-476f-97b5-6cb846a0ddb0",
  "isSidechain": false,
  "requestId": "req_011Cb22PYBx98Wcxvfw67prZ",
  "type": "assistant",
  "uuid": "2d527f2f-b5a3-4a49-9078-7a53e88216bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EufLgmvSGE7a7Y2ABpdwHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24041,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24041
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

_source line 9 · 2026-05-14T06:56:31.625Z_

I'll conduct an independent verification of this idea's claims across multiple dimensions. Let me search systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d527f2f-b5a3-4a49-9078-7a53e88216bf",
  "isSidechain": false,
  "requestId": "req_011Cb22PYBx98Wcxvfw67prZ",
  "type": "assistant",
  "uuid": "4dd04b98-5bb3-4b04-a75e-5bcdd00ee5c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EufLgmvSGE7a7Y2ABpdwHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24041,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24041
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

_source line 10 · 2026-05-14T06:56:31.950Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Smxh42aS2nk74KVgEUcmNt`</summary>

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
  "parentUuid": "4dd04b98-5bb3-4b04-a75e-5bcdd00ee5c2",
  "isSidechain": false,
  "requestId": "req_011Cb22PYBx98Wcxvfw67prZ",
  "type": "assistant",
  "uuid": "d7a49df5-a76c-4882-9e7b-552f67215dbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EufLgmvSGE7a7Y2ABpdwHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24041,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24041
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

_source line 11 · 2026-05-14T06:56:31.956Z_

<details><summary>↩ Tool result · `toolu_01Smxh42aS2nk74KVgEUcmNt`</summary>

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
  "parentUuid": "d7a49df5-a76c-4882-9e7b-552f67215dbc",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "e5c3822c-3b38-493e-b9ef-f48591115eb6",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "d7a49df5-a76c-4882-9e7b-552f67215dbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T06:56:35.166Z_

Starting my independent verification. I'll search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c3822c-3b38-493e-b9ef-f48591115eb6",
  "isSidechain": false,
  "requestId": "req_011Cb22QD9VzX9ixAgJ4gZD4",
  "type": "assistant",
  "uuid": "6cd73511-d61e-4741-88a0-08cc9c308f4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAN5V9vhExmi4De9ctQDKa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 35882,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 35882,
          "cache_creation_input_tokens": 1313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1313
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

_source line 13 · 2026-05-14T06:56:36.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YCG5fApQxm3BwNfK5y2ukR`</summary>

```json
{
  "query": "FocusVLA visual token selection VLA 2026 arXiv 2603.28740"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cd73511-d61e-4741-88a0-08cc9c308f4e",
  "isSidechain": false,
  "requestId": "req_011Cb22QD9VzX9ixAgJ4gZD4",
  "type": "assistant",
  "uuid": "779f7654-42da-4bdf-956d-3ab31675d6d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAN5V9vhExmi4De9ctQDKa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 35882,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 35882,
          "cache_creation_input_tokens": 1313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1313
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

_source line 14 · 2026-05-14T06:56:43.601Z_

<details><summary>↩ Tool result · `toolu_01YCG5fApQxm3BwNfK5y2ukR`</summary>

```text
Web search results for query: "FocusVLA visual token selection VLA 2026 arXiv 2603.28740"

Links: [{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"[2603.28740] FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.28740"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World...","url":"https://arxiv.org/abs/2605.07931v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"}]

I found information about the FocusVLA paper (arXiv 2603.28740). Here's what I discovered:

## FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

Vision-Language-Action (VLA) models improve action generation by conditioning policies on rich vision-language information, but current auto-regressive policies are constrained by three bottlenecks: architectural bias drives models to overlook visual details, an excessive number of visual tokens makes attention difficult to focus on the correct regions, and task-irrelevant visual information introduces substantial noise.

The paper empirically validates that VLA performance is primarily limited by how visual information is utilized rather than by the quality of visual representations, and introduces FocusVLA, a novel paradigm that directs the model's attention to task-relevant visual regions to effectively bridge vision to action.

### Key Technical Contributions

The method proposes Modality Cascaded Attention to eliminate shortcut pathways, and Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise.

### Performance and Impact

Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.

Reducing visual token count via selective retention improves not only accuracy but also inference speed, making FocusVLA more suitable for real-time deployment than architectures that process all visual tokens uniformly.

The paper was submitted to arXiv on March 30, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "779f7654-42da-4bdf-956d-3ab31675d6d2",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "a3fa208c-49a1-49f5-97bf-d2c0b65bff6f",
  "toolUseResult": {
    "query": "FocusVLA visual token selection VLA 2026 arXiv 2603.28740",
    "results": [
      {
        "tool_use_id": "srvtoolu_016WauvN3NnEm7Eki1UDNmke",
        "content": [
          {
            "title": "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.28740"
          },
          {
            "title": "[2603.28740] FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.28740"
          },
          {
            "title": "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy",
            "url": "https://arxiv.org/html/2605.07931v1"
          },
          {
            "title": "Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics",
            "url": "https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"
          },
          {
            "title": "One Token Per Frame: Reconsidering Visual Bandwidth in World...",
            "url": "https://arxiv.org/abs/2605.07931v1"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.15618"
          },
          {
            "title": "[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          }
        ]
      },
      "I found information about the FocusVLA paper (arXiv 2603.28740). Here's what I discovered:\n\n## FocusVLA: Focused Visual Utilization for Vision-Language-Action Models\n\nVision-Language-Action (VLA) models improve action generation by conditioning policies on rich vision-language information, but current auto-regressive policies are constrained by three bottlenecks: architectural bias drives models to overlook visual details, an excessive number of visual tokens makes attention difficult to focus on the correct regions, and task-irrelevant visual information introduces substantial noise.\n\nThe paper empirically validates that VLA performance is primarily limited by how visual information is utilized rather than by the quality of visual representations, and introduces FocusVLA, a novel paradigm that directs the model's attention to task-relevant visual regions to effectively bridge vision to action.\n\n### Key Technical Contributions\n\nThe method proposes Modality Cascaded Attention to eliminate shortcut pathways, and Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise.\n\n### Performance and Impact\n\nExtensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.\n\nReducing visual token count via selective retention improves not only accuracy but also inference speed, making FocusVLA more suitable for real-time deployment than architectures that process all visual tokens uniformly.\n\nThe paper was submitted to arXiv on March 30, 2026."
    ],
    "durationSeconds": 7.480644636000001
  },
  "sourceToolAssistantUUID": "779f7654-42da-4bdf-956d-3ab31675d6d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T06:56:48.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JfMtfbfswuNJXnx6nXdM4S`</summary>

```json
{
  "query": "SmolVLA architecture SigLIP SmolLM2 visual tokens 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3fa208c-49a1-49f5-97bf-d2c0b65bff6f",
  "isSidechain": false,
  "requestId": "req_011Cb22R4baYD4jY7GCVu9Js",
  "type": "assistant",
  "uuid": "fea6bb67-7afd-496f-bdbd-df3ae52535b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015iodkPokqdbNLvDbttrRYm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 37195,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 37195,
          "cache_creation_input_tokens": 1018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1018
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

_source line 16 · 2026-05-14T06:56:56.658Z_

<details><summary>↩ Tool result · `toolu_01JfMtfbfswuNJXnx6nXdM4S`</summary>

```text
Web search results for query: "SmolVLA architecture SigLIP SmolLM2 visual tokens 2025"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLM to SmolVLM2: Compact Models for Multi-Image VQA - PyImageSearch","url":"https://pyimagesearch.com/2025/06/23/smolvlm-to-smolvlm2-compact-models-for-multi-image-vqa/"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"},{"title":"SmolVLM - small yet mighty Vision Language Model","url":"https://huggingface.co/blog/smolvlm"},{"title":"Papers Explained 346: SmolVLM. SmolVLM is a family of small, efficient… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-346-smolvlm-9b4e208fa66b"},{"title":"SmolVLM: Redefining small and efficient multimodal models","url":"https://arxiv.org/html/2504.05299v1"},{"title":"HuggingFaceTB/SmolVLM-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"},{"title":"Weekly Robotics June #1 - SmolVLA discovery and thoughts","url":"https://huggingface.co/blog/Beegbrain/daily-robotics-june"},{"title":"AI and Robotics: With SmolVLA, Hugging Face Opens Vision-Language-Action Models to the Community","url":"https://www.actuia.com/en/news/ai-and-robotics-with-smolvla-hugging-face-opens-vision-language-action-models-to-the-community/"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"}]

Based on the search results, here's comprehensive information about the SmolVLA architecture and its use of SigLIP, SmolLM2, and visual tokens:

## SmolVLA Architecture Overview

SmolVLA is a compact (450M) open-source Vision-Language-Action model for robotics that runs on consumer hardware. It uses SmolVLM2 as its VLM backbone, which is optimized for multi-image inputs and consists of a SigLIP vision encoder and a SmolLM2 language decoder.

## Core Components

**Vision Encoder (SigLIP):**
Each input image (or video frame) is first split into sub-images and encoded by a SigLIP (Sigmoid Loss for Language-Image Pretraining) vision encoder.

**Language Decoder (SmolLM2):**
For the language backbone, SmolVLM uses SmolLM2, a family of small transformer LMs (135M, 360M, 1.7B parameters).

## Visual Token Compression

A key innovation in SmolVLA is its aggressive visual token reduction. SmolVLA skips image tiling (used in the original SmolVLM2) and applies pixel shuffling on the global image only, reducing visual tokens to just 64 per frame. 

In the broader SmolVLM context, a 2×2 pixel shuffle turns each 2×2 block of pixels into 4 channels, so the feature map height and width each halve, reducing the token count by 4×.

## Efficiency Optimizations

Beyond token reduction, SmolVLA employs several optimization techniques: Visual token reduction limiting visual tokens to 64 per frame and using only global images without tiling, Layer skipping using only the first half of VLM layers effectively halving computational cost, and Interleaved attention combining cross-attention and self-attention layers in the action expert.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fea6bb67-7afd-496f-bdbd-df3ae52535b0",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "22c81da1-eb33-4006-8779-4ad5748d403f",
  "toolUseResult": {
    "query": "SmolVLA architecture SigLIP SmolLM2 visual tokens 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ln5EzswxAHQeUE527vUo3S",
        "content": [
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          },
          {
            "title": "SmolVLM to SmolVLM2: Compact Models for Multi-Image VQA - PyImageSearch",
            "url": "https://pyimagesearch.com/2025/06/23/smolvlm-to-smolvlm2-compact-models-for-multi-image-vqa/"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"
          },
          {
            "title": "SmolVLM - small yet mighty Vision Language Model",
            "url": "https://huggingface.co/blog/smolvlm"
          },
          {
            "title": "Papers Explained 346: SmolVLM. SmolVLM is a family of small, efficient… | by Ritvik Rastogi | Medium",
            "url": "https://ritvik19.medium.com/papers-explained-346-smolvlm-9b4e208fa66b"
          },
          {
            "title": "SmolVLM: Redefining small and efficient multimodal models",
            "url": "https://arxiv.org/html/2504.05299v1"
          },
          {
            "title": "HuggingFaceTB/SmolVLM-Instruct · Hugging Face",
            "url": "https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"
          },
          {
            "title": "Weekly Robotics June #1 - SmolVLA discovery and thoughts",
            "url": "https://huggingface.co/blog/Beegbrain/daily-robotics-june"
          },
          {
            "title": "AI and Robotics: With SmolVLA, Hugging Face Opens Vision-Language-Action Models to the Community",
            "url": "https://www.actuia.com/en/news/ai-and-robotics-with-smolvla-hugging-face-opens-vision-language-action-models-to-the-community/"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about the SmolVLA architecture and its use of SigLIP, SmolLM2, and visual tokens:\n\n## SmolVLA Architecture Overview\n\nSmolVLA is a compact (450M) open-source Vision-Language-Action model for robotics that runs on consumer hardware. It uses SmolVLM2 as its VLM backbone, which is optimized for multi-image inputs and consists of a SigLIP vision encoder and a SmolLM2 language decoder.\n\n## Core Components\n\n**Vision Encoder (SigLIP):**\nEach input image (or video frame) is first split into sub-images and encoded by a SigLIP (Sigmoid Loss for Language-Image Pretraining) vision encoder.\n\n**Language Decoder (SmolLM2):**\nFor the language backbone, SmolVLM uses SmolLM2, a family of small transformer LMs (135M, 360M, 1.7B parameters).\n\n## Visual Token Compression\n\nA key innovation in SmolVLA is its aggressive visual token reduction. SmolVLA skips image tiling (used in the original SmolVLM2) and applies pixel shuffling on the global image only, reducing visual tokens to just 64 per frame. \n\nIn the broader SmolVLM context, a 2×2 pixel shuffle turns each 2×2 block of pixels into 4 channels, so the feature map height and width each halve, reducing the token count by 4×.\n\n## Efficiency Optimizations\n\nBeyond token reduction, SmolVLA employs several optimization techniques: Visual token reduction limiting visual tokens to 64 per frame and using only global images without tiling, Layer skipping using only the first half of VLM layers effectively halving computational cost, and Interleaved attention combining cross-attention and self-attention layers in the action expert."
    ],
    "durationSeconds": 7.918006362999996
  },
  "sourceToolAssistantUUID": "fea6bb67-7afd-496f-bdbd-df3ae52535b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T06:57:00.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WkmuXK6AJiio8P6YURA9UR`</summary>

```json
{
  "query": "LIBERO-Plus robustness benchmark VLA SRPO SOTA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22c81da1-eb33-4006-8779-4ad5748d403f",
  "isSidechain": false,
  "requestId": "req_011Cb22S2QeKaprZLT7YDiFi",
  "type": "assistant",
  "uuid": "7c4f8359-3981-4cfe-90de-62d52a0c8305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVPuZ7FbpQLGJFvwjxwe4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 38213,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 38213,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 18 · 2026-05-14T06:57:06.701Z_

<details><summary>↩ Tool result · `toolu_01WkmuXK6AJiio8P6YURA9UR`</summary>

```text
Web search results for query: "LIBERO-Plus robustness benchmark VLA SRPO SOTA 2026"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"}]

Based on the search results, here's what I found about LIBERO-Plus, VLA robustness benchmarking, and SRPO:

## LIBERO-Plus Robustness Benchmark

LIBERO-Plus is a benchmark for in-depth robustness analysis of Vision-Language-Action models that systematically exposes hidden vulnerabilities through comprehensive robustness evaluation across seven perturbation dimensions. These dimensions include objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

### Key Findings on VLA Fragility

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### SRPO Performance (State-of-the-Art)

SRPO (Self-Referential Policy Optimization for Vision-Language-Action Models) achieved an average score of 82.1 on the LIBERO-Plus benchmark. Additionally, SRPO shows significant robustness on the LIBERO-Plus benchmark, achieving a 167% performance gain.

The benchmark reveals that LIBERO-Plus is designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c4f8359-3981-4cfe-90de-62d52a0c8305",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "ae4c2215-054d-47ab-a4c9-bd18eaea100b",
  "toolUseResult": {
    "query": "LIBERO-Plus robustness benchmark VLA SRPO SOTA 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017ZP47XzvdxMbpNG74dvmz6",
        "content": [
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "SRPO Code Implementation Explained — siiRL documentation",
            "url": "https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301"
          }
        ]
      },
      "Based on the search results, here's what I found about LIBERO-Plus, VLA robustness benchmarking, and SRPO:\n\n## LIBERO-Plus Robustness Benchmark\n\nLIBERO-Plus is a benchmark for in-depth robustness analysis of Vision-Language-Action models that systematically exposes hidden vulnerabilities through comprehensive robustness evaluation across seven perturbation dimensions. These dimensions include objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.\n\n### Key Findings on VLA Fragility\n\nModels exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\n### SRPO Performance (State-of-the-Art)\n\nSRPO (Self-Referential Policy Optimization for Vision-Language-Action Models) achieved an average score of 82.1 on the LIBERO-Plus benchmark. Additionally, SRPO shows significant robustness on the LIBERO-Plus benchmark, achieving a 167% performance gain.\n\nThe benchmark reveals that LIBERO-Plus is designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions."
    ],
    "durationSeconds": 6.493419784000005
  },
  "sourceToolAssistantUUID": "7c4f8359-3981-4cfe-90de-62d52a0c8305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ae4c2215-054d-47ab-a4c9-bd18eaea100b",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Tool call

_source line 21 · 2026-05-14T06:57:09.841Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YM9t4ex77Jq6iJDwuvPLRA`</summary>

```json
{
  "query": "FTM \"Feature Token Modulation\" VLA robustness arXiv 2512.02902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae4c2215-054d-47ab-a4c9-bd18eaea100b",
  "isSidechain": false,
  "requestId": "req_011Cb22SmNJ1ncrg7Ti6dvj2",
  "type": "assistant",
  "uuid": "7fefc30e-a50f-4c92-973d-ce8cf4766509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vJc8rAYL2wpSAt5XGe89J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 39334,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 927,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 39334,
          "cache_creation_input_tokens": 927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 927
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

_source line 22 · 2026-05-14T06:57:19.986Z_

<details><summary>↩ Tool result · `toolu_01YM9t4ex77Jq6iJDwuvPLRA`</summary>

```text
Web search results for query: "FTM "Feature Token Modulation" VLA robustness arXiv 2512.02902"

Links: [{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"[2512.02902] VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/abs/2512.02902"},{"title":"awesome-daily-AI-arxiv/hot_topic/Embodied_AI.md at main · Tavish9/awesome-daily-AI-arxiv","url":"https://github.com/Tavish9/awesome-daily-AI-arxiv/blob/main/hot_topic/Embodied_AI.md"},{"title":"Efficient Spatial Adaptation in VLA Models","url":"https://www.emergentmind.com/papers/2512.02902"},{"title":"Feature Token Modulation (FTM)","url":"https://www.emergentmind.com/topics/feature-token-modulation-ftm"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"}]

Based on the search results, I found detailed information about the paper you're looking for:

## Paper Overview

The paper is titled "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling" (arXiv 2512.02902).

## About Feature Token Modulation (FTM)

Feature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. 

FTM is a simple mechanism that applies a global affine transformation to visual token embeddings using only two learnable parameter vectors (γ,β), which re-scales and re-centers feature distributions, allowing the model to adapt rapidly to new visual domains.

## Problem Statement and Solution

Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations, with this brittleness primarily arising from misalignment in Spatial Modeling, rather than Physical Modeling.

The paper proposes a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates.

## Results and Impact

The method achieves consistent improvements across all four LIBERO suites (Spatial, Object, Goal, Long), with the Feature Token Modulation (FTM) variant achieving an average success rate of 87.2%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fefc30e-a50f-4c92-973d-ce8cf4766509",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "e60ba17e-c8a6-4faf-83d7-b4dfdebbfcd4",
  "toolUseResult": {
    "query": "FTM \"Feature Token Modulation\" VLA robustness arXiv 2512.02902",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TAG5nJNVLucKPs6VzzHeQa",
        "content": [
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902"
          },
          {
            "title": "[2512.02902] VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/abs/2512.02902"
          },
          {
            "title": "awesome-daily-AI-arxiv/hot_topic/Embodied_AI.md at main · Tavish9/awesome-daily-AI-arxiv",
            "url": "https://github.com/Tavish9/awesome-daily-AI-arxiv/blob/main/hot_topic/Embodied_AI.md"
          },
          {
            "title": "Efficient Spatial Adaptation in VLA Models",
            "url": "https://www.emergentmind.com/papers/2512.02902"
          },
          {
            "title": "Feature Token Modulation (FTM)",
            "url": "https://www.emergentmind.com/topics/feature-token-modulation-ftm"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.25766v1"
          },
          {
            "title": "Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2512.09927"
          },
          {
            "title": "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.19257"
          },
          {
            "title": "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://www.pi.website/download/fast.pdf"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper you're looking for:\n\n## Paper Overview\n\nThe paper is titled \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling\" (arXiv 2512.02902).\n\n## About Feature Token Modulation (FTM)\n\nFeature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. \n\nFTM is a simple mechanism that applies a global affine transformation to visual token embeddings using only two learnable parameter vectors (γ,β), which re-scales and re-centers feature distributions, allowing the model to adapt rapidly to new visual domains.\n\n## Problem Statement and Solution\n\nVision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations, with this brittleness primarily arising from misalignment in Spatial Modeling, rather than Physical Modeling.\n\nThe paper proposes a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates.\n\n## Results and Impact\n\nThe method achieves consistent improvements across all four LIBERO suites (Spatial, Object, Goal, Long), with the Feature Token Modulation (FTM) variant achieving an average success rate of 87.2%."
    ],
    "durationSeconds": 10.139787256000004
  },
  "sourceToolAssistantUUID": "7fefc30e-a50f-4c92-973d-ce8cf4766509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T06:57:22.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GtadoZXS5RLMqm8TKXD2oD`</summary>

```json
{
  "query": "SimPrune \"similarity-based token pruning\" self-supervised ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e60ba17e-c8a6-4faf-83d7-b4dfdebbfcd4",
  "isSidechain": false,
  "requestId": "req_011Cb22Tk8euu1mXUBmboHei",
  "type": "assistant",
  "uuid": "5b3e7d76-c011-4448-90d5-d077ccb9f9f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aPgSkPAafRXjzxZv26CgQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 40261,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 938,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 40261,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 938
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

_source line 24 · 2026-05-14T06:57:28.179Z_

<details><summary>↩ Tool result · `toolu_01GtadoZXS5RLMqm8TKXD2oD`</summary>

```text
Web search results for query: "SimPrune "similarity-based token pruning" self-supervised ICLR 2025"

Links: [{"title":"Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning | OpenReview","url":"https://openreview.net/forum?id=GTcEe5fayC"},{"title":"ICLR Poster Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning","url":"https://iclr.cc/virtual/2025/poster/30276"},{"title":"BASED TOKEN PRUNING FOR VISION TRANSFORMERS ...","url":"https://openreview.net/pdf?id=GTcEe5fayC"},{"title":"A SIMILARITY- BASED TOKEN PRUNING FOR VISION ...","url":"https://openreview.net/notes/edits/attachment?id=7I9FCztgnH&name=pdf"},{"title":"GitHub - F-JISOO/ICLR-2025-Submitted · GitHub","url":"https://github.com/F-JISOO/ICLR-2025-Submitted"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"GitHub - armenjeddi/saint: a training-free approach to accelerate ViTs and VLMs by pruning redundant tokens based on similarity","url":"https://github.com/ArmenJeddi/saint"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"}]

Based on the search results, I found information about SimPrune, a paper accepted at ICLR 2025:

## SimPrune: Similarity-Based Token Pruning for Vision Transformers in Self-Supervised Learning

SimPrune is a novel token pruning strategy designed for Vision Transformers (ViTs) in self-supervised learning. The full title is "Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning."

### Key Features

SimPrune leverages cross-branch similarity information to efficiently prune tokens, retaining essential semantic information across dual branches. The approach incorporates a difficulty-aware pruning strategy to further enhance SimPrune's effectiveness.

### Motivation

While token pruning can reduce training costs in supervised learning by removing less informative tokens, self-supervised learning's dual-branch encoders make traditional single-branch pruning strategies less effective, as they fail to account for critical cross-branch similarity information.

### Performance

Experimental results show that the approach effectively reduces training computation while maintaining accuracy, offering 24% savings in training costs compared to SSL baseline without sacrificing accuracy.

The paper has been published and is available on OpenReview and the official ICLR 2025 conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b3e7d76-c011-4448-90d5-d077ccb9f9f3",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "d6152f32-2e4a-4afa-b4e6-efa0d3aecc26",
  "toolUseResult": {
    "query": "SimPrune \"similarity-based token pruning\" self-supervised ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011y1Jdz6HyqG87UJ5cRbWTk",
        "content": [
          {
            "title": "Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning | OpenReview",
            "url": "https://openreview.net/forum?id=GTcEe5fayC"
          },
          {
            "title": "ICLR Poster Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning",
            "url": "https://iclr.cc/virtual/2025/poster/30276"
          },
          {
            "title": "BASED TOKEN PRUNING FOR VISION TRANSFORMERS ...",
            "url": "https://openreview.net/pdf?id=GTcEe5fayC"
          },
          {
            "title": "A SIMILARITY- BASED TOKEN PRUNING FOR VISION ...",
            "url": "https://openreview.net/notes/edits/attachment?id=7I9FCztgnH&name=pdf"
          },
          {
            "title": "GitHub - F-JISOO/ICLR-2025-Submitted · GitHub",
            "url": "https://github.com/F-JISOO/ICLR-2025-Submitted"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub",
            "url": "https://github.com/daixiangzi/Awesome-Token-Compress"
          },
          {
            "title": "Token Pruning",
            "url": "https://www.aussieai.com/research/token-pruning"
          },
          {
            "title": "GitHub - armenjeddi/saint: a training-free approach to accelerate ViTs and VLMs by pruning redundant tokens based on similarity",
            "url": "https://github.com/ArmenJeddi/saint"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models",
            "url": "https://aclanthology.org/2025.findings-acl.802.pdf"
          }
        ]
      },
      "Based on the search results, I found information about SimPrune, a paper accepted at ICLR 2025:\n\n## SimPrune: Similarity-Based Token Pruning for Vision Transformers in Self-Supervised Learning\n\nSimPrune is a novel token pruning strategy designed for Vision Transformers (ViTs) in self-supervised learning. The full title is \"Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning.\"\n\n### Key Features\n\nSimPrune leverages cross-branch similarity information to efficiently prune tokens, retaining essential semantic information across dual branches. The approach incorporates a difficulty-aware pruning strategy to further enhance SimPrune's effectiveness.\n\n### Motivation\n\nWhile token pruning can reduce training costs in supervised learning by removing less informative tokens, self-supervised learning's dual-branch encoders make traditional single-branch pruning strategies less effective, as they fail to account for critical cross-branch similarity information.\n\n### Performance\n\nExperimental results show that the approach effectively reduces training computation while maintaining accuracy, offering 24% savings in training costs compared to SSL baseline without sacrificing accuracy.\n\nThe paper has been published and is available on OpenReview and the official ICLR 2025 conference website."
    ],
    "durationSeconds": 5.786605663000002
  },
  "sourceToolAssistantUUID": "5b3e7d76-c011-4448-90d5-d077ccb9f9f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-14T06:57:30.843Z_

Good, confirmed SimPrune exists at ICLR 2025. Now let me search for more potential competitors and counter-evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6152f32-2e4a-4afa-b4e6-efa0d3aecc26",
  "isSidechain": false,
  "requestId": "req_011Cb22UMAKJgkDLwv8FWFpW",
  "type": "assistant",
  "uuid": "e08390b6-b47c-4eb2-a63c-658f836859f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVQRY4fPWJjbdJxMnndBgz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 41199,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 41199,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 26 · 2026-05-14T06:57:31.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017susWuWGvd1RrvrxeGy4L3`</summary>

```json
{
  "query": "token pruning robustness vision transformer distribution shift 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e08390b6-b47c-4eb2-a63c-658f836859f0",
  "isSidechain": false,
  "requestId": "req_011Cb22UMAKJgkDLwv8FWFpW",
  "type": "assistant",
  "uuid": "909d1835-8781-472b-96a4-78be4acf319b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVQRY4fPWJjbdJxMnndBgz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 41199,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 41199,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 27 · 2026-05-14T06:57:38.865Z_

<details><summary>↩ Tool result · `toolu_017susWuWGvd1RrvrxeGy4L3`</summary>

```text
Web search results for query: "token pruning robustness vision transformer distribution shift 2025 2026"

Links: [{"title":"Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06265-z"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"Advancing Transformer Efficiency with Token Pruning[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202503.1577"},{"title":"BASED TOKEN PRUNING FOR VISION TRANSFORMERS ...","url":"https://openreview.net/pdf?id=GTcEe5fayC"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT","url":"https://arxiv.org/html/2602.15720v1"},{"title":"Efficient Token Compression for Vision Transformer with Spatial Information Preserved","url":"https://arxiv.org/html/2503.23455v1"},{"title":"Token Pruning in Transformers","url":"https://www.emergentmind.com/topics/token-pruning-framework"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network | Request PDF","url":"https://www.researchgate.net/publication/390526506_Efficient_token_pruning_in_vision_transformers_using_an_attention-based_multilayer_network"},{"title":"Reducing Computational Overhead in Transformers with Token Pruning by Wang Lei, Zhang Wei, Shui Xiuying :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5171805.pdf?abstractid=5171805&mirid=1"}]

I've found search results on token pruning in vision transformers from 2025-2026. Here's a summary of the key findings:

## Main Research Findings

### Robustness Challenges with Distribution Shift

One of the primary concerns with token pruning is the potential degradation in model generalization and robustness, including domain shift sensitivity where pruned models may perform well on specific datasets but struggle when applied to out-of-distribution inputs. Pruning strategies may unintentionally remove critical tokens, making models more susceptible to adversarial attacks.

### Recent Approaches (2025-2026)

Several recent papers address these challenges:

1. **Automatic Pruning Rate Adjustment**: Research by Ishibashi and Meng on automatic pruning rate adjustment for dynamic token reduction in vision transformers was published in Applied Intelligence in 2025.

2. **Spatial Information Preservation**: One method enhances the Prune and Merge strategy by incorporating prior knowledge from the training dataset, showing high efficacy in classification tasks with stable target positions, but faces challenges with random transformations and in semantic segmentation where target positions vary.

3. **Self-Supervised Learning Approaches**: Self-supervised learning is more sensitive to attention-based token pruning than supervised learning, and pruning dissimilar token pairs may enhance the model's ability to learn more robust and generalized features.

### Future Directions

Future research should explore adaptive pruning mechanisms that dynamically adjust to varying input distributions and task requirements. Key challenges include ensuring generalization across diverse tasks and domains, and promising future directions include reinforcement learning-based adaptive pruning and hardware-aware pruning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "909d1835-8781-472b-96a4-78be4acf319b",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "f92b19bc-2ed8-4d91-945f-a29c31f96186",
  "toolUseResult": {
    "query": "token pruning robustness vision transformer distribution shift 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ELCgkDdyQH7gtBESUts6Nf",
        "content": [
          {
            "title": "Automatic pruning rate adjustment for dynamic token reduction in vision transformer | Applied Intelligence | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10489-025-06265-z"
          },
          {
            "title": "Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0957417425010711"
          },
          {
            "title": "Advancing Transformer Efficiency with Token Pruning[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202503.1577"
          },
          {
            "title": "BASED TOKEN PRUNING FOR VISION TRANSFORMERS ...",
            "url": "https://openreview.net/pdf?id=GTcEe5fayC"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT",
            "url": "https://arxiv.org/html/2602.15720v1"
          },
          {
            "title": "Efficient Token Compression for Vision Transformer with Spatial Information Preserved",
            "url": "https://arxiv.org/html/2503.23455v1"
          },
          {
            "title": "Token Pruning in Transformers",
            "url": "https://www.emergentmind.com/topics/token-pruning-framework"
          },
          {
            "title": "Efficient token pruning in Vision Transformers using an attention-based Multilayer Network | Request PDF",
            "url": "https://www.researchgate.net/publication/390526506_Efficient_token_pruning_in_vision_transformers_using_an_attention-based_multilayer_network"
          },
          {
            "title": "Reducing Computational Overhead in Transformers with Token Pruning by Wang Lei, Zhang Wei, Shui Xiuying :: SSRN",
            "url": "https://papers.ssrn.com/sol3/Delivery.cfm/5171805.pdf?abstractid=5171805&mirid=1"
          }
        ]
      },
      "I've found search results on token pruning in vision transformers from 2025-2026. Here's a summary of the key findings:\n\n## Main Research Findings\n\n### Robustness Challenges with Distribution Shift\n\nOne of the primary concerns with token pruning is the potential degradation in model generalization and robustness, including domain shift sensitivity where pruned models may perform well on specific datasets but struggle when applied to out-of-distribution inputs. Pruning strategies may unintentionally remove critical tokens, making models more susceptible to adversarial attacks.\n\n### Recent Approaches (2025-2026)\n\nSeveral recent papers address these challenges:\n\n1. **Automatic Pruning Rate Adjustment**: Research by Ishibashi and Meng on automatic pruning rate adjustment for dynamic token reduction in vision transformers was published in Applied Intelligence in 2025.\n\n2. **Spatial Information Preservation**: One method enhances the Prune and Merge strategy by incorporating prior knowledge from the training dataset, showing high efficacy in classification tasks with stable target positions, but faces challenges with random transformations and in semantic segmentation where target positions vary.\n\n3. **Self-Supervised Learning Approaches**: Self-supervised learning is more sensitive to attention-based token pruning than supervised learning, and pruning dissimilar token pairs may enhance the model's ability to learn more robust and generalized features.\n\n### Future Directions\n\nFuture research should explore adaptive pruning mechanisms that dynamically adjust to varying input distributions and task requirements. Key challenges include ensuring generalization across diverse tasks and domains, and promising future directions include reinforcement learning-based adaptive pruning and hardware-aware pruning approaches."
    ],
    "durationSeconds": 7.379922674999994
  },
  "sourceToolAssistantUUID": "909d1835-8781-472b-96a4-78be4acf319b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-14T06:57:38.872Z_

```json
{
  "parentUuid": "f92b19bc-2ed8-4d91-945f-a29c31f96186",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "37e713bf-452c-4413-94fa-a4ab9984d839",
  "timestamp": "2026-05-14T06:57:38.872Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 29 · 2026-05-14T06:57:46.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HoRiWb3BEcvpwJaNDUJ9FR`</summary>

```json
{
  "query": "information bottleneck token selection VLA robot manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37e713bf-452c-4413-94fa-a4ab9984d839",
  "isSidechain": false,
  "requestId": "req_011Cb22V8rB3BPtPyD4HB514",
  "type": "assistant",
  "uuid": "1b1d6b5b-e23e-49d6-9821-52884d4bf648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XT3nPPachdvTf5qBopnw6S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 42135,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 42135,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
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

_source line 30 · 2026-05-14T06:57:55.978Z_

<details><summary>↩ Tool result · `toolu_01HoRiWb3BEcvpwJaNDUJ9FR`</summary>

```text
Web search results for query: "information bottleneck token selection VLA robot manipulation 2025 2026"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Precise Manipulation with Efficient Online RL","url":"https://www.pi.website/research/rlt"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"}]

I've performed the web search on "information bottleneck token selection VLA robot manipulation 2025 2026". Here are the key findings:

## Recent Research on Token Selection and Compression in VLA Models

The significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment in Vision-Language-Action models.

Several approaches have been developed to address this:

### Instruction-Guided Compression
The Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details, with compression dynamically modulated by the natural language instruction. This approach achieves competitive success rates while reducing FLOPs by 59% and visual token count by over 3x.

### Information Bottleneck Approach
One method trains a VLA to produce an "RL token" through an encoder-decoder transformer trained to predict the model's internal embeddings through a bottleneck, with the RL token serving as an information bottleneck. This RL token summarizes the information that the RL actor and critic need about the current observation.

### Token-Per-Frame Design
OneWM-VLA uses Adaptive Attention Pooling to distill each view into a single semantic latent token per frame, realizing a bottleneck–rollout coupling through a single-token-per-frame design and joint flow-matching objective.

### Interaction-Aligned Pruning
VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and evaluates physical importance of tokens across three dimensions: Semantic Prior, Motion Prior, and Geometric Prior.

### Differentiable Token Selection
LightVLA addresses efficiency through adaptive, performance-driven pruning of visual tokens by generating dynamic queries to evaluate visual token importance and adopting Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b1d6b5b-e23e-49d6-9821-52884d4bf648",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "0320857a-c1ab-442e-9d34-eb89a006f833",
  "toolUseResult": {
    "query": "information bottleneck token selection VLA robot manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ELFAtkU1kacUYB4TNEjcDz",
        "content": [
          {
            "title": "[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.18950"
          },
          {
            "title": "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy",
            "url": "https://arxiv.org/html/2605.07931v1"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "Precise Manipulation with Efficient Online RL",
            "url": "https://www.pi.website/research/rlt"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "Publications | Chenjia Bai",
            "url": "http://baichenjia.cn/publication/"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          }
        ]
      },
      "I've performed the web search on \"information bottleneck token selection VLA robot manipulation 2025 2026\". Here are the key findings:\n\n## Recent Research on Token Selection and Compression in VLA Models\n\nThe significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment in Vision-Language-Action models.\n\nSeveral approaches have been developed to address this:\n\n### Instruction-Guided Compression\nThe Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details, with compression dynamically modulated by the natural language instruction. This approach achieves competitive success rates while reducing FLOPs by 59% and visual token count by over 3x.\n\n### Information Bottleneck Approach\nOne method trains a VLA to produce an \"RL token\" through an encoder-decoder transformer trained to predict the model's internal embeddings through a bottleneck, with the RL token serving as an information bottleneck. This RL token summarizes the information that the RL actor and critic need about the current observation.\n\n### Token-Per-Frame Design\nOneWM-VLA uses Adaptive Attention Pooling to distill each view into a single semantic latent token per frame, realizing a bottleneck–rollout coupling through a single-token-per-frame design and joint flow-matching objective.\n\n### Interaction-Aligned Pruning\nVLA-IAP introduces a geometric prior mechanism to preserve structural anchors and evaluates physical importance of tokens across three dimensions: Semantic Prior, Motion Prior, and Geometric Prior.\n\n### Differentiable Token Selection\nLightVLA addresses efficiency through adaptive, performance-driven pruning of visual tokens by generating dynamic queries to evaluate visual token importance and adopting Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens."
    ],
    "durationSeconds": 9.406739438000004
  },
  "sourceToolAssistantUUID": "1b1d6b5b-e23e-49d6-9821-52884d4bf648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0320857a-c1ab-442e-9d34-eb89a006f833",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Tool call

_source line 33 · 2026-05-14T06:57:58.548Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMo8tZGCdZHrbhcxKndKsz`</summary>

```json
{
  "query": "BC-IB \"information bottleneck\" behavior cloning ICML 2025 arXiv 2502.02853"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0320857a-c1ab-442e-9d34-eb89a006f833",
  "isSidechain": false,
  "requestId": "req_011Cb22WQ1GqH6qSLdy2ZKem",
  "type": "assistant",
  "uuid": "27dbe11b-92da-4368-b78a-73f76605b0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9J6vWCXFrNJeY9xaAaTmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 43288,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1041,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 43288,
          "cache_creation_input_tokens": 1041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1041
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

_source line 34 · 2026-05-14T06:58:05.431Z_

<details><summary>↩ Tool result · `toolu_01AMo8tZGCdZHrbhcxKndKsz`</summary>

```text
Web search results for query: "BC-IB "information bottleneck" behavior cloning ICML 2025 arXiv 2502.02853"

Links: [{"title":"[2502.02853] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/abs/2502.02853"},{"title":"GitHub - BaiShuanghao/BC-IB: [ICML 2025] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://github.com/BaiShuanghao/BC-IB"},{"title":"BC-IB for Robot Manipulation - GitHub Pages","url":"https://baishuanghao.github.io/BC-IB.github.io/"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853v1"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://arxiv.org/html/2502.02853"},{"title":"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=N2Dey442PJ"},{"title":"[Literature Review] Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://www.themoonlight.io/en/review/rethinking-latent-representations-in-behavior-cloning-an-information-bottleneck-approach-for-robot-manipulation"},{"title":"ICML Poster Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation","url":"https://icml.cc/virtual/2025/poster/45521"},{"title":"Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | Request PDF","url":"https://www.researchgate.net/publication/388754555_Rethinking_Latent_Representations_in_Behavior_Cloning_An_Information_Bottleneck_Approach_for_Robot_Manipulation"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=1225&show=2000"}]

I've found comprehensive information about this paper. Here's what the search results show:

## Paper Overview

The paper is titled "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation" with arXiv ID 2502.02853.

## Key Contribution

The authors adopt an information-theoretic perspective and introduce mutual information to quantify and mitigate redundancy in latent representations, incorporating the Information Bottleneck (IB) principle into BC to provide a structured framework for compressing irrelevant information while preserving task-relevant features.

## Motivation

Behavior Cloning (BC) is a widely adopted visual imitation learning method in robot manipulation that enhances generalization by leveraging large datasets and incorporating additional visual and textual modalities. However, these methods overlook whether the learned representations contain redundant information and lack a solid theoretical foundation to guide the learning process.

## Experimental Validation

Extensive experiments and analyses on the CortexBench and LIBERO benchmarks demonstrate significant performance improvements with IB, underscoring the importance of reducing input data redundancy and highlighting its practical value for more practical applications.

## Publication Status

The paper is accepted at ICML 2025, and the authors are Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, and Badong Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27dbe11b-92da-4368-b78a-73f76605b0fb",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "276cc326-e220-4943-8510-196b6a64cd86",
  "toolUseResult": {
    "query": "BC-IB \"information bottleneck\" behavior cloning ICML 2025 arXiv 2502.02853",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R99bdqAdzPi41zFBRNhiEE",
        "content": [
          {
            "title": "[2502.02853] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://arxiv.org/abs/2502.02853"
          },
          {
            "title": "GitHub - BaiShuanghao/BC-IB: [ICML 2025] Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://github.com/BaiShuanghao/BC-IB"
          },
          {
            "title": "BC-IB for Robot Manipulation - GitHub Pages",
            "url": "https://baishuanghao.github.io/BC-IB.github.io/"
          },
          {
            "title": "Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://arxiv.org/html/2502.02853v1"
          },
          {
            "title": "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://arxiv.org/html/2502.02853"
          },
          {
            "title": "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=N2Dey442PJ"
          },
          {
            "title": "[Literature Review] Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://www.themoonlight.io/en/review/rethinking-latent-representations-in-behavior-cloning-an-information-bottleneck-approach-for-robot-manipulation"
          },
          {
            "title": "ICML Poster Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation",
            "url": "https://icml.cc/virtual/2025/poster/45521"
          },
          {
            "title": "Rethinking Latent Representations in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation | Request PDF",
            "url": "https://www.researchgate.net/publication/388754555_Rethinking_Latent_Representations_in_Behavior_Cloning_An_Information_Bottleneck_Approach_for_Robot_Manipulation"
          },
          {
            "title": "Computer Science Feb 2025",
            "url": "https://arxiv.org/list/cs/2025-02?skip=1225&show=2000"
          }
        ]
      },
      "I've found comprehensive information about this paper. Here's what the search results show:\n\n## Paper Overview\n\nThe paper is titled \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation\" with arXiv ID 2502.02853.\n\n## Key Contribution\n\nThe authors adopt an information-theoretic perspective and introduce mutual information to quantify and mitigate redundancy in latent representations, incorporating the Information Bottleneck (IB) principle into BC to provide a structured framework for compressing irrelevant information while preserving task-relevant features.\n\n## Motivation\n\nBehavior Cloning (BC) is a widely adopted visual imitation learning method in robot manipulation that enhances generalization by leveraging large datasets and incorporating additional visual and textual modalities. However, these methods overlook whether the learned representations contain redundant information and lack a solid theoretical foundation to guide the learning process.\n\n## Experimental Validation\n\nExtensive experiments and analyses on the CortexBench and LIBERO benchmarks demonstrate significant performance improvements with IB, underscoring the importance of reducing input data redundancy and highlighting its practical value for more practical applications.\n\n## Publication Status\n\nThe paper is accepted at ICML 2025, and the authors are Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, and Badong Chen."
    ],
    "durationSeconds": 6.878625159999996
  },
  "sourceToolAssistantUUID": "27dbe11b-92da-4368-b78a-73f76605b0fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T06:58:11.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PABGteiCRBbWu8BktQTFqE`</summary>

```json
{
  "query": "CoRL 2026 submission deadline abstract paper Austin November"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "276cc326-e220-4943-8510-196b6a64cd86",
  "isSidechain": false,
  "requestId": "req_011Cb22X6S8CcyVVNoFCzqu5",
  "type": "assistant",
  "uuid": "ea2e4a4a-affd-45ff-b77c-dfa61b59e9a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZZQdvGBf8ADBubGAwrDtQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 44329,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 44329,
          "cache_creation_input_tokens": 1084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1084
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

_source line 36 · 2026-05-14T06:58:16.541Z_

<details><summary>↩ Tool result · `toolu_01PABGteiCRBbWu8BktQTFqE`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline abstract paper Austin November"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on the search results, here is the information about CoRL 2026 submission deadlines:

**Abstract Submission Deadline:** May 26, 2026 11:59 UTC

**Paper Submission Deadline:** May 29, 2026 11:59 UTC

**Conference Details:** The conference will be held November 9-12, 2026 at JW Marriott Austin, 110 E 2nd St, Austin, TX 78701

**Important Note:** The deadlines are final, and no accommodations can be made for missing the abstract deadline or paper deadline. Additionally, authors may update the title and abstract on OpenReview after the abstract submission deadline, but authors cannot be added or removed after this deadline, as this information is required to facilitate reviewer assignments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea2e4a4a-affd-45ff-b77c-dfa61b59e9a5",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "359d4588-1aff-445a-a073-0dd51b03ba8d",
  "toolUseResult": {
    "query": "CoRL 2026 submission deadline abstract paper Austin November",
    "results": [
      {
        "tool_use_id": "srvtoolu_012RGwU2CsmHWuSRzPW3MpNL",
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
            "title": "CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz",
            "url": "https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          }
        ]
      },
      "Based on the search results, here is the information about CoRL 2026 submission deadlines:\n\n**Abstract Submission Deadline:** May 26, 2026 11:59 UTC\n\n**Paper Submission Deadline:** May 29, 2026 11:59 UTC\n\n**Conference Details:** The conference will be held November 9-12, 2026 at JW Marriott Austin, 110 E 2nd St, Austin, TX 78701\n\n**Important Note:** The deadlines are final, and no accommodations can be made for missing the abstract deadline or paper deadline. Additionally, authors may update the title and abstract on OpenReview after the abstract submission deadline, but authors cannot be added or removed after this deadline, as this information is required to facilitate reviewer assignments."
    ],
    "durationSeconds": 4.611964260000008
  },
  "sourceToolAssistantUUID": "ea2e4a4a-affd-45ff-b77c-dfa61b59e9a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T06:58:19.817Z_

Good, CoRL deadlines confirmed: May 26 abstract, May 29 paper. Now let me search for potential competitors the idea may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "359d4588-1aff-445a-a073-0dd51b03ba8d",
  "isSidechain": false,
  "requestId": "req_011Cb22XuybsKKTtjZMcwnEo",
  "type": "assistant",
  "uuid": "e5f93db5-2fea-4bf4-8f62-4716c759b296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXeFfwX73yJWKx2wyZtoFq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 45413,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 45413,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 691
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

_source line 38 · 2026-05-14T06:58:20.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6iNwV27aL41f1x18XM83r`</summary>

```json
{
  "query": "VLA visual token robustness perturbation invariant 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5f93db5-2fea-4bf4-8f62-4716c759b296",
  "isSidechain": false,
  "requestId": "req_011Cb22XuybsKKTtjZMcwnEo",
  "type": "assistant",
  "uuid": "59df272b-3057-445f-adb2-74c9955540ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXeFfwX73yJWKx2wyZtoFq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 45413,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 45413,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 691
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

_source line 39 · 2026-05-14T06:58:28.606Z_

<details><summary>↩ Tool result · `toolu_01N6iNwV27aL41f1x18XM83r`</summary>

```text
Web search results for query: "VLA visual token robustness perturbation invariant 2026 arXiv"

Links: [{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v3"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations","url":"https://arxiv.org/html/2509.18953v1"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"ℰ₀: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion","url":"https://arxiv.org/html/2511.21542"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"}]

I found several highly relevant papers related to your search query. Here are the key findings:

## Main Result: "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations"

The primary paper evaluates and enhances the robustness of VLAs to multi-modal perturbations, beginning by evaluating the robustness of mainstream VLAs against 17 uncertainties across four modalities. The findings show that action is the most fragile modality, existing visual-robust VLAs do not show improvements in other modalities, and π0 demonstrates superior robustness, outperforming OpenVLA and π0-FAST by large margins.

The approach ensures that noise does not alter the semantics of the current state so the optimal action remains invariant, and regularizes the objective to maintain consistent output actions across diverse input perturbations.

## Related Work on Visual Token Robustness

There are also several complementary papers on this topic:

1. **VLA-IAP (Visual Token Pruning)**: VLA-IAP (Interaction-Aligned Pruning) introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

2. **Spatial Modeling and Perturbation Invariance**: Under viewpoint perturbations, the visual tokens produced by Spatial Modeling become misaligned with the Physical Modeling components, yet even minimal token-level modulation is sufficient to substantially recover robustness.

3. **Compression and Adversarial Robustness**: Visual token compression is widely used to accelerate large vision-language models by pruning or merging visual tokens, yet its adversarial robustness remains unexplored, with existing encoder-based attacks substantially overestimating the robustness of compressed LVLMs due to an optimization-inference mismatch.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59df272b-3057-445f-adb2-74c9955540ea",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "4f919d58-935d-4b93-be6a-c126b9c8b2ef",
  "toolUseResult": {
    "query": "VLA visual token robustness perturbation invariant 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Urzhcvuv4mvEN3zBtGTPRA",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 ON ROBUSTNESS",
            "url": "https://arxiv.org/pdf/2510.00037v4"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/html/2510.00037"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v3"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations",
            "url": "https://arxiv.org/html/2509.18953v1"
          },
          {
            "title": "[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression",
            "url": "https://arxiv.org/abs/2601.21531"
          },
          {
            "title": "ℰ₀: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion",
            "url": "https://arxiv.org/html/2511.21542"
          },
          {
            "title": "VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models",
            "url": "https://arxiv.org/html/2604.03956v2"
          }
        ]
      },
      "I found several highly relevant papers related to your search query. Here are the key findings:\n\n## Main Result: \"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations\"\n\nThe primary paper evaluates and enhances the robustness of VLAs to multi-modal perturbations, beginning by evaluating the robustness of mainstream VLAs against 17 uncertainties across four modalities. The findings show that action is the most fragile modality, existing visual-robust VLAs do not show improvements in other modalities, and π0 demonstrates superior robustness, outperforming OpenVLA and π0-FAST by large margins.\n\nThe approach ensures that noise does not alter the semantics of the current state so the optimal action remains invariant, and regularizes the objective to maintain consistent output actions across diverse input perturbations.\n\n## Related Work on Visual Token Robustness\n\nThere are also several complementary papers on this topic:\n\n1. **VLA-IAP (Visual Token Pruning)**: VLA-IAP (Interaction-Aligned Pruning) introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.\n\n2. **Spatial Modeling and Perturbation Invariance**: Under viewpoint perturbations, the visual tokens produced by Spatial Modeling become misaligned with the Physical Modeling components, yet even minimal token-level modulation is sufficient to substantially recover robustness.\n\n3. **Compression and Adversarial Robustness**: Visual token compression is widely used to accelerate large vision-language models by pruning or merging visual tokens, yet its adversarial robustness remains unexplored, with existing encoder-based attacks substantially overestimating the robustness of compressed LVLMs due to an optimization-inference mismatch."
    ],
    "durationSeconds": 8.190115504999994
  },
  "sourceToolAssistantUUID": "59df272b-3057-445f-adb2-74c9955540ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T06:58:33.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qbj2wCtW88JDZZi55vmY9R`</summary>

```json
{
  "query": "\"token reduction should go beyond efficiency\" arXiv 2505.18227 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f919d58-935d-4b93-be6a-c126b9c8b2ef",
  "isSidechain": false,
  "requestId": "req_011Cb22YoWCU6aA7FFUCDqMG",
  "type": "assistant",
  "uuid": "c910285d-7389-411d-9d2d-d58c8df78b26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4z7iuy7FBQEoSLrbD9ZzA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 46104,
      "output_tokens": 71,
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
          "output_tokens": 71,
          "cache_read_input_tokens": 46104,
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

_source line 41 · 2026-05-14T06:58:39.501Z_

<details><summary>↩ Tool result · `toolu_01Qbj2wCtW88JDZZi55vmY9R`</summary>

```text
Web search results for query: ""token reduction should go beyond efficiency" arXiv 2505.18227 2025"

Links: [{"title":"[2505.18227] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"[2505.18227v2] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227v2"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518227K/abstract"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.18227v2"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"(PDF) Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://www.researchgate.net/publication/392104162_Token_Reduction_Should_Go_Beyond_Efficiency_in_Generative_Models_--_From_Vision_Language_to_Multimodality"},{"title":"Token Reduction","url":"https://www.aussieai.com/research/token-reduction"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=1850&show=2000"}]

I found the paper you're looking for. Here's what I found about arXiv paper 2505.18227:

**Paper Title:** Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality

**Authors:** Zhenglun Kong, Yize Li, Fanhu Zeng, Lei Xin, Shvat Messica, Xue Lin, Pu Zhao, Manolis Kellis, Hao Tang, and Marinka Zitnik

**Key Argument:** While token reduction has primarily been used as an efficiency strategy due to the quadratic computational complexity of transformer self-attention mechanisms, this paper argues that token reduction should transcend its traditional efficiency-oriented role in the era of large generative models.

**Research Context:** Token reduction has been widely adopted in computer vision, language processing, and multimodal tasks. The paper examines token reduction beyond just computational efficiency, positioning it as a fundamental principle in generative modeling, critically influencing both model architecture and broader applications.

The paper was submitted on 23 May 2025 with subsequent revisions on 28 Jul 2025 and 12 Jan 2026. You can access it directly at the arXiv link: https://arxiv.org/abs/2505.18227


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c910285d-7389-411d-9d2d-d58c8df78b26",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "b526ba35-5e07-4df2-8b62-15bd29b5d0b4",
  "toolUseResult": {
    "query": "\"token reduction should go beyond efficiency\" arXiv 2505.18227 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ANkvRJzoRgCV25W7mha9YE",
        "content": [
          {
            "title": "[2505.18227] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality",
            "url": "https://arxiv.org/abs/2505.18227"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in ...",
            "url": "https://arxiv.org/pdf/2505.18227"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality",
            "url": "https://arxiv.org/html/2505.18227v1"
          },
          {
            "title": "[2505.18227v2] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality",
            "url": "https://arxiv.org/abs/2505.18227v2"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250518227K/abstract"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2505.18227v2"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "(PDF) Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality",
            "url": "https://www.researchgate.net/publication/392104162_Token_Reduction_Should_Go_Beyond_Efficiency_in_Generative_Models_--_From_Vision_Language_to_Multimodality"
          },
          {
            "title": "Token Reduction",
            "url": "https://www.aussieai.com/research/token-reduction"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=1850&show=2000"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found about arXiv paper 2505.18227:\n\n**Paper Title:** Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality\n\n**Authors:** Zhenglun Kong, Yize Li, Fanhu Zeng, Lei Xin, Shvat Messica, Xue Lin, Pu Zhao, Manolis Kellis, Hao Tang, and Marinka Zitnik\n\n**Key Argument:** While token reduction has primarily been used as an efficiency strategy due to the quadratic computational complexity of transformer self-attention mechanisms, this paper argues that token reduction should transcend its traditional efficiency-oriented role in the era of large generative models.\n\n**Research Context:** Token reduction has been widely adopted in computer vision, language processing, and multimodal tasks. The paper examines token reduction beyond just computational efficiency, positioning it as a fundamental principle in generative modeling, critically influencing both model architecture and broader applications.\n\nThe paper was submitted on 23 May 2025 with subsequent revisions on 28 Jul 2025 and 12 Jan 2026. You can access it directly at the arXiv link: https://arxiv.org/abs/2505.18227"
    ],
    "durationSeconds": 5.576002039000014
  },
  "sourceToolAssistantUUID": "c910285d-7389-411d-9d2d-d58c8df78b26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b526ba35-5e07-4df2-8b62-15bd29b5d0b4",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Tool call

_source line 44 · 2026-05-14T06:58:41.944Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PeTCqY6Dn3ZgbNREpN4Yzu`</summary>

```json
{
  "query": "adaptive token selection action-conditioned visual robot policy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b526ba35-5e07-4df2-8b62-15bd29b5d0b4",
  "isSidechain": false,
  "requestId": "req_011Cb22Zc4tiU7mpFh4Zgqem",
  "type": "assistant",
  "uuid": "198fe657-d917-4bfc-8a64-7c25181c21c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nwMYKaQdfD4zub4N4Fmmf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 47152,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 47152,
          "cache_creation_input_tokens": 945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 945
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

_source line 45 · 2026-05-14T06:58:48.656Z_

<details><summary>↩ Tool result · `toolu_01PeTCqY6Dn3ZgbNREpN4Yzu`</summary>

```text
Web search results for query: "adaptive token selection action-conditioned visual robot policy 2026"

Links: [{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Unified Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=PklMD8PwUy"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"},{"title":"ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/act-policy-explained"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Guiding Action Diffusion Policies in Robots via Motion Tokens | by Ville Kuosmanen | Apr, 2026 | Medium","url":"https://villekuosmanen.medium.com/guiding-action-diffusion-policies-in-robots-via-motion-tokens-f8a5fe4ef8b1"},{"title":"Unlocking robotics with action tokenization | by Dave Davies | Online Inference | Mar, 2026 | Medium","url":"https://medium.com/online-inference/unlocking-robotics-with-action-tokenization-15e4160c1aee"}]

I found several relevant results about vision-language-action (VLA) models and robot policies from 2026. Here's what the search revealed:

## Overview of Current Research

There are 164 Vision-Language-Action (VLA) model submissions at ICLR 2026, with trends in discrete diffusion VLAs, reasoning models, and benchmarks like LIBERO, CALVIN, and SIMPLER.

## Action Tokenization and Token Selection

The concept of adaptive token selection relates closely to action tokenization methodologies being developed for VLA policies:

Action tokenization is the mapping from continuous robot control trajectories to discrete token sequences that can be modeled alongside words and visual tokens. In pi0FAST and related VLA policies, a single autoregressive Transformer takes language prompts and visual tokens as input, then predicts action tokens, which are later detokenized back into low-level controls.

OAT (Optimal Action Tokenizer) is a learned tokenizer with high compression, total decodability, and left-to-right causal token order aligned with autoregressive generation. It uses a Transformer with register tokens and finite scalar quantization, and supports prefix-based detokenization where decoding the first few tokens yields a coarse action, which can be refined by adding more tokens to enable dynamic tradeoffs between latency and precision at inference time.

## Motion Token Conditioning

Motion tokens can extend diffusion policy inputs to include directional information (x, y, z, roll, pitch, yaw, gripper). Motion token guidance aims to bias action retrieval not to generate novel motions, but to make it more likely that the retrieved action chunk is one of the good candidates already present in the training distribution.

The field appears to be actively exploring how to selectively activate or weight different tokens based on task requirements and observational context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "198fe657-d917-4bfc-8a64-7c25181c21c9",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "e3210929-e145-42a8-a656-ecfed198f015",
  "toolUseResult": {
    "query": "adaptive token selection action-conditioned visual robot policy 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BPdK3Kau9U8zbT5Vs7DW3D",
        "content": [
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          },
          {
            "title": "Unified Vision-Language-Action Model | OpenReview",
            "url": "https://openreview.net/forum?id=PklMD8PwUy"
          },
          {
            "title": "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://www.pi.website/download/fast.pdf"
          },
          {
            "title": "ACT Policy Explained (2026): Action Chunking with Transformers | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/blog/act-policy-explained"
          },
          {
            "title": "Vision-Language-Action Models and the Search for a Generalist Robot Policy",
            "url": "https://itcanthink.substack.com/p/vision-language-action-models-and"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "Guiding Action Diffusion Policies in Robots via Motion Tokens | by Ville Kuosmanen | Apr, 2026 | Medium",
            "url": "https://villekuosmanen.medium.com/guiding-action-diffusion-policies-in-robots-via-motion-tokens-f8a5fe4ef8b1"
          },
          {
            "title": "Unlocking robotics with action tokenization | by Dave Davies | Online Inference | Mar, 2026 | Medium",
            "url": "https://medium.com/online-inference/unlocking-robotics-with-action-tokenization-15e4160c1aee"
          }
        ]
      },
      "I found several relevant results about vision-language-action (VLA) models and robot policies from 2026. Here's what the search revealed:\n\n## Overview of Current Research\n\nThere are 164 Vision-Language-Action (VLA) model submissions at ICLR 2026, with trends in discrete diffusion VLAs, reasoning models, and benchmarks like LIBERO, CALVIN, and SIMPLER.\n\n## Action Tokenization and Token Selection\n\nThe concept of adaptive token selection relates closely to action tokenization methodologies being developed for VLA policies:\n\nAction tokenization is the mapping from continuous robot control trajectories to discrete token sequences that can be modeled alongside words and visual tokens. In pi0FAST and related VLA policies, a single autoregressive Transformer takes language prompts and visual tokens as input, then predicts action tokens, which are later detokenized back into low-level controls.\n\nOAT (Optimal Action Tokenizer) is a learned tokenizer with high compression, total decodability, and left-to-right causal token order aligned with autoregressive generation. It uses a Transformer with register tokens and finite scalar quantization, and supports prefix-based detokenization where decoding the first few tokens yields a coarse action, which can be refined by adding more tokens to enable dynamic tradeoffs between latency and precision at inference time.\n\n## Motion Token Conditioning\n\nMotion tokens can extend diffusion policy inputs to include directional information (x, y, z, roll, pitch, yaw, gripper). Motion token guidance aims to bias action retrieval not to generate novel motions, but to make it more likely that the retrieved action chunk is one of the good candidates already present in the training distribution.\n\nThe field appears to be actively exploring how to selectively activate or weight different tokens based on task requirements and observational context."
    ],
    "durationSeconds": 6.708000804999989
  },
  "sourceToolAssistantUUID": "198fe657-d917-4bfc-8a64-7c25181c21c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T06:58:55.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Z6F98GBFsBesfcYRUTBmb`</summary>

```json
{
  "query": "AVA-VLA active visual attention VLA token reweighting LIBERO-Plus 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3210929-e145-42a8-a656-ecfed198f015",
  "isSidechain": false,
  "requestId": "req_011Cb22aHEb3HBYJYBWibhRY",
  "type": "assistant",
  "uuid": "d84d14f5-c75a-4817-9624-fce123479355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7sd5zCP4Uc7VjEyRvpZ9p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 48097,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 48097,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1024
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

_source line 47 · 2026-05-14T06:59:02.495Z_

<details><summary>↩ Tool result · `toolu_013Z6F98GBFsBesfcYRUTBmb`</summary>

```text
Web search results for query: "AVA-VLA active visual attention VLA token reweighting LIBERO-Plus 2025"

Links: [{"title":"[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/abs/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251118960X/abstract"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://www.researchgate.net/publication/397934001_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.18960v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"}]

Based on the search results, here's what I found about AVA-VLA and its relationship to token reweighting and LIBERO-Plus:

## AVA-VLA Overview

AVA-VLA reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and introduces Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history.

## Key Technical Approach

The AVA module uses the recurrent state to compute soft weights to actively process task-relevant visual tokens based on its historical context. The framework maintains strong performance even with 50-70% visual token pruning, suggesting that the attention mechanism effectively identifies and retains the most informative visual elements.

## Performance on Benchmarks

AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. The framework exhibits improved robustness across various environmental perturbations in the LIBERO+ benchmark, showing particular resilience to lighting and layout changes that typically challenge vision-based robotic systems.

The research was published on arXiv in November 2025 and appears to be highly relevant to the LIBERO-Plus benchmark for evaluating robustness of vision-language-action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d84d14f5-c75a-4817-9624-fce123479355",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "69f114b4-acd5-4b83-adbe-946cb517f9dc",
  "toolUseResult": {
    "query": "AVA-VLA active visual attention VLA token reweighting LIBERO-Plus 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KkudoszKL9KTRLzLtuEU1N",
        "content": [
          {
            "title": "[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/abs/2511.18960"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/html/2511.18960"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251118960X/abstract"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://www.researchgate.net/publication/397934001_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2511.18960v1"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching",
            "url": "https://arxiv.org/html/2502.02175v2"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          }
        ]
      },
      "Based on the search results, here's what I found about AVA-VLA and its relationship to token reweighting and LIBERO-Plus:\n\n## AVA-VLA Overview\n\nAVA-VLA reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and introduces Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history.\n\n## Key Technical Approach\n\nThe AVA module uses the recurrent state to compute soft weights to actively process task-relevant visual tokens based on its historical context. The framework maintains strong performance even with 50-70% visual token pruning, suggesting that the attention mechanism effectively identifies and retains the most informative visual elements.\n\n## Performance on Benchmarks\n\nAVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. The framework exhibits improved robustness across various environmental perturbations in the LIBERO+ benchmark, showing particular resilience to lighting and layout changes that typically challenge vision-based robotic systems.\n\nThe research was published on arXiv in November 2025 and appears to be highly relevant to the LIBERO-Plus benchmark for evaluating robustness of vision-language-action models."
    ],
    "durationSeconds": 6.917583161999995
  },
  "sourceToolAssistantUUID": "d84d14f5-c75a-4817-9624-fce123479355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T06:59:06.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DmDAhj8qkuyTnn8asAYgG3`</summary>

```json
{
  "query": "AVA-VLA LIBERO-Plus score performance results percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69f114b4-acd5-4b83-adbe-946cb517f9dc",
  "isSidechain": false,
  "requestId": "req_011Cb22bJQK5wAyvECGokKAS",
  "type": "assistant",
  "uuid": "94d83189-5da7-4e40-b935-9b5919769671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQm4HbD18tRo5Z1kP8WrUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 969,
      "cache_read_input_tokens": 49121,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 49121,
          "cache_creation_input_tokens": 969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 969
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

_source line 49 · 2026-05-14T06:59:11.604Z_

<details><summary>↩ Tool result · `toolu_01DmDAhj8qkuyTnn8asAYgG3`</summary>

```text
Web search results for query: "AVA-VLA LIBERO-Plus score performance results percentage"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960"},{"title":"Understanding Your Test Results","url":"https://www.va.nesinc.com/PageView.aspx?f=GEN_UnderstandingYourTestResults.html"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Colorado Avalanche News, Scores and Stats 2025-26 - CBS Sports","url":"https://www.cbssports.com/nhl/teams/COL/colorado-avalanche/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, here is the information about AVA-VLA performance on LIBERO-Plus:

## AVA-VLA Performance Results

AVA-VLA achieved an average score of 74.7 on LIBERO-Plus, according to the benchmark's leaderboard.

The AVA-VLA framework achieved state-of-the-art overall performance in both single-task and multi-task settings, and consistently achieved the best performance on the most challenging LIBERO-Long task suite.

The research demonstrates that the model shows robustness to visual token pruning, with only negligible performance drops after pruning, and at pruning ratios of 50%, 60%, and 70%, the proposed method continues to outperform baseline models and maintains performance comparable to state-of-the-art baselines.

The AVA-VLA model improves upon previous approaches like OpenVLA-OFT by incorporating an Active Visual Attention module that helps the model focus on task-relevant visual information while suppressing irrelevant content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94d83189-5da7-4e40-b935-9b5919769671",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "e145b03a-6d58-4de5-ba5b-844109bfaae8",
  "toolUseResult": {
    "query": "AVA-VLA LIBERO-Plus score performance results percentage",
    "results": [
      {
        "tool_use_id": "srvtoolu_014tqBHGY4jHRdWX6mBVrMhm",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/html/2511.18960"
          },
          {
            "title": "Understanding Your Test Results",
            "url": "https://www.va.nesinc.com/PageView.aspx?f=GEN_UnderstandingYourTestResults.html"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "Sylvest/LIBERO-plus · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Colorado Avalanche News, Scores and Stats 2025-26 - CBS Sports",
            "url": "https://www.cbssports.com/nhl/teams/COL/colorado-avalanche/"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          }
        ]
      },
      "Based on the search results, here is the information about AVA-VLA performance on LIBERO-Plus:\n\n## AVA-VLA Performance Results\n\nAVA-VLA achieved an average score of 74.7 on LIBERO-Plus, according to the benchmark's leaderboard.\n\nThe AVA-VLA framework achieved state-of-the-art overall performance in both single-task and multi-task settings, and consistently achieved the best performance on the most challenging LIBERO-Long task suite.\n\nThe research demonstrates that the model shows robustness to visual token pruning, with only negligible performance drops after pruning, and at pruning ratios of 50%, 60%, and 70%, the proposed method continues to outperform baseline models and maintains performance comparable to state-of-the-art baselines.\n\nThe AVA-VLA model improves upon previous approaches like OpenVLA-OFT by incorporating an Active Visual Attention module that helps the model focus on task-relevant visual information while suppressing irrelevant content."
    ],
    "durationSeconds": 5.597079503000016
  },
  "sourceToolAssistantUUID": "94d83189-5da7-4e40-b935-9b5919769671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-14T06:59:19.208Z_

Now let me check for the most recent VLA robustness methods and any concurrent work that might overlap with ACIBS.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e145b03a-6d58-4de5-ba5b-844109bfaae8",
  "isSidechain": false,
  "requestId": "req_011Cb22byLNX5mPCrSUsE3Ek",
  "type": "assistant",
  "uuid": "2e85816a-46a1-4f65-b053-3133db224158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eExG3bsxMrCcxEoyctAoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 50090,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 50090,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 51 · 2026-05-14T06:59:19.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UbQekr3NYr1YBScJ1B9wrF`</summary>

```json
{
  "query": "VLA robustness visual perturbation method 2026 arXiv new approach"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e85816a-46a1-4f65-b053-3133db224158",
  "isSidechain": false,
  "requestId": "req_011Cb22byLNX5mPCrSUsE3Ek",
  "type": "assistant",
  "uuid": "ac46f3d8-0e58-4201-b7d1-8dc44baf93a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eExG3bsxMrCcxEoyctAoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 50090,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 50090,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 52 · 2026-05-14T06:59:26.614Z_

<details><summary>↩ Tool result · `toolu_01UbQekr3NYr1YBScJ1B9wrF`</summary>

```text
Web search results for query: "VLA robustness visual perturbation method 2026 arXiv new approach"

Links: [{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v3"},{"title":"[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037v4"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/abs/2602.01158"}]

Based on the search results, here are the key findings about VLA (Vision-Language-Action) robustness and visual perturbation methods from 2026 arXiv papers:

## Main Research Papers

### RobustVLA - Multi-Modal Robustness Approach
RobustVLA is proposed to address perturbations in VLA inputs and outputs. For output robustness, it performs offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. 

The method frames the problem as a multi-armed bandit and employs the upper confidence bound (UCB) algorithm to select the most harmful perturbation for training. On LIBERO benchmark, RobustVLA achieves absolute gains of 12.6% on the π₀ backbone and 10.4% on the OpenVLA backbone across 17 perturbations, being 50.6x faster than visual-robust BYOVLA.

### LIBERO-Plus - Comprehensive Robustness Analysis
Across all perturbation factors, current VLAs exhibit brittle generalization, with performance degrading significantly under various input perturbations, particularly with changes in camera viewpoint and robot initial state.

### VLA-IAP - Visual Token Pruning Approach
VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

### CRT - Corruption Restoration Method
The Corruption Restoration Transformer (CRT) is a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances, leveraging an adversarial training objective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac46f3d8-0e58-4201-b7d1-8dc44baf93a0",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "6e38953c-276c-41ee-88e6-6d30a5d13845",
  "toolUseResult": {
    "query": "VLA robustness visual perturbation method 2026 arXiv new approach",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KfL2n9weSN7fGwA9VZr8iC",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 ON ROBUSTNESS",
            "url": "https://arxiv.org/pdf/2510.00037v4"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/html/2510.00037"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v3"
          },
          {
            "title": "[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/abs/2510.00037"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.18107"
          },
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902"
          },
          {
            "title": "[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/abs/2510.00037v4"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs",
            "url": "https://arxiv.org/abs/2602.01158"
          }
        ]
      },
      "Based on the search results, here are the key findings about VLA (Vision-Language-Action) robustness and visual perturbation methods from 2026 arXiv papers:\n\n## Main Research Papers\n\n### RobustVLA - Multi-Modal Robustness Approach\nRobustVLA is proposed to address perturbations in VLA inputs and outputs. For output robustness, it performs offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. \n\nThe method frames the problem as a multi-armed bandit and employs the upper confidence bound (UCB) algorithm to select the most harmful perturbation for training. On LIBERO benchmark, RobustVLA achieves absolute gains of 12.6% on the π₀ backbone and 10.4% on the OpenVLA backbone across 17 perturbations, being 50.6x faster than visual-robust BYOVLA.\n\n### LIBERO-Plus - Comprehensive Robustness Analysis\nAcross all perturbation factors, current VLAs exhibit brittle generalization, with performance degrading significantly under various input perturbations, particularly with changes in camera viewpoint and robot initial state.\n\n### VLA-IAP - Visual Token Pruning Approach\nVLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.\n\n### CRT - Corruption Restoration Method\nThe Corruption Restoration Transformer (CRT) is a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances, leveraging an adversarial training objective."
    ],
    "durationSeconds": 7.13766979700001
  },
  "sourceToolAssistantUUID": "ac46f3d8-0e58-4201-b7d1-8dc44baf93a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53 · 2026-05-14T06:59:26.617Z_

```json
{
  "parentUuid": "6e38953c-276c-41ee-88e6-6d30a5d13845",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6558d04d-f7a9-4040-8fab-f66e3ed162fa",
  "timestamp": "2026-05-14T06:59:26.617Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6558d04d-f7a9-4040-8fab-f66e3ed162fa",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Tool call

_source line 56 · 2026-05-14T06:59:29.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KjNt7PrzEerHPNRH4usDc8`</summary>

```json
{
  "query": "\"test-time perturbation learning\" VLA delayed feedback 2026 arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6558d04d-f7a9-4040-8fab-f66e3ed162fa",
  "isSidechain": false,
  "requestId": "req_011Cb22d5VypvhZhGotVc3Yh",
  "type": "assistant",
  "uuid": "0b62812c-977a-4220-bde5-3e0563ba13d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWFzLBugrimHiubSuqnQZr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 50918,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 50918,
          "cache_creation_input_tokens": 1100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1100
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

_source line 57 · 2026-05-14T06:59:37.324Z_

<details><summary>↩ Tool result · `toolu_01KjNt7PrzEerHPNRH4usDc8`</summary>

```text
Web search results for query: ""test-time perturbation learning" VLA delayed feedback 2026 arXiv 2604"

Links: [{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning","url":"https://arxiv.org/html/2602.07845v1"},{"title":"Test-Time Learning for Large Language Models","url":"https://arxiv.org/html/2505.20633v1"},{"title":"EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.14666v1"},{"title":"[2511.04847] Test-Time Adaptation for LLM Agents via Environment Interaction","url":"https://arxiv.org/abs/2511.04847"}]

I found the paper you're looking for! Here are the key details:

## Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models

The paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.

**Main Problem:**
Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. This brittleness is attributed to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns.

**Key Components:**
PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue.

**Results:**
Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation.

**Paper Details:**
- arXiv ID: 2604.18107
- Posted: April 20, 2026
- Authors: Zehua Zang and 6 other authors


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b62812c-977a-4220-bde5-3e0563ba13d6",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "a5b623f6-b4c2-4074-985a-dd3ae859865d",
  "toolUseResult": {
    "query": "\"test-time perturbation learning\" VLA delayed feedback 2026 arXiv 2604",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KXj6VP5LeWcZYbPU7c3oYN",
        "content": [
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.18107"
          },
          {
            "title": "[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.18107"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for",
            "url": "https://arxiv.org/pdf/2604.18107"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://arxiv.org/html/2505.19789v4"
          },
          {
            "title": "GitHub - Ed1sonChen/DailyArxiv · GitHub",
            "url": "https://github.com/Ed1sonChen/DailyArxiv"
          },
          {
            "title": "Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning",
            "url": "https://arxiv.org/html/2602.07845v1"
          },
          {
            "title": "Test-Time Learning for Large Language Models",
            "url": "https://arxiv.org/html/2505.20633v1"
          },
          {
            "title": "EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2512.14666v1"
          },
          {
            "title": "[2511.04847] Test-Time Adaptation for LLM Agents via Environment Interaction",
            "url": "https://arxiv.org/abs/2511.04847"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n## Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models\n\nThe paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.\n\n**Main Problem:**\nVision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. This brittleness is attributed to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns.\n\n**Key Components:**\nPDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue.\n\n**Results:**\nExperiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation.\n\n**Paper Details:**\n- arXiv ID: 2604.18107\n- Posted: April 20, 2026\n- Authors: Zehua Zang and 6 other authors"
    ],
    "durationSeconds": 7.749372604999983
  },
  "sourceToolAssistantUUID": "0b62812c-977a-4220-bde5-3e0563ba13d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-14T06:59:40.727Z_

This is a potentially relevant competitor — test-time perturbation learning for VLA robustness. Let me check more details and search for additional concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b623f6-b4c2-4074-985a-dd3ae859865d",
  "isSidechain": false,
  "requestId": "req_011Cb22dsK2yCngEab2Zzf7g",
  "type": "assistant",
  "uuid": "01acd210-54ba-4c86-b4ac-b94e5e366c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AipJNiTArQEyo31QTYpQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 52018,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 52018,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 59 · 2026-05-14T06:59:41.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JcYcXAH6458Cufw5ha1ZZN`</summary>

```json
{
  "query": "visual token augmentation latent space robustness representation learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01acd210-54ba-4c86-b4ac-b94e5e366c42",
  "isSidechain": false,
  "requestId": "req_011Cb22dsK2yCngEab2Zzf7g",
  "type": "assistant",
  "uuid": "6169af0b-1ce6-42bd-98d8-a7b11360d2bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AipJNiTArQEyo31QTYpQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 52018,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 52018,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 60 · 2026-05-14T06:59:49.724Z_

<details><summary>↩ Tool result · `toolu_01JcYcXAH6458Cufw5ha1ZZN`</summary>

```text
Web search results for query: "visual token augmentation latent space robustness representation learning 2025 2026"

Links: [{"title":"Latent Visual Tokens","url":"https://www.emergentmind.com/topics/latent-visual-tokens"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"Vision Encoders in Vision-Language Models: A Survey Han Xiao Jina AI by Elastic","url":"https://jina.ai/vision-encoder-survey.pdf"},{"title":"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.04678v1"},{"title":"GitHub - ChaofanTao/Autoregressive-Models-in-Vision-Survey: [TMLR 2025🔥] A survey for the autoregressive models in vision.","url":"https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v3"},{"title":"GitHub - 52CV/WACV-2025-Papers · GitHub","url":"https://github.com/52CV/WACV-2025-Papers"},{"title":"GitHub - 52CV/CVPR-2025-Papers · GitHub","url":"https://github.com/52CV/CVPR-2025-Papers"},{"title":"CVPR 2025 Accepted Papers","url":"https://cvpr.thecvf.com/Conferences/2025/AcceptedPapers"},{"title":"GitHub - YU-deep/Awesome-Latent-Space: A paper list of Awesome Latent Space. · GitHub","url":"https://github.com/YU-deep/Awesome-Latent-Space"}]

I found relevant search results on visual token augmentation, latent space robustness, and representation learning from 2025-2026. Here's a summary of the key findings:

## Recent Advances in Visual Tokenization and Latent Space (2025-2026)

### Tokenization Methods and Innovations

Quantization-based tokenizers like VQ-VAE and VQGAN derive latent tokens via a learned codebook, with recent innovations such as WeTok (August 2025) introducing group-wise lookup-free quantization and generative decoders to support scaling and improved reconstruction at high compression.

Binary and compact tokenizers like Instella-T2I (June 2025) employ 1D binary vectors, significantly reducing sequence length while maintaining resolution.

### Latent Space Structuring and Robustness

Structuring the latent space, either via PCA-like ordering or spectral decoupling and denoising-aligned objectives, improves interpretability, robustness, and generative performance.

Visual Gaussian Quantization (VGQ, August 2025) introduces 2D Gaussian-parameterized tokens for spatial and structural augmentation.

### Multimodal Applications and Vision-Language Integration

Unified frameworks like AToken and Ming-UniVision tokenize images, videos, and 3D content into a modality-agnostic latent space, powering both generation and high-level understanding.

In vision-language models, input images are divided into patches and processed by vision encoders that convert pixels into visual tokens, with projection modules mapping these tokens into the language model's embedding space.

### Token Reduction and Robustness

Future methods should preserve spatial diversity by enforcing structural uniformity in retained tokens to improve robustness on visual tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6169af0b-1ce6-42bd-98d8-a7b11360d2bb",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "c45b17d8-4cfe-41ce-ba05-ae4fffb99f74",
  "toolUseResult": {
    "query": "visual token augmentation latent space robustness representation learning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0179spsGaq6yq8p5xoj56Bgt",
        "content": [
          {
            "title": "Latent Visual Tokens",
            "url": "https://www.emergentmind.com/topics/latent-visual-tokens"
          },
          {
            "title": "The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview",
            "url": "https://openreview.net/forum?id=7BKcLeHQsm"
          },
          {
            "title": "Vision Encoders in Vision-Language Models: A Survey Han Xiao Jina AI by Elastic",
            "url": "https://jina.ai/vision-encoder-survey.pdf"
          },
          {
            "title": "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2605.04678v1"
          },
          {
            "title": "GitHub - ChaofanTao/Autoregressive-Models-in-Vision-Survey: [TMLR 2025🔥] A survey for the autoregressive models in vision.",
            "url": "https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality",
            "url": "https://arxiv.org/html/2505.18227v3"
          },
          {
            "title": "GitHub - 52CV/WACV-2025-Papers · GitHub",
            "url": "https://github.com/52CV/WACV-2025-Papers"
          },
          {
            "title": "GitHub - 52CV/CVPR-2025-Papers · GitHub",
            "url": "https://github.com/52CV/CVPR-2025-Papers"
          },
          {
            "title": "CVPR 2025 Accepted Papers",
            "url": "https://cvpr.thecvf.com/Conferences/2025/AcceptedPapers"
          },
          {
            "title": "GitHub - YU-deep/Awesome-Latent-Space: A paper list of Awesome Latent Space. · GitHub",
            "url": "https://github.com/YU-deep/Awesome-Latent-Space"
          }
        ]
      },
      "I found relevant search results on visual token augmentation, latent space robustness, and representation learning from 2025-2026. Here's a summary of the key findings:\n\n## Recent Advances in Visual Tokenization and Latent Space (2025-2026)\n\n### Tokenization Methods and Innovations\n\nQuantization-based tokenizers like VQ-VAE and VQGAN derive latent tokens via a learned codebook, with recent innovations such as WeTok (August 2025) introducing group-wise lookup-free quantization and generative decoders to support scaling and improved reconstruction at high compression.\n\nBinary and compact tokenizers like Instella-T2I (June 2025) employ 1D binary vectors, significantly reducing sequence length while maintaining resolution.\n\n### Latent Space Structuring and Robustness\n\nStructuring the latent space, either via PCA-like ordering or spectral decoupling and denoising-aligned objectives, improves interpretability, robustness, and generative performance.\n\nVisual Gaussian Quantization (VGQ, August 2025) introduces 2D Gaussian-parameterized tokens for spatial and structural augmentation.\n\n### Multimodal Applications and Vision-Language Integration\n\nUnified frameworks like AToken and Ming-UniVision tokenize images, videos, and 3D content into a modality-agnostic latent space, powering both generation and high-level understanding.\n\nIn vision-language models, input images are divided into patches and processed by vision encoders that convert pixels into visual tokens, with projection modules mapping these tokens into the language model's embedding space.\n\n### Token Reduction and Robustness\n\nFuture methods should preserve spatial diversity by enforcing structural uniformity in retained tokens to improve robustness on visual tasks."
    ],
    "durationSeconds": 8.582146764000004
  },
  "sourceToolAssistantUUID": "6169af0b-1ce6-42bd-98d8-a7b11360d2bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T06:59:52.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UtB2LM9GEaV34zW55yex8b`</summary>

```json
{
  "query": "DRIBO multi-view information bottleneck robust reinforcement learning ICML 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c45b17d8-4cfe-41ce-ba05-ae4fffb99f74",
  "isSidechain": false,
  "requestId": "req_011Cb22enbJJLGcH5NoXn8F5",
  "type": "assistant",
  "uuid": "bae380e9-868c-45ce-ae47-5809bbb355f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cARSB3ooK9CGdy1SrjFL3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 52913,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 52913,
          "cache_creation_input_tokens": 1047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1047
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

_source line 62 · 2026-05-14T06:59:58.300Z_

<details><summary>↩ Tool result · `toolu_01UtB2LM9GEaV34zW55yex8b`</summary>

```text
Web search results for query: "DRIBO multi-view information bottleneck robust reinforcement learning ICML 2022"

Links: [{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://proceedings.mlr.press/v162/fan22b/fan22b.pdf"},{"title":"[2102.13268] DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://arxiv.org/abs/2102.13268"},{"title":"ICML Poster DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://icml.cc/virtual/2022/poster/16441"},{"title":"GitHub - JmfanBU/DRIBO: DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://github.com/JmfanBU/DRIBO"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=Py8WbvKH_wv"},{"title":"dblp: Jiameng Fan","url":"https://dblp.org/pid/196/7836.html"},{"title":"Track: MISC: Representation Learning/Causality","url":"https://icml.cc/virtual/2022/session/20088"},{"title":"Robust Deep Reinforcement Learning via MultiView Infomration BOttleneck... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Robust-Deep-Reinforcement-Learning-via-MultiView-Infomration-BOttleneck-DRIBO_fig1_349682874"},{"title":"Home | jiamengf","url":"https://www.jiamengf.com"},{"title":"(PDF) Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://www.researchgate.net/publication/349682874_Robust_Deep_Reinforcement_Learning_via_Multi-View_Information_Bottleneck"}]

I found comprehensive information about DRIBO. Here are the key findings:

## Overview

DRIBO addresses the problem that deep reinforcement learning agents are often sensitive to visual changes unseen during training, by leveraging the sequential nature of RL to learn robust representations that encode only task-relevant information using a novel contrastive version of the Multi-View Information Bottleneck objective for temporal data.

## Technical Approach

DRIBO learns robust representations for RL agents by incorporating temporal information in the RL problems and multi-view observations. The approach trains RL agents from pixels with this auxiliary objective to learn robust representations that can compress away task-irrelevant information and are predictive of task-relevant dynamics.

## Performance

The approach achieves state-of-the-art performance on a diverse set of visual control tasks in the DeepMind Control Suite when the background is replaced with natural videos. Additionally, the approach outperforms well-established baselines for generalization to unseen environments on the Procgen benchmark.

## Publication

DRIBO was published at ICML 2022 with page range 6074-6102. The authors are Jiameng Fan and Wenchao Li.

## Availability

The code is open-sourced and available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bae380e9-868c-45ce-ae47-5809bbb355f8",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "3dec4bb5-6db6-4c99-9598-04e2c9c3b9f5",
  "toolUseResult": {
    "query": "DRIBO multi-view information bottleneck robust reinforcement learning ICML 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_015CWSajyky3QLYAdAaaMn4e",
        "content": [
          {
            "title": "DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck",
            "url": "https://proceedings.mlr.press/v162/fan22b/fan22b.pdf"
          },
          {
            "title": "[2102.13268] DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck",
            "url": "https://arxiv.org/abs/2102.13268"
          },
          {
            "title": "ICML Poster DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck",
            "url": "https://icml.cc/virtual/2022/poster/16441"
          },
          {
            "title": "GitHub - JmfanBU/DRIBO: DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck",
            "url": "https://github.com/JmfanBU/DRIBO"
          },
          {
            "title": "DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck | OpenReview",
            "url": "https://openreview.net/forum?id=Py8WbvKH_wv"
          },
          {
            "title": "dblp: Jiameng Fan",
            "url": "https://dblp.org/pid/196/7836.html"
          },
          {
            "title": "Track: MISC: Representation Learning/Causality",
            "url": "https://icml.cc/virtual/2022/session/20088"
          },
          {
            "title": "Robust Deep Reinforcement Learning via MultiView Infomration BOttleneck... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Robust-Deep-Reinforcement-Learning-via-MultiView-Infomration-BOttleneck-DRIBO_fig1_349682874"
          },
          {
            "title": "Home | jiamengf",
            "url": "https://www.jiamengf.com"
          },
          {
            "title": "(PDF) Robust Deep Reinforcement Learning via Multi-View Information Bottleneck",
            "url": "https://www.researchgate.net/publication/349682874_Robust_Deep_Reinforcement_Learning_via_Multi-View_Information_Bottleneck"
          }
        ]
      },
      "I found comprehensive information about DRIBO. Here are the key findings:\n\n## Overview\n\nDRIBO addresses the problem that deep reinforcement learning agents are often sensitive to visual changes unseen during training, by leveraging the sequential nature of RL to learn robust representations that encode only task-relevant information using a novel contrastive version of the Multi-View Information Bottleneck objective for temporal data.\n\n## Technical Approach\n\nDRIBO learns robust representations for RL agents by incorporating temporal information in the RL problems and multi-view observations. The approach trains RL agents from pixels with this auxiliary objective to learn robust representations that can compress away task-irrelevant information and are predictive of task-relevant dynamics.\n\n## Performance\n\nThe approach achieves state-of-the-art performance on a diverse set of visual control tasks in the DeepMind Control Suite when the background is replaced with natural videos. Additionally, the approach outperforms well-established baselines for generalization to unseen environments on the Procgen benchmark.\n\n## Publication\n\nDRIBO was published at ICML 2022 with page range 6074-6102. The authors are Jiameng Fan and Wenchao Li.\n\n## Availability\n\nThe code is open-sourced and available on GitHub."
    ],
    "durationSeconds": 5.846391391000012
  },
  "sourceToolAssistantUUID": "bae380e9-868c-45ce-ae47-5809bbb355f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-14T07:00:01.531Z_

Now let me look for any very recent work (last 2-3 months) that might directly compete with ACIBS.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dec4bb5-6db6-4c99-9598-04e2c9c3b9f5",
  "isSidechain": false,
  "requestId": "req_011Cb22fR9UxN6riq6diaX5r",
  "type": "assistant",
  "uuid": "dce8ceca-b1e4-45f9-98a6-878597eb6dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kqmSaFZTwvFEKoC2Gz5qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 53960,
      "output_tokens": 103,
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
          "output_tokens": 103,
          "cache_read_input_tokens": 53960,
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

_source line 64 · 2026-05-14T07:00:02.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FTNfxUFiBeMMUCUbyegpyN`</summary>

```json
{
  "query": "VLA token surgery pruning robustness information bottleneck 2026 arXiv March April May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dce8ceca-b1e4-45f9-98a6-878597eb6dab",
  "isSidechain": false,
  "requestId": "req_011Cb22fR9UxN6riq6diaX5r",
  "type": "assistant",
  "uuid": "023a82d3-0417-4b11-b25a-4f42046b08dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kqmSaFZTwvFEKoC2Gz5qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 53960,
      "output_tokens": 103,
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
          "output_tokens": 103,
          "cache_read_input_tokens": 53960,
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

_source line 65 · 2026-05-14T07:00:10.212Z_

<details><summary>↩ Tool result · `toolu_01FTNfxUFiBeMMUCUbyegpyN`</summary>

```text
Web search results for query: "VLA token surgery pruning robustness information bottleneck 2026 arXiv March April May"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm","url":"https://arxiv.org/html/2512.02700"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2603.24941"}]

I found several relevant papers from arXiv in the March-May 2026 timeframe related to VLA token pruning, robustness, and information bottleneck. Here are the key results:

## Main Findings:

**VLA-IAP: Training-Free Visual Token Pruning** (March 24, 2026)
VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment, enabling a conservative-to-aggressive transition ensuring robustness during early uncertainty and efficiency once interaction is locked. The method achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark, and up to 1.54× speedup while maintaining performance comparable to the unpruned backbone.

**Robustness of Compressed Vision-Language Models** (January 29, 2026)
Existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck. The Compression-AliGnEd attack (CAGE) aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget.

**Token Ranking Consistency for VLA** (March 26, 2026)
TIES (Tau-guided Inter-layer Efficient Selection) adaptively balances attention magnitude with ranking consistency, ensuring robust token selection without requiring additional training, improving average success rates by 6% while reducing token usage by 78%.

These papers collectively address the information bottleneck challenge in VLA systems through various pruning approaches while maintaining robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "023a82d3-0417-4b11-b25a-4f42046b08dd",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "c570e113-e4ee-4ba0-aaf9-b5ce7598a39e",
  "toolUseResult": {
    "query": "VLA token surgery pruning robustness information bottleneck 2026 arXiv March April May",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gcs1ZuwMQtFMpds1vZDBGw",
        "content": [
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression",
            "url": "https://arxiv.org/abs/2601.21531"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/html/2506.12723v2"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950v1"
          },
          {
            "title": "[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991"
          },
          {
            "title": "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression",
            "url": "https://arxiv.org/html/2601.21531"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm",
            "url": "https://arxiv.org/html/2512.02700"
          },
          {
            "title": "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.24941"
          }
        ]
      },
      "I found several relevant papers from arXiv in the March-May 2026 timeframe related to VLA token pruning, robustness, and information bottleneck. Here are the key results:\n\n## Main Findings:\n\n**VLA-IAP: Training-Free Visual Token Pruning** (March 24, 2026)\nVLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment, enabling a conservative-to-aggressive transition ensuring robustness during early uncertainty and efficiency once interaction is locked. The method achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark, and up to 1.54× speedup while maintaining performance comparable to the unpruned backbone.\n\n**Robustness of Compressed Vision-Language Models** (January 29, 2026)\nExisting encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck. The Compression-AliGnEd attack (CAGE) aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget.\n\n**Token Ranking Consistency for VLA** (March 26, 2026)\nTIES (Tau-guided Inter-layer Efficient Selection) adaptively balances attention magnitude with ranking consistency, ensuring robust token selection without requiring additional training, improving average success rates by 6% while reducing token usage by 78%.\n\nThese papers collectively address the information bottleneck challenge in VLA systems through various pruning approaches while maintaining robustness."
    ],
    "durationSeconds": 8.065005365000019
  },
  "sourceToolAssistantUUID": "023a82d3-0417-4b11-b25a-4f42046b08dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "c570e113-e4ee-4ba0-aaf9-b5ce7598a39e",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Tool call

_source line 68 · 2026-05-14T07:00:16.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1fdq679Tj1K7mHtSAfa9u`</summary>

```json
{
  "query": "TIES \"tau-guided inter-layer efficient selection\" VLA token selection arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c570e113-e4ee-4ba0-aaf9-b5ce7598a39e",
  "isSidechain": false,
  "requestId": "req_011Cb22gHvSEng3953Td3q4Y",
  "type": "assistant",
  "uuid": "7fc21bfd-4c35-4e9a-a014-56d2bbc8f259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JofRYt85NbTYZsD4RYVwjy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 54863,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 54863,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
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

_source line 69 · 2026-05-14T07:00:23.645Z_

<details><summary>↩ Tool result · `toolu_01F1fdq679Tj1K7mHtSAfa9u`</summary>

```text
Web search results for query: "TIES "tau-guided inter-layer efficient selection" VLA token selection arXiv 2603"

Links: [{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2603.24941v1"},{"title":"[2603.24941] Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.24941"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for","url":"https://arxiv.org/pdf/2603.24941"},{"title":"TIDE: Every Layer Knows the Token Beneath the Context","url":"https://arxiv.org/html/2605.06216"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"Token Reduction via Local and Global Contexts Optimization for Efficient Video Large Language Models","url":"https://arxiv.org/html/2603.01400"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLN-Cache: Enabling Token Caching for VLN Models with Visual/Semantic Dynamics Awareness","url":"https://arxiv.org/html/2603.07080"}]

I found the paper! Here are the search results for TIES (Tau-guided Inter-layer Efficient Selection):

## Paper Summary

TIES (Tau-guided Inter-layer Efficient Selection) is a dynamic framework guided by inter-layer token ranking consistency for Vision-Language-Action (VLA) models. 

**Key Details:**

- **Problem**: VLA models excel in robotic manipulation but suffer from significant inference latency due to processing dense visual tokens, with existing token reduction methods predominantly relying on attention magnitude as a static selection, though high-attention tokens are task-dependent and can even degrade policy performance.

- **Method**: The framework uses Kendall's τ to measure inter-layer ranking consistency, enabling dynamic and content-aware token pruning.

- **Performance**: On the CogACT + SIMPLER benchmark, TIES improves average success rates by 6% while reducing token usage by 78%, and demonstrates strong generalization across diverse decoders and benchmarks.

- **Key Innovation**: By adaptively balancing attention magnitude with ranking consistency, TIES ensures robust token selection without requiring additional training.

The paper (arXiv 2603.24941) was submitted on March 26, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fc21bfd-4c35-4e9a-a014-56d2bbc8f259",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "61f3f189-2e81-4b7e-b594-0c8f6f3ba3c0",
  "toolUseResult": {
    "query": "TIES \"tau-guided inter-layer efficient selection\" VLA token selection arXiv 2603",
    "results": [
      {
        "tool_use_id": "srvtoolu_018bdzBMcnwWn4urE1KZiStm",
        "content": [
          {
            "title": "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.24941v1"
          },
          {
            "title": "[2603.24941] Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.24941"
          },
          {
            "title": "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for",
            "url": "https://arxiv.org/pdf/2603.24941"
          },
          {
            "title": "TIDE: Every Layer Knows the Token Beneath the Context",
            "url": "https://arxiv.org/html/2605.06216"
          },
          {
            "title": "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.25766"
          },
          {
            "title": "Token Reduction via Local and Global Contexts Optimization for Efficient Video Large Language Models",
            "url": "https://arxiv.org/html/2603.01400"
          },
          {
            "title": "[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.25766"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.10100v1"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "VLN-Cache: Enabling Token Caching for VLN Models with Visual/Semantic Dynamics Awareness",
            "url": "https://arxiv.org/html/2603.07080"
          }
        ]
      },
      "I found the paper! Here are the search results for TIES (Tau-guided Inter-layer Efficient Selection):\n\n## Paper Summary\n\nTIES (Tau-guided Inter-layer Efficient Selection) is a dynamic framework guided by inter-layer token ranking consistency for Vision-Language-Action (VLA) models. \n\n**Key Details:**\n\n- **Problem**: VLA models excel in robotic manipulation but suffer from significant inference latency due to processing dense visual tokens, with existing token reduction methods predominantly relying on attention magnitude as a static selection, though high-attention tokens are task-dependent and can even degrade policy performance.\n\n- **Method**: The framework uses Kendall's τ to measure inter-layer ranking consistency, enabling dynamic and content-aware token pruning.\n\n- **Performance**: On the CogACT + SIMPLER benchmark, TIES improves average success rates by 6% while reducing token usage by 78%, and demonstrates strong generalization across diverse decoders and benchmarks.\n\n- **Key Innovation**: By adaptively balancing attention magnitude with ranking consistency, TIES ensures robust token selection without requiring additional training.\n\nThe paper (arXiv 2603.24941) was submitted on March 26, 2026."
    ],
    "durationSeconds": 7.0698423349999935
  },
  "sourceToolAssistantUUID": "7fc21bfd-4c35-4e9a-a014-56d2bbc8f259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T07:00:26.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BECySVgo1QGbSuswxsfMrW`</summary>

```json
{
  "query": "\"PDF\" \"perturbation learning delayed feedback\" VLA LIBERO-Plus results score 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f3f189-2e81-4b7e-b594-0c8f6f3ba3c0",
  "isSidechain": false,
  "requestId": "req_011Cb22hHNUT1bFZVQE3hTEe",
  "type": "assistant",
  "uuid": "5f24ec87-67c3-4392-bcbe-e23ba77fd542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fGwyEZqzeNbh4Bv5sE79k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 55923,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 55923,
          "cache_creation_input_tokens": 882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 882
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

_source line 71 · 2026-05-14T07:00:34.212Z_

<details><summary>↩ Tool result · `toolu_01BECySVgo1QGbSuswxsfMrW`</summary>

```text
Web search results for query: ""PDF" "perturbation learning delayed feedback" VLA LIBERO-Plus results score 2026"

Links: [{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"}]

Based on the search results, I found information about both PDF (Perturbation learning with Delayed Feedback) and LIBERO-Plus:

## PDF (Perturbation Learning with Delayed Feedback)

PDF is a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model. It mitigates spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency.

### PDF Results on LIBERO

PDF attains the best average performance (0.77 SR, 2.5 mean rank), exceeding prior VLA variants and adaptation baselines. More specifically, it reaches 0.89 on Spatial (vs. 0.85 for reproduced OpenVLA) and 0.86 on Goal, slightly ahead of OCTO and OpenVLA. Gains are largest on Long-horizon tasks (0.59, +4.1 over the best baseline), indicating stronger sequential decision quality. Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success.

## LIBERO-Plus Benchmark

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise. Systematic analysis of ten state-of-the-art models reveals consistent brittleness beneath apparent competence, with performance dropping from 95% to below 30% under modest perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f24ec87-67c3-4392-bcbe-e23ba77fd542",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "161d480b-68a9-4446-bf9a-1f809cca8c11",
  "toolUseResult": {
    "query": "\"PDF\" \"perturbation learning delayed feedback\" VLA LIBERO-Plus results score 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HMKTVxmd6s5ctZTAotdb9E",
        "content": [
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.18107"
          },
          {
            "title": "[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.18107"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for",
            "url": "https://arxiv.org/pdf/2604.18107"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
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
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          }
        ]
      },
      "Based on the search results, I found information about both PDF (Perturbation learning with Delayed Feedback) and LIBERO-Plus:\n\n## PDF (Perturbation Learning with Delayed Feedback)\n\nPDF is a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model. It mitigates spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency.\n\n### PDF Results on LIBERO\n\nPDF attains the best average performance (0.77 SR, 2.5 mean rank), exceeding prior VLA variants and adaptation baselines. More specifically, it reaches 0.89 on Spatial (vs. 0.85 for reproduced OpenVLA) and 0.86 on Goal, slightly ahead of OCTO and OpenVLA. Gains are largest on Long-horizon tasks (0.59, +4.1 over the best baseline), indicating stronger sequential decision quality. Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success.\n\n## LIBERO-Plus Benchmark\n\nLIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise. Systematic analysis of ten state-of-the-art models reveals consistent brittleness beneath apparent competence, with performance dropping from 95% to below 30% under modest perturbations."
    ],
    "durationSeconds": 7.743473458999971
  },
  "sourceToolAssistantUUID": "5f24ec87-67c3-4392-bcbe-e23ba77fd542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-14T07:00:37.400Z_

Let me now fetch the FocusVLA paper directly to verify detailed claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "161d480b-68a9-4446-bf9a-1f809cca8c11",
  "isSidechain": false,
  "requestId": "req_011Cb22i4WLtcVcDbh6La1Hm",
  "type": "assistant",
  "uuid": "368f50ae-16c3-47d9-8fcd-057e3499e03f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ex44FYnWDmvXD7GC5zwbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 56805,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 56805,
          "cache_creation_input_tokens": 985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 985
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

_source line 73 · 2026-05-14T07:00:40.709Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019YKfATx8uWqQ5YDv5FokEK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.28740",
  "prompt": "Extract the following details: 1) Exact architecture (which vision encoder, which LLM backbone, total parameters), 2) Number of visual tokens before and after selection, 3) LIBERO benchmark results (exact numbers per suite), 4) Whether robustness or perturbation evaluation was conducted, 5) The token selection mechanism (cross-attention scores, learned scorer, etc.), 6) Training details (compute, datasets)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "368f50ae-16c3-47d9-8fcd-057e3499e03f",
  "isSidechain": false,
  "requestId": "req_011Cb22i4WLtcVcDbh6La1Hm",
  "type": "assistant",
  "uuid": "2c0cf615-daee-4851-b74b-7b1a57bd508d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ex44FYnWDmvXD7GC5zwbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 56805,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 56805,
          "cache_creation_input_tokens": 985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 985
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

_source line 74 · 2026-05-14T07:00:45.024Z_

<details><summary>↩ Tool result · `toolu_019YKfATx8uWqQ5YDv5FokEK`</summary>

```text
# FocusVLA Paper Details - Information Not Available

Based on the provided arXiv webpage content, I can only access the abstract and metadata. The specific technical details you're requesting are **not included** on this page:

1. **Exact Architecture**: Not specified in the abstract or visible page content
2. **Visual Token Numbers**: Not provided in accessible content
3. **LIBERO Benchmark Results**: Not detailed on this page
4. **Robustness Evaluation**: Not mentioned in the abstract
5. **Token Selection Mechanism**: The abstract mentions "Focus Attention, which dynamically selects task-relevant visual patches" but lacks implementation specifics
6. **Training Details**: Compute resources and datasets are not listed

## What Is Available:

The abstract indicates the paper addresses three bottlenecks in Vision-Language-Action models and proposes two main contributions: "Modality Cascaded Attention" and "Focus Attention." The paper contains "25 pages, 18 figures" and was submitted March 30, 2026.

**To obtain the detailed specifications you need**, you would need to access the full PDF or HTML versions of the paper via the links provided on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c0cf615-daee-4851-b74b-7b1a57bd508d",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "20e11493-0317-4cd6-9a08-63e998212381",
  "toolUseResult": {
    "bytes": 47542,
    "code": 200,
    "codeText": "OK",
    "result": "# FocusVLA Paper Details - Information Not Available\n\nBased on the provided arXiv webpage content, I can only access the abstract and metadata. The specific technical details you're requesting are **not included** on this page:\n\n1. **Exact Architecture**: Not specified in the abstract or visible page content\n2. **Visual Token Numbers**: Not provided in accessible content\n3. **LIBERO Benchmark Results**: Not detailed on this page\n4. **Robustness Evaluation**: Not mentioned in the abstract\n5. **Token Selection Mechanism**: The abstract mentions \"Focus Attention, which dynamically selects task-relevant visual patches\" but lacks implementation specifics\n6. **Training Details**: Compute resources and datasets are not listed\n\n## What Is Available:\n\nThe abstract indicates the paper addresses three bottlenecks in Vision-Language-Action models and proposes two main contributions: \"Modality Cascaded Attention\" and \"Focus Attention.\" The paper contains \"25 pages, 18 figures\" and was submitted March 30, 2026.\n\n**To obtain the detailed specifications you need**, you would need to access the full PDF or HTML versions of the paper via the links provided on the arXiv page.",
    "durationMs": 4311,
    "url": "https://arxiv.org/abs/2603.28740"
  },
  "sourceToolAssistantUUID": "2c0cf615-daee-4851-b74b-7b1a57bd508d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 75 · 2026-05-14T07:00:45.026Z_

```json
{
  "parentUuid": "20e11493-0317-4cd6-9a08-63e998212381",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "63a4eace-0a87-4c1f-ab4b-a1241e5d15f2",
  "timestamp": "2026-05-14T07:00:45.026Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 76 · 2026-05-14T07:00:49.759Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0134KSMyGd3W7TSBr141BXmG`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.28740",
  "prompt": "Extract: 1) Exact architecture (vision encoder name, LLM backbone name, total params, trainable params), 2) Number of raw visual tokens vs. selected tokens (e.g., 512 down to 256), 3) LIBERO benchmark results per suite (Object, Spatial, Goal, Long) with exact success rates, 4) Whether any robustness or perturbation evaluation was done (e.g., LIBERO-Plus, viewpoint changes, noise), 5) The token selection mechanism details (cross-attention, learned scorer, Gumbel-softmax, etc.), 6) How many GPUs and how long for training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63a4eace-0a87-4c1f-ab4b-a1241e5d15f2",
  "isSidechain": false,
  "requestId": "req_011Cb22irjSiBzuKpLsQ8fWD",
  "type": "assistant",
  "uuid": "2808fb3b-91aa-43db-a209-86e28f28636a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVYdmFLCvEaTqNmvGMCcCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 57790,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 57790,
          "cache_creation_input_tokens": 572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 572
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

_source line 77 · 2026-05-14T07:00:56.379Z_

<details><summary>↩ Tool result · `toolu_0134KSMyGd3W7TSBr141BXmG`</summary>

```text
# FocusVLA: Key Technical Details

## 1) Architecture Components

**Vision Encoder:** DINOv2 + SigLIP (combined as "DS") plus VGGT for implicit 3D information

**LLM Backbone:** "Qwen2.5-0.5B" serving as the core language model

**Parameters:** Total trainable parameters are 342.7M, split between VLM (103.6M) and policy (239.1M)

## 2) Visual Token Selection

The system reduces from **512 raw visual tokens to 256 selected tokens** using a patch-level focus mechanism based on cross-attention scores between action queries and vision keys, with "top-K scores retained for information propagation."

## 3) LIBERO Benchmark Results (Multi-weight setting)

- **Spatial:** 99.6%
- **Object:** 100.0%
- **Goal:** 98.8%
- **Long:** 96.2%
- **Average:** 98.7%

## 4) Robustness Evaluation

The paper includes real-world experiments with three task variations (background, spatial arrangement, target object changes) but does not explicitly report LIBERO-Plus or systematic perturbation studies. Failure cases show sensitivity to "initialization shifts and environmental variations."

## 5) Token Selection Mechanism

Selection uses "Softmax(TopK(...)) where only tokens with top-K scores are retained," based on attention scores from action latent to vision keys.

## 6) Training Resources

Training used **4 A100 GPUs** for LIBERO (100k steps, batch size 64) and **8 A100 GPUs** for RoboTwin. The method achieved **1.5× overall speedup** compared to VLA-Adapter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2808fb3b-91aa-43db-a209-86e28f28636a",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "37160f1b-55a8-4aa4-824a-7817c865dfc5",
  "toolUseResult": {
    "bytes": 213602,
    "code": 200,
    "codeText": "OK",
    "result": "# FocusVLA: Key Technical Details\n\n## 1) Architecture Components\n\n**Vision Encoder:** DINOv2 + SigLIP (combined as \"DS\") plus VGGT for implicit 3D information\n\n**LLM Backbone:** \"Qwen2.5-0.5B\" serving as the core language model\n\n**Parameters:** Total trainable parameters are 342.7M, split between VLM (103.6M) and policy (239.1M)\n\n## 2) Visual Token Selection\n\nThe system reduces from **512 raw visual tokens to 256 selected tokens** using a patch-level focus mechanism based on cross-attention scores between action queries and vision keys, with \"top-K scores retained for information propagation.\"\n\n## 3) LIBERO Benchmark Results (Multi-weight setting)\n\n- **Spatial:** 99.6%\n- **Object:** 100.0%\n- **Goal:** 98.8%\n- **Long:** 96.2%\n- **Average:** 98.7%\n\n## 4) Robustness Evaluation\n\nThe paper includes real-world experiments with three task variations (background, spatial arrangement, target object changes) but does not explicitly report LIBERO-Plus or systematic perturbation studies. Failure cases show sensitivity to \"initialization shifts and environmental variations.\"\n\n## 5) Token Selection Mechanism\n\nSelection uses \"Softmax(TopK(...)) where only tokens with top-K scores are retained,\" based on attention scores from action latent to vision keys.\n\n## 6) Training Resources\n\nTraining used **4 A100 GPUs** for LIBERO (100k steps, batch size 64) and **8 A100 GPUs** for RoboTwin. The method achieved **1.5× overall speedup** compared to VLA-Adapter.",
    "durationMs": 6596,
    "url": "https://arxiv.org/html/2603.28740"
  },
  "sourceToolAssistantUUID": "2808fb3b-91aa-43db-a209-86e28f28636a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T07:00:59.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbDNuBkhmyraXr8G5QF42g`</summary>

```json
{
  "query": "SmolVLA LIBERO benchmark results success rate 2025 performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37160f1b-55a8-4aa4-824a-7817c865dfc5",
  "isSidechain": false,
  "requestId": "req_011Cb22jhKSERsdqoRbWeuq1",
  "type": "assistant",
  "uuid": "46b0112e-038e-44cc-8166-17bb1c0ef76c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ruk7WbrHaQE9kNdZmYTVmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 58362,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 653,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 58362,
          "cache_creation_input_tokens": 653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 653
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

_source line 79 · 2026-05-14T07:01:05.740Z_

<details><summary>↩ Tool result · `toolu_01MbDNuBkhmyraXr8G5QF42g`</summary>

```text
Web search results for query: "SmolVLA LIBERO benchmark results success rate 2025 performance"

Links: [{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"Hugging Face Unveils SmolVLA: Efficient and Affordable Vision-Language-Action Model for Robotics | Timekeeper","url":"https://kiadev.net/news/2025-06-03-hugging-face-smolvla-efficient-affordable-robotics/"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"}]

Based on the search results, here are the SmolVLA LIBERO benchmark results for 2025:

## LIBERO Benchmark Performance

SmolVLA (0.45B parameters) achieves an average success rate of 87.3% on the LIBERO benchmark, closely matching or surpassing larger models such as π₀ (3.3B).

### Comparative Performance

The 0.45B parameter SmolVLA achieves an average success rate of 87.3% on LIBERO, outperforming Octo (0.09B, 75.1%), OpenVLA (7B, 76.5%), and even the robotics-pretrained π0 (3.3B, 86.0%).

### Task-Specific Breakdown

According to the paper, the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3%.

### Larger Model Variant

The model's performance scales with its parameter count, with the largest SmolVLA variant (2.25B parameters) achieving the highest success rates in both LIBERO (88.75%) and Meta-World (68.24%).

## Additional Highlights

In real-world settings, SmolVLA achieves average success rates of 78.3% across pick-place, stacking, and sorting tasks—outperforming both ACT (trained from scratch) and π₀ (finetuned).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46b0112e-038e-44cc-8166-17bb1c0ef76c",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "12dd804a-5c43-4d84-b542-fdfb958d3c5f",
  "toolUseResult": {
    "query": "SmolVLA LIBERO benchmark results success rate 2025 performance",
    "results": [
      {
        "tool_use_id": "srvtoolu_015vFe2UW8VCukmyFB6Yrk2X",
        "content": [
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "Hugging Face Unveils SmolVLA: Efficient and Affordable Vision-Language-Action Model for Robotics | Timekeeper",
            "url": "https://kiadev.net/news/2025-06-03-hugging-face-smolvla-efficient-affordable-robotics/"
          },
          {
            "title": "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]",
            "url": "https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"
          },
          {
            "title": "VLA-0-Smol",
            "url": "https://robot-learning-collective.github.io/vla-0-smol"
          },
          {
            "title": "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3287"
          },
          {
            "title": "SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2354"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          }
        ]
      },
      "Based on the search results, here are the SmolVLA LIBERO benchmark results for 2025:\n\n## LIBERO Benchmark Performance\n\nSmolVLA (0.45B parameters) achieves an average success rate of 87.3% on the LIBERO benchmark, closely matching or surpassing larger models such as π₀ (3.3B).\n\n### Comparative Performance\n\nThe 0.45B parameter SmolVLA achieves an average success rate of 87.3% on LIBERO, outperforming Octo (0.09B, 75.1%), OpenVLA (7B, 76.5%), and even the robotics-pretrained π0 (3.3B, 86.0%).\n\n### Task-Specific Breakdown\n\nAccording to the paper, the 0.45B model achieves success rates of approximately 90%, 96%, 92%, 71% (Spatial, Object, Goal, Long), averaging 87.3%.\n\n### Larger Model Variant\n\nThe model's performance scales with its parameter count, with the largest SmolVLA variant (2.25B parameters) achieving the highest success rates in both LIBERO (88.75%) and Meta-World (68.24%).\n\n## Additional Highlights\n\nIn real-world settings, SmolVLA achieves average success rates of 78.3% across pick-place, stacking, and sorting tasks—outperforming both ACT (trained from scratch) and π₀ (finetuned)."
    ],
    "durationSeconds": 6.532845381000021
  },
  "sourceToolAssistantUUID": "46b0112e-038e-44cc-8166-17bb1c0ef76c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "12dd804a-5c43-4d84-b542-fdfb958d3c5f",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Tool call

_source line 82 · 2026-05-14T07:01:15.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0171nW1eLuDdaiLHdEmMRZLw`</summary>

```json
{
  "query": "SmolVLA LIBERO-Plus robustness results perturbation evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12dd804a-5c43-4d84-b542-fdfb958d3c5f",
  "isSidechain": false,
  "requestId": "req_011Cb22kPPTC9pE7Rw4AfG6T",
  "type": "assistant",
  "uuid": "7e112f08-a9f0-4f24-92f7-f89e30fe52f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFDusAD6UgHSq9JSfUNojk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 59015,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 59015,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1052
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

_source line 83 · 2026-05-14T07:01:25.386Z_

<details><summary>↩ Tool result · `toolu_0171nW1eLuDdaiLHdEmMRZLw`</summary>

```text
Web search results for query: "SmolVLA LIBERO-Plus robustness results perturbation evaluation 2025 2026"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"}]

I found comprehensive information about LIBERO-Plus and its robustness evaluation results. However, the search results do not contain specific information about SmolVLA's performance on LIBERO-Plus. Let me search more specifically for SmolVLA results.

Links: [{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3264"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2258"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"}]

Based on the web search results, I have found relevant information about LIBERO-Plus robustness evaluation results and SmolVLA, though they weren't directly linked in one specific paper. Here's what I found:

## LIBERO-Plus: Robustness Evaluation Overview

LIBERO-Plus identifies seven core dimensions of perturbation: objects layout, environment background sampling, light variations, camera-view shifts, robot arm initialization perturbations, LLM-based language rewrites, and image noise.

### Key Robustness Findings

VLA models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Language perturbations result in the smallest average performance drop (-25.3) across most models, though models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### Benchmark Structure

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions, with 10,030 tasks organized across seven perturbation factors, and evaluated across four representative models stratified into five difficulty levels.

## SmolVLA Performance

Regarding SmolVLA specifically, in the LIBERO benchmark, SmolVLA (0.45B) achieves an average success rate of 87.3%, closely matching or surpassing larger models such as π₀ (3.3B).

However, the search results don't contain specific published results for SmolVLA's performance on LIBERO-Plus with its perturbation evaluation methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e112f08-a9f0-4f24-92f7-f89e30fe52f9",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "3d97da4d-ac23-4339-b583-c5d5bfc9466e",
  "toolUseResult": {
    "query": "SmolVLA LIBERO-Plus robustness results perturbation evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dy1THJ55PTVQ7X169Vk7VV",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          },
          {
            "title": "Sylvest/LIBERO-plus · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626v1"
          }
        ]
      },
      "I found comprehensive information about LIBERO-Plus and its robustness evaluation results. However, the search results do not contain specific information about SmolVLA's performance on LIBERO-Plus. Let me search more specifically for SmolVLA results.",
      {
        "tool_use_id": "srvtoolu_01X82LomwbvUf8XjwmmvCZxj",
        "content": [
          {
            "title": "[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1316"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          },
          {
            "title": "Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2354"
          },
          {
            "title": "smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/3264"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2258"
          },
          {
            "title": "Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"
          },
          {
            "title": "Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "VLA-0-Smol",
            "url": "https://robot-learning-collective.github.io/vla-0-smol"
          }
        ]
      },
      "Based on the web search results, I have found relevant information about LIBERO-Plus robustness evaluation results and SmolVLA, though they weren't directly linked in one specific paper. Here's what I found:\n\n## LIBERO-Plus: Robustness Evaluation Overview\n\nLIBERO-Plus identifies seven core dimensions of perturbation: objects layout, environment background sampling, light variations, camera-view shifts, robot arm initialization perturbations, LLM-based language rewrites, and image noise.\n\n### Key Robustness Findings\n\nVLA models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\nLanguage perturbations result in the smallest average performance drop (-25.3) across most models, though models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\n### Benchmark Structure\n\nLIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions, with 10,030 tasks organized across seven perturbation factors, and evaluated across four representative models stratified into five difficulty levels.\n\n## SmolVLA Performance\n\nRegarding SmolVLA specifically, in the LIBERO benchmark, SmolVLA (0.45B) achieves an average success rate of 87.3%, closely matching or surpassing larger models such as π₀ (3.3B).\n\nHowever, the search results don't contain specific published results for SmolVLA's performance on LIBERO-Plus with its perturbation evaluation methodology."
    ],
    "durationSeconds": 10.19240155400004
  },
  "sourceToolAssistantUUID": "7e112f08-a9f0-4f24-92f7-f89e30fe52f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-14T07:01:28.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C6KhCsori4xuivNg6dsG6Z`</summary>

```json
{
  "query": "Fischer variational information bottleneck adversarial robustness gradient obfuscation 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d97da4d-ac23-4339-b583-c5d5bfc9466e",
  "isSidechain": false,
  "requestId": "req_011Cb22mqKSzQfYKK6Pp112J",
  "type": "assistant",
  "uuid": "fc4aa89f-817b-411a-b20e-b888d53673de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPmQQ1hW4tepnqjL6GHVs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 60067,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 60067,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1603
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

_source line 85 · 2026-05-14T07:01:33.802Z_

<details><summary>↩ Tool result · `toolu_01C6KhCsori4xuivNg6dsG6Z`</summary>

```text
Web search results for query: "Fischer variational information bottleneck adversarial robustness gradient obfuscation 2021"

Links: [{"title":"A Closer Look at the Adversarial Robustness of Information Bottleneck Models","url":"https://arxiv.org/pdf/2107.05712"},{"title":"DEEP VARIATIONAL INFORMATION BOTTLENECK","url":"https://openreview.net/pdf?id=HyxQzBceg"},{"title":"[1612.00410] Deep Variational Information Bottleneck","url":"https://arxiv.org/abs/1612.00410"},{"title":"A Closer Look at the Adversarial Robustness of Information Bottleneck Models","url":"https://irakorshunova.github.io/advml_icml2021_poster.pdf"},{"title":"[2107.05712] A Closer Look at the Adversarial Robustness of Information Bottleneck Models","url":"https://arxiv.org/abs/2107.05712"},{"title":"A Closer Look at the Adversarial Robustness of Information Bottleneck Models | DeepMind","url":"https://deepmind.com/research/publications/2021/A-Closer-Look-at-the-Adversarial-Robustness-of-Information-Bottleneck-Models"},{"title":"(PDF) A Closer Look at the Adversarial Robustness of Information Bottleneck Models","url":"https://www.researchgate.net/publication/353234073_A_Closer_Look_at_the_Adversarial_Robustness_of_Information_Bottleneck_Models"},{"title":"Deep Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=HyxQzBceg"},{"title":"A Closer Look at the Adversarial Robustness of Information Bottleneck Models | OpenReview","url":"https://openreview.net/forum?id=1UA9zfQuIdp"},{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"}]

Based on the search results, I found highly relevant research on this topic:

## Main Finding

A 2021 study examined the adversarial robustness of information bottleneck models for classification, finding that information bottlenecks alone are not a strong defense strategy, and that previous results were likely influenced by gradient obfuscation.

## Context on Previous Work

Fischer & Alemi (2020) had shown that CEB (Conditional Entropy Bottleneck) models could outperform adversarially trained models under both l∞ and l2 PGD attacks while incurring no drop in standard accuracy. However, no clear explanation had been found as to how information bottleneck models become more robust to adversarial examples, and previous works had failed to investigate possible effects of gradient obfuscation which could lead to a false sense of security.

## Key Investigation

The 2021 research found that when driving robust accuracy to zero by increasing the number of restarts in PGD attacks, it indicated gradient obfuscation, as the loss landscape cannot be efficiently explored by gradient-based methods.

The paper you're searching for appears to be "A Closer Look at the Adversarial Robustness of Information Bottleneck Models" by Korshunova et al., accepted at the ICML 2021 workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc4aa89f-817b-411a-b20e-b888d53673de",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "c5b1a9a8-deb1-478a-98ed-fccdf9dd512a",
  "toolUseResult": {
    "query": "Fischer variational information bottleneck adversarial robustness gradient obfuscation 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_015uyjj74Lc7eCrxEUzHxv4H",
        "content": [
          {
            "title": "A Closer Look at the Adversarial Robustness of Information Bottleneck Models",
            "url": "https://arxiv.org/pdf/2107.05712"
          },
          {
            "title": "DEEP VARIATIONAL INFORMATION BOTTLENECK",
            "url": "https://openreview.net/pdf?id=HyxQzBceg"
          },
          {
            "title": "[1612.00410] Deep Variational Information Bottleneck",
            "url": "https://arxiv.org/abs/1612.00410"
          },
          {
            "title": "A Closer Look at the Adversarial Robustness of Information Bottleneck Models",
            "url": "https://irakorshunova.github.io/advml_icml2021_poster.pdf"
          },
          {
            "title": "[2107.05712] A Closer Look at the Adversarial Robustness of Information Bottleneck Models",
            "url": "https://arxiv.org/abs/2107.05712"
          },
          {
            "title": "A Closer Look at the Adversarial Robustness of Information Bottleneck Models | DeepMind",
            "url": "https://deepmind.com/research/publications/2021/A-Closer-Look-at-the-Adversarial-Robustness-of-Information-Bottleneck-Models"
          },
          {
            "title": "(PDF) A Closer Look at the Adversarial Robustness of Information Bottleneck Models",
            "url": "https://www.researchgate.net/publication/353234073_A_Closer_Look_at_the_Adversarial_Robustness_of_Information_Bottleneck_Models"
          },
          {
            "title": "Deep Variational Information Bottleneck | OpenReview",
            "url": "https://openreview.net/forum?id=HyxQzBceg"
          },
          {
            "title": "A Closer Look at the Adversarial Robustness of Information Bottleneck Models | OpenReview",
            "url": "https://openreview.net/forum?id=1UA9zfQuIdp"
          },
          {
            "title": "Revisiting the Variational Information Bottleneck | OpenReview",
            "url": "https://openreview.net/forum?id=w10KdRwcMk"
          }
        ]
      },
      "Based on the search results, I found highly relevant research on this topic:\n\n## Main Finding\n\nA 2021 study examined the adversarial robustness of information bottleneck models for classification, finding that information bottlenecks alone are not a strong defense strategy, and that previous results were likely influenced by gradient obfuscation.\n\n## Context on Previous Work\n\nFischer & Alemi (2020) had shown that CEB (Conditional Entropy Bottleneck) models could outperform adversarially trained models under both l∞ and l2 PGD attacks while incurring no drop in standard accuracy. However, no clear explanation had been found as to how information bottleneck models become more robust to adversarial examples, and previous works had failed to investigate possible effects of gradient obfuscation which could lead to a false sense of security.\n\n## Key Investigation\n\nThe 2021 research found that when driving robust accuracy to zero by increasing the number of restarts in PGD attacks, it indicated gradient obfuscation, as the loss landscape cannot be efficiently explored by gradient-based methods.\n\nThe paper you're searching for appears to be \"A Closer Look at the Adversarial Robustness of Information Bottleneck Models\" by Korshunova et al., accepted at the ICML 2021 workshop."
    ],
    "durationSeconds": 5.477049893999996
  },
  "sourceToolAssistantUUID": "fc4aa89f-817b-411a-b20e-b888d53673de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-14T07:01:36.946Z_

Good — the Fischer et al. claim is verified. Let me now search for any very recent VLA robustness work from April-May 2026 that might be a direct competitor.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5b1a9a8-deb1-478a-98ed-fccdf9dd512a",
  "isSidechain": false,
  "requestId": "req_011Cb22nTMdWTc2CrHt96PNY",
  "type": "assistant",
  "uuid": "fff95a63-b663-4e83-95c8-c0bae0cce59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHPwdAPSABDxDvKBKXqQQb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 61670,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 61670,
          "cache_creation_input_tokens": 945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 945
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

_source line 87 · 2026-05-14T07:01:37.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6MQqgRyTEEwNJiegsR5jj`</summary>

```json
{
  "query": "VLA robustness method training visual tokens May 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff95a63-b663-4e83-95c8-c0bae0cce59a",
  "isSidechain": false,
  "requestId": "req_011Cb22nTMdWTc2CrHt96PNY",
  "type": "assistant",
  "uuid": "f611d23f-b929-49a0-b4f0-baf62cd92ef6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHPwdAPSABDxDvKBKXqQQb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 61670,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 61670,
          "cache_creation_input_tokens": 945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 945
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

_source line 88 · 2026-05-14T07:01:45.541Z_

<details><summary>↩ Tool result · `toolu_01H6MQqgRyTEEwNJiegsR5jj`</summary>

```text
Web search results for query: "VLA robustness method training visual tokens May 2026 arXiv"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/html/2603.16044"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116v3"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.04678v1"}]

I found several relevant research papers on arXiv related to VLA (Vision-Language-Action) models and robustness methods with visual tokens. Here are the key findings:

## Key Papers Found:

1. **VLA-IAP: Training-Free Visual Token Pruning** (March 24, 2026)
   - Proposes VLA-IAP (Interaction-Aligned Pruning), a training-free method that introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

2. **RobustVLA: Robustness-Aware Reinforcement Post-Training** (December 1, 2025)
   - Introduces RobustVLA, a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models through Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.

3. **Enhancing Generalization by Preserving Pretrained Representations** (September 14, 2025)
   - Addresses co-training issues with a partially frozen visual encoder designed to better preserve pretrained robust visual representations during fine-tuning, and an action tokenizer that reuses pretrained embeddings aligned better with the vision-language training objective.

4. **Latent Reasoning VLA** (Recent - 1 week ago)
   - Demonstrates that latent CoT reasoning not only improves clean performance, but also enhances robustness to corrupted visual inputs.

5. **Improving Robustness by Restoring Corrupted Visual Inputs** (February 1, 2026)
   - Introduces the Corruption Restoration Transformer (CRT), a specialized module designed to restore visual integrity upstream of the VLA by leveraging advanced architectural mechanisms alongside an adversarial training objective.

These papers represent recent advances in VLA robustness methods with various approaches to handling visual tokens and training strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f611d23f-b929-49a0-b4f0-baf62cd92ef6",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "cec25274-7150-404a-b2d1-33710b6e7905",
  "toolUseResult": {
    "query": "VLA robustness method training visual tokens May 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CqwmrpXqRDHXLxWidf8Dq7",
        "content": [
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/html/2509.11417v1"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.01331"
          },
          {
            "title": "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation",
            "url": "https://arxiv.org/html/2603.16044"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/html/2510.00037"
          },
          {
            "title": "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.01166v2"
          },
          {
            "title": "Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs",
            "url": "https://arxiv.org/html/2602.01158"
          },
          {
            "title": "VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting",
            "url": "https://arxiv.org/html/2507.05116v3"
          },
          {
            "title": "VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation",
            "url": "https://arxiv.org/html/2502.02175v1"
          },
          {
            "title": "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2605.04678v1"
          }
        ]
      },
      "I found several relevant research papers on arXiv related to VLA (Vision-Language-Action) models and robustness methods with visual tokens. Here are the key findings:\n\n## Key Papers Found:\n\n1. **VLA-IAP: Training-Free Visual Token Pruning** (March 24, 2026)\n   - Proposes VLA-IAP (Interaction-Aligned Pruning), a training-free method that introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.\n\n2. **RobustVLA: Robustness-Aware Reinforcement Post-Training** (December 1, 2025)\n   - Introduces RobustVLA, a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models through Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.\n\n3. **Enhancing Generalization by Preserving Pretrained Representations** (September 14, 2025)\n   - Addresses co-training issues with a partially frozen visual encoder designed to better preserve pretrained robust visual representations during fine-tuning, and an action tokenizer that reuses pretrained embeddings aligned better with the vision-language training objective.\n\n4. **Latent Reasoning VLA** (Recent - 1 week ago)\n   - Demonstrates that latent CoT reasoning not only improves clean performance, but also enhances robustness to corrupted visual inputs.\n\n5. **Improving Robustness by Restoring Corrupted Visual Inputs** (February 1, 2026)\n   - Introduces the Corruption Restoration Transformer (CRT), a specialized module designed to restore visual integrity upstream of the VLA by leveraging advanced architectural mechanisms alongside an adversarial training objective.\n\nThese papers represent recent advances in VLA robustness methods with various approaches to handling visual tokens and training strategies."
    ],
    "durationSeconds": 7.9552370350000565
  },
  "sourceToolAssistantUUID": "f611d23f-b929-49a0-b4f0-baf62cd92ef6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-14T07:01:49.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H2dnQfhsjvzC1B8zzMF2wJ`</summary>

```json
{
  "query": "VLA visual augmentation consistency invariance domain randomization training robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cec25274-7150-404a-b2d1-33710b6e7905",
  "isSidechain": false,
  "requestId": "req_011Cb22oKWNdn4CWZ9gvLetL",
  "type": "assistant",
  "uuid": "25653f7f-e97d-4a3f-8781-3ac0c5f7b8e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eg1AizbzjRZVyMv6moji1P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 62615,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 62615,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
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

_source line 90 · 2026-05-14T07:01:56.934Z_

<details><summary>↩ Tool result · `toolu_01H2dnQfhsjvzC1B8zzMF2wJ`</summary>

```text
Web search results for query: "VLA visual augmentation consistency invariance domain randomization training robustness 2026"

Links: [{"title":"Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations","url":"https://arxiv.org/html/2509.18953v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"DexGraspVLA: A Vision-Language-Action Framework Towards General","url":"https://arxiv.org/pdf/2502.20900"},{"title":"E-VLA: Event-augmented Vision-Language-Action Model for Dark and Blurred Scenes","url":"https://arxiv.org/html/2604.04834"},{"title":"Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust","url":"https://arxiv.org/html/2410.01971"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

I found several relevant papers and resources on VLA (Vision-Language-Action) models and robustness. Here's what the search returned:

## Key Findings on VLA Robustness and Domain Adaptation

Recent research recommends incorporating spatial augmentation with systematic rotation and translation variations during training, coupled with multi-view consistency to maintain stable object representations under viewpoint transformation.

### Eva-VLA Framework
The Eva-VLA framework provides a direct path to robustness through adversarial training—by using it as an attack generator during training, models can learn to resist worst-case physical variations discovered automatically across simulation environments.

### RobustVLA Approach
RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Through robustness analysis, it identifies two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.

### Generalization Without Extensive Retraining
Robustness under visual perturbations is limited primarily by Spatial Modeling, and targeted lightweight adaptation is sufficient to reactivate the latent robustness of pretrained VLA models—without large-scale retraining or extensive domain randomization.

### Event-Augmented Approaches
E-VLA is an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable.

The search results show active research in 2026 on making VLAs more robust through various training and adaptation strategies, with emphasis on consistency, domain invariance, and efficient methods for improving performance under visual perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25653f7f-e97d-4a3f-8781-3ac0c5f7b8e8",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "3069282e-74f9-423a-8d52-32f17ca72e00",
  "toolUseResult": {
    "query": "VLA visual augmentation consistency invariance domain randomization training robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LaTghAme88bYKRi6mErhVK",
        "content": [
          {
            "title": "Eva-VLA: Evaluating Vision-Language-Action Models’ Robustness Under Real-World Physical Variations",
            "url": "https://arxiv.org/html/2509.18953v1"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.01331"
          },
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902"
          },
          {
            "title": "DexGraspVLA: A Vision-Language-Action Framework Towards General",
            "url": "https://arxiv.org/pdf/2502.20900"
          },
          {
            "title": "E-VLA: Event-augmented Vision-Language-Action Model for Dark and Blurred Scenes",
            "url": "https://arxiv.org/html/2604.04834"
          },
          {
            "title": "Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust",
            "url": "https://arxiv.org/html/2410.01971"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          }
        ]
      },
      "I found several relevant papers and resources on VLA (Vision-Language-Action) models and robustness. Here's what the search returned:\n\n## Key Findings on VLA Robustness and Domain Adaptation\n\nRecent research recommends incorporating spatial augmentation with systematic rotation and translation variations during training, coupled with multi-view consistency to maintain stable object representations under viewpoint transformation.\n\n### Eva-VLA Framework\nThe Eva-VLA framework provides a direct path to robustness through adversarial training—by using it as an attack generator during training, models can learn to resist worst-case physical variations discovered automatically across simulation environments.\n\n### RobustVLA Approach\nRobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Through robustness analysis, it identifies two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.\n\n### Generalization Without Extensive Retraining\nRobustness under visual perturbations is limited primarily by Spatial Modeling, and targeted lightweight adaptation is sufficient to reactivate the latent robustness of pretrained VLA models—without large-scale retraining or extensive domain randomization.\n\n### Event-Augmented Approaches\nE-VLA is an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable.\n\nThe search results show active research in 2026 on making VLAs more robust through various training and adaptation strategies, with emphasis on consistency, domain invariance, and efficient methods for improving performance under visual perturbations."
    ],
    "durationSeconds": 7.242716402999998
  },
  "sourceToolAssistantUUID": "25653f7f-e97d-4a3f-8781-3ac0c5f7b8e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3069282e-74f9-423a-8d52-32f17ca72e00",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Assistant

_source line 93 · 2026-05-14T07:02:00.187Z_

Let me check the "Run-time Observation Interventions" paper — it sounds potentially relevant to the token-level intervention approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3069282e-74f9-423a-8d52-32f17ca72e00",
  "isSidechain": false,
  "requestId": "req_011Cb22pAD4a5rhusGk9YrLD",
  "type": "assistant",
  "uuid": "9bbf103e-b696-4351-a893-ab21145aafd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpSeCjot6p2QFoYvvm7SmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 63700,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 63700,
          "cache_creation_input_tokens": 990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 990
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

_source line 94 · 2026-05-14T07:02:03.018Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015vJGMzkURtT726jH8y3r1a`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.01971",
  "prompt": "Extract: 1) What does this paper do exactly? Is it about token-level interventions or pixel-level? 2) Does it evaluate on LIBERO? 3) What is the approach - training-time or test-time? 4) How is it different from token pruning/selection approaches? 5) When was it published and at what venue?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bbf103e-b696-4351-a893-ab21145aafd8",
  "isSidechain": false,
  "requestId": "req_011Cb22pAD4a5rhusGk9YrLD",
  "type": "assistant",
  "uuid": "34ca6757-6e41-47ae-baa9-80bb5848dcd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpSeCjot6p2QFoYvvm7SmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 63700,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 63700,
          "cache_creation_input_tokens": 990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 990
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

_source line 95 · 2026-05-14T07:02:07.231Z_

<details><summary>↩ Tool result · `toolu_015vJGMzkURtT726jH8y3r1a`</summary>

```text
# Analysis of arXiv:2410.01971

**1) What the paper does & intervention level:**
The paper introduces BYOVLA, which performs pixel-level interventions. It "dynamically identifies regions of the input image that the model is sensitive to, and (2) minimally alters task-irrelevant regions" using automated image editing tools.

**2) LIBERO evaluation:**
The abstract and page content do not mention LIBERO evaluation. Only "language-instructed manipulation tasks" are referenced.

**3) Approach timing:**
This is a test-time (run-time) method. The abstract explicitly states it's a "run-time intervention scheme" that works "without model fine-tuning or access to the model's weights."

**4) Difference from token pruning:**
The document doesn't discuss token pruning or selection approaches, so no comparison is provided in this content.

**5) Publication details:**
The paper was **submitted October 2, 2024** (arXiv:2410.01971). The page shows no peer-reviewed venue publication—it appears to be a preprint submission to arXiv's Robotics and Machine Learning categories only.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ca6757-6e41-47ae-baa9-80bb5848dcd2",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "0a5909f9-5587-4d73-84cb-fcfa0d2d5685",
  "toolUseResult": {
    "bytes": 45102,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2410.01971\n\n**1) What the paper does & intervention level:**\nThe paper introduces BYOVLA, which performs pixel-level interventions. It \"dynamically identifies regions of the input image that the model is sensitive to, and (2) minimally alters task-irrelevant regions\" using automated image editing tools.\n\n**2) LIBERO evaluation:**\nThe abstract and page content do not mention LIBERO evaluation. Only \"language-instructed manipulation tasks\" are referenced.\n\n**3) Approach timing:**\nThis is a test-time (run-time) method. The abstract explicitly states it's a \"run-time intervention scheme\" that works \"without model fine-tuning or access to the model's weights.\"\n\n**4) Difference from token pruning:**\nThe document doesn't discuss token pruning or selection approaches, so no comparison is provided in this content.\n\n**5) Publication details:**\nThe paper was **submitted October 2, 2024** (arXiv:2410.01971). The page shows no peer-reviewed venue publication—it appears to be a preprint submission to arXiv's Robotics and Machine Learning categories only.",
    "durationMs": 4210,
    "url": "https://arxiv.org/abs/2410.01971"
  },
  "sourceToolAssistantUUID": "34ca6757-6e41-47ae-baa9-80bb5848dcd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-14T07:02:10.867Z_

OK, BYOVLA is pixel-level, not token-level — so it's not a direct competitor to ACIBS. Let me verify one more critical claim: the TCA paper for token condensation improving distribution shift robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a5909f9-5587-4d73-84cb-fcfa0d2d5685",
  "isSidechain": false,
  "requestId": "req_011Cb22pvFwwdCMmzz1kqTg5",
  "type": "assistant",
  "uuid": "c733b31f-fbc9-4622-a9b9-f1df22e32fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yUKNWYiCUPm3ss7GvZC3w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 64690,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 64690,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 97 · 2026-05-14T07:02:13.232Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012FgdE3UEwS4S1XeGWrbDos`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.14729",
  "prompt": "Extract: 1) What is TCA and what does it do? 2) What robustness improvement does it achieve (exact numbers, e.g., 21.4% on CIFAR-100-C)? 3) Is it training-free or requires training? 4) Does it use information bottleneck? 5) Is it tested on any robotics or action prediction task? 6) What venue was it published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c733b31f-fbc9-4622-a9b9-f1df22e32fa1",
  "isSidechain": false,
  "requestId": "req_011Cb22pvFwwdCMmzz1kqTg5",
  "type": "assistant",
  "uuid": "10a1bc0e-3bed-480f-8146-8e679a92280f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yUKNWYiCUPm3ss7GvZC3w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 64690,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 64690,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 98 · 2026-05-14T07:03:57.874Z_

<details><summary>↩ Tool result · `toolu_012FgdE3UEwS4S1XeGWrbDos`</summary>

```text
# Analysis of arXiv:2410.14729

**1) What is TCA and what does it do?**

TCA (Token Condensation as Adaptation) is "a training-free adaptation method that takes a step beyond standard TC." It condenses token representations by introducing "reservoir-based domain anchor tokens for information-preserving token reduction and logits correction," enabling efficient test-time adaptation for vision-language models.

**2) What robustness improvement does it achieve?**

The paper reports "up to a 21.4% performance improvement over the strongest baseline on cross-dataset benchmark and the CIFAR-100-Corrupted dataset." Additionally, it achieves computational savings of "12.2% to 48.9%" GFLOPs reduction.

**3) Is it training-free or requires training?**

It is explicitly training-free. The title and abstract describe it as a "training-free test-time adaptation" method.

**4) Does it use information bottleneck?**

The document does not mention information bottleneck theory or methods.

**5) Is it tested on any robotics or action prediction task?**

No robotics or action prediction tasks are mentioned in the provided content.

**6) What venue was it published at?**

The document does not specify a published venue. It is an arXiv preprint (submitted October 2024, last revised March 2025) with no conference or journal publication noted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10a1bc0e-3bed-480f-8146-8e679a92280f",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "f654c916-7094-4d70-b4a8-340b9619c1c9",
  "toolUseResult": {
    "bytes": 48427,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2410.14729\n\n**1) What is TCA and what does it do?**\n\nTCA (Token Condensation as Adaptation) is \"a training-free adaptation method that takes a step beyond standard TC.\" It condenses token representations by introducing \"reservoir-based domain anchor tokens for information-preserving token reduction and logits correction,\" enabling efficient test-time adaptation for vision-language models.\n\n**2) What robustness improvement does it achieve?**\n\nThe paper reports \"up to a 21.4% performance improvement over the strongest baseline on cross-dataset benchmark and the CIFAR-100-Corrupted dataset.\" Additionally, it achieves computational savings of \"12.2% to 48.9%\" GFLOPs reduction.\n\n**3) Is it training-free or requires training?**\n\nIt is explicitly training-free. The title and abstract describe it as a \"training-free test-time adaptation\" method.\n\n**4) Does it use information bottleneck?**\n\nThe document does not mention information bottleneck theory or methods.\n\n**5) Is it tested on any robotics or action prediction task?**\n\nNo robotics or action prediction tasks are mentioned in the provided content.\n\n**6) What venue was it published at?**\n\nThe document does not specify a published venue. It is an arXiv preprint (submitted October 2024, last revised March 2025) with no conference or journal publication noted.",
    "durationMs": 104637,
    "url": "https://arxiv.org/abs/2410.14729"
  },
  "sourceToolAssistantUUID": "10a1bc0e-3bed-480f-8146-8e679a92280f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 99 · 2026-05-14T07:03:57.882Z_

```json
{
  "parentUuid": "f654c916-7094-4d70-b4a8-340b9619c1c9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "51984ea7-01b8-4380-a030-bd513c311f91",
  "timestamp": "2026-05-14T07:03:57.882Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 100 · 2026-05-14T07:04:03.543Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WarqjTGMsomu7D2nqz869M`</summary>

```json
{
  "query": "TCA token condensation test-time adaptation ICCV 2025 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51984ea7-01b8-4380-a030-bd513c311f91",
  "isSidechain": false,
  "requestId": "req_011Cb22y5wL8R4tAJ73iFHRP",
  "type": "assistant",
  "uuid": "cb534f52-f14b-465b-9ba6-1527c3de38ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TiMD7kF6hJsJ9L9cN9kL2m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 65154,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 65154,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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

_source line 101 · 2026-05-14T07:04:08.863Z_

<details><summary>↩ Tool result · `toolu_01WarqjTGMsomu7D2nqz869M`</summary>

```text
Web search results for query: "TCA token condensation test-time adaptation ICCV 2025 accepted"

Links: [{"title":"GitHub - Jo-wang/TCA: Official repo for ICCV 2025 paper \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation\"","url":"https://github.com/Jo-wang/TCA"},{"title":"Is Less More? Exploring Token Condensation as Training-free ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Is_Less_More_Exploring_Token_Condensation_as_Training-free_Test-time_Adaptation_ICCV_2025_paper.pdf"},{"title":"Track: Poster Session 1 & Exhibit Hall","url":"https://iccv.thecvf.com/virtual/2025/session/2873"},{"title":"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/html/2410.14729"},{"title":"[2410.14729] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729"},{"title":"[2410.14729v3] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://arxiv.org/abs/2410.14729v3"},{"title":"Tokens on Demand: Token Condensation as Training-free Test-time Adaptation | OpenReview","url":"https://openreview.net/forum?id=EK1yOLL7GA&noteId=aa1fhh8o1I"},{"title":"awesome-test-time-adaptation/TTA-OTTA.md at main · tim-learn/awesome-test-time-adaptation","url":"https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-OTTA.md"},{"title":"(PDF) Tokens on Demand: Token Condensation as Training-free Test-time Adaptation","url":"https://www.researchgate.net/publication/385107712_Tokens_on_Demand_Token_Condensation_as_Training-free_Test-time_Adaptation"},{"title":"Paper page - Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation","url":"https://huggingface.co/papers/2410.14729"}]

Based on the search results, I can confirm that the TCA (Token Condensation as Adaptation) paper has been accepted to ICCV 2025.

The paper is titled "Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation" and is an official ICCV 2025 publication.

**Key details about the paper:**

- **Authors:** Wang, Zixin; Gong, Dong; Wang, Sen; Huang, Zi; and Luo, Yadan
- **Core Contribution:** TCA is a training-free adaptation method that dynamically refines token selection based on evolving domain knowledge, tracking and maintaining domain-representative tokens over time to allow the model to adapt to new domains
- **Technical Approach:** Rather than passively discarding tokens, TCA condenses token representation by introducing reservoir-based domain anchor tokens for information-preserving token reduction and logit correction
- **Performance:** TCA achieves up to a 21.4% improvement over the strongest baseline while reducing GFLOPs by 12.2% to 48.9%

The paper addresses the challenge of adapting vision-language models like CLIP to distribution shifts during test-time inference without requiring training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb534f52-f14b-465b-9ba6-1527c3de38ed",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "80fef1c9-acbe-4e24-a26f-d980e278bcfd",
  "toolUseResult": {
    "query": "TCA token condensation test-time adaptation ICCV 2025 accepted",
    "results": [
      {
        "tool_use_id": "srvtoolu_019zk1XEUXj4gCHfjuqmpLnF",
        "content": [
          {
            "title": "GitHub - Jo-wang/TCA: Official repo for ICCV 2025 paper \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation\"",
            "url": "https://github.com/Jo-wang/TCA"
          },
          {
            "title": "Is Less More? Exploring Token Condensation as Training-free ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Is_Less_More_Exploring_Token_Condensation_as_Training-free_Test-time_Adaptation_ICCV_2025_paper.pdf"
          },
          {
            "title": "Track: Poster Session 1 & Exhibit Hall",
            "url": "https://iccv.thecvf.com/virtual/2025/session/2873"
          },
          {
            "title": "Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation",
            "url": "https://arxiv.org/html/2410.14729"
          },
          {
            "title": "[2410.14729] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation",
            "url": "https://arxiv.org/abs/2410.14729"
          },
          {
            "title": "[2410.14729v3] Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation",
            "url": "https://arxiv.org/abs/2410.14729v3"
          },
          {
            "title": "Tokens on Demand: Token Condensation as Training-free Test-time Adaptation | OpenReview",
            "url": "https://openreview.net/forum?id=EK1yOLL7GA&noteId=aa1fhh8o1I"
          },
          {
            "title": "awesome-test-time-adaptation/TTA-OTTA.md at main · tim-learn/awesome-test-time-adaptation",
            "url": "https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-OTTA.md"
          },
          {
            "title": "(PDF) Tokens on Demand: Token Condensation as Training-free Test-time Adaptation",
            "url": "https://www.researchgate.net/publication/385107712_Tokens_on_Demand_Token_Condensation_as_Training-free_Test-time_Adaptation"
          },
          {
            "title": "Paper page - Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation",
            "url": "https://huggingface.co/papers/2410.14729"
          }
        ]
      },
      "Based on the search results, I can confirm that the TCA (Token Condensation as Adaptation) paper has been accepted to ICCV 2025.\n\nThe paper is titled \"Is Less More? Exploring Token Condensation as Training-free Test-time Adaptation\" and is an official ICCV 2025 publication.\n\n**Key details about the paper:**\n\n- **Authors:** Wang, Zixin; Gong, Dong; Wang, Sen; Huang, Zi; and Luo, Yadan\n- **Core Contribution:** TCA is a training-free adaptation method that dynamically refines token selection based on evolving domain knowledge, tracking and maintaining domain-representative tokens over time to allow the model to adapt to new domains\n- **Technical Approach:** Rather than passively discarding tokens, TCA condenses token representation by introducing reservoir-based domain anchor tokens for information-preserving token reduction and logit correction\n- **Performance:** TCA achieves up to a 21.4% improvement over the strongest baseline while reducing GFLOPs by 12.2% to 48.9%\n\nThe paper addresses the challenge of adapting vision-language models like CLIP to distribution shifts during test-time inference without requiring training."
    ],
    "durationSeconds": 5.314708830000018
  },
  "sourceToolAssistantUUID": "cb534f52-f14b-465b-9ba6-1527c3de38ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 102 · 2026-05-14T07:04:18.197Z_

Good — TCA confirmed at ICCV 2025. Let me now search for one more critical area: whether anyone has specifically combined IB with token pruning for robustness in VLAs or similar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80fef1c9-acbe-4e24-a26f-d980e278bcfd",
  "isSidechain": false,
  "requestId": "req_011Cb22ytG93kC38674xm9KJ",
  "type": "assistant",
  "uuid": "9029f580-0002-45b0-baf6-be386292ebc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cckDh417dBvFUSYfqD8QB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 65822,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 65822,
          "cache_creation_input_tokens": 983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 983
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

_source line 103 · 2026-05-14T07:04:19.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015hJQ4oTUbAT4VivE5Ydw24`</summary>

```json
{
  "query": "\"information bottleneck\" \"token pruning\" OR \"token selection\" robustness augmentation consistency 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9029f580-0002-45b0-baf6-be386292ebc4",
  "isSidechain": false,
  "requestId": "req_011Cb22ytG93kC38674xm9KJ",
  "type": "assistant",
  "uuid": "773a387c-501e-4133-b7a9-e75c125c4823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cckDh417dBvFUSYfqD8QB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 65822,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 65822,
          "cache_creation_input_tokens": 983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 983
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

_source line 104 · 2026-05-14T07:04:27.554Z_

<details><summary>↩ Tool result · `toolu_015hJQ4oTUbAT4VivE5Ydw24`</summary>

```text
Web search results for query: ""information bottleneck" "token pruning" OR "token selection" robustness augmentation consistency 2025 2026"

Links: [{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v3"},{"title":"Advancing Transformer Efficiency with Token Pruning[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202503.1577"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_TopV_Compatible_Token_Pruning_with_Inference_Time_Optimization_for_Fast_CVPR_2025_paper.pdf"},{"title":"Token Bottleneck: One Token to Remember Dynamics","url":"https://arxiv.org/html/2507.06543v1"},{"title":"[2507.01728] Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach","url":"https://arxiv.org/abs/2507.01728"}]

I found relevant research at the intersection of your search terms. Here are the key findings:

## Information Bottleneck-Guided Token Compression

Recent work includes CompTrack, which uses information bottleneck-guided low-rank dynamic token compression for point cloud tracking at AAAI'26. Additionally, IBTM (Transformer with Information Bottleneck inspired Token Merging) performs token merging in a learnable scheme and reduces FLOPs and inference time while maintaining or improving prediction accuracy.

## Token Pruning and Selection Methods (2025-2026)

Recent work includes SPEECHPRUNE for context-aware token pruning (ICME'25), keyframe-oriented vision token pruning for long-form video (ICCV'25), and multiple token reduction papers at ICML'25, NeurIPS'25, and other major venues.

## Robustness Concerns with Token Compression

Visual token compression is widely used to accelerate vision-language models by pruning or merging tokens, yet adversarial robustness remains a concern—existing attacks can overestimate compressed model robustness due to an optimization-inference mismatch. Primary concerns with token pruning include potential degradation in model generalization and robustness, domain shift sensitivity where pruned models struggle on out-of-distribution inputs, and adversarial vulnerabilities where pruning may remove critical tokens.

## Beyond Efficiency: Consistency and Training

Token reduction integrated into the pre-training phase can improve training stability, with selective token utilization during training leading to more robust model learning. Methods like FastV that rely on attention scores often lead to position bias in retained tokens, and future approaches should preserve spatial diversity by enforcing structural uniformity to improve robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "773a387c-501e-4133-b7a9-e75c125c4823",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "137db4e4-a7d3-4944-a912-c00074405da6",
  "toolUseResult": {
    "query": "\"information bottleneck\" \"token pruning\" OR \"token selection\" robustness augmentation consistency 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VpHGAH4FiuMBXDK78jT4gx",
        "content": [
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models",
            "url": "https://aclanthology.org/2025.findings-acl.802.pdf"
          },
          {
            "title": "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression",
            "url": "https://arxiv.org/html/2601.21531"
          },
          {
            "title": "Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview",
            "url": "https://openreview.net/forum?id=Jwgw3znxT3"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality",
            "url": "https://arxiv.org/html/2505.18227v3"
          },
          {
            "title": "Advancing Transformer Efficiency with Token Pruning[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202503.1577"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in ...",
            "url": "https://arxiv.org/pdf/2505.18227"
          },
          {
            "title": "TopV: Compatible Token Pruning with Inference Time Optimization for Fast",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_TopV_Compatible_Token_Pruning_with_Inference_Time_Optimization_for_Fast_CVPR_2025_paper.pdf"
          },
          {
            "title": "Token Bottleneck: One Token to Remember Dynamics",
            "url": "https://arxiv.org/html/2507.06543v1"
          },
          {
            "title": "[2507.01728] Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach",
            "url": "https://arxiv.org/abs/2507.01728"
          }
        ]
      },
      "I found relevant research at the intersection of your search terms. Here are the key findings:\n\n## Information Bottleneck-Guided Token Compression\n\nRecent work includes CompTrack, which uses information bottleneck-guided low-rank dynamic token compression for point cloud tracking at AAAI'26. Additionally, IBTM (Transformer with Information Bottleneck inspired Token Merging) performs token merging in a learnable scheme and reduces FLOPs and inference time while maintaining or improving prediction accuracy.\n\n## Token Pruning and Selection Methods (2025-2026)\n\nRecent work includes SPEECHPRUNE for context-aware token pruning (ICME'25), keyframe-oriented vision token pruning for long-form video (ICCV'25), and multiple token reduction papers at ICML'25, NeurIPS'25, and other major venues.\n\n## Robustness Concerns with Token Compression\n\nVisual token compression is widely used to accelerate vision-language models by pruning or merging tokens, yet adversarial robustness remains a concern—existing attacks can overestimate compressed model robustness due to an optimization-inference mismatch. Primary concerns with token pruning include potential degradation in model generalization and robustness, domain shift sensitivity where pruned models struggle on out-of-distribution inputs, and adversarial vulnerabilities where pruning may remove critical tokens.\n\n## Beyond Efficiency: Consistency and Training\n\nToken reduction integrated into the pre-training phase can improve training stability, with selective token utilization during training leading to more robust model learning. Methods like FastV that rely on attention scores often lead to position bias in retained tokens, and future approaches should preserve spatial diversity by enforcing structural uniformity to improve robustness."
    ],
    "durationSeconds": 8.526010678999999
  },
  "sourceToolAssistantUUID": "773a387c-501e-4133-b7a9-e75c125c4823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-14T07:04:31.328Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LPMnv4yPJq9GVGZPgXKRr3`</summary>

```json
{
  "query": "LIBERO-PRO benchmark robustness evaluation VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "137db4e4-a7d3-4944-a912-c00074405da6",
  "isSidechain": false,
  "requestId": "req_011Cb231G9oJhCRLqp6Ua9Y6",
  "type": "assistant",
  "uuid": "fcf9c208-f720-431e-bad9-93ee0f2509ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr36Jjfts8acPrNJuvjKhq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 66805,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 66805,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 106 · 2026-05-14T07:04:37.089Z_

<details><summary>↩ Tool result · `toolu_01LPMnv4yPJq9GVGZPgXKRr3`</summary>

```text
Web search results for query: "LIBERO-PRO benchmark robustness evaluation VLA 2025"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"}]

Based on the search results, here's information about the LIBERO-PRO benchmark and robustness evaluation of VLA models in 2025:

## LIBERO-PRO Overview

LIBERO-PRO is a plug-and-play extension of LIBERO designed to foster fair comparison across models and to advance research on building VLA systems that can withstand reasonable and practically necessary perturbations. The benchmark extends the four original task categories in LIBERO by introducing object attribute perturbations, initial position perturbations, instruction perturbations, and environmental perturbations.

## Key Findings on VLA Robustness

The benchmark reveals significant robustness issues with current Vision-Language-Action models:

Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components.

Models persist in executing grasping actions when the target object is replaced with irrelevant items, and their outputs remain unchanged even when given corrupted instructions or even messy tokens.

## Critical Issues with Standard Evaluation

Several recent studies have noted that the high scores reported on LIBERO often fail to translate into reliable performance, even on tasks with only minor variations. These findings expose the severe flaws in current evaluation practices, and the community is called to abandon misleading methodologies in favor of robust assessments of model generalization and comprehension.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcf9c208-f720-431e-bad9-93ee0f2509ee",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "01480c55-d531-4fbe-949d-33606aa8ffa8",
  "toolUseResult": {
    "query": "LIBERO-PRO benchmark robustness evaluation VLA 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013LZnJxybSctFxqwBacU4KV",
        "content": [
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...",
            "url": "https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"
          }
        ]
      },
      "Based on the search results, here's information about the LIBERO-PRO benchmark and robustness evaluation of VLA models in 2025:\n\n## LIBERO-PRO Overview\n\nLIBERO-PRO is a plug-and-play extension of LIBERO designed to foster fair comparison across models and to advance research on building VLA systems that can withstand reasonable and practically necessary perturbations. The benchmark extends the four original task categories in LIBERO by introducing object attribute perturbations, initial position perturbations, instruction perturbations, and environmental perturbations.\n\n## Key Findings on VLA Robustness\n\nThe benchmark reveals significant robustness issues with current Vision-Language-Action models:\n\nDespite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components.\n\nModels persist in executing grasping actions when the target object is replaced with irrelevant items, and their outputs remain unchanged even when given corrupted instructions or even messy tokens.\n\n## Critical Issues with Standard Evaluation\n\nSeveral recent studies have noted that the high scores reported on LIBERO often fail to translate into reliable performance, even on tasks with only minor variations. These findings expose the severe flaws in current evaluation practices, and the community is called to abandon misleading methodologies in favor of robust assessments of model generalization and comprehension."
    ],
    "durationSeconds": 5.758271162000019
  },
  "sourceToolAssistantUUID": "fcf9c208-f720-431e-bad9-93ee0f2509ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 107_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "01480c55-d531-4fbe-949d-33606aa8ffa8",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 108_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Assistant

_source line 109 · 2026-05-14T07:04:40.760Z_

Now I have sufficient information to conduct a thorough review. Let me also quickly check one more thing — whether the idea's architecture details about SmolVLA are now correct after previous review feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01480c55-d531-4fbe-949d-33606aa8ffa8",
  "isSidechain": false,
  "requestId": "req_011Cb231xxUEcWaozTj67hkC",
  "type": "assistant",
  "uuid": "a0047c09-d5bc-440e-9f2a-315925efef61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ebSYzFKVvv4QDUixZF4Uv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 67876,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 67876,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 110 · 2026-05-14T07:04:43.757Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EBSyTMLAgNJF9MXE7x8M7M`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Extract the exact architecture of SmolVLA: 1) What is the vision encoder? Is it SigLIP specifically? 2) What is the language model? Is it SmolLM2 specifically? 3) Total parameter count? 4) Number of visual tokens per frame (64)? 5) How is token compression achieved (pixel shuffle, 3x3)? 6) What is the action expert architecture?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0047c09-d5bc-440e-9f2a-315925efef61",
  "isSidechain": false,
  "requestId": "req_011Cb231xxUEcWaozTj67hkC",
  "type": "assistant",
  "uuid": "79c26bfd-bdf5-407a-ab7d-73d56b7ac84a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ebSYzFKVvv4QDUixZF4Uv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 67876,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 955,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 67876,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 955
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

_source line 111 · 2026-05-14T07:04:49.201Z_

<details><summary>↩ Tool result · `toolu_01EBSyTMLAgNJF9MXE7x8M7M`</summary>

```text
# SmolVLA Architecture Breakdown

## Vision Encoder
**SigLIP** - The paper states: "SmolVLM-2 relies on SigLIP (Zhai et al., 2023) to encode visual features for SmolLM2 language decoder."

## Language Model
**SmolLM2** - Confirmed as the language decoder component of SmolVLM-2 backbone.

## Total Parameter Count
**450 million parameters** overall, with "approximately 100 million dedicated to the action expert." The VLM backbone itself contains the remaining ~350M parameters.

## Visual Tokens Per Frame
**64 tokens per frame** - Achieved by using "the global image only, in addition to a pixel shuffle operation, limiting the visual tokens to 64 per frame." This avoids the more computationally expensive image tiling technique.

## Token Compression Method
The paper specifies using a **pixel shuffle operation** rather than image tiling. No specific stride (like 3x3) is mentioned; the approach simply reduces resolution while maintaining global image context.

## Action Expert Architecture
The action expert uses a **Flow Matching Transformer** with these characteristics:
- Interleaved cross-attention and causal self-attention layers
- Hidden dimension of "0.75×d" (where d is the VLM's hidden dimension)
- Trained with flow matching objective (not regression)
- Outputs action chunks of n=50 timesteps
- Uses 10 inference steps during deployment
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79c26bfd-bdf5-407a-ab7d-73d56b7ac84a",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "1940ff99-ec93-4e2e-98b0-005c50fbcd5e",
  "toolUseResult": {
    "bytes": 522052,
    "code": 200,
    "codeText": "OK",
    "result": "# SmolVLA Architecture Breakdown\n\n## Vision Encoder\n**SigLIP** - The paper states: \"SmolVLM-2 relies on SigLIP (Zhai et al., 2023) to encode visual features for SmolLM2 language decoder.\"\n\n## Language Model\n**SmolLM2** - Confirmed as the language decoder component of SmolVLM-2 backbone.\n\n## Total Parameter Count\n**450 million parameters** overall, with \"approximately 100 million dedicated to the action expert.\" The VLM backbone itself contains the remaining ~350M parameters.\n\n## Visual Tokens Per Frame\n**64 tokens per frame** - Achieved by using \"the global image only, in addition to a pixel shuffle operation, limiting the visual tokens to 64 per frame.\" This avoids the more computationally expensive image tiling technique.\n\n## Token Compression Method\nThe paper specifies using a **pixel shuffle operation** rather than image tiling. No specific stride (like 3x3) is mentioned; the approach simply reduces resolution while maintaining global image context.\n\n## Action Expert Architecture\nThe action expert uses a **Flow Matching Transformer** with these characteristics:\n- Interleaved cross-attention and causal self-attention layers\n- Hidden dimension of \"0.75×d\" (where d is the VLM's hidden dimension)\n- Trained with flow matching objective (not regression)\n- Outputs action chunks of n=50 timesteps\n- Uses 10 inference steps during deployment",
    "durationMs": 5440,
    "url": "https://arxiv.org/html/2506.01844v1"
  },
  "sourceToolAssistantUUID": "79c26bfd-bdf5-407a-ab7d-73d56b7ac84a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-14T07:04:53.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BW7faPyiwTuRmS5ukWeCjd`</summary>

```json
{
  "query": "SmolVLA pixel shuffle 3x3 visual tokens 64 SigLIP architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1940ff99-ec93-4e2e-98b0-005c50fbcd5e",
  "isSidechain": false,
  "requestId": "req_011Cb232rov1DSvnsEvL7ZHb",
  "type": "assistant",
  "uuid": "819d42c0-c5d3-456f-a177-ea085495c920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JW4nw23G5phdQbgDX6XbDY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 68831,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 68831,
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

_source line 113 · 2026-05-14T07:05:01.752Z_

<details><summary>↩ Tool result · `toolu_01BW7faPyiwTuRmS5ukWeCjd`</summary>

```text
Web search results for query: "SmolVLA pixel shuffle 3x3 visual tokens 64 SigLIP architecture details"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLM to SmolVLM2: Compact Models for Multi-Image VQA - PyImageSearch","url":"https://pyimagesearch.com/2025/06/23/smolvlm-to-smolvlm2-compact-models-for-multi-image-vqa/"},{"title":"Weekly Robotics June #1 - SmolVLA discovery and thoughts","url":"https://huggingface.co/blog/Beegbrain/daily-robotics-june"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"SmolVLM: Redefining small and efficient multimodal models","url":"https://arxiv.org/html/2504.05299v1"},{"title":"SmolVLM - small yet mighty Vision Language Model","url":"https://huggingface.co/blog/smolvlm"},{"title":"SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"},{"title":"SmolVLA: Compact Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/smolvla"},{"title":"Papers Explained 346: SmolVLM. SmolVLM is a family of small, efficient… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-346-smolvlm-9b4e208fa66b"},{"title":"GenAI for Robotics: Fine-Tuning SmolVLA to Pick and Place | by Henry H | Medium","url":"https://medium.com/@henryhu1607/genai-for-robotics-fine-tuning-smolvla-to-pick-and-place-940b485e6c9b"}]

Based on the search results, here are the key architecture details for SmolVLA regarding pixel shuffle, visual tokens, and the SigLIP architecture:

## Visual Token Reduction with Pixel Shuffle

A 512×512 image is compressed into just 64 tokens, instead of 1024, using PixelShuffle as an efficient shuffling technique. For example, a 512×512 image normally yields 1024 SigLIP patches, but after a 3×3 pixel shuffle, it yields a 9× reduction.

After SigLIP encodes an image patch into a feature map, pixel-shuffle rearranges it: it trades spatial resolution for extra channels. Concretely, a 2×2 pixel shuffle turns each 2×2 block of pixels into 4 channels, so the feature map height and width each halve, reducing the token count by 4×.

## 3×3 Pixel Shuffle Implementation

SmolVLM uses a 3×3 shuffle (9× reduction) by splitting into 384×384 patches. Patches of 384×384 are used instead of 364×364, because 384 is divisible by 3, which is necessary for the pixel shuffle strategy to work.

## SigLIP Architecture Integration

SmolVLA uses SmolVLM2 as its VLM backbone, which consists of a SigLIP vision encoder and a SmolLM2 language decoder. Each input image is first split into sub-images and encoded by a SigLIP vision encoder, then a pixel-shuffle operation is applied to compress the features, and they are fed through a small MLP to produce "visual tokens."

## Overall Architecture

SmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "819d42c0-c5d3-456f-a177-ea085495c920",
  "isSidechain": false,
  "promptId": "d1b0be73-cca3-45ca-9385-83f7ecfbb564",
  "type": "user",
  "uuid": "4e58b713-5c6b-4283-b905-deb13a53402d",
  "toolUseResult": {
    "query": "SmolVLA pixel shuffle 3x3 visual tokens 64 SigLIP architecture details",
    "results": [
      {
        "tool_use_id": "srvtoolu_0128n6tEbL3fRKttUEDVSJGZ",
        "content": [
          {
            "title": "SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data",
            "url": "https://huggingface.co/blog/smolvla"
          },
          {
            "title": "SmolVLM to SmolVLM2: Compact Models for Multi-Image VQA - PyImageSearch",
            "url": "https://pyimagesearch.com/2025/06/23/smolvlm-to-smolvlm2-compact-models-for-multi-image-vqa/"
          },
          {
            "title": "Weekly Robotics June #1 - SmolVLA discovery and thoughts",
            "url": "https://huggingface.co/blog/Beegbrain/daily-robotics-june"
          },
          {
            "title": "SmolVLA: A vision-language-action model for affordable and efficient robotics",
            "url": "https://arxiv.org/html/2506.01844v1"
          },
          {
            "title": "SmolVLM: Redefining small and efficient multimodal models",
            "url": "https://arxiv.org/html/2504.05299v1"
          },
          {
            "title": "SmolVLM - small yet mighty Vision Language Model",
            "url": "https://huggingface.co/blog/smolvlm"
          },
          {
            "title": "SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"
          },
          {
            "title": "SmolVLA: Compact Vision-Language-Action Model",
            "url": "https://www.emergentmind.com/topics/smolvla"
          },
          {
            "title": "Papers Explained 346: SmolVLM. SmolVLM is a family of small, efficient… | by Ritvik Rastogi | Medium",
            "url": "https://ritvik19.medium.com/papers-explained-346-smolvlm-9b4e208fa66b"
          },
          {
            "title": "GenAI for Robotics: Fine-Tuning SmolVLA to Pick and Place | by Henry H | Medium",
            "url": "https://medium.com/@henryhu1607/genai-for-robotics-fine-tuning-smolvla-to-pick-and-place-940b485e6c9b"
          }
        ]
      },
      "Based on the search results, here are the key architecture details for SmolVLA regarding pixel shuffle, visual tokens, and the SigLIP architecture:\n\n## Visual Token Reduction with Pixel Shuffle\n\nA 512×512 image is compressed into just 64 tokens, instead of 1024, using PixelShuffle as an efficient shuffling technique. For example, a 512×512 image normally yields 1024 SigLIP patches, but after a 3×3 pixel shuffle, it yields a 9× reduction.\n\nAfter SigLIP encodes an image patch into a feature map, pixel-shuffle rearranges it: it trades spatial resolution for extra channels. Concretely, a 2×2 pixel shuffle turns each 2×2 block of pixels into 4 channels, so the feature map height and width each halve, reducing the token count by 4×.\n\n## 3×3 Pixel Shuffle Implementation\n\nSmolVLM uses a 3×3 shuffle (9× reduction) by splitting into 384×384 patches. Patches of 384×384 are used instead of 364×364, because 384 is divisible by 3, which is necessary for the pixel shuffle strategy to work.\n\n## SigLIP Architecture Integration\n\nSmolVLA uses SmolVLM2 as its VLM backbone, which consists of a SigLIP vision encoder and a SmolLM2 language decoder. Each input image is first split into sub-images and encoded by a SigLIP vision encoder, then a pixel-shuffle operation is applied to compress the features, and they are fed through a small MLP to produce \"visual tokens.\"\n\n## Overall Architecture\n\nSmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands."
    ],
    "durationSeconds": 7.956273892000026
  },
  "sourceToolAssistantUUID": "819d42c0-c5d3-456f-a177-ea085495c920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 114 · 2026-05-14T07:07:09.593Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have gathered comprehensive information. Let me synthesize my findings for the review.

Key findings from my research:

1. **FocusVLA (arXiv 2603.28740)**: Confirmed. Uses cross-attention-based top-K selection, DINOv2+SigLIP vision encoder, Qwen2.5-0.5B LLM backbone, 342.7M trainable params. Selects 256 of 512 tokens. Achieves 98.7% on LIBERO. No robustness/perturbation evaluation. The idea correctly cites and differentiates from FocusVLA.


2. **SmolVLA architecture**: Confirmed as SigLIP vision encoder + SmolLM2 language decoder with 450M total params, ~100M action expert, and 64 visual tokens per frame via 3×3 pixel shuffle. The description in the idea is now accurate.
3. **LIBERO-Plus**: Confirmed as CVPR 2026.
4. **SRPO vs baselines**: SRPO achieves 82.1% average, outperforming AVA-VLA's 74.7%, with a notable robustness drop from 95% to below 30%.
5. **FTM**: 4K params with 87.1% viewpoint accuracy using input-independent global affine transformation, tested only on π0.5.
6. **BC-IB**: ICML 2025 paper focusing on representation-level information bottleneck rather than token-level, emphasizing clean accuracy.
7. **SimPrune**: ICLR 2025 work using cross-branch similarity for token pruning in self-supervised learning with efficiency gains.
8. **TCA**: ICCV 2025 training-free token condensation achieving 21.4% improvement on CIFAR-100-C.
9. **DRIBO**: ICML 2022 paper on multi-

view information bottleneck for robust RL representations.
10. **Fischer et al.**: VIB's adversarial robustness partly stems from gradient obfuscation.
11. **CoRL 2026**: Abstract deadline May 26, paper deadline May 29.
12. **Token Reduction Beyond Efficiency**: Confirmed via arXiv 2505.18227.
13. **PDF**: April 2026 paper on test-time perturbation learning for VLA robustness—concurrent work but training-time focused unlike ACIBS.
14. **TIES**: Training-free token selection leveraging inter-layer rank consistency for efficiency improvements.

Now I'm evaluating the novelty across multiple dimensions. The core contribution combines information bottleneck-based token scoring with multi-view augmentation consistency during training, specifically targeting VLA robustness rather than efficiency. Checking against existing work: BC-IB operates at the representation level for RL, DRIBO applies multi-view IB to representations in RL, SimPrune uses cross-branch consistency for efficiency in SSL, TCA handles token condensation for robustness but without IB and at test-time, and FocusVLA addresses token selection in vision-language models. The combination of these elements—IB-grounded scoring, multi-view consistency, and robustness focus—appears genuinely novel in this space.

The individual components are established, so the novelty lies in how they're combined and applied to VLAs specifically. The theoretical grounding is sound but standard, and I'm being careful to frame this as an empirical approach rather than claiming certified robustness. Now I need to assess feasibility, starting with what's actually achievable with models like SmolVLA at 64 tokens.

Working with 64 tokens is quite constrained compared to typical pruning work that starts from 256-1024, though the retention rate sweep should help explore this unusual regime. The compute estimate of 155-185 hours on H100s seems reasonable for a smaller model, but the 15-day timeline is extremely tight—implementing the dual-view pipeline, the Gumbel-softmax scorer, FTM baseline, and LIBERO-Plus evaluation all within that window is ambitious. The progressive submission strategy helps mitigate this risk. There's also uncertainty around SmolVLA's baseline robustness on LIBERO-Plus since it hasn't been published yet, which adds another layer of risk to the evaluation.

The formulation itself is well-articulated with the loss combining action prediction, KL divergence for the information bottleneck, and spatial consistency. The differentiation from prior work is clear, and the progressive submission approach is thoughtfully designed. The core problem—VLA robustness—is important and timely, and token-level information bottleneck pruning does address a real gap between efficiency-focused methods and pixel-level robustness. If successful, this provides a principled lightweight approach. The main uncertainty is whether the improvement over FTM justifies the added complexity, especially given that the 64-token constraint might limit how much pruning effect is actually achievable. SmolVLA's unknown baseline on LIBERO-Plus remains a significant unknown that could affect the claimed robustness gaps. LAs, but SmolVLA specifically hasn't been tested on LIBERO-Plus. If SmolVLA already has different robustness characteristics (perhaps better due to more aggressive compression, or worse), the framing may need adjustment.

The central concern is pruning from just 64 tokens—at k=0.8, only 13 tokens get pruned, which might not give the IB objective enough room to meaningfully separate task-relevant from irrelevant information. FocusVLA operates on much larger reductions (512→256), so there's substantially more redundancy to work with there. FTM is also a risk since it achieves strong viewpoint robustness with minimal parameters; if it adapts well to SmolVLA, justifying ACIBS's added complexity becomes harder, though the plan to combine them as a contingency helps.

There's concurrent work on VLA robustness through test-time perturbation learning that I should acknowledge, even though it takes a different approach than ACIBS's training-time method. I've verified that SmolVLA does use the architecture I described. There's also training-free token selection work using inter-layer rank consistency that represents the competitive landscape in VLA token selection, though neither of these papers are currently cited.

With 15 days until the May 29 deadline and 12 days for the abstract, this is only feasible if the researcher already has SmolVLA and LIBERO infrastructure set up and knows the codebase well. The idea acknowledges this constraint appropriately.

Looking at the novelty, combining information-bottleneck-grounded token scoring with multi-view consistency for VLA robustness is novel, but each component is established. The conceptual progression from prior work like DRIBO and SimPrune feels natural rather than transformative—it's solid incremental work that brings known techniques together in a new configuration, though not groundbreaking.

Actually, reconsidering: the position paper only states the thesis without a concrete method, so ACIBS would be the first concrete VLA instantiation with IB grounding for robustness. The insight that consistency loss implicitly decorrelates from nuisance variables without explicit labels is elegant, and if empirically validated, the finding that post-hoc pruning hurts robustness while trained IB pruning improves it would be a genuine contribution. Still, I'd rate it 3.5—the combination is smart but not surprising given the existing pieces.

On feasibility, the 15-day timeline is extremely tight, and the compact 64-token space creates real risk that pruning may not have enough room to work effectively. SmolVLA's unknown LIBERO-Plus baseline adds uncertainty, and while the compute budget is technically feasible, it's uncomfortably tight.

The progressive submission strategy helps mitigate timeline risk, but the requirement for prior familiarity with SmolVLA, LeRobot, and LIBERO infrastructure is a significant assumption. Juggling multiple simultaneous challenges—implementing the scorer, setting up the dual-view pipeline, adapting FTM, and evaluating on LIBERO-Plus—creates a high probability of missing the deadline.

The formulation itself is clean and well-specified with a concrete loss function and thorough differentiation from related work, though the description is quite long and could be tightened. If the method works, it offers a principled approach to VLA robustness through token-level IB, addressing an important problem with a substantial robustness gap, but there's meaningful execution risk here.

The improvement margin hinges on SmolVLA's baseline robustness, FTM's simplicity makes it an unfavorable comparison against ACIBS's complexity, and relying on simulation-only evaluation limits the impact claims. The core contribution is really about token pruning for robustness rather than a fundamental breakthrough. Averaging the scores puts this at 3.5, below the 4.0 threshold. The idea is fundamentally sound, but the compact token space risk is real and underaddressed, the timeline is extremely aggressive, the novelty is solid but not exceptional, and the FTM baseline risk could be fatal.

Looking back at the previous rounds, this idea has already been substantially refined through four iterations. The remaining concerns are mostly manageable—the missing PDF is minor, the compact token space risk is acknowledged though uncertain, the timeline tension has a progressive strategy to mitigate it, and there's a contingency plan for the FTM baseline. The landscape coverage is comprehensive with 20+ papers cited, the formulation is concrete and well-motivated, and the theoretical grounding is honest about being empirical rather than certified. The progressive submission strategy is pragmatic. Reconsidering the scores more carefully, the novelty is strong as the first concrete VLA instantiation of token reduction for robustness, combining information bottleneck with consistency loss in a novel way.

Feasibility has improved dramatically from Round 1—the current plan with SmolVLA is much more realistic than the original 7B model approach, though the 15-day timeline and untested 64-token pruning regime still present challenges. Clarity is strong with clean formulation and thorough differentiation, though the description could be tighter. Impact is solid given the important problem and principled approach, though simulation-only evaluation and potential FTM dominance are limitations. The average across these dimensions comes to 3.625, which still falls short of 4.0, so I'll recommend revision with targeted feedback to strengthen the weaker areas.

Now I'm noticing some critical gaps in the analysis. There's a missing competitor in the PDF literature on test-time perturbation learning for VLA robustness that should be addressed. The compact token space deserves more rigorous treatment—I need explicit information-theoretic analysis comparing 64 versus 512 tokens per frame. The timeline could be more convincing with concrete milestone breakdowns rather than just the overall 15-day estimate. And there's a significant unknown: whether FTM has actually been adapted to sub-1B models, since prior work tested it on much larger architectures like π0.5. Let me also reconsider the SRPO claim more carefully and re-examine the core idea about how the 64-token compression from 3×3 pixel shuffle interacts with the proposed information bottleneck pruning across different retention rates.

Actually, the idea does address the compact space concern well through the retention rate sweep and the adaptive per-sample mechanism that the KL term provides—that's a genuine strength. And I can verify the architecture claims are correct: SmolVLA does use SigLIP plus SmolLM2, and FocusVLA correctly uses Qwen2.5-0.5B. So the main remaining issues are the missing PDF baseline, the unknown SmolVLA LIBERO-Plus performance, the aggressive timeline, and whether FTM has been validated on such small models. Given this is round 5 of 10 and the idea has improved substantially, I should give targeted feedback on these fixable gaps rather than a hard rejection.

Looking at the scores more carefully: novelty deserves a bump because the core insight—that training a token scorer with information bottleneck and multi-view consistency actually improves robustness, unlike naive post-hoc pruning—is genuinely novel and supported by the counter-evidence papers. The combination of token-level IB, consistency-based nuisance invariance, and differentiable selection applied to VLA robustness is a real contribution. So I'm settling on 3.75 for novelty, which brings the average to 3.69—still a revise, but one where the feedback should be constructive and specific. The feedback points to concrete improvements—adding another paper to the landscape, tightening the token space analysis, checking whether fine-tuning works on smaller models, and potentially running a quick baseline. These are all addressable in a revision. We're at round 5 and the idea has genuinely strengthened over iterations, so I shouldn't be overly critical, but the gap between 3.625 and the 4.0 threshold is real and these revisions should close it. Time to write the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e58b713-5c6b-4283-b905-deb13a53402d",
  "isSidechain": false,
  "requestId": "req_011Cb233nQH8Qst5EwvCPJBz",
  "type": "assistant",
  "uuid": "b0164601-b602-4633-b1cf-6ecd97cb58de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WZz8PQndgVQafLJAQGqiu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1092,
      "cache_read_input_tokens": 69402,
      "output_tokens": 7158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7158,
          "cache_read_input_tokens": 69402,
          "cache_creation_input_tokens": 1092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1092
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

_source line 115 · 2026-05-14T07:07:54.264Z_

I've now completed thorough independent verification across 18+ searches. Let me synthesize my findings.

**Key verification results:**
- SmolVLA architecture (SigLIP + SmolLM2, 450M, 64 tokens via 3×3 pixel shuffle): **CONFIRMED CORRECT**
- FocusVLA (2603.28740): **CORRECTLY CITED** — 512→256 tokens, 98.7% LIBERO, no robustness eval
- CoRL 2026 deadlines (May 26 abstract, May 29 paper): **CONFIRMED**
- SRPO at 82.1% LIBERO-Plus SOTA: **CONFIRMED**
- FTM: 87.1% viewpoint, 4K params on π0.5: **CONFIRMED**
- BC-IB at ICML 2025: **CONFIRMED**
- SimPrune at ICLR 2025: **CONFIRMED**
- TCA at ICCV 2025, 21.4% on CIFAR-100-C: **CONFIRMED**
- Fischer et al. VIB gradient obfuscation: **CONFIRMED**
- Token Reduction Beyond Efficiency (2505.18227): **CONFIRMED**
- Found new concurrent work: **PDF (arXiv 2604.18107)** — test-time perturbation learning for VLA robustness, April 2026

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The combination of token-level IB + multi-view consistency + VLA robustness is genuinely novel — no prior work combines all elements, and it concretely instantiates the thesis of arXiv 2505.18227. However, every individual component (VIB, consistency loss, Gumbel-softmax selection) is standard; the contribution is a well-motivated combination rather than a methodological breakthrough."},
    "feasibility": {"score": 3, "rationale": "The 15-day timeline is extremely aggressive for implementing dual-view augmentation pipeline + Gumbel-softmax scorer + FTM baseline adaptation + LIBERO-Plus evaluation infrastructure simultaneously, even with prior SmolVLA familiarity. More critically, SmolVLA's 64-token space is an untested regime for IB-guided pruning — at k=0.8 only 13 tokens are pruned, and it's unclear whether the IB objective can meaningfully separate task-relevant from irrelevant tokens in such a compact space where each token already carries high information density."},
    "clarity": {"score": 4, "rationale": "The formulation L = L_action + α·D_KL + β·||S(V)-S(V')||² is clean and concrete. Differentiation from 20+ related works is thorough and precise. The progressive submission strategy (MVS vs ideal) is well-articulated. The honest framing of empirical rather than certified robustness is appropriate."},
    "impact": {"score": 3.5, "rationale": "The problem (VLA robustness gap: 95%→<30%) is important and timely for CoRL. However, sim-only evaluation limits impact claims, and FTM's extreme simplicity (4K params, 87.1%) sets a high bar — if FTM adapted to SmolVLA captures most of the robustness gain, ACIBS's added complexity may yield marginal improvement insufficient for a standalone contribution."}
  },
  "issues": [
    "MISSING CONCURRENT WORK: 'Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models' (arXiv 2604.18107, April 2026) proposes a test-time adaptation framework for VLA robustness via uncertainty-based data augmentation and action voting, achieving +7.4% on LIBERO. While it's test-time vs. ACIBS's training-time approach, it represents concurrent work on the same problem (VLA robustness via augmentation-based intervention) and should be cited and differentiated.",
    "SMOLVLA LIBERO-PLUS BASELINE UNKNOWN: The idea's entire framing rests on the '95%→<30% robustness gap,' but SmolVLA (450M params, 64 tokens) has NOT been evaluated on LIBERO-Plus in any published work. SmolVLA's aggressive token compression may already provide different robustness characteristics than larger models — it could be more robust (compression acts as implicit regularization) or less robust (insufficient visual resolution). The first experimental step should be establishing SmolVLA's LIBERO-Plus baseline, and the paper must be prepared for the possibility that SmolVLA's robustness profile doesn't match the narrative.",
    "COMPACT 64-TOKEN PRUNING REGIME REMAINS HIGH-RISK: All existing token pruning methods that demonstrate significant gains operate on 256-1024 token spaces with substantial redundancy (FocusVLA: 512→256, VLA-IAP on OpenVLA/π0 with 256+ tokens). At 64 tokens with 9× pixel-shuffle compression, each token already represents a large spatial region with high information density. The IB objective may not find a meaningful separation between task-relevant and irrelevant tokens — the 'background-dominated tokens' that exist in 512-token spaces may not exist in 64-token spaces where each token covers ~50×50 pixel regions mixing foreground and background. The retention rate sweep is good but doesn't address this fundamental regime difference.",
    "FTM ADAPTATION TO SMOLVLA IS UNTESTED: FTM was validated only on π0.5 (3B+ params, large ViT encoder). SmolVLA uses SigLIP with pixel-shuffle compression, a fundamentally different visual pipeline. The idea plans FTM-SmolVLA as a key baseline but it's unclear whether FTM's global affine transformation will be effective on SmolVLA's already-compressed 64-token representations. This could go either way — FTM might be even more effective (simpler features to modulate) or less effective (insufficient redundancy for affine recalibration). The contingency plan (FTM+ACIBS combination) is good but depends on first successfully adapting FTM.",
    "TIMELINE MILESTONE BREAKDOWN MISSING: The 15-day plan lists components (implement scorer, dual-view pipeline, FTM baseline, LIBERO-Plus eval, paper writing) but doesn't specify which days each component should be completed by. A concrete milestone schedule (days 1-3: SmolVLA LIBERO-Plus baseline + FTM adaptation; days 4-7: ACIBS implementation + initial training; days 8-11: retention rate sweep + ablations; days 12-15: paper writing) would make the feasibility assessment more concrete and help identify the critical path."
  ],
  "feedback": "The idea has matured significantly over 5 rounds — the formulation is clean, the landscape coverage is now exceptional (25+ papers with precise differentiation), and the theoretical framing is appropriately honest. Three targeted fixes to push toward the 4.0 threshold:\n\n1. **ESTABLISH SMOLVLA LIBERO-PLUS BASELINE FIRST (mandatory)**: Before any method development, run SmolVLA on LIBERO-Plus to establish the actual robustness gap for this specific model. If SmolVLA already achieves >60% avg (due to its aggressive compression acting as implicit regularization), the contribution narrative shifts. If it's <30% like larger models, the narrative is confirmed. This baseline run is ~5h and should be the very first experiment. Frame the paper around the ACTUAL measured gap, not the assumed gap from other models.\n\n2. **STRENGTHEN COMPACT TOKEN SPACE ARGUMENT (mandatory)**: Add a concrete analysis comparing information content per token at 64 vs. 512 tokens. Specifically: (a) visualize what spatial regions each of SmolVLA's 64 tokens cover — if each token spans 50×50 pixels mixing object and background, the assumption that 'background-dominated tokens' exist as discrete units may not hold; (b) compute attention entropy over SmolVLA's 64 tokens on LIBERO tasks — if entropy is already low (attention concentrated on few tokens), there's natural room for pruning; if entropy is high (attention spread across all 64), pruning any token loses substantial information; (c) explicitly compare the expected pruning impact: FocusVLA prunes 256 of 512 tokens (50% of tokens, each carrying ~1/512 of spatial info = low info density), while ACIBS at k=0.8 prunes 13 of 64 tokens (20% of tokens, each carrying ~1/64 of spatial info = ~8× higher info density per token). This asymmetry should be the central design consideration, not a secondary acknowledgment.\n\n3. **ADD PDF (arXiv 2604.18107) AND TIGHTEN TIMELINE (recommended)**: Cite the concurrent 'Test-Time Perturbation Learning with Delayed Feedback' paper and differentiate: 'PDF operates at test-time via data augmentation and action voting without model modification, while ACIBS trains a perturbation-invariant token scorer during fine-tuning for zero-overhead inference.' Also add a day-by-day milestone schedule to make the 15-day timeline credible: the critical path is (1) SmolVLA LIBERO-Plus baseline (day 1-2), (2) FTM-SmolVLA adaptation (day 2-3, parallel), (3) ACIBS implementation (day 3-6), (4) training + eval (day 7-11), (5) paper (day 12-15).",
  "reason": "Solid combination of known techniques with clean formulation and exceptional landscape coverage, but the untested compact 64-token pruning regime, unknown SmolVLA LIBERO-Plus baseline, and extremely tight timeline prevent confidence in execution — avg score 3.5/5.0, below the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0164601-b602-4633-b1cf-6ecd97cb58de",
  "isSidechain": false,
  "requestId": "req_011Cb233nQH8Qst5EwvCPJBz",
  "type": "assistant",
  "uuid": "31973ae3-f6d0-4850-bb09-023dde1fd9b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WZz8PQndgVQafLJAQGqiu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1092,
      "cache_read_input_tokens": 69402,
      "output_tokens": 7158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7158,
          "cache_read_input_tokens": 69402,
          "cache_creation_input_tokens": 1092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1092
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

_source line 116_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "31973ae3-f6d0-4850-bb09-023dde1fd9b6",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 117_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 118_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-14 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "31973ae3-f6d0-4850-bb09-023dde1fd9b6",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---

### Runtime record

_source line 119_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify ACIBS VLA robustness via token-level IB and multi-view consistency",
  "sessionId": "d191e023-538e-4ee0-ba64-e2dc7a3a305e"
}
```

---
