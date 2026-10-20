# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 139
- **Recorded user turns:** 1
- **Tool calls:** 45
- **Original source:** `logs/chats/exported-trajectories/account-3/935e2014-ee5c-4147-85a1-8ed314c9698e.jsonl`
- **Structured JSON:** [`75aec33aaf48334a3c32.json`](../../sessions/75/75aec33aaf48334a3c32.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T04:35:04.032Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T04:35:04.032Z",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **VLA中的token裁剪/增强能否提升VLA模型的泛化性（多从理论角度分析为何能增强）**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 2/10)\n{\n  \"title\": \"Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring\",\n  \"core_problem\": \"VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025) further reveals that many attention-based token pruning methods underperform even naive random selection, exposing the absence of principled criteria for identifying which visual tokens truly matter for action prediction. Meanwhile, simple adaptation methods like Feature Token Modulation (FTM, arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?\",\n  \"opportunity\": \"Two research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, and (2) VLA token pruning for efficiency (VLA-Pruner, VLA-IAP, OTPrune), using attention or geometric heuristics without causal grounding. A third thread — causal attention distillation (LeaF, NeurIPS 2025) — applies causal token identification in NLP but has not been adapted to VLA action policies. The key insight connecting these threads is that visual tokens in VLA transformers exhibit *spatial locality of causal features*: task-relevant information (object poses, gripper state, contact geometry) is spatially localized in specific tokens, while spurious features (background, lighting) are spatially distributed. This spatial structure makes token-level selection a natural and efficient unit for causal separation — unlike feature-level approaches (Causal-ACT) where causal and spurious information may be entangled across every feature dimension. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring for scalability, would provide the principled criterion that existing pruning methods lack.\",\n  \"landscape\": \"**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) up from the original 79.6% (OpenVLA-OFT+). **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features and selecting the best graph via interventional evaluation — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures (ResNet encoder, not VLA transformers), uses heuristic energy-based graph search rather than formal causal criteria, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation — demonstrating that VLAs contain substantial latent robustness recoverable through simple recalibration. However, FTM has not been evaluated on the full LIBERO-Plus benchmark (only LIBERO viewpoint), provides no interpretability of what is being recalibrated or why, and its affine transform may be insufficient for perturbation types requiring selective token exclusion (e.g., distractor objects, background changes). FLA extends FTM to 90.8% with 4.7M parameters. **Active attention approaches**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention conditioned on task history, achieving 74.7% on LIBERO-Plus — strong but below SRPO. **Token pruning for VLAs**: VLA-Pruner (arXiv 2511.16449) and VLA-IAP (arXiv 2603.22991) prune tokens using attention-based and geometric/motion-IoU criteria respectively, but neither provides causal grounding. SP-VLA (arXiv 2506.12723) jointly schedules models and prunes tokens. Critically, arXiv 2502.11501 (ACL Findings 2025) shows many attention-based token pruning methods underperform random selection due to flawed scoring — directly motivating causally grounded alternatives. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens and prunes them via causal attention distillation. While directly analogous in spirit, LeaF targets LLM reasoning (not embodied action), uses gradient heuristics (not formal interventions), and does not address cross-environment invariance. **Shortcut learning**: Shortcut Learning in Generalist Robot Policies (CoRL 2025, arXiv 2508.06426) identifies dataset diversity and fragmentation as root causes of shortcut learning, proposing data augmentation solutions — a complementary approach addressing the data side rather than the model/inference side. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization and VLM-based feature removal with heuristic criteria. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck in world models, but evaluates on LIBERO and RLBench — not LIBERO-Plus — so robustness under controlled perturbations is unknown. **IRM limitations**: Rosenfeld et al. (ICLR 2021) demonstrate that IRM fails catastrophically in non-linear settings and requires more training environments than dimensions of environmental features, necessitating careful treatment of any IRM-inspired invariance claims. **No existing work combines formal token-level causal intervention criteria with amortized scalable estimation within VLA transformer architectures for cross-environment policy invariance.**\",\n  \"approach\": \"We propose Causal Token Selection (CaTS) v2, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework that avoids the combinatorial cost of per-token ACE estimation.\\n\\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is tokenized into T(O) = {t_1,...,t_N}; each token t_i carries causal content C_i (object geometry, gripper state) and spurious content S_i (background, lighting); environment variable E influences S_i but not C_i; action A = π(C_1,...,C_N) depends only on causal content. We formalize the *spatial locality of causal features* assumption: causal content C_i is concentrated in a strict subset T* ⊂ T, while spurious content S_i is distributed across all tokens. Under this assumption, token-level selection recovers a lower-dimensional causal identification problem than feature-level selection (as in Causal-ACT), improving finite-sample convergence.\\n\\n**Theorem (Conditional Invariance, sketch).** Under four explicit assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span the support of relevant E dimensions; (A4) finite-sample convergence of intervention estimates — the causal token selection operator S_τ with threshold τ satisfies: the selected set S_τ(T) ⊇ T* with probability ≥ 1-δ, and the resulting policy π(a|S_τ(T)) achieves ε-invariance: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ), where ε decreases with the number of environments N_env and intervention samples M. **Failure modes (explicit):** (F1) Insufficient environment diversity violates A3, confounding causal and spurious features — same fundamental limitation as IRM (Rosenfeld et al., 2021). (F2) Non-linear entanglement of causal/spurious content within individual tokens makes token-level selection a coarse operator. (F3) Amortization gap between the learned scorer and true ACE. We provide analysis of each failure mode's impact and mitigation strategies.\\n\\n**Amortized Causal Scoring (ACS).** Rather than computing per-token ACE via O(N × K) individual interventions (N tokens × K environments), we train a lightweight causal scoring head attached to the frozen VLA backbone. Training data for the scorer is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP, <1M parameters) learns to predict token-level causal effects from token embeddings in a single forward pass, amortizing the intervention cost. This is inspired by recent amortized causal estimation work (ACTIVA, arXiv 2503.01290).\\n\\n**Variance-Regularized Selection.** Instead of an IRM penalty (which fails in non-linear settings), we use V-REx-style variance regularization: the scoring head is trained to minimize action prediction loss while penalizing the *variance* of per-environment losses for the selected token subset. This provides distributional robustness without claiming strict invariance guarantees. The penalty weight is treated as a hyperparameter with explicit sensitivity analysis.\\n\\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head and a thin LoRA adaptation layer (~4M parameters total) are the only trainable components. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned. This provides both robustness (by removing spuriously correlated tokens) and efficiency (by reducing the token count for the action decoder).\\n\\n**Evaluation.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift, targeting the current SOTA of 82.1% (SRPO). Baselines: (1) SRPO — current SOTA, RL-based; (2) FTM/FLA — simple affine adaptation (we reproduce on LIBERO-Plus since original paper only evaluates LIBERO viewpoint); (3) Causal-ACT — adapted to OpenVLA backbone (we implement token-level analog of their feature-masking approach); (4) AVA-VLA — active visual attention; (5) VLA-Pruner — attention-based pruning; (6) VLA-IAP — geometric/interaction pruning; (7) RobustVLA — heuristic robust optimization; (8) Random token pruning — critical control baseline per findings of arXiv 2502.11501; (9) LeaF-adapted — gradient-guided causal pruning adapted from NLP to VLA. Ablations: (a) amortized vs. exact ACE estimation accuracy; (b) variance penalty weight sensitivity; (c) pruning ratio sweep (10-90%); (d) per-perturbation-dimension analysis; (e) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions?).\\n\\n**Key differentiations.** vs. Causal-ACT: token-level in 7B VLA transformers (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation (not single ALOHA task). vs. FTM: interpretable per-token causal scores (not black-box affine transform); selective token removal for distractor/background robustness (not global recalibration). vs. LeaF: VLA action policies (not NLP reasoning); cross-environment invariance objective (not single-domain teacher distillation); formal SCM (not gradient heuristics). vs. VLA-Pruner/IAP: causal criteria with formal conditions (not attention/geometric heuristics that may underperform random per arXiv 2502.11501).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~700h A100 (80GB): ~300h for 20-25 LoRA fine-tuning runs with ACS head at ~15h each, ~200h for batch intervention data generation and amortized scorer training across LIBERO-Plus environments (substantially more than original 100h estimate — generating sufficient intervention data for N=256 tokens × 7 perturbation types × multiple severity levels requires systematic coverage), ~200h for baseline reproduction (FTM on LIBERO-Plus, Causal-ACT adaptation, 9 baselines total) and ablations\",\n      \"gpu_utilization\": \"Low (~25-30%). GPUs sit idle while researchers write code, debug the causal scoring pipeline, analyze intervention results, and iterate on the variance penalty and Shapley decomposition.\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers (one with causal inference/SCM background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)\",\n      \"estimated_gpu_cost\": \"~$1,050 (700h × $1.50/hr A100 spot pricing, May 2026 market rate)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~1000h A100 (80GB): agent explores ~35-45 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions, and evaluates all 9 baselines\",\n      \"gpu_utilization\": \"Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: amortized scorer architecture, Shapley decomposition strategy, variance penalty weight, theorem assumption validation.\",\n      \"timeline\": \"2-4 months\",\n      \"team\": \"1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, and validating theoretical claims\",\n      \"claude_api_cost\": \"$400-600 (4000-6000 conversation turns for experiment design, code generation, theorem checking, result analysis)\",\n      \"estimated_gpu_cost\": \"~$1,500 (1000h × $1.50/hr)\",\n      \"risk_note\": \"Amortized scorer design requires careful validation — human judgment is critical to verify that the scorer's predictions correlate with ground-truth ACE (computed exactly on a small validation set). Theorem formalization needs human review by someone with causal inference expertise.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~2000h A100 (80GB): agent runs 100-120 experiment configurations including aggressive sweeps for variance penalty, pruning ratios, Shapley approximation methods, scorer architectures, plus all baseline reproductions and failed exploration runs\",\n      \"gpu_utilization\": \"High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.\",\n      \"timeline\": \"3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs\",\n      \"team\": \"0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution and Shapley sampling strategy)\",\n      \"claude_api_cost\": \"$600-1000 (6000-10000 turns for autonomous experiment design, debugging, and paper drafting)\",\n      \"estimated_gpu_cost\": \"~$3,000 (2000h × $1.50/hr)\",\n      \"speed_bottleneck\": \"Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments).\",\n      \"risk_note\": \"Without human gates, agent may over-explore suboptimal Shapley approximations or scorer architectures. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification. Risk mitigation: pre-define structured search space with early stopping on scorer validation metrics.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (deadline: May 29, 2026 — extremely tight given revision scope, stretch goal only)\",\n    \"AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development and experiments)\",\n    \"ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation)\",\n    \"ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)\",\n    \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)\",\n    \"Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)\",\n    \"Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)\",\n    \"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)\",\n    \"The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)\",\n    \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)\",\n    \"AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)\",\n    \"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)\",\n    \"Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)\",\n    \"Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026) — evaluated on LIBERO/RLBench only, NOT LIBERO-Plus\",\n    \"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)\",\n    \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)\",\n    \"Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)\",\n    \"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\"\n  ],\n  \"description\": \"VLA models suffer catastrophic failures under visual distribution shifts due to spurious correlations, yet recent work reveals that (a) many token pruning methods underperform random selection (arXiv 2502.11501), exposing the need for principled selection criteria, and (b) simple affine recalibration (FTM) can recover surprising robustness, but without interpretability or formal grounding. We propose Causal Token Selection (CaTS) v2, bridging three disconnected threads: VLA token pruning (VLA-Pruner, VLA-IAP), causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF). CaTS defines a formal SCM over the VLA token-action pipeline, introduces the *spatial locality of causal features* assumption (task-relevant information is spatially concentrated in token subsets while spurious features are distributed), and proves conditional invariance under four explicit assumptions — with documented failure modes when assumptions are violated, avoiding the overclaiming that plagues IRM-based approaches (Rosenfeld et al., 2021). For scalability, CaTS uses Amortized Causal Scoring: a lightweight head (<1M params) trained on batch stochastic interventions with Shapley-value decomposition, predicting per-token causal effects in a single forward pass rather than requiring O(N×K) individual interventions. A V-REx-style variance penalty replaces the problematic IRM objective for distributional robustness. Key differentiations: vs. Causal-ACT (arXiv 2507.22380) — token-level in 7B VLA transformers rather than feature-level in ResNet+ACT, amortized scoring rather than heuristic graph search, comprehensive LIBERO-Plus evaluation rather than single ALOHA task; vs. FTM — interpretable causal scores per token rather than black-box affine transform, selective token removal for distractor robustness; vs. LeaF — VLA action policies rather than NLP, cross-environment invariance rather than single-domain distillation. Evaluated on LIBERO-Plus across all 7 perturbation dimensions against 9 baselines including SRPO (82.1% SOTA), FTM (reproduced on LIBERO-Plus), Causal-ACT (adapted to VLA backbone), AVA-VLA, and random pruning. All building blocks are open-source. Primary targets: AAAI 2027 and ICLR 2027.\",\n  \"project_name\": \"causal_token_sel_vla\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING WORK: 'Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations' (arXiv 2507.22380, July 2025) applies causal intervention to resolve causal confusion in robotic imitation learning—directly overlapping with CaTS's core motivation and approach. This paper was NOT cited.\", \"CRITICAL MISSING WORK: 'VLA Models Are More Generalizable Than You Think' (arXiv 2512.02902) shows Feature Token Modulation (FTM) achieves 87.1% on LIBERO viewpoint with only 4K parameters—a much simpler and cheaper alternative that undermines CaTS's complexity justification. Must be included as a baseline.\", \"MISSING WORK: 'Learning to Focus: Causal Attention Distillation (LeaF)' (NeurIPS 2025, arXiv 2506.07851) uses causal intervention at the token level for pruning confounding tokens. While targeting NLP, the method is directly analogous and must be discussed.\", \"MISSING WORK: 'Shortcut Learning in Generalist Robot Policies' (CoRL 2025, arXiv 2508.06426) addresses the same shortcut/spurious correlation problem through dataset design—a competing solution approach.\", \"MISSING WORK: 'Token Pruning in MLLMs: Are We Solving the Right Problem?' (arXiv 2502.11501, ACL Findings 2025) raises fundamental questions about attention-based token pruning, finding some methods underperform random selection. Must be addressed.\", \"OVERCLAIMED THEORY: 'Provable invariance guarantees' via IRM-style penalty is not justified. IRM fails catastrophically in non-linear settings (Rosenfeld et al., ICLR 2021), requires environment coverage that LIBERO-Plus may not provide, and the IRMv1 penalty doesn't always capture invariance correctly. These failure modes must be acknowledged and addressed.\", \"INVALID BASELINE: Mask World Model (arXiv 2604.19683) evaluates on LIBERO and RLBench, NOT LIBERO-Plus. Listing it as a LIBERO-Plus baseline comparison is misleading.\", \"INSUFFICIENT THEORETICAL DEPTH: The user specifically requested '多从理论角度分析为何能增强' (theoretical analysis of WHY token pruning enhances generalization). The idea merely invokes do-calculus and IRM without formal results—no theorems, no proofs, no explicit assumptions. The theoretical contribution is the supposed differentiator from VLA-Pruner/IAP but is undeveloped.\", \"ACE ESTIMATION SCALABILITY: Estimating per-token ACE by intervening (replacing embeddings with marginal statistics) across multiple environments is combinatorially expensive. For 256+ tokens × multiple perturbation types × sufficient samples for stable KL-divergence estimates, the 100h GPU estimate for 'causal effect estimation sweeps' likely significantly underestimates the real cost.\", \"STALE SOTA TARGET: The 79.6% LIBERO-Plus SOTA may already be surpassed by FTM-style approaches or Mask World Model adaptations. The generator should verify this is still current.\"]\nFeedback: The core idea of using causal criteria for VLA token selection has merit, but significant revisions are needed:\n\n1. **Add missing related work urgently**: (a) arXiv 2507.22380 on causal confusion in imitation learning—this is your closest competitor and must be discussed with clear differentiation. (b) arXiv 2512.02902 (FTM)—this simple 4K-parameter method achieves strong robustness and must be a baseline. If CaTS cannot outperform FTM, the entire approach is questionable. (c) LeaF (NeurIPS 2025)—the NLP-domain analog of your idea. (d) 'Shortcut Learning in Generalist Robot Policies' (CoRL 2025). (e) arXiv 2502.11501 on fundamental problems with token pruning.\n\n2. **Develop the theoretical framework seriously or drop the 'provable guarantees' claim**: The user's core requirement is theoretical analysis. You need: (a) A formal SCM for the VLA token → action pipeline with explicit assumptions. (b) A theorem stating under what conditions causal token selection yields invariant policies, with at least a proof sketch. (c) Explicit discussion of when the guarantees break (IRM failure modes, insufficient environment diversity, non-linear interactions). Without this, the paper is just another engineering method paper, which doesn't match the user's request.\n\n3. **Fix the Mask World Model baseline**: Either demonstrate MWM on LIBERO-Plus yourself or remove it from the comparison table.\n\n4. **Address ACE estimation scalability**: Provide a realistic computational analysis of per-token intervention costs. Consider approximations (e.g., batch interventions, amortized estimation) and include these in the method.\n\n5. **Strengthen differentiation from arXiv 2507.22380**: That paper already does causal intervention in imitation learning. Your contribution must be clearly at the token level within transformer VLA architectures, not just causal intervention in general.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T04:35:04.038Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T04:35:04.038Z",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

## Round 1

137 recorded events

### User

_source line 3 · 2026-05-13T04:35:04.077Z_

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

## Idea under review (round 2/10)
{
  "title": "Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring",
  "core_problem": "VLA models learn spurious visual correlations — attending to background textures, lighting conditions, and distractor objects that co-occur with target actions in training data — causing catastrophic failure under visual distribution shifts. Recent work (arXiv 2502.11501, ACL Findings 2025) further reveals that many attention-based token pruning methods underperform even naive random selection, exposing the absence of principled criteria for identifying which visual tokens truly matter for action prediction. Meanwhile, simple adaptation methods like Feature Token Modulation (FTM, arXiv 2512.02902) can recover substantial robustness with only 4K parameters, raising the question: can we identify *why* certain tokens matter and provide interpretable, formally grounded selection criteria rather than black-box affine recalibration?",
  "opportunity": "Two research threads have developed in isolation: (1) causal intervention for imitation learning robustness (Causal-ACT, arXiv 2507.22380; ICIL, NeurIPS 2021), operating at the feature level in smaller architectures, and (2) VLA token pruning for efficiency (VLA-Pruner, VLA-IAP, OTPrune), using attention or geometric heuristics without causal grounding. A third thread — causal attention distillation (LeaF, NeurIPS 2025) — applies causal token identification in NLP but has not been adapted to VLA action policies. The key insight connecting these threads is that visual tokens in VLA transformers exhibit *spatial locality of causal features*: task-relevant information (object poses, gripper state, contact geometry) is spatially localized in specific tokens, while spurious features (background, lighting) are spatially distributed. This spatial structure makes token-level selection a natural and efficient unit for causal separation — unlike feature-level approaches (Causal-ACT) where causal and spurious information may be entangled across every feature dimension. Formalizing this insight via a structural causal model over the token-action pipeline, with amortized interventional scoring for scalability, would provide the principled criterion that existing pruning methods lack.",
  "landscape": "**Robustness benchmarking**: LIBERO-Plus (arXiv 2510.13626, CVPR 2026) demonstrates VLA catastrophic failures across 7 perturbation dimensions, with the current SOTA at 82.1% average success (SRPO, arXiv 2511.15605) up from the original 79.6% (OpenVLA-OFT+). **Causal approaches in imitation learning**: Causal-ACT (arXiv 2507.22380, July 2025) integrates causal structure learning into ACT by learning binary causal graphs over ResNet features and selecting the best graph via interventional evaluation — achieving 0.82 OOD success on ALOHA cube transfer vs. 0.23 for standard ACT. However, it operates at the feature level in small architectures (ResNet encoder, not VLA transformers), uses heuristic energy-based graph search rather than formal causal criteria, and evaluates on a single simple task. ICIL (NeurIPS 2021) learns domain-invariant features for imitation but not at the token level. CLIP-ICM (ICML 2025) applies causal invariance to VLMs via SCMs but for classification, not action policies. **Simple adaptation baselines**: FTM (arXiv 2512.02902) achieves 87.1% on LIBERO viewpoint with just 4K parameters via global affine token modulation — demonstrating that VLAs contain substantial latent robustness recoverable through simple recalibration. However, FTM has not been evaluated on the full LIBERO-Plus benchmark (only LIBERO viewpoint), provides no interpretability of what is being recalibrated or why, and its affine transform may be insufficient for perturbation types requiring selective token exclusion (e.g., distractor objects, background changes). FLA extends FTM to 90.8% with 4.7M parameters. **Active attention approaches**: AVA-VLA (arXiv 2511.18960) dynamically reweights visual tokens via active attention conditioned on task history, achieving 74.7% on LIBERO-Plus — strong but below SRPO. **Token pruning for VLAs**: VLA-Pruner (arXiv 2511.16449) and VLA-IAP (arXiv 2603.22991) prune tokens using attention-based and geometric/motion-IoU criteria respectively, but neither provides causal grounding. SP-VLA (arXiv 2506.12723) jointly schedules models and prunes tokens. Critically, arXiv 2502.11501 (ACL Findings 2025) shows many attention-based token pruning methods underperform random selection due to flawed scoring — directly motivating causally grounded alternatives. **Causal token pruning in NLP**: LeaF (NeurIPS 2025, arXiv 2506.07851) uses gradient-based teacher-student comparison to identify confounding tokens and prunes them via causal attention distillation. While directly analogous in spirit, LeaF targets LLM reasoning (not embodied action), uses gradient heuristics (not formal interventions), and does not address cross-environment invariance. **Shortcut learning**: Shortcut Learning in Generalist Robot Policies (CoRL 2025, arXiv 2508.06426) identifies dataset diversity and fragmentation as root causes of shortcut learning, proposing data augmentation solutions — a complementary approach addressing the data side rather than the model/inference side. **Robustness training**: RobustVLA (ICLR 2026, arXiv 2510.00037) uses offline robust optimization and VLM-based feature removal with heuristic criteria. **World models**: Mask World Model (arXiv 2604.19683) achieves 98.3% on standard LIBERO via geometric information bottleneck in world models, but evaluates on LIBERO and RLBench — not LIBERO-Plus — so robustness under controlled perturbations is unknown. **IRM limitations**: Rosenfeld et al. (ICLR 2021) demonstrate that IRM fails catastrophically in non-linear settings and requires more training environments than dimensions of environmental features, necessitating careful treatment of any IRM-inspired invariance claims. **No existing work combines formal token-level causal intervention criteria with amortized scalable estimation within VLA transformer architectures for cross-environment policy invariance.**",
  "approach": "We propose Causal Token Selection (CaTS) v2, which identifies and retains visual tokens whose causal effect on action predictions is significant and stable across visual environments, using an amortized interventional scoring framework that avoids the combinatorial cost of per-token ACE estimation.\n\n**Formal SCM for VLA Token-Action Pipeline.** We define a structural causal model: observation O is tokenized into T(O) = {t_1,...,t_N}; each token t_i carries causal content C_i (object geometry, gripper state) and spurious content S_i (background, lighting); environment variable E influences S_i but not C_i; action A = π(C_1,...,C_N) depends only on causal content. We formalize the *spatial locality of causal features* assumption: causal content C_i is concentrated in a strict subset T* ⊂ T, while spurious content S_i is distributed across all tokens. Under this assumption, token-level selection recovers a lower-dimensional causal identification problem than feature-level selection (as in Causal-ACT), improving finite-sample convergence.\n\n**Theorem (Conditional Invariance, sketch).** Under four explicit assumptions — (A1) causal sufficiency: A ⊥ E | C(T*); (A2) token-level identifiability: do(t_i) changes C(T*) with positive probability for t_i ∈ T*; (A3) environment diversity: training environments span the support of relevant E dimensions; (A4) finite-sample convergence of intervention estimates — the causal token selection operator S_τ with threshold τ satisfies: the selected set S_τ(T) ⊇ T* with probability ≥ 1-δ, and the resulting policy π(a|S_τ(T)) achieves ε-invariance: max_{e,e'} |R(π,e) - R(π,e')| ≤ ε(N_env, M, τ), where ε decreases with the number of environments N_env and intervention samples M. **Failure modes (explicit):** (F1) Insufficient environment diversity violates A3, confounding causal and spurious features — same fundamental limitation as IRM (Rosenfeld et al., 2021). (F2) Non-linear entanglement of causal/spurious content within individual tokens makes token-level selection a coarse operator. (F3) Amortization gap between the learned scorer and true ACE. We provide analysis of each failure mode's impact and mitigation strategies.\n\n**Amortized Causal Scoring (ACS).** Rather than computing per-token ACE via O(N × K) individual interventions (N tokens × K environments), we train a lightweight causal scoring head attached to the frozen VLA backbone. Training data for the scorer is generated via *batch stochastic interventions*: for randomly sampled token subsets across LIBERO-Plus perturbation environments, we replace token embeddings with environment-marginal statistics and measure KL divergence in action distributions. A Shapley-value-inspired decomposition attributes group effects to individual tokens. The scorer (2-layer MLP, <1M parameters) learns to predict token-level causal effects from token embeddings in a single forward pass, amortizing the intervention cost. This is inspired by recent amortized causal estimation work (ACTIVA, arXiv 2503.01290).\n\n**Variance-Regularized Selection.** Instead of an IRM penalty (which fails in non-linear settings), we use V-REx-style variance regularization: the scoring head is trained to minimize action prediction loss while penalizing the *variance* of per-environment losses for the selected token subset. This provides distributional robustness without claiming strict invariance guarantees. The penalty weight is treated as a hyperparameter with explicit sensitivity analysis.\n\n**Architecture.** Frozen OpenVLA-OFT backbone (7B). The ACS head and a thin LoRA adaptation layer (~4M parameters total) are the only trainable components. At inference, the scorer assigns causal scores to all visual tokens in a single forward pass; tokens below threshold τ are pruned. This provides both robustness (by removing spuriously correlated tokens) and efficiency (by reducing the token count for the action decoder).\n\n**Evaluation.** Primary benchmark: LIBERO-Plus across all 7 perturbation dimensions. Primary metric: average success rate under distribution shift, targeting the current SOTA of 82.1% (SRPO). Baselines: (1) SRPO — current SOTA, RL-based; (2) FTM/FLA — simple affine adaptation (we reproduce on LIBERO-Plus since original paper only evaluates LIBERO viewpoint); (3) Causal-ACT — adapted to OpenVLA backbone (we implement token-level analog of their feature-masking approach); (4) AVA-VLA — active visual attention; (5) VLA-Pruner — attention-based pruning; (6) VLA-IAP — geometric/interaction pruning; (7) RobustVLA — heuristic robust optimization; (8) Random token pruning — critical control baseline per findings of arXiv 2502.11501; (9) LeaF-adapted — gradient-guided causal pruning adapted from NLP to VLA. Ablations: (a) amortized vs. exact ACE estimation accuracy; (b) variance penalty weight sensitivity; (c) pruning ratio sweep (10-90%); (d) per-perturbation-dimension analysis; (e) causal score interpretability analysis (do high-scoring tokens correspond to task-relevant regions?).\n\n**Key differentiations.** vs. Causal-ACT: token-level in 7B VLA transformers (not feature-level in ResNet+ACT); amortized scoring (not heuristic graph search); comprehensive LIBERO-Plus evaluation (not single ALOHA task). vs. FTM: interpretable per-token causal scores (not black-box affine transform); selective token removal for distractor/background robustness (not global recalibration). vs. LeaF: VLA action policies (not NLP reasoning); cross-environment invariance objective (not single-domain teacher distillation); formal SCM (not gradient heuristics). vs. VLA-Pruner/IAP: causal criteria with formal conditions (not attention/geometric heuristics that may underperform random per arXiv 2502.11501).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~700h A100 (80GB): ~300h for 20-25 LoRA fine-tuning runs with ACS head at ~15h each, ~200h for batch intervention data generation and amortized scorer training across LIBERO-Plus environments (substantially more than original 100h estimate — generating sufficient intervention data for N=256 tokens × 7 perturbation types × multiple severity levels requires systematic coverage), ~200h for baseline reproduction (FTM on LIBERO-Plus, Causal-ACT adaptation, 9 baselines total) and ablations",
      "gpu_utilization": "Low (~25-30%). GPUs sit idle while researchers write code, debug the causal scoring pipeline, analyze intervention results, and iterate on the variance penalty and Shapley decomposition.",
      "timeline": "4-6 months",
      "team": "1-2 researchers (one with causal inference/SCM background for theorem formalization and proof, one with VLA/robotics experience for implementation and evaluation)",
      "estimated_gpu_cost": "~$1,050 (700h × $1.50/hr A100 spot pricing, May 2026 market rate)"
    },
    "human_in_loop": {
      "gpu_hours": "~1000h A100 (80GB): agent explores ~35-45 training configurations more systematically, runs comprehensive ablations across all 7 perturbation dimensions, and evaluates all 9 baselines",
      "gpu_utilization": "Moderate (~50-60%). Agent queues experiments faster but pauses at approval gates for: amortized scorer architecture, Shapley decomposition strategy, variance penalty weight, theorem assumption validation.",
      "timeline": "2-4 months",
      "team": "1 researcher, ~45min/day check-in for approving experiment plans, reviewing causal score visualizations, and validating theoretical claims",
      "claude_api_cost": "$400-600 (4000-6000 conversation turns for experiment design, code generation, theorem checking, result analysis)",
      "estimated_gpu_cost": "~$1,500 (1000h × $1.50/hr)",
      "risk_note": "Amortized scorer design requires careful validation — human judgment is critical to verify that the scorer's predictions correlate with ground-truth ACE (computed exactly on a small validation set). Theorem formalization needs human review by someone with causal inference expertise."
    },
    "auto_research": {
      "gpu_hours": "~2000h A100 (80GB): agent runs 100-120 experiment configurations including aggressive sweeps for variance penalty, pruning ratios, Shapley approximation methods, scorer architectures, plus all baseline reproductions and failed exploration runs",
      "gpu_utilization": "High (~90%+). Agent queues next experiment immediately upon completion. Continuous 24/7 execution.",
      "timeline": "3-5 weeks with 4-8 concurrent A100s; as few as 8-10 days with 16 concurrent GPUs",
      "team": "0 (initial setup: configure LIBERO-Plus environments, OpenVLA-OFT checkpoint, define intervention distribution and Shapley sampling strategy)",
      "claude_api_cost": "$600-1000 (6000-10000 turns for autonomous experiment design, debugging, and paper drafting)",
      "estimated_gpu_cost": "~$3,000 (2000h × $1.50/hr)",
      "speed_bottleneck": "Number of concurrent A100 GPU instances. Secondary: intervention data generation is I/O-intensive (requires rendering perturbation environments).",
      "risk_note": "Without human gates, agent may over-explore suboptimal Shapley approximations or scorer architectures. The theorem formalization cannot be fully automated — agent-generated proofs require expert verification. Risk mitigation: pre-define structured search space with early stopping on scorer validation metrics."
    }
  },
  "target_venues": [
    "CoRL 2026 (deadline: May 29, 2026 — extremely tight given revision scope, stretch goal only)",
    "AAAI 2027 (deadline: ~August 1, 2026 — primary target, sufficient time for theoretical development and experiments)",
    "ICLR 2027 (deadline: ~October 2026 — strong target, allows comprehensive evaluation)",
    "ICRA 2027 (deadline: ~September 2026 — robotics venue, good fit)"
  ],
  "level": "top-tier",
  "key_references": [
    "Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations [Causal-ACT] (arXiv 2507.22380, July 2025)",
    "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling [FTM/FLA] (arXiv 2512.02902, Dec 2025)",
    "Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning [LeaF] (NeurIPS 2025, arXiv 2506.07851)",
    "Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation (CoRL 2025, arXiv 2508.06426)",
    "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? (ACL Findings 2025, arXiv 2502.11501)",
    "The Risks of Invariant Risk Minimization (ICLR 2021, arXiv 2010.05761)",
    "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models (arXiv 2511.15605)",
    "AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960)",
    "ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder (arXiv 2503.01290)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626)",
    "Invariant Causal Imitation Learning for Generalizable Policies [ICIL] (NeurIPS 2021)",
    "Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv 2604.19683, April 2026) — evaluated on LIBERO/RLBench only, NOT LIBERO-Plus",
    "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations [RobustVLA] (ICLR 2026, arXiv 2510.00037)",
    "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient VLA Inference (arXiv 2511.16449)",
    "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for VLA Models (arXiv 2603.22991, March 2026)",
    "Learning Invariant Causal Mechanism from Vision-Language Models [CLIP-ICM] (ICML 2025, arXiv 2405.15289)",
    "OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport (arXiv 2602.20205)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)"
  ],
  "description": "VLA models suffer catastrophic failures under visual distribution shifts due to spurious correlations, yet recent work reveals that (a) many token pruning methods underperform random selection (arXiv 2502.11501), exposing the need for principled selection criteria, and (b) simple affine recalibration (FTM) can recover surprising robustness, but without interpretability or formal grounding. We propose Causal Token Selection (CaTS) v2, bridging three disconnected threads: VLA token pruning (VLA-Pruner, VLA-IAP), causal intervention for imitation learning (Causal-ACT, ICIL), and causal attention distillation (LeaF). CaTS defines a formal SCM over the VLA token-action pipeline, introduces the *spatial locality of causal features* assumption (task-relevant information is spatially concentrated in token subsets while spurious features are distributed), and proves conditional invariance under four explicit assumptions — with documented failure modes when assumptions are violated, avoiding the overclaiming that plagues IRM-based approaches (Rosenfeld et al., 2021). For scalability, CaTS uses Amortized Causal Scoring: a lightweight head (<1M params) trained on batch stochastic interventions with Shapley-value decomposition, predicting per-token causal effects in a single forward pass rather than requiring O(N×K) individual interventions. A V-REx-style variance penalty replaces the problematic IRM objective for distributional robustness. Key differentiations: vs. Causal-ACT (arXiv 2507.22380) — token-level in 7B VLA transformers rather than feature-level in ResNet+ACT, amortized scoring rather than heuristic graph search, comprehensive LIBERO-Plus evaluation rather than single ALOHA task; vs. FTM — interpretable causal scores per token rather than black-box affine transform, selective token removal for distractor robustness; vs. LeaF — VLA action policies rather than NLP, cross-environment invariance rather than single-domain distillation. Evaluated on LIBERO-Plus across all 7 perturbation dimensions against 9 baselines including SRPO (82.1% SOTA), FTM (reproduced on LIBERO-Plus), Causal-ACT (adapted to VLA backbone), AVA-VLA, and random pruning. All building blocks are open-source. Primary targets: AAAI 2027 and ICLR 2027.",
  "project_name": "causal_token_sel_vla",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL MISSING WORK: 'Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations' (arXiv 2507.22380, July 2025) applies causal intervention to resolve causal confusion in robotic imitation learning—directly overlapping with CaTS's core motivation and approach. This paper was NOT cited.", "CRITICAL MISSING WORK: 'VLA Models Are More Generalizable Than You Think' (arXiv 2512.02902) shows Feature Token Modulation (FTM) achieves 87.1% on LIBERO viewpoint with only 4K parameters—a much simpler and cheaper alternative that undermines CaTS's complexity justification. Must be included as a baseline.", "MISSING WORK: 'Learning to Focus: Causal Attention Distillation (LeaF)' (NeurIPS 2025, arXiv 2506.07851) uses causal intervention at the token level for pruning confounding tokens. While targeting NLP, the method is directly analogous and must be discussed.", "MISSING WORK: 'Shortcut Learning in Generalist Robot Policies' (CoRL 2025, arXiv 2508.06426) addresses the same shortcut/spurious correlation problem through dataset design—a competing solution approach.", "MISSING WORK: 'Token Pruning in MLLMs: Are We Solving the Right Problem?' (arXiv 2502.11501, ACL Findings 2025) raises fundamental questions about attention-based token pruning, finding some methods underperform random selection. Must be addressed.", "OVERCLAIMED THEORY: 'Provable invariance guarantees' via IRM-style penalty is not justified. IRM fails catastrophically in non-linear settings (Rosenfeld et al., ICLR 2021), requires environment coverage that LIBERO-Plus may not provide, and the IRMv1 penalty doesn't always capture invariance correctly. These failure modes must be acknowledged and addressed.", "INVALID BASELINE: Mask World Model (arXiv 2604.19683) evaluates on LIBERO and RLBench, NOT LIBERO-Plus. Listing it as a LIBERO-Plus baseline comparison is misleading.", "INSUFFICIENT THEORETICAL DEPTH: The user specifically requested '多从理论角度分析为何能增强' (theoretical analysis of WHY token pruning enhances generalization). The idea merely invokes do-calculus and IRM without formal results—no theorems, no proofs, no explicit assumptions. The theoretical contribution is the supposed differentiator from VLA-Pruner/IAP but is undeveloped.", "ACE ESTIMATION SCALABILITY: Estimating per-token ACE by intervening (replacing embeddings with marginal statistics) across multiple environments is combinatorially expensive. For 256+ tokens × multiple perturbation types × sufficient samples for stable KL-divergence estimates, the 100h GPU estimate for 'causal effect estimation sweeps' likely significantly underestimates the real cost.", "STALE SOTA TARGET: The 79.6% LIBERO-Plus SOTA may already be surpassed by FTM-style approaches or Mask World Model adaptations. The generator should verify this is still current."]
Feedback: The core idea of using causal criteria for VLA token selection has merit, but significant revisions are needed:

1. **Add missing related work urgently**: (a) arXiv 2507.22380 on causal confusion in imitation learning—this is your closest competitor and must be discussed with clear differentiation. (b) arXiv 2512.02902 (FTM)—this simple 4K-parameter method achieves strong robustness and must be a baseline. If CaTS cannot outperform FTM, the entire approach is questionable. (c) LeaF (NeurIPS 2025)—the NLP-domain analog of your idea. (d) 'Shortcut Learning in Generalist Robot Policies' (CoRL 2025). (e) arXiv 2502.11501 on fundamental problems with token pruning.

2. **Develop the theoretical framework seriously or drop the 'provable guarantees' claim**: The user's core requirement is theoretical analysis. You need: (a) A formal SCM for the VLA token → action pipeline with explicit assumptions. (b) A theorem stating under what conditions causal token selection yields invariant policies, with at least a proof sketch. (c) Explicit discussion of when the guarantees break (IRM failure modes, insufficient environment diversity, non-linear interactions). Without this, the paper is just another engineering method paper, which doesn't match the user's request.

3. **Fix the Mask World Model baseline**: Either demonstrate MWM on LIBERO-Plus yourself or remove it from the comparison table.

4. **Address ACE estimation scalability**: Provide a realistic computational analysis of per-token intervention costs. Consider approximations (e.g., batch interventions, amortized estimation) and include these in the method.

5. **Strengthen differentiation from arXiv 2507.22380**: That paper already does causal intervention in imitation learning. Your contribution must be clearly at the token level within transformer VLA architectures, not just causal intervention in general.


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
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "85460ed4-0180-44b2-a0ce-250e0705e13f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T04:35:04.074Z_

```json
{
  "parentUuid": "85460ed4-0180-44b2-a0ce-250e0705e13f",
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
  "uuid": "74e32513-cc1c-4eba-8c04-66e69750a116",
  "timestamp": "2026-05-13T04:35:04.074Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T04:35:04.075Z_

```json
{
  "parentUuid": "74e32513-cc1c-4eba-8c04-66e69750a116",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ed48b2cb-78ff-4f64-b58d-9cc86b802689",
  "timestamp": "2026-05-13T04:35:04.075Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
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
  "leafUuid": "ed48b2cb-78ff-4f64-b58d-9cc86b802689",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Assistant

_source line 8 · 2026-05-13T04:35:13.184Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a thorough adversarial review of a research idea about "Causal Token Selection for Invariant VLA Policies via Amortized Interventional Scoring" (CaTS v2). This is round 2 of review, and the generator has revised based on round 1 feedback.

Let me first understand what the user originally asked for: **VLA中的token裁剪/增强能否提升VLA模型的泛化性（多从理论角度分析为何能增强）** - Whether token pruning/augmentation in VLA can improve VLA model generalization, with emphasis on theoretical analysis of why it enhances generalization.


Now I'm going to systematically verify the core claims by checking whether the cited papers actually exist, validating the SOTA benchmarks they reference, and identifying any gaps in their literature coverage. I'll also need to assess the technical feasibility and novelty of their approach, plus look for any competing work they might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed48b2cb-78ff-4f64-b58d-9cc86b802689",
  "isSidechain": false,
  "requestId": "req_011CaywodMqPe5b6oy28kR6y",
  "type": "assistant",
  "uuid": "85f0b2e6-9d4f-4590-ad27-edcd17b93687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GALoC8tnZDQxhUkJdaiwWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15625,
      "cache_read_input_tokens": 11841,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15625
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

_source line 9 · 2026-05-13T04:35:13.212Z_

I'll conduct a thorough independent review of this revised idea. Let me start with parallel searches to verify claims, check for missing work, and assess the current SOTA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85f0b2e6-9d4f-4590-ad27-edcd17b93687",
  "isSidechain": false,
  "requestId": "req_011CaywodMqPe5b6oy28kR6y",
  "type": "assistant",
  "uuid": "cbd5ef76-b721-4d8d-b262-b6258633c6ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GALoC8tnZDQxhUkJdaiwWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15625,
      "cache_read_input_tokens": 11841,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15625
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

_source line 10 · 2026-05-13T04:35:13.214Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qtu6SH3fGT3N7BdFUJggnz`</summary>

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
  "parentUuid": "cbd5ef76-b721-4d8d-b262-b6258633c6ec",
  "isSidechain": false,
  "requestId": "req_011CaywodMqPe5b6oy28kR6y",
  "type": "assistant",
  "uuid": "a36c2486-7868-465b-813e-aa036eab9bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GALoC8tnZDQxhUkJdaiwWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15625,
      "cache_read_input_tokens": 11841,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15625
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

_source line 11 · 2026-05-13T04:35:13.221Z_

<details><summary>↩ Tool result · `toolu_01Qtu6SH3fGT3N7BdFUJggnz`</summary>

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
  "parentUuid": "a36c2486-7868-465b-813e-aa036eab9bcd",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "a9aaa243-e03e-42d6-a8cb-4a39060c0274",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "a36c2486-7868-465b-813e-aa036eab9bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T04:35:16.074Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start with multiple parallel searches to verify the key claims and find potentially missing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9aaa243-e03e-42d6-a8cb-4a39060c0274",
  "isSidechain": false,
  "requestId": "req_011CaywpHbip6HPWqYTF43g5",
  "type": "assistant",
  "uuid": "fc20e1e2-4b23-494d-aa68-2554076429a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXMD7YM1SXYdnQhjKSUhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 27466,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 27466,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 13 · 2026-05-13T04:35:16.733Z_

Starting my independent verification. Let me search for key claims, competing work, and current SOTA in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc20e1e2-4b23-494d-aa68-2554076429a5",
  "isSidechain": false,
  "requestId": "req_011CaywpHbip6HPWqYTF43g5",
  "type": "assistant",
  "uuid": "6983ade7-69c3-4bee-92bc-7b298627047f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXMD7YM1SXYdnQhjKSUhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 27466,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 27466,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 14 · 2026-05-13T04:35:17.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014iZ4YsFszLGvAT4RRqTJut`</summary>

```json
{
  "query": "LIBERO-Plus benchmark VLA robustness SOTA 2026 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6983ade7-69c3-4bee-92bc-7b298627047f",
  "isSidechain": false,
  "requestId": "req_011CaywpHbip6HPWqYTF43g5",
  "type": "assistant",
  "uuid": "9d6159eb-9410-4665-81bc-98d7dd832125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXMD7YM1SXYdnQhjKSUhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 27466,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 27466,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 15 · 2026-05-13T04:35:25.580Z_

<details><summary>↩ Tool result · `toolu_014iZ4YsFszLGvAT4RRqTJut`</summary>

```text
Web search results for query: "LIBERO-Plus benchmark VLA robustness SOTA 2026 success rate"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"VLA & Dexterous Manipulation SOTA Leaderboard","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"}]

Based on the search results, here's what I found about LIBERO-Plus benchmark, VLA robustness, and SOTA success rates:

## LIBERO-Plus Benchmark Overview

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across the key vulnerability dimensions identified in robustness studies. The benchmark contains 10,030 tasks spanning seven perturbation dimensions.

## VLA Robustness and Success Rates

The research reveals a significant gap between reported SOTA success rates and actual robustness:

- VLA models report impressive success rates exceeding 95% on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness.

- Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## Key Findings

The benchmark provides detailed success rates across seven perturbation categories (Camera, Robot Initialization, Language Instruction, Lighting, Background, Sensor Noise, and Scene Layout) for various VLA methods.

Current VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.

LIBERO-PRO and LIBERO-Plus show that without systematic robustness evaluation, benchmark success rates are misleading.

The results highlight that while conventional LIBERO benchmarks show >95% success under clean conditions, LIBERO-Plus reveals significant fragility when models are subjected to realistic perturbations and distribution shifts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d6159eb-9410-4665-81bc-98d7dd832125",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "3f50b85d-be12-4cff-bd53-3df017605096",
  "toolUseResult": {
    "query": "LIBERO-Plus benchmark VLA robustness SOTA 2026 success rate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FSvGFgZFsVGK16NqAkACUj",
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
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "VLA & Dexterous Manipulation SOTA Leaderboard",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, here's what I found about LIBERO-Plus benchmark, VLA robustness, and SOTA success rates:\n\n## LIBERO-Plus Benchmark Overview\n\nLIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across the key vulnerability dimensions identified in robustness studies. The benchmark contains 10,030 tasks spanning seven perturbation dimensions.\n\n## VLA Robustness and Success Rates\n\nThe research reveals a significant gap between reported SOTA success rates and actual robustness:\n\n- VLA models report impressive success rates exceeding 95% on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness.\n\n- Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n## Key Findings\n\nThe benchmark provides detailed success rates across seven perturbation categories (Camera, Robot Initialization, Language Instruction, Lighting, Background, Sensor Noise, and Scene Layout) for various VLA methods.\n\nCurrent VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.\n\nLIBERO-PRO and LIBERO-Plus show that without systematic robustness evaluation, benchmark success rates are misleading.\n\nThe results highlight that while conventional LIBERO benchmarks show >95% success under clean conditions, LIBERO-Plus reveals significant fragility when models are subjected to realistic perturbations and distribution shifts."
    ],
    "durationSeconds": 8.478017822
  },
  "sourceToolAssistantUUID": "9d6159eb-9410-4665-81bc-98d7dd832125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T04:35:29.062Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D8Q8bdN4qw3LwuxL4rd5BK`</summary>

```json
{
  "query": "SRPO self-referential policy optimization VLA arXiv 2511.15605 LIBERO-Plus results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f50b85d-be12-4cff-bd53-3df017605096",
  "isSidechain": false,
  "requestId": "req_011CaywqCHkvGXrdF8ymqVvk",
  "type": "assistant",
  "uuid": "a5bca9a2-76ca-41ae-bbc0-a97cc6a410a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ave9cjmRx89zaJdSJb3Bq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 28841,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 28841,
          "cache_creation_input_tokens": 1017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1017
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

_source line 17 · 2026-05-13T04:35:36.189Z_

<details><summary>↩ Tool result · `toolu_01D8Q8bdN4qw3LwuxL4rd5BK`</summary>

```text
Web search results for query: "SRPO self-referential policy optimization VLA arXiv 2511.15605 LIBERO-Plus results"

Links: [{"title":"[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15605v2"},{"title":"Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://huggingface.co/papers/2511.15605"},{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.15605v1"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"},{"title":"[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[2506.01713v1] SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning","url":"https://arxiv.org/abs/2506.01713v1"}]

Based on the search results, I found detailed information about SRPO (Self-Referential Policy Optimization) and its LIBERO-Plus results:

## Overview

SRPO is a novel VLA-RL framework that eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference. A core innovation is the use of latent world representations to measure behavioral progress robustly, utilizing compressed, transferable encodings from a world model's latent space that naturally capture progress patterns across environments.

## LIBERO-Plus Results

SRPO achieves a 167% performance improvement on the LIBERO-Plus benchmark. On LIBERO-Plus, SRPO demonstrates substantial robustness, achieving a 167% performance improvement over the one-shot SFT baseline and surpassing even full-shot SFT models in perturbed environments.

## LIBERO Benchmark Results

Starting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision.

The paper demonstrates that SRPO's approach to reward shaping is significantly more effective than traditional sparse reward methods, making it highly efficient for vision-language-action model training in robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5bca9a2-76ca-41ae-bbc0-a97cc6a410a1",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "1aef9d64-639c-4b49-84a0-0dadd88fc923",
  "toolUseResult": {
    "query": "SRPO self-referential policy optimization VLA arXiv 2511.15605 LIBERO-Plus results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ji9Gtfdt4ys2m7MufPeMxE",
        "content": [
          {
            "title": "[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2511.15605"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.15605v2"
          },
          {
            "title": "Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2511.15605"
          },
          {
            "title": "[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2511.15605v1"
          },
          {
            "title": "SRPO Code Implementation Explained — siiRL documentation",
            "url": "https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF",
            "url": "https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"
          },
          {
            "title": "[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"
          },
          {
            "title": "LIBERO-plus/README.md at main · sylvestf/LIBERO-plus",
            "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"
          },
          {
            "title": "[2506.01713v1] SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning",
            "url": "https://arxiv.org/abs/2506.01713v1"
          }
        ]
      },
      "Based on the search results, I found detailed information about SRPO (Self-Referential Policy Optimization) and its LIBERO-Plus results:\n\n## Overview\n\nSRPO is a novel VLA-RL framework that eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference. A core innovation is the use of latent world representations to measure behavioral progress robustly, utilizing compressed, transferable encodings from a world model's latent space that naturally capture progress patterns across environments.\n\n## LIBERO-Plus Results\n\nSRPO achieves a 167% performance improvement on the LIBERO-Plus benchmark. On LIBERO-Plus, SRPO demonstrates substantial robustness, achieving a 167% performance improvement over the one-shot SFT baseline and surpassing even full-shot SFT models in perturbed environments.\n\n## LIBERO Benchmark Results\n\nStarting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision.\n\nThe paper demonstrates that SRPO's approach to reward shaping is significantly more effective than traditional sparse reward methods, making it highly efficient for vision-language-action model training in robotic manipulation tasks."
    ],
    "durationSeconds": 7.120340483999997
  },
  "sourceToolAssistantUUID": "a5bca9a2-76ca-41ae-bbc0-a97cc6a410a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T04:35:38.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UNZHoWhKKW2tiPnHqgb3N1`</summary>

```json
{
  "query": "Causal-ACT causal confusion imitation learning arXiv 2507.22380"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aef9d64-639c-4b49-84a0-0dadd88fc923",
  "isSidechain": false,
  "requestId": "req_011CaywqyemnGP6URPbgsw7H",
  "type": "assistant",
  "uuid": "ceefd05c-3c3c-4663-923e-b01aed895351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRugxgLnx3pVxFhfwgZuVb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 999,
      "cache_read_input_tokens": 29858,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 999,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 29858,
          "cache_creation_input_tokens": 999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 999
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

_source line 19 · 2026-05-13T04:35:46.023Z_

<details><summary>↩ Tool result · `toolu_01UNZHoWhKKW2tiPnHqgb3N1`</summary>

```text
Web search results for query: "Causal-ACT causal confusion imitation learning arXiv 2507.22380"

Links: [{"title":"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations","url":"https://arxiv.org/html/2507.22380"},{"title":"[2507.22380] Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations","url":"https://arxiv.org/abs/2507.22380"},{"title":"Improving Generalization Ability of Robotic Imitation Learning by Resolving","url":"https://arxiv.org/pdf/2507.22380"},{"title":"[2507.22380v1] Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations","url":"https://arxiv.org/abs/2507.22380v1"},{"title":"[1905.11979] Causal Confusion in Imitation Learning","url":"https://arxiv.org/abs/1905.11979"},{"title":"Causal confusion in imitation learning | Proceedings of the 33rd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3454287.3455336"},{"title":"Causal Confusion in Imitation Learning","url":"https://arxiv.org/pdf/1905.11979"},{"title":"Causal Imitation Learning Under Measurement Error and Distribution Shift","url":"https://arxiv.org/html/2601.22206"},{"title":"[PDF] Causal Confusion in Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Causal-Confusion-in-Imitation-Learning-Haan-Jayaraman/3810299e97558e2b51459e702f02344a4034af43"},{"title":"Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding","url":"https://arxiv.org/html/2502.07656"}]

I found the paper! Here's what I found about Causal-ACT (arXiv 2507.22380):

## Overview

Causal-ACT is an extension to imitation learning (IL) models that integrates causal structure learning into a transformer-based policy model.

## Problem Addressed

Current techniques in imitation learning can suffer from poor generalization, limiting performance even under relatively minor domain shifts. The paper proposes to explicitly learn the causal relationship between observation components and expert actions to avoid confusion caused by observations that are not relevant to the target task.

## Key Features

The method avoids the reliance on disentangled representations and learns a causal structure model from an off-the-shelf convolutional encoder, such as ResNet-18. The method jointly optimizes over a space of candidate graphs and intervenes to find the appropriate structure that learns the task-relevant features and avoids causal confusion, allowing the policy to focus on what matters and improves its robustness to domain shifts at test time.

## Evaluation

The approach is demonstrated using a simulation of the ALOHA bimanual robot arms in Mujoco, and results show that the Causal-ACT method substantially outperforms the traditional ACT method under distribution shift conditions.

The paper was submitted on July 30, 2025, by authors including Yifei Chen, Yuzhe Zhang, Giovanni D'urso, Nicholas Lawrance, and Brendan Tidd.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceefd05c-3c3c-4663-923e-b01aed895351",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "e761f219-524c-4e17-9ee5-95e893379dfa",
  "toolUseResult": {
    "query": "Causal-ACT causal confusion imitation learning arXiv 2507.22380",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XURRkcmsXjGBTX7CqAqMy2",
        "content": [
          {
            "title": "Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations",
            "url": "https://arxiv.org/html/2507.22380"
          },
          {
            "title": "[2507.22380] Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations",
            "url": "https://arxiv.org/abs/2507.22380"
          },
          {
            "title": "Improving Generalization Ability of Robotic Imitation Learning by Resolving",
            "url": "https://arxiv.org/pdf/2507.22380"
          },
          {
            "title": "[2507.22380v1] Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations",
            "url": "https://arxiv.org/abs/2507.22380v1"
          },
          {
            "title": "[1905.11979] Causal Confusion in Imitation Learning",
            "url": "https://arxiv.org/abs/1905.11979"
          },
          {
            "title": "Causal confusion in imitation learning | Proceedings of the 33rd International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3454287.3455336"
          },
          {
            "title": "Causal Confusion in Imitation Learning",
            "url": "https://arxiv.org/pdf/1905.11979"
          },
          {
            "title": "Causal Imitation Learning Under Measurement Error and Distribution Shift",
            "url": "https://arxiv.org/html/2601.22206"
          },
          {
            "title": "[PDF] Causal Confusion in Imitation Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Causal-Confusion-in-Imitation-Learning-Haan-Jayaraman/3810299e97558e2b51459e702f02344a4034af43"
          },
          {
            "title": "Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding",
            "url": "https://arxiv.org/html/2502.07656"
          }
        ]
      },
      "I found the paper! Here's what I found about Causal-ACT (arXiv 2507.22380):\n\n## Overview\n\nCausal-ACT is an extension to imitation learning (IL) models that integrates causal structure learning into a transformer-based policy model.\n\n## Problem Addressed\n\nCurrent techniques in imitation learning can suffer from poor generalization, limiting performance even under relatively minor domain shifts. The paper proposes to explicitly learn the causal relationship between observation components and expert actions to avoid confusion caused by observations that are not relevant to the target task.\n\n## Key Features\n\nThe method avoids the reliance on disentangled representations and learns a causal structure model from an off-the-shelf convolutional encoder, such as ResNet-18. The method jointly optimizes over a space of candidate graphs and intervenes to find the appropriate structure that learns the task-relevant features and avoids causal confusion, allowing the policy to focus on what matters and improves its robustness to domain shifts at test time.\n\n## Evaluation\n\nThe approach is demonstrated using a simulation of the ALOHA bimanual robot arms in Mujoco, and results show that the Causal-ACT method substantially outperforms the traditional ACT method under distribution shift conditions.\n\nThe paper was submitted on July 30, 2025, by authors including Yifei Chen, Yuzhe Zhang, Giovanni D'urso, Nicholas Lawrance, and Brendan Tidd."
    ],
    "durationSeconds": 7.396404401
  },
  "sourceToolAssistantUUID": "ceefd05c-3c3c-4663-923e-b01aed895351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
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
  "leafUuid": "e761f219-524c-4e17-9ee5-95e893379dfa",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 22 · 2026-05-13T04:35:49.796Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXAMdCNjpNSghzHHDkc2Z1`</summary>

```json
{
  "query": "Feature Token Modulation FTM VLA generalization arXiv 2512.02902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e761f219-524c-4e17-9ee5-95e893379dfa",
  "isSidechain": false,
  "requestId": "req_011Caywri1TzQYCYEmZFDDM2",
  "type": "assistant",
  "uuid": "7cc2d9b3-8382-4f93-a18d-1000aa388692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HedMfAguK5KM2wiKvw5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 30857,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 30857,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
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

_source line 23 · 2026-05-13T04:35:56.593Z_

<details><summary>↩ Tool result · `toolu_01VXAMdCNjpNSghzHHDkc2Z1`</summary>

```text
Web search results for query: "Feature Token Modulation FTM VLA generalization arXiv 2512.02902"

Links: [{"title":"[2512.02902] VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/abs/2512.02902"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"awesome-daily-AI-arxiv/hot_topic/Embodied_AI.md at main · Tavish9/awesome-daily-AI-arxiv","url":"https://github.com/Tavish9/awesome-daily-AI-arxiv/blob/main/hot_topic/Embodied_AI.md"},{"title":"Feature Token Modulation (FTM)","url":"https://www.emergentmind.com/topics/feature-token-modulation-ftm"},{"title":"[2512.04952] FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization","url":"https://arxiv.org/abs/2512.04952"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257v1"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Resolving Token-Space Gradient Conflicts: Token Space Manipulation for Transformer-Based Multi-Task Learning","url":"https://arxiv.org/html/2507.07485"},{"title":"FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models","url":"https://arxiv.org/html/2511.16233"}]

Based on the search results, here's information about the paper arXiv 2512.02902:

## Paper Overview

The paper is titled "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling" and addresses how Vision-Language-Action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations.

## Feature Token Modulation (FTM)

Feature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. The research shows that the brittleness of VLA models primarily arises from misalignment in Spatial Modeling rather than Physical Modeling, and proposes a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates.

## Performance and Generalization

Building on FTM, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters—matching LoRA-scale finetuning at far lower cost. Across the Libero-V benchmarks, the framework achieves state-of-the-art generalization under novel camera viewpoints and diverse visual perturbations, while being up to 99× more parameter-efficient than LoRA fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cc2d9b3-8382-4f93-a18d-1000aa388692",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "d6ea6266-c93a-4ba3-af87-37cf2a5db289",
  "toolUseResult": {
    "query": "Feature Token Modulation FTM VLA generalization arXiv 2512.02902",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VpLLXLnMizxr9dAGypKoyE",
        "content": [
          {
            "title": "[2512.02902] VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/abs/2512.02902"
          },
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902"
          },
          {
            "title": "awesome-daily-AI-arxiv/hot_topic/Embodied_AI.md at main · Tavish9/awesome-daily-AI-arxiv",
            "url": "https://github.com/Tavish9/awesome-daily-AI-arxiv/blob/main/hot_topic/Embodied_AI.md"
          },
          {
            "title": "Feature Token Modulation (FTM)",
            "url": "https://www.emergentmind.com/topics/feature-token-modulation-ftm"
          },
          {
            "title": "[2512.04952] FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization",
            "url": "https://arxiv.org/abs/2512.04952"
          },
          {
            "title": "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.19257v1"
          },
          {
            "title": "Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2512.09927"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "Resolving Token-Space Gradient Conflicts: Token Space Manipulation for Transformer-Based Multi-Task Learning",
            "url": "https://arxiv.org/html/2507.07485"
          },
          {
            "title": "FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models",
            "url": "https://arxiv.org/html/2511.16233"
          }
        ]
      },
      "Based on the search results, here's information about the paper arXiv 2512.02902:\n\n## Paper Overview\n\nThe paper is titled \"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling\" and addresses how Vision-Language-Action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations.\n\n## Feature Token Modulation (FTM)\n\nFeature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. The research shows that the brittleness of VLA models primarily arises from misalignment in Spatial Modeling rather than Physical Modeling, and proposes a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates.\n\n## Performance and Generalization\n\nBuilding on FTM, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters—matching LoRA-scale finetuning at far lower cost. Across the Libero-V benchmarks, the framework achieves state-of-the-art generalization under novel camera viewpoints and diverse visual perturbations, while being up to 99× more parameter-efficient than LoRA fine-tuning."
    ],
    "durationSeconds": 6.791452556000004
  },
  "sourceToolAssistantUUID": "7cc2d9b3-8382-4f93-a18d-1000aa388692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T04:35:59.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TpJeqrkaAHyqDd3SmPRTSw`</summary>

```json
{
  "query": "LeaF causal attention distillation token pruning NeurIPS 2025 arXiv 2506.07851"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ea6266-c93a-4ba3-af87-37cf2a5db289",
  "isSidechain": false,
  "requestId": "req_011CaywsUwBatLUkbpCnTHCL",
  "type": "assistant",
  "uuid": "3945dfc0-0a04-49e3-87f6-1fcfbb43235b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbzA2dQPEqUsfJAR8RrZqy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 31808,
      "output_tokens": 80,
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
          "output_tokens": 80,
          "cache_read_input_tokens": 31808,
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

_source line 25 · 2026-05-13T04:36:05.787Z_

<details><summary>↩ Tool result · `toolu_01TpJeqrkaAHyqDd3SmPRTSw`</summary>

```text
Web search results for query: "LeaF causal attention distillation token pruning NeurIPS 2025 arXiv 2506.07851"

Links: [{"title":"[2506.07851] Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning","url":"https://arxiv.org/abs/2506.07851"},{"title":"Causal Attention Distillation via Gradient-Guided Token ...","url":"https://arxiv.org/pdf/2506.07851"},{"title":"Causal Attention Distillation via Gradient-Guided Token ...","url":"https://www.arxiv.org/pdf/2506.07851v2"},{"title":"(PDF) Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning","url":"https://www.researchgate.net/publication/392530410_Learning_to_Focus_Causal_Attention_Distillation_via_Gradient-Guided_Token_Pruning"},{"title":"0 Learning to Focus: Causal Attention Distillation via Gradient-","url":"https://neurips.cc/media/neurips-2025/Slides/115296_xoXnMvL.pdf"},{"title":"GitHub - RUCBM/LeaF · GitHub","url":"https://github.com/RUCBM/LeaF"},{"title":"Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning","url":"https://arxiv.org/html/2506.07851v1"},{"title":"NeurIPS Poster Learning to Focus: Causal Attention Distillation via Gradient‐Guided Token Pruning","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115296"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=4100&show=2000"},{"title":"Learning to Focus: Causal Attention Distillation via Gradient‐Guided Token Pruning | OpenReview","url":"https://openreview.net/forum?id=wpkmEV57YT"}]

Based on the search results, I found comprehensive information about the paper you're interested in. Here's a summary:

## Learning to Focus (LeaF): Causal Attention Distillation via Gradient-Guided Token Pruning

The paper was accepted to NeurIPS 2025 and is identified by arXiv identifier 2506.07851.

### Problem Statement
Large language models have demonstrated significant improvements in contextual understanding, but their ability to attend to truly critical information during long-context reasoning and generation still falls behind the pace. The research reveals that certain distracting patterns can misdirect the model's attention during inference, and this is attributed to spurious correlations in the training data.

### Proposed Solution
The paper introduces a two-stage framework called Learning to Focus (LeaF) leveraging intervention-based inference to disentangle confounding factors.

**Stage 1 - Confounding Token Detection:** LeaF employs gradient-based comparisons with an advanced teacher to automatically identify confounding tokens based on causal relationships in the training corpus.

**Stage 2 - Causal Attention Distillation:** In the second stage, it prunes these tokens during distillation to enact intervention, aligning the student's attention with the teacher's focus distribution on truly critical context tokens.

### Results
Experimental results demonstrate that LeaF achieves absolute improvements in various mathematical reasoning, code generation and multi-hop question answering benchmarks while effectively suppressing attention to confounding tokens during inference.

The code and resources are available at the [GitHub repository](https://github.com/RUCBM/LeaF/).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3945dfc0-0a04-49e3-87f6-1fcfbb43235b",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "45754758-92e4-4363-840b-c9264caa62ee",
  "toolUseResult": {
    "query": "LeaF causal attention distillation token pruning NeurIPS 2025 arXiv 2506.07851",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EfsSpBU9NwUkCifMWSkhSt",
        "content": [
          {
            "title": "[2506.07851] Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning",
            "url": "https://arxiv.org/abs/2506.07851"
          },
          {
            "title": "Causal Attention Distillation via Gradient-Guided Token ...",
            "url": "https://arxiv.org/pdf/2506.07851"
          },
          {
            "title": "Causal Attention Distillation via Gradient-Guided Token ...",
            "url": "https://www.arxiv.org/pdf/2506.07851v2"
          },
          {
            "title": "(PDF) Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning",
            "url": "https://www.researchgate.net/publication/392530410_Learning_to_Focus_Causal_Attention_Distillation_via_Gradient-Guided_Token_Pruning"
          },
          {
            "title": "0 Learning to Focus: Causal Attention Distillation via Gradient-",
            "url": "https://neurips.cc/media/neurips-2025/Slides/115296_xoXnMvL.pdf"
          },
          {
            "title": "GitHub - RUCBM/LeaF · GitHub",
            "url": "https://github.com/RUCBM/LeaF"
          },
          {
            "title": "Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning",
            "url": "https://arxiv.org/html/2506.07851v1"
          },
          {
            "title": "NeurIPS Poster Learning to Focus: Causal Attention Distillation via Gradient‐Guided Token Pruning",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/115296"
          },
          {
            "title": "Computer Science Jun 2025",
            "url": "https://arxiv.org/list/cs/2025-06?skip=4100&show=2000"
          },
          {
            "title": "Learning to Focus: Causal Attention Distillation via Gradient‐Guided Token Pruning | OpenReview",
            "url": "https://openreview.net/forum?id=wpkmEV57YT"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're interested in. Here's a summary:\n\n## Learning to Focus (LeaF): Causal Attention Distillation via Gradient-Guided Token Pruning\n\nThe paper was accepted to NeurIPS 2025 and is identified by arXiv identifier 2506.07851.\n\n### Problem Statement\nLarge language models have demonstrated significant improvements in contextual understanding, but their ability to attend to truly critical information during long-context reasoning and generation still falls behind the pace. The research reveals that certain distracting patterns can misdirect the model's attention during inference, and this is attributed to spurious correlations in the training data.\n\n### Proposed Solution\nThe paper introduces a two-stage framework called Learning to Focus (LeaF) leveraging intervention-based inference to disentangle confounding factors.\n\n**Stage 1 - Confounding Token Detection:** LeaF employs gradient-based comparisons with an advanced teacher to automatically identify confounding tokens based on causal relationships in the training corpus.\n\n**Stage 2 - Causal Attention Distillation:** In the second stage, it prunes these tokens during distillation to enact intervention, aligning the student's attention with the teacher's focus distribution on truly critical context tokens.\n\n### Results\nExperimental results demonstrate that LeaF achieves absolute improvements in various mathematical reasoning, code generation and multi-hop question answering benchmarks while effectively suppressing attention to confounding tokens during inference.\n\nThe code and resources are available at the [GitHub repository](https://github.com/RUCBM/LeaF/)."
    ],
    "durationSeconds": 6.166870217999996
  },
  "sourceToolAssistantUUID": "3945dfc0-0a04-49e3-87f6-1fcfbb43235b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T04:36:10.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EPUXT564JQckyR2hA4qTHK`</summary>

```json
{
  "query": "\"token pruning\" VLA \"causal\" robustness 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45754758-92e4-4363-840b-c9264caa62ee",
  "isSidechain": false,
  "requestId": "req_011CaywtAB6XTtovqLyxEjy7",
  "type": "assistant",
  "uuid": "a7d55885-c5f9-4d22-8f35-ed8b7c50e62f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbdQcErD7z6qJRnA9YqSJn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 32766,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 32766,
          "cache_creation_input_tokens": 1016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1016
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

_source line 27 · 2026-05-13T04:36:18.476Z_

<details><summary>↩ Tool result · `toolu_01EPUXT564JQckyR2hA4qTHK`</summary>

```text
Web search results for query: ""token pruning" VLA "causal" robustness 2026 site:arxiv.org"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2603.24941"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"[2506.12723] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/abs/2506.12723"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/html/2603.06480"}]

The search has returned several relevant papers on token pruning for Vision-Language-Action (VLA) models from arxiv.org in 2026. Here are the key findings:

## Notable Papers Found:

1. **VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models** (March 2026)
   - Proposes a training-free method that introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.
   - Consistently outperforms other baselines, maintaining robust manipulation capabilities even under extreme visual compression.

2. **Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models** (March 2026)
   - Introduces inter-layer token ranking consistency as a more stable signal of token credibility across various tasks, and proposes TIES, a lightweight token pruning framework.
   - Demonstrates robustness in handling environmental perturbations such as lighting and texture changes, with the method maintaining a higher average success rate.

3. **VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference** (February 2026)
   - Adopts a dual-level importance criterion for visual token retention and proposes a dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens.

4. **SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration** (October 2025)
   - Maintains high accuracy across various acceleration ratios, demonstrating strong robustness.

5. **ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models** (March 2026)
   - Notes that standard causal attention matrices may not fully capture pure semantic relevance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7d55885-c5f9-4d22-8f35-ed8b7c50e62f",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "914c59c8-9634-4a1d-942f-12c2b96fb9cb",
  "toolUseResult": {
    "query": "\"token pruning\" VLA \"causal\" robustness 2026 site:arxiv.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CzFhvthAAsFNrLJiXu65Pa",
        "content": [
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991"
          },
          {
            "title": "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.24941"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/html/2506.12723v2"
          },
          {
            "title": "[2506.12723] SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/abs/2506.12723"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          },
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          },
          {
            "title": "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.25766"
          },
          {
            "title": "History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation",
            "url": "https://arxiv.org/html/2603.06480"
          }
        ]
      },
      "The search has returned several relevant papers on token pruning for Vision-Language-Action (VLA) models from arxiv.org in 2026. Here are the key findings:\n\n## Notable Papers Found:\n\n1. **VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models** (March 2026)\n   - Proposes a training-free method that introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.\n   - Consistently outperforms other baselines, maintaining robust manipulation capabilities even under extreme visual compression.\n\n2. **Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models** (March 2026)\n   - Introduces inter-layer token ranking consistency as a more stable signal of token credibility across various tasks, and proposes TIES, a lightweight token pruning framework.\n   - Demonstrates robustness in handling environmental perturbations such as lighting and texture changes, with the method maintaining a higher average success rate.\n\n3. **VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference** (February 2026)\n   - Adopts a dual-level importance criterion for visual token retention and proposes a dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens.\n\n4. **SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration** (October 2025)\n   - Maintains high accuracy across various acceleration ratios, demonstrating strong robustness.\n\n5. **ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models** (March 2026)\n   - Notes that standard causal attention matrices may not fully capture pure semantic relevance."
    ],
    "durationSeconds": 8.356480849999993
  },
  "sourceToolAssistantUUID": "a7d55885-c5f9-4d22-8f35-ed8b7c50e62f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T04:36:21.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011aUy4FVdTkdUUBK8WhNieM`</summary>

```json
{
  "query": "ACTIVA amortized causal effect estimation transformer variational autoencoder arXiv 2503.01290"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914c59c8-9634-4a1d-942f-12c2b96fb9cb",
  "isSidechain": false,
  "requestId": "req_011Caywu6StoxKMf2fSftwtG",
  "type": "assistant",
  "uuid": "b268215c-0aac-4b49-b1cf-8b2eccfb4cfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5UriwwLSqkaaATsrhJHgQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 33782,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 33782,
          "cache_creation_input_tokens": 1109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1109
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

_source line 29 · 2026-05-13T04:36:27.712Z_

<details><summary>↩ Tool result · `toolu_011aUy4FVdTkdUUBK8WhNieM`</summary>

```text
Web search results for query: "ACTIVA amortized causal effect estimation transformer variational autoencoder arXiv 2503.01290"

Links: [{"title":"[2503.01290] ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder","url":"https://arxiv.org/abs/2503.01290"},{"title":"(PDF) ACTIVA: Amortized Causal Effect Estimation without Graphs via Transformer-based Variational Autoencoder","url":"https://www.researchgate.net/publication/389548551_ACTIVA_Amortized_Causal_Effect_Estimation_without_Graphs_via_Transformer-based_Variational_Autoencoder"},{"title":"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2503.01290"},{"title":"ACTIVA: Amortized Causal Effect Estimation via ...","url":"https://arxiv.org/pdf/2503.01290"},{"title":"[PDF] ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ACTIVA:-Amortized-Causal-Effect-Estimation-via-Sauter-Salehkaleybar/484cddc785f5d85cb5ddc6539798502aa7f4a2cf"},{"title":"ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder","url":"https://arxiv.org/html/2503.01290"},{"title":"ACTIVA: Amortized Causal Effect Estimation without Graphs via Transformer-based Variational Autoencoder","url":"https://arxiv.org/html/2503.01290v1"},{"title":"1 TabPFN-2.5 performance on the standard TabArena-lite benchmark [], TabPFNv2 classification subset. TabPFN-2.5 outperforms any other model in a forward pass, and marks a strong leap from TabPFNv2. When fine-tuned on real data, Real-TabPFN-2.5 shows even stronger performance. The horizontal dotted line stands for AutoGluon 1.4 extreme mode tuned for 4 hours, an ensemble of models including TabPFNv2.","url":"https://arxiv.org/html/2511.08667v1"},{"title":"[Literature Review] ACTIVA: Amortized Causal Effect Estimation without Graphs via Transformer-based Variational Autoencoder","url":"https://www.themoonlight.io/en/review/activa-amortized-causal-effect-estimation-without-graphs-via-transformer-based-variational-autoencoder"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=650&show=2000"}]

Based on the search results, here's information about the paper:

ACTIVA is a transformer-based conditional variational autoencoder (VAE) architecture for amortized causal inference, which estimates interventional distributions directly from observational data. 

**Key Features:**

- ACTIVA learns a latent representation conditioned on observational inputs and intervention queries, enabling zero-shot inference by amortizing causal knowledge from diverse training scenarios.

- The method extends causal transformer encoders to predict causal effects as mixtures of Gaussians and requires no causal graph, predicting interventional distributions given only observational data and a queried intervention.

**Advantages Over Existing Methods:**

Existing methods often require restrictive assumptions, and are typically limited by the lack of amortization across problem instances. Importantly, there is no need to have access to the underlying causal graph neither during training nor inference, avoiding common pitfalls when relying on such graphs.

**Evaluation:**

The architecture can be trained on synthetic data and then be applied to novel instances during inference, allowing for potential zero-shot transfer from simulated scenarios to real-world ones.

The paper was submitted to arXiv on March 3, 2025 and is authored by Andreas Sauter, Saber Salehkaleybar, Aske Plaat, and Erman Acar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b268215c-0aac-4b49-b1cf-8b2eccfb4cfa",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "fa239f14-b675-4894-9c7c-142c5b9ecf66",
  "toolUseResult": {
    "query": "ACTIVA amortized causal effect estimation transformer variational autoencoder arXiv 2503.01290",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HCzRHpvpi8dLeqK5s6RgCk",
        "content": [
          {
            "title": "[2503.01290] ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder",
            "url": "https://arxiv.org/abs/2503.01290"
          },
          {
            "title": "(PDF) ACTIVA: Amortized Causal Effect Estimation without Graphs via Transformer-based Variational Autoencoder",
            "url": "https://www.researchgate.net/publication/389548551_ACTIVA_Amortized_Causal_Effect_Estimation_without_Graphs_via_Transformer-based_Variational_Autoencoder"
          },
          {
            "title": "ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder | Space Frontiers",
            "url": "https://spacefrontiers.org/r/10.48550/arxiv.2503.01290"
          },
          {
            "title": "ACTIVA: Amortized Causal Effect Estimation via ...",
            "url": "https://arxiv.org/pdf/2503.01290"
          },
          {
            "title": "[PDF] ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ACTIVA:-Amortized-Causal-Effect-Estimation-via-Sauter-Salehkaleybar/484cddc785f5d85cb5ddc6539798502aa7f4a2cf"
          },
          {
            "title": "ACTIVA: Amortized Causal Effect Estimation via Transformer-based Variational Autoencoder",
            "url": "https://arxiv.org/html/2503.01290"
          },
          {
            "title": "ACTIVA: Amortized Causal Effect Estimation without Graphs via Transformer-based Variational Autoencoder",
            "url": "https://arxiv.org/html/2503.01290v1"
          },
          {
            "title": "1 TabPFN-2.5 performance on the standard TabArena-lite benchmark [], TabPFNv2 classification subset. TabPFN-2.5 outperforms any other model in a forward pass, and marks a strong leap from TabPFNv2. When fine-tuned on real data, Real-TabPFN-2.5 shows even stronger performance. The horizontal dotted line stands for AutoGluon 1.4 extreme mode tuned for 4 hours, an ensemble of models including TabPFNv2.",
            "url": "https://arxiv.org/html/2511.08667v1"
          },
          {
            "title": "[Literature Review] ACTIVA: Amortized Causal Effect Estimation without Graphs via Transformer-based Variational Autoencoder",
            "url": "https://www.themoonlight.io/en/review/activa-amortized-causal-effect-estimation-without-graphs-via-transformer-based-variational-autoencoder"
          },
          {
            "title": "Computer Science Mar 2025",
            "url": "https://arxiv.org/list/cs/2025-03?skip=650&show=2000"
          }
        ]
      },
      "Based on the search results, here's information about the paper:\n\nACTIVA is a transformer-based conditional variational autoencoder (VAE) architecture for amortized causal inference, which estimates interventional distributions directly from observational data. \n\n**Key Features:**\n\n- ACTIVA learns a latent representation conditioned on observational inputs and intervention queries, enabling zero-shot inference by amortizing causal knowledge from diverse training scenarios.\n\n- The method extends causal transformer encoders to predict causal effects as mixtures of Gaussians and requires no causal graph, predicting interventional distributions given only observational data and a queried intervention.\n\n**Advantages Over Existing Methods:**\n\nExisting methods often require restrictive assumptions, and are typically limited by the lack of amortization across problem instances. Importantly, there is no need to have access to the underlying causal graph neither during training nor inference, avoiding common pitfalls when relying on such graphs.\n\n**Evaluation:**\n\nThe architecture can be trained on synthetic data and then be applied to novel instances during inference, allowing for potential zero-shot transfer from simulated scenarios to real-world ones.\n\nThe paper was submitted to arXiv on March 3, 2025 and is authored by Andreas Sauter, Saber Salehkaleybar, Aske Plaat, and Erman Acar."
    ],
    "durationSeconds": 6.112835169000013
  },
  "sourceToolAssistantUUID": "b268215c-0aac-4b49-b1cf-8b2eccfb4cfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-13T04:36:27.715Z_

```json
{
  "parentUuid": "fa239f14-b675-4894-9c7c-142c5b9ecf66",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5e87230c-09c0-4517-9a2f-7bd8b2b79347",
  "timestamp": "2026-05-13T04:36:27.715Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5e87230c-09c0-4517-9a2f-7bd8b2b79347",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 33 · 2026-05-13T04:36:30.554Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WCJjxxcJeZGaQgJndjFh4y`</summary>

```json
{
  "query": "V-REx variance risk extrapolation invariant learning limitations non-linear"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e87230c-09c0-4517-9a2f-7bd8b2b79347",
  "isSidechain": false,
  "requestId": "req_011CaywumxRVPk1pxU6btEcj",
  "type": "assistant",
  "uuid": "7e714d94-bc7e-4ef0-a472-11127d80a74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LhQSELQgSWb6Ut5h7Qim4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 34891,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 34891,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 34 · 2026-05-13T04:36:37.557Z_

<details><summary>↩ Tool result · `toolu_01WCJjxxcJeZGaQgJndjFh4y`</summary>

```text
Web search results for query: "V-REx variance risk extrapolation invariant learning limitations non-linear"

Links: [{"title":"Out-of-Distribution Generalization via Risk Extrapolation","url":"http://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf"},{"title":"OUT-OF-DISTRIBUTION GENERALIZATION VIA RISK ...","url":"https://causalrlworkshop.github.io/pdf/CLDM_11.pdf"},{"title":"[2003.00688] Out-of-Distribution Generalization via Risk Extrapolation","url":"https://ar5iv.labs.arxiv.org/html/2003.00688"},{"title":"[2003.00688] Out-of-Distribution Generalization via Risk Extrapolation (REx)","url":"https://arxiv.org/abs/2003.00688"},{"title":"Robust Invariant Representation Learning by Distribution Extrapolation","url":"https://arxiv.org/html/2505.16126"},{"title":"Out-of-Distribution Generalization via Risk Extrapolation","url":"https://arxiv.org/pdf/2003.00688"},{"title":"Out-of-Distribution Generalization via Risk Extrapolation (REx)","url":"https://proceedings.mlr.press/v139/krueger21a.html"},{"title":"Out-of-Distribution Generalization via Risk Extrapolation (REx) | OpenReview","url":"https://openreview.net/forum?id=foNTMJHXHXC"},{"title":"Under review as a conference paper at ICLR 2021","url":"https://openreview.net/pdf?id=foNTMJHXHXC"},{"title":"Meta-Learned Invariant Risk Minimization","url":"https://arxiv.org/pdf/2103.12947"}]

Based on the search results, I've found comprehensive information about V-REx (Variance Risk Extrapolation) and its limitations, particularly regarding invariant learning and non-linear settings. Here are the key findings:

## Overview of V-REx

V-REx is a simpler variant of Risk Extrapolation (REx) that proposes a penalty on the variance of training risks. V-REx is simpler, stabler, and more effective than MM-REx (Minimax-REx), where β controls the balance between reducing average risk and enforcing equality of risks.

## Limitations in Non-linear Settings

A critical limitation of both REx and related approaches like IRM in non-linear settings is highlighted in the research. Studies state that "IRM and its alternatives fundamentally do not improve over standard Empirical Risk Minimization" in the non-linear setting – non-linearity being a primary motivation for the development of IRM.

## Additional Limitations

The theory underlying REx does not provide any guarantees for the settings where it is typically applied – namely, deep networks and finitely many training domains. Furthermore, the original IRMv1 penalty function is inherently non-linear with respect to the data distribution, making it not directly compatible with distributional extrapolation.

## Relationship to Invariant Learning

Like Invariant Risk Minimization (IRM), the Risk Extrapolation approach promotes generalization when "spurious" features are predictive during training but not at test time; for example, a model basing predictions on color will do worse than random guessing at test time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e714d94-bc7e-4ef0-a472-11127d80a74c",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "a289b2df-55be-41ee-b43b-042bc4eab596",
  "toolUseResult": {
    "query": "V-REx variance risk extrapolation invariant learning limitations non-linear",
    "results": [
      {
        "tool_use_id": "srvtoolu_0123CKCFhjj8x5k1JBmKmtFe",
        "content": [
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation",
            "url": "http://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf"
          },
          {
            "title": "OUT-OF-DISTRIBUTION GENERALIZATION VIA RISK ...",
            "url": "https://causalrlworkshop.github.io/pdf/CLDM_11.pdf"
          },
          {
            "title": "[2003.00688] Out-of-Distribution Generalization via Risk Extrapolation",
            "url": "https://ar5iv.labs.arxiv.org/html/2003.00688"
          },
          {
            "title": "[2003.00688] Out-of-Distribution Generalization via Risk Extrapolation (REx)",
            "url": "https://arxiv.org/abs/2003.00688"
          },
          {
            "title": "Robust Invariant Representation Learning by Distribution Extrapolation",
            "url": "https://arxiv.org/html/2505.16126"
          },
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation",
            "url": "https://arxiv.org/pdf/2003.00688"
          },
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation (REx)",
            "url": "https://proceedings.mlr.press/v139/krueger21a.html"
          },
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation (REx) | OpenReview",
            "url": "https://openreview.net/forum?id=foNTMJHXHXC"
          },
          {
            "title": "Under review as a conference paper at ICLR 2021",
            "url": "https://openreview.net/pdf?id=foNTMJHXHXC"
          },
          {
            "title": "Meta-Learned Invariant Risk Minimization",
            "url": "https://arxiv.org/pdf/2103.12947"
          }
        ]
      },
      "Based on the search results, I've found comprehensive information about V-REx (Variance Risk Extrapolation) and its limitations, particularly regarding invariant learning and non-linear settings. Here are the key findings:\n\n## Overview of V-REx\n\nV-REx is a simpler variant of Risk Extrapolation (REx) that proposes a penalty on the variance of training risks. V-REx is simpler, stabler, and more effective than MM-REx (Minimax-REx), where β controls the balance between reducing average risk and enforcing equality of risks.\n\n## Limitations in Non-linear Settings\n\nA critical limitation of both REx and related approaches like IRM in non-linear settings is highlighted in the research. Studies state that \"IRM and its alternatives fundamentally do not improve over standard Empirical Risk Minimization\" in the non-linear setting – non-linearity being a primary motivation for the development of IRM.\n\n## Additional Limitations\n\nThe theory underlying REx does not provide any guarantees for the settings where it is typically applied – namely, deep networks and finitely many training domains. Furthermore, the original IRMv1 penalty function is inherently non-linear with respect to the data distribution, making it not directly compatible with distributional extrapolation.\n\n## Relationship to Invariant Learning\n\nLike Invariant Risk Minimization (IRM), the Risk Extrapolation approach promotes generalization when \"spurious\" features are predictive during training but not at test time; for example, a model basing predictions on color will do worse than random guessing at test time."
    ],
    "durationSeconds": 6.998770217999991
  },
  "sourceToolAssistantUUID": "7e714d94-bc7e-4ef0-a472-11127d80a74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-13T04:36:41.628Z_

Now let me search for more recent competing work and verify specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a289b2df-55be-41ee-b43b-042bc4eab596",
  "isSidechain": false,
  "requestId": "req_011CaywvW7xTuN3odnZ5MjRY",
  "type": "assistant",
  "uuid": "277a1797-16c9-446d-ab2a-34eb175b82df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0124W1h7WvoA13EnFTfCDFgr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 36168,
      "output_tokens": 79,
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
          "output_tokens": 79,
          "cache_read_input_tokens": 36168,
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

_source line 36 · 2026-05-13T04:36:42.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tTf7LmnYmGB8Ee4b8WQ6U`</summary>

```json
{
  "query": "causal invariance token selection vision language action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "277a1797-16c9-446d-ab2a-34eb175b82df",
  "isSidechain": false,
  "requestId": "req_011CaywvW7xTuN3odnZ5MjRY",
  "type": "assistant",
  "uuid": "8bd06ada-fa77-47dd-86ac-d9aa79b97d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0124W1h7WvoA13EnFTfCDFgr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 36168,
      "output_tokens": 79,
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
          "output_tokens": 79,
          "cache_read_input_tokens": 36168,
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

_source line 37 · 2026-05-13T04:36:50.214Z_

<details><summary>↩ Tool result · `toolu_015tTf7LmnYmGB8Ee4b8WQ6U`</summary>

```text
Web search results for query: "causal invariance token selection vision language action model 2026"

Links: [{"title":"Learning Invariant Causal Mechanism from Vision-Language Models","url":"https://arxiv.org/html/2405.15289v3"},{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"ICML Poster Learning Invariant Causal Mechanism from Vision-Language Models","url":"https://icml.cc/virtual/2025/poster/45848"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"Unified Vision-Language-Action Tokenization","url":"https://www.emergentmind.com/topics/unified-vision-language-action-vla-tokenization"},{"title":"[2405.15289] Learning Invariant Causal Mechanism from Vision-Language Models","url":"https://arxiv.org/abs/2405.15289"},{"title":"[2501.09747] FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2501.09747"},{"title":"A Survey on Vision-Language-Action Models for Embodied ...","url":"https://arxiv.org/html/2405.14093v8"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"}]

Based on the search results, here's what I found about causal invariance, token selection, and vision-language-action models:

## Causal Invariance in Vision-Language Models

Research using Structural Causal Models (SCM) shows that causal mechanisms involving both invariant and variant factors in training environments differ from those in test environments, while causal mechanisms with solely invariant factors remain consistent across environments. The Invariant Causal Mechanism of CLIP (CLIP-ICM) framework involves collecting interventional data, estimating a linear projection matrix, and making predictions within the invariant subspace.

## Token Selection in Vision-Language-Action Models

Recent research on VLA models emphasizes the importance of token selection for efficiency. Not all visual information is equally relevant to the decision-making process—in many tasks, substantial portions of the input image, such as background regions, task-irrelevant objects, or temporally invariant content, do not significantly influence action selection.

VLA-Cache pinpoints static tokens with minimal inter-frame variance and evicts task-relevant ones, leveraging KV-cache for seamless redeployment in ensuing iterations. Additionally, this strategy exploits temporal invariances across frames or steps, transforming static or stable representations into persistent assets that undergird fluid embodied trajectories.

## Action Tokenization Approaches

Current VLA models can be unified under a framework where vision and language inputs are processed by a series of VLA modules, producing a chain of action tokens, with the primary design choice distinguishing VLA models lying in how action tokens are formulated.

These developments reflect growing efforts to improve VLA efficiency and robustness through principled approaches to understanding causal factors and optimizing token processing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bd06ada-fa77-47dd-86ac-d9aa79b97d66",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "1efb33fe-6dff-426b-a192-ed91a848ddab",
  "toolUseResult": {
    "query": "causal invariance token selection vision language action model 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RmYsucqV3P7P8ZHhVdY9C2",
        "content": [
          {
            "title": "Learning Invariant Causal Mechanism from Vision-Language Models",
            "url": "https://arxiv.org/html/2405.15289v3"
          },
          {
            "title": "A Survey on Vision-Language-Action Models: An Action Tokenization Perspective",
            "url": "https://arxiv.org/html/2507.01925v1"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          },
          {
            "title": "ICML Poster Learning Invariant Causal Mechanism from Vision-Language Models",
            "url": "https://icml.cc/virtual/2025/poster/45848"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "Unified Vision-Language-Action Tokenization",
            "url": "https://www.emergentmind.com/topics/unified-vision-language-action-vla-tokenization"
          },
          {
            "title": "[2405.15289] Learning Invariant Causal Mechanism from Vision-Language Models",
            "url": "https://arxiv.org/abs/2405.15289"
          },
          {
            "title": "[2501.09747] FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2501.09747"
          },
          {
            "title": "A Survey on Vision-Language-Action Models for Embodied ...",
            "url": "https://arxiv.org/html/2405.14093v8"
          },
          {
            "title": "Vision-Language-Action Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v1"
          }
        ]
      },
      "Based on the search results, here's what I found about causal invariance, token selection, and vision-language-action models:\n\n## Causal Invariance in Vision-Language Models\n\nResearch using Structural Causal Models (SCM) shows that causal mechanisms involving both invariant and variant factors in training environments differ from those in test environments, while causal mechanisms with solely invariant factors remain consistent across environments. The Invariant Causal Mechanism of CLIP (CLIP-ICM) framework involves collecting interventional data, estimating a linear projection matrix, and making predictions within the invariant subspace.\n\n## Token Selection in Vision-Language-Action Models\n\nRecent research on VLA models emphasizes the importance of token selection for efficiency. Not all visual information is equally relevant to the decision-making process—in many tasks, substantial portions of the input image, such as background regions, task-irrelevant objects, or temporally invariant content, do not significantly influence action selection.\n\nVLA-Cache pinpoints static tokens with minimal inter-frame variance and evicts task-relevant ones, leveraging KV-cache for seamless redeployment in ensuing iterations. Additionally, this strategy exploits temporal invariances across frames or steps, transforming static or stable representations into persistent assets that undergird fluid embodied trajectories.\n\n## Action Tokenization Approaches\n\nCurrent VLA models can be unified under a framework where vision and language inputs are processed by a series of VLA modules, producing a chain of action tokens, with the primary design choice distinguishing VLA models lying in how action tokens are formulated.\n\nThese developments reflect growing efforts to improve VLA efficiency and robustness through principled approaches to understanding causal factors and optimizing token processing."
    ],
    "durationSeconds": 7.937970342000001
  },
  "sourceToolAssistantUUID": "8bd06ada-fa77-47dd-86ac-d9aa79b97d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T04:36:53.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McfoLQ2st8A4Vu2137ykEn`</summary>

```json
{
  "query": "VLA robustness distribution shift visual perturbation LIBERO-Plus 2026 new methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efb33fe-6dff-426b-a192-ed91a848ddab",
  "isSidechain": false,
  "requestId": "req_011CaywwSBr8sGUpNNEsnfUr",
  "type": "assistant",
  "uuid": "986a8396-b94f-46a1-a947-9d3c29959616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeUXZwdB96CUDFKdFyVCGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 37071,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 37071,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 39 · 2026-05-13T04:37:01.066Z_

<details><summary>↩ Tool result · `toolu_01McfoLQ2st8A4Vu2137ykEn`</summary>

```text
Web search results for query: "VLA robustness distribution shift visual perturbation LIBERO-Plus 2026 new methods"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"}]

I found comprehensive information about VLA robustness, distribution shift, and visual perturbations related to LIBERO-Plus. Here are the key findings:

## LIBERO-Plus: Robustness Analysis Framework

LIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise.

## Key Robustness Findings

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Critical Vulnerabilities Identified

Current VLA models exhibit extreme sensitivity to perturbations in camera viewpoint and robot initial state, revealing fundamental limitations in their spatial reasoning capabilities.

Current VLA models lack compositional generalization capabilities. Their learned representations are entangled and cannot handle the complex, multi-dimensional perturbations that characterize real-world environments.

## Recent Robustness Methods

On LIBERO benchmark, RobustVLA achieves absolute gains of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across 17 perturbations, being 50.6x faster than visual-robust BYOVLA that requires external LLMs, and achieving a 10.4% gain under mixed perturbations.

The research highlights that while VLA models show impressive benchmark scores, they have fundamental brittleness under distribution shifts and visual perturbations in real-world settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "986a8396-b94f-46a1-a947-9d3c29959616",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "76ee2e5f-38ab-4cf8-ba83-a82288d99082",
  "toolUseResult": {
    "query": "VLA robustness distribution shift visual perturbation LIBERO-Plus 2026 new methods",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wkfd8wrfkzZyKYWRrFv9st",
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
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...",
            "url": "https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "How brittle are the VLA models in robotics | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 ON ROBUSTNESS",
            "url": "https://arxiv.org/pdf/2510.00037v4"
          }
        ]
      },
      "I found comprehensive information about VLA robustness, distribution shift, and visual perturbations related to LIBERO-Plus. Here are the key findings:\n\n## LIBERO-Plus: Robustness Analysis Framework\n\nLIBERO-Plus is a comprehensive, automatic, and fine-grained evaluation framework with controlled perturbations across seven dimensions: object layouts, camera viewpoints, robot initial states, language instructions, lighting conditions, background textures, and sensor noise.\n\n## Key Robustness Findings\n\nModels exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\nSurprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\n## Critical Vulnerabilities Identified\n\nCurrent VLA models exhibit extreme sensitivity to perturbations in camera viewpoint and robot initial state, revealing fundamental limitations in their spatial reasoning capabilities.\n\nCurrent VLA models lack compositional generalization capabilities. Their learned representations are entangled and cannot handle the complex, multi-dimensional perturbations that characterize real-world environments.\n\n## Recent Robustness Methods\n\nOn LIBERO benchmark, RobustVLA achieves absolute gains of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across 17 perturbations, being 50.6x faster than visual-robust BYOVLA that requires external LLMs, and achieving a 10.4% gain under mixed perturbations.\n\nThe research highlights that while VLA models show impressive benchmark scores, they have fundamental brittleness under distribution shifts and visual perturbations in real-world settings."
    ],
    "durationSeconds": 7.793041017000011
  },
  "sourceToolAssistantUUID": "986a8396-b94f-46a1-a947-9d3c29959616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T04:37:04.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MFUTNhp8Gk1MWsdwwknXDR`</summary>

```json
{
  "query": "\"spatial locality\" causal features tokens transformer invariance visual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76ee2e5f-38ab-4cf8-ba83-a82288d99082",
  "isSidechain": false,
  "requestId": "req_011CaywxEasZEURqWe9RU5NG",
  "type": "assistant",
  "uuid": "8603c21e-2c57-4065-95fb-40ac01026dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPWs5Auz1po87dAYV3zsKK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 37985,
      "output_tokens": 63,
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
          "output_tokens": 63,
          "cache_read_input_tokens": 37985,
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

_source line 41 · 2026-05-13T04:37:12.640Z_

<details><summary>↩ Tool result · `toolu_01MFUTNhp8Gk1MWsdwwknXDR`</summary>

```text
Web search results for query: ""spatial locality" causal features tokens transformer invariance visual"

Links: [{"title":"Position Information Emerges in Causal Transformers Without Positional Encodings via Similarity of Nearby Embeddings","url":"https://arxiv.org/html/2501.00073"},{"title":"Vision Transformers Explained: The Future of Computer Vision?","url":"https://blog.roboflow.com/vision-transformers/"},{"title":"Spatial entropy as an inductive bias for vision transformers | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-024-06570-7"},{"title":"26 Transformers – Foundations of Computer Vision","url":"https://visionbook.mit.edu/transformers.html"},{"title":"Unified Local and Global Attention Interaction Modeling for Vision Transformers","url":"https://arxiv.org/html/2412.18778v1"},{"title":"Causal-Transformer: Spatial-temporal causal attention-based transformer for time series prediction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405896324010607"},{"title":"MAIT: INTEGRATING SPATIAL LOCALITY INTO IMAGE ...","url":"https://openreview.net/pdf?id=Xb2YyVApEj6"},{"title":"Incorporating Spatial Locality Into Self-attention for Training Vision Transformer on Small-Scale Datasets | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-78122-3_17"},{"title":"Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features","url":"https://arxiv.org/html/2509.16629"},{"title":"Ripple Attention for Visual Perception with Sub-quadratic Complexity","url":"https://proceedings.mlr.press/v162/zheng22a/zheng22a.pdf"}]

I've completed a web search for your query: "spatial locality" causal features tokens transformer invariance visual

Here are the key findings from the search results:

## Position Information and Causal Attention

Embeddings exhibit an adjacency pattern, meaning position information may be partially recoverable from them, as embeddings corresponding to spatially nearby positions tend to be more similar. Nearby embeddings are more similar to each other than faraway embeddings, allowing the transformer to potentially reconstruct the positions of tokens, and this pattern can occur in both trained and randomly initialized Transformer models with causal attention and no positional encodings.

## Spatial Locality in Vision Transformers

Spatial locality plays a crucial role in computer vision tasks. In contrast to CNN models, locality is not explicitly introduced in the transformer structure. With attention masks, one can explicitly insert locality into self-attention modules without introducing any extra parameter or computation.

A novel self-attention mechanism can incorporate spatial locality constraints in the attention calculation by performing the self-attention process independently in spatially divided regions, limiting the receptive fields of attention and forcing local feature extraction.

## Permutation Invariance and Causal Attention

Transformers with causal attention are not permutation-equivariant to the input sequence, which implies the possibility of success in training causal Transformers without positional encodings — "non-causal" attention could not accomplish that.

## Vision Transformer Limitations

ViTs can be less robust to spatial transformations (such as rotation or mirroring) unless explicitly trained for such invariances. Unlike CNNs, which inherently encode translation invariance, ViTs may struggle with out-of-distribution visual changes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8603c21e-2c57-4065-95fb-40ac01026dd5",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "d92611c7-dc07-4dfd-8d72-b96c84a0cb6c",
  "toolUseResult": {
    "query": "\"spatial locality\" causal features tokens transformer invariance visual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M3vvjFaUTrBni6Jwv1NZGM",
        "content": [
          {
            "title": "Position Information Emerges in Causal Transformers Without Positional Encodings via Similarity of Nearby Embeddings",
            "url": "https://arxiv.org/html/2501.00073"
          },
          {
            "title": "Vision Transformers Explained: The Future of Computer Vision?",
            "url": "https://blog.roboflow.com/vision-transformers/"
          },
          {
            "title": "Spatial entropy as an inductive bias for vision transformers | Machine Learning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10994-024-06570-7"
          },
          {
            "title": "26 Transformers – Foundations of Computer Vision",
            "url": "https://visionbook.mit.edu/transformers.html"
          },
          {
            "title": "Unified Local and Global Attention Interaction Modeling for Vision Transformers",
            "url": "https://arxiv.org/html/2412.18778v1"
          },
          {
            "title": "Causal-Transformer: Spatial-temporal causal attention-based transformer for time series prediction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2405896324010607"
          },
          {
            "title": "MAIT: INTEGRATING SPATIAL LOCALITY INTO IMAGE ...",
            "url": "https://openreview.net/pdf?id=Xb2YyVApEj6"
          },
          {
            "title": "Incorporating Spatial Locality Into Self-attention for Training Vision Transformer on Small-Scale Datasets | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-78122-3_17"
          },
          {
            "title": "Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features",
            "url": "https://arxiv.org/html/2509.16629"
          },
          {
            "title": "Ripple Attention for Visual Perception with Sub-quadratic Complexity",
            "url": "https://proceedings.mlr.press/v162/zheng22a/zheng22a.pdf"
          }
        ]
      },
      "I've completed a web search for your query: \"spatial locality\" causal features tokens transformer invariance visual\n\nHere are the key findings from the search results:\n\n## Position Information and Causal Attention\n\nEmbeddings exhibit an adjacency pattern, meaning position information may be partially recoverable from them, as embeddings corresponding to spatially nearby positions tend to be more similar. Nearby embeddings are more similar to each other than faraway embeddings, allowing the transformer to potentially reconstruct the positions of tokens, and this pattern can occur in both trained and randomly initialized Transformer models with causal attention and no positional encodings.\n\n## Spatial Locality in Vision Transformers\n\nSpatial locality plays a crucial role in computer vision tasks. In contrast to CNN models, locality is not explicitly introduced in the transformer structure. With attention masks, one can explicitly insert locality into self-attention modules without introducing any extra parameter or computation.\n\nA novel self-attention mechanism can incorporate spatial locality constraints in the attention calculation by performing the self-attention process independently in spatially divided regions, limiting the receptive fields of attention and forcing local feature extraction.\n\n## Permutation Invariance and Causal Attention\n\nTransformers with causal attention are not permutation-equivariant to the input sequence, which implies the possibility of success in training causal Transformers without positional encodings — \"non-causal\" attention could not accomplish that.\n\n## Vision Transformer Limitations\n\nViTs can be less robust to spatial transformations (such as rotation or mirroring) unless explicitly trained for such invariances. Unlike CNNs, which inherently encode translation invariance, ViTs may struggle with out-of-distribution visual changes."
    ],
    "durationSeconds": 8.223750880999999
  },
  "sourceToolAssistantUUID": "8603c21e-2c57-4065-95fb-40ac01026dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d92611c7-dc07-4dfd-8d72-b96c84a0cb6c",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 44 · 2026-05-13T04:37:15.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L6gcRCh2thbPisjg5vLyjZ`</summary>

```json
{
  "query": "CoRL 2026 submission deadline date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d92611c7-dc07-4dfd-8d72-b96c84a0cb6c",
  "isSidechain": false,
  "requestId": "req_011Caywy61hrUGPS9BtwhxfH",
  "type": "assistant",
  "uuid": "b56aa376-d41b-40bd-97b7-08cf02fb578a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J3JHrZ6NsYTDencTJ4yHm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 39016,
      "output_tokens": 60,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60,
          "cache_read_input_tokens": 39016,
          "cache_creation_input_tokens": 948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 948
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

_source line 45 · 2026-05-13T04:37:17.923Z_

<details><summary>↩ Tool result · `toolu_01L6gcRCh2thbPisjg5vLyjZ`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline date"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

The conference itself will be held November 9-12, 2026 in Austin, Texas, US.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b56aa376-d41b-40bd-97b7-08cf02fb578a",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "e7a0f340-808b-4531-92b0-24c57b541ea0",
  "toolUseResult": {
    "query": "CoRL 2026 submission deadline date",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B6UwVc6TBgT6FXAhPDFhux",
        "content": [
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
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
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
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
            "title": "Vincent Vanhoucke's Post",
            "url": "https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"
          },
          {
            "title": "CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz",
            "url": "https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"
          }
        ]
      },
      "Based on the search results, here are the CoRL 2026 submission deadlines:\n\nThe abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.\n\nThe conference itself will be held November 9-12, 2026 in Austin, Texas, US."
    ],
    "durationSeconds": 2.8205083049999957
  },
  "sourceToolAssistantUUID": "b56aa376-d41b-40bd-97b7-08cf02fb578a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-13T04:37:20.204Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012CunwwXzSjviGFU5T5JsNN`</summary>

```json
{
  "query": "AAAI 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7a0f340-808b-4531-92b0-24c57b541ea0",
  "isSidechain": false,
  "requestId": "req_011CaywyUbGQSvqMmLf3puKv",
  "type": "assistant",
  "uuid": "25f55db0-dd4e-4da0-904a-8550f54c342d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ginonSd8aSSuMxGeDSuFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 39964,
      "output_tokens": 61,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 61,
          "cache_read_input_tokens": 39964,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
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

_source line 47 · 2026-05-13T04:37:23.906Z_

<details><summary>↩ Tool result · `toolu_012CunwwXzSjviGFU5T5JsNN`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"}]

Based on the search results, here's what I found about the AAAI 2027 submission deadline:

The AAAI 2027 paper submission deadline is TBD (to be determined). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

The conference will be held in Montréal, Québec, Canada from February 16-23, 2027. For the most current information, the official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25f55db0-dd4e-4da0-904a-8550f54c342d",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "ddb1d466-24d7-4ae7-90dd-39ce0a81c205",
  "toolUseResult": {
    "query": "AAAI 2027 submission deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_014TvkjADDCLETf2w1ZVgU2p",
        "content": [
          {
            "title": "AAAI Conference on Artificial Intelligence - AAAI",
            "url": "https://aaai.org/conference/aaai/"
          },
          {
            "title": "AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=3"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "AAAI 2027 Conference Deadline | Live Countdown Tracker",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          },
          {
            "title": "AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/aaai"
          },
          {
            "title": "Key deadlines in AI and ML conferences",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...",
            "url": "https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence",
            "url": "http://aideadlines.org/conference/?id=aaai27"
          }
        ]
      },
      "Based on the search results, here's what I found about the AAAI 2027 submission deadline:\n\nThe AAAI 2027 paper submission deadline is TBD (to be determined). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.\n\nThe conference will be held in Montréal, Québec, Canada from February 16-23, 2027. For the most current information, the official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/."
    ],
    "durationSeconds": 3.698904386999988
  },
  "sourceToolAssistantUUID": "25f55db0-dd4e-4da0-904a-8550f54c342d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-13T04:37:27.109Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DmBKtExkQTQQeD3H4hxxFM`</summary>

```json
{
  "query": "Shapley value token attribution transformer amortized scalability computational cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddb1d466-24d7-4ae7-90dd-39ce0a81c205",
  "isSidechain": false,
  "requestId": "req_011Caywyw4UVf2savH8nZHmF",
  "type": "assistant",
  "uuid": "436926c9-0cc6-404b-a43c-a5190108d079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1kGh15jaRbLSMtj3vU7cV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 40591,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 40591,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 49 · 2026-05-13T04:37:34.583Z_

<details><summary>↩ Tool result · `toolu_01DmBKtExkQTQQeD3H4hxxFM`</summary>

```text
Web search results for query: "Shapley value token attribution transformer amortized scalability computational cost"

Links: [{"title":"TokenShapley: Token Level Context Attribution with Shapley Value","url":"https://arxiv.org/html/2507.05261v2"},{"title":"GitHub - suinleelab/vit-shapley: Learning to Estimate Shapley Values with Vision Transformers · GitHub","url":"https://github.com/suinleelab/vit-shapley"},{"title":"[2507.05261] TokenShapley: Token Level Context Attribution with Shapley Value","url":"https://arxiv.org/abs/2507.05261"},{"title":"Helpful or Harmful Data? Fine-tuning-free Shapley Attribution for Explaining Language Model Predictions","url":"https://arxiv.org/html/2406.04606v1"},{"title":"[2305.19998] Efficient Shapley Values Estimation by Amortization for Text Classification","url":"https://ar5iv.labs.arxiv.org/html/2305.19998"},{"title":"Stochastic Amortization: A Unified Approach to Accelerate Feature and Data Attribution","url":"https://arxiv.org/html/2401.15866"},{"title":"Shapley Value Attribution in Chain of Thought","url":"https://www.lesswrong.com/posts/FX5JmftqL2j6K8dn4/shapley-value-attribution-in-chain-of-thought"},{"title":"Fast Shapley Value Estimation: A Unified Approach","url":"https://arxiv.org/html/2311.01010"},{"title":"(PDF) Learning to Estimate Shapley Values with Vision Transformers","url":"https://www.researchgate.net/publication/361274669_Learning_to_Estimate_Shapley_Values_with_Vision_Transformers"},{"title":"Efficient Shapley Values Calculation for Transformer Explainability | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-47634-1_5"}]

I found several relevant results about Shapley value token attribution and transformer explainability. Here's what the search revealed:

## Key Research Areas

**TokenShapley Method**: An efficient strategy for exact token-level Shapley value calculation leverages embedding-based retrieval and weighted KNN search, eliminating the need for Monte Carlo sampling. TokenShapley is a novel token-level attribution method that combines Shapley value-based data attribution with KNN-based retrieval techniques and leverages a precomputed datastore for contextual retrieval and computing Shapley values to quantify token importance.

**Computational Cost Challenge**: Shapley values are a theoretically grounded model explanation approach, but their exponential computational cost makes them difficult to use with large deep learning models. The cost of computing the Shapley value scales exponentially with the number of tokens.

**Amortization Solutions**: ViT-Shapley makes Shapley values practical for vision transformer models by learning an amortized explainer model that generates explanations in a single forward pass. FreeShap amortizes the cost of calculating Shapley values by pre-computing the eNTK matrix to replace all subsequent training with kernel regression, which is significantly cheaper in computational cost than fine-tuning.

**Additional Methods**: Computing Shapley values encounters exponential complexity as the number of features increases, and various approaches including ApproSemivalue, KernelSHAP, and FastSHAP have been explored to expedite the computation.

The search results show active research into making Shapley value attribution practical for transformers through amortized models and efficient computational techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "436926c9-0cc6-404b-a43c-a5190108d079",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "c4d32c2e-cf3e-4dad-972f-743176fd2471",
  "toolUseResult": {
    "query": "Shapley value token attribution transformer amortized scalability computational cost",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GWZTH8VB4zcqB9ii43CQe8",
        "content": [
          {
            "title": "TokenShapley: Token Level Context Attribution with Shapley Value",
            "url": "https://arxiv.org/html/2507.05261v2"
          },
          {
            "title": "GitHub - suinleelab/vit-shapley: Learning to Estimate Shapley Values with Vision Transformers · GitHub",
            "url": "https://github.com/suinleelab/vit-shapley"
          },
          {
            "title": "[2507.05261] TokenShapley: Token Level Context Attribution with Shapley Value",
            "url": "https://arxiv.org/abs/2507.05261"
          },
          {
            "title": "Helpful or Harmful Data? Fine-tuning-free Shapley Attribution for Explaining Language Model Predictions",
            "url": "https://arxiv.org/html/2406.04606v1"
          },
          {
            "title": "[2305.19998] Efficient Shapley Values Estimation by Amortization for Text Classification",
            "url": "https://ar5iv.labs.arxiv.org/html/2305.19998"
          },
          {
            "title": "Stochastic Amortization: A Unified Approach to Accelerate Feature and Data Attribution",
            "url": "https://arxiv.org/html/2401.15866"
          },
          {
            "title": "Shapley Value Attribution in Chain of Thought",
            "url": "https://www.lesswrong.com/posts/FX5JmftqL2j6K8dn4/shapley-value-attribution-in-chain-of-thought"
          },
          {
            "title": "Fast Shapley Value Estimation: A Unified Approach",
            "url": "https://arxiv.org/html/2311.01010"
          },
          {
            "title": "(PDF) Learning to Estimate Shapley Values with Vision Transformers",
            "url": "https://www.researchgate.net/publication/361274669_Learning_to_Estimate_Shapley_Values_with_Vision_Transformers"
          },
          {
            "title": "Efficient Shapley Values Calculation for Transformer Explainability | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-47634-1_5"
          }
        ]
      },
      "I found several relevant results about Shapley value token attribution and transformer explainability. Here's what the search revealed:\n\n## Key Research Areas\n\n**TokenShapley Method**: An efficient strategy for exact token-level Shapley value calculation leverages embedding-based retrieval and weighted KNN search, eliminating the need for Monte Carlo sampling. TokenShapley is a novel token-level attribution method that combines Shapley value-based data attribution with KNN-based retrieval techniques and leverages a precomputed datastore for contextual retrieval and computing Shapley values to quantify token importance.\n\n**Computational Cost Challenge**: Shapley values are a theoretically grounded model explanation approach, but their exponential computational cost makes them difficult to use with large deep learning models. The cost of computing the Shapley value scales exponentially with the number of tokens.\n\n**Amortization Solutions**: ViT-Shapley makes Shapley values practical for vision transformer models by learning an amortized explainer model that generates explanations in a single forward pass. FreeShap amortizes the cost of calculating Shapley values by pre-computing the eNTK matrix to replace all subsequent training with kernel regression, which is significantly cheaper in computational cost than fine-tuning.\n\n**Additional Methods**: Computing Shapley values encounters exponential complexity as the number of features increases, and various approaches including ApproSemivalue, KernelSHAP, and FastSHAP have been explored to expedite the computation.\n\nThe search results show active research into making Shapley value attribution practical for transformers through amortized models and efficient computational techniques."
    ],
    "durationSeconds": 7.469791584999999
  },
  "sourceToolAssistantUUID": "436926c9-0cc6-404b-a43c-a5190108d079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-13T04:37:37.293Z_

Let me now do deeper searches on competing work and potential gaps in the proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4d32c2e-cf3e-4dad-972f-743176fd2471",
  "isSidechain": false,
  "requestId": "req_011CaywzhqX4Ho7BWueQHJ7H",
  "type": "assistant",
  "uuid": "d80dd29a-0f1c-4d52-9ebf-a6a967901ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GanKKhVxMATsM1DFUZxDt9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 41348,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 41348,
          "cache_creation_input_tokens": 963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 963
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

_source line 51 · 2026-05-13T04:37:38.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019q4A36Z9KV72noRyDvXtJR`</summary>

```json
{
  "query": "TIES inter-layer rank consistency token pruning VLA robustness arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80dd29a-0f1c-4d52-9ebf-a6a967901ad0",
  "isSidechain": false,
  "requestId": "req_011CaywzhqX4Ho7BWueQHJ7H",
  "type": "assistant",
  "uuid": "7eda1670-30d3-439f-85e6-ceea1523fdfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GanKKhVxMATsM1DFUZxDt9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 41348,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 41348,
          "cache_creation_input_tokens": 963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 963
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

_source line 52 · 2026-05-13T04:37:45.675Z_

<details><summary>↩ Tool result · `toolu_019q4A36Z9KV72noRyDvXtJR`</summary>

```text
Web search results for query: "TIES inter-layer rank consistency token pruning VLA robustness arXiv 2603"

Links: [{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2603.24941"},{"title":"[2603.24941] Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.24941"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for","url":"https://arxiv.org/pdf/2603.24941"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766"},{"title":"TIDE: Every Layer Knows the Token Beneath the Context","url":"https://arxiv.org/html/2605.06216"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"}]

I found the paper you're looking for! Here's information about the research:

## TIES: Tau-guided Inter-layer Efficient Selection

TIES (Tau-guided Inter-layer Efficient Selection) is a dynamic framework guided by inter-layer token ranking consistency for Vision-Language-Action (VLA) models. 

### Key Approach

By adaptively balancing attention magnitude with ranking consistency, TIES ensures robust token selection without requiring additional training. The framework introduces inter-layer token ranking consistency, a metric based on the Kendall rank correlation coefficient (τ), which offers a more stable signal of token credibility across various tasks, architectures, and environments.

### Framework Design

TIES employs a small set of task images to establish a reference baseline distribution. During deployment, the framework dynamically adjusts the proportion of retained high-attention tokens by comparing the τ of the current frame to this distribution. To further reduce computational costs, TIES capitalizes on temporal redundancy in VLA inference, ensuring the pruning strategy remains robust to scene changes while avoiding redundant calculations for static observations and minimal changes.

### Results

On the CogACT + SIMPLER benchmark, TIES improves average success rates by 6% while reducing token usage by 78%, and demonstrates strong generalization across diverse decoders and benchmarks. Soft-TIES maintains a high average success rate of 67.6%, effectively bridging the gap between efficiency and robustness in challenging robustness evaluations with environmental perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eda1670-30d3-439f-85e6-ceea1523fdfa",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "54d6d0a7-2aa1-4d4a-85e6-9e25de6fb263",
  "toolUseResult": {
    "query": "TIES inter-layer rank consistency token pruning VLA robustness arXiv 2603",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L3HGNfPFsFnnyEooAvsvYs",
        "content": [
          {
            "title": "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.24941"
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
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.25766"
          },
          {
            "title": "TIDE: Every Layer Knows the Token Beneath the Context",
            "url": "https://arxiv.org/html/2605.06216"
          },
          {
            "title": "[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/html/2506.12723v2"
          },
          {
            "title": "[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.25766"
          }
        ]
      },
      "I found the paper you're looking for! Here's information about the research:\n\n## TIES: Tau-guided Inter-layer Efficient Selection\n\nTIES (Tau-guided Inter-layer Efficient Selection) is a dynamic framework guided by inter-layer token ranking consistency for Vision-Language-Action (VLA) models. \n\n### Key Approach\n\nBy adaptively balancing attention magnitude with ranking consistency, TIES ensures robust token selection without requiring additional training. The framework introduces inter-layer token ranking consistency, a metric based on the Kendall rank correlation coefficient (τ), which offers a more stable signal of token credibility across various tasks, architectures, and environments.\n\n### Framework Design\n\nTIES employs a small set of task images to establish a reference baseline distribution. During deployment, the framework dynamically adjusts the proportion of retained high-attention tokens by comparing the τ of the current frame to this distribution. To further reduce computational costs, TIES capitalizes on temporal redundancy in VLA inference, ensuring the pruning strategy remains robust to scene changes while avoiding redundant calculations for static observations and minimal changes.\n\n### Results\n\nOn the CogACT + SIMPLER benchmark, TIES improves average success rates by 6% while reducing token usage by 78%, and demonstrates strong generalization across diverse decoders and benchmarks. Soft-TIES maintains a high average success rate of 67.6%, effectively bridging the gap between efficiency and robustness in challenging robustness evaluations with environmental perturbations."
    ],
    "durationSeconds": 7.526986621999996
  },
  "sourceToolAssistantUUID": "7eda1670-30d3-439f-85e6-ceea1523fdfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53 · 2026-05-13T04:37:45.678Z_

```json
{
  "parentUuid": "54d6d0a7-2aa1-4d4a-85e6-9e25de6fb263",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2e53fb6c-afed-4b82-bca6-136dbf815f34",
  "timestamp": "2026-05-13T04:37:45.678Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 54 · 2026-05-13T04:37:48.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F9HwNeHUPDjYJM8ZmXacmC`</summary>

```json
{
  "query": "ETA-VLA efficient token adaptation temporal fusion VLA robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e53fb6c-afed-4b82-bca6-136dbf815f34",
  "isSidechain": false,
  "requestId": "req_011Cayx1XFK5ZmvMmsmspS9P",
  "type": "assistant",
  "uuid": "7fbc7248-0b9f-4ac8-aa9c-8fd168cfd972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMWKrRVqpj5poPrhfbtYE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 42311,
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
          "cache_read_input_tokens": 42311,
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

_source line 55 · 2026-05-13T04:37:56.562Z_

<details><summary>↩ Tool result · `toolu_01F9HwNeHUPDjYJM8ZmXacmC`</summary>

```text
Web search results for query: "ETA-VLA efficient token adaptation temporal fusion VLA robustness 2026"

Links: [{"title":"ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.25766v1"},{"title":"[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.25766"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for","url":"https://arxiv.org/pdf/2508.19257"},{"title":"ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time","url":"https://arxiv.org/html/2410.06625v1"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, I found comprehensive information about ETA-VLA:

## ETA-VLA Overview

ETA-VLA is an Efficient Temporal Aggregation framework for VLA (Vision-Language-Action) models. The integration of Vision-Language-Action models into autonomous driving systems offers a unified framework for interpreting complex scenes and executing control commands. However, the necessity to incorporate historical multi-view frames for accurate temporal reasoning imposes a severe computational burden, primarily driven by the quadratic complexity of self-attention mechanisms in Large Language Models (LLMs).

## Key Components

ETA-VLA introduces two complementary components: a Temporal Fusion Module (TFM) and an Intra-LLM Sparse Aggregator (ILSA). TFM adaptively fuses multi-frame historical features into a concise representation via transformer and learnable weights, effectively compressing the temporal dimension while preserving critical motion cues.

ILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency.

## Performance and Robustness

ETA-VLA with 35% token pruning establishes a new state-of-the-art with an EPDMS score of 85.0, significantly outperforming established baselines such as VADv2 (76.6), Transfuser (76.7), and prior SOTA methods including the diffusion-based DiffusionDrive (84.3) and GTRS w/ SimScale (84.6). 

On the Navhard benchmark (designed to test robustness in pseudo closed-loop scenarios), ETA-VLA achieves a state-of-the-art EPDMS score of 48.0, substantially outperforming established baselines such as DiffusionDrive (26.0) and Transfuser (23.1), and compared to the previous leading method GTRS w/ SimScale (47.2), ETA-VLA demonstrates superior robustness with a clear margin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fbc7248-0b9f-4ac8-aa9c-8fd168cfd972",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "3366037b-5499-4905-b6be-b98da7db408d",
  "toolUseResult": {
    "query": "ETA-VLA efficient token adaptation temporal fusion VLA robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LKccS2eQWCDB97kGqstJzk",
        "content": [
          {
            "title": "ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.25766v1"
          },
          {
            "title": "[2603.25766] ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.25766"
          },
          {
            "title": "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.19257"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          },
          {
            "title": "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for",
            "url": "https://arxiv.org/pdf/2508.19257"
          },
          {
            "title": "ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time",
            "url": "https://arxiv.org/html/2410.06625v1"
          },
          {
            "title": "[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2508.19257"
          },
          {
            "title": "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching",
            "url": "https://arxiv.org/html/2502.02175"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about ETA-VLA:\n\n## ETA-VLA Overview\n\nETA-VLA is an Efficient Temporal Aggregation framework for VLA (Vision-Language-Action) models. The integration of Vision-Language-Action models into autonomous driving systems offers a unified framework for interpreting complex scenes and executing control commands. However, the necessity to incorporate historical multi-view frames for accurate temporal reasoning imposes a severe computational burden, primarily driven by the quadratic complexity of self-attention mechanisms in Large Language Models (LLMs).\n\n## Key Components\n\nETA-VLA introduces two complementary components: a Temporal Fusion Module (TFM) and an Intra-LLM Sparse Aggregator (ILSA). TFM adaptively fuses multi-frame historical features into a concise representation via transformer and learnable weights, effectively compressing the temporal dimension while preserving critical motion cues.\n\nILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency.\n\n## Performance and Robustness\n\nETA-VLA with 35% token pruning establishes a new state-of-the-art with an EPDMS score of 85.0, significantly outperforming established baselines such as VADv2 (76.6), Transfuser (76.7), and prior SOTA methods including the diffusion-based DiffusionDrive (84.3) and GTRS w/ SimScale (84.6). \n\nOn the Navhard benchmark (designed to test robustness in pseudo closed-loop scenarios), ETA-VLA achieves a state-of-the-art EPDMS score of 48.0, substantially outperforming established baselines such as DiffusionDrive (26.0) and Transfuser (23.1), and compared to the previous leading method GTRS w/ SimScale (47.2), ETA-VLA demonstrates superior robustness with a clear margin."
    ],
    "durationSeconds": 8.067117734
  },
  "sourceToolAssistantUUID": "7fbc7248-0b9f-4ac8-aa9c-8fd168cfd972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3366037b-5499-4905-b6be-b98da7db408d",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 58 · 2026-05-13T04:37:59.433Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LqnogxkRKnoRd32Pb4WLdK`</summary>

```json
{
  "query": "token pruning random baseline outperforms attention-based pruning MLLM arXiv 2502.11501"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3366037b-5499-4905-b6be-b98da7db408d",
  "isSidechain": false,
  "requestId": "req_011Cayx2KrEZ5T9qgwoBoaN3",
  "type": "assistant",
  "uuid": "c329210a-7171-4547-b2a2-5bcd73546ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur2Dzj4WtqAQV66rBX8Na9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 43396,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 43396,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1065
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

_source line 59 · 2026-05-13T04:38:06.013Z_

<details><summary>↩ Tool result · `toolu_01LqnogxkRKnoRd32Pb4WLdK`</summary>

```text
Web search results for query: "token pruning random baseline outperforms attention-based pruning MLLM arXiv 2502.11501"

Links: [{"title":"[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://arxiv.org/abs/2502.11501"},{"title":"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://arxiv.org/html/2502.11501"},{"title":"[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"http://export.arxiv.org/abs/2502.11501"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://arxiv.org/pdf/2502.11501"},{"title":"Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs","url":"https://arxiv.org/html/2506.10967v1"},{"title":"Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? | Request PDF","url":"https://www.researchgate.net/publication/389090854_Token_Pruning_in_Multimodal_Large_Language_Models_Are_We_Solving_the_Right_Problem"},{"title":"[Literature Review] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?","url":"https://www.themoonlight.io/en/review/token-pruning-in-multimodal-large-language-models-are-we-solving-the-right-problem"},{"title":"D²Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning","url":"https://arxiv.org/html/2512.19443"},{"title":"Treat Visual Tokens as Text? But Your MLLM Only Needs Fewer Efforts to See","url":"https://arxiv.org/pdf/2410.06169"},{"title":"QAPruner: Quantization-Aware Vision Token Pruning for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.02816"}]

I found the arXiv paper 2502.11501 you were searching for. Here are the key findings:

## Paper Overview

The paper addresses multimodal large language models (MLLMs) which suffer from severe inference costs, and investigates token pruning methods that identify and prune redundant tokens to reduce computation and KV storage costs without training.

## Key Finding: Random Baseline Outperforming Attention-Based Methods

The paper asks a critical question: "Why do many existing approaches underperform even compared to naive random token selection?" 

On several common datasets, the performance of FastV and SparseVLM is even worse than random token dropping and pooling.

## Fundamental Questions About Current Approaches

The paper raises several important questions about token pruning methodology:

- Are attention-based scoring sufficient for reliably identifying redundant tokens?
- Is language information really helpful during token pruning?
- What makes a good trade-off between token importance and duplication?

## Insights from Results

The paper reveals that simple approaches often yield better retention of important information than more complex ones, and random and pooling methods maintain better spatial uniformity, leading to better comprehension of visual scenes compared to incumbent pruning techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c329210a-7171-4547-b2a2-5bcd73546ab1",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "be47f90d-f0e1-4873-853d-50896b1197b8",
  "toolUseResult": {
    "query": "token pruning random baseline outperforms attention-based pruning MLLM arXiv 2502.11501",
    "results": [
      {
        "tool_use_id": "srvtoolu_016heqrABmp7UzXYAwqXbpZu",
        "content": [
          {
            "title": "[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?",
            "url": "https://arxiv.org/abs/2502.11501"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?",
            "url": "https://arxiv.org/html/2502.11501"
          },
          {
            "title": "[2502.11501] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?",
            "url": "http://export.arxiv.org/abs/2502.11501"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models",
            "url": "https://arxiv.org/pdf/2502.11501"
          },
          {
            "title": "Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs",
            "url": "https://arxiv.org/html/2506.10967v1"
          },
          {
            "title": "Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem? | Request PDF",
            "url": "https://www.researchgate.net/publication/389090854_Token_Pruning_in_Multimodal_Large_Language_Models_Are_We_Solving_the_Right_Problem"
          },
          {
            "title": "[Literature Review] Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?",
            "url": "https://www.themoonlight.io/en/review/token-pruning-in-multimodal-large-language-models-are-we-solving-the-right-problem"
          },
          {
            "title": "D²Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning",
            "url": "https://arxiv.org/html/2512.19443"
          },
          {
            "title": "Treat Visual Tokens as Text? But Your MLLM Only Needs Fewer Efforts to See",
            "url": "https://arxiv.org/pdf/2410.06169"
          },
          {
            "title": "QAPruner: Quantization-Aware Vision Token Pruning for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2604.02816"
          }
        ]
      },
      "I found the arXiv paper 2502.11501 you were searching for. Here are the key findings:\n\n## Paper Overview\n\nThe paper addresses multimodal large language models (MLLMs) which suffer from severe inference costs, and investigates token pruning methods that identify and prune redundant tokens to reduce computation and KV storage costs without training.\n\n## Key Finding: Random Baseline Outperforming Attention-Based Methods\n\nThe paper asks a critical question: \"Why do many existing approaches underperform even compared to naive random token selection?\" \n\nOn several common datasets, the performance of FastV and SparseVLM is even worse than random token dropping and pooling.\n\n## Fundamental Questions About Current Approaches\n\nThe paper raises several important questions about token pruning methodology:\n\n- Are attention-based scoring sufficient for reliably identifying redundant tokens?\n- Is language information really helpful during token pruning?\n- What makes a good trade-off between token importance and duplication?\n\n## Insights from Results\n\nThe paper reveals that simple approaches often yield better retention of important information than more complex ones, and random and pooling methods maintain better spatial uniformity, leading to better comprehension of visual scenes compared to incumbent pruning techniques."
    ],
    "durationSeconds": 6.576187923999998
  },
  "sourceToolAssistantUUID": "c329210a-7171-4547-b2a2-5bcd73546ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-13T04:38:09.192Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFyzrbbt5ggMqgmLLyKjQ5`</summary>

```json
{
  "query": "AVA-VLA active visual attention VLA arXiv 2511.18960 LIBERO-Plus 74.7%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be47f90d-f0e1-4873-853d-50896b1197b8",
  "isSidechain": false,
  "requestId": "req_011Cayx32FbwHG3Gn1d8mD9g",
  "type": "assistant",
  "uuid": "bae1f895-64f7-4c9d-9628-e1a9b2496654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PP2dEwfXq58Lk5xrpwfsXF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 44461,
      "output_tokens": 81,
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
          "output_tokens": 81,
          "cache_read_input_tokens": 44461,
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

_source line 61 · 2026-05-13T04:38:16.398Z_

<details><summary>↩ Tool result · `toolu_01SFyzrbbt5ggMqgmLLyKjQ5`</summary>

```text
Web search results for query: "AVA-VLA active visual attention VLA arXiv 2511.18960 LIBERO-Plus 74.7%"

Links: [{"title":"[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/abs/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251118960X/abstract"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://www.researchgate.net/publication/397934001_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.18960v1"},{"title":"Recursive Belief Vision Language Action Model","url":"https://arxiv.org/html/2602.20659v1"},{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation","url":"https://arxiv.org/html/2601.08325"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://arxiv.org/list/cs.CV/2025?skip=33700&show=250"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"}]

I found the paper! Here's the information about **AVA-VLA**:

## Overview

AVA-VLA is authored by Lei Xiao, Jifeng Li, Juntao Gao, Feiyang Ye, Yan Jin, Jingjing Qian, Jing Zhang, Yong Wu, and Xiaoyuan Yu, with the paper available on arXiv as 2511.18960.

## Key Contribution

The paper reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and proposes AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history.

## Active Visual Attention Mechanism

Built on this recurrent state, the work introduces Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history.

## Problem Addressed

The paper addresses the fact that most VLA methods process visual observations independently at each timestep, with this history-agnostic design treating robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions.

The paper appears to be a recent contribution to improving Vision-Language-Action models for robotic manipulation by incorporating temporal reasoning and dynamic visual attention mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bae1f895-64f7-4c9d-9628-e1a9b2496654",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "a1ff8ad7-25ea-4991-9e97-898250b21d43",
  "toolUseResult": {
    "query": "AVA-VLA active visual attention VLA arXiv 2511.18960 LIBERO-Plus 74.7%",
    "results": [
      {
        "tool_use_id": "srvtoolu_0177jJqqgXk2A4R1GFTdH487",
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
            "title": "Recursive Belief Vision Language Action Model",
            "url": "https://arxiv.org/html/2602.20659v1"
          },
          {
            "title": "Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2603.23202v1"
          },
          {
            "title": "ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation",
            "url": "https://arxiv.org/html/2601.08325"
          },
          {
            "title": "Computer Vision and Pattern Recognition 2025",
            "url": "https://arxiv.org/list/cs.CV/2025?skip=33700&show=250"
          },
          {
            "title": "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.28740"
          }
        ]
      },
      "I found the paper! Here's the information about **AVA-VLA**:\n\n## Overview\n\nAVA-VLA is authored by Lei Xiao, Jifeng Li, Juntao Gao, Feiyang Ye, Yan Jin, Jingjing Qian, Jing Zhang, Yong Wu, and Xiaoyuan Yu, with the paper available on arXiv as 2511.18960.\n\n## Key Contribution\n\nThe paper reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and proposes AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history.\n\n## Active Visual Attention Mechanism\n\nBuilt on this recurrent state, the work introduces Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history.\n\n## Problem Addressed\n\nThe paper addresses the fact that most VLA methods process visual observations independently at each timestep, with this history-agnostic design treating robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions.\n\nThe paper appears to be a recent contribution to improving Vision-Language-Action models for robotic manipulation by incorporating temporal reasoning and dynamic visual attention mechanisms."
    ],
    "durationSeconds": 7.201098058000003
  },
  "sourceToolAssistantUUID": "bae1f895-64f7-4c9d-9628-e1a9b2496654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-13T04:38:19.815Z_

Now let me fetch the SRPO paper to verify the exact LIBERO-Plus numbers claimed, and check for the most recent LIBERO-Plus leaderboard.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1ff8ad7-25ea-4991-9e97-898250b21d43",
  "isSidechain": false,
  "requestId": "req_011Cayx3ngK15Bd4dUsTbRAS",
  "type": "assistant",
  "uuid": "efa51610-17f1-441c-8fec-4c18498a4f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145qCTQ42coG3bT1Fi8Jo3H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 45388,
      "output_tokens": 163,
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
          "output_tokens": 163,
          "cache_read_input_tokens": 45388,
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

### Tool call

_source line 63 · 2026-05-13T04:38:21.247Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CaSHsYmWF1ntxK8Hs2gcF8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.15605",
  "prompt": "What are the exact LIBERO-Plus benchmark results? What is the average success rate on LIBERO-Plus? Is 82.1% mentioned? List all specific numerical results on LIBERO-Plus."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efa51610-17f1-441c-8fec-4c18498a4f17",
  "isSidechain": false,
  "requestId": "req_011Cayx3ngK15Bd4dUsTbRAS",
  "type": "assistant",
  "uuid": "7b1b5466-7986-4fb6-9da4-e26aab9eb4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145qCTQ42coG3bT1Fi8Jo3H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 45388,
      "output_tokens": 163,
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
          "output_tokens": 163,
          "cache_read_input_tokens": 45388,
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

_source line 64 · 2026-05-13T04:38:24.348Z_

<details><summary>↩ Tool result · `toolu_01CaSHsYmWF1ntxK8Hs2gcF8`</summary>

```text
# LIBERO-Plus Benchmark Results

Based on the provided content, specific numerical results for LIBERO-Plus are **not detailed**. The abstract only states:

"SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark."

The text does **not mention** an 82.1% success rate or provide an exact average success rate on LIBERO-Plus. Only the relative improvement percentage (167%) is given, without baseline or final absolute performance numbers for that benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b1b5466-7986-4fb6-9da4-e26aab9eb4e2",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "cf44815b-ed61-4b49-8c91-ed6b2a557cbc",
  "toolUseResult": {
    "bytes": 48637,
    "code": 200,
    "codeText": "OK",
    "result": "# LIBERO-Plus Benchmark Results\n\nBased on the provided content, specific numerical results for LIBERO-Plus are **not detailed**. The abstract only states:\n\n\"SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark.\"\n\nThe text does **not mention** an 82.1% success rate or provide an exact average success rate on LIBERO-Plus. Only the relative improvement percentage (167%) is given, without baseline or final absolute performance numbers for that benchmark.",
    "durationMs": 3097,
    "url": "https://arxiv.org/abs/2511.15605"
  },
  "sourceToolAssistantUUID": "7b1b5466-7986-4fb6-9da4-e26aab9eb4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-13T04:38:26.955Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AbvEb1zJxeBNzcsw9wGCea`</summary>

```json
{
  "query": "SRPO LIBERO-Plus absolute success rate 82% results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf44815b-ed61-4b49-8c91-ed6b2a557cbc",
  "isSidechain": false,
  "requestId": "req_011Cayx4NdE9o34UZYKnkJgY",
  "type": "assistant",
  "uuid": "2e38b9c9-05da-433f-bfad-8b4630f44e78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1qu8pASrWwxMjQordQccD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 46315,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 46315,
          "cache_creation_input_tokens": 288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 288
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

_source line 66 · 2026-05-13T04:38:31.153Z_

<details><summary>↩ Tool result · `toolu_01AbvEb1zJxeBNzcsw9wGCea`</summary>

```text
Web search results for query: "SRPO LIBERO-Plus absolute success rate 82% results table"

Links: [{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"},{"title":"Case Studies of Foundation Model Integration in Embodied ...","url":"https://aclanthology.org/2025.findings-emnlp.69.pdf"},{"title":"Average success rate across evaluation settings on LIBERO and... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Average-success-rate-across-evaluation-settings-on-LIBERO-and-MetaWorld-v2-All-results_tbl1_397006917"},{"title":"SFK Libero live score, schedule & player stats","url":"https://www.sofascore.com/football/team/sfk-libero/1090942"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"}]

I found search results related to SRPO and LIBERO benchmarks. Based on the results, SRPO shows significant robustness on the LIBERO-Plus benchmark, achieving a 167% performance gain. However, the search results don't contain a specific results table showing an 82% absolute success rate on LIBERO-Plus.

The search results do show that SRPO demonstrates state-of-the-art performance on the LIBERO benchmark, achieving a 99.2% success rate, but this is for the standard LIBERO benchmark rather than LIBERO-Plus with the specific 82% figure you're asking about.

If you're looking for a more detailed results table with the 82% success rate figure, you may need to access the original SRPO research paper or technical documentation directly, as the specific table doesn't appear in these particular search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e38b9c9-05da-433f-bfad-8b4630f44e78",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "998f36cf-8ccc-44e2-b1e3-afc698216e8f",
  "toolUseResult": {
    "query": "SRPO LIBERO-Plus absolute success rate 82% results table",
    "results": [
      {
        "tool_use_id": "srvtoolu_015r9CPRHQ8DEGAXjGCuNcSN",
        "content": [
          {
            "title": "[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"
          },
          {
            "title": "SRPO Code Implementation Explained — siiRL documentation",
            "url": "https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"
          },
          {
            "title": "LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-Object: Lifelong Learning in Robotic Manipulation",
            "url": "https://www.emergentmind.com/topics/libero-object"
          },
          {
            "title": "Case Studies of Foundation Model Integration in Embodied ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.69.pdf"
          },
          {
            "title": "Average success rate across evaluation settings on LIBERO and... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Average-success-rate-across-evaluation-settings-on-LIBERO-and-MetaWorld-v2-All-results_tbl1_397006917"
          },
          {
            "title": "SFK Libero live score, schedule & player stats",
            "url": "https://www.sofascore.com/football/team/sfk-libero/1090942"
          },
          {
            "title": "PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/711"
          }
        ]
      },
      "I found search results related to SRPO and LIBERO benchmarks. Based on the results, SRPO shows significant robustness on the LIBERO-Plus benchmark, achieving a 167% performance gain. However, the search results don't contain a specific results table showing an 82% absolute success rate on LIBERO-Plus.\n\nThe search results do show that SRPO demonstrates state-of-the-art performance on the LIBERO benchmark, achieving a 99.2% success rate, but this is for the standard LIBERO benchmark rather than LIBERO-Plus with the specific 82% figure you're asking about.\n\nIf you're looking for a more detailed results table with the 82% success rate figure, you may need to access the original SRPO research paper or technical documentation directly, as the specific table doesn't appear in these particular search results."
    ],
    "durationSeconds": 4.194814687000005
  },
  "sourceToolAssistantUUID": "2e38b9c9-05da-433f-bfad-8b4630f44e78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-13T04:38:34.315Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VVz2aBax5SMxEY8dMkn6PD`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.15605v2",
  "prompt": "Find the LIBERO-Plus results table. What is SRPO's average success rate on LIBERO-Plus? What baselines are compared? List all numerical results on LIBERO-Plus. Is there an 82.1% number?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998f36cf-8ccc-44e2-b1e3-afc698216e8f",
  "isSidechain": false,
  "requestId": "req_011Cayx4sgiUtLWTGYGPvLmv",
  "type": "assistant",
  "uuid": "d56c21aa-056c-47f2-a50b-7d735977bee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J45eN8UVayMZL2boXejiZ2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 46603,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 46603,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 835
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

_source line 68 · 2026-05-13T04:38:38.745Z_

<details><summary>↩ Tool result · `toolu_01VVz2aBax5SMxEY8dMkn6PD`</summary>

```text
# LIBERO-Plus Results Analysis

## SRPO's Average Success Rate

SRPO achieves **82.1%** average success rate on LIBERO-Plus (with augmented data), as shown in Table 2.

## Baselines Compared

The comparison includes:
- Pi0 and Pi0+fast (zero-shot imitation learning)
- UniVLA, WorldVLA, OpenVLA variants
- NORA-long and RIPT-VLA
- OpenVLA-OFT and OpenVLA-OFT+ (with augmented data)

## LIBERO-Plus Numerical Results (SRPO with Augmented Data)

| Dimension | Performance |
|-----------|------------|
| Camera | 62.0% |
| Robot-Init | 73.6% |
| Language | 97.2% |
| Light | 97.7% |
| Background | 85.7% |
| Noise | 75.2% |
| Layout | 82.1% |
| **Average** | **82.1%** |

Yes, the **82.1% figure appears as both the Layout dimension score and the overall average** for SRPO with augmented data training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d56c21aa-056c-47f2-a50b-7d735977bee5",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "260b3a6e-cb79-4a76-9973-7e5d1048f501",
  "toolUseResult": {
    "bytes": 250921,
    "code": 200,
    "codeText": "OK",
    "result": "# LIBERO-Plus Results Analysis\n\n## SRPO's Average Success Rate\n\nSRPO achieves **82.1%** average success rate on LIBERO-Plus (with augmented data), as shown in Table 2.\n\n## Baselines Compared\n\nThe comparison includes:\n- Pi0 and Pi0+fast (zero-shot imitation learning)\n- UniVLA, WorldVLA, OpenVLA variants\n- NORA-long and RIPT-VLA\n- OpenVLA-OFT and OpenVLA-OFT+ (with augmented data)\n\n## LIBERO-Plus Numerical Results (SRPO with Augmented Data)\n\n| Dimension | Performance |\n|-----------|------------|\n| Camera | 62.0% |\n| Robot-Init | 73.6% |\n| Language | 97.2% |\n| Light | 97.7% |\n| Background | 85.7% |\n| Noise | 75.2% |\n| Layout | 82.1% |\n| **Average** | **82.1%** |\n\nYes, the **82.1% figure appears as both the Layout dimension score and the overall average** for SRPO with augmented data training.",
    "durationMs": 4427,
    "url": "https://arxiv.org/html/2511.15605v2"
  },
  "sourceToolAssistantUUID": "d56c21aa-056c-47f2-a50b-7d735977bee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-13T04:38:41.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015H1gP8oUM8e7GdFi37iWEb`</summary>

```json
{
  "query": "LIBERO-Plus leaderboard SOTA 2026 latest results beyond SRPO 82%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "260b3a6e-cb79-4a76-9973-7e5d1048f501",
  "isSidechain": false,
  "requestId": "req_011Cayx5SA5air9Ht9senxHr",
  "type": "assistant",
  "uuid": "262777bf-ad4a-4fb1-adba-1f4b0bb0571d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjRjA46q6J9177ZBp9ccwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 47438,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 47438,
          "cache_creation_input_tokens": 431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 431
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

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "262777bf-ad4a-4fb1-adba-1f4b0bb0571d",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool result

_source line 72 · 2026-05-13T04:38:52.876Z_

<details><summary>↩ Tool result · `toolu_015H1gP8oUM8e7GdFi37iWEb`</summary>

```text
Web search results for query: "LIBERO-Plus leaderboard SOTA 2026 latest results beyond SRPO 82%"

Links: [{"title":"Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/speech"},{"title":"VLA & Dexterous Manipulation SOTA Leaderboard","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"2026 Senior PGA Championship Leaderboard | Senior PGA Championship","url":"https://www.srpgachampionship.com/leaderboard"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"}]

I found references to LIBERO-Plus in the search results. Let me search more specifically for the latest LIBERO-Plus leaderboard results and SRPO performance data.

Links: [{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Robotics AI Benchmarks 2026: State of the Art | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/robotics"},{"title":"ABB Robotics Division IPO Planned for Q2 2026 | robotics.press","url":"https://robotics.press/news/abb-robotics-ipo-q2-2026-valuation-benchmark/"},{"title":"GitHub - robotperf/benchmarks: Benchmarking suite to evaluate 🤖 robotics computing performance. Vendor-neutral. ⚪Grey-box and ⚫Black-box approaches.","url":"https://github.com/robotperf/benchmarks"},{"title":"2026 robotics and automation predictions: Top trends transforming global industries - Robotics 24/7","url":"https://www.robotics247.com/article/2026-robotics-and-automation-predictions-top-trends-transforming-global-industries/technologies"},{"title":"2026 State of Robotics Report - F-Prime Capital","url":"https://fprimecapital.com/blog/robotics-2026/"},{"title":"State of robotics industry report 2026","url":"https://www.therobotreport.com/state-of-robotics-industry-report-2026/"},{"title":"Positronic Robotics launches ‘PhAIL’ benchmark to test real-world performance of physical AI systems","url":"https://roboticsandautomationnews.com/2026/03/31/positronic-robotics-launches-phail-benchmark-to-test-real-world-performance-of-physical-ai-systems/100214/"},{"title":"Global Robotics Report 2026 | StartUs Insights","url":"https://www.startus-insights.com/innovators-guide/robotics-report/"}]

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"}]

Let me search for more recent LIBERO-Plus leaderboard results to find methods beyond the 82% SRPO threshold.

Links: [{"title":"VLA & Dexterous Manipulation SOTA Leaderboard","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"GitHub - MINT-SJTU/Evo-SOTA.io: This website is for the collection of VLA SOTA results. · GitHub","url":"https://github.com/MINT-SJTU/Evo-SOTA.io"},{"title":"Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LiveCodeBench Leaderboard - Holistic and Contamination Free Evaluation","url":"https://livecodebench.github.io/leaderboard.html"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"}]

Based on my search results, I found information about LIBERO-Plus and SRPO, though the specific detailed leaderboard with results beyond the 82% SRPO benchmark is not directly accessible through these searches. Here's what I found:

## LIBERO-Plus Benchmark Overview

LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions: Camera, Robot, Language, Light, Background, Noise, and Layout. LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities, with a systematic two-stage process involving expanding the original LIBERO benchmark through seven distinct perturbation factors and evaluating tasks using representative models stratified into five difficulty levels.

## SRPO Performance

SRPO demonstrates state-of-the-art performance on the LIBERO benchmark, achieving a 99.2% success rate, which represents a 103% relative improvement over its one-shot supervised fine-tuning (SFT) baseline. However, this refers to the original LIBERO benchmark rather than LIBERO-Plus specifically.

## Available Leaderboard Resource

The VLA SOTA leaderboard at sota.evomind-tech.com tracks LIBERO Plus with extended LIBERO with 6 robustness categories (camera, robot, language, light, background, layout) measuring Average Success Rate (%).

Unfortunately, the search results don't provide the specific detailed leaderboard results showing methods that exceed the 82% SRPO threshold on LIBERO-Plus. For the latest complete leaderboard with current rankings beyond the SRPO 82% baseline, you would need to visit the live leaderboard directly at **sota.evomind-tech.com** or check the official LIBERO-Plus repository at **github.com/sylvestf/LIBERO-plus**.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "262777bf-ad4a-4fb1-adba-1f4b0bb0571d",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "3d240154-35f9-4b76-ac1c-b29c00a5d0e9",
  "toolUseResult": {
    "query": "LIBERO-Plus leaderboard SOTA 2026 latest results beyond SRPO 82%",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HwVxgAemxfjcAqyRhsaJwj",
        "content": [
          {
            "title": "Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"
          },
          {
            "title": "LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/llm"
          },
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/"
          },
          {
            "title": "Codesota — the open, callable registry of SOTA",
            "url": "https://www.codesota.com/"
          },
          {
            "title": "AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/code-generation"
          },
          {
            "title": "Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/speech"
          },
          {
            "title": "VLA & Dexterous Manipulation SOTA Leaderboard",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "2026 Senior PGA Championship Leaderboard | Senior PGA Championship",
            "url": "https://www.srpgachampionship.com/leaderboard"
          },
          {
            "title": "LLM Leaderboard 2026 — Compare Top AI Models - Vellum",
            "url": "https://www.vellum.ai/llm-leaderboard"
          }
        ]
      },
      "I found references to LIBERO-Plus in the search results. Let me search more specifically for the latest LIBERO-Plus leaderboard results and SRPO performance data.",
      {
        "tool_use_id": "srvtoolu_01QHiLyxPkUNEnwkeVqs5q2d",
        "content": [
          {
            "title": "[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"
          },
          {
            "title": "State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/state-of-robotics-2026"
          },
          {
            "title": "Robotics AI Benchmarks 2026: State of the Art | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/robotics"
          },
          {
            "title": "ABB Robotics Division IPO Planned for Q2 2026 | robotics.press",
            "url": "https://robotics.press/news/abb-robotics-ipo-q2-2026-valuation-benchmark/"
          },
          {
            "title": "GitHub - robotperf/benchmarks: Benchmarking suite to evaluate 🤖 robotics computing performance. Vendor-neutral. ⚪Grey-box and ⚫Black-box approaches.",
            "url": "https://github.com/robotperf/benchmarks"
          },
          {
            "title": "2026 robotics and automation predictions: Top trends transforming global industries - Robotics 24/7",
            "url": "https://www.robotics247.com/article/2026-robotics-and-automation-predictions-top-trends-transforming-global-industries/technologies"
          },
          {
            "title": "2026 State of Robotics Report - F-Prime Capital",
            "url": "https://fprimecapital.com/blog/robotics-2026/"
          },
          {
            "title": "State of robotics industry report 2026",
            "url": "https://www.therobotreport.com/state-of-robotics-industry-report-2026/"
          },
          {
            "title": "Positronic Robotics launches ‘PhAIL’ benchmark to test real-world performance of physical AI systems",
            "url": "https://roboticsandautomationnews.com/2026/03/31/positronic-robotics-launches-phail-benchmark-to-test-real-world-performance-of-physical-ai-systems/100214/"
          },
          {
            "title": "Global Robotics Report 2026 | StartUs Insights",
            "url": "https://www.startus-insights.com/innovators-guide/robotics-report/"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_012iquxJw9TnKbEK99Z8GyH3",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "Sylvest/LIBERO-plus · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus"
          }
        ]
      },
      "Let me search for more recent LIBERO-Plus leaderboard results to find methods beyond the 82% SRPO threshold.",
      {
        "tool_use_id": "srvtoolu_01Q1tcQoFp45hDgPvPdZmkbW",
        "content": [
          {
            "title": "VLA & Dexterous Manipulation SOTA Leaderboard",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"
          },
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/"
          },
          {
            "title": "GitHub - MINT-SJTU/Evo-SOTA.io: This website is for the collection of VLA SOTA results. · GitHub",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io"
          },
          {
            "title": "Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"
          },
          {
            "title": "LLM Leaderboard 2026 — Compare Top AI Models - Vellum",
            "url": "https://www.vellum.ai/llm-leaderboard"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/llm"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "LiveCodeBench Leaderboard - Holistic and Contamination Free Evaluation",
            "url": "https://livecodebench.github.io/leaderboard.html"
          },
          {
            "title": "Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings",
            "url": "https://llm-stats.com/leaderboards/open-llm-leaderboard"
          }
        ]
      },
      "Based on my search results, I found information about LIBERO-Plus and SRPO, though the specific detailed leaderboard with results beyond the 82% SRPO benchmark is not directly accessible through these searches. Here's what I found:\n\n## LIBERO-Plus Benchmark Overview\n\nLIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions: Camera, Robot, Language, Light, Background, Noise, and Layout. LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities, with a systematic two-stage process involving expanding the original LIBERO benchmark through seven distinct perturbation factors and evaluating tasks using representative models stratified into five difficulty levels.\n\n## SRPO Performance\n\nSRPO demonstrates state-of-the-art performance on the LIBERO benchmark, achieving a 99.2% success rate, which represents a 103% relative improvement over its one-shot supervised fine-tuning (SFT) baseline. However, this refers to the original LIBERO benchmark rather than LIBERO-Plus specifically.\n\n## Available Leaderboard Resource\n\nThe VLA SOTA leaderboard at sota.evomind-tech.com tracks LIBERO Plus with extended LIBERO with 6 robustness categories (camera, robot, language, light, background, layout) measuring Average Success Rate (%).\n\nUnfortunately, the search results don't provide the specific detailed leaderboard results showing methods that exceed the 82% SRPO threshold on LIBERO-Plus. For the latest complete leaderboard with current rankings beyond the SRPO 82% baseline, you would need to visit the live leaderboard directly at **sota.evomind-tech.com** or check the official LIBERO-Plus repository at **github.com/sylvestf/LIBERO-plus**."
    ],
    "durationSeconds": 11.619165842000017
  },
  "sourceToolAssistantUUID": "262777bf-ad4a-4fb1-adba-1f4b0bb0571d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-13T04:38:56.578Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CYaHax1s86Ffxr73isstAM`</summary>

```json
{
  "url": "https://sota.evomind-tech.com/",
  "prompt": "Find the LIBERO-Plus leaderboard. What is the current top-performing method on LIBERO-Plus? What success rates are reported? List all methods and their average success rates on LIBERO-Plus. Has any method surpassed 82.1%?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d240154-35f9-4b76-ac1c-b29c00a5d0e9",
  "isSidechain": false,
  "requestId": "req_011Cayx6UcwgPngks2j4cVXf",
  "type": "assistant",
  "uuid": "cb5b0e4b-0b01-465e-8fc5-b1560f502463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxeiUW1jtTKrVUPFC1cHJJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 47869,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 47869,
          "cache_creation_input_tokens": 2204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2204
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

_source line 74 · 2026-05-13T04:38:58.907Z_

<details><summary>↩ Tool result · `toolu_01CYaHax1s86Ffxr73isstAM`</summary>

```text
Based on the web page content provided, I cannot answer your questions about the LIBERO-Plus leaderboard performance metrics.

The page shows that "LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions" with "Average Success Rate (%)" as the primary metric. However, the section displays "0 Models" and does not include any actual leaderboard data, top-performing methods, success rates, or comparative results.

To find this information, you would need to visit the full leaderboard at `/benchmarks/liberoplus/`, which is not shown in the current page content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb5b0e4b-0b01-465e-8fc5-b1560f502463",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "0877641e-842e-4871-a108-6ba199112946",
  "toolUseResult": {
    "bytes": 26531,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot answer your questions about the LIBERO-Plus leaderboard performance metrics.\n\nThe page shows that \"LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions\" with \"Average Success Rate (%)\" as the primary metric. However, the section displays \"0 Models\" and does not include any actual leaderboard data, top-performing methods, success rates, or comparative results.\n\nTo find this information, you would need to visit the full leaderboard at `/benchmarks/liberoplus/`, which is not shown in the current page content.",
    "durationMs": 2325,
    "url": "https://sota.evomind-tech.com/"
  },
  "sourceToolAssistantUUID": "cb5b0e4b-0b01-465e-8fc5-b1560f502463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-13T04:39:01.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019as938VtpfAK6WPy4EeiaM`</summary>

```json
{
  "query": "FTM FLA LIBERO-Plus results feature token modulation full benchmark 7 dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0877641e-842e-4871-a108-6ba199112946",
  "isSidechain": false,
  "requestId": "req_011Cayx6vMFniXHeoV1REWa9",
  "type": "assistant",
  "uuid": "14de1247-b196-48ac-b9e5-6a09a119d744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJgyqZgkDgbhsCunAdobXH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 50073,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 50073,
          "cache_creation_input_tokens": 285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 285
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

_source line 76 · 2026-05-13T04:39:09.649Z_

<details><summary>↩ Tool result · `toolu_019as938VtpfAK6WPy4EeiaM`</summary>

```text
Web search results for query: "FTM FLA LIBERO-Plus results feature token modulation full benchmark 7 dimensions"

Links: [{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902"},{"title":"Feature Token Modulation (FTM)","url":"https://www.emergentmind.com/topics/feature-token-modulation-ftm"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Fantom Token (FTM) Overview - ADVFN","url":"https://www.advfn.com/crypto/Fantom-FTM/overview"},{"title":"Fantom Libero Financial price today, FLIBERO to USD live price, marketcap and chart | CoinMarketCap","url":"https://coinmarketcap.com/currencies/fantom-libero-financial/"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"}]

Based on the search results, I found relevant information about FTM, FLA, and LIBERO-Plus benchmarking:

## FTM and FLA Methods

Feature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters—matching LoRA-scale finetuning at far lower cost.

## LIBERO-Plus Seven Dimensions

LIBERO-Plus systematically exposes the hidden vulnerabilities of contemporary VLA models through comprehensive robustness evaluation across seven perturbation dimensions. The benchmark includes multiple types of perturbations affecting vision-language-action models' robustness.

## Key Results

Across the Libero-V benchmarks, the framework achieves state-of-the-art generalization under novel camera viewpoints and diverse visual perturbations, while being up to 99× more parameter-efficient than LoRA fine-tuning.

The research demonstrates that lightweight feature adaptation mechanisms like FTM and FLA can effectively address distribution shifts in vision-language-action models without requiring substantial parameter overhead, particularly for viewpoint and visual perturbation robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14de1247-b196-48ac-b9e5-6a09a119d744",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "72877a85-5d1b-49a4-8f8a-568c8abc2e0f",
  "toolUseResult": {
    "query": "FTM FLA LIBERO-Plus results feature token modulation full benchmark 7 dimensions",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ww4AXzccjW7qLURCjrHBYW",
        "content": [
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902"
          },
          {
            "title": "Feature Token Modulation (FTM)",
            "url": "https://www.emergentmind.com/topics/feature-token-modulation-ftm"
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
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "Fantom Token (FTM) Overview - ADVFN",
            "url": "https://www.advfn.com/crypto/Fantom-FTM/overview"
          },
          {
            "title": "Fantom Libero Financial price today, FLIBERO to USD live price, marketcap and chart | CoinMarketCap",
            "url": "https://coinmarketcap.com/currencies/fantom-libero-financial/"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/en/libero"
          }
        ]
      },
      "Based on the search results, I found relevant information about FTM, FLA, and LIBERO-Plus benchmarking:\n\n## FTM and FLA Methods\n\nFeature Token Modulation (FTM) applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters—matching LoRA-scale finetuning at far lower cost.\n\n## LIBERO-Plus Seven Dimensions\n\nLIBERO-Plus systematically exposes the hidden vulnerabilities of contemporary VLA models through comprehensive robustness evaluation across seven perturbation dimensions. The benchmark includes multiple types of perturbations affecting vision-language-action models' robustness.\n\n## Key Results\n\nAcross the Libero-V benchmarks, the framework achieves state-of-the-art generalization under novel camera viewpoints and diverse visual perturbations, while being up to 99× more parameter-efficient than LoRA fine-tuning.\n\nThe research demonstrates that lightweight feature adaptation mechanisms like FTM and FLA can effectively address distribution shifts in vision-language-action models without requiring substantial parameter overhead, particularly for viewpoint and visual perturbation robustness."
    ],
    "durationSeconds": 7.647936180999998
  },
  "sourceToolAssistantUUID": "14de1247-b196-48ac-b9e5-6a09a119d744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 77 · 2026-05-13T04:39:09.652Z_

```json
{
  "parentUuid": "72877a85-5d1b-49a4-8f8a-568c8abc2e0f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b964e81b-3a78-4c88-91a8-4a0d627b725c",
  "timestamp": "2026-05-13T04:39:09.652Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 78 · 2026-05-13T04:39:14.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHesjBtWdmympzUBG4TnQH`</summary>

```json
{
  "query": "\"causal token\" \"vision language action\" OR VLA selection pruning robustness invariance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b964e81b-3a78-4c88-91a8-4a0d627b725c",
  "isSidechain": false,
  "requestId": "req_011Cayx7iRgMZ5KS6cV7qpc2",
  "type": "assistant",
  "uuid": "38773612-a302-4356-be87-72e104eb736b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ3UWMDZ21MPWJZqJxuc3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 50358,
      "output_tokens": 78,
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
          "output_tokens": 78,
          "cache_read_input_tokens": 50358,
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

_source line 79 · 2026-05-13T04:39:23.495Z_

<details><summary>↩ Tool result · `toolu_01FHesjBtWdmympzUBG4TnQH`</summary>

```text
Web search results for query: ""causal token" "vision language action" OR VLA selection pruning robustness invariance 2025 2026"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v2"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation ...","url":"https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"}]

I've found several recent papers on Vision-Language-Action (VLA) models with focus on token selection, pruning, robustness, and efficiency. Here's a summary of the key findings:

## Key Research Areas Found:

### 1. **Interaction-Aligned Pruning (VLA-IAP)**
VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment. It achieves a state-of-the-art success rate of 97.8% while maintaining a remarkably low latency of 98.6 ms.

### 2. **Differentiable Token Pruning (LightVLA)**
LightVLA is a differentiable token pruning framework that generates dynamic queries to evaluate visual token importance using Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution. LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.

### 3. **Token Caching (VLA-Cache)**
VLA-Cache incorporates a token-selection mechanism that compares the visual input at each step with the input from the previous step, adaptively identifying visual tokens with minimal changes. VLA-Cache maintained the same success rate while reducing FLOPs by 42% and latency by 35%, highlighting its ability to filter out transient or irrelevant tokens, preserving both efficiency and stability in dynamic real-world settings.

### 4. **Action-Aware Pruning (SpecPrune-VLA)**
SpecPrune-VLA addresses spatial-temporal consistency in VLA tasks and proposes that token selection should combine local information with global context of the model using a training-free, two-level pruning method. It achieves up to 1.57× speedup in simulation and an average of 1.70× speedup in real-world robotic tasks.

### 5. **Hierarchical Token Pruning (BFA++)**
BFA++ introduces two-level importance predictors to identify critical camera views and task-relevant regions, jointly trained with the VLA model, removing redundant tokens while preserving essential manipulation details through hierarchical token pruning.

These papers represent significant recent advances (2025-2026) in making VLA models more efficient while maintaining or improving robustness for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38773612-a302-4356-be87-72e104eb736b",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "340e5da3-5ba5-41b6-be4c-0f9af2b6f22b",
  "toolUseResult": {
    "query": "\"causal token\" \"vision language action\" OR VLA selection pruning robustness invariance 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M4x8AQ5L7NXkN2BDC7FQDR",
        "content": [
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation",
            "url": "https://arxiv.org/html/2502.02175v1"
          },
          {
            "title": "[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v2"
          },
          {
            "title": "VLA-Cache: Efficient Vision-Language-Action Manipulation ...",
            "url": "https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf"
          },
          {
            "title": "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model",
            "url": "https://arxiv.org/html/2602.20566"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview",
            "url": "https://openreview.net/forum?id=t85Ni0LwjC"
          }
        ]
      },
      "I've found several recent papers on Vision-Language-Action (VLA) models with focus on token selection, pruning, robustness, and efficiency. Here's a summary of the key findings:\n\n## Key Research Areas Found:\n\n### 1. **Interaction-Aligned Pruning (VLA-IAP)**\nVLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment. It achieves a state-of-the-art success rate of 97.8% while maintaining a remarkably low latency of 98.6 ms.\n\n### 2. **Differentiable Token Pruning (LightVLA)**\nLightVLA is a differentiable token pruning framework that generates dynamic queries to evaluate visual token importance using Gumbel softmax to enable differentiable token selection, learning to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution. LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.\n\n### 3. **Token Caching (VLA-Cache)**\nVLA-Cache incorporates a token-selection mechanism that compares the visual input at each step with the input from the previous step, adaptively identifying visual tokens with minimal changes. VLA-Cache maintained the same success rate while reducing FLOPs by 42% and latency by 35%, highlighting its ability to filter out transient or irrelevant tokens, preserving both efficiency and stability in dynamic real-world settings.\n\n### 4. **Action-Aware Pruning (SpecPrune-VLA)**\nSpecPrune-VLA addresses spatial-temporal consistency in VLA tasks and proposes that token selection should combine local information with global context of the model using a training-free, two-level pruning method. It achieves up to 1.57× speedup in simulation and an average of 1.70× speedup in real-world robotic tasks.\n\n### 5. **Hierarchical Token Pruning (BFA++)**\nBFA++ introduces two-level importance predictors to identify critical camera views and task-relevant regions, jointly trained with the VLA model, removing redundant tokens while preserving essential manipulation details through hierarchical token pruning.\n\nThese papers represent significant recent advances (2025-2026) in making VLA models more efficient while maintaining or improving robustness for robotic manipulation tasks."
    ],
    "durationSeconds": 9.16568181899999
  },
  "sourceToolAssistantUUID": "38773612-a302-4356-be87-72e104eb736b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "340e5da3-5ba5-41b6-be4c-0f9af2b6f22b",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 82 · 2026-05-13T04:39:27.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PUYpfKFTL5ZLAVry2S14zy`</summary>

```json
{
  "query": "FocusVLA focused visual utilization VLA 2026 robustness token"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340e5da3-5ba5-41b6-be4c-0f9af2b6f22b",
  "isSidechain": false,
  "requestId": "req_011Cayx8jTyFnjPrB5etZobw",
  "type": "assistant",
  "uuid": "ed5e2ca0-1cfa-4ef0-a3ec-fef929e18f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhEyYFquJGRw823uN1uwjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1234,
      "cache_read_input_tokens": 51384,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 51384,
          "cache_creation_input_tokens": 1234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1234
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

_source line 83 · 2026-05-13T04:39:33.839Z_

<details><summary>↩ Tool result · `toolu_01PUYpfKFTL5ZLAVry2S14zy`</summary>

```text
Web search results for query: "FocusVLA focused visual utilization VLA 2026 robustness token"

Links: [{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"[2603.28740] FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.28740"},{"title":"Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"ForeAct: Steering Your VLA with Efficient Visual Foresight Planning","url":"https://arxiv.org/html/2602.12322"},{"title":"[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/abs/2602.01158"},{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"XPENG-Peking University Collaborative Research Accepted by AAAI 2026:","url":"https://www.xpeng.com/pressroom/news/019b649d31c59b49d00d8a028c720027"},{"title":"CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33233"},{"title":"TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/html/2508.19257v1"}]

Based on the search results, I found relevant information about **FocusVLA: Focused Visual Utilization for Vision-Language-Action Models**.

## Overview

FocusVLA is a Vision-Language-Action (VLA) model that improves action generation by conditioning policies on rich vision-language information.

## Key Problem Addressed

Current auto-regressive policies are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise.

## Technical Approach

FocusVLA proposes Modality Cascaded Attention to eliminate shortcut pathways, thereby compelling VLA models to rely on task-relevant visual details for action generation. Furthermore, it proposes Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise.

## Performance and Results

Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.

The paper was published in March 2026 and focuses on solving the visual token utilization problem rather than just improving visual representation quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed5e2ca0-1cfa-4ef0-a3ec-fef929e18f45",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "61070dd2-5e7e-4cf1-80d9-b7595d8fab81",
  "toolUseResult": {
    "query": "FocusVLA focused visual utilization VLA 2026 robustness token",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FCm4gCGBErW2tPDj6kWhNW",
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
            "title": "Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics",
            "url": "https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "ForeAct: Steering Your VLA with Efficient Visual Foresight Planning",
            "url": "https://arxiv.org/html/2602.12322"
          },
          {
            "title": "[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs",
            "url": "https://arxiv.org/abs/2602.01158"
          },
          {
            "title": "Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs",
            "url": "https://arxiv.org/html/2602.01158"
          },
          {
            "title": "XPENG-Peking University Collaborative Research Accepted by AAAI 2026:",
            "url": "https://www.xpeng.com/pressroom/news/019b649d31c59b49d00d8a028c720027"
          },
          {
            "title": "CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2025/poster/33233"
          },
          {
            "title": "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2508.19257v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about **FocusVLA: Focused Visual Utilization for Vision-Language-Action Models**.\n\n## Overview\n\nFocusVLA is a Vision-Language-Action (VLA) model that improves action generation by conditioning policies on rich vision-language information.\n\n## Key Problem Addressed\n\nCurrent auto-regressive policies are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise.\n\n## Technical Approach\n\nFocusVLA proposes Modality Cascaded Attention to eliminate shortcut pathways, thereby compelling VLA models to rely on task-relevant visual details for action generation. Furthermore, it proposes Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise.\n\n## Performance and Results\n\nExtensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.\n\nThe paper was published in March 2026 and focuses on solving the visual token utilization problem rather than just improving visual representation quality."
    ],
    "durationSeconds": 6.262781649999961
  },
  "sourceToolAssistantUUID": "ed5e2ca0-1cfa-4ef0-a3ec-fef929e18f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-13T04:39:37.654Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0115bBEHBxh3E5iHdg894K3X`</summary>

```json
{
  "query": "Gaze-Regularized VLA robotic manipulation visual attention token 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61070dd2-5e7e-4cf1-80d9-b7595d8fab81",
  "isSidechain": false,
  "requestId": "req_011Cayx9VhmDTHi2ZGiH3W19",
  "type": "assistant",
  "uuid": "d229bee1-98c5-4bbd-81a8-107b6e5fc4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrpWGr84LueSq5RfQQN4LS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 52618,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 52618,
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

_source line 85 · 2026-05-13T04:39:45.496Z_

<details><summary>↩ Tool result · `toolu_0115bBEHBxh3E5iHdg894K3X`</summary>

```text
Web search results for query: "Gaze-Regularized VLA robotic manipulation visual attention token 2026 arXiv"

Links: [{"title":"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.23202v1"},{"title":"[2603.23202v1] Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/abs/2603.23202v1"},{"title":"[2603.23202] Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation","url":"https://arxiv.org/abs/2603.23202"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning","url":"https://arxiv.org/html/2605.07817v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2510.21356] Gaze-VLM:Bridging Gaze and VLMs through Attention Regularization for Egocentric Understanding","url":"https://arxiv.org/abs/2510.21356"},{"title":"[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models","url":"https://arxiv.org/abs/2508.19257"},{"title":"[2605.07817] GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning","url":"https://arxiv.org/abs/2605.07817"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"}]

I found the paper you're looking for! Here are the key results:

## Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

Despite advances in Vision-Language-Action (VLA) models, robotic manipulation struggles with fine-grained tasks because current models lack mechanisms for active visual attention allocation.

**The Proposed Method:**

The researchers introduce a gaze-regularized training framework that aligns VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead. The method transforms temporally aggregated gaze heatmaps into patch-level distributions and regularizes the transformer's attention through KL divergence, creating an inductive bias toward task-relevant features while preserving deployment efficiency.

**Results and Benefits:**

When integrated into existing VLA architectures, the approach yields 4-12% improvements across manipulation benchmarks. Beyond performance metrics, the learned attention patterns produce interpretable visualizations that mirror human strategies, enhancing trust in robotic systems. Additionally, the framework requires no eye-tracking equipment and applies directly to existing datasets.

**Paper Details:**
- **arXiv ID:** 2603.23202
- **Published:** March 24, 2026
- **Links:** [Abstract](https://arxiv.org/abs/2603.23202) | [HTML Version](https://arxiv.org/html/2603.23202v1)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d229bee1-98c5-4bbd-81a8-107b6e5fc4ca",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "820bf50d-173a-4c0e-86f3-1395363d5293",
  "toolUseResult": {
    "query": "Gaze-Regularized VLA robotic manipulation visual attention token 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JxVWUSYmvgZyqs47HRWcAh",
        "content": [
          {
            "title": "Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2603.23202v1"
          },
          {
            "title": "[2603.23202v1] Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/abs/2603.23202v1"
          },
          {
            "title": "[2603.23202] Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation",
            "url": "https://arxiv.org/abs/2603.23202"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2605.07817v1"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "[2510.21356] Gaze-VLM:Bridging Gaze and VLMs through Attention Regularization for Egocentric Understanding",
            "url": "https://arxiv.org/abs/2510.21356"
          },
          {
            "title": "[2508.19257] TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2508.19257"
          },
          {
            "title": "[2605.07817] GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2605.07817"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950v1"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key results:\n\n## Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation\n\nDespite advances in Vision-Language-Action (VLA) models, robotic manipulation struggles with fine-grained tasks because current models lack mechanisms for active visual attention allocation.\n\n**The Proposed Method:**\n\nThe researchers introduce a gaze-regularized training framework that aligns VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead. The method transforms temporally aggregated gaze heatmaps into patch-level distributions and regularizes the transformer's attention through KL divergence, creating an inductive bias toward task-relevant features while preserving deployment efficiency.\n\n**Results and Benefits:**\n\nWhen integrated into existing VLA architectures, the approach yields 4-12% improvements across manipulation benchmarks. Beyond performance metrics, the learned attention patterns produce interpretable visualizations that mirror human strategies, enhancing trust in robotic systems. Additionally, the framework requires no eye-tracking equipment and applies directly to existing datasets.\n\n**Paper Details:**\n- **arXiv ID:** 2603.23202\n- **Published:** March 24, 2026\n- **Links:** [Abstract](https://arxiv.org/abs/2603.23202) | [HTML Version](https://arxiv.org/html/2603.23202v1)"
    ],
    "durationSeconds": 7.838475783000002
  },
  "sourceToolAssistantUUID": "d229bee1-98c5-4bbd-81a8-107b6e5fc4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-13T04:39:49.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0116cfCsgA48W1Sy5k4PT3pW`</summary>

```json
{
  "query": "\"shortcut learning\" VLA robotic policy causal spurious correlation arXiv 2508.06426"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "820bf50d-173a-4c0e-86f3-1395363d5293",
  "isSidechain": false,
  "requestId": "req_011CayxAMYQTUwmGoMpbN2fw",
  "type": "assistant",
  "uuid": "8070ddcf-44e2-48dd-a70c-3acfbd600a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fycg2CsQUoeWk21YmNXkVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 53564,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 935,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 53564,
          "cache_creation_input_tokens": 935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 935
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

_source line 87 · 2026-05-13T04:40:00.495Z_

<details><summary>↩ Tool result · `toolu_0116cfCsgA48W1Sy5k4PT3pW`</summary>

```text
Web search results for query: ""shortcut learning" VLA robotic policy causal spurious correlation arXiv 2508.06426"

Links: [{"title":"Shortcut Learning in Generalist Robot Policies: The","url":"https://arxiv.org/pdf/2508.06426"},{"title":"Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation","url":"https://arxiv.org/html/2508.06426"},{"title":"[2508.06426] Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation","url":"https://arxiv.org/abs/2508.06426"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"The Clever Hans Mirage: A Comprehensive Survey on Spurious Correlations in Machine Learning","url":"https://arxiv.org/html/2402.12715v3"},{"title":"Navigating Shortcuts, Spurious Correlations, and Confounders: From Origins via Detection to Mitigation","url":"https://arxiv.org/html/2412.05152v1"},{"title":"CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning","url":"https://arxiv.org/html/2508.02219v1"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"[1912.07538] Towards Causal VQA: Revealing and Reducing Spurious Correlations by Invariant and Covariant Semantic Editing","url":"https://arxiv.org/abs/1912.07538"}]

Based on the search results, I found the paper you're looking for. Here's a summary of the key information:

## Shortcut Learning in Generalist Robot Policies (arXiv 2508.06426)

The paper identifies shortcut learning—a model's reliance on spurious correlations between actions and task-irrelevant components of observations—as a significant contributor to limitations in generalization of robot policies.

### Main Findings

Generalist robot policies trained on large-scale datasets such as Open X-Embodiment (OXE) demonstrate strong performance across a wide range of tasks. However, they often struggle to generalize beyond the distribution of their training data.

By learning from confounding factors such as viewpoint, background, and texture, the model fails to capture the true causal relationships between observations and actions. Consequently, it may overlook essential elements like language instructions and target objects, thereby restricting its ability to generalize beyond the training distribution.

### Root Causes

The paper uncovers two primary contributors to shortcut learning: (1) limited diversity within individual sub-datasets, and (2) significant distributional disparities across sub-datasets, leading to dataset fragmentation.

### Proposed Solution

Interleaving sub-datasets weakens spurious correlations. As the degree of interleaving increases, the upper bound on the mutual information tightens and moves towards zero.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8070ddcf-44e2-48dd-a70c-3acfbd600a3b",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "0663f546-a38e-4597-95f4-4d89c1bafdbf",
  "toolUseResult": {
    "query": "\"shortcut learning\" VLA robotic policy causal spurious correlation arXiv 2508.06426",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PHqJ5mNYLQXgYVFUUS4inF",
        "content": [
          {
            "title": "Shortcut Learning in Generalist Robot Policies: The",
            "url": "https://arxiv.org/pdf/2508.06426"
          },
          {
            "title": "Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation",
            "url": "https://arxiv.org/html/2508.06426"
          },
          {
            "title": "[2508.06426] Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation",
            "url": "https://arxiv.org/abs/2508.06426"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.01331v1"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.01331"
          },
          {
            "title": "The Clever Hans Mirage: A Comprehensive Survey on Spurious Correlations in Machine Learning",
            "url": "https://arxiv.org/html/2402.12715v3"
          },
          {
            "title": "Navigating Shortcuts, Spurious Correlations, and Confounders: From Origins via Detection to Mitigation",
            "url": "https://arxiv.org/html/2412.05152v1"
          },
          {
            "title": "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2508.02219v1"
          },
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v1"
          },
          {
            "title": "[1912.07538] Towards Causal VQA: Revealing and Reducing Spurious Correlations by Invariant and Covariant Semantic Editing",
            "url": "https://arxiv.org/abs/1912.07538"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's a summary of the key information:\n\n## Shortcut Learning in Generalist Robot Policies (arXiv 2508.06426)\n\nThe paper identifies shortcut learning—a model's reliance on spurious correlations between actions and task-irrelevant components of observations—as a significant contributor to limitations in generalization of robot policies.\n\n### Main Findings\n\nGeneralist robot policies trained on large-scale datasets such as Open X-Embodiment (OXE) demonstrate strong performance across a wide range of tasks. However, they often struggle to generalize beyond the distribution of their training data.\n\nBy learning from confounding factors such as viewpoint, background, and texture, the model fails to capture the true causal relationships between observations and actions. Consequently, it may overlook essential elements like language instructions and target objects, thereby restricting its ability to generalize beyond the training distribution.\n\n### Root Causes\n\nThe paper uncovers two primary contributors to shortcut learning: (1) limited diversity within individual sub-datasets, and (2) significant distributional disparities across sub-datasets, leading to dataset fragmentation.\n\n### Proposed Solution\n\nInterleaving sub-datasets weakens spurious correlations. As the degree of interleaving increases, the upper bound on the mutual information tightens and moves towards zero."
    ],
    "durationSeconds": 11.45655668400001
  },
  "sourceToolAssistantUUID": "8070ddcf-44e2-48dd-a70c-3acfbd600a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-13T04:40:07.964Z_

Now let me search for specific concurrent/competing work that the generator might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0663f546-a38e-4597-95f4-4d89c1bafdbf",
  "isSidechain": false,
  "requestId": "req_011CayxBTikq4a55MJQP7vKX",
  "type": "assistant",
  "uuid": "5832defd-f80e-40eb-9c32-a84c7148df3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4588JmYGDXE6YZW5swcDw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 54499,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 54499,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
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

_source line 89 · 2026-05-13T04:40:08.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U13MRyhakqL5HvEegnVj5c`</summary>

```json
{
  "query": "causal world modeling robot control invariant representation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5832defd-f80e-40eb-9c32-a84c7148df3d",
  "isSidechain": false,
  "requestId": "req_011CayxBTikq4a55MJQP7vKX",
  "type": "assistant",
  "uuid": "df02c080-1b5a-446a-84b7-01a2f55957f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4588JmYGDXE6YZW5swcDw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 54499,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 54499,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
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

_source line 90 · 2026-05-13T04:40:16.552Z_

<details><summary>↩ Tool result · `toolu_01U13MRyhakqL5HvEegnVj5c`</summary>

```text
Web search results for query: "causal world modeling robot control invariant representation 2026 arXiv"

Links: [{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"[2601.21998] Causal World Modeling for Robot Control","url":"https://arxiv.org/abs/2601.21998"},{"title":"Causal World Modeling for Robot Control Lin Li∗ Qihang Zhang∗† Yiming Luo∗","url":"https://arxiv.org/pdf/2601.21998"},{"title":"Paper page - Causal World Modeling for Robot Control","url":"https://huggingface.co/papers/2601.21998"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"Causal World Modeling for Robot Control (Jan 2026) - YouTube","url":"https://www.youtube.com/watch?v=8Q_js9VMT8Q"},{"title":"A ROBOTIC MANIPULATION BENCHMARK FOR CAUSAL ...","url":"https://openreview.net/pdf?id=SK7A5pdrgov"},{"title":"Causal World Modeling in Robot Control","url":"https://www.emergentmind.com/topics/causal-world-modeling-for-robot-control"}]

I found the research paper you were looking for. Here's information about the work on causal world modeling for robot control:

## Causal World Modeling for Robot Control

The paper is titled "Causal World Modeling for Robot Control" by Li, Lin, Zhang, Qihang, and 10 other authors, published on arXiv as preprint arXiv:2601.21998 in 2026.

### Overview

This work highlights that video world modeling, alongside vision-language pre-training, establishes a fresh foundation for robot learning. Video world models provide the ability to imagine the near future by understanding the causality between actions and visual dynamics.

### Key Contribution: LingBot-VA

The authors introduce LingBot-VA, an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. The model features three carefully crafted designs: (1) a shared latent space, integrating vision and action tokens, driven by a Mixture-of-Transformers (MoT) architecture, (2) a closed-loop rollout mechanism, allowing for ongoing acquisition of environmental feedback with ground-truth observations, (3) an asynchronous inference pipeline, parallelizing action prediction and motor execution to support efficient control.

### Technical Approach

The model operates in a continuous latent space via flow matching, autoregressively generating chunks of video and action representations through iterative denoising. By integrating video and action objectives, the framework maintains strict causal consistency, allowing the policy to synchronize physical execution with the predicted visual evolution of the environment.

You can find the paper at https://arxiv.org/abs/2601.21998 and the associated code on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df02c080-1b5a-446a-84b7-01a2f55957f9",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "df72fefb-74e6-4d55-bf81-b4c07d80c9fa",
  "toolUseResult": {
    "query": "causal world modeling robot control invariant representation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G8vffPc4rtU2gzieGVZrLv",
        "content": [
          {
            "title": "GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub",
            "url": "https://github.com/robbyant/lingbot-va"
          },
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v1"
          },
          {
            "title": "[2601.21998] Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/abs/2601.21998"
          },
          {
            "title": "Causal World Modeling for Robot Control Lin Li∗ Qihang Zhang∗† Yiming Luo∗",
            "url": "https://arxiv.org/pdf/2601.21998"
          },
          {
            "title": "Paper page - Causal World Modeling for Robot Control",
            "url": "https://huggingface.co/papers/2601.21998"
          },
          {
            "title": "GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub",
            "url": "https://github.com/leofan90/awesome-world-models"
          },
          {
            "title": "GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub",
            "url": "https://github.com/LMD0311/Awesome-World-Model"
          },
          {
            "title": "Causal World Modeling for Robot Control (Jan 2026) - YouTube",
            "url": "https://www.youtube.com/watch?v=8Q_js9VMT8Q"
          },
          {
            "title": "A ROBOTIC MANIPULATION BENCHMARK FOR CAUSAL ...",
            "url": "https://openreview.net/pdf?id=SK7A5pdrgov"
          },
          {
            "title": "Causal World Modeling in Robot Control",
            "url": "https://www.emergentmind.com/topics/causal-world-modeling-for-robot-control"
          }
        ]
      },
      "I found the research paper you were looking for. Here's information about the work on causal world modeling for robot control:\n\n## Causal World Modeling for Robot Control\n\nThe paper is titled \"Causal World Modeling for Robot Control\" by Li, Lin, Zhang, Qihang, and 10 other authors, published on arXiv as preprint arXiv:2601.21998 in 2026.\n\n### Overview\n\nThis work highlights that video world modeling, alongside vision-language pre-training, establishes a fresh foundation for robot learning. Video world models provide the ability to imagine the near future by understanding the causality between actions and visual dynamics.\n\n### Key Contribution: LingBot-VA\n\nThe authors introduce LingBot-VA, an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. The model features three carefully crafted designs: (1) a shared latent space, integrating vision and action tokens, driven by a Mixture-of-Transformers (MoT) architecture, (2) a closed-loop rollout mechanism, allowing for ongoing acquisition of environmental feedback with ground-truth observations, (3) an asynchronous inference pipeline, parallelizing action prediction and motor execution to support efficient control.\n\n### Technical Approach\n\nThe model operates in a continuous latent space via flow matching, autoregressively generating chunks of video and action representations through iterative denoising. By integrating video and action objectives, the framework maintains strict causal consistency, allowing the policy to synchronize physical execution with the predicted visual evolution of the environment.\n\nYou can find the paper at https://arxiv.org/abs/2601.21998 and the associated code on GitHub."
    ],
    "durationSeconds": 8.251288578999986
  },
  "sourceToolAssistantUUID": "df02c080-1b5a-446a-84b7-01a2f55957f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "df72fefb-74e6-4d55-bf81-b4c07d80c9fa",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 93 · 2026-05-13T04:40:19.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hewzh2Xmw6wu2dYrPGdx7`</summary>

```json
{
  "query": "improving robustness VLA restoring corrupted visual inputs 2026 arXiv 2602.01158"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df72fefb-74e6-4d55-bf81-b4c07d80c9fa",
  "isSidechain": false,
  "requestId": "req_011CayxCeKGgbnoqnfd65R4H",
  "type": "assistant",
  "uuid": "580b0fb3-81d8-4a4f-abfd-3932ec25bcb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5NDwt3gTUocZvVW2j43o5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 55387,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 994,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 55387,
          "cache_creation_input_tokens": 994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 994
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

_source line 94 · 2026-05-13T04:40:26.527Z_

<details><summary>↩ Tool result · `toolu_018hewzh2Xmw6wu2dYrPGdx7`</summary>

```text
Web search results for query: "improving robustness VLA restoring corrupted visual inputs 2026 arXiv 2602.01158"

Links: [{"title":"[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/abs/2602.01158"},{"title":"Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs","url":"https://arxiv.org/html/2602.01158"},{"title":"Improving Robustness of Vision-Language-Action Models ...","url":"https://arxiv.org/pdf/2602.01158"},{"title":"[2602.00807] Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds","url":"https://arxiv.org/abs/2602.00807"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds","url":"https://arxiv.org/html/2602.00807"},{"title":"Reshaping Action Error Distributions for Reliable Vision-Language-Action Models","url":"https://arxiv.org/html/2602.04228"}]

I found the paper you're looking for. Here are the key findings from arXiv paper 2602.01158:

## Title and Overview
Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs

## Problem Identified
Vision-Language-Action (VLA) models have emerged as a dominant paradigm for generalist robotic manipulation, unifying perception and control within a single end-to-end architecture. However, despite their success in controlled environments, reliable real-world deployment is severely hindered by their fragility to visual disturbances.

Sensor-level artifacts, ranging from electronic noise and dead pixels to lens contaminants, directly compromise the integrity of the visual signal prior to interpretation. State-of-the-art VLAs such as π₀.₅ and SmolVLA suffer catastrophic performance degradation, dropping from 90% success rates to as low as 2%, under common signal artifacts.

## Proposed Solution
The authors introduce the Corruption Restoration Transformer (CRT), a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances. Leveraging an adversarial training objective, CRT restores clean observations from corrupted inputs without requiring computationally expensive fine-tuning of the underlying model.

## Results
Extensive experiments across the LIBERO and Meta-World benchmarks demonstrate that CRT effectively recovers lost performance, enabling VLAs to maintain near-baseline success rates, even under severe visual corruption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "580b0fb3-81d8-4a4f-abfd-3932ec25bcb8",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "e1591d35-e2e7-4a7f-b11e-ab0a4f9b278a",
  "toolUseResult": {
    "query": "improving robustness VLA restoring corrupted visual inputs 2026 arXiv 2602.01158",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y5UC4D5pQVvG9Az1muvb2X",
        "content": [
          {
            "title": "[2602.01158] Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs",
            "url": "https://arxiv.org/abs/2602.01158"
          },
          {
            "title": "Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs",
            "url": "https://arxiv.org/html/2602.01158"
          },
          {
            "title": "Improving Robustness of Vision-Language-Action Models ...",
            "url": "https://arxiv.org/pdf/2602.01158"
          },
          {
            "title": "[2602.00807] Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            "url": "https://arxiv.org/abs/2602.00807"
          },
          {
            "title": "In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=6mEfYoMRpF"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/html/2510.00037"
          },
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.01331"
          },
          {
            "title": "[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2511.01331"
          },
          {
            "title": "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            "url": "https://arxiv.org/html/2602.00807"
          },
          {
            "title": "Reshaping Action Error Distributions for Reliable Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.04228"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key findings from arXiv paper 2602.01158:\n\n## Title and Overview\nImproving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs\n\n## Problem Identified\nVision-Language-Action (VLA) models have emerged as a dominant paradigm for generalist robotic manipulation, unifying perception and control within a single end-to-end architecture. However, despite their success in controlled environments, reliable real-world deployment is severely hindered by their fragility to visual disturbances.\n\nSensor-level artifacts, ranging from electronic noise and dead pixels to lens contaminants, directly compromise the integrity of the visual signal prior to interpretation. State-of-the-art VLAs such as π₀.₅ and SmolVLA suffer catastrophic performance degradation, dropping from 90% success rates to as low as 2%, under common signal artifacts.\n\n## Proposed Solution\nThe authors introduce the Corruption Restoration Transformer (CRT), a plug-and-play and model-agnostic vision transformer designed to immunize VLA models against sensor disturbances. Leveraging an adversarial training objective, CRT restores clean observations from corrupted inputs without requiring computationally expensive fine-tuning of the underlying model.\n\n## Results\nExtensive experiments across the LIBERO and Meta-World benchmarks demonstrate that CRT effectively recovers lost performance, enabling VLAs to maintain near-baseline success rates, even under severe visual corruption."
    ],
    "durationSeconds": 6.972518186000001
  },
  "sourceToolAssistantUUID": "580b0fb3-81d8-4a4f-abfd-3932ec25bcb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-13T04:40:30.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EsD3LjzsjaAoppnz88fH6K`</summary>

```json
{
  "query": "RobustVLA ICLR 2026 arXiv 2510.00037 results LIBERO-Plus success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1591d35-e2e7-4a7f-b11e-ab0a4f9b278a",
  "isSidechain": false,
  "requestId": "req_011CayxDNxKVMZpGLuuJgpfG",
  "type": "assistant",
  "uuid": "0c3170a7-6548-4c89-bb57-812490340ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSgeeFYfviJa3JycnvhGVF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 56381,
      "output_tokens": 82,
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
          "output_tokens": 82,
          "cache_read_input_tokens": 56381,
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

_source line 96 · 2026-05-13T04:40:35.682Z_

<details><summary>↩ Tool result · `toolu_01EsD3LjzsjaAoppnz88fH6K`</summary>

```text
Web search results for query: "RobustVLA ICLR 2026 arXiv 2510.00037 results LIBERO-Plus success rate"

Links: [{"title":"[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/html/2510.00037"},{"title":"[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/abs/2510.00037v4"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"}]

Based on the search results, here are the key findings for RobustVLA (arXiv 2510.00037) regarding LIBERO-Plus and success rates:

On the LIBERO benchmark, RobustVLA delivers absolute gains over baselines of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations.

Additionally, on the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming π0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, the method still outperforms π0 by 30% success rate.

The paper has been published at ICLR 2026 and focuses on improving the robustness of Vision-Language-Action models against multi-modal perturbations through a method that formulates robustness as a multi-armed bandit problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c3170a7-6548-4c89-bb57-812490340ded",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "1bdd0881-69ba-4076-af43-57ceea17f1a7",
  "toolUseResult": {
    "query": "RobustVLA ICLR 2026 arXiv 2510.00037 results LIBERO-Plus success rate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DTZ1VzmxAbDoWaShy78MwA",
        "content": [
          {
            "title": "[2510.00037] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/abs/2510.00037"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 ON ROBUSTNESS",
            "url": "https://arxiv.org/pdf/2510.00037v4"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/html/2510.00037"
          },
          {
            "title": "[2510.00037v4] On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/abs/2510.00037v4"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=6mEfYoMRpF"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
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
            "title": "[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/abs/2510.03827"
          }
        ]
      },
      "Based on the search results, here are the key findings for RobustVLA (arXiv 2510.00037) regarding LIBERO-Plus and success rates:\n\nOn the LIBERO benchmark, RobustVLA delivers absolute gains over baselines of 12.6% on the π0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations.\n\nAdditionally, on the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming π0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, the method still outperforms π0 by 30% success rate.\n\nThe paper has been published at ICLR 2026 and focuses on improving the robustness of Vision-Language-Action models against multi-modal perturbations through a method that formulates robustness as a multi-armed bandit problem."
    ],
    "durationSeconds": 5.543797765999974
  },
  "sourceToolAssistantUUID": "0c3170a7-6548-4c89-bb57-812490340ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-13T04:40:40.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QaFfAub8R57xDpUcXp3ZvN`</summary>

```json
{
  "query": "LightVLA differentiable token pruning VLA 2025 arXiv 2509.12594"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bdd0881-69ba-4076-af43-57ceea17f1a7",
  "isSidechain": false,
  "requestId": "req_011CayxE4EiavrsK5YunU6FH",
  "type": "assistant",
  "uuid": "adec6008-3346-473f-8d5c-5ea28317f972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ap3v5q7ejgrEQ53LJz31EJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 57317,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 891,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 57317,
          "cache_creation_input_tokens": 891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 891
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

_source line 98 · 2026-05-13T04:40:50.681Z_

<details><summary>↩ Tool result · `toolu_01QaFfAub8R57xDpUcXp3ZvN`</summary>

```text
Web search results for query: "LightVLA differentiable token pruning VLA 2025 arXiv 2509.12594"

Links: [{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X","url":"https://x.com/ai_bites/status/1970481721163313156"},{"title":"Efficient Token Pruning for LLaDA-V","url":"https://arxiv.org/html/2601.20168"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/html/2601.16065"}]

I found detailed information about LightVLA (arXiv 2509.12594). Here's what the paper presents:

## Overview

LightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models.

## Problem Addressed

While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens.

## Technical Approach

LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.

## Key Features

Notably, LightVLA requires no heuristic "magic numbers" and introduces no additional trainable parameters, making it compatible with modern inference frameworks.

## Performance Results

Specifically, LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate. Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark, achieving higher success rates with substantially reduced computational overhead.

## Significance

LightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance, marking a significant step toward more efficient, powerful and practical real-time robotic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adec6008-3346-473f-8d5c-5ea28317f972",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "3d4e6517-f6d6-4532-8442-ee64376ba236",
  "toolUseResult": {
    "query": "LightVLA differentiable token pruning VLA 2025 arXiv 2509.12594",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PKWLS1AZcGVXA8sCe2G8uz",
        "content": [
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/abs/2509.12594"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"
          },
          {
            "title": "LightVLA",
            "url": "https://liauto-research.github.io/LightVLA/"
          },
          {
            "title": "Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium",
            "url": "https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"
          },
          {
            "title": "GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)",
            "url": "https://github.com/LiAutoAD/LightVLA"
          },
          {
            "title": "AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X",
            "url": "https://x.com/ai_bites/status/1970481721163313156"
          },
          {
            "title": "Efficient Token Pruning for LLaDA-V",
            "url": "https://arxiv.org/html/2601.20168"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/html/2506.12723v2"
          },
          {
            "title": "DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models",
            "url": "https://arxiv.org/html/2601.16065"
          }
        ]
      },
      "I found detailed information about LightVLA (arXiv 2509.12594). Here's what the paper presents:\n\n## Overview\n\nLightVLA is a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models.\n\n## Problem Addressed\n\nWhile VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens.\n\n## Technical Approach\n\nLightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.\n\n## Key Features\n\nNotably, LightVLA requires no heuristic \"magic numbers\" and introduces no additional trainable parameters, making it compatible with modern inference frameworks.\n\n## Performance Results\n\nSpecifically, LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate. Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark, achieving higher success rates with substantially reduced computational overhead.\n\n## Significance\n\nLightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance, marking a significant step toward more efficient, powerful and practical real-time robotic systems."
    ],
    "durationSeconds": 10.665214806000003
  },
  "sourceToolAssistantUUID": "adec6008-3346-473f-8d5c-5ea28317f972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-13T04:40:54.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GxCLfRN3Ac3he7cfuRtFX9`</summary>

```json
{
  "query": "DTP distracting token pruning VLA 2026 arXiv 2601.16065"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d4e6517-f6d6-4532-8442-ee64376ba236",
  "isSidechain": false,
  "requestId": "req_011CayxFAVHPesqf4Q1YQbsT",
  "type": "assistant",
  "uuid": "50a4bb94-7642-4209-9c1f-e38d2101a857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsRmPS4v9uGr5BfWtJE8nx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 58208,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1144,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 58208,
          "cache_creation_input_tokens": 1144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1144
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

_source line 100 · 2026-05-13T04:41:02.956Z_

<details><summary>↩ Tool result · `toolu_01GxCLfRN3Ac3he7cfuRtFX9`</summary>

```text
Web search results for query: "DTP distracting token pruning VLA 2026 arXiv 2601.16065"

Links: [{"title":"[2601.16065] DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/abs/2601.16065"},{"title":"DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/html/2601.16065"},{"title":"DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models | OpenReview","url":"https://openreview.net/forum?id=5yYQDuXzZh"},{"title":"[2601.07667] Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/abs/2601.07667"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"Efficient Token Pruning for LLaDA-V","url":"https://arxiv.org/html/2601.20168"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"[2601.20168] Efficient Token Pruning for LLaDA-V","url":"https://arxiv.org/abs/2601.20168"}]

Based on the search results, here's what I found about the paper with arXiv ID 2601.16065:

## DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models

Vision-Language Action (VLA) models have shown remarkable progress in robotic manipulation by leveraging the powerful perception abilities of Vision-Language Models. However, by default, VLA models may overly attend to image tokens in the task-irrelevant region, which are described as 'distracting tokens'. This behavior can disturb the model from the generation of the desired action tokens in each step, affecting the success rate of tasks.

The paper introduces a simple yet effective plug-and-play Distracting Token Pruning (DTP) framework, which dynamically detects and prunes these distracting image tokens. By correcting the model's visual attention patterns, the method aims to improve the task success rate, as well as exploring the performance upper boundaries of the model without altering its original architecture or adding additional inputs.

Experiments on the SIMPLER Benchmark show that the method consistently achieves relative improvements in task success rates across different types of novel VLA models, demonstrating generalizability to transformer-based VLAs. Further analysis reveals a negative correlation between the task success rate and the amount of attentions in the task-irrelevant region for all models tested, highlighting a common phenomenon of VLA models that could guide future research.

The paper was submitted to arXiv on January 22, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50a4bb94-7642-4209-9c1f-e38d2101a857",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "2a42c06d-ff6a-40eb-903a-9ade3d788c61",
  "toolUseResult": {
    "query": "DTP distracting token pruning VLA 2026 arXiv 2601.16065",
    "results": [
      {
        "tool_use_id": "srvtoolu_0126p54VBPkU6ZVq9Cubb76m",
        "content": [
          {
            "title": "[2601.16065] DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models",
            "url": "https://arxiv.org/abs/2601.16065"
          },
          {
            "title": "DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models",
            "url": "https://arxiv.org/html/2601.16065"
          },
          {
            "title": "DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=5yYQDuXzZh"
          },
          {
            "title": "[2601.07667] Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference",
            "url": "https://arxiv.org/abs/2601.07667"
          },
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "Efficient Token Pruning for LLaDA-V",
            "url": "https://arxiv.org/html/2601.20168"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "[2601.20168] Efficient Token Pruning for LLaDA-V",
            "url": "https://arxiv.org/abs/2601.20168"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper with arXiv ID 2601.16065:\n\n## DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models\n\nVision-Language Action (VLA) models have shown remarkable progress in robotic manipulation by leveraging the powerful perception abilities of Vision-Language Models. However, by default, VLA models may overly attend to image tokens in the task-irrelevant region, which are described as 'distracting tokens'. This behavior can disturb the model from the generation of the desired action tokens in each step, affecting the success rate of tasks.\n\nThe paper introduces a simple yet effective plug-and-play Distracting Token Pruning (DTP) framework, which dynamically detects and prunes these distracting image tokens. By correcting the model's visual attention patterns, the method aims to improve the task success rate, as well as exploring the performance upper boundaries of the model without altering its original architecture or adding additional inputs.\n\nExperiments on the SIMPLER Benchmark show that the method consistently achieves relative improvements in task success rates across different types of novel VLA models, demonstrating generalizability to transformer-based VLAs. Further analysis reveals a negative correlation between the task success rate and the amount of attentions in the task-irrelevant region for all models tested, highlighting a common phenomenon of VLA models that could guide future research.\n\nThe paper was submitted to arXiv on January 22, 2026."
    ],
    "durationSeconds": 8.044592408999975
  },
  "sourceToolAssistantUUID": "50a4bb94-7642-4209-9c1f-e38d2101a857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 101 · 2026-05-13T04:41:02.962Z_

```json
{
  "parentUuid": "2a42c06d-ff6a-40eb-903a-9ade3d788c61",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "50da7e1f-d9e8-492d-ba7f-50bdb093a831",
  "timestamp": "2026-05-13T04:41:02.962Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 102_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "50da7e1f-d9e8-492d-ba7f-50bdb093a831",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 103_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Assistant

_source line 104 · 2026-05-13T04:41:06.941Z_

This is a very important find — DTP directly addresses "distracting token pruning" for VLA models. Let me also check for the most critical potential competitor: any work combining causal reasoning with token selection for VLA specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50da7e1f-d9e8-492d-ba7f-50bdb093a831",
  "isSidechain": false,
  "requestId": "req_011CayxG4nGRjc3Basn7D77x",
  "type": "assistant",
  "uuid": "408f361e-9033-49e4-9524-b22ac878f57c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsQnZhcyNieWxxxmDL3jEe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 59352,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1097,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 59352,
          "cache_creation_input_tokens": 1097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1097
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

_source line 105 · 2026-05-13T04:41:07.618Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RVr2YMYyPeYpqohcaNbqG8`</summary>

```json
{
  "query": "\"causal\" \"token\" \"pruning\" OR \"selection\" \"robot\" OR \"manipulation\" OR \"VLA\" invariant 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "408f361e-9033-49e4-9524-b22ac878f57c",
  "isSidechain": false,
  "requestId": "req_011CayxG4nGRjc3Basn7D77x",
  "type": "assistant",
  "uuid": "c7026a6b-8a67-4a92-9027-fa90dd004dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsQnZhcyNieWxxxmDL3jEe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 59352,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1097,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 59352,
          "cache_creation_input_tokens": 1097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1097
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

_source line 106 · 2026-05-13T04:41:16.670Z_

<details><summary>↩ Tool result · `toolu_01RVr2YMYyPeYpqohcaNbqG8`</summary>

```text
Web search results for query: ""causal" "token" "pruning" OR "selection" "robot" OR "manipulation" OR "VLA" invariant 2025 2026"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v2"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"}]

I've performed the web search for your query and found several highly relevant papers from 2025-2026. Here's a summary of the key results:

## Recent Research on Token Pruning and VLA Models

**Token Pruning for Vision-Language-Action Models:**

Vision-Language-Action (VLA) models have rapidly advanced embodied intelligence, enabling robots to execute complex, instruction-driven tasks, though as model capacity and visual context length grow, the inference cost of VLA systems becomes a major bottleneck for real-world deployment on resource-constrained platforms.

Several papers address this challenge with different approaches:

1. **VLA-IAP (2026)**: Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA tasks, consequently, current approaches often prune visually sparse yet structurally critical regions that support manipulation, leading to unstable behavior during early task phases.

2. **VLA-Pruner (2025)**: Token pruning (keeping salient visual tokens and dropping redundant ones) has emerged as an effective approach for accelerating Vision-Language Models (VLMs), offering a solution for efficient VLA, however, these VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution.

3. **VLA-Cache (2025)**: Tokens not recomputed do not receive new position IDs, enabling a pruned causal mask aligned with the updated token set.

4. **LightVLA (2025)**: LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models, addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection.

**Causal World Modeling:**

Causal World Modeling for Robot Control is an emerging research direction in embodied AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7026a6b-8a67-4a92-9027-fa90dd004dc2",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "c2ad0514-46cd-4b9d-8a53-d01616236d55",
  "toolUseResult": {
    "query": "\"causal\" \"token\" \"pruning\" OR \"selection\" \"robot\" OR \"manipulation\" OR \"VLA\" invariant 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fs9bhQBjwxuE4ZCRK4jcjT",
        "content": [
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          },
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v2"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          },
          {
            "title": "VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation",
            "url": "https://arxiv.org/html/2502.02175v1"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub",
            "url": "https://github.com/LMD0311/Awesome-World-Model"
          }
        ]
      },
      "I've performed the web search for your query and found several highly relevant papers from 2025-2026. Here's a summary of the key results:\n\n## Recent Research on Token Pruning and VLA Models\n\n**Token Pruning for Vision-Language-Action Models:**\n\nVision-Language-Action (VLA) models have rapidly advanced embodied intelligence, enabling robots to execute complex, instruction-driven tasks, though as model capacity and visual context length grow, the inference cost of VLA systems becomes a major bottleneck for real-world deployment on resource-constrained platforms.\n\nSeveral papers address this challenge with different approaches:\n\n1. **VLA-IAP (2026)**: Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA tasks, consequently, current approaches often prune visually sparse yet structurally critical regions that support manipulation, leading to unstable behavior during early task phases.\n\n2. **VLA-Pruner (2025)**: Token pruning (keeping salient visual tokens and dropping redundant ones) has emerged as an effective approach for accelerating Vision-Language Models (VLMs), offering a solution for efficient VLA, however, these VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution.\n\n3. **VLA-Cache (2025)**: Tokens not recomputed do not receive new position IDs, enabling a pruned causal mask aligned with the updated token set.\n\n4. **LightVLA (2025)**: LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models, addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection.\n\n**Causal World Modeling:**\n\nCausal World Modeling for Robot Control is an emerging research direction in embodied AI."
    ],
    "durationSeconds": 9.048141359
  },
  "sourceToolAssistantUUID": "c7026a6b-8a67-4a92-9027-fa90dd004dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-13T04:41:19.845Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JnxTDDpyCyEH1zX8nc5DeZ`</summary>

```json
{
  "query": "Compressor-VLA instruction-guided visual token compression VLA arXiv 2511.18950"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ad0514-46cd-4b9d-8a53-d01616236d55",
  "isSidechain": false,
  "requestId": "req_011CayxH5NWeBVbbt4W9EPrJ",
  "type": "assistant",
  "uuid": "148c2bf0-d7d4-4446-8067-7b5160d15390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhSbrnjyP9zeViVf44ujUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1210,
      "cache_read_input_tokens": 60449,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 60449,
          "cache_creation_input_tokens": 1210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1210
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

_source line 108 · 2026-05-13T04:41:26.880Z_

<details><summary>↩ Tool result · `toolu_01JnxTDDpyCyEH1zX8nc5DeZ`</summary>

```text
Web search results for query: "Compressor-VLA instruction-guided visual token compression VLA arXiv 2511.18950"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World...","url":"https://arxiv.org/abs/2605.07931v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/html/2605.08329"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"[2605.08329] An Efficient Token Compression Framework for Visual Object Tracking","url":"https://arxiv.org/abs/2605.08329"},{"title":"Think Twice, Act Once: Token-Aware Compression and Action Reuse for Efficient Inference in Vision-Language-Action Models","url":"https://arxiv.org/html/2505.21200"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.09927"}]

Based on the search results, I found detailed information about the paper you're looking for:

## Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

Vision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI. However, the significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment.

### Key Problem and Solution

Standard token pruning techniques can alleviate this, but these task-agnostic methods struggle to preserve task-critical visual information. To address this challenge, the researchers propose Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. The framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.

### Technical Approach

The compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.

### Performance Results

Experimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability.

The paper was submitted on November 24, 2025 and is authored by Juntao Gao, Feiyang Ye, Jing Zhang, and Wenjing Qian.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "148c2bf0-d7d4-4446-8067-7b5160d15390",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "33ac44eb-bc05-4c8d-bb68-9f11cef9429a",
  "toolUseResult": {
    "query": "Compressor-VLA instruction-guided visual token compression VLA arXiv 2511.18950",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ur7pRmacrdZh4Dag8AwH7B",
        "content": [
          {
            "title": "[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.18950"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.18950v1"
          },
          {
            "title": "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation",
            "url": "https://chatpaper.com/paper/212383"
          },
          {
            "title": "One Token Per Frame: Reconsidering Visual Bandwidth in World...",
            "url": "https://arxiv.org/abs/2605.07931v1"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.10100v1"
          },
          {
            "title": "An Efficient Token Compression Framework for Visual Object Tracking",
            "url": "https://arxiv.org/html/2605.08329"
          },
          {
            "title": "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy",
            "url": "https://arxiv.org/html/2605.07931v1"
          },
          {
            "title": "[2605.08329] An Efficient Token Compression Framework for Visual Object Tracking",
            "url": "https://arxiv.org/abs/2605.08329"
          },
          {
            "title": "Think Twice, Act Once: Token-Aware Compression and Action Reuse for Efficient Inference in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2505.21200"
          },
          {
            "title": "Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2512.09927"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper you're looking for:\n\n## Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\n\nVision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI. However, the significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment.\n\n### Key Problem and Solution\n\nStandard token pruning techniques can alleviate this, but these task-agnostic methods struggle to preserve task-critical visual information. To address this challenge, the researchers propose Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. The framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.\n\n### Technical Approach\n\nThe compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information.\n\n### Performance Results\n\nExperimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability.\n\nThe paper was submitted on November 24, 2025 and is authored by Juntao Gao, Feiyang Ye, Jing Zhang, and Wenjing Qian."
    ],
    "durationSeconds": 7.028774809999973
  },
  "sourceToolAssistantUUID": "148c2bf0-d7d4-4446-8067-7b5160d15390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-13T04:41:29.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J4ahyVbgGt91F5j9eVgjct`</summary>

```json
{
  "query": "BFA++ hierarchical best-feature-aware token pruning multi-view VLA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ac44eb-bc05-4c8d-bb68-9f11cef9429a",
  "isSidechain": false,
  "requestId": "req_011CayxHq35h3gzeEsYLzSgo",
  "type": "assistant",
  "uuid": "f3fdda0c-ed2c-48b7-af83-1b3e5295bbe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1abDJpZNsRyooXNkGKMhz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 61659,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 61659,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 965
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

_source line 110 · 2026-05-13T04:41:36.764Z_

<details><summary>↩ Tool result · `toolu_01J4ahyVbgGt91F5j9eVgjct`</summary>

```text
Web search results for query: "BFA++ hierarchical best-feature-aware token pruning multi-view VLA 2026"

Links: [{"title":"[2602.20566] BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/abs/2602.20566"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model","url":"https://arxiv.org/html/2602.20566"},{"title":"BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11433770/;jsessionid=D61CCED0517043E81E8A06ED16169CD6"},{"title":"GitHub - guanweifan/awesome-efficient-vla: 🔥 A curated roadmap to the Efficient VLA landscape. We’re keeping this list live—contribute your latest work!","url":"https://github.com/guanweifan/awesome-efficient-vla"},{"title":"Efficient Token Pruning for LLaDA-V","url":"https://arxiv.org/html/2601.20168"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"}]

I found relevant information about BFA++ and multi-view VLA research. Here are the key findings:

## BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA

BFA++ is a dynamic token pruning framework designed specifically for VLA models that introduces a hierarchical pruning strategy guided by two-level importance predictors: an intra-view predictor highlights task-relevant regions within each image to suppress spatial noise, while an inter-view predictor identifies critical camera views.

### Problem It Addresses

Vision-Language-Action (VLA) models have achieved significant breakthroughs by leveraging Large Vision Language Models (VLMs) to jointly interpret instructions and visual inputs, but the substantial increase in visual tokens, particularly from multi-view inputs, poses serious challenges to real-time robotic manipulation.

### Key Approach

The method uses the inter-view importance score to evaluate the importance of each view and uses intra-view importance to rate the importance of tokens within view, then locally prunes less important tokens within each view using the intra-view importance score, and globally ranks all remaining tokens by intra-view and inter-view importance scores to eliminate less critical tokens across all views.

### Performance Results

Evaluations on the RoboTwin benchmark and real-world robotic tasks demonstrate that BFA++ consistently outperforms existing methods.

The research was published in February 2026 on arXiv (paper 2602.20566) and represents a recent advancement in efficient VLA model design.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3fdda0c-ed2c-48b7-af83-1b3e5295bbe8",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "7ba6a425-dae4-469d-bbfa-69f83dcbfd2f",
  "toolUseResult": {
    "query": "BFA++ hierarchical best-feature-aware token pruning multi-view VLA 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YGh3jeztcMgGo7sVYG8ovG",
        "content": [
          {
            "title": "[2602.20566] BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model",
            "url": "https://arxiv.org/abs/2602.20566"
          },
          {
            "title": "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model",
            "url": "https://arxiv.org/html/2602.20566"
          },
          {
            "title": "BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/11433770/;jsessionid=D61CCED0517043E81E8A06ED16169CD6"
          },
          {
            "title": "GitHub - guanweifan/awesome-efficient-vla: 🔥 A curated roadmap to the Efficient VLA landscape. We’re keeping this list live—contribute your latest work!",
            "url": "https://github.com/guanweifan/awesome-efficient-vla"
          },
          {
            "title": "Efficient Token Pruning for LLaDA-V",
            "url": "https://arxiv.org/html/2601.20168"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub",
            "url": "https://github.com/ZLKong/Awesome-Collection-Token-Reduction"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub",
            "url": "https://github.com/daixiangzi/Awesome-Token-Compress"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          }
        ]
      },
      "I found relevant information about BFA++ and multi-view VLA research. Here are the key findings:\n\n## BFA++: Hierarchical Best-Feature-Aware Token Pruning for Multi-View VLA\n\nBFA++ is a dynamic token pruning framework designed specifically for VLA models that introduces a hierarchical pruning strategy guided by two-level importance predictors: an intra-view predictor highlights task-relevant regions within each image to suppress spatial noise, while an inter-view predictor identifies critical camera views.\n\n### Problem It Addresses\n\nVision-Language-Action (VLA) models have achieved significant breakthroughs by leveraging Large Vision Language Models (VLMs) to jointly interpret instructions and visual inputs, but the substantial increase in visual tokens, particularly from multi-view inputs, poses serious challenges to real-time robotic manipulation.\n\n### Key Approach\n\nThe method uses the inter-view importance score to evaluate the importance of each view and uses intra-view importance to rate the importance of tokens within view, then locally prunes less important tokens within each view using the intra-view importance score, and globally ranks all remaining tokens by intra-view and inter-view importance scores to eliminate less critical tokens across all views.\n\n### Performance Results\n\nEvaluations on the RoboTwin benchmark and real-world robotic tasks demonstrate that BFA++ consistently outperforms existing methods.\n\nThe research was published in February 2026 on arXiv (paper 2602.20566) and represents a recent advancement in efficient VLA model design."
    ],
    "durationSeconds": 6.865093908999988
  },
  "sourceToolAssistantUUID": "f3fdda0c-ed2c-48b7-af83-1b3e5295bbe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-13T04:41:41.173Z_

Now let me do the key fetch — read the Causal-ACT paper more carefully to understand its differentiation from CaTS.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba6a425-dae4-469d-bbfa-69f83dcbfd2f",
  "isSidechain": false,
  "requestId": "req_011CayxJaaxMxmXnKxaR7sHH",
  "type": "assistant",
  "uuid": "497eee92-f06c-4cbf-be11-c5a3886b414d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vg9LmxNJ9mMT6Pti63iEL3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 62624,
      "output_tokens": 241,
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
          "output_tokens": 241,
          "cache_read_input_tokens": 62624,
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

### Tool call

_source line 112 · 2026-05-13T04:41:44.381Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UWYcom5X4smqjD8YPyVyyW`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.22380",
  "prompt": "Extract the following details: 1) What causal framework/SCM does this paper use? 2) How does it identify causal vs spurious features? 3) Does it work at the token level or feature level? 4) What architecture does it use (ResNet, ViT, transformer)? 5) What environments is it evaluated on? 6) What are its specific OOD success rates? 7) Does it use interventions? How? 8) What are the key limitations acknowledged? 9) Does it mention anything about VLA models or scaling to larger architectures?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497eee92-f06c-4cbf-be11-c5a3886b414d",
  "isSidechain": false,
  "requestId": "req_011CayxJaaxMxmXnKxaR7sHH",
  "type": "assistant",
  "uuid": "341c8269-a698-43b4-ac73-34df6b91c4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vg9LmxNJ9mMT6Pti63iEL3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 62624,
      "output_tokens": 241,
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
          "output_tokens": 241,
          "cache_read_input_tokens": 62624,
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

_source line 113 · 2026-05-13T04:41:56.013Z_

<details><summary>↩ Tool result · `toolu_01UWYcom5X4smqjD8YPyVyyW`</summary>

```text
# Causal-ACT Paper Analysis

## 1. Causal Framework/SCM
The paper employs a **Structural Causal Model (SCM)** based on Pearl's causal framework. It models observations and actions as variables in a directed acyclic graph where edges represent direct causal relationships. The key innovation is proving that disentangled representations are unnecessary for learning causal structures in imitation learning contexts.

## 2. Causal vs. Spurious Feature Identification
The method identifies task-relevant features by learning which observation dimensions directly cause action selection. It does this through "targeted intervention"—testing different causal graph configurations during inference and selecting the one producing highest episodic rewards. Spurious correlations (like distractor cubes) are ignored when the learned graph masks them out.

## 3. Token vs. Feature Level
The approach works at the **feature level**. The causal graph is represented as "an array of binary variables" matching the dimensionality of image features extracted by ResNet, operating on encoded representations rather than individual tokens.

## 4. Architecture
Uses **ResNet-18** for image encoding, combined with a **Transformer-based policy** (Action Chunking Transformer or ACT). The system includes style variable learning via a "transformer encoder" that processes action sequences and joint positions.

## 5. Evaluation Environments
Tested on **ALOHA bimanual robot simulation in MuJoCo**. The task involves one arm grasping a red cube and transferring it to the other arm. Training includes six distractor cubes; testing removes them entirely.

## 6. OOD Success Rates
- **Causal-ACT transfer task OOD**: 0.88 (88%)
- **Standard ACT OOD**: 0.23 (23%)
- Dramatic 65-point improvement in generalization

## 7. Intervention Usage
Yes, the method extensively uses interventions. After training, it performs "targeted intervention" by sampling candidate graphs and executing the policy with each, recording episodic rewards. An energy-based model selects the best-performing graph, with probability "proportional to the episodic reward returned."

## 8. Key Limitations Acknowledged
The authors note two main constraints: (1) "intractable to visit each possible graph" due to exponential space size (2^512×15×20); (2) requires "efficient graph sampling method" to differentiate promising options quickly. They defer this to future work.

## 9. VLA Models or Scaling Discussion
The paper makes **no mention of Vision-Language-Action models or scaling to larger architectures**. It focuses specifically on adapting the ACT algorithm without addressing broader architectural scaling challenges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "341c8269-a698-43b4-ac73-34df6b91c4e5",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "b8bd01dc-2671-4498-8f92-133caec8599f",
  "toolUseResult": {
    "bytes": 228821,
    "code": 200,
    "codeText": "OK",
    "result": "# Causal-ACT Paper Analysis\n\n## 1. Causal Framework/SCM\nThe paper employs a **Structural Causal Model (SCM)** based on Pearl's causal framework. It models observations and actions as variables in a directed acyclic graph where edges represent direct causal relationships. The key innovation is proving that disentangled representations are unnecessary for learning causal structures in imitation learning contexts.\n\n## 2. Causal vs. Spurious Feature Identification\nThe method identifies task-relevant features by learning which observation dimensions directly cause action selection. It does this through \"targeted intervention\"—testing different causal graph configurations during inference and selecting the one producing highest episodic rewards. Spurious correlations (like distractor cubes) are ignored when the learned graph masks them out.\n\n## 3. Token vs. Feature Level\nThe approach works at the **feature level**. The causal graph is represented as \"an array of binary variables\" matching the dimensionality of image features extracted by ResNet, operating on encoded representations rather than individual tokens.\n\n## 4. Architecture\nUses **ResNet-18** for image encoding, combined with a **Transformer-based policy** (Action Chunking Transformer or ACT). The system includes style variable learning via a \"transformer encoder\" that processes action sequences and joint positions.\n\n## 5. Evaluation Environments\nTested on **ALOHA bimanual robot simulation in MuJoCo**. The task involves one arm grasping a red cube and transferring it to the other arm. Training includes six distractor cubes; testing removes them entirely.\n\n## 6. OOD Success Rates\n- **Causal-ACT transfer task OOD**: 0.88 (88%)\n- **Standard ACT OOD**: 0.23 (23%)\n- Dramatic 65-point improvement in generalization\n\n## 7. Intervention Usage\nYes, the method extensively uses interventions. After training, it performs \"targeted intervention\" by sampling candidate graphs and executing the policy with each, recording episodic rewards. An energy-based model selects the best-performing graph, with probability \"proportional to the episodic reward returned.\"\n\n## 8. Key Limitations Acknowledged\nThe authors note two main constraints: (1) \"intractable to visit each possible graph\" due to exponential space size (2^512×15×20); (2) requires \"efficient graph sampling method\" to differentiate promising options quickly. They defer this to future work.\n\n## 9. VLA Models or Scaling Discussion\nThe paper makes **no mention of Vision-Language-Action models or scaling to larger architectures**. It focuses specifically on adapting the ACT algorithm without addressing broader architectural scaling challenges.",
    "durationMs": 11629,
    "url": "https://arxiv.org/html/2507.22380"
  },
  "sourceToolAssistantUUID": "341c8269-a698-43b4-ac73-34df6b91c4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 114_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b8bd01dc-2671-4498-8f92-133caec8599f",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 115_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 116 · 2026-05-13T04:42:00.834Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0112eLWGPWzQFi9HTB9GhcyH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.07851",
  "prompt": "Extract the key details about LeaF (Learning to Focus): 1) How does it identify confounding tokens? 2) What is the causal framework used? 3) How does the gradient-based comparison work? 4) Does it use interventions? 5) What tasks/benchmarks is it evaluated on? 6) What are the main results? 7) Does it mention cross-environment invariance? 8) Could this approach be adapted to VLA models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8bd01dc-2671-4498-8f92-133caec8599f",
  "isSidechain": false,
  "requestId": "req_011CayxKyfJNLZ7wYBvKQBmr",
  "type": "assistant",
  "uuid": "a722fc9a-aaf3-4b4b-9806-a1ef6baa18ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPiirim3id3rkzBURCA98r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 63665,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 63665,
          "cache_creation_input_tokens": 863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 863
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

_source line 117 · 2026-05-13T04:42:08.639Z_

<details><summary>↩ Tool result · `toolu_0112eLWGPWzQFi9HTB9GhcyH`</summary>

```text
# LeaF: Learning to Focus - Key Details

**1) Confounding Token Identification:**
LeaF uses "gradient-based comparisons with an advanced teacher to automatically identify confounding tokens based on causal relationships" in the training corpus during the first stage.

**2) Causal Framework:**
The approach leverages "intervention-based inference to disentangle confounding factors," treating spurious correlations in training data as obstacles to learning authentic causal instruction-response relationships.

**3) Gradient-Based Comparison:**
The abstract indicates gradient comparisons occur between a student and teacher model, though specific technical details of the comparison mechanism are not elaborated in this excerpt.

**4) Interventions:**
Yes. The second stage "prunes these tokens during distillation to enact intervention," aligning student attention with teacher focus on critical context tokens.

**5) Evaluation Tasks:**
The model was tested on "mathematical reasoning, code generation and multi-hop question answering benchmarks."

**6) Main Results:**
LeaF achieved "absolute improvement in various" evaluated benchmarks while "effectively suppressing attention to confounding tokens during inference."

**7) Cross-Environment Invariance:**
Not mentioned in the provided content.

**8) VLA Model Adaptation:**
No discussion of vision-language models or VLA applicability appears in this abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a722fc9a-aaf3-4b4b-9806-a1ef6baa18ba",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "b73dc613-c39f-4ee1-8a8e-0ecf33f9c7fe",
  "toolUseResult": {
    "bytes": 47997,
    "code": 200,
    "codeText": "OK",
    "result": "# LeaF: Learning to Focus - Key Details\n\n**1) Confounding Token Identification:**\nLeaF uses \"gradient-based comparisons with an advanced teacher to automatically identify confounding tokens based on causal relationships\" in the training corpus during the first stage.\n\n**2) Causal Framework:**\nThe approach leverages \"intervention-based inference to disentangle confounding factors,\" treating spurious correlations in training data as obstacles to learning authentic causal instruction-response relationships.\n\n**3) Gradient-Based Comparison:**\nThe abstract indicates gradient comparisons occur between a student and teacher model, though specific technical details of the comparison mechanism are not elaborated in this excerpt.\n\n**4) Interventions:**\nYes. The second stage \"prunes these tokens during distillation to enact intervention,\" aligning student attention with teacher focus on critical context tokens.\n\n**5) Evaluation Tasks:**\nThe model was tested on \"mathematical reasoning, code generation and multi-hop question answering benchmarks.\"\n\n**6) Main Results:**\nLeaF achieved \"absolute improvement in various\" evaluated benchmarks while \"effectively suppressing attention to confounding tokens during inference.\"\n\n**7) Cross-Environment Invariance:**\nNot mentioned in the provided content.\n\n**8) VLA Model Adaptation:**\nNo discussion of vision-language models or VLA applicability appears in this abstract.",
    "durationMs": 7801,
    "url": "https://arxiv.org/abs/2506.07851"
  },
  "sourceToolAssistantUUID": "a722fc9a-aaf3-4b4b-9806-a1ef6baa18ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-13T04:42:11.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BEbqjXv7s8NhG8WqDFdmYA`</summary>

```json
{
  "query": "OTPrune distribution-aligned visual token pruning optimal transport arXiv 2602.20205"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b73dc613-c39f-4ee1-8a8e-0ecf33f9c7fe",
  "isSidechain": false,
  "requestId": "req_011CayxLubG5YrS6mdtydpwi",
  "type": "assistant",
  "uuid": "c0f9bf9b-055a-436f-bfc2-360360663273",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNGuC2ZTXn1MFZBwDaYDZH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 493,
      "cache_read_input_tokens": 64528,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 493,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 64528,
          "cache_creation_input_tokens": 493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 493
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

_source line 119 · 2026-05-13T04:42:18.182Z_

<details><summary>↩ Tool result · `toolu_01BEbqjXv7s8NhG8WqDFdmYA`</summary>

```text
Web search results for query: "OTPrune distribution-aligned visual token pruning optimal transport arXiv 2602.20205"

Links: [{"title":"[2602.20205] OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport","url":"https://arxiv.org/abs/2602.20205"},{"title":"OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport","url":"https://arxiv.org/html/2602.20205"},{"title":"GitHub - xiwenc1/OTPrune: Official code for the paper: OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport · GitHub","url":"https://github.com/xiwenc1/OTPrune"},{"title":"Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/html/2604.12035"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Efficient token pruning in Vision Transformers using an attention-based Multilayer Network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425010711"},{"title":"TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model","url":"https://arxiv.org/html/2503.18278v1"},{"title":"IDPruner: Harmonizing Importance and Diversity in Visual Token Pruning for MLLMs","url":"https://arxiv.org/html/2602.13315"},{"title":"[2602.23734] UTPTrack: Towards Simple and Unified Token Pruning for Visual Tracking","url":"https://arxiv.org/abs/2602.23734"},{"title":"[2602.03815] Fast-Slow Efficient Training for Multimodal Large Language Models via Visual Token Pruning","url":"https://arxiv.org/abs/2602.03815"}]

I found detailed information about OTPrune (arXiv 2602.20205). Here's a summary:

## Overview

OTPrune is a training-free framework that formulates pruning as distribution alignment via optimal transport (OT), minimizing the 2-Wasserstein distance between the full and pruned token distributions.

## Problem and Motivation

Multi-modal large language models (MLLMs) achieve strong visual-language reasoning but suffer from high inference cost due to redundant visual tokens. Existing pruning methods overlook the underlying distributional structure of visual representations.

## Key Contributions

OTPrune preserves both local diversity and global representativeness while reducing inference cost. The framework derives a tractable submodular objective that enables efficient optimization, and theoretically proves its monotonicity and submodularity, providing a principled foundation for stable and efficient pruning.

## Performance

OTPrune achieves ~90% token reduction with minimal performance drop. Across diverse image and video benchmarks, OTPrune achieves superior accuracy–efficiency trade-offs compared to state-of-the-art methods such as FastV, VTW, and DivPrune.

## Implementation

OTPrune is a training-free visual token pruning framework for Multi-modal Large Language Models (MLLMs), and the code is available at https://github.com/xiwenc1/OTPrune.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f9bf9b-055a-436f-bfc2-360360663273",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "14581fe3-ae2b-48e4-8c58-9bdf6c73c69c",
  "toolUseResult": {
    "query": "OTPrune distribution-aligned visual token pruning optimal transport arXiv 2602.20205",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AYWLWDJVKzFDpPCxn13Q2v",
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
            "title": "[2602.23734] UTPTrack: Towards Simple and Unified Token Pruning for Visual Tracking",
            "url": "https://arxiv.org/abs/2602.23734"
          },
          {
            "title": "[2602.03815] Fast-Slow Efficient Training for Multimodal Large Language Models via Visual Token Pruning",
            "url": "https://arxiv.org/abs/2602.03815"
          }
        ]
      },
      "I found detailed information about OTPrune (arXiv 2602.20205). Here's a summary:\n\n## Overview\n\nOTPrune is a training-free framework that formulates pruning as distribution alignment via optimal transport (OT), minimizing the 2-Wasserstein distance between the full and pruned token distributions.\n\n## Problem and Motivation\n\nMulti-modal large language models (MLLMs) achieve strong visual-language reasoning but suffer from high inference cost due to redundant visual tokens. Existing pruning methods overlook the underlying distributional structure of visual representations.\n\n## Key Contributions\n\nOTPrune preserves both local diversity and global representativeness while reducing inference cost. The framework derives a tractable submodular objective that enables efficient optimization, and theoretically proves its monotonicity and submodularity, providing a principled foundation for stable and efficient pruning.\n\n## Performance\n\nOTPrune achieves ~90% token reduction with minimal performance drop. Across diverse image and video benchmarks, OTPrune achieves superior accuracy–efficiency trade-offs compared to state-of-the-art methods such as FastV, VTW, and DivPrune.\n\n## Implementation\n\nOTPrune is a training-free visual token pruning framework for Multi-modal Large Language Models (MLLMs), and the code is available at https://github.com/xiwenc1/OTPrune."
    ],
    "durationSeconds": 6.296344746000017
  },
  "sourceToolAssistantUUID": "c0f9bf9b-055a-436f-bfc2-360360663273",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-13T04:42:21.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VdNM5G3PGWfPdyLmd938h4`</summary>

```json
{
  "query": "amortized causal inference scalability token level vision transformer limitations practical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14581fe3-ae2b-48e4-8c58-9bdf6c73c69c",
  "isSidechain": false,
  "requestId": "req_011CayxMcKxXnYBXGaHo8TCV",
  "type": "assistant",
  "uuid": "f6344ab9-3bd1-438e-a02e-4c70e1b9c973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Y5sebCpAYhhWDVuAqPbyM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 960,
      "cache_read_input_tokens": 65021,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 960,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 65021,
          "cache_creation_input_tokens": 960,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 960
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

_source line 121 · 2026-05-13T04:42:29.044Z_

<details><summary>↩ Tool result · `toolu_01VdNM5G3PGWfPdyLmd938h4`</summary>

```text
Web search results for query: "amortized causal inference scalability token level vision transformer limitations practical"

Links: [{"title":"Demystifying amortized causal discovery with transformers","url":"https://arxiv.org/html/2405.16924"},{"title":"Demystifying amortized causal discovery with transformers | OpenReview","url":"https://openreview.net/forum?id=9Lgy7IGSfp"},{"title":"[2405.16924] Demystifying amortized causal discovery with transformers","url":"https://arxiv.org/abs/2405.16924"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v3"},{"title":"Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters","url":"https://arxiv.org/html/2411.03312v2"},{"title":"(PDF) CausalPFN: Amortized Causal Effect Estimation via In-Context Learning","url":"https://www.researchgate.net/publication/392530668_CausalPFN_Amortized_Causal_Effect_Estimation_via_In-Context_Learning"},{"title":"Towards Efficient Large Vision-Language Models: A Comprehensive Survey on Inference Strategies","url":"https://arxiv.org/html/2603.27960v2"},{"title":"Efficient Inference of Large Vision Language Models","url":"https://arxiv.org/html/2603.27960v1"},{"title":"[2411.03312] Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters","url":"https://arxiv.org/abs/2411.03312"},{"title":"Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters | OpenReview","url":"https://openreview.net/forum?id=6VhDQP7WGX"}]

I've completed the web search for your query. The results cover several related topics:

## Key Findings:

**Amortized Causal Inference with Transformers:**
Recent methods leverage supervised learning for amortized inference of causal graphs, optimizing an inference model to directly predict causal structure from newly provided data. However, these approaches often lack a clear connection to existing causal discovery theory, making their outputs generally unreliable.

A specific limitation discovered in research is that amortized causal discovery methods struggle when test data are out-of-distribution, generated by causal models with different mechanism types and noise distributions than those used for training, which is a relevant practical finding.

**Token-Level Vision Transformer Scalability:**
The quadratic computational complexity of the attention mechanism results in high memory usage and slow inference, which token reduction addresses by reducing the number of tokens processed during inference.

The length of visual tokens increases drastically in Large Vision Language Models, introducing a computational burden that scales quadratically with token length. Additionally, while current methods have made significant progress in mitigating quadratic complexity of self-attention, several open challenges exist, particularly the shift toward continuous video streaming demands sophisticated solutions beyond static heuristics.

**Practical Trade-offs:**
Real-world deployment of Vision Language Models is often constrained by high latency during inference, and one can either downsize the LLM or reduce the number of input tokens needed to represent the image.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6344ab9-3bd1-438e-a02e-4c70e1b9c973",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "f473f908-646f-4954-9f1a-deecade3170f",
  "toolUseResult": {
    "query": "amortized causal inference scalability token level vision transformer limitations practical",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BA6UQiWz5gFbJdVWZfbNAv",
        "content": [
          {
            "title": "Demystifying amortized causal discovery with transformers",
            "url": "https://arxiv.org/html/2405.16924"
          },
          {
            "title": "Demystifying amortized causal discovery with transformers | OpenReview",
            "url": "https://openreview.net/forum?id=9Lgy7IGSfp"
          },
          {
            "title": "[2405.16924] Demystifying amortized causal discovery with transformers",
            "url": "https://arxiv.org/abs/2405.16924"
          },
          {
            "title": "Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality",
            "url": "https://arxiv.org/html/2505.18227v3"
          },
          {
            "title": "Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters",
            "url": "https://arxiv.org/html/2411.03312v2"
          },
          {
            "title": "(PDF) CausalPFN: Amortized Causal Effect Estimation via In-Context Learning",
            "url": "https://www.researchgate.net/publication/392530668_CausalPFN_Amortized_Causal_Effect_Estimation_via_In-Context_Learning"
          },
          {
            "title": "Towards Efficient Large Vision-Language Models: A Comprehensive Survey on Inference Strategies",
            "url": "https://arxiv.org/html/2603.27960v2"
          },
          {
            "title": "Efficient Inference of Large Vision Language Models",
            "url": "https://arxiv.org/html/2603.27960v1"
          },
          {
            "title": "[2411.03312] Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters",
            "url": "https://arxiv.org/abs/2411.03312"
          },
          {
            "title": "Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters | OpenReview",
            "url": "https://openreview.net/forum?id=6VhDQP7WGX"
          }
        ]
      },
      "I've completed the web search for your query. The results cover several related topics:\n\n## Key Findings:\n\n**Amortized Causal Inference with Transformers:**\nRecent methods leverage supervised learning for amortized inference of causal graphs, optimizing an inference model to directly predict causal structure from newly provided data. However, these approaches often lack a clear connection to existing causal discovery theory, making their outputs generally unreliable.\n\nA specific limitation discovered in research is that amortized causal discovery methods struggle when test data are out-of-distribution, generated by causal models with different mechanism types and noise distributions than those used for training, which is a relevant practical finding.\n\n**Token-Level Vision Transformer Scalability:**\nThe quadratic computational complexity of the attention mechanism results in high memory usage and slow inference, which token reduction addresses by reducing the number of tokens processed during inference.\n\nThe length of visual tokens increases drastically in Large Vision Language Models, introducing a computational burden that scales quadratically with token length. Additionally, while current methods have made significant progress in mitigating quadratic complexity of self-attention, several open challenges exist, particularly the shift toward continuous video streaming demands sophisticated solutions beyond static heuristics.\n\n**Practical Trade-offs:**\nReal-world deployment of Vision Language Models is often constrained by high latency during inference, and one can either downsize the LLM or reduce the number of input tokens needed to represent the image."
    ],
    "durationSeconds": 7.699007993000036
  },
  "sourceToolAssistantUUID": "f6344ab9-3bd1-438e-a02e-4c70e1b9c973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-13T04:42:32.764Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPdteYYqXgqAFgMaFqbfme`</summary>

```json
{
  "query": "TokenShapley token-level Shapley value context attribution arXiv 2507.05261 computational cost practical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f473f908-646f-4954-9f1a-deecade3170f",
  "isSidechain": false,
  "requestId": "req_011CayxNQowdm3GCGmrGwjQX",
  "type": "assistant",
  "uuid": "38f944da-ef33-4989-9811-de924de5d8fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ5vkY5ygpcBMTjczkfBoX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 65981,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 65981,
          "cache_creation_input_tokens": 887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 887
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

_source line 123 · 2026-05-13T04:42:39.939Z_

<details><summary>↩ Tool result · `toolu_01JPdteYYqXgqAFgMaFqbfme`</summary>

```text
Web search results for query: "TokenShapley token-level Shapley value context attribution arXiv 2507.05261 computational cost practical"

Links: [{"title":"[2507.05261] TokenShapley: Token Level Context Attribution with Shapley Value","url":"https://arxiv.org/abs/2507.05261"},{"title":"TokenShapley: Token Level Context Attribution with Shapley Value","url":"https://arxiv.org/html/2507.05261v2"},{"title":"TokenShapley: Token Level Context Attribution with Shapley Value - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.200/"},{"title":"Token Level Context Attribution with Shapley Value","url":"https://aclanthology.org/2025.findings-acl.200.pdf"},{"title":"Computer Science Jul 2025","url":"https://arxiv.org/list/cs/2025-07?skip=2400&show=50"},{"title":"Token Level Context Attribution with Shapley Value","url":"https://arxiv.org/pdf/2507.05261"},{"title":"The Why Behind the Action: Unveiling Internal Drivers via Agentic Attribution","url":"https://arxiv.org/html/2601.15075v2"},{"title":"GitHub - ronigold/TokenSHAP: TokenSHAP: Explain individual token importance in large language model prompts with SHAP values. Gain insights, debug models, detect biases, and enhance transparency effortlessly","url":"https://github.com/ronigold/TokenSHAP"},{"title":"Computation and Language Jul 2025","url":"https://arxiv.org/list/cs.CL/2025-07?skip=225&show=2000"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=2175&show=500"}]

## Search Results for TokenShapley

I found comprehensive information about the paper arXiv 2507.05261 on TokenShapley. Here are the key findings:

### Paper Overview

TokenShapley is a novel token-level attribution method that combines Shapley value-based data attribution with KNN-based retrieval techniques inspired by recent advances in KNN-augmented LLMs.

### Problem Addressed

Prior work has explored attribution at the sentence level, but these methods fall short when users seek attribution for specific keywords within the response, such as numbers, years, or names.

### Technical Approach

By leveraging a precomputed datastore for contextual retrieval and computing Shapley values to quantify token importance, TokenShapley provides a fine-grained data attribution approach. More specifically, the method introduces an efficient strategy for exact token-level Shapley value calculation that leverages embedding-based retrieval and weighted KNN search, eliminating the need for Monte Carlo sampling.

### Performance

Extensive evaluations on four benchmarks show that TokenShapley outperforms state-of-the-art baselines in token-level attribution, achieving an 11-23% improvement in accuracy.

### Authors and Publication

The paper was authored by Yingtai Xiao, Yuqing Zhu, Sirat Samyoun, Wanrong Zhang, Jiachen T. Wang, and Jian Du from TikTok Inc. and Princeton University. It was published in the Findings of the Association for Computational Linguistics (ACL 2025) in July 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38f944da-ef33-4989-9811-de924de5d8fd",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "51713116-e486-486b-b7b2-f9716e0ea402",
  "toolUseResult": {
    "query": "TokenShapley token-level Shapley value context attribution arXiv 2507.05261 computational cost practical",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W9LQpGAJLBZvNHW9w3L2sy",
        "content": [
          {
            "title": "[2507.05261] TokenShapley: Token Level Context Attribution with Shapley Value",
            "url": "https://arxiv.org/abs/2507.05261"
          },
          {
            "title": "TokenShapley: Token Level Context Attribution with Shapley Value",
            "url": "https://arxiv.org/html/2507.05261v2"
          },
          {
            "title": "TokenShapley: Token Level Context Attribution with Shapley Value - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.200/"
          },
          {
            "title": "Token Level Context Attribution with Shapley Value",
            "url": "https://aclanthology.org/2025.findings-acl.200.pdf"
          },
          {
            "title": "Computer Science Jul 2025",
            "url": "https://arxiv.org/list/cs/2025-07?skip=2400&show=50"
          },
          {
            "title": "Token Level Context Attribution with Shapley Value",
            "url": "https://arxiv.org/pdf/2507.05261"
          },
          {
            "title": "The Why Behind the Action: Unveiling Internal Drivers via Agentic Attribution",
            "url": "https://arxiv.org/html/2601.15075v2"
          },
          {
            "title": "GitHub - ronigold/TokenSHAP: TokenSHAP: Explain individual token importance in large language model prompts with SHAP values. Gain insights, debug models, detect biases, and enhance transparency effortlessly",
            "url": "https://github.com/ronigold/TokenSHAP"
          },
          {
            "title": "Computation and Language Jul 2025",
            "url": "https://arxiv.org/list/cs.CL/2025-07?skip=225&show=2000"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-07?skip=2175&show=500"
          }
        ]
      },
      "## Search Results for TokenShapley\n\nI found comprehensive information about the paper arXiv 2507.05261 on TokenShapley. Here are the key findings:\n\n### Paper Overview\n\nTokenShapley is a novel token-level attribution method that combines Shapley value-based data attribution with KNN-based retrieval techniques inspired by recent advances in KNN-augmented LLMs.\n\n### Problem Addressed\n\nPrior work has explored attribution at the sentence level, but these methods fall short when users seek attribution for specific keywords within the response, such as numbers, years, or names.\n\n### Technical Approach\n\nBy leveraging a precomputed datastore for contextual retrieval and computing Shapley values to quantify token importance, TokenShapley provides a fine-grained data attribution approach. More specifically, the method introduces an efficient strategy for exact token-level Shapley value calculation that leverages embedding-based retrieval and weighted KNN search, eliminating the need for Monte Carlo sampling.\n\n### Performance\n\nExtensive evaluations on four benchmarks show that TokenShapley outperforms state-of-the-art baselines in token-level attribution, achieving an 11-23% improvement in accuracy.\n\n### Authors and Publication\n\nThe paper was authored by Yingtai Xiao, Yuqing Zhu, Sirat Samyoun, Wanrong Zhang, Jiachen T. Wang, and Jian Du from TikTok Inc. and Princeton University. It was published in the Findings of the Association for Computational Linguistics (ACL 2025) in July 2025."
    ],
    "durationSeconds": 7.17093454300001
  },
  "sourceToolAssistantUUID": "38f944da-ef33-4989-9811-de924de5d8fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 124 · 2026-05-13T04:42:39.942Z_

```json
{
  "parentUuid": "51713116-e486-486b-b7b2-f9716e0ea402",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c81d00b0-879a-47b2-9bf3-09978e1c3e12",
  "timestamp": "2026-05-13T04:42:39.942Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 125 · 2026-05-13T04:42:46.311Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hbi5paBmSpfqBYpoa2BwFH`</summary>

```json
{
  "query": "\"invariant risk minimization\" OR \"V-REx\" robotics imitation learning token selection empirical failure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c81d00b0-879a-47b2-9bf3-09978e1c3e12",
  "isSidechain": false,
  "requestId": "req_011CayxPDRrrP8yy35wCeAQG",
  "type": "assistant",
  "uuid": "4509064d-2357-419b-9c83-873dfdce309a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7VScCZ1wBapFHGTdq6UVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 66868,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 66868,
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

_source line 126 · 2026-05-13T04:42:59.631Z_

<details><summary>↩ Tool result · `toolu_01Hbi5paBmSpfqBYpoa2BwFH`</summary>

```text
Web search results for query: ""invariant risk minimization" OR "V-REx" robotics imitation learning token selection empirical failure"

Links: [{"title":"Out-of-Distribution Generalization via Risk Extrapolation","url":"http://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf"},{"title":"Meta-Learned Invariant Risk Minimization","url":"https://arxiv.org/pdf/2103.12947"},{"title":"Invariant Risk Minimization Is A Total Variation Model","url":"https://arxiv.org/pdf/2405.01389"},{"title":"Bayesian Invariant Risk Minimization Yong Lin1* Hanze Dong1* Hao Wang2","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Lin_Bayesian_Invariant_Risk_Minimization_CVPR_2022_paper.pdf"},{"title":"OUT-OF-DISTRIBUTION GENERALIZATION VIA RISK ...","url":"https://causalrlworkshop.github.io/pdf/CLDM_11.pdf"},{"title":"An Empirical Study of Invariant Risk Minimization on Deep Models","url":"https://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-044.pdf"},{"title":"Invariant Risk Minimization","url":"https://arxiv.org/pdf/1907.02893"},{"title":"[1907.02893] Invariant Risk Minimization","url":"https://arxiv.org/abs/1907.02893"},{"title":"Invariant Risk Minimization Is A Total Variation Model","url":"https://proceedings.mlr.press/v235/lai24c.html"},{"title":"Exploring invariance in Machine Learning #2: Invariant Risk Minimization | lgmoneda","url":"https://lgmoneda.github.io/2021/05/27/invariant-risk-minimization.html"}]

Now let me search more specifically for robotics, imitation learning, and token selection aspects:

Links: [{"title":"In-Context Imitation Learning via Next-Token Prediction","url":"https://arxiv.org/html/2408.15980v1"},{"title":"A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics","url":"https://arxiv.org/html/2604.15215"},{"title":"Ch. 21 - Imitation Learning - Underactuated Robotics","url":"https://underactuated.mit.edu/imitation.html"},{"title":"In-Context Imitation Learning via Next-Token Prediction","url":"https://icrt.dev/"},{"title":"[2403.19578] Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics","url":"https://arxiv.org/abs/2403.19578"},{"title":"Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics","url":"https://arxiv.org/html/2403.19578v1"},{"title":"Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics | OpenReview","url":"https://openreview.net/forum?id=6QKttpbRS1"},{"title":"In-Context Imitation Learning via Next-Token Prediction","url":"https://www.research.autodesk.com/publications/in-context-imitation-learning-via-next-token-prediction/"},{"title":"Action Tokenizer Matters in In-Context Imitation Learning","url":"https://arxiv.org/pdf/2503.1206"},{"title":"CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent Action Flow Matching for Robotic Manipulation","url":"https://arxiv.org/html/2601.23087"}]

Links: [{"title":"UNDERSTANDING DOMAIN GENERALIZATION","url":"https://openreview.net/pdf?id=I2mIxuXA72"},{"title":"Out-of-Distribution Generalization via Risk Extrapolation","url":"https://arxiv.org/pdf/2003.00688"},{"title":"[2003.00688] Out-of-Distribution Generalization via Risk Extrapolation (REx)","url":"https://arxiv.org/abs/2003.00688"},{"title":"Out-of-Distribution Generalization via Risk Extrapolation","url":"http://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf"},{"title":"Domain generalization without excess empirical risk | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601243"},{"title":"REX: Designing User-centered Repair and Explanations to Address Robot Failures","url":"https://arxiv.org/html/2405.16710v1"},{"title":"An Empirical Investigation of Domain Generalization ... - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9806840/"},{"title":"Why Domain Generalization Fail? A View of Necessity and Sufficiency","url":"https://arxiv.org/html/2502.10716v1"},{"title":"Failure Modes of Domain Generalization Algorithms","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Galstyan_Failure_Modes_of_Domain_Generalization_Algorithms_CVPR_2022_paper.pdf"},{"title":"A Study on Domain Generalization for Failure Detection through Human Reactions in HRI","url":"https://arxiv.org/html/2403.06315"}]

Based on my search results, I've found comprehensive information on the components of your query. Here's a summary of what the research shows:

## Invariant Risk Minimization (IRM) and V-REx

Invariant Risk Minimization (IRM) is a learning paradigm to estimate invariant correlations across multiple training distributions, where IRM learns a data representation such that the optimal classifier, on top of that data representation, matches for all training distributions.

Risk Extrapolation (REx) proposes a penalty on the variance of training risks (V-REx) as a simpler variant, motivating this approach as a form of robust optimization over a perturbation set of extrapolated domains (MM-REx).

## Empirical Failures

Both IRM and V-REx have documented failure modes. IRMv1 can guarantee to find optimal invariant classifier under the condition that the number of spurious correlations is smaller than the number of training environments, but with simple violation of this condition, IRMv1 can catastrophically fail to generalize for out-of-distribution.

IRMv1 achieves 67.45% test accuracy when provided with 50K training data, whereas only preserves 26% test accuracy with 5K training samples. Additionally, IRMv1, REx, RVP and IRMGame all fail on both ResNet-50(2Env) and ResNet-50(4Env).

Empirically, domain generalization algorithms like V-REx can be beneficial in certain synthetic circumstances where label noise is non-negligible and spurious correlation is severe. However, in general cases with noisy real-world data and pretrained models, there is still no clear evidence that domain generalization algorithms yield better performance.

## Token Selection in Robotics Imitation Learning

Regarding token selection in robotics imitation learning, recent work has focused on action tokenization. In in-context imitation learning, observations and actions within prompt demonstrations are tokenized into prompt tokens, providing contextual information, and an autoregressive transformer subsequently processes these tokens to generate action predictions for a new sequence of query observations.

Conventional action tokenizers in imitation learning fail to preserve temporal smoothness, whereas improved approaches enforce the Lipschitz condition into the latent space, improving landscape smoothness and noise robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4509064d-2357-419b-9c83-873dfdce309a",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "4cc6fd8d-fbdf-49d5-9b6f-4f1bdac5bfe9",
  "toolUseResult": {
    "query": "\"invariant risk minimization\" OR \"V-REx\" robotics imitation learning token selection empirical failure",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ug22zcPdhemfTHab6tbbhV",
        "content": [
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation",
            "url": "http://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf"
          },
          {
            "title": "Meta-Learned Invariant Risk Minimization",
            "url": "https://arxiv.org/pdf/2103.12947"
          },
          {
            "title": "Invariant Risk Minimization Is A Total Variation Model",
            "url": "https://arxiv.org/pdf/2405.01389"
          },
          {
            "title": "Bayesian Invariant Risk Minimization Yong Lin1* Hanze Dong1* Hao Wang2",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/papers/Lin_Bayesian_Invariant_Risk_Minimization_CVPR_2022_paper.pdf"
          },
          {
            "title": "OUT-OF-DISTRIBUTION GENERALIZATION VIA RISK ...",
            "url": "https://causalrlworkshop.github.io/pdf/CLDM_11.pdf"
          },
          {
            "title": "An Empirical Study of Invariant Risk Minimization on Deep Models",
            "url": "https://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-044.pdf"
          },
          {
            "title": "Invariant Risk Minimization",
            "url": "https://arxiv.org/pdf/1907.02893"
          },
          {
            "title": "[1907.02893] Invariant Risk Minimization",
            "url": "https://arxiv.org/abs/1907.02893"
          },
          {
            "title": "Invariant Risk Minimization Is A Total Variation Model",
            "url": "https://proceedings.mlr.press/v235/lai24c.html"
          },
          {
            "title": "Exploring invariance in Machine Learning #2: Invariant Risk Minimization | lgmoneda",
            "url": "https://lgmoneda.github.io/2021/05/27/invariant-risk-minimization.html"
          }
        ]
      },
      "Now let me search more specifically for robotics, imitation learning, and token selection aspects:",
      {
        "tool_use_id": "srvtoolu_01SgaXotwhwoizakEFCrzyAs",
        "content": [
          {
            "title": "In-Context Imitation Learning via Next-Token Prediction",
            "url": "https://arxiv.org/html/2408.15980v1"
          },
          {
            "title": "A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics",
            "url": "https://arxiv.org/html/2604.15215"
          },
          {
            "title": "Ch. 21 - Imitation Learning - Underactuated Robotics",
            "url": "https://underactuated.mit.edu/imitation.html"
          },
          {
            "title": "In-Context Imitation Learning via Next-Token Prediction",
            "url": "https://icrt.dev/"
          },
          {
            "title": "[2403.19578] Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics",
            "url": "https://arxiv.org/abs/2403.19578"
          },
          {
            "title": "Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics",
            "url": "https://arxiv.org/html/2403.19578v1"
          },
          {
            "title": "Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics | OpenReview",
            "url": "https://openreview.net/forum?id=6QKttpbRS1"
          },
          {
            "title": "In-Context Imitation Learning via Next-Token Prediction",
            "url": "https://www.research.autodesk.com/publications/in-context-imitation-learning-via-next-token-prediction/"
          },
          {
            "title": "Action Tokenizer Matters in In-Context Imitation Learning",
            "url": "https://arxiv.org/pdf/2503.1206"
          },
          {
            "title": "CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent Action Flow Matching for Robotic Manipulation",
            "url": "https://arxiv.org/html/2601.23087"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01W7CFAc67uxq3JJv55LLtoo",
        "content": [
          {
            "title": "UNDERSTANDING DOMAIN GENERALIZATION",
            "url": "https://openreview.net/pdf?id=I2mIxuXA72"
          },
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation",
            "url": "https://arxiv.org/pdf/2003.00688"
          },
          {
            "title": "[2003.00688] Out-of-Distribution Generalization via Risk Extrapolation (REx)",
            "url": "https://arxiv.org/abs/2003.00688"
          },
          {
            "title": "Out-of-Distribution Generalization via Risk Extrapolation",
            "url": "http://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf"
          },
          {
            "title": "Domain generalization without excess empirical risk | Proceedings of the 36th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3600270.3601243"
          },
          {
            "title": "REX: Designing User-centered Repair and Explanations to Address Robot Failures",
            "url": "https://arxiv.org/html/2405.16710v1"
          },
          {
            "title": "An Empirical Investigation of Domain Generalization ... - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9806840/"
          },
          {
            "title": "Why Domain Generalization Fail? A View of Necessity and Sufficiency",
            "url": "https://arxiv.org/html/2502.10716v1"
          },
          {
            "title": "Failure Modes of Domain Generalization Algorithms",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/papers/Galstyan_Failure_Modes_of_Domain_Generalization_Algorithms_CVPR_2022_paper.pdf"
          },
          {
            "title": "A Study on Domain Generalization for Failure Detection through Human Reactions in HRI",
            "url": "https://arxiv.org/html/2403.06315"
          }
        ]
      },
      "Based on my search results, I've found comprehensive information on the components of your query. Here's a summary of what the research shows:\n\n## Invariant Risk Minimization (IRM) and V-REx\n\nInvariant Risk Minimization (IRM) is a learning paradigm to estimate invariant correlations across multiple training distributions, where IRM learns a data representation such that the optimal classifier, on top of that data representation, matches for all training distributions.\n\nRisk Extrapolation (REx) proposes a penalty on the variance of training risks (V-REx) as a simpler variant, motivating this approach as a form of robust optimization over a perturbation set of extrapolated domains (MM-REx).\n\n## Empirical Failures\n\nBoth IRM and V-REx have documented failure modes. IRMv1 can guarantee to find optimal invariant classifier under the condition that the number of spurious correlations is smaller than the number of training environments, but with simple violation of this condition, IRMv1 can catastrophically fail to generalize for out-of-distribution.\n\nIRMv1 achieves 67.45% test accuracy when provided with 50K training data, whereas only preserves 26% test accuracy with 5K training samples. Additionally, IRMv1, REx, RVP and IRMGame all fail on both ResNet-50(2Env) and ResNet-50(4Env).\n\nEmpirically, domain generalization algorithms like V-REx can be beneficial in certain synthetic circumstances where label noise is non-negligible and spurious correlation is severe. However, in general cases with noisy real-world data and pretrained models, there is still no clear evidence that domain generalization algorithms yield better performance.\n\n## Token Selection in Robotics Imitation Learning\n\nRegarding token selection in robotics imitation learning, recent work has focused on action tokenization. In in-context imitation learning, observations and actions within prompt demonstrations are tokenized into prompt tokens, providing contextual information, and an autoregressive transformer subsequently processes these tokens to generate action predictions for a new sequence of query observations.\n\nConventional action tokenizers in imitation learning fail to preserve temporal smoothness, whereas improved approaches enforce the Lipschitz condition into the latent space, improving landscape smoothness and noise robustness."
    ],
    "durationSeconds": 13.314401935000031
  },
  "sourceToolAssistantUUID": "4509064d-2357-419b-9c83-873dfdce309a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 127_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "4cc6fd8d-fbdf-49d5-9b6f-4f1bdac5bfe9",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 128_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Tool call

_source line 129 · 2026-05-13T04:43:02.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELsAooV8DqqXLz7neQuD4Y`</summary>

```json
{
  "query": "causal imitation learning token-level VLA generalization spurious 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cc6fd8d-fbdf-49d5-9b6f-4f1bdac5bfe9",
  "isSidechain": false,
  "requestId": "req_011CayxQfb11EprJBuApiv7A",
  "type": "assistant",
  "uuid": "3bab1ca4-cda3-4654-9fd9-8fd3b3f75a03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018H6YAAZ1MU7KRHah3hDx7M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 67905,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 67905,
          "cache_creation_input_tokens": 2015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2015
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

_source line 130 · 2026-05-13T04:43:09.441Z_

<details><summary>↩ Tool result · `toolu_01ELsAooV8DqqXLz7neQuD4Y`</summary>

```text
Web search results for query: "causal imitation learning token-level VLA generalization spurious 2026 arXiv"

Links: [{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations","url":"https://arxiv.org/html/2507.22380"},{"title":"[2601.22206] Causal Imitation Learning Under Measurement Error and Distribution Shift","url":"https://arxiv.org/abs/2601.22206"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"[2507.22380] Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations","url":"https://arxiv.org/abs/2507.22380"},{"title":"Causal Machine Learning: A Survey and Open Problems","url":"https://arxiv.org/pdf/2206.15475"},{"title":"[2208.06267] Causal Imitation Learning with Unobserved Confounders","url":"https://arxiv.org/abs/2208.06267"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"A Survey on Reinforcement Learning of Vision-Language-Action Models for Robotic Manipulation | TechRxiv","url":"https://www.techrxiv.org/users/934012/articles/1366553/master/file/data/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf?inline=true"}]

Based on the web search results, I found several relevant papers and research directions that address your query about causal imitation learning, token-level VLAs, generalization, and spurious correlations:

## Key Findings:

**1. RobustVLA (2025)** - VLA models may rely on spurious correlations between irrelevant observation features and actions, rather than capturing the true causal relationship required for robust generalization. This paper introduces regularization techniques to address robustness issues in Vision-Language-Action models.

**2. Causal Imitation Learning for Robotic Tasks (July 2025)** - Research has addressed the problem of causal confusion in Imitation Learning (IL), where models rely on spurious correlations that impact their ability to generalize to new environments. Causal-ACT is a transformer-based IL framework that incorporates causal graph optimization to allow the policy to focus on task-relevant features.

**3. Token-Level VLA Architecture (2026)** - In token-level VLA models, images are embedded into visual tokens and action tokens are added to the vocabulary, with the network trained using next-token cross-entropy objective with loss computed solely on predicted action tokens.

**4. Causal Imitation Learning Under Distribution Shift (January 2026)** - Recent work studies offline imitation learning when part of the decision-relevant state is observed only through noisy measurements and the distribution may change between training and deployment.

The search results indicate active research in 2025-2026 on improving VLA generalization through causal methods and addressing spurious correlations in token-level models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bab1ca4-cda3-4654-9fd9-8fd3b3f75a03",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "84260295-2302-4e0d-995d-175ed05ce09e",
  "toolUseResult": {
    "query": "causal imitation learning token-level VLA generalization spurious 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qwvzu4oAe1kovfubfPALnH",
        "content": [
          {
            "title": "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.01331"
          },
          {
            "title": "Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations",
            "url": "https://arxiv.org/html/2507.22380"
          },
          {
            "title": "[2601.22206] Causal Imitation Learning Under Measurement Error and Distribution Shift",
            "url": "https://arxiv.org/abs/2601.22206"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://arxiv.org/html/2505.19789v4"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.01331v1"
          },
          {
            "title": "[2507.22380] Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations",
            "url": "https://arxiv.org/abs/2507.22380"
          },
          {
            "title": "Causal Machine Learning: A Survey and Open Problems",
            "url": "https://arxiv.org/pdf/2206.15475"
          },
          {
            "title": "[2208.06267] Causal Imitation Learning with Unobserved Confounders",
            "url": "https://arxiv.org/abs/2208.06267"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "A Survey on Reinforcement Learning of Vision-Language-Action Models for Robotic Manipulation | TechRxiv",
            "url": "https://www.techrxiv.org/users/934012/articles/1366553/master/file/data/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation/TechrxivA_Survey_on_Reinforcement_Learning_of_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf?inline=true"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and research directions that address your query about causal imitation learning, token-level VLAs, generalization, and spurious correlations:\n\n## Key Findings:\n\n**1. RobustVLA (2025)** - VLA models may rely on spurious correlations between irrelevant observation features and actions, rather than capturing the true causal relationship required for robust generalization. This paper introduces regularization techniques to address robustness issues in Vision-Language-Action models.\n\n**2. Causal Imitation Learning for Robotic Tasks (July 2025)** - Research has addressed the problem of causal confusion in Imitation Learning (IL), where models rely on spurious correlations that impact their ability to generalize to new environments. Causal-ACT is a transformer-based IL framework that incorporates causal graph optimization to allow the policy to focus on task-relevant features.\n\n**3. Token-Level VLA Architecture (2026)** - In token-level VLA models, images are embedded into visual tokens and action tokens are added to the vocabulary, with the network trained using next-token cross-entropy objective with loss computed solely on predicted action tokens.\n\n**4. Causal Imitation Learning Under Distribution Shift (January 2026)** - Recent work studies offline imitation learning when part of the decision-relevant state is observed only through noisy measurements and the distribution may change between training and deployment.\n\nThe search results indicate active research in 2025-2026 on improving VLA generalization through causal methods and addressing spurious correlations in token-level models."
    ],
    "durationSeconds": 6.580696710000048
  },
  "sourceToolAssistantUUID": "3bab1ca4-cda3-4654-9fd9-8fd3b3f75a03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 131 · 2026-05-13T04:43:13.590Z_

Now I have sufficient evidence to assess this idea comprehensively. Let me do one final check on the "spatial locality of causal features" assumption, which is central to the theoretical contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84260295-2302-4e0d-995d-175ed05ce09e",
  "isSidechain": false,
  "requestId": "req_011CayxRPVuJJ8ho4cdH3gKZ",
  "type": "assistant",
  "uuid": "8d87dc4e-b788-4032-b6f0-2b75ddcc26b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAmmYinbUGS9VhM2F7y4T9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 69920,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 69920,
          "cache_creation_input_tokens": 1079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1079
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

_source line 132 · 2026-05-13T04:43:13.771Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015MBACL6ghh4yRovkNkNX5A`</summary>

```json
{
  "query": "\"spatial locality\" assumption visual tokens causal features robot manipulation evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d87dc4e-b788-4032-b6f0-2b75ddcc26b7",
  "isSidechain": false,
  "requestId": "req_011CayxRPVuJJ8ho4cdH3gKZ",
  "type": "assistant",
  "uuid": "78ade2bf-8a5d-4f17-a41b-913fe032d5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAmmYinbUGS9VhM2F7y4T9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 69920,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 69920,
          "cache_creation_input_tokens": 1079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1079
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

_source line 133 · 2026-05-13T04:43:24.945Z_

<details><summary>↩ Tool result · `toolu_015MBACL6ghh4yRovkNkNX5A`</summary>

```text
Web search results for query: ""spatial locality" assumption visual tokens causal features robot manipulation evidence"

Links: [{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"SpatialBot: Precise Spatial Understanding with Vision Language Models | Request PDF","url":"https://www.researchgate.net/publication/395229815_SpatialBot_Precise_Spatial_Understanding_with_Vision_Language_Models"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"[2601.21998] Causal World Modeling for Robot Control","url":"https://arxiv.org/abs/2601.21998"},{"title":"Paper page - Leveraging Locality to Boost Sample Efficiency in Robotic Manipulation","url":"https://huggingface.co/papers/2406.10615"},{"title":"SEM: Enhancing Spatial Understanding for Robust Robot Manipulation","url":"https://arxiv.org/html/2505.16196"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"VIMA | General Robot Manipulation with Multimodal Prompts","url":"https://vimalabs.github.io/assets/vima_paper.pdf"},{"title":"CoT-VLA","url":"https://cot-vla.github.io/"}]

I found relevant research on visual tokens, causal features, and robot manipulation. The search results show several papers addressing spatial reasoning and causal understanding in robotic systems, though they don't specifically discuss a "spatial locality assumption" in the exact context you queried.

Here are the key findings:

## Spatial Understanding in Robot Manipulation

Recent work leverages causal video VAEs to compress visual observations into compact latent tokens for robot control. Video world models provide the ability to "imagine" the near future by understanding the causality between actions and visual dynamics.

## Causal Reasoning and Spatial Features

RoboStream uses Spatio-Temporal Fusion Tokens (STF-Tokens) that bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This approach achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.

## Spatial Representation for Manipulation

SEM (Spatial Enhanced Manipulation) constructs a unified spatial representation by projecting multi-view image features and joint-centric robot states into a unified 3D space, providing a consistent feature space for the diffusion policy to condition on during action generation.

The evidence suggests that spatial alignment, causal reasoning between actions and visual outcomes, and structured token representations are indeed important for effective robot manipulation, though I did not find specific discussion of a "spatial locality assumption" per se in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78ade2bf-8a5d-4f17-a41b-913fe032d5a3",
  "isSidechain": false,
  "promptId": "355960e0-9029-4f7e-b302-c5ad305d399e",
  "type": "user",
  "uuid": "2c217489-0fc7-4795-b09b-bd6a68d3ab41",
  "toolUseResult": {
    "query": "\"spatial locality\" assumption visual tokens causal features robot manipulation evidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CXNtj9y7htQQ8TDHcBYqAH",
        "content": [
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v1"
          },
          {
            "title": "SpatialBot: Precise Spatial Understanding with Vision Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/395229815_SpatialBot_Precise_Spatial_Understanding_with_Vision_Language_Models"
          },
          {
            "title": "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"
          },
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "[2601.21998] Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/abs/2601.21998"
          },
          {
            "title": "Paper page - Leveraging Locality to Boost Sample Efficiency in Robotic Manipulation",
            "url": "https://huggingface.co/papers/2406.10615"
          },
          {
            "title": "SEM: Enhancing Spatial Understanding for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2505.16196"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "VIMA | General Robot Manipulation with Multimodal Prompts",
            "url": "https://vimalabs.github.io/assets/vima_paper.pdf"
          },
          {
            "title": "CoT-VLA",
            "url": "https://cot-vla.github.io/"
          }
        ]
      },
      "I found relevant research on visual tokens, causal features, and robot manipulation. The search results show several papers addressing spatial reasoning and causal understanding in robotic systems, though they don't specifically discuss a \"spatial locality assumption\" in the exact context you queried.\n\nHere are the key findings:\n\n## Spatial Understanding in Robot Manipulation\n\nRecent work leverages causal video VAEs to compress visual observations into compact latent tokens for robot control. Video world models provide the ability to \"imagine\" the near future by understanding the causality between actions and visual dynamics.\n\n## Causal Reasoning and Spatial Features\n\nRoboStream uses Spatio-Temporal Fusion Tokens (STF-Tokens) that bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This approach achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.\n\n## Spatial Representation for Manipulation\n\nSEM (Spatial Enhanced Manipulation) constructs a unified spatial representation by projecting multi-view image features and joint-centric robot states into a unified 3D space, providing a consistent feature space for the diffusion policy to condition on during action generation.\n\nThe evidence suggests that spatial alignment, causal reasoning between actions and visual outcomes, and structured token representations are indeed important for effective robot manipulation, though I did not find specific discussion of a \"spatial locality assumption\" per se in these results."
    ],
    "durationSeconds": 11.17086784900003
  },
  "sourceToolAssistantUUID": "78ade2bf-8a5d-4f17-a41b-913fe032d5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 134 · 2026-05-13T04:45:19.313Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all my findings and provide a thorough review.

## Summary of my research findings:

### SOTA verification:
- SRPO indeed achieves 82.1% average success rate on LIBERO-Plus (confirmed via WebFetch of the actual paper). This appears to be the current published SOTA.
- FTM achieves 87.1% on LIBERO viewpoint only (not the full LIBERO-Plus benchmark with all 7 perturbation dimensions). The generator correctly notes this.

### Reference verification:
All key references checked out:


- Causal-ACT (arXiv 2507.22380) exists and operates at the feature level in ResNet+ACT rather than as a VLA
- FTM (arXiv 2512.02902) exists with 4K params, tested only on LIBERO viewpoint
- LeaF (NeurIPS 2025, arXiv 2506.07851) exists and focuses on NLP
- arXiv 2502.11501 (ACL Findings 2025) exists and demonstrates that attention pruning underperforms random baselines
- ACTIVA (arXiv 2503.01290) is also verified

, using amortized causal estimation
- SRPO (arXiv 2511.15605) exists with 82.1% performance on LIBERO-Plus
- AVA-VLA (arXiv 2511.18960) exists

The claimed gap appears valid—no existing work combines formal token-level causal intervention with amortized scalable estimation in VLA transformers. Causal-ACT operates at feature level in ResNets, LeaF works at token level but in NLP contexts, and existing VLA pruning methods don't use formal causal intervention criteria.

The generator has addressed all round 1 issues. However, I'm noticing DTP (arXiv 2601.16065) on distracting token pruning is conceptually similar to CaTS's goal of removing spuriously correlated tokens, though it relies on attention-based detection rather than causal intervention—this should be discussed.

Beyond that, there are several other recent works using different approaches to token selection in VLAs: FocusVLA uses dynamic patch selection via attention mechanisms, TIES applies inter-layer rank consistency for robustness, BFA++ employs hierarchical importance predictors, Compressor-VLA does instruction-guided compression, LightVLA uses differentiable gradient-based pruning, and CRT appears to be another relevant method—all addressing task-relevant token selection but without formal causal intervention. The submission deadlines are tight across venues — CoRL is only 16 days away, while AAAI, ICLR, and ICRA all fall in the plausible range for a 2027 conference cycle. Looking at the theoretical analysis, the proposal directly addresses the user's request by grounding token pruning in a formal structural causal model, introducing explicit assumptions about spatial locality of causal features, and using V-REx to avoid known pitfalls with IRM — all backed by concrete failure modes and theorem sketches.

But I'm noticing some real gaps in the theory: there's no actual proof provided, just a sketch, and the spatial locality assumption feels quite strong given that Vision Transformers explicitly mix information across tokens through self-attention. The environment diversity assumption (A3) carries over IRM's fundamental limitations without resolving them, and V-REx doesn't actually solve IRM's core problems in non-linear settings the way the framing suggests. The ε-invariance bounds depend on N_env and M in ways that might not be tight enough to matter empirically. On the feasibility side, 700 hours of A100 compute for manual mode seems reasonable for the scale they're proposing.

The Shapley value computation at the token level is going to be computationally intensive even with amortization, and the batch stochastic interventions approach—replacing embeddings with environment statistics—is creative but unproven in terms of whether it actually produces meaningful causal signals. Reproducing nine baselines is ambitious though the cost looks manageable, and the 3-5 week timeline for the auto research phase feels achievable. What's genuinely novel here is combining causal intervention for imitation learning robustness with vision-language token pruning and causal attention distillation, which sits at an interesting intersection of three different research directions.

The formal causal framework is the real differentiator from similar work like DTP and FocusVLA that also identify task-relevant tokens, though the theory is still somewhat sketchy. If this works, it could provide principled insight into why token selection matters for VLA generalization—which directly addresses what's being asked. The interpretability angle where causal scores map to task-relevant regions is valuable, but the field is moving fast with many concurrent pruning methods emerging in this timeframe. The computational cost is substantial at around 700 hours on A100s, though the budget seems feasible. The main weaknesses are that several recent competing works aren't cited, the spatial locality assumption may be violated by ViT's global attention patterns, and V-REx doesn't fundamentally solve IRM's non-linear limitations despite the framing suggesting otherwise. The theorem lacks a formal proof, and computing Shapley decomposition across 256 tokens presents real computational challenges.

Now I'm reconsidering the novelty score — while the formal causal intervention framework at the token level is genuinely novel compared to attention or gradient-based approaches like DTP and FocusVLA, the theoretical foundation is still underdeveloped and the practical amortization gap remains unquantified.

On feasibility, the technical complexity is substantial with the Shapley value estimation, batch interventions, and variance penalties all presenting real engineering challenges, though the resource estimates seem plausible.

The proposal is clearly structured and explicit about its assumptions, but the theoretical contribution that sets it apart is still somewhat sketchy. If this works, it would offer a principled causal understanding of VLA generalization, which directly answers the core question, though the field's rapid pace means impact could be limited.

Averaging the scores gives 3.625, which falls short of the 4.0 threshold. The core problems are that recent competing methods aren't addressed, the theory remains underdeveloped from the first round, the V-REx approach doesn't fully resolve IRM's non-linearity issues, and the spatial locality assumption might not hold in Vision Transformers.

The verdict is to revise. Most of these issues are addressable — missing citations are straightforward to add, and the theory can be developed further — though the theoretical underdevelopment was already a concern from the previous feedback.

The spatial locality assumption is the trickiest problem. In Vision Transformers, tokens eventually attend to all other tokens across layers, so the assumption that causal features remain spatially localized breaks down in deeper layers. The authors should clarify whether this assumption only applies to early layers and what that means for where to apply causal scoring. The V-REx limitations also need more explicit discussion, even though the authors already acknowledge they're providing distributional robustness rather than strict invariance guarantees.

All of these are fixable with more work. Now I'm finalizing the individual scores.

For novelty, I initially thought 3, but the revision actually strengthened the positioning significantly. The combination of formal SCM, amortized scoring, and explicit failure modes is genuinely novel—none of the competing approaches like DTP or FocusVLA provide this level of causal formalism, even if they're converging on similar motivations around task-relevant token selection. I'll bump this to 3.5.

Feasibility sits at 3. The Shapley decomposition at token scale is risky, generating intervention data is non-trivial, and the amortization gap remains uncharacterized. But the resource estimates look reasonable and the core building blocks already exist.

Actually, 3 might be too conservative here. The approach leverages existing components—frozen VLA, LoRA, KL divergence—and the resource projections are realistic. The main risk is really just the Shapley decomposition. I'll revise to 3.5.

Clarity is strong at 4—the proposal is well-structured with a clear problem statement, explicit SCM, documented assumptions and failure modes, and a detailed evaluation plan.

Impact lands at 3.5. There's a genuine need for principled token selection in VLAs, and the interpretability angle is valuable. But the real impact hinges on whether this outperforms simpler alternatives empirically.

That gives me an average of 3.625, which falls below 4.0, so the verdict is revise. Though I should double-check the "spatial locality of causal features" assumption—that's really the crux of the theoretical insight here.

The core claim is that task-relevant information like object poses and gripper state clusters in specific tokens, while spurious features like background and lighting scatter across many tokens. In raw image space that's clearly true, and ViT tokens still map to specific patches. But after multiple transformer layers, information gets heavily mixed through self-attention. A background token might have absorbed object information, and vice versa, so the clean separation between causal and spurious content at the token level breaks down deeper in the network. The proposal uses embeddings from the frozen VLA backbone, which means I need to think about what layer depth we're actually working with here.

Recent work like DTP and FocusVLA shows that token-level selection does improve VLA performance, which suggests spatial relevance structure survives even in late layers. So the assumption isn't fundamentally flawed, just needs solid empirical validation. I'll go with my scores: novelty 3.5, feasibility 3.5, clarity 4, impact 3.5, averaging 3.625. That points to a revise verdict. Though I should double-check the novelty claim more carefully—the authors are saying they're the first to combine formal causal intervention criteria with scalable amortized estimation in VLA architectures for cross-environment policy invariance.

Looking at what's actually novel here: the formal SCM framework applied to the VLA token-action pipeline, amortized causal scoring at the token level, using variance regularization for token selection, and connecting causal imitation learning with VLA pruning and attention distillation. The existing work—Causal-ACT, LeaF, DTP, FocusVLA, LightVLA—all approach this differently, whether through feature-level interventions, gradient heuristics, or attention mechanisms without causal formalism. So the novelty is legitimate, though it's more theoretical in nature—applying a causal framework to an existing problem space.

The real tension is whether this theoretical contribution justifies the added complexity when simpler empirical methods might achieve similar results. I'll keep the novelty score at 3.5 and refocus on what the user actually asked for: theoretical analysis of why token pruning and augmentation improve generalization in VLAs. The revised proposal does address this better than the first attempt—it provides the SCM formalization, spatial locality assumptions, a sketch of conditional invariance, explicit failure modes, and connects to V-REx. This theoretical grounding is much closer to what was requested.

But for a top-tier venue, these theoretical claims need to be rigorous. The conditional invariance theorem can't stay as a sketch—it needs a full proof with concrete bounds. The spatial locality assumption requires formal definition and analysis of when it actually holds or breaks down. Right now it's promising but incomplete.

Looking at the overall assessment, I'm settling on novelty at 3.5, feasibility at 3.5, clarity at 4, and impact at 3.5, averaging to 3.625. The verdict is to revise. The main gaps are missing recent concurrent work like DTP, FocusVLA, LightVLA, TIES, BFA++, and Compressor-VLA that need to be addressed.

Beyond that, I need to be more rigorous about how ViT self-attention actually affects the spatial locality assumption, acknowledge that V-REx doesn't fully solve IRM's non-linear problems, move the theorem beyond sketch status with actual proofs, and provide quantitative analysis of the amortization gap rather than leaving it theoretical.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c217489-0fc7-4795-b09b-bd6a68d3ab41",
  "isSidechain": false,
  "requestId": "req_011CayxSXn1HtwK19PcLiYwm",
  "type": "assistant",
  "uuid": "3caa201a-dc49-4e64-84ac-0dc4ec3306db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HC8aFj5npYpXVoCogsYU4E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 70999,
      "output_tokens": 7184,
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
          "output_tokens": 7184,
          "cache_read_input_tokens": 70999,
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

### Assistant

_source line 135 · 2026-05-13T04:46:05.644Z_

I've completed extensive research. Let me now synthesize my findings into the review.

**Key findings from my independent verification:**

1. **SRPO 82.1% on LIBERO-Plus**: Confirmed via full paper fetch — this is indeed the average success rate.
2. **All cited papers verified**: Causal-ACT, FTM, LeaF, ACTIVA, SRPO, AVA-VLA all exist and are accurately described.
3. **FTM evaluated on LIBERO viewpoint only**: Confirmed — the generator correctly notes this limitation.
4. **V-REx has same fundamental limitations as IRM in non-linear settings**: Confirmed via literature.
5. **Several important concurrent works missing**: DTP, FocusVLA, LightVLA, TIES, BFA++, Compressor-VLA, Gaze-Regularized VLA — all from late 2025 to March 2026.
6. **The claimed research gap appears valid**: No existing work combines formal causal intervention criteria + token-level selection + amortized estimation in VLA transformers.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The bridging of causal IL (Causal-ACT), VLA token pruning, and causal attention distillation (LeaF) via a formal SCM is genuinely novel — no existing paper combines these. However, DTP (arXiv 2601.16065), FocusVLA (arXiv 2603.28740), and LightVLA (arXiv 2509.12594/ICRA 2026) all pursue 'which tokens matter for task performance' via different mechanisms, narrowing the novelty gap more than acknowledged. The causal formalism is the key differentiator but remains a 'sketch' rather than a proven theorem."},
    "feasibility": {"score": 3.5, "rationale": "The resource estimates are internally consistent and realistic. However, the Shapley-value decomposition for 256 tokens across 7 perturbation types is computationally demanding even in amortized form, and the amortization gap (F3) is uncharacterized quantitatively. The batch stochastic intervention scheme (replacing token embeddings with environment-marginal statistics) is untested and may not produce clean causal signals due to ViT's global attention mixing."},
    "clarity": {"score": 4, "rationale": "Significantly improved from round 1. The SCM is explicit with four named assumptions (A1-A4), three documented failure modes (F1-F3), and clear differentiation from each competitor. The evaluation plan with 9 baselines is comprehensive."},
    "impact": {"score": 3.5, "rationale": "Addresses the user's core request for theoretical analysis of WHY token selection enhances VLA generalization. If the theory is fully developed and empirically validated, this would be a meaningful contribution. But the rapidly crowding field (6+ new VLA pruning papers in Q1 2026 alone) and competition from simpler methods (FTM/DTP) create risk that the added causal complexity may not yield proportional empirical gains."}
  },
  "issues": [
    "MISSING CONCURRENT WORK (6+ papers): DTP (arXiv 2601.16065, Jan 2026) prunes 'distracting tokens' in VLA — directly analogous motivation to CaTS (removing spuriously correlated tokens). FocusVLA (arXiv 2603.28740, Mar 2026) dynamically selects task-relevant visual patches via 'Focus Attention' to suppress task-irrelevant noise. LightVLA (arXiv 2509.12594, ICRA 2026) uses differentiable token pruning with Gumbel softmax to learn task-relevant token selection — a gradient-based alternative to causal selection. TIES (arXiv 2603.24941, Mar 2026) uses inter-layer rank consistency for robust token selection and explicitly evaluates robustness under environmental perturbations. BFA++ (arXiv 2602.20566, Feb 2026) uses hierarchical importance predictors. Compressor-VLA (arXiv 2511.18950) uses instruction-guided compression. Gaze-Regularized VLA (arXiv 2603.23202) aligns attention with human gaze patterns. All must be discussed and differentiated.",
    "SPATIAL LOCALITY ASSUMPTION PROBLEMATIC IN VITs: The core 'spatial locality of causal features' assumption — that task-relevant content is concentrated in a subset of tokens while spurious content is distributed — may be significantly violated in practice. ViT self-attention layers progressively mix information across ALL token positions. By late layers (which is where the frozen VLA backbone produces embeddings), a 'background' token has incorporated object information and vice versa. This undermines the clean causal/spurious separation at the token level. The proposal needs analysis of which layer's representations to score, and empirical validation that spatial locality holds sufficiently at that layer.",
    "V-REx DOES NOT FIX IRM'S NON-LINEAR PROBLEMS: The proposal frames V-REx as replacing 'the problematic IRM objective' for distributional robustness. However, V-REx has the same fundamental limitations as IRM in non-linear settings (Krueger et al. ICML 2021 acknowledge this; empirical studies show V-REx fails similarly to IRM on non-linear benchmarks). The framing should be more honest: V-REx is simpler and more stable than IRMv1, but does not escape the core failure mode. The 'distributional robustness without claiming strict invariance guarantees' language is good but the justification needs strengthening.",
    "THEOREM STILL A 'SKETCH': For a paper targeting AAAI/ICLR where the theoretical framework is the primary differentiator from simpler methods, the conditional invariance result must move beyond 'sketch' status. A full proof (or at least a detailed proof sketch with all key steps) is needed. The ε-invariance bound ε(N_env, M, τ) needs concrete functional form — otherwise reviewers will view this as hand-waving. What is the convergence rate? How many environments are sufficient? These are the questions the theory should answer.",
    "AMORTIZATION GAP UNQUANTIFIED: Failure mode F3 (amortization gap between learned scorer and true ACE) is acknowledged but not analyzed. How large is this gap expected to be? Under what conditions does it remain bounded? The ACTIVA paper (arXiv 2503.01290) that inspires the approach works on tabular data with much simpler structure — scaling to 256-dimensional token spaces in a 7B VLA is a significant leap. Some empirical or theoretical characterization of the expected gap is needed.",
    "RISK OF NEGATIVE RESULT: The paper arXiv 2502.11501 shows attention-based pruning can underperform random selection. This is used to motivate causal pruning. However, if the amortized causal scorer also underperforms random (due to amortization gap, spatial locality violations, or V-REx limitations), the paper's central claim collapses. The evaluation plan should include a formal statistical protocol for comparing against random pruning baseline to demonstrate significant improvement."
  ],
  "feedback": "The revision substantially improved the proposal from round 1 — all previously flagged issues are addressed, the SCM is formalized, IRM concerns are partially mitigated, and Mask World Model is correctly handled. The idea remains promising. To reach pass threshold:\n\n1. **Cite and differentiate from 6+ new concurrent works** (DTP, FocusVLA, LightVLA, TIES, BFA++, Compressor-VLA, Gaze-VLA). Key differentiation argument: these all use attention/gradient/geometric heuristics proven fragile by arXiv 2502.11501, while CaTS uses formal causal criteria. But acknowledge that DTP/FocusVLA achieve similar goals without causal overhead — the burden is on CaTS to show the causal framework provides measurable empirical improvement beyond interpretability.\n\n2. **Address the spatial locality assumption in ViTs seriously.** Either (a) propose scoring at early/intermediate layers where spatial locality is better preserved, with analysis of the information-quality tradeoff, or (b) provide empirical evidence from existing ViT attention analyses that task-relevant tokens remain spatially concentrated even in late layers, or (c) weaken the assumption and adjust the theory accordingly.\n\n3. **Be fully honest about V-REx limitations.** V-REx is a better choice than IRM, but it doesn't solve the non-linear problem. Frame it as 'practical heuristic with distributional robustness motivation' rather than 'principled fix for IRM.' Consider discussing connections to DRO (distributionally robust optimization) which has stronger finite-sample guarantees.\n\n4. **Develop the theorem beyond a sketch.** Provide the concrete functional form of ε(N_env, M, τ) with at least the dominant terms. Show how the bound degrades as spatial locality weakens. This is the paper's unique selling point — it must be rigorous enough to survive reviewer scrutiny at AAAI/ICLR.\n\n5. **Quantify the amortization gap.** Either theoretically (bound on approximation error of the 2-layer MLP scorer vs. true ACE) or empirically (plan to compute exact ACE on a small validation set and compare to amortized predictions, which is already in the ablation plan — make this a central validation, not just an ablation).",
  "reason": "Strong revision addressing round 1 issues, but spatial locality assumption in ViTs is under-examined, theorem remains a sketch (insufficient for top-venue theoretical paper), 6+ recent concurrent works are missing, and V-REx limitations are understated."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3caa201a-dc49-4e64-84ac-0dc4ec3306db",
  "isSidechain": false,
  "requestId": "req_011CayxSXn1HtwK19PcLiYwm",
  "type": "assistant",
  "uuid": "9b744b82-60d8-4742-bda3-e4ebc93dd839",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HC8aFj5npYpXVoCogsYU4E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 70999,
      "output_tokens": 7184,
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
          "output_tokens": 7184,
          "cache_read_input_tokens": 70999,
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

### Runtime record

_source line 136_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9b744b82-60d8-4742-bda3-e4ebc93dd839",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 137_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 138_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9b744b82-60d8-4742-bda3-e4ebc93dd839",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---

### Runtime record

_source line 139_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CaTS v2 for VLA token selection robustness",
  "sessionId": "935e2014-ee5c-4147-85a1-8ed314c9698e"
}
```

---
