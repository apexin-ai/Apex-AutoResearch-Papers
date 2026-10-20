# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/0f167b53-e63f-46d4-ab31-789b251a64fd.jsonl`
- **Structured JSON:** [`312ccb54bd3b6925b99f.json`](../../sessions/31/312ccb54bd3b6925b99f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T19:45:45.053Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T19:45:45.053Z",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World Action Models (WAMs) — joint world modeling and action prediction in a unified architecture, often built on video diffusion priors. In-scope: unified video+action prediction, MoT (Mixture-of-Transformers) architectures with text/video/action streams, WMs that double as policies via inverse dynamics on imagined futures, action-conditioned video diffusion as policy.\n\nRecent landscape (do not duplicate): UniVLA, DreamVLA, GigaBrain-0.5M, DiT4DiT, MotuBrain, video-diffusion-as-policy lines. WAMs are the hottest CoRL 2026 area — high competition but high reward.\n\nContribution type: METHOD ONLY. New unified architecture, new training scheme that fuses world prediction and action prediction, new inference algorithm extracting actions from imagined futures.\n\nSIM-ONLY MITIGATION: WAM papers at CoRL routinely use sim envs since the method depends on data scale, not real-robot deployment. Use LIBERO/ManiSkill as primary and frame contribution as architectural.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Most challenging budget — video models are heavy. Strategies: (a) fine-tune an open video WM (Cosmos releases, OpenSora, CogVideoX) with action conditioning, (b) distill a large WAM into a smaller one, (c) propose a method that requires only small additional training on top of an existing WAM, (d) propose an inference-time method that needs no training.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos.\n3. Eval: LIBERO, ManiSkill 2/3, RoboCasa for closed-loop control + video prediction quality (PSNR/SSIM/FVD on action-conditioned futures). Compare against UniVLA / DreamVLA / DiT4DiT lineage if open releases exist.\n\nLook for: efficient action-conditioning of video diffusion, latent WAMs that bypass pixel decoding, methods that share representations across world and action streams. Avoid: trivial action-token prepending without architectural insight.\n\nTag: direction=world_action_model, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification of World Knowledge for Robust Action Generation\",\n  \"core_problem\": \"World-Action Models (WAMs) achieve near-saturated performance on standard manipulation benchmarks (Being-H0.7: 99.2%, Fast-WAM: 97.6% on LIBERO) but remain brittle under geometric perturbations — camera viewpoint and robot initial state changes cause drops to 60–90% on LIBERO-Plus. Concurrently, Fast-WAM, GigaWorld-Policy, and MotuBrain demonstrate that video features are dispensable at inference under standard conditions. These facts appear contradictory: if video-encoded spatial knowledge is dispensable, why do WAMs fail precisely under geometric perturbations where spatial reasoning should matter most? We hypothesize the resolution lies in HOW video information is used, not WHETHER it is used. Under standard conditions, the action branch encodes sufficient visual-motor mappings from the training distribution, making video features redundant. Under geometric perturbation, these mappings break — and the video branch's spatial reasoning could compensate, but only if the video→action guidance signal is properly amplified and filtered. Standard classifier-free guidance (CFG) in diffusion models amplifies all conditional contributions equally, mixing action-relevant spatial information with irrelevant appearance features. CPC theory (NeurIPS 2025) proves CFG implicitly performs selective amplification via contrastive principal components, but only in class-conditional settings with well-separated covariance structures — not in heterogeneous cross-modal settings like video→action guidance. The core question: can explicit spectral filtering of the cross-modal guidance signal selectively amplify geometric/spatial components that improve robustness while suppressing components that add noise? Before answering this, a prior diagnostic question must be settled: does cross-modal guidance in WAMs carry any action-relevant signal at all under geometric perturbation? No existing work has tested this.\",\n  \"opportunity\": \"Three converging developments create a precise research opportunity, and a critical correction from the prior proposal version enables a more principled approach: (1) UWM (RSS 2025) uses UniDiffuser-style independent diffusion timesteps for video and action modalities — setting the video timestep t_o'=T marginalizes video information, yielding the unconditional action score, while t_o'&lt;T yields the video-conditioned action score. This natively enables cross-modal CFG through two forward passes without any dropout training, architectural modification, or fine-tuning. UWM releases a pretrained LIBERO-90 checkpoint. (2) LIBERO-Plus and the WAM robustness study (March 2026) reveal that geometric perturbations remain the dominant failure mode: OA-WAM Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%), CKT-WAM (Camera 77.4%, Robot 71.4%), with the overall LIBERO-Plus SOTA at 86.1% (CKT-WAM). Crucially, all geometric robustness improvements to date (OA-WAM, CKT-WAM) require architectural modification or additional training — no training-free inference-time method has been attempted. (3) Independent Condition Guidance (ICG, ICLR 2025) demonstrates that CFG-quality guidance can be obtained from any pretrained conditional model without dropout training, by substituting the unconditional score with a prediction conditioned on a random/independent input. This enables cross-modal guidance on WAMs like Fast-WAM that were not trained with video dropout. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection for filtering diffusion guidance signals, but only in single-modal image restoration. CRITICAL CORRECTION: The prior version incorrectly claimed Fast-WAM was trained with unconditional video feature dropout enabling native CFG. After verification — reading the full paper, project page, and GitHub — this claim is unsupported. Fast-WAM uses CFG scale 1.0 (no guidance amplification), and 'uncond' in checkpoint names refers to its unconditional inference mode (no future video denoising), not CFG-enabling dropout training. UWM's independent timestep mechanism provides the principled alternative, with ICG as a backbone-agnostic complement.\",\n  \"landscape\": \"**Video-at-inference in WAMs:** Fast-WAM (March 2026) removes video denoising at inference, retaining only backbone features. GigaWorld-Policy (March 2026) uses causal masking to block video→action flow. MotuBrain (April 2026) freezes video branch and caches KV pairs. All use binary approaches (all or no video features) and evaluate only on standard benchmarks — none test under geometric perturbation. **Cross-modal CFG support in WAMs:** UWM (RSS 2025) uses independent diffusion timesteps for video and action, enabling native cross-modal conditioning control by setting t_o'=T to marginalize video. Motus (Dec 2025) uses a similar UniDiffuser-style architecture. X-WAM (April 2026) uses asynchronous noise sampling across modalities. Vid2World (ICLR 2026) applies CFG in the action→video direction for video quality. DreamZero (Feb 2026) uses parallelized CFG for real-time inference. No work systematically applies or evaluates cross-modal CFG in the video→action direction for action quality or robustness improvement under perturbation. **Training-free guidance methods:** ICG (ICLR 2025) provides CFG-quality guidance on any pretrained conditional model using independent/random conditions, without dropout training — validated on image generation but not cross-modal robot control. **CFG Theory:** CPC decomposition (NeurIPS 2025) proves CFG implicitly decomposes into mean-shift + positive CPC + negative CPC; explicitly notes limitations when conditional covariances lack discriminative structure — the expected case for heterogeneous video→action conditioning. **SVD-based guidance filtering:** DiffStateGrad (ICLR 2025) projects measurement gradients onto SVD subspaces for image restoration. Related SVD approaches exist for controllable editing (Feb 2025) and concept removal (March 2025). All operate in single-modal image settings; none address cross-modal guidance for robot control. **Geometric robustness methods (competitors):** OA-WAM (May 2026): object-addressable architecture, Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%) — requires architectural modification. CKT-WAM (May 2026): parameter-efficient context transfer, total 86.1% (Camera 77.4%, Robot 71.4%) — requires additional training. Being-H0.7 (May 2026): latent world-action queries with posterior alignment, 82.1% zero-shot / 84.8% fine-tuned — uses implicit world modeling without explicit video branch. π0.5: 85.7% total. AnyCamVLA (March 2026): zero-shot camera adaptation via feed-forward novel view synthesis, training-free but VLA-specific and camera-only. ADPro (2025): test-time adaptive diffusion policy via manifold-constrained denoising, evaluated on RLBench/CALVIN but not LIBERO-Plus. GPC (Feb 2025): inference-time enhancement via predictive world model look-ahead, requires a separately trained world model. **Selective world-model usage:** WoG (Feb 2026) compresses world predictions via learned Q-Former — requires retraining. FFDC (May 2026) decides WHEN to replan, not HOW MUCH or WHICH influence to apply within denoising. **Gap:** No existing work (1) applies cross-modal CFG in the video→action direction of WAMs with systematic evaluation under geometric perturbation, (2) uses spectral filtering to selectively amplify action-relevant components of the cross-modal guidance signal, or (3) provides a training-free, architecture-agnostic method targeting WAM geometric robustness specifically.\",\n  \"approach\": \"We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method for selectively amplifying action-relevant world knowledge in WAMs, targeting geometric robustness. The approach is structured in two phases: a diagnostic phase establishing whether cross-modal guidance carries useful signal under perturbation, and a method phase applying spectral filtering if signal exists.\\n\\n**Phase 1 — Cross-Modal Guidance Diagnostics (primary empirical contribution).** Before spectral filtering, we answer the foundational question: does amplifying video→action guidance improve WAM robustness under geometric perturbation? Using UWM's independent timestep mechanism, we compute the guidance vector g_t = ε(a; t_a, t_o'=t_a) − ε(a; t_a, t_o'=T) at each action denoising step t. The first term uses joint denoising (video and action at matched noise levels, exchanging information through shared attention); the second marginalizes video by setting t_o'=T (pure noise). The guided prediction: ε_guided = ε_marginal + w·g_t. We sweep w ∈ {1.0, 1.5, 2.0, 3.0, 5.0} on both standard LIBERO (sanity check — expect no benefit, confirming video dispensability under standard conditions) and LIBERO-Plus geometric perturbations (camera, robot-init at L1/L3 difficulty). This takes ~25-30h H100 and definitively answers whether guidance carries signal. If uniform CFG shows zero improvement under geometric perturbation at all scales, the paper pivots to a diagnostic/negative-result contribution analyzing what video branches encode vs. what geometric robustness requires.\\n\\n**Phase 2 — Spectral Filtering with Action Quality Correlation (method contribution, contingent on Phase 1).** If Phase 1 reveals that uniform CFG helps (or helps inconsistently — improving some perturbation types but hurting others), we apply spectral filtering to selectively amplify beneficial components. Collect guidance vectors {g_t} across a calibration set (~100 trajectories from LIBERO training data) at each of K=10 denoising steps. For each step t, compute the SVD of the guidance covariance C_t = (1/N)Σ g_t g_t^T = U_t Λ_t U_t^T. For automatic component selection, compute Action Quality Correlation (AQC) for each principal direction u_i: the Spearman rank correlation between |u_i^T g_t| and action quality improvement (loss reduction) when the component is included. Retain components with AQC exceeding a permutation-null threshold (p<0.05), yielding projection Π_t. Filtered guidance: ε_guided = ε_marginal + w(t)·Π_t(g_t), where w(t) follows β-CFG timestep-adaptive scheduling. This extends DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control, with the key difference being AQC-calibrated selection rather than state-defined projection.\\n\\n**Backbone Strategy.** Primary: UWM with released LIBERO-90 checkpoint, fine-tuned on LIBERO tasks. UWM's independent timesteps provide mathematically clean cross-modal CFG: t_o'=T gives the unconditional (video-marginalized) action score natively, with no dropout training or architectural modification needed. Secondary (extension for backbone-agnosticism): ICG applied to Fast-WAM. ICG approximates the unconditional score by conditioning on a random/independent input — for video features, this means substituting real video tokens with random embeddings sampled from a matched distribution. ICG has been validated on image diffusion models (ICLR 2025) but not cross-modal robot control; testing it here is itself a novel contribution. If ICG on Fast-WAM produces consistent results with UWM's native CFG, this demonstrates SCG's architecture-agnosticism.\\n\\n**Evaluation strategy.** Primary benchmark: LIBERO-Plus with 3 perturbation types — camera and robot-init (geometric, where video knowledge should help most), plus light as control (where WAMs already excel, expect no benefit from guidance). 2 difficulty levels (L1, L3), 2 seeds. Standard LIBERO as sanity check. Baselines: (i) UWM standard policy (t_o'=T, no guidance), (ii) UWM joint denoising (t_o'=t_a, no guidance amplification — equivalent to CFG w=1.0), (iii) Uniform cross-modal CFG (w>1), (iv) SCG with AQC spectral filtering (ours). Ablations: (a) AQC threshold sensitivity, (b) per-step vs. global SVD, (c) cross-task transfer of calibrated subspace (calibrate on LIBERO tasks A, evaluate on tasks B), (d) AQC-selected directions vs. top-variance directions (testing whether action-relevant ≠ high-variance), (e) ICG on Fast-WAM vs. UWM native CFG (backbone comparison). Framing vs. OA-WAM: SCG is training-free and architecture-agnostic, complementary to OA-WAM's architectural approach. We explicitly frame SCG as applicable to any WAM with video/action branches, including potentially OA-WAM itself if its checkpoint becomes available.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100-140h H100\",\n      \"gpu_utilization\": \"Low-moderate (25-35%). Human sets up UWM + LIBERO-Plus integration, fine-tunes UWM, implements cross-modal CFG and SVD pipeline, runs evaluation sweeps.\",\n      \"timeline\": \"2.5-3 weeks (feasible for CoRL abstract May 26, paper May 29)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$250-420 (at ~$2.50-3.00/H100-hr spot pricing, May 2026)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~110-160h H100\",\n      \"gpu_utilization\": \"Moderate-high (55-70%). Agent implements cross-modal CFG on UWM, integrates LIBERO-Plus, queues Phase 1 diagnostic sweeps. Human reviews Phase 1 results to decide Phase 2 (~1hr at decision point, then ~30min/day).\",\n      \"timeline\": \"14-18 days (targets CoRL 2026 abstract May 26, paper May 29)\",\n      \"team\": \"1 researcher, ~30-45min/day\",\n      \"claude_api_cost\": \"$100-250 (estimated ~1000-2500 Opus turns)\",\n      \"estimated_gpu_cost\": \"$275-480\",\n      \"risk_note\": \"Primary risk is UWM fine-tuning achieving competitive LIBERO performance. UWM's released LIBERO-90 checkpoint and fine-tuning code reduce this risk. Phase 1 diagnostic is quick (~25-30h) and provides go/no-go signal for Phase 2.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~130-200h H100\",\n      \"gpu_utilization\": \"High (>85%). Agent runs continuous Phase 1 diagnostic → Phase 2 calibration → evaluation loop.\",\n      \"timeline\": \"10-14 days with 2-4 GPUs concurrently\",\n      \"team\": \"0 (initial setup only, ~2 hours)\",\n      \"claude_api_cost\": \"$180-400 (estimated ~1800-4000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$325-600\",\n      \"speed_bottleneck\": \"Phase 1 must complete before Phase 2 begins. Phase 1: ~25-30h across 3 perturbation types × 5 CFG scales × 2 difficulties × 2 seeds = 60 configs. Phase 2: ~40-60h for SVD calibration + SCG evaluation.\",\n      \"risk_note\": \"Agent must correctly interpret Phase 1 results (is there signal?) before proceeding. Human review of Phase 1 results recommended even in auto mode. UWM fine-tuning failure would require fallback to ICG-on-Fast-WAM.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16-19 days; Phase 1 diagnostic is achievable within first week, Phase 2 within second; tight but feasible with UWM checkpoint and focused scope)\",\n    \"AAAI 2027 (deadline Aug 2, 2026 — secondary target if CoRL revision needed; allows ICG-on-Fast-WAM extension, additional WAM backbones, full LIBERO-Plus sweep across all 7 perturbation types)\",\n    \"ICLR 2027 (deadline Sep 24, 2026 — fallback; allows comprehensive multi-backbone study, deeper mechanistic analysis, and potential integration with OA-WAM)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [UWM] (RSS 2025) — PRIMARY BACKBONE; independent diffusion timesteps for video/action natively enable cross-modal CFG by setting t_o'=T to marginalize video; released LIBERO-90 checkpoint with fine-tuning code\",\n    \"No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models [ICG] (ICLR 2025) — Independent Condition Guidance enables CFG on any pretrained conditional model without dropout training; backbone-agnostic complement to UWM; uses random/independent conditions to approximate unconditional score\",\n    \"Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — proves CFG implicitly decomposes into selective amplification (positive CPC) and suppression (negative CPC); limited to class-conditional settings with well-separated covariance structures\",\n    \"Diffusion State-Guided Projected Gradient for Inverse Problems [DiffStateGrad] (ICLR 2025) — SVD-based subspace projection in diffusion models for image inverse problems; key methodological predecessor; single-modal, external gradient projection\",\n    \"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — demonstrates video dispensable at inference under STANDARD conditions; secondary backbone candidate via ICG; NOTE: does NOT support native CFG via dropout training (corrected from prior version)\",\n    \"Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv March 2026) — WAMs weak on geometric perturbations; camera 60-80%, robot-init 63-90%; motivates the robustness focus\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark with L1-L5 difficulty levels\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv May 2026) — LIBERO-Plus Geo-Avg SOTA at 84.3% (Camera 80.5%, Robot 89.6%); requires architectural modification; SCG is complementary (training-free, architecture-agnostic)\",\n    \"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv May 2026) — LIBERO-Plus total SOTA at 86.1% (Camera 77.4%, Robot 71.4%); requires additional training\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv May 2026) — LIBERO standard SOTA at 99.2%; LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned; uses latent world-action queries without explicit video branch\",\n    \"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models (arXiv March 2026) — training-free camera adaptation via novel view synthesis; VLA-specific, camera-perturbation-only; complementary approach\",\n    \"ADPro: Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising (2025) — test-time adaptation via geometric manifold constraints; evaluated on RLBench/CALVIN, not LIBERO-Plus; related inference-time approach\",\n    \"Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling [GPC] (RA-L 2025) — augments frozen diffusion policy with separately trained world model for inference-time look-ahead; requires additional world model training; SCG uses built-in video branch instead\",\n    \"Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational CFG technique\",\n    \"Classifier-free Guidance with Adaptive Scaling [β-CFG] (arXiv Feb 2025) — timestep-adaptive guidance scheduling\",\n    \"Vid2World: Crafting Video Diffusion Models to Interactive World Models (ICLR 2026) — CFG in action→video direction\",\n    \"GigaWorld-Policy: An Efficient Action-Centered World-Action Model (arXiv March 2026) — causal masking prevents video→action flow\",\n    \"MotuBrain: An Advanced World Action Model for Robot Control (arXiv April 2026) — KV cache for video features\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models [FFDC] (arXiv May 2026) — confidence-based replanning at execution level; orthogonal\",\n    \"World Guidance: World Modeling in Condition Space for Action Generation [WoG] (arXiv Feb 2026) — learned world-model compression; requires retraining\",\n    \"X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv April 2026) — asynchronous noise sampling across modalities; depth prediction for 3D awareness; potential alternative backbone with independent timestep control\",\n    \"DreamZero: World Action Models are Zero-shot Policies (arXiv Feb 2026) — parallelized CFG in WAM inference\",\n    \"Motus: A Unified Latent Action World Model (arXiv Dec 2025) — UniDiffuser-style WAM; potential alternative backbone\",\n    \"One Transformer Fits All Distributions in Multi-Modal Diffusion [UniDiffuser] (ICML 2023) — foundational independent timestep mechanism\",\n    \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control (arXiv Jan 2026) — LIBERO-Plus 82.2%\",\n    \"Mechanistic Dissection of Cross-Attention Subspaces in Text-to-Image Diffusion Models (AAAI 2025) — SVD-based spectral analysis of concept-encoding subspaces\",\n    \"Test-Time Perturbation Learning with Delayed Feedback for VLA Models [TTPL] (arXiv April 2026) — verifier-free test-time adaptation; complementary approach\"\n  ],\n  \"description\": \"We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method that selectively amplifies action-relevant world knowledge from the video branch of World-Action Models (WAMs), targeting robustness under geometric perturbations (camera viewpoint, robot initial state). The work is structured as a two-phase investigation. Phase 1 (diagnostic): WAMs achieve near-perfect standard benchmark performance (Fast-WAM 97.6%, Being-H0.7 99.2%) but remain brittle under geometric perturbation (OA-WAM Camera 80.5%, CKT-WAM Camera 77.4%). Multiple works show video features are dispensable at inference under standard conditions — but none test whether amplifying video→action guidance helps under geometric perturbation, where the action branch's learned visual-motor mappings break and the video branch's spatial reasoning could compensate. We use UWM's (RSS 2025) independent timestep mechanism — setting video timestep t_o'=T marginalizes video, giving the unconditional action score; t_o'&lt;T gives the video-conditioned score — to natively enable cross-modal CFG without dropout training or architectural modification. A systematic CFG scale sweep across LIBERO-Plus geometric perturbations answers whether guidance carries action-relevant signal. CRITICAL CORRECTION from prior version: Fast-WAM was previously claimed to support native CFG via video feature dropout, but this is unverified — the paper never mentions dropout training, uses CFG scale 1.0 (no amplification), and 'uncond' in checkpoint names refers to unconditional inference mode. UWM's independent timesteps provide the principled alternative. Phase 2 (method): If Phase 1 reveals signal, SCG applies SVD-based spectral filtering to the guidance vector g_t = ε_cond − ε_uncond, retaining only directions whose Action Quality Correlation (AQC) — Spearman correlation between projection magnitude and action quality improvement — exceeds a permutation-null threshold. This makes component selection automatic and parameter-free, extending DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control with action-quality calibration. For backbone-agnosticism, we additionally test Independent Condition Guidance (ICG, ICLR 2025), which approximates unconditional scores via random conditions on any pretrained model, applied to Fast-WAM. SCG is complementary to OA-WAM (requires architectural modification) and CKT-WAM (requires additional training) — it is training-free, architecture-agnostic, and could be applied on top of these methods. Both phases contribute: Phase 1 provides the first empirical evidence on whether/when world knowledge helps under geometric perturbation (resolving the video-dispensability paradox); Phase 2 provides a practical method for selective guidance when signal exists. If Phase 1 shows no signal, the diagnostic finding itself — that video branches encode information irrelevant to geometric robustness despite encoding spatial features — is a significant negative result that redirects the field away from guidance-based approaches.\",\n  \"project_name\": \"spectral_cross_modal_guidance_wam\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"UniDiffuser (ICML 2023), the foundation of Motus, already supports cross-modal CFG by design — setting video timestep to T while denoising actions gives the 'unconditional' score. This means VB-CFG can be applied to pre-trained Motus/UWM with ZERO training, making the proposed 'dropout fine-tuning' unnecessary rather than a contribution.\", \"Fast-WAM (March 2026) demonstrated that video prediction's value lies in training-time representation learning, not test-time features. This directly challenges VB-CFG's core hypothesis that amplifying video features at inference improves actions — if the learned representations already encode world knowledge, amplifying video tokens may amplify noise rather than signal.\", \"'No Training, No Problem: Rethinking Classifier-Free Guidance' (ICLR 2025) shows CFG works on any pre-trained conditional model without dropout training, further reducing the proposed dropout fine-tuning from 'lightweight contribution' to 'unnecessary overhead.'\", \"LIBERO benchmark is already saturated (>90% success rate for SOTA methods like MotuBrain). Marginal improvements will not be compelling for CoRL reviewers. RoboTwin 2.0 scores also show MotuBrain at 95-96 in both clean and randomized settings.\", \"The contribution as described is an empirical study ('does CFG in video→action direction help?'), not a method paper. The user's requirement explicitly asks for 'METHOD ONLY: new unified architecture, new training scheme, new inference algorithm.' Trying an existing technique in a new direction doesn't qualify as a new inference algorithm.\", \"Vid2World (ICLR 2026) already establishes CFG within WAMs. Applying it in the reverse direction is the obvious next experiment — exactly the kind of 'trivial action-token prepending without architectural insight' the user asked to avoid.\"]\nFeedback: The core observation (video features could be selectively amplified during action denoising) is valid but insufficiently novel for CoRL as a standalone method. To save this direction, consider: (1) **Add genuine technical depth** — propose adaptive per-timestep guidance (guidance scale that changes during the action denoising trajectory), per-token guidance (different video tokens contribute differently), or latent-subspace guidance that operates on identified action-relevant video feature dimensions rather than the full video branch. (2) **Confront the Fast-WAM tension directly** — frame the contribution as 'understanding when and how video features help action prediction' with a mechanistic analysis (which video dimensions encode safety-relevant vs. efficiency-relevant information), going beyond simple guidance scale sweeps. (3) **Target harder benchmarks** — LIBERO is too saturated; use LIBERO-Plus with perturbations, or focus on out-of-distribution generalization where world-model amplification could plausibly help. (4) **Acknowledge UniDiffuser's inherent CFG support** — include zero-shot CFG (no fine-tuning) as a baseline and position dropout training as providing sharper conditional/unconditional separation. (5) **Consider combining with adaptive execution** — merge with the 'When to Trust Imagination' insight to propose adaptive guidance scales based on task difficulty or prediction confidence. This would be a genuine novel inference algorithm rather than a parameter sweep.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"VENUE MISMATCH (CRITICAL): The idea explicitly states CoRL 2026 is 'too tight' and targets ICLR 2027 as primary. The user's hard requirement is CoRL 2026 (deadline May 29, 2026 — 19 days). This is a direct constraint violation.\", \"CPC THEORY UNDERMINES CORE PREMISE: 'Towards Understanding the Mechanisms of Classifier-Free Guidance' (NeurIPS 2025) proves CFG already inherently decomposes into selective amplification of class-specific features (positive CPC) and suppression of generic features (negative CPC). SCG's explicit SVD-based filtering may be adding complexity to achieve what CFG already does implicitly — the burden of proof is on showing the explicit approach significantly outperforms the implicit one.\", \"MISSING COMPETITOR — World Guidance (WoG, arxiv 2602.22010, Feb 2026): This paper maps world-model predictions into compact conditions for action inference, directly addressing the same problem (selective use of world knowledge for actions) via a different mechanism (learned compression vs post-hoc spectral decomposition). Must be cited and differentiated against.\", \"FAST-WAM TENSION UNRESOLVED: Fast-WAM shows video features' primary value is in training-time representation learning. If video→action guidance at inference carries limited useful signal, then even selective amplification of the 'best' spectral components yields negligible improvement. The calibration step might simply discover that no components reliably help.\", \"TIMESTEP-ADAPTIVE COMPONENT IS NOT NOVEL: β-CFG (Feb 2025), Dynamic CFG via Online Feedback (Sep 2025), and 'Applying Guidance in a Limited Interval' (NeurIPS 2024) all propose timestep-adaptive guidance scheduling. This component cannot be claimed as part of the contribution.\", \"COMPUTE BUDGET VIOLATION: Auto research mode estimates 400-700h H100, exceeding the user's 200h hard constraint. Even the human-in-loop mode (180-280h) may exceed budget. Only the manual mode (100-180h) fits within 200h, but manual mode requires 2-3 months — incompatible with 20-day deadline.\", \"CALIBRATION MAKES 'TRAINING-FREE' MISLEADING: The method requires task-specific calibration on ~100 trajectories to identify the action-relevant subspace. This calibration is data-dependent and may not transfer across tasks/environments, limiting the claimed 'architecture-agnostic' generality.\"]\nFeedback: The revision substantially improved technical depth from Round 1, but faces fundamental challenges:\n\n**To save this direction for CoRL 2026:**\n\n1. **MUST target CoRL 2026 explicitly** — reframe the scope to be achievable in 19 days. Suggestion: narrow to a single backbone (Motus), single benchmark (LIBERO-Plus camera/robot-init perturbations only), and position as a focused empirical+mechanistic study.\n\n2. **Address the CPC challenge head-on**: The NeurIPS 2025 paper shows CFG already selectively amplifies discriminative directions. Your contribution must show WHY explicit SVD-based filtering outperforms this implicit mechanism. Hypothesis: in the cross-modal WAM setting (unlike text→image), the guidance vector mixes heterogeneous information (spatial, dynamics, appearance) that don't align with the top principal components of the data distribution — requiring explicit calibration-based selection. Frame this as the core research question, not an assumed benefit.\n\n3. **Cite and differentiate from World Guidance (WoG, arxiv 2602.22010)**: WoG solves the same problem via learned compression. SCG's advantage: training-free, post-hoc, applicable to any pre-trained WAM. WoG's advantage: end-to-end optimized. Position SCG as complementary/alternative for settings where retraining is infeasible.\n\n4. **Resolve Fast-WAM tension with a testable hypothesis**: Argue that Fast-WAM's finding (video features dispensable at inference) applies to STANDARD settings where training representations suffice, but under PERTURBATION (LIBERO-Plus camera shifts, robot-init changes), the world model's geometric reasoning becomes newly relevant at inference — this is testable and would be a strong contribution if confirmed.\n\n5. **Drop the timestep-adaptive component as a claimed contribution** — acknowledge it as existing technique (cite β-CFG, Dynamic CFG) and include only as an engineering choice. Focus novelty entirely on the spectral subspace decomposition of cross-modal guidance.\n\n6. **Ensure compute stays within 200h**: Narrow evaluation to 3-4 perturbation types × 3 difficulty levels × 2 seeds on LIBERO-Plus, plus standard LIBERO as sanity check. This reduces evaluation to ~50-80h H100 + ~20h calibration = within budget.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"COMPUTE BUDGET VIOLATION (CRITICAL): Motus has NO publicly released LIBERO checkpoint — only Motus_robotwin2 is available on HuggingFace. The Motus paper's Stage 3 fine-tuning consumed ~400 GPU-hours. Fine-tuning Motus on LIBERO would cost 100-400h H100 BEFORE any SCG calibration or LIBERO-Plus evaluation. The proposal's 90-130h estimate completely omits this cost, making total compute 300-500h+ H100, far exceeding the 200h hard constraint.\", \"CONTRIBUTION TYPE MISMATCH: The user explicitly requires 'METHOD ONLY — new inference algorithm.' SCG is technically an inference modification, but the proposal hedges: 'Even if SCG shows marginal improvement over uniform CFG... the spectral analysis reveals the structure of cross-modal information flow — a contribution independent of method performance.' This self-hedging reveals it is primarily an analysis/diagnostic paper, not a method paper. A CoRL reviewer will score method novelty lower when the authors themselves frame the analysis as the robust contribution.\", \"NULL RESULT RISK IS HIGH AND INADEQUATELY MITIGATED: Fast-WAM, GigaWorld-Policy, and MotuBrain all find video features dispensable at inference. The perturbation hypothesis (H2: video guidance helps under geometric perturbation) is testable but risky — no prior evidence supports it. If both H1 and H2 yield null results (SCG ≈ CFG ≈ no-video under all conditions), the paper reduces to 'we decomposed a signal that doesn't matter.' The claim that spectral analysis is valuable regardless is weak for a method-focused venue.\", \"MOTUS-LIBERO INTEGRATION RISK: Motus was developed on RoboTwin with its own data pipeline, observation format, and sim environment (ManiSkill-based). Adapting Motus to LIBERO (MuJoCo-based) requires non-trivial engineering for observation preprocessing, action space mapping, and data format conversion. This integration work could consume 5-7 days of the 19-day timeline, leaving insufficient time for the actual research contribution.\", \"LIBERO-PLUS EVALUATION INCOMPLETE: The proposal claims CKT-WAM (86.1%), OA-WAM (Geo-Avg 76.0%), and Cosmos-Policy (82.2%) as LIBERO-Plus baselines. However, none of these use Motus as backbone, making direct comparison confounded by architecture differences. The proposal needs to compare SCG-Motus vs. standard-Motus vs. Fast-WAM-Motus to isolate the effect of spectral guidance, but Motus has no LIBERO-Plus results in the literature to serve as baseline.\", \"CALIBRATION SET DEPENDENCY WEAKENS GENERALITY: SCG requires collecting ~100 trajectory guidance vectors for SVD calibration, making it task-specific. The proposal doesn't discuss whether the calibrated subspace transfers across LIBERO tasks, perturbation types, or environments. If per-task recalibration is needed, the practical advantage over WoG's end-to-end retraining diminishes.\"]\nFeedback: The framing around CPC theory is a genuine improvement from Round 2 — the research question is well-posed and timely. However, three structural problems must be resolved:\n\n**1. Fix the compute/backbone crisis (MOST URGENT):** Switch from Motus to UWM as the primary backbone. UWM has a publicly released LIBERO-90 pretrained checkpoint (Google Drive, WEIRDLabUW/unified-world-model), uses the same UniDiffuser-style independent timesteps as Motus, and has established LIBERO evaluation infrastructure. Fine-tuning UWM on LIBERO-specific tasks should be far cheaper than Motus Stage 3 (~400h). Alternatively, check if Fast-WAM (github.com/yuantianyuan01/FastWAM) releases LIBERO checkpoints for a WAM backbone that already addresses the video-at-inference question — this would give you a natural baseline.\n\n**2. Strengthen the method contribution to match user requirements:** The user needs a 'new inference algorithm,' not an analysis paper. To make SCG a genuine method contribution: (a) Add adaptive component selection — instead of fixed top-k, propose an automatic criterion for selecting k based on the eigenvalue gap or action-quality correlation threshold, making SCG parameter-free. (b) Propose per-perturbation-type component routing — if different spectral components activate for camera vs. robot-init perturbations (as hypothesized), design a lightweight detector that identifies the perturbation type and selects the appropriate spectral subspace automatically. This makes SCG an adaptive inference algorithm, not just SVD + projection.\n\n**3. Derisk null results with a concrete fallback:** If video→action CFG provides no benefit even under geometric perturbation, the pure analysis paper is too thin for CoRL. Consider a concrete fallback: show that the spectral decomposition can be used to EFFICIENTLY COMPRESS the video branch (retain only k components instead of full video denoising), achieving Fast-WAM-like speedup while preserving the specific spectral components that help under perturbation. This gives a practical contribution (efficient selective video usage) even if the guidance scale sweep shows marginal gains.\n\n**4. Timeline and scope:** 19 days is barely feasible even with the right backbone. Drop all secondary benchmarks (ManiSkill, RoboCasa) and focus exclusively on LIBERO-Plus with 2 geometric perturbation types (camera, robot-init) + 1 control (light) at 2 difficulty levels and 2 seeds. This reduces evaluation from 48 configs to ~18, saving significant GPU time.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL — UNVERIFIED CORE ASSUMPTION: Fast-WAM's 'unconditional dropout on video features enabling native CFG' is fabricated or at minimum unverified. After reading the full paper (arxiv 2603.16666), project page, GitHub README, and HuggingFace model card: (a) the paper NEVER mentions unconditional dropout on video features, (b) NEVER discusses video→action CFG, (c) uses CFG scale 1.0 which means zero guidance amplification, (d) contains no mentions of 'p_uncond', 'null condition', 'empty token', or 'mask probability'. The 'uncond' in checkpoint names (libero_uncond_2cam224.pt) almost certainly refers to the unconditional inference mode (no future video denoising) — Fast-WAM's core contribution — NOT to CFG-enabling dropout training. Without verified video feature dropout training, computing ε_uncond by zeroing video features produces out-of-distribution predictions, and the entire SCG pipeline produces unreliable guidance vectors.\", \"CFG SCALE 1.0 CONTRADICTS CFG READINESS: Fast-WAM's paper explicitly states 'During inference, we use 10 denoising steps with classifier-free guidance (CFG) scale set to 1.0.' Scale 1.0 means ε_guided = ε_uncond + 1.0·(ε_cond - ε_uncond) = ε_cond, i.e., NO guidance amplification at all. This strongly suggests the model was not designed for or evaluated with CFG guidance amplification in any modality direction. If the model doesn't benefit from CFG at scale > 1.0, spectral filtering of the guidance signal is filtering noise.\", \"NULL RESULT RISK REMAINS STRUCTURALLY HIGH: The proposal acknowledges Fast-WAM's finding that video features are dispensable at inference but hypothesizes they become relevant under geometric perturbation. However, no prior work supports this hypothesis — it is purely speculative. If the guidance vector g_t = ε_cond - ε_uncond carries negligible action-relevant signal (as suggested by video dispensability), then SVD decomposition of near-zero vectors produces noise, not actionable spectral components.\", \"COMPETITION FROM BEING-H0.7 (May 2026): Being-H0.7 achieves 99.2% on standard LIBERO and strong LIBERO-Plus results using latent world-action queries with posterior alignment — no video generation or video features at inference. This latent approach renders the entire 'video features at inference' question increasingly irrelevant, as the field moves toward implicit world modeling that doesn't require explicit video branches to filter or amplify.\", \"OA-WAM (May 2026) ALREADY ACHIEVES GEOMETRIC ROBUSTNESS SOTA: OA-WAM reaches Geo-Avg 84.3% on LIBERO-Plus (Camera 80.5%, Robot 89.6%) through object-addressable architectural modification. SCG needs to exceed this without any training — an extremely high bar for an inference-time-only method operating on potentially noisy guidance vectors.\", \"CALIBRATION TRANSFERABILITY UNTESTED: AQC requires per-task calibration on ~100 trajectories. The proposal hypothesizes cross-task transfer but doesn't address whether the action-relevant subspace is stable across LIBERO's 90 tasks, across perturbation types, or across difficulty levels. If recalibration is needed per task × perturbation type, the practical overhead approaches WoG's end-to-end retraining cost.\"]\nFeedback: The framing and research question are strong — resolving the apparent contradiction between video dispensability and geometric vulnerability is genuinely interesting. However, the proposal has a fatal dependency on an unverified claim about Fast-WAM's training procedure. To save this direction:\n\n**1. VERIFY THE UNCONDITIONAL DROPOUT CLAIM (BLOCKER):** Before any other work, you MUST verify whether Fast-WAM was trained with video feature dropout. Options: (a) Read the actual Fast-WAM training code on GitHub (check train.py or model configs for p_uncond on video features), (b) Contact the Fast-WAM authors directly, (c) Check if Wan2.2's base model has text dropout (likely yes, but this is TEXT not VIDEO features). If Fast-WAM was NOT trained with video dropout, you have three recovery paths: (i) Fine-tune with video dropout (~50-100h H100, tight but potentially feasible within budget), (ii) Use the 'No Training, No Problem' (ICLR 2025) independent condition guidance approach that doesn't require dropout training, (iii) Switch to UWM which uses UniDiffuser-style independent timesteps and may natively support cross-modal CFG by setting video timestep to T.\n\n**2. IF DROPOUT EXISTS — VALIDATE CFG FIRST:** Before building SCG, run a simple experiment: sweep CFG scale w ∈ {1.0, 1.5, 2.0, 3.0, 5.0} on standard LIBERO and LIBERO-Plus camera perturbation. If uniform CFG shows NO improvement at any scale (likely given CFG=1.0 was chosen by the authors), then spectral filtering of a zero-signal is pointless. This takes ~20h H100 and answers the fundamental question in 2-3 days.\n\n**3. CONSIDER UWM AS PRIMARY BACKBONE:** UWM (RSS 2025) uses UniDiffuser-style independent timesteps — setting video timestep to T gives the unconditional score for free, enabling native cross-modal CFG without dropout training. UWM has a released LIBERO-90 checkpoint. This avoids the entire Fast-WAM dropout verification problem.\n\n**4. STRENGTHEN AGAINST OA-WAM COMPARISON:** OA-WAM's Geo-Avg 84.3% is the target to beat. Frame SCG as complementary (training-free, applicable to any WAM including OA-WAM) rather than competitive. Test SCG on top of OA-WAM if its checkpoint becomes available.\n\n**5. NARROW THE CONTRIBUTION CLAIM:** Drop 'spectral compression' and 'per-perturbation analysis' as contributions — they dilute the method focus. If spectral guidance works, that alone is sufficient for CoRL. If it doesn't work, compression and analysis don't save the paper.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"UWM BASE MODEL WEAKNESS (CRITICAL): UWM achieves only ~79% average success on standard LIBERO evaluation tasks, far below SOTA (Fast-WAM 97.6%, Being-H0.7 99.2%, MotuBrain ~95%+). Running SCG on top of a 79% baseline means even if guidance provides a 5-10% improvement under perturbation, the absolute numbers will be uncompetitive with OA-WAM (84.3% geo-avg) which starts from a stronger base. CoRL reviewers will question why the base model is so much weaker than contemporaries. The proposal must either (a) demonstrate that UWM fine-tuned on specific LIBERO tasks achieves competitive performance (the 79% is from pretraining; task-specific fine-tuning should be much higher), or (b) switch to a stronger backbone.\", \"UWM HAS NO LIBERO-PLUS BASELINE (HIGH RISK): UWM has never been evaluated on LIBERO-Plus. Establishing UWM's LIBERO-Plus baseline requires engineering effort (environment setup, perturbation pipeline integration) and the results are completely unknown. If UWM scores <50% on geometric perturbations (plausible given its weaker standard LIBERO performance), improvements from SCG may still leave it far below OA-WAM/CKT-WAM. This unknown should be resolved in the first 2-3 days before committing to the full plan.\", \"CONTINGENT METHOD CONTRIBUTION MISMATCHES USER REQUIREMENT: The user explicitly requires 'METHOD ONLY — new inference algorithm.' Phase 1 is diagnostic, not a method contribution. If Phase 1 shows no signal (high probability given Fast-WAM/GigaWorld-Policy/MotuBrain all finding video dispensable), the paper reduces to a negative empirical finding. The proposal's fallback ('significant negative result that redirects the field') does not satisfy the METHOD ONLY constraint. The proposal should have a concrete method fallback that works regardless of Phase 1 outcome.\", \"NULL RESULT PROBABILITY REMAINS STRUCTURALLY HIGH: Three independent lines of evidence (Fast-WAM, GigaWorld-Policy, MotuBrain) converge on video features being dispensable at inference. The hypothesis that geometric perturbation changes this is reasonable but entirely speculative — zero prior evidence supports it. The probability of Phase 1 yielding a null result (video guidance provides no benefit even under perturbation) is non-trivial, perhaps 40-60%. The proposal handles this gracefully with the two-phase structure, but doesn't adequately address what happens next.\", \"CALIBRATION TRANSFERABILITY REMAINS UNADDRESSED: AQC requires ~100 calibration trajectories per task to compute the SVD and select components. The proposal mentions cross-task transfer as an ablation but doesn't address whether the action-relevant subspace is stable across (a) different LIBERO tasks, (b) different perturbation types (camera vs. robot-init), or (c) different difficulty levels. If recalibration is needed per task × perturbation type, SCG's practical advantage over training-based methods (OA-WAM, CKT-WAM) is significantly reduced.\", \"FIELD TRAJECTORY CONCERN: Being-H0.7 (May 2026) achieves 99.2% on LIBERO and 82.1%/84.8% on LIBERO-Plus using latent world-action queries WITHOUT explicit video branches. This suggests the field is moving toward implicit world modeling where the video→action guidance signal SCG filters simply doesn't exist. SCG is architecturally specific to WAMs with explicit video branches — a shrinking target.\"]\nFeedback: The proposal has improved substantially from Round 4 — the Fast-WAM correction, switch to UWM, and AQC contribution are genuine advances. The research question is well-framed. However, three structural issues must be resolved:\n\n**1. FIX THE UWM BASELINE GAP (MOST URGENT):** UWM's ~79% on LIBERO is a pretraining-only number. The proposal must explicitly state (and ideally verify) that task-specific fine-tuning from the LIBERO-90 checkpoint achieves competitive performance (>90%). The UWM paper reports fine-tuning for 10K steps per task — run this first on 2-3 LIBERO tasks and report the fine-tuned success rate before committing to the full plan. If fine-tuned UWM achieves >92% on standard LIBERO, the baseline is acceptable. If it stays at ~79%, switch backbone or abandon this approach.\n\n**2. ADD A PHASE-1-INDEPENDENT METHOD CONTRIBUTION:** The user needs a METHOD paper. Consider restructuring: instead of making Phase 2 contingent on Phase 1, propose SCG as a general framework for modality-selective guidance in multi-modal diffusion models, with UWM/WAM as the primary testbed. Even if uniform CFG shows marginal benefit, spectral filtering may still improve the guidance-quality-per-compute tradeoff (fewer effective guidance dimensions → faster convergence → fewer denoising steps). Frame the spectral compression angle as a secondary method contribution: SCG can identify which k of d guidance dimensions matter, enabling 'sparse guidance' that runs faster. This gives a method contribution (efficient selective guidance) independent of whether guidance improves robustness.\n\n**3. ADDRESS UWM-ON-LIBERO-PLUS EARLY:** Before any SCG work, run UWM (fine-tuned) on LIBERO-Plus camera and robot-init perturbations at L1. This takes ~5-10h H100 and answers whether UWM is even competitive enough to serve as a meaningful testbed. If UWM fine-tuned achieves <60% on geometric perturbations, there's enough room for SCG to show improvement. If it achieves >80%, the room for improvement is small but any improvement would be impressive.\n\n**4. STRENGTHEN NOVELTY ARGUMENT AGAINST CPC THEORY:** The CPC paper proves CFG implicitly amplifies 'positive CPCs' and suppresses 'negative CPCs.' Your counter-argument (heterogeneous video→action conditioning lacks well-separated covariance structures) is reasonable but hand-wavy. Sharpen it: (a) CPC analysis assumes class-conditional distributions with shared covariance structure — video→action conditioning has fundamentally different conditional and unconditional covariances because they represent different modalities, not different classes within one modality. (b) AQC selects components based on action-quality correlation, not variance — this is orthogonal to CPC's variance-based implicit selection and should capture different components. Make this argument explicitly in the paper.\n\n**5. SCOPE ICG-ON-FAST-WAM AS EXTENSION, NOT CORE:** ICG on Fast-WAM is interesting but adds complexity and hasn't been validated for cross-modal robot control. Keep it as a single-paragraph extension experiment, not a core contribution. Focus the paper tightly on UWM + spectral filtering.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T19:45:45.062Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T19:45:45.062Z",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-10T19:45:45.113Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).

Direction: World Action Models (WAMs) — joint world modeling and action prediction in a unified architecture, often built on video diffusion priors. In-scope: unified video+action prediction, MoT (Mixture-of-Transformers) architectures with text/video/action streams, WMs that double as policies via inverse dynamics on imagined futures, action-conditioned video diffusion as policy.

Recent landscape (do not duplicate): UniVLA, DreamVLA, GigaBrain-0.5M, DiT4DiT, MotuBrain, video-diffusion-as-policy lines. WAMs are the hottest CoRL 2026 area — high competition but high reward.

Contribution type: METHOD ONLY. New unified architecture, new training scheme that fuses world prediction and action prediction, new inference algorithm extracting actions from imagined futures.

SIM-ONLY MITIGATION: WAM papers at CoRL routinely use sim envs since the method depends on data scale, not real-robot deployment. Use LIBERO/ManiSkill as primary and frame contribution as architectural.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Most challenging budget — video models are heavy. Strategies: (a) fine-tune an open video WM (Cosmos releases, OpenSora, CogVideoX) with action conditioning, (b) distill a large WAM into a smaller one, (c) propose a method that requires only small additional training on top of an existing WAM, (d) propose an inference-time method that needs no training.
2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos.
3. Eval: LIBERO, ManiSkill 2/3, RoboCasa for closed-loop control + video prediction quality (PSNR/SSIM/FVD on action-conditioned futures). Compare against UniVLA / DreamVLA / DiT4DiT lineage if open releases exist.

Look for: efficient action-conditioning of video diffusion, latent WAMs that bypass pixel decoding, methods that share representations across world and action streams. Avoid: trivial action-token prepending without architectural insight.

Tag: direction=world_action_model, contribution_type=method. target_venues=["CoRL 2026"].**
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

## Idea under review (round 6/10)
{
  "title": "Spectral Cross-Modal Guidance: Training-Free Selective Amplification of World Knowledge for Robust Action Generation",
  "core_problem": "World-Action Models (WAMs) achieve near-saturated performance on standard manipulation benchmarks (Being-H0.7: 99.2%, Fast-WAM: 97.6% on LIBERO) but remain brittle under geometric perturbations — camera viewpoint and robot initial state changes cause drops to 60–90% on LIBERO-Plus. Concurrently, Fast-WAM, GigaWorld-Policy, and MotuBrain demonstrate that video features are dispensable at inference under standard conditions. These facts appear contradictory: if video-encoded spatial knowledge is dispensable, why do WAMs fail precisely under geometric perturbations where spatial reasoning should matter most? We hypothesize the resolution lies in HOW video information is used, not WHETHER it is used. Under standard conditions, the action branch encodes sufficient visual-motor mappings from the training distribution, making video features redundant. Under geometric perturbation, these mappings break — and the video branch's spatial reasoning could compensate, but only if the video→action guidance signal is properly amplified and filtered. Standard classifier-free guidance (CFG) in diffusion models amplifies all conditional contributions equally, mixing action-relevant spatial information with irrelevant appearance features. CPC theory (NeurIPS 2025) proves CFG implicitly performs selective amplification via contrastive principal components, but only in class-conditional settings with well-separated covariance structures — not in heterogeneous cross-modal settings like video→action guidance. The core question: can explicit spectral filtering of the cross-modal guidance signal selectively amplify geometric/spatial components that improve robustness while suppressing components that add noise? Before answering this, a prior diagnostic question must be settled: does cross-modal guidance in WAMs carry any action-relevant signal at all under geometric perturbation? No existing work has tested this.",
  "opportunity": "Three converging developments create a precise research opportunity, and a critical correction from the prior proposal version enables a more principled approach: (1) UWM (RSS 2025) uses UniDiffuser-style independent diffusion timesteps for video and action modalities — setting the video timestep t_o'=T marginalizes video information, yielding the unconditional action score, while t_o'&lt;T yields the video-conditioned action score. This natively enables cross-modal CFG through two forward passes without any dropout training, architectural modification, or fine-tuning. UWM releases a pretrained LIBERO-90 checkpoint. (2) LIBERO-Plus and the WAM robustness study (March 2026) reveal that geometric perturbations remain the dominant failure mode: OA-WAM Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%), CKT-WAM (Camera 77.4%, Robot 71.4%), with the overall LIBERO-Plus SOTA at 86.1% (CKT-WAM). Crucially, all geometric robustness improvements to date (OA-WAM, CKT-WAM) require architectural modification or additional training — no training-free inference-time method has been attempted. (3) Independent Condition Guidance (ICG, ICLR 2025) demonstrates that CFG-quality guidance can be obtained from any pretrained conditional model without dropout training, by substituting the unconditional score with a prediction conditioned on a random/independent input. This enables cross-modal guidance on WAMs like Fast-WAM that were not trained with video dropout. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection for filtering diffusion guidance signals, but only in single-modal image restoration. CRITICAL CORRECTION: The prior version incorrectly claimed Fast-WAM was trained with unconditional video feature dropout enabling native CFG. After verification — reading the full paper, project page, and GitHub — this claim is unsupported. Fast-WAM uses CFG scale 1.0 (no guidance amplification), and 'uncond' in checkpoint names refers to its unconditional inference mode (no future video denoising), not CFG-enabling dropout training. UWM's independent timestep mechanism provides the principled alternative, with ICG as a backbone-agnostic complement.",
  "landscape": "**Video-at-inference in WAMs:** Fast-WAM (March 2026) removes video denoising at inference, retaining only backbone features. GigaWorld-Policy (March 2026) uses causal masking to block video→action flow. MotuBrain (April 2026) freezes video branch and caches KV pairs. All use binary approaches (all or no video features) and evaluate only on standard benchmarks — none test under geometric perturbation. **Cross-modal CFG support in WAMs:** UWM (RSS 2025) uses independent diffusion timesteps for video and action, enabling native cross-modal conditioning control by setting t_o'=T to marginalize video. Motus (Dec 2025) uses a similar UniDiffuser-style architecture. X-WAM (April 2026) uses asynchronous noise sampling across modalities. Vid2World (ICLR 2026) applies CFG in the action→video direction for video quality. DreamZero (Feb 2026) uses parallelized CFG for real-time inference. No work systematically applies or evaluates cross-modal CFG in the video→action direction for action quality or robustness improvement under perturbation. **Training-free guidance methods:** ICG (ICLR 2025) provides CFG-quality guidance on any pretrained conditional model using independent/random conditions, without dropout training — validated on image generation but not cross-modal robot control. **CFG Theory:** CPC decomposition (NeurIPS 2025) proves CFG implicitly decomposes into mean-shift + positive CPC + negative CPC; explicitly notes limitations when conditional covariances lack discriminative structure — the expected case for heterogeneous video→action conditioning. **SVD-based guidance filtering:** DiffStateGrad (ICLR 2025) projects measurement gradients onto SVD subspaces for image restoration. Related SVD approaches exist for controllable editing (Feb 2025) and concept removal (March 2025). All operate in single-modal image settings; none address cross-modal guidance for robot control. **Geometric robustness methods (competitors):** OA-WAM (May 2026): object-addressable architecture, Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%) — requires architectural modification. CKT-WAM (May 2026): parameter-efficient context transfer, total 86.1% (Camera 77.4%, Robot 71.4%) — requires additional training. Being-H0.7 (May 2026): latent world-action queries with posterior alignment, 82.1% zero-shot / 84.8% fine-tuned — uses implicit world modeling without explicit video branch. π0.5: 85.7% total. AnyCamVLA (March 2026): zero-shot camera adaptation via feed-forward novel view synthesis, training-free but VLA-specific and camera-only. ADPro (2025): test-time adaptive diffusion policy via manifold-constrained denoising, evaluated on RLBench/CALVIN but not LIBERO-Plus. GPC (Feb 2025): inference-time enhancement via predictive world model look-ahead, requires a separately trained world model. **Selective world-model usage:** WoG (Feb 2026) compresses world predictions via learned Q-Former — requires retraining. FFDC (May 2026) decides WHEN to replan, not HOW MUCH or WHICH influence to apply within denoising. **Gap:** No existing work (1) applies cross-modal CFG in the video→action direction of WAMs with systematic evaluation under geometric perturbation, (2) uses spectral filtering to selectively amplify action-relevant components of the cross-modal guidance signal, or (3) provides a training-free, architecture-agnostic method targeting WAM geometric robustness specifically.",
  "approach": "We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method for selectively amplifying action-relevant world knowledge in WAMs, targeting geometric robustness. The approach is structured in two phases: a diagnostic phase establishing whether cross-modal guidance carries useful signal under perturbation, and a method phase applying spectral filtering if signal exists.\n\n**Phase 1 — Cross-Modal Guidance Diagnostics (primary empirical contribution).** Before spectral filtering, we answer the foundational question: does amplifying video→action guidance improve WAM robustness under geometric perturbation? Using UWM's independent timestep mechanism, we compute the guidance vector g_t = ε(a; t_a, t_o'=t_a) − ε(a; t_a, t_o'=T) at each action denoising step t. The first term uses joint denoising (video and action at matched noise levels, exchanging information through shared attention); the second marginalizes video by setting t_o'=T (pure noise). The guided prediction: ε_guided = ε_marginal + w·g_t. We sweep w ∈ {1.0, 1.5, 2.0, 3.0, 5.0} on both standard LIBERO (sanity check — expect no benefit, confirming video dispensability under standard conditions) and LIBERO-Plus geometric perturbations (camera, robot-init at L1/L3 difficulty). This takes ~25-30h H100 and definitively answers whether guidance carries signal. If uniform CFG shows zero improvement under geometric perturbation at all scales, the paper pivots to a diagnostic/negative-result contribution analyzing what video branches encode vs. what geometric robustness requires.\n\n**Phase 2 — Spectral Filtering with Action Quality Correlation (method contribution, contingent on Phase 1).** If Phase 1 reveals that uniform CFG helps (or helps inconsistently — improving some perturbation types but hurting others), we apply spectral filtering to selectively amplify beneficial components. Collect guidance vectors {g_t} across a calibration set (~100 trajectories from LIBERO training data) at each of K=10 denoising steps. For each step t, compute the SVD of the guidance covariance C_t = (1/N)Σ g_t g_t^T = U_t Λ_t U_t^T. For automatic component selection, compute Action Quality Correlation (AQC) for each principal direction u_i: the Spearman rank correlation between |u_i^T g_t| and action quality improvement (loss reduction) when the component is included. Retain components with AQC exceeding a permutation-null threshold (p<0.05), yielding projection Π_t. Filtered guidance: ε_guided = ε_marginal + w(t)·Π_t(g_t), where w(t) follows β-CFG timestep-adaptive scheduling. This extends DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control, with the key difference being AQC-calibrated selection rather than state-defined projection.\n\n**Backbone Strategy.** Primary: UWM with released LIBERO-90 checkpoint, fine-tuned on LIBERO tasks. UWM's independent timesteps provide mathematically clean cross-modal CFG: t_o'=T gives the unconditional (video-marginalized) action score natively, with no dropout training or architectural modification needed. Secondary (extension for backbone-agnosticism): ICG applied to Fast-WAM. ICG approximates the unconditional score by conditioning on a random/independent input — for video features, this means substituting real video tokens with random embeddings sampled from a matched distribution. ICG has been validated on image diffusion models (ICLR 2025) but not cross-modal robot control; testing it here is itself a novel contribution. If ICG on Fast-WAM produces consistent results with UWM's native CFG, this demonstrates SCG's architecture-agnosticism.\n\n**Evaluation strategy.** Primary benchmark: LIBERO-Plus with 3 perturbation types — camera and robot-init (geometric, where video knowledge should help most), plus light as control (where WAMs already excel, expect no benefit from guidance). 2 difficulty levels (L1, L3), 2 seeds. Standard LIBERO as sanity check. Baselines: (i) UWM standard policy (t_o'=T, no guidance), (ii) UWM joint denoising (t_o'=t_a, no guidance amplification — equivalent to CFG w=1.0), (iii) Uniform cross-modal CFG (w>1), (iv) SCG with AQC spectral filtering (ours). Ablations: (a) AQC threshold sensitivity, (b) per-step vs. global SVD, (c) cross-task transfer of calibrated subspace (calibrate on LIBERO tasks A, evaluate on tasks B), (d) AQC-selected directions vs. top-variance directions (testing whether action-relevant ≠ high-variance), (e) ICG on Fast-WAM vs. UWM native CFG (backbone comparison). Framing vs. OA-WAM: SCG is training-free and architecture-agnostic, complementary to OA-WAM's architectural approach. We explicitly frame SCG as applicable to any WAM with video/action branches, including potentially OA-WAM itself if its checkpoint becomes available.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~100-140h H100",
      "gpu_utilization": "Low-moderate (25-35%). Human sets up UWM + LIBERO-Plus integration, fine-tunes UWM, implements cross-modal CFG and SVD pipeline, runs evaluation sweeps.",
      "timeline": "2.5-3 weeks (feasible for CoRL abstract May 26, paper May 29)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$250-420 (at ~$2.50-3.00/H100-hr spot pricing, May 2026)"
    },
    "human_in_loop": {
      "gpu_hours": "~110-160h H100",
      "gpu_utilization": "Moderate-high (55-70%). Agent implements cross-modal CFG on UWM, integrates LIBERO-Plus, queues Phase 1 diagnostic sweeps. Human reviews Phase 1 results to decide Phase 2 (~1hr at decision point, then ~30min/day).",
      "timeline": "14-18 days (targets CoRL 2026 abstract May 26, paper May 29)",
      "team": "1 researcher, ~30-45min/day",
      "claude_api_cost": "$100-250 (estimated ~1000-2500 Opus turns)",
      "estimated_gpu_cost": "$275-480",
      "risk_note": "Primary risk is UWM fine-tuning achieving competitive LIBERO performance. UWM's released LIBERO-90 checkpoint and fine-tuning code reduce this risk. Phase 1 diagnostic is quick (~25-30h) and provides go/no-go signal for Phase 2."
    },
    "auto_research": {
      "gpu_hours": "~130-200h H100",
      "gpu_utilization": "High (>85%). Agent runs continuous Phase 1 diagnostic → Phase 2 calibration → evaluation loop.",
      "timeline": "10-14 days with 2-4 GPUs concurrently",
      "team": "0 (initial setup only, ~2 hours)",
      "claude_api_cost": "$180-400 (estimated ~1800-4000 Opus turns)",
      "estimated_gpu_cost": "$325-600",
      "speed_bottleneck": "Phase 1 must complete before Phase 2 begins. Phase 1: ~25-30h across 3 perturbation types × 5 CFG scales × 2 difficulties × 2 seeds = 60 configs. Phase 2: ~40-60h for SVD calibration + SCG evaluation.",
      "risk_note": "Agent must correctly interpret Phase 1 results (is there signal?) before proceeding. Human review of Phase 1 results recommended even in auto mode. UWM fine-tuning failure would require fallback to ICG-on-Fast-WAM."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16-19 days; Phase 1 diagnostic is achievable within first week, Phase 2 within second; tight but feasible with UWM checkpoint and focused scope)",
    "AAAI 2027 (deadline Aug 2, 2026 — secondary target if CoRL revision needed; allows ICG-on-Fast-WAM extension, additional WAM backbones, full LIBERO-Plus sweep across all 7 perturbation types)",
    "ICLR 2027 (deadline Sep 24, 2026 — fallback; allows comprehensive multi-backbone study, deeper mechanistic analysis, and potential integration with OA-WAM)"
  ],
  "level": "solid",
  "key_references": [
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [UWM] (RSS 2025) — PRIMARY BACKBONE; independent diffusion timesteps for video/action natively enable cross-modal CFG by setting t_o'=T to marginalize video; released LIBERO-90 checkpoint with fine-tuning code",
    "No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models [ICG] (ICLR 2025) — Independent Condition Guidance enables CFG on any pretrained conditional model without dropout training; backbone-agnostic complement to UWM; uses random/independent conditions to approximate unconditional score",
    "Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — proves CFG implicitly decomposes into selective amplification (positive CPC) and suppression (negative CPC); limited to class-conditional settings with well-separated covariance structures",
    "Diffusion State-Guided Projected Gradient for Inverse Problems [DiffStateGrad] (ICLR 2025) — SVD-based subspace projection in diffusion models for image inverse problems; key methodological predecessor; single-modal, external gradient projection",
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — demonstrates video dispensable at inference under STANDARD conditions; secondary backbone candidate via ICG; NOTE: does NOT support native CFG via dropout training (corrected from prior version)",
    "Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv March 2026) — WAMs weak on geometric perturbations; camera 60-80%, robot-init 63-90%; motivates the robustness focus",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark with L1-L5 difficulty levels",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv May 2026) — LIBERO-Plus Geo-Avg SOTA at 84.3% (Camera 80.5%, Robot 89.6%); requires architectural modification; SCG is complementary (training-free, architecture-agnostic)",
    "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv May 2026) — LIBERO-Plus total SOTA at 86.1% (Camera 77.4%, Robot 71.4%); requires additional training",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv May 2026) — LIBERO standard SOTA at 99.2%; LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned; uses latent world-action queries without explicit video branch",
    "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models (arXiv March 2026) — training-free camera adaptation via novel view synthesis; VLA-specific, camera-perturbation-only; complementary approach",
    "ADPro: Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising (2025) — test-time adaptation via geometric manifold constraints; evaluated on RLBench/CALVIN, not LIBERO-Plus; related inference-time approach",
    "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling [GPC] (RA-L 2025) — augments frozen diffusion policy with separately trained world model for inference-time look-ahead; requires additional world model training; SCG uses built-in video branch instead",
    "Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational CFG technique",
    "Classifier-free Guidance with Adaptive Scaling [β-CFG] (arXiv Feb 2025) — timestep-adaptive guidance scheduling",
    "Vid2World: Crafting Video Diffusion Models to Interactive World Models (ICLR 2026) — CFG in action→video direction",
    "GigaWorld-Policy: An Efficient Action-Centered World-Action Model (arXiv March 2026) — causal masking prevents video→action flow",
    "MotuBrain: An Advanced World Action Model for Robot Control (arXiv April 2026) — KV cache for video features",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models [FFDC] (arXiv May 2026) — confidence-based replanning at execution level; orthogonal",
    "World Guidance: World Modeling in Condition Space for Action Generation [WoG] (arXiv Feb 2026) — learned world-model compression; requires retraining",
    "X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv April 2026) — asynchronous noise sampling across modalities; depth prediction for 3D awareness; potential alternative backbone with independent timestep control",
    "DreamZero: World Action Models are Zero-shot Policies (arXiv Feb 2026) — parallelized CFG in WAM inference",
    "Motus: A Unified Latent Action World Model (arXiv Dec 2025) — UniDiffuser-style WAM; potential alternative backbone",
    "One Transformer Fits All Distributions in Multi-Modal Diffusion [UniDiffuser] (ICML 2023) — foundational independent timestep mechanism",
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control (arXiv Jan 2026) — LIBERO-Plus 82.2%",
    "Mechanistic Dissection of Cross-Attention Subspaces in Text-to-Image Diffusion Models (AAAI 2025) — SVD-based spectral analysis of concept-encoding subspaces",
    "Test-Time Perturbation Learning with Delayed Feedback for VLA Models [TTPL] (arXiv April 2026) — verifier-free test-time adaptation; complementary approach"
  ],
  "description": "We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method that selectively amplifies action-relevant world knowledge from the video branch of World-Action Models (WAMs), targeting robustness under geometric perturbations (camera viewpoint, robot initial state). The work is structured as a two-phase investigation. Phase 1 (diagnostic): WAMs achieve near-perfect standard benchmark performance (Fast-WAM 97.6%, Being-H0.7 99.2%) but remain brittle under geometric perturbation (OA-WAM Camera 80.5%, CKT-WAM Camera 77.4%). Multiple works show video features are dispensable at inference under standard conditions — but none test whether amplifying video→action guidance helps under geometric perturbation, where the action branch's learned visual-motor mappings break and the video branch's spatial reasoning could compensate. We use UWM's (RSS 2025) independent timestep mechanism — setting video timestep t_o'=T marginalizes video, giving the unconditional action score; t_o'&lt;T gives the video-conditioned score — to natively enable cross-modal CFG without dropout training or architectural modification. A systematic CFG scale sweep across LIBERO-Plus geometric perturbations answers whether guidance carries action-relevant signal. CRITICAL CORRECTION from prior version: Fast-WAM was previously claimed to support native CFG via video feature dropout, but this is unverified — the paper never mentions dropout training, uses CFG scale 1.0 (no amplification), and 'uncond' in checkpoint names refers to unconditional inference mode. UWM's independent timesteps provide the principled alternative. Phase 2 (method): If Phase 1 reveals signal, SCG applies SVD-based spectral filtering to the guidance vector g_t = ε_cond − ε_uncond, retaining only directions whose Action Quality Correlation (AQC) — Spearman correlation between projection magnitude and action quality improvement — exceeds a permutation-null threshold. This makes component selection automatic and parameter-free, extending DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control with action-quality calibration. For backbone-agnosticism, we additionally test Independent Condition Guidance (ICG, ICLR 2025), which approximates unconditional scores via random conditions on any pretrained model, applied to Fast-WAM. SCG is complementary to OA-WAM (requires architectural modification) and CKT-WAM (requires additional training) — it is training-free, architecture-agnostic, and could be applied on top of these methods. Both phases contribute: Phase 1 provides the first empirical evidence on whether/when world knowledge helps under geometric perturbation (resolving the video-dispensability paradox); Phase 2 provides a practical method for selective guidance when signal exists. If Phase 1 shows no signal, the diagnostic finding itself — that video branches encode information irrelevant to geometric robustness despite encoding spatial features — is a significant negative result that redirects the field away from guidance-based approaches.",
  "project_name": "spectral_cross_modal_guidance_wam",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["UniDiffuser (ICML 2023), the foundation of Motus, already supports cross-modal CFG by design — setting video timestep to T while denoising actions gives the 'unconditional' score. This means VB-CFG can be applied to pre-trained Motus/UWM with ZERO training, making the proposed 'dropout fine-tuning' unnecessary rather than a contribution.", "Fast-WAM (March 2026) demonstrated that video prediction's value lies in training-time representation learning, not test-time features. This directly challenges VB-CFG's core hypothesis that amplifying video features at inference improves actions — if the learned representations already encode world knowledge, amplifying video tokens may amplify noise rather than signal.", "'No Training, No Problem: Rethinking Classifier-Free Guidance' (ICLR 2025) shows CFG works on any pre-trained conditional model without dropout training, further reducing the proposed dropout fine-tuning from 'lightweight contribution' to 'unnecessary overhead.'", "LIBERO benchmark is already saturated (>90% success rate for SOTA methods like MotuBrain). Marginal improvements will not be compelling for CoRL reviewers. RoboTwin 2.0 scores also show MotuBrain at 95-96 in both clean and randomized settings.", "The contribution as described is an empirical study ('does CFG in video→action direction help?'), not a method paper. The user's requirement explicitly asks for 'METHOD ONLY: new unified architecture, new training scheme, new inference algorithm.' Trying an existing technique in a new direction doesn't qualify as a new inference algorithm.", "Vid2World (ICLR 2026) already establishes CFG within WAMs. Applying it in the reverse direction is the obvious next experiment — exactly the kind of 'trivial action-token prepending without architectural insight' the user asked to avoid."]
Feedback: The core observation (video features could be selectively amplified during action denoising) is valid but insufficiently novel for CoRL as a standalone method. To save this direction, consider: (1) **Add genuine technical depth** — propose adaptive per-timestep guidance (guidance scale that changes during the action denoising trajectory), per-token guidance (different video tokens contribute differently), or latent-subspace guidance that operates on identified action-relevant video feature dimensions rather than the full video branch. (2) **Confront the Fast-WAM tension directly** — frame the contribution as 'understanding when and how video features help action prediction' with a mechanistic analysis (which video dimensions encode safety-relevant vs. efficiency-relevant information), going beyond simple guidance scale sweeps. (3) **Target harder benchmarks** — LIBERO is too saturated; use LIBERO-Plus with perturbations, or focus on out-of-distribution generalization where world-model amplification could plausibly help. (4) **Acknowledge UniDiffuser's inherent CFG support** — include zero-shot CFG (no fine-tuning) as a baseline and position dropout training as providing sharper conditional/unconditional separation. (5) **Consider combining with adaptive execution** — merge with the 'When to Trust Imagination' insight to propose adaptive guidance scales based on task difficulty or prediction confidence. This would be a genuine novel inference algorithm rather than a parameter sweep.

### Round 2 review
Verdict: revise
Issues: ["VENUE MISMATCH (CRITICAL): The idea explicitly states CoRL 2026 is 'too tight' and targets ICLR 2027 as primary. The user's hard requirement is CoRL 2026 (deadline May 29, 2026 — 19 days). This is a direct constraint violation.", "CPC THEORY UNDERMINES CORE PREMISE: 'Towards Understanding the Mechanisms of Classifier-Free Guidance' (NeurIPS 2025) proves CFG already inherently decomposes into selective amplification of class-specific features (positive CPC) and suppression of generic features (negative CPC). SCG's explicit SVD-based filtering may be adding complexity to achieve what CFG already does implicitly — the burden of proof is on showing the explicit approach significantly outperforms the implicit one.", "MISSING COMPETITOR — World Guidance (WoG, arxiv 2602.22010, Feb 2026): This paper maps world-model predictions into compact conditions for action inference, directly addressing the same problem (selective use of world knowledge for actions) via a different mechanism (learned compression vs post-hoc spectral decomposition). Must be cited and differentiated against.", "FAST-WAM TENSION UNRESOLVED: Fast-WAM shows video features' primary value is in training-time representation learning. If video→action guidance at inference carries limited useful signal, then even selective amplification of the 'best' spectral components yields negligible improvement. The calibration step might simply discover that no components reliably help.", "TIMESTEP-ADAPTIVE COMPONENT IS NOT NOVEL: β-CFG (Feb 2025), Dynamic CFG via Online Feedback (Sep 2025), and 'Applying Guidance in a Limited Interval' (NeurIPS 2024) all propose timestep-adaptive guidance scheduling. This component cannot be claimed as part of the contribution.", "COMPUTE BUDGET VIOLATION: Auto research mode estimates 400-700h H100, exceeding the user's 200h hard constraint. Even the human-in-loop mode (180-280h) may exceed budget. Only the manual mode (100-180h) fits within 200h, but manual mode requires 2-3 months — incompatible with 20-day deadline.", "CALIBRATION MAKES 'TRAINING-FREE' MISLEADING: The method requires task-specific calibration on ~100 trajectories to identify the action-relevant subspace. This calibration is data-dependent and may not transfer across tasks/environments, limiting the claimed 'architecture-agnostic' generality."]
Feedback: The revision substantially improved technical depth from Round 1, but faces fundamental challenges:

**To save this direction for CoRL 2026:**

1. **MUST target CoRL 2026 explicitly** — reframe the scope to be achievable in 19 days. Suggestion: narrow to a single backbone (Motus), single benchmark (LIBERO-Plus camera/robot-init perturbations only), and position as a focused empirical+mechanistic study.

2. **Address the CPC challenge head-on**: The NeurIPS 2025 paper shows CFG already selectively amplifies discriminative directions. Your contribution must show WHY explicit SVD-based filtering outperforms this implicit mechanism. Hypothesis: in the cross-modal WAM setting (unlike text→image), the guidance vector mixes heterogeneous information (spatial, dynamics, appearance) that don't align with the top principal components of the data distribution — requiring explicit calibration-based selection. Frame this as the core research question, not an assumed benefit.

3. **Cite and differentiate from World Guidance (WoG, arxiv 2602.22010)**: WoG solves the same problem via learned compression. SCG's advantage: training-free, post-hoc, applicable to any pre-trained WAM. WoG's advantage: end-to-end optimized. Position SCG as complementary/alternative for settings where retraining is infeasible.

4. **Resolve Fast-WAM tension with a testable hypothesis**: Argue that Fast-WAM's finding (video features dispensable at inference) applies to STANDARD settings where training representations suffice, but under PERTURBATION (LIBERO-Plus camera shifts, robot-init changes), the world model's geometric reasoning becomes newly relevant at inference — this is testable and would be a strong contribution if confirmed.

5. **Drop the timestep-adaptive component as a claimed contribution** — acknowledge it as existing technique (cite β-CFG, Dynamic CFG) and include only as an engineering choice. Focus novelty entirely on the spectral subspace decomposition of cross-modal guidance.

6. **Ensure compute stays within 200h**: Narrow evaluation to 3-4 perturbation types × 3 difficulty levels × 2 seeds on LIBERO-Plus, plus standard LIBERO as sanity check. This reduces evaluation to ~50-80h H100 + ~20h calibration = within budget.

### Round 3 review
Verdict: revise
Issues: ["COMPUTE BUDGET VIOLATION (CRITICAL): Motus has NO publicly released LIBERO checkpoint — only Motus_robotwin2 is available on HuggingFace. The Motus paper's Stage 3 fine-tuning consumed ~400 GPU-hours. Fine-tuning Motus on LIBERO would cost 100-400h H100 BEFORE any SCG calibration or LIBERO-Plus evaluation. The proposal's 90-130h estimate completely omits this cost, making total compute 300-500h+ H100, far exceeding the 200h hard constraint.", "CONTRIBUTION TYPE MISMATCH: The user explicitly requires 'METHOD ONLY — new inference algorithm.' SCG is technically an inference modification, but the proposal hedges: 'Even if SCG shows marginal improvement over uniform CFG... the spectral analysis reveals the structure of cross-modal information flow — a contribution independent of method performance.' This self-hedging reveals it is primarily an analysis/diagnostic paper, not a method paper. A CoRL reviewer will score method novelty lower when the authors themselves frame the analysis as the robust contribution.", "NULL RESULT RISK IS HIGH AND INADEQUATELY MITIGATED: Fast-WAM, GigaWorld-Policy, and MotuBrain all find video features dispensable at inference. The perturbation hypothesis (H2: video guidance helps under geometric perturbation) is testable but risky — no prior evidence supports it. If both H1 and H2 yield null results (SCG ≈ CFG ≈ no-video under all conditions), the paper reduces to 'we decomposed a signal that doesn't matter.' The claim that spectral analysis is valuable regardless is weak for a method-focused venue.", "MOTUS-LIBERO INTEGRATION RISK: Motus was developed on RoboTwin with its own data pipeline, observation format, and sim environment (ManiSkill-based). Adapting Motus to LIBERO (MuJoCo-based) requires non-trivial engineering for observation preprocessing, action space mapping, and data format conversion. This integration work could consume 5-7 days of the 19-day timeline, leaving insufficient time for the actual research contribution.", "LIBERO-PLUS EVALUATION INCOMPLETE: The proposal claims CKT-WAM (86.1%), OA-WAM (Geo-Avg 76.0%), and Cosmos-Policy (82.2%) as LIBERO-Plus baselines. However, none of these use Motus as backbone, making direct comparison confounded by architecture differences. The proposal needs to compare SCG-Motus vs. standard-Motus vs. Fast-WAM-Motus to isolate the effect of spectral guidance, but Motus has no LIBERO-Plus results in the literature to serve as baseline.", "CALIBRATION SET DEPENDENCY WEAKENS GENERALITY: SCG requires collecting ~100 trajectory guidance vectors for SVD calibration, making it task-specific. The proposal doesn't discuss whether the calibrated subspace transfers across LIBERO tasks, perturbation types, or environments. If per-task recalibration is needed, the practical advantage over WoG's end-to-end retraining diminishes."]
Feedback: The framing around CPC theory is a genuine improvement from Round 2 — the research question is well-posed and timely. However, three structural problems must be resolved:

**1. Fix the compute/backbone crisis (MOST URGENT):** Switch from Motus to UWM as the primary backbone. UWM has a publicly released LIBERO-90 pretrained checkpoint (Google Drive, WEIRDLabUW/unified-world-model), uses the same UniDiffuser-style independent timesteps as Motus, and has established LIBERO evaluation infrastructure. Fine-tuning UWM on LIBERO-specific tasks should be far cheaper than Motus Stage 3 (~400h). Alternatively, check if Fast-WAM (github.com/yuantianyuan01/FastWAM) releases LIBERO checkpoints for a WAM backbone that already addresses the video-at-inference question — this would give you a natural baseline.

**2. Strengthen the method contribution to match user requirements:** The user needs a 'new inference algorithm,' not an analysis paper. To make SCG a genuine method contribution: (a) Add adaptive component selection — instead of fixed top-k, propose an automatic criterion for selecting k based on the eigenvalue gap or action-quality correlation threshold, making SCG parameter-free. (b) Propose per-perturbation-type component routing — if different spectral components activate for camera vs. robot-init perturbations (as hypothesized), design a lightweight detector that identifies the perturbation type and selects the appropriate spectral subspace automatically. This makes SCG an adaptive inference algorithm, not just SVD + projection.

**3. Derisk null results with a concrete fallback:** If video→action CFG provides no benefit even under geometric perturbation, the pure analysis paper is too thin for CoRL. Consider a concrete fallback: show that the spectral decomposition can be used to EFFICIENTLY COMPRESS the video branch (retain only k components instead of full video denoising), achieving Fast-WAM-like speedup while preserving the specific spectral components that help under perturbation. This gives a practical contribution (efficient selective video usage) even if the guidance scale sweep shows marginal gains.

**4. Timeline and scope:** 19 days is barely feasible even with the right backbone. Drop all secondary benchmarks (ManiSkill, RoboCasa) and focus exclusively on LIBERO-Plus with 2 geometric perturbation types (camera, robot-init) + 1 control (light) at 2 difficulty levels and 2 seeds. This reduces evaluation from 48 configs to ~18, saving significant GPU time.

### Round 4 review
Verdict: revise
Issues: ["CRITICAL — UNVERIFIED CORE ASSUMPTION: Fast-WAM's 'unconditional dropout on video features enabling native CFG' is fabricated or at minimum unverified. After reading the full paper (arxiv 2603.16666), project page, GitHub README, and HuggingFace model card: (a) the paper NEVER mentions unconditional dropout on video features, (b) NEVER discusses video→action CFG, (c) uses CFG scale 1.0 which means zero guidance amplification, (d) contains no mentions of 'p_uncond', 'null condition', 'empty token', or 'mask probability'. The 'uncond' in checkpoint names (libero_uncond_2cam224.pt) almost certainly refers to the unconditional inference mode (no future video denoising) — Fast-WAM's core contribution — NOT to CFG-enabling dropout training. Without verified video feature dropout training, computing ε_uncond by zeroing video features produces out-of-distribution predictions, and the entire SCG pipeline produces unreliable guidance vectors.", "CFG SCALE 1.0 CONTRADICTS CFG READINESS: Fast-WAM's paper explicitly states 'During inference, we use 10 denoising steps with classifier-free guidance (CFG) scale set to 1.0.' Scale 1.0 means ε_guided = ε_uncond + 1.0·(ε_cond - ε_uncond) = ε_cond, i.e., NO guidance amplification at all. This strongly suggests the model was not designed for or evaluated with CFG guidance amplification in any modality direction. If the model doesn't benefit from CFG at scale > 1.0, spectral filtering of the guidance signal is filtering noise.", "NULL RESULT RISK REMAINS STRUCTURALLY HIGH: The proposal acknowledges Fast-WAM's finding that video features are dispensable at inference but hypothesizes they become relevant under geometric perturbation. However, no prior work supports this hypothesis — it is purely speculative. If the guidance vector g_t = ε_cond - ε_uncond carries negligible action-relevant signal (as suggested by video dispensability), then SVD decomposition of near-zero vectors produces noise, not actionable spectral components.", "COMPETITION FROM BEING-H0.7 (May 2026): Being-H0.7 achieves 99.2% on standard LIBERO and strong LIBERO-Plus results using latent world-action queries with posterior alignment — no video generation or video features at inference. This latent approach renders the entire 'video features at inference' question increasingly irrelevant, as the field moves toward implicit world modeling that doesn't require explicit video branches to filter or amplify.", "OA-WAM (May 2026) ALREADY ACHIEVES GEOMETRIC ROBUSTNESS SOTA: OA-WAM reaches Geo-Avg 84.3% on LIBERO-Plus (Camera 80.5%, Robot 89.6%) through object-addressable architectural modification. SCG needs to exceed this without any training — an extremely high bar for an inference-time-only method operating on potentially noisy guidance vectors.", "CALIBRATION TRANSFERABILITY UNTESTED: AQC requires per-task calibration on ~100 trajectories. The proposal hypothesizes cross-task transfer but doesn't address whether the action-relevant subspace is stable across LIBERO's 90 tasks, across perturbation types, or across difficulty levels. If recalibration is needed per task × perturbation type, the practical overhead approaches WoG's end-to-end retraining cost."]
Feedback: The framing and research question are strong — resolving the apparent contradiction between video dispensability and geometric vulnerability is genuinely interesting. However, the proposal has a fatal dependency on an unverified claim about Fast-WAM's training procedure. To save this direction:

**1. VERIFY THE UNCONDITIONAL DROPOUT CLAIM (BLOCKER):** Before any other work, you MUST verify whether Fast-WAM was trained with video feature dropout. Options: (a) Read the actual Fast-WAM training code on GitHub (check train.py or model configs for p_uncond on video features), (b) Contact the Fast-WAM authors directly, (c) Check if Wan2.2's base model has text dropout (likely yes, but this is TEXT not VIDEO features). If Fast-WAM was NOT trained with video dropout, you have three recovery paths: (i) Fine-tune with video dropout (~50-100h H100, tight but potentially feasible within budget), (ii) Use the 'No Training, No Problem' (ICLR 2025) independent condition guidance approach that doesn't require dropout training, (iii) Switch to UWM which uses UniDiffuser-style independent timesteps and may natively support cross-modal CFG by setting video timestep to T.

**2. IF DROPOUT EXISTS — VALIDATE CFG FIRST:** Before building SCG, run a simple experiment: sweep CFG scale w ∈ {1.0, 1.5, 2.0, 3.0, 5.0} on standard LIBERO and LIBERO-Plus camera perturbation. If uniform CFG shows NO improvement at any scale (likely given CFG=1.0 was chosen by the authors), then spectral filtering of a zero-signal is pointless. This takes ~20h H100 and answers the fundamental question in 2-3 days.

**3. CONSIDER UWM AS PRIMARY BACKBONE:** UWM (RSS 2025) uses UniDiffuser-style independent timesteps — setting video timestep to T gives the unconditional score for free, enabling native cross-modal CFG without dropout training. UWM has a released LIBERO-90 checkpoint. This avoids the entire Fast-WAM dropout verification problem.

**4. STRENGTHEN AGAINST OA-WAM COMPARISON:** OA-WAM's Geo-Avg 84.3% is the target to beat. Frame SCG as complementary (training-free, applicable to any WAM including OA-WAM) rather than competitive. Test SCG on top of OA-WAM if its checkpoint becomes available.

**5. NARROW THE CONTRIBUTION CLAIM:** Drop 'spectral compression' and 'per-perturbation analysis' as contributions — they dilute the method focus. If spectral guidance works, that alone is sufficient for CoRL. If it doesn't work, compression and analysis don't save the paper.

### Round 5 review
Verdict: revise
Issues: ["UWM BASE MODEL WEAKNESS (CRITICAL): UWM achieves only ~79% average success on standard LIBERO evaluation tasks, far below SOTA (Fast-WAM 97.6%, Being-H0.7 99.2%, MotuBrain ~95%+). Running SCG on top of a 79% baseline means even if guidance provides a 5-10% improvement under perturbation, the absolute numbers will be uncompetitive with OA-WAM (84.3% geo-avg) which starts from a stronger base. CoRL reviewers will question why the base model is so much weaker than contemporaries. The proposal must either (a) demonstrate that UWM fine-tuned on specific LIBERO tasks achieves competitive performance (the 79% is from pretraining; task-specific fine-tuning should be much higher), or (b) switch to a stronger backbone.", "UWM HAS NO LIBERO-PLUS BASELINE (HIGH RISK): UWM has never been evaluated on LIBERO-Plus. Establishing UWM's LIBERO-Plus baseline requires engineering effort (environment setup, perturbation pipeline integration) and the results are completely unknown. If UWM scores <50% on geometric perturbations (plausible given its weaker standard LIBERO performance), improvements from SCG may still leave it far below OA-WAM/CKT-WAM. This unknown should be resolved in the first 2-3 days before committing to the full plan.", "CONTINGENT METHOD CONTRIBUTION MISMATCHES USER REQUIREMENT: The user explicitly requires 'METHOD ONLY — new inference algorithm.' Phase 1 is diagnostic, not a method contribution. If Phase 1 shows no signal (high probability given Fast-WAM/GigaWorld-Policy/MotuBrain all finding video dispensable), the paper reduces to a negative empirical finding. The proposal's fallback ('significant negative result that redirects the field') does not satisfy the METHOD ONLY constraint. The proposal should have a concrete method fallback that works regardless of Phase 1 outcome.", "NULL RESULT PROBABILITY REMAINS STRUCTURALLY HIGH: Three independent lines of evidence (Fast-WAM, GigaWorld-Policy, MotuBrain) converge on video features being dispensable at inference. The hypothesis that geometric perturbation changes this is reasonable but entirely speculative — zero prior evidence supports it. The probability of Phase 1 yielding a null result (video guidance provides no benefit even under perturbation) is non-trivial, perhaps 40-60%. The proposal handles this gracefully with the two-phase structure, but doesn't adequately address what happens next.", "CALIBRATION TRANSFERABILITY REMAINS UNADDRESSED: AQC requires ~100 calibration trajectories per task to compute the SVD and select components. The proposal mentions cross-task transfer as an ablation but doesn't address whether the action-relevant subspace is stable across (a) different LIBERO tasks, (b) different perturbation types (camera vs. robot-init), or (c) different difficulty levels. If recalibration is needed per task × perturbation type, SCG's practical advantage over training-based methods (OA-WAM, CKT-WAM) is significantly reduced.", "FIELD TRAJECTORY CONCERN: Being-H0.7 (May 2026) achieves 99.2% on LIBERO and 82.1%/84.8% on LIBERO-Plus using latent world-action queries WITHOUT explicit video branches. This suggests the field is moving toward implicit world modeling where the video→action guidance signal SCG filters simply doesn't exist. SCG is architecturally specific to WAMs with explicit video branches — a shrinking target."]
Feedback: The proposal has improved substantially from Round 4 — the Fast-WAM correction, switch to UWM, and AQC contribution are genuine advances. The research question is well-framed. However, three structural issues must be resolved:

**1. FIX THE UWM BASELINE GAP (MOST URGENT):** UWM's ~79% on LIBERO is a pretraining-only number. The proposal must explicitly state (and ideally verify) that task-specific fine-tuning from the LIBERO-90 checkpoint achieves competitive performance (>90%). The UWM paper reports fine-tuning for 10K steps per task — run this first on 2-3 LIBERO tasks and report the fine-tuned success rate before committing to the full plan. If fine-tuned UWM achieves >92% on standard LIBERO, the baseline is acceptable. If it stays at ~79%, switch backbone or abandon this approach.

**2. ADD A PHASE-1-INDEPENDENT METHOD CONTRIBUTION:** The user needs a METHOD paper. Consider restructuring: instead of making Phase 2 contingent on Phase 1, propose SCG as a general framework for modality-selective guidance in multi-modal diffusion models, with UWM/WAM as the primary testbed. Even if uniform CFG shows marginal benefit, spectral filtering may still improve the guidance-quality-per-compute tradeoff (fewer effective guidance dimensions → faster convergence → fewer denoising steps). Frame the spectral compression angle as a secondary method contribution: SCG can identify which k of d guidance dimensions matter, enabling 'sparse guidance' that runs faster. This gives a method contribution (efficient selective guidance) independent of whether guidance improves robustness.

**3. ADDRESS UWM-ON-LIBERO-PLUS EARLY:** Before any SCG work, run UWM (fine-tuned) on LIBERO-Plus camera and robot-init perturbations at L1. This takes ~5-10h H100 and answers whether UWM is even competitive enough to serve as a meaningful testbed. If UWM fine-tuned achieves <60% on geometric perturbations, there's enough room for SCG to show improvement. If it achieves >80%, the room for improvement is small but any improvement would be impressive.

**4. STRENGTHEN NOVELTY ARGUMENT AGAINST CPC THEORY:** The CPC paper proves CFG implicitly amplifies 'positive CPCs' and suppresses 'negative CPCs.' Your counter-argument (heterogeneous video→action conditioning lacks well-separated covariance structures) is reasonable but hand-wavy. Sharpen it: (a) CPC analysis assumes class-conditional distributions with shared covariance structure — video→action conditioning has fundamentally different conditional and unconditional covariances because they represent different modalities, not different classes within one modality. (b) AQC selects components based on action-quality correlation, not variance — this is orthogonal to CPC's variance-based implicit selection and should capture different components. Make this argument explicitly in the paper.

**5. SCOPE ICG-ON-FAST-WAM AS EXTENSION, NOT CORE:** ICG on Fast-WAM is interesting but adds complexity and hasn't been validated for cross-modal robot control. Keep it as a single-paragraph extension experiment, not a core contribution. Focus the paper tightly on UWM + spectral filtering.


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
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "32f780dc-602c-4a6d-9830-9a03c766a6ce",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T19:45:45.109Z_

```json
{
  "parentUuid": "32f780dc-602c-4a6d-9830-9a03c766a6ce",
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
  "uuid": "1d26966f-b677-4a6d-927b-620f190fd1f3",
  "timestamp": "2026-05-10T19:45:45.109Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T19:45:45.109Z_

```json
{
  "parentUuid": "1d26966f-b677-4a6d-927b-620f190fd1f3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eb6c1d3d-2c7b-45c7-8639-ddd017ad67a1",
  "timestamp": "2026-05-10T19:45:45.109Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
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
  "leafUuid": "eb6c1d3d-2c7b-45c7-8639-ddd017ad67a1",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spectral cross-modal guidance WAM proposal",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Assistant

_source line 8 · 2026-05-10T19:45:55.179Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed review of a research idea for CoRL 2026. I need to independently verify the claims made in this proposal through web searches, then issue a verdict. Let me carefully analyze this proposal, which is now in round 6 of 10.

Let me identify the key claims I need to verify:

1. UWM's independent timestep mechanism and LIBERO-90 checkpoint availability
2. LIBERO-Plus benchmark and geometric perturbation results for various methods
3. The correction about Fast-WAM's CFG capabilities
4. OA-WAM, CKT-WAM, Being-H0.7 performance numbers


5. Recent work from ICLR 2025 and NeurIPS 2025 including ICG, DiffStateGrad, and CPC theory
6. Whether this approach offers genuine novelty compared to existing methods
7. Whether the computational requirements are realistic
8. CoRL 2026 submission timeline

I'll need to search for these systematically to validate the claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb6c1d3d-2c7b-45c7-8639-ddd017ad67a1",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "0abc6f56-245a-4b0d-9d72-c1871a57863d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 9 · 2026-05-10T19:45:55.180Z_

I'll systematically verify the key claims in this proposal. Let me start with parallel searches across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0abc6f56-245a-4b0d-9d72-c1871a57863d",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "add84b53-d10e-44e2-be21-064452b59865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 10 · 2026-05-10T19:46:01.726Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011wLid8dxuXkTr1ciThKWDB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify UWM backbone claims",
  "prompt": "I need to verify claims about the UWM (Unified World Models) paper for a research review. Search for:\n\n1. \"Unified World Models\" robot diffusion RSS 2025 — verify the paper exists, its venue, and its key claims about independent diffusion timesteps for video and action\n2. Check if UWM has a publicly released LIBERO-90 checkpoint (search GitHub \"WEIRDLabUW/unified-world-model\" or HuggingFace)\n3. What is UWM's actual performance on LIBERO? The proposal claims ~79% from pretraining. Does fine-tuning improve this significantly?\n4. Search for \"UWM independent timestep cross-modal CFG\" to verify that setting video timestep t_o'=T marginalizes video information\n\nUse WebSearch for each query. Report findings concisely — I need facts, not speculation. Under 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "add84b53-d10e-44e2-be21-064452b59865",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "6558677b-15f4-455d-8c6f-768f86fba55c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 11 · 2026-05-10T19:46:08.383Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0142zzJNhTirMt6Kv1zeM2gd`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify LIBERO-Plus and robustness baselines",
  "prompt": "I need to verify claims about LIBERO-Plus benchmark and WAM robustness baselines for a research review. Search for:\n\n1. \"LIBERO-Plus robustness benchmark\" — verify it exists with 7 perturbation dimensions and difficulty levels L1-L5\n2. \"OA-WAM object addressable world action model\" 2026 — verify it exists and its claimed LIBERO-Plus Geo-Avg of 84.3% (Camera 80.5%, Robot 89.6%)\n3. \"CKT-WAM context knowledge transfer\" 2026 — verify it exists and its claimed LIBERO-Plus total of 86.1% (Camera 77.4%, Robot 71.4%)\n4. \"Being-H0.7 latent world action model\" 2026 — verify it exists with claimed 99.2% on standard LIBERO and 82.1%/84.8% on LIBERO-Plus\n5. \"Do World Action Models Generalize Better\" robustness study 2026 — verify this paper exists\n\nAlso search: \"LIBERO-Plus geometric perturbation SOTA 2026\" to find any methods the proposal might have missed.\n\nUse WebSearch for each query. Report facts with sources. Under 400 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6558677b-15f4-455d-8c6f-768f86fba55c",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "edf9eeae-c7f0-4b17-a05e-1c65757ad60a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 12 · 2026-05-10T19:46:15.084Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HDqSnTtopXSPV6SMGLFxtr`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ICG and DiffStateGrad papers",
  "prompt": "I need to verify two key papers cited in a research proposal:\n\n1. \"No Training No Problem Rethinking Classifier-Free Guidance\" ICLR 2025 — also known as Independent Condition Guidance (ICG). Verify it exists, was published at ICLR 2025, and that it enables CFG on any pretrained conditional model without dropout training by using random/independent conditions.\n\n2. \"Diffusion State-Guided Projected Gradient\" or \"DiffStateGrad\" ICLR 2025 — verify it exists, was published at ICLR 2025, and that it uses SVD-based subspace projection for filtering diffusion guidance signals in image restoration.\n\n3. \"Towards Understanding Mechanisms Classifier-Free Guidance\" CPC theory NeurIPS 2025 — verify this paper about contrastive principal components decomposition of CFG exists and was published at NeurIPS 2025.\n\n4. Search for \"β-CFG adaptive scaling classifier-free guidance\" 2025 — verify timestep-adaptive guidance scheduling exists.\n\nUse WebSearch for each. Report exact findings. Under 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf9eeae-c7f0-4b17-a05e-1c65757ad60a",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "27e0f265-2529-4f1f-a764-84321e3a1031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 13 · 2026-05-10T19:46:23.700Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015SRxnyhATtcpoYfitA5nXa`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing/missing work",
  "prompt": "I'm reviewing a research proposal about \"Spectral Cross-Modal Guidance\" — a training-free method that uses SVD-based spectral filtering on video→action guidance signals in World-Action Models (WAMs) to improve robustness under geometric perturbations. I need to find competing work the proposal may have missed.\n\nSearch for:\n\n1. \"test-time adaptation diffusion policy robustness\" 2025 2026 — any inference-time methods for improving robot policy robustness\n2. \"spectral filtering diffusion guidance robot\" 2025 2026 — any spectral/SVD methods applied to robot action diffusion\n3. \"cross-modal guidance robot manipulation\" 2025 2026 — any cross-modal guidance methods for robot control\n4. \"world model robustness geometric perturbation robot\" 2026 — any other methods addressing WAM geometric robustness\n5. \"inference-time guidance robot policy\" 2025 2026 — training-free methods for improving robot policies\n6. \"SVD diffusion model guidance\" 2025 2026 — SVD-based methods in diffusion model guidance beyond DiffStateGrad\n7. \"ADPro adaptive diffusion policy test-time\" — verify this paper exists and check its relevance\n8. \"TTPL test-time perturbation learning VLA\" 2026 — verify this exists\n\nReport all findings with paper titles, venues, and brief descriptions. Under 500 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27e0f265-2529-4f1f-a764-84321e3a1031",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "2be53511-3694-43f8-92a9-b4b49760f60e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 14 · 2026-05-10T19:46:29.773Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015RggHvVUAa11sdMeGKig6M`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify CoRL 2026 deadline and Fast-WAM claims",
  "prompt": "I need to verify several factual claims:\n\n1. Search \"CoRL 2026 deadline submission\" — verify that CoRL 2026 is in Austin, Nov 9-12, with abstract deadline May 26 and paper deadline May 29, 2026.\n\n2. Search \"Fast-WAM world action model inference video\" arxiv 2025 2026 — verify Fast-WAM exists, its key claims about video being dispensable at inference, and specifically check: does Fast-WAM use classifier-free guidance? What does \"CFG scale 1.0\" mean in their context? Was it trained with video feature dropout?\n\n3. Search \"Fast-WAM github checkpoint LIBERO\" — check if Fast-WAM has released code and LIBERO checkpoints.\n\n4. Search for \"GigaWorld-Policy\" and \"MotuBrain\" WAM 2026 — verify these exist and their claims about video features at inference.\n\nReport exact findings. Under 400 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be53511-3694-43f8-92a9-b4b49760f60e",
  "isSidechain": false,
  "requestId": "req_011CauTph4aUvKvBNApTRm9i",
  "type": "assistant",
  "uuid": "4c681576-d298-4c26-8f5b-89193ec2f9d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9upAAJDx69hdaYz8GgUto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22131,
      "cache_read_input_tokens": 11804,
      "output_tokens": 2026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2026,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 22131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22131
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

_source line 15 · 2026-05-10T19:47:15.908Z_

<details><summary>↩ Tool result · `toolu_01HDqSnTtopXSPV6SMGLFxtr`</summary>

```text
Here are the findings for all four papers:

**1. "No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models" -- VERIFIED.** Published at ICLR 2025 (conference paper). Introduces Independent Condition Guidance (ICG), which enables CFG benefits on any pretrained conditional diffusion model without dropout/null-condition training. Uses random independent conditions instead of unconditional scores. Also proposes Timestep Guidance (TSG) for unconditional models. Claims are accurate.

**2. "Diffusion State-Guided Projected Gradient for Inverse Problems" (DiffStateGrad) -- VERIFIED.** Published at ICLR 2025 (conference paper). Uses SVD on intermediate diffusion states to define a low-rank subspace, then projects measurement guidance gradients onto it to filter artifact-inducing components. Applied to linear and nonlinear image restoration. By Zirvi, Tolooshams, and Anandkumar (Anima-Lab). Claims are accurate.

**3. "Towards Understanding the Mechanisms of Classifier-Free Guidance" -- VERIFIED with corrections.** Published at NeurIPS 2025 as a **spotlight** paper (arXiv: 2505.19210). Decomposes CFG into three components: (i) mean-shift toward class mean, (ii) positive Contrastive Principal Components (CPC) enhancing class-specific features, (iii) negative CPC suppressing generic features. The CPC theory claim is accurate. Note: the title is "Towards Understanding the **Mechanisms** of Classifier-Free Guidance" (not "Mechanisms of").

**4. beta-CFG ("Classifier-free Guidance with Adaptive Scaling") -- PARTIALLY VERIFIED.** The paper exists (arXiv: 2502.10574, Feb 2025) and proposes timestep-adaptive guidance scheduling using beta-distribution curves. However, it appears to remain an **arXiv preprint only** -- no evidence of acceptance at a peer-reviewed venue as of May 2026.

Sources:
- [ICLR 2025 Poster - No Training, No Problem](https://iclr.cc/virtual/2025/poster/29126)
- [ICLR 2025 Proceedings - No Training, No Problem (PDF)](https://proceedings.iclr.cc/paper_files/paper/2025/file/8bead340bb510de5c8356f60ca039efc-Paper-Conference.pdf)
- [DiffStateGrad GitHub (Anima-Lab)](https://github.com/Anima-Lab/DiffStateGrad)
- [ICLR 2025 Proceedings - DiffStateGrad](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4d5b7f7a0603b75e39ffebbf95e3b7ee-Abstract-Conference.html)
- [NeurIPS 2025 Poster - Towards Understanding Mechanisms of CFG](https://neurips.cc/virtual/2025/poster/117182)
- [arXiv 2505.19210 - Towards Understanding Mechanisms of CFG](https://arxiv.org/abs/2505.19210)
- [arXiv 2502.10574 - beta-CFG](https://arxiv.org/abs/2502.10574)
- [beta-CFG GitHub](https://github.com/gmum/beta-CFG)

agentId: a63e0bcfb0ad64b5c (use SendMessage with to: 'a63e0bcfb0ad64b5c' to continue this agent)
&lt;usage>total_tokens: 17523
tool_uses: 8
duration_ms: 60820&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27e0f265-2529-4f1f-a764-84321e3a1031",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "515c74eb-07cb-4ee7-b01a-e967616291e6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two key papers cited in a research proposal:\n\n1. \"No Training No Problem Rethinking Classifier-Free Guidance\" ICLR 2025 — also known as Independent Condition Guidance (ICG). Verify it exists, was published at ICLR 2025, and that it enables CFG on any pretrained conditional model without dropout training by using random/independent conditions.\n\n2. \"Diffusion State-Guided Projected Gradient\" or \"DiffStateGrad\" ICLR 2025 — verify it exists, was published at ICLR 2025, and that it uses SVD-based subspace projection for filtering diffusion guidance signals in image restoration.\n\n3. \"Towards Understanding Mechanisms Classifier-Free Guidance\" CPC theory NeurIPS 2025 — verify this paper about contrastive principal components decomposition of CFG exists and was published at NeurIPS 2025.\n\n4. Search for \"β-CFG adaptive scaling classifier-free guidance\" 2025 — verify timestep-adaptive guidance scheduling exists.\n\nUse WebSearch for each. Report exact findings. Under 300 words.",
    "agentId": "a63e0bcfb0ad64b5c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for all four papers:\n\n**1. \"No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models\" -- VERIFIED.** Published at ICLR 2025 (conference paper). Introduces Independent Condition Guidance (ICG), which enables CFG benefits on any pretrained conditional diffusion model without dropout/null-condition training. Uses random independent conditions instead of unconditional scores. Also proposes Timestep Guidance (TSG) for unconditional models. Claims are accurate.\n\n**2. \"Diffusion State-Guided Projected Gradient for Inverse Problems\" (DiffStateGrad) -- VERIFIED.** Published at ICLR 2025 (conference paper). Uses SVD on intermediate diffusion states to define a low-rank subspace, then projects measurement guidance gradients onto it to filter artifact-inducing components. Applied to linear and nonlinear image restoration. By Zirvi, Tolooshams, and Anandkumar (Anima-Lab). Claims are accurate.\n\n**3. \"Towards Understanding the Mechanisms of Classifier-Free Guidance\" -- VERIFIED with corrections.** Published at NeurIPS 2025 as a **spotlight** paper (arXiv: 2505.19210). Decomposes CFG into three components: (i) mean-shift toward class mean, (ii) positive Contrastive Principal Components (CPC) enhancing class-specific features, (iii) negative CPC suppressing generic features. The CPC theory claim is accurate. Note: the title is \"Towards Understanding the **Mechanisms** of Classifier-Free Guidance\" (not \"Mechanisms of\").\n\n**4. beta-CFG (\"Classifier-free Guidance with Adaptive Scaling\") -- PARTIALLY VERIFIED.** The paper exists (arXiv: 2502.10574, Feb 2025) and proposes timestep-adaptive guidance scheduling using beta-distribution curves. However, it appears to remain an **arXiv preprint only** -- no evidence of acceptance at a peer-reviewed venue as of May 2026.\n\nSources:\n- [ICLR 2025 Poster - No Training, No Problem](https://iclr.cc/virtual/2025/poster/29126)\n- [ICLR 2025 Proceedings - No Training, No Problem (PDF)](https://proceedings.iclr.cc/paper_files/paper/2025/file/8bead340bb510de5c8356f60ca039efc-Paper-Conference.pdf)\n- [DiffStateGrad GitHub (Anima-Lab)](https://github.com/Anima-Lab/DiffStateGrad)\n- [ICLR 2025 Proceedings - DiffStateGrad](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4d5b7f7a0603b75e39ffebbf95e3b7ee-Abstract-Conference.html)\n- [NeurIPS 2025 Poster - Towards Understanding Mechanisms of CFG](https://neurips.cc/virtual/2025/poster/117182)\n- [arXiv 2505.19210 - Towards Understanding Mechanisms of CFG](https://arxiv.org/abs/2505.19210)\n- [arXiv 2502.10574 - beta-CFG](https://arxiv.org/abs/2502.10574)\n- [beta-CFG GitHub](https://github.com/gmum/beta-CFG)"
      }
    ],
    "totalDurationMs": 60820,
    "totalTokens": 17523,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1674,
      "cache_read_input_tokens": 15016,
      "output_tokens": 832,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1674
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 832,
          "cache_read_input_tokens": 15016,
          "cache_creation_input_tokens": 1674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1674,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "27e0f265-2529-4f1f-a764-84321e3a1031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:47:17.730Z_

<details><summary>↩ Tool result · `toolu_0142zzJNhTirMt6Kv1zeM2gd`</summary>

```text
Here are the verification results for each claim:

**1. LIBERO-Plus Benchmark** -- VERIFIED. It exists with 7 perturbation dimensions (objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise) and difficulty levels L1-L5. It contains 10,030 tasks across 21 sub-dimensions. Published as arXiv:2510.13626.

**2. OA-WAM** -- PARTIALLY VERIFIED. The paper exists (arXiv:2605.06481) and describes an object-addressable WAM with a 7B trunk. However, the claimed Geo-Avg of 84.3% (Camera 80.5%, Robot 89.6%) could NOT be confirmed. Search results instead report a Geo-Avg of **76.0** and Camera of **85.7%**. The specific numbers 84.3/80.5/89.6 were not found in any source. These figures may be fabricated or from a different table/setting -- requires checking the paper directly.

**3. CKT-WAM** -- PARTIALLY VERIFIED. The paper exists (arXiv:2605.06247), titled "Parameter-Efficient Context Knowledge Transfer Between World Action Models." The **86.1% total LIBERO-Plus success rate** is confirmed. However, the specific Camera 77.4% and Robot 71.4% breakdown could not be independently confirmed from search results -- these would need to be checked against the paper's tables.

**4. Being-H0.7** -- VERIFIED. The paper exists (arXiv:2605.00078). The **99.2% on standard LIBERO** is confirmed. The **82.1% zero-shot on LIBERO-Plus** and **84.8% after fine-tuning** are both confirmed by the paper.

**5. "Do World Action Models Generalize Better than VLAs? A Robustness Study"** -- VERIFIED. The paper exists (arXiv:2603.22078). It compares VLAs and WAMs on LIBERO-Plus and RoboTwin 2.0-Plus. Key finding: WAMs show strong robustness to noise/lighting/layout but struggle with camera viewpoint and robot initial state changes.

**6. Additional SOTA methods possibly missed**: Cosmos-Policy achieved 82.2% on LIBERO-Plus per the robustness study. LingBot-VA (RSS 2026 causal video-action world model) and Fast-WAM (arXiv:2603.16666) are other relevant WAM methods. MolmoAct2 and MotuBrain also appear as recent entrants.

**FLAG**: The OA-WAM numbers (Geo-Avg 84.3, Camera 80.5, Robot 89.6) are suspicious. The only Geo-Avg found in search results is 76.0, and the camera score reported is 85.7 -- neither matches the claimed figures. Recommend verifying these directly from the paper's tables before citing.

Sources:
- [LIBERO-Plus (arXiv:2510.13626)](https://arxiv.org/abs/2510.13626)
- [OA-WAM (arXiv:2605.06481)](https://arxiv.org/html/2605.06481v1)
- [CKT-WAM (arXiv:2605.06247)](https://arxiv.org/html/2605.06247v1)
- [Being-H0.7 (arXiv:2605.00078)](https://arxiv.org/html/2605.00078v1)
- [Do WAMs Generalize Better (arXiv:2603.22078)](https://arxiv.org/abs/2603.22078)
- [Fast-WAM (arXiv:2603.16666)](https://arxiv.org/abs/2603.16666)
- [Being-H0.7 project page](https://research.beingbeyond.com/being-h07)

agentId: a8637628f5c274561 (use SendMessage with to: 'a8637628f5c274561' to continue this agent)
&lt;usage>total_tokens: 21500
tool_uses: 12
duration_ms: 69344&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edf9eeae-c7f0-4b17-a05e-1c65757ad60a",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "ad76d353-8169-499f-abc9-aba51b980153",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify claims about LIBERO-Plus benchmark and WAM robustness baselines for a research review. Search for:\n\n1. \"LIBERO-Plus robustness benchmark\" — verify it exists with 7 perturbation dimensions and difficulty levels L1-L5\n2. \"OA-WAM object addressable world action model\" 2026 — verify it exists and its claimed LIBERO-Plus Geo-Avg of 84.3% (Camera 80.5%, Robot 89.6%)\n3. \"CKT-WAM context knowledge transfer\" 2026 — verify it exists and its claimed LIBERO-Plus total of 86.1% (Camera 77.4%, Robot 71.4%)\n4. \"Being-H0.7 latent world action model\" 2026 — verify it exists with claimed 99.2% on standard LIBERO and 82.1%/84.8% on LIBERO-Plus\n5. \"Do World Action Models Generalize Better\" robustness study 2026 — verify this paper exists\n\nAlso search: \"LIBERO-Plus geometric perturbation SOTA 2026\" to find any methods the proposal might have missed.\n\nUse WebSearch for each query. Report facts with sources. Under 400 words.",
    "agentId": "a8637628f5c274561",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verification results for each claim:\n\n**1. LIBERO-Plus Benchmark** -- VERIFIED. It exists with 7 perturbation dimensions (objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise) and difficulty levels L1-L5. It contains 10,030 tasks across 21 sub-dimensions. Published as arXiv:2510.13626.\n\n**2. OA-WAM** -- PARTIALLY VERIFIED. The paper exists (arXiv:2605.06481) and describes an object-addressable WAM with a 7B trunk. However, the claimed Geo-Avg of 84.3% (Camera 80.5%, Robot 89.6%) could NOT be confirmed. Search results instead report a Geo-Avg of **76.0** and Camera of **85.7%**. The specific numbers 84.3/80.5/89.6 were not found in any source. These figures may be fabricated or from a different table/setting -- requires checking the paper directly.\n\n**3. CKT-WAM** -- PARTIALLY VERIFIED. The paper exists (arXiv:2605.06247), titled \"Parameter-Efficient Context Knowledge Transfer Between World Action Models.\" The **86.1% total LIBERO-Plus success rate** is confirmed. However, the specific Camera 77.4% and Robot 71.4% breakdown could not be independently confirmed from search results -- these would need to be checked against the paper's tables.\n\n**4. Being-H0.7** -- VERIFIED. The paper exists (arXiv:2605.00078). The **99.2% on standard LIBERO** is confirmed. The **82.1% zero-shot on LIBERO-Plus** and **84.8% after fine-tuning** are both confirmed by the paper.\n\n**5. \"Do World Action Models Generalize Better than VLAs? A Robustness Study\"** -- VERIFIED. The paper exists (arXiv:2603.22078). It compares VLAs and WAMs on LIBERO-Plus and RoboTwin 2.0-Plus. Key finding: WAMs show strong robustness to noise/lighting/layout but struggle with camera viewpoint and robot initial state changes.\n\n**6. Additional SOTA methods possibly missed**: Cosmos-Policy achieved 82.2% on LIBERO-Plus per the robustness study. LingBot-VA (RSS 2026 causal video-action world model) and Fast-WAM (arXiv:2603.16666) are other relevant WAM methods. MolmoAct2 and MotuBrain also appear as recent entrants.\n\n**FLAG**: The OA-WAM numbers (Geo-Avg 84.3, Camera 80.5, Robot 89.6) are suspicious. The only Geo-Avg found in search results is 76.0, and the camera score reported is 85.7 -- neither matches the claimed figures. Recommend verifying these directly from the paper's tables before citing.\n\nSources:\n- [LIBERO-Plus (arXiv:2510.13626)](https://arxiv.org/abs/2510.13626)\n- [OA-WAM (arXiv:2605.06481)](https://arxiv.org/html/2605.06481v1)\n- [CKT-WAM (arXiv:2605.06247)](https://arxiv.org/html/2605.06247v1)\n- [Being-H0.7 (arXiv:2605.00078)](https://arxiv.org/html/2605.00078v1)\n- [Do WAMs Generalize Better (arXiv:2603.22078)](https://arxiv.org/abs/2603.22078)\n- [Fast-WAM (arXiv:2603.16666)](https://arxiv.org/abs/2603.16666)\n- [Being-H0.7 project page](https://research.beingbeyond.com/being-h07)"
      }
    ],
    "totalDurationMs": 69344,
    "totalTokens": 21500,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 18926,
      "output_tokens": 958,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 958,
          "cache_read_input_tokens": 18926,
          "cache_creation_input_tokens": 1615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1615,
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
  "sourceToolAssistantUUID": "edf9eeae-c7f0-4b17-a05e-1c65757ad60a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:47:22.255Z_

<details><summary>↩ Tool result · `toolu_011wLid8dxuXkTr1ciThKWDB`</summary>

```text
Here are the verified findings:

**1. Paper existence and venue:** Confirmed. "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets" (arXiv 2504.02792) by Zhu, Yu et al. from UW WEIRD Lab / Toyota Research Institute. Published at **RSS 2025** (Robotics: Science and Systems). The core claim about independent diffusion timesteps for video and action modalities is accurate -- UWM uses a unified diffusion transformer with separately sampled timesteps per modality.

**2. Public LIBERO-90 checkpoint:** Confirmed. The [GitHub repo](https://github.com/WEIRDLabUW/unified-world-model) exists and explicitly provides a pretrained LIBERO-90 checkpoint for download and fine-tuning. Scripts for DROID pretraining/cotraining/finetuning are also included.

**3. LIBERO performance:** The ~79% claim is accurate but requires context. Table II reports UWM's average success rate as **0.79 +/- 0.11** across 5 evaluation tasks **after fine-tuning** (pretrained on LIBERO-90, then fine-tuned 10K steps on downstream tasks). This is NOT a zero-shot/pretrain-only number -- it is a post-fine-tuning result. Individual task rates range from 0.65 (Mug-Mug) to 0.93 (Soup-Cheese). I could not find a separate zero-shot pretrain-only evaluation in the paper's tables.

**4. Timestep marginalization mechanism:** Confirmed. Setting the video diffusion timestep t_o' = T (fully noised) effectively marginalizes out the video modality, yielding a pure action policy p(a|o). Conversely, fixing the action timestep to 0 (clean actions) yields a forward dynamics model p(o'|o,a). This is the mechanism that enables cross-modal flexibility -- not traditional classifier-free guidance per se, but an analogous marginalization via timestep control during the shared denoising process.

**Key correction for your review:** The 79% figure is a fine-tuned result, not a pretraining-only/zero-shot number. If the proposal claims "~79% from pretraining," that is misleading.

Sources:
- [UWM Project Page](https://weirdlabuw.github.io/uwm/)
- [arXiv 2504.02792](https://arxiv.org/abs/2504.02792)
- [arXiv HTML v3](https://arxiv.org/html/2504.02792v3)
- [RSS 2025 Program](https://roboticsconference.org/program/papers/15/)
- [GitHub: WEIRDLabUW/unified-world-model](https://github.com/WEIRDLabUW/unified-world-model)
- [HuggingFace Paper Page](https://huggingface.co/papers/2504.02792)

agentId: ab37c89f27d8b8c68 (use SendMessage with to: 'ab37c89f27d8b8c68' to continue this agent)
&lt;usage>total_tokens: 19396
tool_uses: 11
duration_ms: 80524&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6558677b-15f4-455d-8c6f-768f86fba55c",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "7b5a3f52-ee21-43f7-943c-c6c13475a9d9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify claims about the UWM (Unified World Models) paper for a research review. Search for:\n\n1. \"Unified World Models\" robot diffusion RSS 2025 — verify the paper exists, its venue, and its key claims about independent diffusion timesteps for video and action\n2. Check if UWM has a publicly released LIBERO-90 checkpoint (search GitHub \"WEIRDLabUW/unified-world-model\" or HuggingFace)\n3. What is UWM's actual performance on LIBERO? The proposal claims ~79% from pretraining. Does fine-tuning improve this significantly?\n4. Search for \"UWM independent timestep cross-modal CFG\" to verify that setting video timestep t_o'=T marginalizes video information\n\nUse WebSearch for each query. Report findings concisely — I need facts, not speculation. Under 300 words.",
    "agentId": "ab37c89f27d8b8c68",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified findings:\n\n**1. Paper existence and venue:** Confirmed. \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets\" (arXiv 2504.02792) by Zhu, Yu et al. from UW WEIRD Lab / Toyota Research Institute. Published at **RSS 2025** (Robotics: Science and Systems). The core claim about independent diffusion timesteps for video and action modalities is accurate -- UWM uses a unified diffusion transformer with separately sampled timesteps per modality.\n\n**2. Public LIBERO-90 checkpoint:** Confirmed. The [GitHub repo](https://github.com/WEIRDLabUW/unified-world-model) exists and explicitly provides a pretrained LIBERO-90 checkpoint for download and fine-tuning. Scripts for DROID pretraining/cotraining/finetuning are also included.\n\n**3. LIBERO performance:** The ~79% claim is accurate but requires context. Table II reports UWM's average success rate as **0.79 +/- 0.11** across 5 evaluation tasks **after fine-tuning** (pretrained on LIBERO-90, then fine-tuned 10K steps on downstream tasks). This is NOT a zero-shot/pretrain-only number -- it is a post-fine-tuning result. Individual task rates range from 0.65 (Mug-Mug) to 0.93 (Soup-Cheese). I could not find a separate zero-shot pretrain-only evaluation in the paper's tables.\n\n**4. Timestep marginalization mechanism:** Confirmed. Setting the video diffusion timestep t_o' = T (fully noised) effectively marginalizes out the video modality, yielding a pure action policy p(a|o). Conversely, fixing the action timestep to 0 (clean actions) yields a forward dynamics model p(o'|o,a). This is the mechanism that enables cross-modal flexibility -- not traditional classifier-free guidance per se, but an analogous marginalization via timestep control during the shared denoising process.\n\n**Key correction for your review:** The 79% figure is a fine-tuned result, not a pretraining-only/zero-shot number. If the proposal claims \"~79% from pretraining,\" that is misleading.\n\nSources:\n- [UWM Project Page](https://weirdlabuw.github.io/uwm/)\n- [arXiv 2504.02792](https://arxiv.org/abs/2504.02792)\n- [arXiv HTML v3](https://arxiv.org/html/2504.02792v3)\n- [RSS 2025 Program](https://roboticsconference.org/program/papers/15/)\n- [GitHub: WEIRDLabUW/unified-world-model](https://github.com/WEIRDLabUW/unified-world-model)\n- [HuggingFace Paper Page](https://huggingface.co/papers/2504.02792)"
      }
    ],
    "totalDurationMs": 80524,
    "totalTokens": 19396,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 18129,
      "output_tokens": 727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 727,
          "cache_read_input_tokens": 18129,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 539,
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
  "sourceToolAssistantUUID": "6558677b-15f4-455d-8c6f-768f86fba55c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7b5a3f52-ee21-43f7-943c-c6c13475a9d9",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spectral cross-modal guidance WAM proposal",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Tool result

_source line 20 · 2026-05-10T19:47:45.188Z_

<details><summary>↩ Tool result · `toolu_015SRxnyhATtcpoYfitA5nXa`</summary>

```text
Here are the findings from all eight searches:

---

## Competing Work Report

### 1. Test-Time Adaptive Diffusion Policies

- **ADPro** (arXiv 2508.06266) -- Confirmed to exist. A test-time adaptive diffusion policy using manifold-constrained denoising and task-aware initialization. Training-free; improves success rates by up to 9 percentage points over diffusion baselines on RLBench, CALVIN, and real-world tasks. **Directly competing**: it is a training-free, inference-time method for improving diffusion policy robustness.

- **Compose Your Policies (GPC)** (arXiv 2510.01068) -- A training-free method that composes multiple pre-trained diffusion/flow policies at test time via distributional score combination and test-time search. Validated on Robomimic, PushT, RoboTwin, and real robots.

### 2. TTPL / PDF for VLAs

- **PDF: Perturbation Learning with Delayed Feedback** (arXiv 2604.18107, April 2026) -- Confirmed to exist (the paper the proposal likely refers to as "TTPL"). A verifier-free test-time adaptation framework for VLAs that uses uncertainty-based data augmentation, action voting, and a lightweight perturbation module. Achieves +7.4% success on LIBERO. **Directly relevant** as a competing test-time robustness method for embodied policies.

### 3. World Model Robustness Under Geometric Perturbations

- **OA-WAM: Object-Addressable World Action Model** (arXiv 2605.06481, May 2026) -- Organizes WAMs as addressable object states to improve robustness under geometric scene rearrangements. **Highly relevant**: directly targets WAM geometric robustness.

- **Mask World Model (MWM)** (arXiv 2604.19683, April 2026) -- Predicts semantic mask evolution instead of pixels via video diffusion, imposing a geometric information bottleneck. Filters visual noise while preserving physical dynamics.

- **"Do WAMs Generalize Better than VLAs?"** (arXiv 2603.22078, March 2026) -- A robustness study showing WAMs inherit spatiotemporal priors from world model backbones, giving them strong robustness to noise, lighting, and layout perturbations. **Must-cite** for any WAM robustness proposal.

- **Dream Diffusion Policy (DDP) / "Dreaming the Unseen"** (arXiv 2603.21017, March 2026) -- Integrates a diffusion world model into the policy via a shared 3D encoder. When OOD perturbations occur, the policy detects discrepancies and falls back to imagined latent dynamics. Addresses geometric robustness but requires training.

### 4. Inference-Time World-Model Guidance

- **Inference-Time Enhancement via Predictive World Modeling** (arXiv 2502.00622) -- Augments a frozen diffusion policy at deployment with a predictive world model, providing inference-time guidance without retraining. **Directly competing** with the "Spectral Cross-Modal Guidance" concept.

- **WARPD** (arXiv 2410.14040, ICLR 2026) -- Generates closed-loop policy weights via diffusion in parameter space, using a co-trained world model. Achieves robustness under perturbations with 1/45th inference FLOPs.

### 5. SVD/Spectral Methods in Diffusion Guidance

- **DiffStateGrad** (ICLR 2025) -- Uses SVD on intermediate diffusion states to project measurement gradients onto a low-rank subspace. Designed for image inverse problems, not robotics, but the core SVD-on-diffusion-state technique is closely related. The proposal should clarify differentiation.

- **Spectral Regularization for Diffusion Models** (arXiv 2603.02447, March 2026) -- Applies wavelet-domain spectral regularization to diffusion training losses. Not robotics-specific but relevant to the spectral filtering methodology.

### 6. No Direct Match Found

No paper combining SVD-based spectral filtering specifically with video-to-action cross-modal guidance in WAMs was found, suggesting the proposal's core contribution may be novel. However, the papers above collectively cover each component (SVD in diffusion guidance, inference-time WAM robustness, geometric perturbation handling), so the proposal should cite and differentiate from all of them.

**Key gaps in the proposal**: The WAM robustness study (arXiv 2603.22078), OA-WAM, DDP, and the inference-time world-model enhancement paper (arXiv 2502.00622) are the most critical potential omissions.

Sources:
- [ADPro](https://arxiv.org/abs/2508.06266)
- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)
- [PDF: Perturbation Learning with Delayed Feedback](https://arxiv.org/abs/2604.18107)
- [OA-WAM](https://arxiv.org/html/2605.06481v1)
- [Mask World Model](https://arxiv.org/html/2604.19683)
- [Do WAMs Generalize Better than VLAs?](https://arxiv.org/html/2603.22078v1)
- [Dream Diffusion Policy (DDP)](https://arxiv.org/html/2603.21017v1)
- [Inference-Time Enhancement via Predictive World Modeling](https://arxiv.org/abs/2502.00622)
- [WARPD](https://arxiv.org/abs/2410.14040)
- [DiffStateGrad](https://arxiv.org/abs/2410.03463)
- [Spectral Regularization for Diffusion Models](https://arxiv.org/html/2603.02447v1)

agentId: ac57742c17df894bb (use SendMessage with to: 'ac57742c17df894bb' to continue this agent)
&lt;usage>total_tokens: 22971
tool_uses: 12
duration_ms: 81481&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2be53511-3694-43f8-92a9-b4b49760f60e",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "606cb421-863f-4b08-9ce7-01ab2f0b8834",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal about \"Spectral Cross-Modal Guidance\" — a training-free method that uses SVD-based spectral filtering on video→action guidance signals in World-Action Models (WAMs) to improve robustness under geometric perturbations. I need to find competing work the proposal may have missed.\n\nSearch for:\n\n1. \"test-time adaptation diffusion policy robustness\" 2025 2026 — any inference-time methods for improving robot policy robustness\n2. \"spectral filtering diffusion guidance robot\" 2025 2026 — any spectral/SVD methods applied to robot action diffusion\n3. \"cross-modal guidance robot manipulation\" 2025 2026 — any cross-modal guidance methods for robot control\n4. \"world model robustness geometric perturbation robot\" 2026 — any other methods addressing WAM geometric robustness\n5. \"inference-time guidance robot policy\" 2025 2026 — training-free methods for improving robot policies\n6. \"SVD diffusion model guidance\" 2025 2026 — SVD-based methods in diffusion model guidance beyond DiffStateGrad\n7. \"ADPro adaptive diffusion policy test-time\" — verify this paper exists and check its relevance\n8. \"TTPL test-time perturbation learning VLA\" 2026 — verify this exists\n\nReport all findings with paper titles, venues, and brief descriptions. Under 500 words.",
    "agentId": "ac57742c17df894bb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings from all eight searches:\n\n---\n\n## Competing Work Report\n\n### 1. Test-Time Adaptive Diffusion Policies\n\n- **ADPro** (arXiv 2508.06266) -- Confirmed to exist. A test-time adaptive diffusion policy using manifold-constrained denoising and task-aware initialization. Training-free; improves success rates by up to 9 percentage points over diffusion baselines on RLBench, CALVIN, and real-world tasks. **Directly competing**: it is a training-free, inference-time method for improving diffusion policy robustness.\n\n- **Compose Your Policies (GPC)** (arXiv 2510.01068) -- A training-free method that composes multiple pre-trained diffusion/flow policies at test time via distributional score combination and test-time search. Validated on Robomimic, PushT, RoboTwin, and real robots.\n\n### 2. TTPL / PDF for VLAs\n\n- **PDF: Perturbation Learning with Delayed Feedback** (arXiv 2604.18107, April 2026) -- Confirmed to exist (the paper the proposal likely refers to as \"TTPL\"). A verifier-free test-time adaptation framework for VLAs that uses uncertainty-based data augmentation, action voting, and a lightweight perturbation module. Achieves +7.4% success on LIBERO. **Directly relevant** as a competing test-time robustness method for embodied policies.\n\n### 3. World Model Robustness Under Geometric Perturbations\n\n- **OA-WAM: Object-Addressable World Action Model** (arXiv 2605.06481, May 2026) -- Organizes WAMs as addressable object states to improve robustness under geometric scene rearrangements. **Highly relevant**: directly targets WAM geometric robustness.\n\n- **Mask World Model (MWM)** (arXiv 2604.19683, April 2026) -- Predicts semantic mask evolution instead of pixels via video diffusion, imposing a geometric information bottleneck. Filters visual noise while preserving physical dynamics.\n\n- **\"Do WAMs Generalize Better than VLAs?\"** (arXiv 2603.22078, March 2026) -- A robustness study showing WAMs inherit spatiotemporal priors from world model backbones, giving them strong robustness to noise, lighting, and layout perturbations. **Must-cite** for any WAM robustness proposal.\n\n- **Dream Diffusion Policy (DDP) / \"Dreaming the Unseen\"** (arXiv 2603.21017, March 2026) -- Integrates a diffusion world model into the policy via a shared 3D encoder. When OOD perturbations occur, the policy detects discrepancies and falls back to imagined latent dynamics. Addresses geometric robustness but requires training.\n\n### 4. Inference-Time World-Model Guidance\n\n- **Inference-Time Enhancement via Predictive World Modeling** (arXiv 2502.00622) -- Augments a frozen diffusion policy at deployment with a predictive world model, providing inference-time guidance without retraining. **Directly competing** with the \"Spectral Cross-Modal Guidance\" concept.\n\n- **WARPD** (arXiv 2410.14040, ICLR 2026) -- Generates closed-loop policy weights via diffusion in parameter space, using a co-trained world model. Achieves robustness under perturbations with 1/45th inference FLOPs.\n\n### 5. SVD/Spectral Methods in Diffusion Guidance\n\n- **DiffStateGrad** (ICLR 2025) -- Uses SVD on intermediate diffusion states to project measurement gradients onto a low-rank subspace. Designed for image inverse problems, not robotics, but the core SVD-on-diffusion-state technique is closely related. The proposal should clarify differentiation.\n\n- **Spectral Regularization for Diffusion Models** (arXiv 2603.02447, March 2026) -- Applies wavelet-domain spectral regularization to diffusion training losses. Not robotics-specific but relevant to the spectral filtering methodology.\n\n### 6. No Direct Match Found\n\nNo paper combining SVD-based spectral filtering specifically with video-to-action cross-modal guidance in WAMs was found, suggesting the proposal's core contribution may be novel. However, the papers above collectively cover each component (SVD in diffusion guidance, inference-time WAM robustness, geometric perturbation handling), so the proposal should cite and differentiate from all of them.\n\n**Key gaps in the proposal**: The WAM robustness study (arXiv 2603.22078), OA-WAM, DDP, and the inference-time world-model enhancement paper (arXiv 2502.00622) are the most critical potential omissions.\n\nSources:\n- [ADPro](https://arxiv.org/abs/2508.06266)\n- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)\n- [PDF: Perturbation Learning with Delayed Feedback](https://arxiv.org/abs/2604.18107)\n- [OA-WAM](https://arxiv.org/html/2605.06481v1)\n- [Mask World Model](https://arxiv.org/html/2604.19683)\n- [Do WAMs Generalize Better than VLAs?](https://arxiv.org/html/2603.22078v1)\n- [Dream Diffusion Policy (DDP)](https://arxiv.org/html/2603.21017v1)\n- [Inference-Time Enhancement via Predictive World Modeling](https://arxiv.org/abs/2502.00622)\n- [WARPD](https://arxiv.org/abs/2410.14040)\n- [DiffStateGrad](https://arxiv.org/abs/2410.03463)\n- [Spectral Regularization for Diffusion Models](https://arxiv.org/html/2603.02447v1)"
      }
    ],
    "totalDurationMs": 81481,
    "totalTokens": 22971,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2837,
      "cache_read_input_tokens": 18668,
      "output_tokens": 1465,
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
          "input_tokens": 1,
          "output_tokens": 1465,
          "cache_read_input_tokens": 18668,
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
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "2be53511-3694-43f8-92a9-b4b49760f60e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T19:48:35.302Z_

<details><summary>↩ Tool result · `toolu_015RggHvVUAa11sdMeGKig6M`</summary>

```text
Now I have enough information to compile the findings. Here is my report:

---

**1. CoRL 2026 Deadlines**

Confirmed. CoRL 2026 is at JW Marriott Austin, TX, November 9--12. Abstract deadline: May 26, 2026 (11:59 UTC). Paper deadline: May 29, 2026 (11:59 UTC). All verified via the official [CoRL 2026 site](https://www.corl.org/) and [Call for Papers](https://www.corl.org/contributions/call-for-papers).

**2. Fast-WAM (arXiv 2603.16666)**

The paper exists. Title: "Fast-WAM: Do World Action Models Need Test-time Future Imagination?" by Tianyuan Yuan et al. (Tsinghua / Galaxea AI, March 2026). Key claim confirmed: video prediction is dispensable at inference; its value lies in improving representations during training. At inference, Fast-WAM uses 10 denoising steps with **CFG scale 1.0** -- meaning classifier-free guidance weight = 1.0, which effectively means **no guidance** (purely conditional prediction, no unconditional branch interpolation). The model does use classifier-free guidance infrastructure, but the scale of 1.0 nullifies its effect. Regarding video feature dropout: Fast-WAM does **not** use traditional feature dropout on video. Instead, it uses a **structured attention mask** -- future video tokens are present during training (for the video co-training objective) but completely removed at inference. The "uncond" in checkpoint names (e.g., `libero_uncond_2cam224.pt`) refers to the unconditional (no-video-generation) inference variant.

**3. Fast-WAM Code and Checkpoints**

Confirmed released. GitHub: [yuantianyuan01/FastWAM](https://github.com/yuantianyuan01/FastWAM). HuggingFace checkpoints at [yuanty/fastwam](https://huggingface.co/yuanty/fastwam), including `libero_uncond_2cam224.pt`. Preprocessed LIBERO datasets also available on HuggingFace.

**4. GigaWorld-Policy and MotuBrain**

Both exist. **GigaWorld-Policy** (arXiv 2603.17240) uses a causal design where future-video tokens cannot influence action tokens, making video generation optional at inference -- achieving 9x faster inference than the Motus baseline. Code at [open-gigaai/giga-world-policy](https://github.com/open-gigaai/giga-world-policy). **MotuBrain** (arXiv 2604.27792) by ShengShu Technology is a unified WAM supporting five modes (VLA, world model, video gen, IDM, joint prediction). It uses V2A-style asymmetric dependency enabling action-only inference without generating future video. Note: "MotuBrain" is the successor/rebrand of "Motus" (arXiv 2512.13030).

Sources:
- [CoRL 2026](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Fast-WAM arXiv](https://arxiv.org/abs/2603.16666)
- [Fast-WAM HTML](https://arxiv.org/html/2603.16666v1)
- [FastWAM GitHub](https://github.com/yuantianyuan01/FastWAM)
- [FastWAM HuggingFace](https://huggingface.co/yuanty/fastwam)
- [GigaWorld-Policy arXiv](https://arxiv.org/abs/2603.17240)
- [GigaWorld-Policy GitHub](https://github.com/open-gigaai/giga-world-policy)
- [MotuBrain arXiv](https://arxiv.org/html/2604.27792v2)
- [MotuBrain press release](https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html)

agentId: ae0907a2909503632 (use SendMessage with to: 'ae0907a2909503632' to continue this agent)
&lt;usage>total_tokens: 25592
tool_uses: 15
duration_ms: 125525&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c681576-d298-4c26-8f5b-89193ec2f9d7",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "2b2d3385-b3da-40d4-8ebb-3a3084acd891",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several factual claims:\n\n1. Search \"CoRL 2026 deadline submission\" — verify that CoRL 2026 is in Austin, Nov 9-12, with abstract deadline May 26 and paper deadline May 29, 2026.\n\n2. Search \"Fast-WAM world action model inference video\" arxiv 2025 2026 — verify Fast-WAM exists, its key claims about video being dispensable at inference, and specifically check: does Fast-WAM use classifier-free guidance? What does \"CFG scale 1.0\" mean in their context? Was it trained with video feature dropout?\n\n3. Search \"Fast-WAM github checkpoint LIBERO\" — check if Fast-WAM has released code and LIBERO checkpoints.\n\n4. Search for \"GigaWorld-Policy\" and \"MotuBrain\" WAM 2026 — verify these exist and their claims about video features at inference.\n\nReport exact findings. Under 400 words.",
    "agentId": "ae0907a2909503632",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile the findings. Here is my report:\n\n---\n\n**1. CoRL 2026 Deadlines**\n\nConfirmed. CoRL 2026 is at JW Marriott Austin, TX, November 9--12. Abstract deadline: May 26, 2026 (11:59 UTC). Paper deadline: May 29, 2026 (11:59 UTC). All verified via the official [CoRL 2026 site](https://www.corl.org/) and [Call for Papers](https://www.corl.org/contributions/call-for-papers).\n\n**2. Fast-WAM (arXiv 2603.16666)**\n\nThe paper exists. Title: \"Fast-WAM: Do World Action Models Need Test-time Future Imagination?\" by Tianyuan Yuan et al. (Tsinghua / Galaxea AI, March 2026). Key claim confirmed: video prediction is dispensable at inference; its value lies in improving representations during training. At inference, Fast-WAM uses 10 denoising steps with **CFG scale 1.0** -- meaning classifier-free guidance weight = 1.0, which effectively means **no guidance** (purely conditional prediction, no unconditional branch interpolation). The model does use classifier-free guidance infrastructure, but the scale of 1.0 nullifies its effect. Regarding video feature dropout: Fast-WAM does **not** use traditional feature dropout on video. Instead, it uses a **structured attention mask** -- future video tokens are present during training (for the video co-training objective) but completely removed at inference. The \"uncond\" in checkpoint names (e.g., `libero_uncond_2cam224.pt`) refers to the unconditional (no-video-generation) inference variant.\n\n**3. Fast-WAM Code and Checkpoints**\n\nConfirmed released. GitHub: [yuantianyuan01/FastWAM](https://github.com/yuantianyuan01/FastWAM). HuggingFace checkpoints at [yuanty/fastwam](https://huggingface.co/yuanty/fastwam), including `libero_uncond_2cam224.pt`. Preprocessed LIBERO datasets also available on HuggingFace.\n\n**4. GigaWorld-Policy and MotuBrain**\n\nBoth exist. **GigaWorld-Policy** (arXiv 2603.17240) uses a causal design where future-video tokens cannot influence action tokens, making video generation optional at inference -- achieving 9x faster inference than the Motus baseline. Code at [open-gigaai/giga-world-policy](https://github.com/open-gigaai/giga-world-policy). **MotuBrain** (arXiv 2604.27792) by ShengShu Technology is a unified WAM supporting five modes (VLA, world model, video gen, IDM, joint prediction). It uses V2A-style asymmetric dependency enabling action-only inference without generating future video. Note: \"MotuBrain\" is the successor/rebrand of \"Motus\" (arXiv 2512.13030).\n\nSources:\n- [CoRL 2026](https://www.corl.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Fast-WAM arXiv](https://arxiv.org/abs/2603.16666)\n- [Fast-WAM HTML](https://arxiv.org/html/2603.16666v1)\n- [FastWAM GitHub](https://github.com/yuantianyuan01/FastWAM)\n- [FastWAM HuggingFace](https://huggingface.co/yuanty/fastwam)\n- [GigaWorld-Policy arXiv](https://arxiv.org/abs/2603.17240)\n- [GigaWorld-Policy GitHub](https://github.com/open-gigaai/giga-world-policy)\n- [MotuBrain arXiv](https://arxiv.org/html/2604.27792v2)\n- [MotuBrain press release](https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html)"
      }
    ],
    "totalDurationMs": 125525,
    "totalTokens": 25592,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 23513,
      "output_tokens": 1056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1056,
          "cache_read_input_tokens": 23513,
          "cache_creation_input_tokens": 1022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1022,
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
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "4c681576-d298-4c26-8f5b-89193ec2f9d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T19:48:40.453Z_

Good findings. Now let me do deeper verification on the critical issues — UWM's actual fine-tuned performance and the OA-WAM number discrepancy, plus check for any missed competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2d3385-b3da-40d4-8ebb-3a3084acd891",
  "isSidechain": false,
  "requestId": "req_011CauU3EZFSm9F3MWYHqnv3",
  "type": "assistant",
  "uuid": "e4f83309-e46a-45f3-8782-d659e8f154cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4bHfZg8ErCxG5YFPmPTGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7545,
      "cache_read_input_tokens": 33935,
      "output_tokens": 992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 992,
          "cache_read_input_tokens": 33935,
          "cache_creation_input_tokens": 7545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7545
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

_source line 23 · 2026-05-10T19:48:47.743Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014WSMxKmVoadkHYc7RCqojy`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Deep-read UWM paper performance",
  "prompt": "I need to read the UWM paper (arxiv 2504.02792) to verify its LIBERO performance numbers. The paper's Table II reportedly shows 79% average after fine-tuning.\n\nUse WebFetch to read https://arxiv.org/abs/2504.02792 and find:\n1. What is UWM's fine-tuned performance on LIBERO tasks? What specific tasks and success rates?\n2. How many fine-tuning steps are used? What compute does fine-tuning require?\n3. Does the paper discuss cross-modal CFG or guidance? Does setting t_o'=T give an unconditional action prediction?\n4. What does the paper say about the relationship between video timestep and action quality?\n\nAlso try WebFetch on https://arxiv.org/html/2504.02792v3 for the HTML version which may be more readable.\n\nReport exact numbers and quotes. Under 400 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f83309-e46a-45f3-8782-d659e8f154cf",
  "isSidechain": false,
  "requestId": "req_011CauU3EZFSm9F3MWYHqnv3",
  "type": "assistant",
  "uuid": "8a6f48fb-bdc6-4825-955d-4359d016bf2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4bHfZg8ErCxG5YFPmPTGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7545,
      "cache_read_input_tokens": 33935,
      "output_tokens": 992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 992,
          "cache_read_input_tokens": 33935,
          "cache_creation_input_tokens": 7545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7545
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

_source line 24 · 2026-05-10T19:48:53.133Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DjsB2JdiqaGuD9oEWcdfmW`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify OA-WAM exact numbers",
  "prompt": "I need to verify OA-WAM's exact LIBERO-Plus performance numbers. The proposal claims Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%), but a prior search found possibly different numbers (Geo-Avg 76.0, Camera 85.7).\n\nUse WebFetch to read the OA-WAM paper at https://arxiv.org/html/2605.06481v1 and find:\n1. The exact LIBERO-Plus results table with per-perturbation-type numbers\n2. What is the Geo-Avg (geometric average across perturbation types)?\n3. What are the Camera and Robot initial state specific numbers?\n4. What architectural modifications does OA-WAM require?\n\nAlso try: https://arxiv.org/abs/2605.06481\n\nReport exact numbers from tables. Under 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a6f48fb-bdc6-4825-955d-4359d016bf2e",
  "isSidechain": false,
  "requestId": "req_011CauU3EZFSm9F3MWYHqnv3",
  "type": "assistant",
  "uuid": "7dd7587e-f227-4fab-b48c-94b208147397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4bHfZg8ErCxG5YFPmPTGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7545,
      "cache_read_input_tokens": 33935,
      "output_tokens": 992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 992,
          "cache_read_input_tokens": 33935,
          "cache_creation_input_tokens": 7545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7545
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

_source line 25 · 2026-05-10T19:49:00.993Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GEtAn9KK98YMydowYJCCb9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for Mask World Model and DDP",
  "prompt": "I found two potentially competing papers that the proposal may have missed. I need to verify their relevance:\n\n1. \"Mask World Model\" (arXiv 2604.19683, April 2026) — Uses semantic mask prediction instead of pixel-level video prediction. Search for this paper and check: does it address geometric robustness? Is it evaluated on LIBERO-Plus? Would it compete with the SCG proposal?\n\n2. \"Dream Diffusion Policy\" or \"Dreaming the Unseen\" (arXiv 2603.21017, March 2026) — Integrates world model into policy via shared 3D encoder for OOD robustness. Search for this and check: is it training-free? Does it address geometric perturbations? LIBERO-Plus evaluation?\n\n3. Also search for \"X-WAM asynchronous denoising\" 2026 — verify this paper exists and its relationship to UWM's independent timestep mechanism.\n\n4. Search for \"Motus UniDiffuser world model robot\" to verify whether Motus uses the same independent timestep mechanism as UWM.\n\nUse WebSearch and WebFetch as needed. Under 400 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dd7587e-f227-4fab-b48c-94b208147397",
  "isSidechain": false,
  "requestId": "req_011CauU3EZFSm9F3MWYHqnv3",
  "type": "assistant",
  "uuid": "783af2e3-de04-4ca7-97b2-3522e85740b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4bHfZg8ErCxG5YFPmPTGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7545,
      "cache_read_input_tokens": 33935,
      "output_tokens": 992,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 992,
          "cache_read_input_tokens": 33935,
          "cache_creation_input_tokens": 7545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7545
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

_source line 26 · 2026-05-10T19:49:21.571Z_

<details><summary>↩ Tool result · `toolu_01DjsB2JdiqaGuD9oEWcdfmW`</summary>

```text
Here are the exact findings from the OA-WAM paper (arXiv 2605.06481):

---

**LIBERO-Plus Results (Table 2) -- OA-WAM exact numbers:**

| Perturbation Axis | Score |
|---|---|
| Camera | 80.5% |
| Robot Initial State | 89.6% |
| Layout | 82.8% |
| Lighting | 96.5% |
| Background | 95.9% |
| Language | 85.3% |
| Sensor Noise | 75.6% |
| **Geo-Avg** | **84.3%** |
| Seven-Axis Average | 83.9% |

**Verdict:** The proposal's claimed numbers (Geo-Avg 84.3%, Camera 80.5%, Robot 89.6%) are **correct** and match the paper exactly. The prior search finding "Geo-Avg 76.0, Camera 85.7" likely referred to a different method (possibly pi-0.5, which the paper notes scored 85.7% on some metric, with OA-WAM achieving +4.8% over it on Geo-Avg).

**Architectural modifications OA-WAM requires:**

1. **Address-only key projection** -- cross-slot key projection reads only the first 32 dims (`addr_k`), with a mask zeroing all coordinates beyond position 32.
2. **Per-layer address-reset hook** -- after every transformer block, a forward hook overwrites `x_k[1:32] <- addr_k` at slot positions, leaving the remaining 4064 coordinates untouched.

These operate across all 32 transformer layers with **no new parameters** -- they are tensor-level constraints (masking + hook), not added modules. This keeps target object selection invariant to scene context shifts.

agentId: a93775f35ca5a3b79 (use SendMessage with to: 'a93775f35ca5a3b79' to continue this agent)
&lt;usage>total_tokens: 11824
tool_uses: 3
duration_ms: 28435&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd7587e-f227-4fab-b48c-94b208147397",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "1ef38f24-463c-40ab-96d0-c6876e021537",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify OA-WAM's exact LIBERO-Plus performance numbers. The proposal claims Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%), but a prior search found possibly different numbers (Geo-Avg 76.0, Camera 85.7).\n\nUse WebFetch to read the OA-WAM paper at https://arxiv.org/html/2605.06481v1 and find:\n1. The exact LIBERO-Plus results table with per-perturbation-type numbers\n2. What is the Geo-Avg (geometric average across perturbation types)?\n3. What are the Camera and Robot initial state specific numbers?\n4. What architectural modifications does OA-WAM require?\n\nAlso try: https://arxiv.org/abs/2605.06481\n\nReport exact numbers from tables. Under 300 words.",
    "agentId": "a93775f35ca5a3b79",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the exact findings from the OA-WAM paper (arXiv 2605.06481):\n\n---\n\n**LIBERO-Plus Results (Table 2) -- OA-WAM exact numbers:**\n\n| Perturbation Axis | Score |\n|---|---|\n| Camera | 80.5% |\n| Robot Initial State | 89.6% |\n| Layout | 82.8% |\n| Lighting | 96.5% |\n| Background | 95.9% |\n| Language | 85.3% |\n| Sensor Noise | 75.6% |\n| **Geo-Avg** | **84.3%** |\n| Seven-Axis Average | 83.9% |\n\n**Verdict:** The proposal's claimed numbers (Geo-Avg 84.3%, Camera 80.5%, Robot 89.6%) are **correct** and match the paper exactly. The prior search finding \"Geo-Avg 76.0, Camera 85.7\" likely referred to a different method (possibly pi-0.5, which the paper notes scored 85.7% on some metric, with OA-WAM achieving +4.8% over it on Geo-Avg).\n\n**Architectural modifications OA-WAM requires:**\n\n1. **Address-only key projection** -- cross-slot key projection reads only the first 32 dims (`addr_k`), with a mask zeroing all coordinates beyond position 32.\n2. **Per-layer address-reset hook** -- after every transformer block, a forward hook overwrites `x_k[1:32] <- addr_k` at slot positions, leaving the remaining 4064 coordinates untouched.\n\nThese operate across all 32 transformer layers with **no new parameters** -- they are tensor-level constraints (masking + hook), not added modules. This keeps target object selection invariant to scene context shifts."
      }
    ],
    "totalDurationMs": 28435,
    "totalTokens": 11824,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 326,
      "cache_creation_input_tokens": 673,
      "cache_read_input_tokens": 10387,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 326,
          "output_tokens": 438,
          "cache_read_input_tokens": 10387,
          "cache_creation_input_tokens": 673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 673,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "7dd7587e-f227-4fab-b48c-94b208147397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1ef38f24-463c-40ab-96d0-c6876e021537",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spectral cross-modal guidance WAM proposal",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Tool result

_source line 29 · 2026-05-10T19:49:34.321Z_

<details><summary>↩ Tool result · `toolu_014WSMxKmVoadkHYc7RCqojy`</summary>

```text
Here are the findings from arxiv 2504.02792 (UWM paper, v3):

**1. LIBERO Fine-Tuned Performance (Table II: "Evaluation on LIBERO benchmark")**

| Task | UWM | DP | PAD | GR1 |
|------|-----|-----|-----|-----|
| Book-Caddy | 0.91 +/- 0.07 | — | — | — |
| Soup-Cheese | 0.93 +/- 0.01 | — | — | — |
| Bowl-Drawer | 0.80 +/- 0.02 | — | — | — |
| Moka-Moka | 0.68 +/- 0.02 | — | — | — |
| Mug-Mug | 0.65 +/- 0.01 | — | — | — |
| **Average** | **0.79 +/- 0.11** | 0.71 +/- 0.12 | 0.57 +/- 0.19 | 0.58 +/- 0.14 |

The 79% average claim is confirmed.

**2. Fine-Tuning Steps/Compute**

The paper states they "finetune on the downstream tasks for **10K gradient steps**." The appendix section "A3 Training Compute" exists but its content was not accessible in the HTML rendering (truncated).

**3. Cross-Modal CFG / Guidance**

The paper does **not** use or mention "classifier-free guidance," "guidance scale," or "CFG." Instead, it uses a timestep-based marginalization mechanism: *"Fixing the timestep for either t_a or t_o' to T marginalizes the corresponding variable a, o'."* Setting t_o'=T with o'_T ~ N(0,I) marginalizes observations, yielding the action distribution p(a|o) -- this is action prediction **without future observation conditioning**, not fully unconditional prediction (it still conditions on the current observation o).

**4. Video Timestep vs. Action Quality**

The paper contains **no explicit analysis or ablation** studying how varying the video denoising timestep t_o' affects action prediction quality. There are forward dynamics visualizations (Figure 8) and trajectory results (Table III), but no systematic study of this relationship.

agentId: a129a0ee23e89453b (use SendMessage with to: 'a129a0ee23e89453b' to continue this agent)
&lt;usage>total_tokens: 12729
tool_uses: 4
duration_ms: 46574&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a6f48fb-bdc6-4825-955d-4359d016bf2e",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "5cd0ba18-fd02-4e24-a6ec-4da48ddb48c8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to read the UWM paper (arxiv 2504.02792) to verify its LIBERO performance numbers. The paper's Table II reportedly shows 79% average after fine-tuning.\n\nUse WebFetch to read https://arxiv.org/abs/2504.02792 and find:\n1. What is UWM's fine-tuned performance on LIBERO tasks? What specific tasks and success rates?\n2. How many fine-tuning steps are used? What compute does fine-tuning require?\n3. Does the paper discuss cross-modal CFG or guidance? Does setting t_o'=T give an unconditional action prediction?\n4. What does the paper say about the relationship between video timestep and action quality?\n\nAlso try WebFetch on https://arxiv.org/html/2504.02792v3 for the HTML version which may be more readable.\n\nReport exact numbers and quotes. Under 400 words.",
    "agentId": "a129a0ee23e89453b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings from arxiv 2504.02792 (UWM paper, v3):\n\n**1. LIBERO Fine-Tuned Performance (Table II: \"Evaluation on LIBERO benchmark\")**\n\n| Task | UWM | DP | PAD | GR1 |\n|------|-----|-----|-----|-----|\n| Book-Caddy | 0.91 +/- 0.07 | — | — | — |\n| Soup-Cheese | 0.93 +/- 0.01 | — | — | — |\n| Bowl-Drawer | 0.80 +/- 0.02 | — | — | — |\n| Moka-Moka | 0.68 +/- 0.02 | — | — | — |\n| Mug-Mug | 0.65 +/- 0.01 | — | — | — |\n| **Average** | **0.79 +/- 0.11** | 0.71 +/- 0.12 | 0.57 +/- 0.19 | 0.58 +/- 0.14 |\n\nThe 79% average claim is confirmed.\n\n**2. Fine-Tuning Steps/Compute**\n\nThe paper states they \"finetune on the downstream tasks for **10K gradient steps**.\" The appendix section \"A3 Training Compute\" exists but its content was not accessible in the HTML rendering (truncated).\n\n**3. Cross-Modal CFG / Guidance**\n\nThe paper does **not** use or mention \"classifier-free guidance,\" \"guidance scale,\" or \"CFG.\" Instead, it uses a timestep-based marginalization mechanism: *\"Fixing the timestep for either t_a or t_o' to T marginalizes the corresponding variable a, o'.\"* Setting t_o'=T with o'_T ~ N(0,I) marginalizes observations, yielding the action distribution p(a|o) -- this is action prediction **without future observation conditioning**, not fully unconditional prediction (it still conditions on the current observation o).\n\n**4. Video Timestep vs. Action Quality**\n\nThe paper contains **no explicit analysis or ablation** studying how varying the video denoising timestep t_o' affects action prediction quality. There are forward dynamics visualizations (Figure 8) and trajectory results (Table III), but no systematic study of this relationship."
      }
    ],
    "totalDurationMs": 46574,
    "totalTokens": 12729,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 11619,
      "output_tokens": 575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 575,
          "cache_read_input_tokens": 11619,
          "cache_creation_input_tokens": 534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 534,
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
  "sourceToolAssistantUUID": "8a6f48fb-bdc6-4825-955d-4359d016bf2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:50:01.169Z_

<details><summary>↩ Tool result · `toolu_01GEtAn9KK98YMydowYJCCb9`</summary>

```text
Here are the findings for all four papers:

**1. Mask World Model (MWM) — arXiv [2604.19683](https://arxiv.org/abs/2604.19683)**
Confirmed real. MWM predicts semantic mask evolution instead of pixels, filtering visual noise (backgrounds, lighting). However, it does **not** address geometric robustness — it targets visual/texture distractions. It evaluates on standard **LIBERO and RLBench**, not LIBERO-Plus. It competes with the SCG proposal on visual robustness but does **not** overlap on geometric perturbations, so it is complementary rather than directly competing.

**2. Dreaming the Unseen / DDP — arXiv [2603.21017](https://arxiv.org/html/2603.21017v1)**
Confirmed real (March 2026, TU Munich / Nanjing). It **is** training-free at test time — it detects OOD anomalies and falls back on internally imagined latent dynamics. It **does** address geometric perturbations (mid-task object displacements outside training bounds). However, it evaluates on **MetaWorld, Adroit, and real-world Franka tasks** — not LIBERO-Plus. This is a genuine competitor on OOD geometric robustness, though it uses a different mechanism (anomaly-triggered imagination vs. SCG's structured consistency).

**3. X-WAM — arXiv [2604.26694](https://arxiv.org/html/2604.26694v2)**
Confirmed real. X-WAM's Asynchronous Noise Sampling (ANS) is **not** the same as UWM's independent timestep mechanism. X-WAM explicitly **rejects** UWM's independent sampling, arguing it creates a train/test distribution mismatch. ANS instead uses coupled joint-distribution sampling that matches the test-time schedule. This is a meaningful architectural distinction worth noting.

**4. Motus — arXiv [2512.13030](https://arxiv.org/abs/2512.13030)**
Confirmed real. Motus **does** use a UniDiffuser-style scheduler with independent timesteps per modality (video and action get distinct noise scales), which is the **same core mechanism** as UWM. It enables freezing the video stream mid-inference while continuing action denoising. So Motus and UWM share this independent-timestep lineage, while X-WAM deliberately departs from it.

Sources:
- [Mask World Model (2604.19683)](https://arxiv.org/abs/2604.19683)
- [Dreaming the Unseen (2603.21017)](https://arxiv.org/html/2603.21017v1)
- [X-WAM (2604.26694)](https://arxiv.org/html/2604.26694v2)
- [Motus (2512.13030)](https://arxiv.org/abs/2512.13030)

agentId: ab7671d1dfacfa515 (use SendMessage with to: 'ab7671d1dfacfa515' to continue this agent)
&lt;usage>total_tokens: 16759
tool_uses: 8
duration_ms: 60173&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "783af2e3-de04-4ca7-97b2-3522e85740b1",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "69075e7f-5dde-41f4-90f7-d0a7b45262ba",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I found two potentially competing papers that the proposal may have missed. I need to verify their relevance:\n\n1. \"Mask World Model\" (arXiv 2604.19683, April 2026) — Uses semantic mask prediction instead of pixel-level video prediction. Search for this paper and check: does it address geometric robustness? Is it evaluated on LIBERO-Plus? Would it compete with the SCG proposal?\n\n2. \"Dream Diffusion Policy\" or \"Dreaming the Unseen\" (arXiv 2603.21017, March 2026) — Integrates world model into policy via shared 3D encoder for OOD robustness. Search for this and check: is it training-free? Does it address geometric perturbations? LIBERO-Plus evaluation?\n\n3. Also search for \"X-WAM asynchronous denoising\" 2026 — verify this paper exists and its relationship to UWM's independent timestep mechanism.\n\n4. Search for \"Motus UniDiffuser world model robot\" to verify whether Motus uses the same independent timestep mechanism as UWM.\n\nUse WebSearch and WebFetch as needed. Under 400 words.",
    "agentId": "ab7671d1dfacfa515",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for all four papers:\n\n**1. Mask World Model (MWM) — arXiv [2604.19683](https://arxiv.org/abs/2604.19683)**\nConfirmed real. MWM predicts semantic mask evolution instead of pixels, filtering visual noise (backgrounds, lighting). However, it does **not** address geometric robustness — it targets visual/texture distractions. It evaluates on standard **LIBERO and RLBench**, not LIBERO-Plus. It competes with the SCG proposal on visual robustness but does **not** overlap on geometric perturbations, so it is complementary rather than directly competing.\n\n**2. Dreaming the Unseen / DDP — arXiv [2603.21017](https://arxiv.org/html/2603.21017v1)**\nConfirmed real (March 2026, TU Munich / Nanjing). It **is** training-free at test time — it detects OOD anomalies and falls back on internally imagined latent dynamics. It **does** address geometric perturbations (mid-task object displacements outside training bounds). However, it evaluates on **MetaWorld, Adroit, and real-world Franka tasks** — not LIBERO-Plus. This is a genuine competitor on OOD geometric robustness, though it uses a different mechanism (anomaly-triggered imagination vs. SCG's structured consistency).\n\n**3. X-WAM — arXiv [2604.26694](https://arxiv.org/html/2604.26694v2)**\nConfirmed real. X-WAM's Asynchronous Noise Sampling (ANS) is **not** the same as UWM's independent timestep mechanism. X-WAM explicitly **rejects** UWM's independent sampling, arguing it creates a train/test distribution mismatch. ANS instead uses coupled joint-distribution sampling that matches the test-time schedule. This is a meaningful architectural distinction worth noting.\n\n**4. Motus — arXiv [2512.13030](https://arxiv.org/abs/2512.13030)**\nConfirmed real. Motus **does** use a UniDiffuser-style scheduler with independent timesteps per modality (video and action get distinct noise scales), which is the **same core mechanism** as UWM. It enables freezing the video stream mid-inference while continuing action denoising. So Motus and UWM share this independent-timestep lineage, while X-WAM deliberately departs from it.\n\nSources:\n- [Mask World Model (2604.19683)](https://arxiv.org/abs/2604.19683)\n- [Dreaming the Unseen (2603.21017)](https://arxiv.org/html/2603.21017v1)\n- [X-WAM (2604.26694)](https://arxiv.org/html/2604.26694v2)\n- [Motus (2512.13030)](https://arxiv.org/abs/2512.13030)"
      }
    ],
    "totalDurationMs": 60173,
    "totalTokens": 16759,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 13816,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 714,
          "cache_read_input_tokens": 13816,
          "cache_creation_input_tokens": 2228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2228,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "783af2e3-de04-4ca7-97b2-3522e85740b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-10T19:50:01.176Z_

```json
{
  "parentUuid": "69075e7f-5dde-41f4-90f7-d0a7b45262ba",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e59ef616-836c-414c-9572-dd655959d92d",
  "timestamp": "2026-05-10T19:50:01.176Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-10T19:50:07.690Z_

Critical finding: UWM's 79% is the **fine-tuned** result, not pretraining-only. Let me verify this and check one more dimension — the X-WAM criticism of UWM's independent timesteps, which could undermine the entire approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e59ef616-836c-414c-9572-dd655959d92d",
  "isSidechain": false,
  "requestId": "req_011CauU9Zm4s7eDe6svHZAit",
  "type": "assistant",
  "uuid": "ca634558-fb87-491f-b43a-319d4638e444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iUjYD3QzJhW5b1upaf9E1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3119,
      "cache_read_input_tokens": 41480,
      "output_tokens": 976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 976,
          "cache_read_input_tokens": 41480,
          "cache_creation_input_tokens": 3119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3119
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

_source line 33 · 2026-05-10T19:50:13.628Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NtGNbpKom32Sq8aoYWnoBg`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "X-WAM critique of UWM timesteps",
  "prompt": "I need to understand X-WAM's critique of UWM's independent timestep mechanism. X-WAM (arXiv 2604.26694) argues that UWM's independent timestep sampling creates a train/test distribution mismatch.\n\nUse WebFetch to read https://arxiv.org/html/2604.26694v2 and find:\n1. What exactly is X-WAM's critique of independent timestep sampling (used by UWM and Motus)?\n2. Does X-WAM provide empirical evidence that independent timesteps hurt performance?\n3. What is X-WAM's alternative (Asynchronous Noise Sampling)?\n4. Does this critique apply to the proposed SCG method's use of UWM's t_o'=T marginalization for computing unconditional scores?\n\nThis is important because if X-WAM's critique is valid, then SCG's entire approach of using t_o'=T to compute unconditional action scores may produce unreliable guidance vectors.\n\nReport exact findings and quotes. Under 400 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca634558-fb87-491f-b43a-319d4638e444",
  "isSidechain": false,
  "requestId": "req_011CauU9Zm4s7eDe6svHZAit",
  "type": "assistant",
  "uuid": "c804b088-1b85-4b45-b444-a288017a74a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iUjYD3QzJhW5b1upaf9E1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3119,
      "cache_read_input_tokens": 41480,
      "output_tokens": 976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 976,
          "cache_read_input_tokens": 41480,
          "cache_creation_input_tokens": 3119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3119
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

_source line 34 · 2026-05-10T19:50:20.481Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VpweqVjdcLrAnUyuddc956`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check UWM fine-tuning compute cost",
  "prompt": "I need to estimate the compute cost of fine-tuning UWM on LIBERO tasks.\n\n1. Search for \"UWM unified world model fine-tuning compute GPU hours\" or check the GitHub repo at https://github.com/WEIRDLabUW/unified-world-model for training configs\n2. The paper says 10K gradient steps for fine-tuning. Search for typical compute costs: what batch size, what model size is UWM? How long would 10K steps take on an H100?\n3. Search for \"UWM model parameters\" or \"unified world model size\" to estimate the model size\n\nAlso important: UWM achieves 79% average on LIBERO after fine-tuning. The proposal needs competitive baseline performance. Search for whether anyone has achieved better LIBERO results by fine-tuning UWM differently, or if 79% is the ceiling.\n\nUnder 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c804b088-1b85-4b45-b444-a288017a74a2",
  "isSidechain": false,
  "requestId": "req_011CauU9Zm4s7eDe6svHZAit",
  "type": "assistant",
  "uuid": "cea44634-518b-4401-8ba5-0993a3606eaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iUjYD3QzJhW5b1upaf9E1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3119,
      "cache_read_input_tokens": 41480,
      "output_tokens": 976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 976,
          "cache_read_input_tokens": 41480,
          "cache_creation_input_tokens": 3119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3119
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

_source line 35 · 2026-05-10T19:50:27.850Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0138GjMuiwxJ1qfoSqeCd8dj`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for concurrent spectral/SVD WAM work",
  "prompt": "I need one final round of competition searching. Search for:\n\n1. \"spectral analysis world model robot\" 2025 2026 — any spectral methods applied to world models for robotics\n2. \"classifier-free guidance robot action diffusion\" 2025 2026 — any CFG applied to action diffusion in robotics\n3. \"video conditioned action prediction guidance\" 2025 2026 — video-to-action guidance methods\n4. \"cross-modal diffusion guidance\" 2025 2026 — general cross-modal guidance in diffusion models\n5. \"selective guidance diffusion model\" 2025 2026 — selective/filtered guidance approaches\n\nI'm looking for any work that combines spectral/SVD filtering with diffusion guidance for robot control, or any work that applies cross-modal CFG in the video→action direction of WAMs.\n\nUnder 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cea44634-518b-4401-8ba5-0993a3606eaa",
  "isSidechain": false,
  "requestId": "req_011CauU9Zm4s7eDe6svHZAit",
  "type": "assistant",
  "uuid": "e471ab53-956e-411a-8bbd-acdbe313e67a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iUjYD3QzJhW5b1upaf9E1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3119,
      "cache_read_input_tokens": 41480,
      "output_tokens": 976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 976,
          "cache_read_input_tokens": 41480,
          "cache_creation_input_tokens": 3119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3119
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

_source line 36 · 2026-05-10T19:50:49.074Z_

<details><summary>↩ Tool result · `toolu_01NtGNbpKom32Sq8aoYWnoBg`</summary>

```text
Here are the exact findings from X-WAM (arXiv 2604.26694v2):

**1. X-WAM's Critique of Independent Timestep Sampling**

X-WAM argues that UWM/Motus-style independent sampling creates configurations during training that never occur at inference. The key quote from Section 3.3:

> "independently sampling each modality's timestep introduces training configurations that never arise at test time (e.g., t_O < t_a), degrading training efficiency."

At inference, actions are always denoised first (fewer steps), so the observation timestep is always >= action timestep. Independent uniform sampling violates this constraint ~50% of the time.

**2. Empirical Evidence**

Table 4(b) provides a direct ablation. Decoupled (independent) training + async inference yields **PSNR 22.60, AbsRel 0.0430**. ANS training + async inference yields **PSNR 23.46, AbsRel 0.0349** -- a meaningful reconstruction quality improvement. The paper explains: the video branch must denoise conditioned on clean actions, "a regime never seen during independently sampled training." However, the success rate difference is marginal (67.2 vs 67.8), suggesting the mismatch primarily hurts video quality, not action quality.

**3. X-WAM's Alternative: Asynchronous Noise Sampling (ANS)**

ANS samples t_O *conditioned on* t_a via a mixture distribution:
- With probability p: t_a=0, t_O ~ U(0,1) (action-clean, video-noisy)
- With probability 1-p: t_a ~ U(0,1), t_O = t_a + (1-t_a)*b where b ~ Beta(1.5,1)

This ensures t_O >= t_a always, matching the inference-time distribution.

**4. Implications for SCG's t_o'=T Marginalization**

The paper contains **no discussion** of t_o=T marginalization for unconditional score computation. Critically, the empirical evidence shows the train/test mismatch primarily degrades **video reconstruction**, not action prediction (success rates are nearly identical: 67.2 vs 67.8). SCG's use of t_o'=T to compute unconditional action scores operates purely on the action modality's score. Since X-WAM's own data shows action performance is robust to the distribution mismatch, this critique does **not** strongly undermine SCG's approach. The concern about unreliable guidance vectors from t_o'=T marginalization appears to be low-risk based on X-WAM's own evidence.

agentId: a5999bddc77ce1a36 (use SendMessage with to: 'a5999bddc77ce1a36' to continue this agent)
&lt;usage>total_tokens: 11976
tool_uses: 2
duration_ms: 35443&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c804b088-1b85-4b45-b444-a288017a74a2",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "71fba10e-2d1b-40b1-9973-fc3cf61ecdaf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand X-WAM's critique of UWM's independent timestep mechanism. X-WAM (arXiv 2604.26694) argues that UWM's independent timestep sampling creates a train/test distribution mismatch.\n\nUse WebFetch to read https://arxiv.org/html/2604.26694v2 and find:\n1. What exactly is X-WAM's critique of independent timestep sampling (used by UWM and Motus)?\n2. Does X-WAM provide empirical evidence that independent timesteps hurt performance?\n3. What is X-WAM's alternative (Asynchronous Noise Sampling)?\n4. Does this critique apply to the proposed SCG method's use of UWM's t_o'=T marginalization for computing unconditional scores?\n\nThis is important because if X-WAM's critique is valid, then SCG's entire approach of using t_o'=T to compute unconditional action scores may produce unreliable guidance vectors.\n\nReport exact findings and quotes. Under 400 words.",
    "agentId": "a5999bddc77ce1a36",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the exact findings from X-WAM (arXiv 2604.26694v2):\n\n**1. X-WAM's Critique of Independent Timestep Sampling**\n\nX-WAM argues that UWM/Motus-style independent sampling creates configurations during training that never occur at inference. The key quote from Section 3.3:\n\n> \"independently sampling each modality's timestep introduces training configurations that never arise at test time (e.g., t_O < t_a), degrading training efficiency.\"\n\nAt inference, actions are always denoised first (fewer steps), so the observation timestep is always >= action timestep. Independent uniform sampling violates this constraint ~50% of the time.\n\n**2. Empirical Evidence**\n\nTable 4(b) provides a direct ablation. Decoupled (independent) training + async inference yields **PSNR 22.60, AbsRel 0.0430**. ANS training + async inference yields **PSNR 23.46, AbsRel 0.0349** -- a meaningful reconstruction quality improvement. The paper explains: the video branch must denoise conditioned on clean actions, \"a regime never seen during independently sampled training.\" However, the success rate difference is marginal (67.2 vs 67.8), suggesting the mismatch primarily hurts video quality, not action quality.\n\n**3. X-WAM's Alternative: Asynchronous Noise Sampling (ANS)**\n\nANS samples t_O *conditioned on* t_a via a mixture distribution:\n- With probability p: t_a=0, t_O ~ U(0,1) (action-clean, video-noisy)\n- With probability 1-p: t_a ~ U(0,1), t_O = t_a + (1-t_a)*b where b ~ Beta(1.5,1)\n\nThis ensures t_O >= t_a always, matching the inference-time distribution.\n\n**4. Implications for SCG's t_o'=T Marginalization**\n\nThe paper contains **no discussion** of t_o=T marginalization for unconditional score computation. Critically, the empirical evidence shows the train/test mismatch primarily degrades **video reconstruction**, not action prediction (success rates are nearly identical: 67.2 vs 67.8). SCG's use of t_o'=T to compute unconditional action scores operates purely on the action modality's score. Since X-WAM's own data shows action performance is robust to the distribution mismatch, this critique does **not** strongly undermine SCG's approach. The concern about unreliable guidance vectors from t_o'=T marginalization appears to be low-risk based on X-WAM's own evidence."
      }
    ],
    "totalDurationMs": 35443,
    "totalTokens": 11976,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 10405,
      "output_tokens": 634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 634,
          "cache_read_input_tokens": 10405,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 936,
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
  "sourceToolAssistantUUID": "c804b088-1b85-4b45-b444-a288017a74a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T19:51:04.771Z_

<details><summary>↩ Tool result · `toolu_0138GjMuiwxJ1qfoSqeCd8dj`</summary>

```text
Here are the results of the final competition search round:

---

**The closest direct hit is CFG-DP** ([Enhancing Diffusion Policy with Classifier-Free Guidance for Temporal Robotic Tasks](https://arxiv.org/abs/2510.09786)), which integrates classifier-free guidance into diffusion policy for robotics, using timestep inputs to track task phase and dynamically adjust action predictions. However, this operates purely in action space -- it does not involve video conditioning or spectral filtering.

In the **video-to-action direction**, Video Prediction Policy (VPP) uses representations from video diffusion models to guide robot action learning, and AVID adapts pretrained video models for action-conditioned prediction. These use video as a representational prior for actions but do not apply CFG-style guidance across the video-action modality boundary.

In **cross-modal diffusion guidance**, the field is active but concentrated in text-image, text-audio, and molecular domains. No work was found applying cross-modal CFG specifically in the video-to-action direction for robotics.

For **selective/adaptive guidance**, Feedback Guidance (FBG) proposes state-dependent guidance coefficients that self-regulate based on need, and Model-Guidance (MG) embeds the classifier directly into the diffusion model. Neither applies spectral filtering or SVD-based selection.

**No existing work was found** that combines spectral/SVD filtering with diffusion guidance for robot control, nor any work applying cross-modal CFG in the video-to-action direction within world-action models. The specific intersection of frequency-domain analysis (spectral decomposition) with guidance mechanisms in WAMs appears to be an open research gap.

---

Sources:
- [CFG-DP: Enhancing Diffusion Policy with CFG for Temporal Robotic Tasks](https://arxiv.org/abs/2510.09786)
- [Video Prediction Policy (VPP)](https://openreview.net/forum?id=c0dhw1du33)
- [AVID: Adapting Video Diffusion](https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_64.pdf)
- [Feedback Guidance of Diffusion Models](https://openreview.net/forum?id=8ySOcf7UpM)
- [Diffusion Models without CFG (Model-Guidance)](https://openreview.net/forum?id=kkiLdrKk0G)
- [Cross-Modal Contextualized Diffusion Models](https://openreview.net/forum?id=nFMS6wF2xq)
- [Diffusion Models for Robotic Manipulation Survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)

agentId: aa3ff46ba88435009 (use SendMessage with to: 'aa3ff46ba88435009' to continue this agent)
&lt;usage>total_tokens: 15961
tool_uses: 6
duration_ms: 36918&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e471ab53-956e-411a-8bbd-acdbe313e67a",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "a0a595ce-e38a-4199-bfa7-84a6f98f56bd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need one final round of competition searching. Search for:\n\n1. \"spectral analysis world model robot\" 2025 2026 — any spectral methods applied to world models for robotics\n2. \"classifier-free guidance robot action diffusion\" 2025 2026 — any CFG applied to action diffusion in robotics\n3. \"video conditioned action prediction guidance\" 2025 2026 — video-to-action guidance methods\n4. \"cross-modal diffusion guidance\" 2025 2026 — general cross-modal guidance in diffusion models\n5. \"selective guidance diffusion model\" 2025 2026 — selective/filtered guidance approaches\n\nI'm looking for any work that combines spectral/SVD filtering with diffusion guidance for robot control, or any work that applies cross-modal CFG in the video→action direction of WAMs.\n\nUnder 300 words.",
    "agentId": "aa3ff46ba88435009",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the results of the final competition search round:\n\n---\n\n**The closest direct hit is CFG-DP** ([Enhancing Diffusion Policy with Classifier-Free Guidance for Temporal Robotic Tasks](https://arxiv.org/abs/2510.09786)), which integrates classifier-free guidance into diffusion policy for robotics, using timestep inputs to track task phase and dynamically adjust action predictions. However, this operates purely in action space -- it does not involve video conditioning or spectral filtering.\n\nIn the **video-to-action direction**, Video Prediction Policy (VPP) uses representations from video diffusion models to guide robot action learning, and AVID adapts pretrained video models for action-conditioned prediction. These use video as a representational prior for actions but do not apply CFG-style guidance across the video-action modality boundary.\n\nIn **cross-modal diffusion guidance**, the field is active but concentrated in text-image, text-audio, and molecular domains. No work was found applying cross-modal CFG specifically in the video-to-action direction for robotics.\n\nFor **selective/adaptive guidance**, Feedback Guidance (FBG) proposes state-dependent guidance coefficients that self-regulate based on need, and Model-Guidance (MG) embeds the classifier directly into the diffusion model. Neither applies spectral filtering or SVD-based selection.\n\n**No existing work was found** that combines spectral/SVD filtering with diffusion guidance for robot control, nor any work applying cross-modal CFG in the video-to-action direction within world-action models. The specific intersection of frequency-domain analysis (spectral decomposition) with guidance mechanisms in WAMs appears to be an open research gap.\n\n---\n\nSources:\n- [CFG-DP: Enhancing Diffusion Policy with CFG for Temporal Robotic Tasks](https://arxiv.org/abs/2510.09786)\n- [Video Prediction Policy (VPP)](https://openreview.net/forum?id=c0dhw1du33)\n- [AVID: Adapting Video Diffusion](https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_64.pdf)\n- [Feedback Guidance of Diffusion Models](https://openreview.net/forum?id=8ySOcf7UpM)\n- [Diffusion Models without CFG (Model-Guidance)](https://openreview.net/forum?id=kkiLdrKk0G)\n- [Cross-Modal Contextualized Diffusion Models](https://openreview.net/forum?id=nFMS6wF2xq)\n- [Diffusion Models for Robotic Manipulation Survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)"
      }
    ],
    "totalDurationMs": 36918,
    "totalTokens": 15961,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 2808,
      "cache_creation_input_tokens": 2102,
      "cache_read_input_tokens": 10375,
      "output_tokens": 676,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2102
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2808,
          "output_tokens": 676,
          "cache_read_input_tokens": 10375,
          "cache_creation_input_tokens": 2102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2102,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "e471ab53-956e-411a-8bbd-acdbe313e67a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a0a595ce-e38a-4199-bfa7-84a6f98f56bd",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spectral cross-modal guidance WAM proposal",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Tool result

_source line 40 · 2026-05-10T19:51:53.813Z_

<details><summary>↩ Tool result · `toolu_01VpweqVjdcLrAnUyuddc956`</summary>

```text
I now have enough information to provide a solid estimate. Here is the summary:

---

## UWM Fine-Tuning Compute Estimate for LIBERO

**Model size:** UWM uses a ~180M-parameter DiT (Diffusion Transformer) backbone with a frozen SDXL VAE encoder, ResNet-18 image encoder, spatiotemporal patchifier (4x4x2), and 8 register tokens for cross-modal information exchange. The full trainable parameter count during fine-tuning is approximately 180M.

**Fine-tuning config:** The paper specifies **10K gradient steps** for LIBERO fine-tuning. Exact batch size and learning rate are not publicly documented in the repo or paper body, but pretraining uses 100K steps on mixed robot/video data. Based on comparable DiT-scale models (e.g., diffusion policy architectures), a typical batch size is 64-256, and fine-tuning a 180M-parameter diffusion transformer for 10K steps on a **single H100** would take roughly **2-6 GPU-hours** depending on batch size, sequence length, and whether video prediction heads are active during fine-tuning.

**Estimated cost:** At ~$3/H100-hour (cloud spot pricing), this is approximately **$6-18 per LIBERO task suite** fine-tune run. This is modest compute.

**Performance ceiling concern:** UWM achieves **79% average** on LIBERO (OOD setting), with individual tasks ranging from 65% (Mug-Mug) to 93% (Soup-Cheese). However, this is **well below current SOTA**: methods like SimpleVLA-RL (99.1%), RLinf-VLA (98.1%), and VITA-VLA (97.3%) substantially outperform UWM on standard LIBERO. These top methods typically use RL fine-tuning on top of behavioral cloning, which yields +20-45 percentage point gains. UWM's 79% reflects pure BC fine-tuning without RL -- it is not competitive as a LIBERO baseline unless augmented with RL or unless you are specifically evaluating OOD generalization, where LIBERO-PRO/Plus analyses show all methods collapse to 0-40%.

Sources:
- [UWM Paper (arXiv)](https://arxiv.org/html/2504.02792v1)
- [UWM GitHub](https://github.com/WEIRDLabUW/unified-world-model)
- [LIBERO Benchmark Overview](https://www.emergentmind.com/topics/libero)
- [LIBERO-PRO Robustness Analysis](https://arxiv.org/html/2510.03827v1)
- [UWM Project Page](https://weirdlabuw.github.io/uwm/)

agentId: a3776aa774931a64a (use SendMessage with to: 'a3776aa774931a64a' to continue this agent)
&lt;usage>total_tokens: 20235
tool_uses: 15
duration_ms: 93329&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cea44634-518b-4401-8ba5-0993a3606eaa",
  "isSidechain": false,
  "promptId": "14982a83-ad67-4f73-8c3e-9a7531dc4dec",
  "type": "user",
  "uuid": "e6fb6db4-b6e5-4958-8438-40e053dba6e5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to estimate the compute cost of fine-tuning UWM on LIBERO tasks.\n\n1. Search for \"UWM unified world model fine-tuning compute GPU hours\" or check the GitHub repo at https://github.com/WEIRDLabUW/unified-world-model for training configs\n2. The paper says 10K gradient steps for fine-tuning. Search for typical compute costs: what batch size, what model size is UWM? How long would 10K steps take on an H100?\n3. Search for \"UWM model parameters\" or \"unified world model size\" to estimate the model size\n\nAlso important: UWM achieves 79% average on LIBERO after fine-tuning. The proposal needs competitive baseline performance. Search for whether anyone has achieved better LIBERO results by fine-tuning UWM differently, or if 79% is the ceiling.\n\nUnder 300 words.",
    "agentId": "a3776aa774931a64a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough information to provide a solid estimate. Here is the summary:\n\n---\n\n## UWM Fine-Tuning Compute Estimate for LIBERO\n\n**Model size:** UWM uses a ~180M-parameter DiT (Diffusion Transformer) backbone with a frozen SDXL VAE encoder, ResNet-18 image encoder, spatiotemporal patchifier (4x4x2), and 8 register tokens for cross-modal information exchange. The full trainable parameter count during fine-tuning is approximately 180M.\n\n**Fine-tuning config:** The paper specifies **10K gradient steps** for LIBERO fine-tuning. Exact batch size and learning rate are not publicly documented in the repo or paper body, but pretraining uses 100K steps on mixed robot/video data. Based on comparable DiT-scale models (e.g., diffusion policy architectures), a typical batch size is 64-256, and fine-tuning a 180M-parameter diffusion transformer for 10K steps on a **single H100** would take roughly **2-6 GPU-hours** depending on batch size, sequence length, and whether video prediction heads are active during fine-tuning.\n\n**Estimated cost:** At ~$3/H100-hour (cloud spot pricing), this is approximately **$6-18 per LIBERO task suite** fine-tune run. This is modest compute.\n\n**Performance ceiling concern:** UWM achieves **79% average** on LIBERO (OOD setting), with individual tasks ranging from 65% (Mug-Mug) to 93% (Soup-Cheese). However, this is **well below current SOTA**: methods like SimpleVLA-RL (99.1%), RLinf-VLA (98.1%), and VITA-VLA (97.3%) substantially outperform UWM on standard LIBERO. These top methods typically use RL fine-tuning on top of behavioral cloning, which yields +20-45 percentage point gains. UWM's 79% reflects pure BC fine-tuning without RL -- it is not competitive as a LIBERO baseline unless augmented with RL or unless you are specifically evaluating OOD generalization, where LIBERO-PRO/Plus analyses show all methods collapse to 0-40%.\n\nSources:\n- [UWM Paper (arXiv)](https://arxiv.org/html/2504.02792v1)\n- [UWM GitHub](https://github.com/WEIRDLabUW/unified-world-model)\n- [LIBERO Benchmark Overview](https://www.emergentmind.com/topics/libero)\n- [LIBERO-PRO Robustness Analysis](https://arxiv.org/html/2510.03827v1)\n- [UWM Project Page](https://weirdlabuw.github.io/uwm/)"
      }
    ],
    "totalDurationMs": 93329,
    "totalTokens": 20235,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 18560,
      "output_tokens": 674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1000
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 674,
          "cache_read_input_tokens": 18560,
          "cache_creation_input_tokens": 1000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1000,
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
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "cea44634-518b-4401-8ba5-0993a3606eaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T19:53:24.644Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information to form my review. Let me synthesize all findings:

## Key Verified Facts

### UWM Backbone
- UWM (RSS 2025) exists, has released LIBERO-90 checkpoint
- Fine-tuned LIBERO performance: **79% average** — this is the POST-fine-tuning number, not pretraining
- Individual tasks range from 65% to 93%
- Model is ~180M parameters, fine-tuning takes ~2-6 GPU-hours per task suite
- UWM does NOT use or mention CFG. It uses timestep marginalization (t_o'=T) to remove video conditioning


- The paper doesn't explore how varying the video timestep impacts action quality

X-WAM raises concerns about independent timestep sampling creating train/test distribution mismatch, but their own results show action performance barely changes (67.2 vs 67.8) — the degradation is mainly in video quality, which somewhat validates UWM's approach. OA-WAM achieves the exact numbers I found (Geo-Avg 84.3%, Camera 80.5%, Robot 89.6%) without introducing new parameters, just through masking and hooks.

I'm verifying the other baseline methods: CKT-WAM hits 86.1%, Being-H0.7 reaches 99.2% on LIBERO standard with 82.1%/84.8% on LIBERO-Plus, and Fast-WAM uses CFG scale 1.0 without video feature dropout, confirming the proposal's correction. ICG, DiffStateGrad, and CPC Theory all check out at their stated venues, and CoRL 2026 is confirmed for Austin November 9-12. The key finding is that no existing work combines SVD spectral filtering with cross-modal diffusion guidance for robot control, and while CFG-DP exists, it's single-modal — the cross-modal CFG application in the video-to-action direction appears novel.

Looking at competing inference-time robustness methods, there's MWM which is complementary rather than directly competing, Dream Diffusion Policy that tackles OOD robustness through a different mechanism, WARPD with an entirely different approach, and CFG-DP as the single-modal baseline.

The critical issue is UWM's baseline performance — it only achieves 79% on standard LIBERO after fine-tuning, which is the best their method can do with their recipe, not a pretraining number. Current state-of-the-art sits at 97-99%, so there's a substantial 20-point gap. The proposal claims UWM fine-tuned on specific LIBERO tasks achieves competitive performance, but this baseline is significantly weaker than what's actually achievable.

This creates a serious problem for the paper's impact. Even if SCG improves UWM by 10% under perturbation, starting from such a low baseline means the absolute numbers will still be uncompetitive. OA-WAM already reaches 84.3% geo-average under perturbation, and UWM might not even match that on standard LIBERO. Reviewers at CoRL will immediately flag why the baseline is so far behind state-of-the-art.

There's also no evidence yet that video-to-action guidance actually helps, despite methods like Fast-WAM, GigaWorld-Policy, and MotuBrain exploring this direction.

The novelty claim itself holds up—applying cross-modal CFG to video-to-action guidance and using spectral filtering for robot control are genuinely new contributions. But the techniques themselves aren't novel: CFG already does selective amplification through CPC theory, and DiffStateGrad already applies SVD-based filtering to guidance in diffusion models. So the core contribution is really just adapting existing methods to this specific problem.

On feasibility, the compute requirements look manageable—around 70-100 hours on H100s, well under the 200-hour budget. The timeline is extremely tight though: 17 days to abstract and 20 to paper, with fine-tuning, diagnostics, calibration, and writing all compressed into a few weeks. It's theoretically possible with significant overlap, but there's almost no buffer for problems.

The research question itself is compelling—it's genuinely worth exploring whether video features are truly dispensable or if the right guidance strategy could make them useful.  But the impact hinges entirely on Phase 1 showing a positive signal, which is far from guaranteed. And there's a deeper concern: the field is already shifting toward implicit world models where this approach wouldn't even apply, so even a successful result might feel somewhat dated.

Looking back at what the previous reviews flagged, most of those issues are still unresolved. The UWM baseline weakness is confirmed, there's no LIBERO-Plus comparison, the null result risk remains high, and the calibration transferability question is still hanging. The field trajectory concern is also valid—this work could be overtaken by the direction the community is moving.

On novelty, the specific combination of techniques is reasonably novel at around 3.5 out of 5.  The core contribution is applying existing methods to a new domain, and while the Phase 1 diagnostic adds value, it's not technically groundbreaking. Feasibility is concerning at 2.5 out of 5—that 79% baseline for UWM is a serious problem, and there's a real risk the proposal doesn't fully account for whether that's a fine-tuned or pretrained number. The null result probability is substantial, and the timeline is extremely tight, though the compute budget itself is manageable. The proposal does score well on clarity at 4 out of 5, with a well-structured two-phase design and honest acknowledgment of limitations. Impact is similarly weak at 2.5 out of 5, constrained by the weak baseline and the uncertainty around whether Phase 1 will even yield positive results.

Averaging these scores gives 3.125, which falls short of the 4.0 threshold. The UWM baseline issue is the critical unresolved blocker—the proposal characterizes it as fine-tuned performance on LIBERO tasks, but there's ambiguity about whether this fully addresses the earlier feedback flagging this as a fundamental problem.

Looking at the proposal more carefully, it plans to fine-tune UWM on LIBERO tasks, yet UWM's fine-tuned result is only 79%—a gap the proposal doesn't explicitly acknowledge. The real question is whether under geometric perturbations, UWM's performance would drop further, potentially creating room for improvement, but the absolute baseline would still be uncompetitive compared to OA-WAM.

Actually, rereading the proposal, it frames the baselines as comparisons within UWM itself—standard policy versus joint denoising with SCG—rather than positioning SCG as a direct competitor to OA-WAM. That's a reasonable framing for a method paper showing consistent improvements, though CoRL reviewers will likely push back on why the stronger backbone wasn't tested. The proposal also references Fast-WAM as another baseline.

If SCG could be applied to Fast-WAM, which hits 97.6% on LIBERO, that would create a much stronger comparison point, but the proposal correctly acknowledges this remains untested. The core tension is whether reviewers will accept this as a proof-of-concept contribution on UWM, given that all WAMs struggle under geometric perturbation—if SCG can lift UWM from around 50% to 65%, that's meaningful progress even if it doesn't match OA-WAM's 84.3%.

The real issue is framing: the paper essentially says "we improved a weaker baseline," which invites skepticism unless the improvement is substantial. And if Phase 1 yields null results, the diagnostic finding about video branches encoding irrelevant information becomes the contribution, which doesn't align with the user's method-only requirement.

I'm settling on a **revise** recommendation since we're at round 6 of 10—there's still time to address the baseline concern directly.

Scoring this out: the novelty is solid at 3.5 for combining cross-modal spectral guidance with WAM robustness in an underexplored space, but it's just existing techniques applied to a new problem. Feasibility drops to 2.5 because UWM's weak 79% fine-tuned performance is a major red flag, the null result risk sits around 40-60%, and the timeline is punishing even if computationally manageable. The writing is exceptionally clear at 4.0—well-structured phases, honest about limitations, thorough landscape review. Impact lands at 3.0: the research question matters, but practical utility is constrained by the weak baseline and architecture-specific approach, though a positive Phase 1 signal would immediately generalize to any WAM. That averages to 3.25, below the 4.0 threshold, so revision is warranted.

Now I'm reviewing what's actually improved versus what's still problematic. The corrections around Fast-WAM, the shift to UWM with principled timestep marginalization, AQC for automatic selection, ICG as a backbone-agnostic method, the two-phase go/no-go structure, and the engagement with CPC theory are all genuine improvements. But the UWM baseline weakness persists as a critical vulnerability, the null result risk remains substantial, and the method's contribution hinges entirely on Phase 1 succeeding. There's also a calibration transferability question that hasn't been resolved. What's becoming clearer is that the proposal treats 79% as if it's a starting point, when it's actually UWM's fine-tuned ceiling—that's a much more serious problem than initially framed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6fb6db4-b6e5-4958-8438-40e053dba6e5",
  "isSidechain": false,
  "requestId": "req_011CauUHsKUDtTrXn3sXmhzX",
  "type": "assistant",
  "uuid": "41e2cac3-937b-4826-b348-fd1ae54f4ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMgHPvNik2a2xLNLmQFAew",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 2478,
      "cache_read_input_tokens": 44599,
      "output_tokens": 5731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 773,
          "output_tokens": 5731,
          "cache_read_input_tokens": 44599,
          "cache_creation_input_tokens": 2478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2478
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

_source line 42 · 2026-05-10T19:54:18.306Z_

Now I have comprehensive evidence. Let me synthesize my findings into the review.

**Key discoveries from my research:**

1. UWM's 79% on LIBERO is the **post-fine-tuning** number (10K steps), not pretraining-only
2. OA-WAM numbers confirmed exactly as claimed (84.3% geo-avg)
3. X-WAM critiques UWM's independent timesteps but their own data shows action quality is barely affected
4. No competing work found combining spectral/SVD filtering with cross-modal guidance for robot control — novelty claim holds
5. CFG-DP exists for single-modal robot diffusion but doesn't overlap

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "Independently verified: no existing work applies cross-modal CFG in video→action direction of WAMs, and no work combines SVD spectral filtering with diffusion guidance for robot control. The specific combination (UWM timestep marginalization + AQC-calibrated spectral filtering) occupies a genuine gap. Slight deduction because the components (CFG, SVD projection, cross-modal guidance) are individually established — novelty is in the principled combination and new domain."},
    "feasibility": {"score": 2, "rationale": "CRITICAL FINDING: UWM achieves only 79% on standard LIBERO AFTER fine-tuning (Table II, arXiv 2504.02792) — this is the post-fine-tuning ceiling, not a pretraining-only number. Individual tasks range 65-93%. Current LIBERO SOTA is 97-99%. Running SCG on a 79% baseline means even significant percentage improvements under perturbation will produce uncompetitive absolute numbers vs. OA-WAM (84.3% geo-avg on LIBERO-Plus). Additionally, null result risk remains ~40-60% given three independent lines of evidence (Fast-WAM, GigaWorld-Policy, MotuBrain) showing video features dispensable at inference."},
    "clarity": {"score": 4, "rationale": "Exceptionally well-structured proposal with honest corrections (Fast-WAM CFG claim), clear two-phase contingent design, comprehensive landscape analysis, and principled engagement with CPC theory limitations. The phased go/no-go structure is a model for risky-but-interesting research."},
    "impact": {"score": 3, "rationale": "The research question (resolving video dispensability vs. geometric vulnerability paradox) is genuinely important for the WAM community. However, practical impact is limited by: (a) weak UWM baseline making absolute results uncompetitive, (b) architecture specificity to explicit video-branch WAMs while the field trends toward implicit world modeling (Being-H0.7), (c) uncertain Phase 1 outcome determining whether the method contribution materializes."}
  },
  "issues": [
    "UWM BASELINE IS 79% AFTER FINE-TUNING — NOT PRETRAINING (CRITICAL): The proposal treats UWM's released LIBERO-90 checkpoint as needing task-specific fine-tuning to reach competitive performance. However, UWM's Table II (arXiv 2504.02792) shows 79% average IS the fine-tuned result (10K gradient steps), with individual tasks ranging 65-93%. This is 20 points below SOTA (Fast-WAM 97.6%, Being-H0.7 99.2%). Even if SCG improves UWM by 10% under geometric perturbation, the absolute numbers will likely remain below OA-WAM's 84.3% geo-avg — and OA-WAM starts from a much stronger standard-LIBERO baseline. CoRL reviewers will immediately question why the backbone is 20 points below contemporary WAMs.",
    "NO LIBERO-PLUS EVALUATION OF UWM EXISTS — BASELINE PERFORMANCE COMPLETELY UNKNOWN: UWM has never been evaluated on LIBERO-Plus. Given its 79% on standard LIBERO, it could plausibly score 40-60% under geometric perturbation. Even a large SCG improvement (e.g., +15%) would leave absolute performance at 55-75%, far below OA-WAM (Camera 80.5%, Robot 89.6%). The proposal must establish UWM's LIBERO-Plus baseline before any SCG work — this takes 5-10h but the results are completely unpredictable and could invalidate the entire experimental plan.",
    "ICG-ON-FAST-WAM AS SECONDARY BACKBONE DOESN'T SOLVE THE PROBLEM: Fast-WAM achieves 97.6% on standard LIBERO, making it a strong baseline candidate. But ICG has never been validated on cross-modal robot control — only on image generation. If ICG produces noisy unconditional estimates on Fast-WAM (likely, since Fast-WAM was not designed for any form of unconditional prediction), the guidance vectors will be unreliable. The proposal correctly notes this as 'itself a novel contribution' but underestimates the risk of it simply not working.",
    "PHASE 1 NULL RESULT DOES NOT SATISFY USER'S METHOD ONLY REQUIREMENT: If Phase 1 shows video→action guidance carries no useful signal under perturbation (40-60% probability given existing evidence), the paper becomes a diagnostic/negative-result contribution. The user explicitly requires 'METHOD ONLY — new inference algorithm.' A negative diagnostic finding, while scientifically valuable, does not meet this constraint and would not satisfy a method-focused CoRL submission.",
    "X-WAM (April 2026) CRITIQUES UWM'S INDEPENDENT TIMESTEP MECHANISM: X-WAM (arXiv 2604.26694) argues that independent timestep sampling creates train/test distribution mismatch, introducing training configurations (t_O < t_a) that never occur at inference. While X-WAM's own ablation shows action quality is barely affected (67.2 vs 67.8 success rate), this architectural concern should be acknowledged. More importantly, X-WAM's Asynchronous Noise Sampling is an alternative mechanism for cross-modal timestep control that should be discussed as a potential alternative backbone.",
    "CALIBRATION TRANSFERABILITY REMAINS UNADDRESSED AFTER TWO ROUNDS OF FEEDBACK: AQC requires ~100 trajectory calibration per task. The proposal mentions cross-task transfer as an ablation but never addresses whether it's realistic. LIBERO has 90+ tasks — if per-task recalibration is needed, the practical overhead is substantial. Previous rounds 4 and 5 both flagged this; the proposal should present a concrete hypothesis about transferability or acknowledge the limitation."
  ],
  "feedback": "The proposal has reached a well-structured, intellectually honest state — the Fast-WAM correction, CPC theory engagement, and two-phase design are commendable. But the UWM baseline problem is now the critical blocker. Here's how to fix it:\n\n**1. RESOLVE THE BACKBONE CRISIS (BLOCKER):** UWM's 79% fine-tuned LIBERO performance is not competitive. Three options:\n\n(a) **Reframe as a proof-of-concept:** Explicitly acknowledge UWM's weaker standard performance and argue that the METHOD is the contribution, not the absolute numbers. Frame as: 'SCG provides X% relative improvement over UWM's own baseline under geometric perturbation, demonstrating the principle of spectral cross-modal guidance. The method is architecture-agnostic and can be applied to stronger WAMs as they release checkpoints.' This is the fastest path but weakest framing.\n\n(b) **Fine-tune UWM more aggressively:** UWM's paper uses 10K steps. Try 50K-100K steps with learning rate sweep — the 180M parameter model is small enough that extended fine-tuning costs only ~10-20h H100 total. If this pushes standard LIBERO to >90%, the baseline becomes acceptable. Check if the UWM repo has any community fine-tuning recipes that achieve better performance.\n\n(c) **Switch to Motus/MotuBrain as backbone:** Motus uses the same UniDiffuser-style independent timesteps as UWM and achieves much stronger performance. MotuBrain (April 2026) reports strong LIBERO results. Check if Motus/MotuBrain checkpoints and LIBERO evaluation code are available — if so, SCG can be applied identically since both use independent timestep marginalization. This is the strongest option if checkpoints exist.\n\n**2. ADD A PHASE-1-INDEPENDENT METHOD GUARANTEE:** To satisfy the METHOD ONLY requirement regardless of Phase 1 outcome, frame SCG as a general 'Spectral Guidance Filtering' framework: even if uniform CFG shows zero benefit, the spectral analysis reveals which guidance dimensions are noise vs. signal, enabling 'sparse guidance' that runs faster (fewer effective dimensions → cheaper guidance computation). This gives a practical speedup contribution independent of robustness improvement.\n\n**3. ADDRESS CALIBRATION TRANSFERABILITY CONCRETELY:** Add a specific experiment: calibrate AQC on 3 LIBERO tasks, evaluate on 3 held-out tasks. If the top-k spectral components are consistent (cosine similarity of selected subspaces >0.8), claim transferability. If not, acknowledge per-task calibration as a limitation but note it requires only ~100 trajectories (~10 minutes of data collection) vs. OA-WAM/CKT-WAM's hours of retraining.\n\n**4. CITE AND DISCUSS X-WAM'S CRITIQUE:** Acknowledge X-WAM's concern about independent timestep sampling but cite their own ablation showing action quality is barely affected. This strengthens the argument for using UWM's marginalization mechanism.\n\n**5. CONSIDER NARROWING TO CAMERA PERTURBATION ONLY:** Camera viewpoint is the perturbation type where video spatial features are most obviously relevant (the camera change directly affects the visual-spatial mapping). Robot initial state is more ambiguous. Focusing Phase 1 on camera perturbation reduces evaluation cost and gives the strongest prior for finding a positive signal.",
  "reason": "UWM's 79% fine-tuned LIBERO performance (confirmed as post-fine-tuning, not pretraining) creates a weak baseline that undermines experimental impact; this critical issue from Round 5 remains unresolved and is now confirmed to be worse than the proposal implies."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e2cac3-937b-4826-b348-fd1ae54f4ad5",
  "isSidechain": false,
  "requestId": "req_011CauUHsKUDtTrXn3sXmhzX",
  "type": "assistant",
  "uuid": "286f6120-e815-4628-923e-1e3a86a2ad59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMgHPvNik2a2xLNLmQFAew",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 2478,
      "cache_read_input_tokens": 44599,
      "output_tokens": 5731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 773,
          "output_tokens": 5731,
          "cache_read_input_tokens": 44599,
          "cache_creation_input_tokens": 2478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2478
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "286f6120-e815-4628-923e-1e3a86a2ad59",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spectral cross-modal guidance WAM proposal",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "286f6120-e815-4628-923e-1e3a86a2ad59",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spectral cross-modal guidance WAM proposal",
  "sessionId": "0f167b53-e63f-46d4-ab31-789b251a64fd"
}
```

---
