# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/4e2e1b29-dee4-426c-8c21-6de856d44d69.jsonl`
- **Structured JSON:** [`4cd9b0b7016e5d8bcd1d.json`](../../sessions/4c/4cd9b0b7016e5d8bcd1d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T05:19:11.672Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T05:19:11.672Z",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **VLA中的token裁剪/增强能否提升VLA模型的泛化性（多从理论角度分析为何能增强）**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"From Representation Compression to Token Selection: Information-Theoretic Generalization Bounds for VLA Visual Token Pruning Under Distribution Shift\",\n  \"core_problem\": \"Recent VLA token pruning methods (LightVLA, OneWM-VLA, GridS, VLA-IAP, VLA-Pruner, EcoVLA, ETA-VLA) empirically demonstrate that aggressive discrete visual token selection improves both efficiency and generalization, yet the theoretical understanding of this phenomenon remains incomplete. BC-IB (Bai et al., ICML 2025) established IB-based generalization bounds for continuous latent compression in lightweight BC architectures, but three critical gaps remain: (1) discrete token selection has fundamentally different mathematical structure than continuous representation compression — it is a combinatorial subset selection problem requiring stochastic relaxation for proper IB treatment, not a variational bottleneck; (2) BC-IB's bounds are i.i.d. and do not address the distribution shift (environment transfer, visual domain change, novel object composition) that defines VLA deployment — where recent benchmarks like LIBERO-Plus show VLA success rates dropping from 95% to below 30% under modest perturbations; (3) BC-IB evaluated only small models (ResNet-18, ViT-S) and explicitly acknowledged not testing VLA-scale architectures, leaving open whether IB-driven compression principles transfer to 3B-7B VLA models where token redundancy patterns differ qualitatively. Meanwhile, the survey 'Token Reduction Should Go Beyond Efficiency' argues token reduction benefits generalization but provides no formal analysis, and the vision token capacity scaling law (Zhuang et al., 2026) characterizes recognition-capacity phase transitions in VLMs but not action-prediction information thresholds in VLAs.\",\n  \"opportunity\": \"The gap between BC-IB's continuous compression theory and the discrete token selection actually used in VLA systems is now tractable to close, thanks to convergence of four developments. First, Kawaguchi et al.'s (ICML 2023) IB generalization framework, already leveraged by BC-IB for i.i.d. bounds, can be combined with PAC-Bayes domain adaptation techniques (Germain et al., ICML 2016) to address covariate shift — complementing the concurrent Causally-Aware IB work (Javidian, 2026) which applies IB to domain adaptation in causal systems but targets tabular data imputation, not visual policy generalization. Second, stochastic relaxations of discrete subset selection (Gumbel Top-k, Drop-Bottleneck) provide a mathematically rigorous bridge between combinatorial token pruning and continuous IB objectives, resolving the formalization subtlety that deterministic selection Z ⊂ X makes I(X;Z) = H(Z). Third, the Latent MI (LMI) approximation method (NeurIPS 2024) makes MI estimation feasible in high-dimensional VLA representations. Fourth — and critically addressing the bound vacuity concern for large models — recent advances in non-vacuous PAC-Bayes bounds for LLMs (SubLoRA at ICML 2024; 'Unlocking Tokens as Data Points' at NeurIPS 2024 Spotlight, achieving non-vacuous bounds for LLaMA2-70B) demonstrate that treating action timesteps as data points and leveraging LoRA's low-rank structure can yield meaningful bounds even at VLA scale. Since LoRA fine-tuning reduces effective learned parameters to ~4-8M (from 7B), the compression requirement for non-vacuous bounds becomes dramatically more achievable. The empirical observation that performance is non-monotonic under extreme compression (1 token/frame works for some tasks but degrades for others) further demands a theoretical explanation that neither BC-IB's monotonic framework nor the recognition-capacity scaling law of Zhuang et al. (2026) provides.\",\n  \"landscape\": \"BC-IB (Bai et al., ICML 2025, arXiv 2502.02853) is the closest prior work: it derives PAC-learning bounds Δ(S) ≤ √[2I(X;Z)+log(2/δ)]/(2n) for IB in robot manipulation BC, tests on LIBERO and CortexBench with small models (ResNet-18, ViT-S, R3M, VC-1), and shows IB reduces I(X;Z) to one-quarter while improving success rate by ~5.5%. However, BC-IB operates on continuous latent compression (variational bottleneck layers), not discrete token selection, and does not address distribution shift or VLA-scale models. **VLA Token Pruning Methods**: LightVLA (ICRA 2026) achieves +2.9% improvement retaining 78/512 tokens via Gumbel-softmax differentiable pruning. OneWM-VLA (arXiv 2605.07931, May 2026) achieves 95.6% on LIBERO-Long with 1 token per frame via Adaptive Attention Pooling. GridS (ICML 2026) preserves geometric details with <10% tokens through grid-based spatial pruning. VLA-IAP (arXiv 2603.22991, Mar 2026) reaches 97.8% on LIBERO with interaction-aligned pruning. SP-VLA (arXiv 2506.12723) introduces joint model scheduling and token pruning addressing temporal redundancy. Compressor-VLA (arXiv 2511.18950) uses instruction-guided compression. VLA-Pruner (arXiv 2511.16449) introduces temporal-aware dual-level pruning combining semantic and action-level token importance. ETA-VLA (arXiv 2603.25766) achieves SOTA on NAVSIM v2 with temporal fusion and intra-LLM sparsification. EcoVLA (arXiv 2602.00780) proposes environment-aware adaptive pruning with interleaved inference orchestration. BFA++ (arXiv 2602.20566) introduces hierarchical best-feature-aware pruning for multi-view VLAs. SpecPrune-VLA (arXiv 2509.05614) combines action-level static and layer-level dynamic pruning. EfficientVLA (arXiv 2506.10100) integrates layer pruning, task-aware token selection, and diffusion caching. **IB Theory and Generalization**: The survey 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues token reduction benefits generalization and hallucination reduction but provides no formal analysis. 'How Much Information Can a Vision Token Hold?' (Zhuang et al., arXiv 2602.02539, 2026) identifies a three-phase transition (Stable/Instability/Collapse) in vision token recognition capacity and derives a probabilistic scaling law Z = w₀ + a·log(V) + α·log(G); this characterizes recognition-capacity limits in VLMs (text/OCR) but does not address action-prediction information thresholds or IB-based analysis. Causally-Aware IB (Javidian, arXiv 2601.04361, 2026) directly combines IB with domain adaptation for covariate shift via Markov Blanket-restricted VIB encoders and proves lossless restriction theorems, but targets tabular/causal-graph data imputation, not visual token selection in policies. CompTrack (AAAI 2026) applies IB-guided token compression to point cloud tracking. IBRO (arXiv 2507.18391) derives token-level IB surrogate objectives for LLM reasoning. InfoPrune frames VLM token pruning as information budgeting but provides no formal bounds. PAC-Bayes IB (ICLR 2022) connects IB with PAC-Bayes generalization bounds via information in weights but does not address token selection. Non-vacuous generalization bounds for LLMs (Lotfi et al., ICML 2024) achieved non-vacuous bounds for ~800M parameter models via SubLoRA compression; 'Unlocking Tokens as Data Points' (Kuang et al., NeurIPS 2024 Spotlight) extended this to LLaMA2-70B by treating each token prediction as a martingale-based data point. Saxe et al. (ICLR 2018) showed emergent compression is not necessary for generalization, but this critique targets emergent compression in hidden layers, not designed compression in VLA token pruning architectures. GIB (arXiv 2509.26327) resolves the ReLU issue by showing synergistic compression is universal across activation functions. IBAC-SNI (NeurIPS 2019) applies IB to RL generalization but not to token-level operations or VLAs. Germain et al. (ICML 2016) established PAC-Bayesian domain adaptation bounds. No existing work derives distribution-shift generalization bounds for discrete token selection in VLA policies, nor provides a principled IB-based framework for token budget selection (k*) in VLAs.\",\n  \"approach\": \"We develop a three-part theoretical and empirical framework extending BC-IB from continuous latent compression to stochastic discrete token selection in VLAs under distribution shift. **Part 1 — Stochastic Token Selection IB Bound**: We address the key formalization subtlety that deterministic subset selection Z ⊂ X makes I(X;Z) = H(Z), which trivializes the IB objective. Instead, we formalize VLA token pruning as a stochastic binary mask process: let M ∈ {0,1}^N be a random binary mask with learned per-token selection probabilities π_i = P(M_i=1|X), and let Z_M = {x_i : M_i=1} be the selected tokens. The IB objective becomes min I(X;M) - β·I(Z_M;Y), where I(X;M) is well-defined for stochastic masks and captures how much information the selection process reveals about the full observation. This aligns naturally with differentiable pruning methods (LightVLA's Gumbel-softmax, VLA-Pruner's dual-level scoring) and can approximate training-free methods (VLA-IAP, EcoVLA) by modeling their attention-threshold selection as soft stochastic masks. We derive a distribution-shift generalization bound by combining Kawaguchi et al.'s (ICML 2023) IB framework with PAC-Bayes domain adaptation bounds (Germain et al., 2016). Critically, to address the well-documented vacuity of PAC-Bayes bounds at overparameterized scale, we exploit two structural properties of the LoRA fine-tuning setting: (a) LoRA reduces effective learned parameters from 7B to ~4-8M, and (b) following Kuang et al. (NeurIPS 2024), we treat each action-prediction timestep as an individual data point (analogous to token-as-data-point for LLMs), vastly increasing effective sample size relative to parameter count. We target non-vacuous bounds within the LoRA-parameterized subspace (where the bound speaks to generalization of the fine-tuning adaptation on the compressed visual representation, not the full pretrained model). If empirical bound evaluation reveals vacuity despite these measures, we have a fallback interpretation: even vacuous absolute bounds yield informative ordinal predictions — the bound's relative ordering across token budgets, pruning strategies, and shift conditions provides a principled ranking framework, analogous to how MDL/compression-based model selection works even when absolute bounds are loose. The domain adaptation component bounds target-domain error by source-domain error plus √[I(X;M)/n_eff] (compression benefit) plus a domain divergence term computed on the masked representation space. Rather than assuming that token pruning reduces domain gap (which would be circular), we derive a testable prediction: IF task-conditioned pruning reduces domain-variant information disproportionately relative to task-relevant information, THEN the divergence term decreases and the generalization gap tightens. This prediction is empirically falsifiable by comparing task-conditioned vs. random pruning. **Part 2 — Phase Transition Analysis**: We derive a critical token budget threshold k* below which I(Z_M;Y) drops sharply (essential action-relevant information is lost), making the bound vacuous despite continued reduction of I(X;M). We distinguish this from the recognition-capacity phase transition of Zhuang et al. (2026), which characterizes how much textual information a vision token can hold (measured by edit distance in OCR tasks) with a latent-difficulty scaling law. Our k* instead characterizes the minimum token budget for preserving action-prediction information, derived from IB theory as the point where the rate-distortion tradeoff between I(X;M) and I(Z_M;Y) transitions from dominated-by-redundancy to dominated-by-information-loss. We characterize k* as a function of task complexity (action space dimensionality, horizon length, spatial precision requirements) and visual redundancy ratio, explaining why k*=1 suffices for simple pick-and-place (OneWM-VLA) but k*≫1 for tasks requiring precise spatial reasoning (GridS). The two phase transition frameworks are complementary: Zhuang et al.'s recognition-capacity limit sets an upper bound on information per token, while our k* sets a lower bound on tokens needed for a given task's action information. **Part 3 — Empirical Validation**: (a) Fine-tune OpenVLA (7B) with LoRA under systematically varied token budgets (1, 4, 8, 16, 32, 64, 128, 256, 512 tokens) on LIBERO-90 (in-distribution) and LIBERO-Plus perturbation suites (distribution shift covering camera viewpoints, object layouts, lighting, textures, robot initial states, and language variation). LIBERO-Plus replaces MetaWorld MT50 as the distribution-shift testbed because it has established OpenVLA baselines, systematic perturbation control, and avoids the non-trivial engineering of integrating OpenVLA 7B with MetaWorld's velocity-based action space. (b) Estimate I(X;M) and I(Z_M;Y) using three complementary approaches: LMI approximation (via learned low-dimensional representations, following NeurIPS 2024), MINE (following BC-IB), and a linear probe surrogate for I(Z_M;Y) (training a linear classifier on Z_M to predict discretized actions). Report all three and measure cross-estimator consistency. (c) Compute the PAC-Bayes bound numerically using SubLoRA-style compression of the LoRA parameters, and report both the absolute bound value (acknowledging it may be vacuous) and the ordinal predictions: (i) whether the bound's ranking across token budgets matches empirical performance ranking, (ii) the predicted phase transition at k ≈ k* vs. empirical performance inflection, and (iii) whether task-conditioned pruning yields tighter bounds than random token selection (testing the domain gap prediction). (d) Empirically characterize (not prove) synergistic information structure in retained tokens using GIB's decomposition, reporting whether retained tokens exhibit higher average interaction information than pruned tokens. (e) Validate the testable prediction on domain gap: compare I_divergence(source, target | task-conditioned pruning) vs. I_divergence(source, target | random pruning) across LIBERO-Plus perturbation types to determine whether task-conditioned pruning indeed preferentially removes domain-variant information.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~300-500h A100 80GB (9 token budgets × LIBERO-90 + LIBERO-Plus perturbation suites × 3 MI estimators × SubLoRA bound computation)\",\n      \"gpu_utilization\": \"Low-moderate (~20-30%): GPUs idle during proof derivation; experiments run in bursts between theory iterations\",\n      \"timeline\": \"4-5 months (theory builds on BC-IB's foundations; key challenges are the stochastic mask IB formalization, domain-shift extension, and SubLoRA bound computation for LoRA-fine-tuned VLAs)\",\n      \"team\": \"1-2 researchers (1 with information theory / learning theory background familiar with PAC-Bayes, IB, and SubLoRA compression bounds; 1 with VLA/robotics experiment experience and LIBERO-Plus setup)\",\n      \"estimated_gpu_cost\": \"$450-750 at ~$1.50/h A100 spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~400-650h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~40-55%): agent runs token-budget sweeps, MI estimation, and SubLoRA bound computation overnight; researcher focuses on stochastic mask IB derivation and phase transition proofs\",\n      \"timeline\": \"2.5-3.5 months (agent handles experiment scheduling, MI estimation pipeline, and bound computation; human drives theory and paper writing)\",\n      \"team\": \"1 researcher, ~45min/day check-in to review MI estimates, verify bound non-vacuity, steer ablation design, and approve LIBERO-Plus perturbation configurations\",\n      \"claude_api_cost\": \"$250-450 (~3000-5000 turns for experiment orchestration, MI estimator debugging, SubLoRA integration, LaTeX drafting, and BC-IB comparison analysis)\",\n      \"estimated_gpu_cost\": \"$600-975 at ~$1.50/h A100 spot pricing\",\n      \"risk_note\": \"Cross-estimator MI consistency may be difficult to achieve in practice; if MINE and LMI diverge substantially, the empirical validation weakens. SubLoRA bound computation for LoRA-fine-tuned VLAs is untested and may require non-trivial adaptation.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~800-1300h A100 80GB (broader sweeps: 9 token budgets × 2 pruning strategies × 3 MI estimators × LIBERO-90 + LIBERO-Plus full perturbation matrix × SubLoRA bound grid search)\",\n      \"gpu_utilization\": \"High (~85-95%): agent queues experiments continuously; near-zero idle time\",\n      \"timeline\": \"2-4 weeks with 4-8 A100s (theory derivation remains the bottleneck; agent can explore bound tightness via numerical verification but the stochastic mask IB proof and phase transition characterization likely require human insight)\",\n      \"team\": \"0 (initial setup: dataset paths, LIBERO-Plus perturbation configs, SubLoRA integration, evaluation scripts, MI estimation pipeline)\",\n      \"claude_api_cost\": \"$600-1000 (~7000-12000 turns for end-to-end exploration, experiment execution, bound computation, analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$1200-1950 at ~$1.50/h A100 spot pricing\",\n      \"speed_bottleneck\": \"GPU count for embarrassingly parallel token-budget sweeps; also limited by whether automated symbolic exploration can derive the stochastic mask phase transition characterization without human mathematical insight\",\n      \"risk_note\": \"SubLoRA-style bound computation for LoRA-fine-tuned VLAs is novel and may require significant engineering; the domain divergence term in the bound may remain loose even with masked representations; the phase transition prediction for k* may not match empirical thresholds across all LIBERO-Plus perturbation types\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (expected deadline: ~September 24, 2026 — primary target, gives ~4 months for theory + experiments)\",\n    \"AAAI 2027 (expected deadline: ~August 2026 — aggressive but feasible backup)\",\n    \"ICRA 2027 (expected deadline: ~September-October 2026 — robotics venue, complements theory with VLA experiments)\",\n    \"NeurIPS 2027 (expected deadline: ~May 2027 — safety net if earlier deadlines are missed)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation [BC-IB] (Bai et al., ICML 2025, arXiv 2502.02853)\",\n    \"How Does Information Bottleneck Help Deep Learning? (Kawaguchi et al., ICML 2023)\",\n    \"On the Information Bottleneck Theory of Deep Learning (Saxe et al., ICLR 2018)\",\n    \"A Generalized Information Bottleneck Theory of Deep Learning [GIB] (arXiv 2509.26327, 2025)\",\n    \"PAC-Bayes Information Bottleneck (Wang et al., ICLR 2022 Spotlight)\",\n    \"Approximating Mutual Information of High-Dimensional Variables Using Learned Representations [LMI] (NeurIPS 2024, arXiv 2409.02732)\",\n    \"Non-Vacuous Generalization Bounds for Large Language Models [SubLoRA] (Lotfi et al., ICML 2024, arXiv 2312.17173)\",\n    \"Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models (Kuang et al., NeurIPS 2024 Spotlight, arXiv 2407.18158)\",\n    \"How Much Information Can a Vision Token Hold? A Scaling Law for Recognition Limits in VLMs (Zhuang et al., arXiv 2602.02539, 2026)\",\n    \"Causally-Aware Information Bottleneck for Domain Adaptation (Javidian, arXiv 2601.04361, 2026)\",\n    \"A New PAC-Bayesian Perspective on Domain Adaptation (Germain et al., ICML 2016)\",\n    \"The Better You Learn, The Smarter You Prune: Towards Efficient VLA Models via Differentiable Token Pruning [LightVLA] (ICRA 2026, arXiv 2509.12594)\",\n    \"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy [OneWM-VLA] (arXiv 2605.07931, 2026)\",\n    \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model [GridS] (ICML 2026)\",\n    \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, 2026)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449, 2025)\",\n    \"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification (arXiv 2603.25766, 2026)\",\n    \"EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration (arXiv 2602.00780, 2026)\",\n    \"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View VLA (arXiv 2602.20566, 2026)\",\n    \"SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614, 2025)\",\n    \"EfficientVLA: Training-Free Acceleration and Compression for VLA Models (arXiv 2506.10100)\",\n    \"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (arXiv 2506.12723)\",\n    \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950, 2025)\",\n    \"Token Reduction Should Go Beyond Efficiency in Generative Models (arXiv 2505.18227, 2025)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\",\n    \"CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking (AAAI 2026)\",\n    \"Revisiting LLM Reasoning via Information Bottleneck [IBRO] (arXiv 2507.18391, 2025)\",\n    \"Generalization in Reinforcement Learning with Selective Noise Injection and Information Bottleneck [IBAC-SNI] (NeurIPS 2019)\",\n    \"Drop-Bottleneck: Learning Discrete Compressed Representation for Noise-Robust Exploration (arXiv 2103.12300)\"\n  ],\n  \"description\": \"We extend BC-IB's (ICML 2025) Information Bottleneck theory from continuous latent compression in lightweight BC architectures to stochastic discrete visual token selection in VLA policies under distribution shift — addressing three gaps that BC-IB explicitly left open. First, we resolve the formalization subtlety that deterministic token selection trivializes the IB objective by modeling VLA token pruning as a stochastic binary mask process (aligning with Gumbel-softmax methods like LightVLA), and derive distribution-shift generalization bounds by combining Kawaguchi et al.'s (ICML 2023) IB framework with PAC-Bayes domain adaptation techniques (Germain et al., 2016). To address the well-documented vacuity of PAC-Bayes bounds at overparameterized scale, we exploit LoRA fine-tuning's low effective parameter count (~4-8M vs 7B) and treat action timesteps as individual data points following Kuang et al.'s (NeurIPS 2024 Spotlight) martingale approach, targeting non-vacuous bounds within the LoRA-parameterized subspace. Rather than assuming task-conditioned pruning reduces domain gap (which would be circular), we derive a testable prediction: the bound predicts that generalization improves if and only if pruning disproportionately removes domain-variant over task-relevant information — empirically falsifiable by comparing task-conditioned vs. random pruning on LIBERO-Plus perturbation suites. Second, we derive a phase transition analysis characterizing the critical token budget k* below which I(Z_M;Y) collapses, complementing (not duplicating) Zhuang et al.'s (2026) recognition-capacity phase transition: theirs characterizes information capacity per token for recognition; ours characterizes minimum tokens for action-prediction information, derived from IB rate-distortion theory and parametrized by task complexity, explaining why k*=1 suffices for simple manipulation but k*≫1 for spatial reasoning tasks. Third, we validate at VLA scale (OpenVLA 7B with LoRA) on LIBERO-90 (in-distribution) and LIBERO-Plus (distribution shift across camera viewpoints, object layouts, lighting, textures, robot states, and language), using three MI estimation approaches (LMI, MINE, linear probe surrogates), computing the PAC-Bayes bound numerically via SubLoRA-style LoRA compression, and reporting both absolute bound values and ordinal predictions. This work addresses the Saxe et al. (ICLR 2018) critique by noting VLA token pruning is designed compression, not emergent compression. The result provides VLA token compression with distribution-shift-aware theoretical grounding, principled token budget selection via k*, and a falsifiable framework for evaluating whether any given pruning strategy improves generalization under shift.\",\n  \"project_name\": \"ib_vla_token_theory\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL OMISSION: BC-IB (Bai et al., 'Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation', ICML 2025, arXiv 2502.02853) already derives PAC-learning generalization bounds (Δ(S) ≤ √[2I(X;Z) + log(2/δ)] / 2n) for IB in robot manipulation behavior cloning, tests on LIBERO, and shows IB reduces I(X;Z) to one-quarter while improving success rate by 7.7%. The Generator's claim that 'no formal theoretical framework explains why compressing visual representations improves action prediction' is factually incorrect — BC-IB does exactly this, albeit for lightweight architectures rather than VLAs.\", \"IB theory has known fundamental limitations: Saxe et al. (ICLR 2018) demonstrated that compression is not necessary for generalization, that the compression phase depends on activation function choice (tanh vs ReLU), and that there is no causal connection between compression and generalization. The proposal does not address how its IB-based framework handles these critiques, which are well-established in the community.\", \"The GIB synergy claim ('token pruning preferentially retains multi-token synergistic features over redundant single-token features') is stated as something to be 'proved' but the proposal provides no sketch of how this proof would work. GIB (arXiv 2509.26327) defines synergy via average interaction information — connecting this to discrete token selection in a VLA is a non-trivial formal challenge with no clear path forward.\", \"MI estimation feasibility: Estimating I(X;Z) and I(Z;Y) in 7B-parameter VLA representations is extremely challenging. Recent work (arXiv 2506.00330, June 2025) confirms that 'accurate estimation of mutual information from finite data remains notoriously difficult' and 'common approaches fail in high-dimensional, undersampled regimes.' The proposal's empirical validation critically depends on reliable MI estimates that may not be obtainable.\", \"Non-monotonic generalization risk: OneWM-VLA shows 1 token/frame works well, but the IB framework predicts monotonic improvement with compression (less I(X;Z) → tighter bound). If empirical generalization is non-monotonic at very low token counts (which is plausible — at some point critical task info is lost), the theoretical bound fails to explain the most interesting empirical phenomenon.\", \"CoRL 2026 deadline (May 29, 2026) is 16 days from today — impossible for a theory paper that requires theorem derivation, proof verification, and systematic experiments. This venue should be removed.\", \"BC-IB (ICML 2025) explicitly acknowledges it did not evaluate VLA-scale models — while this leaves a gap, it also signals that the reviewers of this proposed paper will immediately ask 'how is this different from BC-IB?' and the answer ('we extend to VLAs and token-level pruning') may feel incremental to theory reviewers at top venues.\"]\nFeedback: The idea has a sound intuition but needs significant repositioning given BC-IB (ICML 2025). Specific recommendations:\n\n1. **Acknowledge and differentiate from BC-IB**: This is the most urgent issue. BC-IB must be cited as the closest prior work, and the contribution must be clearly positioned as extending BC-IB in three specific ways: (a) from latent representation compression to discrete token selection/pruning, (b) from lightweight BC architectures to 7B+ VLA models, (c) from i.i.d. generalization to distribution-shift bounds in sequential decision-making. Frame the paper as 'from representation compression to token selection: scaling IB theory to VLA policies.'\n\n2. **Address Saxe et al. criticisms head-on**: Include a section discussing why IB theory is still applicable despite the known criticisms. Argue that in the VLA token-pruning setting, compression is explicitly designed (not emergent), so the Saxe et al. critique about emergent compression not being necessary does not directly apply. This is a defensible argument but must be made explicitly.\n\n3. **Drop or weaken the GIB synergy claims** unless you have a concrete proof sketch. The synergy decomposition is the most speculative part — consider making it an empirical observation rather than a theoretical contribution.\n\n4. **Address MI estimation** by: (a) using multiple MI estimators and showing consistency, (b) using proxy metrics (e.g., linear probe accuracy as a surrogate for I(Z;Y)), (c) focusing on relative trends rather than absolute MI values to validate bound predictions.\n\n5. **Remove CoRL 2026** from target venues. Target ICLR 2027 (Sep 24, 2026) as the primary venue — this gives ~4 months, which is realistic for a team with strong theory background.\n\n6. **Reframe contribution**: Rather than 'the first formal IB theory for VLA token compression' (which BC-IB partially invalidates), position as 'the first IB-based generalization theory that explains why discrete token pruning specifically (not just representation compression) improves VLA policy robustness under domain shift — extending BC-IB to the token selection regime and VLA scale.'\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSING RELATED WORK — 'How Much Information Can a Vision Token Hold? A Scaling Law for Recognition Limits in VLMs' (arXiv 2602.02539, Feb 2026) already identifies a three-phase transition (Stable/Instability/Collapse) in vision token capacity and derives a probabilistic scaling law. While targeting VLMs for recognition rather than VLAs for action prediction, this directly overlaps with the proposed 'phase transition analysis' in Part 2. The proposal must cite this work and clearly differentiate its phase transition characterization (IB-based k* for action prediction) from this recognition-capacity phase transition.\", \"MISSING RELATED WORK — 'Causally-Aware Information Bottleneck for Domain Adaptation' (arXiv 2601.04361, Jan 2026) directly combines Information Bottleneck with domain adaptation for handling covariate shift, including a Variational IB encoder for high-dimensional data. This is a core theoretical building block of the proposal and must be cited and differentiated from.\", \"VACUOUS BOUNDS AT SCALE — PAC-Bayes generalization bounds are well-documented to be vacuous (trivially ≥1) for overparameterized deep networks. Recent work confirms that 'empirically, PAC-Bayes certificates are never tighter than frequentist test-set bounds.' For a 7B-parameter VLA, the proposed bound combining PAC-Bayes + IB + domain divergence will almost certainly be numerically uninformative. The proposal must honestly acknowledge this limitation and reframe the theoretical contribution — either focus on relative trends and ordinal predictions (which weakens the 'bound' framing), or target non-vacuous bounds using data-dependent priors (which adds significant complexity).\", \"DISCRETE IB FORMALIZATION SUBTLETY — When Z ⊂ X is a deterministic subset selection, I(X;Z) has specific mathematical properties that differ from the continuous variational bottleneck in BC-IB. If Z is a deterministic function of a selection mask, I(X;Z) = H(Z) since Z is perfectly determined by X. The proposal needs a careful formalization — either through stochastic selection (Gumbel-softmax relaxation as in LightVLA) or by redefining the IB objective for the discrete case (e.g., via the selected token indices rather than the token values). This mathematical subtlety is not addressed.\", \"CIRCULAR REASONING RISK in domain gap reduction claim — The theoretical argument that 'task-conditioned token pruning tightens the bound by reducing the effective domain gap' assumes that pruned tokens disproportionately carry domain-specific information. But this is the very claim the theory should derive/prove, not assume. If this is an assumption, the bound's applicability is conditional on a property that must be verified empirically for each pruning method, which weakens the theoretical generality.\", \"MINOR FACTUAL ERROR — LightVLA achieves +2.6% improvement on LIBERO per the actual paper (arXiv 2509.12594), not +2.9% as stated. The token retention number (78/512) should be verified.\", \"ADDITIONAL MISSING VLA TOKEN PRUNING WORKS — Several concurrent VLA pruning methods are not cited: VLA-Pruner (arXiv 2511.16449, temporal-aware dual-level pruning), ETA-VLA (arXiv 2603.25766, temporal fusion + sparsification), EcoVLA (arXiv 2602.00780, environment-aware adaptive pruning). While primarily engineering papers, they represent the complete competitive landscape and reviewers will expect them.\", \"METAWORLD MT50 FEASIBILITY — No published work demonstrates OpenVLA 7B fine-tuning and evaluation on MetaWorld MT50. The OneWM-VLA result (47.9%→61.3% on MT50) uses a 2B backbone. Integrating OpenVLA 7B with MetaWorld MT50 may require non-trivial engineering effort not accounted for in the timeline.\"]\nFeedback: The revision meaningfully addressed Round 1 feedback — BC-IB differentiation is now clear, Saxe et al. is handled well, GIB synergy is properly scoped as empirical, and MI estimation uses multiple approaches. However, several issues remain that must be resolved for top-venue quality:\n\n1. **Acknowledge bound vacuity honestly**: This is the most critical theoretical issue. Add a subsection explicitly discussing that PAC-Bayes bounds at VLA scale will likely be vacuous in absolute terms, and reposition the theoretical contribution as providing (a) ordinal predictions about when pruning helps/hurts generalization, (b) a principled framework for token budget selection via k*, and (c) qualitative insights about the relationship between compression and domain gap — rather than claiming numerically tight bounds. This is defensible and honest; claiming tight bounds at 7B scale would be immediately challenged by reviewers familiar with PAC-Bayes literature.\n\n2. **Fix the discrete IB formalization**: Address the mathematical subtlety that deterministic subset selection Z ⊂ X makes I(X;Z) = H(Z). Consider two approaches: (a) model token selection as a stochastic process (aligning with differentiable pruning methods like LightVLA's Gumbel-softmax), or (b) reformulate using the selection mask M as the bottleneck variable, where I(X;M) captures how much information about the full observation the mask reveals. This is a solvable issue but must be addressed explicitly.\n\n3. **Cite and differentiate from arXiv 2602.02539**: The phase transition in vision token capacity (Stable/Instability/Collapse) is already documented for VLMs. Your k* analysis should be positioned as complementary — theirs characterizes recognition capacity limits, yours characterizes action-prediction information thresholds via IB theory, which additionally predicts how k* varies with task complexity.\n\n4. **Address the circularity in domain gap reduction**: Either (a) prove that task-conditioned pruning preferentially removes domain-variant tokens (which would require assumptions about the data distribution structure), or (b) make this an empirically testable prediction of the theory rather than an assumption. Option (b) is more honest: 'our bound predicts that if pruning reduces domain-variant information disproportionately, the generalization gap will tighten; we empirically verify this by comparing task-conditioned vs. random pruning.'\n\n5. **Add missing citations**: arXiv 2602.02539, arXiv 2601.04361, VLA-Pruner, ETA-VLA, EcoVLA. Fix the LightVLA accuracy (+2.6%, not +2.9%).\n\n6. **De-risk MetaWorld MT50**: Either verify that OpenVLA 7B can be fine-tuned on MetaWorld MT50 (check if the observation/action spaces are compatible with OpenVLA's architecture), or replace with LIBERO-90 cross-suite transfer as the primary distribution-shift testbed, which has established OpenVLA baselines.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING RELATED WORK — DTP (Distracting Token Pruning, arXiv 2601.16065, Jan 2026) explicitly demonstrates that pruning 'distracting' tokens (task-irrelevant visual tokens) improves VLA task success rates, finding a negative correlation between attention to task-irrelevant regions and success rate. This provides direct empirical support for the proposal's thesis and should be cited as motivation. FocusVLA (arXiv 2603.28740, Mar 2026) similarly identifies 'attention over-smoothing' and 'token count bloat' as failure modes, showing that attention-focusing on task-relevant tokens improves both performance and convergence.\", \"MISSING RELATED WORK — SemanticVLA (arXiv 2511.10518, AAAI 2026 Oral) achieves SOTA 97.7% on LIBERO with semantic-aligned sparsification, reducing FLOPs by 3-4x. This is a highly cited VLA pruning method at a top venue that should be included in the landscape.\", \"MISSING RELATED WORK — IB-FT (arXiv 2510.16022, Oct 2025) applies IB penalties during LLM fine-tuning to break 'memorization barriers' and improve generalization. While targeting code rather than VLAs, this directly validates the IB-for-fine-tuning-generalization thesis and shares the core mechanism (IB on representations during fine-tuning). Should be cited as a parallel direction.\", \"BOUND VACUITY REMAINS THE CENTRAL WEAKNESS — The proposal now honestly acknowledges that PAC-Bayes bounds will likely be vacuous and proposes 'ordinal predictions' as fallback. However, this fundamentally changes the nature of the contribution: ordinal predictions from a vacuous bound are not theoretically guaranteed to be meaningful — a bound that is ≥1 provides no formal guarantee about ranking either. The CMU blog post on PAC-Bayes for foundation models shows tight bounds are achievable in structured discrete spaces (prompt engineering), but the VLA LoRA setting is far less structured. The proposal should more carefully argue why ordinal predictions from a vacuous bound would be informative, potentially drawing on compression-based model selection literature (MDL principle) rather than claiming the bound itself provides ordinal guarantees.\", \"THE THEORETICAL CONTRIBUTION MAY NOT SATISFY THE USER'S REQUEST — The user asked for theoretical analysis of 'why token pruning enhances VLA generalization' (从理论角度分析为何能增强). A vacuous bound with ordinal fallback does not provide a convincing theoretical 'why' — it provides a framework that may or may not predict empirical trends. The most convincing theoretical contribution would be the qualitative insight that stochastic mask-based pruning reduces I(X;M) which tightens the generalization bound, plus the phase transition k* characterization. But if bounds are vacuous, the connection from 'IB reduces I(X;M)' to 'generalization improves' becomes an empirical correlation rather than a theoretical guarantee.\", \"PHASE TRANSITION k* ANALYSIS — While positioned as complementary to Zhuang et al. (2026), the k* characterization may be empirically difficult to validate. The proposal claims k* depends on 'task complexity (action space dimensionality, horizon length, spatial precision requirements) and visual redundancy ratio,' but deriving a closed-form expression for k* as a function of these variables is a significant theoretical challenge. If k* can only be estimated empirically per-task, the theoretical contribution reduces to 'there exists a phase transition' (which is already observable from the empirical literature — OneWM-VLA's k*=1 success vs. GridS's need for more tokens).\", \"MINOR: LightVLA improvement is stated as +2.9% in the landscape section but Round 2 feedback requested correction to +2.6%. The proposal description mentions aligning with LightVLA's Gumbel-softmax but the landscape section still states +2.9%.\", \"MINOR: The proposal cites an enormous number of VLA pruning methods (15+) which is comprehensive but risks giving reviewers the impression that token pruning is already a saturated empirical area — the theoretical contribution must be strong enough to stand on its own rather than seeming like an afterthought to the empirical VLA pruning wave.\"]\nFeedback: The proposal has improved substantially across two rounds of revision. The BC-IB differentiation is now clear and well-articulated, the stochastic binary mask formalization resolves the discrete IB subtlety, the circularity in domain gap reduction is addressed via falsifiable predictions, and the honest acknowledgment of bound vacuity is appropriate. However, several issues need attention for a top-venue pass:\n\n1. **Strengthen the theoretical 'why' narrative**: The user specifically asked for theoretical analysis of why token pruning enhances generalization. The current framing risks delivering 'a framework that might predict trends' rather than 'a theoretical explanation.' Consider restructuring: (a) Lead with the qualitative IB insight — task-conditioned pruning removes domain-variant visual information disproportionately, which reduces the effective distribution shift seen by the policy; (b) Use the stochastic mask IB bound to formalize this insight; (c) Use the k* phase transition to explain the non-monotonicity; (d) Treat the PAC-Bayes bound computation as validation of the framework rather than the core contribution. This reframing makes the theory more resilient to bound vacuity.\n\n2. **Address the ordinal prediction gap**: A vacuous PAC-Bayes bound does not formally guarantee meaningful ordinal predictions. Either (a) cite MDL/minimum description length literature to justify that compression-based rankings are informative even when absolute bounds are loose (Grünwald's MDL principle), or (b) prove a separate result showing that the bound's relative ordering is preserved under certain conditions even when absolute values are vacuous. Without this, the fallback is ad hoc.\n\n3. **Add missing citations**: DTP (arXiv 2601.16065), FocusVLA (arXiv 2603.28740), SemanticVLA (arXiv 2511.10518, AAAI 2026 Oral), and IB-FT (arXiv 2510.16022). These strengthen the empirical motivation and show the theoretical gap is real — many methods work empirically but none explain why.\n\n4. **Fix LightVLA accuracy**: Landscape section still states +2.9%, should be +2.6%.\n\n5. **Sharpen the k* contribution**: Either (a) provide a concrete analytical form for k* (even under simplifying assumptions like linear policy, Gaussian observations) to show the phase transition can be characterized theoretically, or (b) explicitly frame k* estimation as an empirical method guided by IB theory rather than a closed-form theoretical result. The latter is more honest and still valuable.\n\n6. **Consider scope narrowing**: The proposal tries to deliver too many things (stochastic IB bound + distribution shift extension + k* phase transition + GIB synergy characterization + SubLoRA bound computation + three MI estimators + LIBERO-Plus validation). For a 4-month timeline targeting ICLR 2027, consider dropping or deprioritizing the GIB synergy characterization and reducing MI estimators to two (LMI + linear probe). This focuses the paper on the strongest contributions: the stochastic mask IB formalization, the domain-shift bound, and the k* phase transition.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T05:19:11.678Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T05:19:11.678Z",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-13T05:19:11.714Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-13 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **VLA中的token裁剪/增强能否提升VLA模型的泛化性（多从理论角度分析为何能增强）**
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
  "title": "From Representation Compression to Token Selection: Information-Theoretic Generalization Bounds for VLA Visual Token Pruning Under Distribution Shift",
  "core_problem": "Recent VLA token pruning methods (LightVLA, OneWM-VLA, GridS, VLA-IAP, VLA-Pruner, EcoVLA, ETA-VLA) empirically demonstrate that aggressive discrete visual token selection improves both efficiency and generalization, yet the theoretical understanding of this phenomenon remains incomplete. BC-IB (Bai et al., ICML 2025) established IB-based generalization bounds for continuous latent compression in lightweight BC architectures, but three critical gaps remain: (1) discrete token selection has fundamentally different mathematical structure than continuous representation compression — it is a combinatorial subset selection problem requiring stochastic relaxation for proper IB treatment, not a variational bottleneck; (2) BC-IB's bounds are i.i.d. and do not address the distribution shift (environment transfer, visual domain change, novel object composition) that defines VLA deployment — where recent benchmarks like LIBERO-Plus show VLA success rates dropping from 95% to below 30% under modest perturbations; (3) BC-IB evaluated only small models (ResNet-18, ViT-S) and explicitly acknowledged not testing VLA-scale architectures, leaving open whether IB-driven compression principles transfer to 3B-7B VLA models where token redundancy patterns differ qualitatively. Meanwhile, the survey 'Token Reduction Should Go Beyond Efficiency' argues token reduction benefits generalization but provides no formal analysis, and the vision token capacity scaling law (Zhuang et al., 2026) characterizes recognition-capacity phase transitions in VLMs but not action-prediction information thresholds in VLAs.",
  "opportunity": "The gap between BC-IB's continuous compression theory and the discrete token selection actually used in VLA systems is now tractable to close, thanks to convergence of four developments. First, Kawaguchi et al.'s (ICML 2023) IB generalization framework, already leveraged by BC-IB for i.i.d. bounds, can be combined with PAC-Bayes domain adaptation techniques (Germain et al., ICML 2016) to address covariate shift — complementing the concurrent Causally-Aware IB work (Javidian, 2026) which applies IB to domain adaptation in causal systems but targets tabular data imputation, not visual policy generalization. Second, stochastic relaxations of discrete subset selection (Gumbel Top-k, Drop-Bottleneck) provide a mathematically rigorous bridge between combinatorial token pruning and continuous IB objectives, resolving the formalization subtlety that deterministic selection Z ⊂ X makes I(X;Z) = H(Z). Third, the Latent MI (LMI) approximation method (NeurIPS 2024) makes MI estimation feasible in high-dimensional VLA representations. Fourth — and critically addressing the bound vacuity concern for large models — recent advances in non-vacuous PAC-Bayes bounds for LLMs (SubLoRA at ICML 2024; 'Unlocking Tokens as Data Points' at NeurIPS 2024 Spotlight, achieving non-vacuous bounds for LLaMA2-70B) demonstrate that treating action timesteps as data points and leveraging LoRA's low-rank structure can yield meaningful bounds even at VLA scale. Since LoRA fine-tuning reduces effective learned parameters to ~4-8M (from 7B), the compression requirement for non-vacuous bounds becomes dramatically more achievable. The empirical observation that performance is non-monotonic under extreme compression (1 token/frame works for some tasks but degrades for others) further demands a theoretical explanation that neither BC-IB's monotonic framework nor the recognition-capacity scaling law of Zhuang et al. (2026) provides.",
  "landscape": "BC-IB (Bai et al., ICML 2025, arXiv 2502.02853) is the closest prior work: it derives PAC-learning bounds Δ(S) ≤ √[2I(X;Z)+log(2/δ)]/(2n) for IB in robot manipulation BC, tests on LIBERO and CortexBench with small models (ResNet-18, ViT-S, R3M, VC-1), and shows IB reduces I(X;Z) to one-quarter while improving success rate by ~5.5%. However, BC-IB operates on continuous latent compression (variational bottleneck layers), not discrete token selection, and does not address distribution shift or VLA-scale models. **VLA Token Pruning Methods**: LightVLA (ICRA 2026) achieves +2.9% improvement retaining 78/512 tokens via Gumbel-softmax differentiable pruning. OneWM-VLA (arXiv 2605.07931, May 2026) achieves 95.6% on LIBERO-Long with 1 token per frame via Adaptive Attention Pooling. GridS (ICML 2026) preserves geometric details with <10% tokens through grid-based spatial pruning. VLA-IAP (arXiv 2603.22991, Mar 2026) reaches 97.8% on LIBERO with interaction-aligned pruning. SP-VLA (arXiv 2506.12723) introduces joint model scheduling and token pruning addressing temporal redundancy. Compressor-VLA (arXiv 2511.18950) uses instruction-guided compression. VLA-Pruner (arXiv 2511.16449) introduces temporal-aware dual-level pruning combining semantic and action-level token importance. ETA-VLA (arXiv 2603.25766) achieves SOTA on NAVSIM v2 with temporal fusion and intra-LLM sparsification. EcoVLA (arXiv 2602.00780) proposes environment-aware adaptive pruning with interleaved inference orchestration. BFA++ (arXiv 2602.20566) introduces hierarchical best-feature-aware pruning for multi-view VLAs. SpecPrune-VLA (arXiv 2509.05614) combines action-level static and layer-level dynamic pruning. EfficientVLA (arXiv 2506.10100) integrates layer pruning, task-aware token selection, and diffusion caching. **IB Theory and Generalization**: The survey 'Token Reduction Should Go Beyond Efficiency' (arXiv 2505.18227) argues token reduction benefits generalization and hallucination reduction but provides no formal analysis. 'How Much Information Can a Vision Token Hold?' (Zhuang et al., arXiv 2602.02539, 2026) identifies a three-phase transition (Stable/Instability/Collapse) in vision token recognition capacity and derives a probabilistic scaling law Z = w₀ + a·log(V) + α·log(G); this characterizes recognition-capacity limits in VLMs (text/OCR) but does not address action-prediction information thresholds or IB-based analysis. Causally-Aware IB (Javidian, arXiv 2601.04361, 2026) directly combines IB with domain adaptation for covariate shift via Markov Blanket-restricted VIB encoders and proves lossless restriction theorems, but targets tabular/causal-graph data imputation, not visual token selection in policies. CompTrack (AAAI 2026) applies IB-guided token compression to point cloud tracking. IBRO (arXiv 2507.18391) derives token-level IB surrogate objectives for LLM reasoning. InfoPrune frames VLM token pruning as information budgeting but provides no formal bounds. PAC-Bayes IB (ICLR 2022) connects IB with PAC-Bayes generalization bounds via information in weights but does not address token selection. Non-vacuous generalization bounds for LLMs (Lotfi et al., ICML 2024) achieved non-vacuous bounds for ~800M parameter models via SubLoRA compression; 'Unlocking Tokens as Data Points' (Kuang et al., NeurIPS 2024 Spotlight) extended this to LLaMA2-70B by treating each token prediction as a martingale-based data point. Saxe et al. (ICLR 2018) showed emergent compression is not necessary for generalization, but this critique targets emergent compression in hidden layers, not designed compression in VLA token pruning architectures. GIB (arXiv 2509.26327) resolves the ReLU issue by showing synergistic compression is universal across activation functions. IBAC-SNI (NeurIPS 2019) applies IB to RL generalization but not to token-level operations or VLAs. Germain et al. (ICML 2016) established PAC-Bayesian domain adaptation bounds. No existing work derives distribution-shift generalization bounds for discrete token selection in VLA policies, nor provides a principled IB-based framework for token budget selection (k*) in VLAs.",
  "approach": "We develop a three-part theoretical and empirical framework extending BC-IB from continuous latent compression to stochastic discrete token selection in VLAs under distribution shift. **Part 1 — Stochastic Token Selection IB Bound**: We address the key formalization subtlety that deterministic subset selection Z ⊂ X makes I(X;Z) = H(Z), which trivializes the IB objective. Instead, we formalize VLA token pruning as a stochastic binary mask process: let M ∈ {0,1}^N be a random binary mask with learned per-token selection probabilities π_i = P(M_i=1|X), and let Z_M = {x_i : M_i=1} be the selected tokens. The IB objective becomes min I(X;M) - β·I(Z_M;Y), where I(X;M) is well-defined for stochastic masks and captures how much information the selection process reveals about the full observation. This aligns naturally with differentiable pruning methods (LightVLA's Gumbel-softmax, VLA-Pruner's dual-level scoring) and can approximate training-free methods (VLA-IAP, EcoVLA) by modeling their attention-threshold selection as soft stochastic masks. We derive a distribution-shift generalization bound by combining Kawaguchi et al.'s (ICML 2023) IB framework with PAC-Bayes domain adaptation bounds (Germain et al., 2016). Critically, to address the well-documented vacuity of PAC-Bayes bounds at overparameterized scale, we exploit two structural properties of the LoRA fine-tuning setting: (a) LoRA reduces effective learned parameters from 7B to ~4-8M, and (b) following Kuang et al. (NeurIPS 2024), we treat each action-prediction timestep as an individual data point (analogous to token-as-data-point for LLMs), vastly increasing effective sample size relative to parameter count. We target non-vacuous bounds within the LoRA-parameterized subspace (where the bound speaks to generalization of the fine-tuning adaptation on the compressed visual representation, not the full pretrained model). If empirical bound evaluation reveals vacuity despite these measures, we have a fallback interpretation: even vacuous absolute bounds yield informative ordinal predictions — the bound's relative ordering across token budgets, pruning strategies, and shift conditions provides a principled ranking framework, analogous to how MDL/compression-based model selection works even when absolute bounds are loose. The domain adaptation component bounds target-domain error by source-domain error plus √[I(X;M)/n_eff] (compression benefit) plus a domain divergence term computed on the masked representation space. Rather than assuming that token pruning reduces domain gap (which would be circular), we derive a testable prediction: IF task-conditioned pruning reduces domain-variant information disproportionately relative to task-relevant information, THEN the divergence term decreases and the generalization gap tightens. This prediction is empirically falsifiable by comparing task-conditioned vs. random pruning. **Part 2 — Phase Transition Analysis**: We derive a critical token budget threshold k* below which I(Z_M;Y) drops sharply (essential action-relevant information is lost), making the bound vacuous despite continued reduction of I(X;M). We distinguish this from the recognition-capacity phase transition of Zhuang et al. (2026), which characterizes how much textual information a vision token can hold (measured by edit distance in OCR tasks) with a latent-difficulty scaling law. Our k* instead characterizes the minimum token budget for preserving action-prediction information, derived from IB theory as the point where the rate-distortion tradeoff between I(X;M) and I(Z_M;Y) transitions from dominated-by-redundancy to dominated-by-information-loss. We characterize k* as a function of task complexity (action space dimensionality, horizon length, spatial precision requirements) and visual redundancy ratio, explaining why k*=1 suffices for simple pick-and-place (OneWM-VLA) but k*≫1 for tasks requiring precise spatial reasoning (GridS). The two phase transition frameworks are complementary: Zhuang et al.'s recognition-capacity limit sets an upper bound on information per token, while our k* sets a lower bound on tokens needed for a given task's action information. **Part 3 — Empirical Validation**: (a) Fine-tune OpenVLA (7B) with LoRA under systematically varied token budgets (1, 4, 8, 16, 32, 64, 128, 256, 512 tokens) on LIBERO-90 (in-distribution) and LIBERO-Plus perturbation suites (distribution shift covering camera viewpoints, object layouts, lighting, textures, robot initial states, and language variation). LIBERO-Plus replaces MetaWorld MT50 as the distribution-shift testbed because it has established OpenVLA baselines, systematic perturbation control, and avoids the non-trivial engineering of integrating OpenVLA 7B with MetaWorld's velocity-based action space. (b) Estimate I(X;M) and I(Z_M;Y) using three complementary approaches: LMI approximation (via learned low-dimensional representations, following NeurIPS 2024), MINE (following BC-IB), and a linear probe surrogate for I(Z_M;Y) (training a linear classifier on Z_M to predict discretized actions). Report all three and measure cross-estimator consistency. (c) Compute the PAC-Bayes bound numerically using SubLoRA-style compression of the LoRA parameters, and report both the absolute bound value (acknowledging it may be vacuous) and the ordinal predictions: (i) whether the bound's ranking across token budgets matches empirical performance ranking, (ii) the predicted phase transition at k ≈ k* vs. empirical performance inflection, and (iii) whether task-conditioned pruning yields tighter bounds than random token selection (testing the domain gap prediction). (d) Empirically characterize (not prove) synergistic information structure in retained tokens using GIB's decomposition, reporting whether retained tokens exhibit higher average interaction information than pruned tokens. (e) Validate the testable prediction on domain gap: compare I_divergence(source, target | task-conditioned pruning) vs. I_divergence(source, target | random pruning) across LIBERO-Plus perturbation types to determine whether task-conditioned pruning indeed preferentially removes domain-variant information.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~300-500h A100 80GB (9 token budgets × LIBERO-90 + LIBERO-Plus perturbation suites × 3 MI estimators × SubLoRA bound computation)",
      "gpu_utilization": "Low-moderate (~20-30%): GPUs idle during proof derivation; experiments run in bursts between theory iterations",
      "timeline": "4-5 months (theory builds on BC-IB's foundations; key challenges are the stochastic mask IB formalization, domain-shift extension, and SubLoRA bound computation for LoRA-fine-tuned VLAs)",
      "team": "1-2 researchers (1 with information theory / learning theory background familiar with PAC-Bayes, IB, and SubLoRA compression bounds; 1 with VLA/robotics experiment experience and LIBERO-Plus setup)",
      "estimated_gpu_cost": "$450-750 at ~$1.50/h A100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "~400-650h A100 80GB",
      "gpu_utilization": "Moderate (~40-55%): agent runs token-budget sweeps, MI estimation, and SubLoRA bound computation overnight; researcher focuses on stochastic mask IB derivation and phase transition proofs",
      "timeline": "2.5-3.5 months (agent handles experiment scheduling, MI estimation pipeline, and bound computation; human drives theory and paper writing)",
      "team": "1 researcher, ~45min/day check-in to review MI estimates, verify bound non-vacuity, steer ablation design, and approve LIBERO-Plus perturbation configurations",
      "claude_api_cost": "$250-450 (~3000-5000 turns for experiment orchestration, MI estimator debugging, SubLoRA integration, LaTeX drafting, and BC-IB comparison analysis)",
      "estimated_gpu_cost": "$600-975 at ~$1.50/h A100 spot pricing",
      "risk_note": "Cross-estimator MI consistency may be difficult to achieve in practice; if MINE and LMI diverge substantially, the empirical validation weakens. SubLoRA bound computation for LoRA-fine-tuned VLAs is untested and may require non-trivial adaptation."
    },
    "auto_research": {
      "gpu_hours": "~800-1300h A100 80GB (broader sweeps: 9 token budgets × 2 pruning strategies × 3 MI estimators × LIBERO-90 + LIBERO-Plus full perturbation matrix × SubLoRA bound grid search)",
      "gpu_utilization": "High (~85-95%): agent queues experiments continuously; near-zero idle time",
      "timeline": "2-4 weeks with 4-8 A100s (theory derivation remains the bottleneck; agent can explore bound tightness via numerical verification but the stochastic mask IB proof and phase transition characterization likely require human insight)",
      "team": "0 (initial setup: dataset paths, LIBERO-Plus perturbation configs, SubLoRA integration, evaluation scripts, MI estimation pipeline)",
      "claude_api_cost": "$600-1000 (~7000-12000 turns for end-to-end exploration, experiment execution, bound computation, analysis, and paper drafting)",
      "estimated_gpu_cost": "$1200-1950 at ~$1.50/h A100 spot pricing",
      "speed_bottleneck": "GPU count for embarrassingly parallel token-budget sweeps; also limited by whether automated symbolic exploration can derive the stochastic mask phase transition characterization without human mathematical insight",
      "risk_note": "SubLoRA-style bound computation for LoRA-fine-tuned VLAs is novel and may require significant engineering; the domain divergence term in the bound may remain loose even with masked representations; the phase transition prediction for k* may not match empirical thresholds across all LIBERO-Plus perturbation types"
    }
  },
  "target_venues": [
    "ICLR 2027 (expected deadline: ~September 24, 2026 — primary target, gives ~4 months for theory + experiments)",
    "AAAI 2027 (expected deadline: ~August 2026 — aggressive but feasible backup)",
    "ICRA 2027 (expected deadline: ~September-October 2026 — robotics venue, complements theory with VLA experiments)",
    "NeurIPS 2027 (expected deadline: ~May 2027 — safety net if earlier deadlines are missed)"
  ],
  "level": "top-tier",
  "key_references": [
    "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation [BC-IB] (Bai et al., ICML 2025, arXiv 2502.02853)",
    "How Does Information Bottleneck Help Deep Learning? (Kawaguchi et al., ICML 2023)",
    "On the Information Bottleneck Theory of Deep Learning (Saxe et al., ICLR 2018)",
    "A Generalized Information Bottleneck Theory of Deep Learning [GIB] (arXiv 2509.26327, 2025)",
    "PAC-Bayes Information Bottleneck (Wang et al., ICLR 2022 Spotlight)",
    "Approximating Mutual Information of High-Dimensional Variables Using Learned Representations [LMI] (NeurIPS 2024, arXiv 2409.02732)",
    "Non-Vacuous Generalization Bounds for Large Language Models [SubLoRA] (Lotfi et al., ICML 2024, arXiv 2312.17173)",
    "Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models (Kuang et al., NeurIPS 2024 Spotlight, arXiv 2407.18158)",
    "How Much Information Can a Vision Token Hold? A Scaling Law for Recognition Limits in VLMs (Zhuang et al., arXiv 2602.02539, 2026)",
    "Causally-Aware Information Bottleneck for Domain Adaptation (Javidian, arXiv 2601.04361, 2026)",
    "A New PAC-Bayesian Perspective on Domain Adaptation (Germain et al., ICML 2016)",
    "The Better You Learn, The Smarter You Prune: Towards Efficient VLA Models via Differentiable Token Pruning [LightVLA] (ICRA 2026, arXiv 2509.12594)",
    "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy [OneWM-VLA] (arXiv 2605.07931, 2026)",
    "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model [GridS] (ICML 2026)",
    "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, 2026)",
    "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449, 2025)",
    "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification (arXiv 2603.25766, 2026)",
    "EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration (arXiv 2602.00780, 2026)",
    "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View VLA (arXiv 2602.20566, 2026)",
    "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning (arXiv 2509.05614, 2025)",
    "EfficientVLA: Training-Free Acceleration and Compression for VLA Models (arXiv 2506.10100)",
    "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration (arXiv 2506.12723)",
    "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation (arXiv 2511.18950, 2025)",
    "Token Reduction Should Go Beyond Efficiency in Generative Models (arXiv 2505.18227, 2025)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)",
    "CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking (AAAI 2026)",
    "Revisiting LLM Reasoning via Information Bottleneck [IBRO] (arXiv 2507.18391, 2025)",
    "Generalization in Reinforcement Learning with Selective Noise Injection and Information Bottleneck [IBAC-SNI] (NeurIPS 2019)",
    "Drop-Bottleneck: Learning Discrete Compressed Representation for Noise-Robust Exploration (arXiv 2103.12300)"
  ],
  "description": "We extend BC-IB's (ICML 2025) Information Bottleneck theory from continuous latent compression in lightweight BC architectures to stochastic discrete visual token selection in VLA policies under distribution shift — addressing three gaps that BC-IB explicitly left open. First, we resolve the formalization subtlety that deterministic token selection trivializes the IB objective by modeling VLA token pruning as a stochastic binary mask process (aligning with Gumbel-softmax methods like LightVLA), and derive distribution-shift generalization bounds by combining Kawaguchi et al.'s (ICML 2023) IB framework with PAC-Bayes domain adaptation techniques (Germain et al., 2016). To address the well-documented vacuity of PAC-Bayes bounds at overparameterized scale, we exploit LoRA fine-tuning's low effective parameter count (~4-8M vs 7B) and treat action timesteps as individual data points following Kuang et al.'s (NeurIPS 2024 Spotlight) martingale approach, targeting non-vacuous bounds within the LoRA-parameterized subspace. Rather than assuming task-conditioned pruning reduces domain gap (which would be circular), we derive a testable prediction: the bound predicts that generalization improves if and only if pruning disproportionately removes domain-variant over task-relevant information — empirically falsifiable by comparing task-conditioned vs. random pruning on LIBERO-Plus perturbation suites. Second, we derive a phase transition analysis characterizing the critical token budget k* below which I(Z_M;Y) collapses, complementing (not duplicating) Zhuang et al.'s (2026) recognition-capacity phase transition: theirs characterizes information capacity per token for recognition; ours characterizes minimum tokens for action-prediction information, derived from IB rate-distortion theory and parametrized by task complexity, explaining why k*=1 suffices for simple manipulation but k*≫1 for spatial reasoning tasks. Third, we validate at VLA scale (OpenVLA 7B with LoRA) on LIBERO-90 (in-distribution) and LIBERO-Plus (distribution shift across camera viewpoints, object layouts, lighting, textures, robot states, and language), using three MI estimation approaches (LMI, MINE, linear probe surrogates), computing the PAC-Bayes bound numerically via SubLoRA-style LoRA compression, and reporting both absolute bound values and ordinal predictions. This work addresses the Saxe et al. (ICLR 2018) critique by noting VLA token pruning is designed compression, not emergent compression. The result provides VLA token compression with distribution-shift-aware theoretical grounding, principled token budget selection via k*, and a falsifiable framework for evaluating whether any given pruning strategy improves generalization under shift.",
  "project_name": "ib_vla_token_theory",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL OMISSION: BC-IB (Bai et al., 'Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation', ICML 2025, arXiv 2502.02853) already derives PAC-learning generalization bounds (Δ(S) ≤ √[2I(X;Z) + log(2/δ)] / 2n) for IB in robot manipulation behavior cloning, tests on LIBERO, and shows IB reduces I(X;Z) to one-quarter while improving success rate by 7.7%. The Generator's claim that 'no formal theoretical framework explains why compressing visual representations improves action prediction' is factually incorrect — BC-IB does exactly this, albeit for lightweight architectures rather than VLAs.", "IB theory has known fundamental limitations: Saxe et al. (ICLR 2018) demonstrated that compression is not necessary for generalization, that the compression phase depends on activation function choice (tanh vs ReLU), and that there is no causal connection between compression and generalization. The proposal does not address how its IB-based framework handles these critiques, which are well-established in the community.", "The GIB synergy claim ('token pruning preferentially retains multi-token synergistic features over redundant single-token features') is stated as something to be 'proved' but the proposal provides no sketch of how this proof would work. GIB (arXiv 2509.26327) defines synergy via average interaction information — connecting this to discrete token selection in a VLA is a non-trivial formal challenge with no clear path forward.", "MI estimation feasibility: Estimating I(X;Z) and I(Z;Y) in 7B-parameter VLA representations is extremely challenging. Recent work (arXiv 2506.00330, June 2025) confirms that 'accurate estimation of mutual information from finite data remains notoriously difficult' and 'common approaches fail in high-dimensional, undersampled regimes.' The proposal's empirical validation critically depends on reliable MI estimates that may not be obtainable.", "Non-monotonic generalization risk: OneWM-VLA shows 1 token/frame works well, but the IB framework predicts monotonic improvement with compression (less I(X;Z) → tighter bound). If empirical generalization is non-monotonic at very low token counts (which is plausible — at some point critical task info is lost), the theoretical bound fails to explain the most interesting empirical phenomenon.", "CoRL 2026 deadline (May 29, 2026) is 16 days from today — impossible for a theory paper that requires theorem derivation, proof verification, and systematic experiments. This venue should be removed.", "BC-IB (ICML 2025) explicitly acknowledges it did not evaluate VLA-scale models — while this leaves a gap, it also signals that the reviewers of this proposed paper will immediately ask 'how is this different from BC-IB?' and the answer ('we extend to VLAs and token-level pruning') may feel incremental to theory reviewers at top venues."]
Feedback: The idea has a sound intuition but needs significant repositioning given BC-IB (ICML 2025). Specific recommendations:

1. **Acknowledge and differentiate from BC-IB**: This is the most urgent issue. BC-IB must be cited as the closest prior work, and the contribution must be clearly positioned as extending BC-IB in three specific ways: (a) from latent representation compression to discrete token selection/pruning, (b) from lightweight BC architectures to 7B+ VLA models, (c) from i.i.d. generalization to distribution-shift bounds in sequential decision-making. Frame the paper as 'from representation compression to token selection: scaling IB theory to VLA policies.'

2. **Address Saxe et al. criticisms head-on**: Include a section discussing why IB theory is still applicable despite the known criticisms. Argue that in the VLA token-pruning setting, compression is explicitly designed (not emergent), so the Saxe et al. critique about emergent compression not being necessary does not directly apply. This is a defensible argument but must be made explicitly.

3. **Drop or weaken the GIB synergy claims** unless you have a concrete proof sketch. The synergy decomposition is the most speculative part — consider making it an empirical observation rather than a theoretical contribution.

4. **Address MI estimation** by: (a) using multiple MI estimators and showing consistency, (b) using proxy metrics (e.g., linear probe accuracy as a surrogate for I(Z;Y)), (c) focusing on relative trends rather than absolute MI values to validate bound predictions.

5. **Remove CoRL 2026** from target venues. Target ICLR 2027 (Sep 24, 2026) as the primary venue — this gives ~4 months, which is realistic for a team with strong theory background.

6. **Reframe contribution**: Rather than 'the first formal IB theory for VLA token compression' (which BC-IB partially invalidates), position as 'the first IB-based generalization theory that explains why discrete token pruning specifically (not just representation compression) improves VLA policy robustness under domain shift — extending BC-IB to the token selection regime and VLA scale.'

### Round 2 review
Verdict: revise
Issues: ["MISSING RELATED WORK — 'How Much Information Can a Vision Token Hold? A Scaling Law for Recognition Limits in VLMs' (arXiv 2602.02539, Feb 2026) already identifies a three-phase transition (Stable/Instability/Collapse) in vision token capacity and derives a probabilistic scaling law. While targeting VLMs for recognition rather than VLAs for action prediction, this directly overlaps with the proposed 'phase transition analysis' in Part 2. The proposal must cite this work and clearly differentiate its phase transition characterization (IB-based k* for action prediction) from this recognition-capacity phase transition.", "MISSING RELATED WORK — 'Causally-Aware Information Bottleneck for Domain Adaptation' (arXiv 2601.04361, Jan 2026) directly combines Information Bottleneck with domain adaptation for handling covariate shift, including a Variational IB encoder for high-dimensional data. This is a core theoretical building block of the proposal and must be cited and differentiated from.", "VACUOUS BOUNDS AT SCALE — PAC-Bayes generalization bounds are well-documented to be vacuous (trivially ≥1) for overparameterized deep networks. Recent work confirms that 'empirically, PAC-Bayes certificates are never tighter than frequentist test-set bounds.' For a 7B-parameter VLA, the proposed bound combining PAC-Bayes + IB + domain divergence will almost certainly be numerically uninformative. The proposal must honestly acknowledge this limitation and reframe the theoretical contribution — either focus on relative trends and ordinal predictions (which weakens the 'bound' framing), or target non-vacuous bounds using data-dependent priors (which adds significant complexity).", "DISCRETE IB FORMALIZATION SUBTLETY — When Z ⊂ X is a deterministic subset selection, I(X;Z) has specific mathematical properties that differ from the continuous variational bottleneck in BC-IB. If Z is a deterministic function of a selection mask, I(X;Z) = H(Z) since Z is perfectly determined by X. The proposal needs a careful formalization — either through stochastic selection (Gumbel-softmax relaxation as in LightVLA) or by redefining the IB objective for the discrete case (e.g., via the selected token indices rather than the token values). This mathematical subtlety is not addressed.", "CIRCULAR REASONING RISK in domain gap reduction claim — The theoretical argument that 'task-conditioned token pruning tightens the bound by reducing the effective domain gap' assumes that pruned tokens disproportionately carry domain-specific information. But this is the very claim the theory should derive/prove, not assume. If this is an assumption, the bound's applicability is conditional on a property that must be verified empirically for each pruning method, which weakens the theoretical generality.", "MINOR FACTUAL ERROR — LightVLA achieves +2.6% improvement on LIBERO per the actual paper (arXiv 2509.12594), not +2.9% as stated. The token retention number (78/512) should be verified.", "ADDITIONAL MISSING VLA TOKEN PRUNING WORKS — Several concurrent VLA pruning methods are not cited: VLA-Pruner (arXiv 2511.16449, temporal-aware dual-level pruning), ETA-VLA (arXiv 2603.25766, temporal fusion + sparsification), EcoVLA (arXiv 2602.00780, environment-aware adaptive pruning). While primarily engineering papers, they represent the complete competitive landscape and reviewers will expect them.", "METAWORLD MT50 FEASIBILITY — No published work demonstrates OpenVLA 7B fine-tuning and evaluation on MetaWorld MT50. The OneWM-VLA result (47.9%→61.3% on MT50) uses a 2B backbone. Integrating OpenVLA 7B with MetaWorld MT50 may require non-trivial engineering effort not accounted for in the timeline."]
Feedback: The revision meaningfully addressed Round 1 feedback — BC-IB differentiation is now clear, Saxe et al. is handled well, GIB synergy is properly scoped as empirical, and MI estimation uses multiple approaches. However, several issues remain that must be resolved for top-venue quality:

1. **Acknowledge bound vacuity honestly**: This is the most critical theoretical issue. Add a subsection explicitly discussing that PAC-Bayes bounds at VLA scale will likely be vacuous in absolute terms, and reposition the theoretical contribution as providing (a) ordinal predictions about when pruning helps/hurts generalization, (b) a principled framework for token budget selection via k*, and (c) qualitative insights about the relationship between compression and domain gap — rather than claiming numerically tight bounds. This is defensible and honest; claiming tight bounds at 7B scale would be immediately challenged by reviewers familiar with PAC-Bayes literature.

2. **Fix the discrete IB formalization**: Address the mathematical subtlety that deterministic subset selection Z ⊂ X makes I(X;Z) = H(Z). Consider two approaches: (a) model token selection as a stochastic process (aligning with differentiable pruning methods like LightVLA's Gumbel-softmax), or (b) reformulate using the selection mask M as the bottleneck variable, where I(X;M) captures how much information about the full observation the mask reveals. This is a solvable issue but must be addressed explicitly.

3. **Cite and differentiate from arXiv 2602.02539**: The phase transition in vision token capacity (Stable/Instability/Collapse) is already documented for VLMs. Your k* analysis should be positioned as complementary — theirs characterizes recognition capacity limits, yours characterizes action-prediction information thresholds via IB theory, which additionally predicts how k* varies with task complexity.

4. **Address the circularity in domain gap reduction**: Either (a) prove that task-conditioned pruning preferentially removes domain-variant tokens (which would require assumptions about the data distribution structure), or (b) make this an empirically testable prediction of the theory rather than an assumption. Option (b) is more honest: 'our bound predicts that if pruning reduces domain-variant information disproportionately, the generalization gap will tighten; we empirically verify this by comparing task-conditioned vs. random pruning.'

5. **Add missing citations**: arXiv 2602.02539, arXiv 2601.04361, VLA-Pruner, ETA-VLA, EcoVLA. Fix the LightVLA accuracy (+2.6%, not +2.9%).

6. **De-risk MetaWorld MT50**: Either verify that OpenVLA 7B can be fine-tuned on MetaWorld MT50 (check if the observation/action spaces are compatible with OpenVLA's architecture), or replace with LIBERO-90 cross-suite transfer as the primary distribution-shift testbed, which has established OpenVLA baselines.

### Round 3 review
Verdict: revise
Issues: ["MISSING RELATED WORK — DTP (Distracting Token Pruning, arXiv 2601.16065, Jan 2026) explicitly demonstrates that pruning 'distracting' tokens (task-irrelevant visual tokens) improves VLA task success rates, finding a negative correlation between attention to task-irrelevant regions and success rate. This provides direct empirical support for the proposal's thesis and should be cited as motivation. FocusVLA (arXiv 2603.28740, Mar 2026) similarly identifies 'attention over-smoothing' and 'token count bloat' as failure modes, showing that attention-focusing on task-relevant tokens improves both performance and convergence.", "MISSING RELATED WORK — SemanticVLA (arXiv 2511.10518, AAAI 2026 Oral) achieves SOTA 97.7% on LIBERO with semantic-aligned sparsification, reducing FLOPs by 3-4x. This is a highly cited VLA pruning method at a top venue that should be included in the landscape.", "MISSING RELATED WORK — IB-FT (arXiv 2510.16022, Oct 2025) applies IB penalties during LLM fine-tuning to break 'memorization barriers' and improve generalization. While targeting code rather than VLAs, this directly validates the IB-for-fine-tuning-generalization thesis and shares the core mechanism (IB on representations during fine-tuning). Should be cited as a parallel direction.", "BOUND VACUITY REMAINS THE CENTRAL WEAKNESS — The proposal now honestly acknowledges that PAC-Bayes bounds will likely be vacuous and proposes 'ordinal predictions' as fallback. However, this fundamentally changes the nature of the contribution: ordinal predictions from a vacuous bound are not theoretically guaranteed to be meaningful — a bound that is ≥1 provides no formal guarantee about ranking either. The CMU blog post on PAC-Bayes for foundation models shows tight bounds are achievable in structured discrete spaces (prompt engineering), but the VLA LoRA setting is far less structured. The proposal should more carefully argue why ordinal predictions from a vacuous bound would be informative, potentially drawing on compression-based model selection literature (MDL principle) rather than claiming the bound itself provides ordinal guarantees.", "THE THEORETICAL CONTRIBUTION MAY NOT SATISFY THE USER'S REQUEST — The user asked for theoretical analysis of 'why token pruning enhances VLA generalization' (从理论角度分析为何能增强). A vacuous bound with ordinal fallback does not provide a convincing theoretical 'why' — it provides a framework that may or may not predict empirical trends. The most convincing theoretical contribution would be the qualitative insight that stochastic mask-based pruning reduces I(X;M) which tightens the generalization bound, plus the phase transition k* characterization. But if bounds are vacuous, the connection from 'IB reduces I(X;M)' to 'generalization improves' becomes an empirical correlation rather than a theoretical guarantee.", "PHASE TRANSITION k* ANALYSIS — While positioned as complementary to Zhuang et al. (2026), the k* characterization may be empirically difficult to validate. The proposal claims k* depends on 'task complexity (action space dimensionality, horizon length, spatial precision requirements) and visual redundancy ratio,' but deriving a closed-form expression for k* as a function of these variables is a significant theoretical challenge. If k* can only be estimated empirically per-task, the theoretical contribution reduces to 'there exists a phase transition' (which is already observable from the empirical literature — OneWM-VLA's k*=1 success vs. GridS's need for more tokens).", "MINOR: LightVLA improvement is stated as +2.9% in the landscape section but Round 2 feedback requested correction to +2.6%. The proposal description mentions aligning with LightVLA's Gumbel-softmax but the landscape section still states +2.9%.", "MINOR: The proposal cites an enormous number of VLA pruning methods (15+) which is comprehensive but risks giving reviewers the impression that token pruning is already a saturated empirical area — the theoretical contribution must be strong enough to stand on its own rather than seeming like an afterthought to the empirical VLA pruning wave."]
Feedback: The proposal has improved substantially across two rounds of revision. The BC-IB differentiation is now clear and well-articulated, the stochastic binary mask formalization resolves the discrete IB subtlety, the circularity in domain gap reduction is addressed via falsifiable predictions, and the honest acknowledgment of bound vacuity is appropriate. However, several issues need attention for a top-venue pass:

1. **Strengthen the theoretical 'why' narrative**: The user specifically asked for theoretical analysis of why token pruning enhances generalization. The current framing risks delivering 'a framework that might predict trends' rather than 'a theoretical explanation.' Consider restructuring: (a) Lead with the qualitative IB insight — task-conditioned pruning removes domain-variant visual information disproportionately, which reduces the effective distribution shift seen by the policy; (b) Use the stochastic mask IB bound to formalize this insight; (c) Use the k* phase transition to explain the non-monotonicity; (d) Treat the PAC-Bayes bound computation as validation of the framework rather than the core contribution. This reframing makes the theory more resilient to bound vacuity.

2. **Address the ordinal prediction gap**: A vacuous PAC-Bayes bound does not formally guarantee meaningful ordinal predictions. Either (a) cite MDL/minimum description length literature to justify that compression-based rankings are informative even when absolute bounds are loose (Grünwald's MDL principle), or (b) prove a separate result showing that the bound's relative ordering is preserved under certain conditions even when absolute values are vacuous. Without this, the fallback is ad hoc.

3. **Add missing citations**: DTP (arXiv 2601.16065), FocusVLA (arXiv 2603.28740), SemanticVLA (arXiv 2511.10518, AAAI 2026 Oral), and IB-FT (arXiv 2510.16022). These strengthen the empirical motivation and show the theoretical gap is real — many methods work empirically but none explain why.

4. **Fix LightVLA accuracy**: Landscape section still states +2.9%, should be +2.6%.

5. **Sharpen the k* contribution**: Either (a) provide a concrete analytical form for k* (even under simplifying assumptions like linear policy, Gaussian observations) to show the phase transition can be characterized theoretically, or (b) explicitly frame k* estimation as an empirical method guided by IB theory rather than a closed-form theoretical result. The latter is more honest and still valuable.

6. **Consider scope narrowing**: The proposal tries to deliver too many things (stochastic IB bound + distribution shift extension + k* phase transition + GIB synergy characterization + SubLoRA bound computation + three MI estimators + LIBERO-Plus validation). For a 4-month timeline targeting ICLR 2027, consider dropping or deprioritizing the GIB synergy characterization and reducing MI estimators to two (LMI + linear probe). This focuses the paper on the strongest contributions: the stochastic mask IB formalization, the domain-shift bound, and the k* phase transition.


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
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "92190fa6-dd6b-4ade-a8cb-84704decfacc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T05:19:11.710Z_

```json
{
  "parentUuid": "92190fa6-dd6b-4ade-a8cb-84704decfacc",
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
  "uuid": "eebef7d0-db97-43af-9b14-00ff99200616",
  "timestamp": "2026-05-13T05:19:11.710Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T05:19:11.710Z_

```json
{
  "parentUuid": "eebef7d0-db97-43af-9b14-00ff99200616",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4f0e985a-69e0-46aa-a36d-5d121ba53fc7",
  "timestamp": "2026-05-13T05:19:11.710Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
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
  "leafUuid": "4f0e985a-69e0-46aa-a36d-5d121ba53fc7",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "VLA token pruning: discrete IB theory under domain shift",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Assistant

_source line 8 · 2026-05-13T05:19:18.605Z_

<details><summary>Logged reasoning block</summary>

```text
This is a complex ML research review task. I need to independently verify the claims made in this research proposal about Information Bottleneck theory for VLA (Vision-Language-Action) token pruning. This is round 4 of 10 reviews.

Let me analyze what's been improved since previous rounds and what issues remain. I need to do thorough web searches to verify claims, find missing related work, and assess the overall quality.

Let me start by searching for the key claims and related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f0e985a-69e0-46aa-a36d-5d121ba53fc7",
  "isSidechain": false,
  "requestId": "req_011Caz1Ao1CYmdBeoo24aMPg",
  "type": "assistant",
  "uuid": "04b9f938-9aa8-455f-b218-40f5faa3ba90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EghPvzYnkttDihA1PFV9T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20200,
      "cache_read_input_tokens": 11841,
      "output_tokens": 649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 649,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20200
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

_source line 9 · 2026-05-13T05:19:19.558Z_

I'll conduct an independent review of this proposal by verifying its claims, searching for missing related work, and assessing the theoretical contributions. Let me start with parallel searches across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b9f938-9aa8-455f-b218-40f5faa3ba90",
  "isSidechain": false,
  "requestId": "req_011Caz1Ao1CYmdBeoo24aMPg",
  "type": "assistant",
  "uuid": "777fa3a7-37af-4251-8267-73979ed704ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EghPvzYnkttDihA1PFV9T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20200,
      "cache_read_input_tokens": 11841,
      "output_tokens": 649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 649,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20200
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

_source line 10 · 2026-05-13T05:19:30.434Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QGwuQ4jpKRngu9unMvZ5vc`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify BC-IB and core references",
  "prompt": "I'm reviewing an ML research proposal about Information Bottleneck theory for VLA token pruning. I need to verify several key references and claims. Please search for and verify the following:\n\n1. BC-IB paper: \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation\" by Bai et al., claimed to be at ICML 2025, arXiv 2502.02853. Verify it exists, check what it actually does, and whether it was accepted at ICML 2025.\n\n2. SubLoRA paper: \"Non-Vacuous Generalization Bounds for Large Language Models\" by Lotfi et al., claimed ICML 2024, arXiv 2312.17173. Verify existence and whether it achieves non-vacuous bounds for ~800M models.\n\n3. \"Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models\" by Kuang et al., claimed NeurIPS 2024 Spotlight, arXiv 2407.18158. Verify it extends to LLaMA2-70B.\n\n4. \"How Much Information Can a Vision Token Hold?\" by Zhuang et al., arXiv 2602.02539. Verify existence and its three-phase transition claim.\n\n5. LightVLA paper: arXiv 2509.12594. Verify the improvement percentage — is it +2.6% or +2.9%?\n\nUse WebSearch for each query. For the most important papers (BC-IB and SubLoRA), try to fetch the actual arxiv abstract pages to verify details. Report your findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "777fa3a7-37af-4251-8267-73979ed704ed",
  "isSidechain": false,
  "requestId": "req_011Caz1Ao1CYmdBeoo24aMPg",
  "type": "assistant",
  "uuid": "8bea637f-1323-47db-ae9e-92d11da4d6c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EghPvzYnkttDihA1PFV9T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20200,
      "cache_read_input_tokens": 11841,
      "output_tokens": 649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 649,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20200
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

_source line 11 · 2026-05-13T05:21:04.247Z_

<details><summary>↩ Tool result · `toolu_01QGwuQ4jpKRngu9unMvZ5vc`</summary>

```text
Interesting -- there's a title discrepancy between versions. Here are my consolidated findings:

---

## Verification Results

### 1. BC-IB Paper (arXiv 2502.02853)

**Status: EXISTS, ICML 2025 CONFIRMED** -- but note a minor title discrepancy between versions.

- The paper exists at arXiv 2502.02853 by Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, and Badong Chen.
- **Title discrepancy:** The v1 preprint uses "Rethinking Latent **Representations** in Behavior Cloning..." while the current arXiv version and the ICML proceedings page use "Rethinking Latent **Redundancy** in Behavior Cloning..." The title was apparently revised between versions.
- **ICML 2025 acceptance confirmed** -- it appears in the ICML 2025 proceedings at `proceedings.mlr.press/v267/bai25e.html` and the GitHub repo is tagged `[ICML 2025]`.
- **What it does:** Applies the Information Bottleneck principle to Behavior Cloning for robot manipulation, quantifying and reducing redundancy in latent representations. Experiments on CortexBench and LIBERO benchmarks. This matches the claimed description.

### 2. SubLoRA Paper (arXiv 2312.17173)

**Status: EXISTS, ICML 2024 CONFIRMED, ~800M claim VERIFIED**

- By Sanae Lotfi, Marc Finzi, Yilun Kuang, Tim G. J. Rudner, Micah Goldblum, and Andrew Gordon Wilson.
- **ICML 2024 confirmed** in the arXiv comments.
- Introduces SubLoRA (low-dimensional non-linear parameterization) for extreme compression.
- **Model size:** The abstract says "models with nearly a billion parameters." The web search results specify up to 849 million parameters. Claiming "~800M" is reasonable and roughly accurate.
- Achieves the first non-vacuous generalization bounds for pretrained LLMs.

### 3. Kuang et al. Token Bounds (arXiv 2407.18158)

**Status: EXISTS, NeurIPS 2024 SPOTLIGHT CONFIRMED, LLaMA2-70B CONFIRMED**

- By Sanae Lotfi, Yilun Kuang, Brandon Amos, Micah Goldblum, Marc Finzi, and Andrew Gordon Wilson.
- Note: The first author is actually **Lotfi**, not Kuang -- Kuang is second author. If the proposal cites this as "Kuang et al." that is technically incorrect.
- **NeurIPS 2024 Spotlight confirmed** via the GitHub repo (`[NeurIPS'24 Spotlight]` tag).
- **LLaMA2-70B confirmed:** The abstract explicitly states they achieve "the first non-vacuous bounds for models that are deployed in practice" including LLaMA2-70B.
- Uses martingale properties to treat tokens (not documents) as data points, plus Monarch matrices, Kronecker factorizations, and post-training quantization for compression.

### 4. Zhuang et al. Vision Token Information (arXiv 2602.02539)

**Status: EXISTS, THREE-PHASE TRANSITION CONFIRMED**

- Title: "How Much Information Can a Vision Token Hold? A Scaling Law for Recognition Limits in VLMs" by Shuxin Zhuang et al.
- The paper exists and the three-phase transition claim is verified. The three phases are:
  1. **Stable Phase** -- near-perfect recognition
  2. **Instability Phase** -- increased error variance
  3. **Collapse Phase** -- total failure
- The paper studies vision tokens as a lossy channel with finite representational capacity, using controlled stress tests (progressively increasing character count in images).
- Note: The arXiv ID prefix `2602` corresponds to February 2026, making this a very recent paper.

### 5. LightVLA (arXiv 2509.12594)

**STATUS: EXISTS, the improvement is +2.6%, NOT +2.9%**

- Title: "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning"
- By Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang.
- **The actual arXiv abstract reports a 2.6% improvement in task success rate**, along with 59.1% FLOPs reduction and 38.2% latency reduction. If the proposal claims +2.9%, that is incorrect -- the correct figure from the paper is **+2.6%**.
- Note: One secondary web source (a Medium blog post) incorrectly cited 2.9%, which may be the origin of the error.
- GitHub repo indicates ICRA 2026 acceptance.

---

## Summary of Issues Found

| Paper | Exists? | Venue Correct? | Key Claim Accurate? |
|-------|---------|----------------|---------------------|
| BC-IB (2502.02853) | Yes | ICML 2025 -- correct | Yes, but note title changed between versions |
| SubLoRA (2312.17173) | Yes | ICML 2024 -- correct | ~800M is reasonable (actual: 849M) |
| Kuang et al. (2407.18158) | Yes | NeurIPS 2024 Spotlight -- correct | LLaMA2-70B confirmed; but first author is Lotfi, not Kuang |
| Zhuang et al. (2602.02539) | Yes | N/A (arXiv only) | Three-phase transition confirmed |
| LightVLA (2509.12594) | Yes | ICRA 2026 | **+2.6%, not +2.9%** -- proposal has wrong number |

The two actionable issues for the proposal: (1) the LightVLA improvement should be corrected from +2.9% to +2.6%, and (2) paper 2407.18158 should be cited as "Lotfi et al." rather than "Kuang et al." if following standard first-author convention.

Sources:
- [BC-IB on arXiv](https://arxiv.org/abs/2502.02853)
- [BC-IB ICML 2025 Proceedings](https://proceedings.mlr.press/v267/bai25e.html)
- [BC-IB GitHub](https://github.com/BaiShuanghao/BC-IB)
- [SubLoRA on arXiv](https://arxiv.org/abs/2312.17173)
- [SubLoRA GitHub](https://github.com/Sanaelotfi/SubLoRA-bounds-for-LLMs)
- [Token Bounds on arXiv](https://arxiv.org/abs/2407.18158)
- [Token Bounds GitHub (NeurIPS'24 Spotlight)](https://github.com/YilunKuang/token-bounds-for-llms)
- [Vision Token Information on arXiv](https://arxiv.org/abs/2602.02539)
- [LightVLA on arXiv](https://arxiv.org/abs/2509.12594)
- [LightVLA GitHub (ICRA 2026)](https://github.com/LiAutoAD/LightVLA)

agentId: a085d41f175d9a806 (use SendMessage with to: 'a085d41f175d9a806' to continue this agent)
&lt;usage>total_tokens: 20524
tool_uses: 14
duration_ms: 93805&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bea637f-1323-47db-ae9e-92d11da4d6c4",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "c15f7b34-fa86-494c-b59d-fdba256eeddc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML research proposal about Information Bottleneck theory for VLA token pruning. I need to verify several key references and claims. Please search for and verify the following:\n\n1. BC-IB paper: \"Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation\" by Bai et al., claimed to be at ICML 2025, arXiv 2502.02853. Verify it exists, check what it actually does, and whether it was accepted at ICML 2025.\n\n2. SubLoRA paper: \"Non-Vacuous Generalization Bounds for Large Language Models\" by Lotfi et al., claimed ICML 2024, arXiv 2312.17173. Verify existence and whether it achieves non-vacuous bounds for ~800M models.\n\n3. \"Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models\" by Kuang et al., claimed NeurIPS 2024 Spotlight, arXiv 2407.18158. Verify it extends to LLaMA2-70B.\n\n4. \"How Much Information Can a Vision Token Hold?\" by Zhuang et al., arXiv 2602.02539. Verify existence and its three-phase transition claim.\n\n5. LightVLA paper: arXiv 2509.12594. Verify the improvement percentage — is it +2.6% or +2.9%?\n\nUse WebSearch for each query. For the most important papers (BC-IB and SubLoRA), try to fetch the actual arxiv abstract pages to verify details. Report your findings concisely.",
    "agentId": "a085d41f175d9a806",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Interesting -- there's a title discrepancy between versions. Here are my consolidated findings:\n\n---\n\n## Verification Results\n\n### 1. BC-IB Paper (arXiv 2502.02853)\n\n**Status: EXISTS, ICML 2025 CONFIRMED** -- but note a minor title discrepancy between versions.\n\n- The paper exists at arXiv 2502.02853 by Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, and Badong Chen.\n- **Title discrepancy:** The v1 preprint uses \"Rethinking Latent **Representations** in Behavior Cloning...\" while the current arXiv version and the ICML proceedings page use \"Rethinking Latent **Redundancy** in Behavior Cloning...\" The title was apparently revised between versions.\n- **ICML 2025 acceptance confirmed** -- it appears in the ICML 2025 proceedings at `proceedings.mlr.press/v267/bai25e.html` and the GitHub repo is tagged `[ICML 2025]`.\n- **What it does:** Applies the Information Bottleneck principle to Behavior Cloning for robot manipulation, quantifying and reducing redundancy in latent representations. Experiments on CortexBench and LIBERO benchmarks. This matches the claimed description.\n\n### 2. SubLoRA Paper (arXiv 2312.17173)\n\n**Status: EXISTS, ICML 2024 CONFIRMED, ~800M claim VERIFIED**\n\n- By Sanae Lotfi, Marc Finzi, Yilun Kuang, Tim G. J. Rudner, Micah Goldblum, and Andrew Gordon Wilson.\n- **ICML 2024 confirmed** in the arXiv comments.\n- Introduces SubLoRA (low-dimensional non-linear parameterization) for extreme compression.\n- **Model size:** The abstract says \"models with nearly a billion parameters.\" The web search results specify up to 849 million parameters. Claiming \"~800M\" is reasonable and roughly accurate.\n- Achieves the first non-vacuous generalization bounds for pretrained LLMs.\n\n### 3. Kuang et al. Token Bounds (arXiv 2407.18158)\n\n**Status: EXISTS, NeurIPS 2024 SPOTLIGHT CONFIRMED, LLaMA2-70B CONFIRMED**\n\n- By Sanae Lotfi, Yilun Kuang, Brandon Amos, Micah Goldblum, Marc Finzi, and Andrew Gordon Wilson.\n- Note: The first author is actually **Lotfi**, not Kuang -- Kuang is second author. If the proposal cites this as \"Kuang et al.\" that is technically incorrect.\n- **NeurIPS 2024 Spotlight confirmed** via the GitHub repo (`[NeurIPS'24 Spotlight]` tag).\n- **LLaMA2-70B confirmed:** The abstract explicitly states they achieve \"the first non-vacuous bounds for models that are deployed in practice\" including LLaMA2-70B.\n- Uses martingale properties to treat tokens (not documents) as data points, plus Monarch matrices, Kronecker factorizations, and post-training quantization for compression.\n\n### 4. Zhuang et al. Vision Token Information (arXiv 2602.02539)\n\n**Status: EXISTS, THREE-PHASE TRANSITION CONFIRMED**\n\n- Title: \"How Much Information Can a Vision Token Hold? A Scaling Law for Recognition Limits in VLMs\" by Shuxin Zhuang et al.\n- The paper exists and the three-phase transition claim is verified. The three phases are:\n  1. **Stable Phase** -- near-perfect recognition\n  2. **Instability Phase** -- increased error variance\n  3. **Collapse Phase** -- total failure\n- The paper studies vision tokens as a lossy channel with finite representational capacity, using controlled stress tests (progressively increasing character count in images).\n- Note: The arXiv ID prefix `2602` corresponds to February 2026, making this a very recent paper.\n\n### 5. LightVLA (arXiv 2509.12594)\n\n**STATUS: EXISTS, the improvement is +2.6%, NOT +2.9%**\n\n- Title: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning\"\n- By Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang.\n- **The actual arXiv abstract reports a 2.6% improvement in task success rate**, along with 59.1% FLOPs reduction and 38.2% latency reduction. If the proposal claims +2.9%, that is incorrect -- the correct figure from the paper is **+2.6%**.\n- Note: One secondary web source (a Medium blog post) incorrectly cited 2.9%, which may be the origin of the error.\n- GitHub repo indicates ICRA 2026 acceptance.\n\n---\n\n## Summary of Issues Found\n\n| Paper | Exists? | Venue Correct? | Key Claim Accurate? |\n|-------|---------|----------------|---------------------|\n| BC-IB (2502.02853) | Yes | ICML 2025 -- correct | Yes, but note title changed between versions |\n| SubLoRA (2312.17173) | Yes | ICML 2024 -- correct | ~800M is reasonable (actual: 849M) |\n| Kuang et al. (2407.18158) | Yes | NeurIPS 2024 Spotlight -- correct | LLaMA2-70B confirmed; but first author is Lotfi, not Kuang |\n| Zhuang et al. (2602.02539) | Yes | N/A (arXiv only) | Three-phase transition confirmed |\n| LightVLA (2509.12594) | Yes | ICRA 2026 | **+2.6%, not +2.9%** -- proposal has wrong number |\n\nThe two actionable issues for the proposal: (1) the LightVLA improvement should be corrected from +2.9% to +2.6%, and (2) paper 2407.18158 should be cited as \"Lotfi et al.\" rather than \"Kuang et al.\" if following standard first-author convention.\n\nSources:\n- [BC-IB on arXiv](https://arxiv.org/abs/2502.02853)\n- [BC-IB ICML 2025 Proceedings](https://proceedings.mlr.press/v267/bai25e.html)\n- [BC-IB GitHub](https://github.com/BaiShuanghao/BC-IB)\n- [SubLoRA on arXiv](https://arxiv.org/abs/2312.17173)\n- [SubLoRA GitHub](https://github.com/Sanaelotfi/SubLoRA-bounds-for-LLMs)\n- [Token Bounds on arXiv](https://arxiv.org/abs/2407.18158)\n- [Token Bounds GitHub (NeurIPS'24 Spotlight)](https://github.com/YilunKuang/token-bounds-for-llms)\n- [Vision Token Information on arXiv](https://arxiv.org/abs/2602.02539)\n- [LightVLA on arXiv](https://arxiv.org/abs/2509.12594)\n- [LightVLA GitHub (ICRA 2026)](https://github.com/LiAutoAD/LightVLA)"
      }
    ],
    "totalDurationMs": 93805,
    "totalTokens": 20524,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 18185,
      "output_tokens": 1866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 472
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1866,
          "cache_read_input_tokens": 18185,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 472,
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
  "sourceToolAssistantUUID": "8bea637f-1323-47db-ae9e-92d11da4d6c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T05:21:17.240Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KnmDaRmAPGzxv86e7qYuu9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing/missing related work",
  "prompt": "I'm reviewing an ML research proposal about using Information Bottleneck (IB) theory to explain why token pruning improves VLA (Vision-Language-Action) model generalization. I need to search for competing or missing related work that the proposal may have overlooked. Please conduct the following searches:\n\n1. Search for \"information bottleneck token pruning generalization 2025 2026\" on arXiv\n2. Search for \"VLA token pruning theory\" or \"vision language action pruning theoretical\"\n3. Search for \"PAC-Bayes generalization bounds robotics 2025 2026\"\n4. Search for \"DTP distracting token pruning VLA\" (arXiv 2601.16065) — verify it exists\n5. Search for \"FocusVLA\" (arXiv 2603.28740) — verify it exists\n6. Search for \"SemanticVLA\" (arXiv 2511.10518) — verify it exists and is AAAI 2026 Oral\n7. Search for \"IB-FT information bottleneck fine-tuning LLM generalization\" (arXiv 2510.16022)\n8. Search for \"token reduction generalization vision language model 2026\" to find any very recent work\n9. Search for \"LIBERO-Plus\" benchmark (arXiv 2510.13626) — verify it exists and is CVPR 2026\n\nFor each found paper, report: title, authors, venue, and a 1-2 sentence summary of what it does. Focus especially on finding work that directly combines IB theory with token pruning/selection for generalization analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c15f7b34-fa86-494c-b59d-fdba256eeddc",
  "isSidechain": false,
  "requestId": "req_011Caz1K6QBSfpnTxNS4t4et",
  "type": "assistant",
  "uuid": "3188f3f8-2211-4973-bbc2-198c08a0726a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7BxP8e3N69CcGkzwcu6VU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 32041,
      "output_tokens": 473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 473,
          "cache_read_input_tokens": 32041,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 13 · 2026-05-13T05:24:45.738Z_

<details><summary>↩ Tool result · `toolu_01KnmDaRmAPGzxv86e7qYuu9`</summary>

```text
Now I have comprehensive results. Here is my full report.

---

## Search Results: Related Work for IB Theory + Token Pruning in VLA Models

### 1. Verification of Papers Cited in the Proposal

**DTP (arXiv 2601.16065) -- VERIFIED**
- **Title:** "DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models"
- **Authors:** Chenyang Li, Jieyuan Liu, Bin Li, Bo Gao, Yilin Yuan, Yangfan He, Yuchen Li, Jingqun Tang
- **Date:** January 22, 2026; arXiv preprint (no confirmed venue acceptance)
- **Summary:** Introduces a plug-and-play framework that dynamically detects and prunes "distracting" (task-irrelevant) image tokens in VLA models. Shows a negative correlation between attention to task-irrelevant regions and success rate. Does NOT discuss IB theory or generalization theory.

**FocusVLA (arXiv 2603.28740) -- VERIFIED**
- **Title:** "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models"
- **Authors:** Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan
- **Date:** March 30, 2026; arXiv preprint (no confirmed venue)
- **Summary:** Proposes Modality Cascaded Attention and Focus Attention to force VLA models to rely on task-relevant visual details. Argues performance is limited by how visual information is utilized, not by representation quality. Does NOT discuss IB theory or generalization theory -- purely empirical/architectural.

**SemanticVLA (arXiv 2511.10518) -- VERIFIED as AAAI 2026 Oral**
- **Title:** "SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation"
- **Authors:** Wei Li, Renshan Zhang, Rui Shao, Zhijian Fang, Kaiwen Zhou, Zhuotao Tian, Liqiang Nie
- **Date:** November 13, 2025; **Confirmed AAAI 2026 Oral**
- **Summary:** Uses a Semantic-guided Dual Visual Pruner (SD-Pruner) with instruction-driven and spatial-aggregation sub-pruners. Achieves 97.7% success on LIBERO with 3x training cost reduction and 2.7x inference speedup. Does NOT use IB theory.

**IB-FT (arXiv 2510.16022) -- VERIFIED**
- **Title:** "Breaking Memorization Barriers in LLM Code Fine-Tuning via Information Bottleneck for Improved Generalization"
- **Authors:** Changsheng Wang, Xin Chen, Sijia Liu, Ke Ding
- **Date:** October 15, 2025; arXiv preprint
- **Summary:** Applies an IB penalty on hidden representations during LLM code fine-tuning to compress spurious/memorized features while preserving task-relevant information. This is the closest existing work combining IB with generalization for large models, but it addresses code LLM fine-tuning, NOT token pruning or VLA models.

**LIBERO-Plus (arXiv 2510.13626) -- VERIFIED as CVPR 2026 Poster**
- **Title:** "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" (subtitle on CVPR page: "A Progressive Robustness Benchmark for Visual-Language-Action Models")
- **Authors:** Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, Xipeng Qiu
- **Date:** October 15, 2025; **Confirmed CVPR 2026 Poster** (verified via cvpr.thecvf.com/virtual/2026/poster/38735)
- **Summary:** Systematic robustness analysis of VLA models across 7 perturbation dimensions. Reveals brittleness: performance drops from 95% to below 30% under modest perturbations. Shows models largely ignore language instructions.

---

### 2. Key Competing / Related Work the Proposal May Be Missing

#### A. VLA Token Pruning Methods (Direct Competitors -- Strong Coverage Needed)

**LightVLA (arXiv 2509.12594)**
- **Title:** "The Better You Learn, The Smarter You Prune: Towards Efficient VLA Models via Differentiable Token Pruning"
- **Authors:** Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang
- **Date:** September 16, 2025; under review
- **Summary:** First work applying differentiable (learnable) token pruning to VLA, using Gumbel softmax for differentiable selection. Achieves 59.1% FLOPs reduction with 2.9% success rate improvement. Important because it claims simultaneous efficiency AND performance gains -- relevant to any generalization argument.

**VLA-Pruner (arXiv 2511.16449)**
- **Title:** "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference"
- **Date:** November 2025
- **Summary:** Dual-level importance criterion combining vision-language prefill attention (semantic) and action decode attention (action-level), with temporal smoothing. Addresses the criticism that VLM pruning methods ignore VLA's dual-system nature.

**VLA-IAP (arXiv 2603.22991)**
- **Title:** "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models"
- **Date:** March 24, 2026
- **Summary:** Training-free method introducing geometric prior and dynamic scheduling for conservative-to-aggressive pruning. Achieves 97.8% success with 1.54x speedup. Emphasizes preserving structurally critical manipulation regions.

**BFA++ (arXiv 2602.20566)**
- **Title:** "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model"
- **Date:** February 24, 2026
- **Summary:** Hierarchical pruning for multi-view VLA with intra-view and inter-view importance predictors. Addresses multi-camera setups specifically.

**SP-VLA (arXiv 2506.12723) -- ICLR 2026**
- **Title:** "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration"
- **Date:** June 2025; **Accepted at ICLR 2026**
- **Summary:** Combines action-aware model scheduling (switching between full VLA and lightweight generator) with spatio-semantic dual-aware token pruning. Achieves up to 6% performance gain with 2.4x acceleration. This is the highest-venue VLA pruning paper found (ICLR 2026).

**SpecPrune-VLA (arXiv 2509.05614)**
- **Title:** "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning"
- **Date:** September 2025
- **Summary:** Training-free, two-level pruning exploiting temporal similarity between consecutive frames. Uses action granularity (coarse vs. fine) to dynamically adjust pruning aggressiveness.

**SQAP-VLA (arXiv 2509.09090)**
- **Title:** "SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance VLA Models"
- **Authors:** Hengyu Fang, Yijiang Liu, Yuan Du, Li Du, Huanrui Yang
- **Date:** September 11, 2025
- **Summary:** First framework jointly enabling quantization and token pruning for VLA. Co-designs both to overcome observed incompatibility between aggressive quantization and token pruning.

#### B. Information Bottleneck Theory (Theoretical Foundations)

**Generalized Information Bottleneck (GIB) (arXiv 2509.26327)**
- **Title:** "A Generalized Information Bottleneck Theory of Deep Learning"
- **Authors:** Charles Westphal, Stephen Hailes, Mirco Musolesi
- **Date:** September 30, 2025 (revised January 30, 2026)
- **Summary:** Reformulates IB through "synergy" (information obtainable only through joint processing of features). Shows synergistic functions achieve superior generalization. Achieves compression phases even with ReLU activations where standard IB theory fails. HIGHLY RELEVANT: this could provide the theoretical backbone for explaining why pruning (which removes non-synergistic/redundant tokens) improves generalization.

**How Does Information Bottleneck Help Deep Learning? (arXiv 2305.18887, ICML 2023)**
- **Authors:** Kenji Kawaguchi et al.
- **Summary:** Provides rigorous learning theory relating IB to generalization errors, with new generalization bounds that scale with the degree of information bottleneck. KEY FOUNDATIONAL REFERENCE for any IB-based generalization argument.

**Token Communication via Information Bottleneck (arXiv 2507.01728)**
- **Title:** "Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach"
- **Authors:** Hao Wei, Wanli Ni, Wen Wang, Wenjun Xu, Dusit Niyato, Ping Zhang
- **Date:** July 2, 2025
- **Summary:** Proposes Generative Information Bottleneck (GenIB) for learning tokens that preserve essential information while supporting generation across modalities. While focused on wireless communication, the GenIB formulation for token-level IB is directly relevant.

#### C. IB + Vision Transformer Token Methods

**IBTM: IB-Inspired Token Merging (OpenReview, Withdrawn from ICLR 2025)**
- **Title:** "Efficient Visual Transformer by Information Bottleneck Inspired Token Merging"
- **Authors:** Yancheng Wang, Yingzhen Yang
- **Summary:** Derives a separable variational upper bound for the IB loss to guide learnable token merging. This is the closest existing work to combining IB with token reduction in vision transformers, though it was withdrawn from ICLR 2025 and does NOT discuss generalization theory.

**VTrans: Variational IB-Based Pruning (arXiv 2406.05276)**
- **Title:** "VTrans: Accelerating Transformer Compression with Variational Information Bottleneck based Pruning"
- **Authors:** Oshin Dutta, Ritvik Gupta, Sumeet Agarwal
- **Date:** June 2024
- **Summary:** Uses VIB to guide structural (head/layer) pruning -- NOT token pruning. Achieves 70% more compression than prior art.

**Comprehensive IB for Vision Transformers (CVPR 2025)**
- **Title:** "Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers"
- **Summary:** Uses IB to explain ViT decision-making via layer-wise attribution. Interpretability-focused rather than pruning/generalization.

#### D. Token Reduction Beyond Efficiency (Position/Survey Papers)

**Token Reduction Should Go Beyond Efficiency (arXiv 2505.18227)**
- **Title:** "Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality"
- **Authors:** Zhenglun Kong, Yize Li, Fanhu Zeng, Lei Xin, Shvat Messica, Xue Lin, Pu Zhao, Manolis Kellis, Hao Tang, Marinka Zitnik
- **Date:** May 23, 2025 (revised January 12, 2026)
- **Summary:** Position paper arguing token reduction is a "fundamental principle in generative modeling" beyond efficiency -- impacting multimodal integration, hallucination mitigation, coherence, and training stability. DIRECTLY RELEVANT to the proposal's thesis that pruning improves generalization.

**Token Pruning in MLLMs: Are We Solving the Right Problem? (arXiv 2502.11501, ACL 2025 Findings)**
- **Title:** "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?"
- **Authors:** Zichen Wen, Yifeng Gao, Weijia Li, Conghui He, Linfeng Zhang
- **Date:** February 17, 2025; **ACL 2025 Findings**
- **Summary:** Critical analysis showing many token pruning methods underperform random selection. Questions whether attention-based scoring is sufficient and whether current evaluation protocols are comprehensive. Important cautionary counterpoint.

#### E. PAC-Bayes for Control/Robotics

**PAC-Bayes Control (arXiv 1806.04225)**
- **Title:** "PAC-Bayes Control: Learning Policies that Provably Generalize to Novel Environments"
- **Summary:** Foundational work applying PAC-Bayes to learned control policies, proving generalization to novel environments. Directly relevant if the proposal uses PAC-Bayes bounds.

**Unified PAC-Bayesian Framework (arXiv 2601.08100)**
- **Title:** "Towards A Unified PAC-Bayesian Framework for Norm-based Generalization Bounds"
- **Date:** January 2026
- **Summary:** Derives a family of bounds recovering existing PAC-Bayesian results as special cases. Could provide tighter bounds for the proposal's analysis.

**PAC-Bayes for Linear Control (arXiv 2605.10493)**
- **Title:** "A PAC-Bayes Approach for Controlling Unknown Linear Discrete-time Systems"
- **Date:** May 2026
- **Summary:** Very recent application of PAC-Bayes to control systems with unknown dynamics.

---

### 3. Critical Gap Analysis

**The key finding: No existing paper directly combines IB theory with token pruning/selection to provide a formal generalization analysis for VLA models.** This is the novel contribution space for the proposal. However, several adjacent works should be cited and distinguished:

1. **IB-FT (2510.16022)** applies IB to LLM fine-tuning for generalization -- closest in spirit but for code LLMs, not VLA/token pruning.

2. **GIB (2509.26327)** generalizes IB theory and could provide stronger theoretical tools than the standard IB framework.

3. **IBTM (withdrawn ICLR 2025)** combines IB with token merging in ViTs -- closest mechanistically but lacks generalization analysis and was not published.

4. **Kong et al. (2505.18227)** explicitly argues token reduction goes beyond efficiency -- provides empirical motivation but no formal theory.

5. **Kawaguchi et al. (ICML 2023)** proves IB helps generalization with formal bounds -- essential theoretical foundation.

6. **SP-VLA (ICLR 2026)** is the highest-venue VLA token pruning paper and must be cited as a key practical baseline.

7. The **explosion of VLA-specific token pruning methods** in late 2025 through early 2026 (LightVLA, VLA-Pruner, VLA-IAP, BFA++, SP-VLA, SpecPrune-VLA, SQAP-VLA, DTP, FocusVLA, SemanticVLA) means the proposal's related work section needs comprehensive coverage of this rapidly growing subfield -- at least 7-8 of these should be cited.

Sources:
- [DTP (arXiv 2601.16065)](https://arxiv.org/abs/2601.16065)
- [FocusVLA (arXiv 2603.28740)](https://arxiv.org/abs/2603.28740)
- [SemanticVLA (arXiv 2511.10518)](https://arxiv.org/abs/2511.10518)
- [IB-FT (arXiv 2510.16022)](https://arxiv.org/abs/2510.16022)
- [LIBERO-Plus (arXiv 2510.13626)](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus CVPR 2026 Poster](https://cvpr.thecvf.com/virtual/2026/poster/38735)
- [GIB (arXiv 2509.26327)](https://arxiv.org/abs/2509.26327)
- [Token Reduction Beyond Efficiency (arXiv 2505.18227)](https://arxiv.org/abs/2505.18227)
- [Token Pruning: Right Problem? (arXiv 2502.11501)](https://arxiv.org/abs/2502.11501)
- [LightVLA (arXiv 2509.12594)](https://arxiv.org/abs/2509.12594)
- [VLA-Pruner (arXiv 2511.16449)](https://arxiv.org/abs/2511.16449)
- [VLA-IAP (arXiv 2603.22991)](https://arxiv.org/abs/2603.22991)
- [BFA++ (arXiv 2602.20566)](https://arxiv.org/abs/2602.20566)
- [SP-VLA (arXiv 2506.12723) -- ICLR 2026](https://arxiv.org/abs/2506.12723)
- [SpecPrune-VLA (arXiv 2509.05614)](https://arxiv.org/abs/2509.05614)
- [SQAP-VLA (arXiv 2509.09090)](https://arxiv.org/abs/2509.09090)
- [VTrans (arXiv 2406.05276)](https://arxiv.org/abs/2406.05276)
- [IBTM (OpenReview, Withdrawn)](https://openreview.net/forum?id=Jwgw3znxT3)
- [Token Communication IB (arXiv 2507.01728)](https://arxiv.org/abs/2507.01728)
- [How Does IB Help Deep Learning? (arXiv 2305.18887)](https://arxiv.org/abs/2305.18887)
- [Unified PAC-Bayes (arXiv 2601.08100)](https://arxiv.org/abs/2601.08100)
- [PAC-Bayes Control (arXiv 1806.04225)](https://arxiv.org/abs/1806.04225)
- [PAC-Bayes Linear Control (arXiv 2605.10493)](https://arxiv.org/abs/2605.10493)
- [FASA -- ICLR 2026 (arXiv 2602.03152)](https://arxiv.org/abs/2602.03152)
- [Comprehensive IB for ViTs (CVPR 2025)](https://arxiv.org/abs/2507.04388)

agentId: abfca38d966f31a7a (use SendMessage with to: 'abfca38d966f31a7a' to continue this agent)
&lt;usage>total_tokens: 43472
tool_uses: 36
duration_ms: 208493&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3188f3f8-2211-4973-bbc2-198c08a0726a",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "6d9ba605-9540-4d14-b268-8c7e7113e2dd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML research proposal about using Information Bottleneck (IB) theory to explain why token pruning improves VLA (Vision-Language-Action) model generalization. I need to search for competing or missing related work that the proposal may have overlooked. Please conduct the following searches:\n\n1. Search for \"information bottleneck token pruning generalization 2025 2026\" on arXiv\n2. Search for \"VLA token pruning theory\" or \"vision language action pruning theoretical\"\n3. Search for \"PAC-Bayes generalization bounds robotics 2025 2026\"\n4. Search for \"DTP distracting token pruning VLA\" (arXiv 2601.16065) — verify it exists\n5. Search for \"FocusVLA\" (arXiv 2603.28740) — verify it exists\n6. Search for \"SemanticVLA\" (arXiv 2511.10518) — verify it exists and is AAAI 2026 Oral\n7. Search for \"IB-FT information bottleneck fine-tuning LLM generalization\" (arXiv 2510.16022)\n8. Search for \"token reduction generalization vision language model 2026\" to find any very recent work\n9. Search for \"LIBERO-Plus\" benchmark (arXiv 2510.13626) — verify it exists and is CVPR 2026\n\nFor each found paper, report: title, authors, venue, and a 1-2 sentence summary of what it does. Focus especially on finding work that directly combines IB theory with token pruning/selection for generalization analysis.",
    "agentId": "abfca38d966f31a7a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Here is my full report.\n\n---\n\n## Search Results: Related Work for IB Theory + Token Pruning in VLA Models\n\n### 1. Verification of Papers Cited in the Proposal\n\n**DTP (arXiv 2601.16065) -- VERIFIED**\n- **Title:** \"DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models\"\n- **Authors:** Chenyang Li, Jieyuan Liu, Bin Li, Bo Gao, Yilin Yuan, Yangfan He, Yuchen Li, Jingqun Tang\n- **Date:** January 22, 2026; arXiv preprint (no confirmed venue acceptance)\n- **Summary:** Introduces a plug-and-play framework that dynamically detects and prunes \"distracting\" (task-irrelevant) image tokens in VLA models. Shows a negative correlation between attention to task-irrelevant regions and success rate. Does NOT discuss IB theory or generalization theory.\n\n**FocusVLA (arXiv 2603.28740) -- VERIFIED**\n- **Title:** \"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models\"\n- **Authors:** Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan\n- **Date:** March 30, 2026; arXiv preprint (no confirmed venue)\n- **Summary:** Proposes Modality Cascaded Attention and Focus Attention to force VLA models to rely on task-relevant visual details. Argues performance is limited by how visual information is utilized, not by representation quality. Does NOT discuss IB theory or generalization theory -- purely empirical/architectural.\n\n**SemanticVLA (arXiv 2511.10518) -- VERIFIED as AAAI 2026 Oral**\n- **Title:** \"SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation\"\n- **Authors:** Wei Li, Renshan Zhang, Rui Shao, Zhijian Fang, Kaiwen Zhou, Zhuotao Tian, Liqiang Nie\n- **Date:** November 13, 2025; **Confirmed AAAI 2026 Oral**\n- **Summary:** Uses a Semantic-guided Dual Visual Pruner (SD-Pruner) with instruction-driven and spatial-aggregation sub-pruners. Achieves 97.7% success on LIBERO with 3x training cost reduction and 2.7x inference speedup. Does NOT use IB theory.\n\n**IB-FT (arXiv 2510.16022) -- VERIFIED**\n- **Title:** \"Breaking Memorization Barriers in LLM Code Fine-Tuning via Information Bottleneck for Improved Generalization\"\n- **Authors:** Changsheng Wang, Xin Chen, Sijia Liu, Ke Ding\n- **Date:** October 15, 2025; arXiv preprint\n- **Summary:** Applies an IB penalty on hidden representations during LLM code fine-tuning to compress spurious/memorized features while preserving task-relevant information. This is the closest existing work combining IB with generalization for large models, but it addresses code LLM fine-tuning, NOT token pruning or VLA models.\n\n**LIBERO-Plus (arXiv 2510.13626) -- VERIFIED as CVPR 2026 Poster**\n- **Title:** \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\" (subtitle on CVPR page: \"A Progressive Robustness Benchmark for Visual-Language-Action Models\")\n- **Authors:** Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, Xipeng Qiu\n- **Date:** October 15, 2025; **Confirmed CVPR 2026 Poster** (verified via cvpr.thecvf.com/virtual/2026/poster/38735)\n- **Summary:** Systematic robustness analysis of VLA models across 7 perturbation dimensions. Reveals brittleness: performance drops from 95% to below 30% under modest perturbations. Shows models largely ignore language instructions.\n\n---\n\n### 2. Key Competing / Related Work the Proposal May Be Missing\n\n#### A. VLA Token Pruning Methods (Direct Competitors -- Strong Coverage Needed)\n\n**LightVLA (arXiv 2509.12594)**\n- **Title:** \"The Better You Learn, The Smarter You Prune: Towards Efficient VLA Models via Differentiable Token Pruning\"\n- **Authors:** Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang\n- **Date:** September 16, 2025; under review\n- **Summary:** First work applying differentiable (learnable) token pruning to VLA, using Gumbel softmax for differentiable selection. Achieves 59.1% FLOPs reduction with 2.9% success rate improvement. Important because it claims simultaneous efficiency AND performance gains -- relevant to any generalization argument.\n\n**VLA-Pruner (arXiv 2511.16449)**\n- **Title:** \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference\"\n- **Date:** November 2025\n- **Summary:** Dual-level importance criterion combining vision-language prefill attention (semantic) and action decode attention (action-level), with temporal smoothing. Addresses the criticism that VLM pruning methods ignore VLA's dual-system nature.\n\n**VLA-IAP (arXiv 2603.22991)**\n- **Title:** \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n- **Date:** March 24, 2026\n- **Summary:** Training-free method introducing geometric prior and dynamic scheduling for conservative-to-aggressive pruning. Achieves 97.8% success with 1.54x speedup. Emphasizes preserving structurally critical manipulation regions.\n\n**BFA++ (arXiv 2602.20566)**\n- **Title:** \"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model\"\n- **Date:** February 24, 2026\n- **Summary:** Hierarchical pruning for multi-view VLA with intra-view and inter-view importance predictors. Addresses multi-camera setups specifically.\n\n**SP-VLA (arXiv 2506.12723) -- ICLR 2026**\n- **Title:** \"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration\"\n- **Date:** June 2025; **Accepted at ICLR 2026**\n- **Summary:** Combines action-aware model scheduling (switching between full VLA and lightweight generator) with spatio-semantic dual-aware token pruning. Achieves up to 6% performance gain with 2.4x acceleration. This is the highest-venue VLA pruning paper found (ICLR 2026).\n\n**SpecPrune-VLA (arXiv 2509.05614)**\n- **Title:** \"SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning\"\n- **Date:** September 2025\n- **Summary:** Training-free, two-level pruning exploiting temporal similarity between consecutive frames. Uses action granularity (coarse vs. fine) to dynamically adjust pruning aggressiveness.\n\n**SQAP-VLA (arXiv 2509.09090)**\n- **Title:** \"SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance VLA Models\"\n- **Authors:** Hengyu Fang, Yijiang Liu, Yuan Du, Li Du, Huanrui Yang\n- **Date:** September 11, 2025\n- **Summary:** First framework jointly enabling quantization and token pruning for VLA. Co-designs both to overcome observed incompatibility between aggressive quantization and token pruning.\n\n#### B. Information Bottleneck Theory (Theoretical Foundations)\n\n**Generalized Information Bottleneck (GIB) (arXiv 2509.26327)**\n- **Title:** \"A Generalized Information Bottleneck Theory of Deep Learning\"\n- **Authors:** Charles Westphal, Stephen Hailes, Mirco Musolesi\n- **Date:** September 30, 2025 (revised January 30, 2026)\n- **Summary:** Reformulates IB through \"synergy\" (information obtainable only through joint processing of features). Shows synergistic functions achieve superior generalization. Achieves compression phases even with ReLU activations where standard IB theory fails. HIGHLY RELEVANT: this could provide the theoretical backbone for explaining why pruning (which removes non-synergistic/redundant tokens) improves generalization.\n\n**How Does Information Bottleneck Help Deep Learning? (arXiv 2305.18887, ICML 2023)**\n- **Authors:** Kenji Kawaguchi et al.\n- **Summary:** Provides rigorous learning theory relating IB to generalization errors, with new generalization bounds that scale with the degree of information bottleneck. KEY FOUNDATIONAL REFERENCE for any IB-based generalization argument.\n\n**Token Communication via Information Bottleneck (arXiv 2507.01728)**\n- **Title:** \"Token Communication in the Era of Large Models: An Information Bottleneck-Based Approach\"\n- **Authors:** Hao Wei, Wanli Ni, Wen Wang, Wenjun Xu, Dusit Niyato, Ping Zhang\n- **Date:** July 2, 2025\n- **Summary:** Proposes Generative Information Bottleneck (GenIB) for learning tokens that preserve essential information while supporting generation across modalities. While focused on wireless communication, the GenIB formulation for token-level IB is directly relevant.\n\n#### C. IB + Vision Transformer Token Methods\n\n**IBTM: IB-Inspired Token Merging (OpenReview, Withdrawn from ICLR 2025)**\n- **Title:** \"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging\"\n- **Authors:** Yancheng Wang, Yingzhen Yang\n- **Summary:** Derives a separable variational upper bound for the IB loss to guide learnable token merging. This is the closest existing work to combining IB with token reduction in vision transformers, though it was withdrawn from ICLR 2025 and does NOT discuss generalization theory.\n\n**VTrans: Variational IB-Based Pruning (arXiv 2406.05276)**\n- **Title:** \"VTrans: Accelerating Transformer Compression with Variational Information Bottleneck based Pruning\"\n- **Authors:** Oshin Dutta, Ritvik Gupta, Sumeet Agarwal\n- **Date:** June 2024\n- **Summary:** Uses VIB to guide structural (head/layer) pruning -- NOT token pruning. Achieves 70% more compression than prior art.\n\n**Comprehensive IB for Vision Transformers (CVPR 2025)**\n- **Title:** \"Comprehensive Information Bottleneck for Unveiling Universal Attribution to Interpret Vision Transformers\"\n- **Summary:** Uses IB to explain ViT decision-making via layer-wise attribution. Interpretability-focused rather than pruning/generalization.\n\n#### D. Token Reduction Beyond Efficiency (Position/Survey Papers)\n\n**Token Reduction Should Go Beyond Efficiency (arXiv 2505.18227)**\n- **Title:** \"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality\"\n- **Authors:** Zhenglun Kong, Yize Li, Fanhu Zeng, Lei Xin, Shvat Messica, Xue Lin, Pu Zhao, Manolis Kellis, Hao Tang, Marinka Zitnik\n- **Date:** May 23, 2025 (revised January 12, 2026)\n- **Summary:** Position paper arguing token reduction is a \"fundamental principle in generative modeling\" beyond efficiency -- impacting multimodal integration, hallucination mitigation, coherence, and training stability. DIRECTLY RELEVANT to the proposal's thesis that pruning improves generalization.\n\n**Token Pruning in MLLMs: Are We Solving the Right Problem? (arXiv 2502.11501, ACL 2025 Findings)**\n- **Title:** \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\"\n- **Authors:** Zichen Wen, Yifeng Gao, Weijia Li, Conghui He, Linfeng Zhang\n- **Date:** February 17, 2025; **ACL 2025 Findings**\n- **Summary:** Critical analysis showing many token pruning methods underperform random selection. Questions whether attention-based scoring is sufficient and whether current evaluation protocols are comprehensive. Important cautionary counterpoint.\n\n#### E. PAC-Bayes for Control/Robotics\n\n**PAC-Bayes Control (arXiv 1806.04225)**\n- **Title:** \"PAC-Bayes Control: Learning Policies that Provably Generalize to Novel Environments\"\n- **Summary:** Foundational work applying PAC-Bayes to learned control policies, proving generalization to novel environments. Directly relevant if the proposal uses PAC-Bayes bounds.\n\n**Unified PAC-Bayesian Framework (arXiv 2601.08100)**\n- **Title:** \"Towards A Unified PAC-Bayesian Framework for Norm-based Generalization Bounds\"\n- **Date:** January 2026\n- **Summary:** Derives a family of bounds recovering existing PAC-Bayesian results as special cases. Could provide tighter bounds for the proposal's analysis.\n\n**PAC-Bayes for Linear Control (arXiv 2605.10493)**\n- **Title:** \"A PAC-Bayes Approach for Controlling Unknown Linear Discrete-time Systems\"\n- **Date:** May 2026\n- **Summary:** Very recent application of PAC-Bayes to control systems with unknown dynamics.\n\n---\n\n### 3. Critical Gap Analysis\n\n**The key finding: No existing paper directly combines IB theory with token pruning/selection to provide a formal generalization analysis for VLA models.** This is the novel contribution space for the proposal. However, several adjacent works should be cited and distinguished:\n\n1. **IB-FT (2510.16022)** applies IB to LLM fine-tuning for generalization -- closest in spirit but for code LLMs, not VLA/token pruning.\n\n2. **GIB (2509.26327)** generalizes IB theory and could provide stronger theoretical tools than the standard IB framework.\n\n3. **IBTM (withdrawn ICLR 2025)** combines IB with token merging in ViTs -- closest mechanistically but lacks generalization analysis and was not published.\n\n4. **Kong et al. (2505.18227)** explicitly argues token reduction goes beyond efficiency -- provides empirical motivation but no formal theory.\n\n5. **Kawaguchi et al. (ICML 2023)** proves IB helps generalization with formal bounds -- essential theoretical foundation.\n\n6. **SP-VLA (ICLR 2026)** is the highest-venue VLA token pruning paper and must be cited as a key practical baseline.\n\n7. The **explosion of VLA-specific token pruning methods** in late 2025 through early 2026 (LightVLA, VLA-Pruner, VLA-IAP, BFA++, SP-VLA, SpecPrune-VLA, SQAP-VLA, DTP, FocusVLA, SemanticVLA) means the proposal's related work section needs comprehensive coverage of this rapidly growing subfield -- at least 7-8 of these should be cited.\n\nSources:\n- [DTP (arXiv 2601.16065)](https://arxiv.org/abs/2601.16065)\n- [FocusVLA (arXiv 2603.28740)](https://arxiv.org/abs/2603.28740)\n- [SemanticVLA (arXiv 2511.10518)](https://arxiv.org/abs/2511.10518)\n- [IB-FT (arXiv 2510.16022)](https://arxiv.org/abs/2510.16022)\n- [LIBERO-Plus (arXiv 2510.13626)](https://arxiv.org/abs/2510.13626)\n- [LIBERO-Plus CVPR 2026 Poster](https://cvpr.thecvf.com/virtual/2026/poster/38735)\n- [GIB (arXiv 2509.26327)](https://arxiv.org/abs/2509.26327)\n- [Token Reduction Beyond Efficiency (arXiv 2505.18227)](https://arxiv.org/abs/2505.18227)\n- [Token Pruning: Right Problem? (arXiv 2502.11501)](https://arxiv.org/abs/2502.11501)\n- [LightVLA (arXiv 2509.12594)](https://arxiv.org/abs/2509.12594)\n- [VLA-Pruner (arXiv 2511.16449)](https://arxiv.org/abs/2511.16449)\n- [VLA-IAP (arXiv 2603.22991)](https://arxiv.org/abs/2603.22991)\n- [BFA++ (arXiv 2602.20566)](https://arxiv.org/abs/2602.20566)\n- [SP-VLA (arXiv 2506.12723) -- ICLR 2026](https://arxiv.org/abs/2506.12723)\n- [SpecPrune-VLA (arXiv 2509.05614)](https://arxiv.org/abs/2509.05614)\n- [SQAP-VLA (arXiv 2509.09090)](https://arxiv.org/abs/2509.09090)\n- [VTrans (arXiv 2406.05276)](https://arxiv.org/abs/2406.05276)\n- [IBTM (OpenReview, Withdrawn)](https://openreview.net/forum?id=Jwgw3znxT3)\n- [Token Communication IB (arXiv 2507.01728)](https://arxiv.org/abs/2507.01728)\n- [How Does IB Help Deep Learning? (arXiv 2305.18887)](https://arxiv.org/abs/2305.18887)\n- [Unified PAC-Bayes (arXiv 2601.08100)](https://arxiv.org/abs/2601.08100)\n- [PAC-Bayes Control (arXiv 1806.04225)](https://arxiv.org/abs/1806.04225)\n- [PAC-Bayes Linear Control (arXiv 2605.10493)](https://arxiv.org/abs/2605.10493)\n- [FASA -- ICLR 2026 (arXiv 2602.03152)](https://arxiv.org/abs/2602.03152)\n- [Comprehensive IB for ViTs (CVPR 2025)](https://arxiv.org/abs/2507.04388)"
      }
    ],
    "totalDurationMs": 208493,
    "totalTokens": 43472,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 878,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 35793,
      "output_tokens": 4844,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 878,
          "output_tokens": 4844,
          "cache_read_input_tokens": 35793,
          "cache_creation_input_tokens": 1957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1957,
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
      "otherToolCount": 36
    }
  },
  "sourceToolAssistantUUID": "3188f3f8-2211-4973-bbc2-198c08a0726a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6d9ba605-9540-4d14-b268-8c7e7113e2dd",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "VLA token pruning: discrete IB theory under domain shift",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Tool call

_source line 16 · 2026-05-13T05:25:02.726Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JeACFbRQz29DVSJwz1GrU9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search PAC-Bayes vacuity and IB criticism",
  "prompt": "I'm reviewing a research proposal that claims to derive PAC-Bayes generalization bounds for VLA (Vision-Language-Action) models with 7B parameters, fine-tuned with LoRA. The proposal acknowledges bounds will likely be vacuous but claims \"ordinal predictions\" from the bound are still informative. I need to verify several specific claims:\n\n1. Search for \"PAC-Bayes bounds vacuous overparameterized large models 2024 2025 2026\" — find the latest understanding of whether PAC-Bayes bounds can be non-vacuous for large models, especially with LoRA.\n\n2. Search for \"SubLoRA LoRA generalization bounds fine-tuning\" — is there work applying SubLoRA-style compression bounds specifically to LoRA-fine-tuned models?\n\n3. Search for \"ordinal predictions vacuous bounds model selection\" — is there theoretical justification for using vacuous bounds for ranking/model selection?\n\n4. Search for \"MDL minimum description length model selection PAC-Bayes\" — find work connecting MDL with PAC-Bayes for model selection justification.\n\n5. Search for \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\" (arXiv 2502.11501) — this paper reportedly shows many pruning methods underperform random selection. Verify and summarize.\n\n6. Search for \"IBTM information bottleneck token merging vision transformer\" — any work combining IB with token merging/reduction in vision transformers.\n\n7. Search for \"SP-VLA ICLR 2026\" — verify SP-VLA was accepted at ICLR 2026, as this would be the highest-venue VLA token pruning paper.\n\nReport findings concisely. Focus especially on whether the SubLoRA/token-as-data-point approach has been validated for LoRA fine-tuned models specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d9ba605-9540-4d14-b268-8c7e7113e2dd",
  "isSidechain": false,
  "requestId": "req_011Caz1bQDw63hvpwGp9DNXY",
  "type": "assistant",
  "uuid": "dd95d806-457e-4845-b4f5-0f925ea1198f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeaaAubG8XUZZxkR6acJv7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5395,
      "cache_read_input_tokens": 34634,
      "output_tokens": 541,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 541,
          "cache_read_input_tokens": 34634,
          "cache_creation_input_tokens": 5395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5395
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

_source line 17 · 2026-05-13T05:27:21.574Z_

<details><summary>↩ Tool result · `toolu_01JeACFbRQz29DVSJwz1GrU9`</summary>

```text
Now I have comprehensive information across all seven queries. Here is the consolidated report.

---

## Findings Report

### 1. PAC-Bayes Bounds for Large/Overparameterized Models (incl. LoRA)

The field has made significant progress since 2023:

- **Lotfi et al. (NeurIPS 2024 Spotlight)** -- "Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models" achieves **non-vacuous bounds for LLaMA2-70B** by treating each token as a data point via martingale concentration, combined with Monarch matrices, Kronecker factorizations, and post-training quantization. This is the current state of the art.

- **The original SubLoRA work** (Lotfi et al., 2023) achieved non-vacuous bounds for smaller LLMs but the SubLoRA-compressed models generated low-quality, ungrammatical text. The 2024 token-level follow-up fixed this, achieving non-vacuous bounds for models that actually generate high-quality text.

- **Kim et al. (May 2025)** show non-vacuous bounds via model fusion with as few as 100 examples for 7B-scale models.

- **Than et al. (March 2025)** apply bounds to unmodified pretrained models without retraining.

**Critical caveat for the proposal**: The existing non-vacuous results are for **pretraining** bounds on next-token prediction. I found **no published work** applying SubLoRA or token-as-data-point bounds specifically to **LoRA-fine-tuned** models. The proposal's claim would be extending these techniques to a novel setting (fine-tuning), and acknowledging vacuousness is realistic -- the token-level trick helps because pretraining datasets have billions of tokens, but fine-tuning datasets are much smaller.

### 2. SubLoRA Applied to LoRA Fine-Tuned Models

**No direct work found.** SubLoRA was designed for **pretraining from scratch** -- it combines LoRA-style low-rank structure with subspace training to pretrain compressible models. It is not an approach applied post-hoc to LoRA-fine-tuned models. The GitHub repository ([Sanaelotfi/SubLoRA-bounds-for-LLMs](https://github.com/Sanaelotfi/SubLoRA-bounds-for-LLMs)) confirms this scope. Using LoRA alone yields vacuous bounds for top-1 error; it is SubLoRA's additional subspace compression that achieves non-vacuity, and only in the pretraining regime.

**The proposal's implicit claim that SubLoRA bounds transfer to LoRA fine-tuning is not validated in the literature.** This would be a novel contribution requiring its own justification.

### 3. Ordinal Predictions from Vacuous Bounds

**Weak theoretical support found.** The idea that vacuous PAC-Bayes bounds can still be useful for ordinal ranking/model selection is a folk belief in the community, not a well-established theorem. Key observations:

- Dziugaite & Roy (2017) showed PAC-Bayes bounds can be optimized directly, and tighter bounds correlate with better generalization, but their bounds were non-vacuous.

- A critical 2025 paper -- **"How good is PAC-Bayes at explaining generalisation?"** (arXiv 2503.08231) -- argues that non-vacuous PAC-Bayes certificates in deep learning arise primarily from **prior engineering** encoding generalization knowledge already, and that PAC-Bayes "certifies but does not explain" generalization. This casts doubt on whether ordinal rankings from bounds reflect genuine learning dynamics vs. artifacts of the prior.

- PAC-Bayes bounds have been used for model selection (McAllester, 1999), but this literature assumes non-vacuous bounds. **I found no rigorous theoretical justification for the specific claim that vacuous bounds preserve useful ordinal information for ranking.**

### 4. MDL and PAC-Bayes Connection

The connection is well-established at a high level:

- PAC-Bayes is widely recognized as a generalization of MDL/Occam's razor: both frameworks favor models that compress data well.

- **Lotfi et al. (NeurIPS 2022)** -- "PAC-Bayes Compression Bounds So Tight That They Can Explain Generalization" -- explicitly frames PAC-Bayes as a compression/MDL framework and achieves tight bounds via quantization in linear subspaces.

- However, MDL's model selection guarantees (e.g., convergence to the true model in the MDL sense) do not automatically transfer to PAC-Bayes bounds. The connection is conceptual/inspirational rather than a formal equivalence that licenses using one framework's guarantees within the other.

### 5. Token Pruning Paper (arXiv 2502.11501)

**Verified.** "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?" by Wen et al. (Feb 2025, published in ACL 2025 Findings). Key findings:

- **Random token pruning and average pooling baselines outperform well-known methods** (FastV, SparseVLM) on most benchmarks at 75% and 87.5% pruning ratios.

- The paper questions whether attention-based scoring reliably identifies redundant tokens, whether language information helps during token pruning, and what trade-off between token importance and duplication works best.

- A related paper (arXiv 2512.07580) -- "When Token Pruning is Worse than Random" -- reinforces this finding.

- The paper argues that most previous works ignored comparison against these simple baselines, making their claimed improvements unreliable.

### 6. IBTM: Information Bottleneck Token Merging

**Found.** "Efficient Visual Transformer by Learnable Token Merging" (also called IBTM -- Information Bottleneck inspired Token Merging) appears on [OpenReview](https://openreview.net/forum?id=Jwgw3znxT3) and [arXiv 2407.15219](https://arxiv.org/abs/2407.15219):

- Derives a separable variational upper bound for the Information Bottleneck loss.
- Replaces standard transformer blocks with IBTM blocks that generate learnable token merging masks.
- Compatible with MobileViT, EfficientViT, ViT, and Swin Transformer.
- Reduces FLOPs and inference time while maintaining or improving accuracy.

This is vision-only work (image classification). It has **not been applied to multimodal VLA settings**.

### 7. SP-VLA at ICLR 2026

**Important disambiguation -- there are TWO papers named "SP-VLA":**

1. **SP-VLA / ST4VLA: "Spatially Guided Training for Vision-Language-Action Models"** (arXiv 2602.10109) -- **Confirmed accepted at ICLR 2026** as a poster. This paper is about a training methodology using spatial priors (point, box, trajectory prediction) to improve VLA performance. It is NOT about token pruning. It achieved SOTA on SimplerEnv (66.1 to 84.6 on Google Robot).

2. **SP-VLA: "A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration"** (arXiv 2506.12723) -- This is the token pruning paper. It uses action-aware model scheduling + spatio-semantic dual-aware token pruning. It achieves 1.35x speedup with no accuracy loss. This paper is a **preprint**, NOT accepted at ICLR 2026. It has an OpenReview page but appears to be under review or rejected.

**If the proposal cites SP-VLA as "the highest-venue VLA token pruning paper accepted at ICLR 2026," this is incorrect.** The ICLR 2026 SP-VLA is about spatial training, not token pruning. The token-pruning SP-VLA is a separate, later preprint.

---

## Summary of Red Flags in the Proposal

1. **SubLoRA for LoRA fine-tuning**: Not validated. SubLoRA was designed for pretraining; no one has shown it works for LoRA fine-tuned models.

2. **"Ordinal predictions from vacuous bounds"**: No rigorous theoretical backing found. A 2025 paper (arXiv 2503.08231) actively undermines this by showing PAC-Bayes certificates reflect prior engineering rather than learning dynamics.

3. **SP-VLA confusion**: The ICLR 2026 paper is about spatial training, not token pruning. The token pruning SP-VLA is a separate preprint not (yet) at a top venue.

4. **Token pruning viability**: The Wen et al. (2502.11501) finding that random pruning outperforms sophisticated methods is real and published (ACL 2025 Findings), which could undermine token-pruning-based efficiency arguments in the proposal.

Sources:
- [Unlocking Tokens as Data Points (NeurIPS 2024)](https://arxiv.org/abs/2407.18158)
- [SubLoRA bounds for LLMs (GitHub)](https://github.com/Sanaelotfi/SubLoRA-bounds-for-LLMs)
- [Non-Vacuous Generalization Bounds for LLMs (Lotfi et al.)](https://arxiv.org/html/2312.17173v2)
- [How good is PAC-Bayes at explaining generalisation? (2025)](https://arxiv.org/abs/2503.08231)
- [PAC-Bayes Compression Bounds (NeurIPS 2022)](https://arxiv.org/abs/2211.13609)
- [Token Pruning in MLLMs (arXiv 2502.11501)](https://arxiv.org/abs/2502.11501)
- [When Token Pruning is Worse than Random](https://arxiv.org/abs/2512.07580)
- [IBTM: Efficient Visual Transformer by Learnable Token Merging](https://arxiv.org/abs/2407.15219)
- [SP-VLA: Spatially Guided Training (ICLR 2026)](https://openreview.net/forum?id=eKhOrQWAVJ)
- [SP-VLA: Joint Model Scheduling and Token Pruning (preprint)](https://arxiv.org/abs/2506.12723)
- [Non-Vacuous Generalization Bounds (Emergent Mind topic)](https://www.emergentmind.com/topics/non-vacuous-generalization-bounds)
- [Dziugaite & Roy 2017](https://arxiv.org/abs/1703.11008)

agentId: a2bab8a13f723fe85 (use SendMessage with to: 'a2bab8a13f723fe85' to continue this agent)
&lt;usage>total_tokens: 32363
tool_uses: 19
duration_ms: 138843&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd95d806-457e-4845-b4f5-0f925ea1198f",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "263132d5-aeb6-4a1d-a7df-e86063cea5ec",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal that claims to derive PAC-Bayes generalization bounds for VLA (Vision-Language-Action) models with 7B parameters, fine-tuned with LoRA. The proposal acknowledges bounds will likely be vacuous but claims \"ordinal predictions\" from the bound are still informative. I need to verify several specific claims:\n\n1. Search for \"PAC-Bayes bounds vacuous overparameterized large models 2024 2025 2026\" — find the latest understanding of whether PAC-Bayes bounds can be non-vacuous for large models, especially with LoRA.\n\n2. Search for \"SubLoRA LoRA generalization bounds fine-tuning\" — is there work applying SubLoRA-style compression bounds specifically to LoRA-fine-tuned models?\n\n3. Search for \"ordinal predictions vacuous bounds model selection\" — is there theoretical justification for using vacuous bounds for ranking/model selection?\n\n4. Search for \"MDL minimum description length model selection PAC-Bayes\" — find work connecting MDL with PAC-Bayes for model selection justification.\n\n5. Search for \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\" (arXiv 2502.11501) — this paper reportedly shows many pruning methods underperform random selection. Verify and summarize.\n\n6. Search for \"IBTM information bottleneck token merging vision transformer\" — any work combining IB with token merging/reduction in vision transformers.\n\n7. Search for \"SP-VLA ICLR 2026\" — verify SP-VLA was accepted at ICLR 2026, as this would be the highest-venue VLA token pruning paper.\n\nReport findings concisely. Focus especially on whether the SubLoRA/token-as-data-point approach has been validated for LoRA fine-tuned models specifically.",
    "agentId": "a2bab8a13f723fe85",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information across all seven queries. Here is the consolidated report.\n\n---\n\n## Findings Report\n\n### 1. PAC-Bayes Bounds for Large/Overparameterized Models (incl. LoRA)\n\nThe field has made significant progress since 2023:\n\n- **Lotfi et al. (NeurIPS 2024 Spotlight)** -- \"Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models\" achieves **non-vacuous bounds for LLaMA2-70B** by treating each token as a data point via martingale concentration, combined with Monarch matrices, Kronecker factorizations, and post-training quantization. This is the current state of the art.\n\n- **The original SubLoRA work** (Lotfi et al., 2023) achieved non-vacuous bounds for smaller LLMs but the SubLoRA-compressed models generated low-quality, ungrammatical text. The 2024 token-level follow-up fixed this, achieving non-vacuous bounds for models that actually generate high-quality text.\n\n- **Kim et al. (May 2025)** show non-vacuous bounds via model fusion with as few as 100 examples for 7B-scale models.\n\n- **Than et al. (March 2025)** apply bounds to unmodified pretrained models without retraining.\n\n**Critical caveat for the proposal**: The existing non-vacuous results are for **pretraining** bounds on next-token prediction. I found **no published work** applying SubLoRA or token-as-data-point bounds specifically to **LoRA-fine-tuned** models. The proposal's claim would be extending these techniques to a novel setting (fine-tuning), and acknowledging vacuousness is realistic -- the token-level trick helps because pretraining datasets have billions of tokens, but fine-tuning datasets are much smaller.\n\n### 2. SubLoRA Applied to LoRA Fine-Tuned Models\n\n**No direct work found.** SubLoRA was designed for **pretraining from scratch** -- it combines LoRA-style low-rank structure with subspace training to pretrain compressible models. It is not an approach applied post-hoc to LoRA-fine-tuned models. The GitHub repository ([Sanaelotfi/SubLoRA-bounds-for-LLMs](https://github.com/Sanaelotfi/SubLoRA-bounds-for-LLMs)) confirms this scope. Using LoRA alone yields vacuous bounds for top-1 error; it is SubLoRA's additional subspace compression that achieves non-vacuity, and only in the pretraining regime.\n\n**The proposal's implicit claim that SubLoRA bounds transfer to LoRA fine-tuning is not validated in the literature.** This would be a novel contribution requiring its own justification.\n\n### 3. Ordinal Predictions from Vacuous Bounds\n\n**Weak theoretical support found.** The idea that vacuous PAC-Bayes bounds can still be useful for ordinal ranking/model selection is a folk belief in the community, not a well-established theorem. Key observations:\n\n- Dziugaite & Roy (2017) showed PAC-Bayes bounds can be optimized directly, and tighter bounds correlate with better generalization, but their bounds were non-vacuous.\n\n- A critical 2025 paper -- **\"How good is PAC-Bayes at explaining generalisation?\"** (arXiv 2503.08231) -- argues that non-vacuous PAC-Bayes certificates in deep learning arise primarily from **prior engineering** encoding generalization knowledge already, and that PAC-Bayes \"certifies but does not explain\" generalization. This casts doubt on whether ordinal rankings from bounds reflect genuine learning dynamics vs. artifacts of the prior.\n\n- PAC-Bayes bounds have been used for model selection (McAllester, 1999), but this literature assumes non-vacuous bounds. **I found no rigorous theoretical justification for the specific claim that vacuous bounds preserve useful ordinal information for ranking.**\n\n### 4. MDL and PAC-Bayes Connection\n\nThe connection is well-established at a high level:\n\n- PAC-Bayes is widely recognized as a generalization of MDL/Occam's razor: both frameworks favor models that compress data well.\n\n- **Lotfi et al. (NeurIPS 2022)** -- \"PAC-Bayes Compression Bounds So Tight That They Can Explain Generalization\" -- explicitly frames PAC-Bayes as a compression/MDL framework and achieves tight bounds via quantization in linear subspaces.\n\n- However, MDL's model selection guarantees (e.g., convergence to the true model in the MDL sense) do not automatically transfer to PAC-Bayes bounds. The connection is conceptual/inspirational rather than a formal equivalence that licenses using one framework's guarantees within the other.\n\n### 5. Token Pruning Paper (arXiv 2502.11501)\n\n**Verified.** \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\" by Wen et al. (Feb 2025, published in ACL 2025 Findings). Key findings:\n\n- **Random token pruning and average pooling baselines outperform well-known methods** (FastV, SparseVLM) on most benchmarks at 75% and 87.5% pruning ratios.\n\n- The paper questions whether attention-based scoring reliably identifies redundant tokens, whether language information helps during token pruning, and what trade-off between token importance and duplication works best.\n\n- A related paper (arXiv 2512.07580) -- \"When Token Pruning is Worse than Random\" -- reinforces this finding.\n\n- The paper argues that most previous works ignored comparison against these simple baselines, making their claimed improvements unreliable.\n\n### 6. IBTM: Information Bottleneck Token Merging\n\n**Found.** \"Efficient Visual Transformer by Learnable Token Merging\" (also called IBTM -- Information Bottleneck inspired Token Merging) appears on [OpenReview](https://openreview.net/forum?id=Jwgw3znxT3) and [arXiv 2407.15219](https://arxiv.org/abs/2407.15219):\n\n- Derives a separable variational upper bound for the Information Bottleneck loss.\n- Replaces standard transformer blocks with IBTM blocks that generate learnable token merging masks.\n- Compatible with MobileViT, EfficientViT, ViT, and Swin Transformer.\n- Reduces FLOPs and inference time while maintaining or improving accuracy.\n\nThis is vision-only work (image classification). It has **not been applied to multimodal VLA settings**.\n\n### 7. SP-VLA at ICLR 2026\n\n**Important disambiguation -- there are TWO papers named \"SP-VLA\":**\n\n1. **SP-VLA / ST4VLA: \"Spatially Guided Training for Vision-Language-Action Models\"** (arXiv 2602.10109) -- **Confirmed accepted at ICLR 2026** as a poster. This paper is about a training methodology using spatial priors (point, box, trajectory prediction) to improve VLA performance. It is NOT about token pruning. It achieved SOTA on SimplerEnv (66.1 to 84.6 on Google Robot).\n\n2. **SP-VLA: \"A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration\"** (arXiv 2506.12723) -- This is the token pruning paper. It uses action-aware model scheduling + spatio-semantic dual-aware token pruning. It achieves 1.35x speedup with no accuracy loss. This paper is a **preprint**, NOT accepted at ICLR 2026. It has an OpenReview page but appears to be under review or rejected.\n\n**If the proposal cites SP-VLA as \"the highest-venue VLA token pruning paper accepted at ICLR 2026,\" this is incorrect.** The ICLR 2026 SP-VLA is about spatial training, not token pruning. The token-pruning SP-VLA is a separate, later preprint.\n\n---\n\n## Summary of Red Flags in the Proposal\n\n1. **SubLoRA for LoRA fine-tuning**: Not validated. SubLoRA was designed for pretraining; no one has shown it works for LoRA fine-tuned models.\n\n2. **\"Ordinal predictions from vacuous bounds\"**: No rigorous theoretical backing found. A 2025 paper (arXiv 2503.08231) actively undermines this by showing PAC-Bayes certificates reflect prior engineering rather than learning dynamics.\n\n3. **SP-VLA confusion**: The ICLR 2026 paper is about spatial training, not token pruning. The token pruning SP-VLA is a separate preprint not (yet) at a top venue.\n\n4. **Token pruning viability**: The Wen et al. (2502.11501) finding that random pruning outperforms sophisticated methods is real and published (ACL 2025 Findings), which could undermine token-pruning-based efficiency arguments in the proposal.\n\nSources:\n- [Unlocking Tokens as Data Points (NeurIPS 2024)](https://arxiv.org/abs/2407.18158)\n- [SubLoRA bounds for LLMs (GitHub)](https://github.com/Sanaelotfi/SubLoRA-bounds-for-LLMs)\n- [Non-Vacuous Generalization Bounds for LLMs (Lotfi et al.)](https://arxiv.org/html/2312.17173v2)\n- [How good is PAC-Bayes at explaining generalisation? (2025)](https://arxiv.org/abs/2503.08231)\n- [PAC-Bayes Compression Bounds (NeurIPS 2022)](https://arxiv.org/abs/2211.13609)\n- [Token Pruning in MLLMs (arXiv 2502.11501)](https://arxiv.org/abs/2502.11501)\n- [When Token Pruning is Worse than Random](https://arxiv.org/abs/2512.07580)\n- [IBTM: Efficient Visual Transformer by Learnable Token Merging](https://arxiv.org/abs/2407.15219)\n- [SP-VLA: Spatially Guided Training (ICLR 2026)](https://openreview.net/forum?id=eKhOrQWAVJ)\n- [SP-VLA: Joint Model Scheduling and Token Pruning (preprint)](https://arxiv.org/abs/2506.12723)\n- [Non-Vacuous Generalization Bounds (Emergent Mind topic)](https://www.emergentmind.com/topics/non-vacuous-generalization-bounds)\n- [Dziugaite & Roy 2017](https://arxiv.org/abs/1703.11008)"
      }
    ],
    "totalDurationMs": 138843,
    "totalTokens": 32363,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 28184,
      "output_tokens": 2626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2626,
          "cache_read_input_tokens": 28184,
          "cache_creation_input_tokens": 1552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1552,
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
  "sourceToolAssistantUUID": "dd95d806-457e-4845-b4f5-0f925ea1198f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T05:27:36.474Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01N13FJtGDbDgdC2ej1EgoJK`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search latest VLA pruning + generalization work",
  "prompt": "I'm conducting a final sweep for an ML research review on token pruning in VLA (Vision-Language-Action) models and generalization theory. I need to search for the most recent work (2026) that I might have missed. Please search:\n\n1. Search: \"GridS ICML 2026 VLA token pruning\" — verify GridS was accepted at ICML 2026 and what it does\n2. Search: \"OneWM-VLA arXiv 2605.07931\" — verify this May 2026 paper exists and its claims about 1 token per frame\n3. Search: \"EfficientVLA arXiv 2506.10100\" — verify existence\n4. Search: \"Compressor-VLA arXiv 2511.18950\" — verify existence\n5. Search: \"IBRO information bottleneck LLM reasoning arXiv 2507.18391\" — verify existence\n6. Search: \"InfoPrune VLM token pruning information budgeting\" — find this paper if it exists\n7. Search: \"Drop-Bottleneck learning discrete compressed representation\" arXiv 2103.12300 — verify existence\n8. Search: \"PAC-Bayes domain adaptation Germain 2016 ICML\" — verify this foundational reference\n9. Search: \"IBAC-SNI information bottleneck reinforcement learning generalization NeurIPS 2019\" — verify existence\n10. Search for any very recent (2026) work combining \"token pruning\" with \"distribution shift\" or \"out-of-distribution generalization\" in robotics/VLA\n\nReport findings concisely — existence confirmation plus 1-sentence summary for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "263132d5-aeb6-4a1d-a7df-e86063cea5ec",
  "isSidechain": false,
  "requestId": "req_011Caz1ntc3mG2CpX1np5J6R",
  "type": "assistant",
  "uuid": "437a5a7e-0f3f-4391-94c2-9c6df6cf5c00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ECYdAHqojTZ5Fu1yWu5UB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3246,
      "cache_read_input_tokens": 40029,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 40029,
          "cache_creation_input_tokens": 3246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3246
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

_source line 19 · 2026-05-13T05:29:02.113Z_

<details><summary>↩ Tool result · `toolu_01N13FJtGDbDgdC2ej1EgoJK`</summary>

```text
Here are the findings for all 10 searches:

---

**1. GridS -- ICML 2026 VLA token pruning**
**CONFIRMED.** GridS ("See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model") was accepted as a poster at ICML 2026. It introduces a plug-and-play module that adaptively predicts a minimal set of salient coordinates and extracts features via differentiable interpolation, preserving essential spatial information while compressing to fewer than 10% of visual tokens -- addressing the trade-off where aggressive pruning discards critical geometric details like contact points.

**2. OneWM-VLA -- arXiv 2605.07931**
**CONFIRMED.** "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy" (submitted May 8, 2026). It compresses each camera view into a single semantic token per frame via Adaptive Attention Pooling, and jointly trains world prediction and action generation under a single flow-matching objective on a pi0 (2B) backbone with 14.71M LoRA parameters, improving average success from 47.9% to 61.3% on MetaWorld MT50 and reaching 95.6% on LIBERO-Long.

**3. EfficientVLA -- arXiv 2506.10100**
**CONFIRMED.** "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models" (submitted June 11, 2025). It combines three strategies -- pruning redundant language-module layers, task-aware visual token selection, and diffusion action-head feature caching -- to yield 1.93x inference speedup and 28.9% FLOPs with only 0.6% success-rate drop on SIMPLER when applied to CogACT.

**4. Compressor-VLA -- arXiv 2511.18950**
**CONFIRMED.** "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation" (November 2025). It uses a Semantic Task Compressor (STC) for holistic task-relevant context and a Spatial Refinement Compressor (SRC) for fine-grained spatial details, both dynamically modulated by natural language instructions, achieving 59% FLOPs reduction and >3x visual token compression on LIBERO with competitive success rates.

**5. IBRO -- arXiv 2507.18391**
**CONFIRMED.** "Revisiting LLM Reasoning via Information Bottleneck" (July 24, 2025). It proposes IB-aware reasoning optimization (IBRO), a framework that encourages reasoning trajectories to be both informative about the correct answer and generalizable across diverse prompts, via a token-level surrogate objective that modulates entropy based on advantage -- higher entropy for critical tokens, penalizing uninformative ones -- integrable into existing RLVR pipelines with a single line of code.

**6. InfoPrune -- VLM token pruning via information budgeting**
**FOUND, but withdrawn.** "InfoPrune: Revisiting Visual Token Pruning from an Information-Theoretic Perspective" appeared as an ICLR 2026 submission on OpenReview but was **withdrawn** (last revision November 26, 2025). It recasts pruning as an information budgeting problem with a two-stage training-free framework: Stage 1 selects tokens via attention priors plus structure-aware incremental metrics; Stage 2 detects mid-layer semantic convergence for one-shot pruning. Claimed >96% performance retention with only 11.1% tokens on LLaVA-1.5/LLaVA-Next/Qwen-VL-2.5. **Cite with caution given withdrawn status.**

**7. Drop-Bottleneck -- arXiv 2103.12300**
**CONFIRMED.** "Drop-Bottleneck: Learning Discrete Compressed Representation for Noise-Robust Exploration" (published at ICLR 2021). It proposes an information bottleneck method that discretely drops irrelevant features by learning feature-wise drop probabilities, providing deterministic compressed representations that improve robustness to noise and adversarial examples in RL exploration tasks.

**8. PAC-Bayes domain adaptation -- Germain et al. 2016 ICML**
**CONFIRMED.** "A New PAC-Bayesian Perspective on Domain Adaptation" by Pascal Germain, Amaury Habrard, Francois Laviolette, and Emilie Morvant, published in ICML 2016 (pp. 859-868). It derives an upper bound on target risk where the source-target distribution divergence (expressed as a ratio) controls the trade-off between a source error measure and target voters' disagreement.

**9. IBAC-SNI -- NeurIPS 2019**
**CONFIRMED.** "Generalization in Reinforcement Learning with Selective Noise Injection and Information Bottleneck" by Igl, Ciosek, Li, Tschiatschek, Zhang, Devlin, and Hofmann (NeurIPS 2019, Microsoft Research). It proposes Information Bottleneck Actor Critic (IBAC) combined with Selective Noise Injection (SNI) to improve RL generalization, achieving state-of-the-art on CoinRun and other generalization benchmarks. Code available at github.com/microsoft/IBAC-SNI.

**10. Recent 2026 work combining token pruning with distribution shift/OOD generalization in robotics/VLA**
Three notable papers found:

- **RCP** (arXiv 2604.04972, April 2026): "Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models" -- directly addresses the problem that irreversible token removal causes hidden-state distribution shift; proposes a cross-attention pruner with cumulative masks and a delayed repair adapter (DRA) using FiLM-based modulation. **This is the most directly relevant paper to your review's intersection of token pruning and distribution shift.**

- **VLA-IAP** (arXiv 2603.22991, March 2026): "Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models" -- introduces geometric priors and dynamic scheduling for pruning in VLA models, achieving 97.8% success rate with 1.25x speedup on LIBERO.

- **GridS** (ICML 2026, see item 1 above) also explicitly targets generalizability in its title and framing, positioning token pruning as beneficial for generalization rather than harmful.

---

**Summary of key gaps/flags for your review:**
- InfoPrune (#6) was withdrawn from ICLR 2026 -- verify before citing.
- RCP (arXiv 2604.04972) is likely the most important paper you may have missed, as it is the only 2026 work explicitly framing token pruning through the lens of distribution shift mitigation.
- VLA-IAP (March 2026) is another very recent VLA-specific pruning paper worth checking.

Sources:
- [GridS - ICML 2026 Poster](https://icml.cc/virtual/2026/poster/65010)
- [OneWM-VLA - arXiv 2605.07931](https://arxiv.org/abs/2605.07931v1)
- [EfficientVLA - arXiv 2506.10100](https://arxiv.org/abs/2506.10100)
- [Compressor-VLA - arXiv 2511.18950](https://arxiv.org/abs/2511.18950)
- [IBRO - arXiv 2507.18391](https://arxiv.org/abs/2507.18391)
- [InfoPrune - OpenReview (withdrawn)](https://openreview.net/forum?id=JmdvXuMELg)
- [Drop-Bottleneck - arXiv 2103.12300](https://arxiv.org/abs/2103.12300)
- [PAC-Bayes Domain Adaptation - Germain 2016 ICML](http://proceedings.mlr.press/v48/germain16.pdf)
- [IBAC-SNI - NeurIPS 2019](https://proceedings.neurips.cc/paper/2019/hash/e2ccf95a7f2e1878fcafc8376649b6e8-Abstract.html)
- [RCP - arXiv 2604.04972](https://arxiv.org/abs/2604.04972)
- [VLA-IAP - arXiv 2603.22991](https://arxiv.org/abs/2603.22991)

agentId: ad1d9c4db7d00bc25 (use SendMessage with to: 'ad1d9c4db7d00bc25' to continue this agent)
&lt;usage>total_tokens: 25033
tool_uses: 14
duration_ms: 85632&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "437a5a7e-0f3f-4391-94c2-9c6df6cf5c00",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "3d1240d8-03b5-4f48-b9f7-3ac2436cc199",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm conducting a final sweep for an ML research review on token pruning in VLA (Vision-Language-Action) models and generalization theory. I need to search for the most recent work (2026) that I might have missed. Please search:\n\n1. Search: \"GridS ICML 2026 VLA token pruning\" — verify GridS was accepted at ICML 2026 and what it does\n2. Search: \"OneWM-VLA arXiv 2605.07931\" — verify this May 2026 paper exists and its claims about 1 token per frame\n3. Search: \"EfficientVLA arXiv 2506.10100\" — verify existence\n4. Search: \"Compressor-VLA arXiv 2511.18950\" — verify existence\n5. Search: \"IBRO information bottleneck LLM reasoning arXiv 2507.18391\" — verify existence\n6. Search: \"InfoPrune VLM token pruning information budgeting\" — find this paper if it exists\n7. Search: \"Drop-Bottleneck learning discrete compressed representation\" arXiv 2103.12300 — verify existence\n8. Search: \"PAC-Bayes domain adaptation Germain 2016 ICML\" — verify this foundational reference\n9. Search: \"IBAC-SNI information bottleneck reinforcement learning generalization NeurIPS 2019\" — verify existence\n10. Search for any very recent (2026) work combining \"token pruning\" with \"distribution shift\" or \"out-of-distribution generalization\" in robotics/VLA\n\nReport findings concisely — existence confirmation plus 1-sentence summary for each.",
    "agentId": "ad1d9c4db7d00bc25",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for all 10 searches:\n\n---\n\n**1. GridS -- ICML 2026 VLA token pruning**\n**CONFIRMED.** GridS (\"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\") was accepted as a poster at ICML 2026. It introduces a plug-and-play module that adaptively predicts a minimal set of salient coordinates and extracts features via differentiable interpolation, preserving essential spatial information while compressing to fewer than 10% of visual tokens -- addressing the trade-off where aggressive pruning discards critical geometric details like contact points.\n\n**2. OneWM-VLA -- arXiv 2605.07931**\n**CONFIRMED.** \"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy\" (submitted May 8, 2026). It compresses each camera view into a single semantic token per frame via Adaptive Attention Pooling, and jointly trains world prediction and action generation under a single flow-matching objective on a pi0 (2B) backbone with 14.71M LoRA parameters, improving average success from 47.9% to 61.3% on MetaWorld MT50 and reaching 95.6% on LIBERO-Long.\n\n**3. EfficientVLA -- arXiv 2506.10100**\n**CONFIRMED.** \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" (submitted June 11, 2025). It combines three strategies -- pruning redundant language-module layers, task-aware visual token selection, and diffusion action-head feature caching -- to yield 1.93x inference speedup and 28.9% FLOPs with only 0.6% success-rate drop on SIMPLER when applied to CogACT.\n\n**4. Compressor-VLA -- arXiv 2511.18950**\n**CONFIRMED.** \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" (November 2025). It uses a Semantic Task Compressor (STC) for holistic task-relevant context and a Spatial Refinement Compressor (SRC) for fine-grained spatial details, both dynamically modulated by natural language instructions, achieving 59% FLOPs reduction and >3x visual token compression on LIBERO with competitive success rates.\n\n**5. IBRO -- arXiv 2507.18391**\n**CONFIRMED.** \"Revisiting LLM Reasoning via Information Bottleneck\" (July 24, 2025). It proposes IB-aware reasoning optimization (IBRO), a framework that encourages reasoning trajectories to be both informative about the correct answer and generalizable across diverse prompts, via a token-level surrogate objective that modulates entropy based on advantage -- higher entropy for critical tokens, penalizing uninformative ones -- integrable into existing RLVR pipelines with a single line of code.\n\n**6. InfoPrune -- VLM token pruning via information budgeting**\n**FOUND, but withdrawn.** \"InfoPrune: Revisiting Visual Token Pruning from an Information-Theoretic Perspective\" appeared as an ICLR 2026 submission on OpenReview but was **withdrawn** (last revision November 26, 2025). It recasts pruning as an information budgeting problem with a two-stage training-free framework: Stage 1 selects tokens via attention priors plus structure-aware incremental metrics; Stage 2 detects mid-layer semantic convergence for one-shot pruning. Claimed >96% performance retention with only 11.1% tokens on LLaVA-1.5/LLaVA-Next/Qwen-VL-2.5. **Cite with caution given withdrawn status.**\n\n**7. Drop-Bottleneck -- arXiv 2103.12300**\n**CONFIRMED.** \"Drop-Bottleneck: Learning Discrete Compressed Representation for Noise-Robust Exploration\" (published at ICLR 2021). It proposes an information bottleneck method that discretely drops irrelevant features by learning feature-wise drop probabilities, providing deterministic compressed representations that improve robustness to noise and adversarial examples in RL exploration tasks.\n\n**8. PAC-Bayes domain adaptation -- Germain et al. 2016 ICML**\n**CONFIRMED.** \"A New PAC-Bayesian Perspective on Domain Adaptation\" by Pascal Germain, Amaury Habrard, Francois Laviolette, and Emilie Morvant, published in ICML 2016 (pp. 859-868). It derives an upper bound on target risk where the source-target distribution divergence (expressed as a ratio) controls the trade-off between a source error measure and target voters' disagreement.\n\n**9. IBAC-SNI -- NeurIPS 2019**\n**CONFIRMED.** \"Generalization in Reinforcement Learning with Selective Noise Injection and Information Bottleneck\" by Igl, Ciosek, Li, Tschiatschek, Zhang, Devlin, and Hofmann (NeurIPS 2019, Microsoft Research). It proposes Information Bottleneck Actor Critic (IBAC) combined with Selective Noise Injection (SNI) to improve RL generalization, achieving state-of-the-art on CoinRun and other generalization benchmarks. Code available at github.com/microsoft/IBAC-SNI.\n\n**10. Recent 2026 work combining token pruning with distribution shift/OOD generalization in robotics/VLA**\nThree notable papers found:\n\n- **RCP** (arXiv 2604.04972, April 2026): \"Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models\" -- directly addresses the problem that irreversible token removal causes hidden-state distribution shift; proposes a cross-attention pruner with cumulative masks and a delayed repair adapter (DRA) using FiLM-based modulation. **This is the most directly relevant paper to your review's intersection of token pruning and distribution shift.**\n\n- **VLA-IAP** (arXiv 2603.22991, March 2026): \"Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" -- introduces geometric priors and dynamic scheduling for pruning in VLA models, achieving 97.8% success rate with 1.25x speedup on LIBERO.\n\n- **GridS** (ICML 2026, see item 1 above) also explicitly targets generalizability in its title and framing, positioning token pruning as beneficial for generalization rather than harmful.\n\n---\n\n**Summary of key gaps/flags for your review:**\n- InfoPrune (#6) was withdrawn from ICLR 2026 -- verify before citing.\n- RCP (arXiv 2604.04972) is likely the most important paper you may have missed, as it is the only 2026 work explicitly framing token pruning through the lens of distribution shift mitigation.\n- VLA-IAP (March 2026) is another very recent VLA-specific pruning paper worth checking.\n\nSources:\n- [GridS - ICML 2026 Poster](https://icml.cc/virtual/2026/poster/65010)\n- [OneWM-VLA - arXiv 2605.07931](https://arxiv.org/abs/2605.07931v1)\n- [EfficientVLA - arXiv 2506.10100](https://arxiv.org/abs/2506.10100)\n- [Compressor-VLA - arXiv 2511.18950](https://arxiv.org/abs/2511.18950)\n- [IBRO - arXiv 2507.18391](https://arxiv.org/abs/2507.18391)\n- [InfoPrune - OpenReview (withdrawn)](https://openreview.net/forum?id=JmdvXuMELg)\n- [Drop-Bottleneck - arXiv 2103.12300](https://arxiv.org/abs/2103.12300)\n- [PAC-Bayes Domain Adaptation - Germain 2016 ICML](http://proceedings.mlr.press/v48/germain16.pdf)\n- [IBAC-SNI - NeurIPS 2019](https://proceedings.neurips.cc/paper/2019/hash/e2ccf95a7f2e1878fcafc8376649b6e8-Abstract.html)\n- [RCP - arXiv 2604.04972](https://arxiv.org/abs/2604.04972)\n- [VLA-IAP - arXiv 2603.22991](https://arxiv.org/abs/2603.22991)"
      }
    ],
    "totalDurationMs": 85632,
    "totalTokens": 25033,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 20075,
      "output_tokens": 2129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2129,
          "cache_read_input_tokens": 20075,
          "cache_creation_input_tokens": 2828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2828,
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
  "sourceToolAssistantUUID": "437a5a7e-0f3f-4391-94c2-9c6df6cf5c00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
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
  "leafUuid": "3d1240d8-03b5-4f48-b9f7-3ac2436cc199",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "VLA token pruning: discrete IB theory under domain shift",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Tool call

_source line 22 · 2026-05-13T05:29:14.388Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014GPei3ohmanRKTEuMnp488`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Deep-read critical competing papers",
  "prompt": "I need to deeply read two critical papers for my ML research review. Please use WebFetch to read these arxiv papers and extract key details:\n\n1. **RCP paper (arXiv 2604.04972)**: \"Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models\" — This is potentially a very close competitor to the proposal I'm reviewing. I need:\n   - What specific problem does it address?\n   - Does it provide any theoretical analysis or is it purely empirical?\n   - What is its approach to distribution shift from token pruning?\n   - What benchmarks does it use?\n   - How does it frame the relationship between token pruning and distribution shift?\n\n2. **\"How good is PAC-Bayes at explaining generalisation?\" (arXiv 2503.08231)** — This paper apparently undermines the idea that PAC-Bayes bounds are informative for model selection/understanding generalization. I need:\n   - What are the main claims?\n   - Does it specifically discuss ordinal predictions from vacuous bounds?\n   - How does it view the use of PAC-Bayes bounds for large models?\n\n3. Also fetch the abstract of **\"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\"** (arXiv 2502.11501) to understand the claim that random pruning outperforms sophisticated methods.\n\nFor each paper, try fetching from https://arxiv.org/abs/XXXX.XXXXX format. Report the key findings relevant to this review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d1240d8-03b5-4f48-b9f7-3ac2436cc199",
  "isSidechain": false,
  "requestId": "req_011Caz1vJLkgi2GsDiLBrt8Y",
  "type": "assistant",
  "uuid": "aeaf5c8e-9154-4a9e-97e5-84444e2fad97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132hDEtbbQiEXUNQXDbeUbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 43275,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 43275,
          "cache_creation_input_tokens": 2700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2700
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

_source line 23 · 2026-05-13T05:31:26.297Z_

<details><summary>↩ Tool result · `toolu_014GPei3ohmanRKTEuMnp488`</summary>

```text
Excellent -- I now have detailed information from all three papers. Here is my consolidated report.

---

## Paper 1: RCP -- "Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models" (arXiv 2604.04972)

**Authors:** Jianwei Zhang, Chaoning Zhang, Sihan Cao, Wang Liu, Pengcheng Zheng, Jiaxin Huang, Caiyan Qin, Yalan Ye, Wei Dong, Yang Yang

**Problem addressed:** Token pruning in LVLMs causes distribution shift in hidden states -- removing visual tokens makes the intermediate representations deviate from what the pre-trained model expects under the full-token regime. This drift accumulates through layers, becoming progressively worse in deeper layers.

**Theoretical vs. empirical:** The paper is **purely empirical** -- no formal bounds, proofs, or theoretical guarantees are provided. Distribution shift is measured post-hoc via the squared 2-Wasserstein distance (W2^2) between layer-wise hidden state distributions, but this is an empirical metric, not a theoretical contribution.

**Approach to distribution shift -- three components:**

1. **Cross-attention pruner:** Combines three scoring signals -- (a) a cross-attention score using learnable pruning queries conditioned on the question context, (b) a per-token MLP score, and (c) attention scores extracted from the frozen LLM's decoder self-attention. Final logit = A + Sa + St + bias. Uses Gumbel-Sigmoid with straight-through estimator during training. Crucially maintains cumulative masks across layers (m_tilde^(l) = m_tilde^(l-1) * m^(l)) so pruned tokens never reappear.

2. **Delayed Repair Adapter (DRA):** Caches information about pruned tokens via mask embeddings and pruned-feature embeddings, then applies FiLM-based modulation (feature-wise linear modulation: scale gamma and shift beta parameters) to answer-generation tokens only. Uses a bottleneck residual correction: Delta_h = alpha * Up(gamma * GELU(Down(x)) + beta).

3. **Repair loss:** Matches first-order (mean) and second-order (variance) statistics between pruned and full-token representations. The loss corresponds to the normalized squared 2-Wasserstein distance between diagonal-Gaussian approximations of the feature distributions. This is distribution-level matching, not token-wise matching.

**Benchmarks (7 total):** GQA, MMBench, MME, POPE, ScienceQA, VQAv2, VizWiz. Models tested: LLaVA-1.5-7B (primary), LLaVA-1.5-13B. Baselines: ToMe, FastV, PDrop, HiRED, VisionZip, DART.

**Key results on LLaVA-7B:**
- 192 tokens (66.7% reduction): 0.94% accuracy drop, 63.3% FLOPs reduction
- 128 tokens (77.8% reduction): 3.27% accuracy drop, 75.0% FLOPs reduction
- 64 tokens (88.9% reduction): 5.0% accuracy drop, 85.7% FLOPs reduction

**Training:** Only 40 minutes on 2x RTX 4090; 16.56M trainable parameters for 7B model; no backbone fine-tuning. Trained on 10,000 VQAv2 samples.

**Key framing:** The paper explicitly identifies that "irreversible removal of visual tokens causes distribution shift" and measures this via layer-by-layer W2^2 distance, showing drift is mild near pruning layers but accumulates in deeper layers.

**Notable gap:** Does not compare against random pruning baselines.

---

## Paper 2: "How good is PAC-Bayes at explaining generalisation?" (arXiv 2503.08231)

**Authors:** Antoine Picard-Weibel, Eugenio Clerico, Roman Moscoviz, Benjamin Guedj

**Main claims -- this is an entirely theoretical paper (no experiments):**

**Theorem 1:** For PAC-Bayes bounds of a certain class, the optimal posterior's bound depends *solely* on the push-forward of the prior through the empirical risk function (the "risk prior"): inf_{pi << pi_p} B(pi, pi_p, R) = B^min_{D,b}(pi_p # R). This means the bound is **insensitive to predictor space geometry** -- only the distribution of empirical risk values under the prior matters.

**Theorem 2:** The minimum bound is monotonically increasing under stochastic ordering of risk priors.

**Corollary 2:** Formalizes necessary conditions -- any prior achieving a target guarantee G must satisfy quantile requirements: pi_p#R([0,r)) >= Q_bar(r,G) for all r, meaning the prior must place sufficient probability mass on well-performing predictors.

**On data-dependent priors (critical finding):** The paper extensively critiques the prevalent practice in deep learning PAC-Bayes of using data-dependent priors. It shows that empirical PAC-Bayes bounds on MNIST/CIFAR closely match simple test bounds computed by just training on the prior dataset and testing on the posterior dataset. The authors call this "an unduly complex way to get test bounds" with "almost no learning at the posterior level."

**On vacuous bounds and ordinal ranking:** The paper does **not** directly discuss whether vacuous bounds can still provide useful ordinal/ranking information. Its focus is on absolute guarantee quality.

**On large models:** The paper addresses the "PAC-Bayes paradox" -- why KL divergence doesn't seem to scale with model dimensionality for data-dependent priors. The explanation: it is the risk distribution (not parameter space dimension) that drives the bound. For larger networks with lower test risk, priors naturally concentrate more mass on low-risk values, so shifting weight results in smaller decreases of average risk.

**Central criticism:** PAC-Bayes bounds don't illuminate *why* generalization occurs -- they merely formalize what the prior already knows. If achieving tight bounds requires priors that already generalize well, the framework provides no mechanistic insight into learning.

**Scope limitation:** Results require specific assumptions (bound must be non-decreasing in both arguments, D must be convex). Bernstein-based bounds and some newer bounds are excluded.

---

## Paper 3: "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?" (arXiv 2502.11501)

**Authors:** Zichen Wen, Yifeng Gao, Weijia Li, Conghui He, Linfeng Zhang

**Core finding -- random pruning outperforms sophisticated methods:** On LLaVA-1.5-7B with 75% token reduction, **random selection achieved 95.0% average performance vs. FastV's 89.8%**. At 88.9% reduction, random reached 89.1% vs. FastV's 78.2%. This pattern held across LLaVA-1.5-13B and Qwen2-VL-72B.

**Why sophisticated methods fail -- position bias:** Attention-based methods suffer from systematic position bias where tokens in later positions receive higher attention scores and are preferentially retained. This destroys spatial understanding. The paper's "Window FastV" variant (which corrects for position bias) reduced degradation by 3.4% at 75% reduction and 9% at 88.9%.

**Spatial task catastrophe:** On RefCOCO grounding tasks, vanilla FastV achieved only 18.8% and SparseVLM only 4.8% average performance, while random pruning achieved 23.2% -- spatially non-uniform methods catastrophically fail on spatial tasks.

**Language guidance is conditional:** Text-guided pruning helps only when the task strongly correlates with language information (e.g., Visual Haystack). For many tasks it provides no benefit or hurts.

**Evaluation protocol problems identified:**
- FLOPs don't predict actual latency (methods incompatible with Flash Attention retain O(N^2) memory costs)
- Training-aware compression is overlooked (Qwen2-VL's built-in 4x patch merging means FastV with training-aware adjustment maintains 99.8-100% baseline performance)
- Current benchmarks are biased toward certain task types

**Benchmarks used (9 total):** GQA, MMBench, MMBench-CN, MME, POPE, ScienceQA, TextVQA, VQA V2, Visual Haystack, RefCOCO/RefCOCO+/RefCOCOg.

**Recommendations:** Implement pruning in shallow layers with simple operations; ensure Flash Attention compatibility; focus on training-aware compression; use actual latency measurements; evaluate on OCR-heavy benchmarks.

**On distribution shift:** Not explicitly discussed, but the finding that task-dependent alpha parameters matter (perception tasks favor redundancy-first pruning at alpha=0.0-0.1, knowledge tasks favor importance-first at alpha=0.8-0.9) suggests task-specific distributional effects.

---

## Cross-Paper Implications for Your Review

1. **RCP as a competitor:** RCP directly addresses distribution shift from token pruning with an empirical repair mechanism (moment-matching via W2^2 distance), but provides zero theoretical grounding. If the proposal you're reviewing offers theoretical analysis of distribution shift, that would be a clear differentiator from RCP.

2. **The random pruning challenge (Paper 3):** Any token pruning paper must now contend with the finding that random pruning outperforms FastV and similar methods. RCP does not address this baseline. If the proposal you're reviewing doesn't compare against random pruning, this is a significant gap.

3. **PAC-Bayes skepticism (Paper 2):** If the proposal uses PAC-Bayes bounds to theoretically justify its approach, this paper raises serious concerns: the bounds' quality depends almost entirely on the prior placing mass on good predictors, which may amount to circular reasoning. However, this paper does not address whether vacuous bounds can still provide useful ordinal predictions -- that remains an open question the proposal could potentially exploit.

agentId: a337038734076c9d0 (use SendMessage with to: 'a337038734076c9d0' to continue this agent)
&lt;usage>total_tokens: 19977
tool_uses: 7
duration_ms: 131904&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeaf5c8e-9154-4a9e-97e5-84444e2fad97",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "e8b3a2ef-2416-4ff9-b517-eeb1edd577f8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply read two critical papers for my ML research review. Please use WebFetch to read these arxiv papers and extract key details:\n\n1. **RCP paper (arXiv 2604.04972)**: \"Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models\" — This is potentially a very close competitor to the proposal I'm reviewing. I need:\n   - What specific problem does it address?\n   - Does it provide any theoretical analysis or is it purely empirical?\n   - What is its approach to distribution shift from token pruning?\n   - What benchmarks does it use?\n   - How does it frame the relationship between token pruning and distribution shift?\n\n2. **\"How good is PAC-Bayes at explaining generalisation?\" (arXiv 2503.08231)** — This paper apparently undermines the idea that PAC-Bayes bounds are informative for model selection/understanding generalization. I need:\n   - What are the main claims?\n   - Does it specifically discuss ordinal predictions from vacuous bounds?\n   - How does it view the use of PAC-Bayes bounds for large models?\n\n3. Also fetch the abstract of **\"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\"** (arXiv 2502.11501) to understand the claim that random pruning outperforms sophisticated methods.\n\nFor each paper, try fetching from https://arxiv.org/abs/XXXX.XXXXX format. Report the key findings relevant to this review.",
    "agentId": "a337038734076c9d0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent -- I now have detailed information from all three papers. Here is my consolidated report.\n\n---\n\n## Paper 1: RCP -- \"Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models\" (arXiv 2604.04972)\n\n**Authors:** Jianwei Zhang, Chaoning Zhang, Sihan Cao, Wang Liu, Pengcheng Zheng, Jiaxin Huang, Caiyan Qin, Yalan Ye, Wei Dong, Yang Yang\n\n**Problem addressed:** Token pruning in LVLMs causes distribution shift in hidden states -- removing visual tokens makes the intermediate representations deviate from what the pre-trained model expects under the full-token regime. This drift accumulates through layers, becoming progressively worse in deeper layers.\n\n**Theoretical vs. empirical:** The paper is **purely empirical** -- no formal bounds, proofs, or theoretical guarantees are provided. Distribution shift is measured post-hoc via the squared 2-Wasserstein distance (W2^2) between layer-wise hidden state distributions, but this is an empirical metric, not a theoretical contribution.\n\n**Approach to distribution shift -- three components:**\n\n1. **Cross-attention pruner:** Combines three scoring signals -- (a) a cross-attention score using learnable pruning queries conditioned on the question context, (b) a per-token MLP score, and (c) attention scores extracted from the frozen LLM's decoder self-attention. Final logit = A + Sa + St + bias. Uses Gumbel-Sigmoid with straight-through estimator during training. Crucially maintains cumulative masks across layers (m_tilde^(l) = m_tilde^(l-1) * m^(l)) so pruned tokens never reappear.\n\n2. **Delayed Repair Adapter (DRA):** Caches information about pruned tokens via mask embeddings and pruned-feature embeddings, then applies FiLM-based modulation (feature-wise linear modulation: scale gamma and shift beta parameters) to answer-generation tokens only. Uses a bottleneck residual correction: Delta_h = alpha * Up(gamma * GELU(Down(x)) + beta).\n\n3. **Repair loss:** Matches first-order (mean) and second-order (variance) statistics between pruned and full-token representations. The loss corresponds to the normalized squared 2-Wasserstein distance between diagonal-Gaussian approximations of the feature distributions. This is distribution-level matching, not token-wise matching.\n\n**Benchmarks (7 total):** GQA, MMBench, MME, POPE, ScienceQA, VQAv2, VizWiz. Models tested: LLaVA-1.5-7B (primary), LLaVA-1.5-13B. Baselines: ToMe, FastV, PDrop, HiRED, VisionZip, DART.\n\n**Key results on LLaVA-7B:**\n- 192 tokens (66.7% reduction): 0.94% accuracy drop, 63.3% FLOPs reduction\n- 128 tokens (77.8% reduction): 3.27% accuracy drop, 75.0% FLOPs reduction\n- 64 tokens (88.9% reduction): 5.0% accuracy drop, 85.7% FLOPs reduction\n\n**Training:** Only 40 minutes on 2x RTX 4090; 16.56M trainable parameters for 7B model; no backbone fine-tuning. Trained on 10,000 VQAv2 samples.\n\n**Key framing:** The paper explicitly identifies that \"irreversible removal of visual tokens causes distribution shift\" and measures this via layer-by-layer W2^2 distance, showing drift is mild near pruning layers but accumulates in deeper layers.\n\n**Notable gap:** Does not compare against random pruning baselines.\n\n---\n\n## Paper 2: \"How good is PAC-Bayes at explaining generalisation?\" (arXiv 2503.08231)\n\n**Authors:** Antoine Picard-Weibel, Eugenio Clerico, Roman Moscoviz, Benjamin Guedj\n\n**Main claims -- this is an entirely theoretical paper (no experiments):**\n\n**Theorem 1:** For PAC-Bayes bounds of a certain class, the optimal posterior's bound depends *solely* on the push-forward of the prior through the empirical risk function (the \"risk prior\"): inf_{pi << pi_p} B(pi, pi_p, R) = B^min_{D,b}(pi_p # R). This means the bound is **insensitive to predictor space geometry** -- only the distribution of empirical risk values under the prior matters.\n\n**Theorem 2:** The minimum bound is monotonically increasing under stochastic ordering of risk priors.\n\n**Corollary 2:** Formalizes necessary conditions -- any prior achieving a target guarantee G must satisfy quantile requirements: pi_p#R([0,r)) >= Q_bar(r,G) for all r, meaning the prior must place sufficient probability mass on well-performing predictors.\n\n**On data-dependent priors (critical finding):** The paper extensively critiques the prevalent practice in deep learning PAC-Bayes of using data-dependent priors. It shows that empirical PAC-Bayes bounds on MNIST/CIFAR closely match simple test bounds computed by just training on the prior dataset and testing on the posterior dataset. The authors call this \"an unduly complex way to get test bounds\" with \"almost no learning at the posterior level.\"\n\n**On vacuous bounds and ordinal ranking:** The paper does **not** directly discuss whether vacuous bounds can still provide useful ordinal/ranking information. Its focus is on absolute guarantee quality.\n\n**On large models:** The paper addresses the \"PAC-Bayes paradox\" -- why KL divergence doesn't seem to scale with model dimensionality for data-dependent priors. The explanation: it is the risk distribution (not parameter space dimension) that drives the bound. For larger networks with lower test risk, priors naturally concentrate more mass on low-risk values, so shifting weight results in smaller decreases of average risk.\n\n**Central criticism:** PAC-Bayes bounds don't illuminate *why* generalization occurs -- they merely formalize what the prior already knows. If achieving tight bounds requires priors that already generalize well, the framework provides no mechanistic insight into learning.\n\n**Scope limitation:** Results require specific assumptions (bound must be non-decreasing in both arguments, D must be convex). Bernstein-based bounds and some newer bounds are excluded.\n\n---\n\n## Paper 3: \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\" (arXiv 2502.11501)\n\n**Authors:** Zichen Wen, Yifeng Gao, Weijia Li, Conghui He, Linfeng Zhang\n\n**Core finding -- random pruning outperforms sophisticated methods:** On LLaVA-1.5-7B with 75% token reduction, **random selection achieved 95.0% average performance vs. FastV's 89.8%**. At 88.9% reduction, random reached 89.1% vs. FastV's 78.2%. This pattern held across LLaVA-1.5-13B and Qwen2-VL-72B.\n\n**Why sophisticated methods fail -- position bias:** Attention-based methods suffer from systematic position bias where tokens in later positions receive higher attention scores and are preferentially retained. This destroys spatial understanding. The paper's \"Window FastV\" variant (which corrects for position bias) reduced degradation by 3.4% at 75% reduction and 9% at 88.9%.\n\n**Spatial task catastrophe:** On RefCOCO grounding tasks, vanilla FastV achieved only 18.8% and SparseVLM only 4.8% average performance, while random pruning achieved 23.2% -- spatially non-uniform methods catastrophically fail on spatial tasks.\n\n**Language guidance is conditional:** Text-guided pruning helps only when the task strongly correlates with language information (e.g., Visual Haystack). For many tasks it provides no benefit or hurts.\n\n**Evaluation protocol problems identified:**\n- FLOPs don't predict actual latency (methods incompatible with Flash Attention retain O(N^2) memory costs)\n- Training-aware compression is overlooked (Qwen2-VL's built-in 4x patch merging means FastV with training-aware adjustment maintains 99.8-100% baseline performance)\n- Current benchmarks are biased toward certain task types\n\n**Benchmarks used (9 total):** GQA, MMBench, MMBench-CN, MME, POPE, ScienceQA, TextVQA, VQA V2, Visual Haystack, RefCOCO/RefCOCO+/RefCOCOg.\n\n**Recommendations:** Implement pruning in shallow layers with simple operations; ensure Flash Attention compatibility; focus on training-aware compression; use actual latency measurements; evaluate on OCR-heavy benchmarks.\n\n**On distribution shift:** Not explicitly discussed, but the finding that task-dependent alpha parameters matter (perception tasks favor redundancy-first pruning at alpha=0.0-0.1, knowledge tasks favor importance-first at alpha=0.8-0.9) suggests task-specific distributional effects.\n\n---\n\n## Cross-Paper Implications for Your Review\n\n1. **RCP as a competitor:** RCP directly addresses distribution shift from token pruning with an empirical repair mechanism (moment-matching via W2^2 distance), but provides zero theoretical grounding. If the proposal you're reviewing offers theoretical analysis of distribution shift, that would be a clear differentiator from RCP.\n\n2. **The random pruning challenge (Paper 3):** Any token pruning paper must now contend with the finding that random pruning outperforms FastV and similar methods. RCP does not address this baseline. If the proposal you're reviewing doesn't compare against random pruning, this is a significant gap.\n\n3. **PAC-Bayes skepticism (Paper 2):** If the proposal uses PAC-Bayes bounds to theoretically justify its approach, this paper raises serious concerns: the bounds' quality depends almost entirely on the prior placing mass on good predictors, which may amount to circular reasoning. However, this paper does not address whether vacuous bounds can still provide useful ordinal predictions -- that remains an open question the proposal could potentially exploit."
      }
    ],
    "totalDurationMs": 131904,
    "totalTokens": 19977,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1179,
      "cache_creation_input_tokens": 3874,
      "cache_read_input_tokens": 12480,
      "output_tokens": 2444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1179,
          "output_tokens": 2444,
          "cache_read_input_tokens": 12480,
          "cache_creation_input_tokens": 3874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3874,
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
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "aeaf5c8e-9154-4a9e-97e5-84444e2fad97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T05:32:33.437Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information from all my research agents. Let me synthesize everything and produce my review.

Key findings from my research:

1. **Reference verification**: All major references check out. LightVLA improvement is +2.6% not +2.9% (still flagged). The paper citing "Kuang et al." should be "Lotfi et al." for arXiv 2407.18158.

2. **Missing related work**:
   - **RCP (arXiv 2604.04972, April 2026)**: Very important — directly addresses distribution shift from token pruning, but purely empirical. Uses W2^2 distance to measure drift. 

The proposal needs to cite this work and clarify how it differs from RCP's empirical approach. I'm also noting several other critical papers: SQAP-VLA combines quantization with pruning, while a recent ACL 2025 finding shows random pruning surprisingly outperforms sophisticated methods—a major challenge to the proposal's core premise. IBTM applies information-bottleneck principles to token merging in vision transformers, and there's another IB-related work that appears to be cut off in the list.

Beyond the literature, I'm identifying some serious methodological concerns. The proposal plans to apply SubLoRA bounds to LoRA fine-tuning, but SubLoRA was originally designed for pretraining from scratch—there's no published validation that this approach works for LoRA parameters. Additionally, a 2025 paper argues that PAC-Bayes bounds, while mathematically sound, don't actually explain generalization in a meaningful way, which undermines the theoretical justification for using them here.

There are also practical issues: the fallback to ordinal predictions from vacuous bounds lacks rigorous support, and recent work shows random pruning outperforms more sophisticated methods, suggesting the proposal's core assumption—that task-conditioned pruning is fundamentally different from random pruning—may not hold. If random pruning works just as well, the information-bottleneck explanation becomes less compelling, and the real mechanism might just be "fewer tokens reduce overfitting" rather than intelligent removal of domain-variant information.

The proposal does cite the token pruning paper correctly as a preprint, which is fine. Looking at what's improved: the BC-IB distinction is now clear, the stochastic binary mask formalization addresses the discrete IB issue, the circularity concern is handled through falsifiable predictions, and the bound vacuity is acknowledged honestly. But some gaps remain—LightVLA's +2.9% improvement still isn't fully explained, and a few missing citations from earlier rounds haven't made it into the key references yet.

Now I'm evaluating the remaining issues: RCP from April 2026 directly addresses distribution shift from pruning and should be included, the random pruning results from ACL 2025 Findings challenge the core premise, SubLoRA for LoRA fine-tuning lacks validation, and PAC-Bayes bounds are questioned by recent work. The fundamental problem is that the user asked for theoretical analysis of why pruning improves generalization, but what's being delivered might be vacuous bounds with post-hoc correlations rather than genuine explanatory power.

Thinking through the novelty angle: the proposal does fill a real gap—no existing work combines IB-based generalization theory with discrete token selection in VLAs under distribution shift. BC-IB handles continuous compression, RCP addresses empirical distribution shift mitigation without theory, and IBTM was something else entirely.

The stochastic mask formalization is genuinely novel, but the theoretical contribution gets weakened by bound vacuity, reliance on ordinal predictions without theoretical grounding, and the broader skepticism around PAC-Bayes approaches. I'm settling on 3/5 for novelty—the formalization is solid but the theoretical impact is limited.

For feasibility, there are real concerns: SubLoRA hasn't been tested with LoRA fine-tuning, MI estimation at VLA scale is genuinely hard, and the 4-5 month timeline is tight for both theory and experiments. Even with LoRA's reduced parameters, the bounds could still be vacuous given small fine-tuning datasets. That's also 3/5.

The proposal itself is well-written and comprehensive—detailed structure, extensive landscape coverage, clear differentiation from BC-IB, and articulate methodology.

The mathematical formulations are specific and rigorous, so I'd rate clarity at 4/5. Impact hinges on whether the theory actually delivers non-vacuous bounds and meaningful ordinal predictions with a validated phase transition. If it works, this bridges theory and practice in VLA pruning significantly. But the user's core question about WHY pruning improves generalization might not get a satisfying answer if the bounds turn out vacuous, and the random pruning finding complicates the narrative. That's 3/5 for impact.

Averaging these scores gives 3.25, which falls short of the 4.0 threshold. Still, this is round 4 of 10, so there's opportunity to strengthen it.

The verdict is clear: don't pass, but do revise—the core idea has genuine merit and the gap is fixable. Though I'm noticing a deeper structural problem. The user fundamentally wants theoretical analysis of why token pruning enhances generalization, but the proposal's main theoretical lever—PAC-Bayes bounds—will almost certainly be vacuous. The ordinal predictions fallback lacks rigorous grounding, and recent work suggests PAC-Bayes certifies without explaining generalization. That's a real tension. Still, the proposal does offer other theoretical angles: the stochastic mask information bottleneck formalization and a few other contributions that might partially address the "why" question.

Looking at what's actually been accomplished across three rounds, the proposal has become quite comprehensive—it covers 15+ VLA pruning methods, engages deeply with information bottleneck theory, honestly acknowledges where bounds will fail, and positions itself thoughtfully relative to existing work. But there are still concrete gaps: RCP is directly relevant and missing, recent findings on random pruning effectiveness challenge the core premise, SubLoRA for LoRA fine-tuning hasn't been validated, and there's fundamental skepticism about whether PAC-Bayes can actually explain generalization at all.

Now I'm reconsidering the novelty score more carefully. The core contribution—applying information bottleneck theory to discrete token selection in VLAs under distribution shift—genuinely hasn't been done before. But BC-IB already combined IB with generalization bounds for robot manipulation, IBTM attempted IB plus token merging in vision transformers, IB-FT applied IB to language model fine-tuning, and RCP tackled distribution shift empirically. The theoretical novelty around the stochastic mask is real, but it's narrower than initially framed.

For feasibility, SubLoRA as a LoRA fine-tuning approach is unproven and introduces real risk, mutual information estimation at VLA scale is genuinely hard, and the timeline of 4-5 months is tight for deriving theory, verifying proofs, and running full VLA experiments. The pipeline combining LMI estimation, MINE, and SubLoRA adds complexity, though the experimental foundation with OpenVLA and LIBERO is solid.

The proposal itself is well-articulated and mathematically rigorous with clear differentiation from related work. The theoretical contribution is interesting but the bound vacuity problem undermines how satisfying the answer really is—though the phase transition around k* could be more practically valuable. The random pruning baseline finding muddies the narrative though, bringing the overall assessment to 3.25 and suggesting revision is needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b3a2ef-2416-4ff9-b517-eeb1edd577f8",
  "isSidechain": false,
  "requestId": "req_011Caz26vqVQtwJs8eMfLHik",
  "type": "assistant",
  "uuid": "c0a9518c-3f8f-40f3-ab59-13272930f9b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyE4FoSKn5MNamt3Gzuzk8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2970,
      "cache_read_input_tokens": 45975,
      "output_tokens": 2551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2551,
          "cache_read_input_tokens": 45975,
          "cache_creation_input_tokens": 2970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2970
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

_source line 25 · 2026-05-13T05:32:33.442Z_

Now let me compile my final assessment based on all the research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a9518c-3f8f-40f3-ab59-13272930f9b2",
  "isSidechain": false,
  "requestId": "req_011Caz26vqVQtwJs8eMfLHik",
  "type": "assistant",
  "uuid": "4161ecf8-a879-40d5-8ace-b022c0bbf561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyE4FoSKn5MNamt3Gzuzk8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2970,
      "cache_read_input_tokens": 45975,
      "output_tokens": 2551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2551,
          "cache_read_input_tokens": 45975,
          "cache_creation_input_tokens": 2970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2970
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

_source line 26 · 2026-05-13T05:32:33.444Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B4TPj4RpvtFCNNsKiurBhY`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4161ecf8-a879-40d5-8ace-b022c0bbf561",
  "isSidechain": false,
  "requestId": "req_011Caz26vqVQtwJs8eMfLHik",
  "type": "assistant",
  "uuid": "7bb821b9-da0e-4738-82f5-50e82df585f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyE4FoSKn5MNamt3Gzuzk8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2970,
      "cache_read_input_tokens": 45975,
      "output_tokens": 2551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2551,
          "cache_read_input_tokens": 45975,
          "cache_creation_input_tokens": 2970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2970
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

_source line 27 · 2026-05-13T05:32:33.452Z_

<details><summary>↩ Tool result · `toolu_01B4TPj4RpvtFCNNsKiurBhY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bb821b9-da0e-4738-82f5-50e82df585f6",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "2ccc49aa-1c00-4fee-9117-860bda6ce43f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "7bb821b9-da0e-4738-82f5-50e82df585f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
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
  "leafUuid": "2ccc49aa-1c00-4fee-9117-860bda6ce43f",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "VLA token pruning: discrete IB theory under domain shift",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Assistant

_source line 30 · 2026-05-13T05:32:36.840Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a few final targeted searches to verify the most critical remaining issues before writing my verdict.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ccc49aa-1c00-4fee-9117-860bda6ce43f",
  "isSidechain": false,
  "requestId": "req_011Caz2BtBPTQnaY69nmb6qx",
  "type": "assistant",
  "uuid": "5ad923d3-72ab-4b66-9698-ec5072472518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147gzNpeipKUqmTsQh6Z5y8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 48945,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 48945,
          "cache_creation_input_tokens": 3075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3075
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

_source line 31 · 2026-05-13T05:32:37.339Z_

Let me do a few final targeted searches to verify critical issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ad923d3-72ab-4b66-9698-ec5072472518",
  "isSidechain": false,
  "requestId": "req_011Caz2BtBPTQnaY69nmb6qx",
  "type": "assistant",
  "uuid": "e140c528-bb17-4188-a171-f390a573db6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147gzNpeipKUqmTsQh6Z5y8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 48945,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 48945,
          "cache_creation_input_tokens": 3075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3075
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

_source line 32 · 2026-05-13T05:32:38.976Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MCE7LGNt1KUL8UJSWKS32f`</summary>

```json
{
  "query": "RCP \"Representation Consistency Pruner\" distribution shift token pruning arXiv 2604.04972 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e140c528-bb17-4188-a171-f390a573db6a",
  "isSidechain": false,
  "requestId": "req_011Caz2BtBPTQnaY69nmb6qx",
  "type": "assistant",
  "uuid": "47e83233-b2c0-4008-99fe-cf9b7999fe44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147gzNpeipKUqmTsQh6Z5y8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 48945,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 48945,
          "cache_creation_input_tokens": 3075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3075
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

_source line 33 · 2026-05-13T05:32:39.826Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTBBhQNHrP4QEK729zDQit`</summary>

```json
{
  "query": "\"token pruning\" \"random pruning\" outperforms multimodal LLM ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47e83233-b2c0-4008-99fe-cf9b7999fe44",
  "isSidechain": false,
  "requestId": "req_011Caz2BtBPTQnaY69nmb6qx",
  "type": "assistant",
  "uuid": "7942dc88-c119-42a3-aae2-d584dd1924dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147gzNpeipKUqmTsQh6Z5y8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 48945,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 48945,
          "cache_creation_input_tokens": 3075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3075
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

_source line 34 · 2026-05-13T05:32:40.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qo4mKSHdtoMvJLXQv8heN`</summary>

```json
{
  "query": "SubLoRA PAC-Bayes bounds LoRA fine-tuning generalization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7942dc88-c119-42a3-aae2-d584dd1924dc",
  "isSidechain": false,
  "requestId": "req_011Caz2BtBPTQnaY69nmb6qx",
  "type": "assistant",
  "uuid": "c1f5c75b-7de4-4f31-a53a-6938a2abdf9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147gzNpeipKUqmTsQh6Z5y8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 48945,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 48945,
          "cache_creation_input_tokens": 3075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3075
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

_source line 35 · 2026-05-13T05:32:44.597Z_

<details><summary>↩ Tool result · `toolu_01MCE7LGNt1KUL8UJSWKS32f`</summary>

```text
Web search results for query: "RCP "Representation Consistency Pruner" distribution shift token pruning arXiv 2604.04972 2026"

Links: [{"title":"RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models","url":"https://arxiv.org/html/2604.04972"},{"title":"[2604.04972] RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models","url":"https://arxiv.org/abs/2604.04972"},{"title":"Paper page - Demystifying When Pruning Works via Representation Hierarchies","url":"https://huggingface.co/papers/2603.24652"},{"title":"The Role of Token Pruning in Efficient Transformer Architectures","url":"https://d197for5662m48.cloudfront.net/documents/publicationstatus/248154/preprint_pdf/ea24ae7811cc12006c32c0153c159c82.pdf"},{"title":"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents","url":"https://arxiv.org/html/2604.04979"},{"title":"fast and training-free visual token pruning for multi-modal large ...","url":"https://dl.acm.org/doi/abs/10.1609/aaai.v39i21.34366"},{"title":"QAPruner: Quantization-Aware Vision Token Pruning for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.02816"},{"title":"[2602.20205] OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport","url":"https://arxiv.org/abs/2602.20205"},{"title":"Common-token Optimized Model Pruning Across Channels ...","url":"https://arxiv.org/pdf/2509.06836"},{"title":"[2604.16235] Optimizing Korean-Centric LLMs via Token Pruning","url":"https://arxiv.org/abs/2604.16235"}]

I found the paper you were looking for! Here's what I found about RCP (Representation Consistency Pruner):

RCP is a novel framework that integrates cumulative visual token pruning with a delayed repair mechanism designed to address distribution shift in large vision-language models. The paper, with arXiv ID 2604.04972, is titled "RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models".

Key aspects of the approach include:

- The method employs a repair loss to match the first and second-order statistics of the pruned representations with a full-token teacher
- RCP is highly efficient because it trains only lightweight plug-in modules while allowing for physical token discarding at inference

The paper reports impressive results: RCP removes up to 88.9% of visual tokens and reduces FLOPs by up to 85.7% with only a marginal average accuracy drop, and outperforms prior methods that avoid fine-tuning the original model on several widely used benchmarks.

The paper was posted to arXiv on April 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47e83233-b2c0-4008-99fe-cf9b7999fe44",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "e0d13f4b-0d69-4702-a5a8-6f96496dd888",
  "toolUseResult": {
    "query": "RCP \"Representation Consistency Pruner\" distribution shift token pruning arXiv 2604.04972 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JJijzoNmnVQTyDzZz8bqJP",
        "content": [
          {
            "title": "RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models",
            "url": "https://arxiv.org/html/2604.04972"
          },
          {
            "title": "[2604.04972] RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2604.04972"
          },
          {
            "title": "Paper page - Demystifying When Pruning Works via Representation Hierarchies",
            "url": "https://huggingface.co/papers/2603.24652"
          },
          {
            "title": "The Role of Token Pruning in Efficient Transformer Architectures",
            "url": "https://d197for5662m48.cloudfront.net/documents/publicationstatus/248154/preprint_pdf/ea24ae7811cc12006c32c0153c159c82.pdf"
          },
          {
            "title": "Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents",
            "url": "https://arxiv.org/html/2604.04979"
          },
          {
            "title": "fast and training-free visual token pruning for multi-modal large ...",
            "url": "https://dl.acm.org/doi/abs/10.1609/aaai.v39i21.34366"
          },
          {
            "title": "QAPruner: Quantization-Aware Vision Token Pruning for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2604.02816"
          },
          {
            "title": "[2602.20205] OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport",
            "url": "https://arxiv.org/abs/2602.20205"
          },
          {
            "title": "Common-token Optimized Model Pruning Across Channels ...",
            "url": "https://arxiv.org/pdf/2509.06836"
          },
          {
            "title": "[2604.16235] Optimizing Korean-Centric LLMs via Token Pruning",
            "url": "https://arxiv.org/abs/2604.16235"
          }
        ]
      },
      "I found the paper you were looking for! Here's what I found about RCP (Representation Consistency Pruner):\n\nRCP is a novel framework that integrates cumulative visual token pruning with a delayed repair mechanism designed to address distribution shift in large vision-language models. The paper, with arXiv ID 2604.04972, is titled \"RCP: Representation Consistency Pruner for Mitigating Distribution Shift in Large Vision-Language Models\".\n\nKey aspects of the approach include:\n\n- The method employs a repair loss to match the first and second-order statistics of the pruned representations with a full-token teacher\n- RCP is highly efficient because it trains only lightweight plug-in modules while allowing for physical token discarding at inference\n\nThe paper reports impressive results: RCP removes up to 88.9% of visual tokens and reduces FLOPs by up to 85.7% with only a marginal average accuracy drop, and outperforms prior methods that avoid fine-tuning the original model on several widely used benchmarks.\n\nThe paper was posted to arXiv on April 4, 2026."
    ],
    "durationSeconds": 5.61777556999994
  },
  "sourceToolAssistantUUID": "47e83233-b2c0-4008-99fe-cf9b7999fe44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T05:32:45.294Z_

<details><summary>↩ Tool result · `toolu_01GTBBhQNHrP4QEK729zDQit`</summary>

```text
Web search results for query: ""token pruning" "random pruning" outperforms multimodal LLM ACL 2025"

Links: [{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"},{"title":"[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://arxiv.org/abs/2502.11501"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.802/"},{"title":"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://arxiv.org/html/2502.11501v1"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://arxiv.org/pdf/2502.11501"},{"title":"GitHub - Visual-AI/PruneVid: [ACL 2025] PruneVid: Visual Token Pruning for Efficient Video Large Language Models · GitHub","url":"https://github.com/visual-ai/prunevid"},{"title":"TAMP: Token-Adaptive Layerwise Pruning in Multimodal ...","url":"https://aclanthology.org/2025.findings-acl.359.pdf"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models","url":"https://arxiv.org/html/2503.02175v1"}]

Based on the search results, I found a highly relevant ACL 2025 paper that directly addresses your query:

## Key Finding

A recent ACL 2025 paper asks a critical question: "Why do many existing approaches underperform even compared to naive random token selection?" This finding is from a paper titled "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?" which was published in the Findings of the Association for Computational Linguistics at ACL 2025.

## Research Context

While token pruning methods have been proposed to reduce computation and KV storage costs in multimodal large language models, many existing approaches underperform when compared to naive random token selection. 

The paper goes on to examine fundamental questions about token pruning design, including whether attention-based scoring is sufficient for identifying redundant tokens, whether language information is helpful during token pruning, what makes a good trade-off between token importance and duplication, and whether current evaluation protocols are comprehensive and unbiased.

This research reveals surprising results about the effectiveness of random token pruning compared to more complex, attention-based pruning strategies in multimodal LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7942dc88-c119-42a3-aae2-d584dd1924dc",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "52e356c6-cd5e-45ea-a871-88a08f8ae6d7",
  "toolUseResult": {
    "query": "\"token pruning\" \"random pruning\" outperforms multimodal LLM ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012zxLVmNdDdDd59dRaBstUb",
        "content": [
          {
            "title": "Token Pruning in Multimodal Large Language Models",
            "url": "https://aclanthology.org/2025.findings-acl.802.pdf"
          },
          {
            "title": "[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?",
            "url": "https://arxiv.org/abs/2502.11501"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.802/"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?",
            "url": "https://arxiv.org/html/2502.11501v1"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models",
            "url": "https://arxiv.org/pdf/2502.11501"
          },
          {
            "title": "GitHub - Visual-AI/PruneVid: [ACL 2025] PruneVid: Visual Token Pruning for Efficient Video Large Language Models · GitHub",
            "url": "https://github.com/visual-ai/prunevid"
          },
          {
            "title": "TAMP: Token-Adaptive Layerwise Pruning in Multimodal ...",
            "url": "https://aclanthology.org/2025.findings-acl.359.pdf"
          },
          {
            "title": "Token Pruning",
            "url": "https://www.aussieai.com/research/token-pruning"
          },
          {
            "title": "DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models",
            "url": "https://arxiv.org/html/2503.02175v1"
          }
        ]
      },
      "Based on the search results, I found a highly relevant ACL 2025 paper that directly addresses your query:\n\n## Key Finding\n\nA recent ACL 2025 paper asks a critical question: \"Why do many existing approaches underperform even compared to naive random token selection?\" This finding is from a paper titled \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?\" which was published in the Findings of the Association for Computational Linguistics at ACL 2025.\n\n## Research Context\n\nWhile token pruning methods have been proposed to reduce computation and KV storage costs in multimodal large language models, many existing approaches underperform when compared to naive random token selection. \n\nThe paper goes on to examine fundamental questions about token pruning design, including whether attention-based scoring is sufficient for identifying redundant tokens, whether language information is helpful during token pruning, what makes a good trade-off between token importance and duplication, and whether current evaluation protocols are comprehensive and unbiased.\n\nThis research reveals surprising results about the effectiveness of random token pruning compared to more complex, attention-based pruning strategies in multimodal LLMs."
    ],
    "durationSeconds": 5.466181550999987
  },
  "sourceToolAssistantUUID": "7942dc88-c119-42a3-aae2-d584dd1924dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T05:32:47.405Z_

<details><summary>↩ Tool result · `toolu_012qo4mKSHdtoMvJLXQv8heN`</summary>

```text
Web search results for query: "SubLoRA PAC-Bayes bounds LoRA fine-tuning generalization 2025 2026"

Links: [{"title":"Non-Vacuous Generalization Bounds for Large Language Models Sanae Lotfi∗","url":"https://sslneurips23.github.io/paper_pdfs/paper_40.pdf"},{"title":"Non-Vacuous Generalization Bounds for Large Language Models","url":"https://arxiv.org/html/2312.17173v1"},{"title":"Non-Vacuous Generalization Bounds","url":"https://www.emergentmind.com/topics/non-vacuous-generalization-bounds"},{"title":"Flat-LoRA: Low-Rank Adaptation over a Flat Loss Landscape | OpenReview","url":"https://openreview.net/forum?id=3Qj3xSwN2I"},{"title":"Low-Rank Adaptations (LoRA)","url":"https://www.emergentmind.com/topics/low-rank-adaptations-lora"},{"title":"GitHub - ZJU-LLMs/Awesome-LoRAs · GitHub","url":"https://github.com/ZJU-LLMs/Awesome-LoRAs"},{"title":"A PAC-Bayesian approach to generalization for quantum models","url":"https://arxiv.org/html/2603.22964v1"},{"title":"SC-LoRA: Balancing Efficient Fine-tuning and Knowledge Preservation via Subspace-Constrained LoRA","url":"https://arxiv.org/html/2505.23724v3"},{"title":"ICML Poster Generalization Bounds via Meta-Learned Model Representations: PAC-Bayes and Sample Compression Hypernetworks","url":"https://icml.cc/virtual/2025/poster/45323"},{"title":"A study of large language model Q&A based on LoRA Fine-Tuning and prompt engineering | Proceedings of the 2025 5th International Conference on Applied Mathematics, Modelling and Intelligent Computing","url":"https://dl.acm.org/doi/10.1145/3745533.3745585"}]

Based on the web search results, I found relevant information about SubLoRA, PAC-Bayes bounds, and LoRA fine-tuning generalization:

## Key Findings

### SubLoRA Development
SubLoRA (Subspace-Enhanced Low-Rank Adaptation) is a novel non-linear parameterization for LLMs that makes it possible to smoothly vary the level of compression while maintaining expressivity. SubLoRA combines low-rank adaptation (LoRA) with subspace training, and experiments show that it is efficient when training from scratch, especially when combined with the linear subspace.

### PAC-Bayes Bounds and Generalization
For language models, the challenge involves autoregressive token prediction with non-independent token-level predictions, an unbounded bits per dimension metric for which previously used non-vacuous PAC-Bayes bounds are invalid, and orders of magnitude more parameters than image classification models. To address these challenges, researchers derived new generalization bounds applicable to the unbounded bits per dimension objective.

### Non-Vacuous Bounds Achievement
SubLoRA achieved the first non-vacuous bounds for large language models. SubLoRA achieves a strict improvement over LoRA and subspace training, often being the deciding factor whether the bounds are vacuous or non-vacuous.

### Recent Applications
SubLoRA combines low-rank adaptation and subspace projection and is employed to enhance compressibility and minimize the KL/description length term in PAC-Bayes bounds.

The search results are primarily from 2023-2024 academic publications, with the original SubLoRA work appearing in the NeurIPS 2023 Self-Supervised Learning workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1f5c75b-7de4-4f31-a53a-6938a2abdf9d",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "6f7bc0f0-e7e1-4d20-a8e6-e0091738b6df",
  "toolUseResult": {
    "query": "SubLoRA PAC-Bayes bounds LoRA fine-tuning generalization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nbhwe5MjEJPHJ3agkdrWW9",
        "content": [
          {
            "title": "Non-Vacuous Generalization Bounds for Large Language Models Sanae Lotfi∗",
            "url": "https://sslneurips23.github.io/paper_pdfs/paper_40.pdf"
          },
          {
            "title": "Non-Vacuous Generalization Bounds for Large Language Models",
            "url": "https://arxiv.org/html/2312.17173v1"
          },
          {
            "title": "Non-Vacuous Generalization Bounds",
            "url": "https://www.emergentmind.com/topics/non-vacuous-generalization-bounds"
          },
          {
            "title": "Flat-LoRA: Low-Rank Adaptation over a Flat Loss Landscape | OpenReview",
            "url": "https://openreview.net/forum?id=3Qj3xSwN2I"
          },
          {
            "title": "Low-Rank Adaptations (LoRA)",
            "url": "https://www.emergentmind.com/topics/low-rank-adaptations-lora"
          },
          {
            "title": "GitHub - ZJU-LLMs/Awesome-LoRAs · GitHub",
            "url": "https://github.com/ZJU-LLMs/Awesome-LoRAs"
          },
          {
            "title": "A PAC-Bayesian approach to generalization for quantum models",
            "url": "https://arxiv.org/html/2603.22964v1"
          },
          {
            "title": "SC-LoRA: Balancing Efficient Fine-tuning and Knowledge Preservation via Subspace-Constrained LoRA",
            "url": "https://arxiv.org/html/2505.23724v3"
          },
          {
            "title": "ICML Poster Generalization Bounds via Meta-Learned Model Representations: PAC-Bayes and Sample Compression Hypernetworks",
            "url": "https://icml.cc/virtual/2025/poster/45323"
          },
          {
            "title": "A study of large language model Q&A based on LoRA Fine-Tuning and prompt engineering | Proceedings of the 2025 5th International Conference on Applied Mathematics, Modelling and Intelligent Computing",
            "url": "https://dl.acm.org/doi/10.1145/3745533.3745585"
          }
        ]
      },
      "Based on the web search results, I found relevant information about SubLoRA, PAC-Bayes bounds, and LoRA fine-tuning generalization:\n\n## Key Findings\n\n### SubLoRA Development\nSubLoRA (Subspace-Enhanced Low-Rank Adaptation) is a novel non-linear parameterization for LLMs that makes it possible to smoothly vary the level of compression while maintaining expressivity. SubLoRA combines low-rank adaptation (LoRA) with subspace training, and experiments show that it is efficient when training from scratch, especially when combined with the linear subspace.\n\n### PAC-Bayes Bounds and Generalization\nFor language models, the challenge involves autoregressive token prediction with non-independent token-level predictions, an unbounded bits per dimension metric for which previously used non-vacuous PAC-Bayes bounds are invalid, and orders of magnitude more parameters than image classification models. To address these challenges, researchers derived new generalization bounds applicable to the unbounded bits per dimension objective.\n\n### Non-Vacuous Bounds Achievement\nSubLoRA achieved the first non-vacuous bounds for large language models. SubLoRA achieves a strict improvement over LoRA and subspace training, often being the deciding factor whether the bounds are vacuous or non-vacuous.\n\n### Recent Applications\nSubLoRA combines low-rank adaptation and subspace projection and is employed to enhance compressibility and minimize the KL/description length term in PAC-Bayes bounds.\n\nThe search results are primarily from 2023-2024 academic publications, with the original SubLoRA work appearing in the NeurIPS 2023 Self-Supervised Learning workshop."
    ],
    "durationSeconds": 7.0527130200000245
  },
  "sourceToolAssistantUUID": "c1f5c75b-7de4-4f31-a53a-6938a2abdf9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-13T05:32:47.408Z_

```json
{
  "parentUuid": "6f7bc0f0-e7e1-4d20-a8e6-e0091738b6df",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "60fc89ea-5093-4ab7-b75d-38550539377c",
  "timestamp": "2026-05-13T05:32:47.408Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-13T05:32:51.063Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also search for OTPrune which appeared in the RCP search results - it seems directly relevant as a distribution-aligned pruning method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60fc89ea-5093-4ab7-b75d-38550539377c",
  "isSidechain": false,
  "requestId": "req_011Caz2Cua1cvGmVnGnhHNeb",
  "type": "assistant",
  "uuid": "cdb2aaf9-a39c-44b9-94f1-c9c34a553f75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb1azsyS6coKZhdc4hz2vC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 52020,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 52020,
          "cache_creation_input_tokens": 2915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2915
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

_source line 40 · 2026-05-13T05:32:51.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbvqsGCeEFLG4UmMV15QeW`</summary>

```json
{
  "query": "OTPrune \"Distribution-Aligned Visual Token Pruning\" optimal transport arXiv 2602.20205"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdb2aaf9-a39c-44b9-94f1-c9c34a553f75",
  "isSidechain": false,
  "requestId": "req_011Caz2Cua1cvGmVnGnhHNeb",
  "type": "assistant",
  "uuid": "a1698594-f0c0-4aa8-87a6-5283536dd9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb1azsyS6coKZhdc4hz2vC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 52020,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 52020,
          "cache_creation_input_tokens": 2915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2915
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

_source line 41 · 2026-05-13T05:32:52.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PZGSuTw43Y3BenyaCmhKk1`</summary>

```json
{
  "query": "\"PAC-Bayes\" \"explains generalisation\" \"prior engineering\" 2025 arXiv 2503.08231"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1698594-f0c0-4aa8-87a6-5283536dd9cd",
  "isSidechain": false,
  "requestId": "req_011Caz2Cua1cvGmVnGnhHNeb",
  "type": "assistant",
  "uuid": "d3415d94-f843-4a5f-9a64-a5f51167b5e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb1azsyS6coKZhdc4hz2vC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 52020,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 52020,
          "cache_creation_input_tokens": 2915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2915
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

_source line 42 · 2026-05-13T05:32:58.253Z_

<details><summary>↩ Tool result · `toolu_01MbvqsGCeEFLG4UmMV15QeW`</summary>

```text
Web search results for query: "OTPrune "Distribution-Aligned Visual Token Pruning" optimal transport arXiv 2602.20205"

Links: [{"title":"[2602.20205] OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport","url":"https://arxiv.org/abs/2602.20205"},{"title":"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport","url":"https://arxiv.org/html/2602.20205"},{"title":"GitHub - xiwenc1/OTPrune: Official code for the paper: OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport · GitHub","url":"https://github.com/xiwenc1/OTPrune"},{"title":"Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/html/2604.12035"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model","url":"https://arxiv.org/html/2503.18278v1"},{"title":"IDPruner: Harmonizing Importance and Diversity in Visual Token Pruning for MLLMs","url":"https://arxiv.org/html/2602.13315"},{"title":"UTPTrack: Towards Simple and Unified Token Pruning for Visual Tracking","url":"https://arxiv.org/html/2602.23734"},{"title":"[2602.03815] Fast-Slow Efficient Training for Multimodal Large Language Models via Visual Token Pruning","url":"https://arxiv.org/abs/2602.03815"}]

Based on the search results, here's information about OTPrune:

## Overview

OTPrune is a training-free framework that formulates pruning as distribution alignment via optimal transport (OT). Multi-modal large language models (MLLMs) achieve strong visual-language reasoning but suffer from high inference cost due to redundant visual tokens, and existing pruning methods overlook the underlying distributional structure of visual representations.

## Key Technical Approach

By minimizing the 2-Wasserstein distance between the full and pruned token distributions, OTPrune preserves both local diversity and global representativeness while reducing inference cost. The framework derives a tractable submodular objective that enables efficient optimization, and theoretically proves its monotonicity and submodularity, providing a principled foundation for stable and efficient pruning.

## Performance

Comprehensive experiments on wider benchmarks demonstrate that OTPrune achieves superior performance–efficiency tradeoffs compared to state-of-the-art methods. OTPrune achieves approximately 90% token reduction with minimal performance drop.

## Availability

The code is available at https://github.com/xiwenc1/OTPrune, and the paper was accepted at CVPR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1698594-f0c0-4aa8-87a6-5283536dd9cd",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "0be210c4-76cc-4700-9df3-e95c7c17f372",
  "toolUseResult": {
    "query": "OTPrune \"Distribution-Aligned Visual Token Pruning\" optimal transport arXiv 2602.20205",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QZ3PTfDwDkKveWG9GsHEtd",
        "content": [
          {
            "title": "[2602.20205] OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport",
            "url": "https://arxiv.org/abs/2602.20205"
          },
          {
            "title": "OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport",
            "url": "https://arxiv.org/html/2602.20205"
          },
          {
            "title": "GitHub - xiwenc1/OTPrune: Official code for the paper: OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport · GitHub",
            "url": "https://github.com/xiwenc1/OTPrune"
          },
          {
            "title": "Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs",
            "url": "https://arxiv.org/html/2604.12035"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0957417425010711"
          },
          {
            "title": "TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model",
            "url": "https://arxiv.org/html/2503.18278v1"
          },
          {
            "title": "IDPruner: Harmonizing Importance and Diversity in Visual Token Pruning for MLLMs",
            "url": "https://arxiv.org/html/2602.13315"
          },
          {
            "title": "UTPTrack: Towards Simple and Unified Token Pruning for Visual Tracking",
            "url": "https://arxiv.org/html/2602.23734"
          },
          {
            "title": "[2602.03815] Fast-Slow Efficient Training for Multimodal Large Language Models via Visual Token Pruning",
            "url": "https://arxiv.org/abs/2602.03815"
          }
        ]
      },
      "Based on the search results, here's information about OTPrune:\n\n## Overview\n\nOTPrune is a training-free framework that formulates pruning as distribution alignment via optimal transport (OT). Multi-modal large language models (MLLMs) achieve strong visual-language reasoning but suffer from high inference cost due to redundant visual tokens, and existing pruning methods overlook the underlying distributional structure of visual representations.\n\n## Key Technical Approach\n\nBy minimizing the 2-Wasserstein distance between the full and pruned token distributions, OTPrune preserves both local diversity and global representativeness while reducing inference cost. The framework derives a tractable submodular objective that enables efficient optimization, and theoretically proves its monotonicity and submodularity, providing a principled foundation for stable and efficient pruning.\n\n## Performance\n\nComprehensive experiments on wider benchmarks demonstrate that OTPrune achieves superior performance–efficiency tradeoffs compared to state-of-the-art methods. OTPrune achieves approximately 90% token reduction with minimal performance drop.\n\n## Availability\n\nThe code is available at https://github.com/xiwenc1/OTPrune, and the paper was accepted at CVPR 2026."
    ],
    "durationSeconds": 6.676471653999994
  },
  "sourceToolAssistantUUID": "a1698594-f0c0-4aa8-87a6-5283536dd9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0be210c4-76cc-4700-9df3-e95c7c17f372",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "VLA token pruning: discrete IB theory under domain shift",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Tool result

_source line 45 · 2026-05-13T05:32:59.055Z_

<details><summary>↩ Tool result · `toolu_01PZGSuTw43Y3BenyaCmhKk1`</summary>

```text
Web search results for query: ""PAC-Bayes" "explains generalisation" "prior engineering" 2025 arXiv 2503.08231"

Links: [{"title":"[2503.08231] How good is PAC-Bayes at explaining generalisation?","url":"https://arxiv.org/abs/2503.08231"},{"title":"How good is PAC-Bayes at explaining generalisation?","url":"https://arxiv.org/html/2503.08231v1"},{"title":"Benjamin Guedj's articles on arXiv","url":"https://arxiv.org/a/guedj_b_1.html"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=12225&show=25"},{"title":"PAC-Bayes Generalization Bound","url":"https://www.emergentmind.com/topics/pac-bayes-generalization-bound"},{"title":"Machine Learning Mar 2025 - stat.ML","url":"https://arxiv.org/list/stat.ML/2025-03?skip=50&show=50"},{"title":"Statistics Mar 2025","url":"https://arxiv.org/list/stat/2025-03?skip=225&show=25"},{"title":"Generalization Bounds: Perspectives from Information Theory and PAC-Bayes | Request PDF","url":"https://www.researchgate.net/publication/388322355_Generalization_Bounds_Perspectives_from_Information_Theory_and_PAC-Bayes"},{"title":"Publications - Benjamin Guedj","url":"https://bguedj.github.io/publications/"},{"title":"ICML Poster Generalization Bounds via Meta-Learned Model Representations: PAC-Bayes and Sample Compression Hypernetworks","url":"https://icml.cc/virtual/2025/poster/45323"}]

I found the paper you're looking for! arXiv 2503.08231 is titled "How good is PAC-Bayes at explaining generalisation?" by Antoine Picard-Weibel, Eugenio Clerico, Roman Moscoviz, and Benjamin Guedj, published March 11, 2025.

The paper's key findings relate directly to your search terms on prior engineering and generalization:

The paper discusses necessary conditions for a PAC-Bayes bound to provide meaningful generalization guarantees, revealing that the optimal generalization guarantee depends solely on the distribution of the risk induced by the prior distribution, and that achieving a target generalization level is only achievable if the prior places sufficient mass on high-performing predictors.

Regarding the implications for explaining generalization: The authors relate these requirements to the prevalent practice of using data-dependent priors in deep learning PAC-Bayes applications, and discuss the implications for the claim that PAC-Bayes "explains" generalisation. More specifically, in deep learning, non-vacuous certificates fundamentally do not arise from the PAC-Bayes formalism alone, but from prior engineering that encodes generalization already, thus PAC-Bayes delivers a rigorous framework for certifying, but not explaining, generalization in modern high-capacity learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3415d94-f843-4a5f-9a64-a5f51167b5e8",
  "isSidechain": false,
  "promptId": "9c335e5a-2572-4f4f-ad50-77fe722201ea",
  "type": "user",
  "uuid": "5d31e90c-f941-4738-8c0c-95f2a202b4ac",
  "toolUseResult": {
    "query": "\"PAC-Bayes\" \"explains generalisation\" \"prior engineering\" 2025 arXiv 2503.08231",
    "results": [
      {
        "tool_use_id": "srvtoolu_01857etr75mhevQdgHh91HxY",
        "content": [
          {
            "title": "[2503.08231] How good is PAC-Bayes at explaining generalisation?",
            "url": "https://arxiv.org/abs/2503.08231"
          },
          {
            "title": "How good is PAC-Bayes at explaining generalisation?",
            "url": "https://arxiv.org/html/2503.08231v1"
          },
          {
            "title": "Benjamin Guedj's articles on arXiv",
            "url": "https://arxiv.org/a/guedj_b_1.html"
          },
          {
            "title": "Computer Science Mar 2025",
            "url": "https://arxiv.org/list/cs/2025-03?skip=12225&show=25"
          },
          {
            "title": "PAC-Bayes Generalization Bound",
            "url": "https://www.emergentmind.com/topics/pac-bayes-generalization-bound"
          },
          {
            "title": "Machine Learning Mar 2025 - stat.ML",
            "url": "https://arxiv.org/list/stat.ML/2025-03?skip=50&show=50"
          },
          {
            "title": "Statistics Mar 2025",
            "url": "https://arxiv.org/list/stat/2025-03?skip=225&show=25"
          },
          {
            "title": "Generalization Bounds: Perspectives from Information Theory and PAC-Bayes | Request PDF",
            "url": "https://www.researchgate.net/publication/388322355_Generalization_Bounds_Perspectives_from_Information_Theory_and_PAC-Bayes"
          },
          {
            "title": "Publications - Benjamin Guedj",
            "url": "https://bguedj.github.io/publications/"
          },
          {
            "title": "ICML Poster Generalization Bounds via Meta-Learned Model Representations: PAC-Bayes and Sample Compression Hypernetworks",
            "url": "https://icml.cc/virtual/2025/poster/45323"
          }
        ]
      },
      "I found the paper you're looking for! arXiv 2503.08231 is titled \"How good is PAC-Bayes at explaining generalisation?\" by Antoine Picard-Weibel, Eugenio Clerico, Roman Moscoviz, and Benjamin Guedj, published March 11, 2025.\n\nThe paper's key findings relate directly to your search terms on prior engineering and generalization:\n\nThe paper discusses necessary conditions for a PAC-Bayes bound to provide meaningful generalization guarantees, revealing that the optimal generalization guarantee depends solely on the distribution of the risk induced by the prior distribution, and that achieving a target generalization level is only achievable if the prior places sufficient mass on high-performing predictors.\n\nRegarding the implications for explaining generalization: The authors relate these requirements to the prevalent practice of using data-dependent priors in deep learning PAC-Bayes applications, and discuss the implications for the claim that PAC-Bayes \"explains\" generalisation. More specifically, in deep learning, non-vacuous certificates fundamentally do not arise from the PAC-Bayes formalism alone, but from prior engineering that encodes generalization already, thus PAC-Bayes delivers a rigorous framework for certifying, but not explaining, generalization in modern high-capacity learning systems."
    ],
    "durationSeconds": 6.598975563999964
  },
  "sourceToolAssistantUUID": "d3415d94-f843-4a5f-9a64-a5f51167b5e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-13T05:33:33.165Z_

<details><summary>Logged reasoning block</summary>

```text
Very important finding: OTPrune (arXiv 2602.20205, CVPR 2026) is another highly relevant paper the proposal missed. It uses optimal transport to frame pruning as distribution alignment, minimizing the 2-Wasserstein distance between full and pruned token distributions. It provides theoretical guarantees (monotonicity and submodularity proofs). This is directly relevant to the proposal's concern about distribution shift from pruning.

Now I have all the information I need. Let me synthesize and write my review.

Key issues for this round:

1. **MISSING RELATED WORK — RCP (arXiv 2604.04972, April 2026)**: Directly addresses distribution shift from token pruning in LVLMs. 

2. **MISSING RELATED WORK — OTPrune (arXiv 2602.20205, CVPR 2026)**: Uses optimal transport for distribution-aligned token pruning with theoretical guarantees including submodularity proofs—highly relevant to the proposal's distribution shift analysis.

3. **Random pruning effectiveness (ACL 2025 Findings)**: Wen et al. demonstrate that random pruning outperforms more sophisticated methods, which challenges whether task-conditioned pruning provides meaningful improvements and questions the validity of the IB-based theoretical framework.

4. **SubLoRA for LoRA fine-tuning** —

the bounds haven't been validated on LoRA-fine-tuned models since SubLoRA was originally designed for pretraining from scratch.

5. **PAC-Bayes explanatory skepticism (arXiv 2503.08231)**: A recent paper argues that PAC-Bayes bounds certify generalization without explaining it, and their quality hinges on prior engineering rather than actual learning dynamics.

6. **LightVLA correction needed**: The reported +2.9% should be +2.6%.

7. **Ordinal predictions fallacy**: The fallback to vacuous bounds for ranking lacks any rigorous theoretical justification.

Looking back at the previous round's feedback, I've partially strengthened the theoretical narrative but haven't adequately addressed the ordinal prediction gap—it's still acknowledged rather than resolved.

I did add the missing citations and better positioned the k* contribution, though the LightVLA accuracy error persists in the landscape section. The scope remains ambitious despite suggestions to narrow it.

Now scoring novelty: the core gap is real—no prior work combines information-bottleneck theory with generalization bounds for discrete token selection in VLAs under distribution shift, and the stochastic mask formalization is a legitimate contribution. But there are related precedents: BC-IB applied IB plus generalization to robot manipulation, OTPrune offers distribution-aligned pruning with submodularity guarantees, and RCP directly addresses—

The theoretical contribution feels narrower than initially framed because the bounds end up vacuous, which limits the explanatory power. Feasibility sits at a 3 out of 5—SubLoRA for LoRA fine-tuning is unproven and risky, MI estimation at VLA scale is still challenging, the random pruning baseline could undercut the narrative, and the timeline is tight, though the experimental infrastructure with OpenVLA and LIBERO is already in place. The proposal is clearer now with a comprehensive landscape and solid mathematical framing, but the impact hinges on whether the theoretical analysis actually explains why pruning improves generalization—and if the bounds are vacuous and ordinal predictions lack theoretical grounding, the contribution becomes more empirical than theoretical.

Averaging the scores gives 3.375, which falls below the 4.0 threshold, so revision is needed. The core issues are addressable: missing related work like RCP and OTPrune, the random pruning baseline challenging the premise, the SubLoRA applicability gap, the PAC-Bayes bound's limited explanatory reach, and the LightVLA accuracy discrepancy. The idea has genuine merit and the gap is real, so this warrants revision rather than rejection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d31e90c-f941-4738-8c0c-95f2a202b4ac",
  "isSidechain": false,
  "requestId": "req_011Caz2DmUcqLuAWM844x48o",
  "type": "assistant",
  "uuid": "e36be1c2-20d3-4357-90a6-5da754e95024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MEvRCNnptjZ9EjkjvqzUn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 54935,
      "output_tokens": 3774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3774,
          "cache_read_input_tokens": 54935,
          "cache_creation_input_tokens": 1855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1855
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

_source line 47 · 2026-05-13T05:34:31.566Z_

Now I have comprehensive research across all dimensions. Let me synthesize my findings into the final review.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The gap is genuine — no work provides IB-based distribution-shift generalization bounds for discrete VLA token selection. However, the contribution space is narrower than presented: OTPrune (CVPR 2026) already provides distribution-aligned pruning with theoretical guarantees (submodularity/monotonicity proofs), RCP (arXiv 2604.04972) directly addresses distribution shift from pruning empirically, and the PAC-Bayes bounds will likely be vacuous, reducing the theoretical novelty to qualitative insights (stochastic mask formalization + k* phase transition) that are solid but not 4-score territory."},
    "feasibility": {"score": 3, "rationale": "SubLoRA-style bound computation for LoRA-fine-tuned models is completely unvalidated in the literature — SubLoRA was designed for pretraining from scratch, not post-hoc fine-tuning. Additionally, Wen et al. (ACL 2025 Findings) show random pruning outperforms sophisticated methods, which could empirically undermine the central claim that task-conditioned pruning preferentially removes domain-variant information. These two risks are substantial and underaddressed."},
    "clarity": {"score": 4, "rationale": "The proposal is comprehensive, well-structured, and has improved significantly across three revision rounds. The BC-IB differentiation is now clear, the stochastic mask formalization is precisely articulated, and the landscape coverage of 15+ VLA pruning methods is thorough. The mathematical setup (stochastic binary mask IB objective) is well-defined."},
    "impact": {"score": 3, "rationale": "The user asked for theoretical analysis of WHY token pruning enhances VLA generalization. A vacuous PAC-Bayes bound with an 'ordinal predictions' fallback — for which no rigorous theoretical justification exists (arXiv 2503.08231 argues PAC-Bayes certifies but does not explain generalization) — does not deliver a convincing theoretical 'why.' The k* phase transition and qualitative IB insights are valuable but may not reach the bar of a satisfying theoretical explanation at a top venue."}
  },
  "issues": [
    "MISSING RELATED WORK — OTPrune (arXiv 2602.20205, CVPR 2026) formulates token pruning as distribution alignment via optimal transport, minimizing the 2-Wasserstein distance between full and pruned token distributions, and provides theoretical guarantees (proved monotonicity and submodularity of the pruning objective). This is directly relevant to the proposal's distribution-shift analysis and provides an alternative theoretical framework for principled token selection that the proposal must cite and differentiate from. OTPrune achieves ~90% token reduction with minimal performance drop and has code available.",
    "MISSING RELATED WORK — RCP (arXiv 2604.04972, April 2026) directly addresses distribution shift caused by token pruning in LVLMs, measuring layer-by-layer drift via squared 2-Wasserstein distance and proposing a Delayed Repair Adapter with FiLM-based modulation. While purely empirical (no formal bounds), it is the only 2026 work that explicitly identifies and mitigates the distribution shift problem from token pruning — the very problem the proposal's domain-shift bound targets theoretically. Must be cited.",
    "RANDOM PRUNING BASELINE CHALLENGE — Wen et al. ('Token Pruning in MLLMs: Are We Solving the Right Problem?', ACL 2025 Findings) demonstrate that random token selection outperforms FastV and SparseVLM at 75% and 88.9% pruning ratios on LLaVA-1.5. This directly challenges the proposal's central thesis that task-conditioned pruning is superior because it preferentially removes domain-variant information. If random pruning achieves comparable or better results, the IB-based explanation of WHY intelligent selection helps becomes moot — the mechanism might simply be 'fewer tokens = less overfitting' rather than 'information-theoretic selection removes domain-variant features.' The proposal must address this baseline and explain how its theory accounts for the random pruning phenomenon.",
    "SubLoRA APPLICABILITY GAP — No published work applies SubLoRA-style compression bounds to LoRA-fine-tuned models. SubLoRA was designed for pretraining from scratch (combining LoRA + subspace training during initial training); applying it post-hoc to LoRA fine-tuning weights is a novel and untested extension. Moreover, the non-vacuous bounds achieved by SubLoRA and Lotfi et al. (NeurIPS 2024) exploit billions of training tokens as data points — fine-tuning datasets (e.g., LIBERO-90) have orders of magnitude fewer data points, making vacuity far more likely even with LoRA's reduced parameter count.",
    "PAC-BAYES EXPLANATORY LIMITATION — Picard-Weibel et al. ('How good is PAC-Bayes at explaining generalisation?', arXiv 2503.08231, March 2025) prove that PAC-Bayes bound quality depends solely on the risk distribution induced by the prior, and that non-vacuous certificates in deep learning arise from prior engineering encoding generalization knowledge, not from the PAC-Bayes formalism itself. They conclude PAC-Bayes 'certifies but does not explain' generalization. This directly undermines the proposal's claim to provide a theoretical explanation of WHY token pruning improves generalization via PAC-Bayes bounds. The proposal should either engage with this critique explicitly or reframe the theoretical contribution away from PAC-Bayes certification toward the qualitative IB insights.",
    "ORDINAL PREDICTIONS FALLBACK STILL LACKS THEORETICAL BACKING — The proposal acknowledges bounds will likely be vacuous and falls back to 'ordinal predictions' (relative ranking across token budgets). However, a vacuous bound (≥1) provides no formal guarantee about ordinal ranking either. The MDL/compression analogy is invoked but not formalized. No rigorous result shows that PAC-Bayes bound ordering is preserved when absolute values are vacuous. This makes the core theoretical contribution hinge on an unproven assumption.",
    "LIGHTV LA ACCURACY STILL UNCORRECTED — The landscape section states LightVLA achieves '+2.9% improvement' but the actual paper (arXiv 2509.12594) reports +2.6%. This was flagged in Round 2 and explicitly requested to be corrected in Round 3 feedback. Three rounds later, it remains wrong.",
    "AUTHOR ATTRIBUTION ERROR — arXiv 2407.18158 is cited as 'Kuang et al. (NeurIPS 2024 Spotlight)' but the first author is Sanae Lotfi (Kuang is second author). Should be 'Lotfi et al.'"
  ],
  "feedback": "The proposal has matured substantially across three revision rounds — BC-IB differentiation is excellent, the stochastic mask formalization resolves the discrete IB subtlety elegantly, and the honest acknowledgment of bound vacuity is appropriate. However, several issues remain that prevent a pass:\n\n1. **Address the random pruning challenge head-on**: Wen et al. (ACL 2025 Findings) is the single most important paper for this proposal to engage with. If random pruning outperforms sophisticated methods, the proposal's theory must explain this: perhaps random pruning also reduces I(X;M) (since any pruning compresses), and the theory predicts that random pruning helps generalization too — but task-conditioned pruning achieves better I(Z_M;Y) preservation, yielding a tighter bound. The empirical comparison of task-conditioned vs. random pruning (already planned) becomes the critical experiment, not a side analysis. Frame the random pruning effectiveness as *supporting* the IB thesis (compression helps generalization) while arguing task-conditioned pruning optimizes the compression-relevance tradeoff.\n\n2. **Cite OTPrune and RCP, differentiate clearly**: OTPrune (CVPR 2026) provides a competing theoretical framework (OT-based distribution alignment with submodularity proofs) for principled token selection. RCP (April 2026) empirically addresses distribution shift from pruning. Your contribution should be positioned as: OTPrune provides selection-quality guarantees but not generalization bounds; RCP repairs drift empirically but lacks theoretical understanding; your work provides the generalization-theoretic framework connecting compression to domain-shift robustness.\n\n3. **Restructure the theoretical contribution away from PAC-Bayes certification**: Given Picard-Weibel et al.'s (2025) critique, consider restructuring: (a) Lead with qualitative IB theory — prove that stochastic mask pruning with I(X;M) minimization tightens a generalization gap under specific distributional assumptions; (b) The k* phase transition as a principled token budget selection tool; (c) Relegate PAC-Bayes bound computation to 'numerical evaluation' rather than the core contribution. The theoretical 'why' should come from the IB insight + distributional argument, not from the bound value.\n\n4. **Honestly scope the SubLoRA component**: Acknowledge that SubLoRA for LoRA fine-tuning is novel and untested. Treat it as an experimental contribution (can we get non-vacuous bounds for fine-tuned VLAs?) rather than assuming it works. If it fails, the rest of the paper should stand on the qualitative IB theory + k* + empirical validation.\n\n5. **Fix recurring errors**: LightVLA is +2.6%, not +2.9%. 'Kuang et al.' should be 'Lotfi et al.' for arXiv 2407.18158.\n\n6. **Consider whether the paper is trying to do too much**: Stochastic mask IB formalization + domain-shift bound + k* phase transition + SubLoRA bound computation + three MI estimators + GIB synergy characterization + LIBERO-Plus validation across 9 token budgets is an enormous scope. For a focused ICLR 2027 submission, consider: stochastic mask IB (core theory) + k* phase transition (core theory) + domain-shift predictions (core empirical) + random vs. task-conditioned pruning comparison (critical experiment). Drop GIB synergy, reduce MI estimators to two, and treat SubLoRA as an optional stretch goal.",
  "reason": "Genuine theoretical gap but critical challenges remain: the random pruning baseline threatens the premise, SubLoRA applicability to LoRA fine-tuning is unvalidated, PAC-Bayes explanatory power is fundamentally questioned by recent work, two important 2026 papers (OTPrune CVPR, RCP) are missing, and the LightVLA accuracy error persists after three rounds."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e36be1c2-20d3-4357-90a6-5da754e95024",
  "isSidechain": false,
  "requestId": "req_011Caz2DmUcqLuAWM844x48o",
  "type": "assistant",
  "uuid": "f86074c7-f6d4-46b6-98f7-e313631c0009",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MEvRCNnptjZ9EjkjvqzUn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 54935,
      "output_tokens": 3774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3774,
          "cache_read_input_tokens": 54935,
          "cache_creation_input_tokens": 1855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1855
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

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f86074c7-f6d4-46b6-98f7-e313631c0009",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "VLA token pruning: discrete IB theory under domain shift",
  "sessionId": "4e2e1b29-dee4-426c-8c21-6de856d44d69"
}
```

---
