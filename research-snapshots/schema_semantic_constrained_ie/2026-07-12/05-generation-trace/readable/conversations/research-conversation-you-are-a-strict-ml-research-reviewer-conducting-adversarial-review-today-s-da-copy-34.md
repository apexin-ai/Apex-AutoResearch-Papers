# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/7543766e-83be-44bc-b006-4c1b2c7a9b11.jsonl`
- **Structured JSON:** [`922c182e30a97ffd89ac.json`](../../sessions/92/922c182e30a97ffd89ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:06:58.086Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:06:58.086Z",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Online Schema Adaptation via Extraction-Error Feedback Loops\",\n  \"core_problem\": \"Schema-guided IE models (GoLLIE, KnowCoder, GuideX) fix the extraction schema at training or deployment time. When a new domain has a schema that partially conflicts with training-time guidelines — e.g., a medical ontology where 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure', or a legal corpus where 'Organization' granularity differs from the training ontology — models fail silently with no mechanism to refine their operational schema. This is a *schema-ontology mismatch* problem: the set of types and their definitional boundaries in the target domain do not correspond to the types the model was trained to extract. It is distinct from the annotation instruction clarity problem, which concerns surface wording of fixed type definitions. How can IE models detect and recover from schema-ontology mismatches at test time without gold labels, multiple annotator models, or domain-specific synthetic data?\",\n  \"opportunity\": \"PARSE (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184) demonstrates that automatic schema optimization improves extraction accuracy by 64.7% on SWDE — but requires offline synthetic data generation per domain. GuideX (ACL Findings 2025) shows that auto-generated guidelines improve zero-shot NER by 7 F1 points — but schemas are frozen at fine-tuning time. DiZiNER (arXiv:2604.15866, April 2026) achieves zero-shot SOTA on 14/18 NER benchmarks by having multiple heterogeneous LLMs annotate shared texts and using inter-model disagreement to refine annotation instructions — but (a) uses 8 simultaneous annotator LLMs (high inference cost), (b) explicitly keeps 'the NER schema fixed across iterations,' refining only surface-level instruction wording rather than type definitions, (c) requires 25-document batches sampled from training data, ruling out the truly zero-seed setting, and (d) is NER-only. SAM-NER (arXiv:2605.03706, May 2026) addresses zero-shot NER under schema/domain shifts via a three-stage semantic archetype mediation framework — but uses a frozen LLM throughout, maps to pre-established archetypes rather than revising type definitions at test time, and has no error-signal feedback loop. SPT (arXiv:2506.01276, June 2026) treats schemas as callable parameterized tools for universal IE across closed, open, and on-demand extraction tasks — but uses static schema selection and filling without online error-signal-driven type-definition revision. The gap is *online, single-extractor, schema-ontology* adaptation: using one model's own extraction inconsistencies — context-conditioned type contradictions, systematic pairwise type confusion patterns, and structurally invalid extractions — as signals to iteratively revise schema type definitions (splits, merges, boundary clarifications) during test-time deployment on streaming documents, with no gold labels, no training data access, and no multi-model ensemble.\",\n  \"landscape\": \"GoLLIE (ICLR 2024) shows annotation guidelines improve zero-shot IE but requires manually written guidelines. GuideX (ACL Findings 2025) automates guideline generation and achieves SOTA across 7 zero-shot NER benchmarks but cannot adapt post-deployment — schema is frozen at fine-tuning time. PARSE (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184) optimizes JSON schemas via iterative refinement on synthetic data — 64.7% improvement on SWDE — but is fundamentally offline, requiring seed data per domain. SCIR (AAAI 2026) introduces a self-correcting iterative refinement framework with dual-path feedback (redundancy detection + missing entity detection) for IE across NER, RE, and event extraction; however, it refines extraction predictions given a fixed schema rather than revising schema type definitions in response to concept-level mismatches. DiZiNER (arXiv:2604.15866, April 2026), the most directly concurrent work, achieves zero-shot SOTA on 14/18 NER benchmarks using inter-model disagreement among 8 heterogeneous LLMs to refine task instructions — but explicitly keeps 'the NER schema fixed across iterations to maintain task consistency,' modifies surface-level instruction wording rather than the type ontology, requires 25-document batches from training data, runs at 8× the inference cost of a single-extractor system, and is NER-only. SAM-NER (arXiv:2605.03706, May 2026) is concurrent work that addresses zero-shot NER under schema/domain shifts via semantic archetype mediation: a frozen LLM maps entity mentions to domain-invariant archetypes and resolves them into target-domain types via constrained inference — a distinct paradigm with no online error-signal loop and no test-time type-definition revision. SPT (arXiv:2506.01276, June 2026) is concurrent work that reimagines schemas as parameterized tools for universal IE, enabling closed, open, and on-demand extraction via schema retrieval, filling, and generation — a tool-calling paradigm for static schema selection, not error-signal-driven online type-definition revision. The open problem is the *zero-seed, single-extractor, online, schema-ontology* setting across NER, event extraction, and relation extraction: a model deployed on a new domain should detect its own concept-level schema mismatches from extraction pattern violations and propose targeted type-definition revisions — without gold labels, training data access, or multi-model ensembles.\",\n  \"approach\": \"We propose OSAFE (Online Schema Adaptation via Feedback Errors), a three-stage, zero-seed, single-extractor, test-time framework. In Stage 1, an error-detection layer monitors rolling extraction outputs for schema-domain mismatch signals over a sliding document buffer: (a) context-conditioned entity-type contradictions — the same surface form assigned conflicting types across documents whose surrounding sentence embeddings have cosine similarity above a threshold τ_sim, explicitly filtering out legitimate polysemy arising from different discourse contexts (e.g., 'Washington' as GPE in a political context vs. PERSON in a biographical context are not flagged because their sentence embeddings differ); (b) systematic type confusion patterns — persistent pairwise type swaps accumulating above a statistical confidence threshold, indicating structural boundary misalignment; (c) structurally invalid extractions — missing mandatory arguments in event or relation schemas, argument type constraint violations. In Stage 2, when a type's alignment score drops below an adaptive threshold, a frozen Qwen3-72B (or DeepSeek-R1) schema optimizer accessed via API receives the current type description, concrete mismatch examples, and neighboring type definitions as read-only context, then generates a targeted schema revision — type split, merge, or boundary clarification — without accessing any gold labels. Revisions are type-local by construction: neighboring type descriptions are immutable inputs, preventing cascade instability where revising type A creates new violations for type B. A cooldown mechanism locks a revised type from further revision for L documents, preventing oscillation. In Stage 3, the revised schema description is hot-swapped into the extraction prompt and validated on the same rolling buffer using three fully unsupervised proxy metrics: (1) violation-rate delta (VRD) — change in the fraction of buffer extractions flagging schema violations before vs. after revision; (2) cross-document consistency delta (CDCD) — reduction in context-conditioned entity-type contradictions for the revised type within the buffer; (3) argument completeness proxy (ACP) — for event and relation extraction tasks, change in fraction of instances with all mandatory arguments populated. The revision is committed only if ≥2/3 proxy metrics show improvement; otherwise the original schema description is restored. No gold labels are required or used at any stage.\\n\\nAnalytical experiments: (i) Signal reliability study — across all datasets, measure the fraction of detected context-conditioned contradictions that are true schema mismatches vs. legitimate polysemy at varying τ_sim values, plotting precision-recall and selecting τ_sim at the F1-maximizing point. (ii) Convergence analysis — track rounds-to-convergence and oscillation frequency across datasets and schema sizes, verifying that type-local revision plus cooldown achieves stable termination. (iii) Proxy metric validation — after running OSAFE across all benchmark datasets, compute Spearman rank correlation (ρ) between the composite proxy improvement score (VRD+CDCD+ACP) and actual gold F1 gain on sequestered test splits, reported per task type (NER, event extraction, RE). A correlation ρ ≥ 0.65 validates the ≥2/3 commitment gate; cases where proxy improvement does not correspond to F1 gain (e.g., trivial merges that mechanically reduce violations while collapsing entity distinctions) are analyzed separately to characterize conditions under which proxy reliability weakens. This experiment directly addresses the strongest anticipated reviewer objection: that the commitment gate could be gamed by schema revisions that improve proxy metrics while degrading extraction quality.\\n\\nNatural transfer experiment: Beyond synthetic contamination, we deploy an ACE05-fine-tuned GoLLIE-7B extractor on GENIA biomedical NER (1,854 test instances; 5 fine-grained biological entity types — DNA, RNA, protein, cell_type, cell_line — that naturally conflict with ACE05's coarse-grained entity ontology). No synthetic contamination is introduced; the schema mismatch arises entirely from domain transfer. We compare OSAFE against a frozen-schema baseline and report F1 before and after online adaptation. This validates that the error-detection layer reliably fires on naturally occurring rather than artificially injected mismatches.\\n\\nOptimizer size ablation: We ablate the schema optimizer model size on two representative tasks — ACE05 NER and TACRED RE — comparing Qwen3-72B (API, zero GPU cost) against Qwen3-7B (local inference, ~4h A100 additional). If OSAFE's gains persist with Qwen3-7B, the approach is cost-efficient for resource-constrained deployments; if they degrade, the result quantifies the minimum optimizer capacity required for reliable type-definition revision.\\n\\nMain evaluation is conducted under deliberate schema contamination at five severity levels (type merge, type split, label scramble, argument-type swap, boundary blur) on: ACE05 (NER + event), FewNERD (NER), SciERC (NER + RE), MAVEN (event detection), WikiEvents and RAMS (event argument extraction), TACRED/TACREV (RE), and DocRED (document-level RE). Baselines include PARSE, SCIR, GuideX, and DiZiNER adapted to a single-extractor setting for fair comparison. Target: 10–15% F1 recovery over non-adaptive baselines across NER, event, and relation extraction.\",\n  \"resource_estimate\": {\n    \"cost_architecture_note\": \"OSAFE separates two distinct compute streams: (1) GoLLIE-7B extractor inference — GPU-bound, run locally via vLLM on A100s; (2) Qwen3-72B schema optimizer — API-bound, zero GPU cost, accessed via Qwen/DeepSeek API. Prior estimates incorrectly counted Qwen3-72B against the GPU budget. The corrected estimates below reflect this split explicitly.\",\n    \"component_table\": {\n      \"headers\": [\n        \"Component\",\n        \"GPU cost (A100)\",\n        \"Approx H100 equiv\",\n        \"API cost\",\n        \"Notes\"\n      ],\n      \"rows\": [\n        [\n          \"GoLLIE-7B extractor: 8 datasets × 5 severity levels × {OSAFE + 3 ablation variants + 4 baselines}\",\n          \"~40h A100\",\n          \"~20h H100\",\n          \"$0\",\n          \"vLLM batching at ~4,000 tok/s; ~3,000 docs × 600 tok/doc per condition\"\n        ],\n        [\n          \"Qwen3-72B schema optimizer calls (all datasets, all conditions)\",\n          \"0h\",\n          \"0h\",\n          \"~$80–120\",\n          \"API; ~5,000–10,000 calls × ~1,500 tok avg = ~10M tokens\"\n        ],\n        [\n          \"Natural transfer experiment (ACE05 → GENIA, 1,854 test instances)\",\n          \"~3h A100\",\n          \"~1.5h H100\",\n          \"$5–10\",\n          \"One inference pass per system; GENIA publicly available\"\n        ],\n        [\n          \"Optimizer ablation (Qwen3-7B local, ACE05 + TACRED)\",\n          \"~4h A100\",\n          \"~2h H100\",\n          \"$0\",\n          \"Qwen3-7B runs locally; replaces API calls for ablation conditions only\"\n        ],\n        [\n          \"Proxy metric correlation analysis (post-hoc, no extra GPU)\",\n          \"0h\",\n          \"0h\",\n          \"$0\",\n          \"Spearman ρ computed over cached extraction outputs\"\n        ],\n        [\n          \"TOTAL\",\n          \"~47h A100\",\n          \"~24h H100\",\n          \"~$85–130\",\n          \"Well within 200h H100 budget\"\n        ]\n      ]\n    },\n    \"manual\": {\n      \"gpu_hours\": \"~47h A100 80GB total (≈24h H100) — dominated by extractor inference; Qwen3-72B optimizer runs via API at zero GPU cost\",\n      \"gpu_utilization\": \"~35-45% — idle time while researcher implements error-detection layer, calibrates τ_sim, inspects schema revision quality, runs proxy correlation analysis, and writes paper\",\n      \"timeline\": \"3–4 weeks\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$64 (47h × $1.35/hr on Lambda Labs)\",\n      \"estimated_api_cost\": \"~$85–130 (Qwen3-72B schema optimizer calls via API)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~47h A100 80GB total (≈24h H100) — same compute as manual; agent explores more τ_sim calibration and cooldown L values within the same experimental harness\",\n      \"gpu_utilization\": \"~60-70% — agent runs extractor inference jobs continuously between human approval gates; human reviews signal reliability results, proxy correlation analysis, and schema revision quality samples\",\n      \"timeline\": \"10–14 days wall-clock with 4–6 A100s running experiment queue in parallel (meets the 16-day submission deadline)\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (Opus 4.7 for agent orchestration ~1,500–2,500 turns; Qwen3-72B schema optimizer calls ~$80–120 additional)\",\n      \"estimated_gpu_cost\": \"~$64 (47h × $1.35/hr on Lambda Labs)\",\n      \"risk_note\": \"Two critical human gates: (1) proxy metric correlation results must be reviewed before committing the ≥2/3 gate — if Spearman ρ < 0.50 across task types, the gate threshold or metric weighting must be redesigned before proceeding to main evaluation; (2) a random sample of 20–30 committed schema revisions per dataset should be human-inspected for semantic coherence before paper submission.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~100h A100 80GB (≈50h H100) — full sweep over τ_sim thresholds, rolling window sizes, cooldown periods L, and all cross-domain schema contamination permutations across 8 datasets × 5 severity levels × 3 task types\",\n      \"gpu_utilization\": \"Near-zero idle — agent orchestrates experiment queue 24/7 with parallel GPU jobs; no human bottleneck between successive runs\",\n      \"timeline\": \"5–7 days with 4–8 A100s running in parallel\",\n      \"team\": \"0 (only initial setup of experiment harness and API keys)\",\n      \"claude_api_cost\": \"$300–500 (Opus 4.7 for agent orchestration + Qwen3-72B API schema optimizer calls across all datasets and task types)\",\n      \"estimated_gpu_cost\": \"~$135 (100h × $1.35/hr on Lambda Labs)\",\n      \"speed_bottleneck\": \"Number of A100 GPUs available for parallel experiment runs; Qwen/DeepSeek API rate limits on schema optimizer calls\",\n      \"risk_note\": \"Without human oversight, auto mode risks over-tuning τ_sim to specific dataset polysemy rates that do not generalize. The proxy metric correlation analysis must be explicitly monitored — if Spearman ρ < 0.50 for any task type, the commitment gate requires redesign before proceeding. Final evaluation must use a fully sequestered test split never touched during the adaptation phase.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; conference Oct 24-29, 2026, Budapest, Hungary)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\",\n    \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184)\",\n    \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)\",\n    \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)\",\n    \"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema (AAAI 2026)\",\n    \"DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition (arXiv:2604.15866, April 2026)\",\n    \"SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition (arXiv:2605.03706, May 2026)\",\n    \"SPT: Schema as Parameterized Tools for Universal Information Extraction (arXiv:2506.01276, June 2026)\"\n  ],\n  \"description\": \"Schema-guided IE models fail silently when deployed on domains whose entity type ontologies partially conflict with training-time schemas — for example, when a medical ontology's 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure'. This is a schema-ontology mismatch problem, distinct from the annotation instruction clarity problem addressed by DiZiNER. OSAFE (Online Schema Adaptation via Feedback Errors) addresses schema-ontology mismatch with a three-stage, zero-seed, single-extractor, test-time framework: (1) an error-detection layer accumulates mismatch signals over a rolling document buffer — context-conditioned entity-type contradictions filtered by sentence-embedding cosine similarity (threshold τ_sim) to exclude legitimate polysemy, persistent pairwise type confusion patterns, and structurally invalid extractions; (2) when a type's alignment score drops below an adaptive threshold, a Qwen3-72B schema optimizer accessed via API (zero GPU cost) proposes targeted type-definition revisions (splits, merges, boundary clarifications) using only mismatch examples and read-only neighboring type definitions, with type-local revision constraints and a per-type cooldown preventing cascade instability and oscillation; (3) the revised schema is hot-swapped into the extraction prompt and validated using three fully unsupervised proxy metrics — violation-rate delta (VRD), cross-document consistency delta (CDCD), and argument completeness proxy (ACP) — committing only if ≥2/3 metrics improve. Unlike PARSE (offline synthetic data required), SCIR (refines predictions not schema definitions), DiZiNER (multi-LLM ensemble, schema type definitions fixed, NER-only, requires training data batches), SAM-NER (frozen LLM, pre-established archetypes, no error-signal loop; concurrent work), and SPT (tool-calling for static schema selection, not online error-signal-driven revision; concurrent work), OSAFE operates online, single-extractor, and zero-seed across NER, event extraction, and relation extraction. The experimental plan includes five components: (a) signal reliability study calibrating τ_sim via precision-recall analysis; (b) convergence analysis verifying stable termination; (c) proxy metric validation — Spearman ρ between composite proxy improvement and gold F1 gain on sequestered test splits per task type, directly validating the ≥2/3 commitment gate; (d) natural cross-domain transfer experiment deploying ACE05-fine-tuned GoLLIE-7B on GENIA biomedical NER to demonstrate reliability on naturally occurring (not synthetically injected) schema mismatches; (e) optimizer size ablation (Qwen3-72B vs. Qwen3-7B on ACE05 and TACRED). All extractor inference runs on GoLLIE-7B via vLLM (~47h A100 total across all conditions); Qwen3-72B schema optimizer runs via API at zero GPU cost — total compute ≈ 24h H100, well within budget, with 10–14 day wall-clock achievable with 4–6 A100s. Evaluated under deliberate schema contamination at five severity levels on ACE05, FewNERD, SciERC, MAVEN, WikiEvents, RAMS, TACRED/TACREV, and DocRED, targeting 10–15% F1 recovery over non-adaptive baselines.\",\n  \"project_name\": \"schema_adapt_feedback\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"UNCITED CONCURRENT WORK: DiZiNER (arXiv:2604.15866, Apr 2026) achieves zero-shot SOTA on 14/18 NER benchmarks using multi-LLM disagreement analysis to iteratively refine NER instructions — no parameter updates, no gold labels. This is structurally parallel to OSAFE's error-driven schema revision. The generator must cite, compare against, and differentiate from DiZiNER, or its novelty claim is significantly weakened.\", \"VALIDATION PARADOX (Stage 3): The description states the revised schema is 'validated on a held-out document buffer to confirm F1 improvement' before being committed. F1 requires gold labels. This directly contradicts the zero-seed claim. The paper must either (a) replace F1 with a fully unsupervised proxy signal (violation-rate change, cross-document consistency delta), or (b) acknowledge a small labeled validation split, which must be subtracted from the adaptation budget.\", \"EVALUATION MISMATCH WITH HARD CONSTRAINTS: The user's stated hard-constraint benchmark list is ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS. The proposal evaluates only on FewNERD, CrossNERD, and MultiNERD — the latter two are NOT in the required list. Event extraction (MAVEN, WikiEvents, RAMS) and relation extraction (TACRED, DocRED) are entirely absent, yet EMNLP IE reviewers will expect coverage beyond NER.\", \"SIGNAL RELIABILITY: Cross-sentence entity-type contradictions are noisy signals. The same surface form is legitimately typed differently across documents (e.g., 'Washington' as GPE vs. PERSON). The paper offers no analysis of how many contradictions are true schema mismatches vs. legitimate polysemy, and provides no threshold-calibration strategy beyond 'adaptive threshold' — this needs empirical grounding.\", \"SCHEMA EVOLUTION STABILITY: Iterative schema revisions on a multi-type schema may cause cascading instability — changing the boundary of type A to absorb part of type B will create new apparent violations for type B, potentially triggering further revisions. The paper has no analysis of convergence or oscillation risk in the schema revision loop.\", \"PARSE VENUE MISLABEL: The generator describes PARSE as 'arXiv 2510.08623, 2025' in the opportunity section but correctly identifies it as EMNLP 2025 Industry Track elsewhere. The citation should consistently list its actual publication venue (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184) rather than as a preprint.\"]\nFeedback: The core idea — using the extractor's own type-consistency violations as a signal to drive online schema revision — is conceptually clean and fills a real gap. The three-stage decomposition is well-motivated. To reach acceptance quality, the generator must address four structural issues: (1) **DiZiNER differentiator**: Read arXiv:2604.15866 and add a paragraph explicitly separating OSAFE from DiZiNER. The sharpest differentiator is that DiZiNER requires multiple LLMs annotating the same texts (multi-annotator simulation) whereas OSAFE runs with a single extractor and accumulates cross-document inconsistency signals — frame this as the operational advantage. (2) **Repair the validation paradox**: Replace 'F1 improvement on held-out buffer' with an unsupervised proxy — e.g., *violation-rate delta* (fraction of rolling buffer extractions flagging schema violations before vs. after revision), possibly combined with extraction coverage (recall-proxy via argument completeness). If a small labeled validation split must be used, say so and budget it explicitly. (3) **Expand evaluation to required benchmarks**: Add ACE05 (NER+RE), MAVEN (event extraction), and TACRED (RE) experiments. For event extraction, the schema contamination can be applied to argument-type definitions (e.g., scrambling AGENT vs. PATIENT). This addresses both the hard-constraint mismatch and the concern that NER-only evaluation limits generalization claims. (4) **Add signal-noise analysis**: Include a small analytical experiment quantifying what fraction of detected 'type contradictions' are true schema-domain mismatches vs. legitimate polysemy, and justify the confidence threshold by showing precision-recall trade-off of the error-detection layer.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"DUAL CONSTRAINT INFEASIBILITY: No proposed mode satisfies ≤200 H100-hours AND ≤16 days simultaneously. Manual (250h A100 ≈ 125h H100) meets compute but takes 4–6 months. HIL (350h A100 ≈ 175h H100) meets compute but takes 5–7 weeks. Auto Research (900h A100 ≈ 450h H100) meets the timeline but exceeds the compute budget by ~2.25×. The generator must redesign the experimental plan: the schema optimizer (Qwen3-72B) can run via API with zero GPU cost; the base extractor (GoLLIE-7B) inference across all 8 datasets × 5 severity levels should require only ~20–50h A100 with vLLM batching, well within budget. The 250h A100 manual estimate appears to conflate fine-tuning cost with inference-only evaluation. A corrected compute breakdown — splitting extractor inference (GPU) from schema optimizer (API) — is needed to show the 16-day plan is feasible.\", \"PROXY METRIC CIRCULAR REASONING: VRD (violation-rate delta) and CDCD (cross-document consistency delta) are computed on the same rolling document buffer that generated the mismatch signals that triggered revision. Any schema revision that addresses even a subset of buffer-specific violations will mechanically improve these metrics — including harmful revisions such as merging all confused types into one super-type. The paper must include an empirical validation experiment demonstrating that proxy metric improvements on the buffer predict F1 improvement on a sequestered held-out test split (using gold labels post-hoc only, not for revision decisions). Without this, the unsupervised validation mechanism has no demonstrated reliability.\", \"SYNTHETIC-ONLY EVALUATION: All 8 required benchmark evaluations use deliberately introduced schema contamination (type merge, split, label scramble, argument-type swap, boundary blur). This validates recovery from constructed mismatches but does not establish that the error-detection layer — especially context-conditioned contradiction detection — fires reliably on naturally occurring schema-ontology divergences. At minimum one real-world cross-domain transfer scenario should be added (e.g., ACE05-trained extractor deployed on GENIA biomedical NER, or ACE event types applied to WikiEvents argument definitions), comparing OSAFE against a non-adaptive baseline without synthetic contamination.\", \"SCHEMA OPTIMIZER MODEL SIZE ABLATION MISSING: Qwen3-72B is used as the schema optimizer. A reviewer will immediately ask: does the improvement come from the error-detection algorithm (OSAFE's core contribution) or simply from Qwen3-72B's ability to improve any type definition given examples? An ablation substituting Qwen3-7B, Llama-3-8B-Instruct, or a smaller model as the optimizer is needed to decouple the error-signal quality from raw LLM capability. Without this, the paper risks being read as 'give a very large LLM some confusion examples and ask it to rewrite the schema.'\", \"SAM-NER CONCURRENT WORK UNCITED: SAM-NER (arXiv:2605.03706, May 5, 2026) addresses zero-shot NER under schema shifts via semantic archetype mediation — projecting entities through domain-invariant archetypes before mapping to target types. It is not a direct competitor (uses frozen inference, no online revision, no type-definition modification), but it should be cited as concurrent work. Note: appeared 5 days before the review date; generator cannot be faulted, but the paper should acknowledge it before submission.\"]\nFeedback: The Round 2 revision comprehensively addressed all six Round 1 issues. The positioning against DiZiNER, PARSE, SCIR, and GuideX is now precise and defensible. Five focused issues remain. The most critical are (1) and (2). (1) Fix the resource estimate by explicitly separating extractor inference (GPU, very cheap for GoLLIE-7B inference across 8 datasets — likely 20-50h A100 total) from schema optimizer (Qwen3-72B via API, zero GPU cost). Show that the 16-day plan is feasible using ~50h A100 equivalent, well within 200 H100-hours. The current estimates conflate inference-only evaluation with fine-tuning workloads and will fail a reviewer sanity check. (2) Add an explicit proxy-metric reliability experiment: after running OSAFE on each dataset, plot proxy metric improvement (VRD, CDCD, ACP) against actual F1 improvement on the test split. This correlation analysis — even in one section of the experiments — validates the unsupervised validation gate and preempts the strongest methodological objection. (3) Add one natural domain transfer experiment (no synthetic contamination): pick any cross-domain NER or event pair (e.g., ACE05→biomedical, TACRED→SciERC cross-domain RE) and show OSAFE improves over a frozen schema baseline. This grounds practical value beyond constructed mismatches. (4) Add schema optimizer ablation (Qwen3-72B vs. Qwen3-7B) to isolate the error-signal contribution. (5) Mention SAM-NER (arXiv:2605.03706) as concurrent work in a footnote. Issues (3)-(5) are relatively quick to address. Issues (1)-(2) are the gate to a pass verdict.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — RESOURCE ESTIMATES UNCHANGED (Round 2 Issue 1 persists): The gpu_hours and timeline figures are byte-for-byte identical to Round 2. Manual (~250h A100, 4–6 months) and HIL (~350h A100, 5–7 weeks) satisfy compute (≤200h H100) but violate the 16-day deadline by 3–8×. Auto (~900h A100, 1–2 weeks) meets the timeline but consumes ~450h H100 — 2.25× the compute budget. No mode satisfies both hard constraints. The fix prescribed in Round 2 — separating GoLLIE-7B extractor inference (GPU, ~20–50h A100 total with vLLM batching across all 8 datasets × 5 severity levels) from Qwen3-72B schema optimizer (Anthropic/DeepSeek API, zero GPU cost) — was not implemented. A corrected HIL estimate of ~50h A100 (≈25h H100) with a 16-day wall-clock timeline is readily achievable and must be shown explicitly.\", \"CRITICAL — PROXY METRIC VALIDATION EXPERIMENT MISSING (Round 2 Issue 2 persists): The analytical experiments section describes only a signal reliability study (τ_sim calibration) and a convergence analysis. The correlation experiment prescribed in Round 2 — plotting per-dataset VRD+CDCD+ACP composite improvement against actual F1 improvement on a sequestered test split — is absent. Without this, the ≥2/3 commitment gate is unvalidated: a trivial revision (merge all confused types into one super-type) could mechanically improve all three proxy metrics while degrading test F1. This is the strongest methodological objection a reviewer will raise.\", \"SIGNIFICANT — SYNTHETIC-ONLY EVALUATION (Round 2 Issue 3 persists): All eight benchmark evaluations use deliberately introduced schema contamination. No natural cross-domain transfer experiment is included. The Round 2 reviewer explicitly asked for 'at minimum one real-world cross-domain transfer scenario (e.g., ACE05-trained extractor deployed on GENIA biomedical NER, or TACRED→SciERC cross-domain RE).' Without this, the error-detection layer's reliability on naturally occurring mismatches is undemonstrated, and the paper's claim of practical deployment utility is unsupported.\", \"SIGNIFICANT — SCHEMA OPTIMIZER ABLATION ABSENT (Round 2 Issue 4 persists): Qwen3-72B is used as the schema optimizer throughout. No ablation with Qwen3-7B or Llama-3-8B-Instruct is included. A reviewer will ask whether OSAFE's gains stem from the error-signal algorithm or simply from a 72B model's general instruction-following ability. Two datasets (e.g., ACE05 NER, TACRED RE) with optimizer size as a variable is sufficient.\", \"MINOR — SAM-NER NOT CITED (Round 2 Issue 5 persists): SAM-NER (arXiv:2605.03706, May 5 2026; verified as a real paper) addresses zero-shot NER under schema/domain shifts via semantic archetype mediation. It is a different approach (frozen inference, no online type-definition revision, no error-signal loop) and does not threaten OSAFE's novelty, but it must appear as a concurrent-work footnote before submission.\", \"NEW — SPT NOT CITED: Schema as Parameterized Tools (arXiv:2506.01276, ~June 2026) treats schemas as callable parameterized tools supporting schema retrieval, filling, and on-demand generation for universal IE across four tasks. This directly overlaps OSAFE's motivation (schema adaptability for IE) and must be cited and differentiated. SPT uses a tool-calling paradigm for static schema selection/generation — it does not perform online error-signal-driven type-definition revision — so OSAFE's approach is distinct. One sentence in the related work section is sufficient.\"]\nFeedback: The Round 3 revision successfully preserved all six Round 1 fixes and made meaningful progress on proxy metric precision (VRD/CDCD/ACP with ≥2/3 commitment rule). However, the two most critical Round 2 issues remain completely unaddressed — the generator appears to have not changed the resource section or the experimental plan at all. To unblock passage, address these in priority order:\n\n(1) **Fix the resource estimate NOW** — the numbers are wrong and unchanged. The actual compute cost is: GoLLIE-7B inference across 8 datasets × 5 severity levels × schema optimizer API calls ≈ 30–50h A100 (≈15–25h H100) for extractor inference with vLLM batching, plus zero GPU cost for Qwen3-72B calls via API. A HIL plan with 4–6 A100s runs in 10–14 days and uses <50h H100 total. Write a three-row table: component | GPU cost | API cost | wall-clock. This is a 30-minute fix that eliminates the paper's most obvious reviewability problem.\n\n(2) **Add proxy metric correlation experiment** — after running OSAFE across all datasets, compute Spearman correlation between composite proxy improvement (VRD+CDCD+ACP) and gold F1 gain on sequestered test splits. Report per-task correlations. A correlation ≥ 0.65 validates the commitment gate; if lower, discuss what conditions weaken proxy reliability. This can be a half-page subsection in the experiments.\n\n(3) **Add one natural transfer experiment** — deploy ACE05-fine-tuned GoLLIE on GENIA (biomedical NER, cross-domain, no synthetic contamination) and compare OSAFE vs. frozen schema. This requires one inference run per system and a one-paragraph write-up.\n\n(4) **Optimizer ablation** — run Qwen3-72B vs. Qwen3-7B on ACE05 and TACRED. Add a two-row table to the ablation section.\n\n(5) **Two citation additions** — SAM-NER (arXiv:2605.03706) and SPT (arXiv:2506.01276) as concurrent-work footnotes in §2. Two sentences total.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:06:58.090Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:06:58.090Z",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-10T08:06:58.114Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.

Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.

Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.

Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.

Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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

## Idea under review (round 4/10)
{
  "title": "Online Schema Adaptation via Extraction-Error Feedback Loops",
  "core_problem": "Schema-guided IE models (GoLLIE, KnowCoder, GuideX) fix the extraction schema at training or deployment time. When a new domain has a schema that partially conflicts with training-time guidelines — e.g., a medical ontology where 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure', or a legal corpus where 'Organization' granularity differs from the training ontology — models fail silently with no mechanism to refine their operational schema. This is a *schema-ontology mismatch* problem: the set of types and their definitional boundaries in the target domain do not correspond to the types the model was trained to extract. It is distinct from the annotation instruction clarity problem, which concerns surface wording of fixed type definitions. How can IE models detect and recover from schema-ontology mismatches at test time without gold labels, multiple annotator models, or domain-specific synthetic data?",
  "opportunity": "PARSE (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184) demonstrates that automatic schema optimization improves extraction accuracy by 64.7% on SWDE — but requires offline synthetic data generation per domain. GuideX (ACL Findings 2025) shows that auto-generated guidelines improve zero-shot NER by 7 F1 points — but schemas are frozen at fine-tuning time. DiZiNER (arXiv:2604.15866, April 2026) achieves zero-shot SOTA on 14/18 NER benchmarks by having multiple heterogeneous LLMs annotate shared texts and using inter-model disagreement to refine annotation instructions — but (a) uses 8 simultaneous annotator LLMs (high inference cost), (b) explicitly keeps 'the NER schema fixed across iterations,' refining only surface-level instruction wording rather than type definitions, (c) requires 25-document batches sampled from training data, ruling out the truly zero-seed setting, and (d) is NER-only. SAM-NER (arXiv:2605.03706, May 2026) addresses zero-shot NER under schema/domain shifts via a three-stage semantic archetype mediation framework — but uses a frozen LLM throughout, maps to pre-established archetypes rather than revising type definitions at test time, and has no error-signal feedback loop. SPT (arXiv:2506.01276, June 2026) treats schemas as callable parameterized tools for universal IE across closed, open, and on-demand extraction tasks — but uses static schema selection and filling without online error-signal-driven type-definition revision. The gap is *online, single-extractor, schema-ontology* adaptation: using one model's own extraction inconsistencies — context-conditioned type contradictions, systematic pairwise type confusion patterns, and structurally invalid extractions — as signals to iteratively revise schema type definitions (splits, merges, boundary clarifications) during test-time deployment on streaming documents, with no gold labels, no training data access, and no multi-model ensemble.",
  "landscape": "GoLLIE (ICLR 2024) shows annotation guidelines improve zero-shot IE but requires manually written guidelines. GuideX (ACL Findings 2025) automates guideline generation and achieves SOTA across 7 zero-shot NER benchmarks but cannot adapt post-deployment — schema is frozen at fine-tuning time. PARSE (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184) optimizes JSON schemas via iterative refinement on synthetic data — 64.7% improvement on SWDE — but is fundamentally offline, requiring seed data per domain. SCIR (AAAI 2026) introduces a self-correcting iterative refinement framework with dual-path feedback (redundancy detection + missing entity detection) for IE across NER, RE, and event extraction; however, it refines extraction predictions given a fixed schema rather than revising schema type definitions in response to concept-level mismatches. DiZiNER (arXiv:2604.15866, April 2026), the most directly concurrent work, achieves zero-shot SOTA on 14/18 NER benchmarks using inter-model disagreement among 8 heterogeneous LLMs to refine task instructions — but explicitly keeps 'the NER schema fixed across iterations to maintain task consistency,' modifies surface-level instruction wording rather than the type ontology, requires 25-document batches from training data, runs at 8× the inference cost of a single-extractor system, and is NER-only. SAM-NER (arXiv:2605.03706, May 2026) is concurrent work that addresses zero-shot NER under schema/domain shifts via semantic archetype mediation: a frozen LLM maps entity mentions to domain-invariant archetypes and resolves them into target-domain types via constrained inference — a distinct paradigm with no online error-signal loop and no test-time type-definition revision. SPT (arXiv:2506.01276, June 2026) is concurrent work that reimagines schemas as parameterized tools for universal IE, enabling closed, open, and on-demand extraction via schema retrieval, filling, and generation — a tool-calling paradigm for static schema selection, not error-signal-driven online type-definition revision. The open problem is the *zero-seed, single-extractor, online, schema-ontology* setting across NER, event extraction, and relation extraction: a model deployed on a new domain should detect its own concept-level schema mismatches from extraction pattern violations and propose targeted type-definition revisions — without gold labels, training data access, or multi-model ensembles.",
  "approach": "We propose OSAFE (Online Schema Adaptation via Feedback Errors), a three-stage, zero-seed, single-extractor, test-time framework. In Stage 1, an error-detection layer monitors rolling extraction outputs for schema-domain mismatch signals over a sliding document buffer: (a) context-conditioned entity-type contradictions — the same surface form assigned conflicting types across documents whose surrounding sentence embeddings have cosine similarity above a threshold τ_sim, explicitly filtering out legitimate polysemy arising from different discourse contexts (e.g., 'Washington' as GPE in a political context vs. PERSON in a biographical context are not flagged because their sentence embeddings differ); (b) systematic type confusion patterns — persistent pairwise type swaps accumulating above a statistical confidence threshold, indicating structural boundary misalignment; (c) structurally invalid extractions — missing mandatory arguments in event or relation schemas, argument type constraint violations. In Stage 2, when a type's alignment score drops below an adaptive threshold, a frozen Qwen3-72B (or DeepSeek-R1) schema optimizer accessed via API receives the current type description, concrete mismatch examples, and neighboring type definitions as read-only context, then generates a targeted schema revision — type split, merge, or boundary clarification — without accessing any gold labels. Revisions are type-local by construction: neighboring type descriptions are immutable inputs, preventing cascade instability where revising type A creates new violations for type B. A cooldown mechanism locks a revised type from further revision for L documents, preventing oscillation. In Stage 3, the revised schema description is hot-swapped into the extraction prompt and validated on the same rolling buffer using three fully unsupervised proxy metrics: (1) violation-rate delta (VRD) — change in the fraction of buffer extractions flagging schema violations before vs. after revision; (2) cross-document consistency delta (CDCD) — reduction in context-conditioned entity-type contradictions for the revised type within the buffer; (3) argument completeness proxy (ACP) — for event and relation extraction tasks, change in fraction of instances with all mandatory arguments populated. The revision is committed only if ≥2/3 proxy metrics show improvement; otherwise the original schema description is restored. No gold labels are required or used at any stage.\n\nAnalytical experiments: (i) Signal reliability study — across all datasets, measure the fraction of detected context-conditioned contradictions that are true schema mismatches vs. legitimate polysemy at varying τ_sim values, plotting precision-recall and selecting τ_sim at the F1-maximizing point. (ii) Convergence analysis — track rounds-to-convergence and oscillation frequency across datasets and schema sizes, verifying that type-local revision plus cooldown achieves stable termination. (iii) Proxy metric validation — after running OSAFE across all benchmark datasets, compute Spearman rank correlation (ρ) between the composite proxy improvement score (VRD+CDCD+ACP) and actual gold F1 gain on sequestered test splits, reported per task type (NER, event extraction, RE). A correlation ρ ≥ 0.65 validates the ≥2/3 commitment gate; cases where proxy improvement does not correspond to F1 gain (e.g., trivial merges that mechanically reduce violations while collapsing entity distinctions) are analyzed separately to characterize conditions under which proxy reliability weakens. This experiment directly addresses the strongest anticipated reviewer objection: that the commitment gate could be gamed by schema revisions that improve proxy metrics while degrading extraction quality.\n\nNatural transfer experiment: Beyond synthetic contamination, we deploy an ACE05-fine-tuned GoLLIE-7B extractor on GENIA biomedical NER (1,854 test instances; 5 fine-grained biological entity types — DNA, RNA, protein, cell_type, cell_line — that naturally conflict with ACE05's coarse-grained entity ontology). No synthetic contamination is introduced; the schema mismatch arises entirely from domain transfer. We compare OSAFE against a frozen-schema baseline and report F1 before and after online adaptation. This validates that the error-detection layer reliably fires on naturally occurring rather than artificially injected mismatches.\n\nOptimizer size ablation: We ablate the schema optimizer model size on two representative tasks — ACE05 NER and TACRED RE — comparing Qwen3-72B (API, zero GPU cost) against Qwen3-7B (local inference, ~4h A100 additional). If OSAFE's gains persist with Qwen3-7B, the approach is cost-efficient for resource-constrained deployments; if they degrade, the result quantifies the minimum optimizer capacity required for reliable type-definition revision.\n\nMain evaluation is conducted under deliberate schema contamination at five severity levels (type merge, type split, label scramble, argument-type swap, boundary blur) on: ACE05 (NER + event), FewNERD (NER), SciERC (NER + RE), MAVEN (event detection), WikiEvents and RAMS (event argument extraction), TACRED/TACREV (RE), and DocRED (document-level RE). Baselines include PARSE, SCIR, GuideX, and DiZiNER adapted to a single-extractor setting for fair comparison. Target: 10–15% F1 recovery over non-adaptive baselines across NER, event, and relation extraction.",
  "resource_estimate": {
    "cost_architecture_note": "OSAFE separates two distinct compute streams: (1) GoLLIE-7B extractor inference — GPU-bound, run locally via vLLM on A100s; (2) Qwen3-72B schema optimizer — API-bound, zero GPU cost, accessed via Qwen/DeepSeek API. Prior estimates incorrectly counted Qwen3-72B against the GPU budget. The corrected estimates below reflect this split explicitly.",
    "component_table": {
      "headers": [
        "Component",
        "GPU cost (A100)",
        "Approx H100 equiv",
        "API cost",
        "Notes"
      ],
      "rows": [
        [
          "GoLLIE-7B extractor: 8 datasets × 5 severity levels × {OSAFE + 3 ablation variants + 4 baselines}",
          "~40h A100",
          "~20h H100",
          "$0",
          "vLLM batching at ~4,000 tok/s; ~3,000 docs × 600 tok/doc per condition"
        ],
        [
          "Qwen3-72B schema optimizer calls (all datasets, all conditions)",
          "0h",
          "0h",
          "~$80–120",
          "API; ~5,000–10,000 calls × ~1,500 tok avg = ~10M tokens"
        ],
        [
          "Natural transfer experiment (ACE05 → GENIA, 1,854 test instances)",
          "~3h A100",
          "~1.5h H100",
          "$5–10",
          "One inference pass per system; GENIA publicly available"
        ],
        [
          "Optimizer ablation (Qwen3-7B local, ACE05 + TACRED)",
          "~4h A100",
          "~2h H100",
          "$0",
          "Qwen3-7B runs locally; replaces API calls for ablation conditions only"
        ],
        [
          "Proxy metric correlation analysis (post-hoc, no extra GPU)",
          "0h",
          "0h",
          "$0",
          "Spearman ρ computed over cached extraction outputs"
        ],
        [
          "TOTAL",
          "~47h A100",
          "~24h H100",
          "~$85–130",
          "Well within 200h H100 budget"
        ]
      ]
    },
    "manual": {
      "gpu_hours": "~47h A100 80GB total (≈24h H100) — dominated by extractor inference; Qwen3-72B optimizer runs via API at zero GPU cost",
      "gpu_utilization": "~35-45% — idle time while researcher implements error-detection layer, calibrates τ_sim, inspects schema revision quality, runs proxy correlation analysis, and writes paper",
      "timeline": "3–4 weeks",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$64 (47h × $1.35/hr on Lambda Labs)",
      "estimated_api_cost": "~$85–130 (Qwen3-72B schema optimizer calls via API)"
    },
    "human_in_loop": {
      "gpu_hours": "~47h A100 80GB total (≈24h H100) — same compute as manual; agent explores more τ_sim calibration and cooldown L values within the same experimental harness",
      "gpu_utilization": "~60-70% — agent runs extractor inference jobs continuously between human approval gates; human reviews signal reliability results, proxy correlation analysis, and schema revision quality samples",
      "timeline": "10–14 days wall-clock with 4–6 A100s running experiment queue in parallel (meets the 16-day submission deadline)",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150–250 (Opus 4.7 for agent orchestration ~1,500–2,500 turns; Qwen3-72B schema optimizer calls ~$80–120 additional)",
      "estimated_gpu_cost": "~$64 (47h × $1.35/hr on Lambda Labs)",
      "risk_note": "Two critical human gates: (1) proxy metric correlation results must be reviewed before committing the ≥2/3 gate — if Spearman ρ < 0.50 across task types, the gate threshold or metric weighting must be redesigned before proceeding to main evaluation; (2) a random sample of 20–30 committed schema revisions per dataset should be human-inspected for semantic coherence before paper submission."
    },
    "auto_research": {
      "gpu_hours": "~100h A100 80GB (≈50h H100) — full sweep over τ_sim thresholds, rolling window sizes, cooldown periods L, and all cross-domain schema contamination permutations across 8 datasets × 5 severity levels × 3 task types",
      "gpu_utilization": "Near-zero idle — agent orchestrates experiment queue 24/7 with parallel GPU jobs; no human bottleneck between successive runs",
      "timeline": "5–7 days with 4–8 A100s running in parallel",
      "team": "0 (only initial setup of experiment harness and API keys)",
      "claude_api_cost": "$300–500 (Opus 4.7 for agent orchestration + Qwen3-72B API schema optimizer calls across all datasets and task types)",
      "estimated_gpu_cost": "~$135 (100h × $1.35/hr on Lambda Labs)",
      "speed_bottleneck": "Number of A100 GPUs available for parallel experiment runs; Qwen/DeepSeek API rate limits on schema optimizer calls",
      "risk_note": "Without human oversight, auto mode risks over-tuning τ_sim to specific dataset polysemy rates that do not generalize. The proxy metric correlation analysis must be explicitly monitored — if Spearman ρ < 0.50 for any task type, the commitment gate requires redesign before proceeding. Final evaluation must use a fully sequestered test split never touched during the adaptation phase."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; conference Oct 24-29, 2026, Budapest, Hungary)"
  ],
  "level": "solid",
  "key_references": [
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184)",
    "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema (AAAI 2026)",
    "DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition (arXiv:2604.15866, April 2026)",
    "SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition (arXiv:2605.03706, May 2026)",
    "SPT: Schema as Parameterized Tools for Universal Information Extraction (arXiv:2506.01276, June 2026)"
  ],
  "description": "Schema-guided IE models fail silently when deployed on domains whose entity type ontologies partially conflict with training-time schemas — for example, when a medical ontology's 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure'. This is a schema-ontology mismatch problem, distinct from the annotation instruction clarity problem addressed by DiZiNER. OSAFE (Online Schema Adaptation via Feedback Errors) addresses schema-ontology mismatch with a three-stage, zero-seed, single-extractor, test-time framework: (1) an error-detection layer accumulates mismatch signals over a rolling document buffer — context-conditioned entity-type contradictions filtered by sentence-embedding cosine similarity (threshold τ_sim) to exclude legitimate polysemy, persistent pairwise type confusion patterns, and structurally invalid extractions; (2) when a type's alignment score drops below an adaptive threshold, a Qwen3-72B schema optimizer accessed via API (zero GPU cost) proposes targeted type-definition revisions (splits, merges, boundary clarifications) using only mismatch examples and read-only neighboring type definitions, with type-local revision constraints and a per-type cooldown preventing cascade instability and oscillation; (3) the revised schema is hot-swapped into the extraction prompt and validated using three fully unsupervised proxy metrics — violation-rate delta (VRD), cross-document consistency delta (CDCD), and argument completeness proxy (ACP) — committing only if ≥2/3 metrics improve. Unlike PARSE (offline synthetic data required), SCIR (refines predictions not schema definitions), DiZiNER (multi-LLM ensemble, schema type definitions fixed, NER-only, requires training data batches), SAM-NER (frozen LLM, pre-established archetypes, no error-signal loop; concurrent work), and SPT (tool-calling for static schema selection, not online error-signal-driven revision; concurrent work), OSAFE operates online, single-extractor, and zero-seed across NER, event extraction, and relation extraction. The experimental plan includes five components: (a) signal reliability study calibrating τ_sim via precision-recall analysis; (b) convergence analysis verifying stable termination; (c) proxy metric validation — Spearman ρ between composite proxy improvement and gold F1 gain on sequestered test splits per task type, directly validating the ≥2/3 commitment gate; (d) natural cross-domain transfer experiment deploying ACE05-fine-tuned GoLLIE-7B on GENIA biomedical NER to demonstrate reliability on naturally occurring (not synthetically injected) schema mismatches; (e) optimizer size ablation (Qwen3-72B vs. Qwen3-7B on ACE05 and TACRED). All extractor inference runs on GoLLIE-7B via vLLM (~47h A100 total across all conditions); Qwen3-72B schema optimizer runs via API at zero GPU cost — total compute ≈ 24h H100, well within budget, with 10–14 day wall-clock achievable with 4–6 A100s. Evaluated under deliberate schema contamination at five severity levels on ACE05, FewNERD, SciERC, MAVEN, WikiEvents, RAMS, TACRED/TACREV, and DocRED, targeting 10–15% F1 recovery over non-adaptive baselines.",
  "project_name": "schema_adapt_feedback",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["UNCITED CONCURRENT WORK: DiZiNER (arXiv:2604.15866, Apr 2026) achieves zero-shot SOTA on 14/18 NER benchmarks using multi-LLM disagreement analysis to iteratively refine NER instructions — no parameter updates, no gold labels. This is structurally parallel to OSAFE's error-driven schema revision. The generator must cite, compare against, and differentiate from DiZiNER, or its novelty claim is significantly weakened.", "VALIDATION PARADOX (Stage 3): The description states the revised schema is 'validated on a held-out document buffer to confirm F1 improvement' before being committed. F1 requires gold labels. This directly contradicts the zero-seed claim. The paper must either (a) replace F1 with a fully unsupervised proxy signal (violation-rate change, cross-document consistency delta), or (b) acknowledge a small labeled validation split, which must be subtracted from the adaptation budget.", "EVALUATION MISMATCH WITH HARD CONSTRAINTS: The user's stated hard-constraint benchmark list is ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS. The proposal evaluates only on FewNERD, CrossNERD, and MultiNERD — the latter two are NOT in the required list. Event extraction (MAVEN, WikiEvents, RAMS) and relation extraction (TACRED, DocRED) are entirely absent, yet EMNLP IE reviewers will expect coverage beyond NER.", "SIGNAL RELIABILITY: Cross-sentence entity-type contradictions are noisy signals. The same surface form is legitimately typed differently across documents (e.g., 'Washington' as GPE vs. PERSON). The paper offers no analysis of how many contradictions are true schema mismatches vs. legitimate polysemy, and provides no threshold-calibration strategy beyond 'adaptive threshold' — this needs empirical grounding.", "SCHEMA EVOLUTION STABILITY: Iterative schema revisions on a multi-type schema may cause cascading instability — changing the boundary of type A to absorb part of type B will create new apparent violations for type B, potentially triggering further revisions. The paper has no analysis of convergence or oscillation risk in the schema revision loop.", "PARSE VENUE MISLABEL: The generator describes PARSE as 'arXiv 2510.08623, 2025' in the opportunity section but correctly identifies it as EMNLP 2025 Industry Track elsewhere. The citation should consistently list its actual publication venue (EMNLP 2025 Industry Track, ACL Anthology 2025.emnlp-industry.184) rather than as a preprint."]
Feedback: The core idea — using the extractor's own type-consistency violations as a signal to drive online schema revision — is conceptually clean and fills a real gap. The three-stage decomposition is well-motivated. To reach acceptance quality, the generator must address four structural issues: (1) **DiZiNER differentiator**: Read arXiv:2604.15866 and add a paragraph explicitly separating OSAFE from DiZiNER. The sharpest differentiator is that DiZiNER requires multiple LLMs annotating the same texts (multi-annotator simulation) whereas OSAFE runs with a single extractor and accumulates cross-document inconsistency signals — frame this as the operational advantage. (2) **Repair the validation paradox**: Replace 'F1 improvement on held-out buffer' with an unsupervised proxy — e.g., *violation-rate delta* (fraction of rolling buffer extractions flagging schema violations before vs. after revision), possibly combined with extraction coverage (recall-proxy via argument completeness). If a small labeled validation split must be used, say so and budget it explicitly. (3) **Expand evaluation to required benchmarks**: Add ACE05 (NER+RE), MAVEN (event extraction), and TACRED (RE) experiments. For event extraction, the schema contamination can be applied to argument-type definitions (e.g., scrambling AGENT vs. PATIENT). This addresses both the hard-constraint mismatch and the concern that NER-only evaluation limits generalization claims. (4) **Add signal-noise analysis**: Include a small analytical experiment quantifying what fraction of detected 'type contradictions' are true schema-domain mismatches vs. legitimate polysemy, and justify the confidence threshold by showing precision-recall trade-off of the error-detection layer.

### Round 2 review
Verdict: revise
Issues: ["DUAL CONSTRAINT INFEASIBILITY: No proposed mode satisfies ≤200 H100-hours AND ≤16 days simultaneously. Manual (250h A100 ≈ 125h H100) meets compute but takes 4–6 months. HIL (350h A100 ≈ 175h H100) meets compute but takes 5–7 weeks. Auto Research (900h A100 ≈ 450h H100) meets the timeline but exceeds the compute budget by ~2.25×. The generator must redesign the experimental plan: the schema optimizer (Qwen3-72B) can run via API with zero GPU cost; the base extractor (GoLLIE-7B) inference across all 8 datasets × 5 severity levels should require only ~20–50h A100 with vLLM batching, well within budget. The 250h A100 manual estimate appears to conflate fine-tuning cost with inference-only evaluation. A corrected compute breakdown — splitting extractor inference (GPU) from schema optimizer (API) — is needed to show the 16-day plan is feasible.", "PROXY METRIC CIRCULAR REASONING: VRD (violation-rate delta) and CDCD (cross-document consistency delta) are computed on the same rolling document buffer that generated the mismatch signals that triggered revision. Any schema revision that addresses even a subset of buffer-specific violations will mechanically improve these metrics — including harmful revisions such as merging all confused types into one super-type. The paper must include an empirical validation experiment demonstrating that proxy metric improvements on the buffer predict F1 improvement on a sequestered held-out test split (using gold labels post-hoc only, not for revision decisions). Without this, the unsupervised validation mechanism has no demonstrated reliability.", "SYNTHETIC-ONLY EVALUATION: All 8 required benchmark evaluations use deliberately introduced schema contamination (type merge, split, label scramble, argument-type swap, boundary blur). This validates recovery from constructed mismatches but does not establish that the error-detection layer — especially context-conditioned contradiction detection — fires reliably on naturally occurring schema-ontology divergences. At minimum one real-world cross-domain transfer scenario should be added (e.g., ACE05-trained extractor deployed on GENIA biomedical NER, or ACE event types applied to WikiEvents argument definitions), comparing OSAFE against a non-adaptive baseline without synthetic contamination.", "SCHEMA OPTIMIZER MODEL SIZE ABLATION MISSING: Qwen3-72B is used as the schema optimizer. A reviewer will immediately ask: does the improvement come from the error-detection algorithm (OSAFE's core contribution) or simply from Qwen3-72B's ability to improve any type definition given examples? An ablation substituting Qwen3-7B, Llama-3-8B-Instruct, or a smaller model as the optimizer is needed to decouple the error-signal quality from raw LLM capability. Without this, the paper risks being read as 'give a very large LLM some confusion examples and ask it to rewrite the schema.'", "SAM-NER CONCURRENT WORK UNCITED: SAM-NER (arXiv:2605.03706, May 5, 2026) addresses zero-shot NER under schema shifts via semantic archetype mediation — projecting entities through domain-invariant archetypes before mapping to target types. It is not a direct competitor (uses frozen inference, no online revision, no type-definition modification), but it should be cited as concurrent work. Note: appeared 5 days before the review date; generator cannot be faulted, but the paper should acknowledge it before submission."]
Feedback: The Round 2 revision comprehensively addressed all six Round 1 issues. The positioning against DiZiNER, PARSE, SCIR, and GuideX is now precise and defensible. Five focused issues remain. The most critical are (1) and (2). (1) Fix the resource estimate by explicitly separating extractor inference (GPU, very cheap for GoLLIE-7B inference across 8 datasets — likely 20-50h A100 total) from schema optimizer (Qwen3-72B via API, zero GPU cost). Show that the 16-day plan is feasible using ~50h A100 equivalent, well within 200 H100-hours. The current estimates conflate inference-only evaluation with fine-tuning workloads and will fail a reviewer sanity check. (2) Add an explicit proxy-metric reliability experiment: after running OSAFE on each dataset, plot proxy metric improvement (VRD, CDCD, ACP) against actual F1 improvement on the test split. This correlation analysis — even in one section of the experiments — validates the unsupervised validation gate and preempts the strongest methodological objection. (3) Add one natural domain transfer experiment (no synthetic contamination): pick any cross-domain NER or event pair (e.g., ACE05→biomedical, TACRED→SciERC cross-domain RE) and show OSAFE improves over a frozen schema baseline. This grounds practical value beyond constructed mismatches. (4) Add schema optimizer ablation (Qwen3-72B vs. Qwen3-7B) to isolate the error-signal contribution. (5) Mention SAM-NER (arXiv:2605.03706) as concurrent work in a footnote. Issues (3)-(5) are relatively quick to address. Issues (1)-(2) are the gate to a pass verdict.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL — RESOURCE ESTIMATES UNCHANGED (Round 2 Issue 1 persists): The gpu_hours and timeline figures are byte-for-byte identical to Round 2. Manual (~250h A100, 4–6 months) and HIL (~350h A100, 5–7 weeks) satisfy compute (≤200h H100) but violate the 16-day deadline by 3–8×. Auto (~900h A100, 1–2 weeks) meets the timeline but consumes ~450h H100 — 2.25× the compute budget. No mode satisfies both hard constraints. The fix prescribed in Round 2 — separating GoLLIE-7B extractor inference (GPU, ~20–50h A100 total with vLLM batching across all 8 datasets × 5 severity levels) from Qwen3-72B schema optimizer (Anthropic/DeepSeek API, zero GPU cost) — was not implemented. A corrected HIL estimate of ~50h A100 (≈25h H100) with a 16-day wall-clock timeline is readily achievable and must be shown explicitly.", "CRITICAL — PROXY METRIC VALIDATION EXPERIMENT MISSING (Round 2 Issue 2 persists): The analytical experiments section describes only a signal reliability study (τ_sim calibration) and a convergence analysis. The correlation experiment prescribed in Round 2 — plotting per-dataset VRD+CDCD+ACP composite improvement against actual F1 improvement on a sequestered test split — is absent. Without this, the ≥2/3 commitment gate is unvalidated: a trivial revision (merge all confused types into one super-type) could mechanically improve all three proxy metrics while degrading test F1. This is the strongest methodological objection a reviewer will raise.", "SIGNIFICANT — SYNTHETIC-ONLY EVALUATION (Round 2 Issue 3 persists): All eight benchmark evaluations use deliberately introduced schema contamination. No natural cross-domain transfer experiment is included. The Round 2 reviewer explicitly asked for 'at minimum one real-world cross-domain transfer scenario (e.g., ACE05-trained extractor deployed on GENIA biomedical NER, or TACRED→SciERC cross-domain RE).' Without this, the error-detection layer's reliability on naturally occurring mismatches is undemonstrated, and the paper's claim of practical deployment utility is unsupported.", "SIGNIFICANT — SCHEMA OPTIMIZER ABLATION ABSENT (Round 2 Issue 4 persists): Qwen3-72B is used as the schema optimizer throughout. No ablation with Qwen3-7B or Llama-3-8B-Instruct is included. A reviewer will ask whether OSAFE's gains stem from the error-signal algorithm or simply from a 72B model's general instruction-following ability. Two datasets (e.g., ACE05 NER, TACRED RE) with optimizer size as a variable is sufficient.", "MINOR — SAM-NER NOT CITED (Round 2 Issue 5 persists): SAM-NER (arXiv:2605.03706, May 5 2026; verified as a real paper) addresses zero-shot NER under schema/domain shifts via semantic archetype mediation. It is a different approach (frozen inference, no online type-definition revision, no error-signal loop) and does not threaten OSAFE's novelty, but it must appear as a concurrent-work footnote before submission.", "NEW — SPT NOT CITED: Schema as Parameterized Tools (arXiv:2506.01276, ~June 2026) treats schemas as callable parameterized tools supporting schema retrieval, filling, and on-demand generation for universal IE across four tasks. This directly overlaps OSAFE's motivation (schema adaptability for IE) and must be cited and differentiated. SPT uses a tool-calling paradigm for static schema selection/generation — it does not perform online error-signal-driven type-definition revision — so OSAFE's approach is distinct. One sentence in the related work section is sufficient."]
Feedback: The Round 3 revision successfully preserved all six Round 1 fixes and made meaningful progress on proxy metric precision (VRD/CDCD/ACP with ≥2/3 commitment rule). However, the two most critical Round 2 issues remain completely unaddressed — the generator appears to have not changed the resource section or the experimental plan at all. To unblock passage, address these in priority order:

(1) **Fix the resource estimate NOW** — the numbers are wrong and unchanged. The actual compute cost is: GoLLIE-7B inference across 8 datasets × 5 severity levels × schema optimizer API calls ≈ 30–50h A100 (≈15–25h H100) for extractor inference with vLLM batching, plus zero GPU cost for Qwen3-72B calls via API. A HIL plan with 4–6 A100s runs in 10–14 days and uses <50h H100 total. Write a three-row table: component | GPU cost | API cost | wall-clock. This is a 30-minute fix that eliminates the paper's most obvious reviewability problem.

(2) **Add proxy metric correlation experiment** — after running OSAFE across all datasets, compute Spearman correlation between composite proxy improvement (VRD+CDCD+ACP) and gold F1 gain on sequestered test splits. Report per-task correlations. A correlation ≥ 0.65 validates the commitment gate; if lower, discuss what conditions weaken proxy reliability. This can be a half-page subsection in the experiments.

(3) **Add one natural transfer experiment** — deploy ACE05-fine-tuned GoLLIE on GENIA (biomedical NER, cross-domain, no synthetic contamination) and compare OSAFE vs. frozen schema. This requires one inference run per system and a one-paragraph write-up.

(4) **Optimizer ablation** — run Qwen3-72B vs. Qwen3-7B on ACE05 and TACRED. Add a two-row table to the ablation section.

(5) **Two citation additions** — SAM-NER (arXiv:2605.03706) and SPT (arXiv:2506.01276) as concurrent-work footnotes in §2. Two sentences total.


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
  "promptId": "a218549d-b1e7-4f25-9bd2-75f4f18cea0c",
  "type": "user",
  "uuid": "a796b200-51be-4c5e-9028-afeeee4c30dd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:06:58.112Z_

```json
{
  "parentUuid": "a796b200-51be-4c5e-9028-afeeee4c30dd",
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
  "uuid": "6090094e-bd99-4a7a-960d-9cdcc95571b7",
  "timestamp": "2026-05-10T08:06:58.112Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:06:58.112Z_

```json
{
  "parentUuid": "6090094e-bd99-4a7a-960d-9cdcc95571b7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d5ed2a2e-6a95-4eb5-8343-706ecb3aae3b",
  "timestamp": "2026-05-10T08:06:58.112Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
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
  "leafUuid": "d5ed2a2e-6a95-4eb5-8343-706ecb3aae3b",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reviewer Analysis of OSAFE Schema Adaptation Method",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:07:32.723Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this Round 4 submission of the OSAFE paper idea. The previous rounds have identified several critical issues, and I need to independently verify whether they've been addressed this time.

Key issues from Round 3 that needed fixing:
1. CRITICAL: Resource estimates unchanged (need ≤200 H100-hours AND ≤16 days)
2. CRITICAL: Proxy metric validation experiment missing
3. SIGNIFICANT: Synthetic-only evaluation (need natural cross-domain transfer)
4. SIGNIFICANT: Schema optimizer ablation absent
5. MINOR: SAM-NER not cited
6. NEW: SPT not cited

Let me first read the current submission carefully to see what changed, then do independent research to verify the claims.


Looking at the Round 4 submission, the resource estimates have been broken down more granularly with a detailed cost architecture note separating the GPU-bound GoLLIE-7B extractor from the API-bound Qwen3-72B schema optimizer. The component breakdown shows the extractor at roughly 20 H100-hours, the optimizer using API calls instead of GPU, and the natural transfer plus ablation experiments adding another 3.5 H100-hours, bringing the total to around 24 H100-hours—well under the 200-hour limit.

For the proxy metric validation, they've now included a proper correlation analysis using Spearman rank correlation between the composite proxy improvement and actual gold F1 gains on sequestered test splits, with a commit threshold of ρ ≥ 0.65, which directly resolves the earlier concern about signal reliability.

The natural transfer experiment is set up to take an ACE05-fine-tuned GoLLIE-7B extractor and evaluate it on GENIA biomedical data. Now I need to verify these claims independently—checking whether the resource estimates are realistic, the cited papers actually exist and are accurately described, and whether the benchmarks and novelty claims hold up under scrutiny. I'm noticing a major inconsistency here—SPT is supposedly from June 2026 with arXiv ID 2506.01276, but if today is May 10, 2026, that paper hasn't been submitted yet. The generator is citing a paper from the future, which is a serious problem. I need to verify these papers actually exist and check their descriptions against what's claimed in the review. I'll search for DiZiNER and SAM-NER first to confirm they're real, then try to find SPT—which shouldn't exist since it's dated June 2026. I should also look for other concurrent work on online schema adaptation and validate whether the computational estimates make sense.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5ed2a2e-6a95-4eb5-8343-706ecb3aae3b",
  "isSidechain": false,
  "requestId": "req_011CatYY5YY5V3QzjXS1LiSc",
  "type": "assistant",
  "uuid": "398a99aa-82e0-41ec-b125-b607769aec39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019yu697hixukpupkhEdTon6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18354,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2982,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18354
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

_source line 9 · 2026-05-10T08:07:32.820Z_

I'll conduct independent research to verify the claims in this Round 4 submission, checking whether all five previously flagged issues have been properly addressed and looking for any new problems.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "398a99aa-82e0-41ec-b125-b607769aec39",
  "isSidechain": false,
  "requestId": "req_011CatYY5YY5V3QzjXS1LiSc",
  "type": "assistant",
  "uuid": "c22026dc-9182-4f7b-b913-849317f51384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019yu697hixukpupkhEdTon6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18354,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2982,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18354
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

_source line 10 · 2026-05-10T08:07:37.273Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017EM7txdPnvHfrB8H7rwBiz`</summary>

```json
{
  "description": "Verify key cited papers and find concurrent works",
  "subagent_type": "Explore",
  "prompt": "I need you to search for and verify several papers cited in an ML research proposal about online schema adaptation for information extraction. For each paper, I need to know: (1) does it actually exist, (2) is the arXiv ID correct, (3) is the description accurate?\n\nPapers to verify:\n1. DiZiNER (arXiv:2604.15866, April 2026) - described as \"zero-shot NER using inter-model disagreement among 8 heterogeneous LLMs to refine task instructions — explicitly keeps the NER schema fixed across iterations, modifies surface-level instruction wording rather than the type ontology, requires 25-document batches from training data\"\n2. SAM-NER (arXiv:2605.03706, May 2026) - described as \"zero-shot NER under schema shifts via semantic archetype mediation — frozen LLM, maps entity mentions to domain-invariant archetypes, no online error-signal loop\"\n3. SPT (arXiv:2506.01276, June 2026) - described as \"schemas as callable parameterized tools for universal IE — static schema selection and filling without online error-signal-driven type-definition revision\"\n\nNote: Today's date is 2026-05-10. Pay special attention to whether SPT (June 2026) can possibly be real given today's date.\n\nAlso search for:\n4. GoLLIE (ICLR 2024) - does this exist and is it accessible for fine-tuning?\n5. SCIR (AAAI 2026) - \"self-correcting iterative refinement for IE with schema\"\n6. GuideX / GUIDEX ACL Findings 2025 - schema-guided zero-shot NER\n\nFor each paper, please use WebSearch to find and verify. Report: real/hallucinated, correct venue/date, whether description matches abstract.\n\nSearch queries to try:\n- \"DiZiNER zero-shot NER disagreement\" site:arxiv.org\n- \"SAM-NER semantic archetype\" site:arxiv.org\n- arxiv 2506.01276 schema parameterized tools IE\n- \"GoLLIE annotation guidelines zero-shot information extraction\" ICLR 2024\n- \"SCIR self-correcting iterative refinement information extraction AAAI 2026\"\n- \"GuideX guided synthetic data zero-shot information extraction ACL 2025\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c22026dc-9182-4f7b-b913-849317f51384",
  "isSidechain": false,
  "requestId": "req_011CatYY5YY5V3QzjXS1LiSc",
  "type": "assistant",
  "uuid": "af8943d8-9a69-4f0d-8209-ae1f682af5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019yu697hixukpupkhEdTon6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18354,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2982,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18354
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

_source line 11 · 2026-05-10T08:07:44.304Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SigkQJeiSRXsw1oQ7kN8JJ`</summary>

```json
{
  "description": "Search for concurrent work on test-time schema adaptation for IE",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a research paper proposal about \"online schema adaptation for information extraction at test time\" called OSAFE. I need to independently verify whether there are competing/concurrent works the generator may have missed.\n\nThe paper proposes: using a deployed IE model's own extraction inconsistencies (type contradictions, type confusion patterns, invalid extractions) as signals to iteratively revise schema type definitions at test time — without gold labels, training data, or multiple models.\n\nPlease search for concurrent work in May 2026 or earlier that might overlap:\n\n1. Search: \"test-time schema adaptation information extraction 2025 2026\" site:arxiv.org\n2. Search: \"online schema learning named entity recognition 2025 2026\"\n3. Search: \"schema evolution information extraction LLM 2026\"\n4. Search: \"schema ontology mismatch named entity recognition 2025 2026\" \n5. Search: \"self-adaptive schema information extraction 2025 2026\"\n6. Search: \"type definition revision zero-shot NER 2025 2026\"\n7. Search: site:paperswithcode.com zero-shot named entity recognition SOTA 2025 2026\n\nFor any papers you find that seem highly relevant, fetch the abstract and report:\n- Paper title\n- Authors\n- Venue / arXiv ID\n- Date\n- How similar it is to OSAFE\n- Whether it would threaten OSAFE's novelty claim\n\nAlso check paperswithcode for current SOTA on zero-shot NER to verify that the referenced baselines (GoLLIE, GuideX) are still competitive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af8943d8-9a69-4f0d-8209-ae1f682af5d6",
  "isSidechain": false,
  "requestId": "req_011CatYY5YY5V3QzjXS1LiSc",
  "type": "assistant",
  "uuid": "36febbfb-4baa-4a55-becf-e91d23a6bb83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019yu697hixukpupkhEdTon6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18354,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2982,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18354
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

_source line 12 · 2026-05-10T08:08:34.416Z_

<details><summary>↩ Tool result · `toolu_017EM7txdPnvHfrB8H7rwBiz`</summary>

```text
Perfect. Now I have comprehensive information. Let me compile the verification report:

## Paper Verification Report

### **1. DiZiNER (arXiv:2604.15866)**
**Status: REAL - Details verified**

- **Correct arXiv ID:** ✓ 2604.15866
- **Correct Venue/Date:** ✓ arXiv, submitted April 17, 2026
- **Description Accuracy:** 
  - ✓ "zero-shot NER using inter-model disagreement" — CORRECT
  - ✓ "8 heterogeneous LLMs" — CONFIRMED (specifically: mistral-small3.2:24b, gpt-oss:20b, phi4:14b, qwen3:14b, gemma3:12b, deepseek-r1:8b, llama3.1:8b, nemotron-nano:8b)
  - ✓ "refine task instructions" — CORRECT (supervisor LLM analyzes disagreements to refine instructions)
  - ✓ "keeps the NER schema fixed across iterations" — CORRECT (only modifies instruction wording, not the schema)
  - ✓ "requires 25-document batches" — CONFIRMED (15-25 samples per iteration optimal, paper states "25 samples")
  - ✓ "modifies surface-level instruction wording rather than the type ontology" — CORRECT methodology

---

### **2. SAM-NER (arXiv:2605.03706)**
**Status: REAL - Details verified**

- **Correct arXiv ID:** ✓ 2605.03706
- **Correct Venue/Date:** ✓ arXiv, submitted May 5, 2026; Also accepted to ACL 2026 Findings
- **Description Accuracy:**
  - ✓ "zero-shot NER under schema shifts" — CORRECT
  - ✓ "semantic archetype mediation" — CONFIRMED (core methodology)
  - ✓ "frozen LLM" — CONFIRMED (uses "constrained, definition-aligned inference with a frozen LLM")
  - ✓ "maps entity mentions to domain-invariant archetypes" — CORRECT (core mechanism)
  - ✗ "no online error-signal loop" — CORRECT (three-stage pipeline with no dynamic error feedback mechanism described)

---

### **3. SPT (arXiv:2506.01276)**
**Status: REAL but DATE PROBLEM - Claims June 2026, actually June 2, 2025**

- **Correct arXiv ID:** ✓ 2506.01276
- **Venue/Date Issue:** ⚠️ FLAGGED - Paper shows "arXiv:2506.01276v1 [cs.CL] 2 Jun 2025" (June 2, **2025**, not June 2026 as claimed in proposal)
  - The arXiv ID format indicates it's from **May 2025**, not June 2026
  - This is a past paper from over a year ago, NOT a future paper from June 2026
  - **This is a DATE HALLUCINATION in the proposal**
- **Description Accuracy:**
  - ✓ "schemas as callable parameterized tools for universal IE" — CORRECT
  - ✓ "static schema selection and filling without online error-signal-driven type-definition revision" — CORRECT (operates through schema retrieval, filling, and generation—no iterative revision mechanism)

---

### **4. GoLLIE (ICLR 2024)**
**Status: REAL - Details verified**

- **Correct Venue/Conference:** ✓ ICLR 2024 (published as conference paper)
- **Correct Title:** ✓ "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction"
- **Fine-tuning Available:** ✓ YES - Paper demonstrates fine-tuning approach; code available on GitHub (github.com/hitz-zentroa/GoLLIE)
- **Core Innovation:** Guidelines/annotation instructions as docstrings in Python classes to improve zero-shot IE generalization

---

### **5. SCIR (AAAI 2026)**
**Status: REAL - Details verified**

- **Correct Venue/Conference:** ✓ AAAI 2026 (Proceedings of the AAAI Conference on Artificial Intelligence)
- **Correct Title:** ✓ "SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema"
- **Description:** ✓ Self-correcting iterative refinement for IE with schema — ACCURATE
- **Core Features:** Dual-Path Self-Correcting module + Feedback-Driven Optimization for iterative refinement
- **Also on arXiv:** 2512.12337

---

### **6. GuideX / GUIDEX (ACL Findings 2025)**
**Status: REAL - Details verified**

- **Correct Conference/Venue:** ✓ ACL 2025 Findings (pages 24248–24262, Vienna, Austria)
- **Name Variant:** Both "GuideX" and "GUIDEX" used; official is "GUIDEX"
- **Correct Title:** ✓ "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction"
- **Schema-guided zero-shot NER:** ✓ YES - generates domain-specific schemas, infers guidelines, generates synthetically labeled instances
- **Code/Resources:** ✓ Available at GitHub (Neilus03/GUIDEX) and neilus03.github.io/guidex.com

---

## Summary of Issues Found

**HALLUCINATIONS DETECTED:**
1. **SPT (arxiv:2506.01276)** — The proposal claims this is "June 2026" but the paper was actually submitted **June 2, 2025** (over a year ago). The arXiv ID format (2506) indicates May 2025, not May 2026. This appears to be a **date hallucination or confusion** in the research proposal.

**VERIFICATION RESULTS:**
- **DiZiNER:** All claims verified as accurate
- **SAM-NER:** All claims verified as accurate  
- **SPT:** Methodology verified but date is WRONG (2025, not 2026)
- **GoLLIE:** Real, published, code available
- **SCIR:** Real, published at AAAI 2026
- **GuideX/GUIDEX:** Real, published at ACL 2025 Findings

---

Sources:
- [DiZiNER arXiv](https://arxiv.org/abs/2604.15866)
- [SAM-NER arXiv](https://arxiv.org/abs/2605.03706)
- [SPT arXiv](https://arxiv.org/abs/2506.01276)
- [GoLLIE OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9)
- [GoLLIE GitHub](https://github.com/hitz-zentroa/GoLLIE)
- [SCIR AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40326)
- [GUIDEX ACL Anthology](https://aclanthology.org/2025.findings-acl.1245/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af8943d8-9a69-4f0d-8209-ae1f682af5d6",
  "isSidechain": false,
  "promptId": "a218549d-b1e7-4f25-9bd2-75f4f18cea0c",
  "type": "user",
  "uuid": "f8987e97-a77d-4a81-9274-ab8847cbbf50",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search for and verify several papers cited in an ML research proposal about online schema adaptation for information extraction. For each paper, I need to know: (1) does it actually exist, (2) is the arXiv ID correct, (3) is the description accurate?\n\nPapers to verify:\n1. DiZiNER (arXiv:2604.15866, April 2026) - described as \"zero-shot NER using inter-model disagreement among 8 heterogeneous LLMs to refine task instructions — explicitly keeps the NER schema fixed across iterations, modifies surface-level instruction wording rather than the type ontology, requires 25-document batches from training data\"\n2. SAM-NER (arXiv:2605.03706, May 2026) - described as \"zero-shot NER under schema shifts via semantic archetype mediation — frozen LLM, maps entity mentions to domain-invariant archetypes, no online error-signal loop\"\n3. SPT (arXiv:2506.01276, June 2026) - described as \"schemas as callable parameterized tools for universal IE — static schema selection and filling without online error-signal-driven type-definition revision\"\n\nNote: Today's date is 2026-05-10. Pay special attention to whether SPT (June 2026) can possibly be real given today's date.\n\nAlso search for:\n4. GoLLIE (ICLR 2024) - does this exist and is it accessible for fine-tuning?\n5. SCIR (AAAI 2026) - \"self-correcting iterative refinement for IE with schema\"\n6. GuideX / GUIDEX ACL Findings 2025 - schema-guided zero-shot NER\n\nFor each paper, please use WebSearch to find and verify. Report: real/hallucinated, correct venue/date, whether description matches abstract.\n\nSearch queries to try:\n- \"DiZiNER zero-shot NER disagreement\" site:arxiv.org\n- \"SAM-NER semantic archetype\" site:arxiv.org\n- arxiv 2506.01276 schema parameterized tools IE\n- \"GoLLIE annotation guidelines zero-shot information extraction\" ICLR 2024\n- \"SCIR self-correcting iterative refinement information extraction AAAI 2026\"\n- \"GuideX guided synthetic data zero-shot information extraction ACL 2025\"",
    "agentId": "a436cfac1b720a6f0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have comprehensive information. Let me compile the verification report:\n\n## Paper Verification Report\n\n### **1. DiZiNER (arXiv:2604.15866)**\n**Status: REAL - Details verified**\n\n- **Correct arXiv ID:** ✓ 2604.15866\n- **Correct Venue/Date:** ✓ arXiv, submitted April 17, 2026\n- **Description Accuracy:** \n  - ✓ \"zero-shot NER using inter-model disagreement\" — CORRECT\n  - ✓ \"8 heterogeneous LLMs\" — CONFIRMED (specifically: mistral-small3.2:24b, gpt-oss:20b, phi4:14b, qwen3:14b, gemma3:12b, deepseek-r1:8b, llama3.1:8b, nemotron-nano:8b)\n  - ✓ \"refine task instructions\" — CORRECT (supervisor LLM analyzes disagreements to refine instructions)\n  - ✓ \"keeps the NER schema fixed across iterations\" — CORRECT (only modifies instruction wording, not the schema)\n  - ✓ \"requires 25-document batches\" — CONFIRMED (15-25 samples per iteration optimal, paper states \"25 samples\")\n  - ✓ \"modifies surface-level instruction wording rather than the type ontology\" — CORRECT methodology\n\n---\n\n### **2. SAM-NER (arXiv:2605.03706)**\n**Status: REAL - Details verified**\n\n- **Correct arXiv ID:** ✓ 2605.03706\n- **Correct Venue/Date:** ✓ arXiv, submitted May 5, 2026; Also accepted to ACL 2026 Findings\n- **Description Accuracy:**\n  - ✓ \"zero-shot NER under schema shifts\" — CORRECT\n  - ✓ \"semantic archetype mediation\" — CONFIRMED (core methodology)\n  - ✓ \"frozen LLM\" — CONFIRMED (uses \"constrained, definition-aligned inference with a frozen LLM\")\n  - ✓ \"maps entity mentions to domain-invariant archetypes\" — CORRECT (core mechanism)\n  - ✗ \"no online error-signal loop\" — CORRECT (three-stage pipeline with no dynamic error feedback mechanism described)\n\n---\n\n### **3. SPT (arXiv:2506.01276)**\n**Status: REAL but DATE PROBLEM - Claims June 2026, actually June 2, 2025**\n\n- **Correct arXiv ID:** ✓ 2506.01276\n- **Venue/Date Issue:** ⚠️ FLAGGED - Paper shows \"arXiv:2506.01276v1 [cs.CL] 2 Jun 2025\" (June 2, **2025**, not June 2026 as claimed in proposal)\n  - The arXiv ID format indicates it's from **May 2025**, not June 2026\n  - This is a past paper from over a year ago, NOT a future paper from June 2026\n  - **This is a DATE HALLUCINATION in the proposal**\n- **Description Accuracy:**\n  - ✓ \"schemas as callable parameterized tools for universal IE\" — CORRECT\n  - ✓ \"static schema selection and filling without online error-signal-driven type-definition revision\" — CORRECT (operates through schema retrieval, filling, and generation—no iterative revision mechanism)\n\n---\n\n### **4. GoLLIE (ICLR 2024)**\n**Status: REAL - Details verified**\n\n- **Correct Venue/Conference:** ✓ ICLR 2024 (published as conference paper)\n- **Correct Title:** ✓ \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\"\n- **Fine-tuning Available:** ✓ YES - Paper demonstrates fine-tuning approach; code available on GitHub (github.com/hitz-zentroa/GoLLIE)\n- **Core Innovation:** Guidelines/annotation instructions as docstrings in Python classes to improve zero-shot IE generalization\n\n---\n\n### **5. SCIR (AAAI 2026)**\n**Status: REAL - Details verified**\n\n- **Correct Venue/Conference:** ✓ AAAI 2026 (Proceedings of the AAAI Conference on Artificial Intelligence)\n- **Correct Title:** ✓ \"SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema\"\n- **Description:** ✓ Self-correcting iterative refinement for IE with schema — ACCURATE\n- **Core Features:** Dual-Path Self-Correcting module + Feedback-Driven Optimization for iterative refinement\n- **Also on arXiv:** 2512.12337\n\n---\n\n### **6. GuideX / GUIDEX (ACL Findings 2025)**\n**Status: REAL - Details verified**\n\n- **Correct Conference/Venue:** ✓ ACL 2025 Findings (pages 24248–24262, Vienna, Austria)\n- **Name Variant:** Both \"GuideX\" and \"GUIDEX\" used; official is \"GUIDEX\"\n- **Correct Title:** ✓ \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\"\n- **Schema-guided zero-shot NER:** ✓ YES - generates domain-specific schemas, infers guidelines, generates synthetically labeled instances\n- **Code/Resources:** ✓ Available at GitHub (Neilus03/GUIDEX) and neilus03.github.io/guidex.com\n\n---\n\n## Summary of Issues Found\n\n**HALLUCINATIONS DETECTED:**\n1. **SPT (arxiv:2506.01276)** — The proposal claims this is \"June 2026\" but the paper was actually submitted **June 2, 2025** (over a year ago). The arXiv ID format (2506) indicates May 2025, not May 2026. This appears to be a **date hallucination or confusion** in the research proposal.\n\n**VERIFICATION RESULTS:**\n- **DiZiNER:** All claims verified as accurate\n- **SAM-NER:** All claims verified as accurate  \n- **SPT:** Methodology verified but date is WRONG (2025, not 2026)\n- **GoLLIE:** Real, published, code available\n- **SCIR:** Real, published at AAAI 2026\n- **GuideX/GUIDEX:** Real, published at ACL 2025 Findings\n\n---\n\nSources:\n- [DiZiNER arXiv](https://arxiv.org/abs/2604.15866)\n- [SAM-NER arXiv](https://arxiv.org/abs/2605.03706)\n- [SPT arXiv](https://arxiv.org/abs/2506.01276)\n- [GoLLIE OpenReview](https://openreview.net/forum?id=Y3wpuxd7u9)\n- [GoLLIE GitHub](https://github.com/hitz-zentroa/GoLLIE)\n- [SCIR AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40326)\n- [GUIDEX ACL Anthology](https://aclanthology.org/2025.findings-acl.1245/)"
      }
    ],
    "totalDurationMs": 57135,
    "totalTokens": 29448,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 698,
      "cache_creation_input_tokens": 1498,
      "cache_read_input_tokens": 25436,
      "output_tokens": 1816,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 698,
          "output_tokens": 1816,
          "cache_read_input_tokens": 25436,
          "cache_creation_input_tokens": 1498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1498,
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
  "sourceToolAssistantUUID": "af8943d8-9a69-4f0d-8209-ae1f682af5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f8987e97-a77d-4a81-9274-ab8847cbbf50",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Reviewer Analysis of OSAFE Schema Adaptation Method",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Tool result

_source line 15 · 2026-05-10T08:09:18.827Z_

<details><summary>↩ Tool result · `toolu_01SigkQJeiSRXsw1oQ7kN8JJ`</summary>

```text
Perfect. Now I have comprehensive coverage. Let me compile my findings into a structured report for the user.

## Research Competition Analysis: OSAFE (Online Schema Adaptation for Information Extraction)

Based on a systematic search of recent arxiv publications (2025-2026) and Papers with Code, I've identified several concurrent or near-concurrent works that overlap with OSAFE's core claims. Here's my assessment:

### HIGHEST NOVELTY THREATS

#### 1. **DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition**
- **ArXiv ID**: 2604.15866 (April 2026)
- **Key Concern**: Published in the same month as OSAFE's proposal window
- **Overlap**: Uses inter-model disagreements (analogous to extraction inconsistencies) to refine task instructions, achieving state-of-the-art on 14/18 benchmarks (+8.0 F1)
- **Critical Difference**: Refines instructions, not schema type definitions; uses multiple heterogeneous models rather than single model's contradictions
- **Threat Assessment**: MODERATE - Similar use of disagreement signals, but targets instruction space rather than schema type space

#### 2. **SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition**
- **ArXiv ID**: 2605.03706 (May 2026)
- **Key Concern**: Simultaneously published, directly addresses schema shift brittleness
- **Overlap**: Explicitly targets "unseen label definitions often misalign with LLM's intrinsic semantic organization"; uses three-stage framework including "Semantic Calibration" for definition-aligned inference
- **Approach**: Uses universal semantic archetypes as intermediaries + constrained inference with frozen LLM
- **Threat Assessment**: MODERATE-TO-HIGH - Directly handles schema/type definition mismatch at test time but through archetype mapping rather than type revision

#### 3. **PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction**
- **ArXiv ID**: 2510.08623 (October 2025)
- **Key Concern**: Pre-dated OSAFE by ~6 months; directly optimizes JSON schemas
- **Overlap**: Treats schemas as "dynamically improvable contracts"; uses two components (ARCHITECT for schema refinement, SCOPE for reflection-based extraction with guardrails)
- **Approach**: Autonomously refines JSON schemas for LLM comprehension while maintaining backward compatibility; achieves 64.7% accuracy improvements
- **Threat Assessment**: HIGH - Very similar core concept (schema optimization), but target is developer-facing schema contracts rather than type definitions

#### 4. **Adaptive Schema-aware Event Extraction (ASEE)**
- **ArXiv ID**: 2505.08690 (May 2025)
- **Key Concern**: Earlier work on adaptive schemas
- **Overlap**: Addresses "rigid schema fixation in existing pipeline systems"; dynamically retrieves paraphrased schemas at test time via RAG
- **Approach**: Schema retrieval-augmented generation from a pool of candidates
- **Threat Assessment**: MODERATE - Achieves schema adaptation but through retrieval rather than revision; different mechanism than OSAFE

### SECONDARY OVERLAPS (Partial Relevance)

#### 5. **Schema as Parameterized Tools for Universal Information Extraction (SPT)**
- **ArXiv ID**: 2506.01276 (May 2026)
- **Overlap**: Handles adaptive IE through schema retrieval, filling, and generation
- **Scope**: Broader framework (open, closed, on-demand IE) rather than focused on contradiction-driven type revision
- **Threat Assessment**: LOW-TO-MODERATE - Different framing (tool-calling) and no explicit use of extraction contradictions

#### 6. **GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction**
- **ArXiv ID**: 2506.00649 (May 2026, ACL Findings 2025)
- **Overlap**: Automatically infers domain-specific schemas and generates guidelines
- **Key Difference**: Schema inference is pre-training, not test-time; uses synthetic data generation rather than contradiction signals
- **Threat Assessment**: LOW - Different stage (training vs. test-time) and mechanism (synthetic data vs. contradictions)

### BASELINE COMPETITIVE STATUS

You asked about GoLLIE and GuideX baseline competitiveness:

- **GoLLIE** (ICLR 2024): Still competitive (~58.0 F1) but surpassed by GLiNER-L (60.9 F1 on out-of-domain NER)
- **GuideX** (ACL Findings 2025): Claims SOTA on seven zero-shot NER benchmarks, gaining up to 7 F1 points over prior methods

**Baseline Assessment**: If OSAFE claims to outperform these, benchmark improvement margins would be important for novelty claims.

### CLOSELY RELATED BUT ORTHOGONAL WORK

- **NER Retriever** (2509.04011): Uses type-aware embeddings but static type definitions (no revision)
- **CMAS** (2502.18702): Multi-agent zero-shot NER but no schema/type adaptation
- **A Reasoning Paradigm for NER** (2511.11978): Chain-of-thought reasoning with fixed schemas

### THREAT SUMMARY FOR OSAFE'S NOVELTY

**Core OSAFE Claims at Risk:**
1. Using deployed model's extraction contradictions to guide schema adaptation — **threatened by DiZiNER (disagreement signals) and SAM-NER (definition-aligned inference at test time)**
2. Revising type definitions without gold labels/training data — **somewhat threatened by GuideX (automatic schema inference) and PARSE (autonomous schema refinement)**
3. Iterative test-time refinement — **competed with by SAM-NER, ASEE, and test-time adaptation literature**

**OSAFE's Potential Differentiators (to verify):**
- Focus specifically on **type contradiction patterns** (e.g., same slot assigned incompatible types)
- Single-model signals (using own extractions) vs. multi-model disagreements
- Type **definition** revision (not schema structure, not instruction refinement)
- No external data, no training, no LLM calls during test-time adaptation

### RECOMMENDATIONS FOR GENERATOR

1. **Emphasize mechanism specificity**: If OSAFE uses novel signal patterns (type confusions, invalid extractions) that prior work doesn't explicitly target, highlight this
2. **Verify timing**: Confirm whether concurrent works (DiZiNER, SAM-NER, GuideX) were on arXiv pre-OSAFE submission
3. **Benchmark positioning**: OSAFE should clearly outperform or address failure modes of PARSE, GuideX, and SAM-NER on identical tasks
4. **Single-model claim**: Emphasize that using a single deployed model's contradictions (vs. multi-model disagreement or RAG retrieval) is the differentiator

---

**Sources:**
- [DiZiNER - arXiv 2604.15866](https://arxiv.org/abs/2604.15866)
- [SAM-NER - arXiv 2605.03706](https://arxiv.org/abs/2605.03706)
- [PARSE - arXiv 2510.08623](https://arxiv.org/abs/2510.08623)
- [Adaptive Schema-aware Event Extraction - arXiv 2505.08690](https://arxiv.org/abs/2505.08690)
- [Schema as Parameterized Tools - arXiv 2506.01276](https://arxiv.org/abs/2506.01276)
- [GuideX - arXiv 2506.00649](https://arxiv.org/abs/2506.00649)
- [NER Retriever - arXiv 2509.04011](https://arxiv.org/abs/2509.04011)
- [CMAS - arXiv 2502.18702](https://arxiv.org/abs/2502.18702)
- [GoLLIE - ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36febbfb-4baa-4a55-becf-e91d23a6bb83",
  "isSidechain": false,
  "promptId": "a218549d-b1e7-4f25-9bd2-75f4f18cea0c",
  "type": "user",
  "uuid": "4db79353-7338-4acc-bef6-215d0f1725a2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research paper proposal about \"online schema adaptation for information extraction at test time\" called OSAFE. I need to independently verify whether there are competing/concurrent works the generator may have missed.\n\nThe paper proposes: using a deployed IE model's own extraction inconsistencies (type contradictions, type confusion patterns, invalid extractions) as signals to iteratively revise schema type definitions at test time — without gold labels, training data, or multiple models.\n\nPlease search for concurrent work in May 2026 or earlier that might overlap:\n\n1. Search: \"test-time schema adaptation information extraction 2025 2026\" site:arxiv.org\n2. Search: \"online schema learning named entity recognition 2025 2026\"\n3. Search: \"schema evolution information extraction LLM 2026\"\n4. Search: \"schema ontology mismatch named entity recognition 2025 2026\" \n5. Search: \"self-adaptive schema information extraction 2025 2026\"\n6. Search: \"type definition revision zero-shot NER 2025 2026\"\n7. Search: site:paperswithcode.com zero-shot named entity recognition SOTA 2025 2026\n\nFor any papers you find that seem highly relevant, fetch the abstract and report:\n- Paper title\n- Authors\n- Venue / arXiv ID\n- Date\n- How similar it is to OSAFE\n- Whether it would threaten OSAFE's novelty claim\n\nAlso check paperswithcode for current SOTA on zero-shot NER to verify that the referenced baselines (GoLLIE, GuideX) are still competitive.",
    "agentId": "a5906acd5b8d486c3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have comprehensive coverage. Let me compile my findings into a structured report for the user.\n\n## Research Competition Analysis: OSAFE (Online Schema Adaptation for Information Extraction)\n\nBased on a systematic search of recent arxiv publications (2025-2026) and Papers with Code, I've identified several concurrent or near-concurrent works that overlap with OSAFE's core claims. Here's my assessment:\n\n### HIGHEST NOVELTY THREATS\n\n#### 1. **DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition**\n- **ArXiv ID**: 2604.15866 (April 2026)\n- **Key Concern**: Published in the same month as OSAFE's proposal window\n- **Overlap**: Uses inter-model disagreements (analogous to extraction inconsistencies) to refine task instructions, achieving state-of-the-art on 14/18 benchmarks (+8.0 F1)\n- **Critical Difference**: Refines instructions, not schema type definitions; uses multiple heterogeneous models rather than single model's contradictions\n- **Threat Assessment**: MODERATE - Similar use of disagreement signals, but targets instruction space rather than schema type space\n\n#### 2. **SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition**\n- **ArXiv ID**: 2605.03706 (May 2026)\n- **Key Concern**: Simultaneously published, directly addresses schema shift brittleness\n- **Overlap**: Explicitly targets \"unseen label definitions often misalign with LLM's intrinsic semantic organization\"; uses three-stage framework including \"Semantic Calibration\" for definition-aligned inference\n- **Approach**: Uses universal semantic archetypes as intermediaries + constrained inference with frozen LLM\n- **Threat Assessment**: MODERATE-TO-HIGH - Directly handles schema/type definition mismatch at test time but through archetype mapping rather than type revision\n\n#### 3. **PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction**\n- **ArXiv ID**: 2510.08623 (October 2025)\n- **Key Concern**: Pre-dated OSAFE by ~6 months; directly optimizes JSON schemas\n- **Overlap**: Treats schemas as \"dynamically improvable contracts\"; uses two components (ARCHITECT for schema refinement, SCOPE for reflection-based extraction with guardrails)\n- **Approach**: Autonomously refines JSON schemas for LLM comprehension while maintaining backward compatibility; achieves 64.7% accuracy improvements\n- **Threat Assessment**: HIGH - Very similar core concept (schema optimization), but target is developer-facing schema contracts rather than type definitions\n\n#### 4. **Adaptive Schema-aware Event Extraction (ASEE)**\n- **ArXiv ID**: 2505.08690 (May 2025)\n- **Key Concern**: Earlier work on adaptive schemas\n- **Overlap**: Addresses \"rigid schema fixation in existing pipeline systems\"; dynamically retrieves paraphrased schemas at test time via RAG\n- **Approach**: Schema retrieval-augmented generation from a pool of candidates\n- **Threat Assessment**: MODERATE - Achieves schema adaptation but through retrieval rather than revision; different mechanism than OSAFE\n\n### SECONDARY OVERLAPS (Partial Relevance)\n\n#### 5. **Schema as Parameterized Tools for Universal Information Extraction (SPT)**\n- **ArXiv ID**: 2506.01276 (May 2026)\n- **Overlap**: Handles adaptive IE through schema retrieval, filling, and generation\n- **Scope**: Broader framework (open, closed, on-demand IE) rather than focused on contradiction-driven type revision\n- **Threat Assessment**: LOW-TO-MODERATE - Different framing (tool-calling) and no explicit use of extraction contradictions\n\n#### 6. **GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction**\n- **ArXiv ID**: 2506.00649 (May 2026, ACL Findings 2025)\n- **Overlap**: Automatically infers domain-specific schemas and generates guidelines\n- **Key Difference**: Schema inference is pre-training, not test-time; uses synthetic data generation rather than contradiction signals\n- **Threat Assessment**: LOW - Different stage (training vs. test-time) and mechanism (synthetic data vs. contradictions)\n\n### BASELINE COMPETITIVE STATUS\n\nYou asked about GoLLIE and GuideX baseline competitiveness:\n\n- **GoLLIE** (ICLR 2024): Still competitive (~58.0 F1) but surpassed by GLiNER-L (60.9 F1 on out-of-domain NER)\n- **GuideX** (ACL Findings 2025): Claims SOTA on seven zero-shot NER benchmarks, gaining up to 7 F1 points over prior methods\n\n**Baseline Assessment**: If OSAFE claims to outperform these, benchmark improvement margins would be important for novelty claims.\n\n### CLOSELY RELATED BUT ORTHOGONAL WORK\n\n- **NER Retriever** (2509.04011): Uses type-aware embeddings but static type definitions (no revision)\n- **CMAS** (2502.18702): Multi-agent zero-shot NER but no schema/type adaptation\n- **A Reasoning Paradigm for NER** (2511.11978): Chain-of-thought reasoning with fixed schemas\n\n### THREAT SUMMARY FOR OSAFE'S NOVELTY\n\n**Core OSAFE Claims at Risk:**\n1. Using deployed model's extraction contradictions to guide schema adaptation — **threatened by DiZiNER (disagreement signals) and SAM-NER (definition-aligned inference at test time)**\n2. Revising type definitions without gold labels/training data — **somewhat threatened by GuideX (automatic schema inference) and PARSE (autonomous schema refinement)**\n3. Iterative test-time refinement — **competed with by SAM-NER, ASEE, and test-time adaptation literature**\n\n**OSAFE's Potential Differentiators (to verify):**\n- Focus specifically on **type contradiction patterns** (e.g., same slot assigned incompatible types)\n- Single-model signals (using own extractions) vs. multi-model disagreements\n- Type **definition** revision (not schema structure, not instruction refinement)\n- No external data, no training, no LLM calls during test-time adaptation\n\n### RECOMMENDATIONS FOR GENERATOR\n\n1. **Emphasize mechanism specificity**: If OSAFE uses novel signal patterns (type confusions, invalid extractions) that prior work doesn't explicitly target, highlight this\n2. **Verify timing**: Confirm whether concurrent works (DiZiNER, SAM-NER, GuideX) were on arXiv pre-OSAFE submission\n3. **Benchmark positioning**: OSAFE should clearly outperform or address failure modes of PARSE, GuideX, and SAM-NER on identical tasks\n4. **Single-model claim**: Emphasize that using a single deployed model's contradictions (vs. multi-model disagreement or RAG retrieval) is the differentiator\n\n---\n\n**Sources:**\n- [DiZiNER - arXiv 2604.15866](https://arxiv.org/abs/2604.15866)\n- [SAM-NER - arXiv 2605.03706](https://arxiv.org/abs/2605.03706)\n- [PARSE - arXiv 2510.08623](https://arxiv.org/abs/2510.08623)\n- [Adaptive Schema-aware Event Extraction - arXiv 2505.08690](https://arxiv.org/abs/2505.08690)\n- [Schema as Parameterized Tools - arXiv 2506.01276](https://arxiv.org/abs/2506.01276)\n- [GuideX - arXiv 2506.00649](https://arxiv.org/abs/2506.00649)\n- [NER Retriever - arXiv 2509.04011](https://arxiv.org/abs/2509.04011)\n- [CMAS - arXiv 2502.18702](https://arxiv.org/abs/2502.18702)\n- [GoLLIE - ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf)"
      }
    ],
    "totalDurationMs": 94518,
    "totalTokens": 34661,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 931,
      "cache_creation_input_tokens": 1541,
      "cache_read_input_tokens": 30181,
      "output_tokens": 2008,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 931,
          "output_tokens": 2008,
          "cache_read_input_tokens": 30181,
          "cache_creation_input_tokens": 1541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1541,
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
  "sourceToolAssistantUUID": "36febbfb-4baa-4a55-becf-e91d23a6bb83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T08:10:39.534Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key information I need to formulate my review. Let me analyze what I found:

**Critical Finding: SPT Date Hallucination**
- SPT (arXiv:2506.01276) was submitted on June 2, **2025**, not June 2026 as the generator claims
- In the arXiv ID system, 2506 = May 2025 (submitted May/June 2025)
- Today is May 10, 2026, so this paper is actually from **over a year ago** - not a concurrent June 2026 paper
- The generator classified this as "concurrent work" from June 2026, but it's actually from June 2025 (a year old)


- This means SPT is prior work, not concurrent work, which significantly affects the novelty analysis and represents a clear factual error in the proposal.
- The same issue applies to ASEE (arXiv:2505.08690) - it's from May 2025, making it another prior work that should be compared against rather than dismissed as concurrent. I'm realizing both papers are from 2025, not 2026 — the arXiv ID format YYMM.NNNNN shows 2505 is May 2025 and 2506 is June 2025. The generator made a critical error by dating SPT as "June 2026" when it's actually from June 2025, which means it should be treated as prior work rather than concurrent research and likely belongs in the related work section.

Beyond the date confusion, ASEE from May 2025 on adaptive schemas for event extraction via RAG looks like a genuine gap in the prior work coverage. Looking at the broader revisions, the resource estimates have been properly corrected to separate the GPU-based GoLLIE inference from the API-based Qwen optimizer, the proxy metrics now include explicit correlation thresholds, and they've added both the cross-domain transfer experiment and the optimizer ablation study. The SPT date discrepancy is more serious than I initially thought—if it's actually from June 2025, then it's prior work that the proposal should either baseline against or explain why it's not directly comparable, rather than treating it as concurrent work. ASEE presents a similar problem: if this adaptive schema paper for event extraction actually exists, it's a direct methodological overlap that needs to be addressed, either through citation or by clarifying how OSAFE's approach differs. The arXiv ID format confirms this is June 2025, not 2026 as the generator stated—a clear factual error that a reviewer would catch immediately, though the conceptual differentiation between OSAFE's error-signal-driven approach and SPT's tool-calling mechanism still holds up. This credibility issue doesn't invalidate the core novelty, but it does raise questions about the thoroughness of the research landscape review.

Looking at the bigger picture, Round 4 has successfully tackled the major issues from before—the resource estimates are now grounded, the proxy metrics are validated, and new experiments like the natural transfer study and optimizer ablation strengthen the work. The remaining gaps are relatively minor: fixing the SPT date and potentially adding ASEE as a prior work citation if it genuinely addresses adaptive schema-aware extraction. With the five critical issues from Round 3 resolved and the novelty positioning well-differentiated, the paper is in much stronger shape despite these lingering details. estimates are now correct and meet both hard constraints, and the experimental plan is comprehensive. This feels like a borderline pass—the core idea is solid and major issues are resolved, though the SPT date error and potentially missed ASEE citation are concerning.

Scoring across dimensions: novelty is strong at 4/5 with clear differentiation from related work despite the date confusion, feasibility checks out at 4/5 with validated resource estimates and proper ablations, clarity is solid at 4/5 with well-specified stages, and impact is 4/5 addressing a real deployment problem across multiple tasks and benchmarks. That averages to 4.0, right at the threshold.

The SPT date mistake is embarrassing, but reconsidering it—the conceptual differentiation still holds since SPT uses tool-calling for static selection while this approach does online error-signal-driven revision, so it's really just a reference typo rather than a conceptual flaw. Given that the issues are now minor enough to address in a lighter revision round, I'm leaning toward a revise verdict rather than reject. The ASEE paper (arXiv:2505.08690):
- It was described as "dynamically retrieves paraphrased schemas at test time via RAG"
- This is different from OSAFE's error-detection + revision approach
- It's for event extraction specifically
- But it does address test-time schema adaptation, which overlaps with OSAFE's claims

For an EMNLP 2026 submission at the "solid" level, these are relatively minor issues. The main question is: is this ready to submit, or does it need one more revision?

I think it's borderline. The five major issues from Round 3 are all addressed. The remaining issues are:
1. SPT date typo (easy fix, doesn't threaten novelty)
2. ASEE possibly missed (needs verification and potentially a citation)

I'll go with "revise" for one more round because the SPT date error needs correction and changes how we frame it relative to prior work, ASEE should be checked and potentially cited, and we should verify whether SPT warrants inclusion as a baseline. These are genuinely minor issues that can be addressed quickly.

Actually, reconsidering whether to pass instead. The average score would be around 4.0, and "pass" means the idea is sound with high quality and no critical issues. The SPT date error and ASEE omission aren't critical—they're just citation corrections. The core paper is solid, and the main experimental concerns from previous rounds have been resolved. But the ASEE paper deserves closer attention since it also tackles test-time schema adaptation through RAG-based retrieval, which does overlap with OSAFE's approach.

I can't independently verify whether ASEE is real without another search, so I'll assume the agent's finding is reliable. If it exists, it uses a different mechanism than OSAFE (RAG retrieval versus error-signal-driven revision), and OSAFE still covers more ground with relation extraction and NER alongside events. My final verdict is to revise once more to address these points cleanly.

The core issues remaining are straightforward: the SPT paper is from June 2025, not 2026, and ASEE represents potential prior work on adaptive schema event extraction that needs proper positioning. These aren't deal-breakers, but a real reviewer would catch them immediately. Looking at the scores across novelty, feasibility, clarity, and impact—all sitting around 4/5—the paper is genuinely strong with just these citation details to clean up.

The SPT date error particularly concerns me because it's not just a typo; it fundamentally changes how the work is framed relative to existing literature. When reviewers verify the reference and find it's actually concurrent work from June 2025, they'll question the rigor of the literature review. That kind of discrepancy tends to trigger rejections even when the core contribution is solid.

I think one more revision round focused specifically on these citation issues should get this across the finish line.

Now I'm reconsidering whether ASEE is actually relevant to include. The second agent described it as using RAG to retrieve pre-existing schema paraphrases at test time, which is mechanistically different from OSAFE's approach of generating new type definitions based on extraction errors. The key distinction is that ASEE works with a fixed pool of schema variants while OSAFE learns from feedback signals, so they're addressing the schema rigidity problem through different mechanisms.

But this raises a real concern: if ASEE is working in the exact same space of event extraction with adaptive schemas, omitting it could be a significant gap in the related work, especially if the paper claims novelty in schema adaptation. Combined with the SPT date error, I'm leaning toward asking for a revision rather than accepting as-is. These aren't critical flaws, but they're the kind of issues that undermine confidence in the paper's thoroughness.

Let me finalize my verdict: revise with targeted feedback on the SPT date correction and the ASEE citation. The paper is nearly there—just needs these two specific fixes. Then I'll score the revised version more carefully, looking at novelty and feasibility against the corrected prior work landscape. The fixes are straightforward enough to handle in a day, so one more revision cycle should push this to acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db79353-7338-4acc-bef6-215d0f1725a2",
  "isSidechain": false,
  "requestId": "req_011CatYiT5NJMDMdf9yFMoJu",
  "type": "assistant",
  "uuid": "9ef46385-4577-4e95-8653-558072785e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EM5M4j6uaZQU8sx6KVshp1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6858,
      "cache_read_input_tokens": 29985,
      "output_tokens": 5030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5030,
          "cache_read_input_tokens": 29985,
          "cache_creation_input_tokens": 6858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6858
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

_source line 17 · 2026-05-10T08:10:39.596Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019pk1DFXwSsZpirYzGSxqdh`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ef46385-4577-4e95-8653-558072785e8e",
  "isSidechain": false,
  "requestId": "req_011CatYiT5NJMDMdf9yFMoJu",
  "type": "assistant",
  "uuid": "bca3c140-4e36-452a-9862-739ff87ee3ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EM5M4j6uaZQU8sx6KVshp1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6858,
      "cache_read_input_tokens": 29985,
      "output_tokens": 5030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5030,
          "cache_read_input_tokens": 29985,
          "cache_creation_input_tokens": 6858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6858
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

_source line 18 · 2026-05-10T08:10:39.606Z_

<details><summary>↩ Tool result · `toolu_019pk1DFXwSsZpirYzGSxqdh`</summary>

````text
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
  "parentUuid": "bca3c140-4e36-452a-9862-739ff87ee3ec",
  "isSidechain": false,
  "promptId": "a218549d-b1e7-4f25-9bd2-75f4f18cea0c",
  "type": "user",
  "uuid": "2f65f29c-c2dd-434b-8fc9-90dd7826f267",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "bca3c140-4e36-452a-9862-739ff87ee3ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
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
  "leafUuid": "2f65f29c-c2dd-434b-8fc9-90dd7826f267",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Reviewer Analysis of OSAFE Schema Adaptation Method",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Assistant

_source line 21 · 2026-05-10T08:10:41.802Z_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the SPT paper date and the ASEE paper by fetching their arXiv pages directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f65f29c-c2dd-434b-8fc9-90dd7826f267",
  "isSidechain": false,
  "requestId": "req_011CatYpQW1JqJjENoD153Mm",
  "type": "assistant",
  "uuid": "6230b19e-f04d-4b78-b9e3-b02214077d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XtMuZE4fWkKHXWppbXEhD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 36843,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 36843,
          "cache_creation_input_tokens": 5542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5542
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

_source line 22 · 2026-05-10T08:10:42.538Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dv41H5jEWZ2QpYhYMyp4xK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.01276",
  "prompt": "What is the submission date of this paper? What is the title? What year was it submitted? Give me the exact date from the arXiv page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6230b19e-f04d-4b78-b9e3-b02214077d00",
  "isSidechain": false,
  "requestId": "req_011CatYpQW1JqJjENoD153Mm",
  "type": "assistant",
  "uuid": "544f00de-de63-48a2-b1e6-97c5955da6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XtMuZE4fWkKHXWppbXEhD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 36843,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 36843,
          "cache_creation_input_tokens": 5542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5542
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

_source line 23 · 2026-05-10T08:10:43.473Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AKaHnHxbB33iy5pZoJsKyk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.08690",
  "prompt": "What is this paper about? What is the title, authors, and submission date? Does it address adaptive or test-time schema adaptation for information extraction or event extraction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "544f00de-de63-48a2-b1e6-97c5955da6f4",
  "isSidechain": false,
  "requestId": "req_011CatYpQW1JqJjENoD153Mm",
  "type": "assistant",
  "uuid": "1a35a732-a52b-4316-9a97-18a3ee7c9a2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XtMuZE4fWkKHXWppbXEhD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 36843,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5542,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 36843,
          "cache_creation_input_tokens": 5542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5542
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

_source line 24 · 2026-05-10T08:10:44.298Z_

<details><summary>↩ Tool result · `toolu_01Dv41H5jEWZ2QpYhYMyp4xK`</summary>

```text
# Paper Submission Details

**Submission Date:** Monday, June 2, 2025 at 03:12:44 UTC

**Title:** "Schema as Parameterized Tools for Universal Information Extraction"

**Year:** 2025

The arXiv page indicates the paper was submitted on June 2, 2025, as shown in the submission history: "[v1] Mon, 2 Jun 2025 03:12:44 UTC"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "544f00de-de63-48a2-b1e6-97c5955da6f4",
  "isSidechain": false,
  "promptId": "a218549d-b1e7-4f25-9bd2-75f4f18cea0c",
  "type": "user",
  "uuid": "1bad3cea-98ae-4082-b9e8-278c9737e7ed",
  "toolUseResult": {
    "bytes": 46639,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Submission Details\n\n**Submission Date:** Monday, June 2, 2025 at 03:12:44 UTC\n\n**Title:** \"Schema as Parameterized Tools for Universal Information Extraction\"\n\n**Year:** 2025\n\nThe arXiv page indicates the paper was submitted on June 2, 2025, as shown in the submission history: \"[v1] Mon, 2 Jun 2025 03:12:44 UTC\"",
    "durationMs": 1758,
    "url": "https://arxiv.org/abs/2506.01276"
  },
  "sourceToolAssistantUUID": "544f00de-de63-48a2-b1e6-97c5955da6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T08:10:47.408Z_

<details><summary>↩ Tool result · `toolu_01AKaHnHxbB33iy5pZoJsKyk`</summary>

```text
# Paper Summary

**Title:** "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation"

**Authors:** Sheng Liang, Hang Lv, Zhihao Wen, Yaxiong Wu, Yongyue Zhang, Hao Wang, and Yong Liu

**Submission Date:** May 13, 2025

## Does it Address Adaptive Schema Adaptation?

Yes, directly. The paper proposes **ASEE** (Adaptive Schema-aware Event Extraction), which tackles schema selection dynamically. According to the abstract, the work addresses "two critical gaps: (1) the rigid schema fixation in existing pipeline systems, and (2) the absence of benchmarks for evaluating joint schema matching and extraction."

The approach combines "schema paraphrasing with schema retrieval-augmented generation" to adapt to varying scenarios rather than relying on fixed schemas. The authors also introduce the **MD-SEE benchmark** with "12 datasets across diverse domains, complexity levels, and language settings" to evaluate this adaptive capability, demonstrating the system's "strong adaptability across various scenarios."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a35a732-a52b-4316-9a97-18a3ee7c9a2b",
  "isSidechain": false,
  "promptId": "a218549d-b1e7-4f25-9bd2-75f4f18cea0c",
  "type": "user",
  "uuid": "a3b7f2e2-c53d-4486-938e-c96b7e0a004d",
  "toolUseResult": {
    "bytes": 47049,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** \"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation\"\n\n**Authors:** Sheng Liang, Hang Lv, Zhihao Wen, Yaxiong Wu, Yongyue Zhang, Hao Wang, and Yong Liu\n\n**Submission Date:** May 13, 2025\n\n## Does it Address Adaptive Schema Adaptation?\n\nYes, directly. The paper proposes **ASEE** (Adaptive Schema-aware Event Extraction), which tackles schema selection dynamically. According to the abstract, the work addresses \"two critical gaps: (1) the rigid schema fixation in existing pipeline systems, and (2) the absence of benchmarks for evaluating joint schema matching and extraction.\"\n\nThe approach combines \"schema paraphrasing with schema retrieval-augmented generation\" to adapt to varying scenarios rather than relying on fixed schemas. The authors also introduce the **MD-SEE benchmark** with \"12 datasets across diverse domains, complexity levels, and language settings\" to evaluate this adaptive capability, demonstrating the system's \"strong adaptability across various scenarios.\"",
    "durationMs": 3934,
    "url": "https://arxiv.org/abs/2505.08690"
  },
  "sourceToolAssistantUUID": "1a35a732-a52b-4316-9a97-18a3ee7c9a2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T08:11:06.937Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have confirmation of both issues:

1. **SPT (arXiv:2506.01276)**: Submitted June 2, **2025** (not June 2026). The generator lists this as "arXiv:2506.01276, June 2026" which is incorrect. It's from June 2025, so it's prior work, not concurrent work from June 2026.

2. **ASEE (arXiv:2505.08690)**: "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation" - submitted May 13, 2025. 

This paper directly tackles adaptive schema for event extraction through schema paraphrasing combined with RAG, and it's a real contribution the generator overlooked. Looking at my final review, I can see the key improvements made: resource estimates are now realistic with concrete numbers, proxy metric validation has been explicitly added with the Spearman ρ threshold tied to commitment gates, and there's a natural transfer experiment from ACE05 to GENIA bio.

Beyond those, I've added an optimizer ablation comparing model sizes on standard benchmarks, properly cited SAM-NER, but I'm noticing a critical dating error with SPT—arXiv:2506.01276 is from June 2025, not 2026, which means it's prior work that needs clearer differentiation rather than concurrent work. More importantly, ASEE from May 2025 is completely missing despite being directly relevant to adaptive schema-aware event extraction with RAG, so that's a significant gap that needs addressing. with the wrong date. arXiv:2506.01276 was submitted June 2, 2025 — it's prior work from a year before submission, not concurrent work from June 2026. The generator should correct the date and potentially include SPT in the baseline comparison. The methodology differentiation (tool-calling for static selection vs. error-signal-driven online revision) is still valid, so novelty is not threatened, but the mischaracterization of SPT as "concurrent" rather than "prior work" is a credibility problem.

Issue 2 (MODERATE): ASEE (arXiv:2505.08690, May 2025) is unaddressed. This paper directly addresses adaptive schema for event extraction via schema paraphrasing + RAG retrieval, introduces the MD-SEE benchmark, and addresses "rigid schema fixation in existing pipeline systems" — nearly identical framing to OSAFE's motivation for event extraction. The key difference is that ASEE relies on retrieving pre-existing schema paraphrases while OSAFE generates new type definitions directly from error signals, and ASEE lacks the feedback loop that drives OSAFE's online revision. This paper needs to be cited and properly differentiated, especially given the new MD-SEE benchmark it introduces.

Looking at the scoring, the core novelty holds at 4/5 — the online, single-extractor, error-signal-driven approach to type definition revision without gold labels remains genuinely novel, and while ASEE overlaps on motivation, the mechanisms are fundamentally different. Feasibility also stays at 4/5 with corrected resource estimates, and the 8-dataset × 5-severity evaluation with human-in-the-loop mode is achievable in the 10-14 day window, though it'll be tight.

The framework itself is well-specified and the analytical experiments are clearly motivated, so clarity remains at 4/5 despite the credibility hit from the SPT date error. Impact is also 4/5 — this addresses a real deployment problem with broad evaluation, and the event extraction evaluation especially benefits from including ASEE as a comparison point.

Overall, this lands at 4.0/5 with a verdict to revise. Both citation issues are fixable in half a day, and the core idea is solid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3b7f2e2-c53d-4486-938e-c96b7e0a004d",
  "isSidechain": false,
  "requestId": "req_011CatYpyGUiSJzBG9ekEYHT",
  "type": "assistant",
  "uuid": "f6669edd-1c67-41d6-923e-8c2d3883e7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NdN5B5V6CNzPHeecWoUuGD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 42385,
      "output_tokens": 2717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2717,
          "cache_read_input_tokens": 42385,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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

_source line 27 · 2026-05-10T08:11:32.079Z_

Now I have independent verification of both issues. Let me write my final verdict.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "The online, single-extractor, error-signal-driven type-definition revision mechanism (OSAFE) is genuinely distinct from DiZiNER (multi-LLM, instruction wording only), SAM-NER (frozen LLM + archetypes, no feedback loop), and SCIR (prediction refinement, fixed schema). However, two citation problems weaken the novelty case: SPT is misdated as June 2026 (it's June 2025 prior work), and ASEE (arXiv:2505.08690, May 2025) — an adaptive schema-aware event extraction paper using RAG schema retrieval that frames the problem in nearly identical terms — is unaddressed."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Round 4 properly separates GoLLIE-7B extractor inference (~40h A100, GPU) from Qwen3-72B schema optimizer (API, zero GPU cost), giving ~24h H100 total — well within budget. HIL mode at 10-14 days meets the 16-day deadline. The proxy metric correlation experiment, natural transfer (ACE05→GENIA), and optimizer ablation are all realistic additions."
    },
    "clarity": {
      "score": 4,
      "rationale": "The three-stage framework, commitment gate (≥2/3 proxy metrics), τ_sim calibration, and analytical experiments are precisely specified. The SPT date error (listed as 'June 2026' but actually June 2, 2025) is a factual mistake that undermines perceived rigor of the literature review."
    },
    "impact": {
      "score": 4,
      "rationale": "Schema-ontology mismatch at deployment time is a real, underaddressed problem; the zero-seed, single-extractor framing is practically valuable. Evaluation spanning 8 benchmarks across NER, event, and relation extraction is broad. The missed ASEE comparison slightly weakens the event extraction impact claim."
    }
  },
  "issues": [
    "SPT DATE ERROR — FACTUAL: arXiv:2506.01276 ('Schema as Parameterized Tools for Universal Information Extraction') was submitted June 2, 2025 (verified via arXiv), not 'June 2026' as the generator states. This is prior work published a year before OSAFE's submission, not concurrent work. The generator must (a) correct the date to June 2025, (b) reclassify SPT from 'concurrent work' to 'prior work' in the related-work framing, and (c) consider whether SPT warrants inclusion in the baseline comparison table — given SPT's broader IE framework with schema generation capabilities, a one-sentence justification for why it is not a direct evaluation baseline would preempt reviewer questions. The methodology differentiation (static tool-calling paradigm vs. online error-signal-driven type revision) is still valid, so this does not threaten novelty, but the date hallucination is a credibility-damaging factual error.",
    "ASEE UNCITED — MISSED PRIOR WORK: 'Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation' (arXiv:2505.08690, May 13, 2025) directly addresses 'rigid schema fixation in existing pipeline systems' — nearly identical framing to OSAFE's event extraction motivation — and uses schema paraphrasing combined with retrieval-augmented generation to dynamically adapt schemas at test time. It also introduces the MD-SEE benchmark (12 datasets across diverse domains). This is a real paper (verified via arXiv) that EMNLP IE reviewers familiar with event extraction will likely know. OSAFE must cite ASEE and differentiate in one to two sentences: ASEE retrieves from a pre-existing pool of schema paraphrases (no error signals, no type definition generation, no feedback loop), whereas OSAFE generates new type definitions from the extractor's own extraction error patterns online. The MD-SEE benchmark is worth noting as a potential future evaluation target."
  ],
  "feedback": "Round 4 has genuinely resolved all five Round 3 issues. The resource estimate is now correct and clearly structured (GoLLIE-7B inference ~40h A100 via vLLM + Qwen3-72B optimizer via API at zero GPU cost = ~24h H100 total; HIL mode 10-14 days with 4-6 A100s). The proxy metric correlation experiment (Spearman ρ ≥ 0.65 on sequestered test splits per task type) directly validates the commitment gate. The natural transfer experiment (ACE05-fine-tuned GoLLIE-7B → GENIA biomedical NER, 1,854 instances, no synthetic contamination) and optimizer ablation (Qwen3-72B vs. Qwen3-7B on ACE05+TACRED) are both realistic additions. SAM-NER and SPT are cited. Two targeted fixes remain before a pass verdict:\n\n(1) **Fix SPT date and reclassification**: Change 'arXiv:2506.01276, June 2026' to 'arXiv:2506.01276, June 2025' throughout. Move SPT from 'concurrent work' to 'prior work' in §2. Add one sentence explaining why SPT is not an evaluation baseline (e.g., 'SPT's schema tool-calling paradigm requires a schema library and static selection pipeline incompatible with our online streaming setting'). This is a 15-minute fix.\n\n(2) **Add ASEE citation**: In §2 related work, add one paragraph citing arXiv:2505.08690 as prior work on adaptive schema event extraction, differentiating it from OSAFE on three axes: (a) ASEE retrieves pre-existing schema paraphrases via RAG — no error signals generated; (b) no feedback loop or type definition generation — schema variants are fixed at setup time; (c) no multi-task coverage (NER, RE). One to two sentences is sufficient. This is a 20-minute fix.\n\nAfter these two corrections, the paper should be ready for a pass verdict. The core novelty is well-defended, the resource plan is now believable, and the experimental design is comprehensive.",
  "reason": "All five Round 3 critical/significant issues resolved; two moderate citation errors remain — SPT misdated as June 2026 (actually June 2025, prior work) and ASEE (arXiv:2505.08690, May 2025) on adaptive schema event extraction uncited — both fixable in under an hour."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6669edd-1c67-41d6-923e-8c2d3883e7e0",
  "isSidechain": false,
  "requestId": "req_011CatYpyGUiSJzBG9ekEYHT",
  "type": "assistant",
  "uuid": "8e051948-e03e-4704-aaaf-da51bc5041bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NdN5B5V6CNzPHeecWoUuGD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 42385,
      "output_tokens": 2717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2717,
          "cache_read_input_tokens": 42385,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8e051948-e03e-4704-aaaf-da51bc5041bf",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Reviewer Analysis of OSAFE Schema Adaptation Method",
  "sessionId": "7543766e-83be-44bc-b006-4c1b2c7a9b11"
}
```

---
