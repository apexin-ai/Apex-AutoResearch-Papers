# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/f75f2c79-032b-4734-882a-e5ef8515319c.jsonl`
- **Structured JSON:** [`76824cc61023ae7e0f66.json`](../../sessions/76/76824cc61023ae7e0f66.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:47:31.322Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:47:31.322Z",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World Action Models (WAMs) — joint world modeling and action prediction in a unified architecture, often built on video diffusion priors. In-scope: unified video+action prediction, MoT (Mixture-of-Transformers) architectures with text/video/action streams, WMs that double as policies via inverse dynamics on imagined futures, action-conditioned video diffusion as policy.\n\nRecent landscape (do not duplicate): UniVLA, DreamVLA, GigaBrain-0.5M, DiT4DiT, MotuBrain, video-diffusion-as-policy lines. WAMs are the hottest CoRL 2026 area — high competition but high reward.\n\nContribution type: METHOD ONLY. New unified architecture, new training scheme that fuses world prediction and action prediction, new inference algorithm extracting actions from imagined futures.\n\nSIM-ONLY MITIGATION: WAM papers at CoRL routinely use sim envs since the method depends on data scale, not real-robot deployment. Use LIBERO/ManiSkill as primary and frame contribution as architectural.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Most challenging budget — video models are heavy. Strategies: (a) fine-tune an open video WM (Cosmos releases, OpenSora, CogVideoX) with action conditioning, (b) distill a large WAM into a smaller one, (c) propose a method that requires only small additional training on top of an existing WAM, (d) propose an inference-time method that needs no training.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos.\n3. Eval: LIBERO, ManiSkill 2/3, RoboCasa for closed-loop control + video prediction quality (PSNR/SSIM/FVD on action-conditioned futures). Compare against UniVLA / DreamVLA / DiT4DiT lineage if open releases exist.\n\nLook for: efficient action-conditioning of video diffusion, latent WAMs that bypass pixel decoding, methods that share representations across world and action streams. Avoid: trivial action-token prepending without architectural insight.\n\nTag: direction=world_action_model, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation\",\n  \"core_problem\": \"Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. This paper exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\\n\\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. The per-task breakdown (Table I, arXiv:2512.15692) reveals strong task heterogeneity: Stack Blocks 12.5%→29.2% (+16.7pp), Carrot on Plate 37.5%→54.2% (+16.7pp), Spoon on Towel 37.5%→41.7% (+4.2pp), Eggplant in Basket 100%→100% (+0pp — already saturated at τ_v=1). This heterogeneity is the core motivation for CDR: Eggplant in Basket requires no video denoising below τ_v=1 (already at ceiling), while Stack Blocks and Carrot on Plate strongly benefit from lower τ_v. A per-task router that correctly identifies these task types recovers most of the +9.4pp oracle gain without the 10-rollout-per-task calibration cost. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\\n\\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical (analogous to CDR routing Eggplant to τ_v=1 while Stack Blocks to τ_v<1); (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. This paper addresses the third cost: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task oracle justifies it, and eliminate the 10-rollout-per-task deployment calibration cost via a zero-shot router trained on LIBERO-100.\\n\\nCRITICAL PARETO FRAMING CLARIFICATION (required for reviewer accuracy): If the pre-registered prediction P1 is confirmed (fixed intermediate τ_v < 1 underperforms τ_v=1 on SIMPLER-Bridge — the expected outcome per mimic-video main text), then the zero-shot router routes the MAJORITY of frames to τ_v=1. This means: (a) mean τ_v consumed by CDR stays CLOSE TO 1.0; (b) per-inference GPU compute savings are SMALL (5–10% at most); (c) the primary benefit is TASK SUCCESS RECOVERY (+≥7.5pp zero-shot on SIMPLER-Bridge) and DEPLOYMENT CALIBRATION SAVINGS (10 offline rollouts per new task → 0). The abstract and introduction MUST state this explicitly. CDR's Pareto dominance vs. τ_v=1 is: same or slightly lower mean τ_v consumed, significantly higher task success — not a large speedup per inference call.\\n\\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Table 1 of arXiv:2605.06481: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.\",\n  \"opportunity\": \"The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. This paper exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\\n\\nThe per-task mimic-video breakdown (Table I, arXiv:2512.15692) provides direct motivation for the selective routing thesis: Eggplant in Basket reaches 100% at τ_v=1 and gains nothing from per-task tuning (+0pp); Stack Blocks and Carrot on Plate each gain +16.7pp; Spoon on Towel gains only +4.2pp. This pattern shows that some tasks have saturated performance at τ_v=1 (Eggplant), some are precision-critical and need lower τ_v (Stack Blocks, Carrot), and some fall between (Spoon). A per-task router that correctly identifies task difficulty profile recovers most of the +9.4pp oracle aggregate gain by routing precision-critical tasks to lower τ_v while leaving non-critical tasks at τ_v=1.\\n\\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. The primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost.\\n\\nCRITICAL: THE DEPLOYMENT EFFICIENCY GAIN IS CALIBRATION COST, NOT PER-INFERENCE COMPUTE. When P1 is confirmed (the expected outcome), CDR routes most frames to τ_v=1, keeping mean τ_v close to 1.0. The efficiency improvement CDR delivers is: eliminating the 10-offline-rollout per-task sweep required to find the optimal fixed τ_v for a new task. A new task can be deployed with ZERO rollouts using the zero-shot router, rather than requiring 10 rollouts to calibrate the best fixed τ_v. This is a real and practically important contribution — robotics deployments accumulate many new tasks, and even at 10 rollouts each, calibration cost is significant — but it is DIFFERENT from 'faster inference per call.' The paper's framing must be explicit: 'CDR saves deployment calibration cost (10 rollouts → 0 per new task) and recovers task success (+≥7.5pp zero-shot), not primarily per-inference GPU compute.'\\n\\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, this paper also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies the competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. The Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the tasks/frames that need it, without any offline rollout cost.'\\n\\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. deployment-calibration-rollouts Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\\n\\nThe primary scientific contribution is Phase 1: the FIRST empirical characterization of which 3D manipulation phases require video denoising below the τ_v=1 fixed-global default, using GT-action-referenced τ_v labeling across LIBERO-100. This characterization applies specifically to WAM architectures trained with logit-normal variable-τ_v augmentation (such as mimic-video); architectures that do not expose τ_v as a continuous test-time parameter (e.g., Fast-WAM, which removes the video backbone at test time via architectural retraining) are not architecturally compatible with CDR's per-observation routing and are excluded from this characterization by design. The zero-shot router is the deployment mechanism enabling practical use of Phase 1's findings without offline sweeps — not the architectural novelty. The paper should be read as an empirical methods contribution, not an architectural one.\",\n  \"landscape\": \"LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is the primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\\n\\nmimic-video (arXiv:2512.15692, Dec 2025) is the base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — this paper's contribution is approximating the per-task oracle via zero-shot routing; (d) Table I (mimic-video) provides per-task breakdown for the τ_v=1 baseline and per-task oracle: Stack Blocks 12.5%→29.2% (+16.7pp), Carrot on Plate 37.5%→54.2% (+16.7pp), Spoon on Towel 37.5%→41.7% (+4.2pp), Eggplant in Basket 100%→100% (+0pp) — this per-task heterogeneity directly validates CDR's selective routing thesis; (e) per-task sweep yields +9.4pp aggregate (46.9%→56.3%); (f) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\\n\\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\\n\\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%: Spatial 98.9%, Object 99.0%, Goal 97.4%, Long 95.9%) and SimplerEnv WidowX Bridge Visual Matching (Table 1 of arXiv:2605.06481: 79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching, Table 1 of arXiv:2605.06481); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\\n\\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\\n\\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\\n\\nDiT4DiT (arXiv:2603.10448) ablation (Figure 8b): fewer ACTION denoising steps yield higher task success — this finding concerns the action diffusion process, NOT τ_v (video noise level). These are orthogonal efficiency axes. CDR cites DiT4DiT only as a structural analogy: in both the action domain (DiT4DiT) and the video domain (mimic-video τ_v=1 main-text finding), less denoising tends to be preferable as a global default. CDR does NOT use DiT4DiT to corroborate τ_v=1 video noise optimality; these are different axes and conflating them would be factually incorrect. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\\n\\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\\n\\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\\n\\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) introduces a per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing.\\n\\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1 in WAMs trained with logit-normal variable-τ_v augmentation; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.\",\n  \"approach\": \"CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\\n\\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\\n\\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\\n\\nDecision gate (by May 12):\\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full selective activation story is empirically supported. Proceed to Phase 1.\\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\\n\\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\\n\\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\\n\\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases. The mimic-video per-task breakdown (Table I: Stack Blocks +16.7pp, Carrot on Plate +16.7pp, Spoon on Towel +4.2pp, Eggplant +0pp from per-task tuning) provides task-level priors: precision manipulation tasks (Stack Blocks, Carrot on Plate) are expected to show stronger clustering of τ_v*(f) < 0.9 than already-saturated tasks (Eggplant in Basket). Phase 1 confirms whether this task-level heterogeneity extends to within-task phase-level variation.\\n\\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\\n\\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\\n\\n[SCOPE NOTE]: This characterization applies to WAM architectures trained with logit-normal variable-τ_v augmentation; architectures that do not expose τ_v as a continuous test-time parameter (e.g., Fast-WAM, which removes the video backbone at test time entirely) are architecturally incompatible with CDR's per-observation routing. The paper explicitly states this scope in the introduction: 'CDR's empirical findings characterize WAMs under logit-normal variable-τ_v training; this scope does not extend to architectures that eliminate τ_v as a test-time degree of freedom via retraining.'\\n\\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\\n\\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\\n\\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\\n\\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1} and θ ∈ {0.5, 0.7} to trace the accuracy-efficiency frontier (reduced from full grid to fit within compute budget).\\n\\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\\n\\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\\n\\nZero-shot claim gate:\\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\\n\\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\\n\\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: The primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1'). The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding. NOTE: DiT4DiT's ablation (Figure 8b, about action denoising steps — not τ_v) is NOT cited as corroborating evidence for P1; mimic-video's main text alone anchors this prediction.\\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\\n\\n[CRITICAL PARETO HONESTY REQUIREMENT] If P1 is confirmed (the expected outcome): CDR routes the majority of frames to τ_v=1. Mean τ_v consumed by CDR stays close to 1.0. Per-inference GPU compute savings are SMALL (approximately 5–10%). The primary benefit CDR provides is: (1) TASK SUCCESS RECOVERY: +≥7.5pp zero-shot on SIMPLER-Bridge vs. τ_v=1; (2) DEPLOYMENT CALIBRATION SAVINGS: eliminates 10 offline rollouts per new task required to identify optimal fixed τ_v. The abstract, introduction, and Phase 3 results section MUST state this explicitly. The Pareto curve axis framing should reflect this: if P1 confirmed, the x-axis showing 'mean τ_v consumed' will show CDR close to τ_v=1 with small compute savings; the y-axis showing task success will show the +≥7.5pp gain. This is still a Pareto win (same compute, better performance) but is NOT primarily an efficiency contribution — it is a zero-shot deployment automation contribution that recovers task success without offline rollout cost.\\n\\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR recovers per-task oracle gains zero-shot — same inference compute, +≥7.5pp task success, zero offline calibration rollouts.'\\n\\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim — if confirmed, CDR also delivers genuine per-inference compute savings. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\\n\\nBaselines:\\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\\n(e) Per-observation CDR (full system)\\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\\n\\n[STATISTICAL REPORTING PROTOCOL — REQUIRED]: We will run K=50 closed-loop rollouts per task per baseline (4 tasks × 6 baselines = 1,200 total rollouts in SIMPLER-Bridge). Per-task success rate treated as Bernoulli variable; report mean ± standard deviation per task and aggregate mean ± standard error. Confidence intervals: Wilson CI at 95% for per-task binary success rates (preferred over normal approximation for small K). Primary significance test: one-sided paired t-test across tasks (H₀: CDR mean success ≤ τ_v=1 mean success), threshold p<0.05. The +≥7.5pp target is stated as a lower bound on the mean improvement; statistical significance is reported separately from the threshold claim to maintain interpretability. Power analysis: K=50 provides ~80% power to detect a 7.5pp improvement over 46.9% baseline at α=0.05 (normal approximation to binomial: σ≈√(0.469×0.531/50)≈0.071 per task; standardized effect size ≈1.06). Per-task breakdown is reported alongside aggregate (as mimic-video Table I reports per-task numbers) to enable reviewers to assess whether improvement concentrates on specific tasks (e.g., Stack Blocks, Carrot on Plate — consistent with their +16.7pp per-task oracle gains in Table I of arXiv:2512.15692) or is distributed. Secondary LIBERO-100 evaluation (100 tasks, 50 demonstrations each in held-out set) provides substantially higher statistical power for the within-LIBERO 80/20 router validation and is reported with per-task-type breakdown.\\n\\n[DEPLOYMENT CALIBRATION COST QUANTIFICATION — REQUIRED FOR CoRL FRAMING]: CDR's primary reframed benefit is elimination of per-task τ_v calibration rollouts. This requires a concrete deployment-scale argument to carry CoRL weight. A robot system in a warehouse or lab environment accumulates new manipulation task specifications regularly as it is extended to new objects, placements, and scenarios. Under mimic-video's default workflow, each new task requires 10 closed-loop rollouts to sweep τ_v ∈ {0.5, 0.7, 0.9, 1.0} and identify the optimal fixed-global value — a protocol requiring human setup, rollout execution, and reset between attempts. In real-robot deployment contexts, each rollout consumes ~15 minutes of robot time (execution + object reset + operator oversight), yielding ~2.5 robot-hours of calibration overhead per new task. At N_new = 20 new task specifications per month per robot (a conservative estimate for a warehouse or multi-object lab system): 50 robot-hours/month devoted purely to τ_v calibration, not productive manipulation. Across a 10-robot fleet over a 6-month deployment period: ~3,000 calibration rollouts, 3,000 robot-hours, and significant operator cost — all eliminated by CDR's zero-shot router. Even at simulation-only deployment (no real-robot cost), the 10-rollout overhead multiplied by a growing task library (50+ tasks/year per system) represents a meaningful engineering cost that CDR eliminates entirely. The savings scale linearly with fleet size and deployment lifetime: CDR enables zero-day task deployment — immediately after task specification, with no calibration period — which is qualitatively different from the 'deploy after calibration' workflow mimic-video requires. The introduction and contribution list must state this concretely: 'CDR eliminates 10 rollouts × N_new tasks of deployment overhead, enabling zero-shot task extension without calibration, at no backbone retraining cost.'\\n\\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. Per-task breakdown reported alongside aggregate (consistent with mimic-video Table I format). LIBERO-100 results reported secondarily for comparability. Key empirical claims:\\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: same inference compute as τ_v=1, +≥7.5pp task success, zero offline calibration rollouts — when P1 confirmed, the compute savings (mean τ_v consumed below 1.0) are modest but the task success gain is the primary result\\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in logit-normal variable-τ_v WAMs\\n\\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (Table 1 of arXiv:2605.06481, SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Table 1 of arXiv:2605.06481); the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\\n\\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story). [RoboCasa results and full per-phase heatmap ablations are explicitly dropped from CoRL submission to stay within compute budget — these move to ICLR 2027 extended version if applicable.]\\n\\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in logit-normal variable-τ_v WAMs (Phase 1 study) and the zero-shot deployment automation that eliminates offline calibration rollouts, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\\n\\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default, scoped to logit-normal variable-τ_v WAMs)\\n- Phase 2 router training + 80/20 held-out validation result\\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge, reported with K=50 rollouts per point and Wilson CIs\\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time' in logit-normal variable-τ_v WAMs; (2) zero-shot per-task CDR on SIMPLER-Bridge eliminating 10 offline calibration rollouts; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\\n\\n**Timeline for CoRL 2026 (May 29 deadline):**\\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\\n- Phase 0 gate decision: May 12\\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\\n- Zero-shot claim gate decision: May 19\\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation; K=50 rollouts per point maintained for statistical protocol)\\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\\n- Buffer: May 29 submission\\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines with K=50 rollouts per baseline point, NO RoboCasa; ~20h buffer for reruns)\",\n      \"gpu_utilization\": \"45–55% effective — GPUs idle during Phase 0 gate decision, phase annotation, zero-shot gate decision, and result inspection\",\n      \"timeline\": \"2–3 weeks to CoRL submission (if Phase 0 positive by May 12); 2–3 months to ICLR 2027 otherwise\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$305 (122h × $2.49/hr spot H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~93 H100-hours\",\n      \"gpu_utilization\": \"65–75% — agent runs Phase 1 while human reviews Phase 0 gate; Phase 2 queued immediately after Phase 1 labels available; 80/20 validation runs in parallel with router training\",\n      \"timeline\": \"12–15 days to CoRL submission (Phase 0 gate on day 2, Phase 1 complete day 9, Phase 2 zero-shot gate day 10, Phase 3 complete day 15)\",\n      \"team\": \"1 researcher, ~20 min/day check-in\",\n      \"claude_api_cost\": \"~$100–200 (~1,000–2,000 turns at $0.10/turn Opus 4.7)\",\n      \"estimated_gpu_cost\": \"~$232 (93h × $2.49/hr spot H100)\",\n      \"risk_note\": \"Two critical decision points: (1) Phase 0 gate by May 12 — if <10% activation frames, reframe to zero-shot per-task routing, target ICLR 2027. (2) Phase 2 zero-shot gate by May 19 — if 80/20 LIBERO held-out validation fails (<80% τ_v* recovery), reframe primary zero-shot claim to few-shot SIMPLER-Bridge adaptation before committing it in the paper. Human judgment at both gates is essential. If Phase 1 takes 8 days (upper bound), MVS track is the fallback — dropping per-observation CDR and full ablations to submit the Phase 1 histograms + per-task CDR + pre-registered prediction result. Critical path has no slack beyond MVS; prioritize per-task CDR zero-shot result over per-observation CDR in Phase 3.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~150–175 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 55h; Phase 2 with reduced λ×θ grid (λ∈{0.01,0.1} × θ∈{0.5,0.7}) plus 80/20 validation: 8h; Phase 3 SIMPLER-Bridge + LIBERO primary results only — NO RoboCasa, NO full per-phase heatmap ablations, K=50 rollouts per baseline point for statistical protocol compliance: 70h; buffer: 15h). SCOPE REDUCTION vs. prior 410H estimate: RoboCasa evaluation dropped, full 3×3 λ×θ hyperparameter grid dropped (reduced to 2×2), extensive per-phase heatmap ablations moved to ICLR 2027 extended version. This fits within the ≤200H project constraint.\",\n      \"gpu_utilization\": \"Near-zero idle — phases pipelined\",\n      \"timeline\": \"3–5 days with 8 H100s\",\n      \"team\": \"0 (only initial sweep grid and eval harness setup required)\",\n      \"claude_api_cost\": \"~$200–400 (~2,000–4,000 turns)\",\n      \"estimated_gpu_cost\": \"~$410 (165h × $2.49/hr spot H100)\",\n      \"risk_note\": \"Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections. Auto mode must NOT interpret CDR's benefit as 'inference-time compute savings' if P1 is confirmed — the honest framing is 'deployment calibration cost savings (10 rollouts → 0 per new task, eliminating ~2.5 robot-hours per new task in real-robot settings) and task success recovery (+≥7.5pp), with mean τ_v consumed remaining close to 1.0.' Auto mode must enforce K=50 rollouts per task per baseline in Phase 3 and report Wilson CIs and one-sided t-test significance alongside mean ± SD.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)\",\n    \"ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I provides per-task breakdown for both τ_v=1 baseline and per-task oracle: Stack Blocks 12.5%→29.2% (+16.7pp), Carrot on Plate 37.5%→54.2% (+16.7pp), Spoon on Towel 37.5%→41.7% (+4.2pp), Eggplant in Basket 100%→100% (+0pp) — this per-task heterogeneity directly motivates CDR's selective routing (saturated tasks stay at τ_v=1; precision tasks benefit from lower τ_v); Table I does NOT include fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp aggregate (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining\",\n    \"LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge\",\n    \"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; per-task numbers verified in Table 1 of arXiv:2605.06481: 79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2% (SimplerEnv WidowX Bridge Visual Matching). LIBERO: 97.8% (Spatial 98.9%, Object 99.0%, Goal 97.4%, Long 95.9%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup; cite Table 1 specifically when referencing these numbers. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.\",\n    \"A₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model (arXiv:2604.05672, April 2026) — MUST CITE as concurrent work; applies per-observation Inter-Layer Truncated Flow Matching with early exit for VLA backbone computation, achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION: A₁ targets how many transformer layers to execute in a VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth routing) — orthogonal efficiency axes on different model families (VLAs vs WAMs).\",\n    \"VADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) — adapts ACTION diffusion denoising steps per task stage (shorter for simple, longer for complex); evaluated on Push-T, Adroit, ARX5; DIFFERENTIATION: VADF targets action denoising steps, CDR targets video backbone denoising depth (τ_v) — orthogonal efficiency axes, combinable\",\n    \"Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (arXiv:2603.30043) — 2D commitment motivation: video diffusion commits high-level plan in first few denoising steps; CDR extends and empirically validates for 3D manipulation video backbones\",\n    \"DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control (arXiv:2603.10448) — CDR cites as structural analogy only; DiT4DiT's ablation (Figure 8b) shows that fewer ACTION denoising steps yield higher task success — this is about action diffusion steps, NOT τ_v (video noise level). IMPORTANT: DiT4DiT does NOT corroborate τ_v=1 video noise optimality — these are orthogonal efficiency axes. CDR's related work may note: 'DiT4DiT finds fewer action denoising steps improve task success in the action domain; we investigate the analogous question in the video backbone domain.' Any language claiming DiT4DiT 'independently confirms' high-τ_v video optimality is FACTUALLY INCORRECT and must not appear in the paper. 98.6% LIBERO, 50.8% RoboCasa.\",\n    \"DreamZero: World Action Models are Zero-shot Policies (arXiv:2602.15922, Feb 2026) — velocity caching within denoising trajectory; complementary to CDR (reduces cost within a fixed τ_v level vs. CDR selecting τ_v level before denoising begins)\",\n    \"Denoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) — introduces Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions advance denoising earlier, harder regions receive more steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory frames — which frames need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined. Cited as feasibility motivation only; evaluates image generation, not robot action models.\",\n    \"MotuBrain (arXiv:2604.27792) — unified VAM with Mixture-of-Transformers (MoT) architecture under UniDiffuser formulation; supports policy learning, world modeling, video generation, inverse dynamics; 95.8%+ on RoboTwin 2.0; 50× speedup via step reduction, FP8 quantization. DIFFERENTIATION: training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on frozen mimic-video checkpoint requiring no retraining. Orthogonal — MotuBrain could serve as future CDR base model.\",\n    \"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (arXiv:2508.06804) — adapts ACTION (not video) denoising steps via RL; orthogonal efficiency axis to CDR\",\n    \"S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight (arXiv:2603.16195, Mar 2026) — distillation-based efficiency; requires retraining\",\n    \"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694) — X-WAM; fixed-distribution ANS baseline; not per-observation adaptive\",\n    \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv:2504.02792) — UWM; fixed schedule baseline\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078) — distillation-based; different efficiency axis; 99.2% LIBERO, 62.1% RoboCasa\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv:2605.06222) — introduces per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing\"\n  ],\n  \"description\": \"We present the first empirical study of per-observation optimal video denoising depth (τ_v*) in World Action Models trained with logit-normal variable-τ_v augmentation, finding systematic manipulation-phase structure: [Phase 1 result — e.g., grasp-phase and precision-manipulation frames cluster at τ_v* ≈ 0.4–0.7 while approach/transport frames cluster at τ_v*=1.0 across LIBERO-100]. This characterization is scoped to WAMs with continuous test-time τ_v control (mimic-video family); architectures that eliminate τ_v as a test-time parameter via retraining (Fast-WAM) are outside CDR's scope by design. Building on this empirical foundation, we introduce CDR (Conditional Depth Routing), a zero-shot per-task router that recovers ≥80% of the per-task oracle gain (+≥7.5pp on SIMPLER-Bridge) without offline calibration rollouts, eliminating the 10-rollout-per-task deployment cost of mimic-video's per-task sweep.\\n\\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view. These are compatible: τ_v=1 wins when one fixed value is applied globally, but the per-task oracle τ_v distribution peaks at intermediate levels. The mimic-video per-task breakdown (Table I of arXiv:2512.15692) reveals strong task heterogeneity motivating CDR's selective approach: Stack Blocks 12.5%→29.2% (+16.7pp) and Carrot on Plate 37.5%→54.2% (+16.7pp) strongly benefit from per-task τ_v tuning; Eggplant in Basket 100%→100% (+0pp) is already saturated at τ_v=1; Spoon on Towel gains only +4.2pp. The +9.4pp aggregate oracle gap (46.9%→56.3% on SIMPLER-Bridge) is driven by precision-demanding tasks, not uniform improvement — exactly the selectivity CDR's router exploits.\\n\\nCRITICAL PARETO FRAMING (enforced throughout): When pre-registered prediction P1 is confirmed (the expected outcome per mimic-video main text), CDR routes most frames to τ_v=1, keeping mean τ_v consumed close to 1.0. Per-inference compute savings are small (5–10%). CDR's primary benefits are: (1) TASK SUCCESS RECOVERY — +≥7.5pp zero-shot on SIMPLER-Bridge; (2) DEPLOYMENT CALIBRATION SAVINGS — eliminating 10 offline rollouts per new task (~2.5 robot-hours per task in real-robot settings; ~100 robot-hours/month at N_new=20 new tasks/month per robot across a fleet). The paper DOES NOT claim large per-inference speedups when P1 is confirmed. This distinction is stated explicitly in the abstract and introduction.\\n\\nTwo pre-registered predictions before Phase 3: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text. If P1 confirmed, CDR's Pareto claim is: same inference compute, +≥7.5pp task success, zero offline calibration rollouts. (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\\n\\nStatistical protocol: K=50 rollouts per task per baseline (1,200 total), Wilson CI at 95%, one-sided paired t-test (p<0.05), per-task breakdown reported alongside aggregate. K=50 provides ~80% power to detect the 7.5pp target improvement at α=0.05.\\n\\nThe primary empirical contribution is Phase 1: first systematic study of τ_v* across LIBERO-100 with manipulation-phase breakdown in logit-normal variable-τ_v WAMs. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot per-task generalization, not the central architectural novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point, with per-task breakdown (consistent with mimic-video Table I format).\\n\\nDiT4DiT (arXiv:2603.10448) is cited as structural analogy only: its ablation (Figure 8b) shows fewer action denoising steps improve task success in the action domain — a parallel finding that less denoising can be globally preferable. DiT4DiT does NOT corroborate τ_v=1 video noise optimality directly; these are orthogonal efficiency axes and must not be conflated.\\n\\nOA-WAM (arXiv:2605.06481, Table 1) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing contribution. All OA-WAM per-task numbers (Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%) are verified in Table 1 of arXiv:2605.06481. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.\",\n  \"project_name\": \"commit_depth_router\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Missing mimic-video (arXiv 2512.15692, Dec 2025): This paper introduces partial denoising for video-action models with a fixed τ_v, empirically sweeps noise levels, and finds τ_v=1 (maximum noise, single forward pass) is the best default for manipulation. This is the direct prior art for CDR's core mechanism and is entirely absent from the Generator's landscape. Reviewers will view CDR's per-sample adaptation as incremental relative to this.\", \"CRITICAL — Missing DreamZero (arXiv 2602.15922, Feb 2026): DreamZero uses cosine-similarity-based velocity caching to reduce effective DiT steps from 16→4 in a WAM, achieving 38× total speedup. This is an adaptive WAM step-reduction method that the Generator does not cite or differentiate against.\", \"CRITICAL — Action decoder distribution shift: DiT4DiT's action decoder is trained to take features from a single, fixed video noise level (the forward-hook timestep). Running this frozen decoder on intermediate hidden states from 10 different noise levels during CDR's calibration sweep will yield features outside the training distribution, making the per-sample optimum labels unreliable. Addressing this requires fine-tuning the action decoder across multiple noise levels, which would substantially increase the compute budget.\", \"MAJOR — ChEaP generalization is an unverified assumption: ChEaP (arXiv 2603.30043) demonstrates early trajectory commitment in 2D maze-solving only. The Generator treats this as established fact for 3D robot manipulation, but 3D manipulation requires fine-grained 6-DoF actions that may not be committed early in the diffusion trajectory. This empirical validation step (showing commitment exists and is task-specific in 3D manipulation WAMs) is actually a significant contribution that the Generator treats as motivation rather than as a required result.\", \"MAJOR — If τ_v=1 already works best (mimic-video finding), CDR's entire premise weakens: CDR assumes the optimal video noise level varies meaningfully per observation. But mimic-video shows that the highest noise level (no denoising, trivial single pass) is the best default for action extraction in manipulation — meaning the 'commitment phenomenon' may not produce meaningful variation across observations, making per-sample routing unnecessary.\", \"MODERATE — Compute budget is tight and likely underestimated: 30 H100-hours for the calibration sweep (10 noise levels × LIBERO-100 × ≥50 demos per task × full action decoder rollouts) is optimistic. Actual cost depends on whether evaluation is parallelized per environment instance, and LIBERO simulation evaluation is single-threaded per instance as acknowledged.\", \"MODERATE — CoRL 2026 deadline discrepancy: The Generator states abstract deadline May 25/paper May 28; the actual CoRL 2026 deadlines are abstract May 26/paper May 29. This is minor but suggests the Generator may be working from cached information.\", \"MODERATE — The Pareto loss formulation (L = (1 − success_at_t*) + λ·(t*/T)) trains the router with a convex combination of two objectives, but success_at_t* is a non-differentiable reward requiring policy rollouts or a surrogate. The training procedure for the router is underspecified regarding how this gradient flows.\"]\nFeedback: CDR addresses a real efficiency gap in WAMs but needs two major revisions before it can be competitive at CoRL 2026:\n\n1. **Cite and differentiate against mimic-video and DreamZero.** mimic-video (arXiv 2512.15692) already shows that stopping video denoising at an intermediate noise level τ_v is beneficial for action extraction and empirically sweeps τ_v values. CDR must be framed as: 'mimic-video shows fixed τ_v works; we show per-sample adaptive τ_v yields further Pareto improvements.' DreamZero (arXiv 2602.15922) must be cited as an adaptive step-reduction baseline.\n\n2. **Address the action decoder distribution shift.** CDR cannot run a frozen DiT4DiT action decoder on features from arbitrary noise levels without retraining. Two viable paths: (a) Fine-tune the action decoder jointly across 3–5 noise levels during the CDR calibration phase (adds ~20–40 H100-hours but fixes the distribution shift); or (b) Reframe CDR as working on mimic-video-style architectures where the action decoder is already designed to handle variable-τ_v inputs — this is the cleaner path since mimic-video's τ_v is fixed and CDR adds per-sample adaptation.\n\n3. **Empirically validate commitment in 3D manipulation.** Add a section showing that intermediate features in DiT4DiT or a similar WAM actually carry sufficient action information before full denoising, as a function of task complexity. This turns the key assumption into a publishable finding. If the data shows commitment is task-uniform (all tasks commit at the same depth), CDR's per-sample routing argument collapses — which is important to know before the deadline.\n\n4. **Sharpen the differentiation from mimic-video.** The cleanest pitch: 'mimic-video sets τ_v globally. We show that per-task and per-observation optimal τ_v varies by 2–5× (empirical result), and a 2-layer MLP router recovers 97% of per-sample-optimal performance at near-zero overhead.' If the empirical variation is small, the paper weakens significantly, so validate this first.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Missing LingBot-VA (arXiv 2601.21998, RSS 2026): LingBot-VA introduces Noisy History Augmentation, training the action decoder on partially noisy video latents and enabling fixed τ_v=0.5 inference-time halving — achieving 98.5% on LIBERO. This is the most directly overlapping prior work with CDR's core mechanism (action decoding from intermediate noisy video). The Generator's landscape claims 'no existing VAM paper learns to predict per-observation optimal τ_v automatically' — true, but LingBot-VA already demonstrates the key enabling mechanism (action decoding from noisy video) with a fixed threshold. CDR must differentiate: LingBot-VA sets a universal fixed τ_v=0.5 globally; CDR learns per-observation optimal τ_v adaptively. This differentiation is valid but must be made explicit. LingBot-VA should be added as a primary baseline in Phase 3.\", \"MAJOR — Fast-WAM (arXiv 2603.16666) directly undermines CDR's narrative: Fast-WAM shows that eliminating test-time video prediction entirely is competitive with imagine-then-execute WAMs (4× speedup, no performance loss on LIBERO/RoboTwin). This creates a competing solution to CDR's efficiency goal: skip video at test time entirely rather than route its depth per-observation. The paper acknowledges Fast-WAM but does not address the implication that the field is moving toward eliminating test-time video rather than optimizing how much of it to run. CDR needs an explicit argument for why adaptive routing is preferable to the skip-entirely approach — e.g., showing CDR outperforms Fast-WAM on precision tasks or 6-DoF grasp tasks where some visual grounding is needed.\", \"MAJOR — mimic-video base model is ~4-6pp below current SOTA on LIBERO: mimic-video achieves 93.9% on LIBERO (Spatial/Object/Goal average), while LingBot-VA (98.5%), DiT4DiT (98.6%), and Being-H0.7 (99.2%) are significantly higher. Even with CDR's per-observation routing, CDR's absolute LIBERO numbers will likely remain below these baselines. Reviewers will question why CDR builds on a weaker base, and will interpret CDR's improvements over τ_v=1 baseline as optimization within a sub-SOTA architecture rather than advancing the field. CDR needs to address this positioning explicitly — either by explaining why mimic-video's variable-τ_v property makes it the correct base (which is true), or by computing CDR's improvement as the Pareto gain relative to the fixed-τ_v cost-performance frontier.\", \"MODERATE — Phase 1 compute estimate (~15 H100-hours) may be optimistic: LIBERO-100 (5,000 demos × ~100 steps × 11 τ_v levels) requires ~5.5M video backbone forward passes for the action reconstruction sweep. With proper batching on Cosmos-Predict2 (2B parameter DiT), 30-60 H100-hours is a more conservative estimate. This is still within the 200-hour budget but should be revised in the resource estimate.\", \"MODERATE — If per-observation τ_v variation is small (Phase 1 outcome B), the router's Pareto gain over LingBot-VA's fixed τ_v=0.5 is unclear: LingBot-VA already shows that a fixed τ_v=0.5 universally halves steps with no loss. If CDR's Phase 1 shows that most frames benefit from τ_v ≥ 0.9 (close to τ_v=1), and only grasp phases benefit from lower τ_v, the average speedup from CDR may be modest (e.g., 10-15% above LingBot-VA's fixed halving), making the contribution marginal relative to the added router complexity.\"]\nFeedback: CDR's Round 1 revisions were excellent — distribution shift, deadline accuracy, differentiable loss, and DreamZero/mimic-video citations are all resolved. Two structural additions are needed before CoRL submission:\n\n**1. Add LingBot-VA as primary baseline and differentiate.**\nLingBot-VA (arXiv 2601.21998, accepted RSS 2026) introduces Noisy History Augmentation — training the action decoder on partially noisy video at τ_v∈[0.5,1.0] and using fixed τ_v=0.5 at inference, halving steps without performance loss (98.5% LIBERO). This is CDR's closest competitor. The differentiation is: LingBot-VA applies a universal fixed threshold τ_v=0.5; CDR routes per-observation because different manipulation phases may need different thresholds. Add LingBot-VA to Phase 3 as baseline (d) and make the adaptive-vs-fixed comparison a first-class result. The Pareto curve (task success vs. mean τ_v) directly addresses this comparison.\n\n**2. Address the Fast-WAM tension in Section 1/2.**\nFast-WAM shows that skipping test-time video entirely is competitive (4× speedup). CDR should argue that adaptive routing fills the gap between 'always use full video' and 'skip video entirely' — i.e., CDR selects per-observation whether video features help (especially for grasp phases where spatial precision matters). If Phase 1 shows commitment exists, add an explicit ablation comparing CDR vs. Fast-WAM on grasp-critical tasks.\n\n**3. Reframe the positioning: mimic-video base vs. SOTA absolute performance.**\nAcknowledge upfront that mimic-video (CDR's base) is behind LingBot-VA/DiT4DiT/Being-H0.7 on absolute LIBERO metrics. The paper's contribution is about efficiency-performance tradeoffs, not absolute task success. Lead with the Pareto curve as the primary result, not the task success number. A direct comparison CDR vs. LingBot-VA-style fixed τ_v=0.5 (same base, different routing strategy) is more informative than comparing against architectures with different training data and backbones.\n\n**4. Phase 1 compute budget should be revised to 30-60 H100-hours** for the LIBERO-100 τ_v sweep (5,000 demos × 11 noise levels). This is still within the 200-hour budget.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — τ_v=0 is the wrong Phase 1 reference: mimic-video's paper (verified by WebFetch on arXiv:2512.15692) explicitly states that τ_v=0 (fully denoised video) gives WORSE policy performance than intermediate τ_v values, and τ_v=1 (pure noise, no video denoising) is the best single global default on SIMPLER-Bridge. CDR defines τ_v* = min{τ_v : ||a_{τ_v} − a_{τ_v=0}||₂ ≤ δ}, which targets convergence with a suboptimal operating point. Routing toward τ_v=0 can actively degrade performance relative to the baseline (τ_v=1), making the router counterproductive. Fix: replace the reference with per-observation action error vs. ground truth (||a_{τ_v} − a_GT||₂ using LIBERO demo GT actions), or define τ_v* as convergence to the per-task optimal τ_v (already estimated by mimic-video's sweep), not τ_v=0.\", \"CRITICAL — The core hypothesis conflicts with mimic-video's global-optimum finding: mimic-video reports τ_v=1.0 (single forward pass, no video generation) as the best global default for autonomous policy performance on SIMPLER-Bridge — the same benchmark CDR foregrounds as its primary showcase. If τ_v=1.0 is already globally optimal, then CDR's hypothesis that 'grasp/insert phases need τ_v≈0.3' means the router would systematically push those frames toward a worse operating point. CDR must explain and address this contradiction before submitting; the paper currently cites the +9.4pp per-task gain as motivation but does not engage with mimic-video's per-task sweep showing that the global optimal is at the highest-noise end.\", \"MAJOR — Demo-vs-rollout distribution shift in Phase 1: Phase 1 labels τ_v* on human demonstration states from LIBERO-100 (expert teleop). During closed-loop evaluation the robot visits recovery states, partial-success configurations, and states outside the demonstration support. A router trained on demo-state labels has no guarantee of correct τ_v routing on the novel states seen during closed-loop rollouts — exactly the states where wrong τ_v routing would harm performance most. The paper does not address this distribution gap.\", \"MAJOR — Deadline pressure makes pre-validation essential but is not acknowledged: CDR explicitly frames Phase 1 as an empirical question with uncertain outcome ('both outcomes publishable'). With 19 days to the full-paper deadline (May 29), there is no time to run Phase 1 (30–60 H100-hours), discover the wrong reference, fix it, re-run Phase 1, train the router, and evaluate on LIBERO+SIMPLER-Bridge. The paper should be pre-validated — run Phase 1 immediately and inspect the τ_v* distribution before committing. If τ_v* clusters above 0.8 for all frames (consistent with the global τ_v=1 finding), the paper's story collapses.\", \"MODERATE — Fallback framing ('validation study + per-task routing') is below CoRL bar: CoRL accepts ~22% of submissions in a highly competitive WAM-dense cycle. A paper whose main contribution degrades to '3D commitment validation + automated zero-shot per-task routing' (when per-observation variation < 1pp) is unlikely to cross the acceptance threshold, because zero-shot per-task routing via a frozen 512-dim MLP is architecturally trivial and the validation study alone is more suited to a workshop. Both outcomes must be made independently compelling, or the paper should be conditioned on a positive Phase 1 result.\", \"MODERATE — Absolute LIBERO numbers below SOTA undermines reviewer confidence: CDR built on mimic-video (93.9% LIBERO) versus LingBot-VA (98.5%) and DiT4DiT (98.6%) creates a 4.7pp gap that no router can close without base-model improvement. Reviewers at CoRL, seeing absolute numbers rather than Pareto curves in the abstract, will downweight CDR vs. papers that achieve both efficiency and SOTA accuracy. The paper must lead with SIMPLER-Bridge (where the mimic-video base is competitive and the per-task gain is large) rather than LIBERO in the abstract and intro.\"]\nFeedback: CDR enters Round 3 with its prior critical issues genuinely resolved — LingBot-VA added as primary baseline, mimic-video distribution shift fixed by reframing to use its variable-τ_v decoder, Pareto framing cleanly differentiated from Fast-WAM, compute revised to 30–60 H100-hours for Phase 1. But two previously unknown issues now emerge from independent verification of mimic-video's actual findings:\n\n**Top priority fix (do before anything else):** The Phase 1 reference τ_v=0 is empirically wrong. mimic-video's paper (arXiv:2512.15692, verified) states that τ_v=0 (fully denoised video) gives worse policy performance than intermediate τ_v, and the best single global default on SIMPLER-Bridge is τ_v=1.0 (no video denoising). CDR's proxy ε_τ = ||a_{τ_v} − a_{τ_v=0}||₂ therefore measures 'convergence to a suboptimal point.' Fix Phase 1 to use per-observation action error vs. ground truth (||a_{τ_v} − a_GT||₂, available from LIBERO demos), or define τ_v* as the minimum τ_v that converges to within δ of the per-task optimal τ_v (which mimic-video already sweeps). This is the most important technical correction and must be done before any other Phase 1 computation.\n\n**Second priority (validates the entire premise):** Run a quick Phase 0 sanity check (1–2 H100-hours): take 5 LIBERO tasks and 2–3 demo trajectories, sweep τ_v={1.0, 0.9, ..., 0.3} using the corrected GT reference, and inspect whether per-phase τ_v* shows >2pp within-episode variation. If grasp frames and approach frames cluster at the same τ_v*, the CDR adaptive story does not materialize and the paper should be reframed before committing to the CoRL deadline.\n\n**Third priority (narrative):** Move SIMPLER-Bridge to the primary benchmark in the abstract and intro. LIBERO absolute numbers (94–96% vs. SOTA 98.5%) will hurt reviews; SIMPLER-Bridge is where mimic-video's per-task variation is pronounced (+9.4pp) and where CDR's per-observation extension is most defensible. Explicitly note in the intro that LIBERO results are presented for comparability but the core efficiency-performance trade-off is shown on SIMPLER-Bridge.\n\n**Fallback strengthening:** If per-observation variation is small, the fallback 'automated zero-shot per-task routing' needs a real numerical result to be CoRL-ready: show the MLP router (trained on LIBERO) correctly predicts per-task optimal τ_v on held-out tasks from SIMPLER-Bridge (zero-shot) and recovers ≥80% of the per-task sweep gain (+9.4pp) without offline rollouts. That specific claim is publishable at CoRL as an efficiency-of-deployment contribution.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE — Fast-WAM SIMPLER-Bridge gap: Fast-WAM (arXiv:2603.16666) reports results only on LIBERO and RoboTwin in the abstract and appears not to evaluate on SIMPLER-Bridge. The proposal's Phase 3 plans to compare CDR against a 'Fast-WAM-style' baseline on SIMPLER-Bridge but this requires either (a) running Fast-WAM's architecture on mimic-video's SIMPLER-Bridge setup or (b) using τ_v=1 as a proxy for Fast-WAM's behavior — the proposal conflates these. τ_v=1 in mimic-video is NOT architecturally equivalent to Fast-WAM: τ_v=1 still processes noisy future frames through the full backbone, while Fast-WAM modifies architecture to not generate future frames. The paper must clearly state which 'Fast-WAM-style' baseline is being run and how it is implemented on the mimic-video backbone.\", \"MODERATE — 'Denoising, Fast and Slow' mischaracterized as 'per-sample difficulty routing': WebFetch of arXiv:2604.19141 confirms this CVPR 2026 paper does PATCH-LEVEL spatial routing within images (varying timesteps across image regions), NOT per-sample routing across observations in a trajectory. The proposal describes it as 'per-sample difficulty routing in image diffusion — supports CDR's feasibility argument.' This mischaracterization is relatively minor but CoRL reviewers familiar with the paper will catch it. More importantly, the differentiation from CDR is actually cleaner than the proposal implies: CDR is temporal routing across trajectory timesteps; 'Denoising Fast and Slow' is spatial routing across image patches. The proposal should make this distinction explicit.\", \"MODERATE — τ_v=1 global optimality claim is stated as 'foundational verified' but the WebFetch of the mimic-video HTML only confirmed that the scratch (no per-task tuning) result is 46.9%, not that τ_v=1 specifically is the best single fixed τ_v among all possible fixed values. The paper states 'performance peaks at an INTERMEDIATE noise level' per-task; if a fixed global τ_v=0.8 outperforms τ_v=1 on SIMPLER-Bridge aggregate, CDR's 'τ_v=1 as globally optimal default' framing collapses. This must be verified from Table I or Figure 5 of mimic-video before committing to this framing.\", \"MODERATE — 20-day critical path has zero slack for Phase 1 overruns: Phase 0 decision on May 12 + Phase 1 (5–8 days on 8 H100s) + Phase 2 (1 day) + Phase 3 (6 days) + Writing (4 days) = 16–19 days to May 28-29 submission. If Phase 1 takes 8 days (upper bound of 60h / 8 GPUs), writing is compressed to 2 days or Phase 3 is cut. The proposal should explicitly acknowledge that Phase 3 ablations (RoboCasa, per-phase heatmaps) are drop-able if Phase 1 runs long, and that the minimum viable submission needs only SIMPLER-Bridge primary results.\", \"MINOR — MotuBrain (arXiv:2604.27792) is unaddressed: MotuBrain biases video timestep sampling toward noisier regions during training to improve robustness under noisy visual conditions — this is related to CDR's study of τ_v sensitivity. While MotuBrain is a training-time technique and CDR is a test-time router, reviewers may conflate them. CDR's landscape should acknowledge MotuBrain briefly as a training-time complementary approach vs. CDR's test-time routing.\", \"MINOR — SIMPLER-Bridge is mimic-video's primary benchmark but is not universally known in the CoRL community: if the majority of reviewers are primarily familiar with LIBERO (the most common WAM benchmark), leading with SIMPLER-Bridge scores (where CDR's base 46.9% looks weak in absolute terms) may create a poor first impression. The abstract should explicitly state '46.9% is the state-of-the-art on this task for models of this size' or note that SIMPLER-Bridge is evaluation on real-to-sim transfer tasks where most methods score <55%.\"]\nFeedback: Round 4 correctly resolves all Round 3 critical issues: the τ_v=0 reference has been replaced with GT actions (||a_{τ_v} − a_GT||₂), τ_v=1 is reframed as globally optimal default, distribution shift is mitigated via 50% non-expert rollout states, Phase 0 is a proper gate, and the fallback has concrete numerical targets (≥80% sweep gain recovery). The proposal is now scientifically sound and structurally well-organized. Three focused fixes are needed for Round 5:\n\n**Fix 1 (highest priority — 30 min)**: Verify from mimic-video Table I / Figure 5 that τ_v=1.0 specifically is the best among ALL fixed τ_v values globally (not just 'no per-task tuning'). If the global best is τ_v=0.8 or 0.9, revise the framing to 'near-τ_v=1 region is globally optimal' and adjust CDR's conservative-routing fallback accordingly. This is the entire premise — it must be confirmed with the exact quote and figure number from the paper.\n\n**Fix 2 (clarity — 20 min)**: Correct the 'Denoising, Fast and Slow' characterization from 'per-sample difficulty routing' to 'per-PATCH spatial difficulty routing' and rewrite the differentiation: 'CDR operates in the temporal domain (which trajectory frames need video denoising), while Denoising Fast and Slow operates in the spatial domain (which image patches need more denoising steps). These are orthogonal axes and could in principle be combined.' This turns a potential reviewer objection into a positive contribution statement.\n\n**Fix 3 (baseline specification — 1 day)**: In Phase 3 baseline (e), specify exactly what 'Fast-WAM-style' means on mimic-video backbone: is it (i) running mimic-video with only the first observation frame as video input and zeros for future frames, or (ii) using τ_v=1 as a proxy? Clarify this is NOT the published Fast-WAM model (different architecture), but rather a mimic-video ablation that disables future video usage, implementing the spirit of Fast-WAM post-hoc. This prevents reviewers from thinking CDR is being unfairly compared against a strawman.\n\n**Opportunistic improvement**: If Phase 0 runs TODAY (May 10) and shows ≥20% activation frames clustered in grasp phases, add a 1-paragraph 'Phase 0 Sanity Check Result' section to the paper with the preliminary histogram. This is publishable supporting evidence that CDR's empirical premise is confirmed, and it addresses the biggest risk reviewers will identify when reading the proposal.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — OA-WAM (arXiv:2605.06481, May 7 2026) is uncited but evaluates on both LIBERO (97.8%) and SimplerEnv (79.3%). CDR must cite OA-WAM in related work. More importantly: OA-WAM's 79.3% SimplerEnv vs. CDR's base 46.9% SIMPLER-Bridge will prompt reviewers to ask why CDR doesn't use a stronger base. CDR must explicitly note whether 'SimplerEnv 79.3%' and 'SIMPLER-Bridge 46.9%' are the same evaluation split — if OA-WAM evaluates on all SimplerEnv tasks (not just Bridge), the numbers are not directly comparable and CDR needs to state this clearly in the paper.\", \"MODERATE — Zero-shot LIBERO→SIMPLER-Bridge generalization claim (≥80% of +9.4pp recovery) is still unvalidated and carries high empirical risk. LIBERO tasks (simulated tabletop with 3D rendered objects) and SIMPLER-Bridge (real-to-sim BridgeData transfer with different visual domain) have substantially different task distributions. A router MLP trained on CLIP+language embeddings from LIBERO may not generalize to BridgeData task embeddings zero-shot. CDR should pre-validate this claim in Phase 0 by running the task-level τ_v MLP on a held-out LIBERO task set and verifying ≥80% recovery before committing it as a primary CoRL claim.\", \"MODERATE — Implicit assumption that fixed τ_v < 1 baselines (Phase 3 baselines b,c) will underperform τ_v=1 on SIMPLER-Bridge is not acknowledged as a testable prediction. Mimic-video states τ_v=1 is the best global autonomous default on SIMPLER-Bridge (noise-as-augmentation effect), implying LingBot-VA-style fixed τ_v=0.5/0.7/0.9 may underperform the 46.9% baseline on SIMPLER. CDR should make this a formal pre-registered prediction in Phase 3 and explicitly note: if fixed intermediate τ_v baselines (b,c) all underperform τ_v=1, CDR's Pareto comparison is primarily against (a) τ_v=1 and the per-task sweep oracle — LingBot-VA's approach is not a Pareto competitor on this benchmark.\", \"MINOR — A₁ (arXiv:2604.05672, April 2026) proposes adaptive per-observation early-exit truncated flow matching for VLAs with dynamic denoising depth per observation — similar spirit to CDR's per-observation routing but targeting VLAs via layer-truncation rather than video τ_v routing. CDR should add one sentence noting A₁ as an orthogonal approach: 'Concurrent work (A₁, arXiv:2604.05672) applies per-observation adaptive truncation to VLA action generation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes.'\", \"MINOR — The timeline risk from Phase 1 upper bound (8 days on 8 H100s) compressing writing to 2 days is acknowledged but not adequately mitigated. If Phase 1 takes 8 days (May 12-20), Phase 3 cannot complete before May 26. CDR should explicitly define a 'minimum viable submission' (MVS) track: Phase 0 positive result + Phase 1 τ_v* distribution histograms + per-task CDR router on SIMPLER-Bridge (Phase 2+3 partial) constitutes a submittable paper even without full Phase 3 ablations, as long as the Pareto curve includes at least τ_v=1 baseline, fixed τ_v=0.7, and per-task CDR.\"]\nFeedback: CDR has resolved all critical issues from Rounds 1-4: τ_v=0 reference replaced with GT actions, Denoising Fast and Slow correctly characterized as spatial/patch-level routing, Fast-WAM baseline correctly specified as τ_v=1 proxy (not the published model), MotuBrain acknowledged as orthogonal, and timeline drop-able ablations flagged. The scientific framing is now verified against mimic-video: Figure 5 does show performance peaks at intermediate τ_v, and τ_v=1 is confirmed as the best global autonomous default (noise-as-augmentation effect). CDR's Pareto story is internally consistent and scientifically sound.\n\nThree focused fixes for Round 6:\n\n**Fix 1 (1 hour): Cite OA-WAM and clarify SimplerEnv vs SIMPLER-Bridge.** OA-WAM (arXiv:2605.06481) evaluates on SimplerEnv (79.3%) and LIBERO (97.8%) — reviewers will notice the gap with CDR's 46.9% SIMPLER-Bridge base. Add one sentence: 'OA-WAM (2605.06481) addresses object identity robustness in WAMs; CDR addresses adaptive video denoising depth — orthogonal.' Then explicitly note in the experimental section whether SimplerEnv and SIMPLER-Bridge are the same split; if not, state that direct comparison against OA-WAM is not applicable.\n\n**Fix 2 (Phase 0 addition, run ASAP): Pre-validate zero-shot LIBERO→SIMPLER-Bridge router.** Before finalizing the ≥80% recovery claim as a primary CoRL contribution, validate it in Phase 0 or Phase 1: take a frozen MLP trained on task embeddings from 80 LIBERO-100 tasks, test zero-shot on 20 held-out LIBERO tasks, verify ≥80% τ_v* recovery. If this holds on held-out LIBERO tasks, the SIMPLER-Bridge zero-shot claim is credible. If not, reframe to 'per-task routing with fine-tuning on 3 SIMPLER tasks' rather than zero-shot.\n\n**Fix 3 (framing, 30 min): Pre-register the fixed τ_v < 1 underperformance prediction.** In Phase 3, explicitly state: 'We predict baselines (b,c) — LingBot-VA-style fixed τ_v=0.5/0.7/0.9 — will underperform baseline (a) τ_v=1 on SIMPLER-Bridge due to the noise-as-augmentation regularization effect documented in mimic-video. If this prediction is confirmed, CDR's Pareto comparison is against (a) and the per-task sweep oracle, not against uniform partial denoising approaches.' This pre-registration turns a potential negative result (baseline (b,c) worse than τ_v=1) into a publishable confirmation of CDR's theoretical premise.\n\n**Optional (1 hour): Add A₁ one-sentence cite.** 'Concurrent work (arXiv:2604.05672) applies per-observation adaptive truncation to VLA action generation via inter-layer early exit; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal.'\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MODERATE — mimic-video Figure 5 is cited misleadingly: CDR claims 'Figure 5 shows aggregate performance peaks at an intermediate noise level (not at τ_v=1)' — this reflects the figure *caption* only. The mimic-video main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest flow time τ_v=1.' These are internally contradictory in the source paper, and reviewers reading the main text will perceive CDR as misrepresenting mimic-video. CDR must cite the figure caption specifically ('mimic-video Figure 5 caption states: performance peaks at an intermediate noise level') AND acknowledge that the main text separately concludes τ_v=1 is the best fixed global choice. The reconciliation is straightforward — Figure 5 shows oracle per-task optimal τ_v is at intermediate levels, while τ_v=1 is the best fixed-global-τ_v — but CDR must make this explicit or reviewers will flag it in every review.\", \"MODERATE — The pre-registered prediction that 'fixed τ_v < 1 baselines will underperform τ_v=1' is now strongly supported by mimic-video's *main text* conclusion (τ_v=1 is best autonomous performance). If this prediction is confirmed in Phase 3, CDR's Pareto comparison becomes primarily CDR vs. τ_v=1 baseline — LingBot-VA-style uniform partial denoising is not a Pareto competitor on SIMPLER-Bridge. CDR should elevate this framing: 'Our pre-registered prediction is that LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge; CDR's contribution is Pareto dominance over the τ_v=1 default via selective routing.' If confirmed, the paper becomes a cleaner story but with a narrower competitive comparison than currently implied.\", \"MINOR — The core novelty claim ('no existing VAM paper has empirically studied which manipulation phases benefit from τ_v < 1') is valid but the architectural contribution (2-layer MLP router) is thin for CoRL 2026's competitive WAM track. The Phase 1 empirical study is the genuine contribution; CDR should foreground it as 'the first empirical characterization of video necessity by manipulation phase in 3D WAMs' rather than leading with the routing mechanism.\"]\nFeedback: CDR has resolved all Round 5 issues and is scientifically well-structured. One focused fix is needed before submission:\n\n**Fix 1 (required, 30 minutes): Correct the mimic-video Figure 5 citation.** Replace 'Figure 5 shows aggregate performance peaks at an intermediate noise level (not at τ_v=1)' with 'mimic-video Figure 5 caption reports that performance peaks at an intermediate noise level; the paper's main text separately concludes that τ_v=1 achieves the best fixed-global autonomous policy performance on SIMPLER-Bridge. These findings are reconcilable: the oracle per-task optimal τ_v is intermediate (Figure 5 caption), while the best fixed-global τ_v is τ_v=1 (main text). CDR exploits this gap: a lightweight router approximates the per-observation oracle, recovering gains that a fixed-global τ_v=1 leaves on the table.' This specific reconciliation should appear verbatim in the intro, and the phrase 'aggregate performance peaks at an intermediate noise level' must be removed from all sections where it appears without the Figure 5 caption attribution. Reviewers who have read mimic-video carefully will catch this without the fix.\n\n**Fix 2 (framing, 20 minutes): Elevate the pre-registered prediction as the paper's anchor claim.** Since mimic-video's main text already supports the prediction that uniform τ_v<1 underperforms τ_v=1, CDR's Pareto claim is effectively: CDR vs. τ_v=1 baseline (not CDR vs. LingBot-VA). Make this the headline: 'We show that LingBot-VA-style uniform partial denoising is not a valid Pareto competitor on SIMPLER-Bridge (pre-registered and confirmed), and CDR Pareto-dominates the τ_v=1 fixed-global default by selectively routing only frames that require lower τ_v.' This is a cleaner and more defensible Pareto claim than the current framing.\n\nWith these two changes, CDR is ready for CoRL submission. The MVS track is well-defined, the zero-shot validation gates are appropriately scoped, and the related-work section is comprehensive. The paper's contribution — the first empirical study of manipulation-phase τ_v requirements plus zero-shot per-task routing — is modest but publishable at CoRL if the Phase 1 histograms show meaningful phase-specific variation.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE — DiT4DiT ablation is factually mischaracterized: Independent verification of arXiv:2603.10448 confirms that DiT4DiT's 'single-step is best' ablation (Figure 8b) concerns ACTION DENOISING STEPS (fewer action diffusion steps yield higher success), not τ_v (video noise level). CDR's landscape states: 'DiT4DiT ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding.' This conflates two different efficiency axes (action denoising steps vs. video noise level). Reviewers familiar with DiT4DiT will flag this. Fix: either remove DiT4DiT as corroborating evidence for τ_v=1 optimality, or rewrite as 'DiT4DiT finds that fewer action denoising steps improve performance — a parallel finding that the high-noise, low-denoising regime is preferable, supporting CDR's premise that less denoising is often better.' Do NOT use DiT4DiT to directly corroborate mimic-video's τ_v=1 result.\", \"MODERATE — Pareto efficiency claim is potentially misleading if P1 is confirmed: If P1 is confirmed (fixed intermediate τ_v < 1 uniformly underperforms τ_v=1 on SIMPLER-Bridge), then CDR's router will route the vast majority of frames to τ_v=1 (since τ_v=1 is the best single fixed value). The resulting 'compute savings' from CDR — measured as reduction in mean τ_v consumed below 1 — will be small (perhaps 5–10% of full video generation cost). The Pareto win is primarily in task SUCCESS (+≥7.5pp from zero-shot per-task routing), not in compute efficiency. The paper's abstract and intro must be honest about this: 'CDR's Pareto dominance is primarily measured in task success recovery, not compute savings, if the pre-registered P1 prediction is confirmed. The mean τ_v consumed by CDR remains close to 1 when P1 holds.' Misrepresenting the Pareto win as efficiency-driven when most frames route to τ_v=1 will trigger reviewer pushback.\", \"MODERATE — Auto-mode resource estimate (410 H100-hours) exceeds the ≤200 H100-hour budget constraint stated in user requirements. The manual estimate (115–135H) is within budget, but auto mode at 410H is 2-3× over the stated limit. Either: (a) cap the auto-mode scope to fit within 200H by dropping full RoboCasa, per-phase heatmap ablations, and the full λ×θ grid search; or (b) explicitly acknowledge in the proposal that auto-mode exceeds the 200H constraint and requires expanded budget authorization.\", \"MINOR — 'When to Trust Imagination' (arXiv:2605.06222) is misdescribed as 'reduces replanning frequency'; verified content shows it uses a per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution — not episode-level replanning reduction. The orthogonality claim holds, but the description should be corrected to 'per-chunk adaptive replanning trigger' to avoid misleading reviewers.\", \"MINOR — Method contribution is architecturally thin for CoRL 2026's WAM track: The 2-layer MLP router (512-dim CLIP + 512-dim language → 256-dim hidden → 4-class softmax) is not a novel architecture. CoRL 2026's WAM submissions include DiT4DiT, MotuBrain, OA-WAM with substantial architectural innovation. CDR must foreground Phase 1 (first empirical characterization of manipulation-phase τ_v requirements) as the primary scientific contribution — the router is the deployment mechanism, not the contribution. The paper title 'Commitment Depth Routing' implies a routing method is the contribution; consider retitling to reflect the empirical study: e.g., 'When Do World Action Models Need Video? A Manipulation-Phase Study with Selective Denoising Activation.'\"]\nFeedback: CDR has fixed all prior critical issues through Round 6. The Round 7 proposal is now scientifically well-structured with explicit gates, correct mimic-video Figure 5 reconciliation, pre-registered predictions, and MVS fallback. Three focused fixes are required before CoRL submission:\n\n**Fix 1 (required, 30 minutes): Correct DiT4DiT characterization.** DiT4DiT's ablation (Figure 8b in arXiv:2603.10448) is about action denoising steps — not τ_v (video noise level). CDR incorrectly uses it to corroborate 'high τ_v is best on SIMPLER-Bridge.' Rewrite as: 'DiT4DiT finds that a single action denoising step outperforms multi-step action diffusion — a parallel finding that less denoising in the action domain also improves performance; we observe the same pattern in the video domain with mimic-video's τ_v=1 result.' Remove any language claiming DiT4DiT 'independently confirms' that high video noise τ_v is optimal.\n\n**Fix 2 (required, 20 minutes): Honestly bound the Pareto efficiency claim.** If P1 is confirmed (the expected outcome based on mimic-video main text), CDR routes most frames to τ_v=1, making compute savings modest. Add explicit language in the abstract and intro: 'CDR's primary Pareto benefit is task success recovery (≥7.5pp zero-shot on SIMPLER-Bridge), not compute efficiency — most frames continue to use τ_v=1, with video activation selectively applied only to frames where the Phase 1 study identifies τ_v* < 1.' This prevents reviewers from expecting large speedups and finding only 5-10% compute savings.\n\n**Fix 3 (budget reconciliation, 10 minutes): Cap auto-mode estimate.** The auto mode at 410 H100-hours violates the ≤200H project constraint. Either (a) reduce auto-mode scope to 150-180H (drop RoboCasa, full hyperparameter grid) while keeping the key SIMPLER-Bridge experiments, or (b) add a note that auto-mode exceeds the budget constraint and requires pre-authorization. The manual mode (115-135H) is within budget and should be the reference for the 200H limit.\n\n**Optional (strengthens paper): Retitle to foreground empirical contribution.** 'Commitment Depth Routing' implies a novel routing mechanism as the primary contribution. The actual primary contribution is Phase 1 — the first empirical study of which manipulation phases need τ_v < 1 in 3D WAMs. A title like 'When Does Robot Policy Need Video? Manipulation-Phase Analysis and Selective Activation for World Action Models' better positions the paper as an empirical methods contribution and reduces reviewer expectations of architectural novelty.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"MODERATE — OA-WAM per-task numbers (Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%) could not be independently located in accessible arXiv:2605.06481 text. The aggregate 79.3% and Visual Matching protocol on the same 4 WidowX Bridge tasks were confirmed, but the per-task breakdown is unverified. If these numbers cannot be located in the paper's experimental tables, the proposal should either cite the specific table/figure or replace them with '79.3% aggregate (per-task breakdown not reported in OA-WAM).' Fabricated per-task numbers would be a citation integrity issue reviewers could flag.\", \"MODERATE — The primary reframed benefit ('10 rollouts → 0 per new task calibration') needs quantitative deployment-cost framing to carry CoRL weight. As written, the savings are: 4 SIMPLER-Bridge tasks × 10 rollouts = 40 rollouts eliminated. Without a scaling argument (N new tasks over a deployment lifetime, rollout wall-clock cost), this is not compelling to reviewers. A one-paragraph deployment cost analysis ('a robot deployed for 6 months accumulates ~50 new tasks; CDR eliminates ~500 calibration rollouts at $Y/hour wall-clock cost') is needed to frame this as a practically significant contribution rather than a marginal convenience.\", \"MODERATE — Statistical robustness of the 4-task SIMPLER-Bridge primary evaluation is not specified. The +≥7.5pp Pareto claim is over 4 tasks — a very small evaluation set for a CoRL 2026 WAM paper. The proposal does not state: (a) how many rollout seeds per task-baseline combination will be reported, (b) whether the improvement target (≥7.5pp) is a raw mean or statistically tested, (c) what confidence intervals or standard deviations will be reported. CoRL reviewers will ask for these in every review of a paper with 4-task primary results.\", \"MINOR — The 'first empirical characterization' claim is scoped to the mimic-video variable-τ_v architecture but is not stated as such in the framing. Adding one explicit sentence — 'This characterization applies to WAM architectures trained with logit-normal variable-τ_v augmentation; architectures that do not expose τ_v as a continuous test-time parameter (Fast-WAM) are architecturally incompatible with CDR's approach' — prevents reviewers from questioning why CDR's study doesn't generalize to all WAMs.\", \"MINOR — The paper now foregrounds the empirical study (Phase 1) as the primary contribution per the title, but the abstract structure still leads with the routing mechanism before the empirical finding. CoRL reviewers scan abstracts quickly; if the abstract's first contribution claim is 'zero-shot router,' they will assess it as a method paper and apply architectural novelty standards. The abstract should lead with: 'We present the first empirical study of which 3D manipulation phases require video denoising below τ_v=1 in WAMs, finding [key result from Phase 1]. Building on this, we introduce a zero-shot per-task router that recovers [X]pp of the per-task oracle gain without offline calibration rollouts.'\"]\nFeedback: CDR has resolved all critical issues from Rounds 1-7 and is now scientifically sound with honest Pareto framing, correct DiT4DiT characterization, auto-mode budget within ≤200H, and comprehensive related-work coverage. Three targeted fixes are needed before submission:\n\n**Fix 1 (verify, 30 min): Confirm or remove OA-WAM per-task numbers.** Fetch arXiv:2605.06481's experimental tables and locate the per-task numbers (83%, 71.1%, 65%, 98.2%) in a specific table or figure. If locatable, cite the exact table number. If not found, remove per-task numbers and replace with 'OA-WAM 79.3% aggregate on the same four WidowX Bridge tasks (per-task breakdown not reported in OA-WAM).' Unverified specific numbers in related-work comparison tables are a red flag for reviewers.\n\n**Fix 2 (framing, 30 min): Quantify the deployment calibration savings argument.** The paper's primary reframed benefit is '10 rollouts → 0 per new task.' This needs a scaling argument to be compelling at CoRL: 'A robot system deployed in a warehouse or lab environment encounters N_new new manipulation tasks monthly. At 10 rollouts per task to calibrate the fixed τ_v, calibration cost grows linearly with N_new. CDR's zero-shot router eliminates this cost entirely, enabling zero-shot task extension without offline calibration. At N_new = 20 tasks/month and 30-minute rollout windows, CDR saves ~100 hours of robot time per month per system.' The exact numbers are illustrative — the key point is a concrete deployment scenario that makes the savings tangible rather than abstract.\n\n**Fix 3 (evaluation specification, 1 day): Add statistical reporting protocol to Phase 3.** In the Phase 3 section, explicitly state: 'We will run K=50 closed-loop rollouts per task per baseline, reporting mean ± standard deviation task success and Wilson confidence intervals. The +≥7.5pp target is a lower bound on the mean improvement; we will report significance at p<0.05 via a one-sided t-test.' Without this, reviewers will note that 4-task results are statistically fragile.\n\n**Fix 4 (abstract restructuring, 20 min): Lead abstract with the empirical finding, not the router.** Replace the current abstract structure with: 'We present the first empirical study of per-observation optimal video denoising depth (τ_v*) in World Action Models, finding [Phase 1 key result: e.g., grasp-phase frames require τ_v* ≈ X while approach frames cluster at τ_v*=1]. Building on this, we introduce CDR, a zero-shot per-task router that recovers ≥80% of the per-task oracle gain (+≥7.5pp on SIMPLER-Bridge) without offline calibration rollouts, eliminating 10 rollouts-per-task deployment cost.' This frames CDR as an empirical contribution (which it is) rather than an architecture paper.\n\nWith these four fixes, CDR is at its maximum achievable quality within the 20-day constraint. The paper's ultimate CoRL fate will depend on whether Phase 1 reveals genuinely surprising per-phase variation — if the τ_v* histograms show clear grasp-vs-approach clustering, the paper strengthens significantly; if variation is weak, the MVS track (per-task CDR zero-shot + pre-registered P1 confirmation) is the submission path.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:47:31.326Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:47:31.326Z",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-10T09:47:31.350Z_

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

## Idea under review (round 9/10)
{
  "title": "When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation",
  "core_problem": "Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. This paper exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\n\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. The per-task breakdown (Table I, arXiv:2512.15692) reveals strong task heterogeneity: Stack Blocks 12.5%→29.2% (+16.7pp), Carrot on Plate 37.5%→54.2% (+16.7pp), Spoon on Towel 37.5%→41.7% (+4.2pp), Eggplant in Basket 100%→100% (+0pp — already saturated at τ_v=1). This heterogeneity is the core motivation for CDR: Eggplant in Basket requires no video denoising below τ_v=1 (already at ceiling), while Stack Blocks and Carrot on Plate strongly benefit from lower τ_v. A per-task router that correctly identifies these task types recovers most of the +9.4pp oracle gain without the 10-rollout-per-task calibration cost. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\n\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical (analogous to CDR routing Eggplant to τ_v=1 while Stack Blocks to τ_v<1); (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. This paper addresses the third cost: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task oracle justifies it, and eliminate the 10-rollout-per-task deployment calibration cost via a zero-shot router trained on LIBERO-100.\n\nCRITICAL PARETO FRAMING CLARIFICATION (required for reviewer accuracy): If the pre-registered prediction P1 is confirmed (fixed intermediate τ_v < 1 underperforms τ_v=1 on SIMPLER-Bridge — the expected outcome per mimic-video main text), then the zero-shot router routes the MAJORITY of frames to τ_v=1. This means: (a) mean τ_v consumed by CDR stays CLOSE TO 1.0; (b) per-inference GPU compute savings are SMALL (5–10% at most); (c) the primary benefit is TASK SUCCESS RECOVERY (+≥7.5pp zero-shot on SIMPLER-Bridge) and DEPLOYMENT CALIBRATION SAVINGS (10 offline rollouts per new task → 0). The abstract and introduction MUST state this explicitly. CDR's Pareto dominance vs. τ_v=1 is: same or slightly lower mean τ_v consumed, significantly higher task success — not a large speedup per inference call.\n\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Table 1 of arXiv:2605.06481: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.",
  "opportunity": "The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. This paper exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\n\nThe per-task mimic-video breakdown (Table I, arXiv:2512.15692) provides direct motivation for the selective routing thesis: Eggplant in Basket reaches 100% at τ_v=1 and gains nothing from per-task tuning (+0pp); Stack Blocks and Carrot on Plate each gain +16.7pp; Spoon on Towel gains only +4.2pp. This pattern shows that some tasks have saturated performance at τ_v=1 (Eggplant), some are precision-critical and need lower τ_v (Stack Blocks, Carrot), and some fall between (Spoon). A per-task router that correctly identifies task difficulty profile recovers most of the +9.4pp oracle aggregate gain by routing precision-critical tasks to lower τ_v while leaving non-critical tasks at τ_v=1.\n\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. The primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost.\n\nCRITICAL: THE DEPLOYMENT EFFICIENCY GAIN IS CALIBRATION COST, NOT PER-INFERENCE COMPUTE. When P1 is confirmed (the expected outcome), CDR routes most frames to τ_v=1, keeping mean τ_v close to 1.0. The efficiency improvement CDR delivers is: eliminating the 10-offline-rollout per-task sweep required to find the optimal fixed τ_v for a new task. A new task can be deployed with ZERO rollouts using the zero-shot router, rather than requiring 10 rollouts to calibrate the best fixed τ_v. This is a real and practically important contribution — robotics deployments accumulate many new tasks, and even at 10 rollouts each, calibration cost is significant — but it is DIFFERENT from 'faster inference per call.' The paper's framing must be explicit: 'CDR saves deployment calibration cost (10 rollouts → 0 per new task) and recovers task success (+≥7.5pp zero-shot), not primarily per-inference GPU compute.'\n\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, this paper also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies the competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. The Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the tasks/frames that need it, without any offline rollout cost.'\n\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. deployment-calibration-rollouts Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\n\nThe primary scientific contribution is Phase 1: the FIRST empirical characterization of which 3D manipulation phases require video denoising below the τ_v=1 fixed-global default, using GT-action-referenced τ_v labeling across LIBERO-100. This characterization applies specifically to WAM architectures trained with logit-normal variable-τ_v augmentation (such as mimic-video); architectures that do not expose τ_v as a continuous test-time parameter (e.g., Fast-WAM, which removes the video backbone at test time via architectural retraining) are not architecturally compatible with CDR's per-observation routing and are excluded from this characterization by design. The zero-shot router is the deployment mechanism enabling practical use of Phase 1's findings without offline sweeps — not the architectural novelty. The paper should be read as an empirical methods contribution, not an architectural one.",
  "landscape": "LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is the primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\n\nmimic-video (arXiv:2512.15692, Dec 2025) is the base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — this paper's contribution is approximating the per-task oracle via zero-shot routing; (d) Table I (mimic-video) provides per-task breakdown for the τ_v=1 baseline and per-task oracle: Stack Blocks 12.5%→29.2% (+16.7pp), Carrot on Plate 37.5%→54.2% (+16.7pp), Spoon on Towel 37.5%→41.7% (+4.2pp), Eggplant in Basket 100%→100% (+0pp) — this per-task heterogeneity directly validates CDR's selective routing thesis; (e) per-task sweep yields +9.4pp aggregate (46.9%→56.3%); (f) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\n\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\n\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%: Spatial 98.9%, Object 99.0%, Goal 97.4%, Long 95.9%) and SimplerEnv WidowX Bridge Visual Matching (Table 1 of arXiv:2605.06481: 79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching, Table 1 of arXiv:2605.06481); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\n\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\n\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\n\nDiT4DiT (arXiv:2603.10448) ablation (Figure 8b): fewer ACTION denoising steps yield higher task success — this finding concerns the action diffusion process, NOT τ_v (video noise level). These are orthogonal efficiency axes. CDR cites DiT4DiT only as a structural analogy: in both the action domain (DiT4DiT) and the video domain (mimic-video τ_v=1 main-text finding), less denoising tends to be preferable as a global default. CDR does NOT use DiT4DiT to corroborate τ_v=1 video noise optimality; these are different axes and conflating them would be factually incorrect. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\n\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\n\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\n\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) introduces a per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing.\n\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1 in WAMs trained with logit-normal variable-τ_v augmentation; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.",
  "approach": "CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\n\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\n\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\n\nDecision gate (by May 12):\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full selective activation story is empirically supported. Proceed to Phase 1.\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\n\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\n\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\n\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases. The mimic-video per-task breakdown (Table I: Stack Blocks +16.7pp, Carrot on Plate +16.7pp, Spoon on Towel +4.2pp, Eggplant +0pp from per-task tuning) provides task-level priors: precision manipulation tasks (Stack Blocks, Carrot on Plate) are expected to show stronger clustering of τ_v*(f) < 0.9 than already-saturated tasks (Eggplant in Basket). Phase 1 confirms whether this task-level heterogeneity extends to within-task phase-level variation.\n\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\n\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\n\n[SCOPE NOTE]: This characterization applies to WAM architectures trained with logit-normal variable-τ_v augmentation; architectures that do not expose τ_v as a continuous test-time parameter (e.g., Fast-WAM, which removes the video backbone at test time entirely) are architecturally incompatible with CDR's per-observation routing. The paper explicitly states this scope in the introduction: 'CDR's empirical findings characterize WAMs under logit-normal variable-τ_v training; this scope does not extend to architectures that eliminate τ_v as a test-time degree of freedom via retraining.'\n\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\n\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\n\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\n\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1} and θ ∈ {0.5, 0.7} to trace the accuracy-efficiency frontier (reduced from full grid to fit within compute budget).\n\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\n\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\n\nZero-shot claim gate:\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\n\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\n\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: The primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1'). The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding. NOTE: DiT4DiT's ablation (Figure 8b, about action denoising steps — not τ_v) is NOT cited as corroborating evidence for P1; mimic-video's main text alone anchors this prediction.\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\n\n[CRITICAL PARETO HONESTY REQUIREMENT] If P1 is confirmed (the expected outcome): CDR routes the majority of frames to τ_v=1. Mean τ_v consumed by CDR stays close to 1.0. Per-inference GPU compute savings are SMALL (approximately 5–10%). The primary benefit CDR provides is: (1) TASK SUCCESS RECOVERY: +≥7.5pp zero-shot on SIMPLER-Bridge vs. τ_v=1; (2) DEPLOYMENT CALIBRATION SAVINGS: eliminates 10 offline rollouts per new task required to identify optimal fixed τ_v. The abstract, introduction, and Phase 3 results section MUST state this explicitly. The Pareto curve axis framing should reflect this: if P1 confirmed, the x-axis showing 'mean τ_v consumed' will show CDR close to τ_v=1 with small compute savings; the y-axis showing task success will show the +≥7.5pp gain. This is still a Pareto win (same compute, better performance) but is NOT primarily an efficiency contribution — it is a zero-shot deployment automation contribution that recovers task success without offline rollout cost.\n\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR recovers per-task oracle gains zero-shot — same inference compute, +≥7.5pp task success, zero offline calibration rollouts.'\n\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim — if confirmed, CDR also delivers genuine per-inference compute savings. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\n\nBaselines:\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\n(e) Per-observation CDR (full system)\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\n\n[STATISTICAL REPORTING PROTOCOL — REQUIRED]: We will run K=50 closed-loop rollouts per task per baseline (4 tasks × 6 baselines = 1,200 total rollouts in SIMPLER-Bridge). Per-task success rate treated as Bernoulli variable; report mean ± standard deviation per task and aggregate mean ± standard error. Confidence intervals: Wilson CI at 95% for per-task binary success rates (preferred over normal approximation for small K). Primary significance test: one-sided paired t-test across tasks (H₀: CDR mean success ≤ τ_v=1 mean success), threshold p<0.05. The +≥7.5pp target is stated as a lower bound on the mean improvement; statistical significance is reported separately from the threshold claim to maintain interpretability. Power analysis: K=50 provides ~80% power to detect a 7.5pp improvement over 46.9% baseline at α=0.05 (normal approximation to binomial: σ≈√(0.469×0.531/50)≈0.071 per task; standardized effect size ≈1.06). Per-task breakdown is reported alongside aggregate (as mimic-video Table I reports per-task numbers) to enable reviewers to assess whether improvement concentrates on specific tasks (e.g., Stack Blocks, Carrot on Plate — consistent with their +16.7pp per-task oracle gains in Table I of arXiv:2512.15692) or is distributed. Secondary LIBERO-100 evaluation (100 tasks, 50 demonstrations each in held-out set) provides substantially higher statistical power for the within-LIBERO 80/20 router validation and is reported with per-task-type breakdown.\n\n[DEPLOYMENT CALIBRATION COST QUANTIFICATION — REQUIRED FOR CoRL FRAMING]: CDR's primary reframed benefit is elimination of per-task τ_v calibration rollouts. This requires a concrete deployment-scale argument to carry CoRL weight. A robot system in a warehouse or lab environment accumulates new manipulation task specifications regularly as it is extended to new objects, placements, and scenarios. Under mimic-video's default workflow, each new task requires 10 closed-loop rollouts to sweep τ_v ∈ {0.5, 0.7, 0.9, 1.0} and identify the optimal fixed-global value — a protocol requiring human setup, rollout execution, and reset between attempts. In real-robot deployment contexts, each rollout consumes ~15 minutes of robot time (execution + object reset + operator oversight), yielding ~2.5 robot-hours of calibration overhead per new task. At N_new = 20 new task specifications per month per robot (a conservative estimate for a warehouse or multi-object lab system): 50 robot-hours/month devoted purely to τ_v calibration, not productive manipulation. Across a 10-robot fleet over a 6-month deployment period: ~3,000 calibration rollouts, 3,000 robot-hours, and significant operator cost — all eliminated by CDR's zero-shot router. Even at simulation-only deployment (no real-robot cost), the 10-rollout overhead multiplied by a growing task library (50+ tasks/year per system) represents a meaningful engineering cost that CDR eliminates entirely. The savings scale linearly with fleet size and deployment lifetime: CDR enables zero-day task deployment — immediately after task specification, with no calibration period — which is qualitatively different from the 'deploy after calibration' workflow mimic-video requires. The introduction and contribution list must state this concretely: 'CDR eliminates 10 rollouts × N_new tasks of deployment overhead, enabling zero-shot task extension without calibration, at no backbone retraining cost.'\n\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. Per-task breakdown reported alongside aggregate (consistent with mimic-video Table I format). LIBERO-100 results reported secondarily for comparability. Key empirical claims:\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: same inference compute as τ_v=1, +≥7.5pp task success, zero offline calibration rollouts — when P1 confirmed, the compute savings (mean τ_v consumed below 1.0) are modest but the task success gain is the primary result\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in logit-normal variable-τ_v WAMs\n\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (Table 1 of arXiv:2605.06481, SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Table 1 of arXiv:2605.06481); the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\n\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story). [RoboCasa results and full per-phase heatmap ablations are explicitly dropped from CoRL submission to stay within compute budget — these move to ICLR 2027 extended version if applicable.]\n\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in logit-normal variable-τ_v WAMs (Phase 1 study) and the zero-shot deployment automation that eliminates offline calibration rollouts, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\n\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default, scoped to logit-normal variable-τ_v WAMs)\n- Phase 2 router training + 80/20 held-out validation result\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge, reported with K=50 rollouts per point and Wilson CIs\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time' in logit-normal variable-τ_v WAMs; (2) zero-shot per-task CDR on SIMPLER-Bridge eliminating 10 offline calibration rollouts; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\n\n**Timeline for CoRL 2026 (May 29 deadline):**\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\n- Phase 0 gate decision: May 12\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\n- Zero-shot claim gate decision: May 19\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation; K=50 rollouts per point maintained for statistical protocol)\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\n- Buffer: May 29 submission\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines with K=50 rollouts per baseline point, NO RoboCasa; ~20h buffer for reruns)",
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
      "gpu_hours": "~150–175 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 55h; Phase 2 with reduced λ×θ grid (λ∈{0.01,0.1} × θ∈{0.5,0.7}) plus 80/20 validation: 8h; Phase 3 SIMPLER-Bridge + LIBERO primary results only — NO RoboCasa, NO full per-phase heatmap ablations, K=50 rollouts per baseline point for statistical protocol compliance: 70h; buffer: 15h). SCOPE REDUCTION vs. prior 410H estimate: RoboCasa evaluation dropped, full 3×3 λ×θ hyperparameter grid dropped (reduced to 2×2), extensive per-phase heatmap ablations moved to ICLR 2027 extended version. This fits within the ≤200H project constraint.",
      "gpu_utilization": "Near-zero idle — phases pipelined",
      "timeline": "3–5 days with 8 H100s",
      "team": "0 (only initial sweep grid and eval harness setup required)",
      "claude_api_cost": "~$200–400 (~2,000–4,000 turns)",
      "estimated_gpu_cost": "~$410 (165h × $2.49/hr spot H100)",
      "risk_note": "Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections. Auto mode must NOT interpret CDR's benefit as 'inference-time compute savings' if P1 is confirmed — the honest framing is 'deployment calibration cost savings (10 rollouts → 0 per new task, eliminating ~2.5 robot-hours per new task in real-robot settings) and task success recovery (+≥7.5pp), with mean τ_v consumed remaining close to 1.0.' Auto mode must enforce K=50 rollouts per task per baseline in Phase 3 and report Wilson CIs and one-sided t-test significance alongside mean ± SD."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)",
    "ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)"
  ],
  "level": "solid",
  "key_references": [
    "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I provides per-task breakdown for both τ_v=1 baseline and per-task oracle: Stack Blocks 12.5%→29.2% (+16.7pp), Carrot on Plate 37.5%→54.2% (+16.7pp), Spoon on Towel 37.5%→41.7% (+4.2pp), Eggplant in Basket 100%→100% (+0pp) — this per-task heterogeneity directly motivates CDR's selective routing (saturated tasks stay at τ_v=1; precision tasks benefit from lower τ_v); Table I does NOT include fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp aggregate (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining",
    "LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge",
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; per-task numbers verified in Table 1 of arXiv:2605.06481: 79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2% (SimplerEnv WidowX Bridge Visual Matching). LIBERO: 97.8% (Spatial 98.9%, Object 99.0%, Goal 97.4%, Long 95.9%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup; cite Table 1 specifically when referencing these numbers. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.",
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
  "description": "We present the first empirical study of per-observation optimal video denoising depth (τ_v*) in World Action Models trained with logit-normal variable-τ_v augmentation, finding systematic manipulation-phase structure: [Phase 1 result — e.g., grasp-phase and precision-manipulation frames cluster at τ_v* ≈ 0.4–0.7 while approach/transport frames cluster at τ_v*=1.0 across LIBERO-100]. This characterization is scoped to WAMs with continuous test-time τ_v control (mimic-video family); architectures that eliminate τ_v as a test-time parameter via retraining (Fast-WAM) are outside CDR's scope by design. Building on this empirical foundation, we introduce CDR (Conditional Depth Routing), a zero-shot per-task router that recovers ≥80% of the per-task oracle gain (+≥7.5pp on SIMPLER-Bridge) without offline calibration rollouts, eliminating the 10-rollout-per-task deployment cost of mimic-video's per-task sweep.\n\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view. These are compatible: τ_v=1 wins when one fixed value is applied globally, but the per-task oracle τ_v distribution peaks at intermediate levels. The mimic-video per-task breakdown (Table I of arXiv:2512.15692) reveals strong task heterogeneity motivating CDR's selective approach: Stack Blocks 12.5%→29.2% (+16.7pp) and Carrot on Plate 37.5%→54.2% (+16.7pp) strongly benefit from per-task τ_v tuning; Eggplant in Basket 100%→100% (+0pp) is already saturated at τ_v=1; Spoon on Towel gains only +4.2pp. The +9.4pp aggregate oracle gap (46.9%→56.3% on SIMPLER-Bridge) is driven by precision-demanding tasks, not uniform improvement — exactly the selectivity CDR's router exploits.\n\nCRITICAL PARETO FRAMING (enforced throughout): When pre-registered prediction P1 is confirmed (the expected outcome per mimic-video main text), CDR routes most frames to τ_v=1, keeping mean τ_v consumed close to 1.0. Per-inference compute savings are small (5–10%). CDR's primary benefits are: (1) TASK SUCCESS RECOVERY — +≥7.5pp zero-shot on SIMPLER-Bridge; (2) DEPLOYMENT CALIBRATION SAVINGS — eliminating 10 offline rollouts per new task (~2.5 robot-hours per task in real-robot settings; ~100 robot-hours/month at N_new=20 new tasks/month per robot across a fleet). The paper DOES NOT claim large per-inference speedups when P1 is confirmed. This distinction is stated explicitly in the abstract and introduction.\n\nTwo pre-registered predictions before Phase 3: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text. If P1 confirmed, CDR's Pareto claim is: same inference compute, +≥7.5pp task success, zero offline calibration rollouts. (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\n\nStatistical protocol: K=50 rollouts per task per baseline (1,200 total), Wilson CI at 95%, one-sided paired t-test (p<0.05), per-task breakdown reported alongside aggregate. K=50 provides ~80% power to detect the 7.5pp target improvement at α=0.05.\n\nThe primary empirical contribution is Phase 1: first systematic study of τ_v* across LIBERO-100 with manipulation-phase breakdown in logit-normal variable-τ_v WAMs. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot per-task generalization, not the central architectural novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point, with per-task breakdown (consistent with mimic-video Table I format).\n\nDiT4DiT (arXiv:2603.10448) is cited as structural analogy only: its ablation (Figure 8b) shows fewer action denoising steps improve task success in the action domain — a parallel finding that less denoising can be globally preferable. DiT4DiT does NOT corroborate τ_v=1 video noise optimality directly; these are orthogonal efficiency axes and must not be conflated.\n\nOA-WAM (arXiv:2605.06481, Table 1) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing contribution. All OA-WAM per-task numbers (Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%) are verified in Table 1 of arXiv:2605.06481. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.",
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

### Round 8 review
Verdict: revise
Issues: ["MODERATE — OA-WAM per-task numbers (Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%) could not be independently located in accessible arXiv:2605.06481 text. The aggregate 79.3% and Visual Matching protocol on the same 4 WidowX Bridge tasks were confirmed, but the per-task breakdown is unverified. If these numbers cannot be located in the paper's experimental tables, the proposal should either cite the specific table/figure or replace them with '79.3% aggregate (per-task breakdown not reported in OA-WAM).' Fabricated per-task numbers would be a citation integrity issue reviewers could flag.", "MODERATE — The primary reframed benefit ('10 rollouts → 0 per new task calibration') needs quantitative deployment-cost framing to carry CoRL weight. As written, the savings are: 4 SIMPLER-Bridge tasks × 10 rollouts = 40 rollouts eliminated. Without a scaling argument (N new tasks over a deployment lifetime, rollout wall-clock cost), this is not compelling to reviewers. A one-paragraph deployment cost analysis ('a robot deployed for 6 months accumulates ~50 new tasks; CDR eliminates ~500 calibration rollouts at $Y/hour wall-clock cost') is needed to frame this as a practically significant contribution rather than a marginal convenience.", "MODERATE — Statistical robustness of the 4-task SIMPLER-Bridge primary evaluation is not specified. The +≥7.5pp Pareto claim is over 4 tasks — a very small evaluation set for a CoRL 2026 WAM paper. The proposal does not state: (a) how many rollout seeds per task-baseline combination will be reported, (b) whether the improvement target (≥7.5pp) is a raw mean or statistically tested, (c) what confidence intervals or standard deviations will be reported. CoRL reviewers will ask for these in every review of a paper with 4-task primary results.", "MINOR — The 'first empirical characterization' claim is scoped to the mimic-video variable-τ_v architecture but is not stated as such in the framing. Adding one explicit sentence — 'This characterization applies to WAM architectures trained with logit-normal variable-τ_v augmentation; architectures that do not expose τ_v as a continuous test-time parameter (Fast-WAM) are architecturally incompatible with CDR's approach' — prevents reviewers from questioning why CDR's study doesn't generalize to all WAMs.", "MINOR — The paper now foregrounds the empirical study (Phase 1) as the primary contribution per the title, but the abstract structure still leads with the routing mechanism before the empirical finding. CoRL reviewers scan abstracts quickly; if the abstract's first contribution claim is 'zero-shot router,' they will assess it as a method paper and apply architectural novelty standards. The abstract should lead with: 'We present the first empirical study of which 3D manipulation phases require video denoising below τ_v=1 in WAMs, finding [key result from Phase 1]. Building on this, we introduce a zero-shot per-task router that recovers [X]pp of the per-task oracle gain without offline calibration rollouts.'"]
Feedback: CDR has resolved all critical issues from Rounds 1-7 and is now scientifically sound with honest Pareto framing, correct DiT4DiT characterization, auto-mode budget within ≤200H, and comprehensive related-work coverage. Three targeted fixes are needed before submission:

**Fix 1 (verify, 30 min): Confirm or remove OA-WAM per-task numbers.** Fetch arXiv:2605.06481's experimental tables and locate the per-task numbers (83%, 71.1%, 65%, 98.2%) in a specific table or figure. If locatable, cite the exact table number. If not found, remove per-task numbers and replace with 'OA-WAM 79.3% aggregate on the same four WidowX Bridge tasks (per-task breakdown not reported in OA-WAM).' Unverified specific numbers in related-work comparison tables are a red flag for reviewers.

**Fix 2 (framing, 30 min): Quantify the deployment calibration savings argument.** The paper's primary reframed benefit is '10 rollouts → 0 per new task.' This needs a scaling argument to be compelling at CoRL: 'A robot system deployed in a warehouse or lab environment encounters N_new new manipulation tasks monthly. At 10 rollouts per task to calibrate the fixed τ_v, calibration cost grows linearly with N_new. CDR's zero-shot router eliminates this cost entirely, enabling zero-shot task extension without offline calibration. At N_new = 20 tasks/month and 30-minute rollout windows, CDR saves ~100 hours of robot time per month per system.' The exact numbers are illustrative — the key point is a concrete deployment scenario that makes the savings tangible rather than abstract.

**Fix 3 (evaluation specification, 1 day): Add statistical reporting protocol to Phase 3.** In the Phase 3 section, explicitly state: 'We will run K=50 closed-loop rollouts per task per baseline, reporting mean ± standard deviation task success and Wilson confidence intervals. The +≥7.5pp target is a lower bound on the mean improvement; we will report significance at p<0.05 via a one-sided t-test.' Without this, reviewers will note that 4-task results are statistically fragile.

**Fix 4 (abstract restructuring, 20 min): Lead abstract with the empirical finding, not the router.** Replace the current abstract structure with: 'We present the first empirical study of per-observation optimal video denoising depth (τ_v*) in World Action Models, finding [Phase 1 key result: e.g., grasp-phase frames require τ_v* ≈ X while approach frames cluster at τ_v*=1]. Building on this, we introduce CDR, a zero-shot per-task router that recovers ≥80% of the per-task oracle gain (+≥7.5pp on SIMPLER-Bridge) without offline calibration rollouts, eliminating 10 rollouts-per-task deployment cost.' This frames CDR as an empirical contribution (which it is) rather than an architecture paper.

With these four fixes, CDR is at its maximum achievable quality within the 20-day constraint. The paper's ultimate CoRL fate will depend on whether Phase 1 reveals genuinely surprising per-phase variation — if the τ_v* histograms show clear grasp-vs-approach clustering, the paper strengthens significantly; if variation is weak, the MVS track (per-task CDR zero-shot + pre-registered P1 confirmation) is the submission path.


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
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "2d3d2054-f31c-4340-aad5-2598e19f36ab",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:47:31.346Z_

```json
{
  "parentUuid": "2d3d2054-f31c-4340-aad5-2598e19f36ab",
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
  "uuid": "4e8c76ed-a280-4a13-b894-f37e31914ddb",
  "timestamp": "2026-05-10T09:47:31.346Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:47:31.346Z_

```json
{
  "parentUuid": "4e8c76ed-a280-4a13-b894-f37e31914ddb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "31f59460-1edd-4875-b186-76e059e6ba1f",
  "timestamp": "2026-05-10T09:47:31.346Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
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
  "leafUuid": "31f59460-1edd-4875-b186-76e059e6ba1f",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:49:11.204Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 9 of 10 for reviewing the CDR (Conditional Depth Routing) paper idea for CoRL 2026. Let me carefully analyze what has been fixed from Round 8 and what issues remain.

First, let me understand what the Round 8 review flagged:
1. OA-WAM per-task numbers unverified
2. Deployment calibration savings needs quantitative framing
3. Statistical robustness of 4-task evaluation not specified
4. 'First empirical characterization' scope not stated
5. Abstract still leads with routing mechanism


Now I'm checking what Round 9 has addressed. The proposal appears to have tackled the major issues from the previous round—it's now citing specific table references for the OA-WAM per-task numbers with actual performance breakdowns across the four tasks, and it's verifying these numbers against the source material.

For the deployment calibration piece, there's now a detailed cost breakdown showing concrete figures: roughly 15 minutes of robot time per rollout, accumulating to about 2.5 robot-hours of calibration overhead per new task, and scaling that across a fleet of 10 robots over 6 months yields around 3,000 calibration hours—giving the proposal the quantified deployment context it was missing.

The statistical rigor section specifies K=50 closed-loop rollouts per task across the same four WidowX Bridge tasks, treating success rates as Bernoulli variables with Wilson confidence intervals at 95%, and using a one-sided paired t-test (p<0.05) to compare CDR against the τ_v=1 baseline. The scope is also now explicitly bounded to WAM architectures trained with logit-normal variable-τ_v augmentation, clarifying what this characterization actually applies to.

Now I'm checking whether the OA-WAM per-task numbers are actually reported in Table 1, whether there are any concurrent works I've missed, and whether the auto-mode budget constraint has been properly corrected.

Looking at the compute budget breakdown, I see the Phase 0-3 allocation totals around 150-175 H100-hours with a 15-hour buffer, which fits well under the 200-hour constraint—a significant reduction from the previous 410-hour estimate that exceeded limits. The scope cuts include dropping RoboCasa evaluation and the full per-phase ablation heatmaps to stay within budget while maintaining the core SIMPLER-Bridge and LIBERO results with proper statistical protocol compliance.

Manual mode comes in at 115-135 H100-hours, also comfortably within the budget. Now I want to independently verify some of the key claims, particularly whether OA-WAM's per-task results are actually available in Table 1, check for any concurrent work from May 2026, and assess whether the core methodology holds up and if there are any new issues I haven't encountered yet.

Looking at what's been addressed in Round 9, the per-task numbers for OA-WAM now have specific table citations, deployment calibration savings are quantified with concrete figures, the statistical protocol is clearly defined with K=50 rollouts and Wilson confidence intervals, and the abstract now leads with the empirical finding. But I'm noticing the 4-task evaluation remains quite limited—even with K=50 rollouts per task, a paired t-test across only 4 tasks gives just 4 degrees of freedom, which severely constrains statistical power for detecting meaningful differences.

The power calculation claiming ~80% power to detect a 7.5 percentage point improvement seems to be counting each rollout as independent within a task, but the actual paired comparison across tasks only has 3 degrees of freedom, which is potentially misleading about what we can actually conclude. The timeline is also still extremely compressed with zero buffer—Phase 0 gates by May 12, Phase 1 runs through May 20, Phase 2 is just 1-2 days, Phase 3 takes 6 days, and writing needs 4 days by May 28. I should double-check whether the OA-WAM numbers are actually cited in Table 1 as claimed, and I'm still thinking through what the paper's core contribution really is.

The empirical study plus the 2-layer MLP router is modest on its own—the practical gains are limited (10 rollouts per task down to 0 for new tasks) and the scientific value hinges on Phase 1 revealing meaningful phase-specific patterns. There's also an unresolved tension with the mimic-video work: the proposal reconciles the main text finding that τ_v=1 works best globally with Figure 5 showing oracle per-task peaks at intermediate values, but Phase 1 uses ground-truth action labels from LIBERO demos rather than closed-loop evaluation, so whether the per-observation τ_v* computed from demo labels actually predicts task success improvements in closed-loop remains an untested assumption.

For Phase 1 compute, the 40-60 hour estimate seems reasonable given 7.5M backbone forward passes on a 2B DiT with batch size 64. I should check if there's any concurrent work from March-May 2026 I've missed. Looking back at the revisions, all four moderate issues from Round 8 plus the two minor ones have been addressed—OA-WAM numbers are cited with table references, deployment calibration savings are quantified, the statistical protocol is specified with K=50 and Wilson confidence intervals, the scope of "first empirical characterization" is explicit, and the abstract leads with the empirical finding. This feels ready to move forward.

Now I'm identifying what might still be problematic: the paired t-test on 4 tasks only gives 3 degrees of freedom which is underpowered, there's potential distribution shift between demo and rollout states though Phase 1 addresses this with non-expert rollout data, and the absolute LIBERO performance is below SOTA but that's been positioned as secondary. The real question is whether there are any new critical issues in Round 9 that haven't been handled. I should search for recent WAM papers from April-May 2026 and verify the OA-WAM claims hold up.

I need to check whether OA-WAM's Table 1 results are actually available and match what's cited, look for any new papers post-Round 8, and verify the statistical power calculation is sound. The proposal's power analysis treats each of the 50 rollouts independently, which I should examine more carefully to see if that assumption holds.

The core issue is that while 50 rollouts per task gives good statistical power within a single task, the across-task comparison only has 4 task pairs, yielding just 3 degrees of freedom for a paired t-test—which is actually quite weak for detecting a 7.5 percentage point improvement. The proposal seems to conflate within-task power with across-task power, though it does acknowledge that the LIBERO-100 evaluation with 20 held-out tasks provides much stronger statistical power for validation. The 4-task SIMPLER-Bridge evaluation remains a genuine limitation regardless.

Now I'm weighing whether this paper merits a "revise," "pass," or "fail" for Round 9. The statistical underpowering in the across-task comparison is a real but minor issue—it's the same setup used in other WAM papers, so it's a standard benchmark constraint rather than a methodological flaw. The paper has resolved most of the critical and major issues from earlier rounds, leaving only minor to moderate concerns. Given the substantial improvements made and the defensibility of the core contribution, I need to decide on the final assessment.

Looking at the novelty score of 3/5: the per-observation routing is an incremental advance over mimic-video's fixed approach, but the empirical characterization of manipulation-phase requirements is genuinely novel. The router itself isn't architecturally innovative, and the work is narrowly focused on one model and one parameter. The competitive landscape with concurrent methods like OA-WAM and MotuBrain shows this is an active area. On feasibility, the approach is sound and builds on publicly available components, with a well-designed sanity check in Phase 0, though the compute requirements for Phase 1 appear to be cut off. The WAM track is extremely competitive with strong baselines, and while the deployment savings are now quantified, they're still modest for small-scale operations. My overall score averages to 3.5, which falls short of the 4.0 passing threshold—the novelty and impact scores are pulling it down. I'm weighing whether this needs revision or rejection for Round 9, given the lingering concerns around statistical power for the paired t-tests, the limited novelty of a simple MLP router, and the empirical scope being confined to a single model.

The core issue is that both the novelty and impact have inherent ceilings: the approach is fundamentally post-hoc routing on one specific model, and the contribution is scoped to an empirical study rather than something field-defining. With only one round left, I need to determine if these are problems that further revision can realistically address or if they're baked into the idea itself. Before finalizing my verdict, I should verify some key claims—the OA-WAM per-task numbers, whether there are newer WAM papers from May 2026 I've missed, and the mimic-video SIMPLER-Bridge results. Let me run those searches to verify the key claims and check for concurrent work.

For the verdict, I'm weighing whether this paper should pass or be revised again. The core issue is that while the authors have responsively addressed each round of feedback, the fundamental novelty and impact constraints of the approach keep it at a 3/5 in those dimensions, bringing the average below the 4.0 threshold. The paper isn't fundamentally flawed—it's a solid empirical contribution that CoRL would consider—but I need to decide if eight rounds of revision have brought it to acceptance quality or if it still falls short of the bar.

Given this is Round 9, I'm leaning toward one more focused revision request rather than a pass, since Round 10 will force a final decision anyway. Let me verify the technical claims first before committing to that verdict.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31f59460-1edd-4875-b186-76e059e6ba1f",
  "isSidechain": false,
  "requestId": "req_011CatgCp1J4aVKiojqc8ytT",
  "type": "assistant",
  "uuid": "0b3a7971-8d52-4a08-b63a-7986bbf4a270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019T6yCLf5ZvifkvuYf39EsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4466,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 39933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39933
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

_source line 9 · 2026-05-10T09:49:11.207Z_

I'll conduct independent verification searches before issuing my Round 9 verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b3a7971-8d52-4a08-b63a-7986bbf4a270",
  "isSidechain": false,
  "requestId": "req_011CatgCp1J4aVKiojqc8ytT",
  "type": "assistant",
  "uuid": "5530ddb5-80d3-4c46-8c2e-9a0e5c9e45fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019T6yCLf5ZvifkvuYf39EsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4466,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 39933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39933
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

_source line 10 · 2026-05-10T09:49:11.208Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LoMKZ1p8cyjRu3eCoHmrj8`</summary>

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
  "parentUuid": "5530ddb5-80d3-4c46-8c2e-9a0e5c9e45fc",
  "isSidechain": false,
  "requestId": "req_011CatgCp1J4aVKiojqc8ytT",
  "type": "assistant",
  "uuid": "0d517674-2c66-49dc-ac4d-ecd728986b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019T6yCLf5ZvifkvuYf39EsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4466,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 39933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39933
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

_source line 11 · 2026-05-10T09:49:11.218Z_

<details><summary>↩ Tool result · `toolu_01LoMKZ1p8cyjRu3eCoHmrj8`</summary>

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
  "parentUuid": "0d517674-2c66-49dc-ac4d-ecd728986b66",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "73954de4-918c-4888-9051-57620d29d275",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "0d517674-2c66-49dc-ac4d-ecd728986b66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
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
  "leafUuid": "73954de4-918c-4888-9051-57620d29d275",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Assistant

_source line 14 · 2026-05-10T09:49:18.662Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct my independent research. I'll run several searches in parallel to verify the key claims:

1. OA-WAM (arXiv:2605.06481) - verify per-task Table 1 numbers
2. New WAM papers from May 2026 not cited in the proposal
3. LingBot-VA verification
4. Any competing adaptive denoising/routing work for robotics
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73954de4-918c-4888-9051-57620d29d275",
  "isSidechain": false,
  "requestId": "req_011CatgLB8jb2aktV3weuc2c",
  "type": "assistant",
  "uuid": "d0af2220-2ed3-4bb1-ac90-2f50b166d151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJE5nfBEf3oWpvEeYSZiDv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 51564,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 51564,
          "cache_creation_input_tokens": 5484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5484
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

_source line 15 · 2026-05-10T09:49:18.990Z_

I'll run parallel searches to independently verify the key claims before issuing my verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0af2220-2ed3-4bb1-ac90-2f50b166d151",
  "isSidechain": false,
  "requestId": "req_011CatgLB8jb2aktV3weuc2c",
  "type": "assistant",
  "uuid": "c000302b-0337-4891-845a-73d3ea2cc260",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJE5nfBEf3oWpvEeYSZiDv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 51564,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 51564,
          "cache_creation_input_tokens": 5484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5484
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

_source line 16 · 2026-05-10T09:49:19.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0195TP3WiQXjakV83vBMs1dP`</summary>

```json
{
  "query": "OA-WAM object-addressable world action model arXiv 2605.06481 SimplerEnv results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c000302b-0337-4891-845a-73d3ea2cc260",
  "isSidechain": false,
  "requestId": "req_011CatgLB8jb2aktV3weuc2c",
  "type": "assistant",
  "uuid": "ef803307-6bd4-4fe1-b568-d33d1b4aabf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJE5nfBEf3oWpvEeYSZiDv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 51564,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 51564,
          "cache_creation_input_tokens": 5484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5484
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

_source line 17 · 2026-05-10T09:49:20.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sk5X3T2LG2tdcZrxpK2XPg`</summary>

```json
{
  "query": "adaptive video denoising depth routing robot manipulation policy 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef803307-6bd4-4fe1-b568-d33d1b4aabf4",
  "isSidechain": false,
  "requestId": "req_011CatgLB8jb2aktV3weuc2c",
  "type": "assistant",
  "uuid": "d9857719-3b12-49bb-b2da-384b557009e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJE5nfBEf3oWpvEeYSZiDv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 51564,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 51564,
          "cache_creation_input_tokens": 5484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5484
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

_source line 18 · 2026-05-10T09:49:21.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013WyGmkbt5DsteNUeuW3e8q`</summary>

```json
{
  "query": "world action model video noise level tau robot control 2026 CoRL arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9857719-3b12-49bb-b2da-384b557009e1",
  "isSidechain": false,
  "requestId": "req_011CatgLB8jb2aktV3weuc2c",
  "type": "assistant",
  "uuid": "f800f9ec-b3e0-47f8-a9ae-ffd50b02095a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJE5nfBEf3oWpvEeYSZiDv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5484,
      "cache_read_input_tokens": 51564,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 51564,
          "cache_creation_input_tokens": 5484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5484
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

_source line 19 · 2026-05-10T09:49:24.398Z_

<details><summary>↩ Tool result · `toolu_0195TP3WiQXjakV83vBMs1dP`</summary>

```text
Web search results for query: "OA-WAM object-addressable world action model arXiv 2605.06481 SimplerEnv results table"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"DreamZero: World Action Models are Zero-shot Policies","url":"https://dreamzero0.github.io/"},{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"[2603.24581] Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving","url":"https://arxiv.org/abs/2603.24581"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Paper page - World Action Models are Zero-shot Policies","url":"https://huggingface.co/papers/2602.15922"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"}]

I found the OA-WAM paper (arXiv 2605.06481). Based on the search results, the SimplerEnv WidowX (Bridge) per-task success results are shown in Table 1, and OA-WAM reaches 79.3% average success, leading all published VLA and WAM baselines on in-distribution LIBERO and SimplerEnv WidowX (Visual Matching).

The search results reference Table 1 containing the SimplerEnv results table, but the specific per-task breakdown table data itself is not fully displayed in the HTML excerpts I retrieved. To see the complete SimplerEnv results table with all individual task successes, you would need to view the full paper directly at the arxiv.org link provided in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef803307-6bd4-4fe1-b568-d33d1b4aabf4",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "e7b32152-aaa8-43f3-95b8-f7ee9487920c",
  "toolUseResult": {
    "query": "OA-WAM object-addressable world action model arXiv 2605.06481 SimplerEnv results table",
    "results": [
      {
        "tool_use_id": "srvtoolu_017z4Ge9BviybqSwPTmsSQjX",
        "content": [
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
          },
          {
            "title": "World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/html/2602.15922v1"
          },
          {
            "title": "DreamZero: World Action Models are Zero-shot Policies",
            "url": "https://dreamzero0.github.io/"
          },
          {
            "title": "When to Trust Imagination: Adaptive Action Execution for World Action Models",
            "url": "https://arxiv.org/html/2605.06222"
          },
          {
            "title": "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields",
            "url": "https://arxiv.org/html/2605.06192v1"
          },
          {
            "title": "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models",
            "url": "https://arxiv.org/html/2605.06247v1"
          },
          {
            "title": "[2603.24581] Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving",
            "url": "https://arxiv.org/abs/2603.24581"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "Paper page - World Action Models are Zero-shot Policies",
            "url": "https://huggingface.co/papers/2602.15922"
          },
          {
            "title": "[2602.15922] World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/abs/2602.15922"
          }
        ]
      },
      "I found the OA-WAM paper (arXiv 2605.06481). Based on the search results, the SimplerEnv WidowX (Bridge) per-task success results are shown in Table 1, and OA-WAM reaches 79.3% average success, leading all published VLA and WAM baselines on in-distribution LIBERO and SimplerEnv WidowX (Visual Matching).\n\nThe search results reference Table 1 containing the SimplerEnv results table, but the specific per-task breakdown table data itself is not fully displayed in the HTML excerpts I retrieved. To see the complete SimplerEnv results table with all individual task successes, you would need to view the full paper directly at the arxiv.org link provided in the search results."
    ],
    "durationSeconds": 4.577900727999993
  },
  "sourceToolAssistantUUID": "ef803307-6bd4-4fe1-b568-d33d1b4aabf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T09:49:28.507Z_

<details><summary>↩ Tool result · `toolu_01Sk5X3T2LG2tdcZrxpK2XPg`</summary>

```text
Web search results for query: "adaptive video denoising depth routing robot manipulation policy 2026 arxiv"

Links: [{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation","url":"https://arxiv.org/html/2510.15530v1"},{"title":"Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation","url":"https://arxiv.org/html/2604.01414"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"RoboTransfer: Controllable Geometry-Consistent Video Diffusion for Manipulation Policy Transfer","url":"https://arxiv.org/html/2505.23171"},{"title":"Abstracting Robot Manipulation Skills via Mixture-of- ...","url":"https://arxiv.org/pdf/2601.21251"},{"title":"Adaptive Diffusion Policy Optimization for Robotic Manipulation","url":"https://arxiv.org/html/2505.08376v1"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"}]

Based on the web search results, here are several relevant recent papers on adaptive video denoising, depth routing, and robot manipulation policies from arXiv in 2026 and late 2025:

## Key Papers Found:

1. **ADPro: Adaptive Diffusion Policy for Robotic Manipulation**
   - Proposes a test-time adaptive diffusion policy that injects structure into the denoising process through manifold-constrained denoising guided by relative pose between end-effector and target object, a Gaussian spherical prior for constraining denoising steps, and a coarse initialization strategy based on point cloud registration.

2. **VO-DP: Vision-Only Robotic Manipulation**
   - Uses a vision-only conditioned Denoising Diffusion Probabilistic Model (DDPM) for the policy head, and achieves 96.7% success rate on real-world tasks.

3. **Learning When to See and When to Feel: Adaptive Vision-Torque Fusion**
   - Two independent UNets are trained in parallel and their noise predictions are blended at each denoising step via a learned routing network. This paper uses an adaptive routing mechanism during denoising.

4. **X-WAM: Unified 4D World Action Model**
   - Features a lightweight depth adaptation module for spatial reconstruction and Asynchronous Noise Sampling (ANS) for efficient action decoding, replicating the final blocks of pretrained Diffusion Transformer into a dedicated depth prediction branch.

5. **Adaptive Diffusion Policy Optimization for Robotic Manipulation**
   - Addresses optimization of diffusion models for robotic manipulation, using the conditional denoising process of the diffusion model to represent robot behavior policies.

These papers directly address adaptive mechanisms, depth processing, denoising routing, and manipulation policies within the diffusion model framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9857719-3b12-49bb-b2da-384b557009e1",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "0a328699-ec18-49a3-aec8-373debef443a",
  "toolUseResult": {
    "query": "adaptive video denoising depth routing robot manipulation policy 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_019TZL8x58XTfetDnevoGg9A",
        "content": [
          {
            "title": "ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation",
            "url": "https://arxiv.org/html/2508.06266"
          },
          {
            "title": "VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation",
            "url": "https://arxiv.org/html/2510.15530v1"
          },
          {
            "title": "Learning When to See and When to Feel: Adaptive Vision-Torque Fusion for Contact-Aware Manipulation",
            "url": "https://arxiv.org/html/2604.01414"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "RoboTransfer: Controllable Geometry-Consistent Video Diffusion for Manipulation Policy Transfer",
            "url": "https://arxiv.org/html/2505.23171"
          },
          {
            "title": "Abstracting Robot Manipulation Skills via Mixture-of- ...",
            "url": "https://arxiv.org/pdf/2601.21251"
          },
          {
            "title": "Adaptive Diffusion Policy Optimization for Robotic Manipulation",
            "url": "https://arxiv.org/html/2505.08376v1"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Video Generation Models in Robotics: Applications, Research Challenges, Future Directions",
            "url": "https://arxiv.org/html/2601.07823v1"
          },
          {
            "title": "Unified Video Action Model | Request PDF",
            "url": "https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"
          }
        ]
      },
      "Based on the web search results, here are several relevant recent papers on adaptive video denoising, depth routing, and robot manipulation policies from arXiv in 2026 and late 2025:\n\n## Key Papers Found:\n\n1. **ADPro: Adaptive Diffusion Policy for Robotic Manipulation**\n   - Proposes a test-time adaptive diffusion policy that injects structure into the denoising process through manifold-constrained denoising guided by relative pose between end-effector and target object, a Gaussian spherical prior for constraining denoising steps, and a coarse initialization strategy based on point cloud registration.\n\n2. **VO-DP: Vision-Only Robotic Manipulation**\n   - Uses a vision-only conditioned Denoising Diffusion Probabilistic Model (DDPM) for the policy head, and achieves 96.7% success rate on real-world tasks.\n\n3. **Learning When to See and When to Feel: Adaptive Vision-Torque Fusion**\n   - Two independent UNets are trained in parallel and their noise predictions are blended at each denoising step via a learned routing network. This paper uses an adaptive routing mechanism during denoising.\n\n4. **X-WAM: Unified 4D World Action Model**\n   - Features a lightweight depth adaptation module for spatial reconstruction and Asynchronous Noise Sampling (ANS) for efficient action decoding, replicating the final blocks of pretrained Diffusion Transformer into a dedicated depth prediction branch.\n\n5. **Adaptive Diffusion Policy Optimization for Robotic Manipulation**\n   - Addresses optimization of diffusion models for robotic manipulation, using the conditional denoising process of the diffusion model to represent robot behavior policies.\n\nThese papers directly address adaptive mechanisms, depth processing, denoising routing, and manipulation policies within the diffusion model framework."
    ],
    "durationSeconds": 7.907741427000001
  },
  "sourceToolAssistantUUID": "d9857719-3b12-49bb-b2da-384b557009e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T09:49:29.231Z_

<details><summary>↩ Tool result · `toolu_013WyGmkbt5DsteNUeuW3e8q`</summary>

```text
Web search results for query: "world action model video noise level tau robot control 2026 CoRL arxiv"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/html/2510.10125v3"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"}]

Based on the search results, I found several relevant papers on world action models for robot control from 2026 and recent work on arxiv. Here are the key findings:

## Recent World Action Model Research (2026)

DreamZero is a World Action Model built upon a pretrained video diffusion backbone that learns physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.

X-WAM is a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, featuring a lightweight depth adaptation module for spatial reconstruction and Asynchronous Noise Sampling (ANS) for efficient action decoding.

## Video Noise and Denoising Approaches

A key technical advancement addresses the challenge of jointly generating video and actions. While synthesizing high-fidelity video necessitates numerous denoising steps, low-dimensional actions require far fewer steps and can be accurately recovered even from highly noisy video latents. Asynchronous Noise Sampling (ANS) introduces a specialized asynchronous denoising schedule for inference: it rapidly decodes precise actions using only a fraction of the initial steps to allow them to be immediately executed by the policy, and subsequently completes the remaining steps to render high-fidelity future videos.

Noisy History Augmentation is a training scheme that enables partial denoising at inference time, based on the insight that action decoding does not always require pixel-perfect reconstruction; instead, it can rely on robust semantic structures. By training the action decoder to predict from partially noisy latent representations, computational overhead is significantly reduced while maintaining precise action prediction.

## Robustness Under Perturbations

WAMs generally demonstrate strong robustness to noise, lighting and layout perturbations in both single-arm and bimanual settings, with this robustness believed to be at least partially attributable to the spatiotemporal priors inherited from their world model backbones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f800f9ec-b3e0-47f8-a9ae-ffd50b02095a",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "afb9a35b-a972-475b-a0bc-fbc3ecb2b612",
  "toolUseResult": {
    "query": "world action model video noise level tau robot control 2026 CoRL arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_011BzbtB8n7DHFeXi7KKUWvj",
        "content": [
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/html/2602.15922v1"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields",
            "url": "https://arxiv.org/html/2605.06192v1"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2605.00080v1"
          },
          {
            "title": "Ctrl-World: A Controllable Generative World Model for Robot Manipulation",
            "url": "https://arxiv.org/html/2510.10125v3"
          },
          {
            "title": "Being-H0.7: A Latent World-Action Model from Egocentric Videos",
            "url": "https://arxiv.org/html/2605.00078v1"
          },
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on world action models for robot control from 2026 and recent work on arxiv. Here are the key findings:\n\n## Recent World Action Model Research (2026)\n\nDreamZero is a World Action Model built upon a pretrained video diffusion backbone that learns physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves.\n\nX-WAM is a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, featuring a lightweight depth adaptation module for spatial reconstruction and Asynchronous Noise Sampling (ANS) for efficient action decoding.\n\n## Video Noise and Denoising Approaches\n\nA key technical advancement addresses the challenge of jointly generating video and actions. While synthesizing high-fidelity video necessitates numerous denoising steps, low-dimensional actions require far fewer steps and can be accurately recovered even from highly noisy video latents. Asynchronous Noise Sampling (ANS) introduces a specialized asynchronous denoising schedule for inference: it rapidly decodes precise actions using only a fraction of the initial steps to allow them to be immediately executed by the policy, and subsequently completes the remaining steps to render high-fidelity future videos.\n\nNoisy History Augmentation is a training scheme that enables partial denoising at inference time, based on the insight that action decoding does not always require pixel-perfect reconstruction; instead, it can rely on robust semantic structures. By training the action decoder to predict from partially noisy latent representations, computational overhead is significantly reduced while maintaining precise action prediction.\n\n## Robustness Under Perturbations\n\nWAMs generally demonstrate strong robustness to noise, lighting and layout perturbations in both single-arm and bimanual settings, with this robustness believed to be at least partially attributable to the spatiotemporal priors inherited from their world model backbones."
    ],
    "durationSeconds": 8.032618386999996
  },
  "sourceToolAssistantUUID": "f800f9ec-b3e0-47f8-a9ae-ffd50b02095a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T09:49:37.708Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for more specific information to verify the OA-WAM per-task numbers and check for any new concurrent papers I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afb9a35b-a972-475b-a0bc-fbc3ecb2b612",
  "isSidechain": false,
  "requestId": "req_011CatgMVwMYV8dzMamyyetj",
  "type": "assistant",
  "uuid": "780a97d2-9c5a-4ed8-bd17-7cc10f07f403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4hTwmVHuYc9EskaxcME7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 57048,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 349,
          "cache_read_input_tokens": 57048,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2841
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

_source line 23 · 2026-05-10T09:49:40.733Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016rFZAPQYcse46siDTV4me1`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "Find Table 1 showing SimplerEnv WidowX Bridge results. Extract per-task success rates for: Spoon on Towel, Carrot on Plate, Stack Cube/Blocks, Eggplant in Basket. Also report the overall average and which protocol (Visual Matching or Variant Aggregation) was used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "780a97d2-9c5a-4ed8-bd17-7cc10f07f403",
  "isSidechain": false,
  "requestId": "req_011CatgMVwMYV8dzMamyyetj",
  "type": "assistant",
  "uuid": "4ea0c56d-ac6f-49b3-b570-e24b7a9e6aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4hTwmVHuYc9EskaxcME7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 57048,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 349,
          "cache_read_input_tokens": 57048,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2841
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

_source line 24 · 2026-05-10T09:49:42.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019gnFaeFeNdsEnTbrotzBUD`</summary>

```json
{
  "query": "mimic-video arXiv 2512.15692 SIMPLER-Bridge tau_v noise level per-task results table Stack Blocks Carrot Spoon Eggplant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ea0c56d-ac6f-49b3-b570-e24b7a9e6aaa",
  "isSidechain": false,
  "requestId": "req_011CatgMVwMYV8dzMamyyetj",
  "type": "assistant",
  "uuid": "789cfb16-b976-4fb4-86b0-e0cc4d48b43e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4hTwmVHuYc9EskaxcME7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 57048,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 349,
          "cache_read_input_tokens": 57048,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2841
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

_source line 25 · 2026-05-10T09:49:43.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MWSsAtwmM9nWdV4iq15Lbo`</summary>

```json
{
  "query": "CKT-WAM EA-WM adaptive denoising video action model SIMPLER LIBERO 2026 arxiv CoRL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "789cfb16-b976-4fb4-86b0-e0cc4d48b43e",
  "isSidechain": false,
  "requestId": "req_011CatgMVwMYV8dzMamyyetj",
  "type": "assistant",
  "uuid": "d407a006-e63c-4d64-96fe-36a898664236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4hTwmVHuYc9EskaxcME7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 57048,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 349,
          "cache_read_input_tokens": 57048,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2841
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
  "leafUuid": "d407a006-e63c-4d64-96fe-36a898664236",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Tool result

_source line 28 · 2026-05-10T09:49:44.728Z_

<details><summary>↩ Tool result · `toolu_016rFZAPQYcse46siDTV4me1`</summary>

```text
# SimplerEnv WidowX Bridge Results from OA-WAM

Based on Table 1 in the document, here are the per-task success rates for SimplerEnv WidowX (Visual Matching):

| Task | Success Rate |
|------|--------------|
| Spoon on Towel | 83.0% |
| Carrot on Plate | 71.1% |
| Stack Cube | 65.0% |
| Eggplant in Basket | 98.2% |
| **Overall Average** | **79.3%** |

The evaluation used the **Visual Matching protocol**, which the paper describes as measuring "sim-to-real visual matching against real WidowX scenes." This represents OA-WAM's performance across four manipulation tasks, with notable strength on the basket-placement task and more moderate performance on the stacking challenge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ea0c56d-ac6f-49b3-b570-e24b7a9e6aaa",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "ebe1c84c-1ea5-401c-83fa-cf9d9b184d2a",
  "toolUseResult": {
    "bytes": 793456,
    "code": 200,
    "codeText": "OK",
    "result": "# SimplerEnv WidowX Bridge Results from OA-WAM\n\nBased on Table 1 in the document, here are the per-task success rates for SimplerEnv WidowX (Visual Matching):\n\n| Task | Success Rate |\n|------|--------------|\n| Spoon on Towel | 83.0% |\n| Carrot on Plate | 71.1% |\n| Stack Cube | 65.0% |\n| Eggplant in Basket | 98.2% |\n| **Overall Average** | **79.3%** |\n\nThe evaluation used the **Visual Matching protocol**, which the paper describes as measuring \"sim-to-real visual matching against real WidowX scenes.\" This represents OA-WAM's performance across four manipulation tasks, with notable strength on the basket-placement task and more moderate performance on the stacking challenge.",
    "durationMs": 3990,
    "url": "https://arxiv.org/html/2605.06481v1"
  },
  "sourceToolAssistantUUID": "4ea0c56d-ac6f-49b3-b570-e24b7a9e6aaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T09:49:48.927Z_

<details><summary>↩ Tool result · `toolu_019gnFaeFeNdsEnTbrotzBUD`</summary>

```text
Web search results for query: "mimic-video arXiv 2512.15692 SIMPLER-Bridge tau_v noise level per-task results table Stack Blocks Carrot Spoon Eggplant"

Links: [{"title":"[2512.15692] mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/abs/2512.15692"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/html/2512.15692"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | Papers | HyperAI","url":"https://vercel.hyper.ai/en/papers/2512.15692"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://mimic-video.github.io/"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.15692"},{"title":"GitHub - mimic-video/mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs · GitHub","url":"https://github.com/mimic-video/mimic-video"},{"title":"Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation","url":"https://arxiv.org/html/2512.07212v1"},{"title":"GitHub - lucidrains/mimic-video: Implementation of Mimic-Video, Video-Action Models for SOTA Generalizable Robot Control Beyond VLAs · GitHub","url":"https://github.com/lucidrains/mimic-video"},{"title":"SFBD-OMNI: Bridge models for lossy measurement restoration with limited clean samples","url":"https://arxiv.org/html/2512.17051"},{"title":"MIND-V: Hierarchical Video Generation for Long-Horizon Robotic Manipulation with RL-based Physical Alignment","url":"https://arxiv.org/html/2512.06628v1"}]

Based on the search results for arXiv paper 2512.15692 on mimic-video, I found relevant information about the τ_v (tau_v) noise level parameter and its effects on SIMPLER-Bridge performance:

The choice of the video model's cutoff flow time, τ_v, is a critical inference hyperparameter. Stopping the video generation process early and conditioning the action decoder on a "noisy" visual plan yields substantially better performance than allowing the video model to fully denoise its prediction.

More specifically, τ_v = 1 (maximum noise), not full denoising, is preferred due to distribution mismatch and richer intermediate representations in the video model. Conditioning on noisy video latents acts as effective augmentation, improving robustness, while full denoising leads to higher action reconstruction error and degraded performance.

By adjusting the flow parameter τ_v, the fixed trained model can be specialized to individual task dynamics, achieving further performance gains at the cost of modest increases in computation.

However, the search results provided do not contain the specific per-task results table with success rates for Stack Blocks, Carrot, Spoon, and Eggplant tasks. To access that detailed table, you would need to consult the full paper directly at https://arxiv.org/abs/2512.15692 or the HTML version at https://arxiv.org/html/2512.15692.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "789cfb16-b976-4fb4-86b0-e0cc4d48b43e",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "3d5d4ecd-7a7b-4261-ace4-ec60e6fd9a1e",
  "toolUseResult": {
    "query": "mimic-video arXiv 2512.15692 SIMPLER-Bridge tau_v noise level per-task results table Stack Blocks Carrot Spoon Eggplant",
    "results": [
      {
        "tool_use_id": "srvtoolu_014iRQwamsQtbujavk1CJLid",
        "content": [
          {
            "title": "[2512.15692] mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs",
            "url": "https://arxiv.org/abs/2512.15692"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs",
            "url": "https://arxiv.org/html/2512.15692"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | Papers | HyperAI",
            "url": "https://vercel.hyper.ai/en/papers/2512.15692"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs",
            "url": "https://mimic-video.github.io/"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2512.15692"
          },
          {
            "title": "GitHub - mimic-video/mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs · GitHub",
            "url": "https://github.com/mimic-video/mimic-video"
          },
          {
            "title": "Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation",
            "url": "https://arxiv.org/html/2512.07212v1"
          },
          {
            "title": "GitHub - lucidrains/mimic-video: Implementation of Mimic-Video, Video-Action Models for SOTA Generalizable Robot Control Beyond VLAs · GitHub",
            "url": "https://github.com/lucidrains/mimic-video"
          },
          {
            "title": "SFBD-OMNI: Bridge models for lossy measurement restoration with limited clean samples",
            "url": "https://arxiv.org/html/2512.17051"
          },
          {
            "title": "MIND-V: Hierarchical Video Generation for Long-Horizon Robotic Manipulation with RL-based Physical Alignment",
            "url": "https://arxiv.org/html/2512.06628v1"
          }
        ]
      },
      "Based on the search results for arXiv paper 2512.15692 on mimic-video, I found relevant information about the τ_v (tau_v) noise level parameter and its effects on SIMPLER-Bridge performance:\n\nThe choice of the video model's cutoff flow time, τ_v, is a critical inference hyperparameter. Stopping the video generation process early and conditioning the action decoder on a \"noisy\" visual plan yields substantially better performance than allowing the video model to fully denoise its prediction.\n\nMore specifically, τ_v = 1 (maximum noise), not full denoising, is preferred due to distribution mismatch and richer intermediate representations in the video model. Conditioning on noisy video latents acts as effective augmentation, improving robustness, while full denoising leads to higher action reconstruction error and degraded performance.\n\nBy adjusting the flow parameter τ_v, the fixed trained model can be specialized to individual task dynamics, achieving further performance gains at the cost of modest increases in computation.\n\nHowever, the search results provided do not contain the specific per-task results table with success rates for Stack Blocks, Carrot, Spoon, and Eggplant tasks. To access that detailed table, you would need to consult the full paper directly at https://arxiv.org/abs/2512.15692 or the HTML version at https://arxiv.org/html/2512.15692."
    ],
    "durationSeconds": 6.651173634000006
  },
  "sourceToolAssistantUUID": "789cfb16-b976-4fb4-86b0-e0cc4d48b43e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T09:49:50.708Z_

<details><summary>↩ Tool result · `toolu_01MWSsAtwmM9nWdV4iq15Lbo`</summary>

```text
Web search results for query: "CKT-WAM EA-WM adaptive denoising video action model SIMPLER LIBERO 2026 arxiv CoRL"

Links: [{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"Unified Video Action Model | Request PDF","url":"https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"Controllable Video Generation: A Survey","url":"https://arxiv.org/html/2507.16869v3"},{"title":"Semantic-Aware Adaptive Video Streaming Using Latent Diffusion Models for Wireless Networks","url":"https://arxiv.org/html/2502.05695v1"}]

Based on the search results, I found relevant research papers related to your query. Here are the key findings:

## CKT-WAM (Context Knowledge Transfer Between World Action Models)

CKT-WAM consistently improves zero-shot generalization and achieves the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters, while approaching full fine-tuning performance. Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step and long-horizon tasks.

## EA-WM (Event-Aware Generative World Model)

EA-WM is an Event-Aware Generative World Model that effectively closes the loop between kinematic control and visual perception. The paper explores how video generation can be improved with action guidance for robotic world models.

## Related World Action Models Context

Recent literature has formalized two dominant WAM architectures: imagine-then-execute models that causally generate future visual trajectories before predicting actions, and joint-modeling frameworks that denoise future video and action tokens within a shared generative process.

## Additional Recent Work

The search also revealed other recent adaptive denoising approaches: X-WAM proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency.

These papers appear to be recent submissions to arxiv (from the last few days to weeks) and represent cutting-edge work in world action models for robotic control and planning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d407a006-e63c-4d64-96fe-36a898664236",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "56f65757-5866-4fdc-b1fc-85edeb88835b",
  "toolUseResult": {
    "query": "CKT-WAM EA-WM adaptive denoising video action model SIMPLER LIBERO 2026 arxiv CoRL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XysvDuN3skfE3bCSHnRXTn",
        "content": [
          {
            "title": "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models",
            "url": "https://arxiv.org/html/2605.06247v1"
          },
          {
            "title": "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields",
            "url": "https://arxiv.org/html/2605.06192v1"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://arxiv.org/html/2603.16666v1"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v1"
          },
          {
            "title": "Unified Video Action Model | Request PDF",
            "url": "https://www.researchgate.net/publication/395361978_Unified_Video_Action_Model"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"
          },
          {
            "title": "Controllable Video Generation: A Survey",
            "url": "https://arxiv.org/html/2507.16869v3"
          },
          {
            "title": "Semantic-Aware Adaptive Video Streaming Using Latent Diffusion Models for Wireless Networks",
            "url": "https://arxiv.org/html/2502.05695v1"
          }
        ]
      },
      "Based on the search results, I found relevant research papers related to your query. Here are the key findings:\n\n## CKT-WAM (Context Knowledge Transfer Between World Action Models)\n\nCKT-WAM consistently improves zero-shot generalization and achieves the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters, while approaching full fine-tuning performance. Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step and long-horizon tasks.\n\n## EA-WM (Event-Aware Generative World Model)\n\nEA-WM is an Event-Aware Generative World Model that effectively closes the loop between kinematic control and visual perception. The paper explores how video generation can be improved with action guidance for robotic world models.\n\n## Related World Action Models Context\n\nRecent literature has formalized two dominant WAM architectures: imagine-then-execute models that causally generate future visual trajectories before predicting actions, and joint-modeling frameworks that denoise future video and action tokens within a shared generative process.\n\n## Additional Recent Work\n\nThe search also revealed other recent adaptive denoising approaches: X-WAM proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency.\n\nThese papers appear to be recent submissions to arxiv (from the last few days to weeks) and represent cutting-edge work in world action models for robotic control and planning."
    ],
    "durationSeconds": 7.481644875999977
  },
  "sourceToolAssistantUUID": "d407a006-e63c-4d64-96fe-36a898664236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T09:50:03.881Z_

<details><summary>Logged reasoning block</summary>

```text
The OA-WAM per-task numbers are verified! Table 1 of arXiv:2605.06481v1 does show:
- Spoon on Towel: 83.0%
- Carrot on Plate: 71.1%
- Stack Cube: 65.0%
- Eggplant in Basket: 98.2%
- Overall Average: 79.3%
Using Visual Matching protocol

This is a positive verification for the Round 9 proposal. The numbers cited are accurate.

Now let me check for any new papers I might have missed. I found:


- CKT-WAM (arXiv:2605.06247) - Parameter-Efficient Context Knowledge Transfer Between World Action Models
- EA-WM (arXiv:2605.06192) - Event-Aware Generative World Model

Both are from May 2026 and not cited in the proposal. CKT-WAM appears to focus on transfer learning between WAMs rather than adaptive denoising depth, so it's likely orthogonal to CDR's claims. EA-WM deals with event-aware world modeling with structured kinematic-to-visual action fields, which also doesn't directly address the proposal's core mechanisms.

I should look more closely at ADPro (Test-time Adaptive Diffusion Policy) and especially "Learning When to See and When to Feel: Adaptive Vision-Torque Fusion" from April 2026, since that one explicitly uses adaptive routing during denoising—which seems much more directly aligned with CDR's approach. Let me pull those papers to verify the connection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f65757-5866-4fdc-b1fc-85edeb88835b",
  "isSidechain": false,
  "requestId": "req_011CatgP5VjjG1F8hpR3kEPL",
  "type": "assistant",
  "uuid": "17cf2cd1-3d24-4050-b0af-959dba03017e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BuCXqUbQqMz2BK8M3raRmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 59889,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 59889,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2373
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

_source line 32 · 2026-05-10T09:50:04.310Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016EySwyAVWeCuuB5L9LcLpK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06247",
  "prompt": "What is the key contribution of CKT-WAM? Does it involve adaptive video denoising depth, per-observation tau_v routing, or test-time video noise level selection? What benchmarks does it evaluate on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17cf2cd1-3d24-4050-b0af-959dba03017e",
  "isSidechain": false,
  "requestId": "req_011CatgP5VjjG1F8hpR3kEPL",
  "type": "assistant",
  "uuid": "2c7dc0ca-6e69-4519-b27b-75e436d6bc8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BuCXqUbQqMz2BK8M3raRmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 59889,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 59889,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2373
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

_source line 33 · 2026-05-10T09:50:05.763Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KpHY668ZC7o1rumX5rs8ke`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01414",
  "prompt": "What is the key contribution? Does it involve adaptive routing during video diffusion denoising, per-observation noise level selection, or tau_v routing in world action models? What benchmarks does it evaluate on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c7dc0ca-6e69-4519-b27b-75e436d6bc8f",
  "isSidechain": false,
  "requestId": "req_011CatgP5VjjG1F8hpR3kEPL",
  "type": "assistant",
  "uuid": "fa0edf7a-fafe-422c-990d-5579562672c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BuCXqUbQqMz2BK8M3raRmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 59889,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 59889,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2373
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

_source line 34 · 2026-05-10T09:50:06.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013fkQVaknrucfzgdHvhfSZc`</summary>

```json
{
  "query": "mimic-video tau_v=1 best performance SIMPLER autonomous policy Figure 5 per-task oracle intermediate noise 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa0edf7a-fafe-422c-990d-5579562672c6",
  "isSidechain": false,
  "requestId": "req_011CatgP5VjjG1F8hpR3kEPL",
  "type": "assistant",
  "uuid": "deaabb92-0788-476d-9428-796f5fce61d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BuCXqUbQqMz2BK8M3raRmS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 59889,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 59889,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2373
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

_source line 35 · 2026-05-10T09:50:08.555Z_

<details><summary>↩ Tool result · `toolu_016EySwyAVWeCuuB5L9LcLpK`</summary>

```text
# CKT-WAM: Key Contributions and Evaluation

## Key Contribution

CKT-WAM's primary innovation is a parameter-efficient knowledge transfer mechanism. Rather than relying on output imitation or dense hidden-state matching, it "transfers teacher WAM's knowledge into a student WAM through a compact context in the text embedding space."

The framework uses several technical components: learnable-query cross attention for token compression, an always-on generalized adapter, a lightweight router, and sparsely activated specialized adapters. This allows knowledge injection with minimal architectural changes to the student model.

## Not Related to Your Mentioned Topics

The paper does not involve adaptive video denoising depth, per-observation tau_v routing, or test-time video noise level selection. These appear to be unrelated concepts.

## Benchmarks Evaluated

CKT-WAM demonstrates results on two primary benchmarks:

1. **LIBERO-Plus (simulation)**: Achieved 86.1% total success rate while using only 1.17% trainable parameters

2. **Real-world manipulation tasks**: Demonstrated 83.3% average success rate across four multi-step, long-horizon tasks

The research shows the approach approaches full fine-tuning performance while maintaining parameter efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c7dc0ca-6e69-4519-b27b-75e436d6bc8f",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "5b484a1d-4c82-4203-bf42-f438fc9e82f0",
  "toolUseResult": {
    "bytes": 47980,
    "code": 200,
    "codeText": "OK",
    "result": "# CKT-WAM: Key Contributions and Evaluation\n\n## Key Contribution\n\nCKT-WAM's primary innovation is a parameter-efficient knowledge transfer mechanism. Rather than relying on output imitation or dense hidden-state matching, it \"transfers teacher WAM's knowledge into a student WAM through a compact context in the text embedding space.\"\n\nThe framework uses several technical components: learnable-query cross attention for token compression, an always-on generalized adapter, a lightweight router, and sparsely activated specialized adapters. This allows knowledge injection with minimal architectural changes to the student model.\n\n## Not Related to Your Mentioned Topics\n\nThe paper does not involve adaptive video denoising depth, per-observation tau_v routing, or test-time video noise level selection. These appear to be unrelated concepts.\n\n## Benchmarks Evaluated\n\nCKT-WAM demonstrates results on two primary benchmarks:\n\n1. **LIBERO-Plus (simulation)**: Achieved 86.1% total success rate while using only 1.17% trainable parameters\n\n2. **Real-world manipulation tasks**: Demonstrated 83.3% average success rate across four multi-step, long-horizon tasks\n\nThe research shows the approach approaches full fine-tuning performance while maintaining parameter efficiency.",
    "durationMs": 4240,
    "url": "https://arxiv.org/abs/2605.06247"
  },
  "sourceToolAssistantUUID": "2c7dc0ca-6e69-4519-b27b-75e436d6bc8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T09:50:09.588Z_

<details><summary>↩ Tool result · `toolu_01KpHY668ZC7o1rumX5rs8ke`</summary>

```text
# Key Contributions and Evaluation

## Main Contribution

The paper's primary contribution is an **adaptive vision-torque fusion strategy** for robotic manipulation. According to the abstract, the approach "ignores F/T signals during non-contact phases while adaptively leveraging both vision and torque information during contact."

This differs from your listed options—it's not about adaptive routing during diffusion denoising, per-observation noise selection, or tau_v routing. Instead, it focuses on **contact-aware multimodal sensor fusion** that selectively uses force/torque data based on whether the robot is in contact with objects.

## Performance Gains

The paper reports that their method "outperforms the strongest baseline by 14% in success rate," emphasizing that contact-aware integration of multiple sensor modalities improves manipulation performance.

## Benchmarks

The abstract does not specify which particular benchmarks were used for evaluation. The content provided only confirms experimental results demonstrating the 14% improvement over baselines, without naming specific manipulation tasks or datasets tested.

The work is situated within **diffusion-based manipulation policies** and compares various F/T-vision integration strategies, but specific benchmark names are not detailed in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa0edf7a-fafe-422c-990d-5579562672c6",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "12c1f6ad-c79d-4153-b0ad-548a0ec675bd",
  "toolUseResult": {
    "bytes": 44951,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Contributions and Evaluation\n\n## Main Contribution\n\nThe paper's primary contribution is an **adaptive vision-torque fusion strategy** for robotic manipulation. According to the abstract, the approach \"ignores F/T signals during non-contact phases while adaptively leveraging both vision and torque information during contact.\"\n\nThis differs from your listed options—it's not about adaptive routing during diffusion denoising, per-observation noise selection, or tau_v routing. Instead, it focuses on **contact-aware multimodal sensor fusion** that selectively uses force/torque data based on whether the robot is in contact with objects.\n\n## Performance Gains\n\nThe paper reports that their method \"outperforms the strongest baseline by 14% in success rate,\" emphasizing that contact-aware integration of multiple sensor modalities improves manipulation performance.\n\n## Benchmarks\n\nThe abstract does not specify which particular benchmarks were used for evaluation. The content provided only confirms experimental results demonstrating the 14% improvement over baselines, without naming specific manipulation tasks or datasets tested.\n\nThe work is situated within **diffusion-based manipulation policies** and compares various F/T-vision integration strategies, but specific benchmark names are not detailed in this excerpt.",
    "durationMs": 3823,
    "url": "https://arxiv.org/abs/2604.01414"
  },
  "sourceToolAssistantUUID": "fa0edf7a-fafe-422c-990d-5579562672c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T09:50:13.040Z_

<details><summary>↩ Tool result · `toolu_013fkQVaknrucfzgdHvhfSZc`</summary>

```text
Web search results for query: "mimic-video tau_v=1 best performance SIMPLER autonomous policy Figure 5 per-task oracle intermediate noise 2025"

Links: [{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/html/2512.15692v1"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://mimic-video.github.io/"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | Papers | HyperAI","url":"https://hyper.ai/en/papers/2512.15692"},{"title":"GitHub - mimic-video/mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs · GitHub","url":"https://github.com/mimic-video/mimic-video"},{"title":"Mimic-Video: Video-Driven Robotic Control","url":"https://www.emergentmind.com/topics/mimic-video"},{"title":"Mimic-Video: Efficient Robot Control Model | PDF | Applied Mathematics","url":"https://www.scribd.com/document/968265710/4"},{"title":"GitHub - lucidrains/mimic-video: Implementation of Mimic-Video, Video-Action Models for SOTA Generalizable Robot Control Beyond VLAs · GitHub","url":"https://github.com/lucidrains/mimic-video"},{"title":"[2512.15692] mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs","url":"https://arxiv.org/abs/2512.15692"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs - YouTube","url":"https://www.youtube.com/watch?v=_LkBFL5m1WU"},{"title":"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.15692"}]

Based on the search results, I found relevant information about your query regarding mimic-video with the τ_v=1 parameter and SIMPLER benchmark performance.

The best autonomous policy performance in the SIMPLER experiments is achieved when stopping the video generation process early (at the highest noise level), with conditioning on a "noisy" visual plan yielding substantially better performance than allowing the video model to fully denoise its prediction.

Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies. More specifically, the best autonomous policy performance in SIMPLER experiments is achieved at the highest noise level τ_v = 1.

Operating at τ_v = 1 requires only a single forward pass of the video backbone to generate conditioning features, resulting in both the highest average performance and the fastest inference speed.

Regarding the explanation for this counterintuitive finding, the authors hypothesize that imperfect video generation introduces artifacts, and consequently, fully denoised video latents may diverge from the training distribution, presenting out-of-distribution conditioning to the action decoder.

In terms of overall performance on SIMPLER-Bridge, mimic-video with τ_v tuning achieves an average success rate of 56.3%, compared to 14.6% (OpenVLA) and 35.4% (π0.5-style VLA).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deaabb92-0788-476d-9428-796f5fce61d9",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "c9d25d39-c9a7-4ec2-8133-f7d532b0ecdc",
  "toolUseResult": {
    "query": "mimic-video tau_v=1 best performance SIMPLER autonomous policy Figure 5 per-task oracle intermediate noise 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RRgBFSRrJKdJzReXJqj8ag",
        "content": [
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs",
            "url": "https://arxiv.org/html/2512.15692v1"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs",
            "url": "https://mimic-video.github.io/"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | Papers | HyperAI",
            "url": "https://hyper.ai/en/papers/2512.15692"
          },
          {
            "title": "GitHub - mimic-video/mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs · GitHub",
            "url": "https://github.com/mimic-video/mimic-video"
          },
          {
            "title": "Mimic-Video: Video-Driven Robotic Control",
            "url": "https://www.emergentmind.com/topics/mimic-video"
          },
          {
            "title": "Mimic-Video: Efficient Robot Control Model | PDF | Applied Mathematics",
            "url": "https://www.scribd.com/document/968265710/4"
          },
          {
            "title": "GitHub - lucidrains/mimic-video: Implementation of Mimic-Video, Video-Action Models for SOTA Generalizable Robot Control Beyond VLAs · GitHub",
            "url": "https://github.com/lucidrains/mimic-video"
          },
          {
            "title": "[2512.15692] mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs",
            "url": "https://arxiv.org/abs/2512.15692"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs - YouTube",
            "url": "https://www.youtube.com/watch?v=_LkBFL5m1WU"
          },
          {
            "title": "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2512.15692"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query regarding mimic-video with the τ_v=1 parameter and SIMPLER benchmark performance.\n\nThe best autonomous policy performance in the SIMPLER experiments is achieved when stopping the video generation process early (at the highest noise level), with conditioning on a \"noisy\" visual plan yielding substantially better performance than allowing the video model to fully denoise its prediction.\n\nPerformance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies. More specifically, the best autonomous policy performance in SIMPLER experiments is achieved at the highest noise level τ_v = 1.\n\nOperating at τ_v = 1 requires only a single forward pass of the video backbone to generate conditioning features, resulting in both the highest average performance and the fastest inference speed.\n\nRegarding the explanation for this counterintuitive finding, the authors hypothesize that imperfect video generation introduces artifacts, and consequently, fully denoised video latents may diverge from the training distribution, presenting out-of-distribution conditioning to the action decoder.\n\nIn terms of overall performance on SIMPLER-Bridge, mimic-video with τ_v tuning achieves an average success rate of 56.3%, compared to 14.6% (OpenVLA) and 35.4% (π0.5-style VLA)."
    ],
    "durationSeconds": 6.661852399000025
  },
  "sourceToolAssistantUUID": "deaabb92-0788-476d-9428-796f5fce61d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-10T09:50:13.054Z_

```json
{
  "parentUuid": "c9d25d39-c9a7-4ec2-8133-f7d532b0ecdc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "befd0adf-b8d0-4d11-a2a6-b2cb96bd3a39",
  "timestamp": "2026-05-10T09:50:13.054Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "befd0adf-b8d0-4d11-a2a6-b2cb96bd3a39",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Assistant

_source line 41 · 2026-05-10T09:50:24.444Z_

<details><summary>Logged reasoning block</summary>

```text
The OA-WAM per-task numbers are verified in Table 1 of arXiv:2605.06481v1. The proposal was correct.

CKT-WAM (arXiv:2605.06247) is about parameter-efficient knowledge transfer between WAMs - orthogonal to CDR's approach. Not a competitor.

arXiv:2604.01414 is about vision-torque fusion for contact-aware manipulation - not related to tau_v routing.

The mimic-video findings are confirmed:
- τ_v=1 is the best fixed global autonomous policy performance in SIMPLER


- Performance improves at intermediate noise levels when using per-task oracles, and τ_v=1 needs only a single forward pass

Now I'm searching for recent papers on per-observation or per-task video noise routing in WAMs, and checking whether the robustness study comparing World Action Models to VLAs (arXiv:2603.22078) is relevant to this work. I should also look for any concurrent work on adaptive noise scheduling or per-task tau_v selection in WAMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "befd0adf-b8d0-4d11-a2a6-b2cb96bd3a39",
  "isSidechain": false,
  "requestId": "req_011CatgQj4EGuuULbw7AUmod",
  "type": "assistant",
  "uuid": "739dd70d-9b08-4264-9975-0762dd4614c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DFPvegCGotbXBN3pKfgRyn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 62262,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2348,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 433,
          "cache_read_input_tokens": 62262,
          "cache_creation_input_tokens": 2348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2348
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

_source line 42 · 2026-05-10T09:50:24.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0154t62siihsXirY8sgCVTPw`</summary>

```json
{
  "query": "per-task per-observation noise level selection world action model zero-shot routing 2026 arxiv manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "739dd70d-9b08-4264-9975-0762dd4614c8",
  "isSidechain": false,
  "requestId": "req_011CatgQj4EGuuULbw7AUmod",
  "type": "assistant",
  "uuid": "6b5e19c3-3831-425d-ac43-15fee1503540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DFPvegCGotbXBN3pKfgRyn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 62262,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2348,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 433,
          "cache_read_input_tokens": 62262,
          "cache_creation_input_tokens": 2348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2348
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

_source line 43 · 2026-05-10T09:50:24.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016JrYEbu9QrVCMK2Tx5hdaM`</summary>

```json
{
  "query": "\"Fast-WAM\" SIMPLER SimplerEnv evaluation results 2026 arXiv 2603.16666"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b5e19c3-3831-425d-ac43-15fee1503540",
  "isSidechain": false,
  "requestId": "req_011CatgQj4EGuuULbw7AUmod",
  "type": "assistant",
  "uuid": "c4ab82c6-ab6d-46a1-8ad6-0b3684e46913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DFPvegCGotbXBN3pKfgRyn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 62262,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2348,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 433,
          "cache_read_input_tokens": 62262,
          "cache_creation_input_tokens": 2348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2348
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

_source line 44 · 2026-05-10T09:50:30.584Z_

<details><summary>↩ Tool result · `toolu_016JrYEbu9QrVCMK2Tx5hdaM`</summary>

```text
Web search results for query: ""Fast-WAM" SIMPLER SimplerEnv evaluation results 2026 arXiv 2603.16666"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Rethinking Test-Time Imagination","url":"https://www.emergentmind.com/papers/2603.16666"},{"title":"GitHub - simpler-env/SimplerEnv: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) (CoRL 2024) · GitHub","url":"https://github.com/simpler-env/SimplerEnv"},{"title":"Evaluating Real-World Robot Manipulation Policies in Simulation","url":"https://simpler-env.github.io/"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"Evaluating Real-World Robot Manipulation Policies in Simulation","url":"https://arxiv.org/html/2405.05941v1"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## Fast-WAM Paper Overview

Fast-WAM is a World Action Model (WAM) architecture that retains video co-training during training but skips future prediction at test time.

**Main Research Question:**
The paper investigates whether explicit future imagination is necessary for strong action performance, or whether WAM benefits come primarily from video modeling during training, as most existing WAMs follow an imagine-then-execute paradigm that incurs substantial test-time latency from iterative video denoising.

**Publication Details:**
The paper (arXiv:2603.16666) was submitted on March 17, 2026, and last revised on March 23, 2026, with authors Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao.

**Evaluation:**
The search results indicate that Fast-WAM has been evaluated on benchmarks including SimplerEnv and other robustness tests, though the specific detailed evaluation results from the paper are not fully shown in these search excerpts. You can access the full paper and detailed results at the arXiv page: https://arxiv.org/abs/2603.16666

There's also an official GitHub repository with the codebase available at: https://github.com/yuantianyuan01/FastWAM


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4ab82c6-ab6d-46a1-8ad6-0b3684e46913",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "d2027ed4-4131-443a-8dff-5fa1e3893907",
  "toolUseResult": {
    "query": "\"Fast-WAM\" SIMPLER SimplerEnv evaluation results 2026 arXiv 2603.16666",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vi76vF4mEZPPndZK9mXcmx",
        "content": [
          {
            "title": "[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://arxiv.org/abs/2603.16666"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://arxiv.org/html/2603.16666v1"
          },
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?…",
            "url": "https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"
          },
          {
            "title": "GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub",
            "url": "https://github.com/yuantianyuan01/FastWAM"
          },
          {
            "title": "Fast-WAM: Rethinking Test-Time Imagination",
            "url": "https://www.emergentmind.com/papers/2603.16666"
          },
          {
            "title": "GitHub - simpler-env/SimplerEnv: Evaluating and reproducing real-world robot manipulation policies (e.g., RT-1, RT-1-X, Octo) in simulation under common setups (e.g., Google Robot, WidowX+Bridge) (CoRL 2024) · GitHub",
            "url": "https://github.com/simpler-env/SimplerEnv"
          },
          {
            "title": "Evaluating Real-World Robot Manipulation Policies in Simulation",
            "url": "https://simpler-env.github.io/"
          },
          {
            "title": "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models",
            "url": "https://arxiv.org/html/2605.06247v1"
          },
          {
            "title": "Evaluating Real-World Robot Manipulation Policies in Simulation",
            "url": "https://arxiv.org/html/2405.05941v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\n## Fast-WAM Paper Overview\n\nFast-WAM is a World Action Model (WAM) architecture that retains video co-training during training but skips future prediction at test time.\n\n**Main Research Question:**\nThe paper investigates whether explicit future imagination is necessary for strong action performance, or whether WAM benefits come primarily from video modeling during training, as most existing WAMs follow an imagine-then-execute paradigm that incurs substantial test-time latency from iterative video denoising.\n\n**Publication Details:**\nThe paper (arXiv:2603.16666) was submitted on March 17, 2026, and last revised on March 23, 2026, with authors Tianyuan Yuan, Zibin Dong, Yicheng Liu, and Hang Zhao.\n\n**Evaluation:**\nThe search results indicate that Fast-WAM has been evaluated on benchmarks including SimplerEnv and other robustness tests, though the specific detailed evaluation results from the paper are not fully shown in these search excerpts. You can access the full paper and detailed results at the arXiv page: https://arxiv.org/abs/2603.16666\n\nThere's also an official GitHub repository with the codebase available at: https://github.com/yuantianyuan01/FastWAM"
    ],
    "durationSeconds": 6.117764693999983
  },
  "sourceToolAssistantUUID": "c4ab82c6-ab6d-46a1-8ad6-0b3684e46913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T09:50:31.741Z_

<details><summary>↩ Tool result · `toolu_0154t62siihsXirY8sgCVTPw`</summary>

```text
Web search results for query: "per-task per-observation noise level selection world action model zero-shot routing 2026 arxiv manipulation"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"[2602.15922] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922"},{"title":"World Action Models are Zero-shot Policies (arXiv:2602.15922v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2602.15922"},{"title":"(PDF) World Action Models are Zero-shot Policies","url":"https://www.researchgate.net/publication/400930242_World_Action_Models_are_Zero-shot_Policies"},{"title":"[2602.15922v1] World Action Models are Zero-shot Policies","url":"https://arxiv.org/abs/2602.15922v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Noisy Zero-Shot Coordination: Breaking The Common Knowledge Assumption In Zero-Shot Coordination Games","url":"https://arxiv.org/html/2411.04976v1"},{"title":"World Action Models are Zero-shot Policies | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.15922"}]

Based on the search results, I found several recent arXiv papers from 2026 related to world action models and robot manipulation with zero-shot capabilities:

## Key Papers Found:

1. **"World Action Models are Zero-shot Policies"** (arXiv:2602.15922, February 2026)
   DreamZero jointly models video and action, learning diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations, resulting in over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments.

   DreamZero-Flash uses decoupled noise schedules, biasing video toward high-noise states via a Beta distribution while keeping action noise uniform, training the model to predict clean actions from noisy visual context.

2. **"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"** (arXiv:2605.06481, May 2026)
   OA-WAM sets a new SOTA on the geometric LIBERO-Plus axes, and provides zero-shot evaluation on the LIBERO-Plus robustness benchmark, training on standard LIBERO only.

3. **"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising"** (arXiv:2604.26694)
   This paper discusses X-WAM, a unified 4D world action model featuring noise scheduling approaches for joint video and action prediction.

These papers align with your search query focusing on noise level selection, world action models, zero-shot routing, and robot manipulation tasks from 2026 arXiv submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b5e19c3-3831-425d-ac43-15fee1503540",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "a85353ac-87ab-48c0-bf02-ecd2ec4e5f9f",
  "toolUseResult": {
    "query": "per-task per-observation noise level selection world action model zero-shot routing 2026 arxiv manipulation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GMeNpQBWEUhfyMxHxYRbY1",
        "content": [
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
          },
          {
            "title": "World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/html/2602.15922v1"
          },
          {
            "title": "[2602.15922] World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/abs/2602.15922"
          },
          {
            "title": "World Action Models are Zero-shot Policies (arXiv:2602.15922v1) - ScienceStack",
            "url": "https://www.sciencestack.ai/paper/2602.15922"
          },
          {
            "title": "(PDF) World Action Models are Zero-shot Policies",
            "url": "https://www.researchgate.net/publication/400930242_World_Action_Models_are_Zero-shot_Policies"
          },
          {
            "title": "[2602.15922v1] World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/abs/2602.15922v1"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "Noisy Zero-Shot Coordination: Breaking The Common Knowledge Assumption In Zero-Shot Coordination Games",
            "url": "https://arxiv.org/html/2411.04976v1"
          },
          {
            "title": "World Action Models are Zero-shot Policies | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2602.15922"
          }
        ]
      },
      "Based on the search results, I found several recent arXiv papers from 2026 related to world action models and robot manipulation with zero-shot capabilities:\n\n## Key Papers Found:\n\n1. **\"World Action Models are Zero-shot Policies\"** (arXiv:2602.15922, February 2026)\n   DreamZero jointly models video and action, learning diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations, resulting in over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments.\n\n   DreamZero-Flash uses decoupled noise schedules, biasing video toward high-noise states via a Beta distribution while keeping action noise uniform, training the model to predict clean actions from noisy visual context.\n\n2. **\"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation\"** (arXiv:2605.06481, May 2026)\n   OA-WAM sets a new SOTA on the geometric LIBERO-Plus axes, and provides zero-shot evaluation on the LIBERO-Plus robustness benchmark, training on standard LIBERO only.\n\n3. **\"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising\"** (arXiv:2604.26694)\n   This paper discusses X-WAM, a unified 4D world action model featuring noise scheduling approaches for joint video and action prediction.\n\nThese papers align with your search query focusing on noise level selection, world action models, zero-shot routing, and robot manipulation tasks from 2026 arXiv submissions."
    ],
    "durationSeconds": 7.281970456999988
  },
  "sourceToolAssistantUUID": "6b5e19c3-3831-425d-ac43-15fee1503540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T09:51:04.306Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I've confirmed:
1. OA-WAM per-task numbers verified ✓
2. Fast-WAM does not appear to evaluate on SIMPLER/SimplerEnv - only LIBERO and RoboTwin ✓ (as the proposal claims)
3. No new directly competing work on per-task/per-observation τ_v routing found

Now let me also verify a key claim about the statistical power analysis. The proposal says "K=50 provides ~80% power to detect a 7.5pp improvement over 46.9% baseline at α=0.05 (normal approximation to binomial: σ≈√(0.469×0.531/50)≈0.071 per task; standardized effect size ≈1.06)."


I need to reconsider this more carefully—the proposal is computing per-task power using a normal approximation, but the actual experiment uses a paired t-test across just 4 task pairs, which gives only 3 degrees of freedom and a much higher critical value for detecting effects at α=0.05.

Now I'm looking at what effect size is actually plausible. The claim requires ≥7.5pp improvement, but I need to estimate the mean and variability across tasks. From the mimic-video results, if CDR captures around 80% of the per-task oracle gains, I'd expect improvements ranging from near 0pp on some tasks to around 13pp on others, which means the mean difference would be substantially lower than the claimed threshold and the variance across tasks is quite high. I'm calculating the t-statistic for the paired test, which comes out to about 2.17, but that's just barely below the critical value of 2.353 for a one-sided test with 3 degrees of freedom. To properly assess power, I need to use the non-centrality parameter instead of just comparing the raw t-statistic to the critical value.

The non-centrality parameter λ equals the effect size times the square root of sample size, which gives me 2.18. Using a non-central t-distribution with 3 degrees of freedom and this non-centrality parameter, the probability of exceeding the critical value is roughly 40-60% — nowhere near the 80% power the proposal claims. The issue is that the proposal appears to be calculating power per-task rather than accounting for the actual sample size constraints.

So the core problem is conflating per-task power (with n=50 rollouts) against across-task power (with only n=4 tasks). While the proposal correctly identifies that 50 rollouts gives solid per-task estimates and does report valid Wilson confidence intervals, the claimed 80% power for the paired t-test is statistically incorrect. That said, this isn't unusual — many papers in this space skip formal statistical testing entirely, so the evaluation design itself is reasonable even if the power calculation is off. Now I want to search for whether any prior work has done a similar characterization of the manipulation phase analysis or τ_v estimation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a85353ac-87ab-48c0-bf02-ecd2ec4e5f9f",
  "isSidechain": false,
  "requestId": "req_011CatgS6w8yzfk94jgixCPx",
  "type": "assistant",
  "uuid": "e977528a-68e4-4c3f-9258-793d191b4278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013cmKpv7X8r6LuBsWpubmhH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 64610,
      "output_tokens": 1525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 907,
          "output_tokens": 1525,
          "cache_read_input_tokens": 64610,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 47 · 2026-05-10T09:51:04.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VTPNr771huGF2HvvEE15rp`</summary>

```json
{
  "query": "manipulation phase analysis grasp approach transport video denoising timestep optimal robot learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e977528a-68e4-4c3f-9258-793d191b4278",
  "isSidechain": false,
  "requestId": "req_011CatgS6w8yzfk94jgixCPx",
  "type": "assistant",
  "uuid": "0cc3506d-c297-44ee-8fdb-724b9cfdbfc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013cmKpv7X8r6LuBsWpubmhH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 64610,
      "output_tokens": 1525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 907,
          "output_tokens": 1525,
          "cache_read_input_tokens": 64610,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 48 · 2026-05-10T09:51:04.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0199zPRV8BwaJBkgrEw1sWbu`</summary>

```json
{
  "query": "LingBot-VA causal world modeling arXiv 2601.21998 RSS 2026 noisy history augmentation LIBERO SIMPLER results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc3506d-c297-44ee-8fdb-724b9cfdbfc6",
  "isSidechain": false,
  "requestId": "req_011CatgS6w8yzfk94jgixCPx",
  "type": "assistant",
  "uuid": "01ecf258-14f0-47a6-b9b1-6d6cbad7f3fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013cmKpv7X8r6LuBsWpubmhH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 64610,
      "output_tokens": 1525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 907,
          "output_tokens": 1525,
          "cache_read_input_tokens": 64610,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 49 · 2026-05-10T09:51:13.741Z_

<details><summary>↩ Tool result · `toolu_01VTPNr771huGF2HvvEE15rp`</summary>

```text
Web search results for query: "manipulation phase analysis grasp approach transport video denoising timestep optimal robot learning 2026"

Links: [{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Diffusion Policy for Robot Learning: What It Is and How to Use It | SVRC","url":"https://www.roboticscenter.ai/blog/diffusion-policy-robots"},{"title":"An overview of learning-based dexterous grasping: recent advances and future directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11262-2"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"DiffusionRL: Efficient Training of Diffusion Policies for Robotic Grasping Using RL-Adapted Large-Scale Datasets","url":"https://arxiv.org/html/2505.18876"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2503.03464v1"},{"title":"GitHub - RayYoh/OCRM_survey: A Survey of Embodied Learning for Object-Centric Robotic Manipulation","url":"https://github.com/RayYoh/OCRM_survey"},{"title":"ReinFlow: Fine-tuning Flow Matching Policy with Online ...","url":"https://nicsefc.ee.tsinghua.edu.cn//nics_file/pdf/09dbaac9-e1ab-4e18-abf2-99ec82476290.pdf"}]

Based on the web search results, I found several highly relevant papers and resources related to your query about robot learning, diffusion models, and manipulation tasks. Here are the key findings:

## Diffusion Models for Robotic Manipulation

Grasps are generated using diffusion models with a single backward pass to generate grasp poses. Diffusion Policy is a class of robot control policies based on denoising diffusion probabilistic models, where the "image" being generated is a sequence of robot actions (a trajectory), starting from pure Gaussian noise in action space and iteratively denoising it conditioned on the current visual observation and robot state.

## Video Denoising and Timestep Optimization

To incorporate the reward term during sampling, a regression model is trained to predict the return at each denoising time step. In DDPM (Ho et al., 2020), a noise prediction network conditioned on the noise scale is trained, and new points are generated by sampling Gaussian noise and iteratively denoising the samples.

## Manipulation Phase Analysis and Grasp Approach

Manipulation tasks like picking a block off a table involve multiple valid approach angles, grasp poses, and pre-grasp configurations. SceneDiffuser is proposed as a conditional generative model based on the diffusion process that eliminates discrepancies and provides a unified framework for scene-conditioned generation, optimization, and planning, learning a diffusion model for scene-conditioned generation during training.

## Transport and Recent 2026 Developments

The search results include recent 2026 papers on humanoid robot learning and manipulation. Recent work includes SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning, demonstrating advances in object transport tasks for robotic systems.

The field shows active research in combining diffusion models with reinforcement learning and optimal control strategies for efficient robot manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cc3506d-c297-44ee-8fdb-724b9cfdbfc6",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "19ec30cd-0192-4cb0-883e-4f661113c922",
  "toolUseResult": {
    "query": "manipulation phase analysis grasp approach transport video denoising timestep optimal robot learning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SyP8mA4FCRnaq4Xedi1Urd",
        "content": [
          {
            "title": "Frontiers | Diffusion models for robotic manipulation: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Diffusion Policy for Robot Learning: What It Is and How to Use It | SVRC",
            "url": "https://www.roboticscenter.ai/blog/diffusion-policy-robots"
          },
          {
            "title": "An overview of learning-based dexterous grasping: recent advances and future directions | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11262-2"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "DiffusionRL: Efficient Training of Diffusion Policies for Robotic Grasping Using RL-Adapted Large-Scale Datasets",
            "url": "https://arxiv.org/html/2505.18876"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          },
          {
            "title": "Generative Artificial Intelligence in Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2503.03464v1"
          },
          {
            "title": "GitHub - RayYoh/OCRM_survey: A Survey of Embodied Learning for Object-Centric Robotic Manipulation",
            "url": "https://github.com/RayYoh/OCRM_survey"
          },
          {
            "title": "ReinFlow: Fine-tuning Flow Matching Policy with Online ...",
            "url": "https://nicsefc.ee.tsinghua.edu.cn//nics_file/pdf/09dbaac9-e1ab-4e18-abf2-99ec82476290.pdf"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers and resources related to your query about robot learning, diffusion models, and manipulation tasks. Here are the key findings:\n\n## Diffusion Models for Robotic Manipulation\n\nGrasps are generated using diffusion models with a single backward pass to generate grasp poses. Diffusion Policy is a class of robot control policies based on denoising diffusion probabilistic models, where the \"image\" being generated is a sequence of robot actions (a trajectory), starting from pure Gaussian noise in action space and iteratively denoising it conditioned on the current visual observation and robot state.\n\n## Video Denoising and Timestep Optimization\n\nTo incorporate the reward term during sampling, a regression model is trained to predict the return at each denoising time step. In DDPM (Ho et al., 2020), a noise prediction network conditioned on the noise scale is trained, and new points are generated by sampling Gaussian noise and iteratively denoising the samples.\n\n## Manipulation Phase Analysis and Grasp Approach\n\nManipulation tasks like picking a block off a table involve multiple valid approach angles, grasp poses, and pre-grasp configurations. SceneDiffuser is proposed as a conditional generative model based on the diffusion process that eliminates discrepancies and provides a unified framework for scene-conditioned generation, optimization, and planning, learning a diffusion model for scene-conditioned generation during training.\n\n## Transport and Recent 2026 Developments\n\nThe search results include recent 2026 papers on humanoid robot learning and manipulation. Recent work includes SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning, demonstrating advances in object transport tasks for robotic systems.\n\nThe field shows active research in combining diffusion models with reinforcement learning and optimal control strategies for efficient robot manipulation."
    ],
    "durationSeconds": 9.415405241
  },
  "sourceToolAssistantUUID": "0cc3506d-c297-44ee-8fdb-724b9cfdbfc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "19ec30cd-0192-4cb0-883e-4f661113c922",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Tool result

_source line 52 · 2026-05-10T09:51:17.580Z_

<details><summary>↩ Tool result · `toolu_0199zPRV8BwaJBkgrEw1sWbu`</summary>

```text
Web search results for query: "LingBot-VA causal world modeling arXiv 2601.21998 RSS 2026 noisy history augmentation LIBERO SIMPLER results"

Links: [{"title":"[2601.21998] Causal World Modeling for Robot Control","url":"https://arxiv.org/abs/2601.21998"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"LingBot-VA: Causal World Modeling for Robot Control","url":"https://github.com/robbyant/lingbot-va"},{"title":"Causal World Modeling for Robot Control Lin Li∗ Qihang Zhang∗† Yiming Luo∗","url":"https://arxiv.org/pdf/2601.21998"},{"title":"Paper page - Causal World Modeling for Robot Control","url":"https://huggingface.co/papers/2601.21998"},{"title":"robbyant/lingbot-va-base · Hugging Face","url":"https://huggingface.co/robbyant/lingbot-va-base"},{"title":"Causal World Modeling for Robot Control (Jan 2026) - YouTube","url":"https://www.youtube.com/watch?v=8Q_js9VMT8Q"},{"title":"Causal World Modeling for Robot Control | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.21998v1"},{"title":"GitHub - PRB-R-NINE-T/lingbot-va-fork: Causal video-action world model for generalist robot control","url":"https://github.com/PRB-R-NINE-T/lingbot-va-fork"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"}]

I found information about the LingBot-VA paper. Let me search for more specific details about the LIBERO and SIMPLER benchmarks and the noisy history augmentation results mentioned in your query.

Links: [{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"Lingbot-Va Achieves Simultaneous Frame Prediction","url":"https://quantumzeitgeist.com/prediction-lingbot-achieves-simultaneous-frame-policy/"},{"title":"Robots Learn to Predict the Future with LingBot-VA: A Leap in Autonomous Control Technology | NenPower","url":"https://nenpower.com/blog/robots-learn-to-predict-the-future-with-lingbot-va-a-leap-in-autonomous-control-technology/"},{"title":"Embodied World Models for Robotics Training: How LingBot-VA & Cosmos Policy Enable Robot Reasoning | by Daniel Ikechukwu | Medium","url":"https://medium.com/@creed_1732/embodied-world-models-for-robotics-training-how-lingbot-va-cosmos-policy-enable-robot-reasoning-c0c152625dfe"},{"title":"World Models Enter the Physical World: Antlingbot Opens Source LingBot-VA, Allowing Robots to Think Before Acting","url":"https://news.aibase.com/news/25103"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"Ant Group Releases LingBot-VLA, A Vision Language Action Foundation Model For Real World Robot Manipulation - MarkTechPost","url":"https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/"},{"title":"Post-train on LIBERO Benchmark · Issue #30 · Robbyant/lingbot-va","url":"https://github.com/Robbyant/lingbot-va/issues/30"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"LingBot-VA: Multilingual Virtual Assistant","url":"https://www.emergentmind.com/topics/lingbot-va"}]

Based on my web search results, I have found comprehensive information about LingBot-VA and can provide you with the details you requested:

## LingBot-VA: Causal World Modeling for Robot Control

LingBot-VA is an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. The model features three carefully crafted designs: (1) a shared latent space, integrating vision and action tokens, driven by a Mixture-of-Transformers (MoT) architecture, (2) a closed-loop rollout mechanism, allowing for ongoing acquisition of environmental feedback with ground-truth observations, (3) an asynchronous inference pipeline, parallelizing action prediction and motor execution to support efficient control.

### Noisy History Augmentation

Researchers introduced Noisy History Augmentation, a training scheme enabling partial denoising during inference, and an asynchronous coordination pipeline that overlaps computation with execution. LingBot-VA introduced a persistent mechanism based on memory cache and noise history enhancement strategy, allowing stable and precise action instructions to be output with fewer generation steps during inference.

### RSS 2026 Publication

The paper was published as an RSS 2026 contribution, with post-training and inference code for the LIBERO dataset released on 2026-04-08 and post-training code and dataset released on 2026-02-17.

### LIBERO and SIMPLER Benchmark Results

On LIBERO benchmarks, LingBot-VA achieves new state-of-the-art on LIBERO-Object (99.6%), LIBERO-Long (98.5%), LIBERO-Spatial (98.5%), and overall average (98.5%). Evaluation on benchmarks like LIBERO and RoboTwin demonstrates superior performance, achieving a progress score of 79.2 and a success rate of 65.4, significantly exceeding previous state-of-the-art methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01ecf258-14f0-47a6-b9b1-6d6cbad7f3fa",
  "isSidechain": false,
  "promptId": "ec1048d8-c34d-43d0-993b-a32d554ab02b",
  "type": "user",
  "uuid": "ea4d798d-5f73-4340-9367-ced772585713",
  "toolUseResult": {
    "query": "LingBot-VA causal world modeling arXiv 2601.21998 RSS 2026 noisy history augmentation LIBERO SIMPLER results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F4QJYPhXna8hcxgaXkegWo",
        "content": [
          {
            "title": "[2601.21998] Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/abs/2601.21998"
          },
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v1"
          },
          {
            "title": "LingBot-VA: Causal World Modeling for Robot Control",
            "url": "https://github.com/robbyant/lingbot-va"
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
            "title": "robbyant/lingbot-va-base · Hugging Face",
            "url": "https://huggingface.co/robbyant/lingbot-va-base"
          },
          {
            "title": "Causal World Modeling for Robot Control (Jan 2026) - YouTube",
            "url": "https://www.youtube.com/watch?v=8Q_js9VMT8Q"
          },
          {
            "title": "Causal World Modeling for Robot Control | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2601.21998v1"
          },
          {
            "title": "GitHub - PRB-R-NINE-T/lingbot-va-fork: Causal video-action world model for generalist robot control",
            "url": "https://github.com/PRB-R-NINE-T/lingbot-va-fork"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          }
        ]
      },
      "I found information about the LingBot-VA paper. Let me search for more specific details about the LIBERO and SIMPLER benchmarks and the noisy history augmentation results mentioned in your query.",
      {
        "tool_use_id": "srvtoolu_01Bv6xQqdbu5yFx7vgi73Cdj",
        "content": [
          {
            "title": "GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub",
            "url": "https://github.com/robbyant/lingbot-va"
          },
          {
            "title": "Lingbot-Va Achieves Simultaneous Frame Prediction",
            "url": "https://quantumzeitgeist.com/prediction-lingbot-achieves-simultaneous-frame-policy/"
          },
          {
            "title": "Robots Learn to Predict the Future with LingBot-VA: A Leap in Autonomous Control Technology | NenPower",
            "url": "https://nenpower.com/blog/robots-learn-to-predict-the-future-with-lingbot-va-a-leap-in-autonomous-control-technology/"
          },
          {
            "title": "Embodied World Models for Robotics Training: How LingBot-VA & Cosmos Policy Enable Robot Reasoning | by Daniel Ikechukwu | Medium",
            "url": "https://medium.com/@creed_1732/embodied-world-models-for-robotics-training-how-lingbot-va-cosmos-policy-enable-robot-reasoning-c0c152625dfe"
          },
          {
            "title": "World Models Enter the Physical World: Antlingbot Opens Source LingBot-VA, Allowing Robots to Think Before Acting",
            "url": "https://news.aibase.com/news/25103"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "Ant Group Releases LingBot-VLA, A Vision Language Action Foundation Model For Real World Robot Manipulation - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/"
          },
          {
            "title": "Post-train on LIBERO Benchmark · Issue #30 · Robbyant/lingbot-va",
            "url": "https://github.com/Robbyant/lingbot-va/issues/30"
          },
          {
            "title": "Causal World Modeling for Robot Control",
            "url": "https://arxiv.org/html/2601.21998v1"
          },
          {
            "title": "LingBot-VA: Multilingual Virtual Assistant",
            "url": "https://www.emergentmind.com/topics/lingbot-va"
          }
        ]
      },
      "Based on my web search results, I have found comprehensive information about LingBot-VA and can provide you with the details you requested:\n\n## LingBot-VA: Causal World Modeling for Robot Control\n\nLingBot-VA is an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. The model features three carefully crafted designs: (1) a shared latent space, integrating vision and action tokens, driven by a Mixture-of-Transformers (MoT) architecture, (2) a closed-loop rollout mechanism, allowing for ongoing acquisition of environmental feedback with ground-truth observations, (3) an asynchronous inference pipeline, parallelizing action prediction and motor execution to support efficient control.\n\n### Noisy History Augmentation\n\nResearchers introduced Noisy History Augmentation, a training scheme enabling partial denoising during inference, and an asynchronous coordination pipeline that overlaps computation with execution. LingBot-VA introduced a persistent mechanism based on memory cache and noise history enhancement strategy, allowing stable and precise action instructions to be output with fewer generation steps during inference.\n\n### RSS 2026 Publication\n\nThe paper was published as an RSS 2026 contribution, with post-training and inference code for the LIBERO dataset released on 2026-04-08 and post-training code and dataset released on 2026-02-17.\n\n### LIBERO and SIMPLER Benchmark Results\n\nOn LIBERO benchmarks, LingBot-VA achieves new state-of-the-art on LIBERO-Object (99.6%), LIBERO-Long (98.5%), LIBERO-Spatial (98.5%), and overall average (98.5%). Evaluation on benchmarks like LIBERO and RoboTwin demonstrates superior performance, achieving a progress score of 79.2 and a success rate of 65.4, significantly exceeding previous state-of-the-art methods."
    ],
    "durationSeconds": 13.247619793999998
  },
  "sourceToolAssistantUUID": "01ecf258-14f0-47a6-b9b1-6d6cbad7f3fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-10T09:52:27.412Z_

<details><summary>Logged reasoning block</summary>

```text
LingBot-VA results confirmed: 98.5% LIBERO, as the proposal states. No SIMPLER benchmark results found for LingBot-VA (which aligns with the proposal's claims that CDR's Pareto comparison on SIMPLER-Bridge is primarily against τ_v=1).

Key verification findings so far:
1. ✓ OA-WAM Table 1 per-task numbers verified: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%, Average 79.3%, Visual Matching protocol


2. ✓ Fast-WAM doesn't evaluate on SIMPLER/SimplerEnv
3. ✓ LingBot-VA achieves 98.5% on LIBERO, confirmed for RSS 2026
4. ✓ mimic-video's τ_v=1 represents the strongest fixed autonomous policy baseline on SIMPLER
5. ✓ No other work implements per-task or per-observation τ_v routing
6. ✓ CKT-WAM addresses knowledge transfer orthogonally, not noise routing
7. ✓ No significant concurrent work appears to have been overlooked

Now examining what remaining issues need attention.

There's a flaw in the statistical power analysis—the proposal claims K=50 provides adequate power for the paired t-test, but this conflates two different things. With K=50 rollouts per task, I get tight per-task estimates, but the paired t-test across just 4 tasks (df=3) depends on between-task variance, not within-task sample size. The power calculation needs to account for how much the CDR improvement varies across the four tasks, not just the aggregate gain.

Working through the actual numbers: if the mean gain is 7.5pp but varies substantially across tasks (Stack Blocks and Carrot gain ~13pp, Spoon gains ~3pp, Eggplant gains 0pp), the standard deviation of differences is around 6pp. This gives a t-statistic of 2.5 with 3 degrees of freedom, which only achieves 50-60% power—well below the claimed 80%. The proposal's calculation is really just measuring within-task precision, not the statistical power of the across-task comparison.

That said, this isn't a dealbreaker because the proposal reports Wilson confidence intervals for each task individually, evaluates 1,200 total rollouts which is reasonable, and presents both per-task and aggregate results so reviewers can assess the breakdown themselves. Plus, formal statistical testing isn't standard practice in robotics papers anyway.

Looking at the other issues: CKT-WAM and EA-WM are recent May 2026 papers on world action models that CDR doesn't cite, but they seem orthogonal to CDR's approach rather than direct competitors. And then there's the robustness study paper comparing world action models to VLMs—

that one could actually be relevant to CDR's claims about τ_v's role in robustness, so worth examining.

The deeper structural issue is whether the Phase 1 assumption holds up: using ground-truth demo actions to compute τ_v*(f) as a proxy for closed-loop task success is still fundamentally an assumption. The proposal mitigates this by including failed trajectory states in the rollout distribution, but the core question remains—does per-frame action error actually correlate with per-task success in closed-loop execution? The proposal acknowledges this but it's still an empirical bet.

On novelty and impact, the scores are coming in lower than needed. The novelty is incremental over mimic-video's variable-τ_v approach with just a 2-layer MLP router, and while the empirical study is the first of its kind, it's limited to a specific model family. Impact-wise, the deployment calibration savings are real but modest, the absolute performance still trails SOTA, and the WAM track itself is highly competitive. Averaging these out puts me below the 4.0 threshold needed to pass.

Despite eight rounds of refinement, the proposal has made genuine progress—verified the OA-WAM numbers, added statistical rigor, quantified deployment savings, clarified the empirical scope, restructured the abstract, and fixed the DiT4DiT issue. But the fundamental limitations on novelty and impact remain.

The statistical power calculation needs correction—it's conflating within-task precision with across-task power for the paired t-test—and there are a couple of May 2026 papers that should be cited, though they're orthogonal to the work. The real question is whether these fixes push this to a pass or if it stays at revise given the inherent ceiling on what the approach can contribute.

Looking at the scoring breakdown, I'm at 3.5/5 average, which falls short of the 4.0 threshold. The novelty and impact are both capped at 3 because while the empirical characterization of which phases need τ_v < 1 is genuinely novel and the zero-shot router is practical, the overall contribution feels modest compared to other WAM papers at CoRL. With only one round left, I need to decide if fixing the statistical issue alone is enough or if the fundamental limitations mean this should stay at revise. calculation error (fixable)
2. Novelty ceiling (inherent to approach, not easily fixable)
3. Impact ceiling (inherent to approach)

If I issue a "revise" for Round 9, Round 10 would be forced to either "pass" or "fail." At that point:
- If the statistical issue is fixed: novelty=3, feasibility=4, clarity=4, impact=3 → avg 3.5 → fail
- But CoRL does accept papers in this quality range (not every CoRL paper is 5/5)

Actually, I need to be more nuanced. The question isn't whether this would average exactly 4.0/5.0 in my abstract scoring - it's whether this would be competitive at CoRL 2026. And CoRL 2026's WAM track is specifically identified as "high competition but high reward."

Let me reconsider the actual competitive landscape: CoRL 2026 accepts roughly 22% of submissions, and the WAM track is particularly hot. Looking at what's already out there—OA-WAM with its 7B architecture and slot decomposition, DiT4DiT combining video and action modeling, MotuBrain's unified approach—CDR's contribution of an empirical study plus a 2-layer MLP router built on mimic-video feels incremental. The performance gap is stark: 56.3% on SIMPLER-Bridge versus OA-WAM's 79.3%, and that's a significant disadvantage when competing for limited spots.

My honest take: this paper would likely receive borderline scores (3s and maybe one 4) from reviewers, which typically results in rejection at a top venue like CoRL. The statistical power issue is fixable, but the fundamental novelty and impact limitations aren't. I should recommend "revise" for Round 9 to address the statistical concern, but I need to be realistic about the ceiling here.

For Round 10, if it's still "revise," I'm forced to make a final call between "pass" and "fail." Given the constraints, I'm leaning toward "fail" unless the revision substantially strengthens the empirical findings or novelty argument.

Now I'm scoring the paper across dimensions: novelty sits around 3/5 since the per-phase τ_v* characterization is genuinely new, but the architectural contribution is minimal—just a frozen checkpoint with a 2-layer MLP bolted on top, and the insights are fairly narrow to this one family of methods.

Feasibility looks solid at 4/5 with clear gates and realistic timelines, and the writing has improved significantly to 4/5 after multiple rounds. Impact is the real constraint at 3/5—the deployment gains are real but incremental, performance lags behind existing work, and this reads as a competent empirical study rather than a field-advancing contribution.

Averaging those scores puts me at 3.5/5, which falls short of the 4.0 bar. The statistical power issue at the 4-task level remains the most glaring problem—it undermines confidence in the main claims, and that's what I need to flag in my verdict.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea4d798d-5f73-4340-9367-ced772585713",
  "isSidechain": false,
  "requestId": "req_011CatgVUtpomdUxFJsujcYL",
  "type": "assistant",
  "uuid": "f81a9ba6-8b8f-40ff-abeb-475dc54054a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C7cnE47awaKnQfnGcU6u7P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5039,
      "cache_read_input_tokens": 65929,
      "output_tokens": 4776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4776,
          "cache_read_input_tokens": 65929,
          "cache_creation_input_tokens": 5039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5039
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

_source line 54 · 2026-05-10T09:53:05.253Z_

Now I have enough data for my independent assessment. Let me formulate the verdict.

Key verification results:
- **OA-WAM Table 1 per-task numbers**: Verified ✓ (Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%, avg 79.3%, Visual Matching protocol confirmed in arXiv:2605.06481v1)
- **Fast-WAM**: Confirmed no SIMPLER-Bridge evaluation ✓
- **LingBot-VA**: Confirmed RSS 2026, 98.5% LIBERO ✓
- **mimic-video τ_v=1 finding**: Confirmed as best fixed-global autonomous policy ✓
- **No competing per-task/per-observation τ_v routing paper found**: CDR's empirical study remains the first of its kind ✓
- **CKT-WAM, EA-WM (May 2026)**: Both are orthogonal, not competitors

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The Phase 1 empirical characterization of per-phase τ_v* across LIBERO-100 is genuinely the first such study, and the pre-registered P1 prediction adds scientific rigor. However, the deployment mechanism (2-layer MLP on CLIP + language embeddings) is architecturally trivial, and the contribution is scoped to a single model family (mimic-video) under a specific training regime, limiting generalizability claims."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Phase 0 gate, 80/20 held-out LIBERO validation gate, and MVS fallback are all well-specified; manual (115–135H) and auto-mode (150–175H) estimates are within the ≤200H constraint; the timeline is tight but the critical path is realistic given 8 H100s."
    },
    "clarity": {
      "score": 4,
      "rationale": "After eight rounds of revision, the proposal is exceptionally well-organized: mimic-video Figure 5 reconciliation is precise, Pareto framing is honest about modest compute savings when P1 is confirmed, DiT4DiT characterization is corrected, and related-work differentiation is thorough."
    },
    "impact": {
      "score": 3,
      "rationale": "The deployment calibration savings (10 rollouts → 0 per new task, ~2.5 robot-hours/task) are real and now concretely quantified, but the benefit is modest at typical fleet sizes; absolute performance (46.9%→~56.3% SIMPLER-Bridge) remains 23pp below OA-WAM (79.3%) with no path to closing that gap within CDR's post-hoc framing, making this a solid-but-not-competitive contribution in CoRL 2026's hottest WAM track."
    }
  },
  "issues": [
    "MODERATE — Statistical power calculation is internally inconsistent: The proposal claims 'K=50 provides ~80% power to detect a 7.5pp improvement at α=0.05 (σ≈0.071 per task, effect size≈1.06).' This computes within-task precision (n=50 rollouts give ±7pp estimates per task) and conflates it with across-task paired t-test power (which uses n=4 task pairs with df=3). A one-sided paired t-test with 4 pairs, expected mean difference ~7.5pp (driven by Stack Blocks +~13pp, Carrot +~13pp, Spoon +~3pp, Eggplant +0pp), and across-task SD of gains ≈6pp gives SE=6/√4=3, t≈2.5 vs critical value t(3,0.95)≈2.353—yielding ~50–60% power, not 80%. CoRL reviewers will catch this. Fix: either add more SIMPLER-Bridge tasks (unlikely given the benchmark has only 4), increase K substantially, or honestly report that the aggregate paired t-test has limited power (df=3) and emphasize per-task Wilson CIs as the primary inferential tool alongside the aggregate mean. Do not claim 80% power for the across-task test.",
    "MINOR — CKT-WAM (arXiv:2605.06247, May 2026) and EA-WM (arXiv:2605.06192, May 2026) are uncited. Both appear orthogonal (knowledge transfer between WAMs; event-aware kinematic-to-visual fields), but CoRL reviewers from those groups may notice their omission. One-sentence acknowledge in related work for each is sufficient.",
    "MINOR — The action-error proxy assumption (τ_v*(f) = argmin||a_{τ_v}(f) − a_GT(f)||₂ on demo states) as a surrogate for closed-loop success is still not explicitly defended beyond the non-expert rollout mitigation. The proposal correctly adds 50% non-expert rollout states, but does not address whether the action error metric itself has been validated as a predictor of per-phase success on any held-out task. This is a residual reviewer concern that could arise in rebuttal.",
    "FUNDAMENTAL — Novelty and impact are structurally capped at ~3/5 due to the approach's inherent constraints (post-hoc routing on one frozen checkpoint, 4-task primary evaluation, absolute performance 23pp below SOTA OA-WAM, 2-layer MLP router). In CoRL 2026's WAM track against OA-WAM, MotuBrain, DiT4DiT, and Being-H0.7, this paper competes as a focused empirical contribution rather than an architectural advance—an honest positioning that the proposal now adopts, but which limits the ceiling acceptance probability in the hottest track of the conference."
  ],
  "feedback": "CDR has resolved every critical, major, and most moderate issues across eight rounds. The OA-WAM per-task numbers are independently verified in Table 1 (arXiv:2605.06481v1). No competing per-observation or per-task τ_v routing paper exists—CDR's empirical study is still first. The one actionable fix before Round 10:\n\n**Fix (required, 20 minutes): Correct the statistical power claim.** Replace 'K=50 provides ~80% power' with: 'K=50 rollouts per task provides ±7pp precision on per-task success rate estimates (Wilson 95% CI); per-task CIs are the primary inferential tool. The aggregate one-sided paired t-test across 4 tasks has df=3 and approximately 50–60% power to detect the 7.5pp improvement target at α=0.05, given estimated across-task SD of CDR gains ≈6pp. We therefore report per-task results and aggregate mean ± SE, with significance as a secondary indicator.' This is an honest statistical statement that reviewers expect and will not penalize if stated plainly—what they will penalize is an inflated 80% power claim they can refute in 30 seconds.\n\nThe fundamental ceiling (novelty=3, impact=3) is not fixable by further revision—it is inherent to the post-hoc routing approach on a specific model family. Round 10 should acknowledge that if Phase 1 yields weak per-phase variation (<15% frames with τ_v*<0.9), the paper belongs at ICLR 2027 with expanded scope rather than CoRL 2026 as a borderline empirical contribution.",
  "reason": "All Round 8 issues resolved and independently verified; one moderate statistical power miscalculation remains fixable; fundamental novelty/impact ceiling (avg score ~3.5/5.0) reflects inherent constraints of post-hoc empirical routing on a sub-SOTA base model in CoRL 2026's most competitive track."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f81a9ba6-8b8f-40ff-abeb-475dc54054a0",
  "isSidechain": false,
  "requestId": "req_011CatgVUtpomdUxFJsujcYL",
  "type": "assistant",
  "uuid": "e5fec784-0698-41f4-b743-fa22a5a5ac26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C7cnE47awaKnQfnGcU6u7P",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5039,
      "cache_read_input_tokens": 65929,
      "output_tokens": 4776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4776,
          "cache_read_input_tokens": 65929,
          "cache_creation_input_tokens": 5039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5039
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e5fec784-0698-41f4-b743-fa22a5a5ac26",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e5fec784-0698-41f4-b743-fa22a5a5ac26",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective video activation for WAM deployment automation",
  "sessionId": "f75f2c79-032b-4734-882a-e5ef8515319c"
}
```

---
