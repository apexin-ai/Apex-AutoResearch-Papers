# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/d6a789c0-9c74-4575-85a9-802d261f7af3.jsonl`
- **Structured JSON:** [`652b19409a9ab8f4b00e.json`](../../sessions/65/652b19409a9ab8f4b00e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T05:41:38.188Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T05:41:38.188Z",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\nDirection：因为真实数据采样的时候会有很多噪声，比如收集时的冗余动作等，如何避免训练数据中的噪声影响vla的训练，可以使用一个经验池的形式来训练，借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选，再适当过滤掉一些低分数的冗余动作，如果是从一些底层理论角度提出了筛选方法 感觉不用真机也是可以接受的**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 1/10)\n{\n  \"title\": \"Adaptive Experience Replay with Policy-Driven Priorities for VLA\",\n  \"core_problem\": \"Can we replace static demonstration filtering with an online, adaptive experience replay mechanism during VLA training, where sampling priorities co-evolve with the policy?\",\n  \"opportunity\": \"Every existing demo curation method (SCIZOR, QoQ, RINSE, DataMIL, MI-based) operates as a static preprocessing step — score once, filter once, train once. This ignores that the policy's learning needs change during training: early on it needs diverse coverage; later it needs precise, high-quality transitions. Prioritized Experience Replay (PER) transformed RL training by adaptively focusing on high-TD-error transitions, but has never been adapted for imitation learning of VLA models. The key theoretical insight is that self-supervised TD errors in a goal-conditioned value function can serve as priority signals without rewards, creating a natural curriculum from easy/common transitions to rare/critical ones.\",\n  \"landscape\": \"Prioritized Experience Replay (Schaul et al. 2015) is foundational in RL but not adopted in imitation learning. SCIZOR (ICRA 2026) filters once before training, discarding 15-40% of data statically. GR-RL (Dec 2025) has a multi-stage pipeline (filter → train → RL) but the filtering stage is still static. Curriculum learning for robot IL exists (HRL with curriculum demos, adaptive difficulty) but focuses on task curriculum, not data-quality curriculum. SimpleVLA-RL (ICLR 2026) uses GRPO for VLA online RL but doesn't address demo quality during the SFT stage. The blog post analyzing 164 VLA papers at ICLR 2026 identifies data quality as a critical gap, noting that 'OXE is mostly low-quality data, yet we still lack good methods to quantify data quality.' Concurrent work update (May 2026): Demo-SCORE (RSS 2025) uses online rollout experience to curate demonstrations via binary success/failure classification, but requires expensive environment interaction and operates as a discrete filter-and-retrain cycle rather than continuous priority adaptation. ExpReS-VLA (arXiv 2025) applies prioritized replay buffers with cosine-similarity retrieval for VLA continual learning to prevent catastrophic forgetting, not for improving initial SFT data quality. Freshness-Aware PER (arXiv April 2026) is the first to apply PER to LLM/VLM training but exclusively targets RL post-training with reward signals, leaving the reward-free SFT regime unaddressed. CUPID (CoRL 2025) and QoQ (arXiv 2026) use influence functions for demo curation but remain static preprocessing methods. Prioritized Replay for RL Post-training (arXiv Jan 2026) proposes problem-level prioritization for LLM RL but does not handle demonstration-level priorities in imitation learning. No existing work combines TD-error-based adaptive prioritization with reward-free imitation learning for VLA SFT.\",\n  \"approach\": \"Train a lightweight goal-conditioned value function V(s, g) on the demonstration dataset using hindsight goal relabeling, producing TD errors without requiring any reward signal. During VLA SFT on OpenVLA-OFT (the current open-source SOTA for manipulation), maintain a prioritized replay buffer over the full demonstration dataset where each transition's sampling probability is proportional to its TD error magnitude — transitions with high TD error represent under-learned or critical state changes that the current policy finds surprising. Refresh priorities every K gradient steps by recomputing TD errors with the updated value function, creating a natural curriculum that shifts focus from common/easy transitions to rare/hard ones as training progresses. Apply capped importance-sampling corrections (following Schaul et al.) to remove bias from non-uniform sampling, with an exponential age-decay factor inspired by Freshness-Aware PER to prevent stale high-priority transitions from dominating. Evaluate against static curation baselines (SCIZOR, CUPID, DataMIL, Demo-SCORE) and uniform sampling on LIBERO (4 suites), RoboMimic (multi-human), and OXE subsets to demonstrate that adaptive, policy-driven prioritization outperforms one-shot filtering.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~500h A100-80GB (8-GPU fine-tuning runs: ~5 baselines × 24h + ~8 method runs × 40h + ~10 ablations × 20h)\",\n      \"gpu_utilization\": \"~25-35% effective utilization; GPUs idle while researcher implements value function, debugs priority refresh logic, analyzes priority distributions, and writes paper\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$750 at ~$1.50/hr (budget cloud provider e.g. Vast.ai or Lambda)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~700h A100-80GB (agent explores more hyperparameter configurations but human gates wasteful directions)\",\n      \"gpu_utilization\": \"~60-70% utilization; agent queues experiments overnight and weekends, human reviews results and approves next batch during daily check-in\",\n      \"timeline\": \"5-7 weeks\",\n      \"team\": \"1 researcher, ~30-45min/day check-in\",\n      \"claude_api_cost\": \"$150-300 (1000-2000 turns including code generation, experiment design, result analysis)\",\n      \"estimated_gpu_cost\": \"~$1,050 at ~$1.50/hr\",\n      \"risk_note\": \"Goal-conditioned value function architecture and TD-error priority scale require human judgment for tuning; unstable value learning could waste multiple GPU runs before human intervenes\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~1200-1500h A100-80GB (3x more experimental configurations explored: priority refresh schedules, value function sizes, α/β sweeps, IS correction strategies)\",\n      \"gpu_utilization\": \"~90-95% utilization; agent runs 24/7 scheduling next experiment immediately upon completion, no human wait\",\n      \"timeline\": \"10-18 days with 8× A100 cluster\",\n      \"team\": \"0 (initial setup and final review only)\",\n      \"claude_api_cost\": \"$300-600 (2000-4000 turns for code, experiment orchestration, ablation design, paper drafting)\",\n      \"estimated_gpu_cost\": \"~$2,250 at ~$1.50/hr\",\n      \"speed_bottleneck\": \"GPU cluster availability (requires 8× A100-80GB for OpenVLA-OFT fine-tuning parallelism); secondary bottleneck is LIBERO simulation throughput for evaluation rollouts\",\n      \"risk_note\": \"Agent may over-explore value function architectures without human intuition about which configurations are promising; risk of 20-30% wasted compute on dead-end configurations\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (deadline: May 26-29, 2026 — confirmed open)\",\n    \"AAAI 2027 (deadline: expected ~Aug 2026)\",\n    \"ICRA 2027 (deadline: expected ~Sep 2026)\",\n    \"ICLR 2027 (deadline: expected ~Sep-Oct 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Prioritized Experience Replay (ICLR 2016)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Curating Demonstrations using Online Experience (RSS 2025)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)\",\n    \"GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (arXiv 2025)\",\n    \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (arXiv 2025)\",\n    \"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (arXiv 2025)\",\n    \"Prioritized Replay for RL Post-training (arXiv 2026)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning (arXiv 2026)\",\n    \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models (arXiv 2023)\"\n  ],\n  \"description\": \"We propose Adaptive Prioritized Experience Replay (APER) for VLA model SFT, replacing static demonstration filtering with an online, policy-driven data curriculum. A lightweight goal-conditioned value function V(s,g) is trained via hindsight relabeling on demonstration data, producing TD errors as priority signals without reward annotations. During OpenVLA-OFT fine-tuning, transitions are sampled proportionally to their TD error magnitude — high-error transitions represent under-learned or critical state changes. Priorities are periodically refreshed as the policy improves, creating a natural curriculum from easy/common to rare/critical transitions. Unlike SCIZOR, CUPID, and DataMIL (static preprocessing), APER continuously adapts. Unlike Freshness-Aware PER and Prioritized Replay for RL Post-training (reward-dependent RL), APER operates in the reward-free imitation learning regime. Unlike Demo-SCORE (binary filter-and-retrain), APER provides fine-grained continuous prioritization integrated into the training loop. Evaluated on LIBERO, RoboMimic, and OXE subsets against five baselines, APER adds only ~5% compute overhead via the auxiliary value function while bridging the gap between static data curation and online RL for VLA training.\",\n  \"project_name\": \"adaptive_replay_vla\",\n  \"source\": \"web_research\"\n}\n\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T05:41:38.199Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T05:41:38.199Z",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-13T05:41:38.314Z_

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

## Idea under review (round 1/10)
{
  "title": "Adaptive Experience Replay with Policy-Driven Priorities for VLA",
  "core_problem": "Can we replace static demonstration filtering with an online, adaptive experience replay mechanism during VLA training, where sampling priorities co-evolve with the policy?",
  "opportunity": "Every existing demo curation method (SCIZOR, QoQ, RINSE, DataMIL, MI-based) operates as a static preprocessing step — score once, filter once, train once. This ignores that the policy's learning needs change during training: early on it needs diverse coverage; later it needs precise, high-quality transitions. Prioritized Experience Replay (PER) transformed RL training by adaptively focusing on high-TD-error transitions, but has never been adapted for imitation learning of VLA models. The key theoretical insight is that self-supervised TD errors in a goal-conditioned value function can serve as priority signals without rewards, creating a natural curriculum from easy/common transitions to rare/critical ones.",
  "landscape": "Prioritized Experience Replay (Schaul et al. 2015) is foundational in RL but not adopted in imitation learning. SCIZOR (ICRA 2026) filters once before training, discarding 15-40% of data statically. GR-RL (Dec 2025) has a multi-stage pipeline (filter → train → RL) but the filtering stage is still static. Curriculum learning for robot IL exists (HRL with curriculum demos, adaptive difficulty) but focuses on task curriculum, not data-quality curriculum. SimpleVLA-RL (ICLR 2026) uses GRPO for VLA online RL but doesn't address demo quality during the SFT stage. The blog post analyzing 164 VLA papers at ICLR 2026 identifies data quality as a critical gap, noting that 'OXE is mostly low-quality data, yet we still lack good methods to quantify data quality.' Concurrent work update (May 2026): Demo-SCORE (RSS 2025) uses online rollout experience to curate demonstrations via binary success/failure classification, but requires expensive environment interaction and operates as a discrete filter-and-retrain cycle rather than continuous priority adaptation. ExpReS-VLA (arXiv 2025) applies prioritized replay buffers with cosine-similarity retrieval for VLA continual learning to prevent catastrophic forgetting, not for improving initial SFT data quality. Freshness-Aware PER (arXiv April 2026) is the first to apply PER to LLM/VLM training but exclusively targets RL post-training with reward signals, leaving the reward-free SFT regime unaddressed. CUPID (CoRL 2025) and QoQ (arXiv 2026) use influence functions for demo curation but remain static preprocessing methods. Prioritized Replay for RL Post-training (arXiv Jan 2026) proposes problem-level prioritization for LLM RL but does not handle demonstration-level priorities in imitation learning. No existing work combines TD-error-based adaptive prioritization with reward-free imitation learning for VLA SFT.",
  "approach": "Train a lightweight goal-conditioned value function V(s, g) on the demonstration dataset using hindsight goal relabeling, producing TD errors without requiring any reward signal. During VLA SFT on OpenVLA-OFT (the current open-source SOTA for manipulation), maintain a prioritized replay buffer over the full demonstration dataset where each transition's sampling probability is proportional to its TD error magnitude — transitions with high TD error represent under-learned or critical state changes that the current policy finds surprising. Refresh priorities every K gradient steps by recomputing TD errors with the updated value function, creating a natural curriculum that shifts focus from common/easy transitions to rare/hard ones as training progresses. Apply capped importance-sampling corrections (following Schaul et al.) to remove bias from non-uniform sampling, with an exponential age-decay factor inspired by Freshness-Aware PER to prevent stale high-priority transitions from dominating. Evaluate against static curation baselines (SCIZOR, CUPID, DataMIL, Demo-SCORE) and uniform sampling on LIBERO (4 suites), RoboMimic (multi-human), and OXE subsets to demonstrate that adaptive, policy-driven prioritization outperforms one-shot filtering.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~500h A100-80GB (8-GPU fine-tuning runs: ~5 baselines × 24h + ~8 method runs × 40h + ~10 ablations × 20h)",
      "gpu_utilization": "~25-35% effective utilization; GPUs idle while researcher implements value function, debugs priority refresh logic, analyzes priority distributions, and writes paper",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$750 at ~$1.50/hr (budget cloud provider e.g. Vast.ai or Lambda)"
    },
    "human_in_loop": {
      "gpu_hours": "~700h A100-80GB (agent explores more hyperparameter configurations but human gates wasteful directions)",
      "gpu_utilization": "~60-70% utilization; agent queues experiments overnight and weekends, human reviews results and approves next batch during daily check-in",
      "timeline": "5-7 weeks",
      "team": "1 researcher, ~30-45min/day check-in",
      "claude_api_cost": "$150-300 (1000-2000 turns including code generation, experiment design, result analysis)",
      "estimated_gpu_cost": "~$1,050 at ~$1.50/hr",
      "risk_note": "Goal-conditioned value function architecture and TD-error priority scale require human judgment for tuning; unstable value learning could waste multiple GPU runs before human intervenes"
    },
    "auto_research": {
      "gpu_hours": "~1200-1500h A100-80GB (3x more experimental configurations explored: priority refresh schedules, value function sizes, α/β sweeps, IS correction strategies)",
      "gpu_utilization": "~90-95% utilization; agent runs 24/7 scheduling next experiment immediately upon completion, no human wait",
      "timeline": "10-18 days with 8× A100 cluster",
      "team": "0 (initial setup and final review only)",
      "claude_api_cost": "$300-600 (2000-4000 turns for code, experiment orchestration, ablation design, paper drafting)",
      "estimated_gpu_cost": "~$2,250 at ~$1.50/hr",
      "speed_bottleneck": "GPU cluster availability (requires 8× A100-80GB for OpenVLA-OFT fine-tuning parallelism); secondary bottleneck is LIBERO simulation throughput for evaluation rollouts",
      "risk_note": "Agent may over-explore value function architectures without human intuition about which configurations are promising; risk of 20-30% wasted compute on dead-end configurations"
    }
  },
  "target_venues": [
    "CoRL 2026 (deadline: May 26-29, 2026 — confirmed open)",
    "AAAI 2027 (deadline: expected ~Aug 2026)",
    "ICRA 2027 (deadline: expected ~Sep 2026)",
    "ICLR 2027 (deadline: expected ~Sep-Oct 2026)"
  ],
  "level": "solid",
  "key_references": [
    "Prioritized Experience Replay (ICLR 2016)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "Curating Demonstrations using Online Experience (RSS 2025)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (arXiv 2025)",
    "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning (arXiv 2026)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (arXiv 2025)",
    "ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (arXiv 2025)",
    "Prioritized Replay for RL Post-training (arXiv 2026)",
    "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning (arXiv 2026)",
    "Open X-Embodiment: Robotic Learning Datasets and RT-X Models (arXiv 2023)"
  ],
  "description": "We propose Adaptive Prioritized Experience Replay (APER) for VLA model SFT, replacing static demonstration filtering with an online, policy-driven data curriculum. A lightweight goal-conditioned value function V(s,g) is trained via hindsight relabeling on demonstration data, producing TD errors as priority signals without reward annotations. During OpenVLA-OFT fine-tuning, transitions are sampled proportionally to their TD error magnitude — high-error transitions represent under-learned or critical state changes. Priorities are periodically refreshed as the policy improves, creating a natural curriculum from easy/common to rare/critical transitions. Unlike SCIZOR, CUPID, and DataMIL (static preprocessing), APER continuously adapts. Unlike Freshness-Aware PER and Prioritized Replay for RL Post-training (reward-dependent RL), APER operates in the reward-free imitation learning regime. Unlike Demo-SCORE (binary filter-and-retrain), APER provides fine-grained continuous prioritization integrated into the training loop. Evaluated on LIBERO, RoboMimic, and OXE subsets against five baselines, APER adds only ~5% compute overhead via the auxiliary value function while bridging the gap between static data curation and online RL for VLA training.",
  "project_name": "adaptive_replay_vla",
  "source": "web_research"
}



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
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "9749a4e0-39fe-4acd-8f44-8541d8a46c9e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T05:41:38.309Z_

```json
{
  "parentUuid": "9749a4e0-39fe-4acd-8f44-8541d8a46c9e",
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
  "uuid": "5441e663-c4fd-4331-8d84-6e6283ff7860",
  "timestamp": "2026-05-13T05:41:38.309Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T05:41:38.309Z_

```json
{
  "parentUuid": "5441e663-c4fd-4331-8d84-6e6283ff7860",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "93f469f2-7456-4930-a0b7-034d45104ce4",
  "timestamp": "2026-05-13T05:41:38.309Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
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
  "leafUuid": "93f469f2-7456-4930-a0b7-034d45104ce4",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify adaptive replay priorities for VLA training feasibility",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Assistant

_source line 8 · 2026-05-13T05:41:42.736Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea about "Adaptive Experience Replay with Policy-Driven Priorities for VLA" for CoRL 2026. I need to independently verify the claims, check novelty, feasibility, and assess whether this is truly CoRL-quality work.

Let me start by searching for the key claims and related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93f469f2-7456-4930-a0b7-034d45104ce4",
  "isSidechain": false,
  "requestId": "req_011Caz2t58ZnzfgMVQjjtgtk",
  "type": "assistant",
  "uuid": "79d217ba-2eb1-4b9f-b1bf-c2c253801eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3HDfj7CuyW8qq92riiUEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11487,
      "cache_read_input_tokens": 11841,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 431,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11487
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

_source line 9 · 2026-05-13T05:41:43.238Z_

I'll conduct a thorough adversarial review of this idea. Let me start by independently verifying the key claims through multiple search dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d217ba-2eb1-4b9f-b1bf-c2c253801eb7",
  "isSidechain": false,
  "requestId": "req_011Caz2t58ZnzfgMVQjjtgtk",
  "type": "assistant",
  "uuid": "4da700cf-4fea-48f1-a0ab-f79269094df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3HDfj7CuyW8qq92riiUEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11487,
      "cache_read_input_tokens": 11841,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 431,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11487
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

_source line 10 · 2026-05-13T05:41:49.355Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GsLXwJdk9znZWWTj3DJDqU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search VLA data curation SOTA",
  "prompt": "You are helping me do a literature review. I need you to search for the current state-of-the-art in data curation and filtering for Vision-Language-Action (VLA) model training in robotics. \n\nSpecifically search for:\n1. \"VLA data curation 2025 2026\" \n2. \"demonstration filtering imitation learning robot 2026\"\n3. \"data quality vision language action model\"\n4. \"SCIZOR data curation imitation learning\"\n5. \"adaptive data selection robot learning 2026\"\n\nFor each search, use WebSearch and report the top results with titles, URLs, and brief descriptions. I need to know what the actual current SOTA methods are for filtering/curating robot demonstration data as of May 2026.\n\nAlso search for:\n6. \"site:arxiv.org VLA training data quality 2026\"\n7. \"demonstration quality scoring robot manipulation 2026\"\n\nReport all findings comprehensively."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4da700cf-4fea-48f1-a0ab-f79269094df1",
  "isSidechain": false,
  "requestId": "req_011Caz2t58ZnzfgMVQjjtgtk",
  "type": "assistant",
  "uuid": "e751b148-8c2e-4fc9-a609-67099790063c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3HDfj7CuyW8qq92riiUEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11487,
      "cache_read_input_tokens": 11841,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 431,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11487
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

_source line 11 · 2026-05-13T05:43:24.030Z_

<details><summary>↩ Tool result · `toolu_01GsLXwJdk9znZWWTj3DJDqU`</summary>

```text
Here is a comprehensive report of findings across all seven search queries.

---

## Literature Review: Data Curation and Filtering for VLA Model Training in Robotics (as of May 2026)

### 1. SCIZOR -- The Leading Self-Supervised Data Curation Method

**SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning** (UT Austin RPL, accepted at ICRA 2026)

This is arguably the most prominent recent work directly targeting VLA/imitation learning data curation. SCIZOR addresses two complementary sources of low-quality data:

- **Suboptimal data**: Uses a self-supervised task progress predictor to remove state-action pairs that lack meaningful task progression.
- **Redundant data**: Applies a deduplication module operating on joint state-action representations to remove repetitive patterns.

Key results: Average improvement of 15.4% across benchmarks -- +5.4% on RoboMimic, +8.1% on OXE-Magic-Soup, and +32.9% on Sirius-Fleet real-robot tasks. Crucially, SCIZOR operates at the **state-action pair level** (fine-grained), not just trajectory-level, which is a key differentiator from prior work.

- Paper: [arXiv:2505.22626](https://arxiv.org/abs/2505.22626)
- Project page: [https://ut-austin-rpl.github.io/SCIZOR/](https://ut-austin-rpl.github.io/SCIZOR/)
- Code: [https://github.com/UT-Austin-RPL/SCIZOR](https://github.com/UT-Austin-RPL/SCIZOR)

---

### 2. CUPID -- Influence Function-Based Curation (CoRL 2025)

**CUPID: Curating Data your Robot Loves with Influence Functions**

Uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance. Two capabilities:
1. **Filtering**: Removes training demonstrations that harm policy performance.
2. **Subselection**: Identifies which newly collected trajectories will most improve the policy.

Key results: Training with less than 33% of curated data yields SOTA diffusion policies on RoboMimic. Hardware experiments show the method can identify robust strategies under distribution shift and isolate spurious correlations.

- Paper: [arXiv:2506.19121](https://arxiv.org/abs/2506.19121)
- Project page: [https://cupid-curation.github.io/](https://cupid-curation.github.io/)
- Published in: CoRL 2025, PMLR 305:2907-2932

---

### 3. Quality over Quantity (QoQ) -- Demonstration Curation via Influence Functions (March 2026)

**Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning**

Defines data quality as the contribution of each training sample to reducing loss on validation demonstrations, using influence functions. Addresses noise and suboptimal behaviors introduced by human teleoperation variability.

- Paper: [arXiv:2603.09056](https://arxiv.org/abs/2603.09056) (March 10, 2026)
- Extended HTML: [https://arxiv.org/html/2603.09056](https://arxiv.org/html/2603.09056)

---

### 4. VINE -- Hierarchical VLA Using Success AND Failure Demonstrations

**Hierarchical Vision Language Action Model Using Success and Failure Demonstrations** (December 2025)

Key insight: Prior VLAs discard failed demonstrations, but failures encode where and how policies can be fragile. VINE separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical RL formalism, making failures usable as a structured learning signal. System 2 performs feasibility-guided tree search, predicting success probabilities from both successes and failures and pruning brittle branches.

- Paper: [arXiv:2512.03913](https://arxiv.org/abs/2512.03913)

---

### 5. What Matters in Learning from Large-Scale Datasets for Robot Manipulation (NVIDIA, 2025)

Systematic study of what data diversity dimensions matter most. Developed a procedural data generation framework to emulate common sources of diversity (sensor placements, object types, spatial arrangements). Key finding: **camera poses and spatial arrangements are crucial dimensions** for both diversity in collection and alignment in retrieval. Their retrieval strategies on the DROID dataset outperform existing training strategies by up to 70%.

- Paper: [arXiv:2506.13536](https://arxiv.org/abs/2506.13536)
- NVIDIA project page: [https://research.nvidia.com/labs/srl/publication/saxena-2025-what/](https://research.nvidia.com/labs/srl/publication/saxena-2025-what/)

---

### 6. VLA Foundry -- Unified VLA Training Framework (April 2026)

**VLA Foundry: A Unified Framework for Training Vision-Language-Action Models** (Toyota Research Institute)

Open-source framework unifying LLM, VLM, and VLA training in a single codebase. Supports mixed-modality data (text, image-captions, robotics) and end-to-end training pipelines from LLM to VLM to VLA. Built on FSDP2 with WebDataset streaming.

- Paper: [arXiv:2604.19728](https://arxiv.org/abs/2604.19728)
- Project page: [https://tri-ml.github.io/vla_foundry/](https://tri-ml.github.io/vla_foundry/)

---

### 7. Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines (April 2026)

The most comprehensive and recent survey, arguing that **future VLA advances will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols**. Covers dataset construction along three key dimensions: data quality, scale, and diversity. Discusses mixed data co-training as a strategy for boosting efficiency.

- Paper: [arXiv:2604.23001](https://arxiv.org/abs/2604.23001)

---

### 8. Additional Relevant Work

**Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning** (ICRA 2026)
- Two-stage pipeline: selects a representative demonstration via user-defined task intention scores, extracts canonical motion shape via Periodic DMPs, then uses LSTM to refine the full demo set.
- [OpenReview](https://openreview.net/forum?id=7Ox8aKIFbA) | [GitHub](https://github.com/FocasLab/ICRA-IL-2026)

**ICRA 2026 Workshop: "From Data to Decisions: VLA Pipelines for Real Robots"**
- Dedicated workshop on the full VLA pipeline from data collection/curation to training and inference.
- Competition with 10,000 hours of real-world robot data in LeRobot format.
- [Workshop site](https://icra2026vlapipeline.github.io/) | [AIRoA announcement](https://www.airoa.org/updates/2026-02-10)

**MolmoAct 2 (AI2)**
- Released the YAM dataset: 700+ hours of bimanual robot demonstrations, the largest open-source bimanual robotics dataset.
- [Blog post](https://allenai.org/blog/molmoact2)

**SmolVLA (Hugging Face)**
- Efficient VLA model trained on LeRobot community data, demonstrating the viability of community-curated datasets.
- [Blog post](https://huggingface.co/blog/smolvla)

**State of VLA Research at ICLR 2026** -- A blog summary of VLA trends at ICLR 2026.
- [Blog post](https://mbreuss.github.io/blog_post_iclr_26_vla.html)

**A Survey on Efficient Vision-Language-Action Models** (arXiv:2510.24795)
- First comprehensive review of Efficient VLAs across the model-training-data pipeline.
- [Paper](https://arxiv.org/abs/2510.24795)

---

### Summary of SOTA Methods for Filtering/Curating Robot Demonstration Data (May 2026)

| Method | Approach | Granularity | Key Venue |
|--------|----------|-------------|-----------|
| **SCIZOR** | Self-supervised progress prediction + deduplication | State-action pair | ICRA 2026 |
| **CUPID** | Influence functions on closed-loop returns | Trajectory | CoRL 2025 |
| **QoQ** | Influence functions on validation loss | Sample | arXiv Mar 2026 |
| **VINE** | Hierarchical VLA with failure-aware tree search | Trajectory (success+failure) | arXiv Dec 2025 |
| **Beyond the Teacher** | Representative selection + LSTM refinement | Trajectory | ICRA 2026 |

The clear trend is a shift from manual/heuristic curation toward **automated, principled data quality estimation** -- with influence functions and self-supervised quality predictors as the two dominant paradigms. The field consensus, articulated most clearly in the April 2026 survey (arXiv:2604.23001), is that **data engine co-design will matter more than architecture** for the next generation of VLA models.

Sources:
- [SCIZOR (arXiv:2505.22626)](https://arxiv.org/abs/2505.22626)
- [SCIZOR Project Page](https://ut-austin-rpl.github.io/SCIZOR/)
- [CUPID (arXiv:2506.19121)](https://arxiv.org/abs/2506.19121)
- [CUPID Project Page](https://cupid-curation.github.io/)
- [Quality over Quantity (arXiv:2603.09056)](https://arxiv.org/abs/2603.09056)
- [VINE: Hierarchical VLA (arXiv:2512.03913)](https://arxiv.org/abs/2512.03913)
- [What Matters in Large-Scale Datasets (arXiv:2506.13536)](https://arxiv.org/abs/2506.13536)
- [VLA Foundry (arXiv:2604.19728)](https://arxiv.org/abs/2604.19728)
- [VLA Survey: Datasets, Benchmarks, Data Engines (arXiv:2604.23001)](https://arxiv.org/abs/2604.23001)
- [Beyond the Teacher (OpenReview)](https://openreview.net/forum?id=7Ox8aKIFbA)
- [ICRA 2026 VLA Pipelines Workshop](https://icra2026vlapipeline.github.io/)
- [AIRoA ICRA 2026 Announcement](https://www.airoa.org/updates/2026-02-10)
- [MolmoAct 2 (AI2)](https://allenai.org/blog/molmoact2)
- [SmolVLA (Hugging Face)](https://huggingface.co/blog/smolvla)
- [State of VLA at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- [Efficient VLA Survey (arXiv:2510.24795)](https://arxiv.org/abs/2510.24795)
- [OpenVLA](https://openvla.github.io/)
- [State of Robotics 2026 Report](https://www.roboticscenter.ai/state-of-robotics-2026)
- [VLA Wikipedia](https://en.wikipedia.org/wiki/Vision-language-action_model)

agentId: acab4e3ce805ecb28 (use SendMessage with to: 'acab4e3ce805ecb28' to continue this agent)
&lt;usage>total_tokens: 26919
tool_uses: 16
duration_ms: 94667&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e751b148-8c2e-4fc9-a609-67099790063c",
  "isSidechain": false,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "de1c3665-8a86-4781-b666-7b03b8639e62",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me do a literature review. I need you to search for the current state-of-the-art in data curation and filtering for Vision-Language-Action (VLA) model training in robotics. \n\nSpecifically search for:\n1. \"VLA data curation 2025 2026\" \n2. \"demonstration filtering imitation learning robot 2026\"\n3. \"data quality vision language action model\"\n4. \"SCIZOR data curation imitation learning\"\n5. \"adaptive data selection robot learning 2026\"\n\nFor each search, use WebSearch and report the top results with titles, URLs, and brief descriptions. I need to know what the actual current SOTA methods are for filtering/curating robot demonstration data as of May 2026.\n\nAlso search for:\n6. \"site:arxiv.org VLA training data quality 2026\"\n7. \"demonstration quality scoring robot manipulation 2026\"\n\nReport all findings comprehensively.",
    "agentId": "acab4e3ce805ecb28",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of findings across all seven search queries.\n\n---\n\n## Literature Review: Data Curation and Filtering for VLA Model Training in Robotics (as of May 2026)\n\n### 1. SCIZOR -- The Leading Self-Supervised Data Curation Method\n\n**SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning** (UT Austin RPL, accepted at ICRA 2026)\n\nThis is arguably the most prominent recent work directly targeting VLA/imitation learning data curation. SCIZOR addresses two complementary sources of low-quality data:\n\n- **Suboptimal data**: Uses a self-supervised task progress predictor to remove state-action pairs that lack meaningful task progression.\n- **Redundant data**: Applies a deduplication module operating on joint state-action representations to remove repetitive patterns.\n\nKey results: Average improvement of 15.4% across benchmarks -- +5.4% on RoboMimic, +8.1% on OXE-Magic-Soup, and +32.9% on Sirius-Fleet real-robot tasks. Crucially, SCIZOR operates at the **state-action pair level** (fine-grained), not just trajectory-level, which is a key differentiator from prior work.\n\n- Paper: [arXiv:2505.22626](https://arxiv.org/abs/2505.22626)\n- Project page: [https://ut-austin-rpl.github.io/SCIZOR/](https://ut-austin-rpl.github.io/SCIZOR/)\n- Code: [https://github.com/UT-Austin-RPL/SCIZOR](https://github.com/UT-Austin-RPL/SCIZOR)\n\n---\n\n### 2. CUPID -- Influence Function-Based Curation (CoRL 2025)\n\n**CUPID: Curating Data your Robot Loves with Influence Functions**\n\nUses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance. Two capabilities:\n1. **Filtering**: Removes training demonstrations that harm policy performance.\n2. **Subselection**: Identifies which newly collected trajectories will most improve the policy.\n\nKey results: Training with less than 33% of curated data yields SOTA diffusion policies on RoboMimic. Hardware experiments show the method can identify robust strategies under distribution shift and isolate spurious correlations.\n\n- Paper: [arXiv:2506.19121](https://arxiv.org/abs/2506.19121)\n- Project page: [https://cupid-curation.github.io/](https://cupid-curation.github.io/)\n- Published in: CoRL 2025, PMLR 305:2907-2932\n\n---\n\n### 3. Quality over Quantity (QoQ) -- Demonstration Curation via Influence Functions (March 2026)\n\n**Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning**\n\nDefines data quality as the contribution of each training sample to reducing loss on validation demonstrations, using influence functions. Addresses noise and suboptimal behaviors introduced by human teleoperation variability.\n\n- Paper: [arXiv:2603.09056](https://arxiv.org/abs/2603.09056) (March 10, 2026)\n- Extended HTML: [https://arxiv.org/html/2603.09056](https://arxiv.org/html/2603.09056)\n\n---\n\n### 4. VINE -- Hierarchical VLA Using Success AND Failure Demonstrations\n\n**Hierarchical Vision Language Action Model Using Success and Failure Demonstrations** (December 2025)\n\nKey insight: Prior VLAs discard failed demonstrations, but failures encode where and how policies can be fragile. VINE separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical RL formalism, making failures usable as a structured learning signal. System 2 performs feasibility-guided tree search, predicting success probabilities from both successes and failures and pruning brittle branches.\n\n- Paper: [arXiv:2512.03913](https://arxiv.org/abs/2512.03913)\n\n---\n\n### 5. What Matters in Learning from Large-Scale Datasets for Robot Manipulation (NVIDIA, 2025)\n\nSystematic study of what data diversity dimensions matter most. Developed a procedural data generation framework to emulate common sources of diversity (sensor placements, object types, spatial arrangements). Key finding: **camera poses and spatial arrangements are crucial dimensions** for both diversity in collection and alignment in retrieval. Their retrieval strategies on the DROID dataset outperform existing training strategies by up to 70%.\n\n- Paper: [arXiv:2506.13536](https://arxiv.org/abs/2506.13536)\n- NVIDIA project page: [https://research.nvidia.com/labs/srl/publication/saxena-2025-what/](https://research.nvidia.com/labs/srl/publication/saxena-2025-what/)\n\n---\n\n### 6. VLA Foundry -- Unified VLA Training Framework (April 2026)\n\n**VLA Foundry: A Unified Framework for Training Vision-Language-Action Models** (Toyota Research Institute)\n\nOpen-source framework unifying LLM, VLM, and VLA training in a single codebase. Supports mixed-modality data (text, image-captions, robotics) and end-to-end training pipelines from LLM to VLM to VLA. Built on FSDP2 with WebDataset streaming.\n\n- Paper: [arXiv:2604.19728](https://arxiv.org/abs/2604.19728)\n- Project page: [https://tri-ml.github.io/vla_foundry/](https://tri-ml.github.io/vla_foundry/)\n\n---\n\n### 7. Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines (April 2026)\n\nThe most comprehensive and recent survey, arguing that **future VLA advances will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols**. Covers dataset construction along three key dimensions: data quality, scale, and diversity. Discusses mixed data co-training as a strategy for boosting efficiency.\n\n- Paper: [arXiv:2604.23001](https://arxiv.org/abs/2604.23001)\n\n---\n\n### 8. Additional Relevant Work\n\n**Beyond the Teacher: Leveraging Mixed-Skill Demonstrations for Robust Imitation Learning** (ICRA 2026)\n- Two-stage pipeline: selects a representative demonstration via user-defined task intention scores, extracts canonical motion shape via Periodic DMPs, then uses LSTM to refine the full demo set.\n- [OpenReview](https://openreview.net/forum?id=7Ox8aKIFbA) | [GitHub](https://github.com/FocasLab/ICRA-IL-2026)\n\n**ICRA 2026 Workshop: \"From Data to Decisions: VLA Pipelines for Real Robots\"**\n- Dedicated workshop on the full VLA pipeline from data collection/curation to training and inference.\n- Competition with 10,000 hours of real-world robot data in LeRobot format.\n- [Workshop site](https://icra2026vlapipeline.github.io/) | [AIRoA announcement](https://www.airoa.org/updates/2026-02-10)\n\n**MolmoAct 2 (AI2)**\n- Released the YAM dataset: 700+ hours of bimanual robot demonstrations, the largest open-source bimanual robotics dataset.\n- [Blog post](https://allenai.org/blog/molmoact2)\n\n**SmolVLA (Hugging Face)**\n- Efficient VLA model trained on LeRobot community data, demonstrating the viability of community-curated datasets.\n- [Blog post](https://huggingface.co/blog/smolvla)\n\n**State of VLA Research at ICLR 2026** -- A blog summary of VLA trends at ICLR 2026.\n- [Blog post](https://mbreuss.github.io/blog_post_iclr_26_vla.html)\n\n**A Survey on Efficient Vision-Language-Action Models** (arXiv:2510.24795)\n- First comprehensive review of Efficient VLAs across the model-training-data pipeline.\n- [Paper](https://arxiv.org/abs/2510.24795)\n\n---\n\n### Summary of SOTA Methods for Filtering/Curating Robot Demonstration Data (May 2026)\n\n| Method | Approach | Granularity | Key Venue |\n|--------|----------|-------------|-----------|\n| **SCIZOR** | Self-supervised progress prediction + deduplication | State-action pair | ICRA 2026 |\n| **CUPID** | Influence functions on closed-loop returns | Trajectory | CoRL 2025 |\n| **QoQ** | Influence functions on validation loss | Sample | arXiv Mar 2026 |\n| **VINE** | Hierarchical VLA with failure-aware tree search | Trajectory (success+failure) | arXiv Dec 2025 |\n| **Beyond the Teacher** | Representative selection + LSTM refinement | Trajectory | ICRA 2026 |\n\nThe clear trend is a shift from manual/heuristic curation toward **automated, principled data quality estimation** -- with influence functions and self-supervised quality predictors as the two dominant paradigms. The field consensus, articulated most clearly in the April 2026 survey (arXiv:2604.23001), is that **data engine co-design will matter more than architecture** for the next generation of VLA models.\n\nSources:\n- [SCIZOR (arXiv:2505.22626)](https://arxiv.org/abs/2505.22626)\n- [SCIZOR Project Page](https://ut-austin-rpl.github.io/SCIZOR/)\n- [CUPID (arXiv:2506.19121)](https://arxiv.org/abs/2506.19121)\n- [CUPID Project Page](https://cupid-curation.github.io/)\n- [Quality over Quantity (arXiv:2603.09056)](https://arxiv.org/abs/2603.09056)\n- [VINE: Hierarchical VLA (arXiv:2512.03913)](https://arxiv.org/abs/2512.03913)\n- [What Matters in Large-Scale Datasets (arXiv:2506.13536)](https://arxiv.org/abs/2506.13536)\n- [VLA Foundry (arXiv:2604.19728)](https://arxiv.org/abs/2604.19728)\n- [VLA Survey: Datasets, Benchmarks, Data Engines (arXiv:2604.23001)](https://arxiv.org/abs/2604.23001)\n- [Beyond the Teacher (OpenReview)](https://openreview.net/forum?id=7Ox8aKIFbA)\n- [ICRA 2026 VLA Pipelines Workshop](https://icra2026vlapipeline.github.io/)\n- [AIRoA ICRA 2026 Announcement](https://www.airoa.org/updates/2026-02-10)\n- [MolmoAct 2 (AI2)](https://allenai.org/blog/molmoact2)\n- [SmolVLA (Hugging Face)](https://huggingface.co/blog/smolvla)\n- [State of VLA at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html)\n- [Efficient VLA Survey (arXiv:2510.24795)](https://arxiv.org/abs/2510.24795)\n- [OpenVLA](https://openvla.github.io/)\n- [State of Robotics 2026 Report](https://www.roboticscenter.ai/state-of-robotics-2026)\n- [VLA Wikipedia](https://en.wikipedia.org/wiki/Vision-language-action_model)"
      }
    ],
    "totalDurationMs": 94667,
    "totalTokens": 26919,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4982,
      "cache_read_input_tokens": 18964,
      "output_tokens": 2972,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2972,
          "cache_read_input_tokens": 18964,
          "cache_creation_input_tokens": 4982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4982,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "e751b148-8c2e-4fc9-a609-67099790063c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T05:43:26.875Z_

Good, I have a solid landscape picture. Now let me search for the more specific claims about PER in imitation learning and concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de1c3665-8a86-4781-b666-7b03b8639e62",
  "isSidechain": false,
  "requestId": "req_011Caz31qPYpjimGZpLVWFaa",
  "type": "assistant",
  "uuid": "1f87fe39-23e8-4ec0-805f-6d16956ff072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186Zt8RoRuJauioB9NPwMfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3481,
      "cache_read_input_tokens": 23328,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 23328,
          "cache_creation_input_tokens": 3481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3481
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

_source line 13 · 2026-05-13T05:43:33.722Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SB26GoMNdM6mNQbbW458AY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search PER imitation learning",
  "prompt": "You are helping me with a literature review. I need to verify whether Prioritized Experience Replay (PER) has been applied to imitation learning or supervised fine-tuning of large models. Search for:\n\n1. \"prioritized experience replay imitation learning\" \n2. \"prioritized replay supervised fine-tuning\"\n3. \"adaptive data sampling imitation learning robot 2025 2026\"\n4. \"experience replay demonstration learning robotics\"\n5. \"TD error imitation learning priority\"\n6. \"curriculum learning demonstration data robot 2025 2026\"\n7. \"Freshness-Aware Prioritized Experience Replay\" (verify this paper exists)\n8. \"ExpReS-VLA\" (verify this paper exists)\n9. \"Demo-SCORE demonstration curation\" (verify this paper exists)\n\nFor each search use WebSearch and report all relevant results with titles, URLs, and descriptions. I specifically need to know:\n- Has anyone applied PER or TD-error-based prioritization to imitation learning (not RL)?\n- Has anyone done adaptive/online data selection during SFT training of VLA or LLM models?\n- Do the papers \"Freshness-Aware PER\", \"ExpReS-VLA\", and \"Demo-SCORE\" actually exist?\n\nBe thorough and report everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f87fe39-23e8-4ec0-805f-6d16956ff072",
  "isSidechain": false,
  "requestId": "req_011Caz31qPYpjimGZpLVWFaa",
  "type": "assistant",
  "uuid": "10fe7683-672c-4fa0-901d-2d8c6223515c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186Zt8RoRuJauioB9NPwMfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3481,
      "cache_read_input_tokens": 23328,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 23328,
          "cache_creation_input_tokens": 3481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3481
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

_source line 14 · 2026-05-13T05:43:37.062Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TybAVAoev6LSQ1Nu3WUied`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search CoRL 2026 deadline",
  "prompt": "Search for the CoRL 2026 conference submission deadline. I need to verify:\n1. Is CoRL 2026 happening in Austin, Nov 9-12, 2026?\n2. What is the abstract deadline? Is it May 26, 2026?\n3. What is the paper deadline? Is it May 29, 2026?\n\nSearch for:\n1. \"CoRL 2026 submission deadline\"\n2. \"CoRL 2026 call for papers\"\n3. \"site:corl.org 2026\" or \"corl2026.org\"\n\nReport exact dates found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10fe7683-672c-4fa0-901d-2d8c6223515c",
  "isSidechain": false,
  "requestId": "req_011Caz31qPYpjimGZpLVWFaa",
  "type": "assistant",
  "uuid": "b17d856b-ed3e-4e2a-bc4a-c483337bf8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186Zt8RoRuJauioB9NPwMfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3481,
      "cache_read_input_tokens": 23328,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 23328,
          "cache_creation_input_tokens": 3481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3481
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

_source line 15 · 2026-05-13T05:43:43.826Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UhQUhAKeCb4asUWLUFo96a`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search concurrent work novelty",
  "prompt": "You are helping me with a critical literature review. I need to find work that might be very similar to the following idea: \"Using TD-error based prioritized experience replay during supervised fine-tuning of Vision-Language-Action models, with a goal-conditioned value function trained via hindsight relabeling to produce priority scores without reward signals.\"\n\nSearch specifically for:\n1. \"online data selection SFT training 2025 2026\"\n2. \"adaptive sampling fine-tuning language model 2026\"\n3. \"goal-conditioned value function imitation learning\"\n4. \"hindsight relabeling demonstration quality\"\n5. \"data curriculum robot learning online adaptive 2026\"\n6. \"loss-based sampling training data selection 2026\"\n7. \"self-paced learning imitation learning robotics\"\n8. \"importance sampling demonstration data robot\"\n9. \"RINSE robot imitation noise\" (verify this method exists)\n10. \"DataMIL data selection robot imitation\" (verify this paper exists)\n\nI'm looking for any work that does ADAPTIVE (not static/one-time) data selection during the training loop of imitation learning or SFT. This is the key novelty claim I need to verify.\n\nReport all findings with titles, URLs, and brief descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b17d856b-ed3e-4e2a-bc4a-c483337bf8dd",
  "isSidechain": false,
  "requestId": "req_011Caz31qPYpjimGZpLVWFaa",
  "type": "assistant",
  "uuid": "7c03ae43-b218-4eff-845d-dedfefdb0e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186Zt8RoRuJauioB9NPwMfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3481,
      "cache_read_input_tokens": 23328,
      "output_tokens": 1010,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1010,
          "cache_read_input_tokens": 23328,
          "cache_creation_input_tokens": 3481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3481
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

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7c03ae43-b218-4eff-845d-dedfefdb0e72",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify adaptive replay priorities for VLA training feasibility",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Tool result

_source line 18 · 2026-05-13T05:44:45.447Z_

<details><summary>↩ Tool result · `toolu_01TybAVAoev6LSQ1Nu3WUied`</summary>

```text
Here are the findings from multiple sources:

## CoRL 2026 -- Verified Details

### 1. Location and Conference Dates -- CONFIRMED
CoRL 2026 is happening in **Austin, Texas** at the **JW Marriott Austin** (110 E 2nd St, Austin, TX 78701).
- **Workshops**: November 9, 2026
- **Main conference**: November 10-12, 2026

So "November 9-12, 2026" is correct when counting workshops + main conference together.

### 2. Abstract Deadline -- CONFIRMED
**May 26, 2026 at 11:59 UTC** -- This matches what you asked to verify.

### 3. Paper Deadline -- CONFIRMED
**May 29, 2026 at 11:59 UTC** -- This also matches what you asked to verify.

### Note on a Minor Discrepancy
The official "Instruction for Authors" page on corl.org mentions "the paper submission deadline is Thursday (5/28) EOD rather than Friday!" -- however, the structured data in the Hugging Face AI Deadlines tracker (sourced from corl.org) and search engine results consistently list **May 29, 2026** (which is a Friday). May 28, 2026 is Thursday. It is possible the official site is emphasizing that authors should aim to finish by Thursday 5/28 EOD as a practical warning, while the hard cutoff is technically Friday 5/29 at 11:59 UTC. Regardless, if you are submitting, treat **Thursday May 28** as a safe target to avoid any risk, since the official instructions highlight that date.

### Summary of Key Dates
| Item | Date |
|---|---|
| Abstract deadline | May 26, 2026, 11:59 UTC |
| Paper deadline | May 29, 2026, 11:59 UTC |
| Camera-ready deadline | Oct 12, 2026, 23:59 AoE |
| Workshops | Nov 9, 2026 |
| Main conference | Nov 10-12, 2026 |
| Venue | JW Marriott Austin, TX |

All three items you asked to verify are confirmed correct.

Sources:
- [CoRL 2026 -- Main Site](https://www.corl.org/)
- [CoRL 2026 -- Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 -- Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 Conference | OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)
- [Hugging Face AI Deadlines -- CoRL 2026 update commit](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)

agentId: a7343bd69b62a91a6 (use SendMessage with to: 'a7343bd69b62a91a6' to continue this agent)
&lt;usage>total_tokens: 16788
tool_uses: 12
duration_ms: 68382&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b17d856b-ed3e-4e2a-bc4a-c483337bf8dd",
  "isSidechain": false,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "3f2b07de-690d-4596-82a0-ac8eccb2f24d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the CoRL 2026 conference submission deadline. I need to verify:\n1. Is CoRL 2026 happening in Austin, Nov 9-12, 2026?\n2. What is the abstract deadline? Is it May 26, 2026?\n3. What is the paper deadline? Is it May 29, 2026?\n\nSearch for:\n1. \"CoRL 2026 submission deadline\"\n2. \"CoRL 2026 call for papers\"\n3. \"site:corl.org 2026\" or \"corl2026.org\"\n\nReport exact dates found.",
    "agentId": "a7343bd69b62a91a6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings from multiple sources:\n\n## CoRL 2026 -- Verified Details\n\n### 1. Location and Conference Dates -- CONFIRMED\nCoRL 2026 is happening in **Austin, Texas** at the **JW Marriott Austin** (110 E 2nd St, Austin, TX 78701).\n- **Workshops**: November 9, 2026\n- **Main conference**: November 10-12, 2026\n\nSo \"November 9-12, 2026\" is correct when counting workshops + main conference together.\n\n### 2. Abstract Deadline -- CONFIRMED\n**May 26, 2026 at 11:59 UTC** -- This matches what you asked to verify.\n\n### 3. Paper Deadline -- CONFIRMED\n**May 29, 2026 at 11:59 UTC** -- This also matches what you asked to verify.\n\n### Note on a Minor Discrepancy\nThe official \"Instruction for Authors\" page on corl.org mentions \"the paper submission deadline is Thursday (5/28) EOD rather than Friday!\" -- however, the structured data in the Hugging Face AI Deadlines tracker (sourced from corl.org) and search engine results consistently list **May 29, 2026** (which is a Friday). May 28, 2026 is Thursday. It is possible the official site is emphasizing that authors should aim to finish by Thursday 5/28 EOD as a practical warning, while the hard cutoff is technically Friday 5/29 at 11:59 UTC. Regardless, if you are submitting, treat **Thursday May 28** as a safe target to avoid any risk, since the official instructions highlight that date.\n\n### Summary of Key Dates\n| Item | Date |\n|---|---|\n| Abstract deadline | May 26, 2026, 11:59 UTC |\n| Paper deadline | May 29, 2026, 11:59 UTC |\n| Camera-ready deadline | Oct 12, 2026, 23:59 AoE |\n| Workshops | Nov 9, 2026 |\n| Main conference | Nov 10-12, 2026 |\n| Venue | JW Marriott Austin, TX |\n\nAll three items you asked to verify are confirmed correct.\n\nSources:\n- [CoRL 2026 -- Main Site](https://www.corl.org/)\n- [CoRL 2026 -- Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 -- Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [CoRL 2026 Conference | OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)\n- [Hugging Face AI Deadlines -- CoRL 2026 update commit](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)"
      }
    ],
    "totalDurationMs": 68382,
    "totalTokens": 16788,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 15321,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 732,
          "cache_read_input_tokens": 15321,
          "cache_creation_input_tokens": 734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 734,
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
  "sourceToolAssistantUUID": "b17d856b-ed3e-4e2a-bc4a-c483337bf8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T05:45:56.276Z_

<details><summary>↩ Tool result · `toolu_01SB26GoMNdM6mNQbbW458AY`</summary>

```text
Here is a comprehensive report of all findings across the nine searches.

---

## 1. Has anyone applied PER or TD-error-based prioritization to imitation learning (not RL)?

**Short answer: Not directly in the pure imitation learning (behavioral cloning) setting.** PER and TD-error prioritization remain firmly rooted in RL. However, there are important adjacent works:

**Hybrid RL+IL methods that use PER with demonstrations:**
- **DQfD (Deep Q-Learning from Demonstrations)** and **DDPGfD** both place expert demonstrations into a prioritized replay buffer alongside self-generated transitions. Demonstrations receive a priority bonus so they are replayed more frequently. However, the learning signal is still RL (TD error), not pure imitation. The demonstrations are never overwritten and the prioritized replay buffer governs the ratio of demo vs. self-generated data. [DQfD paper](https://ar5iv.labs.arxiv.org/html/1704.03732)

- **ExpReS-VLA** (see below) uses a prioritized experience replay buffer during VLA fine-tuning (which is supervised/behavioral cloning), making it the closest example of PER applied during SFT of a large model.

**TD-error in imitation learning contexts:**
- **RIZE (Adaptive Regularization for Imitation Learning)** (arxiv:2502.20089) uses a squared TD regularizer with adaptive targets in an inverse RL / imitation learning framework. It integrates distributional RL into IRL and achieves expert-level performance on complex MuJoCo and Adroit tasks. While this is not PER per se, it directly uses TD error as a learning signal within an imitation learning method. [RIZE](https://arxiv.org/abs/2502.20089)

- **LSIQ** minimizes chi-squared divergence between expert and mixture distributions, resulting in a squared TD error objective for imitation learning.

**Bottom line:** No one has taken vanilla PER (rank transitions by |TD error|, sample proportionally) and applied it to pure behavioral cloning / imitation learning. The concept does not straightforwardly transfer because pure IL lacks a value function and TD error. The closest works either (a) use PER in hybrid RL+IL methods (DQfD, DDPGfD), (b) use TD-error-based regularization within IRL frameworks (RIZE, LSIQ), or (c) use experience replay with priority during VLA fine-tuning (ExpReS-VLA).

---

## 2. Has anyone done adaptive/online data selection during SFT training of VLA or LLM models?

**Yes, several recent papers:**

- **DOTS: Difficulty-Targeted Online Data Selection** (arxiv:2506.05316) -- proposes adaptive difficulty-based online data selection for LLM RL fine-tuning. It prioritizes questions of moderate difficulty that yield the most informative learning signals. Reduces RL fine-tuning time by 23-62%. Note: this is for RL post-training (GRPO), not pure SFT. [DOTS](https://arxiv.org/abs/2506.05316)

- **Prioritized Replay for RL Post-training** (arxiv:2601.02648, Mehdi Fatemi, Jan 2026) -- introduces problem-level prioritization for RL post-training of LLMs. Focuses training on problems that are neither consistently solved nor consistently failed. Compatible with GRPO, PPO, etc. Again, this is RL post-training, not SFT. [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)

- **FreshPER** (see below) -- applies prioritized experience replay to LLM/VLM reinforcement learning, not SFT.

- **FIRE (Fine-Tuning with Integrated Replay & Efficiency)** -- a data-centric framework for efficient adaptation and continual improvement targeting LLMs and code generation. Combines replay, targeted data selection, regularization, and algorithmic innovations for both supervised and RL scenarios. [FIRE](https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire)

- **Holdout-Loss-Based Data Selection for LLM Finetuning** (arxiv:2510.14459) -- uses in-context approximation to estimate holdout loss and dynamically reweight gradient updates during SFT as model parameters evolve. This is one of the clearest examples of adaptive data selection during SFT itself. [Holdout-Loss](https://arxiv.org/html/2510.14459)

- **ExpReS-VLA** (see below) -- uses prioritized experience replay and retrieval-augmented generation during VLA fine-tuning (supervised), making it the most direct example for VLA models.

- **Demo-SCORE** (see below) -- curates demonstration data based on online robot experience, filtering out low-quality demonstrations before policy retraining. This is offline curation between training rounds rather than online selection within a training loop.

**Bottom line:** Adaptive/online data selection during RL post-training of LLMs is an active and growing area (DOTS, Prioritized Replay, FreshPER). For pure SFT, it is less explored but emerging (Holdout-Loss, FIRE). For VLA models specifically, ExpReS-VLA is the standout example.

---

## 3. Verification of specific papers

### "Freshness-Aware Prioritized Experience Replay" -- EXISTS

- **Full title:** "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning"
- **ArXiv:** [2604.16918](https://arxiv.org/abs/2604.16918)
- **Date:** April 18, 2026
- **Authors:** Weiyu Ma, Yongcheng Zeng, Yan Song, Xinyu Cui, Jian Zhao, Xuhui Liu, Mohamed Elhoseiny (KAUST, CASIA, UCL)
- **Key idea:** Standard PER fails for LLMs because rapid policy evolution renders stored priorities stale. FreshPER adds multiplicative exponential age decay to priorities, motivated by effective sample size analysis. Evaluated across 8 environments with 0.5B-7B models; achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs. on-policy baselines.
- **Note:** This is for RL training (REINFORCE++), NOT supervised fine-tuning.

### "ExpReS-VLA" -- EXISTS

- **Full title:** "ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval"
- **ArXiv:** [2511.06202](https://arxiv.org/abs/2511.06202)
- **Date:** November 2025
- **Key idea:** Enables rapid on-device adaptation of pre-trained VLAs (OpenVLA) via compressed experience replay (97% storage reduction by storing vision embeddings instead of raw images) and retrieval-augmented generation. Uses a prioritized experience replay buffer that preserves recently successful trajectories. Introduces Thresholded Hybrid Contrastive Loss (THCL) to learn from both successful and failed demonstrations. Maintains separate circular buffers for successful/failed trajectories.
- **Results:** Improves LIBERO spatial reasoning from 82.6% to 93.1%, long-horizon from 61% to 72.3%. Physical robot: 98% success on in-distribution and OOD tasks (up from 84.7% and 32% with naive fine-tuning). Adapts in 31 seconds with 12 demos on a single RTX 5090.
- **Relevance:** This is the closest paper to "PER applied to SFT of a VLA model" -- it uses prioritized replay during supervised fine-tuning of OpenVLA.

### "Demo-SCORE" -- EXISTS

- **Full title:** "Curating Demonstrations using Online Experience" (Demo-SCORE is the method name)
- **ArXiv:** [2503.03707](https://arxiv.org/abs/2503.03707)
- **Date:** March 5, 2025
- **Authors:** Annie S. Chen, Alec M. Lessing, Yuejiang Liu, Chelsea Finn
- **Venue:** Accepted at RSS 2025 (Robotics: Science and Systems)
- **Project page:** [https://anniesch.github.io/demo-score/](https://anniesch.github.io/demo-score/)
- **Key idea:** Self-curates demonstration datasets via online robot experience. Four-step pipeline: (1) train policy on full demo set, (2) generate rollouts with different checkpoints, (3) train classifier to distinguish success/failure trajectories, (4) filter out unreliable demonstrations. No additional human labeling needed beyond success/failure detection.
- **Results:** 15-35% higher absolute success rate compared to training with all original demonstrations.

---

## Additional relevant papers found

- **Active Robot Curriculum Learning from Online Human Demonstrations** (arxiv:2503.02277, HRI 2025) -- Optimizes query sequence of online demonstrations via curriculum learning, guiding demonstrators to provide demos of gradually increasing difficulty. [Paper](https://arxiv.org/abs/2503.02277)

- **Data Scaling Laws in Imitation Learning for Robotic Manipulation** (OpenReview) -- Comprehensive empirical study on how policy generalization changes with number of training environments, objects, and demonstrations. [Paper](https://openreview.net/forum?id=pISLZG7ktL)

- **pi*_0.6: a VLA That Learns From Experience** (arxiv:2511.14759) -- Related VLA that incorporates online experience into learning. [Paper](https://arxiv.org/abs/2511.14759)

---

## Summary of key findings

| Question | Answer |
|----------|--------|
| PER/TD-error prioritization applied to pure imitation learning? | **No direct application.** Hybrid RL+IL methods (DQfD, DDPGfD) use PER with demo data but still use RL objectives. RIZE/LSIQ use TD error within IRL frameworks. |
| Adaptive/online data selection during SFT of VLA/LLM? | **Emerging area.** ExpReS-VLA uses prioritized replay during VLA SFT. For LLMs, most work targets RL post-training (DOTS, FreshPER, Prioritized Replay). Holdout-Loss and FIRE address SFT more directly. |
| "Freshness-Aware PER" exists? | **Yes.** arxiv:2604.16918, April 2026. For RL training of LLMs/VLMs. |
| "ExpReS-VLA" exists? | **Yes.** arxiv:2511.06202, November 2025. Uses PER during VLA fine-tuning. |
| "Demo-SCORE" exists? | **Yes.** arxiv:2503.03707, March 2025. RSS 2025. Curates demos via online experience. |

Sources:
- [Prioritized Experience Replay (Schaul et al.)](https://arxiv.org/abs/1511.05952)
- [Deep Q-Learning from Demonstrations (DQfD)](https://ar5iv.labs.arxiv.org/html/1704.03732)
- [Understanding PER - Daniel Takeshi](https://danieltakeshi.github.io/2019/07/14/per/)
- [Freshness-Aware PER (FreshPER)](https://arxiv.org/abs/2604.16918)
- [ExpReS-VLA](https://arxiv.org/abs/2511.06202)
- [Demo-SCORE](https://arxiv.org/abs/2503.03707)
- [Demo-SCORE Project Page](https://anniesch.github.io/demo-score/)
- [RIZE: Adaptive Regularization for Imitation Learning](https://arxiv.org/abs/2502.20089)
- [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)
- [DOTS: Difficulty-Targeted Online Data Selection](https://arxiv.org/abs/2506.05316)
- [Holdout-Loss-Based Data Selection for LLM Finetuning](https://arxiv.org/html/2510.14459)
- [FIRE: Fine-Tuning with Integrated Replay & Efficiency](https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire)
- [Active Robot Curriculum Learning](https://arxiv.org/abs/2503.02277)
- [Data Scaling Laws in Imitation Learning](https://openreview.net/forum?id=pISLZG7ktL)
- [pi*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)
- [Dynamic Experience Replay](http://proceedings.mlr.press/v100/luo20a/luo20a.pdf)

agentId: a5721a44efe1d1515 (use SendMessage with to: 'a5721a44efe1d1515' to continue this agent)
&lt;usage>total_tokens: 30666
tool_uses: 19
duration_ms: 142549&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10fe7683-672c-4fa0-901d-2d8c6223515c",
  "isSidechain": false,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "364480d2-de67-48cf-87f8-9cc4cca566b8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me with a literature review. I need to verify whether Prioritized Experience Replay (PER) has been applied to imitation learning or supervised fine-tuning of large models. Search for:\n\n1. \"prioritized experience replay imitation learning\" \n2. \"prioritized replay supervised fine-tuning\"\n3. \"adaptive data sampling imitation learning robot 2025 2026\"\n4. \"experience replay demonstration learning robotics\"\n5. \"TD error imitation learning priority\"\n6. \"curriculum learning demonstration data robot 2025 2026\"\n7. \"Freshness-Aware Prioritized Experience Replay\" (verify this paper exists)\n8. \"ExpReS-VLA\" (verify this paper exists)\n9. \"Demo-SCORE demonstration curation\" (verify this paper exists)\n\nFor each search use WebSearch and report all relevant results with titles, URLs, and descriptions. I specifically need to know:\n- Has anyone applied PER or TD-error-based prioritization to imitation learning (not RL)?\n- Has anyone done adaptive/online data selection during SFT training of VLA or LLM models?\n- Do the papers \"Freshness-Aware PER\", \"ExpReS-VLA\", and \"Demo-SCORE\" actually exist?\n\nBe thorough and report everything you find.",
    "agentId": "a5721a44efe1d1515",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of all findings across the nine searches.\n\n---\n\n## 1. Has anyone applied PER or TD-error-based prioritization to imitation learning (not RL)?\n\n**Short answer: Not directly in the pure imitation learning (behavioral cloning) setting.** PER and TD-error prioritization remain firmly rooted in RL. However, there are important adjacent works:\n\n**Hybrid RL+IL methods that use PER with demonstrations:**\n- **DQfD (Deep Q-Learning from Demonstrations)** and **DDPGfD** both place expert demonstrations into a prioritized replay buffer alongside self-generated transitions. Demonstrations receive a priority bonus so they are replayed more frequently. However, the learning signal is still RL (TD error), not pure imitation. The demonstrations are never overwritten and the prioritized replay buffer governs the ratio of demo vs. self-generated data. [DQfD paper](https://ar5iv.labs.arxiv.org/html/1704.03732)\n\n- **ExpReS-VLA** (see below) uses a prioritized experience replay buffer during VLA fine-tuning (which is supervised/behavioral cloning), making it the closest example of PER applied during SFT of a large model.\n\n**TD-error in imitation learning contexts:**\n- **RIZE (Adaptive Regularization for Imitation Learning)** (arxiv:2502.20089) uses a squared TD regularizer with adaptive targets in an inverse RL / imitation learning framework. It integrates distributional RL into IRL and achieves expert-level performance on complex MuJoCo and Adroit tasks. While this is not PER per se, it directly uses TD error as a learning signal within an imitation learning method. [RIZE](https://arxiv.org/abs/2502.20089)\n\n- **LSIQ** minimizes chi-squared divergence between expert and mixture distributions, resulting in a squared TD error objective for imitation learning.\n\n**Bottom line:** No one has taken vanilla PER (rank transitions by |TD error|, sample proportionally) and applied it to pure behavioral cloning / imitation learning. The concept does not straightforwardly transfer because pure IL lacks a value function and TD error. The closest works either (a) use PER in hybrid RL+IL methods (DQfD, DDPGfD), (b) use TD-error-based regularization within IRL frameworks (RIZE, LSIQ), or (c) use experience replay with priority during VLA fine-tuning (ExpReS-VLA).\n\n---\n\n## 2. Has anyone done adaptive/online data selection during SFT training of VLA or LLM models?\n\n**Yes, several recent papers:**\n\n- **DOTS: Difficulty-Targeted Online Data Selection** (arxiv:2506.05316) -- proposes adaptive difficulty-based online data selection for LLM RL fine-tuning. It prioritizes questions of moderate difficulty that yield the most informative learning signals. Reduces RL fine-tuning time by 23-62%. Note: this is for RL post-training (GRPO), not pure SFT. [DOTS](https://arxiv.org/abs/2506.05316)\n\n- **Prioritized Replay for RL Post-training** (arxiv:2601.02648, Mehdi Fatemi, Jan 2026) -- introduces problem-level prioritization for RL post-training of LLMs. Focuses training on problems that are neither consistently solved nor consistently failed. Compatible with GRPO, PPO, etc. Again, this is RL post-training, not SFT. [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)\n\n- **FreshPER** (see below) -- applies prioritized experience replay to LLM/VLM reinforcement learning, not SFT.\n\n- **FIRE (Fine-Tuning with Integrated Replay & Efficiency)** -- a data-centric framework for efficient adaptation and continual improvement targeting LLMs and code generation. Combines replay, targeted data selection, regularization, and algorithmic innovations for both supervised and RL scenarios. [FIRE](https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire)\n\n- **Holdout-Loss-Based Data Selection for LLM Finetuning** (arxiv:2510.14459) -- uses in-context approximation to estimate holdout loss and dynamically reweight gradient updates during SFT as model parameters evolve. This is one of the clearest examples of adaptive data selection during SFT itself. [Holdout-Loss](https://arxiv.org/html/2510.14459)\n\n- **ExpReS-VLA** (see below) -- uses prioritized experience replay and retrieval-augmented generation during VLA fine-tuning (supervised), making it the most direct example for VLA models.\n\n- **Demo-SCORE** (see below) -- curates demonstration data based on online robot experience, filtering out low-quality demonstrations before policy retraining. This is offline curation between training rounds rather than online selection within a training loop.\n\n**Bottom line:** Adaptive/online data selection during RL post-training of LLMs is an active and growing area (DOTS, Prioritized Replay, FreshPER). For pure SFT, it is less explored but emerging (Holdout-Loss, FIRE). For VLA models specifically, ExpReS-VLA is the standout example.\n\n---\n\n## 3. Verification of specific papers\n\n### \"Freshness-Aware Prioritized Experience Replay\" -- EXISTS\n\n- **Full title:** \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning\"\n- **ArXiv:** [2604.16918](https://arxiv.org/abs/2604.16918)\n- **Date:** April 18, 2026\n- **Authors:** Weiyu Ma, Yongcheng Zeng, Yan Song, Xinyu Cui, Jian Zhao, Xuhui Liu, Mohamed Elhoseiny (KAUST, CASIA, UCL)\n- **Key idea:** Standard PER fails for LLMs because rapid policy evolution renders stored priorities stale. FreshPER adds multiplicative exponential age decay to priorities, motivated by effective sample size analysis. Evaluated across 8 environments with 0.5B-7B models; achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs. on-policy baselines.\n- **Note:** This is for RL training (REINFORCE++), NOT supervised fine-tuning.\n\n### \"ExpReS-VLA\" -- EXISTS\n\n- **Full title:** \"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval\"\n- **ArXiv:** [2511.06202](https://arxiv.org/abs/2511.06202)\n- **Date:** November 2025\n- **Key idea:** Enables rapid on-device adaptation of pre-trained VLAs (OpenVLA) via compressed experience replay (97% storage reduction by storing vision embeddings instead of raw images) and retrieval-augmented generation. Uses a prioritized experience replay buffer that preserves recently successful trajectories. Introduces Thresholded Hybrid Contrastive Loss (THCL) to learn from both successful and failed demonstrations. Maintains separate circular buffers for successful/failed trajectories.\n- **Results:** Improves LIBERO spatial reasoning from 82.6% to 93.1%, long-horizon from 61% to 72.3%. Physical robot: 98% success on in-distribution and OOD tasks (up from 84.7% and 32% with naive fine-tuning). Adapts in 31 seconds with 12 demos on a single RTX 5090.\n- **Relevance:** This is the closest paper to \"PER applied to SFT of a VLA model\" -- it uses prioritized replay during supervised fine-tuning of OpenVLA.\n\n### \"Demo-SCORE\" -- EXISTS\n\n- **Full title:** \"Curating Demonstrations using Online Experience\" (Demo-SCORE is the method name)\n- **ArXiv:** [2503.03707](https://arxiv.org/abs/2503.03707)\n- **Date:** March 5, 2025\n- **Authors:** Annie S. Chen, Alec M. Lessing, Yuejiang Liu, Chelsea Finn\n- **Venue:** Accepted at RSS 2025 (Robotics: Science and Systems)\n- **Project page:** [https://anniesch.github.io/demo-score/](https://anniesch.github.io/demo-score/)\n- **Key idea:** Self-curates demonstration datasets via online robot experience. Four-step pipeline: (1) train policy on full demo set, (2) generate rollouts with different checkpoints, (3) train classifier to distinguish success/failure trajectories, (4) filter out unreliable demonstrations. No additional human labeling needed beyond success/failure detection.\n- **Results:** 15-35% higher absolute success rate compared to training with all original demonstrations.\n\n---\n\n## Additional relevant papers found\n\n- **Active Robot Curriculum Learning from Online Human Demonstrations** (arxiv:2503.02277, HRI 2025) -- Optimizes query sequence of online demonstrations via curriculum learning, guiding demonstrators to provide demos of gradually increasing difficulty. [Paper](https://arxiv.org/abs/2503.02277)\n\n- **Data Scaling Laws in Imitation Learning for Robotic Manipulation** (OpenReview) -- Comprehensive empirical study on how policy generalization changes with number of training environments, objects, and demonstrations. [Paper](https://openreview.net/forum?id=pISLZG7ktL)\n\n- **pi*_0.6: a VLA That Learns From Experience** (arxiv:2511.14759) -- Related VLA that incorporates online experience into learning. [Paper](https://arxiv.org/abs/2511.14759)\n\n---\n\n## Summary of key findings\n\n| Question | Answer |\n|----------|--------|\n| PER/TD-error prioritization applied to pure imitation learning? | **No direct application.** Hybrid RL+IL methods (DQfD, DDPGfD) use PER with demo data but still use RL objectives. RIZE/LSIQ use TD error within IRL frameworks. |\n| Adaptive/online data selection during SFT of VLA/LLM? | **Emerging area.** ExpReS-VLA uses prioritized replay during VLA SFT. For LLMs, most work targets RL post-training (DOTS, FreshPER, Prioritized Replay). Holdout-Loss and FIRE address SFT more directly. |\n| \"Freshness-Aware PER\" exists? | **Yes.** arxiv:2604.16918, April 2026. For RL training of LLMs/VLMs. |\n| \"ExpReS-VLA\" exists? | **Yes.** arxiv:2511.06202, November 2025. Uses PER during VLA fine-tuning. |\n| \"Demo-SCORE\" exists? | **Yes.** arxiv:2503.03707, March 2025. RSS 2025. Curates demos via online experience. |\n\nSources:\n- [Prioritized Experience Replay (Schaul et al.)](https://arxiv.org/abs/1511.05952)\n- [Deep Q-Learning from Demonstrations (DQfD)](https://ar5iv.labs.arxiv.org/html/1704.03732)\n- [Understanding PER - Daniel Takeshi](https://danieltakeshi.github.io/2019/07/14/per/)\n- [Freshness-Aware PER (FreshPER)](https://arxiv.org/abs/2604.16918)\n- [ExpReS-VLA](https://arxiv.org/abs/2511.06202)\n- [Demo-SCORE](https://arxiv.org/abs/2503.03707)\n- [Demo-SCORE Project Page](https://anniesch.github.io/demo-score/)\n- [RIZE: Adaptive Regularization for Imitation Learning](https://arxiv.org/abs/2502.20089)\n- [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)\n- [DOTS: Difficulty-Targeted Online Data Selection](https://arxiv.org/abs/2506.05316)\n- [Holdout-Loss-Based Data Selection for LLM Finetuning](https://arxiv.org/html/2510.14459)\n- [FIRE: Fine-Tuning with Integrated Replay & Efficiency](https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire)\n- [Active Robot Curriculum Learning](https://arxiv.org/abs/2503.02277)\n- [Data Scaling Laws in Imitation Learning](https://openreview.net/forum?id=pISLZG7ktL)\n- [pi*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)\n- [Dynamic Experience Replay](http://proceedings.mlr.press/v100/luo20a/luo20a.pdf)"
      }
    ],
    "totalDurationMs": 142549,
    "totalTokens": 30666,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2646,
      "cache_read_input_tokens": 24813,
      "output_tokens": 3206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2646
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3206,
          "cache_read_input_tokens": 24813,
          "cache_creation_input_tokens": 2646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2646,
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
  "sourceToolAssistantUUID": "10fe7683-672c-4fa0-901d-2d8c6223515c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T05:47:03.844Z_

<details><summary>↩ Tool result · `toolu_01UhQUhAKeCb4asUWLUFo96a`</summary>

```text
I now have a comprehensive picture. Here is my complete literature review report.

---

## Literature Review: Adaptive Data Selection During Training for Imitation Learning / SFT of VLA Models

### Your Idea Summary
Using TD-error-based prioritized experience replay during supervised fine-tuning of Vision-Language-Action models, with a goal-conditioned value function trained via hindsight relabeling to produce priority scores without reward signals.

---

### VERIFIED PAPERS AND METHODS

#### 1. DataMIL (Confirmed to exist)
**Title:** "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels"
**URLs:** [arXiv](https://arxiv.org/abs/2505.09603) | [OpenReview](https://openreview.net/forum?id=AcTsKglDdh) | [Project](https://robin-lab.cs.utexas.edu/datamodels4imitation/)
**Venue:** CoRL 2025
**Description:** Uses datamodels to estimate per-trajectory influence scores on downstream policy performance, then selects a co-training subset from large datasets (e.g., Open X-Embodiment). Validated on 60+ simulation and real-world tasks.
**CRITICAL DISTINCTION: This is STATIC/ONE-TIME selection -- it selects a fixed dataset subset BEFORE the final training run. It does NOT adaptively re-weight samples during the training loop.** The selection process itself is expensive (requires training multiple policies on random subsets to build the datamodel).

#### 2. RINSE (Confirmed to exist)
**Title:** "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning"
**URLs:** [arXiv](https://arxiv.org/abs/2604.23000) | [ICML 2025](https://icml.cc/virtual/2025/48703)
**Venue:** ICML 2025
**Description:** Proposes RINSE (Ranking and INdexing Smooth Examples), which scores demonstrations using trajectory smoothness metrics (Spectral Arc Length and Trajectory-Envelope Distance). SAL filtering achieves 16% higher success with 1/6 the data; TED filtering achieves 20% improvement with half data.
**CRITICAL DISTINCTION: This is also STATIC/PRE-TRAINING filtering -- it scores and filters demonstrations before training begins based on biomechanical smoothness properties. No adaptive/online component.**

---

### MOST CLOSELY RELATED WORK (High Relevance to Your Novelty Claim)

#### 3. ExpReS-VLA -- Experience Replay for VLA Specialization
**Title:** "ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval"
**URL:** [arXiv](https://arxiv.org/abs/2511.06202)
**Date:** November 2025 (revised March 2026)
**Description:** Maintains a memory-efficient experience replay buffer for VLA fine-tuning, storing embeddings from the frozen vision backbone (97% memory reduction). Uses cosine-similarity-based retrieval to augment training batches, and a prioritized replay buffer preserves recently successful trajectories. Includes a novelty term from retrieval distances and per-trajectory weights.
**OVERLAP: This is the closest work to your idea -- it does adaptive replay-based data selection DURING VLA training. However, it uses cosine similarity and recency for prioritization, NOT a TD-error-based value function. No hindsight relabeling or goal-conditioned value function.**

#### 4. V-GPS -- Value-Guided Policy Steering
**Title:** "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance"
**URL:** [arXiv](https://arxiv.org/abs/2410.13816) | [Project](https://nakamotoo.github.io/V-GPS/)
**Venue:** CoRL 2024
**Description:** Trains a value function via offline RL and uses it to re-rank action proposals from generalist robot policies at TEST TIME. Works across 5 different policy architectures and 12 tasks.
**OVERLAP: Uses a learned value function to improve generalist robot policies, but applies it at inference (action re-ranking), NOT during training for data selection. No hindsight relabeling.**

#### 5. Robotic Policy Learning via Human-assisted Action Preference Optimization
**Title:** "Robotic Policy Learning via Human-assisted Action Preference Optimization"
**URL:** [arXiv](https://arxiv.org/html/2506.07127v2)
**Date:** 2025
**Description:** Introduces adaptive per-sample reweighting during SFT of VLA models. Uses decoded continuous actions to estimate L1 loss, with a normalized weighting scheme that increases weight of samples with high action prediction errors. Dynamically modulates sample-wise training weights.
**OVERLAP: Does adaptive per-sample weighting DURING the SFT training loop of VLA models. However, the weighting is based on action prediction error (L1 loss), not a learned value function. No hindsight relabeling or goal conditioning.**

#### 6. PLD -- Self-Improving VLA Models
**Title:** "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL"
**URL:** [arXiv](https://arxiv.org/html/2511.00091v1) | [Project](https://wenlixiao.com/self-improve-VLA-PLD)
**Venue:** ICLR 2026
**Description:** Three-stage framework (Probe, Learn, Distill) that trains residual RL specialists on failure regions, collects distribution-aware data via hybrid rollouts, then distills back into the VLA via SFT. Achieves 99% on LIBERO.
**OVERLAP: Uses RL-based data generation to improve SFT, but the data selection is between stages (not continuously adaptive within the training loop). The RL component generates new data rather than re-weighting existing demonstrations.**

---

### RELATED WORK IN ADJACENT DOMAINS

#### 7. Prioritized Replay for RL Post-training (LLMs)
**Title:** "Prioritized Replay for RL Post-training"
**URL:** [arXiv](https://arxiv.org/abs/2601.02648)
**Date:** January 2026
**Description:** Problem-level prioritization for RL post-training of LLMs. Selects problems based on empirical success statistics -- focuses on problems neither consistently solved nor consistently failed. Continuously adapting, no predefined difficulty tiers or auxiliary predictors needed.
**OVERLAP: Adaptive prioritized sampling during the training loop, but for RL (not SFT), for LLMs (not VLAs), and uses success rate statistics (not a value function).**

#### 8. Freshness-Aware Prioritized Experience Replay for LLM/VLM RL
**Title:** "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning"
**URL:** [arXiv](https://arxiv.org/abs/2604.16918)
**Date:** April 2026
**Description:** Addresses priority staleness in PER for billion-parameter LLMs/VLMs by adding exponential age decay. Claims to be the first successful application of PER to LLM/VLM RL. Achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake.
**OVERLAP: Adaptive prioritized replay during VLM training, but for RL (not SFT/imitation learning). No value function for scoring demonstrations.**

#### 9. AgentHER -- Hindsight Experience Replay for LLM Agents
**Title:** "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling"
**URL:** [arXiv](https://arxiv.org/abs/2603.21357)
**Date:** March 2026
**Description:** Applies hindsight relabeling to LLM agent trajectories -- failed trajectories are relabeled with goals the agent actually achieved, then used for SFT. Improves over success-only SFT by 7.1-11.7 percentage points with 2x data efficiency. 97.7% relabeling precision.
**OVERLAP: Combines hindsight relabeling with SFT, but for LLM agents (not VLA/robotics), and the relabeling augments the dataset rather than producing online priority scores for training.**

#### 10. GRAPE -- Model-Driven SFT Data Selection
**Title:** "The Best Instruction-Tuning Data are Those That Fit"
**URL:** [arXiv](https://arxiv.org/abs/2502.04194) | [OpenReview](https://openreview.net/forum?id=4jFSekBaDT)
**Venue:** NeurIPS 2025 Spotlight
**Description:** For each instruction, gathers responses from various sources and selects the one most aligned with the model's pretrained distribution (measured by normalized probability). Surpasses baselines trained on 4.5x more data.
**DISTINCTION: Static pre-training selection for LLM SFT, not online/adaptive during training.**

#### 11. GoFAR and Goal-Conditioned Offline RL Methods
**Title:** "Offline Goal-Conditioned RL via f-Advantage Regression"
**URL:** [NeurIPS 2022 Paper](https://papers.neurips.cc/paper_files/paper/2022/file/022a39052abf9ca467e268923057dfc0-Paper-Conference.pdf)
**Description:** Automatically obtains optimal goal-weighting without explicit hindsight relabeling. Trains as if all data comes from the optimal goal-conditioned policy.
**OVERLAP: Goal-conditioned value function with implicit hindsight-like properties, but for policy learning (not for producing priority scores for SFT data selection).**

#### 12. Active Robot Curriculum Learning from Online Human Demonstrations
**Title:** "Active Robot Curriculum Learning from Online Human Demonstrations"
**URL:** [arXiv](https://arxiv.org/abs/2503.02277)
**Venue:** HRI 2025
**Description:** Optimizes the query sequence for requesting online demonstrations via curriculum learning -- guides demonstrators to provide demonstrations of gradually increasing difficulty.
**DISTINCTION: Adaptive curriculum for DATA COLLECTION (which demonstrations to request), not for DATA SELECTION during the training loop.**

---

### ASSESSMENT OF YOUR NOVELTY CLAIM

Based on this thorough search, here is my assessment of whether the specific combination -- **TD-error-based prioritized experience replay during SFT of VLA models, with a goal-conditioned value function trained via hindsight relabeling to produce priority scores without reward signals** -- has been done:

**The specific combination appears novel.** No existing work I found combines all of these elements. However, individual components have close precedents:

| Component | Closest Prior Work | Gap from Your Idea |
|---|---|---|
| Adaptive sampling DURING SFT training loop | ExpReS-VLA, Action Preference Optimization | Uses similarity/loss, not a learned value function |
| PER applied to LLM/VLM training | Freshness-Aware PER (Apr 2026) | Applied to RL, not SFT/imitation learning |
| Value function for robot data quality | V-GPS (CoRL 2024) | Used at inference, not for training data selection |
| Hindsight relabeling + SFT | AgentHER (Mar 2026) | For LLM agents, augments data rather than scores priorities |
| Goal-conditioned value for data weighting | GoFAR, RWS | For policy learning, not for prioritizing SFT samples |
| Data selection for robot imitation learning | DataMIL, RINSE | Static/one-time, not adaptive during training |

**The key novelty gap** that remains unfilled: no one has used a goal-conditioned value function (trained with hindsight relabeling from reward-free demonstrations) specifically as a priority scoring mechanism for adaptive sample weighting WITHIN the SFT training loop of VLA models. The closest threats are ExpReS-VLA (does adaptive replay for VLA SFT, but with different prioritization) and Freshness-Aware PER (does PER for VLM training, but in RL not SFT).

**Warning:** ExpReS-VLA (Nov 2025 / Mar 2026) and the Action Preference Optimization paper are quite close and should be cited and carefully differentiated in any paper making this novelty claim.

Sources:
- [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](https://arxiv.org/abs/2505.09603)
- [RINSE: Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning](https://arxiv.org/abs/2604.23000)
- [ExpReS-VLA: Specializing VLA Models Through Experience Replay and Retrieval](https://arxiv.org/abs/2511.06202)
- [V-GPS: Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance](https://arxiv.org/abs/2410.13816)
- [Robotic Policy Learning via Human-assisted Action Preference Optimization](https://arxiv.org/html/2506.07127v2)
- [PLD: Self-Improving VLA Models with Data Generation via Residual RL](https://arxiv.org/html/2511.00091v1)
- [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)
- [Freshness-Aware Prioritized Experience Replay for LLM/VLM RL](https://arxiv.org/abs/2604.16918)
- [AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling](https://arxiv.org/abs/2603.21357)
- [GRAPE: The Best Instruction-Tuning Data are Those That Fit](https://arxiv.org/abs/2502.04194)
- [GoFAR: Offline Goal-Conditioned RL via f-Advantage Regression](https://papers.neurips.cc/paper_files/paper/2022/file/022a39052abf9ca467e268923057dfc0-Paper-Conference.pdf)
- [Active Robot Curriculum Learning from Online Human Demonstrations](https://arxiv.org/abs/2503.02277)
- [Goal-conditioned Imitation Learning (NeurIPS 2019)](https://arxiv.org/abs/1906.05838)
- [Harmonizing SFT and RL (CHORD)](https://arxiv.org/pdf/2508.11408)

agentId: a8bb4e2b3b4ef9dad (use SendMessage with to: 'a8bb4e2b3b4ef9dad' to continue this agent)
&lt;usage>total_tokens: 44854
tool_uses: 33
duration_ms: 200012&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c03ae43-b218-4eff-845d-dedfefdb0e72",
  "isSidechain": false,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "688ba1c5-20cc-4565-b998-b4039695eccc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me with a critical literature review. I need to find work that might be very similar to the following idea: \"Using TD-error based prioritized experience replay during supervised fine-tuning of Vision-Language-Action models, with a goal-conditioned value function trained via hindsight relabeling to produce priority scores without reward signals.\"\n\nSearch specifically for:\n1. \"online data selection SFT training 2025 2026\"\n2. \"adaptive sampling fine-tuning language model 2026\"\n3. \"goal-conditioned value function imitation learning\"\n4. \"hindsight relabeling demonstration quality\"\n5. \"data curriculum robot learning online adaptive 2026\"\n6. \"loss-based sampling training data selection 2026\"\n7. \"self-paced learning imitation learning robotics\"\n8. \"importance sampling demonstration data robot\"\n9. \"RINSE robot imitation noise\" (verify this method exists)\n10. \"DataMIL data selection robot imitation\" (verify this paper exists)\n\nI'm looking for any work that does ADAPTIVE (not static/one-time) data selection during the training loop of imitation learning or SFT. This is the key novelty claim I need to verify.\n\nReport all findings with titles, URLs, and brief descriptions.",
    "agentId": "a8bb4e2b3b4ef9dad",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture. Here is my complete literature review report.\n\n---\n\n## Literature Review: Adaptive Data Selection During Training for Imitation Learning / SFT of VLA Models\n\n### Your Idea Summary\nUsing TD-error-based prioritized experience replay during supervised fine-tuning of Vision-Language-Action models, with a goal-conditioned value function trained via hindsight relabeling to produce priority scores without reward signals.\n\n---\n\n### VERIFIED PAPERS AND METHODS\n\n#### 1. DataMIL (Confirmed to exist)\n**Title:** \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels\"\n**URLs:** [arXiv](https://arxiv.org/abs/2505.09603) | [OpenReview](https://openreview.net/forum?id=AcTsKglDdh) | [Project](https://robin-lab.cs.utexas.edu/datamodels4imitation/)\n**Venue:** CoRL 2025\n**Description:** Uses datamodels to estimate per-trajectory influence scores on downstream policy performance, then selects a co-training subset from large datasets (e.g., Open X-Embodiment). Validated on 60+ simulation and real-world tasks.\n**CRITICAL DISTINCTION: This is STATIC/ONE-TIME selection -- it selects a fixed dataset subset BEFORE the final training run. It does NOT adaptively re-weight samples during the training loop.** The selection process itself is expensive (requires training multiple policies on random subsets to build the datamodel).\n\n#### 2. RINSE (Confirmed to exist)\n**Title:** \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning\"\n**URLs:** [arXiv](https://arxiv.org/abs/2604.23000) | [ICML 2025](https://icml.cc/virtual/2025/48703)\n**Venue:** ICML 2025\n**Description:** Proposes RINSE (Ranking and INdexing Smooth Examples), which scores demonstrations using trajectory smoothness metrics (Spectral Arc Length and Trajectory-Envelope Distance). SAL filtering achieves 16% higher success with 1/6 the data; TED filtering achieves 20% improvement with half data.\n**CRITICAL DISTINCTION: This is also STATIC/PRE-TRAINING filtering -- it scores and filters demonstrations before training begins based on biomechanical smoothness properties. No adaptive/online component.**\n\n---\n\n### MOST CLOSELY RELATED WORK (High Relevance to Your Novelty Claim)\n\n#### 3. ExpReS-VLA -- Experience Replay for VLA Specialization\n**Title:** \"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval\"\n**URL:** [arXiv](https://arxiv.org/abs/2511.06202)\n**Date:** November 2025 (revised March 2026)\n**Description:** Maintains a memory-efficient experience replay buffer for VLA fine-tuning, storing embeddings from the frozen vision backbone (97% memory reduction). Uses cosine-similarity-based retrieval to augment training batches, and a prioritized replay buffer preserves recently successful trajectories. Includes a novelty term from retrieval distances and per-trajectory weights.\n**OVERLAP: This is the closest work to your idea -- it does adaptive replay-based data selection DURING VLA training. However, it uses cosine similarity and recency for prioritization, NOT a TD-error-based value function. No hindsight relabeling or goal-conditioned value function.**\n\n#### 4. V-GPS -- Value-Guided Policy Steering\n**Title:** \"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance\"\n**URL:** [arXiv](https://arxiv.org/abs/2410.13816) | [Project](https://nakamotoo.github.io/V-GPS/)\n**Venue:** CoRL 2024\n**Description:** Trains a value function via offline RL and uses it to re-rank action proposals from generalist robot policies at TEST TIME. Works across 5 different policy architectures and 12 tasks.\n**OVERLAP: Uses a learned value function to improve generalist robot policies, but applies it at inference (action re-ranking), NOT during training for data selection. No hindsight relabeling.**\n\n#### 5. Robotic Policy Learning via Human-assisted Action Preference Optimization\n**Title:** \"Robotic Policy Learning via Human-assisted Action Preference Optimization\"\n**URL:** [arXiv](https://arxiv.org/html/2506.07127v2)\n**Date:** 2025\n**Description:** Introduces adaptive per-sample reweighting during SFT of VLA models. Uses decoded continuous actions to estimate L1 loss, with a normalized weighting scheme that increases weight of samples with high action prediction errors. Dynamically modulates sample-wise training weights.\n**OVERLAP: Does adaptive per-sample weighting DURING the SFT training loop of VLA models. However, the weighting is based on action prediction error (L1 loss), not a learned value function. No hindsight relabeling or goal conditioning.**\n\n#### 6. PLD -- Self-Improving VLA Models\n**Title:** \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\"\n**URL:** [arXiv](https://arxiv.org/html/2511.00091v1) | [Project](https://wenlixiao.com/self-improve-VLA-PLD)\n**Venue:** ICLR 2026\n**Description:** Three-stage framework (Probe, Learn, Distill) that trains residual RL specialists on failure regions, collects distribution-aware data via hybrid rollouts, then distills back into the VLA via SFT. Achieves 99% on LIBERO.\n**OVERLAP: Uses RL-based data generation to improve SFT, but the data selection is between stages (not continuously adaptive within the training loop). The RL component generates new data rather than re-weighting existing demonstrations.**\n\n---\n\n### RELATED WORK IN ADJACENT DOMAINS\n\n#### 7. Prioritized Replay for RL Post-training (LLMs)\n**Title:** \"Prioritized Replay for RL Post-training\"\n**URL:** [arXiv](https://arxiv.org/abs/2601.02648)\n**Date:** January 2026\n**Description:** Problem-level prioritization for RL post-training of LLMs. Selects problems based on empirical success statistics -- focuses on problems neither consistently solved nor consistently failed. Continuously adapting, no predefined difficulty tiers or auxiliary predictors needed.\n**OVERLAP: Adaptive prioritized sampling during the training loop, but for RL (not SFT), for LLMs (not VLAs), and uses success rate statistics (not a value function).**\n\n#### 8. Freshness-Aware Prioritized Experience Replay for LLM/VLM RL\n**Title:** \"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning\"\n**URL:** [arXiv](https://arxiv.org/abs/2604.16918)\n**Date:** April 2026\n**Description:** Addresses priority staleness in PER for billion-parameter LLMs/VLMs by adding exponential age decay. Claims to be the first successful application of PER to LLM/VLM RL. Achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake.\n**OVERLAP: Adaptive prioritized replay during VLM training, but for RL (not SFT/imitation learning). No value function for scoring demonstrations.**\n\n#### 9. AgentHER -- Hindsight Experience Replay for LLM Agents\n**Title:** \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n**URL:** [arXiv](https://arxiv.org/abs/2603.21357)\n**Date:** March 2026\n**Description:** Applies hindsight relabeling to LLM agent trajectories -- failed trajectories are relabeled with goals the agent actually achieved, then used for SFT. Improves over success-only SFT by 7.1-11.7 percentage points with 2x data efficiency. 97.7% relabeling precision.\n**OVERLAP: Combines hindsight relabeling with SFT, but for LLM agents (not VLA/robotics), and the relabeling augments the dataset rather than producing online priority scores for training.**\n\n#### 10. GRAPE -- Model-Driven SFT Data Selection\n**Title:** \"The Best Instruction-Tuning Data are Those That Fit\"\n**URL:** [arXiv](https://arxiv.org/abs/2502.04194) | [OpenReview](https://openreview.net/forum?id=4jFSekBaDT)\n**Venue:** NeurIPS 2025 Spotlight\n**Description:** For each instruction, gathers responses from various sources and selects the one most aligned with the model's pretrained distribution (measured by normalized probability). Surpasses baselines trained on 4.5x more data.\n**DISTINCTION: Static pre-training selection for LLM SFT, not online/adaptive during training.**\n\n#### 11. GoFAR and Goal-Conditioned Offline RL Methods\n**Title:** \"Offline Goal-Conditioned RL via f-Advantage Regression\"\n**URL:** [NeurIPS 2022 Paper](https://papers.neurips.cc/paper_files/paper/2022/file/022a39052abf9ca467e268923057dfc0-Paper-Conference.pdf)\n**Description:** Automatically obtains optimal goal-weighting without explicit hindsight relabeling. Trains as if all data comes from the optimal goal-conditioned policy.\n**OVERLAP: Goal-conditioned value function with implicit hindsight-like properties, but for policy learning (not for producing priority scores for SFT data selection).**\n\n#### 12. Active Robot Curriculum Learning from Online Human Demonstrations\n**Title:** \"Active Robot Curriculum Learning from Online Human Demonstrations\"\n**URL:** [arXiv](https://arxiv.org/abs/2503.02277)\n**Venue:** HRI 2025\n**Description:** Optimizes the query sequence for requesting online demonstrations via curriculum learning -- guides demonstrators to provide demonstrations of gradually increasing difficulty.\n**DISTINCTION: Adaptive curriculum for DATA COLLECTION (which demonstrations to request), not for DATA SELECTION during the training loop.**\n\n---\n\n### ASSESSMENT OF YOUR NOVELTY CLAIM\n\nBased on this thorough search, here is my assessment of whether the specific combination -- **TD-error-based prioritized experience replay during SFT of VLA models, with a goal-conditioned value function trained via hindsight relabeling to produce priority scores without reward signals** -- has been done:\n\n**The specific combination appears novel.** No existing work I found combines all of these elements. However, individual components have close precedents:\n\n| Component | Closest Prior Work | Gap from Your Idea |\n|---|---|---|\n| Adaptive sampling DURING SFT training loop | ExpReS-VLA, Action Preference Optimization | Uses similarity/loss, not a learned value function |\n| PER applied to LLM/VLM training | Freshness-Aware PER (Apr 2026) | Applied to RL, not SFT/imitation learning |\n| Value function for robot data quality | V-GPS (CoRL 2024) | Used at inference, not for training data selection |\n| Hindsight relabeling + SFT | AgentHER (Mar 2026) | For LLM agents, augments data rather than scores priorities |\n| Goal-conditioned value for data weighting | GoFAR, RWS | For policy learning, not for prioritizing SFT samples |\n| Data selection for robot imitation learning | DataMIL, RINSE | Static/one-time, not adaptive during training |\n\n**The key novelty gap** that remains unfilled: no one has used a goal-conditioned value function (trained with hindsight relabeling from reward-free demonstrations) specifically as a priority scoring mechanism for adaptive sample weighting WITHIN the SFT training loop of VLA models. The closest threats are ExpReS-VLA (does adaptive replay for VLA SFT, but with different prioritization) and Freshness-Aware PER (does PER for VLM training, but in RL not SFT).\n\n**Warning:** ExpReS-VLA (Nov 2025 / Mar 2026) and the Action Preference Optimization paper are quite close and should be cited and carefully differentiated in any paper making this novelty claim.\n\nSources:\n- [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](https://arxiv.org/abs/2505.09603)\n- [RINSE: Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning](https://arxiv.org/abs/2604.23000)\n- [ExpReS-VLA: Specializing VLA Models Through Experience Replay and Retrieval](https://arxiv.org/abs/2511.06202)\n- [V-GPS: Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance](https://arxiv.org/abs/2410.13816)\n- [Robotic Policy Learning via Human-assisted Action Preference Optimization](https://arxiv.org/html/2506.07127v2)\n- [PLD: Self-Improving VLA Models with Data Generation via Residual RL](https://arxiv.org/html/2511.00091v1)\n- [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)\n- [Freshness-Aware Prioritized Experience Replay for LLM/VLM RL](https://arxiv.org/abs/2604.16918)\n- [AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling](https://arxiv.org/abs/2603.21357)\n- [GRAPE: The Best Instruction-Tuning Data are Those That Fit](https://arxiv.org/abs/2502.04194)\n- [GoFAR: Offline Goal-Conditioned RL via f-Advantage Regression](https://papers.neurips.cc/paper_files/paper/2022/file/022a39052abf9ca467e268923057dfc0-Paper-Conference.pdf)\n- [Active Robot Curriculum Learning from Online Human Demonstrations](https://arxiv.org/abs/2503.02277)\n- [Goal-conditioned Imitation Learning (NeurIPS 2019)](https://arxiv.org/abs/1906.05838)\n- [Harmonizing SFT and RL (CHORD)](https://arxiv.org/pdf/2508.11408)"
      }
    ],
    "totalDurationMs": 200012,
    "totalTokens": 44854,
    "totalToolUseCount": 33,
    "usage": {
      "input_tokens": 904,
      "cache_creation_input_tokens": 1882,
      "cache_read_input_tokens": 38485,
      "output_tokens": 3583,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1882
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 904,
          "output_tokens": 3583,
          "cache_read_input_tokens": 38485,
          "cache_creation_input_tokens": 1882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1882,
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
      "otherToolCount": 33
    }
  },
  "sourceToolAssistantUUID": "7c03ae43-b218-4eff-845d-dedfefdb0e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
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
  "leafUuid": "688ba1c5-20cc-4565-b998-b4039695eccc",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify adaptive replay priorities for VLA training feasibility",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Assistant

_source line 23 · 2026-05-13T05:47:48.795Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I now have very comprehensive search results. Let me now do a few more targeted searches to verify key claims and look for any remaining gaps:

1. I need to verify whether "Holdout-Loss-Based Data Selection" and "Action Preference Optimization" papers are close enough to threaten novelty
2. I need to check if OpenVLA-OFT is truly the SOTA for open-source manipulation
3. I need to think about the feasibility of the goal-conditioned value function approach

Let me also think about the critical issues:


The CoRL 2026 deadlines are confirmed for May 26 and 29, and I've verified all the cited papers exist. The novelty position looks defensible—while ExpReS-VLA uses prioritized replay during VLA training and Action Preference Optimization does adaptive reweighting with L1 action error, neither uses a value function-based approach like what's being proposed here, so there's meaningful differentiation despite the overlapping concepts.

Now I'm digging into the core technical challenge: using a goal-conditioned value function V(s,g) trained via hindsight relabeling in a reward-free setting. The proposal doesn't clearly address how to define what "goals" actually are in demonstration data, or how you'd generate meaningful TD errors without explicit rewards. If the reward signal is just sparse binary feedback for reaching a goal, most transitions would produce uninformative TD errors, which directly undermines the quality of the prioritization scheme itself.

The second issue is that TD error in this reward-free regime—measuring |γV(s',g) - V(s,g)|—reflects temporal consistency of the value function rather than data quality. High TD error could indicate a poorly trained value function, a genuinely important transition, or just noisy demonstration data, making it unreliable for identifying which transitions the VLA actually needs to focus on.

Finally, there's the computational cost of maintaining and training an auxiliary value function alongside the VLA, adding both memory and compute overhead. overhead (forward passes through V for priority updates)
- The claim of "~5% compute overhead" seems optimistic if you need to recompute priorities every K steps over the full dataset

**Issue 4: ExpReS-VLA is quite close**
ExpReS-VLA already does:
- Prioritized experience replay during VLA fine-tuning
- Online adaptation of replay priorities
- Handles both successful and failed trajectories

The main difference is the prioritization mechanism (cosine similarity vs TD error). Is this difference enough for a separate paper?

**Issue 5: Feasibility within 17 days (CoRL deadline)**
The proposal requires:
- Implementing the goal-conditioned value function with HER
- Integrating it into VLA training pipeline
- Running experiments on LIBERO (4 suites), RoboMimic, and OXE subsets
- Comparing against 5 baselines (SCIZOR, CUPID, DataMIL, Demo-SCORE, uniform) and running ablations

This timeline is extremely tight—even with intensive effort, fitting all this work before the abstract deadline seems unrealistic.

**Issue 6: No real-robot experiments**
While a theoretical foundation for the filtering method might make simulation-only work acceptable, CoRL generally expects real-robot validation. Papers without it face a higher bar for acceptance.

**Issue 7: The theoretical contribution is thin**
The core idea of applying TD error-based prioritization to imitation learning is fairly straightforward, and the theoretical novelty feels limited.

Now I'm scoring the proposal. The novelty is around 3/5—while the specific combination is new, it's incremental since PER is well-established and applying it to VLA fine-tuning with goal-conditioned value functions is a relatively direct extension. ExpReS-VLA and Action Preference Optimization already do similar prioritized replay with different mechanisms, so the gap between this work and existing approaches is narrower than initially claimed.

On feasibility, I'm concerned about the tight 17-day timeline to the abstract deadline, especially given the technical unknowns around implementing the goal-conditioned value function and the computational cost of running five baselines including CUPID. The theoretical foundation is also shaky—there's no clear justification for why TD errors in a reward-free setting would reliably indicate data quality.

The clarity scores reasonably well at 3.5/5 since the idea is well-articulated and the positioning is clear, though the mechanism for how TD errors function as quality signals without explicit rewards needs much deeper explanation. Impact-wise, while data quality for VLAs is genuinely important, the approach feels incremental as a combination of existing techniques, and the practical benefits hinge entirely on whether the TD-error signal actually correlates with downstream performance.

Averaging these out gives me around 3.0, which suggests a revision is needed. Since this is round 1 of 10, there's definitely room to iterate. Let me search for related work on Action Preference Optimization for VLAs to see if there's something closer to what the user is aiming for.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "688ba1c5-20cc-4565-b998-b4039695eccc",
  "isSidechain": false,
  "requestId": "req_011Caz3J3EsyGQMH8Ez4PmYF",
  "type": "assistant",
  "uuid": "af4dad65-4b69-4ca7-be2e-7e213cd3aad2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5JnoaJiCg3qSsxerWysd6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8835,
      "cache_read_input_tokens": 26809,
      "output_tokens": 2381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2381,
          "cache_read_input_tokens": 26809,
          "cache_creation_input_tokens": 8835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8835
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

_source line 24 · 2026-05-13T05:47:48.811Z_

Now let me do a few more targeted searches to pressure-test the novelty claim and verify critical technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4dad65-4b69-4ca7-be2e-7e213cd3aad2",
  "isSidechain": false,
  "requestId": "req_011Caz3J3EsyGQMH8Ez4PmYF",
  "type": "assistant",
  "uuid": "a5f53304-0013-490a-b728-2d3ed998d9d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5JnoaJiCg3qSsxerWysd6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8835,
      "cache_read_input_tokens": 26809,
      "output_tokens": 2381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2381,
          "cache_read_input_tokens": 26809,
          "cache_creation_input_tokens": 8835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8835
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

_source line 25 · 2026-05-13T05:47:52.656Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015hf3GgVbwE5ymrEjaW4DkK`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify close competitors and feasibility",
  "prompt": "I need you to search for several specific things:\n\n1. Search for \"Robotic Policy Learning via Human-assisted Action Preference Optimization\" on arxiv. I need to know: does it do adaptive per-sample reweighting during VLA SFT? How close is it to using TD-error-based priorities? Fetch the paper page if you find it and summarize the method.\n\n2. Search for \"OpenVLA-OFT\" to verify: is OpenVLA-OFT the current open-source SOTA for manipulation VLA fine-tuning? What are its resource requirements?\n\n3. Search for \"loss-based data selection during training deep learning 2025 2026\" - specifically looking for methods that adaptively select training data based on model loss during the training loop (not pre-filtering).\n\n4. Search for \"online hard example mining training\" and \"focal loss adaptive training\" - these are existing methods that do something similar (focus on hard examples during training). How do they compare to the proposed TD-error approach?\n\n5. Search for \"goal conditioned value function hindsight relabeling demonstration data\" to verify if this specific technique has been tried.\n\n6. Search for \"LIBERO benchmark robot manipulation\" to verify what success rates current SOTA achieves.\n\nReport all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f53304-0013-490a-b728-2d3ed998d9d7",
  "isSidechain": false,
  "requestId": "req_011Caz3J3EsyGQMH8Ez4PmYF",
  "type": "assistant",
  "uuid": "1a73572b-b27c-4893-a7a1-216c312ea806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5JnoaJiCg3qSsxerWysd6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8835,
      "cache_read_input_tokens": 26809,
      "output_tokens": 2381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2381,
          "cache_read_input_tokens": 26809,
          "cache_creation_input_tokens": 8835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8835
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

_source line 26 · 2026-05-13T05:47:58.357Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011Kwb6Hc3zreRc9QbUfETC3`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for counter-evidence",
  "prompt": "I need you to search for evidence AGAINST the following idea: \"Using TD-error from a goal-conditioned value function to prioritize demonstration data for VLA training.\"\n\nSpecifically search for:\n\n1. \"prioritized experience replay harmful\" or \"PER failure cases\" - cases where PER hurts performance\n2. \"value function quality demonstration data\" - does the quality of a learned value function correlate with data quality?\n3. \"curriculum learning hurts generalization\" - evidence that adaptive curricula can hurt model generalization\n4. \"hard example mining overfitting\" - evidence that focusing on hard examples causes overfitting\n5. \"experience replay bias correction importance sampling\" - how important is proper bias correction when using PER, and does capped IS correction actually work well?\n6. \"simulation to real gap LIBERO\" or \"LIBERO benchmark limitations\" - limitations of simulation-only evaluation\n\nI'm looking for any evidence that the proposed approach might not work or has fundamental issues. Report all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a73572b-b27c-4893-a7a1-216c312ea806",
  "isSidechain": false,
  "requestId": "req_011Caz3J3EsyGQMH8Ez4PmYF",
  "type": "assistant",
  "uuid": "fb4ca82f-a753-488d-86d2-9b8d12bf706b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5JnoaJiCg3qSsxerWysd6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8835,
      "cache_read_input_tokens": 26809,
      "output_tokens": 2381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2381,
          "cache_read_input_tokens": 26809,
          "cache_creation_input_tokens": 8835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8835
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

_source line 27 · 2026-05-13T05:50:18.018Z_

<details><summary>↩ Tool result · `toolu_011Kwb6Hc3zreRc9QbUfETC3`</summary>

```text
Here is a comprehensive report of evidence against using TD-error from a goal-conditioned value function to prioritize demonstration data for VLA training, organized by the six categories you requested.

---

## 1. Cases Where Prioritized Experience Replay (PER) Hurts Performance

**PER fails in continuous control / actor-critic settings.** Despite success in discrete-action domains (Atari), PER's efficacy in continuous control environments is questionable. High TD-error transitions correspond to regions where the critic's value estimates are inaccurate. In actor-critic methods, oversampling these transitions amplifies gradient variance during policy updates, destabilizing the actor. Research on D-SPEAR (2026) explicitly decouples actor and critic sampling because the critic benefits from high-error samples while the actor benefits from stable, low-error ones -- a direct contradiction to using a single TD-error priority for all learning.

**Priority staleness problem with large models.** Freshness-Aware PER (2026) demonstrates that directly applying PER to billion-parameter models fails because rapid policy evolution renders stored priorities stale. Old high-priority trajectories dominate sampling long after they become uninformative. This is directly relevant to VLAs, which are billion-parameter models.

**PER degrades in noisy/stochastic environments.** PER is most effective when value targets are stable and environment noise is moderate. Performance can degrade or induce catastrophic error spikes in high-noise or function-approximation-heavy environments. Demonstration data from real robots is inherently noisy.

**Loss of diversity.** TD-error-based prioritization results in less diverse samples being replayed. Research on catastrophic forgetting found that experience selection based on TD error did not work well in mitigating forgetting, while selection based on distribution matching and state-space coverage performed comparably to unlimited replay buffers. A more diverse set of samples reduces catastrophic forgetting and leads to more stable performance.

---

## 2. Value Function Quality and Demonstration Data Quality

**Value functions are not the main bottleneck in offline RL.** A key 2024 paper ("Is Value Learning Really the Main Bottleneck in Offline RL?") found that current offline RL methods are often heavily limited by how faithfully the policy is extracted from the value function and how well the policy generalizes on test-time states -- not by the value function quality itself. This undermines the premise that a better value function leads to better data prioritization.

**Bootstrapping error accumulates in offline settings.** Bootstrapping error -- due to bootstrapping from actions outside the training data distribution -- is identified as a key source of instability in offline RL. It accumulates via the Bellman backup operator. A goal-conditioned value function trained on demonstration data would be susceptible to this, making its TD errors unreliable signals for data quality.

**For near-optimal demonstrations, value functions may be unnecessary.** Research shows that when the dataset is near-optimal, simple behavior cloning achieves comparable performance to value-function-based methods. Value functions become necessary mainly when dealing with suboptimal demonstrations. If your demonstration data is already high quality (as is typical for curated robot demonstrations), the value function adds complexity without clear benefit.

---

## 3. Evidence That Adaptive Curricula Hurt Generalization

**"When Do Curricula Work?" (ICLR 2021, Wu, Dyer, Neyshabur).** This landmark paper found that for standard benchmark datasets, curricula have only marginal benefits, and randomly ordered samples perform as well or better than curricula. Any benefit is entirely due to the dynamic training set size, not the ordering. Curricula only help with limited training time budgets or noisy data.

**Convexity argument against curricula.** In standard settings where networks are trained on the same dataset until convergence, curriculum can have no effect because the network converges to a minimum uniquely determined by the final slice of data. This provides a theoretical basis for why TD-error-based ordering may not help.

**Difficulty metric trustworthiness.** The quality of learned representations affects the validity of difficulty metrics. If your value function is imperfect (which it will be, especially early in training), the resulting difficulty ordering can be counterproductive. Numerical problems caused by discretely changing data distributions are also documented.

---

## 4. Hard Example Mining and Overfitting

**Overfitting on hard examples is a documented phenomenon.** The existence of "Smoothing Hard Example Mining" (SHEM) loss functions was specifically motivated by the need to prevent overfitting on hard examples, confirming this is a real and recognized failure mode.

**Memorization of difficult examples.** Research shows that models exhibit memorization among difficult training examples. Hard samples have low accuracy even when included in training, suggesting the model memorizes rather than learns from them.

**Redundant information from too many hard examples.** When too many hard examples are selected, lower-ranked "hard" examples possess a majority of redundant information that harms the model. This suggests that TD-error-based prioritization that over-samples "hard" demonstrations could actually degrade VLA performance.

**Focal loss limitations.** Focal loss (a formalization of hard example mining) is less effective or serves no purpose in cases where the unshared part dominates the loss function. This means hard-example-focused training is not universally beneficial.

---

## 5. Importance Sampling Bias Correction Issues

**Beta annealing is a fragile process.** PER requires annealing the IS correction exponent beta from ~0.4 to 1.0 over training. At beta < 1, the updates are biased toward high-priority samples. Full correction (beta = 1) is only applied near convergence, meaning most of training operates with biased updates. The original PER paper acknowledges this is a compromise.

**Full IS correction can be destabilizing.** Large IS weights can produce disruptive gradient steps in non-linear function approximation because the gradient approximation is only reliable locally. The solution of doing many small updates on high-error transitions is a workaround, not a proper fix.

**Capped/normalized weights do not fully correct bias.** The weights are normalized by 1/max_i(w_i), which prevents very large updates but does not eliminate the distribution mismatch. This means the training objective is not the true data-generating distribution -- for VLA training via supervised learning (behavior cloning), this introduces a systematic bias that may hurt the learned policy.

**The bias matters most when it matters most.** The PER paper notes that unbiased updates are most important near convergence. But for VLA fine-tuning, the entire training may be relatively short, meaning the annealing may never reach full correction, and the model trains under biased conditions throughout.

---

## 6. LIBERO Benchmark Limitations and Sim-to-Real Gap

**LIBERO scores reflect memorization, not understanding.** LIBERO-PRO (2025) found that despite achieving over 90% on the standard LIBERO benchmark, reported scores reflect rote recall rather than genuine task understanding. The current evaluation protocol fails to effectively assess model architectures and algorithms.

**Models collapse under perturbations.** Models with 90%+ success rates nearly collapse under changes to object positions or minor task modifications, even when constructed from training components. Most VLA models remain brittle, showing vulnerability to camera and robot state changes.

**Models ignore language instructions.** LIBERO-Plus found that almost all models ignore the language instructions, and some models execute via bare memorization of the trajectory rather than relying on visual feedback. This means a method validated only on LIBERO may be learning spurious correlations.

**Simulation-specific invariances.** LIBERO's constant simulation environment means all tasks share the same visual renderer, physics engine, and workspace geometry. A policy might develop strategies that exploit simulation-specific invariances rather than building robust physical understanding.

**Real-world conditions are absent.** LIBERO lacks changing visual conditions, new physical environments, and unpredictable task arrival. Any data curation method validated only in LIBERO may not transfer to real-world settings.

---

## Summary of Fundamental Issues with the Proposed Approach

The evidence converges on several fundamental concerns:

1. **TD error is an unreliable prioritization signal** -- it is noisy, subject to bootstrapping error accumulation in offline settings, and becomes stale rapidly in large models.

2. **The approach may reduce data diversity** -- a critical factor for VLA generalization. Research consistently shows diversity of environments and objects is far more important than curating "hard" examples.

3. **The value function itself may be poorly calibrated** -- goal-conditioned value functions struggle with sparse rewards and suffer from overestimation bias, making their TD errors unreliable proxies for data informativeness.

4. **Curricula may not help at all** -- ICLR 2021 showed curricula have marginal benefits in standard settings, and any apparent benefit comes from training set size dynamics, not ordering.

5. **IS bias correction is incomplete in practice** -- capped importance sampling does not fully correct the distribution mismatch, and the annealing schedule may not reach full correction during typical VLA fine-tuning.

6. **LIBERO-only evaluation is insufficient** -- models achieving high scores on LIBERO are memorizing rather than generalizing, making it a poor testbed for validating data curation strategies.

Sources:
- [Freshness-Aware Prioritized Experience Replay for LLM/VLM RL](https://arxiv.org/html/2604.16918)
- [Understanding Prioritized Experience Replay (Daniel Takeshi)](https://danieltakeshi.github.io/2019/07/14/per/)
- [D-SPEAR: Dual-Stream Prioritized Experience Adaptive Replay](https://arxiv.org/html/2603.27346)
- [Enhancing DDPG with Decoupled PER](https://arxiv.org/html/2512.05320)
- [Understanding and Mitigating the Limitations of PER](https://ar5iv.labs.arxiv.org/html/2007.09569)
- [Is Value Learning Really the Main Bottleneck in Offline RL?](https://arxiv.org/html/2406.09329v2)
- [Expert or Not? Assessing Data Quality in Offline RL](https://arxiv.org/html/2510.12638)
- [Stabilizing Off-Policy Q-Learning via Bootstrapping Error Reduction](https://arxiv.org/abs/1906.00949)
- [When Do Curricula Work? (ICLR 2021)](https://openreview.net/forum?id=tW4QEInpni)
- [On The Power of Curriculum Learning in Training Deep Networks](https://arxiv.org/pdf/1904.03626)
- [An Analytical Theory of Curriculum Learning](https://pmc.ncbi.nlm.nih.gov/articles/PMC10561397/)
- [Data Quality in Imitation Learning](https://arxiv.org/abs/2306.02437)
- [Data Scaling Laws in Imitation Learning for Robotic Manipulation](https://arxiv.org/html/2410.18647)
- [Shortcut Learning in Generalist Robot Policies](https://arxiv.org/html/2508.06426)
- [Goal-Conditioned RL: Problems and Solutions](https://ar5iv.labs.arxiv.org/html/2201.08299)
- [Prioritized Experience Replay (Schaul et al., 2015)](https://arxiv.org/abs/1511.05952)
- [LIBERO-PRO: Robust and Fair Evaluation Beyond Memorization](https://arxiv.org/html/2510.03827v1)
- [LIBERO-Plus: In-depth Robustness Analysis of VLA Models](https://arxiv.org/html/2510.13626v1)
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf)
- [Catastrophic Forgetting Mitigation via Discrepancy-Weighted Experience Replay](https://arxiv.org/abs/2507.00042)
- [VLA Models: Concepts, Progress, Applications and Challenges](https://arxiv.org/html/2505.04769v2)
- [Enhancing Generalization in VLA Models by Preserving Pretrained Representations](https://arxiv.org/html/2509.11417v1)
- [Is Behavior Cloning All You Need?](https://arxiv.org/abs/2407.15007)
- [RPE-PER: Reward Prediction Error Prioritisation](https://arxiv.org/html/2501.18093v1)

agentId: a609dd1d85af5ff93 (use SendMessage with to: 'a609dd1d85af5ff93' to continue this agent)
&lt;usage>total_tokens: 27573
tool_uses: 16
duration_ms: 139658&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb4ca82f-a753-488d-86d2-9b8d12bf706b",
  "isSidechain": false,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "3534845e-1838-47b5-ab3e-9bb81a87ac27",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for evidence AGAINST the following idea: \"Using TD-error from a goal-conditioned value function to prioritize demonstration data for VLA training.\"\n\nSpecifically search for:\n\n1. \"prioritized experience replay harmful\" or \"PER failure cases\" - cases where PER hurts performance\n2. \"value function quality demonstration data\" - does the quality of a learned value function correlate with data quality?\n3. \"curriculum learning hurts generalization\" - evidence that adaptive curricula can hurt model generalization\n4. \"hard example mining overfitting\" - evidence that focusing on hard examples causes overfitting\n5. \"experience replay bias correction importance sampling\" - how important is proper bias correction when using PER, and does capped IS correction actually work well?\n6. \"simulation to real gap LIBERO\" or \"LIBERO benchmark limitations\" - limitations of simulation-only evaluation\n\nI'm looking for any evidence that the proposed approach might not work or has fundamental issues. Report all findings.",
    "agentId": "a609dd1d85af5ff93",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of evidence against using TD-error from a goal-conditioned value function to prioritize demonstration data for VLA training, organized by the six categories you requested.\n\n---\n\n## 1. Cases Where Prioritized Experience Replay (PER) Hurts Performance\n\n**PER fails in continuous control / actor-critic settings.** Despite success in discrete-action domains (Atari), PER's efficacy in continuous control environments is questionable. High TD-error transitions correspond to regions where the critic's value estimates are inaccurate. In actor-critic methods, oversampling these transitions amplifies gradient variance during policy updates, destabilizing the actor. Research on D-SPEAR (2026) explicitly decouples actor and critic sampling because the critic benefits from high-error samples while the actor benefits from stable, low-error ones -- a direct contradiction to using a single TD-error priority for all learning.\n\n**Priority staleness problem with large models.** Freshness-Aware PER (2026) demonstrates that directly applying PER to billion-parameter models fails because rapid policy evolution renders stored priorities stale. Old high-priority trajectories dominate sampling long after they become uninformative. This is directly relevant to VLAs, which are billion-parameter models.\n\n**PER degrades in noisy/stochastic environments.** PER is most effective when value targets are stable and environment noise is moderate. Performance can degrade or induce catastrophic error spikes in high-noise or function-approximation-heavy environments. Demonstration data from real robots is inherently noisy.\n\n**Loss of diversity.** TD-error-based prioritization results in less diverse samples being replayed. Research on catastrophic forgetting found that experience selection based on TD error did not work well in mitigating forgetting, while selection based on distribution matching and state-space coverage performed comparably to unlimited replay buffers. A more diverse set of samples reduces catastrophic forgetting and leads to more stable performance.\n\n---\n\n## 2. Value Function Quality and Demonstration Data Quality\n\n**Value functions are not the main bottleneck in offline RL.** A key 2024 paper (\"Is Value Learning Really the Main Bottleneck in Offline RL?\") found that current offline RL methods are often heavily limited by how faithfully the policy is extracted from the value function and how well the policy generalizes on test-time states -- not by the value function quality itself. This undermines the premise that a better value function leads to better data prioritization.\n\n**Bootstrapping error accumulates in offline settings.** Bootstrapping error -- due to bootstrapping from actions outside the training data distribution -- is identified as a key source of instability in offline RL. It accumulates via the Bellman backup operator. A goal-conditioned value function trained on demonstration data would be susceptible to this, making its TD errors unreliable signals for data quality.\n\n**For near-optimal demonstrations, value functions may be unnecessary.** Research shows that when the dataset is near-optimal, simple behavior cloning achieves comparable performance to value-function-based methods. Value functions become necessary mainly when dealing with suboptimal demonstrations. If your demonstration data is already high quality (as is typical for curated robot demonstrations), the value function adds complexity without clear benefit.\n\n---\n\n## 3. Evidence That Adaptive Curricula Hurt Generalization\n\n**\"When Do Curricula Work?\" (ICLR 2021, Wu, Dyer, Neyshabur).** This landmark paper found that for standard benchmark datasets, curricula have only marginal benefits, and randomly ordered samples perform as well or better than curricula. Any benefit is entirely due to the dynamic training set size, not the ordering. Curricula only help with limited training time budgets or noisy data.\n\n**Convexity argument against curricula.** In standard settings where networks are trained on the same dataset until convergence, curriculum can have no effect because the network converges to a minimum uniquely determined by the final slice of data. This provides a theoretical basis for why TD-error-based ordering may not help.\n\n**Difficulty metric trustworthiness.** The quality of learned representations affects the validity of difficulty metrics. If your value function is imperfect (which it will be, especially early in training), the resulting difficulty ordering can be counterproductive. Numerical problems caused by discretely changing data distributions are also documented.\n\n---\n\n## 4. Hard Example Mining and Overfitting\n\n**Overfitting on hard examples is a documented phenomenon.** The existence of \"Smoothing Hard Example Mining\" (SHEM) loss functions was specifically motivated by the need to prevent overfitting on hard examples, confirming this is a real and recognized failure mode.\n\n**Memorization of difficult examples.** Research shows that models exhibit memorization among difficult training examples. Hard samples have low accuracy even when included in training, suggesting the model memorizes rather than learns from them.\n\n**Redundant information from too many hard examples.** When too many hard examples are selected, lower-ranked \"hard\" examples possess a majority of redundant information that harms the model. This suggests that TD-error-based prioritization that over-samples \"hard\" demonstrations could actually degrade VLA performance.\n\n**Focal loss limitations.** Focal loss (a formalization of hard example mining) is less effective or serves no purpose in cases where the unshared part dominates the loss function. This means hard-example-focused training is not universally beneficial.\n\n---\n\n## 5. Importance Sampling Bias Correction Issues\n\n**Beta annealing is a fragile process.** PER requires annealing the IS correction exponent beta from ~0.4 to 1.0 over training. At beta < 1, the updates are biased toward high-priority samples. Full correction (beta = 1) is only applied near convergence, meaning most of training operates with biased updates. The original PER paper acknowledges this is a compromise.\n\n**Full IS correction can be destabilizing.** Large IS weights can produce disruptive gradient steps in non-linear function approximation because the gradient approximation is only reliable locally. The solution of doing many small updates on high-error transitions is a workaround, not a proper fix.\n\n**Capped/normalized weights do not fully correct bias.** The weights are normalized by 1/max_i(w_i), which prevents very large updates but does not eliminate the distribution mismatch. This means the training objective is not the true data-generating distribution -- for VLA training via supervised learning (behavior cloning), this introduces a systematic bias that may hurt the learned policy.\n\n**The bias matters most when it matters most.** The PER paper notes that unbiased updates are most important near convergence. But for VLA fine-tuning, the entire training may be relatively short, meaning the annealing may never reach full correction, and the model trains under biased conditions throughout.\n\n---\n\n## 6. LIBERO Benchmark Limitations and Sim-to-Real Gap\n\n**LIBERO scores reflect memorization, not understanding.** LIBERO-PRO (2025) found that despite achieving over 90% on the standard LIBERO benchmark, reported scores reflect rote recall rather than genuine task understanding. The current evaluation protocol fails to effectively assess model architectures and algorithms.\n\n**Models collapse under perturbations.** Models with 90%+ success rates nearly collapse under changes to object positions or minor task modifications, even when constructed from training components. Most VLA models remain brittle, showing vulnerability to camera and robot state changes.\n\n**Models ignore language instructions.** LIBERO-Plus found that almost all models ignore the language instructions, and some models execute via bare memorization of the trajectory rather than relying on visual feedback. This means a method validated only on LIBERO may be learning spurious correlations.\n\n**Simulation-specific invariances.** LIBERO's constant simulation environment means all tasks share the same visual renderer, physics engine, and workspace geometry. A policy might develop strategies that exploit simulation-specific invariances rather than building robust physical understanding.\n\n**Real-world conditions are absent.** LIBERO lacks changing visual conditions, new physical environments, and unpredictable task arrival. Any data curation method validated only in LIBERO may not transfer to real-world settings.\n\n---\n\n## Summary of Fundamental Issues with the Proposed Approach\n\nThe evidence converges on several fundamental concerns:\n\n1. **TD error is an unreliable prioritization signal** -- it is noisy, subject to bootstrapping error accumulation in offline settings, and becomes stale rapidly in large models.\n\n2. **The approach may reduce data diversity** -- a critical factor for VLA generalization. Research consistently shows diversity of environments and objects is far more important than curating \"hard\" examples.\n\n3. **The value function itself may be poorly calibrated** -- goal-conditioned value functions struggle with sparse rewards and suffer from overestimation bias, making their TD errors unreliable proxies for data informativeness.\n\n4. **Curricula may not help at all** -- ICLR 2021 showed curricula have marginal benefits in standard settings, and any apparent benefit comes from training set size dynamics, not ordering.\n\n5. **IS bias correction is incomplete in practice** -- capped importance sampling does not fully correct the distribution mismatch, and the annealing schedule may not reach full correction during typical VLA fine-tuning.\n\n6. **LIBERO-only evaluation is insufficient** -- models achieving high scores on LIBERO are memorizing rather than generalizing, making it a poor testbed for validating data curation strategies.\n\nSources:\n- [Freshness-Aware Prioritized Experience Replay for LLM/VLM RL](https://arxiv.org/html/2604.16918)\n- [Understanding Prioritized Experience Replay (Daniel Takeshi)](https://danieltakeshi.github.io/2019/07/14/per/)\n- [D-SPEAR: Dual-Stream Prioritized Experience Adaptive Replay](https://arxiv.org/html/2603.27346)\n- [Enhancing DDPG with Decoupled PER](https://arxiv.org/html/2512.05320)\n- [Understanding and Mitigating the Limitations of PER](https://ar5iv.labs.arxiv.org/html/2007.09569)\n- [Is Value Learning Really the Main Bottleneck in Offline RL?](https://arxiv.org/html/2406.09329v2)\n- [Expert or Not? Assessing Data Quality in Offline RL](https://arxiv.org/html/2510.12638)\n- [Stabilizing Off-Policy Q-Learning via Bootstrapping Error Reduction](https://arxiv.org/abs/1906.00949)\n- [When Do Curricula Work? (ICLR 2021)](https://openreview.net/forum?id=tW4QEInpni)\n- [On The Power of Curriculum Learning in Training Deep Networks](https://arxiv.org/pdf/1904.03626)\n- [An Analytical Theory of Curriculum Learning](https://pmc.ncbi.nlm.nih.gov/articles/PMC10561397/)\n- [Data Quality in Imitation Learning](https://arxiv.org/abs/2306.02437)\n- [Data Scaling Laws in Imitation Learning for Robotic Manipulation](https://arxiv.org/html/2410.18647)\n- [Shortcut Learning in Generalist Robot Policies](https://arxiv.org/html/2508.06426)\n- [Goal-Conditioned RL: Problems and Solutions](https://ar5iv.labs.arxiv.org/html/2201.08299)\n- [Prioritized Experience Replay (Schaul et al., 2015)](https://arxiv.org/abs/1511.05952)\n- [LIBERO-PRO: Robust and Fair Evaluation Beyond Memorization](https://arxiv.org/html/2510.03827v1)\n- [LIBERO-Plus: In-depth Robustness Analysis of VLA Models](https://arxiv.org/html/2510.13626v1)\n- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf)\n- [Catastrophic Forgetting Mitigation via Discrepancy-Weighted Experience Replay](https://arxiv.org/abs/2507.00042)\n- [VLA Models: Concepts, Progress, Applications and Challenges](https://arxiv.org/html/2505.04769v2)\n- [Enhancing Generalization in VLA Models by Preserving Pretrained Representations](https://arxiv.org/html/2509.11417v1)\n- [Is Behavior Cloning All You Need?](https://arxiv.org/abs/2407.15007)\n- [RPE-PER: Reward Prediction Error Prioritisation](https://arxiv.org/html/2501.18093v1)"
      }
    ],
    "totalDurationMs": 139658,
    "totalTokens": 27573,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2686,
      "cache_read_input_tokens": 21872,
      "output_tokens": 3014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2686
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3014,
          "cache_read_input_tokens": 21872,
          "cache_creation_input_tokens": 2686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2686,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "fb4ca82f-a753-488d-86d2-9b8d12bf706b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
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
  "leafUuid": "3534845e-1838-47b5-ab3e-9bb81a87ac27",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify adaptive replay priorities for VLA training feasibility",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Tool result

_source line 30 · 2026-05-13T05:50:42.526Z_

<details><summary>↩ Tool result · `toolu_015hf3GgVbwE5ymrEjaW4DkK`</summary>

```text
Now I have comprehensive data for all six queries. Here is my full report:

---

## Report on All Six Searches

### 1. "Robotic Policy Learning via Human-assisted Action Preference Optimization" (HAPO)

**Paper**: arxiv:2506.07127 -- "Human-assisted Robotic Policy Refinement via Action Preference Optimization" (NeurIPS 2025).

**Does it do adaptive per-sample reweighting during VLA SFT?** Yes, but not during standard SFT. It does adaptive per-sample reweighting during a **preference optimization** phase that follows SFT. The method, called APO (Action Preference Optimization), uses a loss-based adaptive reweighting mechanism.

**How the reweighting works:**
- Per-sample weights are computed as normalized L1 loss: **w_i = l_i / sum(l_i)** where l_i is the L1 distance between predicted and ground-truth continuous actions.
- These weights modulate importance-sampling parameters lambda_D and lambda_U:
  - **lambda_D = 1 - exp(-beta_D * w)** for desirable actions
  - **lambda_U = exp(-beta_U * w)** for undesirable actions
- Binary desirability signals are derived from human intervention: policy-executed actions are labeled desirable (c_t=1), human interventions are desirable (c_t=2), and the K=10 steps preceding an intervention are auto-labeled undesirable (c_t=0).
- The APO loss uses an implicit reward model: r_theta(o, a_hat) = log[pi_theta(a_hat|o) / pi_ref(a_hat|o)], with a KL penalty term.

**How close is it to TD-error-based priorities?** Moderately close conceptually -- both use per-sample error signals to weight training, but HAPO uses instantaneous L1 action prediction error in a preference optimization framework, not temporal-difference error. There is no bootstrapping, no value function, and no temporal credit assignment. It is closer to OHEM/focal loss applied within a DPO-like framework than to PER with TD-errors.

**VLA backbones used**: OpenVLA (LoRA rank=32) and pi0-FAST.

**Results**: Moderate -- 48% mean success on RoboMimic simulation (vs 40.5% base, 43.5% KTO), 85% on real-world insertion in-distribution. The focus is on post-deployment refinement from human intervention data, not pushing SOTA on standard benchmarks.

### 2. OpenVLA-OFT -- Open-Source SOTA Status

**Is it the current open-source SOTA for manipulation VLA fine-tuning?** It was briefly, but it has been surpassed. The current picture:

| Method | LIBERO Avg (4 suites) | Note |
|--------|----------------------|------|
| **SimpleVLA-RL** | **~99%** (99.1 reported) | ICLR 2026, RL fine-tuning on top of SFT |
| **RLinf-VLA** | **~98.1%** | RL-based |
| **VITA-VLA** | **~97.3%** | |
| **OpenVLA-OFT** | **97.1%** | SFT-only SOTA |
| Base OpenVLA | 76.5% | |

OpenVLA-OFT remains the **SFT-only open-source SOTA** but RL-augmented methods (SimpleVLA-RL) now exceed it.

**Resource requirements for OpenVLA-OFT:**
- **Training**: 8x A100/H100 GPUs (80GB each), 50K-150K gradient steps, 1-2 days. Minimum 4 GPUs feasible with gradient accumulation. Uses LoRA (no model sharding needed).
- **Training memory**: 25.6-38.6 GB per GPU depending on config (LIBERO 1-image: 25.6 GB; ALOHA 3-image: 38.6 GB).
- **Inference memory**: 15.9-18.0 GB.
- **Key technical recipe**: parallel decoding + action chunking + continuous action representation + L1 regression objective. OFT+ variant adds FiLM for language grounding.

### 3. Loss-Based Data Selection During Training (Online, Not Pre-Filtering)

Several methods exist that adaptively select/reweight training data based on model loss during the training loop:

**a) SuperLoss (NeurIPS 2020):** A generic wrapper loss that monitors each sample's loss during training and dynamically down-weights high-loss (potentially noisy) samples. Implements curriculum learning automatically. No extra hyperparameters. Works across classification, regression, detection, and retrieval.

**b) RHO-LOSS / Reducible Holdout Loss Selection (ICML 2022):** Selects training points that most reduce generalization loss by computing the "reducible loss" = current loss minus an estimated irreducible loss (from a small holdout-trained reference model). Trains in 18x fewer steps on Clothing-1M with 2% higher accuracy. This is the closest existing method to "TD-error-like priorities in supervised learning" -- it explicitly filters out noisy/unlearnable samples (high irreducible loss) and already-learned samples (low reducible loss).

**c) LOW -- Learning Optimal sample Weights (Pattern Recognition 2020):** Learns per-sample weights in the loss function automatically, estimating how much each batch sample should contribute.

**d) Data Selection via Optimal Control (ICLR 2025):** Uses optimal control theory to derive principled data selection for LLM pre-training, operating on the reducible loss component.

**e) Dynamic Data Selection for RL (EMNLP 2025 Findings):** Applies similar principles in RL fine-tuning contexts.

### 4. OHEM and Focal Loss vs. TD-Error-Based Priorities

**Online Hard Example Mining (OHEM) -- CVPR 2016:**
- Selects the highest-loss samples in each mini-batch for gradient computation; discards easy examples entirely.
- Binary: a sample is either used or not. No smooth weighting.
- Originally for object detection (Fast R-CNN). Extended to segmentation, adversarial robustness, semi-supervised learning, NAS.

**Focal Loss -- ICCV 2017 (Lin et al.):**
- Smoothly down-weights well-classified examples via a modulating factor (1-p_t)^gamma.
- Outperforms OHEM by >3 AP on detection benchmarks.
- Unlike OHEM, retains all samples but with continuous weighting. More stable training.
- Adaptive variants exist: AdaFocal (calibration-aware), personality-stratified adaptive FL, and training-progress-aware variants yielding 9-11% F1 gains.

**Comparison to TD-error-based priorities:**

| Aspect | OHEM | Focal Loss | TD-Error PER | Proposed TD-error for SFT |
|--------|------|------------|--------------|--------------------------|
| Selection | Hard threshold (top-K loss) | Smooth continuous weighting | Stochastic proportional to |delta| | Would use prediction error as priority |
| Bias correction | None | Implicit (gamma tuning) | Importance sampling weights | Would need IS correction |
| Temporal structure | None | None | Yes (bootstrapped targets) | Could incorporate trajectory structure |
| Handles noise | Poorly (amplifies noisy labels) | Better (gamma controls) | Poorly without clipping | Depends on implementation |
| Domain | Supervised (detection) | Supervised (detection/general) | RL replay buffers | SFT for VLA |

**Key insight**: OHEM and focal loss are the closest supervised-learning analogs to TD-error-based PER. The main gap is that none of them exploit the **sequential/trajectory** structure of robot demonstration data, which TD-error priorities naturally handle. A TD-error approach for VLA SFT would combine the "focus on hard examples" property with temporal credit assignment -- identifying which timesteps in a trajectory are most informative for learning.

### 5. Goal-Conditioned Value Function + Hindsight Relabeling on Demonstration Data

**Has this specific combination been tried?** Yes, extensively, though typically in RL settings rather than pure imitation learning / VLA fine-tuning:

- **HIQL (NeurIPS 2023):** Offline goal-conditioned RL with hierarchical value functions, learns from demonstration data with hindsight relabeling.
- **How Far I'll Go (Ma et al.):** Offline goal-conditioned RL using f-advantage regression on demonstration datasets.
- **Rethinking GCSL (ICLR 2022):** Established formal connections between goal-conditioned supervised learning and offline RL, showing hindsight relabeling of demos is equivalent to a form of offline RL.
- **Act2Goal (2024-2025):** World-model-based approach initialized from large-scale human demo data, uses HER to relabel its own rollouts. Uses LoRA fine-tuning -- architecturally similar to VLA fine-tuning.
- **GCHR (2025):** Goal-Conditioned Hindsight Regularization -- goes beyond trajectory relabeling, generates action regularization priors from hindsight goals.
- **Reachability Weighted Resampling (2025):** Uses Q-value-based reachability classifiers to re-weight experience by preferentially sampling transitions with achievable goals.

**Gap in the literature**: While these methods are well-explored in RL, they have **not** been applied to VLA (Vision-Language-Action) SFT specifically. The VLA community (OpenVLA, pi0, etc.) still primarily uses uniform SFT on demonstration data. Combining goal-conditioned value estimation with hindsight relabeling to reweight VLA SFT data would be novel.

### 6. LIBERO Benchmark -- Current SOTA Success Rates

**LIBERO** (NeurIPS 2023 Datasets & Benchmarks) has four main task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long.

**Current top results (as of 2025-2026):**

| Method | Spatial | Object | Goal | Long | Average | Type |
|--------|---------|--------|------|------|---------|------|
| **SimpleVLA-RL** | 99.4% | 99.1% | 99.2% | 98.5% | **~99%** | RL fine-tuned VLA |
| **RLinf-VLA** | 99.4% | 99.8% | 98.8% | 94.0% | **~98.1%** | RL fine-tuned |
| **VITA-VLA** | -- | -- | -- | -- | **~97.3%** | |
| **OpenVLA-OFT** | -- | -- | -- | -- | **97.1%** | SFT-only |
| **pi0** | -- | -- | -- | -- | lower | diffusion-based |

**Critical caveats about LIBERO:**
- These high success rates (95%+) reflect performance under clean, near-identical train/test splits with minimal distributional shift.
- Critical analyses have shown that SOTA models collapse to **near-zero success** under moderate task, language, object, or environment perturbations.
- Models often ignore corrupted instructions and default to vision-action patterns from training.
- **LIBERO-PRO** and **LIBERO-Plus** variants have been introduced with controlled perturbations (object color/identity, camera, lighting, noise, language rewrites) for more realistic evaluation.
- RL fine-tuning (SimpleVLA-RL) yields the most dramatic gains: up to **+45 percentage points** on LIBERO-Long over behavior cloning baselines, and can achieve 96.9% average from just **one trajectory per task**.

Sources:
- [HAPO/APO Paper (arxiv:2506.07127)](https://arxiv.org/abs/2506.07127)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [OpenVLA-OFT Paper (arxiv:2502.19645)](https://arxiv.org/abs/2502.19645)
- [SimpleVLA-RL (ICLR 2026)](https://github.com/PRIME-RL/SimpleVLA-RL)
- [OHEM Paper (arxiv:1604.03540)](https://arxiv.org/abs/1604.03540)
- [Focal Loss Paper (ICCV 2017)](https://openaccess.thecvf.com/content_ICCV_2017/papers/Lin_Focal_Loss_for_ICCV_2017_paper.pdf)
- [SuperLoss (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/hash/2cfa8f9e50e0f510ede9d12338a5f564-Abstract.html)
- [RHO-LOSS (ICML 2022)](https://arxiv.org/abs/2206.07137)
- [Prioritized Experience Replay](https://arxiv.org/pdf/1511.05952)
- [LIBERO Benchmark](https://arxiv.org/abs/2306.03310)
- [LIBERO Topic Overview](https://www.emergentmind.com/topics/libero)
- [HIQL (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/6d7c4a0727e089ed6cdd3151cbe8d8ba-Paper-Conference.pdf)
- [GCHR (2025)](https://arxiv.org/html/2508.06108v1)
- [Act2Goal](https://arxiv.org/html/2512.23541v1)
- [Data Selection via Optimal Control (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf)
- [Adaptive Focal Loss](https://www.emergentmind.com/topics/adaptive-focal-loss)
- [LOW: Learning Optimal Sample Weights](https://www.sciencedirect.com/science/article/abs/pii/S0031320320303885)

agentId: ad4c1787f22a258e2 (use SendMessage with to: 'ad4c1787f22a258e2' to continue this agent)
&lt;usage>total_tokens: 33416
tool_uses: 22
duration_ms: 169865&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a73572b-b27c-4893-a7a1-216c312ea806",
  "isSidechain": false,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "type": "user",
  "uuid": "04f8799b-47db-4afd-b76c-5cd42730d283",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for several specific things:\n\n1. Search for \"Robotic Policy Learning via Human-assisted Action Preference Optimization\" on arxiv. I need to know: does it do adaptive per-sample reweighting during VLA SFT? How close is it to using TD-error-based priorities? Fetch the paper page if you find it and summarize the method.\n\n2. Search for \"OpenVLA-OFT\" to verify: is OpenVLA-OFT the current open-source SOTA for manipulation VLA fine-tuning? What are its resource requirements?\n\n3. Search for \"loss-based data selection during training deep learning 2025 2026\" - specifically looking for methods that adaptively select training data based on model loss during the training loop (not pre-filtering).\n\n4. Search for \"online hard example mining training\" and \"focal loss adaptive training\" - these are existing methods that do something similar (focus on hard examples during training). How do they compare to the proposed TD-error approach?\n\n5. Search for \"goal conditioned value function hindsight relabeling demonstration data\" to verify if this specific technique has been tried.\n\n6. Search for \"LIBERO benchmark robot manipulation\" to verify what success rates current SOTA achieves.\n\nReport all findings.",
    "agentId": "ad4c1787f22a258e2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data for all six queries. Here is my full report:\n\n---\n\n## Report on All Six Searches\n\n### 1. \"Robotic Policy Learning via Human-assisted Action Preference Optimization\" (HAPO)\n\n**Paper**: arxiv:2506.07127 -- \"Human-assisted Robotic Policy Refinement via Action Preference Optimization\" (NeurIPS 2025).\n\n**Does it do adaptive per-sample reweighting during VLA SFT?** Yes, but not during standard SFT. It does adaptive per-sample reweighting during a **preference optimization** phase that follows SFT. The method, called APO (Action Preference Optimization), uses a loss-based adaptive reweighting mechanism.\n\n**How the reweighting works:**\n- Per-sample weights are computed as normalized L1 loss: **w_i = l_i / sum(l_i)** where l_i is the L1 distance between predicted and ground-truth continuous actions.\n- These weights modulate importance-sampling parameters lambda_D and lambda_U:\n  - **lambda_D = 1 - exp(-beta_D * w)** for desirable actions\n  - **lambda_U = exp(-beta_U * w)** for undesirable actions\n- Binary desirability signals are derived from human intervention: policy-executed actions are labeled desirable (c_t=1), human interventions are desirable (c_t=2), and the K=10 steps preceding an intervention are auto-labeled undesirable (c_t=0).\n- The APO loss uses an implicit reward model: r_theta(o, a_hat) = log[pi_theta(a_hat|o) / pi_ref(a_hat|o)], with a KL penalty term.\n\n**How close is it to TD-error-based priorities?** Moderately close conceptually -- both use per-sample error signals to weight training, but HAPO uses instantaneous L1 action prediction error in a preference optimization framework, not temporal-difference error. There is no bootstrapping, no value function, and no temporal credit assignment. It is closer to OHEM/focal loss applied within a DPO-like framework than to PER with TD-errors.\n\n**VLA backbones used**: OpenVLA (LoRA rank=32) and pi0-FAST.\n\n**Results**: Moderate -- 48% mean success on RoboMimic simulation (vs 40.5% base, 43.5% KTO), 85% on real-world insertion in-distribution. The focus is on post-deployment refinement from human intervention data, not pushing SOTA on standard benchmarks.\n\n### 2. OpenVLA-OFT -- Open-Source SOTA Status\n\n**Is it the current open-source SOTA for manipulation VLA fine-tuning?** It was briefly, but it has been surpassed. The current picture:\n\n| Method | LIBERO Avg (4 suites) | Note |\n|--------|----------------------|------|\n| **SimpleVLA-RL** | **~99%** (99.1 reported) | ICLR 2026, RL fine-tuning on top of SFT |\n| **RLinf-VLA** | **~98.1%** | RL-based |\n| **VITA-VLA** | **~97.3%** | |\n| **OpenVLA-OFT** | **97.1%** | SFT-only SOTA |\n| Base OpenVLA | 76.5% | |\n\nOpenVLA-OFT remains the **SFT-only open-source SOTA** but RL-augmented methods (SimpleVLA-RL) now exceed it.\n\n**Resource requirements for OpenVLA-OFT:**\n- **Training**: 8x A100/H100 GPUs (80GB each), 50K-150K gradient steps, 1-2 days. Minimum 4 GPUs feasible with gradient accumulation. Uses LoRA (no model sharding needed).\n- **Training memory**: 25.6-38.6 GB per GPU depending on config (LIBERO 1-image: 25.6 GB; ALOHA 3-image: 38.6 GB).\n- **Inference memory**: 15.9-18.0 GB.\n- **Key technical recipe**: parallel decoding + action chunking + continuous action representation + L1 regression objective. OFT+ variant adds FiLM for language grounding.\n\n### 3. Loss-Based Data Selection During Training (Online, Not Pre-Filtering)\n\nSeveral methods exist that adaptively select/reweight training data based on model loss during the training loop:\n\n**a) SuperLoss (NeurIPS 2020):** A generic wrapper loss that monitors each sample's loss during training and dynamically down-weights high-loss (potentially noisy) samples. Implements curriculum learning automatically. No extra hyperparameters. Works across classification, regression, detection, and retrieval.\n\n**b) RHO-LOSS / Reducible Holdout Loss Selection (ICML 2022):** Selects training points that most reduce generalization loss by computing the \"reducible loss\" = current loss minus an estimated irreducible loss (from a small holdout-trained reference model). Trains in 18x fewer steps on Clothing-1M with 2% higher accuracy. This is the closest existing method to \"TD-error-like priorities in supervised learning\" -- it explicitly filters out noisy/unlearnable samples (high irreducible loss) and already-learned samples (low reducible loss).\n\n**c) LOW -- Learning Optimal sample Weights (Pattern Recognition 2020):** Learns per-sample weights in the loss function automatically, estimating how much each batch sample should contribute.\n\n**d) Data Selection via Optimal Control (ICLR 2025):** Uses optimal control theory to derive principled data selection for LLM pre-training, operating on the reducible loss component.\n\n**e) Dynamic Data Selection for RL (EMNLP 2025 Findings):** Applies similar principles in RL fine-tuning contexts.\n\n### 4. OHEM and Focal Loss vs. TD-Error-Based Priorities\n\n**Online Hard Example Mining (OHEM) -- CVPR 2016:**\n- Selects the highest-loss samples in each mini-batch for gradient computation; discards easy examples entirely.\n- Binary: a sample is either used or not. No smooth weighting.\n- Originally for object detection (Fast R-CNN). Extended to segmentation, adversarial robustness, semi-supervised learning, NAS.\n\n**Focal Loss -- ICCV 2017 (Lin et al.):**\n- Smoothly down-weights well-classified examples via a modulating factor (1-p_t)^gamma.\n- Outperforms OHEM by >3 AP on detection benchmarks.\n- Unlike OHEM, retains all samples but with continuous weighting. More stable training.\n- Adaptive variants exist: AdaFocal (calibration-aware), personality-stratified adaptive FL, and training-progress-aware variants yielding 9-11% F1 gains.\n\n**Comparison to TD-error-based priorities:**\n\n| Aspect | OHEM | Focal Loss | TD-Error PER | Proposed TD-error for SFT |\n|--------|------|------------|--------------|--------------------------|\n| Selection | Hard threshold (top-K loss) | Smooth continuous weighting | Stochastic proportional to |delta| | Would use prediction error as priority |\n| Bias correction | None | Implicit (gamma tuning) | Importance sampling weights | Would need IS correction |\n| Temporal structure | None | None | Yes (bootstrapped targets) | Could incorporate trajectory structure |\n| Handles noise | Poorly (amplifies noisy labels) | Better (gamma controls) | Poorly without clipping | Depends on implementation |\n| Domain | Supervised (detection) | Supervised (detection/general) | RL replay buffers | SFT for VLA |\n\n**Key insight**: OHEM and focal loss are the closest supervised-learning analogs to TD-error-based PER. The main gap is that none of them exploit the **sequential/trajectory** structure of robot demonstration data, which TD-error priorities naturally handle. A TD-error approach for VLA SFT would combine the \"focus on hard examples\" property with temporal credit assignment -- identifying which timesteps in a trajectory are most informative for learning.\n\n### 5. Goal-Conditioned Value Function + Hindsight Relabeling on Demonstration Data\n\n**Has this specific combination been tried?** Yes, extensively, though typically in RL settings rather than pure imitation learning / VLA fine-tuning:\n\n- **HIQL (NeurIPS 2023):** Offline goal-conditioned RL with hierarchical value functions, learns from demonstration data with hindsight relabeling.\n- **How Far I'll Go (Ma et al.):** Offline goal-conditioned RL using f-advantage regression on demonstration datasets.\n- **Rethinking GCSL (ICLR 2022):** Established formal connections between goal-conditioned supervised learning and offline RL, showing hindsight relabeling of demos is equivalent to a form of offline RL.\n- **Act2Goal (2024-2025):** World-model-based approach initialized from large-scale human demo data, uses HER to relabel its own rollouts. Uses LoRA fine-tuning -- architecturally similar to VLA fine-tuning.\n- **GCHR (2025):** Goal-Conditioned Hindsight Regularization -- goes beyond trajectory relabeling, generates action regularization priors from hindsight goals.\n- **Reachability Weighted Resampling (2025):** Uses Q-value-based reachability classifiers to re-weight experience by preferentially sampling transitions with achievable goals.\n\n**Gap in the literature**: While these methods are well-explored in RL, they have **not** been applied to VLA (Vision-Language-Action) SFT specifically. The VLA community (OpenVLA, pi0, etc.) still primarily uses uniform SFT on demonstration data. Combining goal-conditioned value estimation with hindsight relabeling to reweight VLA SFT data would be novel.\n\n### 6. LIBERO Benchmark -- Current SOTA Success Rates\n\n**LIBERO** (NeurIPS 2023 Datasets & Benchmarks) has four main task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long.\n\n**Current top results (as of 2025-2026):**\n\n| Method | Spatial | Object | Goal | Long | Average | Type |\n|--------|---------|--------|------|------|---------|------|\n| **SimpleVLA-RL** | 99.4% | 99.1% | 99.2% | 98.5% | **~99%** | RL fine-tuned VLA |\n| **RLinf-VLA** | 99.4% | 99.8% | 98.8% | 94.0% | **~98.1%** | RL fine-tuned |\n| **VITA-VLA** | -- | -- | -- | -- | **~97.3%** | |\n| **OpenVLA-OFT** | -- | -- | -- | -- | **97.1%** | SFT-only |\n| **pi0** | -- | -- | -- | -- | lower | diffusion-based |\n\n**Critical caveats about LIBERO:**\n- These high success rates (95%+) reflect performance under clean, near-identical train/test splits with minimal distributional shift.\n- Critical analyses have shown that SOTA models collapse to **near-zero success** under moderate task, language, object, or environment perturbations.\n- Models often ignore corrupted instructions and default to vision-action patterns from training.\n- **LIBERO-PRO** and **LIBERO-Plus** variants have been introduced with controlled perturbations (object color/identity, camera, lighting, noise, language rewrites) for more realistic evaluation.\n- RL fine-tuning (SimpleVLA-RL) yields the most dramatic gains: up to **+45 percentage points** on LIBERO-Long over behavior cloning baselines, and can achieve 96.9% average from just **one trajectory per task**.\n\nSources:\n- [HAPO/APO Paper (arxiv:2506.07127)](https://arxiv.org/abs/2506.07127)\n- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)\n- [OpenVLA-OFT Paper (arxiv:2502.19645)](https://arxiv.org/abs/2502.19645)\n- [SimpleVLA-RL (ICLR 2026)](https://github.com/PRIME-RL/SimpleVLA-RL)\n- [OHEM Paper (arxiv:1604.03540)](https://arxiv.org/abs/1604.03540)\n- [Focal Loss Paper (ICCV 2017)](https://openaccess.thecvf.com/content_ICCV_2017/papers/Lin_Focal_Loss_for_ICCV_2017_paper.pdf)\n- [SuperLoss (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/hash/2cfa8f9e50e0f510ede9d12338a5f564-Abstract.html)\n- [RHO-LOSS (ICML 2022)](https://arxiv.org/abs/2206.07137)\n- [Prioritized Experience Replay](https://arxiv.org/pdf/1511.05952)\n- [LIBERO Benchmark](https://arxiv.org/abs/2306.03310)\n- [LIBERO Topic Overview](https://www.emergentmind.com/topics/libero)\n- [HIQL (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/6d7c4a0727e089ed6cdd3151cbe8d8ba-Paper-Conference.pdf)\n- [GCHR (2025)](https://arxiv.org/html/2508.06108v1)\n- [Act2Goal](https://arxiv.org/html/2512.23541v1)\n- [Data Selection via Optimal Control (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf)\n- [Adaptive Focal Loss](https://www.emergentmind.com/topics/adaptive-focal-loss)\n- [LOW: Learning Optimal Sample Weights](https://www.sciencedirect.com/science/article/abs/pii/S0031320320303885)"
      }
    ],
    "totalDurationMs": 169865,
    "totalTokens": 33416,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 950,
      "cache_creation_input_tokens": 2007,
      "cache_read_input_tokens": 26917,
      "output_tokens": 3542,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 950,
          "output_tokens": 3542,
          "cache_read_input_tokens": 26917,
          "cache_creation_input_tokens": 2007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2007,
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
  "sourceToolAssistantUUID": "1a73572b-b27c-4893-a7a1-216c312ea806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-13T05:51:20.468Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture. Let me synthesize all the findings and produce my review.

## Key Findings Summary

### Novelty Assessment
The specific combination (TD-error PER + goal-conditioned V-function + HER + VLA SFT) appears novel, BUT:
1. **ExpReS-VLA** already does prioritized replay during VLA SFT (cosine similarity-based)
2. **Action Preference Optimization (HAPO/APO)** does adaptive per-sample reweighting during VLA training (L1 loss-based)
3. **RHO-LOSS** (ICML 2022) does adaptive data selection based on "reducible loss" during supervised training - conceptually very similar


4. **SuperLoss** (NeurIPS 2020) and **Freshness-Aware PER** (April 2026) both use similar per-sample loss monitoring and prioritization strategies for curriculum learning and LLM/VLM training respectively.

The novelty gap is narrower than claimed—the core contribution boils down to applying TD-error-based prioritization from a goal-conditioned value function to VLA supervised fine-tuning, which is more of an engineering adaptation than a fundamental theoretical advance.

### Feasibility Concerns
With only 17 days until the abstract deadline and uncertainty around the goal-conditioned value function's quality, I need to assess whether this is actually achievable.

The approach faces several technical hurdles: bootstrapping errors plague offline settings and make TD errors unreliable as quality signals, there's no theoretical grounding for using TD error as a proxy for data quality, LIBERO's near-saturation at 97-99% accuracy means improvements from data curation will likely be marginal, and PER itself has documented failure modes like reduced diversity and stale priorities that could hurt performance.

Looking at the broader evidence, curriculum learning shows only marginal benefits in standard settings, PER is known to fail in continuous control tasks, LIBERO evaluations don't necessarily measure generalization, and hard example mining risks overfitting. The goal-conditioned value function in offline settings is particularly vulnerable to bootstrapping errors. While data quality for VLAs matters, this specific approach feels incremental, and without real-robot validation, the practical impact remains unclear.

Scoring this honestly: novelty is around 3/5 since the combination is somewhat novel but builds heavily on existing work like ExpReS-VLA and RHO-LOSS, though the TD error insight is interesting if underdeveloped. Feasibility drops to 2/5 given the timeline pressure, technical unknowns around the goal-conditioned value function, the computational cost of running five baselines, and LIBERO's saturation making it hard to demonstrate meaningful gains. The clarity is decent at 3.5/5—the idea is well-articulated with solid landscape analysis, though some aspects need tightening.

The core problem is that this doesn't really address what the user asked for: a filtering method grounded in fundamental theory. Instead it's an engineering adaptation of PER to a new setting, which feels incremental rather than theoretically deep. Impact suffers accordingly at 2.5/5—it's tackling an important problem but the approach is more engineering-focused than theoretical, there's no real robot validation, and LIBERO evaluation is increasingly questioned. Averaging these scores gives 2.75, which points toward revision, but the real question is whether revision is even feasible given the 17-day timeline to abstract deadline. The mismatch between what the user wanted and what this idea delivers, combined with the tight deadline, suggests this might need to be rejected rather than revised.

That said, there are concrete ways to fix this. The core insight about doing adaptive data selection during VLA training rather than static pre-filtering is actually valid and timely. If I could strengthen the theoretical grounding—explaining why TD error from a goal-conditioned value function should correlate with data quality—and either use different benchmarks or simplify the approach to avoid needing a separate value function, this could work. But those are substantial changes, and I'm not confident they're achievable in the time remaining.

The user mentioned they'd accept skipping real robot experiments if the theoretical contribution were strong enough, but that's the problem—the theory here is thin. So I'm stuck: either I need to significantly deepen the theoretical analysis, which is risky on this timeline, or I need to add real robot validation, which is impossible in 17 days. Given those constraints, I'm settling on a feasibility score of 2.5/5.

Looking at my overall assessment: novelty is around 3/5 since the combination is somewhat novel but incremental with several similar prior works like ExpReS-VLA and RHO-LOSS already exploring related ideas. Feasibility drops to 2.5/5 given the timeline pressure and the difficulty of validating on a saturated benchmark. Clarity is decent at 3.5/5—the positioning is solid, but the core mechanism still needs better explanation.

Impact lands at 3/5 because while the problem matters, the current framing reads more as engineering optimization than fundamental contribution, and without real robots or fresh benchmarks, the practical significance is limited.

Averaging these out gives me 3.0, which points toward revision. The core insight about adaptive versus static data selection for vision-language model fine-tuning is sound, but the work needs substantial strengthening in theoretical rigor, clearer differentiation from competitors, a more realistic evaluation plan, and ruthless simplification to actually fit the deadline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04f8799b-47db-4afd-b76c-5cd42730d283",
  "isSidechain": false,
  "requestId": "req_011Caz3aAA44G9EutNHfGJKU",
  "type": "assistant",
  "uuid": "b104c29f-1853-4227-a000-4938adbd571d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tfhoamTmEZhUmJXv8Yp9D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3115,
      "cache_creation_input_tokens": 6019,
      "cache_read_input_tokens": 35644,
      "output_tokens": 3844,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3115,
          "output_tokens": 3844,
          "cache_read_input_tokens": 35644,
          "cache_creation_input_tokens": 6019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6019
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

_source line 32 · 2026-05-13T05:52:10.607Z_

I now have comprehensive evidence. Let me synthesize my findings and deliver the review.

---

Based on extensive independent verification across multiple search dimensions, here is my adversarial review:

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The specific combination (TD-error PER + goal-conditioned V-function + HER for VLA SFT) has not been published, but the novelty gap is narrower than claimed. ExpReS-VLA (arXiv:2511.06202, Nov 2025) already does prioritized experience replay during VLA SFT with cosine-similarity priorities; HAPO/APO (arXiv:2506.07127, NeurIPS 2025) does adaptive per-sample reweighting during VLA training using L1 action error; RHO-LOSS (ICML 2022) performs online loss-based data selection during supervised training via 'reducible loss'; and SuperLoss (NeurIPS 2020) does automatic curriculum learning by monitoring per-sample loss. The contribution reduces to 'replace these simpler priority signals with TD errors from an auxiliary value function,' which is a modest technical delta, not a fundamental theoretical advance."
    },
    "feasibility": {
      "score": 2,
      "rationale": "Critical feasibility issues: (1) 17 days to abstract deadline is extremely tight for an approach with significant unknowns—training a stable goal-conditioned value function offline without rewards is a hard open problem subject to bootstrapping error accumulation (Fujimoto et al. 2019). (2) LIBERO is near-saturated at 97-99% SOTA (OpenVLA-OFT 97.1%, SimpleVLA-RL ~99%), making it very hard to show meaningful improvements from data curation. (3) Reproducing 5 baselines (SCIZOR, CUPID, DataMIL, Demo-SCORE, uniform) in this timeline—some requiring expensive influence function computation—is unrealistic. (4) The ~5% compute overhead claim for periodic TD-error recomputation across the full dataset is optimistic and unvalidated."
    },
    "clarity": {
      "score": 3,
      "rationale": "The positioning (adaptive vs. static data curation) is well-articulated and the landscape analysis is thorough. However, the core mechanism—how TD errors from a goal-conditioned V(s,g) trained without rewards serve as reliable 'data quality' signals—is hand-waved. What defines 'goals' in VLA demonstration data? Why would |γV(s',g) - V(s,g)| identify transitions that are important for VLA learning, as opposed to simply reflecting value function approximation error? This theoretical gap is the heart of the paper and it remains unjustified."
    },
    "impact": {
      "score": 3,
      "rationale": "Data quality for VLA is an important and timely problem (the April 2026 VLA survey confirms this). However, the user specifically requested a contribution 'from a fundamental theoretical perspective' (底层理论角度), and this idea delivers an engineering adaptation of PER to a new setting—not a deep theoretical insight. Without real-robot experiments and given LIBERO's documented memorization issues (LIBERO-PRO 2025, LIBERO-Plus 2025 show SOTA models collapse under perturbations), the empirical impact is also uncertain."
    }
  },
  "issues": [
    "CRITICAL — Theoretical foundation is missing: The paper claims TD error is a natural priority signal for data quality in reward-free imitation learning, but provides no theoretical justification. In RL, TD error measures value estimation surprise; in the proposed reward-free setting, it would measure temporal consistency of an auxiliary value function. There is no established link between this quantity and 'demonstration quality' or 'transition informativeness.' The core claim needs either a formal proof or at minimum a rigorous argument (e.g., connection to Fisher information, gradient magnitude, influence functions).",
    "CRITICAL — ExpReS-VLA (arXiv:2511.06202) is a direct competitor that the Generator insufficiently differentiates: ExpReS-VLA already implements prioritized experience replay during VLA SFT, stores compressed embeddings, and uses similarity-based retrieval to augment training batches. The paper needs to explicitly argue why TD-error priorities are fundamentally better than cosine-similarity priorities, not just different.",
    "CRITICAL — RHO-LOSS (ICML 2022) and SuperLoss (NeurIPS 2020) are missed competitors: RHO-LOSS selects training points that most reduce generalization loss (current loss minus irreducible loss), achieving 18x training speedup. SuperLoss dynamically down-weights high-loss samples. Both do adaptive per-sample reweighting during supervised training without needing an auxiliary value function. The paper must explain why the much more complex value-function approach outperforms these simpler baselines.",
    "MAJOR — LIBERO saturation undermines evaluation: With OpenVLA-OFT at 97.1% and SimpleVLA-RL at ~99%, improvements from data curation on LIBERO will be marginal and within noise. LIBERO-PRO and LIBERO-Plus have exposed these scores as reflecting memorization, not generalization. The evaluation needs a more challenging benchmark (e.g., LIBERO-PRO, RoboMimic multi-human with intentionally noisy data, or real robot).",
    "MAJOR — Counter-evidence from curriculum learning literature: 'When Do Curricula Work?' (ICLR 2021, Wu et al.) found curricula have marginal benefits in standard settings—any benefit is entirely from dynamic training set size, not ordering. PER is known to reduce data diversity (which is critical for VLA generalization per the April 2026 survey), cause overfitting on hard examples, and suffer from stale priorities in billion-parameter models (as documented by Freshness-Aware PER). The paper must address these known failure modes head-on.",
    "MAJOR — Goal-conditioned value function in offline setting is technically risky: Bootstrapping error accumulates in offline RL value estimation (Fujimoto et al. 2019 'BEAR'). With only demonstration data (no online interaction), V(s,g) may develop systematic biases that produce misleading TD errors. The paper's quality rests entirely on this component working reliably.",
    "MINOR — The user requested a 'theoretical perspective on filtering' (底层理论角度提出筛选方法), but this idea is primarily empirical/engineering. Consider reframing around a theoretical contribution, such as deriving the optimal sampling distribution for imitation learning under noisy demonstrations using importance-weighted ERM theory.",
    "MINOR — Cost estimates for baselines are underestimated: CUPID requires training multiple intermediate policies and computing influence functions; DataMIL requires training ~100 subset policies to build datamodels. These alone could consume the entire GPU budget."
  ],
  "feedback": "The core insight—adaptive data selection during VLA SFT outperforms static pre-filtering—is valid and timely. But the current approach is over-engineered and under-theorized. Here are specific revision directions:\n\n1. **Simplify the priority mechanism**: Instead of training an auxiliary goal-conditioned value function (expensive, unstable, theoretically unjustified), consider using the VLA's own training loss as the priority signal. This is essentially RHO-LOSS/SuperLoss adapted for VLA, but the novelty would come from (a) the trajectory-level temporal structure of robot data (aggregate transition-level priorities into trajectory priorities), (b) analyzing why static curation methods fail when the policy changes during training (formally, the optimal data distribution shifts as θ changes), and (c) deriving the theoretically optimal resampling distribution for BC under transition-level noise. This is simpler, more theoretically grounded, and cheaper to implement.\n\n2. **Strengthen theoretical contribution**: Derive WHY adaptive beats static from first principles. For example: under what noise model does the optimal training distribution change with θ? What is the regret bound for static vs adaptive selection? Connection to importance-weighted empirical risk minimization (IW-ERM) would give this paper a theoretical backbone that would justify simulation-only evaluation.\n\n3. **Fix evaluation**: Replace or supplement LIBERO with (a) deliberately noisy/corrupted demonstration datasets where curation matters most, (b) LIBERO-PRO for robustness evaluation, (c) a synthetic study where you control noise levels and can measure the theoretical predictions. This would strengthen the sim-only paper.\n\n4. **Add missed baselines**: Must compare against RHO-LOSS, SuperLoss, and loss-based online data selection. Must differentiate clearly from ExpReS-VLA.\n\n5. **Timeline reality check**: With 17 days to abstract deadline, the current scope (5 baselines, 3 benchmarks, auxiliary value function) is infeasible. A focused contribution—theoretical analysis + one clean empirical validation on a single benchmark with noisy data—is more achievable and potentially more impactful for CoRL.",
  "reason": "Valid problem direction but the approach is over-engineered (auxiliary value function adds complexity without theoretical justification), under-differentiated from close competitors (ExpReS-VLA, RHO-LOSS, SuperLoss), and infeasible within 17 days; needs simplification and stronger theoretical grounding to match the user's stated goal of a theoretically-motivated filtering method."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b104c29f-1853-4227-a000-4938adbd571d",
  "isSidechain": false,
  "requestId": "req_011Caz3aAA44G9EutNHfGJKU",
  "type": "assistant",
  "uuid": "31b4efb2-60d2-4f9a-adab-f920278057c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tfhoamTmEZhUmJXv8Yp9D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3115,
      "cache_creation_input_tokens": 6019,
      "cache_read_input_tokens": 35644,
      "output_tokens": 3844,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3115,
          "output_tokens": 3844,
          "cache_read_input_tokens": 35644,
          "cache_creation_input_tokens": 6019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6019
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "31b4efb2-60d2-4f9a-adab-f920278057c1",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify adaptive replay priorities for VLA training feasibility",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "31b4efb2-60d2-4f9a-adab-f920278057c1",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify adaptive replay priorities for VLA training feasibility",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3"
}
```

---
