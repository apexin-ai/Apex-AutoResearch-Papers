# Research conversation: You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 178
- **Recorded user turns:** 1
- **Tool calls:** 59
- **Original source:** `logs/chats/exported-trajectories/account-3/8fe278e7-14ac-4ebd-98dc-470aaa7c69ee.jsonl`
- **Structured JSON:** [`8b0e770652d1f5e55b8d.json`](../../sessions/8b/8b0e770652d1f5e55b8d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T17:08:19.014Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T17:08:19.014Z",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "content": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.\n\n**Today's date: 2026-05-10 (UTC).** Use this when reasoning about conference deadlines — only recommend venues whose submission deadline has NOT yet passed.\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n这不是快速脑暴——这是一项需要深入研究和严谨思考的任务。你必须像一个资深研究员一样，先充分了解领域现状，再深思熟虑地提出有价值的方向。\n\n### 调研要求\n\n1. **广度**：理想情况下做 10-15 次有针对性的搜索（上下文充裕时尽量多搜，但确保最终能完成输出），覆盖：\n   - 当前 SOTA 方法及其具体性能数字\n   - SOTA 的已知局限和失败场景\n   - 近 12 个月的 survey 论文（掌握领域全貌）\n   - 可迁移的跨领域方法\n   - Benchmark 排行榜（获得定量基准）\n\n2. **深度**：对每个有潜力的方向做追踪调研：\n   - 用 WebFetch 阅读关键论文的核心内容（不只是看搜索结果标题）\n   - 查找独立复现结果来验证论文 claim\n   - 检查你发现的 gap 是否已被最近 3 个月的工作解决\n\n### 思考要求\n\n3. **批判性思维**（在生成每个 idea 之前，先停下来认真思考）：\n   - \"如果我是一个怀疑论的 reviewer，我会质疑什么？\"\n   - \"有没有更简单的 baseline 能达到类似效果？\"\n   - \"这真的解决了一个实际问题，还是只是边际改进？\"\n   - \"这个方向为什么现在可以做，之前为什么没人做？是因为缺少前置条件，还是因为问题不够重要？\"\n\n4. **深度思考**：\n   - 不要从浅层理解出发生成 idea——每个 idea 必须建立在具体论文、具体数字、具体 gap 之上\n   - 思考不同方法之间的联系和矛盾——这往往是创新的来源\n   - 考虑方法的 scalability 和 generalizability，不只是在单个 benchmark 上的效果\n\n充分利用你可用的所有工具——WebSearch 查找论文和趋势，WebFetch 深入阅读关键内容。工具是用来帮助你思考的，不是替代思考的。\n\n## Instructions\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nUse the above search strategy to conduct thorough literature research. For Round 1, focus on: (1) establishing current SOTA with evidence, (2) finding the real gaps (not assumed gaps), (3) discovering concurrent/competing work, (4) cross-domain inspiration.\n\n**Landscape freshness rule**: Your training data may be outdated. When assessing SOTA in the landscape field, ONLY cite methods/results you found via WebSearch in this session — do NOT fall back to pre-training knowledge for what the current best methods or benchmarks are. If your searches don't surface clear SOTA for a direction, add an extra search specifically for \"{topic} benchmark SOTA 2026\" or \"{topic} leaderboard\" before writing the landscape.\n\n## Novelty assessment standard (from novelty-check skill)\nWhen evaluating novelty of each direction via WebSearch:\n| Related papers found | Verdict | Action |\n|:---:|---|---|\n| 0-2 | Novel | Proceed — mark as [待验证] |\n| 3-5 | Existing work | Keep but note: \"Related work: {url}, differentiation: {explanation}\" |\n| >5 | Mature field | Downgrade or pivot — too crowded for novel contribution |\nOnly count DIRECTLY relevant papers (same method + same task), not loosely related ones.\n\n2. Identify concrete research gaps and opportunities based on what you find.\n3. Formulate 3-5 research directions grounded in real evidence from your searches.\n\nNote: You may reference the lab's past project directions if relevant — search for them if you know the context, but do not let past work limit your scope.\n\n**Topic seed from user**: Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:\n  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.\n  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.\n\nOUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.\n\nRecent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.\n\nContribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.\n\nSIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.\n3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.\n\nLook for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.\n\nTag: direction=humanoid_data_gen, contribution_type=method. target_venues=[\"CoRL 2026\"].\n\n\n## Previously rejected directions (do not repeat)\n- LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation [adversarial_fail]\n- Physics-Aware Automated Curation Pipeline for Synthetic Humanoid Loco-Manipulation Data [adversarial_fail]\n- Scene-Conditioned Action-Space Trajectory Diffusion for Humanoid Loco-Manipulation Generalization [adversarial_fail]\n\n## Pattern analysis from past failures\nAnalyze the above failures and identify:\n- What types of ideas tend to fail (common failure_type)\n- What successful ideas (if any) have in common\n- Use this to steer towards more promising directions\n\n## Output format (Round 1)\nAfter completing your research, output a JSON array with your findings. Each element has ONLY these fields:\n{\n  \"title\": \"Concise English title (max 10 words)\",\n  \"core_problem\": \"The fundamental research question this idea addresses (1-2 sentences)\",\n  \"opportunity\": \"The specific gap or 'why now' — what makes this timely (2-3 sentences)\",\n  \"landscape\": \"Current SOTA and its key limitations, grounded in papers you found (3-5 sentences)\"\n}\nIMPORTANT: You MUST end your response with the JSON array. You may include research notes before it, but the JSON array MUST appear at the end."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T17:08:19.018Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T17:08:19.018Z",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

## Round 1

176 recorded events

### User

_source line 3 · 2026-05-10T17:08:19.045Z_

You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.

**Today's date: 2026-05-10 (UTC).** Use this when reasoning about conference deadlines — only recommend venues whose submission deadline has NOT yet passed.

## 核心要求：非常仔细地调研，非常仔细地思考

这不是快速脑暴——这是一项需要深入研究和严谨思考的任务。你必须像一个资深研究员一样，先充分了解领域现状，再深思熟虑地提出有价值的方向。

### 调研要求

1. **广度**：理想情况下做 10-15 次有针对性的搜索（上下文充裕时尽量多搜，但确保最终能完成输出），覆盖：
   - 当前 SOTA 方法及其具体性能数字
   - SOTA 的已知局限和失败场景
   - 近 12 个月的 survey 论文（掌握领域全貌）
   - 可迁移的跨领域方法
   - Benchmark 排行榜（获得定量基准）

2. **深度**：对每个有潜力的方向做追踪调研：
   - 用 WebFetch 阅读关键论文的核心内容（不只是看搜索结果标题）
   - 查找独立复现结果来验证论文 claim
   - 检查你发现的 gap 是否已被最近 3 个月的工作解决

### 思考要求

3. **批判性思维**（在生成每个 idea 之前，先停下来认真思考）：
   - "如果我是一个怀疑论的 reviewer，我会质疑什么？"
   - "有没有更简单的 baseline 能达到类似效果？"
   - "这真的解决了一个实际问题，还是只是边际改进？"
   - "这个方向为什么现在可以做，之前为什么没人做？是因为缺少前置条件，还是因为问题不够重要？"

4. **深度思考**：
   - 不要从浅层理解出发生成 idea——每个 idea 必须建立在具体论文、具体数字、具体 gap 之上
   - 思考不同方法之间的联系和矛盾——这往往是创新的来源
   - 考虑方法的 scalability 和 generalizability，不只是在单个 benchmark 上的效果

充分利用你可用的所有工具——WebSearch 查找论文和趋势，WebFetch 深入阅读关键内容。工具是用来帮助你思考的，不是替代思考的。

## Instructions

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


Use the above search strategy to conduct thorough literature research. For Round 1, focus on: (1) establishing current SOTA with evidence, (2) finding the real gaps (not assumed gaps), (3) discovering concurrent/competing work, (4) cross-domain inspiration.

**Landscape freshness rule**: Your training data may be outdated. When assessing SOTA in the landscape field, ONLY cite methods/results you found via WebSearch in this session — do NOT fall back to pre-training knowledge for what the current best methods or benchmarks are. If your searches don't surface clear SOTA for a direction, add an extra search specifically for "{topic} benchmark SOTA 2026" or "{topic} leaderboard" before writing the landscape.

## Novelty assessment standard (from novelty-check skill)
When evaluating novelty of each direction via WebSearch:
| Related papers found | Verdict | Action |
|:---:|---|---|
| 0-2 | Novel | Proceed — mark as [待验证] |
| 3-5 | Existing work | Keep but note: "Related work: {url}, differentiation: {explanation}" |
| >5 | Mature field | Downgrade or pivot — too crowded for novel contribution |
Only count DIRECTLY relevant papers (same method + same task), not loosely related ones.

2. Identify concrete research gaps and opportunities based on what you find.
3. Formulate 3-5 research directions grounded in real evidence from your searches.

Note: You may reference the lab's past project directions if relevant — search for them if you know the context, but do not let past work limit your scope.

**Topic seed from user**: Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).

Direction: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:
  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.
  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.

OUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.

Recent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.

Contribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.

SIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.
2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.
3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.

Look for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.

Tag: direction=humanoid_data_gen, contribution_type=method. target_venues=["CoRL 2026"].


## Previously rejected directions (do not repeat)
- LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation [adversarial_fail]
- Physics-Aware Automated Curation Pipeline for Synthetic Humanoid Loco-Manipulation Data [adversarial_fail]
- Scene-Conditioned Action-Space Trajectory Diffusion for Humanoid Loco-Manipulation Generalization [adversarial_fail]

## Pattern analysis from past failures
Analyze the above failures and identify:
- What types of ideas tend to fail (common failure_type)
- What successful ideas (if any) have in common
- Use this to steer towards more promising directions

## Output format (Round 1)
After completing your research, output a JSON array with your findings. Each element has ONLY these fields:
{
  "title": "Concise English title (max 10 words)",
  "core_problem": "The fundamental research question this idea addresses (1-2 sentences)",
  "opportunity": "The specific gap or 'why now' — what makes this timely (2-3 sentences)",
  "landscape": "Current SOTA and its key limitations, grounded in papers you found (3-5 sentences)"
}
IMPORTANT: You MUST end your response with the JSON array. You may include research notes before it, but the JSON array MUST appear at the end.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "a243c81d-0fbe-4f23-b89c-8a24072fe224",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T17:08:19.044Z_

```json
{
  "parentUuid": "a243c81d-0fbe-4f23-b89c-8a24072fe224",
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
  "uuid": "6bb6eda2-7d4d-4e56-8ca5-ee366538883d",
  "timestamp": "2026-05-10T17:08:19.044Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T17:08:19.044Z_

```json
{
  "parentUuid": "6bb6eda2-7d4d-4e56-8ca5-ee366538883d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "690e5c80-73f7-40e1-9004-eeac328d4614",
  "timestamp": "2026-05-10T17:08:19.044Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Assistant

_source line 7 · 2026-05-10T17:08:30.199Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. The user wants me to generate novel research directions for CoRL 2026 focused on generative models for humanoid robot training data. Let me break down the key constraints:

1. **Scope**: Generation algorithms OR procedural data-generation pipelines for humanoid robots
2. **Out of scope**: Action retargeting innovations
3. **Previously rejected**: LocoMimicGen, Physics-Aware Curation Pipeline, Scene-Conditioned Action-Space Trajectory Diffusion


4. **Compute**: ≤200 H100-hours
5. **Time**: ≤20 days
6. **Known landscape**: GR00T-Dreams, DexMimicGen, MimicGen extensions, Helix, Cosmos

Looking at why those directions got rejected, I'm noticing a pattern—LocoMimicGen was probably too incremental over existing MimicGen work, the physics curation felt like a filtering approach without enough novelty, and trajectory diffusion overlapped too much with what's already being explored.

All three hit adversarial review failures, which tells me the reviewers found clear weaknesses or insufficient differentiation. Now I need to dig into what's actually happening in the space—searching through current SOTA in humanoid data generation, recent video diffusion approaches for robotics, procedural generation pipelines, physics-aware generative models, and the specific bottlenecks in humanoid data synthesis. Let me start broad and work toward something with real novelty.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690e5c80-73f7-40e1-9004-eeac328d4614",
  "isSidechain": false,
  "requestId": "req_011CauFpP6hFpPk7fDEDSqiy",
  "type": "assistant",
  "uuid": "b5bf4f0a-a04c-4562-b4fc-d5e2c970c1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012t5SWPjTSSAdReAR3ozTLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9009,
      "cache_read_input_tokens": 11804,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 9009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9009
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

_source line 8 · 2026-05-10T17:08:30.202Z_

I'll conduct thorough research on generative models for humanoid robot training data, focusing on generation algorithms and procedural pipelines. Let me start with broad landscape searches across multiple sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5bf4f0a-a04c-4562-b4fc-d5e2c970c1c7",
  "isSidechain": false,
  "requestId": "req_011CauFpP6hFpPk7fDEDSqiy",
  "type": "assistant",
  "uuid": "4786ab02-7bd5-4dba-b694-66e953bf022d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012t5SWPjTSSAdReAR3ozTLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9009,
      "cache_read_input_tokens": 11804,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 9009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9009
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

_source line 9 · 2026-05-10T17:08:30.270Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VRCKxT3gy6xbcW1ZjNhtLs`</summary>

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
  "parentUuid": "4786ab02-7bd5-4dba-b694-66e953bf022d",
  "isSidechain": false,
  "requestId": "req_011CauFpP6hFpPk7fDEDSqiy",
  "type": "assistant",
  "uuid": "aff0f8ba-6089-482d-9a83-b225a82463de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012t5SWPjTSSAdReAR3ozTLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9009,
      "cache_read_input_tokens": 11804,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 9009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9009
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

_source line 10 · 2026-05-10T17:08:30.277Z_

<details><summary>↩ Tool result · `toolu_01VRCKxT3gy6xbcW1ZjNhtLs`</summary>

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
  "parentUuid": "aff0f8ba-6089-482d-9a83-b225a82463de",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "fdcd3121-e14e-4ee4-be99-996a19fcb90c",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "aff0f8ba-6089-482d-9a83-b225a82463de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "fdcd3121-e14e-4ee4-be99-996a19fcb90c",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Assistant

_source line 13 · 2026-05-10T17:08:34.581Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start with multiple parallel searches to establish the landscape efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdcd3121-e14e-4ee4-be99-996a19fcb90c",
  "isSidechain": false,
  "requestId": "req_011CauFqDBfjF9YVMvBZGnmZ",
  "type": "assistant",
  "uuid": "f117d2d8-b9a5-4078-babf-cdb922264870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzM712LutMAgmpeVuKehLG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 20813,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 20813,
          "cache_creation_input_tokens": 1550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1550
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

_source line 14 · 2026-05-10T17:08:39.341Z_

Starting deep research on humanoid data generation landscape. Let me first analyze the failure patterns and then conduct systematic searches.

**Failure pattern analysis**: All three rejected directions got "adversarial_fail" — likely meaning a skeptical reviewer could point to existing work that already covers the core contribution. LocoMimicGen is too close to DexMimicGen; the curation pipeline is incremental; the trajectory diffusion idea has concurrent work. I need to find directions with genuine novelty gaps.

Let me begin with broad landscape searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f117d2d8-b9a5-4078-babf-cdb922264870",
  "isSidechain": false,
  "requestId": "req_011CauFqDBfjF9YVMvBZGnmZ",
  "type": "assistant",
  "uuid": "9cec8a2d-25a0-4e6e-9cc0-b62d2d2aea4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzM712LutMAgmpeVuKehLG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 20813,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 20813,
          "cache_creation_input_tokens": 1550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1550
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

_source line 15 · 2026-05-10T17:08:39.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MKgYEkNMUb25tsoP14Dj2q`</summary>

```json
{
  "query": "humanoid robot training data generation 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cec8a2d-25a0-4e6e-9cc0-b62d2d2aea4d",
  "isSidechain": false,
  "requestId": "req_011CauFqDBfjF9YVMvBZGnmZ",
  "type": "assistant",
  "uuid": "374b3d07-b69d-45e6-b4a9-0d292f21ef8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzM712LutMAgmpeVuKehLG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1550,
      "cache_read_input_tokens": 20813,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 20813,
          "cache_creation_input_tokens": 1550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1550
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

_source line 16 · 2026-05-10T17:08:53.712Z_

<details><summary>↩ Tool result · `toolu_01MKgYEkNMUb25tsoP14Dj2q`</summary>

```text
Web search results for query: "humanoid robot training data generation 2026 survey"

Links: [{"title":"Humanoid Training Data Market Survey Result 2026 - Humanoid.guide","url":"https://humanoid.guide/product/humanoid-training-data-market-survey-result-2026/"},{"title":"Humanoid data: 10 Things That Matter in AI Right Now | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/21/1135656/humanoid-data-robot-training-ai-artificial-intelligence/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Humanoid Training Data Survey - Humanoid.guide","url":"https://humanoid.guide/humanoid-training-data-survey/"},{"title":"The gig workers who are training humanoid robots at home | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/"},{"title":"IEEE survey sheds light on how AI and humanoids will affect robotics in 2026 - The Robot Report","url":"https://www.therobotreport.com/ieee-survey-sheds-light-how-ai-humanoids-will-affect-robotics-2026/"},{"title":"Top AI Datasets for Robotics: What You Need in 2026 - Macgence AI","url":"https://macgence.com/blog/ai-datasets-for-robotics"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"Humanoid robots 2026: The convergence moment | Roland Berger","url":"https://www.rolandberger.com/en/Insights/Publications/Humanoid-robots-why-the-convergence-moment-is-now.html"}]

I found several relevant results about humanoid robot training data generation in 2026. Here's what the search revealed:

## Key Findings from 2026 Surveys

The Humanoid Training Data Market Survey Result 2026 reveals what companies in the humanoid robotics industry are actively looking for in training data. Training data is becoming the limiting factor in humanoid robotics, as hardware is improving fast, AI models are scaling, but without the right data, progress stalls.

## Data Generation Approaches

Companies building humanoid robots have decided that collecting real-world data, as cumbersome as it is, could yield a massive payoff. Videos recorded by gig workers are becoming a key way to train humanoids, with companies like Tesla, Figure AI, and Agility Robotics utilizing gig workers in more than 50 countries who are mounting iPhones on their heads and recording themselves folding laundry, washing dishes, and cooking.

## Technical Specifications Being Standardized

The survey gathers input such as required video resolutions (from 480p to 4K), sensory modalities—such as touch-sensitive gloves—and the pricing models that will support the next generation of datasets.

## Market Impact

The average cost per hour of high-quality teleoperation data fell from $340/hour in early 2024 to $118/hour as of March 2026 — a 60% decrease.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "374b3d07-b69d-45e6-b4a9-0d292f21ef8c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "c10f4dbf-c91f-4519-bcb4-718765371908",
  "toolUseResult": {
    "query": "humanoid robot training data generation 2026 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PWghkpgikxky1ngnKhHqiT",
        "content": [
          {
            "title": "Humanoid Training Data Market Survey Result 2026 - Humanoid.guide",
            "url": "https://humanoid.guide/product/humanoid-training-data-market-survey-result-2026/"
          },
          {
            "title": "Humanoid data: 10 Things That Matter in AI Right Now | MIT Technology Review",
            "url": "https://www.technologyreview.com/2026/04/21/1135656/humanoid-data-robot-training-ai-artificial-intelligence/"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Humanoid Training Data Survey - Humanoid.guide",
            "url": "https://humanoid.guide/humanoid-training-data-survey/"
          },
          {
            "title": "The gig workers who are training humanoid robots at home | MIT Technology Review",
            "url": "https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/"
          },
          {
            "title": "IEEE survey sheds light on how AI and humanoids will affect robotics in 2026 - The Robot Report",
            "url": "https://www.therobotreport.com/ieee-survey-sheds-light-how-ai-humanoids-will-affect-robotics-2026/"
          },
          {
            "title": "Top AI Datasets for Robotics: What You Need in 2026 - Macgence AI",
            "url": "https://macgence.com/blog/ai-datasets-for-robotics"
          },
          {
            "title": "State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/state-of-robotics-2026"
          },
          {
            "title": "Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation",
            "url": "https://arxiv.org/html/2510.08807v1"
          },
          {
            "title": "Humanoid robots 2026: The convergence moment | Roland Berger",
            "url": "https://www.rolandberger.com/en/Insights/Publications/Humanoid-robots-why-the-convergence-moment-is-now.html"
          }
        ]
      },
      "I found several relevant results about humanoid robot training data generation in 2026. Here's what the search revealed:\n\n## Key Findings from 2026 Surveys\n\nThe Humanoid Training Data Market Survey Result 2026 reveals what companies in the humanoid robotics industry are actively looking for in training data. Training data is becoming the limiting factor in humanoid robotics, as hardware is improving fast, AI models are scaling, but without the right data, progress stalls.\n\n## Data Generation Approaches\n\nCompanies building humanoid robots have decided that collecting real-world data, as cumbersome as it is, could yield a massive payoff. Videos recorded by gig workers are becoming a key way to train humanoids, with companies like Tesla, Figure AI, and Agility Robotics utilizing gig workers in more than 50 countries who are mounting iPhones on their heads and recording themselves folding laundry, washing dishes, and cooking.\n\n## Technical Specifications Being Standardized\n\nThe survey gathers input such as required video resolutions (from 480p to 4K), sensory modalities—such as touch-sensitive gloves—and the pricing models that will support the next generation of datasets.\n\n## Market Impact\n\nThe average cost per hour of high-quality teleoperation data fell from $340/hour in early 2024 to $118/hour as of March 2026 — a 60% decrease."
    ],
    "durationSeconds": 14.045770511000002
  },
  "sourceToolAssistantUUID": "374b3d07-b69d-45e6-b4a9-0d292f21ef8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T17:08:56.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016tF41bsqLjVtQqtpSE3P1c`</summary>

```json
{
  "query": "GR00T-Dreams NVIDIA humanoid synthetic data generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c10f4dbf-c91f-4519-bcb4-718765371908",
  "isSidechain": false,
  "requestId": "req_011CauFrw9ZyTJi4AtnxZJmK",
  "type": "assistant",
  "uuid": "c89c000c-5417-48f1-aef6-10ffbe6ff093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFvCgtuywDr86HdZPAKtHv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 22363,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 22363,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1130
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

_source line 18 · 2026-05-10T17:09:02.688Z_

<details><summary>↩ Tool result · `toolu_016tF41bsqLjVtQqtpSE3P1c`</summary>

```text
Web search results for query: "GR00T-Dreams NVIDIA humanoid synthetic data generation 2025 2026"

Links: [{"title":"Enhance Robot Learning with Synthetic Trajectory Data Generated by World Foundation Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/"},{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer","url":"https://developer.nvidia.com/isaac/gr00t"},{"title":"NVIDIA Powers Humanoid Robot Industry With Cloud-to-Robot Computing Platforms for Physical AI | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-powers-humanoid-robot-industry-with-cloud-to-robot-computing-platforms-for-physical-ai"},{"title":"NVIDIA Announces Isaac GR00T Blueprint to Accelerate Humanoid Robotics Development | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/isaac-gr00t-blueprint-humanoid-robotics/"},{"title":"NVIDIA Humanoid Robotics: Building the Next-Gen Infrastructure? - Futurum","url":"https://futurumgroup.com/insights/is-nvidia-building-the-defining-infrastructure-for-humanoid-robotics/"},{"title":"Nvidia forges ahead on humanoid development, reveals Isaac GR00T N1.5, Isaac GR00T-Dreams and more - The Tech Portal","url":"https://thetechportal.com/2025/05/20/nvidia-forges-ahead-on-humanoid-development-reveals-isaac-gr00t-n1-5-isaac-gr00t-dreams-and-more/"},{"title":"NVIDIA releases cloud-to-robot computing platforms for physical AI, humanoid development - The Robot Report","url":"https://www.therobotreport.com/nvidia-cloud-robot-computing-platforms-physical-ai-humanoid-development/"},{"title":"Use Case: NVIDIA Computing Platforms for Humanoid Robots","url":"https://www.nvidia.com/en-us/use-cases/humanoid-robots/"},{"title":"NVIDIA Announces Isaac GR00T N1 — the World’s First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development | NVIDIA Newsroom","url":"https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"}]

Based on the search results, here's what I found about GR00T-Dreams and NVIDIA's humanoid synthetic data generation:

## Overview

The NVIDIA Isaac GR00T-Dreams blueprint generates massive synthetic trajectory data from a single image and language prompt, reducing the need for extensive human demonstrations in training humanoid robots.

## How It Works

Using a single image as the input, GR00T-Dreams generates videos of the robot performing new tasks in new environments, then extracts action tokens — compressed, digestible pieces of data — that are used to teach robots how to perform these new tasks.

## Development Timeline (2025-2026)

Using the GR00T-Dreams blueprint, NVIDIA Research developed GR00T N1.5, an update to the world's first open foundation model for generalized humanoid robot reasoning and skills, in just 36 hours, a task that would have taken nearly three months with manual data collection.

The dataset now includes thousands of new robotics trajectories, featuring the first real-world training data from the Unitree G1 robot and 24,000 simulated teleoperation trajectories.

## Key Capabilities

The GR00T-Dreams blueprint enables robots to generalize across behaviors, adapt to new environments, and learn novel actions from language instructions, even with training data from only a single task.

## Technical Foundation

The NVIDIA Isaac GR00T-Dreams blueprint, built on NVIDIA Cosmos, solves this challenge by generating massive synthetic trajectory data from just a single image and language prompt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c89c000c-5417-48f1-aef6-10ffbe6ff093",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "acdc3456-6adc-45ea-8403-bcdea476ae8f",
  "toolUseResult": {
    "query": "GR00T-Dreams NVIDIA humanoid synthetic data generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014AwhMLRf7JMhXda9HSav37",
        "content": [
          {
            "title": "Enhance Robot Learning with Synthetic Trajectory Data Generated by World Foundation Models | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/"
          },
          {
            "title": "Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"
          },
          {
            "title": "Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer",
            "url": "https://developer.nvidia.com/isaac/gr00t"
          },
          {
            "title": "NVIDIA Powers Humanoid Robot Industry With Cloud-to-Robot Computing Platforms for Physical AI | NVIDIA Newsroom",
            "url": "https://nvidianews.nvidia.com/news/nvidia-powers-humanoid-robot-industry-with-cloud-to-robot-computing-platforms-for-physical-ai"
          },
          {
            "title": "NVIDIA Announces Isaac GR00T Blueprint to Accelerate Humanoid Robotics Development | NVIDIA Blog",
            "url": "https://blogs.nvidia.com/blog/isaac-gr00t-blueprint-humanoid-robotics/"
          },
          {
            "title": "NVIDIA Humanoid Robotics: Building the Next-Gen Infrastructure? - Futurum",
            "url": "https://futurumgroup.com/insights/is-nvidia-building-the-defining-infrastructure-for-humanoid-robotics/"
          },
          {
            "title": "Nvidia forges ahead on humanoid development, reveals Isaac GR00T N1.5, Isaac GR00T-Dreams and more - The Tech Portal",
            "url": "https://thetechportal.com/2025/05/20/nvidia-forges-ahead-on-humanoid-development-reveals-isaac-gr00t-n1-5-isaac-gr00t-dreams-and-more/"
          },
          {
            "title": "NVIDIA releases cloud-to-robot computing platforms for physical AI, humanoid development - The Robot Report",
            "url": "https://www.therobotreport.com/nvidia-cloud-robot-computing-platforms-physical-ai-humanoid-development/"
          },
          {
            "title": "Use Case: NVIDIA Computing Platforms for Humanoid Robots",
            "url": "https://www.nvidia.com/en-us/use-cases/humanoid-robots/"
          },
          {
            "title": "NVIDIA Announces Isaac GR00T N1 — the World’s First Open Humanoid Robot Foundation Model — and Simulation Frameworks to Speed Robot Development | NVIDIA Newsroom",
            "url": "https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"
          }
        ]
      },
      "Based on the search results, here's what I found about GR00T-Dreams and NVIDIA's humanoid synthetic data generation:\n\n## Overview\n\nThe NVIDIA Isaac GR00T-Dreams blueprint generates massive synthetic trajectory data from a single image and language prompt, reducing the need for extensive human demonstrations in training humanoid robots.\n\n## How It Works\n\nUsing a single image as the input, GR00T-Dreams generates videos of the robot performing new tasks in new environments, then extracts action tokens — compressed, digestible pieces of data — that are used to teach robots how to perform these new tasks.\n\n## Development Timeline (2025-2026)\n\nUsing the GR00T-Dreams blueprint, NVIDIA Research developed GR00T N1.5, an update to the world's first open foundation model for generalized humanoid robot reasoning and skills, in just 36 hours, a task that would have taken nearly three months with manual data collection.\n\nThe dataset now includes thousands of new robotics trajectories, featuring the first real-world training data from the Unitree G1 robot and 24,000 simulated teleoperation trajectories.\n\n## Key Capabilities\n\nThe GR00T-Dreams blueprint enables robots to generalize across behaviors, adapt to new environments, and learn novel actions from language instructions, even with training data from only a single task.\n\n## Technical Foundation\n\nThe NVIDIA Isaac GR00T-Dreams blueprint, built on NVIDIA Cosmos, solves this challenge by generating massive synthetic trajectory data from just a single image and language prompt."
    ],
    "durationSeconds": 6.424942205
  },
  "sourceToolAssistantUUID": "c89c000c-5417-48f1-aef6-10ffbe6ff093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T17:09:05.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SYEBRZfZModyxtwf44ewbr`</summary>

```json
{
  "query": "DexMimicGen humanoid manipulation data augmentation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdc3456-6adc-45ea-8403-bcdea476ae8f",
  "isSidechain": false,
  "requestId": "req_011CauFsbXPgtViBnVH5kpn4",
  "type": "assistant",
  "uuid": "5705632b-7982-4925-8d1b-69317b56b88c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5Sv7WUAXMVrrYLMPQBX7W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 23493,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 23493,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
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

_source line 20 · 2026-05-10T17:09:12.158Z_

<details><summary>↩ Tool result · `toolu_01SYEBRZfZModyxtwf44ewbr`</summary>

```text
Web search results for query: "DexMimicGen humanoid manipulation data augmentation 2025 arxiv"

Links: [{"title":"[2410.24185] DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/abs/2410.24185"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://arxiv.org/html/2410.24185v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833v2"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241024185J/abstract"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://www.researchgate.net/publication/385443567_DexMimicGen_Automated_Data_Generation_for_Bimanual_Dexterous_Manipulation_via_Imitation_Learning"},{"title":"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning","url":"https://dexmimicgen.github.io/"},{"title":"Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation","url":"https://arxiv.org/html/2503.24361v2"},{"title":"DexMimicGen: Automated Data Generation for Bimanual ...","url":"https://openreview.net/pdf/4189a2bc6c20d5c52d0e6542702e1be54de0fe82.pdf"},{"title":"SPIDER: Scalable Physics-Informed Dexterous Retargeting","url":"https://arxiv.org/html/2511.09484v1"}]

Based on the search results, I found comprehensive information about DexMimicGen. Here's what I found:

## DexMimicGen Overview

DexMimicGen is a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands.

## Key Contributions

The system generates 21K demos across multiple tasks from just 60 source human demos and studies the effect of several data generation and policy learning decisions on agent performance. It presents a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms.

## Real-World Deployment

The paper presents a real-to-sim-to-real pipeline and deploys it on a real-world humanoid can sorting task.

## Publication and Availability

DexMimicGen is accepted to ICRA 2025. The arxiv version is **2410.24185**, and it has been updated as of March 6, 2025. The paper generated over 20,000 demonstrations for bimanual dexterous robots from just 60 source human demonstrations across 9 tasks, multiple simulators, and the real-world.

The work addresses a key challenge in humanoid robotics: data collection is particularly challenging due to the challenges of simultaneously controlling multiple arms and multi-fingered hands.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5705632b-7982-4925-8d1b-69317b56b88c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "aae76afb-f846-460c-8e8a-6229da03f343",
  "toolUseResult": {
    "query": "DexMimicGen humanoid manipulation data augmentation 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P2MPG3AtrcF4zF1SGMEag5",
        "content": [
          {
            "title": "[2410.24185] DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning",
            "url": "https://arxiv.org/abs/2410.24185"
          },
          {
            "title": "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning",
            "url": "https://arxiv.org/html/2410.24185v1"
          },
          {
            "title": "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning",
            "url": "https://arxiv.org/html/2507.00833v2"
          },
          {
            "title": "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv241024185J/abstract"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning",
            "url": "https://www.researchgate.net/publication/385443567_DexMimicGen_Automated_Data_Generation_for_Bimanual_Dexterous_Manipulation_via_Imitation_Learning"
          },
          {
            "title": "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning",
            "url": "https://dexmimicgen.github.io/"
          },
          {
            "title": "Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation",
            "url": "https://arxiv.org/html/2503.24361v2"
          },
          {
            "title": "DexMimicGen: Automated Data Generation for Bimanual ...",
            "url": "https://openreview.net/pdf/4189a2bc6c20d5c52d0e6542702e1be54de0fe82.pdf"
          },
          {
            "title": "SPIDER: Scalable Physics-Informed Dexterous Retargeting",
            "url": "https://arxiv.org/html/2511.09484v1"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about DexMimicGen. Here's what I found:\n\n## DexMimicGen Overview\n\nDexMimicGen is a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands.\n\n## Key Contributions\n\nThe system generates 21K demos across multiple tasks from just 60 source human demos and studies the effect of several data generation and policy learning decisions on agent performance. It presents a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms.\n\n## Real-World Deployment\n\nThe paper presents a real-to-sim-to-real pipeline and deploys it on a real-world humanoid can sorting task.\n\n## Publication and Availability\n\nDexMimicGen is accepted to ICRA 2025. The arxiv version is **2410.24185**, and it has been updated as of March 6, 2025. The paper generated over 20,000 demonstrations for bimanual dexterous robots from just 60 source human demonstrations across 9 tasks, multiple simulators, and the real-world.\n\nThe work addresses a key challenge in humanoid robotics: data collection is particularly challenging due to the challenges of simultaneously controlling multiple arms and multi-fingered hands."
    ],
    "durationSeconds": 6.8789602610000005
  },
  "sourceToolAssistantUUID": "5705632b-7982-4925-8d1b-69317b56b88c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T17:09:14.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Ey7rgEmvmisj1yAKcZawR`</summary>

```json
{
  "query": "video diffusion model robot action conditioned training data generation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aae76afb-f846-460c-8e8a-6229da03f343",
  "isSidechain": false,
  "requestId": "req_011CauFtJR21euDYTHyFgpMM",
  "type": "assistant",
  "uuid": "31675494-0e7c-499b-85f3-6fa41e02a36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4ga6GdUxvms9UgrLDYqW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 24592,
      "output_tokens": 71,
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
          "output_tokens": 71,
          "cache_read_input_tokens": 24592,
          "cache_creation_input_tokens": 994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 994
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

_source line 22 · 2026-05-10T17:09:22.579Z_

<details><summary>↩ Tool result · `toolu_011Ey7rgEmvmisj1yAKcZawR`</summary>

```text
Web search results for query: "video diffusion model robot action conditioned training data generation 2025 2026 arxiv"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"AVID: Adapting Video Diffusion Models to World Models","url":"https://arxiv.org/html/2410.12822v2"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"MITTY: DIFFUSION-BASED HUMAN-TO-ROBOT VIDEO ...","url":"https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf"},{"title":"A Long-Horizon Video Generation Model for Multi-Task ...","url":"https://arxiv.org/pdf/2506.22007"},{"title":"Vid2World: Crafting Video Diffusion Models to Interactive ...","url":"https://arxiv.org/pdf/2505.14357"}]

I found several recent and relevant papers on arXiv about video diffusion models for robot action-conditioned training and data generation from 2025-2026. Here are the key findings:

## Recent Key Papers:

**1. Unified World Models (April 2025)**
A new diffusion-based learning framework that unifies imitation learning and world modeling, integrating an action diffusion process and an image diffusion process into a single diffusion transformer model conditioned on independent diffusion timesteps. This approach enables improved policies through feature sharing between action and pixels, captures causal relationships between actions and images, and can learn from action-free videos.

**2. Video Generation Models in Robotics (January 2026)**
Recent methods parameterize the video-to-action mapping using an encoder-decoder model trained with a diffusion objective. Video diffusion models generally introduce conditioning inputs through channel concatenation, cross-attention, or adaptive normalization.

**3. MotuBrain (Recently published)**
MotuBrain adopts a unified diffusion framework to jointly model video and action, using a three-stream Mixture-of-Transformers architecture to support inference over five distributions: vision-language-action policy modeling, world modeling, video generation, inverse dynamics, and joint video-action prediction.

**4. Vid2World (May 2025)**
Vid2World leverages vast pre-trained knowledge from internet-scale, action-free video data to achieve high-fidelity, action-conditioned generation across diverse downstream domains with limited interaction data.

These papers collectively demonstrate the rapid advancement in using video diffusion models for action-conditioned robot training data generation in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31675494-0e7c-499b-85f3-6fa41e02a36d",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "578d8ce7-c716-47e8-bf2e-396a27db2d1d",
  "toolUseResult": {
    "query": "video diffusion model robot action conditioned training data generation 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_015c3xFcW4BqzbVjb7Cb17tD",
        "content": [
          {
            "title": "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets",
            "url": "https://arxiv.org/html/2504.02792v1"
          },
          {
            "title": "Video Generation Models in Robotics: Applications, Research Challenges, Future Directions",
            "url": "https://arxiv.org/html/2601.07823v1"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "AVID: Adapting Video Diffusion Models to World Models",
            "url": "https://arxiv.org/html/2410.12822v2"
          },
          {
            "title": "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields",
            "url": "https://arxiv.org/html/2605.06192v1"
          },
          {
            "title": "MITTY: DIFFUSION-BASED HUMAN-TO-ROBOT VIDEO ...",
            "url": "https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf"
          },
          {
            "title": "A Long-Horizon Video Generation Model for Multi-Task ...",
            "url": "https://arxiv.org/pdf/2506.22007"
          },
          {
            "title": "Vid2World: Crafting Video Diffusion Models to Interactive ...",
            "url": "https://arxiv.org/pdf/2505.14357"
          }
        ]
      },
      "I found several recent and relevant papers on arXiv about video diffusion models for robot action-conditioned training and data generation from 2025-2026. Here are the key findings:\n\n## Recent Key Papers:\n\n**1. Unified World Models (April 2025)**\nA new diffusion-based learning framework that unifies imitation learning and world modeling, integrating an action diffusion process and an image diffusion process into a single diffusion transformer model conditioned on independent diffusion timesteps. This approach enables improved policies through feature sharing between action and pixels, captures causal relationships between actions and images, and can learn from action-free videos.\n\n**2. Video Generation Models in Robotics (January 2026)**\nRecent methods parameterize the video-to-action mapping using an encoder-decoder model trained with a diffusion objective. Video diffusion models generally introduce conditioning inputs through channel concatenation, cross-attention, or adaptive normalization.\n\n**3. MotuBrain (Recently published)**\nMotuBrain adopts a unified diffusion framework to jointly model video and action, using a three-stream Mixture-of-Transformers architecture to support inference over five distributions: vision-language-action policy modeling, world modeling, video generation, inverse dynamics, and joint video-action prediction.\n\n**4. Vid2World (May 2025)**\nVid2World leverages vast pre-trained knowledge from internet-scale, action-free video data to achieve high-fidelity, action-conditioned generation across diverse downstream domains with limited interaction data.\n\nThese papers collectively demonstrate the rapid advancement in using video diffusion models for action-conditioned robot training data generation in 2025-2026."
    ],
    "durationSeconds": 7.815052265999999
  },
  "sourceToolAssistantUUID": "31675494-0e7c-499b-85f3-6fa41e02a36d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "578d8ce7-c716-47e8-bf2e-396a27db2d1d",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 25 · 2026-05-10T17:09:24.992Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M3bBcLtWWTDTYCBTFa1emU`</summary>

```json
{
  "query": "humanoid whole-body locomotion manipulation data generation procedural pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "578d8ce7-c716-47e8-bf2e-396a27db2d1d",
  "isSidechain": false,
  "requestId": "req_011CauFu4Xd9Vndifuo9X926",
  "type": "assistant",
  "uuid": "cf5158b3-d940-431c-ace7-c6e3e3712597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XK9WQ6kjY3JFiWXV7Pfoa1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 25586,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25586,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
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

_source line 26 · 2026-05-10T17:09:32.080Z_

<details><summary>↩ Tool result · `toolu_01M3bBcLtWWTDTYCBTFa1emU`</summary>

```text
Web search results for query: "humanoid whole-body locomotion manipulation data generation procedural pipeline 2025 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview","url":"https://openreview.net/forum?id=hVoIz6xD9Q"},{"title":"arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control","url":"https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"PHUMA: PHYSICALLY-GROUNDED HUMANOID ...","url":"https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"Whole-body control for humanoid robot locomotion | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/whole-body-control-for-humanoid-robot-locomotion/"},{"title":"Humanoid Motion Generation in Complex 3D Environments","url":"https://www.mdpi.com/2218-6581/14/6/82"},{"title":"[2510.08807] Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/abs/2510.08807"}]

I found several relevant results about humanoid whole-body locomotion and manipulation research from 2025-2026. Here are the key findings:

## Data Generation and Procedural Pipelines

LeVERB implements a scalable, ready-to-use synthetic data generation pipeline that renders robot kinematic motions with photorealistic rendering and diverse scene randomization for training vision-language models for humanoid robots. This data synthesis pipeline collects diverse human motions retargeted to the humanoid robot and renders them photorealistically in randomized scene contexts, with semantically similar language commands annotated using a VLM.

## Large-Scale Datasets

The Humanoid Everyday Dataset is a large-scale collection of 260 tasks across 7 categories that captures full-body locomotion, dexterous manipulation, and rich human-humanoid interactions in diverse environments. It leverages a highly efficient human-supervised teleoperation pipeline to aggregate high-quality multimodal sensory data including RGB, depth, LiDAR, and tactile inputs, along with natural language annotations.

## Control and Learning Approaches

Recent work addresses integrated whole-body control. The ALMI framework enables adversarial policy learning between upper and lower body, where the lower body aims to provide robust locomotion capabilities to follow velocity commands while the upper body tracks various motions.

These recent projects (from late 2025-2026) demonstrate active development in procedural data generation pipelines, large-scale dataset collection, and sophisticated whole-body control methods for humanoid robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf5158b3-d940-431c-ace7-c6e3e3712597",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "bcdc4aa3-0db6-4b6a-a3b9-e3f94825b073",
  "toolUseResult": {
    "query": "humanoid whole-body locomotion manipulation data generation procedural pipeline 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TZcUfJ3RcjK3xkLHc84s1F",
        "content": [
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview",
            "url": "https://openreview.net/forum?id=hVoIz6xD9Q"
          },
          {
            "title": "arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control",
            "url": "https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"
          },
          {
            "title": "Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation",
            "url": "https://arxiv.org/html/2510.08807v1"
          },
          {
            "title": "PHUMA: PHYSICALLY-GROUNDED HUMANOID ...",
            "url": "https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"
          },
          {
            "title": "Advancements in humanoid robot dynamics and learning-based locomotion control methods",
            "url": "https://www.oaepublish.com/articles/ir.2025.32"
          },
          {
            "title": "Whole-body control for humanoid robot locomotion | PatSnap",
            "url": "https://www.patsnap.com/resources/blog/articles/whole-body-control-for-humanoid-robot-locomotion/"
          },
          {
            "title": "Humanoid Motion Generation in Complex 3D Environments",
            "url": "https://www.mdpi.com/2218-6581/14/6/82"
          },
          {
            "title": "[2510.08807] Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation",
            "url": "https://arxiv.org/abs/2510.08807"
          }
        ]
      },
      "I found several relevant results about humanoid whole-body locomotion and manipulation research from 2025-2026. Here are the key findings:\n\n## Data Generation and Procedural Pipelines\n\nLeVERB implements a scalable, ready-to-use synthetic data generation pipeline that renders robot kinematic motions with photorealistic rendering and diverse scene randomization for training vision-language models for humanoid robots. This data synthesis pipeline collects diverse human motions retargeted to the humanoid robot and renders them photorealistically in randomized scene contexts, with semantically similar language commands annotated using a VLM.\n\n## Large-Scale Datasets\n\nThe Humanoid Everyday Dataset is a large-scale collection of 260 tasks across 7 categories that captures full-body locomotion, dexterous manipulation, and rich human-humanoid interactions in diverse environments. It leverages a highly efficient human-supervised teleoperation pipeline to aggregate high-quality multimodal sensory data including RGB, depth, LiDAR, and tactile inputs, along with natural language annotations.\n\n## Control and Learning Approaches\n\nRecent work addresses integrated whole-body control. The ALMI framework enables adversarial policy learning between upper and lower body, where the lower body aims to provide robust locomotion capabilities to follow velocity commands while the upper body tracks various motions.\n\nThese recent projects (from late 2025-2026) demonstrate active development in procedural data generation pipelines, large-scale dataset collection, and sophisticated whole-body control methods for humanoid robots."
    ],
    "durationSeconds": 7.083551577999999
  },
  "sourceToolAssistantUUID": "cf5158b3-d940-431c-ace7-c6e3e3712597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T17:09:34.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNYq1QpvnEzdUDkFD8rwBu`</summary>

```json
{
  "query": "site:arxiv.org humanoid kinematic structure diffusion model action generation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcdc4aa3-0db6-4b6a-a3b9-e3f94825b073",
  "isSidechain": false,
  "requestId": "req_011CauFum89kHLFk3PEFWcju",
  "type": "assistant",
  "uuid": "69750216-6747-4163-86e8-0bbe6330b24c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015t4GwPZ1JyUCkfV2gzwyMS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 26526,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 26526,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
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

_source line 28 · 2026-05-10T17:09:41.797Z_

<details><summary>↩ Tool result · `toolu_01QNYq1QpvnEzdUDkFD8rwBu`</summary>

```text
Web search results for query: "site:arxiv.org humanoid kinematic structure diffusion model action generation 2025"

Links: [{"title":"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/html/2508.08241v3"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"GitHub - YanjieZe/Improved-3D-Diffusion-Policy: [IROS 2025] Generalizable Humanoid Manipulation with 3D Diffusion Policies. Part 1: Train & Deploy of iDP3 · GitHub","url":"https://github.com/YanjieZe/Improved-3D-Diffusion-Policy"},{"title":"Natural Humanoid Robot Locomotion with Generative Motion Prior","url":"https://arxiv.org/html/2503.09015v1"},{"title":"Scalable and General Whole-Body Control for Cross-Humanoid Locomotion","url":"https://arxiv.org/html/2602.05791v2"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335v1"},{"title":"[2409.11920v1] Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/abs/2409.11920v1"},{"title":"Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models","url":"https://arxiv.org/html/2409.11920v1"},{"title":"[2508.08241] BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion","url":"https://arxiv.org/abs/2508.08241"}]

Based on the web search results, I found several relevant papers on arXiv related to humanoid kinematic structure, diffusion models, and action generation from 2025:

## Key Papers Found:

1. **BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion** (August 2025)
   - Denoising diffusion models are emerging as powerful policy generators in robotics and animation, as they naturally handle multi-modal distributions and long-horizon sequences. In character animation, kinematic diffusion models offer intuitive conditioning through text, music, geometric constraints, or loss functions. BeyondMimic is a real-world framework to learn from human motions for versatile and naturalistic humanoid control via guided diffusion.

2. **Natural Humanoid Robot Locomotion with Generative Motion Prior** (March 2025)
   - The objective of whole-body motion retargeting is to transform human motion data into humanoid robots. This section extends the motion retargeting method from the dual-arm robot to the humanoid robot. To keep motion similarity and satisfy kinematic robot constraints, whole-body motion retargeting is formulated as an optimization problem.

3. **Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking** (Recent 2025)
   - Recent work combines diffusion-based motion generation with RL-based motion tracking, allowing the tracker to output physically plausible actions instead of relying solely on kinematic generation.

4. **Scalable and General Whole-Body Control for Cross-Humanoid Locomotion** (2025)
   - The work captures the shared structures of humanoid robots in a template model and defines a parameter vector that encodes its kinematic layout, link geometries, inertial properties, and joint configurations.

These papers demonstrate active research in 2025 on combining kinematic structure awareness with diffusion models for humanoid action generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69750216-6747-4163-86e8-0bbe6330b24c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "7cf3526f-db4d-485e-8a13-c5d357d9a7f6",
  "toolUseResult": {
    "query": "site:arxiv.org humanoid kinematic structure diffusion model action generation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0127EAXxbFKFoANvw379E98V",
        "content": [
          {
            "title": "BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion",
            "url": "https://arxiv.org/html/2508.08241v3"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/pdf/2503.14734"
          },
          {
            "title": "GitHub - YanjieZe/Improved-3D-Diffusion-Policy: [IROS 2025] Generalizable Humanoid Manipulation with 3D Diffusion Policies. Part 1: Train & Deploy of iDP3 · GitHub",
            "url": "https://github.com/YanjieZe/Improved-3D-Diffusion-Policy"
          },
          {
            "title": "Natural Humanoid Robot Locomotion with Generative Motion Prior",
            "url": "https://arxiv.org/html/2503.09015v1"
          },
          {
            "title": "Scalable and General Whole-Body Control for Cross-Humanoid Locomotion",
            "url": "https://arxiv.org/html/2602.05791v2"
          },
          {
            "title": "Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking",
            "url": "https://arxiv.org/html/2604.17335v1"
          },
          {
            "title": "[2409.11920v1] Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models",
            "url": "https://arxiv.org/abs/2409.11920v1"
          },
          {
            "title": "Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models",
            "url": "https://arxiv.org/html/2409.11920v1"
          },
          {
            "title": "[2508.08241] BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion",
            "url": "https://arxiv.org/abs/2508.08241"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on arXiv related to humanoid kinematic structure, diffusion models, and action generation from 2025:\n\n## Key Papers Found:\n\n1. **BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion** (August 2025)\n   - Denoising diffusion models are emerging as powerful policy generators in robotics and animation, as they naturally handle multi-modal distributions and long-horizon sequences. In character animation, kinematic diffusion models offer intuitive conditioning through text, music, geometric constraints, or loss functions. BeyondMimic is a real-world framework to learn from human motions for versatile and naturalistic humanoid control via guided diffusion.\n\n2. **Natural Humanoid Robot Locomotion with Generative Motion Prior** (March 2025)\n   - The objective of whole-body motion retargeting is to transform human motion data into humanoid robots. This section extends the motion retargeting method from the dual-arm robot to the humanoid robot. To keep motion similarity and satisfy kinematic robot constraints, whole-body motion retargeting is formulated as an optimization problem.\n\n3. **Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking** (Recent 2025)\n   - Recent work combines diffusion-based motion generation with RL-based motion tracking, allowing the tracker to output physically plausible actions instead of relying solely on kinematic generation.\n\n4. **Scalable and General Whole-Body Control for Cross-Humanoid Locomotion** (2025)\n   - The work captures the shared structures of humanoid robots in a template model and defines a parameter vector that encodes its kinematic layout, link geometries, inertial properties, and joint configurations.\n\nThese papers demonstrate active research in 2025 on combining kinematic structure awareness with diffusion models for humanoid action generation."
    ],
    "durationSeconds": 7.507063737999997
  },
  "sourceToolAssistantUUID": "69750216-6747-4163-86e8-0bbe6330b24c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-10T17:09:49.757Z_

Good initial landscape established. Let me now dive deeper into specific areas — concurrent work, cross-domain methods, and potential gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cf3526f-db4d-485e-8a13-c5d357d9a7f6",
  "isSidechain": false,
  "requestId": "req_011CauFvUiSnu5fqYtiqTqNG",
  "type": "assistant",
  "uuid": "320a895d-1ee8-4d81-b625-1514fc018a17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MyFGFngwRtjfgeyw4iku2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 27549,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 27549,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 30 · 2026-05-10T17:09:50.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XYZAnURmPdwVHXVkpohZ88`</summary>

```json
{
  "query": "Cosmos video diffusion robotics fine-tune action conditioned synthetic data 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "320a895d-1ee8-4d81-b625-1514fc018a17",
  "isSidechain": false,
  "requestId": "req_011CauFvUiSnu5fqYtiqTqNG",
  "type": "assistant",
  "uuid": "ee3c8ac0-d34e-46be-a5ae-a74e38566640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MyFGFngwRtjfgeyw4iku2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 27549,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 27549,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 31 · 2026-05-10T17:09:57.293Z_

<details><summary>↩ Tool result · `toolu_01XYZAnURmPdwVHXVkpohZ88`</summary>

```text
Web search results for query: "Cosmos video diffusion robotics fine-tune action conditioned synthetic data 2025 2026"

Links: [{"title":"Cosmos World Foundation Model Platform for Physical AI","url":"https://arxiv.org/html/2501.03575v1"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview","url":"https://openreview.net/forum?id=wPEIStHxYH"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"NVIDIA Makes Cosmos World Foundation Models Openly Available to Physical AI Developer Community","url":"https://blogs.nvidia.com/blog/cosmos-world-foundation-models/"},{"title":"NVIDIA Cosmos: World Foundation Models Powering Physical AI","url":"https://www.nvidia.com/en-us/ai/cosmos/"},{"title":"[2601.16163] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/abs/2601.16163"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260116163K/abstract"},{"title":"Curating Synthetic Datasets to Train Physical AI Models with NVIDIA Cosmos Reason | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/curating-synthetic-datasets-to-train-physical-ai-models-with-nvidia-cosmos-reason/"},{"title":"[Paper Note] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning, Moo Jin Kim+, arXiv'26, 2026.01 · Issue #4289 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4289"}]

Based on the search results, here's what I found regarding Cosmos video diffusion, robotics fine-tuning, action-conditioned models, and synthetic data in 2025-2026:

## Cosmos World Foundation Models Platform

NVIDIA has developed world foundation models (WFMs) that can be fine-tuned for various Physical AI tasks, including robotic tasks consisting of video-action sequences. The models have been trained on 9,000 trillion tokens from 20 million hours of real-world human interactions, environment, industrial, robotics and driving data.

## Cosmos Policy for Robotics

Cosmos Policy adapts the Cosmos-Predict2-2B and Cosmos-Predict2.5-2B-Video2World video foundation model into a state-of-the-art robot policy through a single stage of post-training on robot demonstration data, with no architectural modifications. 

Cosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, harnessing the model's pretrained priors and core learning algorithm to capture complex action distributions.

## Synthetic Data Generation

When paired with NVIDIA Omniverse 3D outputs, the diffusion models generate controllable, high-quality synthetic video data to bootstrap training of robotic and AV perception models, allowing developers to generate massive amounts of controllable, physics-based synthetic data by conditioning Cosmos with composed 3D scenes.

## Performance Results

Cosmos Policy achieves state-of-the-art performance on LIBERO (98.5% on Cosmos policy (predict2) and 98.33 on Cosmos policy (predict2.5)), RoboCasa (67.1% on Cosmos policy (predict2) and 71.14 on Cosmos policy (predict2.5)), and ALOHA robot tasks (93.6% on Cosmos policy (predict 2)).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee3c8ac0-d34e-46be-a5ae-a74e38566640",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "0d760365-a520-4827-8271-8f3fe381e8f1",
  "toolUseResult": {
    "query": "Cosmos video diffusion robotics fine-tune action conditioned synthetic data 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WuwVoj81TxbQEhZ8JKk1Mc",
        "content": [
          {
            "title": "Cosmos World Foundation Model Platform for Physical AI",
            "url": "https://arxiv.org/html/2501.03575v1"
          },
          {
            "title": "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview",
            "url": "https://openreview.net/forum?id=wPEIStHxYH"
          },
          {
            "title": "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook",
            "url": "https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"
          },
          {
            "title": "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning",
            "url": "https://arxiv.org/html/2601.16163v1"
          },
          {
            "title": "NVIDIA Makes Cosmos World Foundation Models Openly Available to Physical AI Developer Community",
            "url": "https://blogs.nvidia.com/blog/cosmos-world-foundation-models/"
          },
          {
            "title": "NVIDIA Cosmos: World Foundation Models Powering Physical AI",
            "url": "https://www.nvidia.com/en-us/ai/cosmos/"
          },
          {
            "title": "[2601.16163] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning",
            "url": "https://arxiv.org/abs/2601.16163"
          },
          {
            "title": "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260116163K/abstract"
          },
          {
            "title": "Curating Synthetic Datasets to Train Physical AI Models with NVIDIA Cosmos Reason | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/curating-synthetic-datasets-to-train-physical-ai-models-with-nvidia-cosmos-reason/"
          },
          {
            "title": "[Paper Note] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning, Moo Jin Kim+, arXiv'26, 2026.01 · Issue #4289 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/4289"
          }
        ]
      },
      "Based on the search results, here's what I found regarding Cosmos video diffusion, robotics fine-tuning, action-conditioned models, and synthetic data in 2025-2026:\n\n## Cosmos World Foundation Models Platform\n\nNVIDIA has developed world foundation models (WFMs) that can be fine-tuned for various Physical AI tasks, including robotic tasks consisting of video-action sequences. The models have been trained on 9,000 trillion tokens from 20 million hours of real-world human interactions, environment, industrial, robotics and driving data.\n\n## Cosmos Policy for Robotics\n\nCosmos Policy adapts the Cosmos-Predict2-2B and Cosmos-Predict2.5-2B-Video2World video foundation model into a state-of-the-art robot policy through a single stage of post-training on robot demonstration data, with no architectural modifications. \n\nCosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, harnessing the model's pretrained priors and core learning algorithm to capture complex action distributions.\n\n## Synthetic Data Generation\n\nWhen paired with NVIDIA Omniverse 3D outputs, the diffusion models generate controllable, high-quality synthetic video data to bootstrap training of robotic and AV perception models, allowing developers to generate massive amounts of controllable, physics-based synthetic data by conditioning Cosmos with composed 3D scenes.\n\n## Performance Results\n\nCosmos Policy achieves state-of-the-art performance on LIBERO (98.5% on Cosmos policy (predict2) and 98.33 on Cosmos policy (predict2.5)), RoboCasa (67.1% on Cosmos policy (predict2) and 71.14 on Cosmos policy (predict2.5)), and ALOHA robot tasks (93.6% on Cosmos policy (predict 2))."
    ],
    "durationSeconds": 6.889244298000005
  },
  "sourceToolAssistantUUID": "ee3c8ac0-d34e-46be-a5ae-a74e38566640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-10T17:09:57.300Z_

```json
{
  "parentUuid": "0d760365-a520-4827-8271-8f3fe381e8f1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "201586bf-cdf3-40b2-bc78-0e53901bd6a0",
  "timestamp": "2026-05-10T17:09:57.300Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-10T17:10:00.188Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B7F77UzeWqFt5uSzUysER7`</summary>

```json
{
  "query": "physics-aware video generation kinematic consistency robot simulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "201586bf-cdf3-40b2-bc78-0e53901bd6a0",
  "isSidechain": false,
  "requestId": "req_011CauFwcypBJG4ZoEtKsmdf",
  "type": "assistant",
  "uuid": "8e23ae1a-1174-4028-9814-cbbf9a324d36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8opFBJB2fgX8FrQ81wFQe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 28631,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 28631,
          "cache_creation_input_tokens": 1224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1224
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

_source line 34 · 2026-05-10T17:10:07.632Z_

<details><summary>↩ Tool result · `toolu_01B7F77UzeWqFt5uSzUysER7`</summary>

```text
Web search results for query: "physics-aware video generation kinematic consistency robot simulation 2025 2026"

Links: [{"title":"GitHub - BestJunYu/Awesome-Physics-aware-Generation: Physical laws underpin all existence, and harnessing them for generative modeling opens boundless possibilities for advancing science and shaping the future! · GitHub","url":"https://github.com/BestJunYu/Awesome-Physics-aware-Generation"},{"title":"Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.00110"},{"title":"Learning to Generate Object Interactions with Physics-Guided Video Diffusion | OpenReview","url":"https://openreview.net/forum?id=vrY91av397"},{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"GitHub - ziqihuangg/Awesome-From-Video-Generation-to-World-Model: A list of works on video generation towards world model · GitHub","url":"https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/"},{"title":"Goal Force: Teaching Video Models To Accomplish Physics-Conditioned Goals","url":"https://arxiv.org/html/2601.05848v2"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"GitHub - minnie-lin/Awesome-Physics-Cognition-based-Video-Generation: A comprehensive list of papers investigating physical cognition in video generation, including papers, codes, and related websites. · GitHub","url":"https://github.com/minnie-lin/Awesome-Physics-Cognition-based-Video-Generation"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"[2603.06408] Physical Simulator In-the-Loop Video Generation","url":"https://arxiv.org/abs/2603.06408"}]

I've found comprehensive research results related to physics-aware video generation with kinematic consistency for robot simulation. Here's what recent work in this area shows:

## Key Recent Works (2025-2026)

**Physics-Aware Video Generation for Robotics:**

Recent approaches incorporate causal masking for implicit inverse kinematics, allowing action tokens to attend to future visual states and foster inverse-kinematics reasoning. Methods like PhysGen outperform robust baselines like OpenVLA and WorldVLA by margins of 13.8% and 8.8% respectively.

**Kinematic Control in Video Models:**

EA-WM (Event-Aware Generative World Model) effectively closes the loop between kinematic control and visual perception. These models address the challenge of preserving precise robot spatial geometry and fine-grained robot-object interaction dynamics in generated rollouts.

**Physics-Guided Approaches:**

KineMask introduces physics-guided video generation that enables realistic rigid body control, interactions, and effects. Additionally, Physical Simulator In-the-loop Video Generation (PSIVG) integrates a physical simulator into the video diffusion process, reconstructing 4D scenes and using simulated trajectories to guide video generation toward spatio-temporally physically coherent motion.

**Broader Context:**

Video generation models have emerged as high-fidelity models of the physical world, capable of synthesizing videos capturing fine-grained interactions between agents and environments, addressing long-standing challenges faced by physics-based simulators.

The research community is actively developing benchmarks and evaluation metrics to assess physical consistency and kinematic feasibility in robot video generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e23ae1a-1174-4028-9814-cbbf9a324d36",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "605c1e93-0989-449e-a8e3-01ff7e15462b",
  "toolUseResult": {
    "query": "physics-aware video generation kinematic consistency robot simulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S3F44XrADU4gxKa9Db3PQK",
        "content": [
          {
            "title": "GitHub - BestJunYu/Awesome-Physics-aware-Generation: Physical laws underpin all existence, and harnessing them for generative modeling opens boundless possibilities for advancing science and shaping the future! · GitHub",
            "url": "https://github.com/BestJunYu/Awesome-Physics-aware-Generation"
          },
          {
            "title": "Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2603.00110"
          },
          {
            "title": "Learning to Generate Object Interactions with Physics-Guided Video Diffusion | OpenReview",
            "url": "https://openreview.net/forum?id=vrY91av397"
          },
          {
            "title": "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields",
            "url": "https://arxiv.org/html/2605.06192v1"
          },
          {
            "title": "GitHub - ziqihuangg/Awesome-From-Video-Generation-to-World-Model: A list of works on video generation towards world model · GitHub",
            "url": "https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/"
          },
          {
            "title": "Goal Force: Teaching Video Models To Accomplish Physics-Conditioned Goals",
            "url": "https://arxiv.org/html/2601.05848v2"
          },
          {
            "title": "Rethinking Video Generation Model for the Embodied World",
            "url": "https://arxiv.org/html/2601.15282v1"
          },
          {
            "title": "GitHub - minnie-lin/Awesome-Physics-Cognition-based-Video-Generation: A comprehensive list of papers investigating physical cognition in video generation, including papers, codes, and related websites. · GitHub",
            "url": "https://github.com/minnie-lin/Awesome-Physics-Cognition-based-Video-Generation"
          },
          {
            "title": "Video Generation Models in Robotics: Applications, Research Challenges, Future Directions",
            "url": "https://arxiv.org/html/2601.07823v1"
          },
          {
            "title": "[2603.06408] Physical Simulator In-the-Loop Video Generation",
            "url": "https://arxiv.org/abs/2603.06408"
          }
        ]
      },
      "I've found comprehensive research results related to physics-aware video generation with kinematic consistency for robot simulation. Here's what recent work in this area shows:\n\n## Key Recent Works (2025-2026)\n\n**Physics-Aware Video Generation for Robotics:**\n\nRecent approaches incorporate causal masking for implicit inverse kinematics, allowing action tokens to attend to future visual states and foster inverse-kinematics reasoning. Methods like PhysGen outperform robust baselines like OpenVLA and WorldVLA by margins of 13.8% and 8.8% respectively.\n\n**Kinematic Control in Video Models:**\n\nEA-WM (Event-Aware Generative World Model) effectively closes the loop between kinematic control and visual perception. These models address the challenge of preserving precise robot spatial geometry and fine-grained robot-object interaction dynamics in generated rollouts.\n\n**Physics-Guided Approaches:**\n\nKineMask introduces physics-guided video generation that enables realistic rigid body control, interactions, and effects. Additionally, Physical Simulator In-the-loop Video Generation (PSIVG) integrates a physical simulator into the video diffusion process, reconstructing 4D scenes and using simulated trajectories to guide video generation toward spatio-temporally physically coherent motion.\n\n**Broader Context:**\n\nVideo generation models have emerged as high-fidelity models of the physical world, capable of synthesizing videos capturing fine-grained interactions between agents and environments, addressing long-standing challenges faced by physics-based simulators.\n\nThe research community is actively developing benchmarks and evaluation metrics to assess physical consistency and kinematic feasibility in robot video generation tasks."
    ],
    "durationSeconds": 7.437673078000007
  },
  "sourceToolAssistantUUID": "8e23ae1a-1174-4028-9814-cbbf9a324d36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "605c1e93-0989-449e-a8e3-01ff7e15462b",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 37 · 2026-05-10T17:10:10.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UsDcRB37MHiSVMb4eMHbJN`</summary>

```json
{
  "query": "\"physical simulator in the loop\" video diffusion generation PSIVG 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "605c1e93-0989-449e-a8e3-01ff7e15462b",
  "isSidechain": false,
  "requestId": "req_011CauFxPAP7EDDo5b43Pj9t",
  "type": "assistant",
  "uuid": "ec4d98e9-1bb7-461e-89a0-655ac0b39fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017E6M4wFGaT5R9X745wx1qb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 29855,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 29855,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1007
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

_source line 38 · 2026-05-10T17:10:17.785Z_

<details><summary>↩ Tool result · `toolu_01UsDcRB37MHiSVMb4eMHbJN`</summary>

```text
Web search results for query: ""physical simulator in the loop" video diffusion generation PSIVG 2026 arxiv"

Links: [{"title":"GitHub - MarkHershey/PSIVG: [CVPR 2026] Physical Simulator In-the-Loop Video Generation · GitHub","url":"https://github.com/MarkHershey/PSIVG"},{"title":"[2603.06408] Physical Simulator In-the-Loop Video Generation","url":"https://arxiv.org/abs/2603.06408"},{"title":"Physical Simulator In-the-Loop Video Generation","url":"https://arxiv.org/html/2603.06408"},{"title":"Physical Simulator In-the-Loop Video Generation [Quick Review]","url":"https://liner.com/review/physical-simulator-intheloop-video-generation"},{"title":"Physical Simulator In-the-Loop Video Generation","url":"https://vcai.mpi-inf.mpg.de/projects/PSIVG/"},{"title":"Physical Simulator In-the-Loop Video Generation | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.06408"},{"title":"(PDF) Physical Simulator In-the-Loop Video Generation","url":"https://www.researchgate.net/publication/401691824_Physical_Simulator_In-the-Loop_Video_Generation"},{"title":"Paper page - Physical Simulator In-the-Loop Video Generation","url":"https://huggingface.co/papers/2603.06408"},{"title":"Towards Physically Aware Video Generation via Latent ...","url":"https://arxiv.org/pdf/2601.03665"},{"title":"Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation","url":"https://arxiv.org/html/2603.00110"}]

I found comprehensive information about the paper you searched for. Here are the key details:

## Physical Simulator In-the-Loop Video Generation (PSIVG)

The paper is titled "Physical Simulator In-the-Loop Video Generation" by authors Foo, Lin Geng, Huang, Mark He, Lattas, Alexandros, Moschoglou, Stylianos, Beeler, Thabo, and Theobalt, Christian, published on arXiv as preprint arXiv:2603.06408 in 2026.

### Overview

PSIVG is a novel framework that integrates a physical simulator into the video diffusion process. Recent advances in diffusion-based video generation have achieved remarkable visual realism but still struggle to obey basic physical laws such as gravity, inertia, and collision, with generated objects often moving inconsistently across frames or violating physical constraints.

### Methodology

Starting from a template video generated by a pre-trained diffusion model, PSIVG reconstructs the 4D scene and foreground object meshes, initializes them within a physical simulator, and generates physically consistent trajectories, which are then used to guide the video generator toward spatio-temporally physically coherent motion.

### Key Innovation

PSIVG proposes a Test-Time Texture Consistency Optimization (TTCO) technique that adapts text and feature embeddings based on pixel correspondences from the simulator to improve texture consistency during object movement.

### Results

Comprehensive experiments demonstrate that PSIVG produces videos that better adhere to real-world physics while preserving visual quality and diversity. PSIVG is accepted for CVPR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec4d98e9-1bb7-461e-89a0-655ac0b39fb0",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "8a7528b0-ffdb-43b8-bbc9-70628bbcdc65",
  "toolUseResult": {
    "query": "\"physical simulator in the loop\" video diffusion generation PSIVG 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RkzprZJgo6z6Jkc4pUXV5a",
        "content": [
          {
            "title": "GitHub - MarkHershey/PSIVG: [CVPR 2026] Physical Simulator In-the-Loop Video Generation · GitHub",
            "url": "https://github.com/MarkHershey/PSIVG"
          },
          {
            "title": "[2603.06408] Physical Simulator In-the-Loop Video Generation",
            "url": "https://arxiv.org/abs/2603.06408"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation",
            "url": "https://arxiv.org/html/2603.06408"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation [Quick Review]",
            "url": "https://liner.com/review/physical-simulator-intheloop-video-generation"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation",
            "url": "https://vcai.mpi-inf.mpg.de/projects/PSIVG/"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2603.06408"
          },
          {
            "title": "(PDF) Physical Simulator In-the-Loop Video Generation",
            "url": "https://www.researchgate.net/publication/401691824_Physical_Simulator_In-the-Loop_Video_Generation"
          },
          {
            "title": "Paper page - Physical Simulator In-the-Loop Video Generation",
            "url": "https://huggingface.co/papers/2603.06408"
          },
          {
            "title": "Towards Physically Aware Video Generation via Latent ...",
            "url": "https://arxiv.org/pdf/2601.03665"
          },
          {
            "title": "Learning Physics from Pretrained Video Models: A Multimodal Continuous and Sequential World Interaction Models for Robotic Manipulation",
            "url": "https://arxiv.org/html/2603.00110"
          }
        ]
      },
      "I found comprehensive information about the paper you searched for. Here are the key details:\n\n## Physical Simulator In-the-Loop Video Generation (PSIVG)\n\nThe paper is titled \"Physical Simulator In-the-Loop Video Generation\" by authors Foo, Lin Geng, Huang, Mark He, Lattas, Alexandros, Moschoglou, Stylianos, Beeler, Thabo, and Theobalt, Christian, published on arXiv as preprint arXiv:2603.06408 in 2026.\n\n### Overview\n\nPSIVG is a novel framework that integrates a physical simulator into the video diffusion process. Recent advances in diffusion-based video generation have achieved remarkable visual realism but still struggle to obey basic physical laws such as gravity, inertia, and collision, with generated objects often moving inconsistently across frames or violating physical constraints.\n\n### Methodology\n\nStarting from a template video generated by a pre-trained diffusion model, PSIVG reconstructs the 4D scene and foreground object meshes, initializes them within a physical simulator, and generates physically consistent trajectories, which are then used to guide the video generator toward spatio-temporally physically coherent motion.\n\n### Key Innovation\n\nPSIVG proposes a Test-Time Texture Consistency Optimization (TTCO) technique that adapts text and feature embeddings based on pixel correspondences from the simulator to improve texture consistency during object movement.\n\n### Results\n\nComprehensive experiments demonstrate that PSIVG produces videos that better adhere to real-world physics while preserving visual quality and diversity. PSIVG is accepted for CVPR 2026."
    ],
    "durationSeconds": 7.552326671000002
  },
  "sourceToolAssistantUUID": "ec4d98e9-1bb7-461e-89a0-655ac0b39fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T17:10:20.644Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XB2bxrGGXggEG2MVDbdXVd`</summary>

```json
{
  "query": "humanoid robot loco-manipulation benchmark HumanoidBench Isaac Lab 2025 2026 SOTA results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a7528b0-ffdb-43b8-bbc9-70628bbcdc65",
  "isSidechain": false,
  "requestId": "req_011CauFy8eYBgEUTJ3zJC3c7",
  "type": "assistant",
  "uuid": "f8ebe168-e37d-4a72-a300-72a9b06a3fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EA9QYtR7pUhqZRPiFHF62k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 30862,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 30862,
          "cache_creation_input_tokens": 923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 923
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

_source line 40 · 2026-05-10T17:10:29.231Z_

<details><summary>↩ Tool result · `toolu_01XB2bxrGGXggEG2MVDbdXVd`</summary>

```text
Web search results for query: "humanoid robot loco-manipulation benchmark HumanoidBench Isaac Lab 2025 2026 SOTA results"

Links: [{"title":"HumanoidBench","url":"https://humanoid-bench.github.io/"},{"title":"[2403.10506] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation","url":"https://arxiv.org/abs/2403.10506"},{"title":"HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | Request PDF","url":"https://www.researchgate.net/publication/383889121_HumanoidBench_Simulated_Humanoid_Benchmark_for_Whole-Body_Locomotion_and_Manipulation"},{"title":"[HumanoidBench] Simulating the Future of Humanoid Robots | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/robot/HumanoidBench"},{"title":"HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation","url":"https://arxiv.org/html/2403.10506v1"},{"title":"HumanoidBench: Simulated Humanoid Benchmark for ...","url":"https://arxiv.org/pdf/2403.10506"},{"title":"GitHub - carlosferrazza/humanoid-bench · GitHub","url":"https://github.com/carlosferrazza/humanoid-bench"},{"title":"HumanoidBench: Benchmark for Humanoid Robotics","url":"https://www.emergentmind.com/papers/2403.10506"},{"title":"HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | alphaXiv","url":"https://www.alphaxiv.org/abs/2403.10506v2"},{"title":"Humanoid-Bench: Robotic Benchmark Suite","url":"https://www.emergentmind.com/topics/humanoid-bench"}]

Based on the search results, here's what I found about HumanoidBench and related benchmarks for humanoid robot loco-manipulation research:

## HumanoidBench Overview

HumanoidBench is a high-dimensional, simulated robot learning benchmark featuring a humanoid robot equipped with dexterous hands and a variety of challenging whole-body manipulation and locomotion tasks. HumanoidBench is the first-of-its-kind simulated humanoid robot benchmark, including 27 distinct whole-body control tasks.

## Technical Details

The simulation environment of HumanoidBench uses the MuJoCo physics engine, featuring the choice across different robot models (e.g, Unitree H1, Agility Robotics Digit) and end effectors (e.g., Shadow Hand, Robotiq 2F-85 gripper). In their experiments, they opt for the Unitree H1 humanoid robot with two dexterous Shadow Hands attached to its arms.

## Task Structure

HumanoidBench provides high-dimensional tasks involving full-body locomotion, object transport, multi-contact behaviors, and complex environment traversal, with action spaces as large as 61 DoF per timestep. Tasks range from long-horizon, contact-rich sequences (e.g., walking to and opening a door) to high-precision operations (e.g., needle threading).

## State-of-the-Art Results

State-of-the-art reinforcement learning algorithms struggle with most tasks, whereas a hierarchical learning approach achieves superior performance when supported by robust low-level policies, such as walking or reaching. 

Deterministic policy gradient methods, notably TD3 and its optimized variant FastTD3, have become the dominant choice for state-of-the-art performance. By leveraging the stability of deterministic policies in massively parallelized environments, such as IsaacLab, MuJoCo Playground, and HumanoidBench, these approaches have successfully solved challenging locomotion and manipulation tasks.

The benchmark was originally introduced in 2024 and continues to be an important platform for evaluating humanoid robot learning algorithms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8ebe168-e37d-4a72-a300-72a9b06a3fad",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "12eb3cb9-f6c2-40a6-bc8f-9d05341330e0",
  "toolUseResult": {
    "query": "humanoid robot loco-manipulation benchmark HumanoidBench Isaac Lab 2025 2026 SOTA results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LRxeq45U4De4EYm1jsQdzy",
        "content": [
          {
            "title": "HumanoidBench",
            "url": "https://humanoid-bench.github.io/"
          },
          {
            "title": "[2403.10506] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation",
            "url": "https://arxiv.org/abs/2403.10506"
          },
          {
            "title": "HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | Request PDF",
            "url": "https://www.researchgate.net/publication/383889121_HumanoidBench_Simulated_Humanoid_Benchmark_for_Whole-Body_Locomotion_and_Manipulation"
          },
          {
            "title": "[HumanoidBench] Simulating the Future of Humanoid Robots | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media",
            "url": "https://ai-scholar.tech/en/articles/robot/HumanoidBench"
          },
          {
            "title": "HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation",
            "url": "https://arxiv.org/html/2403.10506v1"
          },
          {
            "title": "HumanoidBench: Simulated Humanoid Benchmark for ...",
            "url": "https://arxiv.org/pdf/2403.10506"
          },
          {
            "title": "GitHub - carlosferrazza/humanoid-bench · GitHub",
            "url": "https://github.com/carlosferrazza/humanoid-bench"
          },
          {
            "title": "HumanoidBench: Benchmark for Humanoid Robotics",
            "url": "https://www.emergentmind.com/papers/2403.10506"
          },
          {
            "title": "HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2403.10506v2"
          },
          {
            "title": "Humanoid-Bench: Robotic Benchmark Suite",
            "url": "https://www.emergentmind.com/topics/humanoid-bench"
          }
        ]
      },
      "Based on the search results, here's what I found about HumanoidBench and related benchmarks for humanoid robot loco-manipulation research:\n\n## HumanoidBench Overview\n\nHumanoidBench is a high-dimensional, simulated robot learning benchmark featuring a humanoid robot equipped with dexterous hands and a variety of challenging whole-body manipulation and locomotion tasks. HumanoidBench is the first-of-its-kind simulated humanoid robot benchmark, including 27 distinct whole-body control tasks.\n\n## Technical Details\n\nThe simulation environment of HumanoidBench uses the MuJoCo physics engine, featuring the choice across different robot models (e.g, Unitree H1, Agility Robotics Digit) and end effectors (e.g., Shadow Hand, Robotiq 2F-85 gripper). In their experiments, they opt for the Unitree H1 humanoid robot with two dexterous Shadow Hands attached to its arms.\n\n## Task Structure\n\nHumanoidBench provides high-dimensional tasks involving full-body locomotion, object transport, multi-contact behaviors, and complex environment traversal, with action spaces as large as 61 DoF per timestep. Tasks range from long-horizon, contact-rich sequences (e.g., walking to and opening a door) to high-precision operations (e.g., needle threading).\n\n## State-of-the-Art Results\n\nState-of-the-art reinforcement learning algorithms struggle with most tasks, whereas a hierarchical learning approach achieves superior performance when supported by robust low-level policies, such as walking or reaching. \n\nDeterministic policy gradient methods, notably TD3 and its optimized variant FastTD3, have become the dominant choice for state-of-the-art performance. By leveraging the stability of deterministic policies in massively parallelized environments, such as IsaacLab, MuJoCo Playground, and HumanoidBench, these approaches have successfully solved challenging locomotion and manipulation tasks.\n\nThe benchmark was originally introduced in 2024 and continues to be an important platform for evaluating humanoid robot learning algorithms."
    ],
    "durationSeconds": 8.582975121000011
  },
  "sourceToolAssistantUUID": "f8ebe168-e37d-4a72-a300-72a9b06a3fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T17:10:34.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U4Ctt41CZUoLVCyffx5BrC`</summary>

```json
{
  "query": "WholebodyVLA ICLR 2026 humanoid whole-body control latent action"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12eb3cb9-f6c2-40a6-bc8f-9d05341330e0",
  "isSidechain": false,
  "requestId": "req_011CauFyyWeCCBLjbWYoQ7SH",
  "type": "assistant",
  "uuid": "b6a62d8e-0422-4432-bfce-02d75a9bb876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hSrVhRBdQnkavgV2GbeBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 31785,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 31785,
          "cache_creation_input_tokens": 1117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1117
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

_source line 42 · 2026-05-10T17:10:41.948Z_

<details><summary>↩ Tool result · `toolu_01U4Ctt41CZUoLVCyffx5BrC`</summary>

```text
Web search results for query: "WholebodyVLA ICLR 2026 humanoid whole-body control latent action"

Links: [{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | OpenReview","url":"https://openreview.net/forum?id=OCJmVjyzN7"},{"title":"[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/abs/2512.11047"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/3067651d96704608727027ec28fda2eb8c2a7c4a.pdf"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control","url":"https://arxiv.org/html/2512.11047v1"},{"title":"LEVERB: HUMANOID WHOLE-BODY CONTROL","url":"https://openreview.net/pdf/4b864af89cc8b909a67e1acc87f57e457df42338.pdf"},{"title":"LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction | OpenReview","url":"https://openreview.net/forum?id=dLgFqCaXNg"},{"title":"WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control","url":"https://wholebodyvla.github.io/"},{"title":"LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction","url":"https://arxiv.org/html/2506.13751v1"}]

Based on the search results, here's information about WholeBodyVLA:

## Overview

WholeBodyVLA is a unified Vision-Language-Action framework for large-space humanoid loco-manipulation. WholeBodyVLA is a unified framework for humanoid loco-manipulation and is one of its kind enabling large-space humanoid loco–manipulation.

## Key Innovation: Latent Action Learning

The framework proposes a unified latent learning framework that enables Vision-Language-Action (VLA) system to learn from low-cost action-free egocentric videos. Latent action learning sidesteps explicit action labels, instead compressing frame-to-frame visual changes into compact, discrete tokens that supervise policy learning from action-free videos.

## Technical Approach

The system encodes egocentric images and language instructions into latent action tokens, which are decoded into dual-arm joint actions and locomotion commands, enabling end-to-end control for complex loco-manipulation tasks. Additionally, a loco-manipulation-oriented (LMO) RL policy is presented specifically tailored for accurate and stable core loco-manipulation movements, such as advancing, turning, and squatting.

## Performance and Results

It was verified via comprehensive experiments on the AgiBot X2 humanoid, outperforming prior baseline by 21.3%, and also demonstrates strong generalization and high extensibility across a broad range of tasks.

The paper was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6a62d8e-0422-4432-bfce-02d75a9bb876",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "a1c793b1-53ec-409e-9890-ec96a659c454",
  "toolUseResult": {
    "query": "WholebodyVLA ICLR 2026 humanoid whole-body control latent action",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XSNQSWjabR6iyYiJCTZgs8",
        "content": [
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"
          },
          {
            "title": "WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | OpenReview",
            "url": "https://openreview.net/forum?id=OCJmVjyzN7"
          },
          {
            "title": "[2512.11047] WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control",
            "url": "https://arxiv.org/abs/2512.11047"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/3067651d96704608727027ec28fda2eb8c2a7c4a.pdf"
          },
          {
            "title": "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control",
            "url": "https://arxiv.org/html/2512.11047v1"
          },
          {
            "title": "LEVERB: HUMANOID WHOLE-BODY CONTROL",
            "url": "https://openreview.net/pdf/4b864af89cc8b909a67e1acc87f57e457df42338.pdf"
          },
          {
            "title": "LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction | OpenReview",
            "url": "https://openreview.net/forum?id=dLgFqCaXNg"
          },
          {
            "title": "WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control",
            "url": "https://wholebodyvla.github.io/"
          },
          {
            "title": "LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction",
            "url": "https://arxiv.org/html/2506.13751v1"
          }
        ]
      },
      "Based on the search results, here's information about WholeBodyVLA:\n\n## Overview\n\nWholeBodyVLA is a unified Vision-Language-Action framework for large-space humanoid loco-manipulation. WholeBodyVLA is a unified framework for humanoid loco-manipulation and is one of its kind enabling large-space humanoid loco–manipulation.\n\n## Key Innovation: Latent Action Learning\n\nThe framework proposes a unified latent learning framework that enables Vision-Language-Action (VLA) system to learn from low-cost action-free egocentric videos. Latent action learning sidesteps explicit action labels, instead compressing frame-to-frame visual changes into compact, discrete tokens that supervise policy learning from action-free videos.\n\n## Technical Approach\n\nThe system encodes egocentric images and language instructions into latent action tokens, which are decoded into dual-arm joint actions and locomotion commands, enabling end-to-end control for complex loco-manipulation tasks. Additionally, a loco-manipulation-oriented (LMO) RL policy is presented specifically tailored for accurate and stable core loco-manipulation movements, such as advancing, turning, and squatting.\n\n## Performance and Results\n\nIt was verified via comprehensive experiments on the AgiBot X2 humanoid, outperforming prior baseline by 21.3%, and also demonstrates strong generalization and high extensibility across a broad range of tasks.\n\nThe paper was published as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 7.124915049000003
  },
  "sourceToolAssistantUUID": "b6a62d8e-0422-4432-bfce-02d75a9bb876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-10T17:10:44.789Z_

This is very relevant — WholeBodyVLA learns from action-free egocentric videos via latent action learning. Let me search for more concurrent/competing work and cross-domain approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1c793b1-53ec-409e-9890-ec96a659c454",
  "isSidechain": false,
  "requestId": "req_011CauFzuqfKV3DjTFdijEn9",
  "type": "assistant",
  "uuid": "db4fa801-becf-4a7c-b9b3-e1271d1f2e0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLwEDnZcynVudnk4gSx4Fg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 32902,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 32902,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 44 · 2026-05-10T17:10:45.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Gyy2wKCtVSJB4oEGbTVJH`</summary>

```json
{
  "query": "Helix humanoid self-supervised pipeline data generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4fa801-becf-4a7c-b9b3-e1271d1f2e0d",
  "isSidechain": false,
  "requestId": "req_011CauFzuqfKV3DjTFdijEn9",
  "type": "assistant",
  "uuid": "4fd28ac1-e4ef-42a7-bb34-ec485463c35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLwEDnZcynVudnk4gSx4Fg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 32902,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 32902,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 45 · 2026-05-10T17:10:53.193Z_

<details><summary>↩ Tool result · `toolu_013Gyy2wKCtVSJB4oEGbTVJH`</summary>

```text
Web search results for query: "Helix humanoid self-supervised pipeline data generation 2025 2026"

Links: [{"title":"Helix: A Vision-Language-Action Model for Generalist Humanoid Control","url":"https://www.figure.ai/news/helix"},{"title":"Figure AI opens new 'Helix Lab' to accelerate learning for ...","url":"https://mlq.ai/news/figure-ai-opens-new-helix-lab-to-accelerate-learning-for-its-humanoid-robots/"},{"title":"Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates","url":"https://humanoid.press/"},{"title":"Embodied AI Milestone: Figure AI Unveils Helix 02 'Brain,' Achieving Breakthrough in Robotic Autonomous Housekeeping — BigGo Finance","url":"https://finance.biggo.com/news/gkcKCJwBE5UokKawh-wG"},{"title":"Figure AI’s Helix: A Paradigm Shift in Humanoid Robotics and Embodied Intelligence — Foreign Affairs Forum","url":"https://www.faf.ae/home/2025/2/22/figure-ais-helix-a-paradigm-shift-in-humanoid-robotics-and-embodied-intelligence"},{"title":"Figure's Helix: AI that Brings Human-Like Robots to your Home - Analytics Vidhya","url":"https://www.analyticsvidhya.com/blog/2025/02/figures-helix/"},{"title":"Figure AI Announces Helix 02 - a General-Purpose Humanoid System - Luigi Freda","url":"https://www.luigifreda.com/2026/02/02/figure-ai-announces-helix-02-a-general-purpose-humanoid-system/"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Figure AI Unveils Helix Model to Accelerate Home Robot Deployment","url":"https://mikekalil.com/blog/figure-helix-ai/"},{"title":"Introducing Helix 02: Full-Body Autonomy","url":"https://www.figure.ai/news/helix-02"}]

Based on the web search results, here's what I found about Helix, humanoid robots, self-supervised pipelines, and data generation in 2025-2026:

## Helix Overview

Helix is built on a Vision-Language-Action (VLA) framework, designed to enable humanoid robots to reason and operate with human-like capabilities. The system has evolved significantly during this period.

## Data Generation and Training

**Original Helix (2025):** Helix was trained with ~500 hours of high quality supervised data in total, a small fraction of the size of previously collected VLA datasets (<5%), and without any dependencies around multi-robot-embodiment collect or multiple stages of training. Unlike traditional robotic pipelines that separate perception, planning, and control, Helix integrates these functions into a single neural network trained through 500 hours of supervised human demonstrations.

**Helix Lab and Self-Supervised Pipeline (2025-2026):** Figure AI presents the Helix Lab as a way to close the loop between data collection, simulation-based training, and on-robot learning. In this setup, egocentric human data gathered in the lab feeds into training pipelines, which may include simulated environments that reproduce recorded scenarios. By focusing on egocentric human video and interaction data, Figure is targeting the closest available proxy to what a robot will experience in deployment, rather than relying solely on external camera views or synthetic scenes.

## Helix 02 (January 2026)

Helix 02 extends capability to the entire robot - walking, manipulating, and balancing as one continuous system. Helix 02 unloads and reloads a dishwasher across a full-sized kitchen - a four-minute, end-to-end autonomous task that integrates walking, manipulation, and balance with no resets and no human intervention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fd28ac1-e4ef-42a7-bb34-ec485463c35b",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "bfe3a611-1a02-45d5-840f-0ad7dec080c3",
  "toolUseResult": {
    "query": "Helix humanoid self-supervised pipeline data generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ACr9481FfJaTY2k9F7jx2Z",
        "content": [
          {
            "title": "Helix: A Vision-Language-Action Model for Generalist Humanoid Control",
            "url": "https://www.figure.ai/news/helix"
          },
          {
            "title": "Figure AI opens new 'Helix Lab' to accelerate learning for ...",
            "url": "https://mlq.ai/news/figure-ai-opens-new-helix-lab-to-accelerate-learning-for-its-humanoid-robots/"
          },
          {
            "title": "Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates",
            "url": "https://humanoid.press/"
          },
          {
            "title": "Embodied AI Milestone: Figure AI Unveils Helix 02 'Brain,' Achieving Breakthrough in Robotic Autonomous Housekeeping — BigGo Finance",
            "url": "https://finance.biggo.com/news/gkcKCJwBE5UokKawh-wG"
          },
          {
            "title": "Figure AI’s Helix: A Paradigm Shift in Humanoid Robotics and Embodied Intelligence — Foreign Affairs Forum",
            "url": "https://www.faf.ae/home/2025/2/22/figure-ais-helix-a-paradigm-shift-in-humanoid-robotics-and-embodied-intelligence"
          },
          {
            "title": "Figure's Helix: AI that Brings Human-Like Robots to your Home - Analytics Vidhya",
            "url": "https://www.analyticsvidhya.com/blog/2025/02/figures-helix/"
          },
          {
            "title": "Figure AI Announces Helix 02 - a General-Purpose Humanoid System - Luigi Freda",
            "url": "https://www.luigifreda.com/2026/02/02/figure-ai-announces-helix-02-a-general-purpose-humanoid-system/"
          },
          {
            "title": "Innovative Humanoid Robots in 2025–2026 - Reality or Hype?",
            "url": "https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"
          },
          {
            "title": "Figure AI Unveils Helix Model to Accelerate Home Robot Deployment",
            "url": "https://mikekalil.com/blog/figure-helix-ai/"
          },
          {
            "title": "Introducing Helix 02: Full-Body Autonomy",
            "url": "https://www.figure.ai/news/helix-02"
          }
        ]
      },
      "Based on the web search results, here's what I found about Helix, humanoid robots, self-supervised pipelines, and data generation in 2025-2026:\n\n## Helix Overview\n\nHelix is built on a Vision-Language-Action (VLA) framework, designed to enable humanoid robots to reason and operate with human-like capabilities. The system has evolved significantly during this period.\n\n## Data Generation and Training\n\n**Original Helix (2025):** Helix was trained with ~500 hours of high quality supervised data in total, a small fraction of the size of previously collected VLA datasets (<5%), and without any dependencies around multi-robot-embodiment collect or multiple stages of training. Unlike traditional robotic pipelines that separate perception, planning, and control, Helix integrates these functions into a single neural network trained through 500 hours of supervised human demonstrations.\n\n**Helix Lab and Self-Supervised Pipeline (2025-2026):** Figure AI presents the Helix Lab as a way to close the loop between data collection, simulation-based training, and on-robot learning. In this setup, egocentric human data gathered in the lab feeds into training pipelines, which may include simulated environments that reproduce recorded scenarios. By focusing on egocentric human video and interaction data, Figure is targeting the closest available proxy to what a robot will experience in deployment, rather than relying solely on external camera views or synthetic scenes.\n\n## Helix 02 (January 2026)\n\nHelix 02 extends capability to the entire robot - walking, manipulating, and balancing as one continuous system. Helix 02 unloads and reloads a dishwasher across a full-sized kitchen - a four-minute, end-to-end autonomous task that integrates walking, manipulation, and balance with no resets and no human intervention."
    ],
    "durationSeconds": 7.88680877600002
  },
  "sourceToolAssistantUUID": "4fd28ac1-e4ef-42a7-bb34-ec485463c35b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
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
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "bfe3a611-1a02-45d5-840f-0ad7dec080c3",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 48 · 2026-05-10T17:10:56.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9GX8DUrgBnt3j9pFuo2iD`</summary>

```json
{
  "query": "procedural scene generation robotic manipulation task diversity RoboCasa 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfe3a611-1a02-45d5-840f-0ad7dec080c3",
  "isSidechain": false,
  "requestId": "req_011CauG1jwskBNJjtdue3Jnr",
  "type": "assistant",
  "uuid": "c8b0f9c1-26fb-4911-affa-0ef7533a8392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bie47YDWtDKSprCM28b2SR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 33921,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 33921,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1138
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

_source line 49 · 2026-05-10T17:11:04.030Z_

<details><summary>↩ Tool result · `toolu_01L9GX8DUrgBnt3j9pFuo2iD`</summary>

```text
Web search results for query: "procedural scene generation robotic manipulation task diversity RoboCasa 2025 2026"

Links: [{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"Bringing robot skills from simulation to the real world","url":"https://itcanthink.substack.com/p/bringing-robot-skills-from-simulation"},{"title":"ROBOGROUND: Robotic Manipulation with Grounded Vision-Language Priors","url":"https://arxiv.org/pdf/2504.21530"},{"title":"[PDF] RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RoboCasa:-Large-Scale-Simulation-of-Everyday-Tasks-Nasiriany-Maddukuri/f773ceb43ffc7f9cd685250c4919924ec0bc85c7"},{"title":"(PDF) scene_synthesizer: A Python Library for Procedural Scene Generation in Robot Manipulation","url":"https://www.researchgate.net/publication/388467515_scene_synthesizer_A_Python_Library_for_Procedural_Scene_Generation_in_Robot_Manipulation"},{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/robocasa-large-scale-simulation-everyday-tasks-generalist"},{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots","url":"https://arxiv.org/html/2406.02523.pdf"},{"title":"GitHub - ZzZZCHS/RoboGround: Code & data for \"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors\" (CVPR 2025) · GitHub","url":"https://github.com/ZzZZCHS/RoboGround"},{"title":"AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation","url":"https://arxiv.org/html/2604.11674v1"}]

Based on the web search results, here's what I found about procedural scene generation for robotic manipulation task diversity in RoboCasa for 2025-2026:

## RoboCasa Overview

RoboCasa is a large-scale simulation framework for training generally capable robots to perform everyday tasks, featuring realistic and diverse human-centered environments with a focus on kitchen scenes.

## Procedural Scene Generation

The framework uses generative AI tools, such as large language models (LLMs) and text-to-image/3D generative models, to create these environments. RoboCasa includes a library of procedurally generated house environments, a collection of interactive objects commonly found in homes, and a suite of household activities that robots must learn to complete.

## Task Diversity and Latest Release

RoboCasa365, the latest release, includes 365 everyday tasks across 2,500 diverse kitchen environments, with 600+ hours of human demonstration data and 1,600+ hours of synthetically generated demonstrations. RoboCasa365 is associated with an ICLR 2026 paper.

RoboCasa uses large language models (LLMs), GPT-4 particularly, to define tasks, as they encapsulate a vast amount of common sense and world knowledge of the human world.

## Scene Customization

Each scene can be customized by replacing textures from a large selection of high-quality AI-generated textures created using text-to-image models from MidJourney, providing 100 textures for walls, floors, counters, and cabinet panels respectively, which serve as realistic domain randomization to increase visual diversity of training datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8b0f9c1-26fb-4911-affa-0ef7533a8392",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "50359dde-cb19-4d6d-b4bc-d0165b0fbc89",
  "toolUseResult": {
    "query": "procedural scene generation robotic manipulation task diversity RoboCasa 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013enify72WAi9vyTkFrzMZb",
        "content": [
          {
            "title": "RoboCasa",
            "url": "https://robocasa.ai/"
          },
          {
            "title": "RoboCasa: Scalable Household Robotics Simulation",
            "url": "https://www.emergentmind.com/topics/robocasa"
          },
          {
            "title": "Bringing robot skills from simulation to the real world",
            "url": "https://itcanthink.substack.com/p/bringing-robot-skills-from-simulation"
          },
          {
            "title": "ROBOGROUND: Robotic Manipulation with Grounded Vision-Language Priors",
            "url": "https://arxiv.org/pdf/2504.21530"
          },
          {
            "title": "[PDF] RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/RoboCasa:-Large-Scale-Simulation-of-Everyday-Tasks-Nasiriany-Maddukuri/f773ceb43ffc7f9cd685250c4919924ec0bc85c7"
          },
          {
            "title": "(PDF) scene_synthesizer: A Python Library for Procedural Scene Generation in Robot Manipulation",
            "url": "https://www.researchgate.net/publication/388467515_scene_synthesizer_A_Python_Library_for_Procedural_Scene_Generation_in_Robot_Manipulation"
          },
          {
            "title": "RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/robocasa-large-scale-simulation-everyday-tasks-generalist"
          },
          {
            "title": "RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots",
            "url": "https://arxiv.org/html/2406.02523.pdf"
          },
          {
            "title": "GitHub - ZzZZCHS/RoboGround: Code & data for \"RoboGround: Robotic Manipulation with Grounded Vision-Language Priors\" (CVPR 2025) · GitHub",
            "url": "https://github.com/ZzZZCHS/RoboGround"
          },
          {
            "title": "AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation",
            "url": "https://arxiv.org/html/2604.11674v1"
          }
        ]
      },
      "Based on the web search results, here's what I found about procedural scene generation for robotic manipulation task diversity in RoboCasa for 2025-2026:\n\n## RoboCasa Overview\n\nRoboCasa is a large-scale simulation framework for training generally capable robots to perform everyday tasks, featuring realistic and diverse human-centered environments with a focus on kitchen scenes.\n\n## Procedural Scene Generation\n\nThe framework uses generative AI tools, such as large language models (LLMs) and text-to-image/3D generative models, to create these environments. RoboCasa includes a library of procedurally generated house environments, a collection of interactive objects commonly found in homes, and a suite of household activities that robots must learn to complete.\n\n## Task Diversity and Latest Release\n\nRoboCasa365, the latest release, includes 365 everyday tasks across 2,500 diverse kitchen environments, with 600+ hours of human demonstration data and 1,600+ hours of synthetically generated demonstrations. RoboCasa365 is associated with an ICLR 2026 paper.\n\nRoboCasa uses large language models (LLMs), GPT-4 particularly, to define tasks, as they encapsulate a vast amount of common sense and world knowledge of the human world.\n\n## Scene Customization\n\nEach scene can be customized by replacing textures from a large selection of high-quality AI-generated textures created using text-to-image models from MidJourney, providing 100 textures for walls, floors, counters, and cabinet panels respectively, which serve as realistic domain randomization to increase visual diversity of training datasets."
    ],
    "durationSeconds": 7.710555867000017
  },
  "sourceToolAssistantUUID": "c8b0f9c1-26fb-4911-affa-0ef7533a8392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-10T17:11:06.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017NABGY6XYnfBQaJgn9PjMu`</summary>

```json
{
  "query": "latent trajectory diffusion model robot manipulation generalization 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50359dde-cb19-4d6d-b4bc-d0165b0fbc89",
  "isSidechain": false,
  "requestId": "req_011CauG2YGBmtY3KqnvXLpeQ",
  "type": "assistant",
  "uuid": "d96e2066-d266-4cac-8d3c-3434c9ac055c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYcdpSSoG1fScw1jLy6at2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 35059,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 35059,
          "cache_creation_input_tokens": 1040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1040
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

_source line 51 · 2026-05-10T17:11:14.694Z_

<details><summary>↩ Tool result · `toolu_017NABGY6XYnfBQaJgn9PjMu`</summary>

```text
Web search results for query: "latent trajectory diffusion model robot manipulation generalization 2025 2026 arxiv"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://arxiv.org/html/2502.10040v1"},{"title":"RoLD: Robot Latent Diffusion for Multi-task Policy Modeling","url":"https://arxiv.org/html/2403.07312"},{"title":"Diffusion Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2504.08438v1"},{"title":"World Models Can Leverage Human Videos for Dexterous Manipulation","url":"https://arxiv.org/html/2512.13644v1"},{"title":"[2502.10040] Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation","url":"https://arxiv.org/abs/2502.10040"},{"title":"Multi-task Manipulation Policy Modeling with Visuomotor Latent Diffusion","url":"https://arxiv.org/html/2403.07312v1"},{"title":"1 Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/pdf/2503.03464"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"}]

I found several relevant research papers and resources on latent trajectory diffusion models for robot manipulation with a focus on generalization. Here are the key findings:

## Notable Recent Papers

**1. RoLD: Robot Latent Diffusion (2024)**

This approach decouples robot action trajectory encoding and control policy generation by leveraging latent action trajectory spaces, enhancing the generalization ability of policy generation on multi-task manipulation tasks. The auto-encoder is pre-trained on the large-scale Open-X-Embodiment robot datasets with 24 diverse subsets across 7 various embodiments, and a latent diffusion process recovers Gaussian noise to the encoded latent action trajectory conditioned on task instructions and observations for effective multi-task policy modeling.

**2. Diffusion Trajectory-guided Policy (DTP) (2025)**

This framework utilizes diffusion trajectories generated in the RGB domain to enhance policy learning in long-horizon robot manipulation tasks, with the method facilitating the creation of additional training data through data augmentation or manually crafted labels, and involving two main stages: training a diffusion trajectory model to generate task-relevant trajectories and using these trajectories to guide the robot's manipulation policy. Validation on the CALVIN simulation benchmark showed the method outperformed state-of-the-art baselines by an average success rate of 25% across various settings.

## Survey Resources

Recent comprehensive surveys on diffusion models for robotic manipulation are available from 2025, covering various architectures, conditioning mechanisms, and applications in multi-task learning and generalization.

These papers represent the latest developments in using latent trajectory diffusion models to improve robot manipulation generalization capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d96e2066-d266-4cac-8d3c-3434c9ac055c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "ae6fe9a7-1ab4-4172-af67-fe14474bb4ea",
  "toolUseResult": {
    "query": "latent trajectory diffusion model robot manipulation generalization 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LHPAg8XTciXtTvW4GJ94ws",
        "content": [
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Frontiers | Diffusion models for robotic manipulation: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"
          },
          {
            "title": "Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation",
            "url": "https://arxiv.org/html/2502.10040v1"
          },
          {
            "title": "RoLD: Robot Latent Diffusion for Multi-task Policy Modeling",
            "url": "https://arxiv.org/html/2403.07312"
          },
          {
            "title": "Diffusion Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2504.08438v1"
          },
          {
            "title": "World Models Can Leverage Human Videos for Dexterous Manipulation",
            "url": "https://arxiv.org/html/2512.13644v1"
          },
          {
            "title": "[2502.10040] Diffusion Trajectory-guided Policy for Long-horizon Robot Manipulation",
            "url": "https://arxiv.org/abs/2502.10040"
          },
          {
            "title": "Multi-task Manipulation Policy Modeling with Visuomotor Latent Diffusion",
            "url": "https://arxiv.org/html/2403.07312v1"
          },
          {
            "title": "1 Generative Artificial Intelligence in Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/pdf/2503.03464"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          }
        ]
      },
      "I found several relevant research papers and resources on latent trajectory diffusion models for robot manipulation with a focus on generalization. Here are the key findings:\n\n## Notable Recent Papers\n\n**1. RoLD: Robot Latent Diffusion (2024)**\n\nThis approach decouples robot action trajectory encoding and control policy generation by leveraging latent action trajectory spaces, enhancing the generalization ability of policy generation on multi-task manipulation tasks. The auto-encoder is pre-trained on the large-scale Open-X-Embodiment robot datasets with 24 diverse subsets across 7 various embodiments, and a latent diffusion process recovers Gaussian noise to the encoded latent action trajectory conditioned on task instructions and observations for effective multi-task policy modeling.\n\n**2. Diffusion Trajectory-guided Policy (DTP) (2025)**\n\nThis framework utilizes diffusion trajectories generated in the RGB domain to enhance policy learning in long-horizon robot manipulation tasks, with the method facilitating the creation of additional training data through data augmentation or manually crafted labels, and involving two main stages: training a diffusion trajectory model to generate task-relevant trajectories and using these trajectories to guide the robot's manipulation policy. Validation on the CALVIN simulation benchmark showed the method outperformed state-of-the-art baselines by an average success rate of 25% across various settings.\n\n## Survey Resources\n\nRecent comprehensive surveys on diffusion models for robotic manipulation are available from 2025, covering various architectures, conditioning mechanisms, and applications in multi-task learning and generalization.\n\nThese papers represent the latest developments in using latent trajectory diffusion models to improve robot manipulation generalization capabilities."
    ],
    "durationSeconds": 7.692901299000019
  },
  "sourceToolAssistantUUID": "d96e2066-d266-4cac-8d3c-3434c9ac055c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-10T17:11:18.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RmzJBpXa11CS9VR1Qx2hZP`</summary>

```json
{
  "query": "humanoid data scarcity bottleneck VLA world model training solution 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae6fe9a7-1ab4-4172-af67-fe14474bb4ea",
  "isSidechain": false,
  "requestId": "req_011CauG3L9TBxumXyucEbMGR",
  "type": "assistant",
  "uuid": "87b80dbb-9d2a-48a9-881e-87d75947df5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jqp5omUkXSx4cduMJineBw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 36099,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 36099,
          "cache_creation_input_tokens": 941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 941
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

_source line 53 · 2026-05-10T17:11:26.699Z_

<details><summary>↩ Tool result · `toolu_01RmzJBpXa11CS9VR1Qx2hZP`</summary>

```text
Web search results for query: "humanoid data scarcity bottleneck VLA world model training solution 2026"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"Development of intelligent robots in the wave of embodied intelligence | National Science Review | Oxford Academic","url":"https://academic.oup.com/nsr/article/doi/10.1093/nsr/nwaf159/8120213"},{"title":"Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"},{"title":"VLA Model Training Data: Architectures, Needs & Challenges","url":"https://macgence.com/blog/vla-model-training-data"},{"title":"Unitree Opens the Floodgates: UnifoLM-WBT-Dataset Is the Largest Open – Warmcore Tech","url":"https://warmcore-tech.com/blogs/press/unitree-opens-the-floodgates-unifolm-wbt-dataset-is-the-largest-open-humanoid-teleoperation-dataset"},{"title":"Embodied AI Robot Large Model (Including VLA) Research Report, 2026","url":"https://www.researchandmarkets.com/reports/6232004/embodied-ai-robot-large-model-including-vla"},{"title":"EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos","url":"https://rchalyang.github.io/EgoVLA/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving | OpenReview","url":"https://openreview.net/forum?id=plrGn3RdzN"},{"title":"VLAs as Model Organisms for AI Safety","url":"https://www.lesswrong.com/posts/4p2HBMxCkh7pZ3xCa/vlas-as-model-organisms-for-ai-safety"}]

Based on the web search results, here's what I found regarding humanoid data scarcity bottlenecks and VLA/world model training solutions in 2026:

## Data Scarcity as a Core Bottleneck

The primary bottleneck for model development at present is the lack of training data. Data scarcity prevents the acquisition of loco-manipulation knowledge, particularly for humanoid robots that need to integrate both locomotion and manipulation capabilities. The core bottleneck is the cost of action-labeled trajectories—expensive teleoperation systems, skilled operators, and substantial collection time.

## Solutions Being Implemented

### World Models for Data Generation
Many enterprises have developed their own world models, such as Alibaba's WorldVLA, NVIDIA's WAM, Tencent Hunyuan 3D World Model, Unitree Robotics' UnifoLM-WMA-0, and AgiBot's GE-1. Unitree Robotics' UnifoLM-WMA-0 was released and open-sourced around September 2025. The simulation mode can generate high-fidelity synthetic data to solve the problem of scarcity of real robot training data.

### Alternative Training Approaches
There are two main approaches to address this issue: to collect data through human teleoperation, or to generate a large volume of virtual data using synthetic data generation techniques. Unified latent learning enables joint locomotion–manipulation learning from abundant low-cost action-free videos and alleviates the scarcity of teleoperation data.

### Recent Dataset Releases
On March 5, 2026, Unitree Robotics published the world's most comprehensive open-source dataset of real-world humanoid whole-body teleoperation — the UnifoLM-WBT-Dataset on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87b80dbb-9d2a-48a9-881e-87d75947df5e",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "f3fe57fb-1f50-4e42-9595-3a2777e4442f",
  "toolUseResult": {
    "query": "humanoid data scarcity bottleneck VLA world model training solution 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016Vjf4zvbCzvJNBHwRWWPpt",
        "content": [
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "Development of intelligent robots in the wave of embodied intelligence | National Science Review | Oxford Academic",
            "url": "https://academic.oup.com/nsr/article/doi/10.1093/nsr/nwaf159/8120213"
          },
          {
            "title": "Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA",
            "url": "https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"
          },
          {
            "title": "VLA Model Training Data: Architectures, Needs & Challenges",
            "url": "https://macgence.com/blog/vla-model-training-data"
          },
          {
            "title": "Unitree Opens the Floodgates: UnifoLM-WBT-Dataset Is the Largest Open – Warmcore Tech",
            "url": "https://warmcore-tech.com/blogs/press/unitree-opens-the-floodgates-unifolm-wbt-dataset-is-the-largest-open-humanoid-teleoperation-dataset"
          },
          {
            "title": "Embodied AI Robot Large Model (Including VLA) Research Report, 2026",
            "url": "https://www.researchandmarkets.com/reports/6232004/embodied-ai-robot-large-model-including-vla"
          },
          {
            "title": "EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos",
            "url": "https://rchalyang.github.io/EgoVLA/"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"
          },
          {
            "title": "DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving | OpenReview",
            "url": "https://openreview.net/forum?id=plrGn3RdzN"
          },
          {
            "title": "VLAs as Model Organisms for AI Safety",
            "url": "https://www.lesswrong.com/posts/4p2HBMxCkh7pZ3xCa/vlas-as-model-organisms-for-ai-safety"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding humanoid data scarcity bottlenecks and VLA/world model training solutions in 2026:\n\n## Data Scarcity as a Core Bottleneck\n\nThe primary bottleneck for model development at present is the lack of training data. Data scarcity prevents the acquisition of loco-manipulation knowledge, particularly for humanoid robots that need to integrate both locomotion and manipulation capabilities. The core bottleneck is the cost of action-labeled trajectories—expensive teleoperation systems, skilled operators, and substantial collection time.\n\n## Solutions Being Implemented\n\n### World Models for Data Generation\nMany enterprises have developed their own world models, such as Alibaba's WorldVLA, NVIDIA's WAM, Tencent Hunyuan 3D World Model, Unitree Robotics' UnifoLM-WMA-0, and AgiBot's GE-1. Unitree Robotics' UnifoLM-WMA-0 was released and open-sourced around September 2025. The simulation mode can generate high-fidelity synthetic data to solve the problem of scarcity of real robot training data.\n\n### Alternative Training Approaches\nThere are two main approaches to address this issue: to collect data through human teleoperation, or to generate a large volume of virtual data using synthetic data generation techniques. Unified latent learning enables joint locomotion–manipulation learning from abundant low-cost action-free videos and alleviates the scarcity of teleoperation data.\n\n### Recent Dataset Releases\nOn March 5, 2026, Unitree Robotics published the world's most comprehensive open-source dataset of real-world humanoid whole-body teleoperation — the UnifoLM-WBT-Dataset on Hugging Face."
    ],
    "durationSeconds": 8.460427144000016
  },
  "sourceToolAssistantUUID": "87b80dbb-9d2a-48a9-881e-87d75947df5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-10T17:11:29.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Aqfs6tsy14PCwK8KUyg3MB`</summary>

```json
{
  "query": "cross-embodiment data generation transfer learning humanoid robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3fe57fb-1f50-4e42-9595-3a2777e4442f",
  "isSidechain": false,
  "requestId": "req_011CauG4DKDatUf5acSd1MuU",
  "type": "assistant",
  "uuid": "d836fb0a-7c92-4564-b968-326aefa3c6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQyY9dTwtHrcw6ivLVdLGK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1080,
      "cache_read_input_tokens": 37040,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 37040,
          "cache_creation_input_tokens": 1080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1080
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

_source line 55 · 2026-05-10T17:11:38.976Z_

<details><summary>↩ Tool result · `toolu_01Aqfs6tsy14PCwK8KUyg3MB`</summary>

```text
Web search results for query: "cross-embodiment data generation transfer learning humanoid robot 2025 2026"

Links: [{"title":"Humanoid Policy ∼ Human Policy","url":"https://arxiv.org/html/2503.13441v3"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Cross-Embodiment Transfer in Robotics","url":"https://www.emergentmind.com/topics/cross-embodiment-transfer"},{"title":"[2412.15166] Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration","url":"https://arxiv.org/abs/2412.15166"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations","url":"https://arxiv.org/html/2511.04671v2"},{"title":"MITTY: DIFFUSION-BASED HUMAN-TO-ROBOT VIDEO ...","url":"https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf"},{"title":"Cross-Embodiment Robotic Manipulation Synthesis via Guided","url":"https://arxiv.org/pdf/2503.08622"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"Yuke Zhu GDC 3.422, 2317 Speedway, Austin, TX, 78712 USA https://yukezhu.me","url":"https://yukezhu.me/documents/yukez.pdf"}]

I've found comprehensive information about cross-embodiment data generation and transfer learning for humanoid robots in 2025-2026. Here's what the research shows:

## Key Developments in Cross-Embodiment Humanoid Robot Learning

### Human-to-Humanoid Data Transfer

Recent work investigates egocentric human demonstrations as cross-embodiment training data for robot learning, mitigating the embodiment gap between humanoids and humans from both data and modeling perspectives. One prominent approach is the Physical Human-Humanoid Data (PH2D) dataset, which collects hand-finger 3D poses from consumer-grade VR devices on manipulation tasks, training a Human Action Transformer that directly models humans as a different humanoid embodiment in an end-to-end manner.

### Cross-Embodiment Training Approaches

Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical, with approaches reducing the data bottleneck by using a unified digital human model as a common prototype. These frameworks learn behavior primitives from human demonstrations through adversarial imitation, decompose complex robot structures into functional components, and transfer skills to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning.

### Data Generation Techniques

Recent work achieves end-to-end generation of robot videos directly from human demonstrations without extracting intermediate representations such as pose, trajectories, or depth. Research on diverse datasets includes OXE-AugE, which augments robot datasets to uniform coverage of embodiments, and HPose, which aggregates human motion data to ensure millimeter-scale compatibility for humanoid transfer.

### Advanced Methods

Human-to-humanoid transfer frameworks use adversarial imitation learning and decomposed policies, with kinematic motion retargeting enabling transfer across multiple robot platforms while reducing fine-tuning time by 80-85% compared to training from scratch.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d836fb0a-7c92-4564-b968-326aefa3c6ab",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "6ef14515-27dd-4e1a-9c5d-214db6cfb061",
  "toolUseResult": {
    "query": "cross-embodiment data generation transfer learning humanoid robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QFgFLsppUSREJQizHwYSvC",
        "content": [
          {
            "title": "Humanoid Policy ∼ Human Policy",
            "url": "https://arxiv.org/html/2503.13441v3"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Cross-Embodiment Transfer in Robotics",
            "url": "https://www.emergentmind.com/topics/cross-embodiment-transfer"
          },
          {
            "title": "[2412.15166] Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration",
            "url": "https://arxiv.org/abs/2412.15166"
          },
          {
            "title": "GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub",
            "url": "https://github.com/YanjieZe/Paper-List"
          },
          {
            "title": "X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations",
            "url": "https://arxiv.org/html/2511.04671v2"
          },
          {
            "title": "MITTY: DIFFUSION-BASED HUMAN-TO-ROBOT VIDEO ...",
            "url": "https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf"
          },
          {
            "title": "Cross-Embodiment Robotic Manipulation Synthesis via Guided",
            "url": "https://arxiv.org/pdf/2503.08622"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "Yuke Zhu GDC 3.422, 2317 Speedway, Austin, TX, 78712 USA https://yukezhu.me",
            "url": "https://yukezhu.me/documents/yukez.pdf"
          }
        ]
      },
      "I've found comprehensive information about cross-embodiment data generation and transfer learning for humanoid robots in 2025-2026. Here's what the research shows:\n\n## Key Developments in Cross-Embodiment Humanoid Robot Learning\n\n### Human-to-Humanoid Data Transfer\n\nRecent work investigates egocentric human demonstrations as cross-embodiment training data for robot learning, mitigating the embodiment gap between humanoids and humans from both data and modeling perspectives. One prominent approach is the Physical Human-Humanoid Data (PH2D) dataset, which collects hand-finger 3D poses from consumer-grade VR devices on manipulation tasks, training a Human Action Transformer that directly models humans as a different humanoid embodiment in an end-to-end manner.\n\n### Cross-Embodiment Training Approaches\n\nGiven the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical, with approaches reducing the data bottleneck by using a unified digital human model as a common prototype. These frameworks learn behavior primitives from human demonstrations through adversarial imitation, decompose complex robot structures into functional components, and transfer skills to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning.\n\n### Data Generation Techniques\n\nRecent work achieves end-to-end generation of robot videos directly from human demonstrations without extracting intermediate representations such as pose, trajectories, or depth. Research on diverse datasets includes OXE-AugE, which augments robot datasets to uniform coverage of embodiments, and HPose, which aggregates human motion data to ensure millimeter-scale compatibility for humanoid transfer.\n\n### Advanced Methods\n\nHuman-to-humanoid transfer frameworks use adversarial imitation learning and decomposed policies, with kinematic motion retargeting enabling transfer across multiple robot platforms while reducing fine-tuning time by 80-85% compared to training from scratch."
    ],
    "durationSeconds": 9.093786355999997
  },
  "sourceToolAssistantUUID": "d836fb0a-7c92-4564-b968-326aefa3c6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-10T17:11:38.982Z_

```json
{
  "parentUuid": "6ef14515-27dd-4e1a-9c5d-214db6cfb061",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a8d0829d-e31d-48c7-aae9-87e26c0180b2",
  "timestamp": "2026-05-10T17:11:38.982Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "a8d0829d-e31d-48c7-aae9-87e26c0180b2",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 59 · 2026-05-10T17:11:42.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JJEK4KLkd7NPzzTVmHFX2Q`</summary>

```json
{
  "query": "automatic quality filtering synthetic robot trajectories physics consistency validation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8d0829d-e31d-48c7-aae9-87e26c0180b2",
  "isSidechain": false,
  "requestId": "req_011CauG57ncGaLqcgDHGDD1p",
  "type": "assistant",
  "uuid": "d3311cc4-7e6d-4b4a-be1e-613f88fbe54b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9MmHjDwX2auKHdZKiqMSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1200,
      "cache_read_input_tokens": 38120,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 38120,
          "cache_creation_input_tokens": 1200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1200
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

_source line 60 · 2026-05-10T17:11:50.269Z_

<details><summary>↩ Tool result · `toolu_01JJEK4KLkd7NPzzTVmHFX2Q`</summary>

```text
Web search results for query: "automatic quality filtering synthetic robot trajectories physics consistency validation 2025 2026"

Links: [{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=748bHL2BAv"},{"title":"[2510.10125] Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/abs/2510.10125"},{"title":"Ctrl-World: A Controllable Generative World Model for Robot Manipulation","url":"https://arxiv.org/html/2510.10125v3"},{"title":"Ai et al., Sci. Robot. 10, eadt1497 (2025) 17 September 2025","url":"https://albertboai.com/assets/pdf/2025_scirobotics.adt1497.pdf"},{"title":"Interactive World Simulator for Robot Policy Training and Evaluation","url":"https://www.yixuanwang.me/interactive_world_sim/texts/main.pdf"},{"title":"Boosting Offline MARL under Imbalanced Datasets via ...","url":"https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"},{"title":"Robotics May 2025","url":"https://www.arxiv.org/list/cs.RO/2025-05?skip=650&show=1000"},{"title":"Robotics Mar 2025","url":"https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"}]

Based on the search results, I found several relevant papers and research from 2025-2026 related to robot trajectory generation and synthesis. Here are the key findings:

## Key Research on Synthetic Robot Trajectories

Ctrl-World generates spatially and temporally consistent trajectories under novel scenarios and new camera placements for over 20 seconds, using the DROID dataset (95k trajectories, 564 scenes). Baseline models struggle to capture robot–object interactions and often generate hallucinated predictions, highlighting the need for quality filtering.

## Approaches to Quality and Consistency Validation

The model maintains long-horizon consistency with a pose-conditioned memory retrieval mechanism and achieves precise action control through frame-level action conditioning. Notably, some works leverage video prediction models to synthesize robotic trajectories with fake action labels, and these synthetic trajectories can then be used for policy learning.

## Physics-Based World Modeling

Errors in video prediction accumulate over time, which leads to compromised action accuracy and downstream policy performance, addressing a key challenge in synthetic trajectory validation. Recent research is exploring unified approaches that better model physics and dynamics consistency.

The search results show active development in this area, with multiple 2025-2026 papers addressing consistency validation, though specific dedicated work on "automatic quality filtering" with explicit physics consistency validation appears to be an emerging focus area rather than an established domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3311cc4-7e6d-4b4a-be1e-613f88fbe54b",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "2e931e10-1a18-4848-9259-f0188c3b8c41",
  "toolUseResult": {
    "query": "automatic quality filtering synthetic robot trajectories physics consistency validation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0182nUTLJHHUfPk68cvSAh64",
        "content": [
          {
            "title": "Ctrl-World: A Controllable Generative World Model for Robot Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=748bHL2BAv"
          },
          {
            "title": "[2510.10125] Ctrl-World: A Controllable Generative World Model for Robot Manipulation",
            "url": "https://arxiv.org/abs/2510.10125"
          },
          {
            "title": "Ctrl-World: A Controllable Generative World Model for Robot Manipulation",
            "url": "https://arxiv.org/html/2510.10125v3"
          },
          {
            "title": "Ai et al., Sci. Robot. 10, eadt1497 (2025) 17 September 2025",
            "url": "https://albertboai.com/assets/pdf/2025_scirobotics.adt1497.pdf"
          },
          {
            "title": "Interactive World Simulator for Robot Policy Training and Evaluation",
            "url": "https://www.yixuanwang.me/interactive_world_sim/texts/main.pdf"
          },
          {
            "title": "Boosting Offline MARL under Imbalanced Datasets via ...",
            "url": "https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"
          },
          {
            "title": "Robotics May 2025",
            "url": "https://www.arxiv.org/list/cs.RO/2025-05?skip=650&show=1000"
          },
          {
            "title": "Robotics Mar 2025",
            "url": "https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"
          },
          {
            "title": "World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/html/2602.15922v1"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and research from 2025-2026 related to robot trajectory generation and synthesis. Here are the key findings:\n\n## Key Research on Synthetic Robot Trajectories\n\nCtrl-World generates spatially and temporally consistent trajectories under novel scenarios and new camera placements for over 20 seconds, using the DROID dataset (95k trajectories, 564 scenes). Baseline models struggle to capture robot–object interactions and often generate hallucinated predictions, highlighting the need for quality filtering.\n\n## Approaches to Quality and Consistency Validation\n\nThe model maintains long-horizon consistency with a pose-conditioned memory retrieval mechanism and achieves precise action control through frame-level action conditioning. Notably, some works leverage video prediction models to synthesize robotic trajectories with fake action labels, and these synthetic trajectories can then be used for policy learning.\n\n## Physics-Based World Modeling\n\nErrors in video prediction accumulate over time, which leads to compromised action accuracy and downstream policy performance, addressing a key challenge in synthetic trajectory validation. Recent research is exploring unified approaches that better model physics and dynamics consistency.\n\nThe search results show active development in this area, with multiple 2025-2026 papers addressing consistency validation, though specific dedicated work on \"automatic quality filtering\" with explicit physics consistency validation appears to be an emerging focus area rather than an established domain."
    ],
    "durationSeconds": 7.538656078999979
  },
  "sourceToolAssistantUUID": "d3311cc4-7e6d-4b4a-be1e-613f88fbe54b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-10T17:11:52.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mr2xLJ3RgG6HQV8tkCFNGw`</summary>

```json
{
  "query": "compositional task generation LLM robotics procedural environment 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e931e10-1a18-4848-9259-f0188c3b8c41",
  "isSidechain": false,
  "requestId": "req_011CauG5wwZ6yjhdw1JDutQS",
  "type": "assistant",
  "uuid": "b455808f-d75d-40dc-b926-9e15dc98c4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qgDjpJh7ToCQnaV9xVxv8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 39320,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 39320,
          "cache_creation_input_tokens": 867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 867
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

_source line 62 · 2026-05-10T17:12:01.487Z_

<details><summary>↩ Tool result · `toolu_01Mr2xLJ3RgG6HQV8tkCFNGw`</summary>

```text
Web search results for query: "compositional task generation LLM robotics procedural environment 2025 2026"

Links: [{"title":"Procedural Environment Generation for Tool-Use Agents","url":"https://arxiv.org/html/2506.11045"},{"title":"GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub","url":"https://github.com/GT-RIPL/Awesome-LLM-Robotics"},{"title":"ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10514-023-10135-3"},{"title":"MALMM: Multi-Agent Large Language Models for Zero-Shot Robotic Manipulation","url":"https://malmm1.github.io/assets/IROS_2025_malmm_v8.pdf"},{"title":"LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-20653-y"},{"title":"Hierarchical Planning for Complex Tasks with Knowledge ...","url":"https://openreview.net/pdf/558e2ff2c7126b87206d9de23de763294a28a6ee.pdf"},{"title":"Language-Driven Procedural Generation","url":"https://www.emergentmind.com/topics/language-driven-procedural-environment-generation"},{"title":"Boosting Offline MARL under Imbalanced Datasets via ...","url":"https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"},{"title":"ProgPrompt","url":"https://progprompt.github.io/"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.10690"}]

Here are the search results for your query on compositional task generation, LLMs, robotics, and procedural environments in 2025-2026:

## Key Findings

**Procedural Environment Generation**

A RandomWorld environment demonstrates agents executing non-linear, compositional tasks with interactive tools through LLM-driven generation of tasks and environments. A procedural environment generation approach achieved approximately 60% pass rate for environment generation, with tasks generated that are more complex than an LLM alone could envision, providing richer training data.

**LLM-Based Robotics Applications**

Recent work demonstrates multiple approaches:
- LLMs fine-tuned for tool use through online reinforcement learning can better adapt to tools and tasks not seen during training
- Multi-agent frameworks leverage collaborative and role-specific reasoning capabilities of multiple LLM agents to complete complex manipulation tasks
- LLMs' planning capabilities are leveraged alongside reinforcement learning to facilitate learning from the environment

**Language-Driven Procedural Generation**

Sequential LLM- or Transformer-based modules map prompt → annotation → layout, or story → keyframes → scene objects, often combined with multimodal object retrieval or 3D asset generation. Notable systems include 3D driving scenarios with dynamic interaction and traffic simulation, tightly aligned to language instructions for robotics and autonomous vehicles.

**Compositional Task Planning**

Evaluation frameworks assess the reasoning and compositional capabilities of LLMs in robotic simulators, with symbolic verification and hierarchical planning integrated within RAG-enhanced LLM-based planners to address complex, long-horizon tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b455808f-d75d-40dc-b926-9e15dc98c4a4",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "862b2149-17c7-4d2b-8a14-d43131db83d2",
  "toolUseResult": {
    "query": "compositional task generation LLM robotics procedural environment 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XzRYkzTfGmgWopcFqiAAc6",
        "content": [
          {
            "title": "Procedural Environment Generation for Tool-Use Agents",
            "url": "https://arxiv.org/html/2506.11045"
          },
          {
            "title": "GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub",
            "url": "https://github.com/GT-RIPL/Awesome-LLM-Robotics"
          },
          {
            "title": "ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10514-023-10135-3"
          },
          {
            "title": "MALMM: Multi-Agent Large Language Models for Zero-Shot Robotic Manipulation",
            "url": "https://malmm1.github.io/assets/IROS_2025_malmm_v8.pdf"
          },
          {
            "title": "LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-20653-y"
          },
          {
            "title": "Hierarchical Planning for Complex Tasks with Knowledge ...",
            "url": "https://openreview.net/pdf/558e2ff2c7126b87206d9de23de763294a28a6ee.pdf"
          },
          {
            "title": "Language-Driven Procedural Generation",
            "url": "https://www.emergentmind.com/topics/language-driven-procedural-environment-generation"
          },
          {
            "title": "Boosting Offline MARL under Imbalanced Datasets via ...",
            "url": "https://www.lamda.nju.edu.cn/lilh/file/codi.pdf"
          },
          {
            "title": "ProgPrompt",
            "url": "https://progprompt.github.io/"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.10690"
          }
        ]
      },
      "Here are the search results for your query on compositional task generation, LLMs, robotics, and procedural environments in 2025-2026:\n\n## Key Findings\n\n**Procedural Environment Generation**\n\nA RandomWorld environment demonstrates agents executing non-linear, compositional tasks with interactive tools through LLM-driven generation of tasks and environments. A procedural environment generation approach achieved approximately 60% pass rate for environment generation, with tasks generated that are more complex than an LLM alone could envision, providing richer training data.\n\n**LLM-Based Robotics Applications**\n\nRecent work demonstrates multiple approaches:\n- LLMs fine-tuned for tool use through online reinforcement learning can better adapt to tools and tasks not seen during training\n- Multi-agent frameworks leverage collaborative and role-specific reasoning capabilities of multiple LLM agents to complete complex manipulation tasks\n- LLMs' planning capabilities are leveraged alongside reinforcement learning to facilitate learning from the environment\n\n**Language-Driven Procedural Generation**\n\nSequential LLM- or Transformer-based modules map prompt → annotation → layout, or story → keyframes → scene objects, often combined with multimodal object retrieval or 3D asset generation. Notable systems include 3D driving scenarios with dynamic interaction and traffic simulation, tightly aligned to language instructions for robotics and autonomous vehicles.\n\n**Compositional Task Planning**\n\nEvaluation frameworks assess the reasoning and compositional capabilities of LLMs in robotic simulators, with symbolic verification and hierarchical planning integrated within RAG-enhanced LLM-based planners to address complex, long-horizon tasks."
    ],
    "durationSeconds": 8.72105787400002
  },
  "sourceToolAssistantUUID": "b455808f-d75d-40dc-b926-9e15dc98c4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-10T17:12:05.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UfRcwTuxDXUMdHwAy7GZ3N`</summary>

```json
{
  "query": "humanoid robot kinematic tree graph neural network policy learning structured action space 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "862b2149-17c7-4d2b-8a14-d43131db83d2",
  "isSidechain": false,
  "requestId": "req_011CauG6n9DmqJLiaoxMqRNv",
  "type": "assistant",
  "uuid": "41a67c79-ffbc-435f-84fd-d0b8e1694d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQrAU3kg6qT5jmR4E9kJ64",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 40187,
      "output_tokens": 68,
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
          "output_tokens": 68,
          "cache_read_input_tokens": 40187,
          "cache_creation_input_tokens": 948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 948
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

_source line 64 · 2026-05-10T17:12:12.428Z_

<details><summary>↩ Tool result · `toolu_01UfRcwTuxDXUMdHwAy7GZ3N`</summary>

```text
Web search results for query: "humanoid robot kinematic tree graph neural network policy learning structured action space 2025"

Links: [{"title":"NERVENET: LEARNING STRUCTURED POLICY WITH ...","url":"https://openreview.net/pdf?id=S1sqHMZCb"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Foundation Control Model for General Embodied Intelligence Wenli Xiao","url":"https://www.ri.cmu.edu/app/uploads/2025/05/MSR_Thesis-1.pdf"},{"title":"Real-world humanoid locomotion with reinforcement learning | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adi9579"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"Research on humanoid robot motion generation and real-time trajectory optimization based on sparse attention mechanism in deep reinforcement learning | Discover Artificial Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44163-025-00603-3"},{"title":"Survey on Graph-Based Reinforcement Learning for Networked Coordination and Control","url":"https://www.mdpi.com/2673-4052/6/4/65"},{"title":"Learning Robust Humanoid Control via Curriculum and Policy ...","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-87.pdf"}]

Based on the web search results, I found several relevant papers and resources on humanoid robot control using graph neural networks and structured approaches:

## Key Findings

**Graph Neural Networks for Robot Control:**

Researchers define agent policies using Graph Neural Networks, which operate over graph structures. Known as NerveNet due to its resemblance to the neural nervous system, this approach propagates information between different parts of the body based on the underlying graph structure before outputting actions for each part.

**Kinematic Tree Structure:**

Robot and animal skeletons have a discrete graph structure that is most often trees, with simulators like MuJoCo organizing agents using an XML-based kinematic tree. These trees assume two types of nodes: body nodes and joint nodes, where joint nodes represent the degrees of freedom of motion between body nodes.

**Action Space Structure:**

Many reinforcement learning problems feature agents with multiple dependent controllers, such as humanoid robots consisting of multiple physically linked joints, where actions taken by each joint should depend not only on its own observations but also on actions of other joints.

**Recent 2025 Research:**

The search results indicate active research in humanoid robot learning in 2025, including work on kinematics-aware multi-policy reinforcement learning for force-capable humanoid loco-manipulation and force-adaptive control frameworks for humanoid robots. Additionally, graph neural networks have been increasingly adopted for reward modeling in reinforcement learning due to their ability to capture structural dependencies among agents, states, and actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41a67c79-ffbc-435f-84fd-d0b8e1694d7c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "050214c9-3428-4622-94a6-fcd0b3f58a29",
  "toolUseResult": {
    "query": "humanoid robot kinematic tree graph neural network policy learning structured action space 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015AvJhRjJ3hYkqRjznKLM1T",
        "content": [
          {
            "title": "NERVENET: LEARNING STRUCTURED POLICY WITH ...",
            "url": "https://openreview.net/pdf?id=S1sqHMZCb"
          },
          {
            "title": "Advancements in humanoid robot dynamics and learning-based locomotion control methods",
            "url": "https://www.oaepublish.com/articles/ir.2025.32"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Foundation Control Model for General Embodied Intelligence Wenli Xiao",
            "url": "https://www.ri.cmu.edu/app/uploads/2025/05/MSR_Thesis-1.pdf"
          },
          {
            "title": "Real-world humanoid locomotion with reinforcement learning | Science Robotics",
            "url": "https://www.science.org/doi/10.1126/scirobotics.adi9579"
          },
          {
            "title": "Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors",
            "url": "https://arxiv.org/html/2501.02116v1"
          },
          {
            "title": "GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub",
            "url": "https://github.com/YanjieZe/Paper-List"
          },
          {
            "title": "Research on humanoid robot motion generation and real-time trajectory optimization based on sparse attention mechanism in deep reinforcement learning | Discover Artificial Intelligence | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s44163-025-00603-3"
          },
          {
            "title": "Survey on Graph-Based Reinforcement Learning for Networked Coordination and Control",
            "url": "https://www.mdpi.com/2673-4052/6/4/65"
          },
          {
            "title": "Learning Robust Humanoid Control via Curriculum and Policy ...",
            "url": "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-87.pdf"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and resources on humanoid robot control using graph neural networks and structured approaches:\n\n## Key Findings\n\n**Graph Neural Networks for Robot Control:**\n\nResearchers define agent policies using Graph Neural Networks, which operate over graph structures. Known as NerveNet due to its resemblance to the neural nervous system, this approach propagates information between different parts of the body based on the underlying graph structure before outputting actions for each part.\n\n**Kinematic Tree Structure:**\n\nRobot and animal skeletons have a discrete graph structure that is most often trees, with simulators like MuJoCo organizing agents using an XML-based kinematic tree. These trees assume two types of nodes: body nodes and joint nodes, where joint nodes represent the degrees of freedom of motion between body nodes.\n\n**Action Space Structure:**\n\nMany reinforcement learning problems feature agents with multiple dependent controllers, such as humanoid robots consisting of multiple physically linked joints, where actions taken by each joint should depend not only on its own observations but also on actions of other joints.\n\n**Recent 2025 Research:**\n\nThe search results indicate active research in humanoid robot learning in 2025, including work on kinematics-aware multi-policy reinforcement learning for force-capable humanoid loco-manipulation and force-adaptive control frameworks for humanoid robots. Additionally, graph neural networks have been increasingly adopted for reward modeling in reinforcement learning due to their ability to capture structural dependencies among agents, states, and actions."
    ],
    "durationSeconds": 7.146358632000018
  },
  "sourceToolAssistantUUID": "41a67c79-ffbc-435f-84fd-d0b8e1694d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-10T17:12:15.167Z_

Let me now search for more specific gaps and cross-domain inspiration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "050214c9-3428-4622-94a6-fcd0b3f58a29",
  "isSidechain": false,
  "requestId": "req_011CauG7ahB1iPsLUkyTcMNc",
  "type": "assistant",
  "uuid": "7690f202-08b6-43c6-9236-9c256aefd07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bWby6PofsDZjVNQoXH5EA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 41135,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 41135,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 956
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

_source line 66 · 2026-05-10T17:12:15.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0164V89shAgxiHf9TsrN9jGi`</summary>

```json
{
  "query": "\"action-conditioned video generation\" humanoid whole-body 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7690f202-08b6-43c6-9236-9c256aefd07b",
  "isSidechain": false,
  "requestId": "req_011CauG7ahB1iPsLUkyTcMNc",
  "type": "assistant",
  "uuid": "0fb5daa9-0c7e-4a78-ade7-e530b4172d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bWby6PofsDZjVNQoXH5EA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 41135,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 41135,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 956
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

_source line 67 · 2026-05-10T17:12:24.116Z_

<details><summary>↩ Tool result · `toolu_0164V89shAgxiHf9TsrN9jGi`</summary>

```text
Web search results for query: ""action-conditioned video generation" humanoid whole-body 2025 2026"

Links: [{"title":"[2502.14795] Humanoid-VLA: Towards Universal Humanoid Control with Visual Integration","url":"https://arxiv.org/abs/2502.14795"},{"title":"ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control","url":"https://arxiv.org/html/2604.27711v1"},{"title":"Whole-Body Conditioned Egocentric Video Prediction – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2025/07/01/peva/"},{"title":"Visual Imitation Enables Contextual Humanoid Control","url":"https://arxiv.org/html/2505.03729v1"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"MultiModal Action Conditioned Video Generation","url":"https://arxiv.org/html/2510.02287"},{"title":"LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction","url":"https://arxiv.org/html/2506.13751v3"},{"title":"Universal Humanoid Robot Pose Learning from Internet Human Videos | OpenReview","url":"https://openreview.net/forum?id=2pBjMDj6uJ"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=action-conditioned+video+generation"},{"title":"arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control","url":"https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"}]

The search results reveal several recent developments in action-conditioned video generation and humanoid whole-body control for 2025-2026:

## Key Research Areas

### Action-Conditioned Video Generation
Current video models lack fine-grained control needed for household robots requiring real-time fine motor control, so researchers have introduced fine-grained multimodal actions to capture such precise control. RealWonder is the first real-time system for action-conditioned video generation from a single image, using physics simulation as an intermediate bridge to translate continuous actions into visual representations that video models can process, integrating 3D reconstruction, physics simulation, and a distilled video generator.

### Humanoid Whole-Body Control
ExoActor is a framework that bridges generative video modeling and humanoid control through third-person video generation. PEVA (Predicting Ego-centric Video from human Actions) predicts the next video frame given past video frames and an action specifying a desired change in 3D pose.

### Vision-Language-Action Models
Humanoid-VLA begins with language-motion pre-alignment using non-egocentric human motion datasets, then incorporates egocentric visual context through parameter efficient video-conditioned fine-tuning for context-aware motion generation. LeVERB (Latent Vision-Language-Encoded Robot Behavior) is a hierarchical latent instruction-following framework for humanoid vision-language whole-body control.

Human video-based learning has also emerged as a key approach, with VideoMimic being a real-to-sim-to-real pipeline that produces whole-body control policies for humanoid robots from everyday videos, demonstrating robust contextual control for skills like staircase ascents and descents and sitting from chairs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb5daa9-0c7e-4a78-ade7-e530b4172d9b",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "7288780d-2ff5-472e-a4a3-89cb07cb530e",
  "toolUseResult": {
    "query": "\"action-conditioned video generation\" humanoid whole-body 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MWeSa3Bjd3zLwoX2Zfe1sa",
        "content": [
          {
            "title": "[2502.14795] Humanoid-VLA: Towards Universal Humanoid Control with Visual Integration",
            "url": "https://arxiv.org/abs/2502.14795"
          },
          {
            "title": "ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control",
            "url": "https://arxiv.org/html/2604.27711v1"
          },
          {
            "title": "Whole-Body Conditioned Egocentric Video Prediction – The Berkeley Artificial Intelligence Research Blog",
            "url": "https://bair.berkeley.edu/blog/2025/07/01/peva/"
          },
          {
            "title": "Visual Imitation Enables Contextual Humanoid Control",
            "url": "https://arxiv.org/html/2505.03729v1"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "MultiModal Action Conditioned Video Generation",
            "url": "https://arxiv.org/html/2510.02287"
          },
          {
            "title": "LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction",
            "url": "https://arxiv.org/html/2506.13751v3"
          },
          {
            "title": "Universal Humanoid Robot Pose Learning from Internet Human Videos | OpenReview",
            "url": "https://openreview.net/forum?id=2pBjMDj6uJ"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=action-conditioned+video+generation"
          },
          {
            "title": "arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control",
            "url": "https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"
          }
        ]
      },
      "The search results reveal several recent developments in action-conditioned video generation and humanoid whole-body control for 2025-2026:\n\n## Key Research Areas\n\n### Action-Conditioned Video Generation\nCurrent video models lack fine-grained control needed for household robots requiring real-time fine motor control, so researchers have introduced fine-grained multimodal actions to capture such precise control. RealWonder is the first real-time system for action-conditioned video generation from a single image, using physics simulation as an intermediate bridge to translate continuous actions into visual representations that video models can process, integrating 3D reconstruction, physics simulation, and a distilled video generator.\n\n### Humanoid Whole-Body Control\nExoActor is a framework that bridges generative video modeling and humanoid control through third-person video generation. PEVA (Predicting Ego-centric Video from human Actions) predicts the next video frame given past video frames and an action specifying a desired change in 3D pose.\n\n### Vision-Language-Action Models\nHumanoid-VLA begins with language-motion pre-alignment using non-egocentric human motion datasets, then incorporates egocentric visual context through parameter efficient video-conditioned fine-tuning for context-aware motion generation. LeVERB (Latent Vision-Language-Encoded Robot Behavior) is a hierarchical latent instruction-following framework for humanoid vision-language whole-body control.\n\nHuman video-based learning has also emerged as a key approach, with VideoMimic being a real-to-sim-to-real pipeline that produces whole-body control policies for humanoid robots from everyday videos, demonstrating robust contextual control for skills like staircase ascents and descents and sitting from chairs."
    ],
    "durationSeconds": 8.658591306000016
  },
  "sourceToolAssistantUUID": "0fb5daa9-0c7e-4a78-ade7-e530b4172d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "7288780d-2ff5-472e-a4a3-89cb07cb530e",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 70 · 2026-05-10T17:12:27.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Cbb34gZCLBzYJTRKKc4hU`</summary>

```json
{
  "query": "GR00T Dreams synthetic trajectory Cosmos world model humanoid data augmentation pipeline arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7288780d-2ff5-472e-a4a3-89cb07cb530e",
  "isSidechain": false,
  "requestId": "req_011CauG8Sij6x5p9RxeASgC2",
  "type": "assistant",
  "uuid": "4c55d030-d7b5-4ce0-8da5-37f9495f1cfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019k2oecc85thwDqaixj5yn8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 42091,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 42091,
          "cache_creation_input_tokens": 1018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1018
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

_source line 71 · 2026-05-10T17:12:35.368Z_

<details><summary>↩ Tool result · `toolu_014Cbb34gZCLBzYJTRKKc4hU`</summary>

```text
Web search results for query: "GR00T Dreams synthetic trajectory Cosmos world model humanoid data augmentation pipeline arxiv 2025"

Links: [{"title":"Enhance Robot Learning with Synthetic Trajectory Data Generated by World Foundation Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://arxiv.org/html/2505.12705v1"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v2"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"GitHub - NVIDIA/GR00T-Dreams: DreamGen: Nvidia GEAR Lab's initiative to solve the robotics data problem using world models · GitHub","url":"https://github.com/nvidia/GR00T-dreams"},{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer","url":"https://developer.nvidia.com/isaac/gr00t"},{"title":"From Generated Human Videos to Physically Plausible Robot Trajectories","url":"https://arxiv.org/html/2512.05094"},{"title":"R²D²: Training Generalist Robots with NVIDIA Research Workflows and World Foundation Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/r2d2-training-generalist-robots-with-nvidia-research-workflows-and-world-foundation-models/"},{"title":"GR00T-Dreams (DreamGen) | sudoremove","url":"https://sudoremove.com/en/knowledge/models/dreamgen/"}]

Based on the search results, here's what I found about GR00T Dreams, synthetic trajectory generation, and the Cosmos world model for humanoid robot data augmentation:

## Overview

The Isaac GR00T-Dreams blueprint is a reference workflow for generating vast amounts of synthetic trajectory data used for teaching humanoid robots to perform new actions in novel environments.

## Core Technology

The NVIDIA Isaac GR00T-Dreams blueprint, built on NVIDIA Cosmos, solves the robotics data bottleneck by generating massive synthetic trajectory data from just a single image and language, using Cosmos world foundation models (WFMs) and generative AI to rapidly create training data for models such as NVIDIA Isaac GR00T N1.5.

## Data Augmentation Pipeline

The pipeline pre-trains models end-to-end across three data layers, spanning (annotated) video datasets, synthetically generated datasets, and real-robot trajectories — by sampling training batches across this heterogeneous data mixture.

To train with action-less data sources such as human videos and neural-generated videos, techniques include learning a latent-action codebook and using a trained inverse dynamics model (IDM) to infer pseudo-actions, enabling annotation of actions on action-less videos.

## Key Results

Using the GR00T-Dreams blueprint, NVIDIA Research developed GR00T N1.5, an update to the world's first open foundation model for generalized humanoid robot reasoning and skills, in just 36 hours, a task that would have taken nearly three months with manual data collection.

For the latest arXiv paper, the DreamGen research (arxiv:2505.12705) appears to be the research foundation underlying the GR00T-Dreams blueprint, demonstrating how to leverage video world models for synthetic trajectory generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c55d030-d7b5-4ce0-8da5-37f9495f1cfa",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "15aa4ca9-f788-446a-95d0-3560f42b717b",
  "toolUseResult": {
    "query": "GR00T Dreams synthetic trajectory Cosmos world model humanoid data augmentation pipeline arxiv 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013jsWac8ERhqpWmAV63Wetc",
        "content": [
          {
            "title": "Enhance Robot Learning with Synthetic Trajectory Data Generated by World Foundation Models | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/"
          },
          {
            "title": "DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories",
            "url": "https://arxiv.org/html/2505.12705v1"
          },
          {
            "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/html/2503.14734v2"
          },
          {
            "title": "2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/pdf/2503.14734"
          },
          {
            "title": "GitHub - NVIDIA/GR00T-Dreams: DreamGen: Nvidia GEAR Lab's initiative to solve the robotics data problem using world models · GitHub",
            "url": "https://github.com/nvidia/GR00T-dreams"
          },
          {
            "title": "Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"
          },
          {
            "title": "Isaac GR00T - Generalist Robot 00 Technology | NVIDIA Developer",
            "url": "https://developer.nvidia.com/isaac/gr00t"
          },
          {
            "title": "From Generated Human Videos to Physically Plausible Robot Trajectories",
            "url": "https://arxiv.org/html/2512.05094"
          },
          {
            "title": "R²D²: Training Generalist Robots with NVIDIA Research Workflows and World Foundation Models | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/r2d2-training-generalist-robots-with-nvidia-research-workflows-and-world-foundation-models/"
          },
          {
            "title": "GR00T-Dreams (DreamGen) | sudoremove",
            "url": "https://sudoremove.com/en/knowledge/models/dreamgen/"
          }
        ]
      },
      "Based on the search results, here's what I found about GR00T Dreams, synthetic trajectory generation, and the Cosmos world model for humanoid robot data augmentation:\n\n## Overview\n\nThe Isaac GR00T-Dreams blueprint is a reference workflow for generating vast amounts of synthetic trajectory data used for teaching humanoid robots to perform new actions in novel environments.\n\n## Core Technology\n\nThe NVIDIA Isaac GR00T-Dreams blueprint, built on NVIDIA Cosmos, solves the robotics data bottleneck by generating massive synthetic trajectory data from just a single image and language, using Cosmos world foundation models (WFMs) and generative AI to rapidly create training data for models such as NVIDIA Isaac GR00T N1.5.\n\n## Data Augmentation Pipeline\n\nThe pipeline pre-trains models end-to-end across three data layers, spanning (annotated) video datasets, synthetically generated datasets, and real-robot trajectories — by sampling training batches across this heterogeneous data mixture.\n\nTo train with action-less data sources such as human videos and neural-generated videos, techniques include learning a latent-action codebook and using a trained inverse dynamics model (IDM) to infer pseudo-actions, enabling annotation of actions on action-less videos.\n\n## Key Results\n\nUsing the GR00T-Dreams blueprint, NVIDIA Research developed GR00T N1.5, an update to the world's first open foundation model for generalized humanoid robot reasoning and skills, in just 36 hours, a task that would have taken nearly three months with manual data collection.\n\nFor the latest arXiv paper, the DreamGen research (arxiv:2505.12705) appears to be the research foundation underlying the GR00T-Dreams blueprint, demonstrating how to leverage video world models for synthetic trajectory generation."
    ],
    "durationSeconds": 7.987454361000011
  },
  "sourceToolAssistantUUID": "4c55d030-d7b5-4ce0-8da5-37f9495f1cfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-10T17:12:40.869Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0166iTtSEnfENSNpqzVzxD8v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.12705",
  "prompt": "Extract the key technical contribution, method details, limitations, and results of the DreamGen paper. What exactly does it do differently from prior work? What are its failure modes? What gaps does it leave open for humanoid-specific data generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15aa4ca9-f788-446a-95d0-3560f42b717b",
  "isSidechain": false,
  "requestId": "req_011CauG9J7aa7nCbkqVTd3Ts",
  "type": "assistant",
  "uuid": "b642c7c2-ae6f-4358-9f01-f0199938f9f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145wWjriMK59NbvRjKLg3vj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1027,
      "cache_read_input_tokens": 43109,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 43109,
          "cache_creation_input_tokens": 1027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1027
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

_source line 73 · 2026-05-10T17:12:46.670Z_

<details><summary>↩ Tool result · `toolu_0166iTtSEnfENSNpqzVzxD8v`</summary>

```text
# DreamGen: Technical Summary

## Key Technical Contribution

DreamGen introduces a four-stage pipeline that leverages video generation models to create synthetic training data for robot policies. The core innovation is adapting existing image-to-video generative models to specific robot embodiments, generating photorealistic videos that can then be converted into actionable training data.

## Method Details

The approach operates through these stages:

1. **Video generation** using adapted state-of-the-art generative models
2. **Pseudo-action recovery** via either latent action models or inverse-dynamics models (IDM)
3. **Policy training** on synthetic trajectories
4. **Evaluation** using their newly introduced DreamGen Bench

The system requires only "teleoperation data from only a single pick-and-place task in one environment" to generalize across diverse scenarios.

## Key Results

- A humanoid robot performed "22 new behaviors in both seen and unseen environments"
- Strong correlation established between benchmark performance and downstream policy success
- Demonstrates "behavior and environment generalization" despite minimal source data

## Limitations & Open Gaps

The document provides minimal explicit failure-mode analysis. Notable gaps include:

- **Humanoid-specific generation**: The paper doesn't detail optimization strategies particular to humanoid morphology
- **Action recovery accuracy**: No detailed analysis of pseudo-action quality from inverse models
- **Generalization boundaries**: Unclear how performance degrades beyond the tested 22 behaviors
- **Sim-to-real transfer**: Limited discussion of bridging photorealistic simulation to physical robots
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b642c7c2-ae6f-4358-9f01-f0199938f9f5",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "0a6261fd-1fab-4e1d-8c56-af2ad177c10d",
  "toolUseResult": {
    "bytes": 50631,
    "code": 200,
    "codeText": "OK",
    "result": "# DreamGen: Technical Summary\n\n## Key Technical Contribution\n\nDreamGen introduces a four-stage pipeline that leverages video generation models to create synthetic training data for robot policies. The core innovation is adapting existing image-to-video generative models to specific robot embodiments, generating photorealistic videos that can then be converted into actionable training data.\n\n## Method Details\n\nThe approach operates through these stages:\n\n1. **Video generation** using adapted state-of-the-art generative models\n2. **Pseudo-action recovery** via either latent action models or inverse-dynamics models (IDM)\n3. **Policy training** on synthetic trajectories\n4. **Evaluation** using their newly introduced DreamGen Bench\n\nThe system requires only \"teleoperation data from only a single pick-and-place task in one environment\" to generalize across diverse scenarios.\n\n## Key Results\n\n- A humanoid robot performed \"22 new behaviors in both seen and unseen environments\"\n- Strong correlation established between benchmark performance and downstream policy success\n- Demonstrates \"behavior and environment generalization\" despite minimal source data\n\n## Limitations & Open Gaps\n\nThe document provides minimal explicit failure-mode analysis. Notable gaps include:\n\n- **Humanoid-specific generation**: The paper doesn't detail optimization strategies particular to humanoid morphology\n- **Action recovery accuracy**: No detailed analysis of pseudo-action quality from inverse models\n- **Generalization boundaries**: Unclear how performance degrades beyond the tested 22 behaviors\n- **Sim-to-real transfer**: Limited discussion of bridging photorealistic simulation to physical robots",
    "durationMs": 5796,
    "url": "https://arxiv.org/abs/2505.12705"
  },
  "sourceToolAssistantUUID": "b642c7c2-ae6f-4358-9f01-f0199938f9f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-10T17:12:49.373Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U7AGieZ28jN1pZfgqTnAoM`</summary>

```json
{
  "query": "CoRL 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a6261fd-1fab-4e1d-8c56-af2ad177c10d",
  "isSidechain": false,
  "requestId": "req_011CauGA7CXSYHPdEbg91C5v",
  "type": "assistant",
  "uuid": "ac2e5780-101b-4ff0-872c-08475856cc7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EGgxWzApKVZjEPrGbvHvG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 491,
      "cache_read_input_tokens": 44136,
      "output_tokens": 62,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 491,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 62,
          "cache_read_input_tokens": 44136,
          "cache_creation_input_tokens": 491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 491
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

_source line 75 · 2026-05-10T17:12:57.418Z_

<details><summary>↩ Tool result · `toolu_01U7AGieZ28jN1pZfgqTnAoM`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline call for papers"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"}]

Based on the search results, here's the information about CoRL 2026 submission deadlines and call for papers:

## CoRL 2026 Call for Papers

The Call for Papers and key dates are now available.

## Submission Deadlines

The key dates for submissions are: May 25 for Abstract Submission and May 28 for Full Paper Submission. (Note: Some sources show slightly different dates - May 26, 2026 for abstract submission and May 29, 2026 for paper submission, both at 11:59 UTC)

## Conference Details

CoRL 2026 will be held in Austin, Texas, US, and the conference runs November 9-12 in Austin, TX.

## Submission Information

Papers may be submitted through OpenReview via their CoRL 2026 Conference page. The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac2e5780-101b-4ff0-872c-08475856cc7c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "17a90483-d30a-40ab-8b16-4cd8389cb726",
  "toolUseResult": {
    "query": "CoRL 2026 submission deadline call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WjCdLb2AreYiuMisPiUChC",
        "content": [
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
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2026 - Annoucements",
            "url": "https://www.corl.org/annoucements"
          },
          {
            "title": "Refactor conference data · huggingface/ai-deadlines at f3cc2d7",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"
          }
        ]
      },
      "Based on the search results, here's the information about CoRL 2026 submission deadlines and call for papers:\n\n## CoRL 2026 Call for Papers\n\nThe Call for Papers and key dates are now available.\n\n## Submission Deadlines\n\nThe key dates for submissions are: May 25 for Abstract Submission and May 28 for Full Paper Submission. (Note: Some sources show slightly different dates - May 26, 2026 for abstract submission and May 29, 2026 for paper submission, both at 11:59 UTC)\n\n## Conference Details\n\nCoRL 2026 will be held in Austin, Texas, US, and the conference runs November 9-12 in Austin, TX.\n\n## Submission Information\n\nPapers may be submitted through OpenReview via their CoRL 2026 Conference page. The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics."
    ],
    "durationSeconds": 8.039971399999981
  },
  "sourceToolAssistantUUID": "ac2e5780-101b-4ff0-872c-08475856cc7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-10T17:13:06.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019hV983cPE7rkN3NTvxw7Jg`</summary>

```json
{
  "query": "structured noise diffusion model kinematic constraint robot embodiment morphology-aware generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a90483-d30a-40ab-8b16-4cd8389cb726",
  "isSidechain": false,
  "requestId": "req_011CauGAu4JtEsuSye5k6zrs",
  "type": "assistant",
  "uuid": "15eda990-ba3d-4eb9-a4f1-b5fe18bfc216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKqmYfbPPxmKSfDvzbLn5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 44627,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 44627,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 77 · 2026-05-10T17:13:15.228Z_

<details><summary>↩ Tool result · `toolu_019hV983cPE7rkN3NTvxw7Jg`</summary>

```text
Web search results for query: "structured noise diffusion model kinematic constraint robot embodiment morphology-aware generation 2025 2026"

Links: [{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"},{"title":"Towards Embodiment Scaling Laws in Robot Locomotion Bo Ai1∗ Liu Dai1∗","url":"https://arxiv.org/pdf/2505.05753"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5692c7dbc4abcaa50f9ce609819212e5-Paper-Conference.pdf"},{"title":"Case Studies of Foundation Model Integration in Embodied ...","url":"https://aclanthology.org/2025.findings-emnlp.69.pdf"},{"title":"1 Physical AI: Bridging the Sim-to-Real Divide Toward Embodied,","url":"https://www.techrxiv.org/users/913189/articles/1355704/master/file/data/physical%20aiv7_compressed/physical%20aiv7_compressed.pdf?inline=true"},{"title":"Embodied neuromorphic intelligence | Nature Communications","url":"https://www.nature.com/articles/s41467-022-28487-2"}]

I've performed the web search for your query. Here are the relevant findings from recent research (2025-2026):

## Key Research Areas Found

**Diffusion Models in Robotics:**
Diffusion models have recently emerged as a promising approach in robotics, especially in robot manipulations, leveraging a probabilistic framework with ability to model multi-modal distributions and robustness to high-dimensional input and output spaces.

**Kinematic Constraints:**
Recent work includes "Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation" (CVPR 2025) and "Learning Diverse Robot Striking Motions with Diffusion Models and Kinematically Constrained Gradient Guidance."

**Embodiment and Morphology-Aware Generation:**
GENBOT-1K procedurally generates ~1,000 blueprint robot descriptions spanning humanoids, quadrupeds, and hexapods by varying topology, geometry, and joint-level kinematic constraints. This enables policies trained on the full training dataset to transfer zero-shot to novel simulated robots and real-world hardware with different morphologies.

Cross-embodiment imitation learning frameworks like Human2LocoMan enable quadrupedal robots to learn manipulation skills from human demonstrations using a Modularized Cross-embodiment Transformer (MXT) architecture with separate tokenizers for different data modalities while sharing a common transformer trunk.

**Structured Noise and Action Generation:**
Recent research focuses on predicting future states and synthesizing executable actions by leveraging inverse kinematics principles, where multimodal states often correspond to multiple valid actions that diffusion models can effectively model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15eda990-ba3d-4eb9-a4f1-b5fe18bfc216",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "1569208d-9437-4d58-94d3-f9610370a0e9",
  "toolUseResult": {
    "query": "structured noise diffusion model kinematic constraint robot embodiment morphology-aware generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MhZh5aZTCQNs3txnvJrvAE",
        "content": [
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Frontiers | Diffusion models for robotic manipulation: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"
          },
          {
            "title": "TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"
          },
          {
            "title": "Towards Embodiment Scaling Laws in Robot Locomotion Bo Ai1∗ Liu Dai1∗",
            "url": "https://arxiv.org/pdf/2505.05753"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/5692c7dbc4abcaa50f9ce609819212e5-Paper-Conference.pdf"
          },
          {
            "title": "Case Studies of Foundation Model Integration in Embodied ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.69.pdf"
          },
          {
            "title": "1 Physical AI: Bridging the Sim-to-Real Divide Toward Embodied,",
            "url": "https://www.techrxiv.org/users/913189/articles/1355704/master/file/data/physical%20aiv7_compressed/physical%20aiv7_compressed.pdf?inline=true"
          },
          {
            "title": "Embodied neuromorphic intelligence | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-022-28487-2"
          }
        ]
      },
      "I've performed the web search for your query. Here are the relevant findings from recent research (2025-2026):\n\n## Key Research Areas Found\n\n**Diffusion Models in Robotics:**\nDiffusion models have recently emerged as a promising approach in robotics, especially in robot manipulations, leveraging a probabilistic framework with ability to model multi-modal distributions and robustness to high-dimensional input and output spaces.\n\n**Kinematic Constraints:**\nRecent work includes \"Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation\" (CVPR 2025) and \"Learning Diverse Robot Striking Motions with Diffusion Models and Kinematically Constrained Gradient Guidance.\"\n\n**Embodiment and Morphology-Aware Generation:**\nGENBOT-1K procedurally generates ~1,000 blueprint robot descriptions spanning humanoids, quadrupeds, and hexapods by varying topology, geometry, and joint-level kinematic constraints. This enables policies trained on the full training dataset to transfer zero-shot to novel simulated robots and real-world hardware with different morphologies.\n\nCross-embodiment imitation learning frameworks like Human2LocoMan enable quadrupedal robots to learn manipulation skills from human demonstrations using a Modularized Cross-embodiment Transformer (MXT) architecture with separate tokenizers for different data modalities while sharing a common transformer trunk.\n\n**Structured Noise and Action Generation:**\nRecent research focuses on predicting future states and synthesizing executable actions by leveraging inverse kinematics principles, where multimodal states often correspond to multiple valid actions that diffusion models can effectively model."
    ],
    "durationSeconds": 8.238669656999992
  },
  "sourceToolAssistantUUID": "15eda990-ba3d-4eb9-a4f1-b5fe18bfc216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-10T17:13:17.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WeKWoYcuyZ47PRyo3wHK1g`</summary>

```json
{
  "query": "humanoid motion generation diffusion model contact-rich loco-manipulation diverse dataset synthesis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1569208d-9437-4d58-94d3-f9610370a0e9",
  "isSidechain": false,
  "requestId": "req_011CauGCDCzNLhnpyEAoHkTP",
  "type": "assistant",
  "uuid": "394a30ee-0872-491c-bff0-98f4e41f2b83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3FWoSvXoKvMbD4uy5C7N2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 45411,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 45411,
          "cache_creation_input_tokens": 1135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1135
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

_source line 79 · 2026-05-10T17:13:25.535Z_

<details><summary>↩ Tool result · `toolu_01WeKWoYcuyZ47PRyo3wHK1g`</summary>

```text
Web search results for query: "humanoid motion generation diffusion model contact-rich loco-manipulation diverse dataset synthesis 2025 2026"

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors","url":"https://arxiv.org/html/2604.00202"},{"title":"Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | Request PDF","url":"https://www.researchgate.net/publication/396873618_Physically_Consistent_Humanoid_Loco-Manipulation_Using_Latent_Diffusion_Models"},{"title":"(PDF) Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models","url":"https://www.researchgate.net/publication/391057797_Physically_Consistent_Humanoid_Loco-Manipulation_using_Latent_Diffusion_Models"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid","url":"https://omniretarget.github.io/static/images/paper.pdf"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models","url":"https://arxiv.org/html/2504.16843v1"},{"title":"[PDF] Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/295b2d39d130a2c125745dc85c0a063ee01cb9f5"},{"title":"Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=abBrq95y1p"},{"title":"Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11202977/11203009/11203092.pdf"}]

Based on the search results, I found several recent papers (2025-2026) related to humanoid motion generation using diffusion models for contact-rich loco-manipulation tasks with diverse dataset synthesis:

## Key Papers and Projects

### DreamControl-v2 (March 2026)
DreamControl-v2 trains a guided diffusion model directly in the humanoid robot's motion space, aggregating diverse human and robot datasets into a unified embodiment space. The data pool is composed of large-scale human motion datasets AMASS/HumanML3D, GRAB, and Nymeria, along with robot trajectories from OmniRetarget, which collectively enable the model to learn diverse, whole-body interaction behaviors.

### Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models (April 2025)
This paper uses latent diffusion models to generate realistic RGB human-object interaction scenes to guide humanoid loco-manipulation planning, extracting contact locations and robot configurations that are then used inside a whole-body trajectory optimization formulation to generate physically consistent trajectories for humanoids.

### OmniRetarget
OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.

### Recent Related Work (2025-2026)
The search results also reveal several recent papers addressing contact-rich loco-manipulation, including:
- Heracles, SafeFlow, LATENT, Ψ₀ (Psi-Zero), and ULTRA, all addressing humanoid whole-body loco-manipulation
- HMC (Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation)

These works collectively demonstrate significant advances in using diffusion models and generative approaches combined with diverse dataset synthesis for humanoid robot motion generation and control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "394a30ee-0872-491c-bff0-98f4e41f2b83",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "1c574ee3-8635-442f-a068-74e6f7154c42",
  "toolUseResult": {
    "query": "humanoid motion generation diffusion model contact-rich loco-manipulation diverse dataset synthesis 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HjmDe6n6ZUoftApsDZMCFa",
        "content": [
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors",
            "url": "https://arxiv.org/html/2604.00202"
          },
          {
            "title": "Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | Request PDF",
            "url": "https://www.researchgate.net/publication/396873618_Physically_Consistent_Humanoid_Loco-Manipulation_Using_Latent_Diffusion_Models"
          },
          {
            "title": "(PDF) Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models",
            "url": "https://www.researchgate.net/publication/391057797_Physically_Consistent_Humanoid_Loco-Manipulation_using_Latent_Diffusion_Models"
          },
          {
            "title": "OmniRetarget: Interaction-Preserving Data Generation for Humanoid",
            "url": "https://omniretarget.github.io/static/images/paper.pdf"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models",
            "url": "https://arxiv.org/html/2504.16843v1"
          },
          {
            "title": "[PDF] Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/295b2d39d130a2c125745dc85c0a063ee01cb9f5"
          },
          {
            "title": "Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models | OpenReview",
            "url": "https://openreview.net/forum?id=abBrq95y1p"
          },
          {
            "title": "Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/11202977/11203009/11203092.pdf"
          }
        ]
      },
      "Based on the search results, I found several recent papers (2025-2026) related to humanoid motion generation using diffusion models for contact-rich loco-manipulation tasks with diverse dataset synthesis:\n\n## Key Papers and Projects\n\n### DreamControl-v2 (March 2026)\nDreamControl-v2 trains a guided diffusion model directly in the humanoid robot's motion space, aggregating diverse human and robot datasets into a unified embodiment space. The data pool is composed of large-scale human motion datasets AMASS/HumanML3D, GRAB, and Nymeria, along with robot trajectories from OmniRetarget, which collectively enable the model to learn diverse, whole-body interaction behaviors.\n\n### Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models (April 2025)\nThis paper uses latent diffusion models to generate realistic RGB human-object interaction scenes to guide humanoid loco-manipulation planning, extracting contact locations and robot configurations that are then used inside a whole-body trajectory optimization formulation to generate physically consistent trajectories for humanoids.\n\n### OmniRetarget\nOmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.\n\n### Recent Related Work (2025-2026)\nThe search results also reveal several recent papers addressing contact-rich loco-manipulation, including:\n- Heracles, SafeFlow, LATENT, Ψ₀ (Psi-Zero), and ULTRA, all addressing humanoid whole-body loco-manipulation\n- HMC (Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation)\n\nThese works collectively demonstrate significant advances in using diffusion models and generative approaches combined with diverse dataset synthesis for humanoid robot motion generation and control."
    ],
    "durationSeconds": 7.7156571530000075
  },
  "sourceToolAssistantUUID": "394a30ee-0872-491c-bff0-98f4e41f2b83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 80 · 2026-05-10T17:13:25.538Z_

```json
{
  "parentUuid": "1c574ee3-8635-442f-a068-74e6f7154c42",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "58ff5815-06af-4dd9-9a41-58e41d9ad90e",
  "timestamp": "2026-05-10T17:13:25.538Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "58ff5815-06af-4dd9-9a41-58e41d9ad90e",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Assistant

_source line 83 · 2026-05-10T17:13:29.279Z_

This is a critical find — DreamControl-v2 and OmniRetarget are very recent concurrent work. Let me dig deeper into these and search for remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58ff5815-06af-4dd9-9a41-58e41d9ad90e",
  "isSidechain": false,
  "requestId": "req_011CauGCyF8iH4j9UerfdrwF",
  "type": "assistant",
  "uuid": "6b3a6a1c-d505-49b8-9564-4b2ae1dff192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUVYngk7aTDE9zdntHM9pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 46546,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 46546,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1289
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

_source line 84 · 2026-05-10T17:13:31.430Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016Ns5PvnhEQhNPGUmWQpZbb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.00202",
  "prompt": "Extract the complete method details of DreamControl-v2. What is their key technical contribution? How do they aggregate data from different sources? What are the limitations? What humanoid embodiments do they target? How do they handle loco-manipulation vs pure manipulation? What compute resources do they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b3a6a1c-d505-49b8-9564-4b2ae1dff192",
  "isSidechain": false,
  "requestId": "req_011CauGCyF8iH4j9UerfdrwF",
  "type": "assistant",
  "uuid": "8862cd65-2e66-4cad-9aa0-86a7fe4011a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUVYngk7aTDE9zdntHM9pw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 46546,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 46546,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1289
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

_source line 85 · 2026-05-10T17:13:36.342Z_

<details><summary>↩ Tool result · `toolu_016Ns5PvnhEQhNPGUmWQpZbb`</summary>

```text
# DreamControl-v2: Summary Based on Available Content

Based on the arXiv abstract provided, here's what can be determined:

## Key Technical Contribution

The primary innovation is training "a guided diffusion model directly in the humanoid robot's motion space" rather than relying on off-the-shelf human motion models. This represents an improvement over the original DreamControl approach.

## Data Aggregation Strategy

The method "aggregat[es] diverse human and robot datasets into a unified embodiment space," enabling the capture of a broader range of skills through larger training data mixtures.

## Pipeline Improvements

A notable advancement is establishing "a more automated pipeline by removing the need for manual filtering interventions," streamlining the workflow compared to prior work.

## Humanoid Embodiment

The research validates results "on a real Unitree-G1," indicating this specific robot serves as their primary hardware testbed.

## Loco-Manipulation Focus

The work addresses "robust autonomous loco-manipulation skills" for humanoids, acknowledging that "applying [RL] to complex, interaction-rich manipulation tasks is harder given long-horizon planning challenges."

## Limitations & Unknowns

The abstract does not specify compute resources, detailed architectural parameters, or explicit limitations. These details would require accessing the full paper PDF or HTML version linked on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8862cd65-2e66-4cad-9aa0-86a7fe4011a7",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "1bbdf60a-0b4f-4f70-9e9f-2a4c7bdc6608",
  "toolUseResult": {
    "bytes": 46973,
    "code": 200,
    "codeText": "OK",
    "result": "# DreamControl-v2: Summary Based on Available Content\n\nBased on the arXiv abstract provided, here's what can be determined:\n\n## Key Technical Contribution\n\nThe primary innovation is training \"a guided diffusion model directly in the humanoid robot's motion space\" rather than relying on off-the-shelf human motion models. This represents an improvement over the original DreamControl approach.\n\n## Data Aggregation Strategy\n\nThe method \"aggregat[es] diverse human and robot datasets into a unified embodiment space,\" enabling the capture of a broader range of skills through larger training data mixtures.\n\n## Pipeline Improvements\n\nA notable advancement is establishing \"a more automated pipeline by removing the need for manual filtering interventions,\" streamlining the workflow compared to prior work.\n\n## Humanoid Embodiment\n\nThe research validates results \"on a real Unitree-G1,\" indicating this specific robot serves as their primary hardware testbed.\n\n## Loco-Manipulation Focus\n\nThe work addresses \"robust autonomous loco-manipulation skills\" for humanoids, acknowledging that \"applying [RL] to complex, interaction-rich manipulation tasks is harder given long-horizon planning challenges.\"\n\n## Limitations & Unknowns\n\nThe abstract does not specify compute resources, detailed architectural parameters, or explicit limitations. These details would require accessing the full paper PDF or HTML version linked on the arXiv page.",
    "durationMs": 4909,
    "url": "https://arxiv.org/abs/2604.00202"
  },
  "sourceToolAssistantUUID": "8862cd65-2e66-4cad-9aa0-86a7fe4011a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-10T17:13:41.702Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Di8ZnwuEBKF6wrNGevJzuU`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.00202",
  "prompt": "Extract the full method details of DreamControl-v2: (1) How exactly do they unify different datasets into a unified embodiment space? (2) What is the guided diffusion architecture? (3) How do they handle locomotion + manipulation jointly? (4) What are the training compute requirements? (5) What tasks and benchmarks do they evaluate on? (6) What are the explicit limitations and failure modes? (7) How does this compare to GR00T-Dreams/DreamGen?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bbdf60a-0b4f-4f70-9e9f-2a4c7bdc6608",
  "isSidechain": false,
  "requestId": "req_011CauGDmXxYMNTppqjrK98H",
  "type": "assistant",
  "uuid": "0ab102bf-e55b-4f37-a9f6-a2facbfb86a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSuksFcFc4M3sy1P1LD9QB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 491,
      "cache_read_input_tokens": 47835,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 491,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 47835,
          "cache_creation_input_tokens": 491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 491
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

_source line 87 · 2026-05-10T17:13:58.383Z_

<details><summary>↩ Tool result · `toolu_01Di8ZnwuEBKF6wrNGevJzuU`</summary>

```text
# DreamControl-v2: Comprehensive Method Analysis

## 1. Unifying Different Datasets into Unified Embodiment Space

DreamControl-v2 consolidates heterogeneous human motion data through **pre-retargeting to the Unitree-G1 robot**. The approach:

- Selects 12 shared keypoints between human and robot (hips, knees, ankles, shoulders, elbows, wrists)
- Solves an optimization problem minimizing "differences in relative joint angles, relative keypoint positions, foot slip, and a scale factor"
- Handles non-SMPL parameterizations (like Xsens) by recovering SMPL parameters through differentiable forward kinematics
- Applies feasibility filters to remove infeasible motions
- Uses keyword-based retrieval for task-specific segments from Nymeria dataset

**Data sources unified:** AMASS/HumanML3D, GRAB, Nymeria, and OmniRetarget robot trajectories, totaling approximately 29.6K samples in the Full-Mix configuration.

## 2. Guided Diffusion Architecture

The model builds on OmniControl with these components:

- **Core architecture:** Denoising diffusion model predicting clean signals rather than noise
- **Conditioning mechanism:** "Realism-guidance module from OmniControl, which is similar to ControlNet" with trainable encoder initialized at zero
- **Multi-modal conditioning:** Accepts open-vocabulary text and spatio-temporal control signals (3D positions per joint across timestamps)
- **Spatial guidance:** Uses MSE loss during sampling to enforce "trajectory μt toward desired constraints" through gradient updates
- **Trajectory parameterization:** 263-dimensional representation encoding root velocities, joint positions/velocities, 6D rotations, and foot contact features

## 3. Handling Locomotion + Manipulation Jointly

The framework achieves whole-body coordination through:

- **Unified action representation:** All 8 tasks use the same 27-DOF action space plus binary hand commands
- **Trajectory-conditioned RL:** Policies track reference trajectories while accomplishing tasks autonomously
- **Spatio-temporal constraints:** Enables fine-grained control over "timing of contact with various objects in the environment"
- **Task-specific filtering:** Post-processing ensures physical plausibility through obstacle avoidance, foot stability, and wrist-orientation constraints

Example: Drawer opening specifies both "open the drawer" text and constrains right wrist to reach the handle at specific xyz coordinates at time tg.

## 4. Training Compute Requirements

The paper provides limited explicit details but indicates:

- **Dataset preparation:** Retargeting performed "across 5 NVIDIA H100 GPUs in parallel"
- **Diffusion model training:** "Single NVIDIA H100 GPU using AdamW optimizer with learning rate of 1×10⁻⁵"
- **RL training:** "Single NVIDIA A6000 GPU for 2,000–5,000 iterations depending on task, on approximately 8,912 parallel simulation environments"
- No explicit wall-clock training times reported

## 5. Tasks and Evaluation Benchmarks

**Skill library (8 tasks):**
Pick, Punch, Deep Squat & Pick, Drawer Open, Pour, Vertical Wipe, Deep Squat, Step & Punch

**Evaluation metrics for diffusion models:**
- FID (Fréchet Inception Distance) measuring distributional similarity
- R-Precision evaluating text-motion alignment
- Diversity measuring trajectory variance
- Control L2 measuring spatial accuracy
- Skating Ratio as physical plausibility proxy

**RL evaluation:** Success ratio and control error across 100 randomized environments per task. Results show high performance: "across all skills, DreamControl-v2 achieves consistently high success rates" (0.91–1.00 success ratio).

## 6. Explicit Limitations and Failure Modes

The paper doesn't extensively discuss limitations but acknowledges:

- **Scalability constraints in original DreamControl:** "Manual tuning process is labor-intensive and bottlenecks scalability, especially difficult for long-horizon and high-dimensional humanoid loco-manipulation tasks"
- **Filtering dependency:** Automated filtering uses "error-based heuristics" and task-specific thresholds, suggesting brittleness
- **Real-world constraints:** Waist configured to allow only yaw rotation; roll and pitch locked
- **Scope limitations:** Evaluation limited to 8 tasks, primarily tabletop/articulated object manipulation

## 7. Comparison to GR00T-Dreams/DreamGen

**The paper does not mention or compare against GR00T-Dreams or DreamGen.** The primary baseline is the original DreamControl framework using OmniControl. Related work discussions reference CLOS-D and Humanoid-X but not these alternative generative approaches.

---

## Summary Table

| Aspect | Implementation |
|--------|-----------------|
| **Dataset unification** | Pre-retargeting human→G1 via optimization |
| **Diffusion prior** | OmniControl architecture + spatio-temporal guidance |
| **Locomotion+manipulation** | Unified action space + trajectory tracking rewards |
| **Compute** | H100s for data prep, single GPU for training phases |
| **Evaluation** | 8 real tasks, 100 trials each, FID/R-Precision/control metrics |
| **Known gaps** | Limited failure mode analysis, task-specific filtering heuristics |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ab102bf-e55b-4f37-a9f6-a2facbfb86a4",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "6ce22613-389e-4f3c-ac64-669de538dd56",
  "toolUseResult": {
    "bytes": 250439,
    "code": 200,
    "codeText": "OK",
    "result": "# DreamControl-v2: Comprehensive Method Analysis\n\n## 1. Unifying Different Datasets into Unified Embodiment Space\n\nDreamControl-v2 consolidates heterogeneous human motion data through **pre-retargeting to the Unitree-G1 robot**. The approach:\n\n- Selects 12 shared keypoints between human and robot (hips, knees, ankles, shoulders, elbows, wrists)\n- Solves an optimization problem minimizing \"differences in relative joint angles, relative keypoint positions, foot slip, and a scale factor\"\n- Handles non-SMPL parameterizations (like Xsens) by recovering SMPL parameters through differentiable forward kinematics\n- Applies feasibility filters to remove infeasible motions\n- Uses keyword-based retrieval for task-specific segments from Nymeria dataset\n\n**Data sources unified:** AMASS/HumanML3D, GRAB, Nymeria, and OmniRetarget robot trajectories, totaling approximately 29.6K samples in the Full-Mix configuration.\n\n## 2. Guided Diffusion Architecture\n\nThe model builds on OmniControl with these components:\n\n- **Core architecture:** Denoising diffusion model predicting clean signals rather than noise\n- **Conditioning mechanism:** \"Realism-guidance module from OmniControl, which is similar to ControlNet\" with trainable encoder initialized at zero\n- **Multi-modal conditioning:** Accepts open-vocabulary text and spatio-temporal control signals (3D positions per joint across timestamps)\n- **Spatial guidance:** Uses MSE loss during sampling to enforce \"trajectory μt toward desired constraints\" through gradient updates\n- **Trajectory parameterization:** 263-dimensional representation encoding root velocities, joint positions/velocities, 6D rotations, and foot contact features\n\n## 3. Handling Locomotion + Manipulation Jointly\n\nThe framework achieves whole-body coordination through:\n\n- **Unified action representation:** All 8 tasks use the same 27-DOF action space plus binary hand commands\n- **Trajectory-conditioned RL:** Policies track reference trajectories while accomplishing tasks autonomously\n- **Spatio-temporal constraints:** Enables fine-grained control over \"timing of contact with various objects in the environment\"\n- **Task-specific filtering:** Post-processing ensures physical plausibility through obstacle avoidance, foot stability, and wrist-orientation constraints\n\nExample: Drawer opening specifies both \"open the drawer\" text and constrains right wrist to reach the handle at specific xyz coordinates at time tg.\n\n## 4. Training Compute Requirements\n\nThe paper provides limited explicit details but indicates:\n\n- **Dataset preparation:** Retargeting performed \"across 5 NVIDIA H100 GPUs in parallel\"\n- **Diffusion model training:** \"Single NVIDIA H100 GPU using AdamW optimizer with learning rate of 1×10⁻⁵\"\n- **RL training:** \"Single NVIDIA A6000 GPU for 2,000–5,000 iterations depending on task, on approximately 8,912 parallel simulation environments\"\n- No explicit wall-clock training times reported\n\n## 5. Tasks and Evaluation Benchmarks\n\n**Skill library (8 tasks):**\nPick, Punch, Deep Squat & Pick, Drawer Open, Pour, Vertical Wipe, Deep Squat, Step & Punch\n\n**Evaluation metrics for diffusion models:**\n- FID (Fréchet Inception Distance) measuring distributional similarity\n- R-Precision evaluating text-motion alignment\n- Diversity measuring trajectory variance\n- Control L2 measuring spatial accuracy\n- Skating Ratio as physical plausibility proxy\n\n**RL evaluation:** Success ratio and control error across 100 randomized environments per task. Results show high performance: \"across all skills, DreamControl-v2 achieves consistently high success rates\" (0.91–1.00 success ratio).\n\n## 6. Explicit Limitations and Failure Modes\n\nThe paper doesn't extensively discuss limitations but acknowledges:\n\n- **Scalability constraints in original DreamControl:** \"Manual tuning process is labor-intensive and bottlenecks scalability, especially difficult for long-horizon and high-dimensional humanoid loco-manipulation tasks\"\n- **Filtering dependency:** Automated filtering uses \"error-based heuristics\" and task-specific thresholds, suggesting brittleness\n- **Real-world constraints:** Waist configured to allow only yaw rotation; roll and pitch locked\n- **Scope limitations:** Evaluation limited to 8 tasks, primarily tabletop/articulated object manipulation\n\n## 7. Comparison to GR00T-Dreams/DreamGen\n\n**The paper does not mention or compare against GR00T-Dreams or DreamGen.** The primary baseline is the original DreamControl framework using OmniControl. Related work discussions reference CLOS-D and Humanoid-X but not these alternative generative approaches.\n\n---\n\n## Summary Table\n\n| Aspect | Implementation |\n|--------|-----------------|\n| **Dataset unification** | Pre-retargeting human→G1 via optimization |\n| **Diffusion prior** | OmniControl architecture + spatio-temporal guidance |\n| **Locomotion+manipulation** | Unified action space + trajectory tracking rewards |\n| **Compute** | H100s for data prep, single GPU for training phases |\n| **Evaluation** | 8 real tasks, 100 trials each, FID/R-Precision/control metrics |\n| **Known gaps** | Limited failure mode analysis, task-specific filtering heuristics |",
    "durationMs": 16677,
    "url": "https://arxiv.org/html/2604.00202"
  },
  "sourceToolAssistantUUID": "0ab102bf-e55b-4f37-a9f6-a2facbfb86a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-10T17:14:06.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JWdPTX1UFiWsnSuRkqarq6`</summary>

```json
{
  "query": "OmniRetarget interaction-preserving data generation humanoid 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce22613-389e-4f3c-ac64-669de538dd56",
  "isSidechain": false,
  "requestId": "req_011CauGFT8yNiG29sYq3wwkS",
  "type": "assistant",
  "uuid": "66e3f7d7-07c6-4388-9d30-64c373723ac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkuQiag69tVzcnNRkhpk8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1489,
      "cache_read_input_tokens": 48326,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 48326,
          "cache_creation_input_tokens": 1489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1489
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

_source line 89 · 2026-05-10T17:14:13.236Z_

<details><summary>↩ Tool result · `toolu_01JWdPTX1UFiWsnSuRkqarq6`</summary>

```text
Web search results for query: "OmniRetarget interaction-preserving data generation humanoid 2025 2026 arxiv"

Links: [{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"omniretarget/OmniRetarget_Dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset"},{"title":"[2509.26633v1] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633v1"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid","url":"https://arxiv.org/pdf/2509.26633"},{"title":"Systems and Control Sep 2025","url":"https://arxiv.org/list/eess.SY/2025-09?skip=675&show=250"},{"title":"[PDF] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OmniRetarget:-Interaction-Preserving-Data-for-and-Yang-Huang/234018fa87b6c649830e1e6274362c58445a9fbc"},{"title":"Paper page - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://huggingface.co/papers/2509.26633"},{"title":"(PDF) OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://www.researchgate.net/publication/396049126_OmniRetarget_Interaction-Preserving_Data_Generation_for_Humanoid_Whole-Body_Loco-Manipulation_and_Scene_Interaction"},{"title":"[Literature Review] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://www.themoonlight.io/en/review/omniretarget-interaction-preserving-data-generation-for-humanoid-whole-body-loco-manipulation-and-scene-interaction"}]

Based on the search results, I found the paper on arXiv. Here's what I discovered:

## OmniRetarget Research Paper

OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.

**Paper Details:**
- **arXiv ID:** 2509.26633
- **Published:** September 30, 2025 (v1), with version 2 updated October 8, 2025
- **Authors:** Lujie Yang, Xiaoyu Huang, Zhen Wu, Angjoo Kanazawa, Pieter Abbeel, Carmelo Sferrazza, C. Karen Liu, Rocky Duan, and Guanya Shi

**Key Problem:**
The dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train RL policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration, and neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation.

**Key Results:**
OmniRetarget was evaluated by retargeting motions from OMOMO, LAFAN1, and in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66e3f7d7-07c6-4388-9d30-64c373723ac1",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "63efbdef-933c-4289-b395-d83c4b708b92",
  "toolUseResult": {
    "query": "OmniRetarget interaction-preserving data generation humanoid 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A7SVYqz4fob3wV6J6ALMCS",
        "content": [
          {
            "title": "[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://arxiv.org/abs/2509.26633"
          },
          {
            "title": "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://arxiv.org/html/2509.26633v2"
          },
          {
            "title": "omniretarget/OmniRetarget_Dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset"
          },
          {
            "title": "[2509.26633v1] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://arxiv.org/abs/2509.26633v1"
          },
          {
            "title": "OmniRetarget: Interaction-Preserving Data Generation for Humanoid",
            "url": "https://arxiv.org/pdf/2509.26633"
          },
          {
            "title": "Systems and Control Sep 2025",
            "url": "https://arxiv.org/list/eess.SY/2025-09?skip=675&show=250"
          },
          {
            "title": "[PDF] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/OmniRetarget:-Interaction-Preserving-Data-for-and-Yang-Huang/234018fa87b6c649830e1e6274362c58445a9fbc"
          },
          {
            "title": "Paper page - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://huggingface.co/papers/2509.26633"
          },
          {
            "title": "(PDF) OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://www.researchgate.net/publication/396049126_OmniRetarget_Interaction-Preserving_Data_Generation_for_Humanoid_Whole-Body_Loco-Manipulation_and_Scene_Interaction"
          },
          {
            "title": "[Literature Review] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://www.themoonlight.io/en/review/omniretarget-interaction-preserving-data-generation-for-humanoid-whole-body-loco-manipulation-and-scene-interaction"
          }
        ]
      },
      "Based on the search results, I found the paper on arXiv. Here's what I discovered:\n\n## OmniRetarget Research Paper\n\nOmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.\n\n**Paper Details:**\n- **arXiv ID:** 2509.26633\n- **Published:** September 30, 2025 (v1), with version 2 updated October 8, 2025\n- **Authors:** Lujie Yang, Xiaoyu Huang, Zhen Wu, Angjoo Kanazawa, Pieter Abbeel, Carmelo Sferrazza, C. Karen Liu, Rocky Duan, and Guanya Shi\n\n**Key Problem:**\nThe dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train RL policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration, and neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation.\n\n**Key Results:**\nOmniRetarget was evaluated by retargeting motions from OMOMO, LAFAN1, and in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid."
    ],
    "durationSeconds": 6.587605961000023
  },
  "sourceToolAssistantUUID": "66e3f7d7-07c6-4388-9d30-64c373723ac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-10T17:14:17.654Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ThzEWvKXEqkaAbsmKSVvrx`</summary>

```json
{
  "query": "world model video generation data augmentation robot policy training sim-to-real 2026 arxiv benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63efbdef-933c-4289-b395-d83c4b708b92",
  "isSidechain": false,
  "requestId": "req_011CauGGVF1TixeaVHZM8bC9",
  "type": "assistant",
  "uuid": "76abed72-0169-4ddb-90e6-7a8a9a4b35ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HPMraNTq1FKmwYZdj7c4p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 49815,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 49815,
          "cache_creation_input_tokens": 1211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1211
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

_source line 91 · 2026-05-10T17:14:26.013Z_

<details><summary>↩ Tool result · `toolu_01ThzEWvKXEqkaAbsmKSVvrx`</summary>

```text
Web search results for query: "world model video generation data augmentation robot policy training sim-to-real 2026 arxiv benchmark"

Links: [{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"[2603.08546] Interactive World Simulator for Robot Policy Training and Evaluation","url":"https://arxiv.org/abs/2603.08546"},{"title":"Building Scalable Real-World Robot Data Generation via Compositional Simulation","url":"https://arxiv.org/html/2604.11386v1"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Interactive World Simulator for Robot Policy Training and Evaluation","url":"https://arxiv.org/html/2603.08546"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/html/2604.19683"},{"title":"Video Generators are Robot Policies","url":"https://arxiv.org/html/2508.00795v1"},{"title":"From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation","url":"https://arxiv.org/html/2604.15805v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"}]

I've found several highly relevant recent papers from arXiv (2026) on world models, video generation, data augmentation, and robot policy training with sim-to-real considerations. Here are the key findings:

## Recent Key Papers (2026)

**Interactive World Simulator for Robot Policy Training and Evaluation** (March 2026)
Action-conditioned video prediction models (world models) have been developed to address limitations in scalability and physical consistency, with a framework that leverages consistency models for both image decoding and latent-space dynamics prediction. Policies trained on world-model-generated data perform comparably to those trained on the same amount of real-world data, with strong correlation between simulated and real-world performance.

**Building Scalable Real-World Robot Data Generation via Compositional Simulation** (April 2026)
A closed-loop real-sim-real data augmentation pipeline utilizes a small amount of real-world data to create training datasets covering a broader distribution of real-world scenarios. The approach proposes a real-sim-real data augmentation pipeline with a neural simulator using Compositional Dynamic Video Generation to ensure accurate action-video alignment while mitigating sim2real domain gap.

**World Model for Robot Learning: A Comprehensive Survey** (May 2026)
PlayWorld learns robot world models from autonomous play with RL in the learned simulator improving downstream real-world performance, while RehearseVLA adapts this to VLA post-training with physically consistent world simulators.

**Video Generation Models in Robotics** (January 2026)
Augmenting observations with corresponding robot joint poses has been shown to improve frame-level action controllability.

These papers represent recent advances in using world models and video generation for data-efficient robot policy training with improved sim-to-real transfer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76abed72-0169-4ddb-90e6-7a8a9a4b35ce",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "747e8c9b-5ebd-41b2-aef5-ac4482c49aaf",
  "toolUseResult": {
    "query": "world model video generation data augmentation robot policy training sim-to-real 2026 arxiv benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EUneha8tLnmxKDJRcCm6jJ",
        "content": [
          {
            "title": "Video Generation Models in Robotics: Applications, Research Challenges, Future Directions",
            "url": "https://arxiv.org/html/2601.07823v1"
          },
          {
            "title": "[2603.08546] Interactive World Simulator for Robot Policy Training and Evaluation",
            "url": "https://arxiv.org/abs/2603.08546"
          },
          {
            "title": "Building Scalable Real-World Robot Data Generation via Compositional Simulation",
            "url": "https://arxiv.org/html/2604.11386v1"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2605.00080v1"
          },
          {
            "title": "Interactive World Simulator for Robot Policy Training and Evaluation",
            "url": "https://arxiv.org/html/2603.08546"
          },
          {
            "title": "Rethinking Video Generation Model for the Embodied World",
            "url": "https://arxiv.org/html/2601.15282v1"
          },
          {
            "title": "Mask World Model: Predicting What Matters for Robust Robot Policy Learning",
            "url": "https://arxiv.org/html/2604.19683"
          },
          {
            "title": "Video Generators are Robot Policies",
            "url": "https://arxiv.org/html/2508.00795v1"
          },
          {
            "title": "From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation",
            "url": "https://arxiv.org/html/2604.15805v1"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          }
        ]
      },
      "I've found several highly relevant recent papers from arXiv (2026) on world models, video generation, data augmentation, and robot policy training with sim-to-real considerations. Here are the key findings:\n\n## Recent Key Papers (2026)\n\n**Interactive World Simulator for Robot Policy Training and Evaluation** (March 2026)\nAction-conditioned video prediction models (world models) have been developed to address limitations in scalability and physical consistency, with a framework that leverages consistency models for both image decoding and latent-space dynamics prediction. Policies trained on world-model-generated data perform comparably to those trained on the same amount of real-world data, with strong correlation between simulated and real-world performance.\n\n**Building Scalable Real-World Robot Data Generation via Compositional Simulation** (April 2026)\nA closed-loop real-sim-real data augmentation pipeline utilizes a small amount of real-world data to create training datasets covering a broader distribution of real-world scenarios. The approach proposes a real-sim-real data augmentation pipeline with a neural simulator using Compositional Dynamic Video Generation to ensure accurate action-video alignment while mitigating sim2real domain gap.\n\n**World Model for Robot Learning: A Comprehensive Survey** (May 2026)\nPlayWorld learns robot world models from autonomous play with RL in the learned simulator improving downstream real-world performance, while RehearseVLA adapts this to VLA post-training with physically consistent world simulators.\n\n**Video Generation Models in Robotics** (January 2026)\nAugmenting observations with corresponding robot joint poses has been shown to improve frame-level action controllability.\n\nThese papers represent recent advances in using world models and video generation for data-efficient robot policy training with improved sim-to-real transfer."
    ],
    "durationSeconds": 8.355689277000026
  },
  "sourceToolAssistantUUID": "76abed72-0169-4ddb-90e6-7a8a9a4b35ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 92_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "747e8c9b-5ebd-41b2-aef5-ac4482c49aaf",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 94 · 2026-05-10T17:14:28.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014fsaba3cw1K4VKSFg92jzi`</summary>

```json
{
  "query": "\"compositional simulation\" OR \"compositional data generation\" robot manipulation diverse task scene 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "747e8c9b-5ebd-41b2-aef5-ac4482c49aaf",
  "isSidechain": false,
  "requestId": "req_011CauGHRrtKqU66tsUqik4Q",
  "type": "assistant",
  "uuid": "f43d49a5-8389-441d-89d5-541b5251f8a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tzzst3oc4oRz7WJVwuPLr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 928,
      "cache_read_input_tokens": 51026,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 928,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 51026,
          "cache_creation_input_tokens": 928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 928
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

_source line 95 · 2026-05-10T17:14:36.461Z_

<details><summary>↩ Tool result · `toolu_014fsaba3cw1K4VKSFg92jzi`</summary>

```text
Web search results for query: ""compositional simulation" OR "compositional data generation" robot manipulation diverse task scene 2026 arxiv"

Links: [{"title":"Efficient Data Collection for Robotic Manipulation via Compositional Generalization","url":"https://arxiv.org/html/2403.05110v1"},{"title":"What Matters in Learning from Large-Scale Datasets for Robot Manipulation","url":"https://arxiv.org/html/2506.13536v1"},{"title":"Iterative Compositional Data Generation for Robot Control","url":"https://arxiv.org/html/2512.10891"},{"title":"[2403.05110] Efficient Data Collection for Robotic Manipulation via Compositional Generalization","url":"https://arxiv.org/abs/2403.05110"},{"title":"Boosting Robotic Manipulation Generalization with Minimal Costly Data","url":"https://arxiv.org/html/2503.19516v2"},{"title":"SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation","url":"https://arxiv.org/html/2603.25725v1"},{"title":"1 Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/pdf/2503.03464"},{"title":"Image Generation as a Visual Planner for Robotic Manipulation","url":"https://arxiv.org/html/2512.00532"},{"title":"ClutterGen: A Cluttered Scene Generator for Robot Learning","url":"https://arxiv.org/html/2407.05425v2"},{"title":"RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation","url":"https://arxiv.org/html/2311.01455v3"}]

I found several relevant papers on compositional data generation and simulation for robot manipulation. Here are the key results:

## Most Recent: Iterative Compositional Data Generation (December 2025)

The most recent work introduces an iterative compositional data generation framework using a semantic compositional diffusion transformer and a self-improvement loop to synthesize and curate manipulation data that is of sufficient quality to train policies solving novel combinations of compositional tasks. The approach factorizes transitions into robot-, object-, obstacle-, and objective-specific components, and once trained on a limited subset of tasks, can zero-shot generate high-quality transitions from which control policies can be learned for unseen task combinations.

## Other Key Works (2025-2026)

1. **What Matters in Learning from Large-Scale Datasets** (June 2025): Uses simulation and synthetic data generation as a testbed by developing a synthetic data generator that can procedurally emulate common sources of diversity found in existing datasets, allowing creation of large-scale robot datasets with precisely controlled composition.

2. **SoftMimicGen** (March 2026): An automated data generation pipeline that synthesizes large-scale datasets for deformable object manipulation from a small number of human demonstrations.

3. **Image Generation as a Visual Planner** (November 2025): Explores generating realistic robotic manipulation videos, with image generation models trained on language-image corpora exhibiting strong compositionality for synthesizing temporally coherent grid images.

The search also returned earlier foundational work on compositional generalization in robot manipulation (2024) and systems like RoboGen and ClutterGen for automated scene and task generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f43d49a5-8389-441d-89d5-541b5251f8a6",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "c40f30d8-7725-431e-88db-7ba5df54f4a4",
  "toolUseResult": {
    "query": "\"compositional simulation\" OR \"compositional data generation\" robot manipulation diverse task scene 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RUpCzQ5gP1Db2GPmomuwLT",
        "content": [
          {
            "title": "Efficient Data Collection for Robotic Manipulation via Compositional Generalization",
            "url": "https://arxiv.org/html/2403.05110v1"
          },
          {
            "title": "What Matters in Learning from Large-Scale Datasets for Robot Manipulation",
            "url": "https://arxiv.org/html/2506.13536v1"
          },
          {
            "title": "Iterative Compositional Data Generation for Robot Control",
            "url": "https://arxiv.org/html/2512.10891"
          },
          {
            "title": "[2403.05110] Efficient Data Collection for Robotic Manipulation via Compositional Generalization",
            "url": "https://arxiv.org/abs/2403.05110"
          },
          {
            "title": "Boosting Robotic Manipulation Generalization with Minimal Costly Data",
            "url": "https://arxiv.org/html/2503.19516v2"
          },
          {
            "title": "SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation",
            "url": "https://arxiv.org/html/2603.25725v1"
          },
          {
            "title": "1 Generative Artificial Intelligence in Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/pdf/2503.03464"
          },
          {
            "title": "Image Generation as a Visual Planner for Robotic Manipulation",
            "url": "https://arxiv.org/html/2512.00532"
          },
          {
            "title": "ClutterGen: A Cluttered Scene Generator for Robot Learning",
            "url": "https://arxiv.org/html/2407.05425v2"
          },
          {
            "title": "RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation",
            "url": "https://arxiv.org/html/2311.01455v3"
          }
        ]
      },
      "I found several relevant papers on compositional data generation and simulation for robot manipulation. Here are the key results:\n\n## Most Recent: Iterative Compositional Data Generation (December 2025)\n\nThe most recent work introduces an iterative compositional data generation framework using a semantic compositional diffusion transformer and a self-improvement loop to synthesize and curate manipulation data that is of sufficient quality to train policies solving novel combinations of compositional tasks. The approach factorizes transitions into robot-, object-, obstacle-, and objective-specific components, and once trained on a limited subset of tasks, can zero-shot generate high-quality transitions from which control policies can be learned for unseen task combinations.\n\n## Other Key Works (2025-2026)\n\n1. **What Matters in Learning from Large-Scale Datasets** (June 2025): Uses simulation and synthetic data generation as a testbed by developing a synthetic data generator that can procedurally emulate common sources of diversity found in existing datasets, allowing creation of large-scale robot datasets with precisely controlled composition.\n\n2. **SoftMimicGen** (March 2026): An automated data generation pipeline that synthesizes large-scale datasets for deformable object manipulation from a small number of human demonstrations.\n\n3. **Image Generation as a Visual Planner** (November 2025): Explores generating realistic robotic manipulation videos, with image generation models trained on language-image corpora exhibiting strong compositionality for synthesizing temporally coherent grid images.\n\nThe search also returned earlier foundational work on compositional generalization in robot manipulation (2024) and systems like RoboGen and ClutterGen for automated scene and task generation."
    ],
    "durationSeconds": 7.818743703000015
  },
  "sourceToolAssistantUUID": "f43d49a5-8389-441d-89d5-541b5251f8a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-10T17:14:40.370Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XfwHoRL5ADGoHQXP19jdxU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.10891",
  "prompt": "Extract the key method of the \"Iterative Compositional Data Generation for Robot Control\" paper. What is the compositional diffusion transformer? How does the self-improvement loop work? What tasks do they evaluate on? What are the limitations? Could this approach be applied to humanoid loco-manipulation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c40f30d8-7725-431e-88db-7ba5df54f4a4",
  "isSidechain": false,
  "requestId": "req_011CauGJCZxQ29L3JAEUDuGS",
  "type": "assistant",
  "uuid": "de9b1f19-9510-4909-88c3-9708dde3bbe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGEmLefLbs7smWHkBDMskG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 51954,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 51954,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 904
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

_source line 97 · 2026-05-10T17:14:45.122Z_

<details><summary>↩ Tool result · `toolu_01XfwHoRL5ADGoHQXP19jdxU`</summary>

```text
# Analysis of "Iterative Compositional Data Generation for Robot Control"

## Key Method

The paper proposes a **semantic compositional diffusion transformer** that addresses the challenge of expensive robotic data collection by learning to generate synthetic training data for unseen task combinations.

## The Compositional Diffusion Transformer

The model "factorizes transitions into robot-, object-, obstacle-, and objective-specific components and learns their interactions through attention." This architectural choice enables the system to decompose complex robotic tasks into reusable semantic elements rather than treating each task monolithically.

## Self-Improvement Loop

The approach employs an iterative refinement mechanism: "synthetic data is validated via offline reinforcement learning and incorporated into subsequent training rounds." This creates a feedback cycle where generated data is tested for quality before being used to retrain the model, progressively improving performance.

## Evaluated Tasks

The abstract mentions evaluation on "multi-object, multi-robot, and multi-environment settings" with focus on "held-out tasks" and "unseen task combinations," though specific task names aren't detailed in the provided content.

## Limitations

The provided webpage content doesn't explicitly discuss limitations. The abstract notes the model "struggle[s] to generalize to unseen task combinations" in prior approaches, which their method addresses, but doesn't acknowledge their own limitations.

## Humanoid Loco-Manipulation Application

The excerpt provides insufficient information to assess applicability to humanoid locomotion-manipulation tasks. The paper's focus on "robotic manipulation" and compositional factorization seems potentially adaptable, but no direct discussion appears in this content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de9b1f19-9510-4909-88c3-9708dde3bbe9",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "75385e59-6510-4fda-aa01-ccdb2de46254",
  "toolUseResult": {
    "bytes": 46906,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Iterative Compositional Data Generation for Robot Control\"\n\n## Key Method\n\nThe paper proposes a **semantic compositional diffusion transformer** that addresses the challenge of expensive robotic data collection by learning to generate synthetic training data for unseen task combinations.\n\n## The Compositional Diffusion Transformer\n\nThe model \"factorizes transitions into robot-, object-, obstacle-, and objective-specific components and learns their interactions through attention.\" This architectural choice enables the system to decompose complex robotic tasks into reusable semantic elements rather than treating each task monolithically.\n\n## Self-Improvement Loop\n\nThe approach employs an iterative refinement mechanism: \"synthetic data is validated via offline reinforcement learning and incorporated into subsequent training rounds.\" This creates a feedback cycle where generated data is tested for quality before being used to retrain the model, progressively improving performance.\n\n## Evaluated Tasks\n\nThe abstract mentions evaluation on \"multi-object, multi-robot, and multi-environment settings\" with focus on \"held-out tasks\" and \"unseen task combinations,\" though specific task names aren't detailed in the provided content.\n\n## Limitations\n\nThe provided webpage content doesn't explicitly discuss limitations. The abstract notes the model \"struggle[s] to generalize to unseen task combinations\" in prior approaches, which their method addresses, but doesn't acknowledge their own limitations.\n\n## Humanoid Loco-Manipulation Application\n\nThe excerpt provides insufficient information to assess applicability to humanoid locomotion-manipulation tasks. The paper's focus on \"robotic manipulation\" and compositional factorization seems potentially adaptable, but no direct discussion appears in this content.",
    "durationMs": 4748,
    "url": "https://arxiv.org/abs/2512.10891"
  },
  "sourceToolAssistantUUID": "de9b1f19-9510-4909-88c3-9708dde3bbe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-10T17:14:48.784Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rd1tL7y2dfdyYag8bBKcFU`</summary>

```json
{
  "query": "humanoid robot data generation scaling law how much data needed VLA training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75385e59-6510-4fda-aa01-ccdb2de46254",
  "isSidechain": false,
  "requestId": "req_011CauGJqZgx1okmvcbSTXrX",
  "type": "assistant",
  "uuid": "dd60c666-3914-4236-82a0-96635cadd887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JP66E952sywwLuhqNzr6n6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 507,
      "cache_read_input_tokens": 52858,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 52858,
          "cache_creation_input_tokens": 507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 507
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

_source line 99 · 2026-05-10T17:14:55.902Z_

<details><summary>↩ Tool result · `toolu_01Rd1tL7y2dfdyYag8bBKcFU`</summary>

```text
Web search results for query: "humanoid robot data generation scaling law how much data needed VLA training 2025 2026"

Links: [{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots","url":"https://arxiv.org/html/2511.09241"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement ...","url":"https://arxiv.org/pdf/2509.09674"},{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"Scalable Vision-Language-Action Model Pretraining for ​Robotic Manipulation with Real-Life Human Activity Videos","url":"https://arxiv.org/html/2510.21571v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Vision Language Action Models (VLA) & Policies for Robots","url":"https://learnopencv.com/vision-language-action-models-lerobot-policy/"}]

Based on the search results, here's what recent research shows about humanoid robot data generation and scaling laws for VLA training:

## Scaling Laws and Data Requirements

Recent work by Lin et al. (2025) argues that scaling laws in robotics depend more on the number of environments and objects rather than the number of demonstrations. This suggests that diversity in training environments may be more important than raw data volume.

Robotics is considered data-constrained because the amount of robotics data readily available is orders of magnitude less than what's needed to reliably deploy general-purpose robots, as robot data collection is expensive and time-consuming.

## Data Generation Approaches

Rather than relying solely on real robot data, recent VLA models use a structured approach. The training data is organized by scale: large quantities of web data and human videos lay the base; synthetic data generated with physics simulations form the middle layer, and real-world data collected on physical robot hardware complete the top.

## Specific Data Scales (2025-2026)

Examples of current models show varying data requirements:

- Helix is a generalist VLA model for humanoid control trained on approximately 500 hours of high-quality, multi-robot dataset.

- The Humanoid-Union dataset comprises over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos.

The research emphasizes leveraging human videos and synthetic data as cost-effective alternatives to real robot data while maintaining grounding through smaller amounts of real-world robot demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd60c666-3914-4236-82a0-96635cadd887",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "53ed8dd3-0690-48b5-9780-c266457b105a",
  "toolUseResult": {
    "query": "humanoid robot data generation scaling law how much data needed VLA training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TEyf1JwP8DnBnVknQQp6zA",
        "content": [
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/pdf/2503.14734"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots",
            "url": "https://arxiv.org/html/2511.09241"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement ...",
            "url": "https://arxiv.org/pdf/2509.09674"
          },
          {
            "title": "2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "Scalable Vision-Language-Action Model Pretraining for ​Robotic Manipulation with Real-Life Human Activity Videos",
            "url": "https://arxiv.org/html/2510.21571v1"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Vision Language Action Models (VLA) & Policies for Robots",
            "url": "https://learnopencv.com/vision-language-action-models-lerobot-policy/"
          }
        ]
      },
      "Based on the search results, here's what recent research shows about humanoid robot data generation and scaling laws for VLA training:\n\n## Scaling Laws and Data Requirements\n\nRecent work by Lin et al. (2025) argues that scaling laws in robotics depend more on the number of environments and objects rather than the number of demonstrations. This suggests that diversity in training environments may be more important than raw data volume.\n\nRobotics is considered data-constrained because the amount of robotics data readily available is orders of magnitude less than what's needed to reliably deploy general-purpose robots, as robot data collection is expensive and time-consuming.\n\n## Data Generation Approaches\n\nRather than relying solely on real robot data, recent VLA models use a structured approach. The training data is organized by scale: large quantities of web data and human videos lay the base; synthetic data generated with physics simulations form the middle layer, and real-world data collected on physical robot hardware complete the top.\n\n## Specific Data Scales (2025-2026)\n\nExamples of current models show varying data requirements:\n\n- Helix is a generalist VLA model for humanoid control trained on approximately 500 hours of high-quality, multi-robot dataset.\n\n- The Humanoid-Union dataset comprises over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos.\n\nThe research emphasizes leveraging human videos and synthetic data as cost-effective alternatives to real robot data while maintaining grounding through smaller amounts of real-world robot demonstrations."
    ],
    "durationSeconds": 7.114172734000022
  },
  "sourceToolAssistantUUID": "dd60c666-3914-4236-82a0-96635cadd887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-10T17:15:04.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011GXwuS5fFD4oK4i3NsR7bF`</summary>

```json
{
  "query": "simulator-in-the-loop video diffusion robot trajectory generation physics grounding 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53ed8dd3-0690-48b5-9780-c266457b105a",
  "isSidechain": false,
  "requestId": "req_011CauGKdgqmSNAoJAvKRAUX",
  "type": "assistant",
  "uuid": "2580435e-90a9-4ce2-ae98-2e9fca9a2e27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vFneLnaTNWAaNonERuf2p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1055,
      "cache_read_input_tokens": 53365,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 53365,
          "cache_creation_input_tokens": 1055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1055
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

_source line 101 · 2026-05-10T17:15:12.658Z_

<details><summary>↩ Tool result · `toolu_011GXwuS5fFD4oK4i3NsR7bF`</summary>

```text
Web search results for query: "simulator-in-the-loop video diffusion robot trajectory generation physics grounding 2025 2026"

Links: [{"title":"V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors","url":"https://arxiv.org/html/2603.18811"},{"title":"(PDF) Physical Simulator In-the-Loop Video Generation","url":"https://www.researchgate.net/publication/401691824_Physical_Simulator_In-the-Loop_Video_Generation"},{"title":"Physical Simulator In-the-Loop Video Generation [Quick Review]","url":"https://liner.com/review/physical-simulator-intheloop-video-generation"},{"title":"GitHub - MarkHershey/PSIVG: [CVPR 2026] Physical Simulator In-the-Loop Video Generation · GitHub","url":"https://github.com/MarkHershey/PSIVG"},{"title":"Physical Simulator In-the-Loop Video Generation | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.06408"},{"title":"GitHub - ziqihuangg/Awesome-From-Video-Generation-to-World-Model: A list of works on video generation towards world model · GitHub","url":"https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/"},{"title":"Physical Simulator In-the-Loop Video Generation","url":"https://arxiv.org/html/2603.06408"},{"title":"[2603.06408] Physical Simulator In-the-Loop Video Generation","url":"https://arxiv.org/abs/2603.06408"},{"title":"Interactive World Simulator for Robot Policy Training and Evaluation","url":"https://www.yixuanwang.me/interactive_world_sim/texts/main.pdf"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"}]

I found several relevant research papers and projects on simulator-in-the-loop video diffusion for robot trajectory generation with physics grounding from 2025-2026. Here are the key findings:

## Primary Results

**Physical Simulator In-the-Loop Video Generation (PSIVG)**

PSIVG is a framework that integrates a physical simulator into the video diffusion process. Starting from a template video generated by a pre-trained diffusion model, PSIVG reconstructs the 4D scene and foreground object meshes, initializes them within a physical simulator, and generates physically consistent trajectories. These simulated trajectories are then used to guide the video generator toward spatio-temporally physically coherent motion. The framework includes a Test-Time Texture Consistency Optimization (TTCO) technique that adapts text and feature embeddings based on pixel correspondences from the simulator.

**V-Dreamer: Video Generation for Robot Trajectory Synthesis**

V-Dreamer is a fully automated framework that generates open-vocabulary, simulation-ready manipulation environments and executable expert trajectories directly from natural language instructions. It introduces a Video-Prior-Based Trajectory Generation approach that leverages state-of-the-art video generation models as rich motion priors to predict the manipulation process. To ground these generated visual motions into actionable data, the system develops a robust Sim-to-Gen visual-kinematic alignment module.

**Physics-Aware Video Generation Research**

Recent work introduces a physics-aware reinforcement learning paradigm for video generation models that enforces physical collision rules directly in high-dimensional spaces. This is extended to a unified framework, termed Mimicry-Discovery Cycle (MDcycle), which allows substantial fine-tuning while fully preserving the model's ability to leverage physics-grounded feedback.

These approaches represent significant progress in combining video diffusion models with physics simulation for robust robot trajectory generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2580435e-90a9-4ce2-ae98-2e9fca9a2e27",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "9ba410e8-4dbe-4268-aca7-93ff3dfa90bb",
  "toolUseResult": {
    "query": "simulator-in-the-loop video diffusion robot trajectory generation physics grounding 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NPB9Sfa1N6cK1kXC5qPe3g",
        "content": [
          {
            "title": "V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors",
            "url": "https://arxiv.org/html/2603.18811"
          },
          {
            "title": "(PDF) Physical Simulator In-the-Loop Video Generation",
            "url": "https://www.researchgate.net/publication/401691824_Physical_Simulator_In-the-Loop_Video_Generation"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation [Quick Review]",
            "url": "https://liner.com/review/physical-simulator-intheloop-video-generation"
          },
          {
            "title": "GitHub - MarkHershey/PSIVG: [CVPR 2026] Physical Simulator In-the-Loop Video Generation · GitHub",
            "url": "https://github.com/MarkHershey/PSIVG"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2603.06408"
          },
          {
            "title": "GitHub - ziqihuangg/Awesome-From-Video-Generation-to-World-Model: A list of works on video generation towards world model · GitHub",
            "url": "https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/"
          },
          {
            "title": "Physical Simulator In-the-Loop Video Generation",
            "url": "https://arxiv.org/html/2603.06408"
          },
          {
            "title": "[2603.06408] Physical Simulator In-the-Loop Video Generation",
            "url": "https://arxiv.org/abs/2603.06408"
          },
          {
            "title": "Interactive World Simulator for Robot Policy Training and Evaluation",
            "url": "https://www.yixuanwang.me/interactive_world_sim/texts/main.pdf"
          },
          {
            "title": "Video Generation Models in Robotics: Applications, Research Challenges, Future Directions",
            "url": "https://arxiv.org/html/2601.07823v1"
          }
        ]
      },
      "I found several relevant research papers and projects on simulator-in-the-loop video diffusion for robot trajectory generation with physics grounding from 2025-2026. Here are the key findings:\n\n## Primary Results\n\n**Physical Simulator In-the-Loop Video Generation (PSIVG)**\n\nPSIVG is a framework that integrates a physical simulator into the video diffusion process. Starting from a template video generated by a pre-trained diffusion model, PSIVG reconstructs the 4D scene and foreground object meshes, initializes them within a physical simulator, and generates physically consistent trajectories. These simulated trajectories are then used to guide the video generator toward spatio-temporally physically coherent motion. The framework includes a Test-Time Texture Consistency Optimization (TTCO) technique that adapts text and feature embeddings based on pixel correspondences from the simulator.\n\n**V-Dreamer: Video Generation for Robot Trajectory Synthesis**\n\nV-Dreamer is a fully automated framework that generates open-vocabulary, simulation-ready manipulation environments and executable expert trajectories directly from natural language instructions. It introduces a Video-Prior-Based Trajectory Generation approach that leverages state-of-the-art video generation models as rich motion priors to predict the manipulation process. To ground these generated visual motions into actionable data, the system develops a robust Sim-to-Gen visual-kinematic alignment module.\n\n**Physics-Aware Video Generation Research**\n\nRecent work introduces a physics-aware reinforcement learning paradigm for video generation models that enforces physical collision rules directly in high-dimensional spaces. This is extended to a unified framework, termed Mimicry-Discovery Cycle (MDcycle), which allows substantial fine-tuning while fully preserving the model's ability to leverage physics-grounded feedback.\n\nThese approaches represent significant progress in combining video diffusion models with physics simulation for robust robot trajectory generation."
    ],
    "durationSeconds": 8.410408343999995
  },
  "sourceToolAssistantUUID": "2580435e-90a9-4ce2-ae98-2e9fca9a2e27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 102_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "9ba410e8-4dbe-4268-aca7-93ff3dfa90bb",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 103_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 104 · 2026-05-10T17:15:33.913Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U7owBprg7X3tCULkUVfp8P`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.18811",
  "prompt": "Extract the key method of V-Dreamer. How does it generate robot trajectories from video priors? What is the Sim-to-Gen alignment module? What tasks and embodiments does it support? Does it handle humanoid robots? What are the limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ba410e8-4dbe-4268-aca7-93ff3dfa90bb",
  "isSidechain": false,
  "requestId": "req_011CauGLsJAusnjRJGXL9jQQ",
  "type": "assistant",
  "uuid": "33a7b4a6-b797-46fb-b670-93bc6e8a8882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CB1yEjTUSKM7voMdRvnnzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 54420,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 54420,
          "cache_creation_input_tokens": 1009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1009
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

_source line 105 · 2026-05-10T17:15:38.676Z_

<details><summary>↩ Tool result · `toolu_01U7owBprg7X3tCULkUVfp8P`</summary>

```text
# V-Dreamer: Key Method Overview

## Core Approach

V-Dreamer generates robot trajectories through a multi-stage pipeline. The system constructs "physically grounded 3D scenes using large language models and 3D generative models" and leverages "video generation models as rich motion priors." These visual predictions are then converted into executable robot commands.

## Sim-to-Gen Alignment Module

The critical innovation is a "robust Sim-to-Gen visual-kinematic alignment module utilizing CoTracker3 and VGGT." This component bridges the gap between generated video sequences and actual robot kinematics, translating visual motion into feasible joint trajectories.

## Supported Tasks & Embodiments

The paper demonstrates evaluation on "tabletop manipulation tasks using the Piper robotic arm." The framework supports "open-vocabulary, simulation-ready manipulation environments," indicating broad task generality, but specific embodiment diversity isn't detailed beyond this single robotic platform.

## Humanoid Robot Support

The content provides no evidence that V-Dreamer handles humanoid robots. Testing focuses exclusively on the Piper arm for tabletop manipulation.

## Limitations

The abstract doesn't explicitly discuss limitations. However, the 8-page paper length suggests constraints remain unaddressed in this excerpt. The emphasis on tabletop manipulation and single-arm testing implies potential limitations with complex multi-body systems or whole-body mobile manipulation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33a7b4a6-b797-46fb-b670-93bc6e8a8882",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "42b473db-8483-4031-8333-48e5f3a12517",
  "toolUseResult": {
    "bytes": 47399,
    "code": 200,
    "codeText": "OK",
    "result": "# V-Dreamer: Key Method Overview\n\n## Core Approach\n\nV-Dreamer generates robot trajectories through a multi-stage pipeline. The system constructs \"physically grounded 3D scenes using large language models and 3D generative models\" and leverages \"video generation models as rich motion priors.\" These visual predictions are then converted into executable robot commands.\n\n## Sim-to-Gen Alignment Module\n\nThe critical innovation is a \"robust Sim-to-Gen visual-kinematic alignment module utilizing CoTracker3 and VGGT.\" This component bridges the gap between generated video sequences and actual robot kinematics, translating visual motion into feasible joint trajectories.\n\n## Supported Tasks & Embodiments\n\nThe paper demonstrates evaluation on \"tabletop manipulation tasks using the Piper robotic arm.\" The framework supports \"open-vocabulary, simulation-ready manipulation environments,\" indicating broad task generality, but specific embodiment diversity isn't detailed beyond this single robotic platform.\n\n## Humanoid Robot Support\n\nThe content provides no evidence that V-Dreamer handles humanoid robots. Testing focuses exclusively on the Piper arm for tabletop manipulation.\n\n## Limitations\n\nThe abstract doesn't explicitly discuss limitations. However, the 8-page paper length suggests constraints remain unaddressed in this excerpt. The emphasis on tabletop manipulation and single-arm testing implies potential limitations with complex multi-body systems or whole-body mobile manipulation tasks.",
    "durationMs": 4759,
    "url": "https://arxiv.org/abs/2603.18811"
  },
  "sourceToolAssistantUUID": "33a7b4a6-b797-46fb-b670-93bc6e8a8882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 106 · 2026-05-10T17:15:38.683Z_

```json
{
  "parentUuid": "42b473db-8483-4031-8333-48e5f3a12517",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "943b0f77-34ef-4706-ae64-9f5357522bd1",
  "timestamp": "2026-05-10T17:15:38.683Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 107 · 2026-05-10T17:15:41.475Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0194XMb3oRDriaqgLMSjKmwn`</summary>

```json
{
  "query": "humanoid robot action space factorization upper body lower body locomotion manipulation decoupled generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "943b0f77-34ef-4706-ae64-9f5357522bd1",
  "isSidechain": false,
  "requestId": "req_011CauGNnaDYj4BFHyYmN3mt",
  "type": "assistant",
  "uuid": "ef70d23c-f9e1-4273-b745-1487d4021150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjnwCMSutWE67jr6idTAuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 55429,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 55429,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 567
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

_source line 108 · 2026-05-10T17:15:49.412Z_

<details><summary>↩ Tool result · `toolu_0194XMb3oRDriaqgLMSjKmwn`</summary>

```text
Web search results for query: "humanoid robot action space factorization upper body lower body locomotion manipulation decoupled generation 2025 2026"

Links: [{"title":"arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control","url":"https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control","url":"https://mobile-tv.github.io/resources/pmp.pdf"},{"title":"A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots","url":"https://arxiv.org/html/2506.20487v2"},{"title":"Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control","url":"https://arxiv.org/html/2412.07773v1"},{"title":"Natural Humanoid Robot Locomotion with Generative Motion Prior","url":"https://arxiv.org/html/2503.09015v1"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://arxiv.org/html/2410.12773v1"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"Whole-body control for humanoid robot locomotion | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/whole-body-control-for-humanoid-robot-locomotion-2/"},{"title":"Frontiers | Walking control of humanoid robots based on improved footstep planner and whole-body coordination controller","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1538979/full"}]

I've completed a web search for humanoid robot action space factorization, upper body/lower body locomotion and manipulation decoupled generation for 2025-2026. Here are the key findings:

## Recent Approaches to Decoupled Humanoid Control

A decoupling approach uses inverse kinematics (IK) and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion. One method decouples upper-body control from locomotion using inverse kinematics and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion, introducing Predictive Motion Priors (PMP) trained with Conditional Variational Autoencoder (CVAE) to effectively represent upper-body motions, with the locomotion policy trained conditioned on this upper-body motion representation.

## Vision-Language Integration with Decoupled Action Processing

One approach decouples the learning process by first training the vision-language component using kinematics reconstruction, then freezing its latent space and training a separate action module that samples from it to learn a proprioception-only controller focused on robot dynamics.

## Whole-Body Control Architecture

Recent work decouples the robot's upper and lower body, independently constructing dynamic models for each, then designs a whole-body coordination controller which incorporates both a Lower-body WBC and an Upper-body WBC to independently control the robot's lower and upper body.

## Modular Skill Decomposition

ModSkill introduces a modular framework that decouples full-body motion into part-specific skills for individual body parts, allowing for efficient and scalable learning, with each body part controlled independently by a low-level controller.

The search results show that decoupled generation strategies for humanoid robots have become a dominant approach in 2025-2026, with various implementations ranging from IK-based upper body control with RL-based locomotion to latent space representations and modular skill frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef70d23c-f9e1-4273-b745-1487d4021150",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "c5b34de0-e2c7-4a92-8019-0c1ceb1cbd6d",
  "toolUseResult": {
    "query": "humanoid robot action space factorization upper body lower body locomotion manipulation decoupled generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NTWEmL8jKDnRFYxbgesDAB",
        "content": [
          {
            "title": "arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control",
            "url": "https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control",
            "url": "https://mobile-tv.github.io/resources/pmp.pdf"
          },
          {
            "title": "A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots",
            "url": "https://arxiv.org/html/2506.20487v2"
          },
          {
            "title": "Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control",
            "url": "https://arxiv.org/html/2412.07773v1"
          },
          {
            "title": "Natural Humanoid Robot Locomotion with Generative Motion Prior",
            "url": "https://arxiv.org/html/2503.09015v1"
          },
          {
            "title": "Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions",
            "url": "https://arxiv.org/html/2410.12773v1"
          },
          {
            "title": "Advancements in humanoid robot dynamics and learning-based locomotion control methods",
            "url": "https://www.oaepublish.com/articles/ir.2025.32"
          },
          {
            "title": "Whole-body control for humanoid robot locomotion | PatSnap",
            "url": "https://www.patsnap.com/resources/blog/articles/whole-body-control-for-humanoid-robot-locomotion-2/"
          },
          {
            "title": "Frontiers | Walking control of humanoid robots based on improved footstep planner and whole-body coordination controller",
            "url": "https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1538979/full"
          }
        ]
      },
      "I've completed a web search for humanoid robot action space factorization, upper body/lower body locomotion and manipulation decoupled generation for 2025-2026. Here are the key findings:\n\n## Recent Approaches to Decoupled Humanoid Control\n\nA decoupling approach uses inverse kinematics (IK) and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion. One method decouples upper-body control from locomotion using inverse kinematics and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion, introducing Predictive Motion Priors (PMP) trained with Conditional Variational Autoencoder (CVAE) to effectively represent upper-body motions, with the locomotion policy trained conditioned on this upper-body motion representation.\n\n## Vision-Language Integration with Decoupled Action Processing\n\nOne approach decouples the learning process by first training the vision-language component using kinematics reconstruction, then freezing its latent space and training a separate action module that samples from it to learn a proprioception-only controller focused on robot dynamics.\n\n## Whole-Body Control Architecture\n\nRecent work decouples the robot's upper and lower body, independently constructing dynamic models for each, then designs a whole-body coordination controller which incorporates both a Lower-body WBC and an Upper-body WBC to independently control the robot's lower and upper body.\n\n## Modular Skill Decomposition\n\nModSkill introduces a modular framework that decouples full-body motion into part-specific skills for individual body parts, allowing for efficient and scalable learning, with each body part controlled independently by a low-level controller.\n\nThe search results show that decoupled generation strategies for humanoid robots have become a dominant approach in 2025-2026, with various implementations ranging from IK-based upper body control with RL-based locomotion to latent space representations and modular skill frameworks."
    ],
    "durationSeconds": 7.931925280000025
  },
  "sourceToolAssistantUUID": "ef70d23c-f9e1-4273-b745-1487d4021150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-10T17:15:52.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TENjj7bdYjTEheM7BYL5p1`</summary>

```json
{
  "query": "LLM task program synthesis humanoid robot demonstration generation automated curriculum 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5b34de0-e2c7-4a92-8019-0c1ceb1cbd6d",
  "isSidechain": false,
  "requestId": "req_011CauGPaUUTHVJKWwbFVeiY",
  "type": "assistant",
  "uuid": "356ce340-a567-44c4-8626-75f94325476b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VhmdHDn3ocgZhsxYQY1mH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 55996,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 55996,
          "cache_creation_input_tokens": 1106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1106
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

_source line 110 · 2026-05-10T17:16:00.889Z_

<details><summary>↩ Tool result · `toolu_01TENjj7bdYjTEheM7BYL5p1`</summary>

```text
Web search results for query: "LLM task program synthesis humanoid robot demonstration generation automated curriculum 2025 2026"

Links: [{"title":"CurricuLLM - ICON Lab - Negar Mehr","url":"https://iconlab.negarmehr.com/CurricuLLM/"},{"title":"CurricuLLM: Automatic Task Curricula Des...","url":"https://axi.lims.ac.uk/paper/2409.18382"},{"title":"GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub","url":"https://github.com/GT-RIPL/Awesome-LLM-Robotics"},{"title":"CurricuLLM: Automatic Task Curricula Design for Learning Complex","url":"https://hybrid-robotics.berkeley.edu/publications/ICRA2025_CurricuLLM.pdf"},{"title":"CurricuLLM: Automatic Task Curricula Design for Learning Complex Robot Skills using Large Language Models","url":"https://arxiv.org/html/2409.18382v2"},{"title":"An LLM-enabled human demonstration-assisted hybrid robot skill synthesis approach for human-robot collaborative assembly - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0007850625000630"},{"title":"HUMANOID-LLA: OPEN-VOCABULARY ...","url":"https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"},{"title":"Full article: Evaluating LLMs for Code Generation in HRI: A Comparative Study of ChatGPT, Gemini, and Claude","url":"https://www.tandfonline.com/doi/full/10.1080/08839514.2024.2439610"},{"title":"Programming-by-Demonstration for Long-Horizon Robot Tasks","url":"https://www.cs.utexas.edu/~isil/prolex.pdf"},{"title":"ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10514-023-10135-3"}]

Based on the web search results, I found highly relevant research on your query. Here are the key findings:

## CurricuLLM: Primary Result

CurricuLLM is titled "Automatic Task Curricula Design for Learning Complex Robot Skills using Large Language Models" and was presented at the 2025 International Conference on Robotics and Automation (ICRA).

CurricuLLM leverages the high-level planning and programming capabilities of LLMs for curriculum design, thereby enhancing the efficient learning of complex tasks. The system consists of: (Step 1) Generating sequence of subtasks in natural language form, (Step 2) Translating natural language description of subtasks in executable task code, including the reward code and goal distribution code, and (Step 3) Evaluating trained policies based on trajectory rollout and subtask description.

CurricuLLM was evaluated in various robotics simulation environments, ranging from manipulation, navigation, and locomotion, and the humanoid locomotion policy learned through CurricuLLM was validated in real-world.

The research used the Berkeley Humanoid environment and validated the policy trained with CurricuLLM on the Berkeley Humanoid, illustrating that the policy learned through CurricuLLM can be transferred to the real world.

## Related Work

The search also revealed other relevant approaches for LLM-based robotics:
- ProLex, a programmatic learning from demonstration algorithm that targets long-horizon robot tasks requiring synthesizing programs with complex control flow structures, first learns a program sketch and then completes it using an LLM-guided search procedure.
- ProgPrompt, which presents a programmatic LLM prompt structure that enables plan generation across situated environments, robot capabilities, and tasks, leveraging LLMs' strengths in both world knowledge and programming language understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "356ce340-a567-44c4-8626-75f94325476b",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "1a61c2cc-c878-416c-885a-e1eee2dda2e8",
  "toolUseResult": {
    "query": "LLM task program synthesis humanoid robot demonstration generation automated curriculum 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UX99TFR2piyz2NaT4Z5uRE",
        "content": [
          {
            "title": "CurricuLLM - ICON Lab - Negar Mehr",
            "url": "https://iconlab.negarmehr.com/CurricuLLM/"
          },
          {
            "title": "CurricuLLM: Automatic Task Curricula Des...",
            "url": "https://axi.lims.ac.uk/paper/2409.18382"
          },
          {
            "title": "GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub",
            "url": "https://github.com/GT-RIPL/Awesome-LLM-Robotics"
          },
          {
            "title": "CurricuLLM: Automatic Task Curricula Design for Learning Complex",
            "url": "https://hybrid-robotics.berkeley.edu/publications/ICRA2025_CurricuLLM.pdf"
          },
          {
            "title": "CurricuLLM: Automatic Task Curricula Design for Learning Complex Robot Skills using Large Language Models",
            "url": "https://arxiv.org/html/2409.18382v2"
          },
          {
            "title": "An LLM-enabled human demonstration-assisted hybrid robot skill synthesis approach for human-robot collaborative assembly - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0007850625000630"
          },
          {
            "title": "HUMANOID-LLA: OPEN-VOCABULARY ...",
            "url": "https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"
          },
          {
            "title": "Full article: Evaluating LLMs for Code Generation in HRI: A Comparative Study of ChatGPT, Gemini, and Claude",
            "url": "https://www.tandfonline.com/doi/full/10.1080/08839514.2024.2439610"
          },
          {
            "title": "Programming-by-Demonstration for Long-Horizon Robot Tasks",
            "url": "https://www.cs.utexas.edu/~isil/prolex.pdf"
          },
          {
            "title": "ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10514-023-10135-3"
          }
        ]
      },
      "Based on the web search results, I found highly relevant research on your query. Here are the key findings:\n\n## CurricuLLM: Primary Result\n\nCurricuLLM is titled \"Automatic Task Curricula Design for Learning Complex Robot Skills using Large Language Models\" and was presented at the 2025 International Conference on Robotics and Automation (ICRA).\n\nCurricuLLM leverages the high-level planning and programming capabilities of LLMs for curriculum design, thereby enhancing the efficient learning of complex tasks. The system consists of: (Step 1) Generating sequence of subtasks in natural language form, (Step 2) Translating natural language description of subtasks in executable task code, including the reward code and goal distribution code, and (Step 3) Evaluating trained policies based on trajectory rollout and subtask description.\n\nCurricuLLM was evaluated in various robotics simulation environments, ranging from manipulation, navigation, and locomotion, and the humanoid locomotion policy learned through CurricuLLM was validated in real-world.\n\nThe research used the Berkeley Humanoid environment and validated the policy trained with CurricuLLM on the Berkeley Humanoid, illustrating that the policy learned through CurricuLLM can be transferred to the real world.\n\n## Related Work\n\nThe search also revealed other relevant approaches for LLM-based robotics:\n- ProLex, a programmatic learning from demonstration algorithm that targets long-horizon robot tasks requiring synthesizing programs with complex control flow structures, first learns a program sketch and then completes it using an LLM-guided search procedure.\n- ProgPrompt, which presents a programmatic LLM prompt structure that enables plan generation across situated environments, robot capabilities, and tasks, leveraging LLMs' strengths in both world knowledge and programming language understanding."
    ],
    "durationSeconds": 8.610015554000041
  },
  "sourceToolAssistantUUID": "356ce340-a567-44c4-8626-75f94325476b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-10T17:16:04.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7Va9L1pwxRfEpJTFsL2H9`</summary>

```json
{
  "query": "humanoid robot skill composition task graph procedural data generation diverse demonstration 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a61c2cc-c878-416c-885a-e1eee2dda2e8",
  "isSidechain": false,
  "requestId": "req_011CauGQRYye7FWiJ8mzA2B2",
  "type": "assistant",
  "uuid": "f2aac588-1d7e-4cbd-92c9-ac0e0fd2e25a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018emmmchPXTbS8PjqFLyvMf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 57102,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 57102,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
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

_source line 112 · 2026-05-10T17:16:15.075Z_

<details><summary>↩ Tool result · `toolu_01K7Va9L1pwxRfEpJTFsL2H9`</summary>

```text
Web search results for query: "humanoid robot skill composition task graph procedural data generation diverse demonstration 2025 2026 arxiv"

Links: [{"title":"SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation","url":"https://arxiv.org/html/2603.25725v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation","url":"https://arxiv.org/html/2601.09031v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v2"},{"title":"RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation","url":"https://arxiv.org/html/2311.01455v3"},{"title":"DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning","url":"https://arxiv.org/html/2506.16012v1"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"Robotic Manipulation via Imitation Learning: Taxonomy, Evolution, Benchmark, and Challenges","url":"https://arxiv.org/html/2508.17449v1"},{"title":"RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot","url":"https://rh20t.github.io/"}]

I found several highly relevant research papers on arxiv from 2025-2026 related to humanoid robot skill composition, task graphs, procedural data generation, and diverse demonstrations. Here are the key findings:

## Key Papers Found:

**1. SoftMimicGen (2026)** - A data generation system that enables efficient scaling of data collection while preserving task-relevant diversity, substantially reducing human effort required to train visuomotor policies for deformable object manipulation tasks. Using a small set of human teleoperated trajectories, SoftMimicGen enables more robust and effective policy learning, significantly reducing the reliance on costly and time-consuming human data collection. The system successfully generates demonstrations across multiple platforms including the GR1 humanoid, Franka Panda arm, surgical robot, and bimanual YAM arms.

**2. RGMP-S (2026)** - Recurrent Geometric-prior Multimodal Policy with Spiking features, facilitating both high-level skill reasoning and data-efficient motion synthesis. The framework advances skill selection via a hierarchical Chain-of-Thought mechanism, enabling the structured decomposition of intricate goals into multi-stage sequences, significantly boosting performance on long-horizon manipulation tasks.

**3. GR00T N1 (2025)** - A Vision-Language-Action model for humanoid robots trained on diverse data sources, containing a vision-language backbone and a DiT-based flow-matching policy that outputs high-frequency actions. The model is pre-trained end-to-end across three data layers: annotated video datasets, synthetically generated datasets, and real-robot trajectories.

**4. RoboGen (2024)** - A generative robotic agent that automatically learns diverse robotic skills at scale via generative simulation, using generative models to automatically generate diversified tasks, scenes, and training supervisions for scaling up robotic skill learning with minimal human supervision.

**5. Humanoid Everyday (2025)** - A large-scale and diverse humanoid manipulation dataset characterized by extensive task variety involving dextrous object manipulation, human-humanoid interaction, locomotion-integrated actions, and more.

These papers collectively address skill composition, procedural data generation, and the use of diverse demonstrations for humanoid robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2aac588-1d7e-4cbd-92c9-ac0e0fd2e25a",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "aebd877e-2038-47af-85d3-4adae7e170ba",
  "toolUseResult": {
    "query": "humanoid robot skill composition task graph procedural data generation diverse demonstration 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MzgDuQzUZKcoFcgUdKCpDg",
        "content": [
          {
            "title": "SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation",
            "url": "https://arxiv.org/html/2603.25725v1"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation",
            "url": "https://arxiv.org/html/2601.09031v1"
          },
          {
            "title": "Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors",
            "url": "https://arxiv.org/html/2501.02116v1"
          },
          {
            "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/html/2503.14734v2"
          },
          {
            "title": "RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation",
            "url": "https://arxiv.org/html/2311.01455v3"
          },
          {
            "title": "DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning",
            "url": "https://arxiv.org/html/2506.16012v1"
          },
          {
            "title": "Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation",
            "url": "https://arxiv.org/html/2510.08807v1"
          },
          {
            "title": "Robotic Manipulation via Imitation Learning: Taxonomy, Evolution, Benchmark, and Challenges",
            "url": "https://arxiv.org/html/2508.17449v1"
          },
          {
            "title": "RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot",
            "url": "https://rh20t.github.io/"
          }
        ]
      },
      "I found several highly relevant research papers on arxiv from 2025-2026 related to humanoid robot skill composition, task graphs, procedural data generation, and diverse demonstrations. Here are the key findings:\n\n## Key Papers Found:\n\n**1. SoftMimicGen (2026)** - A data generation system that enables efficient scaling of data collection while preserving task-relevant diversity, substantially reducing human effort required to train visuomotor policies for deformable object manipulation tasks. Using a small set of human teleoperated trajectories, SoftMimicGen enables more robust and effective policy learning, significantly reducing the reliance on costly and time-consuming human data collection. The system successfully generates demonstrations across multiple platforms including the GR1 humanoid, Franka Panda arm, surgical robot, and bimanual YAM arms.\n\n**2. RGMP-S (2026)** - Recurrent Geometric-prior Multimodal Policy with Spiking features, facilitating both high-level skill reasoning and data-efficient motion synthesis. The framework advances skill selection via a hierarchical Chain-of-Thought mechanism, enabling the structured decomposition of intricate goals into multi-stage sequences, significantly boosting performance on long-horizon manipulation tasks.\n\n**3. GR00T N1 (2025)** - A Vision-Language-Action model for humanoid robots trained on diverse data sources, containing a vision-language backbone and a DiT-based flow-matching policy that outputs high-frequency actions. The model is pre-trained end-to-end across three data layers: annotated video datasets, synthetically generated datasets, and real-robot trajectories.\n\n**4. RoboGen (2024)** - A generative robotic agent that automatically learns diverse robotic skills at scale via generative simulation, using generative models to automatically generate diversified tasks, scenes, and training supervisions for scaling up robotic skill learning with minimal human supervision.\n\n**5. Humanoid Everyday (2025)** - A large-scale and diverse humanoid manipulation dataset characterized by extensive task variety involving dextrous object manipulation, human-humanoid interaction, locomotion-integrated actions, and more.\n\nThese papers collectively address skill composition, procedural data generation, and the use of diverse demonstrations for humanoid robot learning."
    ],
    "durationSeconds": 10.126112714999996
  },
  "sourceToolAssistantUUID": "f2aac588-1d7e-4cbd-92c9-ac0e0fd2e25a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 113_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "aebd877e-2038-47af-85d3-4adae7e170ba",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 114_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 115 · 2026-05-10T17:16:30.033Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016gbcwMfA7EGeGooFEMzSGY`</summary>

```json
{
  "query": "HumanoidGen LLM reasoning bimanual dexterous manipulation data generation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebd877e-2038-47af-85d3-4adae7e170ba",
  "isSidechain": false,
  "requestId": "req_011CauGRUC1FetKVfLJCjifn",
  "type": "assistant",
  "uuid": "b884f811-5ab1-4939-8b33-091f2aad0f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DU2C4NY8zSBHnFhPPkDhTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 58196,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 58196,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1115
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

_source line 116 · 2026-05-10T17:16:37.949Z_

<details><summary>↩ Tool result · `toolu_016gbcwMfA7EGeGooFEMzSGY`</summary>

```text
Web search results for query: "HumanoidGen LLM reasoning bimanual dexterous manipulation data generation 2025 arxiv"

Links: [{"title":"[2507.00833] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833"},{"title":"[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833v2"},{"title":"GitHub - TeleHuman/HumanoidGen: [NeurIPS 2025] Official Implementation of \"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning\"","url":"https://github.com/TeleHuman/HumanoidGen"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=Mk9ykil8eP"},{"title":"NeurIPS Poster HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://neurips.cc/virtual/2025/poster/118438"},{"title":"Github","url":"https://openhumanoidgen.github.io/"},{"title":"(PDF) HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://www.researchgate.net/publication/393260954_HumanoidGen_Data_Generation_for_Bimanual_Dexterous_Manipulation_via_LLM_Reasoning"},{"title":"Data Generation for Bimanual Dexterous Manipulation via ...","url":"https://openreview.net/pdf/753bcc41dc0fe6dba41a235116449a37aba704f7.pdf"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"}]

I found detailed information about HumanoidGen. Here's a summary of the research:

## Overview

HumanoidGen is an automated framework for scene generation, demonstration collection, and data generalization for bimanual dexterous manipulation, aiming to provide high-quality demonstrations over diverse scenarios to facilitate data scaling and policy learning.

## Key Approach

The framework provides spatial annotations for both assets and dexterous hands based on atomic operations, and uses an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes.

To further improve planning ability, it employs a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation.

## Experimental Results

The researchers create a novel benchmark with augmented scenarios to evaluate the quality of the collected data, and the results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset.

## Publication

The paper is published on arXiv as arXiv:2507.00833, with version 2 submitted on November 16, 2025, and it was accepted as a NeurIPS 2025 poster. The authors are Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yugang Jiang, and Chenjia Bai.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b884f811-5ab1-4939-8b33-091f2aad0f8c",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "2a604a2b-4956-4e41-88bb-a2f3f18dcb67",
  "toolUseResult": {
    "query": "HumanoidGen LLM reasoning bimanual dexterous manipulation data generation 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TzfRuJVQ7H5ipsqEQ5Ewqh",
        "content": [
          {
            "title": "[2507.00833] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning",
            "url": "https://arxiv.org/abs/2507.00833"
          },
          {
            "title": "[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning",
            "url": "https://arxiv.org/abs/2507.00833v1"
          },
          {
            "title": "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning",
            "url": "https://arxiv.org/html/2507.00833v2"
          },
          {
            "title": "GitHub - TeleHuman/HumanoidGen: [NeurIPS 2025] Official Implementation of \"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning\"",
            "url": "https://github.com/TeleHuman/HumanoidGen"
          },
          {
            "title": "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=Mk9ykil8eP"
          },
          {
            "title": "NeurIPS Poster HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning",
            "url": "https://neurips.cc/virtual/2025/poster/118438"
          },
          {
            "title": "Github",
            "url": "https://openhumanoidgen.github.io/"
          },
          {
            "title": "(PDF) HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning",
            "url": "https://www.researchgate.net/publication/393260954_HumanoidGen_Data_Generation_for_Bimanual_Dexterous_Manipulation_via_LLM_Reasoning"
          },
          {
            "title": "Data Generation for Bimanual Dexterous Manipulation via ...",
            "url": "https://openreview.net/pdf/753bcc41dc0fe6dba41a235116449a37aba704f7.pdf"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          }
        ]
      },
      "I found detailed information about HumanoidGen. Here's a summary of the research:\n\n## Overview\n\nHumanoidGen is an automated framework for scene generation, demonstration collection, and data generalization for bimanual dexterous manipulation, aiming to provide high-quality demonstrations over diverse scenarios to facilitate data scaling and policy learning.\n\n## Key Approach\n\nThe framework provides spatial annotations for both assets and dexterous hands based on atomic operations, and uses an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes.\n\nTo further improve planning ability, it employs a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation.\n\n## Experimental Results\n\nThe researchers create a novel benchmark with augmented scenarios to evaluate the quality of the collected data, and the results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset.\n\n## Publication\n\nThe paper is published on arXiv as arXiv:2507.00833, with version 2 submitted on November 16, 2025, and it was accepted as a NeurIPS 2025 poster. The authors are Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yugang Jiang, and Chenjia Bai."
    ],
    "durationSeconds": 7.912229931999987
  },
  "sourceToolAssistantUUID": "b884f811-5ab1-4939-8b33-091f2aad0f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 117 · 2026-05-10T17:16:42.566Z_

This is a critical concurrent work — HumanoidGen (NeurIPS 2025) is very close to several potential directions. Let me now do targeted searches for remaining gaps and ideas that are clearly differentiated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a604a2b-4956-4e41-88bb-a2f3f18dcb67",
  "isSidechain": false,
  "requestId": "req_011CauGT9yBx2f7fUxkTwNd2",
  "type": "assistant",
  "uuid": "20bba810-2b2c-46ee-a7ed-2cb13b101eda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QU9h7nUvuTww3mnBa2HL7z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 59311,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 59311,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1012
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

_source line 118 · 2026-05-10T17:16:43.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MjM4PwS1DHhFBuuoWsVJJc`</summary>

```json
{
  "query": "video world model humanoid locomotion manipulation joint generation CogVideoX OpenSora fine-tune robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20bba810-2b2c-46ee-a7ed-2cb13b101eda",
  "isSidechain": false,
  "requestId": "req_011CauGT9yBx2f7fUxkTwNd2",
  "type": "assistant",
  "uuid": "e036f022-693f-4b65-8fba-b93cd2432c14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QU9h7nUvuTww3mnBa2HL7z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 59311,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 59311,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1012
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

_source line 119 · 2026-05-10T17:16:55.156Z_

<details><summary>↩ Tool result · `toolu_01MjM4PwS1DHhFBuuoWsVJJc`</summary>

```text
Web search results for query: "video world model humanoid locomotion manipulation joint generation CogVideoX OpenSora fine-tune robot 2026"

Links: [{"title":"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields","url":"https://arxiv.org/html/2605.06192v1"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"31 Open-Source AI Video Models: Free Tools to Make Videos in 2026 — AI Free Forever","url":"https://aifreeforever.com/blog/open-source-ai-video-models-free-tools-to-make-videos"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163"},{"title":"GitHub - operator22th/awesome-world-models-for-robots: Awesome World Model for Robotics Papers · GitHub","url":"https://github.com/operator22th/awesome-world-models-for-robots"},{"title":"Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation","url":"https://homangab.github.io/gen2act/"},{"title":"WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA","url":"https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"}]

Based on the search results, I found several highly relevant recent papers and projects on video world models for robotics that combine humanoid locomotion, manipulation, and joint generation. Here are the key findings:

## Video World Models for Robotic Control

Pretrained video diffusion models provide powerful spatiotemporal generative priors, making them a natural foundation for robotic world models. Several cutting-edge approaches are being developed:

### EA-WM: Event-Aware Generative World Model
EA-WM is an Event-Aware Generative World Model that effectively closes the loop between kinematic control and visual perception. It outperforms CogVideoX by 5.52 points on the P3CScore metric, with improvements in Interaction Quality from 0.594 to 0.682, Trajectory Accuracy from 0.353 to 0.430, and Instruction Following from 0.727 to 0.792.

### Fine-tuning Video Models for Robotics
Research has initialized IRASim with the pre-trained weights of OpenSora to expedite training. Other work utilizes Stable Video Diffusion, fine-tuned with robotic videos to adapt to the robotics domain. Aether fine-tunes a video model (CogVideoX) to generate depth and camera raymap videos, from which a 3D scene representation is extracted via back-projection.

### Whole-Body Humanoid Control
WholeBodyVLA learns unified latent actions from action-free egocentric videos through a Latent Action Model (LAM), and the system encodes egocentric images and language instructions into latent action tokens, which are decoded into dual-arm joint actions and locomotion commands, enabling end-to-end control for complex loco-manipulation tasks.

### Performance Challenges
Models consistently score higher on coarse-grained locomotion tasks (Quadruped, Humanoid) than on fine-grained manipulation, implying that mastering the fine-grained contact dynamics required for object interaction is physically more challenging than generating the rhythmic patterns of legged locomotion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e036f022-693f-4b65-8fba-b93cd2432c14",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "86e1ebaa-04c9-413a-a15f-7285fc1668f3",
  "toolUseResult": {
    "query": "video world model humanoid locomotion manipulation joint generation CogVideoX OpenSora fine-tune robot 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CT9PfpnPdTja5yXwRcAuJZ",
        "content": [
          {
            "title": "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields",
            "url": "https://arxiv.org/html/2605.06192v1"
          },
          {
            "title": "Rethinking Video Generation Model for the Embodied World",
            "url": "https://arxiv.org/html/2601.15282v1"
          },
          {
            "title": "Video Generation Models in Robotics: Applications, Research Challenges, Future Directions",
            "url": "https://arxiv.org/html/2601.07823v1"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "31 Open-Source AI Video Models: Free Tools to Make Videos in 2026 — AI Free Forever",
            "url": "https://aifreeforever.com/blog/open-source-ai-video-models-free-tools-to-make-videos"
          },
          {
            "title": "A Step Toward World Models: A Survey on Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.02097v1"
          },
          {
            "title": "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning",
            "url": "https://arxiv.org/html/2601.16163"
          },
          {
            "title": "GitHub - operator22th/awesome-world-models-for-robots: Awesome World Model for Robotics Papers · GitHub",
            "url": "https://github.com/operator22th/awesome-world-models-for-robots"
          },
          {
            "title": "Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation",
            "url": "https://homangab.github.io/gen2act/"
          },
          {
            "title": "WholebodyVLA/README.md at main · OpenDriveLab/WholebodyVLA",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, I found several highly relevant recent papers and projects on video world models for robotics that combine humanoid locomotion, manipulation, and joint generation. Here are the key findings:\n\n## Video World Models for Robotic Control\n\nPretrained video diffusion models provide powerful spatiotemporal generative priors, making them a natural foundation for robotic world models. Several cutting-edge approaches are being developed:\n\n### EA-WM: Event-Aware Generative World Model\nEA-WM is an Event-Aware Generative World Model that effectively closes the loop between kinematic control and visual perception. It outperforms CogVideoX by 5.52 points on the P3CScore metric, with improvements in Interaction Quality from 0.594 to 0.682, Trajectory Accuracy from 0.353 to 0.430, and Instruction Following from 0.727 to 0.792.\n\n### Fine-tuning Video Models for Robotics\nResearch has initialized IRASim with the pre-trained weights of OpenSora to expedite training. Other work utilizes Stable Video Diffusion, fine-tuned with robotic videos to adapt to the robotics domain. Aether fine-tunes a video model (CogVideoX) to generate depth and camera raymap videos, from which a 3D scene representation is extracted via back-projection.\n\n### Whole-Body Humanoid Control\nWholeBodyVLA learns unified latent actions from action-free egocentric videos through a Latent Action Model (LAM), and the system encodes egocentric images and language instructions into latent action tokens, which are decoded into dual-arm joint actions and locomotion commands, enabling end-to-end control for complex loco-manipulation tasks.\n\n### Performance Challenges\nModels consistently score higher on coarse-grained locomotion tasks (Quadruped, Humanoid) than on fine-grained manipulation, implying that mastering the fine-grained contact dynamics required for object interaction is physically more challenging than generating the rhythmic patterns of legged locomotion."
    ],
    "durationSeconds": 11.551579674999987
  },
  "sourceToolAssistantUUID": "e036f022-693f-4b65-8fba-b93cd2432c14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-10T17:16:58.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016NEGoy75RaQy4NsMrnZN6d`</summary>

```json
{
  "query": "humanoid whole-body trajectory generation contact sequence planning manipulation walking 2025 2026 arxiv method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86e1ebaa-04c9-413a-a15f-7285fc1668f3",
  "isSidechain": false,
  "requestId": "req_011CauGURYb7ZfZqWiad3BiS",
  "type": "assistant",
  "uuid": "093a8d6a-8aea-4c06-8d13-8941e89dc55f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xNegCzaLToRJemcgKxsy5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 60323,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 60323,
          "cache_creation_input_tokens": 1144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1144
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

_source line 121 · 2026-05-10T17:17:07.253Z_

<details><summary>↩ Tool result · `toolu_016NEGoy75RaQy4NsMrnZN6d`</summary>

```text
Web search results for query: "humanoid whole-body trajectory generation contact sequence planning manipulation walking 2025 2026 arxiv method"

Links: [{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Task and Motion Planning for Humanoid Loco-manipulation","url":"https://arxiv.org/html/2508.14099"},{"title":"WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts","url":"https://arxiv.org/html/2406.06005v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"One-shot Humanoid Whole-body Motion Learning","url":"https://arxiv.org/html/2510.25241v1"},{"title":"TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality","url":"https://arxiv.org/html/2506.15146v1"},{"title":"Humanoid Loco-Manipulations Pattern Generation and Stabilization Control","url":"https://arxiv.org/html/2505.24116"},{"title":"Natural Humanoid Robot Locomotion with Generative Motion Prior","url":"https://arxiv.org/html/2503.09015v1"},{"title":"Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations","url":"https://arxiv.org/html/2602.06643v2"},{"title":"[2509.11839] TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning","url":"https://arxiv.org/abs/2509.11839"}]

I found several relevant arxiv papers from 2025-2026 on humanoid whole-body trajectory generation, contact sequence planning, and loco-manipulation. Here are the key results:

## Recent Methods (2025-2026)

**1. Humanoid Locomotion and Manipulation Survey** (January 2025)
This work addresses humanoid whole-body loco-manipulation planning, where planners must solve trajectories that handle rich interactions with environments or objects, requiring decisions about contact position, contact mode, and contact force. Model Predictive Control (MPC) is highlighted as one of the most popular approaches to trajectory planning for locomotion and manipulation due to its flexibility to define versatile motion objectives and availability of solvers.

**2. Task and Motion Planning for Humanoid Loco-manipulation** (August 2025)
This work presents an optimization-based task and motion planning framework that unifies planning for locomotion and manipulation through a shared representation of contact modes, with symbolic actions defined as contact mode changes. This is the first work enabling integrated TAMP formulation with fully acyclic planning and whole body dynamics with actuation constraints for humanoid loco-manipulation.

**3. WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts** (June 2024)
This framework enables end-to-end RL-based controllers for four challenging whole-body humanoid tasks involving diverse contact sequences: parkour jumping, box loco-manipulation, dynamic dancing, and cliffside climbing.

**4. TACT: Humanoid Whole-body Contact Manipulation** (June 2025)
This work leverages LIPM-based biped control to enable the robot to maintain balance and continue walking while its upper body is governed by a learned policy for contact manipulation.

**5. Humanoid Loco-Manipulations Pattern Generation and Stabilization Control** (May 2025)
The method derives bipedal dynamics accounting for external manipulation forces, proposing a pattern generator to plan center of mass trajectories consistent with manipulation force references and a stabilizer to compensate for force tracking errors.

These papers represent the state-of-the-art in combining contact sequence planning with whole-body trajectory generation for humanoid loco-manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "093a8d6a-8aea-4c06-8d13-8941e89dc55f",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "7b9b99bf-b776-419b-af6d-ccbc258f09b8",
  "toolUseResult": {
    "query": "humanoid whole-body trajectory generation contact sequence planning manipulation walking 2025 2026 arxiv method",
    "results": [
      {
        "tool_use_id": "srvtoolu_015vcAFwxdqAD7sVgfEWRqBM",
        "content": [
          {
            "title": "Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors",
            "url": "https://arxiv.org/html/2501.02116v1"
          },
          {
            "title": "Task and Motion Planning for Humanoid Loco-manipulation",
            "url": "https://arxiv.org/html/2508.14099"
          },
          {
            "title": "WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts",
            "url": "https://arxiv.org/html/2406.06005v1"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "One-shot Humanoid Whole-body Motion Learning",
            "url": "https://arxiv.org/html/2510.25241v1"
          },
          {
            "title": "TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality",
            "url": "https://arxiv.org/html/2506.15146v1"
          },
          {
            "title": "Humanoid Loco-Manipulations Pattern Generation and Stabilization Control",
            "url": "https://arxiv.org/html/2505.24116"
          },
          {
            "title": "Natural Humanoid Robot Locomotion with Generative Motion Prior",
            "url": "https://arxiv.org/html/2503.09015v1"
          },
          {
            "title": "Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations",
            "url": "https://arxiv.org/html/2602.06643v2"
          },
          {
            "title": "[2509.11839] TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning",
            "url": "https://arxiv.org/abs/2509.11839"
          }
        ]
      },
      "I found several relevant arxiv papers from 2025-2026 on humanoid whole-body trajectory generation, contact sequence planning, and loco-manipulation. Here are the key results:\n\n## Recent Methods (2025-2026)\n\n**1. Humanoid Locomotion and Manipulation Survey** (January 2025)\nThis work addresses humanoid whole-body loco-manipulation planning, where planners must solve trajectories that handle rich interactions with environments or objects, requiring decisions about contact position, contact mode, and contact force. Model Predictive Control (MPC) is highlighted as one of the most popular approaches to trajectory planning for locomotion and manipulation due to its flexibility to define versatile motion objectives and availability of solvers.\n\n**2. Task and Motion Planning for Humanoid Loco-manipulation** (August 2025)\nThis work presents an optimization-based task and motion planning framework that unifies planning for locomotion and manipulation through a shared representation of contact modes, with symbolic actions defined as contact mode changes. This is the first work enabling integrated TAMP formulation with fully acyclic planning and whole body dynamics with actuation constraints for humanoid loco-manipulation.\n\n**3. WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts** (June 2024)\nThis framework enables end-to-end RL-based controllers for four challenging whole-body humanoid tasks involving diverse contact sequences: parkour jumping, box loco-manipulation, dynamic dancing, and cliffside climbing.\n\n**4. TACT: Humanoid Whole-body Contact Manipulation** (June 2025)\nThis work leverages LIPM-based biped control to enable the robot to maintain balance and continue walking while its upper body is governed by a learned policy for contact manipulation.\n\n**5. Humanoid Loco-Manipulations Pattern Generation and Stabilization Control** (May 2025)\nThe method derives bipedal dynamics accounting for external manipulation forces, proposing a pattern generator to plan center of mass trajectories consistent with manipulation force references and a stabilizer to compensate for force tracking errors.\n\nThese papers represent the state-of-the-art in combining contact sequence planning with whole-body trajectory generation for humanoid loco-manipulation tasks."
    ],
    "durationSeconds": 8.962639232999994
  },
  "sourceToolAssistantUUID": "093a8d6a-8aea-4c06-8d13-8941e89dc55f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-10T17:17:11.054Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P8SQwuUq7juMt6cVQj33kR`</summary>

```json
{
  "query": "embodiment-aware generative model robot morphology conditioned diffusion policy data 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b9b99bf-b776-419b-af6d-ccbc258f09b8",
  "isSidechain": false,
  "requestId": "req_011CauGVKG6e7Nsb3j5FGgUH",
  "type": "assistant",
  "uuid": "f237cad7-7f0f-4e4c-a99c-d28c40477ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMRBcChtUSbbwoNoxxq3iA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 61467,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 61467,
          "cache_creation_input_tokens": 1077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1077
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

_source line 123 · 2026-05-10T17:17:19.097Z_

<details><summary>↩ Tool result · `toolu_01P8SQwuUq7juMt6cVQj33kR`</summary>

```text
Web search results for query: "embodiment-aware generative model robot morphology conditioned diffusion policy data 2025 2026"

Links: [{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"},{"title":"Large Model Empowered Embodied AI: A Survey on Decision-Making and Embodied Learning","url":"https://arxiv.org/html/2508.10399v1"},{"title":"A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-025-1542-8"},{"title":"Embodied World Models for Decision Making","url":"https://embodied-world-models.github.io/"}]

Based on the web search results, here's what I found regarding embodiment-aware generative models, robot morphology, conditioned diffusion policies, and related data from 2025-2026:

## Key Findings

**Recent Diffusion Policy Advances:**

Vision-Language-Action (VLA) models are being combined with diffusion-based policies to increase precision and adaptability to different robot embodiments. For example, TinyVLA (Wen et al., 2025) incorporates a diffusion-based head module on top of a pretrained VLA to directly generate robotic actions.

**Embodiment-Specific Research:**

Recent work includes "Accelerated co-design of robots through morphological pretraining" and "Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies", which represent advances in handling different robot morphologies.

**Morphological Diversity and Generalization:**

Research on cross-embodiment learning (such as GROQLoco by Narayanan et al., 2025) demonstrates that developing a single, generalist locomotion policy capable of handling various quadrupedal robots across diverse terrains is achievable by training on expert demonstrations that include both terrain types and leveraging data gathered from several quadrupeds to encompass a wide range of gaits and morphological diversity, with the central argument being that enhancing diversity in both robot body types and locomotion behaviors is essential for achieving robust generalization.

**Generative Simulation for Data:**

DreamGen applies video diffusion models to generate robot manipulation demonstrations conditioned on language descriptions, enabling data augmentation without additional physical robot time.

These recent developments (2025-2026) show significant progress in embodiment-aware generative models that can adapt to different robot morphologies through conditioned diffusion policies and large-scale synthetic data generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f237cad7-7f0f-4e4c-a99c-d28c40477ed5",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "25cd49a7-87b0-44d1-aa21-604c9efc1bd7",
  "toolUseResult": {
    "query": "embodiment-aware generative model robot morphology conditioned diffusion policy data 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017WjnWWYW3BogyENQ6J4jqz",
        "content": [
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "Frontiers | Diffusion models for robotic manipulation: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"
          },
          {
            "title": "Generative AI in Industrial Robotics: 2026 Layers Guide",
            "url": "https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"
          },
          {
            "title": "GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more",
            "url": "https://github.com/smallfryy/corl-2025-papers"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          },
          {
            "title": "TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"
          },
          {
            "title": "Large Model Empowered Embodied AI: A Survey on Decision-Making and Embodied Learning",
            "url": "https://arxiv.org/html/2508.10399v1"
          },
          {
            "title": "A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11633-025-1542-8"
          },
          {
            "title": "Embodied World Models for Decision Making",
            "url": "https://embodied-world-models.github.io/"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding embodiment-aware generative models, robot morphology, conditioned diffusion policies, and related data from 2025-2026:\n\n## Key Findings\n\n**Recent Diffusion Policy Advances:**\n\nVision-Language-Action (VLA) models are being combined with diffusion-based policies to increase precision and adaptability to different robot embodiments. For example, TinyVLA (Wen et al., 2025) incorporates a diffusion-based head module on top of a pretrained VLA to directly generate robotic actions.\n\n**Embodiment-Specific Research:**\n\nRecent work includes \"Accelerated co-design of robots through morphological pretraining\" and \"Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies\", which represent advances in handling different robot morphologies.\n\n**Morphological Diversity and Generalization:**\n\nResearch on cross-embodiment learning (such as GROQLoco by Narayanan et al., 2025) demonstrates that developing a single, generalist locomotion policy capable of handling various quadrupedal robots across diverse terrains is achievable by training on expert demonstrations that include both terrain types and leveraging data gathered from several quadrupeds to encompass a wide range of gaits and morphological diversity, with the central argument being that enhancing diversity in both robot body types and locomotion behaviors is essential for achieving robust generalization.\n\n**Generative Simulation for Data:**\n\nDreamGen applies video diffusion models to generate robot manipulation demonstrations conditioned on language descriptions, enabling data augmentation without additional physical robot time.\n\nThese recent developments (2025-2026) show significant progress in embodiment-aware generative models that can adapt to different robot morphologies through conditioned diffusion policies and large-scale synthetic data generation."
    ],
    "durationSeconds": 8.038521141999983
  },
  "sourceToolAssistantUUID": "f237cad7-7f0f-4e4c-a99c-d28c40477ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 124_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "25cd49a7-87b0-44d1-aa21-604c9efc1bd7",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Assistant

_source line 126 · 2026-05-10T17:17:23.774Z_

Now let me do targeted "anti-searches" to check if the gaps I'm identifying are real.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25cd49a7-87b0-44d1-aa21-604c9efc1bd7",
  "isSidechain": false,
  "requestId": "req_011CauGWBv75Lef9vZFqDDoD",
  "type": "assistant",
  "uuid": "05a35af5-d5fb-4d70-af63-a9da65d86dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVLusTAu4BuXexdMLiugdx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 62544,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 62544,
          "cache_creation_input_tokens": 1155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1155
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

_source line 127 · 2026-05-10T17:17:24.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PVzBVecDa2SiXD4ZrFGnTg`</summary>

```json
{
  "query": "humanoid kinematic tree structured diffusion action trajectory generation joint coupling constraint 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05a35af5-d5fb-4d70-af63-a9da65d86dc6",
  "isSidechain": false,
  "requestId": "req_011CauGWBv75Lef9vZFqDDoD",
  "type": "assistant",
  "uuid": "d48d7ec5-b94f-4614-893a-f8fe01f36acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVLusTAu4BuXexdMLiugdx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 62544,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 62544,
          "cache_creation_input_tokens": 1155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1155
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

_source line 128 · 2026-05-10T17:17:32.508Z_

<details><summary>↩ Tool result · `toolu_01PVzBVecDa2SiXD4ZrFGnTg`</summary>

```text
Web search results for query: "humanoid kinematic tree structured diffusion action trajectory generation joint coupling constraint 2025 2026"

Links: [{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Robot Motion Diffusion Model: Motion Generation for Robotic Characters | SIGGRAPH Asia 2024 Conference Papers","url":"https://dl.acm.org/doi/10.1145/3680528.3687626"},{"title":"Optimizing Diffusion Models for Joint Trajectory Prediction ...","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04239-supp.pdf"},{"title":"HUMANOID-LLA: OPEN-VOCABULARY ...","url":"https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"},{"title":"Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning","url":"https://arxiv.org/html/2603.19078v1"},{"title":"Research on humanoid robot motion generation and real-time trajectory optimization based on sparse attention mechanism in deep reinforcement learning | Discover Artificial Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44163-025-00603-3"},{"title":"GT-TD3: A Kinematics-Aware Graph-Transformer Framework for Stable Trajectory Tracking of High-Degree-of-Freedom (DOF) Manipulators","url":"https://www.mdpi.com/2075-1702/14/4/397"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"ControlTraj: Controllable Trajectory Generation with Topology-Constrained Diffusion Model","url":"https://arxiv.org/html/2404.15380v1"}]

I found relevant research on this specialized topic. Here are the key findings from the search results:

## Recent Work on Kinematic Tree Structured Diffusion for Humanoid Control

The Robot Motion Diffusion Model (RobotMDM) is a text-conditioned kinematic diffusion model that interfaces with a reinforcement learning-based tracking controller. This approach integrates kinematic generative models with physics-based character control.

### Kinematic Constraints and Coupling in Robot Learning

Accurate trajectory tracking of redundant manipulators is difficult because the controller must simultaneously model local couplings between adjacent joints and global dependencies across the whole kinematic chain, and existing reinforcement learning methods typically employ multilayer perceptrons which do not explicitly exploit manipulator structure.

A Graph Transformer approach extracts local kinematic coupling information using a graph neural network, while the Transformer, augmented with a kinematic-aware attention bias, models global joint dependencies.

### Kinematic Tree Structures for Robot Representation

To implement structured approaches, robots are represented as a kinematic tree extracted from URDF or MJCF model files, parsing parent-child relationships between links while excluding sensor-related components to focus on the physical structure relevant to control.

### Recent Diffusion-Based Approaches

Recent 2025-2026 research includes Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation (CVPR 2025) and various constraint-aware diffusion methods for trajectory generation that explicitly model joint coupling and kinematic constraints.

These works demonstrate an active research direction combining diffusion models with kinematic tree structures for improved trajectory generation in humanoid robots.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d48d7ec5-b94f-4614-893a-f8fe01f36acc",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "1a3257de-c1a9-4990-b35b-b2a155c6a6f1",
  "toolUseResult": {
    "query": "humanoid kinematic tree structured diffusion action trajectory generation joint coupling constraint 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012VDLmWVBdf1VcYiAEQAjht",
        "content": [
          {
            "title": "Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors",
            "url": "https://arxiv.org/html/2501.02116v1"
          },
          {
            "title": "Robot Motion Diffusion Model: Motion Generation for Robotic Characters | SIGGRAPH Asia 2024 Conference Papers",
            "url": "https://dl.acm.org/doi/10.1145/3680528.3687626"
          },
          {
            "title": "Optimizing Diffusion Models for Joint Trajectory Prediction ...",
            "url": "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04239-supp.pdf"
          },
          {
            "title": "HUMANOID-LLA: OPEN-VOCABULARY ...",
            "url": "https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"
          },
          {
            "title": "Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning",
            "url": "https://arxiv.org/html/2603.19078v1"
          },
          {
            "title": "Research on humanoid robot motion generation and real-time trajectory optimization based on sparse attention mechanism in deep reinforcement learning | Discover Artificial Intelligence | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s44163-025-00603-3"
          },
          {
            "title": "GT-TD3: A Kinematics-Aware Graph-Transformer Framework for Stable Trajectory Tracking of High-Degree-of-Freedom (DOF) Manipulators",
            "url": "https://www.mdpi.com/2075-1702/14/4/397"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "ControlTraj: Controllable Trajectory Generation with Topology-Constrained Diffusion Model",
            "url": "https://arxiv.org/html/2404.15380v1"
          }
        ]
      },
      "I found relevant research on this specialized topic. Here are the key findings from the search results:\n\n## Recent Work on Kinematic Tree Structured Diffusion for Humanoid Control\n\nThe Robot Motion Diffusion Model (RobotMDM) is a text-conditioned kinematic diffusion model that interfaces with a reinforcement learning-based tracking controller. This approach integrates kinematic generative models with physics-based character control.\n\n### Kinematic Constraints and Coupling in Robot Learning\n\nAccurate trajectory tracking of redundant manipulators is difficult because the controller must simultaneously model local couplings between adjacent joints and global dependencies across the whole kinematic chain, and existing reinforcement learning methods typically employ multilayer perceptrons which do not explicitly exploit manipulator structure.\n\nA Graph Transformer approach extracts local kinematic coupling information using a graph neural network, while the Transformer, augmented with a kinematic-aware attention bias, models global joint dependencies.\n\n### Kinematic Tree Structures for Robot Representation\n\nTo implement structured approaches, robots are represented as a kinematic tree extracted from URDF or MJCF model files, parsing parent-child relationships between links while excluding sensor-related components to focus on the physical structure relevant to control.\n\n### Recent Diffusion-Based Approaches\n\nRecent 2025-2026 research includes Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation (CVPR 2025) and various constraint-aware diffusion methods for trajectory generation that explicitly model joint coupling and kinematic constraints.\n\nThese works demonstrate an active research direction combining diffusion models with kinematic tree structures for improved trajectory generation in humanoid robots."
    ],
    "durationSeconds": 7.958370187000022
  },
  "sourceToolAssistantUUID": "d48d7ec5-b94f-4614-893a-f8fe01f36acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 129 · 2026-05-10T17:17:32.512Z_

```json
{
  "parentUuid": "1a3257de-c1a9-4990-b35b-b2a155c6a6f1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b4107fe4-e394-4b45-ae1b-e4be58d08f06",
  "timestamp": "2026-05-10T17:17:32.512Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 130 · 2026-05-10T17:17:35.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011btNBn8Jj2B7zLSwL68ytN`</summary>

```json
{
  "query": "Articulated-Body Dynamics Network dynamics-grounded prior robot learning 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4107fe4-e394-4b45-ae1b-e4be58d08f06",
  "isSidechain": false,
  "requestId": "req_011CauGXBEwxYPNvuMYczvPq",
  "type": "assistant",
  "uuid": "ed4eb9a5-c63c-4f6e-8190-67d278eed701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7wudaEPbSAWwbmjdKDmYX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 63699,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 63699,
          "cache_creation_input_tokens": 1242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1242
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

_source line 131 · 2026-05-10T17:17:41.676Z_

<details><summary>↩ Tool result · `toolu_011btNBn8Jj2B7zLSwL68ytN`</summary>

```text
Web search results for query: "Articulated-Body Dynamics Network dynamics-grounded prior robot learning 2026 arxiv"

Links: [{"title":"Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning","url":"https://arxiv.org/html/2603.19078v1"},{"title":"Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning | Legged AI Lab 熊晓滨课题组","url":"https://www.leggedai.com/publication/2026_submission1/"},{"title":"Neural Robot Dynamics","url":"https://arxiv.org/html/2508.15755v1"},{"title":"Pseudo-rigid body networks: learning interpretable deformable object dynamics from partial observations","url":"https://arxiv.org/html/2307.07975"},{"title":"Fast Articulated Body Dynamics Simulation using Optimization Integrator","url":"https://arxiv.org/pdf/1709.04145v2"},{"title":"[2508.15755] Neural Robot Dynamics","url":"https://arxiv.org/abs/2508.15755"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"Contact-Aware Neural Dynamics","url":"https://arxiv.org/html/2601.12796v1"},{"title":"Simultaneous Learning of Contact and Continuous Dynamics","url":"https://arxiv.org/html/2310.12054"},{"title":"[2209.11588] Learning Articulated Rigid Body Dynamics with Lagrangian Graph Neural Network","url":"https://arxiv.org/abs/2209.11588"}]

Based on the search results, I found the paper you're looking for:

## Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning

ABD-Net is a graph neural network architecture that embeds the computational structure of forward dynamics into the policy actor for articulated robot control.

**Key Contributions:**

The architecture adapts the inertia propagation mechanism from the Articulated Body Algorithm, systematically aggregating inertial quantities from child to parent links in a tree-structured manner, while replacing physical quantities with learnable parameters.

**Performance:**

ABD-Net achieves increased sample efficiency, robustness under dynamics shifts, and computational efficiency across diverse morphologies and tasks, outperforming transformer-based and GNN baselines. Additionally, the learned policy was validated through sim-to-real transfer on real Unitree Go2 and G1 robots, confirming compatibility with standard deployment pipelines and real-time onboard inference.

The paper was published on arXiv on March 19, 2026, with the identifier 2603.19078.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed4eb9a5-c63c-4f6e-8190-67d278eed701",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "cf4b46f4-9f64-42d9-a298-4c5f347e494f",
  "toolUseResult": {
    "query": "Articulated-Body Dynamics Network dynamics-grounded prior robot learning 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FeDntP8997NRfh6yMGMRjc",
        "content": [
          {
            "title": "Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning",
            "url": "https://arxiv.org/html/2603.19078v1"
          },
          {
            "title": "Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning | Legged AI Lab 熊晓滨课题组",
            "url": "https://www.leggedai.com/publication/2026_submission1/"
          },
          {
            "title": "Neural Robot Dynamics",
            "url": "https://arxiv.org/html/2508.15755v1"
          },
          {
            "title": "Pseudo-rigid body networks: learning interpretable deformable object dynamics from partial observations",
            "url": "https://arxiv.org/html/2307.07975"
          },
          {
            "title": "Fast Articulated Body Dynamics Simulation using Optimization Integrator",
            "url": "https://arxiv.org/pdf/1709.04145v2"
          },
          {
            "title": "[2508.15755] Neural Robot Dynamics",
            "url": "https://arxiv.org/abs/2508.15755"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.16391"
          },
          {
            "title": "Contact-Aware Neural Dynamics",
            "url": "https://arxiv.org/html/2601.12796v1"
          },
          {
            "title": "Simultaneous Learning of Contact and Continuous Dynamics",
            "url": "https://arxiv.org/html/2310.12054"
          },
          {
            "title": "[2209.11588] Learning Articulated Rigid Body Dynamics with Lagrangian Graph Neural Network",
            "url": "https://arxiv.org/abs/2209.11588"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning\n\nABD-Net is a graph neural network architecture that embeds the computational structure of forward dynamics into the policy actor for articulated robot control.\n\n**Key Contributions:**\n\nThe architecture adapts the inertia propagation mechanism from the Articulated Body Algorithm, systematically aggregating inertial quantities from child to parent links in a tree-structured manner, while replacing physical quantities with learnable parameters.\n\n**Performance:**\n\nABD-Net achieves increased sample efficiency, robustness under dynamics shifts, and computational efficiency across diverse morphologies and tasks, outperforming transformer-based and GNN baselines. Additionally, the learned policy was validated through sim-to-real transfer on real Unitree Go2 and G1 robots, confirming compatibility with standard deployment pipelines and real-time onboard inference.\n\nThe paper was published on arXiv on March 19, 2026, with the identifier 2603.19078."
    ],
    "durationSeconds": 5.711093647999922
  },
  "sourceToolAssistantUUID": "ed4eb9a5-c63c-4f6e-8190-67d278eed701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-10T17:17:44.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QD8kS6T9gF7s67xwxVbr9r`</summary>

```json
{
  "query": "Isaac Lab humanoid G1 H1 manipulation loco-manipulation environment suite tasks 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf4b46f4-9f64-42d9-a298-4c5f347e494f",
  "isSidechain": false,
  "requestId": "req_011CauGXrR9K5T6hK3oaEYdE",
  "type": "assistant",
  "uuid": "834a805e-d8fa-4842-b12e-2d24566ae44e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmN2zw4jSBBEhBqaNLBr1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 64941,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 64941,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 133 · 2026-05-10T17:17:54.810Z_

<details><summary>↩ Tool result · `toolu_01QD8kS6T9gF7s67xwxVbr9r`</summary>

```text
Web search results for query: "Isaac Lab humanoid G1 H1 manipulation loco-manipulation environment suite tasks 2025 2026"

Links: [{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/html/2511.04831v1"},{"title":"Releases · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/releases"},{"title":"Available Environments — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html"},{"title":"Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/"},{"title":"Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"},{"title":"Release Notes — Isaac Lab Documentation","url":"https://docs.robotsfan.com/isaaclab_official/main/source/refs/release_notes.html"},{"title":"Modifying an existing Direct RL Environment — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/modify_direct_rl_env.html"},{"title":"Reinforcement Learning Policies Examples in Isaac Sim — Isaac Sim Documentation","url":"https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_policy_example.html"},{"title":"[Question] Deploying trained humanoid policy in Isaac Sim · Issue #2437 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2437"}]

Based on the web search results, here's what I found about Isaac Lab's humanoid G1 and H1 manipulation and loco-manipulation environments:

## Locomotion Support

Isaac Lab includes locomotion support for multiple robot morphologies including A1, G1, H1, Go1/2, Anymal-B/C/D, Cassie, Digit, and Spot. This implementation has shown robust sim-to-real transfer for Anymal and Spot.

## Loco-Manipulation Environments

Isaac Lab added a new G1 humanoid environment combining RL-based locomotion with IK-based manipulation, with a full robot navigation stack integrated to augment demonstrations with randomization of tabletop pick/place locations, destination and ground obstacles. By segmenting tasks into pick-navigate-place phases, this method enables generation of large-scale loco-manipulation datasets from manipulation-only demonstrations.

A demonstration shows how to train a G1 robot to perform pick and place tasks with full-body locomotion and manipulation using the Isaac-PickPlace-Locomanipulation-G1-Abs-v0 task environment.

## Manipulation Suites

Isaac Lab's manipulation suite includes dexterous hand-arm tasks such as reorientation and grasping, alongside contact-rich assembly benchmarks that leverage SDF-based contact modeling and force-aware strategies, covering both single-object dexterity and multi-part assembly, with options for tactile/force sensing.

A new DexSuite was added, including dexterous Lift and Reorient environments following DextrAH and DexPBT.

## H1 Support

An interactive demo script for H1 locomotion was added. Additionally, the H1 Flat Terrain Policy was trained in Isaac Lab to control the humanoid's locomotion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "834a805e-d8fa-4842-b12e-2d24566ae44e",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "09322c80-4ee7-4ae1-b8fd-d95c4c665a88",
  "toolUseResult": {
    "query": "Isaac Lab humanoid G1 H1 manipulation loco-manipulation environment suite tasks 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Yjke3jUPu6tZBGKUhen5e",
        "content": [
          {
            "title": "Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"
          },
          {
            "title": "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning",
            "url": "https://arxiv.org/html/2511.04831v1"
          },
          {
            "title": "Releases · isaac-sim/IsaacLab",
            "url": "https://github.com/isaac-sim/IsaacLab/releases"
          },
          {
            "title": "Available Environments — Isaac Lab Documentation",
            "url": "https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html"
          },
          {
            "title": "Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3 | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/"
          },
          {
            "title": "Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation",
            "url": "https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"
          },
          {
            "title": "Release Notes — Isaac Lab Documentation",
            "url": "https://docs.robotsfan.com/isaaclab_official/main/source/refs/release_notes.html"
          },
          {
            "title": "Modifying an existing Direct RL Environment — Isaac Lab Documentation",
            "url": "https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/modify_direct_rl_env.html"
          },
          {
            "title": "Reinforcement Learning Policies Examples in Isaac Sim — Isaac Sim Documentation",
            "url": "https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/ext_isaacsim_robot_policy_example.html"
          },
          {
            "title": "[Question] Deploying trained humanoid policy in Isaac Sim · Issue #2437 · isaac-sim/IsaacLab",
            "url": "https://github.com/isaac-sim/IsaacLab/issues/2437"
          }
        ]
      },
      "Based on the web search results, here's what I found about Isaac Lab's humanoid G1 and H1 manipulation and loco-manipulation environments:\n\n## Locomotion Support\n\nIsaac Lab includes locomotion support for multiple robot morphologies including A1, G1, H1, Go1/2, Anymal-B/C/D, Cassie, Digit, and Spot. This implementation has shown robust sim-to-real transfer for Anymal and Spot.\n\n## Loco-Manipulation Environments\n\nIsaac Lab added a new G1 humanoid environment combining RL-based locomotion with IK-based manipulation, with a full robot navigation stack integrated to augment demonstrations with randomization of tabletop pick/place locations, destination and ground obstacles. By segmenting tasks into pick-navigate-place phases, this method enables generation of large-scale loco-manipulation datasets from manipulation-only demonstrations.\n\nA demonstration shows how to train a G1 robot to perform pick and place tasks with full-body locomotion and manipulation using the Isaac-PickPlace-Locomanipulation-G1-Abs-v0 task environment.\n\n## Manipulation Suites\n\nIsaac Lab's manipulation suite includes dexterous hand-arm tasks such as reorientation and grasping, alongside contact-rich assembly benchmarks that leverage SDF-based contact modeling and force-aware strategies, covering both single-object dexterity and multi-part assembly, with options for tactile/force sensing.\n\nA new DexSuite was added, including dexterous Lift and Reorient environments following DextrAH and DexPBT.\n\n## H1 Support\n\nAn interactive demo script for H1 locomotion was added. Additionally, the H1 Flat Terrain Policy was trained in Isaac Lab to control the humanoid's locomotion."
    ],
    "durationSeconds": 10.289689170000027
  },
  "sourceToolAssistantUUID": "834a805e-d8fa-4842-b12e-2d24566ae44e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 134 · 2026-05-10T17:17:57.427Z_

Now I have a comprehensive landscape picture. Let me do a few more targeted searches to firm up my remaining idea candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09322c80-4ee7-4ae1-b8fd-d95c4c665a88",
  "isSidechain": false,
  "requestId": "req_011CauGYpbnWwiuutAK7XYPe",
  "type": "assistant",
  "uuid": "df5ccdd1-9073-4a62-8608-6a13f5aab7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nVHmmnFYGNASrJZjYN6H9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 65698,
      "output_tokens": 99,
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
          "output_tokens": 99,
          "cache_read_input_tokens": 65698,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 135 · 2026-05-10T17:17:58.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1wgkkhy9Ka8JvgXLFnvku`</summary>

```json
{
  "query": "\"compositional trajectory generation\" humanoid loco-manipulation skill primitive stitching 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df5ccdd1-9073-4a62-8608-6a13f5aab7a2",
  "isSidechain": false,
  "requestId": "req_011CauGYpbnWwiuutAK7XYPe",
  "type": "assistant",
  "uuid": "1f26cc01-2aa3-4f7a-b438-0df28f1e41f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nVHmmnFYGNASrJZjYN6H9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 65698,
      "output_tokens": 99,
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
          "output_tokens": 99,
          "cache_read_input_tokens": 65698,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1121
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

_source line 136 · 2026-05-10T17:18:06.234Z_

<details><summary>↩ Tool result · `toolu_01T1wgkkhy9Ka8JvgXLFnvku`</summary>

```text
Web search results for query: ""compositional trajectory generation" humanoid loco-manipulation skill primitive stitching 2025 2026"

Links: [{"title":"Generative Trajectory Stitching through Diffusion Composition","url":"https://arxiv.org/html/2503.05153v1"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/html/2506.09366v1"},{"title":"[2506.09366] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/abs/2506.09366"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending | Request PDF","url":"https://www.researchgate.net/publication/392597734_SkillBlender_Towards_Versatile_Humanoid_Whole-Body_Loco-Manipulation_via_Skill_Blending"},{"title":"Paper page - SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://huggingface.co/papers/2506.09366"},{"title":"Generative Trajectory Stitching through Diffusion Composition | OpenReview","url":"https://openreview.net/forum?id=VCTt5DXiBe"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Humanoid Loco-Manipulations Pattern Generation and Stabilization Control","url":"https://arxiv.org/html/2505.24116"}]

I found several relevant papers on compositional trajectory generation, humanoid loco-manipulation, and skill primitive stitching from 2025-2026:

## Key Findings:

**1. CompDiffuser - Generative Trajectory Stitching through Diffusion Composition**

CompDiffuser is a novel generative approach that can solve new tasks by learning to compositionally stitch together shorter trajectory chunks from previously seen tasks. The key insight is modeling the trajectory distribution by subdividing it into overlapping chunks and learning their conditional relationships through a single bidirectional diffusion model, which allows information to propagate between segments during generation, ensuring physically consistent connections. This paper was published in March 2025.

**2. SkillBlender - Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending**

SkillBlender is a novel Hierarchical Reinforcement Learning (HRL) framework for versatile humanoid whole-body loco-manipulation, where the system first pretrains a set of goal-conditioned primitive skills that are task-agnostic, reusable, and physically interpretable, and a high-level controller then learns to synthesize subgoals and per-joint weight vectors to blend these low-level skills. This paper was published in June 2025.

**3. Related Works**

Additional recent papers include a framework that first trains a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions, while concurrently training a whole-body reference tracker with RL, and OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f26cc01-2aa3-4f7a-b438-0df28f1e41f9",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "6d268cf4-780a-4d69-b8eb-eaaf73a90d34",
  "toolUseResult": {
    "query": "\"compositional trajectory generation\" humanoid loco-manipulation skill primitive stitching 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BNrGaSSb9jeq6pYXjZbg7U",
        "content": [
          {
            "title": "Generative Trajectory Stitching through Diffusion Composition",
            "url": "https://arxiv.org/html/2503.05153v1"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://arxiv.org/html/2506.09366v1"
          },
          {
            "title": "[2506.09366] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://arxiv.org/abs/2506.09366"
          },
          {
            "title": "Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking",
            "url": "https://arxiv.org/html/2604.17335"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending | Request PDF",
            "url": "https://www.researchgate.net/publication/392597734_SkillBlender_Towards_Versatile_Humanoid_Whole-Body_Loco-Manipulation_via_Skill_Blending"
          },
          {
            "title": "Paper page - SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://huggingface.co/papers/2506.09366"
          },
          {
            "title": "Generative Trajectory Stitching through Diffusion Composition | OpenReview",
            "url": "https://openreview.net/forum?id=VCTt5DXiBe"
          },
          {
            "title": "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://arxiv.org/html/2509.26633v2"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Humanoid Loco-Manipulations Pattern Generation and Stabilization Control",
            "url": "https://arxiv.org/html/2505.24116"
          }
        ]
      },
      "I found several relevant papers on compositional trajectory generation, humanoid loco-manipulation, and skill primitive stitching from 2025-2026:\n\n## Key Findings:\n\n**1. CompDiffuser - Generative Trajectory Stitching through Diffusion Composition**\n\nCompDiffuser is a novel generative approach that can solve new tasks by learning to compositionally stitch together shorter trajectory chunks from previously seen tasks. The key insight is modeling the trajectory distribution by subdividing it into overlapping chunks and learning their conditional relationships through a single bidirectional diffusion model, which allows information to propagate between segments during generation, ensuring physically consistent connections. This paper was published in March 2025.\n\n**2. SkillBlender - Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending**\n\nSkillBlender is a novel Hierarchical Reinforcement Learning (HRL) framework for versatile humanoid whole-body loco-manipulation, where the system first pretrains a set of goal-conditioned primitive skills that are task-agnostic, reusable, and physically interpretable, and a high-level controller then learns to synthesize subgoals and per-joint weight vectors to blend these low-level skills. This paper was published in June 2025.\n\n**3. Related Works**\n\nAdditional recent papers include a framework that first trains a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions, while concurrently training a whole-body reference tracker with RL, and OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves crucial spatial and contact relationships between an agent, the terrain, and manipulated objects."
    ],
    "durationSeconds": 7.90716815199994
  },
  "sourceToolAssistantUUID": "1f26cc01-2aa3-4f7a-b438-0df28f1e41f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 137_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "6d268cf4-780a-4d69-b8eb-eaaf73a90d34",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 138_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 139 · 2026-05-10T17:18:09.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ZeXKbKcE81GvtU8YxpQer`</summary>

```json
{
  "query": "generative world model humanoid-specific architecture body structure dynamics awareness data generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d268cf4-780a-4d69-b8eb-eaaf73a90d34",
  "isSidechain": false,
  "requestId": "req_011CauGZfQupqGND2ckVwBEL",
  "type": "assistant",
  "uuid": "f70e43e8-dcb1-4285-bcd1-96c8b9198a85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wc6QUYeGFVHwQEnpPEkSGu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1094,
      "cache_read_input_tokens": 66819,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1094,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 66819,
          "cache_creation_input_tokens": 1094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1094
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

_source line 140 · 2026-05-10T17:18:16.792Z_

<details><summary>↩ Tool result · `toolu_013ZeXKbKcE81GvtU8YxpQer`</summary>

```text
Web search results for query: "generative world model humanoid-specific architecture body structure dynamics awareness data generation 2026"

Links: [{"title":"Hierarchical World Models as Visual Whole-Body Humanoid Controllers","url":"https://arxiv.org/html/2405.18418v1"},{"title":"Humanoid World Models : Open World Foundation Models for Humanoid Robotics","url":"https://arxiv.org/html/2506.01182"},{"title":"A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots","url":"https://arxiv.org/html/2506.20487v3"},{"title":"[2506.01182] Humanoid World Models: Open World Foundation Models for Humanoid Robotics","url":"https://arxiv.org/abs/2506.01182"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GS-World: An Efficient, Engine-driven Learning Paradigm for ...","url":"https://www.techrxiv.org/users/980915/articles/1347086/master/file/data/GS-World%20An%20Efficient,%20Engine-driven%20Learning%20Paradigm%20for%20Pursuing%20Embodied%20Intelligence%20using%20World%20Models%20of%20Generative%20Simulation/GS-World%20An%20Efficient,%20Engine-driven%20Learning%20Paradigm%20for%20Pursuing%20Embodied%20Intelligence%20using%20World%20Models%20of%20Generative%20Simulation.pdf"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"[2405.18418] Hierarchical World Models as Visual Whole-Body Humanoid Controllers","url":"https://arxiv.org/abs/2405.18418"},{"title":"DualWorld: Dual-System World Models","url":"https://world-mind.github.io/DualWorld/"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"}]

Based on the web search results, here's what I found about generative world models with humanoid-specific architecture:

## Humanoid World Models Overview

Humanoid World Models (HWM) are a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. Two types of generative models are trained—Masked Transformers and Flow-Matching—on 100 hours of humanoid demonstrations.

## Humanoid-Specific Architecture

Architectural variants with different attention mechanisms and parameter-sharing strategies are explored, with parameter-sharing techniques reducing model size by 33-53% with minimal impact on performance or visual fidelity.

## Body Structure and Dynamics Awareness

A hierarchical world model approach uses a high-level agent that generates commands based on visual observations for a low-level agent to execute, both trained with rewards. This dual-system design enables humanoid robots to execute complex whole-body movements with both long-horizon coherence and immediate reactivity.

## Data Generation and Applications

World models predict the future outcome of a given action, supporting capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. BFMs serve as a pivotal bridge between high-level semantic instructions and low-level physical execution, leveraging pre-trained behavioral priors to enable zero-shot adaptation, multi-task generalization, and physics-aware motion synthesis.

The field has rapidly advanced in 2025-2026, with recent work focusing on integrating multiple data sources, improving efficiency through parameter sharing, and enabling complex whole-body coordination for humanoid robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f70e43e8-dcb1-4285-bcd1-96c8b9198a85",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "b07307b1-60b1-4a3f-9847-14f6a5ef1df7",
  "toolUseResult": {
    "query": "generative world model humanoid-specific architecture body structure dynamics awareness data generation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016GagEw49mfHfB5oWa9uQry",
        "content": [
          {
            "title": "Hierarchical World Models as Visual Whole-Body Humanoid Controllers",
            "url": "https://arxiv.org/html/2405.18418v1"
          },
          {
            "title": "Humanoid World Models : Open World Foundation Models for Humanoid Robotics",
            "url": "https://arxiv.org/html/2506.01182"
          },
          {
            "title": "A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots",
            "url": "https://arxiv.org/html/2506.20487v3"
          },
          {
            "title": "[2506.01182] Humanoid World Models: Open World Foundation Models for Humanoid Robotics",
            "url": "https://arxiv.org/abs/2506.01182"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "GS-World: An Efficient, Engine-driven Learning Paradigm for ...",
            "url": "https://www.techrxiv.org/users/980915/articles/1347086/master/file/data/GS-World%20An%20Efficient,%20Engine-driven%20Learning%20Paradigm%20for%20Pursuing%20Embodied%20Intelligence%20using%20World%20Models%20of%20Generative%20Simulation/GS-World%20An%20Efficient,%20Engine-driven%20Learning%20Paradigm%20for%20Pursuing%20Embodied%20Intelligence%20using%20World%20Models%20of%20Generative%20Simulation.pdf"
          },
          {
            "title": "2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/pdf/2503.14734"
          },
          {
            "title": "[2405.18418] Hierarchical World Models as Visual Whole-Body Humanoid Controllers",
            "url": "https://arxiv.org/abs/2405.18418"
          },
          {
            "title": "DualWorld: Dual-System World Models",
            "url": "https://world-mind.github.io/DualWorld/"
          },
          {
            "title": "GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub",
            "url": "https://github.com/leofan90/Awesome-World-Models"
          }
        ]
      },
      "Based on the web search results, here's what I found about generative world models with humanoid-specific architecture:\n\n## Humanoid World Models Overview\n\nHumanoid World Models (HWM) are a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. Two types of generative models are trained—Masked Transformers and Flow-Matching—on 100 hours of humanoid demonstrations.\n\n## Humanoid-Specific Architecture\n\nArchitectural variants with different attention mechanisms and parameter-sharing strategies are explored, with parameter-sharing techniques reducing model size by 33-53% with minimal impact on performance or visual fidelity.\n\n## Body Structure and Dynamics Awareness\n\nA hierarchical world model approach uses a high-level agent that generates commands based on visual observations for a low-level agent to execute, both trained with rewards. This dual-system design enables humanoid robots to execute complex whole-body movements with both long-horizon coherence and immediate reactivity.\n\n## Data Generation and Applications\n\nWorld models predict the future outcome of a given action, supporting capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. BFMs serve as a pivotal bridge between high-level semantic instructions and low-level physical execution, leveraging pre-trained behavioral priors to enable zero-shot adaptation, multi-task generalization, and physics-aware motion synthesis.\n\nThe field has rapidly advanced in 2025-2026, with recent work focusing on integrating multiple data sources, improving efficiency through parameter sharing, and enabling complex whole-body coordination for humanoid robotics."
    ],
    "durationSeconds": 7.595624909000006
  },
  "sourceToolAssistantUUID": "f70e43e8-dcb1-4285-bcd1-96c8b9198a85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-10T17:18:21.454Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FdpGMLGdrVtoWKY8ivrYjU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.01182",
  "prompt": "Extract the key technical details of \"Humanoid World Models\": What is their architecture? How do they condition on humanoid actions? What data do they use? What are the results? What gaps/limitations do they identify? When was this published?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b07307b1-60b1-4a3f-9847-14f6a5ef1df7",
  "isSidechain": false,
  "requestId": "req_011CauGaSbmArDbv8Bo81qc9",
  "type": "assistant",
  "uuid": "c87e55b7-6893-455f-8a61-fa7bff7c5927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeFkFB8uMMk9BVas3Ybojw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 67913,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 67913,
          "cache_creation_input_tokens": 1087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1087
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

_source line 142 · 2026-05-10T17:18:26.756Z_

<details><summary>↩ Tool result · `toolu_01FdpGMLGdrVtoWKY8ivrYjU`</summary>

```text
# Humanoid World Models: Technical Summary

**Publication:** June 1, 2025 (revised July 8, 2025)

**Architecture:**
The models employ two generative approaches: "Masked Transformers and Flow-Matching" designs. The researchers explored "architectural variants with different attention mechanisms and parameter-sharing strategies," achieving significant compression through parameter-sharing that "reduce[s] model size by 33-53% with minimal impact on performance or visual fidelity."

**Action Conditioning:**
The system forecasts "future egocentric video conditioned on humanoid control tokens," treating robot actions as discrete control inputs.

**Training Data:**
Models were trained on "100 hours of humanoid demonstrations," providing the foundational dataset for learning dynamics.

**Design Philosophy:**
These are described as "lightweight, open-source models" specifically engineered for accessibility, as they are "designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs."

**Primary Purpose:**
The models serve dual functions: acting "as a dynamics model in long-horizon planning and generating synthetic data for policy learning."

**Identified Challenges:**
The abstract identifies that "enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge"—the core problem HWM attempts to address.

No explicit limitations section appears in the provided abstract content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c87e55b7-6893-455f-8a61-fa7bff7c5927",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "cdd1855e-111e-429f-a778-dfaab17b461d",
  "toolUseResult": {
    "bytes": 45080,
    "code": 200,
    "codeText": "OK",
    "result": "# Humanoid World Models: Technical Summary\n\n**Publication:** June 1, 2025 (revised July 8, 2025)\n\n**Architecture:**\nThe models employ two generative approaches: \"Masked Transformers and Flow-Matching\" designs. The researchers explored \"architectural variants with different attention mechanisms and parameter-sharing strategies,\" achieving significant compression through parameter-sharing that \"reduce[s] model size by 33-53% with minimal impact on performance or visual fidelity.\"\n\n**Action Conditioning:**\nThe system forecasts \"future egocentric video conditioned on humanoid control tokens,\" treating robot actions as discrete control inputs.\n\n**Training Data:**\nModels were trained on \"100 hours of humanoid demonstrations,\" providing the foundational dataset for learning dynamics.\n\n**Design Philosophy:**\nThese are described as \"lightweight, open-source models\" specifically engineered for accessibility, as they are \"designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.\"\n\n**Primary Purpose:**\nThe models serve dual functions: acting \"as a dynamics model in long-horizon planning and generating synthetic data for policy learning.\"\n\n**Identified Challenges:**\nThe abstract identifies that \"enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge\"—the core problem HWM attempts to address.\n\nNo explicit limitations section appears in the provided abstract content.",
    "durationMs": 5295,
    "url": "https://arxiv.org/abs/2506.01182"
  },
  "sourceToolAssistantUUID": "c87e55b7-6893-455f-8a61-fa7bff7c5927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-10T17:18:29.870Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SbEZiMByR38LTN3eeTv1VJ`</summary>

```json
{
  "query": "inverse dynamics model humanoid action labeling video synthetic trajectory pseudo-action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdd1855e-111e-429f-a778-dfaab17b461d",
  "isSidechain": false,
  "requestId": "req_011CauGbBBLvqVjvQuoV8y31",
  "type": "assistant",
  "uuid": "241621ce-2497-4666-8d2b-128114656225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UTr5nVSZFyvfYErmwuTTnL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 69000,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 69000,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 450
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

_source line 144 · 2026-05-10T17:18:39.238Z_

<details><summary>↩ Tool result · `toolu_01SbEZiMByR38LTN3eeTv1VJ`</summary>

```text
Web search results for query: "inverse dynamics model humanoid action labeling video synthetic trajectory pseudo-action 2025 2026"

Links: [{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734v2"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards","url":"https://arxiv.org/html/2603.17808"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://arxiv.org/html/2505.12705v1"},{"title":"How to train generalist robots with NVIDIA's research workflows and foundation models - The Robot Report","url":"https://www.therobotreport.com/how-to-train-generalist-robots-with-nvidias-research-workflows-and-foundation-models/"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Action-Conditioned Video World Model","url":"https://www.emergentmind.com/topics/action-conditioned-video-world-model"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"}]

Based on the search results, I found several highly relevant research papers and projects from 2025-2026 that discuss inverse dynamics models, humanoid action labeling, video synthetic trajectories, and pseudo-actions. Here are the key findings:

## GR00T N1: Foundation Model for Generalist Humanoid Robots

A trained inverse dynamics model (IDM) is used to infer pseudo-actions, and these techniques enable annotating actions on action-less videos so they can be treated as additional robot embodiments for model training. For action-less data sources like human videos and neural-generated videos, a latent-action codebook is learned and a trained inverse dynamics model (IDM) is used to infer pseudo-actions.

## DreamGen Pipeline

DreamGen leverages state-of-the-art image-to-video generative models, adapting them to target robot embodiments to produce photorealistic synthetic videos, and recovers pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM).

## DeFI: Decoupled Forward and Inverse Dynamics

DeFI unlocks the potential of large-scale, action-free videos by decoupling the forward and inverse dynamics pretraining, then cooperating in an end-to-end manner for mutual benefit.

## Practical Implementation

To extract pseudo-actions, researchers apply a latent action model or inverse dynamics model (IDM) to turn videos into labeled action sequences (neural trajectories).

These approaches enable training humanoid robots on synthetic video trajectories without explicit action labels by using inverse dynamics models to recover the corresponding actions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "241621ce-2497-4666-8d2b-128114656225",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "82abf353-ef59-4c98-9093-45347351a267",
  "toolUseResult": {
    "query": "inverse dynamics model humanoid action labeling video synthetic trajectory pseudo-action 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012n3xitVCuKbpcE1QXRHhNG",
        "content": [
          {
            "title": "2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"
          },
          {
            "title": "2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/pdf/2503.14734"
          },
          {
            "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/html/2503.14734v2"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.16391"
          },
          {
            "title": "Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
            "url": "https://arxiv.org/html/2603.17808"
          },
          {
            "title": "DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories",
            "url": "https://arxiv.org/html/2505.12705v1"
          },
          {
            "title": "How to train generalist robots with NVIDIA's research workflows and foundation models - The Robot Report",
            "url": "https://www.therobotreport.com/how-to-train-generalist-robots-with-nvidias-research-workflows-and-foundation-models/"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Action-Conditioned Video World Model",
            "url": "https://www.emergentmind.com/topics/action-conditioned-video-world-model"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          }
        ]
      },
      "Based on the search results, I found several highly relevant research papers and projects from 2025-2026 that discuss inverse dynamics models, humanoid action labeling, video synthetic trajectories, and pseudo-actions. Here are the key findings:\n\n## GR00T N1: Foundation Model for Generalist Humanoid Robots\n\nA trained inverse dynamics model (IDM) is used to infer pseudo-actions, and these techniques enable annotating actions on action-less videos so they can be treated as additional robot embodiments for model training. For action-less data sources like human videos and neural-generated videos, a latent-action codebook is learned and a trained inverse dynamics model (IDM) is used to infer pseudo-actions.\n\n## DreamGen Pipeline\n\nDreamGen leverages state-of-the-art image-to-video generative models, adapting them to target robot embodiments to produce photorealistic synthetic videos, and recovers pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM).\n\n## DeFI: Decoupled Forward and Inverse Dynamics\n\nDeFI unlocks the potential of large-scale, action-free videos by decoupling the forward and inverse dynamics pretraining, then cooperating in an end-to-end manner for mutual benefit.\n\n## Practical Implementation\n\nTo extract pseudo-actions, researchers apply a latent action model or inverse dynamics model (IDM) to turn videos into labeled action sequences (neural trajectories).\n\nThese approaches enable training humanoid robots on synthetic video trajectories without explicit action labels by using inverse dynamics models to recover the corresponding actions."
    ],
    "durationSeconds": 9.363983018000027
  },
  "sourceToolAssistantUUID": "241621ce-2497-4666-8d2b-128114656225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-10T17:18:42.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NnGfqUBDrjhhv7ErbmS2Xi`</summary>

```json
{
  "query": "contact-aware trajectory generation humanoid object interaction simulation automated 2025 2026 arxiv data pipeline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82abf353-ef59-4c98-9093-45347351a267",
  "isSidechain": false,
  "requestId": "req_011CauGc6aYtF1STMD95dvph",
  "type": "assistant",
  "uuid": "7dcb2fde-eecc-4e44-9806-2bad2e1de4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8SWRSh1xCoT9zejvAGyxi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 69450,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1089,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 69450,
          "cache_creation_input_tokens": 1089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1089
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

_source line 146 · 2026-05-10T17:18:51.604Z_

<details><summary>↩ Tool result · `toolu_01NnGfqUBDrjhhv7ErbmS2Xi`</summary>

```text
Web search results for query: "contact-aware trajectory generation humanoid object interaction simulation automated 2025 2026 arxiv data pipeline"

Links: [{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning","url":"https://arxiv.org/html/2506.16012v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"3D Human Interaction Generation: A Survey","url":"https://arxiv.org/html/2503.13120v1"},{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"[2502.20382] Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization","url":"https://arxiv.org/abs/2502.20382"},{"title":"HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos","url":"https://arxiv.org/html/2602.02473v1"},{"title":"SPIDER: Scalable Physics-Informed Dexterous Retargeting","url":"https://arxiv.org/html/2511.09484v1"},{"title":"[2512.02729] RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning","url":"https://arxiv.org/abs/2512.02729"},{"title":"Decoupled Generative Modeling for Human-Object Interaction Synthesis","url":"https://arxiv.org/html/2512.19049v1"}]

I found several highly relevant research papers on arXiv related to contact-aware trajectory generation, humanoid object interaction, simulation, and automated data pipelines. Here are the key findings:

## Recent Publications (2025-2026)

**Physics-Driven Data Generation for Contact-Rich Manipulation:**
A low-cost data generation pipeline integrates physics-based simulation, human demonstrations, and model-based planning to efficiently generate large-scale, high-quality datasets for contact-rich robotic manipulation tasks, starting with human demonstrations collected in a virtual reality simulation environment and refining them using optimization-based kinematic retargeting and trajectory optimization to adapt them across various robot embodiments and physical parameters.

**HumanX: Humanoid Interaction Skills from Human Videos:**
The XGen data generation system operates in three stages: (1) extracting human motion and retargeting it to the robot; (2) physics-based synthesis of object trajectories coupled with contact-aware refinement; and (3) data augmentation through object geometry scaling and trajectory variation to maximize coverage.

**OmniRetarget: Interaction-Preserving Data Generation:**
OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. The system generates over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation, enabling proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid.

**SPIDER: Scalable Physics-Informed Dexterous Retargeting:**
SPIDER converts human-object interaction trajectories to dynamically feasible robot-object interaction trajectories using sampling with parallel physics simulator and introduces a virtual contact guidance method to minimize solution ambiguity in contact-rich tasks.

**DecHOI: Decoupled Generative Modeling for Human-Object Interaction:**
DecHOI proposes a decoupled framework that separates trajectory generation from fine-grained action synthesis, reducing optimization complexity.

These papers collectively address automated data generation pipelines that leverage physics simulation, contact modeling, and trajectory optimization for humanoid robot control and object manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dcb2fde-eecc-4e44-9806-2bad2e1de4a4",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "0138d9af-d8bb-41f3-b101-7eccb74292d7",
  "toolUseResult": {
    "query": "contact-aware trajectory generation humanoid object interaction simulation automated 2025 2026 arxiv data pipeline",
    "results": [
      {
        "tool_use_id": "srvtoolu_019vEEg1qkab5JPsxDhVqiBs",
        "content": [
          {
            "title": "Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors",
            "url": "https://arxiv.org/html/2501.02116v1"
          },
          {
            "title": "DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning",
            "url": "https://arxiv.org/html/2506.16012v1"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "3D Human Interaction Generation: A Survey",
            "url": "https://arxiv.org/html/2503.13120v1"
          },
          {
            "title": "[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://arxiv.org/abs/2509.26633"
          },
          {
            "title": "[2502.20382] Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization",
            "url": "https://arxiv.org/abs/2502.20382"
          },
          {
            "title": "HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos",
            "url": "https://arxiv.org/html/2602.02473v1"
          },
          {
            "title": "SPIDER: Scalable Physics-Informed Dexterous Retargeting",
            "url": "https://arxiv.org/html/2511.09484v1"
          },
          {
            "title": "[2512.02729] RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning",
            "url": "https://arxiv.org/abs/2512.02729"
          },
          {
            "title": "Decoupled Generative Modeling for Human-Object Interaction Synthesis",
            "url": "https://arxiv.org/html/2512.19049v1"
          }
        ]
      },
      "I found several highly relevant research papers on arXiv related to contact-aware trajectory generation, humanoid object interaction, simulation, and automated data pipelines. Here are the key findings:\n\n## Recent Publications (2025-2026)\n\n**Physics-Driven Data Generation for Contact-Rich Manipulation:**\nA low-cost data generation pipeline integrates physics-based simulation, human demonstrations, and model-based planning to efficiently generate large-scale, high-quality datasets for contact-rich robotic manipulation tasks, starting with human demonstrations collected in a virtual reality simulation environment and refining them using optimization-based kinematic retargeting and trajectory optimization to adapt them across various robot embodiments and physical parameters.\n\n**HumanX: Humanoid Interaction Skills from Human Videos:**\nThe XGen data generation system operates in three stages: (1) extracting human motion and retargeting it to the robot; (2) physics-based synthesis of object trajectories coupled with contact-aware refinement; and (3) data augmentation through object geometry scaling and trajectory variation to maximize coverage.\n\n**OmniRetarget: Interaction-Preserving Data Generation:**\nOmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. The system generates over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation, enabling proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid.\n\n**SPIDER: Scalable Physics-Informed Dexterous Retargeting:**\nSPIDER converts human-object interaction trajectories to dynamically feasible robot-object interaction trajectories using sampling with parallel physics simulator and introduces a virtual contact guidance method to minimize solution ambiguity in contact-rich tasks.\n\n**DecHOI: Decoupled Generative Modeling for Human-Object Interaction:**\nDecHOI proposes a decoupled framework that separates trajectory generation from fine-grained action synthesis, reducing optimization complexity.\n\nThese papers collectively address automated data generation pipelines that leverage physics simulation, contact modeling, and trajectory optimization for humanoid robot control and object manipulation."
    ],
    "durationSeconds": 9.269191896999953
  },
  "sourceToolAssistantUUID": "7dcb2fde-eecc-4e44-9806-2bad2e1de4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 147_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "0138d9af-d8bb-41f3-b101-7eccb74292d7",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 148_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 149 · 2026-05-10T17:18:55.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0184wn4HgCrCFaerL5XSukKE`</summary>

```json
{
  "query": "\"task-conditioned\" OR \"task-aware\" diffusion trajectory generation humanoid sim scalable automated 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0138d9af-d8bb-41f3-b101-7eccb74292d7",
  "isSidechain": false,
  "requestId": "req_011CauGd1RmR7t73HwF5Q4fD",
  "type": "assistant",
  "uuid": "144fe7bb-e249-4072-bfd0-4634d9e862a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HEBwauKgREjhmZtxR5L8Ws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 70539,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 70539,
          "cache_creation_input_tokens": 1118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1118
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

_source line 150 · 2026-05-10T17:19:02.002Z_

<details><summary>↩ Tool result · `toolu_0184wn4HgCrCFaerL5XSukKE`</summary>

```text
Web search results for query: ""task-conditioned" OR "task-aware" diffusion trajectory generation humanoid sim scalable automated 2025 2026"

Links: [{"title":"DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors","url":"https://arxiv.org/html/2604.00202"},{"title":"One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion","url":"https://arxiv.org/html/2505.18780v2"},{"title":"DynScene: Scalable Generation of Dynamic Robotic ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.pdf"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335v1"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"},{"title":"TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"},{"title":"TLControl: Trajectory and Language Control for Human Motion Synthesis | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72913-3_3"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Scalable and General Whole-Body Control for Cross-Humanoid Locomotion","url":"https://arxiv.org/html/2602.05791v2"}]

I've completed the web search for your query. Here are the key findings:

## Recent Research on Task-Conditioned Diffusion for Humanoid Robots (2025-2026)

**DreamControl-v2** (March 2026) is a prominent recent work in this area. The framework uses a four-stage pipeline where a humanoid motion diffusion model is trained to generate reference trajectories conditioned on text and spatio-temporal control signals. The DreamControl-v2 diffusion model can generate trajectories jointly conditioned on both open vocabulary text and spatio-temporal constraints.

**DreamPolicy** (June 2025) represents another key development. DreamPolicy augments reinforcement learning through integration of a terrain-aware autoregressive diffusion planner and introduces Humanoid Motion Imagery (HMI) - future state predictions synthesized by a diffusion model trained on aggregated expert demonstrations. The framework trains an autoregressive Diffusion Planner to model cross-scenario state-action distributions, enabling probabilistic synthesis of physically plausible trajectories.

**Scalable Cross-Humanoid Control** (February 2026) addresses generalization across multiple robot embodiments. Cross-embodiment learning aims to find control policies that generalize across robots with different morphologies and dynamics, though most existing approaches train on a small set of embodiments and achieve limited transfer.

The research demonstrates significant progress in scalable, task-aware trajectory generation for humanoid robots in simulation with deployment capabilities to real systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "144fe7bb-e249-4072-bfd0-4634d9e862a4",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "77a8fefc-bcdf-4bdf-9756-0a03baf0dcb4",
  "toolUseResult": {
    "query": "\"task-conditioned\" OR \"task-aware\" diffusion trajectory generation humanoid sim scalable automated 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CUnGztxzhGmky8zeC2LVZA",
        "content": [
          {
            "title": "DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors",
            "url": "https://arxiv.org/html/2604.00202"
          },
          {
            "title": "One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion",
            "url": "https://arxiv.org/html/2505.18780v2"
          },
          {
            "title": "DynScene: Scalable Generation of Dynamic Robotic ...",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.pdf"
          },
          {
            "title": "Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking",
            "url": "https://arxiv.org/html/2604.17335v1"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          },
          {
            "title": "TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"
          },
          {
            "title": "TLControl: Trajectory and Language Control for Human Motion Synthesis | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-72913-3_3"
          },
          {
            "title": "GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more",
            "url": "https://github.com/smallfryy/corl-2025-papers"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Scalable and General Whole-Body Control for Cross-Humanoid Locomotion",
            "url": "https://arxiv.org/html/2602.05791v2"
          }
        ]
      },
      "I've completed the web search for your query. Here are the key findings:\n\n## Recent Research on Task-Conditioned Diffusion for Humanoid Robots (2025-2026)\n\n**DreamControl-v2** (March 2026) is a prominent recent work in this area. The framework uses a four-stage pipeline where a humanoid motion diffusion model is trained to generate reference trajectories conditioned on text and spatio-temporal control signals. The DreamControl-v2 diffusion model can generate trajectories jointly conditioned on both open vocabulary text and spatio-temporal constraints.\n\n**DreamPolicy** (June 2025) represents another key development. DreamPolicy augments reinforcement learning through integration of a terrain-aware autoregressive diffusion planner and introduces Humanoid Motion Imagery (HMI) - future state predictions synthesized by a diffusion model trained on aggregated expert demonstrations. The framework trains an autoregressive Diffusion Planner to model cross-scenario state-action distributions, enabling probabilistic synthesis of physically plausible trajectories.\n\n**Scalable Cross-Humanoid Control** (February 2026) addresses generalization across multiple robot embodiments. Cross-embodiment learning aims to find control policies that generalize across robots with different morphologies and dynamics, though most existing approaches train on a small set of embodiments and achieve limited transfer.\n\nThe research demonstrates significant progress in scalable, task-aware trajectory generation for humanoid robots in simulation with deployment capabilities to real systems."
    ],
    "durationSeconds": 6.900477155999979
  },
  "sourceToolAssistantUUID": "144fe7bb-e249-4072-bfd0-4634d9e862a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-10T17:19:05.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011tPXyyx5EnXoT1JGcjcN1U`</summary>

```json
{
  "query": "latent action model action-free video humanoid policy learning data scarcity solution 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a8fefc-bcdf-4bdf-9756-0a03baf0dcb4",
  "isSidechain": false,
  "requestId": "req_011CauGdmsiUMcnLkCb9eznA",
  "type": "assistant",
  "uuid": "9ac58ee4-d3cd-4400-839a-bc5310e656a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NeLRT8tWqL1on9YxEx9zc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 71657,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 71657,
          "cache_creation_input_tokens": 1116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1116
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

_source line 152 · 2026-05-10T17:19:14.070Z_

<details><summary>↩ Tool result · `toolu_011tPXyyx5EnXoT1JGcjcN1U`</summary>

```text
Web search results for query: "latent action model action-free video humanoid policy learning data scarcity solution 2025 2026"

Links: [{"title":"Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA","url":"https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"},{"title":"Learning to Act Anywhere with Task-centric Latent Actions | Request PDF","url":"https://www.researchgate.net/publication/395376330_Learning_to_Act_Anywhere_with_Task-centric_Latent_Actions"},{"title":"EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos","url":"https://rchalyang.github.io/EgoVLA/"},{"title":"arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control","url":"https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"},{"title":"Factored Latent Action World Models","url":"https://arxiv.org/html/2602.16229"},{"title":"[2505.04999] CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations","url":"https://arxiv.org/abs/2505.04999"},{"title":"2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"},{"title":"Latent Action Pretraining from Videos | Research","url":"https://research.nvidia.com/publication/2025-04_latent-action-pretraining-videos"},{"title":"Learning to Act Anywhere with Task-centric Latent Actions","url":"https://arxiv.org/pdf/2505.06111"},{"title":"Latent Action Pretraining from Videos | OpenReview","url":"https://openreview.net/forum?id=VYOe2eBQeh"}]

Based on the web search results, I found several relevant papers and approaches addressing latent action models, action-free video learning, and humanoid policy learning to solve data scarcity challenges in 2025-2026:

## Key Findings:

### Latent Action Models for Action-Free Videos

Latent action learning sidesteps explicit action labels by compressing frame-to-frame visual changes into compact, discrete tokens that supervise policy learning from action-free videos.

### WholeBodyVLA - Unified Latent VLA

WholeBodyVLA introduces unified latent learning, enabling joint locomotion–manipulation learning from abundant low-cost action-free videos and alleviating the scarcity of teleoperation data. The approach learns loco–manipulation behaviors from low-cost action-free videos, alleviating the scarcity of teleoperation data.

### Latent Action Pretraining

Latent Action Pretraining is the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. The method trains an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrains a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetunes the VLA on small-scale robot manipulation data to map from latent to robot actions.

### Cross-Embodiment Learning (UniVLA)

UniVLA derives task-centric latent actions in an unsupervised manner and can leverage data from arbitrary embodiments and perspectives without action labels, enabling cross-embodiment generalist policies that can be deployed across various robots.

### GR00T N1 Humanoid Foundation Model

GR00T N1 learns a latent-action codebook and uses a trained inverse dynamics model to infer pseudo-actions, enabling annotation of actions on action-less videos so they can be effectively treated as additional robot embodiments for model training.

### CLAM - Continuous Latent Action Models

CLAM incorporates continuous latent action labels instead of discrete representations, and jointly trains an action decoder to ensure that the latent action space can be easily grounded to real actions with relatively few labeled examples.

These approaches collectively address the data scarcity challenge in humanoid policy learning by leveraging action-free videos and learning latent representations that can be mapped to robot actions efficiently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ac58ee4-d3cd-4400-839a-bc5310e656a7",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "54a25d5e-2d34-43de-96be-8b799ccab1d3",
  "toolUseResult": {
    "query": "latent action model action-free video humanoid policy learning data scarcity solution 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HmeF251VgpysZmtfKqzZec",
        "content": [
          {
            "title": "Preprint WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA",
            "url": "https://opendrivelab.com/WholeBodyVLA/static/pdf/WholeBodyVLA.pdf"
          },
          {
            "title": "Learning to Act Anywhere with Task-centric Latent Actions | Request PDF",
            "url": "https://www.researchgate.net/publication/395376330_Learning_to_Act_Anywhere_with_Task-centric_Latent_Actions"
          },
          {
            "title": "EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos",
            "url": "https://rchalyang.github.io/EgoVLA/"
          },
          {
            "title": "arXiv:2506.13751v2 [cs.RO] 19 Jun 2025 LeVERB: Humanoid Whole-Body Control",
            "url": "https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf"
          },
          {
            "title": "Factored Latent Action World Models",
            "url": "https://arxiv.org/html/2602.16229"
          },
          {
            "title": "[2505.04999] CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations",
            "url": "https://arxiv.org/abs/2505.04999"
          },
          {
            "title": "2025-3-18 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf"
          },
          {
            "title": "Latent Action Pretraining from Videos | Research",
            "url": "https://research.nvidia.com/publication/2025-04_latent-action-pretraining-videos"
          },
          {
            "title": "Learning to Act Anywhere with Task-centric Latent Actions",
            "url": "https://arxiv.org/pdf/2505.06111"
          },
          {
            "title": "Latent Action Pretraining from Videos | OpenReview",
            "url": "https://openreview.net/forum?id=VYOe2eBQeh"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and approaches addressing latent action models, action-free video learning, and humanoid policy learning to solve data scarcity challenges in 2025-2026:\n\n## Key Findings:\n\n### Latent Action Models for Action-Free Videos\n\nLatent action learning sidesteps explicit action labels by compressing frame-to-frame visual changes into compact, discrete tokens that supervise policy learning from action-free videos.\n\n### WholeBodyVLA - Unified Latent VLA\n\nWholeBodyVLA introduces unified latent learning, enabling joint locomotion–manipulation learning from abundant low-cost action-free videos and alleviating the scarcity of teleoperation data. The approach learns loco–manipulation behaviors from low-cost action-free videos, alleviating the scarcity of teleoperation data.\n\n### Latent Action Pretraining\n\nLatent Action Pretraining is the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. The method trains an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrains a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetunes the VLA on small-scale robot manipulation data to map from latent to robot actions.\n\n### Cross-Embodiment Learning (UniVLA)\n\nUniVLA derives task-centric latent actions in an unsupervised manner and can leverage data from arbitrary embodiments and perspectives without action labels, enabling cross-embodiment generalist policies that can be deployed across various robots.\n\n### GR00T N1 Humanoid Foundation Model\n\nGR00T N1 learns a latent-action codebook and uses a trained inverse dynamics model to infer pseudo-actions, enabling annotation of actions on action-less videos so they can be effectively treated as additional robot embodiments for model training.\n\n### CLAM - Continuous Latent Action Models\n\nCLAM incorporates continuous latent action labels instead of discrete representations, and jointly trains an action decoder to ensure that the latent action space can be easily grounded to real actions with relatively few labeled examples.\n\nThese approaches collectively address the data scarcity challenge in humanoid policy learning by leveraging action-free videos and learning latent representations that can be mapped to robot actions efficiently."
    ],
    "durationSeconds": 8.920647222000058
  },
  "sourceToolAssistantUUID": "9ac58ee4-d3cd-4400-839a-bc5310e656a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 153 · 2026-05-10T17:19:14.073Z_

```json
{
  "parentUuid": "54a25d5e-2d34-43de-96be-8b799ccab1d3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6ee990d1-3c63-4ef9-8099-865c51cb9dae",
  "timestamp": "2026-05-10T17:19:14.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 154 · 2026-05-10T17:19:23.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B955Pn8L4tx7Nsqeq1KrB2`</summary>

```json
{
  "query": "Factored Latent Action World Models humanoid robot body part decomposition 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ee990d1-3c63-4ef9-8099-865c51cb9dae",
  "isSidechain": false,
  "requestId": "req_011CauGefhfLUA5cHLC5BxeW",
  "type": "assistant",
  "uuid": "1bf9a526-2518-4aa2-8001-7553778809ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XjKCAiZpHDJqTeWovc5B4H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 72773,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 72773,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1294
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

_source line 155 · 2026-05-10T17:19:29.920Z_

<details><summary>↩ Tool result · `toolu_01B955Pn8L4tx7Nsqeq1KrB2`</summary>

```text
Web search results for query: "Factored Latent Action World Models humanoid robot body part decomposition 2026"

Links: [{"title":"Factored Latent Action World Models","url":"https://arxiv.org/html/2602.16229"},{"title":"Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation | OpenReview","url":"https://openreview.net/forum?id=vEZgPr1deb"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Latent Action Models Overview","url":"https://www.emergentmind.com/topics/latent-action-models"},{"title":"[2602.16229] Factored Latent Action World Models","url":"https://arxiv.org/abs/2602.16229"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Hierarchical World Models as Visual Whole-Body Humanoid Controllers","url":"https://arxiv.org/html/2405.18418v2"}]

Based on the search results, I found relevant information about Factored Latent Action World Models:

## Factored Latent Action World Models

Factored Latent Action Model (FLAM) is a factored dynamics framework that decomposes the scene into independent factors, each inferring its own latent action and predicting its own next-step factor value.

### Problem It Addresses

In robot videos, independent arm movements and shifting camera perspectives occur simultaneously, with each acting independently, and compressing all these motions into a single latent action is challenging, since the complexity of the underlying action space grows exponentially with the number of movable entities.

### Body Part Decomposition

Multi-entity scenes require per-object/action factorization; FLAM demonstrates improved representation quality and controllable multi-entity rollouts. Factored LAMs (FLAM) and scene decomposition are essential for multi-agent and complex embodied settings.

### Recent Development

The paper was submitted on February 18, 2026, authored by Zizhao Wang and 6 other authors. This represents recent research in applying factored latent action models to handle complex multi-entity scenarios in robotics and video understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bf9a526-2518-4aa2-8001-7553778809ed",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "77240484-9d89-4b7e-be04-b3eb37f55c2e",
  "toolUseResult": {
    "query": "Factored Latent Action World Models humanoid robot body part decomposition 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012oawxRTJtDJgyNSWGfDgaJ",
        "content": [
          {
            "title": "Factored Latent Action World Models",
            "url": "https://arxiv.org/html/2602.16229"
          },
          {
            "title": "Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation | OpenReview",
            "url": "https://openreview.net/forum?id=vEZgPr1deb"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Latent Action Models Overview",
            "url": "https://www.emergentmind.com/topics/latent-action-models"
          },
          {
            "title": "[2602.16229] Factored Latent Action World Models",
            "url": "https://arxiv.org/abs/2602.16229"
          },
          {
            "title": "GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub",
            "url": "https://github.com/LMD0311/Awesome-World-Model"
          },
          {
            "title": "GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.",
            "url": "https://github.com/keon/awesome-physical-ai"
          },
          {
            "title": "Hierarchical World Models as Visual Whole-Body Humanoid Controllers",
            "url": "https://arxiv.org/html/2405.18418v2"
          }
        ]
      },
      "Based on the search results, I found relevant information about Factored Latent Action World Models:\n\n## Factored Latent Action World Models\n\nFactored Latent Action Model (FLAM) is a factored dynamics framework that decomposes the scene into independent factors, each inferring its own latent action and predicting its own next-step factor value.\n\n### Problem It Addresses\n\nIn robot videos, independent arm movements and shifting camera perspectives occur simultaneously, with each acting independently, and compressing all these motions into a single latent action is challenging, since the complexity of the underlying action space grows exponentially with the number of movable entities.\n\n### Body Part Decomposition\n\nMulti-entity scenes require per-object/action factorization; FLAM demonstrates improved representation quality and controllable multi-entity rollouts. Factored LAMs (FLAM) and scene decomposition are essential for multi-agent and complex embodied settings.\n\n### Recent Development\n\nThe paper was submitted on February 18, 2026, authored by Zizhao Wang and 6 other authors. This represents recent research in applying factored latent action models to handle complex multi-entity scenarios in robotics and video understanding."
    ],
    "durationSeconds": 6.471652739000041
  },
  "sourceToolAssistantUUID": "1bf9a526-2518-4aa2-8001-7553778809ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 156 · 2026-05-10T17:19:33.799Z_

Excellent — FLAM is very relevant. The factored decomposition idea for multi-entity scenes could be applied to humanoid body parts. Let me do a few final targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77240484-9d89-4b7e-be04-b3eb37f55c2e",
  "isSidechain": false,
  "requestId": "req_011CauGfqEvMKxNqZwWKrNdb",
  "type": "assistant",
  "uuid": "2bee73aa-7b9b-4add-986e-dd9563d27317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144DtBWwuNYWnWjVBHDvHv5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 74067,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 74067,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 157 · 2026-05-10T17:19:34.860Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Dp7amfNbDbdyNJYiTobDW`</summary>

```json
{
  "query": "automated demonstration generation humanoid walking AND picking OR carrying loco-manipulation sim pipeline no retargeting 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bee73aa-7b9b-4add-986e-dd9563d27317",
  "isSidechain": false,
  "requestId": "req_011CauGfqEvMKxNqZwWKrNdb",
  "type": "assistant",
  "uuid": "094cc4c5-bcbd-4bb7-aeb0-f6a3e7ca7da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144DtBWwuNYWnWjVBHDvHv5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 74067,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 74067,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 158 · 2026-05-10T17:19:42.825Z_

<details><summary>↩ Tool result · `toolu_016Dp7amfNbDbdyNJYiTobDW`</summary>

```text
Web search results for query: "automated demonstration generation humanoid walking AND picking OR carrying loco-manipulation sim pipeline no retargeting 2025 2026"

Links: [{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub","url":"https://github.com/visualmimic/VisualMimic"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"AI Humanoid Robots 2026: Technology, Builders & Future","url":"https://www.articsledge.com/post/ai-humanoid-robots"},{"title":"Introducing Helix 02: Full-Body Autonomy","url":"https://www.figure.ai/news/helix-02"},{"title":"Industry Insights: Humanoid Robots in 2025: The Next Stage of Evolution","url":"https://www.automate.org/industry-insights/humanoid-robots-are-evolving"},{"title":"Opportunities challenges and roadmap for humanoid robots in construction | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-30252-6"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"}]

Based on the web search results, I found several relevant papers and research areas related to your query about automated demonstration generation for humanoid loco-manipulation. Here are the key findings:

## Research on Humanoid Loco-Manipulation (2025-2026)

Recent work includes FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv 2025.05) and FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid (arXiv 2026.03).

Notable papers include VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv 2025.09), which appears directly relevant to automated demonstration generation for manipulation tasks.

Other relevant work includes Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation (arXiv 2024.06).

## Simulation and Real-World Transfer

Papers addressing sim-to-real transfer include "Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer" (arXiv 2025.11) and VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (arXiv 2025.11).

Figure's Helix 02 system utilizes "System 0, a learned whole-body controller trained on over 1,000 hours of human motion data and sim-to-real reinforcement learning", demonstrating a sophisticated approach to learning from demonstrations at scale.

The research landscape shows active development in automated pipelines for humanoid loco-manipulation that integrate walking, picking, and carrying tasks, with significant progress in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "094cc4c5-bcbd-4bb7-aeb0-f6a3e7ca7da8",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "3446f19b-17b5-4317-9cbc-8b0d3e29d8ed",
  "toolUseResult": {
    "query": "automated demonstration generation humanoid walking AND picking OR carrying loco-manipulation sim pipeline no retargeting 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QsqV5Qsczu5e4BofSEG7A9",
        "content": [
          {
            "title": "Innovative Humanoid Robots in 2025–2026 - Reality or Hype?",
            "url": "https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub",
            "url": "https://github.com/visualmimic/VisualMimic"
          },
          {
            "title": "Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology",
            "url": "https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "AI Humanoid Robots 2026: Technology, Builders & Future",
            "url": "https://www.articsledge.com/post/ai-humanoid-robots"
          },
          {
            "title": "Introducing Helix 02: Full-Body Autonomy",
            "url": "https://www.figure.ai/news/helix-02"
          },
          {
            "title": "Industry Insights: Humanoid Robots in 2025: The Next Stage of Evolution",
            "url": "https://www.automate.org/industry-insights/humanoid-robots-are-evolving"
          },
          {
            "title": "Opportunities challenges and roadmap for humanoid robots in construction | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-30252-6"
          },
          {
            "title": "Advancements in humanoid robot dynamics and learning-based locomotion control methods",
            "url": "https://www.oaepublish.com/articles/ir.2025.32"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and research areas related to your query about automated demonstration generation for humanoid loco-manipulation. Here are the key findings:\n\n## Research on Humanoid Loco-Manipulation (2025-2026)\n\nRecent work includes FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv 2025.05) and FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid (arXiv 2026.03).\n\nNotable papers include VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv 2025.09), which appears directly relevant to automated demonstration generation for manipulation tasks.\n\nOther relevant work includes Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation (arXiv 2024.06).\n\n## Simulation and Real-World Transfer\n\nPapers addressing sim-to-real transfer include \"Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer\" (arXiv 2025.11) and VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (arXiv 2025.11).\n\nFigure's Helix 02 system utilizes \"System 0, a learned whole-body controller trained on over 1,000 hours of human motion data and sim-to-real reinforcement learning\", demonstrating a sophisticated approach to learning from demonstrations at scale.\n\nThe research landscape shows active development in automated pipelines for humanoid loco-manipulation that integrate walking, picking, and carrying tasks, with significant progress in 2025-2026."
    ],
    "durationSeconds": 7.961560745000025
  },
  "sourceToolAssistantUUID": "094cc4c5-bcbd-4bb7-aeb0-f6a3e7ca7da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 159_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "3446f19b-17b5-4317-9cbc-8b0d3e29d8ed",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 160_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 161 · 2026-05-10T17:19:45.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N1wqyQhKbnXKrz7z2YVDxX`</summary>

```json
{
  "query": "sim-to-real humanoid synthetic data quality curriculum filtering diverse task generation 2025 2026 CoRL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3446f19b-17b5-4317-9cbc-8b0d3e29d8ed",
  "isSidechain": false,
  "requestId": "req_011CauGgnNK1UQbPtXm9BQbd",
  "type": "assistant",
  "uuid": "6ce3ee4b-cf36-49fa-812c-8be33f1f3f03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9pj2fgE6HvLy4qDPnfVfL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 75016,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 75016,
          "cache_creation_input_tokens": 1114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1114
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

_source line 162 · 2026-05-10T17:19:53.789Z_

<details><summary>↩ Tool result · `toolu_01N1wqyQhKbnXKrz7z2YVDxX`</summary>

```text
Web search results for query: "sim-to-real humanoid synthetic data quality curriculum filtering diverse task generation 2025 2026 CoRL"

Links: [{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"A SURVEY OF EMBODIED ARTIFICIAL INTELLIGENCE DATA ENGINEERING","url":"https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"3rd Synthetic Data for Computer Vision - CVPR 2026 | Synthetic Data for Computer Vision","url":"https://syndata4cv.github.io/"},{"title":"Workshop on Generalizable Priors for Robot Manipulation | CoRL 2025","url":"https://corl25-genpriors.github.io/"},{"title":"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | OpenReview","url":"https://openreview.net/forum?id=dk-2R1f_LR"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"}]

I found several relevant results related to your search query about sim-to-real humanoid robotics, synthetic data, and related topics from 2025-2026 including CoRL materials. Here's what the search revealed:

## Key Resources Found:

1. **CoRL 2025 Paper Collection**: There is a collection of 200+ CoRL 2025 papers covering diverse robotics topics, including work on transferring vision-based dexterous manipulation skills onto humanoid platforms via RL.

2. **Synthetic Motion Generation for Humanoids**: Recent work describes building synthetic motion generation pipelines that add additional diversity by randomizing background, lighting, and other variables in scenes, then generate larger sets of physically accurate synthetic motion trajectories and photorealistic, diverse training data.

3. **Sim-to-Real Transfer Research**: Multiple 2025 papers address sim-to-real gaps for humanoids, including work on multi-simulator dynamics randomization and systematic sim-to-real transfer for diverse legged robots.

4. **Data Engineering Survey**: Recent developments involve creating high-fidelity, diverse virtual environments and task scenarios through simulation platforms to generate multimodal data, leveraging 3D modeling, physics engines, and generative AI to rapidly produce large volumes of high-quality training data.

5. **Diverse Task Generation**: Recent papers include work on "DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning" and "RoboSplat: Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation".

6. **CoRL 2025 Workshop on Generalizable Priors**: This workshop covers sim-to-real transfer, learning from human videos, and large-scale robotic data collection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ce3ee4b-cf36-49fa-812c-8be33f1f3f03",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "f89e6c03-cace-41dc-9508-283abba8dafe",
  "toolUseResult": {
    "query": "sim-to-real humanoid synthetic data quality curriculum filtering diverse task generation 2025 2026 CoRL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JqcKWBdq54ZqnbqjJGK1Dk",
        "content": [
          {
            "title": "GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more",
            "url": "https://github.com/smallfryy/corl-2025-papers"
          },
          {
            "title": "Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "A SURVEY OF EMBODIED ARTIFICIAL INTELLIGENCE DATA ENGINEERING",
            "url": "https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf"
          },
          {
            "title": "GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub",
            "url": "https://github.com/YanjieZe/Paper-List"
          },
          {
            "title": "3rd Synthetic Data for Computer Vision - CVPR 2026 | Synthetic Data for Computer Vision",
            "url": "https://syndata4cv.github.io/"
          },
          {
            "title": "Workshop on Generalizable Priors for Robot Manipulation | CoRL 2025",
            "url": "https://corl25-genpriors.github.io/"
          },
          {
            "title": "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | OpenReview",
            "url": "https://openreview.net/forum?id=dk-2R1f_LR"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "TYPE Mini Review PUBLISHED 01 December 2025 DOI 10.3389/frobt.2025.1678567",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"
          }
        ]
      },
      "I found several relevant results related to your search query about sim-to-real humanoid robotics, synthetic data, and related topics from 2025-2026 including CoRL materials. Here's what the search revealed:\n\n## Key Resources Found:\n\n1. **CoRL 2025 Paper Collection**: There is a collection of 200+ CoRL 2025 papers covering diverse robotics topics, including work on transferring vision-based dexterous manipulation skills onto humanoid platforms via RL.\n\n2. **Synthetic Motion Generation for Humanoids**: Recent work describes building synthetic motion generation pipelines that add additional diversity by randomizing background, lighting, and other variables in scenes, then generate larger sets of physically accurate synthetic motion trajectories and photorealistic, diverse training data.\n\n3. **Sim-to-Real Transfer Research**: Multiple 2025 papers address sim-to-real gaps for humanoids, including work on multi-simulator dynamics randomization and systematic sim-to-real transfer for diverse legged robots.\n\n4. **Data Engineering Survey**: Recent developments involve creating high-fidelity, diverse virtual environments and task scenarios through simulation platforms to generate multimodal data, leveraging 3D modeling, physics engines, and generative AI to rapidly produce large volumes of high-quality training data.\n\n5. **Diverse Task Generation**: Recent papers include work on \"DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning\" and \"RoboSplat: Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation\".\n\n6. **CoRL 2025 Workshop on Generalizable Priors**: This workshop covers sim-to-real transfer, learning from human videos, and large-scale robotic data collection."
    ],
    "durationSeconds": 8.324996766000055
  },
  "sourceToolAssistantUUID": "6ce3ee4b-cf36-49fa-812c-8be33f1f3f03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-10T17:19:56.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGas1n99vYr7YJpLmScxeV`</summary>

```json
{
  "query": "contact graph humanoid manipulation task generation object affordance procedural simulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f89e6c03-cace-41dc-9508-283abba8dafe",
  "isSidechain": false,
  "requestId": "req_011CauGhbFrH5MmLq5JC6qep",
  "type": "assistant",
  "uuid": "320a16f7-4b46-4d14-867c-d32efe84c841",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNMbvktQaSnMUzi93hN9aG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1140,
      "cache_read_input_tokens": 76130,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1140,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 76130,
          "cache_creation_input_tokens": 1140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1140
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

_source line 164 · 2026-05-10T17:20:04.559Z_

<details><summary>↩ Tool result · `toolu_01AGas1n99vYr7YJpLmScxeV`</summary>

```text
Web search results for query: "contact graph humanoid manipulation task generation object affordance procedural simulation 2025 2026"

Links: [{"title":"GAM: General affordance-based manipulation for contact-rich object disentangling tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231224001577"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Learning Object Affordance with Contact and Grasp Generation | OpenReview","url":"https://openreview.net/forum?id=e9-w5aLkZM"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v2"},{"title":"Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids","url":"https://arxiv.org/html/2502.20396"},{"title":"Enhancing task-oriented robotic grasping via 3D affordance grounding from vision-language models | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02169-0"},{"title":"learning object affordance with contact","url":"https://openreview.net/pdf?id=e9-w5aLkZM"},{"title":"RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/html/2603.07691v1"}]

I've completed the web search for your query about contact graph, humanoid manipulation, task generation, object affordance, and procedural simulation for 2025-2026. Here are the key findings:

## Recent Research in Humanoid Manipulation and Affordance Learning

**Affordance-Based Manipulation Models:**
The A0 model decomposes robotic manipulation tasks into two levels: high-level spatial affordance understanding and low-level action execution, leveraging an Embodiment-Agnostic Affordance Representation to predict object-centric contact points and post-contact trajectories.

**Contact-Based Task Generation:**
Contact stickers can be procedurally generated along box sides or edges based on object dimensions, with resulting behaviors closely reflecting specified contact positions. This approach is being applied to vision-based dexterous manipulation on humanoid robots.

**Humanoid-Specific Advances (2025-2026):**
The research landscape includes several recent developments: Notable 2025-2026 works include RoboGrasp (a universal grasping policy), 3D-AffordanceLLM for open-vocabulary affordance detection, and Ψ₀ (an open foundation model towards universal humanoid loco-manipulation).

**Contact Prediction for Manipulation Planning:**
Research has focused on learning affordance—potential contact points for household object manipulation tasks. Recent frameworks like RoboPCA propose pose-centered affordance prediction that jointly predicts task-appropriate contact regions and poses conditioned on instructions.

**3D Affordance Grounding:**
Novel approaches involve creating affordance-labeled grasp datasets through simulation with diverse functional interactions, using language-guided frameworks that take partial point clouds and natural language as input, with vision-language affordance grounding modules producing dense 3D affordance maps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "320a16f7-4b46-4d14-867c-d32efe84c841",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "3d8688b3-98e9-41a3-80b2-adbda409c5e2",
  "toolUseResult": {
    "query": "contact graph humanoid manipulation task generation object affordance procedural simulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PA3oRmCkecHEfdBZtAV2c1",
        "content": [
          {
            "title": "GAM: General affordance-based manipulation for contact-rich object disentangling tasks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0925231224001577"
          },
          {
            "title": "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation_ICCV_2025_paper.pdf"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Learning Object Affordance with Contact and Grasp Generation | OpenReview",
            "url": "https://openreview.net/forum?id=e9-w5aLkZM"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors",
            "url": "https://arxiv.org/html/2501.02116v2"
          },
          {
            "title": "Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids",
            "url": "https://arxiv.org/html/2502.20396"
          },
          {
            "title": "Enhancing task-oriented robotic grasping via 3D affordance grounding from vision-language models | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-02169-0"
          },
          {
            "title": "learning object affordance with contact",
            "url": "https://openreview.net/pdf?id=e9-w5aLkZM"
          },
          {
            "title": "RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation",
            "url": "https://arxiv.org/html/2603.07691v1"
          }
        ]
      },
      "I've completed the web search for your query about contact graph, humanoid manipulation, task generation, object affordance, and procedural simulation for 2025-2026. Here are the key findings:\n\n## Recent Research in Humanoid Manipulation and Affordance Learning\n\n**Affordance-Based Manipulation Models:**\nThe A0 model decomposes robotic manipulation tasks into two levels: high-level spatial affordance understanding and low-level action execution, leveraging an Embodiment-Agnostic Affordance Representation to predict object-centric contact points and post-contact trajectories.\n\n**Contact-Based Task Generation:**\nContact stickers can be procedurally generated along box sides or edges based on object dimensions, with resulting behaviors closely reflecting specified contact positions. This approach is being applied to vision-based dexterous manipulation on humanoid robots.\n\n**Humanoid-Specific Advances (2025-2026):**\nThe research landscape includes several recent developments: Notable 2025-2026 works include RoboGrasp (a universal grasping policy), 3D-AffordanceLLM for open-vocabulary affordance detection, and Ψ₀ (an open foundation model towards universal humanoid loco-manipulation).\n\n**Contact Prediction for Manipulation Planning:**\nResearch has focused on learning affordance—potential contact points for household object manipulation tasks. Recent frameworks like RoboPCA propose pose-centered affordance prediction that jointly predicts task-appropriate contact regions and poses conditioned on instructions.\n\n**3D Affordance Grounding:**\nNovel approaches involve creating affordance-labeled grasp datasets through simulation with diverse functional interactions, using language-guided frameworks that take partial point clouds and natural language as input, with vision-language affordance grounding modules producing dense 3D affordance maps."
    ],
    "durationSeconds": 8.089581925999955
  },
  "sourceToolAssistantUUID": "320a16f7-4b46-4d14-867c-d32efe84c841",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-10T17:20:07.614Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BycAgq5kGFi47JNX6bNGd`</summary>

```json
{
  "query": "SkillBlender skill primitive compositional data generation humanoid diverse demonstration synthesis 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d8688b3-98e9-41a3-80b2-adbda409c5e2",
  "isSidechain": false,
  "requestId": "req_011CauGiPK35BmzDi5TBjrt9",
  "type": "assistant",
  "uuid": "4230c72b-d93b-40da-93bc-5fe990ec8f6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBAQGmsnmBWN7WiXM9JW8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 77270,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 77270,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 166 · 2026-05-10T17:20:14.418Z_

<details><summary>↩ Tool result · `toolu_016BycAgq5kGFi47JNX6bNGd`</summary>

```text
Web search results for query: "SkillBlender skill primitive compositional data generation humanoid diverse demonstration synthesis 2025"

Links: [{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/html/2506.09366v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"GitHub - Humanoid-SkillBlender/SkillBlender: Official implementation of SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://github.com/Humanoid-SkillBlender/SkillBlender"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Control via Skill Blending | OpenReview","url":"https://openreview.net/forum?id=4MUgd8EN0F"},{"title":"[2506.09366] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/abs/2506.09366"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending | Request PDF","url":"https://www.researchgate.net/publication/392597734_SkillBlender_Towards_Versatile_Humanoid_Whole-Body_Loco-Manipulation_via_Skill_Blending"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://usc-gvl.github.io/SkillBlender-web/"},{"title":"Paper page - SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://huggingface.co/papers/2506.09366"},{"title":"[Literature Review] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://www.themoonlight.io/en/review/skillblender-towards-versatile-humanoid-whole-body-loco-manipulation-via-skill-blending"},{"title":"Yuxuan Kuang","url":"https://www.catalyzex.com/author/Yuxuan%20Kuang"}]

Based on the search results, here's what I found about SkillBlender:

## SkillBlender Overview

SkillBlender is a novel hierarchical reinforcement learning framework for versatile humanoid loco-manipulation that first pretrains goal-conditioned task-agnostic primitive skills, and then dynamically blends these skills to accomplish complex loco-manipulation tasks with minimal task-specific reward engineering.

## Key Components

**Primitive Skills:** The approach first pretrains a set of goal-conditioned primitive skills that are task-agnostic, reusable, and physically interpretable. The primitive skills include Walking (conditioned on velocity command), Reaching (conditioned on wrist target positions), Squatting (conditioned on target root height), and Stepping.

**Skill Blending:** A high-level controller then learns to synthesize subgoals and per-joint weight vectors to blend these low-level skills.

## SkillBench Benchmark

SkillBlender also introduces SkillBench, a parallel, cross-embodiment, and diverse simulated benchmark containing three embodiments, four primitive skills, and eight challenging loco-manipulation tasks, accompanied by a set of scientific evaluation metrics balancing accuracy and feasibility. SkillBench includes three Unitree humanoid embodiments (H1, G1, H1-2) with varying degrees of freedom, the four primitive skills, and eight challenging whole-body loco-manipulation tasks.

## Results and Impact

SkillBlender not only achieves higher task accuracy, but also avoids reward hacking and yields more natural and feasible movements. The authors also provide a sim2real toolkit support that deploys simulation-trained primitive skill policies in the real world using a Unitree H1 humanoid robot.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4230c72b-d93b-40da-93bc-5fe990ec8f6f",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "43948802-8c8f-415b-81d3-8c1ebf198e50",
  "toolUseResult": {
    "query": "SkillBlender skill primitive compositional data generation humanoid diverse demonstration synthesis 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012jmLxDbUXwpAvWNyY1YBva",
        "content": [
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://arxiv.org/html/2506.09366v1"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "GitHub - Humanoid-SkillBlender/SkillBlender: Official implementation of SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://github.com/Humanoid-SkillBlender/SkillBlender"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Control via Skill Blending | OpenReview",
            "url": "https://openreview.net/forum?id=4MUgd8EN0F"
          },
          {
            "title": "[2506.09366] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://arxiv.org/abs/2506.09366"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending | Request PDF",
            "url": "https://www.researchgate.net/publication/392597734_SkillBlender_Towards_Versatile_Humanoid_Whole-Body_Loco-Manipulation_via_Skill_Blending"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://usc-gvl.github.io/SkillBlender-web/"
          },
          {
            "title": "Paper page - SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://huggingface.co/papers/2506.09366"
          },
          {
            "title": "[Literature Review] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://www.themoonlight.io/en/review/skillblender-towards-versatile-humanoid-whole-body-loco-manipulation-via-skill-blending"
          },
          {
            "title": "Yuxuan Kuang",
            "url": "https://www.catalyzex.com/author/Yuxuan%20Kuang"
          }
        ]
      },
      "Based on the search results, here's what I found about SkillBlender:\n\n## SkillBlender Overview\n\nSkillBlender is a novel hierarchical reinforcement learning framework for versatile humanoid loco-manipulation that first pretrains goal-conditioned task-agnostic primitive skills, and then dynamically blends these skills to accomplish complex loco-manipulation tasks with minimal task-specific reward engineering.\n\n## Key Components\n\n**Primitive Skills:** The approach first pretrains a set of goal-conditioned primitive skills that are task-agnostic, reusable, and physically interpretable. The primitive skills include Walking (conditioned on velocity command), Reaching (conditioned on wrist target positions), Squatting (conditioned on target root height), and Stepping.\n\n**Skill Blending:** A high-level controller then learns to synthesize subgoals and per-joint weight vectors to blend these low-level skills.\n\n## SkillBench Benchmark\n\nSkillBlender also introduces SkillBench, a parallel, cross-embodiment, and diverse simulated benchmark containing three embodiments, four primitive skills, and eight challenging loco-manipulation tasks, accompanied by a set of scientific evaluation metrics balancing accuracy and feasibility. SkillBench includes three Unitree humanoid embodiments (H1, G1, H1-2) with varying degrees of freedom, the four primitive skills, and eight challenging whole-body loco-manipulation tasks.\n\n## Results and Impact\n\nSkillBlender not only achieves higher task accuracy, but also avoids reward hacking and yields more natural and feasible movements. The authors also provide a sim2real toolkit support that deploys simulation-trained primitive skill policies in the real world using a Unitree H1 humanoid robot."
    ],
    "durationSeconds": 6.8011570329999085
  },
  "sourceToolAssistantUUID": "4230c72b-d93b-40da-93bc-5fe990ec8f6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-10T17:20:17.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HHGBGiEpDdxuFqpb1vccNG`</summary>

```json
{
  "query": "Isaac Lab MimicGen humanoid G1 loco-manipulation demo generation pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43948802-8c8f-415b-81d3-8c1ebf198e50",
  "isSidechain": false,
  "requestId": "req_011CauGj7VK5VGygxFDfccQF",
  "type": "assistant",
  "uuid": "54d09fc4-f657-4cb1-9519-539de4ef3070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fWu4vRuufnSwv7nuDdfGZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 78402,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 78402,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 168 · 2026-05-10T17:20:25.058Z_

<details><summary>↩ Tool result · `toolu_01HHGBGiEpDdxuFqpb1vccNG`</summary>

```text
Web search results for query: "Isaac Lab MimicGen humanoid G1 loco-manipulation demo generation pipeline 2025 2026"

Links: [{"title":"Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"},{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"Releases · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/releases"},{"title":"Release Notes — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html"},{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"Release Notes — Isaac Lab Documentation","url":"https://docs.robotsfan.com/isaaclab_official/main/source/refs/release_notes.html"},{"title":"Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/"},{"title":"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/html/2511.04831v1"},{"title":"MimicGen","url":"https://mimicgen.github.io/"},{"title":"Adds Locomanipulation Environment with G1 for Mimic workflow by michaellin6 · Pull Request #3150 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/pull/3150"}]

Based on the search results, here's what I found about Isaac Lab MimicGen humanoid G1 loco-manipulation demo generation pipeline:

## Locomanipulation Environment for G1

Isaac Lab added a new G1 humanoid environment combining RL-based locomotion with IK-based manipulation, with a full robot navigation stack integrated to augment demonstrations with randomization of tabletop pick/place locations.

## Data Generation Pipeline

By segmenting tasks into pick-navigate-place phases, this method enables generation of large-scale loco-manipulation datasets from manipulation-only demonstrations. To create a comprehensive locomanipulation dataset combining manipulation and navigation capabilities, you can generate a navigation dataset using the manipulation dataset as input, creating scenarios where the robot must navigate from one location to another while performing manipulation tasks, which creates a dataset including both locomotion and manipulation behaviors.

## Integration with MimicGen

The pipeline leverages MimicGen for synthetic data generation. The blueprint uses tools like GR00T-Mimic to generate synthetic trajectories, NVIDIA Cosmos Transfer to augment the data with photorealism, and Isaac Lab to train robot policies using imitation learning.

## Training and Deployment

The data generated from this locomanipulation pipeline can be used to finetune an imitation learning policy using GR00T N1.5 by converting the generated dataset to LeRobot format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d09fc4-f657-4cb1-9519-539de4ef3070",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "49ee9067-96ac-4ce7-8549-851cb82c8e1c",
  "toolUseResult": {
    "query": "Isaac Lab MimicGen humanoid G1 loco-manipulation demo generation pipeline 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ea9ttkESvWr5dqDQG8mDMY",
        "content": [
          {
            "title": "Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation",
            "url": "https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"
          },
          {
            "title": "Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"
          },
          {
            "title": "Releases · isaac-sim/IsaacLab",
            "url": "https://github.com/isaac-sim/IsaacLab/releases"
          },
          {
            "title": "Release Notes — Isaac Lab Documentation",
            "url": "https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html"
          },
          {
            "title": "Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"
          },
          {
            "title": "Release Notes — Isaac Lab Documentation",
            "url": "https://docs.robotsfan.com/isaaclab_official/main/source/refs/release_notes.html"
          },
          {
            "title": "Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3 | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/"
          },
          {
            "title": "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning",
            "url": "https://arxiv.org/html/2511.04831v1"
          },
          {
            "title": "MimicGen",
            "url": "https://mimicgen.github.io/"
          },
          {
            "title": "Adds Locomanipulation Environment with G1 for Mimic workflow by michaellin6 · Pull Request #3150 · isaac-sim/IsaacLab",
            "url": "https://github.com/isaac-sim/IsaacLab/pull/3150"
          }
        ]
      },
      "Based on the search results, here's what I found about Isaac Lab MimicGen humanoid G1 loco-manipulation demo generation pipeline:\n\n## Locomanipulation Environment for G1\n\nIsaac Lab added a new G1 humanoid environment combining RL-based locomotion with IK-based manipulation, with a full robot navigation stack integrated to augment demonstrations with randomization of tabletop pick/place locations.\n\n## Data Generation Pipeline\n\nBy segmenting tasks into pick-navigate-place phases, this method enables generation of large-scale loco-manipulation datasets from manipulation-only demonstrations. To create a comprehensive locomanipulation dataset combining manipulation and navigation capabilities, you can generate a navigation dataset using the manipulation dataset as input, creating scenarios where the robot must navigate from one location to another while performing manipulation tasks, which creates a dataset including both locomotion and manipulation behaviors.\n\n## Integration with MimicGen\n\nThe pipeline leverages MimicGen for synthetic data generation. The blueprint uses tools like GR00T-Mimic to generate synthetic trajectories, NVIDIA Cosmos Transfer to augment the data with photorealism, and Isaac Lab to train robot policies using imitation learning.\n\n## Training and Deployment\n\nThe data generated from this locomanipulation pipeline can be used to finetune an imitation learning policy using GR00T N1.5 by converting the generated dataset to LeRobot format."
    ],
    "durationSeconds": 7.584501094999956
  },
  "sourceToolAssistantUUID": "54d09fc4-f657-4cb1-9519-539de4ef3070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 169_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "49ee9067-96ac-4ce7-8549-851cb82c8e1c",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 170_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Tool call

_source line 171 · 2026-05-10T17:20:28.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016KEieaQtAtCSFvQNaGjuNi`</summary>

```json
{
  "query": "humanoid data generation benchmark SOTA comparison success rate 2025 2026 policy training improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49ee9067-96ac-4ce7-8549-851cb82c8e1c",
  "isSidechain": false,
  "requestId": "req_011CauGjtzG5ynRwNpVbGHP9",
  "type": "assistant",
  "uuid": "0a5a6c68-f792-4d30-996f-759bb9710e06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHdjtxfsDb4Bs8GFvPy4t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 79560,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 79560,
          "cache_creation_input_tokens": 987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 987
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

_source line 172 · 2026-05-10T17:20:39.663Z_

<details><summary>↩ Tool result · `toolu_016KEieaQtAtCSFvQNaGjuNi`</summary>

```text
Web search results for query: "humanoid data generation benchmark SOTA comparison success rate 2025 2026 policy training improvement"

Links: [{"title":"Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"CodeSOTA — Open AI Benchmark Registry and SOTA API","url":"https://www.codesota.com/browse/agentic/tool-use"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"State-of-the-Art (SOTA) AI Models: LLMs, NLP, and Computer Vision","url":"https://automatio.ai/blog/sota-models-llm-nlp/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"CoderForge-Preview: SOTA open dataset for training efficient coding agents","url":"https://www.together.ai/blog/coderforge-preview"}]

Let me search more specifically for humanoid robot data generation and policy training benchmarks.

Links: [{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"How to train generalist robots with NVIDIA's research workflows and foundation models - The Robot Report","url":"https://www.therobotreport.com/how-to-train-generalist-robots-with-nvidias-research-workflows-and-foundation-models/"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation","url":"https://arxiv.org/html/2412.13877v1"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://arxiv.org/html/2505.12705v1"},{"title":"Deep Reinforcement Learning for Real-World Humanoid Robot Locomotion Control with Automatic Reward Learning | Research","url":"https://spj.science.org/doi/10.34133/research.1123"},{"title":"Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking","url":"https://arxiv.org/html/2510.02252v1"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"Humanoid-Bench: Robotic Benchmark Suite","url":"https://www.emergentmind.com/topics/humanoid-bench"},{"title":"Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"},{"title":"Humanoid Policy ∼ Human Policy","url":"https://arxiv.org/html/2503.13441v3"}]

Based on my web search results, I found relevant information about humanoid robot data generation benchmarks and policy training improvements. Here are the key findings:

## Humanoid Data Generation and Policy Training Success Rates (2025-2026)

### DreamGen: Synthetic Data Generation for Policy Improvement

DreamGen shows consistent gains on success rate across all robots: from 37% to 46.4% on average of 4 GR1 humanoid tasks, 23% to 37% on average of 3 Franka tasks, and from 21% to 45.5% on average of 2 SO-100 tasks. This demonstrates significant improvements in policy success rates through synthetic data generation.

### GR00T N1.5 Foundation Model

GR00T N1.5 is an upgraded open foundation model for generalist humanoid robots, building on the original GR00T N1, which features a refined VLM trained on a diverse mix of real, simulated, and DreamGen-generated synthetic data. With improvements in architecture and data quality, GR00T N1.5 delivers higher success rates, better language understanding, and stronger generalization to new objects and tasks.

Even with 400 real demonstrations, the co-trained policy consistently outperformed the real-only policy by an average of 38%, demonstrating the value of synthetic data co-training.

### Humanoid Benchmarking Progress

Average success rate on tasks is approximately 51%, though in the "Insert rose into vase" task, nearly all policies achieve a 0% success rate, indicating persistent challenges in fine-grained precision manipulation.

### Synthetic Data Generation Efficiency

This new method achieves similar success rates using a combination of a few human demonstrations and synthetic data, reducing data collection time from hours to minutes, compared to traditional teleoperation approaches.

These results show that 2025-2026 research is advancing humanoid policy training through large-scale synthetic data generation, with notable improvements in both success rates and data collection efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a5a6c68-f792-4d30-996f-759bb9710e06",
  "isSidechain": false,
  "promptId": "e932f05f-18fe-48af-aee1-c7fcf07f1c66",
  "type": "user",
  "uuid": "96a818b0-f185-493c-89ba-bed865805a19",
  "toolUseResult": {
    "query": "humanoid data generation benchmark SOTA comparison success rate 2025 2026 policy training improvement",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TeHTA53vTyXf26jJEU5Gi8",
        "content": [
          {
            "title": "Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/code-generation"
          },
          {
            "title": "LLM Leaderboard 2026 — Compare Top AI Models - Vellum",
            "url": "https://www.vellum.ai/llm-leaderboard"
          },
          {
            "title": "Codesota — the open, callable registry of SOTA",
            "url": "https://www.codesota.com/"
          },
          {
            "title": "LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/llm"
          },
          {
            "title": "CodeSOTA — Open AI Benchmark Registry and SOTA API",
            "url": "https://www.codesota.com/browse/agentic/tool-use"
          },
          {
            "title": "Innovative Humanoid Robots in 2025–2026 - Reality or Hype?",
            "url": "https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"
          },
          {
            "title": "State-of-the-Art (SOTA) AI Models: LLMs, NLP, and Computer Vision",
            "url": "https://automatio.ai/blog/sota-models-llm-nlp/"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "What Are the SOTA AI Models? | Machine Learning Glossary",
            "url": "https://maddevs.io/glossary/state-of-the-art-models/"
          },
          {
            "title": "CoderForge-Preview: SOTA open dataset for training efficient coding agents",
            "url": "https://www.together.ai/blog/coderforge-preview"
          }
        ]
      },
      "Let me search more specifically for humanoid robot data generation and policy training benchmarks.",
      {
        "tool_use_id": "srvtoolu_013fbyMKPP5oAhBs4FMKAzmR",
        "content": [
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "How to train generalist robots with NVIDIA's research workflows and foundation models - The Robot Report",
            "url": "https://www.therobotreport.com/how-to-train-generalist-robots-with-nvidias-research-workflows-and-foundation-models/"
          },
          {
            "title": "RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation",
            "url": "https://arxiv.org/html/2412.13877v1"
          },
          {
            "title": "DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories",
            "url": "https://arxiv.org/html/2505.12705v1"
          },
          {
            "title": "Deep Reinforcement Learning for Real-World Humanoid Robot Locomotion Control with Automatic Reward Learning | Research",
            "url": "https://spj.science.org/doi/10.34133/research.1123"
          },
          {
            "title": "Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking",
            "url": "https://arxiv.org/html/2510.02252v1"
          },
          {
            "title": "Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation",
            "url": "https://arxiv.org/html/2510.08807v1"
          },
          {
            "title": "Humanoid-Bench: Robotic Benchmark Suite",
            "url": "https://www.emergentmind.com/topics/humanoid-bench"
          },
          {
            "title": "Building a Synthetic Motion Generation Pipeline for Humanoid Robot Learning | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/"
          },
          {
            "title": "Humanoid Policy ∼ Human Policy",
            "url": "https://arxiv.org/html/2503.13441v3"
          }
        ]
      },
      "Based on my web search results, I found relevant information about humanoid robot data generation benchmarks and policy training improvements. Here are the key findings:\n\n## Humanoid Data Generation and Policy Training Success Rates (2025-2026)\n\n### DreamGen: Synthetic Data Generation for Policy Improvement\n\nDreamGen shows consistent gains on success rate across all robots: from 37% to 46.4% on average of 4 GR1 humanoid tasks, 23% to 37% on average of 3 Franka tasks, and from 21% to 45.5% on average of 2 SO-100 tasks. This demonstrates significant improvements in policy success rates through synthetic data generation.\n\n### GR00T N1.5 Foundation Model\n\nGR00T N1.5 is an upgraded open foundation model for generalist humanoid robots, building on the original GR00T N1, which features a refined VLM trained on a diverse mix of real, simulated, and DreamGen-generated synthetic data. With improvements in architecture and data quality, GR00T N1.5 delivers higher success rates, better language understanding, and stronger generalization to new objects and tasks.\n\nEven with 400 real demonstrations, the co-trained policy consistently outperformed the real-only policy by an average of 38%, demonstrating the value of synthetic data co-training.\n\n### Humanoid Benchmarking Progress\n\nAverage success rate on tasks is approximately 51%, though in the \"Insert rose into vase\" task, nearly all policies achieve a 0% success rate, indicating persistent challenges in fine-grained precision manipulation.\n\n### Synthetic Data Generation Efficiency\n\nThis new method achieves similar success rates using a combination of a few human demonstrations and synthetic data, reducing data collection time from hours to minutes, compared to traditional teleoperation approaches.\n\nThese results show that 2025-2026 research is advancing humanoid policy training through large-scale synthetic data generation, with notable improvements in both success rates and data collection efficiency."
    ],
    "durationSeconds": 11.543003001000034
  },
  "sourceToolAssistantUUID": "0a5a6c68-f792-4d30-996f-759bb9710e06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 173 · 2026-05-10T17:23:26.772Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me synthesize my findings and identify genuine gaps.

## Key landscape insights:

1. **GR00T-Dreams/DreamGen** (NVIDIA, 2025): Video world model → synthetic trajectory generation. Fine-tunes Cosmos WFM, uses IDM for pseudo-action recovery. Shows 37→46.4% improvement on GR1 tasks. But: primarily tabletop manipulation, doesn't exploit humanoid kinematic structure.

2. **DreamControl-v2** (March 2026): Guided diffusion in motion space, aggregates human+robot data, 8 loco-manipulation tasks on G1. 

The main limitations here are reliance on retargeted human motion, task-specific constraints that need manual specification, and spatio-temporal requirements that don't generalize well.

3. **HumanoidGen** (NeurIPS 2025): LLM-based scene+demo generation for bimanual manipulation. But: focuses on bimanual dexterous manipulation only, no locomotion component.

4. **OmniRetarget** (Sept 2025): Interaction-preserving retargeting with mesh-based contact. But: this IS a retargeting method (out of scope for new contribution).

5. **WholeBodyVLA** (ICLR 2026): Latent action learning from egocentric videos. But: focuses on V

LA architecture rather than data generation itself.

6. **Isaac Lab Mimic Pipeline** (2025-2026): G1 loco-manipulation via pick-navigate-place segmentation. But: simple phase-based decomposition, limited task diversity.

7. **PSIVG** (CVPR 2026): Simulator-in-the-loop video diffusion. But: general video quality, not robot-specific.

8. **Compositional Data Generation** (Dec 2025): Factorizes transitions, self-improvement loop. But: arm manipulation only, not humanoid whole-body.

9. **SkillBlender** (June 2025): Skill blending HRL for loco-manipulation. But: focuses on policy, not data generation.

10. **Humanoid World Models** (June 2025): Lightweight egocentric world models for humanoids. But: 100 hours of data, masked transformers /

Looking at these approaches, I'm seeing a pattern where most either focus on specific manipulation types, policy learning rather than data generation, or lack the whole-body locomotion component I need. The world models approach is interesting but limited by data scale and architectural choices.

Now examining the failed directions: LocoMimicGen is too redundant with existing Isaac Lab work, physics-aware curation is just incremental filtering without real novelty, and the scene-conditioned trajectory diffusion approach seems to be heading in a direction that's already been explored.

Looking at the actual gaps, the key insight is that nobody's really exploited the humanoid's kinematic structure in trajectory diffusion — treating 40+ DoF as a monolithic action space misses the opportunity to factor it by body parts like FLAM does. A factored approach could decompose locomotion, upper-body, and hand trajectories separately, then compose them to generate novel combinations. But I'm realizing CompDiffuser and SkillBlender already handle stitching and blending, so I need to think about what's genuinely novel here.

The real distinction would be focusing on *data generation* rather than policy learning — using compositional trajectory generation to produce diverse training demonstrations by mixing locomotion and manipulation primitives, rather than learning policies that blend skills at runtime.

For the world model angle, the gap is building a humanoid-structure-aware world model that generates physically consistent whole-body trajectories for data amplification, with the kinematic tree embedded directly in the generation process instead of just converting video to pseudo-actions through an inverse dynamics model. Though I'm noticing this starts to overlap with what DreamControl-v2 already does with humanoid motion diffusion, so the distinction would need to be clearer.

The more promising direction might be applying compositional data generation to humanoid whole-body loco-manipulation — defining atomic skill primitives like walk-to, reach, grasp, squat-pick, carry, and place, then using an LLM to compose task programs from those primitives and executing them to generate trajectories with automatic physics validation. This creates a scalable pipeline without needing per-task engineering, though I should check whether HumanoidGen already covers this space.

For video generation, the gap is conditioning on humanoid kinematic state rather than treating the robot as just a visual entity — I could condition video diffusion models on rendered skeleton overlays or URDF-derived joint angles to maintain both visual realism and kinematic consistency, then recover pseudo-actions from the generated videos. Though I need to see what PSIVG does first.

The other direction is a closed-loop data flywheel where I generate trajectories, train a policy, analyze failures, and use that to guide the next generation round — automatically discovering which loco-manipulation data is most valuable. This feels somewhat incremental though.

My strongest bet is kinematic-structure-factored trajectory diffusion, where I decompose humanoid trajectory generation into body-part subtrees...

Actually, let me reconsider the second approach: fine-tuning video diffusion models with humanoid kinematic conditioning...

The key insight is grounding video generation in actual skeleton data and joint angles from the simulator, then validating outputs against physics. This differentiates from prior work like DreamGen that treats video-to-trajectory as a general problem without leveraging the specific structure of humanoid robots. With CogVideoX and OpenSora now accessible, plus Isaac Lab providing the kinematic data, there's a real opportunity to bridge the gap between video-based and simulation-based approaches—though the computational cost of video generation could be a bottleneck.

For the third direction, I'm thinking about using an LLM to orchestrate compositional task generation: breaking down complex loco-manipulation behaviors into sequences of primitives like walking, reaching, grasping, carrying, and placing, executing them through skill-based primitives in Isaac Lab, then auto-filtering the results.

The novelty here is that while HumanoidGen does LLM-based generation, it's limited to static bimanual manipulation, and Isaac Lab has pick-navigate-place but lacks compositional diversity at scale. With the G1 environment and SkillBlender primitives now available, plus LLMs that can generate task programs, this becomes feasible—though I need to be careful the differentiation from HumanoidGen is clear enough.

The fourth approach is a closed-loop flywheel: generate trajectories, train a downstream policy, analyze where it fails, and feed those failure modes back into the next generation cycle. This creates a self-improving data engine specifically for humanoid tasks, which hasn't been done before in this iterative compositional way.

Now I'm checking these ideas against my hard constraints: 200 H100-hours max, 20 days, must evaluate on Isaac Lab humanoid tasks, must be a method contribution not just a dataset, no retargeting, and has to handle loco-manipulation. This rules out training large video models from scratch and complex multi-stage pipelines. Given these limits, I'm narrowing down to the strongest 3-4 directions, starting with kinematic-tree-factored trajectory diffusion—a small diffusion model in action space that should fit within the compute budget.

The second option is LLM-orchestrated compositional data generation, which is mostly engineering work using existing Isaac Lab and SkillBlender primitives, though I need to differentiate it sharply from HumanoidGen. Third is simulator-grounded video diffusion with kinematic conditioning—conceptually novel but risky on compute since fine-tuning a video model could consume my entire budget unless I use a smaller model or efficient LoRA. The fourth direction, closed-loop policy-guided data generation, is feasible and straightforward but risks feeling incremental without the right framing.

Looking back at what's actually failed before, the pattern is clear: reviewers found holes in every submission. LocoMimicGen was too similar to existing work, the physics curation was just incremental, and the scene-conditioned trajectory diffusion overlapped with concurrent work. So I need something with genuine differentiation from what's already out there, real technical novelty beyond combining existing pieces, and something that can't be dismissed as just applying a known method to humanoids.

The kinematic-tree-factored trajectory diffusion keeps looking strongest because it's fundamentally different from how DreamControl-v2 approaches the problem—they use a monolithic trajectory model with task-specific constraints, whereas factoring by the kinematic tree structure is a different architectural choice entirely.

The real innovation here is using a graph-structured diffusion process that respects the humanoid's kinematic structure for data generation specifically, not policy learning. SkillBlender works at the policy level, and that CVPR paper on spatial-temporal graph diffusion is for bimanual manipulation policies, not full-body trajectory generation. So the differentiation holds: this is a data engine using factored diffusion for humanoid whole-body trajectories.

Now I'm considering the video diffusion direction as the second option, which seems to have potential too. I'm stepping back to identify what's actually hard in humanoid data generation. The real bottlenecks are coupled locomotion-manipulation (balance while manipulating, gait adjustment for load), generating diverse contact-rich interactions beyond tabletop tasks, scaling from manual task design to thousands of variations, and maintaining both diversity and physical plausibility across a 40+ DoF action space. Let me reformulate around these concrete problems instead.

For the first direction, I'm proposing a body-part-factored approach where I decompose the humanoid skeleton into independent kinematic chains—locomotion (hips through ankles) and manipulation (shoulders through fingers)—then train separate diffusion models on each factored subtree. The key is composing these via kinematic coupling losses at joint boundaries to ensure physical consistency, which lets me generate novel loco-manipulation combinations by mixing locomotion and manipulation patterns. This differs from prior work because DreamControl uses monolithic trajectory diffusion with per-task constraints, SkillBlender composes at the policy level rather than trajectory generation, and FLAM factorizes for multi-entity scenes rather than body parts.

For the second direction, I'm exploring a world model approach where instead of using it for planning, I leverage it as a data generation engine. I'd build on the lightweight Humanoid World Models architecture and add explicit action-conditioning through kinematic state injection, then run the model in "dream mode" to generate diverse egocentric video trajectories. The critical piece is applying an inverse dynamics model to label actions and using a learned quality classifier in a closed-loop to filter trajectories based on kinematic feasibility and task success—this is humanoid-specific unlike DreamGen.

For the third direction, I'm thinking about using an LLM to generate both task specifications and their demonstrations at scale. The LLM would compose tasks with object placements, locomotion paths, and manipulation sequences that inherently require coupled loco-manipulation behaviors like carrying while walking or pushing while moving.

I'd execute these through a hierarchical controller combining RL-based locomotion with IK-based manipulation, then validate everything through physics simulation to ensure stability and task completion. Failed tasks feed back into the LLM for parameter adjustment and improvement.

This differs from HumanoidGen because it includes locomotion and compositional structure with closed-loop refinement, whereas prior work either focuses on bimanual manipulation alone or generates tasks without the loco-manipulation coupling.

Now for the trajectory augmentation approach: I'm thinking about scaling a small set of humanoid demonstrations by perturbing them along physics-valid dimensions—object poses, initial states, approach trajectories—then using simulation to validate each perturbation for balance, contacts, and joint limits. The key difference would be learning a perturbation policy that maximizes diversity while respecting physics constraints, rather than random perturbations like MimicGen uses. Though I'm realizing this overlaps significantly with the LocoMimicGen concept I already rejected.

Let me step back and focus on the strongest directions that actually avoid repeating past work: body-part-factored compositional trajectory diffusion feels genuinely novel, LLM-driven task-trajectory co-generation addresses a clear gap in loco-manipulation that prior work missed, and a humanoid-kinematic-conditioned video world model could bridge simulation and video approaches in a humanoid-specific way. The closed-loop quality flywheel has potential but needs a stronger conceptual frame.

Now I'm thinking through how each would hold up under adversarial review—compositional skill generation is established for policies but not data generation, so that's defensible; the second needs clear technical differentiation beyond just adding locomotion to HumanoidGen; and the third requires showing that kinematic conditioning actually delivers substantial improvements over generic video models. Let me settle on the final 4 directions and start with the kinematic-tree-factored approach as the lead candidate.

The core insight is that humanoid bodies have natural hierarchical structure—legs, torso, arms, hands—that existing monolithic trajectory generators ignore. While DreamControl-v2 uses single-stage diffusion with spatio-temporal constraints and SkillBlender operates at the policy level, a graph-structured diffusion respecting the kinematic tree could compositionally generate loco-manipulation sequences by learning locomotion and manipulation distributions separately, then combining them.

Looking at the landscape, DreamControl-v2 achieves strong success rates on 29.6K samples, SkillBlender decomposes into walking and reaching primitives, and ABD-Net embeds kinematic structure into graph networks for policy learning. But the actual gap is that nobody's using kinematic-tree-structured diffusion to generate diverse training data at scale. The second opportunity is automating task generation itself—instead of manually engineering each loco-manipulation task, an LLM could orchestrate compositional primitives to create thousands of diverse task-demonstration pairs, building on approaches like HumanoidGen that handle dexterous manipulation but miss the locomotion component. Lab's G1 loco-manipulation pipeline does pick-navigate-place but with limited task variety. RoboGen generates diverse tasks for single-arm manipulation. No system automatically composes and generates diverse humanoid loco-manipulation demonstrations combining walking, reaching, carrying, and placing in novel configurations. LLMs + existing SkillBlender primitives + Isaac Lab environments create the right substrate.

**Landscape**: HumanoidGen (NeurIPS 2025): LLM+MCTS for bimanual manipulation task/demo generation, no locomotion. RoboGen: LLM-driven task generation for single-arm. CurricuLLM (ICRA 2025): LLM curricula for RL, not demo generation. Isaac Lab G1 loco-manipulation: simple pick-navigate-place pipeline. The gap: compositional loco-manipulation task-trajectory co-generation with LLM orchestration.

**Humanoid-Structure-Aware World Model as a Scalable Data Engine**: Video-based generators like DreamGen and GR00T-Dreams produce visually diverse trajectories but lack kinematic consistency for humanoids. The existing approaches fine-tune generic models and recover actions through inverse dynamics, losing humanoid-specific structure, while recent humanoid world models are limited by training data scale. I need to inject humanoid kinematic constraints directly into world model generation to create a lightweight data engine that produces both kinematically valid and visually diverse trajectories. conditioning video generation on URDF-derived kinematic state, or by operating entirely in latent kinematic space.

**Landscape**: DreamGen (May 2025): video → IDM → pseudo-actions, not humanoid-specific. Humanoid World Models (June 2025): masked transformers/flow-matching on 100h humanoid data, designed for 1-2 GPUs. PSIVG (CVPR 2026): simulator-in-the-loop for general physics, not articulated robots. EA-WM (May 2026): kinematic-to-visual action fields for world models, closest competitor. The gap: using kinematic structure directly in generation to ensure consistency, specifically for humanoid data amplification.

### 4. Closed-Loop Policy-Informed Data Generation Flywheel for Humanoid Skills
**Core problem**: Current data generation methods produce trajectories uniformly, without knowing which data distributions would most improve downstream policy performance. How can we create a self-improving data engine that generates targeted humanoid trajectories based on policy failure analysis?

**Opportunity**: Synthetic data clearly helps — DreamGen and GR00T-Dreams show improvements from 37→46.4% on GR1 tasks — but existing approaches generate data uniformly rather than focusing on where policies struggle. The iterative compositional generation work from late 2025 demonstrates self-improvement for arm manipulation, and scaling laws show data diversity matters more than volume, yet no one's applied active or curriculum-guided generation specifically to humanoid whole-body training.

**Landscape**: DreamGen generates one-shot without policy feedback. Iterative Compositional Data Generation handles self-improvement but only for arms. CurricuLLM and similar curriculum methods target RL training itself, not data generation.

I'm now confident in these four directions. Let me finalize the output. Actually, I should reconsider direction 4 more carefully — the physics-aware curation pipeline was rejected earlier, and direction 4 shares some echoes of that (quality filtering plus data selection). The real distinction is that direction 4 focuses on generation policy — what to generate next — rather than just filtering existing data. I'll keep it but make that differentiation crystal clear to preempt skeptical reviewers. Alternatively, I could pivot to an embodiment-factored video-to-trajectory bridge that conditions generation on URDF-derived kinematic state or operates in latent kinematic space instead.

Actually, I think the strongest four ideas that would survive scrutiny are the kinematic-tree-factored trajectory diffusion for highest novelty, the LLM-orchestrated compositional loco-manipulation data factory for practical impact, and the humanoid-structure-aware world model as a data engine that bridges DreamGen concepts with embodiment-specific reasoning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96a818b0-f185-493c-89ba-bed865805a19",
  "isSidechain": false,
  "requestId": "req_011CauGkykXjdopPa8z8R16E",
  "type": "assistant",
  "uuid": "612adac5-f45d-4203-a2fc-bf6b21ff5205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUNK938rSc6pMBiGwDmfMQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1530,
      "cache_read_input_tokens": 80547,
      "output_tokens": 10458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10458,
          "cache_read_input_tokens": 80547,
          "cache_creation_input_tokens": 1530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1530
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

_source line 174 · 2026-05-10T17:24:34.955Z_

I've now completed extensive research across the landscape. Let me synthesize my findings before formulating directions.

**Key landscape observations from research:**

1. **DreamControl-v2** (March 2026) is the closest competitor — uses monolithic trajectory diffusion in humanoid motion space, 8 tasks, Unitree G1, but requires per-task spatio-temporal constraints.

2. **HumanoidGen** (NeurIPS 2025) does LLM-based task+demo generation but ONLY for bimanual dexterous manipulation with static base — no locomotion.

3. **DreamGen/GR00T-Dreams** (May 2025) generates video → IDM → pseudo-actions, but treats humanoid as generic visual entity, doesn't exploit kinematic structure.

4. **OmniRetarget** (Sept 2025) is interaction-preserving data gen but IS a retargeting method (out of scope).

5. **Humanoid World Models** (June 2025) are lightweight egocentric world models but not positioned as data engines.

6. **FLAM** (Feb 2026) factorizes latent actions by entities in multi-entity scenes — body-part factorization is unexplored.

7. **ABD-Net** (March 2026), SkillBlender (June 2025), CompDiffuser (March 2025) exploit kinematic structure or compositional skills but for POLICY learning, not data GENERATION.

**Failure pattern**: All three rejected ideas failed adversarial review. LocoMimicGen was too close to DexMimicGen; Curation Pipeline was incremental; Scene-Conditioned Trajectory Diffusion overlapped with DreamControl-v2. I need ideas with clear differentiation from ALL concurrent work and sufficient standalone algorithmic novelty.

```json
[
  {
    "title": "Kinematic-Tree-Factored Trajectory Diffusion for Humanoid Data Amplification",
    "core_problem": "Monolithic trajectory generation in the 40+ DoF humanoid action space produces either low-quality or low-diversity demonstrations. How can we exploit the humanoid's tree-structured kinematics to compositionally generate diverse, physically plausible whole-body loco-manipulation trajectories for training data?",
    "opportunity": "The humanoid body has natural kinematic factorization (legs/torso/arms/hands) that no existing trajectory generator exploits for data generation. DreamControl-v2 (March 2026) uses monolithic diffusion requiring per-task spatio-temporal constraints—it cannot compositionally combine locomotion patterns with novel manipulation skills. SkillBlender (June 2025) composes skills at the policy level but cannot generate training trajectories. FLAM (Feb 2026) factorizes latent actions by scene entities but not body parts. The key 'why now': ABD-Net (March 2026) proves kinematic-tree GNNs work for humanoid control; graph diffusion exists (CVPR 2025 spatial-temporal graph diffusion for bimanual policy); the missing piece is applying graph-structured factored diffusion to trajectory DATA GENERATION, enabling compositional mixing of locomotion and manipulation distributions to produce novel loco-manipulation demonstrations at scale.",
    "landscape": "DreamControl-v2 (March 2026, arXiv:2604.00202) trains guided diffusion in G1 motion space using 29.6K retargeted samples, achieving 0.91–1.00 success on 8 tasks—but each task requires manually specified spatio-temporal constraints, limiting scalability. SkillBlender (June 2025, arXiv:2506.09366) defines walk/reach/squat/step primitives and blends them via a high-level RL controller, evaluated on SkillBench with G1/H1/H1-2—but this is policy-level composition, not trajectory generation. FLAM (Feb 2026, arXiv:2602.16229) factorizes latent actions for multi-entity scenes, improving controllable rollouts—but targets scene-level entities, not body-part kinematic subtrees. ABD-Net (March 2026, arXiv:2603.19078) embeds articulated body algorithm structure into GNNs for G1/Go2 policy learning with improved sample efficiency—demonstrating that kinematic-tree-aware architectures outperform monolithic ones. No existing work combines kinematic-tree factored diffusion with compositional trajectory generation for humanoid data amplification."
  },
  {
    "title": "LLM-Orchestrated Compositional Loco-Manipulation Data Factory",
    "core_problem": "Existing humanoid data generation pipelines require manual task engineering and produce limited task diversity. How can we automatically generate thousands of diverse, coupled loco-manipulation tasks and their corresponding demonstrations via compositional skill primitives, scaling humanoid training data without per-task human effort?",
    "opportunity": "HumanoidGen (NeurIPS 2025) uses LLM+MCTS for bimanual dexterous manipulation task generation but completely ignores locomotion—its humanoid has a static base. Isaac Lab's G1 loco-manipulation pipeline (PR#3150) segments into pick-navigate-place phases but supports only this single task template. RoboGen generates diverse tasks but for single-arm manipulation only. The gap is clear: no system automatically composes and generates diverse humanoid loco-manipulation demonstrations that couple walking with manipulation in novel configurations. The substrate now exists—Isaac Lab G1 loco-manipulation environments, SkillBlender's validated walk/reach/squat/step primitives, and LLMs that can generate compositional task programs—but nobody has connected these components into a scalable data factory. This direction requires negligible training compute (pipeline-based), making it feasible within 200 H100-hours.",
    "landscape": "HumanoidGen (NeurIPS 2025, arXiv:2507.00833) generates bimanual dexterous manipulation demonstrations using LLM reasoning with MCTS, validated on diffusion policies that scale with dataset size—but the humanoid has a fixed base with no locomotion component, fundamentally limiting the data to tabletop manipulation. Isaac Lab's G1 loco-manipulation environment (added 2025) combines RL-based locomotion with IK-based manipulation via pick-navigate-place phase segmentation—but supports only one task template with limited compositional diversity. RoboGen (NeurIPS 2023, extended 2024) uses LLMs to generate diverse tasks and scenes but only for single-arm Franka manipulation. CurricuLLM (ICRA 2025) uses LLMs to design RL training curricula including humanoid locomotion—but generates reward functions for policy training, not demonstration trajectories. DreamControl-v2 produces trajectories via diffusion but requires manual per-task spatio-temporal constraint specification. The compositional data generation paper (Dec 2025, arXiv:2512.10891) factorizes transitions for arm manipulation self-improvement—but never addresses whole-body humanoid loco-manipulation."
  },
  {
    "title": "Kinematic-Conditioned Video World Model as Humanoid Data Engine",
    "core_problem": "Video-based data generators (DreamGen, GR00T-Dreams) produce visually diverse but kinematically inconsistent humanoid trajectories, while sim-based generators produce physically valid but visually limited data. How can we build a lightweight, humanoid-structure-aware world model that generates both kinematically consistent and visually diverse trajectories specifically for humanoid data amplification?",
    "opportunity": "DreamGen/GR00T-Dreams fine-tunes Cosmos (massive compute, embodiment-agnostic architecture) and recovers actions via generic IDM—losing all humanoid kinematic structure information and producing physically implausible whole-body motions. Humanoid World Models (June 2025) are humanoid-specific and lightweight (1-2 GPUs), but are not positioned as data engines and lack explicit kinematic consistency guarantees. PSIVG (CVPR 2026) integrates physics simulation into video diffusion but targets general rigid-body physics, not articulated humanoid kinematics. EA-WM (May 2026) introduces kinematic-to-visual action fields—the closest concurrent work—but serves as a world model for control, not a data engine. The gap: conditioning video generation on URDF-derived humanoid kinematic state (joint angles, body pose rendered as skeleton overlays) to enforce kinematic consistency during generation, then extracting pseudo-actions via structure-aware IDM, creating a compute-efficient humanoid data engine.",
    "landscape": "DreamGen (May 2025, arXiv:2505.12705) fine-tunes video models on robot embodiments and recovers pseudo-actions via IDM, improving GR1 humanoid policy success from 37% to 46.4%—but treats the humanoid as a generic visual entity without kinematic awareness. Humanoid World Models (June 2025, arXiv:2506.01182) train masked transformers and flow-matching models on 100 hours of humanoid demonstrations, designed for 1-2 GPUs—but focus on next-frame prediction for planning, not scalable data generation. EA-WM (May 2026, arXiv:2605.06192) introduces structured kinematic-to-visual action fields, outperforming CogVideoX by 5.52 P3CScore points—closest concurrent work, but targets world model accuracy for control rather than data amplification. PSIVG (CVPR 2026, arXiv:2603.06408) integrates physics simulators into video diffusion for general rigid-body consistency—not designed for articulated robot kinematics. Cosmos Policy (Jan 2026, arXiv:2601.16163) achieves SOTA on LIBERO (98.5%) and RoboCasa (71.1%) via video model fine-tuning—but is embodiment-agnostic and requires massive compute."
  },
  {
    "title": "Policy-Failure-Guided Active Data Generation for Humanoid Training",
    "core_problem": "Current synthetic data generators produce trajectories uniformly without knowledge of which data distributions would most improve downstream humanoid policy performance. How can we create a closed-loop data engine that actively generates targeted humanoid trajectories based on analysis of policy failure modes, maximizing data efficiency?",
    "opportunity": "DreamGen shows synthetic data improves humanoid policy training (37→46.4%), but generates data uniformly—it cannot identify that the policy fails on carrying heavy objects while turning, and generate more of exactly that data. Recent evidence shows data diversity matters more than volume for robot policy scaling (Lin et al., 2025). The iterative compositional generation paper (Dec 2025) introduces a self-improvement loop with offline RL validation, but only for arm manipulation. No work applies active/curriculum-guided data generation specifically to humanoid whole-body training. The idea: generate trajectories → train downstream policy in sim → identify failure clusters (e.g., balance loss during reaching, collision during navigation) → parameterize failures as generation targets → generate focused data → iterate. This creates a policy-informed data flywheel rather than passive data manufacturing.",
    "landscape": "DreamGen (May 2025): one-shot synthetic trajectory generation without policy feedback, generates uniformly across task distribution. Iterative Compositional Data Generation (Dec 2025, arXiv:2512.10891) introduces self-improvement via offline RL validation on generated data—but only for single-arm tabletop manipulation, not whole-body humanoid. DreamControl-v2 (March 2026) generates trajectories per task specification with no downstream feedback loop. GR00T N1.5 co-trains on real+synthetic data showing 38% average improvement—but the synthetic data composition is manually designed, not adaptively targeted. Active learning for robotic grasping exists but has not been applied to humanoid trajectory generation. The scaling laws paper (Nov 2025, arXiv:2511.09241) shows environment/object diversity matters more than demonstration count for humanoid VLA—suggesting that targeted diverse generation should outperform uniform generation, but nobody has operationalized this insight into a closed-loop data engine."
  }
]
```

Sources:
- [DreamGen: Unlocking Generalization in Robot Learning](https://arxiv.org/abs/2505.12705)
- [DreamControl-v2: Scalable Autonomous Humanoid Skills](https://arxiv.org/html/2604.00202)
- [HumanoidGen: Data Generation via LLM Reasoning](https://arxiv.org/abs/2507.00833)
- [WholeBodyVLA: Unified Latent VLA for Loco-manipulation](https://arxiv.org/abs/2512.11047)
- [SkillBlender: Humanoid Loco-Manipulation via Skill Blending](https://arxiv.org/abs/2506.09366)
- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)
- [Humanoid World Models](https://arxiv.org/abs/2506.01182)
- [FLAM: Factored Latent Action World Models](https://arxiv.org/abs/2602.16229)
- [ABD-Net: Articulated-Body Dynamics Network](https://arxiv.org/html/2603.19078v1)
- [PSIVG: Physical Simulator In-the-Loop Video Generation](https://arxiv.org/abs/2603.06408)
- [EA-WM: Event-Aware World Model](https://arxiv.org/html/2605.06192v1)
- [Cosmos Policy: Fine-Tuning Video Models](https://arxiv.org/abs/2601.16163)
- [Isaac Lab G1 Loco-manipulation PR](https://github.com/isaac-sim/IsaacLab/pull/3150)
- [GR00T N1 Foundation Model](https://arxiv.org/html/2503.14734v2)
- [Iterative Compositional Data Generation](https://arxiv.org/html/2512.10891)
- [CompDiffuser: Trajectory Stitching via Diffusion](https://arxiv.org/html/2503.05153v1)
- [V-Dreamer: Video Generation for Trajectory Synthesis](https://arxiv.org/html/2603.18811)
- [CurricuLLM: Automatic Task Curricula](https://arxiv.org/html/2409.18382v2)
- [HumanoidBench](https://arxiv.org/abs/2403.10506)
- [Video Generation Models in Robotics Survey](https://arxiv.org/html/2601.07823v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "612adac5-f45d-4203-a2fc-bf6b21ff5205",
  "isSidechain": false,
  "requestId": "req_011CauGkykXjdopPa8z8R16E",
  "type": "assistant",
  "uuid": "b6abc85e-5d1f-4a8f-8499-70bba43d3607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUNK938rSc6pMBiGwDmfMQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1530,
      "cache_read_input_tokens": 80547,
      "output_tokens": 10458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10458,
          "cache_read_input_tokens": 80547,
          "cache_creation_input_tokens": 1530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1530
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

_source line 175_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "b6abc85e-5d1f-4a8f-8499-70bba43d3607",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 176_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 177_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-10 (UTC).** Use this when reasoni…",
  "leafUuid": "b6abc85e-5d1f-4a8f-8499-70bba43d3607",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---

### Runtime record

_source line 178_

```json
{
  "type": "ai-title",
  "aiTitle": "Research planning session for humanoid data generation",
  "sessionId": "8fe278e7-14ac-4ebd-98dc-470aaa7c69ee"
}
```

---
