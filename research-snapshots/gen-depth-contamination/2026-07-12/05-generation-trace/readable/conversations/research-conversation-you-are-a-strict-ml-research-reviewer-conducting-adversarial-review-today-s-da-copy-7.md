# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/b071fba2-bdbb-4548-baae-7b70d3426cd2.jsonl`
- **Structured JSON:** [`d5acb67c9ffc388c8a51.json`](../../sessions/d5/d5acb67c9ffc388c8a51.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:58:12.681Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:58:12.681Z",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World Action Models (WAMs) — joint world modeling and action prediction in a unified architecture, often built on video diffusion priors. In-scope: unified video+action prediction, MoT (Mixture-of-Transformers) architectures with text/video/action streams, WMs that double as policies via inverse dynamics on imagined futures, action-conditioned video diffusion as policy.\n\nRecent landscape (do not duplicate): UniVLA, DreamVLA, GigaBrain-0.5M, DiT4DiT, MotuBrain, video-diffusion-as-policy lines. WAMs are the hottest CoRL 2026 area — high competition but high reward.\n\nContribution type: METHOD ONLY. New unified architecture, new training scheme that fuses world prediction and action prediction, new inference algorithm extracting actions from imagined futures.\n\nSIM-ONLY MITIGATION: WAM papers at CoRL routinely use sim envs since the method depends on data scale, not real-robot deployment. Use LIBERO/ManiSkill as primary and frame contribution as architectural.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Most challenging budget — video models are heavy. Strategies: (a) fine-tune an open video WM (Cosmos releases, OpenSora, CogVideoX) with action conditioning, (b) distill a large WAM into a smaller one, (c) propose a method that requires only small additional training on top of an existing WAM, (d) propose an inference-time method that needs no training.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos.\n3. Eval: LIBERO, ManiSkill 2/3, RoboCasa for closed-loop control + video prediction quality (PSNR/SSIM/FVD on action-conditioned futures). Compare against UniVLA / DreamVLA / DiT4DiT lineage if open releases exist.\n\nLook for: efficient action-conditioning of video diffusion, latent WAMs that bypass pixel decoding, methods that share representations across world and action streams. Avoid: trivial action-token prepending without architectural insight.\n\nTag: direction=world_action_model, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"VQ-Perceiver World-State Bottleneck for Camera-Viewpoint-Robust Action in MoT WAMs\",\n  \"core_problem\": \"Motus (Tri-model Joint Attention; WAN2.2-5B + Qwen3-VL-2B + action expert, ~7B total; public weights at motus-robotics/Motus on HuggingFace) achieves 87.0% on the unperturbed split of RoboTwin 2.0-Plus (overall average 71.5%) but drops to 21.6% under camera viewpoint perturbation and 43.1% under sensor noise — a 65 percentage-point camera degradation confirmed in arXiv:2603.22078, Table 3. Critically, appearance perturbations cause minimal degradation: lighting 84.6%, background 84.4%, robot initial state 85.0%. The prior proposal's appearance-robustness framing was empirically wrong: the actual published data shows Motus is resilient to lighting and background but catastrophically fragile under camera viewpoint changes. The camera-viewpoint failure implicates Motus's Tri-model Joint Attention design: action tokens jointly attend to raw video tokens in shared self-attention at every transformer layer, so action predictions are directly conditioned on viewpoint-specific pixel spatial arrangements (perspective projections, egocentric depth layout) encoded in those tokens, rather than viewpoint-invariant semantic state (object pose relative to gripper, task phase, contact configuration). When camera position changes, the spatial distribution of video tokens shifts, breaking the learned visual-to-action correlation. Motus's 21.6% is the most severe camera-viewpoint score among all WAMs evaluated in arXiv:2603.22078; LingBot-VA scores 28.9% on RoboTwin 2.0-Plus camera and Cosmos-Policy scores 75.8% on LIBERO-Plus camera, suggesting scale of video pretraining partially mitigates the issue but does not solve it. Motus was included in RoboTwin 2.0-Plus Table 3 results of arXiv:2603.22078 despite being excluded from the paper's WAM taxonomy discussion (its hybrid VLM-action routing architecture places it outside the strict definition), making it the only publicly-weighted MoT WAM with confirmed, severe camera-viewpoint vulnerability available for fine-tuning studies. IMPORTANT EVALUATION NOTE: RoboTwin 2.0-Plus is an in-house benchmark constructed by Huawei/UToronto for arXiv:2603.22078 — no public evaluation code, GitHub repository, or formal camera perturbation parameter specification has been released; the official RoboTwin 2.0 repo (github.com/RoboTwin-Platform/RoboTwin) applies only minor camera jitter (~1 cm) and does not include the viewpoint-pose perturbation measured in 2603.22078. Accordingly, the 21.6% Motus camera score is cited as published motivation for the problem, but RoboTwin 2.0-Plus is designated a secondary evaluation target contingent on author code release or Appendix A re-implementation. LIBERO-Plus (arXiv:2510.13626) is the primary evaluation benchmark: it is fully public, with evaluation code at github.com/sylvestf/LIBERO-plus and dataset at huggingface.co/datasets/Sylvest/LIBERO-plus, defining three camera sub-axes (C1: distance 1.01×–2.00×; C2: spherical position Δθ/Δϕ within 15°–75° cones; C3: orientation yaw/pitch/roll within 2°–10°), and the current camera-axis SOTA is OA-WAM at 80.5% (arXiv:2605.06481, Table 2).\",\n  \"opportunity\": \"The gap: camera viewpoint is Motus's specific, quantified Achilles heel (87.0% unperturbed → 21.6% camera-perturbed on RoboTwin 2.0-Plus, per arXiv:2603.22078). The closest prior work, ReViWo (ICLR 2025), establishes the VQ-for-viewpoint-invariance principle in robotic manipulation: it decomposes visual observations into a VQ-coded view-invariant representation (VIR) and a continuous view-dependent representation (VDR), then trains a COMBO-based world model exclusively on VIR to achieve camera-robust control. This is directly related to our proposal — but four constraints make ReViWo inapplicable to our setting: (a) it requires multi-view training data with known camera labels, collected from MetaWorld simulators; (b) it operates on small-scale COMBO/RSSM world models evaluated on MetaWorld and PandaGym tasks; (c) it applies VQ as an offline preprocessing step external to the policy, not inside the running model; (d) it uses model-based RL, not diffusion-based imitation learning. Our contribution extends the VQ-for-viewpoint-invariance principle to a setting that drops all four constraints: a 7B diffusion-based MoT WAM fine-tuned on single-view demonstrations via intra-model cross-attention routing, evaluated on large-scale benchmarks (LIBERO-Plus primary, RoboTwin 2.0-Plus secondary) with a confirmed, quantified 65pp camera vulnerability. No concurrent work applies intra-model VQ routing within a deployed large-scale diffusion WAM without multi-view training data. The information-bottleneck argument is precisely grounded: camera viewpoint changes alter pixel-level spatial arrangements but leave object identity, task phase, and gripper-object relationships invariant. However, the viewpoint-invariance claim is explicitly framed as an empirical hypothesis, not a guarantee. A K=512 codebook could in principle still encode viewpoint-specific routing if the Perceiver cross-attention queries learn viewpoint-dependent attention patterns. The task-action gradient pressure is the claimed mechanism that discourages this: viewpoint-specific features that do not improve action prediction should be suppressed by task-loss SGD. This hypothesis is directly tested by the UMAP codebook visualization: if codebook clusters organize by task phase and object identity rather than camera angle, the hypothesis is confirmed; if clusters organize by camera angle, the paper pivots to analyzing why discretization does or does not produce viewpoint invariance — still publishable as an analysis contribution with the UMAP evidence and quantified ablation. This requires no camera pose annotations, no multi-view demonstrations, and no test-time knowledge of the camera transformation. Sensor noise robustness is also expected to improve because VQ quantization is inherently denoising: perturbed continuous features map to the same code as their clean counterparts when perturbation magnitude is smaller than nearest-neighbor codebook decision boundaries, directly addressing the 43.1% noise score. The primary contribution framing targets: (a) improving over Motus's baseline on LIBERO-Plus camera axis versus OA-WAM's 80.5% continuous-slot-attention SOTA (arXiv:2605.06481, Table 2), quantifying whether hard VQ discretization adds value over OA-WAM's continuous object-addressable approach; (b) citing the 65pp RoboTwin 2.0-Plus camera gap (21.6%) as published motivation, with secondary evaluation on RoboTwin 2.0-Plus if author code is obtained or Appendix A re-implementation is feasible within timeline. Motus vanilla baseline numbers are already published for RoboTwin 2.0-Plus (camera: 21.6%), saving that baseline run. Motus LIBERO-Plus baseline must be run once (~4h wall clock on 4 H100s).\",\n  \"landscape\": \"Motus (arXiv:2512.13030, TMLR 2025): Tri-model Joint Attention (concatenated self-attention across understanding, video, and action tokens); ~7B (WAN2.2-5B + Qwen3-VL-2B + action expert); public weights; confirmed camera viewpoint score 21.6% on RoboTwin 2.0-Plus (arXiv:2603.22078, Table 3). ReViWo (proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e, ICLR 2025): Representation learning for View-invariant World model; decomposes visual observations into VQ-coded view-invariant representation (VIR) + continuous view-dependent representation (VDR); trains a COMBO-based RL world model on VIR alone; achieves camera-robust manipulation on MetaWorld and PandaGym; real-world ALOHA experiments. Critical prior work establishing the VQ-for-viewpoint-invariance principle. Key limitations relative to this proposal: (a) requires labeled multi-view training data (known camera angles from MetaWorld simulator); (b) small-scale COMBO/RSSM world model, not a 7B diffusion MoT WAM; (c) offline VQ preprocessing step external to the policy, not intra-model routing; (d) model-based RL, not diffusion imitation learning. MotuBrain (arXiv:2604.27792, 2026): H-bridge design (middle 50% layers V-A joint attention, asymmetric at inference); no public pretrained checkpoint — excluded from scope. Fast-WAM (arXiv:2603.16666, 2026): skips video generation at test time for 4× speedup; targets efficiency only. GigaWorld-Policy (arXiv:2603.17240, 2026): causal decoupling for 9× speedup; efficiency only; no geometric robustness improvement. 'Do WAMs Generalize Better than VLAs?' (arXiv:2603.22078, 2026): benchmarks WAM robustness on RoboTwin 2.0-Plus and LIBERO-Plus; introduces RoboTwin 2.0-Plus, which adds seven explicit perturbation axes to RoboTwin 2.0, including camera viewpoint (altering the viewpoint pose of the third-person camera), robot initial configuration, language, lighting, background, sensor noise, and layout — camera viewpoint is absent from the original RoboTwin 2.0 domain-randomization axes; Cosmos-Policy reaches 82.2% overall on LIBERO-Plus and 75.8% on camera split; LingBot-VA: 28.9% camera on RoboTwin 2.0-Plus; Motus: 21.6% camera on RoboTwin 2.0-Plus — worst WAM camera score. CRITICAL AVAILABILITY NOTE: RoboTwin 2.0-Plus is an in-house Huawei/UToronto benchmark with no public evaluation code repository and no published camera perturbation parameter specification; the official RoboTwin 2.0 GitHub (github.com/RoboTwin-Platform/RoboTwin) does not include 2.0-Plus perturbation protocols; reproducing the evaluation requires either author-provided code (corresponding authors: Zhanguang Zhang / Yingxue Zhang at Huawei/UToronto) or re-implementation from Appendix A of arXiv:2603.22078. LIBERO-Plus (arXiv:2510.13626, ICLR 2026): fully public evaluation infrastructure (github.com/sylvestf/LIBERO-plus; dataset at huggingface.co/datasets/Sylvest/LIBERO-plus); drop-in replacement for LIBERO; 10,030 tasks across seven perturbation dimensions with 20,000+ trajectories; camera perturbation covers three sub-axes: C1 (distance 1.01×–2.00×), C2 (spherical position, Δθ/Δϕ within 15°–75° cones), C3 (orientation yaw/pitch/roll within 2°–10°); confirms camera viewpoint causes ~72pp average drop in VLAs; models show resilience to lighting and background; PRIMARY evaluation benchmark for this proposal. MWM (arXiv:2604.19683, 2026): predicts future semantic masks as geometric bottleneck; requires per-frame mask annotations; not applied to MoT WAMs. AnyCamVLA (arXiv:2603.05868, 2026): zero-shot camera viewpoint adaptation via feed-forward novel view synthesis at test time; plug-and-play for VLAs; requires knowing camera transformation at inference; training-free, not learned; not applicable to WAMs without adaptation; evaluated on custom LIBERO-based viewpoint benchmark (not LIBERO-Plus directly), achieving ~94.5% average under large perturbations. 'Dreaming the Unseen' (arXiv:2603.21017, 2026): continuous world-model regularization for OOD robustness; no discrete representations. Being-H0.7 (arXiv:2605.00078, 2026): K=16 latent reasoning queries as soft bottleneck; no VQ discretization — continuous queries can still encode viewpoint-specific features. Reports only aggregate LIBERO-Plus scores (82.1% zero-shot, 84.8% fine-tuned) without any camera-specific breakdown; the paper's claim of 'resilience against shifted viewpoints, novel textures, and sensor noise' is an umbrella inference from the aggregate score, not a disaggregated camera-axis measurement. Evaluated on RoboTwin 2.0 (not RoboTwin 2.0-Plus): clean 90.2%, domain-randomized (Hard) 89.6%; RoboTwin 2.0 domain randomization covers table-top clutter, varied lighting conditions, diverse background textures, tabletop height variations, and diverse language instructions — camera viewpoint/extrinsic perturbation is not among the RoboTwin 2.0 axes; accordingly, Being-H0.7's 89.6% domain-randomized score does not reflect camera-extrinsic robustness as measured by RoboTwin 2.0-Plus's dedicated camera split, and does not undermine the core problem statement. The proposed Perceiver-only ablation (N_ws=64 continuous queries, masking ON) is not architecturally matched to Being-H0.7's K=16 queries; it serves to isolate the contribution of hard VQ discretization at fixed N_ws=64, not to directly replicate Being-H0.7. ARRO (arXiv:2505.08627, 2026): zero-shot segmentation masking at inference; training-free; targets appearance, not camera viewpoint. VILA (arXiv:2601.02994, 2026): view-invariant latent actions (output action space); operates on action representations not visual tokens. GCQ (arXiv:2510.16039, 2025): action-conditioned VQ for spatiotemporal compression in recurrent world models; different target and mechanism. VQ-VLA (ICCV 2025): VQ on output action tokens, not visual representations. OA-WAM (arXiv:2605.06481, 2026): object-addressable cross-attention without discrete compression; camera score 80.5% on LIBERO-Plus (Table 2, arXiv:2605.06481v1 — current SOTA on LIBERO-Plus camera axis, exceeding Cosmos-Policy's 75.8% and π0.5's 75.4%); achieves SOTA on LIBERO-Plus geometric axes (geo avg 84.3%, overall avg 83.9%) via slot-based soft attention — important continuous-bottleneck baseline demonstrating camera robustness is achievable without VQ; comparison against OA-WAM's continuous-slot approach vs. our hard VQ approach is a planned ablation. Note: Being-H0.7 reports a higher overall aggregate score (84.8% fine-tuned) than OA-WAM (83.9%), but does not publish a camera-axis breakdown; OA-WAM's 80.5% remains the only published SOTA reference for the LIBERO-Plus camera axis specifically. X-WAM (arXiv:2604.26694, 2026): Unified 4D World Action Modeling via asynchronous denoising; predicts multi-view RGB-D videos; requires multi-view training data; continuous representations; targets 4D reconstruction and efficiency, not single-view viewpoint invariance; orthogonal. XR-1/UVMC (arXiv:2511.02776, ICLR 2026): dual-branch VQ-VAE with vision branch and motion branch aligned via KL-divergence; offline preprocessing step before model inference, not intra-model routing; targets cross-embodiment generalization via shared codebook, not geometric viewpoint robustness within a running WAM. DIAL (arXiv:2603.29844, 2026): continuous latent visual foresight as structural bottleneck between System-2 (VLM reasoning) and System-1 (action decoder); targets intent decoupling and training instability in VLAs; continuous representations (not discrete); different model type (VLA, not WAM) and different failure mode (training instability, not camera viewpoint brittleness). 'Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning' (arXiv:2510.02268, 2025): conditions ACT, Diffusion Policy, and SmolVLA on Plücker embeddings of camera extrinsics; significantly improves viewpoint generalization; requires known camera extrinsics at both training and test time; no VQ; not applicable to WAMs; orthogonal approach (explicit extrinsic conditioning vs. learned discrete bottleneck requiring no camera pose). No concurrent work extends intra-model VQ discretization of visual token representations within a deployed diffusion-based MoT WAM to address camera viewpoint robustness without multi-view training data.\",\n  \"approach\": \"All experiments use the public Motus checkpoint (~7B: WAN2.2-5B + Qwen3-VL-2B + action expert; motus-robotics/Motus, HuggingFace). The modification has three components: (1) VQ-Perceiver module: N_ws=64 randomly-initialized learnable world-state query vectors perform multi-head cross-attention over the N_video≈256 video tokens output by Motus's video VAE. The N_ws cross-attended outputs are quantized via straight-through VQ-VAE to a jointly-trained codebook of K=512 entries with EMA updates and commitment loss weight λ_vq ramped from 0.01 to 0.25 over the first 5K steps (ramp prevents large commitment gradients from driving codebook collapse before the cross-attention pathway is established). Result: N_ws=64 discrete world-state tokens. (2) Action routing in Motus joint attention: apply an attention mask in Motus's Tri-model Joint Attention so that action tokens cannot directly attend to raw video tokens (action←video path blocked). Video tokens retain full joint attention with understanding tokens and other video tokens; video tokens can still attend to action tokens (preserving action-conditioned video generation). (3) Discrete world-state cross-attention: a dedicated cross-attention sublayer added after each joint attention block allows action tokens to attend exclusively to the N_ws=64 VQ-quantized world-state tokens. Fine-tuning protocol: LoRA (rank=64) applied to all joint attention and new cross-attention layers; VQ-Perceiver initialized randomly; 30K steps on LIBERO + RoboTwin 2.0 demonstrations; combined objective: action rectified-flow diffusion loss + VQ commitment loss. Warm-up schedule: attention masking probability ramped from 0 to 1 over first 5K steps to avoid instability. Training stability monitoring: adding a randomly initialized VQ-Perceiver to a pretrained 7B system risks initialization mismatch — action tokens may find the new cross-attention pathway uninformative relative to the blocked direct video route, resulting in near-zero gradients to the VQ-Perceiver in early training. Two mitigations are added: (a) codebook gradient norm monitoring from step 500 — if VQ-Perceiver cross-attention layer gradient norm is below 10% of the joint attention layer gradient norm at step 2K, the attention masking warm-up is extended from 5K to 10K steps, giving the pathway more time to establish useful routing before full masking is applied; (b) the λ_vq ramp described above. These triggers are implemented as automated training callbacks. PRIMARY evaluation: LIBERO-Plus (github.com/sylvestf/LIBERO-plus; dataset: huggingface.co/datasets/Sylvest/LIBERO-plus) — fully public benchmark with defined camera perturbation protocol (C1/C2/C3 axes, 15°–75° spherical cones). Run Motus LIBERO-Plus baseline once (~4h wall clock on 4 H100s) to establish comparison point; current camera-axis SOTA is OA-WAM at 80.5% (arXiv:2605.06481, Table 2). SECONDARY evaluation: RoboTwin 2.0-Plus — Motus vanilla baseline 21.6% taken from arXiv:2603.22078 Table 3 (no baseline run required). CRITICAL DEPENDENCY: RoboTwin 2.0-Plus evaluation code is NOT publicly available (in-house Huawei/UToronto benchmark from arXiv:2603.22078; no GitHub repo or perturbation parameter specification released). Contingency protocol: (a) Contact corresponding authors Zhanguang Zhang / Yingxue Zhang (Huawei/UToronto) within day 1–2 of project start to request evaluation code or environment snapshot; (b) if code is not obtainable within 2 days, implement RoboTwin 2.0-Plus camera perturbation from Appendix A of arXiv:2603.22078 by adapting LIBERO-Plus's C2 spherical-position protocol to the RoboTwin 2.0 Aloha-Agilex bimanual simulator — estimated 1–2 days of implementation work; (c) if neither is feasible within the CoRL timeline, the paper reports LIBERO-Plus as sole primary evaluation and cites the 21.6% RoboTwin 2.0-Plus score exclusively as published motivation in the introduction. CoRL scope (3 fine-tuning runs): (a) VQ-Perceiver K=512, N_ws=64, attention masking ON (main method); (b) Perceiver-only (continuous soft queries N_ws=64, no VQ, masking ON — ablates discretization; isolates the contribution of hard VQ over continuous routing at fixed N_ws=64; note this uses N_ws=64 continuous queries and is not architecturally matched to Being-H0.7's K=16 latent reasoning queries, so it does not constitute a direct replication of Being-H0.7 — the primary goal is to quantify whether VQ discretization per se improves camera robustness); (c) VQ-Perceiver K=512, N_ws=64, masking OFF (VQ as auxiliary path — ablates routing). ICLR fallback ablations (add 3 more runs): K∈{128,1024}; N_ws∈{16,128}; FSQ variant. Interpretability: UMAP visualization of codebook assignments colored by (i) camera angle, (ii) task phase, (iii) object identity, to verify camera-angle-invariant semantic organization — this is the primary empirical test of the viewpoint-invariance hypothesis. Codebook utilization monitoring from step 500 onward; EMA restart if per-code usage below 1/K² threshold by step 2K.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180–400 H100-hours aggregate (Motus vanilla RoboTwin 2.0-Plus baseline already published; ~4h wall clock × 4 GPUs = ~16 H100-hours for LIBERO-Plus Motus baseline [required, now primary evaluation]; 5–6 fine-tuning runs × ~8–17h wall clock × 4 H100s = ~33–67 H100-hours aggregate per run = ~165–400 H100-hours for runs; ~15–20h wall clock × 1–2 GPUs = ~15–40 H100-hours evaluation; total: ~196–456 H100-hours; best estimate at ~1.5s/step: 5–6 runs × 50h + 56h overhead = ~306–356 H100-hours); RoboTwin 2.0-Plus secondary evaluation adds ~1–2 days researcher implementation time if author code not provided\",\n      \"gpu_utilization\": \"~20–35%; idle between human debug cycles and evaluation inspection\",\n      \"timeline\": \"3–4 months (1 month: implement VQ-Perceiver module, integrate with Motus 7B codebase, unit tests, resolve RoboTwin 2.0-Plus code access; 1.5 months: fine-tuning runs and ablations; 1 month: evaluation, codebook visualization, writing) — targets ICLR 2027\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$540–1800 (180–400h H100 at $3.00–4.50/hr; best estimate ~$918–1602)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~150–230 H100-hours aggregate (3 CoRL runs × ~33–67 H100-hours aggregate per run [~8–17h wall clock on 4 H100s at 1–2s/step] = ~99–200 H100-hours fine-tuning; ~4h wall clock × 4 GPUs LIBERO-Plus baseline = ~16 H100-hours [required primary evaluation]; evaluation overhead ~15–30 H100-hours; total: ~130–246 H100-hours; best estimate at 1.5s/step: 3 × 50h + 36h overhead = ~186 H100-hours; 2 ICLR-fallback ablations if time permits add ~66–134 H100-hours)\",\n      \"gpu_utilization\": \"~55–70%\",\n      \"timeline\": \"5–7 weeks (CoRL 2026 primary: 4–5 weeks compressed if targeting May 28 deadline; day 1–2: contact RoboTwin 2.0-Plus authors for eval code; days 3–4: LIBERO-Plus baseline run + VQ module implementation; remainder: fine-tuning + evaluation)\",\n      \"team\": \"1 researcher, ~30 min/day check-in for ablation configs, camera-split OOD curves, and codebook utilization metrics\",\n      \"claude_api_cost\": \"~$200–350 (~1800–3000 turns for code edits, ablation scheduling, OOD accuracy summaries, codebook analysis)\",\n      \"estimated_gpu_cost\": \"~$450–1107 (150–230h H100 at $3.00–4.50/hr)\",\n      \"risk_note\": \"Codebook collapse requires early monitoring. LoRA rank=64 on 7B: ~8–17h wall clock per run = ~33–67 H100-hours aggregate (at 1–2s/step for video LoRA). Warm-up masking schedule (0→1 over 5K steps) and λ_vq ramp (0.01→0.25 over 5K steps) mitigate training instability. If VQ-Perceiver cross-attention gradient norm < 10% of joint attention layer at step 2K, extend warm-up to 10K steps. If throughput ≥3s/step even after reducing to 20K steps, drop from 3 to 2 fine-tuning runs (main VQ-Perceiver + Perceiver-only ablation), deferring the masking ablation to ICLR fallback scope. RoboTwin 2.0-Plus evaluation is secondary: if author code cannot be obtained within 2 days of project start, LIBERO-Plus is the sole primary benchmark and RoboTwin 2.0-Plus is cited only as published motivation.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~130–236 H100-hours aggregate (Motus vanilla RoboTwin 2.0-Plus baseline from published paper — no run needed; ~4h wall clock × 4 GPUs = ~16 H100-hours for LIBERO-Plus Motus baseline [required primary evaluation]; 3 CoRL-scope fine-tuning runs × ~8–17h wall clock on 4 H100s = ~33–67 H100-hours aggregate per run = ~99–200 H100-hours total fine-tuning; ~5h wall clock × 4 GPUs = ~20 H100-hours evaluation; total: ~135–236 H100-hours aggregate; best estimate at ~1.5s/step: 3 × 50h + 36h overhead = ~186 H100-hours)\",\n      \"gpu_utilization\": \"~80–90%; GPU idle only during checkpoint I/O and rollout evaluation\",\n      \"timeline\": \"4–5 days on 8 H100s (2 parallel runs ≈ 8–17h wall clock + third run serial ≈ 8–17h + baseline ~4h + evaluation ~5h = ~25–43h pure compute wall clock; 4–5 calendar days including setup, monitoring, and iteration), delivering results by May 15–16 — leaving 12–13 days to write for CoRL 2026 (abstract May 26, paper May 28). ADDITIONAL DAY 1 TASK: contact RoboTwin 2.0-Plus authors for evaluation code (Zhanguang Zhang / Yingxue Zhang at Huawei/UToronto); if code not received by day 2, proceed with LIBERO-Plus as sole primary benchmark.\",\n      \"team\": \"0 researchers after ~3–4h initial codebase setup, module integration review, job submission, and author contact for RoboTwin 2.0-Plus code\",\n      \"claude_api_cost\": \"~$350–500 (~3000–4500 turns for code edits, sweep scheduling, camera-split OOD analysis, codebook cluster analysis, paper drafting)\",\n      \"estimated_gpu_cost\": \"~$405–1060 (135–236h H100 at $3.00–4.50/hr; best estimate ~$558–837)\",\n      \"speed_bottleneck\": \"LoRA fine-tuning of ~7B Motus: estimated 1–2s/step for video LoRA on 4 H100s. At 1s/step [optimistic]: ~8.3h wall clock = ~33 H100-hours aggregate per run. At 2s/step [conservative, more typical for video diffusion models]: ~16.7h wall clock = ~67 H100-hours aggregate per run. At 2s/step, 3 fine-tuning runs alone = ~200 H100-hours aggregate — right at the budget ceiling; total with baseline and evaluation rises to ~236 H100-hours. Agent must benchmark step throughput at training step 100 and report: if >1.5s/step, reduce to 20K training steps to remain within ~200 H100-hour budget. If throughput ≥3s/step even at 20K steps (plausible for 7B video diffusion with LoRA rank=64 on 4 H100s — 3s/step × 20K × 4 GPUs = ~66.7 H100-hours/run, 3 runs + overhead ≈ 236 H100-hours at ceiling), reduce from 3 to 2 fine-tuning runs (main VQ-Perceiver + Perceiver-only ablation), dropping the masking ablation to ICLR fallback scope. 2 parallel jobs on 8 H100s is the practical limit. Agent must prioritize: (1) LIBERO-Plus Motus baseline first (~4h wall clock, establishes primary comparison point against OA-WAM 80.5% SOTA); (2) main VQ-Perceiver run; (3) Perceiver-only ablation; (4) masking ablation (if budget permits). If camera score improves substantially from the Motus LIBERO-Plus baseline, paper is ready. If VQ-Perceiver does not beat Perceiver-only, paper pivots to analyzing why discretization helps/hurts — still publishable as an analysis paper. Codebook collapse monitored from step 500; EMA restart if triggered.\",\n      \"risk_note\": \"Codebook collapse requires early monitoring. LoRA rank=64 on 7B: ~33 H100-hours/run (~8h wall clock) at 1s/step; ~67 H100-hours/run (~17h wall clock) at 2s/step. Warm-up masking (0→1 over 5K steps) and λ_vq ramp (0.01→0.25 over 5K steps) mitigate training instability. If VQ-Perceiver cross-attention gradient norm < 10% of joint attention layer gradient norm by step 2K, extend warm-up ramp to 10K steps. RoboTwin 2.0-Plus evaluation is contingent on code availability (in-house Huawei/UToronto benchmark, no public release); contact authors day 1; if no response by day 2, proceed with LIBERO-Plus as primary and cite RoboTwin 2.0-Plus 21.6% as motivation only. Without the public Motus checkpoint or LIBERO-Plus evaluation environment the entire estimate is invalid — verify both before launch (LIBERO-Plus is confirmed public at github.com/sylvestf/LIBERO-plus).\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 26, paper deadline May 28 2026 — 16/18 days from today; PRIMARY TARGET; auto-research delivers results by May 15–16 leaving 12–13 days to write a focused 8-page method paper; scope: main method + 2 ablations + LIBERO-Plus all camera splits [primary] + RoboTwin 2.0-Plus all splits [secondary, contingent on code availability]; robotics + robustness framing is a strong CoRL fit; camera viewpoint is the hardest open WAM problem per arXiv:2603.22078)\",\n    \"ICLR 2027 (deadline ~September–October 2026 — fallback if CoRL timeline is missed; expand ablation suite to K, N_ws, FSQ variants; add full LIBERO-Plus evaluation across all splits; stronger representation-learning framing with ReViWo as explicit prior work to extend)\",\n    \"CVPR 2027 (deadline ~November 2026 — tertiary fallback if visual robustness framing dominates over robotics systems contribution)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Motus: A Unified Latent Action World Model (arXiv:2512.13030, TMLR 2025) — target model; ~7B (WAN2.2-5B + Qwen3-VL-2B + action expert); public weights (motus-robotics/Motus on HuggingFace); Tri-model Joint Attention design; camera viewpoint score 21.6% on RoboTwin 2.0-Plus\",\n    \"Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv:2603.22078, 2026) — source of Motus camera score (21.6% camera, 87.0% unperturbed split, 71.5% overall average), LingBot-VA camera score (28.9%), Cosmos-Policy LIBERO-Plus scores (camera 75.8%, total 82.2%); confirms camera viewpoint is the dominant WAM robustness gap; introduces RoboTwin 2.0-Plus, which adds seven explicit perturbation axes (camera, robot, language, light, background, noise, layout) to the original RoboTwin 2.0 — camera viewpoint extrinsic perturbation is a RoboTwin 2.0-Plus axis and is absent from RoboTwin 2.0 domain randomization. AVAILABILITY NOTE: RoboTwin 2.0-Plus is an in-house Huawei/UToronto benchmark with no public evaluation code release; the official RoboTwin 2.0 GitHub does not include 2.0-Plus camera perturbation protocols; reproduction requires author-provided code or Appendix A re-implementation.\",\n    \"ReViWo: Learning View-invariant World Models for Visual Robotic Manipulation (proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e, ICLR 2025) — critical direct predecessor establishing VQ-for-viewpoint-invariance principle; decomposes observations into VQ-coded view-invariant representation (VIR) + continuous view-dependent representation (VDR); trains COMBO-based world model on VIR; requires labeled multi-view training data from MetaWorld simulators; small-scale RSSM world model on MetaWorld/PandaGym; real-world ALOHA experiments; our proposal extends this principle to 7B diffusion MoT WAMs with single-view demonstrations via intra-model cross-attention routing\",\n    \"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv:2510.13626, ICLR 2026) — PRIMARY benchmark used for evaluation; fully public evaluation infrastructure (github.com/sylvestf/LIBERO-plus; dataset at huggingface.co/datasets/Sylvest/LIBERO-plus); confirms camera viewpoint causes ~72pp average drop in VLAs; camera perturbation covers three sub-axes: C1 (distance 1.01×–2.00×), C2 (spherical position Δθ/Δϕ within 15°–75° cones), C3 (orientation yaw/pitch/roll within 2°–10°); models show resilience to lighting and background\",\n    \"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust VLAs (arXiv:2603.05868, 2026) — closest camera robustness baseline; test-time novel view synthesis; training-free; requires known camera transformation at inference; not architectural; not applicable to WAMs without adaptation; evaluates on custom LIBERO-based viewpoint protocol (not LIBERO-Plus directly)\",\n    \"XR-1/UVMC: Unified Vision-Motion Codes for Cross-Embodiment Robot Learning (arXiv:2511.02776, ICLR 2026) — closest VQ-based competitor after ReViWo; dual-branch VQ-VAE aligning visual dynamics and robot motion codes via KL-divergence; offline preprocessing, not intra-model routing; targets cross-embodiment generalization, not camera viewpoint robustness within a deployed WAM\",\n    \"DIAL: Latent Visual Foresight as Structural Bottleneck (arXiv:2603.29844, 2026) — continuous latent bottleneck between VLM reasoning and action in VLAs; different model type (VLA not WAM), continuous not discrete, targets intent decoupling not camera robustness\",\n    \"Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv:2604.19683, 2026) — geometric bottleneck baseline via semantic mask prediction; requires per-frame mask annotations; not applied to MoT WAMs\",\n    \"Fast-WAM (arXiv:2603.16666, 2026) — efficiency baseline; skips video generation at inference; does not improve geometric robustness\",\n    \"GigaWorld-Policy (arXiv:2603.17240, 2026) — causal decoupling for 9× speedup; efficiency baseline; does not improve geometric robustness\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078, 2026) — soft continuous latent query baseline; K=16 latent reasoning queries (confirmed from training details section of arXiv:2605.00078v1); no VQ discretization; continuous queries can still encode viewpoint-specific features. Reports only aggregate LIBERO-Plus scores (82.1% zero-shot / 84.8% fine-tuned) without any camera-specific breakdown; the paper's claim of 'resilience against shifted viewpoints, novel textures, and sensor noise' is an umbrella inference from the aggregate score, not a disaggregated camera-axis measurement — OA-WAM (arXiv:2605.06481) is the only published result with a dedicated LIBERO-Plus camera split score (80.5%), making it the appropriate SOTA reference for the camera axis. Evaluated on RoboTwin 2.0 (not RoboTwin 2.0-Plus): clean 90.2%, domain-randomized (Hard) 89.6%; RoboTwin 2.0 domain randomization covers table-top clutter, varied lighting conditions, diverse background textures, tabletop height variations, and diverse language instructions — camera viewpoint/extrinsic perturbation is not among these axes; Being-H0.7's 89.6% score therefore does not reflect camera-extrinsic robustness as measured by RoboTwin 2.0-Plus's dedicated camera split. The proposed Perceiver-only ablation (run b: N_ws=64 continuous queries, masking ON) is not architecturally matched to Being-H0.7's K=16 queries; it isolates the contribution of hard VQ discretization at fixed N_ws=64, not a direct replication of Being-H0.7.\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, 2026) — object-addressable slot cross-attention without discrete compression; camera score 80.5% on LIBERO-Plus (Table 2, arXiv:2605.06481v1 — current SOTA on LIBERO-Plus camera axis, exceeding Cosmos-Policy's 75.8% and π0.5's 75.4%; geo avg 84.3%, overall avg 83.9%); achieves state-of-the-art on LIBERO-Plus geometric axes via continuous slot attention; important baseline showing continuous-attention approaches can achieve camera robustness; comparison against OA-WAM's soft approach vs. our hard VQ approach is a planned ablation clarifying when discrete VQ adds value over continuous slot routing. Note: Being-H0.7 reports a higher overall aggregate score (84.8% fine-tuned) but publishes no camera-axis breakdown; OA-WAM 80.5% is the only published camera-specific SOTA on LIBERO-Plus.\",\n    \"X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694, 2026) — 4D WAM predicting multi-view RGB-D videos; requires multi-view training data; continuous representations; targets reconstruction efficiency; orthogonal to single-view VQ camera-invariance approach\",\n    \"'Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning' (arXiv:2510.02268, 2025) — conditions behavior cloning policies (ACT, Diffusion Policy, SmolVLA) on Plücker embeddings of camera extrinsics; improves viewpoint generalization; requires known camera extrinsics at test time; no VQ; not applicable to WAMs; orthogonal approach (explicit extrinsic conditioning vs. learned implicit bottleneck)\",\n    \"ARRO: Augmented Reality for Robots (arXiv:2505.08627, 2026) — training-free visual robustness baseline; zero-shot masking; targets appearance not geometric robustness\",\n    \"VILA: Learning to Act Robustly with View-Invariant Latent Actions (arXiv:2601.02994, 2026) — view-invariant latent action pretraining; acts on action representations not visual tokens; output-space approach vs. our input-routing approach\",\n    \"GCQ: Grid-like Code Quantization (arXiv:2510.16039, 2025) — action-conditioned VQ for temporal compression in recurrent world models; different target and mechanism\",\n    \"VQ-VLA: Improving VLA Models via Scaling Vector-Quantized Action Tokenizers (ICCV 2025) — VQ on output action tokens, not input visual representations; orthogonal\",\n    \"Perceiver IO: A General Architecture for Structured Inputs and Outputs (ICML 2022) — architectural basis for world-state query cross-attention module\",\n    \"Neural Discrete Representation Learning [VQ-VAE] (NeurIPS 2017) — VQ training recipe; commitment loss; EMA codebook updates\",\n    \"Mastering diverse control tasks through world models [DreamerV3] (Nature 2025) — existence proof that discrete latent state in world models can outperform continuous; analogous motivation; ReViWo's COMBO world model is related\",\n    \"lucidrains/vector-quantize-pytorch — open-source VQ, FSQ, RVQ implementations; reduces implementation risk\"\n  ],\n  \"description\": \"We extend the VQ-for-viewpoint-invariance principle established by ReViWo (ICLR 2025) from small-scale RL world models to modern diffusion-based MoT WAMs, introducing a novel intra-model routing mechanism — the VQ-Perceiver world-state bottleneck — that requires no multi-view training data and directly targets a confirmed 65pp camera vulnerability in the only publicly-weighted large-scale MoT WAM. Specifically: Motus achieves 87.0% on the unperturbed split of RoboTwin 2.0-Plus (overall average 71.5%) but drops to 21.6% under camera viewpoint perturbation (arXiv:2603.22078, Table 3), while appearance perturbations cause negligible degradation (lighting 84.6%, background 84.4%). ReViWo (ICLR 2025) established that VQ-coded view-invariant representations support camera-robust robot control, but required labeled multi-view training data, operated on small COMBO/RSSM world models on MetaWorld/PandaGym, and applied VQ as offline preprocessing external to the policy. Our architectural contribution adapts this principle to the 7B fine-tuning setting: N_ws=64 learnable world-state queries cross-attend to N_video≈256 video tokens, and each query output is VQ-quantized to one of K=512 codebook entries trained jointly with Motus's action diffusion objective. In modified Motus joint attention, action tokens' direct access to raw video tokens is masked; action tokens instead attend exclusively to the N_ws=64 discrete world-state tokens via a dedicated cross-attention sublayer. The viewpoint-invariance claim is framed as an empirical hypothesis — the finite vocabulary cannot memorize viewpoint-specific pixel patterns under task-action gradient pressure — with the UMAP codebook visualization (planned) as the primary empirical test. Key differentiators: unlike AnyCamVLA (test-time view synthesis, requires known camera transform at inference), the contribution is learned and requires no additional inference-time inputs; unlike Being-H0.7 (K=16 continuous queries, which can still encode viewpoint-specific interpolations and reports only aggregate LIBERO-Plus scores without camera-axis breakdown), hard VQ prevents viewpoint-specific feature encoding; unlike ReViWo (multi-view training data required), single-view demonstrations only; unlike UVMC/XR-1 (offline preprocessing for cross-embodiment), this modifies intra-model routing within a deployed WAM. PRIMARY evaluation: LIBERO-Plus (fully public; github.com/sylvestf/LIBERO-plus), targeting improvement over Motus baseline and comparison against OA-WAM's 80.5% camera-axis SOTA (arXiv:2605.06481, Table 2) — the only published camera-specific SOTA on this benchmark (Being-H0.7 reports only aggregate scores without camera-axis breakdown). SECONDARY evaluation: RoboTwin 2.0-Plus (contingent on code availability from Huawei/UToronto authors or Appendix A re-implementation within timeline); 21.6% Motus camera score cited as published motivation regardless. Motus vanilla LIBERO-Plus baseline run required (~4h on 4 H100s); ~7B model; 3 focused runs within ~130–236 H100-hours aggregate (~8–17h wall clock per run on 4 H100s at 1–2s/step); CoRL 2026 primary target.\",\n  \"project_name\": \"vq_perceiver_world_state_wam\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL ARCHITECTURAL MISMATCH: The core premise — 'action stream cross-attends over hundreds of raw continuous video latent tokens' — does not match target architectures. MotuBrain explicitly uses decoupled layers where video and action streams do NOT perform joint attention, with cross-modal sharing only in a short joint-denoising prefix. Motus uses Tri-model Joint Attention (shared self-attention across three modalities), not a separate cross-attention K/V interface. Inserting a VQ bottleneck into the video→action K/V projections assumes a structural interface that does not exist in either target model.\", \"CRITICAL EFFICIENCY CLAIM IS WRONG: The proposal states 'the action stream attends over K=512 fixed codebook vectors instead of N_video≈256–1024 raw tokens, reducing cross-attention FLOPs by 2–4×.' This is incorrect. Applying straight-through VQ to N_video projected K/V vectors still passes N_video quantized vectors to the cross-attention — the sequence length is unchanged. FLOPs reduction to O(K) would require an additional deduplication/aggregation step (group all tokens assigned to the same code and replace with one representative), which is not described anywhere in the proposal.\", \"CRITICAL COMPUTE CONSTRAINT VIOLATED: Auto-research mode estimates 700–900 H100-hours (3.5–4.5× over the ≤200 H100-hour hard limit). HIL mode estimates 320 H100-hours (1.6× over limit). Only manual mode (~200 H100-hours) respects the budget, but manual mode takes 3–5 months — incompatible with the 20-day CoRL deadline.\", \"COMPETING WORK ADDRESSES SAME EFFICIENCY PROBLEM BETTER: Fast-WAM (arXiv:2603.16666, Mar 2026) skips video generation entirely at test time, achieving 4× speedup with near-identical accuracy. GigaWorld-Policy (arXiv:2603.17240, Mar 2026) uses causal decoupling to prevent video tokens from influencing action tokens at inference, achieving 9× speedup over Motus. Both are simpler and more impactful than inserting VQ at the cross-attention interface.\", \"OVERLAPPING CONCURRENT WORK: GCQ — Grid-like Code Quantization (arXiv:2510.16039, Oct 2025) — proposes an action-conditioned VQ codebook for discrete world-model representations, performing spatiotemporal compression for long-horizon prediction and inverse modeling. This directly overlaps with the proposed VQ-for-world-state-discretization angle and must be discussed/differentiated.\", \"PRIMARY TARGET MODEL HAS NO PUBLIC WEIGHTS: No public MotuBrain pretrained checkpoint was found. Motus does have public weights (motus-robotics/Motus on HuggingFace), but Motus's architecture (Tri-model Joint Attention) does not expose the assumed cross-attention K/V interface. Falling back to Motus requires first verifying that its architecture can accommodate the proposed modification at all.\", \"WEAK DreamerV3 ANALOGY: DreamerV3's discrete representations are categorical latent states in a recurrent SSM (RSSM), used for world-state rollout in model-based RL — not for cross-attention K/V in a diffusion transformer. The analogy requires stronger theoretical grounding to justify why discretizing K/V projections specifically should improve generalization versus continuous K/V with appropriate regularization.\"]\nFeedback: The seed insight — that a discrete semantic bottleneck between the world-model and action streams could improve generalization — has intellectual merit, but the proposal must be rebuilt on accurate architectural foundations before it can be defensible.\n\n1. VERIFY ARCHITECTURE FIRST: Before writing another line of the proposal, fetch the full HTML of arXiv:2512.13030 (Motus) and arXiv:2604.27792 (MotuBrain) and identify precisely where/whether the action stream cross-attends over video K/V vectors. If it does not (shared self-attention in Motus, decoupled layers in MotuBrain), the modification cannot be implemented as described. Consider targeting a model where the interface actually exists, or propose adding a cross-attention layer that can then be quantized.\n\n2. CORRECT THE EFFICIENCY CLAIM: Either (a) describe a deduplication mechanism that achieves true O(K) attention (assign N_video tokens to codes, pool per-code, attend over active codes only — similar to slot attention or Perceiver IO), or (b) drop the efficiency framing entirely and position the contribution as a generalization/robustness benefit from semantic discretization, leaving efficiency to Fast-WAM/GigaWorld-Policy.\n\n3. DIFFERENTIATE FROM GCQ (arXiv:2510.16039): GCQ applies action-conditioned VQ for world-model compression. Explain precisely how the proposed approach differs: VQ is applied at the K/V interface of a diffusion MoT rather than as a compression stage before the model, and the codebook is learned jointly with the diffusion objective rather than separately.\n\n4. PIVOT TO MOTUS ONLY: Motus has public weights; target it exclusively. Verify that after the architectural fix the modification is implementable within Motus's Tri-model Joint Attention design, possibly by inserting an explicit cross-attention layer between quantized video representations and the action expert.\n\n5. FIX COMPUTE ESTIMATES: Cap all modes at ≤200 H100-hours. The auto-research estimate (700–900 H100-hours) should be reduced to a focused ablation sweep (3–4 runs of ~40 H100-hours each). Be honest that CoRL 2026 requires pre-existing preliminary results; ICLR 2027 is the realistic primary target.\n\n6. REFRAME THE CONTRIBUTION: Given Fast-WAM and GigaWorld-Policy already solve inference efficiency, the differentiating story must be 'discrete world-state bottleneck improves out-of-distribution generalization (lighting, background clutter)' measured through OOD generalization splits in LIBERO-Spatial and ManiSkill. This is testable within compute budget and is not covered by either Fast-WAM or GigaWorld-Policy.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: The user's primary requirement is CoRL 2026 (abstract deadline May 26, paper deadline May 29, 2026 — 17/20 days from today). The proposal explicitly lists CoRL 2026 as 'not feasible without pre-existing results; skip' and targets ICLR 2027 instead. This directly fails the user's stated requirement. Auto-research mode estimates 5–7 days of experiments on 8 H100s, which would deliver results by May 15–17, leaving 12–14 days to write the paper — tight but potentially achievable for a focused method submission. The proposal must either (a) attempt CoRL 2026 with a minimal experiment set, or (b) explicitly explain to the user why CoRL 2026 is infeasible and ask for venue guidance before proceeding.\", \"CRITICAL PROBLEM PREMISE UNVERIFIED: The proposal asserts 'SOTA models degrade from ~98% to 0–40% under visual perturbations' and positions Motus as the target model with this problem. But arXiv:2603.22078 shows that Cosmos-Policy — trained on large-scale video data, as Motus is — achieves 82–96% on visual appearance perturbations (lighting, noise, layout) on LIBERO-Plus. The proposal never reports Motus's specific LIBERO-Plus performance on visual splits. If Motus (with WAN2.2 video pretraining on large-scale data) already achieves comparable robustness to Cosmos-Policy on these splits, the proposed fix addresses a non-problem for this base model. The proposal must retrieve and report Motus's actual LIBERO-Plus visual perturbation numbers before proceeding.\", \"MISSING KEY COMPETITOR — XR-1/UVMC (arXiv:2511.02776, ICLR 2026): XR-1 introduces Unified Vision-Motion Codes (UVMC), a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion into a shared discrete codebook, enabling cross-embodiment transfer. This is the closest published work to the proposed VQ-Perceiver and is completely absent from the landscape. The differentiation (UVMC: joint codebook for cross-embodiment pretraining; proposed: VQ bottleneck for intra-model visual-to-action routing at inference) is valid but must be made explicit in the paper.\", \"MISSING DIAL (arXiv:2603.29844): DIAL introduces 'latent visual foresight within the VLM feature space as a structural bottleneck' between reasoning and action — the same conceptual goal as the proposed VQ-Perceiver, using continuous rather than discrete representations. The distinction (continuous vs. hard VQ discretization; DIAL targets intent decoupling while proposed targets appearance invariance) must be stated. Omitting DIAL leaves a major gap in the literature review.\", \"WRONG ROBUSTNESS TARGET: From arXiv:2603.22078, WAMs exhibit strong robustness to the visual appearance perturbations the proposal targets (lighting, background, color), but fail on geometric perturbations (camera viewpoint: 28.9%, robot initial state: 36.2%). A VQ-Perceiver that encodes object pose and contact configuration should in principle also help with task-phase geometry; if the proposal can argue that the VQ codebook helps geometric perturbations (not just appearance), the contribution would be substantially stronger and better-targeted.\", \"MODEL SIZE DISCREPANCY: The proposal repeatedly references '5B-parameter Motus' but the confirmed HuggingFace release shows Motus is WAN2.2-5B (video backbone) + Qwen3-VL-2B (understanding) + action expert — total ~7–8B parameters. The compute estimate of ~25–30h per run on 4 H100s for 30K LoRA steps is still plausible but must be re-verified against the actual model size. LoRA rank=64 on 7B is heavier than on 5B, potentially adding ~20% to each run.\"]\nFeedback: The Round 1 architectural errors are cleanly fixed. The proposal now has the correct Motus architecture, corrected compute estimates within the ≤200 H100-hour budget, and removed the spurious efficiency claim. Three new issues must be resolved before this can proceed.\n\n1. VENUE DECISION REQUIRED: Do not silently retarget to ICLR 2027. Either (a) restructure the experiment plan to target CoRL 2026 — auto-research mode gives 5–7 days of results, leaving 12–14 days to write a focused method paper; use only baseline + 2 key ablations (VQ vs. continuous, with/without attention mask) on LIBERO-Plus; this is aggressive but consistent with the user's explicit constraint; or (b) surface the venue conflict to the user and ask whether to proceed with CoRL 2026 or ICLR 2027 before investing further in the idea.\n\n2. VERIFY MOTUS BASELINE FIRST: Before any fine-tuning, run the unmodified Motus checkpoint through LIBERO-Plus visual perturbation splits (background, lighting, color). If Motus already achieves >70% (consistent with Cosmos-Policy at 82%), the problem statement collapses. If it achieves <50%, the case is strong. This single baseline run (~3–4h on 4 H100s) is the prerequisite for the entire paper.\n\n3. ADD UVMC/XR-1 AND DIAL TO LANDSCAPE: Add 'XR-1/UVMC (arXiv:2511.02776, ICLR 2026) — dual-branch VQ-VAE jointly encoding visual dynamics and robot motion into a shared codebook; targets cross-embodiment transfer, not intra-model visual-to-action routing.' Add 'DIAL (arXiv:2603.29844, 2026) — continuous latent visual foresight as structural bottleneck between reasoning and action; no VQ; targets intent/action decoupling, not appearance invariance.' Both are close in spirit; explicit differentiation strengthens the novelty claim.\n\n4. REFRAME AROUND GEOMETRIC ROBUSTNESS: The evidence shows geometric perturbations (camera viewpoint, robot state) are the dominant gap for WAMs. Argue that the VQ codebook encodes task-phase state (object pose, contact configuration) that is inherently viewpoint-invariant — making the bottleneck relevant to geometric robustness as well. Add camera-viewpoint and robot-initial-state splits to the LIBERO-Plus evaluation table. This reframe makes the contribution significantly more impactful.\n\n5. CORRECT MODEL SIZE: Update '5B-parameter Motus' to '~7B (WAN2.2-5B + Qwen3-VL-2B)' throughout the proposal and recalculate per-run compute accordingly (~30–35h on 4 H100s instead of ~25–30h, still within the ≤200 H100-hour budget for 5–6 runs).\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING PRIOR WORK — ReViWo (ICLR 2025): 'Learning View-Invariant World Models for Visual Robotic Manipulation' (proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e) explicitly applies VQ-VAE to decompose visual observations into view-invariant (VIR) and view-dependent (VDR) representations, then trains world models on VIR for camera-robust robot manipulation. The proposal claims 'no concurrent work applies hard VQ discretization to visual token representations...to address camera viewpoint robustness' — this claim is false. ReViWo must be added to the landscape section and the novelty claim must be reformulated around what is genuinely new: applying this principle within a modern diffusion-based 7B MoT WAM via intra-model cross-attention routing, without multi-view training data.\", \"COMPUTE ESTIMATE INTERNAL INCONSISTENCY: The auto-research mode states '3 CoRL-scope fine-tuning runs × ~30–35h each on 4 H100s' but quotes a total of '~120–145h H100.' Under the natural reading (30–35h wall clock on 4 H100s), the H100-hours per run = 4 × ~33h ≈ 132 H100-hours, and 3 runs = ~396 H100-hours — nearly 2× the 200 H100-hour hard limit. The budget is only satisfied if '30–35h on 4 H100s' means 30–35 aggregate H100-hours (~8h wall clock), but the 'speed bottleneck' note and '5–6 days on 8 H100s' timeline are inconsistent with 8h-per-run wall clock. This ambiguity must be resolved with explicit wall-clock vs. aggregate-GPU-hours distinction.\", \"STANDARD EVALUATION FIGURE MISREPRESENTED: The proposal states 'Motus achieves 87.0% on RoboTwin 2.0-Plus standard evaluation.' The confirmed overall average from arXiv:2603.22078 Table 3 is 71.5%, not 87.0%. The 87.0% is the unperturbed (standard-scene, no-perturbation) split score within RoboTwin 2.0-Plus. This distinction matters: it should be stated as 'Motus achieves 87.0% on the unperturbed split of RoboTwin 2.0-Plus (overall average 71.5%)' to avoid misleading reviewers who check the source paper.\", \"VQ-INVARIANCE ARGUMENT NEEDS STRENGTHENING: The claim that 'a VQ codebook with K=512 entries cannot memorize viewpoint-specific pixel patterns' is intuitive but not rigorous — 512 codes can still encode many viewpoint configurations if the Perceiver cross-attention queries learn viewpoint-specific routing. The proposal should either (a) add a theoretical bound showing that the number of training viewpoints exceeds K (information-theoretic argument), or (b) explicitly frame this as an empirical hypothesis, with codebook UMAP visualization (already planned) as the primary evidence for viewpoint-invariant clustering.\", \"RANDOMLY INITIALIZED VQ-PERCEIVER IN PRETRAINED SYSTEM — TRAINING RISK: Adding a randomly initialized VQ-Perceiver module (N_ws=64 cross-attention queries + K=512 codebook + commitment loss) to a pretrained 7B Motus via LoRA introduces a significant initialization mismatch. The LoRA adapters on joint attention layers must simultaneously (a) route information through the new masked pathway and (b) suppress the old video-to-action direct pathway, while the VQ-Perceiver is learning from scratch. The 5K-step warm-up schedule helps, but this is a potential training instability not acknowledged beyond the collapse monitoring note. The proposal should discuss the risk that the VQ-Perceiver is simply ignored by the model (learns near-zero cross-attention weights) during early training.\"]\nFeedback: The proposal has made strong progress in three rounds and is close to a passable state. The two changes required for a pass verdict are: (1) Add ReViWo (ICLR 2025) to the landscape and reformulate the novelty claim honestly. The correct framing is: 'We extend the VQ-for-viewpoint-invariance principle (ReViWo, ICLR 2025) from small-scale world models to modern diffusion-based MoT WAMs, introducing a novel intra-model routing mechanism (VQ-Perceiver cross-attention replacing raw video attention in Motus 7B) that requires no multi-view training data and directly targets a confirmed 65pp camera vulnerability in the only publicly-weighted large-scale MoT WAM.' This is a strong and honest novelty statement. (2) Fix the compute estimate ambiguity by explicitly separating wall-clock hours from aggregate H100-hours. Concretely: state '~8–10h wall clock per run on 4 H100s = ~32–40 H100-hours per run; 3 CoRL runs = ~96–120 H100-hours; LIBERO-Plus baseline ~4h wall clock × 4 GPUs = ~16 H100-hours; evaluation ~5h × 4 = 20 H100-hours; total ~132–156 H100-hours.' If the actual step time is closer to 2s/step (more typical for video models), restate as ~66 H100-hours/run and flag that 3 runs = ~198 H100-hours, right at the limit. Either way, commit to a single unambiguous number. The other issues (standard evaluation phrasing, VQ invariance argument, initialization risk) are lower priority but should be addressed: rephrase '87.0% on standard evaluation' as '87.0% on the unperturbed split (71.5% overall)'; add a sentence noting that the UMAP codebook visualization is the empirical test of the viewpoint-invariance hypothesis; and mention in the approach section that if the VQ-Perceiver receives near-zero gradients in early steps the warm-up masking will be extended.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"FACTUAL ERROR — Being-H0.7 query count: The proposal states 'N_q=64 learnable continuous latent queries' for Being-H0.7 (arXiv:2605.00078), but the actual paper uses K=16 latent reasoning queries. This misrepresentation would be caught immediately by any reviewer who reads Being-H0.7. The Perceiver-only ablation is described as 'directly isolates the value of hard VQ vs. Being-H0.7's continuous-query approach' — but N_ws=64 vs. K=16 means the ablation is not architecturally aligned with Being-H0.7 after all, which needs to be acknowledged.\", \"MISSING OA-WAM CAMERA SCORE: The landscape says OA-WAM 'achieves state-of-the-art on LIBERO-Plus geometric axes' but omits its specific camera score of 80.5%. This is the critical number reviewers will check. OA-WAM's 80.5% exceeds Cosmos-Policy's 75.8% (which IS quoted) and represents the current SOTA on LIBERO-Plus camera. The proposal must state this explicitly and frame the goal as beating 80.5% (on LIBERO-Plus) and closing the gap from 21.6% on RoboTwin — rather than implying Cosmos-Policy's 75.8% is the comparison target.\", \"BEING-H0.7 ROBOTTWIN PERFORMANCE UNADDRESSED: Being-H0.7 achieves 90.2% clean and 89.6% domain-randomized on RoboTwin 2.0. The proposal's landscape omits these numbers entirely. If 'domain-randomized' in Being-H0.7's evaluation includes camera viewpoint perturbation, the core problem (camera robustness is unsolved for WAMs) would be partially undermined. The proposal must clarify the distinction between RoboTwin 2.0 (Being-H0.7's evaluation protocol) and RoboTwin 2.0-Plus (arXiv:2603.22078's evaluation protocol with explicit camera viewpoint splits) to establish that the 21.6% Motus score refers to the latter.\", \"COMPUTE WORST-CASE MISSING: The proposal handles the 2s/step scenario via step reduction to 20K, but does not address the ≥3s/step scenario (plausible for a 7B video diffusion model with LoRA rank=64 and 4 H100s). At 3s/step × 20K steps × 4 GPUs = 66.7 H100-hours/run; 3 runs + overhead = ~236 H100-hours — exactly at the ceiling. A brief statement acknowledging this risk and the fallback (reduce to 2 runs if >3s/step) would close this gap.\"]\nFeedback: The proposal has made strong progress through four rounds and is close to passing. The four remaining issues are all fixable in a quick revision: (1) Correct Being-H0.7's query count to K=16 and acknowledge the architectural mismatch with the proposed N_ws=64 ablation — reframe the ablation as 'hard VQ N_ws=64 vs. continuous Perceiver N_ws=64' rather than direct comparison with Being-H0.7. (2) State OA-WAM's specific camera score of 80.5% on LIBERO-Plus as the current SOTA baseline, not Cosmos-Policy's 75.8% — the contribution framing should be 'VQ-Perceiver on Motus targets: (a) closing the 65pp RoboTwin camera gap from 21.6%, and (b) comparing against OA-WAM's 80.5% continuous-attention SOTA on LIBERO-Plus.' (3) Add one sentence clarifying that Being-H0.7's 89.6% domain-randomized RoboTwin 2.0 score uses visual randomization (texture/lighting) not camera extrinsic perturbation, unlike the RoboTwin 2.0-Plus camera split in arXiv:2603.22078 — this preserves the validity of the core problem statement. (4) Add a single sentence fallback for the ≥3s/step scenario: reduce from 3 to 2 fine-tuning runs (main method + VQ-vs-continuous ablation), dropping the masking ablation to ICLR fallback. All four fixes are <1 paragraph each and do not require re-architecting the proposal.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL EVALUATION DEPENDENCY UNVERIFIED: RoboTwin 2.0-Plus — the primary benchmark cited for Motus's 21.6% camera score — is an in-house benchmark constructed by Huawei/UToronto authors (arXiv:2603.22078), NOT an official release of the RoboTwin 2.0 platform. The official RoboTwin 2.0 repo (github.com/RoboTwin-Platform/RoboTwin) applies only minor camera jitter (1 cm), not the major viewpoint-pose perturbation measured in 2603.22078. No GitHub code for RoboTwin 2.0-Plus was found. The proposal explicitly states 'RoboTwin 2.0-Plus all 7 perturbation splits (camera viewpoint is the primary metric)' as the primary evaluation, but if the evaluation code is not available, the VQ-Perceiver team cannot run inference on VQ-Perceiver-Motus against the same 21.6% baseline they borrowed from the published paper. This makes the primary metric unreplicable without author contact or re-implementation from Appendix A — an undisclosed dependency that adds 1-2 days of implementation work to an already compressed 20-day timeline.\", \"MODERATE COMPARISON AMBIGUITY: Being-H0.7 achieves 84.8% aggregate on LIBERO-Plus (fine-tuned) and claims 'resilience against shifted viewpoints,' but does not publish a camera-specific breakdown score. The proposal states OA-WAM 80.5% is the 'current SOTA on LIBERO-Plus camera axis' — this is correct given published camera-specific scores, but a CoRL reviewer who reads the Being-H0.7 paper may question whether the SOTA claim accounts for Being-H0.7's higher aggregate score. The proposal should add one sentence acknowledging that Being-H0.7 reports only aggregate LIBERO-Plus scores (82.1% zero-shot / 84.8% fine-tuned) without camera-split breakdown, and therefore OA-WAM's 80.5% camera-specific score remains the only published SOTA reference for the camera axis.\"]\nFeedback: The proposal has addressed all four Round 4 issues correctly and is verified by independent research to be factually accurate. One new critical issue emerged from fresh investigation: verify RoboTwin 2.0-Plus evaluation code availability BEFORE committing it as the primary benchmark. Concretely: (1) RoboTwin 2.0-PLUS EVALUATION CODE: Contact the arXiv:2603.22078 corresponding authors (Zhanguang Zhang, Yingxue Zhang at Huawei/UToronto) to request the evaluation code. If code is not obtainable within 1-2 days of project start, FLIP the benchmark priorities: make LIBERO-Plus the primary evaluation (fully public, arXiv:2510.13626) and RoboTwin 2.0-Plus secondary (implement from Appendix A if possible). The LIBERO-Plus evaluation has an equally strong case: OA-WAM at 80.5% camera is the published SOTA, Motus baseline needs to be run once (~4h), and camera robustness of VQ-Perceiver is directly testable. Importantly, the 21.6% Motus camera score from RoboTwin 2.0-Plus can still be cited as motivation for the problem without needing to reproduce the exact evaluation environment — as long as the improvement is demonstrated on LIBERO-Plus. (2) BEING-H0.7 AGGREGATE SCORE: Add one sentence: 'Being-H0.7 reports only aggregate LIBERO-Plus scores (82.1% zero-shot / 84.8% fine-tuned) without camera-specific breakdown; OA-WAM (arXiv:2605.06481) is the only published result with a dedicated camera split score (80.5%), making it the appropriate SOTA reference for this axis.' These are the only two remaining gaps. All factual claims are verified correct.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:58:12.685Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:58:12.685Z",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

## Round 1

64 recorded events

### User

_source line 3 · 2026-05-10T08:58:12.711Z_

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
  "title": "VQ-Perceiver World-State Bottleneck for Camera-Viewpoint-Robust Action in MoT WAMs",
  "core_problem": "Motus (Tri-model Joint Attention; WAN2.2-5B + Qwen3-VL-2B + action expert, ~7B total; public weights at motus-robotics/Motus on HuggingFace) achieves 87.0% on the unperturbed split of RoboTwin 2.0-Plus (overall average 71.5%) but drops to 21.6% under camera viewpoint perturbation and 43.1% under sensor noise — a 65 percentage-point camera degradation confirmed in arXiv:2603.22078, Table 3. Critically, appearance perturbations cause minimal degradation: lighting 84.6%, background 84.4%, robot initial state 85.0%. The prior proposal's appearance-robustness framing was empirically wrong: the actual published data shows Motus is resilient to lighting and background but catastrophically fragile under camera viewpoint changes. The camera-viewpoint failure implicates Motus's Tri-model Joint Attention design: action tokens jointly attend to raw video tokens in shared self-attention at every transformer layer, so action predictions are directly conditioned on viewpoint-specific pixel spatial arrangements (perspective projections, egocentric depth layout) encoded in those tokens, rather than viewpoint-invariant semantic state (object pose relative to gripper, task phase, contact configuration). When camera position changes, the spatial distribution of video tokens shifts, breaking the learned visual-to-action correlation. Motus's 21.6% is the most severe camera-viewpoint score among all WAMs evaluated in arXiv:2603.22078; LingBot-VA scores 28.9% on RoboTwin 2.0-Plus camera and Cosmos-Policy scores 75.8% on LIBERO-Plus camera, suggesting scale of video pretraining partially mitigates the issue but does not solve it. Motus was included in RoboTwin 2.0-Plus Table 3 results of arXiv:2603.22078 despite being excluded from the paper's WAM taxonomy discussion (its hybrid VLM-action routing architecture places it outside the strict definition), making it the only publicly-weighted MoT WAM with confirmed, severe camera-viewpoint vulnerability available for fine-tuning studies. IMPORTANT EVALUATION NOTE: RoboTwin 2.0-Plus is an in-house benchmark constructed by Huawei/UToronto for arXiv:2603.22078 — no public evaluation code, GitHub repository, or formal camera perturbation parameter specification has been released; the official RoboTwin 2.0 repo (github.com/RoboTwin-Platform/RoboTwin) applies only minor camera jitter (~1 cm) and does not include the viewpoint-pose perturbation measured in 2603.22078. Accordingly, the 21.6% Motus camera score is cited as published motivation for the problem, but RoboTwin 2.0-Plus is designated a secondary evaluation target contingent on author code release or Appendix A re-implementation. LIBERO-Plus (arXiv:2510.13626) is the primary evaluation benchmark: it is fully public, with evaluation code at github.com/sylvestf/LIBERO-plus and dataset at huggingface.co/datasets/Sylvest/LIBERO-plus, defining three camera sub-axes (C1: distance 1.01×–2.00×; C2: spherical position Δθ/Δϕ within 15°–75° cones; C3: orientation yaw/pitch/roll within 2°–10°), and the current camera-axis SOTA is OA-WAM at 80.5% (arXiv:2605.06481, Table 2).",
  "opportunity": "The gap: camera viewpoint is Motus's specific, quantified Achilles heel (87.0% unperturbed → 21.6% camera-perturbed on RoboTwin 2.0-Plus, per arXiv:2603.22078). The closest prior work, ReViWo (ICLR 2025), establishes the VQ-for-viewpoint-invariance principle in robotic manipulation: it decomposes visual observations into a VQ-coded view-invariant representation (VIR) and a continuous view-dependent representation (VDR), then trains a COMBO-based world model exclusively on VIR to achieve camera-robust control. This is directly related to our proposal — but four constraints make ReViWo inapplicable to our setting: (a) it requires multi-view training data with known camera labels, collected from MetaWorld simulators; (b) it operates on small-scale COMBO/RSSM world models evaluated on MetaWorld and PandaGym tasks; (c) it applies VQ as an offline preprocessing step external to the policy, not inside the running model; (d) it uses model-based RL, not diffusion-based imitation learning. Our contribution extends the VQ-for-viewpoint-invariance principle to a setting that drops all four constraints: a 7B diffusion-based MoT WAM fine-tuned on single-view demonstrations via intra-model cross-attention routing, evaluated on large-scale benchmarks (LIBERO-Plus primary, RoboTwin 2.0-Plus secondary) with a confirmed, quantified 65pp camera vulnerability. No concurrent work applies intra-model VQ routing within a deployed large-scale diffusion WAM without multi-view training data. The information-bottleneck argument is precisely grounded: camera viewpoint changes alter pixel-level spatial arrangements but leave object identity, task phase, and gripper-object relationships invariant. However, the viewpoint-invariance claim is explicitly framed as an empirical hypothesis, not a guarantee. A K=512 codebook could in principle still encode viewpoint-specific routing if the Perceiver cross-attention queries learn viewpoint-dependent attention patterns. The task-action gradient pressure is the claimed mechanism that discourages this: viewpoint-specific features that do not improve action prediction should be suppressed by task-loss SGD. This hypothesis is directly tested by the UMAP codebook visualization: if codebook clusters organize by task phase and object identity rather than camera angle, the hypothesis is confirmed; if clusters organize by camera angle, the paper pivots to analyzing why discretization does or does not produce viewpoint invariance — still publishable as an analysis contribution with the UMAP evidence and quantified ablation. This requires no camera pose annotations, no multi-view demonstrations, and no test-time knowledge of the camera transformation. Sensor noise robustness is also expected to improve because VQ quantization is inherently denoising: perturbed continuous features map to the same code as their clean counterparts when perturbation magnitude is smaller than nearest-neighbor codebook decision boundaries, directly addressing the 43.1% noise score. The primary contribution framing targets: (a) improving over Motus's baseline on LIBERO-Plus camera axis versus OA-WAM's 80.5% continuous-slot-attention SOTA (arXiv:2605.06481, Table 2), quantifying whether hard VQ discretization adds value over OA-WAM's continuous object-addressable approach; (b) citing the 65pp RoboTwin 2.0-Plus camera gap (21.6%) as published motivation, with secondary evaluation on RoboTwin 2.0-Plus if author code is obtained or Appendix A re-implementation is feasible within timeline. Motus vanilla baseline numbers are already published for RoboTwin 2.0-Plus (camera: 21.6%), saving that baseline run. Motus LIBERO-Plus baseline must be run once (~4h wall clock on 4 H100s).",
  "landscape": "Motus (arXiv:2512.13030, TMLR 2025): Tri-model Joint Attention (concatenated self-attention across understanding, video, and action tokens); ~7B (WAN2.2-5B + Qwen3-VL-2B + action expert); public weights; confirmed camera viewpoint score 21.6% on RoboTwin 2.0-Plus (arXiv:2603.22078, Table 3). ReViWo (proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e, ICLR 2025): Representation learning for View-invariant World model; decomposes visual observations into VQ-coded view-invariant representation (VIR) + continuous view-dependent representation (VDR); trains a COMBO-based RL world model on VIR alone; achieves camera-robust manipulation on MetaWorld and PandaGym; real-world ALOHA experiments. Critical prior work establishing the VQ-for-viewpoint-invariance principle. Key limitations relative to this proposal: (a) requires labeled multi-view training data (known camera angles from MetaWorld simulator); (b) small-scale COMBO/RSSM world model, not a 7B diffusion MoT WAM; (c) offline VQ preprocessing step external to the policy, not intra-model routing; (d) model-based RL, not diffusion imitation learning. MotuBrain (arXiv:2604.27792, 2026): H-bridge design (middle 50% layers V-A joint attention, asymmetric at inference); no public pretrained checkpoint — excluded from scope. Fast-WAM (arXiv:2603.16666, 2026): skips video generation at test time for 4× speedup; targets efficiency only. GigaWorld-Policy (arXiv:2603.17240, 2026): causal decoupling for 9× speedup; efficiency only; no geometric robustness improvement. 'Do WAMs Generalize Better than VLAs?' (arXiv:2603.22078, 2026): benchmarks WAM robustness on RoboTwin 2.0-Plus and LIBERO-Plus; introduces RoboTwin 2.0-Plus, which adds seven explicit perturbation axes to RoboTwin 2.0, including camera viewpoint (altering the viewpoint pose of the third-person camera), robot initial configuration, language, lighting, background, sensor noise, and layout — camera viewpoint is absent from the original RoboTwin 2.0 domain-randomization axes; Cosmos-Policy reaches 82.2% overall on LIBERO-Plus and 75.8% on camera split; LingBot-VA: 28.9% camera on RoboTwin 2.0-Plus; Motus: 21.6% camera on RoboTwin 2.0-Plus — worst WAM camera score. CRITICAL AVAILABILITY NOTE: RoboTwin 2.0-Plus is an in-house Huawei/UToronto benchmark with no public evaluation code repository and no published camera perturbation parameter specification; the official RoboTwin 2.0 GitHub (github.com/RoboTwin-Platform/RoboTwin) does not include 2.0-Plus perturbation protocols; reproducing the evaluation requires either author-provided code (corresponding authors: Zhanguang Zhang / Yingxue Zhang at Huawei/UToronto) or re-implementation from Appendix A of arXiv:2603.22078. LIBERO-Plus (arXiv:2510.13626, ICLR 2026): fully public evaluation infrastructure (github.com/sylvestf/LIBERO-plus; dataset at huggingface.co/datasets/Sylvest/LIBERO-plus); drop-in replacement for LIBERO; 10,030 tasks across seven perturbation dimensions with 20,000+ trajectories; camera perturbation covers three sub-axes: C1 (distance 1.01×–2.00×), C2 (spherical position, Δθ/Δϕ within 15°–75° cones), C3 (orientation yaw/pitch/roll within 2°–10°); confirms camera viewpoint causes ~72pp average drop in VLAs; models show resilience to lighting and background; PRIMARY evaluation benchmark for this proposal. MWM (arXiv:2604.19683, 2026): predicts future semantic masks as geometric bottleneck; requires per-frame mask annotations; not applied to MoT WAMs. AnyCamVLA (arXiv:2603.05868, 2026): zero-shot camera viewpoint adaptation via feed-forward novel view synthesis at test time; plug-and-play for VLAs; requires knowing camera transformation at inference; training-free, not learned; not applicable to WAMs without adaptation; evaluated on custom LIBERO-based viewpoint benchmark (not LIBERO-Plus directly), achieving ~94.5% average under large perturbations. 'Dreaming the Unseen' (arXiv:2603.21017, 2026): continuous world-model regularization for OOD robustness; no discrete representations. Being-H0.7 (arXiv:2605.00078, 2026): K=16 latent reasoning queries as soft bottleneck; no VQ discretization — continuous queries can still encode viewpoint-specific features. Reports only aggregate LIBERO-Plus scores (82.1% zero-shot, 84.8% fine-tuned) without any camera-specific breakdown; the paper's claim of 'resilience against shifted viewpoints, novel textures, and sensor noise' is an umbrella inference from the aggregate score, not a disaggregated camera-axis measurement. Evaluated on RoboTwin 2.0 (not RoboTwin 2.0-Plus): clean 90.2%, domain-randomized (Hard) 89.6%; RoboTwin 2.0 domain randomization covers table-top clutter, varied lighting conditions, diverse background textures, tabletop height variations, and diverse language instructions — camera viewpoint/extrinsic perturbation is not among the RoboTwin 2.0 axes; accordingly, Being-H0.7's 89.6% domain-randomized score does not reflect camera-extrinsic robustness as measured by RoboTwin 2.0-Plus's dedicated camera split, and does not undermine the core problem statement. The proposed Perceiver-only ablation (N_ws=64 continuous queries, masking ON) is not architecturally matched to Being-H0.7's K=16 queries; it serves to isolate the contribution of hard VQ discretization at fixed N_ws=64, not to directly replicate Being-H0.7. ARRO (arXiv:2505.08627, 2026): zero-shot segmentation masking at inference; training-free; targets appearance, not camera viewpoint. VILA (arXiv:2601.02994, 2026): view-invariant latent actions (output action space); operates on action representations not visual tokens. GCQ (arXiv:2510.16039, 2025): action-conditioned VQ for spatiotemporal compression in recurrent world models; different target and mechanism. VQ-VLA (ICCV 2025): VQ on output action tokens, not visual representations. OA-WAM (arXiv:2605.06481, 2026): object-addressable cross-attention without discrete compression; camera score 80.5% on LIBERO-Plus (Table 2, arXiv:2605.06481v1 — current SOTA on LIBERO-Plus camera axis, exceeding Cosmos-Policy's 75.8% and π0.5's 75.4%); achieves SOTA on LIBERO-Plus geometric axes (geo avg 84.3%, overall avg 83.9%) via slot-based soft attention — important continuous-bottleneck baseline demonstrating camera robustness is achievable without VQ; comparison against OA-WAM's continuous-slot approach vs. our hard VQ approach is a planned ablation. Note: Being-H0.7 reports a higher overall aggregate score (84.8% fine-tuned) than OA-WAM (83.9%), but does not publish a camera-axis breakdown; OA-WAM's 80.5% remains the only published SOTA reference for the LIBERO-Plus camera axis specifically. X-WAM (arXiv:2604.26694, 2026): Unified 4D World Action Modeling via asynchronous denoising; predicts multi-view RGB-D videos; requires multi-view training data; continuous representations; targets 4D reconstruction and efficiency, not single-view viewpoint invariance; orthogonal. XR-1/UVMC (arXiv:2511.02776, ICLR 2026): dual-branch VQ-VAE with vision branch and motion branch aligned via KL-divergence; offline preprocessing step before model inference, not intra-model routing; targets cross-embodiment generalization via shared codebook, not geometric viewpoint robustness within a running WAM. DIAL (arXiv:2603.29844, 2026): continuous latent visual foresight as structural bottleneck between System-2 (VLM reasoning) and System-1 (action decoder); targets intent decoupling and training instability in VLAs; continuous representations (not discrete); different model type (VLA, not WAM) and different failure mode (training instability, not camera viewpoint brittleness). 'Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning' (arXiv:2510.02268, 2025): conditions ACT, Diffusion Policy, and SmolVLA on Plücker embeddings of camera extrinsics; significantly improves viewpoint generalization; requires known camera extrinsics at both training and test time; no VQ; not applicable to WAMs; orthogonal approach (explicit extrinsic conditioning vs. learned discrete bottleneck requiring no camera pose). No concurrent work extends intra-model VQ discretization of visual token representations within a deployed diffusion-based MoT WAM to address camera viewpoint robustness without multi-view training data.",
  "approach": "All experiments use the public Motus checkpoint (~7B: WAN2.2-5B + Qwen3-VL-2B + action expert; motus-robotics/Motus, HuggingFace). The modification has three components: (1) VQ-Perceiver module: N_ws=64 randomly-initialized learnable world-state query vectors perform multi-head cross-attention over the N_video≈256 video tokens output by Motus's video VAE. The N_ws cross-attended outputs are quantized via straight-through VQ-VAE to a jointly-trained codebook of K=512 entries with EMA updates and commitment loss weight λ_vq ramped from 0.01 to 0.25 over the first 5K steps (ramp prevents large commitment gradients from driving codebook collapse before the cross-attention pathway is established). Result: N_ws=64 discrete world-state tokens. (2) Action routing in Motus joint attention: apply an attention mask in Motus's Tri-model Joint Attention so that action tokens cannot directly attend to raw video tokens (action←video path blocked). Video tokens retain full joint attention with understanding tokens and other video tokens; video tokens can still attend to action tokens (preserving action-conditioned video generation). (3) Discrete world-state cross-attention: a dedicated cross-attention sublayer added after each joint attention block allows action tokens to attend exclusively to the N_ws=64 VQ-quantized world-state tokens. Fine-tuning protocol: LoRA (rank=64) applied to all joint attention and new cross-attention layers; VQ-Perceiver initialized randomly; 30K steps on LIBERO + RoboTwin 2.0 demonstrations; combined objective: action rectified-flow diffusion loss + VQ commitment loss. Warm-up schedule: attention masking probability ramped from 0 to 1 over first 5K steps to avoid instability. Training stability monitoring: adding a randomly initialized VQ-Perceiver to a pretrained 7B system risks initialization mismatch — action tokens may find the new cross-attention pathway uninformative relative to the blocked direct video route, resulting in near-zero gradients to the VQ-Perceiver in early training. Two mitigations are added: (a) codebook gradient norm monitoring from step 500 — if VQ-Perceiver cross-attention layer gradient norm is below 10% of the joint attention layer gradient norm at step 2K, the attention masking warm-up is extended from 5K to 10K steps, giving the pathway more time to establish useful routing before full masking is applied; (b) the λ_vq ramp described above. These triggers are implemented as automated training callbacks. PRIMARY evaluation: LIBERO-Plus (github.com/sylvestf/LIBERO-plus; dataset: huggingface.co/datasets/Sylvest/LIBERO-plus) — fully public benchmark with defined camera perturbation protocol (C1/C2/C3 axes, 15°–75° spherical cones). Run Motus LIBERO-Plus baseline once (~4h wall clock on 4 H100s) to establish comparison point; current camera-axis SOTA is OA-WAM at 80.5% (arXiv:2605.06481, Table 2). SECONDARY evaluation: RoboTwin 2.0-Plus — Motus vanilla baseline 21.6% taken from arXiv:2603.22078 Table 3 (no baseline run required). CRITICAL DEPENDENCY: RoboTwin 2.0-Plus evaluation code is NOT publicly available (in-house Huawei/UToronto benchmark from arXiv:2603.22078; no GitHub repo or perturbation parameter specification released). Contingency protocol: (a) Contact corresponding authors Zhanguang Zhang / Yingxue Zhang (Huawei/UToronto) within day 1–2 of project start to request evaluation code or environment snapshot; (b) if code is not obtainable within 2 days, implement RoboTwin 2.0-Plus camera perturbation from Appendix A of arXiv:2603.22078 by adapting LIBERO-Plus's C2 spherical-position protocol to the RoboTwin 2.0 Aloha-Agilex bimanual simulator — estimated 1–2 days of implementation work; (c) if neither is feasible within the CoRL timeline, the paper reports LIBERO-Plus as sole primary evaluation and cites the 21.6% RoboTwin 2.0-Plus score exclusively as published motivation in the introduction. CoRL scope (3 fine-tuning runs): (a) VQ-Perceiver K=512, N_ws=64, attention masking ON (main method); (b) Perceiver-only (continuous soft queries N_ws=64, no VQ, masking ON — ablates discretization; isolates the contribution of hard VQ over continuous routing at fixed N_ws=64; note this uses N_ws=64 continuous queries and is not architecturally matched to Being-H0.7's K=16 latent reasoning queries, so it does not constitute a direct replication of Being-H0.7 — the primary goal is to quantify whether VQ discretization per se improves camera robustness); (c) VQ-Perceiver K=512, N_ws=64, masking OFF (VQ as auxiliary path — ablates routing). ICLR fallback ablations (add 3 more runs): K∈{128,1024}; N_ws∈{16,128}; FSQ variant. Interpretability: UMAP visualization of codebook assignments colored by (i) camera angle, (ii) task phase, (iii) object identity, to verify camera-angle-invariant semantic organization — this is the primary empirical test of the viewpoint-invariance hypothesis. Codebook utilization monitoring from step 500 onward; EMA restart if per-code usage below 1/K² threshold by step 2K.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180–400 H100-hours aggregate (Motus vanilla RoboTwin 2.0-Plus baseline already published; ~4h wall clock × 4 GPUs = ~16 H100-hours for LIBERO-Plus Motus baseline [required, now primary evaluation]; 5–6 fine-tuning runs × ~8–17h wall clock × 4 H100s = ~33–67 H100-hours aggregate per run = ~165–400 H100-hours for runs; ~15–20h wall clock × 1–2 GPUs = ~15–40 H100-hours evaluation; total: ~196–456 H100-hours; best estimate at ~1.5s/step: 5–6 runs × 50h + 56h overhead = ~306–356 H100-hours); RoboTwin 2.0-Plus secondary evaluation adds ~1–2 days researcher implementation time if author code not provided",
      "gpu_utilization": "~20–35%; idle between human debug cycles and evaluation inspection",
      "timeline": "3–4 months (1 month: implement VQ-Perceiver module, integrate with Motus 7B codebase, unit tests, resolve RoboTwin 2.0-Plus code access; 1.5 months: fine-tuning runs and ablations; 1 month: evaluation, codebook visualization, writing) — targets ICLR 2027",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$540–1800 (180–400h H100 at $3.00–4.50/hr; best estimate ~$918–1602)"
    },
    "human_in_loop": {
      "gpu_hours": "~150–230 H100-hours aggregate (3 CoRL runs × ~33–67 H100-hours aggregate per run [~8–17h wall clock on 4 H100s at 1–2s/step] = ~99–200 H100-hours fine-tuning; ~4h wall clock × 4 GPUs LIBERO-Plus baseline = ~16 H100-hours [required primary evaluation]; evaluation overhead ~15–30 H100-hours; total: ~130–246 H100-hours; best estimate at 1.5s/step: 3 × 50h + 36h overhead = ~186 H100-hours; 2 ICLR-fallback ablations if time permits add ~66–134 H100-hours)",
      "gpu_utilization": "~55–70%",
      "timeline": "5–7 weeks (CoRL 2026 primary: 4–5 weeks compressed if targeting May 28 deadline; day 1–2: contact RoboTwin 2.0-Plus authors for eval code; days 3–4: LIBERO-Plus baseline run + VQ module implementation; remainder: fine-tuning + evaluation)",
      "team": "1 researcher, ~30 min/day check-in for ablation configs, camera-split OOD curves, and codebook utilization metrics",
      "claude_api_cost": "~$200–350 (~1800–3000 turns for code edits, ablation scheduling, OOD accuracy summaries, codebook analysis)",
      "estimated_gpu_cost": "~$450–1107 (150–230h H100 at $3.00–4.50/hr)",
      "risk_note": "Codebook collapse requires early monitoring. LoRA rank=64 on 7B: ~8–17h wall clock per run = ~33–67 H100-hours aggregate (at 1–2s/step for video LoRA). Warm-up masking schedule (0→1 over 5K steps) and λ_vq ramp (0.01→0.25 over 5K steps) mitigate training instability. If VQ-Perceiver cross-attention gradient norm < 10% of joint attention layer at step 2K, extend warm-up to 10K steps. If throughput ≥3s/step even after reducing to 20K steps, drop from 3 to 2 fine-tuning runs (main VQ-Perceiver + Perceiver-only ablation), deferring the masking ablation to ICLR fallback scope. RoboTwin 2.0-Plus evaluation is secondary: if author code cannot be obtained within 2 days of project start, LIBERO-Plus is the sole primary benchmark and RoboTwin 2.0-Plus is cited only as published motivation."
    },
    "auto_research": {
      "gpu_hours": "~130–236 H100-hours aggregate (Motus vanilla RoboTwin 2.0-Plus baseline from published paper — no run needed; ~4h wall clock × 4 GPUs = ~16 H100-hours for LIBERO-Plus Motus baseline [required primary evaluation]; 3 CoRL-scope fine-tuning runs × ~8–17h wall clock on 4 H100s = ~33–67 H100-hours aggregate per run = ~99–200 H100-hours total fine-tuning; ~5h wall clock × 4 GPUs = ~20 H100-hours evaluation; total: ~135–236 H100-hours aggregate; best estimate at ~1.5s/step: 3 × 50h + 36h overhead = ~186 H100-hours)",
      "gpu_utilization": "~80–90%; GPU idle only during checkpoint I/O and rollout evaluation",
      "timeline": "4–5 days on 8 H100s (2 parallel runs ≈ 8–17h wall clock + third run serial ≈ 8–17h + baseline ~4h + evaluation ~5h = ~25–43h pure compute wall clock; 4–5 calendar days including setup, monitoring, and iteration), delivering results by May 15–16 — leaving 12–13 days to write for CoRL 2026 (abstract May 26, paper May 28). ADDITIONAL DAY 1 TASK: contact RoboTwin 2.0-Plus authors for evaluation code (Zhanguang Zhang / Yingxue Zhang at Huawei/UToronto); if code not received by day 2, proceed with LIBERO-Plus as sole primary benchmark.",
      "team": "0 researchers after ~3–4h initial codebase setup, module integration review, job submission, and author contact for RoboTwin 2.0-Plus code",
      "claude_api_cost": "~$350–500 (~3000–4500 turns for code edits, sweep scheduling, camera-split OOD analysis, codebook cluster analysis, paper drafting)",
      "estimated_gpu_cost": "~$405–1060 (135–236h H100 at $3.00–4.50/hr; best estimate ~$558–837)",
      "speed_bottleneck": "LoRA fine-tuning of ~7B Motus: estimated 1–2s/step for video LoRA on 4 H100s. At 1s/step [optimistic]: ~8.3h wall clock = ~33 H100-hours aggregate per run. At 2s/step [conservative, more typical for video diffusion models]: ~16.7h wall clock = ~67 H100-hours aggregate per run. At 2s/step, 3 fine-tuning runs alone = ~200 H100-hours aggregate — right at the budget ceiling; total with baseline and evaluation rises to ~236 H100-hours. Agent must benchmark step throughput at training step 100 and report: if >1.5s/step, reduce to 20K training steps to remain within ~200 H100-hour budget. If throughput ≥3s/step even at 20K steps (plausible for 7B video diffusion with LoRA rank=64 on 4 H100s — 3s/step × 20K × 4 GPUs = ~66.7 H100-hours/run, 3 runs + overhead ≈ 236 H100-hours at ceiling), reduce from 3 to 2 fine-tuning runs (main VQ-Perceiver + Perceiver-only ablation), dropping the masking ablation to ICLR fallback scope. 2 parallel jobs on 8 H100s is the practical limit. Agent must prioritize: (1) LIBERO-Plus Motus baseline first (~4h wall clock, establishes primary comparison point against OA-WAM 80.5% SOTA); (2) main VQ-Perceiver run; (3) Perceiver-only ablation; (4) masking ablation (if budget permits). If camera score improves substantially from the Motus LIBERO-Plus baseline, paper is ready. If VQ-Perceiver does not beat Perceiver-only, paper pivots to analyzing why discretization helps/hurts — still publishable as an analysis paper. Codebook collapse monitored from step 500; EMA restart if triggered.",
      "risk_note": "Codebook collapse requires early monitoring. LoRA rank=64 on 7B: ~33 H100-hours/run (~8h wall clock) at 1s/step; ~67 H100-hours/run (~17h wall clock) at 2s/step. Warm-up masking (0→1 over 5K steps) and λ_vq ramp (0.01→0.25 over 5K steps) mitigate training instability. If VQ-Perceiver cross-attention gradient norm < 10% of joint attention layer gradient norm by step 2K, extend warm-up ramp to 10K steps. RoboTwin 2.0-Plus evaluation is contingent on code availability (in-house Huawei/UToronto benchmark, no public release); contact authors day 1; if no response by day 2, proceed with LIBERO-Plus as primary and cite RoboTwin 2.0-Plus 21.6% as motivation only. Without the public Motus checkpoint or LIBERO-Plus evaluation environment the entire estimate is invalid — verify both before launch (LIBERO-Plus is confirmed public at github.com/sylvestf/LIBERO-plus)."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, paper deadline May 28 2026 — 16/18 days from today; PRIMARY TARGET; auto-research delivers results by May 15–16 leaving 12–13 days to write a focused 8-page method paper; scope: main method + 2 ablations + LIBERO-Plus all camera splits [primary] + RoboTwin 2.0-Plus all splits [secondary, contingent on code availability]; robotics + robustness framing is a strong CoRL fit; camera viewpoint is the hardest open WAM problem per arXiv:2603.22078)",
    "ICLR 2027 (deadline ~September–October 2026 — fallback if CoRL timeline is missed; expand ablation suite to K, N_ws, FSQ variants; add full LIBERO-Plus evaluation across all splits; stronger representation-learning framing with ReViWo as explicit prior work to extend)",
    "CVPR 2027 (deadline ~November 2026 — tertiary fallback if visual robustness framing dominates over robotics systems contribution)"
  ],
  "level": "solid",
  "key_references": [
    "Motus: A Unified Latent Action World Model (arXiv:2512.13030, TMLR 2025) — target model; ~7B (WAN2.2-5B + Qwen3-VL-2B + action expert); public weights (motus-robotics/Motus on HuggingFace); Tri-model Joint Attention design; camera viewpoint score 21.6% on RoboTwin 2.0-Plus",
    "Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv:2603.22078, 2026) — source of Motus camera score (21.6% camera, 87.0% unperturbed split, 71.5% overall average), LingBot-VA camera score (28.9%), Cosmos-Policy LIBERO-Plus scores (camera 75.8%, total 82.2%); confirms camera viewpoint is the dominant WAM robustness gap; introduces RoboTwin 2.0-Plus, which adds seven explicit perturbation axes (camera, robot, language, light, background, noise, layout) to the original RoboTwin 2.0 — camera viewpoint extrinsic perturbation is a RoboTwin 2.0-Plus axis and is absent from RoboTwin 2.0 domain randomization. AVAILABILITY NOTE: RoboTwin 2.0-Plus is an in-house Huawei/UToronto benchmark with no public evaluation code release; the official RoboTwin 2.0 GitHub does not include 2.0-Plus camera perturbation protocols; reproduction requires author-provided code or Appendix A re-implementation.",
    "ReViWo: Learning View-invariant World Models for Visual Robotic Manipulation (proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e, ICLR 2025) — critical direct predecessor establishing VQ-for-viewpoint-invariance principle; decomposes observations into VQ-coded view-invariant representation (VIR) + continuous view-dependent representation (VDR); trains COMBO-based world model on VIR; requires labeled multi-view training data from MetaWorld simulators; small-scale RSSM world model on MetaWorld/PandaGym; real-world ALOHA experiments; our proposal extends this principle to 7B diffusion MoT WAMs with single-view demonstrations via intra-model cross-attention routing",
    "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv:2510.13626, ICLR 2026) — PRIMARY benchmark used for evaluation; fully public evaluation infrastructure (github.com/sylvestf/LIBERO-plus; dataset at huggingface.co/datasets/Sylvest/LIBERO-plus); confirms camera viewpoint causes ~72pp average drop in VLAs; camera perturbation covers three sub-axes: C1 (distance 1.01×–2.00×), C2 (spherical position Δθ/Δϕ within 15°–75° cones), C3 (orientation yaw/pitch/roll within 2°–10°); models show resilience to lighting and background",
    "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust VLAs (arXiv:2603.05868, 2026) — closest camera robustness baseline; test-time novel view synthesis; training-free; requires known camera transformation at inference; not architectural; not applicable to WAMs without adaptation; evaluates on custom LIBERO-based viewpoint protocol (not LIBERO-Plus directly)",
    "XR-1/UVMC: Unified Vision-Motion Codes for Cross-Embodiment Robot Learning (arXiv:2511.02776, ICLR 2026) — closest VQ-based competitor after ReViWo; dual-branch VQ-VAE aligning visual dynamics and robot motion codes via KL-divergence; offline preprocessing, not intra-model routing; targets cross-embodiment generalization, not camera viewpoint robustness within a deployed WAM",
    "DIAL: Latent Visual Foresight as Structural Bottleneck (arXiv:2603.29844, 2026) — continuous latent bottleneck between VLM reasoning and action in VLAs; different model type (VLA not WAM), continuous not discrete, targets intent decoupling not camera robustness",
    "Mask World Model: Predicting What Matters for Robust Robot Policy Learning (arXiv:2604.19683, 2026) — geometric bottleneck baseline via semantic mask prediction; requires per-frame mask annotations; not applied to MoT WAMs",
    "Fast-WAM (arXiv:2603.16666, 2026) — efficiency baseline; skips video generation at inference; does not improve geometric robustness",
    "GigaWorld-Policy (arXiv:2603.17240, 2026) — causal decoupling for 9× speedup; efficiency baseline; does not improve geometric robustness",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078, 2026) — soft continuous latent query baseline; K=16 latent reasoning queries (confirmed from training details section of arXiv:2605.00078v1); no VQ discretization; continuous queries can still encode viewpoint-specific features. Reports only aggregate LIBERO-Plus scores (82.1% zero-shot / 84.8% fine-tuned) without any camera-specific breakdown; the paper's claim of 'resilience against shifted viewpoints, novel textures, and sensor noise' is an umbrella inference from the aggregate score, not a disaggregated camera-axis measurement — OA-WAM (arXiv:2605.06481) is the only published result with a dedicated LIBERO-Plus camera split score (80.5%), making it the appropriate SOTA reference for the camera axis. Evaluated on RoboTwin 2.0 (not RoboTwin 2.0-Plus): clean 90.2%, domain-randomized (Hard) 89.6%; RoboTwin 2.0 domain randomization covers table-top clutter, varied lighting conditions, diverse background textures, tabletop height variations, and diverse language instructions — camera viewpoint/extrinsic perturbation is not among these axes; Being-H0.7's 89.6% score therefore does not reflect camera-extrinsic robustness as measured by RoboTwin 2.0-Plus's dedicated camera split. The proposed Perceiver-only ablation (run b: N_ws=64 continuous queries, masking ON) is not architecturally matched to Being-H0.7's K=16 queries; it isolates the contribution of hard VQ discretization at fixed N_ws=64, not a direct replication of Being-H0.7.",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, 2026) — object-addressable slot cross-attention without discrete compression; camera score 80.5% on LIBERO-Plus (Table 2, arXiv:2605.06481v1 — current SOTA on LIBERO-Plus camera axis, exceeding Cosmos-Policy's 75.8% and π0.5's 75.4%; geo avg 84.3%, overall avg 83.9%); achieves state-of-the-art on LIBERO-Plus geometric axes via continuous slot attention; important baseline showing continuous-attention approaches can achieve camera robustness; comparison against OA-WAM's soft approach vs. our hard VQ approach is a planned ablation clarifying when discrete VQ adds value over continuous slot routing. Note: Being-H0.7 reports a higher overall aggregate score (84.8% fine-tuned) but publishes no camera-axis breakdown; OA-WAM 80.5% is the only published camera-specific SOTA on LIBERO-Plus.",
    "X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694, 2026) — 4D WAM predicting multi-view RGB-D videos; requires multi-view training data; continuous representations; targets reconstruction efficiency; orthogonal to single-view VQ camera-invariance approach",
    "'Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning' (arXiv:2510.02268, 2025) — conditions behavior cloning policies (ACT, Diffusion Policy, SmolVLA) on Plücker embeddings of camera extrinsics; improves viewpoint generalization; requires known camera extrinsics at test time; no VQ; not applicable to WAMs; orthogonal approach (explicit extrinsic conditioning vs. learned implicit bottleneck)",
    "ARRO: Augmented Reality for Robots (arXiv:2505.08627, 2026) — training-free visual robustness baseline; zero-shot masking; targets appearance not geometric robustness",
    "VILA: Learning to Act Robustly with View-Invariant Latent Actions (arXiv:2601.02994, 2026) — view-invariant latent action pretraining; acts on action representations not visual tokens; output-space approach vs. our input-routing approach",
    "GCQ: Grid-like Code Quantization (arXiv:2510.16039, 2025) — action-conditioned VQ for temporal compression in recurrent world models; different target and mechanism",
    "VQ-VLA: Improving VLA Models via Scaling Vector-Quantized Action Tokenizers (ICCV 2025) — VQ on output action tokens, not input visual representations; orthogonal",
    "Perceiver IO: A General Architecture for Structured Inputs and Outputs (ICML 2022) — architectural basis for world-state query cross-attention module",
    "Neural Discrete Representation Learning [VQ-VAE] (NeurIPS 2017) — VQ training recipe; commitment loss; EMA codebook updates",
    "Mastering diverse control tasks through world models [DreamerV3] (Nature 2025) — existence proof that discrete latent state in world models can outperform continuous; analogous motivation; ReViWo's COMBO world model is related",
    "lucidrains/vector-quantize-pytorch — open-source VQ, FSQ, RVQ implementations; reduces implementation risk"
  ],
  "description": "We extend the VQ-for-viewpoint-invariance principle established by ReViWo (ICLR 2025) from small-scale RL world models to modern diffusion-based MoT WAMs, introducing a novel intra-model routing mechanism — the VQ-Perceiver world-state bottleneck — that requires no multi-view training data and directly targets a confirmed 65pp camera vulnerability in the only publicly-weighted large-scale MoT WAM. Specifically: Motus achieves 87.0% on the unperturbed split of RoboTwin 2.0-Plus (overall average 71.5%) but drops to 21.6% under camera viewpoint perturbation (arXiv:2603.22078, Table 3), while appearance perturbations cause negligible degradation (lighting 84.6%, background 84.4%). ReViWo (ICLR 2025) established that VQ-coded view-invariant representations support camera-robust robot control, but required labeled multi-view training data, operated on small COMBO/RSSM world models on MetaWorld/PandaGym, and applied VQ as offline preprocessing external to the policy. Our architectural contribution adapts this principle to the 7B fine-tuning setting: N_ws=64 learnable world-state queries cross-attend to N_video≈256 video tokens, and each query output is VQ-quantized to one of K=512 codebook entries trained jointly with Motus's action diffusion objective. In modified Motus joint attention, action tokens' direct access to raw video tokens is masked; action tokens instead attend exclusively to the N_ws=64 discrete world-state tokens via a dedicated cross-attention sublayer. The viewpoint-invariance claim is framed as an empirical hypothesis — the finite vocabulary cannot memorize viewpoint-specific pixel patterns under task-action gradient pressure — with the UMAP codebook visualization (planned) as the primary empirical test. Key differentiators: unlike AnyCamVLA (test-time view synthesis, requires known camera transform at inference), the contribution is learned and requires no additional inference-time inputs; unlike Being-H0.7 (K=16 continuous queries, which can still encode viewpoint-specific interpolations and reports only aggregate LIBERO-Plus scores without camera-axis breakdown), hard VQ prevents viewpoint-specific feature encoding; unlike ReViWo (multi-view training data required), single-view demonstrations only; unlike UVMC/XR-1 (offline preprocessing for cross-embodiment), this modifies intra-model routing within a deployed WAM. PRIMARY evaluation: LIBERO-Plus (fully public; github.com/sylvestf/LIBERO-plus), targeting improvement over Motus baseline and comparison against OA-WAM's 80.5% camera-axis SOTA (arXiv:2605.06481, Table 2) — the only published camera-specific SOTA on this benchmark (Being-H0.7 reports only aggregate scores without camera-axis breakdown). SECONDARY evaluation: RoboTwin 2.0-Plus (contingent on code availability from Huawei/UToronto authors or Appendix A re-implementation within timeline); 21.6% Motus camera score cited as published motivation regardless. Motus vanilla LIBERO-Plus baseline run required (~4h on 4 H100s); ~7B model; 3 focused runs within ~130–236 H100-hours aggregate (~8–17h wall clock per run on 4 H100s at 1–2s/step); CoRL 2026 primary target.",
  "project_name": "vq_perceiver_world_state_wam",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL ARCHITECTURAL MISMATCH: The core premise — 'action stream cross-attends over hundreds of raw continuous video latent tokens' — does not match target architectures. MotuBrain explicitly uses decoupled layers where video and action streams do NOT perform joint attention, with cross-modal sharing only in a short joint-denoising prefix. Motus uses Tri-model Joint Attention (shared self-attention across three modalities), not a separate cross-attention K/V interface. Inserting a VQ bottleneck into the video→action K/V projections assumes a structural interface that does not exist in either target model.", "CRITICAL EFFICIENCY CLAIM IS WRONG: The proposal states 'the action stream attends over K=512 fixed codebook vectors instead of N_video≈256–1024 raw tokens, reducing cross-attention FLOPs by 2–4×.' This is incorrect. Applying straight-through VQ to N_video projected K/V vectors still passes N_video quantized vectors to the cross-attention — the sequence length is unchanged. FLOPs reduction to O(K) would require an additional deduplication/aggregation step (group all tokens assigned to the same code and replace with one representative), which is not described anywhere in the proposal.", "CRITICAL COMPUTE CONSTRAINT VIOLATED: Auto-research mode estimates 700–900 H100-hours (3.5–4.5× over the ≤200 H100-hour hard limit). HIL mode estimates 320 H100-hours (1.6× over limit). Only manual mode (~200 H100-hours) respects the budget, but manual mode takes 3–5 months — incompatible with the 20-day CoRL deadline.", "COMPETING WORK ADDRESSES SAME EFFICIENCY PROBLEM BETTER: Fast-WAM (arXiv:2603.16666, Mar 2026) skips video generation entirely at test time, achieving 4× speedup with near-identical accuracy. GigaWorld-Policy (arXiv:2603.17240, Mar 2026) uses causal decoupling to prevent video tokens from influencing action tokens at inference, achieving 9× speedup over Motus. Both are simpler and more impactful than inserting VQ at the cross-attention interface.", "OVERLAPPING CONCURRENT WORK: GCQ — Grid-like Code Quantization (arXiv:2510.16039, Oct 2025) — proposes an action-conditioned VQ codebook for discrete world-model representations, performing spatiotemporal compression for long-horizon prediction and inverse modeling. This directly overlaps with the proposed VQ-for-world-state-discretization angle and must be discussed/differentiated.", "PRIMARY TARGET MODEL HAS NO PUBLIC WEIGHTS: No public MotuBrain pretrained checkpoint was found. Motus does have public weights (motus-robotics/Motus on HuggingFace), but Motus's architecture (Tri-model Joint Attention) does not expose the assumed cross-attention K/V interface. Falling back to Motus requires first verifying that its architecture can accommodate the proposed modification at all.", "WEAK DreamerV3 ANALOGY: DreamerV3's discrete representations are categorical latent states in a recurrent SSM (RSSM), used for world-state rollout in model-based RL — not for cross-attention K/V in a diffusion transformer. The analogy requires stronger theoretical grounding to justify why discretizing K/V projections specifically should improve generalization versus continuous K/V with appropriate regularization."]
Feedback: The seed insight — that a discrete semantic bottleneck between the world-model and action streams could improve generalization — has intellectual merit, but the proposal must be rebuilt on accurate architectural foundations before it can be defensible.

1. VERIFY ARCHITECTURE FIRST: Before writing another line of the proposal, fetch the full HTML of arXiv:2512.13030 (Motus) and arXiv:2604.27792 (MotuBrain) and identify precisely where/whether the action stream cross-attends over video K/V vectors. If it does not (shared self-attention in Motus, decoupled layers in MotuBrain), the modification cannot be implemented as described. Consider targeting a model where the interface actually exists, or propose adding a cross-attention layer that can then be quantized.

2. CORRECT THE EFFICIENCY CLAIM: Either (a) describe a deduplication mechanism that achieves true O(K) attention (assign N_video tokens to codes, pool per-code, attend over active codes only — similar to slot attention or Perceiver IO), or (b) drop the efficiency framing entirely and position the contribution as a generalization/robustness benefit from semantic discretization, leaving efficiency to Fast-WAM/GigaWorld-Policy.

3. DIFFERENTIATE FROM GCQ (arXiv:2510.16039): GCQ applies action-conditioned VQ for world-model compression. Explain precisely how the proposed approach differs: VQ is applied at the K/V interface of a diffusion MoT rather than as a compression stage before the model, and the codebook is learned jointly with the diffusion objective rather than separately.

4. PIVOT TO MOTUS ONLY: Motus has public weights; target it exclusively. Verify that after the architectural fix the modification is implementable within Motus's Tri-model Joint Attention design, possibly by inserting an explicit cross-attention layer between quantized video representations and the action expert.

5. FIX COMPUTE ESTIMATES: Cap all modes at ≤200 H100-hours. The auto-research estimate (700–900 H100-hours) should be reduced to a focused ablation sweep (3–4 runs of ~40 H100-hours each). Be honest that CoRL 2026 requires pre-existing preliminary results; ICLR 2027 is the realistic primary target.

6. REFRAME THE CONTRIBUTION: Given Fast-WAM and GigaWorld-Policy already solve inference efficiency, the differentiating story must be 'discrete world-state bottleneck improves out-of-distribution generalization (lighting, background clutter)' measured through OOD generalization splits in LIBERO-Spatial and ManiSkill. This is testable within compute budget and is not covered by either Fast-WAM or GigaWorld-Policy.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL VENUE MISMATCH: The user's primary requirement is CoRL 2026 (abstract deadline May 26, paper deadline May 29, 2026 — 17/20 days from today). The proposal explicitly lists CoRL 2026 as 'not feasible without pre-existing results; skip' and targets ICLR 2027 instead. This directly fails the user's stated requirement. Auto-research mode estimates 5–7 days of experiments on 8 H100s, which would deliver results by May 15–17, leaving 12–14 days to write the paper — tight but potentially achievable for a focused method submission. The proposal must either (a) attempt CoRL 2026 with a minimal experiment set, or (b) explicitly explain to the user why CoRL 2026 is infeasible and ask for venue guidance before proceeding.", "CRITICAL PROBLEM PREMISE UNVERIFIED: The proposal asserts 'SOTA models degrade from ~98% to 0–40% under visual perturbations' and positions Motus as the target model with this problem. But arXiv:2603.22078 shows that Cosmos-Policy — trained on large-scale video data, as Motus is — achieves 82–96% on visual appearance perturbations (lighting, noise, layout) on LIBERO-Plus. The proposal never reports Motus's specific LIBERO-Plus performance on visual splits. If Motus (with WAN2.2 video pretraining on large-scale data) already achieves comparable robustness to Cosmos-Policy on these splits, the proposed fix addresses a non-problem for this base model. The proposal must retrieve and report Motus's actual LIBERO-Plus visual perturbation numbers before proceeding.", "MISSING KEY COMPETITOR — XR-1/UVMC (arXiv:2511.02776, ICLR 2026): XR-1 introduces Unified Vision-Motion Codes (UVMC), a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion into a shared discrete codebook, enabling cross-embodiment transfer. This is the closest published work to the proposed VQ-Perceiver and is completely absent from the landscape. The differentiation (UVMC: joint codebook for cross-embodiment pretraining; proposed: VQ bottleneck for intra-model visual-to-action routing at inference) is valid but must be made explicit in the paper.", "MISSING DIAL (arXiv:2603.29844): DIAL introduces 'latent visual foresight within the VLM feature space as a structural bottleneck' between reasoning and action — the same conceptual goal as the proposed VQ-Perceiver, using continuous rather than discrete representations. The distinction (continuous vs. hard VQ discretization; DIAL targets intent decoupling while proposed targets appearance invariance) must be stated. Omitting DIAL leaves a major gap in the literature review.", "WRONG ROBUSTNESS TARGET: From arXiv:2603.22078, WAMs exhibit strong robustness to the visual appearance perturbations the proposal targets (lighting, background, color), but fail on geometric perturbations (camera viewpoint: 28.9%, robot initial state: 36.2%). A VQ-Perceiver that encodes object pose and contact configuration should in principle also help with task-phase geometry; if the proposal can argue that the VQ codebook helps geometric perturbations (not just appearance), the contribution would be substantially stronger and better-targeted.", "MODEL SIZE DISCREPANCY: The proposal repeatedly references '5B-parameter Motus' but the confirmed HuggingFace release shows Motus is WAN2.2-5B (video backbone) + Qwen3-VL-2B (understanding) + action expert — total ~7–8B parameters. The compute estimate of ~25–30h per run on 4 H100s for 30K LoRA steps is still plausible but must be re-verified against the actual model size. LoRA rank=64 on 7B is heavier than on 5B, potentially adding ~20% to each run."]
Feedback: The Round 1 architectural errors are cleanly fixed. The proposal now has the correct Motus architecture, corrected compute estimates within the ≤200 H100-hour budget, and removed the spurious efficiency claim. Three new issues must be resolved before this can proceed.

1. VENUE DECISION REQUIRED: Do not silently retarget to ICLR 2027. Either (a) restructure the experiment plan to target CoRL 2026 — auto-research mode gives 5–7 days of results, leaving 12–14 days to write a focused method paper; use only baseline + 2 key ablations (VQ vs. continuous, with/without attention mask) on LIBERO-Plus; this is aggressive but consistent with the user's explicit constraint; or (b) surface the venue conflict to the user and ask whether to proceed with CoRL 2026 or ICLR 2027 before investing further in the idea.

2. VERIFY MOTUS BASELINE FIRST: Before any fine-tuning, run the unmodified Motus checkpoint through LIBERO-Plus visual perturbation splits (background, lighting, color). If Motus already achieves >70% (consistent with Cosmos-Policy at 82%), the problem statement collapses. If it achieves <50%, the case is strong. This single baseline run (~3–4h on 4 H100s) is the prerequisite for the entire paper.

3. ADD UVMC/XR-1 AND DIAL TO LANDSCAPE: Add 'XR-1/UVMC (arXiv:2511.02776, ICLR 2026) — dual-branch VQ-VAE jointly encoding visual dynamics and robot motion into a shared codebook; targets cross-embodiment transfer, not intra-model visual-to-action routing.' Add 'DIAL (arXiv:2603.29844, 2026) — continuous latent visual foresight as structural bottleneck between reasoning and action; no VQ; targets intent/action decoupling, not appearance invariance.' Both are close in spirit; explicit differentiation strengthens the novelty claim.

4. REFRAME AROUND GEOMETRIC ROBUSTNESS: The evidence shows geometric perturbations (camera viewpoint, robot state) are the dominant gap for WAMs. Argue that the VQ codebook encodes task-phase state (object pose, contact configuration) that is inherently viewpoint-invariant — making the bottleneck relevant to geometric robustness as well. Add camera-viewpoint and robot-initial-state splits to the LIBERO-Plus evaluation table. This reframe makes the contribution significantly more impactful.

5. CORRECT MODEL SIZE: Update '5B-parameter Motus' to '~7B (WAN2.2-5B + Qwen3-VL-2B)' throughout the proposal and recalculate per-run compute accordingly (~30–35h on 4 H100s instead of ~25–30h, still within the ≤200 H100-hour budget for 5–6 runs).

### Round 3 review
Verdict: revise
Issues: ["CRITICAL MISSING PRIOR WORK — ReViWo (ICLR 2025): 'Learning View-Invariant World Models for Visual Robotic Manipulation' (proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e) explicitly applies VQ-VAE to decompose visual observations into view-invariant (VIR) and view-dependent (VDR) representations, then trains world models on VIR for camera-robust robot manipulation. The proposal claims 'no concurrent work applies hard VQ discretization to visual token representations...to address camera viewpoint robustness' — this claim is false. ReViWo must be added to the landscape section and the novelty claim must be reformulated around what is genuinely new: applying this principle within a modern diffusion-based 7B MoT WAM via intra-model cross-attention routing, without multi-view training data.", "COMPUTE ESTIMATE INTERNAL INCONSISTENCY: The auto-research mode states '3 CoRL-scope fine-tuning runs × ~30–35h each on 4 H100s' but quotes a total of '~120–145h H100.' Under the natural reading (30–35h wall clock on 4 H100s), the H100-hours per run = 4 × ~33h ≈ 132 H100-hours, and 3 runs = ~396 H100-hours — nearly 2× the 200 H100-hour hard limit. The budget is only satisfied if '30–35h on 4 H100s' means 30–35 aggregate H100-hours (~8h wall clock), but the 'speed bottleneck' note and '5–6 days on 8 H100s' timeline are inconsistent with 8h-per-run wall clock. This ambiguity must be resolved with explicit wall-clock vs. aggregate-GPU-hours distinction.", "STANDARD EVALUATION FIGURE MISREPRESENTED: The proposal states 'Motus achieves 87.0% on RoboTwin 2.0-Plus standard evaluation.' The confirmed overall average from arXiv:2603.22078 Table 3 is 71.5%, not 87.0%. The 87.0% is the unperturbed (standard-scene, no-perturbation) split score within RoboTwin 2.0-Plus. This distinction matters: it should be stated as 'Motus achieves 87.0% on the unperturbed split of RoboTwin 2.0-Plus (overall average 71.5%)' to avoid misleading reviewers who check the source paper.", "VQ-INVARIANCE ARGUMENT NEEDS STRENGTHENING: The claim that 'a VQ codebook with K=512 entries cannot memorize viewpoint-specific pixel patterns' is intuitive but not rigorous — 512 codes can still encode many viewpoint configurations if the Perceiver cross-attention queries learn viewpoint-specific routing. The proposal should either (a) add a theoretical bound showing that the number of training viewpoints exceeds K (information-theoretic argument), or (b) explicitly frame this as an empirical hypothesis, with codebook UMAP visualization (already planned) as the primary evidence for viewpoint-invariant clustering.", "RANDOMLY INITIALIZED VQ-PERCEIVER IN PRETRAINED SYSTEM — TRAINING RISK: Adding a randomly initialized VQ-Perceiver module (N_ws=64 cross-attention queries + K=512 codebook + commitment loss) to a pretrained 7B Motus via LoRA introduces a significant initialization mismatch. The LoRA adapters on joint attention layers must simultaneously (a) route information through the new masked pathway and (b) suppress the old video-to-action direct pathway, while the VQ-Perceiver is learning from scratch. The 5K-step warm-up schedule helps, but this is a potential training instability not acknowledged beyond the collapse monitoring note. The proposal should discuss the risk that the VQ-Perceiver is simply ignored by the model (learns near-zero cross-attention weights) during early training."]
Feedback: The proposal has made strong progress in three rounds and is close to a passable state. The two changes required for a pass verdict are: (1) Add ReViWo (ICLR 2025) to the landscape and reformulate the novelty claim honestly. The correct framing is: 'We extend the VQ-for-viewpoint-invariance principle (ReViWo, ICLR 2025) from small-scale world models to modern diffusion-based MoT WAMs, introducing a novel intra-model routing mechanism (VQ-Perceiver cross-attention replacing raw video attention in Motus 7B) that requires no multi-view training data and directly targets a confirmed 65pp camera vulnerability in the only publicly-weighted large-scale MoT WAM.' This is a strong and honest novelty statement. (2) Fix the compute estimate ambiguity by explicitly separating wall-clock hours from aggregate H100-hours. Concretely: state '~8–10h wall clock per run on 4 H100s = ~32–40 H100-hours per run; 3 CoRL runs = ~96–120 H100-hours; LIBERO-Plus baseline ~4h wall clock × 4 GPUs = ~16 H100-hours; evaluation ~5h × 4 = 20 H100-hours; total ~132–156 H100-hours.' If the actual step time is closer to 2s/step (more typical for video models), restate as ~66 H100-hours/run and flag that 3 runs = ~198 H100-hours, right at the limit. Either way, commit to a single unambiguous number. The other issues (standard evaluation phrasing, VQ invariance argument, initialization risk) are lower priority but should be addressed: rephrase '87.0% on standard evaluation' as '87.0% on the unperturbed split (71.5% overall)'; add a sentence noting that the UMAP codebook visualization is the empirical test of the viewpoint-invariance hypothesis; and mention in the approach section that if the VQ-Perceiver receives near-zero gradients in early steps the warm-up masking will be extended.

### Round 4 review
Verdict: revise
Issues: ["FACTUAL ERROR — Being-H0.7 query count: The proposal states 'N_q=64 learnable continuous latent queries' for Being-H0.7 (arXiv:2605.00078), but the actual paper uses K=16 latent reasoning queries. This misrepresentation would be caught immediately by any reviewer who reads Being-H0.7. The Perceiver-only ablation is described as 'directly isolates the value of hard VQ vs. Being-H0.7's continuous-query approach' — but N_ws=64 vs. K=16 means the ablation is not architecturally aligned with Being-H0.7 after all, which needs to be acknowledged.", "MISSING OA-WAM CAMERA SCORE: The landscape says OA-WAM 'achieves state-of-the-art on LIBERO-Plus geometric axes' but omits its specific camera score of 80.5%. This is the critical number reviewers will check. OA-WAM's 80.5% exceeds Cosmos-Policy's 75.8% (which IS quoted) and represents the current SOTA on LIBERO-Plus camera. The proposal must state this explicitly and frame the goal as beating 80.5% (on LIBERO-Plus) and closing the gap from 21.6% on RoboTwin — rather than implying Cosmos-Policy's 75.8% is the comparison target.", "BEING-H0.7 ROBOTTWIN PERFORMANCE UNADDRESSED: Being-H0.7 achieves 90.2% clean and 89.6% domain-randomized on RoboTwin 2.0. The proposal's landscape omits these numbers entirely. If 'domain-randomized' in Being-H0.7's evaluation includes camera viewpoint perturbation, the core problem (camera robustness is unsolved for WAMs) would be partially undermined. The proposal must clarify the distinction between RoboTwin 2.0 (Being-H0.7's evaluation protocol) and RoboTwin 2.0-Plus (arXiv:2603.22078's evaluation protocol with explicit camera viewpoint splits) to establish that the 21.6% Motus score refers to the latter.", "COMPUTE WORST-CASE MISSING: The proposal handles the 2s/step scenario via step reduction to 20K, but does not address the ≥3s/step scenario (plausible for a 7B video diffusion model with LoRA rank=64 and 4 H100s). At 3s/step × 20K steps × 4 GPUs = 66.7 H100-hours/run; 3 runs + overhead = ~236 H100-hours — exactly at the ceiling. A brief statement acknowledging this risk and the fallback (reduce to 2 runs if >3s/step) would close this gap."]
Feedback: The proposal has made strong progress through four rounds and is close to passing. The four remaining issues are all fixable in a quick revision: (1) Correct Being-H0.7's query count to K=16 and acknowledge the architectural mismatch with the proposed N_ws=64 ablation — reframe the ablation as 'hard VQ N_ws=64 vs. continuous Perceiver N_ws=64' rather than direct comparison with Being-H0.7. (2) State OA-WAM's specific camera score of 80.5% on LIBERO-Plus as the current SOTA baseline, not Cosmos-Policy's 75.8% — the contribution framing should be 'VQ-Perceiver on Motus targets: (a) closing the 65pp RoboTwin camera gap from 21.6%, and (b) comparing against OA-WAM's 80.5% continuous-attention SOTA on LIBERO-Plus.' (3) Add one sentence clarifying that Being-H0.7's 89.6% domain-randomized RoboTwin 2.0 score uses visual randomization (texture/lighting) not camera extrinsic perturbation, unlike the RoboTwin 2.0-Plus camera split in arXiv:2603.22078 — this preserves the validity of the core problem statement. (4) Add a single sentence fallback for the ≥3s/step scenario: reduce from 3 to 2 fine-tuning runs (main method + VQ-vs-continuous ablation), dropping the masking ablation to ICLR fallback. All four fixes are <1 paragraph each and do not require re-architecting the proposal.

### Round 5 review
Verdict: revise
Issues: ["CRITICAL EVALUATION DEPENDENCY UNVERIFIED: RoboTwin 2.0-Plus — the primary benchmark cited for Motus's 21.6% camera score — is an in-house benchmark constructed by Huawei/UToronto authors (arXiv:2603.22078), NOT an official release of the RoboTwin 2.0 platform. The official RoboTwin 2.0 repo (github.com/RoboTwin-Platform/RoboTwin) applies only minor camera jitter (1 cm), not the major viewpoint-pose perturbation measured in 2603.22078. No GitHub code for RoboTwin 2.0-Plus was found. The proposal explicitly states 'RoboTwin 2.0-Plus all 7 perturbation splits (camera viewpoint is the primary metric)' as the primary evaluation, but if the evaluation code is not available, the VQ-Perceiver team cannot run inference on VQ-Perceiver-Motus against the same 21.6% baseline they borrowed from the published paper. This makes the primary metric unreplicable without author contact or re-implementation from Appendix A — an undisclosed dependency that adds 1-2 days of implementation work to an already compressed 20-day timeline.", "MODERATE COMPARISON AMBIGUITY: Being-H0.7 achieves 84.8% aggregate on LIBERO-Plus (fine-tuned) and claims 'resilience against shifted viewpoints,' but does not publish a camera-specific breakdown score. The proposal states OA-WAM 80.5% is the 'current SOTA on LIBERO-Plus camera axis' — this is correct given published camera-specific scores, but a CoRL reviewer who reads the Being-H0.7 paper may question whether the SOTA claim accounts for Being-H0.7's higher aggregate score. The proposal should add one sentence acknowledging that Being-H0.7 reports only aggregate LIBERO-Plus scores (82.1% zero-shot / 84.8% fine-tuned) without camera-split breakdown, and therefore OA-WAM's 80.5% camera-specific score remains the only published SOTA reference for the camera axis."]
Feedback: The proposal has addressed all four Round 4 issues correctly and is verified by independent research to be factually accurate. One new critical issue emerged from fresh investigation: verify RoboTwin 2.0-Plus evaluation code availability BEFORE committing it as the primary benchmark. Concretely: (1) RoboTwin 2.0-PLUS EVALUATION CODE: Contact the arXiv:2603.22078 corresponding authors (Zhanguang Zhang, Yingxue Zhang at Huawei/UToronto) to request the evaluation code. If code is not obtainable within 1-2 days of project start, FLIP the benchmark priorities: make LIBERO-Plus the primary evaluation (fully public, arXiv:2510.13626) and RoboTwin 2.0-Plus secondary (implement from Appendix A if possible). The LIBERO-Plus evaluation has an equally strong case: OA-WAM at 80.5% camera is the published SOTA, Motus baseline needs to be run once (~4h), and camera robustness of VQ-Perceiver is directly testable. Importantly, the 21.6% Motus camera score from RoboTwin 2.0-Plus can still be cited as motivation for the problem without needing to reproduce the exact evaluation environment — as long as the improvement is demonstrated on LIBERO-Plus. (2) BEING-H0.7 AGGREGATE SCORE: Add one sentence: 'Being-H0.7 reports only aggregate LIBERO-Plus scores (82.1% zero-shot / 84.8% fine-tuned) without camera-specific breakdown; OA-WAM (arXiv:2605.06481) is the only published result with a dedicated camera split score (80.5%), making it the appropriate SOTA reference for this axis.' These are the only two remaining gaps. All factual claims are verified correct.


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
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "fa9448fd-67d0-41a2-8dac-5f9c73661c7f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:58:12.708Z_

```json
{
  "parentUuid": "fa9448fd-67d0-41a2-8dac-5f9c73661c7f",
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
  "uuid": "93ae0159-6a97-44e8-88a4-65f6aa0ea34b",
  "timestamp": "2026-05-10T08:58:12.708Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:58:12.708Z_

```json
{
  "parentUuid": "93ae0159-6a97-44e8-88a4-65f6aa0ea34b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2a91a3e4-354b-45cd-9cf5-17abb6f9d226",
  "timestamp": "2026-05-10T08:58:12.708Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
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
  "leafUuid": "2a91a3e4-354b-45cd-9cf5-17abb6f9d226",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:58:29.767Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. This is Round 6 of 10 for reviewing the VQ-Perceiver World-State Bottleneck idea for CoRL 2026. Let me check what's been addressed from Round 5 and do independent verification.

From Round 5 feedback, two issues needed to be addressed:
1. CRITICAL: RoboTwin 2.0-Plus evaluation code availability - The proposal needed to flip benchmark priorities making LIBERO-Plus primary and RoboTwin 2.0-Plus secondary
2. MODERATE: Being-H0.7 aggregate score clarification

Looking at the current (Round 6) proposal:

**Issue 1 - RoboTwin 2.0-Plus evaluation code:**


The proposal now explicitly addresses this with a clear note that RoboTwin 2.0-Plus lacks public evaluation code and formal specifications, while LIBERO-Plus is positioned as the primary benchmark with a contingency protocol: contact authors within 2 days, implement from Appendix A if needed, or fall back to LIBERO-Plus as sole primary. This appears resolved.

**Issue 2 - Being-H0.7 aggregate score:**
The proposal clarifies that Being-H0.7 only reports aggregate LIBERO-Plus scores without camera-specific breakdowns, so claims about resilience to viewpoint shifts are inferences rather than disaggregated measurements. OA-WAM is now identified as the appropriate SOTA reference since it's the only published result with a dedicated LIBERO-Plus camera split score.

Now I'm running independent verification searches to catch any issues I might have missed, starting with whether Motus actually exists as a published work. I'm going to search for these papers and claims systematically to verify their existence and accuracy, starting with the arXiv papers and then checking for any competing work in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a91a3e4-354b-45cd-9cf5-17abb6f9d226",
  "isSidechain": false,
  "requestId": "req_011CatcSiUbNUDfqPKrSqVj9",
  "type": "assistant",
  "uuid": "49e2c9a8-837f-4c18-a9b7-cc0eee7500ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017f4pEPrhZ51a8byiLRSPvW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27980,
      "cache_read_input_tokens": 11631,
      "output_tokens": 831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 831,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27980
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

_source line 9 · 2026-05-10T08:58:29.793Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Gr3Kj4c9YN57Qge44NeJ1s`</summary>

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
  "parentUuid": "49e2c9a8-837f-4c18-a9b7-cc0eee7500ca",
  "isSidechain": false,
  "requestId": "req_011CatcSiUbNUDfqPKrSqVj9",
  "type": "assistant",
  "uuid": "6316c027-c11e-4b0c-95df-566892882289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017f4pEPrhZ51a8byiLRSPvW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27980,
      "cache_read_input_tokens": 11631,
      "output_tokens": 831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 831,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 27980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27980
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

_source line 10 · 2026-05-10T08:58:29.800Z_

<details><summary>↩ Tool result · `toolu_01Gr3Kj4c9YN57Qge44NeJ1s`</summary>

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
  "parentUuid": "6316c027-c11e-4b0c-95df-566892882289",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "aba9e75e-34cb-44f2-812e-1395a23825bb",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "6316c027-c11e-4b0c-95df-566892882289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T08:58:35.139Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do independent verification searches on the key claims in this proposal. I'll run multiple searches in parallel to be efficient.

Key things to verify:
1. OA-WAM (arXiv:2605.06481) - does it exist? Does it have 80.5% camera score on LIBERO-Plus?
2. Being-H0.7 (arXiv:2605.00078) - does it exist? K=16 latent reasoning queries?
3. Motus (arXiv:2512.13030) and camera vulnerability 21.6%
4. arXiv:2603.22078 - "Do World Action Models Generalize Better than VLAs?"


5. ReViWo (ICLR 2025) - does it exist?
6. Any new concurrent work in May 2026 that might overlap with VQ-Perceiver for camera robustness

I'll search for these in parallel to check their validity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aba9e75e-34cb-44f2-812e-1395a23825bb",
  "isSidechain": false,
  "requestId": "req_011CatcTzBBKwaAzB8BBGqV3",
  "type": "assistant",
  "uuid": "909bc874-5877-454b-8f1b-2a752ee3fc79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017WY63hggfYhiQXJJJWY1VU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 39611,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 450,
          "cache_read_input_tokens": 39611,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1851
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

_source line 12 · 2026-05-10T08:58:35.139Z_

I'll conduct independent verification searches on the key claims before issuing a verdict. Running parallel searches now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "909bc874-5877-454b-8f1b-2a752ee3fc79",
  "isSidechain": false,
  "requestId": "req_011CatcTzBBKwaAzB8BBGqV3",
  "type": "assistant",
  "uuid": "79d0ed31-7365-41fd-b1d8-5130e900b7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017WY63hggfYhiQXJJJWY1VU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 39611,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 450,
          "cache_read_input_tokens": 39611,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1851
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

_source line 13 · 2026-05-10T08:58:35.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UosthL5z15Kh6UYxMiRM6H`</summary>

```json
{
  "query": "OA-WAM object addressable world action model LIBERO-Plus camera robustness arXiv 2605.06481"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d0ed31-7365-41fd-b1d8-5130e900b7e0",
  "isSidechain": false,
  "requestId": "req_011CatcTzBBKwaAzB8BBGqV3",
  "type": "assistant",
  "uuid": "4c2e875f-cdcd-4bf1-8ea6-0d8860145c87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017WY63hggfYhiQXJJJWY1VU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 39611,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 450,
          "cache_read_input_tokens": 39611,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1851
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

_source line 14 · 2026-05-10T08:58:35.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G6k5aUETS7msZicvLLeahV`</summary>

```json
{
  "query": "Being-H0.7 latent world action model egocentric arXiv 2605.00078 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2e875f-cdcd-4bf1-8ea6-0d8860145c87",
  "isSidechain": false,
  "requestId": "req_011CatcTzBBKwaAzB8BBGqV3",
  "type": "assistant",
  "uuid": "464e74b7-3534-41eb-91b3-3996d96418a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017WY63hggfYhiQXJJJWY1VU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 39611,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 450,
          "cache_read_input_tokens": 39611,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1851
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

_source line 15 · 2026-05-10T08:58:36.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DxbXw1TYXMvA1dEK5rNtap`</summary>

```json
{
  "query": "VQ-Perceiver camera viewpoint robustness world action model diffusion 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "464e74b7-3534-41eb-91b3-3996d96418a8",
  "isSidechain": false,
  "requestId": "req_011CatcTzBBKwaAzB8BBGqV3",
  "type": "assistant",
  "uuid": "cb299a76-a9a6-4cd7-a57c-8f095b3f7698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017WY63hggfYhiQXJJJWY1VU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 39611,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 450,
          "cache_read_input_tokens": 39611,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1851
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

_source line 16 · 2026-05-10T08:58:41.760Z_

<details><summary>↩ Tool result · `toolu_01UosthL5z15Kh6UYxMiRM6H`</summary>

```text
Web search results for query: "OA-WAM object addressable world action model LIBERO-Plus camera robustness arXiv 2605.06481"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[2605.04443] Dissociating spatial frequency reliance from adversarial robustness advantages in neurally guided deep convolutional neural networks","url":"https://arxiv.org/abs/2605.04443"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"}]

I found the research paper you're looking for. Here's what the search revealed:

The paper "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation" was published on arXiv as 2605.06481v1 on May 7, 2026, with authors from Tsinghua University, Shanghai Jiao Tong University, and Nanyang Technological University.

On in-distribution LIBERO and SimplerEnv WidowX (Visual Matching) benchmarks, OA-WAM achieves approximately 79.3% average success rate, leading all published VLA and WAM baselines. 

Regarding camera robustness specifically, on the LIBERO-Plus robustness benchmark, OA-WAM achieves approximately 85.7% success rate on the camera axis, and sets a new state-of-the-art on the geometric axes most aligned with the hypothesis. OA-WAM sets a new SOTA on the geometric LIBERO-Plus axes with a geometric average of 76.0%.

The object-addressable interface is the key source of the robustness pattern, as confirmed through ablations and slot-intervention tests.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c2e875f-cdcd-4bf1-8ea6-0d8860145c87",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "4268d6e6-e062-4370-872d-3fb9d9e602e7",
  "toolUseResult": {
    "query": "OA-WAM object addressable world action model LIBERO-Plus camera robustness arXiv 2605.06481",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RSLubbWtXcurZBo5zyhacs",
        "content": [
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
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
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2510.13626v2"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "[2605.04443] Dissociating spatial frequency reliance from adversarial robustness advantages in neurally guided deep convolutional neural networks",
            "url": "https://arxiv.org/abs/2605.04443"
          },
          {
            "title": "LIBERO-X: Robustness Litmus for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.06556v1"
          },
          {
            "title": "When to Trust Imagination: Adaptive Action Execution for World Action Models",
            "url": "https://arxiv.org/html/2605.06222"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what the search revealed:\n\nThe paper \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation\" was published on arXiv as 2605.06481v1 on May 7, 2026, with authors from Tsinghua University, Shanghai Jiao Tong University, and Nanyang Technological University.\n\nOn in-distribution LIBERO and SimplerEnv WidowX (Visual Matching) benchmarks, OA-WAM achieves approximately 79.3% average success rate, leading all published VLA and WAM baselines. \n\nRegarding camera robustness specifically, on the LIBERO-Plus robustness benchmark, OA-WAM achieves approximately 85.7% success rate on the camera axis, and sets a new state-of-the-art on the geometric axes most aligned with the hypothesis. OA-WAM sets a new SOTA on the geometric LIBERO-Plus axes with a geometric average of 76.0%.\n\nThe object-addressable interface is the key source of the robustness pattern, as confirmed through ablations and slot-intervention tests."
    ],
    "durationSeconds": 6.013026704
  },
  "sourceToolAssistantUUID": "4c2e875f-cdcd-4bf1-8ea6-0d8860145c87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T08:58:42.945Z_

<details><summary>↩ Tool result · `toolu_01G6k5aUETS7msZicvLLeahV`</summary>

```text
Web search results for query: "Being-H0.7 latent world action model egocentric arXiv 2605.00078 2026"

Links: [{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub","url":"https://github.com/BeingBeyond/Being-H"},{"title":"human-motion-arxiv-daily/README.md at main · AndrewDing616/human-motion-arxiv-daily","url":"https://github.com/AndrewDing616/human-motion-arxiv-daily/blob/main/README.md"},{"title":"Being-H0.7: A Latent World-Action Model from ... - BeingBeyond","url":"https://research.beingbeyond.com/being-h07"},{"title":"Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/html/2507.15597v1"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/html/2601.12993v1"},{"title":"Being-H0: Vision-Language-Action Model | PDF | Learning | Cognitive Science","url":"https://www.scribd.com/document/900573442/Being-H0"},{"title":"EgoAgent: A Joint Predictive Agent Model in Egocentric Worlds","url":"https://arxiv.org/html/2502.05857v3"},{"title":"Being-H0.5: Unified Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/being-h0-5"},{"title":"Co-Evolving Latent Action World Models","url":"https://arxiv.org/html/2510.26433v1"}]

Based on the search results, I found detailed information about Being-H0.7:

## Being-H0.7: A Latent World-Action Model from Egocentric Videos

Being-H0.7 is a latent world-action model pretrained from large-scale egocentric videos. The paper is available on arXiv with identifier 2605.00078v1, posted on April 30, 2026.

### Key Architecture and Design

Instead of predicting future frames, Being-H0.7 introduces a small set of learnable latent queries between the multimodal context and the action tokens. A latent reasoning space is introduced via a set of latent queries in the prior branch, and is further endowed with world modeling by the joint alignment with a future-aware posterior branch.

### Training and Performance

Being-H0.7 is trained on 200,000 hours of egocentric human videos together with 15,000 hours of robot demonstrations. Across six widely used simulation benchmarks, Being-H0.7 reaches the strongest overall performance and the best average rank.

### Key Innovation

The model was designed to enable robots to reason about future interaction in a compact latent space and act immediately without explicit future-image generation at test time, while keeping the predictive value of world modeling through a deployable latent action prior rather than a pixel-space rollout.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "464e74b7-3534-41eb-91b3-3996d96418a8",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "57898a29-0fc0-468a-ac5b-d1a4402db1ad",
  "toolUseResult": {
    "query": "Being-H0.7 latent world action model egocentric arXiv 2605.00078 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0168NLW2qXcc8bU78MQw47H8",
        "content": [
          {
            "title": "Being-H0.7: A Latent World-Action Model from Egocentric Videos",
            "url": "https://arxiv.org/html/2605.00078v1"
          },
          {
            "title": "GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub",
            "url": "https://github.com/BeingBeyond/Being-H"
          },
          {
            "title": "human-motion-arxiv-daily/README.md at main · AndrewDing616/human-motion-arxiv-daily",
            "url": "https://github.com/AndrewDing616/human-motion-arxiv-daily/blob/main/README.md"
          },
          {
            "title": "Being-H0.7: A Latent World-Action Model from ... - BeingBeyond",
            "url": "https://research.beingbeyond.com/being-h07"
          },
          {
            "title": "Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos",
            "url": "https://arxiv.org/html/2507.15597v1"
          },
          {
            "title": "Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization",
            "url": "https://arxiv.org/html/2601.12993v1"
          },
          {
            "title": "Being-H0: Vision-Language-Action Model | PDF | Learning | Cognitive Science",
            "url": "https://www.scribd.com/document/900573442/Being-H0"
          },
          {
            "title": "EgoAgent: A Joint Predictive Agent Model in Egocentric Worlds",
            "url": "https://arxiv.org/html/2502.05857v3"
          },
          {
            "title": "Being-H0.5: Unified Vision-Language-Action Model",
            "url": "https://www.emergentmind.com/topics/being-h0-5"
          },
          {
            "title": "Co-Evolving Latent Action World Models",
            "url": "https://arxiv.org/html/2510.26433v1"
          }
        ]
      },
      "Based on the search results, I found detailed information about Being-H0.7:\n\n## Being-H0.7: A Latent World-Action Model from Egocentric Videos\n\nBeing-H0.7 is a latent world-action model pretrained from large-scale egocentric videos. The paper is available on arXiv with identifier 2605.00078v1, posted on April 30, 2026.\n\n### Key Architecture and Design\n\nInstead of predicting future frames, Being-H0.7 introduces a small set of learnable latent queries between the multimodal context and the action tokens. A latent reasoning space is introduced via a set of latent queries in the prior branch, and is further endowed with world modeling by the joint alignment with a future-aware posterior branch.\n\n### Training and Performance\n\nBeing-H0.7 is trained on 200,000 hours of egocentric human videos together with 15,000 hours of robot demonstrations. Across six widely used simulation benchmarks, Being-H0.7 reaches the strongest overall performance and the best average rank.\n\n### Key Innovation\n\nThe model was designed to enable robots to reason about future interaction in a compact latent space and act immediately without explicit future-image generation at test time, while keeping the predictive value of world modeling through a deployable latent action prior rather than a pixel-space rollout."
    ],
    "durationSeconds": 6.966158671999998
  },
  "sourceToolAssistantUUID": "464e74b7-3534-41eb-91b3-3996d96418a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T08:58:46.190Z_

<details><summary>↩ Tool result · `toolu_01DxbXw1TYXMvA1dEK5rNtap`</summary>

```text
Web search results for query: "VQ-Perceiver camera viewpoint robustness world action model diffusion 2026"

Links: [{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05868v1"},{"title":"X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving","url":"https://arxiv.org/html/2603.19979v1"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LEARNING VIEW-INVARIANT WORLD MODELS FOR ...","url":"https://openreview.net/pdf?id=vJwjWyt4Ed"},{"title":"[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05868"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"GigaBrain-0: A World Model-Powered Vision-Language- Action Model","url":"https://arxiv.org/html/2510.19430v1"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"},{"title":"Stable Virtual Camera: Generative View Synthesis with Diffusion Models","url":"https://stable-virtual-camera.github.io/"}]

Based on the search results, here are the key findings related to your query about VQ-Perceiver, camera viewpoint robustness, world action models, and diffusion-based approaches in 2026:

## Camera Viewpoint Robustness Challenges

Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. This remains a significant challenge for vision-language-action (VLA) models despite recent advances.

## Diffusion-Based and World Action Models

Recent research examines both autoregressive and diffusion-based architectures. A series of representative open-checkpoint models spanning diverse architectures (autoregressive vs. diffusion-based) and training paradigms (web-data co-training, world modeling, reinforcement learning, etc) are being analyzed.

Interestingly, despite strong performance in visual perturbations, WAMs (World Action Models) show reduced consistency and struggle with geometric perturbations, specifically variations in camera viewpoint and the robot's initial state, suggesting that while WAMs excel at understanding dynamic visual changes, their video priors offer limited benefit when the fundamental geometric configuration of the scene or robot is altered.

## Addressing Viewpoint Robustness

A zero-shot camera adaptation framework has been proposed without additional demonstration data, policy fine-tuning, or architectural modification, with the key idea to virtually adjust test-time camera observations to match the training camera configuration in real-time using a feed-forward novel view synthesis model.

The search results show active research into improving viewpoint robustness through various approaches, including world model-based data augmentation and novel view synthesis techniques integrated with diffusion models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb299a76-a9a6-4cd7-a57c-8f095b3f7698",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "40481ae5-4a1c-4d50-880e-8087e9efc356",
  "toolUseResult": {
    "query": "VQ-Perceiver camera viewpoint robustness world action model diffusion 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JDjyeZFfHK69R18Q5iDpYv",
        "content": [
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.05868v1"
          },
          {
            "title": "X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving",
            "url": "https://arxiv.org/html/2603.19979v1"
          },
          {
            "title": "IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...",
            "url": "https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"
          },
          {
            "title": "LEARNING VIEW-INVARIANT WORLD MODELS FOR ...",
            "url": "https://openreview.net/pdf?id=vJwjWyt4Ed"
          },
          {
            "title": "[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.05868"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]",
            "url": "https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"
          },
          {
            "title": "GigaBrain-0: A World Model-Powered Vision-Language- Action Model",
            "url": "https://arxiv.org/html/2510.19430v1"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"
          },
          {
            "title": "Stable Virtual Camera: Generative View Synthesis with Diffusion Models",
            "url": "https://stable-virtual-camera.github.io/"
          }
        ]
      },
      "Based on the search results, here are the key findings related to your query about VQ-Perceiver, camera viewpoint robustness, world action models, and diffusion-based approaches in 2026:\n\n## Camera Viewpoint Robustness Challenges\n\nModels are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. This remains a significant challenge for vision-language-action (VLA) models despite recent advances.\n\n## Diffusion-Based and World Action Models\n\nRecent research examines both autoregressive and diffusion-based architectures. A series of representative open-checkpoint models spanning diverse architectures (autoregressive vs. diffusion-based) and training paradigms (web-data co-training, world modeling, reinforcement learning, etc) are being analyzed.\n\nInterestingly, despite strong performance in visual perturbations, WAMs (World Action Models) show reduced consistency and struggle with geometric perturbations, specifically variations in camera viewpoint and the robot's initial state, suggesting that while WAMs excel at understanding dynamic visual changes, their video priors offer limited benefit when the fundamental geometric configuration of the scene or robot is altered.\n\n## Addressing Viewpoint Robustness\n\nA zero-shot camera adaptation framework has been proposed without additional demonstration data, policy fine-tuning, or architectural modification, with the key idea to virtually adjust test-time camera observations to match the training camera configuration in real-time using a feed-forward novel view synthesis model.\n\nThe search results show active research into improving viewpoint robustness through various approaches, including world model-based data augmentation and novel view synthesis techniques integrated with diffusion models."
    ],
    "durationSeconds": 9.698738339
  },
  "sourceToolAssistantUUID": "cb299a76-a9a6-4cd7-a57c-8f095b3f7698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
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
  "leafUuid": "40481ae5-4a1c-4d50-880e-8087e9efc356",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Assistant

_source line 21 · 2026-05-10T08:59:02.486Z_

<details><summary>Logged reasoning block</summary>

```text
Important finding: The OA-WAM search result says the camera score is ~85.7%, not 80.5% as stated in the proposal! The proposal says "OA-WAM at 80.5% (arXiv:2605.06481, Table 2)" but the search result says "approximately 85.7% success rate on the camera axis." This is a potentially critical discrepancy. I need to verify this more carefully by fetching the actual paper.

Also, I notice the Being-H0.7 search confirms it exists at arXiv:2605.00078v1, consistent with the proposal.


I'm going to pull the OA-WAM paper directly to check what the actual camera score is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40481ae5-4a1c-4d50-880e-8087e9efc356",
  "isSidechain": false,
  "requestId": "req_011CatcVBRdc2unCzyvohuj7",
  "type": "assistant",
  "uuid": "c2fdf588-1fbc-476c-9020-9c591d12f386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TaMY74GyCoFjALqvJna1BL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 41462,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 41462,
          "cache_creation_input_tokens": 3069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3069
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

_source line 22 · 2026-05-10T08:59:02.510Z_

Important discrepancy found: the search says OA-WAM achieves ~85.7% on camera axis, not 80.5% as the proposal claims. Let me verify by reading the actual paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2fdf588-1fbc-476c-9020-9c591d12f386",
  "isSidechain": false,
  "requestId": "req_011CatcVBRdc2unCzyvohuj7",
  "type": "assistant",
  "uuid": "bb436b54-fcc7-46f7-be22-f1b7bdd22b2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TaMY74GyCoFjALqvJna1BL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 41462,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 41462,
          "cache_creation_input_tokens": 3069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3069
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

_source line 23 · 2026-05-10T08:59:03.752Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019ibaqWSzbEzdMX6tpPk87Y`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "What is OA-WAM's camera axis score on LIBERO-Plus? Find Table 2 or any table showing camera robustness scores. Report exact numbers for camera, geometric average, and overall scores. Also confirm the model architecture - is it slot-based attention? What is the comparison against OA-WAM, Cosmos-Policy, Being-H0.7 for camera specifically?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb436b54-fcc7-46f7-be22-f1b7bdd22b2f",
  "isSidechain": false,
  "requestId": "req_011CatcVBRdc2unCzyvohuj7",
  "type": "assistant",
  "uuid": "3316fa07-6d4d-48db-980c-4342ce43a996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TaMY74GyCoFjALqvJna1BL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 41462,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 41462,
          "cache_creation_input_tokens": 3069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3069
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

_source line 24 · 2026-05-10T08:59:04.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QGu19WT3h7iTxpvcWEyBN7`</summary>

```json
{
  "query": "arXiv:2603.22078 \"Do World Action Models Generalize Better\" Motus camera 21.6% RoboTwin 2.0-Plus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3316fa07-6d4d-48db-980c-4342ce43a996",
  "isSidechain": false,
  "requestId": "req_011CatcVBRdc2unCzyvohuj7",
  "type": "assistant",
  "uuid": "ac67c9b2-f937-4a62-9215-9c9b0151dd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TaMY74GyCoFjALqvJna1BL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 41462,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 41462,
          "cache_creation_input_tokens": 3069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3069
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

_source line 25 · 2026-05-10T08:59:08.848Z_

<details><summary>↩ Tool result · `toolu_019ibaqWSzbEzdMX6tpPk87Y`</summary>

```text
# OA-WAM Camera Performance Analysis

## Camera Axis Score (LIBERO-Plus)

According to Table 2, OA-WAM achieves **80.5%** on the camera perturbation axis, which represents a **+4.7% improvement** over the previous best baseline (Cosmos-Policy at 75.8%).

## Key Benchmark Comparisons

| Model | Camera | Geo Avg | Overall Avg |
|-------|--------|---------|------------|
| OA-WAM | 80.5% | 84.3% | 83.9% |
| Cosmos-Policy | 75.8% | 73.8% | 82.2% |
| π₀.₅ | 75.4% | 79.5% | 85.7% |

Note: Being-H0.7 does not appear in the provided comparison tables.

## Architecture Confirmation

Yes, OA-WAM uses slot-based attention. The paper describes "per-slot state tokens" with a "frozen identity address" that routes "cross-slot attention on addr alone at every transformer layer." This architectural choice specifically targets geometric robustness when camera viewpoints shift while target object identity remains constant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3316fa07-6d4d-48db-980c-4342ce43a996",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "7e9c1a46-8c29-493b-901f-29ad3c353998",
  "toolUseResult": {
    "bytes": 793456,
    "code": 200,
    "codeText": "OK",
    "result": "# OA-WAM Camera Performance Analysis\n\n## Camera Axis Score (LIBERO-Plus)\n\nAccording to Table 2, OA-WAM achieves **80.5%** on the camera perturbation axis, which represents a **+4.7% improvement** over the previous best baseline (Cosmos-Policy at 75.8%).\n\n## Key Benchmark Comparisons\n\n| Model | Camera | Geo Avg | Overall Avg |\n|-------|--------|---------|------------|\n| OA-WAM | 80.5% | 84.3% | 83.9% |\n| Cosmos-Policy | 75.8% | 73.8% | 82.2% |\n| π₀.₅ | 75.4% | 79.5% | 85.7% |\n\nNote: Being-H0.7 does not appear in the provided comparison tables.\n\n## Architecture Confirmation\n\nYes, OA-WAM uses slot-based attention. The paper describes \"per-slot state tokens\" with a \"frozen identity address\" that routes \"cross-slot attention on addr alone at every transformer layer.\" This architectural choice specifically targets geometric robustness when camera viewpoints shift while target object identity remains constant.",
    "durationMs": 5091,
    "url": "https://arxiv.org/html/2605.06481v1"
  },
  "sourceToolAssistantUUID": "3316fa07-6d4d-48db-980c-4342ce43a996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T08:59:11.313Z_

<details><summary>↩ Tool result · `toolu_01QGu19WT3h7iTxpvcWEyBN7`</summary>

```text
Web search results for query: "arXiv:2603.22078 "Do World Action Models Generalize Better" Motus camera 21.6% RoboTwin 2.0-Plus"

Links: [{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.22078"},{"title":"Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://huggingface.co/papers/2603.22078"},{"title":"Motus: A Unified Latent Action World Model","url":"https://arxiv.org/html/2512.13030v2"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://www.wispaper.ai/en/blog/world-action-models-generalize-better-than-vlas-20260324/eng"}]

I found the paper and relevant information about your search query. Here are the key findings:

## Paper Overview

arXiv:2603.22078 is titled "Do World Action Models Generalize Better than VLAs? A Robustness Study". The paper conducts a comparative study of prominent state-of-the-art VLA policies and recently released WAMs, evaluating their performance on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations.

## Key Results

Regarding the models mentioned in your query:

- **MOTUS (camera)**: On RoboTwin 2.0-Plus, MOTUS achieves the highest robot initial-state robustness (85.0%) and the second-best overall score (71.5%).

- **RoboTwin 2.0-Plus**: LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus.

## Main Findings

WAMs, by leveraging spatiotemporal priors from video generation backbones, consistently demonstrate strong robustness to noise, lighting, and layout perturbations—a pattern that holds across both single-arm (LIBERO) and bimanual (RoboTwin) settings. However, camera viewpoint and robot initial-state perturbations remain challenging for WAMs, indicating that video priors offer limited benefit when the geometric configuration of the scene is altered.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac67c9b2-f937-4a62-9215-9c9b0151dd62",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "bb89898a-4051-48c1-a68e-f494f1b7b44e",
  "toolUseResult": {
    "query": "arXiv:2603.22078 \"Do World Action Models Generalize Better\" Motus camera 21.6% RoboTwin 2.0-Plus",
    "results": [
      {
        "tool_use_id": "srvtoolu_018J8PAjQEsWHjg54aYYCcVF",
        "content": [
          {
            "title": "[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/abs/2603.22078"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.22078"
          },
          {
            "title": "Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://huggingface.co/papers/2603.22078"
          },
          {
            "title": "Motus: A Unified Latent Action World Model",
            "url": "https://arxiv.org/html/2512.13030v2"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]",
            "url": "https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"
          },
          {
            "title": "GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub",
            "url": "https://github.com/robbyant/lingbot-va"
          },
          {
            "title": "GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub",
            "url": "https://github.com/thu-ml/Motus"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://www.wispaper.ai/en/blog/world-action-models-generalize-better-than-vlas-20260324/eng"
          }
        ]
      },
      "I found the paper and relevant information about your search query. Here are the key findings:\n\n## Paper Overview\n\narXiv:2603.22078 is titled \"Do World Action Models Generalize Better than VLAs? A Robustness Study\". The paper conducts a comparative study of prominent state-of-the-art VLA policies and recently released WAMs, evaluating their performance on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations.\n\n## Key Results\n\nRegarding the models mentioned in your query:\n\n- **MOTUS (camera)**: On RoboTwin 2.0-Plus, MOTUS achieves the highest robot initial-state robustness (85.0%) and the second-best overall score (71.5%).\n\n- **RoboTwin 2.0-Plus**: LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus.\n\n## Main Findings\n\nWAMs, by leveraging spatiotemporal priors from video generation backbones, consistently demonstrate strong robustness to noise, lighting, and layout perturbations—a pattern that holds across both single-arm (LIBERO) and bimanual (RoboTwin) settings. However, camera viewpoint and robot initial-state perturbations remain challenging for WAMs, indicating that video priors offer limited benefit when the geometric configuration of the scene is altered."
    ],
    "durationSeconds": 6.530822523000003
  },
  "sourceToolAssistantUUID": "ac67c9b2-f937-4a62-9215-9c9b0151dd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T08:59:19.331Z_

<details><summary>Logged reasoning block</summary>

```text
Good, OA-WAM's camera score is confirmed at 80.5% (not 85.7% as the initial search summary suggested - that was inaccurate). The actual paper confirms:
- OA-WAM: Camera 80.5%, Geo Avg 84.3%, Overall 83.9% 
- The earlier search result was summarizing π₀.₅'s score as OA-WAM's

Now let me check a few more things:
1. The arXiv:2603.22078 search confirms the paper exists but doesn't explicitly mention the "21.6%" camera score for Motus. 

The search results show MOTUS achieving 85.0% robot initial-state robustness and 71.5% overall score, which aligns with the proposal, though I haven't yet found confirmation of that specific 21.6% camera score. I should search more directly for that metric. I'm also looking for any recent work from May 2026 that tackles the VQ bottleneck in viewpoint-invariant WAMs, or concurrent research on viewpoint-invariant representations published around April-May 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb89898a-4051-48c1-a68e-f494f1b7b44e",
  "isSidechain": false,
  "requestId": "req_011CatcX2mY9HvWQT374rtuE",
  "type": "assistant",
  "uuid": "9a5f54db-5add-4ed9-ae17-2c73143ce2c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016i5rZNXUX3crJ5NyEY86Rv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 44531,
      "output_tokens": 513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 513,
          "cache_read_input_tokens": 44531,
          "cache_creation_input_tokens": 1703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1703
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

_source line 28 · 2026-05-10T08:59:19.489Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S4rKSmqjfzkaoDWox3Kq1P`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078v1",
  "prompt": "Find Table 3 showing RoboTwin 2.0-Plus results. What is Motus's camera viewpoint score? What is Motus's overall score? Is the camera viewpoint perturbation one of the 7 axes? Is there a public GitHub or evaluation code for RoboTwin 2.0-Plus? Who are the corresponding authors?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a5f54db-5add-4ed9-ae17-2c73143ce2c2",
  "isSidechain": false,
  "requestId": "req_011CatcX2mY9HvWQT374rtuE",
  "type": "assistant",
  "uuid": "187d62d8-6f29-43f2-9352-7d7a4d6359e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016i5rZNXUX3crJ5NyEY86Rv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 44531,
      "output_tokens": 513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 513,
          "cache_read_input_tokens": 44531,
          "cache_creation_input_tokens": 1703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1703
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

_source line 29 · 2026-05-10T08:59:19.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016HXrf9YCiKnZ42RHy9ZfTH`</summary>

```json
{
  "query": "discrete bottleneck viewpoint invariant camera robust robot manipulation world model 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "187d62d8-6f29-43f2-9352-7d7a4d6359e3",
  "isSidechain": false,
  "requestId": "req_011CatcX2mY9HvWQT374rtuE",
  "type": "assistant",
  "uuid": "5163e5e4-5ad1-4668-aa3c-1af433ae0bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016i5rZNXUX3crJ5NyEY86Rv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 44531,
      "output_tokens": 513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 513,
          "cache_read_input_tokens": 44531,
          "cache_creation_input_tokens": 1703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1703
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

_source line 30 · 2026-05-10T08:59:23.133Z_

<details><summary>↩ Tool result · `toolu_01S4rKSmqjfzkaoDWox3Kq1P`</summary>

```text
# RoboTwin 2.0-Plus Analysis

**MOTUS Camera Score:** 21.6%

**MOTUS Overall Score:** 71.5%

**Camera Viewpoint as Perturbation Axis:** Yes, camera viewpoint is one of seven perturbation dimensions. The paper specifies: "perturbations are applied along the following axes: (1) Camera, altering the viewpoint pose of the third-person camera; (2) Robot, varying the initial joint configuration; (3) Language..."

**GitHub/Evaluation Code:** The paper does not mention a public GitHub repository or evaluation code link for RoboTwin 2.0-Plus in the provided content.

**Corresponding Authors:** The paper indicates: "Corresponding to {zhanguang.zhang, yingxue.zhang}@huawei.com" - identifying Zhanguang Zhang and Yingxue Zhang as the corresponding authors affiliated with Huawei Technologies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "187d62d8-6f29-43f2-9352-7d7a4d6359e3",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "d6fe628a-2968-4aae-94a5-9584160ffb49",
  "toolUseResult": {
    "bytes": 379226,
    "code": 200,
    "codeText": "OK",
    "result": "# RoboTwin 2.0-Plus Analysis\n\n**MOTUS Camera Score:** 21.6%\n\n**MOTUS Overall Score:** 71.5%\n\n**Camera Viewpoint as Perturbation Axis:** Yes, camera viewpoint is one of seven perturbation dimensions. The paper specifies: \"perturbations are applied along the following axes: (1) Camera, altering the viewpoint pose of the third-person camera; (2) Robot, varying the initial joint configuration; (3) Language...\"\n\n**GitHub/Evaluation Code:** The paper does not mention a public GitHub repository or evaluation code link for RoboTwin 2.0-Plus in the provided content.\n\n**Corresponding Authors:** The paper indicates: \"Corresponding to {zhanguang.zhang, yingxue.zhang}@huawei.com\" - identifying Zhanguang Zhang and Yingxue Zhang as the corresponding authors affiliated with Huawei Technologies.",
    "durationMs": 3639,
    "url": "https://arxiv.org/html/2603.22078v1"
  },
  "sourceToolAssistantUUID": "187d62d8-6f29-43f2-9352-7d7a4d6359e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T08:59:27.637Z_

<details><summary>↩ Tool result · `toolu_016HXrf9YCiKnZ42RHy9ZfTH`</summary>

```text
Web search results for query: "discrete bottleneck viewpoint invariant camera robust robot manipulation world model 2026 arXiv"

Links: [{"title":"Learning View-invariant World Models for Visual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vJwjWyt4Ed"},{"title":"LEARNING VIEW-INVARIANT WORLD MODELS FOR ...","url":"https://openreview.net/pdf?id=vJwjWyt4Ed"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05868"},{"title":"View-Invariant Policy Learning via Zero-Shot Novel View Synthesis","url":"https://arxiv.org/html/2409.03685v1"},{"title":"Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning","url":"https://arxiv.org/html/2510.02268v1"},{"title":"Multi-View Masked World Models for Visual Robotic Manipulation","url":"https://proceedings.mlr.press/v202/seo23a/seo23a.pdf"},{"title":"1 A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://www.techrxiv.org/users/935947/articles/1356038/master/file/data/A%20Step%20Toward%20World%20Models2/A%20Step%20Toward%20World%20Models2.pdf?inline=true"},{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/html/2604.19683"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"}]

Based on the search results, I found several relevant papers related to your query about discrete bottleneck, viewpoint invariant, camera robust robot manipulation, and world models from 2026 on arXiv:

## Key Findings:

1. **ReViWo (Learning View-invariant World Models for Visual Robotic Manipulation)** - This paper proposes ReViWo, which leverages multi-view data to learn robust representations for control under viewpoint disturbance, utilizing an autoencoder framework that combines view-invariant representation (VIR) and view-dependent representation.

2. **AnyCamVLA (Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models)** - The key idea is to virtually adjust test-time camera observations to match the training camera configuration in real-time using a feed-forward novel view synthesis model that handles both extrinsic and intrinsic parameters. This approach enhances viewpoint robustness in real-world robotic manipulation scenarios, including settings with varying camera extrinsics, intrinsics, and freely moving handheld cameras.

3. **Camera Conditioning for View-Invariant Policy Learning** - One approach studies view-invariant imitation learning by explicitly conditioning policies on camera extrinsics, showing that conditioning on extrinsics significantly improves generalization across viewpoints for standard behavior cloning policies.

4. **Mask World Model** - Recent work on predicting what matters for robust robot policy learning that addresses appearance-centric modeling challenges in world models for robotics.

These papers address the challenge of making robot manipulation policies robust to camera viewpoint changes, which is essential for real-world robotic deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5163e5e4-5ad1-4668-aa3c-1af433ae0bf2",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "9a0dade0-9f88-48cb-b45f-007ee158b572",
  "toolUseResult": {
    "query": "discrete bottleneck viewpoint invariant camera robust robot manipulation world model 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CyV2mfJeNSKmo8EnMXtDek",
        "content": [
          {
            "title": "Learning View-invariant World Models for Visual Robotic Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=vJwjWyt4Ed"
          },
          {
            "title": "LEARNING VIEW-INVARIANT WORLD MODELS FOR ...",
            "url": "https://openreview.net/pdf?id=vJwjWyt4Ed"
          },
          {
            "title": "A Step Toward World Models: A Survey on Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.02097v1"
          },
          {
            "title": "[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.05868"
          },
          {
            "title": "View-Invariant Policy Learning via Zero-Shot Novel View Synthesis",
            "url": "https://arxiv.org/html/2409.03685v1"
          },
          {
            "title": "Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning",
            "url": "https://arxiv.org/html/2510.02268v1"
          },
          {
            "title": "Multi-View Masked World Models for Visual Robotic Manipulation",
            "url": "https://proceedings.mlr.press/v202/seo23a/seo23a.pdf"
          },
          {
            "title": "1 A Step Toward World Models: A Survey on Robotic Manipulation",
            "url": "https://www.techrxiv.org/users/935947/articles/1356038/master/file/data/A%20Step%20Toward%20World%20Models2/A%20Step%20Toward%20World%20Models2.pdf?inline=true"
          },
          {
            "title": "Mask World Model: Predicting What Matters for Robust Robot Policy Learning",
            "url": "https://arxiv.org/html/2604.19683"
          },
          {
            "title": "A Comprehensive Survey on World Models for Embodied AI",
            "url": "https://arxiv.org/html/2510.16732v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers related to your query about discrete bottleneck, viewpoint invariant, camera robust robot manipulation, and world models from 2026 on arXiv:\n\n## Key Findings:\n\n1. **ReViWo (Learning View-invariant World Models for Visual Robotic Manipulation)** - This paper proposes ReViWo, which leverages multi-view data to learn robust representations for control under viewpoint disturbance, utilizing an autoencoder framework that combines view-invariant representation (VIR) and view-dependent representation.\n\n2. **AnyCamVLA (Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models)** - The key idea is to virtually adjust test-time camera observations to match the training camera configuration in real-time using a feed-forward novel view synthesis model that handles both extrinsic and intrinsic parameters. This approach enhances viewpoint robustness in real-world robotic manipulation scenarios, including settings with varying camera extrinsics, intrinsics, and freely moving handheld cameras.\n\n3. **Camera Conditioning for View-Invariant Policy Learning** - One approach studies view-invariant imitation learning by explicitly conditioning policies on camera extrinsics, showing that conditioning on extrinsics significantly improves generalization across viewpoints for standard behavior cloning policies.\n\n4. **Mask World Model** - Recent work on predicting what matters for robust robot policy learning that addresses appearance-centric modeling challenges in world models for robotics.\n\nThese papers address the challenge of making robot manipulation policies robust to camera viewpoint changes, which is essential for real-world robotic deployment."
    ],
    "durationSeconds": 7.865479130000007
  },
  "sourceToolAssistantUUID": "5163e5e4-5ad1-4668-aa3c-1af433ae0bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-10T08:59:27.641Z_

```json
{
  "parentUuid": "9a0dade0-9f88-48cb-b45f-007ee158b572",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3783e772-34b3-447d-8c80-b247c309526b",
  "timestamp": "2026-05-10T08:59:27.641Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3783e772-34b3-447d-8c80-b247c309526b",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Assistant

_source line 35 · 2026-05-10T08:59:34.884Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The key facts are verified:
1. OA-WAM camera score on LIBERO-Plus: **80.5%** (confirmed from actual paper fetch)
2. Motus camera score on RoboTwin 2.0-Plus: **21.6%** (confirmed from actual paper fetch)
3. RoboTwin 2.0-Plus has no public GitHub evaluation code (confirmed)
4. Corresponding authors for 2603.22078: Zhanguang Zhang and Yingxue Zhang at Huawei (confirmed)

The proposal is factually correct on these key numbers.


Now I need to search for any recent work from May 2026 that specifically addresses VQ bottlenecks in WAMs or improves camera robustness, and I should double-check Being-H0.7's latent query configuration and whether it reports camera-specific LIBERO-Plus results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3783e772-34b3-447d-8c80-b247c309526b",
  "isSidechain": false,
  "requestId": "req_011CatcYEZUu6d1b8C4oTJMM",
  "type": "assistant",
  "uuid": "e0b64c6e-9eb3-4863-9c69-def956eef0e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RycGizPR6otGfmvk91LdYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 46234,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 535,
          "cache_read_input_tokens": 46234,
          "cache_creation_input_tokens": 1781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1781
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

_source line 36 · 2026-05-10T08:59:34.888Z_

OA-WAM camera score at 80.5% confirmed. Motus 21.6% confirmed. Now let me search for concurrent work on VQ bottlenecks in large WAMs and verify Being-H0.7 details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b64c6e-9eb3-4863-9c69-def956eef0e7",
  "isSidechain": false,
  "requestId": "req_011CatcYEZUu6d1b8C4oTJMM",
  "type": "assistant",
  "uuid": "9cc9881c-b5db-4bf6-a11e-a4cb4cb2dcb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RycGizPR6otGfmvk91LdYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 46234,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 535,
          "cache_read_input_tokens": 46234,
          "cache_creation_input_tokens": 1781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1781
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

_source line 37 · 2026-05-10T08:59:36.059Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015peyrBo4g1a38zaaCQPH8A`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00078v1",
  "prompt": "How many latent queries does Being-H0.7 use? Find the specific number K or N of latent reasoning queries in the prior branch. What are the LIBERO-Plus results? Does it report camera-specific scores or only aggregate scores? What is the aggregate LIBERO-Plus success rate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc9881c-b5db-4bf6-a11e-a4cb4cb2dcb7",
  "isSidechain": false,
  "requestId": "req_011CatcYEZUu6d1b8C4oTJMM",
  "type": "assistant",
  "uuid": "bee31a15-2f73-4bcd-a3c6-0b88f6cf9c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RycGizPR6otGfmvk91LdYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 46234,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 535,
          "cache_read_input_tokens": 46234,
          "cache_creation_input_tokens": 1781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1781
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

_source line 38 · 2026-05-10T08:59:36.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUi8NXV9dmKr1JXKoogVMJ`</summary>

```json
{
  "query": "VQ codebook visual bottleneck action policy camera viewpoint generalization WAM diffusion transformer 2026 arXiv May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bee31a15-2f73-4bcd-a3c6-0b88f6cf9c28",
  "isSidechain": false,
  "requestId": "req_011CatcYEZUu6d1b8C4oTJMM",
  "type": "assistant",
  "uuid": "ba7d37ee-5f40-48f1-9f66-008a5a2e4cd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RycGizPR6otGfmvk91LdYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 46234,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 535,
          "cache_read_input_tokens": 46234,
          "cache_creation_input_tokens": 1781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1781
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

_source line 39 · 2026-05-10T08:59:39.610Z_

<details><summary>↩ Tool result · `toolu_015peyrBo4g1a38zaaCQPH8A`</summary>

```text
# Being-H0.7: Latent Queries and LIBERO-Plus Results

## Number of Latent Queries

Being-H0.7 uses **K=16 latent reasoning queries** in the prior branch. The paper states: "we apply prior-posterior latent alignment to the last L=9 Transformer layers" with "K=16 latent reasoning queries."

## LIBERO-Plus Results

The paper reports **aggregate success rates only**, not camera-specific scores:

- **Zero-shot (trained on standard LIBERO):** 82.1% success rate
- **Fine-tuned (on LIBERO-plus dataset):** 84.8% success rate

The document notes these results demonstrate "resilience against shifted viewpoints, novel textures, and sensor noise" but does not break down performance by individual camera perspectives or environmental conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bee31a15-2f73-4bcd-a3c6-0b88f6cf9c28",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "126c95b4-b7ea-4c54-8e77-424a5a8ba405",
  "toolUseResult": {
    "bytes": 253466,
    "code": 200,
    "codeText": "OK",
    "result": "# Being-H0.7: Latent Queries and LIBERO-Plus Results\n\n## Number of Latent Queries\n\nBeing-H0.7 uses **K=16 latent reasoning queries** in the prior branch. The paper states: \"we apply prior-posterior latent alignment to the last L=9 Transformer layers\" with \"K=16 latent reasoning queries.\"\n\n## LIBERO-Plus Results\n\nThe paper reports **aggregate success rates only**, not camera-specific scores:\n\n- **Zero-shot (trained on standard LIBERO):** 82.1% success rate\n- **Fine-tuned (on LIBERO-plus dataset):** 84.8% success rate\n\nThe document notes these results demonstrate \"resilience against shifted viewpoints, novel textures, and sensor noise\" but does not break down performance by individual camera perspectives or environmental conditions.",
    "durationMs": 3547,
    "url": "https://arxiv.org/html/2605.00078v1"
  },
  "sourceToolAssistantUUID": "bee31a15-2f73-4bcd-a3c6-0b88f6cf9c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T08:59:45.715Z_

<details><summary>↩ Tool result · `toolu_01WUi8NXV9dmKr1JXKoogVMJ`</summary>

```text
Web search results for query: "VQ codebook visual bottleneck action policy camera viewpoint generalization WAM diffusion transformer 2026 arXiv May"

Links: [{"title":"Factorized Visual Tokenization and Generation","url":"https://arxiv.org/html/2411.16681v1"},{"title":"VideoGPT: Video Generation using VQ-VAE and Transformers","url":"https://arxiv.org/pdf/2104.10157"},{"title":"[2202.01334] Adaptive Discrete Communication Bottlenecks with Dynamic Vector Quantization","url":"https://ar5iv.labs.arxiv.org/html/2202.01334"},{"title":"Scalable Training for Vector-Quantized Networks with 100% Codebook Utilization","url":"https://arxiv.org/html/2509.10140"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers","url":"https://arxiv.org/html/2507.01016v1"},{"title":"Dual Codebook VQ: Enhanced Image Reconstruction with Reduced Codebook Size","url":"https://arxiv.org/html/2503.10832v1"},{"title":"VAEVQ: Enhancing Discrete Visual Tokenization through Variational Modeling","url":"https://arxiv.org/html/2511.06863"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Switchable Token-Specific Codebook Quantization For Face Image Compression","url":"https://arxiv.org/html/2510.22943v2"},{"title":"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.04678v1"}]

Based on the search results, I found several relevant papers on arXiv related to your query. Here are the key findings:

**Most Relevant Results:**

1. **MotuBrain: An Advanced World Action Model for Robot Control** - This paper explores World Action Models (WAMs) that unify visual dynamics and action prediction within a single, jointly optimized objective. A practical concern with world-action models is inference latency: jointly denoising a high-dimensional video latent and an action latent over many diffusion steps couples two of the slowest computations in modern generative modeling. This appears to be a very recent paper (about 1 week old).

2. **From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models** - This work uses a Transformer-based VQ-VAE to model visual transitions between observations, which directly relates to your query about VQ codebook and action policy.

3. **VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers** - This paper replaces the simple bin-based action tokenizer used in OpenVLA with a Residual VQ-VAE-based action tokenizer to improve the expressiveness and precision of action tokenization.

The search results show active research in VQ-based methods for action policies and vision-language-action models. However, I did not find a paper from May 2026 that specifically combines all the exact terms you mentioned (visual bottleneck, camera viewpoint generalization). The most recent papers in the results are from the last few weeks of 2025 and early 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba7d37ee-5f40-48f1-9f66-008a5a2e4cd4",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "7b3a6ab3-0150-47ac-9b2d-5ab7c3f52565",
  "toolUseResult": {
    "query": "VQ codebook visual bottleneck action policy camera viewpoint generalization WAM diffusion transformer 2026 arXiv May",
    "results": [
      {
        "tool_use_id": "srvtoolu_014svHJY9Q8zv31CwZaNiXhY",
        "content": [
          {
            "title": "Factorized Visual Tokenization and Generation",
            "url": "https://arxiv.org/html/2411.16681v1"
          },
          {
            "title": "VideoGPT: Video Generation using VQ-VAE and Transformers",
            "url": "https://arxiv.org/pdf/2104.10157"
          },
          {
            "title": "[2202.01334] Adaptive Discrete Communication Bottlenecks with Dynamic Vector Quantization",
            "url": "https://ar5iv.labs.arxiv.org/html/2202.01334"
          },
          {
            "title": "Scalable Training for Vector-Quantized Networks with 100% Codebook Utilization",
            "url": "https://arxiv.org/html/2509.10140"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers",
            "url": "https://arxiv.org/html/2507.01016v1"
          },
          {
            "title": "Dual Codebook VQ: Enhanced Image Reconstruction with Reduced Codebook Size",
            "url": "https://arxiv.org/html/2503.10832v1"
          },
          {
            "title": "VAEVQ: Enhancing Discrete Visual Tokenization through Variational Modeling",
            "url": "https://arxiv.org/html/2511.06863"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "Switchable Token-Specific Codebook Quantization For Face Image Compression",
            "url": "https://arxiv.org/html/2510.22943v2"
          },
          {
            "title": "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2605.04678v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on arXiv related to your query. Here are the key findings:\n\n**Most Relevant Results:**\n\n1. **MotuBrain: An Advanced World Action Model for Robot Control** - This paper explores World Action Models (WAMs) that unify visual dynamics and action prediction within a single, jointly optimized objective. A practical concern with world-action models is inference latency: jointly denoising a high-dimensional video latent and an action latent over many diffusion steps couples two of the slowest computations in modern generative modeling. This appears to be a very recent paper (about 1 week old).\n\n2. **From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models** - This work uses a Transformer-based VQ-VAE to model visual transitions between observations, which directly relates to your query about VQ codebook and action policy.\n\n3. **VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers** - This paper replaces the simple bin-based action tokenizer used in OpenVLA with a Residual VQ-VAE-based action tokenizer to improve the expressiveness and precision of action tokenization.\n\nThe search results show active research in VQ-based methods for action policies and vision-language-action models. However, I did not find a paper from May 2026 that specifically combines all the exact terms you mentioned (visual bottleneck, camera viewpoint generalization). The most recent papers in the results are from the last few weeks of 2025 and early 2026."
    ],
    "durationSeconds": 8.933388566999987
  },
  "sourceToolAssistantUUID": "ba7d37ee-5f40-48f1-9f66-008a5a2e4cd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T08:59:50.793Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Being-H0.7 K=16 confirmed - the proposal is accurate. Being-H0.7 only reports aggregate LIBERO-Plus scores without camera breakdown - confirmed.

The second search found a potentially relevant new paper: "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models" (arXiv:2605.04678v1). This might be relevant. Let me check this paper.

Also let me search for any very recent (May 2026) papers combining VQ with WAMs for viewpoint robustness. The key question is: has any work since Round 5 emerged that directly overlaps with the proposed VQ-Perceiver approach?


I need to pull up the "From Pixels to Tokens" paper to see if it's actually competitive with what we're proposing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3a6ab3-0150-47ac-9b2d-5ab7c3f52565",
  "isSidechain": false,
  "requestId": "req_011CatcZZtbsAxj9BdYEdy2G",
  "type": "assistant",
  "uuid": "30ececaa-5e56-45fa-bfb4-4f4247d5522a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019guQSZZw9gaRYQ3owrcTTt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 48015,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 48015,
          "cache_creation_input_tokens": 1643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1643
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

_source line 42 · 2026-05-10T08:59:51.912Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QnMaQRUSUNaJz5fjLH6Dcc`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.04678v1",
  "prompt": "What is this paper about? Does it apply VQ-VAE or discrete bottleneck to visual representations inside a WAM or VLA for camera viewpoint robustness? Does it modify cross-attention routing inside a large pretrained model? What are the key contributions and benchmarks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30ececaa-5e56-45fa-bfb4-4f4247d5522a",
  "isSidechain": false,
  "requestId": "req_011CatcZZtbsAxj9BdYEdy2G",
  "type": "assistant",
  "uuid": "0cb7ece3-5cac-4da3-8312-f973480b9e04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019guQSZZw9gaRYQ3owrcTTt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 48015,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 48015,
          "cache_creation_input_tokens": 1643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1643
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

_source line 43 · 2026-05-10T08:59:52.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0173NJ7GPay1WMJLkHbgPtV8`</summary>

```json
{
  "query": "intra-model VQ discretization visual tokens camera invariance Motus fine-tuning LoRA robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cb7ece3-5cac-4da3-8312-f973480b9e04",
  "isSidechain": false,
  "requestId": "req_011CatcZZtbsAxj9BdYEdy2G",
  "type": "assistant",
  "uuid": "f890f4a3-c3ff-4876-adc7-693d47143881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019guQSZZw9gaRYQ3owrcTTt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 48015,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 48015,
          "cache_creation_input_tokens": 1643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1643
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

_source line 44 · 2026-05-10T08:59:58.158Z_

<details><summary>↩ Tool result · `toolu_01QnMaQRUSUNaJz5fjLH6Dcc`</summary>

```text
# Summary of "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models"

## Core Focus

This paper systematically compares how to best integrate latent action representations into Vision-Language-Action (VLA) models for robotic control. It does **not** apply VQ-VAE to visual representations or modify cross-attention routing in pretrained models.

## Key Distinctions

Instead, the work studies two complementary approaches:

1. **Image-based latent actions**: Uses visual transitions as intermediate planning supervision to guide VLM decision-making
2. **Action-based latent actions**: Discretizes continuous actions into token space to unify supervision across heterogeneous datasets

The paper implements four integration strategies under a unified baseline (Qwen3-VL-2B), keeping the backbone and action head constant while varying only supervision signals.

## Main Contributions

- Systematic comparison of latent action supervision strategies within a controlled framework
- Identification of "formulation-task correspondence": image-based approaches excel at long-horizon reasoning; action-based approaches handle motorically complex tasks
- Discovery that directly supervising VLMs to predict discrete latent tokens yields strongest performance
- Evidence that latent action supervision reduces negative transfer during multi-task training

## Benchmarks & Results

**Simulation**: LIBERO (manipulation tasks) and RoboTwin 2.0 (bimanual manipulation)

**Real-world**: JAKA robotic arm with manipulation and pick-and-place tasks

Performance improvements range from +2.4% to +17.5% depending on task complexity and formulation choice.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cb7ece3-5cac-4da3-8312-f973480b9e04",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "33c25720-efb8-4eac-ba17-7ecd88d77412",
  "toolUseResult": {
    "bytes": 548141,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of \"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models\"\n\n## Core Focus\n\nThis paper systematically compares how to best integrate latent action representations into Vision-Language-Action (VLA) models for robotic control. It does **not** apply VQ-VAE to visual representations or modify cross-attention routing in pretrained models.\n\n## Key Distinctions\n\nInstead, the work studies two complementary approaches:\n\n1. **Image-based latent actions**: Uses visual transitions as intermediate planning supervision to guide VLM decision-making\n2. **Action-based latent actions**: Discretizes continuous actions into token space to unify supervision across heterogeneous datasets\n\nThe paper implements four integration strategies under a unified baseline (Qwen3-VL-2B), keeping the backbone and action head constant while varying only supervision signals.\n\n## Main Contributions\n\n- Systematic comparison of latent action supervision strategies within a controlled framework\n- Identification of \"formulation-task correspondence\": image-based approaches excel at long-horizon reasoning; action-based approaches handle motorically complex tasks\n- Discovery that directly supervising VLMs to predict discrete latent tokens yields strongest performance\n- Evidence that latent action supervision reduces negative transfer during multi-task training\n\n## Benchmarks & Results\n\n**Simulation**: LIBERO (manipulation tasks) and RoboTwin 2.0 (bimanual manipulation)\n\n**Real-world**: JAKA robotic arm with manipulation and pick-and-place tasks\n\nPerformance improvements range from +2.4% to +17.5% depending on task complexity and formulation choice.",
    "durationMs": 6242,
    "url": "https://arxiv.org/html/2605.04678v1"
  },
  "sourceToolAssistantUUID": "0cb7ece3-5cac-4da3-8312-f973480b9e04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T09:00:01.422Z_

<details><summary>↩ Tool result · `toolu_0173NJ7GPay1WMJLkHbgPtV8`</summary>

```text
Web search results for query: "intra-model VQ discretization visual tokens camera invariance Motus fine-tuning LoRA robot 2026"

Links: [{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers","url":"https://arxiv.org/html/2507.01016v1"},{"title":"[2512.11921] Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/abs/2512.11921"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Fine-Tuning Vision-Language-Action Models | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/vision-language-action-finetuning-robotics"},{"title":"(PDF) Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://www.researchgate.net/publication/398721162_Towards_Accessible_Physical_AI_LoRA-Based_Fine-Tuning_of_VLA_Models_for_Real-World_Robot_Control"}]

Based on the search results, I found relevant information about several of the topics you mentioned. Here's what I discovered:

## VQ Discretization and Visual Tokens in Robot Learning

Vector quantization is used to map continuous visual signals into a discrete token sequence in vision generation tasks. In robot learning, many works model action prediction as a generative problem and tokenize the robot action modality to capture the multi-modal distribution within skills and adapt it to autoregressive generative policies.

## Motus Project

Motus is listed as "A Unified Latent Action World Model" from 2025, indicating it's a recent development in embodied AI focused on action representation.

## LoRA Fine-Tuning for Robot Models

The VQ-VLA pipeline consists of training a general convolutional residual VQ-VAE and fine-tuning OpenVLA using the LoRA approach. LoRA updates only 1.4% of all parameters yet matches full fine-tune performance, facilitating usage on limited hardware.

## Camera Invariance and VLA Models

The search results don't contain specific information about camera invariance in the context you're asking about. However, the results do show that incoming RGB observations are divided into patches, each processed by visual encoders and concatenated as token vectors, which are then projected into the LLM embedding space using a two-layer MLP projector.

The search results provide information about VQ discretization, Motus, and LoRA fine-tuning for robotics, but don't contain detailed information specifically addressing "intra-model VQ discretization" or "camera invariance" in the specific context of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f890f4a3-c3ff-4876-adc7-693d47143881",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "65ac99a5-6d4d-4b59-8874-0beaf35efe14",
  "toolUseResult": {
    "query": "intra-model VQ discretization visual tokens camera invariance Motus fine-tuning LoRA robot 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KeuG6u5QF1E76xCwsxESmi",
        "content": [
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"
          },
          {
            "title": "Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control",
            "url": "https://arxiv.org/html/2512.11921v1"
          },
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers",
            "url": "https://arxiv.org/html/2507.01016v1"
          },
          {
            "title": "[2512.11921] Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control",
            "url": "https://arxiv.org/abs/2512.11921"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models | DigitalOcean",
            "url": "https://www.digitalocean.com/community/tutorials/vision-language-action-finetuning-robotics"
          },
          {
            "title": "(PDF) Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control",
            "url": "https://www.researchgate.net/publication/398721162_Towards_Accessible_Physical_AI_LoRA-Based_Fine-Tuning_of_VLA_Models_for_Real-World_Robot_Control"
          }
        ]
      },
      "Based on the search results, I found relevant information about several of the topics you mentioned. Here's what I discovered:\n\n## VQ Discretization and Visual Tokens in Robot Learning\n\nVector quantization is used to map continuous visual signals into a discrete token sequence in vision generation tasks. In robot learning, many works model action prediction as a generative problem and tokenize the robot action modality to capture the multi-modal distribution within skills and adapt it to autoregressive generative policies.\n\n## Motus Project\n\nMotus is listed as \"A Unified Latent Action World Model\" from 2025, indicating it's a recent development in embodied AI focused on action representation.\n\n## LoRA Fine-Tuning for Robot Models\n\nThe VQ-VLA pipeline consists of training a general convolutional residual VQ-VAE and fine-tuning OpenVLA using the LoRA approach. LoRA updates only 1.4% of all parameters yet matches full fine-tune performance, facilitating usage on limited hardware.\n\n## Camera Invariance and VLA Models\n\nThe search results don't contain specific information about camera invariance in the context you're asking about. However, the results do show that incoming RGB observations are divided into patches, each processed by visual encoders and concatenated as token vectors, which are then projected into the LLM embedding space using a two-layer MLP projector.\n\nThe search results provide information about VQ discretization, Motus, and LoRA fine-tuning for robotics, but don't contain detailed information specifically addressing \"intra-model VQ discretization\" or \"camera invariance\" in the specific context of your query."
    ],
    "durationSeconds": 8.76759017000001
  },
  "sourceToolAssistantUUID": "f890f4a3-c3ff-4876-adc7-693d47143881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "65ac99a5-6d4d-4b59-8874-0beaf35efe14",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Assistant

_source line 48 · 2026-05-10T09:01:44.472Z_

<details><summary>Logged reasoning block</summary>

```text
The "From Pixels to Tokens" paper is about latent action supervision, not visual token quantization for camera robustness. It doesn't compete directly with the proposed approach.

The VQ-invariance for camera robustness within a large pretrained WAM via intra-model routing appears to be genuinely novel. No direct competing work emerged in the search.

Now let me check on a few remaining concerns:

1. I should verify the ReViWo ICLR 2025 paper claims and whether the proposal's description of it is accurate
2. I should check whether Motus has public weights at motus-robotics/Motus on HuggingFace


3. I should also search for any concurrent work on Perceiver-based bottleneck for robustness in WAMs

Looking at the round 6 assessment, I've already addressed the critical benchmark priority flip and the Being-H0.7 score clarification from the previous feedback. The OA-WAM camera score checks out at 80.5% from the actual paper, so I need to see if there are any other unresolved issues that need attention.

Now I'm verifying the remaining technical details: Being-H0.7's K=16 latent queries, Motus's 21.6% camera performance on RoboTwin 2.0-Plus, and confirming there's no public evaluation code available for that benchmark. For the computation budget, my estimates show around 186 H100-hours for the auto-research component across 3 runs with overhead, and I have a clear contingency plan to drop to 2 runs if throughput hits 3 seconds per step at 20K steps. Let me recalculate more carefully — at 1s/step with 30K steps, that's about 8.3 hours of wall clock time across 4 GPUs, giving roughly 33 H100-hours per run, while 2s/step pushes it to 67 H100-hours per run. So the step reduction to 20K becomes critical even at 2s/step to keep the total under budget. The contingency plan holds up across different performance scenarios—even at 3s/step, dropping to 2 runs keeps us within budget at 169 H100-hours. Now I'm flagging the key issues to watch: the CoRL 2026 deadline is extremely tight with only 16-17 days until the abstract is due, and I need to verify that both the Motus weights and LIBERO-Plus benchmark are actually publicly available as claimed in the proposal.

Looking at the core technical novelty, I'm checking whether anyone else has already applied VQ discretization to visual tokens within a deployed large diffusion model for viewpoint invariance. I've found several related approaches—ReViWo handles viewpoint invariance with VQ but requires multi-view data at small scale, UVMC and XR-1 use dual-branch VQ-VAE for cross-embodiment work, VQ-VLA applies VQ to action tokens rather than visual ones, and there's GCQ for compression in world models—but none of these seem to directly combine the specific elements the proposal is claiming as novel.

The proposal's core contribution of applying intra-model VQ-based routing to visual tokens in a 7B diffusion model without requiring multi-view training data does appear to be genuinely novel. Both of the Round 5 concerns have been addressed: LIBERO-Plus is now the explicit primary benchmark with full infrastructure details, and the Being-H0.7 aggregate versus camera-specific results are clarified in the text. On novelty, this lands around 3.5-4 given the genuine contribution of intra-model cross-attention routing without multi-view requirements, properly positioned relative to ReViWo as prior work.

For feasibility, the public weights and code are confirmed available, the compute budget fits within the 200-hour constraint with fallback options, and the timeline of 4-5 days for auto-research plus 12+ days for writing is tight but achievable. The main technical risk centers on VQ-Perceiver training stability when integrated into the pretrained 7B model, though this is mitigated by a warm-up schedule. RoboTwin 2.0-Plus serves as a secondary benchmark to validate generalization.

The proposal is exceptionally clear with detailed contingencies, ablation plans, and compute breakdowns. On impact, it directly addresses the confirmed 65-point camera gap in Motus and competes against OpenAI's 80.5% continuous-attention baseline using a discrete VQ approach—if the method matches or exceeds that performance on the camera axis, it's a solid contribution. The codebook visualization adds interpretability value, though the limitation to a single target model and simulation-only evaluation somewhat constrain the broader applicability and practical significance.

All five rounds of feedback have been incorporated and the key claims check out: OA-WAM is indeed 80.5% on camera (not the 85.7% initially misread), and the Being-H0.7 baseline with K=16 queries is accurately cited. No new competing work has emerged that would undermine the proposal's positioning.

The remaining question is whether the technical implementation is actually feasible in 4-5 days—adding custom cross-attention layers to a 7B model, building out the VQ-VAE with EMA codebook updates, and wiring in the attention masking schedule alongside LoRA training is substantial work, though the proposal does leverage existing HuggingFace libraries and pre-trained checkpoints to reduce the lift.

For my Round 6 assessment: the critical and moderate issues from Round 5 have been addressed, the factual claims check out, and no new competing work has surfaced. The core unresolved tension is that the paper's central claim about VQ invariance is framed as an empirical hypothesis rather than a guaranteed property—the UMAP visualization serves as the test, but if the VQ approach underperforms OA-WAM's continuous method, the contribution weakens considerably, even if the fallback position of publishing it as an analysis remains viable.

Beyond that, there's the limitation of only evaluating on Motus despite the title's broader claim about MoT WAMs, and the strategic shift to LIBERO-Plus as the primary benchmark means the original 21.6% gap on RoboTwin 2.0-Plus isn't directly addressed—I'd need to see Motus's baseline on LIBERO-Plus first to assess whether the improvement is meaningful relative to OA-WAM's 80.5%. These are execution risks rather than fundamental flaws, though they do affect the strength of the final contribution.

After five rounds of revision, I'm settling on this as borderline pass territory. Let me double-check the compute estimates though, since those numbers are critical. The proposal claims roughly 186 H100-hours total for fine-tuning across three runs, which breaks down to about 50 H100-hours per run at best estimate—that's 12.5 wall-clock hours per run on 4 GPUs, which seems reasonable for the scope described.

Now I'm verifying the worst-case scenario at 2 seconds per step, which would push us to 236 H100-hours total and blow past the 200-hour ceiling. The fallback plan of reducing to 20K steps brings us down to around 169 H100-hours, which fits comfortably under budget.

So the contingency actually works. Looking at Round 6 overall, it addresses all the previous issues, the key claims check out independently, there's no conflicting work in the space, compute is within budget with clear fallbacks, and the benchmark priorities are properly ordered with LIBERO-Plus as primary. The Being-H0.7 clarification is explicitly included.

There are still some lingering concerns—the hypothesis is empirically grounded but the fallback of publishing an analysis paper if VQ doesn't outperform OA-WAM is a weaker story for CoRL, the single-model scope with just Motus limits how much I can claim about generalizability, and training VQ-Perceiver on top of a pretrained 7B model carries real stability risks. But these are execution risks and inherent limitations rather than things that need fixing before attempting the work. The proposal is transparent about them.

This feels like it warrants a pass, though I'm noting the marginal novelty—it's applying a known VQ-invariance principle to a new scale and architecture—and the aggressive 20-day timeline. Scoring it out: novelty at 3.5 for extending an existing principle with clear differentiation, feasibility at 3.5 since it's technically sound with realistic compute and contingencies but the timeline is very tight, clarity at 4.5 for being exceptionally well-specified, and impact at 3.5 because it addresses a real gap with a clear SOTA comparison but it's simulation-only and single-model. That averages to 3.75, which falls below the 4.0 pass threshold. But after six rounds of refinement, I'm wondering if this is actually a fail or if it should be revised—the remaining issues are really just timeline pressure and the fact that the fallback plan is weaker than the primary hypothesis.

Let me reconsider the scoring more carefully. The novelty of 3.5 feels right—it's a solid application of VQ for viewpoint invariance in diffusion WAMs with clear differentiation from ReViWo, and the intra-model routing without multi-view data is genuinely novel, even if the overall approach is incremental. Feasibility at 3.5 also holds up: the compute fits within budget with contingencies, the tools are available, but LoRA rank 64 on a 7B model with custom architecture modifications is non-trivial and VQ-Perceiver training stability is a real risk. Clarity at 4.5 is definitely justified—the proposal is exceptionally detailed with all contingencies spelled out and exact numbers. For impact, I need to finish evaluating whether 3.5 is the right call.

The proposal addresses a confirmed gap with a published baseline and compares directly against current SOTA at 80.5%, though it's limited to sim-only evaluation. CoRL 2026 is the right venue, and if VQ outperforms OA-WAM on the camera axis, that's meaningful. The UMAP codebook interpretability adds value. I'd lean toward 4.0 given the clear SOTA comparison and confirmed problem. That gives me an average of 3.875, still below 4.0 and in the revise zone.

But honestly, after six rounds of revision, all critical and moderate issues have been addressed, the factual claims are verified, and the remaining weaknesses are inherent to this type of work.

The fixable issues I could push for are clarifying the contingency if auto-research can't complete all three runs by May 15-16—the timeline needs explicit contingency protocols—and adding clarity on whether the Motus LIBERO-Plus baseline is expected to match or fall short of OA-WAM's 80.5%. The real gap is that we don't have a published Motus camera score on LIBERO-Plus to anchor expectations, only data from RoboTwin. The key risk is whether Motus already achieves strong performance on LIBERO-Plus camera tasks—if it does, there's no room for improvement. The proposal frames running the Motus LIBERO-Plus baseline as establishing a comparison point, suggesting they haven't obtained this score yet, which is concerning since the paper evaluates both benchmarks. Motus's LIBERO-Plus camera score could be anywhere from 20-40% (matching its weak RoboTwin 2.0-Plus performance) to 70-75%, which would significantly change how strong the contribution appears. Since the paper 2603.22078 likely contains this data already, I should look for it directly rather than relying on the RoboTwin baseline as my only evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65ac99a5-6d4d-4b59-8874-0beaf35efe14",
  "isSidechain": false,
  "requestId": "req_011Catcaj62ZS2TZpQjhumEF",
  "type": "assistant",
  "uuid": "b2c56322-5849-471f-83ab-9333d4402dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0191i3qKVBhcL2vdTWwoVUaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1895,
      "cache_read_input_tokens": 49658,
      "output_tokens": 5919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5919,
          "cache_read_input_tokens": 49658,
          "cache_creation_input_tokens": 1895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1895
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

_source line 49 · 2026-05-10T09:01:44.477Z_

Let me check whether arXiv:2603.22078 reports Motus's LIBERO-Plus camera score (this is crucial for assessing whether a baseline run is actually needed).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2c56322-5849-471f-83ab-9333d4402dab",
  "isSidechain": false,
  "requestId": "req_011Catcaj62ZS2TZpQjhumEF",
  "type": "assistant",
  "uuid": "0c040821-5a85-48e6-9481-2b55bdb99305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0191i3qKVBhcL2vdTWwoVUaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1895,
      "cache_read_input_tokens": 49658,
      "output_tokens": 5919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5919,
          "cache_read_input_tokens": 49658,
          "cache_creation_input_tokens": 1895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1895
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

_source line 50 · 2026-05-10T09:01:45.686Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LJJRGLNr74imjmeurLHSX3`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078v1",
  "prompt": "What is Motus's performance on LIBERO-Plus? Specifically, what is Motus's camera score on LIBERO-Plus? Is Motus evaluated on LIBERO-Plus at all in this paper? Also, what are the scores for other models (Cosmos-Policy, LingBot-VA) on LIBERO-Plus camera axis? List any table that shows LIBERO-Plus results broken down by perturbation axis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c040821-5a85-48e6-9481-2b55bdb99305",
  "isSidechain": false,
  "requestId": "req_011Catcaj62ZS2TZpQjhumEF",
  "type": "assistant",
  "uuid": "7fb70d67-f353-46f4-a90f-257099cfdc21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0191i3qKVBhcL2vdTWwoVUaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1895,
      "cache_read_input_tokens": 49658,
      "output_tokens": 5919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5919,
          "cache_read_input_tokens": 49658,
          "cache_creation_input_tokens": 1895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1895
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

_source line 51 · 2026-05-10T09:01:45.752Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DyeNHyseByFMsX4wStV8rD`</summary>

```json
{
  "query": "Motus LIBERO-Plus camera score robustness evaluation 2603.22078 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fb70d67-f353-46f4-a90f-257099cfdc21",
  "isSidechain": false,
  "requestId": "req_011Catcaj62ZS2TZpQjhumEF",
  "type": "assistant",
  "uuid": "089bb11c-ac95-469d-affe-4854fe6dac07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0191i3qKVBhcL2vdTWwoVUaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1895,
      "cache_read_input_tokens": 49658,
      "output_tokens": 5919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5919,
          "cache_read_input_tokens": 49658,
          "cache_creation_input_tokens": 1895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1895
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "089bb11c-ac95-469d-affe-4854fe6dac07",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Tool result

_source line 54 · 2026-05-10T09:01:50.091Z_

<details><summary>↩ Tool result · `toolu_01LJJRGLNr74imjmeurLHSX3`</summary>

```text
# MOTUS Performance on LIBERO-Plus

Based on the provided document, **MOTUS is not evaluated on LIBERO-Plus**. The paper only reports MOTUS results on RoboTwin 2.0-Plus.

## LIBERO-Plus Camera Scores

Table 4 presents the complete LIBERO-Plus evaluation broken down by perturbation type, including camera scores:

- **Cosmos-Policy**: 75.8% (camera)
- **LingBot-VA**: Not evaluated on LIBERO-Plus
- **π0.5**: 75.4% (camera)

The document notes that "The results of π0, π0-FAST, Openvla-OFT-m, UniVLA, RIPT-VLA are sourced from" the LIBERO-Plus paper, while other results come from official repositories.

## Key Finding

The paper states that WAMs "generally demonstrate strong robustness" but notes that "camera viewpoint and robot initial-state perturbations remain challenging for WAMs," with Cosmos-Policy achieving 75.8% accuracy on camera perturbations—comparable to π0.5's 75.4%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fb70d67-f353-46f4-a90f-257099cfdc21",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "ea1c1469-c50d-40a6-ab8e-aa249c0a0789",
  "toolUseResult": {
    "bytes": 379226,
    "code": 200,
    "codeText": "OK",
    "result": "# MOTUS Performance on LIBERO-Plus\n\nBased on the provided document, **MOTUS is not evaluated on LIBERO-Plus**. The paper only reports MOTUS results on RoboTwin 2.0-Plus.\n\n## LIBERO-Plus Camera Scores\n\nTable 4 presents the complete LIBERO-Plus evaluation broken down by perturbation type, including camera scores:\n\n- **Cosmos-Policy**: 75.8% (camera)\n- **LingBot-VA**: Not evaluated on LIBERO-Plus\n- **π0.5**: 75.4% (camera)\n\nThe document notes that \"The results of π0, π0-FAST, Openvla-OFT-m, UniVLA, RIPT-VLA are sourced from\" the LIBERO-Plus paper, while other results come from official repositories.\n\n## Key Finding\n\nThe paper states that WAMs \"generally demonstrate strong robustness\" but notes that \"camera viewpoint and robot initial-state perturbations remain challenging for WAMs,\" with Cosmos-Policy achieving 75.8% accuracy on camera perturbations—comparable to π0.5's 75.4%.",
    "durationMs": 4399,
    "url": "https://arxiv.org/html/2603.22078v1"
  },
  "sourceToolAssistantUUID": "7fb70d67-f353-46f4-a90f-257099cfdc21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T09:01:54.186Z_

<details><summary>↩ Tool result · `toolu_01DyeNHyseByFMsX4wStV8rD`</summary>

```text
Web search results for query: "Motus LIBERO-Plus camera score robustness evaluation 2603.22078 results"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

Based on the search results, I found information about the paper with ID 2603.22078. Here are the key findings:

## Paper Overview

The paper is titled "Do World Action Models Generalize Better than VLAs? A Robustness Study" (arXiv:2603.22078).

## MOTUS Results

MOTUS introduces a Mixture-of-Transformers (MoT) architecture that unifies video and action generation, and it is mentioned as a hybrid approach. MOTUS and similar approaches can achieve comparable or even superior robustness.

## Camera Score Robustness Evaluation

Regarding camera viewpoint robustness, camera viewpoint perturbations include modifications to camera distance, spherical position, and orientation. 

## Key Performance Results

World Action Models achieve strong robustness, with Cosmos-Policy achieving 82.2% on LIBERO-Plus, which is the benchmark used for evaluating camera score robustness among other visual perturbations.

The paper conducts a comparative study evaluating various models' performance under visual and language perturbations, with LIBERO-Plus being one of the primary benchmarks used for this robustness evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "089bb11c-ac95-469d-affe-4854fe6dac07",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "44a5c3d4-f70f-4aec-a6c9-3595d7373dec",
  "toolUseResult": {
    "query": "Motus LIBERO-Plus camera score robustness evaluation 2603.22078 results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GyDfLmkahChnmSW18YWPCm",
        "content": [
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
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2510.13626v2"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/abs/2603.22078"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          }
        ]
      },
      "Based on the search results, I found information about the paper with ID 2603.22078. Here are the key findings:\n\n## Paper Overview\n\nThe paper is titled \"Do World Action Models Generalize Better than VLAs? A Robustness Study\" (arXiv:2603.22078).\n\n## MOTUS Results\n\nMOTUS introduces a Mixture-of-Transformers (MoT) architecture that unifies video and action generation, and it is mentioned as a hybrid approach. MOTUS and similar approaches can achieve comparable or even superior robustness.\n\n## Camera Score Robustness Evaluation\n\nRegarding camera viewpoint robustness, camera viewpoint perturbations include modifications to camera distance, spherical position, and orientation. \n\n## Key Performance Results\n\nWorld Action Models achieve strong robustness, with Cosmos-Policy achieving 82.2% on LIBERO-Plus, which is the benchmark used for evaluating camera score robustness among other visual perturbations.\n\nThe paper conducts a comparative study evaluating various models' performance under visual and language perturbations, with LIBERO-Plus being one of the primary benchmarks used for this robustness evaluation."
    ],
    "durationSeconds": 8.429683132000006
  },
  "sourceToolAssistantUUID": "089bb11c-ac95-469d-affe-4854fe6dac07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-10T09:03:34.275Z_

<details><summary>Logged reasoning block</summary>

```text
Critical finding: **MOTUS IS NOT EVALUATED ON LIBERO-PLUS** in arXiv:2603.22078. 

This is significant because:
1. The proposal claims Motus's camera score on RoboTwin 2.0-Plus (21.6%) as the motivating evidence
2. The primary evaluation benchmark is LIBERO-Plus
3. Motus's LIBERO-Plus camera score is NOT available from published literature
4. The proposal says "Motus LIBERO-Plus baseline must be run once (~4h wall clock on 4 H100s)" - this is correct, and the proposal knows they need to run it


5. There's a real risk that Motus's LIBERO-Plus performance could be substantially different from its RoboTwin 2.0-Plus score since the benchmarks use different camera perturbation protocols, and without seeing the actual LIBERO-Plus results, I can't assess whether this baseline improvement is even meaningful. Looking at the performance spread across these models, OA-WAM's 80.5% on LIBERO-Plus camera is notably higher than Cosmos-Policy's 75.8%, and Motus's actual performance on this benchmark remains uncertain—it could range anywhere from 40% to 75% depending on how the perturbation difficulty compares to RoboTwin 2.0-Plus. If Motus lands in the lower range consistent with its 21.6% RoboTwin score, there's substantial room for improvement and the contribution becomes more significant, but if it's already near 75%, the gap narrows considerably and the impact weakens.

The two benchmarks use different camera perturbation strategies with different magnitudes—LIBERO-Plus specifies exact ranges for distance, spherical position, and orientation changes, while RoboTwin 2.0-Plus's parameters aren't publicly detailed—so there's genuine uncertainty about how Motus will perform without actually running the evaluation. The proposal correctly identifies this as a critical first step requiring about 4 hours on 4 H100s to establish the baseline, acknowledging it as a known risk that needs resolution.

The real concern isn't whether this is a flaw, but whether the motivation for the approach (the 65 percentage point camera gap) comes from RoboTwin 2.0-Plus rather than LIBERO-Plus itself. If Motus's LIBERO-Plus camera performance is already close to the OA-WAM baseline of 80.5%, the practical contribution on LIBERO-Plus camera would be limited—but this is an execution risk that's been appropriately flagged, not a fundamental problem with the proposal.

After six rounds of refinement, the critical issues have been resolved, factual claims are verified, and compute is within budget with contingencies accounted for.

Looking at the remaining weaknesses: the unknown Motus LIBERO-Plus baseline is an acknowledged execution risk, the VQ-invariance hypothesis is empirical with UMAP visualization as the test, training stability is mitigated by warm-up and monitoring, the 20-day timeline is tight but addressed through auto-research mode, and the novelty is incremental but properly scoped as an extension of VQ-invariance to large-scale diffusion WAM with novel intra-model routing that doesn't require multi-view data.

For scoring: novelty rates around 3.5 for extending a known principle to a new setting with meaningful architectural contribution, while feasibility appears strong overall. I'm realizing there's a timing problem I hadn't fully considered: OA-WAM just dropped three days ago, which means the SOTA baseline itself is moving fast. By the time this proposal reaches CoRL submission in late May, there could easily be newer work, or OA-WAM might even be a concurrent submission competing for the same venue. This creates a risk where the comparison target keeps shifting and the novelty claim becomes harder to establish.

There's also a practical concern with the aggregate scores—Being-H0.7 actually achieves 84.8% on the full LIBERO-Plus benchmark compared to OA-WAM's 83.9%, so if the VQ-Perceiver approach improves camera performance but degrades other modalities, the final aggregate could fall short of both baselines. And I'm noticing that Motus was explicitly excluded from LIBERO-Plus evaluation in the original benchmark paper, which affects how the proposal frames its contribution against that particular baseline. After multiple rounds of review, the proposal is fundamentally sound but sits just below the excellence threshold. The core issues aren't deal-breakers—they're mostly execution risks that are already acknowledged—though I could push for one more revision to strengthen the narrative. Specifically, I'd want them to explicitly state that Motus isn't evaluated on LIBERO-Plus in the existing literature, making that baseline run non-negotiable, and to clarify what happens if Motus already performs well on the camera task, since that would significantly narrow the motivation for the work.

But at Round 6 of 10, with the proposal substantially improved from where it started, I need to be honest about whether another revision would genuinely move the needle or just add cosmetic changes. The real constraints are structural: novelty would need broader experimental scope (more models, more benchmarks), feasibility risks like VQ training stability and the tight timeline can't be resolved on paper, and impact would require expanding the contribution itself. Clarity is already strong at 4.5, so there's no meaningful gain there. The question becomes whether there's actually a specific, actionable change that would push the average above 4.0, or if I'm just asking for revisions for their own sake.

What I should flag instead is a concrete gap: the proposal compares against Motus's LIBERO-Plus baseline without having that published number. If Motus already achieved something like 70%+ on LIBERO-Plus camera, the gap to our 80.5% becomes much less impressive than the 21.6% gap on RoboTwin 2.0-Plus suggests. Since Motus doesn't evaluate on LIBERO-Plus in their paper, this is a real unknown that could undermine the motivation—the initial baseline run needs to happen first to validate whether the problem is actually as significant as framed.

I'm leaning toward a "revise" verdict with a couple of minor issues framed as small fixes. The main one is that we need to explicitly acknowledge the Motus LIBERO-Plus baseline is unpublished and could substantially change how we interpret the improvement window. The second issue is that our central claim—beating OA-WAM's 80.5% on camera while staying competitive overall—deserves more explicit focus in the proposal.

Actually, looking back at the proposal, it does address noise robustness through VQ quantization's denoising properties, and it notes that lighting and background features should be preserved in the codebook since they're appearance-based rather than geometry-based. So the VQ bottleneck shouldn't hurt those axes even though all video tokens pass through it.

But there's still an unresolved tension: if we're compressing appearance information through 512 codes for 64 queries, we might lose some of the robustness that Motus currently has on lighting and background (84.6% and 84.4%). The proposal doesn't clearly establish whether the bottleneck preserves this appearance robustness or trades it away for camera robustness, which would weaken the contribution if it does.

The evaluation will reveal this naturally—if lighting and background scores drop significantly, that's a real finding, and the ablation comparing masked versus unmasked attention will help isolate whether it's the VQ effect or the routing mechanism causing any degradation.

After thinking through this extensively, my verdict is that the proposal is well-reasoned and honestly addresses the prior review concerns, with independent verification supporting the key claims. The two remaining risks are whether Motus actually appears in the LIBERO-Plus baseline (since the arXiv paper doesn't quote that score), and whether the VQ bottleneck compromises the appearance robustness Motus already achieves—both are manageable but worth monitoring in the results.

Given the novelty, feasibility, clarity, and impact scores averaging 3.75, I'm recommending a revise decision. The main actionable feedback is to explicitly state that Motus isn't evaluated on LIBERO-Plus in the original paper, making that baseline genuinely unknown, and to add a contingency plan: if Motus already hits 70% or higher on camera robustness, the contribution margin over OA-WAM's 80.5% becomes narrow, and the paper should emphasize the methodological contribution of matching continuous slot attention with discrete VQ routing instead.

I should also verify that the appearance robustness axes—lighting at 84.6% and background at 84.4%—aren't degraded by the bottleneck routing, since VQ codes should preserve appearance information consistently. After six rounds of refinement, these are genuinely minor fixes; the proposal is nearly there. The core issues boil down to clarifying the baseline status and ensuring the evaluation scope covers appearance alongside camera robustness. Looking at the full evaluation scope, I realize the proposal likely intends to run all seven perturbation dimensions even though it emphasizes the camera-axis comparison—but this should be made explicit rather than assumed. The key issue is that Motus doesn't appear in the original LIBERO-Plus paper's results, so establishing this baseline is actually foundational to the entire paper's claims, not just a preliminary step. I should flag this as needing clarification: the proposal should explicitly state whether the full multi-axis evaluation will be conducted and acknowledge why the Motus baseline is critical for validating the paper's core contributions. Looking at these issues more carefully, the first one about Motus's baseline is really just a clarity gap—the proposal mentions the run is needed but doesn't explain that it's because no published baseline exists yet. The second issue about reporting all LIBERO-Plus axes is more substantive; while focusing on camera makes sense for framing, reviewers would expect a full evaluation table across all axes, not just that one. Both are fixable in a revision, so I'm leaning toward a "revise" verdict. Now I'm second-guessing whether I'm being too strict on the Impact score—let me think through what the proposal actually demonstrates.

The proposal has confirmed baselines and a clear SOTA target to beat, it's tackling the hardest open problem in robustness, and the intra-model VQ routing would be genuinely novel. If the experiment succeeds, this becomes a solid contribution for CoRL. The interpretability analysis with UMAP adds another dimension. Given that it's simulation-only and single-model, I'd put Impact at 3.5 rather than pushing it higher. So my final scores are Novelty 3.5, Feasibility 3.5, and Clarity 4.5.

That averages to 3.75, which means I should recommend revision. There are two issues to address: first, Motus doesn't actually appear in the LIBERO-Plus evaluation table from that arXiv paper, so I need to acknowledge this gap and reframe the contribution—if Motus already hits 70% on camera (which seems plausible given Cosmos-Policy's 75.8%), then the story shifts from closing a massive gap to showing that discrete VQ routing can match or exceed OA-WAM's continuous approach. Second, the evaluation plan only commits to the camera axis but doesn't explicitly confirm whether all LIBERO-Plus robustness axes—lighting, background, noise—will be reported, which matters because VQ quantization bottlenecks all visual information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44a5c3d4-f70f-4aec-a6c9-3595d7373dec",
  "isSidechain": false,
  "requestId": "req_011Catcj3Bg9hk9h58KkZ5Zx",
  "type": "assistant",
  "uuid": "b66215a8-5b84-4817-82b7-4a39ae545fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PPrd2YEJRCoAERQiSvfV1r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7051,
      "cache_read_input_tokens": 51553,
      "output_tokens": 5549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5549,
          "cache_read_input_tokens": 51553,
          "cache_creation_input_tokens": 7051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7051
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

_source line 57 · 2026-05-10T09:03:34.277Z_

I now have enough data to issue a thorough verdict. Let me compile the findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b66215a8-5b84-4817-82b7-4a39ae545fc7",
  "isSidechain": false,
  "requestId": "req_011Catcj3Bg9hk9h58KkZ5Zx",
  "type": "assistant",
  "uuid": "84dbfcee-d6d7-41bf-b6c8-56d247fc18ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PPrd2YEJRCoAERQiSvfV1r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7051,
      "cache_read_input_tokens": 51553,
      "output_tokens": 5549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5549,
          "cache_read_input_tokens": 51553,
          "cache_creation_input_tokens": 7051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7051
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

_source line 58 · 2026-05-10T09:03:34.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RkLCEwQCjSDZSDQJ9L8T7B`</summary>

```json
{
  "query": "ReViWo ICLR 2025 view-invariant world model VQ robotic manipulation MetaWorld"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84dbfcee-d6d7-41bf-b6c8-56d247fc18ad",
  "isSidechain": false,
  "requestId": "req_011Catcj3Bg9hk9h58KkZ5Zx",
  "type": "assistant",
  "uuid": "e1af9f2c-2d92-4ef8-87be-9cd1ffdf9f44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PPrd2YEJRCoAERQiSvfV1r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7051,
      "cache_read_input_tokens": 51553,
      "output_tokens": 5549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5549,
          "cache_read_input_tokens": 51553,
          "cache_creation_input_tokens": 7051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7051
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e1af9f2c-2d92-4ef8-87be-9cd1ffdf9f44",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Tool result

_source line 61 · 2026-05-10T09:03:41.164Z_

<details><summary>↩ Tool result · `toolu_01RkLCEwQCjSDZSDQJ9L8T7B`</summary>

```text
Web search results for query: "ReViWo ICLR 2025 view-invariant world model VQ robotic manipulation MetaWorld"

Links: [{"title":"GitHub - lafmdp/ReViWo: Code for ICLR 25 paper: Learning View-invariant World Models for Visual Robotic Manipulation","url":"https://github.com/lafmdp/ReViWo"},{"title":"LEARNING VIEW-INVARIANT WORLD MODELS FOR ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8882d370cdafec9885b918a8cfac642e-Paper-Conference.pdf"},{"title":"Learning View-invariant World Models for Visual Robotic Manipulation","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e-Abstract-Conference.html"},{"title":"ICLR Poster Learning View-invariant World Models for Visual Robotic Manipulation","url":"https://iclr.cc/virtual/2025/poster/27921"},{"title":"Learning View-invariant World Models for Visual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vJwjWyt4Ed"},{"title":"GitHub - Trevor-emt/Reviwo","url":"https://github.com/Trevor-emt/Reviwo"},{"title":"World Models - ICLR 2025 Workshop","url":"https://sites.google.com/view/worldmodel-iclr2025/"},{"title":"About Jing-Cheng Pang (庞竟成): - Jing-Cheng Pang 庞竟成","url":"https://jingchengpang.github.io/"},{"title":"ICLR 2025 Workshop World Models | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2025%2FWorkshop%2FWorld_Models"},{"title":"ICLR 2025 Workshop World Models - Accepted Papers","url":"https://sites.google.com/view/worldmodel-iclr2025/accepted-papers?pli=1"}]

I found comprehensive information about ReViWo, an ICLR 2025 paper on view-invariant world models for robotic manipulation. Here's what I found:

## Overview

ReViWo is a paper presented at ICLR 2025 titled "Learning View-invariant World Models for Visual Robotic Manipulation" authored by Jing-Cheng Pang, Nan Tang, Kaiyuan Li, Yuting Tang, Xin-Qiang Cai, Zhen-Yu Zhang, Gang Niu, Sugiyama Masashi, and Yang Yu.

## Problem and Approach

The paper addresses performance degradation when camera viewpoints change during robotic manipulation, proposing ReViWo which leverages multi-view data to learn robust representations for control under viewpoint disturbance.

ReViWo utilizes an autoencoder framework to reconstruct target images by an architecture that combines view-invariant representation (VIR) and view-dependent representation.

## Training and Implementation

To train ReViWo, multi-view data is collected in simulators with known view labels while simultaneously training on Open X-Embodiment datasets without view labels, and the VIR is then used to train a world model on pre-collected manipulation data and a policy through interaction with the world model.

## Evaluation

The effectiveness of ReViWo is evaluated in various viewpoint disturbance scenarios using Meta-world and PandaGym environments, with experiments also conducted on real world ALOHA robot, demonstrating that ReViWo maintains robust performance under viewpoint disturbance while baseline methods suffer significant performance degradation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1af9f2c-2d92-4ef8-87be-9cd1ffdf9f44",
  "isSidechain": false,
  "promptId": "db3cdda4-9e7f-4a06-8152-6f7428d17e18",
  "type": "user",
  "uuid": "82bbb6f1-61e5-455c-8665-054d07e5f305",
  "toolUseResult": {
    "query": "ReViWo ICLR 2025 view-invariant world model VQ robotic manipulation MetaWorld",
    "results": [
      {
        "tool_use_id": "srvtoolu_017ocYUcM6wbC3Yhi5pSGqw5",
        "content": [
          {
            "title": "GitHub - lafmdp/ReViWo: Code for ICLR 25 paper: Learning View-invariant World Models for Visual Robotic Manipulation",
            "url": "https://github.com/lafmdp/ReViWo"
          },
          {
            "title": "LEARNING VIEW-INVARIANT WORLD MODELS FOR ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8882d370cdafec9885b918a8cfac642e-Paper-Conference.pdf"
          },
          {
            "title": "Learning View-invariant World Models for Visual Robotic Manipulation",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/8882d370cdafec9885b918a8cfac642e-Abstract-Conference.html"
          },
          {
            "title": "ICLR Poster Learning View-invariant World Models for Visual Robotic Manipulation",
            "url": "https://iclr.cc/virtual/2025/poster/27921"
          },
          {
            "title": "Learning View-invariant World Models for Visual Robotic Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=vJwjWyt4Ed"
          },
          {
            "title": "GitHub - Trevor-emt/Reviwo",
            "url": "https://github.com/Trevor-emt/Reviwo"
          },
          {
            "title": "World Models - ICLR 2025 Workshop",
            "url": "https://sites.google.com/view/worldmodel-iclr2025/"
          },
          {
            "title": "About Jing-Cheng Pang (庞竟成): - Jing-Cheng Pang 庞竟成",
            "url": "https://jingchengpang.github.io/"
          },
          {
            "title": "ICLR 2025 Workshop World Models | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2025%2FWorkshop%2FWorld_Models"
          },
          {
            "title": "ICLR 2025 Workshop World Models - Accepted Papers",
            "url": "https://sites.google.com/view/worldmodel-iclr2025/accepted-papers?pli=1"
          }
        ]
      },
      "I found comprehensive information about ReViWo, an ICLR 2025 paper on view-invariant world models for robotic manipulation. Here's what I found:\n\n## Overview\n\nReViWo is a paper presented at ICLR 2025 titled \"Learning View-invariant World Models for Visual Robotic Manipulation\" authored by Jing-Cheng Pang, Nan Tang, Kaiyuan Li, Yuting Tang, Xin-Qiang Cai, Zhen-Yu Zhang, Gang Niu, Sugiyama Masashi, and Yang Yu.\n\n## Problem and Approach\n\nThe paper addresses performance degradation when camera viewpoints change during robotic manipulation, proposing ReViWo which leverages multi-view data to learn robust representations for control under viewpoint disturbance.\n\nReViWo utilizes an autoencoder framework to reconstruct target images by an architecture that combines view-invariant representation (VIR) and view-dependent representation.\n\n## Training and Implementation\n\nTo train ReViWo, multi-view data is collected in simulators with known view labels while simultaneously training on Open X-Embodiment datasets without view labels, and the VIR is then used to train a world model on pre-collected manipulation data and a policy through interaction with the world model.\n\n## Evaluation\n\nThe effectiveness of ReViWo is evaluated in various viewpoint disturbance scenarios using Meta-world and PandaGym environments, with experiments also conducted on real world ALOHA robot, demonstrating that ReViWo maintains robust performance under viewpoint disturbance while baseline methods suffer significant performance degradation."
    ],
    "durationSeconds": 6.87273581600003
  },
  "sourceToolAssistantUUID": "e1af9f2c-2d92-4ef8-87be-9cd1ffdf9f44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 62 · 2026-05-10T09:03:41.168Z_

```json
{
  "parentUuid": "82bbb6f1-61e5-455c-8665-054d07e5f305",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a5cddf23-36de-405f-9dd8-816e5bcd4347",
  "timestamp": "2026-05-10T09:03:41.168Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 63 · 2026-05-10T09:04:03.341Z_

<details><summary>Logged reasoning block</summary>

```text
ReViWo ICLR 2025 is confirmed at the exact URL cited in the proposal. All key references check out.

Now let me compile my final verdict.

Key independent verification results:
1. **OA-WAM camera score**: CONFIRMED at 80.5% (verified by direct paper fetch of arXiv:2605.06481v1)
2. **Motus camera score on RoboTwin 2.0-Plus**: CONFIRMED at 21.6% (verified by direct paper fetch of arXiv:2603.22078v1)


3. **Motus wasn't evaluated on LIBERO-Plus** in the paper I checked—this is a new finding that wasn't explicitly mentioned before.
4. **Being-H0.7 K=16 latent queries**: CONFIRMED (direct paper fetch of arXiv:2605.00078v1)
5. **Being-H0.7 reports only aggregate LIBERO-Plus scores**: CONFIRMED (82.1% zero-shot, 84.8% fine-tuned, no camera breakdown)
6. **RoboTwin 2.0-Plus has no public evaluation code**: CONFIRMED (no public GitHub repository found)
7. **ReViWo ICLR 2025**: CONFIRMED at the exact URL cited
8. **No competing work** using VQ discretization for camera-invariant routing in large diffusion WAMs: CONFIRMED
9. **LIBERO-Plus is public**: CONFIRMED (github.com/sylvestf/LIBERO-plus exists)

Round 5 issues are resolved—I've addressed the RoboTwin evaluation code dependency by making LIBERO-Plus primary with full contingency, and clarified the Being-H0.7 aggregate versus camera-specific distinction.

For Round 6, there's a new moderate issue: since Motus wasn't evaluated on LIBERO-Plus in the published paper, I can't cite a baseline for it—the proposal acknowledges the baseline needs to be run, but this gap isn't explicitly flagged.

More critically, the LIBERO-Plus camera baseline for Motus could be substantially higher than RoboTwin 2.0-Plus's 21.6%, especially given that Cosmos-Policy reaches 75.8% on LIBERO-Plus camera despite lower RoboTwin scores. If Motus lands at 65-75%, the improvement window over OA-WAM's 80.5% becomes much tighter, shifting the narrative from "closing a massive gap" to "showing discrete routing matches continuous slot attention"—I need to prepare for this scenario.

There's also a minor gap: the evaluation plan emphasizes the camera axis but doesn't explicitly confirm all LIBERO-Plus perturbation axes will be reported, which matters since VQ quantization routes all visual information through the bottleneck and could show regressions on appearance axes like lighting or background.

Both are manageable presentation and evaluation scope issues. Looking at the overall assessment: novelty sits at 3.5 for extending ReViWo's VQ-invariance to a 7B diffusion MoT WAM with novel intra-model routing, feasibility at 3.5 given compute fits but with real risks around VQ training stability and the unknown baseline, clarity at 4.5 for being exceptionally detailed with explicit contingencies, and impact at 3.5 for addressing a confirmed gap with clear SOTA potential.

The average comes to 3.75, which falls below the 4.0 threshold, so this needs revision. The verdict is REVISE with two fixable issues, and since we're at round 6 of 10, there's room to address them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5cddf23-36de-405f-9dd8-816e5bcd4347",
  "isSidechain": false,
  "requestId": "req_011CatcrvYJGvgbxyhrrg132",
  "type": "assistant",
  "uuid": "09d5332c-6878-45e2-80af-6e22fa253675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CUyhySUJSd7KWQPVXXia6w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6584,
      "cache_read_input_tokens": 58604,
      "output_tokens": 2725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2725,
          "cache_read_input_tokens": 58604,
          "cache_creation_input_tokens": 6584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6584
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

_source line 64 · 2026-05-10T09:04:30.966Z_

I have sufficient evidence for my verdict. Key independent verification findings:

1. **OA-WAM 80.5% camera score**: CONFIRMED by direct paper fetch
2. **Motus 21.6% camera on RoboTwin 2.0-Plus**: CONFIRMED by direct paper fetch
3. **NEW CRITICAL**: Motus is **not evaluated on LIBERO-Plus** in arXiv:2603.22078 — only RoboTwin 2.0-Plus results exist for Motus in that paper
4. **Being-H0.7 K=16 queries, aggregate-only LIBERO-Plus**: CONFIRMED
5. **RoboTwin 2.0-Plus has no public evaluation code**: CONFIRMED
6. **ReViWo ICLR 2025 at cited URL**: CONFIRMED
7. **No competing concurrent work** on VQ intra-routing for camera-invariant WAMs found: CONFIRMED

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The proposal extends ReViWo's VQ-for-viewpoint-invariance principle (ICLR 2025) to a 7B diffusion MoT WAM via intra-model routing, which is a new and well-differentiated setting. However, the core mechanism (VQ codes suppress viewpoint-specific features) is borrowed wholesale from ReViWo; the architectural novelty is applying it intra-model with cross-attention routing rather than as offline preprocessing. This is incremental innovation, not a conceptual breakthrough."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Motus weights and LIBERO-Plus code are verified public. Compute fits within 200H with explicit contingencies. However, a critical unacknowledged risk exists: arXiv:2603.22078 does NOT evaluate Motus on LIBERO-Plus — the baseline is completely unknown and could be 65-75% (near OA-WAM's 80.5%), shrinking the improvement window dramatically. VQ-Perceiver training stability in a pretrained 7B system and the 20-day hard timeline are also real execution risks."
    },
    "clarity": {
      "score": 4,
      "rationale": "Exceptionally well-specified after six rounds: contingencies are explicit, compute breakdowns are unambiguous, benchmark priorities are clear. The proposal is among the clearest in the review history."
    },
    "impact": {
      "score": 3,
      "rationale": "Addresses a confirmed, quantified vulnerability (65pp camera gap from published data), has a well-defined SOTA comparison (OA-WAM 80.5%), and targets the hardest open problem for WAMs per arXiv:2603.22078. However, sim-only evaluation, single-model scope (Motus only), and the hypothesis-contingent core claim (UMAP must confirm viewpoint-invariant codebook structure) limit the expected impact. If Motus's LIBERO-Plus baseline is already ~70%+, the paper's contribution shrinks to a 10pp camera improvement over a continuous-attention alternative."
    }
  },
  "issues": [
    "CRITICAL NEW — UNKNOWN LIBERO-PLUS BASELINE: Independent verification of arXiv:2603.22078 confirms that Motus is NOT evaluated on LIBERO-Plus in that paper — only RoboTwin 2.0-Plus results exist for Motus. The proposal states the LIBERO-Plus baseline run is needed 'to establish comparison point' but does not acknowledge that the baseline is completely uncharted (0 published data points). This matters: Cosmos-Policy achieves 75.8% on LIBERO-Plus camera but lower scores on RoboTwin 2.0-Plus camera, suggesting the two benchmarks are not correlated. Motus's LIBERO-Plus camera score could plausibly be 60-75% — much higher than the RoboTwin 2.0-Plus 21.6% used as motivation. If the Motus LIBERO-Plus baseline lands at ≥70%, the gap to OA-WAM (80.5%) is only 10-11pp and the paper's framing must shift from 'closing a massive published gap' to 'demonstrating discrete routing can match continuous slot attention.' The proposal needs to add an explicit if-then for this scenario, with a repositioned contribution framing ready to deploy.",
    "MINOR NEW — EVALUATION SCOPE TOO NARROW: The evaluation plan describes comparing against OA-WAM's camera SOTA (80.5%) but never explicitly states that all LIBERO-Plus perturbation axes (lighting, background, noise, layout, robot state, language, camera) will be reported. Since VQ-Perceiver routes ALL visual token information through a K=512 bottleneck for action prediction, regressions on appearance axes where Motus currently performs well (lighting 84.6%, background 84.4% on RoboTwin 2.0-Plus) are possible and must be measured. CoRL reviewers will expect a full LIBERO-Plus evaluation table across all axes — camera-only reporting would look like cherry-picking."
  ],
  "feedback": "Two targeted fixes needed before this can pass: (1) LIBERO-PLUS BASELINE CONTINGENCY: Add one paragraph noting that Motus is absent from arXiv:2603.22078's LIBERO-Plus evaluation table (independently verified), making the 4h baseline run a prerequisite for validating the paper's core premise — not just calibration. Prepare two framing variants: (A) if Motus LIBERO-Plus camera ≤55%: 'closing a large gap from X to Y, significantly exceeding OA-WAM's continuous-attention 80.5%' — strong contribution; (B) if Motus LIBERO-Plus camera is 60-75%: 'demonstrating that hard VQ intra-routing achieves camera robustness comparable to/exceeding OA-WAM's continuous slot attention, with the added benefit of interpretable codebook structure' — method comparison framing. Both are publishable at CoRL but require different abstracts and intro paragraphs. The baseline run (day 1-2) gates which framing to use. (2) FULL EVAL TABLE: Explicitly add to the evaluation plan: 'Report full LIBERO-Plus evaluation table across all 7 perturbation axes for Motus-vanilla, VQ-Perceiver (main), and Perceiver-only ablation; primary claim is camera-axis improvement; secondary analysis documents appearance/noise axis preservation vs. regression from the VQ bottleneck.' Both fixes are ≤2 paragraphs and do not require architectural changes.",
  "reason": "Both Round 5 issues are fully addressed and key factual claims are verified correct, but a new critical finding — Motus is absent from LIBERO-Plus evaluation in the motivating paper, making the primary baseline entirely unknown — requires an explicit contingency framing before the proposal can pass."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d5332c-6878-45e2-80af-6e22fa253675",
  "isSidechain": false,
  "requestId": "req_011CatcrvYJGvgbxyhrrg132",
  "type": "assistant",
  "uuid": "7d751fa0-1e7a-466b-b617-069d2c9a703a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CUyhySUJSd7KWQPVXXia6w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6584,
      "cache_read_input_tokens": 58604,
      "output_tokens": 2725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2725,
          "cache_read_input_tokens": 58604,
          "cache_creation_input_tokens": 6584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6584
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

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7d751fa0-1e7a-466b-b617-069d2c9a703a",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "VQ-Perceiver bottleneck for camera-robust MoT WAMs",
  "sessionId": "b071fba2-bdbb-4548-baae-7b70d3426cd2"
}
```

---
