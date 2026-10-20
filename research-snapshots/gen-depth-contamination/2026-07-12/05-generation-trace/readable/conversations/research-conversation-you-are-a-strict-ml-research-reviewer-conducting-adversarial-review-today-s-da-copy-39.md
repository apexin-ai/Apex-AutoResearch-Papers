# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/012ce64b-5c43-497f-abb0-193915a80ee0.jsonl`
- **Structured JSON:** [`2c8b054500a89c086bce.json`](../../sessions/2c/2c8b054500a89c086bce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:30:44.038Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:30:44.038Z",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World Action Models (WAMs) — joint world modeling and action prediction in a unified architecture, often built on video diffusion priors. In-scope: unified video+action prediction, MoT (Mixture-of-Transformers) architectures with text/video/action streams, WMs that double as policies via inverse dynamics on imagined futures, action-conditioned video diffusion as policy.\n\nRecent landscape (do not duplicate): UniVLA, DreamVLA, GigaBrain-0.5M, DiT4DiT, MotuBrain, video-diffusion-as-policy lines. WAMs are the hottest CoRL 2026 area — high competition but high reward.\n\nContribution type: METHOD ONLY. New unified architecture, new training scheme that fuses world prediction and action prediction, new inference algorithm extracting actions from imagined futures.\n\nSIM-ONLY MITIGATION: WAM papers at CoRL routinely use sim envs since the method depends on data scale, not real-robot deployment. Use LIBERO/ManiSkill as primary and frame contribution as architectural.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Most challenging budget — video models are heavy. Strategies: (a) fine-tune an open video WM (Cosmos releases, OpenSora, CogVideoX) with action conditioning, (b) distill a large WAM into a smaller one, (c) propose a method that requires only small additional training on top of an existing WAM, (d) propose an inference-time method that needs no training.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos.\n3. Eval: LIBERO, ManiSkill 2/3, RoboCasa for closed-loop control + video prediction quality (PSNR/SSIM/FVD on action-conditioned futures). Compare against UniVLA / DreamVLA / DiT4DiT lineage if open releases exist.\n\nLook for: efficient action-conditioning of video diffusion, latent WAMs that bypass pixel decoding, methods that share representations across world and action streams. Avoid: trivial action-token prepending without architectural insight.\n\nTag: direction=world_action_model, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation\",\n  \"core_problem\": \"Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. This paper exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\\n\\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\\n\\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical; (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. This paper addresses the third cost: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task oracle justifies it, and eliminate the 10-rollout-per-task deployment calibration cost via a zero-shot router trained on LIBERO-100.\\n\\nCRITICAL PARETO FRAMING CLARIFICATION (required for reviewer accuracy): If the pre-registered prediction P1 is confirmed (fixed intermediate τ_v < 1 underperforms τ_v=1 on SIMPLER-Bridge — the expected outcome per mimic-video main text), then the zero-shot router routes the MAJORITY of frames to τ_v=1. This means: (a) mean τ_v consumed by CDR stays CLOSE TO 1.0; (b) per-inference GPU compute savings are SMALL (5–10% at most); (c) the primary benefit is TASK SUCCESS RECOVERY (+≥7.5pp zero-shot on SIMPLER-Bridge) and DEPLOYMENT CALIBRATION SAVINGS (10 offline rollouts per new task → 0). The abstract and introduction MUST state this explicitly. CDR's Pareto dominance vs. τ_v=1 is: same or slightly lower mean τ_v consumed, significantly higher task success — not a large speedup per inference call.\\n\\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.\",\n  \"opportunity\": \"The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. This paper exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\\n\\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. The primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost.\\n\\nCRITICAL: THE DEPLOYMENT EFFICIENCY GAIN IS CALIBRATION COST, NOT PER-INFERENCE COMPUTE. When P1 is confirmed (the expected outcome), CDR routes most frames to τ_v=1, keeping mean τ_v close to 1.0. The efficiency improvement CDR delivers is: eliminating the 10-offline-rollout per-task sweep required to find the optimal fixed τ_v for a new task. A new task can be deployed with ZERO rollouts using the zero-shot router, rather than requiring 10 rollouts to calibrate the best fixed τ_v. This is a real and practically important contribution — robotics deployments accumulate many new tasks, and even at 10 rollouts each, calibration cost is significant — but it is DIFFERENT from 'faster inference per call.' The paper's framing must be explicit: 'CDR saves deployment calibration cost (10 rollouts → 0 per new task) and recovers task success (+≥7.5pp zero-shot), not primarily per-inference GPU compute.'\\n\\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, this paper also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies the competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. The Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the tasks/frames that need it, without any offline rollout cost.'\\n\\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. deployment-calibration-rollouts Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\\n\\nThe primary scientific contribution is Phase 1: the FIRST empirical characterization of which 3D manipulation phases require video denoising below the τ_v=1 fixed-global default, using GT-action-referenced τ_v labeling across LIBERO-100. The zero-shot router is the deployment mechanism enabling practical use of Phase 1's findings without offline sweeps — not the architectural novelty. The paper should be read as an empirical methods contribution, not an architectural one.\",\n  \"landscape\": \"LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is the primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\\n\\nmimic-video (arXiv:2512.15692, Dec 2025) is the base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — this paper's contribution is approximating the per-task oracle via zero-shot routing; (d) per-task sweep yields +9.4pp (46.9%→56.3%), confirming the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\\n\\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\\n\\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\\n\\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\\n\\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\\n\\nDiT4DiT (arXiv:2603.10448) ablation (Figure 8b): fewer ACTION denoising steps yield higher task success — this finding concerns the action diffusion process, NOT τ_v (video noise level). These are orthogonal efficiency axes. CDR cites DiT4DiT only as a structural analogy: in both the action domain (DiT4DiT) and the video domain (mimic-video τ_v=1 main-text finding), less denoising tends to be preferable as a global default. CDR does NOT use DiT4DiT to corroborate τ_v=1 video noise optimality; these are different axes and conflating them would be factually incorrect. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\\n\\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\\n\\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\\n\\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) introduces a per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing.\\n\\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.\",\n  \"approach\": \"CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\\n\\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\\n\\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\\n\\nDecision gate (by May 12):\\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full selective activation story is empirically supported. Proceed to Phase 1.\\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\\n\\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\\n\\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\\n\\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases.\\n\\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\\n\\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\\n\\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\\n\\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\\n\\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\\n\\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1} and θ ∈ {0.5, 0.7} to trace the accuracy-efficiency frontier (reduced from full grid to fit within compute budget).\\n\\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\\n\\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\\n\\nZero-shot claim gate:\\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\\n\\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\\n\\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: The primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1'). The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding. NOTE: DiT4DiT's ablation (Figure 8b, about action denoising steps — not τ_v) is NOT cited as corroborating evidence for P1; mimic-video's main text alone anchors this prediction.\\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\\n\\n[CRITICAL PARETO HONESTY REQUIREMENT] If P1 is confirmed (the expected outcome): CDR routes the majority of frames to τ_v=1. Mean τ_v consumed by CDR stays close to 1.0. Per-inference GPU compute savings are SMALL (approximately 5–10%). The primary benefit CDR provides is: (1) TASK SUCCESS RECOVERY: +≥7.5pp zero-shot on SIMPLER-Bridge vs. τ_v=1; (2) DEPLOYMENT CALIBRATION SAVINGS: eliminates 10 offline rollouts per new task required to identify optimal fixed τ_v. The abstract, introduction, and Phase 3 results section MUST state this explicitly. The Pareto curve axis framing should reflect this: if P1 confirmed, the x-axis showing 'mean τ_v consumed' will show CDR close to τ_v=1 with small compute savings; the y-axis showing task success will show the +≥7.5pp gain. This is still a Pareto win (same compute, better performance) but is NOT primarily an efficiency contribution — it is a zero-shot deployment automation contribution that recovers task success without offline rollout cost.\\n\\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR recovers per-task oracle gains zero-shot — same inference compute, +≥7.5pp task success, zero offline calibration rollouts.'\\n\\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim — if confirmed, CDR also delivers genuine per-inference compute savings. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\\n\\nBaselines:\\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\\n(e) Per-observation CDR (full system)\\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\\n\\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. LIBERO-100 results reported secondarily for comparability. Key empirical claims:\\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: same inference compute as τ_v=1, +≥7.5pp task success, zero offline calibration rollouts — when P1 confirmed, the compute savings (mean τ_v consumed below 1.0) are modest but the task success gain is the primary result\\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in 3D WAMs\\n\\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks; the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\\n\\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story). [RoboCasa results and full per-phase heatmap ablations are explicitly dropped from CoRL submission to stay within compute budget — these move to ICLR 2027 extended version if applicable.]\\n\\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in 3D WAMs (Phase 1 study) and the zero-shot deployment automation that eliminates offline calibration rollouts, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\\n\\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default)\\n- Phase 2 router training + 80/20 held-out validation result\\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge\\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time'; (2) zero-shot per-task CDR on SIMPLER-Bridge eliminating 10 offline calibration rollouts; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\\n\\n**Timeline for CoRL 2026 (May 29 deadline):**\\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\\n- Phase 0 gate decision: May 12\\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\\n- Zero-shot claim gate decision: May 19\\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation)\\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\\n- Buffer: May 29 submission\\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines, NO RoboCasa; ~20h buffer for reruns)\",\n      \"gpu_utilization\": \"45–55% effective — GPUs idle during Phase 0 gate decision, phase annotation, zero-shot gate decision, and result inspection\",\n      \"timeline\": \"2–3 weeks to CoRL submission (if Phase 0 positive by May 12); 2–3 months to ICLR 2027 otherwise\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$305 (122h × $2.49/hr spot H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~93 H100-hours\",\n      \"gpu_utilization\": \"65–75% — agent runs Phase 1 while human reviews Phase 0 gate; Phase 2 queued immediately after Phase 1 labels available; 80/20 validation runs in parallel with router training\",\n      \"timeline\": \"12–15 days to CoRL submission (Phase 0 gate on day 2, Phase 1 complete day 9, Phase 2 zero-shot gate day 10, Phase 3 complete day 15)\",\n      \"team\": \"1 researcher, ~20 min/day check-in\",\n      \"claude_api_cost\": \"~$100–200 (~1,000–2,000 turns at $0.10/turn Opus 4.7)\",\n      \"estimated_gpu_cost\": \"~$232 (93h × $2.49/hr spot H100)\",\n      \"risk_note\": \"Two critical decision points: (1) Phase 0 gate by May 12 — if <10% activation frames, reframe to zero-shot per-task routing, target ICLR 2027. (2) Phase 2 zero-shot gate by May 19 — if 80/20 LIBERO held-out validation fails (<80% τ_v* recovery), reframe primary zero-shot claim to few-shot SIMPLER-Bridge adaptation before committing it in the paper. Human judgment at both gates is essential. If Phase 1 takes 8 days (upper bound), MVS track is the fallback — dropping per-observation CDR and full ablations to submit the Phase 1 histograms + per-task CDR + pre-registered prediction result. Critical path has no slack beyond MVS; prioritize per-task CDR zero-shot result over per-observation CDR in Phase 3.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~150–175 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 55h; Phase 2 with reduced λ×θ grid (λ∈{0.01,0.1} × θ∈{0.5,0.7}) plus 80/20 validation: 8h; Phase 3 SIMPLER-Bridge + LIBERO primary results only — NO RoboCasa, NO full per-phase heatmap ablations: 70h; buffer: 15h). SCOPE REDUCTION vs. prior 410H estimate: RoboCasa evaluation dropped, full 3×3 λ×θ hyperparameter grid dropped (reduced to 2×2), extensive per-phase heatmap ablations moved to ICLR 2027 extended version. This fits within the ≤200H project constraint.\",\n      \"gpu_utilization\": \"Near-zero idle — phases pipelined\",\n      \"timeline\": \"3–5 days with 8 H100s\",\n      \"team\": \"0 (only initial sweep grid and eval harness setup required)\",\n      \"claude_api_cost\": \"~$200–400 (~2,000–4,000 turns)\",\n      \"estimated_gpu_cost\": \"~$410 (165h × $2.49/hr spot H100)\",\n      \"risk_note\": \"Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections. Auto mode must NOT interpret CDR's benefit as 'inference-time compute savings' if P1 is confirmed — the honest framing is 'deployment calibration cost savings (10 rollouts → 0) and task success recovery (+≥7.5pp), with mean τ_v consumed remaining close to 1.0.'\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)\",\n    \"ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I does NOT include a fixed-global-τ_v sweep — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining\",\n    \"LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge\",\n    \"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.\",\n    \"A₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model (arXiv:2604.05672, April 2026) — MUST CITE as concurrent work; applies per-observation Inter-Layer Truncated Flow Matching with early exit for VLA backbone computation, achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION: A₁ targets how many transformer layers to execute in a VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth routing) — orthogonal efficiency axes on different model families (VLAs vs WAMs).\",\n    \"VADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) — adapts ACTION diffusion denoising steps per task stage (shorter for simple, longer for complex); evaluated on Push-T, Adroit, ARX5; DIFFERENTIATION: VADF targets action denoising steps, CDR targets video backbone denoising depth (τ_v) — orthogonal efficiency axes, combinable\",\n    \"Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (arXiv:2603.30043) — 2D commitment motivation: video diffusion commits high-level plan in first few denoising steps; CDR extends and empirically validates for 3D manipulation video backbones\",\n    \"DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control (arXiv:2603.10448) — CDR cites as structural analogy only; DiT4DiT's ablation (Figure 8b) shows that fewer ACTION denoising steps yield higher task success — this is about action diffusion steps, NOT τ_v (video noise level). IMPORTANT: DiT4DiT does NOT corroborate τ_v=1 video noise optimality — these are orthogonal efficiency axes. CDR's related work may note: 'DiT4DiT finds fewer action denoising steps improve task success in the action domain; we investigate the analogous question in the video backbone domain.' Any language claiming DiT4DiT 'independently confirms' high-τ_v video optimality is FACTUALLY INCORRECT and must not appear in the paper. 98.6% LIBERO, 50.8% RoboCasa.\",\n    \"DreamZero: World Action Models are Zero-shot Policies (arXiv:2602.15922, Feb 2026) — velocity caching within denoising trajectory; complementary to CDR (reduces cost within a fixed τ_v level vs. CDR selecting τ_v level before denoising begins)\",\n    \"Denoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) — introduces Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions advance denoising earlier, harder regions receive more steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory frames — which frames need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined. Cited as feasibility motivation only; evaluates image generation, not robot action models.\",\n    \"MotuBrain (arXiv:2604.27792) — unified VAM with Mixture-of-Transformers (MoT) architecture under UniDiffuser formulation; supports policy learning, world modeling, video generation, inverse dynamics; 95.8%+ on RoboTwin 2.0; 50× speedup via step reduction, FP8 quantization. DIFFERENTIATION: training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on frozen mimic-video checkpoint requiring no retraining. Orthogonal — MotuBrain could serve as future CDR base model.\",\n    \"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (arXiv:2508.06804) — adapts ACTION (not video) denoising steps via RL; orthogonal efficiency axis to CDR\",\n    \"S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight (arXiv:2603.16195, Mar 2026) — distillation-based efficiency; requires retraining\",\n    \"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694) — X-WAM; fixed-distribution ANS baseline; not per-observation adaptive\",\n    \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv:2504.02792) — UWM; fixed schedule baseline\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078) — distillation-based; different efficiency axis; 99.2% LIBERO, 62.1% RoboCasa\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv:2605.06222) — introduces per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing\"\n  ],\n  \"description\": \"This paper investigates when World Action Models (WAMs) need video: the first systematic empirical study of per-observation optimal denoising depth (τ_v*) across LIBERO-100, with manipulation-phase breakdown, followed by a zero-shot router that automates per-task τ_v selection without offline calibration rollouts.\\n\\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view where τ_v is selected independently per task. These are compatible: τ_v=1 wins when one fixed value is applied globally (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption). The +9.4pp per-task sweep gain (46.9%→56.3% on SIMPLER-Bridge) quantifies the gap. The zero-shot router closes this gap without the 10-rollout per-task sweep cost.\\n\\nCRITICAL PARETO FRAMING (enforced throughout): When pre-registered prediction P1 is confirmed (the expected outcome per mimic-video main text), CDR routes most frames to τ_v=1, keeping mean τ_v consumed close to 1.0. Per-inference compute savings are small (5–10%). CDR's primary benefits are: (1) TASK SUCCESS RECOVERY — +≥7.5pp zero-shot on SIMPLER-Bridge; (2) DEPLOYMENT CALIBRATION SAVINGS — eliminating 10 offline rollouts per new task. The paper DOES NOT claim large per-inference speedups when P1 is confirmed. This distinction is stated explicitly in the abstract and introduction to prevent reviewer disappointment.\\n\\nTwo pre-registered predictions before Phase 3: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text. If P1 confirmed, CDR's Pareto claim is: same inference compute, +≥7.5pp task success, zero offline calibration rollouts. (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\\n\\nThe primary empirical contribution is Phase 1: first systematic study of τ_v* (per-observation optimal denoising depth) across LIBERO-100 with manipulation-phase breakdown — answering for the first time which 3D manipulation phases need video denoising below τ_v=1. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot per-task generalization, not the central architectural novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point.\\n\\nDiT4DiT (arXiv:2603.10448) is cited as structural analogy only: its ablation (Figure 8b) shows fewer action denoising steps improve task success in the action domain — a parallel finding that less denoising can be globally preferable. DiT4DiT does NOT corroborate τ_v=1 video noise optimality directly; these are orthogonal efficiency axes and must not be conflated.\\n\\nThe paper explicitly frames: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing contribution. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.\",\n  \"project_name\": \"commit_depth_router\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Missing mimic-video (arXiv 2512.15692, Dec 2025): This paper introduces partial denoising for video-action models with a fixed τ_v, empirically sweeps noise levels, and finds τ_v=1 (maximum noise, single forward pass) is the best default for manipulation. This is the direct prior art for CDR's core mechanism and is entirely absent from the Generator's landscape. Reviewers will view CDR's per-sample adaptation as incremental relative to this.\", \"CRITICAL — Missing DreamZero (arXiv 2602.15922, Feb 2026): DreamZero uses cosine-similarity-based velocity caching to reduce effective DiT steps from 16→4 in a WAM, achieving 38× total speedup. This is an adaptive WAM step-reduction method that the Generator does not cite or differentiate against.\", \"CRITICAL — Action decoder distribution shift: DiT4DiT's action decoder is trained to take features from a single, fixed video noise level (the forward-hook timestep). Running this frozen decoder on intermediate hidden states from 10 different noise levels during CDR's calibration sweep will yield features outside the training distribution, making the per-sample optimum labels unreliable. Addressing this requires fine-tuning the action decoder across multiple noise levels, which would substantially increase the compute budget.\", \"MAJOR — ChEaP generalization is an unverified assumption: ChEaP (arXiv 2603.30043) demonstrates early trajectory commitment in 2D maze-solving only. The Generator treats this as established fact for 3D robot manipulation, but 3D manipulation requires fine-grained 6-DoF actions that may not be committed early in the diffusion trajectory. This empirical validation step (showing commitment exists and is task-specific in 3D manipulation WAMs) is actually a significant contribution that the Generator treats as motivation rather than as a required result.\", \"MAJOR — If τ_v=1 already works best (mimic-video finding), CDR's entire premise weakens: CDR assumes the optimal video noise level varies meaningfully per observation. But mimic-video shows that the highest noise level (no denoising, trivial single pass) is the best default for action extraction in manipulation — meaning the 'commitment phenomenon' may not produce meaningful variation across observations, making per-sample routing unnecessary.\", \"MODERATE — Compute budget is tight and likely underestimated: 30 H100-hours for the calibration sweep (10 noise levels × LIBERO-100 × ≥50 demos per task × full action decoder rollouts) is optimistic. Actual cost depends on whether evaluation is parallelized per environment instance, and LIBERO simulation evaluation is single-threaded per instance as acknowledged.\", \"MODERATE — CoRL 2026 deadline discrepancy: The Generator states abstract deadline May 25/paper May 28; the actual CoRL 2026 deadlines are abstract May 26/paper May 29. This is minor but suggests the Generator may be working from cached information.\", \"MODERATE — The Pareto loss formulation (L = (1 − success_at_t*) + λ·(t*/T)) trains the router with a convex combination of two objectives, but success_at_t* is a non-differentiable reward requiring policy rollouts or a surrogate. The training procedure for the router is underspecified regarding how this gradient flows.\"]\nFeedback: CDR addresses a real efficiency gap in WAMs but needs two major revisions before it can be competitive at CoRL 2026:\n\n1. **Cite and differentiate against mimic-video and DreamZero.** mimic-video (arXiv 2512.15692) already shows that stopping video denoising at an intermediate noise level τ_v is beneficial for action extraction and empirically sweeps τ_v values. CDR must be framed as: 'mimic-video shows fixed τ_v works; we show per-sample adaptive τ_v yields further Pareto improvements.' DreamZero (arXiv 2602.15922) must be cited as an adaptive step-reduction baseline.\n\n2. **Address the action decoder distribution shift.** CDR cannot run a frozen DiT4DiT action decoder on features from arbitrary noise levels without retraining. Two viable paths: (a) Fine-tune the action decoder jointly across 3–5 noise levels during the CDR calibration phase (adds ~20–40 H100-hours but fixes the distribution shift); or (b) Reframe CDR as working on mimic-video-style architectures where the action decoder is already designed to handle variable-τ_v inputs — this is the cleaner path since mimic-video's τ_v is fixed and CDR adds per-sample adaptation.\n\n3. **Empirically validate commitment in 3D manipulation.** Add a section showing that intermediate features in DiT4DiT or a similar WAM actually carry sufficient action information before full denoising, as a function of task complexity. This turns the key assumption into a publishable finding. If the data shows commitment is task-uniform (all tasks commit at the same depth), CDR's per-sample routing argument collapses — which is important to know before the deadline.\n\n4. **Sharpen the differentiation from mimic-video.** The cleanest pitch: 'mimic-video sets τ_v globally. We show that per-task and per-observation optimal τ_v varies by 2–5× (empirical result), and a 2-layer MLP router recovers 97% of per-sample-optimal performance at near-zero overhead.' If the empirical variation is small, the paper weakens significantly, so validate this first.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Missing LingBot-VA (arXiv 2601.21998, RSS 2026): LingBot-VA introduces Noisy History Augmentation, training the action decoder on partially noisy video latents and enabling fixed τ_v=0.5 inference-time halving — achieving 98.5% on LIBERO. This is the most directly overlapping prior work with CDR's core mechanism (action decoding from intermediate noisy video). The Generator's landscape claims 'no existing VAM paper learns to predict per-observation optimal τ_v automatically' — true, but LingBot-VA already demonstrates the key enabling mechanism (action decoding from noisy video) with a fixed threshold. CDR must differentiate: LingBot-VA sets a universal fixed τ_v=0.5 globally; CDR learns per-observation optimal τ_v adaptively. This differentiation is valid but must be made explicit. LingBot-VA should be added as a primary baseline in Phase 3.\", \"MAJOR — Fast-WAM (arXiv 2603.16666) directly undermines CDR's narrative: Fast-WAM shows that eliminating test-time video prediction entirely is competitive with imagine-then-execute WAMs (4× speedup, no performance loss on LIBERO/RoboTwin). This creates a competing solution to CDR's efficiency goal: skip video at test time entirely rather than route its depth per-observation. The paper acknowledges Fast-WAM but does not address the implication that the field is moving toward eliminating test-time video rather than optimizing how much of it to run. CDR needs an explicit argument for why adaptive routing is preferable to the skip-entirely approach — e.g., showing CDR outperforms Fast-WAM on precision tasks or 6-DoF grasp tasks where some visual grounding is needed.\", \"MAJOR — mimic-video base model is ~4-6pp below current SOTA on LIBERO: mimic-video achieves 93.9% on LIBERO (Spatial/Object/Goal average), while LingBot-VA (98.5%), DiT4DiT (98.6%), and Being-H0.7 (99.2%) are significantly higher. Even with CDR's per-observation routing, CDR's absolute LIBERO numbers will likely remain below these baselines. Reviewers will question why CDR builds on a weaker base, and will interpret CDR's improvements over τ_v=1 baseline as optimization within a sub-SOTA architecture rather than advancing the field. CDR needs to address this positioning explicitly — either by explaining why mimic-video's variable-τ_v property makes it the correct base (which is true), or by computing CDR's improvement as the Pareto gain relative to the fixed-τ_v cost-performance frontier.\", \"MODERATE — Phase 1 compute estimate (~15 H100-hours) may be optimistic: LIBERO-100 (5,000 demos × ~100 steps × 11 τ_v levels) requires ~5.5M video backbone forward passes for the action reconstruction sweep. With proper batching on Cosmos-Predict2 (2B parameter DiT), 30-60 H100-hours is a more conservative estimate. This is still within the 200-hour budget but should be revised in the resource estimate.\", \"MODERATE — If per-observation τ_v variation is small (Phase 1 outcome B), the router's Pareto gain over LingBot-VA's fixed τ_v=0.5 is unclear: LingBot-VA already shows that a fixed τ_v=0.5 universally halves steps with no loss. If CDR's Phase 1 shows that most frames benefit from τ_v ≥ 0.9 (close to τ_v=1), and only grasp phases benefit from lower τ_v, the average speedup from CDR may be modest (e.g., 10-15% above LingBot-VA's fixed halving), making the contribution marginal relative to the added router complexity.\"]\nFeedback: CDR's Round 1 revisions were excellent — distribution shift, deadline accuracy, differentiable loss, and DreamZero/mimic-video citations are all resolved. Two structural additions are needed before CoRL submission:\n\n**1. Add LingBot-VA as primary baseline and differentiate.**\nLingBot-VA (arXiv 2601.21998, accepted RSS 2026) introduces Noisy History Augmentation — training the action decoder on partially noisy video at τ_v∈[0.5,1.0] and using fixed τ_v=0.5 at inference, halving steps without performance loss (98.5% LIBERO). This is CDR's closest competitor. The differentiation is: LingBot-VA applies a universal fixed threshold τ_v=0.5; CDR routes per-observation because different manipulation phases may need different thresholds. Add LingBot-VA to Phase 3 as baseline (d) and make the adaptive-vs-fixed comparison a first-class result. The Pareto curve (task success vs. mean τ_v) directly addresses this comparison.\n\n**2. Address the Fast-WAM tension in Section 1/2.**\nFast-WAM shows that skipping test-time video entirely is competitive (4× speedup). CDR should argue that adaptive routing fills the gap between 'always use full video' and 'skip video entirely' — i.e., CDR selects per-observation whether video features help (especially for grasp phases where spatial precision matters). If Phase 1 shows commitment exists, add an explicit ablation comparing CDR vs. Fast-WAM on grasp-critical tasks.\n\n**3. Reframe the positioning: mimic-video base vs. SOTA absolute performance.**\nAcknowledge upfront that mimic-video (CDR's base) is behind LingBot-VA/DiT4DiT/Being-H0.7 on absolute LIBERO metrics. The paper's contribution is about efficiency-performance tradeoffs, not absolute task success. Lead with the Pareto curve as the primary result, not the task success number. A direct comparison CDR vs. LingBot-VA-style fixed τ_v=0.5 (same base, different routing strategy) is more informative than comparing against architectures with different training data and backbones.\n\n**4. Phase 1 compute budget should be revised to 30-60 H100-hours** for the LIBERO-100 τ_v sweep (5,000 demos × 11 noise levels). This is still within the 200-hour budget.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — τ_v=0 is the wrong Phase 1 reference: mimic-video's paper (verified by WebFetch on arXiv:2512.15692) explicitly states that τ_v=0 (fully denoised video) gives WORSE policy performance than intermediate τ_v values, and τ_v=1 (pure noise, no video denoising) is the best single global default on SIMPLER-Bridge. CDR defines τ_v* = min{τ_v : ||a_{τ_v} − a_{τ_v=0}||₂ ≤ δ}, which targets convergence with a suboptimal operating point. Routing toward τ_v=0 can actively degrade performance relative to the baseline (τ_v=1), making the router counterproductive. Fix: replace the reference with per-observation action error vs. ground truth (||a_{τ_v} − a_GT||₂ using LIBERO demo GT actions), or define τ_v* as convergence to the per-task optimal τ_v (already estimated by mimic-video's sweep), not τ_v=0.\", \"CRITICAL — The core hypothesis conflicts with mimic-video's global-optimum finding: mimic-video reports τ_v=1.0 (single forward pass, no video generation) as the best global default for autonomous policy performance on SIMPLER-Bridge — the same benchmark CDR foregrounds as its primary showcase. If τ_v=1.0 is already globally optimal, then CDR's hypothesis that 'grasp/insert phases need τ_v≈0.3' means the router would systematically push those frames toward a worse operating point. CDR must explain and address this contradiction before submitting; the paper currently cites the +9.4pp per-task gain as motivation but does not engage with mimic-video's per-task sweep showing that the global optimal is at the highest-noise end.\", \"MAJOR — Demo-vs-rollout distribution shift in Phase 1: Phase 1 labels τ_v* on human demonstration states from LIBERO-100 (expert teleop). During closed-loop evaluation the robot visits recovery states, partial-success configurations, and states outside the demonstration support. A router trained on demo-state labels has no guarantee of correct τ_v routing on the novel states seen during closed-loop rollouts — exactly the states where wrong τ_v routing would harm performance most. The paper does not address this distribution gap.\", \"MAJOR — Deadline pressure makes pre-validation essential but is not acknowledged: CDR explicitly frames Phase 1 as an empirical question with uncertain outcome ('both outcomes publishable'). With 19 days to the full-paper deadline (May 29), there is no time to run Phase 1 (30–60 H100-hours), discover the wrong reference, fix it, re-run Phase 1, train the router, and evaluate on LIBERO+SIMPLER-Bridge. The paper should be pre-validated — run Phase 1 immediately and inspect the τ_v* distribution before committing. If τ_v* clusters above 0.8 for all frames (consistent with the global τ_v=1 finding), the paper's story collapses.\", \"MODERATE — Fallback framing ('validation study + per-task routing') is below CoRL bar: CoRL accepts ~22% of submissions in a highly competitive WAM-dense cycle. A paper whose main contribution degrades to '3D commitment validation + automated zero-shot per-task routing' (when per-observation variation < 1pp) is unlikely to cross the acceptance threshold, because zero-shot per-task routing via a frozen 512-dim MLP is architecturally trivial and the validation study alone is more suited to a workshop. Both outcomes must be made independently compelling, or the paper should be conditioned on a positive Phase 1 result.\", \"MODERATE — Absolute LIBERO numbers below SOTA undermines reviewer confidence: CDR built on mimic-video (93.9% LIBERO) versus LingBot-VA (98.5%) and DiT4DiT (98.6%) creates a 4.7pp gap that no router can close without base-model improvement. Reviewers at CoRL, seeing absolute numbers rather than Pareto curves in the abstract, will downweight CDR vs. papers that achieve both efficiency and SOTA accuracy. The paper must lead with SIMPLER-Bridge (where the mimic-video base is competitive and the per-task gain is large) rather than LIBERO in the abstract and intro.\"]\nFeedback: CDR enters Round 3 with its prior critical issues genuinely resolved — LingBot-VA added as primary baseline, mimic-video distribution shift fixed by reframing to use its variable-τ_v decoder, Pareto framing cleanly differentiated from Fast-WAM, compute revised to 30–60 H100-hours for Phase 1. But two previously unknown issues now emerge from independent verification of mimic-video's actual findings:\n\n**Top priority fix (do before anything else):** The Phase 1 reference τ_v=0 is empirically wrong. mimic-video's paper (arXiv:2512.15692, verified) states that τ_v=0 (fully denoised video) gives worse policy performance than intermediate τ_v, and the best single global default on SIMPLER-Bridge is τ_v=1.0 (no video denoising). CDR's proxy ε_τ = ||a_{τ_v} − a_{τ_v=0}||₂ therefore measures 'convergence to a suboptimal point.' Fix Phase 1 to use per-observation action error vs. ground truth (||a_{τ_v} − a_GT||₂, available from LIBERO demos), or define τ_v* as the minimum τ_v that converges to within δ of the per-task optimal τ_v (which mimic-video already sweeps). This is the most important technical correction and must be done before any other Phase 1 computation.\n\n**Second priority (validates the entire premise):** Run a quick Phase 0 sanity check (1–2 H100-hours): take 5 LIBERO tasks and 2–3 demo trajectories, sweep τ_v={1.0, 0.9, ..., 0.3} using the corrected GT reference, and inspect whether per-phase τ_v* shows >2pp within-episode variation. If grasp frames and approach frames cluster at the same τ_v*, the CDR adaptive story does not materialize and the paper should be reframed before committing to the CoRL deadline.\n\n**Third priority (narrative):** Move SIMPLER-Bridge to the primary benchmark in the abstract and intro. LIBERO absolute numbers (94–96% vs. SOTA 98.5%) will hurt reviews; SIMPLER-Bridge is where mimic-video's per-task variation is pronounced (+9.4pp) and where CDR's per-observation extension is most defensible. Explicitly note in the intro that LIBERO results are presented for comparability but the core efficiency-performance trade-off is shown on SIMPLER-Bridge.\n\n**Fallback strengthening:** If per-observation variation is small, the fallback 'automated zero-shot per-task routing' needs a real numerical result to be CoRL-ready: show the MLP router (trained on LIBERO) correctly predicts per-task optimal τ_v on held-out tasks from SIMPLER-Bridge (zero-shot) and recovers ≥80% of the per-task sweep gain (+9.4pp) without offline rollouts. That specific claim is publishable at CoRL as an efficiency-of-deployment contribution.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE — Fast-WAM SIMPLER-Bridge gap: Fast-WAM (arXiv:2603.16666) reports results only on LIBERO and RoboTwin in the abstract and appears not to evaluate on SIMPLER-Bridge. The proposal's Phase 3 plans to compare CDR against a 'Fast-WAM-style' baseline on SIMPLER-Bridge but this requires either (a) running Fast-WAM's architecture on mimic-video's SIMPLER-Bridge setup or (b) using τ_v=1 as a proxy for Fast-WAM's behavior — the proposal conflates these. τ_v=1 in mimic-video is NOT architecturally equivalent to Fast-WAM: τ_v=1 still processes noisy future frames through the full backbone, while Fast-WAM modifies architecture to not generate future frames. The paper must clearly state which 'Fast-WAM-style' baseline is being run and how it is implemented on the mimic-video backbone.\", \"MODERATE — 'Denoising, Fast and Slow' mischaracterized as 'per-sample difficulty routing': WebFetch of arXiv:2604.19141 confirms this CVPR 2026 paper does PATCH-LEVEL spatial routing within images (varying timesteps across image regions), NOT per-sample routing across observations in a trajectory. The proposal describes it as 'per-sample difficulty routing in image diffusion — supports CDR's feasibility argument.' This mischaracterization is relatively minor but CoRL reviewers familiar with the paper will catch it. More importantly, the differentiation from CDR is actually cleaner than the proposal implies: CDR is temporal routing across trajectory timesteps; 'Denoising Fast and Slow' is spatial routing across image patches. The proposal should make this distinction explicit.\", \"MODERATE — τ_v=1 global optimality claim is stated as 'foundational verified' but the WebFetch of the mimic-video HTML only confirmed that the scratch (no per-task tuning) result is 46.9%, not that τ_v=1 specifically is the best single fixed τ_v among all possible fixed values. The paper states 'performance peaks at an INTERMEDIATE noise level' per-task; if a fixed global τ_v=0.8 outperforms τ_v=1 on SIMPLER-Bridge aggregate, CDR's 'τ_v=1 as globally optimal default' framing collapses. This must be verified from Table I or Figure 5 of mimic-video before committing to this framing.\", \"MODERATE — 20-day critical path has zero slack for Phase 1 overruns: Phase 0 decision on May 12 + Phase 1 (5–8 days on 8 H100s) + Phase 2 (1 day) + Phase 3 (6 days) + Writing (4 days) = 16–19 days to May 28-29 submission. If Phase 1 takes 8 days (upper bound of 60h / 8 GPUs), writing is compressed to 2 days or Phase 3 is cut. The proposal should explicitly acknowledge that Phase 3 ablations (RoboCasa, per-phase heatmaps) are drop-able if Phase 1 runs long, and that the minimum viable submission needs only SIMPLER-Bridge primary results.\", \"MINOR — MotuBrain (arXiv:2604.27792) is unaddressed: MotuBrain biases video timestep sampling toward noisier regions during training to improve robustness under noisy visual conditions — this is related to CDR's study of τ_v sensitivity. While MotuBrain is a training-time technique and CDR is a test-time router, reviewers may conflate them. CDR's landscape should acknowledge MotuBrain briefly as a training-time complementary approach vs. CDR's test-time routing.\", \"MINOR — SIMPLER-Bridge is mimic-video's primary benchmark but is not universally known in the CoRL community: if the majority of reviewers are primarily familiar with LIBERO (the most common WAM benchmark), leading with SIMPLER-Bridge scores (where CDR's base 46.9% looks weak in absolute terms) may create a poor first impression. The abstract should explicitly state '46.9% is the state-of-the-art on this task for models of this size' or note that SIMPLER-Bridge is evaluation on real-to-sim transfer tasks where most methods score <55%.\"]\nFeedback: Round 4 correctly resolves all Round 3 critical issues: the τ_v=0 reference has been replaced with GT actions (||a_{τ_v} − a_GT||₂), τ_v=1 is reframed as globally optimal default, distribution shift is mitigated via 50% non-expert rollout states, Phase 0 is a proper gate, and the fallback has concrete numerical targets (≥80% sweep gain recovery). The proposal is now scientifically sound and structurally well-organized. Three focused fixes are needed for Round 5:\n\n**Fix 1 (highest priority — 30 min)**: Verify from mimic-video Table I / Figure 5 that τ_v=1.0 specifically is the best among ALL fixed τ_v values globally (not just 'no per-task tuning'). If the global best is τ_v=0.8 or 0.9, revise the framing to 'near-τ_v=1 region is globally optimal' and adjust CDR's conservative-routing fallback accordingly. This is the entire premise — it must be confirmed with the exact quote and figure number from the paper.\n\n**Fix 2 (clarity — 20 min)**: Correct the 'Denoising, Fast and Slow' characterization from 'per-sample difficulty routing' to 'per-PATCH spatial difficulty routing' and rewrite the differentiation: 'CDR operates in the temporal domain (which trajectory frames need video denoising), while Denoising Fast and Slow operates in the spatial domain (which image patches need more denoising steps). These are orthogonal axes and could in principle be combined.' This turns a potential reviewer objection into a positive contribution statement.\n\n**Fix 3 (baseline specification — 1 day)**: In Phase 3 baseline (e), specify exactly what 'Fast-WAM-style' means on mimic-video backbone: is it (i) running mimic-video with only the first observation frame as video input and zeros for future frames, or (ii) using τ_v=1 as a proxy? Clarify this is NOT the published Fast-WAM model (different architecture), but rather a mimic-video ablation that disables future video usage, implementing the spirit of Fast-WAM post-hoc. This prevents reviewers from thinking CDR is being unfairly compared against a strawman.\n\n**Opportunistic improvement**: If Phase 0 runs TODAY (May 10) and shows ≥20% activation frames clustered in grasp phases, add a 1-paragraph 'Phase 0 Sanity Check Result' section to the paper with the preliminary histogram. This is publishable supporting evidence that CDR's empirical premise is confirmed, and it addresses the biggest risk reviewers will identify when reading the proposal.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — OA-WAM (arXiv:2605.06481, May 7 2026) is uncited but evaluates on both LIBERO (97.8%) and SimplerEnv (79.3%). CDR must cite OA-WAM in related work. More importantly: OA-WAM's 79.3% SimplerEnv vs. CDR's base 46.9% SIMPLER-Bridge will prompt reviewers to ask why CDR doesn't use a stronger base. CDR must explicitly note whether 'SimplerEnv 79.3%' and 'SIMPLER-Bridge 46.9%' are the same evaluation split — if OA-WAM evaluates on all SimplerEnv tasks (not just Bridge), the numbers are not directly comparable and CDR needs to state this clearly in the paper.\", \"MODERATE — Zero-shot LIBERO→SIMPLER-Bridge generalization claim (≥80% of +9.4pp recovery) is still unvalidated and carries high empirical risk. LIBERO tasks (simulated tabletop with 3D rendered objects) and SIMPLER-Bridge (real-to-sim BridgeData transfer with different visual domain) have substantially different task distributions. A router MLP trained on CLIP+language embeddings from LIBERO may not generalize to BridgeData task embeddings zero-shot. CDR should pre-validate this claim in Phase 0 by running the task-level τ_v MLP on a held-out LIBERO task set and verifying ≥80% recovery before committing it as a primary CoRL claim.\", \"MODERATE — Implicit assumption that fixed τ_v < 1 baselines (Phase 3 baselines b,c) will underperform τ_v=1 on SIMPLER-Bridge is not acknowledged as a testable prediction. Mimic-video states τ_v=1 is the best global autonomous default on SIMPLER-Bridge (noise-as-augmentation effect), implying LingBot-VA-style fixed τ_v=0.5/0.7/0.9 may underperform the 46.9% baseline on SIMPLER. CDR should make this a formal pre-registered prediction in Phase 3 and explicitly note: if fixed intermediate τ_v baselines (b,c) all underperform τ_v=1, CDR's Pareto comparison is primarily against (a) τ_v=1 and the per-task sweep oracle — LingBot-VA's approach is not a Pareto competitor on this benchmark.\", \"MINOR — A₁ (arXiv:2604.05672, April 2026) proposes adaptive per-observation early-exit truncated flow matching for VLAs with dynamic denoising depth per observation — similar spirit to CDR's per-observation routing but targeting VLAs via layer-truncation rather than video τ_v routing. CDR should add one sentence noting A₁ as an orthogonal approach: 'Concurrent work (A₁, arXiv:2604.05672) applies per-observation adaptive truncation to VLA action generation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes.'\", \"MINOR — The timeline risk from Phase 1 upper bound (8 days on 8 H100s) compressing writing to 2 days is acknowledged but not adequately mitigated. If Phase 1 takes 8 days (May 12-20), Phase 3 cannot complete before May 26. CDR should explicitly define a 'minimum viable submission' (MVS) track: Phase 0 positive result + Phase 1 τ_v* distribution histograms + per-task CDR router on SIMPLER-Bridge (Phase 2+3 partial) constitutes a submittable paper even without full Phase 3 ablations, as long as the Pareto curve includes at least τ_v=1 baseline, fixed τ_v=0.7, and per-task CDR.\"]\nFeedback: CDR has resolved all critical issues from Rounds 1-4: τ_v=0 reference replaced with GT actions, Denoising Fast and Slow correctly characterized as spatial/patch-level routing, Fast-WAM baseline correctly specified as τ_v=1 proxy (not the published model), MotuBrain acknowledged as orthogonal, and timeline drop-able ablations flagged. The scientific framing is now verified against mimic-video: Figure 5 does show performance peaks at intermediate τ_v, and τ_v=1 is confirmed as the best global autonomous default (noise-as-augmentation effect). CDR's Pareto story is internally consistent and scientifically sound.\n\nThree focused fixes for Round 6:\n\n**Fix 1 (1 hour): Cite OA-WAM and clarify SimplerEnv vs SIMPLER-Bridge.** OA-WAM (arXiv:2605.06481) evaluates on SimplerEnv (79.3%) and LIBERO (97.8%) — reviewers will notice the gap with CDR's 46.9% SIMPLER-Bridge base. Add one sentence: 'OA-WAM (2605.06481) addresses object identity robustness in WAMs; CDR addresses adaptive video denoising depth — orthogonal.' Then explicitly note in the experimental section whether SimplerEnv and SIMPLER-Bridge are the same split; if not, state that direct comparison against OA-WAM is not applicable.\n\n**Fix 2 (Phase 0 addition, run ASAP): Pre-validate zero-shot LIBERO→SIMPLER-Bridge router.** Before finalizing the ≥80% recovery claim as a primary CoRL contribution, validate it in Phase 0 or Phase 1: take a frozen MLP trained on task embeddings from 80 LIBERO-100 tasks, test zero-shot on 20 held-out LIBERO tasks, verify ≥80% τ_v* recovery. If this holds on held-out LIBERO tasks, the SIMPLER-Bridge zero-shot claim is credible. If not, reframe to 'per-task routing with fine-tuning on 3 SIMPLER tasks' rather than zero-shot.\n\n**Fix 3 (framing, 30 min): Pre-register the fixed τ_v < 1 underperformance prediction.** In Phase 3, explicitly state: 'We predict baselines (b,c) — LingBot-VA-style fixed τ_v=0.5/0.7/0.9 — will underperform baseline (a) τ_v=1 on SIMPLER-Bridge due to the noise-as-augmentation regularization effect documented in mimic-video. If this prediction is confirmed, CDR's Pareto comparison is against (a) and the per-task sweep oracle, not against uniform partial denoising approaches.' This pre-registration turns a potential negative result (baseline (b,c) worse than τ_v=1) into a publishable confirmation of CDR's theoretical premise.\n\n**Optional (1 hour): Add A₁ one-sentence cite.** 'Concurrent work (arXiv:2604.05672) applies per-observation adaptive truncation to VLA action generation via inter-layer early exit; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal.'\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MODERATE — mimic-video Figure 5 is cited misleadingly: CDR claims 'Figure 5 shows aggregate performance peaks at an intermediate noise level (not at τ_v=1)' — this reflects the figure *caption* only. The mimic-video main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest flow time τ_v=1.' These are internally contradictory in the source paper, and reviewers reading the main text will perceive CDR as misrepresenting mimic-video. CDR must cite the figure caption specifically ('mimic-video Figure 5 caption states: performance peaks at an intermediate noise level') AND acknowledge that the main text separately concludes τ_v=1 is the best fixed global choice. The reconciliation is straightforward — Figure 5 shows oracle per-task optimal τ_v is at intermediate levels, while τ_v=1 is the best fixed-global-τ_v — but CDR must make this explicit or reviewers will flag it in every review.\", \"MODERATE — The pre-registered prediction that 'fixed τ_v < 1 baselines will underperform τ_v=1' is now strongly supported by mimic-video's *main text* conclusion (τ_v=1 is best autonomous performance). If this prediction is confirmed in Phase 3, CDR's Pareto comparison becomes primarily CDR vs. τ_v=1 baseline — LingBot-VA-style uniform partial denoising is not a Pareto competitor on SIMPLER-Bridge. CDR should elevate this framing: 'Our pre-registered prediction is that LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge; CDR's contribution is Pareto dominance over the τ_v=1 default via selective routing.' If confirmed, the paper becomes a cleaner story but with a narrower competitive comparison than currently implied.\", \"MINOR — The core novelty claim ('no existing VAM paper has empirically studied which manipulation phases benefit from τ_v < 1') is valid but the architectural contribution (2-layer MLP router) is thin for CoRL 2026's competitive WAM track. The Phase 1 empirical study is the genuine contribution; CDR should foreground it as 'the first empirical characterization of video necessity by manipulation phase in 3D WAMs' rather than leading with the routing mechanism.\"]\nFeedback: CDR has resolved all Round 5 issues and is scientifically well-structured. One focused fix is needed before submission:\n\n**Fix 1 (required, 30 minutes): Correct the mimic-video Figure 5 citation.** Replace 'Figure 5 shows aggregate performance peaks at an intermediate noise level (not at τ_v=1)' with 'mimic-video Figure 5 caption reports that performance peaks at an intermediate noise level; the paper's main text separately concludes that τ_v=1 achieves the best fixed-global autonomous policy performance on SIMPLER-Bridge. These findings are reconcilable: the oracle per-task optimal τ_v is intermediate (Figure 5 caption), while the best fixed-global τ_v is τ_v=1 (main text). CDR exploits this gap: a lightweight router approximates the per-observation oracle, recovering gains that a fixed-global τ_v=1 leaves on the table.' This specific reconciliation should appear verbatim in the intro, and the phrase 'aggregate performance peaks at an intermediate noise level' must be removed from all sections where it appears without the Figure 5 caption attribution. Reviewers who have read mimic-video carefully will catch this without the fix.\n\n**Fix 2 (framing, 20 minutes): Elevate the pre-registered prediction as the paper's anchor claim.** Since mimic-video's main text already supports the prediction that uniform τ_v<1 underperforms τ_v=1, CDR's Pareto claim is effectively: CDR vs. τ_v=1 baseline (not CDR vs. LingBot-VA). Make this the headline: 'We show that LingBot-VA-style uniform partial denoising is not a valid Pareto competitor on SIMPLER-Bridge (pre-registered and confirmed), and CDR Pareto-dominates the τ_v=1 fixed-global default by selectively routing only frames that require lower τ_v.' This is a cleaner and more defensible Pareto claim than the current framing.\n\nWith these two changes, CDR is ready for CoRL submission. The MVS track is well-defined, the zero-shot validation gates are appropriately scoped, and the related-work section is comprehensive. The paper's contribution — the first empirical study of manipulation-phase τ_v requirements plus zero-shot per-task routing — is modest but publishable at CoRL if the Phase 1 histograms show meaningful phase-specific variation.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE — DiT4DiT ablation is factually mischaracterized: Independent verification of arXiv:2603.10448 confirms that DiT4DiT's 'single-step is best' ablation (Figure 8b) concerns ACTION DENOISING STEPS (fewer action diffusion steps yield higher success), not τ_v (video noise level). CDR's landscape states: 'DiT4DiT ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding.' This conflates two different efficiency axes (action denoising steps vs. video noise level). Reviewers familiar with DiT4DiT will flag this. Fix: either remove DiT4DiT as corroborating evidence for τ_v=1 optimality, or rewrite as 'DiT4DiT finds that fewer action denoising steps improve performance — a parallel finding that the high-noise, low-denoising regime is preferable, supporting CDR's premise that less denoising is often better.' Do NOT use DiT4DiT to directly corroborate mimic-video's τ_v=1 result.\", \"MODERATE — Pareto efficiency claim is potentially misleading if P1 is confirmed: If P1 is confirmed (fixed intermediate τ_v < 1 uniformly underperforms τ_v=1 on SIMPLER-Bridge), then CDR's router will route the vast majority of frames to τ_v=1 (since τ_v=1 is the best single fixed value). The resulting 'compute savings' from CDR — measured as reduction in mean τ_v consumed below 1 — will be small (perhaps 5–10% of full video generation cost). The Pareto win is primarily in task SUCCESS (+≥7.5pp from zero-shot per-task routing), not in compute efficiency. The paper's abstract and intro must be honest about this: 'CDR's Pareto dominance is primarily measured in task success recovery, not compute savings, if the pre-registered P1 prediction is confirmed. The mean τ_v consumed by CDR remains close to 1 when P1 holds.' Misrepresenting the Pareto win as efficiency-driven when most frames route to τ_v=1 will trigger reviewer pushback.\", \"MODERATE — Auto-mode resource estimate (410 H100-hours) exceeds the ≤200 H100-hour budget constraint stated in user requirements. The manual estimate (115–135H) is within budget, but auto mode at 410H is 2-3× over the stated limit. Either: (a) cap the auto-mode scope to fit within 200H by dropping full RoboCasa, per-phase heatmap ablations, and the full λ×θ grid search; or (b) explicitly acknowledge in the proposal that auto-mode exceeds the 200H constraint and requires expanded budget authorization.\", \"MINOR — 'When to Trust Imagination' (arXiv:2605.06222) is misdescribed as 'reduces replanning frequency'; verified content shows it uses a per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution — not episode-level replanning reduction. The orthogonality claim holds, but the description should be corrected to 'per-chunk adaptive replanning trigger' to avoid misleading reviewers.\", \"MINOR — Method contribution is architecturally thin for CoRL 2026's WAM track: The 2-layer MLP router (512-dim CLIP + 512-dim language → 256-dim hidden → 4-class softmax) is not a novel architecture. CoRL 2026's WAM submissions include DiT4DiT, MotuBrain, OA-WAM with substantial architectural innovation. CDR must foreground Phase 1 (first empirical characterization of manipulation-phase τ_v requirements) as the primary scientific contribution — the router is the deployment mechanism, not the contribution. The paper title 'Commitment Depth Routing' implies a routing method is the contribution; consider retitling to reflect the empirical study: e.g., 'When Do World Action Models Need Video? A Manipulation-Phase Study with Selective Denoising Activation.'\"]\nFeedback: CDR has fixed all prior critical issues through Round 6. The Round 7 proposal is now scientifically well-structured with explicit gates, correct mimic-video Figure 5 reconciliation, pre-registered predictions, and MVS fallback. Three focused fixes are required before CoRL submission:\n\n**Fix 1 (required, 30 minutes): Correct DiT4DiT characterization.** DiT4DiT's ablation (Figure 8b in arXiv:2603.10448) is about action denoising steps — not τ_v (video noise level). CDR incorrectly uses it to corroborate 'high τ_v is best on SIMPLER-Bridge.' Rewrite as: 'DiT4DiT finds that a single action denoising step outperforms multi-step action diffusion — a parallel finding that less denoising in the action domain also improves performance; we observe the same pattern in the video domain with mimic-video's τ_v=1 result.' Remove any language claiming DiT4DiT 'independently confirms' that high video noise τ_v is optimal.\n\n**Fix 2 (required, 20 minutes): Honestly bound the Pareto efficiency claim.** If P1 is confirmed (the expected outcome based on mimic-video main text), CDR routes most frames to τ_v=1, making compute savings modest. Add explicit language in the abstract and intro: 'CDR's primary Pareto benefit is task success recovery (≥7.5pp zero-shot on SIMPLER-Bridge), not compute efficiency — most frames continue to use τ_v=1, with video activation selectively applied only to frames where the Phase 1 study identifies τ_v* < 1.' This prevents reviewers from expecting large speedups and finding only 5-10% compute savings.\n\n**Fix 3 (budget reconciliation, 10 minutes): Cap auto-mode estimate.** The auto mode at 410 H100-hours violates the ≤200H project constraint. Either (a) reduce auto-mode scope to 150-180H (drop RoboCasa, full hyperparameter grid) while keeping the key SIMPLER-Bridge experiments, or (b) add a note that auto-mode exceeds the budget constraint and requires pre-authorization. The manual mode (115-135H) is within budget and should be the reference for the 200H limit.\n\n**Optional (strengthens paper): Retitle to foreground empirical contribution.** 'Commitment Depth Routing' implies a novel routing mechanism as the primary contribution. The actual primary contribution is Phase 1 — the first empirical study of which manipulation phases need τ_v < 1 in 3D WAMs. A title like 'When Does Robot Policy Need Video? Manipulation-Phase Analysis and Selective Activation for World Action Models' better positions the paper as an empirical methods contribution and reduces reviewer expectations of architectural novelty.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:30:44.042Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:30:44.042Z",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-10T09:30:44.070Z_

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

## Idea under review (round 8/10)
{
  "title": "When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation",
  "core_problem": "Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. This paper exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\n\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\n\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical; (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. This paper addresses the third cost: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task oracle justifies it, and eliminate the 10-rollout-per-task deployment calibration cost via a zero-shot router trained on LIBERO-100.\n\nCRITICAL PARETO FRAMING CLARIFICATION (required for reviewer accuracy): If the pre-registered prediction P1 is confirmed (fixed intermediate τ_v < 1 underperforms τ_v=1 on SIMPLER-Bridge — the expected outcome per mimic-video main text), then the zero-shot router routes the MAJORITY of frames to τ_v=1. This means: (a) mean τ_v consumed by CDR stays CLOSE TO 1.0; (b) per-inference GPU compute savings are SMALL (5–10% at most); (c) the primary benefit is TASK SUCCESS RECOVERY (+≥7.5pp zero-shot on SIMPLER-Bridge) and DEPLOYMENT CALIBRATION SAVINGS (10 offline rollouts per new task → 0). The abstract and introduction MUST state this explicitly. CDR's Pareto dominance vs. τ_v=1 is: same or slightly lower mean τ_v consumed, significantly higher task success — not a large speedup per inference call.\n\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.",
  "opportunity": "The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. This paper exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\n\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. The primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost.\n\nCRITICAL: THE DEPLOYMENT EFFICIENCY GAIN IS CALIBRATION COST, NOT PER-INFERENCE COMPUTE. When P1 is confirmed (the expected outcome), CDR routes most frames to τ_v=1, keeping mean τ_v close to 1.0. The efficiency improvement CDR delivers is: eliminating the 10-offline-rollout per-task sweep required to find the optimal fixed τ_v for a new task. A new task can be deployed with ZERO rollouts using the zero-shot router, rather than requiring 10 rollouts to calibrate the best fixed τ_v. This is a real and practically important contribution — robotics deployments accumulate many new tasks, and even at 10 rollouts each, calibration cost is significant — but it is DIFFERENT from 'faster inference per call.' The paper's framing must be explicit: 'CDR saves deployment calibration cost (10 rollouts → 0 per new task) and recovers task success (+≥7.5pp zero-shot), not primarily per-inference GPU compute.'\n\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, this paper also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies the competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. The Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the tasks/frames that need it, without any offline rollout cost.'\n\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. deployment-calibration-rollouts Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\n\nThe primary scientific contribution is Phase 1: the FIRST empirical characterization of which 3D manipulation phases require video denoising below the τ_v=1 fixed-global default, using GT-action-referenced τ_v labeling across LIBERO-100. The zero-shot router is the deployment mechanism enabling practical use of Phase 1's findings without offline sweeps — not the architectural novelty. The paper should be read as an empirical methods contribution, not an architectural one.",
  "landscape": "LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is the primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\n\nmimic-video (arXiv:2512.15692, Dec 2025) is the base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — this paper's contribution is approximating the per-task oracle via zero-shot routing; (d) per-task sweep yields +9.4pp (46.9%→56.3%), confirming the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\n\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\n\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\n\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\n\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\n\nDiT4DiT (arXiv:2603.10448) ablation (Figure 8b): fewer ACTION denoising steps yield higher task success — this finding concerns the action diffusion process, NOT τ_v (video noise level). These are orthogonal efficiency axes. CDR cites DiT4DiT only as a structural analogy: in both the action domain (DiT4DiT) and the video domain (mimic-video τ_v=1 main-text finding), less denoising tends to be preferable as a global default. CDR does NOT use DiT4DiT to corroborate τ_v=1 video noise optimality; these are different axes and conflating them would be factually incorrect. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\n\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\n\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\n\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) introduces a per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing.\n\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.",
  "approach": "CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\n\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\n\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\n\nDecision gate (by May 12):\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full selective activation story is empirically supported. Proceed to Phase 1.\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\n\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\n\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\n\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases.\n\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\n\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\n\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\n\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\n\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\n\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1} and θ ∈ {0.5, 0.7} to trace the accuracy-efficiency frontier (reduced from full grid to fit within compute budget).\n\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\n\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\n\nZero-shot claim gate:\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\n\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\n\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: The primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1'). The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding. NOTE: DiT4DiT's ablation (Figure 8b, about action denoising steps — not τ_v) is NOT cited as corroborating evidence for P1; mimic-video's main text alone anchors this prediction.\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\n\n[CRITICAL PARETO HONESTY REQUIREMENT] If P1 is confirmed (the expected outcome): CDR routes the majority of frames to τ_v=1. Mean τ_v consumed by CDR stays close to 1.0. Per-inference GPU compute savings are SMALL (approximately 5–10%). The primary benefit CDR provides is: (1) TASK SUCCESS RECOVERY: +≥7.5pp zero-shot on SIMPLER-Bridge vs. τ_v=1; (2) DEPLOYMENT CALIBRATION SAVINGS: eliminates 10 offline rollouts per new task required to identify optimal fixed τ_v. The abstract, introduction, and Phase 3 results section MUST state this explicitly. The Pareto curve axis framing should reflect this: if P1 confirmed, the x-axis showing 'mean τ_v consumed' will show CDR close to τ_v=1 with small compute savings; the y-axis showing task success will show the +≥7.5pp gain. This is still a Pareto win (same compute, better performance) but is NOT primarily an efficiency contribution — it is a zero-shot deployment automation contribution that recovers task success without offline rollout cost.\n\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR recovers per-task oracle gains zero-shot — same inference compute, +≥7.5pp task success, zero offline calibration rollouts.'\n\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim — if confirmed, CDR also delivers genuine per-inference compute savings. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\n\nBaselines:\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\n(e) Per-observation CDR (full system)\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\n\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. LIBERO-100 results reported secondarily for comparability. Key empirical claims:\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: same inference compute as τ_v=1, +≥7.5pp task success, zero offline calibration rollouts — when P1 confirmed, the compute savings (mean τ_v consumed below 1.0) are modest but the task success gain is the primary result\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in 3D WAMs\n\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks; the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\n\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story). [RoboCasa results and full per-phase heatmap ablations are explicitly dropped from CoRL submission to stay within compute budget — these move to ICLR 2027 extended version if applicable.]\n\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in 3D WAMs (Phase 1 study) and the zero-shot deployment automation that eliminates offline calibration rollouts, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\n\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default)\n- Phase 2 router training + 80/20 held-out validation result\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time'; (2) zero-shot per-task CDR on SIMPLER-Bridge eliminating 10 offline calibration rollouts; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\n\n**Timeline for CoRL 2026 (May 29 deadline):**\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\n- Phase 0 gate decision: May 12\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\n- Zero-shot claim gate decision: May 19\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation)\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\n- Buffer: May 29 submission\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines, NO RoboCasa; ~20h buffer for reruns)",
      "gpu_utilization": "45–55% effective — GPUs idle during Phase 0 gate decision, phase annotation, zero-shot gate decision, and result inspection",
      "timeline": "2–3 weeks to CoRL submission (if Phase 0 positive by May 12); 2–3 months to ICLR 2027 otherwise",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$305 (122h × $2.49/hr spot H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~93 H100-hours",
      "gpu_utilization": "65–75% — agent runs Phase 1 while human reviews Phase 0 gate; Phase 2 queued immediately after Phase 1 labels available; 80/20 validation runs in parallel with router training",
      "timeline": "12–15 days to CoRL submission (Phase 0 gate on day 2, Phase 1 complete day 9, Phase 2 zero-shot gate day 10, Phase 3 complete day 15)",
      "team": "1 researcher, ~20 min/day check-in",
      "claude_api_cost": "~$100–200 (~1,000–2,000 turns at $0.10/turn Opus 4.7)",
      "estimated_gpu_cost": "~$232 (93h × $2.49/hr spot H100)",
      "risk_note": "Two critical decision points: (1) Phase 0 gate by May 12 — if <10% activation frames, reframe to zero-shot per-task routing, target ICLR 2027. (2) Phase 2 zero-shot gate by May 19 — if 80/20 LIBERO held-out validation fails (<80% τ_v* recovery), reframe primary zero-shot claim to few-shot SIMPLER-Bridge adaptation before committing it in the paper. Human judgment at both gates is essential. If Phase 1 takes 8 days (upper bound), MVS track is the fallback — dropping per-observation CDR and full ablations to submit the Phase 1 histograms + per-task CDR + pre-registered prediction result. Critical path has no slack beyond MVS; prioritize per-task CDR zero-shot result over per-observation CDR in Phase 3."
    },
    "auto_research": {
      "gpu_hours": "~150–175 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 55h; Phase 2 with reduced λ×θ grid (λ∈{0.01,0.1} × θ∈{0.5,0.7}) plus 80/20 validation: 8h; Phase 3 SIMPLER-Bridge + LIBERO primary results only — NO RoboCasa, NO full per-phase heatmap ablations: 70h; buffer: 15h). SCOPE REDUCTION vs. prior 410H estimate: RoboCasa evaluation dropped, full 3×3 λ×θ hyperparameter grid dropped (reduced to 2×2), extensive per-phase heatmap ablations moved to ICLR 2027 extended version. This fits within the ≤200H project constraint.",
      "gpu_utilization": "Near-zero idle — phases pipelined",
      "timeline": "3–5 days with 8 H100s",
      "team": "0 (only initial sweep grid and eval harness setup required)",
      "claude_api_cost": "~$200–400 (~2,000–4,000 turns)",
      "estimated_gpu_cost": "~$410 (165h × $2.49/hr spot H100)",
      "risk_note": "Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections. Auto mode must NOT interpret CDR's benefit as 'inference-time compute savings' if P1 is confirmed — the honest framing is 'deployment calibration cost savings (10 rollouts → 0) and task success recovery (+≥7.5pp), with mean τ_v consumed remaining close to 1.0.'"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)",
    "ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)"
  ],
  "level": "solid",
  "key_references": [
    "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I does NOT include a fixed-global-τ_v sweep — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining",
    "LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge",
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.",
    "A₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model (arXiv:2604.05672, April 2026) — MUST CITE as concurrent work; applies per-observation Inter-Layer Truncated Flow Matching with early exit for VLA backbone computation, achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION: A₁ targets how many transformer layers to execute in a VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth routing) — orthogonal efficiency axes on different model families (VLAs vs WAMs).",
    "VADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) — adapts ACTION diffusion denoising steps per task stage (shorter for simple, longer for complex); evaluated on Push-T, Adroit, ARX5; DIFFERENTIATION: VADF targets action denoising steps, CDR targets video backbone denoising depth (τ_v) — orthogonal efficiency axes, combinable",
    "Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (arXiv:2603.30043) — 2D commitment motivation: video diffusion commits high-level plan in first few denoising steps; CDR extends and empirically validates for 3D manipulation video backbones",
    "DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control (arXiv:2603.10448) — CDR cites as structural analogy only; DiT4DiT's ablation (Figure 8b) shows that fewer ACTION denoising steps yield higher task success — this is about action diffusion steps, NOT τ_v (video noise level). IMPORTANT: DiT4DiT does NOT corroborate τ_v=1 video noise optimality — these are orthogonal efficiency axes. CDR's related work may note: 'DiT4DiT finds fewer action denoising steps improve task success in the action domain; we investigate the analogous question in the video backbone domain.' Any language claiming DiT4DiT 'independently confirms' high-τ_v video optimality is FACTUALLY INCORRECT and must not appear in the paper. 98.6% LIBERO, 50.8% RoboCasa.",
    "DreamZero: World Action Models are Zero-shot Policies (arXiv:2602.15922, Feb 2026) — velocity caching within denoising trajectory; complementary to CDR (reduces cost within a fixed τ_v level vs. CDR selecting τ_v level before denoising begins)",
    "Denoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) — introduces Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions advance denoising earlier, harder regions receive more steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory frames — which frames need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined. Cited as feasibility motivation only; evaluates image generation, not robot action models.",
    "MotuBrain (arXiv:2604.27792) — unified VAM with Mixture-of-Transformers (MoT) architecture under UniDiffuser formulation; supports policy learning, world modeling, video generation, inverse dynamics; 95.8%+ on RoboTwin 2.0; 50× speedup via step reduction, FP8 quantization. DIFFERENTIATION: training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on frozen mimic-video checkpoint requiring no retraining. Orthogonal — MotuBrain could serve as future CDR base model.",
    "D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (arXiv:2508.06804) — adapts ACTION (not video) denoising steps via RL; orthogonal efficiency axis to CDR",
    "S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight (arXiv:2603.16195, Mar 2026) — distillation-based efficiency; requires retraining",
    "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694) — X-WAM; fixed-distribution ANS baseline; not per-observation adaptive",
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv:2504.02792) — UWM; fixed schedule baseline",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078) — distillation-based; different efficiency axis; 99.2% LIBERO, 62.1% RoboCasa",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv:2605.06222) — introduces per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing"
  ],
  "description": "This paper investigates when World Action Models (WAMs) need video: the first systematic empirical study of per-observation optimal denoising depth (τ_v*) across LIBERO-100, with manipulation-phase breakdown, followed by a zero-shot router that automates per-task τ_v selection without offline calibration rollouts.\n\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view where τ_v is selected independently per task. These are compatible: τ_v=1 wins when one fixed value is applied globally (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption). The +9.4pp per-task sweep gain (46.9%→56.3% on SIMPLER-Bridge) quantifies the gap. The zero-shot router closes this gap without the 10-rollout per-task sweep cost.\n\nCRITICAL PARETO FRAMING (enforced throughout): When pre-registered prediction P1 is confirmed (the expected outcome per mimic-video main text), CDR routes most frames to τ_v=1, keeping mean τ_v consumed close to 1.0. Per-inference compute savings are small (5–10%). CDR's primary benefits are: (1) TASK SUCCESS RECOVERY — +≥7.5pp zero-shot on SIMPLER-Bridge; (2) DEPLOYMENT CALIBRATION SAVINGS — eliminating 10 offline rollouts per new task. The paper DOES NOT claim large per-inference speedups when P1 is confirmed. This distinction is stated explicitly in the abstract and introduction to prevent reviewer disappointment.\n\nTwo pre-registered predictions before Phase 3: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text. If P1 confirmed, CDR's Pareto claim is: same inference compute, +≥7.5pp task success, zero offline calibration rollouts. (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\n\nThe primary empirical contribution is Phase 1: first systematic study of τ_v* (per-observation optimal denoising depth) across LIBERO-100 with manipulation-phase breakdown — answering for the first time which 3D manipulation phases need video denoising below τ_v=1. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot per-task generalization, not the central architectural novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point.\n\nDiT4DiT (arXiv:2603.10448) is cited as structural analogy only: its ablation (Figure 8b) shows fewer action denoising steps improve task success in the action domain — a parallel finding that less denoising can be globally preferable. DiT4DiT does NOT corroborate τ_v=1 video noise optimality directly; these are orthogonal efficiency axes and must not be conflated.\n\nThe paper explicitly frames: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing contribution. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.",
  "project_name": "commit_depth_router",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — Missing mimic-video (arXiv 2512.15692, Dec 2025): This paper introduces partial denoising for video-action models with a fixed τ_v, empirically sweeps noise levels, and finds τ_v=1 (maximum noise, single forward pass) is the best default for manipulation. This is the direct prior art for CDR's core mechanism and is entirely absent from the Generator's landscape. Reviewers will view CDR's per-sample adaptation as incremental relative to this.", "CRITICAL — Missing DreamZero (arXiv 2602.15922, Feb 2026): DreamZero uses cosine-similarity-based velocity caching to reduce effective DiT steps from 16→4 in a WAM, achieving 38× total speedup. This is an adaptive WAM step-reduction method that the Generator does not cite or differentiate against.", "CRITICAL — Action decoder distribution shift: DiT4DiT's action decoder is trained to take features from a single, fixed video noise level (the forward-hook timestep). Running this frozen decoder on intermediate hidden states from 10 different noise levels during CDR's calibration sweep will yield features outside the training distribution, making the per-sample optimum labels unreliable. Addressing this requires fine-tuning the action decoder across multiple noise levels, which would substantially increase the compute budget.", "MAJOR — ChEaP generalization is an unverified assumption: ChEaP (arXiv 2603.30043) demonstrates early trajectory commitment in 2D maze-solving only. The Generator treats this as established fact for 3D robot manipulation, but 3D manipulation requires fine-grained 6-DoF actions that may not be committed early in the diffusion trajectory. This empirical validation step (showing commitment exists and is task-specific in 3D manipulation WAMs) is actually a significant contribution that the Generator treats as motivation rather than as a required result.", "MAJOR — If τ_v=1 already works best (mimic-video finding), CDR's entire premise weakens: CDR assumes the optimal video noise level varies meaningfully per observation. But mimic-video shows that the highest noise level (no denoising, trivial single pass) is the best default for action extraction in manipulation — meaning the 'commitment phenomenon' may not produce meaningful variation across observations, making per-sample routing unnecessary.", "MODERATE — Compute budget is tight and likely underestimated: 30 H100-hours for the calibration sweep (10 noise levels × LIBERO-100 × ≥50 demos per task × full action decoder rollouts) is optimistic. Actual cost depends on whether evaluation is parallelized per environment instance, and LIBERO simulation evaluation is single-threaded per instance as acknowledged.", "MODERATE — CoRL 2026 deadline discrepancy: The Generator states abstract deadline May 25/paper May 28; the actual CoRL 2026 deadlines are abstract May 26/paper May 29. This is minor but suggests the Generator may be working from cached information.", "MODERATE — The Pareto loss formulation (L = (1 − success_at_t*) + λ·(t*/T)) trains the router with a convex combination of two objectives, but success_at_t* is a non-differentiable reward requiring policy rollouts or a surrogate. The training procedure for the router is underspecified regarding how this gradient flows."]
Feedback: CDR addresses a real efficiency gap in WAMs but needs two major revisions before it can be competitive at CoRL 2026:

1. **Cite and differentiate against mimic-video and DreamZero.** mimic-video (arXiv 2512.15692) already shows that stopping video denoising at an intermediate noise level τ_v is beneficial for action extraction and empirically sweeps τ_v values. CDR must be framed as: 'mimic-video shows fixed τ_v works; we show per-sample adaptive τ_v yields further Pareto improvements.' DreamZero (arXiv 2602.15922) must be cited as an adaptive step-reduction baseline.

2. **Address the action decoder distribution shift.** CDR cannot run a frozen DiT4DiT action decoder on features from arbitrary noise levels without retraining. Two viable paths: (a) Fine-tune the action decoder jointly across 3–5 noise levels during the CDR calibration phase (adds ~20–40 H100-hours but fixes the distribution shift); or (b) Reframe CDR as working on mimic-video-style architectures where the action decoder is already designed to handle variable-τ_v inputs — this is the cleaner path since mimic-video's τ_v is fixed and CDR adds per-sample adaptation.

3. **Empirically validate commitment in 3D manipulation.** Add a section showing that intermediate features in DiT4DiT or a similar WAM actually carry sufficient action information before full denoising, as a function of task complexity. This turns the key assumption into a publishable finding. If the data shows commitment is task-uniform (all tasks commit at the same depth), CDR's per-sample routing argument collapses — which is important to know before the deadline.

4. **Sharpen the differentiation from mimic-video.** The cleanest pitch: 'mimic-video sets τ_v globally. We show that per-task and per-observation optimal τ_v varies by 2–5× (empirical result), and a 2-layer MLP router recovers 97% of per-sample-optimal performance at near-zero overhead.' If the empirical variation is small, the paper weakens significantly, so validate this first.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Missing LingBot-VA (arXiv 2601.21998, RSS 2026): LingBot-VA introduces Noisy History Augmentation, training the action decoder on partially noisy video latents and enabling fixed τ_v=0.5 inference-time halving — achieving 98.5% on LIBERO. This is the most directly overlapping prior work with CDR's core mechanism (action decoding from intermediate noisy video). The Generator's landscape claims 'no existing VAM paper learns to predict per-observation optimal τ_v automatically' — true, but LingBot-VA already demonstrates the key enabling mechanism (action decoding from noisy video) with a fixed threshold. CDR must differentiate: LingBot-VA sets a universal fixed τ_v=0.5 globally; CDR learns per-observation optimal τ_v adaptively. This differentiation is valid but must be made explicit. LingBot-VA should be added as a primary baseline in Phase 3.", "MAJOR — Fast-WAM (arXiv 2603.16666) directly undermines CDR's narrative: Fast-WAM shows that eliminating test-time video prediction entirely is competitive with imagine-then-execute WAMs (4× speedup, no performance loss on LIBERO/RoboTwin). This creates a competing solution to CDR's efficiency goal: skip video at test time entirely rather than route its depth per-observation. The paper acknowledges Fast-WAM but does not address the implication that the field is moving toward eliminating test-time video rather than optimizing how much of it to run. CDR needs an explicit argument for why adaptive routing is preferable to the skip-entirely approach — e.g., showing CDR outperforms Fast-WAM on precision tasks or 6-DoF grasp tasks where some visual grounding is needed.", "MAJOR — mimic-video base model is ~4-6pp below current SOTA on LIBERO: mimic-video achieves 93.9% on LIBERO (Spatial/Object/Goal average), while LingBot-VA (98.5%), DiT4DiT (98.6%), and Being-H0.7 (99.2%) are significantly higher. Even with CDR's per-observation routing, CDR's absolute LIBERO numbers will likely remain below these baselines. Reviewers will question why CDR builds on a weaker base, and will interpret CDR's improvements over τ_v=1 baseline as optimization within a sub-SOTA architecture rather than advancing the field. CDR needs to address this positioning explicitly — either by explaining why mimic-video's variable-τ_v property makes it the correct base (which is true), or by computing CDR's improvement as the Pareto gain relative to the fixed-τ_v cost-performance frontier.", "MODERATE — Phase 1 compute estimate (~15 H100-hours) may be optimistic: LIBERO-100 (5,000 demos × ~100 steps × 11 τ_v levels) requires ~5.5M video backbone forward passes for the action reconstruction sweep. With proper batching on Cosmos-Predict2 (2B parameter DiT), 30-60 H100-hours is a more conservative estimate. This is still within the 200-hour budget but should be revised in the resource estimate.", "MODERATE — If per-observation τ_v variation is small (Phase 1 outcome B), the router's Pareto gain over LingBot-VA's fixed τ_v=0.5 is unclear: LingBot-VA already shows that a fixed τ_v=0.5 universally halves steps with no loss. If CDR's Phase 1 shows that most frames benefit from τ_v ≥ 0.9 (close to τ_v=1), and only grasp phases benefit from lower τ_v, the average speedup from CDR may be modest (e.g., 10-15% above LingBot-VA's fixed halving), making the contribution marginal relative to the added router complexity."]
Feedback: CDR's Round 1 revisions were excellent — distribution shift, deadline accuracy, differentiable loss, and DreamZero/mimic-video citations are all resolved. Two structural additions are needed before CoRL submission:

**1. Add LingBot-VA as primary baseline and differentiate.**
LingBot-VA (arXiv 2601.21998, accepted RSS 2026) introduces Noisy History Augmentation — training the action decoder on partially noisy video at τ_v∈[0.5,1.0] and using fixed τ_v=0.5 at inference, halving steps without performance loss (98.5% LIBERO). This is CDR's closest competitor. The differentiation is: LingBot-VA applies a universal fixed threshold τ_v=0.5; CDR routes per-observation because different manipulation phases may need different thresholds. Add LingBot-VA to Phase 3 as baseline (d) and make the adaptive-vs-fixed comparison a first-class result. The Pareto curve (task success vs. mean τ_v) directly addresses this comparison.

**2. Address the Fast-WAM tension in Section 1/2.**
Fast-WAM shows that skipping test-time video entirely is competitive (4× speedup). CDR should argue that adaptive routing fills the gap between 'always use full video' and 'skip video entirely' — i.e., CDR selects per-observation whether video features help (especially for grasp phases where spatial precision matters). If Phase 1 shows commitment exists, add an explicit ablation comparing CDR vs. Fast-WAM on grasp-critical tasks.

**3. Reframe the positioning: mimic-video base vs. SOTA absolute performance.**
Acknowledge upfront that mimic-video (CDR's base) is behind LingBot-VA/DiT4DiT/Being-H0.7 on absolute LIBERO metrics. The paper's contribution is about efficiency-performance tradeoffs, not absolute task success. Lead with the Pareto curve as the primary result, not the task success number. A direct comparison CDR vs. LingBot-VA-style fixed τ_v=0.5 (same base, different routing strategy) is more informative than comparing against architectures with different training data and backbones.

**4. Phase 1 compute budget should be revised to 30-60 H100-hours** for the LIBERO-100 τ_v sweep (5,000 demos × 11 noise levels). This is still within the 200-hour budget.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL — τ_v=0 is the wrong Phase 1 reference: mimic-video's paper (verified by WebFetch on arXiv:2512.15692) explicitly states that τ_v=0 (fully denoised video) gives WORSE policy performance than intermediate τ_v values, and τ_v=1 (pure noise, no video denoising) is the best single global default on SIMPLER-Bridge. CDR defines τ_v* = min{τ_v : ||a_{τ_v} − a_{τ_v=0}||₂ ≤ δ}, which targets convergence with a suboptimal operating point. Routing toward τ_v=0 can actively degrade performance relative to the baseline (τ_v=1), making the router counterproductive. Fix: replace the reference with per-observation action error vs. ground truth (||a_{τ_v} − a_GT||₂ using LIBERO demo GT actions), or define τ_v* as convergence to the per-task optimal τ_v (already estimated by mimic-video's sweep), not τ_v=0.", "CRITICAL — The core hypothesis conflicts with mimic-video's global-optimum finding: mimic-video reports τ_v=1.0 (single forward pass, no video generation) as the best global default for autonomous policy performance on SIMPLER-Bridge — the same benchmark CDR foregrounds as its primary showcase. If τ_v=1.0 is already globally optimal, then CDR's hypothesis that 'grasp/insert phases need τ_v≈0.3' means the router would systematically push those frames toward a worse operating point. CDR must explain and address this contradiction before submitting; the paper currently cites the +9.4pp per-task gain as motivation but does not engage with mimic-video's per-task sweep showing that the global optimal is at the highest-noise end.", "MAJOR — Demo-vs-rollout distribution shift in Phase 1: Phase 1 labels τ_v* on human demonstration states from LIBERO-100 (expert teleop). During closed-loop evaluation the robot visits recovery states, partial-success configurations, and states outside the demonstration support. A router trained on demo-state labels has no guarantee of correct τ_v routing on the novel states seen during closed-loop rollouts — exactly the states where wrong τ_v routing would harm performance most. The paper does not address this distribution gap.", "MAJOR — Deadline pressure makes pre-validation essential but is not acknowledged: CDR explicitly frames Phase 1 as an empirical question with uncertain outcome ('both outcomes publishable'). With 19 days to the full-paper deadline (May 29), there is no time to run Phase 1 (30–60 H100-hours), discover the wrong reference, fix it, re-run Phase 1, train the router, and evaluate on LIBERO+SIMPLER-Bridge. The paper should be pre-validated — run Phase 1 immediately and inspect the τ_v* distribution before committing. If τ_v* clusters above 0.8 for all frames (consistent with the global τ_v=1 finding), the paper's story collapses.", "MODERATE — Fallback framing ('validation study + per-task routing') is below CoRL bar: CoRL accepts ~22% of submissions in a highly competitive WAM-dense cycle. A paper whose main contribution degrades to '3D commitment validation + automated zero-shot per-task routing' (when per-observation variation < 1pp) is unlikely to cross the acceptance threshold, because zero-shot per-task routing via a frozen 512-dim MLP is architecturally trivial and the validation study alone is more suited to a workshop. Both outcomes must be made independently compelling, or the paper should be conditioned on a positive Phase 1 result.", "MODERATE — Absolute LIBERO numbers below SOTA undermines reviewer confidence: CDR built on mimic-video (93.9% LIBERO) versus LingBot-VA (98.5%) and DiT4DiT (98.6%) creates a 4.7pp gap that no router can close without base-model improvement. Reviewers at CoRL, seeing absolute numbers rather than Pareto curves in the abstract, will downweight CDR vs. papers that achieve both efficiency and SOTA accuracy. The paper must lead with SIMPLER-Bridge (where the mimic-video base is competitive and the per-task gain is large) rather than LIBERO in the abstract and intro."]
Feedback: CDR enters Round 3 with its prior critical issues genuinely resolved — LingBot-VA added as primary baseline, mimic-video distribution shift fixed by reframing to use its variable-τ_v decoder, Pareto framing cleanly differentiated from Fast-WAM, compute revised to 30–60 H100-hours for Phase 1. But two previously unknown issues now emerge from independent verification of mimic-video's actual findings:

**Top priority fix (do before anything else):** The Phase 1 reference τ_v=0 is empirically wrong. mimic-video's paper (arXiv:2512.15692, verified) states that τ_v=0 (fully denoised video) gives worse policy performance than intermediate τ_v, and the best single global default on SIMPLER-Bridge is τ_v=1.0 (no video denoising). CDR's proxy ε_τ = ||a_{τ_v} − a_{τ_v=0}||₂ therefore measures 'convergence to a suboptimal point.' Fix Phase 1 to use per-observation action error vs. ground truth (||a_{τ_v} − a_GT||₂, available from LIBERO demos), or define τ_v* as the minimum τ_v that converges to within δ of the per-task optimal τ_v (which mimic-video already sweeps). This is the most important technical correction and must be done before any other Phase 1 computation.

**Second priority (validates the entire premise):** Run a quick Phase 0 sanity check (1–2 H100-hours): take 5 LIBERO tasks and 2–3 demo trajectories, sweep τ_v={1.0, 0.9, ..., 0.3} using the corrected GT reference, and inspect whether per-phase τ_v* shows >2pp within-episode variation. If grasp frames and approach frames cluster at the same τ_v*, the CDR adaptive story does not materialize and the paper should be reframed before committing to the CoRL deadline.

**Third priority (narrative):** Move SIMPLER-Bridge to the primary benchmark in the abstract and intro. LIBERO absolute numbers (94–96% vs. SOTA 98.5%) will hurt reviews; SIMPLER-Bridge is where mimic-video's per-task variation is pronounced (+9.4pp) and where CDR's per-observation extension is most defensible. Explicitly note in the intro that LIBERO results are presented for comparability but the core efficiency-performance trade-off is shown on SIMPLER-Bridge.

**Fallback strengthening:** If per-observation variation is small, the fallback 'automated zero-shot per-task routing' needs a real numerical result to be CoRL-ready: show the MLP router (trained on LIBERO) correctly predicts per-task optimal τ_v on held-out tasks from SIMPLER-Bridge (zero-shot) and recovers ≥80% of the per-task sweep gain (+9.4pp) without offline rollouts. That specific claim is publishable at CoRL as an efficiency-of-deployment contribution.

### Round 4 review
Verdict: revise
Issues: ["MODERATE — Fast-WAM SIMPLER-Bridge gap: Fast-WAM (arXiv:2603.16666) reports results only on LIBERO and RoboTwin in the abstract and appears not to evaluate on SIMPLER-Bridge. The proposal's Phase 3 plans to compare CDR against a 'Fast-WAM-style' baseline on SIMPLER-Bridge but this requires either (a) running Fast-WAM's architecture on mimic-video's SIMPLER-Bridge setup or (b) using τ_v=1 as a proxy for Fast-WAM's behavior — the proposal conflates these. τ_v=1 in mimic-video is NOT architecturally equivalent to Fast-WAM: τ_v=1 still processes noisy future frames through the full backbone, while Fast-WAM modifies architecture to not generate future frames. The paper must clearly state which 'Fast-WAM-style' baseline is being run and how it is implemented on the mimic-video backbone.", "MODERATE — 'Denoising, Fast and Slow' mischaracterized as 'per-sample difficulty routing': WebFetch of arXiv:2604.19141 confirms this CVPR 2026 paper does PATCH-LEVEL spatial routing within images (varying timesteps across image regions), NOT per-sample routing across observations in a trajectory. The proposal describes it as 'per-sample difficulty routing in image diffusion — supports CDR's feasibility argument.' This mischaracterization is relatively minor but CoRL reviewers familiar with the paper will catch it. More importantly, the differentiation from CDR is actually cleaner than the proposal implies: CDR is temporal routing across trajectory timesteps; 'Denoising Fast and Slow' is spatial routing across image patches. The proposal should make this distinction explicit.", "MODERATE — τ_v=1 global optimality claim is stated as 'foundational verified' but the WebFetch of the mimic-video HTML only confirmed that the scratch (no per-task tuning) result is 46.9%, not that τ_v=1 specifically is the best single fixed τ_v among all possible fixed values. The paper states 'performance peaks at an INTERMEDIATE noise level' per-task; if a fixed global τ_v=0.8 outperforms τ_v=1 on SIMPLER-Bridge aggregate, CDR's 'τ_v=1 as globally optimal default' framing collapses. This must be verified from Table I or Figure 5 of mimic-video before committing to this framing.", "MODERATE — 20-day critical path has zero slack for Phase 1 overruns: Phase 0 decision on May 12 + Phase 1 (5–8 days on 8 H100s) + Phase 2 (1 day) + Phase 3 (6 days) + Writing (4 days) = 16–19 days to May 28-29 submission. If Phase 1 takes 8 days (upper bound of 60h / 8 GPUs), writing is compressed to 2 days or Phase 3 is cut. The proposal should explicitly acknowledge that Phase 3 ablations (RoboCasa, per-phase heatmaps) are drop-able if Phase 1 runs long, and that the minimum viable submission needs only SIMPLER-Bridge primary results.", "MINOR — MotuBrain (arXiv:2604.27792) is unaddressed: MotuBrain biases video timestep sampling toward noisier regions during training to improve robustness under noisy visual conditions — this is related to CDR's study of τ_v sensitivity. While MotuBrain is a training-time technique and CDR is a test-time router, reviewers may conflate them. CDR's landscape should acknowledge MotuBrain briefly as a training-time complementary approach vs. CDR's test-time routing.", "MINOR — SIMPLER-Bridge is mimic-video's primary benchmark but is not universally known in the CoRL community: if the majority of reviewers are primarily familiar with LIBERO (the most common WAM benchmark), leading with SIMPLER-Bridge scores (where CDR's base 46.9% looks weak in absolute terms) may create a poor first impression. The abstract should explicitly state '46.9% is the state-of-the-art on this task for models of this size' or note that SIMPLER-Bridge is evaluation on real-to-sim transfer tasks where most methods score <55%."]
Feedback: Round 4 correctly resolves all Round 3 critical issues: the τ_v=0 reference has been replaced with GT actions (||a_{τ_v} − a_GT||₂), τ_v=1 is reframed as globally optimal default, distribution shift is mitigated via 50% non-expert rollout states, Phase 0 is a proper gate, and the fallback has concrete numerical targets (≥80% sweep gain recovery). The proposal is now scientifically sound and structurally well-organized. Three focused fixes are needed for Round 5:

**Fix 1 (highest priority — 30 min)**: Verify from mimic-video Table I / Figure 5 that τ_v=1.0 specifically is the best among ALL fixed τ_v values globally (not just 'no per-task tuning'). If the global best is τ_v=0.8 or 0.9, revise the framing to 'near-τ_v=1 region is globally optimal' and adjust CDR's conservative-routing fallback accordingly. This is the entire premise — it must be confirmed with the exact quote and figure number from the paper.

**Fix 2 (clarity — 20 min)**: Correct the 'Denoising, Fast and Slow' characterization from 'per-sample difficulty routing' to 'per-PATCH spatial difficulty routing' and rewrite the differentiation: 'CDR operates in the temporal domain (which trajectory frames need video denoising), while Denoising Fast and Slow operates in the spatial domain (which image patches need more denoising steps). These are orthogonal axes and could in principle be combined.' This turns a potential reviewer objection into a positive contribution statement.

**Fix 3 (baseline specification — 1 day)**: In Phase 3 baseline (e), specify exactly what 'Fast-WAM-style' means on mimic-video backbone: is it (i) running mimic-video with only the first observation frame as video input and zeros for future frames, or (ii) using τ_v=1 as a proxy? Clarify this is NOT the published Fast-WAM model (different architecture), but rather a mimic-video ablation that disables future video usage, implementing the spirit of Fast-WAM post-hoc. This prevents reviewers from thinking CDR is being unfairly compared against a strawman.

**Opportunistic improvement**: If Phase 0 runs TODAY (May 10) and shows ≥20% activation frames clustered in grasp phases, add a 1-paragraph 'Phase 0 Sanity Check Result' section to the paper with the preliminary histogram. This is publishable supporting evidence that CDR's empirical premise is confirmed, and it addresses the biggest risk reviewers will identify when reading the proposal.

### Round 5 review
Verdict: revise
Issues: ["MODERATE — OA-WAM (arXiv:2605.06481, May 7 2026) is uncited but evaluates on both LIBERO (97.8%) and SimplerEnv (79.3%). CDR must cite OA-WAM in related work. More importantly: OA-WAM's 79.3% SimplerEnv vs. CDR's base 46.9% SIMPLER-Bridge will prompt reviewers to ask why CDR doesn't use a stronger base. CDR must explicitly note whether 'SimplerEnv 79.3%' and 'SIMPLER-Bridge 46.9%' are the same evaluation split — if OA-WAM evaluates on all SimplerEnv tasks (not just Bridge), the numbers are not directly comparable and CDR needs to state this clearly in the paper.", "MODERATE — Zero-shot LIBERO→SIMPLER-Bridge generalization claim (≥80% of +9.4pp recovery) is still unvalidated and carries high empirical risk. LIBERO tasks (simulated tabletop with 3D rendered objects) and SIMPLER-Bridge (real-to-sim BridgeData transfer with different visual domain) have substantially different task distributions. A router MLP trained on CLIP+language embeddings from LIBERO may not generalize to BridgeData task embeddings zero-shot. CDR should pre-validate this claim in Phase 0 by running the task-level τ_v MLP on a held-out LIBERO task set and verifying ≥80% recovery before committing it as a primary CoRL claim.", "MODERATE — Implicit assumption that fixed τ_v < 1 baselines (Phase 3 baselines b,c) will underperform τ_v=1 on SIMPLER-Bridge is not acknowledged as a testable prediction. Mimic-video states τ_v=1 is the best global autonomous default on SIMPLER-Bridge (noise-as-augmentation effect), implying LingBot-VA-style fixed τ_v=0.5/0.7/0.9 may underperform the 46.9% baseline on SIMPLER. CDR should make this a formal pre-registered prediction in Phase 3 and explicitly note: if fixed intermediate τ_v baselines (b,c) all underperform τ_v=1, CDR's Pareto comparison is primarily against (a) τ_v=1 and the per-task sweep oracle — LingBot-VA's approach is not a Pareto competitor on this benchmark.", "MINOR — A₁ (arXiv:2604.05672, April 2026) proposes adaptive per-observation early-exit truncated flow matching for VLAs with dynamic denoising depth per observation — similar spirit to CDR's per-observation routing but targeting VLAs via layer-truncation rather than video τ_v routing. CDR should add one sentence noting A₁ as an orthogonal approach: 'Concurrent work (A₁, arXiv:2604.05672) applies per-observation adaptive truncation to VLA action generation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes.'", "MINOR — The timeline risk from Phase 1 upper bound (8 days on 8 H100s) compressing writing to 2 days is acknowledged but not adequately mitigated. If Phase 1 takes 8 days (May 12-20), Phase 3 cannot complete before May 26. CDR should explicitly define a 'minimum viable submission' (MVS) track: Phase 0 positive result + Phase 1 τ_v* distribution histograms + per-task CDR router on SIMPLER-Bridge (Phase 2+3 partial) constitutes a submittable paper even without full Phase 3 ablations, as long as the Pareto curve includes at least τ_v=1 baseline, fixed τ_v=0.7, and per-task CDR."]
Feedback: CDR has resolved all critical issues from Rounds 1-4: τ_v=0 reference replaced with GT actions, Denoising Fast and Slow correctly characterized as spatial/patch-level routing, Fast-WAM baseline correctly specified as τ_v=1 proxy (not the published model), MotuBrain acknowledged as orthogonal, and timeline drop-able ablations flagged. The scientific framing is now verified against mimic-video: Figure 5 does show performance peaks at intermediate τ_v, and τ_v=1 is confirmed as the best global autonomous default (noise-as-augmentation effect). CDR's Pareto story is internally consistent and scientifically sound.

Three focused fixes for Round 6:

**Fix 1 (1 hour): Cite OA-WAM and clarify SimplerEnv vs SIMPLER-Bridge.** OA-WAM (arXiv:2605.06481) evaluates on SimplerEnv (79.3%) and LIBERO (97.8%) — reviewers will notice the gap with CDR's 46.9% SIMPLER-Bridge base. Add one sentence: 'OA-WAM (2605.06481) addresses object identity robustness in WAMs; CDR addresses adaptive video denoising depth — orthogonal.' Then explicitly note in the experimental section whether SimplerEnv and SIMPLER-Bridge are the same split; if not, state that direct comparison against OA-WAM is not applicable.

**Fix 2 (Phase 0 addition, run ASAP): Pre-validate zero-shot LIBERO→SIMPLER-Bridge router.** Before finalizing the ≥80% recovery claim as a primary CoRL contribution, validate it in Phase 0 or Phase 1: take a frozen MLP trained on task embeddings from 80 LIBERO-100 tasks, test zero-shot on 20 held-out LIBERO tasks, verify ≥80% τ_v* recovery. If this holds on held-out LIBERO tasks, the SIMPLER-Bridge zero-shot claim is credible. If not, reframe to 'per-task routing with fine-tuning on 3 SIMPLER tasks' rather than zero-shot.

**Fix 3 (framing, 30 min): Pre-register the fixed τ_v < 1 underperformance prediction.** In Phase 3, explicitly state: 'We predict baselines (b,c) — LingBot-VA-style fixed τ_v=0.5/0.7/0.9 — will underperform baseline (a) τ_v=1 on SIMPLER-Bridge due to the noise-as-augmentation regularization effect documented in mimic-video. If this prediction is confirmed, CDR's Pareto comparison is against (a) and the per-task sweep oracle, not against uniform partial denoising approaches.' This pre-registration turns a potential negative result (baseline (b,c) worse than τ_v=1) into a publishable confirmation of CDR's theoretical premise.

**Optional (1 hour): Add A₁ one-sentence cite.** 'Concurrent work (arXiv:2604.05672) applies per-observation adaptive truncation to VLA action generation via inter-layer early exit; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal.'

### Round 6 review
Verdict: revise
Issues: ["MODERATE — mimic-video Figure 5 is cited misleadingly: CDR claims 'Figure 5 shows aggregate performance peaks at an intermediate noise level (not at τ_v=1)' — this reflects the figure *caption* only. The mimic-video main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest flow time τ_v=1.' These are internally contradictory in the source paper, and reviewers reading the main text will perceive CDR as misrepresenting mimic-video. CDR must cite the figure caption specifically ('mimic-video Figure 5 caption states: performance peaks at an intermediate noise level') AND acknowledge that the main text separately concludes τ_v=1 is the best fixed global choice. The reconciliation is straightforward — Figure 5 shows oracle per-task optimal τ_v is at intermediate levels, while τ_v=1 is the best fixed-global-τ_v — but CDR must make this explicit or reviewers will flag it in every review.", "MODERATE — The pre-registered prediction that 'fixed τ_v < 1 baselines will underperform τ_v=1' is now strongly supported by mimic-video's *main text* conclusion (τ_v=1 is best autonomous performance). If this prediction is confirmed in Phase 3, CDR's Pareto comparison becomes primarily CDR vs. τ_v=1 baseline — LingBot-VA-style uniform partial denoising is not a Pareto competitor on SIMPLER-Bridge. CDR should elevate this framing: 'Our pre-registered prediction is that LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge; CDR's contribution is Pareto dominance over the τ_v=1 default via selective routing.' If confirmed, the paper becomes a cleaner story but with a narrower competitive comparison than currently implied.", "MINOR — The core novelty claim ('no existing VAM paper has empirically studied which manipulation phases benefit from τ_v < 1') is valid but the architectural contribution (2-layer MLP router) is thin for CoRL 2026's competitive WAM track. The Phase 1 empirical study is the genuine contribution; CDR should foreground it as 'the first empirical characterization of video necessity by manipulation phase in 3D WAMs' rather than leading with the routing mechanism."]
Feedback: CDR has resolved all Round 5 issues and is scientifically well-structured. One focused fix is needed before submission:

**Fix 1 (required, 30 minutes): Correct the mimic-video Figure 5 citation.** Replace 'Figure 5 shows aggregate performance peaks at an intermediate noise level (not at τ_v=1)' with 'mimic-video Figure 5 caption reports that performance peaks at an intermediate noise level; the paper's main text separately concludes that τ_v=1 achieves the best fixed-global autonomous policy performance on SIMPLER-Bridge. These findings are reconcilable: the oracle per-task optimal τ_v is intermediate (Figure 5 caption), while the best fixed-global τ_v is τ_v=1 (main text). CDR exploits this gap: a lightweight router approximates the per-observation oracle, recovering gains that a fixed-global τ_v=1 leaves on the table.' This specific reconciliation should appear verbatim in the intro, and the phrase 'aggregate performance peaks at an intermediate noise level' must be removed from all sections where it appears without the Figure 5 caption attribution. Reviewers who have read mimic-video carefully will catch this without the fix.

**Fix 2 (framing, 20 minutes): Elevate the pre-registered prediction as the paper's anchor claim.** Since mimic-video's main text already supports the prediction that uniform τ_v<1 underperforms τ_v=1, CDR's Pareto claim is effectively: CDR vs. τ_v=1 baseline (not CDR vs. LingBot-VA). Make this the headline: 'We show that LingBot-VA-style uniform partial denoising is not a valid Pareto competitor on SIMPLER-Bridge (pre-registered and confirmed), and CDR Pareto-dominates the τ_v=1 fixed-global default by selectively routing only frames that require lower τ_v.' This is a cleaner and more defensible Pareto claim than the current framing.

With these two changes, CDR is ready for CoRL submission. The MVS track is well-defined, the zero-shot validation gates are appropriately scoped, and the related-work section is comprehensive. The paper's contribution — the first empirical study of manipulation-phase τ_v requirements plus zero-shot per-task routing — is modest but publishable at CoRL if the Phase 1 histograms show meaningful phase-specific variation.

### Round 7 review
Verdict: revise
Issues: ["MODERATE — DiT4DiT ablation is factually mischaracterized: Independent verification of arXiv:2603.10448 confirms that DiT4DiT's 'single-step is best' ablation (Figure 8b) concerns ACTION DENOISING STEPS (fewer action diffusion steps yield higher success), not τ_v (video noise level). CDR's landscape states: 'DiT4DiT ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding.' This conflates two different efficiency axes (action denoising steps vs. video noise level). Reviewers familiar with DiT4DiT will flag this. Fix: either remove DiT4DiT as corroborating evidence for τ_v=1 optimality, or rewrite as 'DiT4DiT finds that fewer action denoising steps improve performance — a parallel finding that the high-noise, low-denoising regime is preferable, supporting CDR's premise that less denoising is often better.' Do NOT use DiT4DiT to directly corroborate mimic-video's τ_v=1 result.", "MODERATE — Pareto efficiency claim is potentially misleading if P1 is confirmed: If P1 is confirmed (fixed intermediate τ_v < 1 uniformly underperforms τ_v=1 on SIMPLER-Bridge), then CDR's router will route the vast majority of frames to τ_v=1 (since τ_v=1 is the best single fixed value). The resulting 'compute savings' from CDR — measured as reduction in mean τ_v consumed below 1 — will be small (perhaps 5–10% of full video generation cost). The Pareto win is primarily in task SUCCESS (+≥7.5pp from zero-shot per-task routing), not in compute efficiency. The paper's abstract and intro must be honest about this: 'CDR's Pareto dominance is primarily measured in task success recovery, not compute savings, if the pre-registered P1 prediction is confirmed. The mean τ_v consumed by CDR remains close to 1 when P1 holds.' Misrepresenting the Pareto win as efficiency-driven when most frames route to τ_v=1 will trigger reviewer pushback.", "MODERATE — Auto-mode resource estimate (410 H100-hours) exceeds the ≤200 H100-hour budget constraint stated in user requirements. The manual estimate (115–135H) is within budget, but auto mode at 410H is 2-3× over the stated limit. Either: (a) cap the auto-mode scope to fit within 200H by dropping full RoboCasa, per-phase heatmap ablations, and the full λ×θ grid search; or (b) explicitly acknowledge in the proposal that auto-mode exceeds the 200H constraint and requires expanded budget authorization.", "MINOR — 'When to Trust Imagination' (arXiv:2605.06222) is misdescribed as 'reduces replanning frequency'; verified content shows it uses a per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution — not episode-level replanning reduction. The orthogonality claim holds, but the description should be corrected to 'per-chunk adaptive replanning trigger' to avoid misleading reviewers.", "MINOR — Method contribution is architecturally thin for CoRL 2026's WAM track: The 2-layer MLP router (512-dim CLIP + 512-dim language → 256-dim hidden → 4-class softmax) is not a novel architecture. CoRL 2026's WAM submissions include DiT4DiT, MotuBrain, OA-WAM with substantial architectural innovation. CDR must foreground Phase 1 (first empirical characterization of manipulation-phase τ_v requirements) as the primary scientific contribution — the router is the deployment mechanism, not the contribution. The paper title 'Commitment Depth Routing' implies a routing method is the contribution; consider retitling to reflect the empirical study: e.g., 'When Do World Action Models Need Video? A Manipulation-Phase Study with Selective Denoising Activation.'"]
Feedback: CDR has fixed all prior critical issues through Round 6. The Round 7 proposal is now scientifically well-structured with explicit gates, correct mimic-video Figure 5 reconciliation, pre-registered predictions, and MVS fallback. Three focused fixes are required before CoRL submission:

**Fix 1 (required, 30 minutes): Correct DiT4DiT characterization.** DiT4DiT's ablation (Figure 8b in arXiv:2603.10448) is about action denoising steps — not τ_v (video noise level). CDR incorrectly uses it to corroborate 'high τ_v is best on SIMPLER-Bridge.' Rewrite as: 'DiT4DiT finds that a single action denoising step outperforms multi-step action diffusion — a parallel finding that less denoising in the action domain also improves performance; we observe the same pattern in the video domain with mimic-video's τ_v=1 result.' Remove any language claiming DiT4DiT 'independently confirms' that high video noise τ_v is optimal.

**Fix 2 (required, 20 minutes): Honestly bound the Pareto efficiency claim.** If P1 is confirmed (the expected outcome based on mimic-video main text), CDR routes most frames to τ_v=1, making compute savings modest. Add explicit language in the abstract and intro: 'CDR's primary Pareto benefit is task success recovery (≥7.5pp zero-shot on SIMPLER-Bridge), not compute efficiency — most frames continue to use τ_v=1, with video activation selectively applied only to frames where the Phase 1 study identifies τ_v* < 1.' This prevents reviewers from expecting large speedups and finding only 5-10% compute savings.

**Fix 3 (budget reconciliation, 10 minutes): Cap auto-mode estimate.** The auto mode at 410 H100-hours violates the ≤200H project constraint. Either (a) reduce auto-mode scope to 150-180H (drop RoboCasa, full hyperparameter grid) while keeping the key SIMPLER-Bridge experiments, or (b) add a note that auto-mode exceeds the budget constraint and requires pre-authorization. The manual mode (115-135H) is within budget and should be the reference for the 200H limit.

**Optional (strengthens paper): Retitle to foreground empirical contribution.** 'Commitment Depth Routing' implies a novel routing mechanism as the primary contribution. The actual primary contribution is Phase 1 — the first empirical study of which manipulation phases need τ_v < 1 in 3D WAMs. A title like 'When Does Robot Policy Need Video? Manipulation-Phase Analysis and Selective Activation for World Action Models' better positions the paper as an empirical methods contribution and reduces reviewer expectations of architectural novelty.


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
  "promptId": "7e098ab2-5565-40d9-9460-3fcce424727d",
  "type": "user",
  "uuid": "8a712ea7-0351-431b-b7fa-0f8a370cfedd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:30:44.067Z_

```json
{
  "parentUuid": "8a712ea7-0351-431b-b7fa-0f8a370cfedd",
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
  "uuid": "fbec84e0-8b2d-46da-a94a-3a52c499ad59",
  "timestamp": "2026-05-10T09:30:44.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:30:44.067Z_

```json
{
  "parentUuid": "fbec84e0-8b2d-46da-a94a-3a52c499ad59",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "46d12f9e-6b9d-46f3-a82b-459edc40b856",
  "timestamp": "2026-05-10T09:30:44.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
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
  "leafUuid": "46d12f9e-6b9d-46f3-a82b-459edc40b856",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDR Phase 0 prior to CoRL 2026 commitment",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:31:58.355Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 8/10 of an adversarial review for a research paper idea called "When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation" (previously called "Commitment Depth Routing" or CDR). 

Let me analyze what's been fixed from Round 7 and what still needs attention, then do my own independent research to verify claims.

From the Round 7 review, the issues were:
1. DiT4DiT ablation mischaracterized (MODERATE)
2. Pareto efficiency claim potentially misleading (MODERATE)


3. Auto-mode resource estimate exceeds ≤200H budget (MODERATE)
4. 'When to Trust Imagination' misdescribed (MINOR)
5. Method contribution architecturally thin (MINOR)

Looking at the Round 8 proposal, I'm checking what's been fixed. The DiT4DiT fix now clarifies that the ablation concerns action diffusion steps rather than video noise level, treating them as orthogonal efficiency axes, and CDR cites DiT4DiT only for structural purposes.

The Pareto efficiency claim has been reframed with explicit sections acknowledging that when P1 is confirmed, CDR routes most frames to τ_v=1 with modest compute savings of 5-10%, where the real benefits come from task success recovery and deployment calibration. The auto-mode budget has been revised down to approximately 150–175 H100-hours with scope reductions including dropping RoboCasa evaluation and simplifying the hyperparameter grid from 3×3 to 2×2.

The "When to Trust Imagination" mechanism is now clearly described as an adaptive replanning trigger that uses a learned threshold to decide after each action chunk whether to continue or replan based on prediction reliability. The title has been updated to better reflect the core contribution around selective denoising activation and manipulation-phase analysis.

Now I'm checking whether the two findings from mimic-video actually reconcile—specifically whether τ_v=1 being optimal as a fixed global setting aligns with Figure 5 showing intermediate optimization values.

I should verify several key claims before finalizing: whether OA-WAM uses the same evaluation tasks as SIMPLER-Bridge, if any concurrent work already does per-observation τ_v routing, what the competitive landscape looks like for world action models at CoRL 2026, and whether the performance claims for Fast-WAM and LingBot-VA hold up. Since this is round 8 of 10 and major issues have been addressed, I'll focus on validating the core scientific premise and checking for any newer papers that might affect novelty.

There's a potential tension in the novelty argument that I need to resolve: the paper's main finding is that some tasks benefit from τ_v < 1, yet it also pre-registers that a global fixed τ_v < 1 underperforms τ_v=1. The reconciliation is that per-task optimal τ_v values can be intermediate even when the globally fixed τ_v=1 is best overall—this oracle versus fixed distinction is the key insight, though I should verify this logic holds up under scrutiny.

On the CoRL bar itself, the empirical study of τ_v* distributions across LIBERO-100 with phase annotations is solid, but the routing method is just a 2-layer MLP, which feels methodologically thin. I should also check whether any relevant concurrent work has emerged between the proposal date and now, and then assess whether the overall package truly meets the venue's standards given that the core technical contribution is relatively modest.

Looking at the substantive arguments, the paper has addressed all the critical issues from previous rounds and the framing is now honest about where it delivers value. But there's a real tension I'm noticing: the paper simultaneously claims that τ_v=1 is the optimal fixed default globally, yet also argues that a learned router can beat it by routing to intermediate τ_v values—these narratives pull in opposite directions and need to be reconciled more carefully. These are reconcilable BUT the paper also says "if P1 is confirmed (the expected outcome), CDR routes the MAJORITY of frames to τ_v=1. Mean τ_v consumed by CDR stays CLOSE TO 1.0." 

   If MOST frames route to τ_v=1, and the benefit is primarily deployment calibration savings (10 rollouts → 0) plus +≥7.5pp task success... reviewers will ask: does the +7.5pp come from the router, or from the fact that some tasks genuinely benefit from lower τ_v? If τ_v=1 is best fixed-globally, how does routing to lower τ_v help individual tasks? This needs clearer explanation.

2. **The 10-rollout cost saving claim**: The practical impact here is modest—40 total rollouts across SIMPLER-Bridge's 4 tasks for calibration. For a deployment paper to really stand out, this kind of savings needs to be demonstrated at scale with many new tasks, which the paper mentions but may not stress-test thoroughly enough.

3. **SIMPLER-Bridge task count**: Evaluating on just 4 WidowX Bridge tasks feels like a small test set for statistical reliability claims. Other papers like LingBot-VA use 98.5% LIBERO with many more tasks, and OA-WAM also evaluates on LIBERO, so CoRL reviewers might push back on whether 4 tasks is sufficient for robustness.

Now I need to verify some key claims: whether there's existing work on adaptive video denoising for robotics, what OA-WAM's actual evaluation setup looks like, and what mimic-video found about τ_v.

I should also check what competitive work might have appeared recently and whether OA-WAM actually uses the same 4 SIMPLER-Bridge tasks, plus verify if any newer papers are doing per-observation τ_v routing in WAMs.

Looking at the core issues for CoRL readiness: the calibration savings claim feels underdeveloped as a primary contribution—going from 10 rollouts to 0 per new task is interesting, but the +7.5pp task success improvement across 4 tasks is modest, and the paper hasn't demonstrated this deployment scenario at scale. There's also an internal tension in how the paper frames its benefits around pre-registered claims that I need to examine more closely. prediction P1 says "fixed τ_v < 1 underperforms τ_v=1" — which the proposal calls "strongly supported" and "the expected outcome." If this is so strongly expected, then the scientific contribution of confirming it (Phase 3 baselines b,c) is low novelty. Conversely, if P2 is confirmed (+7.5pp from per-task routing), it validates that per-task oracle τ_v is meaningful — but why would the MLP router be needed if the base model always prefers τ_v=1? The paper's narrative would be cleaner if it emphasized: "we find that the mean τ_v* across frames for some tasks (e.g., precision grasping) is lower than τ_v=1, even though the best GLOBAL fixed τ_v is 1 — this task-level heterogeneity is the gap CDR exploits."

The evaluation scope is concerning — only 4 SIMPLER-Bridge tasks for the main claims feels statistically fragile, and CoRL reviewers will likely demand either broader evaluation or rigorous statistical analysis across multiple seeds and task variants. Additionally, the Phase 0 zero-shot validation gate is too permissive; if the <20% error threshold fails, falling back to few-shot adaptation (3 tasks train, 1 test) is substantially weaker than zero-shot, so either tightening this criterion or running Phase 0 immediately would strengthen the work.

I need to search for concurrent work on adaptive noise levels for robot manipulation, verify the OA-WAM setup, and check for any recent papers on per-observation routing to assess novelty properly. Given this is Round 8 of 10 and the paper has been iteratively revised, I'm weighing whether to recommend acceptance or further revision — the core router architecture remains shallow (2-layer MLP), and while the empirical Phase 1 results show promise, the scientific narrative around why per-task routing matters needs clarification. I'm running targeted searches to verify the key claims in the Round 8 paper and check for any overlooked concerns before finalizing my assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46d12f9e-6b9d-46f3-a82b-459edc40b856",
  "isSidechain": false,
  "requestId": "req_011CatevZGxo6WzbkvWK4mMe",
  "type": "assistant",
  "uuid": "1cea0a95-ce7a-4000-abd0-08389826bafd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DxVVzmEfwv8PUzzwo8zeT6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35466,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3603,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3603,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35466
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

_source line 9 · 2026-05-10T09:31:58.358Z_

I'll conduct independent verification searches to assess this Round 8 proposal before issuing my verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cea0a95-ce7a-4000-abd0-08389826bafd",
  "isSidechain": false,
  "requestId": "req_011CatevZGxo6WzbkvWK4mMe",
  "type": "assistant",
  "uuid": "338b11ec-0881-42fe-bb4c-ed3a88cc4ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DxVVzmEfwv8PUzzwo8zeT6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35466,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3603,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3603,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35466
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

_source line 10 · 2026-05-10T09:32:03.068Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01B9wXA7xrrPFQSL8RCHGftq`</summary>

```json
{
  "description": "Search for concurrent WAM papers on adaptive video denoising",
  "subagent_type": "Explore",
  "prompt": "Search for recent papers (2025-2026) on adaptive video noise/denoising levels for robot manipulation world action models. Specifically look for:\n1. Papers that do per-observation or per-task adaptive video noise level selection in video-action models or world action models\n2. Papers on selective video denoising for robot policies\n3. Any papers that study which robot manipulation phases benefit from video prediction\n\nUse WebSearch with these queries:\n- \"adaptive video noise level robot manipulation policy 2026\"\n- \"per-observation denoising depth world action model 2026\"\n- site:arxiv.org \"video noise level\" \"robot manipulation\" 2026\n- \"selective video generation robot policy\" arxiv 2026\n\nReport all relevant papers found, with titles, arxiv IDs, and brief descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "338b11ec-0881-42fe-bb4c-ed3a88cc4ba8",
  "isSidechain": false,
  "requestId": "req_011CatevZGxo6WzbkvWK4mMe",
  "type": "assistant",
  "uuid": "f165cfed-032c-4ca0-9afc-6dcffa3009d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DxVVzmEfwv8PUzzwo8zeT6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35466,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3603,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3603,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35466
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

_source line 11 · 2026-05-10T09:32:25.069Z_

<details><summary>↩ Tool result · `toolu_01B9wXA7xrrPFQSL8RCHGftq`</summary>

```text
Excellent! I found several highly relevant papers. Here's a comprehensive report of recent papers (2025-2026) on adaptive video noise/denoising and selective video generation for robot manipulation:

## Key Papers Found:

### 1. **X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising**
- **ArXiv ID**: 2604.26694
- **Key Innovation**: Introduces Asynchronous Noise Sampling (ANS) - a specialized asynchronous denoising schedule that rapidly decodes actions with fewer steps while dedicating full denoising sequence to high-fidelity video generation. This directly addresses per-observation adaptive noise level selection.
- **Details**: Predicts multi-view RGB-D videos with lightweight depth prediction branch. ANS jointly optimizes generation quality and action decoding efficiency.

### 2. **MotuBrain: An Advanced World Action Model for Robot Control**
- **ArXiv ID**: 2604.27792
- **Key Focus**: Addresses inference latency in world-action models by tackling the coupling of high-dimensional video and action latent denoising over many diffusion steps.
- **Relevance**: Practical focus on selective denoising for efficient robot control.

### 3. **Draft-and-Target Sampling for Video Generation Policy**
- **ArXiv ID**: 2603.13438
- **Key Innovation**: Training-free diffusion inference paradigm with self-play denoising using two complementary denoising trajectories. Includes token chunking and progressive acceptance strategy.
- **Achievement**: Up to 2.1x speedup with minimal compromise to success rate.
- **Relevance**: Demonstrates selective/adaptive video denoising for improved policy efficiency.

### 4. **Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation**
- **ArXiv ID**: 2604.02979
- **Key Focus**: Explicitly addresses frame-level selective computation in autoregressive video generation. Studies which frames benefit from full processing vs. extrapolation.
- **Relevance**: Directly relevant to understanding which robot manipulation phases benefit from full video prediction.

### 5. **Video Generators are Robot Policies**
- **ArXiv ID**: 2508.00795
- **Key Innovation**: Modular framework combining video and action generation with learned denoising networks. Extracts policies with minimal demonstration data.
- **Details**: Extended architecture to decode actions using action U-Net conditioned on intermediate features from video denoising networks.

### 6. **Astra: General Interactive World Model with Autoregressive Denoising**
- **ArXiv ID**: 2512.08931
- **Key Focus**: Autoregressive denoising architecture using temporal causal attention to aggregate observations and support streaming outputs.
- **Relevance**: Per-observation denoising approach for world models.

### 7. **From Generated Human Videos to Physically Plausible Robot Trajectories (GenMimic)**
- **ArXiv ID**: 2512.05094
- **Key Innovation**: Selective weighted combination approach applied to denoised video outputs with 3D keypoint rewards.
- **Relevance**: Demonstrates selective application of denoising/generation quality to robot learning.

## Summary:

The most directly relevant papers for **adaptive per-observation noise level selection** are:
- **X-WAM** (2604.26694) - Asynchronous Noise Sampling for per-observation adaptive denoising
- **Draft-and-Target Sampling** (2603.13438) - Selective denoising trajectories for video policies
- **Not All Frames Deserve Full Computation** (2604.02979) - Frame-level selective computation

These papers collectively demonstrate emerging techniques for adaptive video noise handling in robot manipulation world action models, with focus on per-observation and phase-aware selective denoising.

Sources:
- [X-WAM: Unified 4D World Action Modeling](https://arxiv.org/html/2604.26694v2)
- [MotuBrain: Advanced World Action Model](https://arxiv.org/html/2604.27792v2)
- [Draft-and-Target Sampling for Video Generation Policy](https://arxiv.org/abs/2603.13438)
- [Not All Frames Deserve Full Computation](https://arxiv.org/html/2604.02979)
- [Video Generators are Robot Policies](https://arxiv.org/html/2508.00795v1)
- [Astra: General Interactive World Model](https://arxiv.org/html/2512.08931)
- [From Generated Human Videos to Physically Plausible Robot Trajectories](https://arxiv.org/html/2512.05094)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f165cfed-032c-4ca0-9afc-6dcffa3009d4",
  "isSidechain": false,
  "promptId": "7e098ab2-5565-40d9-9460-3fcce424727d",
  "type": "user",
  "uuid": "cfc5e951-2a18-49f8-aeac-d17b1cd97d53",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) on adaptive video noise/denoising levels for robot manipulation world action models. Specifically look for:\n1. Papers that do per-observation or per-task adaptive video noise level selection in video-action models or world action models\n2. Papers on selective video denoising for robot policies\n3. Any papers that study which robot manipulation phases benefit from video prediction\n\nUse WebSearch with these queries:\n- \"adaptive video noise level robot manipulation policy 2026\"\n- \"per-observation denoising depth world action model 2026\"\n- site:arxiv.org \"video noise level\" \"robot manipulation\" 2026\n- \"selective video generation robot policy\" arxiv 2026\n\nReport all relevant papers found, with titles, arxiv IDs, and brief descriptions.",
    "agentId": "a0b7235e0d0875e9a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I found several highly relevant papers. Here's a comprehensive report of recent papers (2025-2026) on adaptive video noise/denoising and selective video generation for robot manipulation:\n\n## Key Papers Found:\n\n### 1. **X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising**\n- **ArXiv ID**: 2604.26694\n- **Key Innovation**: Introduces Asynchronous Noise Sampling (ANS) - a specialized asynchronous denoising schedule that rapidly decodes actions with fewer steps while dedicating full denoising sequence to high-fidelity video generation. This directly addresses per-observation adaptive noise level selection.\n- **Details**: Predicts multi-view RGB-D videos with lightweight depth prediction branch. ANS jointly optimizes generation quality and action decoding efficiency.\n\n### 2. **MotuBrain: An Advanced World Action Model for Robot Control**\n- **ArXiv ID**: 2604.27792\n- **Key Focus**: Addresses inference latency in world-action models by tackling the coupling of high-dimensional video and action latent denoising over many diffusion steps.\n- **Relevance**: Practical focus on selective denoising for efficient robot control.\n\n### 3. **Draft-and-Target Sampling for Video Generation Policy**\n- **ArXiv ID**: 2603.13438\n- **Key Innovation**: Training-free diffusion inference paradigm with self-play denoising using two complementary denoising trajectories. Includes token chunking and progressive acceptance strategy.\n- **Achievement**: Up to 2.1x speedup with minimal compromise to success rate.\n- **Relevance**: Demonstrates selective/adaptive video denoising for improved policy efficiency.\n\n### 4. **Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation**\n- **ArXiv ID**: 2604.02979\n- **Key Focus**: Explicitly addresses frame-level selective computation in autoregressive video generation. Studies which frames benefit from full processing vs. extrapolation.\n- **Relevance**: Directly relevant to understanding which robot manipulation phases benefit from full video prediction.\n\n### 5. **Video Generators are Robot Policies**\n- **ArXiv ID**: 2508.00795\n- **Key Innovation**: Modular framework combining video and action generation with learned denoising networks. Extracts policies with minimal demonstration data.\n- **Details**: Extended architecture to decode actions using action U-Net conditioned on intermediate features from video denoising networks.\n\n### 6. **Astra: General Interactive World Model with Autoregressive Denoising**\n- **ArXiv ID**: 2512.08931\n- **Key Focus**: Autoregressive denoising architecture using temporal causal attention to aggregate observations and support streaming outputs.\n- **Relevance**: Per-observation denoising approach for world models.\n\n### 7. **From Generated Human Videos to Physically Plausible Robot Trajectories (GenMimic)**\n- **ArXiv ID**: 2512.05094\n- **Key Innovation**: Selective weighted combination approach applied to denoised video outputs with 3D keypoint rewards.\n- **Relevance**: Demonstrates selective application of denoising/generation quality to robot learning.\n\n## Summary:\n\nThe most directly relevant papers for **adaptive per-observation noise level selection** are:\n- **X-WAM** (2604.26694) - Asynchronous Noise Sampling for per-observation adaptive denoising\n- **Draft-and-Target Sampling** (2603.13438) - Selective denoising trajectories for video policies\n- **Not All Frames Deserve Full Computation** (2604.02979) - Frame-level selective computation\n\nThese papers collectively demonstrate emerging techniques for adaptive video noise handling in robot manipulation world action models, with focus on per-observation and phase-aware selective denoising.\n\nSources:\n- [X-WAM: Unified 4D World Action Modeling](https://arxiv.org/html/2604.26694v2)\n- [MotuBrain: Advanced World Action Model](https://arxiv.org/html/2604.27792v2)\n- [Draft-and-Target Sampling for Video Generation Policy](https://arxiv.org/abs/2603.13438)\n- [Not All Frames Deserve Full Computation](https://arxiv.org/html/2604.02979)\n- [Video Generators are Robot Policies](https://arxiv.org/html/2508.00795v1)\n- [Astra: General Interactive World Model](https://arxiv.org/html/2512.08931)\n- [From Generated Human Videos to Physically Plausible Robot Trajectories](https://arxiv.org/html/2512.05094)"
      }
    ],
    "totalDurationMs": 21972,
    "totalTokens": 19670,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1192,
      "cache_creation_input_tokens": 2947,
      "cache_read_input_tokens": 14397,
      "output_tokens": 1134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1192,
          "output_tokens": 1134,
          "cache_read_input_tokens": 14397,
          "cache_creation_input_tokens": 2947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2947,
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
  "sourceToolAssistantUUID": "f165cfed-032c-4ca0-9afc-6dcffa3009d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "cfc5e951-2a18-49f8-aeac-d17b1cd97d53",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDR Phase 0 prior to CoRL 2026 commitment",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Tool call

_source line 14 · 2026-05-10T09:32:33.794Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JpbuznJwqf2knotEjnjVkF`</summary>

```json
{
  "description": "Verify OA-WAM evaluation setup and check for frame-selective WAM papers",
  "subagent_type": "Explore",
  "prompt": "Please do the following searches and fetch the results:\n\n1. Fetch the abstract and key sections of arXiv:2605.06481 (OA-WAM: Object-Addressable World Action Model) and confirm: (a) does it evaluate on SimplerEnv with WidowX Bridge tasks? (b) what exact tasks does it use? (c) is the evaluation protocol \"Visual Matching\"? Report exact quotes.\n\n2. Search for \"Draft-and-Target Sampling\" (arXiv:2603.13438) for robot video policy - fetch the abstract and describe if it does adaptive per-observation video noise level selection.\n\n3. Search for \"Not All Frames Deserve Full Computation\" (arXiv:2604.02979) - fetch the abstract and describe if it's about robot manipulation or general video generation.\n\n4. Search for any May 2026 papers on \"per-observation adaptive noise\" for WAMs: site:arxiv.org \"per-observation\" \"noise level\" robot 2026\n\nUse WebFetch on https://arxiv.org/abs/2605.06481 and https://arxiv.org/abs/2603.13438 and https://arxiv.org/abs/2604.02979"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc5e951-2a18-49f8-aeac-d17b1cd97d53",
  "isSidechain": false,
  "requestId": "req_011Catf3zvWKiXsdHkNe815B",
  "type": "assistant",
  "uuid": "0ee07033-f03f-4fd8-a985-ae20074682a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NLoEBRcgMDEPEUCSJmdM9V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4744,
      "cache_read_input_tokens": 47097,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 47097,
          "cache_creation_input_tokens": 4744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4744
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

_source line 15 · 2026-05-10T09:32:55.923Z_

<details><summary>↩ Tool result · `toolu_01JpbuznJwqf2knotEjnjVkF`</summary>

```text
## Summary of Findings

Based on the fetches and searches, here are my findings for each of your requests:

### 1. **OA-WAM (arXiv:2605.06481)** - Object-Addressable World Action Model

**SimplerEnv Evaluation:**
- **(a) Does it evaluate on SimplerEnv with WidowX Bridge tasks?** The paper evaluates on SimplerEnv but the abstract does not specify the particular tasks (WidowX Bridge or otherwise).
- **(b) Exact tasks used:** The abstract does not detail the specific tasks evaluated—only that a 79.3% result was achieved on SimplerEnv.
- **(c) "Visual Matching" evaluation protocol?** **No.** The abstract mentions a "causal slot-intervention test" but does NOT use a "Visual Matching" protocol.

**Exact quote from abstract:** "OA-WAM matches strong VLA and WAM baselines on LIBERO (97.8%) and SimplerEnv (79.3%)"

The paper's approach "decomposes each frame into N+1 slot states, with one robot slot and N object slots" for improving vision-language-action policies.

---

### 2. **Draft-and-Target Sampling (arXiv:2603.13438)** - Robot Video Policy

**Adaptive per-observation noise level selection:** **No.** This paper does NOT address adaptive per-observation noise level selection.

The abstract describes "a novel diffusion inference paradigm for video generation policy that is training-free" using "two complementary denoising trajectories" for computational efficiency (achieving "up to 2.1x speedup"). The focus is on inference optimization through draft and target sampling with token chunking and progressive acceptance strategies, not adaptive noise levels per observation.

---

### 3. **Not All Frames Deserve Full Computation (arXiv:2604.02979)**

**Domain:** **General video generation, NOT robot manipulation.** 

This paper (SCOPE) addresses computational efficiency in autoregressive video diffusion models with "a tri-modal scheduler over cache, predict, and recompute" achieving "up to 4.73x speedup" on video benchmarks like MAGI-1 and SkyReels-V2.

---

### 4. **May 2026 Papers on Per-Observation Adaptive Noise for WAMs**

The search did not find a paper specifically titled or focused on "per-observation adaptive noise" for WAMs. However, related adaptive mechanisms in recent WAM literature include:

- **X-WAM** (arXiv:2604.26694): Features Asynchronous Noise Sampling (ANS) for efficient action decoding
- **When to Trust Imagination** (arXiv:2605.06222): Adaptive action execution for WAMs
- **OA-WAM** (arXiv:2605.06481): Documents that "sensor noise can impact performance, where photometric corruption disrupts slot extraction at the perception stage"

---

### Sources:
- [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1)
- [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/html/2605.06222)
- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v2)
- [World Action Models are Zero-shot Policies](https://arxiv.org/html/2602.15922v1)
- [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)
- [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/html/2603.22078v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ee07033-f03f-4fd8-a985-ae20074682a4",
  "isSidechain": false,
  "promptId": "7e098ab2-5565-40d9-9460-3fcce424727d",
  "type": "user",
  "uuid": "5e50c4be-fcc6-443c-9003-d1262bc8b015",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please do the following searches and fetch the results:\n\n1. Fetch the abstract and key sections of arXiv:2605.06481 (OA-WAM: Object-Addressable World Action Model) and confirm: (a) does it evaluate on SimplerEnv with WidowX Bridge tasks? (b) what exact tasks does it use? (c) is the evaluation protocol \"Visual Matching\"? Report exact quotes.\n\n2. Search for \"Draft-and-Target Sampling\" (arXiv:2603.13438) for robot video policy - fetch the abstract and describe if it does adaptive per-observation video noise level selection.\n\n3. Search for \"Not All Frames Deserve Full Computation\" (arXiv:2604.02979) - fetch the abstract and describe if it's about robot manipulation or general video generation.\n\n4. Search for any May 2026 papers on \"per-observation adaptive noise\" for WAMs: site:arxiv.org \"per-observation\" \"noise level\" robot 2026\n\nUse WebFetch on https://arxiv.org/abs/2605.06481 and https://arxiv.org/abs/2603.13438 and https://arxiv.org/abs/2604.02979",
    "agentId": "a05051a9c67d33b31",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Findings\n\nBased on the fetches and searches, here are my findings for each of your requests:\n\n### 1. **OA-WAM (arXiv:2605.06481)** - Object-Addressable World Action Model\n\n**SimplerEnv Evaluation:**\n- **(a) Does it evaluate on SimplerEnv with WidowX Bridge tasks?** The paper evaluates on SimplerEnv but the abstract does not specify the particular tasks (WidowX Bridge or otherwise).\n- **(b) Exact tasks used:** The abstract does not detail the specific tasks evaluated—only that a 79.3% result was achieved on SimplerEnv.\n- **(c) \"Visual Matching\" evaluation protocol?** **No.** The abstract mentions a \"causal slot-intervention test\" but does NOT use a \"Visual Matching\" protocol.\n\n**Exact quote from abstract:** \"OA-WAM matches strong VLA and WAM baselines on LIBERO (97.8%) and SimplerEnv (79.3%)\"\n\nThe paper's approach \"decomposes each frame into N+1 slot states, with one robot slot and N object slots\" for improving vision-language-action policies.\n\n---\n\n### 2. **Draft-and-Target Sampling (arXiv:2603.13438)** - Robot Video Policy\n\n**Adaptive per-observation noise level selection:** **No.** This paper does NOT address adaptive per-observation noise level selection.\n\nThe abstract describes \"a novel diffusion inference paradigm for video generation policy that is training-free\" using \"two complementary denoising trajectories\" for computational efficiency (achieving \"up to 2.1x speedup\"). The focus is on inference optimization through draft and target sampling with token chunking and progressive acceptance strategies, not adaptive noise levels per observation.\n\n---\n\n### 3. **Not All Frames Deserve Full Computation (arXiv:2604.02979)**\n\n**Domain:** **General video generation, NOT robot manipulation.** \n\nThis paper (SCOPE) addresses computational efficiency in autoregressive video diffusion models with \"a tri-modal scheduler over cache, predict, and recompute\" achieving \"up to 4.73x speedup\" on video benchmarks like MAGI-1 and SkyReels-V2.\n\n---\n\n### 4. **May 2026 Papers on Per-Observation Adaptive Noise for WAMs**\n\nThe search did not find a paper specifically titled or focused on \"per-observation adaptive noise\" for WAMs. However, related adaptive mechanisms in recent WAM literature include:\n\n- **X-WAM** (arXiv:2604.26694): Features Asynchronous Noise Sampling (ANS) for efficient action decoding\n- **When to Trust Imagination** (arXiv:2605.06222): Adaptive action execution for WAMs\n- **OA-WAM** (arXiv:2605.06481): Documents that \"sensor noise can impact performance, where photometric corruption disrupts slot extraction at the perception stage\"\n\n---\n\n### Sources:\n- [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/html/2605.06481v1)\n- [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/html/2605.06222)\n- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)\n- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v2)\n- [World Action Models are Zero-shot Policies](https://arxiv.org/html/2602.15922v1)\n- [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)\n- [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/html/2603.22078v1)"
      }
    ],
    "totalDurationMs": 22125,
    "totalTokens": 18004,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 14500,
      "output_tokens": 970,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2527
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 970,
          "cache_read_input_tokens": 14500,
          "cache_creation_input_tokens": 2527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2527,
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
  "sourceToolAssistantUUID": "0ee07033-f03f-4fd8-a985-ae20074682a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T09:34:42.241Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting findings:

1. OA-WAM (2605.06481): The abstract says it achieves 79.3% on SimplerEnv, but the fetch indicates the evaluation protocol might NOT be "Visual Matching" - it mentions a "causal slot-intervention test." The proposal claims OA-WAM uses "Visual Matching protocol" and evaluates on the same 4 WidowX Bridge tasks (Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket). This may be inaccurate, and if OA-WAM uses a different protocol/task set than CDR's SIMPLER-Bridge, the comparison is even less directly comparable than the proposal claims.


2. The other papers I found—one on draft-and-target sampling and another on video generation efficiency—aren't actually relevant to the noise-level selection problem or robot manipulation specifically.

The key issue here is that the proposal appears to mischaracterize OA-WAM's evaluation methodology. Claiming it uses "Visual Matching protocol" when the actual paper describes a different evaluation approach is a factual error that reviewers will likely notice. I should search more carefully to verify what OA-WAM actually does.

On the positive side, my searches haven't turned up any existing work on per-observation adaptive routing for WAMs, so the core novelty claim around CDR still holds. I also haven't found papers analyzing when manipulation phases require full video computation, which is another angle the proposal explores.

The main concern I need to flag is this potential factual inaccuracy about OA-WAM's evaluation protocol—whether it's truly "Visual Matching" or something else like causal slot-intervention testing.  If the protocols differ, the 79.3% versus 46.9% comparison becomes less of an apples-to-apples benchmark. Beyond that, evaluating the primary claim over just four SIMPLER-Bridge tasks feels statistically thin for a competitive robotics paper, and the core architectural novelty question still lingers around whether the approach is sufficiently differentiated from existing work.

The real tension is whether this paper's value proposition holds up under scrutiny. If Phase 1 confirms the expected outcome—most frames routing to minimal compute, a 7.5 percentage point improvement on four tasks, and modest calibration savings—then the contribution starts to feel incremental for a top-tier venue. The calibration benefit alone (eliminating 10 rollouts per new task) doesn't seem substantial enough to carry the narrative. saved), and the task success improvement of +7.5pp on 4 tasks with a base score of 46.9% is real but limited.

The "CoRL bar" assessment shows they accept around 22% of submissions, and the WAM track is competitive with several strong baselines. CDR's contribution—an empirical study plus an MLP router—sits at the boundary of what might be acceptable.

Now I'm forming my verdict at Round 8 of 10. The paper has addressed all critical issues, but the remaining gaps are clear: the novelty is modest (3/5) with a thin router contribution, feasibility is tight but doable (3.5/5) with compute within budget, clarity is strong (4/5) thanks to the honest framing, and impact is limited (3/5) with improvements that won't shift the field. This averages to about 3.4/5—below the 4.0 threshold needed to pass. At this stage, the paper warrants a "revise" verdict with specific guidance.

That said, I should consider whether there's a path to acceptance. The work has been refined through 7 rounds, and the Phase 1 characterization of τ_v* across manipulation phases could genuinely interest the community. Papers with modest methods do get accepted at CoRL when the empirical findings are novel and rigorous. But the 4-task evaluation is a real limitation for CoRL 2026, and the calibration savings argument—now the reframed primary benefit—isn't compelling enough to carry the paper on its own.

I'll recommend "revise" with targeted feedback on the OA-WAM evaluation protocol verification and the statistical robustness of the findings.

Actually, wait. This is Round 8 of 10, and the paper has made substantial progress. Let me identify what's genuinely new here rather than rehashing prior feedback. I'm noticing a potential protocol mismatch: the proposal claims OA-WAM uses the same Visual Matching protocol as their approach, but my search suggests OA-WAM actually uses a causal slot-intervention test instead. If that's accurate, the comparison framing is misleading. There's also a tension in the zero-shot claim that needs clarification around how the pre-registered P1 assumption about fixed τ_v affects the generalization narrative. The global optimum staying near τ_v=1 while individual tasks benefit from lower values is actually consistent—CDR can route tasks A and B to τ_v < 1 for improvements while C and D remain at 1.0, keeping the average stable. Now I'm questioning whether the Minimum Viable Submission track is substantive enough for a CoRL competition paper, given it only requires three Pareto points and Phase 1 histograms across four tasks.

I'm noticing a potential mismatch: the proposal claims OA-WAM evaluates on the same Visual Matching protocol as CDR's SIMPLER-Bridge, but checking the actual paper suggests OA-WAM uses a causal slot-intervention test instead. If the evaluation protocols differ, then comparing their performance numbers (79.3% versus 46.9%) becomes problematic, and the proposal's explanation may need correction. I should verify what OA-WAM actually measures before drawing conclusions about the comparison.

Given the honest Pareto framing where most frames stay at τ_v=1 with modest compute savings, the core contribution boils down to: characterizing τ_v* across manipulation phases in LIBERO-100, building a lightweight MLP router for zero-shot per-task selection, and achieving 7.5+ percentage point gains on SIMPLER-Bridge tasks with 10 rollout savings per task. Now I'm weighing whether this is strong enough for CoRL 2026's WAM track, especially when comparing against recent work like DiT4DiT (98.6% LIBERO, 50.8% RoboCasa) and OA-WAM (97.8% LIBERO, 79.3% SimplerEnv).

The honest assessment is that CDR's 46.9% base performance on SIMPLER-Bridge with a 7.5pp improvement from routing looks modest relative to those benchmarks. There's also a real limitation here: the contribution only applies within the mimic-video architecture family and requires variable-τ_v training, so it's not a general solution across different model families. Still, after eight rounds of addressing critical issues, the paper has solid grounding—the Pareto claims are honest, the DiT4DiT characterization is correct, and the auto-mode budget stays within constraints. Time to make a final call.

Looking at my independent scoring: novelty is 3/5 since the empirical study of τ_v* by manipulation phase is genuinely novel but the MLP router contribution is thin; feasibility is 3.5/5 with the timeline tight and empirical risk still present; clarity is strong at 4/5 with very explicit framing and honest limitations; impact is 3/5 given the modest gains on a small evaluation and a thin calibration savings argument. That averages to 3.4/5, which falls below the 4.0 threshold for acceptance. But this is round 8 of 10—the paper has made substantial progress and the core science is sound. My feedback needs to be focused and actionable, raising only genuinely new issues rather than rehashing old ground.

The structural limitations are real: the method itself is thin, the primary evaluation spans only 4 tasks, and the honest framing keeps the contribution modest. These can't be fixed in the remaining time. I can help fix the OA-WAM evaluation protocol claim, strengthen the CoRL positioning, and potentially broaden the evaluation within compute constraints, but the paper sits at the marginal acceptance threshold—it might get in, but the fundamental constraints make that uncertain.

Given we're in Round 8 of 10 with substantial revisions already done, I should give a "revise" verdict focused on what's actually fixable in the next 20 days before the CoRL deadline. The key empirical questions are whether Phase 1 shows strong per-phase variation and whether the 4-task SIMPLER-Bridge evaluation will be compelling enough for CoRL reviewers.

The main issues I'm flagging are moderate concerns about the OA-WAM evaluation protocol claim potentially being incorrect, the 4-task primary evaluation possibly falling short of the WAM track bar, and the paper's Pareto advantage now boiling down to "deployment calibration savings" (10 rollouts → 0), which is modest and needs a quantified deployment scenario to justify.

I'm second-guessing myself on the OA-WAM details though. The abstract doesn't specify tasks, but the proposal's landscape mentions very specific ones like Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket, and Visual Matching protocol. I need to verify whether these came from the actual paper or were invented, since I only got the abstract from the arXiv fetch.

Now I'm settling on my assessment scores. The novelty is around 3/5 because the Phase 1 empirical study on mimic-video architecture is genuinely novel, but the MLP router contribution is architecturally thin and the overall work is incremental given the existing landscape of competitors. Feasibility sits at 3.5/5 with the compute budget being a key constraint.

For clarity, I'm rating this 4/5 since the paper is now well-specified with explicit gate conditions and pre-registered predictions, though the narrative could be tighter. Impact lands at 3/5 because while the τ_v* study by manipulation phase is interesting, the performance gains of 7.5pp across 4 tasks are modest, and the calibration savings, though practically useful, are limited in scope.

That brings the average to 3.4/5, suggesting revision is needed. I'm flagging two moderate issues for the next round: first, there's a potential mismatch in how OA-WAM's evaluation protocol is characterized—the proposal claims it uses the same Visual Matching protocol on the 4 WidowX Bridge tasks, but my checks suggest it might actually use a causal slot-intervention test instead, which could undermine the 32pp gap attribution. Second, the primary Pareto claim of +7.5pp rests on only 4 tasks, which introduces high variance and seed-level fragility that CoRL reviewers will definitely push back on—I need to add error bars and robustness analysis.

The deployment calibration framing also needs work. The headline benefit of eliminating 10 rollouts per new task sounds good in theory, but at 10 minutes per rollout across 4 tasks, that's only 40 minutes saved—not particularly compelling without context. I should add a quantitative deployment cost analysis showing how many new tasks a typical robotics system encounters and what the actual rollout costs are per task to make this a stronger CoRL contribution.

There's also a minor title issue: "Zero-Shot Selective Denoising Activation" emphasizes the router as the main contribution, but if the prediction holds, most frames won't actually be activated and will stay at the default denoising level, so the title might be overselling how aggressive the approach is.

Now I'm reconsidering the final verdict. The paper has gone through 8 rounds of revisions with solid empirical work and an honest framing that doesn't oversell, plus it fits the compute budget and timeline. But it's missing a strong architectural innovation, only evaluates on 4 tasks, hasn't validated the zero-shot generalization from LIBERO to SIMPLER, and won't transform the field. At CoRL 2026 with a 22% acceptance rate and a competitive WAM track, this feels borderline—below the bar not because of fixable issues but because of fundamental structural limitations.

That said, "revise" doesn't mean asking for the impossible. The remaining concrete fixes are verifying the OA-WAM evaluation protocol, adding error bars for statistical robustness, and quantifying the deployment calibration savings. If those are addressed, the paper reaches its ceiling given its constraints. The real question is whether the empirical study alone provides enough novelty to justify acceptance despite the thin methodological contribution. Since we're at round 8 of 10 and approaching maximum achievable quality, I'm issuing "revise" with those specific actionable items, acknowledging the paper sits right at CoRL's boundary.

My scores reflect this: novelty and impact are both 3 because the empirical work is solid but the method itself is limited, feasibility is 3 due to unconfirmed zero-shot validation, and clarity is strong at 4. The four issues I'm flagging—the OA-WAM protocol verification, statistical fragility of the 4-task evaluation, missing quantification of calibration savings, and the potentially misleading title—are all concrete and fixable. Now I'm drafting the focused feedback around these actionable points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e50c4be-fcc6-443c-9003-d1262bc8b015",
  "isSidechain": false,
  "requestId": "req_011Catf6GpnKRhE8iMhJj9F6",
  "type": "assistant",
  "uuid": "6d087fa3-ee47-4c94-a006-376bc632c3b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HnXZe8KDBiRyD8XSgnTWCu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 51841,
      "output_tokens": 5459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5459,
          "cache_read_input_tokens": 51841,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 17 · 2026-05-10T09:34:49.096Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019iyEoD4sehC2sxWb4LJi8c`</summary>

```json
{
  "description": "Verify OA-WAM evaluation protocol and SIMPLER-Bridge task set",
  "subagent_type": "Explore",
  "prompt": "Please fetch the full text of arXiv:2605.06481 (OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation) and find:\n\n1. The exact SimplerEnv evaluation tasks used (which specific tasks?)\n2. Whether the evaluation uses \"Visual Matching\" protocol\n3. Whether the tasks include \"Spoon on Towel\", \"Carrot on Plate\", \"Stack Cube\", \"Eggplant in Basket\" (the WidowX Bridge tasks)\n4. The 79.3% breakdown per task if available\n\nFetch: https://arxiv.org/html/2605.06481v1 and look in the experimental sections.\n\nAlso try: https://arxiv.org/abs/2605.06481\n\nReport exact quotes from the experimental section about the evaluation setup."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d087fa3-ee47-4c94-a006-376bc632c3b3",
  "isSidechain": false,
  "requestId": "req_011Catf6GpnKRhE8iMhJj9F6",
  "type": "assistant",
  "uuid": "919b59c4-425a-4447-b660-ac8cca6d632e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HnXZe8KDBiRyD8XSgnTWCu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 51841,
      "output_tokens": 5459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5459,
          "cache_read_input_tokens": 51841,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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
  "leafUuid": "919b59c4-425a-4447-b660-ac8cca6d632e",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDR Phase 0 prior to CoRL 2026 commitment",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Tool result

_source line 20 · 2026-05-10T09:35:09.305Z_

<details><summary>↩ Tool result · `toolu_019iyEoD4sehC2sxWb4LJi8c`</summary>

```text
Excellent! I found the information. Based on the full PDF fetch, here are the answers to your questions:

## Findings from arXiv:2605.06481

**1. SimplerEnv Evaluation Tasks:**
The evaluation uses the **WidowX tasks** from SimplerEnv.

**2. Visual Matching Protocol:**
Yes - the evaluation protocol employed **visual matching** to assess task completion.

**3. WidowX Bridge Tasks:**
Yes, the evaluation includes all four of these tasks:
   - **Spoon on Towel**
   - **Carrot on Plate**
   - **Stack Cube**
   - **Eggplant in Basket**

**4. The 79.3% Breakdown:**
The paper reports **79.3% overall success** across these SimplerEnv WidowX manipulation benchmarks. However, the per-task breakdown is not provided in the available content - the paper presents this as an aggregate 79.3% success rate across the multiple manipulation scenarios tested.

The evaluation demonstrates that the OA-WAM model achieves robust performance on practical manipulation tasks using the visual matching protocol for task completion assessment on the WidowX robot platform.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919b59c4-425a-4447-b660-ac8cca6d632e",
  "isSidechain": false,
  "promptId": "7e098ab2-5565-40d9-9460-3fcce424727d",
  "type": "user",
  "uuid": "8ff1e774-7ca5-4b9b-9a57-cab9f334756b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please fetch the full text of arXiv:2605.06481 (OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation) and find:\n\n1. The exact SimplerEnv evaluation tasks used (which specific tasks?)\n2. Whether the evaluation uses \"Visual Matching\" protocol\n3. Whether the tasks include \"Spoon on Towel\", \"Carrot on Plate\", \"Stack Cube\", \"Eggplant in Basket\" (the WidowX Bridge tasks)\n4. The 79.3% breakdown per task if available\n\nFetch: https://arxiv.org/html/2605.06481v1 and look in the experimental sections.\n\nAlso try: https://arxiv.org/abs/2605.06481\n\nReport exact quotes from the experimental section about the evaluation setup.",
    "agentId": "a164c60426304d6e5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I found the information. Based on the full PDF fetch, here are the answers to your questions:\n\n## Findings from arXiv:2605.06481\n\n**1. SimplerEnv Evaluation Tasks:**\nThe evaluation uses the **WidowX tasks** from SimplerEnv.\n\n**2. Visual Matching Protocol:**\nYes - the evaluation protocol employed **visual matching** to assess task completion.\n\n**3. WidowX Bridge Tasks:**\nYes, the evaluation includes all four of these tasks:\n   - **Spoon on Towel**\n   - **Carrot on Plate**\n   - **Stack Cube**\n   - **Eggplant in Basket**\n\n**4. The 79.3% Breakdown:**\nThe paper reports **79.3% overall success** across these SimplerEnv WidowX manipulation benchmarks. However, the per-task breakdown is not provided in the available content - the paper presents this as an aggregate 79.3% success rate across the multiple manipulation scenarios tested.\n\nThe evaluation demonstrates that the OA-WAM model achieves robust performance on practical manipulation tasks using the visual matching protocol for task completion assessment on the WidowX robot platform."
      }
    ],
    "totalDurationMs": 20205,
    "totalTokens": 17000,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 15900,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 819
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 275,
          "cache_read_input_tokens": 15900,
          "cache_creation_input_tokens": 819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 819,
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
  "sourceToolAssistantUUID": "919b59c4-425a-4447-b660-ac8cca6d632e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T09:36:01.145Z_

<details><summary>Logged reasoning block</summary>

```text
Good. OA-WAM does indeed use:
- Visual Matching protocol ✓
- Same 4 WidowX Bridge tasks (Spoon on Towel, Carrot on Plate, Stack Cube, Eggplant in Basket) ✓
- 79.3% aggregate ✓

So the proposal's claim about OA-WAM using the same evaluation setup as SIMPLER-Bridge is verified correct. That's one concern resolved.

Now let me look at the proposal's per-task breakdown claim:
"OA-WAM: SimplerEnv WidowX Bridge Visual Matching (79.3% average: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%)"


The agent didn't find these per-task numbers in the paper, so either they came from supplementary materials my search missed or they were generated. I can't definitively rule out the latter, but given the limited search scope, I'll flag this as unverified rather than confirmed false. Now let me finalize what I've actually confirmed.

I've verified the OA-WAM evaluation uses visual matching on the same 4 tasks, confirmed τ_v routing exists, ruled out "Draft-and-Target Sampling" as a direct competitor since it's a different approach, and confirmed "Not All Frames Deserve Full Computation" is about general video processing, not robotics. The main remaining issues are the unverified per-task breakdown numbers for OA-WAM, the statistical fragility of claiming ≥7.5pp improvements across just 4 tasks without proper confidence intervals or multiple seeds, and the lack of concrete quantification around deployment calibration savings.

The "first empirical characterization" claim also needs tighter scoping—Phase 1 only applies to mimic-video's specific τ_v parametrization, while other WAM architectures like LingBot-VA and Fast-WAM don't use the same approach. For a competitive CoRL 2026 submission, this empirical study on a single architecture plus a 2-layer MLP sits at the acceptance threshold, and would need Phase 1 to surface genuinely surprising insights to justify the contribution.

Now I'm verifying a key factual claim: the proposal states that OA-WAM's SimplerEnv results and CDR's SIMPLER-Bridge results use identical task setups and evaluation protocols, which checks out. But the specific per-task breakdowns given for OA-WAM—Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%—couldn't be located by the agent, so I need to flag whether these are from an unfetched table, independently generated, or potentially fabricated.

For my final assessment: this proposal warrants revision. The phase-one empirical study on mimic-video architecture is novel, but the MLP router is architecturally lightweight, and it faces stiff competition from other WAM submissions at CoRL 2026 with more substantial innovations. Feasibility looks reasonable with compute staying within the 200-hour budget and a viable timeline for the MVS track, though the zero-shot generalization claim from LIBERO to SIMPLER-Bridge still needs empirical validation. The writing is generally clear.

On impact, the gains of 7.5+ percentage points across four tasks are modest, and while the calibration savings from 10 rollouts down to zero is practically useful, it needs better quantification. The contribution is somewhat narrow, limited mainly to the mimic-video family.

The main concern is that I can't independently verify the specific per-task numbers cited for OA-WAM—the proposal claims 83% on Spoon Towel, 71.1% on Carrot Plate, 65% on Stack Cube, and 98.2% on Eggplant Basket—so I'm flagging this as a moderate issue that needs resolution.

For the deployment angle, the "10 rollouts saved per task" framing is too vague for a CoRL venue without concrete numbers: how many new tasks does a typical robot deployment encounter, and what's the actual cost of those rollouts at scale? Without that grounding, reviewers won't see this as a compelling primary contribution.

The 4-task evaluation backing the ≥7.5pp Pareto improvement is concerning—I need to specify how many seeds per task, whether I'm reporting confidence intervals, and whether the gains hit p<0.05 significance. CoRL 2026 expects this rigor for robotics benchmarks.

Also, the "first empirical characterization" claim should be narrowed to just the mimic-video variable-τ_v architecture family, since other WAM variants like LingBot-VA and Fast-WAM use different parametrizations that don't expose τ_v as a tunable test-time parameter. The claim is sound but needs that scope to head off reviewer objections.

Now I need to verify those OA-WAM per-task numbers (83%, 71.1%, 65%, 98.2%) are actually pulled from arXiv:2605.06481's tables, and if not, I should either drop them or note that the paper only reports the 79.3% aggregate. Then I'll add a deployment cost breakdown showing how many rollouts CDR's zero-shot router saves across a realistic 3-month window with 20–50 new tasks, translating that savings to concrete dollars and calibration overhead eliminated.

For the evaluation rigor, I need to add statistical reporting to Phase 3—specifically the number of seeds and rollouts per task-baseline pair, plus 95% confidence intervals or standard deviations on success rates, since the +7.5pp improvement claim needs proper uncertainty bounds given the small 4-task scope. Finally, I should clarify that this characterization only applies to WAM architectures with logit-normal variable-τ_v augmentation like mimic-video and LingBot-VA, and doesn't extend to Fast-WAM or other variants that don't expose τ_v as a continuous test-time parameter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ff1e774-7ca5-4b9b-9a57-cab9f334756b",
  "isSidechain": false,
  "requestId": "req_011CatfG75RzPxVoHjjYghPB",
  "type": "assistant",
  "uuid": "c9f98d0f-2ba5-45fb-8312-9c0375b6c343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QrDrsoeUgW1Y62WRaoeQEe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5732,
      "cache_read_input_tokens": 53207,
      "output_tokens": 4678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4678,
          "cache_read_input_tokens": 53207,
          "cache_creation_input_tokens": 5732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5732
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

_source line 22 · 2026-05-10T09:36:45.680Z_

Now I have sufficient information to render my verdict. Let me synthesize my independent findings.

**Independent verification results:**
- OA-WAM (2605.06481): Visual Matching protocol on the same 4 WidowX Bridge tasks confirmed ✓
- Per-task numbers for OA-WAM (83%, 71.1%, 65%, 98.2%): not locatable in accessible text — unverified
- No direct competitor found for per-observation τ_v routing in robot WAMs ✓
- "Draft-and-Target Sampling" (2603.13438): different mechanism (draft/target trajectories, not noise-level routing), not a competitor ✓
- "Not All Frames Deserve Full Computation" (2604.02979): general video generation, not robot manipulation ✓
- Auto-mode estimate: confirmed at 150-175H, within ≤200H ✓
- DiT4DiT correction: confirmed applied correctly in Round 8 ✓

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "Phase 1 empirical study (first τ_v* characterization by manipulation phase on LIBERO-100) is genuinely first-of-kind for the mimic-video architecture family; no direct competitor for per-observation τ_v routing found. However, the MLP router is architecturally thin, and the contribution is scoped to one architecture's variable-τ_v property — the CoRL WAM track in 2026 has DiT4DiT, OA-WAM, MotuBrain, and Being-H0.7 with substantially broader architectural contributions."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Compute is within budget (auto-mode capped at 150-175H), MVS track exists, and Phase 0 gate appropriately scopes risk. However, the zero-shot LIBERO→SIMPLER-Bridge generalization claim (the primary CoRL contribution) remains empirically unvalidated at submission time, and the 4-task primary evaluation on SIMPLER-Bridge is statistically fragile without reported confidence intervals or seed counts."
    },
    "clarity": {
      "score": 4,
      "rationale": "The proposal is now extremely well-specified: explicit gate conditions, pre-registered predictions with asymmetric outcomes, honest Pareto framing (primary benefit is task success + calibration savings, not large compute savings), and correct characterization of all cited works. The honest framing is a strength."
    },
    "impact": {
      "score": 3,
      "rationale": "+≥7.5pp on 4 tasks with honest mean-τ_v close to 1.0 framing is a modest result; the reframed primary benefit ('10 rollouts → 0 per task') is a real practical contribution but lacks quantitative deployment-cost analysis to land as a compelling CoRL takeaway. The contribution is bounded to the mimic-video architecture family and unlikely to shift the broader WAM field."
    }
  },
  "issues": [
    "MODERATE — OA-WAM per-task numbers (Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%) could not be independently located in accessible arXiv:2605.06481 text. The aggregate 79.3% and Visual Matching protocol on the same 4 WidowX Bridge tasks were confirmed, but the per-task breakdown is unverified. If these numbers cannot be located in the paper's experimental tables, the proposal should either cite the specific table/figure or replace them with '79.3% aggregate (per-task breakdown not reported in OA-WAM).' Fabricated per-task numbers would be a citation integrity issue reviewers could flag.",
    "MODERATE — The primary reframed benefit ('10 rollouts → 0 per new task calibration') needs quantitative deployment-cost framing to carry CoRL weight. As written, the savings are: 4 SIMPLER-Bridge tasks × 10 rollouts = 40 rollouts eliminated. Without a scaling argument (N new tasks over a deployment lifetime, rollout wall-clock cost), this is not compelling to reviewers. A one-paragraph deployment cost analysis ('a robot deployed for 6 months accumulates ~50 new tasks; CDR eliminates ~500 calibration rollouts at $Y/hour wall-clock cost') is needed to frame this as a practically significant contribution rather than a marginal convenience.",
    "MODERATE — Statistical robustness of the 4-task SIMPLER-Bridge primary evaluation is not specified. The +≥7.5pp Pareto claim is over 4 tasks — a very small evaluation set for a CoRL 2026 WAM paper. The proposal does not state: (a) how many rollout seeds per task-baseline combination will be reported, (b) whether the improvement target (≥7.5pp) is a raw mean or statistically tested, (c) what confidence intervals or standard deviations will be reported. CoRL reviewers will ask for these in every review of a paper with 4-task primary results.",
    "MINOR — The 'first empirical characterization' claim is scoped to the mimic-video variable-τ_v architecture but is not stated as such in the framing. Adding one explicit sentence — 'This characterization applies to WAM architectures trained with logit-normal variable-τ_v augmentation; architectures that do not expose τ_v as a continuous test-time parameter (Fast-WAM) are architecturally incompatible with CDR's approach' — prevents reviewers from questioning why CDR's study doesn't generalize to all WAMs.",
    "MINOR — The paper now foregrounds the empirical study (Phase 1) as the primary contribution per the title, but the abstract structure still leads with the routing mechanism before the empirical finding. CoRL reviewers scan abstracts quickly; if the abstract's first contribution claim is 'zero-shot router,' they will assess it as a method paper and apply architectural novelty standards. The abstract should lead with: 'We present the first empirical study of which 3D manipulation phases require video denoising below τ_v=1 in WAMs, finding [key result from Phase 1]. Building on this, we introduce a zero-shot per-task router that recovers [X]pp of the per-task oracle gain without offline calibration rollouts.'"
  ],
  "feedback": "CDR has resolved all critical issues from Rounds 1-7 and is now scientifically sound with honest Pareto framing, correct DiT4DiT characterization, auto-mode budget within ≤200H, and comprehensive related-work coverage. Three targeted fixes are needed before submission:\n\n**Fix 1 (verify, 30 min): Confirm or remove OA-WAM per-task numbers.** Fetch arXiv:2605.06481's experimental tables and locate the per-task numbers (83%, 71.1%, 65%, 98.2%) in a specific table or figure. If locatable, cite the exact table number. If not found, remove per-task numbers and replace with 'OA-WAM 79.3% aggregate on the same four WidowX Bridge tasks (per-task breakdown not reported in OA-WAM).' Unverified specific numbers in related-work comparison tables are a red flag for reviewers.\n\n**Fix 2 (framing, 30 min): Quantify the deployment calibration savings argument.** The paper's primary reframed benefit is '10 rollouts → 0 per new task.' This needs a scaling argument to be compelling at CoRL: 'A robot system deployed in a warehouse or lab environment encounters N_new new manipulation tasks monthly. At 10 rollouts per task to calibrate the fixed τ_v, calibration cost grows linearly with N_new. CDR's zero-shot router eliminates this cost entirely, enabling zero-shot task extension without offline calibration. At N_new = 20 tasks/month and 30-minute rollout windows, CDR saves ~100 hours of robot time per month per system.' The exact numbers are illustrative — the key point is a concrete deployment scenario that makes the savings tangible rather than abstract.\n\n**Fix 3 (evaluation specification, 1 day): Add statistical reporting protocol to Phase 3.** In the Phase 3 section, explicitly state: 'We will run K=50 closed-loop rollouts per task per baseline, reporting mean ± standard deviation task success and Wilson confidence intervals. The +≥7.5pp target is a lower bound on the mean improvement; we will report significance at p<0.05 via a one-sided t-test.' Without this, reviewers will note that 4-task results are statistically fragile.\n\n**Fix 4 (abstract restructuring, 20 min): Lead abstract with the empirical finding, not the router.** Replace the current abstract structure with: 'We present the first empirical study of per-observation optimal video denoising depth (τ_v*) in World Action Models, finding [Phase 1 key result: e.g., grasp-phase frames require τ_v* ≈ X while approach frames cluster at τ_v*=1]. Building on this, we introduce CDR, a zero-shot per-task router that recovers ≥80% of the per-task oracle gain (+≥7.5pp on SIMPLER-Bridge) without offline calibration rollouts, eliminating 10 rollouts-per-task deployment cost.' This frames CDR as an empirical contribution (which it is) rather than an architecture paper.\n\nWith these four fixes, CDR is at its maximum achievable quality within the 20-day constraint. The paper's ultimate CoRL fate will depend on whether Phase 1 reveals genuinely surprising per-phase variation — if the τ_v* histograms show clear grasp-vs-approach clustering, the paper strengthens significantly; if variation is weak, the MVS track (per-task CDR zero-shot + pre-registered P1 confirmation) is the submission path.",
  "reason": "All Round 1-7 critical issues are resolved; Round 8 reveals three actionable moderate issues (OA-WAM per-task numbers unverified, deployment calibration savings lacking quantification, 4-task evaluation lacking statistical specification) that must be fixed before submission to avoid predictable reviewer objections in the competitive CoRL 2026 WAM track."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9f98d0f-2ba5-45fb-8312-9c0375b6c343",
  "isSidechain": false,
  "requestId": "req_011CatfG75RzPxVoHjjYghPB",
  "type": "assistant",
  "uuid": "5e4ff06c-a507-4301-a764-05083bb88c00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QrDrsoeUgW1Y62WRaoeQEe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5732,
      "cache_read_input_tokens": 53207,
      "output_tokens": 4678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4678,
          "cache_read_input_tokens": 53207,
          "cache_creation_input_tokens": 5732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5732
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
  "leafUuid": "5e4ff06c-a507-4301-a764-05083bb88c00",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CDR Phase 0 prior to CoRL 2026 commitment",
  "sessionId": "012ce64b-5c43-497f-abb0-193915a80ee0"
}
```

---
