# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/eb569be8-fd5d-4af2-9acc-96cb78268509.jsonl`
- **Structured JSON:** [`a509df184deda6fa2df8.json`](../../sessions/a5/a509df184deda6fa2df8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:51:48.639Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:51:48.639Z",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World Action Models (WAMs) — joint world modeling and action prediction in a unified architecture, often built on video diffusion priors. In-scope: unified video+action prediction, MoT (Mixture-of-Transformers) architectures with text/video/action streams, WMs that double as policies via inverse dynamics on imagined futures, action-conditioned video diffusion as policy.\n\nRecent landscape (do not duplicate): UniVLA, DreamVLA, GigaBrain-0.5M, DiT4DiT, MotuBrain, video-diffusion-as-policy lines. WAMs are the hottest CoRL 2026 area — high competition but high reward.\n\nContribution type: METHOD ONLY. New unified architecture, new training scheme that fuses world prediction and action prediction, new inference algorithm extracting actions from imagined futures.\n\nSIM-ONLY MITIGATION: WAM papers at CoRL routinely use sim envs since the method depends on data scale, not real-robot deployment. Use LIBERO/ManiSkill as primary and frame contribution as architectural.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Most challenging budget — video models are heavy. Strategies: (a) fine-tune an open video WM (Cosmos releases, OpenSora, CogVideoX) with action conditioning, (b) distill a large WAM into a smaller one, (c) propose a method that requires only small additional training on top of an existing WAM, (d) propose an inference-time method that needs no training.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos.\n3. Eval: LIBERO, ManiSkill 2/3, RoboCasa for closed-loop control + video prediction quality (PSNR/SSIM/FVD on action-conditioned futures). Compare against UniVLA / DreamVLA / DiT4DiT lineage if open releases exist.\n\nLook for: efficient action-conditioning of video diffusion, latent WAMs that bypass pixel decoding, methods that share representations across world and action streams. Avoid: trivial action-token prepending without architectural insight.\n\nTag: direction=world_action_model, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning\",\n  \"core_problem\": \"Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO and 91.8% on RoboTwin at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\\n\\nThe VLA test-time compute literature (2025–2026) has addressed candidate selection for VLA architectures: RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model; MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place; Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but crucially, Cosmos Policy's authors report that a model trained only on demonstrations 'cannot correctly predict failure states' and that rollout fine-tuning is required to enable effective planning. None of these approaches exploit WAMs' unique property: joint video-action pretraining that regularizes action latents z_a to be consistent with physically plausible visual futures, forming a success-biased latent distribution.\\n\\nThe critical unanswered question — which VLA approaches cannot answer — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens, enabling lightweight OOD-based candidate scoring without any rollout data? (2) Is this latent OOD signal more informative than action-space distributional uncertainty (MG-Select's KL signal) for candidate selection? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection. The companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\\n\\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path.\",\n  \"opportunity\": \"UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection, exploiting the distributional structure of the WAM's joint video-action pretraining:\\n\\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8, significantly cheaper than video decoder passes. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\\n\\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) z_a regularized by joint video-action pretraining encodes physical plausibility co-varying with video futures, potentially creating a tighter success latent distribution with less success/failure overlap than VLA action tokens. LOC is WAM-specific in that this tighter latent structure is a direct consequence of joint video-action pretraining absent in VLAs. Differentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty). These are mechanistically distinct signals — one measures distributional membership relative to labeled success data, the other measures task-conditioning confidence.\\n\\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N candidate selection — it generates B actions, predicts future states and values for each, and executes the highest-value action. However, Cosmos Policy's planning mode (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states' (Cosmos Policy, 2026), and (b) queries the world model 3× and value function 5× per action (15 total forward passes per candidate) requiring parallel GPU infrastructure. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\\n\\nNote on PCS: The original approach of using video denoising error S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² as a zero-training quality signal is retained as a diagnostic comparison in the LOC diagnostic step (Step 1), not as a primary method. Cosmos Policy's explicit finding that demonstration-trained video priors do not reliably predict failure states, corroborated by the EVA 'executability gap' finding that visual coherence does not imply executable actions, provides strong prior evidence that raw denoising error will be a weak candidate selection signal. We include it as a secondary signal in Step 1 to report a clean negative result comparison against LOC.\\n\\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N (a_{i*} = argmax_i V(z_{a,i})) is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs or VLA action tokens (the latent geometry argument). Failure demonstrations collected via frozen UWM rollouts in simulation (~15–20 H100-hours) plus Gaussian-perturbed synthetic failures (<1 H100-hour).\\n\\n**Comparison of LOC vs. Value MLP is itself a central contribution**: LOC requires zero training and no rollout data, but relies on the WAM's latent success distribution being well-separated from failure trajectories at inference; Value MLP requires failure demonstration collection but directly learns the task-specific quality function. Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space OOD approach outperforms action-space distributional uncertainty (MG-Select-style KL).\\n\\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline. The 'approaching Cosmos Policy 67.1%' framing is deprioritized; the more defensible framing is 'demonstrating that WAM-specific latent OOD selection enables meaningful gains without any fine-tuning, at ≤40 H100-hours cost.'\",\n  \"landscape\": \"Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\\n\\nWorld2Act (arXiv 2603.10422, March 2026) — NEWLY ADDED. Achieves ~66% on RoboCasa (Cosmos Policy + World2Act) using only 50 real + 50 imagined demos, surpassing baseline Cosmos Policy. Method: aligns VLA action latents with world model video dynamics via a contrastive matching objective, reducing pixel-space dependence. Uses LLM-based skill decomposition to create RoboCasa-Skill and LIBERO-Skill datasets. Differentiation: World2Act requires contrastive post-training to align VLA action latents with video dynamics (modifies weights); our LOC method requires zero post-training and no weight updates — the alignment between action latents and video physics is inherited from UWM's joint pretraining. World2Act applies to VLAs requiring explicit alignment; our method exploits alignment that WAMs provide by construction.\\n\\nFast-WAM (arXiv 2603.16666, May 2026) is the critical framing reference. Test-time video generation adds only 0.5–1.9 percentage points: 97.6% LIBERO-avg and 91.8% RoboTwin without video at inference, at 190ms latency. Generates a single action trajectory with no candidate comparison. Complementary framing: Fast-WAM targets latency-critical deployment (single trajectory, fastest); our method targets success-critical tasks (B trajectories, select best via latent scoring at B × 5ms overhead).\\n\\nRoVer (arXiv 2510.10975, ICLR 2026) — Generates B candidate actions from frozen VLAs, trains a 0.2B Process Reward Model that scores candidates AND predicts refinement directions. Differentiation: (1) RoVer requires training a 0.2B PRM on process labels; LOC requires zero training and Value MLP requires only a 3-layer MLP; (2) RoVer applies to VLA action tokens lacking video-physics regularization; our methods target WAM action latents z_a jointly trained with video.\\n\\nVerifier-free / MG-Select (arXiv 2510.05681, ICLR 2026) — Training-free Best-of-N using KL-divergence from masked unconditional VLA distribution. 168% relative improvement on RoboCasa pick-and-place. Differentiation: MG-Select measures distributional uncertainty (how much task conditioning shifts the distribution from its unconditional prior) — an action-space confidence signal. LOC measures latent OOD membership (whether z_{a,i} is in-distribution relative to success demonstrations) — a latent-space quality signal. These are mechanistically different and testable: we include MG-Select-style KL applied to WAM as an explicit baseline in the ablation grid.\\n\\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — NEWLY ADDED AS SUPPORTING WORK. Frames failure detection as sequential OOD detection using conformal prediction on success-only demonstration data. Uses flow-based density estimation on distilled policy input/output signals. Demonstrates that OOD detection trained only on successes reliably detects failures at execution time. Relationship to LOC: LOC applies the same OOD detection principle to WAM action latents z_a for pre-execution candidate selection (ranking among B candidates before execution rather than monitoring execution). LOC differs in: (1) direct density estimation in action latent space vs. distilled scalar signal; (2) pre-execution selection vs. execution monitoring; (3) WAM-specific latent structure from joint video-action pretraining.\\n\\nEVA (arXiv 2603.17808, 2026) — NEWLY ADDED. Identifies 'executability gap' in video world models: visually coherent rollouts can violate kinematic constraints. Uses inverse dynamics model as training-time reward signal. Relevance: EVA's finding supports our decision to use action latent OOD scoring (LOC) rather than video denoising error (PCS) as the zero-training quality signal — visual coherence measured by denoising error does not imply executable actions. EVA's executability gap is complementary evidence that the latent action space (z_a) is a more direct quality substrate than the video prediction error.\\n\\nWAV: World-Value-Action Model (arXiv 2604.14732, April 2026) — Integrates a trajectory value module as a new architectural component trained from scratch; iterative latent-space inference concentrating probability mass on high-value trajectories. 99.6% LIBERO, 75.6% real-world dual-arm. Differentiation: WAV modifies the architecture and trains from scratch; our method leaves all WAM weights completely frozen and adds only a lightweight scoring module (LOC: no parameters; Value MLP: ~5M parameters). WAV is plug-in-incompatible with pretrained WAMs; our method is plug-in-compatible.\\n\\nCompose Your Policies! / GPC (arXiv 2510.01068) — Training-free convex composition of multiple frozen policy distributions. Different: operates at distribution level (combining score functions of multiple policies), not discrete candidate selection from a single frozen WAM; requires multiple compatible policies.\\n\\nGPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax. Our method uses the WAM's own action latent space as the evaluation substrate — no separate world model.\\n\\nWhen to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution. Orthogonal and combinable with our pre-execution selection.\",\n  \"approach\": \"Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\\n\\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing and drop all 'approaching Cosmos Policy 67.1%' language. Cost: ~2–3 H100-hours.\\n\\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator.\\n\\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\\n\\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Validate whether WAM action latent OOD scoring correlates with ground-truth task success, and compare against video denoising error (PCS) as a secondary signal.\\n\\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and PCS scores.\\n\\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} — expected to show lower AUC and ρ than LOC based on Cosmos Policy finding and EVA's executability gap evidence. Also compute MG-Select-style KL score as third comparison signal.\\n\\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC, confirming latent OOD density is more informative than video denoising error or action-space distributional uncertainty. If LOC AUC < 0.55 at all density estimator configurations, report as negative result; Value MLP becomes sole primary contribution. Decision: if LOC AUC ≥ 0.60, LOC is reported as primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison to PCS.\\n\\nThis diagnostic is a key scientific contribution: it empirically tests whether WAM joint pretraining creates a success latent distribution that is more quality-discriminative than video denoising error or distributional uncertainty, directly addressing open questions about WAM latent structure.\\n\\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity. Binary classification accuracy on held-out demo set as latent separability sanity check.\\n\\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Cost: ~3–5 H100-hours.\\n\\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\\n\\nPrimary results (two methods):\\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific]\\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific]\\n\\nComparisons (required): MG-Select-style KL scoring applied to WAM action-only inference (VLA method applied to WAM backbone, directly comparable to LOC on same benchmark); random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\\n\\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC, confirming negative result); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\\n\\n**Ablation Grid**: B ∈ {1, 2, 4, 8, 16} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. MG-Select-style KL (VLA method applied to WAM, key comparison) vs. PCS denoising error (expected negative result) vs. random selection (sanity check); noise temperature T_noise ∈ {1.0, 1.5, 2.0} (informed by diversity pilot); execution regime: (a) open-loop (B trajectories at episode start, execute selected) vs. (b) periodic replanning every K=5 action chunks.\\n\\n**Primary hypotheses**: (H1) LOC achieves Spearman ρ > 0.3 and AUC > 0.6 in the diagnostic, confirming WAM success latents form an OOD-detectable distribution; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic (latent OOD density > video denoising error ≈ action-space KL), with PCS showing AUC near 0.5 consistent with Cosmos Policy's finding; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform MG-Select-style KL applied to WAM, confirming latent quality-discrimination advantages of WAM joint pretraining over distributional uncertainty.\\n\\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, MG-Select-style KL applied to WAM.\\n\\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~140h H100\",\n      \"gpu_utilization\": \"HIGH idle (~35–55%): GPU waits while researcher implements LOC density estimator (KNN/GMM fitting), interprets LOC diagnostic results, debugs failure collection pipeline, and designs ablations. LOC inference overhead (5ms/candidate) reduces GPU demand vs. PCS (~50ms/candidate).\",\n      \"timeline\": \"2–3 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$350 (140h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~165h H100\",\n      \"gpu_utilization\": \"MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, LOC diagnostic, failure collection, demo encoding, density estimator fitting, and experiment submission; human reviews Step 0a baseline and LOC diagnostic results at daily check-ins to make go/no-go decisions\",\n      \"timeline\": \"3–4 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)\",\n      \"estimated_gpu_cost\": \"~$413 (165h × $2.50/h)\",\n      \"risk_note\": \"Step 0a (frozen UWM RoboCasa baseline) and LOC diagnostic are hard sequential dependencies before main ablation. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → LOC diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, parallel with LOC) → demo encoding + density fitting (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. LOC density estimation (KNN/GMM fitting) is computationally trivial and requires no GPU after demo encoding. DreamZero cross-WAM deferred to camera-ready.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~320h H100 (UWM backbone only; full B/T_noise ablation grid; RoboCasa + LIBERO-Long; multiple seeds; LOC diagnostic, PCS comparison, Value MLP comparisons)\",\n      \"gpu_utilization\": \"MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic (including PCS comparison), failure collection, demo encoding, density fitting, MLP training, and evaluation continuously. LOC inference is faster than PCS, reducing wall-clock time for ablation runs.\",\n      \"timeline\": \"7–10 days with 4–8 H100 GPUs simultaneously\",\n      \"team\": \"0 (only initial repo setup and credential configuration)\",\n      \"claude_api_cost\": \"$200–350 (~2,500–4,000 turns at Opus rates)\",\n      \"estimated_gpu_cost\": \"~$800 (320h × $2.50/h)\",\n      \"speed_bottleneck\": \"Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.\",\n      \"risk_note\": \"LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation — significantly lower implementation risk than PCS, which required implementing UWM mixed-mode forward passes not present in the public repository. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS comparison showing expected negative result) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready. LOC implementation is lower risk than PCS was (no custom mixed-mode forward pass needed).\",\n    \"ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation in WAM vs. VLA latent spaces), DreamZero cross-WAM evaluation, and potential real-world experiments.\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates\",\n    \"World2Act (arXiv 2603.10422, March 2026) — NEWLY ADDED: post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; aligns VLA action latents with world model video dynamics via contrastive matching objective; reports UWM achieves 60.8% on RoboCasa with 1,000 demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; our LOC exploits WAM alignment inherited from joint pretraining\",\n    \"Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666, May 2026) — CRITICAL FRAMING: 97.6% LIBERO, 91.8% RoboTwin at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead\",\n    \"FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — NEWLY ADDED SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; theoretical foundation for LOC's approach of using KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection\",\n    \"EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — NEWLY ADDED: identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; uses inverse dynamics model as training-time reward; supports LOC over PCS: visual denoising error (PCS) does not predict task success, while action latent OOD (LOC) is more directly quality-relevant\",\n    \"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization\",\n    \"Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution; MG-Select cannot exploit WAM latent geometry from joint pretraining\",\n    \"World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — SIGNIFICANT OVERLAPPING MOTIVATION: trajectory value module requiring training from scratch, new architectural component; 99.6% LIBERO, 75.6% real-world; our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs\",\n    \"Compose Your Policies! / GPC (arXiv 2510.01068) — PRIOR WORK: training-free distribution composition for multiple frozen policies; operates at distribution level, not discrete candidate selection from single WAM\",\n    \"Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — PRIOR WORK: frozen policy + separately trained world model + hard argmax; our method uses WAM's own action latent space, no separate world model\",\n    \"Unified World Models / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference; publicly available weights and code\",\n    \"Diffusion Policy (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting\",\n    \"When to Trust Imagination (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides action chunk sizes; orthogonal to our pre-execution selection; combinable\",\n    \"World Action Models as Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version\",\n    \"OA-WAM (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding)\",\n    \"CKT-WAM (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer)\",\n    \"GigaBrain-0.5M* (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training\",\n    \"H-WM (arXiv 2602.11291) — requires hierarchical architectural co-design\",\n    \"Latent Diffusion Planning (arXiv 2504.16925) — trains diffusion planner from scratch\"\n  ],\n  \"description\": \"Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods.\\n\\nThe key insight, refined from prior work: Cosmos Policy's own finding that demonstration-trained video priors 'cannot correctly predict failure states' — and EVA's demonstration of an 'executability gap' where video denoising quality does not predict executable actions — rules out video denoising error as a reliable zero-training quality signal. Instead, we exploit a different WAM-specific property: joint video-action pretraining creates action latents z_a that form a distribution regularized by physical plausibility, where the success demonstration distribution in latent space is distinguishable from failure trajectories. FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects failures; we apply this principle to WAM action latents for pre-execution candidate selection.\\n\\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8. Differentiated from MG-Select: LOC scores latent OOD membership relative to labeled success data; MG-Select scores action-space distributional uncertainty. WAM-specific: z_a regularized by joint video-action pretraining may create tighter, better-separated success latent distributions than VLA action tokens.\\n\\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection avoids multi-modal action-averaging artifact (Diffusion Policy). Central hypothesis: joint pretraining geometry makes z_a more linearly separable between success/failure regimes than VLA action tokens.\\n\\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target > 0.6), compared against: (a) video denoising error S_PCS (expected negative result based on Cosmos Policy and EVA evidence), (b) MG-Select-style KL applied to WAM. If S_LOC AUC < 0.55, LOC reported as negative result; Value MLP becomes sole primary contribution.\\n\\nMandatory baselines: (1) frozen UWM RoboCasa validation (Step 0a, expected 10–25%); (2) MG-Select-style KL as key comparison against LOC; (3) PCS in diagnostic as expected negative result.\\n\\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as upper references). Secondary: LIBERO-Long. CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.\",\n  \"project_name\": \"frozen_wam_mppi\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL OMISSION — Cosmos Policy (arXiv 2601.16163, ICLR 2026): This paper fine-tunes Cosmos-Predict2 (a pretrained video foundation model) to generate future state images and value estimations as latent frames, enabling test-time planning of action trajectories with higher success probability. It achieves 98.5% on LIBERO and 67.1% on RoboCasa — the exact benchmarks proposed here. The Generator does not cite or differentiate against Cosmos Policy. This is the closest prior work and must be addressed head-on.\", \"CRITICAL — Unvalidated 'early commitment' transfer to manipulation: ChEaP (arXiv 2603.30043) demonstrated early plan commitment only for 2D maze solving using Wan2.2-14B and HunyuanVideo-1.5. DreamZero-14B and UWM are trained on manipulation demonstrations with very different visual dynamics, object contact physics, and action-conditioned structure. There is no evidence that T_partial=5–10 steps in these models captures trajectory-discriminative information rather than unstructured noise.\", \"CRITICAL — Inference-time compute cost ignored: Running B=32–64 candidates × T_partial=5–10 diffusion steps through DreamZero-14B at each receding-horizon step requires 160–640 forward passes of a 14B model per action chunk. At 7Hz target control frequency, this is computationally infeasible. The proposal correctly analyzes training cost (≤10 H100-hours for value head) but completely ignores the inference bottleneck, which is the binding constraint for real deployment.\", \"SIGNIFICANT — Value MLP discriminability under high noise: Binary success/failure labels from LIBERO demos will train the MLP on clean completions, but the MLP receives noisy partial latents at T_partial=5–10 steps. The distributional gap between training inputs (full trajectories' latent encodings) and inference inputs (noisy partial denoising outputs) is not addressed. There is no prior work showing a simple MLP can usefully score heavily-noised intermediate latents of a manipulation-domain video diffusion model.\", \"SIGNIFICANT — Training data generation cost underestimated: The ≤5–8 H100-hour value head training estimate ignores the cost of generating the training dataset itself: every LIBERO-90 demo must be encoded by the frozen DreamZero-14B VAE and partially denoised for T_partial steps to produce (latent, label) pairs. With LIBERO-90 × hundreds of demonstrations each, this generation phase alone likely exceeds the stated budget.\", \"MODERATE — Joint video+action latent structure not addressed: DreamZero jointly denoises video and action tokens. Stopping at T_partial steps yields mixed video+action latent states. The proposed 3-layer MLP scores 'video latents' but the actual representation interleaves action information. The architectural mismatch between 'video-only MPPI' and DreamZero's joint denoising structure is not addressed.\", \"MODERATE — UWM compatibility uncertain: UWM (arXiv 2504.02792, RSS 2025) uses independent diffusion timesteps per modality. Treating the video latent of a partially-denoised UWM trajectory as a planning substrate requires careful handling of the asynchronous noise schedule — stopping video denoising at T_partial while action denoising may be at a different schedule step. The proposal does not address this.\"]\nFeedback: The core idea — converting any pretrained WAM into a receding-horizon planner without retraining via partial-denoising MPPI — is intellectually clean and addresses a real gap. But three revisions are needed before this is CoRL-ready:\n\n1. **Acknowledge and differentiate Cosmos Policy (ICLR 2026)**: This paper is your most direct prior work. Both you and Cosmos Policy use value functions over video diffusion WAMs for test-time planning on LIBERO/RoboCasa. Your differentiation must be sharp: 'Cosmos Policy requires full fine-tuning of a 12B+ model on robot demos (~200 H100-hours); our value MLP costs ≤10 H100-hours and leaves WAM weights frozen, making it applicable to any pretrained WAM as a plug-in.' Frame this clearly in abstract and related work.\n\n2. **Pilot experiment validating early commitment for manipulation**: Before submitting, run a quick diagnostic: take DreamZero or UWM, generate B=16 trajectories with T_partial ∈ {3,5,10,20,full} steps, and measure the correlation between early-step latent cosine similarity and final task success rate on LIBERO-Spatial (easy tasks). If early commitment holds, you'll have a strong motivating figure. If it doesn't (i.e., early latents don't predict outcome), the entire method premise collapses and you need a different approach — consider using the full denoising but fewer candidates (B=4–8), or replacing MPPI over partial latents with best-of-N reranking over fully denoised trajectories using the value MLP.\n\n3. **Address inference-time cost honestly**: Calculate and report wall-clock time per planning step with B=32, T_partial=5, DreamZero-14B. If it exceeds ~500ms/step, real-time control is impossible. Propose a solution: (a) use UWM (smaller model) instead of DreamZero-14B; (b) reduce B to 8–16 with correspondingly less compute; (c) restrict experiments to open-loop planning (generate full plan once, execute) rather than receding-horizon replanning. The paper is stronger if it clearly bounds the inference overhead and scopes claims accordingly.\n\nIf the early-commitment pilot experiment fails, consider pivoting to 'Best-of-N with Full Denoising': run B=4 full trajectories through the frozen WAM, score with value MLP trained on clean latents, select the highest-valued action chunk. This avoids the noisy-partial-latent discriminability issue, reduces inference cost, and preserves the zero-WAM-retraining property.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Action-averaging artifact unaddressed: Computing weighted average sum_i w_i * a_i over multi-modal manipulation trajectories is known to produce invalid/infeasible actions. For example, if half the trajectories grasp an object from the left and half from the right, the weighted average drives the gripper straight into the object. This is a well-documented failure mode of averaging over multi-modal distributions (see Diffusion Policy paper and 2025 diffusion survey). The proposal presents soft importance weighting as a strength over hard argmax, but for manipulation this may be strictly worse than GPC-RANK's hard argmax selection. No ablation validates that soft averaging outperforms hard selection in practice.\", \"CRITICAL — No failure demonstrations in LIBERO for value MLP training: LIBERO-90 consists entirely of successful human teleoperation demonstrations. The proposal says 'label each with task success/failure from demo metadata' but there are no failure trajectories in the standard LIBERO-90 dataset — all demos are successful by construction. Training a binary success/failure MLP requires negative examples, which must be generated via online simulation rollouts of the policy. This adds substantial cost (20–40 H100-hours of simulation rollouts, policy execution, and data collection) not accounted for in the ≤18 H100-hour budget.\", \"CRITICAL — Fast-WAM (arXiv 2603.16666) challenges the core premise: Fast-WAM demonstrates that 'the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time,' achieving competitive performance with zero test-time video generation and 4× faster inference. If test-time video futures add minimal value, generating B=4–8 full denoised trajectories per planning step is computationally wasteful with limited benefit. Reviewers will ask: why not just use Fast-WAM-style action prediction (no video generation) instead of full-trajectory MPPI?\", \"SIGNIFICANT — Unlisted concurrent work: 'When to Trust Imagination: Adaptive Action Execution for World Action Models' (arXiv 2605.06222, May 2026) addresses the same problem — when and how to use WAM imagined futures for action execution — and must be cited and differentiated. Additionally, OA-WAM (arXiv 2605.06481) and CKT-WAM (arXiv 2605.06247) are May 2026 papers in the same WAM inference-efficiency space.\", \"SIGNIFICANT — Discriminability assumption not validated: B=4–8 trajectories sampled from the same frozen WAM with the same task conditioning and different Gaussian seeds may have high cosine similarity in the WAM's latent space, leaving the value MLP with insufficient discriminative signal. The entire method's gain depends on there being meaningful variance in V(z_i) across the B samples — this is empirically unvalidated and constitutes a failure mode that would produce near-uniform MPPI weights (degenerate to random selection). No pilot experiment or cited evidence supports that UWM trajectories have sufficient diversity for this purpose.\", \"MODERATE — LIBERO is essentially saturated at the top end: Cosmos Policy achieves 98.5% on LIBERO; multiple 2025 papers report >95%. LIBERO-Long is a better choice (as the proposal selects), but reviewers will note the benchmark is limited. The comparison against Cosmos Policy published results ('cited for context on fine-tuned WAM upper bound') does not constitute a meaningful experimental comparison — CoRL reviewers will expect at least one shared evaluation setup.\", \"MODERATE — Soft vs. hard averaging contribution is marginal: The headline differentiator from GPC-RANK is replacing hard argmax with soft importance-weighted averaging — a 2-line change. This is not a novel architectural contribution. The stronger claim (plug-in to any frozen WAM, no separate world model) is more defensible as a contribution but needs to be empirically demonstrated across at least two WAM backbones (UWM + DreamZero-14B) to support the 'plug-in' generalization claim, which is proposed as secondary and may not be completed within 20 days.\"]\nFeedback: The Round 1 revisions were correctly executed — the pivot from partial denoising to full denoising, addition of Cosmos Policy as critical prior work, and inference cost scoping are all sound. However, three new issues block submission:\n\n1. **Fix the action-averaging artifact or reframe the contribution**: Soft weighted averaging of manipulation trajectories is known to produce infeasible blended actions in multi-modal settings. Either (a) pivot the primary result to hard argmax selection (making MPPI weighting the ablation rather than the headline), or (b) show empirically on LIBERO-Long that MPPI soft weighting outperforms hard argmax. Option (a) is safer given the 20-day timeline and actually aligns better with GPC-RANK comparison story. Keep soft weighting as an ablation, not the main claim.\n\n2. **Generate failure demonstrations before training the value MLP**: LIBERO-90 has no failure trajectories. You must run the frozen UWM policy on LIBERO tasks in simulation to collect rollout failures as negatives. Budget ~20 H100-hours for this. Alternatively, add synthetic failures by perturbing successful demo actions with Gaussian noise and flagging truncated episodes as failures. Without negatives, the classifier cannot train. This should be described explicitly as Step 0 of the approach.\n\n3. **Explicitly address Fast-WAM (arXiv 2603.16666)**: Add a paragraph in related work explaining why generating full video trajectories for scoring is still valuable despite Fast-WAM's finding. The argument: Fast-WAM improves efficiency by removing video generation from inference, but its single-trajectory output cannot compare candidate futures. Frozen-WAM MPPI accepts the compute overhead of B full trajectories to enable candidate selection — a different tradeoff point optimizing for task success rate rather than latency. Frame this as a complementary approach: Fast-WAM for latency-critical deployment, Frozen-WAM MPPI for success-critical tasks where longer planning time is acceptable.\n\n4. **Add a diversity pilot experiment**: Before the full ablation, show a diagnostic figure: sample B=16 trajectories from frozen UWM on 3 LIBERO-Long tasks, measure latent diversity (pairwise cosine distance of z_i) and correlation of V(z_i) with ground-truth success (if rollouts are available). If diversity is low (all z_i are within 0.1 cosine distance), increase noise temperature or add perturbations to the conditioning. This directly validates the premise of the entire method.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"SIGNIFICANT — Three important related papers are completely absent from the landscape: (1) RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975): generates B candidate actions from a frozen VLA, scores with a trained Process Reward Model (PRM), and selects via argmax — evaluated on CALVIN + real robot (GR-1, Dita, MoDE backbones). Different policy class (VLA not WAM) and benchmark (CALVIN not LIBERO/RoboCasa), but the paradigm is essentially identical. Must be cited and differentiated. (2) Verifier-free Test-Time Sampling for Vision Language Action Models (arXiv 2510.05681, ICLR 2026): Best-of-N for frozen VLAs using KL-divergence from a masked reference distribution as a confidence signal — no additional training required; achieves 168% relative improvement on pick-and-place. Differentiator: no trained value model; applicable to VLAs not WAMs. Must be cited. (3) Compose Your Policies! (arXiv 2510.01068): test-time policy composition for diffusion/flow-based robot policies without retraining, using score composition. Must be cited.\", \"CRITICAL — Frozen UWM baseline on RoboCasa is an unvalidated assumption that may be dramatically wrong. The UWM paper (RSS 2025, arXiv 2504.02792) evaluates primarily on LIBERO and OXE-distribution tasks; no published RoboCasa-without-fine-tuning results exist. Cosmos Policy achieves 67.1% on RoboCasa only after 1,536 H100-hours of domain-specific fine-tuning. A frozen UWM — not fine-tuned on RoboCasa's kitchen tasks — achieving 40-55% baseline success seems optimistic; 15-30% is more plausible. If the actual baseline is 15-30%, the ≥60% target requires +30-45pp from a 3-layer MLP scoring action latents, which is almost certainly too large. The Generator should: (a) run a quick 50-episode RoboCasa baseline with frozen UWM before committing to ≥60% target; (b) recalibrate the target to 'improve baseline by ≥10pp' rather than 'approach Cosmos Policy 67.1%' if baseline is lower than expected.\", \"SIGNIFICANT — The World-Value-Action (WAV) model (arXiv 2604.14732, April 2026) proposes a trajectory value function that 'evaluates long-horizon utility' and generates actions via 'inference in latent space where the model progressively concentrates probability mass on high-value trajectories.' This is substantially overlapping in motivation (value scoring over latent trajectory representations) though architecturally different (implicit latent inference vs. discrete Best-of-N selection). Should be cited and explicitly differentiated: WAV modifies the VLA architecture; this proposal keeps all weights frozen.\", \"MODERATE — Novelty argument is insufficiently grounded for CoRL acceptance. The technical differentiation from RoVer reduces to: (a) WAM action latents vs. VLA action space, (b) UWM action-only mode vs. standard policy, (c) LIBERO/RoboCasa vs. CALVIN. These are valid engineering differences but unlikely to meet CoRL's bar for conceptual novelty. The proposal needs a sharper 'why WAM action latents?' argument — specifically, that the WAM's joint video-action pretraining instills physical grounding into the action latent z_a that pure action-space policies lack, making the latent richer for value estimation. This would differentiate from RoVer on principled grounds, not just implementation.\", \"MODERATE — The DreamZero-14B cross-WAM evaluation is described as secondary but is essential for the 'plug-in across WAM architectures' claim. DreamZero-14B requires full video+action denoising (no native action-only mode), making B-trajectory sampling substantially more expensive than for UWM. If this experiment cannot be completed within the 20-day window (likely, given 50 H100-hours estimate), the 'plug-in' contribution collapses to a single-architecture result, significantly weakening the generalization claim. The Generator should either (a) commit to completing DreamZero validation within the timeline or (b) reframe the contribution as UWM-specific and drop the plug-in generalization claim.\", \"MODERATE — The feasibility of training a discriminative value MLP from action latents depends on a premise not yet verified: that frozen UWM action latents from successful and failed demonstrations are separable in the latent space. If UWM's action latent z_a primarily encodes task semantics (what to do) rather than execution quality (how well to do it), success/failure labels may be uncorrelated with latent structure and the MLP will learn a degenerate classifier. The diversity pilot (Spearman ρ > 0.3 target) partially addresses this, but binary classification accuracy on held-out demos should also be reported as a sanity check before the main ablation.\"]\nFeedback: The Round 3 revision has correctly addressed all three Round 2 critical issues: (1) hard argmax is now the primary result with solid justification, (2) Step 0 failure collection is explicitly specified at 15-20 H100-hours, and (3) Fast-WAM is now integrated as a complementary framing. The diversity pilot is a strong addition. However, three concrete fixes are needed before CoRL submission:\n\n**1. Add and differentiate three missing related papers (1-2 days).** You must cite RoVer (arXiv 2510.10975), Verifier-free Test-Time Sampling (ICLR 2026, arXiv 2510.05681), and Compose Your Policies! (arXiv 2510.01068) in your related work section. The differentiation argument for RoVer specifically should be: 'RoVer applies to VLA architectures in token-action space using an explicitly trained PRM; our method targets WAMs whose joint video-action pretraining produces physically grounded action latents z_a that are richer substrates for value estimation than action tokens from VLAs — we exploit this WAM-specific property to eliminate the need for a separate process reward model training stage.' Also cite WAV (arXiv 2604.14732) as addressing value-guided action selection within VLAs via implicit latent inference, and differentiate: 'WAV modifies the architecture; Frozen-WAM BoN leaves all weights frozen.'\n\n**2. Validate the frozen UWM baseline on RoboCasa before committing to ≥60% target (3-5 days, highest priority).** Run 50 episodes of B=1 frozen UWM action-only inference on a representative subset of RoboCasa tasks. If the baseline is 40-55%, the ≥60% target is appropriate. If it is 15-35% (which is equally plausible given no published UWM/RoboCasa results), you must: (a) adjust the target to 'improve baseline success rate by ≥10pp absolute,' and (b) reframe the comparison away from 'approaching fine-tuned Cosmos Policy (67.1%)' toward 'meaningful improvement over frozen WAM without any fine-tuning, at ≤40 H100-hours training.' The latter is still a publishable result; the former collapses if the baseline is too low.\n\n**3. Sharpen the theoretical motivation for WAM latents over action space (0.5 days).** Add one paragraph explaining why z_a from a jointly-trained video-action WAM contains more quality-discriminative information than the output action tokens of a VLA. The key insight: UWM's video diffusion process regularizes z_a to be consistent with physically plausible visual futures, instilling motion-physics grounding that raw VLA action tokens lack. This is why a 3-layer MLP over z_a can succeed where the same MLP over VLA output tokens would fail — and this is your fundamental novelty claim that differentiates Frozen-WAM BoN from RoVer at the conceptual level.\n\nMinimum viable CoRL submission: frozen UWM + RoboCasa Best-of-N (primary) + LIBERO-Long (secondary) + diversity pilot figure + B/hard-argmax ablation. Drop DreamZero cross-WAM to camera-ready — it adds a 50 H100-hour sequential dependency that cannot be completed before the diversity pilot results inform whether the premise holds.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE — Cosmos Policy planning mode under-differentiated: Cosmos Policy already implements Best-of-N video-based candidate selection (generates B actions, predicts future states + values, selects highest-value). The Generator cites Cosmos Policy's training cost but does not explicitly acknowledge its planning mode does conceptually the same candidate scoring loop. The differentiation must be stated precisely in the methods section: 'Cosmos Policy planning mode also ranks candidates via video futures, but requires fine-tuning a value function on rollout data; PCS is zero-training and requires only the frozen WAM's existing video prior — at the cost of relying on a less reliable signal not explicitly trained for failure prediction.'\", \"SIGNIFICANT — PCS premise directly challenged by Cosmos Policy's own finding: Cosmos Policy's paper states the base model trained only on demonstrations 'cannot correctly predict failure states' and requires on-policy rollout fine-tuning to enable effective planning. This directly challenges PCS's claim that a frozen WAM's video prior (trained primarily on demonstrations) can serve as a reliable quality signal. The Generator must address this in the paper — either (a) argue why denoising error is a different and more robust signal than explicit state prediction, or (b) anticipate in the intro that PCS may fail and explicitly credit the diagnostic as a scientific contribution in either outcome. The current framing treats PCS failure as a fallback but does not acknowledge the strong prior evidence suggesting it may fail.\", \"MODERATE — UWM's 60.8% RoboCasa result requires 1000-demo fine-tuning, not frozen inference: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1000 real demonstrations. Since UWM was trained only on DROID data (no RoboCasa), this is a fine-tuned result. The frozen UWM baseline (no RoboCasa demos) is likely 10–25%, not 40–55%. The Generator already handles this with adaptive framing in Step 0a, but the baseline expectation should be calibrated to 'likely 10–25%' to avoid surprises. The framing of 'approaching Cosmos Policy 67.1%' should be deprioritized in favor of the more defensible '≥10pp improvement over frozen baseline.'\", \"MODERATE — World2Act (arXiv 2603.10422, March 2026) is missing from the landscape: World2Act achieves 66.3% on RoboCasa (Cosmos Policy + World2Act) using only 50 real + 50 imagined demos, surpassing baseline Cosmos Policy and representing the current published SOTA approach. As a concurrent March 2026 paper using world model latents to improve policy performance, it should be cited and differentiated: 'World2Act aligns VLA action latents with world model video dynamics via contrastive post-training; our method requires no post-training of any kind for PCS, and no world model separate from the frozen WAM for Value MLP.'\", \"MINOR — Cosmos Policy planning mode inference cost not addressed: Cosmos Policy's planning mode 'ensembles predictions by querying the world model three times per action and the value function five times per future state (15 total value predictions per action)' using N GPUs in parallel. The Generator should note that Cosmos Policy's planning mode at inference is also expensive (requires fine-tuned planning model, multiple forward passes, parallel GPUs) vs. PCS's single video decoder pass per candidate — the inference efficiency comparison is part of the full cost story.\"]\nFeedback: The Round 4 revision has correctly addressed all Round 3 critical issues. The paper is structurally sound with good fallback plans. Three concrete fixes are needed for CoRL submission:\n\n**1. Address the Cosmos Policy planning-mode differentiation gap (0.5 day).** In the methods section and related work, add an explicit paragraph: 'Cosmos Policy (ICLR 2026) implements Best-of-N candidate selection via video-future scoring in its planning mode — it generates B candidate actions, predicts future states and values for each via a fine-tuned planning model, and executes the highest-value action. Our work targets the same planning loop but requires zero weight updates: PCS uses the frozen WAM's existing video prior as quality signal, while Cosmos Policy requires fine-tuning on rollout data to learn an explicit failure-predictive value function.' This is your sharpest differentiation claim.\n\n**2. Confront the Cosmos Policy anti-evidence for PCS (0.5 day).** Cosmos Policy's paper explicitly found that a model trained only on demonstrations cannot predict failure states — rollout fine-tuning is required. Add a paragraph acknowledging this: 'Cosmos Policy's authors observe that demonstration-trained video priors do not reliably predict failure; our PCS hypothesis is distinct — we are not asking the WAM to predict which future will occur, but whether a candidate action's latent z_{a,i} is consistent with the model's learned distribution over physically plausible futures. The PCS diagnostic (Section 3.1) directly tests this hypothesis; if ρ < 0.2, we report a negative result.' This framing makes the science defensible regardless of outcome.\n\n**3. Add World2Act (arXiv 2603.10422) and recalibrate RoboCasa baseline expectation (0.5 day).** Cite World2Act in related work as the March 2026 SOTA approach. Update the baseline expectations: 'UWM achieves 60.8% on RoboCasa with 1000 demo fine-tuning (World2Act, 2026); since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, our frozen baseline (Step 0a) is expected to be substantially lower — likely 10–30%.' Drop 'approaching Cosmos Policy 67.1%' as a primary framing target; the ≥10pp absolute improvement framing is more defensible and still publishable.\n\nMinimum viable CoRL submission remains: frozen UWM RoboCasa baseline + PCS diagnostic figure + Best-of-N results (PCS and/or Value MLP) + LIBERO-Long secondary + B/hard-argmax ablation + MG-Select-style KL baseline. The core contribution is scientifically legitimate; these fixes close the remaining differentiation gaps.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:51:48.644Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:51:48.644Z",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-10T08:51:48.680Z_

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

## Idea under review (round 5/10)
{
  "title": "Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning",
  "core_problem": "Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO and 91.8% on RoboTwin at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\n\nThe VLA test-time compute literature (2025–2026) has addressed candidate selection for VLA architectures: RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model; MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place; Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but crucially, Cosmos Policy's authors report that a model trained only on demonstrations 'cannot correctly predict failure states' and that rollout fine-tuning is required to enable effective planning. None of these approaches exploit WAMs' unique property: joint video-action pretraining that regularizes action latents z_a to be consistent with physically plausible visual futures, forming a success-biased latent distribution.\n\nThe critical unanswered question — which VLA approaches cannot answer — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens, enabling lightweight OOD-based candidate scoring without any rollout data? (2) Is this latent OOD signal more informative than action-space distributional uncertainty (MG-Select's KL signal) for candidate selection? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection. The companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\n\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path.",
  "opportunity": "UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection, exploiting the distributional structure of the WAM's joint video-action pretraining:\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8, significantly cheaper than video decoder passes. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\n\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) z_a regularized by joint video-action pretraining encodes physical plausibility co-varying with video futures, potentially creating a tighter success latent distribution with less success/failure overlap than VLA action tokens. LOC is WAM-specific in that this tighter latent structure is a direct consequence of joint video-action pretraining absent in VLAs. Differentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty). These are mechanistically distinct signals — one measures distributional membership relative to labeled success data, the other measures task-conditioning confidence.\n\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N candidate selection — it generates B actions, predicts future states and values for each, and executes the highest-value action. However, Cosmos Policy's planning mode (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states' (Cosmos Policy, 2026), and (b) queries the world model 3× and value function 5× per action (15 total forward passes per candidate) requiring parallel GPU infrastructure. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\n\nNote on PCS: The original approach of using video denoising error S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² as a zero-training quality signal is retained as a diagnostic comparison in the LOC diagnostic step (Step 1), not as a primary method. Cosmos Policy's explicit finding that demonstration-trained video priors do not reliably predict failure states, corroborated by the EVA 'executability gap' finding that visual coherence does not imply executable actions, provides strong prior evidence that raw denoising error will be a weak candidate selection signal. We include it as a secondary signal in Step 1 to report a clean negative result comparison against LOC.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N (a_{i*} = argmax_i V(z_{a,i})) is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs or VLA action tokens (the latent geometry argument). Failure demonstrations collected via frozen UWM rollouts in simulation (~15–20 H100-hours) plus Gaussian-perturbed synthetic failures (<1 H100-hour).\n\n**Comparison of LOC vs. Value MLP is itself a central contribution**: LOC requires zero training and no rollout data, but relies on the WAM's latent success distribution being well-separated from failure trajectories at inference; Value MLP requires failure demonstration collection but directly learns the task-specific quality function. Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space OOD approach outperforms action-space distributional uncertainty (MG-Select-style KL).\n\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline. The 'approaching Cosmos Policy 67.1%' framing is deprioritized; the more defensible framing is 'demonstrating that WAM-specific latent OOD selection enables meaningful gains without any fine-tuning, at ≤40 H100-hours cost.'",
  "landscape": "Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\n\nWorld2Act (arXiv 2603.10422, March 2026) — NEWLY ADDED. Achieves ~66% on RoboCasa (Cosmos Policy + World2Act) using only 50 real + 50 imagined demos, surpassing baseline Cosmos Policy. Method: aligns VLA action latents with world model video dynamics via a contrastive matching objective, reducing pixel-space dependence. Uses LLM-based skill decomposition to create RoboCasa-Skill and LIBERO-Skill datasets. Differentiation: World2Act requires contrastive post-training to align VLA action latents with video dynamics (modifies weights); our LOC method requires zero post-training and no weight updates — the alignment between action latents and video physics is inherited from UWM's joint pretraining. World2Act applies to VLAs requiring explicit alignment; our method exploits alignment that WAMs provide by construction.\n\nFast-WAM (arXiv 2603.16666, May 2026) is the critical framing reference. Test-time video generation adds only 0.5–1.9 percentage points: 97.6% LIBERO-avg and 91.8% RoboTwin without video at inference, at 190ms latency. Generates a single action trajectory with no candidate comparison. Complementary framing: Fast-WAM targets latency-critical deployment (single trajectory, fastest); our method targets success-critical tasks (B trajectories, select best via latent scoring at B × 5ms overhead).\n\nRoVer (arXiv 2510.10975, ICLR 2026) — Generates B candidate actions from frozen VLAs, trains a 0.2B Process Reward Model that scores candidates AND predicts refinement directions. Differentiation: (1) RoVer requires training a 0.2B PRM on process labels; LOC requires zero training and Value MLP requires only a 3-layer MLP; (2) RoVer applies to VLA action tokens lacking video-physics regularization; our methods target WAM action latents z_a jointly trained with video.\n\nVerifier-free / MG-Select (arXiv 2510.05681, ICLR 2026) — Training-free Best-of-N using KL-divergence from masked unconditional VLA distribution. 168% relative improvement on RoboCasa pick-and-place. Differentiation: MG-Select measures distributional uncertainty (how much task conditioning shifts the distribution from its unconditional prior) — an action-space confidence signal. LOC measures latent OOD membership (whether z_{a,i} is in-distribution relative to success demonstrations) — a latent-space quality signal. These are mechanistically different and testable: we include MG-Select-style KL applied to WAM as an explicit baseline in the ablation grid.\n\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — NEWLY ADDED AS SUPPORTING WORK. Frames failure detection as sequential OOD detection using conformal prediction on success-only demonstration data. Uses flow-based density estimation on distilled policy input/output signals. Demonstrates that OOD detection trained only on successes reliably detects failures at execution time. Relationship to LOC: LOC applies the same OOD detection principle to WAM action latents z_a for pre-execution candidate selection (ranking among B candidates before execution rather than monitoring execution). LOC differs in: (1) direct density estimation in action latent space vs. distilled scalar signal; (2) pre-execution selection vs. execution monitoring; (3) WAM-specific latent structure from joint video-action pretraining.\n\nEVA (arXiv 2603.17808, 2026) — NEWLY ADDED. Identifies 'executability gap' in video world models: visually coherent rollouts can violate kinematic constraints. Uses inverse dynamics model as training-time reward signal. Relevance: EVA's finding supports our decision to use action latent OOD scoring (LOC) rather than video denoising error (PCS) as the zero-training quality signal — visual coherence measured by denoising error does not imply executable actions. EVA's executability gap is complementary evidence that the latent action space (z_a) is a more direct quality substrate than the video prediction error.\n\nWAV: World-Value-Action Model (arXiv 2604.14732, April 2026) — Integrates a trajectory value module as a new architectural component trained from scratch; iterative latent-space inference concentrating probability mass on high-value trajectories. 99.6% LIBERO, 75.6% real-world dual-arm. Differentiation: WAV modifies the architecture and trains from scratch; our method leaves all WAM weights completely frozen and adds only a lightweight scoring module (LOC: no parameters; Value MLP: ~5M parameters). WAV is plug-in-incompatible with pretrained WAMs; our method is plug-in-compatible.\n\nCompose Your Policies! / GPC (arXiv 2510.01068) — Training-free convex composition of multiple frozen policy distributions. Different: operates at distribution level (combining score functions of multiple policies), not discrete candidate selection from a single frozen WAM; requires multiple compatible policies.\n\nGPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax. Our method uses the WAM's own action latent space as the evaluation substrate — no separate world model.\n\nWhen to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution. Orthogonal and combinable with our pre-execution selection.",
  "approach": "Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\n\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing and drop all 'approaching Cosmos Policy 67.1%' language. Cost: ~2–3 H100-hours.\n\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator.\n\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\n\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Validate whether WAM action latent OOD scoring correlates with ground-truth task success, and compare against video denoising error (PCS) as a secondary signal.\n\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and PCS scores.\n\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} — expected to show lower AUC and ρ than LOC based on Cosmos Policy finding and EVA's executability gap evidence. Also compute MG-Select-style KL score as third comparison signal.\n\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC, confirming latent OOD density is more informative than video denoising error or action-space distributional uncertainty. If LOC AUC < 0.55 at all density estimator configurations, report as negative result; Value MLP becomes sole primary contribution. Decision: if LOC AUC ≥ 0.60, LOC is reported as primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison to PCS.\n\nThis diagnostic is a key scientific contribution: it empirically tests whether WAM joint pretraining creates a success latent distribution that is more quality-discriminative than video denoising error or distributional uncertainty, directly addressing open questions about WAM latent structure.\n\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity. Binary classification accuracy on held-out demo set as latent separability sanity check.\n\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Cost: ~3–5 H100-hours.\n\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\n\nPrimary results (two methods):\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific]\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific]\n\nComparisons (required): MG-Select-style KL scoring applied to WAM action-only inference (VLA method applied to WAM backbone, directly comparable to LOC on same benchmark); random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\n\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC, confirming negative result); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\n\n**Ablation Grid**: B ∈ {1, 2, 4, 8, 16} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. MG-Select-style KL (VLA method applied to WAM, key comparison) vs. PCS denoising error (expected negative result) vs. random selection (sanity check); noise temperature T_noise ∈ {1.0, 1.5, 2.0} (informed by diversity pilot); execution regime: (a) open-loop (B trajectories at episode start, execute selected) vs. (b) periodic replanning every K=5 action chunks.\n\n**Primary hypotheses**: (H1) LOC achieves Spearman ρ > 0.3 and AUC > 0.6 in the diagnostic, confirming WAM success latents form an OOD-detectable distribution; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic (latent OOD density > video denoising error ≈ action-space KL), with PCS showing AUC near 0.5 consistent with Cosmos Policy's finding; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform MG-Select-style KL applied to WAM, confirming latent quality-discrimination advantages of WAM joint pretraining over distributional uncertainty.\n\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, MG-Select-style KL applied to WAM.\n\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~140h H100",
      "gpu_utilization": "HIGH idle (~35–55%): GPU waits while researcher implements LOC density estimator (KNN/GMM fitting), interprets LOC diagnostic results, debugs failure collection pipeline, and designs ablations. LOC inference overhead (5ms/candidate) reduces GPU demand vs. PCS (~50ms/candidate).",
      "timeline": "2–3 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$350 (140h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)"
    },
    "human_in_loop": {
      "gpu_hours": "~165h H100",
      "gpu_utilization": "MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, LOC diagnostic, failure collection, demo encoding, density estimator fitting, and experiment submission; human reviews Step 0a baseline and LOC diagnostic results at daily check-ins to make go/no-go decisions",
      "timeline": "3–4 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)",
      "estimated_gpu_cost": "~$413 (165h × $2.50/h)",
      "risk_note": "Step 0a (frozen UWM RoboCasa baseline) and LOC diagnostic are hard sequential dependencies before main ablation. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → LOC diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, parallel with LOC) → demo encoding + density fitting (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. LOC density estimation (KNN/GMM fitting) is computationally trivial and requires no GPU after demo encoding. DreamZero cross-WAM deferred to camera-ready."
    },
    "auto_research": {
      "gpu_hours": "~320h H100 (UWM backbone only; full B/T_noise ablation grid; RoboCasa + LIBERO-Long; multiple seeds; LOC diagnostic, PCS comparison, Value MLP comparisons)",
      "gpu_utilization": "MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic (including PCS comparison), failure collection, demo encoding, density fitting, MLP training, and evaluation continuously. LOC inference is faster than PCS, reducing wall-clock time for ablation runs.",
      "timeline": "7–10 days with 4–8 H100 GPUs simultaneously",
      "team": "0 (only initial repo setup and credential configuration)",
      "claude_api_cost": "$200–350 (~2,500–4,000 turns at Opus rates)",
      "estimated_gpu_cost": "~$800 (320h × $2.50/h)",
      "speed_bottleneck": "Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.",
      "risk_note": "LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation — significantly lower implementation risk than PCS, which required implementing UWM mixed-mode forward passes not present in the public repository. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation."
    }
  },
  "target_venues": [
    "CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS comparison showing expected negative result) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready. LOC implementation is lower risk than PCS was (no custom mixed-mode forward pass needed).",
    "ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation in WAM vs. VLA latent spaces), DreamZero cross-WAM evaluation, and potential real-world experiments."
  ],
  "level": "solid",
  "key_references": [
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates",
    "World2Act (arXiv 2603.10422, March 2026) — NEWLY ADDED: post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; aligns VLA action latents with world model video dynamics via contrastive matching objective; reports UWM achieves 60.8% on RoboCasa with 1,000 demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; our LOC exploits WAM alignment inherited from joint pretraining",
    "Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666, May 2026) — CRITICAL FRAMING: 97.6% LIBERO, 91.8% RoboTwin at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead",
    "FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — NEWLY ADDED SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; theoretical foundation for LOC's approach of using KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection",
    "EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — NEWLY ADDED: identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; uses inverse dynamics model as training-time reward; supports LOC over PCS: visual denoising error (PCS) does not predict task success, while action latent OOD (LOC) is more directly quality-relevant",
    "RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization",
    "Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution; MG-Select cannot exploit WAM latent geometry from joint pretraining",
    "World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — SIGNIFICANT OVERLAPPING MOTIVATION: trajectory value module requiring training from scratch, new architectural component; 99.6% LIBERO, 75.6% real-world; our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs",
    "Compose Your Policies! / GPC (arXiv 2510.01068) — PRIOR WORK: training-free distribution composition for multiple frozen policies; operates at distribution level, not discrete candidate selection from single WAM",
    "Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — PRIOR WORK: frozen policy + separately trained world model + hard argmax; our method uses WAM's own action latent space, no separate world model",
    "Unified World Models / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference; publicly available weights and code",
    "Diffusion Policy (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting",
    "When to Trust Imagination (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides action chunk sizes; orthogonal to our pre-execution selection; combinable",
    "World Action Models as Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version",
    "OA-WAM (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding)",
    "CKT-WAM (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer)",
    "GigaBrain-0.5M* (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training",
    "H-WM (arXiv 2602.11291) — requires hierarchical architectural co-design",
    "Latent Diffusion Planning (arXiv 2504.16925) — trains diffusion planner from scratch"
  ],
  "description": "Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods.\n\nThe key insight, refined from prior work: Cosmos Policy's own finding that demonstration-trained video priors 'cannot correctly predict failure states' — and EVA's demonstration of an 'executability gap' where video denoising quality does not predict executable actions — rules out video denoising error as a reliable zero-training quality signal. Instead, we exploit a different WAM-specific property: joint video-action pretraining creates action latents z_a that form a distribution regularized by physical plausibility, where the success demonstration distribution in latent space is distinguishable from failure trajectories. FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects failures; we apply this principle to WAM action latents for pre-execution candidate selection.\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8. Differentiated from MG-Select: LOC scores latent OOD membership relative to labeled success data; MG-Select scores action-space distributional uncertainty. WAM-specific: z_a regularized by joint video-action pretraining may create tighter, better-separated success latent distributions than VLA action tokens.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection avoids multi-modal action-averaging artifact (Diffusion Policy). Central hypothesis: joint pretraining geometry makes z_a more linearly separable between success/failure regimes than VLA action tokens.\n\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target > 0.6), compared against: (a) video denoising error S_PCS (expected negative result based on Cosmos Policy and EVA evidence), (b) MG-Select-style KL applied to WAM. If S_LOC AUC < 0.55, LOC reported as negative result; Value MLP becomes sole primary contribution.\n\nMandatory baselines: (1) frozen UWM RoboCasa validation (Step 0a, expected 10–25%); (2) MG-Select-style KL as key comparison against LOC; (3) PCS in diagnostic as expected negative result.\n\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as upper references). Secondary: LIBERO-Long. CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.",
  "project_name": "frozen_wam_mppi",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL OMISSION — Cosmos Policy (arXiv 2601.16163, ICLR 2026): This paper fine-tunes Cosmos-Predict2 (a pretrained video foundation model) to generate future state images and value estimations as latent frames, enabling test-time planning of action trajectories with higher success probability. It achieves 98.5% on LIBERO and 67.1% on RoboCasa — the exact benchmarks proposed here. The Generator does not cite or differentiate against Cosmos Policy. This is the closest prior work and must be addressed head-on.", "CRITICAL — Unvalidated 'early commitment' transfer to manipulation: ChEaP (arXiv 2603.30043) demonstrated early plan commitment only for 2D maze solving using Wan2.2-14B and HunyuanVideo-1.5. DreamZero-14B and UWM are trained on manipulation demonstrations with very different visual dynamics, object contact physics, and action-conditioned structure. There is no evidence that T_partial=5–10 steps in these models captures trajectory-discriminative information rather than unstructured noise.", "CRITICAL — Inference-time compute cost ignored: Running B=32–64 candidates × T_partial=5–10 diffusion steps through DreamZero-14B at each receding-horizon step requires 160–640 forward passes of a 14B model per action chunk. At 7Hz target control frequency, this is computationally infeasible. The proposal correctly analyzes training cost (≤10 H100-hours for value head) but completely ignores the inference bottleneck, which is the binding constraint for real deployment.", "SIGNIFICANT — Value MLP discriminability under high noise: Binary success/failure labels from LIBERO demos will train the MLP on clean completions, but the MLP receives noisy partial latents at T_partial=5–10 steps. The distributional gap between training inputs (full trajectories' latent encodings) and inference inputs (noisy partial denoising outputs) is not addressed. There is no prior work showing a simple MLP can usefully score heavily-noised intermediate latents of a manipulation-domain video diffusion model.", "SIGNIFICANT — Training data generation cost underestimated: The ≤5–8 H100-hour value head training estimate ignores the cost of generating the training dataset itself: every LIBERO-90 demo must be encoded by the frozen DreamZero-14B VAE and partially denoised for T_partial steps to produce (latent, label) pairs. With LIBERO-90 × hundreds of demonstrations each, this generation phase alone likely exceeds the stated budget.", "MODERATE — Joint video+action latent structure not addressed: DreamZero jointly denoises video and action tokens. Stopping at T_partial steps yields mixed video+action latent states. The proposed 3-layer MLP scores 'video latents' but the actual representation interleaves action information. The architectural mismatch between 'video-only MPPI' and DreamZero's joint denoising structure is not addressed.", "MODERATE — UWM compatibility uncertain: UWM (arXiv 2504.02792, RSS 2025) uses independent diffusion timesteps per modality. Treating the video latent of a partially-denoised UWM trajectory as a planning substrate requires careful handling of the asynchronous noise schedule — stopping video denoising at T_partial while action denoising may be at a different schedule step. The proposal does not address this."]
Feedback: The core idea — converting any pretrained WAM into a receding-horizon planner without retraining via partial-denoising MPPI — is intellectually clean and addresses a real gap. But three revisions are needed before this is CoRL-ready:

1. **Acknowledge and differentiate Cosmos Policy (ICLR 2026)**: This paper is your most direct prior work. Both you and Cosmos Policy use value functions over video diffusion WAMs for test-time planning on LIBERO/RoboCasa. Your differentiation must be sharp: 'Cosmos Policy requires full fine-tuning of a 12B+ model on robot demos (~200 H100-hours); our value MLP costs ≤10 H100-hours and leaves WAM weights frozen, making it applicable to any pretrained WAM as a plug-in.' Frame this clearly in abstract and related work.

2. **Pilot experiment validating early commitment for manipulation**: Before submitting, run a quick diagnostic: take DreamZero or UWM, generate B=16 trajectories with T_partial ∈ {3,5,10,20,full} steps, and measure the correlation between early-step latent cosine similarity and final task success rate on LIBERO-Spatial (easy tasks). If early commitment holds, you'll have a strong motivating figure. If it doesn't (i.e., early latents don't predict outcome), the entire method premise collapses and you need a different approach — consider using the full denoising but fewer candidates (B=4–8), or replacing MPPI over partial latents with best-of-N reranking over fully denoised trajectories using the value MLP.

3. **Address inference-time cost honestly**: Calculate and report wall-clock time per planning step with B=32, T_partial=5, DreamZero-14B. If it exceeds ~500ms/step, real-time control is impossible. Propose a solution: (a) use UWM (smaller model) instead of DreamZero-14B; (b) reduce B to 8–16 with correspondingly less compute; (c) restrict experiments to open-loop planning (generate full plan once, execute) rather than receding-horizon replanning. The paper is stronger if it clearly bounds the inference overhead and scopes claims accordingly.

If the early-commitment pilot experiment fails, consider pivoting to 'Best-of-N with Full Denoising': run B=4 full trajectories through the frozen WAM, score with value MLP trained on clean latents, select the highest-valued action chunk. This avoids the noisy-partial-latent discriminability issue, reduces inference cost, and preserves the zero-WAM-retraining property.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Action-averaging artifact unaddressed: Computing weighted average sum_i w_i * a_i over multi-modal manipulation trajectories is known to produce invalid/infeasible actions. For example, if half the trajectories grasp an object from the left and half from the right, the weighted average drives the gripper straight into the object. This is a well-documented failure mode of averaging over multi-modal distributions (see Diffusion Policy paper and 2025 diffusion survey). The proposal presents soft importance weighting as a strength over hard argmax, but for manipulation this may be strictly worse than GPC-RANK's hard argmax selection. No ablation validates that soft averaging outperforms hard selection in practice.", "CRITICAL — No failure demonstrations in LIBERO for value MLP training: LIBERO-90 consists entirely of successful human teleoperation demonstrations. The proposal says 'label each with task success/failure from demo metadata' but there are no failure trajectories in the standard LIBERO-90 dataset — all demos are successful by construction. Training a binary success/failure MLP requires negative examples, which must be generated via online simulation rollouts of the policy. This adds substantial cost (20–40 H100-hours of simulation rollouts, policy execution, and data collection) not accounted for in the ≤18 H100-hour budget.", "CRITICAL — Fast-WAM (arXiv 2603.16666) challenges the core premise: Fast-WAM demonstrates that 'the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time,' achieving competitive performance with zero test-time video generation and 4× faster inference. If test-time video futures add minimal value, generating B=4–8 full denoised trajectories per planning step is computationally wasteful with limited benefit. Reviewers will ask: why not just use Fast-WAM-style action prediction (no video generation) instead of full-trajectory MPPI?", "SIGNIFICANT — Unlisted concurrent work: 'When to Trust Imagination: Adaptive Action Execution for World Action Models' (arXiv 2605.06222, May 2026) addresses the same problem — when and how to use WAM imagined futures for action execution — and must be cited and differentiated. Additionally, OA-WAM (arXiv 2605.06481) and CKT-WAM (arXiv 2605.06247) are May 2026 papers in the same WAM inference-efficiency space.", "SIGNIFICANT — Discriminability assumption not validated: B=4–8 trajectories sampled from the same frozen WAM with the same task conditioning and different Gaussian seeds may have high cosine similarity in the WAM's latent space, leaving the value MLP with insufficient discriminative signal. The entire method's gain depends on there being meaningful variance in V(z_i) across the B samples — this is empirically unvalidated and constitutes a failure mode that would produce near-uniform MPPI weights (degenerate to random selection). No pilot experiment or cited evidence supports that UWM trajectories have sufficient diversity for this purpose.", "MODERATE — LIBERO is essentially saturated at the top end: Cosmos Policy achieves 98.5% on LIBERO; multiple 2025 papers report >95%. LIBERO-Long is a better choice (as the proposal selects), but reviewers will note the benchmark is limited. The comparison against Cosmos Policy published results ('cited for context on fine-tuned WAM upper bound') does not constitute a meaningful experimental comparison — CoRL reviewers will expect at least one shared evaluation setup.", "MODERATE — Soft vs. hard averaging contribution is marginal: The headline differentiator from GPC-RANK is replacing hard argmax with soft importance-weighted averaging — a 2-line change. This is not a novel architectural contribution. The stronger claim (plug-in to any frozen WAM, no separate world model) is more defensible as a contribution but needs to be empirically demonstrated across at least two WAM backbones (UWM + DreamZero-14B) to support the 'plug-in' generalization claim, which is proposed as secondary and may not be completed within 20 days."]
Feedback: The Round 1 revisions were correctly executed — the pivot from partial denoising to full denoising, addition of Cosmos Policy as critical prior work, and inference cost scoping are all sound. However, three new issues block submission:

1. **Fix the action-averaging artifact or reframe the contribution**: Soft weighted averaging of manipulation trajectories is known to produce infeasible blended actions in multi-modal settings. Either (a) pivot the primary result to hard argmax selection (making MPPI weighting the ablation rather than the headline), or (b) show empirically on LIBERO-Long that MPPI soft weighting outperforms hard argmax. Option (a) is safer given the 20-day timeline and actually aligns better with GPC-RANK comparison story. Keep soft weighting as an ablation, not the main claim.

2. **Generate failure demonstrations before training the value MLP**: LIBERO-90 has no failure trajectories. You must run the frozen UWM policy on LIBERO tasks in simulation to collect rollout failures as negatives. Budget ~20 H100-hours for this. Alternatively, add synthetic failures by perturbing successful demo actions with Gaussian noise and flagging truncated episodes as failures. Without negatives, the classifier cannot train. This should be described explicitly as Step 0 of the approach.

3. **Explicitly address Fast-WAM (arXiv 2603.16666)**: Add a paragraph in related work explaining why generating full video trajectories for scoring is still valuable despite Fast-WAM's finding. The argument: Fast-WAM improves efficiency by removing video generation from inference, but its single-trajectory output cannot compare candidate futures. Frozen-WAM MPPI accepts the compute overhead of B full trajectories to enable candidate selection — a different tradeoff point optimizing for task success rate rather than latency. Frame this as a complementary approach: Fast-WAM for latency-critical deployment, Frozen-WAM MPPI for success-critical tasks where longer planning time is acceptable.

4. **Add a diversity pilot experiment**: Before the full ablation, show a diagnostic figure: sample B=16 trajectories from frozen UWM on 3 LIBERO-Long tasks, measure latent diversity (pairwise cosine distance of z_i) and correlation of V(z_i) with ground-truth success (if rollouts are available). If diversity is low (all z_i are within 0.1 cosine distance), increase noise temperature or add perturbations to the conditioning. This directly validates the premise of the entire method.

### Round 3 review
Verdict: revise
Issues: ["SIGNIFICANT — Three important related papers are completely absent from the landscape: (1) RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975): generates B candidate actions from a frozen VLA, scores with a trained Process Reward Model (PRM), and selects via argmax — evaluated on CALVIN + real robot (GR-1, Dita, MoDE backbones). Different policy class (VLA not WAM) and benchmark (CALVIN not LIBERO/RoboCasa), but the paradigm is essentially identical. Must be cited and differentiated. (2) Verifier-free Test-Time Sampling for Vision Language Action Models (arXiv 2510.05681, ICLR 2026): Best-of-N for frozen VLAs using KL-divergence from a masked reference distribution as a confidence signal — no additional training required; achieves 168% relative improvement on pick-and-place. Differentiator: no trained value model; applicable to VLAs not WAMs. Must be cited. (3) Compose Your Policies! (arXiv 2510.01068): test-time policy composition for diffusion/flow-based robot policies without retraining, using score composition. Must be cited.", "CRITICAL — Frozen UWM baseline on RoboCasa is an unvalidated assumption that may be dramatically wrong. The UWM paper (RSS 2025, arXiv 2504.02792) evaluates primarily on LIBERO and OXE-distribution tasks; no published RoboCasa-without-fine-tuning results exist. Cosmos Policy achieves 67.1% on RoboCasa only after 1,536 H100-hours of domain-specific fine-tuning. A frozen UWM — not fine-tuned on RoboCasa's kitchen tasks — achieving 40-55% baseline success seems optimistic; 15-30% is more plausible. If the actual baseline is 15-30%, the ≥60% target requires +30-45pp from a 3-layer MLP scoring action latents, which is almost certainly too large. The Generator should: (a) run a quick 50-episode RoboCasa baseline with frozen UWM before committing to ≥60% target; (b) recalibrate the target to 'improve baseline by ≥10pp' rather than 'approach Cosmos Policy 67.1%' if baseline is lower than expected.", "SIGNIFICANT — The World-Value-Action (WAV) model (arXiv 2604.14732, April 2026) proposes a trajectory value function that 'evaluates long-horizon utility' and generates actions via 'inference in latent space where the model progressively concentrates probability mass on high-value trajectories.' This is substantially overlapping in motivation (value scoring over latent trajectory representations) though architecturally different (implicit latent inference vs. discrete Best-of-N selection). Should be cited and explicitly differentiated: WAV modifies the VLA architecture; this proposal keeps all weights frozen.", "MODERATE — Novelty argument is insufficiently grounded for CoRL acceptance. The technical differentiation from RoVer reduces to: (a) WAM action latents vs. VLA action space, (b) UWM action-only mode vs. standard policy, (c) LIBERO/RoboCasa vs. CALVIN. These are valid engineering differences but unlikely to meet CoRL's bar for conceptual novelty. The proposal needs a sharper 'why WAM action latents?' argument — specifically, that the WAM's joint video-action pretraining instills physical grounding into the action latent z_a that pure action-space policies lack, making the latent richer for value estimation. This would differentiate from RoVer on principled grounds, not just implementation.", "MODERATE — The DreamZero-14B cross-WAM evaluation is described as secondary but is essential for the 'plug-in across WAM architectures' claim. DreamZero-14B requires full video+action denoising (no native action-only mode), making B-trajectory sampling substantially more expensive than for UWM. If this experiment cannot be completed within the 20-day window (likely, given 50 H100-hours estimate), the 'plug-in' contribution collapses to a single-architecture result, significantly weakening the generalization claim. The Generator should either (a) commit to completing DreamZero validation within the timeline or (b) reframe the contribution as UWM-specific and drop the plug-in generalization claim.", "MODERATE — The feasibility of training a discriminative value MLP from action latents depends on a premise not yet verified: that frozen UWM action latents from successful and failed demonstrations are separable in the latent space. If UWM's action latent z_a primarily encodes task semantics (what to do) rather than execution quality (how well to do it), success/failure labels may be uncorrelated with latent structure and the MLP will learn a degenerate classifier. The diversity pilot (Spearman ρ > 0.3 target) partially addresses this, but binary classification accuracy on held-out demos should also be reported as a sanity check before the main ablation."]
Feedback: The Round 3 revision has correctly addressed all three Round 2 critical issues: (1) hard argmax is now the primary result with solid justification, (2) Step 0 failure collection is explicitly specified at 15-20 H100-hours, and (3) Fast-WAM is now integrated as a complementary framing. The diversity pilot is a strong addition. However, three concrete fixes are needed before CoRL submission:

**1. Add and differentiate three missing related papers (1-2 days).** You must cite RoVer (arXiv 2510.10975), Verifier-free Test-Time Sampling (ICLR 2026, arXiv 2510.05681), and Compose Your Policies! (arXiv 2510.01068) in your related work section. The differentiation argument for RoVer specifically should be: 'RoVer applies to VLA architectures in token-action space using an explicitly trained PRM; our method targets WAMs whose joint video-action pretraining produces physically grounded action latents z_a that are richer substrates for value estimation than action tokens from VLAs — we exploit this WAM-specific property to eliminate the need for a separate process reward model training stage.' Also cite WAV (arXiv 2604.14732) as addressing value-guided action selection within VLAs via implicit latent inference, and differentiate: 'WAV modifies the architecture; Frozen-WAM BoN leaves all weights frozen.'

**2. Validate the frozen UWM baseline on RoboCasa before committing to ≥60% target (3-5 days, highest priority).** Run 50 episodes of B=1 frozen UWM action-only inference on a representative subset of RoboCasa tasks. If the baseline is 40-55%, the ≥60% target is appropriate. If it is 15-35% (which is equally plausible given no published UWM/RoboCasa results), you must: (a) adjust the target to 'improve baseline success rate by ≥10pp absolute,' and (b) reframe the comparison away from 'approaching fine-tuned Cosmos Policy (67.1%)' toward 'meaningful improvement over frozen WAM without any fine-tuning, at ≤40 H100-hours training.' The latter is still a publishable result; the former collapses if the baseline is too low.

**3. Sharpen the theoretical motivation for WAM latents over action space (0.5 days).** Add one paragraph explaining why z_a from a jointly-trained video-action WAM contains more quality-discriminative information than the output action tokens of a VLA. The key insight: UWM's video diffusion process regularizes z_a to be consistent with physically plausible visual futures, instilling motion-physics grounding that raw VLA action tokens lack. This is why a 3-layer MLP over z_a can succeed where the same MLP over VLA output tokens would fail — and this is your fundamental novelty claim that differentiates Frozen-WAM BoN from RoVer at the conceptual level.

Minimum viable CoRL submission: frozen UWM + RoboCasa Best-of-N (primary) + LIBERO-Long (secondary) + diversity pilot figure + B/hard-argmax ablation. Drop DreamZero cross-WAM to camera-ready — it adds a 50 H100-hour sequential dependency that cannot be completed before the diversity pilot results inform whether the premise holds.

### Round 4 review
Verdict: revise
Issues: ["MODERATE — Cosmos Policy planning mode under-differentiated: Cosmos Policy already implements Best-of-N video-based candidate selection (generates B actions, predicts future states + values, selects highest-value). The Generator cites Cosmos Policy's training cost but does not explicitly acknowledge its planning mode does conceptually the same candidate scoring loop. The differentiation must be stated precisely in the methods section: 'Cosmos Policy planning mode also ranks candidates via video futures, but requires fine-tuning a value function on rollout data; PCS is zero-training and requires only the frozen WAM's existing video prior — at the cost of relying on a less reliable signal not explicitly trained for failure prediction.'", "SIGNIFICANT — PCS premise directly challenged by Cosmos Policy's own finding: Cosmos Policy's paper states the base model trained only on demonstrations 'cannot correctly predict failure states' and requires on-policy rollout fine-tuning to enable effective planning. This directly challenges PCS's claim that a frozen WAM's video prior (trained primarily on demonstrations) can serve as a reliable quality signal. The Generator must address this in the paper — either (a) argue why denoising error is a different and more robust signal than explicit state prediction, or (b) anticipate in the intro that PCS may fail and explicitly credit the diagnostic as a scientific contribution in either outcome. The current framing treats PCS failure as a fallback but does not acknowledge the strong prior evidence suggesting it may fail.", "MODERATE — UWM's 60.8% RoboCasa result requires 1000-demo fine-tuning, not frozen inference: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1000 real demonstrations. Since UWM was trained only on DROID data (no RoboCasa), this is a fine-tuned result. The frozen UWM baseline (no RoboCasa demos) is likely 10–25%, not 40–55%. The Generator already handles this with adaptive framing in Step 0a, but the baseline expectation should be calibrated to 'likely 10–25%' to avoid surprises. The framing of 'approaching Cosmos Policy 67.1%' should be deprioritized in favor of the more defensible '≥10pp improvement over frozen baseline.'", "MODERATE — World2Act (arXiv 2603.10422, March 2026) is missing from the landscape: World2Act achieves 66.3% on RoboCasa (Cosmos Policy + World2Act) using only 50 real + 50 imagined demos, surpassing baseline Cosmos Policy and representing the current published SOTA approach. As a concurrent March 2026 paper using world model latents to improve policy performance, it should be cited and differentiated: 'World2Act aligns VLA action latents with world model video dynamics via contrastive post-training; our method requires no post-training of any kind for PCS, and no world model separate from the frozen WAM for Value MLP.'", "MINOR — Cosmos Policy planning mode inference cost not addressed: Cosmos Policy's planning mode 'ensembles predictions by querying the world model three times per action and the value function five times per future state (15 total value predictions per action)' using N GPUs in parallel. The Generator should note that Cosmos Policy's planning mode at inference is also expensive (requires fine-tuned planning model, multiple forward passes, parallel GPUs) vs. PCS's single video decoder pass per candidate — the inference efficiency comparison is part of the full cost story."]
Feedback: The Round 4 revision has correctly addressed all Round 3 critical issues. The paper is structurally sound with good fallback plans. Three concrete fixes are needed for CoRL submission:

**1. Address the Cosmos Policy planning-mode differentiation gap (0.5 day).** In the methods section and related work, add an explicit paragraph: 'Cosmos Policy (ICLR 2026) implements Best-of-N candidate selection via video-future scoring in its planning mode — it generates B candidate actions, predicts future states and values for each via a fine-tuned planning model, and executes the highest-value action. Our work targets the same planning loop but requires zero weight updates: PCS uses the frozen WAM's existing video prior as quality signal, while Cosmos Policy requires fine-tuning on rollout data to learn an explicit failure-predictive value function.' This is your sharpest differentiation claim.

**2. Confront the Cosmos Policy anti-evidence for PCS (0.5 day).** Cosmos Policy's paper explicitly found that a model trained only on demonstrations cannot predict failure states — rollout fine-tuning is required. Add a paragraph acknowledging this: 'Cosmos Policy's authors observe that demonstration-trained video priors do not reliably predict failure; our PCS hypothesis is distinct — we are not asking the WAM to predict which future will occur, but whether a candidate action's latent z_{a,i} is consistent with the model's learned distribution over physically plausible futures. The PCS diagnostic (Section 3.1) directly tests this hypothesis; if ρ < 0.2, we report a negative result.' This framing makes the science defensible regardless of outcome.

**3. Add World2Act (arXiv 2603.10422) and recalibrate RoboCasa baseline expectation (0.5 day).** Cite World2Act in related work as the March 2026 SOTA approach. Update the baseline expectations: 'UWM achieves 60.8% on RoboCasa with 1000 demo fine-tuning (World2Act, 2026); since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, our frozen baseline (Step 0a) is expected to be substantially lower — likely 10–30%.' Drop 'approaching Cosmos Policy 67.1%' as a primary framing target; the ≥10pp absolute improvement framing is more defensible and still publishable.

Minimum viable CoRL submission remains: frozen UWM RoboCasa baseline + PCS diagnostic figure + Best-of-N results (PCS and/or Value MLP) + LIBERO-Long secondary + B/hard-argmax ablation + MG-Select-style KL baseline. The core contribution is scientifically legitimate; these fixes close the remaining differentiation gaps.


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
  "promptId": "7cfc2bf9-4784-4738-bc7e-6ecf5c05863c",
  "type": "user",
  "uuid": "60ca5ed8-c83e-45f7-aeab-f9f9817347d4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:51:48.673Z_

```json
{
  "parentUuid": "60ca5ed8-c83e-45f7-aeab-f9f9817347d4",
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
  "uuid": "9cfb87d2-0876-491f-8c43-6f99daed26b3",
  "timestamp": "2026-05-10T08:51:48.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:51:48.673Z_

```json
{
  "parentUuid": "9cfb87d2-0876-491f-8c43-6f99daed26b3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dbcb8d59-e86e-4acc-9bef-a06d49ebf2c5",
  "timestamp": "2026-05-10T08:51:48.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
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
  "leafUuid": "dbcb8d59-e86e-4acc-9bef-a06d49ebf2c5",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent candidate selection via OOD and value functions",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:52:04.819Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. This is Round 5 of 10 review for a paper about "Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning" targeting CoRL 2026.

Let me review what's been addressed from Round 4:
1. Cosmos Policy planning-mode differentiation - NOW ADDRESSED: explicit discussion of 15 forward passes per candidate vs. zero weight updates
2. PCS premise vs. Cosmos Policy finding - NOW ADDRESSED: PCS is now a "diagnostic comparison" for a "negative result," while LOC (Latent OOD Consistency Scoring) is the primary zero-training method


3. World2Act added and RoboCasa baseline recalibrated - NOW ADDRESSED: World2Act cited, baseline expected 10-25%
4. Framing changed from "approaching 67.1%" to "≥10pp improvement over frozen baseline" - ADDRESSED

The major pivot in this round: the primary zero-training method has completely shifted from PCS (video denoising error) to LOC (Latent OOD Consistency Scoring using KNN/GMM density estimation on success demo latents), with PCS now serving as a diagnostic comparison showing expected negative results, and FAIL-Detect being incorporated as an additional baseline.

The new contributions center on LOC for zero-weight updates with density estimation on success latents, the Action-Latent Value MLP as the second method, and a diagnostic comparison across LOC, PCS, and MG-Select-style approaches. Now I need to verify whether the cited papers actually support these claims and whether the core assumption about WAM action latents forming a success manifold holds up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbcb8d59-e86e-4acc-9bef-a06d49ebf2c5",
  "isSidechain": false,
  "requestId": "req_011CatbxS84KJPpAq7r85PQM",
  "type": "assistant",
  "uuid": "997279be-2e89-47df-9635-414a4b719b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011aZfB9xc7czT69ufkHp3he",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1962,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 9 · 2026-05-10T08:52:04.827Z_

I'll conduct independent research to verify the key claims of this Round 5 revision before issuing a verdict. Let me search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "997279be-2e89-47df-9635-414a4b719b3f",
  "isSidechain": false,
  "requestId": "req_011CatbxS84KJPpAq7r85PQM",
  "type": "assistant",
  "uuid": "4e949294-538a-45d6-93d7-82a899d43a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011aZfB9xc7czT69ufkHp3he",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1962,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 10 · 2026-05-10T08:52:11.229Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AJgYeS6X2b1LBH8aP8pmQm`</summary>

```json
{
  "description": "Verify FAIL-Detect and EVA paper existence and claims",
  "subagent_type": "Explore",
  "prompt": "Search for and verify two specific papers cited in a robotics ML paper:\n\n1. FAIL-Detect (arXiv 2503.08558): Supposedly \"Failure Detection as OOD Detection for Robot Manipulation\" published at RSS 2025. The paper is claimed to \"prove that OOD detection on success-only demonstration data reliably detects policy failures\" using flow-based density estimation and conformal prediction. Search: \n- site:arxiv.org 2503.08558\n- \"FAIL-Detect\" failure detection OOD detection robot manipulation RSS 2025\n- OOD detection robot failure detection conformal prediction success demonstrations 2025\n\n2. EVA (arXiv 2603.17808): Supposedly \"Aligning Video World Models with Executability\" from 2026. Claims to demonstrate an \"executability gap\" showing visually coherent world model rollouts can violate kinematic constraints.\n- site:arxiv.org 2603.17808\n- EVA executability gap video world models robot 2026\n- \"executability gap\" video world model kinematic constraints\n\nFor each paper, report: Does it actually exist? What does it actually claim? Does it support the uses described above?\n\nAlso search for: \"latent OOD detection robot candidate selection\" to find any prior work on using OOD detection on latent action representations for candidate selection (which would challenge novelty)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e949294-538a-45d6-93d7-82a899d43a63",
  "isSidechain": false,
  "requestId": "req_011CatbxS84KJPpAq7r85PQM",
  "type": "assistant",
  "uuid": "6d4db72d-b2cb-495b-b027-6f914aaa7813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011aZfB9xc7czT69ufkHp3he",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1962,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 11 · 2026-05-10T08:52:18.092Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SjK7UJqWUKVJB15gEJXzru`</summary>

```json
{
  "description": "Search for competing latent OOD candidate selection papers in robotics",
  "subagent_type": "Explore",
  "prompt": "Search for papers that use OOD detection or density estimation on policy latents for candidate selection or action filtering in robot manipulation. I'm reviewing a paper that proposes \"Latent OOD Consistency Scoring (LOC)\" - fitting a KNN/GMM density estimator on success demonstration latents and using it to score/select candidate actions. I need to know if this already exists.\n\nSearch queries to run:\n1. \"OOD detection\" \"action latent\" robot manipulation candidate selection 2025 2026 arxiv\n2. \"density estimation\" \"action latent\" robot policy candidate selection best-of-N\n3. \"success distribution\" latent space robot policy filtering 2025 2026\n4. \"conformal prediction\" robot action selection manipulation 2025 2026 arxiv\n5. \"KNN\" OR \"GMM\" robot policy latent quality scoring candidate selection\n6. site:arxiv.org \"latent OOD\" robot manipulation action selection\n7. \"test-time compute\" robot manipulation \"OOD\" OR \"out-of-distribution\" latent 2025 2026\n\nAlso check: \n- Does MG-Select (arXiv 2510.05681) actually use KL from masked distribution? Is its mechanism really different from LOC?\n- Search: \"MG-Select\" robot VLA test-time sampling arxiv 2510.05681\n\nReport what you find about each query, especially any papers that do something similar to LOC (density estimation on success demo latents for candidate scoring)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d4db72d-b2cb-495b-b027-6f914aaa7813",
  "isSidechain": false,
  "requestId": "req_011CatbxS84KJPpAq7r85PQM",
  "type": "assistant",
  "uuid": "9c834a37-cf39-47ed-98a1-bbaef32c67ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011aZfB9xc7czT69ufkHp3he",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1962,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 12 · 2026-05-10T08:52:25.183Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01F5syVZWrWhuRBf3xo9qRHZ`</summary>

```json
{
  "description": "Search for recent WAM and latent planning papers that could compete with or overlap this idea",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a robotics ML paper for CoRL 2026 (deadline May 29, 2026). The paper proposes using OOD detection on World Action Model (WAM) action latents for best-of-N candidate selection at inference time, without any WAM fine-tuning. I need to find competitive or overlapping work that the authors may have missed.\n\nSearch for:\n1. \"world action model\" inference planning candidate selection 2025 2026 arxiv\n2. \"best-of-N\" robot policy world model latent 2026 arxiv\n3. WAM world model action latent OOD planning 2026\n4. UWM \"unified world model\" inference planning candidate selection 2026\n5. \"frozen\" world model robot planning test-time 2026 arxiv\n6. site:arxiv.org world action model inference 2026\n7. \"action latent\" \"success\" robot policy distribution 2026\n\nAlso:\n- Search for WAV (World-Value-Action Model, arXiv 2604.14732) to verify it exists and what it actually does\n- Search for Fast-WAM (arXiv 2603.16666) - does it really achieve 97.6% LIBERO without test-time video?\n- Search: \"latent value function\" robot manipulation frozen policy 2025 2026\n\nReport each paper found, what it actually does, and whether it overlaps with the proposed method (LOC = KNN/GMM density on success latents, Value MLP on action latents, both leaving WAM frozen)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c834a37-cf39-47ed-98a1-bbaef32c67ee",
  "isSidechain": false,
  "requestId": "req_011CatbxS84KJPpAq7r85PQM",
  "type": "assistant",
  "uuid": "15b77cec-5725-4f19-bb49-4286a757ca8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011aZfB9xc7czT69ufkHp3he",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25573,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1962,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1962,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 25573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25573
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

_source line 13 · 2026-05-10T08:53:30.323Z_

<details><summary>↩ Tool result · `toolu_01AJgYeS6X2b1LBH8aP8pmQm`</summary>

```text
Perfect. Now I have comprehensive information. Let me compile my findings:

## Verification Report

### Paper 1: FAIL-Detect (arXiv 2503.08558)

**Status: CONFIRMED - Paper exists and matches the description**

**Actual Title:** "Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies"

**Publication:** RSS 2025 (Robotics: Science and Systems, Los Angeles, June 2025)

**Verified Claims:**
- ✓ The paper **does prove that OOD detection on success-only demonstration data reliably detects policy failures**
- ✓ It **uses flow-based density estimation** - specifically a "novel flow-based density estimator" (logpZO score)
- ✓ It **employs conformal prediction** as "a versatile framework for uncertainty quantification with statistical guarantees"
- ✓ The method frames failure detection as sequential out-of-distribution (OOD) detection
- ✓ It distills policy inputs and outputs into scalar signals that correlate with policy failures and capture epistemic uncertainty

The claims in your source paper are **accurate and well-supported** by this work.

---

### Paper 2: EVA (arXiv 2603.17808)

**Status: CONFIRMED - Paper exists and matches the description**

**Actual Title:** "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards"

**Publication Date:** March 24, 2026 (very recent)

**Verified Claims:**
- ✓ The paper **does identify and address an "executability gap"**
- ✓ It **confirms that visually coherent world model rollouts can violate kinematic constraints**, producing "unstable or infeasible control commands when decoded by an IDM" 
- ✓ The core contribution is **Executable Video Alignment (EVA)**, an RL post-training framework
- ✓ The method repurposes an inverse dynamics model as a reward signal that penalizes actions violating embodiment constraints

The claims in your source paper are **accurate**.

---

### Search 3: Latent OOD Detection for Robot Candidate Selection

**Status: PRIOR WORK EXISTS - Relevant prior research found**

While searching for prior work on "latent OOD detection robot candidate selection," I found:

**Directly Relevant Prior Work:**

1. **UNISafe: Uncertainty-aware Latent Safety Filters** (arXiv 2505.00779, May 2025)
   - Uses **OOD detection on latent representations** for robot action filtering
   - Performs reachability analysis in an "augmented state space spanning both the latent representation and epistemic uncertainty"
   - Uses **conformal prediction** to calibrate uncertainty thresholds for OOD detection
   - Steers robots away from both known and unseen failures using latent-space uncertainty
   - Published in May 2025 (contemporaneous or slightly after FAIL-Detect)

2. **FIPER: Failure Prediction at Runtime** (arXiv 2510.09459, October 2025)
   - Framework for failure prediction for generative imitation learning policies
   - Identifies out-of-distribution observations and high uncertainty in generated actions
   - Calibrates failure scores using conformal prediction

3. **General trend of conformal prediction + robot action filtering** (2023-2025)
   - Safe Planning in Dynamic Environments using Conformal Prediction
   - Learning Robot Safety from Sparse Human Feedback using Conformal Prediction (2025)
   - Safe Probabilistic Planning using Conformal Risk Control (2026)

**Critical Observation:** UNISafe (2505.00779) is contemporaneous with or potentially slightly post-dating FAIL-Detect (2503.08558). If your source paper is claiming novelty in using OOD detection on latent representations for candidate selection with conformal prediction, this could represent a **potential novelty challenge**, as UNISafe appears to do something very similar (OOD detection in latent space using conformal prediction for safety-critical action filtering).

---

## Summary

| Paper | Exists? | Claims Match? | Status |
|-------|---------|---------------|--------|
| FAIL-Detect (2503.08558) | Yes | Yes, all verified | ✓ Valid |
| EVA (2603.17808) | Yes | Yes, all verified | ✓ Valid |
| Latent OOD for candidate selection | Yes | Partially - UNISafe overlaps | ⚠ Check novelty |

**Sources:**
- [FAIL-Detect on arXiv](https://arxiv.org/abs/2503.08558)
- [FAIL-Detect at RSS 2025](https://www.roboticsproceedings.org/rss21/p073.html)
- [EVA on arXiv](https://arxiv.org/abs/2603.17808)
- [EVA Project Page](https://eva-project-page.github.io/)
- [UNISafe: Uncertainty-aware Latent Safety Filters](https://arxiv.org/abs/2505.00779)
- [UNISafe GitHub/Project Page](https://cmu-intentlab.github.io/UNISafe/)
- [FIPER: Failure Prediction at Runtime](https://arxiv.org/abs/2510.09459)
- [Safe Probabilistic Planning with Conformal Risk Control](https://arxiv.org/html/2603.10392v1)
- [Learning Robot Safety with Conformal Prediction](https://arxiv.org/abs/2501.04823)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d4db72d-b2cb-495b-b027-6f914aaa7813",
  "isSidechain": false,
  "promptId": "7cfc2bf9-4784-4738-bc7e-6ecf5c05863c",
  "type": "user",
  "uuid": "5ba29ce9-0f96-458a-8d29-300c4f9526c6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify two specific papers cited in a robotics ML paper:\n\n1. FAIL-Detect (arXiv 2503.08558): Supposedly \"Failure Detection as OOD Detection for Robot Manipulation\" published at RSS 2025. The paper is claimed to \"prove that OOD detection on success-only demonstration data reliably detects policy failures\" using flow-based density estimation and conformal prediction. Search: \n- site:arxiv.org 2503.08558\n- \"FAIL-Detect\" failure detection OOD detection robot manipulation RSS 2025\n- OOD detection robot failure detection conformal prediction success demonstrations 2025\n\n2. EVA (arXiv 2603.17808): Supposedly \"Aligning Video World Models with Executability\" from 2026. Claims to demonstrate an \"executability gap\" showing visually coherent world model rollouts can violate kinematic constraints.\n- site:arxiv.org 2603.17808\n- EVA executability gap video world models robot 2026\n- \"executability gap\" video world model kinematic constraints\n\nFor each paper, report: Does it actually exist? What does it actually claim? Does it support the uses described above?\n\nAlso search for: \"latent OOD detection robot candidate selection\" to find any prior work on using OOD detection on latent action representations for candidate selection (which would challenge novelty).",
    "agentId": "a089fe7481faf65b4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have comprehensive information. Let me compile my findings:\n\n## Verification Report\n\n### Paper 1: FAIL-Detect (arXiv 2503.08558)\n\n**Status: CONFIRMED - Paper exists and matches the description**\n\n**Actual Title:** \"Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies\"\n\n**Publication:** RSS 2025 (Robotics: Science and Systems, Los Angeles, June 2025)\n\n**Verified Claims:**\n- ✓ The paper **does prove that OOD detection on success-only demonstration data reliably detects policy failures**\n- ✓ It **uses flow-based density estimation** - specifically a \"novel flow-based density estimator\" (logpZO score)\n- ✓ It **employs conformal prediction** as \"a versatile framework for uncertainty quantification with statistical guarantees\"\n- ✓ The method frames failure detection as sequential out-of-distribution (OOD) detection\n- ✓ It distills policy inputs and outputs into scalar signals that correlate with policy failures and capture epistemic uncertainty\n\nThe claims in your source paper are **accurate and well-supported** by this work.\n\n---\n\n### Paper 2: EVA (arXiv 2603.17808)\n\n**Status: CONFIRMED - Paper exists and matches the description**\n\n**Actual Title:** \"EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards\"\n\n**Publication Date:** March 24, 2026 (very recent)\n\n**Verified Claims:**\n- ✓ The paper **does identify and address an \"executability gap\"**\n- ✓ It **confirms that visually coherent world model rollouts can violate kinematic constraints**, producing \"unstable or infeasible control commands when decoded by an IDM\" \n- ✓ The core contribution is **Executable Video Alignment (EVA)**, an RL post-training framework\n- ✓ The method repurposes an inverse dynamics model as a reward signal that penalizes actions violating embodiment constraints\n\nThe claims in your source paper are **accurate**.\n\n---\n\n### Search 3: Latent OOD Detection for Robot Candidate Selection\n\n**Status: PRIOR WORK EXISTS - Relevant prior research found**\n\nWhile searching for prior work on \"latent OOD detection robot candidate selection,\" I found:\n\n**Directly Relevant Prior Work:**\n\n1. **UNISafe: Uncertainty-aware Latent Safety Filters** (arXiv 2505.00779, May 2025)\n   - Uses **OOD detection on latent representations** for robot action filtering\n   - Performs reachability analysis in an \"augmented state space spanning both the latent representation and epistemic uncertainty\"\n   - Uses **conformal prediction** to calibrate uncertainty thresholds for OOD detection\n   - Steers robots away from both known and unseen failures using latent-space uncertainty\n   - Published in May 2025 (contemporaneous or slightly after FAIL-Detect)\n\n2. **FIPER: Failure Prediction at Runtime** (arXiv 2510.09459, October 2025)\n   - Framework for failure prediction for generative imitation learning policies\n   - Identifies out-of-distribution observations and high uncertainty in generated actions\n   - Calibrates failure scores using conformal prediction\n\n3. **General trend of conformal prediction + robot action filtering** (2023-2025)\n   - Safe Planning in Dynamic Environments using Conformal Prediction\n   - Learning Robot Safety from Sparse Human Feedback using Conformal Prediction (2025)\n   - Safe Probabilistic Planning using Conformal Risk Control (2026)\n\n**Critical Observation:** UNISafe (2505.00779) is contemporaneous with or potentially slightly post-dating FAIL-Detect (2503.08558). If your source paper is claiming novelty in using OOD detection on latent representations for candidate selection with conformal prediction, this could represent a **potential novelty challenge**, as UNISafe appears to do something very similar (OOD detection in latent space using conformal prediction for safety-critical action filtering).\n\n---\n\n## Summary\n\n| Paper | Exists? | Claims Match? | Status |\n|-------|---------|---------------|--------|\n| FAIL-Detect (2503.08558) | Yes | Yes, all verified | ✓ Valid |\n| EVA (2603.17808) | Yes | Yes, all verified | ✓ Valid |\n| Latent OOD for candidate selection | Yes | Partially - UNISafe overlaps | ⚠ Check novelty |\n\n**Sources:**\n- [FAIL-Detect on arXiv](https://arxiv.org/abs/2503.08558)\n- [FAIL-Detect at RSS 2025](https://www.roboticsproceedings.org/rss21/p073.html)\n- [EVA on arXiv](https://arxiv.org/abs/2603.17808)\n- [EVA Project Page](https://eva-project-page.github.io/)\n- [UNISafe: Uncertainty-aware Latent Safety Filters](https://arxiv.org/abs/2505.00779)\n- [UNISafe GitHub/Project Page](https://cmu-intentlab.github.io/UNISafe/)\n- [FIPER: Failure Prediction at Runtime](https://arxiv.org/abs/2510.09459)\n- [Safe Probabilistic Planning with Conformal Risk Control](https://arxiv.org/html/2603.10392v1)\n- [Learning Robot Safety with Conformal Prediction](https://arxiv.org/abs/2501.04823)"
      }
    ],
    "totalDurationMs": 79089,
    "totalTokens": 31720,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 28338,
      "output_tokens": 1353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 882,
          "output_tokens": 1353,
          "cache_read_input_tokens": 28338,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1147,
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
  "sourceToolAssistantUUID": "6d4db72d-b2cb-495b-b027-6f914aaa7813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T08:54:03.077Z_

<details><summary>↩ Tool result · `toolu_01F5syVZWrWhuRBf3xo9qRHZ`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile the complete report for you.

## Comprehensive Literature Review: Competitive and Overlapping Work

Based on systematic searches of recent arXiv submissions through May 2026, here is a detailed report of papers that overlap with or are competitive to your proposed method (OOD detection on frozen WAM action latents + value scoring for best-of-N candidate selection):

---

## **DIRECT OVERLAPS - Closest Methods**

### 1. **COSMOS Policy** (arXiv 2601.16163)
- **What it does**: Fine-tunes video foundation models for visuomotor control using "latent frame injection" - encodes actions, proprioceptive state, and future state values directly into the diffusion model's latent sequence. Uses best-of-N sampling: generates candidate actions, imagines resulting future states, ranks by predicted value, executes highest-value action.
- **Key overlap**: Best-of-N candidate selection with latent value scoring (expects cumulative rewards). Generates multiple candidate trajectories and ranks them.
- **Difference**: Requires fine-tuning the video model; not test-time only on frozen base model.
- **Performance**: Achieves 98.5% LIBERO, 67.1% RoboCasa, SOTA on real bimanual manipulation.
- **CRITICAL FOR YOUR PAPER**: This is likely the strongest competitive baseline. It addresses the exact same problem (best-of-N action selection via value scoring) but with a different architecture (diffusion-based vs. WAM-based).

---

### 2. **Fast-WAM** (arXiv 2603.16666)
- **What it does**: World Action Model that keeps video co-training during training but SKIPS future prediction at test time (hence "fast"). Retains video latent context and only predicts actions directly at inference.
- **Specific claims about LIBERO**: Achieves "competitive results on LIBERO" without embodied pretraining; **real-time at 190ms latency (4x faster than imagine-then-execute WAMs)**. 
- **Important caveat**: The paper does NOT claim 97.6% on LIBERO without test-time video. Your reference may be conflating Fast-WAM with Cosmos Policy (98.5% LIBERO) or another method. Fast-WAM achieves competitive but unspecified LIBERO numbers.
- **Key difference from your method**: No explicit OOD detection on action latents; instead, it simply skips the video generation entirely at test time while still using the learned WAM representation.
- **Overlap relevance**: Uses frozen WAM representations but does not apply density/OOD scoring.

---

### 3. **GPC / Inference-Time Enhancement of Generative Robot Policies** (arXiv 2502.00622)
- **What it does**: Augments a frozen diffusion policy at deployment with an action-conditioned world model trained on demos and random rollouts. Performs lightweight online planning that **ranks and refines action proposals via model-based look-ahead** without retraining.
- **Key overlap**: Test-time candidate ranking using a separate world model predictor; keeps the base policy frozen.
- **Difference**: Uses diffusion policies as base, not WAM; world model is action-conditioned predictor (video prediction), not latent OOD scoring.
- **Publications**: IEEE RAL 2025; revised March 2026.

---

## **RELATED METHODS - World-Action Models with Latent/Value Components**

### 4. **World-Value-Action Model (WAV)** (arXiv 2604.14732)
- **What it does**: Unified framework learning structured latent representations of future trajectories with a world model predicting future states + trajectory value function evaluating long-horizon utility. Enables implicit planning by reshaping search distribution toward feasible regions in latent space.
- **Key overlap**: Uses value functions to evaluate trajectory quality; operates in latent space; implicit planning without explicit trajectory optimization.
- **Difference**: Does not address OOD detection; uses a different architecture (trajectory value function vs. MLP on action latents). Jointly trains all components, not test-time only.
- **Performance**: Outperforms SOTA in long-horizon and compositional tasks. Submitted April 16, 2026.

---

### 5. **DreamZero / World Action Models are Zero-shot Policies** (arXiv 2602.15922)
- **What it does**: WAM built on pretrained video diffusion, jointly models video and action via autoregressive DiT with flow matching. Learns from heterogeneous robot data without repetitive demonstrations.
- **Key overlap**: Uses world models with latent action representations; achieves strong generalization and OOD task performance through implicit latent learning.
- **Difference**: No explicit OOD detection or best-of-N selection; relies on pre-training on large diverse data rather than test-time scoring. Requires fine-tuning; not frozen WAM.
- **Performance**: >2x improvement in generalization vs. VLAs; 14B model runs at 7Hz. Submitted Feb 2026.

---

### 6. **MotuBrain: Advanced World Action Model for Robot Control** (arXiv 2604.27792)
- **What it does**: Uses three-stream Mixture-of-Transformers architecture for video generation, action modeling, and language conditioning. Freezes video latent and uses action-only suffix during inference (after initial joint denoising prefix).
- **Key overlap**: Keeps video frozen at inference; performs action-only denoising while attending to cached visual-language context. Multiple inference modes (direct policy vs. planning).
- **Difference**: No explicit OOD detection; focuses on architectural efficiency (frozen streams) rather than latent scoring.
- **Supports inference over 5 distributions**: vision-language-action policy, world modeling, video generation, inverse dynamics, video-action prediction.

---

### 7. **VLA-JEPA: Enhancing VLA with Latent World Model** (arXiv 2602.10098)
- **What it does**: Combines VLA with JEPA-style latent world model using leakage-free state prediction. Student only sees current observation; target encoder produces latent representations from future frames as supervision. Two-stage: JEPA pretraining + action-head fine-tuning.
- **Key overlap**: Learns action-relevant latent representations; predicts latent world dynamics without pixel leakage.
- **Difference**: Uses JEPA architecture for latent learning, not OOD detection; does not apply value scoring or best-of-N selection at inference.
- **Performance**: Consistent gains over baselines on LIBERO, LIBERO-Plus, SimplerEnv; strong OOD robustness. Published Feb 2026.

---

### 8. **Being-H0.7: Latent World-Action Model from Egocentric Videos** (arXiv 2605.00078)
- **What it does**: Latent world-action model that learns compact representations capturing dynamics and affordances without pixel reconstruction. Brings future-aware reasoning into VLA-style policies in latent space.
- **Key overlap**: Operates in learned latent action space; does not require generating future frames.
- **Difference**: No OOD detection; focuses on latent representation learning rather than test-time candidate selection.
- **Performance**: SOTA on 5 evaluation suites (reactive, physical, sequential, generalization) across 3 embodiments.

---

## **SUPPORTING METHODS - OOD Detection & Latent Value Functions**

### 9. **DreamDojo: Generalist Robot World Model** (arXiv 2602.06949)
- **What it does**: Foundation world model trained on 44,711 hours of egocentric human video. Uses **continuous latent actions extracted via spatiotemporal Transformer VAE** as hardware-agnostic control interface. VAE encoder takes 2 consecutive frames → 32-dim latent vector capturing critical motion.
- **Key overlap**: Uses VAE for latent action extraction; creates information bottleneck that disentangles action from visual context. Explicitly designed for strong OOD generalization to unseen objects and skills.
- **Difference**: Uses VAE as a generative model, not as a source for OOD detection scoring. Does not apply best-of-N selection.
- **Enablement**: Enables policy evaluation and model-based planning on frozen world models.
- **Status**: NVIDIA release; real-time at 10.81 FPS; stable for 60-second rollouts.

---

### 10. **LaST-R1: Robotic Manipulation via Adaptive Physical Latent Reasoning** (arXiv 2604.28192)
- **What it does**: Uses a 4-layer MLP value head to estimate state values, sharing backbone with VLA model. Injects value function estimations into latent token sequences.
- **Key overlap**: Latent value function for state evaluation; operates in frozen model's latent space.
- **Difference**: Value head shared with VLA backbone, not standalone OOD detector. Does not focus on best-of-N candidate selection.

---

### 11. **Uncertainty-Aware Robotic World Model (RWM-U)** (arXiv 2504.16680)
- **What it does**: Extends autoregressive world models with epistemic uncertainty estimation; combines with MOPO-PPO for offline RL-based policy optimization.
- **Key overlap**: Uses uncertainty (related to OOD confidence) in world models for policy improvement.
- **Difference**: Focuses on offline RL adaptation, not test-time best-of-N selection. Uncertainty used for policy learning, not candidate ranking.

---

### 12. **UNISafe: Uncertainty-aware Latent Safety Filters** (arXiv preprint)
- **What it does**: Detects OOD failures by calibrating uncertainty thresholds via conformal prediction. Trains anomaly predictors for failure detection and OOD detection scenarios.
- **Key overlap**: Principled OOD detection in latent space using uncertainty thresholding.
- **Difference**: Focuses on safety filtering (blocking bad actions), not ranking candidates. Different application context.

---

### 13. **Unified World Models (UWM)** (arXiv 2504.02792)
- **What it does**: Multimodal diffusion transformer using separate diffusion timesteps for actions and videos; learns policies, forward dynamics, inverse dynamics, and video prediction from robot and video data.
- **Key overlap**: Unified action-video modeling with flexible inference capabilities.
- **Difference**: Does not explicitly use latent OOD scoring; focuses on architectural unification rather than test-time candidate selection.

---

## **AUXILIARY SEARCH RESULTS - Distance Varying**

### 14. **WorldVLA: Towards Autoregressive Action World Model** (arXiv 2506.21539)
- Integrates VLA and world model in single framework; world model predicts future images; action model generates actions. **4% grasping improvement** over action-only model on LIBERO.
- Overlap: Action-world integration; action attention masking to prevent error accumulation in autoregressive generation.
- Difference: Joint training; no test-time OOD or value scoring.

### 15. **Unified 4D World Action Modeling (X-WAM)** (arXiv 2604.26694)
- Unifies real-time action execution with 4D world synthesis (video + 3D reconstruction).
- Addresses limitations of prior UWM (2D pixel-space only). Addresses action efficiency and world modeling quality balance.
- Overlap: Unified world modeling with action alignment.

### 16. **Latent-WAM: Latent World Action Modeling for Autonomous Driving** (arXiv 2603.24581)
- Domain: Autonomous driving (NOT manipulation, but relevant architecture).
- Uses Spatial-Aware Compressive World Encoder + Dynamic Latent World Model with causal Transformer for predicting future world status.
- Overlap: Latent WAM with structured latent representations.

### 17. **CKT-WAM: Parameter-Efficient Context Knowledge Transfer** (arXiv 2605.06247)
- Enables transfer between world action models with minimal parameters.
- Difference: Focuses on transfer learning, not test-time planning.

### 18. **OA-WAM: Object-Addressable World Action Model** (arXiv 2605.06481)
- Enables object-centric action planning in world models.
- Difference: Focuses on object-level grounding, not latent OOD detection.

### 19. **Hierarchical Latent Action Model (HiLAM)** (arXiv 2603.05815, ICLR 2026 workshop)
- Predicts next latent action using dynamic chunking; automatically detects skill boundaries in untrimmed sequences.
- Overlap: Latent action space with automatic structure discovery.
- Difference: Hierarchical structure detection, not OOD scoring.

### 20. **Latent Policy Steering (LPS)** (arXiv 2507.13340)
- Improves behavior-cloned policies via embodiment-agnostic pretrained world models.
- Achieves 10.6% average improvement on Robomimic; 70% relative improvement in real-world with few-shot embodiment demos.
- Overlap: Uses frozen pretrained world model for policy steering.

### 21. **Efficient Robotic Policy Learning via Latent Space Backward Planning (LBP)** (ICML 2025)
- Grounds task into final latent goals; recursively predicts intermediate subgoals.
- Overlap: Latent space planning without explicit pixel generation.
- Outperforms forward planning methods on LIBERO.

### 22. **Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation (LAC-WM)**
- Operates in unified latent action space shared across embodiments.
- Overlap: Shared latent action space improves generalization across embodiments.

### 23. **Do World Action Models Generalize Better than VLAs?** (arXiv 2603.22078)
- Robustness comparison between WAMs and VLAs.
- Relevant for positioning: WAMs demonstrate better OOD robustness than VLA-only approaches.

### 24. **LIBERO-Plus & LIBERO-PRO** (arXiv 2510.13626, 2510.03827)
- Systematic OOD evaluation of VLA/WAM models with controlled perturbations.
- Shows 90%+ standard LIBERO → 0% under LIBERO-PRO generalization.
- Relevant benchmark context.

---

## **CLAIMS VERIFICATION**

**Fast-WAM (2603.16666) - 97.6% LIBERO claim**: The paper does NOT claim 97.6% LIBERO success without test-time video. It claims "competitive results" with state-of-the-art, running at 190ms latency (4x faster). The 98.5% figure comes from **COSMOS Policy (2601.16163)**, which is the strongest baseline you should reference.

**WAV (2604.14732)**: Confirmed to exist and explicitly use trajectory value functions for implicit planning in latent space. This is highly relevant to your approach.

**Verification resources**:
- [arXiv World Action Model Survey](https://arxiv.org/abs/2605.00080) - comprehensive 2026 survey
- [World Model Reading List](https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9) - comprehensive reference

---

## **SUMMARY: NOVELTY AND GAPS FOR YOUR PAPER**

Your method's **novel contributions relative to competitive work**:

1. **Explicit OOD detection on action latents** via GMM/KNN density estimation - This is not explicitly used in Fast-WAM, DreamZero, or MotuBrain
2. **Value MLP trained separately on action latents** - COSMOS uses latent value injection but requires model fine-tuning; you keep WAM frozen
3. **Zero-parameter frozen WAM approach** - Both COSMOS and WAV require training new components; you leverage learned action latent geometry directly
4. **Comparison of density-based (GMM/KNN) vs. learned value scoring** - This ablation is missing from prior best-of-N work

**Primary competitive methods to cite**:
- COSMOS Policy (best-of-N with value, but fine-tuned)
- Fast-WAM (frozen WAM inference, but no value scoring)
- GPC (frozen policy + inference-time planning, but with diffusion not WAM)
- WAV (value-based latent planning, but jointly trained)

**Call-outs for your limitations to pre-empt**:
- You should compare against COSMOS Policy directly (the obvious 98%+ LIBERO baseline)
- Acknowledge that DreamDojo's VAE latent actions provide a competing latent action discovery method
- Cite LIBERO-Plus robustness concerns (90%→0% gap) as motivation for robustness of your OOD detection

Sources:
- [COSMOS Policy](https://arxiv.org/abs/2601.16163)
- [Fast-WAM](https://arxiv.org/abs/2603.16666)
- [GPC](https://arxiv.org/abs/2502.00622)
- [World-Value-Action Model](https://arxiv.org/abs/2604.14732)
- [DreamZero](https://arxiv.org/abs/2602.15922)
- [MotuBrain](https://arxiv.org/abs/2604.27792)
- [VLA-JEPA](https://arxiv.org/abs/2602.10098)
- [Being-H0.7](https://arxiv.org/abs/2605.00078)
- [DreamDojo](https://arxiv.org/abs/2602.06949)
- [WorldVLA](https://arxiv.org/abs/2506.21539)
- [UWM](https://arxiv.org/abs/2504.02792)
- [World Model Survey 2026](https://arxiv.org/abs/2605.00080)
- [LIBERO-Pro](https://arxiv.org/abs/2510.03827)
- [Demystifying Diffusion Policies OOD](https://arxiv.org/abs/2505.05787)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15b77cec-5725-4f19-bb49-4286a757ca8f",
  "isSidechain": false,
  "promptId": "7cfc2bf9-4784-4738-bc7e-6ecf5c05863c",
  "type": "user",
  "uuid": "8bf99018-4c40-45a4-a8ef-72266b79e01e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a robotics ML paper for CoRL 2026 (deadline May 29, 2026). The paper proposes using OOD detection on World Action Model (WAM) action latents for best-of-N candidate selection at inference time, without any WAM fine-tuning. I need to find competitive or overlapping work that the authors may have missed.\n\nSearch for:\n1. \"world action model\" inference planning candidate selection 2025 2026 arxiv\n2. \"best-of-N\" robot policy world model latent 2026 arxiv\n3. WAM world model action latent OOD planning 2026\n4. UWM \"unified world model\" inference planning candidate selection 2026\n5. \"frozen\" world model robot planning test-time 2026 arxiv\n6. site:arxiv.org world action model inference 2026\n7. \"action latent\" \"success\" robot policy distribution 2026\n\nAlso:\n- Search for WAV (World-Value-Action Model, arXiv 2604.14732) to verify it exists and what it actually does\n- Search for Fast-WAM (arXiv 2603.16666) - does it really achieve 97.6% LIBERO without test-time video?\n- Search: \"latent value function\" robot manipulation frozen policy 2025 2026\n\nReport each paper found, what it actually does, and whether it overlaps with the proposed method (LOC = KNN/GMM density on success latents, Value MLP on action latents, both leaving WAM frozen).",
    "agentId": "a5f5de676eff56e8d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile the complete report for you.\n\n## Comprehensive Literature Review: Competitive and Overlapping Work\n\nBased on systematic searches of recent arXiv submissions through May 2026, here is a detailed report of papers that overlap with or are competitive to your proposed method (OOD detection on frozen WAM action latents + value scoring for best-of-N candidate selection):\n\n---\n\n## **DIRECT OVERLAPS - Closest Methods**\n\n### 1. **COSMOS Policy** (arXiv 2601.16163)\n- **What it does**: Fine-tunes video foundation models for visuomotor control using \"latent frame injection\" - encodes actions, proprioceptive state, and future state values directly into the diffusion model's latent sequence. Uses best-of-N sampling: generates candidate actions, imagines resulting future states, ranks by predicted value, executes highest-value action.\n- **Key overlap**: Best-of-N candidate selection with latent value scoring (expects cumulative rewards). Generates multiple candidate trajectories and ranks them.\n- **Difference**: Requires fine-tuning the video model; not test-time only on frozen base model.\n- **Performance**: Achieves 98.5% LIBERO, 67.1% RoboCasa, SOTA on real bimanual manipulation.\n- **CRITICAL FOR YOUR PAPER**: This is likely the strongest competitive baseline. It addresses the exact same problem (best-of-N action selection via value scoring) but with a different architecture (diffusion-based vs. WAM-based).\n\n---\n\n### 2. **Fast-WAM** (arXiv 2603.16666)\n- **What it does**: World Action Model that keeps video co-training during training but SKIPS future prediction at test time (hence \"fast\"). Retains video latent context and only predicts actions directly at inference.\n- **Specific claims about LIBERO**: Achieves \"competitive results on LIBERO\" without embodied pretraining; **real-time at 190ms latency (4x faster than imagine-then-execute WAMs)**. \n- **Important caveat**: The paper does NOT claim 97.6% on LIBERO without test-time video. Your reference may be conflating Fast-WAM with Cosmos Policy (98.5% LIBERO) or another method. Fast-WAM achieves competitive but unspecified LIBERO numbers.\n- **Key difference from your method**: No explicit OOD detection on action latents; instead, it simply skips the video generation entirely at test time while still using the learned WAM representation.\n- **Overlap relevance**: Uses frozen WAM representations but does not apply density/OOD scoring.\n\n---\n\n### 3. **GPC / Inference-Time Enhancement of Generative Robot Policies** (arXiv 2502.00622)\n- **What it does**: Augments a frozen diffusion policy at deployment with an action-conditioned world model trained on demos and random rollouts. Performs lightweight online planning that **ranks and refines action proposals via model-based look-ahead** without retraining.\n- **Key overlap**: Test-time candidate ranking using a separate world model predictor; keeps the base policy frozen.\n- **Difference**: Uses diffusion policies as base, not WAM; world model is action-conditioned predictor (video prediction), not latent OOD scoring.\n- **Publications**: IEEE RAL 2025; revised March 2026.\n\n---\n\n## **RELATED METHODS - World-Action Models with Latent/Value Components**\n\n### 4. **World-Value-Action Model (WAV)** (arXiv 2604.14732)\n- **What it does**: Unified framework learning structured latent representations of future trajectories with a world model predicting future states + trajectory value function evaluating long-horizon utility. Enables implicit planning by reshaping search distribution toward feasible regions in latent space.\n- **Key overlap**: Uses value functions to evaluate trajectory quality; operates in latent space; implicit planning without explicit trajectory optimization.\n- **Difference**: Does not address OOD detection; uses a different architecture (trajectory value function vs. MLP on action latents). Jointly trains all components, not test-time only.\n- **Performance**: Outperforms SOTA in long-horizon and compositional tasks. Submitted April 16, 2026.\n\n---\n\n### 5. **DreamZero / World Action Models are Zero-shot Policies** (arXiv 2602.15922)\n- **What it does**: WAM built on pretrained video diffusion, jointly models video and action via autoregressive DiT with flow matching. Learns from heterogeneous robot data without repetitive demonstrations.\n- **Key overlap**: Uses world models with latent action representations; achieves strong generalization and OOD task performance through implicit latent learning.\n- **Difference**: No explicit OOD detection or best-of-N selection; relies on pre-training on large diverse data rather than test-time scoring. Requires fine-tuning; not frozen WAM.\n- **Performance**: >2x improvement in generalization vs. VLAs; 14B model runs at 7Hz. Submitted Feb 2026.\n\n---\n\n### 6. **MotuBrain: Advanced World Action Model for Robot Control** (arXiv 2604.27792)\n- **What it does**: Uses three-stream Mixture-of-Transformers architecture for video generation, action modeling, and language conditioning. Freezes video latent and uses action-only suffix during inference (after initial joint denoising prefix).\n- **Key overlap**: Keeps video frozen at inference; performs action-only denoising while attending to cached visual-language context. Multiple inference modes (direct policy vs. planning).\n- **Difference**: No explicit OOD detection; focuses on architectural efficiency (frozen streams) rather than latent scoring.\n- **Supports inference over 5 distributions**: vision-language-action policy, world modeling, video generation, inverse dynamics, video-action prediction.\n\n---\n\n### 7. **VLA-JEPA: Enhancing VLA with Latent World Model** (arXiv 2602.10098)\n- **What it does**: Combines VLA with JEPA-style latent world model using leakage-free state prediction. Student only sees current observation; target encoder produces latent representations from future frames as supervision. Two-stage: JEPA pretraining + action-head fine-tuning.\n- **Key overlap**: Learns action-relevant latent representations; predicts latent world dynamics without pixel leakage.\n- **Difference**: Uses JEPA architecture for latent learning, not OOD detection; does not apply value scoring or best-of-N selection at inference.\n- **Performance**: Consistent gains over baselines on LIBERO, LIBERO-Plus, SimplerEnv; strong OOD robustness. Published Feb 2026.\n\n---\n\n### 8. **Being-H0.7: Latent World-Action Model from Egocentric Videos** (arXiv 2605.00078)\n- **What it does**: Latent world-action model that learns compact representations capturing dynamics and affordances without pixel reconstruction. Brings future-aware reasoning into VLA-style policies in latent space.\n- **Key overlap**: Operates in learned latent action space; does not require generating future frames.\n- **Difference**: No OOD detection; focuses on latent representation learning rather than test-time candidate selection.\n- **Performance**: SOTA on 5 evaluation suites (reactive, physical, sequential, generalization) across 3 embodiments.\n\n---\n\n## **SUPPORTING METHODS - OOD Detection & Latent Value Functions**\n\n### 9. **DreamDojo: Generalist Robot World Model** (arXiv 2602.06949)\n- **What it does**: Foundation world model trained on 44,711 hours of egocentric human video. Uses **continuous latent actions extracted via spatiotemporal Transformer VAE** as hardware-agnostic control interface. VAE encoder takes 2 consecutive frames → 32-dim latent vector capturing critical motion.\n- **Key overlap**: Uses VAE for latent action extraction; creates information bottleneck that disentangles action from visual context. Explicitly designed for strong OOD generalization to unseen objects and skills.\n- **Difference**: Uses VAE as a generative model, not as a source for OOD detection scoring. Does not apply best-of-N selection.\n- **Enablement**: Enables policy evaluation and model-based planning on frozen world models.\n- **Status**: NVIDIA release; real-time at 10.81 FPS; stable for 60-second rollouts.\n\n---\n\n### 10. **LaST-R1: Robotic Manipulation via Adaptive Physical Latent Reasoning** (arXiv 2604.28192)\n- **What it does**: Uses a 4-layer MLP value head to estimate state values, sharing backbone with VLA model. Injects value function estimations into latent token sequences.\n- **Key overlap**: Latent value function for state evaluation; operates in frozen model's latent space.\n- **Difference**: Value head shared with VLA backbone, not standalone OOD detector. Does not focus on best-of-N candidate selection.\n\n---\n\n### 11. **Uncertainty-Aware Robotic World Model (RWM-U)** (arXiv 2504.16680)\n- **What it does**: Extends autoregressive world models with epistemic uncertainty estimation; combines with MOPO-PPO for offline RL-based policy optimization.\n- **Key overlap**: Uses uncertainty (related to OOD confidence) in world models for policy improvement.\n- **Difference**: Focuses on offline RL adaptation, not test-time best-of-N selection. Uncertainty used for policy learning, not candidate ranking.\n\n---\n\n### 12. **UNISafe: Uncertainty-aware Latent Safety Filters** (arXiv preprint)\n- **What it does**: Detects OOD failures by calibrating uncertainty thresholds via conformal prediction. Trains anomaly predictors for failure detection and OOD detection scenarios.\n- **Key overlap**: Principled OOD detection in latent space using uncertainty thresholding.\n- **Difference**: Focuses on safety filtering (blocking bad actions), not ranking candidates. Different application context.\n\n---\n\n### 13. **Unified World Models (UWM)** (arXiv 2504.02792)\n- **What it does**: Multimodal diffusion transformer using separate diffusion timesteps for actions and videos; learns policies, forward dynamics, inverse dynamics, and video prediction from robot and video data.\n- **Key overlap**: Unified action-video modeling with flexible inference capabilities.\n- **Difference**: Does not explicitly use latent OOD scoring; focuses on architectural unification rather than test-time candidate selection.\n\n---\n\n## **AUXILIARY SEARCH RESULTS - Distance Varying**\n\n### 14. **WorldVLA: Towards Autoregressive Action World Model** (arXiv 2506.21539)\n- Integrates VLA and world model in single framework; world model predicts future images; action model generates actions. **4% grasping improvement** over action-only model on LIBERO.\n- Overlap: Action-world integration; action attention masking to prevent error accumulation in autoregressive generation.\n- Difference: Joint training; no test-time OOD or value scoring.\n\n### 15. **Unified 4D World Action Modeling (X-WAM)** (arXiv 2604.26694)\n- Unifies real-time action execution with 4D world synthesis (video + 3D reconstruction).\n- Addresses limitations of prior UWM (2D pixel-space only). Addresses action efficiency and world modeling quality balance.\n- Overlap: Unified world modeling with action alignment.\n\n### 16. **Latent-WAM: Latent World Action Modeling for Autonomous Driving** (arXiv 2603.24581)\n- Domain: Autonomous driving (NOT manipulation, but relevant architecture).\n- Uses Spatial-Aware Compressive World Encoder + Dynamic Latent World Model with causal Transformer for predicting future world status.\n- Overlap: Latent WAM with structured latent representations.\n\n### 17. **CKT-WAM: Parameter-Efficient Context Knowledge Transfer** (arXiv 2605.06247)\n- Enables transfer between world action models with minimal parameters.\n- Difference: Focuses on transfer learning, not test-time planning.\n\n### 18. **OA-WAM: Object-Addressable World Action Model** (arXiv 2605.06481)\n- Enables object-centric action planning in world models.\n- Difference: Focuses on object-level grounding, not latent OOD detection.\n\n### 19. **Hierarchical Latent Action Model (HiLAM)** (arXiv 2603.05815, ICLR 2026 workshop)\n- Predicts next latent action using dynamic chunking; automatically detects skill boundaries in untrimmed sequences.\n- Overlap: Latent action space with automatic structure discovery.\n- Difference: Hierarchical structure detection, not OOD scoring.\n\n### 20. **Latent Policy Steering (LPS)** (arXiv 2507.13340)\n- Improves behavior-cloned policies via embodiment-agnostic pretrained world models.\n- Achieves 10.6% average improvement on Robomimic; 70% relative improvement in real-world with few-shot embodiment demos.\n- Overlap: Uses frozen pretrained world model for policy steering.\n\n### 21. **Efficient Robotic Policy Learning via Latent Space Backward Planning (LBP)** (ICML 2025)\n- Grounds task into final latent goals; recursively predicts intermediate subgoals.\n- Overlap: Latent space planning without explicit pixel generation.\n- Outperforms forward planning methods on LIBERO.\n\n### 22. **Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation (LAC-WM)**\n- Operates in unified latent action space shared across embodiments.\n- Overlap: Shared latent action space improves generalization across embodiments.\n\n### 23. **Do World Action Models Generalize Better than VLAs?** (arXiv 2603.22078)\n- Robustness comparison between WAMs and VLAs.\n- Relevant for positioning: WAMs demonstrate better OOD robustness than VLA-only approaches.\n\n### 24. **LIBERO-Plus & LIBERO-PRO** (arXiv 2510.13626, 2510.03827)\n- Systematic OOD evaluation of VLA/WAM models with controlled perturbations.\n- Shows 90%+ standard LIBERO → 0% under LIBERO-PRO generalization.\n- Relevant benchmark context.\n\n---\n\n## **CLAIMS VERIFICATION**\n\n**Fast-WAM (2603.16666) - 97.6% LIBERO claim**: The paper does NOT claim 97.6% LIBERO success without test-time video. It claims \"competitive results\" with state-of-the-art, running at 190ms latency (4x faster). The 98.5% figure comes from **COSMOS Policy (2601.16163)**, which is the strongest baseline you should reference.\n\n**WAV (2604.14732)**: Confirmed to exist and explicitly use trajectory value functions for implicit planning in latent space. This is highly relevant to your approach.\n\n**Verification resources**:\n- [arXiv World Action Model Survey](https://arxiv.org/abs/2605.00080) - comprehensive 2026 survey\n- [World Model Reading List](https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9) - comprehensive reference\n\n---\n\n## **SUMMARY: NOVELTY AND GAPS FOR YOUR PAPER**\n\nYour method's **novel contributions relative to competitive work**:\n\n1. **Explicit OOD detection on action latents** via GMM/KNN density estimation - This is not explicitly used in Fast-WAM, DreamZero, or MotuBrain\n2. **Value MLP trained separately on action latents** - COSMOS uses latent value injection but requires model fine-tuning; you keep WAM frozen\n3. **Zero-parameter frozen WAM approach** - Both COSMOS and WAV require training new components; you leverage learned action latent geometry directly\n4. **Comparison of density-based (GMM/KNN) vs. learned value scoring** - This ablation is missing from prior best-of-N work\n\n**Primary competitive methods to cite**:\n- COSMOS Policy (best-of-N with value, but fine-tuned)\n- Fast-WAM (frozen WAM inference, but no value scoring)\n- GPC (frozen policy + inference-time planning, but with diffusion not WAM)\n- WAV (value-based latent planning, but jointly trained)\n\n**Call-outs for your limitations to pre-empt**:\n- You should compare against COSMOS Policy directly (the obvious 98%+ LIBERO baseline)\n- Acknowledge that DreamDojo's VAE latent actions provide a competing latent action discovery method\n- Cite LIBERO-Plus robustness concerns (90%→0% gap) as motivation for robustness of your OOD detection\n\nSources:\n- [COSMOS Policy](https://arxiv.org/abs/2601.16163)\n- [Fast-WAM](https://arxiv.org/abs/2603.16666)\n- [GPC](https://arxiv.org/abs/2502.00622)\n- [World-Value-Action Model](https://arxiv.org/abs/2604.14732)\n- [DreamZero](https://arxiv.org/abs/2602.15922)\n- [MotuBrain](https://arxiv.org/abs/2604.27792)\n- [VLA-JEPA](https://arxiv.org/abs/2602.10098)\n- [Being-H0.7](https://arxiv.org/abs/2605.00078)\n- [DreamDojo](https://arxiv.org/abs/2602.06949)\n- [WorldVLA](https://arxiv.org/abs/2506.21539)\n- [UWM](https://arxiv.org/abs/2504.02792)\n- [World Model Survey 2026](https://arxiv.org/abs/2605.00080)\n- [LIBERO-Pro](https://arxiv.org/abs/2510.03827)\n- [Demystifying Diffusion Policies OOD](https://arxiv.org/abs/2505.05787)"
      }
    ],
    "totalDurationMs": 97889,
    "totalTokens": 41631,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3024,
      "cache_read_input_tokens": 34167,
      "output_tokens": 4433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3024
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 4433,
          "cache_read_input_tokens": 34167,
          "cache_creation_input_tokens": 3024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3024,
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
  "sourceToolAssistantUUID": "15b77cec-5725-4f19-bb49-4286a757ca8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8bf99018-4c40-45a4-a8ef-72266b79e01e",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent candidate selection via OOD and value functions",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Tool result

_source line 17 · 2026-05-10T08:54:48.300Z_

<details><summary>↩ Tool result · `toolu_01SjK7UJqWUKVJB15gEJXzru`</summary>

```text
Perfect. Now let me compile a comprehensive report based on all the searches.

## Comprehensive Search Report: OOD Detection and Density Estimation for Robot Action Selection

I've completed a thorough search for papers using OOD detection or density estimation on policy latents for candidate selection/action filtering in robot manipulation. Here's what I found:

---

### Query 1: "OOD detection" "action latent" robot manipulation candidate selection 2025 2026 arxiv

**Findings:**
- **Latent Theory of Mind** (2025): Addresses OOD changes in multi-robot cooperative manipulation with directional consensus mechanisms
- **Latent Policy Barrier** (NeurIPS 2025): "Learning Robust Visuomotor Policies by Staying In-Distribution" 
- Multiple papers on VLAs struggling with OOD generalization but none specifically using density estimation on success latents

---

### Query 2: "density estimation" "action latent" robot policy candidate selection best-of-N

**HIGHLY RELEVANT FINDING - KDPE:**

**[KDPE: Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection](https://arxiv.org/abs/2508.10511)** (2025, CoRL)
- Uses Kernel Density Estimation to filter diffusion policy trajectories
- **Key difference from LOC**: Operates in **action space** (end-effector position, orientation, gripper state), NOT latent space
- Fits KDE on ALL training actions (not just successful ones)
- Selects trajectory with highest density in action space
- Demonstrates this can be effective for filtering trajectories

**[KDE-based Probabilistic Modeling (KDE-PM)](https://arxiv.org/html/2505.13255)** in robotic foundation models:
- Calculates action probability distributions using KDE for diffusion policies
- Also works in explicit action space, not latent

---

### Query 3: "success distribution" latent space robot policy filtering 2025 2026

**Findings:**
- **Latent Space Backward Planning (LBP)** (ICML 2025): Plans through latent space but doesn't score actions by success distribution
- **Ctrl-World** (2025): Synthesizes successful trajectories in imagination space for policy improvement, but doesn't score candidates
- No papers found that explicitly fit density models on successful demonstration latents

---

### Query 4: "conformal prediction" robot action selection manipulation 2025 2026 arxiv

**Findings:**
- **Safe Probabilistic Planning with Conformal Risk Control** (March 2026): Uses conformal prediction for safety but not for action scoring
- **Learning Robot Safety from Sparse Human Feedback** (January 2025): Conformal prediction for identifying unsafe regions, not for scoring candidates
- **Learnable Conformal Prediction** (September 2025): For uncertainty quantification but in different context
- None use conformal prediction for scoring action candidates from policy latents

---

### Query 5: "KNN" OR "GMM" robot policy latent quality scoring candidate selection

**No direct matches found**, but related work:
- Papers discussing Gaussian Mixture Models for learning distributions of demonstrations
- KNN mentioned in broader context of nearest-neighbor retrieval but not for scoring policy latent candidates

---

### Query 6: site:arxiv.org "latent OOD" robot manipulation action selection

**RELEVANT FINDING:**

**[Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives](https://arxiv.org/abs/2505.05787)** (May 2025)
- Proposes ALT (Action Lookup Table) policy using contrastive learning
- **OOD Detection mechanism**: Simple threshold on cosine similarity in latent space
- If max similarity < threshold γ, flags as OOD
- **Key difference from LOC**: Uses hard threshold, not a density model; finds nearest neighbor with cosine similarity, not KNN/GMM
- Performs nearest neighbor lookup in contrastive latent space

---

### Query 7: "test-time compute" robot manipulation "OOD" OR "out-of-distribution" latent 2025 2026

**HIGHLY RELEVANT FINDINGS:**

**[Verifier-free Test-Time Sampling for Vision Language Action Models (MG-Select)](https://arxiv.org/abs/2510.05681)** (October 2025, ICLR 2026)
- **Scoring mechanism**: KL divergence from reference action distribution
- Reference distribution: obtained by masking states/language conditions (maximum uncertainty)
- Selects actions with **highest** KL divergence
- Best-of-N sampling without external verifier
- **Critical difference from LOC**: Uses KL divergence from uncertainty-aware masked distribution, NOT density estimation on success latents
- No fitting to demonstration data; uses model's own masked predictions as reference

**[RoVer: Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)** (October 2025)
- Uses learned Process Reward Model (PRM) to score candidates
- Scores are scalar process rewards (not density-based)
- Generates multiple candidates, expands along PRM-predicted directions, selects best
- Different paradigm: trained reward model vs. density estimation on latents

---

### Query 8: "MG-Select" robot VLA test-time sampling arxiv 2510.05681

**Direct Answer to Your Question:**

**Does MG-Select use KL from masked distribution? Is it really different from LOC?**

✓ **Yes, MG-Select uses KL from masked distribution** (not density estimation)

**Key Mechanism:**
- Generates reference distribution by passing same VLA with randomly **masked states and language conditions** as inputs
- This forces maximum uncertainty while staying task-aligned
- Computes KL divergence between sampled actions and this reference distribution
- Selects actions with **highest** KL (most confident/different from uncertainty)
- **No fitting to demonstrations required** - uses model's own outputs

**How it differs from LOC:**
| Aspect | LOC | MG-Select |
|--------|-----|-----------|
| **Basis** | Fit density model (KNN/GMM) on success demo latents | KL divergence from masked reference distribution |
| **Training** | Requires fitting to successful trajectory data | Zero training, uses base VLA only |
| **Computation** | Distance/density in fitted model | KL divergence between distributions |
| **Mechanism** | "In-distribution according to success data" | "Confident/different from uncertainty" |

---

### Additional Test-Time Scaling Work Found:

**[RoboMonkey / Cortex 2.0](https://arxiv.org/html/2604.20246)** (2024):
- World model generates candidates in visual latent space
- Process-Reward Operator scores each for task progress and risk
- Different from density estimation approach

**[Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068v1)** (2025):
- Convex composition of distributional scores from multiple policies
- Theoretical framework for composition, not density-based selection

**[Steering Your Generalists (V-GPS)](https://arxiv.org/html/2410.13816v2)** (2024):
- Re-ranks actions using value function Q(s,a)
- Operates in explicit action space, not latent; learned via offline RL

---

## Summary: Does LOC Already Exist?

**No direct precedent found**, but closest approaches:

1. **KDPE** - Uses KDE for trajectory filtering, but in action space not latent space, and on all training actions not just successful ones

2. **MG-Select** - Performs best-of-N candidate selection in action latent space (for VLAs), but uses KL divergence from masked distribution, not density estimation on success demonstrations

3. **ALT Policy** - Uses NN lookup with threshold-based OOD detection in contrastive latent space, not density modeling

4. **RoVer** - Uses learned reward model to score candidates, not density estimation

**The core idea of your LOC approach** - fitting a density model (KNN/GMM) on **successful demonstration latents** and using it to score/select actions - **appears to be novel**. The closest work does density estimation in action space (KDPE) or uses other scoring mechanisms (MG-Select's KL, RoVer's rewards, V-GPS's Q-function), but none directly estimate density over success latents for candidate filtering in the way you describe.

---

## Sources:

- [Latent Theory of Mind](https://arxiv.org/html/2505.09144v1)
- [KDPE: Kernel Density Estimation Strategy](https://arxiv.org/abs/2508.10511)
- [Demystifying Diffusion Policies (ALT)](https://arxiv.org/abs/2505.05787)
- [Verifier-free Test-Time Sampling (MG-Select)](https://arxiv.org/abs/2510.05681)
- [RoVer: Robot Reward Model](https://arxiv.org/abs/2510.10975)
- [Steering Your Generalists (V-GPS)](https://arxiv.org/html/2410.13816v2)
- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068v1)
- [Efficient Robotic Policy Learning via LBP](https://arxiv.org/abs/2505.06861)
- [Ctrl-World Generative World Model](https://arxiv.org/html/2510.10125v1)
- [Safe Probabilistic Planning with Conformal Risk Control](https://arxiv.org/html/2603.10392v1)
- [Learning Robot Safety via Conformal Prediction](https://arxiv.org/html/2501.04823)
- [Latent Space Backward Planning](https://lbp-authors.github.io/)
- [Deep Generative Models in Robotics Survey](https://arxiv.org/html/2408.04380v1)
- [Continuous Latent Action Models (CLAM)](https://arxiv.org/abs/2505.04999)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c834a37-cf39-47ed-98a1-bbaef32c67ee",
  "isSidechain": false,
  "promptId": "7cfc2bf9-4784-4738-bc7e-6ecf5c05863c",
  "type": "user",
  "uuid": "173576d7-64e8-4890-b7ed-1f16fd39b08e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for papers that use OOD detection or density estimation on policy latents for candidate selection or action filtering in robot manipulation. I'm reviewing a paper that proposes \"Latent OOD Consistency Scoring (LOC)\" - fitting a KNN/GMM density estimator on success demonstration latents and using it to score/select candidate actions. I need to know if this already exists.\n\nSearch queries to run:\n1. \"OOD detection\" \"action latent\" robot manipulation candidate selection 2025 2026 arxiv\n2. \"density estimation\" \"action latent\" robot policy candidate selection best-of-N\n3. \"success distribution\" latent space robot policy filtering 2025 2026\n4. \"conformal prediction\" robot action selection manipulation 2025 2026 arxiv\n5. \"KNN\" OR \"GMM\" robot policy latent quality scoring candidate selection\n6. site:arxiv.org \"latent OOD\" robot manipulation action selection\n7. \"test-time compute\" robot manipulation \"OOD\" OR \"out-of-distribution\" latent 2025 2026\n\nAlso check: \n- Does MG-Select (arXiv 2510.05681) actually use KL from masked distribution? Is its mechanism really different from LOC?\n- Search: \"MG-Select\" robot VLA test-time sampling arxiv 2510.05681\n\nReport what you find about each query, especially any papers that do something similar to LOC (density estimation on success demo latents for candidate scoring).",
    "agentId": "afdf5ab2ac5485e75",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now let me compile a comprehensive report based on all the searches.\n\n## Comprehensive Search Report: OOD Detection and Density Estimation for Robot Action Selection\n\nI've completed a thorough search for papers using OOD detection or density estimation on policy latents for candidate selection/action filtering in robot manipulation. Here's what I found:\n\n---\n\n### Query 1: \"OOD detection\" \"action latent\" robot manipulation candidate selection 2025 2026 arxiv\n\n**Findings:**\n- **Latent Theory of Mind** (2025): Addresses OOD changes in multi-robot cooperative manipulation with directional consensus mechanisms\n- **Latent Policy Barrier** (NeurIPS 2025): \"Learning Robust Visuomotor Policies by Staying In-Distribution\" \n- Multiple papers on VLAs struggling with OOD generalization but none specifically using density estimation on success latents\n\n---\n\n### Query 2: \"density estimation\" \"action latent\" robot policy candidate selection best-of-N\n\n**HIGHLY RELEVANT FINDING - KDPE:**\n\n**[KDPE: Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection](https://arxiv.org/abs/2508.10511)** (2025, CoRL)\n- Uses Kernel Density Estimation to filter diffusion policy trajectories\n- **Key difference from LOC**: Operates in **action space** (end-effector position, orientation, gripper state), NOT latent space\n- Fits KDE on ALL training actions (not just successful ones)\n- Selects trajectory with highest density in action space\n- Demonstrates this can be effective for filtering trajectories\n\n**[KDE-based Probabilistic Modeling (KDE-PM)](https://arxiv.org/html/2505.13255)** in robotic foundation models:\n- Calculates action probability distributions using KDE for diffusion policies\n- Also works in explicit action space, not latent\n\n---\n\n### Query 3: \"success distribution\" latent space robot policy filtering 2025 2026\n\n**Findings:**\n- **Latent Space Backward Planning (LBP)** (ICML 2025): Plans through latent space but doesn't score actions by success distribution\n- **Ctrl-World** (2025): Synthesizes successful trajectories in imagination space for policy improvement, but doesn't score candidates\n- No papers found that explicitly fit density models on successful demonstration latents\n\n---\n\n### Query 4: \"conformal prediction\" robot action selection manipulation 2025 2026 arxiv\n\n**Findings:**\n- **Safe Probabilistic Planning with Conformal Risk Control** (March 2026): Uses conformal prediction for safety but not for action scoring\n- **Learning Robot Safety from Sparse Human Feedback** (January 2025): Conformal prediction for identifying unsafe regions, not for scoring candidates\n- **Learnable Conformal Prediction** (September 2025): For uncertainty quantification but in different context\n- None use conformal prediction for scoring action candidates from policy latents\n\n---\n\n### Query 5: \"KNN\" OR \"GMM\" robot policy latent quality scoring candidate selection\n\n**No direct matches found**, but related work:\n- Papers discussing Gaussian Mixture Models for learning distributions of demonstrations\n- KNN mentioned in broader context of nearest-neighbor retrieval but not for scoring policy latent candidates\n\n---\n\n### Query 6: site:arxiv.org \"latent OOD\" robot manipulation action selection\n\n**RELEVANT FINDING:**\n\n**[Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives](https://arxiv.org/abs/2505.05787)** (May 2025)\n- Proposes ALT (Action Lookup Table) policy using contrastive learning\n- **OOD Detection mechanism**: Simple threshold on cosine similarity in latent space\n- If max similarity < threshold γ, flags as OOD\n- **Key difference from LOC**: Uses hard threshold, not a density model; finds nearest neighbor with cosine similarity, not KNN/GMM\n- Performs nearest neighbor lookup in contrastive latent space\n\n---\n\n### Query 7: \"test-time compute\" robot manipulation \"OOD\" OR \"out-of-distribution\" latent 2025 2026\n\n**HIGHLY RELEVANT FINDINGS:**\n\n**[Verifier-free Test-Time Sampling for Vision Language Action Models (MG-Select)](https://arxiv.org/abs/2510.05681)** (October 2025, ICLR 2026)\n- **Scoring mechanism**: KL divergence from reference action distribution\n- Reference distribution: obtained by masking states/language conditions (maximum uncertainty)\n- Selects actions with **highest** KL divergence\n- Best-of-N sampling without external verifier\n- **Critical difference from LOC**: Uses KL divergence from uncertainty-aware masked distribution, NOT density estimation on success latents\n- No fitting to demonstration data; uses model's own masked predictions as reference\n\n**[RoVer: Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)** (October 2025)\n- Uses learned Process Reward Model (PRM) to score candidates\n- Scores are scalar process rewards (not density-based)\n- Generates multiple candidates, expands along PRM-predicted directions, selects best\n- Different paradigm: trained reward model vs. density estimation on latents\n\n---\n\n### Query 8: \"MG-Select\" robot VLA test-time sampling arxiv 2510.05681\n\n**Direct Answer to Your Question:**\n\n**Does MG-Select use KL from masked distribution? Is it really different from LOC?**\n\n✓ **Yes, MG-Select uses KL from masked distribution** (not density estimation)\n\n**Key Mechanism:**\n- Generates reference distribution by passing same VLA with randomly **masked states and language conditions** as inputs\n- This forces maximum uncertainty while staying task-aligned\n- Computes KL divergence between sampled actions and this reference distribution\n- Selects actions with **highest** KL (most confident/different from uncertainty)\n- **No fitting to demonstrations required** - uses model's own outputs\n\n**How it differs from LOC:**\n| Aspect | LOC | MG-Select |\n|--------|-----|-----------|\n| **Basis** | Fit density model (KNN/GMM) on success demo latents | KL divergence from masked reference distribution |\n| **Training** | Requires fitting to successful trajectory data | Zero training, uses base VLA only |\n| **Computation** | Distance/density in fitted model | KL divergence between distributions |\n| **Mechanism** | \"In-distribution according to success data\" | \"Confident/different from uncertainty\" |\n\n---\n\n### Additional Test-Time Scaling Work Found:\n\n**[RoboMonkey / Cortex 2.0](https://arxiv.org/html/2604.20246)** (2024):\n- World model generates candidates in visual latent space\n- Process-Reward Operator scores each for task progress and risk\n- Different from density estimation approach\n\n**[Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068v1)** (2025):\n- Convex composition of distributional scores from multiple policies\n- Theoretical framework for composition, not density-based selection\n\n**[Steering Your Generalists (V-GPS)](https://arxiv.org/html/2410.13816v2)** (2024):\n- Re-ranks actions using value function Q(s,a)\n- Operates in explicit action space, not latent; learned via offline RL\n\n---\n\n## Summary: Does LOC Already Exist?\n\n**No direct precedent found**, but closest approaches:\n\n1. **KDPE** - Uses KDE for trajectory filtering, but in action space not latent space, and on all training actions not just successful ones\n\n2. **MG-Select** - Performs best-of-N candidate selection in action latent space (for VLAs), but uses KL divergence from masked distribution, not density estimation on success demonstrations\n\n3. **ALT Policy** - Uses NN lookup with threshold-based OOD detection in contrastive latent space, not density modeling\n\n4. **RoVer** - Uses learned reward model to score candidates, not density estimation\n\n**The core idea of your LOC approach** - fitting a density model (KNN/GMM) on **successful demonstration latents** and using it to score/select actions - **appears to be novel**. The closest work does density estimation in action space (KDPE) or uses other scoring mechanisms (MG-Select's KL, RoVer's rewards, V-GPS's Q-function), but none directly estimate density over success latents for candidate filtering in the way you describe.\n\n---\n\n## Sources:\n\n- [Latent Theory of Mind](https://arxiv.org/html/2505.09144v1)\n- [KDPE: Kernel Density Estimation Strategy](https://arxiv.org/abs/2508.10511)\n- [Demystifying Diffusion Policies (ALT)](https://arxiv.org/abs/2505.05787)\n- [Verifier-free Test-Time Sampling (MG-Select)](https://arxiv.org/abs/2510.05681)\n- [RoVer: Robot Reward Model](https://arxiv.org/abs/2510.10975)\n- [Steering Your Generalists (V-GPS)](https://arxiv.org/html/2410.13816v2)\n- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068v1)\n- [Efficient Robotic Policy Learning via LBP](https://arxiv.org/abs/2505.06861)\n- [Ctrl-World Generative World Model](https://arxiv.org/html/2510.10125v1)\n- [Safe Probabilistic Planning with Conformal Risk Control](https://arxiv.org/html/2603.10392v1)\n- [Learning Robot Safety via Conformal Prediction](https://arxiv.org/html/2501.04823)\n- [Latent Space Backward Planning](https://lbp-authors.github.io/)\n- [Deep Generative Models in Robotics Survey](https://arxiv.org/html/2408.04380v1)\n- [Continuous Latent Action Models (CLAM)](https://arxiv.org/abs/2505.04999)"
      }
    ],
    "totalDurationMs": 150202,
    "totalTokens": 46087,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2190,
      "cache_read_input_tokens": 41433,
      "output_tokens": 2457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2457,
          "cache_read_input_tokens": 41433,
          "cache_creation_input_tokens": 2190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2190,
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
      "otherToolCount": 28
    }
  },
  "sourceToolAssistantUUID": "9c834a37-cf39-47ed-98a1-bbaef32c67ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T08:56:11.552Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research findings. Let me analyze the key issues:

1. **FAIL-Detect and EVA are confirmed** - Both papers exist and their claims as described are accurate.

2. **Key novelty question - LOC approach**: The search found KDPE (Kernel Density Estimation for diffusion policy trajectory selection) which operates in action space (not latent space) and on all training data (not just success demos). No paper found that does exactly what LOC proposes - fitting density estimator on success demo latents of a jointly-trained video-action WAM.

3. **Fast-WAM claim verification**: The agent says Fast-WAM does NOT claim 97.6% LIBERO without test-time video. 

The generator cites "97.6% LIBERO-avg and 91.8% RoboTwin without video at inference, at 190ms latency," which appears to be inaccurate—the 98.5% LIBERO figure actually comes from Cosmos Policy. I also found several related papers during my search: UNISafe uses conformal prediction for OOD detection on latent representations for safety filtering, KDPE applies kernel density estimation to diffusion policies in action space, and there's LPS as well, though none of these match the exact approach LOC describes.

Looking at the shift from Round 4 to Round 5, the move from PCS (video denoising error) to LOC (Latent OOD Consistency Scoring) is a fundamental change to the entire primary method. The reasoning makes sense—Cosmos Policy showed that demo-only video priors can't predict failure states, EVA revealed that visual coherence doesn't guarantee task success, and FAIL-Detect demonstrated that OOD detection on success demos reliably catches failures. But there's a critical unverified assumption at the heart of LOC: the claim that action latents from successful demonstrations form a tight, separable distribution that's clearly distinguishable from failure latents.

The problem is that FAIL-Detect operates on execution-time policy signals during rollout, not on pre-execution latent representations from a different inference mode. There's a significant gap between how FAIL-Detect works and what LOC assumes—whether the success/failure separation in these latents is actually meaningful enough to discriminate between just 4-8 candidates is completely unvalidated. Additionally, the Fast-WAM performance claims seem inconsistent with what the research agent reported, so I need to reconcile those numbers.

The diagnostic design for LOC has a critical failure mode: if LOC underperforms (AUC < 0.55), the paper falls back on Value MLP as the primary contribution, but that requires failure demonstrations from simulation. If both approaches fail, there's no contribution at all. And I haven't seen how this work differentiates from KDPE, which already does KDE-based trajectory selection for diffusion policies.

The core issue is that the paper's entire value rests on an unproven hypothesis—that z_a regularized by joint video-action pretraining creates better-separated success latent distributions than VLA action tokens. The diagnostic in Step 1 tests this, but if it fails, the zero-training contribution evaporates. What's more concerning is the structure itself: they're proposing to submit to CoRL without knowing if their primary method actually works, with the diagnostic happening during the submission window.

If LOC underperforms, the fallback to Value MLP is significantly less novel. There's also the KDPE problem—if that CoRL 2025 work is already doing KDE-based trajectory selection for diffusion policies, the distinction between operating in action space versus latent space, and targeting WAMs instead, needs to be articulated clearly. Finally, the resource estimates are tight: 165 hours for human-in-loop and 320 for auto, but the compute budget maxes out at 200 H100-hours.

The core question is whether LOC's novelty—applying standard density estimation to action latents at inference time—goes beyond just "density estimation in a different space." The real contribution might be showing that MG-Select's KL approach, when applied directly to WAM latents, underperforms compared to LOC's simpler density-based selection.

The experimental design has merit: the pivot from PCS to LOC is grounded in actual theory, the LOC diagnostic acts as a validation gate before committing resources, and there's intellectual honesty in planning for negative results. But there's a critical vulnerability—if the Fast-WAM 97.6% LIBERO baseline is inaccurate or fabricated, the entire framing collapses.

More fundamentally, the LOC hypothesis itself is unvalidated. The core claim that WAM action latents naturally separate success from failure in z_a is plausible but unproven—unlike FAIL-Detect which demonstrated this on policy execution signals, there's no evidence this holds for action-only inference mode. I'm also noticing KDPE (arXiv 2508.10511) is missing from the related work, which directly addresses density-based trajectory selection in diffusion policies and should be cited as a predecessor. Finally, the 165-hour estimate for human-in-loop mode seems optimistic given the complexity involved.

The resource constraints are tight—auto research alone needs 320 hours, which already exceeds the 200 H100-hour budget. Everything hinges on whether LOC achieves an AUC ≥ 0.6 in the first step. If it fails, the contribution collapses to just a Value MLP on top of RoVer and WAM, which is far less novel. The new title is descriptive but unwieldy for a conference submission.

On novelty, I'd rate this 3/5—LOC is a solid application of OOD density scoring to WAM latents with decent theoretical grounding, but the core hypothesis remains unproven and there's an unaddressed precedent in KDPE. Feasibility is also 3/5 given the budget overrun in auto mode and the risky sequential dependencies compressed into 20 days. The proposal itself is well-articulated though, so clarity lands at 4/5.

For impact, it hinges entirely on whether WAM latents actually have the distributional structure LOC needs—if they do, this is genuinely useful; if not, we're just looking at a cheaper variant of existing methods. That uncertainty brings the overall score to 3.25/5, below the 4.0 threshold, so this needs revision. The main gaps are verifying the Fast-WAM claim, properly addressing KDPE as prior art, and bringing the auto research timeline within the 200-hour hard limit.

But I need to double-check the Fast-WAM numbers themselves. The research agent clarified that the paper doesn't claim 97.6% on LIBERO without video—it says "competitive results" at 190ms latency. The 97.6% figure I cited appears to be either a real but unverified number or possibly conflated with Cosmos Policy's 98.5%. I should verify whether Fast-WAM actually achieves those specific numbers before treating them as established fact.

Now looking at KDPE more carefully—if it's using KDE for trajectory selection in diffusion policies, that's potentially relevant prior work, but there's a key difference: KDPE operates in action space rather than latent space, which changes how directly comparable it is to the approach being proposed.

For Round 5's overall assessment, the shift from PCS to LOC as the primary zero-training method is a meaningful improvement since PCS has been undermined by the Cosmos Policy results. The diagnostic now treats PCS as an expected negative case, which is more scientifically sound. The main remaining concerns are the KDPE citation gap, the auto research time exceeding the stated constraint, the unvalidated LOC hypothesis, and verification of the Fast-WAM numbers.

The LOC approach has a reasonable fallback in the Value MLP, which itself represents a novel contribution in the WAM latent space context. However, the core theoretical bet—that WAM's action latent space provides better success/failure separation than standard VLA tokens—lacks empirical support, which is a significant risk. I should verify the KDPE paper date since the research agent cited an August 2025 arXiv number, which would suggest it's a recent CoRL paper.

Given we're at Round 5 of 10 and previous critical issues have been resolved, the remaining problems are moderate rather fundamental. The main concerns are the uncited KDPE work, the auto-research exceeding the 200-hour budget, verification of Fast-WAM specific numbers, and the unvalidated core hypothesis about latent space structure. REVISE seems appropriate here.

Looking at the scoring: novelty sits at 3.5/5 since the LOC approach is genuinely novel within the WAM latent context and clearly differentiated from prior work like MG-Select and RoVer, though KDPE's absence is notable. Feasibility is 3/5—the human-in-loop component at 165 hours fits the budget, but the auto-research at 320 hours significantly overshoots, and the 20-day timeline is tight for a method requiring sequential diagnostics.

Clarity scores well at 4.5/5 with exceptional detail and honest failure modes, while impact is 3/5 since success hinges on LOC working; otherwise it reduces to the more incremental Value MLP contribution. This averages to 3.5/5, below the 4.0 threshold.

But reconsidering impact—the WAM field is moving fast, and a practical tool that converts any frozen WAM into a multi-candidate planner without retraining would genuinely matter. The zero-training aspect is compelling if LOC succeeds, and even if it doesn't, the latent geometry analysis comparing WAM and VLA latents still offers value.

Bumping impact to 3.5 gives a revised average of 3.625, still below 4.0, so I need to write up the verdict and flag the key issues: KDPE is missing from the related work, the auto research budget at 320 H100-hours exceeds the stated constraint, Fast-WAM's 97.6% LIBERO claim couldn't be independently verified, and the LOC hypothesis itself needs more scrutiny.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "173576d7-64e8-4890-b7ed-1f16fd39b08e",
  "isSidechain": false,
  "requestId": "req_011CatcBeVoxKGetsisEfyGg",
  "type": "assistant",
  "uuid": "709da1bb-250e-4f54-92c9-1857b06e5d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AMNp8N9eghrQGXbAe3kGqL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4459,
      "cache_creation_input_tokens": 5818,
      "cache_read_input_tokens": 37204,
      "output_tokens": 4929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4459,
          "output_tokens": 4929,
          "cache_read_input_tokens": 37204,
          "cache_creation_input_tokens": 5818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5818
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

_source line 19 · 2026-05-10T08:56:11.554Z_

Now let me conduct one more targeted search on KDPE and verify the Fast-WAM numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "709da1bb-250e-4f54-92c9-1857b06e5d78",
  "isSidechain": false,
  "requestId": "req_011CatcBeVoxKGetsisEfyGg",
  "type": "assistant",
  "uuid": "3b6d1aa7-081b-445d-a99e-39a1c947898f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AMNp8N9eghrQGXbAe3kGqL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4459,
      "cache_creation_input_tokens": 5818,
      "cache_read_input_tokens": 37204,
      "output_tokens": 4929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4459,
          "output_tokens": 4929,
          "cache_read_input_tokens": 37204,
          "cache_creation_input_tokens": 5818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5818
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

_source line 20 · 2026-05-10T08:56:17.079Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SLfAxt1Gr6mjzPxVWBR2Pq`</summary>

```json
{
  "description": "Verify Fast-WAM numbers and KDPE paper details",
  "subagent_type": "Explore",
  "prompt": "I need to verify two specific claims for a paper review:\n\n1. **Fast-WAM (arXiv 2603.16666)**: The paper under review claims \"97.6% LIBERO-avg and 91.8% RoboTwin without video at inference, at 190ms latency.\" Please:\n- Fetch https://arxiv.org/abs/2603.16666 to check the abstract and results\n- Also try https://arxiv.org/pdf/2603.16666 for more details\n- Does Fast-WAM actually report 97.6% on LIBERO-avg? \n- Does it report 91.8% on RoboTwin?\n- Does it operate at 190ms latency?\n\n2. **KDPE (arXiv 2508.10511)**: A paper claimed to use \"Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection\" for robots, published at CoRL (circa August 2025).\n- Fetch https://arxiv.org/abs/2508.10511\n- Does this paper exist? What does it actually do?\n- Does it use KDE on action space (not latent space)?\n- Does it select trajectories from diffusion policies?\n- If it exists, how is it differentiated from using KDE/KNN on WAM action latents (which is what the reviewed paper proposes)?\n\nReport exact findings with numbers where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b6d1aa7-081b-445d-a99e-39a1c947898f",
  "isSidechain": false,
  "requestId": "req_011CatcBeVoxKGetsisEfyGg",
  "type": "assistant",
  "uuid": "466668a6-212f-4a6a-bf7b-bcb6bea795bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AMNp8N9eghrQGXbAe3kGqL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4459,
      "cache_creation_input_tokens": 5818,
      "cache_read_input_tokens": 37204,
      "output_tokens": 4929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4459,
          "output_tokens": 4929,
          "cache_read_input_tokens": 37204,
          "cache_creation_input_tokens": 5818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5818
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "466668a6-212f-4a6a-bf7b-bcb6bea795bb",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent candidate selection via OOD and value functions",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Tool result

_source line 23 · 2026-05-10T08:56:32.697Z_

<details><summary>↩ Tool result · `toolu_01SLfAxt1Gr6mjzPxVWBR2Pq`</summary>

```text
Based on my verification, here are the exact findings:

## Claim 1: Fast-WAM (arXiv 2603.16666)

**Latency Claim - VERIFIED:**
- The paper DOES report **190ms latency** as stated. The abstract confirms: "It runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs."

**Performance Claims - UNVERIFIED IN ABSTRACT:**
- The abstract mentions "competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin)" but **does NOT provide the specific percentages** (97.6% LIBERO-avg or 91.8% RoboTwin) in the accessible portions I retrieved.
- These exact numbers likely appear in the paper's results tables, but they are not visible in the abstract or immediately accessible sections. You would need to access the full PDF body to verify these specific performance metrics.

## Claim 2: KDPE (arXiv 2508.10511)

**Paper EXISTS - CONFIRMED:**
- Full title: **"KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection"**

**What it actually does:**
- It proposes a KDE-based filtering strategy to select/filter trajectories from Diffusion Policy outputs
- It uses "a manifold-aware kernel to model a probability density function for actions composed of end-effector Cartesian position, orientation, and gripper state"
- It addresses multimodality and stochasticity issues in Diffusion Policy by intelligently filtering potentially harmful trajectories

**Key difference from reviewed paper's approach:**
- **KDPE applies KDE to the action space directly** (Cartesian position, orientation, gripper state) to filter Diffusion Policy outputs
- Your reviewed paper proposes **KDE/KNN on WAM action latents** (applying it to the latent representation of a different model)
- These are fundamentally different applications: KDPE uses KDE as a post-hoc filter for diffusion policy trajectories, while your paper applies it to the latent representation of a WAM model

**Critical distinction:** KDPE is about trajectory filtering/selection (choosing which outputs to keep), whereas your paper appears to be about nearest-neighbor matching in latent space, which is a different use case.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "466668a6-212f-4a6a-bf7b-bcb6bea795bb",
  "isSidechain": false,
  "promptId": "7cfc2bf9-4784-4738-bc7e-6ecf5c05863c",
  "type": "user",
  "uuid": "03da439a-57d8-4e33-b4a6-9fa21b75e75c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific claims for a paper review:\n\n1. **Fast-WAM (arXiv 2603.16666)**: The paper under review claims \"97.6% LIBERO-avg and 91.8% RoboTwin without video at inference, at 190ms latency.\" Please:\n- Fetch https://arxiv.org/abs/2603.16666 to check the abstract and results\n- Also try https://arxiv.org/pdf/2603.16666 for more details\n- Does Fast-WAM actually report 97.6% on LIBERO-avg? \n- Does it report 91.8% on RoboTwin?\n- Does it operate at 190ms latency?\n\n2. **KDPE (arXiv 2508.10511)**: A paper claimed to use \"Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection\" for robots, published at CoRL (circa August 2025).\n- Fetch https://arxiv.org/abs/2508.10511\n- Does this paper exist? What does it actually do?\n- Does it use KDE on action space (not latent space)?\n- Does it select trajectories from diffusion policies?\n- If it exists, how is it differentiated from using KDE/KNN on WAM action latents (which is what the reviewed paper proposes)?\n\nReport exact findings with numbers where possible.",
    "agentId": "a27b7794af905af2f",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my verification, here are the exact findings:\n\n## Claim 1: Fast-WAM (arXiv 2603.16666)\n\n**Latency Claim - VERIFIED:**\n- The paper DOES report **190ms latency** as stated. The abstract confirms: \"It runs in real time with 190ms latency, over 4× faster than existing imagine-then-execute WAMs.\"\n\n**Performance Claims - UNVERIFIED IN ABSTRACT:**\n- The abstract mentions \"competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin)\" but **does NOT provide the specific percentages** (97.6% LIBERO-avg or 91.8% RoboTwin) in the accessible portions I retrieved.\n- These exact numbers likely appear in the paper's results tables, but they are not visible in the abstract or immediately accessible sections. You would need to access the full PDF body to verify these specific performance metrics.\n\n## Claim 2: KDPE (arXiv 2508.10511)\n\n**Paper EXISTS - CONFIRMED:**\n- Full title: **\"KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection\"**\n\n**What it actually does:**\n- It proposes a KDE-based filtering strategy to select/filter trajectories from Diffusion Policy outputs\n- It uses \"a manifold-aware kernel to model a probability density function for actions composed of end-effector Cartesian position, orientation, and gripper state\"\n- It addresses multimodality and stochasticity issues in Diffusion Policy by intelligently filtering potentially harmful trajectories\n\n**Key difference from reviewed paper's approach:**\n- **KDPE applies KDE to the action space directly** (Cartesian position, orientation, gripper state) to filter Diffusion Policy outputs\n- Your reviewed paper proposes **KDE/KNN on WAM action latents** (applying it to the latent representation of a different model)\n- These are fundamentally different applications: KDPE uses KDE as a post-hoc filter for diffusion policy trajectories, while your paper applies it to the latent representation of a WAM model\n\n**Critical distinction:** KDPE is about trajectory filtering/selection (choosing which outputs to keep), whereas your paper appears to be about nearest-neighbor matching in latent space, which is a different use case."
      }
    ],
    "totalDurationMs": 15613,
    "totalTokens": 19407,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 337,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 16906,
      "output_tokens": 540,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 337,
          "output_tokens": 540,
          "cache_read_input_tokens": 16906,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1624,
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
  "sourceToolAssistantUUID": "466668a6-212f-4a6a-bf7b-bcb6bea795bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T08:56:54.449Z_

<details><summary>Logged reasoning block</summary>

```text
So KDPE (arXiv 2508.10511) is confirmed to exist. It uses KDE on action space (Cartesian coordinates) for trajectory selection. The reviewed paper's LOC uses KNN/GMM on WAM action latents (z_a) - so there is a real difference, but the general idea of "density-based trajectory selection using KDE/KNN" is already established.

Fast-WAM's 97.6% LIBERO and 91.8% RoboTwin numbers couldn't be confirmed from the abstract, but are plausible (they're in the results tables). 

The abstract confirms 190ms latency and competitive results. Looking at my findings: FAIL-Detect and EVA are confirmed as supporting prior work, KDPE is the closest existing approach for density-based trajectory selection that wasn't cited, and while I can't verify the exact Fast-WAM performance numbers, the 190ms latency claim checks out.

The main issues are that KDPE should have been cited as prior art, the specific performance metrics appear unverified, the auto research consumed roughly 320 hours of compute against a stated 200-hour budget, and the core LOC hypothesis about latent geometry differences remains entirely unvalidated.

For novelty, the approach scores around 3.5 out of 5—the success-latent KNN/GMM selection does differentiate from both MG-Select and KDPE, and the theoretical framing around joint pretraining regularization is coherent, though KDPE deserves acknowledgment as the closest prior work. Feasibility lands at 3 out of 5 since the human-in-loop path barely fits the budget while the auto research path clearly overshoots it.

The plan itself is exceptionally clear and well-structured with honest fallback reasoning, earning 4.5 for clarity—the LOC diagnostic as a mandatory first step is the right call. Impact sits at 3.5: if LOC succeeds it's a clean contribution to the WAM community, if it fails the Value MLP becomes more incremental, but either way the diagnostic generates useful scientific knowledge in a competitive, high-reward area.

Averaging these scores gives 3.625, which falls below the 4.0 threshold, so the paper needs revision. The technical direction has genuinely improved across iterations—moving from PCS to LOC is much more principled—but four concrete issues remain: the KDPE citation needs clarification, the Fast-WAM performance numbers require verification, the auto research budget overruns the hard constraint and needs trimming or explicit acknowledgment, and the LOC hypothesis should be framed more rigorously with a null hypothesis stated upfront.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03da439a-57d8-4e33-b4a6-9fa21b75e75c",
  "isSidechain": false,
  "requestId": "req_011CatcKLeEeS4U1Fw3a6Esy",
  "type": "assistant",
  "uuid": "1c0fcae5-b067-41bd-bb9f-29d0b3b3705b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UgHXbU1XZbkuWcCBBofsFa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9933,
      "cache_read_input_tokens": 43022,
      "output_tokens": 3516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3516,
          "cache_read_input_tokens": 43022,
          "cache_creation_input_tokens": 9933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9933
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

_source line 25 · 2026-05-10T08:57:38.402Z_

Based on my independent research, I can now form a verdict. Key findings:
- FAIL-Detect (2503.08558) and EVA (2603.17808): **both confirmed** — claims are accurate
- **KDPE (arXiv 2508.10511, CoRL 2025)**: confirmed to exist — uses KDE on diffusion policy action trajectories for selection; NOT cited in this paper
- Fast-WAM: 190ms latency confirmed; specific 97.6% LIBERO / 91.8% RoboTwin numbers **unverifiable from abstract** — only "competitive results" stated
- LOC approach: no direct prior work found fitting density estimators on WAM success-demo latents for pre-execution candidate selection — appears novel with respect to cited space

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "LOC's use of KNN/GMM density estimation on WAM success-demo action latents is differentiated from MG-Select (KL-from-masked-distribution) and RoVer (trained PRM), but KDPE (arXiv 2508.10511, CoRL 2025) — which uses KDE on diffusion policy action trajectories for candidate selection — is entirely absent from the landscape, and the distinction between 'action space KDE' (KDPE) and 'action latent KDE on success-only data' (LOC) requires explicit argumentation; the core theoretical claim (WAM z_a has more separable success/failure geometry than VLA action tokens due to joint pretraining) is a hypothesis rather than an established finding."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Human-in-loop estimate (165h) barely clears the ≤200 H100-hour hard constraint, but auto research (~320h) exceeds it by ~60%, violating the user-specified hard limit; the 20-day sequential dependency chain (Step 0a → LOC diagnostic → failure collection → density fitting → Value MLP → ablations) with RoboCasa environment setup as a latent blocker remains extremely aggressive."
    },
    "clarity": {
      "score": 4,
      "rationale": "The proposal has exceptional methodological clarity — decision trees, failure-mode branching, mandatory diagnostic before commitment, and honest fallback planning are all well-specified; the split between LOC diagnostic (scientific question) and main ablation (engineering question) is a strong structural choice."
    },
    "impact": {
      "score": 3,
      "rationale": "If LOC AUC ≥ 0.6 is validated, a zero-training frozen-WAM multi-candidate planner is practically valuable for the hot WAM community; if LOC falls below threshold, the paper reduces to Value MLP, which is a more incremental contribution compared to WAV/RoVer in the WAM latent context and weakens the headline narrative."
    }
  },
  "issues": [
    "SIGNIFICANT — KDPE (arXiv 2508.10511, CoRL 2025) is absent from the landscape section. This paper uses Kernel Density Estimation on diffusion policy action trajectories (Cartesian position/orientation/gripper) for trajectory selection and filtering — the closest prior work for density-based candidate selection in robot policies. The differentiation from LOC is real (action space vs. action latent space; all training data vs. success-only; base diffusion policy vs. frozen WAM) but must be explicitly stated. A reviewer familiar with KDPE will immediately ask why it is not cited. Add it to related work with the differentiation: 'KDPE applies KDE in Cartesian action space using all training demonstrations; LOC fits density in the WAM's joint-pretraining-regularized action latent space z_a using only success demonstrations, exploiting WAM-specific latent geometry unavailable to action-space-only density methods.'",
    "SIGNIFICANT — Fast-WAM's specific performance numbers (97.6% LIBERO-avg, 91.8% RoboTwin) are unverifiable from the paper's abstract. My independent fetch of arXiv 2603.16666 confirms the 190ms latency and 'competitive with SOTA' language, but the 97.6% and 91.8% figures do not appear in the accessible abstract and could not be confirmed. If these numbers are taken from results tables they should be cited with table references; if they were inferred or estimated they must be verified before submission. Inaccurate framing reference numbers will be caught by reviewers who read Fast-WAM.",
    "SIGNIFICANT — Auto research GPU estimate (~320h H100) exceeds the user's ≤200 H100-hour hard constraint by ~60%. Even though human-in-loop (165h) is under budget, the paper should either: (a) revise the auto research estimate with explicit task-parallel scheduling showing how 320h wall-clock is achieved within budget using concurrent GPU allocation (4–8 GPUs × 40–80 hours wall clock ≤ 200 billed GPU-hours is mathematically impossible — parallel GPUs multiply billed hours, not reduce them), or (b) scope auto research to stay under 200h by pruning the ablation grid (e.g., drop T_noise sweep or reduce B grid). As written, auto research violates a hard user constraint.",
    "MODERATE — The LOC hypothesis ('WAM z_a regularized by joint video-action pretraining forms a success latent distribution more separable from failure regimes than VLA action tokens') is the paper's central theoretical claim but is stated as established fact rather than as an empirical hypothesis to be tested. FAIL-Detect proves OOD detection on success-only data works for execution-time policy signals — a meaningfully different signal domain from pre-execution WAM z_a generated via action-only inference. The proposal should frame this clearly as Hypothesis H1 (tested in Step 1 LOC diagnostic) rather than citing FAIL-Detect as if it proves LOC will work a priori. The diagnostic is the right design; the framing should match it.",
    "MODERATE — If LOC AUC < 0.55 in the diagnostic and the paper falls back to Value MLP as the sole primary contribution, the novelty argument needs to be independently reassessed in that scenario. Value MLP on WAM action latents differentiates from WAV (WAV trains from scratch; Value MLP is plug-in) and from RoVer (0.2B PRM vs. 3-layer MLP; VLA action tokens vs. WAM z_a), but these differentiations are currently only secondary claims. The paper should have a brief paragraph ready that constructs Value MLP as a complete standalone contribution if LOC fails — so the submission narrative does not implicitly depend on LOC succeeding."
  ],
  "feedback": "Round 5 represents a major legitimate pivot: replacing PCS (directly contradicted by Cosmos Policy's own finding) with LOC (grounded in FAIL-Detect + EVA + WAM latent geometry) is the right scientific call. The mandatory LOC diagnostic before main ablation is excellent experimental design. Four concrete fixes are needed:\n\n**1. Cite and differentiate KDPE (1 day).** Add KDPE (arXiv 2508.10511, CoRL 2025) to the landscape section. Write: 'KDPE (CoRL 2025) applies KDE to Cartesian action trajectories from diffusion policies to filter multimodal outputs. LOC differs in three ways: (a) density estimation in the WAM's action latent space z_a rather than Cartesian action space; (b) success-demonstrations-only reference distribution rather than all training data; (c) exploitation of WAM-specific joint pretraining regularization that structures z_a along physical plausibility dimensions unavailable in action space.' This closes the most significant gap a CoRL reviewer will notice.\n\n**2. Verify or correct Fast-WAM numbers (0.5 day).** Fetch the Fast-WAM PDF and confirm the 97.6% LIBERO-avg and 91.8% RoboTwin numbers from the results tables. If the numbers are correct, cite with 'Table X in Fast-WAM.' If they are not in the paper, correct the framing reference to match the actual reported results. This is a basic credibility check that reviewers will do.\n\n**3. Fix the auto research budget (0.5 day).** The auto research estimate of ~320h H100 exceeds the ≤200h hard constraint. Trim the auto research ablation grid to fit within budget: drop the T_noise sweep from auto mode (keep in human-in-loop for targeted follow-up), reduce B to {1,4,8} from {1,2,4,8,16} in auto mode, and reduce seeds from N to 3. Show explicitly: '4 GPUs × ~45h wall-clock = ~180 billed H100-hours.' Alternatively, move T_noise and full B-sweep to camera-ready. The 200h constraint is a hard user requirement.\n\n**4. Reframe the LOC hypothesis (0.5 day).** Retitle the theoretical motivation section something like 'Hypothesis: WAM Joint Pretraining Creates an OOD-Detectable Success Latent Distribution' and state explicitly: 'The LOC diagnostic (Section 3.1) empirically tests this hypothesis; if AUC < 0.55, LOC reports a negative result and Value MLP becomes the primary contribution.' This is scientifically more honest and actually *strengthens* the paper's credibility — reviewers respect null-result framing. Also note explicitly that FAIL-Detect demonstrates this principle on execution-time signals; LOC applies it to pre-execution z_a from a different inference mode, and Step 1 is the first empirical test of whether this transfer holds.",
  "reason": "All Round 4 issues addressed and the PCS→LOC pivot is scientifically sound, but KDPE (closest prior art) is uncited, Fast-WAM numbers are unverified, auto research exceeds the 200h hard constraint, and the LOC hypothesis needs to be framed as a testable hypothesis rather than established fact."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c0fcae5-b067-41bd-bb9f-29d0b3b3705b",
  "isSidechain": false,
  "requestId": "req_011CatcKLeEeS4U1Fw3a6Esy",
  "type": "assistant",
  "uuid": "7b410782-f712-4837-ab73-5f36c4a89e11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UgHXbU1XZbkuWcCBBofsFa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9933,
      "cache_read_input_tokens": 43022,
      "output_tokens": 3516,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3516,
          "cache_read_input_tokens": 43022,
          "cache_creation_input_tokens": 9933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9933
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7b410782-f712-4837-ab73-5f36c4a89e11",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent candidate selection via OOD and value functions",
  "sessionId": "eb569be8-fd5d-4af2-9acc-96cb78268509"
}
```

---
