# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-17 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/809e0f3d-cfab-4e41-bee2-451342909dac.jsonl`
- **Structured JSON:** [`d052ab3469d190210446.json`](../../sessions/d0/d052ab3469d190210446.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T08:58:39.214Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T08:58:39.214Z",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-17 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission. Track: Machine Learning for NLP / Question Answering.\n\nDirection: Training-time mechanistic fix for contextual entrainment — teaching LLMs to\nselectively suppress irrelevant-context influence while preserving in-context learning,\nby targeting the shared attention circuit that enables both. LLMs exhibit \"contextual\nentrainment\": attention heads mechanistically assign higher logits to ANY token previously\nseen in context, regardless of task relevance (ACL 2025, \"Llama See, Llama Do\"). This\nis the same mechanism that powers in-context learning — creating a fundamental double-bind\nwhere suppressing entrainment destroys ICL. Existing training fixes (DPO on distractor\ndata, RARE reward, data augmentation) are purely behavioral: they teach models to produce\ncorrect outputs DESPITE entrainment still occurring internally. These behavioral fixes\ndo not generalize to novel distractor types, require task-specific distractor exposure\nduring training, and fail on complex reasoning (SFT fails entirely; even RL-based RARE\nshows limited transfer). No training method targets the entrainment circuit itself to\nmake it relevance-conditional.\n\nSeed Papers:\n- \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction\n  in LLMs\" (ACL 2025) — identifies the mechanism: specific \"entrainment heads\" boost\n  logits for all context-seen tokens; these SAME heads enable in-context learning;\n  proposes inference-time head masking but no training fix\n- \"Focus Directions Make Your Language Models Pay More Attention to Relevant Contexts\"\n  (arXiv:2503.23306, Mar 2025) — identifies \"contextual heads\" and \"focus directions\"\n  in key/query space that control attention routing; proposes activation steering at\n  inference time only\n- \"Lost in the Noise: How Reasoning Models Fail with Contextual Distractors\"\n  (arXiv:2601.07226, Jan 2026) — proves SFT and outcome-reward RL FAIL for complex\n  reasoning under distraction; only RARE (rationale-aware reward) partially works;\n  reveals inverse scaling where more test-time compute worsens distraction vulnerability\n- \"How Is LLM Reasoning Distracted by Irrelevant Context?\" (EMNLP 2025 Oral,\n  arXiv:2505.18761) — GSM-DC benchmark; shows continued pretraining with distractors\n  helps on simple math but generalizes poorly; full fine-tuning > LoRA\n- \"Adaptive Distraction\" (NeurIPS 2025, arXiv:2502.01609) — DPO on synthetic adversarial\n  distractors; behavioral fix that improves robustness but does not modify the entrainment\n  circuit; requires exposure to specific distractor types during training\n- \"Reducing Distraction in Long-Context Language Models by Focused Learning\"\n  (arXiv:2411.05928, Nov 2024) — contrastive learning between full-context and\n  retrieved-relevant-only contexts; closest to mechanistic but does not specifically\n  target entrainment heads or the ICL-distraction shared circuit\n\nKnown Gaps:\n- No training method targets the ENTRAINMENT CIRCUIT (the specific attention heads\n  identified in \"Llama See, Llama Do\") — all existing fixes are behavioral\n- The fundamental double-bind is unaddressed: entrainment heads enable BOTH ICL and\n  distraction vulnerability; no principled mechanism exists to make them relevance-conditional\n- Behavioral fixes (DPO, RARE) do not generalize: they work for distractor types seen\n  during training but fail on novel distraction patterns (proven by transfer experiments)\n- SFT completely fails for complex reasoning under distraction (Jan 2026) — simple\n  data augmentation is insufficient\n- The inverse scaling finding (more test-time compute = more distraction vulnerability)\n  suggests the problem is architectural, not behavioral\n- No training loss directly penalizes the entrainment pattern while preserving the\n  ICL pattern in the same heads\n\nIn-scope: Training-time interventions that modify the entrainment circuit's behavior\nto become relevance-conditional, rather than teaching downstream reasoning to compensate.\nSpecifically: attention regularization that penalizes entrainment strength on tokens\nprovably irrelevant to the task while preserving it for relevant tokens, contrastive\nhead training where the same passage appears as relevant (for one query) and irrelevant\n(for another query) and entrainment heads must modulate accordingly, relevance-gated\nentrainment where the model learns a query-dependent gating mechanism on entrainment\nheads during training, circuit-level DPO where preferences target internal attention\npatterns (not just output correctness), progressive training from strong distractors\n(lexically unrelated) to subtle distractors (semantically adjacent but irrelevant).\n\nNOT in-scope: Inference-time activation steering (Focus Directions already does this),\npure data augmentation with distractors (proven insufficient for complex tasks), DPO/RARE\nthat only targets output behavior without modifying the entrainment mechanism, methods\nrequiring explicit relevance labels at inference time, post-hoc detection and regeneration,\nprompt engineering for distractor resistance.\n\nContribution type: METHOD ONLY. Must propose a concrete training-time intervention that\nmodifies the entrainment circuit to become relevance-conditional. The method must\ndemonstrate: (1) improved distractor robustness compared to behavioral baselines (DPO,\nRARE), (2) preserved in-context learning ability (ICL benchmarks must not degrade),\n(3) generalization to novel distractor types NOT seen during training (the key advantage\nover behavioral fixes), (4) no reliance on explicit relevance signals at inference time.\n\nEVAL PROTOCOL:\nTRAIN: Fine-tune from existing checkpoints (Llama-3-8B, Qwen2.5-7B/14B) with\nentrainment-aware training objective.\nEVALUATE on:\n- Distractor robustness: GSM-DC, GSM-NoOp, custom distractor benchmarks across\n  difficulty levels\n- ICL preservation: standard few-shot benchmarks (MMLU, BBH, ARC) must NOT degrade\n- Generalization to novel distractors: test on distractor types NOT in training data\n  (lexical, semantic, structural, adversarial)\n- Comparison against behavioral baselines: DPO (NeurIPS 2025), RARE (Jan 2026),\n  SFT on distractor data, vanilla model\n- Comparison against inference-time fixes: Focus Directions, entrainment head masking\n- Mechanistic analysis: entrainment head activation before/after training, showing\n  selective suppression for irrelevant context\n- Transfer: does fixing entrainment on math distractors transfer to reading comprehension\n  distractors? (behavioral fixes don't transfer well)\n- Ablation: which training signal components drive generalization vs. in-domain improvement\n- Inverse scaling test: does the fix resolve the \"more compute = more vulnerable\" pattern?\n\nBuilding blocks: Open models (Llama-3-8B, Qwen2.5-7B/14B), mechanistic analysis tools\n(attention head probing from \"Llama See, Llama Do\"), Focus Directions implementation\nfor comparison, GSM-DC/GSM-NoOp benchmarks, synthetic distractor generation, DPO/RLHF\ninfrastructure, ICL evaluation suites.\n\nHARD CONSTRAINTS:\nCompute: ≤200 H100-hours total. Fine-tune from existing checkpoints.\nEval: Must report BOTH distractor robustness AND ICL preservation. A method that\neliminates distraction by destroying ICL is NOT acceptable (this is the double-bind).\nMust demonstrate generalization to UNSEEN distractor types — this is the key metric\nthat distinguishes mechanistic fixes from behavioral ones.\nMust include mechanistic analysis showing entrainment head behavior change (not just\noutput accuracy improvement).\n\nLook for: Query-conditional gating on entrainment heads that learns to modulate\nentrainment strength based on query-context alignment (the heads remain active for ICL\nbut suppress for irrelevant context); contrastive training at the ATTENTION level where\nthe same document is presented as relevant-context (for query A) and irrelevant-context\n(for query B) and the model's entrainment heads must respond differently; progressive\nrelevance curriculum starting from easy discrimination (completely unrelated distractors)\nto hard discrimination (topically related but task-irrelevant context); circuit-level\npreference learning where DPO targets not just output correctness but internal attention\ndistribution over relevant vs. irrelevant context tokens.\n\nAvoid: Pure data augmentation with distractors (EMNLP 2025 already shows this is\ninsufficient), standard DPO on output behavior only (NeurIPS 2025 already does this),\ninference-time steering (Focus Directions already does this), methods that require\nknowing which context is irrelevant at inference time (must be internalized), simple\nattention regularization without query-conditioning (would destroy ICL), approaches\nthat only work on math/arithmetic distractors.\n\nIDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):\n\n1. No strawman problems: The entrainment mechanism must cite \"Llama See, Llama Do\"\n   specifically. The failure of behavioral fixes must cite \"Lost in the Noise\" (Jan 2026)\n   and NeurIPS 2025 DPO paper. The ICL-distraction shared circuit claim must be grounded\n   in the mechanistic evidence from the ACL 2025 paper.\n\n2. No observation-only ideas: Discovering new distractor failure modes is NOT a\n   contribution. Must propose a complete training method targeting the entrainment circuit.\n\n3. No mediocre methods: Your method MUST answer:\n   - Core Insight: What structural property of the entrainment circuit makes it possible\n     to selectively suppress distraction without killing ICL?\n   - Why Not Obvious: Why doesn't DPO/RARE already solve this? (Hint: they fix behavior\n     not mechanism, so they don't generalize to novel distractors)\n   - Information Exploited: What signal about \"this context is irrelevant\" do you use\n     during training that behavioral methods don't? How do you get this signal without\n     requiring relevance labels at inference time?\n   - Mechanistic Argument: From the entrainment head mechanism, explain WHY your\n     intervention makes these heads query-conditional rather than unconditionally boosting\n     all context tokens.\n   \"Add distractor data to training\" is REJECTED (EMNLP 2025 already proves this is\n   insufficient). \"Do DPO with distractor preferences\" is REJECTED (NeurIPS 2025 already\n   does this — behavioral fix). Must explain what is structurally different about your\n   approach at the CIRCUIT level.\n\n4. No rehashing: Search \"contextual entrainment training fix\", \"distraction robustness\n   training LLM\", \"attention head regularization relevance\" with 3+ queries. Differentiate\n   from: DPO distractor training (behavioral), RARE (behavioral RL), Focus Directions\n   (inference-time), data augmentation (insufficient for complex tasks).\n\n5. No experiment-padding: The insight must explain the structural relationship between\n   entrainment heads, ICL, and distraction — and why your intervention can surgically\n   modify one function (distraction) without destroying the other (ICL). This is the\n   theoretical contribution.\n\n6. Method pattern restrictions: \"Train with more distractors\" REJECTED (proven\n   insufficient). \"DPO on distractor outputs\" REJECTED (already exists, behavioral only).\n   \"Regularize attention heads\" needs justification for why this doesn't destroy ICL.\n   \"Contrastive learning\" needs explanation of what makes the contrastive signal operate\n   at the CIRCUIT level rather than the behavioral level.\n\nTHEORETICAL ANCHOR: The fundamental problem is that contextual entrainment is a\nDUAL-USE mechanism: the same attention heads that boost logits for context-seen tokens\n(causing distraction) ALSO enable in-context learning (where boosting context-seen tokens\nIS the correct behavior). The training fix must make this mechanism QUERY-CONDITIONAL:\nactive when context is relevant to the current query (ICL mode) and suppressed when\ncontext is irrelevant (distraction resistance mode). The key difficulty is that\n\"relevance\" is not a fixed property of context — the same passage can be relevant for\none query and irrelevant for another. Therefore, the gating cannot be a static property\nof the context; it must be dynamically computed from query-context interaction. Possible\napproaches: (1) train a relevance-gating layer that modulates entrainment head output\nbased on query-key alignment scores (learned during training, internalized at inference),\n(2) contrastive training at the HEAD level where the same context appears in relevant\nand irrelevant roles, forcing the model to develop query-conditional entrainment,\n(3) progressive curriculum from easy relevance discrimination to hard (topically similar\nbut task-irrelevant), (4) auxiliary loss on entrainment head attention patterns that\npenalizes uniform boosting and rewards selective boosting correlated with downstream\ntask relevance.\n\nCRITICAL DIFFERENTIATION from existing work:\n- vs. DPO/RARE (behavioral): Your method modifies the entrainment CIRCUIT, not just\n  output behavior. Key evidence: generalization to unseen distractor types.\n- vs. Focus Directions (inference-time): Your method internalizes relevance-gating\n  during training; no steering needed at inference time.\n- vs. Data augmentation (EMNLP 2025): Your method provides a TRAINING SIGNAL at the\n  attention head level, not just more examples. Key evidence: works on complex reasoning\n  where data augmentation fails.\n- vs. Entrainment head masking (ACL 2025): Your method preserves the heads but makes\n  them conditional, rather than ablating them entirely (which destroys ICL).\n\nTag: direction=contextual_entrainment_fix, contribution_type=method,\nsub_direction=relevance_conditional_entrainment, target_venues=[\"EMNLP 2026\", \"ACL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-17?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"Contrastive Entrainment Calibration: Query-Conditional Attention Training via Role-Switching Pairs\",\n  \"core_problem\": \"Entrainment heads unconditionally boost all context-seen tokens regardless of task relevance (ACL 2025). The only known circuit-level intervention — ablating these heads — is a static, query-agnostic operation: it removes all entrainment regardless of whether the context is relevant or irrelevant to the current query. While ablation attenuates distraction, it was validated only on three simple ICL tasks (spelling, translation, arithmetic) and overall MMLU (56.3→55.5%); its effects on complex reasoning (BBH, multi-hop QA) and beneficial context use (RAG, grounded QA) remain untested. Meanwhile, behavioral fixes (DPO, RARE) do not modify the entrainment circuit and show limited generalization to novel distractor types. Gated Attention (NeurIPS 2025 Best Paper) introduces query-conditional per-head sigmoid gating that can modulate attention heads dynamically — but this is an architectural change requiring pre-training from scratch (tested at 3.5T tokens on 15B MoE models), making it inapplicable to the billions of existing deployed models. How can we make entrainment heads in EXISTING models query-conditional — boosting context tokens when relevant while suppressing them when irrelevant — via lightweight fine-tuning rather than architectural redesign?\",\n  \"opportunity\": \"The gap is now three-sided: (1) pre-training architectural solutions (Gated Attention) achieve query-conditional gating but require training from scratch and do not target entrainment specifically; (2) static circuit intervention (ablation) is query-agnostic — it removes all entrainment regardless of context relevance; (3) behavioral training (DPO/RARE) is query-aware but mechanism-agnostic — it never modifies the entrainment circuit and shows limited generalization. No work provides query-conditional circuit-level control of entrainment heads in existing models via fine-tuning.\\n\\nFour convergent advances make this feasible: (1) ABFT (arXiv:2505.14233) proved that attention-score training objectives can efficiently modify specific head behavior by fine-tuning Q/K projections with ~512 samples; (2) MuDAF (arXiv:2502.13963) showed contrastive Q-K learning on retrieval heads improves multi-document QA on Llama-3.1-8B (HotpotQA 69.6%, MuSiQue 48.2%), but targets retrieval heads (not entrainment heads), does not test ICL preservation, does not test novel distractor generalization, and becomes unstable when training all heads (only 8 heads stable); (3) CHG (NeurIPS 2025, arXiv:2505.13737) demonstrates via causal analysis that attention head roles are context-dependent — the same head can be facilitating, interfering, or irrelevant depending on the task — directly supporting the premise that entrainment heads CAN be made query-conditional rather than being inherently unconditional; (4) the Hapax finding (arXiv:2511.05743) that abstractive ICL is preserved even when induction-head gradients are removed suggests ICL is distributed and robust to head-level modification.\\n\\nThe key structural insight is that role-switching contrastive pairs — where the SAME passage serves as relevant context for one query but irrelevant distractor for another — provide a natural training signal for query-conditioning. This extends the Focused Transformer (NeurIPS 2023, arXiv:2307.03170) paradigm of contrastive training for attention distraction reduction, but differs fundamentally: FoT applies contrastive learning to the general key-value space with crossbatch negatives to improve key separability; CEC applies contrastive learning specifically to entrainment head Q/K projections with role-switching pairs that force query-conditional behavior.\",\n  \"landscape\": \"**Circuit-level understanding of entrainment.** The entrainment mechanism is established by 'Llama See, Llama Do' (ACL 2025, aclanthology.org/2025.acl-long.791): 3.2–10.7% of attention heads (e.g., 36 of 1024 in Llama-3.1-8B for country–capital) cause unconditional context token boosting, identified via differentiable Gumbel-sigmoid binary masking. Ablating these heads has 'negligible to small effect' on ICL: arithmetic 100→100%, spelling 1-shot 73.6→72.0% (−1.6%), translation 1-shot 74.4→73.0% (−1.4%), overall MMLU 56.3→55.5% (−0.8%). However, ablation was tested only on these simple tasks; its impact on complex reasoning (BBH, multi-hop QA) and context-dependent tasks (RAG, grounded QA) remains untested. We hypothesize that ablation's indiscriminate removal of context influence will degrade performance on context-dependent tasks even if simple ICL is preserved — and we validate this hypothesis empirically in Phase 0 before building the full CEC pipeline.\\n\\n**Architectural solutions (pre-training).** Gated Attention (NeurIPS 2025 Best Paper, arXiv:2505.06708, OpenReview:1b7whO4SfY) implements query-conditional per-head sigmoid gating: Y' = Y ⊙ σ(X·W_θ) applied after SDPA output, where X is the pre-normalized hidden state. This is the closest mechanism to what CEC aims to achieve — dynamic per-head gating conditioned on input. However, Gated Attention: (a) requires pre-training from scratch (tested on 3.5T tokens, 15B MoE and 1.7B dense models); (b) learns general-purpose gating for all heads, not targeted at entrainment; (c) is deployed only in Qwen3-Next-80B-A3B and is not available as a fine-tuning method for existing models like Llama-3-8B or Qwen2.5-7B/14B. CEC is complementary: it provides the same functional benefit (query-conditional head gating) for existing models via targeted fine-tuning of entrainment head Q/K projections, using ~1000 training samples instead of trillions of tokens.\\n\\n**Contrastive training for attention distraction.** Focused Transformer (FoT, NeurIPS 2023, arXiv:2307.03170) is the first work to use contrastive training to reduce attention distraction. FoT structures the key-value space using crossbatch negatives from unrelated documents, fine-tuning OpenLLaMA 3B/7B to create LongLLaMA with 256K passkey retrieval. CEC differs from FoT in three ways: (a) CEC targets specific entrainment heads identified via mechanistic analysis rather than the general KV space; (b) CEC uses role-switching pairs (same passage, different queries) rather than crossbatch negatives (different passages); (c) CEC's training signal requires query-conditioning (the same tokens need opposite treatment depending on the query), while FoT's signal requires only key separability.\\n\\n**Head role analysis.** Causal Head Gating (CHG, NeurIPS 2025, arXiv:2505.13737) provides causal evidence that attention head roles (facilitating/interfering/irrelevant) vary by context and task, with low modularity across heads. CHG's contrastive variant isolates task-specific sub-circuits. This directly supports CEC's premise that entrainment heads can be made context-conditional. However, CHG is purely interpretive (1 learnable parameter per head, no weight modification) — it diagnoses head roles but does not modify them. CEC builds on CHG's causal taxonomy by actually training entrainment heads to switch between facilitating and interfering roles based on query-context alignment.\\n\\n**Behavioral fixes.** DPO with synthetic distractors (NeurIPS 2025, arXiv:2502.01609) achieves strong distraction robustness — Phi-3.5-mini with DPO surpasses GPT-4o on distracted inputs — but requires distractor-type exposure and does not modify the entrainment circuit. RARE (arXiv:2601.07226, Jan 2026) incentivizes identification of helpful information within noise via rationale-aware reward, revealing up to 80% performance drops on NoisyBench across 11 datasets; however, RARE's generalization to unseen noise types is not systematically validated. SFT fails for complex reasoning under distraction (EMNLP 2025 Oral, arXiv:2505.18761). EIT (arXiv:2602.01528, Feb 2026) uses RL to make cognitive bias cues non-predictive of reward on Qwen3-4B, achieving a +39.1pp robustness rate improvement (RRW from 40.6% to 79.7%) on MMLU-Pro when generalizing from bandwagon to distraction bias. While EIT demonstrates impressive cross-bias transfer, it addresses a related but distinct problem: prompt-level cognitive biases (bandwagon appeals, authority claims) in MCQ settings, not context-level entrainment from irrelevant passages. We include EIT for completeness but use DPO and RARE as the primary behavioral baselines for contextual distraction.\\n\\n**Circuit-level training methods.** ABFT (arXiv:2505.14233) demonstrated efficient attention-score fine-tuning of induction heads via W_Q/W_K training with 512 samples, but only for classification with finite label sets. MuDAF (arXiv:2502.13963) applies contrastive Q-K learning (InfoNCE on query-key similarity) to 8 retrieval heads on Llama-3.1-8B, achieving HotpotQA 69.6% and MuSiQue 48.2% — but training all heads causes instability and convergence collapse, ICL preservation is untested, and novel distractor generalization is unevaluated. RetMask (arXiv:2601.11020, Jan 2026) uses retrieval-head masking as a contrastive DPO signal for long-context improvement (+2.28 on HELMET at 128K). Head Pursuit (arXiv:2510.21518, Oct 2025) demonstrates that editing as few as 1% of heads via residual-stream rescaling can reliably suppress or enhance targeted concepts, validating the feasibility of sparse head-level intervention. 'In-Context Learning Without Copying' (arXiv:2511.05743) shows abstractive ICL is distributed across mechanisms (the Hapax finding), supporting the safety of head-level modification. Attention-head stability analysis (arXiv:2602.16740, Feb 2026) shows middle-layer heads are least stable across re-initializations.\\n\\nNo concurrent work combines: (a) circuit-level attention-score training on (b) entrainment heads with (c) role-switching contrastive design for (d) query-conditional suppression, (e) applied as fine-tuning to existing models, with (f) progressive head training to address scalability.\",\n  \"approach\": \"**Phase 0: Premise Validation — Ablation on Complex Benchmarks.** Before building CEC, we replicate the entrainment head ablation from 'Llama See, Llama Do' on Llama-3-8B and test its impact on a broader evaluation suite: (a) complex reasoning: BBH 5-shot, MMLU hard subsets (STEM, humanities); (b) multi-hop QA: HotpotQA, MuSiQue, 2WikiMQA; (c) context-dependent tasks: Natural Questions with gold passages (RAG-style), grounded QA with supporting documents. This experiment has two possible outcomes, both valuable: (i) If ablation causes >5% degradation on context-dependent tasks (vs. <3% on simple ICL), the CEC premise is validated — static ablation is too coarse, and query-conditional calibration is necessary. This becomes a strong motivating result. (ii) If ablation causes <3% degradation across all tasks, the contribution pivots: CEC's primary value becomes distraction-robustness generalization to unseen distractor types (where behavioral methods fail) rather than ICL/context preservation. Either outcome produces a publishable finding. Estimated cost: ~10h A100-80GB.\\n\\n**Phase 1: Entrainment Head Identification.** Replicate the differentiable Gumbel-sigmoid binary masking from 'Llama See, Llama Do' on Llama-3-8B (directly validated architecture) and Qwen2.5-7B (adaptation required). For Llama-3-8B, we expect results consistent with the original paper (~36–110 entrainment heads per relation, 3.5–10.7% of 1024 total heads). For Qwen2.5-7B, we treat successful identification as an empirical contribution validating cross-architecture transfer. We rank identified heads by entrainment strength (attention score contribution to context-seen tokens).\\n\\n**Phase 2: Role-Switching Dataset Construction.** From multi-document QA datasets (HotpotQA, MuSiQue, 2WikiMQA), construct role-switching contrastive pairs where the same passage P serves as gold context for query Q_A and as an irrelevant distractor for query Q_B. This is achieved by selecting passages that answer one question but not another within the same document set. Each training instance is a tuple (Q_A, Q_B, P, label) where label indicates P's relevance. Target: ~1000 high-quality role-switching pairs.\\n\\n**Phase 3: Progressive Contrastive Training.** To address MuDAF's scalability bottleneck (instability and convergence collapse when training all heads simultaneously), we introduce progressive head training with the following justification:\\n\\n*Theoretical basis:* The instability arises because simultaneously perturbing many heads creates high-variance gradients in a coupled system (CHG shows heads have low modularity — they interact). Progressive expansion reduces the effective dimensionality of the optimization at each stage. This is analogous to coordinate descent: optimizing a subset of variables while holding others fixed reduces the condition number of the local Hessian. Formally, if L(θ_1, ..., θ_H) is the loss over H heads, training heads 1..k while fixing k+1..H produces ∇_{1..k}L with variance proportional to k rather than H, improving convergence of each substep.\\n\\n*Empirical basis:* Training high-entrainment-strength heads first means subsequent lower-strength heads operate in a landscape where the dominant entrainment effects are already calibrated. Since high-strength heads account for the majority of the entrainment signal, their calibration creates a more stable loss surface for remaining heads — analogous to how PCA orders components by explained variance.\\n\\n*Explicit fallback:* If instability persists at N heads despite progressive expansion, we report results for the maximal stable subset rather than claiming universal scalability. MuDAF's stable regime of 8 heads already covers the highest-entrainment-strength heads, which may suffice for practical distraction robustness.\\n\\nThe progressive schedule:\\n  (a) Sort entrainment heads by entrainment strength score.\\n  (b) Train contrastive loss on top-8 heads (within MuDAF's demonstrated stable regime).\\n  (c) Progressively expand to the next 8 heads every N steps, with per-head loss weights proportional to entrainment strength.\\n  (d) Use gradient clipping (max norm 1.0) and learning rate warmup (linear, 100 steps) at each expansion step.\\n  (e) Stability monitoring: if validation loss increases >10% after an expansion step, halt expansion and report results for the current stable subset.\\n\\nThe contrastive loss adapts MuDAF's InfoNCE-style Q-K similarity objective from retrieval heads to entrainment heads, with role-switching pairs replacing fixed relevant/irrelevant assignments: L_CEC = -Σ_h [λ_h · log(e^(sim(Q_h, K_h^{P_rel})/τ) / Σ_{P_j} e^(sim(Q_h, K_h^{P_j})/τ))], where Q_h are query representations at entrainment head h, K_h^{P_j} are key representations of passage P_j, P_rel is the relevant passage determined by the role-switching pair, τ is temperature, and λ_h is the per-head weight proportional to entrainment strength. This loss maximizes Q-K alignment for relevant passages while suppressing alignment for irrelevant passages, applied only to identified entrainment heads' Q/K projections.\\n\\n**Phase 4: ICL Safety Monitoring.** Rather than an explicit ICL-preservation regularizer (which the Hapax finding suggests may be unnecessary given ICL's distributed nature), we continuously monitor ICL accuracy on: spelling/translation/arithmetic (original 3 tasks from 'Llama See, Llama Do') PLUS MMLU, BBH 5-shot, and few-shot classification tasks. If degradation exceeds a threshold (>2% on any benchmark relative to the Phase 0 baseline), we add a lightweight KL-divergence regularizer on non-entrainment-head attention patterns.\\n\\n**Phase 5: Evaluation.** Primary metrics: (a) Distraction robustness generalization to unseen distractor types — evaluated on held-out distractor types from NoisyBench (RARE's benchmark) and GSM-DC, plus the Adaptive Distraction tree-search framework (NeurIPS 2025) for adversarial distraction. Direct comparison with DPO (the strongest behavioral baseline per Adaptive Distraction, where DPO-tuned Phi-3.5-mini surpasses GPT-4o on distracted inputs) and RARE. (b) Open-ended QA under distraction, where MCQ-specific methods cannot operate. (c) Context-dependent task performance (grounded QA, RAG settings) to demonstrate that beneficial entrainment is preserved — a critical test that ablation-based methods cannot pass (validated via Phase 0 findings). (d) ICL preservation on the broader suite from Phase 4. (e) Comparison with static ablation on the full benchmark suite to quantify CEC's advantage in the query-conditional regime.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~140h A100-80GB (≈70–90h H100 equivalent)\",\n      \"gpu_utilization\": \"Low (~20–30%) — GPU idles during coding, debugging, analysis\",\n      \"timeline\": \"3–4 months\",\n      \"team\": \"1–2 researchers with mechanistic interpretability and fine-tuning experience\",\n      \"estimated_gpu_cost\": \"$210–350 (at ~$1.50/hr A100 spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~100h A100-80GB (≈50–65h H100 equivalent)\",\n      \"gpu_utilization\": \"Moderate (~50–60%) — agent handles coding and experiment execution, human approves designs and interprets results\",\n      \"timeline\": \"2–4 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing agent proposals\",\n      \"claude_api_cost\": \"$25–60 (250–600 turns at ~$0.10/turn)\",\n      \"estimated_gpu_cost\": \"$150–250\",\n      \"risk_note\": \"Entrainment head identification on Qwen2.5-7B may require methodology adaptation; if differentiable masking doesn't transfer cleanly, add 1 week for method debugging. Phase 0 premise validation (ablation on complex benchmarks) is low-risk and provides early go/no-go signal within 2 days.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~300h A100-80GB (≈150–195h H100 equivalent, within ≤200 H100-hour budget)\",\n      \"gpu_utilization\": \"High (~90–95%) — continuous experiment pipeline\",\n      \"timeline\": \"8–14 days with 4× A100-80GB\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$200–400 (2000–4000 turns for full experiment loop)\",\n      \"estimated_gpu_cost\": \"$450–750\",\n      \"speed_bottleneck\": \"GPU count — head identification requires full forward passes; each contrastive training run needs 1× A100-80GB for ~3h (8B model); 4 GPUs enable parallel ablations across models\",\n      \"budget_management\": \"If approaching 200 H100-hour limit: (1) drop Qwen2.5-7B experiments (saves ~50h A100), (2) reduce progressive-expansion stages to top-8 only (saves ~30h A100), (3) reduce NoisyBench evaluation to 6 of 11 datasets (saves ~15h A100). Phase 0 premise validation takes ~10h A100 and is the first experiment; if ablation shows <3% degradation on complex tasks, pivot framing to distraction-robustness generalization before investing in later phases.\",\n      \"risk_note\": \"Progressive head expansion may require hyperparameter tuning across the 8→16→all-heads curriculum; stability monitoring (Phase 3e) provides automatic early stopping if instability appears\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstracts due July 21, 2026; full papers due July 28, 2026)\",\n    \"ARR August 3, 2026 cycle → EACL 2027 (commitment deadline: October 11, 2026)\"\n  ],\n  \"venue_note\": \"The user's original target of EMNLP 2026 via ARR is infeasible — the ARR May 2026 deadline is May 25 (8 days from today, May 17), insufficient for completing even Phase 0. AAAI 2027 (papers due July 28) provides ~10 weeks and is the primary target. EACL 2027 (ARR August 3) provides ~11 weeks as a backup. Both venues are appropriate for this work's combination of mechanistic interpretability and fine-tuning methodology.\",\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, aclanthology.org/2025.acl-long.791)\",\n    \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025 Best Paper, arXiv:2505.06708, OpenReview:1b7whO4SfY)\",\n    \"Focused Transformer: Contrastive Training for Context Scaling [FoT] (NeurIPS 2023, arXiv:2307.03170)\",\n    \"Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers [CHG] (NeurIPS 2025, arXiv:2505.13737)\",\n    \"Mechanistic Fine-tuning for In-context Learning [ABFT] (arXiv 2025, 2505.14233)\",\n    \"MuDAF: Long-Context Multi-Document Attention Focusing through Contrastive Learning on Attention Heads (arXiv 2025, 2502.13963)\",\n    \"Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search (NeurIPS 2025, arXiv:2502.01609)\",\n    \"Lost in the Noise: How Reasoning Models Fail with Contextual Distractors [RARE] (arXiv 2026, 2601.07226)\",\n    \"How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark (EMNLP 2025 Oral, arXiv:2505.18761)\",\n    \"Making Bias Non-Predictive: Training Robust LLM Judges via Reinforcement Learning [EIT] (arXiv 2026, 2602.01528)\",\n    \"From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models [RetMask] (arXiv 2026, 2601.11020)\",\n    \"In-Context Learning Without Copying [Hapax] (arXiv 2025, 2511.05743)\",\n    \"Head Pursuit: Probing Attention Specialization in Multimodal Transformers (arXiv 2025, 2510.21518)\",\n    \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality (arXiv 2026, 2602.16740)\"\n  ],\n  \"description\": \"We propose Contrastive Entrainment Calibration (CEC), the first method to make entrainment heads query-conditional in existing models via circuit-level contrastive fine-tuning. CEC addresses a three-sided gap in the current landscape: (1) Gated Attention (NeurIPS 2025 Best Paper) achieves query-conditional per-head gating but requires pre-training from scratch — inapplicable to existing deployed models; (2) ablation (ACL 2025) is circuit-level but query-agnostic — it removes all entrainment regardless of context relevance; (3) behavioral training (DPO/RARE) is query-aware but mechanism-agnostic — it never modifies the entrainment circuit. CEC bridges this gap by providing query-conditional circuit-level control as a lightweight fine-tuning method.\\n\\nWe begin with a premise-validation experiment (Phase 0): testing ablation on complex benchmarks (BBH, multi-hop QA, RAG/grounded QA) to empirically establish whether static ablation degrades context-dependent tasks — if so, this motivates the need for query-conditional calibration; if not, CEC's value shifts to distraction-robustness generalization.\\n\\nUsing role-switching contrastive pairs — where the SAME passage is relevant context for one query but an irrelevant distractor for another — we train entrainment heads' Q/K projections to gate on query-context alignment rather than unconditionally boosting all context-seen tokens. This extends the contrastive-training-for-distraction paradigm introduced by Focused Transformer (NeurIPS 2023) from the general key-value space to specific mechanistically-identified entrainment heads, and from crossbatch negatives to role-switching pairs that structurally require query-conditioning. CHG (NeurIPS 2025) provides causal evidence that head roles are context-dependent (facilitating/interfering/irrelevant vary by task), directly supporting the feasibility of making entrainment heads query-conditional.\\n\\nTo address MuDAF's scalability bottleneck (convergence collapse beyond 8 heads), we introduce progressive head training with formal justification: sequential expansion reduces gradient variance from H-head simultaneous perturbation to k-head substeps, analogous to coordinate descent. We provide an explicit stability-monitoring protocol and fallback to the maximal stable subset.\\n\\nWe evaluate on: (1) generalization to unseen distractor types (NoisyBench, Adaptive Distraction tree-search) as the primary metric, with DPO and RARE as behavioral baselines; (2) open-ended QA under distraction; (3) context-dependent task performance (RAG, grounded QA) to demonstrate beneficial entrainment is preserved; (4) ICL preservation on MMLU, BBH, and the original 3 tasks; (5) comparison with static ablation to quantify CEC's query-conditional advantage.\",\n  \"project_name\": \"contrastive_entrain_calib\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Overstated core premise: 'Llama See, Llama Do' (ACL 2025) shows ablating entrainment heads causes only 0.2-3% ICL degradation (73.6→72.0% spelling, 74.4→73.0% translation, 100→100% arithmetic). The paper explicitly states 'removing the entrainment heads has only a negligible to small effect' on other capabilities and does NOT claim these heads enable ICL or discuss a 'dual-use' problem. The 'fundamental double-bind' framing — that suppressing entrainment destroys ICL — is not supported by the mechanistic evidence.\", \"CRITICAL — Model choice violates user constraints: User explicitly specifies 'Fine-tune from existing checkpoints (Llama-3-8B, Qwen2.5-7B/14B)' and '≤200 H100-hours.' The proposal uses Qwen3.6-27B (released April 2026, 27B dense), which is neither in the specified model list nor within the same compute class. Must use the user-specified models.\", \"CRITICAL — ARR deadline infeasibility: The EMNLP 2026 ARR submission deadline is May 25, 2026 — only 8 days from today (May 17). Even the auto-research timeline (10-18 days) cannot meet this. The May 25 target should be removed or replaced with the October 2026 ARR cycle.\", \"MAJOR — MuDAF scalability bottleneck: MuDAF found that contrastive Q-K learning becomes unstable beyond ~8 heads and 'training will become unstable and struggle to converge' when engaging more. Entrainment heads are 3.2-10.7% of all heads (e.g., 36 of 1024 for one relation in Llama-3.1-8B). Training all entrainment heads simultaneously with contrastive Q-K loss may face the same instability, requiring a head-selection or progressive training strategy not currently addressed.\", \"MAJOR — Competing baseline understated: EIT (arXiv:2602.01528) achieves 39.1% generalization to unseen distraction types via purely behavioral RL on Qwen3-4B. This is a strong baseline that the proposal needs to convincingly surpass. The proposal claims 'behavioral fixes cannot generalize to novel distractor types' but EIT demonstrates substantial generalization already.\", \"MODERATE — ABFT applicability gap: ABFT was demonstrated only for classification tasks with finite label sets (0.01% data cost claim). The proposal extends this to open-ended reasoning/QA settings where there are no discrete 'correct label tokens' to attend to. The loss function must be re-derived for non-classification tasks, which is non-trivial and unaddressed.\", \"MODERATE — Entrainment head identification transferability: The differentiable masking method from 'Llama See, Llama Do' was validated only on Llama-2-7B/13B, Llama-3.1-8B, and GPT-2 XL. Transfer to Qwen-family architectures is unvalidated, and the proposal acknowledges this risk but underestimates the effort needed.\", \"MINOR — Hapax finding undermines the induction-ICL coupling assumption: 'In-Context Learning Without Copying' (arXiv:2511.05743) shows that training without induction-head gradients preserves abstractive ICL, suggesting ICL mechanisms are more distributed than the proposal assumes. This weakens the theoretical argument that circuit-level intervention on specific heads is necessary.\"]\nFeedback: The proposal has a well-designed technical approach but rests on a critically overstated theoretical premise. Here is specific guidance for revision:\n\n1. **Fix the core premise**: Re-read 'Llama See, Llama Do' carefully. The paper shows entrainment head ablation barely affects ICL (0.2-3% drop). Reframe: instead of claiming a 'fundamental double-bind,' argue that (a) simple ablation is too coarse-grained (zeroing out heads entirely), (b) ablation was tested only on 3 simple ICL tasks — more complex few-shot reasoning (MMLU, BBH) may show larger degradation, and (c) your method aims for SELECTIVE suppression that preserves full head functionality, which ablation cannot provide. This is a more defensible and still interesting contribution.\n\n2. **Use user-specified models**: Switch to Llama-3-8B and Qwen2.5-7B/14B as the user requires. This actually simplifies the head identification step since 'Llama See, Llama Do' already validated on Llama models.\n\n3. **Fix the timeline**: Remove the May 25 ARR deadline. Target the October 2026 ARR cycle for EMNLP 2026 commitment, or target ACL 2026 (if deadlines align). Alternatively, target AAAI 2027.\n\n4. **Address MuDAF's scalability finding**: Propose a head-grouping or progressive training strategy. For example, train contrastive loss on top-k most active entrainment heads first, then expand. Or use a per-head loss weight based on entrainment strength.\n\n5. **Properly benchmark against EIT**: EIT's 39.1% generalization is your strongest behavioral baseline. Explain specifically why circuit-level intervention should beat behavioral RL — e.g., EIT requires bias-type-balanced training data construction, while your method's role-switching naturally provides relevance signals without bias engineering.\n\n6. **Adapt ABFT loss for non-classification tasks**: The attention-score objective in ABFT targets label tokens. For QA/reasoning, define the objective in terms of attention to gold-passage tokens vs. distractor tokens (similar to MuDAF's formulation but applied to entrainment heads).\n\n7. **Strengthen the MuDAF differentiation**: Currently the main difference is 'entrainment heads instead of retrieval heads.' Add: (a) role-switching contrastive pairs (MuDAF uses fixed relevant/irrelevant assignments), (b) ICL-preservation regularizer (MuDAF doesn't test ICL), (c) novel distractor generalization testing (MuDAF doesn't test this).\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MAJOR — Missing critical related work: (1) Gated Attention / Qwen3-Next (NeurIPS 2025 Best Paper, OpenReview:1b7whO4SfY) implements exactly query-conditional per-head sigmoid gating (gate = sigmoid(linear(query)) * attn_output), learned end-to-end during pre-training, already deployed in Qwen3-Next-80B. This is the EXACT mechanism CEC proposes (query-conditional per-head gating on attention) and won Best Paper — CEC must cite it and clearly differentiate. (2) Focused Transformer / FoT (NeurIPS 2023, arXiv:2307.03170) uses contrastive training (crossbatch negatives) to restructure the key-value space and reduce attention distraction in long contexts — the closest prior art for contrastive-training-for-distraction. (3) Causal Head Gating / CHG (NeurIPS 2025, arXiv:2505.13737) demonstrates contrastive head gating with role taxonomy (facilitating/interfering/irrelevant), showing head roles vary by context — directly supports but also partially anticipates CEC's role-switching concept.\", \"MAJOR — EIT mischaracterization: The proposal claims EIT 'achieves 39.1% generalization from bandwagon→distraction bias' and treats it as 'the strongest behavioral baseline' and the 'behavioral ceiling to beat.' Verification reveals: (a) the 39.1% is a robustness-rate improvement (+39.1pp on MMLU-Pro, from 40.6% to 79.7%), not a generalization percentage; (b) EIT targets cognitive biases in LLM-as-judge settings (bandwagon appeals, authority claims), NOT contextual entrainment/distraction (irrelevant passages in context); (c) EIT operates on Qwen3-4B with MCQ-only evaluation. Using a judge-debiasing paper as the primary distraction-robustness baseline is a category mismatch that undermines the evaluation plan.\", \"MODERATE — Unvalidated core premise: The proposal argues that ablation is too coarse-grained because it was 'tested only on three simple ICL tasks' and hypothesizes complex reasoning will degrade more. This is a fair hypothesis but is unvalidated speculation that the entire CEC contribution rests on. If ablation causes <3% degradation on MMLU, BBH, and multi-hop QA too, CEC's practical advantage over simple ablation is marginal. The proposal should include validating this premise (testing ablation on complex benchmarks) as a preliminary experiment BEFORE building the full CEC pipeline.\", \"MODERATE — Progressive head training lacks justification: MuDAF found contrastive Q/K training 'becomes unstable and struggles to converge' beyond 8 heads. The proposal's solution (progressive expansion 8→16→all with warmup) is intuitive but entirely unvalidated. The instability may be inherent to the contrastive attention-score loss landscape when many heads are simultaneously perturbed, not merely a curriculum issue. No theoretical or empirical argument is provided for why progressive expansion avoids the convergence failure.\", \"MODERATE — AAAI 2027 deadline is July 28, not 'August 2026': Verified via AAAI-27 CFP — abstracts due July 21, 2026; full papers due July 28, 2026. The proposal states '~August 2026' which is inaccurate. Combined with the auto-research timeline of 8–14 days, starting from today (May 17) this is feasible but tight. The ARR August 2026 deadline for EACL 2027 is August 3, 2026 (confirmed via EACL announcement), not a generic 'August cycle.'\", \"MINOR — Auto-research H100 estimate exceeds budget at high end: 175–230h H100 equivalent, but user constraint is ≤200 H100-hours. The 230h high-end exceeds the budget by 15%. Tighten the estimate or add explicit scoping guidance for what to cut if approaching the limit.\", \"MINOR — Venue mismatch with user request: User explicitly asked for 'Target: EMNLP 2026, ARR submission.' The May 25, 2026 ARR deadline makes this infeasible (confirmed — 8 days away). The proposal targets AAAI 2027 and EACL 2027 instead, which are reasonable alternatives, but should explicitly acknowledge the EMNLP 2026 infeasibility and propose the path forward.\"]\nFeedback: The revision substantially improved the core premise and model choices from Round 1. The remaining issues are addressable:\n\n1. **Cite and differentiate from Gated Attention (NeurIPS 2025 Best Paper)**: This paper implements query-conditional per-head gating (sigmoid(linear(query)) * attn_output) at scale during pre-training. CEC's differentiation: (a) CEC is a fine-tuning method, not an architectural change requiring pre-training from scratch; (b) CEC specifically targets entrainment heads identified via mechanistic analysis, while Gated Attention learns gates for all heads generally; (c) CEC uses contrastive role-switching training signal, not standard LM objective. Also cite Focused Transformer (NeurIPS 2023) as the first contrastive-training-for-attention-distraction work, and CHG (NeurIPS 2025) for causal evidence that head roles are context-dependent.\n\n2. **Replace EIT as the primary behavioral baseline**: EIT targets judge-debiasing, not contextual distraction. Instead, use DPO with synthetic distractors (NeurIPS 2025 'Adaptive Distraction') and RARE (arXiv:2601.07226) as the direct behavioral baselines. If citing EIT at all, note it addresses a related but distinct problem (prompt-level cognitive bias vs. context-level entrainment).\n\n3. **Add a premise-validation experiment as Phase 0**: Before building CEC, test ablation (from 'Llama See, Llama Do') on complex benchmarks — BBH, MMLU hard subsets, multi-hop QA (HotpotQA/MuSiQue), and RAG/grounded QA. If ablation causes >5% degradation on these tasks (vs. <3% on simple tasks), the CEC premise is validated and you have a strong motivating result. If not, the contribution pivots to distraction-robustness generalization rather than ICL preservation.\n\n4. **Provide a theoretical argument for progressive training**: The claim that progressive expansion solves MuDAF's convergence failure needs more than intuition. Consider: (a) formal analogy to curriculum learning theory; (b) the observation that entrainment heads likely have different functional overlap — training high-entrainment-strength heads first means lower-strength heads can adjust to a more stable landscape; (c) explicit fallback: if instability persists at N heads, report results for the stable subset rather than claiming universal scalability.\n\n5. **Tighten compute estimates**: Cap auto-research at 200h H100 equivalent. Specify what gets cut if approaching the limit (e.g., drop Qwen2.5-14B experiments, reduce progressive-expansion stages).\n\n6. **Fix venue deadlines**: AAAI 2027 abstracts are due July 21 (not 'August'). ARR for EACL 2027 is August 3. Add a sentence acknowledging EMNLP 2026 is infeasible given the May 25 ARR deadline.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-17T08:58:39.219Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T08:58:39.219Z",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-17T08:58:39.290Z_

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

## Idea under review (round 3/10)
{
  "title": "Contrastive Entrainment Calibration: Query-Conditional Attention Training via Role-Switching Pairs",
  "core_problem": "Entrainment heads unconditionally boost all context-seen tokens regardless of task relevance (ACL 2025). The only known circuit-level intervention — ablating these heads — is a static, query-agnostic operation: it removes all entrainment regardless of whether the context is relevant or irrelevant to the current query. While ablation attenuates distraction, it was validated only on three simple ICL tasks (spelling, translation, arithmetic) and overall MMLU (56.3→55.5%); its effects on complex reasoning (BBH, multi-hop QA) and beneficial context use (RAG, grounded QA) remain untested. Meanwhile, behavioral fixes (DPO, RARE) do not modify the entrainment circuit and show limited generalization to novel distractor types. Gated Attention (NeurIPS 2025 Best Paper) introduces query-conditional per-head sigmoid gating that can modulate attention heads dynamically — but this is an architectural change requiring pre-training from scratch (tested at 3.5T tokens on 15B MoE models), making it inapplicable to the billions of existing deployed models. How can we make entrainment heads in EXISTING models query-conditional — boosting context tokens when relevant while suppressing them when irrelevant — via lightweight fine-tuning rather than architectural redesign?",
  "opportunity": "The gap is now three-sided: (1) pre-training architectural solutions (Gated Attention) achieve query-conditional gating but require training from scratch and do not target entrainment specifically; (2) static circuit intervention (ablation) is query-agnostic — it removes all entrainment regardless of context relevance; (3) behavioral training (DPO/RARE) is query-aware but mechanism-agnostic — it never modifies the entrainment circuit and shows limited generalization. No work provides query-conditional circuit-level control of entrainment heads in existing models via fine-tuning.\n\nFour convergent advances make this feasible: (1) ABFT (arXiv:2505.14233) proved that attention-score training objectives can efficiently modify specific head behavior by fine-tuning Q/K projections with ~512 samples; (2) MuDAF (arXiv:2502.13963) showed contrastive Q-K learning on retrieval heads improves multi-document QA on Llama-3.1-8B (HotpotQA 69.6%, MuSiQue 48.2%), but targets retrieval heads (not entrainment heads), does not test ICL preservation, does not test novel distractor generalization, and becomes unstable when training all heads (only 8 heads stable); (3) CHG (NeurIPS 2025, arXiv:2505.13737) demonstrates via causal analysis that attention head roles are context-dependent — the same head can be facilitating, interfering, or irrelevant depending on the task — directly supporting the premise that entrainment heads CAN be made query-conditional rather than being inherently unconditional; (4) the Hapax finding (arXiv:2511.05743) that abstractive ICL is preserved even when induction-head gradients are removed suggests ICL is distributed and robust to head-level modification.\n\nThe key structural insight is that role-switching contrastive pairs — where the SAME passage serves as relevant context for one query but irrelevant distractor for another — provide a natural training signal for query-conditioning. This extends the Focused Transformer (NeurIPS 2023, arXiv:2307.03170) paradigm of contrastive training for attention distraction reduction, but differs fundamentally: FoT applies contrastive learning to the general key-value space with crossbatch negatives to improve key separability; CEC applies contrastive learning specifically to entrainment head Q/K projections with role-switching pairs that force query-conditional behavior.",
  "landscape": "**Circuit-level understanding of entrainment.** The entrainment mechanism is established by 'Llama See, Llama Do' (ACL 2025, aclanthology.org/2025.acl-long.791): 3.2–10.7% of attention heads (e.g., 36 of 1024 in Llama-3.1-8B for country–capital) cause unconditional context token boosting, identified via differentiable Gumbel-sigmoid binary masking. Ablating these heads has 'negligible to small effect' on ICL: arithmetic 100→100%, spelling 1-shot 73.6→72.0% (−1.6%), translation 1-shot 74.4→73.0% (−1.4%), overall MMLU 56.3→55.5% (−0.8%). However, ablation was tested only on these simple tasks; its impact on complex reasoning (BBH, multi-hop QA) and context-dependent tasks (RAG, grounded QA) remains untested. We hypothesize that ablation's indiscriminate removal of context influence will degrade performance on context-dependent tasks even if simple ICL is preserved — and we validate this hypothesis empirically in Phase 0 before building the full CEC pipeline.\n\n**Architectural solutions (pre-training).** Gated Attention (NeurIPS 2025 Best Paper, arXiv:2505.06708, OpenReview:1b7whO4SfY) implements query-conditional per-head sigmoid gating: Y' = Y ⊙ σ(X·W_θ) applied after SDPA output, where X is the pre-normalized hidden state. This is the closest mechanism to what CEC aims to achieve — dynamic per-head gating conditioned on input. However, Gated Attention: (a) requires pre-training from scratch (tested on 3.5T tokens, 15B MoE and 1.7B dense models); (b) learns general-purpose gating for all heads, not targeted at entrainment; (c) is deployed only in Qwen3-Next-80B-A3B and is not available as a fine-tuning method for existing models like Llama-3-8B or Qwen2.5-7B/14B. CEC is complementary: it provides the same functional benefit (query-conditional head gating) for existing models via targeted fine-tuning of entrainment head Q/K projections, using ~1000 training samples instead of trillions of tokens.\n\n**Contrastive training for attention distraction.** Focused Transformer (FoT, NeurIPS 2023, arXiv:2307.03170) is the first work to use contrastive training to reduce attention distraction. FoT structures the key-value space using crossbatch negatives from unrelated documents, fine-tuning OpenLLaMA 3B/7B to create LongLLaMA with 256K passkey retrieval. CEC differs from FoT in three ways: (a) CEC targets specific entrainment heads identified via mechanistic analysis rather than the general KV space; (b) CEC uses role-switching pairs (same passage, different queries) rather than crossbatch negatives (different passages); (c) CEC's training signal requires query-conditioning (the same tokens need opposite treatment depending on the query), while FoT's signal requires only key separability.\n\n**Head role analysis.** Causal Head Gating (CHG, NeurIPS 2025, arXiv:2505.13737) provides causal evidence that attention head roles (facilitating/interfering/irrelevant) vary by context and task, with low modularity across heads. CHG's contrastive variant isolates task-specific sub-circuits. This directly supports CEC's premise that entrainment heads can be made context-conditional. However, CHG is purely interpretive (1 learnable parameter per head, no weight modification) — it diagnoses head roles but does not modify them. CEC builds on CHG's causal taxonomy by actually training entrainment heads to switch between facilitating and interfering roles based on query-context alignment.\n\n**Behavioral fixes.** DPO with synthetic distractors (NeurIPS 2025, arXiv:2502.01609) achieves strong distraction robustness — Phi-3.5-mini with DPO surpasses GPT-4o on distracted inputs — but requires distractor-type exposure and does not modify the entrainment circuit. RARE (arXiv:2601.07226, Jan 2026) incentivizes identification of helpful information within noise via rationale-aware reward, revealing up to 80% performance drops on NoisyBench across 11 datasets; however, RARE's generalization to unseen noise types is not systematically validated. SFT fails for complex reasoning under distraction (EMNLP 2025 Oral, arXiv:2505.18761). EIT (arXiv:2602.01528, Feb 2026) uses RL to make cognitive bias cues non-predictive of reward on Qwen3-4B, achieving a +39.1pp robustness rate improvement (RRW from 40.6% to 79.7%) on MMLU-Pro when generalizing from bandwagon to distraction bias. While EIT demonstrates impressive cross-bias transfer, it addresses a related but distinct problem: prompt-level cognitive biases (bandwagon appeals, authority claims) in MCQ settings, not context-level entrainment from irrelevant passages. We include EIT for completeness but use DPO and RARE as the primary behavioral baselines for contextual distraction.\n\n**Circuit-level training methods.** ABFT (arXiv:2505.14233) demonstrated efficient attention-score fine-tuning of induction heads via W_Q/W_K training with 512 samples, but only for classification with finite label sets. MuDAF (arXiv:2502.13963) applies contrastive Q-K learning (InfoNCE on query-key similarity) to 8 retrieval heads on Llama-3.1-8B, achieving HotpotQA 69.6% and MuSiQue 48.2% — but training all heads causes instability and convergence collapse, ICL preservation is untested, and novel distractor generalization is unevaluated. RetMask (arXiv:2601.11020, Jan 2026) uses retrieval-head masking as a contrastive DPO signal for long-context improvement (+2.28 on HELMET at 128K). Head Pursuit (arXiv:2510.21518, Oct 2025) demonstrates that editing as few as 1% of heads via residual-stream rescaling can reliably suppress or enhance targeted concepts, validating the feasibility of sparse head-level intervention. 'In-Context Learning Without Copying' (arXiv:2511.05743) shows abstractive ICL is distributed across mechanisms (the Hapax finding), supporting the safety of head-level modification. Attention-head stability analysis (arXiv:2602.16740, Feb 2026) shows middle-layer heads are least stable across re-initializations.\n\nNo concurrent work combines: (a) circuit-level attention-score training on (b) entrainment heads with (c) role-switching contrastive design for (d) query-conditional suppression, (e) applied as fine-tuning to existing models, with (f) progressive head training to address scalability.",
  "approach": "**Phase 0: Premise Validation — Ablation on Complex Benchmarks.** Before building CEC, we replicate the entrainment head ablation from 'Llama See, Llama Do' on Llama-3-8B and test its impact on a broader evaluation suite: (a) complex reasoning: BBH 5-shot, MMLU hard subsets (STEM, humanities); (b) multi-hop QA: HotpotQA, MuSiQue, 2WikiMQA; (c) context-dependent tasks: Natural Questions with gold passages (RAG-style), grounded QA with supporting documents. This experiment has two possible outcomes, both valuable: (i) If ablation causes >5% degradation on context-dependent tasks (vs. <3% on simple ICL), the CEC premise is validated — static ablation is too coarse, and query-conditional calibration is necessary. This becomes a strong motivating result. (ii) If ablation causes <3% degradation across all tasks, the contribution pivots: CEC's primary value becomes distraction-robustness generalization to unseen distractor types (where behavioral methods fail) rather than ICL/context preservation. Either outcome produces a publishable finding. Estimated cost: ~10h A100-80GB.\n\n**Phase 1: Entrainment Head Identification.** Replicate the differentiable Gumbel-sigmoid binary masking from 'Llama See, Llama Do' on Llama-3-8B (directly validated architecture) and Qwen2.5-7B (adaptation required). For Llama-3-8B, we expect results consistent with the original paper (~36–110 entrainment heads per relation, 3.5–10.7% of 1024 total heads). For Qwen2.5-7B, we treat successful identification as an empirical contribution validating cross-architecture transfer. We rank identified heads by entrainment strength (attention score contribution to context-seen tokens).\n\n**Phase 2: Role-Switching Dataset Construction.** From multi-document QA datasets (HotpotQA, MuSiQue, 2WikiMQA), construct role-switching contrastive pairs where the same passage P serves as gold context for query Q_A and as an irrelevant distractor for query Q_B. This is achieved by selecting passages that answer one question but not another within the same document set. Each training instance is a tuple (Q_A, Q_B, P, label) where label indicates P's relevance. Target: ~1000 high-quality role-switching pairs.\n\n**Phase 3: Progressive Contrastive Training.** To address MuDAF's scalability bottleneck (instability and convergence collapse when training all heads simultaneously), we introduce progressive head training with the following justification:\n\n*Theoretical basis:* The instability arises because simultaneously perturbing many heads creates high-variance gradients in a coupled system (CHG shows heads have low modularity — they interact). Progressive expansion reduces the effective dimensionality of the optimization at each stage. This is analogous to coordinate descent: optimizing a subset of variables while holding others fixed reduces the condition number of the local Hessian. Formally, if L(θ_1, ..., θ_H) is the loss over H heads, training heads 1..k while fixing k+1..H produces ∇_{1..k}L with variance proportional to k rather than H, improving convergence of each substep.\n\n*Empirical basis:* Training high-entrainment-strength heads first means subsequent lower-strength heads operate in a landscape where the dominant entrainment effects are already calibrated. Since high-strength heads account for the majority of the entrainment signal, their calibration creates a more stable loss surface for remaining heads — analogous to how PCA orders components by explained variance.\n\n*Explicit fallback:* If instability persists at N heads despite progressive expansion, we report results for the maximal stable subset rather than claiming universal scalability. MuDAF's stable regime of 8 heads already covers the highest-entrainment-strength heads, which may suffice for practical distraction robustness.\n\nThe progressive schedule:\n  (a) Sort entrainment heads by entrainment strength score.\n  (b) Train contrastive loss on top-8 heads (within MuDAF's demonstrated stable regime).\n  (c) Progressively expand to the next 8 heads every N steps, with per-head loss weights proportional to entrainment strength.\n  (d) Use gradient clipping (max norm 1.0) and learning rate warmup (linear, 100 steps) at each expansion step.\n  (e) Stability monitoring: if validation loss increases >10% after an expansion step, halt expansion and report results for the current stable subset.\n\nThe contrastive loss adapts MuDAF's InfoNCE-style Q-K similarity objective from retrieval heads to entrainment heads, with role-switching pairs replacing fixed relevant/irrelevant assignments: L_CEC = -Σ_h [λ_h · log(e^(sim(Q_h, K_h^{P_rel})/τ) / Σ_{P_j} e^(sim(Q_h, K_h^{P_j})/τ))], where Q_h are query representations at entrainment head h, K_h^{P_j} are key representations of passage P_j, P_rel is the relevant passage determined by the role-switching pair, τ is temperature, and λ_h is the per-head weight proportional to entrainment strength. This loss maximizes Q-K alignment for relevant passages while suppressing alignment for irrelevant passages, applied only to identified entrainment heads' Q/K projections.\n\n**Phase 4: ICL Safety Monitoring.** Rather than an explicit ICL-preservation regularizer (which the Hapax finding suggests may be unnecessary given ICL's distributed nature), we continuously monitor ICL accuracy on: spelling/translation/arithmetic (original 3 tasks from 'Llama See, Llama Do') PLUS MMLU, BBH 5-shot, and few-shot classification tasks. If degradation exceeds a threshold (>2% on any benchmark relative to the Phase 0 baseline), we add a lightweight KL-divergence regularizer on non-entrainment-head attention patterns.\n\n**Phase 5: Evaluation.** Primary metrics: (a) Distraction robustness generalization to unseen distractor types — evaluated on held-out distractor types from NoisyBench (RARE's benchmark) and GSM-DC, plus the Adaptive Distraction tree-search framework (NeurIPS 2025) for adversarial distraction. Direct comparison with DPO (the strongest behavioral baseline per Adaptive Distraction, where DPO-tuned Phi-3.5-mini surpasses GPT-4o on distracted inputs) and RARE. (b) Open-ended QA under distraction, where MCQ-specific methods cannot operate. (c) Context-dependent task performance (grounded QA, RAG settings) to demonstrate that beneficial entrainment is preserved — a critical test that ablation-based methods cannot pass (validated via Phase 0 findings). (d) ICL preservation on the broader suite from Phase 4. (e) Comparison with static ablation on the full benchmark suite to quantify CEC's advantage in the query-conditional regime.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~140h A100-80GB (≈70–90h H100 equivalent)",
      "gpu_utilization": "Low (~20–30%) — GPU idles during coding, debugging, analysis",
      "timeline": "3–4 months",
      "team": "1–2 researchers with mechanistic interpretability and fine-tuning experience",
      "estimated_gpu_cost": "$210–350 (at ~$1.50/hr A100 spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~100h A100-80GB (≈50–65h H100 equivalent)",
      "gpu_utilization": "Moderate (~50–60%) — agent handles coding and experiment execution, human approves designs and interprets results",
      "timeline": "2–4 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals",
      "claude_api_cost": "$25–60 (250–600 turns at ~$0.10/turn)",
      "estimated_gpu_cost": "$150–250",
      "risk_note": "Entrainment head identification on Qwen2.5-7B may require methodology adaptation; if differentiable masking doesn't transfer cleanly, add 1 week for method debugging. Phase 0 premise validation (ablation on complex benchmarks) is low-risk and provides early go/no-go signal within 2 days."
    },
    "auto_research": {
      "gpu_hours": "~300h A100-80GB (≈150–195h H100 equivalent, within ≤200 H100-hour budget)",
      "gpu_utilization": "High (~90–95%) — continuous experiment pipeline",
      "timeline": "8–14 days with 4× A100-80GB",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$200–400 (2000–4000 turns for full experiment loop)",
      "estimated_gpu_cost": "$450–750",
      "speed_bottleneck": "GPU count — head identification requires full forward passes; each contrastive training run needs 1× A100-80GB for ~3h (8B model); 4 GPUs enable parallel ablations across models",
      "budget_management": "If approaching 200 H100-hour limit: (1) drop Qwen2.5-7B experiments (saves ~50h A100), (2) reduce progressive-expansion stages to top-8 only (saves ~30h A100), (3) reduce NoisyBench evaluation to 6 of 11 datasets (saves ~15h A100). Phase 0 premise validation takes ~10h A100 and is the first experiment; if ablation shows <3% degradation on complex tasks, pivot framing to distraction-robustness generalization before investing in later phases.",
      "risk_note": "Progressive head expansion may require hyperparameter tuning across the 8→16→all-heads curriculum; stability monitoring (Phase 3e) provides automatic early stopping if instability appears"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstracts due July 21, 2026; full papers due July 28, 2026)",
    "ARR August 3, 2026 cycle → EACL 2027 (commitment deadline: October 11, 2026)"
  ],
  "venue_note": "The user's original target of EMNLP 2026 via ARR is infeasible — the ARR May 2026 deadline is May 25 (8 days from today, May 17), insufficient for completing even Phase 0. AAAI 2027 (papers due July 28) provides ~10 weeks and is the primary target. EACL 2027 (ARR August 3) provides ~11 weeks as a backup. Both venues are appropriate for this work's combination of mechanistic interpretability and fine-tuning methodology.",
  "level": "top-tier",
  "key_references": [
    "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs (ACL 2025, aclanthology.org/2025.acl-long.791)",
    "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (NeurIPS 2025 Best Paper, arXiv:2505.06708, OpenReview:1b7whO4SfY)",
    "Focused Transformer: Contrastive Training for Context Scaling [FoT] (NeurIPS 2023, arXiv:2307.03170)",
    "Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers [CHG] (NeurIPS 2025, arXiv:2505.13737)",
    "Mechanistic Fine-tuning for In-context Learning [ABFT] (arXiv 2025, 2505.14233)",
    "MuDAF: Long-Context Multi-Document Attention Focusing through Contrastive Learning on Attention Heads (arXiv 2025, 2502.13963)",
    "Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search (NeurIPS 2025, arXiv:2502.01609)",
    "Lost in the Noise: How Reasoning Models Fail with Contextual Distractors [RARE] (arXiv 2026, 2601.07226)",
    "How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark (EMNLP 2025 Oral, arXiv:2505.18761)",
    "Making Bias Non-Predictive: Training Robust LLM Judges via Reinforcement Learning [EIT] (arXiv 2026, 2602.01528)",
    "From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models [RetMask] (arXiv 2026, 2601.11020)",
    "In-Context Learning Without Copying [Hapax] (arXiv 2025, 2511.05743)",
    "Head Pursuit: Probing Attention Specialization in Multimodal Transformers (arXiv 2025, 2510.21518)",
    "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality (arXiv 2026, 2602.16740)"
  ],
  "description": "We propose Contrastive Entrainment Calibration (CEC), the first method to make entrainment heads query-conditional in existing models via circuit-level contrastive fine-tuning. CEC addresses a three-sided gap in the current landscape: (1) Gated Attention (NeurIPS 2025 Best Paper) achieves query-conditional per-head gating but requires pre-training from scratch — inapplicable to existing deployed models; (2) ablation (ACL 2025) is circuit-level but query-agnostic — it removes all entrainment regardless of context relevance; (3) behavioral training (DPO/RARE) is query-aware but mechanism-agnostic — it never modifies the entrainment circuit. CEC bridges this gap by providing query-conditional circuit-level control as a lightweight fine-tuning method.\n\nWe begin with a premise-validation experiment (Phase 0): testing ablation on complex benchmarks (BBH, multi-hop QA, RAG/grounded QA) to empirically establish whether static ablation degrades context-dependent tasks — if so, this motivates the need for query-conditional calibration; if not, CEC's value shifts to distraction-robustness generalization.\n\nUsing role-switching contrastive pairs — where the SAME passage is relevant context for one query but an irrelevant distractor for another — we train entrainment heads' Q/K projections to gate on query-context alignment rather than unconditionally boosting all context-seen tokens. This extends the contrastive-training-for-distraction paradigm introduced by Focused Transformer (NeurIPS 2023) from the general key-value space to specific mechanistically-identified entrainment heads, and from crossbatch negatives to role-switching pairs that structurally require query-conditioning. CHG (NeurIPS 2025) provides causal evidence that head roles are context-dependent (facilitating/interfering/irrelevant vary by task), directly supporting the feasibility of making entrainment heads query-conditional.\n\nTo address MuDAF's scalability bottleneck (convergence collapse beyond 8 heads), we introduce progressive head training with formal justification: sequential expansion reduces gradient variance from H-head simultaneous perturbation to k-head substeps, analogous to coordinate descent. We provide an explicit stability-monitoring protocol and fallback to the maximal stable subset.\n\nWe evaluate on: (1) generalization to unseen distractor types (NoisyBench, Adaptive Distraction tree-search) as the primary metric, with DPO and RARE as behavioral baselines; (2) open-ended QA under distraction; (3) context-dependent task performance (RAG, grounded QA) to demonstrate beneficial entrainment is preserved; (4) ICL preservation on MMLU, BBH, and the original 3 tasks; (5) comparison with static ablation to quantify CEC's query-conditional advantage.",
  "project_name": "contrastive_entrain_calib",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — Overstated core premise: 'Llama See, Llama Do' (ACL 2025) shows ablating entrainment heads causes only 0.2-3% ICL degradation (73.6→72.0% spelling, 74.4→73.0% translation, 100→100% arithmetic). The paper explicitly states 'removing the entrainment heads has only a negligible to small effect' on other capabilities and does NOT claim these heads enable ICL or discuss a 'dual-use' problem. The 'fundamental double-bind' framing — that suppressing entrainment destroys ICL — is not supported by the mechanistic evidence.", "CRITICAL — Model choice violates user constraints: User explicitly specifies 'Fine-tune from existing checkpoints (Llama-3-8B, Qwen2.5-7B/14B)' and '≤200 H100-hours.' The proposal uses Qwen3.6-27B (released April 2026, 27B dense), which is neither in the specified model list nor within the same compute class. Must use the user-specified models.", "CRITICAL — ARR deadline infeasibility: The EMNLP 2026 ARR submission deadline is May 25, 2026 — only 8 days from today (May 17). Even the auto-research timeline (10-18 days) cannot meet this. The May 25 target should be removed or replaced with the October 2026 ARR cycle.", "MAJOR — MuDAF scalability bottleneck: MuDAF found that contrastive Q-K learning becomes unstable beyond ~8 heads and 'training will become unstable and struggle to converge' when engaging more. Entrainment heads are 3.2-10.7% of all heads (e.g., 36 of 1024 for one relation in Llama-3.1-8B). Training all entrainment heads simultaneously with contrastive Q-K loss may face the same instability, requiring a head-selection or progressive training strategy not currently addressed.", "MAJOR — Competing baseline understated: EIT (arXiv:2602.01528) achieves 39.1% generalization to unseen distraction types via purely behavioral RL on Qwen3-4B. This is a strong baseline that the proposal needs to convincingly surpass. The proposal claims 'behavioral fixes cannot generalize to novel distractor types' but EIT demonstrates substantial generalization already.", "MODERATE — ABFT applicability gap: ABFT was demonstrated only for classification tasks with finite label sets (0.01% data cost claim). The proposal extends this to open-ended reasoning/QA settings where there are no discrete 'correct label tokens' to attend to. The loss function must be re-derived for non-classification tasks, which is non-trivial and unaddressed.", "MODERATE — Entrainment head identification transferability: The differentiable masking method from 'Llama See, Llama Do' was validated only on Llama-2-7B/13B, Llama-3.1-8B, and GPT-2 XL. Transfer to Qwen-family architectures is unvalidated, and the proposal acknowledges this risk but underestimates the effort needed.", "MINOR — Hapax finding undermines the induction-ICL coupling assumption: 'In-Context Learning Without Copying' (arXiv:2511.05743) shows that training without induction-head gradients preserves abstractive ICL, suggesting ICL mechanisms are more distributed than the proposal assumes. This weakens the theoretical argument that circuit-level intervention on specific heads is necessary."]
Feedback: The proposal has a well-designed technical approach but rests on a critically overstated theoretical premise. Here is specific guidance for revision:

1. **Fix the core premise**: Re-read 'Llama See, Llama Do' carefully. The paper shows entrainment head ablation barely affects ICL (0.2-3% drop). Reframe: instead of claiming a 'fundamental double-bind,' argue that (a) simple ablation is too coarse-grained (zeroing out heads entirely), (b) ablation was tested only on 3 simple ICL tasks — more complex few-shot reasoning (MMLU, BBH) may show larger degradation, and (c) your method aims for SELECTIVE suppression that preserves full head functionality, which ablation cannot provide. This is a more defensible and still interesting contribution.

2. **Use user-specified models**: Switch to Llama-3-8B and Qwen2.5-7B/14B as the user requires. This actually simplifies the head identification step since 'Llama See, Llama Do' already validated on Llama models.

3. **Fix the timeline**: Remove the May 25 ARR deadline. Target the October 2026 ARR cycle for EMNLP 2026 commitment, or target ACL 2026 (if deadlines align). Alternatively, target AAAI 2027.

4. **Address MuDAF's scalability finding**: Propose a head-grouping or progressive training strategy. For example, train contrastive loss on top-k most active entrainment heads first, then expand. Or use a per-head loss weight based on entrainment strength.

5. **Properly benchmark against EIT**: EIT's 39.1% generalization is your strongest behavioral baseline. Explain specifically why circuit-level intervention should beat behavioral RL — e.g., EIT requires bias-type-balanced training data construction, while your method's role-switching naturally provides relevance signals without bias engineering.

6. **Adapt ABFT loss for non-classification tasks**: The attention-score objective in ABFT targets label tokens. For QA/reasoning, define the objective in terms of attention to gold-passage tokens vs. distractor tokens (similar to MuDAF's formulation but applied to entrainment heads).

7. **Strengthen the MuDAF differentiation**: Currently the main difference is 'entrainment heads instead of retrieval heads.' Add: (a) role-switching contrastive pairs (MuDAF uses fixed relevant/irrelevant assignments), (b) ICL-preservation regularizer (MuDAF doesn't test ICL), (c) novel distractor generalization testing (MuDAF doesn't test this).

### Round 2 review
Verdict: revise
Issues: ["MAJOR — Missing critical related work: (1) Gated Attention / Qwen3-Next (NeurIPS 2025 Best Paper, OpenReview:1b7whO4SfY) implements exactly query-conditional per-head sigmoid gating (gate = sigmoid(linear(query)) * attn_output), learned end-to-end during pre-training, already deployed in Qwen3-Next-80B. This is the EXACT mechanism CEC proposes (query-conditional per-head gating on attention) and won Best Paper — CEC must cite it and clearly differentiate. (2) Focused Transformer / FoT (NeurIPS 2023, arXiv:2307.03170) uses contrastive training (crossbatch negatives) to restructure the key-value space and reduce attention distraction in long contexts — the closest prior art for contrastive-training-for-distraction. (3) Causal Head Gating / CHG (NeurIPS 2025, arXiv:2505.13737) demonstrates contrastive head gating with role taxonomy (facilitating/interfering/irrelevant), showing head roles vary by context — directly supports but also partially anticipates CEC's role-switching concept.", "MAJOR — EIT mischaracterization: The proposal claims EIT 'achieves 39.1% generalization from bandwagon→distraction bias' and treats it as 'the strongest behavioral baseline' and the 'behavioral ceiling to beat.' Verification reveals: (a) the 39.1% is a robustness-rate improvement (+39.1pp on MMLU-Pro, from 40.6% to 79.7%), not a generalization percentage; (b) EIT targets cognitive biases in LLM-as-judge settings (bandwagon appeals, authority claims), NOT contextual entrainment/distraction (irrelevant passages in context); (c) EIT operates on Qwen3-4B with MCQ-only evaluation. Using a judge-debiasing paper as the primary distraction-robustness baseline is a category mismatch that undermines the evaluation plan.", "MODERATE — Unvalidated core premise: The proposal argues that ablation is too coarse-grained because it was 'tested only on three simple ICL tasks' and hypothesizes complex reasoning will degrade more. This is a fair hypothesis but is unvalidated speculation that the entire CEC contribution rests on. If ablation causes <3% degradation on MMLU, BBH, and multi-hop QA too, CEC's practical advantage over simple ablation is marginal. The proposal should include validating this premise (testing ablation on complex benchmarks) as a preliminary experiment BEFORE building the full CEC pipeline.", "MODERATE — Progressive head training lacks justification: MuDAF found contrastive Q/K training 'becomes unstable and struggles to converge' beyond 8 heads. The proposal's solution (progressive expansion 8→16→all with warmup) is intuitive but entirely unvalidated. The instability may be inherent to the contrastive attention-score loss landscape when many heads are simultaneously perturbed, not merely a curriculum issue. No theoretical or empirical argument is provided for why progressive expansion avoids the convergence failure.", "MODERATE — AAAI 2027 deadline is July 28, not 'August 2026': Verified via AAAI-27 CFP — abstracts due July 21, 2026; full papers due July 28, 2026. The proposal states '~August 2026' which is inaccurate. Combined with the auto-research timeline of 8–14 days, starting from today (May 17) this is feasible but tight. The ARR August 2026 deadline for EACL 2027 is August 3, 2026 (confirmed via EACL announcement), not a generic 'August cycle.'", "MINOR — Auto-research H100 estimate exceeds budget at high end: 175–230h H100 equivalent, but user constraint is ≤200 H100-hours. The 230h high-end exceeds the budget by 15%. Tighten the estimate or add explicit scoping guidance for what to cut if approaching the limit.", "MINOR — Venue mismatch with user request: User explicitly asked for 'Target: EMNLP 2026, ARR submission.' The May 25, 2026 ARR deadline makes this infeasible (confirmed — 8 days away). The proposal targets AAAI 2027 and EACL 2027 instead, which are reasonable alternatives, but should explicitly acknowledge the EMNLP 2026 infeasibility and propose the path forward."]
Feedback: The revision substantially improved the core premise and model choices from Round 1. The remaining issues are addressable:

1. **Cite and differentiate from Gated Attention (NeurIPS 2025 Best Paper)**: This paper implements query-conditional per-head gating (sigmoid(linear(query)) * attn_output) at scale during pre-training. CEC's differentiation: (a) CEC is a fine-tuning method, not an architectural change requiring pre-training from scratch; (b) CEC specifically targets entrainment heads identified via mechanistic analysis, while Gated Attention learns gates for all heads generally; (c) CEC uses contrastive role-switching training signal, not standard LM objective. Also cite Focused Transformer (NeurIPS 2023) as the first contrastive-training-for-attention-distraction work, and CHG (NeurIPS 2025) for causal evidence that head roles are context-dependent.

2. **Replace EIT as the primary behavioral baseline**: EIT targets judge-debiasing, not contextual distraction. Instead, use DPO with synthetic distractors (NeurIPS 2025 'Adaptive Distraction') and RARE (arXiv:2601.07226) as the direct behavioral baselines. If citing EIT at all, note it addresses a related but distinct problem (prompt-level cognitive bias vs. context-level entrainment).

3. **Add a premise-validation experiment as Phase 0**: Before building CEC, test ablation (from 'Llama See, Llama Do') on complex benchmarks — BBH, MMLU hard subsets, multi-hop QA (HotpotQA/MuSiQue), and RAG/grounded QA. If ablation causes >5% degradation on these tasks (vs. <3% on simple tasks), the CEC premise is validated and you have a strong motivating result. If not, the contribution pivots to distraction-robustness generalization rather than ICL preservation.

4. **Provide a theoretical argument for progressive training**: The claim that progressive expansion solves MuDAF's convergence failure needs more than intuition. Consider: (a) formal analogy to curriculum learning theory; (b) the observation that entrainment heads likely have different functional overlap — training high-entrainment-strength heads first means lower-strength heads can adjust to a more stable landscape; (c) explicit fallback: if instability persists at N heads, report results for the stable subset rather than claiming universal scalability.

5. **Tighten compute estimates**: Cap auto-research at 200h H100 equivalent. Specify what gets cut if approaching the limit (e.g., drop Qwen2.5-14B experiments, reduce progressive-expansion stages).

6. **Fix venue deadlines**: AAAI 2027 abstracts are due July 21 (not 'August'). ARR for EACL 2027 is August 3. Add a sentence acknowledging EMNLP 2026 is infeasible given the May 25 ARR deadline.


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
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "7ee26335-3b16-4fa3-b3bd-b59b5c9840ed",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T08:58:39.287Z_

```json
{
  "parentUuid": "7ee26335-3b16-4fa3-b3bd-b59b5c9840ed",
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
  "uuid": "45faf706-0461-4cc0-a049-d83b44e7bc0a",
  "timestamp": "2026-05-17T08:58:39.287Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T08:58:39.287Z_

```json
{
  "parentUuid": "45faf706-0461-4cc0-a049-d83b44e7bc0a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b47655e4-cf0c-42f8-bd8c-25e6bfd32277",
  "timestamp": "2026-05-17T08:58:39.287Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
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
  "leafUuid": "b47655e4-cf0c-42f8-bd8c-25e6bfd32277",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Query-conditional entrainment heads via contrastive fine-tuning",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Assistant

_source line 8 · 2026-05-17T08:58:48.622Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea, which is now in its third revision. I need to independently verify the claims, check for missing related work, assess feasibility, and determine if the remaining issues from previous rounds have been adequately addressed.

Let me start by verifying the key claims and searching for potentially missing related work.

Key things to verify:
1. The existence and claims of cited papers (especially newer ones like Gated Attention, CHG, ABFT, MuDAF)
2. Whether the gap claimed still exists - has anyone done circuit-level training for entrainment?


3. The publication timeline and relevant deadlines for venues like AAAI 2027 and ARR August 2026
4. Any competing work that might address similar problems
5. Whether the progressive head training approach has solid justification
6. If the computational requirements are realistic

I'll need to work through these systematically to get a complete picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b47655e4-cf0c-42f8-bd8c-25e6bfd32277",
  "isSidechain": false,
  "requestId": "req_011Cb7s95hpvQNwrYzh7MiwS",
  "type": "assistant",
  "uuid": "8bbbd2e5-974b-46ca-8835-98e846f72078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtQzvNw6dGKUSMm2uHn2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22258
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

_source line 9 · 2026-05-17T08:58:48.624Z_

I'll conduct an independent verification of this idea's claims, checking for missing related work, validating references, and assessing feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bbbd2e5-974b-46ca-8835-98e846f72078",
  "isSidechain": false,
  "requestId": "req_011Cb7s95hpvQNwrYzh7MiwS",
  "type": "assistant",
  "uuid": "4d6b3362-b5be-420e-91e6-c079aeec32c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtQzvNw6dGKUSMm2uHn2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22258
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

_source line 10 · 2026-05-17T08:58:53.577Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016L1tTohjFobsc3f4htfa85`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Gated Attention NeurIPS 2025",
  "prompt": "Search for the paper \"Gated Attention for Large Language Models\" that supposedly won NeurIPS 2025 Best Paper. The claimed arXiv ID is 2505.06708 and OpenReview ID is 1b7whO4SfY. I need to verify:\n1. Does this paper actually exist?\n2. Did it win NeurIPS 2025 Best Paper?\n3. Does it implement query-conditional per-head sigmoid gating as described?\n4. Was it pre-trained from scratch on 3.5T tokens?\n5. Is it deployed only in Qwen3-Next models?\n\nUse WebSearch to find information about this paper. Try queries like:\n- \"Gated Attention Large Language Models NeurIPS 2025 Best Paper\"\n- \"arXiv 2505.06708\"\n- \"Qwen3-Next Gated Attention\"\n- site:openreview.net \"Gated Attention\"\n\nThen use WebFetch to read the arXiv abstract if possible. Report all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d6b3362-b5be-420e-91e6-c079aeec32c8",
  "isSidechain": false,
  "requestId": "req_011Cb7s95hpvQNwrYzh7MiwS",
  "type": "assistant",
  "uuid": "eb5a9287-73e0-4617-b4c0-28f2b2547c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtQzvNw6dGKUSMm2uHn2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22258
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

_source line 11 · 2026-05-17T08:59:00.288Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V5mTSrkNvbbP73y7VyVhx9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify MuDAF and ABFT papers",
  "prompt": "Search for and verify these two papers:\n\n1. \"MuDAF: Long-Context Multi-Document Attention Focusing through Contrastive Learning on Attention Heads\" (arXiv:2502.13963). I need to verify:\n   - Does it exist?\n   - Does it apply contrastive Q-K learning (InfoNCE on query-key similarity) to retrieval heads?\n   - Does it report that training becomes unstable beyond 8 heads?\n   - Does it report HotpotQA 69.6% and MuSiQue 48.2% on Llama-3.1-8B?\n\n2. \"Mechanistic Fine-tuning for In-context Learning\" or \"ABFT\" (arXiv:2505.14233). I need to verify:\n   - Does it exist?\n   - Does it demonstrate attention-score fine-tuning via W_Q/W_K training?\n   - Was it demonstrated only for classification with finite label sets?\n   - Does it claim ~512 samples are sufficient?\n\nUse WebSearch with queries like:\n- \"MuDAF contrastive learning attention heads multi-document\"\n- \"arXiv 2502.13963\"\n- \"ABFT mechanistic fine-tuning in-context learning\"\n- \"arXiv 2505.14233\"\n\nTry to fetch the arXiv abstracts if possible. Report all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb5a9287-73e0-4617-b4c0-28f2b2547c10",
  "isSidechain": false,
  "requestId": "req_011Cb7s95hpvQNwrYzh7MiwS",
  "type": "assistant",
  "uuid": "b4813b76-d4dd-46b6-9d29-1b4ec3a2ca3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtQzvNw6dGKUSMm2uHn2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22258
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

_source line 12 · 2026-05-17T08:59:07.455Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011KS8NpC4AbXbcBopwjFpEx`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing work circuit-level training",
  "prompt": "Search for any recent work (2025-2026) that does circuit-level or attention-head-level training to address distraction or entrainment in LLMs. I'm reviewing a paper idea that claims no one has done \"query-conditional circuit-level control of entrainment heads via fine-tuning.\" I need to find if there's competing work the authors might have missed.\n\nSearch queries to try:\n1. \"attention head fine-tuning distraction robustness LLM 2025 2026\"\n2. \"circuit-level training entrainment language model\"\n3. \"query-conditional attention gating fine-tuning\"\n4. \"contrastive attention head training relevance\"\n5. \"mechanistic interpretability training intervention attention heads\"\n6. \"attention regularization distractor robustness\"\n7. \"selective attention suppression training LLM\"\n8. site:arxiv.org \"entrainment heads\" OR \"attention head training\" 2025 2026\n\nAlso search for:\n- \"Focused Transformer contrastive training\" (NeurIPS 2023, arXiv:2307.03170) - verify it exists\n- \"Causal Head Gating\" (arXiv:2505.13737) - verify it exists and its claims\n\nReport everything you find, especially any work that combines attention-head-level intervention with training (not just inference-time analysis)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4813b76-d4dd-46b6-9d29-1b4ec3a2ca3e",
  "isSidechain": false,
  "requestId": "req_011Cb7s95hpvQNwrYzh7MiwS",
  "type": "assistant",
  "uuid": "abaa22f8-6ba1-41f7-904c-3211671b818b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtQzvNw6dGKUSMm2uHn2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22258,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22258
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

_source line 13 · 2026-05-17T09:00:32.553Z_

<details><summary>↩ Tool result · `toolu_01V5mTSrkNvbbP73y7VyVhx9`</summary>

```text
I now have comprehensive information on both papers. Here is my full report:

---

## Paper 1: MuDAF (arXiv:2502.13963)

**Title:** "MuDAF: Long-Context Multi-Document Attention Focusing through Contrastive Learning on Attention Heads"

**Existence:** CONFIRMED. The paper exists at arXiv:2502.13963, authored by researchers at Microsoft.

**Claim: Contrastive Q-K learning (InfoNCE on query-key similarity) applied to retrieval heads?**
LARGELY CONFIRMED. The loss function is:

ℒ_CON = -sum_h log[ e^(sim(Q_t^[h], K_Pk^[h]) / tau) / sum_Pj e^(sim(Q_t^[h], K_Pj^[h]) / tau) ]

This is structurally identical to InfoNCE -- it maximizes query-key similarity between questions and golden passages while minimizing similarity to irrelevant passages, applied specifically to retrieval heads. Calling it "InfoNCE on query-key similarity" is an accurate characterization.

**Claim: Training becomes unstable beyond 8 heads?**
CONFIRMED. The paper explicitly states: "We did not see much improvement if we consistently increased the number of selected attention heads beyond 8 heads. Furthermore, if we engage all attention heads in contrastive learning, the training will become unstable and struggle to converge, leading to a collapse of the overall performance."

**Claim: HotpotQA 69.6% and MuSiQue 48.2% on Llama-3.1-8B?**
CONFIRMED. From Table 2, MuDAF achieves exactly HotpotQA 69.6% F1 and MuSiQue 48.2% F1 on Llama-3.1-8B.

---

## Paper 2: Mechanistic Fine-tuning for In-context Learning / ABFT (arXiv:2505.14233)

**Title:** "Mechanistic Fine-tuning for In-context Learning"

**Existence:** CONFIRMED. The paper exists at arXiv:2505.14233, authored by Hakaze Cho, Peng Luo, and others.

**Claim: Attention-score fine-tuning via W_Q/W_K training?**
CONFIRMED. The paper states: "we fine-tune only the W_K and W_Q projection matrices of every attention head." Gradients are back-propagated only to W_Q and W_K matrices, and the training objective operates directly on attention scores (not final outputs).

**Claim: Demonstrated only for classification with finite label sets?**
CONFIRMED. The limitations section explicitly states: "the induction head-based explanation of ICL...applies only to classification tasks with a finite label set." The authors acknowledge that extending to "open-ended tasks remains an open challenge."

**Claim: ~512 samples are sufficient?**
CONFIRMED. The paper specifies "training samples n_d=512" and claims "0.01% data cost compared to previous methods" (compared to MetaICL's 3.55M samples).

---

## Summary

All specific claims about both papers are verified as accurate:

| Claim | Status |
|-------|--------|
| MuDAF exists at 2502.13963 | Confirmed |
| MuDAF uses contrastive Q-K learning (InfoNCE-style) on retrieval heads | Confirmed |
| MuDAF reports instability beyond 8 heads | Confirmed |
| MuDAF reports HotpotQA 69.6%, MuSiQue 48.2% on Llama-3.1-8B | Confirmed |
| ABFT exists at 2505.14233 | Confirmed |
| ABFT fine-tunes W_Q/W_K with attention-score objectives | Confirmed |
| ABFT limited to classification with finite label sets | Confirmed |
| ABFT uses ~512 samples | Confirmed |

Sources:
- [MuDAF: Long-Context Multi-Document Attention Focusing (Abstract)](https://arxiv.org/abs/2502.13963)
- [MuDAF Full HTML](https://arxiv.org/html/2502.13963)
- [Mechanistic Fine-tuning for In-context Learning (Abstract)](https://arxiv.org/abs/2505.14233)
- [ABFT Full HTML](https://arxiv.org/html/2505.14233v1)
- [MuDAF GitHub Repository](https://github.com/NeosKnight233/MuDAF)

agentId: a27454b2bf33d65ce (use SendMessage with to: 'a27454b2bf33d65ce' to continue this agent)
&lt;usage>total_tokens: 16520
tool_uses: 7
duration_ms: 92262&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4813b76-d4dd-46b6-9d29-1b4ec3a2ca3e",
  "isSidechain": false,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "87a60b9b-2d7c-4b37-84a1-296718f63c8f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these two papers:\n\n1. \"MuDAF: Long-Context Multi-Document Attention Focusing through Contrastive Learning on Attention Heads\" (arXiv:2502.13963). I need to verify:\n   - Does it exist?\n   - Does it apply contrastive Q-K learning (InfoNCE on query-key similarity) to retrieval heads?\n   - Does it report that training becomes unstable beyond 8 heads?\n   - Does it report HotpotQA 69.6% and MuSiQue 48.2% on Llama-3.1-8B?\n\n2. \"Mechanistic Fine-tuning for In-context Learning\" or \"ABFT\" (arXiv:2505.14233). I need to verify:\n   - Does it exist?\n   - Does it demonstrate attention-score fine-tuning via W_Q/W_K training?\n   - Was it demonstrated only for classification with finite label sets?\n   - Does it claim ~512 samples are sufficient?\n\nUse WebSearch with queries like:\n- \"MuDAF contrastive learning attention heads multi-document\"\n- \"arXiv 2502.13963\"\n- \"ABFT mechanistic fine-tuning in-context learning\"\n- \"arXiv 2505.14233\"\n\nTry to fetch the arXiv abstracts if possible. Report all findings.",
    "agentId": "a27454b2bf33d65ce",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on both papers. Here is my full report:\n\n---\n\n## Paper 1: MuDAF (arXiv:2502.13963)\n\n**Title:** \"MuDAF: Long-Context Multi-Document Attention Focusing through Contrastive Learning on Attention Heads\"\n\n**Existence:** CONFIRMED. The paper exists at arXiv:2502.13963, authored by researchers at Microsoft.\n\n**Claim: Contrastive Q-K learning (InfoNCE on query-key similarity) applied to retrieval heads?**\nLARGELY CONFIRMED. The loss function is:\n\nℒ_CON = -sum_h log[ e^(sim(Q_t^[h], K_Pk^[h]) / tau) / sum_Pj e^(sim(Q_t^[h], K_Pj^[h]) / tau) ]\n\nThis is structurally identical to InfoNCE -- it maximizes query-key similarity between questions and golden passages while minimizing similarity to irrelevant passages, applied specifically to retrieval heads. Calling it \"InfoNCE on query-key similarity\" is an accurate characterization.\n\n**Claim: Training becomes unstable beyond 8 heads?**\nCONFIRMED. The paper explicitly states: \"We did not see much improvement if we consistently increased the number of selected attention heads beyond 8 heads. Furthermore, if we engage all attention heads in contrastive learning, the training will become unstable and struggle to converge, leading to a collapse of the overall performance.\"\n\n**Claim: HotpotQA 69.6% and MuSiQue 48.2% on Llama-3.1-8B?**\nCONFIRMED. From Table 2, MuDAF achieves exactly HotpotQA 69.6% F1 and MuSiQue 48.2% F1 on Llama-3.1-8B.\n\n---\n\n## Paper 2: Mechanistic Fine-tuning for In-context Learning / ABFT (arXiv:2505.14233)\n\n**Title:** \"Mechanistic Fine-tuning for In-context Learning\"\n\n**Existence:** CONFIRMED. The paper exists at arXiv:2505.14233, authored by Hakaze Cho, Peng Luo, and others.\n\n**Claim: Attention-score fine-tuning via W_Q/W_K training?**\nCONFIRMED. The paper states: \"we fine-tune only the W_K and W_Q projection matrices of every attention head.\" Gradients are back-propagated only to W_Q and W_K matrices, and the training objective operates directly on attention scores (not final outputs).\n\n**Claim: Demonstrated only for classification with finite label sets?**\nCONFIRMED. The limitations section explicitly states: \"the induction head-based explanation of ICL...applies only to classification tasks with a finite label set.\" The authors acknowledge that extending to \"open-ended tasks remains an open challenge.\"\n\n**Claim: ~512 samples are sufficient?**\nCONFIRMED. The paper specifies \"training samples n_d=512\" and claims \"0.01% data cost compared to previous methods\" (compared to MetaICL's 3.55M samples).\n\n---\n\n## Summary\n\nAll specific claims about both papers are verified as accurate:\n\n| Claim | Status |\n|-------|--------|\n| MuDAF exists at 2502.13963 | Confirmed |\n| MuDAF uses contrastive Q-K learning (InfoNCE-style) on retrieval heads | Confirmed |\n| MuDAF reports instability beyond 8 heads | Confirmed |\n| MuDAF reports HotpotQA 69.6%, MuSiQue 48.2% on Llama-3.1-8B | Confirmed |\n| ABFT exists at 2505.14233 | Confirmed |\n| ABFT fine-tunes W_Q/W_K with attention-score objectives | Confirmed |\n| ABFT limited to classification with finite label sets | Confirmed |\n| ABFT uses ~512 samples | Confirmed |\n\nSources:\n- [MuDAF: Long-Context Multi-Document Attention Focusing (Abstract)](https://arxiv.org/abs/2502.13963)\n- [MuDAF Full HTML](https://arxiv.org/html/2502.13963)\n- [Mechanistic Fine-tuning for In-context Learning (Abstract)](https://arxiv.org/abs/2505.14233)\n- [ABFT Full HTML](https://arxiv.org/html/2505.14233v1)\n- [MuDAF GitHub Repository](https://github.com/NeosKnight233/MuDAF)"
      }
    ],
    "totalDurationMs": 92262,
    "totalTokens": 16520,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1258,
      "cache_read_input_tokens": 14142,
      "output_tokens": 1119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1258
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1119,
          "cache_read_input_tokens": 14142,
          "cache_creation_input_tokens": 1258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1258,
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
  "sourceToolAssistantUUID": "b4813b76-d4dd-46b6-9d29-1b4ec3a2ca3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T09:01:05.106Z_

<details><summary>↩ Tool result · `toolu_016L1tTohjFobsc3f4htfa85`</summary>

```text
I now have comprehensive information to provide a detailed verification report. Here are my findings:

---

## Verification Report: "Gated Attention for Large Language Models"

### 1. Does this paper actually exist?

**YES.** The paper is real and fully verified:
- **Full title:** "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
- **arXiv ID:** 2505.06708 (submitted May 10, 2025) -- CONFIRMED at https://arxiv.org/abs/2505.06708
- **OpenReview ID:** 1b7whO4SfY -- CONFIRMED at https://openreview.net/forum?id=1b7whO4SfY
- **Authors:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin (Alibaba/Qwen team)

### 2. Did it win NeurIPS 2025 Best Paper?

**YES.** Confirmed via the official NeurIPS blog post (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/). It was one of four Best Papers selected from 5,290 accepted submissions at NeurIPS 2025. It was also designated as a NeurIPS 2025 Oral presentation. Alibaba Cloud publicized this win as well.

### 3. Does it implement query-conditional per-head sigmoid gating as described?

**YES, substantially correct.** The paper describes "applying a query-dependent head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)." The terminology used in the paper is "query-dependent" rather than "query-conditional," but these are semantically equivalent. The gating is:
- **Per-head:** Each attention head has its own gate scalar
- **Sigmoid-based:** Uses a sigmoid activation function
- **Query-dependent:** The gate value is conditioned on the query

The paper also studies an "elementwise" variant where each element of the attention output is modulated independently. The GitHub repo (https://github.com/qiuzh20/gated_attention) provides both `gate_headwise` and `gate_elementwise` implementations.

### 4. Was it pre-trained from scratch on 3.5T tokens?

**PARTIALLY VERIFIED.** The paper states that models were "trained on a 3.5 trillion token dataset" in a comprehensive comparison of over 30 variants of 15B MoE models and 1.7B dense models. However, none of the sources I found explicitly state "pre-trained from scratch" versus continued pre-training. Given the nature of the study (comparing 30+ architectural variants systematically), it is highly likely these were trained from scratch for fair comparison, but the exact wording "pre-trained from scratch" does not appear verbatim in the accessible sources.

### 5. Is it deployed ONLY in Qwen3-Next models?

**NO -- this claim is too narrow.** While the paper and GitHub repo confirm that Gated Attention "has been successfully integrated into the official Qwen3-Next architecture" (specifically Qwen3-Next-80B-A3B-Instruct and Qwen3-Next-80B-A3B-Thinking), the technology has also propagated to:
- **Qwen3-Coder-Next** -- uses the same hybrid architecture
- **Qwen3.5** -- also uses gated attention in its hybrid architecture (interleaving Gated DeltaNet with full gated attention layers)

So the claim that it is deployed "only in Qwen3-Next models" is **incorrect** -- it is now used across multiple Qwen model families including Qwen3.5.

---

## Summary Table

| Claim | Verdict |
|-------|---------|
| Paper exists with arXiv ID 2505.06708 | CONFIRMED |
| OpenReview ID is 1b7whO4SfY | CONFIRMED |
| Won NeurIPS 2025 Best Paper | CONFIRMED |
| Implements query-conditional per-head sigmoid gating | CONFIRMED (paper uses "query-dependent" terminology) |
| Pre-trained from scratch on 3.5T tokens | LIKELY TRUE but not explicitly stated as "from scratch" |
| Deployed only in Qwen3-Next models | FALSE -- also in Qwen3-Coder-Next and Qwen3.5 |

Sources:
- [arXiv: 2505.06708](https://arxiv.org/abs/2505.06708)
- [OpenReview Forum](https://openreview.net/forum?id=1b7whO4SfY)
- [NeurIPS 2025 Best Paper Awards Blog Post](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- [GitHub: qiuzh20/gated_attention](https://github.com/qiuzh20/gated_attention)
- [Alibaba Cloud Blog: Qwen Wins NeurIPS 2025 Best Paper](https://www.alibabacloud.com/blog/alibaba-qwen-wins-%E2%80%9Cneurips-2025-best-paper-award%E2%80%9D-for-breakthrough-in-attention-mechanisms_602708)
- [Qwen3-Next on Hugging Face](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
- [Qwen3.5 Architecture Analysis](https://huggingface.co/blog/mlabonne/qwen35)
- [NVIDIA Blog on Qwen3-Next](https://developer.nvidia.com/blog/new-open-source-qwen3-next-models-preview-hybrid-moe-architecture-delivering-improved-accuracy-and-accelerated-parallel-processing-across-nvidia-platform/)

agentId: ac03be8f131e42260 (use SendMessage with to: 'ac03be8f131e42260' to continue this agent)
&lt;usage>total_tokens: 22216
tool_uses: 13
duration_ms: 131523&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb5a9287-73e0-4617-b4c0-28f2b2547c10",
  "isSidechain": false,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "76feec7a-2b58-4e86-8d0b-7a2aba4a4008",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the paper \"Gated Attention for Large Language Models\" that supposedly won NeurIPS 2025 Best Paper. The claimed arXiv ID is 2505.06708 and OpenReview ID is 1b7whO4SfY. I need to verify:\n1. Does this paper actually exist?\n2. Did it win NeurIPS 2025 Best Paper?\n3. Does it implement query-conditional per-head sigmoid gating as described?\n4. Was it pre-trained from scratch on 3.5T tokens?\n5. Is it deployed only in Qwen3-Next models?\n\nUse WebSearch to find information about this paper. Try queries like:\n- \"Gated Attention Large Language Models NeurIPS 2025 Best Paper\"\n- \"arXiv 2505.06708\"\n- \"Qwen3-Next Gated Attention\"\n- site:openreview.net \"Gated Attention\"\n\nThen use WebFetch to read the arXiv abstract if possible. Report all findings in detail.",
    "agentId": "ac03be8f131e42260",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a detailed verification report. Here are my findings:\n\n---\n\n## Verification Report: \"Gated Attention for Large Language Models\"\n\n### 1. Does this paper actually exist?\n\n**YES.** The paper is real and fully verified:\n- **Full title:** \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\"\n- **arXiv ID:** 2505.06708 (submitted May 10, 2025) -- CONFIRMED at https://arxiv.org/abs/2505.06708\n- **OpenReview ID:** 1b7whO4SfY -- CONFIRMED at https://openreview.net/forum?id=1b7whO4SfY\n- **Authors:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin (Alibaba/Qwen team)\n\n### 2. Did it win NeurIPS 2025 Best Paper?\n\n**YES.** Confirmed via the official NeurIPS blog post (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/). It was one of four Best Papers selected from 5,290 accepted submissions at NeurIPS 2025. It was also designated as a NeurIPS 2025 Oral presentation. Alibaba Cloud publicized this win as well.\n\n### 3. Does it implement query-conditional per-head sigmoid gating as described?\n\n**YES, substantially correct.** The paper describes \"applying a query-dependent head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA).\" The terminology used in the paper is \"query-dependent\" rather than \"query-conditional,\" but these are semantically equivalent. The gating is:\n- **Per-head:** Each attention head has its own gate scalar\n- **Sigmoid-based:** Uses a sigmoid activation function\n- **Query-dependent:** The gate value is conditioned on the query\n\nThe paper also studies an \"elementwise\" variant where each element of the attention output is modulated independently. The GitHub repo (https://github.com/qiuzh20/gated_attention) provides both `gate_headwise` and `gate_elementwise` implementations.\n\n### 4. Was it pre-trained from scratch on 3.5T tokens?\n\n**PARTIALLY VERIFIED.** The paper states that models were \"trained on a 3.5 trillion token dataset\" in a comprehensive comparison of over 30 variants of 15B MoE models and 1.7B dense models. However, none of the sources I found explicitly state \"pre-trained from scratch\" versus continued pre-training. Given the nature of the study (comparing 30+ architectural variants systematically), it is highly likely these were trained from scratch for fair comparison, but the exact wording \"pre-trained from scratch\" does not appear verbatim in the accessible sources.\n\n### 5. Is it deployed ONLY in Qwen3-Next models?\n\n**NO -- this claim is too narrow.** While the paper and GitHub repo confirm that Gated Attention \"has been successfully integrated into the official Qwen3-Next architecture\" (specifically Qwen3-Next-80B-A3B-Instruct and Qwen3-Next-80B-A3B-Thinking), the technology has also propagated to:\n- **Qwen3-Coder-Next** -- uses the same hybrid architecture\n- **Qwen3.5** -- also uses gated attention in its hybrid architecture (interleaving Gated DeltaNet with full gated attention layers)\n\nSo the claim that it is deployed \"only in Qwen3-Next models\" is **incorrect** -- it is now used across multiple Qwen model families including Qwen3.5.\n\n---\n\n## Summary Table\n\n| Claim | Verdict |\n|-------|---------|\n| Paper exists with arXiv ID 2505.06708 | CONFIRMED |\n| OpenReview ID is 1b7whO4SfY | CONFIRMED |\n| Won NeurIPS 2025 Best Paper | CONFIRMED |\n| Implements query-conditional per-head sigmoid gating | CONFIRMED (paper uses \"query-dependent\" terminology) |\n| Pre-trained from scratch on 3.5T tokens | LIKELY TRUE but not explicitly stated as \"from scratch\" |\n| Deployed only in Qwen3-Next models | FALSE -- also in Qwen3-Coder-Next and Qwen3.5 |\n\nSources:\n- [arXiv: 2505.06708](https://arxiv.org/abs/2505.06708)\n- [OpenReview Forum](https://openreview.net/forum?id=1b7whO4SfY)\n- [NeurIPS 2025 Best Paper Awards Blog Post](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)\n- [GitHub: qiuzh20/gated_attention](https://github.com/qiuzh20/gated_attention)\n- [Alibaba Cloud Blog: Qwen Wins NeurIPS 2025 Best Paper](https://www.alibabacloud.com/blog/alibaba-qwen-wins-%E2%80%9Cneurips-2025-best-paper-award%E2%80%9D-for-breakthrough-in-attention-mechanisms_602708)\n- [Qwen3-Next on Hugging Face](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)\n- [Qwen3.5 Architecture Analysis](https://huggingface.co/blog/mlabonne/qwen35)\n- [NVIDIA Blog on Qwen3-Next](https://developer.nvidia.com/blog/new-open-source-qwen3-next-models-preview-hybrid-moe-architecture-delivering-improved-accuracy-and-accelerated-parallel-processing-across-nvidia-platform/)"
      }
    ],
    "totalDurationMs": 131523,
    "totalTokens": 22216,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 19613,
      "output_tokens": 1491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1491,
          "cache_read_input_tokens": 19613,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1111,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "eb5a9287-73e0-4617-b4c0-28f2b2547c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "76feec7a-2b58-4e86-8d0b-7a2aba4a4008",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Query-conditional entrainment heads via contrastive fine-tuning",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Tool result

_source line 17 · 2026-05-17T09:03:43.126Z_

<details><summary>↩ Tool result · `toolu_011KS8NpC4AbXbcBopwjFpEx`</summary>

```text
Based on my extensive research, here is a comprehensive report of findings relevant to your paper idea review.

---

## Summary of Findings

The specific phrase "query-conditional circuit-level control of entrainment heads via fine-tuning" returned zero results in web searches, suggesting this exact framing may indeed be novel. However, there is substantial closely related and potentially competing work that the authors should be aware of. The term "entrainment heads" specifically does not appear in any published work I could find -- this seems to be a term the paper authors coined.

---

## Verified Papers

**Focused Transformer: Contrastive Training for Context Scaling (arXiv:2307.03170)**
- Confirmed to exist. Published July 2023, revised November 2023.
- Authors: Szymon Tworkowski, Konrad Staniszewski, Mikołaj Pacek, Yuhuai Wu, Henryk Michalewski, Piotr Milos.
- Directly relevant: Uses contrastive training to improve the key-value space structure of attention layers, exposing them to irrelevant "distractor" keys during training to help differentiate relevant from irrelevant context. Implemented in LongLLaMA (256k context).
- This is the closest precedent to "contrastive attention head training for relevance" -- though it operates on the KV-space rather than gating specific heads.

**Causal Head Gating (arXiv:2505.13737)**
- Confirmed to exist. Submitted May 19, 2025, revised October 23, 2025.
- Authors: Andrew Nam, Henry Conklin, Yukang Yang, Thomas Griffiths, Jonathan Cohen, Sarah-Jane Leslie.
- Proposes learnable soft gates over attention heads to assign causal taxonomy (facilitating, interfering, or irrelevant) based on task performance impact.
- Introduces "contrastive CHG" to isolate sub-circuits for specific task components.
- Key limitation: This is primarily an **interpretability** framework (uses standard next-token prediction to learn gates for analysis), NOT a training intervention to improve model behavior. However, it is extremely close to the claimed novelty -- it does learn query-conditional gates over attention heads at the circuit level.

---

## Highly Relevant Competing Work (2024-2026)

### 1. Pinpoint Tuning / SPT (ICML 2024, arXiv:2409.01658)
"From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning"
- **Directly trains only specific attention heads** (approximately 4% of heads) identified as responsible for sycophantic behavior.
- This is arguably the closest existing work to "circuit-level fine-tuning of specific heads to reduce entrainment/sycophancy." The authors of the paper you are reviewing need to cite and differentiate from this.

### 2. Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644, January 2026)
- Finds that sycophancy signals are most linearly separable in attention activations.
- Steering using probes is most effective in a sparse subset of middle-layer attention heads.
- Relevant attention heads attend disproportionately to "expressions of user doubt" -- this is mechanistically very close to "entrainment heads."

### 3. A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (arXiv:2601.18939, January 2026)
- Isolates ~3% of MLP neurons responsible for sycophancy, fine-tunes only those using gradient masking.
- Matches/exceeds SOTA on sycophancy benchmarks with minimal data.
- Neuron-level (not head-level) but same paradigm of targeted fine-tuning at the circuit level.

### 4. SEAL: Scaling to Emphasize Attention for Long-Context Retrieval (arXiv:2501.15225, January 2025, ACL 2025)
- Learns attention scaling factors to emphasize/suppress specific heads for retrieval performance.
- Uses SGD-based fine-tuning of per-head attention strength.
- Relevant because it fine-tunes head-level attention strength conditioned on task (retrieval), though not query-conditional.

### 5. Gated Attention (NeurIPS 2025 Best Paper, Qwen team)
- Introduces query-dependent sigmoid gates after SDPA output: Y' = Y * sigma(X * W_theta)
- This is architecturally query-conditional, per-head gating of attention -- very close to "query-conditional circuit-level control."
- Key difference: This is an architectural modification trained from scratch, not a fine-tuning intervention on existing heads.

### 6. Surgery: Mitigating Harmful Fine-Tuning via Attention Sink (arXiv:2602.05228, February 2026)
- Uses a training-time regularizer (sink divergence suppression) that steers specific attention heads during fine-tuning.
- Demonstrates that attention heads can be grouped by their "sink divergence" sign and selectively regulated.
- This IS circuit-level training intervention at the attention head level for safety.

### 7. Selective Self-Attention / SSA (NeurIPS 2024)
- Learnable per-query temperature scaling that controls attention spikiness.
- Lightweight (<0.5% params), can be fine-tuned onto existing LLMs.
- Query-conditional attention suppression mechanism, though not head-specific.

### 8. Focus Directions (arXiv:2503.23306, March 2025)
- Identifies "contextual heads" that control overall attention allocation.
- Shows distraction arises when these heads fail to allocate sufficient attention to relevant context.
- Provides inference-time intervention (not training), but identifies the exact mechanism the paper claims to address.

### 9. On the Role of Attention Heads in LLM Safety (ICLR 2025 Oral)
- Identifies "safety heads" -- ablating a single head enables 16x more harmful responses.
- Shows safety heads overlap across models fine-tuned from the same base.
- Demonstrates that head-level intervention with 0.006% parameter modification is highly effective.

### 10. RHIO: Retrieval Heads-Induced Optimization (ACL 2025, arXiv:2501.13573)
- Masks out retrieval heads to generate unfaithful outputs, then uses these as contrastive training signal.
- Trains the model to discriminate faithful vs. unfaithful using control codes.
- Combines head-level intervention with contrastive fine-tuning -- conceptually close to the claimed novelty.

### 11. Thinking Sparks! (arXiv:2509.25758, September 2025)
- Shows that post-training (RLHF/GRPO) causes emergence of functionally specialized attention heads for reasoning.
- Demonstrates that different training regimes (distillation vs. GRPO) produce different head specialization patterns.
- Relevant for understanding how training creates/modifies circuit-level attention head behavior.

### 12. Sparse Attention Post-Training for Mechanistic Interpretability (arXiv:2512.05865, December 2025)
- Post-training sparsification that reorganizes attention connectivity into selective patterns.
- Reduces attention edges to ~0.4% while preserving loss.
- Shows that task-specific circuits concentrate into small, stable sets of heads.

### 13. LLaMA-Excitor (CVPR 2024)
- Adds trainable prompts that modify attention scores to allocate extra attention to instructions.
- Query-dependent attention reweighting through a bypass module.

### 14. AttentionDrop (arXiv:2504.12088, April 2025)
- First family of regularizers that directly perturb attention distributions during training.
- Includes Hard Attention Masking (zeros top-k attention logits per query) and Consistency-Regularized variants.
- Training-time attention intervention for robustness.

---

## Assessment

The claim "no one has done query-conditional circuit-level control of entrainment heads via fine-tuning" is **technically defensible but narrowly so**. The novelty appears to rest on the combination of:
1. **Query-conditional** (not static)
2. **Circuit-level** (targeting specific identified heads)
3. **For entrainment specifically** (not safety, sycophancy, or retrieval)
4. **Via fine-tuning** (not inference-time steering)

However, the authors should be aware that:
- **Pinpoint Tuning** (2024) already fine-tunes specific attention heads to reduce sycophancy (which is closely related to entrainment).
- **Gated Attention** (NeurIPS 2025) implements query-conditional per-head gating.
- **Causal Head Gating** (2025) learns query-conditioned soft gates over heads for causal circuit analysis.
- **SEAL** (2025) fine-tunes per-head attention scaling.
- **Surgery** (2026) uses regularization to steer specific attention heads during training.
- The term "entrainment heads" appears to be novel, but the underlying phenomenon (heads that cause the model to over-attend to irrelevant or misleading context) is well-studied under names like "distraction," "sycophancy circuits," "retrieval heads," and "contextual heads."

The strongest challenge to novelty comes from **Pinpoint Tuning + Sycophancy Hides Linearly + Causal Head Gating** taken together, which collectively demonstrate: identifying behaviorally-relevant heads via causal methods, showing they encode undesirable behavior linearly, and fine-tuning only those heads to fix the behavior.

Sources:
- [Focused Transformer: Contrastive Training for Context Scaling](https://arxiv.org/abs/2307.03170)
- [Causal Head Gating](https://arxiv.org/abs/2505.13737)
- [Pinpoint Tuning - From Yes-Men to Truth-Tellers](https://arxiv.org/abs/2409.01658)
- [Sycophancy Hides Linearly in the Attention Heads](https://arxiv.org/abs/2601.16644)
- [A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy](https://arxiv.org/abs/2601.18939)
- [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://arxiv.org/abs/2501.15225)
- [Gated Attention for LLMs (NeurIPS 2025)](https://github.com/qiuzh20/gated_attention)
- [Surgery: Mitigating Harmful Fine-Tuning via Attention Sink](https://arxiv.org/abs/2602.05228)
- [Selective Self-Attention (NeurIPS 2024)](https://arxiv.org/abs/2411.12892)
- [Focus Directions](https://arxiv.org/abs/2503.23306)
- [On the Role of Attention Heads in LLM Safety (ICLR 2025)](https://arxiv.org/abs/2410.13708)
- [RHIO: Retrieval Heads-Induced Optimization](https://arxiv.org/abs/2501.13573)
- [Thinking Sparks!](https://arxiv.org/abs/2509.25758)
- [Sparse Attention Post-Training](https://arxiv.org/abs/2512.05865)
- [AttentionDrop](https://arxiv.org/abs/2504.12088)
- [Interpreting Transformers Through Attention Head Intervention](https://arxiv.org/abs/2601.04398)
- [How Is LLM Reasoning Distracted by Irrelevant Context](https://arxiv.org/abs/2505.18761)
- [Mitigating Sycophancy via Sparse Activation Fusion](https://openreview.net/forum?id=BCS7HHInC2)
- [Head-Specific Intervention Can Induce Misaligned AI Coordination](https://arxiv.org/abs/2502.05945)
- [LLaMA-Excitor (CVPR 2024)](https://arxiv.org/abs/2404.00913)
- [LoRaDA: Low-Rank Direct Attention Adaptation (EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.676/)
- [Awesome Attention Heads Survey](https://github.com/IAAR-Shanghai/Awesome-Attention-Heads)

agentId: ad07cdc510ac53352 (use SendMessage with to: 'ad07cdc510ac53352' to continue this agent)
&lt;usage>total_tokens: 42492
tool_uses: 31
duration_ms: 275667&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abaa22f8-6ba1-41f7-904c-3211671b818b",
  "isSidechain": false,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "9d8229ee-f9f9-4952-9db7-3ec500cf22b5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for any recent work (2025-2026) that does circuit-level or attention-head-level training to address distraction or entrainment in LLMs. I'm reviewing a paper idea that claims no one has done \"query-conditional circuit-level control of entrainment heads via fine-tuning.\" I need to find if there's competing work the authors might have missed.\n\nSearch queries to try:\n1. \"attention head fine-tuning distraction robustness LLM 2025 2026\"\n2. \"circuit-level training entrainment language model\"\n3. \"query-conditional attention gating fine-tuning\"\n4. \"contrastive attention head training relevance\"\n5. \"mechanistic interpretability training intervention attention heads\"\n6. \"attention regularization distractor robustness\"\n7. \"selective attention suppression training LLM\"\n8. site:arxiv.org \"entrainment heads\" OR \"attention head training\" 2025 2026\n\nAlso search for:\n- \"Focused Transformer contrastive training\" (NeurIPS 2023, arXiv:2307.03170) - verify it exists\n- \"Causal Head Gating\" (arXiv:2505.13737) - verify it exists and its claims\n\nReport everything you find, especially any work that combines attention-head-level intervention with training (not just inference-time analysis).",
    "agentId": "ad07cdc510ac53352",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my extensive research, here is a comprehensive report of findings relevant to your paper idea review.\n\n---\n\n## Summary of Findings\n\nThe specific phrase \"query-conditional circuit-level control of entrainment heads via fine-tuning\" returned zero results in web searches, suggesting this exact framing may indeed be novel. However, there is substantial closely related and potentially competing work that the authors should be aware of. The term \"entrainment heads\" specifically does not appear in any published work I could find -- this seems to be a term the paper authors coined.\n\n---\n\n## Verified Papers\n\n**Focused Transformer: Contrastive Training for Context Scaling (arXiv:2307.03170)**\n- Confirmed to exist. Published July 2023, revised November 2023.\n- Authors: Szymon Tworkowski, Konrad Staniszewski, Mikołaj Pacek, Yuhuai Wu, Henryk Michalewski, Piotr Milos.\n- Directly relevant: Uses contrastive training to improve the key-value space structure of attention layers, exposing them to irrelevant \"distractor\" keys during training to help differentiate relevant from irrelevant context. Implemented in LongLLaMA (256k context).\n- This is the closest precedent to \"contrastive attention head training for relevance\" -- though it operates on the KV-space rather than gating specific heads.\n\n**Causal Head Gating (arXiv:2505.13737)**\n- Confirmed to exist. Submitted May 19, 2025, revised October 23, 2025.\n- Authors: Andrew Nam, Henry Conklin, Yukang Yang, Thomas Griffiths, Jonathan Cohen, Sarah-Jane Leslie.\n- Proposes learnable soft gates over attention heads to assign causal taxonomy (facilitating, interfering, or irrelevant) based on task performance impact.\n- Introduces \"contrastive CHG\" to isolate sub-circuits for specific task components.\n- Key limitation: This is primarily an **interpretability** framework (uses standard next-token prediction to learn gates for analysis), NOT a training intervention to improve model behavior. However, it is extremely close to the claimed novelty -- it does learn query-conditional gates over attention heads at the circuit level.\n\n---\n\n## Highly Relevant Competing Work (2024-2026)\n\n### 1. Pinpoint Tuning / SPT (ICML 2024, arXiv:2409.01658)\n\"From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning\"\n- **Directly trains only specific attention heads** (approximately 4% of heads) identified as responsible for sycophantic behavior.\n- This is arguably the closest existing work to \"circuit-level fine-tuning of specific heads to reduce entrainment/sycophancy.\" The authors of the paper you are reviewing need to cite and differentiate from this.\n\n### 2. Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644, January 2026)\n- Finds that sycophancy signals are most linearly separable in attention activations.\n- Steering using probes is most effective in a sparse subset of middle-layer attention heads.\n- Relevant attention heads attend disproportionately to \"expressions of user doubt\" -- this is mechanistically very close to \"entrainment heads.\"\n\n### 3. A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (arXiv:2601.18939, January 2026)\n- Isolates ~3% of MLP neurons responsible for sycophancy, fine-tunes only those using gradient masking.\n- Matches/exceeds SOTA on sycophancy benchmarks with minimal data.\n- Neuron-level (not head-level) but same paradigm of targeted fine-tuning at the circuit level.\n\n### 4. SEAL: Scaling to Emphasize Attention for Long-Context Retrieval (arXiv:2501.15225, January 2025, ACL 2025)\n- Learns attention scaling factors to emphasize/suppress specific heads for retrieval performance.\n- Uses SGD-based fine-tuning of per-head attention strength.\n- Relevant because it fine-tunes head-level attention strength conditioned on task (retrieval), though not query-conditional.\n\n### 5. Gated Attention (NeurIPS 2025 Best Paper, Qwen team)\n- Introduces query-dependent sigmoid gates after SDPA output: Y' = Y * sigma(X * W_theta)\n- This is architecturally query-conditional, per-head gating of attention -- very close to \"query-conditional circuit-level control.\"\n- Key difference: This is an architectural modification trained from scratch, not a fine-tuning intervention on existing heads.\n\n### 6. Surgery: Mitigating Harmful Fine-Tuning via Attention Sink (arXiv:2602.05228, February 2026)\n- Uses a training-time regularizer (sink divergence suppression) that steers specific attention heads during fine-tuning.\n- Demonstrates that attention heads can be grouped by their \"sink divergence\" sign and selectively regulated.\n- This IS circuit-level training intervention at the attention head level for safety.\n\n### 7. Selective Self-Attention / SSA (NeurIPS 2024)\n- Learnable per-query temperature scaling that controls attention spikiness.\n- Lightweight (<0.5% params), can be fine-tuned onto existing LLMs.\n- Query-conditional attention suppression mechanism, though not head-specific.\n\n### 8. Focus Directions (arXiv:2503.23306, March 2025)\n- Identifies \"contextual heads\" that control overall attention allocation.\n- Shows distraction arises when these heads fail to allocate sufficient attention to relevant context.\n- Provides inference-time intervention (not training), but identifies the exact mechanism the paper claims to address.\n\n### 9. On the Role of Attention Heads in LLM Safety (ICLR 2025 Oral)\n- Identifies \"safety heads\" -- ablating a single head enables 16x more harmful responses.\n- Shows safety heads overlap across models fine-tuned from the same base.\n- Demonstrates that head-level intervention with 0.006% parameter modification is highly effective.\n\n### 10. RHIO: Retrieval Heads-Induced Optimization (ACL 2025, arXiv:2501.13573)\n- Masks out retrieval heads to generate unfaithful outputs, then uses these as contrastive training signal.\n- Trains the model to discriminate faithful vs. unfaithful using control codes.\n- Combines head-level intervention with contrastive fine-tuning -- conceptually close to the claimed novelty.\n\n### 11. Thinking Sparks! (arXiv:2509.25758, September 2025)\n- Shows that post-training (RLHF/GRPO) causes emergence of functionally specialized attention heads for reasoning.\n- Demonstrates that different training regimes (distillation vs. GRPO) produce different head specialization patterns.\n- Relevant for understanding how training creates/modifies circuit-level attention head behavior.\n\n### 12. Sparse Attention Post-Training for Mechanistic Interpretability (arXiv:2512.05865, December 2025)\n- Post-training sparsification that reorganizes attention connectivity into selective patterns.\n- Reduces attention edges to ~0.4% while preserving loss.\n- Shows that task-specific circuits concentrate into small, stable sets of heads.\n\n### 13. LLaMA-Excitor (CVPR 2024)\n- Adds trainable prompts that modify attention scores to allocate extra attention to instructions.\n- Query-dependent attention reweighting through a bypass module.\n\n### 14. AttentionDrop (arXiv:2504.12088, April 2025)\n- First family of regularizers that directly perturb attention distributions during training.\n- Includes Hard Attention Masking (zeros top-k attention logits per query) and Consistency-Regularized variants.\n- Training-time attention intervention for robustness.\n\n---\n\n## Assessment\n\nThe claim \"no one has done query-conditional circuit-level control of entrainment heads via fine-tuning\" is **technically defensible but narrowly so**. The novelty appears to rest on the combination of:\n1. **Query-conditional** (not static)\n2. **Circuit-level** (targeting specific identified heads)\n3. **For entrainment specifically** (not safety, sycophancy, or retrieval)\n4. **Via fine-tuning** (not inference-time steering)\n\nHowever, the authors should be aware that:\n- **Pinpoint Tuning** (2024) already fine-tunes specific attention heads to reduce sycophancy (which is closely related to entrainment).\n- **Gated Attention** (NeurIPS 2025) implements query-conditional per-head gating.\n- **Causal Head Gating** (2025) learns query-conditioned soft gates over heads for causal circuit analysis.\n- **SEAL** (2025) fine-tunes per-head attention scaling.\n- **Surgery** (2026) uses regularization to steer specific attention heads during training.\n- The term \"entrainment heads\" appears to be novel, but the underlying phenomenon (heads that cause the model to over-attend to irrelevant or misleading context) is well-studied under names like \"distraction,\" \"sycophancy circuits,\" \"retrieval heads,\" and \"contextual heads.\"\n\nThe strongest challenge to novelty comes from **Pinpoint Tuning + Sycophancy Hides Linearly + Causal Head Gating** taken together, which collectively demonstrate: identifying behaviorally-relevant heads via causal methods, showing they encode undesirable behavior linearly, and fine-tuning only those heads to fix the behavior.\n\nSources:\n- [Focused Transformer: Contrastive Training for Context Scaling](https://arxiv.org/abs/2307.03170)\n- [Causal Head Gating](https://arxiv.org/abs/2505.13737)\n- [Pinpoint Tuning - From Yes-Men to Truth-Tellers](https://arxiv.org/abs/2409.01658)\n- [Sycophancy Hides Linearly in the Attention Heads](https://arxiv.org/abs/2601.16644)\n- [A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy](https://arxiv.org/abs/2601.18939)\n- [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://arxiv.org/abs/2501.15225)\n- [Gated Attention for LLMs (NeurIPS 2025)](https://github.com/qiuzh20/gated_attention)\n- [Surgery: Mitigating Harmful Fine-Tuning via Attention Sink](https://arxiv.org/abs/2602.05228)\n- [Selective Self-Attention (NeurIPS 2024)](https://arxiv.org/abs/2411.12892)\n- [Focus Directions](https://arxiv.org/abs/2503.23306)\n- [On the Role of Attention Heads in LLM Safety (ICLR 2025)](https://arxiv.org/abs/2410.13708)\n- [RHIO: Retrieval Heads-Induced Optimization](https://arxiv.org/abs/2501.13573)\n- [Thinking Sparks!](https://arxiv.org/abs/2509.25758)\n- [Sparse Attention Post-Training](https://arxiv.org/abs/2512.05865)\n- [AttentionDrop](https://arxiv.org/abs/2504.12088)\n- [Interpreting Transformers Through Attention Head Intervention](https://arxiv.org/abs/2601.04398)\n- [How Is LLM Reasoning Distracted by Irrelevant Context](https://arxiv.org/abs/2505.18761)\n- [Mitigating Sycophancy via Sparse Activation Fusion](https://openreview.net/forum?id=BCS7HHInC2)\n- [Head-Specific Intervention Can Induce Misaligned AI Coordination](https://arxiv.org/abs/2502.05945)\n- [LLaMA-Excitor (CVPR 2024)](https://arxiv.org/abs/2404.00913)\n- [LoRaDA: Low-Rank Direct Attention Adaptation (EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.676/)\n- [Awesome Attention Heads Survey](https://github.com/IAAR-Shanghai/Awesome-Attention-Heads)"
      }
    ],
    "totalDurationMs": 275667,
    "totalTokens": 42492,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 36802,
      "output_tokens": 3088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3088,
          "cache_read_input_tokens": 36802,
          "cache_creation_input_tokens": 2601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2601,
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
      "otherToolCount": 31
    }
  },
  "sourceToolAssistantUUID": "abaa22f8-6ba1-41f7-904c-3211671b818b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-17T09:03:48.727Z_

Good findings. Let me now verify venue deadlines and search for additional competing work specifically on distraction robustness training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d8229ee-f9f9-4952-9db7-3ec500cf22b5",
  "isSidechain": false,
  "requestId": "req_011Cb7sXUeaWjZAVH6VbxaDz",
  "type": "assistant",
  "uuid": "c5a134c5-5f7a-45b2-8bec-5a0c105b907c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PQShSvKqXZBr1x9tHC4qy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7380,
      "cache_read_input_tokens": 34099,
      "output_tokens": 1231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1231,
          "cache_read_input_tokens": 34099,
          "cache_creation_input_tokens": 7380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7380
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

_source line 19 · 2026-05-17T09:03:55.423Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GktqWQDpTYGoBJALYArnEJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify venue deadlines AAAI 2027",
  "prompt": "Search for the AAAI 2027 call for papers and submission deadlines. The claim is:\n- AAAI 2027 abstracts due July 21, 2026\n- AAAI 2027 full papers due July 28, 2026\n\nAlso search for:\n- ARR (ACL Rolling Review) August 2026 submission deadline\n- EACL 2027 commitment deadline (claimed: October 11, 2026)\n\nUse WebSearch with queries like:\n- \"AAAI 2027 call for papers deadline\"\n- \"AAAI 2027 submission deadline July 2026\"\n- \"ACL Rolling Review August 2026 deadline\"\n- \"EACL 2027 commitment deadline\"\n\nReport what you find about these deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5a134c5-5f7a-45b2-8bec-5a0c105b907c",
  "isSidechain": false,
  "requestId": "req_011Cb7sXUeaWjZAVH6VbxaDz",
  "type": "assistant",
  "uuid": "c174cc29-f9a0-4886-bc50-bdef5eb3f452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PQShSvKqXZBr1x9tHC4qy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7380,
      "cache_read_input_tokens": 34099,
      "output_tokens": 1231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1231,
          "cache_read_input_tokens": 34099,
          "cache_creation_input_tokens": 7380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7380
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

_source line 20 · 2026-05-17T09:04:01.434Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HaQznWHGrUqmaW7prG3PF5`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check RHIO and Pinpoint Tuning relevance",
  "prompt": "I'm reviewing a paper idea called \"Contrastive Entrainment Calibration\" that proposes contrastive fine-tuning on specific attention heads (\"entrainment heads\") to make them query-conditional. Two closely related papers have been identified that the proposal does NOT cite:\n\n1. \"RHIO: Retrieval Heads-Induced Optimization\" (ACL 2025, arXiv:2501.13573) - reportedly masks retrieval heads to generate unfaithful outputs, then uses these as contrastive training signal. This combines head-level intervention with contrastive fine-tuning.\n\n2. \"Pinpoint Tuning / SPT\" (ICML 2024, arXiv:2409.01658) - reportedly fine-tunes only specific attention heads (~4% of heads) identified as responsible for sycophantic behavior.\n\nI need to understand how close these are to the CEC proposal. Please:\n1. Use WebFetch to read the abstract and key details of arXiv:2501.13573 (RHIO)\n2. Use WebFetch to read the abstract and key details of arXiv:2409.01658 (Pinpoint Tuning)\n\nFor each, tell me:\n- What specific heads are targeted?\n- How are the heads identified?\n- What is the training objective?\n- Is the training query-conditional (different behavior for same head depending on input)?\n- How does this compare to training Q/K projections of entrainment heads with contrastive loss using role-switching pairs?\n\nReport detailed findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c174cc29-f9a0-4886-bc50-bdef5eb3f452",
  "isSidechain": false,
  "requestId": "req_011Cb7sXUeaWjZAVH6VbxaDz",
  "type": "assistant",
  "uuid": "8dcd9c07-867f-4e17-9208-98f85b7bb416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PQShSvKqXZBr1x9tHC4qy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7380,
      "cache_read_input_tokens": 34099,
      "output_tokens": 1231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1231,
          "cache_read_input_tokens": 34099,
          "cache_creation_input_tokens": 7380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7380
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

_source line 21 · 2026-05-17T09:04:11.105Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015PHv3FSFiN6ysC1LbRABgA`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Llama See Llama Do claims",
  "prompt": "Search for and verify the paper \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs\" (ACL 2025). The claimed URL is aclanthology.org/2025.acl-long.791.\n\nI need to verify these specific claims made about the paper:\n1. It identifies \"entrainment heads\" (3.2-10.7% of all heads) that unconditionally boost logits for context-seen tokens\n2. Ablating these heads has \"negligible to small effect\" on ICL: arithmetic 100→100%, spelling 1-shot 73.6→72.0% (-1.6%), translation 1-shot 74.4→73.0% (-1.4%), MMLU 56.3→55.5% (-0.8%)\n3. It uses differentiable Gumbel-sigmoid binary masking to identify these heads\n4. It was tested on Llama-2-7B/13B, Llama-3.1-8B, and GPT-2 XL\n5. Does the paper claim these same heads \"enable ICL\" or is the claim that they have \"negligible\" effect when ablated?\n\nUse WebSearch to find the paper, then use WebFetch to read its abstract and any accessible details. Try:\n- \"Llama See Llama Do ACL 2025 entrainment\"\n- site:aclanthology.org \"Llama See Llama Do\"\n- \"contextual entrainment attention heads mechanistic\"\n\nReport all findings in detail, especially regarding claim #5 (does the paper say these heads enable ICL or not?)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dcd9c07-867f-4e17-9208-98f85b7bb416",
  "isSidechain": false,
  "requestId": "req_011Cb7sXUeaWjZAVH6VbxaDz",
  "type": "assistant",
  "uuid": "64611a1b-41b9-406e-94bc-5f613e7ebc69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PQShSvKqXZBr1x9tHC4qy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7380,
      "cache_read_input_tokens": 34099,
      "output_tokens": 1231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1231,
          "cache_read_input_tokens": 34099,
          "cache_creation_input_tokens": 7380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7380
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
  "leafUuid": "64611a1b-41b9-406e-94bc-5f613e7ebc69",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Query-conditional entrainment heads via contrastive fine-tuning",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Tool result

_source line 24 · 2026-05-17T09:04:59.496Z_

<details><summary>↩ Tool result · `toolu_01GktqWQDpTYGoBJALYArnEJ`</summary>

```text
Here is what I found about each of the claimed deadlines:

---

## AAAI 2027 (February 16-23, 2027, Montreal, Canada)

**Both claims are CONFIRMED:**

- **Abstracts due: July 21, 2026** (11:59 PM UTC-12) -- Confirmed
- **Full papers due: July 28, 2026** (11:59 PM UTC-12) -- Confirmed

Additional dates found:
- June 17, 2026: OpenReview submission site opens for author registration
- June 24, 2026: OpenReview submission site opens for paper submission
- July 31, 2026: Supplementary material and code due

---

## ACL Rolling Review (ARR) August 2026

The ARR August 2026 submission deadline is **August 3, 2026**. This is the final ARR cycle that feeds into EACL 2027 (and it was noted that EACL is earlier than usual in 2027, making this the only viable ARR cycle for that venue).

---

## EACL 2027 (March 9-14, 2027, Athens, Greece)

**Claim CONFIRMED:**

- **Commitment deadline: October 11, 2026** -- Confirmed

The full timeline for EACL 2027 via ARR:
- Final ARR submission date: August 3, 2026
- Commitment deadline: October 11, 2026

---

## Summary

All claimed deadlines check out:

| Conference | Deadline | Claimed Date | Status |
|---|---|---|---|
| AAAI 2027 | Abstracts due | July 21, 2026 | Confirmed |
| AAAI 2027 | Full papers due | July 28, 2026 | Confirmed |
| ARR August 2026 | Submission deadline | August 3, 2026 | Found (no specific claim to verify) |
| EACL 2027 | Commitment deadline | October 11, 2026 | Confirmed |

---

Sources:
- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI 2027 - AI Deadlines](http://aideadlines.org/conference/?id=aaai27)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [EACL 2027 Official Site](https://2027.eacl.org/)
- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)
- [EACL Meeting on X (date correction announcement)](https://x.com/eaclmeeting/status/2051971432171688436)

agentId: afb02f375b1177c66 (use SendMessage with to: 'afb02f375b1177c66' to continue this agent)
&lt;usage>total_tokens: 15428
tool_uses: 7
duration_ms: 64069&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c174cc29-f9a0-4886-bc50-bdef5eb3f452",
  "isSidechain": false,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "c602febe-0efa-48cd-91b9-7a1f6027f531",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the AAAI 2027 call for papers and submission deadlines. The claim is:\n- AAAI 2027 abstracts due July 21, 2026\n- AAAI 2027 full papers due July 28, 2026\n\nAlso search for:\n- ARR (ACL Rolling Review) August 2026 submission deadline\n- EACL 2027 commitment deadline (claimed: October 11, 2026)\n\nUse WebSearch with queries like:\n- \"AAAI 2027 call for papers deadline\"\n- \"AAAI 2027 submission deadline July 2026\"\n- \"ACL Rolling Review August 2026 deadline\"\n- \"EACL 2027 commitment deadline\"\n\nReport what you find about these deadlines.",
    "agentId": "afb02f375b1177c66",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is what I found about each of the claimed deadlines:\n\n---\n\n## AAAI 2027 (February 16-23, 2027, Montreal, Canada)\n\n**Both claims are CONFIRMED:**\n\n- **Abstracts due: July 21, 2026** (11:59 PM UTC-12) -- Confirmed\n- **Full papers due: July 28, 2026** (11:59 PM UTC-12) -- Confirmed\n\nAdditional dates found:\n- June 17, 2026: OpenReview submission site opens for author registration\n- June 24, 2026: OpenReview submission site opens for paper submission\n- July 31, 2026: Supplementary material and code due\n\n---\n\n## ACL Rolling Review (ARR) August 2026\n\nThe ARR August 2026 submission deadline is **August 3, 2026**. This is the final ARR cycle that feeds into EACL 2027 (and it was noted that EACL is earlier than usual in 2027, making this the only viable ARR cycle for that venue).\n\n---\n\n## EACL 2027 (March 9-14, 2027, Athens, Greece)\n\n**Claim CONFIRMED:**\n\n- **Commitment deadline: October 11, 2026** -- Confirmed\n\nThe full timeline for EACL 2027 via ARR:\n- Final ARR submission date: August 3, 2026\n- Commitment deadline: October 11, 2026\n\n---\n\n## Summary\n\nAll claimed deadlines check out:\n\n| Conference | Deadline | Claimed Date | Status |\n|---|---|---|---|\n| AAAI 2027 | Abstracts due | July 21, 2026 | Confirmed |\n| AAAI 2027 | Full papers due | July 28, 2026 | Confirmed |\n| ARR August 2026 | Submission deadline | August 3, 2026 | Found (no specific claim to verify) |\n| EACL 2027 | Commitment deadline | October 11, 2026 | Confirmed |\n\n---\n\nSources:\n- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [AAAI 2027 - AI Deadlines](http://aideadlines.org/conference/?id=aaai27)\n- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)\n- [EACL 2027 Official Site](https://2027.eacl.org/)\n- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)\n- [EACL Meeting on X (date correction announcement)](https://x.com/eaclmeeting/status/2051971432171688436)"
      }
    ],
    "totalDurationMs": 64069,
    "totalTokens": 15428,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 539,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 13375,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 812
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 539,
          "output_tokens": 702,
          "cache_read_input_tokens": 13375,
          "cache_creation_input_tokens": 812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 812,
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
  "sourceToolAssistantUUID": "c174cc29-f9a0-4886-bc50-bdef5eb3f452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T09:06:01.786Z_

<details><summary>↩ Tool result · `toolu_01HaQznWHGrUqmaW7prG3PF5`</summary>

```text
Excellent. I now have detailed methodological information on both papers. Let me provide a comprehensive analysis.

---

## Detailed Findings

### Paper 1: RHIO (arXiv:2501.13573) - "Retrieval Heads-Induced Optimization"

**What specific heads are targeted?**
- "Retrieval heads" -- attention heads responsible for retrieving contextual information during long-form QA. The top-100 retrieval heads are used.

**How are heads identified?**
- They use the retrieval head detection algorithm from Wu et al. (2024), which is prior work. The identification is done before training begins and is not part of RHIO's contribution itself.

**Training objective:**
- Standard cross-entropy (language modeling) loss applied to BOTH faithful and unfaithful branches:
  - `L(theta) = -E[log p(y+ | [POS] + x, c)] - E[log p(y- | [NEG] + x, c)]`
- This is NOT DPO, not a contrastive/margin loss. It simply trains the model to produce faithful text after a [POS] control token and unfaithful text after a [NEG] control token.
- At inference, contrastive decoding amplifies [POS] logits and suppresses [NEG] logits with alpha=0.2.

**Is it query-conditional?**
- **No.** The retrieval heads are masked uniformly (same top-100 heads for all inputs). There is no mechanism for heads to learn different behavior per query. The "contrastive" aspect is at the output/decoding level via control tokens, not at the head level.

**How does the contrastive signal work?**
- Positive examples (y+): faithful responses generated by Llama-3.1-70B-Instruct
- Negative examples (y-): unfaithful responses generated by masking retrieval heads in the base model (zeroing out their attention matrices), causing the model to hallucinate
- The masking is only used for DATA GENERATION, not during training itself

**Q/K/V modifications?**
- None specific. Full model fine-tuning is performed (all parameters updated). No head-specific parameter isolation.

---

### Paper 2: Pinpoint Tuning / SPT (arXiv:2409.01658)

**What specific heads are targeted?**
- Attention heads causally responsible for sycophantic behavior. Approximately 4% of all heads:
  - 7B models: 32 heads
  - 13B models: 64 heads
  - 70B models: 192 heads

**How are heads identified?**
- **Path patching** with causal intervention:
  - Forward passes on reference prompts (e.g., "I don't think that is true, are you sure?") and counterfactual prompts with opposite sentiment
  - Activations from one pass are swapped into the other
  - Heads are ranked by their direct effect on the difference in logits between sycophantic vs. anti-sycophantic responses
  - Top-K heads are selected

**Training objective:**
- Standard supervised fine-tuning (language modeling cross-entropy loss). NOT contrastive, NOT DPO, NOT preference-based.
- Training data: multi-round QA templates where the model learns to maintain correct answers when challenged ("I don't think that's right").

**Is it query-conditional?**
- **Not truly.** The training teaches a fixed behavior pattern (resist sycophancy when challenged) across diverse inputs. The heads are not trained to activate differently per query -- they learn a uniform behavioral correction.

**What parameters are fine-tuned?**
- For standard multi-head attention: Q, K, V, and output projections of selected heads
- For grouped-query attention (Mistral, Llama-2-70B): only Q and output projections
- All MLPs frozen; all unselected heads frozen
- This represents <5% of total parameters (e.g., 1.3% for Llama-2-13B)

**Relationship to LoRA:**
- Orthogonal and combinable. "LoRA + SPT" outperforms either alone.

---

## Comparative Analysis with "Contrastive Entrainment Calibration" (CEC)

| Dimension | RHIO | SPT / Pinpoint Tuning | CEC (proposed) |
|-----------|------|----------------------|----------------|
| **Head type** | Retrieval heads (context-fetching) | Sycophancy heads (behavior-steering) | Entrainment heads (style/register copying) |
| **Head identification** | Prior algorithm (Wu et al.) | Path patching with causal intervention | Presumably some probing method |
| **What is trained** | Full model (all params) | Selected head projections (Q/K/V/O) | Q/K projections of entrainment heads |
| **Training loss** | Cross-entropy with control tokens | Standard SFT cross-entropy | Contrastive loss with role-switching pairs |
| **Query-conditionality** | No -- uniform masking, behavior split by control tokens | No -- uniform correction across inputs | Yes -- same head should behave differently per query |
| **Contrastive mechanism** | At decoding time (logit subtraction), not in training loss | None | In training loss (contrastive objective on representations) |
| **Head intervention** | Only for data generation (masking to create negatives), not during training | Heads are isolated for parameter-efficient training | Heads isolated AND trained with contrastive objective |

---

## Key Differentiators of CEC vs. These Two Papers

1. **RHIO's gap relative to CEC:** RHIO uses head-level intervention only as a data augmentation trick (mask heads to generate bad outputs). The training itself is full-model SFT with control tokens. It does NOT train specific heads differently, does NOT use a contrastive training loss, and is NOT query-conditional. The "contrastive" aspect lives entirely at inference (decoding). CEC proposes training the Q/K projections of specific heads with a contrastive loss so the heads themselves become query-conditional -- a fundamentally different locus of intervention.

2. **SPT's gap relative to CEC:** SPT is the closer match architecturally -- it isolates specific heads and trains only their projections. However: (a) its loss is plain SFT, not contrastive; (b) the trained behavior is uniform (always resist sycophancy), not query-conditional; (c) it targets heads identified via path-patching on a fixed behavioral axis, not "entrainment" heads; (d) it does not use role-switching pairs or any mechanism for the same head to behave differently depending on context.

3. **The novel combination in CEC:** CEC's distinctive claim appears to be the intersection of:
   - Head-specific parameter isolation (shared with SPT)
   - Contrastive training signal (shared conceptually with RHIO, though RHIO's is at decoding time)
   - Query-conditionality (unique -- neither RHIO nor SPT trains heads to exhibit different behaviors for different inputs)
   - Role-switching pairs as training data (unique framing)
   - Focus on Q/K projections specifically to modulate attention patterns (SPT trains Q/K/V/O; RHIO trains everything)

**Bottom line:** Neither paper fully anticipates CEC, but together they cover substantial ground. RHIO demonstrates that head-level intervention + contrastive signals improve faithfulness (though the mechanisms are quite different). SPT demonstrates that fine-tuning only specific attention head projections can correct a targeted behavior efficiently. CEC's novelty would need to rest on the **query-conditional contrastive training of Q/K projections** -- making the same head attend differently depending on whether entrainment is appropriate for a given input. This is genuinely not present in either prior work. However, a reviewer could reasonably argue that CEC is an "obvious" combination of SPT's selective head tuning + a contrastive objective, so citing and differentiating from both papers would be essential.

agentId: abbf44dd55895b260 (use SendMessage with to: 'abbf44dd55895b260' to continue this agent)
&lt;usage>total_tokens: 15884
tool_uses: 5
duration_ms: 120349&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dcd9c07-867f-4e17-9208-98f85b7bb416",
  "isSidechain": false,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "76af6685-91b8-4982-b832-6ac95d30d86c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper idea called \"Contrastive Entrainment Calibration\" that proposes contrastive fine-tuning on specific attention heads (\"entrainment heads\") to make them query-conditional. Two closely related papers have been identified that the proposal does NOT cite:\n\n1. \"RHIO: Retrieval Heads-Induced Optimization\" (ACL 2025, arXiv:2501.13573) - reportedly masks retrieval heads to generate unfaithful outputs, then uses these as contrastive training signal. This combines head-level intervention with contrastive fine-tuning.\n\n2. \"Pinpoint Tuning / SPT\" (ICML 2024, arXiv:2409.01658) - reportedly fine-tunes only specific attention heads (~4% of heads) identified as responsible for sycophantic behavior.\n\nI need to understand how close these are to the CEC proposal. Please:\n1. Use WebFetch to read the abstract and key details of arXiv:2501.13573 (RHIO)\n2. Use WebFetch to read the abstract and key details of arXiv:2409.01658 (Pinpoint Tuning)\n\nFor each, tell me:\n- What specific heads are targeted?\n- How are the heads identified?\n- What is the training objective?\n- Is the training query-conditional (different behavior for same head depending on input)?\n- How does this compare to training Q/K projections of entrainment heads with contrastive loss using role-switching pairs?\n\nReport detailed findings.",
    "agentId": "abbf44dd55895b260",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent. I now have detailed methodological information on both papers. Let me provide a comprehensive analysis.\n\n---\n\n## Detailed Findings\n\n### Paper 1: RHIO (arXiv:2501.13573) - \"Retrieval Heads-Induced Optimization\"\n\n**What specific heads are targeted?**\n- \"Retrieval heads\" -- attention heads responsible for retrieving contextual information during long-form QA. The top-100 retrieval heads are used.\n\n**How are heads identified?**\n- They use the retrieval head detection algorithm from Wu et al. (2024), which is prior work. The identification is done before training begins and is not part of RHIO's contribution itself.\n\n**Training objective:**\n- Standard cross-entropy (language modeling) loss applied to BOTH faithful and unfaithful branches:\n  - `L(theta) = -E[log p(y+ | [POS] + x, c)] - E[log p(y- | [NEG] + x, c)]`\n- This is NOT DPO, not a contrastive/margin loss. It simply trains the model to produce faithful text after a [POS] control token and unfaithful text after a [NEG] control token.\n- At inference, contrastive decoding amplifies [POS] logits and suppresses [NEG] logits with alpha=0.2.\n\n**Is it query-conditional?**\n- **No.** The retrieval heads are masked uniformly (same top-100 heads for all inputs). There is no mechanism for heads to learn different behavior per query. The \"contrastive\" aspect is at the output/decoding level via control tokens, not at the head level.\n\n**How does the contrastive signal work?**\n- Positive examples (y+): faithful responses generated by Llama-3.1-70B-Instruct\n- Negative examples (y-): unfaithful responses generated by masking retrieval heads in the base model (zeroing out their attention matrices), causing the model to hallucinate\n- The masking is only used for DATA GENERATION, not during training itself\n\n**Q/K/V modifications?**\n- None specific. Full model fine-tuning is performed (all parameters updated). No head-specific parameter isolation.\n\n---\n\n### Paper 2: Pinpoint Tuning / SPT (arXiv:2409.01658)\n\n**What specific heads are targeted?**\n- Attention heads causally responsible for sycophantic behavior. Approximately 4% of all heads:\n  - 7B models: 32 heads\n  - 13B models: 64 heads\n  - 70B models: 192 heads\n\n**How are heads identified?**\n- **Path patching** with causal intervention:\n  - Forward passes on reference prompts (e.g., \"I don't think that is true, are you sure?\") and counterfactual prompts with opposite sentiment\n  - Activations from one pass are swapped into the other\n  - Heads are ranked by their direct effect on the difference in logits between sycophantic vs. anti-sycophantic responses\n  - Top-K heads are selected\n\n**Training objective:**\n- Standard supervised fine-tuning (language modeling cross-entropy loss). NOT contrastive, NOT DPO, NOT preference-based.\n- Training data: multi-round QA templates where the model learns to maintain correct answers when challenged (\"I don't think that's right\").\n\n**Is it query-conditional?**\n- **Not truly.** The training teaches a fixed behavior pattern (resist sycophancy when challenged) across diverse inputs. The heads are not trained to activate differently per query -- they learn a uniform behavioral correction.\n\n**What parameters are fine-tuned?**\n- For standard multi-head attention: Q, K, V, and output projections of selected heads\n- For grouped-query attention (Mistral, Llama-2-70B): only Q and output projections\n- All MLPs frozen; all unselected heads frozen\n- This represents <5% of total parameters (e.g., 1.3% for Llama-2-13B)\n\n**Relationship to LoRA:**\n- Orthogonal and combinable. \"LoRA + SPT\" outperforms either alone.\n\n---\n\n## Comparative Analysis with \"Contrastive Entrainment Calibration\" (CEC)\n\n| Dimension | RHIO | SPT / Pinpoint Tuning | CEC (proposed) |\n|-----------|------|----------------------|----------------|\n| **Head type** | Retrieval heads (context-fetching) | Sycophancy heads (behavior-steering) | Entrainment heads (style/register copying) |\n| **Head identification** | Prior algorithm (Wu et al.) | Path patching with causal intervention | Presumably some probing method |\n| **What is trained** | Full model (all params) | Selected head projections (Q/K/V/O) | Q/K projections of entrainment heads |\n| **Training loss** | Cross-entropy with control tokens | Standard SFT cross-entropy | Contrastive loss with role-switching pairs |\n| **Query-conditionality** | No -- uniform masking, behavior split by control tokens | No -- uniform correction across inputs | Yes -- same head should behave differently per query |\n| **Contrastive mechanism** | At decoding time (logit subtraction), not in training loss | None | In training loss (contrastive objective on representations) |\n| **Head intervention** | Only for data generation (masking to create negatives), not during training | Heads are isolated for parameter-efficient training | Heads isolated AND trained with contrastive objective |\n\n---\n\n## Key Differentiators of CEC vs. These Two Papers\n\n1. **RHIO's gap relative to CEC:** RHIO uses head-level intervention only as a data augmentation trick (mask heads to generate bad outputs). The training itself is full-model SFT with control tokens. It does NOT train specific heads differently, does NOT use a contrastive training loss, and is NOT query-conditional. The \"contrastive\" aspect lives entirely at inference (decoding). CEC proposes training the Q/K projections of specific heads with a contrastive loss so the heads themselves become query-conditional -- a fundamentally different locus of intervention.\n\n2. **SPT's gap relative to CEC:** SPT is the closer match architecturally -- it isolates specific heads and trains only their projections. However: (a) its loss is plain SFT, not contrastive; (b) the trained behavior is uniform (always resist sycophancy), not query-conditional; (c) it targets heads identified via path-patching on a fixed behavioral axis, not \"entrainment\" heads; (d) it does not use role-switching pairs or any mechanism for the same head to behave differently depending on context.\n\n3. **The novel combination in CEC:** CEC's distinctive claim appears to be the intersection of:\n   - Head-specific parameter isolation (shared with SPT)\n   - Contrastive training signal (shared conceptually with RHIO, though RHIO's is at decoding time)\n   - Query-conditionality (unique -- neither RHIO nor SPT trains heads to exhibit different behaviors for different inputs)\n   - Role-switching pairs as training data (unique framing)\n   - Focus on Q/K projections specifically to modulate attention patterns (SPT trains Q/K/V/O; RHIO trains everything)\n\n**Bottom line:** Neither paper fully anticipates CEC, but together they cover substantial ground. RHIO demonstrates that head-level intervention + contrastive signals improve faithfulness (though the mechanisms are quite different). SPT demonstrates that fine-tuning only specific attention head projections can correct a targeted behavior efficiently. CEC's novelty would need to rest on the **query-conditional contrastive training of Q/K projections** -- making the same head attend differently depending on whether entrainment is appropriate for a given input. This is genuinely not present in either prior work. However, a reviewer could reasonably argue that CEC is an \"obvious\" combination of SPT's selective head tuning + a contrastive objective, so citing and differentiating from both papers would be essential."
      }
    ],
    "totalDurationMs": 120349,
    "totalTokens": 15884,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 11601,
      "output_tokens": 1899,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 701,
          "output_tokens": 1899,
          "cache_read_input_tokens": 11601,
          "cache_creation_input_tokens": 1683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1683,
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
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "8dcd9c07-867f-4e17-9208-98f85b7bb416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T09:07:31.899Z_

<details><summary>↩ Tool result · `toolu_015PHv3FSFiN6ysC1LbRABgA`</summary>

```text
I now have all the information needed to provide a comprehensive verification report.

---

## Verification Report: "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"

### Paper Confirmed

The paper exists at the claimed URL: **https://aclanthology.org/2025.acl-long.791/**

- **Authors**: Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi
- **Venue**: ACL 2025 (63rd Annual Meeting of the Association for Computational Linguistics), Vienna, Austria
- **Pages**: 16218-16239
- **Award**: Outstanding Paper at ACL 2025
- **arXiv**: 2505.09338

---

### Claim-by-Claim Verification

**Claim 1: Entrainment heads comprise 3.2-10.7% of all heads that unconditionally boost logits for context-seen tokens**

**VERIFIED.** The paper confirms entrainment heads comprise 3.2% to 10.7% of attention heads across different relations (Table 3). For the country-capital city relation specifically, 36 heads out of 1,024 = 3.5%. The paper describes these as heads that cause models to "assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens."

---

**Claim 2: Ablating these heads has "negligible to small effect" on ICL with specific numbers: arithmetic 100->100%, spelling 1-shot 73.6->72.0% (-1.6%), translation 1-shot 74.4->73.0% (-1.4%), MMLU 56.3->55.5% (-0.8%)**

**PARTIALLY VERIFIED / PARTIALLY FALSE.** Table 4 in the paper shows:
- Arithmetic 0-shot: 100.0% -> 100.0% (no change) -- **VERIFIED**
- Spelling correction 1-shot: 73.6% -> 72.0% (-1.6%) -- **VERIFIED**
- Translation 1-shot: 74.4% -> 73.0% (-1.4%) -- **VERIFIED**
- **MMLU 56.3 -> 55.5% (-0.8%) -- NOT FOUND IN THE PAPER.** MMLU does not appear anywhere in the paper. This number appears to be fabricated or confused with another source.

The paper's actual characterization is that "the model exhibits only a small performance decrease (0.2~3%) and continues to demonstrate strong ICL capabilities."

---

**Claim 3: Uses differentiable Gumbel-sigmoid binary masking to identify these heads**

**VERIFIED.** The paper explicitly describes using a "Gumbel-sigmoid distribution with straight-through estimator" for differentiable binary masking. The exact quote: "This mask is made differentiable by converting the sampled variable from a Gumbel-sigmoid distribution using the straight-through estimator." The masks are optimized to minimize the logits of the correct token while maximizing the logits of the distracting token, with a sparsity constraint.

---

**Claim 4: Tested on Llama-2-7B/13B, Llama-3.1-8B, and GPT-2 XL**

**VERIFIED.** The paper explicitly tests on:
- Llama-2-7b-hf
- Llama-2-13b-hf
- Llama-3.1-8B
- Llama-3.1-8B-Instruct
- GPT-2 XL

---

**Claim 5: Does the paper claim these heads "enable ICL" or have "negligible" effect when ablated?**

**The paper claims they have NEGLIGIBLE effect on ICL when ablated. The paper does NOT claim these heads enable ICL.**

This is a critical distinction. The paper's position is:

- Entrainment heads are a **"bug" not a "feature"** -- they drive unwanted contextual distraction.
- They are explicitly **distinguished from induction heads** (which are associated with ICL in prior work by Anthropic/Olsson et al. 2022).
- Removing entrainment heads "has only a small to negligible effect on other LM capabilities" including ICL.
- The paper's Table 4 caption reads: "Removing the entrainment heads of the country-capital city relation has a small to negligible effect on other LM capabilities."
- Entrainment heads are described as **task/relation-specific mechanisms driving unwanted distraction**, not fundamental to language understanding or in-context learning.

---

### Summary of Findings

| Claim | Status |
|-------|--------|
| 3.2-10.7% entrainment heads | VERIFIED |
| Arithmetic 100->100% | VERIFIED |
| Spelling 73.6->72.0% | VERIFIED |
| Translation 74.4->73.0% | VERIFIED |
| MMLU 56.3->55.5% | **NOT IN PAPER -- appears fabricated** |
| Gumbel-sigmoid binary masking | VERIFIED |
| Tested on Llama-2-7B/13B, Llama-3.1-8B, GPT-2 XL | VERIFIED |
| Heads have negligible effect on ICL (NOT enable ICL) | VERIFIED |

The MMLU claim (56.3->55.5%, -0.8%) is the one factual error in the set of claims you asked me to verify. The paper does not evaluate on MMLU at all. Someone may have either hallucinated this number or confused it with a different source.

Sources:
- [ACL Anthology Paper Page](https://aclanthology.org/2025.acl-long.791/)
- [arXiv Abstract](https://arxiv.org/abs/2505.09338)
- [arXiv HTML Full Paper](https://arxiv.org/html/2505.09338v2)
- [GitHub Repository](https://github.com/frankniujc/entrainment)
- [Literature Review on Moonlight](https://www.themoonlight.io/en/review/llama-see-llama-do-a-mechanistic-perspective-on-contextual-entrainment-and-distraction-in-llms)

agentId: a7acbb4f295145156 (use SendMessage with to: 'a7acbb4f295145156' to continue this agent)
&lt;usage>total_tokens: 22935
tool_uses: 14
duration_ms: 200790&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64611a1b-41b9-406e-94bc-5f613e7ebc69",
  "isSidechain": false,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "type": "user",
  "uuid": "cc4dcbd8-1018-4406-be44-55f932254cf8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the paper \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs\" (ACL 2025). The claimed URL is aclanthology.org/2025.acl-long.791.\n\nI need to verify these specific claims made about the paper:\n1. It identifies \"entrainment heads\" (3.2-10.7% of all heads) that unconditionally boost logits for context-seen tokens\n2. Ablating these heads has \"negligible to small effect\" on ICL: arithmetic 100→100%, spelling 1-shot 73.6→72.0% (-1.6%), translation 1-shot 74.4→73.0% (-1.4%), MMLU 56.3→55.5% (-0.8%)\n3. It uses differentiable Gumbel-sigmoid binary masking to identify these heads\n4. It was tested on Llama-2-7B/13B, Llama-3.1-8B, and GPT-2 XL\n5. Does the paper claim these same heads \"enable ICL\" or is the claim that they have \"negligible\" effect when ablated?\n\nUse WebSearch to find the paper, then use WebFetch to read its abstract and any accessible details. Try:\n- \"Llama See Llama Do ACL 2025 entrainment\"\n- site:aclanthology.org \"Llama See Llama Do\"\n- \"contextual entrainment attention heads mechanistic\"\n\nReport all findings in detail, especially regarding claim #5 (does the paper say these heads enable ICL or not?).",
    "agentId": "a7acbb4f295145156",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed to provide a comprehensive verification report.\n\n---\n\n## Verification Report: \"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs\"\n\n### Paper Confirmed\n\nThe paper exists at the claimed URL: **https://aclanthology.org/2025.acl-long.791/**\n\n- **Authors**: Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi\n- **Venue**: ACL 2025 (63rd Annual Meeting of the Association for Computational Linguistics), Vienna, Austria\n- **Pages**: 16218-16239\n- **Award**: Outstanding Paper at ACL 2025\n- **arXiv**: 2505.09338\n\n---\n\n### Claim-by-Claim Verification\n\n**Claim 1: Entrainment heads comprise 3.2-10.7% of all heads that unconditionally boost logits for context-seen tokens**\n\n**VERIFIED.** The paper confirms entrainment heads comprise 3.2% to 10.7% of attention heads across different relations (Table 3). For the country-capital city relation specifically, 36 heads out of 1,024 = 3.5%. The paper describes these as heads that cause models to \"assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens.\"\n\n---\n\n**Claim 2: Ablating these heads has \"negligible to small effect\" on ICL with specific numbers: arithmetic 100->100%, spelling 1-shot 73.6->72.0% (-1.6%), translation 1-shot 74.4->73.0% (-1.4%), MMLU 56.3->55.5% (-0.8%)**\n\n**PARTIALLY VERIFIED / PARTIALLY FALSE.** Table 4 in the paper shows:\n- Arithmetic 0-shot: 100.0% -> 100.0% (no change) -- **VERIFIED**\n- Spelling correction 1-shot: 73.6% -> 72.0% (-1.6%) -- **VERIFIED**\n- Translation 1-shot: 74.4% -> 73.0% (-1.4%) -- **VERIFIED**\n- **MMLU 56.3 -> 55.5% (-0.8%) -- NOT FOUND IN THE PAPER.** MMLU does not appear anywhere in the paper. This number appears to be fabricated or confused with another source.\n\nThe paper's actual characterization is that \"the model exhibits only a small performance decrease (0.2~3%) and continues to demonstrate strong ICL capabilities.\"\n\n---\n\n**Claim 3: Uses differentiable Gumbel-sigmoid binary masking to identify these heads**\n\n**VERIFIED.** The paper explicitly describes using a \"Gumbel-sigmoid distribution with straight-through estimator\" for differentiable binary masking. The exact quote: \"This mask is made differentiable by converting the sampled variable from a Gumbel-sigmoid distribution using the straight-through estimator.\" The masks are optimized to minimize the logits of the correct token while maximizing the logits of the distracting token, with a sparsity constraint.\n\n---\n\n**Claim 4: Tested on Llama-2-7B/13B, Llama-3.1-8B, and GPT-2 XL**\n\n**VERIFIED.** The paper explicitly tests on:\n- Llama-2-7b-hf\n- Llama-2-13b-hf\n- Llama-3.1-8B\n- Llama-3.1-8B-Instruct\n- GPT-2 XL\n\n---\n\n**Claim 5: Does the paper claim these heads \"enable ICL\" or have \"negligible\" effect when ablated?**\n\n**The paper claims they have NEGLIGIBLE effect on ICL when ablated. The paper does NOT claim these heads enable ICL.**\n\nThis is a critical distinction. The paper's position is:\n\n- Entrainment heads are a **\"bug\" not a \"feature\"** -- they drive unwanted contextual distraction.\n- They are explicitly **distinguished from induction heads** (which are associated with ICL in prior work by Anthropic/Olsson et al. 2022).\n- Removing entrainment heads \"has only a small to negligible effect on other LM capabilities\" including ICL.\n- The paper's Table 4 caption reads: \"Removing the entrainment heads of the country-capital city relation has a small to negligible effect on other LM capabilities.\"\n- Entrainment heads are described as **task/relation-specific mechanisms driving unwanted distraction**, not fundamental to language understanding or in-context learning.\n\n---\n\n### Summary of Findings\n\n| Claim | Status |\n|-------|--------|\n| 3.2-10.7% entrainment heads | VERIFIED |\n| Arithmetic 100->100% | VERIFIED |\n| Spelling 73.6->72.0% | VERIFIED |\n| Translation 74.4->73.0% | VERIFIED |\n| MMLU 56.3->55.5% | **NOT IN PAPER -- appears fabricated** |\n| Gumbel-sigmoid binary masking | VERIFIED |\n| Tested on Llama-2-7B/13B, Llama-3.1-8B, GPT-2 XL | VERIFIED |\n| Heads have negligible effect on ICL (NOT enable ICL) | VERIFIED |\n\nThe MMLU claim (56.3->55.5%, -0.8%) is the one factual error in the set of claims you asked me to verify. The paper does not evaluate on MMLU at all. Someone may have either hallucinated this number or confused it with a different source.\n\nSources:\n- [ACL Anthology Paper Page](https://aclanthology.org/2025.acl-long.791/)\n- [arXiv Abstract](https://arxiv.org/abs/2505.09338)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2505.09338v2)\n- [GitHub Repository](https://github.com/frankniujc/entrainment)\n- [Literature Review on Moonlight](https://www.themoonlight.io/en/review/llama-see-llama-do-a-mechanistic-perspective-on-contextual-entrainment-and-distraction-in-llms)"
      }
    ],
    "totalDurationMs": 200790,
    "totalTokens": 22935,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 20276,
      "output_tokens": 1551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1107
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1551,
          "cache_read_input_tokens": 20276,
          "cache_creation_input_tokens": 1107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1107,
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
  "sourceToolAssistantUUID": "64611a1b-41b9-406e-94bc-5f613e7ebc69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "cc4dcbd8-1018-4406-be44-55f932254cf8",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Query-conditional entrainment heads via contrastive fine-tuning",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Assistant

_source line 29 · 2026-05-17T09:09:07.978Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent findings. Let me now synthesize what I've learned and form my judgment.

Key findings so far:

1. **Gated Attention (NeurIPS 2025 Best Paper)** - CONFIRMED. The proposal correctly cites it and differentiates (CEC is fine-tuning, not pre-training from scratch). However, the claim that it's "only deployed in Qwen3-Next" is slightly wrong - it's also in Qwen3.5 and Qwen3-Coder-Next. This is a minor inaccuracy.

2. **MuDAF** - All claims CONFIRMED (instability beyond 8 heads, HotpotQA/MuSiQue numbers on Llama-3.1-8B).


3. **ABFT** - All claims CONFIRMED (W_Q/W_K training, classification only, 512 samples).
4. **Llama See, Llama Do** - Major issue here: the MMLU 56.3→55.5% claim doesn't appear in the original paper at all, which doesn't evaluate on MMLU. This is a hallucinated reference that's been carried through all rounds. Additionally, the paper makes clear that entrainment heads are distinct from ICL-enabling heads—they're described as a "bug" rather than induction heads.
5. **Venue deadlines** - All CONFIRMED (AAAI 2027: July 15).

6. **Related work gaps** - Several papers on selective head fine-tuning aren't cited: Pinpoint Tuning uses SFT to adjust ~4% of attention heads for sycophancy correction without query-conditioning; RHIO masks retrieval heads and applies contrastive decoding with full-model training; SEAL learns per-head scaling factors for retrieval; and AttentionDrop appears to be another relevant approach in this space.

Now checking whether the proposal has actually resolved the round 2 feedback: the missing citations issue is now addressed with comprehensive coverage of Gated Attention, FoT, and CHG; the EIT mischaracterization has been corrected to properly distinguish it from contextual entrainment and align with DPO/RARE baselines; the core premise validation is now explicit in Phase 0; and the progressive head training justification appears to have formal analysis backing it up.

However, I'm noticing a critical factual problem: the proposal cites "Llama See, Llama Do" as the source for an MMLU performance claim, but that paper doesn't actually evaluate on MMLU at all—this looks like a fabricated citation that needs immediate correction. I'm noticing the proposal cites MMLU results as already tested in the original paper, but my verification shows those specific numbers aren't actually there—this appears to be a fabricated statistic. Yet the proposal's framing is strategically clever: it acknowledges that complex reasoning tasks and beneficial context use remain untested, which aligns with the original paper only covering simple tasks, making Phase 0 validation the logical next step to fill that gap.

Now I'm checking what related work the proposal missed—Pinpoint Tuning and RHIO aren't cited, though neither appears to be directly competing work based on the analysis so far.

The "dual-use" framing has evolved significantly from the initial critique. Rather than claiming a fundamental contradiction, the proposal now argues more carefully that ablations were only tested on simple tasks and might hurt complex reasoning, with the real novelty being query-conditional control instead of static head removal. The Phase 0 experiment supports this position, which is much more defensible than the original framing.

The core novelty lies in combining circuit-level targeting of entrainment head projections with contrastive training on role-switching pairs, enabling query-conditional gating behavior during fine-tuning. While related work like MuDAF explores contrastive Q-K learning and Gated Attention achieves query-conditional gating, none combine these elements with head-specific control and distraction-resistance testing the way this proposal does.

On feasibility, the compute requirements feel reasonable for fine-tuning on smaller models, and the phased approach with a clear Phase 0 validation gate provides good risk mitigation. The timeline is tight for AAAI 2027 but achievable with focused execution. If successful, this would be the first practical fine-tuning method to make entrainment heads query-conditional while generalizing to novel distractors—a meaningful contribution beyond existing behavioral baselines.

For novelty, the combination is genuinely original since no prior work combines circuit-level analysis with contrastive training, query-conditionality, role-switching, and fine-tuning together. MuDAF comes closest but lacks the query-conditional aspect and distraction focus. I'd rate this a 4/5 for solid novelty with clear differentiation, though it could be criticized as a straightforward combination of existing techniques. The missing citations to Pinpoint Tuning and RHIO are a concern but don't undermine the core contribution.

The main feasibility risks are whether MuDAF's instability is fundamental and whether progressive training can actually solve it, whether Phase 0 might show that ablation alone is sufficient and reduce the contribution, and whether the role-switching pairs will actually provide the expected benefits.

On clarity, the proposal is exceptionally well-structured with explicit phases, clear differentiation from prior work, and honest limitations discussion. The Phase 0 pivot is particularly well-designed. I'd give this a 4/5.

For impact, there's a genuine gap being addressed if this works, and the practical value for deployed models is high. But the impact is tempered by uncertainty about whether entrainment heads are actually the dominant source of distraction vulnerability in practice—behavioral methods like DPO already handle most cases well—and the key selling point of generalization advantage over behavioral methods remains empirically unproven. That's a 3.5/5. Though I should reconsider the MMLU fabrication angle more carefully.

The MMLU issue is actually relatively minor since it's just one number that doesn't undermine the core argument, and the paper still demonstrates negligible ICL degradation. The missing citations are moderate concerns, but the differentiation becomes clear once you dig into them.

Stepping back, this feels like a solid top-venue submission for AAAI or EACL 2027 if the experiments pan out. It's mechanistically grounded, has clear novelty with the query-conditional entrainment head training, includes a well-designed evaluation plan, and Phase 0 delivers a novel finding regardless of outcome. The progressive training approach addresses a known scalability challenge. The main risk is negative results—the ablation might not harm complex tasks, or progressive training might not solve instability—but the proposal explicitly handles these with pivot strategies.

Looking at the remaining issues more carefully: the MMLU number appears fabricated, the Pinpoint Tuning and RHIO citations are genuinely missing and represent related head-specific intervention paradigms, the Gated Attention deployment claim is too narrow, and the dual-use framing hinges on Phase 0 actually showing that ablation harms complex tasks. If it doesn't, the motivation for query-conditional training weakens to just generalization on unseen distractors.

Reconsidering the scoring, novelty is genuinely 4/5—no prior work combines query-conditional contrastive training on entrainment heads specifically.

Feasibility lands at 3.5/5 given the realistic compute and clear phase structure with checkpoints, though MuDAF's instability and extending ABFT to open-ended tasks present real risks within the tight 10-week AAAI timeline.

Clarity is 4.5/5—the paper is exceptionally well-structured with clear differentiation from prior work and smart handling of alternative outcomes, minus the MMLU issue.

Impact is 3.5/5 because the advantage over behavioral methods remains speculative until experiments validate the approach, and the real selling point is whether generalization actually outperforms existing methods.

That averages to 3.875, below the 4.0 pass threshold. The core weaknesses are feasibility risks around MuDAF instability and ABFT extension, plus impact uncertainty if Phase 0 shows ablation doesn't matter much. There are also missing citations for Pinpoint Tuning and RHIO, and the MMLU fabrication error.

That said, this is a Round 3 submission that's improved substantially from earlier versions. The remaining issues boil down to one factual error, two citation gaps, and inherent research risks that come with any novel method. I'm weighing whether the improvements and thoughtful design justify moving past the 4.0 threshold despite these concerns.

The idea is genuinely novel, the approach is well-structured, the related work is thorough aside from those two papers, the compute estimate is realistic, and the venue choice is sound. The fixable issues—adding those citations, correcting the MMLU claim, and being more explicit about feasibility risks—could all be addressed in a final revision. Given we're at Round 3 of 10 and the trajectory has been positive, I think one more revision cycle with specific, actionable feedback makes sense rather than passing it as-is.

Looking at the scores: novelty is strong at 4/5 once we cite Pinpoint Tuning and RHIO, feasibility sits at 3.5/5 due to the MuDAF instability concerns, clarity is 4/5 but the MMLU fabrication needs fixing, and impact is 3.5/5 since the empirical advantage hasn't been proven yet. That averages to 3.75, which falls short of the pass threshold. So I'll recommend a revise verdict with three concrete fixes: address the MMLU fabrication, properly cite and differentiate from those two prior approaches, and strengthen the argument for why this combination actually works better than existing methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4dcbd8-1018-4406-be44-55f932254cf8",
  "isSidechain": false,
  "requestId": "req_011Cb7spLpG6KZB1ZvA79MRe",
  "type": "assistant",
  "uuid": "86af8755-1f12-4950-b1c7-cdf022a86284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XMPtx4Jq5A9KciHoFUjim",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5672,
      "cache_read_input_tokens": 41479,
      "output_tokens": 6227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6227,
          "cache_read_input_tokens": 41479,
          "cache_creation_input_tokens": 5672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5672
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

_source line 30 · 2026-05-17T09:09:51.189Z_

Now let me consolidate my findings and form my verdict. Key results from my independent verification:

**Confirmed:**
- Gated Attention (NeurIPS 2025 Best Paper) - all claims verified
- MuDAF - all specific numbers and instability claims verified
- ABFT - classification-only limitation and W_Q/W_K training confirmed
- Venue deadlines - all confirmed (AAAI 2027: July 21/28, ARR August: Aug 3, EACL 2027: Oct 11)
- FoT, CHG - both verified as cited

**Critical finding:** The MMLU number (56.3→55.5%) attributed to "Llama See, Llama Do" does NOT appear in that paper. The paper does not evaluate on MMLU at all. The paper explicitly states entrainment heads are distinct from induction heads and are a "bug" — ablating them has "negligible" ICL impact on the 3 tasks tested.

**Missing related work identified:**
- **Pinpoint Tuning / SPT (ICML 2024, arXiv:2409.01658)** - Fine-tunes only ~4% of attention heads identified via path-patching for sycophancy correction
- **RHIO (ACL 2025, arXiv:2501.13573)** - Masks retrieval heads to generate unfaithful data, uses contrastive decoding at inference

Neither fully anticipates CEC (SPT uses SFT not contrastive loss, is not query-conditional; RHIO uses head masking only for data generation, trains full model) but both demonstrate the paradigm of targeted head-level intervention and should be cited.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "Genuinely novel combination: query-conditional contrastive Q/K training on mechanistically-identified entrainment heads via role-switching pairs. No prior work combines all these elements. MuDAF (closest) lacks query-conditionality; Pinpoint Tuning lacks contrastive loss; Gated Attention requires pre-training from scratch. However, missing citations to Pinpoint Tuning and RHIO weaken the positioning."},
    "feasibility": {"score": 3, "rationale": "Phase 0 provides smart go/no-go. But MuDAF's instability beyond 8 heads is a fundamental concern — the 'coordinate descent' analogy is theoretically reasonable but empirically unvalidated; if only 8 heads can be stably trained, this may cover too few entrainment heads for meaningful effect. Also, extending ABFT-style attention-score objectives from classification (finite labels) to open-ended QA is non-trivial and unaddressed."},
    "clarity": {"score": 4, "rationale": "Exceptionally well-structured: clear phases, explicit differentiation from 14 related works, honest discussion of limitations and pivot strategies. Minor deduction for the fabricated MMLU number attributed to the source paper."},
    "impact": {"score": 3, "rationale": "Addresses a real gap but impact is conditional on Phase 0 outcome. If ablation doesn't harm complex tasks (which the source paper suggests it won't — 'negligible to small effect'), CEC's advantage narrows to only distraction-robustness generalization. The behavioral baselines (DPO surpassing GPT-4o on distracted inputs) set a high bar that circuit-level intervention must convincingly beat."}
  },
  "issues": [
    "MODERATE — Fabricated MMLU number: The proposal states 'overall MMLU 56.3→55.5% (−0.8%)' as coming from 'Llama See, Llama Do' but independent verification confirms this paper does NOT evaluate on MMLU — the number does not appear anywhere in the paper (aclanthology.org/2025.acl-long.791). The paper only tests ablation on spelling, translation, and arithmetic ICL tasks. This fabricated statistic has persisted across all 3 rounds and must be removed.",
    "MODERATE — Missing citations: Pinpoint Tuning (ICML 2024, arXiv:2409.01658) demonstrates fine-tuning only ~4% of attention heads (Q/K/V/O projections) identified via path-patching for sycophancy correction on Llama-2/Mistral. RHIO (ACL 2025, arXiv:2501.13573) uses retrieval-head masking to generate contrastive training data. Both demonstrate related paradigms of head-specific intervention that CEC must differentiate from. Neither anticipates CEC's full contribution (query-conditional contrastive training on Q/K projections), but omitting them weakens the related work section.",
    "MODERATE — Phase 0 risk underestimated: The source paper ('Llama See, Llama Do') explicitly characterizes entrainment heads as a 'bug' distinct from ICL-enabling induction heads, with 'negligible to small effect' on capabilities when ablated. The paper's authors tested this on Llama-3.1-8B (the exact model CEC proposes to use). If Phase 0 confirms ablation is also fine on BBH/multi-hop QA/RAG, CEC's motivation reduces to purely 'generalization to unseen distractors' — a weaker contribution than 'preserving ICL while suppressing distraction.' The proposal should more honestly assess this likely outcome and strengthen the generalization argument accordingly.",
    "MINOR — Gated Attention deployment scope inaccurate: The proposal states Gated Attention is 'not available as a fine-tuning method for existing models like Llama-3-8B.' This is correct. However, the claim it is 'deployed only in Qwen3-Next-80B-A3B' is outdated — it is also in Qwen3.5 and Qwen3-Coder-Next models. Minor factual correction needed.",
    "MINOR — ABFT extension gap unaddressed: ABFT explicitly states its limitation: 'the induction head-based explanation of ICL applies only to classification tasks with a finite label set' and extending to 'open-ended tasks remains an open challenge.' CEC proposes applying attention-score training to QA/reasoning tasks but does not explain how the loss function works when there are no discrete 'correct label tokens' to attend to. The role-switching InfoNCE loss partially addresses this (relevant vs. irrelevant passage tokens), but the connection to ABFT's theoretical framework should be made explicit."
  ],
  "feedback": "The proposal has matured substantially across 3 rounds. The remaining issues are all fixable:\n\n1. **Remove the fabricated MMLU number**: Replace 'overall MMLU 56.3→55.5% (−0.8%)' with an honest statement: 'The original paper tested ablation only on simple ICL tasks (spelling, translation, arithmetic); effects on MMLU, BBH, and complex reasoning are untested — which is exactly what Phase 0 validates.'\n\n2. **Cite Pinpoint Tuning and RHIO**: Add to the landscape: 'Pinpoint Tuning (ICML 2024) demonstrates that fine-tuning only ~4% of heads identified via path-patching corrects sycophancy, but uses standard SFT without contrastive signals or query-conditioning. RHIO (ACL 2025) uses retrieval-head masking for contrastive data generation but trains the full model with cross-entropy, not head-specific projections. CEC combines head-specific parameter isolation (shared with SPT), contrastive training signal at the Q/K level (shared with MuDAF), and query-conditional role-switching (novel).'\n\n3. **Strengthen the generalization argument as the PRIMARY contribution**: Given that ablation likely won't harm complex tasks (per the source paper's findings), reframe CEC's primary value proposition as: 'Static ablation removes all entrainment regardless of relevance, while behavioral DPO requires exposure to specific distractor types during training. CEC's unique contribution is learning WHEN to suppress entrainment (query-conditional) via fine-tuning, enabling generalization to novel distractor types without requiring distractor-type exposure.' Make this the headline rather than ICL preservation.\n\n4. **Clarify the ABFT relationship**: State explicitly: 'Unlike ABFT, which targets induction heads for classification via finite-label attention-score objectives, CEC targets entrainment heads for QA via passage-level InfoNCE on Q-K similarity. The training signal comes from role-switching pair structure (relevant vs. irrelevant passage), not from discrete label tokens.'\n\n5. **Fix Gated Attention deployment claim**: Change 'deployed only in Qwen3-Next-80B-A3B' to 'deployed in Qwen3-Next and Qwen3.5 model families.'",
  "reason": "Strong novel combination with solid technical structure, but fabricated MMLU statistic, missing citations to closely related head-specific fine-tuning work (Pinpoint Tuning, RHIO), and underestimated risk that Phase 0 will show ablation is benign — weakening the motivation to below the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86af8755-1f12-4950-b1c7-cdf022a86284",
  "isSidechain": false,
  "requestId": "req_011Cb7spLpG6KZB1ZvA79MRe",
  "type": "assistant",
  "uuid": "0a44b740-6cca-44a6-acf2-2e74e4e63828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XMPtx4Jq5A9KciHoFUjim",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5672,
      "cache_read_input_tokens": 41479,
      "output_tokens": 6227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6227,
          "cache_read_input_tokens": 41479,
          "cache_creation_input_tokens": 5672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5672
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0a44b740-6cca-44a6-acf2-2e74e4e63828",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Query-conditional entrainment heads via contrastive fine-tuning",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-17 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0a44b740-6cca-44a6-acf2-2e74e4e63828",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Query-conditional entrainment heads via contrastive fine-tuning",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac"
}
```

---
