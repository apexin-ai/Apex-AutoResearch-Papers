# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-17 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/1f0e797b-0a1e-4f77-9732-430b6c13ecc8.jsonl`
- **Structured JSON:** [`6182f044ac2906c4da73.json`](../../sessions/61/6182f044ac2906c4da73.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T08:43:45.544Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T08:43:45.544Z",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-17 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission. Track: Machine Learning for NLP / Question Answering.\n\nDirection: Training-time mechanistic fix for contextual entrainment — teaching LLMs to\nselectively suppress irrelevant-context influence while preserving in-context learning,\nby targeting the shared attention circuit that enables both. LLMs exhibit \"contextual\nentrainment\": attention heads mechanistically assign higher logits to ANY token previously\nseen in context, regardless of task relevance (ACL 2025, \"Llama See, Llama Do\"). This\nis the same mechanism that powers in-context learning — creating a fundamental double-bind\nwhere suppressing entrainment destroys ICL. Existing training fixes (DPO on distractor\ndata, RARE reward, data augmentation) are purely behavioral: they teach models to produce\ncorrect outputs DESPITE entrainment still occurring internally. These behavioral fixes\ndo not generalize to novel distractor types, require task-specific distractor exposure\nduring training, and fail on complex reasoning (SFT fails entirely; even RL-based RARE\nshows limited transfer). No training method targets the entrainment circuit itself to\nmake it relevance-conditional.\n\nSeed Papers:\n- \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction\n  in LLMs\" (ACL 2025) — identifies the mechanism: specific \"entrainment heads\" boost\n  logits for all context-seen tokens; these SAME heads enable in-context learning;\n  proposes inference-time head masking but no training fix\n- \"Focus Directions Make Your Language Models Pay More Attention to Relevant Contexts\"\n  (arXiv:2503.23306, Mar 2025) — identifies \"contextual heads\" and \"focus directions\"\n  in key/query space that control attention routing; proposes activation steering at\n  inference time only\n- \"Lost in the Noise: How Reasoning Models Fail with Contextual Distractors\"\n  (arXiv:2601.07226, Jan 2026) — proves SFT and outcome-reward RL FAIL for complex\n  reasoning under distraction; only RARE (rationale-aware reward) partially works;\n  reveals inverse scaling where more test-time compute worsens distraction vulnerability\n- \"How Is LLM Reasoning Distracted by Irrelevant Context?\" (EMNLP 2025 Oral,\n  arXiv:2505.18761) — GSM-DC benchmark; shows continued pretraining with distractors\n  helps on simple math but generalizes poorly; full fine-tuning > LoRA\n- \"Adaptive Distraction\" (NeurIPS 2025, arXiv:2502.01609) — DPO on synthetic adversarial\n  distractors; behavioral fix that improves robustness but does not modify the entrainment\n  circuit; requires exposure to specific distractor types during training\n- \"Reducing Distraction in Long-Context Language Models by Focused Learning\"\n  (arXiv:2411.05928, Nov 2024) — contrastive learning between full-context and\n  retrieved-relevant-only contexts; closest to mechanistic but does not specifically\n  target entrainment heads or the ICL-distraction shared circuit\n\nKnown Gaps:\n- No training method targets the ENTRAINMENT CIRCUIT (the specific attention heads\n  identified in \"Llama See, Llama Do\") — all existing fixes are behavioral\n- The fundamental double-bind is unaddressed: entrainment heads enable BOTH ICL and\n  distraction vulnerability; no principled mechanism exists to make them relevance-conditional\n- Behavioral fixes (DPO, RARE) do not generalize: they work for distractor types seen\n  during training but fail on novel distraction patterns (proven by transfer experiments)\n- SFT completely fails for complex reasoning under distraction (Jan 2026) — simple\n  data augmentation is insufficient\n- The inverse scaling finding (more test-time compute = more distraction vulnerability)\n  suggests the problem is architectural, not behavioral\n- No training loss directly penalizes the entrainment pattern while preserving the\n  ICL pattern in the same heads\n\nIn-scope: Training-time interventions that modify the entrainment circuit's behavior\nto become relevance-conditional, rather than teaching downstream reasoning to compensate.\nSpecifically: attention regularization that penalizes entrainment strength on tokens\nprovably irrelevant to the task while preserving it for relevant tokens, contrastive\nhead training where the same passage appears as relevant (for one query) and irrelevant\n(for another query) and entrainment heads must modulate accordingly, relevance-gated\nentrainment where the model learns a query-dependent gating mechanism on entrainment\nheads during training, circuit-level DPO where preferences target internal attention\npatterns (not just output correctness), progressive training from strong distractors\n(lexically unrelated) to subtle distractors (semantically adjacent but irrelevant).\n\nNOT in-scope: Inference-time activation steering (Focus Directions already does this),\npure data augmentation with distractors (proven insufficient for complex tasks), DPO/RARE\nthat only targets output behavior without modifying the entrainment mechanism, methods\nrequiring explicit relevance labels at inference time, post-hoc detection and regeneration,\nprompt engineering for distractor resistance.\n\nContribution type: METHOD ONLY. Must propose a concrete training-time intervention that\nmodifies the entrainment circuit to become relevance-conditional. The method must\ndemonstrate: (1) improved distractor robustness compared to behavioral baselines (DPO,\nRARE), (2) preserved in-context learning ability (ICL benchmarks must not degrade),\n(3) generalization to novel distractor types NOT seen during training (the key advantage\nover behavioral fixes), (4) no reliance on explicit relevance signals at inference time.\n\nEVAL PROTOCOL:\nTRAIN: Fine-tune from existing checkpoints (Llama-3-8B, Qwen2.5-7B/14B) with\nentrainment-aware training objective.\nEVALUATE on:\n- Distractor robustness: GSM-DC, GSM-NoOp, custom distractor benchmarks across\n  difficulty levels\n- ICL preservation: standard few-shot benchmarks (MMLU, BBH, ARC) must NOT degrade\n- Generalization to novel distractors: test on distractor types NOT in training data\n  (lexical, semantic, structural, adversarial)\n- Comparison against behavioral baselines: DPO (NeurIPS 2025), RARE (Jan 2026),\n  SFT on distractor data, vanilla model\n- Comparison against inference-time fixes: Focus Directions, entrainment head masking\n- Mechanistic analysis: entrainment head activation before/after training, showing\n  selective suppression for irrelevant context\n- Transfer: does fixing entrainment on math distractors transfer to reading comprehension\n  distractors? (behavioral fixes don't transfer well)\n- Ablation: which training signal components drive generalization vs. in-domain improvement\n- Inverse scaling test: does the fix resolve the \"more compute = more vulnerable\" pattern?\n\nBuilding blocks: Open models (Llama-3-8B, Qwen2.5-7B/14B), mechanistic analysis tools\n(attention head probing from \"Llama See, Llama Do\"), Focus Directions implementation\nfor comparison, GSM-DC/GSM-NoOp benchmarks, synthetic distractor generation, DPO/RLHF\ninfrastructure, ICL evaluation suites.\n\nHARD CONSTRAINTS:\nCompute: ≤200 H100-hours total. Fine-tune from existing checkpoints.\nEval: Must report BOTH distractor robustness AND ICL preservation. A method that\neliminates distraction by destroying ICL is NOT acceptable (this is the double-bind).\nMust demonstrate generalization to UNSEEN distractor types — this is the key metric\nthat distinguishes mechanistic fixes from behavioral ones.\nMust include mechanistic analysis showing entrainment head behavior change (not just\noutput accuracy improvement).\n\nLook for: Query-conditional gating on entrainment heads that learns to modulate\nentrainment strength based on query-context alignment (the heads remain active for ICL\nbut suppress for irrelevant context); contrastive training at the ATTENTION level where\nthe same document is presented as relevant-context (for query A) and irrelevant-context\n(for query B) and the model's entrainment heads must respond differently; progressive\nrelevance curriculum starting from easy discrimination (completely unrelated distractors)\nto hard discrimination (topically related but task-irrelevant context); circuit-level\npreference learning where DPO targets not just output correctness but internal attention\ndistribution over relevant vs. irrelevant context tokens.\n\nAvoid: Pure data augmentation with distractors (EMNLP 2025 already shows this is\ninsufficient), standard DPO on output behavior only (NeurIPS 2025 already does this),\ninference-time steering (Focus Directions already does this), methods that require\nknowing which context is irrelevant at inference time (must be internalized), simple\nattention regularization without query-conditioning (would destroy ICL), approaches\nthat only work on math/arithmetic distractors.\n\nIDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):\n\n1. No strawman problems: The entrainment mechanism must cite \"Llama See, Llama Do\"\n   specifically. The failure of behavioral fixes must cite \"Lost in the Noise\" (Jan 2026)\n   and NeurIPS 2025 DPO paper. The ICL-distraction shared circuit claim must be grounded\n   in the mechanistic evidence from the ACL 2025 paper.\n\n2. No observation-only ideas: Discovering new distractor failure modes is NOT a\n   contribution. Must propose a complete training method targeting the entrainment circuit.\n\n3. No mediocre methods: Your method MUST answer:\n   - Core Insight: What structural property of the entrainment circuit makes it possible\n     to selectively suppress distraction without killing ICL?\n   - Why Not Obvious: Why doesn't DPO/RARE already solve this? (Hint: they fix behavior\n     not mechanism, so they don't generalize to novel distractors)\n   - Information Exploited: What signal about \"this context is irrelevant\" do you use\n     during training that behavioral methods don't? How do you get this signal without\n     requiring relevance labels at inference time?\n   - Mechanistic Argument: From the entrainment head mechanism, explain WHY your\n     intervention makes these heads query-conditional rather than unconditionally boosting\n     all context tokens.\n   \"Add distractor data to training\" is REJECTED (EMNLP 2025 already proves this is\n   insufficient). \"Do DPO with distractor preferences\" is REJECTED (NeurIPS 2025 already\n   does this — behavioral fix). Must explain what is structurally different about your\n   approach at the CIRCUIT level.\n\n4. No rehashing: Search \"contextual entrainment training fix\", \"distraction robustness\n   training LLM\", \"attention head regularization relevance\" with 3+ queries. Differentiate\n   from: DPO distractor training (behavioral), RARE (behavioral RL), Focus Directions\n   (inference-time), data augmentation (insufficient for complex tasks).\n\n5. No experiment-padding: The insight must explain the structural relationship between\n   entrainment heads, ICL, and distraction — and why your intervention can surgically\n   modify one function (distraction) without destroying the other (ICL). This is the\n   theoretical contribution.\n\n6. Method pattern restrictions: \"Train with more distractors\" REJECTED (proven\n   insufficient). \"DPO on distractor outputs\" REJECTED (already exists, behavioral only).\n   \"Regularize attention heads\" needs justification for why this doesn't destroy ICL.\n   \"Contrastive learning\" needs explanation of what makes the contrastive signal operate\n   at the CIRCUIT level rather than the behavioral level.\n\nTHEORETICAL ANCHOR: The fundamental problem is that contextual entrainment is a\nDUAL-USE mechanism: the same attention heads that boost logits for context-seen tokens\n(causing distraction) ALSO enable in-context learning (where boosting context-seen tokens\nIS the correct behavior). The training fix must make this mechanism QUERY-CONDITIONAL:\nactive when context is relevant to the current query (ICL mode) and suppressed when\ncontext is irrelevant (distraction resistance mode). The key difficulty is that\n\"relevance\" is not a fixed property of context — the same passage can be relevant for\none query and irrelevant for another. Therefore, the gating cannot be a static property\nof the context; it must be dynamically computed from query-context interaction. Possible\napproaches: (1) train a relevance-gating layer that modulates entrainment head output\nbased on query-key alignment scores (learned during training, internalized at inference),\n(2) contrastive training at the HEAD level where the same context appears in relevant\nand irrelevant roles, forcing the model to develop query-conditional entrainment,\n(3) progressive curriculum from easy relevance discrimination to hard (topically similar\nbut task-irrelevant), (4) auxiliary loss on entrainment head attention patterns that\npenalizes uniform boosting and rewards selective boosting correlated with downstream\ntask relevance.\n\nCRITICAL DIFFERENTIATION from existing work:\n- vs. DPO/RARE (behavioral): Your method modifies the entrainment CIRCUIT, not just\n  output behavior. Key evidence: generalization to unseen distractor types.\n- vs. Focus Directions (inference-time): Your method internalizes relevance-gating\n  during training; no steering needed at inference time.\n- vs. Data augmentation (EMNLP 2025): Your method provides a TRAINING SIGNAL at the\n  attention head level, not just more examples. Key evidence: works on complex reasoning\n  where data augmentation fails.\n- vs. Entrainment head masking (ACL 2025): Your method preserves the heads but makes\n  them conditional, rather than ablating them entirely (which destroys ICL).\n\nTag: direction=contextual_entrainment_fix, contribution_type=method,\nsub_direction=relevance_conditional_entrainment, target_venues=[\"EMNLP 2026\", \"ACL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-17?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 2/10)\n{\n  \"title\": \"Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization\",\n  \"core_problem\": \"LLMs suffer catastrophic performance degradation (up to 80% on NoisyBench) when contextual distractors are injected into prompts. Mechanistic analysis ('Llama See, Llama Do,' ACL 2025) identifies specific 'entrainment heads' — attention heads that indiscriminately boost previously-seen context tokens — as the causal mechanism. Current defenses split into two paradigms with complementary weaknesses: (1) Behavioral approaches (EIT, DPO, SFT+RL) optimize output quality and can achieve strong generalization — EIT's balanced conflict RL achieves +39.1% on unseen bias types — but operate without mechanistic targeting, meaning we cannot verify WHAT internal mechanism changed, predict failure modes, or guarantee the fix addresses the root cause rather than learning compensatory output heuristics. (2) Inference-time interventions (head ablation) directly target entrainment heads with only 0.2-3% ICL cost, but provide only binary all-or-nothing suppression, require per-task head rediscovery (entrainment heads are task-specific, not model-specific), and cannot achieve graded, context-sensitive control — they suppress entrainment entirely rather than teaching the model to entrain selectively on relevant context. The gap: no approach combines the mechanistic precision of circuit-level targeting with the learned generalization of training-time optimization.\",\n  \"opportunity\": \"Three convergent opportunities enable Circuit-DPO: (1) The entrainment circuit foundation from 'Llama See, Llama Do' (ACL 2025) — differentiable masking identifies 30-110 task-specific entrainment heads that can be ablated with minimal ICL cost (0.2-3%). Crucially, this cheap ablation shows the heads are modifiable without breaking broader capabilities, but binary ablation is a blunt instrument. Training-time circuit modification can teach these heads graded, query-conditional behavior: boost relevant context, suppress distractors — something inference-time masking fundamentally cannot achieve. (2) Self-supervised attention targets are freely available in distractor-injection settings: the model's own attention patterns on clean inputs (without distractors) define the 'correct' attention distribution for entrainment heads, eliminating the need for external relevance annotations. For any task where clean/noisy input pairs can be constructed (all distractor-injection benchmarks by definition), the clean-attention pattern serves as the supervision target. (3) The DPO framework is uniquely suited for this extension — it already operates on paired preferences and avoids RL instability. Augmenting the DPO loss with an attention-distribution KL term on entrainment heads is a natural extension that propagates the preference signal through the attention mechanism during backpropagation. No existing DPO variant targets internal attention distributions. RAL (arXiv:2602.04884) optimizes attention distributions via policy gradient for multimodal perception — a different domain, method (RL not DPO), and granularity (all attention, not circuit-targeted). FPO (arXiv:2411.07618) constrains SAE feature representations during DPO but does not target attention. TI-DPO weights output tokens by importance but does not operate on internal attention patterns. Circuit-DPO is the first to bridge mechanistic interpretability (which identifies causal circuits) with preference optimization (which modifies model behavior), using circuit analysis to determine WHERE to apply attention supervision during DPO training.\",\n  \"landscape\": \"The distraction robustness landscape has matured rapidly in 2025-2026, with approaches spanning behavioral training, mechanistic analysis, and architectural modification: (1) Behavioral training methods. EIT (arXiv:2602.01528) achieves +39.1% generalization to unseen bias types (bandwagon→distraction) via balanced conflict RL that makes bias cues non-predictive of reward — the strongest OOD generalization result, but through cross-bias-type transfer (trained on one bias, tested on another), not within-distraction generalization to novel distractor implementations. Standard DPO for distraction (NeurIPS 2025, arXiv:2502.01609) achieves strong in-distribution robustness but does not evaluate OOD generalization. RARE (arXiv:2601.07226) uses rationale-aware reward shaping with limited transfer. Distractor Injection defense (arXiv:2510.16259) achieves >50-point improvement via SFT+RL on synthetic adversarial data — purely behavioral. All these methods modify behavior without targeting the entrainment mechanism, offering no mechanistic verification. (2) Mechanistic and circuit methods. 'Llama See, Llama Do' (ACL 2025) identifies and ablates entrainment heads at inference time — interpretable but binary and task-specific. CHG (NeurIPS 2025, arXiv:2505.13737) uses contrastive gating to identify separable sub-circuits (ICL vs. instruction following) and could be applied to separate entrainment circuits, but it is an analysis tool, not a training method — it identifies circuits without modifying them. Our approach uses CHG-style analysis as INPUT, then goes further by optimizing the identified circuits during preference training. (3) Architectural and representation methods. Gated Attention (NeurIPS 2025 Best Paper, arXiv:2505.06708) introduces per-head sigmoid gates as a pretraining architectural modification for all heads — orthogonal to our training-time approach that targets specific heads post-hoc. Could serve as a complementary architectural foundation. Pref-CTRL (arXiv:2604.23543) and RE-Control (NeurIPS 2024) operate on hidden-state representations, not attention distributions. 'Preference Heads' (arXiv:2604.22345) identifies causally important heads for personalization via inference-time steering — complementary but different application (style, not robustness) and phase (inference, not training). (4) Attention optimization. RAL (arXiv:2602.04884) optimizes internal attention distributions via policy gradient for multimodal LLMs — the closest conceptual relative, but differs in method (RL vs. DPO), target (all attention vs. entrainment heads), domain (multimodal perception vs. text distraction), and role (primary objective vs. auxiliary loss). Circuit-DPO occupies the unique intersection of DPO-based training, circuit-targeted intervention, and attention-level supervision — the only method that is all three.\",\n  \"approach\": \"Circuit-DPO augments the standard DPO loss with a self-supervised attention-distribution KL term operating specifically on entrainment heads. The method proceeds in four stages: (1) Entrainment head discovery. Apply the differentiable masking method from 'Llama See, Llama Do' (github.com/frankniujc/entrainment) to identify entrainment heads in Llama-3-8B and Qwen2.5-7B. The method uses Gumbel-sigmoid binary masks with straight-through estimators, optimizing learnable logit parameters per head against an entrainment-specific loss with sparsity constraints. Note: the original method was validated on Llama-3.1-8B which uses the same GQA configuration (32Q/8KV) as Llama-3-8B, so architectural transfer is direct. For Qwen2.5-7B (28Q/4KV, different GQA ratio), we mask at query-head granularity within each KV group, preserving the method's per-head resolution. (2) Self-supervised attention target construction. For each training example, construct paired clean/noisy inputs: x_clean = question + relevant context, x_noisy = question + relevant context + injected distractors. Run x_clean through the model and extract attention distributions from entrainment heads over shared context tokens (with stop-gradient). These clean-attention patterns define what entrainment heads SHOULD do even when distractors are present — attend to relevant context in the same proportional distribution. No external relevance annotations are needed; the clean/noisy pairing is inherent to all distractor-injection benchmarks. (3) Circuit-DPO training. Define the combined loss: L = L_DPO(y_chosen, y_rejected | x_noisy) + λ · Σ_{h ∈ H_ent} KL(A_h^noisy_shared || sg[A_h^clean_shared]), where A_h^noisy_shared is the attention distribution of entrainment head h on x_noisy renormalized over shared (clean-context) token positions, A_h^clean_shared is the corresponding distribution on x_clean (stop-gradient), and λ is annealed linearly from 0 over the first 20% of training to prevent early instability. The DPO loss ensures correct preference ranking; the attention KL term ensures the model achieves this by modifying HOW entrainment heads process context rather than learning compensatory output behavior. (4) Evaluation protocol. Primary: NoisyBench (arXiv:2601.07226) with held-out distractor types (train on random documents + irrelevant chat, test on hard negatives) and Adaptive Distraction benchmark (NeurIPS 2025, arXiv:2502.01609). Secondary: GSM-DC (EMNLP 2025) for math-specific distraction. Baselines: standard DPO (output-only), EIT (behavioral RL), inference-time head masking ('Llama See, Llama Do'), and a Circuit-DPO + EIT combination to test composability. Key ablations: (a) attention KL on ALL heads vs. entrainment heads only (tests whether circuit targeting matters vs. general attention regularization), (b) attention KL on random heads (controls for regularization effect), (c) varying λ magnitude. Three testable hypotheses: (H1) Circuit-DPO achieves stronger within-distraction OOD generalization than output-only DPO and inference-time masking because it modifies the causal mechanism in a graded, learned manner. (H2) Circuit-DPO is more data-efficient than EIT because it directly targets the mechanism rather than learning behavioral independence from scratch. (H3) Circuit-DPO composes with behavioral approaches — combining Circuit-DPO with EIT's balanced conflict strategy yields additive benefits.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~170h H100 80GB\",\n      \"gpu_utilization\": \"~25-35% — GPU idles during human code development, debugging, and analysis\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers (mechanistic interpretability + alignment)\",\n      \"estimated_gpu_cost\": \"$510-680 (at ~$3.00/hr H100 80GB cloud rental)\",\n      \"breakdown\": \"Head discovery: 20h (10h × 2 models). Circuit-DPO training: 60h (30h × 2 models, includes paired forward passes for clean-attention targets). Baselines (DPO, EIT replication): 50h (25h × 2 models). Ablations (3 variants): 30h (15h × 2 models). Evaluation: 10h.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~185h H100 80GB\",\n      \"gpu_utilization\": \"~55-65% — agent handles code iteration and hyperparameter sweeps, human reviews experiment designs\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing agent proposals and results\",\n      \"claude_api_cost\": \"$120-250 (1200-2500 turns for experiment planning, code generation, result analysis)\",\n      \"estimated_gpu_cost\": \"$555-740\",\n      \"risk_note\": \"Entrainment head discovery validated on Llama-3.1-8B (same GQA as Llama-3-8B); Qwen2.5-7B has different GQA ratio (28Q/4KV vs 32Q/8KV) requiring validation of masking granularity\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200h H100 80GB (maximum under compute budget; broader λ schedule search, additional ablations)\",\n      \"gpu_utilization\": \"~90-95% — agent queues experiments, runs parallel ablations on multi-GPU\",\n      \"timeline\": \"8-14 days with 4× H100 80GB\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$250-400 (2500-4000 turns including failed experiments and automated analysis)\",\n      \"estimated_gpu_cost\": \"$600-800\",\n      \"speed_bottleneck\": \"GPU count — with 4× H100, can run 2 models × 2 configurations in parallel. Paired forward passes (clean + noisy) add ~35% overhead vs. standard DPO\",\n      \"risk_note\": \"Automated entrainment head discovery may identify spurious circuits without human sanity-checking; λ schedule search may overexplore without recognizing diminishing returns\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (full paper deadline Sep 24, 2026 — primary target, 4-month timeline)\",\n    \"ARR October 2026 (submission Oct 12, 2026 — backup, feeds into NAACL 2027 or ACL 2027)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025)\",\n    \"Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning [EIT] (arXiv 2026, arXiv:2602.01528)\",\n    \"Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search (NeurIPS 2025, arXiv:2502.01609)\",\n    \"Lost in the Noise: How Reasoning Models Fail with Contextual Distractors [RARE/NoisyBench] (arXiv 2025, arXiv:2601.07226)\",\n    \"Causal Head Gating: Scalable Attention Head Interpretation [CHG] (NeurIPS 2025, arXiv:2505.13737)\",\n    \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025 Best Paper, arXiv:2505.06708)\",\n    \"Reinforced Attention Learning [RAL] (arXiv 2026, arXiv:2602.04884)\",\n    \"Distractor Injection Attacks on LLMs: Defense via SFT+RL (arXiv 2025, arXiv:2510.16259)\",\n    \"Circuit-Aware Reward Training [CART] (arXiv 2025, arXiv:2509.24713)\",\n    \"Pref-CTRL: Preference Driven LLM Alignment using Representation Editing (arXiv 2026, arXiv:2604.23543)\",\n    \"Aligning Large Language Models with Representation Editing: A Control Perspective [RE-Control] (NeurIPS 2024)\",\n    \"Direct Preference Optimization Using Sparse Feature-Level Constraints [FPO] (arXiv 2024, arXiv:2411.07618)\",\n    \"Preference Heads in Large Language Models (arXiv 2026, arXiv:2604.22345)\",\n    \"How Is LLM Reasoning Distracted by Irrelevant Context? [GSM-DC] (EMNLP 2025)\",\n    \"A Comprehensive Survey of Direct Preference Optimization (arXiv 2024, arXiv:2410.15595v3)\"\n  ],\n  \"description\": \"We propose Circuit-DPO, a preference optimization method that augments the standard DPO loss with a self-supervised attention-distribution KL divergence term operating specifically on entrainment heads — attention heads mechanistically responsible for contextual entrainment in LLMs. Unlike prior approaches that either optimize outputs without targeting the causal mechanism (EIT, standard DPO) or bluntly suppress entrainment heads at inference time (head ablation), Circuit-DPO teaches entrainment heads to maintain their clean-input attention patterns even when distractors are present, enabling graded, context-sensitive control. The attention supervision targets are self-supervised: the model's own attention distributions on clean inputs (without distractors) define what entrainment heads should do, requiring no external relevance annotations. Using differentiable masking from 'Llama See, Llama Do' to discover entrainment circuits in Llama-3-8B and Qwen2.5-7B, we train with L = L_DPO + λ·KL(A_entrainment_noisy || A_entrainment_clean) where the KL term acts only on identified entrainment heads. This bridges mechanistic interpretability (which identifies causal circuits) with preference optimization (which modifies model behavior), creating the first DPO variant that targets internal attention distributions on mechanistically-identified heads. We test three hypotheses: (1) Circuit-DPO achieves stronger within-distraction OOD generalization than output-only methods, (2) it is more data-efficient than behavioral RL approaches like EIT because it targets the mechanism directly, and (3) it composes with behavioral approaches for additive robustness. Evaluation uses NoisyBench held-out distractor types and the Adaptive Distraction benchmark.\",\n  \"project_name\": \"circuit_dpo_entrainment\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Theoretical foundation is unsupported: 'Llama See, Llama Do' (ACL 2025) shows ablating entrainment heads causes only 0.2-3% ICL degradation and explicitly states entrainment is 'task-specific, not model-specific.' The paper does NOT claim these are the same heads as ICL heads. The 'fundamental double-bind' premise that motivates the entire proposal is overstated — if entrainment heads can be cheaply ablated without ICL cost, simple inference-time masking already works and the complex training-time circuit modification is hard to justify.\", \"CRITICAL — EIT (arXiv:2602.01528) already achieves +39.1% generalization to UNSEEN distractor types through purely behavioral RL (balanced conflict strategy), directly contradicting the proposal's central claim that 'behavioral fixes don't generalize to novel distractor types.' The proposal must compare against EIT and explain what additional generalization benefit circuit-level modification provides beyond EIT's already-strong transfer.\", \"VENUE MISMATCH — User explicitly requested 'Target: EMNLP 2026, ARR submission' but the proposal targets ICLR 2027 (Sep 24, 2026) and AAAI 2027 (Aug 2, 2026). The EMNLP 2026 ARR deadline is May 25, 2026 — 8 days away, making it infeasible for a 3-4 month project.\", \"ARCHITECTURE RISK — Qwen3-8B uses Grouped Query Attention (32 query heads, 8 KV heads), fundamentally different from Llama-3.1-8B's standard MHA (32 query/32 KV heads). The differentiable masking method from 'Llama See, Llama Do' was developed for standard MHA. Transfer to GQA is non-trivial and unvalidated — which head granularity do you mask, query heads or KV heads?\", \"MODEL MISMATCH — User constraints specify 'Llama-3-8B, Qwen2.5-7B/14B' but the proposal uses Qwen3-8B, a different model family.\", \"MISSING COMPETITOR — Causal Head Gating (CHG, NeurIPS 2025, arXiv:2505.13737) already uses contrastive gating to identify separable sub-circuits for ICL vs. instruction following. Contrastive CHG could be directly applied to separate entrainment-for-ICL from entrainment-for-distraction circuits, making it a very close competitor.\", \"MISSING COMPETITOR — Gated Attention (NeurIPS 2025 Best Paper) introduces query-dependent sigmoid gates on attention heads — architecturally similar to the proposed 'relevance-gated entrainment.' Must discuss.\", \"MISSING COMPETITOR — Distractor Injection Attacks defense (arXiv:2510.16259) achieves >50 point robustness improvement through SFT+RL on synthetic adversarial data.\", \"ATTENTION TARGET CONSTRUCTION — The method requires knowing which context tokens are 'question-relevant' to construct attention supervision targets for 'chosen' responses. This effectively requires relevance annotations during training. For math (GSM-DC), this is straightforward, but for general NLP tasks, relevance boundaries are ambiguous. The proposal doesn't address how to scale this beyond tasks with clear relevant/irrelevant context boundaries.\", \"RESOURCE INCONSISTENCY — User's hard constraint is '≤200 H100-hours total' but the resource estimate lists 250-500 A100-80GB hours. Even accounting for H100 vs A100 speed difference (~1.5-2x), the lower bound of 250 A100-hours ≈ 125-170 H100-hours is tight, and the upper bound of 500 A100-hours ≈ 250-330 H100-hours exceeds the constraint.\"]\nFeedback: The proposal has a well-crafted method formulation (Circuit-DPO loss = L_DPO + λ·KL(attn_entrainment || attn_target)) but is built on a shaky theoretical foundation. To revise successfully:\n\n1. **Fix the theoretical premise**: Drop or weaken the 'shared circuit double-bind' claim. 'Llama See, Llama Do' actually shows entrainment heads CAN be ablated with minimal ICL cost (0.2-3%). Reframe: instead of 'we must solve the double-bind,' argue that inference-time masking is a blunt instrument (all-or-nothing suppression) and training-time circuit modification enables GRADED, query-conditional entrainment that inference-time masking cannot achieve. This is a weaker but defensible claim.\n\n2. **Add EIT as primary baseline**: EIT's 39.1% unseen-distraction generalization through behavioral RL is the strongest counterevidence to your motivation. You MUST compare against it and demonstrate that Circuit-DPO achieves stronger OOD generalization OR additional benefits (mechanistic interpretability, no RL instability, etc.).\n\n3. **Fix the venue**: Target EMNLP 2026 ARR or adjust timeline. Given the research takes 3-4 months, the earliest feasible ARR cycle would be around September 2026 — check which venues accept that cycle.\n\n4. **Use user-specified models**: Switch to Llama-3-8B and Qwen2.5-7B/14B as requested, which also avoids the GQA architecture issue (Llama-3-8B uses standard MHA with GQA, but Qwen2.5 is closer to what the masking method was tested on).\n\n5. **Address attention target construction**: Explicitly describe how relevance annotations are generated for training data. Options: (a) use tasks with synthetic distractors where relevance is known by construction, (b) use retrieval models to score relevance, (c) use attention patterns from correct reasoning traces as pseudo-labels.\n\n6. **Discuss CHG and Gated Attention**: CHG (NeurIPS 2025) and Gated Attention (NeurIPS 2025 Best Paper) are close competitors. Differentiate clearly.\n\n7. **Tighten resource estimates**: Stay within ≤200 H100-hours. Reduce scope if needed (e.g., 1-2 model sizes instead of full sweep).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-17T08:43:45.548Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T08:43:45.548Z",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-17T08:43:45.584Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-17 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission. Track: Machine Learning for NLP / Question Answering.

Direction: Training-time mechanistic fix for contextual entrainment — teaching LLMs to
selectively suppress irrelevant-context influence while preserving in-context learning,
by targeting the shared attention circuit that enables both. LLMs exhibit "contextual
entrainment": attention heads mechanistically assign higher logits to ANY token previously
seen in context, regardless of task relevance (ACL 2025, "Llama See, Llama Do"). This
is the same mechanism that powers in-context learning — creating a fundamental double-bind
where suppressing entrainment destroys ICL. Existing training fixes (DPO on distractor
data, RARE reward, data augmentation) are purely behavioral: they teach models to produce
correct outputs DESPITE entrainment still occurring internally. These behavioral fixes
do not generalize to novel distractor types, require task-specific distractor exposure
during training, and fail on complex reasoning (SFT fails entirely; even RL-based RARE
shows limited transfer). No training method targets the entrainment circuit itself to
make it relevance-conditional.

Seed Papers:
- "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction
  in LLMs" (ACL 2025) — identifies the mechanism: specific "entrainment heads" boost
  logits for all context-seen tokens; these SAME heads enable in-context learning;
  proposes inference-time head masking but no training fix
- "Focus Directions Make Your Language Models Pay More Attention to Relevant Contexts"
  (arXiv:2503.23306, Mar 2025) — identifies "contextual heads" and "focus directions"
  in key/query space that control attention routing; proposes activation steering at
  inference time only
- "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors"
  (arXiv:2601.07226, Jan 2026) — proves SFT and outcome-reward RL FAIL for complex
  reasoning under distraction; only RARE (rationale-aware reward) partially works;
  reveals inverse scaling where more test-time compute worsens distraction vulnerability
- "How Is LLM Reasoning Distracted by Irrelevant Context?" (EMNLP 2025 Oral,
  arXiv:2505.18761) — GSM-DC benchmark; shows continued pretraining with distractors
  helps on simple math but generalizes poorly; full fine-tuning > LoRA
- "Adaptive Distraction" (NeurIPS 2025, arXiv:2502.01609) — DPO on synthetic adversarial
  distractors; behavioral fix that improves robustness but does not modify the entrainment
  circuit; requires exposure to specific distractor types during training
- "Reducing Distraction in Long-Context Language Models by Focused Learning"
  (arXiv:2411.05928, Nov 2024) — contrastive learning between full-context and
  retrieved-relevant-only contexts; closest to mechanistic but does not specifically
  target entrainment heads or the ICL-distraction shared circuit

Known Gaps:
- No training method targets the ENTRAINMENT CIRCUIT (the specific attention heads
  identified in "Llama See, Llama Do") — all existing fixes are behavioral
- The fundamental double-bind is unaddressed: entrainment heads enable BOTH ICL and
  distraction vulnerability; no principled mechanism exists to make them relevance-conditional
- Behavioral fixes (DPO, RARE) do not generalize: they work for distractor types seen
  during training but fail on novel distraction patterns (proven by transfer experiments)
- SFT completely fails for complex reasoning under distraction (Jan 2026) — simple
  data augmentation is insufficient
- The inverse scaling finding (more test-time compute = more distraction vulnerability)
  suggests the problem is architectural, not behavioral
- No training loss directly penalizes the entrainment pattern while preserving the
  ICL pattern in the same heads

In-scope: Training-time interventions that modify the entrainment circuit's behavior
to become relevance-conditional, rather than teaching downstream reasoning to compensate.
Specifically: attention regularization that penalizes entrainment strength on tokens
provably irrelevant to the task while preserving it for relevant tokens, contrastive
head training where the same passage appears as relevant (for one query) and irrelevant
(for another query) and entrainment heads must modulate accordingly, relevance-gated
entrainment where the model learns a query-dependent gating mechanism on entrainment
heads during training, circuit-level DPO where preferences target internal attention
patterns (not just output correctness), progressive training from strong distractors
(lexically unrelated) to subtle distractors (semantically adjacent but irrelevant).

NOT in-scope: Inference-time activation steering (Focus Directions already does this),
pure data augmentation with distractors (proven insufficient for complex tasks), DPO/RARE
that only targets output behavior without modifying the entrainment mechanism, methods
requiring explicit relevance labels at inference time, post-hoc detection and regeneration,
prompt engineering for distractor resistance.

Contribution type: METHOD ONLY. Must propose a concrete training-time intervention that
modifies the entrainment circuit to become relevance-conditional. The method must
demonstrate: (1) improved distractor robustness compared to behavioral baselines (DPO,
RARE), (2) preserved in-context learning ability (ICL benchmarks must not degrade),
(3) generalization to novel distractor types NOT seen during training (the key advantage
over behavioral fixes), (4) no reliance on explicit relevance signals at inference time.

EVAL PROTOCOL:
TRAIN: Fine-tune from existing checkpoints (Llama-3-8B, Qwen2.5-7B/14B) with
entrainment-aware training objective.
EVALUATE on:
- Distractor robustness: GSM-DC, GSM-NoOp, custom distractor benchmarks across
  difficulty levels
- ICL preservation: standard few-shot benchmarks (MMLU, BBH, ARC) must NOT degrade
- Generalization to novel distractors: test on distractor types NOT in training data
  (lexical, semantic, structural, adversarial)
- Comparison against behavioral baselines: DPO (NeurIPS 2025), RARE (Jan 2026),
  SFT on distractor data, vanilla model
- Comparison against inference-time fixes: Focus Directions, entrainment head masking
- Mechanistic analysis: entrainment head activation before/after training, showing
  selective suppression for irrelevant context
- Transfer: does fixing entrainment on math distractors transfer to reading comprehension
  distractors? (behavioral fixes don't transfer well)
- Ablation: which training signal components drive generalization vs. in-domain improvement
- Inverse scaling test: does the fix resolve the "more compute = more vulnerable" pattern?

Building blocks: Open models (Llama-3-8B, Qwen2.5-7B/14B), mechanistic analysis tools
(attention head probing from "Llama See, Llama Do"), Focus Directions implementation
for comparison, GSM-DC/GSM-NoOp benchmarks, synthetic distractor generation, DPO/RLHF
infrastructure, ICL evaluation suites.

HARD CONSTRAINTS:
Compute: ≤200 H100-hours total. Fine-tune from existing checkpoints.
Eval: Must report BOTH distractor robustness AND ICL preservation. A method that
eliminates distraction by destroying ICL is NOT acceptable (this is the double-bind).
Must demonstrate generalization to UNSEEN distractor types — this is the key metric
that distinguishes mechanistic fixes from behavioral ones.
Must include mechanistic analysis showing entrainment head behavior change (not just
output accuracy improvement).

Look for: Query-conditional gating on entrainment heads that learns to modulate
entrainment strength based on query-context alignment (the heads remain active for ICL
but suppress for irrelevant context); contrastive training at the ATTENTION level where
the same document is presented as relevant-context (for query A) and irrelevant-context
(for query B) and the model's entrainment heads must respond differently; progressive
relevance curriculum starting from easy discrimination (completely unrelated distractors)
to hard discrimination (topically related but task-irrelevant context); circuit-level
preference learning where DPO targets not just output correctness but internal attention
distribution over relevant vs. irrelevant context tokens.

Avoid: Pure data augmentation with distractors (EMNLP 2025 already shows this is
insufficient), standard DPO on output behavior only (NeurIPS 2025 already does this),
inference-time steering (Focus Directions already does this), methods that require
knowing which context is irrelevant at inference time (must be internalized), simple
attention regularization without query-conditioning (would destroy ICL), approaches
that only work on math/arithmetic distractors.

IDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):

1. No strawman problems: The entrainment mechanism must cite "Llama See, Llama Do"
   specifically. The failure of behavioral fixes must cite "Lost in the Noise" (Jan 2026)
   and NeurIPS 2025 DPO paper. The ICL-distraction shared circuit claim must be grounded
   in the mechanistic evidence from the ACL 2025 paper.

2. No observation-only ideas: Discovering new distractor failure modes is NOT a
   contribution. Must propose a complete training method targeting the entrainment circuit.

3. No mediocre methods: Your method MUST answer:
   - Core Insight: What structural property of the entrainment circuit makes it possible
     to selectively suppress distraction without killing ICL?
   - Why Not Obvious: Why doesn't DPO/RARE already solve this? (Hint: they fix behavior
     not mechanism, so they don't generalize to novel distractors)
   - Information Exploited: What signal about "this context is irrelevant" do you use
     during training that behavioral methods don't? How do you get this signal without
     requiring relevance labels at inference time?
   - Mechanistic Argument: From the entrainment head mechanism, explain WHY your
     intervention makes these heads query-conditional rather than unconditionally boosting
     all context tokens.
   "Add distractor data to training" is REJECTED (EMNLP 2025 already proves this is
   insufficient). "Do DPO with distractor preferences" is REJECTED (NeurIPS 2025 already
   does this — behavioral fix). Must explain what is structurally different about your
   approach at the CIRCUIT level.

4. No rehashing: Search "contextual entrainment training fix", "distraction robustness
   training LLM", "attention head regularization relevance" with 3+ queries. Differentiate
   from: DPO distractor training (behavioral), RARE (behavioral RL), Focus Directions
   (inference-time), data augmentation (insufficient for complex tasks).

5. No experiment-padding: The insight must explain the structural relationship between
   entrainment heads, ICL, and distraction — and why your intervention can surgically
   modify one function (distraction) without destroying the other (ICL). This is the
   theoretical contribution.

6. Method pattern restrictions: "Train with more distractors" REJECTED (proven
   insufficient). "DPO on distractor outputs" REJECTED (already exists, behavioral only).
   "Regularize attention heads" needs justification for why this doesn't destroy ICL.
   "Contrastive learning" needs explanation of what makes the contrastive signal operate
   at the CIRCUIT level rather than the behavioral level.

THEORETICAL ANCHOR: The fundamental problem is that contextual entrainment is a
DUAL-USE mechanism: the same attention heads that boost logits for context-seen tokens
(causing distraction) ALSO enable in-context learning (where boosting context-seen tokens
IS the correct behavior). The training fix must make this mechanism QUERY-CONDITIONAL:
active when context is relevant to the current query (ICL mode) and suppressed when
context is irrelevant (distraction resistance mode). The key difficulty is that
"relevance" is not a fixed property of context — the same passage can be relevant for
one query and irrelevant for another. Therefore, the gating cannot be a static property
of the context; it must be dynamically computed from query-context interaction. Possible
approaches: (1) train a relevance-gating layer that modulates entrainment head output
based on query-key alignment scores (learned during training, internalized at inference),
(2) contrastive training at the HEAD level where the same context appears in relevant
and irrelevant roles, forcing the model to develop query-conditional entrainment,
(3) progressive curriculum from easy relevance discrimination to hard (topically similar
but task-irrelevant), (4) auxiliary loss on entrainment head attention patterns that
penalizes uniform boosting and rewards selective boosting correlated with downstream
task relevance.

CRITICAL DIFFERENTIATION from existing work:
- vs. DPO/RARE (behavioral): Your method modifies the entrainment CIRCUIT, not just
  output behavior. Key evidence: generalization to unseen distractor types.
- vs. Focus Directions (inference-time): Your method internalizes relevance-gating
  during training; no steering needed at inference time.
- vs. Data augmentation (EMNLP 2025): Your method provides a TRAINING SIGNAL at the
  attention head level, not just more examples. Key evidence: works on complex reasoning
  where data augmentation fails.
- vs. Entrainment head masking (ACL 2025): Your method preserves the heads but makes
  them conditional, rather than ablating them entirely (which destroys ICL).

Tag: direction=contextual_entrainment_fix, contribution_type=method,
sub_direction=relevance_conditional_entrainment, target_venues=["EMNLP 2026", "ACL 2026"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-17?
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
  "title": "Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization",
  "core_problem": "LLMs suffer catastrophic performance degradation (up to 80% on NoisyBench) when contextual distractors are injected into prompts. Mechanistic analysis ('Llama See, Llama Do,' ACL 2025) identifies specific 'entrainment heads' — attention heads that indiscriminately boost previously-seen context tokens — as the causal mechanism. Current defenses split into two paradigms with complementary weaknesses: (1) Behavioral approaches (EIT, DPO, SFT+RL) optimize output quality and can achieve strong generalization — EIT's balanced conflict RL achieves +39.1% on unseen bias types — but operate without mechanistic targeting, meaning we cannot verify WHAT internal mechanism changed, predict failure modes, or guarantee the fix addresses the root cause rather than learning compensatory output heuristics. (2) Inference-time interventions (head ablation) directly target entrainment heads with only 0.2-3% ICL cost, but provide only binary all-or-nothing suppression, require per-task head rediscovery (entrainment heads are task-specific, not model-specific), and cannot achieve graded, context-sensitive control — they suppress entrainment entirely rather than teaching the model to entrain selectively on relevant context. The gap: no approach combines the mechanistic precision of circuit-level targeting with the learned generalization of training-time optimization.",
  "opportunity": "Three convergent opportunities enable Circuit-DPO: (1) The entrainment circuit foundation from 'Llama See, Llama Do' (ACL 2025) — differentiable masking identifies 30-110 task-specific entrainment heads that can be ablated with minimal ICL cost (0.2-3%). Crucially, this cheap ablation shows the heads are modifiable without breaking broader capabilities, but binary ablation is a blunt instrument. Training-time circuit modification can teach these heads graded, query-conditional behavior: boost relevant context, suppress distractors — something inference-time masking fundamentally cannot achieve. (2) Self-supervised attention targets are freely available in distractor-injection settings: the model's own attention patterns on clean inputs (without distractors) define the 'correct' attention distribution for entrainment heads, eliminating the need for external relevance annotations. For any task where clean/noisy input pairs can be constructed (all distractor-injection benchmarks by definition), the clean-attention pattern serves as the supervision target. (3) The DPO framework is uniquely suited for this extension — it already operates on paired preferences and avoids RL instability. Augmenting the DPO loss with an attention-distribution KL term on entrainment heads is a natural extension that propagates the preference signal through the attention mechanism during backpropagation. No existing DPO variant targets internal attention distributions. RAL (arXiv:2602.04884) optimizes attention distributions via policy gradient for multimodal perception — a different domain, method (RL not DPO), and granularity (all attention, not circuit-targeted). FPO (arXiv:2411.07618) constrains SAE feature representations during DPO but does not target attention. TI-DPO weights output tokens by importance but does not operate on internal attention patterns. Circuit-DPO is the first to bridge mechanistic interpretability (which identifies causal circuits) with preference optimization (which modifies model behavior), using circuit analysis to determine WHERE to apply attention supervision during DPO training.",
  "landscape": "The distraction robustness landscape has matured rapidly in 2025-2026, with approaches spanning behavioral training, mechanistic analysis, and architectural modification: (1) Behavioral training methods. EIT (arXiv:2602.01528) achieves +39.1% generalization to unseen bias types (bandwagon→distraction) via balanced conflict RL that makes bias cues non-predictive of reward — the strongest OOD generalization result, but through cross-bias-type transfer (trained on one bias, tested on another), not within-distraction generalization to novel distractor implementations. Standard DPO for distraction (NeurIPS 2025, arXiv:2502.01609) achieves strong in-distribution robustness but does not evaluate OOD generalization. RARE (arXiv:2601.07226) uses rationale-aware reward shaping with limited transfer. Distractor Injection defense (arXiv:2510.16259) achieves >50-point improvement via SFT+RL on synthetic adversarial data — purely behavioral. All these methods modify behavior without targeting the entrainment mechanism, offering no mechanistic verification. (2) Mechanistic and circuit methods. 'Llama See, Llama Do' (ACL 2025) identifies and ablates entrainment heads at inference time — interpretable but binary and task-specific. CHG (NeurIPS 2025, arXiv:2505.13737) uses contrastive gating to identify separable sub-circuits (ICL vs. instruction following) and could be applied to separate entrainment circuits, but it is an analysis tool, not a training method — it identifies circuits without modifying them. Our approach uses CHG-style analysis as INPUT, then goes further by optimizing the identified circuits during preference training. (3) Architectural and representation methods. Gated Attention (NeurIPS 2025 Best Paper, arXiv:2505.06708) introduces per-head sigmoid gates as a pretraining architectural modification for all heads — orthogonal to our training-time approach that targets specific heads post-hoc. Could serve as a complementary architectural foundation. Pref-CTRL (arXiv:2604.23543) and RE-Control (NeurIPS 2024) operate on hidden-state representations, not attention distributions. 'Preference Heads' (arXiv:2604.22345) identifies causally important heads for personalization via inference-time steering — complementary but different application (style, not robustness) and phase (inference, not training). (4) Attention optimization. RAL (arXiv:2602.04884) optimizes internal attention distributions via policy gradient for multimodal LLMs — the closest conceptual relative, but differs in method (RL vs. DPO), target (all attention vs. entrainment heads), domain (multimodal perception vs. text distraction), and role (primary objective vs. auxiliary loss). Circuit-DPO occupies the unique intersection of DPO-based training, circuit-targeted intervention, and attention-level supervision — the only method that is all three.",
  "approach": "Circuit-DPO augments the standard DPO loss with a self-supervised attention-distribution KL term operating specifically on entrainment heads. The method proceeds in four stages: (1) Entrainment head discovery. Apply the differentiable masking method from 'Llama See, Llama Do' (github.com/frankniujc/entrainment) to identify entrainment heads in Llama-3-8B and Qwen2.5-7B. The method uses Gumbel-sigmoid binary masks with straight-through estimators, optimizing learnable logit parameters per head against an entrainment-specific loss with sparsity constraints. Note: the original method was validated on Llama-3.1-8B which uses the same GQA configuration (32Q/8KV) as Llama-3-8B, so architectural transfer is direct. For Qwen2.5-7B (28Q/4KV, different GQA ratio), we mask at query-head granularity within each KV group, preserving the method's per-head resolution. (2) Self-supervised attention target construction. For each training example, construct paired clean/noisy inputs: x_clean = question + relevant context, x_noisy = question + relevant context + injected distractors. Run x_clean through the model and extract attention distributions from entrainment heads over shared context tokens (with stop-gradient). These clean-attention patterns define what entrainment heads SHOULD do even when distractors are present — attend to relevant context in the same proportional distribution. No external relevance annotations are needed; the clean/noisy pairing is inherent to all distractor-injection benchmarks. (3) Circuit-DPO training. Define the combined loss: L = L_DPO(y_chosen, y_rejected | x_noisy) + λ · Σ_{h ∈ H_ent} KL(A_h^noisy_shared || sg[A_h^clean_shared]), where A_h^noisy_shared is the attention distribution of entrainment head h on x_noisy renormalized over shared (clean-context) token positions, A_h^clean_shared is the corresponding distribution on x_clean (stop-gradient), and λ is annealed linearly from 0 over the first 20% of training to prevent early instability. The DPO loss ensures correct preference ranking; the attention KL term ensures the model achieves this by modifying HOW entrainment heads process context rather than learning compensatory output behavior. (4) Evaluation protocol. Primary: NoisyBench (arXiv:2601.07226) with held-out distractor types (train on random documents + irrelevant chat, test on hard negatives) and Adaptive Distraction benchmark (NeurIPS 2025, arXiv:2502.01609). Secondary: GSM-DC (EMNLP 2025) for math-specific distraction. Baselines: standard DPO (output-only), EIT (behavioral RL), inference-time head masking ('Llama See, Llama Do'), and a Circuit-DPO + EIT combination to test composability. Key ablations: (a) attention KL on ALL heads vs. entrainment heads only (tests whether circuit targeting matters vs. general attention regularization), (b) attention KL on random heads (controls for regularization effect), (c) varying λ magnitude. Three testable hypotheses: (H1) Circuit-DPO achieves stronger within-distraction OOD generalization than output-only DPO and inference-time masking because it modifies the causal mechanism in a graded, learned manner. (H2) Circuit-DPO is more data-efficient than EIT because it directly targets the mechanism rather than learning behavioral independence from scratch. (H3) Circuit-DPO composes with behavioral approaches — combining Circuit-DPO with EIT's balanced conflict strategy yields additive benefits.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~170h H100 80GB",
      "gpu_utilization": "~25-35% — GPU idles during human code development, debugging, and analysis",
      "timeline": "3-4 months",
      "team": "1-2 researchers (mechanistic interpretability + alignment)",
      "estimated_gpu_cost": "$510-680 (at ~$3.00/hr H100 80GB cloud rental)",
      "breakdown": "Head discovery: 20h (10h × 2 models). Circuit-DPO training: 60h (30h × 2 models, includes paired forward passes for clean-attention targets). Baselines (DPO, EIT replication): 50h (25h × 2 models). Ablations (3 variants): 30h (15h × 2 models). Evaluation: 10h."
    },
    "human_in_loop": {
      "gpu_hours": "~185h H100 80GB",
      "gpu_utilization": "~55-65% — agent handles code iteration and hyperparameter sweeps, human reviews experiment designs",
      "timeline": "6-8 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals and results",
      "claude_api_cost": "$120-250 (1200-2500 turns for experiment planning, code generation, result analysis)",
      "estimated_gpu_cost": "$555-740",
      "risk_note": "Entrainment head discovery validated on Llama-3.1-8B (same GQA as Llama-3-8B); Qwen2.5-7B has different GQA ratio (28Q/4KV vs 32Q/8KV) requiring validation of masking granularity"
    },
    "auto_research": {
      "gpu_hours": "~200h H100 80GB (maximum under compute budget; broader λ schedule search, additional ablations)",
      "gpu_utilization": "~90-95% — agent queues experiments, runs parallel ablations on multi-GPU",
      "timeline": "8-14 days with 4× H100 80GB",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$250-400 (2500-4000 turns including failed experiments and automated analysis)",
      "estimated_gpu_cost": "$600-800",
      "speed_bottleneck": "GPU count — with 4× H100, can run 2 models × 2 configurations in parallel. Paired forward passes (clean + noisy) add ~35% overhead vs. standard DPO",
      "risk_note": "Automated entrainment head discovery may identify spurious circuits without human sanity-checking; λ schedule search may overexplore without recognizing diminishing returns"
    }
  },
  "target_venues": [
    "ICLR 2027 (full paper deadline Sep 24, 2026 — primary target, 4-month timeline)",
    "ARR October 2026 (submission Oct 12, 2026 — backup, feeds into NAACL 2027 or ACL 2027)"
  ],
  "level": "top-tier",
  "key_references": [
    "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025)",
    "Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning [EIT] (arXiv 2026, arXiv:2602.01528)",
    "Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search (NeurIPS 2025, arXiv:2502.01609)",
    "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors [RARE/NoisyBench] (arXiv 2025, arXiv:2601.07226)",
    "Causal Head Gating: Scalable Attention Head Interpretation [CHG] (NeurIPS 2025, arXiv:2505.13737)",
    "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025 Best Paper, arXiv:2505.06708)",
    "Reinforced Attention Learning [RAL] (arXiv 2026, arXiv:2602.04884)",
    "Distractor Injection Attacks on LLMs: Defense via SFT+RL (arXiv 2025, arXiv:2510.16259)",
    "Circuit-Aware Reward Training [CART] (arXiv 2025, arXiv:2509.24713)",
    "Pref-CTRL: Preference Driven LLM Alignment using Representation Editing (arXiv 2026, arXiv:2604.23543)",
    "Aligning Large Language Models with Representation Editing: A Control Perspective [RE-Control] (NeurIPS 2024)",
    "Direct Preference Optimization Using Sparse Feature-Level Constraints [FPO] (arXiv 2024, arXiv:2411.07618)",
    "Preference Heads in Large Language Models (arXiv 2026, arXiv:2604.22345)",
    "How Is LLM Reasoning Distracted by Irrelevant Context? [GSM-DC] (EMNLP 2025)",
    "A Comprehensive Survey of Direct Preference Optimization (arXiv 2024, arXiv:2410.15595v3)"
  ],
  "description": "We propose Circuit-DPO, a preference optimization method that augments the standard DPO loss with a self-supervised attention-distribution KL divergence term operating specifically on entrainment heads — attention heads mechanistically responsible for contextual entrainment in LLMs. Unlike prior approaches that either optimize outputs without targeting the causal mechanism (EIT, standard DPO) or bluntly suppress entrainment heads at inference time (head ablation), Circuit-DPO teaches entrainment heads to maintain their clean-input attention patterns even when distractors are present, enabling graded, context-sensitive control. The attention supervision targets are self-supervised: the model's own attention distributions on clean inputs (without distractors) define what entrainment heads should do, requiring no external relevance annotations. Using differentiable masking from 'Llama See, Llama Do' to discover entrainment circuits in Llama-3-8B and Qwen2.5-7B, we train with L = L_DPO + λ·KL(A_entrainment_noisy || A_entrainment_clean) where the KL term acts only on identified entrainment heads. This bridges mechanistic interpretability (which identifies causal circuits) with preference optimization (which modifies model behavior), creating the first DPO variant that targets internal attention distributions on mechanistically-identified heads. We test three hypotheses: (1) Circuit-DPO achieves stronger within-distraction OOD generalization than output-only methods, (2) it is more data-efficient than behavioral RL approaches like EIT because it targets the mechanism directly, and (3) it composes with behavioral approaches for additive robustness. Evaluation uses NoisyBench held-out distractor types and the Adaptive Distraction benchmark.",
  "project_name": "circuit_dpo_entrainment",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — Theoretical foundation is unsupported: 'Llama See, Llama Do' (ACL 2025) shows ablating entrainment heads causes only 0.2-3% ICL degradation and explicitly states entrainment is 'task-specific, not model-specific.' The paper does NOT claim these are the same heads as ICL heads. The 'fundamental double-bind' premise that motivates the entire proposal is overstated — if entrainment heads can be cheaply ablated without ICL cost, simple inference-time masking already works and the complex training-time circuit modification is hard to justify.", "CRITICAL — EIT (arXiv:2602.01528) already achieves +39.1% generalization to UNSEEN distractor types through purely behavioral RL (balanced conflict strategy), directly contradicting the proposal's central claim that 'behavioral fixes don't generalize to novel distractor types.' The proposal must compare against EIT and explain what additional generalization benefit circuit-level modification provides beyond EIT's already-strong transfer.", "VENUE MISMATCH — User explicitly requested 'Target: EMNLP 2026, ARR submission' but the proposal targets ICLR 2027 (Sep 24, 2026) and AAAI 2027 (Aug 2, 2026). The EMNLP 2026 ARR deadline is May 25, 2026 — 8 days away, making it infeasible for a 3-4 month project.", "ARCHITECTURE RISK — Qwen3-8B uses Grouped Query Attention (32 query heads, 8 KV heads), fundamentally different from Llama-3.1-8B's standard MHA (32 query/32 KV heads). The differentiable masking method from 'Llama See, Llama Do' was developed for standard MHA. Transfer to GQA is non-trivial and unvalidated — which head granularity do you mask, query heads or KV heads?", "MODEL MISMATCH — User constraints specify 'Llama-3-8B, Qwen2.5-7B/14B' but the proposal uses Qwen3-8B, a different model family.", "MISSING COMPETITOR — Causal Head Gating (CHG, NeurIPS 2025, arXiv:2505.13737) already uses contrastive gating to identify separable sub-circuits for ICL vs. instruction following. Contrastive CHG could be directly applied to separate entrainment-for-ICL from entrainment-for-distraction circuits, making it a very close competitor.", "MISSING COMPETITOR — Gated Attention (NeurIPS 2025 Best Paper) introduces query-dependent sigmoid gates on attention heads — architecturally similar to the proposed 'relevance-gated entrainment.' Must discuss.", "MISSING COMPETITOR — Distractor Injection Attacks defense (arXiv:2510.16259) achieves >50 point robustness improvement through SFT+RL on synthetic adversarial data.", "ATTENTION TARGET CONSTRUCTION — The method requires knowing which context tokens are 'question-relevant' to construct attention supervision targets for 'chosen' responses. This effectively requires relevance annotations during training. For math (GSM-DC), this is straightforward, but for general NLP tasks, relevance boundaries are ambiguous. The proposal doesn't address how to scale this beyond tasks with clear relevant/irrelevant context boundaries.", "RESOURCE INCONSISTENCY — User's hard constraint is '≤200 H100-hours total' but the resource estimate lists 250-500 A100-80GB hours. Even accounting for H100 vs A100 speed difference (~1.5-2x), the lower bound of 250 A100-hours ≈ 125-170 H100-hours is tight, and the upper bound of 500 A100-hours ≈ 250-330 H100-hours exceeds the constraint."]
Feedback: The proposal has a well-crafted method formulation (Circuit-DPO loss = L_DPO + λ·KL(attn_entrainment || attn_target)) but is built on a shaky theoretical foundation. To revise successfully:

1. **Fix the theoretical premise**: Drop or weaken the 'shared circuit double-bind' claim. 'Llama See, Llama Do' actually shows entrainment heads CAN be ablated with minimal ICL cost (0.2-3%). Reframe: instead of 'we must solve the double-bind,' argue that inference-time masking is a blunt instrument (all-or-nothing suppression) and training-time circuit modification enables GRADED, query-conditional entrainment that inference-time masking cannot achieve. This is a weaker but defensible claim.

2. **Add EIT as primary baseline**: EIT's 39.1% unseen-distraction generalization through behavioral RL is the strongest counterevidence to your motivation. You MUST compare against it and demonstrate that Circuit-DPO achieves stronger OOD generalization OR additional benefits (mechanistic interpretability, no RL instability, etc.).

3. **Fix the venue**: Target EMNLP 2026 ARR or adjust timeline. Given the research takes 3-4 months, the earliest feasible ARR cycle would be around September 2026 — check which venues accept that cycle.

4. **Use user-specified models**: Switch to Llama-3-8B and Qwen2.5-7B/14B as requested, which also avoids the GQA architecture issue (Llama-3-8B uses standard MHA with GQA, but Qwen2.5 is closer to what the masking method was tested on).

5. **Address attention target construction**: Explicitly describe how relevance annotations are generated for training data. Options: (a) use tasks with synthetic distractors where relevance is known by construction, (b) use retrieval models to score relevance, (c) use attention patterns from correct reasoning traces as pseudo-labels.

6. **Discuss CHG and Gated Attention**: CHG (NeurIPS 2025) and Gated Attention (NeurIPS 2025 Best Paper) are close competitors. Differentiate clearly.

7. **Tighten resource estimates**: Stay within ≤200 H100-hours. Reduce scope if needed (e.g., 1-2 model sizes instead of full sweep).


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
  "promptId": "a3d75b2b-6fea-4c0e-a4c1-2babd86d2ee9",
  "type": "user",
  "uuid": "e7698380-4653-4b66-8822-abbe8c175505",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T08:43:45.582Z_

```json
{
  "parentUuid": "e7698380-4653-4b66-8822-abbe8c175505",
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
  "uuid": "25e34350-1859-4f7a-a043-670b91268638",
  "timestamp": "2026-05-17T08:43:45.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T08:43:45.582Z_

```json
{
  "parentUuid": "25e34350-1859-4f7a-a043-670b91268638",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fa75c031-413c-4ebf-987b-18c566b8e12c",
  "timestamp": "2026-05-17T08:43:45.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "fa75c031-413c-4ebf-987b-18c566b8e12c",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Assistant

_source line 8 · 2026-05-17T08:43:56.253Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this revised idea (Round 2) for Circuit-DPO. I need to independently verify the claims, check for competing work, and assess whether the Round 1 issues have been adequately addressed.

Let me start by identifying what changed from Round 1:
1. The theoretical premise has been reframed - now argues inference-time masking is "blunt" (all-or-nothing) vs. training-time "graded" control
2. EIT is now included as a baseline
3. Venue changed to ICLR 2027 and ARR October 2026 (but user asked for EMNLP 2026)


4. The model selection has shifted to Llama-3-8B and Qwen2.5-7B, resource requirements are now estimated at around 170-200 H100 hours, and they're addressing attention target construction through self-supervised pairing of clean and noisy examples while also discussing CHG and Gated Attention approaches.

Now I need to verify these claims and search for competing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa75c031-413c-4ebf-987b-18c566b8e12c",
  "isSidechain": false,
  "requestId": "req_011Cb7r1CjQu7FgKTz7pyBr5",
  "type": "assistant",
  "uuid": "ab6c39a7-ccd5-4826-aa38-943036e62229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UC6ZxqdkQHvjFV2sbW7owd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 994,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 994,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17974
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

_source line 9 · 2026-05-17T08:43:56.257Z_

I'll conduct an independent verification of this revised proposal. Let me start by searching for the key claims and competing work in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6c39a7-ccd5-4826-aa38-943036e62229",
  "isSidechain": false,
  "requestId": "req_011Cb7r1CjQu7FgKTz7pyBr5",
  "type": "assistant",
  "uuid": "dedb01a6-b4d2-4ecb-bfc7-0cc1c0e71fdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UC6ZxqdkQHvjFV2sbW7owd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 994,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 994,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17974
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

_source line 10 · 2026-05-17T08:44:10.993Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01P6evBBPgPbBpQySd48ZfYQ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify core papers and claims",
  "prompt": "You are helping me verify claims in an ML research proposal. I need you to use WebSearch and WebFetch to verify the following specific claims. Be thorough — I need actual evidence, not assumptions.\n\n1. **Verify \"Llama See, Llama Do\" (ACL 2025)**: Search for this paper. Confirm:\n   - Does it identify \"entrainment heads\" that boost logits for context-seen tokens?\n   - Does it show these heads can be ablated with only 0.2-3% ICL degradation?\n   - Does it say entrainment is \"task-specific, not model-specific\"?\n   - Does it propose inference-time masking only (no training fix)?\n   - What architecture was it validated on? (Llama-3.1-8B MHA vs GQA?)\n   - How many entrainment heads does it identify (the proposal claims 30-110)?\n\n2. **Verify EIT (arXiv:2602.01528)**: Search for \"Making Bias Non-Predictive Training Robust LLM Reasoning Reinforcement Learning arXiv 2602.01528\". Confirm:\n   - Does it achieve +39.1% generalization to unseen bias types?\n   - Is this cross-bias-type transfer (bandwagon→distraction) or within-distraction-type generalization?\n   - What is the method exactly?\n\n3. **Verify RAL (arXiv:2602.04884)**: Search for \"Reinforced Attention Learning arXiv 2602.04884\". Confirm:\n   - Does it optimize internal attention distributions?\n   - Is it multimodal only or also text?\n   - How close is it to Circuit-DPO conceptually?\n\n4. **Verify CHG (arXiv:2505.13737)**: Search for \"Causal Head Gating arXiv 2505.13737\". Is it an analysis tool or training method?\n\n5. **Verify Gated Attention (arXiv:2505.06708)**: Was this actually NeurIPS 2025 Best Paper? What does it do?\n\n6. **Verify venue deadlines**: \n   - ICLR 2027 deadline — is Sep 24, 2026 correct?\n   - ARR October 2026 — is Oct 12, 2026 correct?\n   - What is the actual EMNLP 2026 ARR submission deadline?\n\nFor each item, search using WebSearch with 2-3 different queries, and use WebFetch on the most relevant result to read the actual content. Report exactly what you find — do not speculate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedb01a6-b4d2-4ecb-bfc7-0cc1c0e71fdd",
  "isSidechain": false,
  "requestId": "req_011Cb7r1CjQu7FgKTz7pyBr5",
  "type": "assistant",
  "uuid": "c1f5fe6a-950b-41fa-a08f-35e89edf24d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UC6ZxqdkQHvjFV2sbW7owd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 994,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 994,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17974
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

_source line 11 · 2026-05-17T08:47:24.327Z_

<details><summary>↩ Tool result · `toolu_01P6evBBPgPbBpQySd48ZfYQ`</summary>

```text
Now I have comprehensive evidence for all claims. Here is my full verification report:

---

## Verification Report

### 1. "Llama See, Llama Do" (arXiv:2505.09338, ACL 2025)

**Paper confirmed to exist.** Published at ACL 2025 (Volume 1: Long Papers, pages 16218-16239, Vienna). It won an **Outstanding Paper** award. Authors: Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi.

Claim-by-claim:

- **"Entrainment heads" that boost logits for context-seen tokens?** CONFIRMED. The paper identifies attention heads that substantially increase the logit gap for tokens seen in context, regardless of relevance.

- **Ablated with only 0.2-3% ICL degradation?** CONFIRMED. Table 4 in the paper shows degradation of 0.2-3%. For example, spelling correction 5-shot goes from 99.0% to 98.4%, and translation 5-shot from 98.6% to 97.2%.

- **"Task-specific, not model-specific"?** CONFIRMED. The paper explicitly states: "Entrainment heads are task-specific (or relation-specific), not model-specific."

- **Inference-time masking only (no training fix)?** CONFIRMED. The paper only proposes inference-time masking (setting head outputs to zero). The authors explicitly acknowledge this limitation: "we do not propose an application to mitigate the distraction problem. We believe our findings serve as foundational steps."

- **Architecture: Llama-3.1-8B MHA vs GQA?** PARTIALLY CONFIRMED. The paper tests on Llama-3.1-8B (primary), Llama-3.1-8B-Instruct, Llama-2-7b-hf, Llama-2-13b-hf, and GPT-2 XL. I could **not find evidence** that it specifically contrasts MHA vs GQA architectures. Note that Llama-3.1-8B uses GQA, while GPT-2 XL uses MHA, so both architectures are covered in their model set, but this does not appear to be a focus of the paper.

- **30-110 entrainment heads?** CONFIRMED. Table 3 shows relation-specific counts ranging from 30 heads (2.9% density, for country-language) to 110 heads (10.7% density, for product-by-company). The paper states a small set (3.2% to 10.7%) of attention heads are responsible.

---

### 2. EIT (arXiv:2602.01528)

**Paper confirmed to exist.** Title: "Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning" (note: an earlier version used "Judges" instead of "Reasoning" in the title). Posted February 2, 2026, revised April 2026.

Claim-by-claim:

- **+39.1% generalization to unseen bias types?** CONFIRMED. On Qwen3-4B, distraction wrong-bias robustness improved from 40.6% to 79.7% (+39.1%) despite distraction never being seen during training.

- **Cross-bias-type transfer (bandwagon to distraction)?** CONFIRMED. The model was trained only on bandwagon bias and generalized to authority and distraction biases. The +39.1% figure specifically refers to bandwagon-to-distraction transfer. The paper notes minimal transfer to position bias (which is structural rather than content-based).

- **What is the method?** Epistemic Independence Training (EIT): a reinforcement learning framework using a "balanced conflict strategy where bias signals are equally likely to support correct and incorrect answers, combined with a reward design that penalizes bias-following without rewarding bias agreement." Primary model: Qwen3-4B, with cross-model generalization tested on Llama-3.2-3B and Qwen3-8B.

**IMPORTANT NUANCE:** The proposal's description says "reasoning" but the paper addresses LLMs as both reasoners AND evaluators/judges (LLM-as-a-Judge). The title itself changed between versions.

---

### 3. RAL (arXiv:2602.04884)

**Paper confirmed to exist.** Title: "Reinforced Attention Learning." Authors: Bangzheng Li, Jianmo Ni, Chen Qu, Ian Miao, Liu Yang, Xingyu Fu, Muhao Chen, Derek Zhiyuan Cheng. Submitted February 4, 2026.

Claim-by-claim:

- **Optimizes internal attention distributions?** CONFIRMED. RAL is a "policy-gradient framework that directly optimizes internal attention distributions rather than output token sequences." It formulates attention distributions as a policy and applies advantage-weighted divergence minimization using Jensen-Shannon Divergence.

- **Multimodal only or also text?** MULTIMODAL ONLY. The paper is exclusively about Multimodal LLMs (MLLMs), addressing Visual Question Answering across image and video benchmarks. It does not address text-only scenarios.

- **How close to Circuit-DPO?** "Circuit-DPO" does **not appear to exist** as a published paper. Multiple searches across arXiv and the web returned zero results for any paper titled "Circuit-DPO." The proposal's reference to this concept may be fabricated or refer to an unpublished idea. RAL itself does not mention Circuit-DPO. RAL's conceptual novelty is optimizing *where* the model attends (internal attention) rather than *what* it generates (output tokens), which is distinct from standard DPO/RLHF approaches.

---

### 4. CHG (arXiv:2505.13737)

**Paper confirmed to exist.** Title: "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers." Authors: Andrew Nam, Henry Conklin, Yukang Yang, Thomas Griffiths, Jonathan Cohen, Sarah-Jane Leslie (Princeton University). Published May 2025.

- **Analysis tool or training method?** It is an **interpretability/analysis tool**, not a training method. The paper describes CHG as "a scalable method for interpreting the functional roles of attention heads." It learns soft gates over heads and assigns them a causal taxonomy (facilitating, interfering, or irrelevant). Tested on Llama 3 family models across syntax, commonsense, and math reasoning tasks. Validated via ablation and causal mediation analyses.

---

### 5. Gated Attention (arXiv:2505.06708)

**Paper confirmed to exist.** Title: "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free." From the Qwen Team.

- **NeurIPS 2025 Best Paper?** CONFIRMED. The official NeurIPS blog post ([link](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)) lists it as one of 4 Best Paper winners out of 5,290 accepted submissions.

- **What does it do?** Applies a head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA). The gating introduces non-linearity and query-dependent sparse gating scores. Tested across 30 variants of 15B MoE models and 1.7B dense models on 3.5T tokens. Benefits: improved training stability, tolerance for larger learning rates, reduced "attention sink" phenomenon, and better context length extension.

---

### 6. Venue Deadlines

- **ICLR 2027 deadline -- Sep 24, 2026?** LIKELY CORRECT BUT UNOFFICIAL. The trybibby.com conference tracker lists ICLR 2027 with abstract deadline September 19, 2026 and full paper deadline September 24, 2026. However, **no official ICLR 2027 call for papers has been published** as of May 2026. The ICLR 2026 paper deadline was September 24, 2025, so September 24, 2026 for ICLR 2027 is a plausible extrapolation but not yet officially confirmed.

- **ARR October 2026 -- Oct 12, 2026?** CONFIRMED. The ACL Rolling Review dates page ([aclrollingreview.org/dates](http://aclrollingreview.org/dates)) lists October 12 as the submission deadline for the October 2026 ARR cycle.

- **EMNLP 2026 ARR submission deadline?** The EMNLP 2026 call for papers ([2026.emnlp.org](https://2026.emnlp.org/calls/main_conference_papers/)) states the relevant ARR cycle is **May 2026, with a deadline of May 25, 2026**. The October 2026 ARR cycle would **NOT** be applicable to EMNLP 2026 -- it is far too late. EMNLP 2026 takes place October 24-29, 2026, with acceptance notification August 20, 2026. If the proposal claims October 2026 ARR for EMNLP 2026, that is **incorrect**.

---

### Summary of Red Flags

1. **"Circuit-DPO"** appears to be a non-existent paper/method. No search results found across multiple queries.
2. **RAL is multimodal-only**, not text. The proposal may be misrepresenting its applicability if suggesting it for text-only tasks.
3. **CHG is an analysis tool**, not a training method. If the proposal frames it as a training approach, that is inaccurate.
4. **EMNLP 2026 via October ARR** is incorrect -- EMNLP 2026 uses the May 2026 ARR cycle (deadline May 25, 2026).
5. **ICLR 2027 Sep 24 deadline** is plausible but not officially announced yet.
6. The "Llama See Llama Do" paper does **not** appear to explicitly contrast MHA vs GQA as a finding, though it tests models that happen to use both architectures.

Sources:
- [Llama See, Llama Do - arXiv](https://arxiv.org/abs/2505.09338)
- [Llama See, Llama Do - ACL Anthology](https://aclanthology.org/2025.acl-long.791/)
- [EIT - arXiv:2602.01528](https://arxiv.org/abs/2602.01528)
- [RAL - arXiv:2602.04884](https://arxiv.org/abs/2602.04884)
- [CHG - arXiv:2505.13737](https://arxiv.org/abs/2505.13737)
- [Gated Attention - arXiv:2505.06708](https://arxiv.org/abs/2505.06708)
- [NeurIPS 2025 Best Paper Awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Dates](http://aclrollingreview.org/dates)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [Conference Deadlines Tracker](https://trybibby.com/conference-deadlines)

agentId: ab48f9e181e4f00ec (use SendMessage with to: 'ab48f9e181e4f00ec' to continue this agent)
&lt;usage>total_tokens: 34495
tool_uses: 30
duration_ms: 193327&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1f5fe6a-950b-41fa-a08f-35e89edf24d1",
  "isSidechain": false,
  "promptId": "a3d75b2b-6fea-4c0e-a4c1-2babd86d2ee9",
  "type": "user",
  "uuid": "3b738567-9323-4473-aa60-7bb687404fe1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims in an ML research proposal. I need you to use WebSearch and WebFetch to verify the following specific claims. Be thorough — I need actual evidence, not assumptions.\n\n1. **Verify \"Llama See, Llama Do\" (ACL 2025)**: Search for this paper. Confirm:\n   - Does it identify \"entrainment heads\" that boost logits for context-seen tokens?\n   - Does it show these heads can be ablated with only 0.2-3% ICL degradation?\n   - Does it say entrainment is \"task-specific, not model-specific\"?\n   - Does it propose inference-time masking only (no training fix)?\n   - What architecture was it validated on? (Llama-3.1-8B MHA vs GQA?)\n   - How many entrainment heads does it identify (the proposal claims 30-110)?\n\n2. **Verify EIT (arXiv:2602.01528)**: Search for \"Making Bias Non-Predictive Training Robust LLM Reasoning Reinforcement Learning arXiv 2602.01528\". Confirm:\n   - Does it achieve +39.1% generalization to unseen bias types?\n   - Is this cross-bias-type transfer (bandwagon→distraction) or within-distraction-type generalization?\n   - What is the method exactly?\n\n3. **Verify RAL (arXiv:2602.04884)**: Search for \"Reinforced Attention Learning arXiv 2602.04884\". Confirm:\n   - Does it optimize internal attention distributions?\n   - Is it multimodal only or also text?\n   - How close is it to Circuit-DPO conceptually?\n\n4. **Verify CHG (arXiv:2505.13737)**: Search for \"Causal Head Gating arXiv 2505.13737\". Is it an analysis tool or training method?\n\n5. **Verify Gated Attention (arXiv:2505.06708)**: Was this actually NeurIPS 2025 Best Paper? What does it do?\n\n6. **Verify venue deadlines**: \n   - ICLR 2027 deadline — is Sep 24, 2026 correct?\n   - ARR October 2026 — is Oct 12, 2026 correct?\n   - What is the actual EMNLP 2026 ARR submission deadline?\n\nFor each item, search using WebSearch with 2-3 different queries, and use WebFetch on the most relevant result to read the actual content. Report exactly what you find — do not speculate.",
    "agentId": "ab48f9e181e4f00ec",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive evidence for all claims. Here is my full verification report:\n\n---\n\n## Verification Report\n\n### 1. \"Llama See, Llama Do\" (arXiv:2505.09338, ACL 2025)\n\n**Paper confirmed to exist.** Published at ACL 2025 (Volume 1: Long Papers, pages 16218-16239, Vienna). It won an **Outstanding Paper** award. Authors: Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi.\n\nClaim-by-claim:\n\n- **\"Entrainment heads\" that boost logits for context-seen tokens?** CONFIRMED. The paper identifies attention heads that substantially increase the logit gap for tokens seen in context, regardless of relevance.\n\n- **Ablated with only 0.2-3% ICL degradation?** CONFIRMED. Table 4 in the paper shows degradation of 0.2-3%. For example, spelling correction 5-shot goes from 99.0% to 98.4%, and translation 5-shot from 98.6% to 97.2%.\n\n- **\"Task-specific, not model-specific\"?** CONFIRMED. The paper explicitly states: \"Entrainment heads are task-specific (or relation-specific), not model-specific.\"\n\n- **Inference-time masking only (no training fix)?** CONFIRMED. The paper only proposes inference-time masking (setting head outputs to zero). The authors explicitly acknowledge this limitation: \"we do not propose an application to mitigate the distraction problem. We believe our findings serve as foundational steps.\"\n\n- **Architecture: Llama-3.1-8B MHA vs GQA?** PARTIALLY CONFIRMED. The paper tests on Llama-3.1-8B (primary), Llama-3.1-8B-Instruct, Llama-2-7b-hf, Llama-2-13b-hf, and GPT-2 XL. I could **not find evidence** that it specifically contrasts MHA vs GQA architectures. Note that Llama-3.1-8B uses GQA, while GPT-2 XL uses MHA, so both architectures are covered in their model set, but this does not appear to be a focus of the paper.\n\n- **30-110 entrainment heads?** CONFIRMED. Table 3 shows relation-specific counts ranging from 30 heads (2.9% density, for country-language) to 110 heads (10.7% density, for product-by-company). The paper states a small set (3.2% to 10.7%) of attention heads are responsible.\n\n---\n\n### 2. EIT (arXiv:2602.01528)\n\n**Paper confirmed to exist.** Title: \"Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning\" (note: an earlier version used \"Judges\" instead of \"Reasoning\" in the title). Posted February 2, 2026, revised April 2026.\n\nClaim-by-claim:\n\n- **+39.1% generalization to unseen bias types?** CONFIRMED. On Qwen3-4B, distraction wrong-bias robustness improved from 40.6% to 79.7% (+39.1%) despite distraction never being seen during training.\n\n- **Cross-bias-type transfer (bandwagon to distraction)?** CONFIRMED. The model was trained only on bandwagon bias and generalized to authority and distraction biases. The +39.1% figure specifically refers to bandwagon-to-distraction transfer. The paper notes minimal transfer to position bias (which is structural rather than content-based).\n\n- **What is the method?** Epistemic Independence Training (EIT): a reinforcement learning framework using a \"balanced conflict strategy where bias signals are equally likely to support correct and incorrect answers, combined with a reward design that penalizes bias-following without rewarding bias agreement.\" Primary model: Qwen3-4B, with cross-model generalization tested on Llama-3.2-3B and Qwen3-8B.\n\n**IMPORTANT NUANCE:** The proposal's description says \"reasoning\" but the paper addresses LLMs as both reasoners AND evaluators/judges (LLM-as-a-Judge). The title itself changed between versions.\n\n---\n\n### 3. RAL (arXiv:2602.04884)\n\n**Paper confirmed to exist.** Title: \"Reinforced Attention Learning.\" Authors: Bangzheng Li, Jianmo Ni, Chen Qu, Ian Miao, Liu Yang, Xingyu Fu, Muhao Chen, Derek Zhiyuan Cheng. Submitted February 4, 2026.\n\nClaim-by-claim:\n\n- **Optimizes internal attention distributions?** CONFIRMED. RAL is a \"policy-gradient framework that directly optimizes internal attention distributions rather than output token sequences.\" It formulates attention distributions as a policy and applies advantage-weighted divergence minimization using Jensen-Shannon Divergence.\n\n- **Multimodal only or also text?** MULTIMODAL ONLY. The paper is exclusively about Multimodal LLMs (MLLMs), addressing Visual Question Answering across image and video benchmarks. It does not address text-only scenarios.\n\n- **How close to Circuit-DPO?** \"Circuit-DPO\" does **not appear to exist** as a published paper. Multiple searches across arXiv and the web returned zero results for any paper titled \"Circuit-DPO.\" The proposal's reference to this concept may be fabricated or refer to an unpublished idea. RAL itself does not mention Circuit-DPO. RAL's conceptual novelty is optimizing *where* the model attends (internal attention) rather than *what* it generates (output tokens), which is distinct from standard DPO/RLHF approaches.\n\n---\n\n### 4. CHG (arXiv:2505.13737)\n\n**Paper confirmed to exist.** Title: \"Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers.\" Authors: Andrew Nam, Henry Conklin, Yukang Yang, Thomas Griffiths, Jonathan Cohen, Sarah-Jane Leslie (Princeton University). Published May 2025.\n\n- **Analysis tool or training method?** It is an **interpretability/analysis tool**, not a training method. The paper describes CHG as \"a scalable method for interpreting the functional roles of attention heads.\" It learns soft gates over heads and assigns them a causal taxonomy (facilitating, interfering, or irrelevant). Tested on Llama 3 family models across syntax, commonsense, and math reasoning tasks. Validated via ablation and causal mediation analyses.\n\n---\n\n### 5. Gated Attention (arXiv:2505.06708)\n\n**Paper confirmed to exist.** Title: \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free.\" From the Qwen Team.\n\n- **NeurIPS 2025 Best Paper?** CONFIRMED. The official NeurIPS blog post ([link](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)) lists it as one of 4 Best Paper winners out of 5,290 accepted submissions.\n\n- **What does it do?** Applies a head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA). The gating introduces non-linearity and query-dependent sparse gating scores. Tested across 30 variants of 15B MoE models and 1.7B dense models on 3.5T tokens. Benefits: improved training stability, tolerance for larger learning rates, reduced \"attention sink\" phenomenon, and better context length extension.\n\n---\n\n### 6. Venue Deadlines\n\n- **ICLR 2027 deadline -- Sep 24, 2026?** LIKELY CORRECT BUT UNOFFICIAL. The trybibby.com conference tracker lists ICLR 2027 with abstract deadline September 19, 2026 and full paper deadline September 24, 2026. However, **no official ICLR 2027 call for papers has been published** as of May 2026. The ICLR 2026 paper deadline was September 24, 2025, so September 24, 2026 for ICLR 2027 is a plausible extrapolation but not yet officially confirmed.\n\n- **ARR October 2026 -- Oct 12, 2026?** CONFIRMED. The ACL Rolling Review dates page ([aclrollingreview.org/dates](http://aclrollingreview.org/dates)) lists October 12 as the submission deadline for the October 2026 ARR cycle.\n\n- **EMNLP 2026 ARR submission deadline?** The EMNLP 2026 call for papers ([2026.emnlp.org](https://2026.emnlp.org/calls/main_conference_papers/)) states the relevant ARR cycle is **May 2026, with a deadline of May 25, 2026**. The October 2026 ARR cycle would **NOT** be applicable to EMNLP 2026 -- it is far too late. EMNLP 2026 takes place October 24-29, 2026, with acceptance notification August 20, 2026. If the proposal claims October 2026 ARR for EMNLP 2026, that is **incorrect**.\n\n---\n\n### Summary of Red Flags\n\n1. **\"Circuit-DPO\"** appears to be a non-existent paper/method. No search results found across multiple queries.\n2. **RAL is multimodal-only**, not text. The proposal may be misrepresenting its applicability if suggesting it for text-only tasks.\n3. **CHG is an analysis tool**, not a training method. If the proposal frames it as a training approach, that is inaccurate.\n4. **EMNLP 2026 via October ARR** is incorrect -- EMNLP 2026 uses the May 2026 ARR cycle (deadline May 25, 2026).\n5. **ICLR 2027 Sep 24 deadline** is plausible but not officially announced yet.\n6. The \"Llama See Llama Do\" paper does **not** appear to explicitly contrast MHA vs GQA as a finding, though it tests models that happen to use both architectures.\n\nSources:\n- [Llama See, Llama Do - arXiv](https://arxiv.org/abs/2505.09338)\n- [Llama See, Llama Do - ACL Anthology](https://aclanthology.org/2025.acl-long.791/)\n- [EIT - arXiv:2602.01528](https://arxiv.org/abs/2602.01528)\n- [RAL - arXiv:2602.04884](https://arxiv.org/abs/2602.04884)\n- [CHG - arXiv:2505.13737](https://arxiv.org/abs/2505.13737)\n- [Gated Attention - arXiv:2505.06708](https://arxiv.org/abs/2505.06708)\n- [NeurIPS 2025 Best Paper Awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ARR Dates](http://aclrollingreview.org/dates)\n- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)\n- [Conference Deadlines Tracker](https://trybibby.com/conference-deadlines)"
      }
    ],
    "totalDurationMs": 193327,
    "totalTokens": 34495,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2734,
      "cache_read_input_tokens": 28902,
      "output_tokens": 2858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2858,
          "cache_read_input_tokens": 28902,
          "cache_creation_input_tokens": 2734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2734,
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
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "c1f5fe6a-950b-41fa-a08f-35e89edf24d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T08:47:41.932Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XEaZi4Yh77QZRaMKLnuyTw`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing/concurrent work",
  "prompt": "You are helping me review an ML research proposal called \"Circuit-DPO\" that augments DPO loss with an attention-distribution KL term on mechanistically-identified \"entrainment heads\" to improve LLM distractor robustness. I need you to search for competing and concurrent work that the proposal might have missed.\n\nUse WebSearch extensively (at least 8-10 searches) to find:\n\n1. **Attention-level DPO or preference optimization**: Search for papers that modify DPO to target internal representations or attention patterns, not just output behavior.\n   - Try: \"DPO attention regularization LLM 2025 2026\"\n   - Try: \"preference optimization internal representations attention\"\n   - Try: \"circuit-level preference learning language model\"\n\n2. **Training-time distraction robustness**: Search for ANY training method (not inference-time) that targets attention mechanisms for distraction robustness in LLMs.\n   - Try: \"attention head training distraction robustness LLM 2025 2026\"\n   - Try: \"mechanistic training fix contextual entrainment\"\n   - Try: \"training attention heads relevance LLM\"\n\n3. **Self-supervised attention targets for training**: Has anyone used clean-input attention patterns as supervision targets for noisy inputs?\n   - Try: \"self-supervised attention distillation clean noisy inputs\"\n   - Try: \"attention pattern supervision training LLM\"\n\n4. **Circuit-targeted training**: Search for methods that use mechanistic interpretability findings to guide training interventions.\n   - Try: \"mechanistic interpretability guided training intervention\"\n   - Try: \"circuit discovery training optimization LLM 2025 2026\"\n   - Try: \"CART circuit aware reward training arXiv 2509.24713\"\n\n5. **FPO (arXiv:2411.07618)**: Verify this paper - \"Direct Preference Optimization Using Sparse Feature-Level Constraints\". How close is it to Circuit-DPO?\n\n6. **Concurrent distraction robustness work from 2026**:\n   - Try: \"LLM distraction robustness 2026\"\n   - Try: \"irrelevant context LLM training 2026\"\n   - Try: \"contextual distractor defense training 2026\"\n\nFor each relevant paper found, report: title, venue/year, method summary, and how close it is to Circuit-DPO. Use WebFetch on the 2-3 most relevant findings to read more detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b738567-9323-4473-aa60-7bb687404fe1",
  "isSidechain": false,
  "requestId": "req_011Cb7rHKtxus2uWtG73ezZz",
  "type": "assistant",
  "uuid": "7d8cd711-6a3e-45f3-a82d-9cdc34c8072c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012N6Zb3WG8iofNF3gaoXBzq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3930,
      "cache_read_input_tokens": 29815,
      "output_tokens": 671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 671,
          "cache_read_input_tokens": 29815,
          "cache_creation_input_tokens": 3930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3930
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7d8cd711-6a3e-45f3-a82d-9cdc34c8072c",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Tool result

_source line 15 · 2026-05-17T08:51:45.095Z_

<details><summary>↩ Tool result · `toolu_01XEaZi4Yh77QZRaMKLnuyTw`</summary>

```text
Now I have a comprehensive picture. Let me compile the final report.

---

## Literature Review: Competing and Concurrent Work to Circuit-DPO

Below is a structured review of the most relevant papers found, organized by how closely they relate to Circuit-DPO's core idea of augmenting DPO loss with an attention-distribution KL term on mechanistically-identified "entrainment heads."

---

### 1. DIRECT PREDECESSORS / MOST CLOSELY RELATED

#### (A) "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"
- **Authors**: Niu et al. (Microsoft / University of Toronto)
- **Venue/Year**: ACL 2025 (arXiv: 2505.09338)
- **Method**: Identifies "entrainment heads" via differentiable masking -- specific attention heads that, when turned off, dramatically suppress contextual entrainment (the tendency of LLMs to up-weight any tokens previously seen in context, even random ones). The intervention is inference-time only: zero out the identified heads' outputs.
- **Proximity to Circuit-DPO**: **EXTREMELY HIGH**. This is clearly the foundational work that Circuit-DPO builds upon. Circuit-DPO's key novelty over this paper is making the entrainment-head fix a *training-time* intervention (via a KL term in DPO loss targeting attention distributions of these heads) rather than an inference-time ablation. The proposal should cite this prominently and clearly articulate the training-vs-inference distinction.

#### (B) FPO: "Direct Preference Optimization Using Sparse Feature-Level Constraints"
- **Authors**: Zhu, Yang et al.
- **Venue/Year**: arXiv 2411.07618 (Nov 2024), under review
- **Method**: Replaces the standard KL divergence constraint in DPO with a constraint on *sparse autoencoder (SAE) feature activations* at specific internal layers. Uses pre-trained SAEs to extract sparse features from hidden representations, then penalizes the MSE between top-k activated features of the policy and reference model. Operates on layer 25 (near output) of 2B models. Achieves 5%+ win rate improvements with 17.6% memory reduction vs TDPO.
- **Proximity to Circuit-DPO**: **HIGH**. Both FPO and Circuit-DPO modify DPO's loss to target internal representations rather than just output distributions. Key differences: FPO targets SAE-derived *feature activations* in hidden states (a general regularization), while Circuit-DPO targets *attention distributions* on specific mechanistically-identified heads. FPO is not circuit-specific or task-specific -- it is a general alignment stabilizer. Circuit-DPO is targeted at a specific failure mode (entrainment/distraction). The proposal should discuss FPO as the closest methodological relative.

#### (C) RetMask: "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models"
- **Authors**: arXiv 2601.11020 (Jan 2026)
- **Method**: Identifies "retrieval heads" (attention heads responsible for copying information from context) using Needle-In-A-Haystack probing. Creates an ablated model by zeroing out retrieval heads' output projection columns. Generates DPO preference pairs: chosen = outputs from normal model, rejected = outputs from ablated (retrieval-head-masked) model. Trains with standard DPO on these mechanistically-grounded pairs. Achieves +2.28 on HELMET at 128K for Llama-3.1.
- **Proximity to Circuit-DPO**: **HIGH**. RetMask is arguably the closest existing work in spirit: it uses mechanistic interpretability to identify specific attention heads, then feeds that knowledge into DPO training. The difference: RetMask uses head identification to *generate preference data* (contrastive sampling), while Circuit-DPO uses head identification to add an *auxiliary loss term* on attention distributions. RetMask targets retrieval capability (boosting it), while Circuit-DPO targets entrainment (suppressing it). **This paper should be cited and discussed as a key concurrent work.**

---

### 2. CIRCUIT-TARGETED TRAINING METHODS

#### (D) CART: "Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF"
- **Venue/Year**: arXiv 2509.24713 (Sep 2025), under review
- **Method**: Three-phase framework for reward models: (1) circuit discovery via activation pattern analysis + causal validation, (2) vulnerability assessment of longtail circuits, (3) targeted interventions including data augmentation, circuit-variance regularization, progressive curriculum, and ensemble. Targets the *reward model* rather than the policy.
- **Proximity to Circuit-DPO**: **MODERATE**. Shares the philosophy of "use circuit discovery to guide training," but targets reward model robustness on longtail distributions rather than policy attention patterns for distraction robustness. Different failure mode, different target model, different mechanism. Should be cited as a parallel effort in the "circuit-guided training" paradigm.

#### (E) Circuit Breakers: "Improving Alignment and Robustness with Circuit Breakers"
- **Authors**: Gray Swan / CMU
- **Venue/Year**: NeurIPS 2024
- **Method**: Trains models to map harmful internal representations to a "circuit breaker" state, directly modifying internal activations during training rather than relying on refusal-at-output. Operates on representation engineering principles. Shown to be highly robust to adversarial jailbreaks (87-90% reduction in harmful compliance).
- **Proximity to Circuit-DPO**: **MODERATE**. Both modify training to target internal representations rather than just outputs. Circuit Breakers target safety/harmful content; Circuit-DPO targets distraction robustness. Different problem domain but similar philosophy of "train internal representations, not just output behavior."

---

### 3. DISTRACTION ROBUSTNESS TRAINING METHODS

#### (F) "Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search"
- **Venue/Year**: NeurIPS 2025 (arXiv: 2502.01609)
- **Method**: Generates challenging distractions via tree search, causing 45%+ performance drops. Tests mitigation strategies and finds that *post-training with DPO* significantly improves contextual robustness, while prompt-based methods yield limited gains.
- **Proximity to Circuit-DPO**: **MODERATE**. Validates that DPO-based post-training is effective for distraction robustness (supporting Circuit-DPO's general approach), but uses standard DPO without any attention-level or circuit-level modification. Circuit-DPO could cite this as evidence that DPO is the right framework, and argue that circuit-targeting should improve it further.

#### (G) EIT: "Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning"
- **Venue/Year**: arXiv 2602.01528 (Feb 2026)
- **Method**: RL-based training with a "balanced conflict strategy" where bias signals are equally likely to support correct/incorrect answers, plus an asymmetric reward that penalizes following bias. Trained on bandwagon bias only, but transfers to distraction (+39.1%) and authority bias.
- **Proximity to Circuit-DPO**: **LOW-MODERATE**. Addresses distraction robustness via training but through reward engineering, not attention-mechanism targeting. Does not use mechanistic interpretability. Complementary approach -- could potentially be combined with Circuit-DPO.

#### (H) GSM-DC and Hard-IC Training
- **Venue/Year**: Various 2025-2026
- **Method**: Training with strong/hard distractors in math contexts. Key finding: "distractor difficulty, rather than variety, is the primary driver of improvement." Continued pretraining with strong irrelevant context boosts resilience.
- **Proximity to Circuit-DPO**: **LOW**. Data-centric approach (harder training distractors) rather than architecture/loss-centric. Orthogonal to Circuit-DPO's mechanism-targeting approach.

---

### 4. MECHANISTIC INTERPRETABILITY + TRAINING SURVEYS

#### (I) "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in LLMs"
- **Venue/Year**: arXiv 2601.14004 (Jan 2026)
- **Method**: Survey of 200+ papers on using MI for actionable model improvement. Structured around locate-steer-improve pipeline.
- **Key finding for Circuit-DPO**: The survey confirms that **training-level integration of MI remains underdeveloped** -- most MI work focuses on inference-time steering. This supports Circuit-DPO's novelty claim.

#### (J) "Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization"
- **Venue/Year**: arXiv 2604.22345 (Apr 2026)
- **Method**: Identifies "Preference Heads" -- attention heads encoding user-specific preferences -- via causal masking analysis. Uses them for training-free inference-time personalization (Differential Preference Steering).
- **Proximity to Circuit-DPO**: **LOW-MODERATE**. Shares the approach of identifying functionally-specific attention heads, but applies them at inference time for personalization rather than training time for robustness.

---

### 5. RELATED DPO/RLHF MODIFICATIONS

#### (K) T-REG: Token-Level Reward Regularization
- **Venue/Year**: ACL 2025
- **Method**: Uses LLM-generated token-level rewards as regularization during preference optimization.
- **Proximity**: **LOW**. Token-level, not attention-level.

#### (L) "Why Is RLHF Alignment Shallow?"
- **Venue/Year**: arXiv 2603.04851 (Mar 2026)
- **Key finding**: Safety alignment concentrates in early tokens; KL divergence between aligned and base models decays rapidly. Circuit breakers and representation engineering are cited as deeper alternatives.
- **Relevance to Circuit-DPO**: Supports the argument that output-level DPO may be insufficient and that targeting internal mechanisms (as Circuit-DPO does) is needed.

---

### SUMMARY: GAPS AND RECOMMENDATIONS

**What the proposal might be missing:**

1. **RetMask (arXiv 2601.11020)** -- This is the most important omission risk. It directly combines mechanistic head identification with DPO training for long-context tasks. Circuit-DPO must differentiate itself from RetMask clearly (auxiliary loss vs. contrastive data generation; entrainment suppression vs. retrieval enhancement).

2. **FPO (arXiv 2411.07618)** -- The closest methodological analog: modifying DPO's loss with internal-representation constraints. Circuit-DPO should position itself relative to FPO by emphasizing that FPO's SAE-based features are general and unsupervised, while Circuit-DPO's attention targets are mechanistically motivated for a specific failure mode.

3. **CART (arXiv 2509.24713)** -- A parallel "circuit-aware training" paper, though targeting reward models for longtail robustness. Should be cited in related work.

4. **Adaptive Distraction (NeurIPS 2025)** -- Provides evidence that standard DPO improves distraction robustness, serving as both validation and baseline for Circuit-DPO.

5. **EIT (arXiv 2602.01528)** -- An alternative training-time approach to distraction robustness via RL reward design. Complementary, not competing.

6. **"Locate, Steer, and Improve" survey (arXiv 2601.14004)** -- Confirms that training-time MI integration is an underexplored area, supporting the novelty claim.

7. **Circuit Breakers (NeurIPS 2024)** -- Important precedent for training on internal representations rather than outputs.

**The proposal's strongest novelty claims are:**
- Being one of the first to add an attention-distribution KL term (not just hidden-state or feature-level) to DPO loss
- Targeting mechanistically-identified heads for a specific failure mode (entrainment), rather than general alignment
- Bridging the gap between inference-time MI interventions (Llama See Llama Do) and training-time optimization

Sources:
- [Llama See, Llama Do (ACL 2025)](https://aclanthology.org/2025.acl-long.791/)
- [FPO: Sparse Feature-Level Constraints (arXiv 2411.07618)](https://arxiv.org/abs/2411.07618)
- [RetMask: Optimizing Retrieval Heads (arXiv 2601.11020)](https://arxiv.org/abs/2601.11020)
- [CART: Circuit-Aware Reward Training (arXiv 2509.24713)](https://arxiv.org/abs/2509.24713)
- [Circuit Breakers (NeurIPS 2024)](https://arxiv.org/abs/2406.04313)
- [Adaptive Distraction (NeurIPS 2025)](https://arxiv.org/abs/2502.01609)
- [EIT: Making Bias Non-Predictive (arXiv 2602.01528)](https://arxiv.org/html/2602.01528v2)
- [Preference Heads (arXiv 2604.22345)](https://arxiv.org/abs/2604.22345)
- [Locate, Steer, and Improve Survey (arXiv 2601.14004)](https://arxiv.org/abs/2601.14004)
- [T-REG: Token-Level Reward (ACL 2025)](https://aclanthology.org/2025.acl-long.1353.pdf)
- [Why Is RLHF Alignment Shallow? (arXiv 2603.04851)](https://arxiv.org/html/2603.04851)
- [GSM-DC / Irrelevant Context (arXiv 2505.18761)](https://arxiv.org/abs/2505.18761)
- [LLM Circuit Analyses Consistent Across Scale (NeurIPS 2024)](https://arxiv.org/abs/2407.10827)
- [OPA-DPO](https://opa-dpo.github.io/)
- [Attention Tracker for Prompt Injection (NAACL 2025)](https://aclanthology.org/2025.findings-naacl.123.pdf)

agentId: a04b6a5daebb2a5c3 (use SendMessage with to: 'a04b6a5daebb2a5c3' to continue this agent)
&lt;usage>total_tokens: 42011
tool_uses: 32
duration_ms: 243158&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d8cd711-6a3e-45f3-a82d-9cdc34c8072c",
  "isSidechain": false,
  "promptId": "a3d75b2b-6fea-4c0e-a4c1-2babd86d2ee9",
  "type": "user",
  "uuid": "61d7dc2a-7554-461e-bdf3-496d1fac313c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML research proposal called \"Circuit-DPO\" that augments DPO loss with an attention-distribution KL term on mechanistically-identified \"entrainment heads\" to improve LLM distractor robustness. I need you to search for competing and concurrent work that the proposal might have missed.\n\nUse WebSearch extensively (at least 8-10 searches) to find:\n\n1. **Attention-level DPO or preference optimization**: Search for papers that modify DPO to target internal representations or attention patterns, not just output behavior.\n   - Try: \"DPO attention regularization LLM 2025 2026\"\n   - Try: \"preference optimization internal representations attention\"\n   - Try: \"circuit-level preference learning language model\"\n\n2. **Training-time distraction robustness**: Search for ANY training method (not inference-time) that targets attention mechanisms for distraction robustness in LLMs.\n   - Try: \"attention head training distraction robustness LLM 2025 2026\"\n   - Try: \"mechanistic training fix contextual entrainment\"\n   - Try: \"training attention heads relevance LLM\"\n\n3. **Self-supervised attention targets for training**: Has anyone used clean-input attention patterns as supervision targets for noisy inputs?\n   - Try: \"self-supervised attention distillation clean noisy inputs\"\n   - Try: \"attention pattern supervision training LLM\"\n\n4. **Circuit-targeted training**: Search for methods that use mechanistic interpretability findings to guide training interventions.\n   - Try: \"mechanistic interpretability guided training intervention\"\n   - Try: \"circuit discovery training optimization LLM 2025 2026\"\n   - Try: \"CART circuit aware reward training arXiv 2509.24713\"\n\n5. **FPO (arXiv:2411.07618)**: Verify this paper - \"Direct Preference Optimization Using Sparse Feature-Level Constraints\". How close is it to Circuit-DPO?\n\n6. **Concurrent distraction robustness work from 2026**:\n   - Try: \"LLM distraction robustness 2026\"\n   - Try: \"irrelevant context LLM training 2026\"\n   - Try: \"contextual distractor defense training 2026\"\n\nFor each relevant paper found, report: title, venue/year, method summary, and how close it is to Circuit-DPO. Use WebFetch on the 2-3 most relevant findings to read more detail.",
    "agentId": "a04b6a5daebb2a5c3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the final report.\n\n---\n\n## Literature Review: Competing and Concurrent Work to Circuit-DPO\n\nBelow is a structured review of the most relevant papers found, organized by how closely they relate to Circuit-DPO's core idea of augmenting DPO loss with an attention-distribution KL term on mechanistically-identified \"entrainment heads.\"\n\n---\n\n### 1. DIRECT PREDECESSORS / MOST CLOSELY RELATED\n\n#### (A) \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs\"\n- **Authors**: Niu et al. (Microsoft / University of Toronto)\n- **Venue/Year**: ACL 2025 (arXiv: 2505.09338)\n- **Method**: Identifies \"entrainment heads\" via differentiable masking -- specific attention heads that, when turned off, dramatically suppress contextual entrainment (the tendency of LLMs to up-weight any tokens previously seen in context, even random ones). The intervention is inference-time only: zero out the identified heads' outputs.\n- **Proximity to Circuit-DPO**: **EXTREMELY HIGH**. This is clearly the foundational work that Circuit-DPO builds upon. Circuit-DPO's key novelty over this paper is making the entrainment-head fix a *training-time* intervention (via a KL term in DPO loss targeting attention distributions of these heads) rather than an inference-time ablation. The proposal should cite this prominently and clearly articulate the training-vs-inference distinction.\n\n#### (B) FPO: \"Direct Preference Optimization Using Sparse Feature-Level Constraints\"\n- **Authors**: Zhu, Yang et al.\n- **Venue/Year**: arXiv 2411.07618 (Nov 2024), under review\n- **Method**: Replaces the standard KL divergence constraint in DPO with a constraint on *sparse autoencoder (SAE) feature activations* at specific internal layers. Uses pre-trained SAEs to extract sparse features from hidden representations, then penalizes the MSE between top-k activated features of the policy and reference model. Operates on layer 25 (near output) of 2B models. Achieves 5%+ win rate improvements with 17.6% memory reduction vs TDPO.\n- **Proximity to Circuit-DPO**: **HIGH**. Both FPO and Circuit-DPO modify DPO's loss to target internal representations rather than just output distributions. Key differences: FPO targets SAE-derived *feature activations* in hidden states (a general regularization), while Circuit-DPO targets *attention distributions* on specific mechanistically-identified heads. FPO is not circuit-specific or task-specific -- it is a general alignment stabilizer. Circuit-DPO is targeted at a specific failure mode (entrainment/distraction). The proposal should discuss FPO as the closest methodological relative.\n\n#### (C) RetMask: \"From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models\"\n- **Authors**: arXiv 2601.11020 (Jan 2026)\n- **Method**: Identifies \"retrieval heads\" (attention heads responsible for copying information from context) using Needle-In-A-Haystack probing. Creates an ablated model by zeroing out retrieval heads' output projection columns. Generates DPO preference pairs: chosen = outputs from normal model, rejected = outputs from ablated (retrieval-head-masked) model. Trains with standard DPO on these mechanistically-grounded pairs. Achieves +2.28 on HELMET at 128K for Llama-3.1.\n- **Proximity to Circuit-DPO**: **HIGH**. RetMask is arguably the closest existing work in spirit: it uses mechanistic interpretability to identify specific attention heads, then feeds that knowledge into DPO training. The difference: RetMask uses head identification to *generate preference data* (contrastive sampling), while Circuit-DPO uses head identification to add an *auxiliary loss term* on attention distributions. RetMask targets retrieval capability (boosting it), while Circuit-DPO targets entrainment (suppressing it). **This paper should be cited and discussed as a key concurrent work.**\n\n---\n\n### 2. CIRCUIT-TARGETED TRAINING METHODS\n\n#### (D) CART: \"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF\"\n- **Venue/Year**: arXiv 2509.24713 (Sep 2025), under review\n- **Method**: Three-phase framework for reward models: (1) circuit discovery via activation pattern analysis + causal validation, (2) vulnerability assessment of longtail circuits, (3) targeted interventions including data augmentation, circuit-variance regularization, progressive curriculum, and ensemble. Targets the *reward model* rather than the policy.\n- **Proximity to Circuit-DPO**: **MODERATE**. Shares the philosophy of \"use circuit discovery to guide training,\" but targets reward model robustness on longtail distributions rather than policy attention patterns for distraction robustness. Different failure mode, different target model, different mechanism. Should be cited as a parallel effort in the \"circuit-guided training\" paradigm.\n\n#### (E) Circuit Breakers: \"Improving Alignment and Robustness with Circuit Breakers\"\n- **Authors**: Gray Swan / CMU\n- **Venue/Year**: NeurIPS 2024\n- **Method**: Trains models to map harmful internal representations to a \"circuit breaker\" state, directly modifying internal activations during training rather than relying on refusal-at-output. Operates on representation engineering principles. Shown to be highly robust to adversarial jailbreaks (87-90% reduction in harmful compliance).\n- **Proximity to Circuit-DPO**: **MODERATE**. Both modify training to target internal representations rather than just outputs. Circuit Breakers target safety/harmful content; Circuit-DPO targets distraction robustness. Different problem domain but similar philosophy of \"train internal representations, not just output behavior.\"\n\n---\n\n### 3. DISTRACTION ROBUSTNESS TRAINING METHODS\n\n#### (F) \"Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search\"\n- **Venue/Year**: NeurIPS 2025 (arXiv: 2502.01609)\n- **Method**: Generates challenging distractions via tree search, causing 45%+ performance drops. Tests mitigation strategies and finds that *post-training with DPO* significantly improves contextual robustness, while prompt-based methods yield limited gains.\n- **Proximity to Circuit-DPO**: **MODERATE**. Validates that DPO-based post-training is effective for distraction robustness (supporting Circuit-DPO's general approach), but uses standard DPO without any attention-level or circuit-level modification. Circuit-DPO could cite this as evidence that DPO is the right framework, and argue that circuit-targeting should improve it further.\n\n#### (G) EIT: \"Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning\"\n- **Venue/Year**: arXiv 2602.01528 (Feb 2026)\n- **Method**: RL-based training with a \"balanced conflict strategy\" where bias signals are equally likely to support correct/incorrect answers, plus an asymmetric reward that penalizes following bias. Trained on bandwagon bias only, but transfers to distraction (+39.1%) and authority bias.\n- **Proximity to Circuit-DPO**: **LOW-MODERATE**. Addresses distraction robustness via training but through reward engineering, not attention-mechanism targeting. Does not use mechanistic interpretability. Complementary approach -- could potentially be combined with Circuit-DPO.\n\n#### (H) GSM-DC and Hard-IC Training\n- **Venue/Year**: Various 2025-2026\n- **Method**: Training with strong/hard distractors in math contexts. Key finding: \"distractor difficulty, rather than variety, is the primary driver of improvement.\" Continued pretraining with strong irrelevant context boosts resilience.\n- **Proximity to Circuit-DPO**: **LOW**. Data-centric approach (harder training distractors) rather than architecture/loss-centric. Orthogonal to Circuit-DPO's mechanism-targeting approach.\n\n---\n\n### 4. MECHANISTIC INTERPRETABILITY + TRAINING SURVEYS\n\n#### (I) \"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in LLMs\"\n- **Venue/Year**: arXiv 2601.14004 (Jan 2026)\n- **Method**: Survey of 200+ papers on using MI for actionable model improvement. Structured around locate-steer-improve pipeline.\n- **Key finding for Circuit-DPO**: The survey confirms that **training-level integration of MI remains underdeveloped** -- most MI work focuses on inference-time steering. This supports Circuit-DPO's novelty claim.\n\n#### (J) \"Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization\"\n- **Venue/Year**: arXiv 2604.22345 (Apr 2026)\n- **Method**: Identifies \"Preference Heads\" -- attention heads encoding user-specific preferences -- via causal masking analysis. Uses them for training-free inference-time personalization (Differential Preference Steering).\n- **Proximity to Circuit-DPO**: **LOW-MODERATE**. Shares the approach of identifying functionally-specific attention heads, but applies them at inference time for personalization rather than training time for robustness.\n\n---\n\n### 5. RELATED DPO/RLHF MODIFICATIONS\n\n#### (K) T-REG: Token-Level Reward Regularization\n- **Venue/Year**: ACL 2025\n- **Method**: Uses LLM-generated token-level rewards as regularization during preference optimization.\n- **Proximity**: **LOW**. Token-level, not attention-level.\n\n#### (L) \"Why Is RLHF Alignment Shallow?\"\n- **Venue/Year**: arXiv 2603.04851 (Mar 2026)\n- **Key finding**: Safety alignment concentrates in early tokens; KL divergence between aligned and base models decays rapidly. Circuit breakers and representation engineering are cited as deeper alternatives.\n- **Relevance to Circuit-DPO**: Supports the argument that output-level DPO may be insufficient and that targeting internal mechanisms (as Circuit-DPO does) is needed.\n\n---\n\n### SUMMARY: GAPS AND RECOMMENDATIONS\n\n**What the proposal might be missing:**\n\n1. **RetMask (arXiv 2601.11020)** -- This is the most important omission risk. It directly combines mechanistic head identification with DPO training for long-context tasks. Circuit-DPO must differentiate itself from RetMask clearly (auxiliary loss vs. contrastive data generation; entrainment suppression vs. retrieval enhancement).\n\n2. **FPO (arXiv 2411.07618)** -- The closest methodological analog: modifying DPO's loss with internal-representation constraints. Circuit-DPO should position itself relative to FPO by emphasizing that FPO's SAE-based features are general and unsupervised, while Circuit-DPO's attention targets are mechanistically motivated for a specific failure mode.\n\n3. **CART (arXiv 2509.24713)** -- A parallel \"circuit-aware training\" paper, though targeting reward models for longtail robustness. Should be cited in related work.\n\n4. **Adaptive Distraction (NeurIPS 2025)** -- Provides evidence that standard DPO improves distraction robustness, serving as both validation and baseline for Circuit-DPO.\n\n5. **EIT (arXiv 2602.01528)** -- An alternative training-time approach to distraction robustness via RL reward design. Complementary, not competing.\n\n6. **\"Locate, Steer, and Improve\" survey (arXiv 2601.14004)** -- Confirms that training-time MI integration is an underexplored area, supporting the novelty claim.\n\n7. **Circuit Breakers (NeurIPS 2024)** -- Important precedent for training on internal representations rather than outputs.\n\n**The proposal's strongest novelty claims are:**\n- Being one of the first to add an attention-distribution KL term (not just hidden-state or feature-level) to DPO loss\n- Targeting mechanistically-identified heads for a specific failure mode (entrainment), rather than general alignment\n- Bridging the gap between inference-time MI interventions (Llama See Llama Do) and training-time optimization\n\nSources:\n- [Llama See, Llama Do (ACL 2025)](https://aclanthology.org/2025.acl-long.791/)\n- [FPO: Sparse Feature-Level Constraints (arXiv 2411.07618)](https://arxiv.org/abs/2411.07618)\n- [RetMask: Optimizing Retrieval Heads (arXiv 2601.11020)](https://arxiv.org/abs/2601.11020)\n- [CART: Circuit-Aware Reward Training (arXiv 2509.24713)](https://arxiv.org/abs/2509.24713)\n- [Circuit Breakers (NeurIPS 2024)](https://arxiv.org/abs/2406.04313)\n- [Adaptive Distraction (NeurIPS 2025)](https://arxiv.org/abs/2502.01609)\n- [EIT: Making Bias Non-Predictive (arXiv 2602.01528)](https://arxiv.org/html/2602.01528v2)\n- [Preference Heads (arXiv 2604.22345)](https://arxiv.org/abs/2604.22345)\n- [Locate, Steer, and Improve Survey (arXiv 2601.14004)](https://arxiv.org/abs/2601.14004)\n- [T-REG: Token-Level Reward (ACL 2025)](https://aclanthology.org/2025.acl-long.1353.pdf)\n- [Why Is RLHF Alignment Shallow? (arXiv 2603.04851)](https://arxiv.org/html/2603.04851)\n- [GSM-DC / Irrelevant Context (arXiv 2505.18761)](https://arxiv.org/abs/2505.18761)\n- [LLM Circuit Analyses Consistent Across Scale (NeurIPS 2024)](https://arxiv.org/abs/2407.10827)\n- [OPA-DPO](https://opa-dpo.github.io/)\n- [Attention Tracker for Prompt Injection (NAACL 2025)](https://aclanthology.org/2025.findings-naacl.123.pdf)"
      }
    ],
    "totalDurationMs": 243158,
    "totalTokens": 42011,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 449,
      "cache_creation_input_tokens": 1955,
      "cache_read_input_tokens": 36021,
      "output_tokens": 3586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1955
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 449,
          "output_tokens": 3586,
          "cache_read_input_tokens": 36021,
          "cache_creation_input_tokens": 1955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1955,
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
      "otherToolCount": 32
    }
  },
  "sourceToolAssistantUUID": "7d8cd711-6a3e-45f3-a82d-9cdc34c8072c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T08:51:58.134Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JLpwRqVfyXhG1MBqPmNrUo`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify RetMask and attention KL",
  "prompt": "I need you to do two focused verification tasks using WebSearch and WebFetch:\n\n**Task 1: Verify RetMask (arXiv:2601.11020)**\nSearch for \"RetMask retrieval heads DPO long-context arXiv 2601.11020\". I need to know:\n- Does this paper actually exist?\n- Does it combine mechanistic head identification (retrieval heads) with DPO training?\n- What exactly is its method?\n- How is it different from using an auxiliary attention KL loss during DPO?\n\nUse WebFetch on the arxiv page to read the abstract and method details.\n\n**Task 2: Search for attention-distribution KL as training objective**\nSearch for papers that use KL divergence between attention distributions as a training loss term:\n- Try: \"attention distribution KL divergence training loss language model\"\n- Try: \"attention transfer KL divergence distillation\"\n- Try: \"attention pattern matching training loss transformer\"\n\nI specifically want to know: has anyone used a model's own clean-input attention patterns as self-supervised targets for noisy-input training? This is the core technical novelty of Circuit-DPO.\n\n**Task 3: Search for \"Llama See Llama Do\" GQA architecture details**\n- Try: \"Llama 3 8B GQA grouped query attention heads\"\n- Confirm: Does Llama-3-8B use GQA (32 query heads, 8 KV heads) or standard MHA?\n- Does Llama-3.1-8B use the same architecture?\n\nReport findings with citations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61d7dc2a-7554-461e-bdf3-496d1fac313c",
  "isSidechain": false,
  "requestId": "req_011Cb7rcYndscyt2tPXb5Jr1",
  "type": "assistant",
  "uuid": "886606cf-b5b4-4583-84df-279758f186de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4HjHHaSaBB6abXZQPBXZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4340,
      "cache_read_input_tokens": 33745,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 33745,
          "cache_creation_input_tokens": 4340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4340
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "886606cf-b5b4-4583-84df-279758f186de",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Tool result

_source line 19 · 2026-05-17T08:54:55.657Z_

<details><summary>↩ Tool result · `toolu_01JLpwRqVfyXhG1MBqPmNrUo`</summary>

```text
Now I have comprehensive information. Let me compile the findings.

Here are the detailed findings for all three tasks:

---

## Task 1: RetMask (arXiv:2601.11020) -- Verified

**The paper exists.** Full title: "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models" by Youmi Ma and Naoaki Okazaki.

**Method:**
- RetMask identifies "retrieval heads" -- specific attention heads responsible for retrieving information from long contexts (building on prior mechanistic interpretability work).
- It creates an ablated model variant by zeroing out the columns in the attention output projection matrices of identified retrieval heads.
- For each input, it generates two responses: one from the normal model (chosen/preferred) and one from the ablated model (rejected).
- These synthetic preference pairs are used to train the model with **standard DPO** -- no modifications to the DPO objective itself.
- The masking is only used during data synthesis, not during the actual DPO training.

**Does it use attention KL divergence loss?** No. RetMask uses **no auxiliary attention loss whatsoever**. It does not constrain, regularize, or supervise attention distributions during training. The training objective is vanilla DPO on the synthetically generated preference pairs.

**How it differs from an auxiliary attention KL loss during DPO:**
- RetMask operates at the **data generation** level: it exploits retrieval heads to create contrastive training examples, then applies standard DPO.
- An auxiliary attention KL loss would operate at the **training objective** level: directly penalizing deviations in attention distributions during the DPO training loop.
- RetMask is indirect (better data -> better model); an attention KL approach would be direct (explicit gradient signal on attention patterns).

**Results:** +2.28 points on HELMET at 128K for Llama-3.1, +70% on generation with citation, +32% on passage re-ranking. Effectiveness depends on retrieval head concentration -- models with concentrated retrieval heads (like Llama-3.1) benefit most, while models with distributed patterns (like OLMo-3) show limited gains.

Sources:
- [arXiv:2601.11020 Abstract](https://arxiv.org/abs/2601.11020)
- [arXiv:2601.11020 Full HTML](https://arxiv.org/html/2601.11020v1)

---

## Task 2: Attention-Distribution KL as Training Objective -- Prior Art Assessment

### What exists in the literature:

1. **KL Attention Loss (KLAL):** An established technique using KL divergence to align model attention with **ground-truth** distributions. Applied in vision-language models (Esmaeilkhani et al., 2025 for visual grounding) and bias mitigation (Patel et al., 2024 for facial attributes; KLAAD at EMNLP 2025 for debiasing LLMs). In all cases, the target distribution comes from **external annotations** (geometric ground truth, class labels, or paired stereotype/anti-stereotype sentences), not from the model's own clean-input behavior.

2. **Attention Transfer in Knowledge Distillation:** Well-established (TinyBERT, MobileBERT, etc.) using MSE or KL divergence to align a **student** model's attention with a **teacher** model's attention. This is inter-model transfer, not self-supervised within a single model.

3. **AttentionDrop Consistency Regularization** (arXiv:2504.12088): Applies stochastic perturbations to attention distributions twice on the same input, then uses KL divergence between the two perturbed outputs as a consistency loss. This is similar in spirit but operates via random attention perturbation (R-Drop style), not via clean-vs-noisy input contrast.

4. **Guiding Attention for Self-Supervised Learning** (arXiv:2010.02399, EMNLP Findings 2020): Uses an auxiliary loss to guide attention heads to predefined patterns during pre-training. The targets are structural priors, not the model's own clean-input attention.

5. **DINO / Self-Distillation:** Uses KL between teacher (EMA) and student outputs for self-supervised learning, but this is over **output logits**, not attention distributions specifically.

### The specific novelty question:
**Has anyone used a model's own clean-input attention patterns as self-supervised targets for noisy/perturbed-input training?**

Based on extensive searching, **I found no prior work that does exactly this.** The closest approaches are:
- KLAL uses external ground-truth targets, not the model's own behavior.
- AttentionDrop uses consistency between two perturbed versions, not clean-vs-perturbed.
- Knowledge distillation transfers attention from teacher to student, not within the same model across input conditions.
- DINO-style self-distillation works on output distributions, not internal attention maps.

**This appears to be a genuine technical novelty for Circuit-DPO** -- using the model's own attention distributions on clean/unperturbed inputs as self-supervised targets for attention regularization during training on noisy/perturbed inputs.

Sources:
- [KL Attention Loss (KLAL) Overview](https://www.emergentmind.com/topics/kl-attention-loss-klal)
- [AttentionDrop: A Novel Regularization Method](https://arxiv.org/html/2504.12088)
- [Guiding Attention for Self-Supervised Learning with Transformers](https://arxiv.org/abs/2010.02399)
- [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias](https://arxiv.org/abs/2507.19962)
- [Attention-Based Distillation in LLMs: Overview](https://adasci.org/attention-based-distillation-in-llms-a-comprehensive-overview/)
- [Attention and Feature Transfer Based Knowledge Distillation](https://www.nature.com/articles/s41598-023-43986-y)

---

## Task 3: Llama-3 / Llama-3.1 8B GQA Architecture -- Confirmed

**Both Llama-3-8B and Llama-3.1-8B use GQA with identical attention architecture:**

| Parameter | Llama-3-8B | Llama-3.1-8B |
|-----------|-----------|-------------|
| num_attention_heads (query) | **32** | **32** |
| num_key_value_heads | **8** | **8** |
| num_hidden_layers | 32 | 32 |
| hidden_size | 4096 | 4096 |
| head_dim | 128 | 128 |
| intermediate_size | 14336 | 14336 |
| hidden_act | silu | silu |
| vocab_size | 128256 | 128256 |
| max_position_embeddings | 8192 | 131072 |
| rope_theta | 500000.0 | 500000.0 |

**Confirmed: Both use GQA, not standard MHA.** With 32 query heads and 8 KV heads, every group of 4 query heads shares one KV head. This is critical for any work involving per-head attention analysis -- there are 32 distinct query-head attention patterns per layer but only 8 distinct key-value projections.

The only meaningful architectural difference between Llama-3-8B and Llama-3.1-8B is the context length: 8K vs. 131K (achieved via RoPE scaling with factor 8.0, using the "llama3" rope type).

Sources:
- [config.json for Llama-3-8B](https://huggingface.co/unsloth/llama-3-8b/blob/main/config.json)
- [config.json for Llama-3.1-8B](https://huggingface.co/unsloth/Meta-Llama-3.1-8B/blob/main/config.json)
- [Meta Llama 3 Announcement](https://ai.meta.com/blog/meta-llama-3/)
- [Llama 3 Architecture Overview](https://www.emergentmind.com/topics/llama-3-architecture)
- [Sebastian Raschka: GQA in Llama](https://sebastianraschka.com/llms-from-scratch/ch04/04_gqa/)

agentId: aa3633c60466bcdcd (use SendMessage with to: 'aa3633c60466bcdcd' to continue this agent)
&lt;usage>total_tokens: 30554
tool_uses: 22
duration_ms: 177517&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "886606cf-b5b4-4583-84df-279758f186de",
  "isSidechain": false,
  "promptId": "a3d75b2b-6fea-4c0e-a4c1-2babd86d2ee9",
  "type": "user",
  "uuid": "abd8db55-bc4a-4d04-bf26-55da2d6904ce",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to do two focused verification tasks using WebSearch and WebFetch:\n\n**Task 1: Verify RetMask (arXiv:2601.11020)**\nSearch for \"RetMask retrieval heads DPO long-context arXiv 2601.11020\". I need to know:\n- Does this paper actually exist?\n- Does it combine mechanistic head identification (retrieval heads) with DPO training?\n- What exactly is its method?\n- How is it different from using an auxiliary attention KL loss during DPO?\n\nUse WebFetch on the arxiv page to read the abstract and method details.\n\n**Task 2: Search for attention-distribution KL as training objective**\nSearch for papers that use KL divergence between attention distributions as a training loss term:\n- Try: \"attention distribution KL divergence training loss language model\"\n- Try: \"attention transfer KL divergence distillation\"\n- Try: \"attention pattern matching training loss transformer\"\n\nI specifically want to know: has anyone used a model's own clean-input attention patterns as self-supervised targets for noisy-input training? This is the core technical novelty of Circuit-DPO.\n\n**Task 3: Search for \"Llama See Llama Do\" GQA architecture details**\n- Try: \"Llama 3 8B GQA grouped query attention heads\"\n- Confirm: Does Llama-3-8B use GQA (32 query heads, 8 KV heads) or standard MHA?\n- Does Llama-3.1-8B use the same architecture?\n\nReport findings with citations.",
    "agentId": "aa3633c60466bcdcd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the findings.\n\nHere are the detailed findings for all three tasks:\n\n---\n\n## Task 1: RetMask (arXiv:2601.11020) -- Verified\n\n**The paper exists.** Full title: \"From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models\" by Youmi Ma and Naoaki Okazaki.\n\n**Method:**\n- RetMask identifies \"retrieval heads\" -- specific attention heads responsible for retrieving information from long contexts (building on prior mechanistic interpretability work).\n- It creates an ablated model variant by zeroing out the columns in the attention output projection matrices of identified retrieval heads.\n- For each input, it generates two responses: one from the normal model (chosen/preferred) and one from the ablated model (rejected).\n- These synthetic preference pairs are used to train the model with **standard DPO** -- no modifications to the DPO objective itself.\n- The masking is only used during data synthesis, not during the actual DPO training.\n\n**Does it use attention KL divergence loss?** No. RetMask uses **no auxiliary attention loss whatsoever**. It does not constrain, regularize, or supervise attention distributions during training. The training objective is vanilla DPO on the synthetically generated preference pairs.\n\n**How it differs from an auxiliary attention KL loss during DPO:**\n- RetMask operates at the **data generation** level: it exploits retrieval heads to create contrastive training examples, then applies standard DPO.\n- An auxiliary attention KL loss would operate at the **training objective** level: directly penalizing deviations in attention distributions during the DPO training loop.\n- RetMask is indirect (better data -> better model); an attention KL approach would be direct (explicit gradient signal on attention patterns).\n\n**Results:** +2.28 points on HELMET at 128K for Llama-3.1, +70% on generation with citation, +32% on passage re-ranking. Effectiveness depends on retrieval head concentration -- models with concentrated retrieval heads (like Llama-3.1) benefit most, while models with distributed patterns (like OLMo-3) show limited gains.\n\nSources:\n- [arXiv:2601.11020 Abstract](https://arxiv.org/abs/2601.11020)\n- [arXiv:2601.11020 Full HTML](https://arxiv.org/html/2601.11020v1)\n\n---\n\n## Task 2: Attention-Distribution KL as Training Objective -- Prior Art Assessment\n\n### What exists in the literature:\n\n1. **KL Attention Loss (KLAL):** An established technique using KL divergence to align model attention with **ground-truth** distributions. Applied in vision-language models (Esmaeilkhani et al., 2025 for visual grounding) and bias mitigation (Patel et al., 2024 for facial attributes; KLAAD at EMNLP 2025 for debiasing LLMs). In all cases, the target distribution comes from **external annotations** (geometric ground truth, class labels, or paired stereotype/anti-stereotype sentences), not from the model's own clean-input behavior.\n\n2. **Attention Transfer in Knowledge Distillation:** Well-established (TinyBERT, MobileBERT, etc.) using MSE or KL divergence to align a **student** model's attention with a **teacher** model's attention. This is inter-model transfer, not self-supervised within a single model.\n\n3. **AttentionDrop Consistency Regularization** (arXiv:2504.12088): Applies stochastic perturbations to attention distributions twice on the same input, then uses KL divergence between the two perturbed outputs as a consistency loss. This is similar in spirit but operates via random attention perturbation (R-Drop style), not via clean-vs-noisy input contrast.\n\n4. **Guiding Attention for Self-Supervised Learning** (arXiv:2010.02399, EMNLP Findings 2020): Uses an auxiliary loss to guide attention heads to predefined patterns during pre-training. The targets are structural priors, not the model's own clean-input attention.\n\n5. **DINO / Self-Distillation:** Uses KL between teacher (EMA) and student outputs for self-supervised learning, but this is over **output logits**, not attention distributions specifically.\n\n### The specific novelty question:\n**Has anyone used a model's own clean-input attention patterns as self-supervised targets for noisy/perturbed-input training?**\n\nBased on extensive searching, **I found no prior work that does exactly this.** The closest approaches are:\n- KLAL uses external ground-truth targets, not the model's own behavior.\n- AttentionDrop uses consistency between two perturbed versions, not clean-vs-perturbed.\n- Knowledge distillation transfers attention from teacher to student, not within the same model across input conditions.\n- DINO-style self-distillation works on output distributions, not internal attention maps.\n\n**This appears to be a genuine technical novelty for Circuit-DPO** -- using the model's own attention distributions on clean/unperturbed inputs as self-supervised targets for attention regularization during training on noisy/perturbed inputs.\n\nSources:\n- [KL Attention Loss (KLAL) Overview](https://www.emergentmind.com/topics/kl-attention-loss-klal)\n- [AttentionDrop: A Novel Regularization Method](https://arxiv.org/html/2504.12088)\n- [Guiding Attention for Self-Supervised Learning with Transformers](https://arxiv.org/abs/2010.02399)\n- [KLAAD: Refining Attention Mechanisms to Reduce Societal Bias](https://arxiv.org/abs/2507.19962)\n- [Attention-Based Distillation in LLMs: Overview](https://adasci.org/attention-based-distillation-in-llms-a-comprehensive-overview/)\n- [Attention and Feature Transfer Based Knowledge Distillation](https://www.nature.com/articles/s41598-023-43986-y)\n\n---\n\n## Task 3: Llama-3 / Llama-3.1 8B GQA Architecture -- Confirmed\n\n**Both Llama-3-8B and Llama-3.1-8B use GQA with identical attention architecture:**\n\n| Parameter | Llama-3-8B | Llama-3.1-8B |\n|-----------|-----------|-------------|\n| num_attention_heads (query) | **32** | **32** |\n| num_key_value_heads | **8** | **8** |\n| num_hidden_layers | 32 | 32 |\n| hidden_size | 4096 | 4096 |\n| head_dim | 128 | 128 |\n| intermediate_size | 14336 | 14336 |\n| hidden_act | silu | silu |\n| vocab_size | 128256 | 128256 |\n| max_position_embeddings | 8192 | 131072 |\n| rope_theta | 500000.0 | 500000.0 |\n\n**Confirmed: Both use GQA, not standard MHA.** With 32 query heads and 8 KV heads, every group of 4 query heads shares one KV head. This is critical for any work involving per-head attention analysis -- there are 32 distinct query-head attention patterns per layer but only 8 distinct key-value projections.\n\nThe only meaningful architectural difference between Llama-3-8B and Llama-3.1-8B is the context length: 8K vs. 131K (achieved via RoPE scaling with factor 8.0, using the \"llama3\" rope type).\n\nSources:\n- [config.json for Llama-3-8B](https://huggingface.co/unsloth/llama-3-8b/blob/main/config.json)\n- [config.json for Llama-3.1-8B](https://huggingface.co/unsloth/Meta-Llama-3.1-8B/blob/main/config.json)\n- [Meta Llama 3 Announcement](https://ai.meta.com/blog/meta-llama-3/)\n- [Llama 3 Architecture Overview](https://www.emergentmind.com/topics/llama-3-architecture)\n- [Sebastian Raschka: GQA in Llama](https://sebastianraschka.com/llms-from-scratch/ch04/04_gqa/)"
      }
    ],
    "totalDurationMs": 177517,
    "totalTokens": 30554,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 999,
      "cache_read_input_tokens": 27477,
      "output_tokens": 2077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 999
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2077,
          "cache_read_input_tokens": 27477,
          "cache_creation_input_tokens": 999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 999,
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
  "sourceToolAssistantUUID": "886606cf-b5b4-4583-84df-279758f186de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-17T08:56:13.677Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile all findings and form my review. Let me assess the Round 2 proposal against the Round 1 feedback:

### Round 1 Issues — What Was Fixed?

1. **Theoretical premise (CRITICAL)**: Round 1 said the "double-bind" premise was overstated since ablating entrainment heads costs only 0.2-3% ICL. Round 2 reframes: inference-time masking is "blunt" (binary all-or-nothing suppression) and task-specific (heads must be rediscovered per task). Training-time modification enables "graded, query-conditional" behavior. 

That's a much stronger framing. ✅ Fixed.

2. **EIT baseline (CRITICAL)**: Round 2 now includes EIT as a primary baseline and discusses the +39.1% result. The framing differentiates: EIT's transfer is cross-bias-type (bandwagon→distraction), not within-distraction OOD. ✅ Fixed.

3. **Venue mismatch**: User asked for EMNLP 2026 ARR. Round 2 targets ICLR 2027 (Sep 24, 2026) and ARR October 2026. But EMNLP 2026 uses the May 2026 ARR cycle (deadline May 25, 2026, which is 8 days away). The October ARR cycle feeds into NAACL 2027 or ACL 2027 instead. The proposal acknowledges this infeasibility but doesn't explicitly state that EMNLP 2026 is no longer the target. ⚠️ Partially addressed.

4. **Model mismatch**: Round 2 now uses Llama-3-8B and Qwen2.5-7B. ✅ Fixed.

5. **Architecture risk**: I'm checking whether Llama-3.1-8B and Llama-3-8B share the same GQA configuration...

they both use 32Q/8KV with query-head granularity masking. Qwen2.5-7B has a different ratio at 28Q/4KV, and the proposal acknowledges this difference and proposes masking at the same granularity level. ✅ Addressed.

6. **CHG and Gated Attention**: Both are properly positioned—CHG as an analysis tool rather than a training method, and Gated Attention as a complementary architectural modification. ✅ Fixed.

7. **Attention target construction**: The approach now uses self-supervised clean/noisy pairing where the model's own attention on clean inputs becomes the training target, eliminating the need for external relevance annotations. ✅ Fixed.

8. **Resource estimates**: Converted to H100 hours at 170-200h, which stays within budget. ✅ Fixed.

Looking at the strengths now, the self-supervised attention target construction with clean/noisy pairing is genuinely innovative.

RetMask is the closest related work but uses mechanistic heads for synthetic data generation in DPO, not as an auxiliary attention loss like this approach does. FPO operates on SAE features at a different granularity than attention distributions. The method itself is clean and implementable, and the recent "Locate, Steer, and Improve" survey confirms that training-time mechanistic interpretability integration remains underexplored, which supports the novelty claim.

There's still a venue mismatch though—the user asked for EMNLP 2026, but the proposal is targeting ICLR 2027 and ARR October 2026 for NAACL/ACL 2027.  The EMNLP 2026 ARR deadline is May 25, which is infeasible, so I need to explicitly flag this and get buy-in for the venue pivot. I should also clarify the distinction between EIT's cross-bias-type transfer improvements and Circuit-DPO's within-distraction OOD generalization—they're optimizing different axes. There's also a lingering concern about whether the clean-attention target is actually valid for the method.

The core issue is that clean inputs have no distractors, so attention naturally concentrates on relevant context. When distractors appear, the model should still attend to relevant content, but the attention distribution will shift just from the presence of additional tokens and the softmax renormalization across all positions. The proposal tries to handle this by renormalizing only over shared positions, but that's still a rigid constraint—even attention over the original context positions may legitimately change when new irrelevant tokens are added, since softmax operates jointly across everything. I'm concerned this might be overconstrained. On the λ sensitivity front, the method uses a linearly annealed auxiliary loss weight starting from zero over the first 20% of training, but I need to think through whether this schedule is actually well-justified.

The bigger concern is whether the entrainment heads identified before training remain the right targets after the model has been modified by Circuit-DPO. And since the paper emphasizes that entrainment is task-specific, the heads that matter for math reasoning distraction might be completely different from those for factual recall. That means I'd need to rediscover heads for each new task domain rather than reusing the same ones across different reasoning types.

Now I'm evaluating the novelty here. The core idea of using self-supervised attention KL on mechanistically-identified heads is genuinely novel—no prior work combines these pieces exactly this way. The individual components like DPO, attention KL, and entrainment heads are established, but the specific combination is non-obvious and well-motivated. The survey on training-time mechanistic integration confirms this is underexplored territory, and the formulation of self-supervised attention targets from clean/noisy pairs feels like a solid incremental contribution that bridges mechanistic interpretability with preference learning in a way that hasn't been done before.

On feasibility, the method is implementable with existing components—head discovery code is public, DPO infrastructure is standard, and the attention KL loss is straightforward. The 200 H100-hour budget seems reasonable, though there are real implementation challenges: entrainment heads are task-specific so discovery needs repeating per domain, clean-attention targets might be too rigid due to softmax renormalization, λ tuning could be finicky, and heads may shift during training. These aren't blockers but they're genuine risks to account for.

The proposal itself is well-written with clear method formulation, well-stated hypotheses, and a comprehensive evaluation plan, though there are minor gaps around venue fit and some missing baseline comparisons.

On impact, if this works it bridges mechanistic interpretability and alignment training nicely. But the practical value hinges on how much it improves over EIT, which already achieves strong +39.1% OOD generalization through simpler behavioral RL. If Circuit-DPO only marginally outperforms EIT, the added complexity of head discovery and attention KL might not justify the extra effort. The mechanistic angle is intellectually valuable but may not translate to substantial real-world gains.

Averaging these scores puts me below the 4.0 threshold, so this needs revision. Looking back at what the Round 2 revision actually addressed from Round 1, I should be more precise about what's still broken. The venue mismatch is a clear structural problem that needs fixing.

Now I'm reconsidering whether I'm being too harsh. The real issues are the venue mismatch, the missing RetMask baseline, and the methodological concern about using clean attention as a target. These are all fixable problems. The core question is whether this reaches top-venue caliber for somewhere like ICLR 2027 or EMNLP. The idea has genuine strengths—it connects two active research areas, proposes clear testable hypotheses, and includes a novel technical contribution with attention KL on entrainment heads. But it's also incremental in nature; adding an auxiliary loss to DPO isn't a major methodological leap, and the core insight about using clean attention as a target is fairly straightforward. The gains over EIT might be modest, and the theoretical justification for graded versus binary suppression needs to be more convincing. This feels borderline to me.

Looking at the specific scores, I'd place novelty at 3.5 since it's a novel combination but the individual pieces are established, and I haven't seen RetMask discussed. Feasibility is also 3.5 given the implementability but several technical risks. Clarity is solid at 4. Impact is the tricky one at 3, since it hinges on whether the empirical results beat EIT and whether the mechanistic insights about entrainment heads prove valuable. The three testable hypotheses—especially stronger OOD generalization and composability with EIT—could genuinely matter if they hold up. But EIT's +39.1% improvement sets a high bar. My verdict is revise rather than reject. at 3.

Hmm, let me also reconsider novelty more carefully. The self-supervised attention target is genuinely novel (confirmed by my search). The application to mechanistically-identified heads specifically (not all heads) is a meaningful design choice with strong justification. RetMask uses heads for data generation, not auxiliary loss — different approach. FPO uses SAE features, not attention. This combination really is novel. Maybe 4 for novelty?

Actually no — let me remember: "4 means 'this is really good', 5 means 'exciting'." The novelty is solid but not exciting. It's a well-motivated combination of existing techniques. 3.5 is fair.

Let me finalize:
- Novelty: 3.5
- Feasibility: 3.5  
- Clarity: 4
- Impact: 3

Average: 3.5. Verdict: revise.

Now I need to identify the main issues to address: the venue choice doesn't align with what was requested, I missed discussing RetMask as a related work, there's a question about whether the clean-attention target is actually valid, the impact argument needs more concrete comparison to existing interpretability techniques, and the fact that entrainment heads are task-specific creates complications for the method's generalizability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abd8db55-bc4a-4d04-bf26-55da2d6904ce",
  "isSidechain": false,
  "requestId": "req_011Cb7rrbXUwLLW1fGkqwZL2",
  "type": "assistant",
  "uuid": "04d9b80a-c333-4d1f-8ccd-4d70c6ec8bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1kTcEoi7LffThbBVsCUud",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 38085,
      "output_tokens": 5153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5153,
          "cache_read_input_tokens": 38085,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2620
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

_source line 21 · 2026-05-17T08:56:58.432Z_

Now let me synthesize all findings into my review.

My research agents have completed their investigations. Here are the key findings:

**Verification results:**
- "Llama See, Llama Do" claims verified (ACL 2025, Outstanding Paper). Both Llama-3-8B and Llama-3.1-8B use identical GQA (32Q/8KV) — the proposal correctly notes architectural transfer is direct.
- EIT verified: +39.1% cross-bias-type transfer (bandwagon→distraction), not within-distraction OOD.
- CHG confirmed as analysis tool only; Gated Attention confirmed as NeurIPS 2025 Best Paper.
- Self-supervised attention KL on clean/noisy pairs is **genuinely novel** — no prior work does this exactly.
- **Critical omission found: RetMask (arXiv:2601.11020)** — combines mechanistic head identification with DPO training, though via data generation (not auxiliary loss).
- EMNLP 2026 uses May 2026 ARR cycle (deadline May 25, 2026) — October ARR feeds NAACL/ACL 2027, not EMNLP 2026.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "Self-supervised attention KL on mechanistically-identified entrainment heads is genuinely novel (no prior work confirmed), but individual components (DPO, attention KL, entrainment heads) are known — the contribution is a well-motivated combination. RetMask (arXiv:2601.11020) is an uncited close competitor that also bridges mechanistic head identification with DPO training, differing in mechanism (data generation vs. auxiliary loss) but sharing the core philosophy."},
    "feasibility": {"score": 3.5, "rationale": "All components exist and are implementable within 200 H100-hours. However, three technical risks are underaddressed: (1) entrainment heads are task-specific per the source paper, requiring per-domain rediscovery; (2) softmax renormalization means clean-input attention distributions over shared positions may legitimately differ from noisy-input distributions even for 'correct' behavior, making the KL target potentially too rigid; (3) entrainment heads may shift during Circuit-DPO training, invalidating the pre-training head identification."},
    "clarity": {"score": 4, "rationale": "The method formulation is precise (L = L_DPO + λ·KL), the three testable hypotheses are well-stated, the evaluation plan is comprehensive with appropriate ablations, and the reframing from 'double-bind' to 'graded vs. binary control' is defensible. Minor gaps in competitor discussion."},
    "impact": {"score": 3, "rationale": "EIT already achieves +39.1% OOD generalization through simpler behavioral RL, setting a high bar. Circuit-DPO's advantage (mechanistic targeting → better within-distraction OOD generalization) is plausible but unproven, and the added complexity of entrainment head discovery + attention KL may not yield sufficient gains over EIT to justify the approach. The mechanistic interpretability angle is valuable for the community but may not translate to large practical improvements."}
  },
  "issues": [
    "VENUE MISMATCH (persists) — User explicitly requested 'Target: EMNLP 2026, ARR submission.' EMNLP 2026 uses the May 2026 ARR cycle (deadline May 25, 2026 — 8 days away), making it infeasible. The proposal targets ICLR 2027 and ARR October 2026 but does not explicitly acknowledge that EMNLP 2026 is infeasible or seek user buy-in for the venue change. October 2026 ARR feeds into NAACL 2027 or ACL 2027, not EMNLP 2026.",
    "MISSING COMPETITOR — RetMask (arXiv:2601.11020, Jan 2026) combines mechanistic head identification (retrieval heads) with DPO training for long-context tasks. While RetMask uses heads for synthetic preference DATA GENERATION rather than as an auxiliary attention loss, it shares Circuit-DPO's core philosophy of bridging mechanistic interpretability with preference optimization. This is the most important uncited concurrent work and must be discussed with clear differentiation.",
    "CLEAN-ATTENTION TARGET VALIDITY — The method assumes attention distributions on clean inputs (without distractors) represent 'correct' attention for entrainment heads. However, softmax attention is computed jointly over ALL positions. Even after renormalizing A_noisy over shared positions, the attention distribution legitimately changes when new tokens are present (distractors compete for attention mass, altering the softmax denominator). Forcing renormalized-noisy attention to match clean attention may be an overly rigid constraint that could suppress beneficial attention redistribution. The proposal should: (a) acknowledge this limitation, (b) consider softer constraints (e.g., upper bound on KL rather than minimizing it, or using Jensen-Shannon divergence with temperature), (c) provide theoretical or empirical justification for why exact matching is the right target.",
    "ENTRAINMENT HEAD STABILITY DURING TRAINING — The differentiable masking identifies entrainment heads PRE-training. As Circuit-DPO modifies these heads' behavior, the originally-identified heads may no longer be the primary entrainment circuit. Should head discovery be repeated periodically during training? The proposal includes no mechanism for this and no ablation studying head stability across training.",
    "TASK-SPECIFICITY COMPLICATION — 'Llama See, Llama Do' explicitly states entrainment heads are 'task-specific, not model-specific.' The proposal trains on math distractor data (GSM-DC, NoisyBench) — but the entrainment heads for math reasoning may differ from those for reading comprehension, QA, or other tasks. This undermines the generalization claims: even if Circuit-DPO generalizes to novel DISTRACTOR types within math, does it generalize to novel TASK types? Head discovery must be repeated per domain, adding hidden compute cost and limiting the method's generality.",
    "IMPACT CASE VS. EIT INSUFFICIENTLY ARGUED — EIT achieves +39.1% OOD generalization through purely behavioral RL without any mechanistic targeting. The proposal claims Circuit-DPO provides 'stronger within-distraction OOD generalization' but does not articulate a clear mechanistic argument for WHY circuit-level targeting would outperform EIT's balanced conflict strategy on this specific metric. The composability hypothesis (H3: Circuit-DPO + EIT) is interesting but is positioned as tertiary rather than the central argument."
  ],
  "feedback": "The revision successfully addressed the most critical Round 1 issues (theoretical reframing, EIT inclusion, model/resource alignment), and the self-supervised clean/noisy attention target is a genuinely novel contribution confirmed by literature search. To reach pass threshold:\n\n1. **Venue**: Explicitly acknowledge EMNLP 2026 infeasibility (May 25 ARR deadline). State the venue pivot clearly: primary ICLR 2027 (Sep 24, 2026), backup ARR October 2026 → NAACL/ACL 2027.\n\n2. **Cite RetMask (arXiv:2601.11020)**: This is the closest concurrent work — it also bridges mechanistic head identification with DPO. Differentiate clearly: RetMask uses heads for contrastive data generation (indirect), Circuit-DPO uses heads as auxiliary loss targets (direct gradient signal on attention). RetMask enhances retrieval capability; Circuit-DPO suppresses entrainment selectively.\n\n3. **Soften the attention KL target**: Replace strict KL minimization with a bounded constraint or temperature-scaled divergence. Acknowledge that exact attention matching after softmax renormalization is overly rigid. Consider: (a) KL with a slack margin, (b) only penalizing large deviations, (c) projecting attention onto a lower-dimensional space before matching.\n\n4. **Address head stability**: Add an ablation studying whether entrainment heads remain stable during Circuit-DPO training. If they shift, propose periodic re-identification (e.g., every N steps) or a warm-start approach.\n\n5. **Strengthen impact argument against EIT**: Elevate hypothesis H3 (composability) to the primary contribution frame. Argue: 'Circuit-DPO and EIT operate at orthogonal levels (circuit mechanism vs. behavioral reward). Their combination should yield additive benefits because they address different aspects of the distraction vulnerability.' This is a stronger position than claiming Circuit-DPO alone beats EIT.\n\n6. **Task-specificity**: Explicitly scope the generalization claims. If entrainment heads are task-specific, state that Circuit-DPO generalizes across distractor types within a task domain, and add a cross-domain transfer experiment as exploratory (not a central claim).",
  "reason": "Solid technical contribution with genuinely novel self-supervised attention KL mechanism, but missing a key competitor (RetMask), venue mismatch persists, and several methodological concerns (attention target rigidity, head stability, task-specificity) need addressing to reach top-venue threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04d9b80a-c333-4d1f-8ccd-4d70c6ec8bae",
  "isSidechain": false,
  "requestId": "req_011Cb7rrbXUwLLW1fGkqwZL2",
  "type": "assistant",
  "uuid": "d09ac48b-7845-4f6e-921b-cb73548551d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1kTcEoi7LffThbBVsCUud",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 38085,
      "output_tokens": 5153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5153,
          "cache_read_input_tokens": 38085,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2620
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d09ac48b-7845-4f6e-921b-cb73548551d7",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d09ac48b-7845-4f6e-921b-cb73548551d7",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-DPO: Distraction-Invariant Attention via Mechanistically-Targeted Preference Optimization",
  "sessionId": "1f0e797b-0a1e-4f77-9732-430b6c13ecc8"
}
```

---
